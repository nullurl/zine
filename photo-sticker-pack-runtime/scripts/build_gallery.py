from __future__ import annotations

import argparse
import base64
from copy import deepcopy
import html
from io import BytesIO
import json
import os
from pathlib import Path, PurePosixPath
import re
import math
import stat
import tempfile
import warnings
import zipfile
from xml.etree import ElementTree as ET

from PIL import Image, ImageChops, UnidentifiedImageError

from artifact_contract import safe_asset_path as _contract_safe_asset_path, validate_artifact_paths
from manifest_utils import load_manifest, validate_manifest
from svg_layers import decode_svg_layers, serialized_svg, validate_rendered_png


SVG_NS = "http://www.w3.org/2000/svg"
SVG = f"{{{SVG_NS}}}"
ZIP_NAME = "stickers-default-blue.zip"
PAPER_ASPECT_RATIO = 1200 / 1697
PAPER_HEIGHT = 100 / PAPER_ASPECT_RATIO
MIN_STICKER_GAP = 1.35
SCATTER_LAYOUT = (
    {"x": "35%", "y": "82%", "w": "21%", "r": "-1deg"},
    {"x": "5%", "y": "65%", "w": "19%", "r": "-2deg"},
    {"x": "5%", "y": "4%", "w": "48%", "r": "-1.5deg"},
    {"x": "69%", "y": "4%", "w": "24%", "r": "2.5deg"},
    {"x": "61%", "y": "34%", "w": "30%", "r": "1.5deg"},
    {"x": "6%", "y": "40%", "w": "24%", "r": "-2.5deg"},
    {"x": "76%", "y": "74%", "w": "18%", "r": "3deg"},
    {"x": "33%", "y": "59%", "w": "25%", "r": "-0.5deg"},
)
HEX_COLOR = re.compile(r"#[0-9A-Fa-f]{6}\Z")
PATH_DATA = re.compile(r"(?:[MmLlHhVvCcSsQqTtAaZz]|[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][-+]?\d+)?|[\s,])+\Z")
PATH_NUMBER = re.compile(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][-+]?\d+)?")
EXPORT_RLE_RUN = re.compile(r"M([0-9]+) ([0-9]+)h([1-9][0-9]*)v1h-([0-9]+)z")
DATA_PNG = re.compile(r"data:image/png;base64,([A-Za-z0-9+/]*={0,2})\Z")
WINDOWS_RESERVED_NAMES = {"CON", "PRN", "AUX", "NUL"} | {
    f"{prefix}{number}" for prefix in ("COM", "LPT") for number in range(1, 10)
}
WIN32_FORBIDDEN_CHARACTERS = set('<>"|?*')

ET.register_namespace("", SVG_NS)


def _safe_asset_path(pack_dir: Path, value: object, field: str) -> tuple[Path, str]:
    return _contract_safe_asset_path(pack_dir, value, field)


def _require_svg_tag(element: ET.Element, name: str) -> None:
    if element.tag != SVG + name:
        raise ValueError("SVG contains an unexpected element or namespace")


def _require_attributes(element: ET.Element, allowed: set[str]) -> None:
    for key in element.attrib:
        if key not in allowed:
            raise ValueError("SVG contains an unexpected or event attribute")


def _require_whitespace_only(element: ET.Element) -> None:
    if element.text and element.text.strip():
        raise ValueError("SVG contains unexpected text")
    if element.tail and element.tail.strip():
        raise ValueError("SVG contains unexpected text")


def _validate_data_png(value: str) -> bytes:
    match = DATA_PNG.fullmatch(value)
    if not match:
        raise ValueError("SVG image href must be an embedded PNG data URI")
    try:
        decoded = base64.b64decode(match.group(1), validate=True)
    except ValueError as error:
        raise ValueError("SVG image href must contain valid base64") from error
    if not decoded.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("SVG image href must contain PNG data")
    return decoded


def _validate_mask_png(data: bytes) -> None:
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(BytesIO(data)) as image:
                if image.size != (1024, 1024) or image.mode not in {"1", "L", "LA", "RGBA"}:
                    raise ValueError("SVG mask image must be a 1024px mask PNG")
                image.verify()
            with Image.open(BytesIO(data)) as image:
                image.load()
                luminance = image.convert("L")
                effective = luminance
                if "A" in image.getbands():
                    effective = ImageChops.multiply(luminance, image.getchannel("A"))
                if effective.getbbox() is None:
                    raise ValueError("SVG mask image must contain effective luminance")
    except (OSError, UnidentifiedImageError, ValueError, Image.DecompressionBombError, Image.DecompressionBombWarning) as error:
        if isinstance(error, ValueError) and str(error).startswith("SVG mask"):
            raise
        raise ValueError("SVG image href must contain a valid PNG mask") from error


def _validate_path_data(value: object) -> None:
    if not isinstance(value, str) or not value:
        raise ValueError("SVG path d uses unsupported data")
    tokens: list[str] = []
    position = 0
    while position < len(value):
        character = value[position]
        if character.isspace() or character == ",":
            position += 1
            continue
        if character in "MmLlHhVvCcSsQqTtAaZz":
            tokens.append(character)
            position += 1
            continue
        match = PATH_NUMBER.match(value, position)
        if match is None:
            raise ValueError("SVG path d uses unsupported data")
        number = match.group(0)
        if not math.isfinite(float(number)):
            raise ValueError("SVG path d contains a non-finite number")
        tokens.append(number)
        position = match.end()
    if not tokens or tokens[0] not in {"M", "m"}:
        raise ValueError("SVG path d must begin with moveto")

    arity = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7}
    index = 0
    command: str | None = None
    drawn = False
    while index < len(tokens):
        if tokens[index] in "MmLlHhVvCcSsQqTtAaZz":
            command = tokens[index]
            index += 1
            if command in "Zz":
                command = None
                continue
        if command is None:
            raise ValueError("SVG path d has operands without a command")
        upper = command.upper()
        count = arity[upper]
        groups = 0
        while index < len(tokens) and tokens[index] not in "MmLlHhVvCcSsQqTtAaZz":
            if index + count > len(tokens) or any(token in "MmLlHhVvCcSsQqTtAaZz" for token in tokens[index:index + count]):
                raise ValueError("SVG path d has incomplete command operands")
            values = tokens[index:index + count]
            if upper == "A":
                if float(values[0]) < 0 or float(values[1]) < 0 or values[3] not in {"0", "1"} or values[4] not in {"0", "1"}:
                    raise ValueError("SVG arc command has invalid radii or flags")
            if upper != "M" or groups > 0:
                drawn = True
            index += count
            groups += 1
        if groups == 0:
            raise ValueError("SVG path d has incomplete command operands")
    if not drawn:
        raise ValueError("SVG path d must contain renderable geometry")


def _validate_exported_rle_path(value: object) -> None:
    """Require the exact run grammar produced by vectorize_sticker.mask_to_path."""
    if not isinstance(value, str) or not value:
        raise ValueError("SVG path must contain exported RLE runs")
    position = 0
    while position < len(value):
        match = EXPORT_RLE_RUN.match(value, position)
        if match is None:
            raise ValueError("SVG path must contain only exported RLE runs")
        x, y, length, reverse_length = (int(part) for part in match.groups())
        if length != reverse_length or y >= 1024 or x + length > 1024:
            raise ValueError("SVG path run is outside the 1024px canvas")
        position = match.end()


def _sanitize_svg(svg_text: str, representation: str | None = None, expected_color: str | None = None) -> ET.Element:
    """Parse and strictly validate the limited SVG vocabulary exported by this skill."""
    if representation is not None and expected_color is not None:
        return decode_svg_layers(svg_text, representation, expected_color)[0]
    if re.search(r"<!\s*(?:DOCTYPE|ENTITY)|<!--|<\?(?!xml\s)", svg_text, re.IGNORECASE):
        raise ValueError("SVG contains disallowed XML declarations or content")
    try:
        root = ET.fromstring(svg_text)
    except ET.ParseError as error:
        raise ValueError("SVG must contain exactly one well-formed root") from error

    _require_svg_tag(root, "svg")
    _require_attributes(root, {"width", "height", "viewBox", "style"})
    style = root.attrib.get("style", "")
    if (
        root.attrib.get("width") != "1024"
        or root.attrib.get("height") != "1024"
        or root.attrib.get("viewBox") != "0 0 1024 1024"
        or not style.startswith("color:")
        or not HEX_COLOR.fullmatch(style[6:])
    ):
        raise ValueError("SVG root must use 1024 dimensions and a strict color style")
    if expected_color is not None and style != f"color:{expected_color}":
        raise ValueError("SVG root must use the pack default color")
    _require_whitespace_only(root)

    mask_ids: set[str] = set()
    rect_masks: dict[str, str] = {}
    mask_images: dict[str, int] = {}
    for element in root.iter():
        _require_whitespace_only(element)
        if element is root:
            continue
        if element.tag == SVG + "path":
            _require_attributes(element, {"fill", "d"})
            if element.attrib.get("fill") not in {"#FFFFFF", "currentColor"}:
                raise ValueError("SVG path fill is not allowed")
            _validate_path_data(element.attrib.get("d"))
            if representation == "path":
                _validate_exported_rle_path(element.attrib.get("d"))
        elif element.tag == SVG + "defs":
            _require_attributes(element, set())
        elif element.tag == SVG + "mask":
            _require_attributes(element, {"id", "mask-type"})
            mask_id = element.attrib.get("id")
            if mask_id not in {"white-mask", "ink-mask"} or element.attrib.get("mask-type") != "luminance":
                raise ValueError("SVG mask is not an exported local mask")
            if mask_id in mask_ids:
                raise ValueError("SVG mask ids must be unique")
            mask_ids.add(mask_id)
            mask_images[mask_id] = 0
        elif element.tag == SVG + "image":
            _require_attributes(element, {"width", "height", "href"})
            if element.attrib.get("width") != "1024" or element.attrib.get("height") != "1024":
                raise ValueError("SVG image dimensions must be 1024")
            data = _validate_data_png(element.attrib.get("href", ""))
            parent_is_mask = any(child is element for mask in root.iter(SVG + "mask") for child in mask)
            if parent_is_mask and representation is not None:
                _validate_mask_png(data)
        elif element.tag == SVG + "rect":
            _require_attributes(element, {"width", "height", "fill", "mask"})
            fill = element.attrib.get("fill")
            mask = element.attrib.get("mask")
            if (
                element.attrib.get("width") != "1024"
                or element.attrib.get("height") != "1024"
                or fill not in {"#FFFFFF", "currentColor"}
                or mask not in {"url(#white-mask)", "url(#ink-mask)"}
            ):
                raise ValueError("SVG rect is not an exported masked layer")
            rect_masks[fill] = mask
        else:
            raise ValueError("SVG contains an unexpected element or namespace")

        for child in element:
            if element is root and child.tag not in {SVG + "path", SVG + "defs", SVG + "rect"}:
                raise ValueError("SVG contains an unexpected element hierarchy")
            if element.tag == SVG + "defs" and child.tag != SVG + "mask":
                raise ValueError("SVG contains an unexpected element hierarchy")
            if element.tag == SVG + "mask" and child.tag != SVG + "image":
                raise ValueError("SVG contains an unexpected element hierarchy")
            if element.tag == SVG + "mask" and child.tag == SVG + "image":
                mask_images[element.attrib["id"]] += 1
            if element.tag in {SVG + "path", SVG + "image", SVG + "rect"}:
                raise ValueError("SVG contains an unexpected element hierarchy")

    if mask_ids and (
        mask_ids != {"white-mask", "ink-mask"}
        or rect_masks != {"#FFFFFF": "url(#white-mask)", "currentColor": "url(#ink-mask)"}
    ):
        raise ValueError("SVG masks must be the exported white and ink layers")
    if not mask_ids and rect_masks:
        raise ValueError("SVG rect layers require local masks")
    path_fills = {element.attrib.get("fill") for element in root if element.tag == SVG + "path"}
    if representation is not None and not mask_ids and path_fills != {"#FFFFFF", "currentColor"}:
        raise ValueError("SVG paths must be fixed white and currentColor layers")
    if representation == "path" and mask_ids:
        raise ValueError("path representation must not contain mask images")
    if representation == "mask" and not mask_ids:
        raise ValueError("mask representation must contain exported masks")
    if representation == "mask" and mask_images != {"white-mask": 1, "ink-mask": 1}:
        raise ValueError("mask representation must contain exactly one image per mask")
    return root


def _serialized_svg(root: ET.Element, color: str) -> str:
    return serialized_svg(root, color)


def _is_eligible(row: dict[str, object], svg_path: Path, png_path: Path) -> bool:
    return row.get("status") == "complete" and row.get("representation") in {"path", "mask"} and svg_path.is_file() and png_path.is_file()


def _layout_number(value: str, suffix: str) -> float:
    if not value.endswith(suffix):
        raise ValueError(f"layout value must end in {suffix}")
    return float(value.removesuffix(suffix))


def _rotated_layout_box(
    slot: dict[str, str], aspect_ratio: float
) -> tuple[float, float, float, float]:
    if not math.isfinite(aspect_ratio) or aspect_ratio <= 0:
        raise ValueError("sticker aspect ratio must be positive")
    x = _layout_number(slot["x"], "%")
    y = _layout_number(slot["y"], "%") / 100 * PAPER_HEIGHT
    width = _layout_number(slot["w"], "%")
    height = width / aspect_ratio
    radians = math.radians(_layout_number(slot["r"], "deg"))
    rotated_width = abs(width * math.cos(radians)) + abs(height * math.sin(radians))
    rotated_height = abs(width * math.sin(radians)) + abs(height * math.cos(radians))
    center_x = x + width / 2
    center_y = y + height / 2
    return (
        center_x - rotated_width / 2,
        center_y - rotated_height / 2,
        center_x + rotated_width / 2,
        center_y + rotated_height / 2,
    )


def _box_inside_paper(box: tuple[float, float, float, float]) -> bool:
    left, top, right, bottom = box
    return left >= 0 and top >= 0 and right <= 100 and bottom <= PAPER_HEIGHT


def _boxes_overlap(
    first: tuple[float, float, float, float],
    second: tuple[float, float, float, float],
    gap: float = 0,
) -> bool:
    return not (
        first[2] + gap <= second[0]
        or second[2] + gap <= first[0]
        or first[3] + gap <= second[1]
        or second[3] + gap <= first[1]
    )


def _candidate_offsets() -> list[tuple[float, float]]:
    steps = range(-20, 21)
    offsets = [(x * 1.5, y * 1.5) for x in steps for y in steps]
    return sorted(
        offsets,
        key=lambda offset: (
            offset[0] * offset[0] + offset[1] * offset[1],
            abs(offset[1]),
            abs(offset[0]),
            0 if offset[1] >= 0 else 1,
            0 if offset[0] >= 0 else 1,
        ),
    )


def _resolve_scatter_layout(
    aspect_ratios: tuple[float, ...] | list[float],
) -> tuple[dict[str, str], ...]:
    if len(aspect_ratios) != len(SCATTER_LAYOUT):
        raise ValueError("scatter layout requires exactly eight aspect ratios")
    if any(not math.isfinite(value) or value <= 0 for value in aspect_ratios):
        raise ValueError("sticker aspect ratios must be positive")

    resolved: list[dict[str, str] | None] = [None] * len(SCATTER_LAYOUT)
    boxes: list[tuple[float, float, float, float]] = []
    # Place the large visual anchors first, then let smaller supporting pieces
    # make the shortest deterministic move needed to preserve white space.
    placement_order = (2, 4, 7, 3, 5, 1, 6, 0)
    offsets = _candidate_offsets()
    scales = (1.0, 0.96, 0.92, 0.88, 0.84, 0.80)

    for index in placement_order:
        preferred = SCATTER_LAYOUT[index]
        preferred_x = _layout_number(preferred["x"], "%")
        preferred_y = _layout_number(preferred["y"], "%") / 100 * PAPER_HEIGHT
        preferred_width = _layout_number(preferred["w"], "%")
        rotation = preferred["r"]
        selected = None
        selected_box = None
        for scale in scales:
            width = preferred_width * scale
            for offset_x, offset_y in offsets:
                candidate = {
                    "x": f"{preferred_x + offset_x:.2f}%",
                    "y": f"{(preferred_y + offset_y) / PAPER_HEIGHT * 100:.2f}%",
                    "w": f"{width:.2f}%",
                    "r": rotation,
                }
                box = _rotated_layout_box(candidate, aspect_ratios[index])
                if not _box_inside_paper(box):
                    continue
                if any(_boxes_overlap(box, placed, MIN_STICKER_GAP) for placed in boxes):
                    continue
                selected = candidate
                selected_box = box
                break
            if selected is not None:
                break
        if selected is None or selected_box is None:
            raise ValueError(f"could not find a collision-free layout for sticker {index + 1}")
        resolved[index] = selected
        boxes.append(selected_box)

    return tuple(slot for slot in resolved if slot is not None)


def _scatter_style(
    item_id: int,
    aspect_ratio: float = 1.0,
    resolved_layout: tuple[dict[str, str], ...] | None = None,
) -> str:
    slot = (resolved_layout or SCATTER_LAYOUT)[item_id - 1]
    values = {**slot, "ar": f"{aspect_ratio:.4f}"}
    return ";".join(f"--{name}:{value}" for name, value in values.items())


def _preview_bounds(mask: Image.Image, padding: int = 16) -> tuple[int, int, int, int]:
    bbox = mask.getbbox()
    if bbox is None:
        raise ValueError("sticker preview mask is empty")
    left, top, right, bottom = bbox
    return (
        max(0, left - padding),
        max(0, top - padding),
        min(1024, right + padding),
        min(1024, bottom + padding),
    )


def _preview_svg(root: ET.Element, bounds: tuple[int, int, int, int]) -> str:
    left, top, right, bottom = bounds
    preview = deepcopy(root)
    preview.attrib["width"] = str(right - left)
    preview.attrib["height"] = str(bottom - top)
    preview.attrib["viewBox"] = f"{left} {top} {right - left} {bottom - top}"
    preview.attrib["style"] = "color:var(--ink)"
    return ET.tostring(preview, encoding="unicode", short_empty_elements=True)


def _template_output(template_path: Path, cards: list[str], payload: str) -> str:
    template = template_path.read_text(encoding="utf-8")
    if template.count("__PACK_JSON__") != 1 or template.count("__CARDS__") != 1:
        raise ValueError("gallery template must contain each marker exactly once")
    if template.index("__CARDS__") > template.index("__PACK_JSON__"):
        raise ValueError("gallery template must place cards marker before PACK marker")
    if template.count("__THREE_JS__") != 1:
        raise ValueError("gallery template must contain the Three.js marker exactly once")
    vendor_path = template_path.with_name("three.min.js")
    try:
        vendor_stat = vendor_path.lstat()
    except OSError as error:
        raise ValueError("gallery Three.js runtime is unavailable") from error
    if vendor_path.is_symlink() or not stat.S_ISREG(vendor_stat.st_mode):
        raise ValueError("gallery Three.js runtime must be a regular file")
    vendor = vendor_path.read_text(encoding="utf-8")
    if not vendor or re.search(r"</script", vendor, re.IGNORECASE):
        raise ValueError("gallery Three.js runtime is unsafe to inline")
    before_cards, after_cards = template.split("__CARDS__", 1)
    between_markers, after_pack = after_cards.split("__PACK_JSON__", 1)
    output = before_cards + "\n".join(cards) + between_markers + payload + after_pack
    return output.replace("__THREE_JS__", vendor, 1)


def _final_is_regular_or_absent(path: Path) -> bool:
    """Return whether a final exists, rejecting symlinks and non-regular nodes via lstat."""
    try:
        file_stat = path.lstat()
    except FileNotFoundError:
        return False
    except OSError as error:
        raise ValueError(f"{path.name} cannot be inspected safely") from error
    if not stat.S_ISREG(file_stat.st_mode):
        raise ValueError(f"{path.name} must be an existing regular file or be absent")
    return True


def _exclusive_path(pack_dir: Path, label: str, suffix: str = ".tmp") -> tuple[int, Path]:
    fd, value = tempfile.mkstemp(prefix=f".{label}.", suffix=suffix, dir=str(pack_dir))
    return fd, Path(value)


def _cleanup_paths(paths: list[Path]) -> None:
    for path in paths:
        try:
            path.unlink()
        except FileNotFoundError:
            pass


def _backup_final(path: Path, existed: bool, cleanup: list[Path]) -> Path | None:
    if not existed:
        return None
    fd, backup = _exclusive_path(path.parent, f"{path.name}.backup")
    os.close(fd)
    cleanup.append(backup)
    os.replace(path, backup)
    return backup


def _rollback_final(path: Path, backup: Path | None, published: bool) -> None:
    backup_exists = False
    if backup is not None:
        try:
            backup.lstat()
            backup_exists = True
        except FileNotFoundError:
            pass
    if backup_exists:
        os.replace(backup, path)
    elif published:
        try:
            path.unlink()
        except FileNotFoundError:
            pass


def _verify_zip(path: Path, expected_names: list[str]) -> None:
    with zipfile.ZipFile(path) as archive:
        if archive.namelist() != expected_names or archive.testzip() is not None:
            raise ValueError("default ZIP verification failed")


def build_gallery(pack_dir: Path, template_path: Path) -> Path:
    pack_dir = Path(pack_dir).resolve(strict=True)
    manifest_path = pack_dir / "manifest.json"
    if manifest_path.is_symlink():
        raise ValueError("manifest.json must not be a symlink")
    manifest = load_manifest(manifest_path)
    errors = validate_manifest(manifest)
    if errors:
        raise ValueError("; ".join(errors))

    artifact_rows, path_errors = validate_artifact_paths(pack_dir, manifest["items"])
    if path_errors:
        raise ValueError("; ".join(path_errors))
    assets = []
    for row, resolved in zip(manifest["items"], artifact_rows):
        svg_path = resolved["svg_path"]
        png_path = resolved["png_path"]
        svg_name = str(row["svg_path"])
        png_name = str(row["png_path"])
        assets.append((row, svg_path, png_path, svg_name, png_name))
    normalized_names = [name.casefold() for _, _, _, svg_name, png_name in assets for name in (svg_name, png_name)]
    if len(normalized_names) != len(set(normalized_names)):
        raise ValueError("duplicate normalized asset path")
    browser_stems = [Path(svg_name).stem.casefold() for _, _, _, svg_name, _ in assets]
    if len(browser_stems) != len(set(browser_stems)):
        raise ValueError("duplicate browser ZIP stem")

    prepared = []
    for row, svg_path, png_path, svg_name, png_name in assets:
        if not _is_eligible(row, svg_path, png_path):
            prepared.append(
                {
                    "row": row,
                    "eligible": False,
                    "aspect_ratio": 1.0,
                }
            )
            continue
        try:
            root, white, ink = decode_svg_layers(
                svg_path.read_text(encoding="utf-8"), row.get("representation"), manifest["default_color"]
            )
        except (OSError, UnicodeDecodeError, ValueError, RuntimeError) as error:
            raise ValueError(f"invalid SVG {svg_name}: {error}") from error
        png_errors = validate_rendered_png(
            png_path, png_name, white, ink, manifest["default_color"]
        )
        if png_errors:
            raise ValueError("; ".join(png_errors))
        svg_text = _serialized_svg(root, manifest["default_color"])
        bounds = _preview_bounds(white)
        preview_width = bounds[2] - bounds[0]
        preview_height = bounds[3] - bounds[1]
        prepared.append(
            {
                "row": row,
                "eligible": True,
                "root": root,
                "svg_text": svg_text,
                "svg_name": svg_name,
                "bounds": bounds,
                "aspect_ratio": preview_width / preview_height,
            }
        )

    resolved_layout = _resolve_scatter_layout(
        [float(entry["aspect_ratio"]) for entry in prepared]
    )
    items = []
    cards = []
    for entry in prepared:
        row = entry["row"]
        label = html.escape(row["caption"] or f"贴图 {row['id']}", quote=True)
        style = html.escape(
            _scatter_style(
                int(row["id"]),
                float(entry["aspect_ratio"]),
                resolved_layout,
            ),
            quote=True,
        )
        if not entry["eligible"]:
            cards.append(
                f'<div class="sticker missing" style="{style}" '
                f'aria-label="{label}，尚未生成"><span>尚未生成</span></div>'
            )
            continue
        root = entry["root"]
        bounds = entry["bounds"]
        svg_name = entry["svg_name"]
        svg_text = entry["svg_text"]
        preview_svg = _preview_svg(root, bounds)
        stem = Path(svg_name).stem
        items.append({"id": row["id"], "stem": stem, "caption": row["caption"], "svg": svg_text})
        cards.append(
            f'<button class="sticker" type="button" style="{style}" '
            f'data-download-id="{int(row["id"])}" aria-label="下载 {label} PNG">'
            f'<span class="sticker-face">{preview_svg}</span>'
            f'<span class="sr-only">点击揭下并下载 PNG</span></button>'
        )

    complete = manifest.get("status") == "complete" and len(items) == 8
    payload = json.dumps({"defaultColor": manifest["default_color"], "complete": complete, "items": items}, ensure_ascii=False).replace("</", "<\\/")
    destination = pack_dir / "index.html"
    zip_path = pack_dir / ZIP_NAME
    old_index_exists = _final_is_regular_or_absent(destination)
    old_zip_exists = _final_is_regular_or_absent(zip_path)
    output = _template_output(template_path, cards, payload)
    cleanup: list[Path] = []
    index_fd, temp_index_path = _exclusive_path(pack_dir, "index.html", suffix=".html.tmp")
    cleanup.append(temp_index_path)
    try:
        with os.fdopen(index_fd, "w", encoding="utf-8") as staged_index:
            staged_index.write(output)
        if temp_index_path.read_text(encoding="utf-8") != output:
            raise ValueError("gallery HTML staging verification failed")

        temp_zip_path: Path | None = None
        if complete:
            zip_fd, temp_zip_path = _exclusive_path(
                pack_dir, "stickers-default-blue", suffix=".zip.tmp"
            )
            cleanup.append(temp_zip_path)
            with os.fdopen(zip_fd, "w+b") as staged_zip:
                with zipfile.ZipFile(
                    staged_zip, "w", compression=zipfile.ZIP_DEFLATED
                ) as archive:
                    for _, svg_path, png_path, svg_name, png_name in assets:
                        archive.write(svg_path, arcname=svg_name)
                        archive.write(png_path, arcname=png_name)
            expected_names = [
                name
                for _, _, _, svg_name, png_name in assets
                for name in (svg_name, png_name)
            ]
            _verify_zip(temp_zip_path, expected_names)

        index_backup = None
        zip_backup = None
        index_published = False
        zip_published = False
        try:
            index_backup = _backup_final(destination, old_index_exists, cleanup)
            if complete:
                zip_backup = _backup_final(zip_path, old_zip_exists, cleanup)
            os.replace(temp_index_path, destination)
            index_published = True
            if complete:
                os.replace(temp_zip_path, zip_path)
                zip_published = True
            elif old_zip_exists:
                zip_backup = _backup_final(zip_path, True, cleanup)
        except Exception as publish_error:
            rollback_errors = []
            for final, backup, published in (
                (zip_path, zip_backup, zip_published),
                (destination, index_backup, index_published),
            ):
                try:
                    _rollback_final(final, backup, published)
                except Exception as rollback_error:
                    rollback_errors.append(str(rollback_error))
                    if backup is not None and backup in cleanup:
                        cleanup.remove(backup)
            if rollback_errors:
                raise RuntimeError(
                    "gallery derivative rollback failed: " + "; ".join(rollback_errors)
                ) from publish_error
            raise
    finally:
        _cleanup_paths(cleanup)
    return destination


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack_dir", type=Path)
    parser.add_argument("--template", required=True, type=Path)
    args = parser.parse_args()
    print(build_gallery(args.pack_dir, args.template))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
