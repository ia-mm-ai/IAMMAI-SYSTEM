"""Bounded carrier lifecycle boundary resolver.

This resolver records what lifecycle status may be recorded for one carrier or
one carrier transition without collapse. It preserves lifecycle posture only.
It does not create carrier registry, persistence, currentness, authority,
permission, carrier hierarchy, distributed standing, repository
synchronization, full body transfer, continuation, distributed operation, or
evidence erasure.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CarrierLifecycleBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit lifecycle inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


REPO_ROOT = Path(__file__).resolve().parents[1]

CARRIER_LIFECYCLE_BOUNDARY_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_carrier_lifecycle_boundary"
)

RESOLVER_MODULE = "resolve_carrier_lifecycle_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "carrier_lifecycle_boundary_result"

RECORD_INTENT = "RECORD_CARRIER_LIFECYCLE_STATUS"
DO_NOT_RECORD_INTENT = "DO_NOT_RECORD_CARRIER_LIFECYCLE_STATUS"
BLOCK_INTENT = "BLOCK_CARRIER_LIFECYCLE_STATUS"
SUPPORTED_LIFECYCLE_INTENTS = {
    RECORD_INTENT,
    DO_NOT_RECORD_INTENT,
    BLOCK_INTENT,
}

CARRIER_LIFECYCLE_STATUS_RECORDED = "CARRIER_LIFECYCLE_STATUS_RECORDED"
CARRIER_LIFECYCLE_STATUS_NOT_RECORDED = "CARRIER_LIFECYCLE_STATUS_NOT_RECORDED"
CARRIER_LIFECYCLE_STATUS_BLOCKED = "CARRIER_LIFECYCLE_STATUS_BLOCKED"

SUPPORTED_LIFECYCLE_STATUSES = {
    "CARRIER_CANDIDATE",
    "CARRIER_DECLARED_FOR_EXPERIMENT",
    "CARRIER_ACTIVE_FOR_OPERATION",
    "CARRIER_HOLDING_EVIDENCE",
    "CARRIER_RETURNED_EVIDENCE",
    "CARRIER_REFUSED_OR_BLOCKED",
    "CARRIER_UNAVAILABLE",
    "CARRIER_STALE",
    "CARRIER_CORRUPTED",
    "CARRIER_WITHDRAWN",
    "CARRIER_REPLACED",
    "CARRIER_REINTRODUCTION_CANDIDATE",
    "CARRIER_REINTRODUCED",
    "CARRIER_RETIRED",
    "CARRIER_LIFECYCLE_BLOCKED",
}

SUPPORTED_EXPLICIT_TRANSITIONS = {
    ("CARRIER_CANDIDATE", "CARRIER_DECLARED_FOR_EXPERIMENT"),
    ("CARRIER_DECLARED_FOR_EXPERIMENT", "CARRIER_ACTIVE_FOR_OPERATION"),
    ("CARRIER_ACTIVE_FOR_OPERATION", "CARRIER_RETURNED_EVIDENCE"),
    ("CARRIER_ACTIVE_FOR_OPERATION", "CARRIER_REFUSED_OR_BLOCKED"),
    ("CARRIER_ACTIVE_FOR_OPERATION", "CARRIER_UNAVAILABLE"),
    ("CARRIER_HOLDING_EVIDENCE", "CARRIER_STALE"),
    ("CARRIER_HOLDING_EVIDENCE", "CARRIER_CORRUPTED"),
    ("CARRIER_STALE", "CARRIER_REINTRODUCTION_CANDIDATE"),
    ("CARRIER_UNAVAILABLE", "CARRIER_REINTRODUCTION_CANDIDATE"),
    ("CARRIER_WITHDRAWN", "CARRIER_REINTRODUCTION_CANDIDATE"),
    ("CARRIER_REINTRODUCTION_CANDIDATE", "CARRIER_REINTRODUCED"),
}

WITHDRAWABLE_STATUSES = {
    "CARRIER_CANDIDATE",
    "CARRIER_DECLARED_FOR_EXPERIMENT",
    "CARRIER_ACTIVE_FOR_OPERATION",
    "CARRIER_REINTRODUCTION_CANDIDATE",
    "CARRIER_REINTRODUCED",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "carrier_lifecycle_created_source": False,
    "carrier_lifecycle_created_currentness": False,
    "carrier_lifecycle_created_authority": False,
    "carrier_lifecycle_created_permission": False,
    "carrier_lifecycle_created_hierarchy": False,
    "carrier_lifecycle_created_distributed_standing": False,
    "carrier_lifecycle_created_registry": False,
    "carrier_lifecycle_authorized_sync": False,
    "carrier_lifecycle_authorized_full_body_transfer": False,
    "carrier_lifecycle_authorized_continuation": False,
    "carrier_lifecycle_authorized_distributed_operation": False,
    "carrier_lifecycle_erased_evidence": False,
    "carrier_lifecycle_hid_refusal": False,
    "carrier_lifecycle_hid_divergence": False,
    "carrier_lifecycle_hid_corruption": False,
    "carrier_lifecycle_repaired_by_overwrite": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "distributed_standing_created": False,
    "carrier_registry_created": False,
    "repository_synchronization_authorized": False,
    "full_body_transfer_authorized": False,
    "second_body_created": False,
    "continuation_authorized": False,
    "distributed_operation_authorized": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "DECLARED_LIFECYCLE_REQUEST_UNREADABLE": "Declared lifecycle request path could not be read.",
    "DECLARED_LIFECYCLE_REQUEST_MALFORMED": "Declared lifecycle request is not a JSON object or mapping.",
    "LIFECYCLE_QUESTION_UNDECLARED": "Lifecycle question is undeclared.",
    "LIFECYCLE_INTENT_UNSUPPORTED": "Lifecycle intent is unsupported.",
    "LIFECYCLE_REQUEST_EXPLICITLY_BLOCKED": "Lifecycle request explicitly declares a blocked posture.",
    "CARRIER_IDENTITY_MISSING": "Carrier identity is missing.",
    "LIFECYCLE_STATUS_UNSUPPORTED": "Requested or prior lifecycle status is unsupported.",
    "LIFECYCLE_BASIS_MISSING": "Lifecycle basis is missing.",
    "LIFECYCLE_TRANSITION_BASIS_MISSING": "Lifecycle transition basis is missing.",
    "LIFECYCLE_TRANSITION_UNSUPPORTED": "Lifecycle transition is unsupported.",
    "RELATED_EVIDENCE_MALFORMED": "Related carrier evidence is malformed.",
    "LIFECYCLE_ERASES_EVIDENCE": "Lifecycle erases prior evidence.",
    "LIFECYCLE_HIDES_REFUSAL": "Lifecycle hides refusal.",
    "LIFECYCLE_HIDES_DIVERGENCE": "Lifecycle hides divergence or mismatch.",
    "LIFECYCLE_HIDES_CORRUPTION": "Lifecycle hides corruption.",
    "LIFECYCLE_REPAIRS_BY_OVERWRITE": "Lifecycle repairs by overwrite.",
    "LIFECYCLE_REPLACES_SOURCE": "Lifecycle replaces source.",
    "LIFECYCLE_CREATES_CURRENTNESS": "Lifecycle creates currentness.",
    "LIFECYCLE_CREATES_AUTHORITY": "Lifecycle creates authority.",
    "LIFECYCLE_CREATES_PERMISSION": "Lifecycle creates permission.",
    "LIFECYCLE_CREATES_CARRIER_HIERARCHY": "Lifecycle creates carrier hierarchy.",
    "LIFECYCLE_SELECTS_WINNING_CARRIER": "Lifecycle selects a winning carrier.",
    "LIFECYCLE_INVALIDATES_LOSING_CARRIER": "Lifecycle invalidates a losing carrier.",
    "LIFECYCLE_CREATES_DISTRIBUTED_STANDING": "Lifecycle creates distributed standing.",
    "LIFECYCLE_AUTHORIZES_REPOSITORY_SYNC": "Lifecycle authorizes repository synchronization.",
    "LIFECYCLE_AUTHORIZES_FULL_BODY_TRANSFER": "Lifecycle authorizes full body transfer.",
    "LIFECYCLE_CREATES_CARRIER_REGISTRY": "Lifecycle creates carrier registry.",
    "LIFECYCLE_AUTHORIZES_CONTINUATION": "Lifecycle authorizes continuation.",
    "LIFECYCLE_AUTHORIZES_DISTRIBUTED_OPERATION": "Lifecycle authorizes distributed operation.",
    "LATEST_FILE_CURRENTNESS": "Latest-file recency is treated as currentness.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge was detected.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required lifecycle non-claim is missing or flipped.",
}

LIFECYCLE_NON_MEANING = {
    "does_not_mean_source_replacement": True,
    "does_not_mean_currentness": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission_beyond_declared_lifecycle_review": True,
    "does_not_mean_carrier_hierarchy": True,
    "does_not_mean_carrier_priority": True,
    "does_not_mean_carrier_sovereignty": True,
    "does_not_mean_carrier_correctness": True,
    "does_not_mean_winning_carrier": True,
    "does_not_mean_losing_carrier_invalidated": True,
    "does_not_mean_evidence_erased": True,
    "does_not_mean_refusal_erased": True,
    "does_not_mean_divergence_resolved": True,
    "does_not_mean_distributed_standing": True,
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
}

WHAT_REMAINS_OPEN = {
    "carrier_lifecycle_implementation_refinement": True,
    "carrier_registry_persistence_boundary": True,
    "standing_propagation_law": True,
    "cross_carrier_currentness_successor_law": True,
    "divergence_consequence_law": True,
    "distributed_standing_boundary": True,
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


def resolve_carrier_lifecycle_boundary(
    declared_lifecycle_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded carrier lifecycle status request."""

    if declared_lifecycle_request is None:
        return _resolve_lifecycle({}, None, [])
    if not isinstance(declared_lifecycle_request, Mapping):
        return _resolve_lifecycle({}, None, ["DECLARED_LIFECYCLE_REQUEST_MALFORMED"])
    return _resolve_lifecycle(copy.deepcopy(dict(declared_lifecycle_request)), None, [])


def resolve_carrier_lifecycle_boundary_from_path(
    declared_lifecycle_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one bounded carrier lifecycle status request from JSON."""

    path = Path(declared_lifecycle_request_path)
    try:
        request = _read_json_mapping(path)
    except CarrierLifecycleBoundaryError as exc:
        return _resolve_lifecycle({}, path, [exc.block_code])
    return _resolve_lifecycle(request, path, [])


def write_carrier_lifecycle_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an additive carrier lifecycle result without overwriting."""

    if not isinstance(result, Mapping):
        raise CarrierLifecycleBoundaryError(
            "DECLARED_LIFECYCLE_REQUEST_MALFORMED",
            "Carrier lifecycle result must be a mapping.",
        )

    if output_path is None:
        summary = _as_mapping(result.get("carrier_lifecycle_summary"))
        basis_id = (
            summary.get("lifecycle_request_id")
            or summary.get("selected_carrier_id")
            or "carrier_lifecycle"
        )
        output_path = CARRIER_LIFECYCLE_BOUNDARY_ROOT / (
            f"{_safe_filename_part(basis_id)}__carrier_lifecycle_result.json"
        )

    target = _non_overwriting_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, ensure_ascii=False, default=str)
        + "\n",
        encoding="utf-8",
    )
    return target


def build_carrier_lifecycle_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact summary for a carrier lifecycle result."""

    checks = _mapping_list(result.get("lifecycle_checks"))
    question = _as_mapping(result.get("declared_lifecycle_question"))
    selected = _as_mapping(result.get("selected_carrier"))
    prior = _as_mapping(result.get("prior_lifecycle_status"))
    requested = _as_mapping(result.get("requested_lifecycle_status"))
    basis = _as_mapping(result.get("lifecycle_basis"))
    evidence = _as_mapping(result.get("related_carrier_evidence"))
    transition = _as_mapping(result.get("lifecycle_transition"))
    statement = _as_mapping(result.get("lifecycle_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "lifecycle_request_id": question.get("lifecycle_request_id"),
        "lifecycle_question": question.get("lifecycle_question"),
        "lifecycle_intent": question.get("lifecycle_intent"),
        "selected_carrier_id": selected.get("selected_carrier_id"),
        "prior_lifecycle_status": prior.get("prior_lifecycle_status"),
        "requested_lifecycle_status": requested.get("requested_lifecycle_status"),
        "lifecycle_basis": basis.get("raw_lifecycle_basis"),
        "transition_basis": transition.get("transition_basis"),
        "related_evidence_ids": evidence.get("related_evidence_ids"),
        "related_evidence_outcomes": evidence.get("related_evidence_outcomes"),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "lifecycle_status_recorded": bool(statement.get("carrier_lifecycle_status_recorded")),
        "prior_evidence_erased": bool(statement.get("prior_evidence_erased")),
        "visible_refusal_preserved": bool(statement.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(statement.get("visible_divergence_preserved")),
        "visible_corruption_preserved": bool(statement.get("visible_corruption_preserved")),
        "visible_staleness_preserved": bool(statement.get("visible_staleness_preserved")),
        "no_source_currentness_authority_permission": not bool(
            statement.get("source_replaced")
            or statement.get("currentness_created")
            or statement.get("authority_created")
            or statement.get("permission_created")
        ),
        "no_carrier_hierarchy": not bool(statement.get("carrier_hierarchy_created")),
        "no_winning_losing_carrier_collapse": not bool(
            statement.get("winning_carrier_selected")
            or statement.get("losing_carrier_invalidated")
        ),
        "no_distributed_standing": not bool(statement.get("distributed_standing_created")),
        "no_registry_sync_full_body_transfer": not bool(
            statement.get("carrier_registry_created")
            or statement.get("repository_synchronization_authorized")
            or statement.get("full_body_transfer_authorized")
        ),
        "no_continuation": not bool(statement.get("continuation_authorized")),
        "no_distributed_operation": not bool(statement.get("distributed_operation_authorized")),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_declared_carrier_lifecycle_request(
    lifecycle_request_id: str,
    lifecycle_question: str,
    carrier_id: str,
    requested_lifecycle_status: str,
    lifecycle_basis: Mapping[str, Any] | str,
    lifecycle_intent: str = RECORD_INTENT,
    *,
    prior_lifecycle_status: str | None = None,
    transition_basis: Mapping[str, Any] | str | None = None,
    related_carrier_evidence: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Build one bounded lifecycle request without inferring force."""

    request: dict[str, Any] = {
        "lifecycle_request_id": lifecycle_request_id,
        "lifecycle_question": lifecycle_question,
        "lifecycle_intent": lifecycle_intent,
        "selected_carrier": {
            "carrier_id": carrier_id,
            "carrier_identity_preserved": True,
            "lifecycle_participant_not_body_participant": True,
        },
        "requested_lifecycle_status": requested_lifecycle_status,
        "lifecycle_basis": copy.deepcopy(lifecycle_basis),
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }
    if prior_lifecycle_status is not None:
        request["prior_lifecycle_status"] = prior_lifecycle_status
    if transition_basis is not None:
        request["transition_basis"] = copy.deepcopy(transition_basis)
        request["lifecycle_transition"] = {
            "prior_lifecycle_status": prior_lifecycle_status,
            "requested_lifecycle_status": requested_lifecycle_status,
            "transition_basis": copy.deepcopy(transition_basis),
        }
    if related_carrier_evidence is not None:
        request["related_carrier_evidence"] = [
            copy.deepcopy(dict(item)) for item in related_carrier_evidence
        ]
    return request


def _resolve_lifecycle(
    request: Mapping[str, Any],
    request_path: Path | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    normalized_request = _as_mapping(request)
    question = _declared_lifecycle_question(normalized_request, request_path)
    selected_carrier = _selected_carrier(normalized_request)
    prior_status = _prior_lifecycle_status(normalized_request)
    requested_status = _requested_lifecycle_status(normalized_request)
    basis = _lifecycle_basis(normalized_request)
    related_evidence = _related_carrier_evidence(normalized_request)
    transition = _lifecycle_transition(
        normalized_request,
        prior_status,
        requested_status,
    )
    checks = _build_checks(
        normalized_request,
        question,
        selected_carrier,
        prior_status,
        requested_status,
        basis,
        related_evidence,
        transition,
        precheck_failures,
    )
    failed_checks = [check for check in checks if check.get("passed") is False]
    intent = question.get("lifecycle_intent")
    explicit_block_code = _declared_block_code(normalized_request)

    if failed_checks:
        outcome = CARRIER_LIFECYCLE_STATUS_BLOCKED
        block_code = str(failed_checks[0].get("block_code") or "NON_CLAIM_MISSING_OR_FLIPPED")
    elif intent == BLOCK_INTENT:
        outcome = CARRIER_LIFECYCLE_STATUS_BLOCKED
        block_code = explicit_block_code or "LIFECYCLE_REQUEST_EXPLICITLY_BLOCKED"
    elif intent == DO_NOT_RECORD_INTENT:
        outcome = CARRIER_LIFECYCLE_STATUS_NOT_RECORDED
        block_code = None
    else:
        outcome = CARRIER_LIFECYCLE_STATUS_RECORDED
        block_code = None

    block_reason = _block_reason(block_code)
    result: dict[str, Any] = {
        "carrier_lifecycle_metadata": {
            "carrier_lifecycle_result_id": _result_id(question, selected_carrier, outcome),
            "carrier_lifecycle_result_type": RESULT_TYPE,
            "carrier_lifecycle_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_lifecycle_question": question,
        "selected_carrier": selected_carrier,
        "prior_lifecycle_status": prior_status,
        "requested_lifecycle_status": requested_status,
        "lifecycle_basis": basis,
        "related_carrier_evidence": related_evidence,
        "lifecycle_transition": transition,
        "lifecycle_checks": checks,
        "lifecycle_statement": _lifecycle_statement(
            outcome,
            question,
            selected_carrier,
            prior_status,
            requested_status,
            basis,
            related_evidence,
            transition,
            checks,
            block_code,
            block_reason,
        ),
        "lifecycle_non_meaning": copy.deepcopy(LIFECYCLE_NON_MEANING),
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
    result["carrier_lifecycle_summary"] = build_carrier_lifecycle_summary(result)
    return result


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    artifact_path = Path(path)
    try:
        loaded = json.loads(artifact_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise CarrierLifecycleBoundaryError(
            "DECLARED_LIFECYCLE_REQUEST_UNREADABLE",
            BLOCK_REASONS["DECLARED_LIFECYCLE_REQUEST_UNREADABLE"],
        ) from exc
    except json.JSONDecodeError as exc:
        raise CarrierLifecycleBoundaryError(
            "DECLARED_LIFECYCLE_REQUEST_MALFORMED",
            BLOCK_REASONS["DECLARED_LIFECYCLE_REQUEST_MALFORMED"],
        ) from exc
    if not isinstance(loaded, Mapping):
        raise CarrierLifecycleBoundaryError(
            "DECLARED_LIFECYCLE_REQUEST_MALFORMED",
            BLOCK_REASONS["DECLARED_LIFECYCLE_REQUEST_MALFORMED"],
        )
    return copy.deepcopy(dict(loaded))


def _declared_lifecycle_question(
    request: Mapping[str, Any],
    request_path: Path | None,
) -> dict[str, Any]:
    return {
        "lifecycle_request_id": request.get("lifecycle_request_id"),
        "lifecycle_request_path": _display_path(request_path)
        if request_path
        else request.get("_lifecycle_request_path"),
        "lifecycle_question": request.get("lifecycle_question"),
        "lifecycle_intent": _normalize_token(request.get("lifecycle_intent")),
        "not_recorded_reason": request.get("not_recorded_reason"),
        "operator_note": request.get("operator_note"),
        "selected_experiment_basis": copy.deepcopy(request.get("selected_experiment_basis")),
        "selected_relation_basis": copy.deepcopy(request.get("selected_relation_basis")),
        "selected_currentness_basis": copy.deepcopy(request.get("selected_currentness_basis")),
        "selected_admission_basis": copy.deepcopy(request.get("selected_admission_basis")),
        "declared_non_claims": copy.deepcopy(
            request.get("declared_non_claims") or request.get("non_claims")
        ),
        "records_one_carrier_lifecycle_question": True,
        "lifecycle_is_not_registry": True,
        "lifecycle_is_not_currentness": True,
        "lifecycle_is_not_distributed_standing": True,
        "lifecycle_does_not_authorize_continuation": True,
        "lifecycle_does_not_authorize_distributed_operation": True,
    }


def _selected_carrier(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("selected_carrier")
    if isinstance(raw, Mapping):
        carrier = copy.deepcopy(dict(raw))
        carrier_id = (
            carrier.get("selected_carrier_id")
            or carrier.get("carrier_id")
            or carrier.get("carrier_identity")
            or carrier.get("id")
        )
    else:
        carrier = raw
        carrier_id = raw if isinstance(raw, str) else None
    return {
        "selected_carrier_declared": raw is not None,
        "selected_carrier_id": carrier_id,
        "carrier_identity_declared": _nonempty(carrier_id),
        "carrier_identity_preserved": _nonempty(carrier_id),
        "lifecycle_participant_not_body_participant": True,
        "lifecycle_status_does_not_make_carrier_current": True,
        "lifecycle_status_does_not_create_carrier_hierarchy": True,
        "raw_selected_carrier": copy.deepcopy(carrier),
    }


def _prior_lifecycle_status(request: Mapping[str, Any]) -> dict[str, Any]:
    status = _status_value(request.get("prior_lifecycle_status"))
    return {
        "prior_lifecycle_status_supplied": status is not None,
        "prior_lifecycle_status": status,
        "prior_lifecycle_status_supported_where_supplied": status is None
        or status in SUPPORTED_LIFECYCLE_STATUSES,
        "prior_lifecycle_status_preserved": status is not None,
        "raw_prior_lifecycle_status": copy.deepcopy(request.get("prior_lifecycle_status")),
    }


def _requested_lifecycle_status(request: Mapping[str, Any]) -> dict[str, Any]:
    status = _status_value(request.get("requested_lifecycle_status"))
    return {
        "requested_lifecycle_status_declared": status is not None,
        "requested_lifecycle_status": status,
        "requested_lifecycle_status_supported": status in SUPPORTED_LIFECYCLE_STATUSES,
        "requested_lifecycle_status_preserved": status is not None,
        "raw_requested_lifecycle_status": copy.deepcopy(request.get("requested_lifecycle_status")),
    }


def _lifecycle_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    raw_basis = request.get("lifecycle_basis")
    visible_refusal = _visible_basis_posture(request.get("visible_refusal_basis"), "refusal")
    visible_divergence = _visible_basis_posture(
        request.get("visible_divergence_basis"),
        "divergence",
    )
    visible_corruption = _visible_basis_posture(
        request.get("visible_corruption_basis"),
        "corruption",
    )
    visible_staleness = _visible_basis_posture(
        request.get("visible_staleness_basis"),
        "staleness",
    )
    return {
        "lifecycle_basis_declared": _basis_declared(raw_basis),
        "lifecycle_basis_preserved": _basis_declared(raw_basis),
        "raw_lifecycle_basis": copy.deepcopy(raw_basis),
        "selected_experiment_basis": copy.deepcopy(request.get("selected_experiment_basis")),
        "selected_relation_basis": copy.deepcopy(request.get("selected_relation_basis")),
        "selected_currentness_basis": copy.deepcopy(request.get("selected_currentness_basis")),
        "selected_admission_basis": copy.deepcopy(request.get("selected_admission_basis")),
        "visible_refusal_available": visible_refusal["available"],
        "visible_refusal_preserved": visible_refusal["preserved"],
        "visible_refusal_basis": copy.deepcopy(request.get("visible_refusal_basis")),
        "visible_divergence_available": visible_divergence["available"],
        "visible_divergence_preserved": visible_divergence["preserved"],
        "visible_divergence_basis": copy.deepcopy(request.get("visible_divergence_basis")),
        "visible_corruption_available": visible_corruption["available"],
        "visible_corruption_preserved": visible_corruption["preserved"],
        "visible_corruption_basis": copy.deepcopy(request.get("visible_corruption_basis")),
        "visible_staleness_available": visible_staleness["available"],
        "visible_staleness_preserved": visible_staleness["preserved"],
        "visible_staleness_basis": copy.deepcopy(request.get("visible_staleness_basis")),
        "lifecycle_preserves_prior_evidence": True,
        "lifecycle_does_not_create_source_currentness_authority_permission": True,
        "lifecycle_does_not_create_distributed_standing": True,
        "lifecycle_does_not_authorize_continuation": True,
    }


def _related_carrier_evidence(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("related_carrier_evidence")
    if raw is None:
        return {
            "related_evidence_supplied": False,
            "related_evidence_parseable": True,
            "related_evidence_entries": [],
            "related_evidence_ids": [],
            "related_evidence_outcomes": [],
            "related_evidence_preserved": False,
            "raw_related_carrier_evidence": None,
        }
    entries: list[dict[str, Any]] = []
    parseable = True
    raw_items: list[Any]
    if isinstance(raw, Mapping):
        raw_items = [raw]
    elif isinstance(raw, Sequence) and not isinstance(raw, (str, bytes, bytearray)):
        raw_items = list(raw)
    else:
        raw_items = [raw]
        parseable = False

    for item in raw_items:
        if not isinstance(item, Mapping):
            parseable = False
            continue
        evidence = copy.deepcopy(dict(item))
        evidence_id = (
            evidence.get("evidence_id")
            or evidence.get("related_evidence_id")
            or evidence.get("carrier_evidence_id")
            or evidence.get("result_id")
            or evidence.get("id")
        )
        outcome = (
            evidence.get("outcome")
            or evidence.get("status")
            or evidence.get("evidence_outcome")
            or evidence.get("evidence_status")
        )
        entries.append(
            {
                "evidence_id": evidence_id,
                "evidence_outcome_or_status": outcome,
                "carrier_id": evidence.get("carrier_id") or evidence.get("selected_carrier_id"),
                "basis": copy.deepcopy(evidence.get("basis") or evidence.get("evidence_basis")),
                "raw_evidence": evidence,
            }
        )

    return {
        "related_evidence_supplied": True,
        "related_evidence_parseable": parseable,
        "related_evidence_entries": entries,
        "related_evidence_ids": [entry.get("evidence_id") for entry in entries],
        "related_evidence_outcomes": [
            entry.get("evidence_outcome_or_status") for entry in entries
        ],
        "related_evidence_preserved": bool(entries),
        "raw_related_carrier_evidence": copy.deepcopy(raw),
    }


def _lifecycle_transition(
    request: Mapping[str, Any],
    prior_status: Mapping[str, Any],
    requested_status: Mapping[str, Any],
) -> dict[str, Any]:
    transition_request = _as_mapping(request.get("lifecycle_transition"))
    prior = (
        _status_value(transition_request.get("prior_lifecycle_status"))
        or prior_status.get("prior_lifecycle_status")
    )
    requested = (
        _status_value(transition_request.get("requested_lifecycle_status"))
        or requested_status.get("requested_lifecycle_status")
    )
    transition_basis = (
        request.get("transition_basis")
        if request.get("transition_basis") is not None
        else transition_request.get("transition_basis") or transition_request.get("basis")
    )
    transition_requested = bool(prior and requested and prior != requested)
    transition_basis_declared = _basis_declared(transition_basis)
    supported = (
        not transition_requested
        or (
            transition_basis_declared
            and _transition_supported(str(prior), str(requested))
        )
    )
    return {
        "transition_requested": transition_requested,
        "prior_lifecycle_status": prior,
        "requested_lifecycle_status": requested,
        "transition_basis": copy.deepcopy(transition_basis),
        "transition_basis_preserved": transition_basis_declared,
        "transition_supported": supported,
        "transition_preserves_previous_status": True,
        "transition_preserves_new_status": bool(requested),
        "transition_preserves_affected_evidence": True,
        "transition_is_not_registry": True,
        "transition_does_not_create_source_currentness_authority_permission": True,
        "transition_does_not_erase_evidence": True,
        "transition_does_not_create_distributed_standing": True,
        "raw_lifecycle_transition": copy.deepcopy(request.get("lifecycle_transition")),
    }


def _build_checks(
    request: Mapping[str, Any],
    question: Mapping[str, Any],
    selected_carrier: Mapping[str, Any],
    prior_status: Mapping[str, Any],
    requested_status: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
    transition: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    collapse_source = _without_safe_sections(request)
    declared_non_claims = _as_mapping(
        request.get("declared_non_claims") or request.get("non_claims")
    )
    sources = [
        collapse_source,
        question,
        selected_carrier,
        prior_status,
        requested_status,
        basis,
        related_evidence,
        transition,
        declared_non_claims,
    ]
    precheck_code = precheck_failures[0] if precheck_failures else None
    transition_requested = bool(transition.get("transition_requested"))
    checks = [
        _check(
            "declared_lifecycle_request_parseable_mapping",
            not precheck_failures,
            "declared lifecycle request is a parseable mapping",
            list(precheck_failures),
            precheck_code or "DECLARED_LIFECYCLE_REQUEST_MALFORMED",
        ),
        _check(
            "lifecycle_question_declared",
            _nonempty(question.get("lifecycle_question")),
            "lifecycle question is declared",
            question.get("lifecycle_question"),
            "LIFECYCLE_QUESTION_UNDECLARED",
        ),
        _check(
            "lifecycle_intent_supported",
            question.get("lifecycle_intent") in SUPPORTED_LIFECYCLE_INTENTS,
            "lifecycle intent is supported",
            question.get("lifecycle_intent"),
            "LIFECYCLE_INTENT_UNSUPPORTED",
        ),
        _check(
            "carrier_identity_declared",
            bool(selected_carrier.get("carrier_identity_declared")),
            "selected carrier identity is declared",
            selected_carrier.get("selected_carrier_id"),
            "CARRIER_IDENTITY_MISSING",
        ),
        _check(
            "requested_lifecycle_status_declared",
            bool(requested_status.get("requested_lifecycle_status_declared")),
            "requested lifecycle status is declared",
            requested_status.get("requested_lifecycle_status"),
            "LIFECYCLE_STATUS_UNSUPPORTED",
        ),
        _check(
            "requested_lifecycle_status_supported",
            bool(requested_status.get("requested_lifecycle_status_supported")),
            "requested lifecycle status is supported",
            requested_status.get("requested_lifecycle_status"),
            "LIFECYCLE_STATUS_UNSUPPORTED",
        ),
        _check(
            "prior_lifecycle_status_supported_where_supplied",
            bool(prior_status.get("prior_lifecycle_status_supported_where_supplied")),
            "prior lifecycle status is supported where supplied",
            prior_status.get("prior_lifecycle_status"),
            "LIFECYCLE_STATUS_UNSUPPORTED",
        ),
        _check(
            "lifecycle_basis_declared",
            bool(basis.get("lifecycle_basis_declared")),
            "lifecycle basis is declared",
            basis.get("raw_lifecycle_basis"),
            "LIFECYCLE_BASIS_MISSING",
        ),
        _check(
            "related_evidence_parseable_where_supplied",
            bool(related_evidence.get("related_evidence_parseable")),
            "related carrier evidence is parseable where supplied",
            _shape(related_evidence.get("raw_related_carrier_evidence")),
            "RELATED_EVIDENCE_MALFORMED",
        ),
        _check(
            "transition_basis_supplied_where_required",
            not transition_requested or bool(transition.get("transition_basis_preserved")),
            "transition basis is supplied where prior status changes",
            transition.get("transition_basis"),
            "LIFECYCLE_TRANSITION_BASIS_MISSING",
        ),
        _check(
            "transition_supported_where_applicable",
            bool(transition.get("transition_supported")),
            "transition is supported where applicable",
            {
                "prior_lifecycle_status": transition.get("prior_lifecycle_status"),
                "requested_lifecycle_status": transition.get("requested_lifecycle_status"),
            },
            "LIFECYCLE_TRANSITION_UNSUPPORTED",
        ),
        _collapse_check(
            "prior_evidence_preserved",
            sources,
            (
                "prior_evidence_erased",
                "evidence_erased",
                "evidence_overwritten",
                "carrier_lifecycle_erased_evidence",
                "lifecycle_erases_evidence",
            ),
            "prior evidence is preserved",
            "LIFECYCLE_ERASES_EVIDENCE",
        ),
        _check(
            "visible_refusal_preserved_where_applicable",
            not basis.get("visible_refusal_available")
            or bool(basis.get("visible_refusal_preserved")),
            "visible refusal remains visible where applicable",
            {
                "visible_refusal_available": basis.get("visible_refusal_available"),
                "visible_refusal_preserved": basis.get("visible_refusal_preserved"),
            },
            "LIFECYCLE_HIDES_REFUSAL",
        ),
        _check(
            "visible_divergence_preserved_where_applicable",
            not basis.get("visible_divergence_available")
            or bool(basis.get("visible_divergence_preserved")),
            "visible divergence remains visible where applicable",
            {
                "visible_divergence_available": basis.get("visible_divergence_available"),
                "visible_divergence_preserved": basis.get("visible_divergence_preserved"),
            },
            "LIFECYCLE_HIDES_DIVERGENCE",
        ),
        _check(
            "visible_corruption_preserved_where_applicable",
            not basis.get("visible_corruption_available")
            or bool(basis.get("visible_corruption_preserved")),
            "visible corruption remains visible where applicable",
            {
                "visible_corruption_available": basis.get("visible_corruption_available"),
                "visible_corruption_preserved": basis.get("visible_corruption_preserved"),
            },
            "LIFECYCLE_HIDES_CORRUPTION",
        ),
        _check(
            "visible_staleness_preserved_where_applicable",
            not basis.get("visible_staleness_available")
            or bool(basis.get("visible_staleness_preserved")),
            "visible staleness remains visible where applicable",
            {
                "visible_staleness_available": basis.get("visible_staleness_available"),
                "visible_staleness_preserved": basis.get("visible_staleness_preserved"),
            },
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _collapse_check(
            "no_evidence_erased",
            sources,
            (
                "prior_evidence_erased",
                "evidence_erased",
                "evidence_overwritten",
                "carrier_lifecycle_erased_evidence",
                "lifecycle_erases_evidence",
            ),
            "lifecycle does not erase evidence",
            "LIFECYCLE_ERASES_EVIDENCE",
        ),
        _collapse_check(
            "no_refusal_hidden",
            sources,
            (
                "refusal_hidden",
                "hidden_refusal",
                "carrier_lifecycle_hid_refusal",
                "lifecycle_hides_refusal",
            ),
            "lifecycle does not hide refusal",
            "LIFECYCLE_HIDES_REFUSAL",
        ),
        _collapse_check(
            "no_divergence_hidden",
            sources,
            (
                "divergence_hidden",
                "mismatch_hidden",
                "hidden_divergence",
                "hidden_mismatch",
                "carrier_lifecycle_hid_divergence",
                "lifecycle_hides_divergence",
            ),
            "lifecycle does not hide divergence",
            "LIFECYCLE_HIDES_DIVERGENCE",
        ),
        _collapse_check(
            "no_corruption_hidden",
            sources,
            (
                "corruption_hidden",
                "hidden_corruption",
                "carrier_lifecycle_hid_corruption",
                "lifecycle_hides_corruption",
            ),
            "lifecycle does not hide corruption",
            "LIFECYCLE_HIDES_CORRUPTION",
        ),
        _collapse_check(
            "no_repair_by_overwrite",
            sources,
            (
                "repair_by_overwrite",
                "repaired_by_overwrite",
                "carrier_lifecycle_repaired_by_overwrite",
                "lifecycle_repairs_by_overwrite",
            ),
            "lifecycle does not repair by overwrite",
            "LIFECYCLE_REPAIRS_BY_OVERWRITE",
        ),
        _collapse_check(
            "no_source_replacement",
            sources,
            (
                "source_replaced",
                "carrier_lifecycle_created_source",
                "lifecycle_replaces_source",
                "carrier_became_source",
            ),
            "lifecycle does not replace source",
            "LIFECYCLE_REPLACES_SOURCE",
        ),
        _collapse_check(
            "no_currentness",
            sources,
            (
                "currentness_created",
                "carrier_lifecycle_created_currentness",
                "current_carrier_selected",
                "carrier_became_current",
                "lifecycle_creates_currentness",
            ),
            "lifecycle does not create currentness",
            "LIFECYCLE_CREATES_CURRENTNESS",
        ),
        _collapse_check(
            "no_authority",
            sources,
            (
                "authority_created",
                "carrier_lifecycle_created_authority",
                "carrier_became_authority",
                "lifecycle_creates_authority",
            ),
            "lifecycle does not create authority",
            "LIFECYCLE_CREATES_AUTHORITY",
        ),
        _collapse_check(
            "no_permission",
            sources,
            (
                "permission_created",
                "carrier_lifecycle_created_permission",
                "permission_beyond_declared_lifecycle_review_created",
                "lifecycle_creates_permission",
            ),
            "lifecycle does not create permission",
            "LIFECYCLE_CREATES_PERMISSION",
        ),
        _collapse_check(
            "no_carrier_hierarchy",
            sources,
            (
                "carrier_hierarchy_created",
                "carrier_lifecycle_created_hierarchy",
                "lifecycle_creates_carrier_hierarchy",
            ),
            "lifecycle does not create carrier hierarchy",
            "LIFECYCLE_CREATES_CARRIER_HIERARCHY",
        ),
        _collapse_check(
            "no_winning_carrier_selected",
            sources,
            ("winning_carrier_selected", "lifecycle_selects_winning_carrier"),
            "lifecycle does not select winning carrier",
            "LIFECYCLE_SELECTS_WINNING_CARRIER",
        ),
        _collapse_check(
            "no_losing_carrier_invalidated",
            sources,
            ("losing_carrier_invalidated", "lifecycle_invalidates_losing_carrier"),
            "lifecycle does not invalidate losing carrier",
            "LIFECYCLE_INVALIDATES_LOSING_CARRIER",
        ),
        _collapse_check(
            "no_distributed_standing",
            sources,
            (
                "distributed_standing_created",
                "carrier_lifecycle_created_distributed_standing",
                "lifecycle_creates_distributed_standing",
            ),
            "lifecycle does not create distributed standing",
            "LIFECYCLE_CREATES_DISTRIBUTED_STANDING",
        ),
        _collapse_check(
            "no_repository_synchronization",
            sources,
            (
                "repository_synchronization_authorized",
                "repository_synchronization_created",
                "repository_sync_authorized",
                "carrier_lifecycle_authorized_sync",
                "lifecycle_authorizes_repository_sync",
            ),
            "lifecycle does not authorize repository synchronization",
            "LIFECYCLE_AUTHORIZES_REPOSITORY_SYNC",
        ),
        _collapse_check(
            "no_full_body_transfer",
            sources,
            (
                "full_body_transfer_authorized",
                "full_body_transfer_created",
                "carrier_lifecycle_authorized_full_body_transfer",
                "lifecycle_authorizes_full_body_transfer",
            ),
            "lifecycle does not authorize full body transfer",
            "LIFECYCLE_AUTHORIZES_FULL_BODY_TRANSFER",
        ),
        _collapse_check(
            "no_carrier_registry",
            sources,
            (
                "carrier_registry_created",
                "carrier_registry_authorized",
                "carrier_lifecycle_created_registry",
                "lifecycle_creates_carrier_registry",
            ),
            "lifecycle does not create carrier registry",
            "LIFECYCLE_CREATES_CARRIER_REGISTRY",
        ),
        _collapse_check(
            "no_continuation",
            sources,
            (
                "continuation_authorized",
                "carrier_lifecycle_authorized_continuation",
                "lifecycle_authorizes_continuation",
            ),
            "lifecycle does not authorize continuation",
            "LIFECYCLE_AUTHORIZES_CONTINUATION",
        ),
        _collapse_check(
            "no_distributed_operation",
            sources,
            (
                "distributed_operation_authorized",
                "carrier_lifecycle_authorized_distributed_operation",
                "lifecycle_authorizes_distributed_operation",
            ),
            "lifecycle does not authorize distributed operation",
            "LIFECYCLE_AUTHORIZES_DISTRIBUTED_OPERATION",
        ),
        _collapse_check(
            "no_latest_file_currentness",
            sources,
            ("latest_file_currentness", "recency_fraud"),
            "lifecycle does not use latest-file currentness or recency fraud",
            "LATEST_FILE_CURRENTNESS",
        ),
        _collapse_check(
            "no_mutation_replay_merge",
            sources,
            (
                "mutation_performed",
                "replay_performed",
                "merge_performed",
                "mutation_requested",
                "replay_requested",
                "merge_requested",
            ),
            "lifecycle does not mutate, replay, or merge evidence",
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "non_claims_remain_false",
            _required_non_claims_false(declared_non_claims),
            "required lifecycle non-claims are present and false",
            declared_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    return checks


def _lifecycle_statement(
    outcome: str,
    question: Mapping[str, Any],
    selected_carrier: Mapping[str, Any],
    prior_status: Mapping[str, Any],
    requested_status: Mapping[str, Any],
    basis: Mapping[str, Any],
    related_evidence: Mapping[str, Any],
    transition: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    recorded = outcome == CARRIER_LIFECYCLE_STATUS_RECORDED
    not_recorded = outcome == CARRIER_LIFECYCLE_STATUS_NOT_RECORDED
    return {
        "carrier_lifecycle_status_recorded": recorded,
        "not_recorded_reason": question.get("not_recorded_reason")
        or ("lifecycle status explicitly not recorded" if not_recorded else None),
        "block_code": block_code,
        "block_reason": block_reason,
        "carrier_identity_preserved": bool(selected_carrier.get("carrier_identity_preserved")),
        "requested_lifecycle_status_preserved": bool(
            requested_status.get("requested_lifecycle_status_preserved")
        ),
        "prior_lifecycle_status_preserved": bool(
            prior_status.get("prior_lifecycle_status_preserved")
        ),
        "lifecycle_basis_preserved": bool(basis.get("lifecycle_basis_preserved")),
        "transition_basis_preserved": bool(transition.get("transition_basis_preserved")),
        "related_evidence_preserved": bool(related_evidence.get("related_evidence_preserved")),
        "visible_refusal_preserved": bool(
            basis.get("visible_refusal_available") and basis.get("visible_refusal_preserved")
        ),
        "visible_divergence_preserved": bool(
            basis.get("visible_divergence_available")
            and basis.get("visible_divergence_preserved")
        ),
        "visible_corruption_preserved": bool(
            basis.get("visible_corruption_available")
            and basis.get("visible_corruption_preserved")
        ),
        "visible_staleness_preserved": bool(
            basis.get("visible_staleness_available") and basis.get("visible_staleness_preserved")
        ),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "prior_evidence_erased": False,
        "source_replaced": False,
        "currentness_created": False,
        "authority_created": False,
        "permission_created": False,
        "carrier_hierarchy_created": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "distributed_standing_created": False,
        "carrier_registry_created": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
        "lifecycle_created_registry": False,
        "lifecycle_created_persistence": False,
        "lifecycle_created_body_participation": False,
        "lifecycle_repaired_by_overwrite": False,
        "lifecycle_mutated_evidence": False,
        "lifecycle_replayed_evidence": False,
        "lifecycle_merged_evidence": False,
    }


def _status_value(raw: Any) -> str | None:
    value: Any
    if isinstance(raw, Mapping):
        value = (
            raw.get("lifecycle_status")
            or raw.get("requested_lifecycle_status")
            or raw.get("prior_lifecycle_status")
            or raw.get("status")
            or raw.get("value")
        )
    else:
        value = raw
    normalized = _normalize_token(value)
    return normalized or None


def _transition_supported(prior: str, requested: str) -> bool:
    if prior == requested:
        return True
    if (prior, requested) in SUPPORTED_EXPLICIT_TRANSITIONS:
        return True
    if requested == "CARRIER_WITHDRAWN" and prior in WITHDRAWABLE_STATUSES:
        return True
    if requested in {"CARRIER_RETIRED", "CARRIER_REPLACED"}:
        return prior in SUPPORTED_LIFECYCLE_STATUSES
    return False


def _visible_basis_posture(raw: Any, posture_name: str) -> dict[str, bool]:
    if raw is None:
        return {"available": False, "preserved": True}
    if isinstance(raw, Mapping):
        basis = _as_mapping(raw)
        hidden_keys = (
            f"{posture_name}_hidden",
            f"hidden_{posture_name}",
            f"{posture_name}_erased",
            f"{posture_name}_not_visible",
        )
        preserved_keys = (
            f"visible_{posture_name}_preserved",
            f"{posture_name}_preserved",
            f"{posture_name}_remains_visible",
            "remains_visible",
            "visible",
            "preserved",
        )
        hidden = any(basis.get(key) is True for key in hidden_keys)
        explicit_false = any(basis.get(key) is False for key in preserved_keys)
        explicit_true = any(basis.get(key) is True for key in preserved_keys)
        return {
            "available": bool(basis),
            "preserved": bool(basis) and not hidden and not explicit_false and (explicit_true or True),
        }
    return {"available": _nonempty(raw), "preserved": _nonempty(raw)}


def _basis_declared(value: Any) -> bool:
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return _nonempty(value)


def _declared_block_code(request: Mapping[str, Any]) -> str | None:
    block = _as_mapping(request.get("block"))
    code = (
        request.get("declared_block_code")
        or request.get("block_code")
        or block.get("block_code")
        or block.get("code")
    )
    normalized = _normalize_token(code)
    return normalized if normalized in BLOCK_REASONS else None


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


def _without_safe_sections(request: Mapping[str, Any]) -> dict[str, Any]:
    safe_keys = {
        "lifecycle_non_meaning",
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
    return BLOCK_REASONS.get(block_code, f"Lifecycle blocked by {block_code}.")


def _result_id(
    question: Mapping[str, Any],
    selected_carrier: Mapping[str, Any],
    outcome: str,
) -> str:
    basis_id = (
        question.get("lifecycle_request_id")
        or selected_carrier.get("selected_carrier_id")
        or "carrier_lifecycle"
    )
    return f"{_safe_filename_part(basis_id)}__{_safe_filename_part(outcome.lower())}"


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "source_replaced",
        "carrier_lifecycle_created_hierarchy",
        "carrier_lifecycle_created_distributed_standing",
        "carrier_lifecycle_created_registry",
        "carrier_lifecycle_authorized_sync",
        "carrier_lifecycle_authorized_full_body_transfer",
        "carrier_lifecycle_erased_evidence",
        "carrier_lifecycle_hid_refusal",
        "carrier_lifecycle_hid_divergence",
        "carrier_lifecycle_hid_corruption",
        "carrier_lifecycle_repaired_by_overwrite",
        "winning_carrier_selected",
        "losing_carrier_invalidated",
        "distributed_standing_created",
        "carrier_registry_created",
        "repository_synchronization_authorized",
        "full_body_transfer_authorized",
        "continuation_authorized",
        "distributed_operation_authorized",
        "latest_file_currentness",
        "recency_fraud",
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    )
    return {key: non_claims.get(key) for key in keys}


def _safe_filename_part(value: Any) -> str:
    raw = str(value or "carrier_lifecycle").strip()
    cleaned = "".join(char if char.isalnum() or char in "._-" else "_" for char in raw)
    return cleaned.strip("._-") or "carrier_lifecycle"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise CarrierLifecycleBoundaryError(
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "Could not allocate a non-overwriting lifecycle result path.",
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
