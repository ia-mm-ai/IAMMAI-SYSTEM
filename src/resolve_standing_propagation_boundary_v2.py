"""Standing propagation boundary resolver v2.

This is a lineage-preserving successor to
``resolve_standing_propagation_boundary``. V1 remains standing and its
artifacts remain untouched. V2 exists for one narrow reason: a v1 result body
could preserve visible refusal, visible divergence, and receipt/refusal/
return/admission posture inside nested standing propagation basis while the
statement and summary projected those fields as false.

V2 keeps the same boundary and outcome family, writes only to a v2 output root,
and improves projection so statement and summary fields correspond to detailed
nested basis, explicit posture fields, and related carrier evidence. It remains
posture recording only: no distributed standing, currentness, source
replacement, authority, permission, carrier hierarchy, synchronization, full
body transfer, continuation, distributed operation, receipt-standing,
admission-standing, registry-standing, or evidence erasure is created here.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class StandingPropagationBoundaryV2Error(Exception):
    """Hard failure for malformed or unreadable explicit v2 inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


REPO_ROOT = Path(__file__).resolve().parents[1]

STANDING_PROPAGATION_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_standing_propagation_boundary_v2"
)

RESOLVER_MODULE = "resolve_standing_propagation_boundary_v2"
SUCCESSOR_OF_MODULE = "resolve_standing_propagation_boundary"
RESULT_VERSION = "0.2.0"
RESULT_TYPE = "standing_propagation_boundary_v2_result"

RECORD_INTENT = "RECORD_STANDING_PROPAGATION_POSTURE"
DO_NOT_RECORD_INTENT = "DO_NOT_RECORD_STANDING_PROPAGATION_POSTURE"
BLOCK_INTENT = "BLOCK_STANDING_PROPAGATION_POSTURE"
SUPPORTED_PROPAGATION_INTENTS = {
    RECORD_INTENT,
    DO_NOT_RECORD_INTENT,
    BLOCK_INTENT,
}

STANDING_PROPAGATION_POSTURE_RECORDED = "STANDING_PROPAGATION_POSTURE_RECORDED"
STANDING_PROPAGATION_POSTURE_NOT_RECORDED = "STANDING_PROPAGATION_POSTURE_NOT_RECORDED"
STANDING_PROPAGATION_POSTURE_BLOCKED = "STANDING_PROPAGATION_POSTURE_BLOCKED"

SUPPORTED_PROPAGATION_POSTURES = {
    "SOURCE_STANDING_PRESERVED",
    "STANDING_CARRIED_AS_EVIDENCE",
    "CARRIED_STANDING_RECEIVED",
    "CARRIED_STANDING_REFUSED_OR_BLOCKED",
    "CARRIED_STANDING_RETURNED",
    "CARRIED_STANDING_ADMITTED_AS_EVIDENCE",
    "CARRIED_STANDING_DIVERGENCE_RECORDED",
    "CARRIED_STANDING_CURRENTNESS_PARTICIPATION_ELIGIBLE",
    "CARRIED_STANDING_CURRENTNESS_PARTICIPATION_EXCLUDED",
    "CARRIED_STANDING_RELATION_RECOGNIZED",
    "CARRIED_STANDING_RELATION_CONFORMANT",
    "CARRIED_STANDING_RELATION_CLOSED",
    "CARRIED_STANDING_LIFECYCLE_REFERENCED",
    "CARRIED_STANDING_REGISTRY_REFERENCED",
    "CARRIED_STANDING_STALE",
    "CARRIED_STANDING_CORRUPTED",
    "CARRIED_STANDING_EXCLUDED_FROM_RELIANCE",
    "STANDING_PROPAGATION_BLOCKED",
}

CARRIED_POSTURES = {
    "STANDING_CARRIED_AS_EVIDENCE",
    "CARRIED_STANDING_RECEIVED",
    "CARRIED_STANDING_REFUSED_OR_BLOCKED",
    "CARRIED_STANDING_RETURNED",
    "CARRIED_STANDING_ADMITTED_AS_EVIDENCE",
    "CARRIED_STANDING_DIVERGENCE_RECORDED",
    "CARRIED_STANDING_CURRENTNESS_PARTICIPATION_ELIGIBLE",
    "CARRIED_STANDING_CURRENTNESS_PARTICIPATION_EXCLUDED",
    "CARRIED_STANDING_RELATION_RECOGNIZED",
    "CARRIED_STANDING_RELATION_CONFORMANT",
    "CARRIED_STANDING_RELATION_CLOSED",
    "CARRIED_STANDING_LIFECYCLE_REFERENCED",
    "CARRIED_STANDING_REGISTRY_REFERENCED",
    "CARRIED_STANDING_STALE",
    "CARRIED_STANDING_CORRUPTED",
    "CARRIED_STANDING_EXCLUDED_FROM_RELIANCE",
}

REQUIRED_RECEIPT_POSTURE_BY_PROPAGATION_POSTURE = {
    "CARRIED_STANDING_RECEIVED": ("receipt_posture",),
    "CARRIED_STANDING_REFUSED_OR_BLOCKED": ("refusal_posture",),
    "CARRIED_STANDING_RETURNED": ("return_posture",),
    "CARRIED_STANDING_ADMITTED_AS_EVIDENCE": ("admission_posture",),
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "standing_propagation_created_source": False,
    "standing_propagation_created_currentness": False,
    "standing_propagation_created_authority": False,
    "standing_propagation_created_permission": False,
    "standing_propagation_created_carrier_hierarchy": False,
    "standing_propagation_created_distributed_standing": False,
    "standing_propagation_authorized_sync": False,
    "standing_propagation_authorized_full_body_transfer": False,
    "standing_propagation_created_second_body": False,
    "standing_propagation_authorized_continuation": False,
    "standing_propagation_authorized_distributed_operation": False,
    "standing_propagation_erased_evidence": False,
    "standing_propagation_hid_refusal": False,
    "standing_propagation_hid_divergence": False,
    "standing_propagation_hid_corruption": False,
    "standing_propagation_hid_staleness": False,
    "standing_propagation_repaired_by_overwrite": False,
    "standing_propagation_made_registry_reference_standing": False,
    "standing_propagation_made_receipt_standing": False,
    "standing_propagation_made_admission_standing": False,
    "current_carrier_selected": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "distributed_standing_created": False,
    "carrier_registry_created_as_authority": False,
    "repository_synchronization_authorized": False,
    "full_body_transfer_authorized": False,
    "second_body_created": False,
    "continuation_authorized": False,
    "distributed_operation_authorized": False,
    "latest_copy_currentness": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "DECLARED_STANDING_PROPAGATION_REQUEST_UNREADABLE": "Declared standing propagation request path could not be read.",
    "DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED": "Declared standing propagation request is not a JSON object or mapping.",
    "STANDING_PROPAGATION_QUESTION_UNDECLARED": "Standing propagation question is undeclared.",
    "STANDING_PROPAGATION_INTENT_UNSUPPORTED": "Standing propagation intent is unsupported.",
    "STANDING_PROPAGATION_REQUEST_EXPLICITLY_BLOCKED": "Standing propagation request explicitly declares a blocked posture.",
    "PROPAGATION_POSTURE_UNSUPPORTED": "Requested propagation posture is missing or unsupported.",
    "SELECTED_STANDING_SURFACE_OR_ARTIFACT_MISSING": "Selected standing surface or artifact is missing.",
    "SELECTED_STANDING_SURFACE_OR_ARTIFACT_MALFORMED": "Selected standing surface or artifact is malformed.",
    "SELECTED_STANDING_SURFACE_OR_ARTIFACT_IDENTITY_MISSING": "Selected standing surface or artifact identity is missing.",
    "SOURCE_STANDING_BASIS_MISSING": "Source standing basis is missing where required.",
    "CARRIER_IDENTITY_MISSING": "Carrier identity is missing where required or supplied.",
    "CARRIED_SURFACE_OR_PACKET_BASIS_MISSING": "Carried surface or packet basis is missing where required.",
    "RECEIPT_REFUSAL_RETURN_ADMISSION_POSTURE_MISSING": "Receipt, refusal, return, or admission posture is missing where required.",
    "PROPAGATION_HIDES_DIVERGENCE": "Standing propagation hides divergence.",
    "PROPAGATION_HIDES_REFUSAL": "Standing propagation hides refusal.",
    "PROPAGATION_HIDES_CORRUPTION": "Standing propagation hides corruption.",
    "PROPAGATION_HIDES_STALENESS": "Standing propagation hides staleness.",
    "PROPAGATION_LINEAGE_MISSING": "Standing propagation lineage is missing.",
    "PROPAGATION_REPLACES_SOURCE": "Standing propagation replaces source.",
    "PROPAGATION_CREATES_CURRENTNESS": "Standing propagation creates currentness.",
    "PROPAGATION_CREATES_AUTHORITY": "Standing propagation creates authority.",
    "PROPAGATION_CREATES_PERMISSION": "Standing propagation creates permission.",
    "PROPAGATION_CREATES_CARRIER_HIERARCHY": "Standing propagation creates carrier hierarchy.",
    "PROPAGATION_SELECTS_CURRENT_CARRIER": "Standing propagation selects a current carrier.",
    "PROPAGATION_SELECTS_WINNING_CARRIER": "Standing propagation selects a winning carrier.",
    "PROPAGATION_INVALIDATES_LOSING_CARRIER": "Standing propagation invalidates a losing carrier.",
    "PROPAGATION_RESOLVES_DIVERGENCE": "Standing propagation resolves divergence.",
    "PROPAGATION_ERASES_EVIDENCE": "Standing propagation erases evidence.",
    "PROPAGATION_REPAIRS_BY_OVERWRITE": "Standing propagation repairs by overwrite.",
    "PROPAGATION_CREATES_DISTRIBUTED_STANDING": "Standing propagation creates distributed standing.",
    "PROPAGATION_AUTHORIZES_REPOSITORY_SYNC": "Standing propagation authorizes repository synchronization.",
    "PROPAGATION_AUTHORIZES_FULL_BODY_TRANSFER": "Standing propagation authorizes full body transfer.",
    "PROPAGATION_CREATES_SECOND_BODY": "Standing propagation creates a second body.",
    "PROPAGATION_AUTHORIZES_CONTINUATION": "Standing propagation authorizes continuation.",
    "PROPAGATION_AUTHORIZES_DISTRIBUTED_OPERATION": "Standing propagation authorizes distributed operation.",
    "PROPAGATION_MAKES_REGISTRY_REFERENCE_STANDING": "Standing propagation makes a registry reference standing.",
    "PROPAGATION_MAKES_RECEIPT_STANDING": "Standing propagation makes receipt standing.",
    "PROPAGATION_MAKES_ADMISSION_STANDING": "Standing propagation makes admission standing.",
    "LATEST_COPY_CURRENTNESS": "Latest propagated copy is treated as currentness.",
    "LATEST_FILE_CURRENTNESS": "Latest-file recency or recency fraud is treated as currentness.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge was detected.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required standing propagation non-claim is missing or flipped.",
}

PROPAGATION_NON_MEANING = {
    "does_not_mean_distributed_standing": True,
    "does_not_mean_currentness": True,
    "does_not_mean_source_replacement": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_standing_on_every_carrier": True,
    "does_not_mean_standing_on_receiving_carrier": True,
    "does_not_mean_carrier_hierarchy": True,
    "does_not_mean_carrier_priority": True,
    "does_not_mean_carrier_sovereignty": True,
    "does_not_mean_current_carrier_selected": True,
    "does_not_mean_winning_carrier_selected": True,
    "does_not_mean_losing_carrier_invalidated": True,
    "does_not_mean_divergence_resolved": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_carrier_registry_authority": True,
    "does_not_mean_persistence_as_standing": True,
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
    "does_not_mean_success_means_propagation": True,
    "does_not_mean_registry_reference_means_propagation": True,
    "does_not_mean_receipt_means_standing": True,
    "does_not_mean_admission_means_standing": True,
    "does_not_mean_latest_propagated_record_currentness": True,
    "does_not_mean_majority_carrier_standing": True,
    "does_not_mean_successful_receipt_count_standing": True,
}

WHAT_REMAINS_OPEN = {
    "standing_propagation_implementation_refinement": True,
    "cross_carrier_currentness_successor_law": True,
    "divergence_consequence_law": True,
    "distributed_standing_boundary": True,
    "distributed_standing": True,
    "carrier_registry_implementation": True,
    "persistence_implementation": True,
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


def resolve_standing_propagation_boundary(
    declared_propagation_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded standing propagation posture request."""

    if declared_propagation_request is None:
        return _resolve_propagation({}, None, [])
    if not isinstance(declared_propagation_request, Mapping):
        return _resolve_propagation(
            {},
            None,
            ["DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED"],
        )
    return _resolve_propagation(copy.deepcopy(dict(declared_propagation_request)), None, [])


def resolve_standing_propagation_boundary_from_path(
    declared_propagation_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one bounded standing propagation posture request from JSON."""

    path = Path(declared_propagation_request_path)
    try:
        request = _read_json_mapping(path)
    except StandingPropagationBoundaryV2Error as exc:
        return _resolve_propagation({}, path, [exc.block_code])
    return _resolve_propagation(request, path, [])


def write_standing_propagation_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an additive v2 standing propagation result without overwriting."""

    if not isinstance(result, Mapping):
        raise StandingPropagationBoundaryV2Error(
            "DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED",
            "Standing propagation result must be a mapping.",
        )

    if output_path is None:
        summary = _as_mapping(result.get("standing_propagation_summary"))
        basis_id = (
            summary.get("standing_propagation_request_id")
            or summary.get("requested_propagation_posture")
            or "standing_propagation"
        )
        output_path = STANDING_PROPAGATION_BOUNDARY_ROOT / (
            f"{_safe_filename_part(basis_id)}__standing_propagation_v2_result.json"
        )

    target = _non_overwriting_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, ensure_ascii=False, default=str)
        + "\n",
        encoding="utf-8",
    )
    return target


def build_standing_propagation_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact v2 summary from full result body, not shallow fields."""

    checks = _mapping_list(result.get("propagation_checks"))
    question = _as_mapping(result.get("declared_standing_propagation_question"))
    selected = _as_mapping(result.get("selected_standing_surface_or_artifact"))
    source_basis = _as_mapping(result.get("source_standing_basis"))
    carriers = _as_mapping(result.get("selected_carriers"))
    carried_basis = _as_mapping(result.get("carried_surface_or_packet_basis"))
    basis = _as_mapping(result.get("standing_propagation_basis"))
    posture = _as_mapping(result.get("standing_propagation_posture"))
    statement = _as_mapping(result.get("propagation_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    projection = _projection_from_result(result)
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "standing_propagation_request_id": question.get("standing_propagation_request_id"),
        "standing_propagation_question": question.get("standing_propagation_question"),
        "standing_propagation_intent": question.get("standing_propagation_intent"),
        "requested_propagation_posture": posture.get("requested_propagation_posture"),
        "selected_standing_surface_or_artifact_id": selected.get(
            "selected_standing_surface_or_artifact_id"
        ),
        "source_standing_basis": source_basis.get("raw_source_standing_basis"),
        "selected_carrier_ids": carriers.get("selected_carrier_ids"),
        "carried_surface_or_packet_basis": carried_basis.get(
            "raw_carried_surface_or_packet_basis"
        ),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "standing_propagation_posture_recorded": bool(
            statement.get("standing_propagation_posture_recorded")
        ),
        "lineage_preserved": bool(
            statement.get("lineage_preserved") or projection["lineage_preserved"]
        ),
        "source_standing_preserved": projection["source_standing_preserved"],
        "visible_refusal_preserved": projection["visible_refusal_preserved"],
        "visible_divergence_preserved": projection["visible_divergence_preserved"],
        "visible_corruption_preserved": bool(
            statement.get("visible_corruption_preserved")
            or projection["visible_corruption_preserved"]
        ),
        "visible_staleness_preserved": bool(
            statement.get("visible_staleness_preserved")
            or projection["visible_staleness_preserved"]
        ),
        "receipt_refusal_return_admission_posture_preserved": projection[
            "receipt_refusal_return_admission_posture_preserved"
        ],
        "divergence_posture_preserved": projection["divergence_posture_preserved"],
        "currentness_participation_posture_preserved": projection[
            "currentness_participation_posture_preserved"
        ],
        "relation_posture_preserved": projection["relation_posture_preserved"],
        "lifecycle_posture_preserved": projection["lifecycle_posture_preserved"],
        "registry_persistence_posture_preserved": projection[
            "registry_persistence_posture_preserved"
        ],
        "no_source_currentness_authority_permission": not bool(
            statement.get("source_replaced")
            or statement.get("currentness_created")
            or statement.get("authority_created")
            or statement.get("permission_created")
        ),
        "no_carrier_hierarchy": not bool(statement.get("carrier_hierarchy_created")),
        "no_current_winning_losing_carrier_collapse": not bool(
            statement.get("current_carrier_selected")
            or statement.get("winning_carrier_selected")
            or statement.get("losing_carrier_invalidated")
        ),
        "no_divergence_resolution": not bool(statement.get("divergence_resolved")),
        "no_evidence_erasure": not bool(statement.get("evidence_erased")),
        "no_repair_by_overwrite": not bool(statement.get("repaired_by_overwrite")),
        "no_distributed_standing": not bool(statement.get("distributed_standing_created")),
        "no_sync_full_body_transfer_second_body": not bool(
            statement.get("repository_synchronization_authorized")
            or statement.get("full_body_transfer_authorized")
            or statement.get("second_body_created")
        ),
        "no_continuation": not bool(statement.get("continuation_authorized")),
        "no_distributed_operation": not bool(statement.get("distributed_operation_authorized")),
        "no_registry_reference_receipt_admission_standing": not bool(
            statement.get("standing_propagation_made_registry_reference_standing")
            or statement.get("standing_propagation_made_receipt_standing")
            or statement.get("standing_propagation_made_admission_standing")
        ),
        "no_latest_copy_file_currentness": not bool(
            statement.get("latest_copy_currentness")
            or statement.get("latest_file_currentness")
        ),
        "standing_propagation_basis": basis.get("raw_standing_propagation_basis"),
        "key_non_claims": _key_non_claims(non_claims),
        "successor_of_module": SUCCESSOR_OF_MODULE,
    }


def build_declared_standing_propagation_request(
    standing_propagation_request_id: str,
    standing_propagation_question: str,
    selected_standing_surface_or_artifact: Mapping[str, Any],
    requested_propagation_posture: str,
    standing_propagation_basis: Mapping[str, Any] | str,
    standing_propagation_intent: str = RECORD_INTENT,
    *,
    source_standing_basis: Mapping[str, Any] | str | None = None,
    selected_carriers: Sequence[Mapping[str, Any]] | None = None,
    related_carrier_evidence: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Build one bounded standing propagation request without inferring force."""

    posture = _normalize_token(requested_propagation_posture)
    request: dict[str, Any] = {
        "standing_propagation_request_id": standing_propagation_request_id,
        "standing_propagation_question": standing_propagation_question,
        "standing_propagation_intent": standing_propagation_intent,
        "selected_standing_surface_or_artifact": copy.deepcopy(
            dict(selected_standing_surface_or_artifact)
        ),
        "requested_propagation_posture": requested_propagation_posture,
        "standing_propagation_basis": copy.deepcopy(standing_propagation_basis),
        "lineage_basis": {
            "lineage_preserved": True,
            "source_standing_remains_upstream": True,
            "does_not_create_distributed_standing": True,
        },
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }
    if source_standing_basis is not None:
        request["source_standing_basis"] = copy.deepcopy(source_standing_basis)
    elif posture == "SOURCE_STANDING_PRESERVED":
        request["source_standing_basis"] = copy.deepcopy(standing_propagation_basis)
    if posture in CARRIED_POSTURES:
        request["carried_surface_or_packet_basis"] = copy.deepcopy(
            standing_propagation_basis
        )
    for field in REQUIRED_RECEIPT_POSTURE_BY_PROPAGATION_POSTURE.get(posture or "", ()):
        request[field] = {
            "posture": posture,
            "preserved": True,
            "standing_posture_only": True,
        }
    if selected_carriers is not None:
        request["selected_carriers"] = [
            copy.deepcopy(dict(item)) for item in selected_carriers
        ]
    if related_carrier_evidence is not None:
        request["related_carrier_evidence"] = [
            copy.deepcopy(dict(item)) for item in related_carrier_evidence
        ]
    return request


def _resolve_propagation(
    request: Mapping[str, Any],
    request_path: Path | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    normalized_request = _as_mapping(request)
    question = _declared_propagation_question(normalized_request, request_path)
    selected = _selected_standing_surface_or_artifact(normalized_request)
    posture = _standing_propagation_posture(normalized_request)
    source_basis = _source_standing_basis(normalized_request, posture)
    carriers = _selected_carriers(normalized_request)
    carried_basis = _carried_surface_or_packet_basis(normalized_request, posture)
    basis = _standing_propagation_basis(normalized_request)
    related_evidence = _related_carrier_evidence(normalized_request)
    projection = _projection_from_sections(
        normalized_request,
        source_basis,
        carried_basis,
        basis,
        related_evidence,
    )
    checks = _build_checks(
        normalized_request,
        question,
        selected,
        posture,
        source_basis,
        carriers,
        carried_basis,
        basis,
        related_evidence,
        projection,
        precheck_failures,
    )
    failed_checks = [check for check in checks if check.get("passed") is False]
    intent = question.get("standing_propagation_intent")
    explicit_block_code = _declared_block_code(normalized_request)

    if failed_checks:
        outcome = STANDING_PROPAGATION_POSTURE_BLOCKED
        block_code = str(failed_checks[0].get("block_code") or "NON_CLAIM_MISSING_OR_FLIPPED")
    elif intent == BLOCK_INTENT:
        outcome = STANDING_PROPAGATION_POSTURE_BLOCKED
        block_code = explicit_block_code or "STANDING_PROPAGATION_REQUEST_EXPLICITLY_BLOCKED"
    elif intent == DO_NOT_RECORD_INTENT:
        outcome = STANDING_PROPAGATION_POSTURE_NOT_RECORDED
        block_code = None
    else:
        outcome = STANDING_PROPAGATION_POSTURE_RECORDED
        block_code = None

    block_reason = _block_reason(block_code)
    result: dict[str, Any] = {
        "standing_propagation_metadata": {
            "standing_propagation_result_id": _result_id(question, posture, outcome),
            "standing_propagation_result_type": RESULT_TYPE,
            "standing_propagation_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
            "successor_of_module": SUCCESSOR_OF_MODULE,
        },
        "declared_standing_propagation_question": question,
        "selected_standing_surface_or_artifact": selected,
        "source_standing_basis": source_basis,
        "selected_carriers": carriers,
        "carried_surface_or_packet_basis": carried_basis,
        "standing_propagation_basis": basis,
        "standing_propagation_posture": posture,
        "related_carrier_evidence": related_evidence,
        "propagation_checks": checks,
        "propagation_statement": _propagation_statement(
            outcome,
            question,
            selected,
            posture,
            source_basis,
            carriers,
            carried_basis,
            basis,
            related_evidence,
            projection,
            checks,
            block_code,
            block_reason,
        ),
        "propagation_non_meaning": copy.deepcopy(PROPAGATION_NON_MEANING),
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
    result["standing_propagation_summary"] = build_standing_propagation_summary(result)
    return result


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    artifact_path = Path(path)
    try:
        loaded = json.loads(artifact_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise StandingPropagationBoundaryV2Error(
            "DECLARED_STANDING_PROPAGATION_REQUEST_UNREADABLE",
            BLOCK_REASONS["DECLARED_STANDING_PROPAGATION_REQUEST_UNREADABLE"],
        ) from exc
    except json.JSONDecodeError as exc:
        raise StandingPropagationBoundaryV2Error(
            "DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED",
            BLOCK_REASONS["DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED"],
        ) from exc
    if not isinstance(loaded, Mapping):
        raise StandingPropagationBoundaryV2Error(
            "DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED",
            BLOCK_REASONS["DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED"],
        )
    return copy.deepcopy(dict(loaded))


def _declared_propagation_question(
    request: Mapping[str, Any],
    request_path: Path | None,
) -> dict[str, Any]:
    section = _as_mapping(request.get("declared_standing_propagation_question"))
    return {
        "standing_propagation_request_id": request.get("standing_propagation_request_id")
        or section.get("standing_propagation_request_id"),
        "standing_propagation_request_path": _display_path(request_path)
        if request_path
        else request.get("_standing_propagation_request_path")
        or section.get("standing_propagation_request_path"),
        "standing_propagation_question": request.get("standing_propagation_question")
        or section.get("standing_propagation_question"),
        "standing_propagation_intent": _normalize_token(
            request.get("standing_propagation_intent")
            or section.get("standing_propagation_intent")
        ),
        "not_recorded_reason": request.get("not_recorded_reason")
        or section.get("not_recorded_reason"),
        "operator_note": request.get("operator_note") or section.get("operator_note"),
        "declared_non_claims": copy.deepcopy(
            request.get("declared_non_claims")
            or request.get("non_claims")
            or section.get("declared_non_claims")
        ),
        "records_one_standing_propagation_question": True,
        "standing_propagation_is_not_distributed_standing": True,
        "standing_propagation_is_not_currentness": True,
        "standing_propagation_is_not_authority": True,
        "standing_propagation_does_not_replace_source": True,
        "standing_propagation_does_not_authorize_sync_full_body_transfer_or_distributed_operation": True,
    }


def _selected_standing_surface_or_artifact(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("selected_standing_surface_or_artifact")
    if isinstance(raw, Mapping):
        selected = copy.deepcopy(dict(raw))
        identity = (
            selected.get("selected_standing_surface_or_artifact_id")
            or selected.get("standing_surface_or_artifact_id")
            or selected.get("standing_surface_id")
            or selected.get("artifact_id")
            or selected.get("surface_id")
            or selected.get("id")
        )
        parseable = True
    elif isinstance(raw, str):
        selected = raw
        identity = raw
        parseable = _nonempty(raw)
    elif raw is None:
        selected = None
        identity = None
        parseable = False
    else:
        selected = copy.deepcopy(raw)
        identity = None
        parseable = False
    return {
        "selected_standing_surface_or_artifact_declared": raw is not None,
        "selected_standing_surface_or_artifact_parseable": parseable,
        "selected_standing_surface_or_artifact_id": identity,
        "selected_standing_surface_or_artifact_identity_present": _nonempty(identity),
        "selected_standing_surface_or_artifact_preserved": parseable and _nonempty(identity),
        "selected_artifact_remains_evidence_or_reference": True,
        "selected_artifact_does_not_become_distributed_standing": True,
        "selected_artifact_does_not_create_currentness": True,
        "raw_selected_standing_surface_or_artifact": copy.deepcopy(selected),
    }


def _standing_propagation_posture(request: Mapping[str, Any]) -> dict[str, Any]:
    section = _as_mapping(request.get("standing_propagation_posture"))
    raw = request.get("requested_propagation_posture") or section.get(
        "requested_propagation_posture"
    )
    posture = _normalize_token(raw)
    return {
        "requested_propagation_posture_declared": posture is not None,
        "requested_propagation_posture": posture,
        "requested_propagation_posture_supported": posture in SUPPORTED_PROPAGATION_POSTURES,
        "requested_propagation_posture_preserved": posture is not None,
        "raw_requested_propagation_posture": copy.deepcopy(raw),
        "posture_does_not_mean_distributed_standing": True,
        "posture_does_not_mean_currentness": True,
        "posture_does_not_mean_standing_on_receiving_carrier": True,
    }


def _source_standing_basis(
    request: Mapping[str, Any],
    posture: Mapping[str, Any],
) -> dict[str, Any]:
    raw_basis = _nested_or_direct(request, "source_standing_basis")
    raw_basis_mapping = _as_mapping(raw_basis)
    raw_standing_basis = _raw_standing_basis_mapping(request.get("standing_propagation_basis"))
    required = bool(
        _truthy_flag(request, ("source_standing_basis_required",))
        or posture.get("requested_propagation_posture") == "SOURCE_STANDING_PRESERVED"
    )
    declared = _basis_declared(raw_basis)
    preserved_by_projection = bool(
        raw_basis_mapping.get("source_standing_basis_preserved_upstream")
        or raw_basis_mapping.get("source_standing_preserved")
        or raw_standing_basis.get("source_standing_preserved")
    )
    return {
        "source_standing_basis_required": required,
        "source_standing_basis_declared": declared,
        "source_standing_basis_preserved": declared or preserved_by_projection,
        "source_standing_preserved": declared or preserved_by_projection or not required,
        "source_standing_remains_upstream": True,
        "carrying_does_not_move_source_standing": True,
        "receipt_does_not_replace_source_standing": True,
        "admission_does_not_move_source_standing": True,
        "registry_reference_does_not_move_source_standing": True,
        "raw_source_standing_basis": copy.deepcopy(raw_basis),
    }


def _selected_carriers(request: Mapping[str, Any]) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    parseable = True
    raw_selected = request.get("selected_carriers")

    if raw_selected is not None:
        normalized, selected_parseable = _carrier_entries(raw_selected, "selected")
        entries.extend(normalized)
        parseable = parseable and selected_parseable

    for field, role in (("source_carrier", "source"), ("receiving_carrier", "receiving")):
        raw = request.get(field)
        if raw is not None:
            normalized, field_parseable = _carrier_entries(raw, role)
            entries.extend(normalized)
            parseable = parseable and field_parseable

    carrier_ids = [
        entry.get("carrier_id") for entry in entries if _nonempty(entry.get("carrier_id"))
    ]
    supplied = (
        raw_selected is not None
        or request.get("source_carrier") is not None
        or request.get("receiving_carrier") is not None
    )
    required = bool(
        _truthy_flag(
            request,
            (
                "carrier_identity_required",
                "selected_carrier_identity_required",
                "selected_carriers_required",
            ),
        )
    )
    all_supplied_have_identity = (
        not supplied or (parseable and len(carrier_ids) == len(entries))
    )
    return {
        "selected_carriers_required": required,
        "selected_carriers_supplied": supplied,
        "selected_carriers_parseable": parseable,
        "selected_carrier_entries": entries,
        "selected_carrier_ids": carrier_ids,
        "carrier_identity_preserved_where_supplied": all_supplied_have_identity,
        "selected_carriers_preserved": supplied and parseable and bool(carrier_ids),
        "source_carrier": copy.deepcopy(request.get("source_carrier")),
        "receiving_carrier": copy.deepcopy(request.get("receiving_carrier")),
        "carriers_do_not_become_currentness": True,
        "carriers_do_not_create_distributed_standing": True,
        "raw_selected_carriers": copy.deepcopy(raw_selected),
    }


def _carried_surface_or_packet_basis(
    request: Mapping[str, Any],
    posture: Mapping[str, Any],
) -> dict[str, Any]:
    raw_basis = _nested_or_direct(request, "carried_surface_or_packet_basis")
    requested_posture = posture.get("requested_propagation_posture")
    required = bool(
        requested_posture in CARRIED_POSTURES
        or _truthy_flag(request, ("carried_surface_or_packet_basis_required",))
    )
    declared = _basis_declared(raw_basis)
    return {
        "carried_surface_or_packet_basis_required": required,
        "carried_surface_or_packet_basis_declared": declared,
        "carried_surface_or_packet_basis_preserved": declared,
        "carried_surface_remains_evidence_or_reference": True,
        "carried_surface_does_not_become_currentness": True,
        "carried_surface_does_not_become_standing_on_receiver": True,
        "raw_carried_surface_or_packet_basis": copy.deepcopy(raw_basis),
    }


def _standing_propagation_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    raw_basis = request.get("standing_propagation_basis")
    raw_basis_value = _raw_standing_basis_value(raw_basis)
    raw_basis_mapping = _as_mapping(raw_basis_value)
    visible_refusal = _direct_visible_posture(
        request,
        raw_basis_mapping,
        "refusal",
    )
    visible_divergence = _direct_visible_posture(
        request,
        raw_basis_mapping,
        "divergence",
    )
    visible_corruption = _direct_visible_posture(
        request,
        raw_basis_mapping,
        "corruption",
    )
    visible_staleness = _direct_visible_posture(
        request,
        raw_basis_mapping,
        "staleness",
    )
    lineage_basis = (
        request.get("lineage_basis")
        or raw_basis_mapping.get("lineage_basis")
        or raw_basis_mapping
    )
    lineage_missing = _truthy_flag(request, ("lineage_missing", "propagation_lineage_missing"))
    lineage_preserved = (
        not lineage_missing
        and _basis_declared(raw_basis_value)
        and not _false_flag(lineage_basis, ("lineage_preserved", "preserved"))
        and not _false_flag(raw_basis_mapping, ("lineage_preserved",))
    )
    return {
        "standing_propagation_basis_declared": _basis_declared(raw_basis_value),
        "standing_propagation_basis_preserved": _basis_declared(raw_basis_value),
        "raw_standing_propagation_basis": copy.deepcopy(raw_basis_value),
        "lineage_basis": copy.deepcopy(lineage_basis),
        "lineage_preserved": lineage_preserved,
        "visible_refusal_available": visible_refusal["available"],
        "visible_refusal_preserved": visible_refusal["preserved"],
        "visible_refusal_basis": copy.deepcopy(
            request.get("visible_refusal_basis")
            or raw_basis_mapping.get("visible_refusal_basis")
        ),
        "visible_divergence_available": visible_divergence["available"],
        "visible_divergence_preserved": visible_divergence["preserved"],
        "visible_divergence_basis": copy.deepcopy(
            request.get("visible_divergence_basis")
            or raw_basis_mapping.get("visible_divergence_basis")
        ),
        "visible_corruption_available": visible_corruption["available"],
        "visible_corruption_preserved": visible_corruption["preserved"],
        "visible_corruption_basis": copy.deepcopy(
            request.get("visible_corruption_basis")
            or raw_basis_mapping.get("visible_corruption_basis")
        ),
        "visible_staleness_available": visible_staleness["available"],
        "visible_staleness_preserved": visible_staleness["preserved"],
        "visible_staleness_basis": copy.deepcopy(
            request.get("visible_staleness_basis")
            or raw_basis_mapping.get("visible_staleness_basis")
        ),
        "receipt_posture": _posture_basis(request, raw_basis_mapping, "receipt_posture"),
        "refusal_posture": _posture_basis(request, raw_basis_mapping, "refusal_posture"),
        "return_posture": _posture_basis(request, raw_basis_mapping, "return_posture"),
        "admission_posture": _posture_basis(request, raw_basis_mapping, "admission_posture"),
        "receipt_refusal_return_admission_posture": _posture_basis(
            request,
            raw_basis_mapping,
            "receipt_refusal_return_admission_posture",
        ),
        "divergence_posture": _posture_basis(request, raw_basis_mapping, "divergence_posture"),
        "currentness_participation_posture": _posture_basis(
            request,
            raw_basis_mapping,
            "currentness_participation_posture",
        ),
        "relation_posture": _posture_basis(request, raw_basis_mapping, "relation_posture"),
        "lifecycle_posture": _posture_basis(request, raw_basis_mapping, "lifecycle_posture"),
        "registry_persistence_posture": _posture_basis(
            request,
            raw_basis_mapping,
            "registry_persistence_posture",
        ),
        "propagation_preserves_evidence_not_force": True,
        "propagation_does_not_create_distributed_standing": True,
        "propagation_does_not_authorize_continuation": True,
    }


def _related_carrier_evidence(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("related_carrier_evidence")
    if raw is None:
        return {
            "related_carrier_evidence_supplied": False,
            "related_carrier_evidence_parseable": True,
            "related_carrier_evidence_entries": [],
            "related_carrier_evidence_ids": [],
            "related_carrier_evidence_outcomes": [],
            "related_carrier_ids": [],
            "related_carrier_evidence_preserved": False,
            "evidence_remains_evidence": True,
            "raw_related_carrier_evidence": None,
        }
    entries: list[dict[str, Any]] = []
    parseable = True
    raw_items: Sequence[Any]
    if isinstance(raw, Mapping):
        if isinstance(raw.get("related_carrier_evidence_entries"), list):
            raw_items = raw.get("related_carrier_evidence_entries") or []
        else:
            raw_items = [raw]
    elif isinstance(raw, list):
        raw_items = raw
    else:
        raw_items = []
        parseable = False

    for item in raw_items:
        if not isinstance(item, Mapping):
            parseable = False
            continue
        entry = copy.deepcopy(dict(item))
        raw_evidence = _as_mapping(entry.get("raw_evidence")) or entry
        evidence_id = (
            entry.get("evidence_id")
            or entry.get("artifact_id")
            or entry.get("result_id")
            or entry.get("id")
            or raw_evidence.get("evidence_id")
            or raw_evidence.get("artifact_id")
            or raw_evidence.get("result_id")
            or raw_evidence.get("id")
        )
        outcome = (
            entry.get("outcome")
            or entry.get("result_outcome")
            or entry.get("evidence_outcome")
            or entry.get("status")
            or raw_evidence.get("outcome")
            or raw_evidence.get("result_outcome")
            or raw_evidence.get("evidence_outcome")
            or raw_evidence.get("status")
        )
        carrier_id = (
            entry.get("carrier_id")
            or entry.get("selected_carrier_id")
            or raw_evidence.get("carrier_id")
            or raw_evidence.get("selected_carrier_id")
        )
        role = (
            entry.get("evidence_role")
            or entry.get("role")
            or raw_evidence.get("evidence_role")
            or raw_evidence.get("role")
        )
        evidence_class = (
            entry.get("evidence_class")
            or entry.get("artifact_class")
            or raw_evidence.get("evidence_class")
            or raw_evidence.get("artifact_class")
        )
        entries.append(
            {
                "evidence_id": evidence_id,
                "outcome": outcome,
                "carrier_id": carrier_id,
                "evidence_role": role,
                "evidence_class": evidence_class,
                "raw_evidence": entry,
            }
        )

    return {
        "related_carrier_evidence_supplied": True,
        "related_carrier_evidence_parseable": parseable,
        "related_carrier_evidence_entries": entries,
        "related_carrier_evidence_ids": [
            entry.get("evidence_id") for entry in entries if _nonempty(entry.get("evidence_id"))
        ],
        "related_carrier_evidence_outcomes": [
            entry.get("outcome") for entry in entries if _nonempty(entry.get("outcome"))
        ],
        "related_carrier_ids": [
            entry.get("carrier_id") for entry in entries if _nonempty(entry.get("carrier_id"))
        ],
        "related_carrier_evidence_preserved": parseable and bool(entries),
        "evidence_remains_evidence": True,
        "evidence_does_not_create_standing_by_relation": True,
        "raw_related_carrier_evidence": copy.deepcopy(raw),
    }


def _build_checks(
    request: Mapping[str, Any],
    question: Mapping[str, Any],
    selected: Mapping[str, Any],
    posture: Mapping[str, Any],
    source_basis: Mapping[str, Any],
    carriers: Mapping[str, Any],
    carried_basis: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
    projection: Mapping[str, bool],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    collapse_source = _without_safe_sections(request)
    declared_non_claims = _as_mapping(
        request.get("declared_non_claims")
        or request.get("non_claims")
        or question.get("declared_non_claims")
    )
    sources = [
        collapse_source,
        question,
        selected,
        posture,
        source_basis,
        carriers,
        carried_basis,
        basis,
        related_evidence,
        declared_non_claims,
    ]
    precheck_code = precheck_failures[0] if precheck_failures else None
    requested_posture = posture.get("requested_propagation_posture")
    required_posture_fields = REQUIRED_RECEIPT_POSTURE_BY_PROPAGATION_POSTURE.get(
        str(requested_posture),
        (),
    )
    receipt_signal = bool(
        required_posture_fields
        or _posture_supplied(basis, "receipt_posture")
        or _posture_supplied(basis, "refusal_posture")
        or _posture_supplied(basis, "return_posture")
        or _posture_supplied(basis, "admission_posture")
        or _posture_supplied(basis, "receipt_refusal_return_admission_posture")
    )
    refusal_signal = _visible_refusal_signal(request, basis, related_evidence)
    divergence_signal = _visible_divergence_signal(request, basis, related_evidence)

    checks = [
        _check(
            "declared_standing_propagation_request_parseable_mapping",
            not precheck_failures,
            "declared standing propagation request is a parseable mapping",
            list(precheck_failures),
            precheck_code or "DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED",
        ),
        _check(
            "standing_propagation_question_declared",
            _nonempty(question.get("standing_propagation_question")),
            "standing propagation question is declared",
            question.get("standing_propagation_question"),
            "STANDING_PROPAGATION_QUESTION_UNDECLARED",
        ),
        _check(
            "standing_propagation_intent_supported",
            question.get("standing_propagation_intent") in SUPPORTED_PROPAGATION_INTENTS,
            "standing propagation intent is supported",
            question.get("standing_propagation_intent"),
            "STANDING_PROPAGATION_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_standing_surface_or_artifact_present",
            bool(selected.get("selected_standing_surface_or_artifact_declared")),
            "selected standing surface or artifact is present",
            selected.get("raw_selected_standing_surface_or_artifact"),
            "SELECTED_STANDING_SURFACE_OR_ARTIFACT_MISSING",
        ),
        _check(
            "selected_standing_surface_or_artifact_parseable",
            bool(selected.get("selected_standing_surface_or_artifact_parseable")),
            "selected standing surface or artifact is parseable",
            _shape(selected.get("raw_selected_standing_surface_or_artifact")),
            "SELECTED_STANDING_SURFACE_OR_ARTIFACT_MALFORMED",
        ),
        _check(
            "selected_standing_surface_or_artifact_identity_present",
            bool(selected.get("selected_standing_surface_or_artifact_identity_present")),
            "selected standing surface or artifact identity is present",
            selected.get("selected_standing_surface_or_artifact_id"),
            "SELECTED_STANDING_SURFACE_OR_ARTIFACT_IDENTITY_MISSING",
        ),
        _check(
            "requested_propagation_posture_supported",
            bool(posture.get("requested_propagation_posture_supported")),
            "requested propagation posture is supported",
            posture.get("requested_propagation_posture"),
            "PROPAGATION_POSTURE_UNSUPPORTED",
        ),
        _check(
            "standing_propagation_basis_declared",
            bool(basis.get("standing_propagation_basis_declared")),
            "standing propagation basis is declared",
            basis.get("raw_standing_propagation_basis"),
            "CARRIED_SURFACE_OR_PACKET_BASIS_MISSING",
        ),
        _check(
            "source_standing_basis_preserved_where_required",
            not source_basis.get("source_standing_basis_required")
            or bool(projection.get("source_standing_preserved")),
            "source standing basis is preserved where required",
            source_basis.get("raw_source_standing_basis"),
            "SOURCE_STANDING_BASIS_MISSING",
        ),
        _check(
            "carrier_identity_preserved_where_required_or_supplied",
            (
                not carriers.get("selected_carriers_required")
                and not carriers.get("selected_carriers_supplied")
            )
            or bool(carriers.get("carrier_identity_preserved_where_supplied")),
            "carrier identity is preserved where required or supplied",
            {
                "selected_carriers_required": carriers.get("selected_carriers_required"),
                "selected_carrier_ids": carriers.get("selected_carrier_ids"),
            },
            "CARRIER_IDENTITY_MISSING",
        ),
        _check(
            "carried_surface_or_packet_basis_preserved_where_required",
            not carried_basis.get("carried_surface_or_packet_basis_required")
            or bool(carried_basis.get("carried_surface_or_packet_basis_preserved")),
            "carried surface or packet basis is preserved where required",
            carried_basis.get("raw_carried_surface_or_packet_basis"),
            "CARRIED_SURFACE_OR_PACKET_BASIS_MISSING",
        ),
        _check(
            "receipt_refusal_return_admission_posture_preserved_where_required",
            not receipt_signal
            or bool(projection.get("receipt_refusal_return_admission_posture_preserved")),
            "receipt/refusal/return/admission posture is preserved where supplied or inferable",
            {
                "required_fields": required_posture_fields,
                "receipt_refusal_return_admission_posture": basis.get(
                    "receipt_refusal_return_admission_posture"
                ),
                "projection": projection.get(
                    "receipt_refusal_return_admission_posture_preserved"
                ),
            },
            "RECEIPT_REFUSAL_RETURN_ADMISSION_POSTURE_MISSING",
        ),
        _check(
            "lineage_preserved",
            bool(projection.get("lineage_preserved")),
            "lineage is preserved",
            basis.get("lineage_basis"),
            "PROPAGATION_LINEAGE_MISSING",
        ),
        _check(
            "visible_refusal_preserved_where_applicable",
            not refusal_signal or bool(projection.get("visible_refusal_preserved")),
            "visible refusal remains visible where supplied or inferable",
            {
                "visible_refusal_basis": basis.get("visible_refusal_basis"),
                "projection": projection.get("visible_refusal_preserved"),
            },
            "PROPAGATION_HIDES_REFUSAL",
        ),
        _check(
            "visible_divergence_preserved_where_applicable",
            not divergence_signal or bool(projection.get("visible_divergence_preserved")),
            "visible divergence remains visible where supplied or inferable",
            {
                "visible_divergence_basis": basis.get("visible_divergence_basis"),
                "projection": projection.get("visible_divergence_preserved"),
            },
            "PROPAGATION_HIDES_DIVERGENCE",
        ),
        _check(
            "visible_corruption_preserved_where_applicable",
            not basis.get("visible_corruption_available")
            or bool(projection.get("visible_corruption_preserved")),
            "visible corruption remains visible where applicable",
            basis.get("visible_corruption_basis"),
            "PROPAGATION_HIDES_CORRUPTION",
        ),
        _check(
            "visible_staleness_preserved_where_applicable",
            not basis.get("visible_staleness_available")
            or bool(projection.get("visible_staleness_preserved")),
            "visible staleness remains visible where applicable",
            basis.get("visible_staleness_basis"),
            "PROPAGATION_HIDES_STALENESS",
        ),
        _collapse_check(
            "no_source_replacement",
            sources,
            (
                "source_replaced",
                "standing_propagation_created_source",
                "propagation_replaces_source",
                "propagation_replaced_source",
                "source_replacement_created",
                "standing_source_replaced",
            ),
            "standing propagation does not replace source",
            "PROPAGATION_REPLACES_SOURCE",
        ),
        _collapse_check(
            "no_currentness",
            sources,
            (
                "currentness_created",
                "standing_propagation_created_currentness",
                "propagation_creates_currentness",
                "propagation_created_currentness",
                "standing_became_currentness",
            ),
            "standing propagation does not create currentness",
            "PROPAGATION_CREATES_CURRENTNESS",
        ),
        _collapse_check(
            "no_authority",
            sources,
            (
                "authority_created",
                "standing_propagation_created_authority",
                "propagation_creates_authority",
                "propagation_created_authority",
            ),
            "standing propagation does not create authority",
            "PROPAGATION_CREATES_AUTHORITY",
        ),
        _collapse_check(
            "no_permission",
            sources,
            (
                "permission_created",
                "standing_propagation_created_permission",
                "propagation_creates_permission",
                "propagation_created_permission",
            ),
            "standing propagation does not create permission",
            "PROPAGATION_CREATES_PERMISSION",
        ),
        _collapse_check(
            "no_carrier_hierarchy",
            sources,
            (
                "carrier_hierarchy_created",
                "standing_propagation_created_carrier_hierarchy",
                "propagation_creates_carrier_hierarchy",
                "carrier_priority_created",
            ),
            "standing propagation does not create carrier hierarchy",
            "PROPAGATION_CREATES_CARRIER_HIERARCHY",
        ),
        _collapse_check(
            "no_current_carrier_selected",
            sources,
            ("current_carrier_selected", "propagation_selects_current_carrier"),
            "standing propagation does not select a current carrier",
            "PROPAGATION_SELECTS_CURRENT_CARRIER",
        ),
        _collapse_check(
            "no_winning_carrier_selected",
            sources,
            ("winning_carrier_selected", "propagation_selects_winning_carrier"),
            "standing propagation does not select a winning carrier",
            "PROPAGATION_SELECTS_WINNING_CARRIER",
        ),
        _collapse_check(
            "no_losing_carrier_invalidated",
            sources,
            ("losing_carrier_invalidated", "propagation_invalidates_losing_carrier"),
            "standing propagation does not invalidate a losing carrier",
            "PROPAGATION_INVALIDATES_LOSING_CARRIER",
        ),
        _collapse_check(
            "no_divergence_resolution",
            sources,
            ("divergence_resolved", "propagation_resolves_divergence"),
            "standing propagation does not resolve divergence",
            "PROPAGATION_RESOLVES_DIVERGENCE",
        ),
        _collapse_check(
            "no_evidence_erasure",
            sources,
            (
                "evidence_erased",
                "prior_evidence_erased",
                "standing_propagation_erased_evidence",
                "propagation_erases_evidence",
            ),
            "standing propagation does not erase evidence",
            "PROPAGATION_ERASES_EVIDENCE",
        ),
        _collapse_check(
            "no_repair_by_overwrite",
            sources,
            (
                "repaired_by_overwrite",
                "standing_propagation_repaired_by_overwrite",
                "propagation_repairs_by_overwrite",
            ),
            "standing propagation does not repair by overwrite",
            "PROPAGATION_REPAIRS_BY_OVERWRITE",
        ),
        _collapse_check(
            "no_distributed_standing",
            sources,
            (
                "distributed_standing_created",
                "standing_propagation_created_distributed_standing",
                "propagation_creates_distributed_standing",
            ),
            "standing propagation does not create distributed standing",
            "PROPAGATION_CREATES_DISTRIBUTED_STANDING",
        ),
        _collapse_check(
            "no_repository_synchronization",
            sources,
            (
                "repository_synchronization_authorized",
                "standing_propagation_authorized_sync",
                "propagation_authorizes_repository_sync",
            ),
            "standing propagation does not authorize repository synchronization",
            "PROPAGATION_AUTHORIZES_REPOSITORY_SYNC",
        ),
        _collapse_check(
            "no_full_body_transfer",
            sources,
            (
                "full_body_transfer_authorized",
                "standing_propagation_authorized_full_body_transfer",
                "propagation_authorizes_full_body_transfer",
            ),
            "standing propagation does not authorize full body transfer",
            "PROPAGATION_AUTHORIZES_FULL_BODY_TRANSFER",
        ),
        _collapse_check(
            "no_second_body",
            sources,
            (
                "second_body_created",
                "standing_propagation_created_second_body",
                "propagation_creates_second_body",
            ),
            "standing propagation does not create a second body",
            "PROPAGATION_CREATES_SECOND_BODY",
        ),
        _collapse_check(
            "no_continuation",
            sources,
            (
                "continuation_authorized",
                "standing_propagation_authorized_continuation",
                "propagation_authorizes_continuation",
            ),
            "standing propagation does not authorize continuation",
            "PROPAGATION_AUTHORIZES_CONTINUATION",
        ),
        _collapse_check(
            "no_distributed_operation",
            sources,
            (
                "distributed_operation_authorized",
                "standing_propagation_authorized_distributed_operation",
                "propagation_authorizes_distributed_operation",
            ),
            "standing propagation does not authorize distributed operation",
            "PROPAGATION_AUTHORIZES_DISTRIBUTED_OPERATION",
        ),
        _collapse_check(
            "no_registry_reference_standing",
            sources,
            (
                "standing_propagation_made_registry_reference_standing",
                "registry_reference_standing",
                "propagation_makes_registry_reference_standing",
            ),
            "standing propagation does not make registry reference standing",
            "PROPAGATION_MAKES_REGISTRY_REFERENCE_STANDING",
        ),
        _collapse_check(
            "no_receipt_standing",
            sources,
            (
                "standing_propagation_made_receipt_standing",
                "receipt_standing",
                "successful_receipt_standing",
                "propagation_makes_receipt_standing",
            ),
            "standing propagation does not make receipt standing",
            "PROPAGATION_MAKES_RECEIPT_STANDING",
        ),
        _collapse_check(
            "no_admission_standing",
            sources,
            (
                "standing_propagation_made_admission_standing",
                "admission_standing",
                "propagation_makes_admission_standing",
            ),
            "standing propagation does not make admission standing",
            "PROPAGATION_MAKES_ADMISSION_STANDING",
        ),
        _collapse_check(
            "no_latest_copy_currentness",
            sources,
            (
                "latest_copy_currentness",
                "latest_propagated_record_currentness",
                "propagation_uses_latest_copy_as_currentness",
            ),
            "standing propagation does not make latest copy current",
            "LATEST_COPY_CURRENTNESS",
        ),
        _collapse_check(
            "no_latest_file_currentness_or_recency_fraud",
            sources,
            (
                "latest_file_currentness",
                "recency_fraud",
                "latest_file_recency_currentness",
            ),
            "standing propagation does not use latest-file recency as currentness",
            "LATEST_FILE_CURRENTNESS",
        ),
        _collapse_check(
            "no_mutation_replay_or_merge",
            sources,
            (
                "mutation_performed",
                "replay_performed",
                "merge_performed",
                "propagation_mutated_evidence",
                "propagation_replayed_source_body",
                "propagation_merged_carriers",
            ),
            "standing propagation does not mutate, replay, or merge",
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "non_claims_remain_false",
            _required_non_claims_false(declared_non_claims),
            "required standing propagation non-claims remain false",
            declared_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    return checks


def _propagation_statement(
    outcome: str,
    question: Mapping[str, Any],
    selected: Mapping[str, Any],
    posture: Mapping[str, Any],
    source_basis: Mapping[str, Any],
    carriers: Mapping[str, Any],
    carried_basis: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
    projection: Mapping[str, bool],
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    recorded = outcome == STANDING_PROPAGATION_POSTURE_RECORDED
    not_recorded = outcome == STANDING_PROPAGATION_POSTURE_NOT_RECORDED
    return {
        "standing_propagation_posture_recorded": recorded,
        "not_recorded_reason": question.get("not_recorded_reason")
        or ("standing propagation posture explicitly not recorded" if not_recorded else None),
        "block_code": block_code,
        "block_reason": block_reason,
        "selected_standing_surface_or_artifact_preserved": bool(
            selected.get("selected_standing_surface_or_artifact_preserved")
        ),
        "requested_propagation_posture_preserved": bool(
            posture.get("requested_propagation_posture_preserved")
        ),
        "source_standing_basis_preserved": bool(
            source_basis.get("source_standing_basis_preserved")
            or projection["source_standing_preserved"]
        ),
        "source_standing_preserved": projection["source_standing_preserved"],
        "selected_carriers_preserved": bool(carriers.get("selected_carriers_preserved")),
        "carried_surface_or_packet_basis_preserved": bool(
            carried_basis.get("carried_surface_or_packet_basis_preserved")
        ),
        "receipt_refusal_return_admission_posture_preserved": projection[
            "receipt_refusal_return_admission_posture_preserved"
        ],
        "divergence_posture_preserved": projection["divergence_posture_preserved"],
        "currentness_participation_posture_preserved": projection[
            "currentness_participation_posture_preserved"
        ],
        "relation_posture_preserved": projection["relation_posture_preserved"],
        "lifecycle_posture_preserved": projection["lifecycle_posture_preserved"],
        "registry_persistence_posture_preserved": projection[
            "registry_persistence_posture_preserved"
        ],
        "related_carrier_evidence_preserved": bool(
            related_evidence.get("related_carrier_evidence_preserved")
        ),
        "lineage_preserved": projection["lineage_preserved"],
        "visible_refusal_preserved": projection["visible_refusal_preserved"],
        "visible_divergence_preserved": projection["visible_divergence_preserved"],
        "visible_corruption_preserved": projection["visible_corruption_preserved"],
        "visible_staleness_preserved": projection["visible_staleness_preserved"],
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "source_replaced": False,
        "currentness_created": False,
        "authority_created": False,
        "permission_created": False,
        "carrier_hierarchy_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "divergence_resolved": False,
        "evidence_erased": False,
        "repaired_by_overwrite": False,
        "distributed_standing_created": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
        "standing_propagation_made_registry_reference_standing": False,
        "standing_propagation_made_receipt_standing": False,
        "standing_propagation_made_admission_standing": False,
        "standing_on_receiving_carrier_created": False,
        "received_standing_evidence_became_standing_on_receiver": False,
        "returned_standing_evidence_became_admission": False,
        "admitted_standing_evidence_became_source": False,
        "latest_copy_currentness": False,
        "latest_file_currentness": False,
        "recency_fraud": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
        "successor_of_module": SUCCESSOR_OF_MODULE,
    }


def _projection_from_result(result: Mapping[str, Any]) -> dict[str, bool]:
    return _projection_from_sections(
        result,
        _as_mapping(result.get("source_standing_basis")),
        _as_mapping(result.get("carried_surface_or_packet_basis")),
        _as_mapping(result.get("standing_propagation_basis")),
        _as_mapping(result.get("related_carrier_evidence")),
    )


def _projection_from_sections(
    request_or_result: Mapping[str, Any],
    source_basis: Mapping[str, Any],
    carried_basis: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
) -> dict[str, bool]:
    return {
        "lineage_preserved": _project_lineage_preserved(request_or_result, basis),
        "source_standing_preserved": _project_source_standing_preserved(
            request_or_result,
            source_basis,
            basis,
        ),
        "visible_refusal_preserved": _project_visible_refusal_preserved(
            request_or_result,
            basis,
            related_evidence,
        ),
        "visible_divergence_preserved": _project_visible_divergence_preserved(
            request_or_result,
            basis,
            related_evidence,
        ),
        "visible_corruption_preserved": bool(basis.get("visible_corruption_preserved")),
        "visible_staleness_preserved": bool(basis.get("visible_staleness_preserved")),
        "receipt_refusal_return_admission_posture_preserved": (
            _project_receipt_refusal_return_admission_preserved(
                request_or_result,
                basis,
            )
        ),
        "divergence_posture_preserved": _project_divergence_posture_preserved(
            request_or_result,
            basis,
            related_evidence,
        ),
        "currentness_participation_posture_preserved": _project_posture_preserved(
            request_or_result,
            basis,
            "currentness_participation_posture",
        ),
        "relation_posture_preserved": _project_posture_preserved(
            request_or_result,
            basis,
            "relation_posture",
        ),
        "lifecycle_posture_preserved": _project_lifecycle_posture_preserved(
            request_or_result,
            basis,
            related_evidence,
        ),
        "registry_persistence_posture_preserved": (
            _project_registry_persistence_posture_preserved(
                request_or_result,
                basis,
                related_evidence,
            )
        ),
        "carried_surface_or_packet_basis_preserved": bool(
            carried_basis.get("carried_surface_or_packet_basis_preserved")
        ),
    }


def _project_lineage_preserved(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
) -> bool:
    if _truthy_flag(request_or_result, ("lineage_missing", "propagation_lineage_missing")):
        return False
    raw_basis = _raw_standing_basis_mapping(basis)
    if bool(basis.get("lineage_preserved")) or bool(raw_basis.get("lineage_preserved")):
        return True
    lineage = _as_mapping(basis.get("lineage_basis") or raw_basis.get("lineage_basis"))
    return bool(lineage.get("lineage_preserved") or lineage.get("preserved"))


def _project_source_standing_preserved(
    request_or_result: Mapping[str, Any],
    source_basis: Mapping[str, Any],
    basis: Mapping[str, Any],
) -> bool:
    raw_source = _as_mapping(
        source_basis.get("raw_source_standing_basis")
        or request_or_result.get("source_standing_basis")
    )
    raw_basis = _raw_standing_basis_mapping(basis)
    return bool(
        source_basis.get("source_standing_preserved")
        or source_basis.get("source_standing_basis_preserved")
        or raw_source.get("source_standing_basis_preserved_upstream")
        or raw_source.get("source_standing_preserved")
        or raw_basis.get("source_standing_preserved")
        or _truthy_flag(raw_basis, ("source_standing_basis_preserved_upstream",))
    )


def _project_visible_refusal_preserved(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
) -> bool:
    if _hidden(request_or_result, basis, related_evidence, "refusal"):
        return False
    raw_basis = _raw_standing_basis_mapping(basis)
    if bool(basis.get("visible_refusal_preserved")):
        return True
    if bool(raw_basis.get("visible_refusal_preserved")):
        return True
    rra = _as_mapping(raw_basis.get("receipt_refusal_return_admission_posture"))
    if bool(rra.get("carrier_c_returned_blocked_receipt_preserved")):
        return True
    refusal = _raw_posture_mapping(request_or_result, basis, "refusal_posture")
    if bool(
        refusal.get("visible_refusal_preserved")
        or refusal.get("refusal_preserved")
        or refusal.get("preserved")
    ):
        return True
    visible_basis = _as_mapping(
        request_or_result.get("visible_refusal_basis")
        or raw_basis.get("visible_refusal_basis")
        or basis.get("visible_refusal_basis")
    )
    if bool(
        visible_basis.get("visible_refusal_preserved")
        or visible_basis.get("refusal_preserved")
        or visible_basis.get("preserved")
    ):
        return True
    return _related_evidence_contains(
        related_evidence,
        ("blocked", "block", "refusal", "refused"),
    )


def _project_visible_divergence_preserved(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
) -> bool:
    if _hidden(request_or_result, basis, related_evidence, "divergence"):
        return False
    raw_basis = _raw_standing_basis_mapping(basis)
    if bool(basis.get("visible_divergence_preserved")):
        return True
    if bool(raw_basis.get("visible_divergence_preserved")):
        return True
    divergence = _raw_posture_mapping(request_or_result, basis, "divergence_posture")
    if bool(
        divergence.get("visible_divergence_preserved")
        or divergence.get("divergence_preserved")
        or divergence.get("preserved")
    ):
        return True
    visible_basis = _as_mapping(
        request_or_result.get("visible_divergence_basis")
        or raw_basis.get("visible_divergence_basis")
        or basis.get("visible_divergence_basis")
    )
    if bool(
        visible_basis.get("visible_divergence_preserved")
        or visible_basis.get("divergence_preserved")
        or visible_basis.get("preserved")
    ):
        return True
    return _related_evidence_contains(
        related_evidence,
        ("carrier_divergence_recorded", "divergence"),
    )


def _project_receipt_refusal_return_admission_preserved(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
) -> bool:
    raw_basis = _raw_standing_basis_mapping(basis)
    rra = _raw_posture_mapping(
        request_or_result,
        basis,
        "receipt_refusal_return_admission_posture",
    )
    if not rra:
        rra = _as_mapping(raw_basis.get("receipt_refusal_return_admission_posture"))
    if rra and not _false_flag(rra, ("preserved",)):
        if any(
            bool(rra.get(key))
            for key in (
                "carrier_c_returned_blocked_receipt_preserved",
                "return_did_not_create_admission",
                "admission_as_evidence_only",
                "receipt_preserved",
                "refusal_preserved",
                "return_preserved",
                "admission_preserved",
                "preserved",
            )
        ):
            return True
        if any(
            token in str(key).lower()
            and value is True
            for key, value in rra.items()
            for token in ("receipt", "refusal", "return", "admission")
        ):
            return True
    for field in ("receipt_posture", "refusal_posture", "return_posture", "admission_posture"):
        posture = _raw_posture_mapping(request_or_result, basis, field)
        if posture and not _false_flag(posture, ("preserved",)):
            return True
        processed = _as_mapping(basis.get(field))
        if processed.get("supplied") and processed.get("parseable"):
            return True
        direct = request_or_result.get(field)
        if direct is not None and isinstance(direct, (Mapping, str)):
            return True
    return False


def _project_divergence_posture_preserved(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
) -> bool:
    if _project_posture_preserved(request_or_result, basis, "divergence_posture"):
        return True
    return _project_visible_divergence_preserved(request_or_result, basis, related_evidence)


def _project_lifecycle_posture_preserved(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
) -> bool:
    if _project_posture_preserved(request_or_result, basis, "lifecycle_posture"):
        return True
    registry = _raw_posture_mapping(request_or_result, basis, "registry_persistence_posture")
    if bool(registry.get("lifecycle_reference_preserved")):
        return True
    return _related_evidence_contains(
        related_evidence,
        ("carrier_lifecycle_status_recorded", "lifecycle"),
    )


def _project_registry_persistence_posture_preserved(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
) -> bool:
    registry = _raw_posture_mapping(request_or_result, basis, "registry_persistence_posture")
    processed = _as_mapping(basis.get("registry_persistence_posture"))
    if processed.get("preserved"):
        return True
    if isinstance(registry, Mapping) and registry:
        if _false_flag(
            registry,
            (
                "registry_reference_is_not_standing",
                "persistence_is_not_currentness",
                "preserved",
            ),
        ):
            return False
        if bool(registry.get("lifecycle_reference_preserved")):
            return True
        return True
    if request_or_result.get("registry_persistence_posture") is not None:
        return True
    return _related_evidence_contains(
        related_evidence,
        ("carrier_registry_persistence_boundary_recorded", "registry_persistence"),
    )


def _project_posture_preserved(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
    field_name: str,
) -> bool:
    processed = _as_mapping(basis.get(field_name))
    if processed.get("preserved") is True:
        return True
    raw = _raw_posture_mapping(request_or_result, basis, field_name)
    if isinstance(raw, Mapping):
        return bool(raw) and not _false_flag(raw, ("preserved",))
    return raw is not None and _nonempty(raw)


def _visible_refusal_signal(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
) -> bool:
    return bool(
        basis.get("visible_refusal_available")
        or basis.get("visible_refusal_preserved")
        or _raw_standing_basis_mapping(basis).get("visible_refusal_preserved") is not None
        or _raw_posture_mapping(request_or_result, basis, "refusal_posture")
        or _raw_standing_basis_mapping(basis).get("receipt_refusal_return_admission_posture")
        or _related_evidence_contains(
            related_evidence,
            ("blocked", "block", "refusal", "refused"),
        )
        or _hidden(request_or_result, basis, related_evidence, "refusal")
    )


def _visible_divergence_signal(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
) -> bool:
    return bool(
        basis.get("visible_divergence_available")
        or basis.get("visible_divergence_preserved")
        or _raw_standing_basis_mapping(basis).get("visible_divergence_preserved") is not None
        or _raw_posture_mapping(request_or_result, basis, "divergence_posture")
        or _related_evidence_contains(
            related_evidence,
            ("carrier_divergence_recorded", "divergence"),
        )
        or _hidden(request_or_result, basis, related_evidence, "divergence")
    )


def _posture_basis(
    request: Mapping[str, Any],
    raw_basis: Mapping[str, Any],
    field_name: str,
) -> dict[str, Any]:
    raw = request.get(field_name)
    if raw is None:
        raw = raw_basis.get(field_name)
    supplied = raw is not None
    parseable = raw is None or isinstance(raw, (Mapping, str))
    preserved = supplied and parseable and not _false_flag(raw, ("preserved",))
    return {
        "supplied": supplied,
        "parseable": parseable,
        "preserved": preserved,
        "raw": copy.deepcopy(raw),
        "posture_remains_evidence": True,
        "posture_does_not_create_standing": True,
    }


def _direct_visible_posture(
    request: Mapping[str, Any],
    raw_basis: Mapping[str, Any],
    posture_name: str,
) -> dict[str, bool]:
    basis_key = f"visible_{posture_name}_basis"
    preserved_key = f"visible_{posture_name}_preserved"
    value = request.get(basis_key) or raw_basis.get(basis_key)
    available = value is not None or preserved_key in raw_basis
    hidden = _truthy_flag(
        value,
        (
            f"{posture_name}_hidden",
            f"hidden_{posture_name}",
            f"hides_{posture_name}",
            f"{posture_name}_erased",
        ),
    ) or _truthy_flag(
        raw_basis,
        (
            f"{posture_name}_hidden",
            f"hidden_{posture_name}",
            f"hides_{posture_name}",
            f"{posture_name}_erased",
        ),
    )
    if value is None:
        preserved = bool(raw_basis.get(preserved_key)) and not hidden
    elif isinstance(value, Mapping):
        preserved = (
            bool(
                value.get(preserved_key)
                or value.get(f"{posture_name}_preserved")
                or value.get("preserved")
                or raw_basis.get(preserved_key)
            )
            and not hidden
        )
    else:
        preserved = _nonempty(value) and not hidden
    return {"available": available, "preserved": preserved}


def _carrier_entries(value: Any, role: str) -> tuple[list[dict[str, Any]], bool]:
    raw_items: Sequence[Any]
    if isinstance(value, Mapping):
        raw_items = [value]
    elif isinstance(value, str):
        raw_items = [{"carrier_id": value}]
    elif isinstance(value, list):
        raw_items = value
    else:
        return [], False

    entries: list[dict[str, Any]] = []
    parseable = True
    for item in raw_items:
        if isinstance(item, str):
            entry = {"carrier_id": item}
        elif isinstance(item, Mapping):
            entry = copy.deepcopy(dict(item))
        else:
            parseable = False
            continue
        carrier_id = (
            entry.get("selected_carrier_id")
            or entry.get("carrier_id")
            or entry.get("carrier_identity")
            or entry.get(f"{role}_carrier_id")
            or entry.get("id")
        )
        entries.append(
            {
                "carrier_id": carrier_id,
                "carrier_role": entry.get("carrier_role") or role,
                "raw_carrier": entry,
            }
        )
    return entries, parseable


def _nested_or_direct(request: Mapping[str, Any], field_name: str) -> Any:
    if field_name in request:
        return request.get(field_name)
    raw_basis = _raw_standing_basis_mapping(request.get("standing_propagation_basis"))
    return raw_basis.get(field_name)


def _declared_block_code(request: Mapping[str, Any]) -> str | None:
    raw_block = request.get("block")
    if isinstance(raw_block, Mapping):
        block_code = raw_block.get("block_code") or raw_block.get("code")
    else:
        block_code = None
    return _normalize_token(
        request.get("standing_propagation_block_code")
        or request.get("declared_block_code")
        or request.get("block_code")
        or block_code
    )


def _required_non_claims_false(non_claims: Mapping[str, Any]) -> bool:
    if not isinstance(non_claims, Mapping):
        return False
    return all(non_claims.get(key) is False for key in REQUIRED_NON_CLAIMS)


def _collapse_check(
    check_name: str,
    sources: Sequence[Mapping[str, Any]],
    flag_keys: Sequence[str],
    expected_posture: str,
    block_code: str,
) -> dict[str, Any]:
    found = _first_true_flag(sources, flag_keys)
    return _check(
        check_name,
        found is None,
        expected_posture,
        found or {key: False for key in flag_keys},
        block_code,
    )


def _first_true_flag(
    sources: Sequence[Mapping[str, Any]],
    flag_keys: Sequence[str],
) -> dict[str, Any] | None:
    for source in sources:
        found = _find_true_flag(source, set(flag_keys))
        if found is not None:
            return found
    return None


def _find_true_flag(value: Any, flag_keys: set[str]) -> dict[str, Any] | None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in flag_keys and item is True:
                return {str(key): item}
            nested = _find_true_flag(item, flag_keys)
            if nested is not None:
                return nested
    elif isinstance(value, list):
        for item in value:
            nested = _find_true_flag(item, flag_keys)
            if nested is not None:
                return nested
    return None


def _truthy_flag(value: Any, flag_keys: Sequence[str]) -> bool:
    return _find_true_flag(value, set(flag_keys)) is not None


def _false_flag(value: Any, flag_keys: Sequence[str]) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in set(flag_keys) and item is False:
                return True
            if _false_flag(item, flag_keys):
                return True
    elif isinstance(value, list):
        return any(_false_flag(item, flag_keys) for item in value)
    return False


def _hidden(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
    posture_name: str,
) -> bool:
    keys = (
        f"{posture_name}_hidden",
        f"hidden_{posture_name}",
        f"hides_{posture_name}",
        f"standing_propagation_hid_{posture_name}",
        f"propagation_hides_{posture_name}",
    )
    return bool(
        _truthy_flag(request_or_result, keys)
        or _truthy_flag(basis, keys)
        or _truthy_flag(related_evidence, keys)
    )


def _without_safe_sections(request: Mapping[str, Any]) -> dict[str, Any]:
    safe_keys = {
        "propagation_non_meaning",
        "what_remains_open",
        "non_meaning",
        "open_items",
    }
    return {key: copy.deepcopy(value) for key, value in request.items() if key not in safe_keys}


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


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]


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
    return BLOCK_REASONS.get(block_code, f"Standing propagation blocked by {block_code}.")


def _result_id(
    question: Mapping[str, Any],
    posture: Mapping[str, Any],
    outcome: str,
) -> str:
    basis_id = (
        question.get("standing_propagation_request_id")
        or posture.get("requested_propagation_posture")
        or "standing_propagation"
    )
    return f"{_safe_filename_part(basis_id)}__{_safe_filename_part(outcome.lower())}"


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    return {key: non_claims.get(key) for key in REQUIRED_NON_CLAIMS}


def _raw_standing_basis_value(value: Any) -> Any:
    if isinstance(value, Mapping) and "raw_standing_propagation_basis" in value:
        return copy.deepcopy(value.get("raw_standing_propagation_basis"))
    return copy.deepcopy(value)


def _raw_standing_basis_mapping(value: Any) -> dict[str, Any]:
    return _as_mapping(_raw_standing_basis_value(value))


def _raw_posture_mapping(
    request_or_result: Mapping[str, Any],
    basis: Mapping[str, Any],
    field_name: str,
) -> dict[str, Any]:
    direct = request_or_result.get(field_name)
    if isinstance(direct, Mapping):
        return _as_mapping(direct)
    raw_basis = _raw_standing_basis_mapping(basis)
    raw_value = raw_basis.get(field_name)
    if isinstance(raw_value, Mapping):
        return _as_mapping(raw_value)
    processed = _as_mapping(basis.get(field_name))
    raw_processed = processed.get("raw")
    if isinstance(raw_processed, Mapping):
        return _as_mapping(raw_processed)
    return {}


def _posture_supplied(basis: Mapping[str, Any], field_name: str) -> bool:
    processed = _as_mapping(basis.get(field_name))
    if processed.get("supplied"):
        return True
    return _raw_standing_basis_mapping(basis).get(field_name) is not None


def _related_evidence_contains(
    related_evidence: Mapping[str, Any],
    tokens: Sequence[str],
) -> bool:
    normalized_tokens = tuple(token.lower() for token in tokens)
    entries = _mapping_list(related_evidence.get("related_carrier_evidence_entries"))
    raw_related = related_evidence.get("raw_related_carrier_evidence")
    if isinstance(raw_related, list):
        entries.extend(_mapping_list(raw_related))
    elif isinstance(raw_related, Mapping):
        entries.append(_as_mapping(raw_related))
    for entry in entries:
        if _entry_has_any_token(entry, normalized_tokens):
            return True
    for outcome in related_evidence.get("related_carrier_evidence_outcomes") or []:
        if _text_has_any_token(outcome, normalized_tokens):
            return True
    return False


def _entry_has_any_token(entry: Mapping[str, Any], tokens: Sequence[str]) -> bool:
    return _text_has_any_token(
        " ".join(
            str(value)
            for value in (
                entry.get("evidence_id"),
                entry.get("outcome"),
                entry.get("evidence_role"),
                entry.get("evidence_class"),
                entry.get("role"),
                entry.get("status"),
                entry.get("evidence_outcome"),
                entry.get("result_outcome"),
                entry.get("raw_evidence"),
            )
        ),
        tokens,
    )


def _text_has_any_token(value: Any, tokens: Sequence[str]) -> bool:
    text = str(value or "").lower()
    return any(token in text for token in tokens)


def _safe_filename_part(value: Any) -> str:
    raw = str(value or "standing_propagation").strip()
    cleaned = "".join(char if char.isalnum() or char in "._-" else "_" for char in raw)
    return cleaned.strip("._-") or "standing_propagation"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise StandingPropagationBoundaryV2Error(
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "Could not allocate a non-overwriting standing propagation v2 result path.",
    )


def _display_path(path: Path | None) -> str | None:
    if path is None:
        return None
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
