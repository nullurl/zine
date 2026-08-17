from __future__ import annotations

from pathlib import Path, PurePosixPath
import stat
from typing import Dict, Iterable, List, Tuple

from manifest_utils import ARTIFACT_KEYS, _relative_paths


WINDOWS_RESERVED_NAMES = {"CON", "PRN", "AUX", "NUL"} | {
    f"{prefix}{number}" for prefix in ("COM", "LPT") for number in range(1, 10)
}
WIN32_FORBIDDEN_CHARACTERS = set('<>"|?*')


def safe_asset_path(pack_dir: Path, value: object, field: str) -> Tuple[Path, str]:
    """Resolve one portable relative path without following symlink components."""
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError(f"{field} must use a safe relative path")
    relative = PurePosixPath(value)
    if relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
        raise ValueError(f"{field} must use a safe relative path")
    for component in relative.parts:
        basename = component.split(".", 1)[0].rstrip(" ").upper()
        if (
            ":" in component
            or any(character in WIN32_FORBIDDEN_CHARACTERS for character in component)
            or component.endswith((" ", "."))
            or any(ord(character) < 32 or ord(character) == 127 for character in component)
            or basename in WINDOWS_RESERVED_NAMES
        ):
            raise ValueError(f"{field} must use a safe relative path")
    try:
        root = Path(pack_dir).resolve(strict=True)
    except (OSError, RuntimeError) as error:
        raise ValueError("pack_dir cannot be resolved safely") from error

    current = root
    for component in relative.parts:
        current = current / component
        try:
            if current.is_symlink():
                raise ValueError(f"{field} must not contain a symlink")
        except OSError as error:
            raise ValueError(f"{field} cannot be resolved safely") from error
    try:
        candidate = (root / Path(*relative.parts)).resolve(strict=False)
        normalized = candidate.relative_to(root)
    except (OSError, RuntimeError, ValueError) as error:
        raise ValueError(f"{field} must stay within pack_dir") from error
    if normalized == Path("."):
        raise ValueError(f"{field} must use a non-empty relative path")
    return candidate, normalized.as_posix()


def canonical_write_paths(pack_dir: Path, row: Dict[str, object]) -> Dict[str, Path]:
    """Derive trusted write targets from id/kind, never from stored artifact paths."""
    item_id = row.get("id")
    kind = row.get("kind")
    if type(item_id) is not int or not isinstance(kind, str):
        raise ValueError("item id and kind are required for canonical paths")
    result: Dict[str, Path] = {}
    for key, relative in _relative_paths(item_id, kind).items():
        path = safe_asset_path(pack_dir, relative, key)[0]
        try:
            file_stat = path.lstat()
        except FileNotFoundError:
            pass
        except OSError as error:
            raise ValueError(f"{key} cannot be inspected safely") from error
        else:
            if stat.S_ISREG(file_stat.st_mode) and file_stat.st_nlink != 1:
                raise ValueError(f"{key} must not be a hardlink (link count must equal 1)")
        result[key] = path
    return result


def validate_artifact_paths(
    pack_dir: Path, rows: Iterable[Dict[str, object]]
) -> Tuple[List[Dict[str, Path]], List[str]]:
    """Validate every stored artifact field and reject aliases deterministically."""
    resolved_rows: List[Dict[str, Path]] = []
    errors: List[str] = []
    seen_names: Dict[str, Tuple[object, str]] = {}
    seen_files: Dict[Path, Tuple[object, str]] = {}
    seen_inodes: Dict[Tuple[int, int], Tuple[object, str]] = {}
    for row in rows:
        item_id = row.get("id")
        kind = row.get("kind")
        expected = _relative_paths(item_id, kind) if type(item_id) is int and isinstance(kind, str) else {}
        resolved: Dict[str, Path] = {}
        for key in ARTIFACT_KEYS:
            value = row.get(key)
            if value != expected.get(key):
                errors.append(f"item {item_id} {key} must use its canonical deterministic path")
            try:
                path, normalized = safe_asset_path(pack_dir, value, key)
            except (ValueError, OSError, RuntimeError) as error:
                detail = str(error)
                label = "symlink" if "symlink" in detail else "safe non-symlink path"
                errors.append(f"item {item_id} {key} must be a {label}")
                continue
            resolved[key] = path
            folded = normalized.casefold()
            if folded in seen_names:
                other_id, other_key = seen_names[folded]
                errors.append(
                    f"item {item_id} {key} duplicates item {other_id} {other_key} after case-folding"
                )
            else:
                seen_names[folded] = (item_id, key)
            if path in seen_files:
                other_id, other_key = seen_files[path]
                errors.append(
                    f"item {item_id} {key} resolves to the same file as item {other_id} {other_key}"
                )
            else:
                seen_files[path] = (item_id, key)
            try:
                file_stat = path.lstat()
            except FileNotFoundError:
                continue
            except OSError:
                errors.append(f"item {item_id} {key} cannot be inspected safely")
                continue
            if stat.S_ISREG(file_stat.st_mode):
                if file_stat.st_nlink != 1:
                    errors.append(
                        f"item {item_id} {key} must not be a hardlink (link count is {file_stat.st_nlink})"
                    )
                inode = (file_stat.st_dev, file_stat.st_ino)
                if inode in seen_inodes:
                    other_id, other_key = seen_inodes[inode]
                    errors.append(
                        f"item {item_id} {key} hardlinks item {other_id} {other_key} to the same inode"
                    )
                else:
                    seen_inodes[inode] = (item_id, key)
        resolved_rows.append(resolved)
    return resolved_rows, list(dict.fromkeys(errors))
