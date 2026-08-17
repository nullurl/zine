from __future__ import annotations

import argparse
import os
from pathlib import Path
import uuid

from PIL import Image

from postprocess_sticker import INK, WHITE, _ink_from_rgba


def normalize_palette(image: Image.Image) -> Image.Image:
    """Flatten visible source art to the pack's exact cobalt/white palette."""
    rgba = image.convert("RGBA")
    ink_mask = _ink_from_rgba(rgba)
    cobalt = Image.new("RGBA", rgba.size, INK)
    white = Image.new("RGBA", rgba.size, WHITE)
    normalized = Image.composite(cobalt, white, ink_mask)
    normalized.putalpha(rgba.getchannel("A"))
    return normalized


def save_atomically(image: Image.Image, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(f".{output.name}.{uuid.uuid4().hex}.tmp")
    try:
        image.save(temporary, format="PNG")
        os.replace(temporary, output)
    finally:
        if temporary.exists():
            temporary.unlink()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    save_atomically(normalize_palette(Image.open(args.input)), args.output)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
