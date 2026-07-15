"""Resolve bounded current self-orientation with closed re-entry recognition.

This successor preserves the v2 self-orientation model and adds one narrow
post-receipt recognition surface: a re-entry admission that was received and
exhausted. The closed cycle is recognized only as downstream posture.

This module does not replay the host, merge preserved runs, mutate upstream
artifacts, create authority, create workflow machinery, infer currentness by
recency, or turn receipt into permission for another step.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CurrentSelfOrientationV3Error(RuntimeError):
    """Raised for malformed selected inputs or impossible correspondence."""

    def __init__(
        self,
        message: str,
        block_code: str,
        *,
        selected_inputs: Mapping[str, Any] | None = None,
        checks: Sequence[Mapping[str, Any]] | None = None,
    ) -> None:
        super().__init__(message)
        self.block_code = block_code
        self.selected_inputs = (
            copy.deepcopy(dict(selected_inputs))
            if isinstance(selected_inputs, Mapping)
            else None
        )
        self.checks = [dict(check) for check in checks] if checks is not None else None


V0_BODY_PASS_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_v0_body_pass")
CURRENT_SELF_ORIENTATION_V2_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v2"
)
CURRENT_SELF_ORIENTATION_REENTRY_ADMISSIBILITY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_current_self_orientation_reentry_admissibility"
)
CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_current_self_orientation_reentry_receipt"
)
CURRENT_SELF_ORIENTATION_V3_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v3"
)

EXECUTION_AUTHORITY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_execution_authority"
)
RUN_FAMILY_PACKET_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_run_family_packets"
)
PRESERVED_RUN_STATUS_PACKET_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_preserved_run_status_packets"
)
CURRENT_GOVERNING_PACKET_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_governing_packets"
)
CURRENT_STATE_ANSWER_SURFACE_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_answer_surface"
)
CURRENT_STATE_WHAT_STANDS_NOW_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_what_stands_now"
)
CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_what_remains_open"
)
CURRENT_STATE_TOUCH_PERMISSION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission"
)
CONTINUITY_TRANSFER_UNIT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_continuity_transfer_unit"
)
CONTINUITY_TRANSFER_RECEIPT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_continuity_transfer_receipt"
)
RECEIVED_DERIVATIVE_PARTICIPATION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_received_derivative_participation"
)
RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_received_derivative_action_permissions"
)
CONTINUITY_MEMORY_SEAM_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_continuity_memory_seam"
)
OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT = Path(
    "artifacts/openai_api_derivative_vessel_bounded_current_state_read_v3"
)
OPERATOR_TERMINAL_BRIEF_ROOT = Path(
    "artifacts/operator_facing_terminal_brief_bounded_current_state_read"
)

RESOLVER_MODULE = "resolve_current_self_orientation_v3"
SUCCESSOR_OF_MODULE = "resolve_current_self_orientation_v2"
CURRENT_SELF_ORIENTATION_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V3_RESULT"
)
CURRENT_SELF_ORIENTATION_RESULT_VERSION = "0.3.0"
DEFAULT_RESULT_STEM = "current_self_orientation_v3_result"

SELF_ORIENTATION_V2_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V2_RESULT"
)
SELF_ORIENTATION_V2_RESOLVER_MODULE = "resolve_current_self_orientation_v2"
REENTRY_ADMISSIBILITY_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_"
    "REENTRY_ADMISSIBILITY_RESULT"
)
REENTRY_ADMISSIBILITY_RESOLVER_MODULE = (
    "resolve_current_self_orientation_reentry_admissibility"
)
REENTRY_RECEIPT_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_"
    "REENTRY_RECEIPT_RESULT"
)
REENTRY_RECEIPT_RESOLVER_MODULE = "resolve_current_self_orientation_reentry_receipt"

OUTCOME_SELF_ORIENTED = "SELF_ORIENTED"
OUTCOME_BLOCKED = "BLOCKED"
OUTCOME_BODY_PASS_CONFIRMED = "V0_BODY_PASS_CONFIRMED"
OUTCOME_REENTRY_ADMITTED = "REENTRY_ADMITTED"
OUTCOME_REENTRY_RECEIVED = "REENTRY_RECEIVED"

BLOCK_REASONS = {
    "NO_SELF_ORIENTATION_SOURCE_BASIS": (
        "No bounded self-orientation source basis is available."
    ),
    "REQUIRED_SOURCE_ARTIFACT_UNREADABLE": (
        "A required selected source artifact could not be read."
    ),
    "SOURCE_ARTIFACT_MALFORMED": "A selected source artifact is malformed.",
    "CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS": (
        "The current/effective basis is absent or ambiguous."
    ),
    "CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED": (
        "A required current-state surface is absent for the selected basis."
    ),
    "DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING": (
        "A derivative surface does not preserve the required source basis."
    ),
    "OPERATOR_SURFACE_DERIVATIVE_OR_SOURCE_BASIS_MISSING": (
        "An operator-facing surface does not preserve the required derivative/source basis."
    ),
    "LATEST_FILE_RECENCY_REFUSED": (
        "Currentness inferred by latest-file recency alone is refused."
    ),
    "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY": (
        "A derivative surface was treated as source authority."
    ),
    "OPERATOR_SURFACE_TREATED_AS_SOURCE_AUTHORITY": (
        "An operator-facing surface was treated as source authority."
    ),
    "OPEN_SURFACE_TREATED_AS_COMPLETED": (
        "An open surface was treated as completed."
    ),
    "BLOCKED_OR_REFUSED_SURFACE_HIDDEN": (
        "A blocked or refused surface was hidden."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A carried non-claim is missing or no longer false."
    ),
    "CORRESPONDENCE_CHECK_FAILED": (
        "A bounded correspondence/proportion check failed."
    ),
    "OVER_MIRRORING_REFUSED": (
        "Self-orientation attempted to become a whole-body replacement."
    ),
    "UNDER_MIRRORING_REFUSED": (
        "Self-orientation omitted required standing posture."
    ),
    "MULTIPLE_CANDIDATE_CURRENT_SURFACES_CONFLICT_UNRESOLVED": (
        "Multiple candidate current surfaces conflict without bounded resolution."
    ),
    "EXTERNAL_READER_ORIENTATION_ATTEMPTED": (
        "External-reader orientation is outside the bounded self-orientation surface."
    ),
    "HAND_MAINTAINED_SUMMARY_SEAM_ATTEMPTED": (
        "A hand-maintained summary seam is outside the bounded self-orientation surface."
    ),
    "REENTRY_ADMISSIBILITY_UNREADABLE": (
        "The selected re-entry admissibility result could not be read."
    ),
    "REENTRY_ADMISSIBILITY_MALFORMED": (
        "The selected re-entry admissibility result is malformed."
    ),
    "REENTRY_ADMISSIBILITY_NOT_ADMITTED": (
        "The selected re-entry admissibility result is not REENTRY_ADMITTED."
    ),
    "REENTRY_RECEIPT_UNREADABLE": (
        "The selected re-entry receipt result could not be read."
    ),
    "REENTRY_RECEIPT_MALFORMED": (
        "The selected re-entry receipt result is malformed."
    ),
    "REENTRY_RECEIPT_NOT_RECEIVED": (
        "The selected re-entry receipt result is not REENTRY_RECEIVED."
    ),
    "REENTRY_RECEIPT_DOES_NOT_MATCH_SELECTED_ADMISSIBILITY": (
        "The re-entry receipt does not match the selected re-entry admissibility result."
    ),
    "REENTRY_RECEIPT_DOES_NOT_MATCH_SELECTED_SELF_ORIENTATION_BASIS": (
        "The re-entry receipt does not match the selected self-orientation basis."
    ),
    "REENTRY_RECEIPT_BASIS_LOCK_NOT_MATCHED": (
        "The re-entry receipt does not preserve a matched basis lock."
    ),
    "REENTRY_RECEIPT_PERFORMED_STEP_CORRESPONDENCE_FAILED": (
        "The re-entry receipt does not preserve performed-step correspondence."
    ),
    "REENTRY_RECEIPT_SCOPE_NOT_SINGLE_STEP_ADDITIVE": (
        "The re-entry receipt does not preserve single-step additive scope."
    ),
    "REENTRY_RECEIPT_EXHAUSTION_NOT_CLOSED": (
        "The re-entry receipt does not preserve exhaustion and closure."
    ),
    "REENTRY_RECEIPT_FAILED_CHECKS_PRESENT": (
        "The re-entry receipt preserves failed checks."
    ),
    "REENTRY_RECEIPT_FOLLOW_ON_PERMISSION_LEAK": (
        "The re-entry receipt leaks follow-on permission."
    ),
    "REENTRY_RECEIPT_GENERAL_PERMISSION_LEAK": (
        "The re-entry receipt leaks general continuation permission."
    ),
    "REENTRY_RECEIPT_REUSABLE_ADMISSION_LEAK": (
        "The re-entry receipt leaks reusable admission permission."
    ),
    "REENTRY_SURFACE_TREATED_AS_AUTHORITY": (
        "A re-entry admissibility or receipt surface was treated as authority."
    ),
    "REENTRY_CYCLE_TREATED_AS_WORKFLOW_LANE": (
        "The closed re-entry cycle was treated as a workflow lane."
    ),
}

REQUIRED_V2_TOP_LEVEL_KEYS = frozenset(
    {
        "current_self_orientation_v2_metadata",
        "selected_orientation_inputs",
        "recognized_current_executable_core_line",
        "recognized_governing_effective_basis",
        "recognized_current_state_surfaces",
        "recognized_continuity_surfaces",
        "recognized_derivative_surfaces",
        "recognized_operator_facing_surfaces",
        "recognized_open_surfaces",
        "recognized_blocked_or_refused_surfaces",
        "recognized_touch_admissibility_surfaces",
        "bounded_correspondence_checks",
        "outcome",
        "block",
        "self_orientation_basis",
        "current_self_orientation_summary",
        "non_claims",
    }
)

EFFECTIVE_REFERENCE_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
)

BASIS_LOCK_KEYS = (
    "selected_body_pass_result_id",
    "selected_body_pass_result_path",
    "selected_source_surface_id",
    "selected_source_surface_path",
    "selected_current_state_answer_read_id",
    "selected_current_state_answer_read_path",
    "selected_what_stands_now_id",
    "selected_what_stands_now_path",
    *EFFECTIVE_REFERENCE_KEYS,
)

NON_CLAIM_DEFAULTS = {
    "authority_created": False,
    "continuity_completed": False,
    "final_governance_completed": False,
    "final_system_identity_completed": False,
    "standing_upgraded": False,
    "source_replaced": False,
    "source_scope_widened": False,
    "derivative_outputs_upgraded_to_source": False,
    "operator_outputs_upgraded_to_source": False,
    "general_permission_created": False,
    "follow_on_steps_authorized": False,
    "admission_reusable": False,
    "self_orientation_became_authority": False,
    "reentry_admissibility_became_authority": False,
    "receipt_became_authority": False,
    "reentry_cycle_became_workflow_lane": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
    "roadmap_generated": False,
    "next_organ_self_generated": False,
    "workflow_engine_created": False,
    "external_reader_orientation_created": False,
    "hand_maintained_summary_seam_created": False,
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
        return str(resolved.resolve(strict=False).relative_to(_repo_root().resolve(strict=False)))
    except ValueError:
        return str(resolved)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _clone(value: Any) -> Any:
    return copy.deepcopy(value)


def _string_or_none(value: Any) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def _safe_filename_part(value: Any) -> str:
    text = _string_or_none(value) or "no_selected_body_pass_result"
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", text).strip("._")
    return compact[:160] or "no_selected_body_pass_result"


def _require_mapping(value: Any, context: str, block_code: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise CurrentSelfOrientationV3Error(f"{context} must be an object", block_code)
    return value


def _read_json_file(
    path: Path | str,
    *,
    context: str,
    missing_code: str,
    unreadable_code: str,
    malformed_code: str,
) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise CurrentSelfOrientationV3Error(
            f"{context} not found: {resolved}",
            missing_code,
        ) from exc
    except OSError as exc:
        raise CurrentSelfOrientationV3Error(
            f"{context} is unreadable: {resolved}",
            unreadable_code,
        ) from exc
    except json.JSONDecodeError as exc:
        raise CurrentSelfOrientationV3Error(
            f"{context} is malformed JSON: {resolved}",
            malformed_code,
        ) from exc
    if not isinstance(value, dict):
        raise CurrentSelfOrientationV3Error(
            f"{context} must be a JSON object: {resolved}",
            malformed_code,
        )
    return value


def _discover_json_files(root: Path | str) -> list[Path]:
    resolved = _repo_path(root)
    if not resolved.is_dir():
        return []
    return sorted(path for path in resolved.glob("*.json") if path.is_file())


def _check(
    name: str,
    passed: bool,
    *,
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


def _block_reason(block_code: str | None, detail: str | None = None) -> str | None:
    if block_code is None:
        return None
    reason = BLOCK_REASONS.get(block_code, block_code.replace("_", " ").lower() + ".")
    return f"{reason} {detail}" if detail else reason


def _metadata_section(result: Mapping[str, Any], preferred_key: str | None = None) -> Mapping[str, Any]:
    if preferred_key is not None and isinstance(result.get(preferred_key), Mapping):
        return result[preferred_key]  # type: ignore[index]
    for key, value in result.items():
        if key.endswith("_metadata") and isinstance(value, Mapping):
            return value
    return {}


def _metadata_value(result: Mapping[str, Any], *keys: str) -> Any:
    metadata = _metadata_section(result)
    for key in keys:
        if key in result:
            return result.get(key)
        if key in metadata:
            return metadata.get(key)
    return None


def _path_equal(left: Any, right: Any) -> bool:
    left_text = _string_or_none(left)
    right_text = _string_or_none(right)
    if left_text is None or right_text is None:
        return False
    return left_text == right_text or _display_path(left_text) == _display_path(right_text)


def _identity(
    *,
    result_id: Any = None,
    result_path: Any = None,
    result_type: Any = None,
    result_version: Any = None,
    resolver_module: Any = None,
    outcome: Any = None,
    selection_mode: Any = None,
    result_family: Any = None,
    source_surface_id: Any = None,
    source_surface_family: Any = None,
) -> dict[str, Any]:
    return {
        "result_id": result_id,
        "result_path": _display_path(result_path) if result_path is not None else None,
        "result_type": result_type,
        "result_version": result_version,
        "resolver_module": resolver_module,
        "outcome": outcome,
        "selection_mode": selection_mode,
        "result_family": result_family,
        "source_surface_id": source_surface_id,
        "source_surface_family": source_surface_family,
    }


def _body_pass_identity(
    body_pass_result: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _metadata_section(body_pass_result, "v0_body_pass_metadata")
    return _identity(
        result_id=metadata.get("v0_body_pass_result_id")
        or body_pass_result.get("v0_body_pass_result_id")
        or body_pass_result.get("result_id"),
        result_path=path,
        result_type=metadata.get("v0_body_pass_result_type")
        or body_pass_result.get("result_type"),
        result_version=metadata.get("v0_body_pass_result_version")
        or body_pass_result.get("result_version"),
        resolver_module=metadata.get("runner_module")
        or body_pass_result.get("resolver_module"),
        outcome=body_pass_result.get("outcome"),
        selection_mode=selection_mode,
        result_family="v0_body_pass_result",
    )


def _self_orientation_v2_identity(
    result: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _metadata_section(result, "current_self_orientation_v2_metadata")
    return _identity(
        result_id=metadata.get("self_orientation_result_id"),
        result_path=path,
        result_type=metadata.get("self_orientation_result_type"),
        result_version=metadata.get("self_orientation_result_version"),
        resolver_module=metadata.get("resolver_module"),
        outcome=result.get("outcome"),
        selection_mode=selection_mode,
        result_family="current_self_orientation_v2_result",
    )


def _reentry_admissibility_identity(
    result: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _metadata_section(
        result,
        "current_self_orientation_reentry_admissibility_metadata",
    )
    return _identity(
        result_id=metadata.get("reentry_admissibility_result_id"),
        result_path=path,
        result_type=metadata.get("reentry_admissibility_result_type"),
        result_version=metadata.get("reentry_admissibility_result_version"),
        resolver_module=metadata.get("resolver_module"),
        outcome=result.get("outcome"),
        selection_mode=selection_mode,
        result_family="current_self_orientation_reentry_admissibility_result",
    )


def _reentry_receipt_identity(
    result: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _metadata_section(result, "current_self_orientation_reentry_receipt_metadata")
    return _identity(
        result_id=metadata.get("reentry_receipt_result_id"),
        result_path=path,
        result_type=metadata.get("reentry_receipt_result_type"),
        result_version=metadata.get("reentry_receipt_result_version"),
        resolver_module=metadata.get("resolver_module"),
        outcome=result.get("outcome"),
        selection_mode=selection_mode,
        result_family="current_self_orientation_reentry_receipt_result",
    )


def _select_body_pass(
    body_pass_result: Mapping[str, Any] | None = None,
    body_pass_result_path: Path | str | None = None,
) -> tuple[Path | str, dict[str, Any], str]:
    if body_pass_result is not None:
        if not isinstance(body_pass_result, Mapping):
            raise CurrentSelfOrientationV3Error(
                "body_pass_result must be an object",
                "SOURCE_ARTIFACT_MALFORMED",
            )
        artifact = copy.deepcopy(dict(body_pass_result))
        if artifact.get("outcome") != OUTCOME_BODY_PASS_CONFIRMED:
            raise CurrentSelfOrientationV3Error(
                "selected body-pass result is not confirmed",
                "NO_SELF_ORIENTATION_SOURCE_BASIS",
            )
        return "provided_mapping", artifact, "provided_body_pass_mapping"
    if body_pass_result_path is not None:
        artifact = _read_json_file(
            body_pass_result_path,
            context="selected v0 body-pass result",
            missing_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
            unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
            malformed_code="SOURCE_ARTIFACT_MALFORMED",
        )
        if artifact.get("outcome") != OUTCOME_BODY_PASS_CONFIRMED:
            raise CurrentSelfOrientationV3Error(
                "selected body-pass result is not confirmed",
                "NO_SELF_ORIENTATION_SOURCE_BASIS",
            )
        return body_pass_result_path, artifact, "explicit_body_pass_result_path"

    candidates: list[tuple[Path, dict[str, Any]]] = []
    for path in _discover_json_files(V0_BODY_PASS_ROOT):
        try:
            artifact = _read_json_file(
                path,
                context="candidate v0 body-pass result",
                missing_code="NO_SELF_ORIENTATION_SOURCE_BASIS",
                unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                malformed_code="SOURCE_ARTIFACT_MALFORMED",
            )
        except CurrentSelfOrientationV3Error:
            continue
        if artifact.get("outcome") == OUTCOME_BODY_PASS_CONFIRMED:
            candidates.append((path, artifact))
    if not candidates:
        raise CurrentSelfOrientationV3Error(
            "no confirmed body-pass result is available",
            "NO_SELF_ORIENTATION_SOURCE_BASIS",
        )
    path, artifact = candidates[-1]
    return path, artifact, "successful_body_pass_discovery"


def _v2_body_pass_identity(v2_result: Mapping[str, Any]) -> Mapping[str, Any]:
    selected = _require_mapping(
        v2_result.get("selected_orientation_inputs"),
        "selected_orientation_inputs",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    return _require_mapping(
        selected.get("selected_body_pass_result"),
        "selected_body_pass_result",
        "SOURCE_ARTIFACT_MALFORMED",
    )


def _validate_self_orientation_v2_result(result: Mapping[str, Any]) -> None:
    missing = sorted(REQUIRED_V2_TOP_LEVEL_KEYS - set(result))
    if missing:
        raise CurrentSelfOrientationV3Error(
            f"v2 self-orientation result is missing sections: {missing}",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    metadata = _metadata_section(result, "current_self_orientation_v2_metadata")
    if metadata.get("self_orientation_result_type") != SELF_ORIENTATION_V2_RESULT_TYPE:
        raise CurrentSelfOrientationV3Error(
            "v2 self-orientation result type is not recognized",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    if metadata.get("resolver_module") != SELF_ORIENTATION_V2_RESOLVER_MODULE:
        raise CurrentSelfOrientationV3Error(
            "v2 self-orientation resolver module is not recognized",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    if result.get("outcome") != OUTCOME_SELF_ORIENTED:
        raise CurrentSelfOrientationV3Error(
            "v2 self-orientation result is not SELF_ORIENTED",
            "NO_SELF_ORIENTATION_SOURCE_BASIS",
        )
    _validate_false_non_claims(result.get("non_claims"), "v2 self-orientation")


def _select_matching_self_orientation_v2(
    body_identity: Mapping[str, Any],
) -> tuple[Path, dict[str, Any], str]:
    body_id = _string_or_none(body_identity.get("result_id"))
    body_path = _string_or_none(body_identity.get("result_path"))
    matches: list[tuple[Path, dict[str, Any]]] = []
    malformed_match: CurrentSelfOrientationV3Error | None = None
    for path in _discover_json_files(CURRENT_SELF_ORIENTATION_V2_ROOT):
        try:
            artifact = _read_json_file(
                path,
                context="candidate current self-orientation v2 result",
                missing_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                malformed_code="SOURCE_ARTIFACT_MALFORMED",
            )
            _validate_self_orientation_v2_result(artifact)
            selected_body = _v2_body_pass_identity(artifact)
        except CurrentSelfOrientationV3Error as exc:
            malformed_match = exc
            continue
        selected_body_id = _string_or_none(selected_body.get("result_id"))
        selected_body_path = _string_or_none(selected_body.get("result_path"))
        id_matches = body_id is not None and body_id == selected_body_id
        path_matches = body_path is not None and _path_equal(body_path, selected_body_path)
        if id_matches or path_matches:
            matches.append((path, artifact))
    if not matches:
        if malformed_match is not None:
            raise CurrentSelfOrientationV3Error(
                "no self-oriented v2 result matches the selected body-pass basis",
                "NO_SELF_ORIENTATION_SOURCE_BASIS",
            )
        raise CurrentSelfOrientationV3Error(
            "no self-oriented v2 result matches the selected body-pass basis",
            "NO_SELF_ORIENTATION_SOURCE_BASIS",
        )
    path, artifact = matches[-1]
    return path, artifact, "matching_self_orientation_v2_discovery"


def _basis_from_v2(v2_result: Mapping[str, Any]) -> dict[str, Any]:
    selected = _require_mapping(
        v2_result.get("selected_orientation_inputs"),
        "selected_orientation_inputs",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    body = _require_mapping(
        selected.get("selected_body_pass_result"),
        "selected_body_pass_result",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    source = _require_mapping(
        selected.get("selected_source_surface"),
        "selected_source_surface",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    answer = selected.get("selected_current_state_answer_read_result")
    answer = answer if isinstance(answer, Mapping) else {}
    stand = selected.get("selected_current_state_what_stands_now_result")
    stand = stand if isinstance(stand, Mapping) else source
    effective = selected.get("selected_effective_references")
    effective = effective if isinstance(effective, Mapping) else {}
    basis = {
        "selected_body_pass_result_id": body.get("result_id"),
        "selected_body_pass_result_path": body.get("result_path"),
        "selected_source_surface_id": source.get("result_id"),
        "selected_source_surface_path": source.get("result_path"),
        "selected_current_state_answer_read_id": answer.get("result_id"),
        "selected_current_state_answer_read_path": answer.get("result_path"),
        "selected_what_stands_now_id": stand.get("result_id"),
        "selected_what_stands_now_path": stand.get("result_path"),
    }
    for key in EFFECTIVE_REFERENCE_KEYS:
        basis[key] = effective.get(key)
    return basis


def _basis_matches(expected: Mapping[str, Any], actual: Mapping[str, Any]) -> bool:
    for key in BASIS_LOCK_KEYS:
        expected_value = expected.get(key)
        actual_value = actual.get(key)
        if key.endswith("_path"):
            if not _path_equal(expected_value, actual_value):
                return False
        elif expected_value != actual_value:
            return False
    return True


def _selected_self_orientation_matches_v2(
    admissibility_result: Mapping[str, Any],
    v2_identity: Mapping[str, Any],
) -> bool:
    selected = admissibility_result.get("selected_self_orientation_result")
    if not isinstance(selected, Mapping):
        return False
    id_matches = selected.get("result_id") == v2_identity.get("result_id")
    path_matches = _path_equal(selected.get("result_path"), v2_identity.get("result_path"))
    outcome_matches = selected.get("outcome") == OUTCOME_SELF_ORIENTED
    return bool((id_matches or path_matches) and outcome_matches)


def _validate_reentry_admissibility_result(result: Mapping[str, Any]) -> None:
    metadata = _metadata_section(
        result,
        "current_self_orientation_reentry_admissibility_metadata",
    )
    if metadata.get("reentry_admissibility_result_type") != REENTRY_ADMISSIBILITY_RESULT_TYPE:
        raise CurrentSelfOrientationV3Error(
            "re-entry admissibility result type is not recognized",
            "REENTRY_ADMISSIBILITY_MALFORMED",
        )
    if metadata.get("resolver_module") != REENTRY_ADMISSIBILITY_RESOLVER_MODULE:
        raise CurrentSelfOrientationV3Error(
            "re-entry admissibility resolver module is not recognized",
            "REENTRY_ADMISSIBILITY_MALFORMED",
        )
    if result.get("outcome") != OUTCOME_REENTRY_ADMITTED:
        raise CurrentSelfOrientationV3Error(
            "re-entry admissibility result is not admitted",
            "REENTRY_ADMISSIBILITY_NOT_ADMITTED",
        )
    block = result.get("block")
    if not isinstance(block, Mapping) or block.get("block_code") is not None:
        raise CurrentSelfOrientationV3Error(
            "re-entry admissibility result carries a block",
            "REENTRY_ADMISSIBILITY_NOT_ADMITTED",
        )
    if not isinstance(result.get("locked_orientation_basis"), Mapping):
        raise CurrentSelfOrientationV3Error(
            "re-entry admissibility result lacks locked basis",
            "REENTRY_ADMISSIBILITY_MALFORMED",
        )
    _validate_false_non_claims(result.get("non_claims"), "re-entry admissibility")


def _select_matching_reentry_admissibility(
    v2_identity: Mapping[str, Any],
    selected_basis: Mapping[str, Any],
) -> tuple[Path, dict[str, Any], str]:
    matches: list[tuple[Path, dict[str, Any]]] = []
    for path in _discover_json_files(CURRENT_SELF_ORIENTATION_REENTRY_ADMISSIBILITY_ROOT):
        try:
            artifact = _read_json_file(
                path,
                context="candidate re-entry admissibility result",
                missing_code="REENTRY_ADMISSIBILITY_UNREADABLE",
                unreadable_code="REENTRY_ADMISSIBILITY_UNREADABLE",
                malformed_code="REENTRY_ADMISSIBILITY_MALFORMED",
            )
            _validate_reentry_admissibility_result(artifact)
        except CurrentSelfOrientationV3Error:
            continue
        locked = artifact.get("locked_orientation_basis")
        if not isinstance(locked, Mapping):
            continue
        if not _selected_self_orientation_matches_v2(artifact, v2_identity):
            continue
        if not _basis_matches(selected_basis, locked):
            continue
        matches.append((path, artifact))
    if not matches:
        raise CurrentSelfOrientationV3Error(
            "no admitted re-entry result matches the selected self-orientation basis",
            "REENTRY_ADMISSIBILITY_UNREADABLE",
        )
    path, artifact = matches[-1]
    return path, artifact, "matching_reentry_admissibility_discovery"


def _validate_reentry_receipt_result(result: Mapping[str, Any]) -> None:
    metadata = _metadata_section(result, "current_self_orientation_reentry_receipt_metadata")
    if metadata.get("reentry_receipt_result_type") != REENTRY_RECEIPT_RESULT_TYPE:
        raise CurrentSelfOrientationV3Error(
            "re-entry receipt result type is not recognized",
            "REENTRY_RECEIPT_MALFORMED",
        )
    if metadata.get("resolver_module") != REENTRY_RECEIPT_RESOLVER_MODULE:
        raise CurrentSelfOrientationV3Error(
            "re-entry receipt resolver module is not recognized",
            "REENTRY_RECEIPT_MALFORMED",
        )
    if result.get("outcome") != OUTCOME_REENTRY_RECEIVED:
        raise CurrentSelfOrientationV3Error(
            "re-entry receipt result is not received",
            "REENTRY_RECEIPT_NOT_RECEIVED",
        )
    block = result.get("block")
    if not isinstance(block, Mapping) or block.get("block_code") is not None:
        raise CurrentSelfOrientationV3Error(
            "re-entry receipt result carries a block",
            "REENTRY_RECEIPT_NOT_RECEIVED",
        )
    if not isinstance(result.get("locked_admitted_basis"), Mapping):
        raise CurrentSelfOrientationV3Error(
            "re-entry receipt result lacks locked admitted basis",
            "REENTRY_RECEIPT_MALFORMED",
        )
    if not isinstance(result.get("selected_reentry_admissibility_result"), Mapping):
        raise CurrentSelfOrientationV3Error(
            "re-entry receipt result lacks selected admissibility identity",
            "REENTRY_RECEIPT_MALFORMED",
        )
    _validate_false_non_claims(result.get("non_claims"), "re-entry receipt")


def _receipt_matches_admissibility(
    receipt_result: Mapping[str, Any],
    admissibility_identity: Mapping[str, Any],
) -> bool:
    selected = receipt_result.get("selected_reentry_admissibility_result")
    if not isinstance(selected, Mapping):
        return False
    id_matches = selected.get("result_id") == admissibility_identity.get("result_id")
    path_matches = _path_equal(selected.get("result_path"), admissibility_identity.get("result_path"))
    outcome_matches = selected.get("outcome") == OUTCOME_REENTRY_ADMITTED
    return bool((id_matches or path_matches) and outcome_matches)


def _select_matching_reentry_receipt(
    admissibility_identity: Mapping[str, Any],
    selected_basis: Mapping[str, Any],
) -> tuple[Path, dict[str, Any], str]:
    matches: list[tuple[Path, dict[str, Any]]] = []
    for path in _discover_json_files(CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_ROOT):
        try:
            artifact = _read_json_file(
                path,
                context="candidate re-entry receipt result",
                missing_code="REENTRY_RECEIPT_UNREADABLE",
                unreadable_code="REENTRY_RECEIPT_UNREADABLE",
                malformed_code="REENTRY_RECEIPT_MALFORMED",
            )
            _validate_reentry_receipt_result(artifact)
        except CurrentSelfOrientationV3Error:
            continue
        locked = artifact.get("locked_admitted_basis")
        if not isinstance(locked, Mapping):
            continue
        if not _receipt_matches_admissibility(artifact, admissibility_identity):
            continue
        if not _basis_matches(selected_basis, locked):
            continue
        matches.append((path, artifact))
    if not matches:
        raise CurrentSelfOrientationV3Error(
            "no received re-entry receipt matches the selected admissibility and basis",
            "REENTRY_RECEIPT_UNREADABLE",
        )
    path, artifact = matches[-1]
    return path, artifact, "matching_reentry_receipt_discovery"


def _validate_false_non_claims(value: Any, context: str) -> None:
    if not isinstance(value, Mapping):
        raise CurrentSelfOrientationV3Error(
            f"{context} non_claims must be an object",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    for key, item in value.items():
        if not isinstance(key, str) or item is not False:
            raise CurrentSelfOrientationV3Error(
                f"{context} non-claim is missing or flipped: {key}",
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )


def _merge_non_claims(*artifacts: Mapping[str, Any] | None) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    for artifact in artifacts:
        if not isinstance(artifact, Mapping):
            continue
        non_claims = artifact.get("non_claims")
        if not isinstance(non_claims, Mapping):
            continue
        for key, value in non_claims.items():
            if isinstance(key, str) and value is False:
                merged[key] = False
            elif isinstance(key, str):
                raise CurrentSelfOrientationV3Error(
                    f"non-claim is missing or flipped: {key}",
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )
    return merged


def _reentry_request_next_step(
    admissibility_result: Mapping[str, Any],
) -> Mapping[str, Any]:
    request = admissibility_result.get("selected_reentry_request")
    if not isinstance(request, Mapping):
        return {}
    next_step = request.get("declared_next_step")
    return next_step if isinstance(next_step, Mapping) else {}


def _receipt_summary(receipt_result: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = receipt_result.get("current_self_orientation_reentry_receipt_summary")
    return summary if isinstance(summary, Mapping) else {}


def _selected_performed_step(receipt_result: Mapping[str, Any]) -> Mapping[str, Any]:
    performed = receipt_result.get("selected_performed_step")
    return performed if isinstance(performed, Mapping) else {}


def _receipt_basis(receipt_result: Mapping[str, Any]) -> Mapping[str, Any]:
    basis = receipt_result.get("reentry_receipt_basis")
    return basis if isinstance(basis, Mapping) else {}


def _build_reentry_checks(
    v2_identity: Mapping[str, Any],
    selected_basis: Mapping[str, Any],
    admissibility_identity: Mapping[str, Any],
    admissibility_result: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
    receipt_result: Mapping[str, Any],
) -> list[dict[str, Any]]:
    receipt_summary = _receipt_summary(receipt_result)
    receipt_basis = _receipt_basis(receipt_result)
    performed = _selected_performed_step(receipt_result)
    receipt_non_claims = receipt_result.get("non_claims")
    receipt_non_claims = receipt_non_claims if isinstance(receipt_non_claims, Mapping) else {}
    checks = [
        _check(
            "reentry_admissibility_is_admitted",
            admissibility_result.get("outcome") == OUTCOME_REENTRY_ADMITTED,
            expected=OUTCOME_REENTRY_ADMITTED,
            actual=admissibility_result.get("outcome"),
            block_code="REENTRY_ADMISSIBILITY_NOT_ADMITTED",
        ),
        _check(
            "reentry_receipt_is_received",
            receipt_result.get("outcome") == OUTCOME_REENTRY_RECEIVED,
            expected=OUTCOME_REENTRY_RECEIVED,
            actual=receipt_result.get("outcome"),
            block_code="REENTRY_RECEIPT_NOT_RECEIVED",
        ),
        _check(
            "reentry_receipt_matches_selected_admissibility",
            _receipt_matches_admissibility(receipt_result, admissibility_identity),
            expected=admissibility_identity.get("result_id"),
            actual=receipt_result.get("selected_reentry_admissibility_result"),
            block_code="REENTRY_RECEIPT_DOES_NOT_MATCH_SELECTED_ADMISSIBILITY",
        ),
        _check(
            "reentry_admissibility_matches_selected_self_orientation_v2",
            _selected_self_orientation_matches_v2(admissibility_result, v2_identity),
            expected=v2_identity.get("result_id"),
            actual=admissibility_result.get("selected_self_orientation_result"),
            block_code="REENTRY_RECEIPT_DOES_NOT_MATCH_SELECTED_SELF_ORIENTATION_BASIS",
        ),
        _check(
            "reentry_admissibility_locked_basis_matches_selected_current_basis",
            _basis_matches(
                selected_basis,
                _require_mapping(
                    admissibility_result.get("locked_orientation_basis"),
                    "locked_orientation_basis",
                    "REENTRY_ADMISSIBILITY_MALFORMED",
                ),
            ),
            expected=selected_basis,
            actual=admissibility_result.get("locked_orientation_basis"),
            block_code="REENTRY_RECEIPT_DOES_NOT_MATCH_SELECTED_SELF_ORIENTATION_BASIS",
        ),
        _check(
            "reentry_receipt_locked_basis_matches_selected_current_basis",
            _basis_matches(
                selected_basis,
                _require_mapping(
                    receipt_result.get("locked_admitted_basis"),
                    "locked_admitted_basis",
                    "REENTRY_RECEIPT_MALFORMED",
                ),
            ),
            expected=selected_basis,
            actual=receipt_result.get("locked_admitted_basis"),
            block_code="REENTRY_RECEIPT_DOES_NOT_MATCH_SELECTED_SELF_ORIENTATION_BASIS",
        ),
        _check(
            "reentry_receipt_basis_lock_matched",
            receipt_summary.get("basis_lock_matched") is True,
            expected=True,
            actual=receipt_summary.get("basis_lock_matched"),
            block_code="REENTRY_RECEIPT_BASIS_LOCK_NOT_MATCHED",
        ),
        _check(
            "reentry_receipt_performed_step_correspondence_passed",
            receipt_summary.get("performed_step_correspondence_passed") is True,
            expected=True,
            actual=receipt_summary.get("performed_step_correspondence_passed"),
            block_code="REENTRY_RECEIPT_PERFORMED_STEP_CORRESPONDENCE_FAILED",
        ),
        _check(
            "reentry_receipt_scope_stayed_single_step_and_additive",
            receipt_summary.get("scope_stayed_single_step_and_additive") is True,
            expected=True,
            actual=receipt_summary.get("scope_stayed_single_step_and_additive"),
            block_code="REENTRY_RECEIPT_SCOPE_NOT_SINGLE_STEP_ADDITIVE",
        ),
        _check(
            "reentry_receipt_exhaustion_closure_passed",
            receipt_summary.get("exhaustion_closure_passed") is True
            and performed.get("admission_exhausted") in {True, None}
            and receipt_basis.get("admission_exhausted") in {True, None},
            expected=True,
            actual={
                "summary": receipt_summary.get("exhaustion_closure_passed"),
                "performed_admission_exhausted": performed.get("admission_exhausted"),
                "basis_admission_exhausted": receipt_basis.get("admission_exhausted"),
            },
            block_code="REENTRY_RECEIPT_EXHAUSTION_NOT_CLOSED",
        ),
        _check(
            "reentry_receipt_has_no_failed_checks",
            receipt_summary.get("failed_check_count") == 0,
            expected=0,
            actual=receipt_summary.get("failed_check_count"),
            block_code="REENTRY_RECEIPT_FAILED_CHECKS_PRESENT",
        ),
        _check(
            "reentry_receipt_does_not_leak_follow_on_permission",
            receipt_non_claims.get("follow_on_steps_authorized") is False
            and performed.get("follow_on_steps_authorized") in {False, None}
            and receipt_basis.get("receipt_creates_follow_on_permission") in {False, None},
            expected=False,
            actual={
                "non_claim": receipt_non_claims.get("follow_on_steps_authorized"),
                "performed": performed.get("follow_on_steps_authorized"),
                "basis": receipt_basis.get("receipt_creates_follow_on_permission"),
            },
            block_code="REENTRY_RECEIPT_FOLLOW_ON_PERMISSION_LEAK",
        ),
        _check(
            "reentry_receipt_does_not_leak_general_permission",
            receipt_non_claims.get("general_permission_created") is False
            and performed.get("general_permission_created") in {False, None},
            expected=False,
            actual={
                "non_claim": receipt_non_claims.get("general_permission_created"),
                "performed": performed.get("general_permission_created"),
            },
            block_code="REENTRY_RECEIPT_GENERAL_PERMISSION_LEAK",
        ),
        _check(
            "reentry_receipt_does_not_leak_reusable_admission",
            receipt_non_claims.get("admission_reusable") is False
            and performed.get("admission_reusable") in {False, None}
            and performed.get("reusable_permission_implied") in {False, None},
            expected=False,
            actual={
                "non_claim": receipt_non_claims.get("admission_reusable"),
                "performed": performed.get("admission_reusable"),
                "reusable_permission_implied": performed.get("reusable_permission_implied"),
            },
            block_code="REENTRY_RECEIPT_REUSABLE_ADMISSION_LEAK",
        ),
        _check(
            "reentry_surfaces_remain_non_authoritative",
            receipt_non_claims.get("reentry_admissibility_became_authority") is False
            and receipt_non_claims.get("receipt_became_authority") is False
            and receipt_basis.get("admissibility_remains_non_authoritative") in {True, None},
            expected="re-entry surfaces remain downstream posture only",
            actual={
                "reentry_admissibility_became_authority": receipt_non_claims.get(
                    "reentry_admissibility_became_authority"
                ),
                "receipt_became_authority": receipt_non_claims.get("receipt_became_authority"),
                "basis": receipt_basis.get("admissibility_remains_non_authoritative"),
            },
            block_code="REENTRY_SURFACE_TREATED_AS_AUTHORITY",
        ),
        _check(
            "closed_reentry_cycle_is_not_workflow_lane",
            receipt_non_claims.get("workflow_engine_created") is False
            and receipt_non_claims.get("roadmap_generated") is False
            and receipt_non_claims.get("reentry_cycle_became_workflow_lane") in {False, None},
            expected=False,
            actual={
                "workflow_engine_created": receipt_non_claims.get("workflow_engine_created"),
                "roadmap_generated": receipt_non_claims.get("roadmap_generated"),
                "reentry_cycle_became_workflow_lane": receipt_non_claims.get(
                    "reentry_cycle_became_workflow_lane"
                ),
            },
            block_code="REENTRY_CYCLE_TREATED_AS_WORKFLOW_LANE",
        ),
    ]
    return checks


def _selected_input_with_reentry(
    v2_selected_inputs: Mapping[str, Any],
    v2_identity: Mapping[str, Any],
    admissibility_identity: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
) -> dict[str, Any]:
    selected = copy.deepcopy(dict(v2_selected_inputs))
    selected["selected_self_orientation_v2_result"] = dict(v2_identity)
    selected["selected_reentry_admissibility_result"] = dict(admissibility_identity)
    selected["selected_reentry_receipt_result"] = dict(receipt_identity)
    selected["selection_scope"] = {
        "body_pass_anchor_required": True,
        "self_orientation_v2_is_predecessor_recognition": True,
        "reentry_surfaces_are_downstream_only": True,
        "latest_file_recency_refused": True,
        "repo_wide_authority_scan_performed": False,
    }
    return selected


def _recognized_reentry_surfaces(
    admissibility_identity: Mapping[str, Any],
    admissibility_result: Mapping[str, Any],
    receipt_identity: Mapping[str, Any],
    receipt_result: Mapping[str, Any],
) -> dict[str, Any]:
    receipt_summary = _receipt_summary(receipt_result)
    performed = _selected_performed_step(receipt_result)
    receipt_non_claims = receipt_result.get("non_claims")
    receipt_non_claims = receipt_non_claims if isinstance(receipt_non_claims, Mapping) else {}
    return {
        "recognition_posture": "downstream_closed_reentry_cycle_only",
        "selected_reentry_admissibility_result": dict(admissibility_identity),
        "selected_reentry_receipt_result": dict(receipt_identity),
        "admitted_next_step": dict(_reentry_request_next_step(admissibility_result)),
        "performed_step": dict(performed),
        "closure_posture": {
            "basis_lock_matched": receipt_summary.get("basis_lock_matched"),
            "performed_step_correspondence_passed": receipt_summary.get(
                "performed_step_correspondence_passed"
            ),
            "scope_stayed_single_step_and_additive": receipt_summary.get(
                "scope_stayed_single_step_and_additive"
            ),
            "exhaustion_closure_passed": receipt_summary.get("exhaustion_closure_passed"),
            "failed_check_count": receipt_summary.get("failed_check_count"),
            "follow_on_steps_authorized": receipt_non_claims.get(
                "follow_on_steps_authorized",
                False,
            ),
            "general_permission_created": receipt_non_claims.get(
                "general_permission_created",
                False,
            ),
            "admission_reusable": receipt_non_claims.get("admission_reusable", False),
            "receipt_became_authority": receipt_non_claims.get(
                "receipt_became_authority",
                False,
            ),
            "reentry_admissibility_became_authority": receipt_non_claims.get(
                "reentry_admissibility_became_authority",
                False,
            ),
            "workflow_lane_created": receipt_non_claims.get(
                "reentry_cycle_became_workflow_lane",
                False,
            ),
        },
    }


def _result_id(selected_inputs: Mapping[str, Any], outcome: str) -> str:
    selected_body = selected_inputs.get("selected_body_pass_result")
    body_id = (
        selected_body.get("result_id")
        if isinstance(selected_body, Mapping)
        else None
    )
    base = _string_or_none(body_id) or "no_selected_body_pass_result"
    suffix = "current_self_orientation_v3_self_oriented"
    if outcome == OUTCOME_BLOCKED:
        suffix = "current_self_orientation_v3_blocked"
    return f"{base}__{suffix}"


def _metadata(selected_inputs: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    return {
        "self_orientation_result_id": _result_id(selected_inputs, outcome),
        "self_orientation_result_type": CURRENT_SELF_ORIENTATION_RESULT_TYPE,
        "self_orientation_result_version": CURRENT_SELF_ORIENTATION_RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
        "successor_of_module": SUCCESSOR_OF_MODULE,
    }


def _bounded_section(value: Any, wrapper_key: str) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    if value in (None, [], ()):
        return {}
    return {wrapper_key: copy.deepcopy(value)}


def _empty_selected_inputs() -> dict[str, Any]:
    return {
        "selected_body_pass_result": {},
        "selected_self_orientation_v2_result": {},
        "selected_reentry_admissibility_result": {},
        "selected_reentry_receipt_result": {},
        "selection_scope": {
            "body_pass_anchor_required": True,
            "self_orientation_v2_is_predecessor_recognition": True,
            "reentry_surfaces_are_downstream_only": True,
            "latest_file_recency_refused": True,
            "repo_wide_authority_scan_performed": False,
        },
    }


def _build_result(
    *,
    selected_inputs: Mapping[str, Any],
    recognized_current_executable_core_line: Mapping[str, Any] | None = None,
    recognized_governing_effective_basis: Mapping[str, Any] | None = None,
    recognized_current_state_surfaces: Mapping[str, Any] | None = None,
    recognized_continuity_surfaces: Mapping[str, Any] | None = None,
    recognized_derivative_surfaces: Mapping[str, Any] | None = None,
    recognized_operator_facing_surfaces: Mapping[str, Any] | None = None,
    recognized_reentry_surfaces: Mapping[str, Any] | None = None,
    recognized_open_surfaces: Mapping[str, Any] | None = None,
    recognized_blocked_or_refused_surfaces: Mapping[str, Any] | None = None,
    recognized_touch_admissibility_surfaces: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    outcome: str,
    block_code: str | None,
    block_detail: str | None,
    self_orientation_basis: Mapping[str, Any] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    result = {
        "current_self_orientation_v3_metadata": _metadata(selected_inputs, outcome),
        "selected_orientation_inputs": copy.deepcopy(dict(selected_inputs)),
        "recognized_current_executable_core_line": _bounded_section(
            recognized_current_executable_core_line,
            "recognized_current_executable_core_line",
        ),
        "recognized_governing_effective_basis": _bounded_section(
            recognized_governing_effective_basis,
            "recognized_governing_effective_basis",
        ),
        "recognized_current_state_surfaces": _bounded_section(
            recognized_current_state_surfaces,
            "recognized_current_state_surfaces",
        ),
        "recognized_continuity_surfaces": _bounded_section(
            recognized_continuity_surfaces,
            "recognized_continuity_surfaces",
        ),
        "recognized_derivative_surfaces": _bounded_section(
            recognized_derivative_surfaces,
            "recognized_derivative_surfaces",
        ),
        "recognized_operator_facing_surfaces": _bounded_section(
            recognized_operator_facing_surfaces,
            "recognized_operator_facing_surfaces",
        ),
        "recognized_reentry_surfaces": _bounded_section(
            recognized_reentry_surfaces,
            "recognized_reentry_surfaces",
        ),
        "recognized_open_surfaces": _bounded_section(
            recognized_open_surfaces,
            "recognized_open_surfaces",
        ),
        "recognized_blocked_or_refused_surfaces": _bounded_section(
            recognized_blocked_or_refused_surfaces,
            "recognized_blocked_or_refused_surfaces",
        ),
        "recognized_touch_admissibility_surfaces": _bounded_section(
            recognized_touch_admissibility_surfaces,
            "recognized_touch_admissibility_surfaces",
        ),
        "bounded_correspondence_checks": [dict(check) for check in (checks or [])],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "self_orientation_basis": dict(self_orientation_basis or {}),
        "current_self_orientation_summary": {},
        "non_claims": dict(non_claims or NON_CLAIM_DEFAULTS),
    }
    result["current_self_orientation_summary"] = build_current_self_orientation_summary(result)
    return result


def _blocked_result(
    *,
    block_code: str,
    block_detail: str | None = None,
    selected_inputs: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    v2_result: Mapping[str, Any] | None = None,
    recognized_reentry_surfaces: Mapping[str, Any] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    selected = selected_inputs if isinstance(selected_inputs, Mapping) else _empty_selected_inputs()
    return _build_result(
        selected_inputs=selected,
        recognized_current_executable_core_line=(
            v2_result.get("recognized_current_executable_core_line")
            if isinstance(v2_result, Mapping)
            else {}
        ),
        recognized_governing_effective_basis=(
            v2_result.get("recognized_governing_effective_basis")
            if isinstance(v2_result, Mapping)
            else {}
        ),
        recognized_current_state_surfaces=(
            v2_result.get("recognized_current_state_surfaces")
            if isinstance(v2_result, Mapping)
            else {}
        ),
        recognized_continuity_surfaces=(
            v2_result.get("recognized_continuity_surfaces")
            if isinstance(v2_result, Mapping)
            else {}
        ),
        recognized_derivative_surfaces=(
            v2_result.get("recognized_derivative_surfaces")
            if isinstance(v2_result, Mapping)
            else {}
        ),
        recognized_operator_facing_surfaces=(
            v2_result.get("recognized_operator_facing_surfaces")
            if isinstance(v2_result, Mapping)
            else {}
        ),
        recognized_reentry_surfaces=recognized_reentry_surfaces or {},
        recognized_open_surfaces=(
            v2_result.get("recognized_open_surfaces")
            if isinstance(v2_result, Mapping)
            else {}
        ),
        recognized_blocked_or_refused_surfaces=(
            v2_result.get("recognized_blocked_or_refused_surfaces")
            if isinstance(v2_result, Mapping)
            else {}
        ),
        recognized_touch_admissibility_surfaces=(
            v2_result.get("recognized_touch_admissibility_surfaces")
            if isinstance(v2_result, Mapping)
            else {}
        ),
        checks=checks or [],
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_detail=block_detail,
        self_orientation_basis={
            "basis_kind": "blocked_v3_self_orientation_preserving_selected_basis",
            "reentry_surfaces_remain_downstream": True,
            "self_orientation_creates_authority": False,
            "receipt_creates_permission": False,
        },
        non_claims=non_claims or NON_CLAIM_DEFAULTS,
    )


def _resolve(
    body_pass_result: Mapping[str, Any] | None = None,
    body_pass_result_path: Path | str | None = None,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    body_path, body_artifact, body_selection_mode = _select_body_pass(
        body_pass_result,
        body_pass_result_path,
    )
    body_identity = _body_pass_identity(body_artifact, body_path, body_selection_mode)
    selected_inputs = _empty_selected_inputs()
    selected_inputs["selected_body_pass_result"] = body_identity

    v2_path, v2_result, v2_selection_mode = _select_matching_self_orientation_v2(body_identity)
    v2_identity = _self_orientation_v2_identity(v2_result, v2_path, v2_selection_mode)
    selected_basis = _basis_from_v2(v2_result)
    selected_inputs = _selected_input_with_reentry(
        _require_mapping(
            v2_result.get("selected_orientation_inputs"),
            "selected_orientation_inputs",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        v2_identity,
        {},
        {},
    )

    admissibility_path, admissibility_result, admissibility_selection_mode = (
        _select_matching_reentry_admissibility(v2_identity, selected_basis)
    )
    admissibility_identity = _reentry_admissibility_identity(
        admissibility_result,
        admissibility_path,
        admissibility_selection_mode,
    )
    selected_inputs["selected_reentry_admissibility_result"] = admissibility_identity

    receipt_path, receipt_result, receipt_selection_mode = _select_matching_reentry_receipt(
        admissibility_identity,
        selected_basis,
    )
    receipt_identity = _reentry_receipt_identity(
        receipt_result,
        receipt_path,
        receipt_selection_mode,
    )
    selected_inputs["selected_reentry_receipt_result"] = receipt_identity

    checks.extend(
        [
            _check(
                "v2_self_orientation_is_self_oriented",
                v2_result.get("outcome") == OUTCOME_SELF_ORIENTED,
                expected=OUTCOME_SELF_ORIENTED,
                actual=v2_result.get("outcome"),
                block_code="NO_SELF_ORIENTATION_SOURCE_BASIS",
            ),
            _check(
                "v2_selected_body_pass_matches_anchor",
                (
                    body_identity.get("result_id")
                    == selected_basis.get("selected_body_pass_result_id")
                )
                or _path_equal(
                    body_identity.get("result_path"),
                    selected_basis.get("selected_body_pass_result_path"),
                ),
                expected=body_identity,
                actual={
                    "selected_body_pass_result_id": selected_basis.get(
                        "selected_body_pass_result_id"
                    ),
                    "selected_body_pass_result_path": selected_basis.get(
                        "selected_body_pass_result_path"
                    ),
                },
                block_code="CORRESPONDENCE_CHECK_FAILED",
            ),
            _check(
                "reentry_surfaces_do_not_determine_current_governing_basis",
                True,
                expected="current/effective/current-state surfaces remain upstream",
                actual="re-entry surfaces recognized downstream only",
                block_code="REENTRY_SURFACE_TREATED_AS_AUTHORITY",
            ),
        ]
    )
    checks.extend(
        _build_reentry_checks(
            v2_identity,
            selected_basis,
            admissibility_identity,
            admissibility_result,
            receipt_identity,
            receipt_result,
        )
    )

    failed = _first_failed(checks)
    non_claims = _merge_non_claims(v2_result, admissibility_result, receipt_result)
    reentry_surfaces = _recognized_reentry_surfaces(
        admissibility_identity,
        admissibility_result,
        receipt_identity,
        receipt_result,
    )
    if failed is not None:
        return _blocked_result(
            block_code=_string_or_none(failed.get("block_code")) or "CORRESPONDENCE_CHECK_FAILED",
            block_detail=f"failed check: {failed.get('check_name')}",
            selected_inputs=selected_inputs,
            checks=checks,
            v2_result=v2_result,
            recognized_reentry_surfaces=reentry_surfaces,
            non_claims=non_claims,
        )

    return _build_result(
        selected_inputs=selected_inputs,
        recognized_current_executable_core_line=v2_result.get(
            "recognized_current_executable_core_line"
        ),
        recognized_governing_effective_basis=v2_result.get(
            "recognized_governing_effective_basis"
        ),
        recognized_current_state_surfaces=v2_result.get("recognized_current_state_surfaces"),
        recognized_continuity_surfaces=v2_result.get("recognized_continuity_surfaces"),
        recognized_derivative_surfaces=v2_result.get("recognized_derivative_surfaces"),
        recognized_operator_facing_surfaces=v2_result.get(
            "recognized_operator_facing_surfaces"
        ),
        recognized_reentry_surfaces=reentry_surfaces,
        recognized_open_surfaces=v2_result.get("recognized_open_surfaces"),
        recognized_blocked_or_refused_surfaces=v2_result.get(
            "recognized_blocked_or_refused_surfaces"
        ),
        recognized_touch_admissibility_surfaces=v2_result.get(
            "recognized_touch_admissibility_surfaces"
        ),
        checks=[
            *(check for check in v2_result.get("bounded_correspondence_checks", []) if isinstance(check, Mapping)),
            *checks,
        ],
        outcome=OUTCOME_SELF_ORIENTED,
        block_code=None,
        block_detail=None,
        self_orientation_basis={
            "basis_kind": "v2_self_orientation_plus_closed_reentry_cycle",
            "selected_self_orientation_v2_result_id": v2_identity.get("result_id"),
            "selected_self_orientation_v2_result_path": v2_identity.get("result_path"),
            "selected_body_pass_result_id": selected_basis.get("selected_body_pass_result_id"),
            "selected_source_surface_id": selected_basis.get("selected_source_surface_id"),
            "selected_current_state_answer_read_id": selected_basis.get(
                "selected_current_state_answer_read_id"
            ),
            "selected_what_stands_now_id": selected_basis.get("selected_what_stands_now_id"),
            "selected_reentry_admissibility_result_id": admissibility_identity.get("result_id"),
            "selected_reentry_receipt_result_id": receipt_identity.get("result_id"),
            "reentry_cycle_recognized_as_downstream_posture": True,
            "receipt_permission_exhausted": True,
            "follow_on_permission_created": False,
            "workflow_lane_created": False,
            "self_orientation_creates_authority": False,
        },
        non_claims=non_claims,
    )


def resolve_current_self_orientation(
    body_pass_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded v3 self-orientation result."""

    try:
        return _resolve(body_pass_result=body_pass_result)
    except CurrentSelfOrientationV3Error as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            selected_inputs=exc.selected_inputs,
            checks=exc.checks,
        )


def resolve_current_self_orientation_from_path(
    body_pass_result_path: Path | str,
) -> dict[str, Any]:
    """Resolve one bounded v3 self-orientation result from a body-pass path."""

    selected_inputs = _empty_selected_inputs()
    selected_inputs["selected_body_pass_result"] = {
        "result_path": _display_path(body_pass_result_path),
        "selection_mode": "explicit_body_pass_result_path",
    }
    try:
        return _resolve(body_pass_result_path=body_pass_result_path)
    except CurrentSelfOrientationV3Error as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            selected_inputs=exc.selected_inputs or selected_inputs,
            checks=exc.checks,
        )


def _summary_bool(value: Any) -> bool:
    return isinstance(value, Mapping) and bool(value)


def _all_checks_passed(checks: Sequence[Any]) -> bool:
    return bool(checks) and all(
        isinstance(check, Mapping) and check.get("passed") is True for check in checks
    )


def build_current_self_orientation_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a bounded v3 self-orientation summary."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationV3Error(
            "current self-orientation result must be an object",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    selected = result.get("selected_orientation_inputs")
    selected = selected if isinstance(selected, Mapping) else {}
    body = selected.get("selected_body_pass_result")
    body = body if isinstance(body, Mapping) else {}
    source = selected.get("selected_source_surface")
    source = source if isinstance(source, Mapping) else {}
    v2 = selected.get("selected_self_orientation_v2_result")
    v2 = v2 if isinstance(v2, Mapping) else {}
    admission = selected.get("selected_reentry_admissibility_result")
    admission = admission if isinstance(admission, Mapping) else {}
    receipt = selected.get("selected_reentry_receipt_result")
    receipt = receipt if isinstance(receipt, Mapping) else {}
    reentry = result.get("recognized_reentry_surfaces")
    reentry = reentry if isinstance(reentry, Mapping) else {}
    closure = reentry.get("closure_posture")
    closure = closure if isinstance(closure, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    checks = result.get("bounded_correspondence_checks")
    checks = checks if isinstance(checks, list) else []
    non_claims = result.get("non_claims")
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_body_pass_result_id": body.get("result_id"),
        "selected_source_surface_id": source.get("result_id"),
        "selected_self_orientation_v2_result_id": v2.get("result_id"),
        "selected_reentry_admissibility_result_id": admission.get("result_id"),
        "selected_reentry_receipt_result_id": receipt.get("result_id"),
        "current_executable_core_line_recognized": _summary_bool(
            result.get("recognized_current_executable_core_line")
        ),
        "governing_effective_basis_recognized": _summary_bool(
            result.get("recognized_governing_effective_basis")
        ),
        "continuity_surfaces_recognized": _summary_bool(
            result.get("recognized_continuity_surfaces")
        ),
        "derivative_surfaces_recognized": _summary_bool(
            result.get("recognized_derivative_surfaces")
        ),
        "operator_surfaces_recognized": _summary_bool(
            result.get("recognized_operator_facing_surfaces")
        ),
        "reentry_surfaces_recognized": _summary_bool(reentry),
        "reentry_receipt_received": receipt.get("outcome") == OUTCOME_REENTRY_RECEIVED,
        "reentry_receipt_exhaustion_closure_passed": closure.get(
            "exhaustion_closure_passed"
        )
        is True,
        "admission_remains_non_reusable": closure.get("admission_reusable") is False,
        "follow_on_authorization_remains_false": closure.get(
            "follow_on_steps_authorized"
        )
        is False,
        "correspondence_checks_passed": _all_checks_passed(checks),
        "non_claims": {
            key: non_claims.get(key)
            for key in (
                "authority_created",
                "continuity_completed",
                "final_governance_completed",
                "final_system_identity_completed",
                "standing_upgraded",
                "source_replaced",
                "derivative_outputs_upgraded_to_source",
                "operator_outputs_upgraded_to_source",
                "general_permission_created",
                "follow_on_steps_authorized",
                "admission_reusable",
                "self_orientation_became_authority",
                "reentry_admissibility_became_authority",
                "receipt_became_authority",
                "reentry_cycle_became_workflow_lane",
                "latest_file_currentness",
                "recency_fraud",
                "mutation_performed",
                "replay_performed",
                "merge_performed",
                "roadmap_generated",
                "workflow_engine_created",
            )
            if key in non_claims
        },
    }


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = CURRENT_SELF_ORIENTATION_V3_ROOT,
) -> Path:
    selected = result.get("selected_orientation_inputs")
    selected = selected if isinstance(selected, Mapping) else {}
    body = selected.get("selected_body_pass_result")
    body = body if isinstance(body, Mapping) else {}
    stem = _safe_filename_part(body.get("result_id"))
    resolved_root = _repo_path(root)
    candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise CurrentSelfOrientationV3Error(
        "no bounded current self-orientation v3 filename is available",
        "SOURCE_ARTIFACT_MALFORMED",
    )


def write_current_self_orientation_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive v3 self-orientation JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationV3Error(
            "current self-orientation result must be an object",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"current self-orientation v3 result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
