"""Bounded cross-carrier currentness successor boundary resolver.

This resolver records how body-side current posture may account for selected
plural carrier evidence without making any carrier current. It preserves
visible refusal, visible divergence, blocked attempts, projection mismatch,
detailed basis over shallow summary, and explicit non-claims.

It does not create carrier currentness, select a current carrier, select a
winning carrier, invalidate a losing carrier, replace source, create authority,
create permission, create carrier hierarchy, resolve divergence, erase
evidence, create distributed standing, synchronize repositories, authorize full
body transfer, create a second body, authorize continuation, or authorize
distributed operation.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CrossCarrierCurrentnessSuccessorBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit successor inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


REPO_ROOT = Path(__file__).resolve().parents[1]

CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_cross_carrier_currentness_successor_boundary"
)

RESOLVER_MODULE = "resolve_cross_carrier_currentness_successor_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "cross_carrier_currentness_successor_boundary_result"

RECORD_INTENT = "RECORD_CROSS_CARRIER_CURRENTNESS_SUCCESSOR"
DO_NOT_RECORD_INTENT = "DO_NOT_RECORD_CROSS_CARRIER_CURRENTNESS_SUCCESSOR"
BLOCK_INTENT = "BLOCK_CROSS_CARRIER_CURRENTNESS_SUCCESSOR"
SUPPORTED_CURRENTNESS_SUCCESSOR_INTENTS = {
    RECORD_INTENT,
    DO_NOT_RECORD_INTENT,
    BLOCK_INTENT,
}

CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED = (
    "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED"
)
CROSS_CARRIER_CURRENTNESS_SUCCESSOR_NOT_RECORDED = (
    "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_NOT_RECORDED"
)
CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED = (
    "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED"
)

SUPPORTED_CURRENTNESS_SUCCESSOR_POSTURES = {
    "BODY_CURRENT_POSTURE_ACCOUNTED_FOR_CARRIER_EVIDENCE",
    "CARRIER_EVIDENCE_CURRENTNESS_RELEVANT",
    "CARRIER_EVIDENCE_CURRENTNESS_NOT_RELEVANT",
    "CARRIER_EVIDENCE_CURRENTNESS_EXCLUDED",
    "VISIBLE_DIVERGENCE_REQUIRES_CURRENTNESS_CAUTION",
    "VISIBLE_REFUSAL_REQUIRES_CURRENTNESS_CAUTION",
    "CURRENTNESS_SUCCESSOR_NOT_RECORDED",
    "CURRENTNESS_SUCCESSOR_BLOCKED",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "carrier_currentness_created": False,
    "source_replaced": False,
    "current_carrier_selected": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "currentness_successor_created_source": False,
    "currentness_successor_created_authority": False,
    "currentness_successor_created_permission": False,
    "currentness_successor_created_carrier_hierarchy": False,
    "currentness_successor_created_distributed_standing": False,
    "currentness_successor_resolved_divergence": False,
    "currentness_successor_erased_evidence": False,
    "currentness_successor_hid_refusal": False,
    "currentness_successor_hid_divergence": False,
    "currentness_successor_hid_blocked_attempt": False,
    "currentness_successor_hid_projection_mismatch": False,
    "summary_overrode_detailed_basis": False,
    "latest_file_currentness": False,
    "latest_turn_currentness": False,
    "majority_carrier_currentness": False,
    "successful_receipt_count_currentness": False,
    "registry_record_currentness": False,
    "lifecycle_status_currentness": False,
    "standing_propagation_currentness": False,
    "continuity_turn_currentness": False,
    "repository_synchronization_authorized": False,
    "full_body_transfer_authorized": False,
    "second_body_created": False,
    "continuation_authorized": False,
    "distributed_operation_authorized": False,
    "distributed_standing_created": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "DECLARED_CURRENTNESS_SUCCESSOR_REQUEST_UNREADABLE": "Declared currentness successor request path could not be read.",
    "DECLARED_CURRENTNESS_SUCCESSOR_REQUEST_MALFORMED": "Declared currentness successor request is not a JSON object or mapping.",
    "CURRENTNESS_SUCCESSOR_REQUEST_EXPLICITLY_BLOCKED": "Currentness successor request explicitly declares a blocked posture.",
    "CURRENTNESS_SUCCESSOR_QUESTION_UNDECLARED": "Currentness successor question is undeclared.",
    "CURRENTNESS_SUCCESSOR_INTENT_UNSUPPORTED": "Currentness successor intent is unsupported.",
    "CURRENTNESS_SUCCESSOR_POSTURE_UNSUPPORTED": "Requested currentness successor posture is missing or unsupported.",
    "BODY_CURRENT_POSTURE_MISSING": "Selected body-side current posture is missing.",
    "SELECTED_CARRIER_EVIDENCE_MISSING": "Selected carrier evidence is missing.",
    "SELECTED_CARRIER_EVIDENCE_MALFORMED": "Selected carrier evidence is malformed.",
    "SELECTED_CARRIER_EVIDENCE_IDENTITY_MISSING": "Selected carrier evidence identity is missing.",
    "SELECTED_CARRIER_EVIDENCE_OUTCOME_MISSING": "Selected carrier evidence outcome is missing.",
    "CURRENTNESS_SUCCESSOR_BASIS_MISSING": "Currentness successor basis is missing.",
    "PRIOR_CURRENTNESS_PARTICIPATION_BASIS_MISSING": "Prior currentness participation basis is missing where required.",
    "CARRIER_CONTINUITY_TURN_BASIS_MISSING": "Carrier continuity-turn basis is missing where required.",
    "LIFECYCLE_REGISTRY_PROPAGATION_BASIS_MISSING": "Lifecycle, registry/persistence, or standing propagation basis is missing where required.",
    "CURRENTNESS_SUCCESSOR_HIDES_REFUSAL": "Currentness successor hides visible refusal.",
    "CURRENTNESS_SUCCESSOR_HIDES_DIVERGENCE": "Currentness successor hides visible divergence.",
    "CURRENTNESS_SUCCESSOR_HIDES_BLOCKED_ATTEMPT": "Currentness successor hides a blocked attempt.",
    "CURRENTNESS_SUCCESSOR_HIDES_PROJECTION_MISMATCH": "Currentness successor hides projection mismatch.",
    "SUMMARY_OVERWRITES_DETAILED_BASIS": "Summary projection overwrites detailed basis.",
    "CURRENTNESS_SUCCESSOR_CREATES_CARRIER_CURRENTNESS": "Currentness successor creates carrier currentness.",
    "CURRENTNESS_SUCCESSOR_SELECTS_CURRENT_CARRIER": "Currentness successor selects a current carrier.",
    "CURRENTNESS_SUCCESSOR_SELECTS_WINNING_CARRIER": "Currentness successor selects a winning carrier.",
    "CURRENTNESS_SUCCESSOR_INVALIDATES_LOSING_CARRIER": "Currentness successor invalidates a losing carrier.",
    "CURRENTNESS_SUCCESSOR_REPLACES_SOURCE": "Currentness successor replaces source.",
    "CURRENTNESS_SUCCESSOR_CREATES_AUTHORITY": "Currentness successor creates authority.",
    "CURRENTNESS_SUCCESSOR_CREATES_PERMISSION": "Currentness successor creates permission.",
    "CURRENTNESS_SUCCESSOR_CREATES_CARRIER_HIERARCHY": "Currentness successor creates carrier hierarchy.",
    "CURRENTNESS_SUCCESSOR_RESOLVES_DIVERGENCE": "Currentness successor resolves divergence.",
    "CURRENTNESS_SUCCESSOR_ERASES_EVIDENCE": "Currentness successor erases evidence.",
    "CURRENTNESS_SUCCESSOR_CREATES_DISTRIBUTED_STANDING": "Currentness successor creates distributed standing.",
    "CURRENTNESS_SUCCESSOR_AUTHORIZES_REPOSITORY_SYNC": "Currentness successor authorizes repository synchronization.",
    "CURRENTNESS_SUCCESSOR_AUTHORIZES_FULL_BODY_TRANSFER": "Currentness successor authorizes full body transfer.",
    "CURRENTNESS_SUCCESSOR_CREATES_SECOND_BODY": "Currentness successor creates a second body.",
    "CURRENTNESS_SUCCESSOR_AUTHORIZES_CONTINUATION": "Currentness successor authorizes continuation.",
    "CURRENTNESS_SUCCESSOR_AUTHORIZES_DISTRIBUTED_OPERATION": "Currentness successor authorizes distributed operation.",
    "LATEST_FILE_CURRENTNESS": "Latest-file recency is treated as currentness.",
    "LATEST_TURN_CURRENTNESS": "Latest turn is treated as currentness.",
    "MAJORITY_OR_SUCCESS_COUNT_CURRENTNESS": "Majority or successful receipt count is treated as currentness.",
    "REGISTRY_LIFECYCLE_PROPAGATION_OR_TURN_CURRENTNESS": "Registry, lifecycle, standing propagation, or continuity-turn posture is treated as currentness.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge was detected.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required currentness successor non-claim is missing or flipped.",
}

CURRENTNESS_SUCCESSOR_NON_MEANING = {
    "does_not_mean_carrier_currentness": True,
    "does_not_mean_current_carrier_selected": True,
    "does_not_mean_winning_carrier_selected": True,
    "does_not_mean_losing_carrier_invalidated": True,
    "does_not_mean_source_replacement": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_distributed_standing": True,
    "does_not_mean_distributed_currentness": True,
    "does_not_mean_carrier_hierarchy": True,
    "does_not_mean_carrier_priority": True,
    "does_not_mean_carrier_sovereignty": True,
    "does_not_mean_divergence_resolved": True,
    "does_not_mean_refusal_erased": True,
    "does_not_mean_evidence_erased": True,
    "does_not_mean_standing_on_carrier": True,
    "does_not_mean_registry_currentness": True,
    "does_not_mean_lifecycle_currentness": True,
    "does_not_mean_propagation_currentness": True,
    "does_not_mean_continuity_turn_currentness": True,
    "does_not_mean_latest_file_currentness": True,
    "does_not_mean_latest_turn_currentness": True,
    "does_not_mean_majority_currentness": True,
    "does_not_mean_success_count_currentness": True,
    "does_not_mean_availability_currentness": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_continuation": True,
    "does_not_mean_distributed_operation": True,
    "does_not_mean_truth": True,
    "does_not_mean_action": True,
    "does_not_mean_consequence": True,
}

WHAT_REMAINS_OPEN = {
    "cross_carrier_currentness_successor_implementation_refinement": True,
    "divergence_consequence_law": True,
    "distributed_standing_boundary": True,
    "distributed_standing": True,
    "carrier_registry_implementation": True,
    "persistence_implementation": True,
    "standing_propagation_implementation_beyond_boundary_recording": True,
    "carrier_continuity_turn_implementation_refinement": True,
    "presence_law": True,
    "threshold_law": True,
    "truth_law": True,
    "action_consequence_law": True,
    "generalized_vessel_relation_lifecycle": True,
    "body_relevance_medium": True,
    "signal_series_or_accumulation_logic": True,
    "successor_carrier_law": True,
    "future_self_orientation_successor_only_if_separately_justified": True,
    "distributed_operation_only_if_separately_declared_and_bounded": True,
    "open_means_not_scheduled": True,
    "open_means_not_authorized": True,
    "open_means_not_executed": True,
}


def resolve_cross_carrier_currentness_successor_boundary(
    declared_currentness_successor_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded cross-carrier currentness successor request."""

    if declared_currentness_successor_request is None:
        return _resolve_currentness_successor({}, None, [])
    if not isinstance(declared_currentness_successor_request, Mapping):
        return _resolve_currentness_successor(
            {},
            None,
            ["DECLARED_CURRENTNESS_SUCCESSOR_REQUEST_MALFORMED"],
        )
    return _resolve_currentness_successor(
        copy.deepcopy(dict(declared_currentness_successor_request)),
        None,
        [],
    )


def resolve_cross_carrier_currentness_successor_boundary_from_path(
    declared_currentness_successor_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one bounded cross-carrier currentness successor request from JSON."""

    path = Path(declared_currentness_successor_request_path)
    try:
        request = _read_json_mapping(path)
    except CrossCarrierCurrentnessSuccessorBoundaryError as exc:
        return _resolve_currentness_successor({}, path, [exc.block_code])
    return _resolve_currentness_successor(request, path, [])


def write_cross_carrier_currentness_successor_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an additive currentness successor result without overwriting."""

    if not isinstance(result, Mapping):
        raise CrossCarrierCurrentnessSuccessorBoundaryError(
            "DECLARED_CURRENTNESS_SUCCESSOR_REQUEST_MALFORMED",
            "Cross-carrier currentness successor result must be a mapping.",
        )

    if output_path is None:
        summary = _as_mapping(
            result.get("cross_carrier_currentness_successor_summary")
        )
        basis_id = (
            summary.get("currentness_successor_request_id")
            or summary.get("requested_currentness_successor_posture")
            or "cross_carrier_currentness_successor"
        )
        output_path = CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BOUNDARY_ROOT / (
            f"{_safe_filename_part(basis_id)}__cross_carrier_currentness_successor_result.json"
        )

    target = _non_overwriting_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, ensure_ascii=False, default=str)
        + "\n",
        encoding="utf-8",
    )
    return target


def build_cross_carrier_currentness_successor_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary from the full result body."""

    checks = _mapping_list(result.get("currentness_successor_checks"))
    question = _as_mapping(result.get("declared_currentness_successor_question"))
    body_posture = _as_mapping(result.get("selected_body_current_posture"))
    evidence = _as_mapping(result.get("selected_carrier_evidence"))
    posture = _as_mapping(result.get("currentness_successor_posture"))
    accounting = _as_mapping(result.get("evidence_accounting"))
    statement = _as_mapping(result.get("currentness_successor_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "currentness_successor_request_id": question.get(
            "currentness_successor_request_id"
        ),
        "currentness_successor_question": question.get(
            "currentness_successor_question"
        ),
        "currentness_successor_intent": question.get(
            "currentness_successor_intent"
        ),
        "requested_currentness_successor_posture": posture.get(
            "requested_currentness_successor_posture"
        ),
        "selected_body_current_posture_id": body_posture.get(
            "selected_body_current_posture_id"
        ),
        "selected_body_current_posture_outcome": body_posture.get(
            "selected_body_current_posture_outcome"
        ),
        "selected_carrier_evidence_ids": evidence.get(
            "selected_carrier_evidence_ids"
        ),
        "selected_carrier_evidence_outcomes": evidence.get(
            "selected_carrier_evidence_outcomes"
        ),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "cross_carrier_currentness_successor_recorded": bool(
            statement.get("cross_carrier_currentness_successor_recorded")
        ),
        "evidence_accounting_preserved": bool(
            statement.get("evidence_accounting_preserved")
        ),
        "visible_refusal_preserved": bool(
            statement.get("visible_refusal_preserved")
        ),
        "visible_divergence_preserved": bool(
            statement.get("visible_divergence_preserved")
        ),
        "blocked_attempts_preserved": bool(
            statement.get("blocked_attempts_preserved")
        ),
        "projection_mismatch_preserved": bool(
            statement.get("projection_mismatch_preserved")
        ),
        "prior_currentness_participation_basis_preserved": bool(
            statement.get("prior_currentness_participation_basis_preserved")
        ),
        "lifecycle_basis_preserved": bool(
            statement.get("lifecycle_basis_preserved")
        ),
        "registry_persistence_basis_preserved": bool(
            statement.get("registry_persistence_basis_preserved")
        ),
        "standing_propagation_basis_preserved": bool(
            statement.get("standing_propagation_basis_preserved")
        ),
        "carrier_continuity_turn_basis_preserved": bool(
            statement.get("carrier_continuity_turn_basis_preserved")
        ),
        "relation_conformance_closure_basis_preserved": bool(
            statement.get("relation_conformance_closure_basis_preserved")
        ),
        "detailed_basis_distinguished_from_summary": bool(
            statement.get("detailed_basis_distinguished_from_summary")
        ),
        "summary_overrode_detailed_basis": bool(
            statement.get("summary_overrode_detailed_basis")
        ),
        "carrier_currentness_created": bool(
            statement.get("carrier_currentness_created")
        ),
        "current_carrier_selected": bool(
            statement.get("current_carrier_selected")
        ),
        "winning_carrier_selected": bool(
            statement.get("winning_carrier_selected")
        ),
        "losing_carrier_invalidated": bool(
            statement.get("losing_carrier_invalidated")
        ),
        "no_source_currentness_authority_permission": not bool(
            statement.get("source_replaced")
            or statement.get("currentness_created")
            or statement.get("authority_created")
            or statement.get("permission_created")
        ),
        "no_carrier_hierarchy": not bool(statement.get("carrier_hierarchy_created")),
        "no_divergence_resolution": not bool(statement.get("divergence_resolved")),
        "no_evidence_erasure": not bool(statement.get("evidence_erased")),
        "no_distributed_standing": not bool(
            statement.get("distributed_standing_created")
        ),
        "no_sync_full_body_transfer_second_body": not bool(
            statement.get("repository_synchronization_authorized")
            or statement.get("full_body_transfer_authorized")
            or statement.get("second_body_created")
        ),
        "no_continuation": not bool(statement.get("continuation_authorized")),
        "no_distributed_operation": not bool(
            statement.get("distributed_operation_authorized")
        ),
        "no_latest_file_turn_currentness": not bool(
            statement.get("latest_file_currentness")
            or statement.get("latest_turn_currentness")
        ),
        "no_majority_success_count_currentness": not bool(
            statement.get("majority_carrier_currentness")
            or statement.get("successful_receipt_count_currentness")
        ),
        "evidence_accounting": accounting.get("raw_evidence_accounting"),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_declared_cross_carrier_currentness_successor_request(
    currentness_successor_request_id: str,
    currentness_successor_question: str,
    selected_body_current_posture: Mapping[str, Any],
    selected_carrier_evidence: Sequence[Mapping[str, Any]],
    requested_currentness_successor_posture: str,
    currentness_successor_basis: Mapping[str, Any] | str,
    currentness_successor_intent: str = RECORD_INTENT,
    *,
    prior_currentness_participation_basis: Mapping[str, Any] | str | None = None,
    lifecycle_basis: Mapping[str, Any] | str | None = None,
    registry_persistence_basis: Mapping[str, Any] | str | None = None,
    standing_propagation_basis: Mapping[str, Any] | str | None = None,
    carrier_continuity_turn_basis: Mapping[str, Any] | str | None = None,
    relation_conformance_closure_basis: Mapping[str, Any] | str | None = None,
    evidence_accounting: Sequence[Mapping[str, Any]] | Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build one bounded currentness successor request without inferring force."""

    evidence_items = [
        copy.deepcopy(dict(item))
        for item in selected_carrier_evidence
        if isinstance(item, Mapping)
    ]
    if evidence_accounting is None:
        accounting: list[dict[str, Any]] | dict[str, Any] = [
            {
                "carrier_evidence_id": _extract_identity(item),
                "carrier_evidence_outcome": _entry_outcome(item),
                "accounting_posture": requested_currentness_successor_posture,
                "evidence_remains_evidence": True,
                "carrier_evidence_does_not_become_currentness": True,
            }
            for item in evidence_items
        ]
    else:
        accounting = copy.deepcopy(evidence_accounting)

    request: dict[str, Any] = {
        "currentness_successor_request_id": currentness_successor_request_id,
        "currentness_successor_question": currentness_successor_question,
        "currentness_successor_intent": currentness_successor_intent,
        "selected_body_current_posture": copy.deepcopy(
            dict(selected_body_current_posture)
        ),
        "selected_carrier_evidence": evidence_items,
        "requested_currentness_successor_posture": requested_currentness_successor_posture,
        "currentness_successor_basis": copy.deepcopy(currentness_successor_basis),
        "evidence_accounting": accounting,
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }
    optional_sections = {
        "prior_currentness_participation_basis": prior_currentness_participation_basis,
        "lifecycle_basis": lifecycle_basis,
        "registry_persistence_basis": registry_persistence_basis,
        "standing_propagation_basis": standing_propagation_basis,
        "carrier_continuity_turn_basis": carrier_continuity_turn_basis,
        "relation_conformance_closure_basis": relation_conformance_closure_basis,
    }
    for key, value in optional_sections.items():
        if value is not None:
            request[key] = copy.deepcopy(value)
    return request


def _resolve_currentness_successor(
    request: Mapping[str, Any],
    request_path: Path | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    normalized_request = _as_mapping(request)
    question = _declared_currentness_successor_question(
        normalized_request,
        request_path,
    )
    body_posture = _selected_body_current_posture_section(normalized_request)
    carrier_evidence = _selected_carrier_evidence_section(normalized_request)
    posture = _currentness_successor_posture_section(normalized_request)
    successor_basis = _currentness_successor_basis_section(normalized_request)
    prior_participation = _optional_basis_section(
        normalized_request,
        "prior_currentness_participation_basis",
        "prior_currentness_participation_basis",
        "prior_currentness_participation_basis_required",
    )
    lifecycle_basis = _optional_basis_section(
        normalized_request,
        "lifecycle_basis",
        "lifecycle_basis",
        "lifecycle_basis_required",
    )
    registry_basis = _optional_basis_section(
        normalized_request,
        "registry_persistence_basis",
        "registry_persistence_basis",
        "registry_persistence_basis_required",
    )
    standing_basis = _optional_basis_section(
        normalized_request,
        "standing_propagation_basis",
        "standing_propagation_basis",
        "standing_propagation_basis_required",
    )
    continuity_basis = _optional_basis_section(
        normalized_request,
        "carrier_continuity_turn_basis",
        "carrier_continuity_turn_basis",
        "carrier_continuity_turn_basis_required",
    )
    relation_closure_basis = _optional_basis_section(
        normalized_request,
        "relation_conformance_closure_basis",
        "relation_conformance_closure_basis",
        "relation_conformance_closure_basis_required",
    )
    evidence_accounting = _evidence_accounting_section(
        normalized_request,
        carrier_evidence,
    )
    non_claims = _non_claims_section(normalized_request, question)
    visibility = _visibility_projection(
        normalized_request,
        successor_basis,
        carrier_evidence,
        evidence_accounting,
        prior_participation,
        lifecycle_basis,
        registry_basis,
        standing_basis,
        continuity_basis,
        relation_closure_basis,
        non_claims,
    )
    checks = _build_checks(
        normalized_request,
        question,
        body_posture,
        carrier_evidence,
        posture,
        successor_basis,
        prior_participation,
        lifecycle_basis,
        registry_basis,
        standing_basis,
        continuity_basis,
        relation_closure_basis,
        evidence_accounting,
        non_claims,
        visibility,
        precheck_failures,
    )

    failed_checks = [check for check in checks if check.get("passed") is False]
    explicit_block_code = "CURRENTNESS_SUCCESSOR_REQUEST_EXPLICITLY_BLOCKED"
    if failed_checks:
        outcome = CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED
        block_code = failed_checks[0].get("block_code")
    elif question.get("currentness_successor_intent") == BLOCK_INTENT:
        outcome = CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED
        block_code = explicit_block_code
    elif question.get("currentness_successor_intent") == DO_NOT_RECORD_INTENT:
        outcome = CROSS_CARRIER_CURRENTNESS_SUCCESSOR_NOT_RECORDED
        block_code = None
    else:
        outcome = CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED
        block_code = None

    block = {
        "blocked": outcome == CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED,
        "code": block_code,
        "reason": _block_reason(block_code),
        "block_code": block_code,
        "block_reason": _block_reason(block_code),
    }
    statement = _currentness_successor_statement(
        outcome,
        question,
        body_posture,
        carrier_evidence,
        posture,
        successor_basis,
        prior_participation,
        lifecycle_basis,
        registry_basis,
        standing_basis,
        continuity_basis,
        relation_closure_basis,
        evidence_accounting,
        visibility,
        block,
    )
    result: dict[str, Any] = {
        "cross_carrier_currentness_successor_metadata": _metadata(
            question,
            posture,
            outcome,
        ),
        "declared_currentness_successor_question": question,
        "selected_body_current_posture": body_posture,
        "selected_carrier_evidence": carrier_evidence,
        "prior_currentness_participation_basis": prior_participation,
        "lifecycle_basis": lifecycle_basis,
        "registry_persistence_basis": registry_basis,
        "standing_propagation_basis": standing_basis,
        "carrier_continuity_turn_basis": continuity_basis,
        "relation_conformance_closure_basis": relation_closure_basis,
        "currentness_successor_posture": posture,
        "evidence_accounting": evidence_accounting,
        "currentness_successor_checks": checks,
        "currentness_successor_statement": statement,
        "currentness_successor_non_meaning": copy.deepcopy(
            CURRENTNESS_SUCCESSOR_NON_MEANING
        ),
        "what_remains_open": copy.deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    result["cross_carrier_currentness_successor_summary"] = (
        build_cross_carrier_currentness_successor_summary(result)
    )
    return result


def _declared_currentness_successor_question(
    request: Mapping[str, Any],
    request_path: Path | None,
) -> dict[str, Any]:
    section = _as_mapping(request.get("declared_currentness_successor_question"))
    raw_intent = (
        request.get("currentness_successor_intent")
        or section.get("currentness_successor_intent")
    )
    intent = _normalize_token(raw_intent)
    declared_non_claims = _as_mapping(
        request.get("declared_non_claims")
        or request.get("non_claims")
        or section.get("declared_non_claims")
    )
    return {
        "currentness_successor_request_id": request.get(
            "currentness_successor_request_id"
        )
        or section.get("currentness_successor_request_id"),
        "currentness_successor_question": request.get(
            "currentness_successor_question"
        )
        or section.get("currentness_successor_question"),
        "currentness_successor_intent": intent,
        "raw_currentness_successor_intent": raw_intent,
        "request_path": _display_path(request_path) or section.get("request_path"),
        "not_recorded_reason": request.get("not_recorded_reason")
        or section.get("not_recorded_reason")
        or (
            "declared request does not record cross-carrier currentness successor posture"
            if intent == DO_NOT_RECORD_INTENT
            else None
        ),
        "declared_non_claims": declared_non_claims,
        "currentness_successor_is_not_distributed_standing": True,
        "currentness_participation_is_not_currentness": True,
        "carrier_evidence_does_not_become_current": True,
        "plural_carrier_evidence_is_not_majority_currentness": True,
        "successful_receipt_is_not_currentness": True,
        "blocked_receipt_is_not_exclusion_by_default": True,
        "registry_presence_is_not_currentness": True,
        "lifecycle_status_is_not_currentness": True,
        "standing_propagation_is_not_currentness": True,
        "continuity_turn_lineage_is_not_currentness": True,
    }


def _selected_body_current_posture_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("selected_body_current_posture")
    declared = raw is not None
    parseable = isinstance(raw, Mapping) or isinstance(raw, str)
    posture_id = _extract_identity(raw)
    posture_outcome = _field_from_mapping(
        raw,
        (
            "selected_body_current_posture_outcome",
            "body_current_posture_outcome",
            "current_posture_outcome",
            "result_outcome",
            "outcome",
            "status",
        ),
    )
    posture_kind = _field_from_mapping(
        raw,
        (
            "selected_body_current_posture",
            "body_current_posture",
            "current_posture",
            "posture",
            "type",
        ),
    )
    if isinstance(raw, str) and not posture_id:
        posture_id = raw
        posture_kind = raw
    return {
        "selected_body_current_posture_declared": declared,
        "selected_body_current_posture_parseable": parseable if declared else False,
        "selected_body_current_posture_id": posture_id,
        "selected_body_current_posture_outcome": posture_outcome,
        "selected_body_current_posture_kind": posture_kind,
        "raw_selected_body_current_posture": copy.deepcopy(raw),
        "body_current_posture_preserved": declared and parseable,
        "body_current_posture_is_body_side": True,
        "body_current_posture_is_not_carrier_currentness": True,
    }


def _selected_carrier_evidence_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("selected_carrier_evidence")
    declared = raw is not None
    if isinstance(raw, Mapping):
        entries = _entries_from_value(raw.get("selected_carrier_evidence_entries"))
        if not entries:
            entries = _entries_from_value(raw.get("evidence"))
        if not entries:
            entries = [_as_mapping(raw)]
        parseable = True
    elif isinstance(raw, Sequence) and not isinstance(raw, (str, bytes, bytearray)):
        entries = _entries_from_value(raw)
        parseable = True
    else:
        entries = []
        parseable = False if declared else False

    evidence_ids = [_extract_identity(entry) for entry in entries]
    evidence_outcomes = [_entry_outcome(entry) for entry in entries]
    return {
        "selected_carrier_evidence_declared": declared,
        "selected_carrier_evidence_parseable": parseable,
        "selected_carrier_evidence_entries": entries,
        "selected_carrier_evidence_count": len(entries),
        "selected_carrier_evidence_ids": [value for value in evidence_ids if value],
        "selected_carrier_evidence_outcomes": [
            value for value in evidence_outcomes if value
        ],
        "selected_carrier_evidence_identities_preserved": bool(entries)
        and all(_nonempty(value) for value in evidence_ids),
        "selected_carrier_evidence_outcomes_preserved": bool(entries)
        and all(_nonempty(value) for value in evidence_outcomes),
        "raw_selected_carrier_evidence": copy.deepcopy(raw),
        "selected_carrier_evidence_preserved": bool(entries)
        and all(_nonempty(value) for value in evidence_ids)
        and all(_nonempty(value) for value in evidence_outcomes),
        "carrier_evidence_remains_evidence": True,
        "carrier_evidence_is_not_currentness": True,
        "carrier_evidence_does_not_select_carrier": True,
    }


def _currentness_successor_posture_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = (
        request.get("requested_currentness_successor_posture")
        or _field_from_mapping(
            request.get("currentness_successor_posture"),
            (
                "requested_currentness_successor_posture",
                "currentness_successor_posture",
                "posture",
            ),
        )
    )
    posture = _normalize_token(raw)
    return {
        "requested_currentness_successor_posture": posture,
        "raw_requested_currentness_successor_posture": raw,
        "currentness_successor_posture_supported": posture
        in SUPPORTED_CURRENTNESS_SUCCESSOR_POSTURES,
        "supported_currentness_successor_postures": sorted(
            SUPPORTED_CURRENTNESS_SUCCESSOR_POSTURES
        ),
        "currentness_successor_posture_preserved": posture
        in SUPPORTED_CURRENTNESS_SUCCESSOR_POSTURES,
        "posture_is_body_side_accounting_not_carrier_currentness": True,
    }


def _currentness_successor_basis_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("currentness_successor_basis")
    raw_mapping = _as_mapping(raw)
    return {
        "currentness_successor_basis_declared": _basis_declared(raw),
        "currentness_successor_basis_preserved": _basis_declared(raw),
        "currentness_successor_basis_id": _extract_identity(raw),
        "raw_currentness_successor_basis": copy.deepcopy(raw),
        "detailed_basis_reference": _first_declared(
            request.get("detailed_basis_reference"),
            raw_mapping.get("detailed_basis_reference"),
            raw_mapping.get("detailed_basis_path_or_section"),
        ),
        "summary_projection_reference": _first_declared(
            request.get("summary_projection_reference"),
            raw_mapping.get("summary_projection_reference"),
            raw_mapping.get("summary_projection_path_or_section"),
        ),
        "currentness_successor_basis_is_not_carrier_currentness": True,
        "currentness_successor_basis_does_not_select_carrier": True,
        "currentness_successor_basis_does_not_authorize_continuation": True,
    }


def _optional_basis_section(
    request: Mapping[str, Any],
    key: str,
    section_name: str,
    required_key: str,
) -> dict[str, Any]:
    raw = request.get(key)
    nested = _as_mapping(request.get(section_name))
    if raw is None and nested:
        raw = nested.get(f"raw_{section_name}") or nested
    declared = _basis_declared(raw)
    required = bool(
        _is_true(request.get(required_key))
        or _is_true(nested.get("basis_required"))
        or _is_true(nested.get(required_key))
    )
    return {
        f"{section_name}_declared": declared,
        f"{section_name}_required": required,
        f"{section_name}_preserved": declared,
        f"{section_name}_id": _extract_identity(raw),
        f"raw_{section_name}": copy.deepcopy(raw),
        "basis_preserved_where_supplied": bool(not declared or _basis_declared(raw)),
        "basis_is_not_currentness": True,
        "basis_does_not_decide_currentness": True,
    }


def _evidence_accounting_section(
    request: Mapping[str, Any],
    carrier_evidence: Mapping[str, Any],
) -> dict[str, Any]:
    raw = request.get("evidence_accounting")
    entries = _entries_from_value(raw)
    raw_mapping = _as_mapping(raw)
    selected_ids = carrier_evidence.get("selected_carrier_evidence_ids") or []
    selected_outcomes = carrier_evidence.get("selected_carrier_evidence_outcomes") or []
    return {
        "evidence_accounting_declared": _basis_declared(raw),
        "evidence_accounting_preserved": _basis_declared(raw),
        "raw_evidence_accounting": copy.deepcopy(raw),
        "evidence_accounting_entries": entries,
        "accounted_carrier_evidence_ids": [
            _extract_identity(entry) for entry in entries if _extract_identity(entry)
        ],
        "selected_carrier_evidence_identities": copy.deepcopy(selected_ids),
        "selected_carrier_evidence_outcomes": copy.deepcopy(selected_outcomes),
        "carrier_b_successful_receipt_relevant_only_under_declared_basis": True,
        "carrier_c_blocked_receipt_caution_only_under_declared_basis": True,
        "bc_divergence_may_require_currentness_caution": True,
        "lifecycle_status_may_inform_but_not_decide_currentness": True,
        "registry_persistence_may_locate_but_not_decide_currentness": True,
        "standing_propagation_may_preserve_posture_but_not_decide_currentness": True,
        "continuity_turn_may_preserve_lineage_but_not_decide_currentness": True,
        "relation_conformance_closure_may_preserve_coherence_but_not_decide_currentness": True,
        "no_majority_success_count_latest_currentness": not _recursive_true(
            [raw, raw_mapping],
            (
                "majority_carrier_currentness",
                "successful_receipt_count_currentness",
                "latest_file_currentness",
                "latest_turn_currentness",
            ),
        ),
    }


def _non_claims_section(
    request: Mapping[str, Any],
    question: Mapping[str, Any],
) -> dict[str, Any]:
    declared = _as_mapping(
        request.get("declared_non_claims")
        or request.get("non_claims")
        or question.get("declared_non_claims")
    )
    non_claims = copy.deepcopy(REQUIRED_NON_CLAIMS)
    for key in REQUIRED_NON_CLAIMS:
        if key in declared:
            non_claims[key] = copy.deepcopy(declared[key])
    missing = [key for key in REQUIRED_NON_CLAIMS if key not in declared]
    flipped = [
        key
        for key, expected in REQUIRED_NON_CLAIMS.items()
        if key in declared and declared.get(key) is not expected
    ]
    non_claims["required_non_claims_preserved"] = not missing and not flipped
    non_claims["missing_required_non_claims"] = missing
    non_claims["flipped_required_non_claims"] = flipped
    return non_claims


def _visibility_projection(
    request: Mapping[str, Any],
    successor_basis: Mapping[str, Any],
    carrier_evidence: Mapping[str, Any],
    evidence_accounting: Mapping[str, Any],
    prior_participation: Mapping[str, Any],
    lifecycle_basis: Mapping[str, Any],
    registry_basis: Mapping[str, Any],
    standing_basis: Mapping[str, Any],
    continuity_basis: Mapping[str, Any],
    relation_closure_basis: Mapping[str, Any],
    non_claims: Mapping[str, Any],
) -> dict[str, bool]:
    evidence_entries = carrier_evidence.get("selected_carrier_evidence_entries") or []
    accounting_entries = evidence_accounting.get("evidence_accounting_entries") or []
    sources = [
        successor_basis.get("raw_currentness_successor_basis"),
        carrier_evidence.get("raw_selected_carrier_evidence"),
        evidence_accounting.get("raw_evidence_accounting"),
        prior_participation.get("raw_prior_currentness_participation_basis"),
        lifecycle_basis.get("raw_lifecycle_basis"),
        registry_basis.get("raw_registry_persistence_basis"),
        standing_basis.get("raw_standing_propagation_basis"),
        continuity_basis.get("raw_carrier_continuity_turn_basis"),
        relation_closure_basis.get("raw_relation_conformance_closure_basis"),
    ]

    refusal_hidden = _recursive_true(
        [request, non_claims],
        (
            "currentness_successor_hid_refusal",
            "currentness_successor_hides_refusal",
            "visible_refusal_hidden",
            "refusal_hidden",
            "hides_refusal",
        ),
    )
    refusal_applicable = bool(
        _basis_declared(request.get("visible_refusal_basis"))
        or _recursive_true(
            sources,
            (
                "visible_refusal_applicable",
                "visible_refusal_present",
                "visible_refusal_preserved",
                "refusal_applicable",
                "refusal_preserved",
            ),
        )
        or _entries_have_token(evidence_entries + accounting_entries, ("refusal", "refused", "blocked"))
    )
    refusal_preserved = bool(
        not refusal_hidden
        and (
            _basis_declared(request.get("visible_refusal_basis"))
            or _recursive_true(
                sources,
                (
                    "visible_refusal_preserved",
                    "refusal_preserved",
                    "refusal_remains_visible",
                ),
            )
            or _entries_have_token(evidence_entries + accounting_entries, ("refusal", "refused", "blocked"))
        )
    )

    divergence_hidden = _recursive_true(
        [request, non_claims],
        (
            "currentness_successor_hid_divergence",
            "currentness_successor_hides_divergence",
            "visible_divergence_hidden",
            "divergence_hidden",
            "hides_divergence",
        ),
    )
    divergence_applicable = bool(
        _basis_declared(request.get("visible_divergence_basis"))
        or _recursive_true(
            sources,
            (
                "visible_divergence_applicable",
                "visible_divergence_present",
                "visible_divergence_preserved",
                "divergence_applicable",
                "divergence_preserved",
            ),
        )
        or _entries_have_token(evidence_entries + accounting_entries, ("divergence", "mismatch"))
        or _entries_have_outcome(evidence_entries, ("CARRIER_DIVERGENCE_RECORDED",))
    )
    divergence_preserved = bool(
        not divergence_hidden
        and (
            _basis_declared(request.get("visible_divergence_basis"))
            or _recursive_true(
                sources,
                (
                    "visible_divergence_preserved",
                    "divergence_preserved",
                    "divergence_remains_visible",
                ),
            )
            or _entries_have_token(evidence_entries + accounting_entries, ("divergence", "mismatch"))
            or _entries_have_outcome(evidence_entries, ("CARRIER_DIVERGENCE_RECORDED",))
        )
    )

    blocked_hidden = _recursive_true(
        [request, non_claims],
        (
            "currentness_successor_hid_blocked_attempt",
            "currentness_successor_hides_blocked_attempt",
            "blocked_attempt_hidden",
            "blocked_attempts_hidden",
        ),
    )
    blocked_applicable = bool(
        _basis_declared(request.get("blocked_attempt_basis"))
        or _recursive_true(
            sources,
            (
                "blocked_attempt_applicable",
                "blocked_attempt_preserved",
                "blocked_attempts_preserved",
            ),
        )
        or _entries_have_token(evidence_entries + accounting_entries, ("blocked", "block", "failed"))
        or _entries_have_outcome(evidence_entries, ("BLOCKED",))
    )
    blocked_preserved = bool(
        not blocked_hidden
        and (
            _basis_declared(request.get("blocked_attempt_basis"))
            or _recursive_true(
                sources,
                (
                    "blocked_attempt_preserved",
                    "blocked_attempts_preserved",
                    "blocked_attempt_remains_visible",
                ),
            )
            or _entries_have_token(evidence_entries + accounting_entries, ("blocked", "block", "failed"))
            or _entries_have_outcome(evidence_entries, ("BLOCKED",))
        )
    )

    projection_hidden = _recursive_true(
        [request, non_claims],
        (
            "currentness_successor_hid_projection_mismatch",
            "currentness_successor_hides_projection_mismatch",
            "projection_mismatch_hidden",
            "hides_projection_mismatch",
        ),
    )
    projection_applicable = bool(
        _basis_declared(request.get("projection_mismatch_basis"))
        or _recursive_true(
            sources,
            (
                "projection_mismatch_applicable",
                "projection_mismatch_present",
                "projection_mismatch_detected",
                "projection_mismatch_visible",
                "summary_under_projected_detailed_basis",
            ),
        )
        or _entries_have_token(accounting_entries, ("projection_mismatch", "under_project", "under-project"))
    )
    projection_preserved = bool(
        not projection_hidden
        and (
            _basis_declared(request.get("projection_mismatch_basis"))
            or _recursive_true(
                sources,
                (
                    "projection_mismatch_visible",
                    "projection_mismatch_preserved",
                    "predecessor_projection_mismatch_visible",
                ),
            )
            or _entries_have_token(accounting_entries, ("projection_mismatch", "under_project", "under-project"))
        )
    )

    detailed_ref = successor_basis.get("detailed_basis_reference")
    summary_ref = successor_basis.get("summary_projection_reference")
    detailed_distinguished = bool(
        _recursive_true(
            sources,
            (
                "detailed_basis_distinguished_from_summary",
                "detailed_basis_distinguishable_from_summary",
            ),
        )
        or (_basis_declared(detailed_ref) and _basis_declared(summary_ref))
    )
    detailed_applicable = bool(
        _basis_declared(detailed_ref)
        or _basis_declared(summary_ref)
        or _recursive_true(
            sources,
            (
                "detailed_basis_distinguished_from_summary",
                "detailed_basis_distinguishable_from_summary",
                "detailed_basis_reference",
                "summary_projection_reference",
            ),
        )
    )
    summary_overrode = _recursive_true(
        [request, non_claims] + sources,
        (
            "summary_overrode_detailed_basis",
            "summary_overwrites_detailed_basis",
            "summary_projection_overrode_detailed_basis",
        ),
    )

    return {
        "visible_refusal_applicable": refusal_applicable,
        "visible_refusal_preserved": refusal_preserved,
        "visible_refusal_hidden": refusal_hidden,
        "visible_divergence_applicable": divergence_applicable,
        "visible_divergence_preserved": divergence_preserved,
        "visible_divergence_hidden": divergence_hidden,
        "blocked_attempts_applicable": blocked_applicable,
        "blocked_attempts_preserved": blocked_preserved,
        "blocked_attempt_hidden": blocked_hidden,
        "projection_mismatch_applicable": projection_applicable,
        "projection_mismatch_preserved": projection_preserved,
        "projection_mismatch_hidden": projection_hidden,
        "detailed_basis_applicable": detailed_applicable,
        "detailed_basis_distinguished_from_summary": detailed_distinguished,
        "summary_overrode_detailed_basis": summary_overrode,
    }


def _build_checks(
    request: Mapping[str, Any],
    question: Mapping[str, Any],
    body_posture: Mapping[str, Any],
    carrier_evidence: Mapping[str, Any],
    posture: Mapping[str, Any],
    successor_basis: Mapping[str, Any],
    prior_participation: Mapping[str, Any],
    lifecycle_basis: Mapping[str, Any],
    registry_basis: Mapping[str, Any],
    standing_basis: Mapping[str, Any],
    continuity_basis: Mapping[str, Any],
    relation_closure_basis: Mapping[str, Any],
    evidence_accounting: Mapping[str, Any],
    non_claims: Mapping[str, Any],
    visibility: Mapping[str, bool],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for failure in precheck_failures:
        checks.append(_check(failure.lower(), False, "readable JSON object", failure, failure))

    checks.extend(
        [
            _check(
                "currentness_successor_question_declared",
                _nonempty(question.get("currentness_successor_question")),
                "declared currentness successor question",
                question.get("currentness_successor_question"),
                "CURRENTNESS_SUCCESSOR_QUESTION_UNDECLARED",
            ),
            _check(
                "currentness_successor_intent_supported",
                question.get("currentness_successor_intent")
                in SUPPORTED_CURRENTNESS_SUCCESSOR_INTENTS,
                sorted(SUPPORTED_CURRENTNESS_SUCCESSOR_INTENTS),
                question.get("currentness_successor_intent"),
                "CURRENTNESS_SUCCESSOR_INTENT_UNSUPPORTED",
            ),
            _check(
                "body_current_posture_present",
                bool(body_posture.get("body_current_posture_preserved")),
                "selected body-side current posture present",
                body_posture.get("raw_selected_body_current_posture"),
                "BODY_CURRENT_POSTURE_MISSING",
            ),
            _check(
                "carrier_evidence_present",
                bool(carrier_evidence.get("selected_carrier_evidence_declared")),
                "selected carrier evidence present",
                carrier_evidence.get("raw_selected_carrier_evidence"),
                "SELECTED_CARRIER_EVIDENCE_MISSING",
            ),
            _check(
                "carrier_evidence_parseable",
                bool(
                    not carrier_evidence.get("selected_carrier_evidence_declared")
                    or carrier_evidence.get("selected_carrier_evidence_parseable")
                ),
                "selected carrier evidence parseable",
                carrier_evidence.get("selected_carrier_evidence_parseable"),
                "SELECTED_CARRIER_EVIDENCE_MALFORMED",
            ),
            _check(
                "carrier_evidence_identity_present",
                bool(
                    carrier_evidence.get(
                        "selected_carrier_evidence_identities_preserved"
                    )
                ),
                "selected carrier evidence identities present",
                carrier_evidence.get("selected_carrier_evidence_ids"),
                "SELECTED_CARRIER_EVIDENCE_IDENTITY_MISSING",
            ),
            _check(
                "carrier_evidence_outcome_present",
                bool(
                    carrier_evidence.get(
                        "selected_carrier_evidence_outcomes_preserved"
                    )
                ),
                "selected carrier evidence outcomes present",
                carrier_evidence.get("selected_carrier_evidence_outcomes"),
                "SELECTED_CARRIER_EVIDENCE_OUTCOME_MISSING",
            ),
            _check(
                "currentness_successor_posture_supported",
                bool(posture.get("currentness_successor_posture_supported")),
                sorted(SUPPORTED_CURRENTNESS_SUCCESSOR_POSTURES),
                posture.get("requested_currentness_successor_posture"),
                "CURRENTNESS_SUCCESSOR_POSTURE_UNSUPPORTED",
            ),
            _check(
                "successor_basis_declared",
                bool(successor_basis.get("currentness_successor_basis_declared")),
                "currentness successor basis declared",
                successor_basis.get("raw_currentness_successor_basis"),
                "CURRENTNESS_SUCCESSOR_BASIS_MISSING",
            ),
            _basis_check(
                "prior_participation_basis_preserved_where_supplied",
                prior_participation,
                "prior_currentness_participation_basis",
                "PRIOR_CURRENTNESS_PARTICIPATION_BASIS_MISSING",
            ),
            _basis_check(
                "lifecycle_basis_preserved_where_supplied",
                lifecycle_basis,
                "lifecycle_basis",
                "LIFECYCLE_REGISTRY_PROPAGATION_BASIS_MISSING",
            ),
            _basis_check(
                "registry_persistence_basis_preserved_where_supplied",
                registry_basis,
                "registry_persistence_basis",
                "LIFECYCLE_REGISTRY_PROPAGATION_BASIS_MISSING",
            ),
            _basis_check(
                "standing_propagation_basis_preserved_where_supplied",
                standing_basis,
                "standing_propagation_basis",
                "LIFECYCLE_REGISTRY_PROPAGATION_BASIS_MISSING",
            ),
            _basis_check(
                "continuity_turn_basis_preserved_where_supplied",
                continuity_basis,
                "carrier_continuity_turn_basis",
                "CARRIER_CONTINUITY_TURN_BASIS_MISSING",
            ),
            _basis_check(
                "relation_conformance_closure_basis_preserved_where_supplied",
                relation_closure_basis,
                "relation_conformance_closure_basis",
                "CURRENTNESS_SUCCESSOR_BASIS_MISSING",
            ),
            _check(
                "evidence_accounting_preserved",
                bool(evidence_accounting.get("evidence_accounting_preserved")),
                "evidence accounting declared",
                evidence_accounting.get("raw_evidence_accounting"),
                "CURRENTNESS_SUCCESSOR_BASIS_MISSING",
            ),
            _visibility_check(
                "visible_refusal_preserved",
                visibility,
                "visible_refusal_applicable",
                "visible_refusal_preserved",
                "CURRENTNESS_SUCCESSOR_HIDES_REFUSAL",
            ),
            _visibility_check(
                "visible_divergence_preserved",
                visibility,
                "visible_divergence_applicable",
                "visible_divergence_preserved",
                "CURRENTNESS_SUCCESSOR_HIDES_DIVERGENCE",
            ),
            _visibility_check(
                "blocked_attempts_preserved",
                visibility,
                "blocked_attempts_applicable",
                "blocked_attempts_preserved",
                "CURRENTNESS_SUCCESSOR_HIDES_BLOCKED_ATTEMPT",
            ),
            _visibility_check(
                "projection_mismatch_preserved",
                visibility,
                "projection_mismatch_applicable",
                "projection_mismatch_preserved",
                "CURRENTNESS_SUCCESSOR_HIDES_PROJECTION_MISMATCH",
            ),
            _visibility_check(
                "detailed_basis_distinguishable_from_summary",
                visibility,
                "detailed_basis_applicable",
                "detailed_basis_distinguished_from_summary",
                "SUMMARY_OVERWRITES_DETAILED_BASIS",
            ),
            _check(
                "summary_does_not_override_detailed_basis",
                not visibility.get("summary_overrode_detailed_basis"),
                "summary does not override detailed basis",
                visibility.get("summary_overrode_detailed_basis"),
                "SUMMARY_OVERWRITES_DETAILED_BASIS",
            ),
        ]
    )

    checks.extend(_anti_collapse_checks(request))
    checks.append(
        _check(
            "non_claims_remain_false",
            bool(non_claims.get("required_non_claims_preserved")),
            "all required non-claims present and false",
            {
                "missing_required_non_claims": non_claims.get(
                    "missing_required_non_claims"
                ),
                "flipped_required_non_claims": non_claims.get(
                    "flipped_required_non_claims"
                ),
            },
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _basis_check(
    check_name: str,
    section: Mapping[str, Any],
    section_name: str,
    block_code: str,
) -> dict[str, Any]:
    declared = bool(section.get(f"{section_name}_declared"))
    required = bool(section.get(f"{section_name}_required"))
    preserved = bool(section.get(f"{section_name}_preserved"))
    return _check(
        check_name,
        bool((not required and not declared) or preserved),
        "basis preserved where required or supplied",
        {
            "declared": declared,
            "required": required,
            "preserved": preserved,
        },
        block_code,
    )


def _visibility_check(
    check_name: str,
    visibility: Mapping[str, bool],
    applicable_key: str,
    preserved_key: str,
    block_code: str,
) -> dict[str, Any]:
    applicable = bool(visibility.get(applicable_key))
    preserved = bool(visibility.get(preserved_key))
    return _check(
        check_name,
        bool(not applicable or preserved),
        "visible posture preserved where applicable",
        {
            "applicable": applicable,
            "preserved": preserved,
        },
        block_code,
    )


def _anti_collapse_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    anti_collapse_specs: tuple[tuple[str, tuple[str, ...], str, str], ...] = (
        (
            "no_carrier_currentness",
            (
                "carrier_currentness_created",
                "currentness_created",
                "currentness_successor_creates_carrier_currentness",
                "distributed_currentness_created",
                "currentness_successor_creates_distributed_currentness",
                "carrier_evidence_became_current",
                "carrier_evidence_currentness",
            ),
            "carrier currentness not created",
            "CURRENTNESS_SUCCESSOR_CREATES_CARRIER_CURRENTNESS",
        ),
        (
            "no_current_carrier_selected",
            ("current_carrier_selected", "currentness_successor_selects_current_carrier"),
            "current carrier not selected",
            "CURRENTNESS_SUCCESSOR_SELECTS_CURRENT_CARRIER",
        ),
        (
            "no_winning_carrier_selected",
            ("winning_carrier_selected", "currentness_successor_selects_winning_carrier"),
            "winning carrier not selected",
            "CURRENTNESS_SUCCESSOR_SELECTS_WINNING_CARRIER",
        ),
        (
            "no_losing_carrier_invalidated",
            ("losing_carrier_invalidated", "currentness_successor_invalidates_losing_carrier"),
            "losing carrier not invalidated",
            "CURRENTNESS_SUCCESSOR_INVALIDATES_LOSING_CARRIER",
        ),
        (
            "no_source_replacement",
            ("source_replaced", "currentness_successor_created_source", "currentness_successor_replaces_source"),
            "source not replaced",
            "CURRENTNESS_SUCCESSOR_REPLACES_SOURCE",
        ),
        (
            "no_authority",
            ("authority_created", "currentness_successor_created_authority", "currentness_successor_creates_authority"),
            "authority not created",
            "CURRENTNESS_SUCCESSOR_CREATES_AUTHORITY",
        ),
        (
            "no_permission",
            ("permission_created", "currentness_successor_created_permission", "currentness_successor_creates_permission"),
            "permission not created",
            "CURRENTNESS_SUCCESSOR_CREATES_PERMISSION",
        ),
        (
            "no_carrier_hierarchy",
            ("carrier_hierarchy_created", "currentness_successor_created_carrier_hierarchy", "currentness_successor_creates_carrier_hierarchy"),
            "carrier hierarchy not created",
            "CURRENTNESS_SUCCESSOR_CREATES_CARRIER_HIERARCHY",
        ),
        (
            "no_divergence_resolution",
            ("divergence_resolved", "currentness_successor_resolved_divergence", "currentness_successor_resolves_divergence"),
            "divergence not resolved",
            "CURRENTNESS_SUCCESSOR_RESOLVES_DIVERGENCE",
        ),
        (
            "no_evidence_erasure",
            ("evidence_erased", "currentness_successor_erased_evidence", "currentness_successor_erases_evidence"),
            "evidence not erased",
            "CURRENTNESS_SUCCESSOR_ERASES_EVIDENCE",
        ),
        (
            "no_distributed_standing",
            ("distributed_standing_created", "currentness_successor_created_distributed_standing", "currentness_successor_creates_distributed_standing"),
            "distributed standing not created",
            "CURRENTNESS_SUCCESSOR_CREATES_DISTRIBUTED_STANDING",
        ),
        (
            "no_repository_synchronization",
            ("repository_synchronization_authorized", "currentness_successor_authorizes_repository_sync"),
            "repository synchronization not authorized",
            "CURRENTNESS_SUCCESSOR_AUTHORIZES_REPOSITORY_SYNC",
        ),
        (
            "no_full_body_transfer",
            ("full_body_transfer_authorized", "currentness_successor_authorizes_full_body_transfer"),
            "full body transfer not authorized",
            "CURRENTNESS_SUCCESSOR_AUTHORIZES_FULL_BODY_TRANSFER",
        ),
        (
            "no_second_body",
            ("second_body_created", "currentness_successor_creates_second_body"),
            "second body not created",
            "CURRENTNESS_SUCCESSOR_CREATES_SECOND_BODY",
        ),
        (
            "no_continuation",
            ("continuation_authorized", "currentness_successor_authorizes_continuation"),
            "continuation not authorized",
            "CURRENTNESS_SUCCESSOR_AUTHORIZES_CONTINUATION",
        ),
        (
            "no_distributed_operation",
            ("distributed_operation_authorized", "currentness_successor_authorizes_distributed_operation"),
            "distributed operation not authorized",
            "CURRENTNESS_SUCCESSOR_AUTHORIZES_DISTRIBUTED_OPERATION",
        ),
        (
            "no_latest_file_currentness",
            ("latest_file_currentness",),
            "latest file not treated as currentness",
            "LATEST_FILE_CURRENTNESS",
        ),
        (
            "no_latest_turn_currentness",
            ("latest_turn_currentness",),
            "latest turn not treated as currentness",
            "LATEST_TURN_CURRENTNESS",
        ),
        (
            "no_majority_or_success_count_currentness",
            (
                "majority_carrier_currentness",
                "successful_receipt_count_currentness",
                "majority_currentness",
                "success_count_currentness",
            ),
            "majority or success count not treated as currentness",
            "MAJORITY_OR_SUCCESS_COUNT_CURRENTNESS",
        ),
        (
            "no_registry_lifecycle_propagation_or_turn_currentness",
            (
                "registry_record_currentness",
                "lifecycle_status_currentness",
                "standing_propagation_currentness",
                "continuity_turn_currentness",
                "availability_currentness",
                "completeness_currentness",
                "carrier_label_currentness",
                "physical_possession_currentness",
                "returned_evidence_currentness",
                "admitted_evidence_currentness",
                "relation_conformance_currentness",
                "closure_currentness",
            ),
            "registry, lifecycle, propagation, and turn posture are not currentness",
            "REGISTRY_LIFECYCLE_PROPAGATION_OR_TURN_CURRENTNESS",
        ),
        (
            "no_mutation_replay_or_merge",
            ("mutation_performed", "replay_performed", "merge_performed"),
            "mutation, replay, and merge not performed",
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
    )
    return [
        _check(
            check_name,
            not _recursive_true(request, keys),
            expected,
            _first_true_key(request, keys),
            block_code,
        )
        for check_name, keys, expected, block_code in anti_collapse_specs
    ]


def _currentness_successor_statement(
    outcome: str,
    question: Mapping[str, Any],
    body_posture: Mapping[str, Any],
    carrier_evidence: Mapping[str, Any],
    posture: Mapping[str, Any],
    successor_basis: Mapping[str, Any],
    prior_participation: Mapping[str, Any],
    lifecycle_basis: Mapping[str, Any],
    registry_basis: Mapping[str, Any],
    standing_basis: Mapping[str, Any],
    continuity_basis: Mapping[str, Any],
    relation_closure_basis: Mapping[str, Any],
    evidence_accounting: Mapping[str, Any],
    visibility: Mapping[str, bool],
    block: Mapping[str, Any],
) -> dict[str, Any]:
    recorded = outcome == CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED
    not_recorded = outcome == CROSS_CARRIER_CURRENTNESS_SUCCESSOR_NOT_RECORDED
    return {
        "cross_carrier_currentness_successor_recorded": recorded,
        "not_recorded_reason": question.get("not_recorded_reason")
        if not_recorded
        else None,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "body_current_posture_preserved": bool(
            body_posture.get("body_current_posture_preserved")
        ),
        "selected_carrier_evidence_preserved": bool(
            carrier_evidence.get("selected_carrier_evidence_preserved")
        ),
        "selected_carrier_evidence_identities_preserved": bool(
            carrier_evidence.get("selected_carrier_evidence_identities_preserved")
        ),
        "selected_carrier_evidence_outcomes_preserved": bool(
            carrier_evidence.get("selected_carrier_evidence_outcomes_preserved")
        ),
        "currentness_successor_posture_preserved": bool(
            posture.get("currentness_successor_posture_preserved")
        ),
        "currentness_successor_basis_preserved": bool(
            successor_basis.get("currentness_successor_basis_preserved")
        ),
        "evidence_accounting_preserved": bool(
            evidence_accounting.get("evidence_accounting_preserved")
        ),
        "visible_refusal_preserved": bool(
            visibility.get("visible_refusal_preserved")
        ),
        "visible_divergence_preserved": bool(
            visibility.get("visible_divergence_preserved")
        ),
        "blocked_attempts_preserved": bool(
            visibility.get("blocked_attempts_preserved")
        ),
        "projection_mismatch_preserved": bool(
            visibility.get("projection_mismatch_preserved")
        ),
        "prior_currentness_participation_basis_preserved": bool(
            prior_participation.get("prior_currentness_participation_basis_preserved")
        ),
        "lifecycle_basis_preserved": bool(
            lifecycle_basis.get("lifecycle_basis_preserved")
        ),
        "registry_persistence_basis_preserved": bool(
            registry_basis.get("registry_persistence_basis_preserved")
        ),
        "standing_propagation_basis_preserved": bool(
            standing_basis.get("standing_propagation_basis_preserved")
        ),
        "carrier_continuity_turn_basis_preserved": bool(
            continuity_basis.get("carrier_continuity_turn_basis_preserved")
        ),
        "relation_conformance_closure_basis_preserved": bool(
            relation_closure_basis.get("relation_conformance_closure_basis_preserved")
        ),
        "detailed_basis_distinguished_from_summary": bool(
            visibility.get("detailed_basis_distinguished_from_summary")
        ),
        "summary_overrode_detailed_basis": False,
        "carrier_currentness_created": False,
        "currentness_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "source_replaced": False,
        "authority_created": False,
        "permission_created": False,
        "carrier_hierarchy_created": False,
        "divergence_resolved": False,
        "evidence_erased": False,
        "distributed_standing_created": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
        "latest_file_currentness": False,
        "latest_turn_currentness": False,
        "majority_carrier_currentness": False,
        "successful_receipt_count_currentness": False,
        "registry_record_currentness": False,
        "lifecycle_status_currentness": False,
        "standing_propagation_currentness": False,
        "continuity_turn_currentness": False,
    }


def _metadata(
    question: Mapping[str, Any],
    posture: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    generated_at = _utc_now()
    request_id = (
        question.get("currentness_successor_request_id")
        or posture.get("requested_currentness_successor_posture")
        or "cross_carrier_currentness_successor"
    )
    return {
        "cross_carrier_currentness_successor_result_id": (
            f"{_safe_filename_part(request_id)}__{_safe_filename_part(outcome)}__{generated_at}"
        ),
        "cross_carrier_currentness_successor_result_type": RESULT_TYPE,
        "cross_carrier_currentness_successor_result_version": RESULT_VERSION,
        "generated_at": generated_at,
        "resolver_module": RESOLVER_MODULE,
    }


def _read_json_mapping(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CrossCarrierCurrentnessSuccessorBoundaryError(
            "DECLARED_CURRENTNESS_SUCCESSOR_REQUEST_UNREADABLE",
            str(exc),
        ) from exc
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CrossCarrierCurrentnessSuccessorBoundaryError(
            "DECLARED_CURRENTNESS_SUCCESSOR_REQUEST_MALFORMED",
            str(exc),
        ) from exc
    if not isinstance(parsed, Mapping):
        raise CrossCarrierCurrentnessSuccessorBoundaryError(
            "DECLARED_CURRENTNESS_SUCCESSOR_REQUEST_MALFORMED",
            "Declared currentness successor request JSON must be an object.",
        )
    return copy.deepcopy(dict(parsed))


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": copy.deepcopy(expected_posture),
        "actual_posture": copy.deepcopy(actual_posture),
        "block_code": None if passed else block_code,
    }


def _block_reason(block_code: Any) -> str | None:
    if not block_code:
        return None
    return BLOCK_REASONS.get(str(block_code), "Currentness successor posture blocked.")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    resolved = Path(path)
    try:
        return str(resolved.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(resolved)


def _as_mapping(value: Any) -> dict[str, Any]:
    return copy.deepcopy(dict(value)) if isinstance(value, Mapping) else {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return []
    return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]


def _entries_from_value(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, Mapping):
        for key in (
            "entries",
            "items",
            "evidence",
            "selected_carrier_evidence_entries",
            "evidence_accounting_entries",
        ):
            entries = value.get(key)
            if isinstance(entries, Sequence) and not isinstance(
                entries,
                (str, bytes, bytearray),
            ):
                return [
                    copy.deepcopy(dict(item))
                    for item in entries
                    if isinstance(item, Mapping)
                ]
        return [copy.deepcopy(dict(value))]
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]
    return []


def _basis_declared(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    if isinstance(value, str):
        return bool(value.strip())
    return bool(value)


def _nonempty(value: Any) -> bool:
    return value is not None and (not isinstance(value, str) or bool(value.strip()))


def _normalize_token(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        normalized = value.strip()
        return normalized or None
    return str(value)


def _extract_identity(value: Any) -> str | None:
    if isinstance(value, str):
        return value.strip() or None
    if not isinstance(value, Mapping):
        return None
    for key in (
        "currentness_successor_request_id",
        "selected_body_current_posture_id",
        "body_current_posture_id",
        "current_posture_id",
        "selected_carrier_evidence_id",
        "carrier_evidence_id",
        "evidence_id",
        "artifact_id",
        "result_id",
        "id",
        "name",
    ):
        candidate = value.get(key)
        if _nonempty(candidate):
            return str(candidate)
    return None


def _entry_outcome(value: Any) -> Any:
    if not isinstance(value, Mapping):
        return None
    for key in (
        "selected_carrier_evidence_outcome",
        "carrier_evidence_outcome",
        "evidence_outcome",
        "artifact_outcome",
        "result_outcome",
        "lifecycle_status",
        "status",
        "outcome",
    ):
        if _nonempty(value.get(key)):
            return value.get(key)
    return None


def _field_from_mapping(value: Any, keys: Sequence[str]) -> Any:
    if not isinstance(value, Mapping):
        return None
    for key in keys:
        if key in value and _nonempty(value.get(key)):
            return value.get(key)
    return None


def _first_declared(*values: Any) -> Any:
    for value in values:
        if _basis_declared(value):
            return copy.deepcopy(value)
    return None


def _is_true(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1"}
    return False


def _recursive_true(value: Any, keys: Sequence[str]) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if key in keys and _is_true(item):
                return True
            if _recursive_true(item, keys):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_recursive_true(item, keys) for item in value)
    return False


def _first_true_key(value: Any, keys: Sequence[str]) -> str | None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if key in keys and _is_true(item):
                return key
            nested = _first_true_key(item, keys)
            if nested:
                return nested
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for item in value:
            nested = _first_true_key(item, keys)
            if nested:
                return nested
    return None


def _entries_have_token(entries: Sequence[Mapping[str, Any]], tokens: Sequence[str]) -> bool:
    return any(_text_has_any_token(entry, tokens) for entry in entries)


def _entries_have_outcome(
    entries: Sequence[Mapping[str, Any]],
    outcomes: Sequence[str],
) -> bool:
    normalized_outcomes = {item.lower() for item in outcomes}
    return any(
        str(_entry_outcome(entry)).lower() in normalized_outcomes
        for entry in entries
        if _entry_outcome(entry) is not None
    )


def _text_has_any_token(value: Any, tokens: Sequence[str]) -> bool:
    lowered_tokens = tuple(token.lower() for token in tokens)
    if isinstance(value, str):
        lowered = value.lower()
        return any(token in lowered for token in lowered_tokens)
    if isinstance(value, Mapping):
        return any(_text_has_any_token(item, tokens) for item in value.values())
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_text_has_any_token(item, tokens) for item in value)
    return False


def _safe_filename_part(value: Any) -> str:
    raw = str(value or "cross_carrier_currentness_successor").strip().lower()
    chars: list[str] = []
    for char in raw:
        if char.isalnum() or char in {"-", "_"}:
            chars.append(char)
        else:
            chars.append("_")
    cleaned = "".join(chars).strip("_")
    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")
    return cleaned[:160] or "cross_carrier_currentness_successor"


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


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "carrier_currentness_created",
        "source_replaced",
        "current_carrier_selected",
        "winning_carrier_selected",
        "losing_carrier_invalidated",
        "currentness_successor_created_distributed_standing",
        "currentness_successor_resolved_divergence",
        "currentness_successor_erased_evidence",
        "summary_overrode_detailed_basis",
        "latest_file_currentness",
        "latest_turn_currentness",
        "majority_carrier_currentness",
        "successful_receipt_count_currentness",
        "registry_record_currentness",
        "lifecycle_status_currentness",
        "standing_propagation_currentness",
        "continuity_turn_currentness",
        "repository_synchronization_authorized",
        "full_body_transfer_authorized",
        "second_body_created",
        "continuation_authorized",
        "distributed_operation_authorized",
        "distributed_standing_created",
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    )
    return {key: copy.deepcopy(non_claims.get(key)) for key in keys}
