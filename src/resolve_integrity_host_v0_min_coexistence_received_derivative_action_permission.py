"""Resolve bounded received-derivative action permission for the v0-min line.

This module emits one additive post-participation action-permission result
from one successful received-derivative participation result and one bounded
action-permission request. It preserves participation, receipt, transfer,
source, and derivative distinctions while permitting only one bounded local
action over already participated material.

It does not replay source actions into a live host, merge preserved runs,
mutate prior artifacts, complete continuity, upgrade standing, replace source,
define persistence or registry law, or turn action permission into final
governance.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

import resolve_integrity_host_v0_min_coexistence_received_derivative_participation as participation_resolver


class ReceivedDerivativeActionPermissionError(RuntimeError):
    """Raised for malformed action-permission inputs or correspondence."""


RECEIVED_DERIVATIVE_PARTICIPATION_ROOT = (
    participation_resolver.RECEIVED_DERIVATIVE_PARTICIPATION_ROOT
)
RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_received_derivative_action_permissions"
)

CONTINUITY_TRANSFER_RECEIPT_ROOT = (
    participation_resolver.CONTINUITY_TRANSFER_RECEIPT_ROOT
)
CONTINUITY_TRANSFER_UNIT_ROOT = participation_resolver.CONTINUITY_TRANSFER_UNIT_ROOT
CURRENT_STATE_TOUCH_PERMISSION_ROOT = (
    participation_resolver.CURRENT_STATE_TOUCH_PERMISSION_ROOT
)
CURRENT_STATE_ANSWER_SURFACE_ROOT = (
    participation_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
)
CURRENT_STATE_QUERY_ROOT = participation_resolver.CURRENT_STATE_QUERY_ROOT
CURRENT_STATE_WHAT_STANDS_NOW_ROOT = (
    participation_resolver.CURRENT_STATE_WHAT_STANDS_NOW_ROOT
)
CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT = (
    participation_resolver.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
)

CANONICAL_CORE_EXECUTION_FILE = participation_resolver.CANONICAL_CORE_EXECUTION_FILE
PATH_INPUT_KEYS = participation_resolver.PATH_INPUT_KEYS
EFFECTIVE_INPUT_KEYS = participation_resolver.EFFECTIVE_INPUT_KEYS
REQUIRED_FALSE_NON_CLAIMS = participation_resolver.REQUIRED_FALSE_NON_CLAIMS

RESOLVER_MODULE = (
    "resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission"
)
RECEIVED_DERIVATIVE_ACTION_PERMISSION_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_RECEIVED_DERIVATIVE_ACTION_PERMISSION_RESULT"
)
RECEIVED_DERIVATIVE_ACTION_PERMISSION_RESULT_VERSION = "0.1.0"

OUTCOME_ACTION_PERMITTED = "ACTION_PERMITTED"
OUTCOME_REFUSED = "REFUSED"

ACTOR_CLASS_LOCAL_EMISSION = "LOCAL_EMISSION_ACTOR"
ACTOR_CLASS_LOCAL_INVOCATION = "LOCAL_INVOCATION_ACTOR"
SUPPORTED_ACTOR_CLASSES = frozenset(
    {ACTOR_CLASS_LOCAL_EMISSION, ACTOR_CLASS_LOCAL_INVOCATION}
)

ACTION_CLASS_DERIVATIVE_EMISSION = "DERIVATIVE_EMISSION_ACTION"
ACTION_CLASS_BOUNDED_SURFACE_INVOCATION = "BOUNDED_SURFACE_INVOCATION_ACTION"
SUPPORTED_ACTION_CLASSES = frozenset(
    {ACTION_CLASS_DERIVATIVE_EMISSION, ACTION_CLASS_BOUNDED_SURFACE_INVOCATION}
)

NON_CLAIM_DEFAULTS = {
    **participation_resolver.NON_CLAIM_DEFAULTS,
    "final_received_derivative_action_permission_completed": False,
}

BLOCK_CODES = (
    "NO_ADMISSIBLE_PARTICIPATION_RESULT",
    "SELECTED_PARTICIPATION_RESULT_UNREADABLE",
    "SELECTED_PARTICIPATION_RESULT_MALFORMED",
    "SELECTED_PARTICIPATION_RESULT_BLOCKED",
    "SELECTED_PARTICIPATION_RESULT_OUT_OF_SCOPE",
    "SELECTED_PARTICIPATION_RESULT_NOT_PARTICIPATED",
    "PARTICIPATION_PAYLOAD_UNREADABLE",
    "PARTICIPATION_PAYLOAD_MALFORMED",
    "PARTICIPATION_PAYLOAD_MISSING_DERIVATIVE_STATUS",
    "SOURCE_REMAINS_SOURCE_NOT_TRUE",
    "RECEIPT_REMAINS_RECEIPT_NOT_TRUE",
    "TRANSFER_REMAINS_TRANSFER_NOT_TRUE",
    "PARTICIPATION_PAYLOAD_REMAINS_DERIVATIVE_NOT_TRUE",
    "SELECTED_SOURCE_SURFACE_IDENTITY_MISSING",
    "SELECTED_TRANSFER_RESULT_IDENTITY_MISSING",
    "SELECTED_RECEIPT_RESULT_IDENTITY_MISSING",
    "TOUCH_PERMISSION_LINEAGE_INCOHERENT",
    "CANONICAL_EXECUTION_LINE_MISMATCH",
    "EFFECTIVE_REFERENCE_INCOHERENCE",
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
    "LATEST_FILE_INFERENCE_REFUSED",
    "REPLAY_SHORTCUT_REFUSED",
    "MERGE_SHORTCUT_REFUSED",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
    "SILENT_STANDING_UPGRADE_REFUSED",
    "IMPLICIT_MUTATION_REFUSED",
    "IMPLICIT_AUTHORITY_CLAIM_REFUSED",
    "ACTOR_CLASS_OUT_OF_SCOPE",
    "ACTION_CLASS_OUT_OF_SCOPE",
    "ACTION_PAYLOAD_OUT_OF_SCOPE",
    "SOURCE_REPLACEMENT_REFUSED",
    "SOURCE_TRANSFER_RECEIPT_DERIVATIVE_COLLAPSE_REFUSED",
    "MULTIPLE_PARTICIPATION_RESULTS_CONFLICT_UNRESOLVED",
)
BLOCK_REASONS = {
    code: code.replace("_", " ").lower() + "." for code in BLOCK_CODES
}


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
        raise ReceivedDerivativeActionPermissionError(
            f"{context} is malformed JSON: {resolved}"
        ) from exc
    if not isinstance(value, dict):
        raise ReceivedDerivativeActionPermissionError(
            f"{context} must be a JSON object: {resolved}"
        )
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
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _safe_filename_part(value: Any) -> str:
    if not isinstance(value, str) or not value:
        value = "received_derivative_action_permission_result"
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    return compact[:160] or "received_derivative_action_permission_result"


def _normal_action_permission_request(request: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(request, Mapping):
        raise ReceivedDerivativeActionPermissionError(
            "received-derivative action-permission request must be a mapping"
        )
    required = {
        "received_derivative_action_permission_request_id",
        "actor_class",
        "action_class",
        "action_basis",
        "requested_action_fields",
        "action_surface_label",
    }
    extra = set(request) - required
    missing = required - set(request)
    if extra or missing:
        raise ReceivedDerivativeActionPermissionError(
            "received-derivative action-permission request shape is malformed"
        )
    normalized: dict[str, Any] = {}
    for key in required - {"requested_action_fields"}:
        value = request[key]
        if not isinstance(value, str) or not value.strip():
            raise ReceivedDerivativeActionPermissionError(
                f"received-derivative action-permission request {key} must be non-empty"
            )
        normalized[key] = value.strip()
    fields = request["requested_action_fields"]
    if not isinstance(fields, list):
        raise ReceivedDerivativeActionPermissionError(
            "requested_action_fields must be a list"
        )
    normalized_fields: list[str] = []
    for index, value in enumerate(fields):
        if not isinstance(value, str) or not value.strip():
            raise ReceivedDerivativeActionPermissionError(
                f"requested_action_fields entry {index} must be non-empty"
            )
        normalized_fields.append(value.strip())
    normalized["requested_action_fields"] = normalized_fields
    return normalized


def read_received_derivative_action_permission_request(
    path: Path | str,
) -> dict[str, Any]:
    """Read one bounded received-derivative action-permission request."""

    return _normal_action_permission_request(
        _read_json_file(path, "received-derivative action-permission request")
    )


def _section(artifact: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = artifact.get(key)
    if not isinstance(value, Mapping):
        raise ReceivedDerivativeActionPermissionError(f"{key} must be an object")
    return value


def _looks_like_participation_result(participation: Mapping[str, Any]) -> bool:
    return any(
        key in participation
        for key in (
            "received_derivative_participation_metadata",
            "selected_receipt_result",
            "selected_transfer_result",
            "selected_source_surface",
            "participation_request",
            "participation_payload",
        )
    )


def _participation_identity(
    participation: Mapping[str, Any] | None,
    participation_path: Path | str | None,
) -> dict[str, Any]:
    if participation is None:
        return {
            "selected_participation_result_path": _display_path(participation_path),
            "selected_participation_result_id": None,
            "selected_participation_result_type": None,
            "selected_participation_result_outcome": None,
            "participant_class": None,
            "use_class": None,
            "participation_basis": None,
        }
    metadata = _section(participation, "received_derivative_participation_metadata")
    request = _section(participation, "participation_request")
    for key in (
        "received_derivative_participation_result_id",
        "received_derivative_participation_result_type",
        "received_derivative_participation_result_version",
    ):
        if not isinstance(metadata.get(key), str) or not metadata.get(key):
            raise ReceivedDerivativeActionPermissionError(
                f"selected participation result metadata {key} is malformed"
            )
    return {
        "selected_participation_result_path": _display_path(participation_path)
        if participation_path is not None
        else "provided_mapping",
        "selected_participation_result_id": metadata[
            "received_derivative_participation_result_id"
        ],
        "selected_participation_result_type": metadata[
            "received_derivative_participation_result_type"
        ],
        "selected_participation_result_outcome": participation.get("outcome"),
        "participant_class": request.get("participant_class"),
        "use_class": request.get("use_class"),
        "participation_basis": request.get("participation_basis"),
    }


def _lineage_identity(section: Mapping[str, Any], keys: Sequence[str]) -> dict[str, Any]:
    return {key: section.get(key) for key in keys}


def _receipt_identity_from_participation(
    participation: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if participation is None:
        return {
            "selected_receipt_result_path": None,
            "selected_receipt_result_id": None,
            "receipt_class": None,
            "receipt_basis": None,
        }
    return _lineage_identity(
        _section(participation, "selected_receipt_result"),
        (
            "selected_receipt_result_path",
            "selected_receipt_result_id",
            "receipt_class",
            "receipt_basis",
        ),
    )


def _transfer_identity_from_participation(
    participation: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if participation is None:
        return {
            "selected_transfer_result_path": None,
            "selected_transfer_result_id": None,
            "transfer_class": None,
            "transfer_basis": None,
        }
    return _lineage_identity(
        _section(participation, "selected_transfer_result"),
        (
            "selected_transfer_result_path",
            "selected_transfer_result_id",
            "transfer_class",
            "transfer_basis",
        ),
    )


def _source_identity_from_participation(
    participation: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if participation is None:
        return {
            "selected_source_surface_path": None,
            "selected_source_surface_id": None,
            "selected_source_surface_family": None,
            "selected_source_surface_outcome": None,
            "selected_source_surface_effective_references": {},
        }
    selected = _section(participation, "selected_source_surface")
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


def _touch_lineage_from_participation(
    participation: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if participation is None:
        return {
            "touch_permission_result_path": None,
            "touch_permission_result_id": None,
            "admitted_touch_class": None,
            "admitted_touch_scope": None,
        }
    payload = _section(participation, "participation_payload")
    references = payload.get("participated_references", {})
    if references is None:
        references = {}
    if not isinstance(references, Mapping):
        raise ReceivedDerivativeActionPermissionError(
            "participated references must be an object"
        )
    return {
        "touch_permission_result_path": references.get("touch_permission_result_path"),
        "touch_permission_result_id": references.get("touch_permission_result_id"),
        "admitted_touch_class": references.get("admitted_touch_class"),
        "admitted_touch_scope": references.get("admitted_touch_scope"),
    }


def _merge_non_claims(
    participation: Mapping[str, Any] | None,
) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    raw = {} if participation is None else participation.get("non_claims", {})
    if raw is None:
        return merged
    if not isinstance(raw, Mapping):
        raise ReceivedDerivativeActionPermissionError("non_claims must be an object")
    for key, value in raw.items():
        if not isinstance(key, str) or not isinstance(value, bool):
            raise ReceivedDerivativeActionPermissionError(
                "non_claims must map strings to booleans"
            )
        merged[key] = value
    return merged


def _discover_artifacts(root: Path | str, context: str) -> list[Path]:
    resolved = _repo_path(root)
    if not resolved.exists():
        return []
    if not resolved.is_dir():
        raise ReceivedDerivativeActionPermissionError(
            f"{context} root is not a directory: {resolved}"
        )
    try:
        return sorted(path for path in resolved.glob("*.json") if path.is_file())
    except OSError as exc:
        raise ReceivedDerivativeActionPermissionError(
            f"{context} root is unreadable: {resolved}"
        ) from exc


def _participation_effective_key(participation: Mapping[str, Any]) -> tuple[Any, ...]:
    source = participation.get("selected_source_surface", {})
    receipt = participation.get("selected_receipt_result", {})
    transfer = participation.get("selected_transfer_result", {})
    payload = participation.get("participation_payload", {})
    request = participation.get("participation_request", {})
    references = (
        source.get("selected_source_surface_effective_references", {})
        if isinstance(source, Mapping)
        else {}
    )
    fields = (
        payload.get("participated_fields", {}) if isinstance(payload, Mapping) else {}
    )
    return (
        source.get("selected_source_surface_id") if isinstance(source, Mapping) else None,
        source.get("selected_source_surface_family")
        if isinstance(source, Mapping)
        else None,
        receipt.get("selected_receipt_result_id")
        if isinstance(receipt, Mapping)
        else None,
        transfer.get("selected_transfer_result_id")
        if isinstance(transfer, Mapping)
        else None,
        request.get("participant_class") if isinstance(request, Mapping) else None,
        request.get("use_class") if isinstance(request, Mapping) else None,
        tuple(sorted(str(key) for key in fields)) if isinstance(fields, Mapping) else (),
        tuple(references.get(key) for key in EFFECTIVE_INPUT_KEYS)
        if isinstance(references, Mapping)
        else (),
    )


def _select_default_participation_result() -> tuple[
    Mapping[str, Any] | None,
    Path | None,
    str | None,
]:
    candidates: list[tuple[str, Mapping[str, Any], Path]] = []
    for path in _discover_artifacts(
        RECEIVED_DERIVATIVE_PARTICIPATION_ROOT,
        "received-derivative participation",
    ):
        participation = _read_json_file(
            path,
            "received-derivative participation result",
        )
        if participation.get("outcome") == participation_resolver.OUTCOME_PARTICIPATED:
            candidates.append((_display_path(path) or str(path), participation, path))
    if not candidates:
        return None, None, "NO_ADMISSIBLE_PARTICIPATION_RESULT"
    if len({_participation_effective_key(item[1]) for item in candidates}) > 1:
        return None, None, "MULTIPLE_PARTICIPATION_RESULTS_CONFLICT_UNRESOLVED"
    _, participation, path = sorted(candidates, key=lambda item: item[0])[-1]
    return participation, path, None


def _checks_all_passed(artifact: Mapping[str, Any], label: str) -> bool:
    checks = artifact.get("checks", [])
    if not isinstance(checks, list):
        raise ReceivedDerivativeActionPermissionError(f"{label} checks must be a list")
    return all(
        isinstance(check, Mapping) and check.get("passed") is True
        for check in checks
    )


def _effective_inputs_from_participation(
    participation: Mapping[str, Any],
) -> dict[str, Any]:
    selected = _section(participation, "selected_source_surface")
    raw = selected.get("selected_source_surface_effective_references")
    if not isinstance(raw, Mapping):
        raise ReceivedDerivativeActionPermissionError(
            "effective references must be an object"
        )
    result = dict(raw)
    for key in PATH_INPUT_KEYS:
        if not isinstance(result.get(key), str) or not str(result.get(key)).strip():
            raise ReceivedDerivativeActionPermissionError(
                f"effective reference {key} must be a non-empty string"
            )
    for key in ("effective_source_run_path", "effective_ingress_run_path"):
        if result.get(key) is not None and not isinstance(result.get(key), str):
            raise ReceivedDerivativeActionPermissionError(
                f"effective reference {key} must be a string when present"
            )
    return {key: result.get(key) for key in EFFECTIVE_INPUT_KEYS}


def _load_effective_artifacts(
    inputs: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    labels = (
        ("effective_authority_artifact_path", "effective authority artifact"),
        ("effective_family_packet_path", "effective run-family packet"),
        ("effective_status_packet_path", "effective preserved-run status packet"),
        (
            "effective_current_governing_packet_path",
            "effective current-governing packet",
        ),
    )
    try:
        values = tuple(_read_json_file(str(inputs[key]), label) for key, label in labels)
    except (FileNotFoundError, OSError) as exc:
        raise FileNotFoundError(str(exc)) from exc
    return values  # type: ignore[return-value]


def _effective_summaries(*artifacts: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    query_resolver = participation_resolver.receipt_resolver.transfer_resolver.query_resolver
    try:
        authority, family, status, governing = artifacts
        return {
            "authority": query_resolver.build_execution_authority_summary(authority),
            "family": query_resolver.build_run_family_summary(family),
            "status": query_resolver.build_preserved_run_status_summary(status),
            "governing": query_resolver.build_current_governing_summary(governing),
        }
    except Exception as exc:  # noqa: BLE001
        raise ReceivedDerivativeActionPermissionError(
            "effective reference artifact is malformed"
        ) from exc


def _same_path(left: Any, right: Any) -> bool:
    if not isinstance(left, str) or not isinstance(right, str):
        return False
    return _repo_path(left).resolve(strict=False) == _repo_path(right).resolve(
        strict=False
    )


def _effective_currentness_checks(
    inputs: Mapping[str, Any],
    summaries: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    canonical = {
        name: summary.get("core_execution_file")
        for name, summary in summaries.items()
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
    exposed_source = [
        value for value in source_values if isinstance(value, str) and value
    ]
    exposed_ingress = [
        value for value in ingress_values if isinstance(value, str) and value
    ]
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


def _touch_permission_path(lineage: Mapping[str, Any]) -> str | None:
    value = lineage.get("touch_permission_result_path")
    if not isinstance(value, str) or not value.strip() or value == "provided_mapping":
        return None
    return value


def _validate_touch_lineage(lineage: Mapping[str, Any]) -> list[dict[str, Any]]:
    touch_id = lineage.get("touch_permission_result_id")
    path = _touch_permission_path(lineage)
    if touch_id is None and path is None:
        return [
            _check(
                "touch_permission_lineage_optional_or_carried",
                True,
                expected="no file-backed touch-permission lineage required",
                actual=lineage,
            )
        ]
    if touch_id is not None and (not isinstance(touch_id, str) or not touch_id.strip()):
        raise ReceivedDerivativeActionPermissionError(
            "touch-permission lineage result id is malformed"
        )
    if path is None:
        return [
            _check(
                "touch_permission_lineage_file_readable_where_applicable",
                True,
                expected="provided mapping or carried touch-permission lineage",
                actual=lineage.get("touch_permission_result_path"),
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
                block_code="TOUCH_PERMISSION_LINEAGE_INCOHERENT",
            )
        ]
    metadata = _section(touch, "touch_permission_metadata")
    admitted = (
        participation_resolver.receipt_resolver.transfer_resolver.touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH
    )
    checks_passed = _checks_all_passed(touch, "touch-permission lineage")
    return [
        _check(
            "touch_permission_lineage_file_readable_where_applicable",
            True,
            expected="readable touch-permission result where path is preserved",
            actual=path,
        ),
        _check(
            "touch_permission_lineage_id_corresponds",
            not isinstance(touch_id, str)
            or metadata.get("touch_permission_result_id") == touch_id,
            expected=touch_id,
            actual=metadata.get("touch_permission_result_id"),
            block_code="TOUCH_PERMISSION_LINEAGE_INCOHERENT"
            if isinstance(touch_id, str)
            and metadata.get("touch_permission_result_id") != touch_id
            else None,
        ),
        _check(
            "touch_permission_lineage_is_successful",
            touch.get("outcome") == admitted,
            expected=admitted,
            actual=touch.get("outcome"),
            block_code="TOUCH_PERMISSION_LINEAGE_INCOHERENT"
            if touch.get("outcome") != admitted
            else None,
        ),
        _check(
            "touch_permission_lineage_checks_passed",
            checks_passed,
            expected="touch-permission checks all passed",
            actual="all passed" if checks_passed else "one or more failed",
            block_code="TOUCH_PERMISSION_LINEAGE_INCOHERENT"
            if not checks_passed
            else None,
        ),
    ]


def _contains(text: str, phrases: Sequence[str]) -> bool:
    return any(phrase in text for phrase in phrases)


def _request_refusal_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    text = " ".join(
        (
            str(request.get("action_basis", "")),
            str(request.get("action_surface_label", "")),
            " ".join(str(field) for field in request.get("requested_action_fields", [])),
        )
    ).lower()
    table = (
        (
            "action_request_does_not_attempt_replay",
            ("replay into", "replay-based", "allow replay"),
            "REPLAY_SHORTCUT_REFUSED",
        ),
        (
            "action_request_does_not_attempt_merge",
            ("merge into", "merge-based", "allow merge"),
            "MERGE_SHORTCUT_REFUSED",
        ),
        (
            "action_request_does_not_claim_continuity_completion",
            ("complete continuity", "continuity completion", "claim continuity"),
            "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        (
            "action_request_does_not_silently_upgrade_standing",
            ("standing upgrade", "upgrade standing"),
            "SILENT_STANDING_UPGRADE_REFUSED",
        ),
        (
            "action_request_does_not_request_stale_prior_family_fallback",
            ("stale prior", "prior-family fallback"),
            "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
        (
            "action_request_does_not_infer_from_latest_files",
            (
                "latest authority",
                "latest family",
                "latest status",
                "latest governing",
                "latest receipt",
                "latest transfer",
                "latest participation",
            ),
            "LATEST_FILE_INFERENCE_REFUSED",
        ),
        (
            "action_request_does_not_authorize_mutation",
            ("mutate", "rewrite", "overwrite", "delete prior"),
            "IMPLICIT_MUTATION_REFUSED",
        ),
        (
            "action_request_does_not_claim_implicit_authority",
            (
                "final governance",
                "system law",
                "protocol law",
                "governing standing",
                "authority claim",
                "final identity",
                "constitutional author",
                "local authority",
            ),
            "IMPLICIT_AUTHORITY_CLAIM_REFUSED",
        ),
        (
            "action_request_does_not_replace_source",
            ("replace source", "source replacement", "become source"),
            "SOURCE_REPLACEMENT_REFUSED",
        ),
        (
            "action_request_preserves_source_transfer_receipt_derivative_distinction",
            (
                "collapse source",
                "collapse transfer",
                "collapse receipt",
                "collapse derivative",
                "derivative becomes source",
            ),
            "SOURCE_TRANSFER_RECEIPT_DERIVATIVE_COLLAPSE_REFUSED",
        ),
    )
    return [
        _check(
            name,
            not _contains(text, phrases),
            expected=f"no {code.lower()}",
            actual=request.get("action_basis"),
            block_code=code if _contains(text, phrases) else None,
        )
        for name, phrases, code in table
    ]


def _non_claim_checks(non_claims: Mapping[str, bool]) -> list[dict[str, Any]]:
    block_by_key = {
        "replayed_into_live_host": "REPLAY_SHORTCUT_REFUSED",
        "merged_into_local_state": "MERGE_SHORTCUT_REFUSED",
        "continuity_completed": "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        "standing_upgraded": "SILENT_STANDING_UPGRADE_REFUSED",
    }
    checks = [
        _check(
            f"non_claim_{key}_remains_false",
            non_claims.get(key) is False,
            expected=False,
            actual=non_claims.get(key),
            block_code=block_by_key[key] if non_claims.get(key) is not False else None,
        )
        for key in REQUIRED_FALSE_NON_CLAIMS
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
    checks.append(
        _check(
            "non_claim_source_replaced_remains_false",
            non_claims.get("source_replaced") is False,
            expected=False,
            actual=non_claims.get("source_replaced"),
            block_code="SOURCE_REPLACEMENT_REFUSED"
            if non_claims.get("source_replaced") is not False
            else None,
        )
    )
    return checks


def _participated_field_maps(
    payload: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    fields = payload.get("participated_fields", {})
    references = payload.get("participated_references", {})
    if not isinstance(fields, Mapping) or not isinstance(references, Mapping):
        raise ReceivedDerivativeActionPermissionError(
            "participation payload fields and references must be objects"
        )
    return dict(fields), dict(references)


def _action_values(
    participation_identity: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    touch_lineage: Mapping[str, Any],
    payload: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    participated_fields, participated_references = _participated_field_maps(payload)
    values: dict[str, Any] = {
        **dict(participation_identity),
        **dict(receipt_identity),
        **dict(transfer_identity),
        **dict(source_identity),
        **dict(touch_lineage),
        "payload_participation_status": payload.get("payload_participation_status"),
        "source_remains_source": payload.get("source_remains_source"),
        "receipt_remains_receipt": payload.get("receipt_remains_receipt"),
        "transfer_remains_transfer": payload.get("transfer_remains_transfer"),
        "participation_payload_remains_derivative": payload.get(
            "participation_payload_remains_derivative"
        ),
        "participated_fields": participated_fields,
        "participated_references": participated_references,
        "non_claims": dict(non_claims),
    }
    for mapping in (participated_fields, participated_references, non_claims):
        values.update(
            {key: value for key, value in mapping.items() if isinstance(key, str)}
        )
    return values


def _action_payload_scope(
    request: Mapping[str, Any],
    participation_identity: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    touch_lineage: Mapping[str, Any],
    payload: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> tuple[dict[str, Any], dict[str, Any] | None, list[str]]:
    actor_class = str(request["actor_class"])
    action_class = str(request["action_class"])
    fields = list(request["requested_action_fields"])
    values = _action_values(
        participation_identity,
        receipt_identity,
        transfer_identity,
        source_identity,
        touch_lineage,
        payload,
        non_claims,
    )
    if actor_class not in SUPPORTED_ACTOR_CLASSES:
        return (
            _check(
                "actor_class_is_supported",
                False,
                expected=sorted(SUPPORTED_ACTOR_CLASSES),
                actual=actor_class,
                block_code="ACTOR_CLASS_OUT_OF_SCOPE",
            ),
            None,
            fields,
        )
    if action_class not in SUPPORTED_ACTION_CLASSES:
        return (
            _check(
                "action_class_is_supported",
                False,
                expected=sorted(SUPPORTED_ACTION_CLASSES),
                actual=action_class,
                block_code="ACTION_CLASS_OUT_OF_SCOPE",
            ),
            None,
            fields,
        )
    if not fields:
        return (
            _check(
                "action_payload_scope_is_bounded",
                False,
                expected="non-empty requested fields for bounded action permission",
                actual=fields,
                block_code="ACTION_PAYLOAD_OUT_OF_SCOPE",
            ),
            None,
            fields,
        )
    participated_fields, participated_references = _participated_field_maps(payload)
    allowed = (
        set(participated_fields)
        | set(participated_references)
        | {"participated_fields", "participated_references", "non_claims"}
        | set(non_claims)
    )
    invalid = sorted(
        {
            field
            for field in fields
            if field not in values or field not in allowed
        }
    )
    check = _check(
        "action_payload_scope_is_bounded",
        not invalid,
        expected="fields already participated and admitted for requested action",
        actual={"action_fields": fields, "invalid_fields": invalid},
        block_code="ACTION_PAYLOAD_OUT_OF_SCOPE" if invalid else None,
    )
    if invalid:
        return check, None, fields
    payload_result = {
        "payload_action_permission_status": "action_permitted_received_derivative",
        "source_remains_source": True,
        "receipt_remains_receipt": True,
        "transfer_remains_transfer": True,
        "participation_remains_participation": True,
        "action_permission_payload_remains_derivative": True,
        "permitted_action_fields": {field: values[field] for field in fields},
        "permitted_action_references": {
            "selected_participation_result_path": participation_identity.get(
                "selected_participation_result_path"
            ),
            "selected_participation_result_id": participation_identity.get(
                "selected_participation_result_id"
            ),
            "selected_receipt_result_path": receipt_identity.get(
                "selected_receipt_result_path"
            ),
            "selected_receipt_result_id": receipt_identity.get(
                "selected_receipt_result_id"
            ),
            "selected_transfer_result_path": transfer_identity.get(
                "selected_transfer_result_path"
            ),
            "selected_transfer_result_id": transfer_identity.get(
                "selected_transfer_result_id"
            ),
            "selected_source_surface_path": source_identity.get(
                "selected_source_surface_path"
            ),
            "selected_source_surface_id": source_identity.get(
                "selected_source_surface_id"
            ),
            "selected_source_surface_effective_references": source_identity.get(
                "selected_source_surface_effective_references"
            ),
            "touch_permission_result_path": touch_lineage.get(
                "touch_permission_result_path"
            ),
            "touch_permission_result_id": touch_lineage.get(
                "touch_permission_result_id"
            ),
        },
    }
    return check, payload_result, fields


def _result_id(
    participation_identity: Mapping[str, Any],
    request: Mapping[str, Any],
    outcome: str,
) -> str:
    participation_id = (
        participation_identity.get("selected_participation_result_id")
        or "no_participation_result"
    )
    request_id = (
        request.get("received_derivative_action_permission_request_id")
        or "action_permission_request"
    )
    suffix = "permitted" if outcome == OUTCOME_ACTION_PERMITTED else "refused"
    return (
        f"{participation_id}__{request_id}__"
        f"received_derivative_action_permission_{suffix}"
    )


def _result(
    request: Mapping[str, Any],
    participation_identity: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
    transfer_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    action_permission_payload: Mapping[str, Any] | None,
    action_permission_summary: Mapping[str, Any] | None,
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    return {
        "received_derivative_action_permission_metadata": {
            "received_derivative_action_permission_result_id": _result_id(
                participation_identity,
                request,
                outcome,
            ),
            "received_derivative_action_permission_result_type": RECEIVED_DERIVATIVE_ACTION_PERMISSION_RESULT_TYPE,
            "received_derivative_action_permission_result_version": RECEIVED_DERIVATIVE_ACTION_PERMISSION_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_participation_result": dict(participation_identity),
        "selected_receipt_result": dict(receipt_identity),
        "selected_transfer_result": dict(transfer_identity),
        "selected_source_surface": dict(source_identity),
        "action_permission_request": dict(request),
        "checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": BLOCK_REASONS.get(block_code) if block_code else None,
        },
        "action_permission_payload": dict(action_permission_payload)
        if action_permission_payload is not None
        else None,
        "action_permission_summary": dict(action_permission_summary)
        if action_permission_summary is not None
        else None,
        "non_claims": dict(non_claims),
    }


def _refused_result(
    request: Mapping[str, Any],
    block_code: str,
    checks: Sequence[Mapping[str, Any]],
    participation_identity: Mapping[str, Any] | None = None,
    receipt_identity: Mapping[str, Any] | None = None,
    transfer_identity: Mapping[str, Any] | None = None,
    source_identity: Mapping[str, Any] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    return _result(
        request,
        participation_identity or _participation_identity(None, None),
        receipt_identity or _receipt_identity_from_participation(None),
        transfer_identity or _transfer_identity_from_participation(None),
        source_identity or _source_identity_from_participation(None),
        checks,
        OUTCOME_REFUSED,
        block_code,
        None,
        None,
        non_claims or dict(NON_CLAIM_DEFAULTS),
    )


def _fail_if_needed(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
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
        block_code = "EFFECTIVE_REFERENCE_INCOHERENCE"
    return _refused_result(
        request,
        block_code,
        checks,
        participation_identity=participation_identity,
        receipt_identity=receipt_identity,
        transfer_identity=transfer_identity,
        source_identity=source_identity,
        non_claims=non_claims,
    )


def _resolve_selected_participation(
    request: Mapping[str, Any],
    participation: Mapping[str, Any],
    participation_path: Path | str | None,
    selection_source: str,
) -> dict[str, Any]:
    if not _looks_like_participation_result(participation):
        return _refused_result(
            request,
            "SELECTED_PARTICIPATION_RESULT_OUT_OF_SCOPE",
            [
                _check(
                    "selected_participation_result_is_in_action_permission_scope",
                    False,
                    expected="received-derivative participation result",
                    actual="unrecognized artifact",
                    block_code="SELECTED_PARTICIPATION_RESULT_OUT_OF_SCOPE",
                )
            ],
        )

    participation_identity = _participation_identity(
        participation,
        participation_path,
    )
    receipt_identity = _receipt_identity_from_participation(participation)
    transfer_identity = _transfer_identity_from_participation(participation)
    source_identity = _source_identity_from_participation(participation)
    touch_lineage = _touch_lineage_from_participation(participation)
    non_claims = _merge_non_claims(participation)
    outcome = participation.get("outcome")

    if outcome == participation_resolver.OUTCOME_REFUSED or outcome == "BLOCKED":
        return _refused_result(
            request,
            "SELECTED_PARTICIPATION_RESULT_BLOCKED",
            [
                _check(
                    "selected_participation_result_has_participated_outcome",
                    False,
                    expected=participation_resolver.OUTCOME_PARTICIPATED,
                    actual=outcome,
                    block_code="SELECTED_PARTICIPATION_RESULT_BLOCKED",
                )
            ],
            participation_identity,
            receipt_identity,
            transfer_identity,
            source_identity,
            non_claims,
        )
    if outcome != participation_resolver.OUTCOME_PARTICIPATED:
        return _refused_result(
            request,
            "SELECTED_PARTICIPATION_RESULT_NOT_PARTICIPATED",
            [
                _check(
                    "selected_participation_result_has_participated_outcome",
                    False,
                    expected=participation_resolver.OUTCOME_PARTICIPATED,
                    actual=outcome,
                    block_code="SELECTED_PARTICIPATION_RESULT_NOT_PARTICIPATED",
                )
            ],
            participation_identity,
            receipt_identity,
            transfer_identity,
            source_identity,
            non_claims,
        )

    for key in (
        "selected_receipt_result",
        "selected_transfer_result",
        "selected_source_surface",
        "participation_request",
    ):
        _section(participation, key)
    payload = participation.get("participation_payload")
    payload_ok = isinstance(payload, Mapping)
    participation_checks_passed = _checks_all_passed(
        participation,
        "selected participation result",
    )
    checks: list[dict[str, Any]] = [
        _check(
            "selected_participation_result_exists_and_is_readable",
            True,
            expected="one readable selected participation result",
            actual=participation_identity.get("selected_participation_result_path"),
        ),
        _check(
            "selected_participation_result_has_participated_outcome",
            True,
            expected=participation_resolver.OUTCOME_PARTICIPATED,
            actual=outcome,
        ),
        _check(
            "selected_participation_result_is_in_action_permission_scope",
            True,
            expected="received-derivative participation result",
            actual=participation_identity.get("selected_participation_result_type"),
        ),
        _check(
            "selected_participation_result_checks_passed",
            participation_checks_passed,
            expected="participation checks all passed",
            actual="all passed" if participation_checks_passed else "one or more failed",
            block_code="EFFECTIVE_REFERENCE_INCOHERENCE"
            if not participation_checks_passed
            else None,
        ),
        _check(
            "participation_payload_is_readable",
            payload_ok,
            expected="participation_payload object",
            actual=payload,
            block_code="PARTICIPATION_PAYLOAD_UNREADABLE" if not payload_ok else None,
        ),
    ]
    if not payload_ok or not isinstance(payload, Mapping):
        return _refused_result(
            request,
            "PARTICIPATION_PAYLOAD_UNREADABLE",
            checks,
            participation_identity,
            receipt_identity,
            transfer_identity,
            source_identity,
            non_claims,
        )
    try:
        _participated_field_maps(payload)
    except ReceivedDerivativeActionPermissionError:
        checks.append(
            _check(
                "participation_payload_fields_and_references_are_objects",
                False,
                expected="participated_fields and participated_references objects",
                actual=payload,
                block_code="PARTICIPATION_PAYLOAD_MALFORMED",
            )
        )
        return _refused_result(
            request,
            "PARTICIPATION_PAYLOAD_MALFORMED",
            checks,
            participation_identity,
            receipt_identity,
            transfer_identity,
            source_identity,
            non_claims,
        )

    source_refs = source_identity.get("selected_source_surface_effective_references")
    source_identity_missing = any(
        not isinstance(source_identity.get(key), str)
        or not str(source_identity.get(key)).strip()
        for key in (
            "selected_source_surface_id",
            "selected_source_surface_family",
            "selected_source_surface_outcome",
        )
    ) or not isinstance(source_refs, Mapping)
    transfer_identity_missing = not isinstance(
        transfer_identity.get("selected_transfer_result_id"),
        str,
    ) or not str(transfer_identity.get("selected_transfer_result_id")).strip()
    receipt_identity_missing = not isinstance(
        receipt_identity.get("selected_receipt_result_id"),
        str,
    ) or not str(receipt_identity.get("selected_receipt_result_id")).strip()
    checks.extend(
        [
            _check(
                "participation_payload_preserves_derivative_status",
                payload.get("payload_participation_status")
                == "participated_received_derivative",
                expected="participated_received_derivative",
                actual=payload.get("payload_participation_status"),
                block_code="PARTICIPATION_PAYLOAD_MISSING_DERIVATIVE_STATUS"
                if payload.get("payload_participation_status")
                != "participated_received_derivative"
                else None,
            ),
            _check(
                "participation_payload_preserves_source_remains_source",
                payload.get("source_remains_source") is True,
                expected=True,
                actual=payload.get("source_remains_source"),
                block_code="SOURCE_REMAINS_SOURCE_NOT_TRUE"
                if payload.get("source_remains_source") is not True
                else None,
            ),
            _check(
                "participation_payload_preserves_receipt_remains_receipt",
                payload.get("receipt_remains_receipt") is True,
                expected=True,
                actual=payload.get("receipt_remains_receipt"),
                block_code="RECEIPT_REMAINS_RECEIPT_NOT_TRUE"
                if payload.get("receipt_remains_receipt") is not True
                else None,
            ),
            _check(
                "participation_payload_preserves_transfer_remains_transfer",
                payload.get("transfer_remains_transfer") is True,
                expected=True,
                actual=payload.get("transfer_remains_transfer"),
                block_code="TRANSFER_REMAINS_TRANSFER_NOT_TRUE"
                if payload.get("transfer_remains_transfer") is not True
                else None,
            ),
            _check(
                "participation_payload_preserves_derivative_payload_status",
                payload.get("participation_payload_remains_derivative") is True,
                expected=True,
                actual=payload.get("participation_payload_remains_derivative"),
                block_code="PARTICIPATION_PAYLOAD_REMAINS_DERIVATIVE_NOT_TRUE"
                if payload.get("participation_payload_remains_derivative") is not True
                else None,
            ),
            _check(
                "selected_receipt_result_identity_is_preserved",
                not receipt_identity_missing,
                expected="selected receipt id",
                actual=receipt_identity,
                block_code="SELECTED_RECEIPT_RESULT_IDENTITY_MISSING"
                if receipt_identity_missing
                else None,
            ),
            _check(
                "selected_transfer_result_identity_is_preserved",
                not transfer_identity_missing,
                expected="selected transfer id",
                actual=transfer_identity,
                block_code="SELECTED_TRANSFER_RESULT_IDENTITY_MISSING"
                if transfer_identity_missing
                else None,
            ),
            _check(
                "selected_source_surface_identity_is_preserved",
                not source_identity_missing,
                expected="source identity and effective references",
                actual=source_identity,
                block_code="SELECTED_SOURCE_SURFACE_IDENTITY_MISSING"
                if source_identity_missing
                else None,
            ),
            _check(
                "action_uses_selected_participation_result_not_latest_files_alone",
                True,
                expected="selected participation result",
                actual=selection_source,
            ),
            _check(
                "action_does_not_fall_back_to_stale_prior_family",
                True,
                expected="carried effective references",
                actual=source_refs,
            ),
        ]
    )
    early_refusal = _fail_if_needed(
        request,
        checks,
        participation_identity,
        receipt_identity,
        transfer_identity,
        source_identity,
        non_claims,
    )
    if early_refusal is not None:
        return early_refusal

    checks.extend(_validate_touch_lineage(touch_lineage))
    touch_refusal = _fail_if_needed(
        request,
        checks,
        participation_identity,
        receipt_identity,
        transfer_identity,
        source_identity,
        non_claims,
    )
    if touch_refusal is not None:
        return touch_refusal

    effective_inputs = _effective_inputs_from_participation(participation)
    try:
        effective_artifacts = _load_effective_artifacts(effective_inputs)
    except (FileNotFoundError, OSError) as exc:
        checks.append(
            _check(
                "effective_references_are_readable",
                False,
                expected="readable authority/family/status/governing artifacts",
                actual=str(exc),
                block_code="EFFECTIVE_REFERENCE_INCOHERENCE",
            )
        )
        return _refused_result(
            request,
            "EFFECTIVE_REFERENCE_INCOHERENCE",
            checks,
            participation_identity,
            receipt_identity,
            transfer_identity,
            source_identity,
            non_claims,
        )
    checks.append(
        _check(
            "effective_references_are_readable",
            True,
            expected="readable authority/family/status/governing artifacts",
            actual={key: effective_inputs.get(key) for key in PATH_INPUT_KEYS},
        )
    )
    checks.extend(
        _effective_currentness_checks(
            effective_inputs,
            _effective_summaries(*effective_artifacts),
        )
    )
    checks.extend(
        [
            _check(
                "actor_class_is_supported",
                request["actor_class"] in SUPPORTED_ACTOR_CLASSES,
                expected=sorted(SUPPORTED_ACTOR_CLASSES),
                actual=request["actor_class"],
                block_code="ACTOR_CLASS_OUT_OF_SCOPE"
                if request["actor_class"] not in SUPPORTED_ACTOR_CLASSES
                else None,
            ),
            _check(
                "action_class_is_supported",
                request["action_class"] in SUPPORTED_ACTION_CLASSES,
                expected=sorted(SUPPORTED_ACTION_CLASSES),
                actual=request["action_class"],
                block_code="ACTION_CLASS_OUT_OF_SCOPE"
                if request["action_class"] not in SUPPORTED_ACTION_CLASSES
                else None,
            ),
        ]
    )
    scope_check, action_permission_payload, fields = _action_payload_scope(
        request,
        participation_identity,
        receipt_identity,
        transfer_identity,
        source_identity,
        touch_lineage,
        payload,
        non_claims,
    )
    checks.append(scope_check)
    checks.extend(_request_refusal_checks(request))
    checks.extend(_non_claim_checks(non_claims))
    distinctions_ok = action_permission_payload is None or (
        action_permission_payload.get("payload_action_permission_status")
        == "action_permitted_received_derivative"
        and action_permission_payload.get("source_remains_source") is True
        and action_permission_payload.get("receipt_remains_receipt") is True
        and action_permission_payload.get("transfer_remains_transfer") is True
        and action_permission_payload.get("participation_remains_participation") is True
        and action_permission_payload.get("action_permission_payload_remains_derivative")
        is True
    )
    checks.append(
        _check(
            "source_transfer_receipt_participation_derivative_distinctions_preserved",
            distinctions_ok,
            expected="all distinctions preserved",
            actual=action_permission_payload,
            block_code="SOURCE_TRANSFER_RECEIPT_DERIVATIVE_COLLAPSE_REFUSED"
            if not distinctions_ok
            else None,
        )
    )
    refusal = _fail_if_needed(
        request,
        checks,
        participation_identity,
        receipt_identity,
        transfer_identity,
        source_identity,
        non_claims,
    )
    if refusal is not None:
        return refusal

    action_permission_summary = {
        "permitted_action_field_count": len(fields),
        "permitted_action_field_names": list(fields),
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
        "selected_source_surface_family": source_identity.get(
            "selected_source_surface_family"
        ),
        "actor_class": request.get("actor_class"),
        "action_class": request.get("action_class"),
        "action_basis": request.get("action_basis"),
        "action_surface_label": request.get("action_surface_label"),
    }
    return _result(
        request,
        participation_identity,
        receipt_identity,
        transfer_identity,
        source_identity,
        checks,
        OUTCOME_ACTION_PERMITTED,
        None,
        action_permission_payload,
        action_permission_summary,
        non_claims,
    )


def resolve_received_derivative_action_permission(
    action_permission_request: Mapping[str, Any],
    participation_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded received-derivative action-permission decision."""

    request = _normal_action_permission_request(action_permission_request)
    if participation_result is not None:
        if not isinstance(participation_result, Mapping):
            raise ReceivedDerivativeActionPermissionError(
                "participation_result must be a mapping or None"
            )
        return _resolve_selected_participation(
            request,
            dict(participation_result),
            None,
            "provided_mapping",
        )
    participation, path, block_code = _select_default_participation_result()
    if block_code is not None:
        return _refused_result(
            request,
            block_code,
            [
                _check(
                    "admissible_participation_result_selected",
                    False,
                    expected="one participated participation result",
                    actual=block_code,
                    block_code=block_code,
                )
            ],
        )
    if participation is None:
        raise ReceivedDerivativeActionPermissionError(
            "selected participation result is absent"
        )
    return _resolve_selected_participation(
        request,
        participation,
        path,
        "participation_result_discovery",
    )


def resolve_received_derivative_action_permission_from_path(
    participation_result_path: Path | str,
    action_permission_request: Mapping[str, Any],
) -> dict[str, Any]:
    """Read one participation result and resolve action permission."""

    request = _normal_action_permission_request(action_permission_request)
    resolved_path = _repo_path(participation_result_path)
    try:
        participation = _read_json_file(
            resolved_path,
            "selected received-derivative participation result",
        )
    except (FileNotFoundError, OSError):
        return _refused_result(
            request,
            "SELECTED_PARTICIPATION_RESULT_UNREADABLE",
            [
                _check(
                    "selected_participation_result_exists_and_is_readable",
                    False,
                    expected="readable selected participation result",
                    actual=_display_path(resolved_path),
                    block_code="SELECTED_PARTICIPATION_RESULT_UNREADABLE",
                )
            ],
            participation_identity=_participation_identity(None, resolved_path),
        )
    return _resolve_selected_participation(
        request,
        participation,
        resolved_path,
        "explicit_participation_result_path",
    )


def build_received_derivative_action_permission_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact inspection summary for one action-permission result."""

    if not isinstance(result, Mapping):
        raise ReceivedDerivativeActionPermissionError(
            "action-permission result must be a mapping"
        )
    checks = result.get("checks", [])
    if not isinstance(checks, list):
        raise ReceivedDerivativeActionPermissionError(
            "action-permission checks must be a list"
        )
    passed, failed = _count_checks(checks)
    metadata = result.get("received_derivative_action_permission_metadata", {})
    participation = result.get("selected_participation_result", {})
    receipt = result.get("selected_receipt_result", {})
    transfer = result.get("selected_transfer_result", {})
    source = result.get("selected_source_surface", {})
    request = result.get("action_permission_request", {})
    block = result.get("block", {})
    summary = result.get("action_permission_summary", {})
    non_claims = result.get("non_claims", {})
    return {
        "received_derivative_action_permission_result_id": metadata.get(
            "received_derivative_action_permission_result_id"
        )
        if isinstance(metadata, Mapping)
        else None,
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason")
        if isinstance(block, Mapping)
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
        "actor_class": request.get("actor_class") if isinstance(request, Mapping) else None,
        "action_class": request.get("action_class")
        if isinstance(request, Mapping)
        else None,
        "permitted_action_field_names": summary.get("permitted_action_field_names")
        if isinstance(summary, Mapping)
        else None,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (*REQUIRED_FALSE_NON_CLAIMS, "source_replaced")
            if isinstance(non_claims, Mapping)
        },
    }


def _default_output_path(result: Mapping[str, Any]) -> Path:
    selected = result.get("selected_participation_result", {})
    selected_id = (
        selected.get("selected_participation_result_id")
        if isinstance(selected, Mapping)
        else None
    )
    stem = _safe_filename_part(selected_id)
    root = _repo_path(RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT)
    candidate = root / f"{stem}__received_derivative_action_permission_result.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = (
            root
            / f"{stem}__received_derivative_action_permission_result_{index:03d}.json"
        )
        if not candidate.exists():
            return candidate
    raise ReceivedDerivativeActionPermissionError(
        "no bounded action-permission filename available"
    )


def write_received_derivative_action_permission_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive received-derivative action-permission JSON result."""

    if not isinstance(result, Mapping):
        raise ReceivedDerivativeActionPermissionError(
            "action-permission result must be a mapping"
        )
    target = _repo_path(output_path) if output_path is not None else _default_output_path(result)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(
            f"received-derivative action-permission result already exists: {target}"
        )
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
