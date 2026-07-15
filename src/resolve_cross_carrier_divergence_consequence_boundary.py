"""Bounded cross-carrier divergence consequence boundary resolver.

This resolver records what visible divergence may lawfully require, limit,
block, exclude, or caution for one declared reliance or use question. It
preserves divergence consequence as bounded reliance effect only. It does not
resolve divergence, create truth, authorize action, create currentness, select
winners or losers, create authority, create permission, create carrier
hierarchy, erase evidence, create distributed standing, synchronize
repositories, authorize full body transfer, authorize continuation, or
authorize distributed operation.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CrossCarrierDivergenceConsequenceBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit consequence inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


REPO_ROOT = Path(__file__).resolve().parents[1]

CROSS_CARRIER_DIVERGENCE_CONSEQUENCE_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_cross_carrier_divergence_consequence_boundary"
)

RESOLVER_MODULE = "resolve_cross_carrier_divergence_consequence_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "cross_carrier_divergence_consequence_boundary_result"

RECORD_INTENT = "RECORD_DIVERGENCE_CONSEQUENCE"
DO_NOT_RECORD_INTENT = "DO_NOT_RECORD_DIVERGENCE_CONSEQUENCE"
BLOCK_INTENT = "BLOCK_DIVERGENCE_CONSEQUENCE"
SUPPORTED_DIVERGENCE_CONSEQUENCE_INTENTS = {
    RECORD_INTENT,
    DO_NOT_RECORD_INTENT,
    BLOCK_INTENT,
}

DIVERGENCE_CONSEQUENCE_RECORDED = "DIVERGENCE_CONSEQUENCE_RECORDED"
DIVERGENCE_CONSEQUENCE_NOT_RECORDED = "DIVERGENCE_CONSEQUENCE_NOT_RECORDED"
DIVERGENCE_CONSEQUENCE_BLOCKED = "DIVERGENCE_CONSEQUENCE_BLOCKED"

SUPPORTED_DIVERGENCE_CONSEQUENCE_POSTURES = {
    "DIVERGENCE_CONSEQUENCE_RECORDED",
    "DIVERGENCE_REQUIRES_CAUTION",
    "DIVERGENCE_LIMITS_RELIANCE",
    "DIVERGENCE_BLOCKS_SPECIFIC_RELIANCE",
    "DIVERGENCE_REQUIRES_REVALIDATION",
    "DIVERGENCE_REQUIRES_SEPARATE_REVIEW",
    "DIVERGENCE_EXCLUDES_EVIDENCE_FOR_DECLARED_USE",
    "DIVERGENCE_HAS_NO_CONSEQUENCE_FOR_DECLARED_USE",
    "DIVERGENCE_CONSEQUENCE_NOT_RECORDED",
    "DIVERGENCE_CONSEQUENCE_BLOCKED",
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
    "consequence_action_created": False,
    "divergence_consequence_created_source": False,
    "divergence_consequence_created_authority": False,
    "divergence_consequence_created_permission": False,
    "divergence_consequence_created_carrier_hierarchy": False,
    "divergence_consequence_created_distributed_standing": False,
    "divergence_consequence_erased_evidence": False,
    "divergence_consequence_hid_refusal": False,
    "divergence_consequence_hid_divergence": False,
    "divergence_consequence_hid_blocked_attempt": False,
    "divergence_consequence_hid_projection_mismatch": False,
    "summary_overrode_detailed_basis": False,
    "latest_file_consequence": False,
    "latest_turn_consequence": False,
    "majority_carrier_consequence": False,
    "successful_receipt_count_consequence": False,
    "registry_record_consequence": False,
    "lifecycle_status_consequence": False,
    "standing_propagation_consequence": False,
    "continuity_turn_consequence": False,
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
    "DECLARED_DIVERGENCE_CONSEQUENCE_REQUEST_UNREADABLE": "Declared divergence consequence request path could not be read.",
    "DECLARED_DIVERGENCE_CONSEQUENCE_REQUEST_MALFORMED": "Declared divergence consequence request is not a JSON object or mapping.",
    "DIVERGENCE_CONSEQUENCE_REQUEST_EXPLICITLY_BLOCKED": "Divergence consequence request explicitly declares a blocked posture.",
    "DIVERGENCE_CONSEQUENCE_QUESTION_UNDECLARED": "Divergence consequence question is undeclared.",
    "DIVERGENCE_CONSEQUENCE_INTENT_UNSUPPORTED": "Divergence consequence intent is unsupported.",
    "DIVERGENCE_CONSEQUENCE_POSTURE_UNSUPPORTED": "Divergence consequence posture is unsupported.",
    "RELIANCE_OR_USE_QUESTION_MISSING": "Declared reliance or use question is missing.",
    "SELECTED_DIVERGENCE_EVIDENCE_MISSING": "Selected divergence evidence is missing.",
    "SELECTED_DIVERGENCE_EVIDENCE_MALFORMED": "Selected divergence evidence is malformed.",
    "SELECTED_DIVERGENCE_EVIDENCE_OUTCOME_MISSING": "Selected divergence evidence outcome is missing.",
    "SELECTED_CARRIER_EVIDENCE_MISSING": "Selected carrier evidence is missing where required.",
    "DIVERGENCE_CONSEQUENCE_BASIS_MISSING": "Divergence consequence basis is missing.",
    "CURRENTNESS_SUCCESSOR_BASIS_MISSING": "Currentness successor basis is missing where required.",
    "CARRIER_CONTINUITY_TURN_BASIS_MISSING": "Carrier continuity-turn basis is missing where required.",
    "LIFECYCLE_REGISTRY_PROPAGATION_BASIS_MISSING": "Lifecycle, registry, or standing propagation basis is missing where required.",
    "RELATION_CONFORMANCE_CLOSURE_BASIS_MISSING": "Relation, conformance, or closure basis is missing where required.",
    "CONSEQUENCE_SCOPE_MISSING": "Consequence scope is missing.",
    "DIVERGENCE_CONSEQUENCE_HIDES_DIVERGENCE": "Divergence consequence hides visible divergence.",
    "DIVERGENCE_CONSEQUENCE_HIDES_REFUSAL": "Divergence consequence hides visible refusal.",
    "DIVERGENCE_CONSEQUENCE_HIDES_BLOCKED_ATTEMPT": "Divergence consequence hides a blocked attempt.",
    "DIVERGENCE_CONSEQUENCE_HIDES_PROJECTION_MISMATCH": "Divergence consequence hides projection mismatch.",
    "SUMMARY_OVERWRITES_DETAILED_BASIS": "Summary overwrites the detailed divergence consequence basis.",
    "DIVERGENCE_CONSEQUENCE_RESOLVES_DIVERGENCE": "Divergence consequence resolves divergence.",
    "DIVERGENCE_CONSEQUENCE_SELECTS_WINNER": "Divergence consequence selects a winner.",
    "DIVERGENCE_CONSEQUENCE_INVALIDATES_LOSER": "Divergence consequence invalidates a loser.",
    "DIVERGENCE_CONSEQUENCE_CREATES_CARRIER_CURRENTNESS": "Divergence consequence creates carrier currentness.",
    "DIVERGENCE_CONSEQUENCE_SELECTS_CURRENT_CARRIER": "Divergence consequence selects a current carrier.",
    "DIVERGENCE_CONSEQUENCE_REPLACES_SOURCE": "Divergence consequence replaces source.",
    "DIVERGENCE_CONSEQUENCE_CREATES_AUTHORITY": "Divergence consequence creates authority.",
    "DIVERGENCE_CONSEQUENCE_CREATES_PERMISSION": "Divergence consequence creates permission.",
    "DIVERGENCE_CONSEQUENCE_CREATES_TRUTH": "Divergence consequence creates truth.",
    "DIVERGENCE_CONSEQUENCE_AUTHORIZES_ACTION": "Divergence consequence authorizes action.",
    "DIVERGENCE_CONSEQUENCE_CREATES_CARRIER_HIERARCHY": "Divergence consequence creates carrier hierarchy.",
    "DIVERGENCE_CONSEQUENCE_ERASES_EVIDENCE": "Divergence consequence erases evidence.",
    "DIVERGENCE_CONSEQUENCE_CREATES_DISTRIBUTED_STANDING": "Divergence consequence creates distributed standing.",
    "DIVERGENCE_CONSEQUENCE_AUTHORIZES_REPOSITORY_SYNC": "Divergence consequence authorizes repository synchronization.",
    "DIVERGENCE_CONSEQUENCE_AUTHORIZES_FULL_BODY_TRANSFER": "Divergence consequence authorizes full body transfer.",
    "DIVERGENCE_CONSEQUENCE_CREATES_SECOND_BODY": "Divergence consequence creates a second body.",
    "DIVERGENCE_CONSEQUENCE_AUTHORIZES_CONTINUATION": "Divergence consequence authorizes continuation.",
    "DIVERGENCE_CONSEQUENCE_AUTHORIZES_DISTRIBUTED_OPERATION": "Divergence consequence authorizes distributed operation.",
    "LATEST_FILE_OR_TURN_CONSEQUENCE": "Latest file or latest turn is treated as consequence.",
    "MAJORITY_OR_SUCCESS_COUNT_CONSEQUENCE": "Majority or success count is treated as consequence.",
    "REGISTRY_LIFECYCLE_PROPAGATION_OR_TURN_CONSEQUENCE": "Registry, lifecycle, standing propagation, or continuity turn decides consequence by itself.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge was detected.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required divergence consequence non-claim is missing or flipped.",
}

CONSEQUENCE_NON_MEANING = {
    "does_not_mean_divergence_resolved": True,
    "does_not_mean_truth_created": True,
    "does_not_mean_action_authorized": True,
    "does_not_mean_consequence_action_law_created": True,
    "does_not_mean_winner_selected": True,
    "does_not_mean_loser_invalidated": True,
    "does_not_mean_carrier_hierarchy": True,
    "does_not_mean_current_carrier_selected": True,
    "does_not_mean_carrier_currentness": True,
    "does_not_mean_source_replacement": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_distributed_standing": True,
    "does_not_mean_distributed_currentness": True,
    "does_not_mean_evidence_erased": True,
    "does_not_mean_refusal_erased": True,
    "does_not_mean_blocked_attempt_erased": True,
    "does_not_mean_projection_mismatch_erased": True,
    "does_not_mean_registry_lifecycle_propagation_turn_currentness": True,
    "does_not_mean_latest_file_consequence": True,
    "does_not_mean_latest_turn_consequence": True,
    "does_not_mean_majority_consequence": True,
    "does_not_mean_success_count_consequence": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_continuation": True,
    "does_not_mean_distributed_operation": True,
}

WHAT_REMAINS_OPEN = {
    "divergence_consequence_implementation_refinement": True,
    "distributed_standing_boundary": True,
    "distributed_standing": True,
    "carrier_registry_implementation": True,
    "persistence_implementation": True,
    "standing_propagation_implementation_beyond_boundary_recording": True,
    "carrier_continuity_turn_implementation_refinement": True,
    "future_currentness_successor_refinement_if_separately_justified": True,
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

IDENTITY_KEYS = (
    "selected_divergence_evidence_id",
    "divergence_evidence_id",
    "selected_carrier_evidence_id",
    "carrier_evidence_id",
    "evidence_id",
    "artifact_id",
    "result_id",
    "id",
    "path",
)
OUTCOME_KEYS = (
    "selected_divergence_evidence_outcome",
    "divergence_evidence_outcome",
    "selected_carrier_evidence_outcome",
    "carrier_evidence_outcome",
    "evidence_outcome",
    "artifact_outcome",
    "result_outcome",
    "outcome",
    "status",
)


def resolve_cross_carrier_divergence_consequence_boundary(
    declared_divergence_consequence_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded cross-carrier divergence consequence request."""

    if declared_divergence_consequence_request is None:
        return _resolve_divergence_consequence({}, None, [])
    if not isinstance(declared_divergence_consequence_request, Mapping):
        return _resolve_divergence_consequence(
            {},
            None,
            ["DECLARED_DIVERGENCE_CONSEQUENCE_REQUEST_MALFORMED"],
        )
    return _resolve_divergence_consequence(
        copy.deepcopy(dict(declared_divergence_consequence_request)),
        None,
        [],
    )


def resolve_cross_carrier_divergence_consequence_boundary_from_path(
    declared_divergence_consequence_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one bounded divergence consequence request from a JSON object."""

    path = Path(declared_divergence_consequence_request_path)
    try:
        request = _read_json_mapping(path)
    except CrossCarrierDivergenceConsequenceBoundaryError as exc:
        return _resolve_divergence_consequence({}, path, [exc.block_code])
    return _resolve_divergence_consequence(request, path, [])


def write_cross_carrier_divergence_consequence_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an additive divergence consequence result without overwriting."""

    if not isinstance(result, Mapping):
        raise CrossCarrierDivergenceConsequenceBoundaryError(
            "DECLARED_DIVERGENCE_CONSEQUENCE_REQUEST_MALFORMED",
            "Divergence consequence result must be a mapping.",
        )

    if output_path is None:
        summary = _as_mapping(result.get("divergence_consequence_summary"))
        basis_id = (
            summary.get("divergence_consequence_request_id")
            or summary.get("requested_divergence_consequence_posture")
            or "divergence_consequence"
        )
        output_path = CROSS_CARRIER_DIVERGENCE_CONSEQUENCE_BOUNDARY_ROOT / (
            f"{_safe_filename_part(basis_id)}__cross_carrier_divergence_consequence_result.json"
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


def build_cross_carrier_divergence_consequence_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary from the full divergence consequence body."""

    checks = _mapping_list(result.get("consequence_checks"))
    question = _as_mapping(result.get("declared_divergence_consequence_question"))
    reliance = _as_mapping(result.get("declared_reliance_or_use_question"))
    divergence_evidence = _as_mapping(result.get("selected_divergence_evidence"))
    carrier_evidence = _as_mapping(result.get("selected_carrier_evidence"))
    posture = _as_mapping(result.get("divergence_consequence_posture"))
    scope = _as_mapping(result.get("consequence_scope"))
    statement = _as_mapping(result.get("consequence_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "divergence_consequence_request_id": question.get(
            "divergence_consequence_request_id"
        ),
        "divergence_consequence_question": question.get(
            "divergence_consequence_question"
        ),
        "divergence_consequence_intent": question.get(
            "divergence_consequence_intent"
        ),
        "declared_reliance_or_use_question": reliance.get(
            "declared_reliance_or_use_question"
        ),
        "requested_divergence_consequence_posture": posture.get(
            "requested_divergence_consequence_posture"
        ),
        "selected_divergence_evidence_id": divergence_evidence.get(
            "selected_divergence_evidence_id"
        ),
        "selected_divergence_evidence_outcome": divergence_evidence.get(
            "selected_divergence_evidence_outcome"
        ),
        "selected_carrier_evidence_ids": carrier_evidence.get(
            "selected_carrier_evidence_ids"
        ),
        "selected_carrier_evidence_outcomes": carrier_evidence.get(
            "selected_carrier_evidence_outcomes"
        ),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "divergence_consequence_recorded": bool(
            statement.get("divergence_consequence_recorded")
        ),
        "consequence_scope_preserved": bool(
            statement.get("consequence_scope_preserved")
        ),
        "visible_divergence_preserved": bool(
            statement.get("visible_divergence_preserved")
        ),
        "visible_refusal_preserved": bool(
            statement.get("visible_refusal_preserved")
        ),
        "blocked_attempts_preserved": bool(
            statement.get("blocked_attempts_preserved")
        ),
        "projection_mismatch_preserved": bool(
            statement.get("projection_mismatch_preserved")
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
        "detailed_basis_distinguished_from_summary": bool(
            statement.get("detailed_basis_distinguished_from_summary")
        ),
        "summary_overrode_detailed_basis": bool(
            statement.get("summary_overrode_detailed_basis")
        ),
        "divergence_resolved": bool(statement.get("divergence_resolved")),
        "winning_carrier_selected": bool(
            statement.get("winning_carrier_selected")
        ),
        "losing_carrier_invalidated": bool(
            statement.get("losing_carrier_invalidated")
        ),
        "no_carrier_currentness_current_carrier_source_authority_permission": not bool(
            statement.get("carrier_currentness_created")
            or statement.get("current_carrier_selected")
            or statement.get("source_replaced")
            or statement.get("authority_created")
            or statement.get("permission_created")
        ),
        "no_truth_action": not bool(
            statement.get("truth_created") or statement.get("action_authorized")
        ),
        "no_carrier_hierarchy": not bool(statement.get("carrier_hierarchy_created")),
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
        "no_latest_file_turn_majority_success_count_consequence": not bool(
            statement.get("latest_file_consequence")
            or statement.get("latest_turn_consequence")
            or statement.get("majority_carrier_consequence")
            or statement.get("successful_receipt_count_consequence")
        ),
        "consequence_scope": scope.get("raw_consequence_scope"),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_declared_cross_carrier_divergence_consequence_request(
    divergence_consequence_request_id: str,
    divergence_consequence_question: str,
    declared_reliance_or_use_question: str,
    selected_divergence_evidence: Mapping[str, Any],
    requested_divergence_consequence_posture: str,
    divergence_consequence_basis: Mapping[str, Any] | str,
    divergence_consequence_intent: str = RECORD_INTENT,
    *,
    selected_carrier_evidence: Sequence[Mapping[str, Any]] | None = None,
    currentness_successor_basis: Mapping[str, Any] | str | None = None,
    carrier_continuity_turn_basis: Mapping[str, Any] | str | None = None,
    standing_propagation_basis: Mapping[str, Any] | str | None = None,
    registry_persistence_basis: Mapping[str, Any] | str | None = None,
    lifecycle_basis: Mapping[str, Any] | str | None = None,
    relation_conformance_closure_basis: Mapping[str, Any] | str | None = None,
    consequence_scope: Mapping[str, Any] | str | None = None,
) -> dict[str, Any]:
    """Build one bounded request without inferring truth, action, or force."""

    request: dict[str, Any] = {
        "divergence_consequence_request_id": divergence_consequence_request_id,
        "divergence_consequence_question": divergence_consequence_question,
        "divergence_consequence_intent": divergence_consequence_intent,
        "declared_reliance_or_use_question": declared_reliance_or_use_question,
        "selected_divergence_evidence": copy.deepcopy(
            dict(selected_divergence_evidence)
        ),
        "requested_divergence_consequence_posture": requested_divergence_consequence_posture,
        "divergence_consequence_basis": copy.deepcopy(divergence_consequence_basis),
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }
    if selected_carrier_evidence is not None:
        request["selected_carrier_evidence"] = [
            copy.deepcopy(dict(item))
            for item in selected_carrier_evidence
            if isinstance(item, Mapping)
        ]
    if consequence_scope is None:
        request["consequence_scope"] = {
            "declared_reliance_or_use_question": declared_reliance_or_use_question,
            "selected_divergence_evidence_id": _extract_identity(
                selected_divergence_evidence
            ),
            "requested_divergence_consequence_posture": requested_divergence_consequence_posture,
            "consequence_is_scoped_to_declared_use": True,
            "consequence_is_not_general_invalidation": True,
            "consequence_is_not_general_permission": True,
            "consequence_is_not_global_currentness_rule": True,
            "consequence_is_not_distributed_standing_rule": True,
        }
    else:
        request["consequence_scope"] = copy.deepcopy(consequence_scope)

    optional_sections = {
        "currentness_successor_basis": currentness_successor_basis,
        "carrier_continuity_turn_basis": carrier_continuity_turn_basis,
        "standing_propagation_basis": standing_propagation_basis,
        "registry_persistence_basis": registry_persistence_basis,
        "lifecycle_basis": lifecycle_basis,
        "relation_conformance_closure_basis": relation_conformance_closure_basis,
    }
    for key, value in optional_sections.items():
        if value is not None:
            request[key] = copy.deepcopy(value)
    return request


def _resolve_divergence_consequence(
    request: Mapping[str, Any],
    request_path: Path | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    normalized_request = _as_mapping(request)
    question = _declared_divergence_consequence_question(
        normalized_request,
        request_path,
    )
    reliance_question = _declared_reliance_or_use_question_section(
        normalized_request
    )
    divergence_evidence = _selected_divergence_evidence_section(normalized_request)
    carrier_evidence = _selected_carrier_evidence_section(normalized_request)
    posture = _divergence_consequence_posture_section(normalized_request)
    consequence_basis = _divergence_consequence_basis_section(normalized_request)
    currentness_basis = _optional_basis_section(
        normalized_request,
        "currentness_successor_basis",
        "currentness_successor_basis",
        ("currentness_successor_basis_required", "requires_currentness_successor_basis"),
    )
    continuity_basis = _optional_basis_section(
        normalized_request,
        "carrier_continuity_turn_basis",
        "carrier_continuity_turn_basis",
        ("carrier_continuity_turn_basis_required", "requires_carrier_continuity_turn_basis"),
    )
    standing_basis = _optional_basis_section(
        normalized_request,
        "standing_propagation_basis",
        "standing_propagation_basis",
        ("standing_propagation_basis_required", "requires_standing_propagation_basis"),
    )
    registry_basis = _optional_basis_section(
        normalized_request,
        "registry_persistence_basis",
        "registry_persistence_basis",
        ("registry_persistence_basis_required", "requires_registry_persistence_basis"),
    )
    lifecycle_basis = _optional_basis_section(
        normalized_request,
        "lifecycle_basis",
        "lifecycle_basis",
        ("lifecycle_basis_required", "requires_lifecycle_basis"),
    )
    relation_basis = _optional_basis_section(
        normalized_request,
        "relation_conformance_closure_basis",
        "relation_conformance_closure_basis",
        (
            "relation_conformance_closure_basis_required",
            "relation_conformance_basis_required",
            "requires_relation_conformance_closure_basis",
        ),
    )
    consequence_scope = _consequence_scope_section(
        normalized_request,
        reliance_question,
        divergence_evidence,
        carrier_evidence,
    )
    non_claims = _non_claims_section(normalized_request, question)
    visibility = _visibility_projection(
        normalized_request,
        divergence_evidence,
        carrier_evidence,
        consequence_basis,
        currentness_basis,
        continuity_basis,
        standing_basis,
        registry_basis,
        lifecycle_basis,
        relation_basis,
        consequence_scope,
        non_claims,
    )
    checks = _build_checks(
        normalized_request,
        question,
        reliance_question,
        divergence_evidence,
        carrier_evidence,
        posture,
        consequence_basis,
        currentness_basis,
        continuity_basis,
        standing_basis,
        registry_basis,
        lifecycle_basis,
        relation_basis,
        consequence_scope,
        non_claims,
        visibility,
        precheck_failures,
    )

    failed_checks = [check for check in checks if check.get("passed") is False]
    if failed_checks:
        outcome = DIVERGENCE_CONSEQUENCE_BLOCKED
        block_code = failed_checks[0].get("block_code")
    elif question.get("divergence_consequence_intent") == BLOCK_INTENT:
        outcome = DIVERGENCE_CONSEQUENCE_BLOCKED
        block_code = "DIVERGENCE_CONSEQUENCE_REQUEST_EXPLICITLY_BLOCKED"
    elif question.get("divergence_consequence_intent") == DO_NOT_RECORD_INTENT:
        outcome = DIVERGENCE_CONSEQUENCE_NOT_RECORDED
        block_code = None
    else:
        outcome = DIVERGENCE_CONSEQUENCE_RECORDED
        block_code = None

    block = {
        "blocked": outcome == DIVERGENCE_CONSEQUENCE_BLOCKED,
        "code": block_code,
        "reason": _block_reason(block_code),
        "block_code": block_code,
        "block_reason": _block_reason(block_code),
    }
    statement = _divergence_consequence_statement(
        outcome,
        reliance_question,
        divergence_evidence,
        carrier_evidence,
        posture,
        currentness_basis,
        continuity_basis,
        standing_basis,
        registry_basis,
        lifecycle_basis,
        relation_basis,
        consequence_scope,
        visibility,
    )
    result: dict[str, Any] = {
        "divergence_consequence_metadata": _metadata(question, posture, outcome),
        "declared_divergence_consequence_question": question,
        "declared_reliance_or_use_question": reliance_question,
        "selected_divergence_evidence": divergence_evidence,
        "selected_carrier_evidence": carrier_evidence,
        "currentness_successor_basis": currentness_basis,
        "carrier_continuity_turn_basis": continuity_basis,
        "standing_propagation_basis": standing_basis,
        "registry_persistence_basis": registry_basis,
        "lifecycle_basis": lifecycle_basis,
        "relation_conformance_closure_basis": relation_basis,
        "divergence_consequence_posture": posture,
        "consequence_scope": consequence_scope,
        "consequence_checks": checks,
        "consequence_statement": statement,
        "consequence_non_meaning": copy.deepcopy(CONSEQUENCE_NON_MEANING),
        "what_remains_open": copy.deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    result["divergence_consequence_summary"] = (
        build_cross_carrier_divergence_consequence_summary(result)
    )
    return result


def _declared_divergence_consequence_question(
    request: Mapping[str, Any],
    request_path: Path | None,
) -> dict[str, Any]:
    section = _as_mapping(request.get("declared_divergence_consequence_question"))
    raw_intent = (
        request.get("divergence_consequence_intent")
        or section.get("divergence_consequence_intent")
    )
    intent = _normalize_token(raw_intent)
    declared_non_claims = _as_mapping(
        request.get("declared_non_claims")
        or request.get("non_claims")
        or section.get("declared_non_claims")
    )
    return {
        "divergence_consequence_request_id": request.get(
            "divergence_consequence_request_id"
        )
        or section.get("divergence_consequence_request_id"),
        "divergence_consequence_question": request.get(
            "divergence_consequence_question"
        )
        or section.get("divergence_consequence_question"),
        "divergence_consequence_intent": intent,
        "raw_divergence_consequence_intent": raw_intent,
        "request_path": _display_path(request_path) or section.get("request_path"),
        "not_recorded_reason": request.get("not_recorded_reason")
        or section.get("not_recorded_reason")
        or (
            "declared request does not record divergence consequence posture"
            if intent == DO_NOT_RECORD_INTENT
            else None
        ),
        "declared_non_claims": declared_non_claims,
        "divergence_consequence_is_not_divergence_resolution": True,
        "divergence_consequence_is_not_truth": True,
        "divergence_consequence_is_not_action": True,
        "divergence_consequence_is_not_punishment": True,
        "divergence_consequence_is_not_currentness": True,
        "divergence_consequence_is_not_distributed_standing": True,
        "visible_divergence_not_erased_as_noise": True,
        "visible_divergence_not_overread_as_truth": True,
        "latest_file_or_turn_does_not_decide_consequence": True,
        "majority_or_success_count_does_not_decide_consequence": True,
    }


def _declared_reliance_or_use_question_section(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    section = _as_mapping(request.get("declared_reliance_or_use_question"))
    raw = request.get("declared_reliance_or_use_question")
    question = raw
    if isinstance(raw, Mapping):
        question = _first_declared(
            raw.get("declared_reliance_or_use_question"),
            raw.get("reliance_or_use_question"),
            raw.get("question"),
        )
    return {
        "declared_reliance_or_use_question": question,
        "raw_declared_reliance_or_use_question": copy.deepcopy(raw),
        "reliance_or_use_question_declared": _nonempty(question),
        "reliance_or_use_question_preserved": _nonempty(question),
        "consequence_scope_must_remain_declared_use_only": True,
        "consequence_is_not_general_invalidation": True,
        "consequence_is_not_general_permission": True,
    }


def _selected_divergence_evidence_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("selected_divergence_evidence")
    declared = raw is not None
    parseable = isinstance(raw, Mapping)
    evidence_id = _extract_identity(raw)
    outcome = _entry_outcome(raw)
    evidence_class = _field_from_mapping(
        raw,
        ("evidence_class", "evidence_role", "divergence_type", "type", "class"),
    )
    return {
        "selected_divergence_evidence_declared": declared,
        "selected_divergence_evidence_parseable": parseable if declared else False,
        "selected_divergence_evidence_id": evidence_id,
        "selected_divergence_evidence_identity_present": _nonempty(evidence_id),
        "selected_divergence_evidence_outcome": outcome,
        "selected_divergence_evidence_outcome_present": _nonempty(outcome),
        "selected_divergence_evidence_type_or_class": evidence_class,
        "raw_selected_divergence_evidence": copy.deepcopy(raw),
        "selected_divergence_evidence_preserved": declared and parseable,
        "selected_divergence_evidence_outcome_preserved": _nonempty(outcome),
        "evidence_remains_evidence": True,
        "divergence_remains_visible_not_resolved": True,
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
    required = _basis_required(
        request,
        (
            "selected_carrier_evidence_required",
            "requires_selected_carrier_evidence",
        ),
    )
    return {
        "selected_carrier_evidence_declared": declared,
        "selected_carrier_evidence_required": required,
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
        "selected_carrier_evidence_preserved": (
            (not required and not declared)
            or (
                bool(entries)
                and parseable
                and all(_nonempty(value) for value in evidence_ids)
                and all(_nonempty(value) for value in evidence_outcomes)
            )
        ),
        "carrier_evidence_remains_evidence": True,
        "carrier_evidence_does_not_become_currentness": True,
        "carrier_evidence_does_not_select_winner_or_loser": True,
    }


def _divergence_consequence_posture_section(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    raw = (
        request.get("requested_divergence_consequence_posture")
        or _field_from_mapping(
            request.get("divergence_consequence_posture"),
            (
                "requested_divergence_consequence_posture",
                "divergence_consequence_posture",
                "posture",
            ),
        )
    )
    posture = _normalize_token(raw)
    return {
        "requested_divergence_consequence_posture": posture,
        "raw_requested_divergence_consequence_posture": raw,
        "divergence_consequence_posture_supported": posture
        in SUPPORTED_DIVERGENCE_CONSEQUENCE_POSTURES,
        "supported_divergence_consequence_postures": sorted(
            SUPPORTED_DIVERGENCE_CONSEQUENCE_POSTURES
        ),
        "divergence_consequence_posture_preserved": posture
        in SUPPORTED_DIVERGENCE_CONSEQUENCE_POSTURES,
        "posture_is_bounded_reliance_effect": True,
        "posture_is_not_truth_action_currentness_or_distributed_standing": True,
    }


def _divergence_consequence_basis_section(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    raw = request.get("divergence_consequence_basis")
    raw_mapping = _as_mapping(raw)
    return {
        "divergence_consequence_basis_declared": _basis_declared(raw),
        "divergence_consequence_basis_preserved": _basis_declared(raw),
        "divergence_consequence_basis_id": _extract_identity(raw),
        "raw_divergence_consequence_basis": copy.deepcopy(raw),
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
        "basis_is_not_truth_action_or_currentness": True,
        "basis_does_not_resolve_divergence": True,
    }


def _optional_basis_section(
    request: Mapping[str, Any],
    key: str,
    section_name: str,
    required_keys: Sequence[str],
) -> dict[str, Any]:
    raw = request.get(key)
    nested = _as_mapping(request.get(section_name))
    if raw is None and nested:
        raw = nested.get(f"raw_{section_name}") or nested
    declared = _basis_declared(raw)
    required = _basis_required(request, required_keys) or any(
        _is_true(nested.get(required_key)) for required_key in required_keys
    )
    return {
        f"{section_name}_declared": declared,
        f"{section_name}_required": required,
        f"{section_name}_preserved": declared,
        f"{section_name}_id": _extract_identity(raw),
        f"raw_{section_name}": copy.deepcopy(raw),
        "basis_preserved_where_supplied": bool(not declared or _basis_declared(raw)),
        "basis_does_not_decide_consequence_by_itself": True,
        "basis_does_not_create_currentness": True,
        "basis_does_not_create_distributed_standing": True,
    }


def _consequence_scope_section(
    request: Mapping[str, Any],
    reliance_question: Mapping[str, Any],
    divergence_evidence: Mapping[str, Any],
    carrier_evidence: Mapping[str, Any],
) -> dict[str, Any]:
    raw = request.get("consequence_scope")
    declared = _basis_declared(raw)
    raw_mapping = _as_mapping(raw)
    return {
        "consequence_scope_declared": declared,
        "consequence_scope_preserved": declared,
        "raw_consequence_scope": copy.deepcopy(raw),
        "declared_reliance_or_use_question": reliance_question.get(
            "declared_reliance_or_use_question"
        ),
        "selected_divergence_affected": divergence_evidence.get(
            "selected_divergence_evidence_id"
        ),
        "selected_evidence_affected": carrier_evidence.get(
            "selected_carrier_evidence_ids"
        ),
        "scope_statement": raw_mapping.get("scope_statement") if raw_mapping else raw,
        "consequence_is_scoped_not_general_invalidation": True,
        "consequence_is_not_general_permission": True,
        "consequence_is_not_global_currentness_rule": True,
        "consequence_is_not_distributed_standing_rule": True,
        "may_block_limit_caution_exclude_revalidate_or_require_separate_review_for_declared_use_only": True,
        "separate_review_scheduled": False,
        "separate_review_authorized": False,
        "revalidation_scheduled": False,
        "revalidation_authorized": False,
        "evidence_remains_preserved_for_other_possible_future_uses": True,
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
    divergence_evidence: Mapping[str, Any],
    carrier_evidence: Mapping[str, Any],
    consequence_basis: Mapping[str, Any],
    currentness_basis: Mapping[str, Any],
    continuity_basis: Mapping[str, Any],
    standing_basis: Mapping[str, Any],
    registry_basis: Mapping[str, Any],
    lifecycle_basis: Mapping[str, Any],
    relation_basis: Mapping[str, Any],
    consequence_scope: Mapping[str, Any],
    non_claims: Mapping[str, Any],
) -> dict[str, bool]:
    evidence_entries = carrier_evidence.get("selected_carrier_evidence_entries") or []
    sources = [
        divergence_evidence.get("raw_selected_divergence_evidence"),
        carrier_evidence.get("raw_selected_carrier_evidence"),
        consequence_basis.get("raw_divergence_consequence_basis"),
        currentness_basis.get("raw_currentness_successor_basis"),
        continuity_basis.get("raw_carrier_continuity_turn_basis"),
        standing_basis.get("raw_standing_propagation_basis"),
        registry_basis.get("raw_registry_persistence_basis"),
        lifecycle_basis.get("raw_lifecycle_basis"),
        relation_basis.get("raw_relation_conformance_closure_basis"),
        consequence_scope.get("raw_consequence_scope"),
    ]

    divergence_hidden = _recursive_true(
        [request, non_claims],
        (
            "divergence_consequence_hid_divergence",
            "divergence_consequence_hides_divergence",
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
                    "divergence_visible",
                    "divergence_remains_visible",
                ),
            )
            or _entry_outcome(divergence_evidence.get("raw_selected_divergence_evidence"))
            == "CARRIER_DIVERGENCE_RECORDED"
            or _entries_have_token(
                [divergence_evidence.get("raw_selected_divergence_evidence")]
                + evidence_entries,
                ("divergence", "mismatch"),
            )
        )
    )

    refusal_hidden = _recursive_true(
        [request, non_claims],
        (
            "divergence_consequence_hid_refusal",
            "divergence_consequence_hides_refusal",
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
                "visible_refusal_preserved",
                "refusal_preserved",
                "refusal_visible",
            ),
        )
        or _entries_have_token(evidence_entries, ("refusal", "refused", "blocked"))
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
            or _entries_have_token(evidence_entries, ("refusal", "refused", "blocked"))
        )
    )

    blocked_hidden = _recursive_true(
        [request, non_claims],
        (
            "divergence_consequence_hid_blocked_attempt",
            "divergence_consequence_hides_blocked_attempt",
            "blocked_attempt_hidden",
            "blocked_attempts_hidden",
            "hides_blocked_attempt",
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
                "blocked_attempt_visible",
            ),
        )
        or _entries_have_token(evidence_entries, ("blocked", "block", "failed"))
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
            or _entries_have_token(evidence_entries, ("blocked", "block", "failed"))
            or _entries_have_outcome(evidence_entries, ("BLOCKED",))
        )
    )

    projection_hidden = _recursive_true(
        [request, non_claims],
        (
            "divergence_consequence_hid_projection_mismatch",
            "divergence_consequence_hides_projection_mismatch",
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
            ),
        )
        or _entries_have_token(evidence_entries, ("projection_mismatch", "projection"))
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
            or _entries_have_token(evidence_entries, ("projection_mismatch", "projection"))
        )
    )

    detailed_ref = consequence_basis.get("detailed_basis_reference")
    summary_ref = consequence_basis.get("summary_projection_reference")
    summary_overrode = _recursive_true(
        [request, non_claims] + sources,
        (
            "summary_overrode_detailed_basis",
            "summary_overwrites_detailed_basis",
            "summary_projection_overrode_detailed_basis",
        ),
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
    detailed_distinguished = bool(
        not summary_overrode
        and (
            _recursive_true(
                sources,
                (
                    "detailed_basis_distinguished_from_summary",
                    "detailed_basis_distinguishable_from_summary",
                ),
            )
            or (_basis_declared(detailed_ref) and _basis_declared(summary_ref))
        )
    )

    return {
        "visible_divergence_preserved": divergence_preserved,
        "visible_divergence_hidden": divergence_hidden,
        "visible_refusal_applicable": refusal_applicable,
        "visible_refusal_preserved": refusal_preserved,
        "visible_refusal_hidden": refusal_hidden,
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
    reliance_question: Mapping[str, Any],
    divergence_evidence: Mapping[str, Any],
    carrier_evidence: Mapping[str, Any],
    posture: Mapping[str, Any],
    consequence_basis: Mapping[str, Any],
    currentness_basis: Mapping[str, Any],
    continuity_basis: Mapping[str, Any],
    standing_basis: Mapping[str, Any],
    registry_basis: Mapping[str, Any],
    lifecycle_basis: Mapping[str, Any],
    relation_basis: Mapping[str, Any],
    consequence_scope: Mapping[str, Any],
    non_claims: Mapping[str, Any],
    visibility: Mapping[str, bool],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for code in precheck_failures:
        checks.append(
            _check(
                "declared_divergence_consequence_request_parseable",
                False,
                "declared request is a JSON object or mapping",
                "declared request is unreadable or malformed",
                code,
            )
        )

    checks.extend(
        [
            _check(
                "divergence_consequence_question_declared",
                _nonempty(question.get("divergence_consequence_question")),
                "divergence consequence question declared",
                question.get("divergence_consequence_question"),
                "DIVERGENCE_CONSEQUENCE_QUESTION_UNDECLARED",
            ),
            _check(
                "divergence_consequence_intent_supported",
                question.get("divergence_consequence_intent")
                in SUPPORTED_DIVERGENCE_CONSEQUENCE_INTENTS,
                "supported divergence consequence intent",
                question.get("divergence_consequence_intent"),
                "DIVERGENCE_CONSEQUENCE_INTENT_UNSUPPORTED",
            ),
            _check(
                "reliance_or_use_question_declared",
                bool(reliance_question.get("reliance_or_use_question_declared")),
                "declared reliance or use question present",
                reliance_question.get("declared_reliance_or_use_question"),
                "RELIANCE_OR_USE_QUESTION_MISSING",
            ),
            _check(
                "selected_divergence_evidence_present",
                bool(divergence_evidence.get("selected_divergence_evidence_declared")),
                "selected divergence evidence present",
                divergence_evidence.get("raw_selected_divergence_evidence"),
                "SELECTED_DIVERGENCE_EVIDENCE_MISSING",
            ),
            _check(
                "selected_divergence_evidence_parseable",
                bool(divergence_evidence.get("selected_divergence_evidence_parseable"))
                or not divergence_evidence.get("selected_divergence_evidence_declared"),
                "selected divergence evidence is a mapping",
                divergence_evidence.get("raw_selected_divergence_evidence"),
                "SELECTED_DIVERGENCE_EVIDENCE_MALFORMED",
            ),
            _check(
                "selected_divergence_evidence_outcome_present",
                bool(
                    divergence_evidence.get(
                        "selected_divergence_evidence_outcome_present"
                    )
                ),
                "selected divergence evidence outcome present",
                divergence_evidence.get("selected_divergence_evidence_outcome"),
                "SELECTED_DIVERGENCE_EVIDENCE_OUTCOME_MISSING",
            ),
            _check(
                "selected_carrier_evidence_preserved_where_required_or_supplied",
                bool(carrier_evidence.get("selected_carrier_evidence_preserved")),
                "selected carrier evidence preserved where supplied or required",
                carrier_evidence.get("raw_selected_carrier_evidence"),
                "SELECTED_CARRIER_EVIDENCE_MISSING",
            ),
            _check(
                "divergence_consequence_posture_supported",
                bool(posture.get("divergence_consequence_posture_supported")),
                "supported divergence consequence posture",
                posture.get("requested_divergence_consequence_posture"),
                "DIVERGENCE_CONSEQUENCE_POSTURE_UNSUPPORTED",
            ),
            _check(
                "divergence_consequence_basis_declared",
                bool(consequence_basis.get("divergence_consequence_basis_declared")),
                "divergence consequence basis declared",
                consequence_basis.get("raw_divergence_consequence_basis"),
                "DIVERGENCE_CONSEQUENCE_BASIS_MISSING",
            ),
            _check(
                "currentness_successor_basis_preserved_where_required_or_supplied",
                _optional_basis_ok(currentness_basis, "currentness_successor_basis"),
                "currentness successor basis preserved where required or supplied",
                currentness_basis.get("raw_currentness_successor_basis"),
                "CURRENTNESS_SUCCESSOR_BASIS_MISSING",
            ),
            _check(
                "carrier_continuity_turn_basis_preserved_where_required_or_supplied",
                _optional_basis_ok(continuity_basis, "carrier_continuity_turn_basis"),
                "carrier continuity-turn basis preserved where required or supplied",
                continuity_basis.get("raw_carrier_continuity_turn_basis"),
                "CARRIER_CONTINUITY_TURN_BASIS_MISSING",
            ),
            _check(
                "lifecycle_registry_propagation_basis_preserved_where_required_or_supplied",
                _lifecycle_registry_propagation_ok(
                    request,
                    lifecycle_basis,
                    registry_basis,
                    standing_basis,
                ),
                "lifecycle, registry, and standing propagation basis preserved where required or supplied",
                {
                    "lifecycle": lifecycle_basis.get("raw_lifecycle_basis"),
                    "registry": registry_basis.get("raw_registry_persistence_basis"),
                    "standing": standing_basis.get("raw_standing_propagation_basis"),
                },
                "LIFECYCLE_REGISTRY_PROPAGATION_BASIS_MISSING",
            ),
            _check(
                "relation_conformance_closure_basis_preserved_where_required_or_supplied",
                _optional_basis_ok(
                    relation_basis,
                    "relation_conformance_closure_basis",
                ),
                "relation/conformance/closure basis preserved where required or supplied",
                relation_basis.get("raw_relation_conformance_closure_basis"),
                "RELATION_CONFORMANCE_CLOSURE_BASIS_MISSING",
            ),
            _check(
                "consequence_scope_declared",
                bool(consequence_scope.get("consequence_scope_declared")),
                "consequence scope declared",
                consequence_scope.get("raw_consequence_scope"),
                "CONSEQUENCE_SCOPE_MISSING",
            ),
            _check(
                "visible_divergence_preserved",
                bool(visibility.get("visible_divergence_preserved")),
                "visible divergence remains visible",
                visibility,
                "DIVERGENCE_CONSEQUENCE_HIDES_DIVERGENCE",
            ),
            _check(
                "visible_refusal_preserved_where_applicable",
                (not visibility.get("visible_refusal_applicable"))
                or bool(visibility.get("visible_refusal_preserved")),
                "visible refusal remains visible where applicable",
                visibility,
                "DIVERGENCE_CONSEQUENCE_HIDES_REFUSAL",
            ),
            _check(
                "blocked_attempts_preserved_where_applicable",
                (not visibility.get("blocked_attempts_applicable"))
                or bool(visibility.get("blocked_attempts_preserved")),
                "blocked attempts remain visible where applicable",
                visibility,
                "DIVERGENCE_CONSEQUENCE_HIDES_BLOCKED_ATTEMPT",
            ),
            _check(
                "projection_mismatch_preserved_where_applicable",
                (not visibility.get("projection_mismatch_applicable"))
                or bool(visibility.get("projection_mismatch_preserved")),
                "projection mismatch remains visible where applicable",
                visibility,
                "DIVERGENCE_CONSEQUENCE_HIDES_PROJECTION_MISMATCH",
            ),
            _check(
                "detailed_basis_distinguishable_from_summary_where_applicable",
                (not visibility.get("detailed_basis_applicable"))
                or bool(visibility.get("detailed_basis_distinguished_from_summary")),
                "detailed basis remains distinguishable from summary where applicable",
                visibility,
                "SUMMARY_OVERWRITES_DETAILED_BASIS",
            ),
            _check(
                "summary_does_not_override_detailed_basis",
                not bool(visibility.get("summary_overrode_detailed_basis")),
                "summary does not override detailed basis",
                visibility.get("summary_overrode_detailed_basis"),
                "SUMMARY_OVERWRITES_DETAILED_BASIS",
            ),
        ]
    )

    collapse_checks = [
        (
            "no_divergence_resolution",
            (
                "divergence_resolved",
                "consequence_resolves_divergence",
                "divergence_consequence_resolved_divergence",
            ),
            "DIVERGENCE_CONSEQUENCE_RESOLVES_DIVERGENCE",
        ),
        (
            "no_winner_selection",
            ("winning_carrier_selected", "winner_selected", "selects_winner"),
            "DIVERGENCE_CONSEQUENCE_SELECTS_WINNER",
        ),
        (
            "no_loser_invalidation",
            ("losing_carrier_invalidated", "loser_invalidated", "invalidates_loser"),
            "DIVERGENCE_CONSEQUENCE_INVALIDATES_LOSER",
        ),
        (
            "no_carrier_currentness",
            ("carrier_currentness_created", "creates_carrier_currentness"),
            "DIVERGENCE_CONSEQUENCE_CREATES_CARRIER_CURRENTNESS",
        ),
        (
            "no_current_carrier_selection",
            ("current_carrier_selected", "selects_current_carrier"),
            "DIVERGENCE_CONSEQUENCE_SELECTS_CURRENT_CARRIER",
        ),
        (
            "no_source_replacement",
            ("source_replaced", "replaces_source", "source_replacement"),
            "DIVERGENCE_CONSEQUENCE_REPLACES_SOURCE",
        ),
        (
            "no_authority",
            ("authority_created", "creates_authority"),
            "DIVERGENCE_CONSEQUENCE_CREATES_AUTHORITY",
        ),
        (
            "no_permission",
            ("permission_created", "creates_permission"),
            "DIVERGENCE_CONSEQUENCE_CREATES_PERMISSION",
        ),
        (
            "no_truth",
            ("truth_created", "creates_truth"),
            "DIVERGENCE_CONSEQUENCE_CREATES_TRUTH",
        ),
        (
            "no_action",
            ("action_authorized", "authorizes_action"),
            "DIVERGENCE_CONSEQUENCE_AUTHORIZES_ACTION",
        ),
        (
            "no_carrier_hierarchy",
            (
                "carrier_hierarchy_created",
                "divergence_consequence_created_carrier_hierarchy",
            ),
            "DIVERGENCE_CONSEQUENCE_CREATES_CARRIER_HIERARCHY",
        ),
        (
            "no_evidence_erasure",
            ("evidence_erased", "divergence_consequence_erased_evidence"),
            "DIVERGENCE_CONSEQUENCE_ERASES_EVIDENCE",
        ),
        (
            "no_distributed_standing",
            (
                "distributed_standing_created",
                "divergence_consequence_created_distributed_standing",
            ),
            "DIVERGENCE_CONSEQUENCE_CREATES_DISTRIBUTED_STANDING",
        ),
        (
            "no_repository_sync",
            ("repository_synchronization_authorized", "repository_sync_authorized"),
            "DIVERGENCE_CONSEQUENCE_AUTHORIZES_REPOSITORY_SYNC",
        ),
        (
            "no_full_body_transfer",
            ("full_body_transfer_authorized",),
            "DIVERGENCE_CONSEQUENCE_AUTHORIZES_FULL_BODY_TRANSFER",
        ),
        (
            "no_second_body",
            ("second_body_created",),
            "DIVERGENCE_CONSEQUENCE_CREATES_SECOND_BODY",
        ),
        (
            "no_continuation",
            ("continuation_authorized",),
            "DIVERGENCE_CONSEQUENCE_AUTHORIZES_CONTINUATION",
        ),
        (
            "no_distributed_operation",
            ("distributed_operation_authorized",),
            "DIVERGENCE_CONSEQUENCE_AUTHORIZES_DISTRIBUTED_OPERATION",
        ),
        (
            "no_latest_file_or_turn_consequence",
            ("latest_file_consequence", "latest_turn_consequence"),
            "LATEST_FILE_OR_TURN_CONSEQUENCE",
        ),
        (
            "no_majority_or_success_count_consequence",
            ("majority_carrier_consequence", "successful_receipt_count_consequence"),
            "MAJORITY_OR_SUCCESS_COUNT_CONSEQUENCE",
        ),
        (
            "no_registry_lifecycle_propagation_or_turn_consequence_by_itself",
            (
                "registry_record_consequence",
                "lifecycle_status_consequence",
                "standing_propagation_consequence",
                "continuity_turn_consequence",
            ),
            "REGISTRY_LIFECYCLE_PROPAGATION_OR_TURN_CONSEQUENCE",
        ),
        (
            "no_mutation_replay_or_merge",
            ("mutation_performed", "replay_performed", "merge_performed"),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
    ]
    for check_name, keys, block_code in collapse_checks:
        collapsed = _recursive_true([request, non_claims], keys)
        checks.append(
            _check(
                check_name,
                not collapsed,
                "collapse flag absent or false",
                {key: _recursive_key_values([request, non_claims], key) for key in keys},
                block_code,
            )
        )

    checks.append(
        _check(
            "non_claims_remain_false",
            bool(non_claims.get("required_non_claims_preserved")),
            "all required divergence consequence non-claims present and false",
            {
                "missing": non_claims.get("missing_required_non_claims"),
                "flipped": non_claims.get("flipped_required_non_claims"),
            },
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _divergence_consequence_statement(
    outcome: str,
    reliance_question: Mapping[str, Any],
    divergence_evidence: Mapping[str, Any],
    carrier_evidence: Mapping[str, Any],
    posture: Mapping[str, Any],
    currentness_basis: Mapping[str, Any],
    continuity_basis: Mapping[str, Any],
    standing_basis: Mapping[str, Any],
    registry_basis: Mapping[str, Any],
    lifecycle_basis: Mapping[str, Any],
    relation_basis: Mapping[str, Any],
    consequence_scope: Mapping[str, Any],
    visibility: Mapping[str, bool],
) -> dict[str, Any]:
    recorded = outcome == DIVERGENCE_CONSEQUENCE_RECORDED
    return {
        "divergence_consequence_recorded": recorded,
        "declared_reliance_or_use_question_preserved": bool(
            reliance_question.get("reliance_or_use_question_preserved")
        ),
        "selected_divergence_evidence_preserved": bool(
            divergence_evidence.get("selected_divergence_evidence_preserved")
        ),
        "selected_divergence_evidence_outcome_preserved": bool(
            divergence_evidence.get("selected_divergence_evidence_outcome_preserved")
        ),
        "selected_carrier_evidence_preserved": bool(
            carrier_evidence.get("selected_carrier_evidence_preserved")
        ),
        "divergence_consequence_posture_preserved": bool(
            posture.get("divergence_consequence_posture_preserved")
        ),
        "consequence_scope_preserved": bool(
            consequence_scope.get("consequence_scope_preserved")
        ),
        "visible_divergence_preserved": bool(
            visibility.get("visible_divergence_preserved")
        ),
        "visible_refusal_preserved": bool(
            visibility.get("visible_refusal_preserved")
        ),
        "blocked_attempts_preserved": bool(
            visibility.get("blocked_attempts_preserved")
        ),
        "projection_mismatch_preserved": bool(
            visibility.get("projection_mismatch_preserved")
        ),
        "currentness_successor_basis_preserved": bool(
            currentness_basis.get("currentness_successor_basis_preserved")
        ),
        "carrier_continuity_turn_basis_preserved": bool(
            continuity_basis.get("carrier_continuity_turn_basis_preserved")
        ),
        "standing_propagation_basis_preserved": bool(
            standing_basis.get("standing_propagation_basis_preserved")
        ),
        "registry_persistence_basis_preserved": bool(
            registry_basis.get("registry_persistence_basis_preserved")
        ),
        "lifecycle_basis_preserved": bool(lifecycle_basis.get("lifecycle_basis_preserved")),
        "relation_conformance_closure_basis_preserved": bool(
            relation_basis.get("relation_conformance_closure_basis_preserved")
        ),
        "detailed_basis_distinguished_from_summary": bool(
            visibility.get("detailed_basis_distinguished_from_summary")
        ),
        "summary_overrode_detailed_basis": False,
        "divergence_resolved": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "carrier_currentness_created": False,
        "currentness_created": False,
        "current_carrier_selected": False,
        "source_replaced": False,
        "authority_created": False,
        "permission_created": False,
        "truth_created": False,
        "action_authorized": False,
        "carrier_hierarchy_created": False,
        "evidence_erased": False,
        "distributed_standing_created": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
        "latest_file_consequence": False,
        "latest_turn_consequence": False,
        "majority_carrier_consequence": False,
        "successful_receipt_count_consequence": False,
    }


def _metadata(
    question: Mapping[str, Any],
    posture: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    generated_at = datetime.now(timezone.utc).isoformat()
    request_id = (
        question.get("divergence_consequence_request_id")
        or posture.get("requested_divergence_consequence_posture")
        or "unidentified_divergence_consequence"
    )
    return {
        "divergence_consequence_result_id": (
            f"{_safe_filename_part(request_id)}__{_safe_filename_part(outcome)}__{generated_at}"
        ),
        "divergence_consequence_result_type": RESULT_TYPE,
        "divergence_consequence_result_version": RESULT_VERSION,
        "generated_at": generated_at,
        "resolver_module": RESOLVER_MODULE,
    }


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
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": None if passed else block_code,
    }


def _read_json_mapping(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CrossCarrierDivergenceConsequenceBoundaryError(
            "DECLARED_DIVERGENCE_CONSEQUENCE_REQUEST_UNREADABLE",
            str(exc),
        ) from exc
    try:
        loaded = json.loads(text)
    except json.JSONDecodeError as exc:
        raise CrossCarrierDivergenceConsequenceBoundaryError(
            "DECLARED_DIVERGENCE_CONSEQUENCE_REQUEST_MALFORMED",
            str(exc),
        ) from exc
    if not isinstance(loaded, Mapping):
        raise CrossCarrierDivergenceConsequenceBoundaryError(
            "DECLARED_DIVERGENCE_CONSEQUENCE_REQUEST_MALFORMED",
            "Declared divergence consequence request JSON must be an object.",
        )
    return copy.deepcopy(dict(loaded))


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
        if key in value and _nonempty(value.get(key)):
            return value.get(key)
    return None


def _extract_identity(value: Any) -> str | None:
    if isinstance(value, str):
        return value if _nonempty(value) else None
    if not isinstance(value, Mapping):
        return None
    for key in IDENTITY_KEYS:
        if _nonempty(value.get(key)):
            return str(value.get(key))
    metadata = value.get("metadata")
    if isinstance(metadata, Mapping):
        for key in IDENTITY_KEYS:
            if _nonempty(metadata.get(key)):
                return str(metadata.get(key))
    return None


def _entry_outcome(value: Any) -> str | None:
    if not isinstance(value, Mapping):
        return None
    for key in OUTCOME_KEYS:
        if _nonempty(value.get(key)):
            return str(value.get(key))
    metadata = value.get("metadata")
    if isinstance(metadata, Mapping):
        for key in OUTCOME_KEYS:
            if _nonempty(metadata.get(key)):
                return str(metadata.get(key))
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
    return False


def _basis_required(request: Mapping[str, Any], keys: Sequence[str]) -> bool:
    basis = _as_mapping(request.get("divergence_consequence_basis"))
    return any(
        _is_true(request.get(key))
        or _is_true(basis.get(key))
        or _recursive_true([request], (key,))
        for key in keys
    )


def _optional_basis_ok(section: Mapping[str, Any], section_name: str) -> bool:
    return bool(
        (not section.get(f"{section_name}_required"))
        or section.get(f"{section_name}_preserved")
    )


def _lifecycle_registry_propagation_ok(
    request: Mapping[str, Any],
    lifecycle_basis: Mapping[str, Any],
    registry_basis: Mapping[str, Any],
    standing_basis: Mapping[str, Any],
) -> bool:
    required = _basis_required(
        request,
        (
            "lifecycle_registry_propagation_basis_required",
            "requires_lifecycle_registry_propagation_basis",
        ),
    )
    if not required:
        return (
            _optional_basis_ok(lifecycle_basis, "lifecycle_basis")
            and _optional_basis_ok(registry_basis, "registry_persistence_basis")
            and _optional_basis_ok(standing_basis, "standing_propagation_basis")
        )
    return bool(
        lifecycle_basis.get("lifecycle_basis_preserved")
        or registry_basis.get("registry_persistence_basis_preserved")
        or standing_basis.get("standing_propagation_basis_preserved")
    )


def _recursive_true(values: Any, keys: Sequence[str]) -> bool:
    key_set = set(keys)

    def walk(value: Any) -> bool:
        if isinstance(value, Mapping):
            for key, item in value.items():
                if key in key_set and _is_true(item):
                    return True
                if walk(item):
                    return True
        elif isinstance(value, Sequence) and not isinstance(
            value,
            (str, bytes, bytearray),
        ):
            return any(walk(item) for item in value)
        return False

    return walk(values)


def _recursive_key_values(values: Any, key: str) -> list[Any]:
    found: list[Any] = []

    def walk(value: Any) -> None:
        if isinstance(value, Mapping):
            for item_key, item_value in value.items():
                if item_key == key:
                    found.append(copy.deepcopy(item_value))
                walk(item_value)
        elif isinstance(value, Sequence) and not isinstance(
            value,
            (str, bytes, bytearray),
        ):
            for item in value:
                walk(item)

    walk(values)
    return found


def _entries_have_token(entries: Sequence[Any], tokens: Sequence[str]) -> bool:
    lowered_tokens = tuple(token.lower() for token in tokens)
    for entry in entries:
        text = json.dumps(entry, sort_keys=True, default=str).lower()
        if any(token in text for token in lowered_tokens):
            return True
    return False


def _entries_have_outcome(entries: Sequence[Any], outcomes: Sequence[str]) -> bool:
    outcome_set = {outcome.upper() for outcome in outcomes}
    for entry in entries:
        outcome = _entry_outcome(entry)
        if outcome and outcome.upper() in outcome_set:
            return True
    return False


def _is_true(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "y"}
    return False


def _nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    return True


def _first_declared(*values: Any) -> Any:
    for value in values:
        if _basis_declared(value) or _nonempty(value):
            return value
    return None


def _normalize_token(value: Any) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        value = str(value)
    normalized = value.strip()
    return normalized.upper() if normalized else None


def _block_reason(block_code: Any) -> str | None:
    if not block_code:
        return None
    return BLOCK_REASONS.get(str(block_code), str(block_code))


def _display_path(path: Path | None) -> str | None:
    if path is None:
        return None
    try:
        return str(path.resolve())
    except OSError:
        return str(path)


def _safe_filename_part(value: Any) -> str:
    text = str(value or "divergence_consequence").strip()
    safe = []
    for char in text:
        if char.isalnum() or char in {"-", "_"}:
            safe.append(char)
        else:
            safe.append("_")
    collapsed = "".join(safe).strip("_")
    return collapsed[:160] or "divergence_consequence"


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
        "divergence_resolved",
        "truth_created",
        "action_authorized",
        "divergence_consequence_erased_evidence",
        "divergence_consequence_hid_refusal",
        "divergence_consequence_hid_divergence",
        "divergence_consequence_hid_blocked_attempt",
        "divergence_consequence_hid_projection_mismatch",
        "summary_overrode_detailed_basis",
        "latest_file_consequence",
        "latest_turn_consequence",
        "majority_carrier_consequence",
        "successful_receipt_count_consequence",
        "distributed_standing_created",
        "repository_synchronization_authorized",
        "full_body_transfer_authorized",
        "second_body_created",
        "continuation_authorized",
        "distributed_operation_authorized",
        "mutation_performed",
        "replay_performed",
        "merge_performed",
        "required_non_claims_preserved",
    )
    return {key: copy.deepcopy(non_claims.get(key)) for key in keys if key in non_claims}
