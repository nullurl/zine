from __future__ import annotations

import argparse
from contextlib import contextmanager
import fcntl
import json
import os
from pathlib import Path
import secrets
import stat
import tempfile
from typing import Dict
import warnings

from PIL import Image, UnidentifiedImageError

from artifact_contract import safe_asset_path, validate_artifact_paths
from manifest_utils import _staged_relative_path, load_manifest, validate_manifest
from svg_layers import decode_svg_layers, validate_rendered_png


DECISION_TRANSITIONS = {
    "skip": {
        "normalize_status": None,
        "operation": None,
        "success_status": None,
    },
    "chroma": {
        "normalize_status": "generating",
        "operation": "remove_chroma_key",
        "success_status": "generating",
    },
    "gate": {
        "normalize_status": "generating",
        "operation": "quality_gate",
        "success_status": "generated",
    },
    "fail": {
        "normalize_status": "failed",
        "operation": None,
        "success_status": None,
    },
    "process": {
        "normalize_status": "generated",
        "operation": "postprocess_and_vectorize",
        "success_status": "processed",
    },
    "finalize": {
        "normalize_status": "processed",
        "operation": "verify",
        "success_status": "complete",
    },
    "generate": {
        "normalize_status": "generating",
        "operation": "image_gen",
        "success_status": "generating",
    },
}


def decision_transition(decision: str) -> Dict[str, object]:
    """Return the executable status/operation contract for a resume decision."""
    if decision not in DECISION_TRANSITIONS:
        raise ValueError(f"unknown resume decision: {decision}")
    return dict(DECISION_TRANSITIONS[decision])


def staged_relative_path(row: Dict[str, object]) -> str:
    item_id = row.get("id")
    kind = row.get("kind")
    if type(item_id) is not int or not isinstance(kind, str):
        raise ValueError("item id and kind are required for a staged path")
    return _staged_relative_path(item_id, kind)


def _atomic_replace_manifest(manifest_path: Path, manifest: Dict[str, object]) -> None:
    original_mode = stat.S_IMODE(manifest_path.stat().st_mode)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=manifest_path.parent,
        prefix=f".{manifest_path.name}.",
        suffix=".tmp",
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as output:
            json.dump(manifest, output, ensure_ascii=False, indent=2)
            output.write("\n")
            output.flush()
            os.fsync(output.fileno())
        os.chmod(temporary_path, original_mode)
        os.replace(temporary_path, manifest_path)
    finally:
        try:
            temporary_path.unlink()
        except FileNotFoundError:
            pass


def _compact_error(failure: str, reasons: list[str]) -> str:
    return json.dumps(
        {failure: reasons}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
    )


def _retry_reservation_error(
    failure: str,
    reasons: list[str],
    phase: str,
    quarantine_paths: list[str],
    token: str,
) -> str:
    return json.dumps(
        {
            "retry_reservation": {
                "failure": failure,
                "phase": phase,
                "quarantine_paths": quarantine_paths,
                "reasons": reasons,
                "token": token,
            }
        },
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )


def _valid_retry_token(token: object) -> bool:
    return (
        isinstance(token, str)
        and len(token) == 64
        and all(character in "0123456789abcdef" for character in token)
    )


def _retry_reservation(row: Dict[str, object]) -> Dict[str, object] | None:
    if row.get("retry_count") != 1:
        return None
    error = row.get("error")
    if not isinstance(error, str):
        return None
    try:
        payload = json.loads(error)
    except (json.JSONDecodeError, TypeError):
        return None
    if not isinstance(payload, dict) or set(payload) != {"retry_reservation"}:
        return None
    reservation = payload["retry_reservation"]
    if not isinstance(reservation, dict) or set(reservation) != {
        "failure",
        "phase",
        "quarantine_paths",
        "reasons",
        "token",
    }:
        return None
    failure = reservation["failure"]
    phase = reservation["phase"]
    quarantine_paths = reservation["quarantine_paths"]
    reasons = reservation["reasons"]
    token = reservation["token"]
    if failure not in {"generation", "quality_gate"}:
        return None
    if phase not in {
        "invalidation_in_progress",
        "authorized",
        "raw_ready",
        "cleanup_failed",
    }:
        return None
    if not isinstance(quarantine_paths, list) or any(
        not isinstance(path, str) or not path for path in quarantine_paths
    ):
        return None
    if len(quarantine_paths) != len(set(quarantine_paths)):
        return None
    if not isinstance(reasons, list) or not reasons or any(
        not isinstance(reason, str) or not reason for reason in reasons
    ):
        return None
    if not _valid_retry_token(token):
        return None
    return reservation


def _retry_reservation_phase(row: Dict[str, object]) -> str | None:
    reservation = _retry_reservation(row)
    return None if reservation is None else str(reservation["phase"])


def _retry_reservation_active(row: Dict[str, object]) -> bool:
    return (
        row.get("status") == "generating"
        and _retry_reservation_phase(row) == "authorized"
    )


def _retry_terminal_failure(row: Dict[str, object]) -> bool:
    if row.get("status") != "failed" or row.get("retry_count") != 1:
        return False
    error = row.get("error")
    if not isinstance(error, str):
        return False
    try:
        payload = json.loads(error)
    except (json.JSONDecodeError, TypeError):
        return False
    if not isinstance(payload, dict) or len(payload) != 1:
        return False
    failure, reasons = next(iter(payload.items()))
    return failure in {"generation", "quality_gate", "retry_invalidation"} and isinstance(
        reasons, list
    ) and bool(reasons) and all(isinstance(reason, str) and reason for reason in reasons)


def _validate_retry_artifact(path: Path, label: str) -> bool:
    try:
        file_stat = path.lstat()
    except FileNotFoundError:
        return False
    except OSError as error:
        raise ValueError(f"{label} cannot be inspected safely") from error
    if stat.S_ISLNK(file_stat.st_mode) or not stat.S_ISREG(file_stat.st_mode):
        raise ValueError(f"{label} must be a regular non-symlink file")
    if file_stat.st_nlink != 1:
        raise ValueError(f"{label} must not be a hardlink")
    return True


def _retry_quarantine_paths(row: Dict[str, object]) -> Dict[str, str]:
    item_id = row.get("id")
    kind = row.get("kind")
    if type(item_id) is not int or not isinstance(kind, str):
        raise ValueError("item id and kind are required for retry quarantine paths")
    stem = f"{item_id:02d}-{kind.replace('_', '-')}"
    return {
        "raw_path": f"work/.retry-quarantine/{stem}-raw.quarantine",
        "staged_path": f"work/.retry-quarantine/{stem}-staged.quarantine",
    }


def _prepare_retry_quarantine_directory(pack_dir: Path) -> None:
    directory, _ = safe_asset_path(
        pack_dir, "work/.retry-quarantine", "retry_quarantine_dir"
    )
    directory.mkdir(parents=True, exist_ok=True)
    directory_stat = directory.lstat()
    if stat.S_ISLNK(directory_stat.st_mode) or not stat.S_ISDIR(directory_stat.st_mode):
        raise ValueError("retry quarantine directory must be a real directory")


def _quarantine_retry_artifact(
    path: Path, label: str, quarantine_path: Path
) -> Path:
    if not _validate_retry_artifact(path, label):
        raise ValueError(f"{label} disappeared before quarantine")
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(quarantine_path, flags, 0o600)
    except OSError as error:
        raise ValueError(f"{label} quarantine destination is unsafe") from error
    try:
        destination_stat = os.fstat(descriptor)
        if not stat.S_ISREG(destination_stat.st_mode) or destination_stat.st_nlink != 1:
            raise ValueError(f"{label} quarantine destination is unsafe")
    finally:
        os.close(descriptor)
    try:
        os.replace(path, quarantine_path)
    except (OSError, RuntimeError) as error:
        try:
            quarantine_path.unlink()
        except FileNotFoundError:
            pass
        raise ValueError(f"{label} could not be quarantined") from error
    return quarantine_path


def _remove_retry_artifact(path: Path, label: str) -> None:
    if not _validate_retry_artifact(path, label):
        return
    try:
        path.unlink()
    except (OSError, RuntimeError) as error:
        raise ValueError(f"{label} could not be removed safely") from error


def _cleanup_retry_quarantine_directory(
    pack_dir: Path, manifest: Dict[str, object]
) -> None:
    directory, normalized = safe_asset_path(
        pack_dir, "work/.retry-quarantine", "retry_quarantine_dir"
    )
    try:
        directory_stat = directory.lstat()
    except FileNotFoundError:
        return
    except OSError as error:
        raise ValueError("retry quarantine directory cannot be inspected") from error
    if stat.S_ISLNK(directory_stat.st_mode) or not stat.S_ISDIR(directory_stat.st_mode):
        raise ValueError("retry quarantine directory must be a real directory")

    expected_remaining = set()
    for other_row in manifest["items"]:
        other_reservation = _retry_reservation(other_row)
        if other_reservation is None or other_reservation["phase"] not in {
            "invalidation_in_progress",
            "authorized",
            "cleanup_failed",
        }:
            continue
        allowed = set(_retry_quarantine_paths(other_row).values())
        expected_remaining.update(
            path
            for path in other_reservation["quarantine_paths"]
            if path in allowed
        )

    try:
        entries = list(directory.iterdir())
    except OSError as error:
        raise ValueError("retry quarantine directory cannot be listed") from error
    for entry in entries:
        relative = f"{normalized}/{entry.name}"
        if relative not in expected_remaining:
            raise ValueError("retry quarantine directory contains unexpected residue")
        if not _validate_retry_artifact(entry, "retry_quarantine_residue"):
            raise ValueError("retry quarantine residue disappeared")
    if entries:
        return
    try:
        directory.rmdir()
    except OSError as error:
        raise ValueError("empty retry quarantine directory could not be removed") from error


@contextmanager
def _candidate_retry_lock(manifest_path: Path):
    candidate = manifest_path.parent
    try:
        candidate_stat = candidate.lstat()
    except OSError as error:
        raise ValueError("retry candidate cannot be inspected safely") from error
    if stat.S_ISLNK(candidate_stat.st_mode) or not stat.S_ISDIR(candidate_stat.st_mode):
        raise ValueError("retry candidate must be a real directory")
    try:
        resolved_candidate = candidate.resolve(strict=True)
    except (OSError, RuntimeError) as error:
        raise ValueError("retry candidate cannot be resolved safely") from error
    lock_path = resolved_candidate.parent / f".{resolved_candidate.name}.retry.lock"
    flags = os.O_RDWR | os.O_CREAT
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(lock_path, flags, 0o600)
    except OSError as error:
        raise ValueError("retry lock cannot be opened safely") from error
    try:
        descriptor_stat = os.fstat(descriptor)
        path_stat = lock_path.lstat()
        if (
            not stat.S_ISREG(descriptor_stat.st_mode)
            or descriptor_stat.st_nlink != 1
            or stat.S_ISLNK(path_stat.st_mode)
            or not stat.S_ISREG(path_stat.st_mode)
            or path_stat.st_nlink != 1
            or (descriptor_stat.st_dev, descriptor_stat.st_ino)
            != (path_stat.st_dev, path_stat.st_ino)
        ):
            raise ValueError("retry lock must be one regular non-linked file")
        fcntl.flock(descriptor, fcntl.LOCK_EX)
        descriptor_stat = os.fstat(descriptor)
        path_stat = lock_path.lstat()
        if (
            descriptor_stat.st_nlink != 1
            or path_stat.st_nlink != 1
            or (descriptor_stat.st_dev, descriptor_stat.st_ino)
            != (path_stat.st_dev, path_stat.st_ino)
        ):
            raise ValueError("retry lock changed while waiting")
        yield
    finally:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
        finally:
            os.close(descriptor)


def reserve_retry(
    manifest_path: Path,
    item_id: int,
    failure: str,
    reasons: list[str],
) -> bool:
    """Atomically consume the one shared Image Gen retry before a caller invokes it."""
    manifest_path = Path(manifest_path)
    if manifest_path.name != "manifest.json":
        raise ValueError("retry manifest must be named manifest.json")
    if not manifest_path.parent.name.endswith(".candidate"):
        raise ValueError("retry reservation requires a candidate manifest")
    with _candidate_retry_lock(manifest_path):
        return _reserve_retry_locked(manifest_path, item_id, failure, reasons)


def _reserve_retry_locked(
    manifest_path: Path,
    item_id: int,
    failure: str,
    reasons: list[str],
) -> bool:
    selected = _inspect_state_directory(manifest_path.parent, "retry")
    if selected is None or selected / "manifest.json" != manifest_path.resolve(strict=True):
        raise ValueError("retry manifest must belong to the inspected pack directory")
    manifest = load_manifest(manifest_path)
    if type(item_id) is not int:
        raise ValueError("retry item id must be an integer")
    if failure not in {"generation", "quality_gate"}:
        raise ValueError("retry failure must be generation or quality_gate")
    if not isinstance(reasons, list) or not reasons or any(
        not isinstance(reason, str) or not reason for reason in reasons
    ):
        raise ValueError("retry reasons must be a non-empty list of strings")
    try:
        row_index, row = next(
            (index, row)
            for index, row in enumerate(manifest["items"])
            if row.get("id") == item_id
        )
    except StopIteration as error:
        raise ValueError(f"unknown retry item id: {item_id}") from error

    if row["retry_count"] >= 1:
        return False

    resolved_rows, artifact_errors = validate_artifact_paths(selected, manifest["items"])
    try:
        if artifact_errors:
            raise ValueError("unsafe canonical artifact")
        raw = resolved_rows[row_index].get("raw_path")
        if raw is None:
            raise ValueError("canonical raw artifact is unresolved")
        staged, _ = safe_asset_path(selected, staged_relative_path(row), "staged_path")
        raw_exists = _validate_retry_artifact(raw, "raw_path")
        staged_exists = _validate_retry_artifact(staged, "staged_path")
        _prepare_retry_quarantine_directory(selected)
        quarantine_relatives = _retry_quarantine_paths(row)
        quarantine_targets = {
            label: safe_asset_path(
                selected, quarantine_relatives[label], f"{label}_quarantine"
            )[0]
            for label, exists in (
                ("raw_path", raw_exists),
                ("staged_path", staged_exists),
            )
            if exists
        }
        for label, target in quarantine_targets.items():
            if _validate_retry_artifact(target, f"{label}_quarantine"):
                raise ValueError(f"{label} quarantine destination already exists")
    except (OSError, ValueError, RuntimeError):
        row["retry_count"] = 1
        row["status"] = "failed"
        row["error"] = _compact_error("retry_invalidation", ["unsafe_artifact"])
        _atomic_replace_manifest(manifest_path, manifest)
        return False

    reservation_token = secrets.token_hex(32)
    row["retry_count"] = 1
    row["status"] = "failed"
    row["error"] = _retry_reservation_error(
        failure,
        reasons,
        "invalidation_in_progress",
        list(quarantine_relatives[label] for label in quarantine_targets),
        reservation_token,
    )
    _atomic_replace_manifest(manifest_path, manifest)

    try:
        for label, source in (("raw_path", raw), ("staged_path", staged)):
            if label in quarantine_targets:
                _quarantine_retry_artifact(
                    source, label, quarantine_targets[label]
                )
    except (OSError, ValueError, RuntimeError):
        row["retry_count"] = 1
        row["status"] = "failed"
        row["error"] = _compact_error("retry_invalidation", ["unsafe_artifact"])
        _atomic_replace_manifest(manifest_path, manifest)
        return False

    row["status"] = "generating"
    row["error"] = _retry_reservation_error(
        failure,
        reasons,
        "authorized",
        list(quarantine_relatives[label] for label in quarantine_targets),
        reservation_token,
    )
    _atomic_replace_manifest(manifest_path, manifest)
    return True


def fail_reserved_retry(
    manifest_path: Path,
    item_id: int,
    token: str,
    failure: str,
    reasons: list[str],
) -> bool:
    """Terminalize an actual reserved retry failure only for its owning token."""
    manifest_path = Path(manifest_path)
    if manifest_path.name != "manifest.json":
        raise ValueError("retry manifest must be named manifest.json")
    if not manifest_path.parent.name.endswith(".candidate"):
        raise ValueError("reserved retry failure requires a candidate manifest")
    if type(item_id) is not int:
        raise ValueError("retry item id must be an integer")
    if not _valid_retry_token(token):
        return False
    if failure not in {"generation", "quality_gate"}:
        raise ValueError("retry failure must be generation or quality_gate")
    if not isinstance(reasons, list) or not reasons or any(
        not isinstance(reason, str) or not reason for reason in reasons
    ):
        raise ValueError("retry reasons must be a non-empty list of strings")
    with _candidate_retry_lock(manifest_path):
        selected = _inspect_state_directory(manifest_path.parent, "retry")
        if selected is None or selected / "manifest.json" != manifest_path.resolve(
            strict=True
        ):
            raise ValueError("retry manifest must belong to the inspected pack directory")
        manifest = load_manifest(manifest_path)
        try:
            row = next(row for row in manifest["items"] if row.get("id") == item_id)
        except StopIteration as error:
            raise ValueError(f"unknown retry item id: {item_id}") from error
        reservation = _retry_reservation(row)
        if (
            reservation is None
            or row.get("status") != "generating"
            or reservation["phase"] not in {"authorized", "raw_ready"}
            or not secrets.compare_digest(reservation["token"], token)
        ):
            return False
        row["status"] = "failed"
        row["error"] = _compact_error(failure, reasons)
        _atomic_replace_manifest(manifest_path, manifest)
        return True


def mark_retry_raw_ready(manifest_path: Path, item_id: int) -> bool:
    """Persist retry chroma progress, then securely remove retry-only artifacts."""
    manifest_path = Path(manifest_path)
    if manifest_path.name != "manifest.json":
        raise ValueError("retry manifest must be named manifest.json")
    if not manifest_path.parent.name.endswith(".candidate"):
        raise ValueError("retry raw-ready transition requires a candidate manifest")
    with _candidate_retry_lock(manifest_path):
        return _mark_retry_raw_ready_locked(manifest_path, item_id)


def _mark_retry_raw_ready_locked(manifest_path: Path, item_id: int) -> bool:
    selected = _inspect_state_directory(manifest_path.parent, "retry")
    if selected is None or selected / "manifest.json" != manifest_path.resolve(strict=True):
        raise ValueError("retry manifest must belong to the inspected pack directory")
    manifest = load_manifest(manifest_path)
    if type(item_id) is not int:
        raise ValueError("retry item id must be an integer")
    try:
        row_index, row = next(
            (index, row)
            for index, row in enumerate(manifest["items"])
            if row.get("id") == item_id
        )
    except StopIteration as error:
        raise ValueError(f"unknown retry item id: {item_id}") from error

    reservation = _retry_reservation(row)
    if (
        reservation is None
        or row.get("status") != "generating"
        or reservation["phase"] not in {"authorized", "raw_ready"}
    ):
        raise ValueError("retry raw-ready transition requires an active reservation")

    failure = str(reservation["failure"])
    reasons = list(reservation["reasons"])
    quarantine_paths = list(reservation["quarantine_paths"])
    reservation_token = str(reservation["token"])

    def fail_cleanup() -> bool:
        row["status"] = "failed"
        row["error"] = _retry_reservation_error(
            failure,
            reasons,
            "cleanup_failed",
            quarantine_paths,
            reservation_token,
        )
        _atomic_replace_manifest(manifest_path, manifest)
        return False

    resolved_rows, artifact_errors = validate_artifact_paths(selected, manifest["items"])
    try:
        if artifact_errors:
            raise ValueError("unsafe canonical artifact")
        raw = resolved_rows[row_index].get("raw_path")
        if raw is None or not _valid_raw_image(raw):
            raise ValueError("canonical retry raw is invalid")
        allowed_quarantines = set(_retry_quarantine_paths(row).values())
        if any(path not in allowed_quarantines for path in quarantine_paths):
            raise ValueError("retry quarantine metadata contains an unexpected path")
        resolved_quarantines = [
            safe_asset_path(selected, path, "retry_quarantine_path")[0]
            for path in quarantine_paths
        ]
        staged, _ = safe_asset_path(
            selected, staged_relative_path(row), "staged_path"
        )
        _validate_retry_artifact(staged, "staged_path")
        for path in resolved_quarantines:
            _remove_retry_artifact(path, "retry_quarantine_path")
    except (OSError, ValueError, RuntimeError):
        return fail_cleanup()

    if reservation["phase"] == "authorized":
        row["error"] = _retry_reservation_error(
            failure,
            reasons,
            "raw_ready",
            quarantine_paths,
            reservation_token,
        )
        _atomic_replace_manifest(manifest_path, manifest)

    try:
        _remove_retry_artifact(staged, "staged_path")
        _cleanup_retry_quarantine_directory(selected, manifest)
    except (OSError, ValueError, RuntimeError):
        return fail_cleanup()
    return True


def _recovery_required(detail: str, error: Exception = None) -> ValueError:
    recovery_error = ValueError(f"recovery required: {detail}")
    if error is not None:
        recovery_error.__cause__ = error
    return recovery_error


def _inspect_state_directory(path: Path, label: str) -> Path | None:
    try:
        directory_stat = path.lstat()
    except FileNotFoundError:
        return None
    except OSError as error:
        raise _recovery_required(f"{label} cannot be inspected", error)
    if stat.S_ISLNK(directory_stat.st_mode) or not stat.S_ISDIR(directory_stat.st_mode):
        raise _recovery_required(f"{label} must be a real directory")

    manifest_path = path / "manifest.json"
    try:
        manifest_stat = manifest_path.lstat()
    except FileNotFoundError as error:
        raise _recovery_required(f"{label} manifest is missing", error)
    except OSError as error:
        raise _recovery_required(f"{label} manifest cannot be inspected", error)
    if stat.S_ISLNK(manifest_stat.st_mode) or not stat.S_ISREG(manifest_stat.st_mode):
        raise _recovery_required(f"{label} manifest must be a regular non-symlink file")
    if manifest_stat.st_nlink != 1:
        raise _recovery_required(f"{label} manifest link count must equal 1")
    try:
        manifest = load_manifest(manifest_path)
    except (OSError, ValueError, TypeError, RuntimeError) as error:
        raise _recovery_required(f"{label} manifest is unreadable or malformed", error)
    errors = validate_manifest(manifest)
    if errors:
        raise _recovery_required(f"{label} manifest state is invalid: {'; '.join(errors)}")
    try:
        return path.resolve(strict=True)
    except (OSError, RuntimeError) as error:
        raise _recovery_required(f"{label} directory cannot be resolved", error)


def resolve_resume_target(root: Path, candidate: Path = None) -> Path:
    """Choose a valid candidate before root; reject every unresolved recovery state."""
    root = Path(root)
    candidate = Path(candidate) if candidate is not None else Path(str(root) + ".candidate")
    backup = Path(str(root) + ".backup")
    try:
        backup.lstat()
    except FileNotFoundError:
        pass
    except OSError as error:
        raise _recovery_required("backup cannot be inspected", error)
    else:
        raise _recovery_required(
            "backup exists; complete backup or transaction recovery and rerun the helper"
        )

    root_state = _inspect_state_directory(root, "root")
    candidate_state = _inspect_state_directory(candidate, "candidate")
    if candidate_state is not None:
        return candidate_state
    if root_state is not None:
        return root_state
    return root.resolve(strict=False)


def _valid_raw_image(path: Path) -> bool:
    try:
        if path.is_symlink() or not path.is_file():
            return False
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(path) as image:
                image.load()
                if image.size != (1024, 1024) or image.mode != "RGBA":
                    return False
                alpha = image.getchannel("A")
                alpha_minimum, alpha_maximum = alpha.getextrema()
                if alpha_maximum == 0 or alpha_minimum == 255:
                    return False
                corner_boxes = (
                    (0, 0, 16, 16),
                    (1008, 0, 1024, 16),
                    (0, 1008, 16, 1024),
                    (1008, 1008, 1024, 1024),
                )
                if any(alpha.crop(box).getextrema()[1] > 12 for box in corner_boxes):
                    return False
                histogram = alpha.histogram()
                visible = sum(histogram[13:])
                coverage = visible / (1024 * 1024)
                if not 0.01 <= coverage <= 0.90:
                    return False
                for red, green, blue, opacity in image.getdata():
                    if (
                        opacity > 12
                        and green >= 160
                        and green - red >= 50
                        and green - blue >= 50
                    ):
                        return False
                return True
    except (OSError, RuntimeError, UnidentifiedImageError, Image.DecompressionBombError, Image.DecompressionBombWarning):
        return False


def _valid_staged_image(path: Path) -> bool:
    try:
        if path.is_symlink() or not path.is_file():
            return False
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(path) as image:
                image.load()
                if image.size != (1024, 1024) or image.mode not in {"RGB", "RGBA"}:
                    return False
                if image.mode == "RGBA" and image.getchannel("A").getextrema() != (255, 255):
                    return False
                rgb = image.convert("RGB")

        key = rgb.getpixel((0, 0))
        red, green, blue = key
        if green < 140 or green - red < 20 or green - blue < 50:
            return False

        def chroma_green(pixel):
            pixel_red, pixel_green, pixel_blue = pixel
            return (
                pixel_green >= 140
                and pixel_green - pixel_red >= 20
                and pixel_green - pixel_blue >= 50
            )

        corner_boxes = (
            (0, 0, 16, 16),
            (1008, 0, 1024, 16),
            (0, 1008, 16, 1024),
            (1008, 1008, 1024, 1024),
        )
        for box in corner_boxes:
            pixels = list(rgb.crop(box).getdata())
            if sum(chroma_green(pixel) for pixel in pixels) / len(pixels) < 0.98:
                return False

        border_width = 64
        border_parts = (
            rgb.crop((0, 0, 1024, border_width)),
            rgb.crop((0, 1024 - border_width, 1024, 1024)),
            rgb.crop((0, border_width, border_width, 1024 - border_width)),
            rgb.crop((1024 - border_width, border_width, 1024, 1024 - border_width)),
        )
        border_pixels = [pixel for part in border_parts for pixel in part.getdata()]
        if sum(chroma_green(pixel) for pixel in border_pixels) / len(border_pixels) < 0.97:
            return False

        subject_pixels = sum(not chroma_green(pixel) for pixel in rgb.getdata())
        subject_coverage = subject_pixels / (1024 * 1024)
        return 0.01 <= subject_coverage <= 0.70
    except (OSError, RuntimeError, UnidentifiedImageError, Image.DecompressionBombError, Image.DecompressionBombWarning):
        return False


def _valid_processed(row: Dict[str, object], assets: Dict[str, Path]) -> bool:
    svg = assets.get("svg_path")
    png = assets.get("png_path")
    if svg is None or png is None or not svg.is_file() or not png.is_file():
        return False
    try:
        _, white, ink = decode_svg_layers(
            svg.read_text(encoding="utf-8"), row.get("representation"), "#2E429B"
        )
    except (OSError, UnicodeDecodeError, ValueError, RuntimeError):
        return False
    return not validate_rendered_png(png, str(row.get("png_path")), white, ink, "#2E429B")


def classify_item(pack_dir: Path, row: Dict[str, object]) -> str:
    """Return the state-aware operation for one interrupted row."""
    pack_dir = Path(pack_dir).resolve(strict=True)
    resolved_rows, path_errors = validate_artifact_paths(pack_dir, [row])
    if path_errors:
        raise ValueError("; ".join(path_errors))
    assets = resolved_rows[0]
    reservation_phase = _retry_reservation_phase(row)
    if reservation_phase in {"invalidation_in_progress", "cleanup_failed"}:
        return "fail"
    if _retry_terminal_failure(row):
        return "fail"
    try:
        staged, _ = safe_asset_path(pack_dir, staged_relative_path(row), "staged_path")
    except (ValueError, OSError, RuntimeError):
        staged = None
    staged_is_valid = staged is not None and _valid_staged_image(staged)
    raw = assets.get("raw_path")
    raw_is_valid = raw is not None and _valid_raw_image(raw)
    if reservation_phase == "authorized":
        return "chroma" if _retry_reservation_active(row) and staged_is_valid else "fail"
    if reservation_phase == "raw_ready":
        return "gate" if row.get("status") == "generating" and raw_is_valid else "fail"
    if _valid_processed(row, assets):
        return "skip" if row.get("status") == "complete" else "finalize"
    if raw_is_valid:
        return "process" if row.get("status") in {"generated", "processed", "complete"} else "gate"
    if staged_is_valid:
        return "chroma"
    if row.get("retry_count", 0) >= 1:
        return "fail"
    return "generate"


def resume_plan(pack_dir: Path, allow_new: bool = False) -> Dict[str, object]:
    selected = resolve_resume_target(pack_dir)
    manifest_path = selected / "manifest.json"
    if not manifest_path.is_file() or manifest_path.is_symlink():
        if allow_new:
            return {"pack_dir": str(selected), "state": "fresh", "items": []}
        raise FileNotFoundError(f"no resumable manifest at {manifest_path}")
    manifest = load_manifest(manifest_path)
    errors = validate_manifest(manifest)
    if errors:
        raise ValueError("; ".join(errors))
    _, artifact_errors = validate_artifact_paths(selected, manifest["items"])
    if artifact_errors:
        raise ValueError("; ".join(artifact_errors))
    return {
        "pack_dir": str(selected),
        "state": "resume",
        "items": [
            {
                "id": row["id"],
                "decision": (decision := classify_item(selected, row)),
                "transition": decision_transition(decision),
            }
            for row in manifest["items"]
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan deterministic sticker-pack resume work")
    parser.add_argument("pack_dir", type=Path)
    parser.add_argument(
        "--allow-new",
        action="store_true",
        help="return a structured fresh state when no resumable manifest exists",
    )
    args = parser.parse_args()
    try:
        print(json.dumps(resume_plan(args.pack_dir, allow_new=args.allow_new), ensure_ascii=False))
    except (OSError, ValueError, TypeError, RuntimeError) as error:
        print(str(error))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
