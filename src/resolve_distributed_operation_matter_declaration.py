"""Bounded distributed operation matter declaration resolver.

This resolver records one declared distributed operation candidate as one
bounded matter for possible future eligibility review. It does not decide
eligibility, admit operation, authorize operation, execute operation,
synchronize repositories, transfer the full body, create a second body,
authorize continuation, create consequence, create public readiness, schedule
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


class DistributedOperationMatterDeclarationError(Exception):
    """Hard failure for impossible matter declaration write or shape errors."""


REPO_ROOT = Path(__file__).resolve().parents[1]
DISTRIBUTED_OPERATION_MATTER_DECLARATION_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_distributed_operation_matter_declaration"
)

RESOLVER_MODULE = "resolve_distributed_operation_matter_declaration"
RESULT_TYPE = "distributed_operation_matter_declaration_result"
RESULT_VERSION = "0.1.0"

OUTCOME_DECLARED = "DISTRIBUTED_OPERATION_MATTER_DECLARED"
OUTCOME_NOT_DECLARED = "DISTRIBUTED_OPERATION_MATTER_NOT_DECLARED"
OUTCOME_BLOCKED = "DISTRIBUTED_OPERATION_MATTER_DECLARATION_BLOCKED"
SUPPORTED_OUTCOMES = {
    OUTCOME_DECLARED,
    OUTCOME_NOT_DECLARED,
    OUTCOME_BLOCKED,
}

INTENT_DECLARE = "DECLARE_DISTRIBUTED_OPERATION_MATTER"
INTENT_DO_NOT_DECLARE = "DO_NOT_DECLARE_DISTRIBUTED_OPERATION_MATTER"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_OPERATION_MATTER_DECLARATION"
SUPPORTED_INTENTS = {
    INTENT_DECLARE,
    INTENT_DO_NOT_DECLARE,
    INTENT_BLOCK,
}

SUPPORTED_PROPOSED_OPERATION_KINDS = {
    "DISTRIBUTED_READINESS_REVIEW_CANDIDATE",
    "DISTRIBUTED_ARTIFACT_RECEIPT_REVIEW_CANDIDATE",
    "DISTRIBUTED_CARRIER_STATUS_REVIEW_CANDIDATE",
    "DISTRIBUTED_BOUNDARY_CONFORMANCE_REVIEW_CANDIDATE",
    "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
}
BLOCKED_OPERATION_KIND = "DISTRIBUTED_OPERATION_KIND_UNSPECIFIED_BLOCKED"

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "operation_admitted": False,
    "operation_authorized": False,
    "operation_executed": False,
    "eligibility_decided": False,
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

COLLAPSE_FIELDS: tuple[tuple[str, str], ...] = (
    ("operation_admitted", "DECLARATION_ADMITS_OPERATION"),
    ("declaration_admits_operation", "DECLARATION_ADMITS_OPERATION"),
    ("eligibility_decided", "DECLARATION_ADMITS_OPERATION"),
    ("operation_authorized", "DECLARATION_AUTHORIZES_OPERATION"),
    ("declaration_authorizes_operation", "DECLARATION_AUTHORIZES_OPERATION"),
    ("declaration_authorized_operation", "DECLARATION_AUTHORIZES_OPERATION"),
    ("distributed_operation_authorized", "DECLARATION_AUTHORIZES_OPERATION"),
    ("operation_executed", "DECLARATION_EXECUTES_OPERATION"),
    ("declaration_executes_operation", "DECLARATION_EXECUTES_OPERATION"),
    ("declaration_executed_operation", "DECLARATION_EXECUTES_OPERATION"),
    (
        "repository_synchronization_authorized",
        "DECLARATION_AUTHORIZES_REPOSITORY_SYNC",
    ),
    ("repository_sync_authorized", "DECLARATION_AUTHORIZES_REPOSITORY_SYNC"),
    ("declaration_authorizes_repository_sync", "DECLARATION_AUTHORIZES_REPOSITORY_SYNC"),
    ("full_body_transfer_authorized", "DECLARATION_AUTHORIZES_FULL_BODY_TRANSFER"),
    ("declaration_authorizes_full_body_transfer", "DECLARATION_AUTHORIZES_FULL_BODY_TRANSFER"),
    ("second_body_created", "DECLARATION_CREATES_SECOND_BODY"),
    ("declaration_creates_second_body", "DECLARATION_CREATES_SECOND_BODY"),
    ("continuation_authorized", "DECLARATION_AUTHORIZES_CONTINUATION"),
    ("declaration_authorizes_continuation", "DECLARATION_AUTHORIZES_CONTINUATION"),
    ("carrier_currentness_created", "DECLARATION_CREATES_CARRIER_CURRENTNESS"),
    ("declaration_creates_carrier_currentness", "DECLARATION_CREATES_CARRIER_CURRENTNESS"),
    ("current_carrier_selected", "DECLARATION_SELECTS_CURRENT_CARRIER"),
    ("declaration_selects_current_carrier", "DECLARATION_SELECTS_CURRENT_CARRIER"),
    ("winning_carrier_selected", "DECLARATION_SELECTS_WINNING_CARRIER"),
    ("declaration_selects_winning_carrier", "DECLARATION_SELECTS_WINNING_CARRIER"),
    ("losing_carrier_invalidated", "DECLARATION_INVALIDATES_LOSING_CARRIER"),
    ("declaration_invalidates_losing_carrier", "DECLARATION_INVALIDATES_LOSING_CARRIER"),
    ("source_replaced", "DECLARATION_REPLACES_SOURCE"),
    ("declaration_replaces_source", "DECLARATION_REPLACES_SOURCE"),
    ("authority_created", "DECLARATION_CREATES_AUTHORITY"),
    ("declaration_creates_authority", "DECLARATION_CREATES_AUTHORITY"),
    ("permission_created", "DECLARATION_CREATES_PERMISSION"),
    ("declaration_creates_permission", "DECLARATION_CREATES_PERMISSION"),
    ("truth_created", "DECLARATION_CREATES_TRUTH_OR_ACTION"),
    ("action_authorized", "DECLARATION_CREATES_TRUTH_OR_ACTION"),
    ("declaration_creates_truth", "DECLARATION_CREATES_TRUTH_OR_ACTION"),
    ("declaration_authorizes_action", "DECLARATION_CREATES_TRUTH_OR_ACTION"),
    ("consequence_created", "DECLARATION_CREATES_CONSEQUENCE"),
    ("declaration_creates_consequence", "DECLARATION_CREATES_CONSEQUENCE"),
    ("divergence_resolved", "DECLARATION_RESOLVES_DIVERGENCE"),
    ("declaration_resolves_divergence", "DECLARATION_RESOLVES_DIVERGENCE"),
    ("evidence_erased", "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL"),
    ("refusal_erased", "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL"),
    ("blocked_attempt_erased", "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL"),
    ("projection_mismatch_hidden", "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL"),
    ("declaration_erases_evidence", "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL"),
    ("declaration_erases_refusal", "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL"),
    ("public_launch_readiness_created", "DECLARATION_CREATES_PUBLIC_READINESS"),
    ("public_readiness_created", "DECLARATION_CREATES_PUBLIC_READINESS"),
    ("declaration_creates_public_readiness", "DECLARATION_CREATES_PUBLIC_READINESS"),
    ("final_completion_claimed", "DECLARATION_CLAIMS_FINAL_COMPLETION"),
    ("final_governance_completed", "DECLARATION_CLAIMS_FINAL_COMPLETION"),
    ("final_continuity_completed", "DECLARATION_CLAIMS_FINAL_COMPLETION"),
    ("final_system_identity_completed", "DECLARATION_CLAIMS_FINAL_COMPLETION"),
    ("declaration_claims_final_completion", "DECLARATION_CLAIMS_FINAL_COMPLETION"),
    ("follow_on_work_authorized", "DECLARATION_SCHEDULES_FOLLOW_ON_WORK"),
    ("declaration_schedules_follow_on_work", "DECLARATION_SCHEDULES_FOLLOW_ON_WORK"),
    ("self_orientation_successor_scheduled", "DECLARATION_SCHEDULES_FOLLOW_ON_WORK"),
)

WHAT_REMAINS_OPEN = {
    "distributed_operation_eligibility_boundary": (
        "open_not_scheduled_not_authorized_not_executed"
    ),
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
    if isinstance(value, Mapping) or isinstance(value, Sequence):
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


def _iter_mappings(value: Any, depth: int = 0) -> Sequence[Mapping[str, Any]]:
    if depth > 5:
        return []
    found: list[Mapping[str, Any]] = []
    if isinstance(value, Mapping):
        found.append(value)
        for child in value.values():
            found.extend(_iter_mappings(child, depth + 1))
    elif isinstance(value, Sequence) and not _is_text(value):
        for child in value:
            found.extend(_iter_mappings(child, depth + 1))
    return found


def _field_true(request: Mapping[str, Any], field: str) -> bool:
    return any(container.get(field) is True for container in _iter_mappings(request))


def _any_field_true(request: Mapping[str, Any], fields: Sequence[str]) -> bool:
    return any(_field_true(request, field) for field in fields)


def _first_true_field_code(request: Mapping[str, Any]) -> str | None:
    if any(
        _field_true(request, field)
        for field in ("mutation_performed", "replay_performed", "merge_performed")
    ):
        return "MUTATION_REPLAY_OR_MERGE_DETECTED"
    for field, code in COLLAPSE_FIELDS:
        if _field_true(request, field):
            return code
    return None


def _all_required_non_claims_false(non_claims: Any) -> bool:
    return isinstance(non_claims, Mapping) and all(
        non_claims.get(key) is False for key in REQUIRED_NON_CLAIMS
    )


def _result_non_claims() -> dict[str, bool]:
    return dict(REQUIRED_NON_CLAIMS)


def _operation_candidate_id(request: Mapping[str, Any]) -> Any:
    candidate = request.get("operation_candidate")
    if isinstance(candidate, Mapping):
        return (
            request.get("operation_candidate_id")
            or candidate.get("operation_candidate_id")
            or candidate.get("candidate_id")
            or candidate.get("id")
        )
    if isinstance(candidate, str):
        return candidate
    return request.get("operation_candidate_id")


def _operation_matter_id(request: Mapping[str, Any]) -> Any:
    matter = request.get("operation_matter")
    if isinstance(matter, Mapping):
        return (
            request.get("operation_matter_id")
            or matter.get("operation_matter_id")
            or matter.get("matter_id")
            or matter.get("id")
        )
    if isinstance(matter, str):
        return matter
    return request.get("operation_matter_id")


def _operation_question(request: Mapping[str, Any]) -> Any:
    candidate = _as_mapping(request.get("operation_candidate"))
    matter = _as_mapping(request.get("operation_matter"))
    return (
        request.get("operation_question")
        or candidate.get("operation_question")
        or candidate.get("declared_operation_question")
        or candidate.get("requested_operation_question")
        or matter.get("operation_question")
        or matter.get("declared_operation_question")
    )


def _operation_purpose_value(request: Mapping[str, Any]) -> Any:
    purpose = request.get("operation_purpose")
    if isinstance(purpose, Mapping):
        return (
            purpose.get("declared_operation_purpose")
            or purpose.get("operation_purpose")
            or purpose.get("purpose")
            or purpose
        )
    return purpose


def _selected_operation_basis_mapping(request: Mapping[str, Any]) -> Mapping[str, Any]:
    return _as_mapping(request.get("selected_operation_basis"))


def _source_body_basis(request: Mapping[str, Any]) -> Any:
    basis = _selected_operation_basis_mapping(request)
    return (
        request.get("source_body_basis")
        or basis.get("source_body_basis")
        or basis.get("selected_source_body_basis")
        or basis.get("source_body_lineage")
    )


def _current_body_orientation_conformance_basis(request: Mapping[str, Any]) -> Any:
    basis = _selected_operation_basis_mapping(request)
    return (
        request.get("current_body_conformance_v4_closure_basis")
        or request.get("current_self_orientation_v9_basis")
        or basis.get("current_body_orientation_conformance_basis")
        or basis.get("selected_current_body_orientation_conformance_basis")
        or basis.get("current_body_conformance_v4_closure_basis")
        or basis.get("current_self_orientation_v9_basis")
    )


def _distributed_or_v4_closure_basis(request: Mapping[str, Any]) -> Any:
    basis = _selected_operation_basis_mapping(request)
    return (
        request.get("distributed_standing_basis")
        or request.get("current_body_conformance_v4_closure_basis")
        or basis.get("distributed_standing_basis")
        or basis.get("selected_distributed_standing_basis")
        or basis.get("current_body_conformance_v4_closure_basis")
        or basis.get("distributed_standing_or_v4_closure_basis")
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
    block_code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": None if passed else block_code,
    }


def _matter_declaration_non_meaning() -> dict[str, bool]:
    non_meaning = {
        "operation_eligible": True,
        "operation_admitted": True,
        "operation_authorized": True,
        "operation_executed": True,
        "operation_conformed": True,
        "operation_closed": True,
        "repository_synchronization": True,
        "full_body_transfer": True,
        "second_body": True,
        "continuation": True,
        "distributed_operation": True,
        "carrier_currentness": True,
        "current_carrier_selected": True,
        "winning_carrier_selected": True,
        "losing_carrier_invalidated": True,
        "source_replacement": True,
        "authority": True,
        "permission": True,
        "truth": True,
        "action": True,
        "consequence": True,
        "divergence_resolution": True,
        "evidence_erasure": True,
        "public_launch_readiness": True,
        "final_completion": True,
        "final_governance": True,
        "final_continuity_completion": True,
        "final_system_identity": True,
        "follow_on_work_authorization": True,
        "current_self_orientation_v10": True,
    }
    for key in tuple(non_meaning):
        non_meaning[f"does_not_mean_{key}"] = True
    return non_meaning


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    result_source = (
        request.get("matter_declaration_request_id")
        or _operation_matter_id(request)
        or _operation_candidate_id(request)
        or "undeclared"
    )
    return {
        "distributed_operation_matter_declaration_result_id": (
            f"{result_source}__distributed_operation_matter_declaration_result"
        ),
        "distributed_operation_matter_declaration_result_type": RESULT_TYPE,
        "distributed_operation_matter_declaration_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _declared_matter_question(
    request: Mapping[str, Any],
    request_path: str | None = None,
) -> dict[str, Any]:
    return {
        "matter_declaration_request_id": request.get("matter_declaration_request_id"),
        "matter_declaration_question": request.get("matter_declaration_question"),
        "matter_declaration_intent": request.get("matter_declaration_intent"),
        "declared_non_claims": _deepcopy(request.get("declared_non_claims")),
        "declared_matter_request_path": request_path
        or request.get("declared_matter_request_path"),
        "matter_declaration_is_not_eligibility": True,
        "matter_declaration_is_not_admission": True,
        "matter_declaration_is_not_operation": True,
        "matter_declaration_is_not_execution": True,
        "matter_declaration_is_not_synchronization": True,
        "matter_declaration_is_not_full_body_transfer": True,
        "matter_declaration_is_not_continuation": True,
        "matter_declaration_is_not_permission": True,
        "matter_declaration_does_not_mutate_upstream_artifacts": True,
    }


def _operation_candidate_section(request: Mapping[str, Any]) -> dict[str, Any]:
    candidate = request.get("operation_candidate")
    return {
        "operation_candidate": _deepcopy(candidate),
        "operation_candidate_id": _operation_candidate_id(request),
        "declared_operation_question": _operation_question(request),
        "candidate_visible_as_candidate_only": True,
        "candidate_not_admitted": True,
        "candidate_not_authorized": True,
        "candidate_not_executed": True,
        "candidate_not_eligible_by_declaration": True,
        "candidate_not_scheduled_for_operation": True,
    }


def _operation_matter_section(request: Mapping[str, Any]) -> dict[str, Any]:
    matter = request.get("operation_matter")
    return {
        "operation_matter": _deepcopy(matter),
        "operation_matter_id": _operation_matter_id(request),
        "operation_candidate_id": _operation_candidate_id(request),
        "declared_matter_question": request.get("matter_declaration_question"),
        "declared_matter_scope": _deepcopy(request.get("matter_scope")),
        "matter_is_one_bounded_matter_only": True,
        "matter_declaration_is_not_eligibility": True,
        "matter_declaration_is_not_admission": True,
        "matter_declaration_is_not_operation": True,
        "matter_declaration_is_not_execution": True,
        "matter_declaration_is_not_permission": True,
    }


def _operation_purpose_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "operation_purpose": _deepcopy(request.get("operation_purpose")),
        "declared_operation_purpose": _deepcopy(_operation_purpose_value(request)),
        "purpose_is_not_permission": True,
        "purpose_is_not_operation_plan": True,
        "purpose_is_not_output_authorization": True,
        "purpose_is_not_follow_on_work_authorization": True,
    }


def _proposed_operation_kind_section(request: Mapping[str, Any]) -> dict[str, Any]:
    kind = request.get("proposed_operation_kind")
    return {
        "proposed_operation_kind": kind,
        "selected_proposed_operation_kind": kind,
        "kind_supported": kind in SUPPORTED_PROPOSED_OPERATION_KINDS,
        "kind_is_candidate_kind_only": True,
        "kind_is_not_authorization": True,
        "kind_is_not_admission": True,
        "kind_is_not_execution": True,
        "kind_is_not_operation": True,
    }


def _selected_operation_basis_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "selected_operation_basis": _deepcopy(request.get("selected_operation_basis")),
        "selected_source_body_basis": _deepcopy(_source_body_basis(request)),
        "selected_current_body_orientation_conformance_basis": _deepcopy(
            _current_body_orientation_conformance_basis(request)
        ),
        "selected_distributed_standing_or_v4_closure_basis": _deepcopy(
            _distributed_or_v4_closure_basis(request)
        ),
        "source_body_basis": _deepcopy(request.get("source_body_basis")),
        "current_body_conformance_v4_closure_basis": _deepcopy(
            request.get("current_body_conformance_v4_closure_basis")
        ),
        "current_self_orientation_v9_basis": _deepcopy(
            request.get("current_self_orientation_v9_basis")
        ),
        "distributed_standing_basis": _deepcopy(request.get("distributed_standing_basis")),
        "reference_grounding": _deepcopy(request.get("reference_grounding")),
        "read_only_reference_grounding": _deepcopy(request.get("reference_grounding")),
        "basis_is_not_permission_set": True,
        "basis_is_not_operation_plan": True,
        "basis_is_not_synchronization_plan": True,
        "basis_is_not_full_body_transfer_plan": True,
        "basis_is_not_final_governance": True,
    }


def _selected_carrier_context_section(request: Mapping[str, Any]) -> dict[str, Any]:
    context = request.get("selected_carrier_context")
    return {
        "selected_carrier_context": _deepcopy(context),
        "selected_carrier_context_supplied": context is not None,
        "selected_carrier_context_preserved": context is not None
        and _carrier_context_parseable(context),
        "carrier_b_success_as_evidence_context_only": True,
        "carrier_c_block_as_evidence_context_only": True,
        "b_c_divergence_as_visible_context_only": True,
        "refusal_and_blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible_where_supplied": True,
        "selected_carriers_are_context_not_operational_participants": True,
        "no_current_carrier_selected": True,
        "no_winning_carrier_selected": True,
        "no_losing_carrier_invalidated": True,
        "no_carrier_currentness_created": True,
    }


def _proposed_affected_surfaces_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "proposed_affected_surfaces": _deepcopy(request.get("proposed_affected_surfaces")),
        "declared_affected_surfaces": _deepcopy(request.get("proposed_affected_surfaces")),
        "affected_surfaces_are_proposed_only": True,
        "no_surface_is_mutated": True,
        "no_surface_is_synchronized": True,
        "no_surface_is_transferred": True,
        "no_surface_is_executed": True,
        "no_output_is_emitted_by_declaration": True,
    }


def _proposed_output_family_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "proposed_output_family": _deepcopy(request.get("proposed_output_family")),
        "declared_proposed_output_family": _deepcopy(request.get("proposed_output_family")),
        "output_family_is_named_only": True,
        "output_family_is_not_authorized": True,
        "output_family_is_not_emitted": True,
        "output_family_does_not_create_consequence": True,
        "output_family_does_not_authorize_future_outputs": True,
    }


def _eligibility_review_request_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "eligibility_review_request": _deepcopy(request.get("eligibility_review_request")),
        "request_for_future_eligibility_review": _non_empty(
            request.get("eligibility_review_request")
        ),
        "eligibility_is_not_decided": True,
        "eligibility_review_is_not_scheduled": True,
        "eligibility_review_is_not_authorized_by_declaration": True,
        "eligibility_boundary_remains_open": True,
        "declaration_is_only_prerequisite_visibility": True,
    }


def _awareness_declared(value: Any, token: str) -> bool:
    if isinstance(value, Mapping):
        return any(
            value.get(key) is True
            for key in (
                token,
                f"awareness_{token}",
                f"awareness_that_{token}",
                f"declared_awareness_{token}",
                f"declared_awareness_that_{token}",
            )
        )
    if isinstance(value, Sequence) and not _is_text(value):
        normalized = " ".join(str(item).lower() for item in value)
        return token.replace("_", " ") in normalized
    if isinstance(value, str):
        return token.replace("_", " ") in value.lower()
    return False


def _refusal_abort_awareness_section(request: Mapping[str, Any]) -> dict[str, Any]:
    awareness = request.get("refusal_abort_awareness")
    present = _non_empty(awareness)
    return {
        "refusal_abort_awareness": _deepcopy(awareness),
        "awareness_that_operation_may_later_be_blocked": present
        and (
            _awareness_declared(awareness, "operation_may_later_be_blocked")
            or _awareness_declared(awareness, "operation_may_be_blocked")
            or not isinstance(awareness, Mapping)
        ),
        "awareness_that_eligibility_may_fail": present
        and (
            _awareness_declared(awareness, "eligibility_may_fail")
            or not isinstance(awareness, Mapping)
        ),
        "awareness_that_carrier_refusal_must_remain_visible": present
        and (
            _awareness_declared(awareness, "carrier_refusal_must_remain_visible")
            or not isinstance(awareness, Mapping)
        ),
        "awareness_that_operation_admission_must_include_abort_refusal_conditions": present
        and (
            _awareness_declared(
                awareness,
                "operation_admission_must_include_abort_refusal_conditions",
            )
            or _awareness_declared(awareness, "admission_must_include_abort_refusal")
            or not isinstance(awareness, Mapping)
        ),
        "awareness_that_no_operation_may_proceed_without_later_refusal_abort_boundary": present
        and (
            _awareness_declared(
                awareness,
                "no_operation_may_proceed_without_later_refusal_abort_boundary",
            )
            or not isinstance(awareness, Mapping)
        ),
        "awareness_that_abort_refusal_is_part_of_operation_law": present
        and (
            _awareness_declared(awareness, "abort_refusal_is_part_of_operation_law")
            or not isinstance(awareness, Mapping)
        ),
        "refusal_abort_awareness_is_not_abort_mechanism_by_itself": True,
        "refusal_abort_awareness_is_not_admission": True,
        "refusal_abort_awareness_is_not_operation": True,
    }


def _checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    intent = request.get("matter_declaration_intent")
    kind = request.get("proposed_operation_kind")
    carrier_context = request.get("selected_carrier_context")
    checks: list[dict[str, Any]] = [
        _make_check(
            "matter declaration question declared",
            bool(request.get("matter_declaration_question")),
            "declared matter declaration question",
            request.get("matter_declaration_question"),
            "MATTER_DECLARATION_QUESTION_UNDECLARED",
        ),
        _make_check(
            "matter declaration intent supported",
            intent in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            intent,
            "MATTER_DECLARATION_INTENT_UNSUPPORTED",
        ),
        _make_check(
            "operation candidate id present",
            bool(_operation_candidate_id(request)),
            "operation candidate id",
            _operation_candidate_id(request),
            "OPERATION_CANDIDATE_ID_MISSING",
        ),
        _make_check(
            "operation matter id present",
            bool(_operation_matter_id(request)),
            "operation matter id",
            _operation_matter_id(request),
            "OPERATION_MATTER_ID_MISSING",
        ),
        _make_check(
            "operation question present",
            bool(_operation_question(request)),
            "declared operation question",
            _operation_question(request),
            "OPERATION_QUESTION_MISSING",
        ),
        _make_check(
            "operation purpose present",
            _non_empty(_operation_purpose_value(request)),
            "declared operation purpose",
            _operation_purpose_value(request),
            "OPERATION_PURPOSE_MISSING",
        ),
        _make_check(
            "proposed operation kind supported",
            kind in SUPPORTED_PROPOSED_OPERATION_KINDS,
            sorted(SUPPORTED_PROPOSED_OPERATION_KINDS),
            kind,
            "OPERATION_KIND_UNSUPPORTED",
        ),
        _make_check(
            "source-body basis present",
            _non_empty(_source_body_basis(request)),
            "selected source-body basis",
            _source_body_basis(request),
            "SOURCE_BODY_BASIS_MISSING",
        ),
        _make_check(
            "current body orientation conformance basis present",
            _non_empty(_current_body_orientation_conformance_basis(request)),
            "selected current body orientation/conformance basis",
            _current_body_orientation_conformance_basis(request),
            "CURRENT_BODY_ORIENTATION_CONFORMANCE_BASIS_MISSING",
        ),
        _make_check(
            "distributed standing or v4 closure basis present where claimed",
            _non_empty(_distributed_or_v4_closure_basis(request)),
            "selected distributed standing or v4 closure basis",
            _distributed_or_v4_closure_basis(request),
            "DISTRIBUTED_STANDING_OR_V4_CLOSURE_BASIS_MISSING",
        ),
        _make_check(
            "selected carrier context parseable where supplied",
            _carrier_context_parseable(carrier_context),
            "mapping or bounded sequence when supplied",
            "not supplied" if carrier_context is None else type(carrier_context).__name__,
            "SELECTED_CARRIER_CONTEXT_MALFORMED",
        ),
        _make_check(
            "proposed affected surfaces present",
            _non_empty(request.get("proposed_affected_surfaces")),
            "declared proposed affected surfaces",
            request.get("proposed_affected_surfaces"),
            "PROPOSED_AFFECTED_SURFACES_MISSING",
        ),
        _make_check(
            "proposed output family present",
            _non_empty(request.get("proposed_output_family")),
            "declared proposed output family",
            request.get("proposed_output_family"),
            "PROPOSED_OUTPUT_FAMILY_MISSING",
        ),
        _make_check(
            "eligibility review request present",
            _non_empty(request.get("eligibility_review_request")),
            "requested future eligibility review",
            request.get("eligibility_review_request"),
            "ELIGIBILITY_REVIEW_REQUEST_MISSING",
        ),
        _make_check(
            "refusal abort awareness present",
            _non_empty(request.get("refusal_abort_awareness")),
            "declared refusal/abort awareness",
            request.get("refusal_abort_awareness"),
            "REFUSAL_ABORT_AWARENESS_MISSING",
        ),
    ]

    for check_name, fields, code in (
        (
            "declaration does not admit operation",
            ("operation_admitted", "declaration_admits_operation"),
            "DECLARATION_ADMITS_OPERATION",
        ),
        (
            "declaration does not decide eligibility",
            ("eligibility_decided",),
            "DECLARATION_ADMITS_OPERATION",
        ),
        (
            "declaration does not authorize operation",
            (
                "operation_authorized",
                "distributed_operation_authorized",
                "declaration_authorizes_operation",
                "declaration_authorized_operation",
            ),
            "DECLARATION_AUTHORIZES_OPERATION",
        ),
        (
            "declaration does not execute operation",
            ("operation_executed", "declaration_executes_operation", "declaration_executed_operation"),
            "DECLARATION_EXECUTES_OPERATION",
        ),
        (
            "declaration does not authorize repository synchronization",
            (
                "repository_synchronization_authorized",
                "repository_sync_authorized",
                "declaration_authorizes_repository_sync",
            ),
            "DECLARATION_AUTHORIZES_REPOSITORY_SYNC",
        ),
        (
            "declaration does not authorize full body transfer",
            ("full_body_transfer_authorized", "declaration_authorizes_full_body_transfer"),
            "DECLARATION_AUTHORIZES_FULL_BODY_TRANSFER",
        ),
        (
            "declaration does not create second body",
            ("second_body_created", "declaration_creates_second_body"),
            "DECLARATION_CREATES_SECOND_BODY",
        ),
        (
            "declaration does not authorize continuation",
            ("continuation_authorized", "declaration_authorizes_continuation"),
            "DECLARATION_AUTHORIZES_CONTINUATION",
        ),
        (
            "declaration does not create carrier currentness",
            ("carrier_currentness_created", "declaration_creates_carrier_currentness"),
            "DECLARATION_CREATES_CARRIER_CURRENTNESS",
        ),
        (
            "declaration does not select current carrier",
            ("current_carrier_selected", "declaration_selects_current_carrier"),
            "DECLARATION_SELECTS_CURRENT_CARRIER",
        ),
        (
            "declaration does not select winning carrier",
            ("winning_carrier_selected", "declaration_selects_winning_carrier"),
            "DECLARATION_SELECTS_WINNING_CARRIER",
        ),
        (
            "declaration does not invalidate losing carrier",
            ("losing_carrier_invalidated", "declaration_invalidates_losing_carrier"),
            "DECLARATION_INVALIDATES_LOSING_CARRIER",
        ),
        (
            "declaration does not replace source",
            ("source_replaced", "declaration_replaces_source"),
            "DECLARATION_REPLACES_SOURCE",
        ),
        (
            "declaration does not create authority",
            ("authority_created", "declaration_creates_authority"),
            "DECLARATION_CREATES_AUTHORITY",
        ),
        (
            "declaration does not create permission",
            ("permission_created", "declaration_creates_permission"),
            "DECLARATION_CREATES_PERMISSION",
        ),
        (
            "declaration does not create truth",
            ("truth_created", "declaration_creates_truth"),
            "DECLARATION_CREATES_TRUTH_OR_ACTION",
        ),
        (
            "declaration does not authorize action",
            ("action_authorized", "declaration_authorizes_action"),
            "DECLARATION_CREATES_TRUTH_OR_ACTION",
        ),
        (
            "declaration does not create consequence",
            ("consequence_created", "declaration_creates_consequence"),
            "DECLARATION_CREATES_CONSEQUENCE",
        ),
        (
            "declaration does not resolve divergence",
            ("divergence_resolved", "declaration_resolves_divergence"),
            "DECLARATION_RESOLVES_DIVERGENCE",
        ),
        (
            "declaration does not erase evidence",
            ("evidence_erased", "declaration_erases_evidence"),
            "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL",
        ),
        (
            "declaration does not erase refusal",
            ("refusal_erased", "declaration_erases_refusal"),
            "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL",
        ),
        (
            "declaration does not create public readiness",
            (
                "public_launch_readiness_created",
                "public_readiness_created",
                "declaration_creates_public_readiness",
            ),
            "DECLARATION_CREATES_PUBLIC_READINESS",
        ),
        (
            "declaration does not claim final completion",
            (
                "final_completion_claimed",
                "final_governance_completed",
                "final_continuity_completed",
                "final_system_identity_completed",
                "declaration_claims_final_completion",
            ),
            "DECLARATION_CLAIMS_FINAL_COMPLETION",
        ),
        (
            "declaration does not schedule follow-on work",
            ("follow_on_work_authorized", "declaration_schedules_follow_on_work"),
            "DECLARATION_SCHEDULES_FOLLOW_ON_WORK",
        ),
        (
            "declaration does not schedule self-orientation successor",
            ("self_orientation_successor_scheduled",),
            "DECLARATION_SCHEDULES_FOLLOW_ON_WORK",
        ),
    ):
        actual = _any_field_true(request, fields)
        checks.append(_make_check(check_name, not actual, False, actual, code))

    mutation_detected = any(
        _field_true(request, field)
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
            "non-claims remain false",
            _all_required_non_claims_false(request.get("declared_non_claims")),
            REQUIRED_NON_CLAIMS,
            _deepcopy(request.get("declared_non_claims")),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True and check.get("block_code"):
            return str(check["block_code"])
    return None


def _statement_for(
    outcome: str,
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    declared = outcome == OUTCOME_DECLARED
    statement = {
        "distributed_operation_matter_declared": declared,
        "operation_candidate_preserved": _operation_candidate_id(request) is not None,
        "operation_matter_preserved": _operation_matter_id(request) is not None,
        "operation_purpose_preserved": _non_empty(_operation_purpose_value(request)),
        "proposed_operation_kind_preserved": request.get("proposed_operation_kind")
        in SUPPORTED_PROPOSED_OPERATION_KINDS,
        "selected_operation_basis_preserved": _non_empty(
            request.get("selected_operation_basis")
        ),
        "selected_carrier_context_preserved": request.get("selected_carrier_context")
        is not None
        and _carrier_context_parseable(request.get("selected_carrier_context")),
        "proposed_affected_surfaces_preserved": _non_empty(
            request.get("proposed_affected_surfaces")
        ),
        "proposed_output_family_preserved": _non_empty(
            request.get("proposed_output_family")
        ),
        "eligibility_review_request_preserved": _non_empty(
            request.get("eligibility_review_request")
        ),
        "refusal_abort_awareness_preserved": _non_empty(
            request.get("refusal_abort_awareness")
        ),
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "eligibility_decided": False,
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
        "upstream_artifacts_not_mutated": True,
        "failed_check_count": failed_count,
    }
    if outcome == OUTCOME_NOT_DECLARED:
        statement["not_declared_reason"] = request.get(
            "not_declared_reason",
            "Matter declaration request did not declare the matter.",
        )
    if outcome == OUTCOME_BLOCKED:
        statement["distributed_operation_matter_declared"] = False
    return statement


def _block(outcome: str, code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {
        "blocked": outcome == OUTCOME_BLOCKED,
        "block_code": code if outcome == OUTCOME_BLOCKED else None,
        "block_reason": reason if outcome == OUTCOME_BLOCKED else None,
    }


def _base_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None = None,
    block_reason: str | None = None,
    request_path: str | None = None,
) -> dict[str, Any]:
    result = {
        "distributed_operation_matter_declaration_metadata": _metadata(request),
        "declared_matter_question": _declared_matter_question(request, request_path),
        "operation_candidate": _operation_candidate_section(request),
        "operation_matter": _operation_matter_section(request),
        "operation_purpose": _operation_purpose_section(request),
        "proposed_operation_kind": _proposed_operation_kind_section(request),
        "selected_operation_basis": _selected_operation_basis_section(request),
        "selected_carrier_context": _selected_carrier_context_section(request),
        "proposed_affected_surfaces": _proposed_affected_surfaces_section(request),
        "proposed_output_family": _proposed_output_family_section(request),
        "eligibility_review_request": _eligibility_review_request_section(request),
        "refusal_abort_awareness": _refusal_abort_awareness_section(request),
        "matter_declaration_checks": list(checks),
        "matter_declaration_statement": _statement_for(outcome, request, checks),
        "matter_declaration_non_meaning": _matter_declaration_non_meaning(),
        "what_remains_open": _deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": _result_non_claims(),
        "outcome": outcome,
        "block": _block(outcome, block_code, block_reason),
    }
    result["distributed_operation_matter_declaration_summary"] = (
        build_distributed_operation_matter_declaration_summary(result)
    )
    return result


def _blocked_result(
    request: Mapping[str, Any] | None,
    code: str,
    reason: str,
    request_path: str | None = None,
) -> dict[str, Any]:
    clean_request = _deepcopy(dict(request)) if isinstance(request, Mapping) else {}
    checks = [
        _make_check(
            "matter declaration blocked",
            False,
            "lawful bounded matter declaration request",
            reason,
            code,
        )
    ]
    return _base_result(
        clean_request,
        OUTCOME_BLOCKED,
        checks,
        code,
        reason,
        request_path,
    )


def resolve_distributed_operation_matter_declaration(
    declared_matter_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one distributed operation matter declaration request."""

    if declared_matter_request is None:
        return _blocked_result(
            {},
            "MATTER_DECLARATION_QUESTION_UNDECLARED",
            "No declared matter declaration request was supplied.",
        )
    if not isinstance(declared_matter_request, Mapping):
        return _blocked_result(
            {},
            "DECLARED_MATTER_DECLARATION_REQUEST_MALFORMED",
            "Declared matter declaration request must be a mapping.",
        )

    request: dict[str, Any] = _deepcopy(dict(declared_matter_request))
    if not request.get("matter_declaration_question"):
        return _blocked_result(
            request,
            "MATTER_DECLARATION_QUESTION_UNDECLARED",
            "Matter declaration question is undeclared.",
            request.get("declared_matter_request_path"),
        )

    intent = request.get("matter_declaration_intent")
    if intent == INTENT_BLOCK:
        return _blocked_result(
            request,
            "MATTER_DECLARATION_REQUEST_EXPLICITLY_BLOCKED",
            request.get("block_reason") or "Matter declaration request explicitly blocked.",
            request.get("declared_matter_request_path"),
        )
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(
            request,
            "MATTER_DECLARATION_INTENT_UNSUPPORTED",
            "Matter declaration intent is unsupported.",
            request.get("declared_matter_request_path"),
        )

    checks = _checks(request)
    failed_code = _first_failed_code(checks)
    collapse_code = _first_true_field_code(request)
    block_code = collapse_code or failed_code

    if block_code:
        return _base_result(
            request,
            OUTCOME_BLOCKED,
            checks,
            block_code,
            request.get("block_reason") or block_code,
            request.get("declared_matter_request_path"),
        )

    explicitly_not_declared = (
        intent == INTENT_DO_NOT_DECLARE
        or request.get("matter_declared") is False
        or request.get("declare_matter") is False
    )
    if explicitly_not_declared:
        return _base_result(
            request,
            OUTCOME_NOT_DECLARED,
            checks,
            request_path=request.get("declared_matter_request_path"),
        )

    return _base_result(
        request,
        OUTCOME_DECLARED,
        checks,
        request_path=request.get("declared_matter_request_path"),
    )


def resolve_distributed_operation_matter_declaration_from_path(
    declared_matter_request_path: Path | str,
) -> dict:
    """Load a declared matter request JSON object and resolve it."""

    path = _to_path(declared_matter_request_path)
    parsed, error = _read_json_object(path)
    if error == "unreadable":
        return _blocked_result(
            {},
            "DECLARED_MATTER_DECLARATION_REQUEST_UNREADABLE",
            "Declared matter declaration request path is unreadable.",
            str(path),
        )
    if error == "malformed":
        return _blocked_result(
            {},
            "DECLARED_MATTER_DECLARATION_REQUEST_MALFORMED",
            "Declared matter declaration request JSON must be an object.",
            str(path),
        )
    request = _deepcopy(parsed)
    request["declared_matter_request_path"] = str(path)
    result = resolve_distributed_operation_matter_declaration(request)
    result["declared_matter_question"]["declared_matter_request_path"] = str(path)
    result["distributed_operation_matter_declaration_summary"] = (
        build_distributed_operation_matter_declaration_summary(result)
    )
    return result


def build_distributed_operation_matter_declaration_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded summary for a matter declaration result artifact."""

    checks = result.get("matter_declaration_checks")
    if not isinstance(checks, Sequence) or _is_text(checks):
        checks = []
    passed = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True)
    failed = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is not True)
    declared = _as_mapping(result.get("declared_matter_question"))
    candidate = _as_mapping(result.get("operation_candidate"))
    matter = _as_mapping(result.get("operation_matter"))
    purpose = _as_mapping(result.get("operation_purpose"))
    kind = _as_mapping(result.get("proposed_operation_kind"))
    statement = _as_mapping(result.get("matter_declaration_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "matter_declaration_request_id": declared.get("matter_declaration_request_id"),
        "matter_declaration_question": declared.get("matter_declaration_question"),
        "matter_declaration_intent": declared.get("matter_declaration_intent"),
        "operation_candidate_id": candidate.get("operation_candidate_id"),
        "operation_matter_id": matter.get("operation_matter_id"),
        "operation_question": candidate.get("declared_operation_question"),
        "operation_purpose": purpose.get("declared_operation_purpose"),
        "proposed_operation_kind": kind.get("proposed_operation_kind"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "distributed_operation_matter_declared": statement.get(
            "distributed_operation_matter_declared",
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
        "selected_carrier_context_preserved": statement.get(
            "selected_carrier_context_preserved",
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
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "eligibility_decided": False,
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
                "eligibility_decided",
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
    text = str(value or "distributed_operation_matter_declaration")
    safe = []
    for char in text:
        safe.append(char if char.isalnum() or char in {"-", "_"} else "_")
    return "".join(safe).strip("_") or "distributed_operation_matter_declaration"


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


def write_distributed_operation_matter_declaration_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a matter declaration result as additive UTF-8 JSON."""

    if not isinstance(result, Mapping):
        raise DistributedOperationMatterDeclarationError("result must be a mapping")
    if output_path is None:
        summary = _as_mapping(result.get("distributed_operation_matter_declaration_summary"))
        request_id = summary.get("matter_declaration_request_id") or summary.get(
            "operation_matter_id"
        )
        filename = (
            f"{_safe_filename_part(request_id)}"
            "__distributed_operation_matter_declaration_result.json"
        )
        output = DISTRIBUTED_OPERATION_MATTER_DECLARATION_ROOT / filename
    else:
        output = Path(output_path)
    output = _non_overwriting_path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return output


def build_declared_distributed_operation_matter_request(
    matter_declaration_request_id: str,
    matter_declaration_question: str,
    operation_candidate: Mapping[str, Any],
    operation_matter: Mapping[str, Any],
    operation_purpose: Mapping[str, Any] | str,
    proposed_operation_kind: str,
    selected_operation_basis: Mapping[str, Any] | str,
    proposed_affected_surfaces: Sequence[str] | Mapping[str, Any],
    proposed_output_family: Sequence[str] | Mapping[str, Any],
    eligibility_review_request: Mapping[str, Any] | str,
    refusal_abort_awareness: Mapping[str, Any] | Sequence[str],
    matter_declaration_intent: str = INTENT_DECLARE,
    *,
    selected_carrier_context: Sequence[Mapping[str, Any]] | Mapping[str, Any] | None = None,
) -> dict:
    """Build a bounded declared matter request with required non-claims false."""

    selected_basis = _deepcopy(selected_operation_basis)
    basis_mapping = selected_basis if isinstance(selected_basis, Mapping) else {}
    request = {
        "matter_declaration_request_id": matter_declaration_request_id,
        "matter_declaration_question": matter_declaration_question,
        "matter_declaration_intent": matter_declaration_intent,
        "operation_candidate": _deepcopy(operation_candidate),
        "operation_matter": _deepcopy(operation_matter),
        "operation_question": _get_nested(
            operation_candidate,
            (
                ("operation_question",),
                ("declared_operation_question",),
                ("requested_operation_question",),
            ),
        )
        or matter_declaration_question,
        "operation_purpose": _deepcopy(operation_purpose),
        "proposed_operation_kind": proposed_operation_kind,
        "selected_operation_basis": selected_basis,
        "source_body_basis": _deepcopy(
            basis_mapping.get("source_body_basis", selected_operation_basis)
        ),
        "current_body_conformance_v4_closure_basis": _deepcopy(
            basis_mapping.get(
                "current_body_conformance_v4_closure_basis",
                selected_operation_basis,
            )
        ),
        "distributed_standing_basis": _deepcopy(
            basis_mapping.get("distributed_standing_basis", selected_operation_basis)
        ),
        "proposed_affected_surfaces": _deepcopy(proposed_affected_surfaces),
        "proposed_output_family": _deepcopy(proposed_output_family),
        "eligibility_review_request": _deepcopy(eligibility_review_request),
        "refusal_abort_awareness": _deepcopy(refusal_abort_awareness),
        "declared_non_claims": _result_non_claims(),
    }
    if selected_carrier_context is not None:
        request["selected_carrier_context"] = _deepcopy(selected_carrier_context)
    return request
