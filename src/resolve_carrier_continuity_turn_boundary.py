"""Bounded carrier continuity-turn boundary resolver.

This resolver records one bounded carrier continuity-turn posture: how
carrier-related continuity is preserved across turns without flattening,
overwrite, latest-file currentness, summary authority, or predecessor mutation.
It preserves turn/pass/lineage posture only. It does not implement a generic
continuity subsystem, cross-carrier currentness successor law, registry,
persistence, distributed standing, repository synchronization, full body
transfer, continuation, distributed operation, or workflow machinery.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CarrierContinuityTurnBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit continuity inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


REPO_ROOT = Path(__file__).resolve().parents[1]

CARRIER_CONTINUITY_TURN_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_carrier_continuity_turn_boundary"
)

RESOLVER_MODULE = "resolve_carrier_continuity_turn_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "carrier_continuity_turn_boundary_result"

RECORD_INTENT = "RECORD_CARRIER_CONTINUITY_TURN"
DO_NOT_RECORD_INTENT = "DO_NOT_RECORD_CARRIER_CONTINUITY_TURN"
BLOCK_INTENT = "BLOCK_CARRIER_CONTINUITY_TURN"
SUPPORTED_CONTINUITY_TURN_INTENTS = {
    RECORD_INTENT,
    DO_NOT_RECORD_INTENT,
    BLOCK_INTENT,
}

CARRIER_CONTINUITY_TURN_RECORDED = "CARRIER_CONTINUITY_TURN_RECORDED"
CARRIER_CONTINUITY_TURN_NOT_RECORDED = "CARRIER_CONTINUITY_TURN_NOT_RECORDED"
CARRIER_CONTINUITY_TURN_BLOCKED = "CARRIER_CONTINUITY_TURN_BLOCKED"

SUPPORTED_TURN_KINDS = {
    "EXPERIMENT_DECLARATION_TURN",
    "PHYSICAL_RECEIPT_ATTEMPT_TURN",
    "RETURNED_EVIDENCE_TURN",
    "ADMISSION_AS_EVIDENCE_TURN",
    "DIVERGENCE_RECORDING_TURN",
    "CURRENTNESS_PARTICIPATION_TURN",
    "RELATION_RECOGNITION_TURN",
    "RELATION_CONFORMANCE_TURN",
    "RELATION_CLOSURE_TURN",
    "LIFECYCLE_STATUS_TURN",
    "REGISTRY_PERSISTENCE_REFERENCE_TURN",
    "STANDING_PROPAGATION_TURN",
    "PROJECTION_SUCCESSOR_TURN",
    "CONFORMANCE_SUCCESSOR_TURN",
    "CLOSURE_SUCCESSOR_TURN",
    "BLOCKED_TURN",
}

SUCCESSOR_TURN_KINDS = {
    "PROJECTION_SUCCESSOR_TURN",
    "CONFORMANCE_SUCCESSOR_TURN",
    "CLOSURE_SUCCESSOR_TURN",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "carrier_continuity_turn_created_source": False,
    "carrier_continuity_turn_created_currentness": False,
    "carrier_continuity_turn_created_authority": False,
    "carrier_continuity_turn_created_permission": False,
    "carrier_continuity_turn_created_hierarchy": False,
    "carrier_continuity_turn_created_distributed_standing": False,
    "carrier_continuity_turn_authorized_sync": False,
    "carrier_continuity_turn_authorized_full_body_transfer": False,
    "carrier_continuity_turn_created_second_body": False,
    "carrier_continuity_turn_authorized_continuation": False,
    "carrier_continuity_turn_authorized_distributed_operation": False,
    "carrier_continuity_turn_erased_evidence": False,
    "carrier_continuity_turn_hid_refusal": False,
    "carrier_continuity_turn_hid_divergence": False,
    "carrier_continuity_turn_hid_projection_mismatch": False,
    "carrier_continuity_turn_mutated_predecessor": False,
    "summary_overrode_detailed_basis": False,
    "latest_turn_currentness": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
    "distributed_standing_created": False,
    "repository_synchronization_authorized": False,
    "full_body_transfer_authorized": False,
    "second_body_created": False,
    "continuation_authorized": False,
    "distributed_operation_authorized": False,
}

BLOCK_REASONS = {
    "DECLARED_CONTINUITY_TURN_REQUEST_UNREADABLE": "Declared continuity-turn request path could not be read.",
    "DECLARED_CONTINUITY_TURN_REQUEST_MALFORMED": "Declared continuity-turn request is not a JSON object or mapping.",
    "CARRIER_CONTINUITY_TURN_REQUEST_EXPLICITLY_BLOCKED": "Continuity-turn request explicitly declares a blocked posture.",
    "CONTINUITY_TURN_QUESTION_UNDECLARED": "Continuity-turn question is undeclared.",
    "CONTINUITY_TURN_INTENT_UNSUPPORTED": "Continuity-turn intent is unsupported.",
    "SELECTED_ARTIFACT_MISSING": "Selected artifact is missing.",
    "SELECTED_ARTIFACT_MALFORMED": "Selected artifact is malformed.",
    "SELECTED_ARTIFACT_IDENTITY_MISSING": "Selected artifact identity is missing.",
    "SELECTED_ARTIFACT_OUTCOME_MISSING": "Selected artifact outcome is missing where required.",
    "TURN_KIND_UNSUPPORTED": "Turn kind is missing or unsupported.",
    "TURN_BASIS_MISSING": "Turn basis is missing.",
    "PREDECESSOR_REQUIRED_BUT_MISSING": "Predecessor is required but missing.",
    "SUCCESSOR_RELATION_PREDECESSOR_MISSING": "Successor relation is claimed but predecessor is missing.",
    "SUCCESSOR_REASON_MISSING": "Successor reason is missing where successor is claimed.",
    "PROJECTION_MISMATCH_HIDDEN": "Projection mismatch is hidden.",
    "BLOCKED_ATTEMPT_HIDDEN": "Blocked attempt is hidden.",
    "REFUSAL_HIDDEN": "Refusal is hidden.",
    "DIVERGENCE_HIDDEN": "Divergence is hidden.",
    "SUMMARY_OVERWRITES_DETAILED_BASIS": "Summary projection overwrites detailed basis.",
    "PREDECESSOR_MUTATED_OR_ERASED": "Predecessor is mutated or erased.",
    "TURN_CREATES_CURRENTNESS": "Turn creates currentness.",
    "TURN_CREATES_AUTHORITY": "Turn creates authority.",
    "TURN_CREATES_PERMISSION": "Turn creates permission.",
    "TURN_REPLACES_SOURCE": "Turn replaces source.",
    "TURN_ERASES_EVIDENCE": "Turn erases evidence.",
    "TURN_CREATES_CARRIER_HIERARCHY": "Turn creates carrier hierarchy.",
    "TURN_SELECTS_CURRENT_CARRIER": "Turn selects a current carrier.",
    "TURN_SELECTS_WINNING_CARRIER": "Turn selects a winning carrier.",
    "TURN_INVALIDATES_LOSING_CARRIER": "Turn invalidates a losing carrier.",
    "TURN_CREATES_DISTRIBUTED_STANDING": "Turn creates distributed standing.",
    "TURN_AUTHORIZES_REPOSITORY_SYNC": "Turn authorizes repository synchronization.",
    "TURN_AUTHORIZES_FULL_BODY_TRANSFER": "Turn authorizes full body transfer.",
    "TURN_CREATES_SECOND_BODY": "Turn creates a second body.",
    "TURN_AUTHORIZES_CONTINUATION": "Turn authorizes continuation.",
    "TURN_AUTHORIZES_DISTRIBUTED_OPERATION": "Turn authorizes distributed operation.",
    "LATEST_TURN_CURRENTNESS": "Latest turn is treated as currentness.",
    "LATEST_FILE_CURRENTNESS": "Latest file or recency is treated as currentness.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge was detected.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required continuity-turn non-claim is missing or flipped.",
}

CONTINUITY_TURN_NON_MEANING = {
    "does_not_mean_currentness": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_distributed_standing": True,
    "does_not_mean_source_replacement": True,
    "does_not_mean_carrier_hierarchy": True,
    "does_not_mean_carrier_priority": True,
    "does_not_mean_carrier_sovereignty": True,
    "does_not_mean_workflow_authorization": True,
    "does_not_mean_continuation": True,
    "does_not_mean_action": True,
    "does_not_mean_consequence": True,
    "does_not_mean_truth": True,
    "does_not_mean_final_governance": True,
    "does_not_mean_final_system_identity": True,
    "does_not_mean_automatic_successor": True,
    "does_not_mean_patch_permission": True,
    "does_not_mean_overwrite_permission": True,
    "does_not_mean_evidence_erasure": True,
    "does_not_mean_summary_authority": True,
    "does_not_mean_registry_authority": True,
    "does_not_mean_latest_file_currentness": True,
    "does_not_mean_latest_turn_currentness": True,
    "does_not_mean_distributed_operation": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_standing_propagation_implementation": True,
    "does_not_mean_currentness_successor_law": True,
    "does_not_mean_distributed_standing_prerequisite_completion": True,
}

WHAT_REMAINS_OPEN = {
    "carrier_continuity_turn_implementation_refinement": True,
    "cross_carrier_currentness_successor_law": True,
    "divergence_consequence_law": True,
    "distributed_standing_boundary": True,
    "distributed_standing": True,
    "carrier_registry_implementation": True,
    "persistence_implementation": True,
    "standing_propagation_implementation_beyond_boundary_recording": True,
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


def resolve_carrier_continuity_turn_boundary(
    declared_continuity_turn_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded carrier continuity-turn posture request."""

    if declared_continuity_turn_request is None:
        return _resolve_continuity_turn({}, None, [])
    if not isinstance(declared_continuity_turn_request, Mapping):
        return _resolve_continuity_turn(
            {},
            None,
            ["DECLARED_CONTINUITY_TURN_REQUEST_MALFORMED"],
        )
    return _resolve_continuity_turn(
        copy.deepcopy(dict(declared_continuity_turn_request)),
        None,
        [],
    )


def resolve_carrier_continuity_turn_boundary_from_path(
    declared_continuity_turn_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one bounded carrier continuity-turn posture request from JSON."""

    path = Path(declared_continuity_turn_request_path)
    try:
        request = _read_json_mapping(path)
    except CarrierContinuityTurnBoundaryError as exc:
        return _resolve_continuity_turn({}, path, [exc.block_code])
    return _resolve_continuity_turn(request, path, [])


def write_carrier_continuity_turn_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an additive carrier continuity-turn result without overwriting."""

    if not isinstance(result, Mapping):
        raise CarrierContinuityTurnBoundaryError(
            "DECLARED_CONTINUITY_TURN_REQUEST_MALFORMED",
            "Carrier continuity-turn result must be a mapping.",
        )

    if output_path is None:
        summary = _as_mapping(result.get("carrier_continuity_turn_summary"))
        basis_id = (
            summary.get("continuity_turn_request_id")
            or summary.get("turn_kind")
            or "carrier_continuity_turn"
        )
        output_path = CARRIER_CONTINUITY_TURN_BOUNDARY_ROOT / (
            f"{_safe_filename_part(basis_id)}__carrier_continuity_turn_result.json"
        )

    target = _non_overwriting_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, ensure_ascii=False, default=str)
        + "\n",
        encoding="utf-8",
    )
    return target


def build_carrier_continuity_turn_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact continuity-turn summary from the full result body."""

    checks = _mapping_list(result.get("continuity_turn_checks"))
    question = _as_mapping(result.get("declared_continuity_turn_question"))
    selected = _as_mapping(result.get("selected_artifact"))
    kind = _as_mapping(result.get("turn_kind"))
    basis = _as_mapping(result.get("turn_basis"))
    relation = _as_mapping(result.get("predecessor_successor_relation"))
    projection = _as_mapping(result.get("projection_correspondence"))
    blocked = _as_mapping(result.get("blocked_or_refusal_turns"))
    statement = _as_mapping(result.get("continuity_turn_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "continuity_turn_request_id": question.get("continuity_turn_request_id"),
        "continuity_turn_question": question.get("continuity_turn_question"),
        "continuity_turn_intent": question.get("continuity_turn_intent"),
        "selected_artifact_id": selected.get("selected_artifact_id"),
        "selected_artifact_outcome": selected.get("selected_artifact_outcome"),
        "turn_kind": kind.get("turn_kind"),
        "turn_basis": basis.get("raw_turn_basis"),
        "predecessor_artifact_id": relation.get("predecessor_artifact_id"),
        "successor_artifact_id": relation.get("successor_artifact_id"),
        "successor_relation": relation.get("successor_relation"),
        "successor_reason": relation.get("successor_reason"),
        "projection_correspondence_status": projection.get(
            "projection_correspondence_status"
        ),
        "projection_mismatch_visible": bool(
            statement.get("projection_mismatch_visible")
        ),
        "blocked_attempts_preserved": bool(
            statement.get("blocked_attempts_preserved")
        ),
        "refusal_preserved": bool(statement.get("refusal_preserved")),
        "divergence_preserved": bool(statement.get("divergence_preserved")),
        "detailed_basis_distinguished_from_summary": bool(
            statement.get("detailed_basis_distinguished_from_summary")
        ),
        "summary_overrode_detailed_basis": bool(
            statement.get("summary_overrode_detailed_basis")
        ),
        "predecessor_mutated_or_erased": bool(
            statement.get("predecessor_mutated_or_erased")
        ),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "continuity_turn_recorded": bool(
            statement.get("carrier_continuity_turn_recorded")
        ),
        "no_currentness_authority_permission_source_replacement": not bool(
            statement.get("currentness_created")
            or statement.get("authority_created")
            or statement.get("permission_created")
            or statement.get("source_replaced")
        ),
        "no_evidence_erasure": not bool(statement.get("evidence_erased")),
        "no_carrier_hierarchy": not bool(statement.get("carrier_hierarchy_created")),
        "no_current_winning_losing_carrier_collapse": not bool(
            statement.get("current_carrier_selected")
            or statement.get("winning_carrier_selected")
            or statement.get("losing_carrier_invalidated")
        ),
        "no_distributed_standing": not bool(statement.get("distributed_standing_created")),
        "no_sync_full_body_transfer_second_body": not bool(
            statement.get("repository_synchronization_authorized")
            or statement.get("full_body_transfer_authorized")
            or statement.get("second_body_created")
        ),
        "no_continuation": not bool(statement.get("continuation_authorized")),
        "no_distributed_operation": not bool(statement.get("distributed_operation_authorized")),
        "no_latest_turn_file_currentness": not bool(
            statement.get("latest_turn_currentness")
            or statement.get("latest_file_currentness")
        ),
        "blocked_or_refusal_turns": blocked.get("raw_blocked_or_refusal_turns"),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_declared_carrier_continuity_turn_request(
    continuity_turn_request_id: str,
    continuity_turn_question: str,
    selected_artifact: Mapping[str, Any],
    turn_kind: str,
    turn_basis: Mapping[str, Any] | str,
    continuity_turn_intent: str = RECORD_INTENT,
    *,
    predecessor_artifact: Mapping[str, Any] | None = None,
    successor_artifact: Mapping[str, Any] | None = None,
    successor_reason: str | None = None,
    projection_correspondence: Mapping[str, Any] | None = None,
    blocked_or_refusal_turns: Sequence[Mapping[str, Any]] | None = None,
    related_carrier_evidence: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Build one bounded continuity-turn request without inferring force."""

    request: dict[str, Any] = {
        "continuity_turn_request_id": continuity_turn_request_id,
        "continuity_turn_question": continuity_turn_question,
        "continuity_turn_intent": continuity_turn_intent,
        "selected_artifact": copy.deepcopy(dict(selected_artifact)),
        "turn_kind": turn_kind,
        "turn_basis": copy.deepcopy(turn_basis),
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }
    if predecessor_artifact is not None:
        request["predecessor_artifact"] = copy.deepcopy(dict(predecessor_artifact))
    if successor_artifact is not None:
        request["successor_artifact"] = copy.deepcopy(dict(successor_artifact))
    if predecessor_artifact is not None or successor_artifact is not None:
        request["successor_relation"] = {
            "successor_relation_claimed": True,
            "predecessor_artifact_id": _extract_identity(predecessor_artifact),
            "successor_artifact_id": _extract_identity(successor_artifact),
            "successor_is_additive": True,
            "successor_does_not_overwrite_predecessor": True,
        }
    if successor_reason is not None:
        request["successor_reason"] = successor_reason
    if projection_correspondence is not None:
        request["projection_correspondence"] = copy.deepcopy(
            dict(projection_correspondence)
        )
    if blocked_or_refusal_turns is not None:
        request["blocked_or_refusal_turns"] = [
            copy.deepcopy(dict(item))
            for item in blocked_or_refusal_turns
            if isinstance(item, Mapping)
        ]
    if related_carrier_evidence is not None:
        request["related_carrier_evidence"] = [
            copy.deepcopy(dict(item))
            for item in related_carrier_evidence
            if isinstance(item, Mapping)
        ]
    return request


def _resolve_continuity_turn(
    request: Mapping[str, Any],
    request_path: Path | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    question = _declared_continuity_turn_question(request, request_path)
    selected = _selected_artifact_section(request)
    kind = _turn_kind_section(request)
    basis = _turn_basis_section(request)
    relation = _predecessor_successor_relation_section(request, kind)
    projection = _projection_correspondence_section(request)
    blocked_turns = _blocked_or_refusal_turns_section(request)
    related_evidence = _related_carrier_evidence_section(request)
    non_claims = _non_claims_section(request, question)
    checks = _build_checks(
        request,
        question,
        selected,
        kind,
        basis,
        relation,
        projection,
        blocked_turns,
        related_evidence,
        non_claims,
        precheck_failures,
    )

    failed_checks = [check for check in checks if check.get("passed") is False]
    explicit_block_code = _explicit_block_code(request)
    if failed_checks:
        outcome = CARRIER_CONTINUITY_TURN_BLOCKED
        block_code = failed_checks[0].get("block_code")
    elif question.get("continuity_turn_intent") == BLOCK_INTENT:
        outcome = CARRIER_CONTINUITY_TURN_BLOCKED
        block_code = explicit_block_code
    elif question.get("continuity_turn_intent") == DO_NOT_RECORD_INTENT:
        outcome = CARRIER_CONTINUITY_TURN_NOT_RECORDED
        block_code = None
    else:
        outcome = CARRIER_CONTINUITY_TURN_RECORDED
        block_code = None

    block = {
        "blocked": outcome == CARRIER_CONTINUITY_TURN_BLOCKED,
        "block_code": block_code,
        "block_reason": _block_reason(block_code),
    }
    statement = _continuity_turn_statement(
        outcome,
        question,
        selected,
        kind,
        basis,
        relation,
        projection,
        blocked_turns,
        checks,
        block,
    )
    metadata = _metadata(question, selected, kind, outcome)
    result: dict[str, Any] = {
        "carrier_continuity_turn_metadata": metadata,
        "declared_continuity_turn_question": question,
        "selected_artifact": selected,
        "turn_kind": kind,
        "turn_basis": basis,
        "predecessor_successor_relation": relation,
        "projection_correspondence": projection,
        "blocked_or_refusal_turns": blocked_turns,
        "related_carrier_evidence": related_evidence,
        "continuity_turn_checks": checks,
        "continuity_turn_statement": statement,
        "continuity_turn_non_meaning": copy.deepcopy(CONTINUITY_TURN_NON_MEANING),
        "what_remains_open": copy.deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    result["carrier_continuity_turn_summary"] = build_carrier_continuity_turn_summary(
        result
    )
    return result


def _declared_continuity_turn_question(
    request: Mapping[str, Any],
    request_path: Path | None,
) -> dict[str, Any]:
    raw_intent = request.get("continuity_turn_intent")
    intent = _normalize_token(raw_intent)
    declared_non_claims = _as_mapping(
        request.get("declared_non_claims") or request.get("non_claims")
    )
    return {
        "continuity_turn_request_id": request.get("continuity_turn_request_id"),
        "continuity_turn_question": request.get("continuity_turn_question"),
        "continuity_turn_intent": intent,
        "raw_continuity_turn_intent": raw_intent,
        "request_path": _display_path(request_path),
        "not_recorded_reason": request.get("not_recorded_reason")
        or (
            "declared request does not record carrier continuity-turn posture"
            if intent == DO_NOT_RECORD_INTENT
            else None
        ),
        "declared_non_claims": declared_non_claims,
        "carrier_continuity_turn_is_not_currentness": True,
        "turn_is_not_authority": True,
        "turn_is_not_permission": True,
        "successor_is_not_overwrite": True,
        "summary_is_not_artifact_body": True,
        "registry_presence_is_not_continuity": True,
        "latest_turn_is_not_currentness": True,
        "distributed_standing_not_created": True,
        "repository_synchronization_not_authorized": True,
        "full_body_transfer_not_authorized": True,
        "continuation_not_authorized": True,
        "distributed_operation_not_authorized": True,
    }


def _selected_artifact_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("selected_artifact")
    declared = raw is not None
    parseable = isinstance(raw, Mapping) or isinstance(raw, str)
    selected_id = _extract_identity(raw)
    selected_outcome = (
        request.get("selected_artifact_outcome")
        or _field_from_mapping(
            raw,
            (
                "selected_artifact_outcome",
                "artifact_outcome",
                "result_outcome",
                "outcome",
                "status",
            ),
        )
    )
    outcome_required = _is_true(
        request.get("selected_artifact_outcome_required")
        or _field_from_mapping(raw, ("selected_artifact_outcome_required",))
    )
    artifact_type = _field_from_mapping(
        raw,
        ("artifact_type", "result_type", "type", "artifact_class", "evidence_class"),
    )
    return {
        "selected_artifact_declared": declared,
        "selected_artifact_parseable": parseable if declared else False,
        "selected_artifact_id": selected_id,
        "selected_artifact_identity_present": _nonempty(selected_id),
        "selected_artifact_outcome": selected_outcome,
        "selected_artifact_outcome_required": outcome_required,
        "selected_artifact_outcome_present": _nonempty(selected_outcome),
        "selected_artifact_type_or_class": artifact_type,
        "raw_selected_artifact": copy.deepcopy(raw),
        "selected_artifact_preserved": declared and parseable and _nonempty(selected_id),
        "selected_artifact_remains_evidence_or_reference": True,
        "selected_artifact_is_not_currentness": True,
        "selected_artifact_is_not_distributed_standing": True,
    }


def _turn_kind_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("turn_kind")
    turn_kind = _normalize_token(raw)
    return {
        "turn_kind": turn_kind,
        "raw_turn_kind": raw,
        "turn_kind_supported": turn_kind in SUPPORTED_TURN_KINDS,
        "supported_turn_kinds": sorted(SUPPORTED_TURN_KINDS),
        "turn_kind_is_not_currentness": True,
        "turn_kind_is_not_authority": True,
    }


def _turn_basis_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("turn_basis")
    dimensions = {
        "selected_carrier_ids": copy.deepcopy(request.get("selected_carrier_ids")),
        "selected_surface_or_artifact_id": request.get("selected_surface_or_artifact_id"),
        "source_basis_id": request.get("source_basis_id"),
        "carried_basis_id": request.get("carried_basis_id"),
        "receipt_or_refusal_basis_id": request.get("receipt_or_refusal_basis_id"),
        "admission_basis_id": request.get("admission_basis_id"),
        "divergence_basis_id": request.get("divergence_basis_id"),
        "currentness_participation_basis_id": request.get(
            "currentness_participation_basis_id"
        ),
        "relation_basis_id": request.get("relation_basis_id"),
        "conformance_basis_id": request.get("conformance_basis_id"),
        "closure_basis_id": request.get("closure_basis_id"),
        "lifecycle_basis_id": request.get("lifecycle_basis_id"),
        "registry_persistence_basis_id": request.get("registry_persistence_basis_id"),
        "standing_propagation_basis_id": request.get("standing_propagation_basis_id"),
        "detailed_basis_reference": copy.deepcopy(request.get("detailed_basis_reference")),
        "summary_projection_reference": copy.deepcopy(
            request.get("summary_projection_reference")
        ),
    }
    return {
        "turn_basis_declared": _basis_declared(raw),
        "raw_turn_basis": copy.deepcopy(raw),
        "turn_basis_preserved": _basis_declared(raw),
        "continuity_turn_dimensions": dimensions,
        "turn_basis_is_not_authority": True,
        "turn_basis_is_not_currentness": True,
        "turn_basis_does_not_authorize_continuation": True,
    }


def _predecessor_successor_relation_section(
    request: Mapping[str, Any],
    kind: Mapping[str, Any],
) -> dict[str, Any]:
    predecessor = request.get("predecessor_artifact")
    successor = request.get("successor_artifact")
    relation = request.get("successor_relation")
    reason = request.get("successor_reason")
    turn_kind = kind.get("turn_kind")
    successor_claimed = bool(
        turn_kind in SUCCESSOR_TURN_KINDS
        or _basis_declared(successor)
        or _basis_declared(relation)
        or _nonempty(reason)
        or _is_true(request.get("successor_relation_claimed"))
    )
    predecessor_required = bool(
        successor_claimed or _is_true(request.get("predecessor_required"))
    )
    predecessor_id = _extract_identity(predecessor)
    successor_id = _extract_identity(successor)
    relation_declared = _basis_declared(relation)
    return {
        "raw_predecessor_artifact": copy.deepcopy(predecessor),
        "predecessor_artifact_id": predecessor_id,
        "predecessor_artifact_declared": _basis_declared(predecessor),
        "predecessor_required": predecessor_required,
        "predecessor_preserved": (
            _nonempty(predecessor_id) if _basis_declared(predecessor) else False
        ),
        "raw_successor_artifact": copy.deepcopy(successor),
        "successor_artifact_id": successor_id,
        "successor_artifact_declared": _basis_declared(successor),
        "successor_relation": copy.deepcopy(relation),
        "successor_relation_claimed": successor_claimed,
        "successor_relation_declared": relation_declared,
        "successor_relation_preserved": bool(
            not successor_claimed or relation_declared
        ),
        "successor_reason": reason,
        "successor_reason_required": successor_claimed,
        "successor_reason_preserved": bool(
            not successor_claimed or _nonempty(reason)
        ),
        "successor_does_not_overwrite_predecessor": True,
        "successor_does_not_invalidate_predecessor": not _any_flag_true(
            [request, _as_mapping(relation)],
            (
                "successor_invalidated_predecessor",
                "predecessor_invalidated_by_successor",
            ),
        ),
    }


def _projection_correspondence_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("projection_correspondence")
    raw_mapping = _as_mapping(raw)
    detailed_ref = request.get("detailed_basis_reference") or raw_mapping.get(
        "detailed_basis_reference"
    )
    summary_ref = request.get("summary_projection_reference") or raw_mapping.get(
        "summary_projection_reference"
    )
    status = (
        raw_mapping.get("projection_correspondence_status")
        or raw_mapping.get("correspondence_status")
        or raw_mapping.get("status")
    )
    mismatch_applicable = bool(
        _any_flag_true(
            [request, raw_mapping],
            (
                "projection_mismatch_applicable",
                "projection_mismatch_present",
                "projection_mismatch_detected",
                "summary_under_projected_detailed_basis",
            ),
        )
        or _text_has_any_token(status, ("mismatch", "under_project", "under-project"))
    )
    mismatch_hidden = _any_flag_true(
        [request, raw_mapping],
        (
            "projection_mismatch_hidden",
            "carrier_continuity_turn_hid_projection_mismatch",
            "hid_projection_mismatch",
        ),
    )
    mismatch_visible = bool(
        not mismatch_applicable
        or (
            not mismatch_hidden
            and (
                _any_flag_true(
                    [request, raw_mapping],
                    (
                        "projection_mismatch_visible",
                        "mismatch_visible",
                        "projection_mismatch_preserved",
                    ),
                )
                or _basis_declared(raw)
            )
        )
    )
    detailed_distinguishable = bool(
        _any_flag_true(
            [request, raw_mapping],
            (
                "detailed_basis_distinguished_from_summary",
                "detailed_basis_distinguishable_from_summary",
            ),
        )
        or (_basis_declared(detailed_ref) and _basis_declared(summary_ref))
    )
    correspondence_supplied = bool(
        _basis_declared(raw) or _basis_declared(detailed_ref) or _basis_declared(summary_ref)
    )
    return {
        "raw_projection_correspondence": copy.deepcopy(raw),
        "projection_correspondence_declared": correspondence_supplied,
        "projection_correspondence_status": status,
        "projection_correspondence_preserved": correspondence_supplied,
        "projection_mismatch_applicable": mismatch_applicable,
        "projection_mismatch_visible": mismatch_visible,
        "projection_mismatch_hidden": mismatch_hidden,
        "detailed_basis_reference": copy.deepcopy(detailed_ref),
        "summary_projection_reference": copy.deepcopy(summary_ref),
        "detailed_basis_distinguished_from_summary": detailed_distinguishable,
        "summary_overrode_detailed_basis": _any_flag_true(
            [request, raw_mapping],
            (
                "summary_overrode_detailed_basis",
                "summary_overwrites_detailed_basis",
                "summary_projection_overrode_detailed_basis",
            ),
        ),
    }


def _blocked_or_refusal_turns_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("blocked_or_refusal_turns")
    entries = _entries_from_value(raw)
    related_entries = _entries_from_value(request.get("related_carrier_evidence"))
    all_entries = entries + related_entries
    blocked_applicable = _entries_have_token(all_entries, ("blocked", "block", "failed"))
    refusal_applicable = _entries_have_token(all_entries, ("refusal", "refused", "blocked"))
    divergence_applicable = _entries_have_token(all_entries, ("divergence", "mismatch"))
    blocked_hidden = _any_flag_true(
        [request, _as_mapping(raw)],
        ("blocked_attempt_hidden", "blocked_attempts_hidden"),
    )
    refusal_hidden = _any_flag_true(
        [request, _as_mapping(raw)],
        ("refusal_hidden", "carrier_continuity_turn_hid_refusal"),
    )
    divergence_hidden = _any_flag_true(
        [request, _as_mapping(raw)],
        ("divergence_hidden", "carrier_continuity_turn_hid_divergence"),
    )
    return {
        "raw_blocked_or_refusal_turns": copy.deepcopy(raw),
        "blocked_or_refusal_turn_entries": entries,
        "blocked_attempt_applicable": blocked_applicable,
        "blocked_attempts_preserved": bool(blocked_applicable and not blocked_hidden),
        "blocked_attempt_hidden": blocked_hidden,
        "refusal_applicable": refusal_applicable,
        "refusal_preserved": bool(refusal_applicable and not refusal_hidden),
        "refusal_hidden": refusal_hidden,
        "divergence_applicable": divergence_applicable,
        "divergence_preserved": bool(divergence_applicable and not divergence_hidden),
        "divergence_hidden": divergence_hidden,
        "blocked_turn_does_not_invalidate_body": True,
        "refusal_does_not_erase_success": True,
        "success_does_not_erase_refusal": True,
    }


def _related_carrier_evidence_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("related_carrier_evidence")
    entries = _entries_from_value(raw)
    return {
        "raw_related_carrier_evidence": copy.deepcopy(raw),
        "related_carrier_evidence_entries": entries,
        "related_carrier_evidence_ids": [
            _extract_identity(entry) for entry in entries if _extract_identity(entry)
        ],
        "related_carrier_evidence_outcomes": [
            entry.get("outcome") or entry.get("result_outcome") or entry.get("status")
            for entry in entries
            if entry.get("outcome") or entry.get("result_outcome") or entry.get("status")
        ],
        "related_carrier_evidence_preserved": bool(entries),
        "evidence_remains_evidence": True,
        "related_evidence_does_not_create_currentness": True,
        "related_evidence_does_not_create_distributed_standing": True,
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


def _build_checks(
    request: Mapping[str, Any],
    question: Mapping[str, Any],
    selected: Mapping[str, Any],
    kind: Mapping[str, Any],
    basis: Mapping[str, Any],
    relation: Mapping[str, Any],
    projection: Mapping[str, Any],
    blocked_turns: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
    non_claims: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    collapse_source = _without_safe_sections(request)
    sources = [
        collapse_source,
        question,
        selected,
        kind,
        basis,
        relation,
        projection,
        blocked_turns,
        related_evidence,
        non_claims,
    ]
    precheck_code = precheck_failures[0] if precheck_failures else None
    checks = [
        _check(
            "declared_continuity_turn_request_parseable_mapping",
            not precheck_failures,
            "declared continuity-turn request is a parseable mapping",
            list(precheck_failures),
            precheck_code or "DECLARED_CONTINUITY_TURN_REQUEST_MALFORMED",
        ),
        _check(
            "continuity_turn_question_declared",
            _nonempty(question.get("continuity_turn_question")),
            "continuity-turn question is declared",
            question.get("continuity_turn_question"),
            "CONTINUITY_TURN_QUESTION_UNDECLARED",
        ),
        _check(
            "continuity_turn_intent_supported",
            question.get("continuity_turn_intent")
            in SUPPORTED_CONTINUITY_TURN_INTENTS,
            "continuity-turn intent is supported",
            question.get("continuity_turn_intent"),
            "CONTINUITY_TURN_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_artifact_present",
            bool(selected.get("selected_artifact_declared")),
            "selected artifact is present",
            selected.get("raw_selected_artifact"),
            "SELECTED_ARTIFACT_MISSING",
        ),
        _check(
            "selected_artifact_parseable",
            bool(selected.get("selected_artifact_parseable")),
            "selected artifact is parseable",
            _shape(selected.get("raw_selected_artifact")),
            "SELECTED_ARTIFACT_MALFORMED",
        ),
        _check(
            "selected_artifact_identity_present",
            bool(selected.get("selected_artifact_identity_present")),
            "selected artifact identity is present",
            selected.get("selected_artifact_id"),
            "SELECTED_ARTIFACT_IDENTITY_MISSING",
        ),
        _check(
            "selected_artifact_outcome_preserved_where_required",
            not selected.get("selected_artifact_outcome_required")
            or bool(selected.get("selected_artifact_outcome_present")),
            "selected artifact outcome is present where required",
            selected.get("selected_artifact_outcome"),
            "SELECTED_ARTIFACT_OUTCOME_MISSING",
        ),
        _check(
            "turn_kind_supported",
            bool(kind.get("turn_kind_supported")),
            "turn kind is supported",
            kind.get("turn_kind"),
            "TURN_KIND_UNSUPPORTED",
        ),
        _check(
            "turn_basis_declared",
            bool(basis.get("turn_basis_declared")),
            "turn basis is declared",
            basis.get("raw_turn_basis"),
            "TURN_BASIS_MISSING",
        ),
        _check(
            "successor_relation_predecessor_present_where_claimed",
            not relation.get("successor_relation_declared")
            or bool(relation.get("predecessor_artifact_id")),
            "successor relation has predecessor where claimed",
            {
                "successor_relation_declared": relation.get(
                    "successor_relation_declared"
                ),
                "predecessor_artifact_id": relation.get("predecessor_artifact_id"),
            },
            "SUCCESSOR_RELATION_PREDECESSOR_MISSING",
        ),
        _check(
            "predecessor_preserved_where_required",
            not relation.get("predecessor_required")
            or bool(relation.get("predecessor_artifact_id")),
            "predecessor is preserved where required",
            relation.get("predecessor_artifact_id"),
            "PREDECESSOR_REQUIRED_BUT_MISSING",
        ),
        _check(
            "successor_relation_preserved_where_claimed",
            not relation.get("successor_relation_claimed")
            or bool(relation.get("successor_relation_declared")),
            "successor relation is preserved where claimed",
            relation.get("successor_relation"),
            "SUCCESSOR_RELATION_PREDECESSOR_MISSING",
        ),
        _check(
            "successor_reason_preserved_where_claimed",
            bool(relation.get("successor_reason_preserved")),
            "successor reason is preserved where claimed",
            relation.get("successor_reason"),
            "SUCCESSOR_REASON_MISSING",
        ),
        _check(
            "projection_mismatch_visible_where_applicable",
            not projection.get("projection_mismatch_applicable")
            or bool(projection.get("projection_mismatch_visible")),
            "projection mismatch remains visible where applicable",
            {
                "projection_mismatch_applicable": projection.get(
                    "projection_mismatch_applicable"
                ),
                "projection_mismatch_visible": projection.get(
                    "projection_mismatch_visible"
                ),
            },
            "PROJECTION_MISMATCH_HIDDEN",
        ),
        _check(
            "blocked_attempt_visible_where_applicable",
            not blocked_turns.get("blocked_attempt_applicable")
            or bool(blocked_turns.get("blocked_attempts_preserved")),
            "blocked attempts remain visible where applicable",
            blocked_turns.get("raw_blocked_or_refusal_turns"),
            "BLOCKED_ATTEMPT_HIDDEN",
        ),
        _check(
            "refusal_visible_where_applicable",
            not blocked_turns.get("refusal_applicable")
            or bool(blocked_turns.get("refusal_preserved")),
            "refusal remains visible where applicable",
            blocked_turns.get("raw_blocked_or_refusal_turns"),
            "REFUSAL_HIDDEN",
        ),
        _check(
            "divergence_visible_where_applicable",
            not blocked_turns.get("divergence_applicable")
            or bool(blocked_turns.get("divergence_preserved")),
            "divergence remains visible where applicable",
            blocked_turns.get("raw_blocked_or_refusal_turns"),
            "DIVERGENCE_HIDDEN",
        ),
        _check(
            "detailed_basis_distinguishable_from_summary_projection",
            not _projection_distinction_required(projection)
            or bool(projection.get("detailed_basis_distinguished_from_summary")),
            "detailed basis remains distinguishable from summary projection",
            {
                "detailed_basis_reference": projection.get("detailed_basis_reference"),
                "summary_projection_reference": projection.get(
                    "summary_projection_reference"
                ),
            },
            "SUMMARY_OVERWRITES_DETAILED_BASIS",
        ),
        _check(
            "summary_does_not_override_detailed_basis",
            not bool(projection.get("summary_overrode_detailed_basis")),
            "summary projection does not override detailed basis",
            projection.get("summary_overrode_detailed_basis"),
            "SUMMARY_OVERWRITES_DETAILED_BASIS",
        ),
        _check(
            "predecessor_not_mutated_or_erased",
            not _any_flag_true(
                sources,
                (
                    "predecessor_mutated_or_erased",
                    "carrier_continuity_turn_mutated_predecessor",
                    "predecessor_erased",
                    "predecessor_mutated",
                ),
            ),
            "predecessor is not mutated or erased",
            _matching_true_flags(
                sources,
                (
                    "predecessor_mutated_or_erased",
                    "carrier_continuity_turn_mutated_predecessor",
                    "predecessor_erased",
                    "predecessor_mutated",
                ),
            ),
            "PREDECESSOR_MUTATED_OR_ERASED",
        ),
        _check(
            "successor_does_not_invalidate_predecessor",
            bool(relation.get("successor_does_not_invalidate_predecessor")),
            "successor does not invalidate predecessor without separate basis",
            relation.get("successor_does_not_invalidate_predecessor"),
            "PREDECESSOR_MUTATED_OR_ERASED",
        ),
        _collapse_check(
            "latest_turn_not_currentness",
            sources,
            ("latest_turn_currentness", "latest_turn_treated_as_currentness"),
            "latest turn is not currentness",
            "LATEST_TURN_CURRENTNESS",
        ),
        _collapse_check(
            "latest_file_not_currentness",
            sources,
            ("latest_file_currentness", "recency_fraud"),
            "latest file and recency are not currentness",
            "LATEST_FILE_CURRENTNESS",
        ),
        _collapse_check(
            "no_currentness",
            sources,
            (
                "currentness_created",
                "carrier_continuity_turn_created_currentness",
                "turn_creates_currentness",
            ),
            "turn does not create currentness",
            "TURN_CREATES_CURRENTNESS",
        ),
        _collapse_check(
            "no_authority",
            sources,
            (
                "authority_created",
                "carrier_continuity_turn_created_authority",
                "turn_creates_authority",
            ),
            "turn does not create authority",
            "TURN_CREATES_AUTHORITY",
        ),
        _collapse_check(
            "no_permission",
            sources,
            (
                "permission_created",
                "carrier_continuity_turn_created_permission",
                "turn_creates_permission",
            ),
            "turn does not create permission",
            "TURN_CREATES_PERMISSION",
        ),
        _collapse_check(
            "no_source_replacement",
            sources,
            (
                "source_replaced",
                "carrier_continuity_turn_created_source",
                "turn_replaces_source",
            ),
            "turn does not replace source",
            "TURN_REPLACES_SOURCE",
        ),
        _collapse_check(
            "no_evidence_erasure",
            sources,
            (
                "evidence_erased",
                "carrier_continuity_turn_erased_evidence",
                "turn_erases_evidence",
            ),
            "turn does not erase evidence",
            "TURN_ERASES_EVIDENCE",
        ),
        _collapse_check(
            "no_carrier_hierarchy",
            sources,
            (
                "carrier_hierarchy_created",
                "carrier_continuity_turn_created_hierarchy",
                "turn_creates_carrier_hierarchy",
            ),
            "turn does not create carrier hierarchy",
            "TURN_CREATES_CARRIER_HIERARCHY",
        ),
        _collapse_check(
            "no_current_carrier_selected",
            sources,
            ("current_carrier_selected", "turn_selects_current_carrier"),
            "turn does not select current carrier",
            "TURN_SELECTS_CURRENT_CARRIER",
        ),
        _collapse_check(
            "no_winning_carrier_selected",
            sources,
            ("winning_carrier_selected", "turn_selects_winning_carrier"),
            "turn does not select winning carrier",
            "TURN_SELECTS_WINNING_CARRIER",
        ),
        _collapse_check(
            "no_losing_carrier_invalidated",
            sources,
            ("losing_carrier_invalidated", "turn_invalidates_losing_carrier"),
            "turn does not invalidate losing carrier",
            "TURN_INVALIDATES_LOSING_CARRIER",
        ),
        _collapse_check(
            "no_distributed_standing",
            sources,
            (
                "distributed_standing_created",
                "carrier_continuity_turn_created_distributed_standing",
                "turn_creates_distributed_standing",
            ),
            "turn does not create distributed standing",
            "TURN_CREATES_DISTRIBUTED_STANDING",
        ),
        _collapse_check(
            "no_repository_synchronization",
            sources,
            (
                "repository_synchronization_authorized",
                "carrier_continuity_turn_authorized_sync",
                "turn_authorizes_repository_sync",
            ),
            "turn does not authorize repository synchronization",
            "TURN_AUTHORIZES_REPOSITORY_SYNC",
        ),
        _collapse_check(
            "no_full_body_transfer",
            sources,
            (
                "full_body_transfer_authorized",
                "carrier_continuity_turn_authorized_full_body_transfer",
                "turn_authorizes_full_body_transfer",
            ),
            "turn does not authorize full body transfer",
            "TURN_AUTHORIZES_FULL_BODY_TRANSFER",
        ),
        _collapse_check(
            "no_second_body",
            sources,
            (
                "second_body_created",
                "carrier_continuity_turn_created_second_body",
                "turn_creates_second_body",
            ),
            "turn does not create second body",
            "TURN_CREATES_SECOND_BODY",
        ),
        _collapse_check(
            "no_continuation",
            sources,
            (
                "continuation_authorized",
                "carrier_continuity_turn_authorized_continuation",
                "turn_authorizes_continuation",
            ),
            "turn does not authorize continuation",
            "TURN_AUTHORIZES_CONTINUATION",
        ),
        _collapse_check(
            "no_distributed_operation",
            sources,
            (
                "distributed_operation_authorized",
                "carrier_continuity_turn_authorized_distributed_operation",
                "turn_authorizes_distributed_operation",
            ),
            "turn does not authorize distributed operation",
            "TURN_AUTHORIZES_DISTRIBUTED_OPERATION",
        ),
        _check(
            "no_mutation_replay_or_merge",
            not _any_flag_true(
                sources, ("mutation_performed", "replay_performed", "merge_performed")
            ),
            "mutation, replay, and merge are false",
            _matching_true_flags(
                sources, ("mutation_performed", "replay_performed", "merge_performed")
            ),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "non_claims_remain_false",
            bool(non_claims.get("required_non_claims_preserved")),
            "required continuity-turn non-claims are present and false",
            {
                "missing_required_non_claims": non_claims.get(
                    "missing_required_non_claims"
                ),
                "flipped_required_non_claims": non_claims.get(
                    "flipped_required_non_claims"
                ),
            },
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    return checks


def _continuity_turn_statement(
    outcome: str,
    question: Mapping[str, Any],
    selected: Mapping[str, Any],
    kind: Mapping[str, Any],
    basis: Mapping[str, Any],
    relation: Mapping[str, Any],
    projection: Mapping[str, Any],
    blocked_turns: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    block: Mapping[str, Any],
) -> dict[str, Any]:
    recorded = outcome == CARRIER_CONTINUITY_TURN_RECORDED
    return {
        "carrier_continuity_turn_recorded": recorded,
        "not_recorded_reason": (
            question.get("not_recorded_reason")
            if outcome == CARRIER_CONTINUITY_TURN_NOT_RECORDED
            else None
        ),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "failed_checks": [
            copy.deepcopy(dict(check)) for check in checks if check.get("passed") is False
        ],
        "selected_artifact_preserved": recorded
        and bool(selected.get("selected_artifact_preserved")),
        "selected_artifact_outcome_preserved": bool(
            selected.get("selected_artifact_outcome_present")
        ),
        "turn_kind_preserved": recorded and bool(kind.get("turn_kind_supported")),
        "turn_basis_preserved": recorded and bool(basis.get("turn_basis_preserved")),
        "predecessor_preserved": bool(relation.get("predecessor_artifact_id")),
        "successor_relation_preserved": bool(
            relation.get("successor_relation_declared")
        ),
        "successor_reason_preserved": bool(relation.get("successor_reason")),
        "projection_correspondence_preserved": bool(
            projection.get("projection_correspondence_preserved")
        ),
        "projection_mismatch_visible": bool(
            projection.get("projection_mismatch_applicable")
            and projection.get("projection_mismatch_visible")
        ),
        "blocked_attempts_preserved": bool(
            blocked_turns.get("blocked_attempts_preserved")
        ),
        "refusal_preserved": bool(blocked_turns.get("refusal_preserved")),
        "divergence_preserved": bool(blocked_turns.get("divergence_preserved")),
        "detailed_basis_distinguished_from_summary": bool(
            projection.get("detailed_basis_distinguished_from_summary")
        ),
        "summary_overrode_detailed_basis": False,
        "predecessor_mutated_or_erased": False,
        "latest_turn_currentness": False,
        "latest_file_currentness": False,
        "currentness_created": False,
        "authority_created": False,
        "permission_created": False,
        "source_replaced": False,
        "evidence_erased": False,
        "carrier_hierarchy_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "distributed_standing_created": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
    }


def _metadata(
    question: Mapping[str, Any],
    selected: Mapping[str, Any],
    kind: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    return {
        "carrier_continuity_turn_result_id": _result_id(question, selected, kind, outcome),
        "carrier_continuity_turn_result_type": RESULT_TYPE,
        "carrier_continuity_turn_result_version": RESULT_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "resolver_module": RESOLVER_MODULE,
        "selected_artifact_id": selected.get("selected_artifact_id"),
        "selected_turn_kind": kind.get("turn_kind"),
    }


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    target = Path(path)
    try:
        raw = target.read_text(encoding="utf-8")
    except OSError as exc:
        raise CarrierContinuityTurnBoundaryError(
            "DECLARED_CONTINUITY_TURN_REQUEST_UNREADABLE",
            f"Could not read declared continuity-turn request: {target}",
        ) from exc
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CarrierContinuityTurnBoundaryError(
            "DECLARED_CONTINUITY_TURN_REQUEST_MALFORMED",
            f"Declared continuity-turn request is malformed JSON: {target}",
        ) from exc
    if not isinstance(parsed, Mapping):
        raise CarrierContinuityTurnBoundaryError(
            "DECLARED_CONTINUITY_TURN_REQUEST_MALFORMED",
            "Declared continuity-turn request JSON must be an object.",
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
        "expected_posture": expected_posture,
        "actual_posture": copy.deepcopy(actual_posture),
        "block_code": None if passed else block_code,
    }


def _collapse_check(
    check_name: str,
    sources: Sequence[Mapping[str, Any]],
    aliases: Sequence[str],
    expected_posture: str,
    block_code: str,
) -> dict[str, Any]:
    return _check(
        check_name,
        not _any_flag_true(sources, aliases),
        expected_posture,
        _matching_true_flags(sources, aliases),
        block_code,
    )


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]


def _entries_from_value(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, Mapping):
        return [copy.deepcopy(dict(value))]
    if isinstance(value, list):
        return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]
    return []


def _basis_declared(value: Any) -> bool:
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return _nonempty(value)


def _nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def _normalize_token(value: Any) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().upper().replace("-", "_").replace(" ", "_")
    return normalized or None


def _shape(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, Mapping):
        return {"type": "mapping", "keys": sorted(str(key) for key in value.keys())}
    if isinstance(value, list):
        return {"type": "list", "length": len(value)}
    return {"type": type(value).__name__, "value": value}


def _block_reason(block_code: str | None) -> str | None:
    if block_code is None:
        return None
    return BLOCK_REASONS.get(
        block_code,
        f"Carrier continuity-turn blocked by {block_code}.",
    )


def _explicit_block_code(request: Mapping[str, Any]) -> str:
    requested = _normalize_token(
        request.get("declared_block_code")
        or request.get("block_code")
        or request.get("requested_block_code")
    )
    if requested and requested in BLOCK_REASONS:
        return requested
    return "CARRIER_CONTINUITY_TURN_REQUEST_EXPLICITLY_BLOCKED"


def _result_id(
    question: Mapping[str, Any],
    selected: Mapping[str, Any],
    kind: Mapping[str, Any],
    outcome: str,
) -> str:
    basis_id = (
        question.get("continuity_turn_request_id")
        or selected.get("selected_artifact_id")
        or kind.get("turn_kind")
        or "carrier_continuity_turn"
    )
    return f"{_safe_filename_part(basis_id)}__{_safe_filename_part(outcome.lower())}"


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    return {key: non_claims.get(key) for key in REQUIRED_NON_CLAIMS}


def _extract_identity(value: Any) -> Any:
    if isinstance(value, str):
        return value.strip() or None
    if not isinstance(value, Mapping):
        return None
    for field in (
        "selected_artifact_id",
        "artifact_id",
        "result_id",
        "evidence_id",
        "carrier_continuity_turn_artifact_id",
        "id",
    ):
        candidate = value.get(field)
        if _nonempty(candidate):
            return candidate
    metadata = value.get("metadata")
    if isinstance(metadata, Mapping):
        for field in (
            "result_id",
            "artifact_id",
            "standing_propagation_result_id",
            "carrier_registry_persistence_result_id",
            "carrier_lifecycle_result_id",
        ):
            candidate = metadata.get(field)
            if _nonempty(candidate):
                return candidate
    return None


def _field_from_mapping(value: Any, fields: Sequence[str]) -> Any:
    if not isinstance(value, Mapping):
        return None
    for field in fields:
        if field in value and _nonempty(value.get(field)):
            return value.get(field)
    return None


def _projection_distinction_required(projection: Mapping[str, Any]) -> bool:
    return bool(
        _basis_declared(projection.get("detailed_basis_reference"))
        or _basis_declared(projection.get("summary_projection_reference"))
        or projection.get("projection_mismatch_applicable")
    )


def _without_safe_sections(request: Mapping[str, Any]) -> dict[str, Any]:
    cleaned = copy.deepcopy(dict(request))
    for key in (
        "declared_non_claims",
        "non_claims",
        "continuity_turn_question",
        "selected_artifact",
        "turn_basis",
        "predecessor_artifact",
        "successor_artifact",
        "related_carrier_evidence",
        "blocked_or_refusal_turns",
    ):
        cleaned.pop(key, None)
    return cleaned


def _any_flag_true(
    sources: Sequence[Mapping[str, Any]],
    aliases: Sequence[str],
) -> bool:
    return bool(_matching_true_flags(sources, aliases))


def _matching_true_flags(
    sources: Sequence[Mapping[str, Any]],
    aliases: Sequence[str],
) -> dict[str, Any]:
    matches: dict[str, Any] = {}
    alias_set = set(aliases)
    for source in sources:
        if not isinstance(source, Mapping):
            continue
        for key, value in source.items():
            if key in alias_set and _is_true(value):
                matches[key] = value
            elif isinstance(value, Mapping):
                nested = _matching_true_flags([value], aliases)
                matches.update({f"{key}.{nested_key}": nested_value for nested_key, nested_value in nested.items()})
    return matches


def _is_true(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1"}
    return False


def _entries_have_token(entries: Sequence[Mapping[str, Any]], tokens: Sequence[str]) -> bool:
    normalized_tokens = tuple(token.lower() for token in tokens)
    return any(_entry_has_any_token(entry, normalized_tokens) for entry in entries)


def _entry_has_any_token(entry: Mapping[str, Any], tokens: Sequence[str]) -> bool:
    return _text_has_any_token(
        " ".join(
            str(value)
            for value in (
                entry.get("turn_id"),
                entry.get("turn_kind"),
                entry.get("evidence_id"),
                entry.get("artifact_id"),
                entry.get("outcome"),
                entry.get("result_outcome"),
                entry.get("status"),
                entry.get("role"),
                entry.get("evidence_role"),
                entry.get("evidence_class"),
                entry.get("description"),
            )
        ),
        tokens,
    )


def _text_has_any_token(value: Any, tokens: Sequence[str]) -> bool:
    text = str(value or "").lower()
    return any(token in text for token in tokens)


def _safe_filename_part(value: Any) -> str:
    raw = str(value or "carrier_continuity_turn").strip()
    cleaned = "".join(char if char.isalnum() or char in "._-" else "_" for char in raw)
    return cleaned.strip("._-") or "carrier_continuity_turn"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise CarrierContinuityTurnBoundaryError(
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "Could not allocate a non-overwriting carrier continuity-turn result path.",
    )


def _display_path(path: Path | None) -> str | None:
    if path is None:
        return None
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)
