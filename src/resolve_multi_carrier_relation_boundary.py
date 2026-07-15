"""Bounded multi-carrier relation boundary resolver.

This resolver records whether selected carriers or carrier-evidence surfaces
stand in bounded body-side relation for one declared relation question. It does
not create source, currentness, authority, permission, carrier hierarchy,
distributed standing, synchronization, body formation, truth, action,
consequence, or continuation.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class MultiCarrierRelationBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit relation inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


MULTI_CARRIER_RELATION_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_multi_carrier_relation_boundary"
)
RESOLVER_MODULE = "resolve_multi_carrier_relation_boundary"
RESULT_VERSION = "0.1.0"

MULTI_CARRIER_RELATION_RECOGNIZED = "MULTI_CARRIER_RELATION_RECOGNIZED"
NO_MULTI_CARRIER_RELATION = "NO_MULTI_CARRIER_RELATION"
MULTI_CARRIER_RELATION_BLOCKED = "MULTI_CARRIER_RELATION_BLOCKED"

SUPPORTED_RELATION_TYPES = {
    "SOURCE_RECEIVER_RELATION",
    "RECEIPT_RETURN_RELATION",
    "ADMITTED_EVIDENCE_RELATION",
    "REFUSAL_SUCCESS_RELATION",
    "DIVERGENCE_BOUNDED_RELATION",
    "CURRENTNESS_PARTICIPATION_RELATION",
    "ROLE_EMISSION_RELATION",
    "CARRIER_EVIDENCE_SET_RELATION",
    "NO_MULTI_CARRIER_RELATION",
}

ADMITTED_CARRIER_ROLES = {
    "SOURCE_CARRIER_FOR_PACKET",
    "RECEIVING_CARRIER",
    "HOLDING_CARRIER",
    "RETURNING_CARRIER",
    "REFUSING_CARRIER",
}
CANDIDATE_CARRIER_ROLES = {
    "WITNESS_CARRIER",
    "COMPARISON_CARRIER",
    "EMITTING_CARRIER",
    "STALE_CARRIER",
    "SUCCESSOR_CARRIER",
}

SUCCESS_OUTCOME_HINTS = {
    "ADMITTED",
    "CARRIER_DIVERGENCE_RECORDED",
    "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
    "CARRIER_EMISSION_RECOGNIZED",
    "CARRIER_ROLE_RECOGNIZED",
    "CARRIED_SURFACE_RECEIVED",
    "CORRESPONDENCE_RECOGNIZED",
    "CURRENTNESS_PARTICIPATION_ELIGIBLE",
    "ELIGIBLE",
    "PASS",
    "PASSED",
    "RECEIVED",
    "RECOGNIZED",
    "SUCCESS",
    "SUCCESSFUL",
}
REFUSAL_OUTCOME_HINTS = {
    "BLOCKED",
    "FAILED",
    "FAILURE",
    "REFUSAL",
    "REFUSED",
    "RECEIPT_BLOCK",
    "RECEIPT_REFUSAL_REASON",
    "RETURNED_BLOCKED_RECEIPT_EVIDENCE",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "carrier_relation_created_source": False,
    "carrier_relation_created_currentness": False,
    "carrier_relation_created_authority": False,
    "carrier_relation_created_permission": False,
    "carrier_relation_created_successor": False,
    "carrier_relation_created_body": False,
    "carrier_relation_created_hierarchy": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "divergence_hidden": False,
    "refusal_hidden": False,
    "mismatch_hidden": False,
    "evidence_overwritten": False,
    "evidence_merged_into_source": False,
    "distributed_standing_created": False,
    "carrier_registry_created": False,
    "repository_synchronization_created": False,
    "signal_created_by_default": False,
    "presence_established": False,
    "threshold_met": False,
    "truth_created": False,
    "action_authorized": False,
    "consequence_created": False,
    "continuation_authorized": False,
    "divergence_resolved_by_majority": False,
    "divergence_resolved_by_latest_file": False,
    "divergence_resolved_by_success_count": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "DECLARED_RELATION_REQUEST_MISSING": "No declared relation request was supplied.",
    "DECLARED_RELATION_REQUEST_UNREADABLE": "The declared relation request path could not be read.",
    "DECLARED_RELATION_REQUEST_MALFORMED": "The declared relation request is not a JSON object or mapping.",
    "RELATION_QUESTION_UNDECLARED": "Relation question is undeclared.",
    "INSUFFICIENT_SELECTED_CARRIERS_OR_EVIDENCE": "At least two selected carrier roles, carrier identities, or evidence surfaces are required.",
    "SELECTED_CARRIER_EVIDENCE_MISSING": "Selected carriers or selected carrier evidence are missing.",
    "SELECTED_CARRIER_EVIDENCE_MALFORMED": "Selected carriers or selected carrier evidence are malformed.",
    "EVIDENCE_IDENTITY_MISSING": "Selected evidence identity is missing.",
    "EVIDENCE_OUTCOME_MISSING": "Selected evidence outcome or status is missing.",
    "CARRIER_IDENTITY_MISSING": "Carrier identity is missing where required.",
    "CARRIER_ROLE_UNSUPPORTED": "Carrier role is unsupported or unbounded.",
    "RELATION_TYPE_UNSUPPORTED": "Relation type is unsupported.",
    "RELATION_HIDES_DIVERGENCE": "Relation hides divergence.",
    "RELATION_HIDES_REFUSAL": "Relation hides refusal.",
    "RELATION_OVERWRITES_EVIDENCE": "Relation overwrites evidence.",
    "RELATION_MUTATES_OR_REPLAYS_EVIDENCE": "Relation mutates, replays, or merges evidence.",
    "RELATION_REPLACES_SOURCE": "Relation replaces source.",
    "RELATION_CREATES_CURRENTNESS": "Relation creates currentness.",
    "RELATION_CREATES_AUTHORITY": "Relation creates authority.",
    "RELATION_CREATES_PERMISSION": "Relation creates permission.",
    "RELATION_CREATES_SUCCESSOR": "Relation creates successor standing.",
    "RELATION_CREATES_BODY": "Relation creates body formation.",
    "RELATION_CREATES_CARRIER_HIERARCHY": "Relation creates carrier hierarchy.",
    "RELATION_SELECTS_WINNING_CARRIER": "Relation selects a winning carrier.",
    "RELATION_INVALIDATES_LOSING_CARRIER": "Relation invalidates a losing carrier.",
    "RELATION_CREATES_SIGNAL_BY_DEFAULT": "Relation creates signal by default.",
    "RELATION_ESTABLISHES_PRESENCE": "Relation establishes presence.",
    "RELATION_ESTABLISHES_THRESHOLD": "Relation establishes threshold.",
    "RELATION_CREATES_TRUTH": "Relation creates truth.",
    "RELATION_AUTHORIZES_ACTION": "Relation authorizes action.",
    "RELATION_CREATES_CONSEQUENCE": "Relation creates consequence.",
    "RELATION_CREATES_DISTRIBUTED_STANDING": "Relation creates distributed standing.",
    "RELATION_AUTHORIZES_CONTINUATION": "Relation authorizes continuation.",
    "RELATION_RESOLVES_DIVERGENCE_BY_MAJORITY": "Relation resolves divergence by majority.",
    "RELATION_RESOLVES_DIVERGENCE_BY_LATEST_FILE": "Relation resolves divergence by latest file.",
    "RELATION_RESOLVES_DIVERGENCE_BY_SUCCESS_COUNT": "Relation resolves divergence by success count.",
    "LATEST_FILE_CURRENTNESS": "Latest-file recency is treated as currentness.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required relation non-claim is missing or flipped.",
}

RELATION_NON_MEANING = {
    "does_not_mean_source_replacement": True,
    "does_not_mean_currentness": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_successor_standing": True,
    "does_not_mean_body_formation": True,
    "does_not_mean_carrier_hierarchy": True,
    "does_not_mean_carrier_priority": True,
    "does_not_mean_carrier_sovereignty": True,
    "does_not_mean_winning_carrier": True,
    "does_not_mean_losing_carrier_invalidated": True,
    "does_not_mean_distributed_standing": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_carrier_registry": True,
    "does_not_mean_signal_by_default": True,
    "does_not_mean_presence": True,
    "does_not_mean_threshold": True,
    "does_not_mean_truth": True,
    "does_not_mean_action": True,
    "does_not_mean_consequence": True,
    "does_not_mean_continuation": True,
    "does_not_mean_divergence_resolution": True,
    "does_not_mean_majority_rule": True,
    "does_not_mean_latest_file_rule": True,
    "does_not_mean_success_count_rule": True,
    "does_not_mean_current_carrier_selection": True,
}

OPEN_SURFACES = [
    "multi-carrier relation implementation refinement",
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

ANTI_COLLAPSE_CHECKS = (
    ("visible_divergence_preserved_where_applicable", ("relation_hides_divergence", "divergence_hidden", "hidden_divergence"), "visible divergence remains visible where applicable", "RELATION_HIDES_DIVERGENCE"),
    ("hidden_divergence_false", ("relation_hides_divergence", "divergence_hidden", "hidden_divergence"), "hidden divergence is false", "RELATION_HIDES_DIVERGENCE"),
    ("refusal_hidden_false", ("relation_hides_refusal", "refusal_hidden", "hidden_refusal"), "refusal hidden is false", "RELATION_HIDES_REFUSAL"),
    ("relation_does_not_overwrite_evidence", ("relation_overwrites_evidence", "evidence_overwritten", "evidence_erased"), "relation overwrites no evidence", "RELATION_OVERWRITES_EVIDENCE"),
    ("relation_does_not_mutate_replay_or_merge_evidence", ("relation_mutates_evidence", "relation_replays_evidence", "relation_merges_evidence", "mutation_performed", "replay_performed", "merge_performed"), "relation performs no mutation, replay, or merge", "RELATION_MUTATES_OR_REPLAYS_EVIDENCE"),
    ("relation_does_not_replace_source", ("relation_replaces_source", "source_replaced", "carrier_relation_created_source", "evidence_merged_into_source"), "relation replaces no source", "RELATION_REPLACES_SOURCE"),
    ("relation_does_not_create_currentness", ("relation_creates_currentness", "currentness_created", "carrier_relation_created_currentness", "currentness_from_relation"), "relation creates no currentness", "RELATION_CREATES_CURRENTNESS"),
    ("relation_does_not_create_authority", ("relation_creates_authority", "authority_created", "carrier_relation_created_authority"), "relation creates no authority", "RELATION_CREATES_AUTHORITY"),
    ("relation_does_not_create_permission", ("relation_creates_permission", "permission_created", "carrier_relation_created_permission"), "relation creates no permission", "RELATION_CREATES_PERMISSION"),
    ("relation_does_not_create_successor_body", ("relation_creates_successor", "carrier_relation_created_successor", "successor_standing_created", "relation_creates_body", "carrier_relation_created_body", "body_created", "body_formed"), "relation creates no successor standing or body", "RELATION_CREATES_SUCCESSOR"),
    ("relation_does_not_create_carrier_hierarchy", ("relation_creates_carrier_hierarchy", "carrier_relation_created_hierarchy", "carrier_hierarchy_created"), "relation creates no carrier hierarchy", "RELATION_CREATES_CARRIER_HIERARCHY"),
    ("relation_does_not_select_winning_carrier", ("winning_carrier_selected", "relation_selects_winning_carrier"), "relation selects no winning carrier", "RELATION_SELECTS_WINNING_CARRIER"),
    ("relation_does_not_invalidate_losing_carrier", ("losing_carrier_invalidated", "relation_invalidates_losing_carrier"), "relation invalidates no losing carrier", "RELATION_INVALIDATES_LOSING_CARRIER"),
    ("relation_does_not_create_signal_by_default", ("signal_created_by_default", "relation_creates_signal_by_default"), "relation creates no signal by default", "RELATION_CREATES_SIGNAL_BY_DEFAULT"),
    ("relation_does_not_establish_presence_threshold", ("presence_established", "threshold_met", "relation_establishes_presence", "relation_establishes_threshold"), "relation establishes no presence or threshold", "RELATION_ESTABLISHES_PRESENCE"),
    ("relation_does_not_create_truth", ("truth_created", "relation_creates_truth"), "relation creates no truth", "RELATION_CREATES_TRUTH"),
    ("relation_does_not_authorize_action_create_consequence", ("action_authorized", "consequence_created", "relation_authorizes_action", "relation_creates_consequence"), "relation authorizes no action and creates no consequence", "RELATION_AUTHORIZES_ACTION"),
    ("relation_does_not_create_distributed_standing", ("distributed_standing_created", "relation_creates_distributed_standing"), "relation creates no distributed standing", "RELATION_CREATES_DISTRIBUTED_STANDING"),
    ("relation_does_not_authorize_continuation", ("continuation_authorized", "relation_authorizes_continuation", "follow_on_work_authorized", "follow_on_steps_authorized"), "relation authorizes no continuation", "RELATION_AUTHORIZES_CONTINUATION"),
    ("relation_does_not_resolve_divergence_by_majority_latest_success_count", ("divergence_resolved_by_majority", "relation_resolves_divergence_by_majority", "divergence_resolved_by_latest_file", "relation_resolves_divergence_by_latest_file", "divergence_resolved_by_success_count", "relation_resolves_divergence_by_success_count"), "relation does not resolve divergence by majority, latest file, or success count", "RELATION_RESOLVES_DIVERGENCE_BY_MAJORITY"),
    ("latest_file_currentness_false", ("latest_file_currentness", "latest_file_recency_currentness"), "latest local file is not currentness", "LATEST_FILE_CURRENTNESS"),
    ("recency_fraud_false", ("recency_fraud", "recency_currentness"), "recency is not used as currentness", "LATEST_FILE_CURRENTNESS"),
)


def resolve_multi_carrier_relation_boundary(
    declared_relation_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one declared multi-carrier relation request."""

    if declared_relation_request is None:
        return _resolve_request({}, ["DECLARED_RELATION_REQUEST_MISSING"])
    if not isinstance(declared_relation_request, Mapping):
        return _resolve_request({}, ["DECLARED_RELATION_REQUEST_MALFORMED"])
    return _resolve_request(copy.deepcopy(dict(declared_relation_request)), [])


def resolve_multi_carrier_relation_boundary_from_path(
    declared_relation_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one declared relation request JSON path."""

    try:
        request = _read_json_mapping(declared_relation_request_path)
        request["_declared_relation_request_path"] = str(Path(declared_relation_request_path))
        return _resolve_request(request, [])
    except MultiCarrierRelationBoundaryError as exc:
        return _resolve_request({}, [exc.block_code])


def write_multi_carrier_relation_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded relation result artifact without overwriting."""

    if output_path is None:
        question = _as_mapping(result.get("declared_relation_question"))
        basis_id = question.get("relation_request_id") or question.get("relation_type") or "multi_carrier_relation"
        output_path = MULTI_CARRIER_RELATION_BOUNDARY_ROOT / (
            f"{_safe_filename_part(basis_id)}__multi_carrier_relation_result.json"
        )
    target = _non_overwriting_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    return target


def build_multi_carrier_relation_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact bounded summary for a relation result."""

    checks = _mapping_list(result.get("relation_checks"))
    question = _as_mapping(result.get("declared_relation_question"))
    relation = _as_mapping(result.get("relation_result"))
    non_claims = _as_mapping(result.get("non_claims"))
    block = _as_mapping(result.get("block"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "relation_request_id": question.get("relation_request_id"),
        "relation_question": question.get("relation_question"),
        "relation_type": question.get("relation_type"),
        "relation_recognized": bool(relation.get("multi_carrier_relation_recognized")),
        "no_relation": bool(relation.get("no_multi_carrier_relation")),
        "selected_carrier_count": relation.get("selected_carrier_count"),
        "selected_evidence_count": relation.get("selected_evidence_count"),
        "selected_carrier_ids": copy.deepcopy(relation.get("selected_carrier_ids")),
        "selected_evidence_ids": copy.deepcopy(relation.get("selected_evidence_ids")),
        "selected_evidence_outcomes": copy.deepcopy(relation.get("selected_evidence_outcomes")),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "carrier_roles_preserved": bool(relation.get("carrier_roles_preserved")),
        "evidence_identities_preserved": bool(relation.get("evidence_identities_preserved")),
        "local_outcomes_preserved": bool(relation.get("local_outcomes_preserved")),
        "visible_refusal_preserved": bool(relation.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(relation.get("visible_divergence_preserved")),
        "downstream_evidence_posture_preserved": bool(relation.get("downstream_evidence_posture_preserved")),
        "current_carrier_not_selected": bool(relation.get("current_carrier_not_selected")),
        "winning_carrier_selected": bool(non_claims.get("winning_carrier_selected")),
        "losing_carrier_invalidated": bool(non_claims.get("losing_carrier_invalidated")),
        "source_created": bool(non_claims.get("source_replaced")),
        "currentness_created": bool(non_claims.get("currentness_created")),
        "authority_created": bool(non_claims.get("authority_created")),
        "permission_created": bool(non_claims.get("permission_created")),
        "source_currentness_authority_permission_created": bool(non_claims.get("source_replaced") or non_claims.get("currentness_created") or non_claims.get("authority_created") or non_claims.get("permission_created")),
        "carrier_hierarchy_created": bool(non_claims.get("carrier_relation_created_hierarchy")),
        "distributed_standing_created": bool(non_claims.get("distributed_standing_created")),
        "presence_created": bool(non_claims.get("presence_established")),
        "threshold_created": bool(non_claims.get("threshold_met")),
        "truth_created": bool(non_claims.get("truth_created")),
        "action_authorized": bool(non_claims.get("action_authorized")),
        "consequence_created": bool(non_claims.get("consequence_created")),
        "presence_threshold_truth_action_consequence_created": bool(non_claims.get("presence_established") or non_claims.get("threshold_met") or non_claims.get("truth_created") or non_claims.get("action_authorized") or non_claims.get("consequence_created")),
        "continuation_authorized": bool(non_claims.get("continuation_authorized")),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_declared_relation_request(
    relation_request_id: str,
    relation_question: str,
    relation_type: str,
    selected_carrier_evidence: Sequence[Mapping[str, Any]],
    selected_carriers: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Build a minimum declared relation request."""

    return {
        "relation_request_id": relation_request_id,
        "relation_question": relation_question,
        "relation_type": _normalize_token(relation_type) or relation_type,
        "selected_carriers": [copy.deepcopy(dict(item)) for item in (selected_carriers or [])],
        "selected_carrier_evidence": [copy.deepcopy(dict(item)) for item in selected_carrier_evidence],
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }


def _resolve_request(request: Mapping[str, Any], precheck_failures: Sequence[str]) -> dict[str, Any]:
    request = _as_mapping(request)
    raw_carriers = request.get("selected_carriers")
    raw_evidence = request.get("selected_carrier_evidence")
    selected_carriers = _normalize_carriers(raw_carriers)
    selected_evidence = _normalize_evidence(raw_evidence)
    relation_type = _normalize_token(request.get("relation_type"))
    detection = _detect_relation(request, relation_type, selected_carriers, selected_evidence)
    checks = _build_checks(
        request,
        raw_carriers,
        raw_evidence,
        selected_carriers,
        selected_evidence,
        relation_type,
        detection,
        _as_mapping(request.get("declared_non_claims")),
        precheck_failures,
    )
    failed = _first_failed(checks)
    if failed:
        outcome = MULTI_CARRIER_RELATION_BLOCKED
        block_code = str(failed.get("block_code"))
    elif relation_type == "NO_MULTI_CARRIER_RELATION":
        outcome = NO_MULTI_CARRIER_RELATION
        block_code = None
    elif detection.get("relation_supported"):
        outcome = MULTI_CARRIER_RELATION_RECOGNIZED
        block_code = None
    else:
        outcome = NO_MULTI_CARRIER_RELATION
        block_code = None
    block_reason = _block_reason(block_code)
    result: dict[str, Any] = {
        "multi_carrier_relation_metadata": {
            "multi_carrier_relation_result_id": _result_id(request, relation_type, outcome),
            "multi_carrier_relation_result_type": "multi_carrier_relation_boundary_result",
            "multi_carrier_relation_result_version": RESULT_VERSION,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_relation_question": _declared_question(request, relation_type, selected_carriers, selected_evidence),
        "selected_carriers": selected_carriers,
        "selected_carrier_evidence": selected_evidence,
        "relation_basis": _relation_basis(request, relation_type, selected_carriers, selected_evidence, detection),
        "relation_checks": checks,
        "relation_result": _relation_result(outcome, request, relation_type, selected_carriers, selected_evidence, detection, checks, block_code, block_reason),
        "relation_non_meaning": copy.deepcopy(RELATION_NON_MEANING),
        "relation_consequence_boundary": _relation_consequence_boundary(),
        "what_remains_open": _what_remains_open(),
        "non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
        "outcome": outcome,
        "block": {"code": block_code, "reason": block_reason, "block_code": block_code, "block_reason": block_reason},
    }
    result["multi_carrier_relation_summary"] = build_multi_carrier_relation_summary(result)
    return result


def _build_checks(
    request: Mapping[str, Any],
    raw_carriers: Any,
    raw_evidence: Any,
    selected_carriers: Sequence[Mapping[str, Any]],
    selected_evidence: Sequence[Mapping[str, Any]],
    relation_type: str | None,
    detection: Mapping[str, Any],
    declared_non_claims: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    sources = [
        request,
        raw_carriers,
        raw_evidence,
        selected_carriers,
        selected_evidence,
        _as_mapping(request.get("relation_basis")),
        _as_mapping(request.get("selected_admission_basis")),
        _as_mapping(request.get("selected_correspondence_basis")),
        _as_mapping(request.get("selected_divergence_basis")),
        _as_mapping(request.get("selected_currentness_basis")),
        declared_non_claims,
    ]
    units = _relation_unit_count(selected_carriers, selected_evidence)
    checks = [
        _check("declared_relation_request_is_parseable_mapping", not precheck_failures, "declared relation request is a mapping", list(precheck_failures), precheck_failures[0] if precheck_failures else "DECLARED_RELATION_REQUEST_MALFORMED"),
        _check("relation_question_declared", bool(str(request.get("relation_question") or "").strip()), "relation question is declared", request.get("relation_question"), "RELATION_QUESTION_UNDECLARED"),
        _check("relation_type_supported", relation_type in SUPPORTED_RELATION_TYPES, "relation type is supported by this boundary", relation_type, "RELATION_TYPE_UNSUPPORTED"),
        _check("selected_carriers_or_evidence_exists", raw_carriers is not None or raw_evidence is not None, "selected carriers or selected carrier evidence are supplied", {"selected_carriers_shape": _shape(raw_carriers), "selected_evidence_shape": _shape(raw_evidence)}, "SELECTED_CARRIER_EVIDENCE_MISSING"),
        _check("selected_carriers_or_evidence_parseable", _selection_parseable(raw_carriers) and _selection_parseable(raw_evidence), "selected carriers and evidence are mappings or lists of mappings", {"selected_carriers_shape": _shape(raw_carriers), "selected_evidence_shape": _shape(raw_evidence)}, "SELECTED_CARRIER_EVIDENCE_MALFORMED"),
        _check("sufficient_selected_carriers_or_evidence", units >= 2, "at least two carrier roles, carrier identities, or evidence surfaces are selected", {"relation_unit_count": units, "selected_carrier_count": len(selected_carriers), "selected_evidence_count": len(selected_evidence)}, "INSUFFICIENT_SELECTED_CARRIERS_OR_EVIDENCE"),
        _check("evidence_identity_present", not selected_evidence or all(item.get("evidence_id") for item in selected_evidence), "each supplied evidence identity is declared", [item.get("evidence_id") for item in selected_evidence], "EVIDENCE_IDENTITY_MISSING"),
        _check("evidence_outcome_present", not selected_evidence or all(item.get("evidence_outcome") for item in selected_evidence), "each supplied evidence outcome or status is declared", [item.get("evidence_outcome") for item in selected_evidence], "EVIDENCE_OUTCOME_MISSING"),
        _check("carrier_identity_present_where_required", _carrier_identities_present(selected_carriers, selected_evidence), "carrier identities are declared where selected", {"selected_carrier_ids": [item.get("carrier_id") for item in selected_carriers], "evidence_carrier_ids": [item.get("carrier_id") for item in selected_evidence]}, "CARRIER_IDENTITY_MISSING"),
        _check("carrier_role_supported_where_required", _carrier_roles_supported(selected_carriers, selected_evidence), "selected carrier roles are admitted or absent", {"selected_carrier_roles": [item.get("carrier_role") for item in selected_carriers], "evidence_carrier_roles": [item.get("carrier_role") for item in selected_evidence]}, "CARRIER_ROLE_UNSUPPORTED"),
        _check("relation_detection_is_bounded", relation_type in SUPPORTED_RELATION_TYPES, "relation detection is limited to supported bounded relation types", {"relation_type": relation_type, "relation_supported": detection.get("relation_supported"), "no_relation_reason": detection.get("no_relation_reason")}, "RELATION_TYPE_UNSUPPORTED"),
    ]
    for check_name, aliases, expected, block_code in ANTI_COLLAPSE_CHECKS:
        actual = _flag_snapshot(sources, aliases)
        code = _specific_block_code(check_name, block_code, sources)
        checks.append(_check(check_name, not _flag_true(sources, aliases), expected, actual, code))
    failures = _missing_or_flipped_non_claims(declared_non_claims)
    selected_failures = _selected_non_claim_collapse(selected_carriers, selected_evidence)
    checks.append(
        _check(
            "non_claims_remain_false",
            not failures and not selected_failures,
            "all required relation non-claims are present and false",
            {"declared_non_claim_failures": failures, "selected_non_claim_collapse": selected_failures},
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _detect_relation(
    request: Mapping[str, Any],
    relation_type: str | None,
    carriers: Sequence[Mapping[str, Any]],
    evidence: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    if relation_type not in SUPPORTED_RELATION_TYPES:
        return _detection(False, "unsupported_relation_type", {}, carriers, evidence)
    if relation_type == "NO_MULTI_CARRIER_RELATION":
        return _detection(False, "declared_no_multi_carrier_relation", {}, carriers, evidence)

    roles = _selected_roles(carriers, evidence)
    carrier_ids = _selected_carrier_ids(carriers, evidence)
    shared_basis = _shared_basis_present(request, evidence)
    has_source = "SOURCE_CARRIER_FOR_PACKET" in roles or any(item.get("source_carrier_id") for item in evidence) or _first_text(request, ("source_carrier_id",))
    has_receiver = "RECEIVING_CARRIER" in roles or any(item.get("receiving_carrier_id") for item in evidence) or _first_text(request, ("receiving_carrier_id",))
    has_receipt = any(_has_token(item, {"RECEIPT", "CARRIED_SURFACE_RECEIVED"}) for item in evidence)
    has_return = bool(request.get("return_path") or request.get("return_basis")) or any(item.get("return_path") or item.get("return_context") or _has_token(item, {"RETURN", "RETURNED"}) for item in evidence)
    has_admitted = any(_has_token(item, {"ADMITTED"}) for item in evidence)
    has_refusal = any(item.get("refusal_or_blocked_outcome") for item in evidence)
    has_success = any(item.get("received_or_success_outcome") for item in evidence)
    has_divergence = bool(request.get("selected_divergence_basis")) or any(_has_token(item, {"DIVERGENCE"}) for item in evidence)
    has_currentness = any(_has_token(item, {"CURRENTNESS_PARTICIPATION_ELIGIBLE", "PARTICIPATION_ELIGIBLE"}) or _truthy(_as_mapping(item.get("raw_evidence")).get("currentness_participation_eligible")) for item in evidence)
    has_role_emission = any(item.get("carrier_role") and item.get("emission_class") for item in evidence)
    relation_evidence = {
        "selected_carrier_ids": carrier_ids,
        "selected_carrier_roles": roles,
        "shared_basis_present": shared_basis,
        "has_source_carrier": bool(has_source),
        "has_receiving_carrier": bool(has_receiver),
        "has_receipt_evidence": has_receipt,
        "has_return_evidence": has_return,
        "has_admitted_evidence": has_admitted,
        "has_refusal_evidence": has_refusal,
        "has_success_evidence": has_success,
        "has_divergence_evidence": has_divergence,
        "has_currentness_participation_evidence": has_currentness,
        "has_role_emission_evidence": has_role_emission,
    }
    supported = {
        "SOURCE_RECEIVER_RELATION": bool(has_source and has_receiver and (shared_basis or evidence)),
        "RECEIPT_RETURN_RELATION": bool(has_receipt and has_return and (shared_basis or evidence)),
        "ADMITTED_EVIDENCE_RELATION": bool(has_admitted and evidence),
        "REFUSAL_SUCCESS_RELATION": bool(has_refusal and has_success and (shared_basis or evidence)),
        "DIVERGENCE_BOUNDED_RELATION": bool(has_divergence and evidence),
        "CURRENTNESS_PARTICIPATION_RELATION": bool(has_currentness and evidence),
        "ROLE_EMISSION_RELATION": bool(has_role_emission),
        "CARRIER_EVIDENCE_SET_RELATION": bool(len(evidence) >= 2 and (shared_basis or evidence)),
    }.get(str(relation_type), False)
    return _detection(
        supported,
        None if supported else "selected carriers or evidence do not support declared relation type",
        relation_evidence,
        carriers,
        evidence,
    )


def _detection(
    supported: bool,
    no_reason: str | None,
    relation_evidence: Mapping[str, Any],
    carriers: Sequence[Mapping[str, Any]],
    evidence: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    return {
        "relation_supported": bool(supported),
        "no_relation_reason": no_reason,
        "relation_evidence": copy.deepcopy(dict(relation_evidence)),
        "visible_refusal_preserved": any(item.get("refusal_or_blocked_outcome") for item in evidence),
        "visible_divergence_preserved": any(_has_token(item, {"DIVERGENCE"}) for item in evidence),
        "selected_carrier_count": len(carriers),
        "selected_evidence_count": len(evidence),
    }


def _declared_question(
    request: Mapping[str, Any],
    relation_type: str | None,
    carriers: Sequence[Mapping[str, Any]],
    evidence: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    return {
        "relation_request_id": _first_text(request, ("relation_request_id", "request_id", "id")),
        "relation_question": request.get("relation_question"),
        "relation_purpose": request.get("relation_purpose"),
        "relation_type": relation_type,
        "declared_scope": copy.deepcopy(request.get("declared_scope")),
        "selected_carrier_count": len(carriers),
        "selected_evidence_count": len(evidence),
        "declared_non_claims": copy.deepcopy(_as_mapping(request.get("declared_non_claims"))),
        "declared_relation_request_path": request.get("_declared_relation_request_path"),
    }


def _relation_basis(
    request: Mapping[str, Any],
    relation_type: str | None,
    carriers: Sequence[Mapping[str, Any]],
    evidence: Sequence[Mapping[str, Any]],
    detection: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "relation_question": request.get("relation_question"),
        "relation_type": relation_type,
        "supported_relation_types": sorted(SUPPORTED_RELATION_TYPES),
        "relation_purpose": request.get("relation_purpose"),
        "declared_scope": copy.deepcopy(request.get("declared_scope")),
        "selected_carrier_ids": _selected_carrier_ids(carriers, evidence),
        "selected_carrier_roles": _selected_roles(carriers, evidence),
        "selected_evidence_ids": [item.get("evidence_id") for item in evidence],
        "selected_evidence_outcomes": [item.get("evidence_outcome") for item in evidence],
        "selected_evidence_classes": [item.get("evidence_class") for item in evidence],
        "selected_emission_classes": [item.get("emission_class") for item in evidence],
        "selected_admission_statuses": [item.get("admission_status") for item in evidence],
        "selected_correspondence_statuses": [item.get("correspondence_status") for item in evidence],
        "selected_divergence_statuses": [item.get("divergence_status") for item in evidence],
        "selected_currentness_participation_statuses": [item.get("currentness_participation_status") for item in evidence],
        "lineage_basis": copy.deepcopy(request.get("lineage_basis")),
        "selected_admission_basis": copy.deepcopy(request.get("selected_admission_basis")),
        "selected_correspondence_basis": copy.deepcopy(request.get("selected_correspondence_basis")),
        "selected_divergence_basis": copy.deepcopy(request.get("selected_divergence_basis")),
        "selected_currentness_basis": copy.deepcopy(request.get("selected_currentness_basis")),
        "relation_detection": copy.deepcopy(dict(detection)),
        "visible_divergence_remains_visible": True,
        "hidden_divergence": False,
        "refusal_hidden": False,
        "relation_does_not_create_source_replacement": True,
        "relation_does_not_create_currentness": True,
        "relation_does_not_create_authority": True,
        "relation_does_not_create_permission": True,
        "relation_does_not_create_carrier_hierarchy": True,
        "relation_does_not_create_distributed_standing": True,
        "relation_does_not_authorize_continuation": True,
        "required_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }


def _relation_result(
    outcome: str,
    request: Mapping[str, Any],
    relation_type: str | None,
    carriers: Sequence[Mapping[str, Any]],
    evidence: Sequence[Mapping[str, Any]],
    detection: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    base = {
        "relation_type": relation_type,
        "selected_carrier_count": len(carriers),
        "selected_evidence_count": len(evidence),
        "selected_carrier_ids": _selected_carrier_ids(carriers, evidence),
        "selected_evidence_ids": [item.get("evidence_id") for item in evidence],
        "selected_evidence_outcomes": [item.get("evidence_outcome") for item in evidence],
        "selected_carriers_preserved": copy.deepcopy(list(carriers)),
        "selected_evidence_preserved": copy.deepcopy(list(evidence)),
        "carrier_roles_preserved": True,
        "evidence_identities_preserved": True,
        "local_outcomes_preserved": True,
        "return_admission_divergence_currentness_participation_distinctions_preserved": True,
        "visible_refusal_preserved": bool(detection.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(detection.get("visible_divergence_preserved")),
        "downstream_evidence_posture_preserved": True,
        "carriers_not_merged": True,
        "evidence_not_merged_into_source": True,
        "current_carrier_not_selected": True,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "source_not_replaced": True,
        "currentness_not_created": True,
        "authority_not_created": True,
        "permission_not_created": True,
        "carrier_hierarchy_not_created": True,
        "distributed_standing_not_created": True,
        "truth_not_created": True,
        "action_not_authorized": True,
        "continuation_not_authorized": True,
    }
    if outcome == MULTI_CARRIER_RELATION_RECOGNIZED:
        base.update({
            "multi_carrier_relation_recognized": True,
            "no_multi_carrier_relation": False,
            "relation_claim": "selected carriers or carrier evidence stand in bounded relation for the declared relation question",
            "relation_evidence": copy.deepcopy(_as_mapping(detection.get("relation_evidence"))),
        })
    elif outcome == NO_MULTI_CARRIER_RELATION:
        base.update({
            "multi_carrier_relation_recognized": False,
            "no_multi_carrier_relation": True,
            "no_relation_reason": detection.get("no_relation_reason") or "declared no multi-carrier relation",
            "relation_evidence": copy.deepcopy(_as_mapping(detection.get("relation_evidence"))),
            "no_collapse_flags_true": True,
        })
    else:
        base.update({
            "multi_carrier_relation_recognized": False,
            "no_multi_carrier_relation": False,
            "block_code": block_code,
            "block_reason": block_reason,
            "failed_checks": [copy.deepcopy(dict(check)) for check in checks if check.get("passed") is False],
            "selected_basis_where_available": {
                "relation_request_id": _first_text(request, ("relation_request_id", "request_id", "id")),
                "relation_question": request.get("relation_question"),
                "relation_type": relation_type,
                "selected_carrier_ids": _selected_carrier_ids(carriers, evidence),
                "selected_evidence_ids": [item.get("evidence_id") for item in evidence],
            },
            "declared_non_claims_where_available": copy.deepcopy(_as_mapping(request.get("declared_non_claims"))),
        })
    return base


def _normalize_carriers(raw: Any) -> list[dict[str, Any]]:
    normalized = []
    for index, item in enumerate(_raw_mapping_items(raw)):
        role = _normalize_token(_first_text(item, ("carrier_role", "role", "declared_carrier_role")))
        normalized.append({
            "carrier_index": index,
            "carrier_id": _first_text(item, ("carrier_id", "selected_carrier_id", "source_carrier_id", "receiving_carrier_id", "id", "carrier_identifier", "carrier_label", "label")),
            "carrier_label": _first_text(item, ("carrier_label", "label", "name")),
            "carrier_role": role,
            "role_declared": bool(role),
            "role_bounded": not role or role in ADMITTED_CARRIER_ROLES,
            "raw_carrier": copy.deepcopy(dict(item)),
        })
    return normalized


def _normalize_evidence(raw: Any) -> list[dict[str, Any]]:
    normalized = []
    for index, item in enumerate(_raw_mapping_items(raw)):
        carrier = _as_mapping(item.get("carrier") or item.get("selected_carrier") or item.get("emitting_carrier") or item.get("receiving_carrier"))
        outcome = _first_text(item, ("evidence_outcome", "outcome", "status", "emission_outcome", "receipt_outcome", "admission_outcome", "divergence_outcome", "currentness_outcome", "result_outcome"))
        normalized_outcome = _normalize_token(outcome)
        basis = _source_basis(item)
        block = _as_mapping(item.get("block"))
        return_basis = _as_mapping(item.get("return_basis"))
        integrity = _as_mapping(item.get("integrity_evidence") or item.get("integrity") or item.get("carried_surface_integrity"))
        evidence = {
            "evidence_index": index,
            "evidence_id": _first_text(item, ("evidence_id", "id", "emission_id", "receipt_id", "admission_id", "divergence_result_id", "currentness_result_id", "correspondence_result_id", "surface_id", "result_id", "selected_evidence_id")),
            "evidence_outcome": outcome,
            "normalized_evidence_outcome": normalized_outcome,
            "carrier_id": _first_text(item, ("carrier_id", "selected_carrier_id", "emitting_carrier_id", "source_carrier_id", "receiving_carrier_id", "returning_carrier_id")) or _first_text(carrier, ("carrier_id", "id", "carrier_identifier")),
            "source_carrier_id": _first_text(item, ("source_carrier_id",)),
            "receiving_carrier_id": _first_text(item, ("receiving_carrier_id",)),
            "carrier_role": _normalize_token(_first_text(item, ("carrier_role", "role", "declared_carrier_role")) or _first_text(carrier, ("carrier_role", "role"))),
            "evidence_class": _normalize_token(_first_text(item, ("evidence_class", "evidence_type", "result_type", "surface_type"))),
            "emission_class": _normalize_token(_first_text(item, ("emission_class", "declared_emission_class", "carrier_emission_class"))),
            "source_or_carried_basis": copy.deepcopy(basis),
            "source_or_carried_basis_fingerprint": _fingerprint(basis),
            "admission_status": _first_text(item, ("admission_status", "admission_outcome", "carrier_local_emission_admission_status")),
            "correspondence_status": _first_text(item, ("correspondence_status", "correspondence_outcome")),
            "divergence_status": _first_text(item, ("divergence_status", "divergence_outcome")),
            "currentness_participation_status": _first_text(item, ("currentness_participation_status", "currentness_status", "participation_status")),
            "return_path": _first_text(item, ("return_path",)) or _first_text(return_basis, ("return_path", "path")),
            "return_context": copy.deepcopy(item.get("return_context") if "return_context" in item else return_basis.get("return_context")),
            "integrity_hash": _first_text(item, ("integrity_hash", "hash", "sha256", "content_hash")) or _first_text(integrity, ("integrity_hash", "hash", "sha256", "content_hash")),
            "integrity_status": _first_text(item, ("integrity_status", "integrity_outcome", "hash_status")) or _first_text(integrity, ("integrity_status", "outcome", "status")),
            "block_code": _first_text(item, ("block_code", "code")) or _first_text(block, ("block_code", "code")),
            "block_reason": _first_text(item, ("block_reason", "reason")) or _first_text(block, ("block_reason", "reason")),
            "non_claims": _as_mapping(item.get("non_claims")),
            "refusal_or_blocked_outcome": _token_contains(normalized_outcome, REFUSAL_OUTCOME_HINTS),
            "received_or_success_outcome": _token_contains(normalized_outcome, SUCCESS_OUTCOME_HINTS),
            "raw_evidence": copy.deepcopy(dict(item)),
        }
        normalized.append(evidence)
    return normalized


def _source_basis(item: Mapping[str, Any]) -> Any:
    for key in ("source_or_carried_basis", "source_carried_basis", "carried_surface_basis", "source_basis", "selected_basis", "basis", "lineage_basis"):
        if key in item:
            return copy.deepcopy(item.get(key))
    basis = {}
    for key in ("basis_id", "source_basis_id", "carried_surface_id", "surface_id", "packet_id", "operation_id", "receipt_id", "admission_id"):
        if key in item:
            basis[key] = copy.deepcopy(item.get(key))
    return basis or None


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    try:
        loaded = json.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as exc:
        raise MultiCarrierRelationBoundaryError("DECLARED_RELATION_REQUEST_UNREADABLE", BLOCK_REASONS["DECLARED_RELATION_REQUEST_UNREADABLE"]) from exc
    except json.JSONDecodeError as exc:
        raise MultiCarrierRelationBoundaryError("DECLARED_RELATION_REQUEST_MALFORMED", BLOCK_REASONS["DECLARED_RELATION_REQUEST_MALFORMED"]) from exc
    if not isinstance(loaded, Mapping):
        raise MultiCarrierRelationBoundaryError("DECLARED_RELATION_REQUEST_MALFORMED", BLOCK_REASONS["DECLARED_RELATION_REQUEST_MALFORMED"])
    return copy.deepcopy(dict(loaded))


def _relation_consequence_boundary() -> dict[str, Any]:
    return {
        "relation_may": {
            "permit_selected_surfaces_as_bounded_relation_set": True,
            "preserve_visible_relation_posture": True,
            "support_later_relation_conformance": True,
            "support_later_closure_if_conformance_passes": True,
            "support_later_currentness_review_only_if_separately_admitted": True,
            "preserve_visible_divergence_as_part_of_relation": True,
        },
        "relation_may_not": {
            "decide_source": True,
            "decide_currentness": True,
            "decide_truth": True,
            "decide_action": True,
            "select_winning_carrier": True,
            "erase_losing_carrier_evidence": True,
            "create_carrier_hierarchy": True,
            "create_distributed_standing": True,
            "create_carrier_registry": True,
            "create_synchronization": True,
            "authorize_continuation": True,
        },
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [{"name": item, "scheduled": False, "authorized": False, "executed": False} for item in OPEN_SURFACES],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _check(name: str, passed: bool, expected: Any, actual: Any, block_code: str | None) -> dict[str, Any]:
    return {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": copy.deepcopy(expected),
        "actual_posture": copy.deepcopy(actual),
        "block_code": None if passed else block_code,
    }


def _specific_block_code(check_name: str, block_code: str, sources: Sequence[Any]) -> str:
    if check_name == "relation_does_not_create_successor_body" and _flag_true(sources, ("relation_creates_body", "carrier_relation_created_body", "body_created", "body_formed")):
        return "RELATION_CREATES_BODY"
    if check_name == "relation_does_not_establish_presence_threshold" and _flag_true(sources, ("threshold_met", "relation_establishes_threshold")):
        return "RELATION_ESTABLISHES_THRESHOLD"
    if check_name == "relation_does_not_authorize_action_create_consequence" and _flag_true(sources, ("consequence_created", "relation_creates_consequence")):
        return "RELATION_CREATES_CONSEQUENCE"
    if check_name == "relation_does_not_resolve_divergence_by_majority_latest_success_count":
        if _flag_true(sources, ("divergence_resolved_by_latest_file", "relation_resolves_divergence_by_latest_file")):
            return "RELATION_RESOLVES_DIVERGENCE_BY_LATEST_FILE"
        if _flag_true(sources, ("divergence_resolved_by_success_count", "relation_resolves_divergence_by_success_count")):
            return "RELATION_RESOLVES_DIVERGENCE_BY_SUCCESS_COUNT"
    return block_code


def _carrier_identities_present(carriers: Sequence[Mapping[str, Any]], evidence: Sequence[Mapping[str, Any]]) -> bool:
    return (not carriers or all(item.get("carrier_id") for item in carriers)) and (not evidence or all(item.get("carrier_id") for item in evidence))


def _carrier_roles_supported(carriers: Sequence[Mapping[str, Any]], evidence: Sequence[Mapping[str, Any]]) -> bool:
    for role in _selected_roles(carriers, evidence):
        if role in CANDIDATE_CARRIER_ROLES or (role and role not in ADMITTED_CARRIER_ROLES):
            return False
    return True


def _relation_unit_count(carriers: Sequence[Mapping[str, Any]], evidence: Sequence[Mapping[str, Any]]) -> int:
    return max(
        len(carriers) + len(evidence),
        len(_selected_carrier_ids(carriers, evidence)),
        len(_selected_roles(carriers, evidence)),
        len(_unique_values(item.get("evidence_id") for item in evidence)),
    )


def _selected_roles(carriers: Sequence[Mapping[str, Any]], evidence: Sequence[Mapping[str, Any]]) -> list[str]:
    return _unique_values([item.get("carrier_role") for item in carriers] + [item.get("carrier_role") for item in evidence])


def _selected_carrier_ids(carriers: Sequence[Mapping[str, Any]], evidence: Sequence[Mapping[str, Any]]) -> list[str]:
    values = [item.get("carrier_id") for item in carriers]
    for item in evidence:
        values.extend((item.get("carrier_id"), item.get("source_carrier_id"), item.get("receiving_carrier_id")))
    return _unique_values(values)


def _shared_basis_present(request: Mapping[str, Any], evidence: Sequence[Mapping[str, Any]]) -> bool:
    if request.get("lineage_basis"):
        return True
    values = _unique_values(item.get("source_or_carried_basis_fingerprint") for item in evidence)
    return len(values) == 1 and bool(values[0])


def _has_token(item: Mapping[str, Any], hints: set[str]) -> bool:
    return any(
        _token_contains(item.get(key), hints)
        for key in ("evidence_outcome", "normalized_evidence_outcome", "evidence_class", "emission_class", "admission_status", "correspondence_status", "divergence_status", "currentness_participation_status")
    )


def _token_contains(value: Any, hints: set[str]) -> bool:
    token = _normalize_token(value)
    return bool(token and any(hint in token for hint in hints))


def _selection_parseable(value: Any) -> bool:
    return value is None or isinstance(value, Mapping) or (isinstance(value, list) and all(isinstance(item, Mapping) for item in value))


def _raw_mapping_items(value: Any) -> list[Mapping[str, Any]]:
    if isinstance(value, Mapping):
        return [_as_mapping(value)]
    if isinstance(value, list):
        return [_as_mapping(item) for item in value if isinstance(item, Mapping)]
    return []


def _shape(value: Any) -> Any:
    if isinstance(value, list):
        return [type(item).__name__ for item in value]
    return None if value is None else type(value).__name__


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is False:
            return check
    return None


def _block_reason(block_code: str | None) -> str | None:
    if block_code is None:
        return None
    return BLOCK_REASONS.get(block_code, f"Relation blocked: {block_code}.")


def _result_id(request: Mapping[str, Any], relation_type: str | None, outcome: str) -> str:
    basis_id = _first_text(request, ("relation_request_id", "request_id", "id")) or relation_type or "multi_carrier_relation"
    return f"{_safe_filename_part(basis_id)}__{outcome.lower()}__multi_carrier_relation_result"


def _as_mapping(value: Any) -> dict[str, Any]:
    return copy.deepcopy(dict(value)) if isinstance(value, Mapping) else {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    return [copy.deepcopy(dict(item)) for item in value] if isinstance(value, list) and all(isinstance(item, Mapping) for item in value) else []


def _first_text(mapping: Mapping[str, Any], keys: Sequence[str]) -> str | None:
    for key in keys:
        value = mapping.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if isinstance(value, (int, float)):
            return str(value)
    return None


def _normalize_token(value: Any) -> str | None:
    if value is None:
        return None
    token = str(value).strip().upper().replace("-", "_").replace(" ", "_")
    while "__" in token:
        token = token.replace("__", "_")
    return token or None


def _fingerprint(value: Any) -> str | None:
    if value is None:
        return None
    return json.dumps(value, sort_keys=True, default=str, separators=(",", ":"))


def _unique_values(values: Any) -> list[str]:
    if values is None or isinstance(values, (str, bytes)):
        raw_values = [values]
    else:
        try:
            raw_values = list(values)
        except TypeError:
            raw_values = [values]
    unique = []
    for value in raw_values:
        text = str(value).strip() if value is not None else ""
        if text and text not in unique:
            unique.append(text)
    return unique


def _missing_or_flipped_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    return {key: ("missing" if key not in non_claims else non_claims.get(key)) for key in REQUIRED_NON_CLAIMS if key not in non_claims or non_claims.get(key) is not False}


def _selected_non_claim_collapse(carriers: Sequence[Mapping[str, Any]], evidence: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    conflicts = {}
    for section_name, selected in (("selected_carriers", carriers), ("selected_carrier_evidence", evidence)):
        for item in selected:
            flipped = {key: value for key, value in _as_mapping(item.get("non_claims")).items() if key in REQUIRED_NON_CLAIMS and value is not False}
            if flipped:
                conflicts[f"{section_name}:{item.get('evidence_id') or item.get('carrier_id') or item.get('evidence_index') or item.get('carrier_index')}"] = flipped
    return conflicts


def _flag_true(sources: Any, aliases: Sequence[str]) -> bool:
    alias_set = {alias.lower() for alias in aliases}
    return any(key.lower() in alias_set and _truthy(value) for key, value in _walk_key_values(sources))


def _flag_snapshot(sources: Any, aliases: Sequence[str]) -> dict[str, Any]:
    alias_set = {alias.lower() for alias in aliases}
    return {key: copy.deepcopy(value) for key, value in _walk_key_values(sources) if key.lower() in alias_set}


def _walk_key_values(value: Any) -> list[tuple[str, Any]]:
    found = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            found.append((str(key), item))
            found.extend(_walk_key_values(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(_walk_key_values(item))
    return found


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "on", "created", "authorized"}
    return bool(value)


def _safe_filename_part(value: Any) -> str:
    text = str(value or "multi_carrier_relation").strip().lower()
    safe = "".join(char if char.isalnum() or char in {"-", "_"} else "_" for char in text).strip("_")
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe or "multi_carrier_relation"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.parent / f"{path.stem}_{index:03d}{path.suffix}"
        if not candidate.exists():
            return candidate
    raise MultiCarrierRelationBoundaryError("RELATION_OVERWRITES_EVIDENCE", "Could not create a non-overwriting relation result path.")


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "source_replaced",
        "carrier_relation_created_hierarchy",
        "winning_carrier_selected",
        "losing_carrier_invalidated",
        "distributed_standing_created",
        "carrier_registry_created",
        "repository_synchronization_created",
        "signal_created_by_default",
        "presence_established",
        "threshold_met",
        "truth_created",
        "action_authorized",
        "consequence_created",
        "continuation_authorized",
        "latest_file_currentness",
        "recency_fraud",
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    )
    return {key: copy.deepcopy(non_claims.get(key)) for key in keys}
