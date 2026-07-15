"""Resolve the bounded v0 continuity-memory seam for the coexistence line.

This module emits one additive closure result from one successful
received-derivative action-permission result. It reads the closure tip and the
preserved lineage it names, then verifies that continuity memory remains
preserved lineage without overwrite, currentness without latest-file recency,
and derivative carry without source collapse.

It does not replay a host, merge preserved runs, mutate prior artifacts, create
mutable storage, rewrite history, complete continuity, replace source, or turn
seam closure into final governance.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

import resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission as action_resolver


class ContinuityMemorySeamError(RuntimeError):
    """Raised for malformed closure-tip, lineage, or effective references."""


RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT = (
    action_resolver.RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT
)
CONTINUITY_MEMORY_SEAM_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_continuity_memory_seam"
)

RECEIVED_DERIVATIVE_PARTICIPATION_ROOT = (
    action_resolver.RECEIVED_DERIVATIVE_PARTICIPATION_ROOT
)
CONTINUITY_TRANSFER_RECEIPT_ROOT = action_resolver.CONTINUITY_TRANSFER_RECEIPT_ROOT
CONTINUITY_TRANSFER_UNIT_ROOT = action_resolver.CONTINUITY_TRANSFER_UNIT_ROOT
CURRENT_STATE_TOUCH_PERMISSION_ROOT = action_resolver.CURRENT_STATE_TOUCH_PERMISSION_ROOT
CURRENT_STATE_ANSWER_SURFACE_ROOT = action_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
CURRENT_STATE_QUERY_ROOT = action_resolver.CURRENT_STATE_QUERY_ROOT
CURRENT_STATE_WHAT_STANDS_NOW_ROOT = action_resolver.CURRENT_STATE_WHAT_STANDS_NOW_ROOT
CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT = (
    action_resolver.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
)

CANONICAL_CORE_EXECUTION_FILE = action_resolver.CANONICAL_CORE_EXECUTION_FILE
PATH_INPUT_KEYS = action_resolver.PATH_INPUT_KEYS
EFFECTIVE_INPUT_KEYS = action_resolver.EFFECTIVE_INPUT_KEYS
REQUIRED_FALSE_NON_CLAIMS = action_resolver.REQUIRED_FALSE_NON_CLAIMS

RESOLVER_MODULE = (
    "resolve_integrity_host_v0_min_coexistence_continuity_memory_seam"
)
CONTINUITY_MEMORY_SEAM_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CONTINUITY_MEMORY_SEAM_RESULT"
)
CONTINUITY_MEMORY_SEAM_RESULT_VERSION = "0.1.0"

OUTCOME_SEAM_CLOSED = "SEAM_CLOSED"
OUTCOME_BLOCKED = "BLOCKED"

NON_CLAIM_DEFAULTS = {
    **action_resolver.NON_CLAIM_DEFAULTS,
    "source_replaced": False,
    "overwrite_style_correction": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "standing_memory_collapsed_with_interpretation": False,
    "final_continuity_memory_seam_completed": False,
}

BLOCK_CODES = (
    "NO_ADMISSIBLE_ACTION_PERMISSION_RESULT",
    "SELECTED_ACTION_PERMISSION_RESULT_UNREADABLE",
    "SELECTED_ACTION_PERMISSION_RESULT_MALFORMED",
    "SELECTED_ACTION_PERMISSION_RESULT_BLOCKED",
    "SELECTED_ACTION_PERMISSION_RESULT_OUT_OF_SCOPE",
    "SELECTED_ACTION_PERMISSION_RESULT_NOT_PERMITTED",
    "ACTION_PERMISSION_PAYLOAD_UNREADABLE",
    "ACTION_PERMISSION_PAYLOAD_MALFORMED",
    "LINEAGE_REFERENCE_MISSING",
    "LINEAGE_REFERENCE_INCOHERENT",
    "CANONICAL_EXECUTION_LINE_MISMATCH",
    "EFFECTIVE_REFERENCE_INCOHERENCE",
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
    "LATEST_FILE_INFERENCE_REFUSED",
    "RECENCY_FRAUD_REFUSED",
    "OVERWRITE_STYLE_CORRECTION_REFUSED",
    "SOURCE_REPLACEMENT_REFUSED",
    "SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED",
    "STANDING_MEMORY_COLLAPSED_WITH_INTERPRETATION_REFUSED",
    "SUCCESSOR_RELATION_NOT_EXPLICIT",
    "RANK_CURRENTNESS_NOT_EXPLICIT",
    "REPLAY_SHORTCUT_REFUSED",
    "MERGE_SHORTCUT_REFUSED",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
    "SILENT_STANDING_UPGRADE_REFUSED",
    "IMPLICIT_AUTHORITY_CLAIM_REFUSED",
    "MULTIPLE_CLOSURE_TIPS_CONFLICT_UNRESOLVED",
)
BLOCK_REASONS = {code: code.replace("_", " ").lower() + "." for code in BLOCK_CODES}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else _repo_root() / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    if path == "provided_mapping":
        return "provided_mapping"
    resolved = _repo_path(path)
    try:
        return str(resolved.relative_to(_repo_root()))
    except ValueError:
        return str(resolved)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _read_json_file(path: Path | str, context: str) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"{context} not found: {resolved}") from exc
    except OSError as exc:
        raise OSError(f"{context} is unreadable: {resolved}") from exc
    except json.JSONDecodeError as exc:
        raise ContinuityMemorySeamError(f"{context} is malformed JSON: {resolved}") from exc
    if not isinstance(value, dict):
        raise ContinuityMemorySeamError(f"{context} must be a JSON object: {resolved}")
    return value


def _section(artifact: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = artifact.get(key)
    if not isinstance(value, Mapping):
        raise ContinuityMemorySeamError(f"{key} must be an object")
    return value


def _check(
    name: str,
    passed: bool,
    expected: Any | None = None,
    actual: Any | None = None,
    block_code: str | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {"check_name": name, "passed": bool(passed)}
    if expected is not None:
        result["expected_posture"] = expected
    if actual is not None:
        result["actual_posture"] = actual
    if block_code is not None:
        result["block_code"] = block_code
    return result


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _count_checks(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    return (
        sum(1 for check in checks if check.get("passed") is True),
        sum(1 for check in checks if check.get("passed") is not True),
    )


def _safe_filename_part(value: Any) -> str:
    if not isinstance(value, str) or not value:
        value = "received_derivative_action_permission_result"
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    return compact[:160] or "received_derivative_action_permission_result"


def _looks_like_action_permission_result(result: Mapping[str, Any]) -> bool:
    return any(
        key in result
        for key in (
            "received_derivative_action_permission_metadata",
            "selected_participation_result",
            "selected_receipt_result",
            "selected_transfer_result",
            "selected_source_surface",
            "action_permission_payload",
        )
    )


def _validate_action_permission_result(result: Mapping[str, Any]) -> None:
    if not _looks_like_action_permission_result(result):
        return
    for key in (
        "received_derivative_action_permission_metadata",
        "selected_participation_result",
        "selected_receipt_result",
        "selected_transfer_result",
        "selected_source_surface",
        "action_permission_request",
        "checks",
        "block",
        "non_claims",
    ):
        if key == "checks":
            if not isinstance(result.get(key), list):
                raise ContinuityMemorySeamError("action-permission checks must be a list")
        else:
            _section(result, key)
    metadata = _section(result, "received_derivative_action_permission_metadata")
    for key in (
        "received_derivative_action_permission_result_id",
        "received_derivative_action_permission_result_type",
        "received_derivative_action_permission_result_version",
    ):
        if not isinstance(metadata.get(key), str) or not metadata.get(key):
            raise ContinuityMemorySeamError(
                f"selected action-permission metadata {key} is malformed"
            )


def _checks_all_passed(artifact: Mapping[str, Any], label: str) -> bool:
    checks = artifact.get("checks", [])
    if not isinstance(checks, list):
        raise ContinuityMemorySeamError(f"{label} checks must be a list")
    return all(
        isinstance(check, Mapping) and check.get("passed") is True for check in checks
    )


def _lineage_identity(
    artifact: Mapping[str, Any],
    section_key: str,
    keys: Sequence[str],
) -> dict[str, Any]:
    section = _section(artifact, section_key)
    return {key: section.get(key) for key in keys}


def _selected_action_permission_identity(
    action_permission: Mapping[str, Any] | None,
    path: Path | str | None,
) -> dict[str, Any]:
    if action_permission is None:
        return {
            "selected_action_permission_result_path": _display_path(path),
            "selected_action_permission_result_id": None,
            "selected_action_permission_result_type": None,
            "selected_action_permission_result_outcome": None,
            "actor_class": None,
            "action_class": None,
            "action_basis": None,
        }
    metadata = _section(
        action_permission,
        "received_derivative_action_permission_metadata",
    )
    request = _section(action_permission, "action_permission_request")
    return {
        "selected_action_permission_result_path": _display_path(path)
        if path is not None
        else "provided_mapping",
        "selected_action_permission_result_id": metadata.get(
            "received_derivative_action_permission_result_id"
        ),
        "selected_action_permission_result_type": metadata.get(
            "received_derivative_action_permission_result_type"
        ),
        "selected_action_permission_result_outcome": action_permission.get("outcome"),
        "actor_class": request.get("actor_class"),
        "action_class": request.get("action_class"),
        "action_basis": request.get("action_basis"),
    }


def _participation_identity(action_permission: Mapping[str, Any] | None) -> dict[str, Any]:
    if action_permission is None:
        return {
            "selected_participation_result_path": None,
            "selected_participation_result_id": None,
            "participant_class": None,
            "use_class": None,
            "participation_basis": None,
        }
    return _lineage_identity(
        action_permission,
        "selected_participation_result",
        (
            "selected_participation_result_path",
            "selected_participation_result_id",
            "participant_class",
            "use_class",
            "participation_basis",
        ),
    )


def _receipt_identity(action_permission: Mapping[str, Any] | None) -> dict[str, Any]:
    if action_permission is None:
        return {
            "selected_receipt_result_path": None,
            "selected_receipt_result_id": None,
            "receipt_class": None,
            "receipt_basis": None,
        }
    return _lineage_identity(
        action_permission,
        "selected_receipt_result",
        (
            "selected_receipt_result_path",
            "selected_receipt_result_id",
            "receipt_class",
            "receipt_basis",
        ),
    )


def _transfer_identity(action_permission: Mapping[str, Any] | None) -> dict[str, Any]:
    if action_permission is None:
        return {
            "selected_transfer_result_path": None,
            "selected_transfer_result_id": None,
            "transfer_class": None,
            "transfer_basis": None,
        }
    return _lineage_identity(
        action_permission,
        "selected_transfer_result",
        (
            "selected_transfer_result_path",
            "selected_transfer_result_id",
            "transfer_class",
            "transfer_basis",
        ),
    )


def _source_identity(action_permission: Mapping[str, Any] | None) -> dict[str, Any]:
    if action_permission is None:
        return {
            "selected_source_surface_path": None,
            "selected_source_surface_id": None,
            "selected_source_surface_family": None,
            "selected_source_surface_outcome": None,
            "selected_source_surface_effective_references": {},
        }
    selected = _section(action_permission, "selected_source_surface")
    references = selected.get("selected_source_surface_effective_references", {})
    return {
        "selected_source_surface_path": selected.get("selected_source_surface_path"),
        "selected_source_surface_id": selected.get("selected_source_surface_id"),
        "selected_source_surface_family": selected.get(
            "selected_source_surface_family"
        ),
        "selected_source_surface_outcome": selected.get(
            "selected_source_surface_outcome"
        ),
        "selected_source_surface_effective_references": dict(references)
        if isinstance(references, Mapping)
        else references,
    }


def _merge_non_claims(action_permission: Mapping[str, Any] | None) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    raw = {} if action_permission is None else action_permission.get("non_claims", {})
    if raw is None:
        return merged
    if not isinstance(raw, Mapping):
        raise ContinuityMemorySeamError("non_claims must be an object")
    for key, value in raw.items():
        if not isinstance(key, str) or not isinstance(value, bool):
            raise ContinuityMemorySeamError("non_claims must map strings to booleans")
        merged[key] = value
    return merged


def _discover_artifacts(root: Path | str, context: str) -> list[Path]:
    resolved = _repo_path(root)
    if not resolved.exists():
        return []
    if not resolved.is_dir():
        raise ContinuityMemorySeamError(f"{context} root is not a directory: {resolved}")
    try:
        return sorted(path for path in resolved.glob("*.json") if path.is_file())
    except OSError as exc:
        raise ContinuityMemorySeamError(
            f"{context} root is unreadable: {resolved}"
        ) from exc


def _closure_tip_key(action_permission: Mapping[str, Any]) -> tuple[Any, ...]:
    metadata = action_permission.get("received_derivative_action_permission_metadata", {})
    request = action_permission.get("action_permission_request", {})
    participation = action_permission.get("selected_participation_result", {})
    receipt = action_permission.get("selected_receipt_result", {})
    transfer = action_permission.get("selected_transfer_result", {})
    source = action_permission.get("selected_source_surface", {})
    payload = action_permission.get("action_permission_payload", {})
    fields = payload.get("permitted_action_fields", {}) if isinstance(payload, Mapping) else {}
    refs = (
        source.get("selected_source_surface_effective_references", {})
        if isinstance(source, Mapping)
        else {}
    )
    return (
        metadata.get("received_derivative_action_permission_result_type")
        if isinstance(metadata, Mapping)
        else None,
        participation.get("selected_participation_result_id")
        if isinstance(participation, Mapping)
        else None,
        receipt.get("selected_receipt_result_id") if isinstance(receipt, Mapping) else None,
        transfer.get("selected_transfer_result_id")
        if isinstance(transfer, Mapping)
        else None,
        source.get("selected_source_surface_id") if isinstance(source, Mapping) else None,
        request.get("actor_class") if isinstance(request, Mapping) else None,
        request.get("action_class") if isinstance(request, Mapping) else None,
        tuple(sorted(str(key) for key in fields)) if isinstance(fields, Mapping) else (),
        tuple(refs.get(key) for key in EFFECTIVE_INPUT_KEYS)
        if isinstance(refs, Mapping)
        else (),
    )


def _select_default_action_permission_result() -> tuple[
    Mapping[str, Any] | None,
    Path | None,
    str | None,
]:
    candidates: list[tuple[str, Mapping[str, Any], Path]] = []
    for path in _discover_artifacts(
        RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT,
        "received-derivative action-permission",
    ):
        action_permission = _read_json_file(
            path,
            "received-derivative action-permission result",
        )
        _validate_action_permission_result(action_permission)
        if action_permission.get("outcome") == action_resolver.OUTCOME_ACTION_PERMITTED:
            candidates.append((_display_path(path) or str(path), action_permission, path))
    if not candidates:
        return None, None, "NO_ADMISSIBLE_ACTION_PERMISSION_RESULT"
    if len({_closure_tip_key(item[1]) for item in candidates}) > 1:
        return None, None, "MULTIPLE_CLOSURE_TIPS_CONFLICT_UNRESOLVED"
    _, action_permission, path = sorted(candidates, key=lambda item: item[0])[-1]
    return action_permission, path, None


def _source_surface_artifact_identity(
    artifact: Mapping[str, Any],
) -> tuple[str | None, str | None]:
    preferred = (
        ("readout_metadata", "readout_result_id"),
        ("handoff_metadata", "handoff_result_id"),
        ("export_metadata", "export_result_id"),
        ("delivery_metadata", "delivery_result_id"),
        ("application_metadata", "application_result_id"),
        ("answer_read_metadata", "answer_read_result_id"),
        ("query_metadata", "query_result_id"),
        ("what_stands_now_metadata", "what_stands_now_result_id"),
        ("what_remains_open_metadata", "what_remains_open_result_id"),
    )
    for metadata_key, id_key in preferred:
        metadata = artifact.get(metadata_key)
        if isinstance(metadata, Mapping) and isinstance(metadata.get(id_key), str):
            return metadata[id_key], artifact.get("outcome") if isinstance(artifact.get("outcome"), str) else None
    for metadata_key, metadata in artifact.items():
        if not metadata_key.endswith("_metadata") or not isinstance(metadata, Mapping):
            continue
        for id_key, value in metadata.items():
            if id_key.endswith("_result_id") and isinstance(value, str) and value:
                return value, artifact.get("outcome") if isinstance(artifact.get("outcome"), str) else None
    return None, artifact.get("outcome") if isinstance(artifact.get("outcome"), str) else None


def _result_id_from_metadata(
    artifact: Mapping[str, Any],
    metadata_key: str,
    id_key: str,
) -> str | None:
    metadata = artifact.get(metadata_key)
    if not isinstance(metadata, Mapping):
        return None
    value = metadata.get(id_key)
    return value if isinstance(value, str) and value else None


def _path_value(identity: Mapping[str, Any], key: str) -> str | None:
    value = identity.get(key)
    if not isinstance(value, str) or not value.strip() or value == "provided_mapping":
        return None
    return value


def _lineage_checks(
    action_identity: Mapping[str, Any],
    participation_identity: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
) -> list[dict[str, Any]]:
    paths = {
        "participation": _path_value(
            participation_identity,
            "selected_participation_result_path",
        ),
        "receipt": _path_value(receipt_identity, "selected_receipt_result_path"),
        "transfer": _path_value(transfer_identity, "selected_transfer_result_path"),
        "source": _path_value(source_identity, "selected_source_surface_path"),
    }
    ids = {
        "action": action_identity.get("selected_action_permission_result_id"),
        "participation": participation_identity.get("selected_participation_result_id"),
        "receipt": receipt_identity.get("selected_receipt_result_id"),
        "transfer": transfer_identity.get("selected_transfer_result_id"),
        "source": source_identity.get("selected_source_surface_id"),
    }
    missing = [
        key
        for key, value in {**paths, **ids}.items()
        if not isinstance(value, str) or not value.strip()
    ]
    checks = [
        _check(
            "lineage_reference_identities_and_paths_are_preserved",
            not missing,
            expected="action, participation, receipt, transfer, and source lineage",
            actual=missing,
            block_code="LINEAGE_REFERENCE_MISSING" if missing else None,
        )
    ]
    if missing:
        return checks

    try:
        participation = _read_json_file(str(paths["participation"]), "participation lineage")
        receipt = _read_json_file(str(paths["receipt"]), "receipt lineage")
        transfer = _read_json_file(str(paths["transfer"]), "transfer lineage")
        source = _read_json_file(str(paths["source"]), "source-surface lineage")
    except (FileNotFoundError, OSError) as exc:
        checks.append(
            _check(
                "lineage_reference_artifacts_are_readable",
                False,
                expected="readable lineage artifacts",
                actual=str(exc),
                block_code="LINEAGE_REFERENCE_INCOHERENT",
            )
        )
        return checks

    source_id, source_outcome = _source_surface_artifact_identity(source)
    correspondences = {
        "participation": (
            _result_id_from_metadata(
                participation,
                "received_derivative_participation_metadata",
                "received_derivative_participation_result_id",
            ),
            ids["participation"],
            participation.get("outcome"),
            action_resolver.participation_resolver.OUTCOME_PARTICIPATED,
        ),
        "receipt": (
            _result_id_from_metadata(
                receipt,
                "continuity_transfer_receipt_metadata",
                "continuity_transfer_receipt_result_id",
            ),
            ids["receipt"],
            receipt.get("outcome"),
            action_resolver.participation_resolver.receipt_resolver.OUTCOME_RECEIVED,
        ),
        "transfer": (
            _result_id_from_metadata(
                transfer,
                "continuity_transfer_metadata",
                "continuity_transfer_result_id",
            ),
            ids["transfer"],
            transfer.get("outcome"),
            action_resolver.participation_resolver.receipt_resolver.transfer_resolver.OUTCOME_TRANSFERRED,
        ),
        "source": (
            source_id,
            ids["source"],
            source_outcome,
            source_identity.get("selected_source_surface_outcome"),
        ),
    }
    mismatches = {
        label: values
        for label, values in correspondences.items()
        if values[0] != values[1] or values[2] != values[3]
    }
    lineage_checks_pass = (
        _checks_all_passed(participation, "participation lineage")
        and _checks_all_passed(receipt, "receipt lineage")
        and _checks_all_passed(transfer, "transfer lineage")
        and _checks_all_passed(source, "source-surface lineage")
    )
    checks.extend(
        [
            _check(
                "lineage_reference_artifacts_are_readable",
                True,
                expected="readable lineage artifacts",
                actual=paths,
            ),
            _check(
                "lineage_reference_artifacts_correspond_to_selected_identities",
                not mismatches,
                expected="selected ids and outcomes match preserved lineage files",
                actual=mismatches,
                block_code="LINEAGE_REFERENCE_INCOHERENT" if mismatches else None,
            ),
            _check(
                "lineage_reference_artifacts_preserve_successful_checks",
                lineage_checks_pass,
                expected="all preserved lineage checks passed",
                actual="all passed" if lineage_checks_pass else "one or more failed",
                block_code="LINEAGE_REFERENCE_INCOHERENT"
                if not lineage_checks_pass
                else None,
            ),
        ]
    )
    checks.extend(_touch_lineage_checks(receipt))
    return checks


def _touch_lineage_checks(receipt: Mapping[str, Any]) -> list[dict[str, Any]]:
    reference = receipt.get("touch_permission_reference")
    if not isinstance(reference, Mapping):
        return [
            _check(
                "touch_permission_lineage_optional_or_carried",
                True,
                expected="no readable touch-permission reference required",
                actual=None,
            )
        ]
    path = reference.get("touch_permission_result_path")
    touch_id = reference.get("touch_permission_result_id")
    if path is None and touch_id is None:
        return [
            _check(
                "touch_permission_lineage_optional_or_carried",
                True,
                expected="no file-backed touch-permission lineage required",
                actual=reference,
            )
        ]
    if not isinstance(path, str) or not path.strip() or path == "provided_mapping":
        return [
            _check(
                "touch_permission_lineage_file_readable_where_applicable",
                True,
                expected="provided mapping or carried touch-permission lineage",
                actual=path,
            )
        ]
    try:
        touch = _read_json_file(path, "touch-permission lineage")
    except (FileNotFoundError, OSError) as exc:
        return [
            _check(
                "touch_permission_lineage_file_readable_where_applicable",
                False,
                expected="readable touch-permission result where path is preserved",
                actual=str(exc),
                block_code="LINEAGE_REFERENCE_INCOHERENT",
            )
        ]
    metadata = _section(touch, "touch_permission_metadata")
    admitted = (
        action_resolver.participation_resolver.receipt_resolver.transfer_resolver.touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH
    )
    id_matches = not isinstance(touch_id, str) or metadata.get(
        "touch_permission_result_id"
    ) == touch_id
    touch_checks_pass = _checks_all_passed(touch, "touch-permission lineage")
    return [
        _check(
            "touch_permission_lineage_file_readable_where_applicable",
            True,
            expected="readable touch-permission result where path is preserved",
            actual=path,
        ),
        _check(
            "touch_permission_lineage_id_corresponds",
            id_matches,
            expected=touch_id,
            actual=metadata.get("touch_permission_result_id"),
            block_code="LINEAGE_REFERENCE_INCOHERENT" if not id_matches else None,
        ),
        _check(
            "touch_permission_lineage_is_successful",
            touch.get("outcome") == admitted,
            expected=admitted,
            actual=touch.get("outcome"),
            block_code="LINEAGE_REFERENCE_INCOHERENT"
            if touch.get("outcome") != admitted
            else None,
        ),
        _check(
            "touch_permission_lineage_checks_passed",
            touch_checks_pass,
            expected="touch-permission checks all passed",
            actual="all passed" if touch_checks_pass else "one or more failed",
            block_code="LINEAGE_REFERENCE_INCOHERENT"
            if not touch_checks_pass
            else None,
        ),
    ]


def _effective_inputs(source_identity: Mapping[str, Any]) -> dict[str, Any]:
    raw = source_identity.get("selected_source_surface_effective_references")
    if not isinstance(raw, Mapping):
        raise ContinuityMemorySeamError("effective references must be an object")
    result = dict(raw)
    for key in PATH_INPUT_KEYS:
        if not isinstance(result.get(key), str) or not str(result.get(key)).strip():
            raise ContinuityMemorySeamError(
                f"effective reference {key} must be a non-empty string"
            )
    for key in ("effective_source_run_path", "effective_ingress_run_path"):
        if result.get(key) is not None and not isinstance(result.get(key), str):
            raise ContinuityMemorySeamError(
                f"effective reference {key} must be a string when present"
            )
    return {key: result.get(key) for key in EFFECTIVE_INPUT_KEYS}


def _same_path(left: Any, right: Any) -> bool:
    return isinstance(left, str) and isinstance(right, str) and (
        _repo_path(left).resolve(strict=False) == _repo_path(right).resolve(strict=False)
    )


def _effective_currentness_checks(
    inputs: Mapping[str, Any],
    summaries: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    canonical = {
        name: summary.get("core_execution_file") for name, summary in summaries.items()
    }
    source_values = [
        inputs.get("effective_source_run_path"),
        summaries["authority"].get("selected_source_run_directory_path"),
        summaries["family"].get("current_authority_source_run_path"),
        summaries["status"].get("selected_current_authority_source_run_path"),
        summaries["governing"].get("current_governing_source_run_path"),
    ]
    ingress_values = [
        inputs.get("effective_ingress_run_path"),
        summaries["authority"].get("selected_ingress_run_directory_path"),
        summaries["family"].get("current_authority_ingress_run_path"),
        summaries["governing"].get("current_governing_ingress_run_path"),
    ]
    exposed_source = [value for value in source_values if isinstance(value, str) and value]
    exposed_ingress = [value for value in ingress_values if isinstance(value, str) and value]
    canonical_ok = all(
        value == CANONICAL_CORE_EXECUTION_FILE for value in canonical.values()
    )
    source_ok = len(exposed_source) < 2 or all(
        _same_path(exposed_source[0], value) for value in exposed_source[1:]
    )
    ingress_ok = len(exposed_ingress) < 2 or all(
        _same_path(exposed_ingress[0], value) for value in exposed_ingress[1:]
    )
    return [
        _check(
            "canonical_core_execution_file_aligned",
            canonical_ok,
            expected=CANONICAL_CORE_EXECUTION_FILE,
            actual=canonical,
            block_code="CANONICAL_EXECUTION_LINE_MISMATCH"
            if not canonical_ok
            else None,
        ),
        _check(
            "effective_references_share_current_governing_source_run_where_exposed",
            source_ok,
            expected="same current governing source run where exposed",
            actual=source_values,
            block_code="EFFECTIVE_REFERENCE_INCOHERENCE" if not source_ok else None,
        ),
        _check(
            "effective_references_share_current_governing_ingress_run_where_exposed",
            ingress_ok,
            expected="same current governing ingress run where exposed",
            actual=ingress_values,
            block_code="EFFECTIVE_REFERENCE_INCOHERENCE" if not ingress_ok else None,
        ),
    ]


def _effective_checks(source_identity: Mapping[str, Any]) -> list[dict[str, Any]]:
    inputs = _effective_inputs(source_identity)
    try:
        artifacts = tuple(
            _read_json_file(str(inputs[key]), label)
            for key, label in (
                ("effective_authority_artifact_path", "effective authority artifact"),
                ("effective_family_packet_path", "effective run-family packet"),
                ("effective_status_packet_path", "effective preserved-run status packet"),
                (
                    "effective_current_governing_packet_path",
                    "effective current-governing packet",
                ),
            )
        )
    except (FileNotFoundError, OSError) as exc:
        return [
            _check(
                "effective_references_are_readable",
                False,
                expected="readable authority/family/status/governing artifacts",
                actual=str(exc),
                block_code="EFFECTIVE_REFERENCE_INCOHERENCE",
            )
        ]
    try:
        summaries = action_resolver._effective_summaries(*artifacts)
    except Exception as exc:  # noqa: BLE001
        raise ContinuityMemorySeamError(
            "effective reference artifact is malformed"
        ) from exc
    checks = [
        _check(
            "effective_references_are_readable",
            True,
            expected="readable authority/family/status/governing artifacts",
            actual={key: inputs.get(key) for key in PATH_INPUT_KEYS},
        )
    ]
    checks.extend(_effective_currentness_checks(inputs, summaries))
    checks.append(
        _check(
            "rank_currentness_is_explicit",
            all(
                isinstance(inputs.get(key), str) and str(inputs.get(key)).strip()
                for key in PATH_INPUT_KEYS
            ),
            expected="authority/family/status/current-governing references",
            actual={key: inputs.get(key) for key in PATH_INPUT_KEYS},
            block_code="RANK_CURRENTNESS_NOT_EXPLICIT"
            if not all(
                isinstance(inputs.get(key), str) and str(inputs.get(key)).strip()
                for key in PATH_INPUT_KEYS
            )
            else None,
        )
    )
    return checks


def _identity_checks(
    action_identity: Mapping[str, Any],
    participation_identity: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
) -> list[dict[str, Any]]:
    source_refs = source_identity.get("selected_source_surface_effective_references")
    checks = []
    for check_name, identity, id_key in (
        (
            "selected_action_permission_result_identity_is_preserved",
            action_identity,
            "selected_action_permission_result_id",
        ),
        (
            "selected_participation_result_identity_is_preserved",
            participation_identity,
            "selected_participation_result_id",
        ),
        (
            "selected_receipt_result_identity_is_preserved",
            receipt_identity,
            "selected_receipt_result_id",
        ),
        (
            "selected_transfer_result_identity_is_preserved",
            transfer_identity,
            "selected_transfer_result_id",
        ),
    ):
        value = identity.get(id_key)
        checks.append(
            _check(
                check_name,
                isinstance(value, str) and bool(value.strip()),
                expected=id_key,
                actual=identity,
                block_code="LINEAGE_REFERENCE_MISSING"
                if not isinstance(value, str) or not value.strip()
                else None,
            )
        )
    source_ok = (
        isinstance(source_identity.get("selected_source_surface_id"), str)
        and isinstance(source_identity.get("selected_source_surface_family"), str)
        and isinstance(source_identity.get("selected_source_surface_outcome"), str)
        and isinstance(source_refs, Mapping)
    )
    checks.append(
        _check(
            "selected_source_surface_identity_is_preserved",
            source_ok,
            expected="source id, family, outcome, and effective references",
            actual=source_identity,
            block_code="LINEAGE_REFERENCE_MISSING" if not source_ok else None,
        )
    )
    return checks


def _payload_checks(payload: Any) -> list[dict[str, Any]]:
    payload_ok = isinstance(payload, Mapping)
    checks = [
        _check(
            "action_permission_payload_is_readable",
            payload_ok,
            expected="action_permission_payload object",
            actual=payload,
            block_code="ACTION_PERMISSION_PAYLOAD_UNREADABLE" if not payload_ok else None,
        )
    ]
    if not payload_ok:
        return checks
    fields = payload.get("permitted_action_fields")
    refs = payload.get("permitted_action_references")
    checks.append(
        _check(
            "action_permission_payload_fields_and_references_are_objects",
            isinstance(fields, Mapping) and isinstance(refs, Mapping),
            expected="permitted_action_fields and permitted_action_references objects",
            actual={
                "permitted_action_fields": type(fields).__name__,
                "permitted_action_references": type(refs).__name__,
            },
            block_code="ACTION_PERMISSION_PAYLOAD_MALFORMED"
            if not isinstance(fields, Mapping) or not isinstance(refs, Mapping)
            else None,
        )
    )
    for name, key, expected in (
        (
            "action_permission_payload_preserves_derivative_status",
            "payload_action_permission_status",
            "action_permitted_received_derivative",
        ),
        ("action_permission_payload_preserves_source_remains_source", "source_remains_source", True),
        ("action_permission_payload_preserves_receipt_remains_receipt", "receipt_remains_receipt", True),
        ("action_permission_payload_preserves_transfer_remains_transfer", "transfer_remains_transfer", True),
        (
            "action_permission_payload_preserves_participation_remains_participation",
            "participation_remains_participation",
            True,
        ),
        (
            "action_permission_payload_remains_derivative",
            "action_permission_payload_remains_derivative",
            True,
        ),
    ):
        passed = payload.get(key) == expected if isinstance(expected, str) else payload.get(key) is True
        checks.append(
            _check(
                name,
                passed,
                expected=expected,
                actual=payload.get(key),
                block_code="ACTION_PERMISSION_PAYLOAD_MALFORMED"
                if key == "payload_action_permission_status" and not passed
                else (
                    "SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED"
                    if not passed
                    else None
                ),
            )
        )
    return checks


def _contains(text: str, phrases: Sequence[str]) -> bool:
    return any(phrase in text for phrase in phrases)


def _shortcut_refusal_checks(
    action_permission: Mapping[str, Any],
    non_claims: Mapping[str, bool],
    selection_source: str,
) -> list[dict[str, Any]]:
    request = action_permission.get("action_permission_request", {})
    payload = action_permission.get("action_permission_payload", {})
    text = " ".join(
        (
            selection_source,
            str(request.get("action_basis", "")) if isinstance(request, Mapping) else "",
            str(payload.get("permitted_action_fields", "")) if isinstance(payload, Mapping) else "",
        )
    ).lower()
    table = (
        ("seam_does_not_replay_into_live_host", ("replay into", "replay-based", "allow replay"), "REPLAY_SHORTCUT_REFUSED"),
        ("seam_does_not_merge_preserved_runs", ("merge into", "merge-based", "allow merge"), "MERGE_SHORTCUT_REFUSED"),
        (
            "seam_does_not_claim_continuity_completion",
            ("complete continuity", "continuity completion", "claim continuity"),
            "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        (
            "seam_does_not_use_latest_file_inference",
            ("latest authority", "latest family", "latest status", "latest governing", "latest action", "latest file"),
            "LATEST_FILE_INFERENCE_REFUSED",
        ),
        (
            "seam_does_not_claim_recency_as_currentness",
            ("latest wins", "timestamp wins", "newest file", "lexical latest"),
            "RECENCY_FRAUD_REFUSED",
        ),
        (
            "seam_does_not_use_overwrite_style_correction",
            ("overwrite", "rewrite", "delete prior", "edit prior"),
            "OVERWRITE_STYLE_CORRECTION_REFUSED",
        ),
        ("seam_does_not_replace_source", ("replace source", "source replacement", "become source"), "SOURCE_REPLACEMENT_REFUSED"),
        (
            "seam_does_not_collapse_standing_memory_into_interpretation",
            ("decision is memory", "interpretation is memory", "answer is whole memory", "action is whole memory"),
            "STANDING_MEMORY_COLLAPSED_WITH_INTERPRETATION_REFUSED",
        ),
        ("seam_does_not_request_stale_prior_family_fallback", ("stale prior", "prior-family fallback"), "STALE_PRIOR_FAMILY_FALLBACK_REFUSED"),
    )
    checks = [
        _check(
            name,
            not _contains(text, phrases),
            expected=f"no {code.lower()}",
            actual=selection_source,
            block_code=code if _contains(text, phrases) else None,
        )
        for name, phrases, code in table
    ]
    checks.extend(_non_claim_checks(non_claims))
    return checks


def _non_claim_checks(non_claims: Mapping[str, bool]) -> list[dict[str, Any]]:
    block_by_key = {
        "replayed_into_live_host": "REPLAY_SHORTCUT_REFUSED",
        "merged_into_local_state": "MERGE_SHORTCUT_REFUSED",
        "continuity_completed": "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        "standing_upgraded": "SILENT_STANDING_UPGRADE_REFUSED",
        "source_replaced": "SOURCE_REPLACEMENT_REFUSED",
        "overwrite_style_correction": "OVERWRITE_STYLE_CORRECTION_REFUSED",
        "latest_file_currentness": "LATEST_FILE_INFERENCE_REFUSED",
        "recency_fraud": "RECENCY_FRAUD_REFUSED",
        "standing_memory_collapsed_with_interpretation": "STANDING_MEMORY_COLLAPSED_WITH_INTERPRETATION_REFUSED",
    }
    keys = set(REQUIRED_FALSE_NON_CLAIMS) | set(block_by_key)
    checks = [
        _check(
            f"non_claim_{key}_remains_false",
            non_claims.get(key) is False,
            expected=False,
            actual=non_claims.get(key),
            block_code=block_by_key.get(key)
            if non_claims.get(key) is not False
            else None,
        )
        for key in sorted(keys)
    ]
    finality_failures = {
        key: value
        for key, value in non_claims.items()
        if (key.startswith("final_") or key == "minimum_lawful_system_completed")
        and value is not False
    }
    checks.append(
        _check(
            "broader_finality_non_claims_remain_false",
            not finality_failures,
            expected="all carried finality non-claims false",
            actual=finality_failures,
            block_code="IMPLICIT_AUTHORITY_CLAIM_REFUSED"
            if finality_failures
            else None,
        )
    )
    return checks


def _seam_relation_checks(
    action_identity: Mapping[str, Any],
    participation_identity: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
) -> list[dict[str, Any]]:
    ids = {
        "action": action_identity.get("selected_action_permission_result_id"),
        "participation": participation_identity.get("selected_participation_result_id"),
        "receipt": receipt_identity.get("selected_receipt_result_id"),
        "transfer": transfer_identity.get("selected_transfer_result_id"),
        "source": source_identity.get("selected_source_surface_id"),
    }
    all_ids = all(isinstance(value, str) and value.strip() for value in ids.values())
    distinct = len({str(value) for value in ids.values()}) == len(ids)
    return [
        _check(
            "successor_relation_posture_is_explicit",
            all_ids,
            expected="lineage relation across action, participation, receipt, transfer, source",
            actual=ids,
            block_code="SUCCESSOR_RELATION_NOT_EXPLICIT" if not all_ids else None,
        ),
        _check(
            "source_transfer_receipt_participation_action_distinctions_preserved",
            distinct,
            expected="distinct action, participation, receipt, transfer, source ids",
            actual=ids,
            block_code="SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED"
            if not distinct
            else None,
        ),
        _check(
            "standing_memory_is_distinct_from_interpretation_and_action_surfaces",
            ids["source"] != ids["action"],
            expected="standing source remains separate from action-permission surface",
            actual={"source": ids["source"], "action": ids["action"]},
            block_code="STANDING_MEMORY_COLLAPSED_WITH_INTERPRETATION_REFUSED"
            if ids["source"] == ids["action"]
            else None,
        ),
    ]


def _closure_posture(checks: Sequence[Mapping[str, Any]]) -> dict[str, bool]:
    passed = {str(check.get("check_name")): check.get("passed") is True for check in checks}
    return {
        "preserved_lineage_without_overwrite": all(
            passed.get(name) is True
            for name in (
                "lineage_reference_identities_and_paths_are_preserved",
                "lineage_reference_artifacts_correspond_to_selected_identities",
                "lineage_reference_artifacts_preserve_successful_checks",
                "non_claim_overwrite_style_correction_remains_false",
            )
        ),
        "correction_by_successor_not_edit": all(
            passed.get(name) is True
            for name in (
                "successor_relation_posture_is_explicit",
                "seam_does_not_use_overwrite_style_correction",
            )
        ),
        "currentness_without_recency_fraud": all(
            passed.get(name) is True
            for name in (
                "effective_references_are_readable",
                "canonical_core_execution_file_aligned",
                "effective_references_share_current_governing_source_run_where_exposed",
                "rank_currentness_is_explicit",
                "seam_does_not_use_latest_file_inference",
                "seam_does_not_claim_recency_as_currentness",
            )
        ),
        "derivative_carry_without_source_collapse": all(
            passed.get(name) is True
            for name in (
                "action_permission_payload_preserves_source_remains_source",
                "action_permission_payload_preserves_receipt_remains_receipt",
                "action_permission_payload_preserves_transfer_remains_transfer",
                "action_permission_payload_preserves_participation_remains_participation",
                "action_permission_payload_remains_derivative",
                "source_transfer_receipt_participation_action_distinctions_preserved",
            )
        ),
        "standing_memory_distinct_from_interpretation_surfaces": all(
            passed.get(name) is True
            for name in (
                "standing_memory_is_distinct_from_interpretation_and_action_surfaces",
                "non_claim_standing_memory_collapsed_with_interpretation_remains_false",
            )
        ),
    }


def _summary_payload(
    action_identity: Mapping[str, Any],
    participation_identity: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    posture: Mapping[str, bool],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    passed, failed = _count_checks(checks)
    return {
        "selected_action_permission_result_id": action_identity.get(
            "selected_action_permission_result_id"
        ),
        "selected_participation_result_id": participation_identity.get(
            "selected_participation_result_id"
        ),
        "selected_receipt_result_id": receipt_identity.get(
            "selected_receipt_result_id"
        ),
        "selected_transfer_result_id": transfer_identity.get(
            "selected_transfer_result_id"
        ),
        "selected_source_surface_id": source_identity.get(
            "selected_source_surface_id"
        ),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "closure_posture_summary": dict(posture),
    }


def _result_id(action_identity: Mapping[str, Any], outcome: str) -> str:
    action_id = (
        action_identity.get("selected_action_permission_result_id")
        or "no_action_permission_result"
    )
    suffix = "closed" if outcome == OUTCOME_SEAM_CLOSED else "blocked"
    return f"{action_id}__continuity_memory_seam_{suffix}"


def _result(
    action_identity: Mapping[str, Any],
    participation_identity: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    posture: Mapping[str, bool],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    return {
        "continuity_memory_seam_metadata": {
            "continuity_memory_seam_result_id": _result_id(action_identity, outcome),
            "continuity_memory_seam_result_type": CONTINUITY_MEMORY_SEAM_RESULT_TYPE,
            "continuity_memory_seam_result_version": CONTINUITY_MEMORY_SEAM_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_action_permission_result": dict(action_identity),
        "selected_participation_result": dict(participation_identity),
        "selected_receipt_result": dict(receipt_identity),
        "selected_transfer_result": dict(transfer_identity),
        "selected_source_surface": dict(source_identity),
        "closure_posture": dict(posture),
        "checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": BLOCK_REASONS.get(block_code) if block_code else None,
        },
        "continuity_memory_seam_summary": _summary_payload(
            action_identity,
            participation_identity,
            receipt_identity,
            transfer_identity,
            source_identity,
            posture,
            checks,
        ),
        "non_claims": dict(non_claims),
    }


def _empty_posture() -> dict[str, bool]:
    return {
        "preserved_lineage_without_overwrite": False,
        "correction_by_successor_not_edit": False,
        "currentness_without_recency_fraud": False,
        "derivative_carry_without_source_collapse": False,
        "standing_memory_distinct_from_interpretation_surfaces": False,
    }


def _blocked_result(
    block_code: str,
    checks: Sequence[Mapping[str, Any]],
    action_identity: Mapping[str, Any] | None = None,
    participation_identity: Mapping[str, Any] | None = None,
    receipt_identity: Mapping[str, Any] | None = None,
    transfer_identity: Mapping[str, Any] | None = None,
    source_identity: Mapping[str, Any] | None = None,
    posture: Mapping[str, bool] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    return _result(
        action_identity or _selected_action_permission_identity(None, None),
        participation_identity or _participation_identity(None),
        receipt_identity or _receipt_identity(None),
        transfer_identity or _transfer_identity(None),
        source_identity or _source_identity(None),
        posture or _empty_posture(),
        checks,
        OUTCOME_BLOCKED,
        block_code,
        non_claims or dict(NON_CLAIM_DEFAULTS),
    )


def _fail_if_needed(
    checks: Sequence[Mapping[str, Any]],
    action_identity: Mapping[str, Any],
    participation_identity: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any] | None:
    failed = _first_failed(checks)
    if failed is None:
        return None
    block_code = failed.get("block_code")
    if not isinstance(block_code, str) or block_code not in BLOCK_REASONS:
        block_code = "LINEAGE_REFERENCE_INCOHERENT"
    return _blocked_result(
        block_code,
        checks,
        action_identity,
        participation_identity,
        receipt_identity,
        transfer_identity,
        source_identity,
        _closure_posture(checks),
        non_claims,
    )


def _resolve_selected_action_permission(
    action_permission: Mapping[str, Any],
    path: Path | str | None,
    selection_source: str,
) -> dict[str, Any]:
    _validate_action_permission_result(action_permission)
    if not _looks_like_action_permission_result(action_permission):
        return _blocked_result(
            "SELECTED_ACTION_PERMISSION_RESULT_OUT_OF_SCOPE",
            [
                _check(
                    "selected_action_permission_result_is_in_seam_closure_scope",
                    False,
                    expected="received-derivative action-permission result",
                    actual="unrecognized artifact",
                    block_code="SELECTED_ACTION_PERMISSION_RESULT_OUT_OF_SCOPE",
                )
            ],
        )

    action_identity = _selected_action_permission_identity(action_permission, path)
    participation_identity = _participation_identity(action_permission)
    receipt_identity = _receipt_identity(action_permission)
    transfer_identity = _transfer_identity(action_permission)
    source_identity = _source_identity(action_permission)
    non_claims = _merge_non_claims(action_permission)
    outcome = action_permission.get("outcome")

    if outcome == action_resolver.OUTCOME_REFUSED or outcome == "BLOCKED":
        return _blocked_result(
            "SELECTED_ACTION_PERMISSION_RESULT_BLOCKED",
            [
                _check(
                    "selected_action_permission_result_has_permitted_outcome",
                    False,
                    expected=action_resolver.OUTCOME_ACTION_PERMITTED,
                    actual=outcome,
                    block_code="SELECTED_ACTION_PERMISSION_RESULT_BLOCKED",
                )
            ],
            action_identity,
            participation_identity,
            receipt_identity,
            transfer_identity,
            source_identity,
            non_claims=non_claims,
        )
    if outcome != action_resolver.OUTCOME_ACTION_PERMITTED:
        return _blocked_result(
            "SELECTED_ACTION_PERMISSION_RESULT_NOT_PERMITTED",
            [
                _check(
                    "selected_action_permission_result_has_permitted_outcome",
                    False,
                    expected=action_resolver.OUTCOME_ACTION_PERMITTED,
                    actual=outcome,
                    block_code="SELECTED_ACTION_PERMISSION_RESULT_NOT_PERMITTED",
                )
            ],
            action_identity,
            participation_identity,
            receipt_identity,
            transfer_identity,
            source_identity,
            non_claims=non_claims,
        )

    checks: list[dict[str, Any]] = [
        _check(
            "selected_action_permission_result_exists_and_is_readable",
            True,
            expected="one readable selected action-permission result",
            actual=action_identity.get("selected_action_permission_result_path"),
        ),
        _check(
            "selected_action_permission_result_has_permitted_outcome",
            True,
            expected=action_resolver.OUTCOME_ACTION_PERMITTED,
            actual=outcome,
        ),
        _check(
            "selected_action_permission_result_is_in_seam_closure_scope",
            True,
            expected="received-derivative action-permission result",
            actual=action_identity.get("selected_action_permission_result_type"),
        ),
        _check(
            "selected_action_permission_result_checks_passed",
            _checks_all_passed(action_permission, "selected action-permission result"),
            expected="action-permission checks all passed",
            actual="all passed"
            if _checks_all_passed(action_permission, "selected action-permission result")
            else "one or more failed",
            block_code="LINEAGE_REFERENCE_INCOHERENT"
            if not _checks_all_passed(
                action_permission,
                "selected action-permission result",
            )
            else None,
        ),
        _check(
            "seam_uses_selected_action_permission_result_not_latest_files_alone",
            selection_source != "latest_file_inference",
            expected="explicit selected action-permission result or bounded discovery",
            actual=selection_source,
            block_code="LATEST_FILE_INFERENCE_REFUSED"
            if selection_source == "latest_file_inference"
            else None,
        ),
    ]
    checks.extend(
        _identity_checks(
            action_identity,
            participation_identity,
            receipt_identity,
            transfer_identity,
            source_identity,
        )
    )
    checks.extend(_payload_checks(action_permission.get("action_permission_payload")))
    early_block = _fail_if_needed(
        checks,
        action_identity,
        participation_identity,
        receipt_identity,
        transfer_identity,
        source_identity,
        non_claims,
    )
    if early_block is not None:
        return early_block

    checks.extend(
        _lineage_checks(
            action_identity,
            participation_identity,
            receipt_identity,
            transfer_identity,
            source_identity,
        )
    )
    lineage_block = _fail_if_needed(
        checks,
        action_identity,
        participation_identity,
        receipt_identity,
        transfer_identity,
        source_identity,
        non_claims,
    )
    if lineage_block is not None:
        return lineage_block

    checks.extend(_effective_checks(source_identity))
    checks.extend(
        _seam_relation_checks(
            action_identity,
            participation_identity,
            receipt_identity,
            transfer_identity,
            source_identity,
        )
    )
    checks.extend(_shortcut_refusal_checks(action_permission, non_claims, selection_source))
    posture = _closure_posture(checks)
    checks.extend(
        [
            _check(
                "closure_posture_preserves_lineage_without_overwrite",
                posture["preserved_lineage_without_overwrite"],
                expected=True,
                actual=posture,
                block_code="OVERWRITE_STYLE_CORRECTION_REFUSED"
                if not posture["preserved_lineage_without_overwrite"]
                else None,
            ),
            _check(
                "closure_posture_preserves_currentness_without_recency_fraud",
                posture["currentness_without_recency_fraud"],
                expected=True,
                actual=posture,
                block_code="RECENCY_FRAUD_REFUSED"
                if not posture["currentness_without_recency_fraud"]
                else None,
            ),
            _check(
                "closure_posture_preserves_derivative_carry_without_source_collapse",
                posture["derivative_carry_without_source_collapse"],
                expected=True,
                actual=posture,
                block_code="SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED"
                if not posture["derivative_carry_without_source_collapse"]
                else None,
            ),
            _check(
                "closure_posture_keeps_standing_memory_distinct",
                posture["standing_memory_distinct_from_interpretation_surfaces"],
                expected=True,
                actual=posture,
                block_code="STANDING_MEMORY_COLLAPSED_WITH_INTERPRETATION_REFUSED"
                if not posture["standing_memory_distinct_from_interpretation_surfaces"]
                else None,
            ),
        ]
    )
    final_block = _fail_if_needed(
        checks,
        action_identity,
        participation_identity,
        receipt_identity,
        transfer_identity,
        source_identity,
        non_claims,
    )
    if final_block is not None:
        return final_block

    return _result(
        action_identity,
        participation_identity,
        receipt_identity,
        transfer_identity,
        source_identity,
        posture,
        checks,
        OUTCOME_SEAM_CLOSED,
        None,
        non_claims,
    )


def resolve_continuity_memory_seam(
    action_permission_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded continuity-memory seam decision."""

    if action_permission_result is not None:
        if not isinstance(action_permission_result, Mapping):
            raise ContinuityMemorySeamError(
                "action_permission_result must be a mapping or None"
            )
        return _resolve_selected_action_permission(
            dict(action_permission_result),
            None,
            "provided_mapping",
        )
    action_permission, path, block_code = _select_default_action_permission_result()
    if block_code is not None:
        return _blocked_result(
            block_code,
            [
                _check(
                    "admissible_action_permission_result_selected",
                    False,
                    expected="one action-permitted action-permission result",
                    actual=block_code,
                    block_code=block_code,
                )
            ],
        )
    if action_permission is None:
        raise ContinuityMemorySeamError("selected action-permission result is absent")
    return _resolve_selected_action_permission(
        action_permission,
        path,
        "action_permission_result_discovery",
    )


def resolve_continuity_memory_seam_from_path(
    action_permission_result_path: Path | str,
) -> dict[str, Any]:
    """Read one action-permission result and resolve the continuity-memory seam."""

    resolved_path = _repo_path(action_permission_result_path)
    try:
        action_permission = _read_json_file(
            resolved_path,
            "selected received-derivative action-permission result",
        )
    except (FileNotFoundError, OSError):
        return _blocked_result(
            "SELECTED_ACTION_PERMISSION_RESULT_UNREADABLE",
            [
                _check(
                    "selected_action_permission_result_exists_and_is_readable",
                    False,
                    expected="readable selected action-permission result",
                    actual=_display_path(resolved_path),
                    block_code="SELECTED_ACTION_PERMISSION_RESULT_UNREADABLE",
                )
            ],
            action_identity=_selected_action_permission_identity(None, resolved_path),
        )
    return _resolve_selected_action_permission(
        action_permission,
        resolved_path,
        "explicit_action_permission_result_path",
    )


def build_continuity_memory_seam_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return a compact inspection summary for one continuity-memory seam result."""

    if not isinstance(result, Mapping):
        raise ContinuityMemorySeamError("continuity-memory seam result must be a mapping")
    checks = result.get("checks", [])
    if not isinstance(checks, list):
        raise ContinuityMemorySeamError("continuity-memory seam checks must be a list")
    passed, failed = _count_checks(checks)
    metadata = result.get("continuity_memory_seam_metadata", {})
    action = result.get("selected_action_permission_result", {})
    participation = result.get("selected_participation_result", {})
    receipt = result.get("selected_receipt_result", {})
    transfer = result.get("selected_transfer_result", {})
    source = result.get("selected_source_surface", {})
    posture = result.get("closure_posture", {})
    block = result.get("block", {})
    non_claims = result.get("non_claims", {})
    return {
        "continuity_memory_seam_result_id": metadata.get(
            "continuity_memory_seam_result_id"
        )
        if isinstance(metadata, Mapping)
        else None,
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "selected_action_permission_result_id": action.get(
            "selected_action_permission_result_id"
        )
        if isinstance(action, Mapping)
        else None,
        "selected_participation_result_id": participation.get(
            "selected_participation_result_id"
        )
        if isinstance(participation, Mapping)
        else None,
        "selected_receipt_result_id": receipt.get("selected_receipt_result_id")
        if isinstance(receipt, Mapping)
        else None,
        "selected_transfer_result_id": transfer.get("selected_transfer_result_id")
        if isinstance(transfer, Mapping)
        else None,
        "selected_source_surface_id": source.get("selected_source_surface_id")
        if isinstance(source, Mapping)
        else None,
        "closure_posture": dict(posture) if isinstance(posture, Mapping) else None,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                *REQUIRED_FALSE_NON_CLAIMS,
                "source_replaced",
                "overwrite_style_correction",
                "latest_file_currentness",
                "recency_fraud",
                "standing_memory_collapsed_with_interpretation",
            )
            if isinstance(non_claims, Mapping)
        },
    }


def _default_output_path(result: Mapping[str, Any]) -> Path:
    selected = result.get("selected_action_permission_result", {})
    selected_id = (
        selected.get("selected_action_permission_result_id")
        if isinstance(selected, Mapping)
        else None
    )
    stem = _safe_filename_part(selected_id)
    root = _repo_path(CONTINUITY_MEMORY_SEAM_ROOT)
    candidate = root / f"{stem}__continuity_memory_seam_result.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = root / f"{stem}__continuity_memory_seam_result_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise ContinuityMemorySeamError("no bounded continuity-memory seam filename available")


def write_continuity_memory_seam_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive continuity-memory seam JSON result."""

    if not isinstance(result, Mapping):
        raise ContinuityMemorySeamError("continuity-memory seam result must be a mapping")
    target = _repo_path(output_path) if output_path is not None else _default_output_path(result)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"continuity-memory seam result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
