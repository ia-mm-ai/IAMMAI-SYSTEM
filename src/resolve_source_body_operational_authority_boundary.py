"""Resolve source-body operational authority basis for one eligible matter.

This module records whether an eligible distributed operation matter has
sufficient source-body authority basis for future admission / transition review.
It does not grant authority, create permission, admit operation, authorize
operation, execute operation, define carrier roles, synchronize repositories,
transfer a body, create a second body, authorize continuation, create
consequence, create public readiness, claim final completion, or schedule
follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class SourceBodyOperationalAuthorityBoundaryError(Exception):
    """Raised for impossible source-body authority boundary failures."""


RESOLVER_MODULE = "resolve_source_body_operational_authority_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "source_body_operational_authority_boundary_result"
REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_BODY_OPERATIONAL_AUTHORITY_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_source_body_operational_authority_boundary"
)

INTENT_RECORD = "RECORD_SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS"
INTENT_BLOCK = "BLOCK_SOURCE_BODY_OPERATIONAL_AUTHORITY_REVIEW"
SUPPORTED_AUTHORITY_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

OUTCOME_RECORDED = "SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS_RECORDED"
OUTCOME_NOT_SUFFICIENT = "SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS_NOT_SUFFICIENT"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_OPERATIONAL_AUTHORITY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "SOURCE_BODY_OPERATIONAL_AUTHORITY_REVIEW_BLOCKED"
SUPPORTED_AUTHORITY_OUTCOMES = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_SUFFICIENT,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

EXPECTED_ELIGIBILITY_OUTCOME = "DISTRIBUTED_OPERATION_MATTER_ELIGIBLE_FOR_REVIEW"

BLOCK_AUTHORITY_QUESTION_UNDECLARED = "AUTHORITY_QUESTION_UNDECLARED"
BLOCK_AUTHORITY_INTENT_UNSUPPORTED = "AUTHORITY_INTENT_UNSUPPORTED"
BLOCK_SELECTED_ELIGIBILITY_RESULT_MISSING = "SELECTED_ELIGIBILITY_RESULT_MISSING"
BLOCK_SELECTED_ELIGIBILITY_RESULT_UNREADABLE = "SELECTED_ELIGIBILITY_RESULT_UNREADABLE"
BLOCK_SELECTED_ELIGIBILITY_RESULT_MALFORMED = "SELECTED_ELIGIBILITY_RESULT_MALFORMED"
BLOCK_SELECTED_ELIGIBILITY_RESULT_OUTCOME_MISSING = (
    "SELECTED_ELIGIBILITY_RESULT_OUTCOME_MISSING"
)
BLOCK_SELECTED_ELIGIBILITY_RESULT_NOT_ELIGIBLE = (
    "SELECTED_ELIGIBILITY_RESULT_NOT_ELIGIBLE"
)
BLOCK_SELECTED_ELIGIBILITY_RESULT_HAS_FAILED_CHECKS = (
    "SELECTED_ELIGIBILITY_RESULT_HAS_FAILED_CHECKS"
)
BLOCK_SELECTED_MATTER_DECLARATION_MISSING = "SELECTED_MATTER_DECLARATION_MISSING"
BLOCK_SELECTED_OPERATION_CANDIDATE_MISSING = "SELECTED_OPERATION_CANDIDATE_MISSING"
BLOCK_SELECTED_OPERATION_MATTER_MISSING = "SELECTED_OPERATION_MATTER_MISSING"
BLOCK_SOURCE_BODY_LINEAGE_BASIS_MISSING = "SOURCE_BODY_LINEAGE_BASIS_MISSING"
BLOCK_SOURCE_BODY_AUTHORITY_REFERENCE_MISSING = (
    "SOURCE_BODY_AUTHORITY_REFERENCE_MISSING"
)
BLOCK_CURRENT_BODY_CONFORMANCE_V4_CLOSURE_BASIS_MISSING = (
    "CURRENT_BODY_CONFORMANCE_V4_CLOSURE_BASIS_MISSING"
)
BLOCK_CURRENT_SELF_ORIENTATION_V9_BASIS_MISSING = (
    "CURRENT_SELF_ORIENTATION_V9_BASIS_MISSING"
)
BLOCK_REFUSAL_ABORT_AWARENESS_MISSING = "REFUSAL_ABORT_AWARENESS_MISSING"
BLOCK_AUTHORITY_REVIEW_GRANTS_AUTHORITY = "AUTHORITY_REVIEW_GRANTS_AUTHORITY"
BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY = "AUTHORITY_REVIEW_CREATES_AUTHORITY"
BLOCK_AUTHORITY_REVIEW_CREATES_PERMISSION = "AUTHORITY_REVIEW_CREATES_PERMISSION"
BLOCK_AUTHORITY_REVIEW_ADMITS_OPERATION = "AUTHORITY_REVIEW_ADMITS_OPERATION"
BLOCK_AUTHORITY_REVIEW_AUTHORIZES_OPERATION = "AUTHORITY_REVIEW_AUTHORIZES_OPERATION"
BLOCK_AUTHORITY_REVIEW_EXECUTES_OPERATION = "AUTHORITY_REVIEW_EXECUTES_OPERATION"
BLOCK_AUTHORITY_REVIEW_DEFINES_CARRIER_ROLES = (
    "AUTHORITY_REVIEW_DEFINES_CARRIER_ROLES"
)
BLOCK_AUTHORITY_REVIEW_AUTHORIZES_REPOSITORY_SYNC = (
    "AUTHORITY_REVIEW_AUTHORIZES_REPOSITORY_SYNC"
)
BLOCK_AUTHORITY_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER = (
    "AUTHORITY_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER"
)
BLOCK_AUTHORITY_REVIEW_CREATES_SECOND_BODY = "AUTHORITY_REVIEW_CREATES_SECOND_BODY"
BLOCK_AUTHORITY_REVIEW_AUTHORIZES_CONTINUATION = (
    "AUTHORITY_REVIEW_AUTHORIZES_CONTINUATION"
)
BLOCK_AUTHORITY_REVIEW_CREATES_CARRIER_CURRENTNESS = (
    "AUTHORITY_REVIEW_CREATES_CARRIER_CURRENTNESS"
)
BLOCK_AUTHORITY_REVIEW_SELECTS_CURRENT_CARRIER = (
    "AUTHORITY_REVIEW_SELECTS_CURRENT_CARRIER"
)
BLOCK_AUTHORITY_REVIEW_SELECTS_WINNING_CARRIER = (
    "AUTHORITY_REVIEW_SELECTS_WINNING_CARRIER"
)
BLOCK_AUTHORITY_REVIEW_INVALIDATES_LOSING_CARRIER = (
    "AUTHORITY_REVIEW_INVALIDATES_LOSING_CARRIER"
)
BLOCK_AUTHORITY_REVIEW_REPLACES_SOURCE = "AUTHORITY_REVIEW_REPLACES_SOURCE"
BLOCK_AUTHORITY_REVIEW_CREATES_TRUTH_OR_ACTION = (
    "AUTHORITY_REVIEW_CREATES_TRUTH_OR_ACTION"
)
BLOCK_AUTHORITY_REVIEW_CREATES_CONSEQUENCE = "AUTHORITY_REVIEW_CREATES_CONSEQUENCE"
BLOCK_AUTHORITY_REVIEW_RESOLVES_DIVERGENCE = "AUTHORITY_REVIEW_RESOLVES_DIVERGENCE"
BLOCK_AUTHORITY_REVIEW_ERASES_EVIDENCE_OR_REFUSAL = (
    "AUTHORITY_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"
)
BLOCK_AUTHORITY_REVIEW_CREATES_PUBLIC_READINESS = (
    "AUTHORITY_REVIEW_CREATES_PUBLIC_READINESS"
)
BLOCK_AUTHORITY_REVIEW_CLAIMS_FINAL_COMPLETION = (
    "AUTHORITY_REVIEW_CLAIMS_FINAL_COMPLETION"
)
BLOCK_AUTHORITY_REVIEW_SCHEDULES_FOLLOW_ON_WORK = (
    "AUTHORITY_REVIEW_SCHEDULES_FOLLOW_ON_WORK"
)
BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED = "MUTATION_REPLAY_OR_MERGE_DETECTED"
BLOCK_NON_CLAIM_MISSING_OR_FLIPPED = "NON_CLAIM_MISSING_OR_FLIPPED"
BLOCK_DECLARED_AUTHORITY_REQUEST_UNREADABLE = "DECLARED_AUTHORITY_REQUEST_UNREADABLE"
BLOCK_DECLARED_AUTHORITY_REQUEST_MALFORMED = "DECLARED_AUTHORITY_REQUEST_MALFORMED"
BLOCK_AUTHORITY_REQUEST_EXPLICITLY_BLOCKED = "AUTHORITY_REQUEST_EXPLICITLY_BLOCKED"

REQUIRED_NON_CLAIMS = {
    "authority_granted": False,
    "authority_created": False,
    "permission_created": False,
    "operation_admitted": False,
    "operation_authorized": False,
    "operation_executed": False,
    "carrier_roles_defined": False,
    "repository_synchronization_authorized": False,
    "full_body_transfer_authorized": False,
    "second_body_created": False,
    "continuation_authorized": False,
    "distributed_operation_authorized": False,
    "carrier_currentness_created": False,
    "current_carrier_selected": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "source_replaced": False,
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

AUTHORITY_COLLAPSE_FIELDS = (
    ("authority_granted", BLOCK_AUTHORITY_REVIEW_GRANTS_AUTHORITY),
    ("authority_created", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("carrier_becomes_authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("registry_becomes_authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("lifecycle_posture_becomes_authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("currentness_successor_becomes_authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("distributed_standing_posture_becomes_authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("eligibility_result_becomes_authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("successful_receipt_count_becomes_authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("majority_authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("latest_file_authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("latest_turn_authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("current_turn_authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY),
    ("permission_created", BLOCK_AUTHORITY_REVIEW_CREATES_PERMISSION),
    ("operation_admitted", BLOCK_AUTHORITY_REVIEW_ADMITS_OPERATION),
    ("operation_authorized", BLOCK_AUTHORITY_REVIEW_AUTHORIZES_OPERATION),
    ("distributed_operation_authorized", BLOCK_AUTHORITY_REVIEW_AUTHORIZES_OPERATION),
    ("operation_executed", BLOCK_AUTHORITY_REVIEW_EXECUTES_OPERATION),
    ("carrier_roles_defined", BLOCK_AUTHORITY_REVIEW_DEFINES_CARRIER_ROLES),
    (
        "repository_synchronization_authorized",
        BLOCK_AUTHORITY_REVIEW_AUTHORIZES_REPOSITORY_SYNC,
    ),
    ("repository_sync_authorized", BLOCK_AUTHORITY_REVIEW_AUTHORIZES_REPOSITORY_SYNC),
    (
        "full_body_transfer_authorized",
        BLOCK_AUTHORITY_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER,
    ),
    ("second_body_created", BLOCK_AUTHORITY_REVIEW_CREATES_SECOND_BODY),
    ("continuation_authorized", BLOCK_AUTHORITY_REVIEW_AUTHORIZES_CONTINUATION),
    ("carrier_currentness_created", BLOCK_AUTHORITY_REVIEW_CREATES_CARRIER_CURRENTNESS),
    ("current_carrier_selected", BLOCK_AUTHORITY_REVIEW_SELECTS_CURRENT_CARRIER),
    ("winning_carrier_selected", BLOCK_AUTHORITY_REVIEW_SELECTS_WINNING_CARRIER),
    ("losing_carrier_invalidated", BLOCK_AUTHORITY_REVIEW_INVALIDATES_LOSING_CARRIER),
    ("source_replaced", BLOCK_AUTHORITY_REVIEW_REPLACES_SOURCE),
    ("source_body_authority_replaced", BLOCK_AUTHORITY_REVIEW_REPLACES_SOURCE),
    ("truth_created", BLOCK_AUTHORITY_REVIEW_CREATES_TRUTH_OR_ACTION),
    ("action_authorized", BLOCK_AUTHORITY_REVIEW_CREATES_TRUTH_OR_ACTION),
    ("consequence_created", BLOCK_AUTHORITY_REVIEW_CREATES_CONSEQUENCE),
    ("divergence_resolved", BLOCK_AUTHORITY_REVIEW_RESOLVES_DIVERGENCE),
    ("evidence_erased", BLOCK_AUTHORITY_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("refusal_erased", BLOCK_AUTHORITY_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("blocked_attempt_erased", BLOCK_AUTHORITY_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    ("projection_mismatch_hidden", BLOCK_AUTHORITY_REVIEW_ERASES_EVIDENCE_OR_REFUSAL),
    (
        "public_launch_readiness_created",
        BLOCK_AUTHORITY_REVIEW_CREATES_PUBLIC_READINESS,
    ),
    ("public_readiness_created", BLOCK_AUTHORITY_REVIEW_CREATES_PUBLIC_READINESS),
    ("final_completion_claimed", BLOCK_AUTHORITY_REVIEW_CLAIMS_FINAL_COMPLETION),
    ("final_governance_completed", BLOCK_AUTHORITY_REVIEW_CLAIMS_FINAL_COMPLETION),
    ("final_continuity_completed", BLOCK_AUTHORITY_REVIEW_CLAIMS_FINAL_COMPLETION),
    ("final_system_identity_completed", BLOCK_AUTHORITY_REVIEW_CLAIMS_FINAL_COMPLETION),
    ("follow_on_work_authorized", BLOCK_AUTHORITY_REVIEW_SCHEDULES_FOLLOW_ON_WORK),
    (
        "self_orientation_successor_scheduled",
        BLOCK_AUTHORITY_REVIEW_SCHEDULES_FOLLOW_ON_WORK,
    ),
    ("mutation_performed", BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED),
    ("replay_performed", BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED),
    ("merge_performed", BLOCK_MUTATION_REPLAY_OR_MERGE_DETECTED),
)

WHAT_REMAINS_OPEN = {
    "carrier_operational_role_boundary": True,
    "synchronization_non_synchronization_boundary": True,
    "distributed_operation_admission_transition_authority": True,
    "distributed_refusal_and_abort_law": True,
    "distributed_execution_emission_boundary": True,
    "distributed_action_consequence_boundary": True,
    "distributed_operation_receipt_exhaustion": True,
    "distributed_operation_conformance": True,
    "distributed_operation_closure": True,
    "distributed_operation_itself": True,
    "repository_synchronization": True,
    "full_body_transfer": True,
    "second_body_creation": True,
    "current_self_orientation_v10": True,
    "public_launch_readiness": True,
    "final_governance": True,
    "final_continuity_completion": True,
    "final_system_identity": True,
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
    raw = _stringify(value).strip() or "source_body_operational_authority"
    allowed = []
    for character in raw:
        if character.isalnum() or character in {"-", "_", "."}:
            allowed.append(character)
        else:
            allowed.append("_")
    sanitized = "".join(allowed).strip("._")
    return sanitized[:180] or "source_body_operational_authority"


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
    raise SourceBodyOperationalAuthorityBoundaryError(
        f"could not create unique output path for {path}"
    )


def _extract_failed_check_count(result: Mapping[str, Any]) -> int | None:
    summary_value = _get_path_value(
        result, ("source_body_operational_authority_summary", "failed_check_count")
    )
    if summary_value is None:
        summary_value = _get_path_value(
            result, ("distributed_operation_eligibility_summary", "failed_check_count")
        )
    if summary_value is None:
        summary_value = _get_path_value(result, ("eligibility_summary", "failed_check_count"))
    if summary_value is None:
        summary_value = _get_path_value(result, ("eligibility_statement", "failed_check_count"))
    if summary_value is None:
        checks = result.get("eligibility_checks") or result.get("authority_checks")
        if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray)):
            return _failed_check_count([check for check in checks if isinstance(check, Mapping)])
        return None
    try:
        return int(summary_value)
    except (TypeError, ValueError):
        return None


def _extract_eligibility_result_id(result: Mapping[str, Any]) -> str | None:
    value = _first_present(
        _get_path_value(
            result,
            (
                "distributed_operation_eligibility_metadata",
                "distributed_operation_eligibility_result_id",
            ),
        ),
        _get_path_value(
            result,
            (
                "source_body_operational_authority_summary",
                "selected_eligibility_result_id",
            ),
        ),
        _get_path_value(
            result,
            ("distributed_operation_eligibility_summary", "eligibility_request_id"),
        ),
        _get_path_value(result, ("declared_eligibility_question", "eligibility_request_id")),
        result.get("eligibility_request_id"),
        result.get("selected_eligibility_result_id"),
    )
    return _stringify(value) if value is not None else None


def _extract_eligibility_outcome(result: Mapping[str, Any]) -> str | None:
    value = _first_present(
        result.get("outcome"),
        _get_path_value(result, ("distributed_operation_eligibility_summary", "outcome")),
        _get_path_value(result, ("declared_eligibility_question", "selected_matter_declaration_outcome")),
    )
    return _stringify(value) if value is not None else None


def _basis_mapping(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("source_body_authority_basis")
    return _copy(basis) if isinstance(basis, Mapping) else {}


def _selected_eligibility_basis(selected_eligibility_result: Mapping[str, Any]) -> dict[str, Any]:
    basis = selected_eligibility_result.get("eligibility_basis")
    return _copy(basis) if isinstance(basis, Mapping) else {}


def _selected_matter_declaration(selected_eligibility_result: Mapping[str, Any]) -> Any:
    return _first_present(
        selected_eligibility_result.get("selected_matter_declaration"),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "selected_matter_declaration_result")),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "selected_matter_declaration")),
    )


def _selected_operation_candidate(
    request: Mapping[str, Any], selected_eligibility_result: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("selected_operation_candidate"),
        selected_eligibility_result.get("selected_operation_candidate"),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "selected_operation_candidate")),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "selected_operation_candidate_identity")),
        _get_path_value(selected_eligibility_result, ("selected_matter_declaration", "operation_candidate")),
    )


def _selected_operation_matter(
    request: Mapping[str, Any], selected_eligibility_result: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("selected_operation_matter"),
        selected_eligibility_result.get("selected_operation_matter"),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "selected_operation_matter")),
        _get_path_value(selected_eligibility_result, ("selected_matter_declaration", "operation_matter")),
    )


def _selected_operation_purpose(
    request: Mapping[str, Any], selected_eligibility_result: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("selected_operation_purpose"),
        request.get("operation_purpose"),
        selected_eligibility_result.get("operation_purpose"),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "selected_operation_purpose")),
        _get_path_value(selected_eligibility_result, ("distributed_operation_eligibility_summary", "operation_purpose")),
        _get_path_value(selected_eligibility_result, ("selected_matter_declaration", "operation_purpose")),
    )


def _selected_operation_question(
    request: Mapping[str, Any], selected_eligibility_result: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("selected_operation_question"),
        request.get("operation_question"),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "selected_operation_question")),
        _get_path_value(
            selected_eligibility_result,
            ("distributed_operation_eligibility_summary", "operation_question"),
        ),
        _get_path_value(selected_eligibility_result, ("selected_operation_candidate", "selected_operation_question")),
        _get_path_value(selected_eligibility_result, ("selected_operation_candidate", "declared_operation_question")),
    )


def _proposed_operation_kind(
    request: Mapping[str, Any], selected_eligibility_result: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("proposed_operation_kind"),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "selected_proposed_operation_kind")),
        _get_path_value(
            selected_eligibility_result,
            ("distributed_operation_eligibility_summary", "proposed_operation_kind"),
        ),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "proposed_operation_kind")),
    )


def _source_body_lineage_basis(
    request: Mapping[str, Any], basis: Mapping[str, Any], eligibility_basis: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("source_body_lineage_basis"),
        basis.get("source_body_lineage_basis"),
        request.get("source_body_basis"),
        basis.get("source_body_basis"),
        eligibility_basis.get("source_body_basis"),
        eligibility_basis.get("selected_source_body_basis"),
    )


def _source_body_authority_reference(
    request: Mapping[str, Any], basis: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("source_body_authority_reference"),
        basis.get("source_body_authority_reference"),
        basis.get("authority_reference"),
    )


def _current_body_conformance_v4_closure_basis(
    request: Mapping[str, Any], basis: Mapping[str, Any], eligibility_basis: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("current_body_conformance_v4_closure_basis"),
        basis.get("current_body_conformance_v4_closure_basis"),
        eligibility_basis.get("current_body_conformance_v4_closure_basis"),
    )


def _current_self_orientation_v9_basis(
    request: Mapping[str, Any], basis: Mapping[str, Any], eligibility_basis: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("current_self_orientation_v9_basis"),
        basis.get("current_self_orientation_v9_basis"),
        eligibility_basis.get("current_self_orientation_v9_basis"),
    )


def _distributed_standing_basis(
    request: Mapping[str, Any], basis: Mapping[str, Any], eligibility_basis: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("distributed_standing_basis"),
        basis.get("distributed_standing_basis"),
        eligibility_basis.get("distributed_standing_basis"),
    )


def _divergence_consequence_basis(
    request: Mapping[str, Any], basis: Mapping[str, Any], eligibility_basis: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("divergence_consequence_basis"),
        basis.get("divergence_consequence_basis"),
        eligibility_basis.get("divergence_consequence_basis"),
    )


def _refusal_abort_awareness(
    request: Mapping[str, Any],
    basis: Mapping[str, Any],
    eligibility_basis: Mapping[str, Any],
    selected_eligibility_result: Mapping[str, Any],
) -> Any:
    return _first_present(
        request.get("refusal_abort_awareness"),
        basis.get("refusal_abort_awareness"),
        eligibility_basis.get("selected_refusal_abort_awareness"),
        eligibility_basis.get("refusal_abort_awareness"),
        selected_eligibility_result.get("refusal_abort_awareness"),
        _get_path_value(selected_eligibility_result, ("selected_matter_declaration", "refusal_abort_awareness")),
    )


def _selected_carrier_context(
    request: Mapping[str, Any], basis: Mapping[str, Any], eligibility_basis: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("selected_carrier_context"),
        basis.get("selected_carrier_context"),
        eligibility_basis.get("selected_carrier_context"),
    )


def _proposed_affected_surfaces(
    request: Mapping[str, Any], selected_eligibility_result: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("proposed_affected_surfaces"),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "selected_proposed_affected_surfaces")),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "proposed_affected_surfaces")),
        selected_eligibility_result.get("proposed_affected_surfaces"),
    )


def _proposed_output_family(
    request: Mapping[str, Any], selected_eligibility_result: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("proposed_output_family"),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "selected_proposed_output_family")),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "proposed_output_family")),
        selected_eligibility_result.get("proposed_output_family"),
    )


def _eligibility_review_request(
    request: Mapping[str, Any], selected_eligibility_result: Mapping[str, Any]
) -> Any:
    return _first_present(
        request.get("eligibility_review_request"),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "selected_eligibility_review_request")),
        _get_path_value(selected_eligibility_result, ("eligibility_basis", "eligibility_review_request")),
        selected_eligibility_result.get("eligibility_review_request"),
    )


def _declared_non_claims_are_false(request: Mapping[str, Any]) -> bool:
    claims = request.get("declared_non_claims")
    if not isinstance(claims, Mapping):
        return False
    return all(claim in claims and claims[claim] is False for claim in REQUIRED_NON_CLAIMS)


def _selected_eligibility_non_claims_are_false(selected_eligibility_result: Mapping[str, Any]) -> bool:
    claims = selected_eligibility_result.get("non_claims")
    if not isinstance(claims, Mapping):
        return False
    for claim in (
        "operation_admitted",
        "operation_authorized",
        "operation_executed",
        "source_body_authority_decided",
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
        "authority_created",
        "permission_created",
        "truth_created",
        "action_authorized",
        "consequence_created",
        "evidence_erased",
        "refusal_erased",
        "public_launch_readiness_created",
        "final_completion_claimed",
        "follow_on_work_authorized",
    ):
        if claims.get(claim) is not False:
            return False
    return True


def _matter_declaration_non_claims_are_false(selected_matter_declaration: Any) -> bool:
    if not isinstance(selected_matter_declaration, Mapping):
        return False
    claims = selected_matter_declaration.get("non_claims")
    if not isinstance(claims, Mapping):
        return False
    for claim in (
        "operation_admitted",
        "operation_authorized",
        "operation_executed",
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
        "authority_created",
        "permission_created",
        "truth_created",
        "action_authorized",
        "consequence_created",
        "evidence_erased",
        "refusal_erased",
        "public_launch_readiness_created",
        "final_completion_claimed",
        "follow_on_work_authorized",
    ):
        if claims.get(claim) is not False:
            return False
    return True


def _first_collapse_code(*containers: Any) -> str | None:
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        for field, code in AUTHORITY_COLLAPSE_FIELDS:
            if _is_true(container.get(field)):
                return code
    return None


def _result_id(authority_request_id: Any, selected_eligibility_result_id: Any) -> str:
    source = _first_present(authority_request_id, selected_eligibility_result_id)
    return f"{_sanitize_filename(source)}__source_body_operational_authority_result"


def _load_selected_eligibility_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    selected_path = request.get("selected_eligibility_result_path")
    if _is_non_empty(selected_path):
        loaded, error = _read_json_object(_stringify(selected_path))
        if error == "unreadable":
            return None, BLOCK_SELECTED_ELIGIBILITY_RESULT_UNREADABLE, _stringify(selected_path)
        if error == "malformed":
            return None, BLOCK_SELECTED_ELIGIBILITY_RESULT_MALFORMED, _stringify(selected_path)
        return _copy(loaded), None, _stringify(selected_path)

    selected = request.get("selected_eligibility_result")
    if isinstance(selected, Mapping):
        return _copy(selected), None, None
    if _is_non_empty(selected):
        return None, BLOCK_SELECTED_ELIGIBILITY_RESULT_MALFORMED, None
    return None, BLOCK_SELECTED_ELIGIBILITY_RESULT_MISSING, None


def _build_declared_authority_question(
    request: Mapping[str, Any],
    selected_eligibility_result_id: str | None,
    selected_eligibility_outcome: str | None,
    request_path: str | None,
) -> dict[str, Any]:
    return {
        "authority_request_id": request.get("authority_request_id"),
        "authority_question": request.get("authority_question"),
        "authority_intent": request.get("authority_intent"),
        "authority_request_path": request_path,
        "selected_eligibility_result_id": _first_present(
            request.get("selected_eligibility_result_id"), selected_eligibility_result_id
        ),
        "selected_eligibility_result_outcome": _first_present(
            request.get("selected_eligibility_result_outcome"),
            request.get("expected_selected_eligibility_outcome"),
            selected_eligibility_outcome,
        ),
        "authority_is_not_authority_grant": True,
        "authority_is_not_permission": True,
        "authority_is_not_admission": True,
        "authority_is_not_authorization": True,
        "authority_is_not_execution": True,
        "authority_is_not_operation": True,
        "authority_is_not_synchronization": True,
        "authority_is_not_full_body_transfer": True,
        "authority_is_not_continuation": True,
        "authority_is_not_carrier_role_definition": True,
    }


def _build_selected_eligibility_section(
    selected_eligibility_result: Mapping[str, Any] | None,
    selected_eligibility_result_path: str | None,
    selected_eligibility_result_id: str | None,
    selected_eligibility_outcome: str | None,
    failed_check_count: int | None,
) -> dict[str, Any]:
    result = _copy(selected_eligibility_result) if isinstance(selected_eligibility_result, Mapping) else None
    return {
        "selected_eligibility_result": result,
        "selected_eligibility_result_path": selected_eligibility_result_path,
        "selected_eligibility_result_id": selected_eligibility_result_id,
        "selected_eligibility_result_outcome": selected_eligibility_outcome,
        "selected_eligibility_result_outcome_is_eligible": (
            selected_eligibility_outcome == EXPECTED_ELIGIBILITY_OUTCOME
        ),
        "selected_eligibility_result_failed_check_count": failed_check_count,
        "selected_eligibility_result_failed_check_count_zero": failed_check_count == 0,
        "selected_eligibility_result_remains_eligibility_only": True,
        "selected_eligibility_result_did_not_admit_operation": True,
        "selected_eligibility_result_did_not_authorize_operation": True,
        "selected_eligibility_result_did_not_execute_operation": True,
        "selected_eligibility_result_did_not_decide_source_body_authority": True,
        "selected_eligibility_result_did_not_define_carrier_roles": True,
    }


def _build_selected_operation_matter_section(
    request: Mapping[str, Any],
    selected_eligibility_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    eligibility = selected_eligibility_result or {}
    candidate = _selected_operation_candidate(request, eligibility)
    matter = _selected_operation_matter(request, eligibility)
    matter_declaration = _first_present(request.get("selected_matter_declaration"), _selected_matter_declaration(eligibility))
    operation_question = _selected_operation_question(request, eligibility)
    operation_purpose = _selected_operation_purpose(request, eligibility)
    proposed_kind = _proposed_operation_kind(request, eligibility)
    return {
        "selected_eligibility_result": _copy(eligibility) if eligibility else None,
        "selected_matter_declaration": _copy(matter_declaration),
        "selected_operation_candidate": _copy(candidate),
        "selected_operation_matter": _copy(matter),
        "selected_operation_question": _copy(operation_question),
        "selected_operation_purpose": _copy(operation_purpose),
        "proposed_operation_kind": _copy(proposed_kind),
        "selected_operation_candidate_id": _first_present(
            _get_path_value(_as_mapping(candidate), ("operation_candidate_id",)),
            _get_path_value(_as_mapping(candidate), ("selected_operation_candidate_id",)),
            _get_path_value(eligibility, ("distributed_operation_eligibility_summary", "operation_candidate_id")),
        ),
        "selected_operation_matter_id": _first_present(
            _get_path_value(_as_mapping(matter), ("operation_matter_id",)),
            _get_path_value(_as_mapping(matter), ("selected_operation_matter_id",)),
            _get_path_value(eligibility, ("distributed_operation_eligibility_summary", "operation_matter_id")),
        ),
        "matter_remains_declaration_only": True,
        "candidate_remains_candidate_only": True,
        "eligibility_remains_eligibility_only": True,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
    }


def _build_source_body_authority_basis_section(
    request: Mapping[str, Any],
    selected_eligibility_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    eligibility = selected_eligibility_result or {}
    basis = _basis_mapping(request)
    eligibility_basis = _selected_eligibility_basis(eligibility)
    lineage_basis = _source_body_lineage_basis(request, basis, eligibility_basis)
    authority_reference = _source_body_authority_reference(request, basis)
    v4_basis = _current_body_conformance_v4_closure_basis(request, basis, eligibility_basis)
    v9_basis = _current_self_orientation_v9_basis(request, basis, eligibility_basis)
    standing_basis = _distributed_standing_basis(request, basis, eligibility_basis)
    divergence_basis = _divergence_consequence_basis(request, basis, eligibility_basis)
    refusal_abort = _refusal_abort_awareness(request, basis, eligibility_basis, eligibility)
    carrier_context = _selected_carrier_context(request, basis, eligibility_basis)
    return {
        "source_body_authority_basis": _copy(request.get("source_body_authority_basis")),
        "source_body_lineage_basis": _copy(lineage_basis),
        "source_body_authority_reference": _copy(authority_reference),
        "operational_authority_origin": "source_body_lineage_reference_only"
        if _is_non_empty(lineage_basis) and _is_non_empty(authority_reference)
        else None,
        "operational_authority_origin_is_source_body_lineage_reference_only": True,
        "current_body_conformance_v4_closure_basis": _copy(v4_basis),
        "current_self_orientation_v9_basis": _copy(v9_basis),
        "distributed_standing_basis": _copy(standing_basis),
        "distributed_standing_basis_is_basis_only": True if _is_non_empty(standing_basis) else False,
        "divergence_consequence_basis": _copy(divergence_basis),
        "divergence_consequence_basis_is_caution_context_only": True
        if _is_non_empty(divergence_basis)
        else False,
        "refusal_abort_awareness": _copy(refusal_abort),
        "selected_carrier_context": _copy(carrier_context),
        "selected_carrier_context_is_context_only": True if _is_non_empty(carrier_context) else False,
        "source_body_authority_basis_is_not_authority_grant": True,
        "source_body_authority_basis_is_not_permission": True,
        "source_body_authority_basis_is_not_operation_admission": True,
        "source_body_authority_basis_is_not_operation_authorization": True,
        "source_body_authority_basis_is_not_execution": True,
        "source_body_authority_basis_is_not_carrier_authority": True,
        "source_body_authority_basis_is_not_registry_authority": True,
        "source_body_authority_basis_is_not_currentness_authority": True,
        "source_body_authority_basis_is_not_distributed_standing_authority": True,
    }


def _build_checks(
    request: Mapping[str, Any],
    selected_eligibility_result: Mapping[str, Any] | None,
    selected_eligibility_load_code: str | None,
) -> list[dict[str, Any]]:
    eligibility = selected_eligibility_result or {}
    basis = _basis_mapping(request)
    eligibility_basis = _selected_eligibility_basis(eligibility)
    selected_matter_declaration = _first_present(
        request.get("selected_matter_declaration"), _selected_matter_declaration(eligibility)
    )
    selected_operation_candidate = _selected_operation_candidate(request, eligibility)
    selected_operation_matter = _selected_operation_matter(request, eligibility)
    selected_operation_purpose = _selected_operation_purpose(request, eligibility)
    eligibility_review_request = _eligibility_review_request(request, eligibility)
    refusal_abort = _refusal_abort_awareness(request, basis, eligibility_basis, eligibility)
    selected_eligibility_outcome = _extract_eligibility_outcome(eligibility)
    failed_check_count = _extract_failed_check_count(eligibility)
    source_body_lineage = _source_body_lineage_basis(request, basis, eligibility_basis)
    authority_reference = _source_body_authority_reference(request, basis)
    v4_basis = _current_body_conformance_v4_closure_basis(request, basis, eligibility_basis)
    v9_basis = _current_self_orientation_v9_basis(request, basis, eligibility_basis)
    standing_basis = _distributed_standing_basis(request, basis, eligibility_basis)
    carrier_context = _selected_carrier_context(request, basis, eligibility_basis)
    request_claims = request.get("declared_non_claims")
    eligibility_claims = eligibility.get("non_claims") if isinstance(eligibility, Mapping) else {}
    basis_claims = basis.get("declared_non_claims") if isinstance(basis, Mapping) else {}
    eligibility_statement = eligibility.get("eligibility_statement")
    matter_statement = (
        selected_matter_declaration.get("matter_declaration_statement")
        if isinstance(selected_matter_declaration, Mapping)
        else {}
    )

    checks: list[dict[str, Any]] = []
    checks.append(
        _make_check(
            "authority question declared",
            _is_non_empty(request.get("authority_question")),
            "authority question present",
            request.get("authority_question"),
            BLOCK_AUTHORITY_QUESTION_UNDECLARED,
        )
    )
    checks.append(
        _make_check(
            "authority intent supported",
            request.get("authority_intent") in SUPPORTED_AUTHORITY_INTENTS,
            f"one of {sorted(SUPPORTED_AUTHORITY_INTENTS)}",
            request.get("authority_intent"),
            BLOCK_AUTHORITY_INTENT_UNSUPPORTED,
        )
    )
    checks.append(
        _make_check(
            "selected eligibility result present",
            selected_eligibility_result is not None and selected_eligibility_load_code is None,
            "selected eligibility result mapping",
            selected_eligibility_load_code or ("present" if selected_eligibility_result is not None else "missing"),
            selected_eligibility_load_code or BLOCK_SELECTED_ELIGIBILITY_RESULT_MISSING,
        )
    )
    checks.append(
        _make_check(
            "selected eligibility result outcome declared",
            _is_non_empty(selected_eligibility_outcome),
            "selected eligibility outcome present",
            selected_eligibility_outcome,
            BLOCK_SELECTED_ELIGIBILITY_RESULT_OUTCOME_MISSING,
        )
    )
    checks.append(
        _make_check(
            "selected eligibility result outcome eligible",
            selected_eligibility_outcome == EXPECTED_ELIGIBILITY_OUTCOME,
            EXPECTED_ELIGIBILITY_OUTCOME,
            selected_eligibility_outcome,
            BLOCK_SELECTED_ELIGIBILITY_RESULT_NOT_ELIGIBLE,
        )
    )
    checks.append(
        _make_check(
            "selected eligibility result failed check count zero",
            failed_check_count == 0,
            "failed check count 0",
            failed_check_count,
            BLOCK_SELECTED_ELIGIBILITY_RESULT_HAS_FAILED_CHECKS,
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
            "selected operation purpose preserved",
            _is_non_empty(selected_operation_purpose),
            "selected operation purpose present",
            "present" if _is_non_empty(selected_operation_purpose) else "missing",
            BLOCK_SELECTED_OPERATION_MATTER_MISSING,
        )
    )
    checks.append(
        _make_check(
            "eligibility review request preserved",
            _is_non_empty(eligibility_review_request),
            "eligibility review request present",
            "present" if _is_non_empty(eligibility_review_request) else "missing",
            BLOCK_SELECTED_ELIGIBILITY_RESULT_MALFORMED,
        )
    )
    checks.append(
        _make_check(
            "refusal/abort awareness preserved",
            _is_non_empty(refusal_abort),
            "refusal/abort awareness present",
            "present" if _is_non_empty(refusal_abort) else "missing",
            BLOCK_REFUSAL_ABORT_AWARENESS_MISSING,
        )
    )
    checks.append(
        _make_check(
            "source-body lineage basis present",
            _is_non_empty(source_body_lineage),
            "source-body lineage basis present",
            "present" if _is_non_empty(source_body_lineage) else "missing",
            BLOCK_SOURCE_BODY_LINEAGE_BASIS_MISSING,
        )
    )
    checks.append(
        _make_check(
            "source-body authority reference present",
            _is_non_empty(authority_reference),
            "source-body authority reference present",
            "present" if _is_non_empty(authority_reference) else "missing",
            BLOCK_SOURCE_BODY_AUTHORITY_REFERENCE_MISSING,
        )
    )
    checks.append(
        _make_check(
            "current-body conformance v4 closure basis present",
            _is_non_empty(v4_basis),
            "current-body conformance v4 closure basis present",
            "present" if _is_non_empty(v4_basis) else "missing",
            BLOCK_CURRENT_BODY_CONFORMANCE_V4_CLOSURE_BASIS_MISSING,
        )
    )
    checks.append(
        _make_check(
            "current self-orientation v9 basis present",
            _is_non_empty(v9_basis),
            "current self-orientation v9 basis present",
            "present" if _is_non_empty(v9_basis) else "missing",
            BLOCK_CURRENT_SELF_ORIENTATION_V9_BASIS_MISSING,
        )
    )
    checks.append(
        _make_check(
            "distributed standing basis remains basis only where supplied",
            not _is_non_empty(standing_basis)
            or not _is_true(_as_mapping(standing_basis).get("distributed_standing_becomes_authority")),
            "distributed standing basis is basis/context only",
            "basis only" if _is_non_empty(standing_basis) else "not supplied",
            BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY,
        )
    )
    checks.append(
        _make_check(
            "carrier context remains context only where supplied",
            not _is_non_empty(carrier_context)
            or not _is_true(_as_mapping(carrier_context).get("carrier_becomes_authority")),
            "carrier context is context/evidence only",
            "context only" if _is_non_empty(carrier_context) else "not supplied",
            BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY,
        )
    )

    collapse_containers = (
        request,
        basis,
        request_claims,
        basis_claims,
        eligibility_claims,
        eligibility_statement,
        matter_statement,
    )
    check_names = (
        ("no carrier becomes authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY, ("carrier_becomes_authority",)),
        ("no registry becomes authority", BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY, ("registry_becomes_authority",)),
        (
            "no lifecycle posture becomes authority",
            BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY,
            ("lifecycle_posture_becomes_authority",),
        ),
        (
            "no currentness successor becomes authority",
            BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY,
            ("currentness_successor_becomes_authority",),
        ),
        (
            "no distributed standing posture becomes authority",
            BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY,
            ("distributed_standing_posture_becomes_authority",),
        ),
        (
            "no eligibility result becomes authority",
            BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY,
            ("eligibility_result_becomes_authority",),
        ),
        (
            "no successful receipt count becomes authority",
            BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY,
            ("successful_receipt_count_becomes_authority",),
        ),
        (
            "no majority/latest-file/current-turn authority",
            BLOCK_AUTHORITY_REVIEW_CREATES_AUTHORITY,
            ("majority_authority", "latest_file_authority", "latest_turn_authority", "current_turn_authority"),
        ),
        ("no operation admitted", BLOCK_AUTHORITY_REVIEW_ADMITS_OPERATION, ("operation_admitted",)),
        ("no operation authorized", BLOCK_AUTHORITY_REVIEW_AUTHORIZES_OPERATION, ("operation_authorized", "distributed_operation_authorized")),
        ("no operation executed", BLOCK_AUTHORITY_REVIEW_EXECUTES_OPERATION, ("operation_executed",)),
        ("no carrier roles defined", BLOCK_AUTHORITY_REVIEW_DEFINES_CARRIER_ROLES, ("carrier_roles_defined",)),
        (
            "no repository synchronization authorized",
            BLOCK_AUTHORITY_REVIEW_AUTHORIZES_REPOSITORY_SYNC,
            ("repository_synchronization_authorized", "repository_sync_authorized"),
        ),
        (
            "no full body transfer authorized",
            BLOCK_AUTHORITY_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER,
            ("full_body_transfer_authorized",),
        ),
        ("no second body created", BLOCK_AUTHORITY_REVIEW_CREATES_SECOND_BODY, ("second_body_created",)),
        ("no continuation authorized", BLOCK_AUTHORITY_REVIEW_AUTHORIZES_CONTINUATION, ("continuation_authorized",)),
        (
            "no distributed operation authorized",
            BLOCK_AUTHORITY_REVIEW_AUTHORIZES_OPERATION,
            ("distributed_operation_authorized",),
        ),
        (
            "no source-body authority replaced",
            BLOCK_AUTHORITY_REVIEW_REPLACES_SOURCE,
            ("source_replaced", "source_body_authority_replaced"),
        ),
        ("no permission created", BLOCK_AUTHORITY_REVIEW_CREATES_PERMISSION, ("permission_created",)),
        (
            "no truth/action created",
            BLOCK_AUTHORITY_REVIEW_CREATES_TRUTH_OR_ACTION,
            ("truth_created", "action_authorized"),
        ),
        ("no consequence created", BLOCK_AUTHORITY_REVIEW_CREATES_CONSEQUENCE, ("consequence_created",)),
        (
            "no public readiness/final completion/follow-on work",
            BLOCK_AUTHORITY_REVIEW_CREATES_PUBLIC_READINESS,
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
    for check_name, block_code, fields in check_names:
        tripped = None
        for container in collapse_containers:
            if not isinstance(container, Mapping):
                continue
            for field in fields:
                if _is_true(container.get(field)):
                    tripped = field
                    break
            if tripped:
                break
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
            and _selected_eligibility_non_claims_are_false(eligibility)
            and _matter_declaration_non_claims_are_false(selected_matter_declaration),
            "required non-claims are explicit and false",
            "preserved" if _declared_non_claims_are_false(request) else "missing or flipped",
            BLOCK_NON_CLAIM_MISSING_OR_FLIPPED,
        )
    )
    return checks


def _build_authority_non_meaning() -> dict[str, bool]:
    keys = (
        "authority_granted",
        "authority_created",
        "permission_created",
        "operation_admitted",
        "operation_authorized",
        "operation_executed",
        "carrier_roles_defined",
        "synchronization_authorized",
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
            "additional source-body authority basis required" if requires else None,
        ),
        "source_body_authority_reference_too_generic": bool(
            context_mapping.get("source_body_authority_reference_too_generic", False)
        ),
        "source_body_lineage_basis_insufficiently_specific": bool(
            context_mapping.get("source_body_lineage_basis_insufficiently_specific", False)
        ),
        "operation_purpose_requires_stronger_source_body_authorization_surface": bool(
            context_mapping.get(
                "operation_purpose_requires_stronger_source_body_authorization_surface",
                False,
            )
        ),
        "proposed_affected_surfaces_require_additional_authority_basis": bool(
            context_mapping.get(
                "proposed_affected_surfaces_require_additional_authority_basis",
                False,
            )
        ),
        "proposed_output_family_requires_additional_authority_basis": bool(
            context_mapping.get(
                "proposed_output_family_requires_additional_authority_basis",
                False,
            )
        ),
        "carrier_context_creates_authority_ambiguity": bool(
            context_mapping.get("carrier_context_creates_authority_ambiguity", False)
        ),
        "refusal_abort_awareness_needs_authority_specific_binding": bool(
            context_mapping.get(
                "refusal_abort_awareness_needs_authority_specific_binding", False
            )
        ),
        "admission_transition_boundary_cannot_yet_inspect_authority_safely": bool(
            context_mapping.get(
                "admission_transition_boundary_cannot_yet_inspect_authority_safely",
                False,
            )
        ),
        "additional_basis_not_scheduled": True,
        "additional_basis_not_authorized": True,
        "additional_basis_not_executed": True,
    }


def _build_authority_statement(
    outcome: str,
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    passed_names = {check.get("check_name") for check in checks if check.get("passed") is True}
    statement = {
        "source_body_operational_authority_basis_recorded": outcome == OUTCOME_RECORDED,
        "authority_basis_not_sufficient": outcome == OUTCOME_NOT_SUFFICIENT,
        "source_body_operational_authority_requires_additional_basis": (
            outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        ),
        "selected_eligibility_result_preserved": "selected eligibility result present" in passed_names,
        "selected_eligibility_result_eligible": "selected eligibility result outcome eligible" in passed_names,
        "selected_eligibility_result_failed_check_count_zero": (
            "selected eligibility result failed check count zero" in passed_names
        ),
        "selected_matter_declaration_preserved": "selected matter declaration preserved" in passed_names,
        "selected_operation_candidate_preserved": "selected operation candidate preserved" in passed_names,
        "selected_operation_matter_preserved": "selected operation matter preserved" in passed_names,
        "source_body_lineage_basis_preserved": "source-body lineage basis present" in passed_names,
        "source_body_authority_reference_preserved": (
            "source-body authority reference present" in passed_names
        ),
        "current_body_conformance_v4_closure_basis_preserved": (
            "current-body conformance v4 closure basis present" in passed_names
        ),
        "current_self_orientation_v9_basis_preserved": (
            "current self-orientation v9 basis present" in passed_names
        ),
        "refusal_abort_awareness_preserved": "refusal/abort awareness preserved" in passed_names,
        "future_admission_transition_review_may_be_considered": outcome == OUTCOME_RECORDED,
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
    request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]], preliminary_block_code: str | None
) -> tuple[str, str | None, str | None]:
    if preliminary_block_code:
        return OUTCOME_BLOCKED, preliminary_block_code, request.get("block_reason") or preliminary_block_code
    if request.get("authority_intent") == INTENT_BLOCK:
        return (
            OUTCOME_BLOCKED,
            BLOCK_AUTHORITY_REQUEST_EXPLICITLY_BLOCKED,
            request.get("block_reason") or "authority review explicitly blocked",
        )
    failed_code = _first_failed_code(checks)
    if failed_code:
        collapse_code = _first_collapse_code(
            request,
            _basis_mapping(request),
            request.get("declared_non_claims"),
        )
        code = collapse_code or failed_code
        return OUTCOME_BLOCKED, code, request.get("block_reason") or code

    requested_outcome = request.get("requested_authority_outcome")
    if request.get("authority_intent") == INTENT_DO_NOT_RECORD:
        return (
            OUTCOME_NOT_SUFFICIENT,
            None,
            request.get("not_sufficient_reason") or "source-body authority basis not recorded",
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
    if requested_outcome and requested_outcome not in SUPPORTED_AUTHORITY_OUTCOMES:
        return OUTCOME_BLOCKED, BLOCK_AUTHORITY_INTENT_UNSUPPORTED, _stringify(requested_outcome)
    return OUTCOME_RECORDED, None, None


def build_source_body_operational_authority_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    statement = _as_mapping(result.get("authority_statement"))
    declared_question = _as_mapping(result.get("declared_authority_question"))
    selected_eligibility = _as_mapping(result.get("selected_eligibility_result"))
    selected_matter = _as_mapping(result.get("selected_operation_matter"))
    checks = result.get("authority_checks")
    check_list = [check for check in checks if isinstance(check, Mapping)] if isinstance(checks, Sequence) else []
    non_claims = _as_mapping(result.get("non_claims"))
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": _get_path_value(result, ("block", "block_code")),
        "block_reason": _get_path_value(result, ("block", "block_reason")),
        "authority_request_id": declared_question.get("authority_request_id"),
        "authority_question": declared_question.get("authority_question"),
        "authority_intent": declared_question.get("authority_intent"),
        "selected_eligibility_result_id": selected_eligibility.get("selected_eligibility_result_id")
        or declared_question.get("selected_eligibility_result_id"),
        "selected_eligibility_result_outcome": selected_eligibility.get(
            "selected_eligibility_result_outcome"
        )
        or declared_question.get("selected_eligibility_result_outcome"),
        "selected_operation_candidate_id": selected_matter.get("selected_operation_candidate_id"),
        "selected_operation_matter_id": selected_matter.get("selected_operation_matter_id"),
        "passed_check_count": _passed_check_count(check_list),
        "failed_check_count": _failed_check_count(check_list),
        "source_body_operational_authority_basis_recorded": statement.get(
            "source_body_operational_authority_basis_recorded", False
        ),
        "authority_basis_not_sufficient": statement.get("authority_basis_not_sufficient", False),
        "requires_additional_basis": statement.get(
            "source_body_operational_authority_requires_additional_basis", False
        ),
        "selected_eligibility_result_preserved": statement.get(
            "selected_eligibility_result_preserved", False
        ),
        "selected_eligibility_result_eligible": statement.get(
            "selected_eligibility_result_eligible", False
        ),
        "selected_eligibility_result_failed_check_count_zero": statement.get(
            "selected_eligibility_result_failed_check_count_zero", False
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
        "source_body_lineage_basis_preserved": statement.get(
            "source_body_lineage_basis_preserved", False
        ),
        "source_body_authority_reference_preserved": statement.get(
            "source_body_authority_reference_preserved", False
        ),
        "current_body_conformance_v4_closure_basis_preserved": statement.get(
            "current_body_conformance_v4_closure_basis_preserved", False
        ),
        "current_self_orientation_v9_basis_preserved": statement.get(
            "current_self_orientation_v9_basis_preserved", False
        ),
        "refusal_abort_awareness_preserved": statement.get(
            "refusal_abort_awareness_preserved", False
        ),
        "future_admission_transition_review_may_be_considered": statement.get(
            "future_admission_transition_review_may_be_considered", False
        ),
        "authority_granted": False,
        "authority_created": False,
        "permission_created": False,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "carrier_roles_defined": False,
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
        "no_source_replacement_truth_action_consequence": not any(
            (
                statement.get("source_replaced", False),
                statement.get("truth_created", False),
                statement.get("action_authorized", False),
                statement.get("consequence_created", False),
            )
        ),
        "no_public_readiness_final_completion_follow_on_work": not any(
            (
                statement.get("public_launch_readiness_created", False),
                statement.get("final_completion_claimed", False),
                statement.get("follow_on_work_authorized", False),
            )
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
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
                "consequence_created",
                "public_launch_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
            )
        },
    }


def resolve_source_body_operational_authority_boundary(
    declared_authority_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_authority_request is None:
        request: dict[str, Any] = {}
        preliminary_block_code = BLOCK_AUTHORITY_QUESTION_UNDECLARED
        request_path = None
    elif not isinstance(declared_authority_request, Mapping):
        request = {}
        preliminary_block_code = BLOCK_DECLARED_AUTHORITY_REQUEST_MALFORMED
        request_path = None
    else:
        request = _copy(declared_authority_request)
        preliminary_block_code = None
        request_path = request.get("authority_request_path")

    selected_eligibility_result, selected_eligibility_load_code, selected_eligibility_path = (
        _load_selected_eligibility_result(request)
    )
    selected_eligibility_id = _first_present(
        request.get("selected_eligibility_result_id"),
        _extract_eligibility_result_id(selected_eligibility_result or {}),
    )
    selected_eligibility_outcome = _first_present(
        request.get("selected_eligibility_result_outcome"),
        request.get("expected_selected_eligibility_outcome"),
        _extract_eligibility_outcome(selected_eligibility_result or {}),
    )
    failed_check_count = _extract_failed_check_count(selected_eligibility_result or {})
    checks = _build_checks(request, selected_eligibility_result, selected_eligibility_load_code)
    outcome, block_code, block_reason = _decide_outcome(
        request, checks, preliminary_block_code
    )
    authority_request_id = request.get("authority_request_id")
    result_id = _result_id(authority_request_id, selected_eligibility_id)
    metadata = {
        "source_body_operational_authority_result_id": result_id,
        "source_body_operational_authority_result_type": RESULT_TYPE,
        "source_body_operational_authority_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }
    result: dict[str, Any] = {
        "source_body_operational_authority_metadata": metadata,
        "declared_authority_question": _build_declared_authority_question(
            request,
            _stringify(selected_eligibility_id) if selected_eligibility_id else None,
            _stringify(selected_eligibility_outcome) if selected_eligibility_outcome else None,
            _stringify(request_path) if request_path else None,
        ),
        "selected_eligibility_result": _build_selected_eligibility_section(
            selected_eligibility_result,
            selected_eligibility_path,
            _stringify(selected_eligibility_id) if selected_eligibility_id else None,
            _stringify(selected_eligibility_outcome) if selected_eligibility_outcome else None,
            failed_check_count,
        ),
        "selected_operation_matter": _build_selected_operation_matter_section(
            request, selected_eligibility_result
        ),
        "source_body_authority_basis": _build_source_body_authority_basis_section(
            request, selected_eligibility_result
        ),
        "authority_checks": checks,
        "authority_statement": _build_authority_statement(
            outcome, request, checks, block_code, block_reason
        ),
        "authority_non_meaning": _build_authority_non_meaning(),
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
    result["source_body_operational_authority_summary"] = (
        build_source_body_operational_authority_summary(result)
    )
    return result


def resolve_source_body_operational_authority_boundary_from_path(
    declared_authority_request_path: Path | str,
) -> dict[str, Any]:
    request, error = _read_json_object(declared_authority_request_path)
    if error:
        block_code = (
            BLOCK_DECLARED_AUTHORITY_REQUEST_UNREADABLE
            if error == "unreadable"
            else BLOCK_DECLARED_AUTHORITY_REQUEST_MALFORMED
        )
        request = {
            "authority_request_path": _stringify(declared_authority_request_path),
            "block_reason": block_code,
        }
        result = resolve_source_body_operational_authority_boundary(request)
        result["outcome"] = OUTCOME_BLOCKED
        result["block"] = {
            "blocked": True,
            "block_code": block_code,
            "block_reason": block_code,
        }
        result["authority_statement"]["block_code"] = block_code
        result["authority_statement"]["block_reason"] = block_code
        result["source_body_operational_authority_summary"] = (
            build_source_body_operational_authority_summary(result)
        )
        return result
    if request is None:
        raise SourceBodyOperationalAuthorityBoundaryError(
            "request path returned neither request nor error"
        )
    request["authority_request_path"] = _stringify(declared_authority_request_path)
    return resolve_source_body_operational_authority_boundary(request)


def write_source_body_operational_authority_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    if not isinstance(result, Mapping):
        raise SourceBodyOperationalAuthorityBoundaryError("result must be a mapping")
    metadata = _as_mapping(result.get("source_body_operational_authority_metadata"))
    declared = _as_mapping(result.get("declared_authority_question"))
    result_id = _first_present(
        metadata.get("source_body_operational_authority_result_id"),
        declared.get("authority_request_id"),
        declared.get("selected_eligibility_result_id"),
        "source_body_operational_authority_result",
    )
    filename = f"{_sanitize_filename(result_id)}.json"
    if output_path is None:
        target = SOURCE_BODY_OPERATIONAL_AUTHORITY_BOUNDARY_ROOT / filename
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


def build_declared_source_body_operational_authority_request(
    authority_request_id: str,
    authority_question: str,
    selected_eligibility_result: Mapping[str, Any] | str,
    source_body_authority_basis: Mapping[str, Any] | str,
    authority_intent: str = INTENT_RECORD,
    *,
    selected_eligibility_result_path: str | None = None,
    selected_eligibility_result_id: str | None = None,
    selected_eligibility_result_outcome: str | None = None,
    requested_authority_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_sufficient_reason: str | None = None,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "authority_request_id": authority_request_id,
        "authority_question": authority_question,
        "authority_intent": authority_intent,
        "source_body_authority_basis": _copy(source_body_authority_basis),
        "selected_eligibility_result_id": selected_eligibility_result_id,
        "selected_eligibility_result_outcome": selected_eligibility_result_outcome,
        "expected_selected_eligibility_outcome": EXPECTED_ELIGIBILITY_OUTCOME,
        "requested_authority_outcome": requested_authority_outcome,
        "additional_basis_context": _copy(additional_basis_context)
        if additional_basis_context is not None
        else None,
        "not_sufficient_reason": not_sufficient_reason,
        "declared_non_claims": _copy(REQUIRED_NON_CLAIMS),
    }
    if selected_eligibility_result_path is not None:
        request["selected_eligibility_result_path"] = selected_eligibility_result_path
        if isinstance(selected_eligibility_result, Mapping):
            request["selected_eligibility_result"] = _copy(selected_eligibility_result)
    elif isinstance(selected_eligibility_result, Mapping):
        request["selected_eligibility_result"] = _copy(selected_eligibility_result)
    else:
        request["selected_eligibility_result_path"] = _stringify(selected_eligibility_result)

    if isinstance(source_body_authority_basis, Mapping):
        request.setdefault(
            "source_body_lineage_basis",
            source_body_authority_basis.get("source_body_lineage_basis"),
        )
        request.setdefault(
            "source_body_authority_reference",
            source_body_authority_basis.get("source_body_authority_reference"),
        )
        request.setdefault(
            "current_body_conformance_v4_closure_basis",
            source_body_authority_basis.get("current_body_conformance_v4_closure_basis"),
        )
        request.setdefault(
            "current_self_orientation_v9_basis",
            source_body_authority_basis.get("current_self_orientation_v9_basis"),
        )
        request.setdefault(
            "refusal_abort_awareness",
            source_body_authority_basis.get("refusal_abort_awareness"),
        )
    return request
