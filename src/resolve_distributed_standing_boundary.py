"""Bounded distributed standing boundary resolver.

This resolver records one bounded distributed-standing boundary posture for a
declared question: what it would mean for the body to stand across carriers
without source collapse. It preserves prerequisite basis and non-claims only.
It does not execute distributed standing, synchronize repositories, transfer a
full body, create a second body, select a current carrier, select a winning
carrier, invalidate a losing carrier, create carrier currentness, create truth,
authorize action, authorize continuation, or authorize distributed operation.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class DistributedStandingBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit distributed inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


REPO_ROOT = Path(__file__).resolve().parents[1]

DISTRIBUTED_STANDING_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_distributed_standing_boundary"
)

RESOLVER_MODULE = "resolve_distributed_standing_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "distributed_standing_boundary_result"

RECORD_INTENT = "RECORD_DISTRIBUTED_STANDING_BOUNDARY_POSTURE"
DO_NOT_RECORD_INTENT = "DO_NOT_RECORD_DISTRIBUTED_STANDING_BOUNDARY_POSTURE"
BLOCK_INTENT = "BLOCK_DISTRIBUTED_STANDING_BOUNDARY_POSTURE"
SUPPORTED_DISTRIBUTED_STANDING_INTENTS = {
    RECORD_INTENT,
    DO_NOT_RECORD_INTENT,
    BLOCK_INTENT,
}

DISTRIBUTED_STANDING_POSTURE_RECORDED = "DISTRIBUTED_STANDING_POSTURE_RECORDED"
DISTRIBUTED_STANDING_POSTURE_NOT_RECORDED = (
    "DISTRIBUTED_STANDING_POSTURE_NOT_RECORDED"
)
DISTRIBUTED_STANDING_POSTURE_BLOCKED = "DISTRIBUTED_STANDING_POSTURE_BLOCKED"
DISTRIBUTED_STANDING_REQUIRES_ADDITIONAL_BASIS = (
    "DISTRIBUTED_STANDING_REQUIRES_ADDITIONAL_BASIS"
)
DISTRIBUTED_STANDING_EXCLUDED_FOR_DECLARED_SCOPE = (
    "DISTRIBUTED_STANDING_EXCLUDED_FOR_DECLARED_SCOPE"
)
DISTRIBUTED_STANDING_REQUIRES_REVALIDATION = (
    "DISTRIBUTED_STANDING_REQUIRES_REVALIDATION"
)
DISTRIBUTED_STANDING_REQUIRES_SEPARATE_REVIEW = (
    "DISTRIBUTED_STANDING_REQUIRES_SEPARATE_REVIEW"
)

SUPPORTED_DISTRIBUTED_STANDING_POSTURES = {
    DISTRIBUTED_STANDING_POSTURE_RECORDED,
    DISTRIBUTED_STANDING_POSTURE_NOT_RECORDED,
    DISTRIBUTED_STANDING_POSTURE_BLOCKED,
    DISTRIBUTED_STANDING_REQUIRES_ADDITIONAL_BASIS,
    DISTRIBUTED_STANDING_EXCLUDED_FOR_DECLARED_SCOPE,
    DISTRIBUTED_STANDING_REQUIRES_REVALIDATION,
    DISTRIBUTED_STANDING_REQUIRES_SEPARATE_REVIEW,
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
    "divergence_resolved": False,
    "truth_created": False,
    "action_authorized": False,
    "distributed_standing_authorized_sync": False,
    "distributed_standing_authorized_full_body_transfer": False,
    "distributed_standing_created_second_body": False,
    "distributed_standing_authorized_continuation": False,
    "distributed_standing_authorized_distributed_operation": False,
    "distributed_standing_erased_evidence": False,
    "distributed_standing_hid_refusal": False,
    "distributed_standing_hid_divergence": False,
    "distributed_standing_hid_blocked_attempt": False,
    "distributed_standing_hid_projection_mismatch": False,
    "summary_overrode_detailed_basis": False,
    "latest_file_standing": False,
    "latest_turn_standing": False,
    "majority_carrier_standing": False,
    "successful_receipt_count_standing": False,
    "registry_record_standing": False,
    "lifecycle_status_standing": False,
    "standing_propagation_standing": False,
    "continuity_turn_standing": False,
    "currentness_successor_standing": False,
    "divergence_consequence_standing": False,
    "repository_synchronization_authorized": False,
    "full_body_transfer_authorized": False,
    "second_body_created": False,
    "continuation_authorized": False,
    "distributed_operation_authorized": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "DECLARED_DISTRIBUTED_STANDING_REQUEST_UNREADABLE": "Declared distributed standing request path could not be read.",
    "DECLARED_DISTRIBUTED_STANDING_REQUEST_MALFORMED": "Declared distributed standing request is not a JSON object or mapping.",
    "DISTRIBUTED_STANDING_REQUEST_EXPLICITLY_BLOCKED": "Distributed standing request explicitly declares a blocked posture.",
    "DISTRIBUTED_STANDING_QUESTION_UNDECLARED": "Distributed standing question is undeclared.",
    "DISTRIBUTED_STANDING_INTENT_UNSUPPORTED": "Distributed standing intent is unsupported.",
    "DISTRIBUTED_STANDING_POSTURE_UNSUPPORTED": "Distributed standing posture is unsupported.",
    "BODY_SIDE_STANDING_POSTURE_MISSING": "Selected body-side standing posture is missing.",
    "SELECTED_CARRIER_EVIDENCE_MISSING": "Selected carrier evidence is missing.",
    "SELECTED_CARRIER_EVIDENCE_MALFORMED": "Selected carrier evidence is malformed.",
    "SELECTED_CARRIER_EVIDENCE_IDENTITY_OR_OUTCOME_MISSING": "Selected carrier evidence identity or outcome is missing.",
    "DISTRIBUTED_STANDING_BASIS_MISSING": "Distributed standing basis is missing.",
    "SOURCE_BODY_LINEAGE_MISSING": "Source-body lineage is missing.",
    "DIVERGENCE_CONSEQUENCE_BASIS_MISSING": "Divergence consequence basis is missing.",
    "CURRENTNESS_SUCCESSOR_BASIS_MISSING": "Currentness successor basis is missing.",
    "CARRIER_CONTINUITY_TURN_BASIS_MISSING": "Carrier continuity-turn basis is missing.",
    "STANDING_PROPAGATION_BASIS_MISSING": "Standing propagation basis is missing.",
    "REGISTRY_PERSISTENCE_BASIS_MISSING": "Registry/persistence basis is missing.",
    "LIFECYCLE_BASIS_MISSING": "Lifecycle basis is missing.",
    "RELATION_CONFORMANCE_CLOSURE_BASIS_MISSING": "Relation/conformance/closure basis is missing where required.",
    "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BASIS_MISSING": "Current-body conformance v3 closure basis is missing.",
    "DISTRIBUTED_STANDING_HIDES_REFUSAL": "Distributed standing hides visible refusal.",
    "DISTRIBUTED_STANDING_HIDES_DIVERGENCE": "Distributed standing hides visible divergence.",
    "DISTRIBUTED_STANDING_HIDES_BLOCKED_ATTEMPT": "Distributed standing hides a blocked attempt.",
    "DISTRIBUTED_STANDING_HIDES_PROJECTION_MISMATCH": "Distributed standing hides projection mismatch.",
    "SUMMARY_OVERWRITES_DETAILED_BASIS": "Summary projection overwrites detailed basis.",
    "DISTRIBUTED_STANDING_CREATES_CARRIER_CURRENTNESS": "Distributed standing creates carrier currentness.",
    "DISTRIBUTED_STANDING_SELECTS_CURRENT_CARRIER": "Distributed standing selects a current carrier.",
    "DISTRIBUTED_STANDING_SELECTS_WINNING_CARRIER": "Distributed standing selects a winning carrier.",
    "DISTRIBUTED_STANDING_INVALIDATES_LOSING_CARRIER": "Distributed standing invalidates a losing carrier.",
    "DISTRIBUTED_STANDING_REPLACES_SOURCE": "Distributed standing replaces source.",
    "DISTRIBUTED_STANDING_CREATES_AUTHORITY": "Distributed standing creates authority.",
    "DISTRIBUTED_STANDING_CREATES_PERMISSION": "Distributed standing creates permission.",
    "DISTRIBUTED_STANDING_RESOLVES_DIVERGENCE": "Distributed standing resolves divergence.",
    "DISTRIBUTED_STANDING_CREATES_TRUTH": "Distributed standing creates truth.",
    "DISTRIBUTED_STANDING_AUTHORIZES_ACTION": "Distributed standing authorizes action.",
    "DISTRIBUTED_STANDING_ERASES_EVIDENCE": "Distributed standing erases evidence.",
    "DISTRIBUTED_STANDING_AUTHORIZES_REPOSITORY_SYNC": "Distributed standing authorizes repository synchronization.",
    "DISTRIBUTED_STANDING_AUTHORIZES_FULL_BODY_TRANSFER": "Distributed standing authorizes full body transfer.",
    "DISTRIBUTED_STANDING_CREATES_SECOND_BODY": "Distributed standing creates a second body.",
    "DISTRIBUTED_STANDING_AUTHORIZES_CONTINUATION": "Distributed standing authorizes continuation.",
    "DISTRIBUTED_STANDING_AUTHORIZES_DISTRIBUTED_OPERATION": "Distributed standing authorizes distributed operation.",
    "LATEST_FILE_OR_TURN_STANDING": "Latest file or latest turn is treated as distributed standing.",
    "MAJORITY_OR_SUCCESS_COUNT_STANDING": "Majority or successful receipt count is treated as distributed standing.",
    "REGISTRY_LIFECYCLE_PROPAGATION_TURN_CURRENTNESS_OR_CONSEQUENCE_STANDING": "Registry, lifecycle, standing propagation, continuity turn, currentness successor, or divergence consequence is treated as standing by itself.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge was detected.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required distributed standing non-claim is missing or flipped.",
}

DISTRIBUTED_STANDING_NON_MEANING = {
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_distributed_operation": True,
    "does_not_mean_carrier_currentness": True,
    "does_not_mean_current_carrier_selected": True,
    "does_not_mean_winning_carrier_selected": True,
    "does_not_mean_losing_carrier_invalidated": True,
    "does_not_mean_source_replacement": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_truth": True,
    "does_not_mean_action": True,
    "does_not_mean_consequence_action_law": True,
    "does_not_mean_divergence_resolved": True,
    "does_not_mean_refusal_erased": True,
    "does_not_mean_blocked_attempt_erased": True,
    "does_not_mean_evidence_erased": True,
    "does_not_mean_registry_authority": True,
    "does_not_mean_lifecycle_authority": True,
    "does_not_mean_standing_propagation_authority": True,
    "does_not_mean_continuity_turn_authority": True,
    "does_not_mean_currentness_successor_authority": True,
    "does_not_mean_divergence_consequence_authority": True,
    "does_not_mean_carrier_hierarchy": True,
    "does_not_mean_carrier_priority": True,
    "does_not_mean_carrier_sovereignty": True,
    "does_not_mean_majority_standing": True,
    "does_not_mean_success_count_standing": True,
    "does_not_mean_latest_file_standing": True,
    "does_not_mean_latest_turn_standing": True,
    "does_not_mean_availability_standing": True,
    "does_not_mean_possession_standing": True,
    "does_not_mean_network_standing": True,
    "does_not_mean_consensus_standing": True,
    "does_not_mean_launch_publication_readiness": True,
}

WHAT_REMAINS_OPEN = {
    "distributed_standing_implementation": True,
    "actual_distributed_standing_posture_execution_beyond_this_bounded_result": True,
    "carrier_registry_implementation": True,
    "persistence_implementation": True,
    "standing_propagation_implementation_beyond_boundary_recording": True,
    "carrier_continuity_turn_implementation_refinement": True,
    "future_currentness_successor_refinement_if_separately_justified": True,
    "future_divergence_consequence_refinement_if_separately_justified": True,
    "presence_law": True,
    "threshold_law": True,
    "truth_law": True,
    "action_consequence_law": True,
    "generalized_vessel_relation_lifecycle": True,
    "body_relevance_medium": True,
    "signal_series_or_accumulation_logic": True,
    "successor_carrier_law": True,
    "future_self_orientation_successor_only_if_separately_justified": True,
    "repository_synchronization_only_if_separately_declared_and_bounded": True,
    "full_body_transfer_only_if_separately_declared_and_bounded": True,
    "distributed_operation_only_if_separately_declared_and_bounded": True,
    "open_means_not_scheduled": True,
    "open_means_not_authorized": True,
    "open_means_not_executed": True,
}

IDENTITY_KEYS = (
    "selected_body_side_standing_posture_id",
    "body_side_standing_posture_id",
    "standing_posture_id",
    "selected_carrier_evidence_id",
    "carrier_evidence_id",
    "evidence_id",
    "artifact_id",
    "result_id",
    "basis_id",
    "id",
    "path",
)
OUTCOME_KEYS = (
    "selected_body_side_standing_posture_outcome",
    "body_side_standing_posture_outcome",
    "standing_posture_outcome",
    "selected_carrier_evidence_outcome",
    "carrier_evidence_outcome",
    "evidence_outcome",
    "artifact_outcome",
    "result_outcome",
    "basis_outcome",
    "outcome",
    "status",
)


def resolve_distributed_standing_boundary(
    declared_distributed_standing_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded distributed standing request mapping."""

    if declared_distributed_standing_request is None:
        return _resolve_distributed_standing({}, None, [])
    if not isinstance(declared_distributed_standing_request, Mapping):
        return _resolve_distributed_standing(
            {},
            None,
            ["DECLARED_DISTRIBUTED_STANDING_REQUEST_MALFORMED"],
        )
    return _resolve_distributed_standing(
        copy.deepcopy(dict(declared_distributed_standing_request)),
        None,
        [],
    )


def resolve_distributed_standing_boundary_from_path(
    declared_distributed_standing_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one bounded distributed standing request from a JSON object."""

    path = Path(declared_distributed_standing_request_path)
    try:
        request = _read_json_mapping(path)
    except DistributedStandingBoundaryError as exc:
        return _resolve_distributed_standing({}, path, [exc.block_code])
    return _resolve_distributed_standing(request, path, [])


def write_distributed_standing_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an additive distributed standing result without overwriting."""

    if not isinstance(result, Mapping):
        raise DistributedStandingBoundaryError(
            "DECLARED_DISTRIBUTED_STANDING_REQUEST_MALFORMED",
            "Distributed standing result must be a mapping.",
        )

    if output_path is None:
        summary = _as_mapping(result.get("distributed_standing_summary"))
        basis_id = (
            summary.get("distributed_standing_request_id")
            or summary.get("requested_distributed_standing_posture")
            or "distributed_standing"
        )
        output_path = DISTRIBUTED_STANDING_BOUNDARY_ROOT / (
            f"{_safe_filename_part(basis_id)}__distributed_standing_result.json"
        )

    target = _non_overwriting_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(
            dict(result),
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            default=str,
        )
        + "\n",
        encoding="utf-8",
    )
    return target


def build_distributed_standing_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact summary from a full distributed standing result."""

    checks = _mapping_list(result.get("distributed_standing_checks"))
    question = _as_mapping(result.get("declared_distributed_standing_question"))
    body_posture = _as_mapping(result.get("selected_body_side_standing_posture"))
    carrier_evidence = _as_mapping(result.get("selected_carrier_evidence"))
    posture = _as_mapping(result.get("distributed_standing_posture"))
    statement = _as_mapping(result.get("distributed_standing_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "distributed_standing_request_id": question.get(
            "distributed_standing_request_id"
        ),
        "distributed_standing_question": question.get(
            "distributed_standing_question"
        ),
        "distributed_standing_intent": question.get("distributed_standing_intent"),
        "requested_distributed_standing_posture": posture.get(
            "requested_distributed_standing_posture"
        ),
        "selected_body_side_standing_posture_id": body_posture.get(
            "selected_body_side_standing_posture_id"
        ),
        "selected_body_side_standing_posture_outcome": body_posture.get(
            "selected_body_side_standing_posture_outcome"
        ),
        "selected_carrier_evidence_ids": carrier_evidence.get(
            "selected_carrier_evidence_ids"
        ),
        "selected_carrier_evidence_outcomes": carrier_evidence.get(
            "selected_carrier_evidence_outcomes"
        ),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "distributed_standing_posture_recorded": bool(
            statement.get("distributed_standing_posture_recorded")
        ),
        "source_body_lineage_preserved": bool(
            statement.get("source_body_lineage_preserved")
        ),
        "selected_carrier_evidence_preserved": bool(
            statement.get("selected_carrier_evidence_preserved")
        ),
        "divergence_consequence_basis_preserved": bool(
            statement.get("divergence_consequence_basis_preserved")
        ),
        "currentness_successor_basis_preserved": bool(
            statement.get("currentness_successor_basis_preserved")
        ),
        "carrier_continuity_turn_basis_preserved": bool(
            statement.get("carrier_continuity_turn_basis_preserved")
        ),
        "standing_propagation_basis_preserved": bool(
            statement.get("standing_propagation_basis_preserved")
        ),
        "registry_persistence_basis_preserved": bool(
            statement.get("registry_persistence_basis_preserved")
        ),
        "lifecycle_basis_preserved": bool(
            statement.get("lifecycle_basis_preserved")
        ),
        "relation_conformance_closure_basis_preserved": bool(
            statement.get("relation_conformance_closure_basis_preserved")
        ),
        "current_body_conformance_v3_closure_basis_preserved": bool(
            statement.get("current_body_conformance_v3_closure_basis_preserved")
        ),
        "visible_refusal_preserved": bool(statement.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(
            statement.get("visible_divergence_preserved")
        ),
        "blocked_attempts_preserved": bool(
            statement.get("blocked_attempts_preserved")
        ),
        "projection_mismatch_preserved": bool(
            statement.get("projection_mismatch_preserved")
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
        "no_truth_action": not bool(
            statement.get("truth_created") or statement.get("action_authorized")
        ),
        "no_divergence_resolution": not bool(statement.get("divergence_resolved")),
        "no_evidence_erasure": not bool(statement.get("evidence_erased")),
        "no_sync_full_body_transfer_second_body": not bool(
            statement.get("repository_synchronization_authorized")
            or statement.get("full_body_transfer_authorized")
            or statement.get("second_body_created")
        ),
        "no_continuation": not bool(statement.get("continuation_authorized")),
        "no_distributed_operation": not bool(
            statement.get("distributed_operation_authorized")
        ),
        "no_latest_file_turn_majority_success_count_standing": not bool(
            statement.get("latest_file_standing")
            or statement.get("latest_turn_standing")
            or statement.get("majority_carrier_standing")
            or statement.get("successful_receipt_count_standing")
        ),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_declared_distributed_standing_request(
    distributed_standing_request_id: str,
    distributed_standing_question: str,
    selected_body_side_standing_posture: Mapping[str, Any],
    selected_carrier_evidence: Sequence[Mapping[str, Any]],
    requested_distributed_standing_posture: str,
    distributed_standing_basis: Mapping[str, Any] | str,
    distributed_standing_intent: str = RECORD_INTENT,
    *,
    source_body_lineage: Mapping[str, Any] | str | None = None,
    receipt_refusal_admission_basis: Mapping[str, Any] | str | None = None,
    divergence_basis: Mapping[str, Any] | str | None = None,
    divergence_consequence_basis: Mapping[str, Any] | str | None = None,
    currentness_successor_basis: Mapping[str, Any] | str | None = None,
    carrier_continuity_turn_basis: Mapping[str, Any] | str | None = None,
    standing_propagation_basis: Mapping[str, Any] | str | None = None,
    registry_persistence_basis: Mapping[str, Any] | str | None = None,
    lifecycle_basis: Mapping[str, Any] | str | None = None,
    relation_conformance_closure_basis: Mapping[str, Any] | str | None = None,
    current_body_conformance_v3_closure_basis: Mapping[str, Any] | str | None = None,
) -> dict[str, Any]:
    """Build one bounded request without inferring operation or carrier force."""

    evidence_items = [
        copy.deepcopy(dict(item))
        for item in selected_carrier_evidence
        if isinstance(item, Mapping)
    ]
    request: dict[str, Any] = {
        "distributed_standing_request_id": distributed_standing_request_id,
        "distributed_standing_question": distributed_standing_question,
        "distributed_standing_intent": distributed_standing_intent,
        "selected_body_side_standing_posture": copy.deepcopy(
            dict(selected_body_side_standing_posture)
        ),
        "selected_carrier_evidence": evidence_items,
        "requested_distributed_standing_posture": requested_distributed_standing_posture,
        "distributed_standing_basis": copy.deepcopy(distributed_standing_basis),
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
        "source_body_lineage": copy.deepcopy(
            source_body_lineage
            if source_body_lineage is not None
            else _default_basis(
                distributed_standing_request_id,
                "source_body_lineage",
                source_body_lineage_preserved=True,
            )
        ),
        "divergence_consequence_basis": copy.deepcopy(
            divergence_consequence_basis
            if divergence_consequence_basis is not None
            else _default_basis(
                distributed_standing_request_id,
                "divergence_consequence_basis",
                divergence_consequence_basis_preserved=True,
                divergence_consequence_standing=False,
                visible_divergence_preserved=True,
                visible_refusal_preserved=True,
            )
        ),
        "currentness_successor_basis": copy.deepcopy(
            currentness_successor_basis
            if currentness_successor_basis is not None
            else _default_basis(
                distributed_standing_request_id,
                "currentness_successor_basis",
                currentness_successor_basis_preserved=True,
                currentness_successor_standing=False,
                carrier_currentness_created=False,
            )
        ),
        "carrier_continuity_turn_basis": copy.deepcopy(
            carrier_continuity_turn_basis
            if carrier_continuity_turn_basis is not None
            else _default_basis(
                distributed_standing_request_id,
                "carrier_continuity_turn_basis",
                carrier_continuity_turn_basis_preserved=True,
                continuity_turn_standing=False,
                blocked_attempts_preserved=True,
                projection_mismatch_preserved=True,
            )
        ),
        "standing_propagation_basis": copy.deepcopy(
            standing_propagation_basis
            if standing_propagation_basis is not None
            else _default_basis(
                distributed_standing_request_id,
                "standing_propagation_basis",
                standing_propagation_basis_preserved=True,
                standing_propagation_standing=False,
            )
        ),
        "registry_persistence_basis": copy.deepcopy(
            registry_persistence_basis
            if registry_persistence_basis is not None
            else _default_basis(
                distributed_standing_request_id,
                "registry_persistence_basis",
                registry_persistence_basis_preserved=True,
                registry_record_standing=False,
            )
        ),
        "lifecycle_basis": copy.deepcopy(
            lifecycle_basis
            if lifecycle_basis is not None
            else _default_basis(
                distributed_standing_request_id,
                "lifecycle_basis",
                lifecycle_basis_preserved=True,
                lifecycle_status_standing=False,
            )
        ),
        "current_body_conformance_v3_closure_basis": copy.deepcopy(
            current_body_conformance_v3_closure_basis
            if current_body_conformance_v3_closure_basis is not None
            else _default_basis(
                distributed_standing_request_id,
                "current_body_conformance_v3_closure_basis",
                current_body_conformance_v3_closure_basis_preserved=True,
            )
        ),
        "visible_refusal_basis": {
            "visible_refusal_preserved": True,
            "refusal_remains_visible": True,
        },
        "visible_divergence_basis": {
            "visible_divergence_preserved": True,
            "divergence_remains_visible": True,
        },
        "blocked_attempt_basis": {
            "blocked_attempts_preserved": True,
            "blocked_attempt_remains_visible": True,
        },
        "projection_mismatch_basis": {
            "projection_mismatch_preserved": True,
            "projection_mismatch_remains_visible": True,
        },
        "detailed_basis_reference": "declared_detailed_distributed_standing_basis",
        "summary_projection_reference": "declared_summary_projection_only",
    }
    optional_sections = {
        "receipt_refusal_admission_basis": receipt_refusal_admission_basis,
        "divergence_basis": divergence_basis,
        "relation_conformance_closure_basis": relation_conformance_closure_basis,
    }
    for key, value in optional_sections.items():
        if value is not None:
            request[key] = copy.deepcopy(value)
    return request


def _resolve_distributed_standing(
    request: Mapping[str, Any],
    request_path: Path | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    normalized_request = _as_mapping(request)
    question = _declared_distributed_standing_question(
        normalized_request,
        request_path,
    )
    body_posture = _selected_body_side_standing_posture_section(normalized_request)
    carrier_evidence = _selected_carrier_evidence_section(normalized_request)
    posture = _distributed_standing_posture_section(normalized_request)
    standing_basis = _distributed_standing_basis_section(normalized_request)
    source_lineage = _basis_section(
        normalized_request,
        "source_body_lineage",
        "source_body_lineage",
        ("source_body_lineage_required", "requires_source_body_lineage"),
        required_default=True,
    )
    receipt_basis = _basis_section(
        normalized_request,
        "receipt_refusal_admission_basis",
        "receipt_refusal_admission_basis",
        (
            "receipt_refusal_admission_basis_required",
            "requires_receipt_refusal_admission_basis",
        ),
    )
    divergence_basis = _basis_section(
        normalized_request,
        "divergence_basis",
        "divergence_basis",
        ("divergence_basis_required", "requires_divergence_basis"),
    )
    divergence_consequence_basis = _basis_section(
        normalized_request,
        "divergence_consequence_basis",
        "divergence_consequence_basis",
        (
            "divergence_consequence_basis_required",
            "requires_divergence_consequence_basis",
        ),
        required_default=True,
    )
    currentness_successor_basis = _basis_section(
        normalized_request,
        "currentness_successor_basis",
        "currentness_successor_basis",
        (
            "currentness_successor_basis_required",
            "requires_currentness_successor_basis",
        ),
        required_default=True,
    )
    continuity_basis = _basis_section(
        normalized_request,
        "carrier_continuity_turn_basis",
        "carrier_continuity_turn_basis",
        (
            "carrier_continuity_turn_basis_required",
            "requires_carrier_continuity_turn_basis",
        ),
        required_default=True,
    )
    standing_propagation_basis = _basis_section(
        normalized_request,
        "standing_propagation_basis",
        "standing_propagation_basis",
        (
            "standing_propagation_basis_required",
            "requires_standing_propagation_basis",
        ),
        required_default=True,
    )
    registry_basis = _basis_section(
        normalized_request,
        "registry_persistence_basis",
        "registry_persistence_basis",
        (
            "registry_persistence_basis_required",
            "requires_registry_persistence_basis",
        ),
        required_default=True,
    )
    lifecycle_basis = _basis_section(
        normalized_request,
        "lifecycle_basis",
        "lifecycle_basis",
        ("lifecycle_basis_required", "requires_lifecycle_basis"),
        required_default=True,
    )
    relation_basis = _basis_section(
        normalized_request,
        "relation_conformance_closure_basis",
        "relation_conformance_closure_basis",
        (
            "relation_conformance_closure_basis_required",
            "relation_conformance_basis_required",
            "requires_relation_conformance_closure_basis",
        ),
    )
    current_body_closure_basis = _basis_section(
        normalized_request,
        "current_body_conformance_v3_closure_basis",
        "current_body_conformance_v3_closure_basis",
        (
            "current_body_conformance_v3_closure_basis_required",
            "requires_current_body_conformance_v3_closure_basis",
        ),
        required_default=True,
    )
    non_claims = _non_claims_section(normalized_request, question)
    visibility = _visibility_projection(
        normalized_request,
        carrier_evidence,
        standing_basis,
        source_lineage,
        receipt_basis,
        divergence_basis,
        divergence_consequence_basis,
        currentness_successor_basis,
        continuity_basis,
        standing_propagation_basis,
        registry_basis,
        lifecycle_basis,
        relation_basis,
        current_body_closure_basis,
        non_claims,
    )
    checks = _build_checks(
        normalized_request,
        question,
        body_posture,
        carrier_evidence,
        posture,
        standing_basis,
        source_lineage,
        receipt_basis,
        divergence_basis,
        divergence_consequence_basis,
        currentness_successor_basis,
        continuity_basis,
        standing_propagation_basis,
        registry_basis,
        lifecycle_basis,
        relation_basis,
        current_body_closure_basis,
        non_claims,
        visibility,
        precheck_failures,
    )

    failed_checks = [check for check in checks if check.get("passed") is False]
    requested_posture = posture.get("requested_distributed_standing_posture")
    if failed_checks:
        outcome = DISTRIBUTED_STANDING_POSTURE_BLOCKED
        block_code = failed_checks[0].get("block_code")
    elif question.get("distributed_standing_intent") == BLOCK_INTENT:
        outcome = DISTRIBUTED_STANDING_POSTURE_BLOCKED
        block_code = "DISTRIBUTED_STANDING_REQUEST_EXPLICITLY_BLOCKED"
    elif question.get("distributed_standing_intent") == DO_NOT_RECORD_INTENT:
        outcome = DISTRIBUTED_STANDING_POSTURE_NOT_RECORDED
        block_code = None
    elif requested_posture == DISTRIBUTED_STANDING_POSTURE_BLOCKED:
        outcome = DISTRIBUTED_STANDING_POSTURE_BLOCKED
        block_code = "DISTRIBUTED_STANDING_REQUEST_EXPLICITLY_BLOCKED"
    elif requested_posture in SUPPORTED_DISTRIBUTED_STANDING_POSTURES:
        outcome = requested_posture
        block_code = None
    else:
        outcome = DISTRIBUTED_STANDING_POSTURE_BLOCKED
        block_code = "DISTRIBUTED_STANDING_POSTURE_UNSUPPORTED"

    block = {
        "blocked": outcome == DISTRIBUTED_STANDING_POSTURE_BLOCKED,
        "code": block_code,
        "reason": _block_reason(block_code),
        "block_code": block_code,
        "block_reason": _block_reason(block_code),
    }
    statement = _distributed_standing_statement(
        normalized_request,
        outcome,
        body_posture,
        carrier_evidence,
        standing_basis,
        source_lineage,
        receipt_basis,
        divergence_basis,
        divergence_consequence_basis,
        currentness_successor_basis,
        continuity_basis,
        standing_propagation_basis,
        registry_basis,
        lifecycle_basis,
        relation_basis,
        current_body_closure_basis,
        visibility,
    )
    result: dict[str, Any] = {
        "distributed_standing_metadata": _metadata(question, posture, outcome),
        "declared_distributed_standing_question": question,
        "selected_body_side_standing_posture": body_posture,
        "selected_carrier_evidence": carrier_evidence,
        "source_body_lineage": source_lineage,
        "receipt_refusal_admission_basis": receipt_basis,
        "divergence_basis": divergence_basis,
        "divergence_consequence_basis": divergence_consequence_basis,
        "currentness_successor_basis": currentness_successor_basis,
        "carrier_continuity_turn_basis": continuity_basis,
        "standing_propagation_basis": standing_propagation_basis,
        "registry_persistence_basis": registry_basis,
        "lifecycle_basis": lifecycle_basis,
        "relation_conformance_closure_basis": relation_basis,
        "current_body_conformance_v3_closure_basis": current_body_closure_basis,
        "distributed_standing_posture": posture,
        "distributed_standing_checks": checks,
        "distributed_standing_statement": statement,
        "distributed_standing_non_meaning": copy.deepcopy(
            DISTRIBUTED_STANDING_NON_MEANING
        ),
        "what_remains_open": copy.deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    result["distributed_standing_summary"] = build_distributed_standing_summary(result)
    return result


def _declared_distributed_standing_question(
    request: Mapping[str, Any],
    request_path: Path | None,
) -> dict[str, Any]:
    section = _as_mapping(request.get("declared_distributed_standing_question"))
    raw_intent = (
        request.get("distributed_standing_intent")
        or section.get("distributed_standing_intent")
    )
    intent = _normalize_token(raw_intent)
    declared_non_claims = _as_mapping(
        request.get("declared_non_claims")
        or request.get("non_claims")
        or section.get("declared_non_claims")
    )
    return {
        "distributed_standing_request_id": request.get(
            "distributed_standing_request_id"
        )
        or section.get("distributed_standing_request_id"),
        "distributed_standing_question": request.get("distributed_standing_question")
        or section.get("distributed_standing_question"),
        "distributed_standing_intent": intent,
        "raw_distributed_standing_intent": raw_intent,
        "request_path": _display_path(request_path) or section.get("request_path"),
        "not_recorded_reason": request.get("not_recorded_reason")
        or section.get("not_recorded_reason")
        or (
            "declared request does not record distributed standing boundary posture"
            if intent == DO_NOT_RECORD_INTENT
            else None
        ),
        "declared_non_claims": declared_non_claims,
        "distributed_standing_is_not_synchronization": True,
        "distributed_standing_is_not_distributed_currentness": True,
        "distributed_standing_is_not_carrier_majority": True,
        "distributed_standing_is_not_successful_receipt_count": True,
        "distributed_standing_is_not_registry_presence": True,
        "distributed_standing_is_not_latest_file": True,
        "distributed_standing_is_not_carrier_availability": True,
        "distributed_standing_is_not_body_transfer": True,
        "distributed_standing_is_not_second_body": True,
        "distributed_standing_is_not_carrier_sovereignty": True,
        "distributed_standing_is_not_current_carrier_selection": True,
        "distributed_standing_is_not_winner_loser_selection": True,
        "distributed_standing_is_not_action": True,
        "distributed_standing_is_not_truth": True,
    }


def _selected_body_side_standing_posture_section(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    raw = request.get("selected_body_side_standing_posture")
    declared = raw is not None
    parseable = isinstance(raw, Mapping) or isinstance(raw, str)
    posture_id = _extract_identity(raw)
    posture_outcome = _entry_outcome(raw)
    posture_kind = _field_from_mapping(
        raw,
        (
            "selected_body_side_standing_posture",
            "body_side_standing_posture",
            "standing_posture",
            "posture",
            "type",
        ),
    )
    if isinstance(raw, str) and not posture_id:
        posture_id = raw
        posture_kind = raw
    return {
        "selected_body_side_standing_posture_declared": declared,
        "selected_body_side_standing_posture_parseable": parseable if declared else False,
        "selected_body_side_standing_posture_id": posture_id,
        "selected_body_side_standing_posture_outcome": posture_outcome,
        "selected_body_side_standing_posture_kind": posture_kind,
        "raw_selected_body_side_standing_posture": copy.deepcopy(raw),
        "body_side_standing_posture_preserved": declared and parseable,
        "body_side_posture_remains_body_side": True,
        "body_side_posture_is_not_held_by_carrier": True,
        "body_side_posture_does_not_select_current_carrier": True,
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
        and parseable
        and all(_nonempty(value) for value in evidence_ids)
        and all(_nonempty(value) for value in evidence_outcomes),
        "carrier_evidence_remains_evidence": True,
        "carrier_evidence_does_not_become_source": True,
        "carrier_evidence_does_not_become_currentness": True,
        "carrier_evidence_does_not_select_winner_or_loser": True,
    }


def _distributed_standing_posture_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = (
        request.get("requested_distributed_standing_posture")
        or _field_from_mapping(
            request.get("distributed_standing_posture"),
            (
                "requested_distributed_standing_posture",
                "distributed_standing_posture",
                "posture",
            ),
        )
    )
    posture = _normalize_token(raw)
    return {
        "requested_distributed_standing_posture": posture,
        "raw_requested_distributed_standing_posture": raw,
        "distributed_standing_posture_supported": posture
        in SUPPORTED_DISTRIBUTED_STANDING_POSTURES,
        "supported_distributed_standing_postures": sorted(
            SUPPORTED_DISTRIBUTED_STANDING_POSTURES
        ),
        "distributed_standing_posture_preserved": posture
        in SUPPORTED_DISTRIBUTED_STANDING_POSTURES,
        "posture_is_bounded_body_side_standing_posture": True,
        "posture_is_not_repository_synchronization": True,
        "posture_is_not_full_body_transfer": True,
        "posture_is_not_distributed_operation": True,
    }


def _distributed_standing_basis_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("distributed_standing_basis")
    raw_mapping = _as_mapping(raw)
    return {
        "distributed_standing_basis_declared": _basis_declared(raw),
        "distributed_standing_basis_preserved": _basis_declared(raw),
        "distributed_standing_basis_id": _extract_identity(raw),
        "raw_distributed_standing_basis": copy.deepcopy(raw),
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
        "distributed_standing_basis_is_not_sync": True,
        "distributed_standing_basis_does_not_select_carrier": True,
        "distributed_standing_basis_does_not_replace_source": True,
    }


def _basis_section(
    request: Mapping[str, Any],
    key: str,
    section_name: str,
    required_keys: Sequence[str],
    *,
    required_default: bool = False,
) -> dict[str, Any]:
    raw = request.get(key)
    nested = _as_mapping(request.get(section_name))
    if raw is None and nested:
        raw = nested.get(f"raw_{section_name}") or nested
    declared = _basis_declared(raw)
    required = required_default or _basis_required(request, required_keys) or any(
        _is_true(nested.get(required_key)) for required_key in required_keys
    )
    return {
        f"{section_name}_declared": declared,
        f"{section_name}_required": required,
        f"{section_name}_preserved": declared,
        f"{section_name}_id": _extract_identity(raw),
        f"raw_{section_name}": copy.deepcopy(raw),
        "basis_preserved_where_supplied_or_required": bool(not required or declared),
        "basis_is_prerequisite_only": True,
        "basis_does_not_decide_distributed_standing_by_itself": True,
        "basis_does_not_authorize_sync_or_operation": True,
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
    non_claims["raw_declared_non_claims"] = copy.deepcopy(declared)
    return non_claims


def _visibility_projection(
    request: Mapping[str, Any],
    carrier_evidence: Mapping[str, Any],
    standing_basis: Mapping[str, Any],
    source_lineage: Mapping[str, Any],
    receipt_basis: Mapping[str, Any],
    divergence_basis: Mapping[str, Any],
    divergence_consequence_basis: Mapping[str, Any],
    currentness_successor_basis: Mapping[str, Any],
    continuity_basis: Mapping[str, Any],
    standing_propagation_basis: Mapping[str, Any],
    registry_basis: Mapping[str, Any],
    lifecycle_basis: Mapping[str, Any],
    relation_basis: Mapping[str, Any],
    current_body_closure_basis: Mapping[str, Any],
    non_claims: Mapping[str, Any],
) -> dict[str, bool]:
    evidence_entries = carrier_evidence.get("selected_carrier_evidence_entries") or []
    sources = [
        standing_basis.get("raw_distributed_standing_basis"),
        source_lineage.get("raw_source_body_lineage"),
        receipt_basis.get("raw_receipt_refusal_admission_basis"),
        divergence_basis.get("raw_divergence_basis"),
        divergence_consequence_basis.get("raw_divergence_consequence_basis"),
        currentness_successor_basis.get("raw_currentness_successor_basis"),
        continuity_basis.get("raw_carrier_continuity_turn_basis"),
        standing_propagation_basis.get("raw_standing_propagation_basis"),
        registry_basis.get("raw_registry_persistence_basis"),
        lifecycle_basis.get("raw_lifecycle_basis"),
        relation_basis.get("raw_relation_conformance_closure_basis"),
        current_body_closure_basis.get(
            "raw_current_body_conformance_v3_closure_basis"
        ),
        carrier_evidence.get("raw_selected_carrier_evidence"),
    ]

    refusal_hidden = _recursive_true(
        [request, non_claims],
        (
            "distributed_standing_hid_refusal",
            "distributed_standing_hides_refusal",
            "visible_refusal_hidden",
            "refusal_hidden",
            "hides_refusal",
        ),
    )
    refusal_preserved = bool(
        not refusal_hidden
        and (
            _basis_declared(request.get("visible_refusal_basis"))
            or _recursive_true(
                sources,
                (
                    "visible_refusal_preserved",
                    "visible_refusal_visible",
                    "refusal_preserved",
                    "refusal_remains_visible",
                ),
            )
            or _entries_have_token(evidence_entries, ("refusal", "refused", "blocked"))
        )
    )

    divergence_hidden = _recursive_true(
        [request, non_claims],
        (
            "distributed_standing_hid_divergence",
            "distributed_standing_hides_divergence",
            "visible_divergence_hidden",
            "divergence_hidden",
            "hides_divergence",
        ),
    )
    divergence_preserved = bool(
        not divergence_hidden
        and (
            _basis_declared(request.get("visible_divergence_basis"))
            or _recursive_true(
                sources,
                (
                    "visible_divergence_preserved",
                    "visible_divergence_visible",
                    "divergence_preserved",
                    "divergence_remains_visible",
                ),
            )
            or _entries_have_token(evidence_entries, ("divergence", "mismatch"))
            or _entries_have_outcome(evidence_entries, ("CARRIER_DIVERGENCE_RECORDED",))
        )
    )

    blocked_hidden = _recursive_true(
        [request, non_claims],
        (
            "distributed_standing_hid_blocked_attempt",
            "distributed_standing_hides_blocked_attempt",
            "blocked_attempt_hidden",
            "blocked_attempts_hidden",
        ),
    )
    blocked_preserved = bool(
        not blocked_hidden
        and (
            _basis_declared(request.get("blocked_attempt_basis"))
            or _recursive_true(
                sources,
                (
                    "blocked_attempts_preserved",
                    "blocked_attempt_preserved",
                    "blocked_attempt_remains_visible",
                ),
            )
            or _entries_have_token(evidence_entries, ("blocked", "block"))
        )
    )

    projection_hidden = _recursive_true(
        [request, non_claims],
        (
            "distributed_standing_hid_projection_mismatch",
            "distributed_standing_hides_projection_mismatch",
            "projection_mismatch_hidden",
            "hides_projection_mismatch",
        ),
    )
    projection_preserved = bool(
        not projection_hidden
        and (
            _basis_declared(request.get("projection_mismatch_basis"))
            or _recursive_true(
                sources,
                (
                    "projection_mismatch_preserved",
                    "projection_mismatch_visible",
                    "projection_mismatch_remains_visible",
                ),
            )
            or bool(
                standing_basis.get("detailed_basis_reference")
                and standing_basis.get("summary_projection_reference")
            )
        )
    )

    detailed_distinguished = bool(
        _recursive_true(
            sources,
            (
                "detailed_basis_distinguished_from_summary",
                "detailed_basis_distinguishable_from_summary",
                "detailed_basis_preserved_over_summary",
            ),
        )
        or bool(
            standing_basis.get("detailed_basis_reference")
            and standing_basis.get("summary_projection_reference")
        )
    )
    summary_overrode = _recursive_true(
        [request, non_claims] + sources,
        ("summary_overrode_detailed_basis", "summary_overwrites_detailed_basis"),
    )
    return {
        "visible_refusal_preserved": refusal_preserved,
        "visible_refusal_hidden": refusal_hidden,
        "visible_divergence_preserved": divergence_preserved,
        "visible_divergence_hidden": divergence_hidden,
        "blocked_attempts_preserved": blocked_preserved,
        "blocked_attempts_hidden": blocked_hidden,
        "projection_mismatch_preserved": projection_preserved,
        "projection_mismatch_hidden": projection_hidden,
        "detailed_basis_distinguished_from_summary": detailed_distinguished,
        "summary_overrode_detailed_basis": summary_overrode,
    }


def _build_checks(
    request: Mapping[str, Any],
    question: Mapping[str, Any],
    body_posture: Mapping[str, Any],
    carrier_evidence: Mapping[str, Any],
    posture: Mapping[str, Any],
    standing_basis: Mapping[str, Any],
    source_lineage: Mapping[str, Any],
    receipt_basis: Mapping[str, Any],
    divergence_basis: Mapping[str, Any],
    divergence_consequence_basis: Mapping[str, Any],
    currentness_successor_basis: Mapping[str, Any],
    continuity_basis: Mapping[str, Any],
    standing_propagation_basis: Mapping[str, Any],
    registry_basis: Mapping[str, Any],
    lifecycle_basis: Mapping[str, Any],
    relation_basis: Mapping[str, Any],
    current_body_closure_basis: Mapping[str, Any],
    non_claims: Mapping[str, Any],
    visibility: Mapping[str, bool],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for failure in precheck_failures:
        checks.append(
            _make_check(
                "declared_distributed_standing_request_parseable",
                False,
                "declared distributed standing request is a mapping",
                failure,
                failure,
            )
        )

    checks.extend(
        [
            _make_check(
                "distributed_standing_question_declared",
                _nonempty(question.get("distributed_standing_question")),
                "distributed standing question declared",
                question.get("distributed_standing_question"),
                "DISTRIBUTED_STANDING_QUESTION_UNDECLARED",
            ),
            _make_check(
                "distributed_standing_intent_supported",
                question.get("distributed_standing_intent")
                in SUPPORTED_DISTRIBUTED_STANDING_INTENTS,
                "supported distributed standing intent",
                question.get("distributed_standing_intent"),
                "DISTRIBUTED_STANDING_INTENT_UNSUPPORTED",
            ),
            _make_check(
                "selected_body_side_standing_posture_present",
                bool(body_posture.get("body_side_standing_posture_preserved")),
                "selected body-side standing posture present",
                body_posture.get("raw_selected_body_side_standing_posture"),
                "BODY_SIDE_STANDING_POSTURE_MISSING",
            ),
            _make_check(
                "selected_carrier_evidence_present",
                bool(carrier_evidence.get("selected_carrier_evidence_declared")),
                "selected carrier evidence present",
                carrier_evidence.get("raw_selected_carrier_evidence"),
                "SELECTED_CARRIER_EVIDENCE_MISSING",
            ),
            _make_check(
                "selected_carrier_evidence_parseable",
                bool(carrier_evidence.get("selected_carrier_evidence_parseable")),
                "selected carrier evidence parseable",
                carrier_evidence.get("raw_selected_carrier_evidence"),
                "SELECTED_CARRIER_EVIDENCE_MALFORMED",
            ),
            _make_check(
                "selected_carrier_evidence_identities_present",
                bool(
                    carrier_evidence.get(
                        "selected_carrier_evidence_identities_preserved"
                    )
                ),
                "selected carrier evidence identities present",
                carrier_evidence.get("selected_carrier_evidence_ids"),
                "SELECTED_CARRIER_EVIDENCE_IDENTITY_OR_OUTCOME_MISSING",
            ),
            _make_check(
                "selected_carrier_evidence_outcomes_present",
                bool(
                    carrier_evidence.get(
                        "selected_carrier_evidence_outcomes_preserved"
                    )
                ),
                "selected carrier evidence outcomes present",
                carrier_evidence.get("selected_carrier_evidence_outcomes"),
                "SELECTED_CARRIER_EVIDENCE_IDENTITY_OR_OUTCOME_MISSING",
            ),
            _make_check(
                "distributed_standing_posture_supported",
                bool(posture.get("distributed_standing_posture_supported")),
                "supported distributed standing posture",
                posture.get("requested_distributed_standing_posture"),
                "DISTRIBUTED_STANDING_POSTURE_UNSUPPORTED",
            ),
            _make_check(
                "distributed_standing_basis_declared",
                bool(standing_basis.get("distributed_standing_basis_declared")),
                "distributed standing basis declared",
                standing_basis.get("raw_distributed_standing_basis"),
                "DISTRIBUTED_STANDING_BASIS_MISSING",
            ),
            _make_check(
                "source_body_lineage_preserved",
                bool(source_lineage.get("source_body_lineage_preserved")),
                "source-body lineage preserved",
                source_lineage.get("raw_source_body_lineage"),
                "SOURCE_BODY_LINEAGE_MISSING",
            ),
            _make_check(
                "receipt_refusal_admission_basis_preserved_where_required_or_supplied",
                _basis_ok(receipt_basis, "receipt_refusal_admission_basis"),
                "receipt/refusal/admission basis preserved where supplied or required",
                receipt_basis.get("raw_receipt_refusal_admission_basis"),
                "DISTRIBUTED_STANDING_BASIS_MISSING",
            ),
            _make_check(
                "divergence_basis_preserved_where_required_or_supplied",
                _basis_ok(divergence_basis, "divergence_basis"),
                "divergence basis preserved where supplied or required",
                divergence_basis.get("raw_divergence_basis"),
                "DISTRIBUTED_STANDING_BASIS_MISSING",
            ),
            _make_check(
                "divergence_consequence_basis_preserved",
                bool(
                    divergence_consequence_basis.get(
                        "divergence_consequence_basis_preserved"
                    )
                ),
                "divergence consequence basis preserved",
                divergence_consequence_basis.get("raw_divergence_consequence_basis"),
                "DIVERGENCE_CONSEQUENCE_BASIS_MISSING",
            ),
            _make_check(
                "currentness_successor_basis_preserved",
                bool(
                    currentness_successor_basis.get(
                        "currentness_successor_basis_preserved"
                    )
                ),
                "currentness successor basis preserved",
                currentness_successor_basis.get("raw_currentness_successor_basis"),
                "CURRENTNESS_SUCCESSOR_BASIS_MISSING",
            ),
            _make_check(
                "continuity_turn_basis_preserved",
                bool(continuity_basis.get("carrier_continuity_turn_basis_preserved")),
                "carrier continuity-turn basis preserved",
                continuity_basis.get("raw_carrier_continuity_turn_basis"),
                "CARRIER_CONTINUITY_TURN_BASIS_MISSING",
            ),
            _make_check(
                "standing_propagation_basis_preserved",
                bool(
                    standing_propagation_basis.get(
                        "standing_propagation_basis_preserved"
                    )
                ),
                "standing propagation basis preserved",
                standing_propagation_basis.get("raw_standing_propagation_basis"),
                "STANDING_PROPAGATION_BASIS_MISSING",
            ),
            _make_check(
                "registry_persistence_basis_preserved",
                bool(registry_basis.get("registry_persistence_basis_preserved")),
                "registry/persistence basis preserved",
                registry_basis.get("raw_registry_persistence_basis"),
                "REGISTRY_PERSISTENCE_BASIS_MISSING",
            ),
            _make_check(
                "lifecycle_basis_preserved",
                bool(lifecycle_basis.get("lifecycle_basis_preserved")),
                "lifecycle basis preserved",
                lifecycle_basis.get("raw_lifecycle_basis"),
                "LIFECYCLE_BASIS_MISSING",
            ),
            _make_check(
                "relation_conformance_closure_basis_preserved_where_required_or_supplied",
                _basis_ok(relation_basis, "relation_conformance_closure_basis"),
                "relation/conformance/closure basis preserved where supplied or required",
                relation_basis.get("raw_relation_conformance_closure_basis"),
                "RELATION_CONFORMANCE_CLOSURE_BASIS_MISSING",
            ),
            _make_check(
                "current_body_conformance_v3_closure_basis_preserved",
                bool(
                    current_body_closure_basis.get(
                        "current_body_conformance_v3_closure_basis_preserved"
                    )
                ),
                "current-body conformance v3 closure basis preserved",
                current_body_closure_basis.get(
                    "raw_current_body_conformance_v3_closure_basis"
                ),
                "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BASIS_MISSING",
            ),
            _make_check(
                "visible_refusal_preserved",
                bool(visibility.get("visible_refusal_preserved")),
                "visible refusal remains visible",
                visibility.get("visible_refusal_preserved"),
                "DISTRIBUTED_STANDING_HIDES_REFUSAL",
            ),
            _make_check(
                "visible_divergence_preserved",
                bool(visibility.get("visible_divergence_preserved")),
                "visible divergence remains visible",
                visibility.get("visible_divergence_preserved"),
                "DISTRIBUTED_STANDING_HIDES_DIVERGENCE",
            ),
            _make_check(
                "blocked_attempts_preserved",
                bool(visibility.get("blocked_attempts_preserved")),
                "blocked attempts remain visible",
                visibility.get("blocked_attempts_preserved"),
                "DISTRIBUTED_STANDING_HIDES_BLOCKED_ATTEMPT",
            ),
            _make_check(
                "projection_mismatch_preserved",
                bool(visibility.get("projection_mismatch_preserved")),
                "projection mismatch remains visible",
                visibility.get("projection_mismatch_preserved"),
                "DISTRIBUTED_STANDING_HIDES_PROJECTION_MISMATCH",
            ),
            _make_check(
                "detailed_basis_distinguishable_from_summary",
                bool(visibility.get("detailed_basis_distinguished_from_summary")),
                "detailed basis distinguishable from summary",
                visibility.get("detailed_basis_distinguished_from_summary"),
                "SUMMARY_OVERWRITES_DETAILED_BASIS",
            ),
            _make_check(
                "summary_does_not_override_detailed_basis",
                not bool(visibility.get("summary_overrode_detailed_basis")),
                "summary does not override detailed basis",
                visibility.get("summary_overrode_detailed_basis"),
                "SUMMARY_OVERWRITES_DETAILED_BASIS",
            ),
        ]
    )

    collapse_sources = [request, non_claims]
    checks.extend(
        [
            _anti_check(
                "no_carrier_currentness",
                collapse_sources,
                ("carrier_currentness_created", "distributed_standing_creates_carrier_currentness"),
                "no carrier currentness",
                "DISTRIBUTED_STANDING_CREATES_CARRIER_CURRENTNESS",
            ),
            _anti_check(
                "no_current_carrier_selected",
                collapse_sources,
                ("current_carrier_selected", "distributed_standing_selects_current_carrier"),
                "no current carrier selected",
                "DISTRIBUTED_STANDING_SELECTS_CURRENT_CARRIER",
            ),
            _anti_check(
                "no_winning_carrier_selected",
                collapse_sources,
                ("winning_carrier_selected", "distributed_standing_selects_winning_carrier"),
                "no winning carrier selected",
                "DISTRIBUTED_STANDING_SELECTS_WINNING_CARRIER",
            ),
            _anti_check(
                "no_losing_carrier_invalidated",
                collapse_sources,
                ("losing_carrier_invalidated", "distributed_standing_invalidates_losing_carrier"),
                "no losing carrier invalidated",
                "DISTRIBUTED_STANDING_INVALIDATES_LOSING_CARRIER",
            ),
            _anti_check(
                "no_source_replacement",
                collapse_sources,
                ("source_replaced", "distributed_standing_replaces_source"),
                "no source replacement",
                "DISTRIBUTED_STANDING_REPLACES_SOURCE",
            ),
            _anti_check(
                "no_authority",
                collapse_sources,
                ("authority_created", "distributed_standing_creates_authority"),
                "no authority",
                "DISTRIBUTED_STANDING_CREATES_AUTHORITY",
            ),
            _anti_check(
                "no_permission",
                collapse_sources,
                ("permission_created", "distributed_standing_creates_permission"),
                "no permission",
                "DISTRIBUTED_STANDING_CREATES_PERMISSION",
            ),
            _anti_check(
                "no_truth",
                collapse_sources,
                ("truth_created", "distributed_standing_creates_truth"),
                "no truth",
                "DISTRIBUTED_STANDING_CREATES_TRUTH",
            ),
            _anti_check(
                "no_action",
                collapse_sources,
                ("action_authorized", "distributed_standing_authorizes_action"),
                "no action",
                "DISTRIBUTED_STANDING_AUTHORIZES_ACTION",
            ),
            _anti_check(
                "no_divergence_resolution",
                collapse_sources,
                ("divergence_resolved", "distributed_standing_resolves_divergence"),
                "no divergence resolution",
                "DISTRIBUTED_STANDING_RESOLVES_DIVERGENCE",
            ),
            _anti_check(
                "no_evidence_erasure",
                collapse_sources,
                ("distributed_standing_erased_evidence", "evidence_erased"),
                "no evidence erasure",
                "DISTRIBUTED_STANDING_ERASES_EVIDENCE",
            ),
            _anti_check(
                "no_repository_sync",
                collapse_sources,
                (
                    "repository_synchronization_authorized",
                    "distributed_standing_authorized_sync",
                ),
                "no repository sync",
                "DISTRIBUTED_STANDING_AUTHORIZES_REPOSITORY_SYNC",
            ),
            _anti_check(
                "no_full_body_transfer",
                collapse_sources,
                (
                    "full_body_transfer_authorized",
                    "distributed_standing_authorized_full_body_transfer",
                ),
                "no full body transfer",
                "DISTRIBUTED_STANDING_AUTHORIZES_FULL_BODY_TRANSFER",
            ),
            _anti_check(
                "no_second_body",
                collapse_sources,
                ("second_body_created", "distributed_standing_created_second_body"),
                "no second body",
                "DISTRIBUTED_STANDING_CREATES_SECOND_BODY",
            ),
            _anti_check(
                "no_continuation",
                collapse_sources,
                (
                    "continuation_authorized",
                    "distributed_standing_authorized_continuation",
                ),
                "no continuation",
                "DISTRIBUTED_STANDING_AUTHORIZES_CONTINUATION",
            ),
            _anti_check(
                "no_distributed_operation",
                collapse_sources,
                (
                    "distributed_operation_authorized",
                    "distributed_standing_authorized_distributed_operation",
                ),
                "no distributed operation",
                "DISTRIBUTED_STANDING_AUTHORIZES_DISTRIBUTED_OPERATION",
            ),
            _anti_check(
                "no_latest_file_turn_standing",
                collapse_sources,
                ("latest_file_standing", "latest_turn_standing"),
                "no latest-file or latest-turn standing",
                "LATEST_FILE_OR_TURN_STANDING",
            ),
            _anti_check(
                "no_majority_success_count_standing",
                collapse_sources,
                ("majority_carrier_standing", "successful_receipt_count_standing"),
                "no majority or success-count standing",
                "MAJORITY_OR_SUCCESS_COUNT_STANDING",
            ),
            _anti_check(
                "no_registry_lifecycle_propagation_turn_currentness_or_consequence_standing",
                collapse_sources,
                (
                    "registry_record_standing",
                    "lifecycle_status_standing",
                    "standing_propagation_standing",
                    "continuity_turn_standing",
                    "currentness_successor_standing",
                    "divergence_consequence_standing",
                    "availability_standing",
                ),
                "no prerequisite surface decides standing by itself",
                "REGISTRY_LIFECYCLE_PROPAGATION_TURN_CURRENTNESS_OR_CONSEQUENCE_STANDING",
            ),
            _anti_check(
                "no_mutation_replay_merge",
                collapse_sources,
                ("mutation_performed", "replay_performed", "merge_performed"),
                "no mutation, replay, or merge",
                "MUTATION_REPLAY_OR_MERGE_DETECTED",
            ),
            _make_check(
                "non_claims_remain_false",
                bool(non_claims.get("required_non_claims_preserved")),
                "required non-claims remain false",
                {
                    "missing": non_claims.get("missing_required_non_claims"),
                    "flipped": non_claims.get("flipped_required_non_claims"),
                },
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        ]
    )
    return checks


def _distributed_standing_statement(
    request: Mapping[str, Any],
    outcome: str,
    body_posture: Mapping[str, Any],
    carrier_evidence: Mapping[str, Any],
    standing_basis: Mapping[str, Any],
    source_lineage: Mapping[str, Any],
    receipt_basis: Mapping[str, Any],
    divergence_basis: Mapping[str, Any],
    divergence_consequence_basis: Mapping[str, Any],
    currentness_successor_basis: Mapping[str, Any],
    continuity_basis: Mapping[str, Any],
    standing_propagation_basis: Mapping[str, Any],
    registry_basis: Mapping[str, Any],
    lifecycle_basis: Mapping[str, Any],
    relation_basis: Mapping[str, Any],
    current_body_closure_basis: Mapping[str, Any],
    visibility: Mapping[str, bool],
) -> dict[str, Any]:
    statement = {
        "distributed_standing_posture_recorded": outcome
        == DISTRIBUTED_STANDING_POSTURE_RECORDED,
        "body_side_standing_posture_preserved": bool(
            body_posture.get("body_side_standing_posture_preserved")
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
        "source_body_lineage_preserved": bool(
            source_lineage.get("source_body_lineage_preserved")
        ),
        "receipt_refusal_admission_basis_preserved": bool(
            receipt_basis.get("receipt_refusal_admission_basis_preserved")
        ),
        "divergence_basis_preserved": bool(
            divergence_basis.get("divergence_basis_preserved")
        ),
        "divergence_consequence_basis_preserved": bool(
            divergence_consequence_basis.get("divergence_consequence_basis_preserved")
        ),
        "currentness_successor_basis_preserved": bool(
            currentness_successor_basis.get("currentness_successor_basis_preserved")
        ),
        "carrier_continuity_turn_basis_preserved": bool(
            continuity_basis.get("carrier_continuity_turn_basis_preserved")
        ),
        "standing_propagation_basis_preserved": bool(
            standing_propagation_basis.get("standing_propagation_basis_preserved")
        ),
        "registry_persistence_basis_preserved": bool(
            registry_basis.get("registry_persistence_basis_preserved")
        ),
        "lifecycle_basis_preserved": bool(
            lifecycle_basis.get("lifecycle_basis_preserved")
        ),
        "relation_conformance_closure_basis_preserved": bool(
            relation_basis.get("relation_conformance_closure_basis_preserved")
        ),
        "current_body_conformance_v3_closure_basis_preserved": bool(
            current_body_closure_basis.get(
                "current_body_conformance_v3_closure_basis_preserved"
            )
        ),
        "visible_refusal_preserved": bool(visibility.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(
            visibility.get("visible_divergence_preserved")
        ),
        "blocked_attempts_preserved": bool(
            visibility.get("blocked_attempts_preserved")
        ),
        "projection_mismatch_preserved": bool(
            visibility.get("projection_mismatch_preserved")
        ),
        "detailed_basis_distinguished_from_summary": bool(
            visibility.get("detailed_basis_distinguished_from_summary")
        ),
        "summary_overrode_detailed_basis": False,
        "carrier_currentness_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "source_replaced": False,
        "currentness_created": False,
        "authority_created": False,
        "permission_created": False,
        "truth_created": False,
        "action_authorized": False,
        "divergence_resolved": False,
        "evidence_erased": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
        "latest_file_standing": False,
        "latest_turn_standing": False,
        "majority_carrier_standing": False,
        "successful_receipt_count_standing": False,
        "additional_basis_explanation": None,
        "excluded_declared_scope": None,
        "exclusion_reason": None,
        "revalidation_reason": None,
        "revalidation_scheduled": False,
        "revalidation_authorized": False,
        "separate_review_reason": None,
        "separate_review_scheduled": False,
        "separate_review_authorized": False,
    }
    if outcome == DISTRIBUTED_STANDING_POSTURE_NOT_RECORDED:
        statement["not_recorded_reason"] = (
            request.get("not_recorded_reason")
            or "declared request does not record distributed standing boundary posture"
        )
    if outcome == DISTRIBUTED_STANDING_REQUIRES_ADDITIONAL_BASIS:
        statement["additional_basis_explanation"] = request.get(
            "required_additional_basis_explanation"
        ) or "distributed standing requires additional declared basis before posture recording"
        statement["additional_basis_scheduled"] = False
        statement["additional_basis_authorized"] = False
    if outcome == DISTRIBUTED_STANDING_EXCLUDED_FOR_DECLARED_SCOPE:
        statement["excluded_declared_scope"] = request.get("declared_scope")
        statement["exclusion_reason"] = request.get(
            "exclusion_reason"
        ) or "distributed standing is excluded only for the declared scope"
        statement["exclusion_generalized_beyond_declared_scope"] = False
    if outcome == DISTRIBUTED_STANDING_REQUIRES_REVALIDATION:
        statement["revalidation_reason"] = request.get(
            "revalidation_reason"
        ) or "distributed standing requires bounded revalidation before review"
    if outcome == DISTRIBUTED_STANDING_REQUIRES_SEPARATE_REVIEW:
        statement["separate_review_reason"] = request.get(
            "separate_review_reason"
        ) or "distributed standing requires a separate bounded review before review"
    return statement


def _metadata(
    question: Mapping[str, Any],
    posture: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    generated_at = _utc_now()
    basis_id = (
        question.get("distributed_standing_request_id")
        or posture.get("requested_distributed_standing_posture")
        or "distributed_standing"
    )
    return {
        "distributed_standing_result_id": (
            f"{basis_id}__{outcome.lower()}__{generated_at}"
        ),
        "distributed_standing_result_type": RESULT_TYPE,
        "distributed_standing_result_version": RESULT_VERSION,
        "generated_at": generated_at,
        "resolver_module": RESOLVER_MODULE,
    }


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
        "actual_posture": copy.deepcopy(actual_posture),
        "block_code": None if passed else block_code,
    }


def _anti_check(
    check_name: str,
    sources: Sequence[Any],
    keys: Sequence[str],
    expected_posture: str,
    block_code: str,
) -> dict[str, Any]:
    detected = _recursive_true(sources, keys)
    return _make_check(check_name, not detected, expected_posture, detected, block_code)


def _basis_ok(section: Mapping[str, Any], section_name: str) -> bool:
    required = bool(section.get(f"{section_name}_required"))
    declared = bool(section.get(f"{section_name}_declared"))
    preserved = bool(section.get(f"{section_name}_preserved"))
    return (not required and not declared) or (declared and preserved)


def _read_json_mapping(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise DistributedStandingBoundaryError(
            "DECLARED_DISTRIBUTED_STANDING_REQUEST_UNREADABLE",
            f"Declared distributed standing request path could not be read: {path}",
        ) from exc
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise DistributedStandingBoundaryError(
            "DECLARED_DISTRIBUTED_STANDING_REQUEST_MALFORMED",
            f"Declared distributed standing request JSON is malformed: {path}",
        ) from exc
    if not isinstance(parsed, Mapping):
        raise DistributedStandingBoundaryError(
            "DECLARED_DISTRIBUTED_STANDING_REQUEST_MALFORMED",
            "Declared distributed standing request JSON must be an object.",
        )
    return copy.deepcopy(dict(parsed))


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]
    return []


def _entries_from_value(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, Mapping):
        return [copy.deepcopy(dict(value))]
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]
    return []


def _field_from_mapping(value: Any, keys: Sequence[str]) -> Any:
    if not isinstance(value, Mapping):
        return None
    for key in keys:
        found = value.get(key)
        if _nonempty(found):
            return copy.deepcopy(found)
    return None


def _extract_identity(value: Any) -> str | None:
    if isinstance(value, str):
        return value if value.strip() else None
    if not isinstance(value, Mapping):
        return None
    for key in IDENTITY_KEYS:
        found = value.get(key)
        if _nonempty(found):
            return str(found)
    for nested_key in (
        "metadata",
        "summary",
        "distributed_standing_metadata",
        "cross_carrier_currentness_successor_metadata",
        "divergence_consequence_metadata",
    ):
        nested = value.get(nested_key)
        if isinstance(nested, Mapping):
            found = _extract_identity(nested)
            if found:
                return found
    return None


def _entry_outcome(value: Any) -> str | None:
    if not isinstance(value, Mapping):
        return None
    for key in OUTCOME_KEYS:
        found = value.get(key)
        if _nonempty(found):
            return str(found)
    for nested_key in (
        "metadata",
        "summary",
        "distributed_standing_summary",
        "cross_carrier_currentness_successor_summary",
        "divergence_consequence_summary",
    ):
        nested = value.get(nested_key)
        if isinstance(nested, Mapping):
            found = _entry_outcome(nested)
            if found:
                return found
    return None


def _basis_declared(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return True


def _basis_required(request: Mapping[str, Any], keys: Sequence[str]) -> bool:
    return any(_is_true(request.get(key)) for key in keys)


def _first_declared(*values: Any) -> Any:
    for value in values:
        if _nonempty(value):
            return copy.deepcopy(value)
    return None


def _nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (Mapping, Sequence)) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        return bool(value)
    return value is not False


def _normalize_token(value: Any) -> str | None:
    if value is None:
        return None
    token = str(value).strip()
    return token.upper() if token else None


def _is_true(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1"}
    return False


def _recursive_true(value: Any, keys: Sequence[str]) -> bool:
    key_set = set(keys)
    if isinstance(value, Mapping):
        for key, item in value.items():
            if key in key_set and _is_true(item):
                return True
            if _recursive_true(item, keys):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_recursive_true(item, keys) for item in value)
    return False


def _entries_have_token(entries: Sequence[Mapping[str, Any]], tokens: Sequence[str]) -> bool:
    lowered_tokens = tuple(token.lower() for token in tokens)
    for entry in entries:
        text = json.dumps(entry, sort_keys=True, default=str).lower()
        if any(token in text for token in lowered_tokens):
            return True
    return False


def _entries_have_outcome(entries: Sequence[Mapping[str, Any]], outcomes: Sequence[str]) -> bool:
    outcome_set = set(outcomes)
    return any(_entry_outcome(entry) in outcome_set for entry in entries)


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
        "divergence_resolved",
        "truth_created",
        "action_authorized",
        "repository_synchronization_authorized",
        "full_body_transfer_authorized",
        "second_body_created",
        "continuation_authorized",
        "distributed_operation_authorized",
        "latest_file_standing",
        "latest_turn_standing",
        "majority_carrier_standing",
        "successful_receipt_count_standing",
        "registry_record_standing",
        "lifecycle_status_standing",
        "standing_propagation_standing",
        "continuity_turn_standing",
        "currentness_successor_standing",
        "divergence_consequence_standing",
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    )
    return {key: copy.deepcopy(non_claims.get(key)) for key in keys if key in non_claims}


def _block_reason(block_code: str | None) -> str | None:
    if block_code is None:
        return None
    return BLOCK_REASONS.get(block_code, block_code)


def _display_path(path: Path | None) -> str | None:
    if path is None:
        return None
    try:
        return str(path.resolve())
    except OSError:
        return str(path)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _safe_filename_part(value: Any) -> str:
    text = str(value or "distributed_standing").strip().lower()
    safe = []
    for character in text:
        if character.isalnum() or character in {"-", "_"}:
            safe.append(character)
        else:
            safe.append("_")
    filename = "".join(safe).strip("_")
    return filename or "distributed_standing"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def _default_basis(identifier: str, name: str, **flags: Any) -> dict[str, Any]:
    basis = {
        "basis_id": f"{identifier}__{name}",
        "basis_preserved": True,
        "basis_is_prerequisite_only": True,
        "basis_does_not_authorize_sync_or_operation": True,
    }
    basis.update(flags)
    return basis
