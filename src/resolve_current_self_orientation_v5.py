"""Resolve bounded current self-orientation with body-signal scope posture.

This successor preserves the v4 self-orientation model and adds one narrow
post-signal-scope surface: body-signal scope is recognized only as downstream
applicability-containment posture.

The resolver does not replay the host, merge preserved runs, mutate upstream
artifacts, create authority, create permission, infer currentness by recency,
establish signal presence, meet a threshold, create truth, use or route a
signal, create workflow machinery, or create a body relevance medium.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CurrentSelfOrientationV5Error(RuntimeError):
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
CURRENT_SELF_ORIENTATION_V3_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v3"
)
CURRENT_SELF_ORIENTATION_V4_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v4"
)
CURRENT_SELF_ORIENTATION_REENTRY_ADMISSIBILITY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_current_self_orientation_reentry_admissibility"
)
CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_current_self_orientation_reentry_receipt"
)
BODY_SIGNAL_RECOGNITION_V2_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_body_signal_recognition_v2"
)
BODY_SIGNAL_ACCEPTANCE_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_body_signal_acceptance"
)
BODY_SIGNAL_SCOPE_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_body_signal_scope"
)
CURRENT_SELF_ORIENTATION_V5_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v5"
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
    "artifacts/integrity_host_v0_min_coexistence_current_state_touch_permissions"
)
CONTINUITY_TRANSFER_UNIT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_continuity_transfer_units"
)
CONTINUITY_TRANSFER_RECEIPT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_continuity_transfer_receipts"
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
    "artifacts/openai_api_derivative_vessel__bounded_current_state_read_v3"
)
OPERATOR_TERMINAL_BRIEF_ROOT = Path(
    "artifacts/operator_facing_terminal_brief__bounded_current_state_read"
)

RESOLVER_MODULE = "resolve_current_self_orientation_v5"
SUCCESSOR_OF_MODULE = "resolve_current_self_orientation_v4"
CURRENT_SELF_ORIENTATION_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V5_RESULT"
)
CURRENT_SELF_ORIENTATION_RESULT_VERSION = "0.5.0"
DEFAULT_RESULT_STEM = "current_self_orientation_v5_result"

SELF_ORIENTATION_V3_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V3_RESULT"
)
SELF_ORIENTATION_V3_RESOLVER_MODULE = "resolve_current_self_orientation_v3"
SELF_ORIENTATION_V4_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V4_RESULT"
)
SELF_ORIENTATION_V4_RESOLVER_MODULE = "resolve_current_self_orientation_v4"
BODY_SIGNAL_RECOGNITION_V2_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_RECOGNITION_V2_RESULT"
)
BODY_SIGNAL_RECOGNITION_V2_RESOLVER_MODULE = "resolve_body_signal_recognition_v2"
BODY_SIGNAL_ACCEPTANCE_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_ACCEPTANCE_RESULT"
)
BODY_SIGNAL_ACCEPTANCE_RESOLVER_MODULE = "resolve_body_signal_acceptance"
BODY_SIGNAL_SCOPE_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_SCOPE_RESULT"
)
BODY_SIGNAL_SCOPE_RESOLVER_MODULE = "resolve_body_signal_scope"

OUTCOME_SELF_ORIENTED = "SELF_ORIENTED"
OUTCOME_BLOCKED = "BLOCKED"
OUTCOME_BODY_PASS_CONFIRMED = "V0_BODY_PASS_CONFIRMED"
OUTCOME_SIGNAL_RECOGNIZED = "SIGNAL_RECOGNIZED"
OUTCOME_SIGNAL_ACCEPTED = "SIGNAL_ACCEPTED"
OUTCOME_SIGNAL_SCOPED = "SIGNAL_SCOPED"

SIGNAL_CATEGORY_BODY_PASS = "BODY_PASS_SIGNAL"
BODY_PASS_RESULT_FAMILY = "v0_body_pass_result"
ACCEPTANCE_MATTER_ID = "current_signal_recognition_standing"
SCOPE_ID = "current_signal_recognition_standing__body_pass_signal_nonoperative_posture_scope"

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
        "The selected re-entry admissibility result is not admitted."
    ),
    "REENTRY_RECEIPT_UNREADABLE": (
        "The selected re-entry receipt result could not be read."
    ),
    "REENTRY_RECEIPT_MALFORMED": (
        "The selected re-entry receipt result is malformed."
    ),
    "REENTRY_RECEIPT_NOT_RECEIVED": (
        "The selected re-entry receipt result is not received."
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
    "BODY_SIGNAL_RECOGNITION_UNREADABLE": (
        "The selected body-signal recognition result could not be read."
    ),
    "BODY_SIGNAL_RECOGNITION_MALFORMED": (
        "The selected body-signal recognition result is malformed."
    ),
    "BODY_SIGNAL_RECOGNITION_NOT_RECOGNIZED": (
        "The selected body-signal recognition result is not recognized."
    ),
    "BODY_SIGNAL_RECOGNITION_CATEGORY_MISMATCH": (
        "The body-signal recognition category does not match the selected posture."
    ),
    "BODY_SIGNAL_RECOGNITION_SOURCE_FAMILY_MISMATCH": (
        "The body-signal recognition source family does not match the selected body pass."
    ),
    "BODY_SIGNAL_BLOCKED_PERMISSION_REFUSAL_NOT_VISIBLE": (
        "A blocked false permission-shaped body signal is not visible where selected."
    ),
    "BODY_SIGNAL_ACCEPTANCE_UNREADABLE": (
        "The selected body-signal acceptance result could not be read."
    ),
    "BODY_SIGNAL_ACCEPTANCE_MALFORMED": (
        "The selected body-signal acceptance result is malformed."
    ),
    "BODY_SIGNAL_ACCEPTANCE_NOT_ACCEPTED": (
        "The selected body-signal acceptance result is not accepted."
    ),
    "BODY_SIGNAL_ACCEPTANCE_DOES_NOT_MATCH_SELECTED_RECOGNITION": (
        "The body-signal acceptance result does not match the selected recognition result."
    ),
    "BODY_SIGNAL_ACCEPTANCE_MATTER_MISMATCH": (
        "The body-signal acceptance matter is not current signal-recognition standing."
    ),
    "BODY_SIGNAL_ACCEPTANCE_SCOPE_COLLAPSE": (
        "The accepted body signal was treated as scoped or present."
    ),
    "BODY_SIGNAL_ACCEPTANCE_TRUTH_COLLAPSE": (
        "The accepted body signal was treated as truth or threshold."
    ),
    "BODY_SIGNAL_ACCEPTANCE_ACTION_PERMISSION_LEAK": (
        "The accepted body signal leaked action permission."
    ),
    "BODY_SIGNAL_ACCEPTANCE_FOLLOW_ON_PERMISSION_LEAK": (
        "The accepted body signal leaked follow-on permission."
    ),
    "BODY_SIGNAL_ACCEPTANCE_ROUTING_LEAK": (
        "The accepted body signal leaked routing."
    ),
    "BODY_SIGNAL_ACCEPTANCE_WORKFLOW_LEAK": (
        "The accepted body signal leaked workflow."
    ),
    "BODY_SIGNAL_ACCEPTANCE_BODY_RELEVANCE_MEDIUM_LEAK": (
        "The accepted body signal leaked body relevance medium posture."
    ),
    "BODY_SIGNAL_SURFACE_TREATED_AS_AUTHORITY": (
        "A body-signal surface was treated as authority."
    ),
    "BODY_SIGNAL_SURFACE_TREATED_AS_CURRENT_OR_GOVERNING_BASIS": (
        "A body-signal surface was treated as current or governing basis."
    ),
    "BODY_SIGNAL_LINE_TREATED_AS_ACTION_OR_CONTINUATION": (
        "The body-signal line was treated as action or continuation."
    ),
    "BODY_SIGNAL_SCOPE_UNREADABLE": (
        "The selected body-signal scope result could not be read."
    ),
    "BODY_SIGNAL_SCOPE_MALFORMED": (
        "The selected body-signal scope result is malformed."
    ),
    "BODY_SIGNAL_SCOPE_NOT_SCOPED": (
        "The selected body-signal scope result is not scoped."
    ),
    "BODY_SIGNAL_SCOPE_DOES_NOT_MATCH_SELECTED_ACCEPTANCE": (
        "The body-signal scope result does not match the selected acceptance result."
    ),
    "BODY_SIGNAL_SCOPE_DOES_NOT_MATCH_SELECTED_RECOGNITION": (
        "The body-signal scope result does not match the selected recognition result."
    ),
    "BODY_SIGNAL_SCOPE_DECLARED_SCOPE_MISMATCH": (
        "The body-signal scope declaration is not the supported non-operative posture scope."
    ),
    "BODY_SIGNAL_SCOPE_ACCEPTED_MATTER_MISMATCH": (
        "The body-signal scope accepted matter is not current signal-recognition standing."
    ),
    "BODY_SIGNAL_SCOPE_PRESENCE_COLLAPSE": (
        "The scoped body signal was treated as present."
    ),
    "BODY_SIGNAL_SCOPE_THRESHOLD_COLLAPSE": (
        "The scoped body signal was treated as threshold-met."
    ),
    "BODY_SIGNAL_SCOPE_TRUTH_COLLAPSE": (
        "The scoped body signal was treated as truth."
    ),
    "BODY_SIGNAL_SCOPE_ACTION_PERMISSION_LEAK": (
        "The scoped body signal leaked action permission."
    ),
    "BODY_SIGNAL_SCOPE_FOLLOW_ON_PERMISSION_LEAK": (
        "The scoped body signal leaked follow-on permission."
    ),
    "BODY_SIGNAL_SCOPE_ROUTING_LEAK": (
        "The scoped body signal leaked routing."
    ),
    "BODY_SIGNAL_SCOPE_WORKFLOW_LEAK": (
        "The scoped body signal leaked workflow."
    ),
    "BODY_SIGNAL_SCOPE_BODY_RELEVANCE_MEDIUM_LEAK": (
        "The scoped body signal leaked body relevance medium posture."
    ),
    "BODY_SIGNAL_SCOPE_APPLIED_OUTSIDE_DECLARED_SCOPE": (
        "The scoped body signal applied outside the declared scope."
    ),
    "BODY_SIGNAL_SCOPE_TREATED_AS_AUTHORITY": (
        "A body-signal scope surface was treated as authority."
    ),
    "BODY_SIGNAL_SCOPE_TREATED_AS_CURRENT_OR_GOVERNING_BASIS": (
        "A body-signal scope surface was treated as current or governing basis."
    ),
}

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
    "signal_recognition_became_authority": False,
    "signal_acceptance_became_authority": False,
    "signal_scope_became_authority": False,
    "signal_surface_became_current_or_governing_basis": False,
    "recognized_signal_became_permission": False,
    "accepted_signal_became_permission": False,
    "accepted_signal_became_scope": False,
    "accepted_signal_became_presence": False,
    "accepted_signal_became_threshold": False,
    "accepted_signal_became_truth": False,
    "accepted_signal_became_action": False,
    "accepted_signal_became_routing": False,
    "accepted_signal_became_workflow": False,
    "accepted_signal_became_body_relevance_medium": False,
    "scoped_signal_became_permission": False,
    "scoped_signal_became_presence": False,
    "scoped_signal_became_threshold": False,
    "scoped_signal_became_truth": False,
    "scoped_signal_became_action": False,
    "scoped_signal_became_routing": False,
    "scoped_signal_became_workflow": False,
    "scoped_signal_became_body_relevance_medium": False,
    "scoped_signal_applied_outside_declared_scope": False,
    "body_signal_line_became_action_or_continuation": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
    "roadmap_generated": False,
    "next_organ_self_generated": False,
    "workflow_engine_created": False,
    "event_bus_created": False,
    "signal_router_created": False,
    "body_relevance_medium_created": False,
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
        raise CurrentSelfOrientationV5Error(f"{context} must be an object", block_code)
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
        raise CurrentSelfOrientationV5Error(
            f"{context} not found: {resolved}",
            missing_code,
        ) from exc
    except OSError as exc:
        raise CurrentSelfOrientationV5Error(
            f"{context} is unreadable: {resolved}",
            unreadable_code,
        ) from exc
    except json.JSONDecodeError as exc:
        raise CurrentSelfOrientationV5Error(
            f"{context} is malformed JSON: {resolved}",
            malformed_code,
        ) from exc
    if not isinstance(value, dict):
        raise CurrentSelfOrientationV5Error(
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


def _path_equal(left: Any, right: Any) -> bool:
    left_text = _string_or_none(left)
    right_text = _string_or_none(right)
    if left_text is None or right_text is None:
        return False
    return left_text == right_text or _display_path(left_text) == _display_path(right_text)


def _loose_equal(left: Any, right: Any) -> bool:
    left_text = _string_or_none(left)
    right_text = _string_or_none(right)
    if left_text is None or right_text is None:
        return False
    return left_text == right_text


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
        result_family=BODY_PASS_RESULT_FAMILY,
    )


def _self_orientation_v4_identity(
    result: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _metadata_section(result, "current_self_orientation_v4_metadata")
    return _identity(
        result_id=metadata.get("self_orientation_result_id"),
        result_path=path,
        result_type=metadata.get("self_orientation_result_type"),
        result_version=metadata.get("self_orientation_result_version"),
        resolver_module=metadata.get("resolver_module"),
        outcome=result.get("outcome"),
        selection_mode=selection_mode,
        result_family="current_self_orientation_v4_result",
    )


def _body_signal_recognition_identity(
    result: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _metadata_section(result, "body_signal_recognition_v2_metadata")
    recognized = result.get("recognized_signal")
    recognized = recognized if isinstance(recognized, Mapping) else {}
    basis = result.get("body_signal_recognition_basis")
    basis = basis if isinstance(basis, Mapping) else {}
    source = basis.get("selected_source_artifact")
    source = source if isinstance(source, Mapping) else {}
    return {
        **_identity(
            result_id=metadata.get("body_signal_recognition_result_id"),
            result_path=path,
            result_type=metadata.get("body_signal_recognition_result_type"),
            result_version=metadata.get("body_signal_recognition_result_version"),
            resolver_module=metadata.get("resolver_module"),
            outcome=result.get("outcome"),
            selection_mode=selection_mode,
            result_family="body_signal_recognition_v2_result",
        ),
        "recognized_signal_id": recognized.get("recognized_signal_id"),
        "recognized_signal_category": recognized.get("signal_category")
        or basis.get("signal_category"),
        "recognized_source_artifact_id": recognized.get("source_artifact_id")
        or source.get("source_artifact_id"),
        "recognized_source_artifact_path": _display_path(
            recognized.get("source_artifact_path") or source.get("source_artifact_path")
        ),
        "recognized_source_artifact_family": recognized.get("source_artifact_family")
        or source.get("source_artifact_family"),
        "recognized_source_artifact_outcome": recognized.get("source_artifact_outcome")
        or source.get("source_artifact_outcome"),
    }


def _body_signal_acceptance_identity(
    result: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _metadata_section(result, "body_signal_acceptance_metadata")
    accepted = result.get("accepted_signal")
    accepted = accepted if isinstance(accepted, Mapping) else {}
    matter = result.get("declared_matter")
    matter = matter if isinstance(matter, Mapping) else {}
    return {
        **_identity(
            result_id=metadata.get("body_signal_acceptance_result_id"),
            result_path=path,
            result_type=metadata.get("body_signal_acceptance_result_type"),
            result_version=metadata.get("body_signal_acceptance_result_version"),
            resolver_module=metadata.get("resolver_module"),
            outcome=result.get("outcome"),
            selection_mode=selection_mode,
            result_family="body_signal_acceptance_result",
        ),
        "accepted_signal_id": accepted.get("accepted_signal_id"),
        "accepted_signal_category": accepted.get("accepted_signal_category"),
        "selected_signal_recognition_result_id": accepted.get(
            "selected_signal_recognition_result_id"
        ),
        "selected_signal_recognition_result_path": _display_path(
            accepted.get("selected_signal_recognition_result_path")
        ),
        "declared_matter_id": accepted.get("declared_matter_id")
        or matter.get("matter_id"),
        "declared_matter_family": accepted.get("declared_matter_family")
        or matter.get("matter_family"),
        "declared_matter_kind": accepted.get("declared_matter_kind")
        or matter.get("matter_kind"),
    }


def _body_signal_scope_identity(
    result: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _metadata_section(result, "body_signal_scope_metadata")
    scoped = result.get("scoped_signal")
    scoped = scoped if isinstance(scoped, Mapping) else {}
    selected_acceptance = result.get("selected_signal_acceptance_result")
    selected_acceptance = (
        selected_acceptance if isinstance(selected_acceptance, Mapping) else {}
    )
    declared_scope = result.get("declared_scope")
    declared_scope = declared_scope if isinstance(declared_scope, Mapping) else {}
    return {
        **_identity(
            result_id=metadata.get("body_signal_scope_result_id"),
            result_path=path,
            result_type=metadata.get("body_signal_scope_result_type"),
            result_version=metadata.get("body_signal_scope_result_version"),
            resolver_module=metadata.get("resolver_module"),
            outcome=result.get("outcome"),
            selection_mode=selection_mode,
            result_family="body_signal_scope_result",
        ),
        "scoped_signal_id": scoped.get("scoped_signal_id"),
        "scoped_signal_category": scoped.get("scoped_signal_category"),
        "accepted_signal_id": scoped.get("accepted_signal_id"),
        "accepted_signal_category": scoped.get("accepted_signal_category"),
        "selected_signal_acceptance_result_id": scoped.get(
            "selected_signal_acceptance_result_id"
        )
        or selected_acceptance.get("signal_acceptance_result_id"),
        "selected_signal_acceptance_result_path": _display_path(
            scoped.get("selected_signal_acceptance_result_path")
            or selected_acceptance.get("signal_acceptance_result_path")
        ),
        "accepted_matter_id": scoped.get("accepted_matter_id"),
        "accepted_matter_family": scoped.get("accepted_matter_family"),
        "accepted_matter_kind": scoped.get("accepted_matter_kind"),
        "declared_scope_id": scoped.get("declared_scope_id")
        or declared_scope.get("scope_id"),
        "declared_scope_family": scoped.get("declared_scope_family")
        or declared_scope.get("scope_family"),
        "declared_scope_kind": scoped.get("declared_scope_kind")
        or declared_scope.get("scope_kind"),
        "recognized_source_artifact_id": scoped.get("recognized_source_artifact_id"),
        "recognized_source_artifact_path": _display_path(
            scoped.get("recognized_source_artifact_path")
        ),
        "recognized_source_artifact_family": scoped.get(
            "recognized_source_artifact_family"
        ),
        "recognized_source_artifact_outcome": scoped.get(
            "recognized_source_artifact_outcome"
        ),
    }


def _select_body_pass(
    body_pass_result: Mapping[str, Any] | None = None,
    body_pass_result_path: Path | str | None = None,
) -> tuple[Path | str, dict[str, Any], str]:
    if body_pass_result is not None:
        if not isinstance(body_pass_result, Mapping):
            raise CurrentSelfOrientationV5Error(
                "body_pass_result must be an object",
                "SOURCE_ARTIFACT_MALFORMED",
            )
        artifact = copy.deepcopy(dict(body_pass_result))
        if artifact.get("outcome") != OUTCOME_BODY_PASS_CONFIRMED:
            raise CurrentSelfOrientationV5Error(
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
            raise CurrentSelfOrientationV5Error(
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
        except CurrentSelfOrientationV5Error:
            continue
        if artifact.get("outcome") == OUTCOME_BODY_PASS_CONFIRMED:
            candidates.append((path, artifact))
    if not candidates:
        raise CurrentSelfOrientationV5Error(
            "no confirmed body-pass result is available",
            "NO_SELF_ORIENTATION_SOURCE_BASIS",
        )
    path, artifact = candidates[-1]
    return path, artifact, "successful_body_pass_discovery"


def _selected_body_pass_from_orientation(result: Mapping[str, Any]) -> Mapping[str, Any]:
    selected = _require_mapping(
        result.get("selected_orientation_inputs"),
        "selected_orientation_inputs",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    return _require_mapping(
        selected.get("selected_body_pass_result"),
        "selected_body_pass_result",
        "SOURCE_ARTIFACT_MALFORMED",
    )


def _body_pass_matches(selected_body: Mapping[str, Any], body_identity: Mapping[str, Any]) -> bool:
    body_id = _string_or_none(body_identity.get("result_id"))
    body_path = _string_or_none(body_identity.get("result_path"))
    selected_id = _string_or_none(selected_body.get("result_id"))
    selected_path = _string_or_none(selected_body.get("result_path"))
    return bool(
        (body_id is not None and body_id == selected_id)
        or (body_path is not None and _path_equal(body_path, selected_path))
    )


def _validate_false_non_claims(value: Any, context: str) -> None:
    if not isinstance(value, Mapping):
        raise CurrentSelfOrientationV5Error(
            f"{context} non_claims must be an object",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    for key, item in value.items():
        if not isinstance(key, str) or item is not False:
            raise CurrentSelfOrientationV5Error(
                f"{context} non-claim is missing or flipped: {key}",
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )


def _validate_self_orientation_v4_result(result: Mapping[str, Any]) -> None:
    metadata = _metadata_section(result, "current_self_orientation_v4_metadata")
    if metadata.get("self_orientation_result_type") != SELF_ORIENTATION_V4_RESULT_TYPE:
        raise CurrentSelfOrientationV5Error(
            "v4 self-orientation result type is not recognized",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    if metadata.get("resolver_module") != SELF_ORIENTATION_V4_RESOLVER_MODULE:
        raise CurrentSelfOrientationV5Error(
            "v4 self-orientation resolver module is not recognized",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    if result.get("outcome") != OUTCOME_SELF_ORIENTED:
        raise CurrentSelfOrientationV5Error(
            "v4 self-orientation result is not SELF_ORIENTED",
            "NO_SELF_ORIENTATION_SOURCE_BASIS",
        )
    _validate_false_non_claims(result.get("non_claims"), "v4 self-orientation")


def _select_matching_self_orientation_v4(
    body_identity: Mapping[str, Any],
) -> tuple[Path, dict[str, Any], str]:
    matches: list[tuple[Path, dict[str, Any]]] = []
    for path in _discover_json_files(CURRENT_SELF_ORIENTATION_V4_ROOT):
        try:
            artifact = _read_json_file(
                path,
                context="candidate current self-orientation v4 result",
                missing_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                malformed_code="SOURCE_ARTIFACT_MALFORMED",
            )
            _validate_self_orientation_v4_result(artifact)
            selected_body = _selected_body_pass_from_orientation(artifact)
        except CurrentSelfOrientationV5Error:
            continue
        if _body_pass_matches(selected_body, body_identity):
            matches.append((path, artifact))
    if not matches:
        raise CurrentSelfOrientationV5Error(
            "no self-oriented v4 result matches the selected body-pass basis",
            "NO_SELF_ORIENTATION_SOURCE_BASIS",
        )
    path, artifact = matches[-1]
    return path, artifact, "matching_self_orientation_v4_discovery"


def _validate_body_signal_recognition_v2_result(result: Mapping[str, Any]) -> None:
    metadata = _metadata_section(result, "body_signal_recognition_v2_metadata")
    if metadata.get("body_signal_recognition_result_type") != BODY_SIGNAL_RECOGNITION_V2_RESULT_TYPE:
        raise CurrentSelfOrientationV5Error(
            "body-signal recognition result type is not recognized",
            "BODY_SIGNAL_RECOGNITION_MALFORMED",
        )
    if metadata.get("resolver_module") != BODY_SIGNAL_RECOGNITION_V2_RESOLVER_MODULE:
        raise CurrentSelfOrientationV5Error(
            "body-signal recognition resolver module is not recognized",
            "BODY_SIGNAL_RECOGNITION_MALFORMED",
        )
    if result.get("outcome") not in {OUTCOME_SIGNAL_RECOGNIZED, OUTCOME_BLOCKED}:
        raise CurrentSelfOrientationV5Error(
            "body-signal recognition result outcome is not recognized",
            "BODY_SIGNAL_RECOGNITION_MALFORMED",
        )
    _validate_false_non_claims(result.get("non_claims"), "body-signal recognition")


def _recognition_source_matches_body(
    recognition_identity: Mapping[str, Any],
    body_identity: Mapping[str, Any],
) -> bool:
    source_id = _string_or_none(recognition_identity.get("recognized_source_artifact_id"))
    source_path = _string_or_none(recognition_identity.get("recognized_source_artifact_path"))
    body_id = _string_or_none(body_identity.get("result_id"))
    body_path = _string_or_none(body_identity.get("result_path"))
    return bool(
        (body_id is not None and source_id == body_id)
        or (body_path is not None and _path_equal(source_path, body_path))
    )


def _select_matching_body_signal_recognition(
    body_identity: Mapping[str, Any],
) -> tuple[Path, dict[str, Any], dict[str, Any], str]:
    matches: list[tuple[Path, dict[str, Any], dict[str, Any]]] = []
    for path in _discover_json_files(BODY_SIGNAL_RECOGNITION_V2_ROOT):
        try:
            artifact = _read_json_file(
                path,
                context="candidate body-signal recognition v2 result",
                missing_code="BODY_SIGNAL_RECOGNITION_UNREADABLE",
                unreadable_code="BODY_SIGNAL_RECOGNITION_UNREADABLE",
                malformed_code="BODY_SIGNAL_RECOGNITION_MALFORMED",
            )
            _validate_body_signal_recognition_v2_result(artifact)
        except CurrentSelfOrientationV5Error:
            continue
        identity = _body_signal_recognition_identity(
            artifact,
            path,
            "matching_body_signal_recognition_v2_discovery",
        )
        if (
            artifact.get("outcome") == OUTCOME_SIGNAL_RECOGNIZED
            and identity.get("recognized_signal_category") == SIGNAL_CATEGORY_BODY_PASS
            and identity.get("recognized_source_artifact_family") == BODY_PASS_RESULT_FAMILY
            and _recognition_source_matches_body(identity, body_identity)
        ):
            matches.append((path, artifact, identity))
    if not matches:
        raise CurrentSelfOrientationV5Error(
            "no recognized body-pass signal matches the selected body-pass basis",
            "BODY_SIGNAL_RECOGNITION_UNREADABLE",
        )
    path, artifact, identity = matches[-1]
    return path, artifact, identity, "matching_body_signal_recognition_v2_discovery"


def _select_blocked_false_permission_signal(
    body_identity: Mapping[str, Any],
) -> tuple[Path, dict[str, Any], dict[str, Any], str] | None:
    matches: list[tuple[Path, dict[str, Any], dict[str, Any]]] = []
    for path in _discover_json_files(BODY_SIGNAL_RECOGNITION_V2_ROOT):
        try:
            artifact = _read_json_file(
                path,
                context="candidate blocked body-signal recognition v2 result",
                missing_code="BODY_SIGNAL_RECOGNITION_UNREADABLE",
                unreadable_code="BODY_SIGNAL_RECOGNITION_UNREADABLE",
                malformed_code="BODY_SIGNAL_RECOGNITION_MALFORMED",
            )
            _validate_body_signal_recognition_v2_result(artifact)
        except CurrentSelfOrientationV5Error:
            continue
        identity = _body_signal_recognition_identity(
            artifact,
            path,
            "matching_blocked_body_signal_recognition_v2_discovery",
        )
        block = artifact.get("block")
        block = block if isinstance(block, Mapping) else {}
        basis = artifact.get("body_signal_recognition_basis")
        basis = basis if isinstance(basis, Mapping) else {}
        category = identity.get("recognized_signal_category") or basis.get("signal_category")
        source_matches = _recognition_source_matches_body(identity, body_identity)
        if (
            artifact.get("outcome") == OUTCOME_BLOCKED
            and block.get("block_code") == "SIGNAL_ATTEMPTS_PERMISSION"
            and category == SIGNAL_CATEGORY_BODY_PASS
            and source_matches
        ):
            matches.append((path, artifact, identity))
    if not matches:
        return None
    path, artifact, identity = matches[-1]
    return path, artifact, identity, "matching_blocked_permission_signal_discovery"


def _validate_body_signal_acceptance_result(result: Mapping[str, Any]) -> None:
    metadata = _metadata_section(result, "body_signal_acceptance_metadata")
    if metadata.get("body_signal_acceptance_result_type") != BODY_SIGNAL_ACCEPTANCE_RESULT_TYPE:
        raise CurrentSelfOrientationV5Error(
            "body-signal acceptance result type is not recognized",
            "BODY_SIGNAL_ACCEPTANCE_MALFORMED",
        )
    if metadata.get("resolver_module") != BODY_SIGNAL_ACCEPTANCE_RESOLVER_MODULE:
        raise CurrentSelfOrientationV5Error(
            "body-signal acceptance resolver module is not recognized",
            "BODY_SIGNAL_ACCEPTANCE_MALFORMED",
        )
    if result.get("outcome") != OUTCOME_SIGNAL_ACCEPTED:
        raise CurrentSelfOrientationV5Error(
            "body-signal acceptance result is not accepted",
            "BODY_SIGNAL_ACCEPTANCE_NOT_ACCEPTED",
        )
    _validate_false_non_claims(result.get("non_claims"), "body-signal acceptance")


def _acceptance_matches_recognition(
    acceptance_identity: Mapping[str, Any],
    recognition_identity: Mapping[str, Any],
) -> bool:
    recognition_id = _string_or_none(recognition_identity.get("result_id"))
    recognition_path = _string_or_none(recognition_identity.get("result_path"))
    selected_id = _string_or_none(acceptance_identity.get("selected_signal_recognition_result_id"))
    selected_path = _string_or_none(
        acceptance_identity.get("selected_signal_recognition_result_path")
    )
    return bool(
        (recognition_id is not None and recognition_id == selected_id)
        or (recognition_path is not None and _path_equal(recognition_path, selected_path))
    )


def _select_matching_body_signal_acceptance(
    recognition_identity: Mapping[str, Any],
) -> tuple[Path, dict[str, Any], dict[str, Any], str]:
    matches: list[tuple[Path, dict[str, Any], dict[str, Any]]] = []
    for path in _discover_json_files(BODY_SIGNAL_ACCEPTANCE_ROOT):
        try:
            artifact = _read_json_file(
                path,
                context="candidate body-signal acceptance result",
                missing_code="BODY_SIGNAL_ACCEPTANCE_UNREADABLE",
                unreadable_code="BODY_SIGNAL_ACCEPTANCE_UNREADABLE",
                malformed_code="BODY_SIGNAL_ACCEPTANCE_MALFORMED",
            )
            _validate_body_signal_acceptance_result(artifact)
        except CurrentSelfOrientationV5Error:
            continue
        identity = _body_signal_acceptance_identity(
            artifact,
            path,
            "matching_body_signal_acceptance_discovery",
        )
        if (
            artifact.get("outcome") == OUTCOME_SIGNAL_ACCEPTED
            and _acceptance_matches_recognition(identity, recognition_identity)
            and identity.get("declared_matter_id") == ACCEPTANCE_MATTER_ID
        ):
            matches.append((path, artifact, identity))
    if not matches:
        raise CurrentSelfOrientationV5Error(
            "no accepted body signal matches the selected signal-recognition result",
            "BODY_SIGNAL_ACCEPTANCE_UNREADABLE",
        )
    path, artifact, identity = matches[-1]
    return path, artifact, identity, "matching_body_signal_acceptance_discovery"


def _validate_body_signal_scope_result(result: Mapping[str, Any]) -> None:
    metadata = _metadata_section(result, "body_signal_scope_metadata")
    if metadata.get("body_signal_scope_result_type") != BODY_SIGNAL_SCOPE_RESULT_TYPE:
        raise CurrentSelfOrientationV5Error(
            "body-signal scope result type is not recognized",
            "BODY_SIGNAL_SCOPE_MALFORMED",
        )
    if metadata.get("resolver_module") != BODY_SIGNAL_SCOPE_RESOLVER_MODULE:
        raise CurrentSelfOrientationV5Error(
            "body-signal scope resolver module is not recognized",
            "BODY_SIGNAL_SCOPE_MALFORMED",
        )
    if result.get("outcome") != OUTCOME_SIGNAL_SCOPED:
        raise CurrentSelfOrientationV5Error(
            "body-signal scope result is not scoped",
            "BODY_SIGNAL_SCOPE_NOT_SCOPED",
        )
    _validate_false_non_claims(result.get("non_claims"), "body-signal scope")


def _scope_matches_acceptance(
    scope_identity: Mapping[str, Any],
    acceptance_identity: Mapping[str, Any],
) -> bool:
    acceptance_id = _string_or_none(acceptance_identity.get("result_id"))
    acceptance_path = _string_or_none(acceptance_identity.get("result_path"))
    selected_id = _string_or_none(
        scope_identity.get("selected_signal_acceptance_result_id")
    )
    selected_path = _string_or_none(
        scope_identity.get("selected_signal_acceptance_result_path")
    )
    return bool(
        (acceptance_id is not None and acceptance_id == selected_id)
        or (acceptance_path is not None and _path_equal(acceptance_path, selected_path))
    )


def _scope_matches_recognition(
    scope_result: Mapping[str, Any],
    recognition_identity: Mapping[str, Any],
) -> bool:
    selected_accepted = scope_result.get("selected_accepted_signal")
    selected_accepted = (
        selected_accepted if isinstance(selected_accepted, Mapping) else {}
    )
    recognition_id = _string_or_none(recognition_identity.get("result_id"))
    recognition_path = _string_or_none(recognition_identity.get("result_path"))
    selected_id = _string_or_none(
        selected_accepted.get("selected_signal_recognition_result_id")
    )
    selected_path = _string_or_none(
        selected_accepted.get("selected_signal_recognition_result_path")
    )
    return bool(
        (recognition_id is not None and recognition_id == selected_id)
        or (recognition_path is not None and _path_equal(recognition_path, selected_path))
    )


def _select_matching_body_signal_scope(
    acceptance_identity: Mapping[str, Any],
    recognition_identity: Mapping[str, Any],
) -> tuple[Path, dict[str, Any], dict[str, Any], str]:
    matches: list[tuple[Path, dict[str, Any], dict[str, Any]]] = []
    for path in _discover_json_files(BODY_SIGNAL_SCOPE_ROOT):
        try:
            artifact = _read_json_file(
                path,
                context="candidate body-signal scope result",
                missing_code="BODY_SIGNAL_SCOPE_UNREADABLE",
                unreadable_code="BODY_SIGNAL_SCOPE_UNREADABLE",
                malformed_code="BODY_SIGNAL_SCOPE_MALFORMED",
            )
            _validate_body_signal_scope_result(artifact)
        except CurrentSelfOrientationV5Error:
            continue
        identity = _body_signal_scope_identity(
            artifact,
            path,
            "matching_body_signal_scope_discovery",
        )
        if (
            artifact.get("outcome") == OUTCOME_SIGNAL_SCOPED
            and _scope_matches_acceptance(identity, acceptance_identity)
            and _scope_matches_recognition(artifact, recognition_identity)
            and identity.get("declared_scope_id") == SCOPE_ID
            and identity.get("accepted_matter_id") == ACCEPTANCE_MATTER_ID
        ):
            matches.append((path, artifact, identity))
    if not matches:
        raise CurrentSelfOrientationV5Error(
            "no scoped body signal matches the selected signal-acceptance result",
            "BODY_SIGNAL_SCOPE_UNREADABLE",
        )
    path, artifact, identity = matches[-1]
    return path, artifact, identity, "matching_body_signal_scope_discovery"


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
                raise CurrentSelfOrientationV5Error(
                    f"non-claim is missing or flipped: {key}",
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )
    return merged


def _accepted_signal(result: Mapping[str, Any]) -> Mapping[str, Any]:
    accepted = result.get("accepted_signal")
    return accepted if isinstance(accepted, Mapping) else {}


def _recognized_signal(result: Mapping[str, Any]) -> Mapping[str, Any]:
    recognized = result.get("recognized_signal")
    return recognized if isinstance(recognized, Mapping) else {}


def _acceptance_summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = result.get("body_signal_acceptance_summary")
    return summary if isinstance(summary, Mapping) else {}


def _scoped_signal(result: Mapping[str, Any]) -> Mapping[str, Any]:
    scoped = result.get("scoped_signal")
    return scoped if isinstance(scoped, Mapping) else {}


def _scope_summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = result.get("body_signal_scope_summary")
    return summary if isinstance(summary, Mapping) else {}


def _recognition_summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = result.get("body_signal_recognition_summary")
    return summary if isinstance(summary, Mapping) else {}


def _body_signal_recognition_check_passed(result: Mapping[str, Any]) -> bool:
    summary = _recognition_summary(result)
    return (
        summary.get("failed_check_count") == 0
        and summary.get("hierarchy_constraints_passed") is True
        and summary.get("correspondence_requirements_passed") is True
        and summary.get("non_claims_passed") is True
    )


def _body_signal_acceptance_check_passed(result: Mapping[str, Any]) -> bool:
    summary = _acceptance_summary(result)
    return (
        summary.get("failed_check_count") == 0
        and summary.get("recognition_basis_passed") is True
        and summary.get("matter_boundary_passed") is True
        and summary.get("acceptance_scope_passed") is True
        and summary.get("hierarchy_constraints_passed") is True
        and summary.get("correspondence_requirements_passed") is True
        and summary.get("non_claims_passed") is True
    )


def _body_signal_scope_check_passed(result: Mapping[str, Any]) -> bool:
    summary = _scope_summary(result)
    return (
        summary.get("failed_check_count") == 0
        and summary.get("acceptance_basis_passed") is True
        and summary.get("scope_boundary_passed") is True
        and summary.get("scope_limits_passed") is True
        and summary.get("hierarchy_constraints_passed") is True
        and summary.get("correspondence_requirements_passed") is True
        and summary.get("non_claims_passed") is True
    )


def _build_body_signal_checks(
    body_identity: Mapping[str, Any],
    recognition_identity: Mapping[str, Any],
    recognition_result: Mapping[str, Any],
    blocked_recognition_identity: Mapping[str, Any] | None,
    blocked_recognition_result: Mapping[str, Any] | None,
    acceptance_identity: Mapping[str, Any],
    acceptance_result: Mapping[str, Any],
    scope_identity: Mapping[str, Any],
    scope_result: Mapping[str, Any],
) -> list[dict[str, Any]]:
    recognized = _recognized_signal(recognition_result)
    accepted = _accepted_signal(acceptance_result)
    scoped = _scoped_signal(scope_result)
    acceptance_non_claims = acceptance_result.get("non_claims")
    acceptance_non_claims = (
        acceptance_non_claims if isinstance(acceptance_non_claims, Mapping) else {}
    )
    scope_non_claims = scope_result.get("non_claims")
    scope_non_claims = (
        scope_non_claims if isinstance(scope_non_claims, Mapping) else {}
    )
    recognition_non_claims = recognition_result.get("non_claims")
    recognition_non_claims = (
        recognition_non_claims if isinstance(recognition_non_claims, Mapping) else {}
    )
    blocked_block = (
        blocked_recognition_result.get("block")
        if isinstance(blocked_recognition_result, Mapping)
        else {}
    )
    blocked_block = blocked_block if isinstance(blocked_block, Mapping) else {}

    accepted_category = accepted.get("accepted_signal_category")
    accepted_matter_id = accepted.get("declared_matter_id") or acceptance_identity.get(
        "declared_matter_id"
    )
    no_scope = accepted.get("not_scoped_yet") is True and acceptance_non_claims.get(
        "scope_assigned"
    ) is False
    no_presence = accepted.get("not_present_yet") is True and acceptance_non_claims.get(
        "presence_established"
    ) is False
    no_threshold = accepted.get("not_threshold_yet") is True and acceptance_non_claims.get(
        "threshold_met"
    ) is False
    no_truth = accepted.get("not_truth") is True and acceptance_non_claims.get(
        "truth_created"
    ) is False
    no_action = accepted.get("no_action") is True and acceptance_non_claims.get(
        "action_authorized"
    ) is False
    no_follow_on = acceptance_non_claims.get("follow_on_work_authorized") is False
    no_routing = accepted.get("no_routing") is True and acceptance_non_claims.get(
        "signal_router_created"
    ) is False
    no_workflow = accepted.get("no_workflow") is True and acceptance_non_claims.get(
        "workflow_created"
    ) is False
    no_medium = accepted.get("no_body_relevance_medium") is True and acceptance_non_claims.get(
        "body_relevance_medium_created"
    ) is False
    scoped_no_presence = (
        scoped.get("not_present_yet") is True
        and scope_non_claims.get("presence_established") is False
    )
    scoped_no_threshold = (
        scoped.get("not_threshold_yet") is True
        and scope_non_claims.get("threshold_met") is False
    )
    scoped_no_truth = (
        scoped.get("not_truth") is True
        and scope_non_claims.get("truth_created") is False
    )
    scoped_no_action = (
        scoped.get("no_action") is True
        and scope_non_claims.get("action_authorized") is False
    )
    scoped_no_follow_on = scope_non_claims.get("follow_on_work_authorized") is False
    scoped_no_routing = (
        scoped.get("no_routing") is True
        and scope_non_claims.get("signal_router_created") is False
    )
    scoped_no_workflow = (
        scoped.get("no_workflow") is True
        and scope_non_claims.get("workflow_created") is False
    )
    scoped_no_medium = (
        scoped.get("no_body_relevance_medium") is True
        and scope_non_claims.get("body_relevance_medium_created") is False
    )
    scoped_no_outside_scope = (
        scoped.get("no_application_outside_declared_scope") is True
        and scope_non_claims.get("applied_outside_declared_scope") is False
    )

    checks = [
        _check(
            "body_signal_recognition_v2_is_recognized",
            recognition_result.get("outcome") == OUTCOME_SIGNAL_RECOGNIZED,
            expected=OUTCOME_SIGNAL_RECOGNIZED,
            actual=recognition_result.get("outcome"),
            block_code="BODY_SIGNAL_RECOGNITION_NOT_RECOGNIZED",
        ),
        _check(
            "body_signal_recognition_category_is_body_pass_signal",
            recognition_identity.get("recognized_signal_category") == SIGNAL_CATEGORY_BODY_PASS,
            expected=SIGNAL_CATEGORY_BODY_PASS,
            actual=recognition_identity.get("recognized_signal_category"),
            block_code="BODY_SIGNAL_RECOGNITION_CATEGORY_MISMATCH",
        ),
        _check(
            "body_signal_recognition_source_family_is_v0_body_pass_result",
            recognition_identity.get("recognized_source_artifact_family")
            == BODY_PASS_RESULT_FAMILY,
            expected=BODY_PASS_RESULT_FAMILY,
            actual=recognition_identity.get("recognized_source_artifact_family"),
            block_code="BODY_SIGNAL_RECOGNITION_SOURCE_FAMILY_MISMATCH",
        ),
        _check(
            "body_signal_recognition_source_matches_selected_body_pass",
            _recognition_source_matches_body(recognition_identity, body_identity),
            expected=body_identity,
            actual={
                "recognized_source_artifact_id": recognition_identity.get(
                    "recognized_source_artifact_id"
                ),
                "recognized_source_artifact_path": recognition_identity.get(
                    "recognized_source_artifact_path"
                ),
            },
            block_code="BODY_SIGNAL_RECOGNITION_SOURCE_FAMILY_MISMATCH",
        ),
        _check(
            "body_signal_recognition_checks_passed",
            _body_signal_recognition_check_passed(recognition_result),
            expected="recognition checks passed",
            actual=_recognition_summary(recognition_result),
            block_code="BODY_SIGNAL_RECOGNITION_MALFORMED",
        ),
        _check(
            "body_signal_blocked_false_permission_signal_remains_blocked",
            blocked_recognition_result is None
            or (
                blocked_recognition_result.get("outcome") == OUTCOME_BLOCKED
                and blocked_block.get("block_code") == "SIGNAL_ATTEMPTS_PERMISSION"
            ),
            expected="blocked permission-shaped candidate stays blocked when selected",
            actual=blocked_block if blocked_recognition_result is not None else "not selected",
            block_code="BODY_SIGNAL_BLOCKED_PERMISSION_REFUSAL_NOT_VISIBLE",
        ),
        _check(
            "body_signal_acceptance_is_accepted",
            acceptance_result.get("outcome") == OUTCOME_SIGNAL_ACCEPTED,
            expected=OUTCOME_SIGNAL_ACCEPTED,
            actual=acceptance_result.get("outcome"),
            block_code="BODY_SIGNAL_ACCEPTANCE_NOT_ACCEPTED",
        ),
        _check(
            "body_signal_acceptance_matches_selected_recognition",
            _acceptance_matches_recognition(acceptance_identity, recognition_identity),
            expected=recognition_identity,
            actual=acceptance_identity,
            block_code="BODY_SIGNAL_ACCEPTANCE_DOES_NOT_MATCH_SELECTED_RECOGNITION",
        ),
        _check(
            "body_signal_acceptance_declared_matter_is_current_signal_recognition_standing",
            accepted_matter_id == ACCEPTANCE_MATTER_ID,
            expected=ACCEPTANCE_MATTER_ID,
            actual=accepted_matter_id,
            block_code="BODY_SIGNAL_ACCEPTANCE_MATTER_MISMATCH",
        ),
        _check(
            "accepted_signal_category_matches_recognized_signal_category",
            accepted_category == recognized.get("signal_category"),
            expected=recognized.get("signal_category"),
            actual=accepted_category,
            block_code="BODY_SIGNAL_ACCEPTANCE_DOES_NOT_MATCH_SELECTED_RECOGNITION",
        ),
        _check(
            "body_signal_acceptance_checks_passed",
            _body_signal_acceptance_check_passed(acceptance_result),
            expected="acceptance checks passed",
            actual=_acceptance_summary(acceptance_result),
            block_code="BODY_SIGNAL_ACCEPTANCE_MALFORMED",
        ),
        _check(
            "accepted_signal_remains_non_authoritative",
            accepted.get("non_authoritative") is True
            and acceptance_non_claims.get("authority_created") is False
            and recognition_non_claims.get("authority_created") is False,
            expected=True,
            actual={
                "accepted_signal": accepted.get("non_authoritative"),
                "acceptance_authority_created": acceptance_non_claims.get(
                    "authority_created"
                ),
                "recognition_authority_created": recognition_non_claims.get(
                    "authority_created"
                ),
            },
            block_code="BODY_SIGNAL_SURFACE_TREATED_AS_AUTHORITY",
        ),
        _check(
            "accepted_signal_remains_non_permission",
            accepted.get("non_permission") is True
            and acceptance_non_claims.get("permission_created") is False
            and recognition_non_claims.get("permission_created") is False,
            expected=True,
            actual={
                "accepted_signal": accepted.get("non_permission"),
                "acceptance_permission_created": acceptance_non_claims.get(
                    "permission_created"
                ),
                "recognition_permission_created": recognition_non_claims.get(
                    "permission_created"
                ),
            },
            block_code="BODY_SIGNAL_ACCEPTANCE_ACTION_PERMISSION_LEAK",
        ),
        _check(
            "accepted_signal_remains_non_currentness",
            accepted.get("non_currentness") is True
            and acceptance_non_claims.get("currentness_created") is False
            and recognition_non_claims.get("currentness_created") is False,
            expected=True,
            actual={
                "accepted_signal": accepted.get("non_currentness"),
                "acceptance_currentness_created": acceptance_non_claims.get(
                    "currentness_created"
                ),
                "recognition_currentness_created": recognition_non_claims.get(
                    "currentness_created"
                ),
            },
            block_code="BODY_SIGNAL_SURFACE_TREATED_AS_CURRENT_OR_GOVERNING_BASIS",
        ),
        _check(
            "accepted_signal_is_not_scoped",
            no_scope,
            expected=True,
            actual={
                "not_scoped_yet": accepted.get("not_scoped_yet"),
                "scope_assigned": acceptance_non_claims.get("scope_assigned"),
            },
            block_code="BODY_SIGNAL_ACCEPTANCE_SCOPE_COLLAPSE",
        ),
        _check(
            "accepted_signal_is_not_present",
            no_presence,
            expected=True,
            actual={
                "not_present_yet": accepted.get("not_present_yet"),
                "presence_established": acceptance_non_claims.get("presence_established"),
            },
            block_code="BODY_SIGNAL_ACCEPTANCE_SCOPE_COLLAPSE",
        ),
        _check(
            "accepted_signal_has_not_met_threshold",
            no_threshold,
            expected=True,
            actual={
                "not_threshold_yet": accepted.get("not_threshold_yet"),
                "threshold_met": acceptance_non_claims.get("threshold_met"),
            },
            block_code="BODY_SIGNAL_ACCEPTANCE_TRUTH_COLLAPSE",
        ),
        _check(
            "accepted_signal_is_not_truth",
            no_truth,
            expected=True,
            actual={
                "not_truth": accepted.get("not_truth"),
                "truth_created": acceptance_non_claims.get("truth_created"),
            },
            block_code="BODY_SIGNAL_ACCEPTANCE_TRUTH_COLLAPSE",
        ),
        _check(
            "accepted_signal_does_not_authorize_action",
            no_action,
            expected=True,
            actual={
                "no_action": accepted.get("no_action"),
                "action_authorized": acceptance_non_claims.get("action_authorized"),
            },
            block_code="BODY_SIGNAL_ACCEPTANCE_ACTION_PERMISSION_LEAK",
        ),
        _check(
            "accepted_signal_does_not_authorize_follow_on_work",
            no_follow_on,
            expected=False,
            actual=acceptance_non_claims.get("follow_on_work_authorized"),
            block_code="BODY_SIGNAL_ACCEPTANCE_FOLLOW_ON_PERMISSION_LEAK",
        ),
        _check(
            "accepted_signal_does_not_route_signal",
            no_routing,
            expected=True,
            actual={
                "no_routing": accepted.get("no_routing"),
                "signal_router_created": acceptance_non_claims.get(
                    "signal_router_created"
                ),
            },
            block_code="BODY_SIGNAL_ACCEPTANCE_ROUTING_LEAK",
        ),
        _check(
            "accepted_signal_does_not_create_workflow",
            no_workflow,
            expected=True,
            actual={
                "no_workflow": accepted.get("no_workflow"),
                "workflow_created": acceptance_non_claims.get("workflow_created"),
            },
            block_code="BODY_SIGNAL_ACCEPTANCE_WORKFLOW_LEAK",
        ),
        _check(
            "accepted_signal_does_not_create_body_relevance_medium",
            no_medium,
            expected=True,
            actual={
                "no_body_relevance_medium": accepted.get("no_body_relevance_medium"),
                "body_relevance_medium_created": acceptance_non_claims.get(
                    "body_relevance_medium_created"
                ),
            },
            block_code="BODY_SIGNAL_ACCEPTANCE_BODY_RELEVANCE_MEDIUM_LEAK",
        ),
        _check(
            "body_signal_surfaces_remain_non_authoritative",
            recognition_non_claims.get("authority_created") is False
            and acceptance_non_claims.get("authority_created") is False,
            expected=False,
            actual={
                "recognition_authority_created": recognition_non_claims.get(
                    "authority_created"
                ),
                "acceptance_authority_created": acceptance_non_claims.get(
                    "authority_created"
                ),
            },
            block_code="BODY_SIGNAL_SURFACE_TREATED_AS_AUTHORITY",
        ),
        _check(
            "body_signal_surfaces_do_not_determine_current_governing_basis",
            acceptance_non_claims.get("currentness_created") is False
            and recognition_non_claims.get("currentness_created") is False,
            expected=False,
            actual={
                "recognition_currentness_created": recognition_non_claims.get(
                    "currentness_created"
                ),
                "acceptance_currentness_created": acceptance_non_claims.get(
                    "currentness_created"
                ),
            },
            block_code="BODY_SIGNAL_SURFACE_TREATED_AS_CURRENT_OR_GOVERNING_BASIS",
        ),
        _check(
            "body_signal_line_is_not_action_route_workflow_or_continuation",
            no_action and no_follow_on and no_routing and no_workflow,
            expected="no action, continuation, route, or workflow",
            actual={
                "no_action": no_action,
                "no_follow_on": no_follow_on,
                "no_routing": no_routing,
                "no_workflow": no_workflow,
            },
            block_code="BODY_SIGNAL_LINE_TREATED_AS_ACTION_OR_CONTINUATION",
        ),
        _check(
            "body_signal_scope_is_scoped",
            scope_result.get("outcome") == OUTCOME_SIGNAL_SCOPED,
            expected=OUTCOME_SIGNAL_SCOPED,
            actual=scope_result.get("outcome"),
            block_code="BODY_SIGNAL_SCOPE_NOT_SCOPED",
        ),
        _check(
            "body_signal_scope_matches_selected_acceptance",
            _scope_matches_acceptance(scope_identity, acceptance_identity),
            expected=acceptance_identity,
            actual=scope_identity,
            block_code="BODY_SIGNAL_SCOPE_DOES_NOT_MATCH_SELECTED_ACCEPTANCE",
        ),
        _check(
            "body_signal_scope_matches_selected_recognition",
            _scope_matches_recognition(scope_result, recognition_identity),
            expected=recognition_identity,
            actual=scope_result.get("selected_accepted_signal"),
            block_code="BODY_SIGNAL_SCOPE_DOES_NOT_MATCH_SELECTED_RECOGNITION",
        ),
        _check(
            "body_signal_scope_declared_scope_is_nonoperative_body_pass_scope",
            scope_identity.get("declared_scope_id") == SCOPE_ID,
            expected=SCOPE_ID,
            actual=scope_identity.get("declared_scope_id"),
            block_code="BODY_SIGNAL_SCOPE_DECLARED_SCOPE_MISMATCH",
        ),
        _check(
            "body_signal_scope_accepted_matter_is_current_signal_recognition_standing",
            scope_identity.get("accepted_matter_id") == ACCEPTANCE_MATTER_ID,
            expected=ACCEPTANCE_MATTER_ID,
            actual=scope_identity.get("accepted_matter_id"),
            block_code="BODY_SIGNAL_SCOPE_ACCEPTED_MATTER_MISMATCH",
        ),
        _check(
            "scoped_signal_category_matches_accepted_signal_category",
            scoped.get("scoped_signal_category") == accepted.get("accepted_signal_category"),
            expected=accepted.get("accepted_signal_category"),
            actual=scoped.get("scoped_signal_category"),
            block_code="BODY_SIGNAL_SCOPE_DOES_NOT_MATCH_SELECTED_ACCEPTANCE",
        ),
        _check(
            "body_signal_scope_checks_passed",
            _body_signal_scope_check_passed(scope_result),
            expected="scope checks passed",
            actual=_scope_summary(scope_result),
            block_code="BODY_SIGNAL_SCOPE_MALFORMED",
        ),
        _check(
            "scoped_signal_remains_non_authoritative",
            scoped.get("non_authoritative") is True
            and scope_non_claims.get("authority_created") is False,
            expected=True,
            actual={
                "scoped_signal": scoped.get("non_authoritative"),
                "scope_authority_created": scope_non_claims.get("authority_created"),
            },
            block_code="BODY_SIGNAL_SCOPE_TREATED_AS_AUTHORITY",
        ),
        _check(
            "scoped_signal_remains_non_permission",
            scoped.get("non_permission") is True
            and scope_non_claims.get("permission_created") is False,
            expected=True,
            actual={
                "scoped_signal": scoped.get("non_permission"),
                "scope_permission_created": scope_non_claims.get("permission_created"),
            },
            block_code="BODY_SIGNAL_SCOPE_ACTION_PERMISSION_LEAK",
        ),
        _check(
            "scoped_signal_remains_non_currentness",
            scoped.get("non_currentness") is True
            and scope_non_claims.get("currentness_created") is False,
            expected=True,
            actual={
                "scoped_signal": scoped.get("non_currentness"),
                "scope_currentness_created": scope_non_claims.get("currentness_created"),
            },
            block_code="BODY_SIGNAL_SCOPE_TREATED_AS_CURRENT_OR_GOVERNING_BASIS",
        ),
        _check(
            "scoped_signal_not_present",
            scoped_no_presence,
            expected=True,
            actual={
                "not_present_yet": scoped.get("not_present_yet"),
                "presence_established": scope_non_claims.get("presence_established"),
            },
            block_code="BODY_SIGNAL_SCOPE_PRESENCE_COLLAPSE",
        ),
        _check(
            "scoped_signal_not_threshold",
            scoped_no_threshold,
            expected=True,
            actual={
                "not_threshold_yet": scoped.get("not_threshold_yet"),
                "threshold_met": scope_non_claims.get("threshold_met"),
            },
            block_code="BODY_SIGNAL_SCOPE_THRESHOLD_COLLAPSE",
        ),
        _check(
            "scoped_signal_not_truth",
            scoped_no_truth,
            expected=True,
            actual={
                "not_truth": scoped.get("not_truth"),
                "truth_created": scope_non_claims.get("truth_created"),
            },
            block_code="BODY_SIGNAL_SCOPE_TRUTH_COLLAPSE",
        ),
        _check(
            "scoped_signal_no_action",
            scoped_no_action,
            expected=True,
            actual={
                "no_action": scoped.get("no_action"),
                "action_authorized": scope_non_claims.get("action_authorized"),
            },
            block_code="BODY_SIGNAL_SCOPE_ACTION_PERMISSION_LEAK",
        ),
        _check(
            "scoped_signal_no_follow_on",
            scoped_no_follow_on,
            expected=False,
            actual=scope_non_claims.get("follow_on_work_authorized"),
            block_code="BODY_SIGNAL_SCOPE_FOLLOW_ON_PERMISSION_LEAK",
        ),
        _check(
            "scoped_signal_no_routing",
            scoped_no_routing,
            expected=True,
            actual={
                "no_routing": scoped.get("no_routing"),
                "signal_router_created": scope_non_claims.get("signal_router_created"),
            },
            block_code="BODY_SIGNAL_SCOPE_ROUTING_LEAK",
        ),
        _check(
            "scoped_signal_no_workflow",
            scoped_no_workflow,
            expected=True,
            actual={
                "no_workflow": scoped.get("no_workflow"),
                "workflow_created": scope_non_claims.get("workflow_created"),
            },
            block_code="BODY_SIGNAL_SCOPE_WORKFLOW_LEAK",
        ),
        _check(
            "scoped_signal_no_body_relevance_medium",
            scoped_no_medium,
            expected=True,
            actual={
                "no_body_relevance_medium": scoped.get("no_body_relevance_medium"),
                "body_relevance_medium_created": scope_non_claims.get(
                    "body_relevance_medium_created"
                ),
            },
            block_code="BODY_SIGNAL_SCOPE_BODY_RELEVANCE_MEDIUM_LEAK",
        ),
        _check(
            "scoped_signal_no_application_outside_declared_scope",
            scoped_no_outside_scope,
            expected=True,
            actual={
                "no_application_outside_declared_scope": scoped.get(
                    "no_application_outside_declared_scope"
                ),
                "applied_outside_declared_scope": scope_non_claims.get(
                    "applied_outside_declared_scope"
                ),
            },
            block_code="BODY_SIGNAL_SCOPE_APPLIED_OUTSIDE_DECLARED_SCOPE",
        ),
        _check(
            "body_signal_scope_surface_remains_downstream",
            scope_non_claims.get("authority_created") is False,
            expected=False,
            actual=scope_non_claims.get("authority_created"),
            block_code="BODY_SIGNAL_SCOPE_TREATED_AS_AUTHORITY",
        ),
        _check(
            "body_signal_scope_surface_does_not_determine_current_governing_basis",
            scope_non_claims.get("currentness_created") is False,
            expected=False,
            actual=scope_non_claims.get("currentness_created"),
            block_code="BODY_SIGNAL_SCOPE_TREATED_AS_CURRENT_OR_GOVERNING_BASIS",
        ),
        _check(
            "body_signal_line_does_not_become_action_or_continuation",
            scoped_no_action and scoped_no_follow_on and scoped_no_routing and scoped_no_workflow,
            expected="no action, continuation, route, or workflow",
            actual={
                "scoped_no_action": scoped_no_action,
                "scoped_no_follow_on": scoped_no_follow_on,
                "scoped_no_routing": scoped_no_routing,
                "scoped_no_workflow": scoped_no_workflow,
            },
            block_code="BODY_SIGNAL_LINE_TREATED_AS_ACTION_OR_CONTINUATION",
        ),
    ]
    return checks


def _selected_inputs_with_signal_line(
    v4_result: Mapping[str, Any],
    v4_identity: Mapping[str, Any],
    recognition_identity: Mapping[str, Any],
    blocked_recognition_identity: Mapping[str, Any] | None,
    acceptance_identity: Mapping[str, Any],
    scope_identity: Mapping[str, Any],
) -> dict[str, Any]:
    selected = copy.deepcopy(
        dict(
            _require_mapping(
                v4_result.get("selected_orientation_inputs"),
                "selected_orientation_inputs",
                "SOURCE_ARTIFACT_MALFORMED",
            )
        )
    )
    selected["selected_self_orientation_v4_result"] = dict(v4_identity)
    selected["selected_body_signal_recognition_result"] = dict(recognition_identity)
    selected["selected_blocked_body_signal_recognition_result"] = (
        dict(blocked_recognition_identity) if blocked_recognition_identity else {}
    )
    selected["selected_body_signal_acceptance_result"] = dict(acceptance_identity)
    selected["selected_body_signal_scope_result"] = dict(scope_identity)
    selected["selection_scope"] = {
        **(
            selected.get("selection_scope")
            if isinstance(selected.get("selection_scope"), Mapping)
            else {}
        ),
        "body_pass_anchor_required": True,
        "self_orientation_v4_is_predecessor_recognition": True,
        "reentry_surfaces_are_downstream_only": True,
        "body_signal_surfaces_are_downstream_only": True,
        "body_signal_scope_surface_is_downstream_only": True,
        "latest_file_recency_refused": True,
        "repo_wide_authority_scan_performed": False,
    }
    return selected


def _recognized_body_signal_surfaces(
    recognition_identity: Mapping[str, Any],
    recognition_result: Mapping[str, Any],
    blocked_recognition_identity: Mapping[str, Any] | None,
    blocked_recognition_result: Mapping[str, Any] | None,
    acceptance_identity: Mapping[str, Any],
    acceptance_result: Mapping[str, Any],
    scope_identity: Mapping[str, Any],
    scope_result: Mapping[str, Any],
) -> dict[str, Any]:
    recognized = _recognized_signal(recognition_result)
    accepted = _accepted_signal(acceptance_result)
    scoped = _scoped_signal(scope_result)
    scope_summary = _scope_summary(scope_result)
    acceptance_summary = _acceptance_summary(acceptance_result)
    recognition_summary = _recognition_summary(recognition_result)
    blocked_block = (
        blocked_recognition_result.get("block")
        if isinstance(blocked_recognition_result, Mapping)
        else {}
    )
    blocked_block = blocked_block if isinstance(blocked_block, Mapping) else {}
    return {
        "recognition_posture": "downstream_body_signal_recognition_acceptance_and_scope_only",
        "selected_body_signal_recognition_result": dict(recognition_identity),
        "selected_recognized_signal": {
            "recognized_signal_id": recognized.get("recognized_signal_id"),
            "signal_category": recognized.get("signal_category"),
            "source_artifact_id": recognized.get("source_artifact_id"),
            "source_artifact_path": _display_path(recognized.get("source_artifact_path")),
            "source_artifact_family": recognized.get("source_artifact_family"),
            "source_artifact_outcome": recognized.get("source_artifact_outcome"),
            "non_authoritative": recognized.get("non_authoritative"),
            "non_permission": recognized.get("non_permission"),
            "non_currentness": recognized.get("non_currentness"),
        },
        "selected_blocked_body_signal_recognition_result": (
            dict(blocked_recognition_identity) if blocked_recognition_identity else {}
        ),
        "blocked_permission_refusal_posture": {
            "selected": blocked_recognition_result is not None,
            "outcome": (
                blocked_recognition_result.get("outcome")
                if isinstance(blocked_recognition_result, Mapping)
                else None
            ),
            "block_code": blocked_block.get("block_code"),
            "block_reason": blocked_block.get("block_reason"),
        },
        "selected_body_signal_acceptance_result": dict(acceptance_identity),
        "accepted_signal": {
            "accepted_signal_id": accepted.get("accepted_signal_id"),
            "accepted_signal_category": accepted.get("accepted_signal_category"),
            "declared_matter_id": accepted.get("declared_matter_id"),
            "declared_matter_family": accepted.get("declared_matter_family"),
            "declared_matter_kind": accepted.get("declared_matter_kind"),
            "recognized_source_artifact_id": accepted.get(
                "recognized_source_artifact_id"
            ),
            "recognized_source_artifact_path": _display_path(
                accepted.get("recognized_source_artifact_path")
            ),
            "recognized_source_artifact_family": accepted.get(
                "recognized_source_artifact_family"
            ),
            "recognized_source_artifact_outcome": accepted.get(
                "recognized_source_artifact_outcome"
            ),
            "non_authoritative": accepted.get("non_authoritative"),
            "non_permission": accepted.get("non_permission"),
            "non_currentness": accepted.get("non_currentness"),
            "not_scoped_yet": accepted.get("not_scoped_yet"),
            "not_present_yet": accepted.get("not_present_yet"),
            "not_threshold_yet": accepted.get("not_threshold_yet"),
            "not_truth": accepted.get("not_truth"),
            "no_action": accepted.get("no_action"),
            "no_routing": accepted.get("no_routing"),
            "no_workflow": accepted.get("no_workflow"),
            "no_body_relevance_medium": accepted.get("no_body_relevance_medium"),
        },
        "declared_matter": {
            "matter_id": accepted.get("declared_matter_id")
            or acceptance_identity.get("declared_matter_id"),
            "matter_family": accepted.get("declared_matter_family")
            or acceptance_identity.get("declared_matter_family"),
            "matter_kind": accepted.get("declared_matter_kind")
            or acceptance_identity.get("declared_matter_kind"),
            "matter_purpose": accepted.get("declared_matter_purpose"),
        },
        "selected_body_signal_scope_result": dict(scope_identity),
        "scoped_signal": {
            "scoped_signal_id": scoped.get("scoped_signal_id"),
            "scoped_signal_category": scoped.get("scoped_signal_category"),
            "accepted_signal_id": scoped.get("accepted_signal_id"),
            "accepted_signal_category": scoped.get("accepted_signal_category"),
            "accepted_matter_id": scoped.get("accepted_matter_id"),
            "accepted_matter_family": scoped.get("accepted_matter_family"),
            "accepted_matter_kind": scoped.get("accepted_matter_kind"),
            "recognized_source_artifact_id": scoped.get("recognized_source_artifact_id"),
            "recognized_source_artifact_path": _display_path(
                scoped.get("recognized_source_artifact_path")
            ),
            "recognized_source_artifact_family": scoped.get(
                "recognized_source_artifact_family"
            ),
            "recognized_source_artifact_outcome": scoped.get(
                "recognized_source_artifact_outcome"
            ),
            "declared_scope_id": scoped.get("declared_scope_id"),
            "declared_scope_family": scoped.get("declared_scope_family"),
            "declared_scope_kind": scoped.get("declared_scope_kind"),
            "declared_scope_purpose": scoped.get("declared_scope_purpose"),
            "declared_scope_boundary": scoped.get("declared_scope_boundary"),
            "applies_to": _clone(scoped.get("applies_to")),
            "does_not_apply_to": _clone(scoped.get("does_not_apply_to")),
            "non_authoritative": scoped.get("non_authoritative"),
            "non_permission": scoped.get("non_permission"),
            "non_currentness": scoped.get("non_currentness"),
            "not_present_yet": scoped.get("not_present_yet"),
            "not_threshold_yet": scoped.get("not_threshold_yet"),
            "not_truth": scoped.get("not_truth"),
            "no_action": scoped.get("no_action"),
            "no_routing": scoped.get("no_routing"),
            "no_workflow": scoped.get("no_workflow"),
            "no_body_relevance_medium": scoped.get("no_body_relevance_medium"),
            "no_application_outside_declared_scope": scoped.get(
                "no_application_outside_declared_scope"
            ),
        },
        "declared_scope": {
            "scope_id": scoped.get("declared_scope_id")
            or scope_identity.get("declared_scope_id"),
            "scope_family": scoped.get("declared_scope_family")
            or scope_identity.get("declared_scope_family"),
            "scope_kind": scoped.get("declared_scope_kind")
            or scope_identity.get("declared_scope_kind"),
            "accepted_matter_id": scoped.get("accepted_matter_id")
            or scope_identity.get("accepted_matter_id"),
        },
        "recognition_basis_passed": _body_signal_recognition_check_passed(
            recognition_result
        ),
        "recognition_hierarchy_constraints_passed": recognition_summary.get(
            "hierarchy_constraints_passed"
        ),
        "recognition_correspondence_requirements_passed": recognition_summary.get(
            "correspondence_requirements_passed"
        ),
        "recognition_non_claims_passed": recognition_summary.get("non_claims_passed"),
        "matter_boundary_passed": acceptance_summary.get("matter_boundary_passed"),
        "acceptance_scope_passed": acceptance_summary.get("acceptance_scope_passed"),
        "acceptance_hierarchy_constraints_passed": acceptance_summary.get(
            "hierarchy_constraints_passed"
        ),
        "acceptance_correspondence_requirements_passed": acceptance_summary.get(
            "correspondence_requirements_passed"
        ),
        "acceptance_non_claims_passed": acceptance_summary.get("non_claims_passed"),
        "scope_boundary_passed": scope_summary.get("scope_boundary_passed"),
        "scope_limits_passed": scope_summary.get("scope_limits_passed"),
        "scope_hierarchy_constraints_passed": scope_summary.get(
            "hierarchy_constraints_passed"
        ),
        "scope_correspondence_requirements_passed": scope_summary.get(
            "correspondence_requirements_passed"
        ),
        "scope_non_claims_passed": scope_summary.get("non_claims_passed"),
        "accepted_signal_remains": {
            "non_authoritative": accepted.get("non_authoritative") is True,
            "non_permission": accepted.get("non_permission") is True,
            "non_currentness": accepted.get("non_currentness") is True,
            "not_scoped": accepted.get("not_scoped_yet") is True,
            "not_present": accepted.get("not_present_yet") is True,
            "not_threshold": accepted.get("not_threshold_yet") is True,
            "not_truth": accepted.get("not_truth") is True,
            "no_action": accepted.get("no_action") is True,
            "no_follow_on_work": acceptance_result.get("non_claims", {}).get(
                "follow_on_work_authorized"
            )
            is False
            if isinstance(acceptance_result.get("non_claims"), Mapping)
            else False,
            "no_routing": accepted.get("no_routing") is True,
            "no_workflow": accepted.get("no_workflow") is True,
            "no_body_relevance_medium": accepted.get("no_body_relevance_medium") is True,
        },
        "scoped_signal_remains": {
            "non_authoritative": scoped.get("non_authoritative") is True,
            "non_permission": scoped.get("non_permission") is True,
            "non_currentness": scoped.get("non_currentness") is True,
            "not_present": scoped.get("not_present_yet") is True,
            "not_threshold": scoped.get("not_threshold_yet") is True,
            "not_truth": scoped.get("not_truth") is True,
            "no_action": scoped.get("no_action") is True,
            "no_follow_on_work": scope_result.get("non_claims", {}).get(
                "follow_on_work_authorized"
            )
            is False
            if isinstance(scope_result.get("non_claims"), Mapping)
            else False,
            "no_routing": scoped.get("no_routing") is True,
            "no_workflow": scoped.get("no_workflow") is True,
            "no_body_relevance_medium": scoped.get("no_body_relevance_medium") is True,
            "no_application_outside_declared_scope": scoped.get(
                "no_application_outside_declared_scope"
            )
            is True,
        },
        "body_signal_surfaces_remain_downstream": True,
        "body_signal_surfaces_create_authority": False,
        "body_signal_surfaces_create_permission": False,
        "body_signal_surfaces_create_currentness": False,
        "body_signal_scope_creates_authority": False,
        "body_signal_scope_creates_permission": False,
        "body_signal_scope_creates_currentness": False,
    }


def _result_id(selected_inputs: Mapping[str, Any], outcome: str) -> str:
    selected_body = selected_inputs.get("selected_body_pass_result")
    body_id = (
        selected_body.get("result_id")
        if isinstance(selected_body, Mapping)
        else None
    )
    base = _string_or_none(body_id) or "no_selected_body_pass_result"
    suffix = "current_self_orientation_v5_self_oriented"
    if outcome == OUTCOME_BLOCKED:
        suffix = "current_self_orientation_v5_blocked"
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
        "selected_self_orientation_v3_result": {},
        "selected_self_orientation_v4_result": {},
        "selected_reentry_admissibility_result": {},
        "selected_reentry_receipt_result": {},
        "selected_body_signal_recognition_result": {},
        "selected_blocked_body_signal_recognition_result": {},
        "selected_body_signal_acceptance_result": {},
        "selected_body_signal_scope_result": {},
        "selection_scope": {
            "body_pass_anchor_required": True,
            "self_orientation_v4_is_predecessor_recognition": True,
            "reentry_surfaces_are_downstream_only": True,
            "body_signal_surfaces_are_downstream_only": True,
            "body_signal_scope_surface_is_downstream_only": True,
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
    recognized_body_signal_surfaces: Mapping[str, Any] | None = None,
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
        "current_self_orientation_v5_metadata": _metadata(selected_inputs, outcome),
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
        "recognized_body_signal_surfaces": _bounded_section(
            recognized_body_signal_surfaces,
            "recognized_body_signal_surfaces",
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


def _predecessor_section(
    predecessor_result: Mapping[str, Any] | None,
    key: str,
) -> Mapping[str, Any]:
    if not isinstance(predecessor_result, Mapping):
        return {}
    value = predecessor_result.get(key)
    return value if isinstance(value, Mapping) else {}


def _blocked_result(
    *,
    block_code: str,
    block_detail: str | None = None,
    selected_inputs: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    predecessor_result: Mapping[str, Any] | None = None,
    recognized_body_signal_surfaces: Mapping[str, Any] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    selected = selected_inputs if isinstance(selected_inputs, Mapping) else _empty_selected_inputs()
    return _build_result(
        selected_inputs=selected,
        recognized_current_executable_core_line=_predecessor_section(
            predecessor_result,
            "recognized_current_executable_core_line",
        ),
        recognized_governing_effective_basis=_predecessor_section(
            predecessor_result,
            "recognized_governing_effective_basis",
        ),
        recognized_current_state_surfaces=_predecessor_section(
            predecessor_result,
            "recognized_current_state_surfaces",
        ),
        recognized_continuity_surfaces=_predecessor_section(
            predecessor_result,
            "recognized_continuity_surfaces",
        ),
        recognized_derivative_surfaces=_predecessor_section(
            predecessor_result,
            "recognized_derivative_surfaces",
        ),
        recognized_operator_facing_surfaces=_predecessor_section(
            predecessor_result,
            "recognized_operator_facing_surfaces",
        ),
        recognized_reentry_surfaces=_predecessor_section(
            predecessor_result,
            "recognized_reentry_surfaces",
        ),
        recognized_body_signal_surfaces=recognized_body_signal_surfaces or {},
        recognized_open_surfaces=_predecessor_section(
            predecessor_result,
            "recognized_open_surfaces",
        ),
        recognized_blocked_or_refused_surfaces=_predecessor_section(
            predecessor_result,
            "recognized_blocked_or_refused_surfaces",
        ),
        recognized_touch_admissibility_surfaces=_predecessor_section(
            predecessor_result,
            "recognized_touch_admissibility_surfaces",
        ),
        checks=checks or [],
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_detail=block_detail,
        self_orientation_basis={
            "basis_kind": "blocked_v5_self_orientation_preserving_selected_basis",
            "body_signal_surfaces_remain_downstream": True,
            "self_orientation_creates_authority": False,
            "signal_recognition_creates_permission": False,
            "signal_acceptance_creates_permission": False,
            "signal_scope_creates_permission": False,
        },
        non_claims=non_claims or NON_CLAIM_DEFAULTS,
    )


def _as_check_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [dict(item) for item in value if isinstance(item, Mapping)]


def _resolve(
    body_pass_result: Mapping[str, Any] | None = None,
    body_pass_result_path: Path | str | None = None,
) -> dict[str, Any]:
    body_path, body_artifact, body_selection_mode = _select_body_pass(
        body_pass_result,
        body_pass_result_path,
    )
    body_identity = _body_pass_identity(body_artifact, body_path, body_selection_mode)
    selected_inputs = _empty_selected_inputs()
    selected_inputs["selected_body_pass_result"] = body_identity

    v4_path, v4_result, v4_selection_mode = _select_matching_self_orientation_v4(
        body_identity
    )
    v4_identity = _self_orientation_v4_identity(v4_result, v4_path, v4_selection_mode)
    v4_selected_inputs = _require_mapping(
        v4_result.get("selected_orientation_inputs"),
        "selected_orientation_inputs",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    selected_inputs = copy.deepcopy(dict(v4_selected_inputs))
    selected_inputs["selected_self_orientation_v4_result"] = dict(v4_identity)

    recognition_path, recognition_result, recognition_identity, _ = (
        _select_matching_body_signal_recognition(body_identity)
    )
    recognition_identity = _body_signal_recognition_identity(
        recognition_result,
        recognition_path,
        "matching_body_signal_recognition_v2_discovery",
    )

    blocked_match = _select_blocked_false_permission_signal(body_identity)
    if blocked_match is not None:
        blocked_path, blocked_result, blocked_identity, _ = blocked_match
        blocked_identity = _body_signal_recognition_identity(
            blocked_result,
            blocked_path,
            "matching_blocked_permission_signal_discovery",
        )
    else:
        blocked_result = None
        blocked_identity = None

    acceptance_path, acceptance_result, acceptance_identity, _ = (
        _select_matching_body_signal_acceptance(recognition_identity)
    )
    acceptance_identity = _body_signal_acceptance_identity(
        acceptance_result,
        acceptance_path,
        "matching_body_signal_acceptance_discovery",
    )

    scope_path, scope_result, scope_identity, _ = _select_matching_body_signal_scope(
        acceptance_identity,
        recognition_identity,
    )
    scope_identity = _body_signal_scope_identity(
        scope_result,
        scope_path,
        "matching_body_signal_scope_discovery",
    )

    selected_inputs = _selected_inputs_with_signal_line(
        v4_result,
        v4_identity,
        recognition_identity,
        blocked_identity,
        acceptance_identity,
        scope_identity,
    )

    body_signal_checks = _build_body_signal_checks(
        body_identity,
        recognition_identity,
        recognition_result,
        blocked_identity,
        blocked_result,
        acceptance_identity,
        acceptance_result,
        scope_identity,
        scope_result,
    )
    checks = [
        *_as_check_list(v4_result.get("bounded_correspondence_checks")),
        _check(
            "v4_self_orientation_is_self_oriented",
            v4_result.get("outcome") == OUTCOME_SELF_ORIENTED,
            expected=OUTCOME_SELF_ORIENTED,
            actual=v4_result.get("outcome"),
            block_code="NO_SELF_ORIENTATION_SOURCE_BASIS",
        ),
        _check(
            "v4_selected_body_pass_matches_anchor",
            _body_pass_matches(_selected_body_pass_from_orientation(v4_result), body_identity),
            expected=body_identity,
            actual=_selected_body_pass_from_orientation(v4_result),
            block_code="CORRESPONDENCE_CHECK_FAILED",
        ),
        _check(
            "body_signal_surfaces_do_not_establish_current_or_governing_basis",
            True,
            expected="current/effective/current-state surfaces remain upstream",
            actual="body-signal surfaces recognized downstream only",
            block_code="BODY_SIGNAL_SURFACE_TREATED_AS_CURRENT_OR_GOVERNING_BASIS",
        ),
        *body_signal_checks,
    ]

    non_claims = _merge_non_claims(
        v4_result,
        recognition_result,
        blocked_result,
        acceptance_result,
        scope_result,
    )
    body_signal_surfaces = _recognized_body_signal_surfaces(
        recognition_identity,
        recognition_result,
        blocked_identity,
        blocked_result,
        acceptance_identity,
        acceptance_result,
        scope_identity,
        scope_result,
    )
    failed = _first_failed(checks)
    if failed is not None:
        return _blocked_result(
            block_code=_string_or_none(failed.get("block_code")) or "CORRESPONDENCE_CHECK_FAILED",
            block_detail=f"failed check: {failed.get('check_name')}",
            selected_inputs=selected_inputs,
            checks=checks,
            predecessor_result=v4_result,
            recognized_body_signal_surfaces=body_signal_surfaces,
            non_claims=non_claims,
        )

    accepted = _accepted_signal(acceptance_result)
    scoped = _scoped_signal(scope_result)
    return _build_result(
        selected_inputs=selected_inputs,
        recognized_current_executable_core_line=v4_result.get(
            "recognized_current_executable_core_line"
        ),
        recognized_governing_effective_basis=v4_result.get(
            "recognized_governing_effective_basis"
        ),
        recognized_current_state_surfaces=v4_result.get("recognized_current_state_surfaces"),
        recognized_continuity_surfaces=v4_result.get("recognized_continuity_surfaces"),
        recognized_derivative_surfaces=v4_result.get("recognized_derivative_surfaces"),
        recognized_operator_facing_surfaces=v4_result.get(
            "recognized_operator_facing_surfaces"
        ),
        recognized_reentry_surfaces=v4_result.get("recognized_reentry_surfaces"),
        recognized_body_signal_surfaces=body_signal_surfaces,
        recognized_open_surfaces=v4_result.get("recognized_open_surfaces"),
        recognized_blocked_or_refused_surfaces=v4_result.get(
            "recognized_blocked_or_refused_surfaces"
        ),
        recognized_touch_admissibility_surfaces=v4_result.get(
            "recognized_touch_admissibility_surfaces"
        ),
        checks=checks,
        outcome=OUTCOME_SELF_ORIENTED,
        block_code=None,
        block_detail=None,
        self_orientation_basis={
            "basis_kind": "v4_self_orientation_plus_downstream_body_signal_scope",
            "selected_self_orientation_v4_result_id": v4_identity.get("result_id"),
            "selected_self_orientation_v4_result_path": v4_identity.get("result_path"),
            "selected_body_pass_result_id": body_identity.get("result_id"),
            "selected_body_pass_result_path": body_identity.get("result_path"),
            "selected_body_signal_recognition_result_id": recognition_identity.get(
                "result_id"
            ),
            "selected_body_signal_acceptance_result_id": acceptance_identity.get(
                "result_id"
            ),
            "selected_body_signal_scope_result_id": scope_identity.get("result_id"),
            "body_signal_recognition_recognized": True,
            "body_signal_acceptance_accepted": True,
            "body_signal_scope_scoped": True,
            "accepted_signal_category": accepted.get("accepted_signal_category"),
            "accepted_matter_id": accepted.get("declared_matter_id"),
            "scoped_signal_category": scoped.get("scoped_signal_category"),
            "declared_scope_id": scoped.get("declared_scope_id"),
            "body_signal_surfaces_remain_downstream": True,
            "signal_recognition_creates_authority": False,
            "signal_acceptance_creates_authority": False,
            "signal_scope_creates_authority": False,
            "recognized_signal_creates_permission": False,
            "accepted_signal_creates_permission": False,
            "scoped_signal_creates_permission": False,
            "scoped_signal_establishes_presence": False,
            "scoped_signal_meets_threshold": False,
            "scoped_signal_creates_truth": False,
            "scoped_signal_authorizes_action": False,
            "scoped_signal_authorizes_follow_on_work": False,
            "scoped_signal_routes": False,
            "scoped_signal_creates_workflow": False,
            "scoped_signal_creates_body_relevance_medium": False,
            "scoped_signal_applies_outside_declared_scope": False,
            "self_orientation_creates_authority": False,
        },
        non_claims=non_claims,
    )


def resolve_current_self_orientation(
    body_pass_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded v5 self-orientation result."""

    try:
        return _resolve(body_pass_result=body_pass_result)
    except CurrentSelfOrientationV5Error as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            selected_inputs=exc.selected_inputs,
            checks=exc.checks,
        )


def resolve_current_self_orientation_from_path(
    body_pass_result_path: Path | str,
) -> dict[str, Any]:
    """Resolve one bounded v5 self-orientation result from a body-pass path."""

    selected_inputs = _empty_selected_inputs()
    selected_inputs["selected_body_pass_result"] = {
        "result_path": _display_path(body_pass_result_path),
        "selection_mode": "explicit_body_pass_result_path",
    }
    try:
        return _resolve(body_pass_result_path=body_pass_result_path)
    except CurrentSelfOrientationV5Error as exc:
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
    """Build a bounded v5 self-orientation summary."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationV5Error(
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
    v3 = selected.get("selected_self_orientation_v3_result")
    v3 = v3 if isinstance(v3, Mapping) else {}
    v4 = selected.get("selected_self_orientation_v4_result")
    v4 = v4 if isinstance(v4, Mapping) else {}
    admission = selected.get("selected_reentry_admissibility_result")
    admission = admission if isinstance(admission, Mapping) else {}
    receipt = selected.get("selected_reentry_receipt_result")
    receipt = receipt if isinstance(receipt, Mapping) else {}
    recognition = selected.get("selected_body_signal_recognition_result")
    recognition = recognition if isinstance(recognition, Mapping) else {}
    acceptance = selected.get("selected_body_signal_acceptance_result")
    acceptance = acceptance if isinstance(acceptance, Mapping) else {}
    scope = selected.get("selected_body_signal_scope_result")
    scope = scope if isinstance(scope, Mapping) else {}
    body_signal = result.get("recognized_body_signal_surfaces")
    body_signal = body_signal if isinstance(body_signal, Mapping) else {}
    accepted = body_signal.get("accepted_signal")
    accepted = accepted if isinstance(accepted, Mapping) else {}
    scoped = body_signal.get("scoped_signal")
    scoped = scoped if isinstance(scoped, Mapping) else {}
    accepted_remains = body_signal.get("accepted_signal_remains")
    accepted_remains = accepted_remains if isinstance(accepted_remains, Mapping) else {}
    scoped_remains = body_signal.get("scoped_signal_remains")
    scoped_remains = scoped_remains if isinstance(scoped_remains, Mapping) else {}
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
        "selected_self_orientation_v3_result_id": v3.get("result_id"),
        "selected_self_orientation_v4_result_id": v4.get("result_id"),
        "selected_reentry_admissibility_result_id": admission.get("result_id"),
        "selected_reentry_receipt_result_id": receipt.get("result_id"),
        "selected_body_signal_recognition_result_id": recognition.get("result_id"),
        "selected_body_signal_acceptance_result_id": acceptance.get("result_id"),
        "selected_body_signal_scope_result_id": scope.get("result_id"),
        "current_executable_core_line_recognized": _summary_bool(
            result.get("recognized_current_executable_core_line")
        ),
        "governing_effective_basis_recognized": _summary_bool(
            result.get("recognized_governing_effective_basis")
        ),
        "current_state_surfaces_recognized": _summary_bool(
            result.get("recognized_current_state_surfaces")
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
        "reentry_surfaces_recognized": _summary_bool(
            result.get("recognized_reentry_surfaces")
        ),
        "body_signal_surfaces_recognized": _summary_bool(body_signal),
        "body_signal_recognition_recognized": recognition.get("outcome")
        == OUTCOME_SIGNAL_RECOGNIZED,
        "body_signal_acceptance_accepted": acceptance.get("outcome")
        == OUTCOME_SIGNAL_ACCEPTED,
        "body_signal_scope_scoped": scope.get("outcome") == OUTCOME_SIGNAL_SCOPED,
        "accepted_signal_category": accepted.get("accepted_signal_category"),
        "accepted_matter_id": accepted.get("declared_matter_id"),
        "scoped_signal_category": scoped.get("scoped_signal_category"),
        "declared_scope_id": scoped.get("declared_scope_id"),
        "accepted_signal_remains_non_authoritative": accepted_remains.get(
            "non_authoritative"
        )
        is True,
        "accepted_signal_remains_non_permission": accepted_remains.get(
            "non_permission"
        )
        is True,
        "accepted_signal_remains_non_currentness": accepted_remains.get(
            "non_currentness"
        )
        is True,
        "accepted_signal_remains_not_scoped": accepted_remains.get("not_scoped")
        is True,
        "accepted_signal_remains_not_present": accepted_remains.get("not_present")
        is True,
        "accepted_signal_remains_not_threshold": accepted_remains.get("not_threshold")
        is True,
        "accepted_signal_remains_not_truth": accepted_remains.get("not_truth")
        is True,
        "accepted_signal_remains_no_action": accepted_remains.get("no_action") is True,
        "accepted_signal_remains_no_routing": accepted_remains.get("no_routing")
        is True,
        "accepted_signal_remains_no_workflow": accepted_remains.get("no_workflow")
        is True,
        "accepted_signal_remains_no_body_relevance_medium": accepted_remains.get(
            "no_body_relevance_medium"
        )
        is True,
        "scoped_signal_remains_non_authoritative": scoped_remains.get(
            "non_authoritative"
        )
        is True,
        "scoped_signal_remains_non_permission": scoped_remains.get("non_permission")
        is True,
        "scoped_signal_remains_non_currentness": scoped_remains.get("non_currentness")
        is True,
        "scoped_signal_remains_not_present": scoped_remains.get("not_present") is True,
        "scoped_signal_remains_not_threshold": scoped_remains.get("not_threshold")
        is True,
        "scoped_signal_remains_not_truth": scoped_remains.get("not_truth") is True,
        "scoped_signal_remains_no_action": scoped_remains.get("no_action") is True,
        "scoped_signal_remains_no_routing": scoped_remains.get("no_routing") is True,
        "scoped_signal_remains_no_workflow": scoped_remains.get("no_workflow") is True,
        "scoped_signal_remains_no_body_relevance_medium": scoped_remains.get(
            "no_body_relevance_medium"
        )
        is True,
        "scoped_signal_remains_no_application_outside_declared_scope": scoped_remains.get(
            "no_application_outside_declared_scope"
        )
        is True,
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
                "signal_recognition_became_authority",
                "signal_acceptance_became_authority",
                "signal_scope_became_authority",
                "signal_surface_became_current_or_governing_basis",
                "recognized_signal_became_permission",
                "accepted_signal_became_permission",
                "accepted_signal_became_scope",
                "accepted_signal_became_presence",
                "accepted_signal_became_threshold",
                "accepted_signal_became_truth",
                "accepted_signal_became_action",
                "accepted_signal_became_routing",
                "accepted_signal_became_workflow",
                "accepted_signal_became_body_relevance_medium",
                "scoped_signal_became_permission",
                "scoped_signal_became_presence",
                "scoped_signal_became_threshold",
                "scoped_signal_became_truth",
                "scoped_signal_became_action",
                "scoped_signal_became_routing",
                "scoped_signal_became_workflow",
                "scoped_signal_became_body_relevance_medium",
                "scoped_signal_applied_outside_declared_scope",
                "body_signal_line_became_action_or_continuation",
                "latest_file_currentness",
                "recency_fraud",
                "mutation_performed",
                "replay_performed",
                "merge_performed",
                "roadmap_generated",
                "workflow_engine_created",
                "event_bus_created",
                "signal_router_created",
                "body_relevance_medium_created",
            )
            if key in non_claims
        },
    }


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = CURRENT_SELF_ORIENTATION_V5_ROOT,
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
    raise CurrentSelfOrientationV5Error(
        "no bounded current self-orientation v5 filename is available",
        "SOURCE_ARTIFACT_MALFORMED",
    )


def write_current_self_orientation_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive v5 self-orientation JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationV5Error(
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
        raise FileExistsError(f"current self-orientation v5 result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
