"""Bounded distributed operation eligibility boundary resolver.

This resolver evaluates one selected distributed operation matter declaration
for eligibility to proceed toward a future admission/authority review. It does
not admit operation, authorize operation, execute operation, decide
source-body authority, define carrier roles, synchronize repositories,
transfer the full body, create a second body, authorize continuation, create
consequence, create public readiness, claim final completion, schedule
follow-on work, or mutate upstream artifacts.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DistributedOperationEligibilityBoundaryError(Exception):
    """Hard failure for impossible eligibility write or shape errors."""


REPO_ROOT = Path(__file__).resolve().parents[1]
DISTRIBUTED_OPERATION_ELIGIBILITY_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_distributed_operation_eligibility_boundary"
)

RESOLVER_MODULE = "resolve_distributed_operation_eligibility_boundary"
RESULT_TYPE = "distributed_operation_eligibility_result"
RESULT_VERSION = "0.1.0"

OUTCOME_ELIGIBLE = "DISTRIBUTED_OPERATION_MATTER_ELIGIBLE_FOR_REVIEW"
OUTCOME_NOT_ELIGIBLE = "DISTRIBUTED_OPERATION_MATTER_NOT_ELIGIBLE_FOR_REVIEW"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DISTRIBUTED_OPERATION_MATTER_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_OPERATION_ELIGIBILITY_BLOCKED"
SUPPORTED_OUTCOMES = {
    OUTCOME_ELIGIBLE,
    OUTCOME_NOT_ELIGIBLE,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_DISTRIBUTED_OPERATION_ELIGIBILITY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DISTRIBUTED_OPERATION_ELIGIBILITY"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_OPERATION_ELIGIBILITY"
SUPPORTED_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

EXPECTED_SELECTED_MATTER_DECLARATION_OUTCOME = "DISTRIBUTED_OPERATION_MATTER_DECLARED"
EXPECTED_FAILED_CHECK_COUNT = 0

SUPPORTED_PROPOSED_OPERATION_KINDS = {
    "DISTRIBUTED_READINESS_REVIEW_CANDIDATE",
    "DISTRIBUTED_ARTIFACT_RECEIPT_REVIEW_CANDIDATE",
    "DISTRIBUTED_CARRIER_STATUS_REVIEW_CANDIDATE",
    "DISTRIBUTED_BOUNDARY_CONFORMANCE_REVIEW_CANDIDATE",
    "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "operation_admitted": False,
    "operation_authorized": False,
    "operation_executed": False,
    "source_body_authority_decided": False,
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
    "authority_created": False,
    "permission_created": False,
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

MATTER_DECLARATION_NON_CLAIM_FIELDS = tuple(
    key
    for key in REQUIRED_NON_CLAIMS
    if key not in {"source_body_authority_decided", "carrier_roles_defined"}
) + ("eligibility_decided",)

MATTER_DECLARATION_COLLAPSE_FIELDS: tuple[tuple[str, str], ...] = (
    ("operation_admitted", "MATTER_DECLARATION_ADMITTED_OPERATION"),
    ("declaration_admits_operation", "MATTER_DECLARATION_ADMITTED_OPERATION"),
    ("operation_authorized", "MATTER_DECLARATION_AUTHORIZED_OPERATION"),
    ("distributed_operation_authorized", "MATTER_DECLARATION_AUTHORIZED_OPERATION"),
    ("declaration_authorizes_operation", "MATTER_DECLARATION_AUTHORIZED_OPERATION"),
    ("declaration_authorized_operation", "MATTER_DECLARATION_AUTHORIZED_OPERATION"),
    ("operation_executed", "MATTER_DECLARATION_EXECUTED_OPERATION"),
    ("declaration_executes_operation", "MATTER_DECLARATION_EXECUTED_OPERATION"),
    ("declaration_executed_operation", "MATTER_DECLARATION_EXECUTED_OPERATION"),
)

ELIGIBILITY_COLLAPSE_FIELDS: tuple[tuple[str, str], ...] = (
    ("operation_admitted", "ELIGIBILITY_ADMITS_OPERATION"),
    ("eligibility_admits_operation", "ELIGIBILITY_ADMITS_OPERATION"),
    ("operation_authorized", "ELIGIBILITY_AUTHORIZES_OPERATION"),
    ("distributed_operation_authorized", "ELIGIBILITY_AUTHORIZES_OPERATION"),
    ("eligibility_authorizes_operation", "ELIGIBILITY_AUTHORIZES_OPERATION"),
    ("operation_executed", "ELIGIBILITY_EXECUTES_OPERATION"),
    ("eligibility_executes_operation", "ELIGIBILITY_EXECUTES_OPERATION"),
    ("source_body_authority_decided", "ELIGIBILITY_DECIDES_SOURCE_BODY_AUTHORITY"),
    (
        "eligibility_decides_source_body_authority",
        "ELIGIBILITY_DECIDES_SOURCE_BODY_AUTHORITY",
    ),
    ("carrier_roles_defined", "ELIGIBILITY_DEFINES_CARRIER_OPERATIONAL_ROLES"),
    (
        "eligibility_defines_carrier_operational_roles",
        "ELIGIBILITY_DEFINES_CARRIER_OPERATIONAL_ROLES",
    ),
    (
        "repository_synchronization_authorized",
        "ELIGIBILITY_AUTHORIZES_REPOSITORY_SYNC",
    ),
    ("repository_sync_authorized", "ELIGIBILITY_AUTHORIZES_REPOSITORY_SYNC"),
    ("full_body_transfer_authorized", "ELIGIBILITY_AUTHORIZES_FULL_BODY_TRANSFER"),
    ("second_body_created", "ELIGIBILITY_CREATES_SECOND_BODY"),
    ("continuation_authorized", "ELIGIBILITY_AUTHORIZES_CONTINUATION"),
    ("carrier_currentness_created", "ELIGIBILITY_CREATES_CARRIER_CURRENTNESS"),
    ("current_carrier_selected", "ELIGIBILITY_SELECTS_CURRENT_CARRIER"),
    ("winning_carrier_selected", "ELIGIBILITY_SELECTS_WINNING_CARRIER"),
    ("losing_carrier_invalidated", "ELIGIBILITY_INVALIDATES_LOSING_CARRIER"),
    ("source_replaced", "ELIGIBILITY_REPLACES_SOURCE"),
    ("authority_created", "ELIGIBILITY_CREATES_AUTHORITY"),
    ("permission_created", "ELIGIBILITY_CREATES_PERMISSION"),
    ("truth_created", "ELIGIBILITY_CREATES_TRUTH_OR_ACTION"),
    ("action_authorized", "ELIGIBILITY_CREATES_TRUTH_OR_ACTION"),
    ("consequence_created", "ELIGIBILITY_CREATES_CONSEQUENCE"),
    ("divergence_resolved", "ELIGIBILITY_RESOLVES_DIVERGENCE"),
    ("evidence_erased", "ELIGIBILITY_ERASES_EVIDENCE_OR_REFUSAL"),
    ("refusal_erased", "ELIGIBILITY_ERASES_EVIDENCE_OR_REFUSAL"),
    ("blocked_attempt_erased", "ELIGIBILITY_ERASES_EVIDENCE_OR_REFUSAL"),
    ("projection_mismatch_hidden", "ELIGIBILITY_ERASES_EVIDENCE_OR_REFUSAL"),
    ("public_launch_readiness_created", "ELIGIBILITY_CREATES_PUBLIC_READINESS"),
    ("public_readiness_created", "ELIGIBILITY_CREATES_PUBLIC_READINESS"),
    ("final_completion_claimed", "ELIGIBILITY_CLAIMS_FINAL_COMPLETION"),
    ("final_governance_completed", "ELIGIBILITY_CLAIMS_FINAL_COMPLETION"),
    ("final_continuity_completed", "ELIGIBILITY_CLAIMS_FINAL_COMPLETION"),
    ("final_system_identity_completed", "ELIGIBILITY_CLAIMS_FINAL_COMPLETION"),
    ("follow_on_work_authorized", "ELIGIBILITY_SCHEDULES_FOLLOW_ON_WORK"),
    ("self_orientation_successor_scheduled", "ELIGIBILITY_SCHEDULES_FOLLOW_ON_WORK"),
)

WHAT_REMAINS_OPEN = {
    "source_body_operational_authority_boundary": (
        "open_not_scheduled_not_authorized_not_executed"
    ),
    "carrier_operational_role_boundary": "open_not_scheduled_not_authorized_not_executed",
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


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _deepcopy(value: Any) -> Any:
    return copy.deepcopy(value)


def _to_path(path: Path | str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return REPO_ROOT / candidate


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None]:
    try:
        parsed = json.loads(_to_path(path).read_text(encoding="utf-8"))
    except OSError:
        return None, "unreadable"
    except json.JSONDecodeError:
        return None, "malformed"
    if not isinstance(parsed, Mapping):
        return None, "malformed"
    return dict(parsed), None


def _is_text(value: Any) -> bool:
    return isinstance(value, (str, bytes, bytearray))


def _non_empty(value: Any) -> bool:
    if value is None:
        return False
    if _is_text(value):
        return bool(str(value).strip())
    if isinstance(value, Mapping) or (
        isinstance(value, Sequence) and not _is_text(value)
    ):
        return len(value) > 0
    return True


def _as_mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _get_nested(mapping: Mapping[str, Any], paths: Sequence[Sequence[str]]) -> Any:
    for path in paths:
        current: Any = mapping
        found = True
        for key in path:
            if not isinstance(current, Mapping) or key not in current:
                found = False
                break
            current = current[key]
        if found:
            return current
    return None


def _iter_mappings(value: Any, depth: int = 0) -> list[Mapping[str, Any]]:
    if depth > 6:
        return []
    found: list[Mapping[str, Any]] = []
    if isinstance(value, Mapping):
        found.append(value)
        for key, child in value.items():
            if key in {
                "matter_declaration_non_meaning",
                "eligibility_non_meaning",
                "what_remains_open",
            }:
                continue
            found.extend(_iter_mappings(child, depth + 1))
    elif isinstance(value, Sequence) and not _is_text(value):
        for child in value:
            found.extend(_iter_mappings(child, depth + 1))
    return found


def _field_true(value: Any, field: str) -> bool:
    return any(container.get(field) is True for container in _iter_mappings(value))


def _any_field_true(value: Any, fields: Sequence[str]) -> bool:
    return any(_field_true(value, field) for field in fields)


def _first_true_field_code(
    value: Any,
    field_codes: Sequence[tuple[str, str]],
) -> str | None:
    if any(
        _field_true(value, field)
        for field in ("mutation_performed", "replay_performed", "merge_performed")
    ):
        return "MUTATION_REPLAY_OR_MERGE_DETECTED"
    for field, code in field_codes:
        if _field_true(value, field):
            return code
    return None


def _all_required_non_claims_false(non_claims: Any) -> bool:
    return isinstance(non_claims, Mapping) and all(
        non_claims.get(key) is False for key in REQUIRED_NON_CLAIMS
    )


def _all_matter_non_claims_false(matter: Mapping[str, Any]) -> bool:
    declared = _as_mapping(matter.get("declared_matter_question"))
    non_claims = matter.get("non_claims") or declared.get("declared_non_claims")
    return isinstance(non_claims, Mapping) and all(
        non_claims.get(key) is False for key in MATTER_DECLARATION_NON_CLAIM_FIELDS
    )


def _result_non_claims() -> dict[str, bool]:
    return dict(REQUIRED_NON_CLAIMS)


def _failed_check_count_from_checks(checks: Any) -> int | None:
    if not isinstance(checks, Sequence) or _is_text(checks):
        return None
    failed = 0
    saw_check = False
    for check in checks:
        if isinstance(check, Mapping):
            saw_check = True
            if check.get("passed") is not True:
                failed += 1
    return failed if saw_check else None


def _passed_check_count(checks: Any) -> int:
    if not isinstance(checks, Sequence) or _is_text(checks):
        return 0
    return sum(
        1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True
    )


def _matter_summary(matter: Mapping[str, Any]) -> Mapping[str, Any]:
    return _as_mapping(matter.get("distributed_operation_matter_declaration_summary"))


def _matter_statement(matter: Mapping[str, Any]) -> Mapping[str, Any]:
    return _as_mapping(matter.get("matter_declaration_statement"))


def _matter_collapse_scan(matter: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "declared_matter_question": _deepcopy(matter.get("declared_matter_question")),
        "operation_candidate": _deepcopy(matter.get("operation_candidate")),
        "operation_matter": _deepcopy(matter.get("operation_matter")),
        "operation_purpose": _deepcopy(matter.get("operation_purpose")),
        "proposed_operation_kind": _deepcopy(matter.get("proposed_operation_kind")),
        "selected_operation_basis": _deepcopy(matter.get("selected_operation_basis")),
        "selected_carrier_context": _deepcopy(matter.get("selected_carrier_context")),
        "proposed_affected_surfaces": _deepcopy(
            matter.get("proposed_affected_surfaces")
        ),
        "proposed_output_family": _deepcopy(matter.get("proposed_output_family")),
        "eligibility_review_request": _deepcopy(matter.get("eligibility_review_request")),
        "refusal_abort_awareness": _deepcopy(matter.get("refusal_abort_awareness")),
        "matter_declaration_statement": _deepcopy(matter.get("matter_declaration_statement")),
        "non_claims": _deepcopy(matter.get("non_claims")),
    }


def _eligibility_request_collapse_scan(request: Mapping[str, Any]) -> dict[str, Any]:
    clean = _deepcopy(dict(request))
    clean.pop("selected_matter_declaration", None)
    clean.pop("selected_matter_declaration_path", None)
    clean.pop("eligibility_non_meaning", None)
    clean.pop("what_remains_open", None)
    return clean


def _selected_matter_declaration_id(
    matter: Mapping[str, Any],
    request: Mapping[str, Any],
) -> Any:
    metadata = _as_mapping(matter.get("distributed_operation_matter_declaration_metadata"))
    declared = _as_mapping(matter.get("declared_matter_question"))
    summary = _matter_summary(matter)
    return (
        metadata.get("distributed_operation_matter_declaration_result_id")
        or request.get("selected_matter_declaration_id")
        or summary.get("matter_declaration_request_id")
        or declared.get("matter_declaration_request_id")
        or _operation_matter_id(request, matter)
    )


def _selected_matter_declaration_outcome(
    matter: Mapping[str, Any],
    request: Mapping[str, Any],
) -> Any:
    summary = _matter_summary(matter)
    return (
        matter.get("outcome")
        or summary.get("outcome")
        or request.get("selected_matter_declaration_outcome")
    )


def _selected_matter_failed_check_count(matter: Mapping[str, Any]) -> int | None:
    summary = _matter_summary(matter)
    statement = _matter_statement(matter)
    for value in (
        summary.get("failed_check_count"),
        statement.get("failed_check_count"),
    ):
        if isinstance(value, int):
            return value
    return _failed_check_count_from_checks(matter.get("matter_declaration_checks"))


def _operation_candidate_mapping(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Mapping[str, Any]:
    if isinstance(request.get("operation_candidate"), Mapping):
        return _as_mapping(request.get("operation_candidate"))
    return _as_mapping(matter.get("operation_candidate"))


def _operation_matter_mapping(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Mapping[str, Any]:
    if isinstance(request.get("operation_matter"), Mapping):
        return _as_mapping(request.get("operation_matter"))
    return _as_mapping(matter.get("operation_matter"))


def _operation_purpose_mapping(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Mapping[str, Any]:
    if isinstance(request.get("operation_purpose"), Mapping):
        return _as_mapping(request.get("operation_purpose"))
    return _as_mapping(matter.get("operation_purpose"))


def _operation_candidate_id(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    candidate = request.get("operation_candidate")
    candidate_section = _operation_candidate_mapping(request, matter)
    summary = _matter_summary(matter)
    if isinstance(candidate, str):
        return candidate
    return (
        request.get("operation_candidate_id")
        or candidate_section.get("operation_candidate_id")
        or _get_nested(
            candidate_section,
            (
                ("operation_candidate", "operation_candidate_id"),
                ("operation_candidate", "candidate_id"),
                ("operation_candidate", "id"),
            ),
        )
        or summary.get("operation_candidate_id")
    )


def _operation_matter_id(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    operation_matter = request.get("operation_matter")
    matter_section = _operation_matter_mapping(request, matter)
    summary = _matter_summary(matter)
    if isinstance(operation_matter, str):
        return operation_matter
    return (
        request.get("operation_matter_id")
        or matter_section.get("operation_matter_id")
        or matter_section.get("selected_matter_id")
        or _get_nested(
            matter_section,
            (
                ("operation_matter", "operation_matter_id"),
                ("operation_matter", "matter_id"),
                ("operation_matter", "id"),
            ),
        )
        or summary.get("operation_matter_id")
    )


def _operation_question(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    candidate = _operation_candidate_mapping(request, matter)
    matter_section = _operation_matter_mapping(request, matter)
    summary = _matter_summary(matter)
    return (
        request.get("operation_question")
        or candidate.get("declared_operation_question")
        or candidate.get("operation_question")
        or candidate.get("requested_operation_question")
        or _get_nested(
            candidate,
            (
                ("operation_candidate", "declared_operation_question"),
                ("operation_candidate", "operation_question"),
            ),
        )
        or matter_section.get("declared_operation_question")
        or matter_section.get("operation_question")
        or summary.get("operation_question")
    )


def _operation_purpose_value(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    purpose = request.get("operation_purpose")
    if isinstance(purpose, Mapping):
        return (
            purpose.get("declared_operation_purpose")
            or purpose.get("operation_purpose")
            or purpose.get("purpose")
            or purpose
        )
    if _non_empty(purpose):
        return purpose
    purpose_section = _operation_purpose_mapping(request, matter)
    summary = _matter_summary(matter)
    return (
        purpose_section.get("declared_operation_purpose")
        or purpose_section.get("operation_purpose")
        or purpose_section.get("purpose")
        or summary.get("operation_purpose")
    )


def _proposed_operation_kind(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    kind_section = _as_mapping(matter.get("proposed_operation_kind"))
    summary = _matter_summary(matter)
    return (
        request.get("proposed_operation_kind")
        or kind_section.get("proposed_operation_kind")
        or kind_section.get("selected_proposed_operation_kind")
        or summary.get("proposed_operation_kind")
    )


def _selected_operation_basis_value(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    return (
        request.get("selected_operation_basis")
        or _as_mapping(matter.get("selected_operation_basis")).get(
            "selected_operation_basis"
        )
        or matter.get("selected_operation_basis")
    )


def _selected_carrier_context_value(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    if "selected_carrier_context" in request:
        return request.get("selected_carrier_context")
    carrier = matter.get("selected_carrier_context")
    if isinstance(carrier, Mapping):
        return carrier.get("selected_carrier_context") or carrier
    return carrier


def _proposed_affected_surfaces_value(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    section = _as_mapping(matter.get("proposed_affected_surfaces"))
    return (
        request.get("proposed_affected_surfaces")
        or section.get("proposed_affected_surfaces")
        or section.get("declared_affected_surfaces")
        or matter.get("proposed_affected_surfaces")
    )


def _proposed_output_family_value(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    section = _as_mapping(matter.get("proposed_output_family"))
    return (
        request.get("proposed_output_family")
        or section.get("proposed_output_family")
        or section.get("declared_proposed_output_family")
        or matter.get("proposed_output_family")
    )


def _eligibility_review_request_value(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    section = _as_mapping(matter.get("eligibility_review_request"))
    return (
        request.get("eligibility_review_request")
        or section.get("eligibility_review_request")
        or matter.get("eligibility_review_request")
    )


def _refusal_abort_awareness_value(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    section = _as_mapping(matter.get("refusal_abort_awareness"))
    return (
        request.get("refusal_abort_awareness")
        or section.get("refusal_abort_awareness")
        or matter.get("refusal_abort_awareness")
    )


def _current_body_conformance_v4_closure_basis(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    eligibility_basis = _as_mapping(request.get("eligibility_basis"))
    selected_basis = _as_mapping(_selected_operation_basis_value(request, matter))
    selected_basis_nested = _as_mapping(selected_basis.get("selected_operation_basis"))
    return (
        request.get("current_body_conformance_v4_closure_basis")
        or eligibility_basis.get("current_body_conformance_v4_closure_basis")
        or selected_basis.get("current_body_conformance_v4_closure_basis")
        or selected_basis_nested.get("current_body_conformance_v4_closure_basis")
        or selected_basis.get("current_body_conformance_v4_closure_basis_path")
        or selected_basis_nested.get("current_body_conformance_v4_closure_basis_path")
    )


def _current_self_orientation_v9_basis(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    eligibility_basis = _as_mapping(request.get("eligibility_basis"))
    selected_basis = _as_mapping(_selected_operation_basis_value(request, matter))
    selected_basis_nested = _as_mapping(selected_basis.get("selected_operation_basis"))
    return (
        request.get("current_self_orientation_v9_basis")
        or eligibility_basis.get("current_self_orientation_v9_basis")
        or selected_basis.get("current_self_orientation_v9_basis")
        or selected_basis_nested.get("current_self_orientation_v9_basis")
        or selected_basis.get("current_self_orientation_v9_basis_path")
        or selected_basis_nested.get("current_self_orientation_v9_basis_path")
    )


def _distributed_standing_basis(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> Any:
    eligibility_basis = _as_mapping(request.get("eligibility_basis"))
    selected_basis = _as_mapping(_selected_operation_basis_value(request, matter))
    selected_basis_nested = _as_mapping(selected_basis.get("selected_operation_basis"))
    return (
        request.get("distributed_standing_basis")
        or eligibility_basis.get("distributed_standing_basis")
        or selected_basis.get("distributed_standing_basis")
        or selected_basis_nested.get("distributed_standing_basis")
        or selected_basis.get("distributed_standing_or_v4_closure_basis")
        or selected_basis_nested.get("distributed_standing_or_v4_closure_basis")
    )


def _source_body_basis(request: Mapping[str, Any], matter: Mapping[str, Any]) -> Any:
    eligibility_basis = _as_mapping(request.get("eligibility_basis"))
    selected_basis = _as_mapping(_selected_operation_basis_value(request, matter))
    selected_basis_nested = _as_mapping(selected_basis.get("selected_operation_basis"))
    return (
        request.get("source_body_basis")
        or eligibility_basis.get("source_body_basis")
        or selected_basis.get("source_body_basis")
        or selected_basis_nested.get("source_body_basis")
        or selected_basis.get("selected_source_body_basis")
        or selected_basis_nested.get("selected_source_body_basis")
    )


def _carrier_context_parseable(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, Mapping):
        return True
    if isinstance(value, Sequence) and not _is_text(value):
        return all(isinstance(item, Mapping) or _non_empty(item) for item in value)
    return False


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _checks(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
    selected_matter_path: str | None = None,
) -> list[dict[str, Any]]:
    intent = request.get("eligibility_intent")
    outcome = _selected_matter_declaration_outcome(matter, request)
    failed_count = _selected_matter_failed_check_count(matter)
    kind = _proposed_operation_kind(request, matter)
    request_scan = _eligibility_request_collapse_scan(request)
    matter_scan = _matter_collapse_scan(matter)
    carrier_context = _selected_carrier_context_value(request, matter)
    checks: list[dict[str, Any]] = [
        _make_check(
            "eligibility question declared",
            bool(request.get("eligibility_question")),
            "declared eligibility question",
            request.get("eligibility_question"),
            "ELIGIBILITY_QUESTION_UNDECLARED",
        ),
        _make_check(
            "eligibility intent supported",
            intent in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            intent,
            "ELIGIBILITY_INTENT_UNSUPPORTED",
        ),
        _make_check(
            "selected matter declaration present",
            bool(matter),
            "selected matter declaration result",
            bool(matter),
            "SELECTED_MATTER_DECLARATION_MISSING",
        ),
        _make_check(
            "selected matter declaration outcome declared",
            outcome is not None,
            "selected matter declaration outcome",
            outcome,
            "SELECTED_MATTER_DECLARATION_OUTCOME_MISSING",
        ),
        _make_check(
            "selected matter declaration outcome is declared",
            outcome == EXPECTED_SELECTED_MATTER_DECLARATION_OUTCOME,
            EXPECTED_SELECTED_MATTER_DECLARATION_OUTCOME,
            outcome,
            "SELECTED_MATTER_DECLARATION_NOT_DECLARED",
        ),
        _make_check(
            "selected matter declaration failed check count zero",
            failed_count == EXPECTED_FAILED_CHECK_COUNT,
            EXPECTED_FAILED_CHECK_COUNT,
            failed_count,
            "SELECTED_MATTER_DECLARATION_HAS_FAILED_CHECKS",
        ),
        _make_check(
            "operation candidate preserved",
            _non_empty(_operation_candidate_id(request, matter)),
            "operation candidate id",
            _operation_candidate_id(request, matter),
            "OPERATION_CANDIDATE_MISSING",
        ),
        _make_check(
            "operation matter preserved",
            _non_empty(_operation_matter_id(request, matter)),
            "operation matter id",
            _operation_matter_id(request, matter),
            "OPERATION_MATTER_MISSING",
        ),
        _make_check(
            "operation purpose preserved",
            _non_empty(_operation_purpose_value(request, matter)),
            "operation purpose",
            _operation_purpose_value(request, matter),
            "OPERATION_PURPOSE_MISSING",
        ),
        _make_check(
            "proposed operation kind preserved and supported",
            kind in SUPPORTED_PROPOSED_OPERATION_KINDS,
            sorted(SUPPORTED_PROPOSED_OPERATION_KINDS),
            kind,
            "OPERATION_KIND_MISSING_OR_UNSUPPORTED",
        ),
        _make_check(
            "selected operation basis preserved",
            _non_empty(_selected_operation_basis_value(request, matter)),
            "selected operation basis",
            _selected_operation_basis_value(request, matter),
            "SELECTED_OPERATION_BASIS_MISSING",
        ),
        _make_check(
            "selected carrier context parseable where applicable",
            _carrier_context_parseable(carrier_context),
            "mapping or bounded sequence when supplied",
            "not supplied" if carrier_context is None else type(carrier_context).__name__,
            "SELECTED_CARRIER_CONTEXT_MALFORMED",
        ),
        _make_check(
            "proposed affected surfaces preserved",
            _non_empty(_proposed_affected_surfaces_value(request, matter)),
            "selected proposed affected surfaces",
            _proposed_affected_surfaces_value(request, matter),
            "PROPOSED_AFFECTED_SURFACES_MISSING",
        ),
        _make_check(
            "proposed output family preserved",
            _non_empty(_proposed_output_family_value(request, matter)),
            "selected proposed output family",
            _proposed_output_family_value(request, matter),
            "PROPOSED_OUTPUT_FAMILY_MISSING",
        ),
        _make_check(
            "eligibility review request preserved",
            _non_empty(_eligibility_review_request_value(request, matter)),
            "selected eligibility review request",
            _eligibility_review_request_value(request, matter),
            "ELIGIBILITY_REVIEW_REQUEST_MISSING",
        ),
        _make_check(
            "refusal abort awareness preserved",
            _non_empty(_refusal_abort_awareness_value(request, matter)),
            "selected refusal/abort awareness",
            _refusal_abort_awareness_value(request, matter),
            "REFUSAL_ABORT_AWARENESS_MISSING",
        ),
        _make_check(
            "matter declaration non-claims remain false",
            _all_matter_non_claims_false(matter),
            "selected matter declaration non-claims false",
            _deepcopy(matter.get("non_claims")),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]

    matter_checks = (
        (
            "matter declaration did not admit operation",
            ("operation_admitted", "declaration_admits_operation"),
            "MATTER_DECLARATION_ADMITTED_OPERATION",
        ),
        (
            "matter declaration did not authorize operation",
            (
                "operation_authorized",
                "distributed_operation_authorized",
                "declaration_authorizes_operation",
                "declaration_authorized_operation",
            ),
            "MATTER_DECLARATION_AUTHORIZED_OPERATION",
        ),
        (
            "matter declaration did not execute operation",
            (
                "operation_executed",
                "declaration_executes_operation",
                "declaration_executed_operation",
            ),
            "MATTER_DECLARATION_EXECUTED_OPERATION",
        ),
        (
            "eligibility not already decided by matter declaration",
            ("eligibility_decided",),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    )
    for check_name, fields, code in matter_checks:
        actual = _any_field_true(matter_scan, fields)
        checks.append(_make_check(check_name, not actual, False, actual, code))

    eligibility_checks = (
        (
            "operation not admitted",
            ("operation_admitted", "eligibility_admits_operation"),
            "ELIGIBILITY_ADMITS_OPERATION",
        ),
        (
            "operation not authorized",
            (
                "operation_authorized",
                "distributed_operation_authorized",
                "eligibility_authorizes_operation",
            ),
            "ELIGIBILITY_AUTHORIZES_OPERATION",
        ),
        (
            "operation not executed",
            ("operation_executed", "eligibility_executes_operation"),
            "ELIGIBILITY_EXECUTES_OPERATION",
        ),
        (
            "no repository synchronization authorized",
            ("repository_synchronization_authorized", "repository_sync_authorized"),
            "ELIGIBILITY_AUTHORIZES_REPOSITORY_SYNC",
        ),
        (
            "no full body transfer authorized",
            ("full_body_transfer_authorized",),
            "ELIGIBILITY_AUTHORIZES_FULL_BODY_TRANSFER",
        ),
        (
            "no second body created",
            ("second_body_created",),
            "ELIGIBILITY_CREATES_SECOND_BODY",
        ),
        (
            "no continuation authorized",
            ("continuation_authorized",),
            "ELIGIBILITY_AUTHORIZES_CONTINUATION",
        ),
        (
            "no distributed operation authorized",
            ("distributed_operation_authorized",),
            "ELIGIBILITY_AUTHORIZES_OPERATION",
        ),
        (
            "no carrier currentness collapse",
            ("carrier_currentness_created",),
            "ELIGIBILITY_CREATES_CARRIER_CURRENTNESS",
        ),
        (
            "no current carrier selected",
            ("current_carrier_selected",),
            "ELIGIBILITY_SELECTS_CURRENT_CARRIER",
        ),
        (
            "no winning carrier selected",
            ("winning_carrier_selected",),
            "ELIGIBILITY_SELECTS_WINNING_CARRIER",
        ),
        (
            "no losing carrier invalidated",
            ("losing_carrier_invalidated",),
            "ELIGIBILITY_INVALIDATES_LOSING_CARRIER",
        ),
        (
            "no source replaced",
            ("source_replaced",),
            "ELIGIBILITY_REPLACES_SOURCE",
        ),
        (
            "no authority created",
            ("authority_created",),
            "ELIGIBILITY_CREATES_AUTHORITY",
        ),
        (
            "no permission created",
            ("permission_created",),
            "ELIGIBILITY_CREATES_PERMISSION",
        ),
        (
            "no truth created",
            ("truth_created",),
            "ELIGIBILITY_CREATES_TRUTH_OR_ACTION",
        ),
        (
            "no action authorized",
            ("action_authorized",),
            "ELIGIBILITY_CREATES_TRUTH_OR_ACTION",
        ),
        (
            "no consequence created",
            ("consequence_created",),
            "ELIGIBILITY_CREATES_CONSEQUENCE",
        ),
        (
            "no public readiness created",
            ("public_launch_readiness_created", "public_readiness_created"),
            "ELIGIBILITY_CREATES_PUBLIC_READINESS",
        ),
        (
            "no final completion claimed",
            (
                "final_completion_claimed",
                "final_governance_completed",
                "final_continuity_completed",
                "final_system_identity_completed",
            ),
            "ELIGIBILITY_CLAIMS_FINAL_COMPLETION",
        ),
        (
            "no follow-on work scheduled",
            ("follow_on_work_authorized", "self_orientation_successor_scheduled"),
            "ELIGIBILITY_SCHEDULES_FOLLOW_ON_WORK",
        ),
        (
            "no source-body authority decided",
            ("source_body_authority_decided",),
            "ELIGIBILITY_DECIDES_SOURCE_BODY_AUTHORITY",
        ),
        (
            "no carrier roles defined",
            ("carrier_roles_defined",),
            "ELIGIBILITY_DEFINES_CARRIER_OPERATIONAL_ROLES",
        ),
        (
            "no divergence resolved",
            ("divergence_resolved",),
            "ELIGIBILITY_RESOLVES_DIVERGENCE",
        ),
        (
            "no evidence refusal or projection mismatch erased",
            (
                "evidence_erased",
                "refusal_erased",
                "blocked_attempt_erased",
                "projection_mismatch_hidden",
            ),
            "ELIGIBILITY_ERASES_EVIDENCE_OR_REFUSAL",
        ),
    )
    for check_name, fields, code in eligibility_checks:
        actual = _any_field_true(request_scan, fields)
        checks.append(_make_check(check_name, not actual, False, actual, code))

    mutation_detected = any(
        _field_true(request_scan, field)
        for field in ("mutation_performed", "replay_performed", "merge_performed")
    )
    checks.append(
        _make_check(
            "no mutation replay or merge",
            not mutation_detected,
            False,
            mutation_detected,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        )
    )
    checks.append(
        _make_check(
            "eligibility non-claims remain false",
            _all_required_non_claims_false(request.get("declared_non_claims")),
            REQUIRED_NON_CLAIMS,
            _deepcopy(request.get("declared_non_claims")),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    if selected_matter_path:
        checks.append(
            _make_check(
                "selected matter declaration readable from path",
                True,
                "readable JSON object",
                selected_matter_path,
                "SELECTED_MATTER_DECLARATION_UNREADABLE",
            )
        )
    return checks


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if code:
                return str(code)
    return None


def _metadata(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> dict[str, Any]:
    result_source = (
        request.get("eligibility_request_id")
        or _operation_matter_id(request, matter)
        or _selected_matter_declaration_id(matter, request)
        or "undeclared"
    )
    return {
        "distributed_operation_eligibility_result_id": (
            f"{result_source}__distributed_operation_eligibility_result"
        ),
        "distributed_operation_eligibility_result_type": RESULT_TYPE,
        "distributed_operation_eligibility_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _declared_eligibility_question(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
    request_path: str | None = None,
) -> dict[str, Any]:
    return {
        "eligibility_request_id": request.get("eligibility_request_id"),
        "eligibility_question": request.get("eligibility_question"),
        "eligibility_intent": request.get("eligibility_intent"),
        "declared_eligibility_request_path": request_path
        or request.get("declared_eligibility_request_path"),
        "selected_matter_declaration_id": _selected_matter_declaration_id(
            matter,
            request,
        ),
        "selected_matter_declaration_outcome": _selected_matter_declaration_outcome(
            matter,
            request,
        ),
        "declared_non_claims": _deepcopy(request.get("declared_non_claims")),
        "eligibility_is_not_admission": True,
        "eligibility_is_not_authorization": True,
        "eligibility_is_not_execution": True,
        "eligibility_is_not_operation": True,
        "eligibility_is_not_synchronization": True,
        "eligibility_is_not_full_body_transfer": True,
        "eligibility_is_not_continuation": True,
        "eligibility_is_not_permission": True,
        "eligibility_does_not_mutate_selected_matter": True,
    }


def _selected_matter_declaration_section(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
    selected_matter_path: str | None = None,
) -> dict[str, Any]:
    failed_count = _selected_matter_failed_check_count(matter)
    outcome = _selected_matter_declaration_outcome(matter, request)
    matter_scan = _matter_collapse_scan(matter)
    admitted = _any_field_true(
        matter_scan,
        ("operation_admitted", "declaration_admits_operation"),
    )
    authorized = _any_field_true(
        matter_scan,
        (
            "operation_authorized",
            "distributed_operation_authorized",
            "declaration_authorizes_operation",
        ),
    )
    executed = _any_field_true(
        matter_scan,
        ("operation_executed", "declaration_executes_operation"),
    )
    return {
        "selected_matter_declaration": _deepcopy(matter),
        "selected_matter_declaration_path": selected_matter_path
        or request.get("selected_matter_declaration_path"),
        "selected_matter_declaration_id": _selected_matter_declaration_id(
            matter,
            request,
        ),
        "selected_matter_declaration_outcome": outcome,
        "selected_matter_declaration_is_declared": (
            outcome == EXPECTED_SELECTED_MATTER_DECLARATION_OUTCOME
        ),
        "selected_matter_declaration_failed_check_count": failed_count,
        "selected_matter_declaration_failed_check_count_zero": (
            failed_count == EXPECTED_FAILED_CHECK_COUNT
        ),
        "selected_matter_declaration_remains_declaration_only": True,
        "selected_matter_declaration_did_not_admit_operation": not admitted,
        "selected_matter_declaration_did_not_authorize_operation": not authorized,
        "selected_matter_declaration_did_not_execute_operation": not executed,
        "selected_matter_declaration_not_mutated": True,
    }


def _selected_operation_candidate_section(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "operation_candidate": _deepcopy(_operation_candidate_mapping(request, matter)),
        "operation_candidate_id": _operation_candidate_id(request, matter),
        "selected_operation_question": _operation_question(request, matter),
        "candidate_remains_candidate_only": True,
        "candidate_not_admitted": True,
        "candidate_not_authorized": True,
        "candidate_not_executed": True,
        "candidate_not_eligible_by_declaration": True,
        "eligibility_does_not_make_candidate_operation": True,
    }


def _selected_operation_matter_section(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "operation_matter": _deepcopy(_operation_matter_mapping(request, matter)),
        "operation_matter_id": _operation_matter_id(request, matter),
        "selected_matter_id": _selected_matter_declaration_id(matter, request),
        "matter_declaration_outcome": _selected_matter_declaration_outcome(
            matter,
            request,
        ),
        "matter_remains_declaration_only": True,
        "matter_not_upgraded_into_admission": True,
        "matter_not_upgraded_into_authorization": True,
        "matter_not_upgraded_into_operation": True,
    }


def _eligibility_basis_section(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "eligibility_basis": _deepcopy(request.get("eligibility_basis")),
        "selected_matter_declaration_result": _deepcopy(matter),
        "selected_matter_identity": _selected_matter_declaration_id(matter, request),
        "selected_operation_candidate_identity": _operation_candidate_id(request, matter),
        "selected_operation_question": _operation_question(request, matter),
        "selected_operation_purpose": _deepcopy(_operation_purpose_value(request, matter)),
        "selected_proposed_operation_kind": _proposed_operation_kind(request, matter),
        "selected_operation_basis": _deepcopy(
            _selected_operation_basis_value(request, matter)
        ),
        "selected_carrier_context": _deepcopy(
            _selected_carrier_context_value(request, matter)
        ),
        "selected_proposed_affected_surfaces": _deepcopy(
            _proposed_affected_surfaces_value(request, matter)
        ),
        "selected_proposed_output_family": _deepcopy(
            _proposed_output_family_value(request, matter)
        ),
        "selected_eligibility_review_request": _deepcopy(
            _eligibility_review_request_value(request, matter)
        ),
        "selected_refusal_abort_awareness": _deepcopy(
            _refusal_abort_awareness_value(request, matter)
        ),
        "current_body_conformance_v4_closure_basis": _deepcopy(
            _current_body_conformance_v4_closure_basis(request, matter)
        ),
        "current_self_orientation_v9_basis": _deepcopy(
            _current_self_orientation_v9_basis(request, matter)
        ),
        "distributed_standing_basis": _deepcopy(
            _distributed_standing_basis(request, matter)
        ),
        "source_body_basis": _deepcopy(_source_body_basis(request, matter)),
        "eligibility_basis_is_not_permission": True,
        "eligibility_basis_is_not_admission": True,
        "eligibility_basis_is_not_operation_plan": True,
        "eligibility_basis_is_not_synchronization_plan": True,
        "eligibility_basis_is_not_full_body_transfer_plan": True,
    }


def _additional_basis_required_section(
    outcome: str,
    request: Mapping[str, Any],
) -> dict[str, Any]:
    context = _as_mapping(request.get("additional_basis_context"))
    requires = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": requires,
        "additional_basis_context": _deepcopy(context),
        "additional_basis_reason": request.get("additional_basis_reason")
        or context.get("additional_basis_reason"),
        "source_body_operational_authority_basis_insufficient": bool(
            context.get("source_body_operational_authority_basis_insufficient")
        ),
        "carrier_role_basis_insufficient": bool(
            context.get("carrier_role_basis_insufficient")
        ),
        "synchronization_non_synchronization_basis_insufficient": bool(
            context.get("synchronization_non_synchronization_basis_insufficient")
        ),
        "refusal_abort_law_insufficient": bool(
            context.get("refusal_abort_law_insufficient")
        ),
        "affected_surface_scope_insufficient": bool(
            context.get("affected_surface_scope_insufficient")
        ),
        "proposed_output_family_insufficient": bool(
            context.get("proposed_output_family_insufficient")
        ),
        "operation_candidate_too_broad": bool(
            context.get("operation_candidate_too_broad")
        ),
        "carrier_context_too_broad": bool(context.get("carrier_context_too_broad")),
        "source_body_basis_too_generic": bool(
            context.get("source_body_basis_too_generic")
        ),
        "additional_basis_not_scheduled": True,
        "additional_basis_not_authorized": True,
        "additional_basis_not_executed": True,
    }


def _eligibility_statement(
    outcome: str,
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    eligible = outcome == OUTCOME_ELIGIBLE
    not_eligible = outcome == OUTCOME_NOT_ELIGIBLE
    requires_additional = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    selected_outcome = _selected_matter_declaration_outcome(matter, request)
    selected_failed_count = _selected_matter_failed_check_count(matter)
    statement = {
        "distributed_operation_matter_eligible_for_review": eligible,
        "distributed_operation_matter_not_eligible_for_review": not_eligible,
        "distributed_operation_matter_requires_additional_basis": requires_additional,
        "selected_matter_declaration_preserved": bool(matter),
        "selected_matter_declaration_declared": (
            selected_outcome == EXPECTED_SELECTED_MATTER_DECLARATION_OUTCOME
        ),
        "selected_matter_declaration_failed_check_count_zero": (
            selected_failed_count == EXPECTED_FAILED_CHECK_COUNT
        ),
        "operation_candidate_preserved": _non_empty(
            _operation_candidate_id(request, matter)
        ),
        "operation_matter_preserved": _non_empty(_operation_matter_id(request, matter)),
        "operation_purpose_preserved": _non_empty(
            _operation_purpose_value(request, matter)
        ),
        "proposed_operation_kind_preserved": _proposed_operation_kind(request, matter)
        in SUPPORTED_PROPOSED_OPERATION_KINDS,
        "selected_operation_basis_preserved": _non_empty(
            _selected_operation_basis_value(request, matter)
        ),
        "proposed_affected_surfaces_preserved": _non_empty(
            _proposed_affected_surfaces_value(request, matter)
        ),
        "proposed_output_family_preserved": _non_empty(
            _proposed_output_family_value(request, matter)
        ),
        "eligibility_review_request_preserved": _non_empty(
            _eligibility_review_request_value(request, matter)
        ),
        "refusal_abort_awareness_preserved": _non_empty(
            _refusal_abort_awareness_value(request, matter)
        ),
        "future_admission_authority_review_may_be_considered": eligible,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "source_body_authority_decided": False,
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
        "authority_created": False,
        "permission_created": False,
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
        "selected_matter_declaration_not_mutated": True,
        "failed_check_count": failed_count,
    }
    if not_eligible:
        statement["not_eligible_reason"] = request.get(
            "not_eligible_reason",
            "Selected matter is readable but not eligible for future review.",
        )
    if requires_additional:
        statement["additional_basis_reason"] = request.get(
            "additional_basis_reason",
            "Selected matter requires additional bounded basis before eligibility.",
        )
        statement["missing_basis_not_scheduled"] = True
        statement["missing_basis_not_authorized"] = True
    if outcome == OUTCOME_BLOCKED:
        statement["distributed_operation_matter_eligible_for_review"] = False
    return statement


def _eligibility_non_meaning() -> dict[str, bool]:
    non_meaning = {
        "operation_admitted": True,
        "operation_authorized": True,
        "operation_executed": True,
        "source_body_authority_decided": True,
        "carrier_roles_decided": True,
        "synchronization_authorized": True,
        "full_body_transfer_authorized": True,
        "second_body_created": True,
        "continuation_authorized": True,
        "distributed_operation_authorized": True,
        "carrier_currentness_created": True,
        "current_carrier_selected": True,
        "winning_carrier_selected": True,
        "losing_carrier_invalidated": True,
        "source_replaced": True,
        "authority_created": True,
        "permission_created": True,
        "truth_action_created": True,
        "consequence_created": True,
        "divergence_resolved": True,
        "evidence_erased": True,
        "refusal_erased": True,
        "blocked_attempt_erased": True,
        "projection_mismatch_hidden": True,
        "public_launch_readiness_created": True,
        "final_completion_claimed": True,
        "final_governance_completed": True,
        "final_continuity_completed": True,
        "final_system_identity_completed": True,
        "follow_on_work_authorized": True,
        "self_orientation_successor_scheduled": True,
    }
    for key in tuple(non_meaning):
        non_meaning[f"does_not_mean_{key}"] = True
    return non_meaning


def _block(outcome: str, code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {
        "blocked": outcome == OUTCOME_BLOCKED,
        "block_code": code if outcome == OUTCOME_BLOCKED else None,
        "block_reason": reason if outcome == OUTCOME_BLOCKED else None,
    }


def _base_result(
    request: Mapping[str, Any],
    matter: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None = None,
    block_reason: str | None = None,
    request_path: str | None = None,
    selected_matter_path: str | None = None,
) -> dict[str, Any]:
    result = {
        "distributed_operation_eligibility_metadata": _metadata(request, matter),
        "declared_eligibility_question": _declared_eligibility_question(
            request,
            matter,
            request_path,
        ),
        "selected_matter_declaration": _selected_matter_declaration_section(
            request,
            matter,
            selected_matter_path,
        ),
        "selected_operation_candidate": _selected_operation_candidate_section(
            request,
            matter,
        ),
        "selected_operation_matter": _selected_operation_matter_section(request, matter),
        "eligibility_basis": _eligibility_basis_section(request, matter),
        "eligibility_checks": list(checks),
        "eligibility_statement": _eligibility_statement(outcome, request, matter, checks),
        "eligibility_non_meaning": _eligibility_non_meaning(),
        "additional_basis_required": _additional_basis_required_section(outcome, request),
        "what_remains_open": _deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": _result_non_claims(),
        "outcome": outcome,
        "block": _block(outcome, block_code, block_reason),
    }
    result["distributed_operation_eligibility_summary"] = (
        build_distributed_operation_eligibility_summary(result)
    )
    return result


def _blocked_result(
    request: Mapping[str, Any] | None,
    code: str,
    reason: str,
    request_path: str | None = None,
    selected_matter: Mapping[str, Any] | None = None,
    selected_matter_path: str | None = None,
) -> dict[str, Any]:
    clean_request = _deepcopy(dict(request)) if isinstance(request, Mapping) else {}
    clean_matter = _deepcopy(dict(selected_matter)) if isinstance(selected_matter, Mapping) else {}
    checks = [
        _make_check(
            "eligibility blocked",
            False,
            "lawful bounded eligibility request",
            reason,
            code,
        )
    ]
    return _base_result(
        clean_request,
        clean_matter,
        OUTCOME_BLOCKED,
        checks,
        code,
        reason,
        request_path,
        selected_matter_path,
    )


def _load_selected_matter_declaration(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    path_value = request.get("selected_matter_declaration_path")
    if path_value:
        path = _to_path(path_value)
        parsed, error = _read_json_object(path)
        if error == "unreadable":
            return None, "SELECTED_MATTER_DECLARATION_UNREADABLE", str(path)
        if error == "malformed":
            return None, "SELECTED_MATTER_DECLARATION_MALFORMED", str(path)
        return _deepcopy(parsed), None, str(path)

    selected = request.get("selected_matter_declaration")
    if selected is None:
        return None, "SELECTED_MATTER_DECLARATION_MISSING", None
    if not isinstance(selected, Mapping):
        return None, "SELECTED_MATTER_DECLARATION_MALFORMED", None
    return _deepcopy(dict(selected)), None, None


def resolve_distributed_operation_eligibility_boundary(
    declared_eligibility_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one distributed operation eligibility boundary request."""

    if declared_eligibility_request is None:
        return _blocked_result(
            {},
            "ELIGIBILITY_QUESTION_UNDECLARED",
            "No declared eligibility request was supplied.",
        )
    if not isinstance(declared_eligibility_request, Mapping):
        return _blocked_result(
            {},
            "DECLARED_ELIGIBILITY_REQUEST_MALFORMED",
            "Declared eligibility request must be a mapping.",
        )

    request: dict[str, Any] = _deepcopy(dict(declared_eligibility_request))
    request_path = request.get("declared_eligibility_request_path")
    if not request.get("eligibility_question"):
        return _blocked_result(
            request,
            "ELIGIBILITY_QUESTION_UNDECLARED",
            "Eligibility question is undeclared.",
            request_path,
        )

    intent = request.get("eligibility_intent")
    if intent == INTENT_BLOCK:
        return _blocked_result(
            request,
            "ELIGIBILITY_REQUEST_EXPLICITLY_BLOCKED",
            request.get("block_reason") or "Eligibility request explicitly blocked.",
            request_path,
        )
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(
            request,
            "ELIGIBILITY_INTENT_UNSUPPORTED",
            "Eligibility intent is unsupported.",
            request_path,
        )

    selected_matter, load_error, selected_matter_path = _load_selected_matter_declaration(
        request
    )
    if load_error:
        return _blocked_result(
            request,
            load_error,
            request.get("block_reason") or load_error,
            request_path,
            selected_matter,
            selected_matter_path,
        )
    matter = selected_matter or {}

    checks = _checks(request, matter, selected_matter_path)
    failed_code = _first_failed_code(checks)
    matter_collapse_code = _first_true_field_code(
        _matter_collapse_scan(matter),
        MATTER_DECLARATION_COLLAPSE_FIELDS,
    )
    eligibility_collapse_code = _first_true_field_code(
        _eligibility_request_collapse_scan(request),
        ELIGIBILITY_COLLAPSE_FIELDS,
    )
    block_code = matter_collapse_code or eligibility_collapse_code or failed_code

    if block_code:
        return _base_result(
            request,
            matter,
            OUTCOME_BLOCKED,
            checks,
            block_code,
            request.get("block_reason") or block_code,
            request_path,
            selected_matter_path,
        )

    requested_outcome = request.get("requested_eligibility_outcome")
    if (
        intent == INTENT_DO_NOT_RECORD
        or requested_outcome == OUTCOME_NOT_ELIGIBLE
        or request.get("eligible_for_review") is False
        or request.get("not_eligible_reason")
    ):
        return _base_result(
            request,
            matter,
            OUTCOME_NOT_ELIGIBLE,
            checks,
            request_path=request_path,
            selected_matter_path=selected_matter_path,
        )

    if (
        requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        or _non_empty(request.get("additional_basis_context"))
        or request.get("requires_additional_basis") is True
    ):
        return _base_result(
            request,
            matter,
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            checks,
            request_path=request_path,
            selected_matter_path=selected_matter_path,
        )

    return _base_result(
        request,
        matter,
        OUTCOME_ELIGIBLE,
        checks,
        request_path=request_path,
        selected_matter_path=selected_matter_path,
    )


def resolve_distributed_operation_eligibility_boundary_from_path(
    declared_eligibility_request_path: Path | str,
) -> dict:
    """Load a declared eligibility request JSON object and resolve it."""

    path = _to_path(declared_eligibility_request_path)
    parsed, error = _read_json_object(path)
    if error == "unreadable":
        return _blocked_result(
            {},
            "DECLARED_ELIGIBILITY_REQUEST_UNREADABLE",
            "Declared eligibility request path is unreadable.",
            str(path),
        )
    if error == "malformed":
        return _blocked_result(
            {},
            "DECLARED_ELIGIBILITY_REQUEST_MALFORMED",
            "Declared eligibility request JSON must be an object.",
            str(path),
        )
    request = _deepcopy(parsed)
    request["declared_eligibility_request_path"] = str(path)
    result = resolve_distributed_operation_eligibility_boundary(request)
    result["declared_eligibility_question"]["declared_eligibility_request_path"] = str(path)
    result["distributed_operation_eligibility_summary"] = (
        build_distributed_operation_eligibility_summary(result)
    )
    return result


def build_distributed_operation_eligibility_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded summary for a distributed operation eligibility result."""

    checks = result.get("eligibility_checks")
    if not isinstance(checks, Sequence) or _is_text(checks):
        checks = []
    passed = _passed_check_count(checks)
    failed = sum(
        1 for check in checks if isinstance(check, Mapping) and check.get("passed") is not True
    )
    declared = _as_mapping(result.get("declared_eligibility_question"))
    selected = _as_mapping(result.get("selected_matter_declaration"))
    candidate = _as_mapping(result.get("selected_operation_candidate"))
    matter = _as_mapping(result.get("selected_operation_matter"))
    basis = _as_mapping(result.get("eligibility_basis"))
    statement = _as_mapping(result.get("eligibility_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "eligibility_request_id": declared.get("eligibility_request_id"),
        "eligibility_question": declared.get("eligibility_question"),
        "eligibility_intent": declared.get("eligibility_intent"),
        "selected_matter_declaration_id": selected.get(
            "selected_matter_declaration_id"
        ),
        "selected_matter_declaration_outcome": selected.get(
            "selected_matter_declaration_outcome"
        ),
        "operation_candidate_id": candidate.get("operation_candidate_id"),
        "operation_matter_id": matter.get("operation_matter_id"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "matter_eligible_for_review": statement.get(
            "distributed_operation_matter_eligible_for_review",
            False,
        ),
        "matter_not_eligible": statement.get(
            "distributed_operation_matter_not_eligible_for_review",
            False,
        ),
        "requires_additional_basis": statement.get(
            "distributed_operation_matter_requires_additional_basis",
            False,
        ),
        "selected_matter_declaration_preserved": statement.get(
            "selected_matter_declaration_preserved",
            False,
        ),
        "selected_matter_declaration_declared": statement.get(
            "selected_matter_declaration_declared",
            False,
        ),
        "selected_matter_declaration_failed_check_count_zero": statement.get(
            "selected_matter_declaration_failed_check_count_zero",
            False,
        ),
        "operation_candidate_preserved": statement.get(
            "operation_candidate_preserved",
            False,
        ),
        "operation_matter_preserved": statement.get("operation_matter_preserved", False),
        "operation_purpose_preserved": statement.get(
            "operation_purpose_preserved",
            False,
        ),
        "proposed_operation_kind_preserved": statement.get(
            "proposed_operation_kind_preserved",
            False,
        ),
        "selected_operation_basis_preserved": statement.get(
            "selected_operation_basis_preserved",
            False,
        ),
        "proposed_affected_surfaces_preserved": statement.get(
            "proposed_affected_surfaces_preserved",
            False,
        ),
        "proposed_output_family_preserved": statement.get(
            "proposed_output_family_preserved",
            False,
        ),
        "eligibility_review_request_preserved": statement.get(
            "eligibility_review_request_preserved",
            False,
        ),
        "refusal_abort_awareness_preserved": statement.get(
            "refusal_abort_awareness_preserved",
            False,
        ),
        "future_admission_authority_review_may_be_considered": statement.get(
            "future_admission_authority_review_may_be_considered",
            False,
        ),
        "selected_operation_question": basis.get("selected_operation_question"),
        "selected_operation_purpose": basis.get("selected_operation_purpose"),
        "selected_proposed_operation_kind": basis.get("selected_proposed_operation_kind"),
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "source_body_authority_decided": False,
        "carrier_roles_defined": False,
        "no_sync_full_body_transfer_second_body": (
            statement.get("repository_synchronization_authorized") is False
            and statement.get("full_body_transfer_authorized") is False
            and statement.get("second_body_created") is False
        ),
        "no_continuation_distributed_operation": (
            statement.get("continuation_authorized") is False
            and statement.get("distributed_operation_authorized") is False
        ),
        "no_carrier_currentness_current_winning_losing_carrier": (
            statement.get("carrier_currentness_created") is False
            and statement.get("current_carrier_selected") is False
            and statement.get("winning_carrier_selected") is False
            and statement.get("losing_carrier_invalidated") is False
        ),
        "no_source_authority_permission_truth_action_consequence": (
            statement.get("source_replaced") is False
            and statement.get("authority_created") is False
            and statement.get("permission_created") is False
            and statement.get("truth_created") is False
            and statement.get("action_authorized") is False
            and statement.get("consequence_created") is False
        ),
        "no_public_readiness_final_completion_follow_on_work": (
            statement.get("public_launch_readiness_created") is False
            and statement.get("final_completion_claimed") is False
            and statement.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
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
                "public_launch_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
            )
        },
    }


def _safe_filename_part(value: Any) -> str:
    text = str(value or "distributed_operation_eligibility")
    safe = []
    for char in text:
        safe.append(char if char.isalnum() or char in {"-", "_"} else "_")
    return "".join(safe).strip("_") or "distributed_operation_eligibility"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter:03d}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def write_distributed_operation_eligibility_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an eligibility result as additive UTF-8 JSON."""

    if not isinstance(result, Mapping):
        raise DistributedOperationEligibilityBoundaryError("result must be a mapping")
    if output_path is None:
        summary = _as_mapping(result.get("distributed_operation_eligibility_summary"))
        request_id = summary.get("eligibility_request_id") or summary.get(
            "operation_matter_id"
        )
        filename = (
            f"{_safe_filename_part(request_id)}"
            "__distributed_operation_eligibility_result.json"
        )
        output = DISTRIBUTED_OPERATION_ELIGIBILITY_BOUNDARY_ROOT / filename
    else:
        output = Path(output_path)
    output = _non_overwriting_path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return output


def _matter_request_non_claims() -> dict[str, bool]:
    return {key: False for key in MATTER_DECLARATION_NON_CLAIM_FIELDS}


def _minimal_selected_matter_from_reference(
    selected_matter_declaration: Mapping[str, Any] | str,
    selected_matter_declaration_id: str | None,
    selected_matter_declaration_outcome: str | None,
) -> dict[str, Any]:
    if isinstance(selected_matter_declaration, Mapping):
        return _deepcopy(dict(selected_matter_declaration))
    matter_id = selected_matter_declaration_id or str(selected_matter_declaration)
    outcome = (
        selected_matter_declaration_outcome
        or EXPECTED_SELECTED_MATTER_DECLARATION_OUTCOME
    )
    return {
        "outcome": outcome,
        "distributed_operation_matter_declaration_metadata": {
            "distributed_operation_matter_declaration_result_id": matter_id,
        },
        "distributed_operation_matter_declaration_summary": {
            "matter_declaration_request_id": matter_id,
            "outcome": outcome,
            "failed_check_count": 0,
        },
        "matter_declaration_statement": {
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
            "eligibility_decided": False,
        },
        "non_claims": _matter_request_non_claims(),
    }


def build_declared_distributed_operation_eligibility_request(
    eligibility_request_id: str,
    eligibility_question: str,
    selected_matter_declaration: Mapping[str, Any] | str,
    eligibility_basis: Mapping[str, Any] | str,
    eligibility_intent: str = INTENT_RECORD,
    *,
    selected_matter_declaration_path: str | None = None,
    selected_matter_declaration_id: str | None = None,
    selected_matter_declaration_outcome: str | None = None,
    requested_eligibility_outcome: str = OUTCOME_ELIGIBLE,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_eligible_reason: str | None = None,
) -> dict:
    """Build a bounded declared eligibility request with non-claims false."""

    selected_matter = _minimal_selected_matter_from_reference(
        selected_matter_declaration,
        selected_matter_declaration_id,
        selected_matter_declaration_outcome,
    )
    basis = _deepcopy(eligibility_basis)
    basis_mapping = basis if isinstance(basis, Mapping) else {}
    request = {
        "eligibility_request_id": eligibility_request_id,
        "eligibility_question": eligibility_question,
        "eligibility_intent": eligibility_intent,
        "selected_matter_declaration": selected_matter,
        "selected_matter_declaration_id": selected_matter_declaration_id
        or _selected_matter_declaration_id(selected_matter, {}),
        "selected_matter_declaration_outcome": selected_matter_declaration_outcome
        or _selected_matter_declaration_outcome(selected_matter, {}),
        "expected_selected_matter_declaration_outcome": (
            EXPECTED_SELECTED_MATTER_DECLARATION_OUTCOME
        ),
        "eligibility_basis": basis,
        "operation_candidate": _deepcopy(
            basis_mapping.get("operation_candidate")
            or selected_matter.get("operation_candidate")
        ),
        "operation_matter": _deepcopy(
            basis_mapping.get("operation_matter")
            or selected_matter.get("operation_matter")
        ),
        "operation_purpose": _deepcopy(
            basis_mapping.get("operation_purpose")
            or selected_matter.get("operation_purpose")
        ),
        "proposed_operation_kind": basis_mapping.get("proposed_operation_kind")
        or _proposed_operation_kind({}, selected_matter),
        "selected_operation_basis": _deepcopy(
            basis_mapping.get("selected_operation_basis")
            or selected_matter.get("selected_operation_basis")
            or basis
        ),
        "selected_carrier_context": _deepcopy(
            basis_mapping.get("selected_carrier_context")
            or selected_matter.get("selected_carrier_context")
        ),
        "proposed_affected_surfaces": _deepcopy(
            basis_mapping.get("proposed_affected_surfaces")
            or selected_matter.get("proposed_affected_surfaces")
        ),
        "proposed_output_family": _deepcopy(
            basis_mapping.get("proposed_output_family")
            or selected_matter.get("proposed_output_family")
        ),
        "eligibility_review_request": _deepcopy(
            basis_mapping.get("eligibility_review_request")
            or selected_matter.get("eligibility_review_request")
        ),
        "refusal_abort_awareness": _deepcopy(
            basis_mapping.get("refusal_abort_awareness")
            or selected_matter.get("refusal_abort_awareness")
        ),
        "current_body_conformance_v4_closure_basis": _deepcopy(
            basis_mapping.get("current_body_conformance_v4_closure_basis")
        ),
        "current_self_orientation_v9_basis": _deepcopy(
            basis_mapping.get("current_self_orientation_v9_basis")
        ),
        "distributed_standing_basis": _deepcopy(
            basis_mapping.get("distributed_standing_basis")
        ),
        "source_body_basis": _deepcopy(basis_mapping.get("source_body_basis")),
        "requested_eligibility_outcome": requested_eligibility_outcome,
        "declared_non_claims": _result_non_claims(),
    }
    if selected_matter_declaration_path is not None:
        request["selected_matter_declaration_path"] = selected_matter_declaration_path
    if additional_basis_context is not None:
        request["additional_basis_context"] = _deepcopy(additional_basis_context)
    if not_eligible_reason is not None:
        request["not_eligible_reason"] = not_eligible_reason
    return request
