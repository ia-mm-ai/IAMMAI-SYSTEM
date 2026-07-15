"""Resolve distributed synchronization / non-synchronization boundary posture.

This module records which synchronization and non-synchronization postures may
be recognized as bounded context before any future operation admission. It does
not authorize repository synchronization, create shared live state, authorize
state merge or replay, transfer a body, create a second body, authorize
non-synchronized operation, activate carrier roles, admit operation, authorize
operation, execute operation, create consequence, create public readiness, claim
final completion, or schedule follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class DistributedSynchronizationNonSynchronizationBoundaryError(Exception):
    """Raised for impossible distributed sync/non-sync boundary failures."""


RESOLVER_MODULE = "resolve_distributed_synchronization_non_synchronization_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "distributed_synchronization_non_synchronization_boundary_result"
REPO_ROOT = Path(__file__).resolve().parents[1]
DISTRIBUTED_SYNCHRONIZATION_NON_SYNCHRONIZATION_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_distributed_synchronization_non_synchronization_boundary"
)

INTENT_RECORD = "RECORD_DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_SYNC_NON_SYNC_REVIEW"
SUPPORTED_SYNC_NON_SYNC_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

OUTCOME_RECORDED = "DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY_RECORDED"
OUTCOME_NOT_SUFFICIENT = "DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY_NOT_SUFFICIENT"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DISTRIBUTED_SYNC_NON_SYNC_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_SYNC_NON_SYNC_REVIEW_BLOCKED"
SUPPORTED_SYNC_NON_SYNC_OUTCOMES = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_SUFFICIENT,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

EXPECTED_CARRIER_ROLE_OUTCOME = "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS_RECORDED"
EXPECTED_FAILED_CHECK_COUNT = 0

SUPPORTED_SYNC_NON_SYNC_POSTURES = {
    "NO_REPOSITORY_SYNCHRONIZATION_BY_DEFAULT",
    "NO_SHARED_LIVE_STATE_BY_DEFAULT",
    "NO_STATE_MERGE_BY_DEFAULT",
    "NO_FULL_BODY_TRANSFER_BY_DEFAULT",
    "NO_SECOND_BODY_BY_DEFAULT",
    "CARRIER_EVIDENCE_REMAINS_UNMERGED",
    "CARRIER_CONTEXT_REMAINS_CONTEXT_ONLY",
    "DIVERGENCE_REMAINS_VISIBLE",
    "REFUSAL_REMAINS_VISIBLE",
    "BLOCKED_ATTEMPTS_REMAIN_VISIBLE",
    "PROJECTION_MISMATCH_REMAINS_VISIBLE",
    "FUTURE_SYNCHRONIZATION_REQUIRES_SEPARATE_BOUNDARY",
    "FUTURE_NON_SYNCHRONIZED_OPERATION_REQUIRES_SEPARATE_ADMISSION",
}

SUPPORTED_CARRIER_ROLE_SHAPES = {
    "SOURCE_BODY_REFERENCE_CONTEXT",
    "EVIDENCE_CARRIER_CONTEXT",
    "RECEIVING_CARRIER_CONTEXT",
    "RETURNED_EVIDENCE_CARRIER_CONTEXT",
    "BLOCKED_OR_REFUSAL_CARRIER_CONTEXT",
    "DIVERGENCE_CONTEXT_CARRIER",
    "OBSERVING_CARRIER_CONTEXT",
    "CANDIDATE_CARRIER_CONTEXT",
    "NON_OPERATIONAL_CONTEXT_CARRIER",
    "FUTURE_OPERATIONAL_ROLE_REQUIRES_ADMISSION",
}

BLOCK_SYNC_NON_SYNC_QUESTION_UNDECLARED = "SYNC_NON_SYNC_QUESTION_UNDECLARED"
BLOCK_SYNC_NON_SYNC_INTENT_UNSUPPORTED = "SYNC_NON_SYNC_INTENT_UNSUPPORTED"
BLOCK_CARRIER_ROLE_RESULT_MISSING = "CARRIER_ROLE_RESULT_MISSING"
BLOCK_CARRIER_ROLE_RESULT_UNREADABLE = "CARRIER_ROLE_RESULT_UNREADABLE"
BLOCK_CARRIER_ROLE_RESULT_MALFORMED = "CARRIER_ROLE_RESULT_MALFORMED"
BLOCK_CARRIER_ROLE_RESULT_OUTCOME_MISSING = "CARRIER_ROLE_RESULT_OUTCOME_MISSING"
BLOCK_CARRIER_ROLE_RESULT_NOT_RECORDED = "CARRIER_ROLE_RESULT_NOT_RECORDED"
BLOCK_CARRIER_ROLE_RESULT_HAS_FAILED_CHECKS = (
    "CARRIER_ROLE_RESULT_HAS_FAILED_CHECKS"
)
BLOCK_SOURCE_BODY_AUTHORITY_RESULT_MISSING = "SOURCE_BODY_AUTHORITY_RESULT_MISSING"
BLOCK_SELECTED_ELIGIBILITY_RESULT_MISSING = "SELECTED_ELIGIBILITY_RESULT_MISSING"
BLOCK_SELECTED_MATTER_DECLARATION_MISSING = "SELECTED_MATTER_DECLARATION_MISSING"
BLOCK_SELECTED_OPERATION_CANDIDATE_MISSING = "SELECTED_OPERATION_CANDIDATE_MISSING"
BLOCK_SELECTED_OPERATION_MATTER_MISSING = "SELECTED_OPERATION_MATTER_MISSING"
BLOCK_CARRIER_ROLE_BASIS_MISSING = "CARRIER_ROLE_BASIS_MISSING"
BLOCK_CARRIER_ROLE_SHAPES_MISSING = "CARRIER_ROLE_SHAPES_MISSING"
BLOCK_SELECTED_CARRIER_CONTEXT_MALFORMED = "SELECTED_CARRIER_CONTEXT_MALFORMED"
BLOCK_UNSUPPORTED_SYNC_NON_SYNC_POSTURE = "UNSUPPORTED_SYNC_NON_SYNC_POSTURE"
BLOCK_SYNC_REVIEW_AUTHORIZES_REPOSITORY_SYNC = (
    "SYNC_REVIEW_AUTHORIZES_REPOSITORY_SYNC"
)
BLOCK_SYNC_REVIEW_CREATES_SHARED_LIVE_STATE = (
    "SYNC_REVIEW_CREATES_SHARED_LIVE_STATE"
)
BLOCK_SYNC_REVIEW_AUTHORIZES_STATE_MERGE = "SYNC_REVIEW_AUTHORIZES_STATE_MERGE"
BLOCK_SYNC_REVIEW_AUTHORIZES_REPLAY = "SYNC_REVIEW_AUTHORIZES_REPLAY"
BLOCK_SYNC_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER = (
    "SYNC_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER"
)
BLOCK_SYNC_REVIEW_CREATES_SECOND_BODY = "SYNC_REVIEW_CREATES_SECOND_BODY"
BLOCK_NON_SYNC_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION = (
    "NON_SYNC_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION"
)
BLOCK_NON_SYNC_REVIEW_AUTHORIZES_CARRIER_AUTONOMY = (
    "NON_SYNC_REVIEW_AUTHORIZES_CARRIER_AUTONOMY"
)
BLOCK_NON_SYNC_REVIEW_AUTHORIZES_STALE_CARRIER_OPERATION = (
    "NON_SYNC_REVIEW_AUTHORIZES_STALE_CARRIER_OPERATION"
)
BLOCK_SYNC_NON_SYNC_REVIEW_ADMITS_OPERATION = (
    "SYNC_NON_SYNC_REVIEW_ADMITS_OPERATION"
)
BLOCK_SYNC_NON_SYNC_REVIEW_AUTHORIZES_OPERATION = (
    "SYNC_NON_SYNC_REVIEW_AUTHORIZES_OPERATION"
)
BLOCK_SYNC_NON_SYNC_REVIEW_EXECUTES_OPERATION = (
    "SYNC_NON_SYNC_REVIEW_EXECUTES_OPERATION"
)
BLOCK_SYNC_NON_SYNC_REVIEW_ACTIVATES_CARRIER_ROLES = (
    "SYNC_NON_SYNC_REVIEW_ACTIVATES_CARRIER_ROLES"
)
BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_AUTHORITY = (
    "SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_AUTHORITY"
)
BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_PERMISSION = (
    "SYNC_NON_SYNC_REVIEW_CREATES_PERMISSION"
)
BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_CURRENTNESS = (
    "SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_CURRENTNESS"
)
BLOCK_SYNC_NON_SYNC_REVIEW_SELECTS_CURRENT_CARRIER = (
    "SYNC_NON_SYNC_REVIEW_SELECTS_CURRENT_CARRIER"
)
BLOCK_SYNC_NON_SYNC_REVIEW_SELECTS_WINNING_CARRIER = (
    "SYNC_NON_SYNC_REVIEW_SELECTS_WINNING_CARRIER"
)
BLOCK_SYNC_NON_SYNC_REVIEW_INVALIDATES_LOSING_CARRIER = (
    "SYNC_NON_SYNC_REVIEW_INVALIDATES_LOSING_CARRIER"
)
BLOCK_SYNC_NON_SYNC_REVIEW_REPLACES_SOURCE = (
    "SYNC_NON_SYNC_REVIEW_REPLACES_SOURCE"
)
BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_TRUTH_OR_ACTION = (
    "SYNC_NON_SYNC_REVIEW_CREATES_TRUTH_OR_ACTION"
)
BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_CONSEQUENCE = (
    "SYNC_NON_SYNC_REVIEW_CREATES_CONSEQUENCE"
)
BLOCK_SYNC_NON_SYNC_REVIEW_RESOLVES_DIVERGENCE = (
    "SYNC_NON_SYNC_REVIEW_RESOLVES_DIVERGENCE"
)
BLOCK_SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL = (
    "SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"
)
BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_PUBLIC_READINESS = (
    "SYNC_NON_SYNC_REVIEW_CREATES_PUBLIC_READINESS"
)
BLOCK_SYNC_NON_SYNC_REVIEW_CLAIMS_FINAL_COMPLETION = (
    "SYNC_NON_SYNC_REVIEW_CLAIMS_FINAL_COMPLETION"
)
BLOCK_SYNC_NON_SYNC_REVIEW_SCHEDULES_FOLLOW_ON_WORK = (
    "SYNC_NON_SYNC_REVIEW_SCHEDULES_FOLLOW_ON_WORK"
)
BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED = "MUTATION_REPLAY_OR_MERGE_DETECTED"
BLOCK_NON_CLAIM_MISSING_OR_FLIPPED = "NON_CLAIM_MISSING_OR_FLIPPED"
BLOCK_DECLARED_SYNC_NON_SYNC_REQUEST_UNREADABLE = (
    "DECLARED_SYNC_NON_SYNC_REQUEST_UNREADABLE"
)
BLOCK_DECLARED_SYNC_NON_SYNC_REQUEST_MALFORMED = (
    "DECLARED_SYNC_NON_SYNC_REQUEST_MALFORMED"
)
BLOCK_SYNC_NON_SYNC_REVIEW_REQUEST_EXPLICITLY_BLOCKED = (
    "SYNC_NON_SYNC_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
)

REQUIRED_NON_CLAIMS = {
    "repository_synchronization_authorized": False,
    "shared_live_state_created": False,
    "state_merge_authorized": False,
    "replay_authorized": False,
    "full_body_transfer_authorized": False,
    "second_body_created": False,
    "non_synchronized_operation_authorized": False,
    "carrier_autonomy_authorized": False,
    "stale_carrier_operation_authorized": False,
    "carrier_role_activated": False,
    "carrier_role_assigned_for_operation": False,
    "carrier_authority_created": False,
    "carrier_currentness_created": False,
    "current_carrier_selected": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "carrier_hierarchy_created": False,
    "source_replaced": False,
    "authority_created": False,
    "permission_created": False,
    "operation_admitted": False,
    "operation_authorized": False,
    "operation_executed": False,
    "continuation_authorized": False,
    "distributed_operation_authorized": False,
    "truth_created": False,
    "action_authorized": False,
    "consequence_created": False,
    "divergence_resolved": False,
    "evidence_erased": False,
    "refusal_erased": False,
    "blocked_attempt_erased": False,
    "projection_mismatch_hidden": False,
    "public_launch_readiness_created": False,
    "final_completion_claimed": False,
    "follow_on_work_authorized": False,
    "self_orientation_successor_scheduled": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

CARRIER_ROLE_NON_CLAIM_FIELDS = (
    "carrier_role_activated",
    "carrier_roles_activated",
    "carrier_role_assigned_for_operation",
    "carrier_roles_assigned_for_operation",
    "carrier_authority_created",
    "carrier_currentness_created",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "carrier_hierarchy_created",
    "source_replaced",
    "authority_created",
    "permission_created",
    "operation_admitted",
    "operation_authorized",
    "operation_executed",
    "repository_synchronization_authorized",
    "full_body_transfer_authorized",
    "second_body_created",
    "continuation_authorized",
    "distributed_operation_authorized",
    "truth_created",
    "action_authorized",
    "consequence_created",
    "divergence_resolved",
    "evidence_erased",
    "refusal_erased",
    "blocked_attempt_erased",
    "projection_mismatch_hidden",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "follow_on_work_authorized",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

SYNC_NON_SYNC_COLLAPSE_FIELDS = (
    (
        "repository_synchronization_authorized",
        BLOCK_SYNC_REVIEW_AUTHORIZES_REPOSITORY_SYNC,
    ),
    ("repository_sync_authorized", BLOCK_SYNC_REVIEW_AUTHORIZES_REPOSITORY_SYNC),
    ("sync_authorized", BLOCK_SYNC_REVIEW_AUTHORIZES_REPOSITORY_SYNC),
    ("synchronization_authorized", BLOCK_SYNC_REVIEW_AUTHORIZES_REPOSITORY_SYNC),
    ("shared_live_state_created", BLOCK_SYNC_REVIEW_CREATES_SHARED_LIVE_STATE),
    ("shared_live_state_authorized", BLOCK_SYNC_REVIEW_CREATES_SHARED_LIVE_STATE),
    ("synchronized_state_created", BLOCK_SYNC_REVIEW_CREATES_SHARED_LIVE_STATE),
    ("state_merge_authorized", BLOCK_SYNC_REVIEW_AUTHORIZES_STATE_MERGE),
    ("state_merge_permission_created", BLOCK_SYNC_REVIEW_AUTHORIZES_STATE_MERGE),
    ("repository_merge_authorized", BLOCK_SYNC_REVIEW_AUTHORIZES_STATE_MERGE),
    ("replay_authorized", BLOCK_SYNC_REVIEW_AUTHORIZES_REPLAY),
    ("source_replay_authorized", BLOCK_SYNC_REVIEW_AUTHORIZES_REPLAY),
    ("full_body_transfer_authorized", BLOCK_SYNC_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER),
    ("full_body_transfer_created", BLOCK_SYNC_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER),
    ("second_body_created", BLOCK_SYNC_REVIEW_CREATES_SECOND_BODY),
    ("second_body_authorized", BLOCK_SYNC_REVIEW_CREATES_SECOND_BODY),
    (
        "non_synchronized_operation_authorized",
        BLOCK_NON_SYNC_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION,
    ),
    (
        "non_sync_operation_authorized",
        BLOCK_NON_SYNC_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION,
    ),
    (
        "divergent_live_operation_authorized",
        BLOCK_NON_SYNC_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION,
    ),
    ("carrier_autonomy_authorized", BLOCK_NON_SYNC_REVIEW_AUTHORIZES_CARRIER_AUTONOMY),
    (
        "unsupervised_carrier_autonomy_authorized",
        BLOCK_NON_SYNC_REVIEW_AUTHORIZES_CARRIER_AUTONOMY,
    ),
    (
        "stale_carrier_operation_authorized",
        BLOCK_NON_SYNC_REVIEW_AUTHORIZES_STALE_CARRIER_OPERATION,
    ),
    ("operation_admitted", BLOCK_SYNC_NON_SYNC_REVIEW_ADMITS_OPERATION),
    ("operation_authorized", BLOCK_SYNC_NON_SYNC_REVIEW_AUTHORIZES_OPERATION),
    (
        "distributed_operation_authorized",
        BLOCK_SYNC_NON_SYNC_REVIEW_AUTHORIZES_OPERATION,
    ),
    ("operation_executed", BLOCK_SYNC_NON_SYNC_REVIEW_EXECUTES_OPERATION),
    ("carrier_role_activated", BLOCK_SYNC_NON_SYNC_REVIEW_ACTIVATES_CARRIER_ROLES),
    ("carrier_roles_activated", BLOCK_SYNC_NON_SYNC_REVIEW_ACTIVATES_CARRIER_ROLES),
    (
        "role_review_activates_carrier_role",
        BLOCK_SYNC_NON_SYNC_REVIEW_ACTIVATES_CARRIER_ROLES,
    ),
    (
        "carrier_role_assigned_for_operation",
        BLOCK_SYNC_NON_SYNC_REVIEW_ACTIVATES_CARRIER_ROLES,
    ),
    (
        "carrier_roles_assigned_for_operation",
        BLOCK_SYNC_NON_SYNC_REVIEW_ACTIVATES_CARRIER_ROLES,
    ),
    ("carrier_authority_created", BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_AUTHORITY),
    ("carrier_becomes_authority", BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_AUTHORITY),
    ("authority_created", BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_AUTHORITY),
    ("permission_created", BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_PERMISSION),
    (
        "carrier_currentness_created",
        BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_CURRENTNESS,
    ),
    (
        "carrier_becomes_currentness",
        BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_CURRENTNESS,
    ),
    ("current_carrier_selected", BLOCK_SYNC_NON_SYNC_REVIEW_SELECTS_CURRENT_CARRIER),
    ("carrier_becomes_current", BLOCK_SYNC_NON_SYNC_REVIEW_SELECTS_CURRENT_CARRIER),
    ("latest_carrier_becomes_current", BLOCK_SYNC_NON_SYNC_REVIEW_SELECTS_CURRENT_CARRIER),
    ("winning_carrier_selected", BLOCK_SYNC_NON_SYNC_REVIEW_SELECTS_WINNING_CARRIER),
    ("latest_carrier_wins", BLOCK_SYNC_NON_SYNC_REVIEW_SELECTS_WINNING_CARRIER),
    ("carrier_b_success_becomes_winner", BLOCK_SYNC_NON_SYNC_REVIEW_SELECTS_WINNING_CARRIER),
    (
        "losing_carrier_invalidated",
        BLOCK_SYNC_NON_SYNC_REVIEW_INVALIDATES_LOSING_CARRIER,
    ),
    (
        "carrier_c_block_becomes_loser",
        BLOCK_SYNC_NON_SYNC_REVIEW_INVALIDATES_LOSING_CARRIER,
    ),
    ("source_replaced", BLOCK_SYNC_NON_SYNC_REVIEW_REPLACES_SOURCE),
    ("source_replaced_by_carrier", BLOCK_SYNC_NON_SYNC_REVIEW_REPLACES_SOURCE),
    ("carrier_becomes_source", BLOCK_SYNC_NON_SYNC_REVIEW_REPLACES_SOURCE),
    ("truth_created", BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_TRUTH_OR_ACTION),
    ("action_authorized", BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_TRUTH_OR_ACTION),
    ("consequence_created", BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_CONSEQUENCE),
    ("divergence_resolved", BLOCK_SYNC_NON_SYNC_REVIEW_RESOLVES_DIVERGENCE),
    ("evidence_erased", BLOCK_SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("refusal_erased", BLOCK_SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("blocked_attempt_erased", BLOCK_SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("projection_mismatch_hidden", BLOCK_SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("refusal_hidden", BLOCK_SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("blocked_attempt_hidden", BLOCK_SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("b_c_divergence_hidden", BLOCK_SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    (
        "public_launch_readiness_created",
        BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_PUBLIC_READINESS,
    ),
    ("public_readiness_created", BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_PUBLIC_READINESS),
    ("final_completion_claimed", BLOCK_SYNC_NON_SYNC_REVIEW_CLAIMS_FINAL_COMPLETION),
    ("final_governance_completed", BLOCK_SYNC_NON_SYNC_REVIEW_CLAIMS_FINAL_COMPLETION),
    ("final_continuity_completed", BLOCK_SYNC_NON_SYNC_REVIEW_CLAIMS_FINAL_COMPLETION),
    (
        "final_system_identity_completed",
        BLOCK_SYNC_NON_SYNC_REVIEW_CLAIMS_FINAL_COMPLETION,
    ),
    (
        "follow_on_work_authorized",
        BLOCK_SYNC_NON_SYNC_REVIEW_SCHEDULES_FOLLOW_ON_WORK,
    ),
    (
        "self_orientation_successor_scheduled",
        BLOCK_SYNC_NON_SYNC_REVIEW_SCHEDULES_FOLLOW_ON_WORK,
    ),
    ("mutation_performed", BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED),
    ("replay_performed", BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED),
    ("merge_performed", BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED),
)

WHAT_REMAINS_OPEN = {
    "distributed_refusal_and_abort_law": "open_not_scheduled_not_authorized_not_executed",
    "distributed_operation_admission_transition_authority": (
        "open_not_scheduled_not_authorized_not_executed"
    ),
    "distributed_execution_emission_boundary": (
        "open_not_scheduled_not_authorized_not_executed"
    ),
    "distributed_action_consequence_boundary": (
        "open_not_scheduled_not_authorized_not_executed"
    ),
    "distributed_operation_receipt_exhaustion": (
        "open_not_scheduled_not_authorized_not_executed"
    ),
    "distributed_operation_conformance": "open_not_scheduled_not_authorized_not_executed",
    "distributed_operation_closure": "open_not_scheduled_not_authorized_not_executed",
    "distributed_operation_itself": "open_not_scheduled_not_authorized_not_executed",
    "repository_synchronization": "open_not_scheduled_not_authorized_not_executed",
    "non_synchronized_operation": "open_not_scheduled_not_authorized_not_executed",
    "full_body_transfer": "open_not_scheduled_not_authorized_not_executed",
    "second_body_creation": "open_not_scheduled_not_authorized_not_executed",
    "current_self_orientation_v10": "open_not_scheduled_not_authorized_not_executed",
    "public_launch_readiness": "open_not_scheduled_not_authorized_not_executed",
    "final_governance": "open_not_scheduled_not_authorized_not_executed",
    "final_continuity_completion": "open_not_scheduled_not_authorized_not_executed",
    "final_system_identity": "open_not_scheduled_not_authorized_not_executed",
    "open_means_not_scheduled": True,
    "open_means_not_authorized": True,
    "open_means_not_executed": True,
}


def _utc_now() -> str:
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat()


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    return {}


def _is_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return bool(value)


def _is_true(value: Any) -> bool:
    return value is True


def _get_path_value(value: Mapping[str, Any], path: Sequence[str], default: Any = None) -> Any:
    current: Any = value
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return default
        current = current[key]
    return current


def _first_present(*values: Any) -> Any:
    for value in values:
        if _is_non_empty(value):
            return value
    return None


def _stringify(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return str(value)


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None]:
    resolved = Path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except OSError:
        return None, "unreadable"
    except json.JSONDecodeError:
        return None, "malformed"
    if not isinstance(payload, Mapping):
        return None, "malformed"
    return dict(payload), None


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    block_code: str | None,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": None if passed else block_code,
        "failure_code": None if passed else block_code,
    }


def _passed_check_count(checks: Sequence[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is True)


def _failed_check_count(checks: Sequence[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is not True)


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if code:
                return _stringify(code)
    return None


def _sanitize_filename(value: Any) -> str:
    raw = _stringify(value).strip() or "distributed_sync_non_sync"
    allowed = []
    for character in raw:
        if character.isalnum() or character in {"-", "_", "."}:
            allowed.append(character)
        else:
            allowed.append("_")
    sanitized = "".join(allowed).strip("._")
    return sanitized[:180] or "distributed_sync_non_sync"


def _deduplicate_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    for index in range(1, 10000):
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
    raise DistributedSynchronizationNonSynchronizationBoundaryError(
        f"could not create unique output path for {path}"
    )


def _extract_failed_check_count(result: Mapping[str, Any]) -> int | None:
    summary_value = _first_present(
        _get_path_value(result, ("distributed_carrier_operational_role_summary", "failed_check_count")),
        _get_path_value(result, ("role_statement", "failed_check_count")),
    )
    if summary_value is None:
        checks = result.get("role_checks")
        if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray)):
            return _failed_check_count([check for check in checks if isinstance(check, Mapping)])
        return None
    try:
        return int(summary_value)
    except (TypeError, ValueError):
        return None


def _extract_carrier_role_result_id(result: Mapping[str, Any]) -> str | None:
    value = _first_present(
        _get_path_value(
            result,
            (
                "distributed_carrier_operational_role_metadata",
                "distributed_carrier_operational_role_result_id",
            ),
        ),
        _get_path_value(
            result,
            ("distributed_carrier_operational_role_summary", "role_request_id"),
        ),
        _get_path_value(result, ("declared_role_question", "role_request_id")),
        result.get("distributed_carrier_operational_role_result_id"),
        result.get("selected_carrier_role_result_id"),
    )
    return _stringify(value) if value is not None else None


def _extract_carrier_role_outcome(result: Mapping[str, Any]) -> str | None:
    value = _first_present(
        result.get("outcome"),
        _get_path_value(result, ("distributed_carrier_operational_role_summary", "outcome")),
        result.get("selected_carrier_role_result_outcome"),
    )
    return _stringify(value) if value is not None else None


def _basis_mapping(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("sync_non_sync_basis")
    return _copy(basis) if isinstance(basis, Mapping) else {}


def _carrier_role_basis_mapping(
    request: Mapping[str, Any], carrier_role_result: Mapping[str, Any]
) -> dict[str, Any]:
    basis = _first_present(
        request.get("carrier_role_basis"),
        _basis_mapping(request).get("carrier_role_basis"),
        carrier_role_result.get("carrier_role_basis"),
    )
    return _copy(basis) if isinstance(basis, Mapping) else {}


def _selected_source_body_authority_result(
    request: Mapping[str, Any], carrier_role_result: Mapping[str, Any]
) -> Any:
    selected_section = carrier_role_result.get("selected_source_body_authority_result")
    return _first_present(
        request.get("selected_source_body_authority_result"),
        _get_path_value(_as_mapping(selected_section), ("selected_source_body_authority_result",)),
        selected_section,
        _get_path_value(
            carrier_role_result,
            ("selected_operation_matter", "selected_source_body_authority_result"),
        ),
    )


def _selected_eligibility_result(
    request: Mapping[str, Any], carrier_role_result: Mapping[str, Any]
) -> Any:
    role_matter = _as_mapping(carrier_role_result.get("selected_operation_matter"))
    authority = _as_mapping(_selected_source_body_authority_result(request, carrier_role_result))
    return _first_present(
        request.get("selected_eligibility_result"),
        role_matter.get("selected_eligibility_result"),
        _get_path_value(authority, ("selected_operation_matter", "selected_eligibility_result")),
        _get_path_value(authority, ("selected_eligibility_result", "selected_eligibility_result")),
    )


def _selected_matter_declaration(
    request: Mapping[str, Any], carrier_role_result: Mapping[str, Any]
) -> Any:
    role_matter = _as_mapping(carrier_role_result.get("selected_operation_matter"))
    eligibility = _as_mapping(_selected_eligibility_result(request, carrier_role_result))
    return _first_present(
        request.get("selected_matter_declaration"),
        role_matter.get("selected_matter_declaration"),
        eligibility.get("selected_matter_declaration"),
        _get_path_value(eligibility, ("eligibility_basis", "selected_matter_declaration_result")),
    )


def _selected_operation_candidate(
    request: Mapping[str, Any], carrier_role_result: Mapping[str, Any]
) -> Any:
    role_matter = _as_mapping(carrier_role_result.get("selected_operation_matter"))
    eligibility = _as_mapping(_selected_eligibility_result(request, carrier_role_result))
    return _first_present(
        request.get("selected_operation_candidate"),
        role_matter.get("selected_operation_candidate"),
        eligibility.get("selected_operation_candidate"),
        _get_path_value(eligibility, ("eligibility_basis", "selected_operation_candidate")),
        _get_path_value(eligibility, ("eligibility_basis", "selected_operation_candidate_identity")),
    )


def _selected_operation_matter(
    request: Mapping[str, Any], carrier_role_result: Mapping[str, Any]
) -> Any:
    role_matter = _as_mapping(carrier_role_result.get("selected_operation_matter"))
    eligibility = _as_mapping(_selected_eligibility_result(request, carrier_role_result))
    return _first_present(
        request.get("selected_operation_matter"),
        role_matter.get("selected_operation_matter"),
        eligibility.get("selected_operation_matter"),
        _get_path_value(eligibility, ("eligibility_basis", "selected_operation_matter")),
    )


def _selected_operation_question(
    request: Mapping[str, Any], carrier_role_result: Mapping[str, Any]
) -> Any:
    role_matter = _as_mapping(carrier_role_result.get("selected_operation_matter"))
    eligibility = _as_mapping(_selected_eligibility_result(request, carrier_role_result))
    return _first_present(
        request.get("selected_operation_question"),
        request.get("operation_question"),
        role_matter.get("selected_operation_question"),
        _get_path_value(eligibility, ("eligibility_basis", "selected_operation_question")),
        _get_path_value(eligibility, ("distributed_operation_eligibility_summary", "operation_question")),
    )


def _selected_operation_purpose(
    request: Mapping[str, Any], carrier_role_result: Mapping[str, Any]
) -> Any:
    role_matter = _as_mapping(carrier_role_result.get("selected_operation_matter"))
    eligibility = _as_mapping(_selected_eligibility_result(request, carrier_role_result))
    return _first_present(
        request.get("selected_operation_purpose"),
        request.get("operation_purpose"),
        role_matter.get("selected_operation_purpose"),
        _get_path_value(eligibility, ("eligibility_basis", "selected_operation_purpose")),
        _get_path_value(eligibility, ("distributed_operation_eligibility_summary", "operation_purpose")),
    )


def _proposed_operation_kind(
    request: Mapping[str, Any], carrier_role_result: Mapping[str, Any]
) -> Any:
    role_matter = _as_mapping(carrier_role_result.get("selected_operation_matter"))
    eligibility = _as_mapping(_selected_eligibility_result(request, carrier_role_result))
    return _first_present(
        request.get("proposed_operation_kind"),
        role_matter.get("proposed_operation_kind"),
        _get_path_value(eligibility, ("eligibility_basis", "selected_proposed_operation_kind")),
        _get_path_value(eligibility, ("distributed_operation_eligibility_summary", "proposed_operation_kind")),
    )


def _source_body_lineage_basis(
    request: Mapping[str, Any],
    sync_basis: Mapping[str, Any],
    role_basis: Mapping[str, Any],
) -> Any:
    source_authority_basis = _as_mapping(role_basis.get("source_body_authority_basis"))
    return _first_present(
        request.get("source_body_lineage_basis"),
        sync_basis.get("source_body_lineage_basis"),
        role_basis.get("source_body_lineage_basis"),
        source_authority_basis.get("source_body_lineage_basis"),
    )


def _distributed_standing_basis(
    request: Mapping[str, Any],
    sync_basis: Mapping[str, Any],
    role_basis: Mapping[str, Any],
) -> Any:
    source_authority_basis = _as_mapping(role_basis.get("source_body_authority_basis"))
    return _first_present(
        request.get("distributed_standing_basis"),
        sync_basis.get("distributed_standing_basis"),
        role_basis.get("distributed_standing_basis"),
        source_authority_basis.get("distributed_standing_basis"),
    )


def _selected_carrier_context(
    request: Mapping[str, Any],
    sync_basis: Mapping[str, Any],
    role_basis: Mapping[str, Any],
) -> Any:
    return _first_present(
        request.get("selected_carrier_context"),
        sync_basis.get("selected_carrier_context"),
        role_basis.get("selected_carrier_context"),
    )


def _context_value(
    request: Mapping[str, Any],
    sync_basis: Mapping[str, Any],
    role_basis: Mapping[str, Any],
    carrier_context: Any,
    key: str,
) -> Any:
    carrier_map = _as_mapping(carrier_context)
    return _first_present(
        request.get(key),
        sync_basis.get(key),
        role_basis.get(key),
        carrier_map.get(key),
    )


def _carrier_context_explicitly_not_required(
    request: Mapping[str, Any], sync_basis: Mapping[str, Any], role_basis: Mapping[str, Any]
) -> bool:
    return any(
        _is_true(value)
        for value in (
            request.get("selected_carrier_context_not_required"),
            request.get("carrier_context_not_required"),
            sync_basis.get("selected_carrier_context_not_required"),
            sync_basis.get("carrier_context_not_required"),
            role_basis.get("selected_carrier_context_not_required"),
            role_basis.get("carrier_context_not_required"),
        )
    )


def _carrier_context_parseable(carrier_context: Any, not_required: bool) -> bool:
    if not _is_non_empty(carrier_context):
        return not_required
    if isinstance(carrier_context, Mapping):
        return True
    if isinstance(carrier_context, Sequence) and not isinstance(
        carrier_context, (str, bytes, bytearray)
    ):
        return all(isinstance(item, Mapping) for item in carrier_context)
    return False


def _selected_shape_values(value: Any, source_keys: Sequence[str], supported: set[str]) -> list[str]:
    if isinstance(value, Mapping):
        shape_source = None
        for key in source_keys:
            if key in value:
                shape_source = value.get(key)
                break
        if shape_source is None:
            shape_source = [key for key, enabled in value.items() if key in supported and enabled]
    else:
        shape_source = value

    if isinstance(shape_source, str):
        return [shape_source]
    if isinstance(shape_source, Sequence) and not isinstance(
        shape_source, (str, bytes, bytearray)
    ):
        values: list[str] = []
        for item in shape_source:
            if isinstance(item, str):
                values.append(item)
            elif isinstance(item, Mapping):
                posture = _first_present(
                    item.get("posture"),
                    item.get("sync_non_sync_posture"),
                    item.get("synchronization_posture"),
                    item.get("non_synchronization_posture"),
                    item.get("shape"),
                )
                if posture is not None:
                    values.append(_stringify(posture))
        return values
    return []


def _selected_role_shape_values(value: Any) -> list[str]:
    return _selected_shape_values(
        value,
        (
            "selected_carrier_role_shapes",
            "carrier_role_shapes",
            "role_shapes",
            "selected_shapes",
        ),
        SUPPORTED_CARRIER_ROLE_SHAPES,
    )


def _selected_role_shapes(
    request: Mapping[str, Any], carrier_role_result: Mapping[str, Any]
) -> list[str]:
    request_values = _selected_role_shape_values(request.get("carrier_role_shapes"))
    if request_values:
        return request_values
    basis_values = _selected_role_shape_values(_basis_mapping(request).get("carrier_role_shapes"))
    if basis_values:
        return basis_values
    role_section = carrier_role_result.get("carrier_role_shapes")
    section_values = _selected_role_shape_values(role_section)
    if section_values:
        return section_values
    return []


def _selected_sync_non_sync_postures(request: Mapping[str, Any]) -> list[str]:
    values = _selected_shape_values(
        request.get("sync_non_sync_postures"),
        (
            "selected_sync_non_sync_postures",
            "sync_non_sync_postures",
            "selected_postures",
            "postures",
        ),
        SUPPORTED_SYNC_NON_SYNC_POSTURES,
    )
    if not values:
        sync_posture = request.get("proposed_synchronization_posture")
        non_sync_posture = request.get("proposed_non_synchronization_posture")
        for posture in (sync_posture, non_sync_posture):
            if isinstance(posture, str):
                values.append(posture)
            elif isinstance(posture, Sequence) and not isinstance(
                posture, (str, bytes, bytearray)
            ):
                values.extend(_stringify(item) for item in posture)
    return values


def _unsupported_sync_non_sync_postures(postures: Sequence[str]) -> list[str]:
    return [posture for posture in postures if posture not in SUPPORTED_SYNC_NON_SYNC_POSTURES]


def _declared_non_claims_are_false(request: Mapping[str, Any]) -> bool:
    claims = request.get("declared_non_claims")
    if not isinstance(claims, Mapping):
        return False
    return all(claim in claims and claims[claim] is False for claim in REQUIRED_NON_CLAIMS)


def _carrier_role_non_claims_are_false(carrier_role_result: Mapping[str, Any]) -> bool:
    claims = carrier_role_result.get("non_claims")
    statement = _as_mapping(carrier_role_result.get("role_statement"))
    if not isinstance(claims, Mapping):
        claims = {}
    for claim in CARRIER_ROLE_NON_CLAIM_FIELDS:
        claim_value = claims.get(claim, statement.get(claim))
        if claim_value is not None and claim_value is not False:
            return False
    return True


def _field_tripped(containers: Sequence[Any], fields: Sequence[str]) -> str | None:
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        for field in fields:
            if _is_true(container.get(field)):
                return field
    return None


def _first_collapse_code(*containers: Any) -> str | None:
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        for field, code in SYNC_NON_SYNC_COLLAPSE_FIELDS:
            if _is_true(container.get(field)):
                return code
    return None


def _result_id(sync_non_sync_request_id: Any, selected_carrier_role_result_id: Any) -> str:
    source = _first_present(sync_non_sync_request_id, selected_carrier_role_result_id)
    return f"{_sanitize_filename(source)}__distributed_sync_non_sync_result"


def _load_selected_carrier_role_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    selected_path = request.get("selected_carrier_role_result_path")
    if _is_non_empty(selected_path):
        loaded, error = _read_json_object(_stringify(selected_path))
        if error == "unreadable":
            return None, BLOCK_CARRIER_ROLE_RESULT_UNREADABLE, _stringify(selected_path)
        if error == "malformed":
            return None, BLOCK_CARRIER_ROLE_RESULT_MALFORMED, _stringify(selected_path)
        return _copy(loaded), None, _stringify(selected_path)

    selected = request.get("selected_carrier_role_result")
    if isinstance(selected, Mapping):
        return _copy(selected), None, None
    if _is_non_empty(selected):
        return None, BLOCK_CARRIER_ROLE_RESULT_MALFORMED, None
    return None, BLOCK_CARRIER_ROLE_RESULT_MISSING, None


def _build_declared_sync_non_sync_question(
    request: Mapping[str, Any],
    selected_carrier_role_result_id: str | None,
    selected_carrier_role_outcome: str | None,
    request_path: str | None,
) -> dict[str, Any]:
    return {
        "sync_non_sync_request_id": request.get("sync_non_sync_request_id"),
        "sync_non_sync_question": request.get("sync_non_sync_question"),
        "sync_non_sync_intent": request.get("sync_non_sync_intent"),
        "sync_non_sync_request_path": request_path,
        "selected_carrier_role_result_id": _first_present(
            request.get("selected_carrier_role_result_id"),
            selected_carrier_role_result_id,
        ),
        "selected_carrier_role_result_outcome": _first_present(
            request.get("selected_carrier_role_result_outcome"),
            request.get("expected_selected_carrier_role_outcome"),
            selected_carrier_role_outcome,
        ),
        "sync_non_sync_boundary_is_not_synchronization_authorization": True,
        "sync_non_sync_boundary_is_not_non_synchronized_operation_authorization": True,
        "sync_non_sync_boundary_is_not_repository_synchronization": True,
        "sync_non_sync_boundary_is_not_shared_live_state": True,
        "sync_non_sync_boundary_is_not_state_merge": True,
        "sync_non_sync_boundary_is_not_replay": True,
        "sync_non_sync_boundary_is_not_full_body_transfer": True,
        "sync_non_sync_boundary_is_not_second_body": True,
        "sync_non_sync_boundary_is_not_role_activation": True,
        "sync_non_sync_boundary_is_not_carrier_authority": True,
        "sync_non_sync_boundary_is_not_operation_admission": True,
        "sync_non_sync_boundary_is_not_operation_authorization": True,
        "sync_non_sync_boundary_is_not_operation_execution": True,
        "sync_non_sync_boundary_is_not_consequence": True,
        "sync_non_sync_boundary_is_not_follow_on_work": True,
    }


def _build_selected_carrier_role_result_section(
    selected_carrier_role_result: Mapping[str, Any] | None,
    selected_carrier_role_result_path: str | None,
    selected_carrier_role_result_id: str | None,
    selected_carrier_role_outcome: str | None,
    failed_check_count: int | None,
) -> dict[str, Any]:
    result = _copy(selected_carrier_role_result) if isinstance(selected_carrier_role_result, Mapping) else None
    return {
        "selected_carrier_role_result": result,
        "selected_carrier_role_result_path": selected_carrier_role_result_path,
        "selected_carrier_role_result_id": selected_carrier_role_result_id,
        "selected_carrier_role_result_outcome": selected_carrier_role_outcome,
        "selected_carrier_role_result_outcome_is_recorded": (
            selected_carrier_role_outcome == EXPECTED_CARRIER_ROLE_OUTCOME
        ),
        "selected_carrier_role_result_failed_check_count": failed_check_count,
        "selected_carrier_role_result_failed_check_count_zero": (
            failed_check_count == EXPECTED_FAILED_CHECK_COUNT
        ),
        "selected_carrier_role_result_remains_role_basis_only": True,
        "selected_carrier_role_result_did_not_activate_roles": True,
        "selected_carrier_role_result_did_not_assign_carriers_to_operation": True,
        "selected_carrier_role_result_did_not_admit_operation": True,
        "selected_carrier_role_result_did_not_authorize_operation": True,
        "selected_carrier_role_result_did_not_execute_operation": True,
        "selected_carrier_role_result_did_not_authorize_sync": True,
        "selected_carrier_role_result_did_not_authorize_full_body_transfer": True,
        "selected_carrier_role_result_did_not_create_second_body": True,
        "selected_carrier_role_result_did_not_authorize_continuation": True,
        "selected_carrier_role_result_did_not_authorize_distributed_operation": True,
        "selected_carrier_role_result_did_not_create_consequence": True,
    }


def _build_selected_operation_matter_section(
    request: Mapping[str, Any],
    selected_carrier_role_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    carrier_role = selected_carrier_role_result or {}
    source_authority = _selected_source_body_authority_result(request, carrier_role)
    eligibility = _selected_eligibility_result(request, carrier_role)
    matter_declaration = _selected_matter_declaration(request, carrier_role)
    candidate = _selected_operation_candidate(request, carrier_role)
    matter = _selected_operation_matter(request, carrier_role)
    operation_question = _selected_operation_question(request, carrier_role)
    operation_purpose = _selected_operation_purpose(request, carrier_role)
    proposed_kind = _proposed_operation_kind(request, carrier_role)
    candidate_mapping = _as_mapping(candidate)
    matter_mapping = _as_mapping(matter)
    summary = _as_mapping(carrier_role.get("distributed_carrier_operational_role_summary"))
    return {
        "selected_carrier_role_result": _copy(carrier_role) if carrier_role else None,
        "selected_source_body_authority_result": _copy(source_authority),
        "selected_eligibility_result": _copy(eligibility),
        "selected_matter_declaration": _copy(matter_declaration),
        "selected_operation_candidate": _copy(candidate),
        "selected_operation_matter": _copy(matter),
        "selected_operation_question": _copy(operation_question),
        "selected_operation_purpose": _copy(operation_purpose),
        "proposed_operation_kind": _copy(proposed_kind),
        "selected_operation_candidate_id": _first_present(
            candidate_mapping.get("operation_candidate_id"),
            candidate_mapping.get("selected_operation_candidate_id"),
            summary.get("selected_operation_candidate_id"),
        ),
        "selected_operation_matter_id": _first_present(
            matter_mapping.get("operation_matter_id"),
            matter_mapping.get("selected_operation_matter_id"),
            summary.get("selected_operation_matter_id"),
        ),
        "carrier_role_basis_remains_role_basis_only": True,
        "carrier_roles_remain_non_active": True,
        "matter_remains_declaration_only": True,
        "candidate_remains_candidate_only": True,
        "eligibility_remains_eligibility_only": True,
        "authority_remains_basis_only": True,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
    }


def _build_sync_non_sync_basis_section(
    request: Mapping[str, Any],
    selected_carrier_role_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    carrier_role = selected_carrier_role_result or {}
    sync_basis = _basis_mapping(request)
    role_basis = _carrier_role_basis_mapping(request, carrier_role)
    carrier_context = _selected_carrier_context(request, sync_basis, role_basis)
    role_shapes = _selected_role_shapes(request, carrier_role)
    return {
        "sync_non_sync_basis": _copy(request.get("sync_non_sync_basis")),
        "selected_carrier_role_basis": _copy(role_basis)
        if role_basis
        else _copy(request.get("carrier_role_basis")),
        "selected_carrier_role_shapes": _copy(role_shapes),
        "selected_carrier_context": _copy(carrier_context),
        "carrier_b_success_context": _copy(
            _context_value(request, sync_basis, role_basis, carrier_context, "carrier_b_success_context")
        ),
        "carrier_c_block_context": _copy(
            _context_value(request, sync_basis, role_basis, carrier_context, "carrier_c_block_context")
        ),
        "b_c_divergence_context": _copy(
            _context_value(request, sync_basis, role_basis, carrier_context, "b_c_divergence_context")
        ),
        "refusal_blocked_attempt_context": _copy(
            _context_value(
                request, sync_basis, role_basis, carrier_context, "refusal_blocked_attempt_context"
            )
        ),
        "projection_mismatch_context": _copy(
            _context_value(request, sync_basis, role_basis, carrier_context, "projection_mismatch_context")
        ),
        "source_body_lineage_basis": _copy(
            _source_body_lineage_basis(request, sync_basis, role_basis)
        ),
        "distributed_standing_basis": _copy(
            _distributed_standing_basis(request, sync_basis, role_basis)
        ),
        "distributed_standing_basis_is_basis_only": bool(
            _distributed_standing_basis(request, sync_basis, role_basis)
        ),
        "proposed_synchronization_posture": _copy(
            _first_present(
                request.get("proposed_synchronization_posture"),
                sync_basis.get("proposed_synchronization_posture"),
            )
        ),
        "proposed_non_synchronization_posture": _copy(
            _first_present(
                request.get("proposed_non_synchronization_posture"),
                sync_basis.get("proposed_non_synchronization_posture"),
            )
        ),
        "carrier_evidence_remains_unmerged": True,
        "carrier_context_remains_context_only": True,
        "divergence_remains_visible": True,
        "refusal_remains_visible": True,
        "blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible": True,
        "sync_non_sync_basis_is_not_synchronization_authorization": True,
        "sync_non_sync_basis_is_not_non_synchronized_operation_authorization": True,
        "sync_non_sync_basis_is_not_shared_live_state": True,
        "sync_non_sync_basis_is_not_state_merge": True,
        "sync_non_sync_basis_is_not_full_body_transfer": True,
        "sync_non_sync_basis_is_not_second_body": True,
    }


def _build_sync_non_sync_postures_section(request: Mapping[str, Any]) -> dict[str, Any]:
    selected_postures = _selected_sync_non_sync_postures(request)
    unsupported = _unsupported_sync_non_sync_postures(selected_postures)
    selected_set = set(selected_postures)
    all_supported = bool(selected_postures) and not unsupported
    return {
        "selected_sync_non_sync_postures": selected_postures,
        "supported_sync_non_sync_postures": sorted(SUPPORTED_SYNC_NON_SYNC_POSTURES),
        "unsupported_sync_non_sync_postures": unsupported,
        "all_selected_postures_supported": all_supported,
        "postures_are_boundary_postures_only": True,
        "postures_are_not_synchronization_authorization": True,
        "postures_are_not_non_synchronized_operation_authorization": True,
        "postures_do_not_create_operational_autonomy": True,
        "postures_do_not_create_shared_state": True,
        "postures_do_not_create_merge_permission": True,
        "postures_do_not_create_full_body_transfer": True,
        "postures_do_not_create_second_body": True,
        "no_repository_synchronization_by_default": (
            "NO_REPOSITORY_SYNCHRONIZATION_BY_DEFAULT" in selected_set
        ),
        "no_shared_live_state_by_default": (
            "NO_SHARED_LIVE_STATE_BY_DEFAULT" in selected_set
        ),
        "no_state_merge_by_default": "NO_STATE_MERGE_BY_DEFAULT" in selected_set,
        "no_full_body_transfer_by_default": (
            "NO_FULL_BODY_TRANSFER_BY_DEFAULT" in selected_set
        ),
        "no_second_body_by_default": "NO_SECOND_BODY_BY_DEFAULT" in selected_set,
        "carrier_evidence_remains_unmerged": (
            "CARRIER_EVIDENCE_REMAINS_UNMERGED" in selected_set
        ),
        "carrier_context_remains_context_only": (
            "CARRIER_CONTEXT_REMAINS_CONTEXT_ONLY" in selected_set
        ),
        "divergence_remains_visible": "DIVERGENCE_REMAINS_VISIBLE" in selected_set,
        "refusal_remains_visible": "REFUSAL_REMAINS_VISIBLE" in selected_set,
        "blocked_attempts_remain_visible": (
            "BLOCKED_ATTEMPTS_REMAIN_VISIBLE" in selected_set
        ),
        "projection_mismatch_remains_visible": (
            "PROJECTION_MISMATCH_REMAINS_VISIBLE" in selected_set
        ),
        "future_synchronization_requires_separate_boundary": (
            "FUTURE_SYNCHRONIZATION_REQUIRES_SEPARATE_BOUNDARY" in selected_set
        ),
        "future_non_synchronized_operation_requires_separate_admission": (
            "FUTURE_NON_SYNCHRONIZED_OPERATION_REQUIRES_SEPARATE_ADMISSION"
            in selected_set
        ),
    }


def _build_checks(
    request: Mapping[str, Any],
    selected_carrier_role_result: Mapping[str, Any] | None,
    selected_carrier_role_load_code: str | None,
) -> list[dict[str, Any]]:
    carrier_role = selected_carrier_role_result or {}
    role_statement = _as_mapping(carrier_role.get("role_statement"))
    role_non_claims = _as_mapping(carrier_role.get("non_claims"))
    sync_basis = _basis_mapping(request)
    role_basis = _carrier_role_basis_mapping(request, carrier_role)
    selected_carrier_role_outcome = _extract_carrier_role_outcome(carrier_role)
    failed_check_count = _extract_failed_check_count(carrier_role)
    selected_source_authority = _selected_source_body_authority_result(request, carrier_role)
    selected_eligibility = _selected_eligibility_result(request, carrier_role)
    selected_matter_declaration = _selected_matter_declaration(request, carrier_role)
    selected_operation_candidate = _selected_operation_candidate(request, carrier_role)
    selected_operation_matter = _selected_operation_matter(request, carrier_role)
    selected_carrier_context = _selected_carrier_context(request, sync_basis, role_basis)
    carrier_context_not_required = _carrier_context_explicitly_not_required(
        request, sync_basis, role_basis
    )
    carrier_context_parseable = _carrier_context_parseable(
        selected_carrier_context, carrier_context_not_required
    )
    role_shapes = _selected_role_shapes(request, carrier_role)
    postures = _selected_sync_non_sync_postures(request)
    unsupported_postures = _unsupported_sync_non_sync_postures(postures)

    collapse_containers = (
        request,
        sync_basis,
        request.get("sync_non_sync_postures"),
        request.get("proposed_synchronization_posture"),
        request.get("proposed_non_synchronization_posture"),
        request.get("declared_non_claims"),
        role_statement,
        role_non_claims,
    )

    checks: list[dict[str, Any]] = []
    checks.append(
        _make_check(
            "sync/non-sync question declared",
            _is_non_empty(request.get("sync_non_sync_question")),
            "sync/non-sync question present",
            request.get("sync_non_sync_question"),
            BLOCK_SYNC_NON_SYNC_QUESTION_UNDECLARED,
        )
    )
    checks.append(
        _make_check(
            "sync/non-sync intent supported",
            request.get("sync_non_sync_intent") in SUPPORTED_SYNC_NON_SYNC_INTENTS,
            f"one of {sorted(SUPPORTED_SYNC_NON_SYNC_INTENTS)}",
            request.get("sync_non_sync_intent"),
            BLOCK_SYNC_NON_SYNC_INTENT_UNSUPPORTED,
        )
    )
    checks.append(
        _make_check(
            "selected carrier role result present",
            selected_carrier_role_result is not None and selected_carrier_role_load_code is None,
            "selected carrier role result mapping",
            selected_carrier_role_load_code
            or ("present" if selected_carrier_role_result is not None else "missing"),
            selected_carrier_role_load_code or BLOCK_CARRIER_ROLE_RESULT_MISSING,
        )
    )
    checks.append(
        _make_check(
            "selected carrier role result outcome declared",
            _is_non_empty(selected_carrier_role_outcome),
            "selected carrier role outcome present",
            selected_carrier_role_outcome,
            BLOCK_CARRIER_ROLE_RESULT_OUTCOME_MISSING,
        )
    )
    checks.append(
        _make_check(
            "selected carrier role result outcome recorded",
            selected_carrier_role_outcome == EXPECTED_CARRIER_ROLE_OUTCOME,
            EXPECTED_CARRIER_ROLE_OUTCOME,
            selected_carrier_role_outcome,
            BLOCK_CARRIER_ROLE_RESULT_NOT_RECORDED,
        )
    )
    checks.append(
        _make_check(
            "selected carrier role result failed check count zero",
            failed_check_count == EXPECTED_FAILED_CHECK_COUNT,
            "failed check count 0",
            failed_check_count,
            BLOCK_CARRIER_ROLE_RESULT_HAS_FAILED_CHECKS,
        )
    )
    checks.append(
        _make_check(
            "selected source-body authority result preserved",
            _is_non_empty(selected_source_authority),
            "selected source-body authority result present",
            "present" if _is_non_empty(selected_source_authority) else "missing",
            BLOCK_SOURCE_BODY_AUTHORITY_RESULT_MISSING,
        )
    )
    checks.append(
        _make_check(
            "selected eligibility result preserved",
            _is_non_empty(selected_eligibility),
            "selected eligibility result present",
            "present" if _is_non_empty(selected_eligibility) else "missing",
            BLOCK_SELECTED_ELIGIBILITY_RESULT_MISSING,
        )
    )
    checks.append(
        _make_check(
            "selected matter declaration preserved",
            _is_non_empty(selected_matter_declaration),
            "selected matter declaration present",
            "present" if _is_non_empty(selected_matter_declaration) else "missing",
            BLOCK_SELECTED_MATTER_DECLARATION_MISSING,
        )
    )
    checks.append(
        _make_check(
            "selected operation candidate preserved",
            _is_non_empty(selected_operation_candidate),
            "selected operation candidate present",
            "present" if _is_non_empty(selected_operation_candidate) else "missing",
            BLOCK_SELECTED_OPERATION_CANDIDATE_MISSING,
        )
    )
    checks.append(
        _make_check(
            "selected operation matter preserved",
            _is_non_empty(selected_operation_matter),
            "selected operation matter present",
            "present" if _is_non_empty(selected_operation_matter) else "missing",
            BLOCK_SELECTED_OPERATION_MATTER_MISSING,
        )
    )
    checks.append(
        _make_check(
            "carrier role basis preserved",
            _is_non_empty(role_basis),
            "carrier role basis present",
            "present" if _is_non_empty(role_basis) else "missing",
            BLOCK_CARRIER_ROLE_BASIS_MISSING,
        )
    )
    checks.append(
        _make_check(
            "carrier role shapes preserved",
            _is_non_empty(role_shapes),
            "carrier role shapes present",
            role_shapes or "missing",
            BLOCK_CARRIER_ROLE_SHAPES_MISSING,
        )
    )
    checks.append(
        _make_check(
            "carrier context preserved",
            (_is_non_empty(selected_carrier_context) or carrier_context_not_required)
            and carrier_context_parseable,
            "selected carrier context mapping or sequence of mappings",
            "present"
            if _is_non_empty(selected_carrier_context) and carrier_context_parseable
            else ("not required" if carrier_context_not_required else type(selected_carrier_context).__name__),
            BLOCK_SELECTED_CARRIER_CONTEXT_MALFORMED,
        )
    )

    collapse_checks = (
        (
            "carrier roles not activated",
            BLOCK_SYNC_NON_SYNC_REVIEW_ACTIVATES_CARRIER_ROLES,
            ("carrier_role_activated", "carrier_roles_activated", "role_review_activates_carrier_role"),
        ),
        (
            "no carrier assigned to operation",
            BLOCK_SYNC_NON_SYNC_REVIEW_ACTIVATES_CARRIER_ROLES,
            ("carrier_role_assigned_for_operation", "carrier_roles_assigned_for_operation"),
        ),
        (
            "no carrier authority/currentness/hierarchy created",
            BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_AUTHORITY,
            (
                "carrier_authority_created",
                "carrier_becomes_authority",
                "authority_created",
                "carrier_currentness_created",
                "carrier_becomes_currentness",
                "carrier_hierarchy_created",
                "carrier_hierarchy_defined",
            ),
        ),
    )
    for check_name, block_code, fields in collapse_checks:
        tripped = _field_tripped(collapse_containers, fields)
        checks.append(
            _make_check(
                check_name,
                tripped is None,
                "false collapse posture",
                tripped or "false",
                block_code,
            )
        )

    checks.append(
        _make_check(
            "selected sync/non-sync postures supported",
            bool(postures) and not unsupported_postures,
            f"subset of {sorted(SUPPORTED_SYNC_NON_SYNC_POSTURES)}",
            unsupported_postures or postures or "missing",
            BLOCK_UNSUPPORTED_SYNC_NON_SYNC_POSTURE,
        )
    )

    sync_context_checks = (
        (
            "no repository synchronization authorized",
            BLOCK_SYNC_REVIEW_AUTHORIZES_REPOSITORY_SYNC,
            ("repository_synchronization_authorized", "repository_sync_authorized", "sync_authorized", "synchronization_authorized"),
        ),
        (
            "no shared live state created",
            BLOCK_SYNC_REVIEW_CREATES_SHARED_LIVE_STATE,
            ("shared_live_state_created", "shared_live_state_authorized", "synchronized_state_created"),
        ),
        (
            "no state merge authorized",
            BLOCK_SYNC_REVIEW_AUTHORIZES_STATE_MERGE,
            ("state_merge_authorized", "repository_merge_authorized", "state_merge_permission_created"),
        ),
        (
            "no replay authorized",
            BLOCK_SYNC_REVIEW_AUTHORIZES_REPLAY,
            ("replay_authorized", "source_replay_authorized"),
        ),
        (
            "no full body transfer authorized",
            BLOCK_SYNC_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER,
            ("full_body_transfer_authorized", "full_body_transfer_created"),
        ),
        (
            "no second body created",
            BLOCK_SYNC_REVIEW_CREATES_SECOND_BODY,
            ("second_body_created", "second_body_authorized"),
        ),
        (
            "no non-synchronized operation authorized",
            BLOCK_NON_SYNC_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION,
            (
                "non_synchronized_operation_authorized",
                "non_sync_operation_authorized",
                "divergent_live_operation_authorized",
            ),
        ),
        (
            "no carrier autonomy authorized",
            BLOCK_NON_SYNC_REVIEW_AUTHORIZES_CARRIER_AUTONOMY,
            ("carrier_autonomy_authorized", "unsupervised_carrier_autonomy_authorized"),
        ),
        (
            "no stale carrier operation authorized",
            BLOCK_NON_SYNC_REVIEW_AUTHORIZES_STALE_CARRIER_OPERATION,
            ("stale_carrier_operation_authorized",),
        ),
        (
            "no operation admitted",
            BLOCK_SYNC_NON_SYNC_REVIEW_ADMITS_OPERATION,
            ("operation_admitted",),
        ),
        (
            "no operation authorized",
            BLOCK_SYNC_NON_SYNC_REVIEW_AUTHORIZES_OPERATION,
            ("operation_authorized", "distributed_operation_authorized"),
        ),
        (
            "no operation executed",
            BLOCK_SYNC_NON_SYNC_REVIEW_EXECUTES_OPERATION,
            ("operation_executed",),
        ),
        (
            "divergence remains visible",
            BLOCK_SYNC_NON_SYNC_REVIEW_RESOLVES_DIVERGENCE,
            ("divergence_resolved", "b_c_divergence_hidden"),
        ),
        (
            "refusal remains visible",
            BLOCK_SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL,
            ("refusal_erased", "refusal_hidden"),
        ),
        (
            "blocked attempts remain visible",
            BLOCK_SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL,
            ("blocked_attempt_erased", "blocked_attempt_hidden"),
        ),
        (
            "projection mismatch remains visible",
            BLOCK_SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL,
            ("projection_mismatch_hidden",),
        ),
        (
            "no consequence/public readiness/final completion/follow-on work",
            BLOCK_SYNC_NON_SYNC_REVIEW_CREATES_CONSEQUENCE,
            (
                "consequence_created",
                "public_launch_readiness_created",
                "public_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
            ),
        ),
        (
            "no mutation/replay/merge",
            BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED,
            ("mutation_performed", "replay_performed", "merge_performed"),
        ),
    )
    for check_name, block_code, fields in sync_context_checks:
        tripped = _field_tripped(collapse_containers, fields)
        checks.append(
            _make_check(
                check_name,
                tripped is None,
                "false collapse posture",
                tripped or "false",
                block_code,
            )
        )

    checks.append(
        _make_check(
            "non-claims remain false",
            _declared_non_claims_are_false(request)
            and _carrier_role_non_claims_are_false(carrier_role),
            "required sync/non-sync non-claims are explicit and false",
            "preserved" if _declared_non_claims_are_false(request) else "missing or flipped",
            BLOCK_NON_CLAIM_MISSING_OR_FLIPPED,
        )
    )
    return checks


def _build_sync_non_sync_non_meaning() -> dict[str, bool]:
    keys = (
        "repository_synchronization_authorized",
        "synchronization_authorized",
        "shared_live_state_created",
        "state_merge_authorized",
        "replay_authorized",
        "full_body_transfer_authorized",
        "second_body_created",
        "non_synchronized_operation_authorized",
        "carrier_autonomy_authorized",
        "stale_carrier_operation_authorized",
        "operation_admitted",
        "operation_authorized",
        "operation_executed",
        "carrier_role_activated",
        "carrier_roles_activated",
        "carrier_authority_created",
        "carrier_currentness_created",
        "current_carrier_selected",
        "winning_carrier_selected",
        "losing_carrier_invalidated",
        "carrier_hierarchy_created",
        "source_replaced",
        "authority_created",
        "permission_created",
        "truth_action_created",
        "truth_created",
        "action_authorized",
        "consequence_created",
        "divergence_resolved",
        "evidence_erased",
        "refusal_erased",
        "blocked_attempt_erased",
        "projection_mismatch_hidden",
        "public_launch_readiness_created",
        "public_readiness_created",
        "final_completion_claimed",
        "follow_on_work_authorized",
    )
    non_meaning: dict[str, bool] = {}
    for key in keys:
        non_meaning[key] = True
        non_meaning[f"does_not_mean_{key}"] = True
    return non_meaning


def _build_additional_basis_required(
    outcome: str, request: Mapping[str, Any]
) -> dict[str, Any]:
    context = request.get("additional_basis_context")
    context_mapping = _copy(context) if isinstance(context, Mapping) else {}
    requires = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": requires,
        "additional_basis_context": context_mapping,
        "additional_basis_reason": _first_present(
            request.get("additional_basis_reason"),
            context_mapping.get("additional_basis_reason"),
            context_mapping.get("reason"),
            "additional sync/non-sync basis required" if requires else None,
        ),
        "selected_carrier_evidence_merge_posture_not_explicit_enough": bool(
            context_mapping.get(
                "selected_carrier_evidence_merge_posture_not_explicit_enough", False
            )
        ),
        "no_sync_posture_too_generic": bool(
            context_mapping.get("no_sync_posture_too_generic", False)
        ),
        "future_sync_boundary_requirements_not_specific_enough": bool(
            context_mapping.get(
                "future_sync_boundary_requirements_not_specific_enough", False
            )
        ),
        "non_synchronized_operation_refusal_not_explicit_enough": bool(
            context_mapping.get(
                "non_synchronized_operation_refusal_not_explicit_enough", False
            )
        ),
        "divergence_refusal_preservation_needs_stronger_basis": bool(
            context_mapping.get(
                "divergence_refusal_preservation_needs_stronger_basis", False
            )
        ),
        "projection_mismatch_preservation_needs_stronger_basis": bool(
            context_mapping.get(
                "projection_mismatch_preservation_needs_stronger_basis", False
            )
        ),
        "affected_surface_sync_risk_requires_clearer_classification": bool(
            context_mapping.get(
                "affected_surface_sync_risk_requires_clearer_classification", False
            )
        ),
        "proposed_output_family_creates_sync_ambiguity": bool(
            context_mapping.get("proposed_output_family_creates_sync_ambiguity", False)
        ),
        "admission_transition_boundary_cannot_yet_inspect_sync_non_sync_safely": bool(
            context_mapping.get(
                "admission_transition_boundary_cannot_yet_inspect_sync_non_sync_safely",
                False,
            )
        ),
        "additional_basis_not_scheduled": True,
        "additional_basis_not_authorized": True,
        "additional_basis_not_executed": True,
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
    }


def _build_sync_non_sync_statement(
    outcome: str,
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    passed_names = {check.get("check_name") for check in checks if check.get("passed") is True}
    statement = {
        "distributed_sync_non_sync_boundary_recorded": outcome == OUTCOME_RECORDED,
        "sync_non_sync_basis_not_sufficient": outcome == OUTCOME_NOT_SUFFICIENT,
        "distributed_sync_non_sync_requires_additional_basis": (
            outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        ),
        "selected_carrier_role_result_preserved": (
            "selected carrier role result present" in passed_names
        ),
        "selected_carrier_role_result_recorded": (
            "selected carrier role result outcome recorded" in passed_names
        ),
        "selected_carrier_role_result_failed_check_count_zero": (
            "selected carrier role result failed check count zero" in passed_names
        ),
        "selected_source_body_authority_result_preserved": (
            "selected source-body authority result preserved" in passed_names
        ),
        "selected_eligibility_result_preserved": (
            "selected eligibility result preserved" in passed_names
        ),
        "selected_matter_declaration_preserved": (
            "selected matter declaration preserved" in passed_names
        ),
        "selected_operation_candidate_preserved": (
            "selected operation candidate preserved" in passed_names
        ),
        "selected_operation_matter_preserved": (
            "selected operation matter preserved" in passed_names
        ),
        "carrier_role_basis_preserved": "carrier role basis preserved" in passed_names,
        "carrier_role_shapes_preserved": "carrier role shapes preserved" in passed_names,
        "carrier_context_preserved": "carrier context preserved" in passed_names,
        "sync_non_sync_postures_preserved": (
            "selected sync/non-sync postures supported" in passed_names
        ),
        "sync_non_sync_postures_supported": (
            "selected sync/non-sync postures supported" in passed_names
        ),
        "carrier_evidence_remains_unmerged": (
            "selected sync/non-sync postures supported" in passed_names
        ),
        "carrier_context_remains_context_only": (
            "carrier context preserved" in passed_names
        ),
        "divergence_remains_visible": "divergence remains visible" in passed_names,
        "refusal_remains_visible": "refusal remains visible" in passed_names,
        "blocked_attempts_remain_visible": "blocked attempts remain visible" in passed_names,
        "projection_mismatch_remains_visible": (
            "projection mismatch remains visible" in passed_names
        ),
        "repository_synchronization_authorized": False,
        "shared_live_state_created": False,
        "state_merge_authorized": False,
        "replay_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "non_synchronized_operation_authorized": False,
        "carrier_autonomy_authorized": False,
        "stale_carrier_operation_authorized": False,
        "carrier_role_activated": False,
        "carrier_roles_activated": False,
        "carrier_role_assigned_for_operation": False,
        "carrier_roles_assigned_for_operation": False,
        "carrier_authority_created": False,
        "carrier_currentness_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "carrier_hierarchy_created": False,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
        "consequence_created": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "future_admission_transition_may_later_review_sync_non_sync": (
            outcome == OUTCOME_RECORDED
        ),
        "not_sufficient_reason": request.get("not_sufficient_reason")
        if outcome == OUTCOME_NOT_SUFFICIENT
        else None,
        "additional_basis_reason": _first_present(
            request.get("additional_basis_reason"),
            _as_mapping(request.get("additional_basis_context")).get("reason"),
        )
        if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        else None,
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
        "block_code": block_code,
        "block_reason": block_reason,
    }
    statement.update(REQUIRED_NON_CLAIMS)
    return statement


def _decide_outcome(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    preliminary_block_code: str | None,
) -> tuple[str, str | None, str | None]:
    if preliminary_block_code:
        return (
            OUTCOME_BLOCKED,
            preliminary_block_code,
            request.get("block_reason") or preliminary_block_code,
        )
    if request.get("sync_non_sync_intent") == INTENT_BLOCK:
        return (
            OUTCOME_BLOCKED,
            BLOCK_SYNC_NON_SYNC_REVIEW_REQUEST_EXPLICITLY_BLOCKED,
            request.get("block_reason") or "sync/non-sync review explicitly blocked",
        )
    failed_code = _first_failed_code(checks)
    if failed_code:
        collapse_code = _first_collapse_code(
            request,
            _basis_mapping(request),
            request.get("sync_non_sync_postures"),
            request.get("declared_non_claims"),
        )
        code = collapse_code or failed_code
        return OUTCOME_BLOCKED, code, request.get("block_reason") or code

    requested_outcome = request.get("requested_sync_non_sync_outcome")
    if request.get("sync_non_sync_intent") == INTENT_DO_NOT_RECORD:
        return (
            OUTCOME_NOT_SUFFICIENT,
            None,
            request.get("not_sufficient_reason") or "sync/non-sync boundary not recorded",
        )
    if requested_outcome == OUTCOME_NOT_SUFFICIENT or _is_non_empty(
        request.get("not_sufficient_reason")
    ):
        return OUTCOME_NOT_SUFFICIENT, None, request.get("not_sufficient_reason")
    if requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS or _is_non_empty(
        request.get("additional_basis_context")
    ):
        return (
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            None,
            request.get("additional_basis_reason")
            or _as_mapping(request.get("additional_basis_context")).get("reason"),
        )
    if requested_outcome and requested_outcome not in SUPPORTED_SYNC_NON_SYNC_OUTCOMES:
        return OUTCOME_BLOCKED, BLOCK_SYNC_NON_SYNC_INTENT_UNSUPPORTED, _stringify(requested_outcome)
    return OUTCOME_RECORDED, None, None


def build_distributed_synchronization_non_synchronization_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    statement = _as_mapping(result.get("sync_non_sync_statement"))
    declared_question = _as_mapping(result.get("declared_sync_non_sync_question"))
    selected_role = _as_mapping(result.get("selected_carrier_role_result"))
    selected_matter = _as_mapping(result.get("selected_operation_matter"))
    postures = _as_mapping(result.get("sync_non_sync_postures"))
    checks = result.get("sync_non_sync_checks")
    check_list = [check for check in checks if isinstance(check, Mapping)] if isinstance(checks, Sequence) else []
    non_claims = _as_mapping(result.get("non_claims"))
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": _get_path_value(result, ("block", "block_code")),
        "block_reason": _get_path_value(result, ("block", "block_reason")),
        "sync_non_sync_request_id": declared_question.get("sync_non_sync_request_id"),
        "sync_non_sync_question": declared_question.get("sync_non_sync_question"),
        "sync_non_sync_intent": declared_question.get("sync_non_sync_intent"),
        "selected_carrier_role_result_id": selected_role.get(
            "selected_carrier_role_result_id"
        )
        or declared_question.get("selected_carrier_role_result_id"),
        "selected_carrier_role_result_outcome": selected_role.get(
            "selected_carrier_role_result_outcome"
        )
        or declared_question.get("selected_carrier_role_result_outcome"),
        "selected_operation_candidate_id": selected_matter.get(
            "selected_operation_candidate_id"
        ),
        "selected_operation_matter_id": selected_matter.get("selected_operation_matter_id"),
        "passed_check_count": _passed_check_count(check_list),
        "failed_check_count": _failed_check_count(check_list),
        "distributed_sync_non_sync_boundary_recorded": statement.get(
            "distributed_sync_non_sync_boundary_recorded", False
        ),
        "sync_non_sync_basis_not_sufficient": statement.get(
            "sync_non_sync_basis_not_sufficient", False
        ),
        "requires_additional_basis": statement.get(
            "distributed_sync_non_sync_requires_additional_basis", False
        ),
        "selected_carrier_role_result_preserved": statement.get(
            "selected_carrier_role_result_preserved", False
        ),
        "selected_carrier_role_result_recorded": statement.get(
            "selected_carrier_role_result_recorded", False
        ),
        "selected_carrier_role_result_failed_check_count_zero": statement.get(
            "selected_carrier_role_result_failed_check_count_zero", False
        ),
        "selected_source_body_authority_result_preserved": statement.get(
            "selected_source_body_authority_result_preserved", False
        ),
        "selected_eligibility_result_preserved": statement.get(
            "selected_eligibility_result_preserved", False
        ),
        "selected_matter_declaration_preserved": statement.get(
            "selected_matter_declaration_preserved", False
        ),
        "selected_operation_candidate_preserved": statement.get(
            "selected_operation_candidate_preserved", False
        ),
        "selected_operation_matter_preserved": statement.get(
            "selected_operation_matter_preserved", False
        ),
        "carrier_role_basis_preserved": statement.get(
            "carrier_role_basis_preserved", False
        ),
        "carrier_role_shapes_preserved": statement.get(
            "carrier_role_shapes_preserved", False
        ),
        "carrier_context_preserved": statement.get("carrier_context_preserved", False),
        "sync_non_sync_postures_preserved": statement.get(
            "sync_non_sync_postures_preserved", False
        ),
        "sync_non_sync_postures_supported": statement.get(
            "sync_non_sync_postures_supported", False
        ),
        "selected_sync_non_sync_postures": postures.get(
            "selected_sync_non_sync_postures", []
        ),
        "carrier_evidence_remains_unmerged": statement.get(
            "carrier_evidence_remains_unmerged", False
        ),
        "carrier_context_remains_context_only": statement.get(
            "carrier_context_remains_context_only", False
        ),
        "divergence_remains_visible": statement.get("divergence_remains_visible", False),
        "refusal_remains_visible": statement.get("refusal_remains_visible", False),
        "blocked_attempts_remain_visible": statement.get(
            "blocked_attempts_remain_visible", False
        ),
        "projection_mismatch_remains_visible": statement.get(
            "projection_mismatch_remains_visible", False
        ),
        "no_repository_sync_shared_live_state_state_merge_replay": not any(
            (
                statement.get("repository_synchronization_authorized", False),
                statement.get("shared_live_state_created", False),
                statement.get("state_merge_authorized", False),
                statement.get("replay_authorized", False),
            )
        ),
        "no_full_body_transfer_second_body": not any(
            (
                statement.get("full_body_transfer_authorized", False),
                statement.get("second_body_created", False),
            )
        ),
        "repository_synchronization_authorized": False,
        "shared_live_state_created": False,
        "state_merge_authorized": False,
        "replay_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "no_non_synchronized_operation_carrier_autonomy_stale_carrier_operation": not any(
            (
                statement.get("non_synchronized_operation_authorized", False),
                statement.get("carrier_autonomy_authorized", False),
                statement.get("stale_carrier_operation_authorized", False),
            )
        ),
        "non_synchronized_operation_authorized": False,
        "carrier_autonomy_authorized": False,
        "stale_carrier_operation_authorized": False,
        "carrier_role_activated": False,
        "carrier_roles_activated": False,
        "carrier_role_assigned_for_operation": False,
        "carrier_roles_assigned_for_operation": False,
        "carrier_authority_created": False,
        "carrier_currentness_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "carrier_hierarchy_created": False,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "no_consequence_public_readiness_final_completion_follow_on_work": not any(
            (
                statement.get("consequence_created", False),
                statement.get("public_launch_readiness_created", False),
                statement.get("final_completion_claimed", False),
                statement.get("follow_on_work_authorized", False),
            )
        ),
        "future_admission_transition_may_later_review_sync_non_sync": statement.get(
            "future_admission_transition_may_later_review_sync_non_sync", False
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "repository_synchronization_authorized",
                "shared_live_state_created",
                "state_merge_authorized",
                "replay_authorized",
                "full_body_transfer_authorized",
                "second_body_created",
                "non_synchronized_operation_authorized",
                "carrier_autonomy_authorized",
                "stale_carrier_operation_authorized",
                "carrier_role_activated",
                "operation_admitted",
                "operation_authorized",
                "operation_executed",
                "consequence_created",
                "public_launch_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
            )
        },
    }


def resolve_distributed_synchronization_non_synchronization_boundary(
    declared_sync_non_sync_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_sync_non_sync_request is None:
        request: dict[str, Any] = {}
        preliminary_block_code = BLOCK_SYNC_NON_SYNC_QUESTION_UNDECLARED
        request_path = None
    elif not isinstance(declared_sync_non_sync_request, Mapping):
        request = {}
        preliminary_block_code = BLOCK_DECLARED_SYNC_NON_SYNC_REQUEST_MALFORMED
        request_path = None
    else:
        request = _copy(declared_sync_non_sync_request)
        preliminary_block_code = None
        request_path = request.get("sync_non_sync_request_path")

    selected_carrier_role_result, selected_carrier_role_load_code, selected_carrier_role_path = (
        _load_selected_carrier_role_result(request)
    )
    selected_carrier_role_id = _first_present(
        request.get("selected_carrier_role_result_id"),
        _extract_carrier_role_result_id(selected_carrier_role_result or {}),
    )
    selected_carrier_role_outcome = _first_present(
        request.get("selected_carrier_role_result_outcome"),
        request.get("expected_selected_carrier_role_outcome"),
        _extract_carrier_role_outcome(selected_carrier_role_result or {}),
    )
    failed_check_count = _extract_failed_check_count(selected_carrier_role_result or {})
    checks = _build_checks(
        request, selected_carrier_role_result, selected_carrier_role_load_code
    )
    outcome, block_code, block_reason = _decide_outcome(
        request, checks, preliminary_block_code
    )
    sync_non_sync_request_id = request.get("sync_non_sync_request_id")
    result_id = _result_id(sync_non_sync_request_id, selected_carrier_role_id)
    metadata = {
        "distributed_sync_non_sync_result_id": result_id,
        "distributed_sync_non_sync_result_type": RESULT_TYPE,
        "distributed_sync_non_sync_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }
    result: dict[str, Any] = {
        "distributed_sync_non_sync_metadata": metadata,
        "declared_sync_non_sync_question": _build_declared_sync_non_sync_question(
            request,
            _stringify(selected_carrier_role_id) if selected_carrier_role_id else None,
            _stringify(selected_carrier_role_outcome) if selected_carrier_role_outcome else None,
            _stringify(request_path) if request_path else None,
        ),
        "selected_carrier_role_result": _build_selected_carrier_role_result_section(
            selected_carrier_role_result,
            selected_carrier_role_path,
            _stringify(selected_carrier_role_id) if selected_carrier_role_id else None,
            _stringify(selected_carrier_role_outcome)
            if selected_carrier_role_outcome
            else None,
            failed_check_count,
        ),
        "selected_operation_matter": _build_selected_operation_matter_section(
            request, selected_carrier_role_result
        ),
        "sync_non_sync_basis": _build_sync_non_sync_basis_section(
            request, selected_carrier_role_result
        ),
        "sync_non_sync_postures": _build_sync_non_sync_postures_section(request),
        "sync_non_sync_checks": checks,
        "sync_non_sync_statement": _build_sync_non_sync_statement(
            outcome, request, checks, block_code, block_reason
        ),
        "sync_non_sync_non_meaning": _build_sync_non_sync_non_meaning(),
        "additional_basis_required": _build_additional_basis_required(outcome, request),
        "what_remains_open": _copy(WHAT_REMAINS_OPEN),
        "non_claims": _copy(REQUIRED_NON_CLAIMS),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
            "block_reason": block_reason if outcome == OUTCOME_BLOCKED else None,
        },
    }
    result["distributed_sync_non_sync_summary"] = (
        build_distributed_synchronization_non_synchronization_summary(result)
    )
    return result


def resolve_distributed_synchronization_non_synchronization_boundary_from_path(
    declared_sync_non_sync_request_path: Path | str,
) -> dict[str, Any]:
    request, error = _read_json_object(declared_sync_non_sync_request_path)
    if error:
        block_code = (
            BLOCK_DECLARED_SYNC_NON_SYNC_REQUEST_UNREADABLE
            if error == "unreadable"
            else BLOCK_DECLARED_SYNC_NON_SYNC_REQUEST_MALFORMED
        )
        request = {
            "sync_non_sync_request_path": _stringify(declared_sync_non_sync_request_path),
            "block_reason": block_code,
        }
        result = resolve_distributed_synchronization_non_synchronization_boundary(request)
        result["outcome"] = OUTCOME_BLOCKED
        result["block"] = {
            "blocked": True,
            "block_code": block_code,
            "block_reason": block_code,
        }
        result["sync_non_sync_statement"]["block_code"] = block_code
        result["sync_non_sync_statement"]["block_reason"] = block_code
        result["distributed_sync_non_sync_summary"] = (
            build_distributed_synchronization_non_synchronization_summary(result)
        )
        return result
    if request is None:
        raise DistributedSynchronizationNonSynchronizationBoundaryError(
            "request path returned neither request nor error"
        )
    request["sync_non_sync_request_path"] = _stringify(declared_sync_non_sync_request_path)
    return resolve_distributed_synchronization_non_synchronization_boundary(request)


def write_distributed_synchronization_non_synchronization_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    if not isinstance(result, Mapping):
        raise DistributedSynchronizationNonSynchronizationBoundaryError(
            "result must be a mapping"
        )
    metadata = _as_mapping(result.get("distributed_sync_non_sync_metadata"))
    declared = _as_mapping(result.get("declared_sync_non_sync_question"))
    result_id = _first_present(
        metadata.get("distributed_sync_non_sync_result_id"),
        declared.get("sync_non_sync_request_id"),
        declared.get("selected_carrier_role_result_id"),
        "distributed_sync_non_sync_result",
    )
    filename = f"{_sanitize_filename(result_id)}.json"
    if output_path is None:
        target = DISTRIBUTED_SYNCHRONIZATION_NON_SYNCHRONIZATION_BOUNDARY_ROOT / filename
    else:
        candidate = Path(output_path)
        if candidate.suffix:
            target = candidate
        else:
            target = candidate / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _deduplicate_path(target)
    with target.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps(result, indent=2, sort_keys=True))
        handle.write("\n")
    return target


def build_declared_distributed_synchronization_non_synchronization_request(
    sync_non_sync_request_id: str,
    sync_non_sync_question: str,
    selected_carrier_role_result: Mapping[str, Any] | str,
    sync_non_sync_basis: Mapping[str, Any] | str,
    sync_non_sync_postures: Sequence[str] | Mapping[str, Any],
    sync_non_sync_intent: str = INTENT_RECORD,
    *,
    selected_carrier_role_result_path: str | None = None,
    selected_carrier_role_result_id: str | None = None,
    selected_carrier_role_result_outcome: str | None = None,
    requested_sync_non_sync_outcome: str = OUTCOME_RECORDED,
    selected_carrier_context: Sequence[Mapping[str, Any]] | Mapping[str, Any] | None = None,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_sufficient_reason: str | None = None,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "sync_non_sync_request_id": sync_non_sync_request_id,
        "sync_non_sync_question": sync_non_sync_question,
        "sync_non_sync_intent": sync_non_sync_intent,
        "sync_non_sync_basis": _copy(sync_non_sync_basis),
        "sync_non_sync_postures": _copy(sync_non_sync_postures),
        "selected_carrier_role_result_id": selected_carrier_role_result_id,
        "selected_carrier_role_result_outcome": selected_carrier_role_result_outcome,
        "expected_selected_carrier_role_outcome": EXPECTED_CARRIER_ROLE_OUTCOME,
        "requested_sync_non_sync_outcome": requested_sync_non_sync_outcome,
        "selected_carrier_context": _copy(selected_carrier_context)
        if selected_carrier_context is not None
        else None,
        "additional_basis_context": _copy(additional_basis_context)
        if additional_basis_context is not None
        else None,
        "not_sufficient_reason": not_sufficient_reason,
        "declared_non_claims": _copy(REQUIRED_NON_CLAIMS),
    }
    if selected_carrier_role_result_path is not None:
        request["selected_carrier_role_result_path"] = selected_carrier_role_result_path
        if isinstance(selected_carrier_role_result, Mapping):
            request["selected_carrier_role_result"] = _copy(selected_carrier_role_result)
    elif isinstance(selected_carrier_role_result, Mapping):
        request["selected_carrier_role_result"] = _copy(selected_carrier_role_result)
    else:
        request["selected_carrier_role_result_path"] = _stringify(
            selected_carrier_role_result
        )

    if isinstance(sync_non_sync_basis, Mapping):
        request.setdefault("carrier_role_basis", sync_non_sync_basis.get("carrier_role_basis"))
        request.setdefault("carrier_role_shapes", sync_non_sync_basis.get("carrier_role_shapes"))
        request.setdefault(
            "source_body_lineage_basis",
            sync_non_sync_basis.get("source_body_lineage_basis"),
        )
        request.setdefault(
            "distributed_standing_basis",
            sync_non_sync_basis.get("distributed_standing_basis"),
        )
        request.setdefault(
            "proposed_synchronization_posture",
            sync_non_sync_basis.get("proposed_synchronization_posture"),
        )
        request.setdefault(
            "proposed_non_synchronization_posture",
            sync_non_sync_basis.get("proposed_non_synchronization_posture"),
        )
        if selected_carrier_context is None:
            request["selected_carrier_context"] = sync_non_sync_basis.get(
                "selected_carrier_context"
            )
        for key in (
            "carrier_b_success_context",
            "carrier_c_block_context",
            "b_c_divergence_context",
            "refusal_blocked_attempt_context",
            "projection_mismatch_context",
        ):
            if key in sync_non_sync_basis:
                request[key] = sync_non_sync_basis.get(key)
    return request
