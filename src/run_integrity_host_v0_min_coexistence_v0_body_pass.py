"""Run one bounded whole-body pass for the v0-min coexistence line.

This module reads an already-closed continuity-memory seam result and the
upstream organ artifacts named by that seam. It verifies that the selected
current-state, touch, transfer, receipt, participation, action-permission, and
seam line still stands coherently as one bounded body, then emits one additive
body-pass result.

It does not replay the host, merge preserved runs, recompute authority, mutate
prior artifacts, create mutable memory, replace source, or claim final
whole-system completion.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

import resolve_integrity_host_v0_min_coexistence_current_state_application as application_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_answer_surface as answer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_delivery as delivery_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_export as export_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_handoff as handoff_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_query as query_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_readout as readout_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open as open_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now as stand_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_memory_seam as seam_resolver


class V0BodyPassError(RuntimeError):
    """Raised for malformed body-pass tips, lineage, or effective references."""


CURRENT_STATE_READOUT_ROOT = readout_resolver.CURRENT_STATE_READOUT_ROOT
CURRENT_STATE_HANDOFF_ROOT = handoff_resolver.CURRENT_STATE_HANDOFF_ROOT
CURRENT_STATE_EXPORT_ROOT = export_resolver.CURRENT_STATE_EXPORT_ROOT
CURRENT_STATE_DELIVERY_ROOT = delivery_resolver.CURRENT_STATE_DELIVERY_ROOT
CURRENT_STATE_APPLICATION_ROOT = application_resolver.CURRENT_STATE_APPLICATION_ROOT
CURRENT_STATE_ANSWER_SURFACE_ROOT = answer_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
CURRENT_STATE_QUERY_ROOT = query_resolver.CURRENT_STATE_QUERY_ROOT
CURRENT_STATE_WHAT_STANDS_NOW_ROOT = stand_resolver.CURRENT_STATE_WHAT_STANDS_NOW_ROOT
CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT = open_resolver.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
CURRENT_STATE_TOUCH_PERMISSION_ROOT = seam_resolver.CURRENT_STATE_TOUCH_PERMISSION_ROOT
CONTINUITY_TRANSFER_UNIT_ROOT = seam_resolver.CONTINUITY_TRANSFER_UNIT_ROOT
CONTINUITY_TRANSFER_RECEIPT_ROOT = seam_resolver.CONTINUITY_TRANSFER_RECEIPT_ROOT
RECEIVED_DERIVATIVE_PARTICIPATION_ROOT = seam_resolver.RECEIVED_DERIVATIVE_PARTICIPATION_ROOT
RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT = seam_resolver.RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT
CONTINUITY_MEMORY_SEAM_ROOT = seam_resolver.CONTINUITY_MEMORY_SEAM_ROOT
V0_BODY_PASS_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_v0_body_pass")

CANONICAL_CORE_EXECUTION_FILE = seam_resolver.CANONICAL_CORE_EXECUTION_FILE
PATH_INPUT_KEYS = seam_resolver.PATH_INPUT_KEYS
EFFECTIVE_INPUT_KEYS = seam_resolver.EFFECTIVE_INPUT_KEYS
REQUIRED_FALSE_NON_CLAIMS = seam_resolver.REQUIRED_FALSE_NON_CLAIMS

RUNNER_MODULE = "run_integrity_host_v0_min_coexistence_v0_body_pass"
V0_BODY_PASS_RESULT_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_V0_BODY_PASS_RESULT"
V0_BODY_PASS_RESULT_VERSION = "0.1.0"
OUTCOME_V0_BODY_PASS_CONFIRMED = "V0_BODY_PASS_CONFIRMED"
OUTCOME_BLOCKED = "BLOCKED"

ACTION = seam_resolver.action_resolver
PARTICIPATION = ACTION.participation_resolver
RECEIPT = PARTICIPATION.receipt_resolver
TRANSFER = RECEIPT.transfer_resolver
TOUCH = TRANSFER.touch_resolver

SUPPORTED_CURRENT_STATE_OUTCOMES = frozenset(
    {
        readout_resolver.OUTCOME_EMITTED,
        handoff_resolver.OUTCOME_HANDED_OFF,
        export_resolver.OUTCOME_EXPORTED,
        delivery_resolver.OUTCOME_DELIVERED,
        application_resolver.OUTCOME_APPLIED,
        answer_resolver.OUTCOME_ANSWERED,
        query_resolver.OUTCOME_ANSWERED_QUERY,
        stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
        open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
    }
)

NON_CLAIM_DEFAULTS = {
    **seam_resolver.NON_CLAIM_DEFAULTS,
    "source_replaced": False,
    "overwrite_style_correction": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "standing_memory_collapsed_with_interpretation": False,
    "final_v0_body_pass_completed": False,
}

BLOCK_CODES = (
    "NO_ADMISSIBLE_SEAM_RESULT",
    "SELECTED_SEAM_RESULT_UNREADABLE",
    "SELECTED_SEAM_RESULT_MALFORMED",
    "SELECTED_SEAM_RESULT_NOT_CLOSED",
    "UPSTREAM_ORGAN_UNREADABLE",
    "UPSTREAM_ORGAN_MALFORMED",
    "UPSTREAM_ORGAN_NOT_SUCCESSFUL",
    "LINEAGE_INCOHERENCE",
    "CANONICAL_EXECUTION_LINE_MISMATCH",
    "EFFECTIVE_REFERENCE_INCOHERENCE",
    "LATEST_FILE_INFERENCE_REFUSED",
    "RECENCY_FRAUD_REFUSED",
    "OVERWRITE_STYLE_CORRECTION_REFUSED",
    "SOURCE_REPLACEMENT_REFUSED",
    "SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED",
    "STANDING_MEMORY_COLLAPSED_WITH_INTERPRETATION_REFUSED",
    "NON_CLAIM_FALSEHOOD_BREACH",
    "MULTIPLE_BODY_PASS_TIPS_CONFLICT_UNRESOLVED",
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
        raise V0BodyPassError(f"{context} is malformed JSON: {resolved}") from exc
    if not isinstance(value, dict):
        raise V0BodyPassError(f"{context} must be a JSON object: {resolved}")
    return value


def _section(artifact: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = artifact.get(key)
    if not isinstance(value, Mapping):
        raise V0BodyPassError(f"{key} must be an object")
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


def _count_checks(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    return (
        sum(1 for check in checks if check.get("passed") is True),
        sum(1 for check in checks if check.get("passed") is not True),
    )


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    return next((check for check in checks if check.get("passed") is not True), None)


def _safe_filename_part(value: Any) -> str:
    if not isinstance(value, str) or not value:
        value = "continuity_memory_seam_result"
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    return compact[:160] or "continuity_memory_seam_result"


def _discover_artifacts(root: Path | str, context: str) -> list[Path]:
    resolved = _repo_path(root)
    if not resolved.exists():
        return []
    if not resolved.is_dir():
        raise V0BodyPassError(f"{context} root is not a directory: {resolved}")
    try:
        return sorted(path for path in resolved.glob("*.json") if path.is_file())
    except OSError as exc:
        raise V0BodyPassError(f"{context} root is unreadable: {resolved}") from exc


def _metadata_value(artifact: Mapping[str, Any], metadata_key: str, field_key: str) -> str | None:
    metadata = artifact.get(metadata_key)
    if not isinstance(metadata, Mapping):
        return None
    value = metadata.get(field_key)
    return value if isinstance(value, str) and value else None


def _source_surface_identity(artifact: Mapping[str, Any]) -> tuple[str | None, str | None, str | None]:
    preferred = (
        ("readout_metadata", "readout_result_id", "readout"),
        ("handoff_metadata", "handoff_result_id", "handoff"),
        ("export_metadata", "export_result_id", "export"),
        ("delivery_metadata", "delivery_result_id", "delivery"),
        ("application_metadata", "application_result_id", "application"),
        ("answer_read_metadata", "answer_read_result_id", "answer_read"),
        ("query_metadata", "query_result_id", "query"),
        ("what_stands_now_metadata", "what_stands_now_result_id", "what_stands_now"),
        ("what_remains_open_metadata", "what_remains_open_result_id", "what_remains_open"),
    )
    outcome = artifact.get("outcome") if isinstance(artifact.get("outcome"), str) else None
    for metadata_key, id_key, family in preferred:
        metadata = artifact.get(metadata_key)
        if isinstance(metadata, Mapping) and isinstance(metadata.get(id_key), str):
            return metadata[id_key], family, outcome
    return None, None, outcome


def _path_value(identity: Mapping[str, Any], key: str) -> str | None:
    value = identity.get(key)
    if not isinstance(value, str) or not value.strip() or value == "provided_mapping":
        return None
    return value


def _find_first_key(value: Any, keys: Sequence[str]) -> Any | None:
    if isinstance(value, Mapping):
        for key in keys:
            if value.get(key) is not None:
                return value[key]
        for nested in value.values():
            found = _find_first_key(nested, keys)
            if found is not None:
                return found
    if isinstance(value, list):
        for nested in value:
            found = _find_first_key(nested, keys)
            if found is not None:
                return found
    return None


def _looks_like_seam_result(result: Mapping[str, Any]) -> bool:
    return any(
        key in result
        for key in (
            "continuity_memory_seam_metadata",
            "selected_action_permission_result",
            "selected_participation_result",
            "selected_receipt_result",
            "selected_transfer_result",
            "selected_source_surface",
            "closure_posture",
        )
    )


def _validate_seam_result(result: Mapping[str, Any]) -> None:
    if not _looks_like_seam_result(result):
        return
    for key in (
        "continuity_memory_seam_metadata",
        "selected_action_permission_result",
        "selected_participation_result",
        "selected_receipt_result",
        "selected_transfer_result",
        "selected_source_surface",
        "closure_posture",
        "block",
        "continuity_memory_seam_summary",
        "non_claims",
    ):
        _section(result, key)
    if not isinstance(result.get("checks"), list):
        raise V0BodyPassError("continuity-memory seam checks must be a list")
    metadata = _section(result, "continuity_memory_seam_metadata")
    for key in (
        "continuity_memory_seam_result_id",
        "continuity_memory_seam_result_type",
        "continuity_memory_seam_result_version",
    ):
        if not isinstance(metadata.get(key), str) or not metadata.get(key):
            raise V0BodyPassError(f"selected seam metadata {key} is malformed")


def _checks_all_passed(artifact: Mapping[str, Any], label: str) -> bool:
    checks = artifact.get("checks", [])
    if not isinstance(checks, list):
        raise V0BodyPassError(f"{label} checks must be a list")
    return all(isinstance(check, Mapping) and check.get("passed") is True for check in checks)


def _identity_from_seam(seam: Mapping[str, Any] | None, path: Path | str | None = None) -> dict[str, dict[str, Any]]:
    if seam is None:
        return {
            "seam": {
                "selected_seam_result_path": _display_path(path),
                "selected_seam_result_id": None,
                "selected_seam_result_type": None,
                "selected_seam_result_outcome": None,
            },
            "action": {"selected_action_permission_result_path": None, "selected_action_permission_result_id": None, "selected_action_permission_result_outcome": None},
            "participation": {"selected_participation_result_path": None, "selected_participation_result_id": None, "selected_participation_result_outcome": None},
            "receipt": {"selected_receipt_result_path": None, "selected_receipt_result_id": None, "selected_receipt_result_outcome": None},
            "transfer": {"selected_transfer_result_path": None, "selected_transfer_result_id": None, "selected_transfer_result_outcome": None},
            "touch": {"selected_touch_permission_result_path": None, "selected_touch_permission_result_id": None, "selected_touch_permission_result_outcome": None},
            "source": {"selected_source_surface_path": None, "selected_source_surface_id": None, "selected_source_surface_family": None, "selected_source_surface_outcome": None, "selected_source_surface_effective_references": {}},
        }
    metadata = _section(seam, "continuity_memory_seam_metadata")
    action = _section(seam, "selected_action_permission_result")
    participation = _section(seam, "selected_participation_result")
    receipt = _section(seam, "selected_receipt_result")
    transfer = _section(seam, "selected_transfer_result")
    source = _section(seam, "selected_source_surface")
    refs = source.get("selected_source_surface_effective_references", {})
    return {
        "seam": {
            "selected_seam_result_path": _display_path(path) if path is not None else "provided_mapping",
            "selected_seam_result_id": metadata.get("continuity_memory_seam_result_id"),
            "selected_seam_result_type": metadata.get("continuity_memory_seam_result_type"),
            "selected_seam_result_outcome": seam.get("outcome"),
        },
        "action": dict(action),
        "participation": {**dict(participation), "selected_participation_result_outcome": None},
        "receipt": {**dict(receipt), "selected_receipt_result_outcome": None},
        "transfer": {**dict(transfer), "selected_transfer_result_outcome": None},
        "touch": {"selected_touch_permission_result_path": None, "selected_touch_permission_result_id": None, "selected_touch_permission_result_outcome": None},
        "source": {
            "selected_source_surface_path": source.get("selected_source_surface_path"),
            "selected_source_surface_id": source.get("selected_source_surface_id"),
            "selected_source_surface_family": source.get("selected_source_surface_family"),
            "selected_source_surface_outcome": source.get("selected_source_surface_outcome"),
            "selected_source_surface_effective_references": dict(refs) if isinstance(refs, Mapping) else refs,
        },
    }


def _merge_non_claims(*artifacts: Mapping[str, Any] | None) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    for artifact in artifacts:
        if artifact is None:
            continue
        raw = artifact.get("non_claims", {})
        if raw is None:
            continue
        if not isinstance(raw, Mapping):
            raise V0BodyPassError("non_claims must be an object")
        for key, value in raw.items():
            if not isinstance(key, str) or not isinstance(value, bool):
                raise V0BodyPassError("non_claims must map strings to booleans")
            merged[key] = value
    return merged


def _body_tip_key(seam: Mapping[str, Any]) -> tuple[Any, ...]:
    ids = _identity_from_seam(seam)
    refs = ids["source"].get("selected_source_surface_effective_references", {})
    return (
        ids["action"].get("selected_action_permission_result_id"),
        ids["participation"].get("selected_participation_result_id"),
        ids["receipt"].get("selected_receipt_result_id"),
        ids["transfer"].get("selected_transfer_result_id"),
        ids["source"].get("selected_source_surface_id"),
        tuple(refs.get(key) for key in EFFECTIVE_INPUT_KEYS) if isinstance(refs, Mapping) else (),
    )


def _select_default_seam_result() -> tuple[Mapping[str, Any] | None, Path | None, str | None]:
    candidates: list[tuple[str, Mapping[str, Any], Path]] = []
    for path in _discover_artifacts(CONTINUITY_MEMORY_SEAM_ROOT, "continuity-memory seam"):
        seam = _read_json_file(path, "continuity-memory seam result")
        _validate_seam_result(seam)
        if seam.get("outcome") == seam_resolver.OUTCOME_SEAM_CLOSED:
            candidates.append((_display_path(path) or str(path), seam, path))
    if not candidates:
        return None, None, "NO_ADMISSIBLE_SEAM_RESULT"
    if len({_body_tip_key(item[1]) for item in candidates}) > 1:
        return None, None, "MULTIPLE_BODY_PASS_TIPS_CONFLICT_UNRESOLVED"
    _, seam, path = sorted(candidates, key=lambda item: item[0])[-1]
    return seam, path, None


def _read_required(identity: Mapping[str, Any], path_key: str, label: str) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    path = _path_value(identity, path_key)
    if path is None:
        return None, _check(f"selected_{label}_path_is_preserved", False, path_key, identity.get(path_key), "LINEAGE_INCOHERENCE")
    try:
        artifact = _read_json_file(path, f"selected {label} result")
    except (FileNotFoundError, OSError) as exc:
        return None, _check(f"selected_{label}_result_exists_and_is_readable", False, "readable upstream organ artifact", str(exc), "UPSTREAM_ORGAN_UNREADABLE")
    return artifact, _check(f"selected_{label}_result_exists_and_is_readable", True, "readable upstream organ artifact", _display_path(path))


def _successful_count(root: Path | str, expected_outcome: str, context: str) -> int:
    count = 0
    for path in _discover_artifacts(root, context):
        artifact = _read_json_file(path, context)
        if artifact.get("outcome") == expected_outcome:
            count += 1
    return count


def _touch_reference(receipt: Mapping[str, Any], transfer: Mapping[str, Any]) -> tuple[str | None, str | None]:
    for artifact in (receipt, transfer):
        reference = artifact.get("touch_permission_reference")
        if isinstance(reference, Mapping):
            path = reference.get("touch_permission_result_path")
            touch_id = reference.get("touch_permission_result_id")
            return (
                path if isinstance(path, str) and path.strip() else None,
                touch_id if isinstance(touch_id, str) and touch_id.strip() else None,
            )
    return None, None


def _read_touch(receipt: Mapping[str, Any], transfer: Mapping[str, Any]) -> tuple[dict[str, Any] | None, dict[str, Any], list[dict[str, Any]]]:
    path, touch_id = _touch_reference(receipt, transfer)
    empty = {"selected_touch_permission_result_path": path, "selected_touch_permission_result_id": touch_id, "selected_touch_permission_result_outcome": None}
    if path is None:
        return None, empty, [_check("selected_touch_permission_result_path_is_preserved", False, "touch_permission_result_path", None, "LINEAGE_INCOHERENCE")]
    try:
        touch = _read_json_file(path, "current-state touch-permission result")
    except (FileNotFoundError, OSError) as exc:
        return None, empty, [_check("selected_touch_permission_result_exists_and_is_readable", False, "readable touch-permission result", str(exc), "UPSTREAM_ORGAN_UNREADABLE")]
    metadata = _section(touch, "touch_permission_metadata")
    selected = {
        "selected_touch_permission_result_path": path,
        "selected_touch_permission_result_id": metadata.get("touch_permission_result_id", touch_id),
        "selected_touch_permission_result_outcome": touch.get("outcome"),
    }
    expected = TOUCH.OUTCOME_ADMITTED_FOR_TOUCH
    return touch, selected, [
        _check("selected_touch_permission_result_exists_and_is_readable", True, "readable touch-permission result", _display_path(path)),
        _check("selected_touch_permission_result_id_corresponds", not touch_id or metadata.get("touch_permission_result_id") == touch_id, touch_id, metadata.get("touch_permission_result_id"), "LINEAGE_INCOHERENCE" if touch_id and metadata.get("touch_permission_result_id") != touch_id else None),
        _check("selected_touch_permission_result_has_admitted_outcome", touch.get("outcome") == expected, expected, touch.get("outcome"), "UPSTREAM_ORGAN_NOT_SUCCESSFUL" if touch.get("outcome") != expected else None),
    ]


def _current_state_checks(source: Mapping[str, Any]) -> list[dict[str, Any]]:
    source_id, source_family, source_outcome = _source_surface_identity(source)
    answer_path = _find_first_key(source, ("current_state_answer_read_result_path",))
    if isinstance(answer_path, str) and answer_path.strip():
        try:
            answer = _read_json_file(answer_path, "current-state answer/read result")
            answer_ok = answer.get("outcome") == answer_resolver.OUTCOME_ANSWERED
            answer_actual: Any = {"path": _display_path(answer_path), "outcome": answer.get("outcome")}
        except (FileNotFoundError, OSError) as exc:
            answer_ok = False
            answer_actual = str(exc)
    else:
        count = _successful_count(CURRENT_STATE_ANSWER_SURFACE_ROOT, answer_resolver.OUTCOME_ANSWERED, "current-state answer/read")
        answer_ok = count > 0
        answer_actual = {"successful_artifact_count": count}
    stand_ok = source_family == "what_stands_now" and source_outcome == stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW
    stand_actual: Any = {"source_family": source_family, "source_outcome": source_outcome}
    if not stand_ok:
        count = _successful_count(CURRENT_STATE_WHAT_STANDS_NOW_ROOT, stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW, "current-state what-stands-now")
        stand_ok = count > 0
        stand_actual = {"successful_artifact_count": count}
    open_ok = source_family == "what_remains_open" and source_outcome == open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN
    open_actual: Any = {"source_family": source_family, "source_outcome": source_outcome}
    if not open_ok:
        count = _successful_count(CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT, open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN, "current-state what-remains-open")
        open_ok = count > 0
        open_actual = {"successful_artifact_count": count}
    return [
        _check("current_state_answer_read_organ_is_present_readable_and_successful", answer_ok, answer_resolver.OUTCOME_ANSWERED, answer_actual, "UPSTREAM_ORGAN_NOT_SUCCESSFUL" if not answer_ok else None),
        _check("current_state_what_stands_now_organ_is_present_readable_and_successful", stand_ok, stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW, stand_actual, "UPSTREAM_ORGAN_NOT_SUCCESSFUL" if not stand_ok else None),
        _check("current_state_what_remains_open_organ_is_present_readable_and_successful", open_ok, open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN, open_actual, "UPSTREAM_ORGAN_NOT_SUCCESSFUL" if not open_ok else None),
        _check("selected_source_surface_has_supported_current_state_outcome", isinstance(source_id, str) and source_outcome in SUPPORTED_CURRENT_STATE_OUTCOMES, "supported successful current-state source outcome", {"source_id": source_id, "source_family": source_family, "source_outcome": source_outcome}, "UPSTREAM_ORGAN_NOT_SUCCESSFUL" if source_outcome not in SUPPORTED_CURRENT_STATE_OUTCOMES else None),
    ]


def _same_path(left: Any, right: Any) -> bool:
    return isinstance(left, str) and isinstance(right, str) and _repo_path(left).resolve(strict=False) == _repo_path(right).resolve(strict=False)


def _effective_inputs(source_identity: Mapping[str, Any]) -> dict[str, Any]:
    raw = source_identity.get("selected_source_surface_effective_references")
    if not isinstance(raw, Mapping):
        raise V0BodyPassError("effective references must be an object")
    result = dict(raw)
    for key in PATH_INPUT_KEYS:
        if not isinstance(result.get(key), str) or not str(result.get(key)).strip():
            raise V0BodyPassError(f"effective reference {key} must be a non-empty string")
    for key in ("effective_source_run_path", "effective_ingress_run_path"):
        if result.get(key) is not None and not isinstance(result.get(key), str):
            raise V0BodyPassError(f"effective reference {key} must be a string when present")
    return {key: result.get(key) for key in EFFECTIVE_INPUT_KEYS}


def _effective_checks(source_identity: Mapping[str, Any]) -> list[dict[str, Any]]:
    inputs = _effective_inputs(source_identity)
    try:
        artifacts = tuple(
            _read_json_file(str(inputs[key]), label)
            for key, label in (
                ("effective_authority_artifact_path", "effective authority artifact"),
                ("effective_family_packet_path", "effective run-family packet"),
                ("effective_status_packet_path", "effective preserved-run status packet"),
                ("effective_current_governing_packet_path", "effective current-governing packet"),
            )
        )
    except (FileNotFoundError, OSError) as exc:
        return [_check("effective_references_are_readable", False, "readable authority/family/status/governing artifacts", str(exc), "EFFECTIVE_REFERENCE_INCOHERENCE")]
    try:
        summaries = ACTION._effective_summaries(*artifacts)
    except Exception as exc:  # noqa: BLE001
        raise V0BodyPassError("effective reference artifact is malformed") from exc
    canonical = {name: summary.get("core_execution_file") for name, summary in summaries.items()}
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
    canonical_ok = all(value == CANONICAL_CORE_EXECUTION_FILE for value in canonical.values())
    source_ok = len(exposed_source) < 2 or all(_same_path(exposed_source[0], value) for value in exposed_source[1:])
    ingress_ok = len(exposed_ingress) < 2 or all(_same_path(exposed_ingress[0], value) for value in exposed_ingress[1:])
    return [
        _check("effective_references_are_readable", True, "readable authority/family/status/governing artifacts", {key: inputs.get(key) for key in PATH_INPUT_KEYS}),
        _check("canonical_core_execution_file_aligned", canonical_ok, CANONICAL_CORE_EXECUTION_FILE, canonical, "CANONICAL_EXECUTION_LINE_MISMATCH" if not canonical_ok else None),
        _check("effective_references_share_current_governing_source_run_where_exposed", source_ok, "same current governing source run where exposed", source_values, "EFFECTIVE_REFERENCE_INCOHERENCE" if not source_ok else None),
        _check("effective_references_share_current_governing_ingress_run_where_exposed", ingress_ok, "same current governing ingress run where exposed", ingress_values, "EFFECTIVE_REFERENCE_INCOHERENCE" if not ingress_ok else None),
        _check("rank_currentness_references_are_explicit", all(isinstance(inputs.get(key), str) and str(inputs.get(key)).strip() for key in PATH_INPUT_KEYS), "authority/family/status/current-governing paths", {key: inputs.get(key) for key in PATH_INPUT_KEYS}, "EFFECTIVE_REFERENCE_INCOHERENCE" if not all(isinstance(inputs.get(key), str) and str(inputs.get(key)).strip() for key in PATH_INPUT_KEYS) else None),
    ]


def _lineage_checks(seam: Mapping[str, Any], artifacts: Mapping[str, Mapping[str, Any]]) -> list[dict[str, Any]]:
    ids = {
        "seam": _section(seam, "continuity_memory_seam_metadata").get("continuity_memory_seam_result_id"),
        "action": _metadata_value(artifacts["action"], "received_derivative_action_permission_metadata", "received_derivative_action_permission_result_id"),
        "participation": _metadata_value(artifacts["participation"], "received_derivative_participation_metadata", "received_derivative_participation_result_id"),
        "receipt": _metadata_value(artifacts["receipt"], "continuity_transfer_receipt_metadata", "continuity_transfer_receipt_result_id"),
        "transfer": _metadata_value(artifacts["transfer"], "continuity_transfer_metadata", "continuity_transfer_result_id"),
        "source": _source_surface_identity(artifacts["source"])[0],
    }
    selected = {
        "action": _section(seam, "selected_action_permission_result").get("selected_action_permission_result_id"),
        "participation": _section(seam, "selected_participation_result").get("selected_participation_result_id"),
        "receipt": _section(seam, "selected_receipt_result").get("selected_receipt_result_id"),
        "transfer": _section(seam, "selected_transfer_result").get("selected_transfer_result_id"),
        "source": _section(seam, "selected_source_surface").get("selected_source_surface_id"),
    }
    outcomes = {
        "action": (artifacts["action"].get("outcome"), ACTION.OUTCOME_ACTION_PERMITTED),
        "participation": (artifacts["participation"].get("outcome"), PARTICIPATION.OUTCOME_PARTICIPATED),
        "receipt": (artifacts["receipt"].get("outcome"), RECEIPT.OUTCOME_RECEIVED),
        "transfer": (artifacts["transfer"].get("outcome"), TRANSFER.OUTCOME_TRANSFERRED),
        "source": (_source_surface_identity(artifacts["source"])[2], _section(seam, "selected_source_surface").get("selected_source_surface_outcome")),
    }
    checks = [
        _check(f"selected_{name}_matches_artifact", selected[name] == ids[name] and outcomes[name][0] == outcomes[name][1], {"id": selected[name], "outcome": outcomes[name][1]}, {"id": ids[name], "outcome": outcomes[name][0]}, "LINEAGE_INCOHERENCE" if selected[name] != ids[name] else ("UPSTREAM_ORGAN_NOT_SUCCESSFUL" if outcomes[name][0] != outcomes[name][1] else None))
        for name in ("action", "participation", "receipt", "transfer", "source")
    ]
    references = (
        ("action", "selected_participation_result", "selected_participation_result_id", "participation"),
        ("action", "selected_receipt_result", "selected_receipt_result_id", "receipt"),
        ("action", "selected_transfer_result", "selected_transfer_result_id", "transfer"),
        ("action", "selected_source_surface", "selected_source_surface_id", "source"),
        ("participation", "selected_receipt_result", "selected_receipt_result_id", "receipt"),
        ("participation", "selected_transfer_result", "selected_transfer_result_id", "transfer"),
        ("participation", "selected_source_surface", "selected_source_surface_id", "source"),
        ("receipt", "selected_transfer_result", "selected_transfer_result_id", "transfer"),
        ("receipt", "selected_source_surface", "selected_source_surface_id", "source"),
        ("transfer", "selected_source_surface", "selected_source_surface_id", "source"),
    )
    mismatches = {}
    for owner, section, key, target in references:
        actual = _section(artifacts[owner], section).get(key)
        if actual != ids[target]:
            mismatches[f"{owner}.{section}.{key}"] = {"expected": ids[target], "actual": actual}
    distinct = len({str(value) for value in ids.values() if value}) == len(ids)
    checks.extend(
        [
            _check("lineage_across_source_touch_transfer_receipt_participation_action_seam_is_explicit", not mismatches, "selected ids carried forward", mismatches, "LINEAGE_INCOHERENCE" if mismatches else None),
            _check("source_transfer_receipt_participation_action_seam_distinctions_preserved", distinct, "distinct source, transfer, receipt, participation, action, seam ids", ids, "SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED" if not distinct else None),
        ]
    )
    return checks


def _payload_checks(action: Mapping[str, Any], participation: Mapping[str, Any], receipt: Mapping[str, Any]) -> list[dict[str, Any]]:
    specs = (
        (
            "action_permission",
            action.get("action_permission_payload"),
            {
                "payload_action_permission_status": "action_permitted_received_derivative",
                "source_remains_source": True,
                "receipt_remains_receipt": True,
                "transfer_remains_transfer": True,
                "participation_remains_participation": True,
                "action_permission_payload_remains_derivative": True,
            },
        ),
        (
            "participation",
            participation.get("participation_payload"),
            {
                "payload_participation_status": "participated_received_derivative",
                "source_remains_source": True,
                "receipt_remains_receipt": True,
                "transfer_remains_transfer": True,
                "participation_payload_remains_derivative": True,
            },
        ),
        (
            "receipt",
            receipt.get("received_payload"),
            {
                "payload_receipt_status": "received_carried_derivative",
                "source_remains_source": True,
                "carried_derivative_remains_derivative": True,
            },
        ),
    )
    checks = []
    for label, payload, expected in specs:
        passed = isinstance(payload, Mapping) and all(payload.get(key) == value for key, value in expected.items())
        checks.append(_check(f"{label}_payload_preserves_source_and_derivative_distinctions", passed, expected, payload, "SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED" if not passed else None))
    return checks


def _non_claim_checks(non_claims: Mapping[str, bool]) -> list[dict[str, Any]]:
    block_by_key = {
        "continuity_completed": "NON_CLAIM_FALSEHOOD_BREACH",
        "standing_upgraded": "NON_CLAIM_FALSEHOOD_BREACH",
        "replayed_into_live_host": "SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED",
        "merged_into_local_state": "SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED",
        "source_replaced": "SOURCE_REPLACEMENT_REFUSED",
        "overwrite_style_correction": "OVERWRITE_STYLE_CORRECTION_REFUSED",
        "latest_file_currentness": "LATEST_FILE_INFERENCE_REFUSED",
        "recency_fraud": "RECENCY_FRAUD_REFUSED",
        "standing_memory_collapsed_with_interpretation": "STANDING_MEMORY_COLLAPSED_WITH_INTERPRETATION_REFUSED",
    }
    keys = set(REQUIRED_FALSE_NON_CLAIMS) | set(block_by_key)
    checks = [
        _check(f"non_claim_{key}_remains_false", non_claims.get(key) is False, False, non_claims.get(key), block_by_key.get(key, "NON_CLAIM_FALSEHOOD_BREACH") if non_claims.get(key) is not False else None)
        for key in sorted(keys)
    ]
    finality_failures = {
        key: value
        for key, value in non_claims.items()
        if (key.startswith("final_") or key == "minimum_lawful_system_completed") and value is not False
    }
    checks.append(_check("broader_finality_non_claims_remain_false", not finality_failures, "all carried finality non-claims false", finality_failures, "NON_CLAIM_FALSEHOOD_BREACH" if finality_failures else None))
    return checks


def _shortcut_checks(seam: Mapping[str, Any], action: Mapping[str, Any], non_claims: Mapping[str, bool], selection_source: str) -> list[dict[str, Any]]:
    text = " ".join((selection_source, str(action.get("action_permission_request", "")), str(action.get("action_permission_summary", "")), str(seam.get("block", "")))).lower()
    table = (
        ("body_pass_does_not_use_latest_file_inference", ("latest authority", "latest family", "latest status", "latest governing", "latest file"), "LATEST_FILE_INFERENCE_REFUSED"),
        ("body_pass_does_not_claim_recency_as_currentness", ("latest wins", "timestamp wins", "newest file", "lexical latest"), "RECENCY_FRAUD_REFUSED"),
        ("body_pass_does_not_use_overwrite_style_correction", ("overwrite", "rewrite", "delete prior", "edit prior"), "OVERWRITE_STYLE_CORRECTION_REFUSED"),
        ("body_pass_does_not_replace_source", ("replace source", "source replacement", "become source"), "SOURCE_REPLACEMENT_REFUSED"),
        ("body_pass_keeps_standing_memory_distinct_from_interpretation", ("decision is memory", "interpretation is memory", "answer is whole memory", "action is whole memory"), "STANDING_MEMORY_COLLAPSED_WITH_INTERPRETATION_REFUSED"),
    )
    checks = [
        _check(name, not any(phrase in text for phrase in phrases), f"no {code.lower()}", selection_source, code if any(phrase in text for phrase in phrases) else None)
        for name, phrases, code in table
    ]
    checks.extend(_non_claim_checks(non_claims))
    return checks


def _body_pass_posture(checks: Sequence[Mapping[str, Any]]) -> dict[str, bool]:
    passed = {str(check.get("check_name")): check.get("passed") is True for check in checks}
    has = lambda *names: all(passed.get(name) is True for name in names)
    organs = has(
        "selected_action_result_exists_and_is_readable",
        "selected_participation_result_exists_and_is_readable",
        "selected_receipt_result_exists_and_is_readable",
        "selected_transfer_result_exists_and_is_readable",
        "selected_touch_permission_result_exists_and_is_readable",
        "selected_source_result_exists_and_is_readable",
        "current_state_answer_read_organ_is_present_readable_and_successful",
        "current_state_what_stands_now_organ_is_present_readable_and_successful",
        "current_state_what_remains_open_organ_is_present_readable_and_successful",
    )
    lineage = has(
        "selected_action_matches_artifact",
        "selected_participation_matches_artifact",
        "selected_receipt_matches_artifact",
        "selected_transfer_matches_artifact",
        "selected_source_matches_artifact",
        "lineage_across_source_touch_transfer_receipt_participation_action_seam_is_explicit",
    )
    currentness = has(
        "effective_references_are_readable",
        "canonical_core_execution_file_aligned",
        "effective_references_share_current_governing_source_run_where_exposed",
        "effective_references_share_current_governing_ingress_run_where_exposed",
        "rank_currentness_references_are_explicit",
        "body_pass_does_not_use_latest_file_inference",
        "body_pass_does_not_claim_recency_as_currentness",
    )
    derivative = has(
        "action_permission_payload_preserves_source_and_derivative_distinctions",
        "participation_payload_preserves_source_and_derivative_distinctions",
        "receipt_payload_preserves_source_and_derivative_distinctions",
        "source_transfer_receipt_participation_action_seam_distinctions_preserved",
        "non_claim_source_replaced_remains_false",
    )
    seam_stands = has("selected_seam_result_has_closed_outcome", "selected_seam_result_closure_posture_booleans_are_true")
    return {
        "organs_present_and_successful": organs,
        "lineage_preserved": lineage,
        "currentness_without_recency_fraud": currentness,
        "derivative_carry_without_source_collapse": derivative,
        "closure_seam_stands": seam_stands,
        "v0_body_reads_as_one_bounded_body": all((organs, lineage, currentness, derivative, seam_stands)),
    }


def _summary_payload(ids: Mapping[str, Mapping[str, Any]], posture: Mapping[str, bool], checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    passed, failed = _count_checks(checks)
    return {
        "selected_seam_result_id": ids["seam"].get("selected_seam_result_id"),
        "selected_action_permission_result_id": ids["action"].get("selected_action_permission_result_id"),
        "selected_participation_result_id": ids["participation"].get("selected_participation_result_id"),
        "selected_receipt_result_id": ids["receipt"].get("selected_receipt_result_id"),
        "selected_transfer_result_id": ids["transfer"].get("selected_transfer_result_id"),
        "selected_touch_permission_result_id": ids["touch"].get("selected_touch_permission_result_id"),
        "selected_source_surface_id": ids["source"].get("selected_source_surface_id"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "body_pass_posture_summary": dict(posture),
    }


def _result_id(seam_identity: Mapping[str, Any], outcome: str) -> str:
    seam_id = seam_identity.get("selected_seam_result_id") or "no_seam_result"
    suffix = "confirmed" if outcome == OUTCOME_V0_BODY_PASS_CONFIRMED else "blocked"
    return f"{seam_id}__v0_body_pass_{suffix}"


def _empty_posture() -> dict[str, bool]:
    return {
        "organs_present_and_successful": False,
        "lineage_preserved": False,
        "currentness_without_recency_fraud": False,
        "derivative_carry_without_source_collapse": False,
        "closure_seam_stands": False,
        "v0_body_reads_as_one_bounded_body": False,
    }


def _result(
    ids: Mapping[str, Mapping[str, Any]],
    posture: Mapping[str, bool],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    return {
        "v0_body_pass_metadata": {
            "v0_body_pass_result_id": _result_id(ids["seam"], outcome),
            "v0_body_pass_result_type": V0_BODY_PASS_RESULT_TYPE,
            "v0_body_pass_result_version": V0_BODY_PASS_RESULT_VERSION,
            "generated_at": _now_iso(),
            "runner_module": RUNNER_MODULE,
        },
        "selected_seam_result": dict(ids["seam"]),
        "selected_action_permission_result": dict(ids["action"]),
        "selected_participation_result": dict(ids["participation"]),
        "selected_receipt_result": dict(ids["receipt"]),
        "selected_transfer_result": dict(ids["transfer"]),
        "selected_touch_permission_result": dict(ids["touch"]),
        "selected_source_surface": dict(ids["source"]),
        "body_pass_posture": dict(posture),
        "checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {"block_code": block_code, "block_reason": BLOCK_REASONS.get(block_code) if block_code else None},
        "v0_body_pass_summary": _summary_payload(ids, posture, checks),
        "non_claims": dict(non_claims),
    }


def _blocked_result(
    block_code: str,
    checks: Sequence[Mapping[str, Any]],
    ids: Mapping[str, Mapping[str, Any]] | None = None,
    posture: Mapping[str, bool] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    return _result(
        ids or _identity_from_seam(None),
        posture or _empty_posture(),
        checks,
        OUTCOME_BLOCKED,
        block_code,
        non_claims or dict(NON_CLAIM_DEFAULTS),
    )


def _fail_if_needed(checks: Sequence[Mapping[str, Any]], ids: Mapping[str, Mapping[str, Any]], non_claims: Mapping[str, bool]) -> dict[str, Any] | None:
    failed = _first_failed(checks)
    if failed is None:
        return None
    block_code = failed.get("block_code")
    if not isinstance(block_code, str) or block_code not in BLOCK_REASONS:
        block_code = "LINEAGE_INCOHERENCE"
    return _blocked_result(block_code, checks, ids, _body_pass_posture(checks), non_claims)


def _resolve_selected_seam(seam: Mapping[str, Any], path: Path | str | None, selection_source: str) -> dict[str, Any]:
    _validate_seam_result(seam)
    if not _looks_like_seam_result(seam):
        return _blocked_result(
            "SELECTED_SEAM_RESULT_MALFORMED",
            [_check("selected_seam_result_is_well_formed", False, "continuity-memory seam result", "unrecognized artifact", "SELECTED_SEAM_RESULT_MALFORMED")],
        )

    ids = _identity_from_seam(seam, path)
    non_claims = _merge_non_claims(seam)
    if seam.get("outcome") != seam_resolver.OUTCOME_SEAM_CLOSED:
        return _blocked_result(
            "SELECTED_SEAM_RESULT_NOT_CLOSED",
            [_check("selected_seam_result_has_closed_outcome", False, seam_resolver.OUTCOME_SEAM_CLOSED, seam.get("outcome"), "SELECTED_SEAM_RESULT_NOT_CLOSED")],
            ids,
            non_claims=non_claims,
        )

    closure = seam.get("closure_posture", {})
    closure_ok = isinstance(closure, Mapping) and all(
        closure.get(key) is True
        for key in (
            "preserved_lineage_without_overwrite",
            "correction_by_successor_not_edit",
            "currentness_without_recency_fraud",
            "derivative_carry_without_source_collapse",
            "standing_memory_distinct_from_interpretation_surfaces",
        )
    )
    checks = [
        _check("selected_seam_result_exists_and_is_readable", True, "one readable selected seam result", ids["seam"].get("selected_seam_result_path")),
        _check("selected_seam_result_has_closed_outcome", True, seam_resolver.OUTCOME_SEAM_CLOSED, seam.get("outcome")),
        _check("selected_seam_result_checks_passed", _checks_all_passed(seam, "selected seam result"), "seam checks all passed", "all passed" if _checks_all_passed(seam, "selected seam result") else "one or more failed", "LINEAGE_INCOHERENCE" if not _checks_all_passed(seam, "selected seam result") else None),
        _check("selected_seam_result_closure_posture_booleans_are_true", closure_ok, "all closure-posture booleans true", closure, "LINEAGE_INCOHERENCE" if not closure_ok else None),
        _check("body_pass_uses_selected_seam_not_latest_files_alone", selection_source != "latest_file_inference", "explicit seam or bounded successful-outcome discovery", selection_source, "LATEST_FILE_INFERENCE_REFUSED" if selection_source == "latest_file_inference" else None),
    ]
    for name, key in (
        ("action", "selected_action_permission_result_path"),
        ("participation", "selected_participation_result_path"),
        ("receipt", "selected_receipt_result_path"),
        ("transfer", "selected_transfer_result_path"),
        ("source", "selected_source_surface_path"),
    ):
        checks.append(_check(f"selected_{name}_path_is_preserved", _path_value(ids[name], key) is not None, key, ids[name].get(key), "LINEAGE_INCOHERENCE" if _path_value(ids[name], key) is None else None))
    early = _fail_if_needed(checks, ids, non_claims)
    if early is not None:
        return early

    artifacts: dict[str, Mapping[str, Any]] = {}
    for name, key in (
        ("action", "selected_action_permission_result_path"),
        ("participation", "selected_participation_result_path"),
        ("receipt", "selected_receipt_result_path"),
        ("transfer", "selected_transfer_result_path"),
        ("source", "selected_source_surface_path"),
    ):
        artifact, check = _read_required(ids[name], key, name)
        checks.append(check)
        if artifact is None:
            return _blocked_result("UPSTREAM_ORGAN_UNREADABLE", checks, ids, _body_pass_posture(checks), non_claims)
        artifacts[name] = artifact

    ids["participation"]["selected_participation_result_outcome"] = artifacts["participation"].get("outcome")
    ids["receipt"]["selected_receipt_result_outcome"] = artifacts["receipt"].get("outcome")
    ids["transfer"]["selected_transfer_result_outcome"] = artifacts["transfer"].get("outcome")
    touch, touch_identity, touch_checks = _read_touch(artifacts["receipt"], artifacts["transfer"])
    ids["touch"] = touch_identity
    checks.extend(touch_checks)
    non_claims = _merge_non_claims(seam, artifacts["action"], artifacts["participation"], artifacts["receipt"], artifacts["transfer"], artifacts["source"], touch)

    checks.extend(_lineage_checks(seam, artifacts))
    checks.extend(_current_state_checks(artifacts["source"]))
    checks.extend(_payload_checks(artifacts["action"], artifacts["participation"], artifacts["receipt"]))
    lineage_block = _fail_if_needed(checks, ids, non_claims)
    if lineage_block is not None:
        return lineage_block

    checks.extend(_effective_checks(ids["source"]))
    checks.extend(_shortcut_checks(seam, artifacts["action"], non_claims, selection_source))
    posture = _body_pass_posture(checks)
    checks.extend(
        [
            _check("body_pass_posture_organs_present_and_successful", posture["organs_present_and_successful"], True, posture, "UPSTREAM_ORGAN_NOT_SUCCESSFUL" if not posture["organs_present_and_successful"] else None),
            _check("body_pass_posture_lineage_preserved", posture["lineage_preserved"], True, posture, "LINEAGE_INCOHERENCE" if not posture["lineage_preserved"] else None),
            _check("body_pass_posture_currentness_without_recency_fraud", posture["currentness_without_recency_fraud"], True, posture, "RECENCY_FRAUD_REFUSED" if not posture["currentness_without_recency_fraud"] else None),
            _check("body_pass_posture_derivative_carry_without_source_collapse", posture["derivative_carry_without_source_collapse"], True, posture, "SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED" if not posture["derivative_carry_without_source_collapse"] else None),
            _check("body_pass_posture_v0_reads_as_one_bounded_body", posture["v0_body_reads_as_one_bounded_body"], True, posture, "LINEAGE_INCOHERENCE" if not posture["v0_body_reads_as_one_bounded_body"] else None),
        ]
    )
    posture = _body_pass_posture(checks)
    final_block = _fail_if_needed(checks, ids, non_claims)
    if final_block is not None:
        return final_block
    return _result(ids, posture, checks, OUTCOME_V0_BODY_PASS_CONFIRMED, None, non_claims)


def run_v0_body_pass(seam_result: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Run one bounded v0 whole-body composite verification pass."""

    if seam_result is not None:
        if not isinstance(seam_result, Mapping):
            raise V0BodyPassError("seam_result must be a mapping or None")
        return _resolve_selected_seam(dict(seam_result), None, "provided_mapping")
    seam, path, block_code = _select_default_seam_result()
    if block_code is not None:
        return _blocked_result(
            block_code,
            [_check("admissible_seam_result_selected", False, "one seam-closed continuity-memory seam result", block_code, block_code)],
        )
    if seam is None:
        raise V0BodyPassError("selected seam result is absent")
    return _resolve_selected_seam(seam, path, "seam_result_discovery")


def run_v0_body_pass_from_path(seam_result_path: Path | str) -> dict[str, Any]:
    """Read one seam result and run the bounded v0 whole-body pass."""

    resolved_path = _repo_path(seam_result_path)
    try:
        seam = _read_json_file(resolved_path, "selected continuity-memory seam result")
    except (FileNotFoundError, OSError):
        ids = _identity_from_seam(None, resolved_path)
        return _blocked_result(
            "SELECTED_SEAM_RESULT_UNREADABLE",
            [_check("selected_seam_result_exists_and_is_readable", False, "readable selected seam result", _display_path(resolved_path), "SELECTED_SEAM_RESULT_UNREADABLE")],
            ids,
        )
    return _resolve_selected_seam(seam, resolved_path, "explicit_seam_result_path")


def build_v0_body_pass_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return a compact inspection summary for one v0 body-pass result."""

    if not isinstance(result, Mapping):
        raise V0BodyPassError("v0 body-pass result must be a mapping")
    checks = result.get("checks", [])
    if not isinstance(checks, list):
        raise V0BodyPassError("v0 body-pass checks must be a list")
    passed, failed = _count_checks(checks)
    metadata = result.get("v0_body_pass_metadata", {})
    block = result.get("block", {})
    non_claims = result.get("non_claims", {})
    sections = {
        "seam": result.get("selected_seam_result", {}),
        "action": result.get("selected_action_permission_result", {}),
        "participation": result.get("selected_participation_result", {}),
        "receipt": result.get("selected_receipt_result", {}),
        "transfer": result.get("selected_transfer_result", {}),
        "touch": result.get("selected_touch_permission_result", {}),
        "source": result.get("selected_source_surface", {}),
    }
    return {
        "v0_body_pass_result_id": metadata.get("v0_body_pass_result_id") if isinstance(metadata, Mapping) else None,
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "selected_seam_result_id": sections["seam"].get("selected_seam_result_id") if isinstance(sections["seam"], Mapping) else None,
        "selected_action_permission_result_id": sections["action"].get("selected_action_permission_result_id") if isinstance(sections["action"], Mapping) else None,
        "selected_participation_result_id": sections["participation"].get("selected_participation_result_id") if isinstance(sections["participation"], Mapping) else None,
        "selected_receipt_result_id": sections["receipt"].get("selected_receipt_result_id") if isinstance(sections["receipt"], Mapping) else None,
        "selected_transfer_result_id": sections["transfer"].get("selected_transfer_result_id") if isinstance(sections["transfer"], Mapping) else None,
        "selected_touch_permission_result_id": sections["touch"].get("selected_touch_permission_result_id") if isinstance(sections["touch"], Mapping) else None,
        "selected_source_surface_id": sections["source"].get("selected_source_surface_id") if isinstance(sections["source"], Mapping) else None,
        "body_pass_posture": dict(result.get("body_pass_posture", {})) if isinstance(result.get("body_pass_posture"), Mapping) else None,
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
    selected = result.get("selected_seam_result", {})
    selected_id = selected.get("selected_seam_result_id") if isinstance(selected, Mapping) else None
    root = _repo_path(V0_BODY_PASS_ROOT)
    stem = _safe_filename_part(selected_id)
    candidate = root / f"{stem}__v0_body_pass_result.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = root / f"{stem}__v0_body_pass_result_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise V0BodyPassError("no bounded v0 body-pass filename available")


def write_v0_body_pass_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive v0 body-pass JSON result."""

    if not isinstance(result, Mapping):
        raise V0BodyPassError("v0 body-pass result must be a mapping")
    target = _repo_path(output_path) if output_path is not None else _default_output_path(result)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"v0 body-pass result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
