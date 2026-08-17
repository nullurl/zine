from pathlib import Path
from typing import Iterable

from PIL import ImageFont


FONT_CANDIDATES = (
    Path("/System/Library/Fonts/STHeiti Light.ttc"),
    Path("/Library/Fonts/Arial Unicode.ttf"),
    Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
    Path("/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc"),
)

LATIN_DISPLAY_FONT_CANDIDATES = (
    Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
    Path("/Library/Fonts/Arial Bold.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
)


def _glyph_signature(font: ImageFont.FreeTypeFont, glyph: str) -> tuple[tuple[int, int], bytes]:
    """Return a Pillow-rendered glyph signature without relying on advance width."""
    mask = font.getmask(glyph, mode="L")
    return mask.size, bytes(mask)


def _renders_cjk(font: ImageFont.FreeTypeFont) -> bool:
    """Check that both required Han glyphs differ from the font's missing-glyph tofu."""
    try:
        missing = {
            _glyph_signature(font, "\U0010ffff"),
            _glyph_signature(font, "\ue000"),
        }
        required = [_glyph_signature(font, glyph) for glyph in ("贴", "图")]
    except OSError:
        return False
    return required[0] != required[1] and all(signature not in missing for signature in required)


def resolve_cjk_font(size: int, candidates: Iterable[Path] = FONT_CANDIDATES) -> ImageFont.FreeTypeFont:
    """Return the first installed CJK-capable font from the stable candidate list."""
    for path in candidates:
        if path.is_file():
            try:
                font = ImageFont.truetype(str(path), size=size)
            except OSError:
                continue
            if _renders_cjk(font):
                return font
    raise RuntimeError("No CJK-capable font found; install Noto Sans CJK or provide a redistributable font asset")


def resolve_latin_display_font(
    size: int, candidates: Iterable[Path] = LATIN_DISPLAY_FONT_CANDIDATES
) -> ImageFont.FreeTypeFont:
    """Return a stable bold sans face for short uppercase sticker captions."""
    for path in candidates:
        if path.is_file():
            try:
                return ImageFont.truetype(str(path), size=size)
            except OSError:
                continue
    raise RuntimeError(
        "No bold Latin display font found; install Arial Bold or DejaVu Sans Bold"
    )
