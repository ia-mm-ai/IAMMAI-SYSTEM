"""Resolve distributed carrier operational role basis for one eligible matter.

This module records which carrier role shapes may be recognized as bounded
context before any future operation admission. It does not activate carrier
roles, assign live operation, create carrier authority, create carrier
currentness, select carriers, create hierarchy, admit operation, authorize
operation, execute operation, synchronize repositories, transfer a body,
create a second body, authorize continuation, create consequence, create
public readiness, claim final completion, or schedule follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class DistributedCarrierOperationalRoleBoundaryError(Exception):
    """Raised for impossible distributed carrier role boundary failures."""


RESOLVER_MODULE = "resolve_distributed_carrier_operational_role_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "distributed_carrier_operational_role_boundary_result"
REPO_ROOT = Path(__file__).resolve().parents[1]
DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_distributed_carrier_operational_role_boundary"
)

INTENT_RECORD = "RECORD_DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_REVIEW"
SUPPORTED_ROLE_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

OUTCOME_RECORDED = "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS_RECORDED"
OUTCOME_NOT_SUFFICIENT = "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS_NOT_SUFFICIENT"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_REVIEW_BLOCKED"
SUPPORTED_ROLE_OUTCOMES = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_SUFFICIENT,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

EXPECTED_AUTHORITY_OUTCOME = "SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS_RECORDED"
EXPECTED_FAILED_CHECK_COUNT = 0

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

BLOCK_ROLE_QUESTION_UNDECLARED = "ROLE_QUESTION_UNDECLARED"
BLOCK_ROLE_INTENT_UNSUPPORTED = "ROLE_INTENT_UNSUPPORTED"
BLOCK_SOURCE_BODY_AUTHORITY_RESULT_MISSING = "SOURCE_BODY_AUTHORITY_RESULT_MISSING"
BLOCK_SOURCE_BODY_AUTHORITY_RESULT_UNREADABLE = "SOURCE_BODY_AUTHORITY_RESULT_UNREADABLE"
BLOCK_SOURCE_BODY_AUTHORITY_RESULT_MALFORMED = "SOURCE_BODY_AUTHORITY_RESULT_MALFORMED"
BLOCK_SOURCE_BODY_AUTHORITY_RESULT_OUTCOME_MISSING = (
    "SOURCE_BODY_AUTHORITY_RESULT_OUTCOME_MISSING"
)
BLOCK_SOURCE_BODY_AUTHORITY_RESULT_NOT_RECORDED = (
    "SOURCE_BODY_AUTHORITY_RESULT_NOT_RECORDED"
)
BLOCK_SOURCE_BODY_AUTHORITY_RESULT_HAS_FAILED_CHECKS = (
    "SOURCE_BODY_AUTHORITY_RESULT_HAS_FAILED_CHECKS"
)
BLOCK_SELECTED_ELIGIBILITY_RESULT_MISSING = "SELECTED_ELIGIBILITY_RESULT_MISSING"
BLOCK_SELECTED_MATTER_DECLARATION_MISSING = "SELECTED_MATTER_DECLARATION_MISSING"
BLOCK_SELECTED_OPERATION_CANDIDATE_MISSING = "SELECTED_OPERATION_CANDIDATE_MISSING"
BLOCK_SELECTED_OPERATION_MATTER_MISSING = "SELECTED_OPERATION_MATTER_MISSING"
BLOCK_SOURCE_BODY_AUTHORITY_BASIS_MISSING = "SOURCE_BODY_AUTHORITY_BASIS_MISSING"
BLOCK_SELECTED_CARRIER_CONTEXT_MALFORMED = "SELECTED_CARRIER_CONTEXT_MALFORMED"
BLOCK_UNSUPPORTED_CARRIER_ROLE_SHAPE = "UNSUPPORTED_CARRIER_ROLE_SHAPE"
BLOCK_ROLE_REVIEW_ACTIVATES_CARRIER_ROLE = "ROLE_REVIEW_ACTIVATES_CARRIER_ROLE"
BLOCK_ROLE_REVIEW_ASSIGNS_LIVE_OPERATION = "ROLE_REVIEW_ASSIGNS_LIVE_OPERATION"
BLOCK_ROLE_REVIEW_CREATES_CARRIER_AUTHORITY = (
    "ROLE_REVIEW_CREATES_CARRIER_AUTHORITY"
)
BLOCK_ROLE_REVIEW_CREATES_PERMISSION = "ROLE_REVIEW_CREATES_PERMISSION"
BLOCK_ROLE_REVIEW_CREATES_CARRIER_CURRENTNESS = (
    "ROLE_REVIEW_CREATES_CARRIER_CURRENTNESS"
)
BLOCK_ROLE_REVIEW_SELECTS_CURRENT_CARRIER = "ROLE_REVIEW_SELECTS_CURRENT_CARRIER"
BLOCK_ROLE_REVIEW_SELECTS_WINNING_CARRIER = "ROLE_REVIEW_SELECTS_WINNING_CARRIER"
BLOCK_ROLE_REVIEW_INVALIDATES_LOSING_CARRIER = (
    "ROLE_REVIEW_INVALIDATES_LOSING_CARRIER"
)
BLOCK_ROLE_REVIEW_CREATES_CARRIER_HIERARCHY = (
    "ROLE_REVIEW_CREATES_CARRIER_HIERARCHY"
)
BLOCK_ROLE_REVIEW_REPLACES_SOURCE = "ROLE_REVIEW_REPLACES_SOURCE"
BLOCK_ROLE_REVIEW_ADMITS_OPERATION = "ROLE_REVIEW_ADMITS_OPERATION"
BLOCK_ROLE_REVIEW_AUTHORIZES_OPERATION = "ROLE_REVIEW_AUTHORIZES_OPERATION"
BLOCK_ROLE_REVIEW_EXECUTES_OPERATION = "ROLE_REVIEW_EXECUTES_OPERATION"
BLOCK_ROLE_REVIEW_AUTHORIZES_REPOSITORY_SYNC = (
    "ROLE_REVIEW_AUTHORIZES_REPOSITORY_SYNC"
)
BLOCK_ROLE_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER = (
    "ROLE_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER"
)
BLOCK_ROLE_REVIEW_CREATES_SECOND_BODY = "ROLE_REVIEW_CREATES_SECOND_BODY"
BLOCK_ROLE_REVIEW_AUTHORIZES_CONTINUATION = "ROLE_REVIEW_AUTHORIZES_CONTINUATION"
BLOCK_ROLE_REVIEW_CREATES_TRUTH_OR_ACTION = "ROLE_REVIEW_CREATES_TRUTH_OR_ACTION"
BLOCK_ROLE_REVIEW_CREATES_CONSEQUENCE = "ROLE_REVIEW_CREATES_CONSEQUENCE"
BLOCK_ROLE_REVIEW_RESOLVES_DIVERGENCE = "ROLE_REVIEW_RESOLVES_DIVERGENCE"
BLOCK_ROLE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL = (
    "ROLE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"
)
BLOCK_ROLE_REVIEW_CREATES_PUBLIC_READINESS = (
    "ROLE_REVIEW_CREATES_PUBLIC_READINESS"
)
BLOCK_ROLE_REVIEW_CLAIMS_FINAL_COMPLETION = "ROLE_REVIEW_CLAIMS_FINAL_COMPLETION"
BLOCK_ROLE_REVIEW_SCHEDULES_FOLLOW_ON_WORK = (
    "ROLE_REVIEW_SCHEDULES_FOLLOW_ON_WORK"
)
BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED = "MUTATION_REPLAY_OR_MERGE_DETECTED"
BLOCK_NON_CLAIM_MISSING_OR_FLIPPED = "NON_CLAIM_MISSING_OR_FLIPPED"
BLOCK_DECLARED_ROLE_REQUEST_UNREADABLE = "DECLARED_ROLE_REQUEST_UNREADABLE"
BLOCK_DECLARED_ROLE_REQUEST_MALFORMED = "DECLARED_ROLE_REQUEST_MALFORMED"
BLOCK_ROLE_REVIEW_REQUEST_EXPLICITLY_BLOCKED = (
    "ROLE_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
)

REQUIRED_NON_CLAIMS = {
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
    "repository_synchronization_authorized": False,
    "full_body_transfer_authorized": False,
    "second_body_created": False,
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

SOURCE_BODY_AUTHORITY_NON_CLAIM_FIELDS = (
    "authority_granted",
    "authority_created",
    "permission_created",
    "operation_admitted",
    "operation_authorized",
    "operation_executed",
    "carrier_roles_defined",
    "repository_synchronization_authorized",
    "full_body_transfer_authorized",
    "second_body_created",
    "continuation_authorized",
    "distributed_operation_authorized",
    "carrier_currentness_created",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "source_replaced",
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
)

ROLE_COLLAPSE_FIELDS = (
    ("carrier_role_activated", BLOCK_ROLE_REVIEW_ACTIVATES_CARRIER_ROLE),
    ("carrier_roles_activated", BLOCK_ROLE_REVIEW_ACTIVATES_CARRIER_ROLE),
    ("role_review_activates_carrier_role", BLOCK_ROLE_REVIEW_ACTIVATES_CARRIER_ROLE),
    ("role_activated", BLOCK_ROLE_REVIEW_ACTIVATES_CARRIER_ROLE),
    (
        "carrier_role_assigned_for_operation",
        BLOCK_ROLE_REVIEW_ASSIGNS_LIVE_OPERATION,
    ),
    (
        "carrier_roles_assigned_for_operation",
        BLOCK_ROLE_REVIEW_ASSIGNS_LIVE_OPERATION,
    ),
    ("carrier_assigned_to_live_operation", BLOCK_ROLE_REVIEW_ASSIGNS_LIVE_OPERATION),
    ("assigns_live_operation", BLOCK_ROLE_REVIEW_ASSIGNS_LIVE_OPERATION),
    ("carrier_authority_created", BLOCK_ROLE_REVIEW_CREATES_CARRIER_AUTHORITY),
    ("carrier_becomes_authority", BLOCK_ROLE_REVIEW_CREATES_CARRIER_AUTHORITY),
    (
        "role_review_creates_carrier_authority",
        BLOCK_ROLE_REVIEW_CREATES_CARRIER_AUTHORITY,
    ),
    ("authority_created", BLOCK_ROLE_REVIEW_CREATES_CARRIER_AUTHORITY),
    ("permission_created", BLOCK_ROLE_REVIEW_CREATES_PERMISSION),
    ("carrier_currentness_created", BLOCK_ROLE_REVIEW_CREATES_CARRIER_CURRENTNESS),
    ("carrier_becomes_currentness", BLOCK_ROLE_REVIEW_CREATES_CARRIER_CURRENTNESS),
    ("current_carrier_selected", BLOCK_ROLE_REVIEW_SELECTS_CURRENT_CARRIER),
    ("carrier_becomes_current", BLOCK_ROLE_REVIEW_SELECTS_CURRENT_CARRIER),
    ("winning_carrier_selected", BLOCK_ROLE_REVIEW_SELECTS_WINNING_CARRIER),
    ("carrier_b_success_becomes_winner", BLOCK_ROLE_REVIEW_SELECTS_WINNING_CARRIER),
    (
        "carrier_b_success_implies_winner_role",
        BLOCK_ROLE_REVIEW_SELECTS_WINNING_CARRIER,
    ),
    ("losing_carrier_invalidated", BLOCK_ROLE_REVIEW_INVALIDATES_LOSING_CARRIER),
    ("carrier_c_block_becomes_loser", BLOCK_ROLE_REVIEW_INVALIDATES_LOSING_CARRIER),
    (
        "carrier_c_block_implies_loser_invalidation",
        BLOCK_ROLE_REVIEW_INVALIDATES_LOSING_CARRIER,
    ),
    ("carrier_hierarchy_created", BLOCK_ROLE_REVIEW_CREATES_CARRIER_HIERARCHY),
    ("carrier_hierarchy_defined", BLOCK_ROLE_REVIEW_CREATES_CARRIER_HIERARCHY),
    ("carrier_rank_created", BLOCK_ROLE_REVIEW_CREATES_CARRIER_HIERARCHY),
    ("source_replaced", BLOCK_ROLE_REVIEW_REPLACES_SOURCE),
    ("source_replaced_by_carrier", BLOCK_ROLE_REVIEW_REPLACES_SOURCE),
    ("carrier_becomes_source", BLOCK_ROLE_REVIEW_REPLACES_SOURCE),
    ("operation_admitted", BLOCK_ROLE_REVIEW_ADMITS_OPERATION),
    ("operation_authorized", BLOCK_ROLE_REVIEW_AUTHORIZES_OPERATION),
    ("distributed_operation_authorized", BLOCK_ROLE_REVIEW_AUTHORIZES_OPERATION),
    ("operation_executed", BLOCK_ROLE_REVIEW_EXECUTES_OPERATION),
    (
        "repository_synchronization_authorized",
        BLOCK_ROLE_REVIEW_AUTHORIZES_REPOSITORY_SYNC,
    ),
    ("repository_sync_authorized", BLOCK_ROLE_REVIEW_AUTHORIZES_REPOSITORY_SYNC),
    ("full_body_transfer_authorized", BLOCK_ROLE_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER),
    ("second_body_created", BLOCK_ROLE_REVIEW_CREATES_SECOND_BODY),
    ("continuation_authorized", BLOCK_ROLE_REVIEW_AUTHORIZES_CONTINUATION),
    ("truth_created", BLOCK_ROLE_REVIEW_CREATES_TRUTH_OR_ACTION),
    ("action_authorized", BLOCK_ROLE_REVIEW_CREATES_TRUTH_OR_ACTION),
    ("consequence_created", BLOCK_ROLE_REVIEW_CREATES_CONSEQUENCE),
    ("divergence_resolved", BLOCK_ROLE_REVIEW_RESOLVES_DIVERGENCE),
    ("evidence_erased", BLOCK_ROLE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("refusal_erased", BLOCK_ROLE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("blocked_attempt_erased", BLOCK_ROLE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("projection_mismatch_hidden", BLOCK_ROLE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("public_launch_readiness_created", BLOCK_ROLE_REVIEW_CREATES_PUBLIC_READINESS),
    ("public_readiness_created", BLOCK_ROLE_REVIEW_CREATES_PUBLIC_READINESS),
    ("final_completion_claimed", BLOCK_ROLE_REVIEW_CLAIMS_FINAL_COMPLETION),
    ("final_governance_completed", BLOCK_ROLE_REVIEW_CLAIMS_FINAL_COMPLETION),
    ("final_continuity_completed", BLOCK_ROLE_REVIEW_CLAIMS_FINAL_COMPLETION),
    ("final_system_identity_completed", BLOCK_ROLE_REVIEW_CLAIMS_FINAL_COMPLETION),
    ("follow_on_work_authorized", BLOCK_ROLE_REVIEW_SCHEDULES_FOLLOW_ON_WORK),
    (
        "self_orientation_successor_scheduled",
        BLOCK_ROLE_REVIEW_SCHEDULES_FOLLOW_ON_WORK,
    ),
    ("mutation_performed", BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED),
    ("replay_performed", BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED),
    ("merge_performed", BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED),
)

WHAT_REMAINS_OPEN = {
    "synchronization_non_synchronization_boundary": (
        "open_not_scheduled_not_authorized_not_executed"
    ),
    "distributed_operation_admission_transition_authority": (
        "open_not_scheduled_not_authorized_not_executed"
    ),
    "distributed_refusal_and_abort_law": "open_not_scheduled_not_authorized_not_executed",
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


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


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


def _is_false(value: Any) -> bool:
    return value is False


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
    raw = _stringify(value).strip() or "distributed_carrier_operational_role"
    allowed = []
    for character in raw:
        if character.isalnum() or character in {"-", "_", "."}:
            allowed.append(character)
        else:
            allowed.append("_")
    sanitized = "".join(allowed).strip("._")
    return sanitized[:180] or "distributed_carrier_operational_role"


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
    raise DistributedCarrierOperationalRoleBoundaryError(
        f"could not create unique output path for {path}"
    )


def _extract_failed_check_count(result: Mapping[str, Any]) -> int | None:
    summary_value = _first_present(
        _get_path_value(
            result, ("distributed_carrier_operational_role_summary", "failed_check_count")
        ),
        _get_path_value(
            result, ("source_body_operational_authority_summary", "failed_check_count")
        ),
        _get_path_value(result, ("authority_statement", "failed_check_count")),
    )
    if summary_value is None:
        checks = result.get("authority_checks") or result.get("role_checks")
        if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray)):
            return _failed_check_count([check for check in checks if isinstance(check, Mapping)])
        return None
    try:
        return int(summary_value)
    except (TypeError, ValueError):
        return None


def _extract_source_body_authority_result_id(result: Mapping[str, Any]) -> str | None:
    value = _first_present(
        _get_path_value(
            result,
            (
                "source_body_operational_authority_metadata",
                "source_body_operational_authority_result_id",
            ),
        ),
        _get_path_value(
            result,
            (
                "distributed_carrier_operational_role_summary",
                "selected_source_body_authority_result_id",
            ),
        ),
        _get_path_value(
            result,
            (
                "source_body_operational_authority_summary",
                "authority_request_id",
            ),
        ),
        _get_path_value(result, ("declared_authority_question", "authority_request_id")),
        result.get("source_body_authority_result_id"),
        result.get("selected_source_body_authority_result_id"),
    )
    return _stringify(value) if value is not None else None


def _extract_source_body_authority_outcome(result: Mapping[str, Any]) -> str | None:
    value = _first_present(
        result.get("outcome"),
        _get_path_value(result, ("source_body_operational_authority_summary", "outcome")),
        _get_path_value(result, ("declared_authority_question", "selected_eligibility_result_outcome")),
    )
    return _stringify(value) if value is not None else None


def _basis_mapping(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("carrier_role_basis")
    return _copy(basis) if isinstance(basis, Mapping) else {}


def _source_authority_basis_mapping(
    request: Mapping[str, Any], source_authority_result: Mapping[str, Any]
) -> dict[str, Any]:
    basis = _first_present(
        request.get("source_body_authority_basis"),
        _basis_mapping(request).get("source_body_authority_basis"),
        source_authority_result.get("source_body_authority_basis"),
    )
    return _copy(basis) if isinstance(basis, Mapping) else {}


def _selected_eligibility_result(
    request: Mapping[str, Any], source_authority_result: Mapping[str, Any]
) -> Any:
    selected_section = source_authority_result.get("selected_eligibility_result")
    return _first_present(
        request.get("selected_eligibility_result"),
        _get_path_value(_as_mapping(selected_section), ("selected_eligibility_result",)),
        selected_section,
        _get_path_value(
            source_authority_result,
            ("selected_operation_matter", "selected_eligibility_result"),
        ),
    )


def _selected_matter_declaration(
    request: Mapping[str, Any], source_authority_result: Mapping[str, Any]
) -> Any:
    eligibility = _as_mapping(_selected_eligibility_result(request, source_authority_result))
    return _first_present(
        request.get("selected_matter_declaration"),
        _get_path_value(
            source_authority_result,
            ("selected_operation_matter", "selected_matter_declaration"),
        ),
        eligibility.get("selected_matter_declaration"),
        _get_path_value(eligibility, ("eligibility_basis", "selected_matter_declaration_result")),
    )


def _selected_operation_candidate(
    request: Mapping[str, Any], source_authority_result: Mapping[str, Any]
) -> Any:
    eligibility = _as_mapping(_selected_eligibility_result(request, source_authority_result))
    return _first_present(
        request.get("selected_operation_candidate"),
        _get_path_value(
            source_authority_result,
            ("selected_operation_matter", "selected_operation_candidate"),
        ),
        eligibility.get("selected_operation_candidate"),
        _get_path_value(eligibility, ("eligibility_basis", "selected_operation_candidate")),
        _get_path_value(eligibility, ("eligibility_basis", "selected_operation_candidate_identity")),
    )


def _selected_operation_matter(
    request: Mapping[str, Any], source_authority_result: Mapping[str, Any]
) -> Any:
    eligibility = _as_mapping(_selected_eligibility_result(request, source_authority_result))
    return _first_present(
        request.get("selected_operation_matter"),
        _get_path_value(
            source_authority_result,
            ("selected_operation_matter", "selected_operation_matter"),
        ),
        eligibility.get("selected_operation_matter"),
        _get_path_value(eligibility, ("eligibility_basis", "selected_operation_matter")),
    )


def _selected_operation_question(
    request: Mapping[str, Any], source_authority_result: Mapping[str, Any]
) -> Any:
    eligibility = _as_mapping(_selected_eligibility_result(request, source_authority_result))
    return _first_present(
        request.get("selected_operation_question"),
        request.get("operation_question"),
        _get_path_value(
            source_authority_result,
            ("selected_operation_matter", "selected_operation_question"),
        ),
        _get_path_value(eligibility, ("eligibility_basis", "selected_operation_question")),
        _get_path_value(
            eligibility,
            ("distributed_operation_eligibility_summary", "operation_question"),
        ),
        _get_path_value(eligibility, ("selected_operation_candidate", "selected_operation_question")),
        _get_path_value(eligibility, ("selected_operation_candidate", "declared_operation_question")),
    )


def _selected_operation_purpose(
    request: Mapping[str, Any], source_authority_result: Mapping[str, Any]
) -> Any:
    eligibility = _as_mapping(_selected_eligibility_result(request, source_authority_result))
    return _first_present(
        request.get("selected_operation_purpose"),
        request.get("operation_purpose"),
        _get_path_value(
            source_authority_result,
            ("selected_operation_matter", "selected_operation_purpose"),
        ),
        _get_path_value(eligibility, ("eligibility_basis", "selected_operation_purpose")),
        _get_path_value(
            eligibility,
            ("distributed_operation_eligibility_summary", "operation_purpose"),
        ),
        eligibility.get("operation_purpose"),
    )


def _proposed_operation_kind(
    request: Mapping[str, Any], source_authority_result: Mapping[str, Any]
) -> Any:
    eligibility = _as_mapping(_selected_eligibility_result(request, source_authority_result))
    return _first_present(
        request.get("proposed_operation_kind"),
        _get_path_value(
            source_authority_result,
            ("selected_operation_matter", "proposed_operation_kind"),
        ),
        _get_path_value(eligibility, ("eligibility_basis", "selected_proposed_operation_kind")),
        _get_path_value(
            eligibility,
            ("distributed_operation_eligibility_summary", "proposed_operation_kind"),
        ),
    )


def _source_body_lineage_basis(
    request: Mapping[str, Any],
    role_basis: Mapping[str, Any],
    source_authority_basis: Mapping[str, Any],
) -> Any:
    return _first_present(
        request.get("source_body_lineage_basis"),
        role_basis.get("source_body_lineage_basis"),
        source_authority_basis.get("source_body_lineage_basis"),
        _get_path_value(source_authority_basis, ("source_body_authority_basis", "source_body_lineage_basis")),
    )


def _selected_carrier_context(
    request: Mapping[str, Any],
    role_basis: Mapping[str, Any],
    source_authority_basis: Mapping[str, Any],
) -> Any:
    return _first_present(
        request.get("selected_carrier_context"),
        role_basis.get("selected_carrier_context"),
        source_authority_basis.get("selected_carrier_context"),
        _get_path_value(source_authority_basis, ("source_body_authority_basis", "selected_carrier_context")),
    )


def _distributed_standing_basis(
    request: Mapping[str, Any],
    role_basis: Mapping[str, Any],
    source_authority_basis: Mapping[str, Any],
) -> Any:
    return _first_present(
        request.get("distributed_standing_basis"),
        role_basis.get("distributed_standing_basis"),
        source_authority_basis.get("distributed_standing_basis"),
        _get_path_value(source_authority_basis, ("source_body_authority_basis", "distributed_standing_basis")),
    )


def _context_value(
    request: Mapping[str, Any],
    role_basis: Mapping[str, Any],
    carrier_context: Any,
    key: str,
) -> Any:
    carrier_map = _as_mapping(carrier_context)
    return _first_present(request.get(key), role_basis.get(key), carrier_map.get(key))


def _carrier_context_explicitly_not_required(
    request: Mapping[str, Any], role_basis: Mapping[str, Any]
) -> bool:
    return any(
        _is_true(value)
        for value in (
            request.get("selected_carrier_context_not_required"),
            request.get("carrier_context_not_required"),
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


def _selected_role_shape_values(value: Any) -> list[str]:
    if isinstance(value, Mapping):
        shape_source = _first_present(
            value.get("selected_carrier_role_shapes"),
            value.get("carrier_role_shapes"),
            value.get("role_shapes"),
            value.get("selected_shapes"),
        )
        if shape_source is None:
            shape_source = [
                key for key, enabled in value.items() if key in SUPPORTED_CARRIER_ROLE_SHAPES and enabled
            ]
    else:
        shape_source = value

    if isinstance(shape_source, str):
        return [shape_source]
    if isinstance(shape_source, Sequence) and not isinstance(
        shape_source, (str, bytes, bytearray)
    ):
        shapes: list[str] = []
        for item in shape_source:
            if isinstance(item, str):
                shapes.append(item)
            elif isinstance(item, Mapping):
                role_shape = _first_present(
                    item.get("role_shape"),
                    item.get("carrier_role_shape"),
                    item.get("shape"),
                )
                if role_shape is not None:
                    shapes.append(_stringify(role_shape))
        return shapes
    return []


def _selected_role_shapes(request: Mapping[str, Any]) -> list[str]:
    return _selected_role_shape_values(request.get("carrier_role_shapes"))


def _unsupported_role_shapes(shapes: Sequence[str]) -> list[str]:
    return [shape for shape in shapes if shape not in SUPPORTED_CARRIER_ROLE_SHAPES]


def _declared_non_claims_are_false(request: Mapping[str, Any]) -> bool:
    claims = request.get("declared_non_claims")
    if not isinstance(claims, Mapping):
        return False
    return all(claim in claims and claims[claim] is False for claim in REQUIRED_NON_CLAIMS)


def _source_authority_non_claims_are_false(source_authority_result: Mapping[str, Any]) -> bool:
    claims = source_authority_result.get("non_claims")
    statement = _as_mapping(source_authority_result.get("authority_statement"))
    if not isinstance(claims, Mapping):
        claims = {}
    for claim in SOURCE_BODY_AUTHORITY_NON_CLAIM_FIELDS:
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
        for field, code in ROLE_COLLAPSE_FIELDS:
            if _is_true(container.get(field)):
                return code
    return None


def _result_id(role_request_id: Any, selected_authority_result_id: Any) -> str:
    source = _first_present(role_request_id, selected_authority_result_id)
    return f"{_sanitize_filename(source)}__distributed_carrier_operational_role_result"


def _load_selected_source_body_authority_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    selected_path = request.get("selected_source_body_authority_result_path")
    if _is_non_empty(selected_path):
        loaded, error = _read_json_object(_stringify(selected_path))
        if error == "unreadable":
            return None, BLOCK_SOURCE_BODY_AUTHORITY_RESULT_UNREADABLE, _stringify(selected_path)
        if error == "malformed":
            return None, BLOCK_SOURCE_BODY_AUTHORITY_RESULT_MALFORMED, _stringify(selected_path)
        return _copy(loaded), None, _stringify(selected_path)

    selected = request.get("selected_source_body_authority_result")
    if isinstance(selected, Mapping):
        return _copy(selected), None, None
    if _is_non_empty(selected):
        return None, BLOCK_SOURCE_BODY_AUTHORITY_RESULT_MALFORMED, None
    return None, BLOCK_SOURCE_BODY_AUTHORITY_RESULT_MISSING, None


def _build_declared_role_question(
    request: Mapping[str, Any],
    selected_authority_result_id: str | None,
    selected_authority_outcome: str | None,
    request_path: str | None,
) -> dict[str, Any]:
    return {
        "role_request_id": request.get("role_request_id"),
        "role_question": request.get("role_question"),
        "role_intent": request.get("role_intent"),
        "role_request_path": request_path,
        "selected_source_body_authority_result_id": _first_present(
            request.get("selected_source_body_authority_result_id"),
            selected_authority_result_id,
        ),
        "selected_source_body_authority_result_outcome": _first_present(
            request.get("selected_source_body_authority_result_outcome"),
            request.get("expected_selected_authority_outcome"),
            selected_authority_outcome,
        ),
        "role_boundary_is_not_role_activation": True,
        "role_boundary_is_not_role_assignment": True,
        "role_boundary_is_not_carrier_authority": True,
        "role_boundary_is_not_carrier_currentness": True,
        "role_boundary_is_not_current_carrier_selection": True,
        "role_boundary_is_not_winner_loser_selection": True,
        "role_boundary_is_not_admission": True,
        "role_boundary_is_not_authorization": True,
        "role_boundary_is_not_execution": True,
        "role_boundary_is_not_operation": True,
        "role_boundary_is_not_synchronization": True,
        "role_boundary_is_not_full_body_transfer": True,
        "role_boundary_is_not_continuation": True,
        "role_boundary_is_not_permission": True,
    }


def _build_selected_source_body_authority_section(
    selected_authority_result: Mapping[str, Any] | None,
    selected_authority_result_path: str | None,
    selected_authority_result_id: str | None,
    selected_authority_outcome: str | None,
    failed_check_count: int | None,
) -> dict[str, Any]:
    result = _copy(selected_authority_result) if isinstance(selected_authority_result, Mapping) else None
    return {
        "selected_source_body_authority_result": result,
        "selected_source_body_authority_result_path": selected_authority_result_path,
        "selected_source_body_authority_result_id": selected_authority_result_id,
        "selected_source_body_authority_result_outcome": selected_authority_outcome,
        "selected_source_body_authority_result_outcome_is_recorded": (
            selected_authority_outcome == EXPECTED_AUTHORITY_OUTCOME
        ),
        "selected_source_body_authority_result_failed_check_count": failed_check_count,
        "selected_source_body_authority_result_failed_check_count_zero": (
            failed_check_count == EXPECTED_FAILED_CHECK_COUNT
        ),
        "selected_source_body_authority_result_remains_authority_basis_only": True,
        "selected_source_body_authority_result_did_not_grant_authority": True,
        "selected_source_body_authority_result_did_not_create_authority": True,
        "selected_source_body_authority_result_did_not_create_permission": True,
        "selected_source_body_authority_result_did_not_define_carrier_roles": True,
        "selected_source_body_authority_result_did_not_admit_operation": True,
        "selected_source_body_authority_result_did_not_authorize_operation": True,
        "selected_source_body_authority_result_did_not_execute_operation": True,
    }


def _build_selected_operation_matter_section(
    request: Mapping[str, Any],
    selected_authority_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    authority = selected_authority_result or {}
    eligibility = _selected_eligibility_result(request, authority)
    matter_declaration = _selected_matter_declaration(request, authority)
    candidate = _selected_operation_candidate(request, authority)
    matter = _selected_operation_matter(request, authority)
    operation_question = _selected_operation_question(request, authority)
    operation_purpose = _selected_operation_purpose(request, authority)
    proposed_kind = _proposed_operation_kind(request, authority)
    candidate_mapping = _as_mapping(candidate)
    matter_mapping = _as_mapping(matter)
    return {
        "selected_source_body_authority_result": _copy(authority) if authority else None,
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
            _get_path_value(
                authority,
                (
                    "source_body_operational_authority_summary",
                    "selected_operation_candidate_id",
                ),
            ),
        ),
        "selected_operation_matter_id": _first_present(
            matter_mapping.get("operation_matter_id"),
            matter_mapping.get("selected_operation_matter_id"),
            _get_path_value(
                authority,
                ("source_body_operational_authority_summary", "selected_operation_matter_id"),
            ),
        ),
        "source_body_authority_basis_remains_basis_only": True,
        "matter_remains_declaration_only": True,
        "candidate_remains_candidate_only": True,
        "eligibility_remains_eligibility_only": True,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
    }


def _build_carrier_role_basis_section(
    request: Mapping[str, Any],
    selected_authority_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    authority = selected_authority_result or {}
    role_basis = _basis_mapping(request)
    source_authority_basis = _source_authority_basis_mapping(request, authority)
    source_body_lineage = _source_body_lineage_basis(
        request, role_basis, source_authority_basis
    )
    carrier_context = _selected_carrier_context(
        request, role_basis, source_authority_basis
    )
    standing_basis = _distributed_standing_basis(request, role_basis, source_authority_basis)
    return {
        "carrier_role_basis": _copy(request.get("carrier_role_basis")),
        "source_body_authority_basis": _copy(source_authority_basis)
        if source_authority_basis
        else _copy(request.get("source_body_authority_basis")),
        "source_body_lineage_basis": _copy(source_body_lineage),
        "selected_carrier_context": _copy(carrier_context),
        "carrier_b_success_context": _copy(
            _context_value(request, role_basis, carrier_context, "carrier_b_success_context")
        ),
        "carrier_c_block_context": _copy(
            _context_value(request, role_basis, carrier_context, "carrier_c_block_context")
        ),
        "b_c_divergence_context": _copy(
            _context_value(request, role_basis, carrier_context, "b_c_divergence_context")
        ),
        "refusal_blocked_attempt_context": _copy(
            _context_value(
                request, role_basis, carrier_context, "refusal_blocked_attempt_context"
            )
        ),
        "projection_mismatch_context": _copy(
            _context_value(request, role_basis, carrier_context, "projection_mismatch_context")
        ),
        "distributed_standing_basis": _copy(standing_basis),
        "distributed_standing_basis_is_basis_only": True
        if _is_non_empty(standing_basis)
        else False,
        "carrier_context_is_not_authority": True,
        "carrier_context_is_not_currentness": True,
        "carrier_context_is_not_source_replacement": True,
        "carrier_context_is_not_winner_loser_selection": True,
        "carrier_context_is_not_hierarchy": True,
        "carrier_context_is_not_operation_admission": True,
        "carrier_context_is_not_operation_authorization": True,
        "carrier_context_is_not_execution": True,
        "carrier_context_is_not_synchronization": True,
        "carrier_context_is_not_full_body_transfer": True,
        "carrier_context_is_not_continuation": True,
        "carrier_context_is_not_consequence": True,
    }


def _build_carrier_role_shapes_section(request: Mapping[str, Any]) -> dict[str, Any]:
    selected_shapes = _selected_role_shapes(request)
    unsupported = _unsupported_role_shapes(selected_shapes)
    all_supported = bool(selected_shapes) and not unsupported
    return {
        "selected_carrier_role_shapes": selected_shapes,
        "supported_carrier_role_shapes": sorted(SUPPORTED_CARRIER_ROLE_SHAPES),
        "unsupported_carrier_role_shapes": unsupported,
        "all_selected_shapes_supported": all_supported,
        "role_shapes_are_context_only": True,
        "role_shapes_are_not_active_operational_roles": True,
        "role_shapes_do_not_create_authority": True,
        "role_shapes_do_not_create_permission": True,
        "role_shapes_do_not_select_current_carrier": True,
        "role_shapes_do_not_select_winning_carrier": True,
        "role_shapes_do_not_invalidate_losing_carrier": True,
        "role_shapes_do_not_make_any_carrier_source": True,
        "future_operational_role_requires_admission": (
            "FUTURE_OPERATIONAL_ROLE_REQUIRES_ADMISSION" in selected_shapes
        ),
        "future_operational_role_requires_later_admission_transition_boundary": True,
        "role_activation_is_impossible_here": True,
    }


def _build_checks(
    request: Mapping[str, Any],
    selected_authority_result: Mapping[str, Any] | None,
    selected_authority_load_code: str | None,
) -> list[dict[str, Any]]:
    authority = selected_authority_result or {}
    authority_statement = _as_mapping(authority.get("authority_statement"))
    authority_non_claims = _as_mapping(authority.get("non_claims"))
    role_basis = _basis_mapping(request)
    source_authority_basis = _source_authority_basis_mapping(request, authority)
    selected_authority_outcome = _extract_source_body_authority_outcome(authority)
    failed_check_count = _extract_failed_check_count(authority)
    selected_eligibility = _selected_eligibility_result(request, authority)
    selected_matter_declaration = _selected_matter_declaration(request, authority)
    selected_operation_candidate = _selected_operation_candidate(request, authority)
    selected_operation_matter = _selected_operation_matter(request, authority)
    selected_carrier_context = _selected_carrier_context(
        request, role_basis, source_authority_basis
    )
    carrier_context_not_required = _carrier_context_explicitly_not_required(
        request, role_basis
    )
    carrier_context_parseable = _carrier_context_parseable(
        selected_carrier_context, carrier_context_not_required
    )
    role_shapes = _selected_role_shapes(request)
    unsupported_shapes = _unsupported_role_shapes(role_shapes)

    collapse_containers = (
        request,
        role_basis,
        request.get("carrier_role_shapes"),
        request.get("declared_non_claims"),
        authority_statement,
        authority_non_claims,
    )

    checks: list[dict[str, Any]] = []
    checks.append(
        _make_check(
            "role question declared",
            _is_non_empty(request.get("role_question")),
            "role question present",
            request.get("role_question"),
            BLOCK_ROLE_QUESTION_UNDECLARED,
        )
    )
    checks.append(
        _make_check(
            "role intent supported",
            request.get("role_intent") in SUPPORTED_ROLE_INTENTS,
            f"one of {sorted(SUPPORTED_ROLE_INTENTS)}",
            request.get("role_intent"),
            BLOCK_ROLE_INTENT_UNSUPPORTED,
        )
    )
    checks.append(
        _make_check(
            "selected source-body authority result present",
            selected_authority_result is not None and selected_authority_load_code is None,
            "selected source-body authority result mapping",
            selected_authority_load_code
            or ("present" if selected_authority_result is not None else "missing"),
            selected_authority_load_code or BLOCK_SOURCE_BODY_AUTHORITY_RESULT_MISSING,
        )
    )
    checks.append(
        _make_check(
            "selected source-body authority result outcome declared",
            _is_non_empty(selected_authority_outcome),
            "selected source-body authority outcome present",
            selected_authority_outcome,
            BLOCK_SOURCE_BODY_AUTHORITY_RESULT_OUTCOME_MISSING,
        )
    )
    checks.append(
        _make_check(
            "selected source-body authority result outcome recorded",
            selected_authority_outcome == EXPECTED_AUTHORITY_OUTCOME,
            EXPECTED_AUTHORITY_OUTCOME,
            selected_authority_outcome,
            BLOCK_SOURCE_BODY_AUTHORITY_RESULT_NOT_RECORDED,
        )
    )
    checks.append(
        _make_check(
            "selected source-body authority result failed check count zero",
            failed_check_count == EXPECTED_FAILED_CHECK_COUNT,
            "failed check count 0",
            failed_check_count,
            BLOCK_SOURCE_BODY_AUTHORITY_RESULT_HAS_FAILED_CHECKS,
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
            "source-body authority basis remains basis only",
            _is_non_empty(source_authority_basis),
            "source-body authority basis present and basis only",
            "present" if _is_non_empty(source_authority_basis) else "missing",
            BLOCK_SOURCE_BODY_AUTHORITY_BASIS_MISSING,
        )
    )

    authority_false_checks = (
        (
            "source-body authority result did not grant authority",
            ("authority_granted",),
            BLOCK_ROLE_REVIEW_CREATES_CARRIER_AUTHORITY,
        ),
        (
            "source-body authority result did not create authority",
            ("authority_created",),
            BLOCK_ROLE_REVIEW_CREATES_CARRIER_AUTHORITY,
        ),
        (
            "source-body authority result did not create permission",
            ("permission_created",),
            BLOCK_ROLE_REVIEW_CREATES_PERMISSION,
        ),
        (
            "source-body authority result did not define carrier roles",
            ("carrier_roles_defined",),
            BLOCK_ROLE_REVIEW_ACTIVATES_CARRIER_ROLE,
        ),
        (
            "source-body authority result did not admit operation",
            ("operation_admitted",),
            BLOCK_ROLE_REVIEW_ADMITS_OPERATION,
        ),
        (
            "source-body authority result did not authorize operation",
            ("operation_authorized", "distributed_operation_authorized"),
            BLOCK_ROLE_REVIEW_AUTHORIZES_OPERATION,
        ),
        (
            "source-body authority result did not execute operation",
            ("operation_executed",),
            BLOCK_ROLE_REVIEW_EXECUTES_OPERATION,
        ),
    )
    for check_name, fields, block_code in authority_false_checks:
        tripped = _field_tripped((authority_statement, authority_non_claims), fields)
        checks.append(
            _make_check(
                check_name,
                tripped is None,
                "false in selected authority result statement/non-claims",
                tripped or "false",
                block_code,
            )
        )

    checks.append(
        _make_check(
            "selected carrier context present or explicitly not required",
            _is_non_empty(selected_carrier_context) or carrier_context_not_required,
            "selected carrier context present or explicitly not required",
            "present"
            if _is_non_empty(selected_carrier_context)
            else ("not required" if carrier_context_not_required else "missing"),
            BLOCK_SELECTED_CARRIER_CONTEXT_MALFORMED,
        )
    )
    checks.append(
        _make_check(
            "selected carrier context parseable",
            carrier_context_parseable,
            "carrier context mapping or sequence of mappings",
            "parseable" if carrier_context_parseable else type(selected_carrier_context).__name__,
            BLOCK_SELECTED_CARRIER_CONTEXT_MALFORMED,
        )
    )
    checks.append(
        _make_check(
            "all selected carrier role shapes supported",
            bool(role_shapes) and not unsupported_shapes,
            f"subset of {sorted(SUPPORTED_CARRIER_ROLE_SHAPES)}",
            unsupported_shapes or role_shapes or "missing",
            BLOCK_UNSUPPORTED_CARRIER_ROLE_SHAPE,
        )
    )

    role_context_checks = (
        (
            "Carrier B success does not become winner role",
            BLOCK_ROLE_REVIEW_SELECTS_WINNING_CARRIER,
            ("carrier_b_success_becomes_winner", "carrier_b_success_implies_winner_role"),
        ),
        (
            "Carrier C block does not become loser role",
            BLOCK_ROLE_REVIEW_INVALIDATES_LOSING_CARRIER,
            ("carrier_c_block_becomes_loser", "carrier_c_block_implies_loser_invalidation"),
        ),
        (
            "B/C divergence remains visible",
            BLOCK_ROLE_REVIEW_RESOLVES_DIVERGENCE,
            ("divergence_resolved", "b_c_divergence_hidden"),
        ),
        (
            "refusal and blocked attempts remain visible",
            BLOCK_ROLE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL,
            ("refusal_erased", "blocked_attempt_erased", "refusal_hidden", "blocked_attempt_hidden"),
        ),
        (
            "projection mismatch remains visible where supplied",
            BLOCK_ROLE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL,
            ("projection_mismatch_hidden",),
        ),
        (
            "no carrier becomes authority",
            BLOCK_ROLE_REVIEW_CREATES_CARRIER_AUTHORITY,
            ("carrier_becomes_authority", "carrier_authority_created", "authority_created"),
        ),
        (
            "no carrier becomes source",
            BLOCK_ROLE_REVIEW_REPLACES_SOURCE,
            ("carrier_becomes_source", "source_replaced", "source_replaced_by_carrier"),
        ),
        (
            "no carrier becomes current",
            BLOCK_ROLE_REVIEW_SELECTS_CURRENT_CARRIER,
            ("carrier_becomes_current", "current_carrier_selected"),
        ),
        (
            "no carrier hierarchy created",
            BLOCK_ROLE_REVIEW_CREATES_CARRIER_HIERARCHY,
            ("carrier_hierarchy_created", "carrier_hierarchy_defined", "carrier_rank_created"),
        ),
        (
            "no operation admitted",
            BLOCK_ROLE_REVIEW_ADMITS_OPERATION,
            ("operation_admitted",),
        ),
        (
            "no operation authorized",
            BLOCK_ROLE_REVIEW_AUTHORIZES_OPERATION,
            ("operation_authorized", "distributed_operation_authorized"),
        ),
        (
            "no operation executed",
            BLOCK_ROLE_REVIEW_EXECUTES_OPERATION,
            ("operation_executed",),
        ),
        (
            "no repository synchronization authorized",
            BLOCK_ROLE_REVIEW_AUTHORIZES_REPOSITORY_SYNC,
            ("repository_synchronization_authorized", "repository_sync_authorized"),
        ),
        (
            "no full body transfer authorized",
            BLOCK_ROLE_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER,
            ("full_body_transfer_authorized",),
        ),
        (
            "no second body created",
            BLOCK_ROLE_REVIEW_CREATES_SECOND_BODY,
            ("second_body_created",),
        ),
        (
            "no continuation authorized",
            BLOCK_ROLE_REVIEW_AUTHORIZES_CONTINUATION,
            ("continuation_authorized",),
        ),
        (
            "no distributed operation authorized",
            BLOCK_ROLE_REVIEW_AUTHORIZES_OPERATION,
            ("distributed_operation_authorized",),
        ),
        (
            "no consequence created",
            BLOCK_ROLE_REVIEW_CREATES_CONSEQUENCE,
            ("consequence_created",),
        ),
        (
            "no public readiness/final completion/follow-on work",
            BLOCK_ROLE_REVIEW_CREATES_PUBLIC_READINESS,
            (
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
    for check_name, block_code, fields in role_context_checks:
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
            and _source_authority_non_claims_are_false(authority),
            "required role non-claims are explicit and false",
            "preserved" if _declared_non_claims_are_false(request) else "missing or flipped",
            BLOCK_NON_CLAIM_MISSING_OR_FLIPPED,
        )
    )
    return checks


def _build_role_non_meaning() -> dict[str, bool]:
    keys = (
        "carrier_role_activated",
        "carrier_role_assigned_for_live_operation",
        "carrier_role_assigned_for_operation",
        "carrier_authority_created",
        "carrier_currentness_created",
        "current_carrier_selected",
        "winning_carrier_selected",
        "losing_carrier_invalidated",
        "carrier_hierarchy_created",
        "source_replaced_by_carrier",
        "source_replaced",
        "authority_created",
        "permission_created",
        "operation_admitted",
        "operation_authorized",
        "operation_executed",
        "synchronization_authorized",
        "repository_synchronization_authorized",
        "full_body_transfer_authorized",
        "second_body_created",
        "continuation_authorized",
        "distributed_operation_authorized",
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
        "self_orientation_successor_scheduled",
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
            "additional carrier role basis required" if requires else None,
        ),
        "selected_carrier_context_too_generic": bool(
            context_mapping.get("selected_carrier_context_too_generic", False)
        ),
        "selected_carrier_evidence_identities_insufficiently_specific": bool(
            context_mapping.get(
                "selected_carrier_evidence_identities_insufficiently_specific", False
            )
        ),
        "role_shapes_incomplete": bool(context_mapping.get("role_shapes_incomplete", False)),
        "carrier_b_success_and_carrier_c_block_need_clearer_classification": bool(
            context_mapping.get(
                "carrier_b_success_and_carrier_c_block_need_clearer_classification",
                False,
            )
        ),
        "divergence_context_needs_stronger_role_preservation": bool(
            context_mapping.get(
                "divergence_context_needs_stronger_role_preservation", False
            )
        ),
        "refusal_block_context_needs_stronger_role_preservation": bool(
            context_mapping.get(
                "refusal_block_context_needs_stronger_role_preservation", False
            )
        ),
        "projection_mismatch_context_needs_stronger_role_preservation": bool(
            context_mapping.get(
                "projection_mismatch_context_needs_stronger_role_preservation", False
            )
        ),
        "admission_transition_boundary_cannot_yet_inspect_role_activation_safely": bool(
            context_mapping.get(
                "admission_transition_boundary_cannot_yet_inspect_role_activation_safely",
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


def _build_role_statement(
    outcome: str,
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    passed_names = {check.get("check_name") for check in checks if check.get("passed") is True}
    statement = {
        "distributed_carrier_operational_role_basis_recorded": outcome == OUTCOME_RECORDED,
        "role_basis_not_sufficient": outcome == OUTCOME_NOT_SUFFICIENT,
        "distributed_carrier_operational_role_requires_additional_basis": (
            outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        ),
        "selected_source_body_authority_result_preserved": (
            "selected source-body authority result present" in passed_names
        ),
        "selected_source_body_authority_result_recorded": (
            "selected source-body authority result outcome recorded" in passed_names
        ),
        "selected_source_body_authority_result_failed_check_count_zero": (
            "selected source-body authority result failed check count zero" in passed_names
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
        "source_body_authority_basis_preserved": (
            "source-body authority basis remains basis only" in passed_names
        ),
        "carrier_role_shapes_preserved": (
            "all selected carrier role shapes supported" in passed_names
        ),
        "carrier_context_preserved": (
            "selected carrier context present or explicitly not required" in passed_names
        ),
        "carrier_role_shapes_supported": (
            "all selected carrier role shapes supported" in passed_names
        ),
        "carrier_roles_activated": False,
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
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
        "consequence_created": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "future_admission_transition_may_later_review_role_activation": (
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
        return OUTCOME_BLOCKED, preliminary_block_code, request.get("block_reason") or preliminary_block_code
    if request.get("role_intent") == INTENT_BLOCK:
        return (
            OUTCOME_BLOCKED,
            BLOCK_ROLE_REVIEW_REQUEST_EXPLICITLY_BLOCKED,
            request.get("block_reason") or "role review explicitly blocked",
        )
    failed_code = _first_failed_code(checks)
    if failed_code:
        collapse_code = _first_collapse_code(
            request,
            _basis_mapping(request),
            request.get("carrier_role_shapes"),
            request.get("declared_non_claims"),
        )
        code = collapse_code or failed_code
        return OUTCOME_BLOCKED, code, request.get("block_reason") or code

    requested_outcome = request.get("requested_role_outcome")
    if request.get("role_intent") == INTENT_DO_NOT_RECORD:
        return (
            OUTCOME_NOT_SUFFICIENT,
            None,
            request.get("not_sufficient_reason") or "carrier role basis not recorded",
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
    if requested_outcome and requested_outcome not in SUPPORTED_ROLE_OUTCOMES:
        return OUTCOME_BLOCKED, BLOCK_ROLE_INTENT_UNSUPPORTED, _stringify(requested_outcome)
    return OUTCOME_RECORDED, None, None


def build_distributed_carrier_operational_role_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    statement = _as_mapping(result.get("role_statement"))
    declared_question = _as_mapping(result.get("declared_role_question"))
    selected_authority = _as_mapping(result.get("selected_source_body_authority_result"))
    selected_matter = _as_mapping(result.get("selected_operation_matter"))
    role_shapes = _as_mapping(result.get("carrier_role_shapes"))
    checks = result.get("role_checks")
    check_list = [check for check in checks if isinstance(check, Mapping)] if isinstance(checks, Sequence) else []
    non_claims = _as_mapping(result.get("non_claims"))
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": _get_path_value(result, ("block", "block_code")),
        "block_reason": _get_path_value(result, ("block", "block_reason")),
        "role_request_id": declared_question.get("role_request_id"),
        "role_question": declared_question.get("role_question"),
        "role_intent": declared_question.get("role_intent"),
        "selected_source_body_authority_result_id": selected_authority.get(
            "selected_source_body_authority_result_id"
        )
        or declared_question.get("selected_source_body_authority_result_id"),
        "selected_source_body_authority_result_outcome": selected_authority.get(
            "selected_source_body_authority_result_outcome"
        )
        or declared_question.get("selected_source_body_authority_result_outcome"),
        "selected_operation_candidate_id": selected_matter.get(
            "selected_operation_candidate_id"
        ),
        "selected_operation_matter_id": selected_matter.get(
            "selected_operation_matter_id"
        ),
        "passed_check_count": _passed_check_count(check_list),
        "failed_check_count": _failed_check_count(check_list),
        "distributed_carrier_operational_role_basis_recorded": statement.get(
            "distributed_carrier_operational_role_basis_recorded", False
        ),
        "role_basis_not_sufficient": statement.get("role_basis_not_sufficient", False),
        "requires_additional_basis": statement.get(
            "distributed_carrier_operational_role_requires_additional_basis", False
        ),
        "selected_source_body_authority_result_preserved": statement.get(
            "selected_source_body_authority_result_preserved", False
        ),
        "selected_source_body_authority_result_recorded": statement.get(
            "selected_source_body_authority_result_recorded", False
        ),
        "selected_source_body_authority_result_failed_check_count_zero": statement.get(
            "selected_source_body_authority_result_failed_check_count_zero", False
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
        "source_body_authority_basis_preserved": statement.get(
            "source_body_authority_basis_preserved", False
        ),
        "carrier_role_shapes_preserved": statement.get(
            "carrier_role_shapes_preserved", False
        ),
        "carrier_context_preserved": statement.get("carrier_context_preserved", False),
        "carrier_role_shapes_supported": statement.get(
            "carrier_role_shapes_supported", False
        ),
        "selected_carrier_role_shapes": role_shapes.get("selected_carrier_role_shapes", []),
        "carrier_roles_activated": False,
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
        "no_sync_full_body_transfer_second_body": not any(
            (
                statement.get("repository_synchronization_authorized", False),
                statement.get("full_body_transfer_authorized", False),
                statement.get("second_body_created", False),
            )
        ),
        "no_continuation_distributed_operation": not any(
            (
                statement.get("continuation_authorized", False),
                statement.get("distributed_operation_authorized", False),
            )
        ),
        "no_consequence_public_readiness_final_completion_follow_on_work": not any(
            (
                statement.get("consequence_created", False),
                statement.get("public_launch_readiness_created", False),
                statement.get("final_completion_claimed", False),
                statement.get("follow_on_work_authorized", False),
            )
        ),
        "future_admission_transition_may_later_review_role_activation": statement.get(
            "future_admission_transition_may_later_review_role_activation", False
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "carrier_role_activated",
                "carrier_role_assigned_for_operation",
                "carrier_authority_created",
                "carrier_currentness_created",
                "current_carrier_selected",
                "winning_carrier_selected",
                "losing_carrier_invalidated",
                "carrier_hierarchy_created",
                "operation_admitted",
                "operation_authorized",
                "operation_executed",
                "repository_synchronization_authorized",
                "full_body_transfer_authorized",
                "second_body_created",
                "continuation_authorized",
                "distributed_operation_authorized",
                "consequence_created",
                "public_launch_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
            )
        },
    }


def resolve_distributed_carrier_operational_role_boundary(
    declared_role_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_role_request is None:
        request: dict[str, Any] = {}
        preliminary_block_code = BLOCK_ROLE_QUESTION_UNDECLARED
        request_path = None
    elif not isinstance(declared_role_request, Mapping):
        request = {}
        preliminary_block_code = BLOCK_DECLARED_ROLE_REQUEST_MALFORMED
        request_path = None
    else:
        request = _copy(declared_role_request)
        preliminary_block_code = None
        request_path = request.get("role_request_path")

    selected_authority_result, selected_authority_load_code, selected_authority_path = (
        _load_selected_source_body_authority_result(request)
    )
    selected_authority_id = _first_present(
        request.get("selected_source_body_authority_result_id"),
        _extract_source_body_authority_result_id(selected_authority_result or {}),
    )
    selected_authority_outcome = _first_present(
        request.get("selected_source_body_authority_result_outcome"),
        request.get("expected_selected_authority_outcome"),
        _extract_source_body_authority_outcome(selected_authority_result or {}),
    )
    failed_check_count = _extract_failed_check_count(selected_authority_result or {})
    checks = _build_checks(request, selected_authority_result, selected_authority_load_code)
    outcome, block_code, block_reason = _decide_outcome(
        request, checks, preliminary_block_code
    )
    role_request_id = request.get("role_request_id")
    result_id = _result_id(role_request_id, selected_authority_id)
    metadata = {
        "distributed_carrier_operational_role_result_id": result_id,
        "distributed_carrier_operational_role_result_type": RESULT_TYPE,
        "distributed_carrier_operational_role_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }
    result: dict[str, Any] = {
        "distributed_carrier_operational_role_metadata": metadata,
        "declared_role_question": _build_declared_role_question(
            request,
            _stringify(selected_authority_id) if selected_authority_id else None,
            _stringify(selected_authority_outcome) if selected_authority_outcome else None,
            _stringify(request_path) if request_path else None,
        ),
        "selected_source_body_authority_result": (
            _build_selected_source_body_authority_section(
                selected_authority_result,
                selected_authority_path,
                _stringify(selected_authority_id) if selected_authority_id else None,
                _stringify(selected_authority_outcome) if selected_authority_outcome else None,
                failed_check_count,
            )
        ),
        "selected_operation_matter": _build_selected_operation_matter_section(
            request, selected_authority_result
        ),
        "carrier_role_basis": _build_carrier_role_basis_section(
            request, selected_authority_result
        ),
        "carrier_role_shapes": _build_carrier_role_shapes_section(request),
        "role_checks": checks,
        "role_statement": _build_role_statement(
            outcome, request, checks, block_code, block_reason
        ),
        "role_non_meaning": _build_role_non_meaning(),
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
    result["distributed_carrier_operational_role_summary"] = (
        build_distributed_carrier_operational_role_summary(result)
    )
    return result


def resolve_distributed_carrier_operational_role_boundary_from_path(
    declared_role_request_path: Path | str,
) -> dict[str, Any]:
    request, error = _read_json_object(declared_role_request_path)
    if error:
        block_code = (
            BLOCK_DECLARED_ROLE_REQUEST_UNREADABLE
            if error == "unreadable"
            else BLOCK_DECLARED_ROLE_REQUEST_MALFORMED
        )
        request = {
            "role_request_path": _stringify(declared_role_request_path),
            "block_reason": block_code,
        }
        result = resolve_distributed_carrier_operational_role_boundary(request)
        result["outcome"] = OUTCOME_BLOCKED
        result["block"] = {
            "blocked": True,
            "block_code": block_code,
            "block_reason": block_code,
        }
        result["role_statement"]["block_code"] = block_code
        result["role_statement"]["block_reason"] = block_code
        result["distributed_carrier_operational_role_summary"] = (
            build_distributed_carrier_operational_role_summary(result)
        )
        return result
    if request is None:
        raise DistributedCarrierOperationalRoleBoundaryError(
            "request path returned neither request nor error"
        )
    request["role_request_path"] = _stringify(declared_role_request_path)
    return resolve_distributed_carrier_operational_role_boundary(request)


def write_distributed_carrier_operational_role_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    if not isinstance(result, Mapping):
        raise DistributedCarrierOperationalRoleBoundaryError("result must be a mapping")
    metadata = _as_mapping(result.get("distributed_carrier_operational_role_metadata"))
    declared = _as_mapping(result.get("declared_role_question"))
    result_id = _first_present(
        metadata.get("distributed_carrier_operational_role_result_id"),
        declared.get("role_request_id"),
        declared.get("selected_source_body_authority_result_id"),
        "distributed_carrier_operational_role_result",
    )
    filename = f"{_sanitize_filename(result_id)}.json"
    if output_path is None:
        target = DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BOUNDARY_ROOT / filename
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


def build_declared_distributed_carrier_operational_role_request(
    role_request_id: str,
    role_question: str,
    selected_source_body_authority_result: Mapping[str, Any] | str,
    carrier_role_basis: Mapping[str, Any] | str,
    carrier_role_shapes: Sequence[str] | Mapping[str, Any],
    role_intent: str = INTENT_RECORD,
    *,
    selected_source_body_authority_result_path: str | None = None,
    selected_source_body_authority_result_id: str | None = None,
    selected_source_body_authority_result_outcome: str | None = None,
    requested_role_outcome: str = OUTCOME_RECORDED,
    selected_carrier_context: Sequence[Mapping[str, Any]] | Mapping[str, Any] | None = None,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_sufficient_reason: str | None = None,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "role_request_id": role_request_id,
        "role_question": role_question,
        "role_intent": role_intent,
        "carrier_role_basis": _copy(carrier_role_basis),
        "carrier_role_shapes": _copy(carrier_role_shapes),
        "selected_source_body_authority_result_id": selected_source_body_authority_result_id,
        "selected_source_body_authority_result_outcome": (
            selected_source_body_authority_result_outcome
        ),
        "expected_selected_authority_outcome": EXPECTED_AUTHORITY_OUTCOME,
        "requested_role_outcome": requested_role_outcome,
        "selected_carrier_context": _copy(selected_carrier_context)
        if selected_carrier_context is not None
        else None,
        "additional_basis_context": _copy(additional_basis_context)
        if additional_basis_context is not None
        else None,
        "not_sufficient_reason": not_sufficient_reason,
        "declared_non_claims": _copy(REQUIRED_NON_CLAIMS),
    }
    if selected_source_body_authority_result_path is not None:
        request["selected_source_body_authority_result_path"] = (
            selected_source_body_authority_result_path
        )
        if isinstance(selected_source_body_authority_result, Mapping):
            request["selected_source_body_authority_result"] = _copy(
                selected_source_body_authority_result
            )
    elif isinstance(selected_source_body_authority_result, Mapping):
        request["selected_source_body_authority_result"] = _copy(
            selected_source_body_authority_result
        )
    else:
        request["selected_source_body_authority_result_path"] = _stringify(
            selected_source_body_authority_result
        )

    if isinstance(carrier_role_basis, Mapping):
        request.setdefault(
            "source_body_authority_basis",
            carrier_role_basis.get("source_body_authority_basis"),
        )
        request.setdefault(
            "source_body_lineage_basis",
            carrier_role_basis.get("source_body_lineage_basis"),
        )
        request.setdefault(
            "distributed_standing_basis",
            carrier_role_basis.get("distributed_standing_basis"),
        )
        if selected_carrier_context is None:
            request["selected_carrier_context"] = carrier_role_basis.get(
                "selected_carrier_context"
            )
    return request
