from __future__ import annotations

import argparse
from collections import deque
import json
from pathlib import Path

from PIL import Image, ImageFilter

from postprocess_sticker import _ink_from_rgba


MIN_COVERAGE = 0.03
MAX_COVERAGE = 0.72
MAX_FORBIDDEN_RATIO = 0.01
MIN_BORDER_CLEARANCE = 48
# Pixels removed by a 3x3 opening are unsupported one-pixel/fine ink.
MAX_FINE_DETAIL_RATIO = 0.12
# Tiny disconnected marks may be incidental, but cannot dominate the ink.
SMALL_COMPONENT_MAX_AREA = 192
MAX_SMALL_COMPONENT_RATIO = 0.08
# Ink is measured relative to visible subject pixels, not the whole canvas.
MIN_INK_DENSITY = 0.015


def mask_run_count(mask: Image.Image) -> int:
    binary = mask.convert("L").point(lambda value: 1 if value >= 128 else 0)
    pixels = binary.load()
    return sum(
        1
        for y in range(binary.height)
        for x in range(binary.width)
        if pixels[x, y] and (x == 0 or not pixels[x - 1, y])
    )


def small_component_ratio(mask: Image.Image) -> float:
    binary = mask.convert("L").point(lambda value: 255 if value >= 128 else 0)
    width, height = binary.size
    pixels = binary.load()
    seen = bytearray(width * height)
    total_ink = 0
    small_ink = 0
    for y in range(height):
        for x in range(width):
            index = y * width + x
            if seen[index] or not pixels[x, y]:
                continue
            queue = deque([(x, y)])
            seen[index] = 1
            component_area = 0
            while queue:
                px, py = queue.popleft()
                component_area += 1
                for nx, ny in ((px - 1, py), (px + 1, py), (px, py - 1), (px, py + 1)):
                    if 0 <= nx < width and 0 <= ny < height:
                        neighbor_index = ny * width + nx
                        if not seen[neighbor_index] and pixels[nx, ny]:
                            seen[neighbor_index] = 1
                            queue.append((nx, ny))
            total_ink += component_area
            if component_area <= SMALL_COMPONENT_MAX_AREA:
                small_ink += component_area
    return small_ink / max(total_ink, 1)


def fine_detail_ratio(mask: Image.Image) -> float:
    binary = mask.convert("L").point(lambda value: 255 if value >= 128 else 0)
    opened = binary.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    ink_pixels = sum(1 for value in binary.getdata() if value)
    supported_pixels = sum(1 for value in opened.getdata() if value)
    return max(0, ink_pixels - supported_pixels) / max(ink_pixels, 1)


def detail_is_excessive(
    fine_ratio: float, component_ratio: float, ink_density: float
) -> bool:
    return (
        fine_ratio > MAX_FINE_DETAIL_RATIO
        or component_ratio > MAX_SMALL_COMPONENT_RATIO
        or ink_density < MIN_INK_DENSITY
    )


def quality_report(image: Image.Image) -> dict[str, object]:
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A").point(lambda value: 255 if value >= 16 else 0)
    visible = sum(1 for value in alpha.getdata() if value)
    coverage = visible / (rgba.width * rgba.height)
    bbox = alpha.getbbox()
    allowed = ((46, 66, 155), (255, 255, 255))
    forbidden = sum(
        1
        for red, green, blue, opacity in rgba.getdata()
        if opacity >= 16
        and min(
            sum(abs(value - target) for value, target in zip((red, green, blue), color))
            for color in allowed
        )
        > 48
    )
    forbidden_ratio = forbidden / max(visible, 1)
    ink = _ink_from_rgba(rgba)
    ink_pixels = sum(1 for value in ink.getdata() if value >= 128)
    ink_density = ink_pixels / max(visible, 1)
    fine_ratio = fine_detail_ratio(ink)
    component_ratio = small_component_ratio(ink)
    clearance = (
        0
        if bbox is None
        else min(bbox[0], bbox[1], rgba.width - bbox[2], rgba.height - bbox[3])
    )
    reasons = []
    if not MIN_COVERAGE <= coverage <= MAX_COVERAGE:
        reasons.append("coverage")
    if forbidden_ratio > MAX_FORBIDDEN_RATIO:
        reasons.append("forbidden_palette")
    if detail_is_excessive(fine_ratio, component_ratio, ink_density):
        reasons.append("excessive_detail")
    if clearance < MIN_BORDER_CLEARANCE:
        reasons.append("unsafe_border")
    return {
        "passed": not reasons,
        "reasons": reasons,
        "coverage": coverage,
        "forbidden_ratio": forbidden_ratio,
        "fine_detail_ratio": fine_ratio,
        "small_component_ratio": component_ratio,
        "ink_density": ink_density,
        "border_clearance": clearance,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    report = quality_report(Image.open(args.input))
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
