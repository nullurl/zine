from __future__ import annotations

import base64
from copy import deepcopy
from io import BytesIO
from pathlib import Path
import re
import warnings
from typing import Dict, Tuple
from xml.etree import ElementTree as ET

from PIL import Image, ImageChops, ImageDraw, UnidentifiedImageError


SIZE = 1024
SVG_NS = "http://www.w3.org/2000/svg"
SVG = f"{{{SVG_NS}}}"
HEX_COLOR = re.compile(r"#[0-9A-Fa-f]{6}\Z")
RLE_RUN = re.compile(r"M([0-9]+) ([0-9]+)h([1-9][0-9]*)v1h-([0-9]+)z")
DATA_PNG = re.compile(r"data:image/png;base64,([A-Za-z0-9+/]*={0,2})\Z")

ET.register_namespace("", SVG_NS)


def compose_layers(white: Image.Image, ink: Image.Image, color: str) -> Image.Image:
    """Compose binary fixed-white and recolorable ink masks into exact RGBA pixels."""
    if white.size != ink.size or not HEX_COLOR.fullmatch(color):
        raise ValueError("layers require matching sizes and a six-digit HEX color")
    white = white.convert("L").point(lambda value: 255 if value >= 128 else 0)
    ink = ink.convert("L").point(lambda value: 255 if value >= 128 else 0)
    rgb = tuple(int(color[index:index + 2], 16) for index in (1, 3, 5))
    result = Image.new("RGBA", white.size, (0, 0, 0, 0))
    result.alpha_composite(Image.composite(Image.new("RGBA", white.size, (255, 255, 255, 255)), Image.new("RGBA", white.size), white))
    result.alpha_composite(Image.composite(Image.new("RGBA", ink.size, rgb + (255,)), Image.new("RGBA", ink.size), ink))
    return result


def _has_continuous_white_support(
    white: Image.Image, ink: Image.Image, radius: int = 32
) -> bool:
    """Return whether white contains the exact square dilation of ink."""
    binary_ink = ink.convert("L").point(lambda value: 255 if value >= 128 else 0)
    horizontal = Image.new("L", binary_ink.size, 0)
    for offset in range(-radius, radius + 1):
        horizontal = ImageChops.lighter(horizontal, ImageChops.offset(binary_ink, offset, 0))
    dilated = Image.new("L", binary_ink.size, 0)
    for offset in range(-radius, radius + 1):
        dilated = ImageChops.lighter(dilated, ImageChops.offset(horizontal, 0, offset))
    unsupported = ImageChops.subtract(dilated, white.convert("L"))
    return unsupported.getbbox() is None


def validate_rendered_png(
    path: Path, relative_path: str, white: Image.Image, ink: Image.Image, color: str
) -> list:
    """Validate the completed PNG palette, geometry, support, and SVG agreement."""
    errors = []
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(path) as source:
                if source.size != (SIZE, SIZE) or source.mode != "RGBA":
                    return [f"{relative_path} must be 1024x1024 RGBA"]
                source.load()
                image = source.copy()
    except (OSError, UnidentifiedImageError, RuntimeError, Image.DecompressionBombError, Image.DecompressionBombWarning):
        return [f"invalid PNG {relative_path}"]
    expected_palette = {
        (0, 0, 0, 0),
        (255, 255, 255, 255),
        tuple(int(color[index:index + 2], 16) for index in (1, 3, 5)) + (255,),
    }
    if not set(image.getdata()).issubset(expected_palette):
        errors.append(f"{relative_path} must use exact transparent, #FFFFFF, and {color} palette")
    alpha = image.getchannel("A")
    if any(image.getpixel(corner)[3] != 0 for corner in ((0, 0), (SIZE - 1, 0), (0, SIZE - 1), (SIZE - 1, SIZE - 1))):
        errors.append(f"{relative_path} must have transparent corners")
    if not set(alpha.getdata()).issubset({0, 255}):
        errors.append(f"{relative_path} alpha must be binary")
    coverage = (SIZE * SIZE - alpha.histogram()[0]) / (SIZE * SIZE)
    if not 0.01 <= coverage <= 0.90:
        errors.append(f"{relative_path} subject coverage must be between 1% and 90%")
    union = ImageChops.lighter(white, ink)
    bbox = union.getbbox()
    if bbox is None or min(bbox[0], bbox[1], SIZE - bbox[2], SIZE - bbox[3]) < 64:
        errors.append(f"{relative_path} must keep at least 64px outer safe area")
    if not _has_continuous_white_support(white, ink):
        errors.append(f"{relative_path} must keep about 32px continuous white support around ink")
    if ImageChops.difference(image, compose_layers(white, ink, color)).getbbox() is not None:
        errors.append(f"{relative_path} must exactly match its SVG white and ink layers")
    return errors


def _whitespace_only(element: ET.Element) -> None:
    if (element.text and element.text.strip()) or (element.tail and element.tail.strip()):
        raise ValueError("SVG contains unexpected text")


def _exact_attributes(element: ET.Element, allowed: set) -> None:
    if set(element.attrib) != allowed:
        raise ValueError("SVG contains unexpected or missing attributes")


def _rle_mask(value: object) -> Image.Image:
    if not isinstance(value, str) or not value:
        raise ValueError("SVG path must contain exported RLE runs")
    mask = Image.new("L", (SIZE, SIZE), 0)
    draw = ImageDraw.Draw(mask)
    position = 0
    while position < len(value):
        match = RLE_RUN.match(value, position)
        if match is None:
            raise ValueError("SVG path must contain only exported RLE runs")
        x, y, length, reverse = (int(part) for part in match.groups())
        if length != reverse or y >= SIZE or x + length > SIZE:
            raise ValueError("SVG path run is outside the 1024px canvas")
        draw.line((x, y, x + length - 1, y), fill=255)
        position = match.end()
    if mask.getbbox() is None:
        raise ValueError("SVG path layer must not be empty")
    return mask


def _mask_png(value: object) -> Image.Image:
    if not isinstance(value, str):
        raise ValueError("SVG image href must be an embedded PNG data URI")
    match = DATA_PNG.fullmatch(value)
    if not match:
        raise ValueError("SVG image href must be an embedded PNG data URI")
    try:
        data = base64.b64decode(match.group(1), validate=True)
    except ValueError as error:
        raise ValueError("SVG image href must contain valid base64") from error
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(BytesIO(data)) as image:
                if image.size != (SIZE, SIZE) or image.mode not in {"1", "L", "LA", "RGBA"}:
                    raise ValueError("SVG mask image must be a 1024px mask PNG")
                image.load()
                luminance = image.convert("L")
                effective = luminance
                if "A" in image.getbands():
                    effective = ImageChops.multiply(luminance, image.getchannel("A"))
    except (OSError, UnidentifiedImageError, Image.DecompressionBombError, Image.DecompressionBombWarning) as error:
        raise ValueError("SVG image href must contain a valid PNG mask") from error
    values = set(effective.getdata())
    if not values.issubset({0, 255}) or 255 not in values:
        raise ValueError("SVG mask image must be a non-empty binary mask")
    return effective


def _parse_root(svg_text: str, expected_color: str) -> ET.Element:
    if not isinstance(expected_color, str) or not HEX_COLOR.fullmatch(expected_color):
        raise ValueError("expected SVG color must be a six-digit HEX value")
    if re.search(r"<!\s*(?:DOCTYPE|ENTITY)|<!--|<\?(?!xml\s)", svg_text, re.IGNORECASE):
        raise ValueError("SVG contains disallowed XML declarations or content")
    try:
        root = ET.fromstring(svg_text)
    except ET.ParseError as error:
        raise ValueError("SVG must contain exactly one well-formed root") from error
    if root.tag != SVG + "svg":
        raise ValueError("SVG root namespace is invalid")
    _exact_attributes(root, {"width", "height", "viewBox", "style"})
    if (
        root.attrib.get("width") != str(SIZE)
        or root.attrib.get("height") != str(SIZE)
        or root.attrib.get("viewBox") != f"0 0 {SIZE} {SIZE}"
        or root.attrib.get("style") != f"color:{expected_color}"
    ):
        raise ValueError("SVG root must use 1024 dimensions and the pack default color")
    for element in root.iter():
        _whitespace_only(element)
    return root


def _decode_path(root: ET.Element) -> Tuple[Image.Image, Image.Image]:
    children = list(root)
    if len(children) != 2 or any(child.tag != SVG + "path" for child in children):
        raise ValueError("path representation must contain exactly two path layers")
    layers: Dict[str, Image.Image] = {}
    for child in children:
        _exact_attributes(child, {"fill", "d"})
        fill = child.attrib.get("fill")
        if fill not in {"#FFFFFF", "currentColor"} or fill in layers:
            raise ValueError("SVG paths must be unique fixed-white and currentColor layers")
        if list(child):
            raise ValueError("SVG path elements must not contain children")
        layers[fill] = _rle_mask(child.attrib.get("d"))
    if set(layers) != {"#FFFFFF", "currentColor"}:
        raise ValueError("SVG paths must be fixed-white and currentColor layers")
    return layers["#FFFFFF"], layers["currentColor"]


def _decode_mask(root: ET.Element) -> Tuple[Image.Image, Image.Image]:
    children = list(root)
    if len(children) != 3 or [child.tag for child in children] != [SVG + "defs", SVG + "rect", SVG + "rect"]:
        raise ValueError("mask representation must contain exported defs and two rect layers")
    defs = children[0]
    _exact_attributes(defs, set())
    masks: Dict[str, Image.Image] = {}
    for mask in list(defs):
        if mask.tag != SVG + "mask":
            raise ValueError("SVG defs may contain only exported masks")
        _exact_attributes(mask, {"id", "mask-type"})
        mask_id = mask.attrib.get("id")
        if mask_id not in {"white-mask", "ink-mask"} or mask_id in masks or mask.attrib.get("mask-type") != "luminance":
            raise ValueError("SVG mask is not an exported local mask")
        images = list(mask)
        if len(images) != 1 or images[0].tag != SVG + "image":
            raise ValueError("SVG mask must contain exactly one image")
        image = images[0]
        _exact_attributes(image, {"width", "height", "href"})
        if image.attrib.get("width") != str(SIZE) or image.attrib.get("height") != str(SIZE):
            raise ValueError("SVG image dimensions must be 1024")
        masks[mask_id] = _mask_png(image.attrib.get("href"))
    if set(masks) != {"white-mask", "ink-mask"}:
        raise ValueError("SVG masks must contain white-mask and ink-mask")
    expected_rects = (
        ("#FFFFFF", "url(#white-mask)"),
        ("currentColor", "url(#ink-mask)"),
    )
    for rect, (fill, mask_ref) in zip(children[1:], expected_rects):
        _exact_attributes(rect, {"width", "height", "fill", "mask"})
        if (
            rect.attrib.get("width") != str(SIZE)
            or rect.attrib.get("height") != str(SIZE)
            or rect.attrib.get("fill") != fill
            or rect.attrib.get("mask") != mask_ref
            or list(rect)
        ):
            raise ValueError("SVG rect is not an exported masked layer")
    return masks["white-mask"], masks["ink-mask"]


def decode_svg_layers(
    svg_text: str, representation: object, expected_color: str
) -> Tuple[ET.Element, Image.Image, Image.Image]:
    """Validate one exporter SVG and recover exact binary white/ink masks."""
    if not isinstance(representation, str) or representation not in {"path", "mask"}:
        raise ValueError("representation must be path or mask")
    root = _parse_root(svg_text, expected_color)
    if representation == "path":
        white, ink = _decode_path(root)
    else:
        white, ink = _decode_mask(root)
    return root, white, ink


def serialized_svg(root: ET.Element, color: str) -> str:
    copy = deepcopy(root)
    copy.attrib["style"] = f"color:{color}"
    return ET.tostring(copy, encoding="unicode", short_empty_elements=True)
