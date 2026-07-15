"""Bounded additional physical carrier experiment declaration resolver.

This resolver records whether one additional physical receiving-carrier
experiment may be declared as one bounded receipt/refusal experiment over one
selected carried surface or packet. It declares scope only. It does not execute
the experiment, create a packet, create receipt evidence, admit returned
evidence, resolve divergence, create currentness, create distributed standing,
authorize repository synchronization, authorize full body transfer, authorize
self-orientation or conformance on the receiving carrier, authorize distributed
operation, authorize continuation, or authorize expansion by success.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class AdditionalPhysicalCarrierExperimentBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit experiment inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


REPO_ROOT = Path(__file__).resolve().parents[1]

ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_additional_physical_carrier_experiment_boundary"
)

RESOLVER_MODULE = "resolve_additional_physical_carrier_experiment_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "additional_physical_carrier_experiment_boundary_result"

DECLARE_INTENT = "DECLARE_ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT"
DO_NOT_DECLARE_INTENT = "DO_NOT_DECLARE_ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT"
BLOCK_INTENT = "BLOCK_ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT"
SUPPORTED_EXPERIMENT_INTENTS = {
    DECLARE_INTENT,
    DO_NOT_DECLARE_INTENT,
    BLOCK_INTENT,
}

ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_DECLARED = (
    "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_DECLARED"
)
ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_NOT_DECLARED = (
    "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_NOT_DECLARED"
)
ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_BLOCKED = (
    "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_BLOCKED"
)

SOURCE_ROLES = {"EXPERIMENT_SOURCE_CARRIER", "SOURCE_CARRIER_FOR_PACKET"}
RECEIVING_ROLES = {"EXPERIMENT_RECEIVING_CARRIER"}
PERMITTED_OPERATION_TOKENS = {
    "RECEIPT",
    "RECEIPT_ATTEMPT",
    "RECEIPT_OR_BLOCK",
    "RECEIPT_OR_REFUSAL",
    "BLOCK",
    "REFUSAL",
    "RECEIPT_BLOCK",
    "RECEIPT_REFUSAL",
    "VERIFY_RECEIPT_BASIS",
    "VERIFY_BLOCK_BASIS",
    "INTEGRITY_VERIFICATION",
    "HASH_VERIFICATION",
    "PRESERVE_RECEIPT_OR_REFUSAL_EVIDENCE",
    "RETURN_RECEIPT_OR_REFUSAL_EVIDENCE",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "additional_physical_carrier_experiment_created_currentness": False,
    "additional_physical_carrier_experiment_created_authority": False,
    "additional_physical_carrier_experiment_created_permission_beyond_scope": False,
    "additional_physical_carrier_experiment_created_hierarchy": False,
    "receiving_carrier_became_source": False,
    "receiving_carrier_became_current": False,
    "receiving_carrier_became_authority": False,
    "receiving_carrier_became_successor": False,
    "receiving_carrier_became_body": False,
    "distributed_standing_created": False,
    "carrier_registry_created": False,
    "repository_synchronization_authorized": False,
    "full_body_transfer_authorized": False,
    "second_body_created": False,
    "self_orientation_on_receiving_carrier_authorized": False,
    "conformance_on_receiving_carrier_authorized": False,
    "relation_on_receiving_carrier_authorized": False,
    "distributed_operation_authorized": False,
    "continuation_authorized": False,
    "success_authorizes_expansion": False,
    "majority_carrier_currentness": False,
    "successful_receipt_count_currentness": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "DECLARED_EXPERIMENT_REQUEST_UNREADABLE": "Declared experiment request path could not be read.",
    "DECLARED_EXPERIMENT_REQUEST_MALFORMED": "Declared experiment request is not a JSON object or mapping.",
    "EXPERIMENT_QUESTION_UNDECLARED": "Experiment question is undeclared.",
    "EXPERIMENT_PURPOSE_UNDECLARED": "Experiment purpose is undeclared.",
    "EXPERIMENT_INTENT_UNSUPPORTED": "Experiment intent is unsupported.",
    "EXPERIMENT_REQUEST_EXPLICITLY_BLOCKED": "Experiment request explicitly declares a blocked posture.",
    "SOURCE_CARRIER_MISSING": "Source carrier is missing.",
    "RECEIVING_CARRIER_MISSING": "Receiving carrier is missing.",
    "SOURCE_AND_RECEIVING_CARRIER_COLLAPSED": "Source carrier and receiving carrier collapsed into the same carrier.",
    "SELECTED_SURFACE_OR_PACKET_MISSING": "Selected carried surface or packet is missing.",
    "SELECTED_SURFACE_OR_PACKET_MALFORMED": "Selected carried surface or packet is malformed.",
    "SELECTED_SURFACE_OR_PACKET_IDENTITY_MISSING": "Selected carried surface or packet identity is missing.",
    "SELECTED_SURFACE_OR_PACKET_BASIS_MISSING": "Selected carried surface or packet basis is missing.",
    "CARRIER_ROLE_UNSUPPORTED": "Experiment carrier role is unsupported.",
    "EXPERIMENT_SCOPE_NOT_SINGLE_CARRIER": "Experiment scope is not one additional receiving carrier.",
    "EXPERIMENT_SCOPE_NOT_SINGLE_SURFACE_OR_PACKET": "Experiment scope is not one selected carried surface or packet.",
    "PERMITTED_OPERATIONS_NOT_RECEIPT_OR_BLOCK_ONLY": "Permitted operations are not bounded to receipt/refusal behavior.",
    "PROHIBITED_OPERATIONS_NOT_EXPLICIT": "Prohibited operations are not explicit.",
    "RETURN_POSTURE_MISSING": "Return and admission posture is missing or incomplete.",
    "ADMISSION_CREATED_BY_RETURN": "Return is treated as admission.",
    "REPOSITORY_SYNCHRONIZATION_REQUESTED": "Repository synchronization is requested or authorized.",
    "FULL_BODY_TRANSFER_REQUESTED": "Full body transfer is requested or authorized.",
    "SELF_ORIENTATION_ON_RECEIVING_CARRIER_REQUESTED": "Self-orientation on the receiving carrier is requested or authorized.",
    "CONFORMANCE_ON_RECEIVING_CARRIER_REQUESTED": "Conformance on the receiving carrier is requested or authorized.",
    "RELATION_CONFORMANCE_OR_CLOSURE_ON_RECEIVING_CARRIER_REQUESTED": "Relation, conformance, or closure on the receiving carrier is requested or authorized.",
    "CARRIER_REGISTRY_REQUESTED": "Carrier registry is requested or authorized.",
    "CURRENTNESS_REQUESTED": "Currentness is requested or created.",
    "DISTRIBUTED_STANDING_REQUESTED": "Distributed standing is requested or created.",
    "DISTRIBUTED_OPERATION_REQUESTED": "Distributed operation is requested or authorized.",
    "CONTINUATION_REQUESTED": "Continuation is requested or authorized.",
    "MAJORITY_OR_SUCCESS_COUNT_DECISIONING_REQUESTED": "Majority or success-count decisioning is requested.",
    "SOURCE_REPLACEMENT_REQUESTED": "Source replacement is requested or created.",
    "AUTHORITY_OR_PERMISSION_BEYOND_DECLARED_EXPERIMENT": "Authority or permission beyond the declared experiment is requested or created.",
    "CARRIER_HIERARCHY_CREATED": "Carrier hierarchy is created.",
    "EXPERIMENT_HIDES_REFUSAL_OR_DIVERGENCE": "Experiment hides refusal or divergence.",
    "MUTATION_REPLAY_OR_MERGE_REQUESTED": "Mutation, replay, or merge is requested.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required experiment non-claim is missing or flipped.",
}

EXPERIMENT_NON_MEANING = {
    "does_not_mean_distributed_standing": True,
    "does_not_mean_currentness": True,
    "does_not_mean_source_replacement": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission_beyond_declared_experiment": True,
    "does_not_mean_standing_permission_for_more_carriers": True,
    "does_not_mean_carrier_hierarchy": True,
    "does_not_mean_carrier_priority": True,
    "does_not_mean_carrier_sovereignty": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_carrier_registry": True,
    "does_not_mean_persistence": True,
    "does_not_mean_signal_by_default": True,
    "does_not_mean_presence": True,
    "does_not_mean_threshold": True,
    "does_not_mean_truth": True,
    "does_not_mean_action": True,
    "does_not_mean_consequence": True,
    "does_not_mean_continuation": True,
    "does_not_mean_automatic_admission": True,
    "does_not_mean_automatic_relation": True,
    "does_not_mean_automatic_currentness": True,
    "does_not_mean_automatic_conformance": True,
    "does_not_mean_automatic_closure": True,
    "does_not_mean_distributed_operation": True,
    "does_not_mean_success_means_expansion": True,
}

WHAT_REMAINS_OPEN = {
    "physical_execution_of_additional_carrier_receipt_refusal": True,
    "admission_of_any_returned_evidence": True,
    "divergence_review_involving_additional_carrier_evidence": True,
    "currentness_participation_review_involving_additional_carrier_evidence": True,
    "multi_carrier_relation_involving_additional_carrier_evidence": True,
    "conformance_over_any_later_relation": True,
    "closure_over_any_later_conformance": True,
    "distributed_standing": True,
    "persistence_registry_law": True,
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


def resolve_additional_physical_carrier_experiment_boundary(
    declared_experiment_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve whether one additional physical carrier experiment may be declared."""

    if declared_experiment_request is None:
        return _resolve_experiment({}, None, [])
    if not isinstance(declared_experiment_request, Mapping):
        return _resolve_experiment({}, None, ["DECLARED_EXPERIMENT_REQUEST_MALFORMED"])
    return _resolve_experiment(copy.deepcopy(dict(declared_experiment_request)), None, [])


def resolve_additional_physical_carrier_experiment_boundary_from_path(
    declared_experiment_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve a bounded experiment declaration request from one JSON object path."""

    path = Path(declared_experiment_request_path)
    try:
        request = _read_json_mapping(path)
    except AdditionalPhysicalCarrierExperimentBoundaryError as exc:
        return _resolve_experiment({}, path, [exc.block_code])
    return _resolve_experiment(request, path, [])


def write_additional_physical_carrier_experiment_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an additive experiment declaration result without overwriting."""

    if not isinstance(result, Mapping):
        raise AdditionalPhysicalCarrierExperimentBoundaryError(
            "DECLARED_EXPERIMENT_REQUEST_MALFORMED",
            "Additional physical carrier experiment result must be a mapping.",
        )

    if output_path is None:
        request_id = (
            _nested(result, "declared_experiment_question", "experiment_request_id")
            or "additional_physical_carrier_experiment"
        )
        output_path = ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_ROOT / (
            f"{_safe_filename_part(request_id)}__additional_physical_carrier_experiment_result.json"
        )

    target = _non_overwriting_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, ensure_ascii=False, default=str)
        + "\n",
        encoding="utf-8",
    )
    return target


def build_additional_physical_carrier_experiment_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary for an experiment declaration result."""

    checks = _mapping_list(result.get("experiment_checks"))
    question = _as_mapping(result.get("declared_experiment_question"))
    source = _as_mapping(result.get("source_carrier"))
    receiving = _as_mapping(result.get("receiving_carrier"))
    selected = _as_mapping(result.get("selected_carried_surface_or_packet"))
    statement = _as_mapping(result.get("experiment_declaration_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "experiment_request_id": question.get("experiment_request_id"),
        "experiment_question": question.get("experiment_question"),
        "experiment_purpose": question.get("experiment_purpose"),
        "experiment_intent": question.get("experiment_intent"),
        "source_carrier_id": source.get("source_carrier_id"),
        "receiving_carrier_id": receiving.get("receiving_carrier_id"),
        "selected_surface_or_packet_id": selected.get("selected_surface_or_packet_id"),
        "selected_surface_or_packet_basis": selected.get("selected_surface_or_packet_basis"),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "experiment_declared": bool(statement.get("additional_physical_carrier_experiment_declared")),
        "single_carrier_scope": bool(statement.get("experiment_scope_single_carrier")),
        "single_surface_or_packet_scope": bool(statement.get("experiment_scope_single_surface_or_packet")),
        "permitted_operation_receipt_or_block_only": bool(statement.get("permitted_operation_receipt_or_block_only")),
        "return_required_for_body_visibility": bool(statement.get("return_required_for_body_visibility")),
        "admission_not_created_by_return": bool(statement.get("admission_not_created_by_return")),
        "no_repository_synchronization": not bool(statement.get("repository_synchronization_authorized")),
        "no_full_body_transfer": not bool(statement.get("full_body_transfer_authorized")),
        "no_self_orientation_conformance_relation_on_receiving_carrier": not bool(
            statement.get("self_orientation_on_receiving_carrier_authorized")
            or statement.get("conformance_on_receiving_carrier_authorized")
            or statement.get("relation_on_receiving_carrier_authorized")
        ),
        "no_distributed_standing": not bool(statement.get("distributed_standing_created")),
        "no_currentness": not bool(statement.get("currentness_created")),
        "no_carrier_hierarchy": not bool(statement.get("carrier_hierarchy_created")),
        "no_distributed_operation": not bool(statement.get("distributed_operation_authorized")),
        "no_continuation": not bool(statement.get("continuation_authorized")),
        "no_success_based_expansion": not bool(statement.get("success_authorizes_expansion")),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_declared_additional_physical_carrier_experiment_request(
    experiment_request_id: str,
    experiment_question: str,
    experiment_purpose: str,
    source_carrier_id: str,
    receiving_carrier_id: str,
    selected_surface_or_packet: Mapping[str, Any],
    experiment_intent: str = DECLARE_INTENT,
) -> dict[str, Any]:
    """Build one bounded declaration request without inferring execution or force."""

    selected = copy.deepcopy(dict(selected_surface_or_packet))
    return {
        "experiment_request_id": experiment_request_id,
        "experiment_question": experiment_question,
        "experiment_purpose": experiment_purpose,
        "experiment_intent": experiment_intent,
        "source_carrier": {
            "carrier_id": source_carrier_id,
            "carrier_role": "EXPERIMENT_SOURCE_CARRIER",
            "role_is_operation_local": True,
            "does_not_create_universal_source_authority": True,
        },
        "receiving_carrier": {
            "carrier_id": receiving_carrier_id,
            "carrier_role": "EXPERIMENT_RECEIVING_CARRIER",
            "role_is_operation_local": True,
            "does_not_create_source_currentness_authority_body_or_standing": True,
        },
        "selected_carried_surface_or_packet": selected,
        "experiment_scope": {
            "single_receiving_carrier": True,
            "receiving_carrier_count": 1,
            "single_surface_or_packet": True,
            "selected_surface_or_packet_count": 1,
        },
        "permitted_operations": [
            "RECEIPT_OR_BLOCK",
            "INTEGRITY_VERIFICATION",
            "RETURN_RECEIPT_OR_REFUSAL_EVIDENCE",
        ],
        "prohibited_operations": {
            "repository_synchronization": True,
            "full_body_transfer": True,
            "self_orientation_on_receiving_carrier": True,
            "conformance_on_receiving_carrier": True,
            "relation_conformance_or_closure_on_receiving_carrier": True,
            "carrier_registry": True,
            "currentness": True,
            "distributed_standing": True,
            "distributed_operation": True,
            "continuation": True,
            "success_based_expansion": True,
        },
        "return_and_admission_posture": {
            "return_required_for_body_visibility": True,
            "admission_not_created_by_return": True,
            "admission_must_be_separate": True,
            "later_divergence_review_must_be_separate": True,
            "later_currentness_review_must_be_separate": True,
            "later_relation_review_must_be_separate": True,
        },
        "declared_execution_constraints": {
            "physical_execution_authorized_by_this_result": False,
            "packet_file_created_by_this_result": False,
            "repository_synchronization_authorized": False,
            "full_body_transfer_authorized": False,
            "distributed_operation_authorized": False,
            "continuation_authorized": False,
        },
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }


def _resolve_experiment(
    request: Mapping[str, Any],
    request_path: Path | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    normalized_request = _as_mapping(request)
    question = _declared_experiment_question(normalized_request, request_path)
    scope = _experiment_scope(normalized_request)
    source = _source_carrier(normalized_request)
    receiving = _receiving_carrier(normalized_request)
    selected = _selected_surface_or_packet(normalized_request)
    permitted = _permitted_operations(normalized_request)
    prohibited = _prohibited_operations(normalized_request)
    return_posture = _return_and_admission_posture(normalized_request)
    checks = _build_checks(
        normalized_request,
        question,
        scope,
        source,
        receiving,
        selected,
        permitted,
        prohibited,
        return_posture,
        precheck_failures,
    )
    failed_checks = [check for check in checks if check.get("passed") is False]
    intent = question.get("experiment_intent")
    explicit_block_code = _declared_block_code(normalized_request)

    if failed_checks:
        outcome = ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_BLOCKED
        block_code = str(failed_checks[0].get("block_code") or "NON_CLAIM_MISSING_OR_FLIPPED")
    elif intent == BLOCK_INTENT:
        outcome = ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_BLOCKED
        block_code = explicit_block_code or "EXPERIMENT_REQUEST_EXPLICITLY_BLOCKED"
    elif intent == DO_NOT_DECLARE_INTENT:
        outcome = ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_NOT_DECLARED
        block_code = None
    else:
        outcome = ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_DECLARED
        block_code = None

    block_reason = _block_reason(block_code)
    result: dict[str, Any] = {
        "additional_physical_carrier_experiment_metadata": {
            "additional_physical_carrier_experiment_result_id": _result_id(question, outcome),
            "additional_physical_carrier_experiment_result_type": RESULT_TYPE,
            "additional_physical_carrier_experiment_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_experiment_question": question,
        "experiment_scope": scope,
        "source_carrier": source,
        "receiving_carrier": receiving,
        "selected_carried_surface_or_packet": selected,
        "permitted_operations": permitted,
        "prohibited_operations": prohibited,
        "return_and_admission_posture": return_posture,
        "experiment_checks": checks,
        "experiment_declaration_statement": _experiment_declaration_statement(
            outcome,
            question,
            scope,
            source,
            receiving,
            selected,
            permitted,
            return_posture,
            checks,
            block_code,
            block_reason,
        ),
        "experiment_non_meaning": copy.deepcopy(EXPERIMENT_NON_MEANING),
        "what_remains_open": copy.deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
        "outcome": outcome,
        "block": {
            "code": block_code,
            "reason": block_reason,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["additional_physical_carrier_experiment_summary"] = (
        build_additional_physical_carrier_experiment_summary(result)
    )
    return result


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    artifact_path = Path(path)
    try:
        loaded = json.loads(artifact_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise AdditionalPhysicalCarrierExperimentBoundaryError(
            "DECLARED_EXPERIMENT_REQUEST_UNREADABLE",
            BLOCK_REASONS["DECLARED_EXPERIMENT_REQUEST_UNREADABLE"],
        ) from exc
    except json.JSONDecodeError as exc:
        raise AdditionalPhysicalCarrierExperimentBoundaryError(
            "DECLARED_EXPERIMENT_REQUEST_MALFORMED",
            BLOCK_REASONS["DECLARED_EXPERIMENT_REQUEST_MALFORMED"],
        ) from exc
    if not isinstance(loaded, Mapping):
        raise AdditionalPhysicalCarrierExperimentBoundaryError(
            "DECLARED_EXPERIMENT_REQUEST_MALFORMED",
            BLOCK_REASONS["DECLARED_EXPERIMENT_REQUEST_MALFORMED"],
        )
    return copy.deepcopy(dict(loaded))


def _declared_experiment_question(
    request: Mapping[str, Any],
    request_path: Path | None,
) -> dict[str, Any]:
    intent = _normalize_token(request.get("experiment_intent"))
    return {
        "experiment_request_id": request.get("experiment_request_id"),
        "experiment_request_path": _display_path(request_path)
        if request_path
        else request.get("_experiment_request_path"),
        "experiment_question": request.get("experiment_question"),
        "experiment_purpose": request.get("experiment_purpose"),
        "experiment_intent": intent,
        "operator_note": request.get("operator_note"),
        "declaration_is_for_one_additional_physical_receiving_carrier": True,
        "declaration_is_for_one_selected_surface_or_packet": True,
        "declaration_executes_physical_experiment": False,
        "declaration_creates_packet_file": False,
        "declaration_authorizes_repository_synchronization": False,
        "declaration_authorizes_full_body_transfer": False,
        "declaration_authorizes_self_orientation_on_receiving_carrier": False,
        "declaration_authorizes_conformance_on_receiving_carrier": False,
        "declaration_authorizes_distributed_operation": False,
        "declaration_authorizes_continuation": False,
        "declaration_authorizes_expansion_by_success": False,
        "selected_prior_closure_basis": copy.deepcopy(
            request.get("selected_prior_closure_basis")
        ),
        "selected_v3_closure_basis": copy.deepcopy(request.get("selected_v3_closure_basis")),
        "selected_relation_band_basis": copy.deepcopy(
            request.get("selected_relation_band_basis")
        ),
        "declared_non_claims": copy.deepcopy(
            request.get("declared_non_claims") or request.get("non_claims")
        ),
    }


def _experiment_scope(request: Mapping[str, Any]) -> dict[str, Any]:
    scope = _as_mapping(request.get("experiment_scope"))
    receiving_count = _int_or_none(
        scope.get("receiving_carrier_count")
        or scope.get("additional_receiving_carrier_count")
        or scope.get("carrier_count")
    )
    selected_count = _int_or_none(
        scope.get("selected_surface_or_packet_count")
        or scope.get("surface_or_packet_count")
        or scope.get("selected_packet_count")
    )
    single_carrier = (
        scope.get("single_receiving_carrier") is True
        or scope.get("single_carrier") is True
        or scope.get("experiment_scope_single_carrier") is True
        or receiving_count == 1
    )
    single_surface = (
        scope.get("single_surface_or_packet") is True
        or scope.get("single_carried_surface_or_packet") is True
        or scope.get("experiment_scope_single_surface_or_packet") is True
        or selected_count == 1
    )
    return {
        "single_carrier_scope": bool(single_carrier),
        "single_surface_or_packet_scope": bool(single_surface),
        "receiving_carrier_count": receiving_count,
        "selected_surface_or_packet_count": selected_count,
        "raw_experiment_scope": copy.deepcopy(scope),
        "scope_does_not_create_distributed_standing": True,
        "scope_does_not_authorize_continuation": True,
        "scope_does_not_authorize_expansion_by_success": True,
    }


def _source_carrier(request: Mapping[str, Any]) -> dict[str, Any]:
    carrier = _normalize_carrier(request.get("source_carrier"))
    return {
        "source_carrier_id": carrier.get("carrier_id"),
        "source_carrier_role": carrier.get("carrier_role"),
        "source_carrier_role_supported": carrier.get("carrier_role") in SOURCE_ROLES,
        "source_role_is_operation_local": carrier.get("role_is_operation_local") is not False,
        "source_carrier_does_not_create_universal_source_authority": True,
        "raw_source_carrier": copy.deepcopy(carrier.get("raw_carrier")),
    }


def _receiving_carrier(request: Mapping[str, Any]) -> dict[str, Any]:
    carrier = _normalize_carrier(request.get("receiving_carrier"))
    return {
        "receiving_carrier_id": carrier.get("carrier_id"),
        "receiving_carrier_role": carrier.get("carrier_role"),
        "receiving_carrier_role_supported": carrier.get("carrier_role") in RECEIVING_ROLES,
        "receiving_carrier_role_is_operation_local": carrier.get("role_is_operation_local") is not False,
        "receiving_carrier_bounded_to_receipt_refusal": True,
        "receiving_carrier_does_not_become_source_current_authority_body_or_standing": True,
        "raw_receiving_carrier": copy.deepcopy(carrier.get("raw_carrier")),
    }


def _selected_surface_or_packet(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("selected_carried_surface_or_packet")
    if raw is None:
        return {
            "selected_surface_or_packet_declared": False,
            "selected_surface_or_packet_parseable": False,
            "selected_surface_or_packet_id": None,
            "selected_surface_or_packet_basis": None,
            "selected_surface_or_packet_outcome_or_status": None,
            "integrity_basis": copy.deepcopy(request.get("integrity_basis")),
            "raw_selected_surface_or_packet": None,
        }
    if not isinstance(raw, Mapping):
        return {
            "selected_surface_or_packet_declared": True,
            "selected_surface_or_packet_parseable": False,
            "selected_surface_or_packet_id": None,
            "selected_surface_or_packet_basis": None,
            "selected_surface_or_packet_outcome_or_status": None,
            "integrity_basis": copy.deepcopy(request.get("integrity_basis")),
            "raw_selected_surface_or_packet": copy.deepcopy(raw),
        }
    selected = _as_mapping(raw)
    selected_id = (
        selected.get("selected_surface_or_packet_id")
        or selected.get("surface_or_packet_id")
        or selected.get("carried_surface_id")
        or selected.get("packet_id")
        or selected.get("surface_id")
        or selected.get("result_id")
        or selected.get("id")
    )
    basis = (
        selected.get("selected_surface_or_packet_basis")
        or selected.get("basis")
        or selected.get("selected_basis")
        or selected.get("carried_surface_basis")
        or selected.get("packet_basis")
        or selected.get("source_basis")
    )
    outcome = (
        selected.get("outcome")
        or selected.get("status")
        or selected.get("surface_outcome")
        or selected.get("packet_status")
    )
    integrity_basis = selected.get("integrity_basis") or request.get("integrity_basis")
    return {
        "selected_surface_or_packet_declared": True,
        "selected_surface_or_packet_parseable": True,
        "selected_surface_or_packet_id": selected_id,
        "selected_surface_or_packet_basis": copy.deepcopy(basis),
        "selected_surface_or_packet_basis_preserved": bool(basis)
        or selected.get("basis_preserved") is True,
        "selected_surface_or_packet_outcome_or_status": outcome,
        "integrity_basis": copy.deepcopy(integrity_basis),
        "integrity_basis_preserved_where_supplied": integrity_basis is None
        or bool(integrity_basis),
        "raw_selected_surface_or_packet": copy.deepcopy(selected),
    }


def _permitted_operations(request: Mapping[str, Any]) -> dict[str, Any]:
    operations = _operation_tokens(request.get("permitted_operations"))
    unsupported = sorted(token for token in operations if token not in PERMITTED_OPERATION_TOKENS)
    return {
        "operation_tokens": sorted(operations),
        "permitted_operations_declared": bool(operations),
        "receipt_or_block_only": bool(operations) and not unsupported,
        "unsupported_operation_tokens": unsupported,
        "raw_permitted_operations": copy.deepcopy(request.get("permitted_operations")),
    }


def _prohibited_operations(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("prohibited_operations")
    explicit = False
    if isinstance(raw, Mapping):
        explicit = bool(raw)
    elif isinstance(raw, list):
        explicit = bool(raw)
    elif isinstance(raw, str):
        explicit = bool(raw.strip())
    return {
        "prohibited_operations_explicit": explicit,
        "raw_prohibited_operations": copy.deepcopy(raw),
    }


def _return_and_admission_posture(request: Mapping[str, Any]) -> dict[str, Any]:
    posture = _as_mapping(request.get("return_and_admission_posture"))
    return_required = _truth_from_sources(
        posture,
        keys=(
            "return_required_for_body_visibility",
            "return_required",
            "returned_evidence_required_for_body_visibility",
        ),
    )
    admission_not_created = _truth_from_sources(
        posture,
        keys=(
            "admission_not_created_by_return",
            "return_does_not_create_admission",
            "admission_must_be_separate",
        ),
    )
    admission_created = _flag_true(
        posture,
        (
            "admission_created_by_return",
            "return_creates_admission",
            "returned_evidence_admitted_by_return",
        ),
    )
    return {
        "return_posture_declared": bool(posture),
        "return_required_for_body_visibility": return_required,
        "admission_not_created_by_return": admission_not_created,
        "admission_created_by_return": admission_created,
        "admission_must_be_separate": posture.get("admission_must_be_separate") is True
        or admission_not_created,
        "later_divergence_review_must_be_separate": posture.get("later_divergence_review_must_be_separate")
        is not False,
        "later_currentness_review_must_be_separate": posture.get("later_currentness_review_must_be_separate")
        is not False,
        "later_relation_review_must_be_separate": posture.get("later_relation_review_must_be_separate")
        is not False,
        "raw_return_and_admission_posture": copy.deepcopy(posture),
    }


def _build_checks(
    request: Mapping[str, Any],
    question: Mapping[str, Any],
    scope: Mapping[str, Any],
    source: Mapping[str, Any],
    receiving: Mapping[str, Any],
    selected: Mapping[str, Any],
    permitted: Mapping[str, Any],
    prohibited: Mapping[str, Any],
    return_posture: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    collapse_source = _without_safe_sections(request)
    sources = [
        collapse_source,
        question,
        scope,
        source,
        receiving,
        selected,
        permitted,
        return_posture,
        _as_mapping(request.get("declared_non_claims") or request.get("non_claims")),
    ]
    precheck_code = precheck_failures[0] if precheck_failures else None
    source_id = source.get("source_carrier_id")
    receiving_id = receiving.get("receiving_carrier_id")
    checks = [
        _check(
            "declared_experiment_request_parseable_mapping",
            not precheck_failures,
            "declared experiment request is a parseable mapping",
            list(precheck_failures),
            precheck_code or "DECLARED_EXPERIMENT_REQUEST_MALFORMED",
        ),
        _check(
            "experiment_question_declared",
            _nonempty(question.get("experiment_question")),
            "experiment question is declared",
            question.get("experiment_question"),
            "EXPERIMENT_QUESTION_UNDECLARED",
        ),
        _check(
            "experiment_purpose_declared",
            _nonempty(question.get("experiment_purpose")),
            "experiment purpose is declared",
            question.get("experiment_purpose"),
            "EXPERIMENT_PURPOSE_UNDECLARED",
        ),
        _check(
            "experiment_intent_supported",
            question.get("experiment_intent") in SUPPORTED_EXPERIMENT_INTENTS,
            "experiment intent is supported",
            question.get("experiment_intent"),
            "EXPERIMENT_INTENT_UNSUPPORTED",
        ),
        _check(
            "source_carrier_declared",
            _nonempty(source_id),
            "source carrier is declared",
            source_id,
            "SOURCE_CARRIER_MISSING",
        ),
        _check(
            "receiving_carrier_declared",
            _nonempty(receiving_id),
            "receiving carrier is declared",
            receiving_id,
            "RECEIVING_CARRIER_MISSING",
        ),
        _check(
            "receiving_carrier_is_additional_and_bounded",
            _nonempty(receiving_id)
            and _nonempty(source_id)
            and _normalize_token(receiving_id) != _normalize_token(source_id),
            "receiving carrier is additional to source carrier",
            {"source_carrier_id": source_id, "receiving_carrier_id": receiving_id},
            "SOURCE_AND_RECEIVING_CARRIER_COLLAPSED",
        ),
        _check(
            "carrier_roles_supported",
            bool(source.get("source_carrier_role_supported"))
            and bool(receiving.get("receiving_carrier_role_supported")),
            "source and receiving carrier roles are operation-local and supported",
            {
                "source_carrier_role": source.get("source_carrier_role"),
                "receiving_carrier_role": receiving.get("receiving_carrier_role"),
            },
            "CARRIER_ROLE_UNSUPPORTED",
        ),
        _check(
            "selected_surface_or_packet_declared",
            bool(selected.get("selected_surface_or_packet_declared")),
            "one selected carried surface or packet is declared",
            selected.get("raw_selected_surface_or_packet"),
            "SELECTED_SURFACE_OR_PACKET_MISSING",
        ),
        _check(
            "selected_surface_or_packet_parseable",
            bool(selected.get("selected_surface_or_packet_parseable")),
            "selected carried surface or packet is parseable",
            _shape(selected.get("raw_selected_surface_or_packet")),
            "SELECTED_SURFACE_OR_PACKET_MALFORMED",
        ),
        _check(
            "selected_surface_or_packet_identity_exists",
            _nonempty(selected.get("selected_surface_or_packet_id")),
            "selected carried surface or packet identity exists",
            selected.get("selected_surface_or_packet_id"),
            "SELECTED_SURFACE_OR_PACKET_IDENTITY_MISSING",
        ),
        _check(
            "selected_surface_or_packet_basis_preserved",
            bool(selected.get("selected_surface_or_packet_basis_preserved")),
            "selected carried surface or packet basis is preserved",
            selected.get("selected_surface_or_packet_basis"),
            "SELECTED_SURFACE_OR_PACKET_BASIS_MISSING",
        ),
        _check(
            "scope_single_carrier",
            bool(scope.get("single_carrier_scope")),
            "experiment scope is one additional receiving carrier",
            scope.get("raw_experiment_scope"),
            "EXPERIMENT_SCOPE_NOT_SINGLE_CARRIER",
        ),
        _check(
            "scope_single_surface_or_packet",
            bool(scope.get("single_surface_or_packet_scope")),
            "experiment scope is one selected surface or packet",
            scope.get("raw_experiment_scope"),
            "EXPERIMENT_SCOPE_NOT_SINGLE_SURFACE_OR_PACKET",
        ),
        _check(
            "permitted_operations_receipt_refusal_only",
            bool(permitted.get("receipt_or_block_only")),
            "permitted operations are bounded to receipt/refusal behavior",
            permitted,
            "PERMITTED_OPERATIONS_NOT_RECEIPT_OR_BLOCK_ONLY",
        ),
        _check(
            "prohibited_operations_explicit",
            bool(prohibited.get("prohibited_operations_explicit")),
            "prohibited operations are explicit",
            prohibited.get("raw_prohibited_operations"),
            "PROHIBITED_OPERATIONS_NOT_EXPLICIT",
        ),
        _check(
            "return_required_for_body_visibility",
            bool(return_posture.get("return_required_for_body_visibility")),
            "return is required for body visibility",
            return_posture,
            "RETURN_POSTURE_MISSING",
        ),
        _check(
            "admission_not_created_by_return",
            bool(return_posture.get("admission_not_created_by_return"))
            and not bool(return_posture.get("admission_created_by_return")),
            "return does not create admission",
            return_posture,
            "ADMISSION_CREATED_BY_RETURN"
            if return_posture.get("admission_created_by_return")
            else "RETURN_POSTURE_MISSING",
        ),
        _collapse_check(
            "no_self_orientation_on_receiving_carrier",
            sources,
            (
                "self_orientation_on_receiving_carrier_authorized",
                "self_orientation_on_receiving_carrier_requested",
                "run_self_orientation_on_receiving_carrier",
            ),
            "self-orientation on receiving carrier is not authorized",
            "SELF_ORIENTATION_ON_RECEIVING_CARRIER_REQUESTED",
        ),
        _collapse_check(
            "no_conformance_on_receiving_carrier",
            sources,
            (
                "conformance_on_receiving_carrier_authorized",
                "conformance_on_receiving_carrier_requested",
                "current_body_conformance_on_receiving_carrier_authorized",
                "run_conformance_on_receiving_carrier",
            ),
            "conformance on receiving carrier is not authorized",
            "CONFORMANCE_ON_RECEIVING_CARRIER_REQUESTED",
        ),
        _collapse_check(
            "no_relation_conformance_or_closure_on_receiving_carrier",
            sources,
            (
                "relation_on_receiving_carrier_authorized",
                "relation_on_receiving_carrier_requested",
                "relation_conformance_on_receiving_carrier_authorized",
                "relation_closure_on_receiving_carrier_authorized",
                "closure_on_receiving_carrier_authorized",
            ),
            "relation, conformance, or closure on receiving carrier is not authorized",
            "RELATION_CONFORMANCE_OR_CLOSURE_ON_RECEIVING_CARRIER_REQUESTED",
        ),
        _collapse_check(
            "no_repository_synchronization",
            sources,
            (
                "repository_synchronization_authorized",
                "repository_synchronization_requested",
                "repository_synchronization_created",
                "sync_authorized",
                "sync_requested",
            ),
            "repository synchronization is not authorized",
            "REPOSITORY_SYNCHRONIZATION_REQUESTED",
        ),
        _collapse_check(
            "no_full_body_transfer",
            sources,
            (
                "full_body_transfer_authorized",
                "full_body_transfer_requested",
                "body_transfer_authorized",
                "body_transfer_requested",
            ),
            "full body transfer is not authorized",
            "FULL_BODY_TRANSFER_REQUESTED",
        ),
        _collapse_check(
            "no_carrier_registry",
            sources,
            ("carrier_registry_created", "carrier_registry_requested", "carrier_registry_authorized"),
            "carrier registry is not authorized",
            "CARRIER_REGISTRY_REQUESTED",
        ),
        _collapse_check(
            "no_currentness",
            sources,
            (
                "currentness_created",
                "currentness_requested",
                "currentness_authorized",
                "additional_physical_carrier_experiment_created_currentness",
                "receiving_carrier_became_current",
            ),
            "currentness is not created or requested",
            "CURRENTNESS_REQUESTED",
        ),
        _collapse_check(
            "no_distributed_standing",
            sources,
            (
                "distributed_standing_created",
                "distributed_standing_requested",
                "distributed_standing_authorized",
            ),
            "distributed standing is not created or requested",
            "DISTRIBUTED_STANDING_REQUESTED",
        ),
        _collapse_check(
            "no_distributed_operation",
            sources,
            ("distributed_operation_authorized", "distributed_operation_requested"),
            "distributed operation is not authorized",
            "DISTRIBUTED_OPERATION_REQUESTED",
        ),
        _collapse_check(
            "no_continuation",
            sources,
            ("continuation_authorized", "continuation_requested", "follow_on_work_authorized"),
            "continuation is not authorized",
            "CONTINUATION_REQUESTED",
        ),
        _collapse_check(
            "no_carrier_hierarchy",
            sources,
            (
                "carrier_hierarchy_created",
                "additional_physical_carrier_experiment_created_hierarchy",
                "carrier_priority_created",
                "winning_carrier_selected",
                "losing_carrier_invalidated",
            ),
            "carrier hierarchy is not created",
            "CARRIER_HIERARCHY_CREATED",
        ),
        _collapse_check(
            "no_source_replacement",
            sources,
            ("source_replaced", "source_replacement_requested", "receiving_carrier_became_source"),
            "source is not replaced",
            "SOURCE_REPLACEMENT_REQUESTED",
        ),
        _collapse_check(
            "no_authority_or_permission_beyond_declared_experiment",
            sources,
            (
                "authority_created",
                "authority_requested",
                "permission_created",
                "permission_requested",
                "additional_physical_carrier_experiment_created_authority",
                "additional_physical_carrier_experiment_created_permission_beyond_scope",
                "receiving_carrier_became_authority",
            ),
            "authority or permission beyond the declared experiment is not created",
            "AUTHORITY_OR_PERMISSION_BEYOND_DECLARED_EXPERIMENT",
        ),
        _collapse_check(
            "no_success_based_expansion",
            sources,
            (
                "success_authorizes_expansion",
                "success_based_expansion_authorized",
                "success_means_expansion",
                "permission_for_more_carriers",
            ),
            "success does not authorize expansion",
            "AUTHORITY_OR_PERMISSION_BEYOND_DECLARED_EXPERIMENT",
        ),
        _collapse_check(
            "no_majority_success_count_or_latest_file_currentness",
            sources,
            (
                "majority_carrier_currentness",
                "successful_receipt_count_currentness",
                "success_count_currentness",
                "latest_file_currentness",
                "recency_fraud",
            ),
            "majority, success-count, and latest-file currentness are false",
            "MAJORITY_OR_SUCCESS_COUNT_DECISIONING_REQUESTED",
        ),
        _collapse_check(
            "no_hidden_refusal_or_divergence",
            sources,
            (
                "refusal_hidden",
                "divergence_hidden",
                "mismatch_hidden",
                "hide_refusal",
                "hide_divergence",
            ),
            "visible refusal and divergence are not hidden",
            "EXPERIMENT_HIDES_REFUSAL_OR_DIVERGENCE",
        ),
        _collapse_check(
            "no_mutation_replay_or_merge",
            sources,
            (
                "mutation_performed",
                "mutation_requested",
                "replay_performed",
                "replay_requested",
                "merge_performed",
                "merge_requested",
            ),
            "mutation, replay, and merge are not requested",
            "MUTATION_REPLAY_OR_MERGE_REQUESTED",
        ),
    ]
    non_claim_failures = _non_claim_failures(
        _as_mapping(request.get("declared_non_claims") or request.get("non_claims")),
        sources,
    )
    checks.append(
        _check(
            "non_claims_remain_false",
            not non_claim_failures,
            "required non-claims are explicit and false",
            non_claim_failures,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _experiment_declaration_statement(
    outcome: str,
    question: Mapping[str, Any],
    scope: Mapping[str, Any],
    source: Mapping[str, Any],
    receiving: Mapping[str, Any],
    selected: Mapping[str, Any],
    permitted: Mapping[str, Any],
    return_posture: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    declared = outcome == ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_DECLARED
    failed_checks = [copy.deepcopy(dict(check)) for check in checks if check.get("passed") is False]
    base = {
        "additional_physical_carrier_experiment_declared": declared,
        "additional_physical_carrier_experiment_not_declared": outcome == ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_NOT_DECLARED,
        "additional_physical_carrier_experiment_blocked": outcome == ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_BLOCKED,
        "experiment_scope_single_carrier": bool(scope.get("single_carrier_scope")),
        "experiment_scope_single_surface_or_packet": bool(scope.get("single_surface_or_packet_scope")),
        "source_carrier_declared": _nonempty(source.get("source_carrier_id")),
        "receiving_carrier_declared": _nonempty(receiving.get("receiving_carrier_id")),
        "selected_surface_or_packet_declared": bool(selected.get("selected_surface_or_packet_declared")),
        "permitted_operation_receipt_or_block_only": bool(permitted.get("receipt_or_block_only")),
        "return_required_for_body_visibility": bool(return_posture.get("return_required_for_body_visibility")),
        "admission_not_created_by_return": bool(return_posture.get("admission_not_created_by_return")),
        "distributed_standing_created": False,
        "currentness_created": False,
        "carrier_hierarchy_created": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "self_orientation_on_receiving_carrier_authorized": False,
        "conformance_on_receiving_carrier_authorized": False,
        "relation_on_receiving_carrier_authorized": False,
        "distributed_operation_authorized": False,
        "continuation_authorized": False,
        "success_authorizes_expansion": False,
        "experiment_executes_physical_receipt": False,
        "experiment_creates_packet_file": False,
        "experiment_creates_returned_evidence": False,
        "experiment_admits_returned_evidence": False,
        "selected_request_basis": {
            "experiment_request_id": question.get("experiment_request_id"),
            "experiment_question": question.get("experiment_question"),
            "experiment_purpose": question.get("experiment_purpose"),
            "experiment_intent": question.get("experiment_intent"),
            "source_carrier": copy.deepcopy(dict(source)),
            "receiving_carrier": copy.deepcopy(dict(receiving)),
            "selected_carried_surface_or_packet": copy.deepcopy(dict(selected)),
        },
        "failed_checks": failed_checks,
    }
    if declared:
        base.update(
            {
                "additional_physical_carrier_experiment_declared": True,
                "experiment_scope_single_carrier": True,
                "experiment_scope_single_surface_or_packet": True,
                "source_carrier_declared": True,
                "receiving_carrier_declared": True,
                "permitted_operation_receipt_or_block_only": True,
                "return_required_for_body_visibility": True,
                "admission_not_created_by_return": True,
            }
        )
    elif outcome == ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_NOT_DECLARED:
        base.update(
            {
                "not_declared_reason": "Readable request explicitly does not declare an additional physical carrier experiment.",
                "no_collapse_flags_true": True,
            }
        )
    else:
        base.update(
            {
                "block_code": block_code,
                "block_reason": block_reason,
                "non_claims_where_available": _declared_non_claims_from_basis(question),
            }
        )
    return base


def _declared_non_claims_from_basis(question: Mapping[str, Any]) -> dict[str, Any]:
    declared = _as_mapping(question.get("declared_non_claims"))
    if declared:
        return declared
    selected = _as_mapping(question.get("selected_prior_closure_basis"))
    if selected:
        return _as_mapping(selected.get("declared_non_claims") or selected.get("non_claims"))
    return {}


def _check(
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    block_code: str | None,
) -> dict[str, Any]:
    return {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": copy.deepcopy(expected),
        "actual_posture": copy.deepcopy(actual),
        "block_code": None if passed else block_code,
    }


def _collapse_check(
    name: str,
    sources: Sequence[Any],
    aliases: Sequence[str],
    expected: str,
    block_code: str,
) -> dict[str, Any]:
    return _check(
        name,
        not _flag_true(sources, aliases),
        expected,
        _flag_snapshot(sources, aliases),
        block_code,
    )


def _non_claim_failures(
    declared_non_claims: Mapping[str, Any],
    sources: Sequence[Any],
) -> dict[str, Any]:
    failures: dict[str, Any] = {}
    if not declared_non_claims:
        failures["declared_non_claims"] = "missing"
    else:
        for key in sorted(REQUIRED_NON_CLAIMS):
            if key not in declared_non_claims:
                failures[key] = "missing"
            elif declared_non_claims.get(key) is not False:
                failures[key] = declared_non_claims.get(key)
    for key in sorted(REQUIRED_NON_CLAIMS):
        if _flag_true(sources, (key,)):
            failures[key] = True
    return failures


def _normalize_carrier(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        carrier = _as_mapping(value)
        carrier_id = (
            carrier.get("carrier_id")
            or carrier.get("source_carrier_id")
            or carrier.get("receiving_carrier_id")
            or carrier.get("id")
            or carrier.get("carrier_label")
            or carrier.get("label")
        )
        role = _normalize_token(carrier.get("carrier_role") or carrier.get("role"))
        return {
            "carrier_id": carrier_id,
            "carrier_role": role,
            "role_is_operation_local": carrier.get("role_is_operation_local"),
            "raw_carrier": copy.deepcopy(carrier),
        }
    if isinstance(value, str) and value.strip():
        return {
            "carrier_id": value.strip(),
            "carrier_role": None,
            "role_is_operation_local": None,
            "raw_carrier": value.strip(),
        }
    return {
        "carrier_id": None,
        "carrier_role": None,
        "role_is_operation_local": None,
        "raw_carrier": copy.deepcopy(value),
    }


def _operation_tokens(value: Any) -> set[str]:
    tokens: set[str] = set()
    if isinstance(value, Mapping):
        for key, item in value.items():
            if _truthy(item):
                tokens.add(str(key))
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, str):
                tokens.add(item)
            elif isinstance(item, Mapping):
                name = item.get("operation") or item.get("operation_name") or item.get("name")
                if name and item.get("permitted") is not False:
                    tokens.add(str(name))
    elif isinstance(value, str):
        tokens.add(value)
    return {_normalize_token(token) or "" for token in tokens if _normalize_token(token)}


def _declared_block_code(request: Mapping[str, Any]) -> str | None:
    candidate = _normalize_token(
        request.get("block_code")
        or _nested(request, "block", "block_code")
        or _nested(request, "block", "code")
        or _nested(request, "declared_block", "block_code")
    )
    return candidate if candidate in BLOCK_REASONS else None


def _block_reason(block_code: str | None) -> str | None:
    if block_code is None:
        return None
    return BLOCK_REASONS.get(block_code, f"Additional physical carrier experiment blocked: {block_code}.")


def _result_id(question: Mapping[str, Any], outcome: str) -> str:
    request_id = question.get("experiment_request_id") or "additional_physical_carrier_experiment"
    return f"{_safe_filename_part(request_id)}__{outcome.lower()}__additional_physical_carrier_experiment_result"


def _as_mapping(value: Any) -> dict[str, Any]:
    return copy.deepcopy(dict(value)) if isinstance(value, Mapping) else {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list) and all(isinstance(item, Mapping) for item in value):
        return [copy.deepcopy(dict(item)) for item in value]
    return []


def _nested(mapping: Mapping[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = mapping
    for key in keys:
        if not isinstance(value, Mapping):
            return default
        value = value.get(key)
    return default if value is None else value


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    resolved = Path(path)
    try:
        return str(resolved.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(resolved)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _truth_from_sources(source: Mapping[str, Any], *, keys: Sequence[str]) -> bool:
    return any(source.get(key) is True for key in keys)


def _int_or_none(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.strip().isdigit():
        return int(value.strip())
    return None


def _nonempty(value: Any) -> bool:
    return value is not None and str(value).strip() != ""


def _shape(value: Any) -> str:
    if isinstance(value, Mapping):
        return "mapping"
    if isinstance(value, list):
        return f"list[{len(value)}]"
    return type(value).__name__


def _flag_true(sources: Any, aliases: Sequence[str]) -> bool:
    alias_set = {alias.lower() for alias in aliases}
    return any(key.lower() in alias_set and _truthy(value) for key, value in _walk_key_values(sources))


def _flag_snapshot(sources: Any, aliases: Sequence[str]) -> dict[str, Any]:
    alias_set = {alias.lower() for alias in aliases}
    return {
        key: copy.deepcopy(value)
        for key, value in _walk_key_values(sources)
        if key.lower() in alias_set
    }


def _walk_key_values(value: Any) -> list[tuple[str, Any]]:
    found: list[tuple[str, Any]] = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            key_text = str(key)
            if key_text in {"experiment_non_meaning", "what_remains_open", "prohibited_operations"}:
                continue
            found.append((key_text, item))
            found.extend(_walk_key_values(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(_walk_key_values(item))
    return found


def _without_safe_sections(value: Mapping[str, Any]) -> dict[str, Any]:
    skipped = {
        "experiment_non_meaning",
        "what_remains_open",
        "prohibited_operations",
    }
    return {key: copy.deepcopy(item) for key, item in value.items() if key not in skipped}


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {
            "true",
            "yes",
            "1",
            "on",
            "created",
            "authorized",
            "requested",
            "selected",
            "forced",
        }
    return bool(value)


def _normalize_token(value: Any) -> str | None:
    if value is None:
        return None
    token = str(value).strip().upper().replace("-", "_").replace(" ", "_")
    while "__" in token:
        token = token.replace("__", "_")
    return token or None


def _safe_filename_part(value: Any) -> str:
    text = str(value or "additional_physical_carrier_experiment").strip().lower()
    safe = "".join(char if char.isalnum() or char in {"-", "_"} else "_" for char in text).strip("_")
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe[:180] or "additional_physical_carrier_experiment"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.parent / f"{path.stem}_{index:03d}{path.suffix}"
        if not candidate.exists():
            return candidate
    raise AdditionalPhysicalCarrierExperimentBoundaryError(
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "Could not create a non-overwriting additional physical carrier experiment result path.",
    )


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "source_replaced",
        "distributed_standing_created",
        "carrier_registry_created",
        "repository_synchronization_authorized",
        "full_body_transfer_authorized",
        "second_body_created",
        "self_orientation_on_receiving_carrier_authorized",
        "conformance_on_receiving_carrier_authorized",
        "relation_on_receiving_carrier_authorized",
        "distributed_operation_authorized",
        "continuation_authorized",
        "success_authorizes_expansion",
        "majority_carrier_currentness",
        "successful_receipt_count_currentness",
        "latest_file_currentness",
        "recency_fraud",
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    )
    return {key: non_claims.get(key) for key in keys}
