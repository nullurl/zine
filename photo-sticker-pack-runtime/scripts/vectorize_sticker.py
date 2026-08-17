from __future__ import annotations

import argparse
import base64
from io import BytesIO
from pathlib import Path
import re
from typing import List, Sequence, Tuple

from PIL import Image


Run = Tuple[int, int, int]
HEX_COLOR = re.compile(r"#[0-9A-Fa-f]{6}\Z")


def _binary_mask(mask: Image.Image) -> Image.Image:
    """Return an L-mode binary copy of a mask."""
    return mask.convert("L").point(lambda value: 255 if value >= 128 else 0)


def mask_to_runs(mask: Image.Image) -> List[Run]:
    """Encode every contiguous foreground span as (x, y, length)."""
    binary = _binary_mask(mask)
    pixels = binary.load()
    runs: List[Run] = []
    for y in range(binary.height):
        x = 0
        while x < binary.width:
            while x < binary.width and pixels[x, y] == 0:
                x += 1
            start = x
            while x < binary.width and pixels[x, y] != 0:
                x += 1
            if x > start:
                runs.append((start, y, x - start))
    return runs


def runs_to_mask(runs: Sequence[Run], size: Tuple[int, int]) -> Image.Image:
    """Recreate an L-mode binary mask from run-length spans."""
    mask = Image.new("L", size, 0)
    pixels = mask.load()
    width, height = size
    for start, y, length in runs:
        if not (0 <= y < height and 0 <= start < width and length > 0 and start + length <= width):
            raise ValueError("run is outside the requested mask size")
        for x in range(start, start + length):
            pixels[x, y] = 255
    return mask


def mask_quality(original: Image.Image, reconstructed: Image.Image) -> Tuple[float, float]:
    """Return binary IoU and differing-pixel fraction for two same-size masks."""
    if original.size != reconstructed.size:
        raise ValueError("masks must have the same size")
    left = _binary_mask(original)
    right = _binary_mask(reconstructed)
    left_data = list(left.getdata())
    right_data = list(right.getdata())
    intersection = sum(1 for a, b in zip(left_data, right_data) if a and b)
    union = sum(1 for a, b in zip(left_data, right_data) if a or b)
    iou = intersection / union if union else 1.0
    mean_difference = sum(abs(a - b) for a, b in zip(left_data, right_data)) / (255 * len(left_data))
    return iou, mean_difference


def mask_to_path(mask: Image.Image) -> str:
    """Encode a binary mask as one one-pixel-high closed SVG path per run."""
    return "".join(f"M{start} {y}h{length}v1h-{length}z" for start, y, length in mask_to_runs(mask))


def _mask_data_uri(mask: Image.Image) -> str:
    buffer = BytesIO()
    _binary_mask(mask).save(buffer, format="PNG", optimize=True)
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def _path_svg(width: int, height: int, white_path: str, ink_path: str, color: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" style="color:{color}">'
        f'<path fill="#FFFFFF" d="{white_path}"/>'
        f'<path fill="currentColor" d="{ink_path}"/>'
        "</svg>"
    )


def _mask_svg(width: int, height: int, white: Image.Image, ink: Image.Image, color: str) -> str:
    white_uri = _mask_data_uri(white)
    ink_uri = _mask_data_uri(ink)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" style="color:{color}">
<defs>
  <mask id="white-mask" mask-type="luminance"><image width="{width}" height="{height}" href="{white_uri}"/></mask>
  <mask id="ink-mask" mask-type="luminance"><image width="{width}" height="{height}" href="{ink_uri}"/></mask>
</defs>
<rect width="{width}" height="{height}" fill="#FFFFFF" mask="url(#white-mask)"/>
<rect width="{width}" height="{height}" fill="currentColor" mask="url(#ink-mask)"/>
</svg>'''


def export_svg(
    white_mask: Image.Image,
    ink_mask: Image.Image,
    output: Path,
    default_color: str = "#2E429B",
    max_path_bytes: int = 4_000_000,
) -> str:
    """Write a recolorable SVG and return either ``path`` or ``mask``."""
    if white_mask.size != ink_mask.size:
        raise ValueError("white and ink masks must have the same size")
    if not isinstance(default_color, str) or not HEX_COLOR.fullmatch(default_color):
        raise ValueError("default_color must be a six-digit hexadecimal color")

    white_runs = mask_to_runs(white_mask)
    ink_runs = mask_to_runs(ink_mask)
    white_path = mask_to_path(white_mask)
    ink_path = mask_to_path(ink_mask)

    white_quality = mask_quality(white_mask, runs_to_mask(white_runs, white_mask.size))
    ink_quality = mask_quality(ink_mask, runs_to_mask(ink_runs, ink_mask.size))
    quality_passes = min(white_quality[0], ink_quality[0]) >= 0.98 and max(
        white_quality[1], ink_quality[1]
    ) <= 0.015
    path_bytes = len(white_path.encode("utf-8")) + len(ink_path.encode("utf-8"))

    if quality_passes and path_bytes <= max_path_bytes:
        text = _path_svg(white_mask.width, white_mask.height, white_path, ink_path, default_color)
        representation = "path"
    else:
        text = _mask_svg(white_mask.width, white_mask.height, white_mask, ink_mask, default_color)
        representation = "mask"

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text + "\n", encoding="utf-8")
    return representation


def main() -> int:
    parser = argparse.ArgumentParser(description="Export recolorable sticker masks to SVG")
    parser.add_argument("--white-mask", required=True, type=Path)
    parser.add_argument("--ink-mask", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    with Image.open(args.white_mask) as white_mask, Image.open(args.ink_mask) as ink_mask:
        representation = export_svg(white_mask, ink_mask, args.output)
    print(representation)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
