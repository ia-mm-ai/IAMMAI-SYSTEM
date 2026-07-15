"""Bounded cross-carrier divergence boundary resolver.

This resolver records visible disagreement between selected carrier-produced
or carrier-admitted evidence surfaces. It preserves divergence as mismatch,
not resolution. It does not create sourcehood, currentness, authority,
permission, successor standing, body formation, signal posture, presence,
threshold, truth, action, consequence, multi-carrier law, distributed standing,
carrier hierarchy, or continuation.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CrossCarrierDivergenceBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit divergence inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


CROSS_CARRIER_DIVERGENCE_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_cross_carrier_divergence_boundary"
)

RESOLVER_MODULE = "resolve_cross_carrier_divergence_boundary"
RESULT_VERSION = "0.1.0"

CARRIER_DIVERGENCE_RECORDED = "CARRIER_DIVERGENCE_RECORDED"
NO_CARRIER_DIVERGENCE = "NO_CARRIER_DIVERGENCE"
CARRIER_DIVERGENCE_BLOCKED = "CARRIER_DIVERGENCE_BLOCKED"

SUPPORTED_DIVERGENCE_TYPES = {
    "OUTCOME_DIVERGENCE",
    "RECEIPT_REFUSAL_DIVERGENCE",
    "BASIS_DIVERGENCE",
    "INTEGRITY_DIVERGENCE",
    "CARRIER_IDENTITY_DIVERGENCE",
    "ROLE_DIVERGENCE",
    "EMISSION_CLASS_DIVERGENCE",
    "RETURN_PATH_DIVERGENCE",
    "NON_CLAIM_DIVERGENCE",
    "STALE_OR_SEQUENCE_DIVERGENCE",
    "MISSING_EVIDENCE_DIVERGENCE",
    "MALFORMED_EVIDENCE_DIVERGENCE",
    "NO_DIVERGENCE",
}

POSITIVE_DIVERGENCE_TYPES = SUPPORTED_DIVERGENCE_TYPES - {"NO_DIVERGENCE"}

RECEIVED_OR_SUCCESS_OUTCOME_HINTS = {
    "ADMITTED",
    "ADMITTED_AS_EVIDENCE",
    "BODY_CONFORMANT",
    "CARRIER_EMISSION_RECOGNIZED",
    "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
    "CARRIED_SURFACE_RECEIVED",
    "CONFORMANCE_CLOSURE_RECORDED",
    "CORRESPONDENCE_RECOGNIZED",
    "PASS",
    "PASSED",
    "RECEIVED",
    "RECOGNIZED",
    "SELF_ORIENTED",
    "SUCCESS",
    "SUCCESSFUL",
}

BLOCKED_OR_REFUSAL_OUTCOME_HINTS = {
    "ADMISSION_BLOCKED",
    "BLOCKED",
    "CARRIER_DIVERGENCE_BLOCKED",
    "CARRIER_LOCAL_EMISSION_ADMISSION_BLOCKED",
    "CARRIER_ROLE_EMISSION_BLOCKED",
    "FAILED",
    "FAILURE",
    "REFUSAL",
    "REFUSED",
    "RECEIPT_BLOCK",
    "RECEIPT_REFUSAL_REASON",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "divergence_hidden": False,
    "refusal_hidden": False,
    "mismatch_hidden": False,
    "evidence_overwritten": False,
    "divergence_resolved_by_majority": False,
    "divergence_resolved_by_latest_file": False,
    "divergence_resolved_by_success_count": False,
    "carrier_hierarchy_created": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
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
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "DECLARED_DIVERGENCE_REQUEST_MISSING": "No declared divergence request was supplied.",
    "DECLARED_DIVERGENCE_REQUEST_UNREADABLE": "The declared divergence request path could not be read.",
    "DECLARED_DIVERGENCE_REQUEST_MALFORMED": "The declared divergence request is not a JSON object or mapping.",
    "INSUFFICIENT_EVIDENCE_SURFACES": "At least two selected evidence surfaces are required.",
    "SELECTED_EVIDENCE_MISSING": "Selected carrier evidence is missing.",
    "SELECTED_EVIDENCE_MALFORMED": "Selected carrier evidence is malformed.",
    "EVIDENCE_IDENTITY_MISSING": "Selected evidence identity is missing.",
    "CARRIER_IDENTITY_MISSING": "Carrier identity is missing where required.",
    "EVIDENCE_OUTCOME_MISSING": "Selected evidence outcome or status is missing.",
    "DIVERGENCE_QUESTION_UNDECLARED": "Divergence question is undeclared.",
    "DIVERGENCE_TYPE_UNSUPPORTED": "Divergence type is unsupported.",
    "DIVERGENCE_HIDES_MISMATCH": "Divergence hides mismatch.",
    "DIVERGENCE_HIDES_REFUSAL": "Divergence hides refusal.",
    "DIVERGENCE_OVERWRITES_EVIDENCE": "Divergence overwrites evidence.",
    "DIVERGENCE_MUTATES_OR_REPLAYS_EVIDENCE": "Divergence mutates, replays, or merges evidence.",
    "DIVERGENCE_REPLACES_SOURCE": "Divergence replaces source.",
    "DIVERGENCE_CREATES_CURRENTNESS": "Divergence creates currentness.",
    "DIVERGENCE_CREATES_AUTHORITY": "Divergence creates authority.",
    "DIVERGENCE_CREATES_PERMISSION": "Divergence creates permission.",
    "DIVERGENCE_CREATES_SUCCESSOR": "Divergence creates successor standing.",
    "DIVERGENCE_CREATES_BODY": "Divergence creates body formation.",
    "DIVERGENCE_CREATES_SIGNAL_BY_DEFAULT": "Divergence creates signal by default.",
    "DIVERGENCE_ESTABLISHES_PRESENCE": "Divergence establishes presence.",
    "DIVERGENCE_ESTABLISHES_THRESHOLD": "Divergence establishes threshold.",
    "DIVERGENCE_CREATES_TRUTH": "Divergence creates truth.",
    "DIVERGENCE_AUTHORIZES_ACTION": "Divergence authorizes action.",
    "DIVERGENCE_CREATES_CONSEQUENCE": "Divergence creates consequence.",
    "DIVERGENCE_CREATES_MULTI_CARRIER_LAW": "Divergence creates multi-carrier law.",
    "DIVERGENCE_CREATES_DISTRIBUTED_STANDING": "Divergence creates distributed standing.",
    "DIVERGENCE_AUTHORIZES_CONTINUATION": "Divergence authorizes continuation.",
    "DIVERGENCE_RESOLVES_BY_MAJORITY": "Divergence resolves by majority.",
    "DIVERGENCE_RESOLVES_BY_LATEST_FILE": "Divergence resolves by latest file.",
    "DIVERGENCE_RESOLVES_BY_SUCCESS_COUNT": "Divergence resolves by successful receipt count.",
    "LATEST_FILE_CURRENTNESS": "Latest-file recency is treated as currentness.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required divergence non-claim is missing or flipped.",
}

DIVERGENCE_NON_MEANING = {
    "does_not_mean_source_replacement": True,
    "does_not_mean_currentness": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_successor_standing": True,
    "does_not_mean_body_formation": True,
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
    "does_not_mean_majority_rule": True,
    "does_not_mean_latest_file_rule": True,
    "does_not_mean_successful_receipt_count_rule": True,
    "does_not_mean_winning_carrier": True,
    "does_not_mean_losing_carrier_invalidated": True,
    "does_not_mean_body_must_resolve_now": True,
}

OPEN_SURFACES = [
    "cross-carrier divergence implementation refinement",
    "cross-carrier currentness boundary",
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

ANTI_COLLAPSE_CHECKS = (
    (
        "divergence_does_not_hide_mismatch",
        ("divergence_hidden", "mismatch_hidden", "divergence_hides_mismatch", "hides_mismatch"),
        "divergence keeps mismatch visible",
        "DIVERGENCE_HIDES_MISMATCH",
    ),
    (
        "divergence_does_not_hide_refusal",
        ("refusal_hidden", "divergence_hides_refusal", "hides_refusal"),
        "divergence keeps refusal visible",
        "DIVERGENCE_HIDES_REFUSAL",
    ),
    (
        "divergence_does_not_overwrite_evidence",
        ("evidence_overwritten", "divergence_overwrites_evidence", "evidence_erased"),
        "divergence overwrites no evidence",
        "DIVERGENCE_OVERWRITES_EVIDENCE",
    ),
    (
        "divergence_does_not_mutate_replay_or_merge_evidence",
        (
            "mutation_performed",
            "replay_performed",
            "merge_performed",
            "divergence_mutates_evidence",
            "divergence_replays_evidence",
            "divergence_merges_evidence",
        ),
        "divergence performs no mutation, replay, or merge",
        "DIVERGENCE_MUTATES_OR_REPLAYS_EVIDENCE",
    ),
    (
        "divergence_does_not_replace_source",
        ("source_replaced", "divergence_replaces_source"),
        "divergence replaces no source",
        "DIVERGENCE_REPLACES_SOURCE",
    ),
    (
        "divergence_does_not_create_currentness",
        ("currentness_created", "divergence_creates_currentness"),
        "divergence creates no currentness",
        "DIVERGENCE_CREATES_CURRENTNESS",
    ),
    (
        "divergence_does_not_create_authority",
        ("authority_created", "divergence_creates_authority"),
        "divergence creates no authority",
        "DIVERGENCE_CREATES_AUTHORITY",
    ),
    (
        "divergence_does_not_create_permission",
        ("permission_created", "divergence_creates_permission"),
        "divergence creates no permission",
        "DIVERGENCE_CREATES_PERMISSION",
    ),
    (
        "divergence_does_not_create_successor_body",
        (
            "divergence_creates_successor",
            "successor_standing_created",
            "divergence_creates_body",
            "body_created",
            "body_formed",
        ),
        "divergence creates no successor standing or body",
        "DIVERGENCE_CREATES_SUCCESSOR",
    ),
    (
        "divergence_does_not_create_signal_by_default",
        ("signal_created_by_default", "divergence_creates_signal_by_default"),
        "divergence creates no signal by default",
        "DIVERGENCE_CREATES_SIGNAL_BY_DEFAULT",
    ),
    (
        "divergence_does_not_establish_presence_threshold",
        (
            "presence_established",
            "threshold_met",
            "divergence_establishes_presence",
            "divergence_establishes_threshold",
        ),
        "divergence establishes no presence or threshold",
        "DIVERGENCE_ESTABLISHES_PRESENCE",
    ),
    (
        "divergence_does_not_create_truth",
        ("truth_created", "divergence_creates_truth"),
        "divergence creates no truth",
        "DIVERGENCE_CREATES_TRUTH",
    ),
    (
        "divergence_does_not_authorize_action_create_consequence",
        (
            "action_authorized",
            "consequence_created",
            "divergence_authorizes_action",
            "divergence_creates_consequence",
        ),
        "divergence authorizes no action and creates no consequence",
        "DIVERGENCE_AUTHORIZES_ACTION",
    ),
    (
        "divergence_does_not_create_multi_carrier_law_distributed_standing",
        (
            "multi_carrier_law_created",
            "distributed_standing_created",
            "divergence_creates_multi_carrier_law",
            "divergence_creates_distributed_standing",
        ),
        "divergence creates no multi-carrier law or distributed standing",
        "DIVERGENCE_CREATES_MULTI_CARRIER_LAW",
    ),
    (
        "divergence_does_not_authorize_continuation",
        (
            "continuation_authorized",
            "divergence_authorizes_continuation",
            "follow_on_work_authorized",
            "follow_on_steps_authorized",
        ),
        "divergence authorizes no continuation",
        "DIVERGENCE_AUTHORIZES_CONTINUATION",
    ),
    (
        "divergence_does_not_resolve_by_majority_latest_success_count",
        (
            "divergence_resolved_by_majority",
            "divergence_resolves_by_majority",
            "divergence_resolved_by_latest_file",
            "divergence_resolves_by_latest_file",
            "divergence_resolved_by_success_count",
            "divergence_resolves_by_success_count",
        ),
        "divergence is not resolved by majority, latest file, or success count",
        "DIVERGENCE_RESOLVES_BY_MAJORITY",
    ),
    (
        "latest_file_currentness_false",
        ("latest_file_currentness", "latest_file_recency_currentness"),
        "latest local file is not currentness",
        "LATEST_FILE_CURRENTNESS",
    ),
    (
        "recency_fraud_false",
        ("recency_fraud", "recency_currentness"),
        "recency is not used as currentness",
        "LATEST_FILE_CURRENTNESS",
    ),
)


def resolve_cross_carrier_divergence_boundary(
    declared_divergence_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one declared cross-carrier divergence request."""

    if declared_divergence_request is None:
        request: dict[str, Any] = {}
        precheck_failures = ["DECLARED_DIVERGENCE_REQUEST_MISSING"]
    elif not isinstance(declared_divergence_request, Mapping):
        request = {}
        precheck_failures = ["DECLARED_DIVERGENCE_REQUEST_MALFORMED"]
    else:
        request = copy.deepcopy(dict(declared_divergence_request))
        precheck_failures = []
    return _resolve_request(request, precheck_failures)


def resolve_cross_carrier_divergence_boundary_from_path(
    declared_divergence_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one declared divergence request JSON path."""

    try:
        request = _read_json_mapping(declared_divergence_request_path)
        request["_declared_divergence_request_path"] = str(
            Path(declared_divergence_request_path)
        )
        precheck_failures: list[str] = []
    except CrossCarrierDivergenceBoundaryError as exc:
        request = {}
        precheck_failures = [exc.block_code]
    return _resolve_request(request, precheck_failures)


def write_cross_carrier_divergence_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded divergence result artifact without overwriting."""

    if output_path is None:
        question = _as_mapping(result.get("declared_divergence_question"))
        basis_id = (
            question.get("divergence_request_id")
            or question.get("divergence_type")
            or "cross_carrier_divergence"
        )
        filename = (
            f"{_safe_filename_part(basis_id)}"
            "__cross_carrier_divergence_result.json"
        )
        target = CROSS_CARRIER_DIVERGENCE_BOUNDARY_ROOT / filename
    else:
        target = Path(output_path)
    target = _non_overwriting_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    return target


def build_cross_carrier_divergence_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact bounded summary for a divergence result."""

    checks = _mapping_list(result.get("divergence_checks"))
    question = _as_mapping(result.get("declared_divergence_question"))
    divergence_result = _as_mapping(result.get("divergence_result"))
    non_claims = _as_mapping(result.get("non_claims"))
    block = _as_mapping(result.get("block"))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "divergence_request_id": question.get("divergence_request_id"),
        "divergence_question": question.get("divergence_question"),
        "divergence_type": question.get("divergence_type"),
        "divergence_recorded": bool(divergence_result.get("divergence_recorded")),
        "no_carrier_divergence": bool(
            divergence_result.get("no_carrier_divergence")
        ),
        "selected_evidence_count": divergence_result.get("selected_evidence_count"),
        "selected_evidence_ids": copy.deepcopy(
            divergence_result.get("selected_evidence_ids")
        ),
        "selected_evidence_outcomes": copy.deepcopy(
            divergence_result.get("selected_evidence_outcomes")
        ),
        "selected_carrier_ids": copy.deepcopy(
            divergence_result.get("selected_carrier_ids")
        ),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "visible_divergence": bool(divergence_result.get("visible_divergence")),
        "hidden_divergence": bool(divergence_result.get("hidden_divergence")),
        "mismatch_hidden": bool(non_claims.get("mismatch_hidden")),
        "refusal_hidden": bool(non_claims.get("refusal_hidden")),
        "source_created": bool(non_claims.get("source_replaced")),
        "currentness_created": bool(non_claims.get("currentness_created")),
        "authority_created": bool(non_claims.get("authority_created")),
        "permission_created": bool(non_claims.get("permission_created")),
        "truth_created": bool(non_claims.get("truth_created")),
        "action_authorized": bool(non_claims.get("action_authorized")),
        "consequence_created": bool(non_claims.get("consequence_created")),
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
        "continuation_authorized": bool(non_claims.get("continuation_authorized")),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_declared_divergence_request(
    divergence_request_id: str,
    divergence_question: str,
    divergence_type: str,
    selected_carrier_evidence: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Build a minimum valid declared divergence request."""

    return {
        "divergence_request_id": divergence_request_id,
        "divergence_question": divergence_question,
        "divergence_type": _normalize_token(divergence_type) or divergence_type,
        "selected_carrier_evidence": [
            copy.deepcopy(dict(item)) for item in selected_carrier_evidence
        ],
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }


def _resolve_request(
    request: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    request_mapping = _as_mapping(request)
    raw_evidence = request_mapping.get("selected_carrier_evidence")
    selected = _normalize_selected_evidence(raw_evidence)
    divergence_type = _normalize_token(request_mapping.get("divergence_type"))
    declared_non_claims = _as_mapping(request_mapping.get("declared_non_claims"))
    detection = _detect_divergence(request_mapping, divergence_type, selected)
    checks = _build_divergence_checks(
        request_mapping,
        raw_evidence,
        selected,
        divergence_type,
        detection,
        declared_non_claims,
        precheck_failures,
    )
    failed_check = _first_failed(checks)

    if failed_check:
        outcome = CARRIER_DIVERGENCE_BLOCKED
        block_code = str(failed_check.get("block_code"))
    elif divergence_type == "NO_DIVERGENCE":
        outcome = NO_CARRIER_DIVERGENCE
        block_code = None
    elif detection.get("mismatch_visible"):
        outcome = CARRIER_DIVERGENCE_RECORDED
        block_code = None
    else:
        outcome = NO_CARRIER_DIVERGENCE
        block_code = None

    block_reason = _block_reason(block_code, failed_check)
    result: dict[str, Any] = {
        "cross_carrier_divergence_metadata": {
            "cross_carrier_divergence_result_id": _result_id(
                request_mapping,
                divergence_type,
                outcome,
            ),
            "cross_carrier_divergence_result_type": (
                "cross_carrier_divergence_boundary_result"
            ),
            "cross_carrier_divergence_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_divergence_question": _declared_divergence_question(
            request_mapping,
            divergence_type,
        ),
        "selected_carrier_evidence": selected,
        "divergence_basis": _divergence_basis(
            request_mapping,
            selected,
            divergence_type,
            detection,
        ),
        "divergence_checks": checks,
        "divergence_result": _divergence_result(
            outcome,
            selected,
            divergence_type,
            detection,
            block_code,
            block_reason,
            checks,
        ),
        "divergence_non_meaning": copy.deepcopy(DIVERGENCE_NON_MEANING),
        "divergence_consequence_boundary": _divergence_consequence_boundary(),
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
    result["cross_carrier_divergence_summary"] = (
        build_cross_carrier_divergence_summary(result)
    )
    return result


def _build_divergence_checks(
    request: Mapping[str, Any],
    raw_evidence: Any,
    selected: Sequence[Mapping[str, Any]],
    divergence_type: str | None,
    detection: Mapping[str, Any],
    declared_non_claims: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    sources = [
        request,
        raw_evidence,
        selected,
        _as_mapping(request.get("divergence_basis")),
        declared_non_claims,
    ]
    precheck_code = (
        precheck_failures[0]
        if precheck_failures
        else "DECLARED_DIVERGENCE_REQUEST_MALFORMED"
    )
    raw_is_sequence = isinstance(raw_evidence, list)
    checks = [
        _check(
            "declared_divergence_request_is_parseable_mapping",
            not precheck_failures,
            "declared divergence request is a mapping",
            list(precheck_failures),
            precheck_code,
        ),
        _check(
            "selected_evidence_exists",
            raw_evidence is not None,
            "selected carrier evidence is supplied",
            raw_evidence,
            "SELECTED_EVIDENCE_MISSING",
        ),
        _check(
            "selected_evidence_parseable",
            raw_evidence is None
            or (
                raw_is_sequence
                and all(isinstance(item, Mapping) for item in raw_evidence)
            ),
            "each selected evidence surface is a mapping",
            [type(item).__name__ for item in raw_evidence]
            if raw_is_sequence
            else type(raw_evidence).__name__,
            "SELECTED_EVIDENCE_MALFORMED",
        ),
        _check(
            "sufficient_evidence_surfaces",
            raw_is_sequence and len(raw_evidence) >= 2,
            "at least two selected evidence surfaces exist",
            len(raw_evidence) if raw_is_sequence else type(raw_evidence).__name__,
            "INSUFFICIENT_EVIDENCE_SURFACES",
        ),
        _check(
            "evidence_identity_present",
            bool(selected) and all(item.get("evidence_id") for item in selected),
            "each selected evidence identity is declared",
            [item.get("evidence_id") for item in selected],
            "EVIDENCE_IDENTITY_MISSING",
        ),
        _check(
            "evidence_outcome_present",
            bool(selected) and all(item.get("evidence_outcome") for item in selected),
            "each selected evidence outcome or status is declared",
            [item.get("evidence_outcome") for item in selected],
            "EVIDENCE_OUTCOME_MISSING",
        ),
        _check(
            "carrier_identity_present_where_required",
            bool(selected) and all(item.get("carrier_id") for item in selected),
            "selected carrier identities are declared",
            [item.get("carrier_id") for item in selected],
            "CARRIER_IDENTITY_MISSING",
        ),
        _check(
            "divergence_question_declared",
            bool(str(request.get("divergence_question") or "").strip()),
            "divergence question is declared",
            request.get("divergence_question"),
            "DIVERGENCE_QUESTION_UNDECLARED",
        ),
        _check(
            "divergence_type_supported",
            divergence_type in SUPPORTED_DIVERGENCE_TYPES,
            "divergence type is supported by this boundary",
            divergence_type,
            "DIVERGENCE_TYPE_UNSUPPORTED",
        ),
        _check(
            "mismatch_visible_where_required",
            divergence_type in SUPPORTED_DIVERGENCE_TYPES,
            "mismatch is visibly recorded when present; absence yields no-divergence",
            {
                "divergence_type": divergence_type,
                "mismatch_visible": detection.get("mismatch_visible"),
                "no_divergence_reason": detection.get("no_divergence_reason"),
            },
            "DIVERGENCE_HIDES_MISMATCH",
        ),
        _check(
            "refusal_visible_where_applicable",
            not _flag_true(sources, ("refusal_hidden", "divergence_hides_refusal")),
            "refusal remains visible where applicable",
            {
                "has_refusal_evidence": detection.get("has_refusal_evidence"),
                "has_success_evidence": detection.get("has_success_evidence"),
                "refusal_hidden": _flag_snapshot(
                    sources,
                    ("refusal_hidden", "divergence_hides_refusal"),
                ),
            },
            "DIVERGENCE_HIDES_REFUSAL",
        ),
    ]

    for check_name, aliases, expected, block_code in ANTI_COLLAPSE_CHECKS:
        actual = _flag_snapshot(sources, aliases)
        flagged = _flag_true(sources, aliases)
        effective_block_code = block_code
        if check_name == "divergence_does_not_create_successor_body" and (
            _flag_true(sources, ("divergence_creates_body", "body_created", "body_formed"))
        ):
            effective_block_code = "DIVERGENCE_CREATES_BODY"
        elif check_name == "divergence_does_not_establish_presence_threshold":
            if _flag_true(sources, ("threshold_met", "divergence_establishes_threshold")):
                effective_block_code = "DIVERGENCE_ESTABLISHES_THRESHOLD"
        elif check_name == "divergence_does_not_authorize_action_create_consequence":
            if _flag_true(sources, ("consequence_created", "divergence_creates_consequence")):
                effective_block_code = "DIVERGENCE_CREATES_CONSEQUENCE"
        elif check_name == "divergence_does_not_create_multi_carrier_law_distributed_standing":
            if _flag_true(
                sources,
                ("distributed_standing_created", "divergence_creates_distributed_standing"),
            ):
                effective_block_code = "DIVERGENCE_CREATES_DISTRIBUTED_STANDING"
        elif check_name == "divergence_does_not_resolve_by_majority_latest_success_count":
            if _flag_true(
                sources,
                ("divergence_resolved_by_latest_file", "divergence_resolves_by_latest_file"),
            ):
                effective_block_code = "DIVERGENCE_RESOLVES_BY_LATEST_FILE"
            elif _flag_true(
                sources,
                (
                    "divergence_resolved_by_success_count",
                    "divergence_resolves_by_success_count",
                ),
            ):
                effective_block_code = "DIVERGENCE_RESOLVES_BY_SUCCESS_COUNT"
        checks.append(
            _check(
                check_name,
                not flagged,
                expected,
                actual,
                effective_block_code,
            )
        )

    missing_or_flipped = _missing_or_flipped_non_claims(declared_non_claims)
    selected_non_claim_conflicts = _selected_non_claim_collapse(selected)
    checks.append(
        _check(
            "required_non_claims_remain_false",
            not missing_or_flipped and not selected_non_claim_conflicts,
            "all required divergence non-claims are present and false",
            {
                "declared_non_claim_failures": missing_or_flipped,
                "selected_evidence_non_claim_collapse": selected_non_claim_conflicts,
            },
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _detect_divergence(
    request: Mapping[str, Any],
    divergence_type: str | None,
    selected: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    if divergence_type not in SUPPORTED_DIVERGENCE_TYPES:
        return _detection(False, "unsupported_divergence_type", {})
    if not selected:
        return _detection(False, "selected_evidence_missing", {})

    evidence: dict[str, Any] = {}
    mismatch_visible = False
    no_reason = "selected evidence does not diverge for declared question"

    if divergence_type == "NO_DIVERGENCE":
        return _detection(False, "declared_no_divergence", evidence, selected)

    if divergence_type == "OUTCOME_DIVERGENCE":
        values = _unique_values(item.get("normalized_evidence_outcome") for item in selected)
        mismatch_visible = len(values) > 1
        evidence = {"outcome_values": values}
    elif divergence_type == "RECEIPT_REFUSAL_DIVERGENCE":
        has_refusal = any(item.get("refusal_or_blocked_outcome") for item in selected)
        has_success = any(item.get("received_or_success_outcome") for item in selected)
        mismatch_visible = has_refusal and has_success
        evidence = {"has_refusal_evidence": has_refusal, "has_success_evidence": has_success}
    elif divergence_type == "BASIS_DIVERGENCE":
        values = _unique_values(item.get("source_or_carried_basis_fingerprint") for item in selected)
        mismatch_visible = len(values) > 1
        evidence = {"source_or_carried_basis_values": values}
    elif divergence_type == "INTEGRITY_DIVERGENCE":
        hashes = _unique_values(item.get("integrity_hash") for item in selected)
        failures = [
            item.get("evidence_id")
            for item in selected
            if item.get("integrity_failure") is True
        ]
        mismatch_visible = len(hashes) > 1 or bool(failures)
        evidence = {"integrity_hashes": hashes, "integrity_failure_evidence_ids": failures}
    elif divergence_type == "CARRIER_IDENTITY_DIVERGENCE":
        values = _unique_values(item.get("carrier_id") for item in selected)
        mismatch_visible = len(values) > 1
        evidence = {"carrier_ids": values}
    elif divergence_type == "ROLE_DIVERGENCE":
        values = _unique_values(item.get("carrier_role") for item in selected)
        mismatch_visible = len(values) > 1
        evidence = {"carrier_roles": values}
    elif divergence_type == "EMISSION_CLASS_DIVERGENCE":
        values = _unique_values(item.get("emission_class") for item in selected)
        mismatch_visible = len(values) > 1
        evidence = {"emission_classes": values}
    elif divergence_type == "RETURN_PATH_DIVERGENCE":
        values = _unique_values(item.get("return_path") for item in selected)
        mismatch_visible = len(values) > 1
        evidence = {"return_paths": values}
    elif divergence_type == "NON_CLAIM_DIVERGENCE":
        conflict = _non_claim_divergence(selected)
        mismatch_visible = bool(conflict or _flag_true([request, selected], ("non_claim_conflict_visible",)))
        evidence = {"non_claim_conflicts": conflict}
    elif divergence_type == "STALE_OR_SEQUENCE_DIVERGENCE":
        values = _unique_values(item.get("sequence_or_version") for item in selected)
        mismatch_visible = len(values) > 1 or _flag_true(
            [request, selected],
            ("stale_or_sequence_mismatch", "stale_sequence_mismatch"),
        )
        evidence = {"sequence_or_version_values": values}
    elif divergence_type == "MISSING_EVIDENCE_DIVERGENCE":
        missing_ids = [
            item.get("evidence_id")
            for item in selected
            if item.get("missing_evidence") is True
        ]
        mismatch_visible = bool(missing_ids)
        evidence = {"missing_evidence_ids": missing_ids}
    elif divergence_type == "MALFORMED_EVIDENCE_DIVERGENCE":
        malformed_ids = [
            item.get("evidence_id")
            for item in selected
            if item.get("malformed_evidence") is True
        ]
        mismatch_visible = bool(malformed_ids)
        evidence = {"malformed_evidence_ids": malformed_ids}

    if mismatch_visible:
        no_reason = None
    return _detection(mismatch_visible, no_reason, evidence, selected)


def _detection(
    mismatch_visible: bool,
    no_divergence_reason: str | None,
    divergence_evidence: Mapping[str, Any],
    selected: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    selected_list = list(selected or [])
    has_refusal = any(item.get("refusal_or_blocked_outcome") for item in selected_list)
    has_success = any(item.get("received_or_success_outcome") for item in selected_list)
    return {
        "mismatch_visible": bool(mismatch_visible),
        "visible_divergence": bool(mismatch_visible),
        "hidden_divergence": False,
        "no_divergence_reason": no_divergence_reason,
        "divergence_evidence": copy.deepcopy(dict(divergence_evidence)),
        "has_refusal_evidence": has_refusal,
        "has_success_evidence": has_success,
    }


def _normalize_selected_evidence(raw_evidence: Any) -> list[dict[str, Any]]:
    if not isinstance(raw_evidence, list):
        return []
    normalized: list[dict[str, Any]] = []
    for index, raw_item in enumerate(raw_evidence):
        if not isinstance(raw_item, Mapping):
            continue
        item = _as_mapping(raw_item)
        outcome = _first_text(
            item,
            (
                "evidence_outcome",
                "outcome",
                "status",
                "emission_outcome",
                "receipt_outcome",
                "admission_outcome",
                "result_outcome",
            ),
        )
        normalized_outcome = _normalize_token(outcome)
        carrier = _as_mapping(
            item.get("carrier")
            or item.get("selected_carrier")
            or item.get("emitting_carrier")
            or item.get("receiving_carrier")
        )
        source_basis = _selected_source_basis(item)
        integrity = _as_mapping(
            item.get("integrity_evidence")
            or item.get("integrity")
            or item.get("carried_surface_integrity")
        )
        block = _as_mapping(item.get("block"))
        non_claims = _as_mapping(item.get("non_claims"))
        return_basis = _as_mapping(item.get("return_basis"))
        normalized.append(
            {
                "evidence_index": index,
                "evidence_id": _first_text(
                    item,
                    (
                        "evidence_id",
                        "id",
                        "emission_id",
                        "receipt_id",
                        "admission_id",
                        "surface_id",
                        "result_id",
                        "selected_evidence_id",
                    ),
                ),
                "evidence_outcome": outcome,
                "normalized_evidence_outcome": normalized_outcome,
                "carrier_id": _first_text(
                    item,
                    (
                        "carrier_id",
                        "emitting_carrier_id",
                        "receiving_carrier_id",
                        "source_carrier_id",
                        "selected_carrier_id",
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
                "source_or_carried_basis": copy.deepcopy(source_basis),
                "source_or_carried_basis_fingerprint": _fingerprint(source_basis),
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
                or _first_text(integrity, ("integrity_hash", "hash", "sha256", "content_hash")),
                "integrity_status": _first_text(
                    item,
                    ("integrity_status", "integrity_outcome", "hash_status"),
                )
                or _first_text(integrity, ("integrity_status", "outcome", "status")),
                "integrity_failure": _integrity_failure(item, integrity),
                "block_code": _first_text(item, ("block_code", "code"))
                or _first_text(block, ("block_code", "code")),
                "block_reason": _first_text(item, ("block_reason", "reason"))
                or _first_text(block, ("block_reason", "reason")),
                "non_claims": non_claims,
                "sequence_or_version": _sequence_or_version(item),
                "missing_evidence": _missing_evidence(item, normalized_outcome),
                "malformed_evidence": _malformed_evidence(item, normalized_outcome),
                "refusal_or_blocked_outcome": _is_refusal_or_blocked(normalized_outcome),
                "received_or_success_outcome": _is_received_or_success(normalized_outcome),
                "raw_evidence": copy.deepcopy(dict(item)),
            }
        )
    return normalized


def _selected_source_basis(item: Mapping[str, Any]) -> Any:
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


def _integrity_failure(
    item: Mapping[str, Any],
    integrity: Mapping[str, Any],
) -> bool:
    if _flag_true(
        [item, integrity],
        (
            "integrity_failure",
            "integrity_failed",
            "integrity_check_failed",
            "hash_mismatch",
            "integrity_mismatch",
        ),
    ):
        return True
    status = _normalize_token(
        _first_text(item, ("integrity_status", "hash_status"))
        or _first_text(integrity, ("integrity_status", "outcome", "status"))
    )
    return bool(status and ("FAIL" in status or "MISMATCH" in status))


def _sequence_or_version(item: Mapping[str, Any]) -> Any:
    for key in (
        "sequence",
        "version",
        "evidence_version",
        "basis_order",
        "basis_sequence",
        "timestamp",
        "generated_at",
        "created_at",
        "returned_at",
        "admitted_at",
    ):
        value = item.get(key)
        if value is not None:
            return _fingerprint(value)
    return None


def _missing_evidence(item: Mapping[str, Any], normalized_outcome: str | None) -> bool:
    return _flag_true(
        [item],
        ("missing_evidence", "evidence_missing", "is_missing"),
    ) or normalized_outcome in {"MISSING", "EVIDENCE_MISSING", "SELECTED_EVIDENCE_MISSING"}


def _malformed_evidence(item: Mapping[str, Any], normalized_outcome: str | None) -> bool:
    return _flag_true(
        [item],
        ("malformed_evidence", "evidence_malformed", "is_malformed"),
    ) or normalized_outcome in {
        "MALFORMED",
        "EVIDENCE_MALFORMED",
        "SELECTED_EVIDENCE_MALFORMED",
    }


def _is_refusal_or_blocked(normalized_outcome: str | None) -> bool:
    if normalized_outcome is None:
        return False
    if normalized_outcome in BLOCKED_OR_REFUSAL_OUTCOME_HINTS:
        return True
    return "BLOCK" in normalized_outcome or "REFUS" in normalized_outcome


def _is_received_or_success(normalized_outcome: str | None) -> bool:
    if normalized_outcome is None:
        return False
    if normalized_outcome in RECEIVED_OR_SUCCESS_OUTCOME_HINTS:
        return True
    return (
        "RECEIVED" in normalized_outcome
        or "ADMITTED" in normalized_outcome
        or "SUCCESS" in normalized_outcome
        or "RECOGNIZED" in normalized_outcome
        or "CONFORMANT" in normalized_outcome
    )


def _declared_divergence_question(
    request: Mapping[str, Any],
    divergence_type: str | None,
) -> dict[str, Any]:
    return {
        "divergence_request_id": request.get("divergence_request_id"),
        "divergence_question": request.get("divergence_question"),
        "divergence_purpose": request.get("divergence_purpose"),
        "declared_scope": request.get("declared_scope"),
        "divergence_type": divergence_type,
        "raw_divergence_type": request.get("divergence_type"),
        "expected_comparison_basis": copy.deepcopy(
            request.get("expected_comparison_basis")
        ),
        "allow_returned_not_admitted_evidence": bool(
            request.get("allow_returned_not_admitted_evidence")
        ),
        "selected_admission_basis": copy.deepcopy(
            request.get("selected_admission_basis")
        ),
        "selected_correspondence_basis": copy.deepcopy(
            request.get("selected_correspondence_basis")
        ),
        "declared_non_claims": copy.deepcopy(request.get("declared_non_claims")),
        "declared_divergence_request_path": request.get(
            "_declared_divergence_request_path"
        ),
    }


def _divergence_basis(
    request: Mapping[str, Any],
    selected: Sequence[Mapping[str, Any]],
    divergence_type: str | None,
    detection: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "divergence_type": divergence_type,
        "supported_divergence_types": sorted(SUPPORTED_DIVERGENCE_TYPES),
        "positive_divergence_types": sorted(POSITIVE_DIVERGENCE_TYPES),
        "divergence_type_supported": divergence_type in SUPPORTED_DIVERGENCE_TYPES,
        "selected_evidence_count": len(selected),
        "selected_evidence_ids": [item.get("evidence_id") for item in selected],
        "selected_evidence_outcomes": [
            item.get("evidence_outcome") for item in selected
        ],
        "selected_carrier_ids": [item.get("carrier_id") for item in selected],
        "selected_carrier_roles": [item.get("carrier_role") for item in selected],
        "selected_emission_classes": [
            item.get("emission_class") for item in selected
        ],
        "selected_return_paths": [item.get("return_path") for item in selected],
        "visible_mismatch": bool(detection.get("mismatch_visible")),
        "hidden_divergence": False,
        "divergence_evidence": copy.deepcopy(detection.get("divergence_evidence")),
        "expected_comparison_basis": copy.deepcopy(
            request.get("expected_comparison_basis")
        ),
        "allow_returned_not_admitted_evidence": bool(
            request.get("allow_returned_not_admitted_evidence")
        ),
        "selected_admission_basis": copy.deepcopy(
            request.get("selected_admission_basis")
        ),
        "selected_correspondence_basis": copy.deepcopy(
            request.get("selected_correspondence_basis")
        ),
        "non_claims_explicit": bool(_as_mapping(request.get("declared_non_claims"))),
    }


def _divergence_result(
    outcome: str,
    selected: Sequence[Mapping[str, Any]],
    divergence_type: str | None,
    detection: Mapping[str, Any],
    block_code: str | None,
    block_reason: str | None,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    recorded = outcome == CARRIER_DIVERGENCE_RECORDED
    no_divergence = outcome == NO_CARRIER_DIVERGENCE
    blocked = outcome == CARRIER_DIVERGENCE_BLOCKED
    failed_checks = [
        copy.deepcopy(dict(check)) for check in checks if check.get("passed") is False
    ]
    selected_ids = [item.get("evidence_id") for item in selected]
    selected_outcomes = [item.get("evidence_outcome") for item in selected]
    selected_carrier_ids = [item.get("carrier_id") for item in selected]
    return {
        "divergence_recorded": recorded,
        "visible_divergence": recorded,
        "hidden_divergence": False,
        "divergence_type": divergence_type,
        "divergence_claim": (
            "selected carrier evidence diverges visibly for the declared question"
            if recorded
            else None
        ),
        "selected_evidence_count": len(selected),
        "selected_evidence_ids": selected_ids,
        "selected_evidence_outcomes": selected_outcomes,
        "selected_carrier_ids": selected_carrier_ids,
        "divergence_evidence": copy.deepcopy(detection.get("divergence_evidence")),
        "mismatch_preserved": recorded,
        "refusal_hidden": False,
        "mismatch_hidden": False,
        "evidence_overwritten": False,
        "source_not_replaced": True,
        "currentness_not_created": True,
        "authority_not_created": True,
        "permission_not_created": True,
        "truth_not_created": True,
        "action_not_authorized": True,
        "carrier_hierarchy_not_created": True,
        "multi_carrier_law_not_created": True,
        "distributed_standing_not_created": True,
        "continuation_not_authorized": True,
        "no_carrier_divergence": no_divergence,
        "no_divergence_reason": detection.get("no_divergence_reason")
        if no_divergence
        else None,
        "selected_evidence_preserved": no_divergence or blocked,
        "divergence_blocked": blocked,
        "block_code": block_code,
        "block_reason": block_reason,
        "failed_checks": failed_checks if blocked else [],
        "selected_basis_preserved_where_available": blocked,
    }


def _divergence_consequence_boundary() -> dict[str, Any]:
    return {
        "divergence_may": {
            "prevent_downstream_reliance": True,
            "require_later_correspondence_review": True,
            "require_later_admission_review": True,
            "require_later_currentness_boundary_review": True,
            "remain_open_as_visible_divergence": True,
            "be_used_as_evidence_for_future_block": True,
        },
        "divergence_may_not": {
            "decide_source": True,
            "decide_currentness": True,
            "decide_truth": True,
            "decide_action": True,
            "select_winning_carrier": True,
            "erase_losing_carrier_evidence": True,
            "create_carrier_hierarchy": True,
            "create_carrier_relation": True,
            "create_multi_carrier_law": True,
            "create_distributed_standing": True,
            "authorize_continuation": True,
        },
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_surfaces": list(OPEN_SURFACES),
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    selected_path = Path(path)
    try:
        raw = selected_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CrossCarrierDivergenceBoundaryError(
            "DECLARED_DIVERGENCE_REQUEST_UNREADABLE",
            f"{BLOCK_REASONS['DECLARED_DIVERGENCE_REQUEST_UNREADABLE']} path={selected_path} detail={exc}",
        ) from exc
    try:
        loaded = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CrossCarrierDivergenceBoundaryError(
            "DECLARED_DIVERGENCE_REQUEST_MALFORMED",
            f"{BLOCK_REASONS['DECLARED_DIVERGENCE_REQUEST_MALFORMED']} path={selected_path} detail={exc}",
        ) from exc
    if not isinstance(loaded, Mapping):
        raise CrossCarrierDivergenceBoundaryError(
            "DECLARED_DIVERGENCE_REQUEST_MALFORMED",
            f"{BLOCK_REASONS['DECLARED_DIVERGENCE_REQUEST_MALFORMED']} path={selected_path} expected object",
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
        if check.get("passed") is not True:
            return check
    return None


def _block_reason(
    block_code: str | None,
    failed_check: Mapping[str, Any] | None,
) -> str | None:
    if block_code is None:
        return None
    reason = BLOCK_REASONS.get(block_code, "Cross-carrier divergence blocked.")
    if failed_check:
        return f"{reason} failed check: {failed_check.get('check_name')}"
    return reason


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]


def _first_text(mapping: Mapping[str, Any], keys: Sequence[str]) -> str | None:
    for key in keys:
        value = mapping.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _normalize_token(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    normalized: list[str] = []
    previous_underscore = False
    for character in value.strip().upper():
        if character.isalnum():
            normalized.append(character)
            previous_underscore = False
        elif not previous_underscore:
            normalized.append("_")
            previous_underscore = True
    token = "".join(normalized).strip("_")
    return token or None


def _normalize_key(value: Any) -> str:
    return _normalize_token(str(value)) or ""


def _flag_true(sources: Sequence[Any], aliases: Sequence[str]) -> bool:
    alias_set = {_normalize_key(alias) for alias in aliases}
    for source in sources:
        if _contains_true_key(source, alias_set):
            return True
    return False


def _contains_true_key(value: Any, alias_set: set[str]) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if _normalize_key(key) in alias_set and item is True:
                return True
            if isinstance(item, (Mapping, list)) and _contains_true_key(item, alias_set):
                return True
    elif isinstance(value, list):
        for item in value:
            if _contains_true_key(item, alias_set):
                return True
    return False


def _flag_snapshot(sources: Sequence[Any], aliases: Sequence[str]) -> dict[str, Any]:
    alias_set = {_normalize_key(alias) for alias in aliases}
    found: dict[str, Any] = {}
    for source in sources:
        _collect_flag_snapshot(source, alias_set, found)
    return found


def _collect_flag_snapshot(
    value: Any,
    alias_set: set[str],
    found: dict[str, Any],
) -> None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if _normalize_key(key) in alias_set:
                found[str(key)] = copy.deepcopy(item)
            if isinstance(item, (Mapping, list)):
                _collect_flag_snapshot(item, alias_set, found)
    elif isinstance(value, list):
        for item in value:
            _collect_flag_snapshot(item, alias_set, found)


def _missing_or_flipped_non_claims(non_claims: Mapping[str, Any]) -> list[str]:
    if not isinstance(non_claims, Mapping) or not non_claims:
        return list(REQUIRED_NON_CLAIMS)
    return [
        key
        for key, expected in REQUIRED_NON_CLAIMS.items()
        if non_claims.get(key) is not expected
    ]


def _selected_non_claim_collapse(
    selected: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    for item in selected:
        non_claims = _as_mapping(item.get("non_claims"))
        for key in REQUIRED_NON_CLAIMS:
            if key in non_claims and non_claims.get(key) is not False:
                failures.append(
                    {
                        "evidence_id": item.get("evidence_id"),
                        "non_claim": key,
                        "value": non_claims.get(key),
                    }
                )
    return failures


def _non_claim_divergence(
    selected: Sequence[Mapping[str, Any]],
) -> dict[str, list[Any]]:
    conflicts: dict[str, list[Any]] = {}
    for key in REQUIRED_NON_CLAIMS:
        values: list[Any] = []
        for item in selected:
            non_claims = _as_mapping(item.get("non_claims"))
            if key in non_claims:
                values.append(non_claims.get(key))
        if len(set(json.dumps(value, sort_keys=True) for value in values)) > 1:
            conflicts[key] = values
    return conflicts


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "source_replaced",
        "divergence_hidden",
        "refusal_hidden",
        "mismatch_hidden",
        "evidence_overwritten",
        "divergence_resolved_by_majority",
        "divergence_resolved_by_latest_file",
        "divergence_resolved_by_success_count",
        "carrier_hierarchy_created",
        "winning_carrier_selected",
        "losing_carrier_invalidated",
        "carrier_relation_created",
        "multi_carrier_law_created",
        "distributed_standing_created",
        "signal_created_by_default",
        "presence_established",
        "threshold_met",
        "truth_created",
        "action_authorized",
        "consequence_created",
        "continuation_authorized",
    )
    return {key: non_claims.get(key) for key in keys}


def _unique_values(values: Any) -> list[Any]:
    seen: set[str] = set()
    unique: list[Any] = []
    for value in values:
        if value in (None, "", [], {}):
            continue
        key = _fingerprint(value)
        if key not in seen:
            seen.add(key)
            unique.append(copy.deepcopy(value))
    return unique


def _fingerprint(value: Any) -> str | None:
    if value in (None, "", [], {}):
        return None
    try:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)
    except TypeError:
        return str(value)


def _result_id(
    request: Mapping[str, Any],
    divergence_type: str | None,
    outcome: str,
) -> str:
    base = (
        request.get("divergence_request_id")
        or divergence_type
        or "cross_carrier_divergence"
    )
    return (
        f"{_safe_filename_part(base)}__{outcome.lower()}"
        "__cross_carrier_divergence_result"
    )


def _safe_filename_part(value: Any) -> str:
    text = str(value or "cross_carrier_divergence")
    allowed: list[str] = []
    previous_underscore = False
    for character in text:
        if character.isalnum() or character in "._-":
            allowed.append(character)
            previous_underscore = False
        elif not previous_underscore:
            allowed.append("_")
            previous_underscore = True
    stem = "".join(allowed).strip("._")
    return stem[:180] or "cross_carrier_divergence"


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
