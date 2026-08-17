from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
from typing import Iterable

from PIL import Image, ImageOps

from artifact_contract import canonical_write_paths, safe_asset_path, validate_artifact_paths
from cache_utils import store_raw
from manifest_utils import load_manifest, validate_manifest
from normalize_raw_palette import normalize_palette, save_atomically
from postprocess_sticker import compose_default_png, make_layers
from quality_gate import quality_report
from resume_utils import (
    _atomic_replace_manifest,
    _valid_processed,
    _valid_raw_image,
    _valid_staged_image,
    classify_item,
    decision_transition,
    staged_relative_path,
)
from svg_layers import validate_rendered_png
from vectorize_sticker import export_svg


MAX_LOCAL_WORKERS = 4


def bounded_workers(requested: int, item_count: int) -> int:
    return max(1, min(MAX_LOCAL_WORKERS, max(1, requested), max(1, item_count)))


def _save_png_atomic(image: Image.Image, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=destination.parent,
        prefix=f".{destination.name}.",
        suffix=".tmp",
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        image.save(temporary, format="PNG")
        os.replace(temporary, destination)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def _export_svg_atomic(white: Image.Image, ink: Image.Image, destination: Path) -> str:
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=destination.parent,
        prefix=f".{destination.name}.",
        suffix=".tmp",
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        representation = export_svg(white, ink, temporary)
        os.replace(temporary, destination)
        return representation
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def _default_chroma_script() -> Path:
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    return codex_home / "skills" / ".system" / "imagegen" / "scripts" / "remove_chroma_key.py"


def _remove_chroma(stage: Path, raw: Path, chroma_script: Path) -> None:
    if not chroma_script.is_file():
        raise ValueError("remove_chroma_key.py is unavailable")
    command = [
        sys.executable,
        str(chroma_script),
        "--input",
        str(stage),
        "--out",
        str(raw),
        "--auto-key",
        "border",
        "--soft-matte",
        "--transparent-threshold",
        "12",
        "--opaque-threshold",
        "220",
        "--despill",
        "--force",
    ]
    result = subprocess.run(command, capture_output=True, text=True, timeout=180)
    if result.returncode != 0:
        raise ValueError("chroma removal failed")
    if _valid_raw_image(raw):
        return
    retry = subprocess.run(
        command[:-1] + ["--edge-contract", "1", "--force"],
        capture_output=True,
        text=True,
        timeout=180,
    )
    if retry.returncode != 0 or not _valid_raw_image(raw):
        raise ValueError("chroma removal left an invalid raw image")


def _regular_single_link(path: Path) -> bool:
    try:
        metadata = path.lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISREG(metadata.st_mode) and metadata.st_nlink == 1


def _valid_flexible_stage(path: Path) -> bool:
    try:
        if not _regular_single_link(path):
            return False
        with Image.open(path) as image:
            image.load()
            if image.mode not in {"RGB", "RGBA"}:
                return False
            if not 512 <= image.width <= 4096 or not 512 <= image.height <= 4096:
                return False
            if image.mode == "RGBA" and image.getchannel("A").getextrema() != (255, 255):
                return False
            rgb = image.convert("RGB")
        key = rgb.getpixel((0, 0))
        red, green, blue = key
        if green < 180 or green - red < 80 or green - blue < 80:
            return False

        def key_green(pixel: tuple[int, int, int]) -> bool:
            pixel_red, pixel_green, pixel_blue = pixel
            return (
                pixel_green >= 160
                and pixel_green - pixel_red >= 50
                and pixel_green - pixel_blue >= 50
            )

        border_width = max(16, min(rgb.size) // 16)
        border_parts = (
            rgb.crop((0, 0, rgb.width, border_width)),
            rgb.crop((0, rgb.height - border_width, rgb.width, rgb.height)),
            rgb.crop((0, border_width, border_width, rgb.height - border_width)),
            rgb.crop(
                (
                    rgb.width - border_width,
                    border_width,
                    rgb.width,
                    rgb.height - border_width,
                )
            ),
        )
        border_pixels = [pixel for part in border_parts for pixel in part.getdata()]
        if sum(key_green(pixel) for pixel in border_pixels) / len(border_pixels) < 0.98:
            return False
        subject_pixels = sum(not key_green(pixel) for pixel in rgb.getdata())
        return 0.01 <= subject_pixels / (rgb.width * rgb.height) <= 0.70
    except (OSError, RuntimeError, ValueError):
        return False


def _canonicalize_stage(path: Path) -> bool:
    if _valid_staged_image(path):
        return True
    if not _valid_flexible_stage(path):
        return False
    with Image.open(path) as source:
        rgb = source.convert("RGB")
        flattened = []
        for red, green, blue in rgb.getdata():
            if green >= 160 and green - red >= 50 and green - blue >= 50:
                flattened.append((0, 255, 0))
            else:
                flattened.append((red, green, blue))
        rgb.putdata(flattened)
        fitted = ImageOps.contain(rgb, (1024, 1024), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (1024, 1024), (0, 255, 0))
    canvas.paste(fitted, ((1024 - fitted.width) // 2, (1024 - fitted.height) // 2))
    _save_png_atomic(canvas, path)
    return _valid_staged_image(path)


def _process_one(payload: dict[str, object]) -> dict[str, object]:
    pack_dir = Path(str(payload["pack_dir"])).resolve(strict=True)
    row = dict(payload["row"])
    item_id = int(row["id"])
    if int(row.get("retry_count", 0)) != 0:
        return {
            "id": item_id,
            "ok": False,
            "failure": "safe_item_flow",
            "reasons": ["retry and crash recovery require the safe item-wise flow"],
        }
    assets = canonical_write_paths(pack_dir, row)
    if _valid_processed(row, assets):
        return {
            "id": item_id,
            "ok": True,
            "representation": row["representation"],
            "cache": None,
        }

    raw = assets["raw_path"]
    stage, _ = safe_asset_path(pack_dir, staged_relative_path(row), "staged_path")
    try:
        if not _valid_raw_image(raw):
            if not _valid_staged_image(stage):
                raise ValueError("valid staged or raw artwork is required")
            _remove_chroma(stage, raw, Path(str(payload["chroma_script"])))
        save_atomically(normalize_palette(Image.open(raw)), raw)
        if not _valid_raw_image(raw):
            raise ValueError("normalized raw image is invalid")
        with Image.open(raw) as source:
            report = quality_report(source)
        if not report["passed"]:
            return {
                "id": item_id,
                "ok": False,
                "failure": "quality_gate",
                "reasons": report["reasons"],
                "quality": report,
            }

        cache_key = None
        cache_dir = payload.get("cache_dir")
        style_reference = payload.get("style_reference")
        if cache_dir and style_reference:
            try:
                cache_key = store_raw(
                    Path(str(cache_dir)),
                    pack_dir,
                    dict(payload["manifest"]),
                    row,
                    Path(str(style_reference)),
                )
            except (OSError, ValueError, RuntimeError):
                cache_key = None

        with Image.open(raw) as source:
            white, ink = make_layers(source, str(row.get("caption", "")))
        png = compose_default_png(white, ink)
        _save_png_atomic(ink, assets["ink_mask_path"])
        _save_png_atomic(white, assets["white_mask_path"])
        _save_png_atomic(png, assets["png_path"])
        representation = _export_svg_atomic(white, ink, assets["svg_path"])
        png_errors = validate_rendered_png(
            assets["png_path"],
            str(row["png_path"]),
            white,
            ink,
            "#2E429B",
        )
        if png_errors:
            raise ValueError("; ".join(png_errors))
        completed_row = dict(row)
        completed_row["representation"] = representation
        if not _valid_processed(completed_row, assets):
            raise ValueError("processed PNG/SVG verification failed")
        if _regular_single_link(stage):
            stage.unlink()
        return {
            "id": item_id,
            "ok": True,
            "representation": representation,
            "cache": cache_key,
        }
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        return {
            "id": item_id,
            "ok": False,
            "failure": "pipeline",
            "reasons": [str(error)],
        }


def _selected_rows(manifest: dict[str, object], ids: Iterable[int]) -> list[dict[str, object]]:
    requested = list(ids)
    if not requested or len(requested) != len(set(requested)):
        raise ValueError("item ids must be a non-empty unique list")
    rows = {
        row["id"]: row
        for row in manifest["items"]
        if isinstance(row, dict) and type(row.get("id")) is int
    }
    if any(item_id not in rows for item_id in requested):
        raise ValueError("unknown item id")
    return [rows[item_id] for item_id in requested]


def _subprocess_results(
    payloads: list[dict[str, object]], worker_count: int
) -> list[dict[str, object]]:
    results = []
    script = Path(__file__).resolve()
    for offset in range(0, len(payloads), worker_count):
        wave = payloads[offset : offset + worker_count]
        processes = []
        for payload in wave:
            process = subprocess.Popen(
                [sys.executable, str(script), "--worker"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            assert process.stdin is not None
            process.stdin.write(json.dumps(payload, ensure_ascii=False))
            process.stdin.close()
            processes.append(process)
        for process in processes:
            assert process.stdout is not None
            assert process.stderr is not None
            stdout = process.stdout.read()
            stderr = process.stderr.read()
            process.stdout.close()
            process.stderr.close()
            return_code = process.wait()
            if return_code != 0:
                raise ValueError(stderr.strip() or "local pipeline worker failed")
            result = json.loads(stdout)
            if not isinstance(result, dict):
                raise ValueError("local pipeline worker returned invalid JSON")
            results.append(result)
    return results


def _commit_successes(
    manifest_path: Path,
    results: list[dict[str, object]],
    initial_decisions: dict[int, str],
) -> dict[int, list[str]]:
    transitions: dict[int, list[str]] = {}
    for result in sorted(results, key=lambda value: int(value["id"])):
        if not result["ok"]:
            continue
        item_id = int(result["id"])
        transitions[item_id] = []
        decision = initial_decisions[item_id]
        remaining = {
            "chroma": ("generated", "processed", "complete"),
            "gate": ("generated", "processed", "complete"),
            "process": ("processed", "complete"),
            "finalize": ("complete",),
            "skip": (),
        }[decision]
        for status in remaining:
            manifest = load_manifest(manifest_path)
            errors = validate_manifest(manifest)
            if errors:
                raise ValueError("; ".join(errors))
            row = next(item for item in manifest["items"] if item["id"] == item_id)
            row["status"] = status
            row["error"] = None
            if status in {"processed", "complete"}:
                row["representation"] = result["representation"]
            _atomic_replace_manifest(manifest_path, manifest)
            transitions[item_id].append(status)
    return transitions


def run_fast_pipeline(
    pack_dir: Path,
    ids: Iterable[int],
    *,
    workers: int = 3,
    chroma_script: Path | None = None,
    cache_dir: Path | None = None,
    style_reference: Path | None = None,
) -> dict[str, object]:
    pack_dir = Path(pack_dir).resolve(strict=True)
    manifest_path = pack_dir / "manifest.json"
    manifest = load_manifest(manifest_path)
    errors = validate_manifest(manifest)
    if errors:
        raise ValueError("; ".join(errors))
    _, artifact_errors = validate_artifact_paths(pack_dir, manifest["items"])
    if artifact_errors:
        raise ValueError("; ".join(artifact_errors))
    rows = _selected_rows(manifest, ids)
    if any(int(row.get("retry_count", 0)) != 0 for row in rows):
        raise ValueError("retry and crash recovery require the safe item-wise flow")
    for row in rows:
        stage, _ = safe_asset_path(pack_dir, staged_relative_path(row), "staged_path")
        if stage.exists() and not _canonicalize_stage(stage):
            raise ValueError(f"item {row['id']} generated stage is invalid")
    initial_decisions = {
        int(row["id"]): classify_item(pack_dir, row)
        for row in rows
    }
    unsupported = {
        item_id: decision
        for item_id, decision in initial_decisions.items()
        if decision not in {"chroma", "gate", "process", "finalize", "skip"}
    }
    if unsupported:
        raise ValueError(f"items are not ready for the fast pipeline: {unsupported}")
    changed = False
    for row in rows:
        decision = initial_decisions[int(row["id"])]
        normalized = decision_transition(decision)["normalize_status"]
        if normalized is not None and row.get("status") != normalized:
            row["status"] = normalized
            changed = True
    if changed:
        _atomic_replace_manifest(manifest_path, manifest)
        manifest = load_manifest(manifest_path)
        rows = _selected_rows(manifest, ids)
    payloads = [
        {
            "pack_dir": str(pack_dir),
            "row": row,
            "manifest": manifest,
            "chroma_script": str(chroma_script or _default_chroma_script()),
            "cache_dir": None if cache_dir is None else str(cache_dir),
            "style_reference": (
                None if style_reference is None else str(style_reference)
            ),
        }
        for row in rows
    ]
    count = bounded_workers(workers, len(payloads))
    if count == 1:
        results = [_process_one(payloads[0])]
    else:
        results = _subprocess_results(payloads, count)
    transitions = _commit_successes(manifest_path, results, initial_decisions)
    completed = sorted(int(result["id"]) for result in results if result["ok"])
    failed = sorted(
        (
            {
                "id": int(result["id"]),
                "failure": result["failure"],
                "reasons": result["reasons"],
            }
            for result in results
            if not result["ok"]
        ),
        key=lambda result: result["id"],
    )
    return {
        "completed": completed,
        "failed": failed,
        "transitions": transitions,
        "workers": count,
    }


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--worker":
        try:
            payload = json.loads(sys.stdin.read())
            if not isinstance(payload, dict):
                raise ValueError("worker payload must be an object")
            print(json.dumps(_process_one(payload), ensure_ascii=False, sort_keys=True))
            return 0
        except (OSError, ValueError, TypeError, RuntimeError) as error:
            print(str(error), file=sys.stderr)
            return 1
    parser = argparse.ArgumentParser(
        description="Process quality sticker items in a bounded local worker pool"
    )
    parser.add_argument("pack_dir", type=Path)
    parser.add_argument("--ids", required=True)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--chroma-script", type=Path)
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument("--style-reference", type=Path)
    args = parser.parse_args()
    try:
        ids = [int(value) for value in args.ids.split(",") if value]
        report = run_fast_pipeline(
            args.pack_dir,
            ids,
            workers=args.workers,
            chroma_script=args.chroma_script,
            cache_dir=args.cache_dir,
            style_reference=args.style_reference,
        )
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
        return 0 if not report["failed"] else 1
    except (OSError, ValueError, TypeError, RuntimeError) as error:
        print(str(error))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
