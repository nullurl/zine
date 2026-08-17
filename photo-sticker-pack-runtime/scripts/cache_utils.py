from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import tempfile
from typing import Iterable

from PIL import Image

from artifact_contract import canonical_write_paths
from manifest_utils import load_manifest, validate_manifest
from quality_gate import quality_report
from resume_utils import _valid_raw_image


CACHE_SCHEMA = "photo-sticker-pack-raw-v1"
VISUAL_KEYS = ("kind", "action", "accessory", "expression", "prompt")


def _file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        while chunk := source.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def cache_key(
    manifest: dict[str, object],
    row: dict[str, object],
    style_reference: Path,
) -> str:
    """Hash only the source/style/visual brief; captions remain locally replaceable."""
    source_path = manifest.get("source_path")
    if not isinstance(source_path, str) or not source_path:
        raise ValueError("manifest source_path is unavailable for caching")
    source = Path(source_path)
    style_reference = Path(style_reference)
    if not source.is_file() or not style_reference.is_file():
        raise FileNotFoundError("cache source and style reference must exist")
    subject = manifest.get("subject")
    if not isinstance(subject, dict):
        raise ValueError("manifest subject must be an object")
    payload = {
        "schema": CACHE_SCHEMA,
        "source_sha256": _file_digest(source),
        "style_sha256": _file_digest(style_reference),
        "visible_features": subject.get("visible_features", []),
        "visual": {key: row.get(key) for key in VISUAL_KEYS},
    }
    serialized = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(serialized).hexdigest()


def _entry_path(cache_dir: Path, key: str) -> Path:
    if len(key) != 64 or any(character not in "0123456789abcdef" for character in key):
        raise ValueError("cache key must be a SHA-256 hex digest")
    return Path(cache_dir) / key[:2] / f"{key}.png"


def _regular_single_link(path: Path) -> bool:
    try:
        metadata = path.lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISREG(metadata.st_mode) and metadata.st_nlink == 1


def _atomic_copy(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=destination.parent,
        prefix=f".{destination.name}.",
        suffix=".tmp",
    )
    temporary = Path(temporary_name)
    try:
        with source.open("rb") as input_file, os.fdopen(descriptor, "wb") as output_file:
            shutil.copyfileobj(input_file, output_file, length=1024 * 1024)
            output_file.flush()
            os.fsync(output_file.fileno())
        if not _valid_raw_image(temporary):
            raise ValueError("cache copy is not valid raw sticker art")
        os.replace(temporary, destination)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def store_raw(
    cache_dir: Path,
    pack_dir: Path,
    manifest: dict[str, object],
    row: dict[str, object],
    style_reference: Path,
) -> str:
    pack_dir = Path(pack_dir).resolve(strict=True)
    raw = canonical_write_paths(pack_dir, row)["raw_path"]
    if not _regular_single_link(raw) or not _valid_raw_image(raw):
        raise ValueError("only a valid canonical raw sticker may enter the cache")
    with Image.open(raw) as image:
        report = quality_report(image)
    if not report["passed"]:
        raise ValueError("only quality-gate-passing raw art may enter the cache")
    key = cache_key(manifest, row, style_reference)
    entry = _entry_path(cache_dir, key)
    if _regular_single_link(entry) and _valid_raw_image(entry):
        return key
    if entry.exists() or entry.is_symlink():
        raise ValueError("cache entry is unsafe or invalid")
    _atomic_copy(raw, entry)
    return key


def restore_raw(
    cache_dir: Path,
    pack_dir: Path,
    manifest: dict[str, object],
    row: dict[str, object],
    style_reference: Path,
) -> str | None:
    pack_dir = Path(pack_dir).resolve(strict=True)
    key = cache_key(manifest, row, style_reference)
    entry = _entry_path(cache_dir, key)
    if not _regular_single_link(entry) or not _valid_raw_image(entry):
        return None
    destination = canonical_write_paths(pack_dir, row)["raw_path"]
    _atomic_copy(entry, destination)
    return key


def _selected_rows(manifest: dict[str, object], ids: Iterable[int]) -> list[dict[str, object]]:
    requested = list(ids)
    if not requested or len(requested) != len(set(requested)):
        raise ValueError("item ids must be a non-empty unique list")
    index = {
        row["id"]: row
        for row in manifest["items"]
        if isinstance(row, dict) and type(row.get("id")) is int
    }
    if any(item_id not in index for item_id in requested):
        raise ValueError("unknown item id")
    return [index[item_id] for item_id in requested]


def main() -> int:
    parser = argparse.ArgumentParser(description="Reuse quality-approved raw sticker art")
    parser.add_argument("operation", choices=("probe", "restore", "store"))
    parser.add_argument("pack_dir", type=Path)
    parser.add_argument("--style-reference", required=True, type=Path)
    parser.add_argument("--cache-dir", required=True, type=Path)
    parser.add_argument("--ids", required=True)
    args = parser.parse_args()
    try:
        pack_dir = args.pack_dir.resolve(strict=True)
        manifest = load_manifest(pack_dir / "manifest.json")
        errors = validate_manifest(manifest)
        if errors:
            raise ValueError("; ".join(errors))
        ids = [int(value) for value in args.ids.split(",") if value]
        rows = _selected_rows(manifest, ids)
        hits = []
        misses = []
        for row in rows:
            key = cache_key(manifest, row, args.style_reference)
            if args.operation == "store":
                store_raw(args.cache_dir, pack_dir, manifest, row, args.style_reference)
                hits.append(row["id"])
            elif args.operation == "restore":
                restored = restore_raw(
                    args.cache_dir, pack_dir, manifest, row, args.style_reference
                )
                (hits if restored else misses).append(row["id"])
            else:
                entry = _entry_path(args.cache_dir, key)
                target = (
                    hits
                    if _regular_single_link(entry) and _valid_raw_image(entry)
                    else misses
                )
                target.append(row["id"])
        print(json.dumps({"hits": hits, "misses": misses}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError, RuntimeError) as error:
        print(str(error))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
