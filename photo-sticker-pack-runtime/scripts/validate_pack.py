from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Optional, Tuple

from PIL import Image

from artifact_contract import validate_artifact_paths
from manifest_utils import load_manifest, validate_manifest
from svg_layers import decode_svg_layers, validate_rendered_png


def _decoded_svg(
    path: Path, representation: object, default_color: str
) -> Optional[Tuple[Image.Image, Image.Image]]:
    try:
        _, white, ink = decode_svg_layers(
            path.read_text(encoding="utf-8"), representation, default_color
        )
    except (ValueError, OSError, UnicodeDecodeError, RuntimeError):
        return None
    return white, ink


def _validate_png(
    path: Path,
    relative_path: str,
    white: Image.Image,
    ink: Image.Image,
    default_color: str,
    errors: List[str],
) -> None:
    errors.extend(validate_rendered_png(path, relative_path, white, ink, default_color))


def validate_pack(pack_dir: Path) -> List[str]:
    """Return validation errors without creating, deleting, or changing pack files."""
    pack_dir = Path(pack_dir)
    try:
        pack_dir = pack_dir.resolve(strict=True)
    except (OSError, RuntimeError):
        return ["invalid pack directory"]
    manifest_path = pack_dir / "manifest.json"
    try:
        if manifest_path.is_symlink():
            return ["manifest.json must not be a symlink"]
    except OSError:
        return ["invalid manifest.json"]
    if not manifest_path.is_file():
        return ["missing manifest.json"]
    try:
        manifest = load_manifest(manifest_path)
    except (OSError, ValueError, TypeError, AttributeError, RuntimeError, Image.DecompressionBombError, Image.DecompressionBombWarning):
        return ["invalid manifest.json"]
    if not isinstance(manifest, dict):
        return ["invalid manifest.json"]

    try:
        errors = validate_manifest(manifest)
    except (TypeError, AttributeError, RuntimeError):
        return ["invalid manifest.json"]
    items = manifest.get("items", [])
    if not isinstance(items, list):
        return errors
    artifact_rows, artifact_errors = validate_artifact_paths(pack_dir, [row for row in items if isinstance(row, dict)])
    errors.extend(artifact_errors)
    default_color = manifest.get("default_color")
    if not isinstance(default_color, str):
        default_color = "#2E429B"
    artifact_index = 0
    for row in items:
        if not isinstance(row, dict):
            continue
        assets = artifact_rows[artifact_index]
        artifact_index += 1
        item_id = row.get("id")
        if row.get("status") != "complete":
            errors.append(f"item {item_id} status must be complete")
        representation = row.get("representation")
        if not isinstance(representation, str) or representation not in {"path", "mask"}:
            errors.append(f"item {item_id} representation must be path or mask")

        svg_path = assets.get("svg_path")
        png_path = assets.get("png_path")
        decoded = None
        if svg_path is not None:
            relative_svg = str(row.get("svg_path"))
            if not svg_path.is_file():
                errors.append(f"missing {relative_svg}")
            else:
                decoded = _decoded_svg(svg_path, representation, default_color)
                if decoded is None:
                    errors.append(f"invalid recolorable SVG {relative_svg}")
        if png_path is not None:
            relative_png = str(row.get("png_path"))
            if not png_path.is_file():
                errors.append(f"missing {relative_png}")
            elif decoded is not None:
                _validate_png(png_path, relative_png, decoded[0], decoded[1], default_color, errors)
    return list(dict.fromkeys(errors))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack_dir", type=Path)
    args = parser.parse_args()
    try:
        errors = validate_pack(args.pack_dir)
    except (OSError, ValueError, TypeError, AttributeError, RuntimeError):
        errors = ["invalid pack"]
    if errors:
        print("\n".join(errors))
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
