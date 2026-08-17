from __future__ import annotations

import argparse
from collections import deque
from pathlib import Path
import re
from typing import Tuple

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps

from font_utils import resolve_cjk_font, resolve_latin_display_font
from svg_layers import compose_layers


SIZE = 1024
SAFE_MARGIN = 64
DIE_CUT_RADIUS = 32
FINAL_DILATION_RADIUS = 1
ART_INSET = SAFE_MARGIN + DIE_CUT_RADIUS + FINAL_DILATION_RADIUS
MAX_ART_SIZE = SIZE - (2 * ART_INSET)
PREFERRED_CAPTIONED_ART_SIZE = 700
MIN_USEFUL_CAPTIONED_ART_SIZE = 384
DIE_CUT_FILTER_SIZE = (2 * DIE_CUT_RADIUS) + 1
FINAL_DILATION_FILTER_SIZE = (2 * FINAL_DILATION_RADIUS) + 1
INK = (46, 66, 155, 255)
WHITE = (255, 255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
ENGLISH_WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")


def _binary(mask: Image.Image, threshold: int = 128) -> Image.Image:
    return mask.convert("L").point(lambda value: 255 if value >= threshold else 0, mode="L")


def _remove_small_components(mask: Image.Image, min_area: int) -> Image.Image:
    binary = _binary(mask)
    width, height = binary.size
    pixels = binary.load()
    seen = bytearray(width * height)
    kept = Image.new("L", binary.size, 0)
    output = kept.load()
    for y in range(height):
        for x in range(width):
            index = y * width + x
            if seen[index] or not pixels[x, y]:
                continue
            queue = deque([(x, y)])
            seen[index] = 1
            component = []
            while queue:
                px, py = queue.popleft()
                component.append((px, py))
                for nx, ny in ((px - 1, py), (px + 1, py), (px, py - 1), (px, py + 1)):
                    if 0 <= nx < width and 0 <= ny < height:
                        neighbor_index = ny * width + nx
                        if not seen[neighbor_index] and pixels[nx, ny]:
                            seen[neighbor_index] = 1
                            queue.append((nx, ny))
            if len(component) >= min_area:
                for px, py in component:
                    output[px, py] = 255
    return kept


def _clean_binary_mask(mask: Image.Image, min_area: int = 24) -> Image.Image:
    opened = _binary(mask).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    closed = opened.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3))
    width, height = mask.size
    smoothing_size = (max(1, width // 2), max(1, height // 2))
    small = closed.resize(smoothing_size, Image.Resampling.LANCZOS)
    smooth = small.resize(mask.size, Image.Resampling.LANCZOS)
    return _remove_small_components(_binary(smooth, 144), min_area)


def _fit_rgba(
    image: Image.Image, max_art_size: int = MAX_ART_SIZE, center_y: int = SIZE // 2
) -> Image.Image:
    source = image.convert("RGBA")
    source.thumbnail((max_art_size, max_art_size), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (SIZE, SIZE), TRANSPARENT)
    left = (SIZE - source.width) // 2
    top = center_y - (source.height // 2)
    canvas.alpha_composite(source, (left, top))
    return canvas


def _crop_to_alpha(image: Image.Image) -> Image.Image:
    source = image.convert("RGBA")
    bbox = source.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("sticker artwork is empty")
    return source.crop(bbox)


def _ink_from_rgba(image: Image.Image) -> Image.Image:
    red, green, blue, alpha = image.split()
    channel_minimum = ImageChops.darker(ImageChops.darker(red, green), blue)
    channel_maximum = ImageChops.lighter(ImageChops.lighter(red, green), blue)
    distance_from_white = ImageOps.invert(channel_minimum)
    chroma = ImageChops.subtract(channel_maximum, channel_minimum)
    colored_or_dark = ImageChops.lighter(_binary(distance_from_white, 42), _binary(chroma, 32))
    return ImageChops.darker(_binary(alpha, 16), colored_or_dark)


def _caption_lines(caption: str) -> list[str]:
    if not caption.strip():
        return []
    lines = [line.strip() for line in caption.splitlines() if line.strip()]
    if not 1 <= len(lines) <= 2:
        raise ValueError("caption must contain one or two non-empty lines")

    cjk_count = len(CJK_RE.findall(caption))
    english_word_count = len(ENGLISH_WORD_RE.findall(caption))
    if cjk_count and not 2 <= cjk_count <= 8:
        raise ValueError("caption must contain 2 to 8 CJK characters")
    if not cjk_count and not 2 <= english_word_count <= 4:
        raise ValueError("caption must contain 2 to 4 English words")
    if cjk_count and english_word_count and not 2 <= english_word_count <= 4:
        raise ValueError("caption must contain 2 to 4 English words")
    return lines


def _caption_mask(lines: list[str]) -> Image.Image:
    mask = Image.new("L", (SIZE, SIZE), 0)
    is_latin_only = not any(CJK_RE.search(line) for line in lines)
    for font_size in (*range(96, 42, -4), 42):
        font = (
            resolve_latin_display_font(font_size)
            if is_latin_only
            else resolve_cjk_font(font_size)
        )
        widths = [font.getlength(line) for line in lines]
        if max(widths) <= 460:
            break
    else:
        raise ValueError("caption is too long for the sticker canvas")

    line_height = int(font_size * 1.12)
    block = Image.new("L", (int(max(widths)) + 4, line_height * len(lines)), 0)
    draw = ImageDraw.Draw(block)
    for index, line in enumerate(lines):
        x = 0 if is_latin_only else (block.width - font.getlength(line)) / 2
        draw.text(
            (x, index * line_height),
            line,
            font=font,
            fill=255,
        )
    mask.paste(block, (0, 0))
    return mask.crop(mask.getbbox())


def _place_caption(art: Image.Image, text: Image.Image) -> tuple[str, Image.Image]:
    art_box = _binary(art).getbbox()
    if art_box is None:
        raise ValueError("sticker artwork is empty")
    left, top, right, bottom = art_box
    gap = 24
    candidates = (
        ("left", left - gap - text.width, (top + bottom - text.height) // 2),
        ("right", right + gap, (top + bottom - text.height) // 2),
        ("bottom", (left + right - text.width) // 2, bottom + gap),
        ("top", (left + right - text.width) // 2, top - gap - text.height),
    )
    occupied = _binary(art).filter(ImageFilter.MaxFilter(33))
    for name, x, y in candidates:
        if (
            x < ART_INSET
            or y < ART_INSET
            or x + text.width > SIZE - ART_INSET
            or y + text.height > SIZE - ART_INSET
        ):
            continue
        placed = Image.new("L", (SIZE, SIZE), 0)
        placed.paste(text, (x, y))
        if ImageChops.multiply(occupied, placed).getbbox() is None:
            return name, placed
    raise ValueError("no integrated caption placement is available")


def _caption_fits_bounds(art: Image.Image, text: Image.Image) -> bool:
    """Cheap conservative preflight for the same four caption positions."""
    art_box = art.getbbox()
    if art_box is None:
        raise ValueError("sticker artwork is empty")
    left, top, right, bottom = art_box
    gap = 24
    candidates = (
        (left - gap - text.width, (top + bottom - text.height) // 2),
        (right + gap, (top + bottom - text.height) // 2),
        ((left + right - text.width) // 2, bottom + gap),
        ((left + right - text.width) // 2, top - gap - text.height),
    )
    return any(
        x >= ART_INSET
        and y >= ART_INSET
        and x + text.width <= SIZE - ART_INSET
        and y + text.height <= SIZE - ART_INSET
        for x, y in candidates
    )


def _fit_captioned_rgba(subject: Image.Image, text: Image.Image) -> Image.Image:
    """Keep the largest useful artwork size for which the stable solver succeeds."""

    def fitted_at(max_art_size: int) -> Image.Image | None:
        fitted = _fit_rgba(subject, max_art_size=max_art_size)
        return fitted if _caption_fits_bounds(fitted.getchannel("A"), text) else None

    preferred = fitted_at(PREFERRED_CAPTIONED_ART_SIZE)
    if preferred is not None:
        return preferred

    minimum = fitted_at(MIN_USEFUL_CAPTIONED_ART_SIZE)
    if minimum is None:
        raise ValueError("no integrated caption placement is available at minimum useful art size")

    best = minimum
    low = MIN_USEFUL_CAPTIONED_ART_SIZE + 1
    high = PREFERRED_CAPTIONED_ART_SIZE - 1
    while low <= high:
        candidate_size = (low + high) // 2
        candidate = fitted_at(candidate_size)
        if candidate is None:
            high = candidate_size - 1
        else:
            best = candidate
            low = candidate_size + 1
    return best


def make_layers(image: Image.Image, caption: str = "") -> Tuple[Image.Image, Image.Image]:
    """Build deterministic binary white-support and blue-ink masks at 1024 px."""
    caption_lines = _caption_lines(caption)
    subject = _crop_to_alpha(image)
    caption_text = _caption_mask(caption_lines) if caption_lines else None
    fitted = _fit_captioned_rgba(subject, caption_text) if caption_text else _fit_rgba(subject)
    alpha = _clean_binary_mask(fitted.getchannel("A"), min_area=32)
    ink = ImageChops.darker(_clean_binary_mask(_ink_from_rgba(fitted), 24), alpha)
    if caption_text is not None:
        _, caption_ink = _place_caption(alpha, caption_text)
        ink = ImageChops.lighter(ink, caption_ink)
        alpha = ImageChops.lighter(alpha, caption_ink)
    white = _binary(alpha.filter(ImageFilter.MaxFilter(DIE_CUT_FILTER_SIZE)))
    white = _binary(white.filter(ImageFilter.MaxFilter(FINAL_DILATION_FILTER_SIZE)))
    return white, _binary(ink)


def compose_default_png(white_mask: Image.Image, ink_mask: Image.Image, color: str = "#2E429B") -> Image.Image:
    """Composite the binding white and default-blue layers into an RGBA PNG."""
    if color.lower() != "#2e429b":
        raise ValueError("default PNG color must be #2E429B")
    if white_mask.size != ink_mask.size:
        raise ValueError("white and ink masks must have matching dimensions")
    white_mask = _binary(white_mask)
    ink_mask = _binary(ink_mask)
    return compose_layers(white_mask, ink_mask, color)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--ink-mask", required=True, type=Path)
    parser.add_argument("--white-mask", required=True, type=Path)
    parser.add_argument("--png", required=True, type=Path)
    parser.add_argument("--caption", default="")
    args = parser.parse_args()

    white, ink = make_layers(Image.open(args.input), args.caption)
    for path in (args.ink_mask, args.white_mask, args.png):
        path.parent.mkdir(parents=True, exist_ok=True)
    ink.save(args.ink_mask)
    white.save(args.white_mask)
    compose_default_png(white, ink).save(args.png)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
