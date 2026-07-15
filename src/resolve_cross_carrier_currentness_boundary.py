"""Bounded cross-carrier currentness participation boundary resolver.

This resolver records whether selected carrier evidence may participate in a
later body-side current posture assessment. It does not create currentness,
select a current carrier, resolve divergence, decide source, decide truth,
authorize action, admit evidence, create carrier relation, create
multi-carrier law, create distributed standing, or authorize continuation.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CrossCarrierCurrentnessBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit currentness inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


CROSS_CARRIER_CURRENTNESS_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_cross_carrier_currentness_boundary"
)

RESOLVER_MODULE = "resolve_cross_carrier_currentness_boundary"
RESULT_VERSION = "0.1.0"

CURRENTNESS_PARTICIPATION_ELIGIBLE = "CURRENTNESS_PARTICIPATION_ELIGIBLE"
CURRENTNESS_PARTICIPATION_EXCLUDED = "CURRENTNESS_PARTICIPATION_EXCLUDED"
CURRENTNESS_PARTICIPATION_BLOCKED = "CURRENTNESS_PARTICIPATION_BLOCKED"

SUPPORTED_PARTICIPATION_INTENTS = {
    "EVALUATE_PARTICIPATION",
    "EXCLUDE_FROM_CURRENTNESS_PARTICIPATION",
    "BLOCK_CURRENTNESS_PARTICIPATION",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created_by_carrier": False,
    "source_replaced": False,
    "carrier_evidence_became_current": False,
    "local_copy_currentness": False,
    "latest_file_currentness": False,
    "newest_timestamp_currentness": False,
    "possession_currentness": False,
    "return_currentness": False,
    "receipt_currentness": False,
    "admission_currentness": False,
    "correspondence_currentness": False,
    "divergence_currentness": False,
    "majority_carrier_currentness": False,
    "successful_receipt_count_currentness": False,
    "successful_admission_count_currentness": False,
    "carrier_availability_currentness": False,
    "carrier_label_currentness": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "carrier_hierarchy_created": False,
    "carrier_relation_created": False,
    "multi_carrier_law_created": False,
    "distributed_standing_created": False,
    "signal_created_by_default": False,
    "presence_established": False,
    "threshold_met": False,
    "truth_created": False,
    "action_authorized": False,
    "consequence_created": False,
    "continuation_authorized": False,
    "divergence_hidden": False,
    "refusal_hidden": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "DECLARED_CURRENTNESS_REQUEST_MISSING": "No declared currentness request was supplied.",
    "DECLARED_CURRENTNESS_REQUEST_UNREADABLE": "The declared currentness request path could not be read.",
    "DECLARED_CURRENTNESS_REQUEST_MALFORMED": "The declared currentness request is not a JSON object or mapping.",
    "CURRENTNESS_QUESTION_UNDECLARED": "Currentness question is undeclared.",
    "BODY_CURRENT_POSTURE_UNDECLARED": "Selected body-side current posture is undeclared.",
    "SELECTED_CARRIER_EVIDENCE_MISSING": "Selected carrier evidence is missing.",
    "SELECTED_CARRIER_EVIDENCE_MALFORMED": "Selected carrier evidence is malformed.",
    "EVIDENCE_IDENTITY_MISSING": "Selected evidence identity is missing.",
    "EVIDENCE_OUTCOME_MISSING": "Selected evidence outcome or status is missing.",
    "CARRIER_IDENTITY_MISSING": "Carrier identity is missing where required.",
    "ADMISSION_STATUS_UNKNOWN": "Admission status is unknown where required.",
    "DIVERGENCE_STATUS_UNKNOWN": "Divergence status is unknown where required.",
    "HIDDEN_DIVERGENCE_BLOCKS_CURRENTNESS": "Hidden divergence blocks currentness participation.",
    "LATEST_FILE_CURRENTNESS": "Latest-file recency is treated as currentness.",
    "NEWEST_TIMESTAMP_CURRENTNESS": "Newest timestamp is treated as currentness.",
    "LOCAL_COPY_CURRENTNESS": "Local copy is treated as currentness.",
    "POSSESSION_CURRENTNESS": "Possession is treated as currentness.",
    "RETURN_CURRENTNESS": "Return is treated as currentness.",
    "RECEIPT_CURRENTNESS": "Receipt is treated as currentness.",
    "ADMISSION_CURRENTNESS": "Admission is treated as currentness.",
    "CORRESPONDENCE_CURRENTNESS": "Correspondence is treated as currentness.",
    "DIVERGENCE_CURRENTNESS": "Divergence is treated as currentness.",
    "MAJORITY_CARRIER_CURRENTNESS": "Majority carriers are treated as currentness.",
    "SUCCESSFUL_RECEIPT_COUNT_CURRENTNESS": "Successful receipt count is treated as currentness.",
    "SUCCESSFUL_ADMISSION_COUNT_CURRENTNESS": "Successful admission count is treated as currentness.",
    "CARRIER_AVAILABILITY_CURRENTNESS": "Carrier availability is treated as currentness.",
    "CARRIER_LABEL_CURRENTNESS": "Carrier label is treated as currentness.",
    "WINNING_CARRIER_SELECTED": "Currentness selects a winning carrier.",
    "LOSING_CARRIER_INVALIDATED": "Currentness invalidates a losing carrier.",
    "CARRIER_HIERARCHY_CREATED": "Currentness creates carrier hierarchy.",
    "CURRENTNESS_REPLACES_SOURCE": "Currentness replaces source.",
    "CURRENTNESS_CREATES_AUTHORITY": "Currentness creates authority.",
    "CURRENTNESS_CREATES_PERMISSION": "Currentness creates permission.",
    "CURRENTNESS_CREATES_SUCCESSOR": "Currentness creates successor standing.",
    "CURRENTNESS_CREATES_BODY": "Currentness creates body formation.",
    "CURRENTNESS_CREATES_SIGNAL_BY_DEFAULT": "Currentness creates signal by default.",
    "CURRENTNESS_ESTABLISHES_PRESENCE": "Currentness establishes presence.",
    "CURRENTNESS_ESTABLISHES_THRESHOLD": "Currentness establishes threshold.",
    "CURRENTNESS_CREATES_TRUTH": "Currentness creates truth.",
    "CURRENTNESS_AUTHORIZES_ACTION": "Currentness authorizes action.",
    "CURRENTNESS_CREATES_CONSEQUENCE": "Currentness creates consequence.",
    "CURRENTNESS_CREATES_MULTI_CARRIER_LAW": "Currentness creates multi-carrier law.",
    "CURRENTNESS_CREATES_DISTRIBUTED_STANDING": "Currentness creates distributed standing.",
    "CURRENTNESS_AUTHORIZES_CONTINUATION": "Currentness authorizes continuation.",
    "CURRENTNESS_HIDES_REFUSAL": "Currentness hides refusal.",
    "CURRENTNESS_MUTATES_OR_REPLAYS_EVIDENCE": "Currentness mutates, replays, or merges evidence.",
    "PARTICIPATION_INTENT_UNSUPPORTED": "Currentness participation intent is unsupported.",
    "BLOCK_CURRENTNESS_PARTICIPATION_REQUESTED": "Currentness participation was explicitly blocked by declared intent.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required currentness non-claim is missing or flipped.",
}

CURRENTNESS_NON_MEANING = {
    "does_not_mean_carrier_currentness": True,
    "does_not_mean_evidence_currentness": True,
    "does_not_mean_source_replacement": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_successor": True,
    "does_not_mean_body": True,
    "does_not_mean_carrier_relation": True,
    "does_not_mean_multi_carrier_law": True,
    "does_not_mean_distributed_standing": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_signal_by_default": True,
    "does_not_mean_presence": True,
    "does_not_mean_threshold": True,
    "does_not_mean_truth": True,
    "does_not_mean_action": True,
    "does_not_mean_consequence": True,
    "does_not_mean_continuation": True,
    "does_not_mean_winning_carrier": True,
    "does_not_mean_losing_carrier_invalidated": True,
    "does_not_mean_carrier_hierarchy": True,
    "does_not_mean_divergence_resolved": True,
    "does_not_mean_majority_rule": True,
    "does_not_mean_latest_file_rule": True,
    "does_not_mean_successful_receipt_count_rule": True,
    "does_not_mean_successful_admission_count_rule": True,
}

OPEN_SURFACES = [
    "cross-carrier currentness implementation refinement",
    "multi-carrier relation law",
    "multi-carrier relation conformance",
    "multi-carrier relation closure",
    "distributed standing",
    "persistence/registry law",
    "presence law",
    "threshold law",
    "truth law",
    "action/consequence law",
    "generalized vessel relation lifecycle",
    "body relevance medium",
    "signal series or accumulation logic",
    "successor carrier law",
    "future self-orientation successor only if separately justified",
]

ANTI_CURRENTNESS_CHECKS = (
    (
        "carrier_does_not_create_currentness",
        ("currentness_created_by_carrier", "carrier_created_currentness", "carrier_creates_currentness"),
        "carrier does not create currentness",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    ),
    (
        "carrier_evidence_does_not_become_current",
        ("carrier_evidence_became_current", "evidence_became_current", "selected_evidence_became_current"),
        "carrier evidence does not become current",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    ),
    (
        "currentness_not_derived_from_carrier_emission",
        ("emission_currentness", "carrier_emission_currentness", "carrier_produced_currentness"),
        "carrier emission is not currentness",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    ),
    (
        "currentness_not_derived_from_latest_file",
        ("latest_file_currentness", "latest_file_recency_currentness", "currentness_derived_from_latest_file"),
        "latest file is not currentness",
        "LATEST_FILE_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_newest_timestamp",
        ("newest_timestamp_currentness", "currentness_derived_from_newest_timestamp"),
        "newest timestamp is not currentness",
        "NEWEST_TIMESTAMP_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_local_copy",
        ("local_copy_currentness", "currentness_derived_from_local_copy"),
        "local copy is not currentness",
        "LOCAL_COPY_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_possession",
        ("possession_currentness", "currentness_derived_from_possession"),
        "possession is not currentness",
        "POSSESSION_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_return",
        ("return_currentness", "returned_evidence_currentness", "currentness_derived_from_return"),
        "return is not currentness",
        "RETURN_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_receipt",
        ("receipt_currentness", "successful_receipt_currentness", "currentness_derived_from_receipt"),
        "receipt is not currentness",
        "RECEIPT_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_admission",
        ("admission_currentness", "successful_admission_currentness", "currentness_derived_from_admission"),
        "admission is not currentness",
        "ADMISSION_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_correspondence",
        ("correspondence_currentness", "currentness_derived_from_correspondence"),
        "correspondence is not currentness",
        "CORRESPONDENCE_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_divergence",
        ("divergence_currentness", "currentness_derived_from_divergence"),
        "divergence is not currentness",
        "DIVERGENCE_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_majority_carriers",
        ("majority_carrier_currentness", "majority_carriers_currentness", "currentness_derived_from_majority"),
        "majority carriers are not currentness",
        "MAJORITY_CARRIER_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_carrier_count",
        ("carrier_count_currentness", "currentness_derived_from_carrier_count"),
        "carrier count is not currentness",
        "MAJORITY_CARRIER_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_successful_receipt_count",
        ("successful_receipt_count_currentness", "currentness_derived_from_successful_receipt_count"),
        "successful receipt count is not currentness",
        "SUCCESSFUL_RECEIPT_COUNT_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_successful_admission_count",
        ("successful_admission_count_currentness", "currentness_derived_from_successful_admission_count"),
        "successful admission count is not currentness",
        "SUCCESSFUL_ADMISSION_COUNT_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_carrier_availability",
        ("carrier_availability_currentness", "currentness_derived_from_carrier_availability"),
        "carrier availability is not currentness",
        "CARRIER_AVAILABILITY_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_carrier_label",
        ("carrier_label_currentness", "currentness_derived_from_carrier_label"),
        "carrier label is not currentness",
        "CARRIER_LABEL_CURRENTNESS",
    ),
    (
        "currentness_not_derived_from_convenience",
        ("convenience_currentness", "convenient_path_currentness", "currentness_derived_from_convenience"),
        "convenience is not currentness",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    ),
    (
        "no_winning_carrier_selected",
        ("winning_carrier_selected", "currentness_selects_winning_carrier"),
        "no winning carrier is selected",
        "WINNING_CARRIER_SELECTED",
    ),
    (
        "no_losing_carrier_invalidated",
        ("losing_carrier_invalidated", "currentness_invalidates_losing_carrier"),
        "no losing carrier is invalidated",
        "LOSING_CARRIER_INVALIDATED",
    ),
    (
        "no_carrier_hierarchy_created",
        ("carrier_hierarchy_created", "currentness_creates_carrier_hierarchy"),
        "no carrier hierarchy is created",
        "CARRIER_HIERARCHY_CREATED",
    ),
    (
        "source_not_replaced",
        ("source_replaced", "currentness_replaces_source"),
        "source is not replaced",
        "CURRENTNESS_REPLACES_SOURCE",
    ),
    (
        "authority_not_created",
        ("authority_created", "currentness_creates_authority"),
        "authority is not created",
        "CURRENTNESS_CREATES_AUTHORITY",
    ),
    (
        "permission_not_created",
        ("permission_created", "currentness_creates_permission"),
        "permission is not created",
        "CURRENTNESS_CREATES_PERMISSION",
    ),
    (
        "successor_not_created",
        ("currentness_creates_successor", "successor_created", "successor_standing_created"),
        "successor standing is not created",
        "CURRENTNESS_CREATES_SUCCESSOR",
    ),
    (
        "body_not_created",
        ("currentness_creates_body", "body_created", "body_formed"),
        "body is not created",
        "CURRENTNESS_CREATES_BODY",
    ),
    (
        "signal_not_created_by_default",
        ("signal_created_by_default", "currentness_creates_signal_by_default"),
        "signal is not created by default",
        "CURRENTNESS_CREATES_SIGNAL_BY_DEFAULT",
    ),
    (
        "presence_not_established",
        ("presence_established", "currentness_establishes_presence"),
        "presence is not established",
        "CURRENTNESS_ESTABLISHES_PRESENCE",
    ),
    (
        "threshold_not_met",
        ("threshold_met", "currentness_establishes_threshold"),
        "threshold is not met",
        "CURRENTNESS_ESTABLISHES_THRESHOLD",
    ),
    (
        "truth_not_created",
        ("truth_created", "currentness_creates_truth"),
        "truth is not created",
        "CURRENTNESS_CREATES_TRUTH",
    ),
    (
        "action_not_authorized",
        ("action_authorized", "currentness_authorizes_action"),
        "action is not authorized",
        "CURRENTNESS_AUTHORIZES_ACTION",
    ),
    (
        "consequence_not_created",
        ("consequence_created", "currentness_creates_consequence"),
        "consequence is not created",
        "CURRENTNESS_CREATES_CONSEQUENCE",
    ),
    (
        "carrier_relation_not_created",
        ("carrier_relation_created", "currentness_creates_carrier_relation"),
        "carrier relation is not created",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    ),
    (
        "multi_carrier_law_not_created",
        ("multi_carrier_law_created", "currentness_creates_multi_carrier_law"),
        "multi-carrier law is not created",
        "CURRENTNESS_CREATES_MULTI_CARRIER_LAW",
    ),
    (
        "distributed_standing_not_created",
        ("distributed_standing_created", "currentness_creates_distributed_standing"),
        "distributed standing is not created",
        "CURRENTNESS_CREATES_DISTRIBUTED_STANDING",
    ),
    (
        "continuation_not_authorized",
        ("continuation_authorized", "currentness_authorizes_continuation", "follow_on_work_authorized", "follow_on_steps_authorized"),
        "continuation is not authorized",
        "CURRENTNESS_AUTHORIZES_CONTINUATION",
    ),
    (
        "mutation_replay_merge_not_performed",
        ("mutation_performed", "replay_performed", "merge_performed", "currentness_mutates_evidence", "currentness_replays_evidence", "currentness_merges_evidence"),
        "mutation, replay, and merge are not performed",
        "CURRENTNESS_MUTATES_OR_REPLAYS_EVIDENCE",
    ),
)


def resolve_cross_carrier_currentness_boundary(
    declared_currentness_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one declared cross-carrier currentness participation request."""

    if declared_currentness_request is None:
        request: dict[str, Any] = {}
        precheck_failures = ["DECLARED_CURRENTNESS_REQUEST_MISSING"]
    elif not isinstance(declared_currentness_request, Mapping):
        request = {}
        precheck_failures = ["DECLARED_CURRENTNESS_REQUEST_MALFORMED"]
    else:
        request = copy.deepcopy(dict(declared_currentness_request))
        precheck_failures = []
    return _resolve_request(request, precheck_failures)


def resolve_cross_carrier_currentness_boundary_from_path(
    declared_currentness_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one declared currentness request JSON path."""

    try:
        request = _read_json_mapping(declared_currentness_request_path)
        request["_declared_currentness_request_path"] = str(
            Path(declared_currentness_request_path)
        )
        precheck_failures: list[str] = []
    except CrossCarrierCurrentnessBoundaryError as exc:
        request = {}
        precheck_failures = [exc.block_code]
    return _resolve_request(request, precheck_failures)


def write_cross_carrier_currentness_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded currentness participation result without overwriting."""

    if output_path is None:
        question = _as_mapping(result.get("declared_currentness_question"))
        basis_id = (
            question.get("currentness_request_id")
            or question.get("participation_intent")
            or "cross_carrier_currentness"
        )
        filename = (
            f"{_safe_filename_part(basis_id)}"
            "__cross_carrier_currentness_result.json"
        )
        target = CROSS_CARRIER_CURRENTNESS_BOUNDARY_ROOT / filename
    else:
        target = Path(output_path)
    target = _non_overwriting_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    return target


def build_cross_carrier_currentness_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact bounded summary for a currentness participation result."""

    checks = _mapping_list(result.get("currentness_checks"))
    question = _as_mapping(result.get("declared_currentness_question"))
    body_posture = _as_mapping(result.get("selected_body_current_posture"))
    participation = _as_mapping(result.get("currentness_participation_result"))
    status = _as_mapping(result.get("carrier_evidence_status"))
    non_claims = _as_mapping(result.get("non_claims"))
    block = _as_mapping(result.get("block"))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "currentness_request_id": question.get("currentness_request_id"),
        "currentness_question": question.get("currentness_question"),
        "participation_intent": question.get("participation_intent"),
        "selected_body_current_posture_id": body_posture.get(
            "body_current_posture_id"
        ),
        "selected_body_current_posture_label": body_posture.get(
            "body_current_posture_label"
        ),
        "selected_evidence_count": status.get("selected_evidence_count"),
        "selected_evidence_ids": copy.deepcopy(status.get("selected_evidence_ids")),
        "selected_evidence_outcomes": copy.deepcopy(
            status.get("selected_evidence_outcomes")
        ),
        "selected_carrier_ids": copy.deepcopy(status.get("selected_carrier_ids")),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "participation_eligible": bool(
            participation.get("currentness_participation_eligible")
        ),
        "participation_excluded": bool(
            participation.get("currentness_participation_excluded")
        ),
        "carrier_evidence_became_current": bool(
            non_claims.get("carrier_evidence_became_current")
        ),
        "currentness_created_by_carrier": bool(
            non_claims.get("currentness_created_by_carrier")
        ),
        "source_created": bool(non_claims.get("source_replaced")),
        "authority_created": bool(non_claims.get("authority_created")),
        "permission_created": bool(non_claims.get("permission_created")),
        "source_authority_permission_created": bool(
            non_claims.get("source_replaced")
            or non_claims.get("authority_created")
            or non_claims.get("permission_created")
        ),
        "carrier_hierarchy_created": bool(
            non_claims.get("carrier_hierarchy_created")
        ),
        "winning_carrier_selected": bool(non_claims.get("winning_carrier_selected")),
        "losing_carrier_invalidated": bool(
            non_claims.get("losing_carrier_invalidated")
        ),
        "multi_carrier_law_created": bool(non_claims.get("multi_carrier_law_created")),
        "distributed_standing_created": bool(
            non_claims.get("distributed_standing_created")
        ),
        "presence_created": bool(non_claims.get("presence_established")),
        "threshold_created": bool(non_claims.get("threshold_met")),
        "truth_created": bool(non_claims.get("truth_created")),
        "action_authorized": bool(non_claims.get("action_authorized")),
        "consequence_created": bool(non_claims.get("consequence_created")),
        "presence_threshold_truth_action_consequence_created": bool(
            non_claims.get("presence_established")
            or non_claims.get("threshold_met")
            or non_claims.get("truth_created")
            or non_claims.get("action_authorized")
            or non_claims.get("consequence_created")
        ),
        "continuation_authorized": bool(non_claims.get("continuation_authorized")),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_declared_currentness_request(
    currentness_request_id: str,
    currentness_question: str,
    selected_body_current_posture: Mapping[str, Any],
    selected_carrier_evidence: Sequence[Mapping[str, Any]],
    participation_intent: str = "EVALUATE_PARTICIPATION",
) -> dict[str, Any]:
    """Build a minimum declared currentness participation request."""

    return {
        "currentness_request_id": currentness_request_id,
        "currentness_question": currentness_question,
        "selected_body_current_posture": copy.deepcopy(
            dict(selected_body_current_posture)
        ),
        "selected_carrier_evidence": [
            copy.deepcopy(dict(item)) for item in selected_carrier_evidence
        ],
        "participation_intent": _normalize_token(participation_intent)
        or participation_intent,
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }


def _resolve_request(
    request: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    request_mapping = _as_mapping(request)
    raw_evidence = request_mapping.get("selected_carrier_evidence")
    selected_evidence = _normalize_selected_carrier_evidence(raw_evidence)
    body_posture = _normalize_body_current_posture(
        request_mapping.get("selected_body_current_posture")
    )
    intent = _normalize_token(request_mapping.get("participation_intent"))
    declared_non_claims = _as_mapping(request_mapping.get("declared_non_claims"))
    checks = _build_currentness_checks(
        request_mapping,
        body_posture,
        raw_evidence,
        selected_evidence,
        intent,
        declared_non_claims,
        precheck_failures,
    )
    failed_check = _first_failed(checks)

    if failed_check:
        outcome = CURRENTNESS_PARTICIPATION_BLOCKED
        block_code = str(failed_check.get("block_code"))
    elif intent == "EXCLUDE_FROM_CURRENTNESS_PARTICIPATION":
        outcome = CURRENTNESS_PARTICIPATION_EXCLUDED
        block_code = None
    elif intent == "BLOCK_CURRENTNESS_PARTICIPATION":
        outcome = CURRENTNESS_PARTICIPATION_BLOCKED
        block_code = (
            _requested_block_code(request_mapping)
            or "BLOCK_CURRENTNESS_PARTICIPATION_REQUESTED"
        )
    else:
        outcome = CURRENTNESS_PARTICIPATION_ELIGIBLE
        block_code = None

    block_reason = _block_reason(block_code, failed_check)
    result: dict[str, Any] = {
        "cross_carrier_currentness_metadata": {
            "cross_carrier_currentness_result_id": _result_id(
                request_mapping,
                intent,
                outcome,
            ),
            "cross_carrier_currentness_result_type": (
                "cross_carrier_currentness_boundary_result"
            ),
            "cross_carrier_currentness_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_currentness_question": _declared_currentness_question(
            request_mapping,
            intent,
            selected_evidence,
        ),
        "selected_body_current_posture": body_posture,
        "selected_carrier_evidence": selected_evidence,
        "carrier_evidence_status": _carrier_evidence_status(selected_evidence),
        "currentness_basis": _currentness_basis(
            request_mapping,
            body_posture,
            selected_evidence,
            intent,
        ),
        "currentness_checks": checks,
        "currentness_participation_result": _currentness_participation_result(
            outcome,
            request_mapping,
            selected_evidence,
            body_posture,
            block_code,
            block_reason,
            checks,
        ),
        "currentness_non_meaning": copy.deepcopy(CURRENTNESS_NON_MEANING),
        "what_remains_open": _what_remains_open(),
        "non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
        "outcome": outcome,
        "block": {
            "code": block_code,
            "reason": block_reason,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["cross_carrier_currentness_summary"] = (
        build_cross_carrier_currentness_summary(result)
    )
    return result


def _build_currentness_checks(
    request: Mapping[str, Any],
    body_posture: Mapping[str, Any],
    raw_evidence: Any,
    selected_evidence: Sequence[Mapping[str, Any]],
    intent: str | None,
    declared_non_claims: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    currentness_basis = _as_mapping(request.get("currentness_basis"))
    lineage_basis = request.get("lineage_basis")
    selected_admission_basis = request.get("selected_admission_basis")
    selected_divergence_basis = request.get("selected_divergence_basis")
    selected_correspondence_basis = request.get("selected_correspondence_basis")
    sources = [
        request,
        currentness_basis,
        body_posture,
        raw_evidence,
        selected_evidence,
        declared_non_claims,
        _as_mapping(selected_admission_basis),
        _as_mapping(selected_divergence_basis),
        _as_mapping(selected_correspondence_basis),
    ]
    precheck_code = (
        precheck_failures[0]
        if precheck_failures
        else "DECLARED_CURRENTNESS_REQUEST_MALFORMED"
    )
    raw_parseable = (
        raw_evidence is None
        or isinstance(raw_evidence, Mapping)
        or (
            isinstance(raw_evidence, list)
            and all(isinstance(item, Mapping) for item in raw_evidence)
        )
    )
    admission_status_required = _admission_status_required(request, selected_evidence)
    divergence_status_required = _divergence_status_required(request, selected_evidence)
    checks = [
        _check(
            "declared_currentness_request_is_parseable_mapping",
            not precheck_failures,
            "declared currentness request is a mapping",
            list(precheck_failures),
            precheck_code,
        ),
        _check(
            "currentness_question_declared",
            bool(str(request.get("currentness_question") or "").strip()),
            "currentness question is declared",
            request.get("currentness_question"),
            "CURRENTNESS_QUESTION_UNDECLARED",
        ),
        _check(
            "selected_body_current_posture_declared",
            bool(body_posture.get("body_current_posture_declared")),
            "selected body-side current posture is declared",
            body_posture,
            "BODY_CURRENT_POSTURE_UNDECLARED",
        ),
        _check(
            "participation_intent_supported",
            intent in SUPPORTED_PARTICIPATION_INTENTS,
            "participation intent is in the bounded intent set",
            intent,
            "PARTICIPATION_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_carrier_evidence_exists",
            raw_evidence is not None and bool(selected_evidence),
            "selected carrier evidence is supplied",
            raw_evidence,
            "SELECTED_CARRIER_EVIDENCE_MISSING",
        ),
        _check(
            "selected_carrier_evidence_parseable",
            raw_parseable,
            "selected carrier evidence is a mapping or list of mappings",
            _raw_evidence_shape(raw_evidence),
            "SELECTED_CARRIER_EVIDENCE_MALFORMED",
        ),
        _check(
            "evidence_identity_present",
            bool(selected_evidence)
            and all(item.get("evidence_id") for item in selected_evidence),
            "each selected evidence identity is declared",
            [item.get("evidence_id") for item in selected_evidence],
            "EVIDENCE_IDENTITY_MISSING",
        ),
        _check(
            "evidence_outcome_present",
            bool(selected_evidence)
            and all(item.get("evidence_outcome") for item in selected_evidence),
            "each selected evidence outcome or status is declared",
            [item.get("evidence_outcome") for item in selected_evidence],
            "EVIDENCE_OUTCOME_MISSING",
        ),
        _check(
            "carrier_identity_present_where_required",
            bool(selected_evidence)
            and all(item.get("carrier_id") for item in selected_evidence),
            "selected carrier identities are declared",
            [item.get("carrier_id") for item in selected_evidence],
            "CARRIER_IDENTITY_MISSING",
        ),
        _check(
            "admission_status_known_where_required",
            not admission_status_required
            or all(item.get("admission_status") for item in selected_evidence),
            "admission status is known where required",
            {
                "admission_status_required": admission_status_required,
                "admission_statuses": [
                    item.get("admission_status") for item in selected_evidence
                ],
            },
            "ADMISSION_STATUS_UNKNOWN",
        ),
        _check(
            "admission_status_not_unknown_where_required",
            not admission_status_required
            or not any(
                _status_unknown(item.get("admission_status"))
                for item in selected_evidence
            ),
            "admission status is not unknown where required",
            {
                "admission_status_required": admission_status_required,
                "admission_statuses": [
                    item.get("admission_status") for item in selected_evidence
                ],
            },
            "ADMISSION_STATUS_UNKNOWN",
        ),
        _check(
            "divergence_status_known_where_required",
            not divergence_status_required
            or all(item.get("divergence_status") for item in selected_evidence),
            "divergence status is known where required",
            {
                "divergence_status_required": divergence_status_required,
                "divergence_statuses": [
                    item.get("divergence_status") for item in selected_evidence
                ],
            },
            "DIVERGENCE_STATUS_UNKNOWN",
        ),
        _check(
            "divergence_status_not_unknown_or_unresolved_where_required",
            not divergence_status_required
            or not any(
                _status_unknown_or_unresolved(item.get("divergence_status"))
                for item in selected_evidence
            ),
            "divergence status is not unknown or unresolved where required",
            {
                "divergence_status_required": divergence_status_required,
                "divergence_statuses": [
                    item.get("divergence_status") for item in selected_evidence
                ],
            },
            "DIVERGENCE_STATUS_UNKNOWN",
        ),
        _check(
            "hidden_divergence_false",
            not _flag_true(
                sources,
                ("divergence_hidden", "hidden_divergence", "currentness_hides_divergence"),
            ),
            "hidden divergence is false",
            _flag_snapshot(
                sources,
                ("divergence_hidden", "hidden_divergence", "currentness_hides_divergence"),
            ),
            "HIDDEN_DIVERGENCE_BLOCKS_CURRENTNESS",
        ),
        _check(
            "refusal_hidden_false",
            not _flag_true(sources, ("refusal_hidden", "currentness_hides_refusal")),
            "refusal hidden is false",
            _flag_snapshot(sources, ("refusal_hidden", "currentness_hides_refusal")),
            "CURRENTNESS_HIDES_REFUSAL",
        ),
        _check(
            "lineage_basis_preserved_where_supplied",
            _lineage_basis_preserved(lineage_basis),
            "lineage basis is preserved where supplied",
            lineage_basis,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]

    for check_name, aliases, expected, block_code in ANTI_CURRENTNESS_CHECKS:
        actual = _flag_snapshot(sources, aliases)
        checks.append(
            _check(
                check_name,
                not _flag_true(sources, aliases),
                expected,
                actual,
                block_code,
            )
        )

    missing_or_flipped = _missing_or_flipped_non_claims(declared_non_claims)
    selected_non_claim_conflicts = _selected_non_claim_collapse(selected_evidence)
    checks.append(
        _check(
            "non_claims_remain_false",
            not missing_or_flipped and not selected_non_claim_conflicts,
            "all required currentness non-claims are present and false",
            {
                "declared_non_claim_failures": missing_or_flipped,
                "selected_evidence_non_claim_collapse": selected_non_claim_conflicts,
            },
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _declared_currentness_question(
    request: Mapping[str, Any],
    intent: str | None,
    selected_evidence: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    body_posture = _normalize_body_current_posture(
        request.get("selected_body_current_posture")
    )
    return {
        "currentness_request_id": _first_text(
            request,
            ("currentness_request_id", "request_id", "id"),
        ),
        "currentness_question": request.get("currentness_question"),
        "currentness_purpose": request.get("currentness_purpose"),
        "declared_scope": copy.deepcopy(request.get("declared_scope")),
        "participation_intent": intent,
        "selected_body_current_posture_id": body_posture.get(
            "body_current_posture_id"
        ),
        "selected_body_current_posture_label": body_posture.get(
            "body_current_posture_label"
        ),
        "selected_evidence_count": len(selected_evidence),
        "declared_non_claims": copy.deepcopy(
            _as_mapping(request.get("declared_non_claims"))
        ),
        "declared_currentness_request_path": request.get(
            "_declared_currentness_request_path"
        ),
    }


def _carrier_evidence_status(
    selected_evidence: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    return {
        "selected_evidence_count": len(selected_evidence),
        "selected_evidence_ids": [
            item.get("evidence_id") for item in selected_evidence
        ],
        "selected_evidence_outcomes": [
            item.get("evidence_outcome") for item in selected_evidence
        ],
        "selected_carrier_ids": [item.get("carrier_id") for item in selected_evidence],
        "selected_carrier_roles": [
            item.get("carrier_role") for item in selected_evidence
        ],
        "selected_emission_classes": [
            item.get("emission_class") for item in selected_evidence
        ],
        "admission_statuses": [
            item.get("admission_status") for item in selected_evidence
        ],
        "correspondence_statuses": [
            item.get("correspondence_status") for item in selected_evidence
        ],
        "divergence_statuses": [
            item.get("divergence_status") for item in selected_evidence
        ],
        "carrier_held_does_not_mean_current": True,
        "carrier_produced_does_not_mean_current": True,
        "carrier_returned_does_not_mean_current": True,
        "carrier_admitted_as_evidence_does_not_mean_current": True,
        "carrier_corresponded_does_not_mean_current": True,
        "carrier_divergent_does_not_mean_current": True,
        "selected_evidence_remains_downstream": True,
    }


def _currentness_basis(
    request: Mapping[str, Any],
    body_posture: Mapping[str, Any],
    selected_evidence: Sequence[Mapping[str, Any]],
    intent: str | None,
) -> dict[str, Any]:
    return {
        "currentness_question": request.get("currentness_question"),
        "participation_intent": intent,
        "selected_body_current_posture_declared": bool(
            body_posture.get("body_current_posture_declared")
        ),
        "selected_body_current_posture": copy.deepcopy(dict(body_posture)),
        "currentness_basis": copy.deepcopy(_as_mapping(request.get("currentness_basis"))),
        "lineage_basis": copy.deepcopy(request.get("lineage_basis")),
        "selected_admission_basis": copy.deepcopy(
            request.get("selected_admission_basis")
        ),
        "selected_correspondence_basis": copy.deepcopy(
            request.get("selected_correspondence_basis")
        ),
        "selected_divergence_basis": copy.deepcopy(
            request.get("selected_divergence_basis")
        ),
        "selected_evidence_ids": [
            item.get("evidence_id") for item in selected_evidence
        ],
        "selected_evidence_outcomes": [
            item.get("evidence_outcome") for item in selected_evidence
        ],
        "selected_carrier_ids": [item.get("carrier_id") for item in selected_evidence],
        "admission_status_required": _admission_status_required(
            request,
            selected_evidence,
        ),
        "divergence_status_required": _divergence_status_required(
            request,
            selected_evidence,
        ),
        "admission_statuses": [
            item.get("admission_status") for item in selected_evidence
        ],
        "correspondence_statuses": [
            item.get("correspondence_status") for item in selected_evidence
        ],
        "divergence_statuses": [
            item.get("divergence_status") for item in selected_evidence
        ],
        "hidden_divergence": False,
        "refusal_hidden": False,
        "currentness_participation_is_not_currentness_creation": True,
        "carrier_evidence_is_not_current_by_itself": True,
        "currentness_not_derived_from": {
            "latest_file": True,
            "newest_timestamp": True,
            "local_copy": True,
            "possession": True,
            "return": True,
            "receipt": True,
            "admission": True,
            "correspondence": True,
            "divergence": True,
            "majority_carriers": True,
            "successful_receipt_count": True,
            "successful_admission_count": True,
            "carrier_availability": True,
            "carrier_label": True,
            "convenience": True,
        },
        "required_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }


def _currentness_participation_result(
    outcome: str,
    request: Mapping[str, Any],
    selected_evidence: Sequence[Mapping[str, Any]],
    body_posture: Mapping[str, Any],
    block_code: str | None,
    block_reason: str | None,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    admission_available = any(item.get("admission_status") for item in selected_evidence)
    correspondence_available = any(
        item.get("correspondence_status") for item in selected_evidence
    )
    divergence_available = any(
        item.get("divergence_status") for item in selected_evidence
    )
    visible_divergence_available = any(
        item.get("visible_divergence") is True for item in selected_evidence
    )
    base = {
        "selected_evidence_count": len(selected_evidence),
        "selected_evidence_ids": [
            item.get("evidence_id") for item in selected_evidence
        ],
        "selected_evidence_outcomes": [
            item.get("evidence_outcome") for item in selected_evidence
        ],
        "selected_carrier_ids": [item.get("carrier_id") for item in selected_evidence],
        "participation_is_not_currentness_creation": True,
        "body_side_current_posture_declared": bool(
            body_posture.get("body_current_posture_declared")
        ),
        "selected_carrier_evidence_preserved": bool(selected_evidence),
        "selected_evidence_remains_downstream": True,
        "admission_status_preserved": admission_available,
        "correspondence_status_preserved": correspondence_available,
        "divergence_status_preserved": divergence_available,
        "visible_divergence_preserved": visible_divergence_available,
        "hidden_divergence": False,
        "carrier_evidence_became_current": False,
        "currentness_created_by_carrier": False,
        "source_not_replaced": True,
        "authority_not_created": True,
        "permission_not_created": True,
        "successor_not_created": True,
        "body_not_created": True,
        "carrier_hierarchy_not_created": True,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "multi_carrier_law_not_created": True,
        "distributed_standing_not_created": True,
        "presence_threshold_truth_action_consequence_not_created": True,
        "continuation_not_authorized": True,
    }
    if outcome == CURRENTNESS_PARTICIPATION_ELIGIBLE:
        base.update(
            {
                "currentness_participation_eligible": True,
                "selected_evidence_may_participate": True,
                "currentness_participation_excluded": False,
                "selected_evidence_preserved": True,
            }
        )
    elif outcome == CURRENTNESS_PARTICIPATION_EXCLUDED:
        base.update(
            {
                "currentness_participation_eligible": False,
                "selected_evidence_may_participate": False,
                "currentness_participation_excluded": True,
                "selected_evidence_preserved": True,
                "exclusion_reason": _first_text(
                    request,
                    ("exclusion_reason", "participation_exclusion_reason"),
                )
                or "selected evidence is excluded for the declared currentness question",
            }
        )
    else:
        base.update(
            {
                "currentness_participation_eligible": False,
                "selected_evidence_may_participate": False,
                "currentness_participation_excluded": False,
                "block_code": block_code,
                "block_reason": block_reason,
                "failed_checks": [
                    copy.deepcopy(dict(check))
                    for check in checks
                    if check.get("passed") is False
                ],
                "selected_basis_preserved_where_available": True,
            }
        )
    return base


def _normalize_body_current_posture(raw_posture: Any) -> dict[str, Any]:
    if isinstance(raw_posture, Mapping):
        posture = _as_mapping(raw_posture)
        posture_id = _first_text(
            posture,
            (
                "body_current_posture_id",
                "current_posture_id",
                "posture_id",
                "id",
                "result_id",
            ),
        )
        label = _first_text(
            posture,
            ("body_current_posture_label", "current_posture_label", "label", "name"),
        )
        outcome = _first_text(posture, ("outcome", "status", "result_outcome"))
        return {
            "body_current_posture_declared": bool(posture),
            "body_current_posture_id": posture_id,
            "body_current_posture_label": label,
            "body_current_posture_outcome": outcome,
            "raw_body_current_posture": posture,
        }
    if isinstance(raw_posture, str) and raw_posture.strip():
        return {
            "body_current_posture_declared": True,
            "body_current_posture_id": None,
            "body_current_posture_label": raw_posture.strip(),
            "body_current_posture_outcome": None,
            "raw_body_current_posture": raw_posture.strip(),
        }
    return {
        "body_current_posture_declared": False,
        "body_current_posture_id": None,
        "body_current_posture_label": None,
        "body_current_posture_outcome": None,
        "raw_body_current_posture": copy.deepcopy(raw_posture),
    }


def _normalize_selected_carrier_evidence(raw_evidence: Any) -> list[dict[str, Any]]:
    if isinstance(raw_evidence, Mapping):
        raw_items = [raw_evidence]
    elif isinstance(raw_evidence, list):
        raw_items = raw_evidence
    else:
        return []

    normalized: list[dict[str, Any]] = []
    for index, raw_item in enumerate(raw_items):
        if not isinstance(raw_item, Mapping):
            continue
        item = _as_mapping(raw_item)
        carrier = _as_mapping(
            item.get("carrier")
            or item.get("selected_carrier")
            or item.get("emitting_carrier")
            or item.get("receiving_carrier")
        )
        admission_basis = _as_mapping(
            item.get("admission_basis") or item.get("selected_admission_basis")
        )
        correspondence_basis = _as_mapping(
            item.get("correspondence_basis")
            or item.get("selected_correspondence_basis")
        )
        divergence_basis = _as_mapping(
            item.get("divergence_basis") or item.get("selected_divergence_basis")
        )
        return_basis = _as_mapping(item.get("return_basis"))
        integrity = _as_mapping(
            item.get("integrity_evidence")
            or item.get("integrity")
            or item.get("carried_surface_integrity")
        )
        block = _as_mapping(item.get("block"))
        non_claims = _as_mapping(item.get("non_claims"))
        evidence_outcome = _first_text(
            item,
            (
                "evidence_outcome",
                "outcome",
                "status",
                "emission_outcome",
                "receipt_outcome",
                "admission_outcome",
                "divergence_outcome",
                "result_outcome",
            ),
        )
        divergence_status = _first_text(
            item,
            ("divergence_status", "divergence_outcome", "carrier_divergence_status"),
        ) or _first_text(divergence_basis, ("divergence_status", "outcome", "status"))
        normalized.append(
            {
                "evidence_index": index,
                "evidence_id": _first_text(
                    item,
                    (
                        "evidence_id",
                        "id",
                        "selected_evidence_id",
                        "carrier_evidence_id",
                        "emission_id",
                        "receipt_id",
                        "admission_id",
                        "divergence_id",
                        "surface_id",
                        "result_id",
                    ),
                ),
                "evidence_outcome": evidence_outcome,
                "normalized_evidence_outcome": _normalize_token(evidence_outcome),
                "carrier_id": _first_text(
                    item,
                    (
                        "carrier_id",
                        "selected_carrier_id",
                        "emitting_carrier_id",
                        "receiving_carrier_id",
                        "source_carrier_id",
                    ),
                )
                or _first_text(carrier, ("carrier_id", "id", "carrier_identifier")),
                "carrier_role": _normalize_token(
                    _first_text(
                        item,
                        ("carrier_role", "role", "declared_carrier_role"),
                    )
                    or _first_text(carrier, ("carrier_role", "role"))
                ),
                "emission_class": _normalize_token(
                    _first_text(
                        item,
                        (
                            "emission_class",
                            "declared_emission_class",
                            "carrier_emission_class",
                        ),
                    )
                ),
                "source_or_carried_basis": copy.deepcopy(
                    _selected_source_or_carried_basis(item)
                ),
                "admission_status": _first_text(
                    item,
                    ("admission_status", "admission_outcome", "admitted_status"),
                )
                or _first_text(admission_basis, ("admission_status", "outcome", "status")),
                "correspondence_status": _first_text(
                    item,
                    (
                        "correspondence_status",
                        "correspondence_outcome",
                        "corresponded_status",
                    ),
                )
                or _first_text(
                    correspondence_basis,
                    ("correspondence_status", "outcome", "status"),
                ),
                "divergence_status": divergence_status,
                "visible_divergence": _visible_divergence(item, divergence_basis),
                "return_path": _first_text(item, ("return_path",))
                or _first_text(return_basis, ("return_path", "path")),
                "return_context": copy.deepcopy(
                    item.get("return_context")
                    if "return_context" in item
                    else return_basis.get("return_context")
                ),
                "integrity_hash": _first_text(
                    item,
                    ("integrity_hash", "hash", "sha256", "content_hash"),
                )
                or _first_text(
                    integrity,
                    ("integrity_hash", "hash", "sha256", "content_hash"),
                ),
                "integrity_status": _first_text(
                    item,
                    ("integrity_status", "integrity_outcome", "hash_status"),
                )
                or _first_text(integrity, ("integrity_status", "outcome", "status")),
                "block_code": _first_text(item, ("block_code", "code"))
                or _first_text(block, ("block_code", "code")),
                "block_reason": _first_text(item, ("block_reason", "reason"))
                or _first_text(block, ("block_reason", "reason")),
                "non_claims": non_claims,
                "raw_evidence": copy.deepcopy(dict(item)),
            }
        )
    return normalized


def _selected_source_or_carried_basis(item: Mapping[str, Any]) -> Any:
    for key in (
        "source_or_carried_basis",
        "source_carried_basis",
        "carried_surface_basis",
        "source_basis",
        "selected_basis",
        "basis",
    ):
        if key in item:
            return copy.deepcopy(item.get(key))
    for key in ("basis_id", "source_basis_id", "carried_surface_id", "surface_id"):
        if key in item:
            return {key: copy.deepcopy(item.get(key))}
    return None


def _visible_divergence(
    item: Mapping[str, Any],
    divergence_basis: Mapping[str, Any],
) -> bool:
    if _flag_true([item, divergence_basis], ("visible_divergence", "mismatch_visible")):
        return True
    status = _normalize_token(
        _first_text(item, ("divergence_status",))
        or _first_text(divergence_basis, ("divergence_status", "outcome", "status"))
    )
    return bool(status and "DIVERGENCE" in status and "NO_" not in status)


def _admission_status_required(
    request: Mapping[str, Any],
    selected_evidence: Sequence[Mapping[str, Any]],
) -> bool:
    basis = _as_mapping(request.get("currentness_basis"))
    if _flag_true(
        [request, basis],
        ("admission_status_required", "require_admission_status"),
    ):
        return True
    if isinstance(request.get("selected_admission_basis"), Mapping):
        return True
    return any(
        _flag_true(
            [item, _as_mapping(item.get("raw_evidence"))],
            ("admission_status_required", "requires_admission_status"),
        )
        for item in selected_evidence
    )


def _divergence_status_required(
    request: Mapping[str, Any],
    selected_evidence: Sequence[Mapping[str, Any]],
) -> bool:
    basis = _as_mapping(request.get("currentness_basis"))
    if _flag_true(
        [request, basis],
        ("divergence_status_required", "require_divergence_status"),
    ):
        return True
    if isinstance(request.get("selected_divergence_basis"), Mapping):
        return True
    return any(
        item.get("visible_divergence") is True
        or _flag_true(
            [item, _as_mapping(item.get("raw_evidence"))],
            ("divergence_status_required", "requires_divergence_status"),
        )
        for item in selected_evidence
    )


def _lineage_basis_preserved(lineage_basis: Any) -> bool:
    if lineage_basis is None:
        return True
    if isinstance(lineage_basis, Mapping):
        return bool(lineage_basis)
    if isinstance(lineage_basis, str):
        return bool(lineage_basis.strip())
    return True


def _status_unknown(value: Any) -> bool:
    token = _normalize_token(value)
    return token in {"UNKNOWN", "UNDECLARED", "MISSING", "NOT_DECLARED"}


def _status_unknown_or_unresolved(value: Any) -> bool:
    token = _normalize_token(value)
    return token in {
        "UNKNOWN",
        "UNDECLARED",
        "MISSING",
        "NOT_DECLARED",
        "UNRESOLVED",
        "HIDDEN",
        "HIDDEN_DIVERGENCE",
    }


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    target = Path(path)
    try:
        loaded = json.loads(target.read_text(encoding="utf-8"))
    except OSError as exc:
        raise CrossCarrierCurrentnessBoundaryError(
            "DECLARED_CURRENTNESS_REQUEST_UNREADABLE",
            BLOCK_REASONS["DECLARED_CURRENTNESS_REQUEST_UNREADABLE"],
        ) from exc
    except json.JSONDecodeError as exc:
        raise CrossCarrierCurrentnessBoundaryError(
            "DECLARED_CURRENTNESS_REQUEST_MALFORMED",
            BLOCK_REASONS["DECLARED_CURRENTNESS_REQUEST_MALFORMED"],
        ) from exc
    if not isinstance(loaded, Mapping):
        raise CrossCarrierCurrentnessBoundaryError(
            "DECLARED_CURRENTNESS_REQUEST_MALFORMED",
            BLOCK_REASONS["DECLARED_CURRENTNESS_REQUEST_MALFORMED"],
        )
    return copy.deepcopy(dict(loaded))


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


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is False:
            return check
    return None


def _block_reason(
    block_code: str | None,
    failed_check: Mapping[str, Any] | None,
) -> str | None:
    if block_code is None:
        return None
    if failed_check and failed_check.get("expected_posture"):
        return BLOCK_REASONS.get(block_code, str(failed_check.get("expected_posture")))
    return BLOCK_REASONS.get(block_code, block_code)


def _requested_block_code(request: Mapping[str, Any]) -> str | None:
    block = _as_mapping(request.get("block"))
    for source in (request, block):
        for key in (
            "bounded_block_code",
            "declared_block_code",
            "requested_block_code",
            "block_code",
            "code",
        ):
            value = _normalize_token(source.get(key))
            if value:
                return value
    return None


def _result_id(
    request: Mapping[str, Any],
    intent: str | None,
    outcome: str,
) -> str:
    base = (
        _first_text(request, ("currentness_request_id", "request_id", "id"))
        or intent
        or "cross_carrier_currentness"
    )
    return f"{_safe_filename_part(base)}__{_safe_filename_part(outcome)}"


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            {
                "item": item,
                "scheduled": False,
                "authorized": False,
                "executed": False,
            }
            for item in OPEN_SURFACES
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _missing_or_flipped_non_claims(
    declared_non_claims: Mapping[str, Any],
) -> list[dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    for key, expected in REQUIRED_NON_CLAIMS.items():
        if key not in declared_non_claims:
            failures.append(
                {"non_claim": key, "reason": "missing", "expected": expected}
            )
        elif _truthy(declared_non_claims.get(key)) != expected:
            failures.append(
                {
                    "non_claim": key,
                    "reason": "flipped",
                    "expected": expected,
                    "actual": declared_non_claims.get(key),
                }
            )
    return failures


def _selected_non_claim_collapse(
    selected_evidence: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    for item in selected_evidence:
        non_claims = _as_mapping(item.get("non_claims"))
        for key in REQUIRED_NON_CLAIMS:
            if key in non_claims and _truthy(non_claims.get(key)):
                failures.append(
                    {
                        "evidence_id": item.get("evidence_id"),
                        "non_claim": key,
                        "actual": non_claims.get(key),
                    }
                )
    return failures


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "currentness_created_by_carrier",
        "carrier_evidence_became_current",
        "source_replaced",
        "authority_created",
        "permission_created",
        "latest_file_currentness",
        "newest_timestamp_currentness",
        "majority_carrier_currentness",
        "successful_receipt_count_currentness",
        "successful_admission_count_currentness",
        "winning_carrier_selected",
        "losing_carrier_invalidated",
        "carrier_hierarchy_created",
        "multi_carrier_law_created",
        "distributed_standing_created",
        "continuation_authorized",
    )
    return {key: copy.deepcopy(non_claims.get(key)) for key in keys}


def _flag_true(sources: Sequence[Any], aliases: Sequence[str]) -> bool:
    return any(_truthy(value) for value in _find_key_values(sources, aliases))


def _flag_snapshot(sources: Sequence[Any], aliases: Sequence[str]) -> dict[str, Any]:
    snapshot: dict[str, Any] = {}
    for alias in aliases:
        values = _find_key_values(sources, (alias,))
        if values:
            snapshot[alias] = copy.deepcopy(values)
    return snapshot


def _find_key_values(value: Any, aliases: Sequence[str]) -> list[Any]:
    values: list[Any] = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            if key in aliases:
                values.append(item)
            values.extend(_find_key_values(item, aliases))
    elif isinstance(value, list):
        for item in value:
            values.extend(_find_key_values(item, aliases))
    return values


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "1", "yes", "y", "on"}
    if isinstance(value, (int, float)):
        return value != 0
    return bool(value)


def _first_text(source: Mapping[str, Any], keys: Sequence[str]) -> str | None:
    for key in keys:
        value = source.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if value is not None and not isinstance(value, (Mapping, list)):
            text = str(value).strip()
            if text:
                return text
    return None


def _normalize_token(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    chars: list[str] = []
    previous_underscore = False
    for char in text:
        if char.isalnum():
            chars.append(char.upper())
            previous_underscore = False
        elif not previous_underscore:
            chars.append("_")
            previous_underscore = True
    normalized = "".join(chars).strip("_")
    return normalized or None


def _safe_filename_part(value: Any) -> str:
    text = str(value or "").strip().lower()
    chars: list[str] = []
    previous_underscore = False
    for char in text:
        if char.isalnum():
            chars.append(char)
            previous_underscore = False
        elif not previous_underscore:
            chars.append("_")
            previous_underscore = True
    safe = "".join(chars).strip("_")
    return safe or "cross_carrier_currentness"


def _raw_evidence_shape(raw_evidence: Any) -> Any:
    if isinstance(raw_evidence, list):
        return [type(item).__name__ for item in raw_evidence]
    return type(raw_evidence).__name__


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]


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


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
