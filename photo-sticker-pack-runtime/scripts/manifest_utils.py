from __future__ import annotations

from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import re
import unicodedata
from typing import Any, Dict, Iterable, List, Optional


DEFAULT_COLOR = "#2E429B"
EXPECTED_COUNTS = {
    "character_accessory": 3,
    "character_accessory_text": 2,
    "accessory_text": 2,
    "character_expression": 1,
}
TEXT_KINDS = {"character_accessory_text", "accessory_text"}
EXPECTED_KIND_SEQUENCE = (
    "character_accessory",
    "character_accessory",
    "character_accessory",
    "character_accessory_text",
    "character_accessory_text",
    "accessory_text",
    "accessory_text",
    "character_expression",
)
ARTIFACT_KEYS = ("raw_path", "ink_mask_path", "white_mask_path", "svg_path", "png_path")
PLAN_STRING_KEYS = ("kind", "action", "accessory", "expression", "caption", "prompt")
ALLOWED_STATUSES = {"planned", "generating", "generated", "processed", "complete", "failed"}


def _relative_paths(item_id: int, kind: str) -> Dict[str, str]:
    stem = f"{item_id:02d}-{kind.replace('_', '-')}"
    return {
        "raw_path": f"raw/{stem}.png",
        "ink_mask_path": f"work/{stem}-ink.png",
        "white_mask_path": f"work/{stem}-white.png",
        "svg_path": f"vectors/{stem}.svg",
        "png_path": f"stickers/{stem}.png",
    }


def _staged_relative_path(item_id: int, kind: str) -> str:
    stem = f"{item_id:02d}-{kind.replace('_', '-')}"
    return f"work/{stem}-imagegen-staged.png"


def _normalized_text(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(unicodedata.normalize("NFKC", value).split()).casefold()


def _validate_plan_items(items: Iterable[Dict[str, Any]]) -> List[str]:
    rows = list(items)
    errors: List[str] = []
    if len(rows) != 8:
        errors.append("manifest must contain exactly 8 items")
    ids = [row.get("id") for row in rows]
    if any(type(item_id) is not int for item_id in ids) or ids != list(range(1, 9)):
        errors.append("item ids must be the ordered integers 1 through 8")
    for position, row in enumerate(rows, start=1):
        item_id = row.get("id")
        label = item_id if type(item_id) is int else position
        for key in PLAN_STRING_KEYS:
            if not isinstance(row.get(key), str):
                errors.append(f"item {label} {key} must be a string")
    kinds = [row.get("kind") if isinstance(row.get("kind"), str) else None for row in rows]
    counts = Counter(kind for kind in kinds if kind is not None)
    if counts != Counter(EXPECTED_COUNTS):
        errors.append(f"kind counts must equal {EXPECTED_COUNTS}")
    if tuple(kinds) != EXPECTED_KIND_SEQUENCE:
        errors.append("items must use the exact ordered kind sequence")
    for row in rows:
        raw_caption = row.get("caption")
        caption = raw_caption.strip() if isinstance(raw_caption, str) else ""
        kind = row.get("kind")
        is_text_kind = isinstance(kind, str) and kind in TEXT_KINDS
        if is_text_kind and not caption:
            errors.append(f"item {row.get('id')} requires a caption")
        if not is_text_kind and caption:
            errors.append(f"item {row.get('id')} must not contain a caption")
        if caption.count("\n") > 1:
            errors.append(f"item {row.get('id')} caption exceeds two lines")
        if caption:
            cjk_count = len(re.findall(r"[\u3400-\u9fff]", caption))
            english_words = re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)?", caption)
            if cjk_count and not 2 <= cjk_count <= 8:
                errors.append(f"item {row.get('id')} Chinese caption must contain 2 to 8 characters")
            if not cjk_count and not 2 <= len(english_words) <= 4:
                errors.append(f"item {row.get('id')} English caption must contain 2 to 4 words")
            elif english_words and not 2 <= len(english_words) <= 4:
                errors.append(f"item {row.get('id')} English caption must contain 2 to 4 words")
            if not cjk_count and not english_words:
                errors.append(f"item {row.get('id')} caption must contain supported CJK or English content")
    actions = [_normalized_text(row.get("action")) for row in rows]
    if any(not action for action in actions):
        errors.append("actions must be non-empty")
    if len(actions) != len(set(actions)):
        errors.append("actions must be unique")
    captions = [
        _normalized_text(row.get("caption"))
        for row in rows
        if isinstance(row.get("kind"), str) and row.get("kind") in TEXT_KINDS
    ]
    if len(captions) != len(set(captions)):
        errors.append("captions must be unique")
    combinations = [
        (_normalized_text(row.get("action")), _normalized_text(row.get("accessory"))) for row in rows
    ]
    if len(combinations) != len(set(combinations)):
        errors.append("action and accessory combinations must be unique")
    return list(dict.fromkeys(errors))


def _validate_subject(subject: object) -> List[str]:
    if not isinstance(subject, dict):
        return ["subject must be an object"]
    visible_features = subject.get("visible_features")
    if not isinstance(visible_features, list) or any(
        not isinstance(feature, str) for feature in visible_features
    ):
        return ["subject visible_features must be a list of strings"]
    return []


def new_manifest(source_path: str, subject: Dict[str, Any], items: List[Dict[str, Any]]) -> Dict[str, Any]:
    errors: List[str] = []
    if not isinstance(source_path, str):
        errors.append("source_path must be a string")
    if not isinstance(subject, dict):
        errors.append("subject must be an object")
    else:
        subject = deepcopy(subject)
        subject.setdefault("visible_features", [])
        errors.extend(_validate_subject(subject))
    if not isinstance(items, list):
        errors.append("manifest items must be a list")
    elif any(not isinstance(row, dict) for row in items):
        errors.append("manifest items must contain only objects")
    else:
        errors.extend(_validate_plan_items(items))
    if errors:
        raise ValueError("; ".join(errors))
    output_items = []
    for row in deepcopy(items):
        row.update(_relative_paths(int(row["id"]), str(row["kind"])))
        row.update({"status": "planned", "representation": None, "retry_count": 0, "error": None})
        output_items.append(row)
    return {
        "version": 1,
        "default_color": DEFAULT_COLOR,
        "status": "planned",
        "source_path": source_path,
        "subject": deepcopy(subject),
        "items": output_items,
    }


def validate_manifest(data: Dict[str, Any], require_files: bool = False, pack_dir: Optional[Path] = None) -> List[str]:
    if not isinstance(data, dict):
        return ["manifest must be an object"]
    items = data.get("items", [])
    if not isinstance(items, list):
        return ["manifest items must be a list"]
    if any(not isinstance(row, dict) for row in items):
        return ["manifest items must contain only objects"]
    errors = _validate_plan_items(items)
    if not isinstance(data.get("source_path"), str):
        errors.append("source_path must be a string")
    errors.extend(_validate_subject(data.get("subject")))
    if type(data.get("version")) is not int or data.get("version") != 1:
        errors.append("version must be exact integer 1")
    if not isinstance(data.get("default_color"), str) or data.get("default_color") != DEFAULT_COLOR:
        errors.append(f"default_color must be the string {DEFAULT_COLOR}")
    if not isinstance(data.get("status"), str) or data.get("status") not in ALLOWED_STATUSES:
        errors.append("manifest status must be an allowed string")
    for position, row in enumerate(items, start=1):
        item_id = row.get("id")
        label = item_id if type(item_id) is int else position
        for key in ARTIFACT_KEYS:
            if not isinstance(row.get(key), str):
                errors.append(f"item {label} {key} must be a string")
        if not isinstance(row.get("status"), str) or row.get("status") not in ALLOWED_STATUSES:
            errors.append(f"item {label} status must be an allowed string")
        representation = row.get("representation")
        if representation is not None and (
            not isinstance(representation, str) or representation not in {"path", "mask"}
        ):
            errors.append(f"item {label} representation must be null, path, or mask")
        retry_count = row.get("retry_count")
        if type(retry_count) is not int or retry_count < 0:
            errors.append(f"item {label} retry_count must be a nonnegative integer")
        if row.get("error") is not None and not isinstance(row.get("error"), str):
            errors.append(f"item {label} error must be null or a string")
    if require_files:
        if pack_dir is None:
            errors.append("pack_dir is required when require_files is true")
        else:
            for row in items:
                for key in ("svg_path", "png_path"):
                    relative_path = row.get(key)
                    if not isinstance(relative_path, str):
                        errors.append(f"item {row.get('id')} {key} must be a string")
                    elif not (pack_dir / relative_path).is_file():
                        errors.append(f"missing {relative_path}")
    return list(dict.fromkeys(errors))


def save_manifest(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_manifest(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))
