"""Bounded carrier-local emission admission boundary resolver.

This resolver records whether one carrier-local or returned emission may be
admitted into the body line as evidence. It preserves the distinction between
local emission, return, and body-line admission. It does not create source,
currentness, authority, permission, successor standing, body formation, signal,
presence, threshold, truth, action, consequence, multi-carrier law, distributed
standing, or continuation.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CarrierLocalEmissionAdmissionBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit admission inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


CARRIER_LOCAL_EMISSION_ADMISSION_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_carrier_local_emission_admission_boundary"
)

RESOLVER_MODULE = "resolve_carrier_local_emission_admission_boundary"
RESULT_VERSION = "0.1.0"

CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE = (
    "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE"
)
CARRIER_LOCAL_EMISSION_NOT_ADMITTED = "CARRIER_LOCAL_EMISSION_NOT_ADMITTED"
CARRIER_LOCAL_EMISSION_ADMISSION_BLOCKED = "CARRIER_LOCAL_EMISSION_ADMISSION_BLOCKED"

EMITTED_LOCAL = "EMITTED_LOCAL"
RETURNED_TO_BODY_LINE = "RETURNED_TO_BODY_LINE"
ADMITTED_AS_EVIDENCE = "ADMITTED_AS_EVIDENCE"
NOT_ADMITTED = "NOT_ADMITTED"
ADMISSION_BLOCKED = "ADMISSION_BLOCKED"

ADMITTED_CARRIER_ROLES = {
    "SOURCE_CARRIER_FOR_PACKET",
    "RECEIVING_CARRIER",
    "HOLDING_CARRIER",
    "RETURNING_CARRIER",
    "REFUSING_CARRIER",
}

ADMISSIBLE_EMISSION_CLASSES = {
    "CARRIED_SURFACE_RECEIPT",
    "RECEIPT_BLOCK",
    "RECEIPT_REFUSAL_REASON",
    "RETURNED_RECEIPT_EVIDENCE",
    "RETURNED_BLOCKED_RECEIPT_EVIDENCE",
    "RETURNED_EVIDENCE_PACKET",
    "INTEGRITY_EVIDENCE",
    "PACKET_MANIFEST",
    "TRANSFER_DECLARATION",
}

NOT_ADMITTED_EMISSION_CLASSES = {
    "SELF_ORIENTATION",
    "BODY_CONFORMANCE",
    "CURRENTNESS",
    "STANDING_UPGRADE",
    "SOURCE_AUTHORITY",
    "SUCCESSOR_ARTIFACT",
    "PRESENCE",
    "THRESHOLD",
    "TRUTH",
    "ACTION",
    "CONSEQUENCE",
    "MULTI_CARRIER_RELATION",
    "DISTRIBUTED_STANDING",
    "CARRIER_REGISTRY",
    "REPOSITORY_SYNCHRONIZATION",
    "SIGNAL_BY_DEFAULT",
    "BODY_RELEVANCE_MEDIUM",
    "WORKFLOW",
    "ROUTING",
    "CONTINUATION_AUTHORIZATION",
}

POSITIVE_ADMISSION_INTENTS = {
    "ADMIT",
    "ADMIT_AS_EVIDENCE",
    "ADMITTED_AS_EVIDENCE",
    "REQUEST_ADMISSION",
    "ADMISSION_REQUESTED",
    "BODY_LINE_ADMISSION_REQUESTED",
}

NON_ADMISSION_INTENTS = {
    "DO_NOT_ADMIT",
    "NOT_ADMITTED",
    "NO_ADMISSION",
    "PRESERVE_WITHOUT_ADMISSION",
    "RECORD_WITHOUT_ADMISSION",
    "EMITTED_LOCAL_ONLY",
    "RETURNED_ONLY",
    "RETURNED_TO_BODY_LINE_ONLY",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "carrier_emission_self_admitted": False,
    "returned_emission_self_admitted": False,
    "emission_admission_created_source": False,
    "emission_admission_created_currentness": False,
    "emission_admission_created_authority": False,
    "emission_admission_created_permission": False,
    "emission_admission_created_successor": False,
    "emission_admission_created_body": False,
    "emission_admission_created_signal_by_default": False,
    "presence_established": False,
    "threshold_met": False,
    "truth_created": False,
    "action_authorized": False,
    "consequence_created": False,
    "multi_carrier_law_created": False,
    "distributed_standing_created": False,
    "continuation_authorized": False,
    "refusal_hidden": False,
    "divergence_hidden": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "DECLARED_ADMISSION_REQUEST_MISSING": "No declared admission request was supplied.",
    "DECLARED_ADMISSION_REQUEST_UNREADABLE": "The declared admission request path could not be read.",
    "DECLARED_ADMISSION_REQUEST_MALFORMED": "The declared admission request is not a JSON object or mapping.",
    "CARRIER_LOCAL_EMISSION_MISSING": "Carrier-local emission is missing.",
    "CARRIER_LOCAL_EMISSION_MALFORMED": "Carrier-local emission is malformed.",
    "EMISSION_IDENTITY_MISSING": "Emission identity is missing.",
    "EMISSION_OUTCOME_MISSING": "Emission outcome or status is missing.",
    "EMITTING_CARRIER_MISSING": "Emitting carrier identity is missing.",
    "CARRIER_ROLE_MISSING": "Carrier role is missing.",
    "CARRIER_ROLE_UNSUPPORTED": "Carrier role is unsupported or unbounded.",
    "EMISSION_CLASS_MISSING": "Emission class is missing.",
    "EMISSION_CLASS_UNSUPPORTED": "Emission class is not admissible.",
    "ADMISSION_PURPOSE_UNDECLARED": "Admission purpose is undeclared.",
    "ADMISSION_INTENT_UNDECLARED": "Admission intent is undeclared.",
    "EMISSION_SELF_ADMITTED": "Emission claims admission by being emitted.",
    "RETURN_MISTAKEN_FOR_ADMISSION": "Return is mistaken for admission.",
    "POSSESSION_MISTAKEN_FOR_ADMISSION": "Possession is mistaken for admission.",
    "RECEIPT_MISTAKEN_FOR_ADMISSION": "Receipt is mistaken for admission.",
    "CORRESPONDENCE_MISTAKEN_FOR_ADMISSION": "Correspondence is mistaken for admission.",
    "SELF_ORIENTATION_RECOGNITION_MISTAKEN_FOR_ADMISSION": "Self-orientation recognition is mistaken for admission.",
    "ADMISSION_REPLACES_SOURCE": "Admission replaces source.",
    "ADMISSION_CREATES_CURRENTNESS": "Admission creates currentness.",
    "ADMISSION_CREATES_AUTHORITY": "Admission creates authority.",
    "ADMISSION_CREATES_PERMISSION": "Admission creates permission.",
    "ADMISSION_CREATES_SUCCESSOR": "Admission creates successor standing.",
    "ADMISSION_CREATES_BODY": "Admission creates body formation.",
    "ADMISSION_CREATES_SIGNAL_BY_DEFAULT": "Admission creates signal by default.",
    "ADMISSION_ESTABLISHES_PRESENCE": "Admission establishes presence.",
    "ADMISSION_ESTABLISHES_THRESHOLD": "Admission establishes threshold.",
    "ADMISSION_CREATES_TRUTH": "Admission creates truth.",
    "ADMISSION_AUTHORIZES_ACTION": "Admission authorizes action.",
    "ADMISSION_CREATES_CONSEQUENCE": "Admission creates consequence.",
    "ADMISSION_CREATES_MULTI_CARRIER_LAW": "Admission creates multi-carrier law.",
    "ADMISSION_CREATES_DISTRIBUTED_STANDING": "Admission creates distributed standing.",
    "ADMISSION_AUTHORIZES_CONTINUATION": "Admission authorizes continuation.",
    "ADMISSION_HIDES_REFUSAL": "Admission hides refusal.",
    "ADMISSION_HIDES_DIVERGENCE": "Admission hides divergence.",
    "ADMISSION_MUTATES_OR_REPLAYS_EMISSION": "Admission mutates, replays, or merges emission.",
    "LATEST_FILE_CURRENTNESS": "Latest-file recency is treated as currentness.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required admission non-claim is missing or flipped.",
}

ADMISSION_NON_MEANING = {
    "does_not_mean_emission": True,
    "does_not_mean_return": True,
    "does_not_mean_possession": True,
    "does_not_mean_receipt": True,
    "does_not_mean_correspondence": True,
    "does_not_mean_self_orientation_recognition": True,
    "does_not_mean_currentness": True,
    "does_not_mean_source": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_successor": True,
    "does_not_mean_body": True,
    "does_not_mean_carrier_participation_by_default": True,
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
    "does_not_mean_self_orientation_successor": True,
    "does_not_mean_conformance_successor": True,
}

OPEN_SURFACES = [
    "carrier-local emission admission implementation refinement",
    "cross-carrier divergence boundary",
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

MISTAKEN_ADMISSION_CHECKS = (
    (
        "emission_not_self_admitted",
        (
            "carrier_emission_self_admitted",
            "carrier_emission_self_admits",
            "emission_self_admitted",
            "emission_self_admits",
            "emitted_local_self_admitted",
            "body_line_admitted_by_emission",
        ),
        "emission does not self-admit by being emitted",
        "EMISSION_SELF_ADMITTED",
    ),
    (
        "return_not_mistaken_for_admission",
        (
            "returned_emission_self_admitted",
            "return_mistaken_for_admission",
            "returned_by_itself_admitted",
            "returned_evidence_self_admitted",
        ),
        "return does not create admission",
        "RETURN_MISTAKEN_FOR_ADMISSION",
    ),
    (
        "possession_not_mistaken_for_admission",
        (
            "possession_mistaken_for_admission",
            "passive_storage_admitted",
            "bytes_present_admitted",
        ),
        "possession does not create admission",
        "POSSESSION_MISTAKEN_FOR_ADMISSION",
    ),
    (
        "receipt_not_mistaken_for_admission",
        (
            "receipt_mistaken_for_admission",
            "receipt_self_admitted",
            "receipt_is_admission",
        ),
        "receipt does not create admission by itself",
        "RECEIPT_MISTAKEN_FOR_ADMISSION",
    ),
    (
        "correspondence_not_mistaken_for_admission",
        (
            "correspondence_mistaken_for_admission",
            "correspondence_self_admitted",
            "correspondence_is_admission",
        ),
        "correspondence does not create admission by itself",
        "CORRESPONDENCE_MISTAKEN_FOR_ADMISSION",
    ),
    (
        "self_orientation_recognition_not_mistaken_for_admission",
        (
            "self_orientation_recognition_mistaken_for_admission",
            "self_orientation_recognition_self_admitted",
            "self_orientation_is_admission",
        ),
        "self-orientation recognition does not create admission by itself",
        "SELF_ORIENTATION_RECOGNITION_MISTAKEN_FOR_ADMISSION",
    ),
)

ANTI_COLLAPSE_CHECKS = (
    (
        "source_not_replaced",
        ("source_replaced", "admission_replaces_source", "emission_admission_created_source"),
        "admission does not replace source or create source",
        "ADMISSION_REPLACES_SOURCE",
    ),
    (
        "currentness_not_created",
        (
            "currentness_created",
            "admission_creates_currentness",
            "emission_admission_created_currentness",
        ),
        "admission creates no currentness",
        "ADMISSION_CREATES_CURRENTNESS",
    ),
    (
        "authority_not_created",
        ("authority_created", "admission_creates_authority", "emission_admission_created_authority"),
        "admission creates no authority",
        "ADMISSION_CREATES_AUTHORITY",
    ),
    (
        "permission_not_created",
        ("permission_created", "admission_creates_permission", "emission_admission_created_permission"),
        "admission creates no permission",
        "ADMISSION_CREATES_PERMISSION",
    ),
    (
        "successor_not_created",
        (
            "emission_admission_created_successor",
            "admission_creates_successor",
            "successor_standing_created",
        ),
        "admission creates no successor standing",
        "ADMISSION_CREATES_SUCCESSOR",
    ),
    (
        "body_not_created",
        ("emission_admission_created_body", "admission_creates_body", "body_formed", "body_created"),
        "admission creates no body formation",
        "ADMISSION_CREATES_BODY",
    ),
    (
        "signal_not_created_by_default",
        (
            "emission_admission_created_signal_by_default",
            "admission_creates_signal_by_default",
            "signal_created_by_default",
        ),
        "admission creates no signal by default",
        "ADMISSION_CREATES_SIGNAL_BY_DEFAULT",
    ),
    (
        "presence_not_established",
        ("presence_established", "admission_establishes_presence"),
        "admission establishes no presence",
        "ADMISSION_ESTABLISHES_PRESENCE",
    ),
    (
        "threshold_not_met",
        ("threshold_met", "admission_establishes_threshold"),
        "admission establishes no threshold",
        "ADMISSION_ESTABLISHES_THRESHOLD",
    ),
    (
        "truth_not_created",
        ("truth_created", "admission_creates_truth"),
        "admission creates no truth",
        "ADMISSION_CREATES_TRUTH",
    ),
    (
        "action_not_authorized",
        ("action_authorized", "admission_authorizes_action"),
        "admission authorizes no action",
        "ADMISSION_AUTHORIZES_ACTION",
    ),
    (
        "consequence_not_created",
        ("consequence_created", "admission_creates_consequence"),
        "admission creates no consequence",
        "ADMISSION_CREATES_CONSEQUENCE",
    ),
    (
        "multi_carrier_law_not_created",
        ("multi_carrier_law_created", "admission_creates_multi_carrier_law"),
        "admission creates no multi-carrier law",
        "ADMISSION_CREATES_MULTI_CARRIER_LAW",
    ),
    (
        "distributed_standing_not_created",
        ("distributed_standing_created", "admission_creates_distributed_standing"),
        "admission creates no distributed standing",
        "ADMISSION_CREATES_DISTRIBUTED_STANDING",
    ),
    (
        "continuation_not_authorized",
        (
            "continuation_authorized",
            "admission_authorizes_continuation",
            "follow_on_work_authorized",
            "follow_on_steps_authorized",
        ),
        "admission authorizes no continuation",
        "ADMISSION_AUTHORIZES_CONTINUATION",
    ),
    (
        "refusal_not_hidden",
        ("refusal_hidden", "admission_hides_refusal", "hides_refusal"),
        "admission does not hide refusal",
        "ADMISSION_HIDES_REFUSAL",
    ),
    (
        "divergence_not_hidden",
        ("divergence_hidden", "admission_hides_divergence", "hides_divergence"),
        "admission does not hide divergence",
        "ADMISSION_HIDES_DIVERGENCE",
    ),
    (
        "mutation_replay_merge_not_performed",
        (
            "mutation_performed",
            "replay_performed",
            "merge_performed",
            "admission_mutates_or_replays_emission",
            "admission_mutates_emission",
            "admission_replays_emission",
            "admission_merges_emission",
        ),
        "admission performs no mutation, replay, or merge",
        "ADMISSION_MUTATES_OR_REPLAYS_EMISSION",
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


def resolve_carrier_local_emission_admission_boundary(
    declared_admission_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one declared carrier-local emission admission request."""

    if declared_admission_request is None:
        request: dict[str, Any] = {}
        precheck_failures = ["DECLARED_ADMISSION_REQUEST_MISSING"]
    elif not isinstance(declared_admission_request, Mapping):
        request = {}
        precheck_failures = ["DECLARED_ADMISSION_REQUEST_MALFORMED"]
    else:
        request = copy.deepcopy(dict(declared_admission_request))
        precheck_failures = []
    return _resolve_request(request, precheck_failures)


def resolve_carrier_local_emission_admission_boundary_from_path(
    declared_admission_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one declared admission request JSON path."""

    try:
        request = _read_json_mapping(declared_admission_request_path)
        request["_declared_admission_request_path"] = str(
            Path(declared_admission_request_path)
        )
        precheck_failures: list[str] = []
    except CarrierLocalEmissionAdmissionBoundaryError as exc:
        request = {}
        precheck_failures = [exc.block_code]
    return _resolve_request(request, precheck_failures)


def write_carrier_local_emission_admission_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded admission result artifact without overwriting."""

    if output_path is None:
        question = _as_mapping(result.get("declared_admission_question"))
        selected = _as_mapping(result.get("selected_carrier_emission"))
        basis_id = (
            question.get("admission_request_id")
            or selected.get("emission_id")
            or "carrier_local_emission_admission"
        )
        filename = (
            f"{_safe_filename_part(basis_id)}"
            "__carrier_local_emission_admission_result.json"
        )
        target = CARRIER_LOCAL_EMISSION_ADMISSION_BOUNDARY_ROOT / filename
    else:
        target = Path(output_path)
    target = _non_overwriting_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    return target


def build_carrier_local_emission_admission_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact bounded summary for an admission result."""

    checks = _mapping_list(result.get("admission_checks"))
    question = _as_mapping(result.get("declared_admission_question"))
    selected = _as_mapping(result.get("selected_carrier_emission"))
    role_basis = _as_mapping(result.get("carrier_role_basis"))
    emission_basis = _as_mapping(result.get("emission_basis"))
    return_basis = _as_mapping(result.get("return_basis"))
    statement = _as_mapping(result.get("admission_statement"))
    non_claims = _as_mapping(result.get("non_claims"))
    block = _as_mapping(result.get("block"))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "admission_request_id": question.get("admission_request_id"),
        "admission_purpose": question.get("admission_purpose"),
        "admission_intent": question.get("admission_intent"),
        "selected_emission_id": selected.get("emission_id"),
        "selected_emission_outcome": selected.get("emission_outcome"),
        "emitting_carrier_id": selected.get("emitting_carrier_id"),
        "carrier_role": role_basis.get("carrier_role"),
        "emission_class": emission_basis.get("emission_class"),
        "return_path": return_basis.get("return_path"),
        "return_context": return_basis.get("return_context"),
        "admission_as_evidence": bool(
            statement.get("carrier_local_emission_admitted_as_evidence")
        ),
        "not_admitted": result.get("outcome") == CARRIER_LOCAL_EMISSION_NOT_ADMITTED,
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "source_created": bool(
            non_claims.get("source_replaced")
            or non_claims.get("emission_admission_created_source")
        ),
        "currentness_created": bool(
            non_claims.get("currentness_created")
            or non_claims.get("emission_admission_created_currentness")
        ),
        "authority_created": bool(
            non_claims.get("authority_created")
            or non_claims.get("emission_admission_created_authority")
        ),
        "permission_created": bool(
            non_claims.get("permission_created")
            or non_claims.get("emission_admission_created_permission")
        ),
        "successor_created": bool(
            non_claims.get("emission_admission_created_successor")
        ),
        "body_created": bool(non_claims.get("emission_admission_created_body")),
        "signal_created_by_default": bool(
            non_claims.get("emission_admission_created_signal_by_default")
        ),
        "presence_established": bool(non_claims.get("presence_established")),
        "threshold_met": bool(non_claims.get("threshold_met")),
        "truth_created": bool(non_claims.get("truth_created")),
        "action_authorized": bool(non_claims.get("action_authorized")),
        "consequence_created": bool(non_claims.get("consequence_created")),
        "multi_carrier_law_created": bool(non_claims.get("multi_carrier_law_created")),
        "distributed_standing_created": bool(
            non_claims.get("distributed_standing_created")
        ),
        "continuation_authorized": bool(non_claims.get("continuation_authorized")),
        "refusal_hidden": bool(non_claims.get("refusal_hidden")),
        "divergence_hidden": bool(non_claims.get("divergence_hidden")),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_declared_admission_request(
    admission_request_id: str,
    admission_purpose: str,
    selected_emission_id: str,
    selected_emission_outcome: str,
    emitting_carrier_id: str,
    carrier_role: str,
    emission_class: str,
    admission_intent: str = "ADMIT_AS_EVIDENCE",
    *,
    return_path: str | None = None,
    selected_basis: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a minimum valid declared admission request."""

    normalized_role = _normalize_token(carrier_role) or carrier_role
    normalized_emission = _normalize_token(emission_class) or emission_class
    request: dict[str, Any] = {
        "admission_request_id": admission_request_id,
        "declared_admission_question": (
            "May this carrier-local emission be admitted as body-line evidence?"
        ),
        "admission_purpose": admission_purpose,
        "selected_carrier_emission": {
            "emission_id": selected_emission_id,
            "emission_outcome": selected_emission_outcome,
            "emitting_carrier_id": emitting_carrier_id,
            "carrier_role": normalized_role,
            "emission_class": normalized_emission,
            "emission_state": RETURNED_TO_BODY_LINE if return_path else EMITTED_LOCAL,
        },
        "carrier_role_basis": {
            "carrier_role": normalized_role,
            "carrier_role_bounded": normalized_role in ADMITTED_CARRIER_ROLES,
        },
        "emission_basis": {
            "emission_class": normalized_emission,
            "emission_class_admissible": normalized_emission
            in ADMISSIBLE_EMISSION_CLASSES,
        },
        "admission_intent": admission_intent,
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }
    if return_path is not None:
        request["return_path"] = return_path
        request["return_basis"] = {
            "return_path": return_path,
            "return_state": RETURNED_TO_BODY_LINE,
            "return_does_not_self_admit": True,
        }
    if selected_basis is not None:
        request["source_or_carried_basis"] = copy.deepcopy(dict(selected_basis))
    return request


def _resolve_request(
    request: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    request_mapping = _as_mapping(request)
    raw_selected = request_mapping.get("selected_carrier_emission")
    selected = _normalize_selected_emission(raw_selected, request_mapping)
    role = selected.get("carrier_role")
    emission_class = selected.get("emission_class")
    intent = _admission_intent_basis(request_mapping, selected)
    declared_non_claims = _as_mapping(request_mapping.get("declared_non_claims"))

    return_basis = _return_basis(request_mapping)
    checks = _build_admission_checks(
        request_mapping,
        raw_selected,
        selected,
        role,
        emission_class,
        intent,
        declared_non_claims,
        precheck_failures,
    )
    failed_check = _first_failed(checks)
    if failed_check:
        outcome = CARRIER_LOCAL_EMISSION_ADMISSION_BLOCKED
        block_code = str(failed_check.get("block_code"))
    elif intent["positive_admission_requested"]:
        outcome = CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE
        block_code = None
    else:
        outcome = CARRIER_LOCAL_EMISSION_NOT_ADMITTED
        block_code = None
    block_reason = _block_reason(block_code, failed_check)

    result: dict[str, Any] = {
        "carrier_local_emission_admission_metadata": {
            "carrier_local_emission_admission_result_id": _result_id(
                request_mapping,
                selected,
                outcome,
            ),
            "carrier_local_emission_admission_result_type": (
                "carrier_local_emission_admission_boundary_result"
            ),
            "carrier_local_emission_admission_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_admission_question": _declared_admission_question(
            request_mapping,
            selected,
            intent,
        ),
        "selected_carrier_emission": selected,
        "carrier_role_basis": _carrier_role_basis(request_mapping, selected, role),
        "emission_basis": _emission_basis(request_mapping, emission_class),
        "return_basis": return_basis,
        "admission_basis": _admission_basis(request_mapping, selected, intent, return_basis),
        "admission_checks": checks,
        "admission_statement": _admission_statement(
            outcome,
            selected,
            return_basis,
            request_mapping,
            block_code,
            block_reason,
            checks,
        ),
        "admission_non_meaning": copy.deepcopy(ADMISSION_NON_MEANING),
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
    result["carrier_local_emission_admission_summary"] = (
        build_carrier_local_emission_admission_summary(result)
    )
    return result


def _build_admission_checks(
    request: Mapping[str, Any],
    raw_selected: Any,
    selected: Mapping[str, Any],
    role: str | None,
    emission_class: str | None,
    intent: Mapping[str, Any],
    declared_non_claims: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    sources = [
        request,
        raw_selected,
        selected,
        _as_mapping(request.get("carrier_role_basis")),
        _as_mapping(request.get("emission_basis")),
        _as_mapping(request.get("return_basis")),
        _as_mapping(request.get("admission_basis")),
        declared_non_claims,
    ]
    precheck_code = (
        precheck_failures[0]
        if precheck_failures
        else "DECLARED_ADMISSION_REQUEST_MALFORMED"
    )
    checks = [
        _check(
            "declared_admission_request_is_parseable_mapping",
            not precheck_failures,
            "declared admission request is a mapping",
            list(precheck_failures),
            precheck_code,
        ),
        _check(
            "carrier_local_emission_exists",
            raw_selected is not None,
            "selected carrier-local emission is supplied",
            raw_selected,
            "CARRIER_LOCAL_EMISSION_MISSING",
        ),
        _check(
            "carrier_local_emission_is_mapping",
            raw_selected is None or isinstance(raw_selected, Mapping),
            "selected carrier-local emission is a mapping",
            type(raw_selected).__name__,
            "CARRIER_LOCAL_EMISSION_MALFORMED",
        ),
        _check(
            "emission_identity_exists",
            bool(selected.get("emission_id")),
            "emission identity is declared",
            selected.get("emission_id"),
            "EMISSION_IDENTITY_MISSING",
        ),
        _check(
            "emission_outcome_exists",
            bool(selected.get("emission_outcome")),
            "emission outcome or status is declared",
            selected.get("emission_outcome"),
            "EMISSION_OUTCOME_MISSING",
        ),
        _check(
            "emitting_carrier_exists",
            bool(selected.get("emitting_carrier_id")),
            "emitting carrier identity is declared",
            selected.get("emitting_carrier_id"),
            "EMITTING_CARRIER_MISSING",
        ),
        _check(
            "carrier_role_exists",
            bool(role),
            "carrier role is declared",
            role,
            "CARRIER_ROLE_MISSING",
        ),
        _check(
            "carrier_role_is_bounded",
            role in ADMITTED_CARRIER_ROLES,
            "carrier role is bounded and admitted for this version",
            role,
            "CARRIER_ROLE_UNSUPPORTED",
        ),
        _check(
            "emission_class_exists",
            bool(emission_class),
            "emission class is declared",
            emission_class,
            "EMISSION_CLASS_MISSING",
        ),
        _check(
            "emission_class_admissible",
            emission_class in ADMISSIBLE_EMISSION_CLASSES
            and emission_class not in NOT_ADMITTED_EMISSION_CLASSES,
            "emission class is admissible as evidence only",
            {
                "emission_class": emission_class,
                "not_admitted_by_default": emission_class
                in NOT_ADMITTED_EMISSION_CLASSES,
            },
            "EMISSION_CLASS_UNSUPPORTED",
        ),
        _check(
            "admission_purpose_declared",
            bool(str(request.get("admission_purpose") or "").strip()),
            "admission purpose is declared",
            request.get("admission_purpose"),
            "ADMISSION_PURPOSE_UNDECLARED",
        ),
        _check(
            "admission_intent_declared",
            bool(intent.get("intent_declared")),
            "admission intent is declared",
            intent,
            "ADMISSION_INTENT_UNDECLARED",
        ),
    ]
    for check_name, aliases, expected, block_code in MISTAKEN_ADMISSION_CHECKS:
        checks.append(
            _check(
                check_name,
                not _flag_true(sources, aliases),
                expected,
                _flag_snapshot(sources, aliases),
                block_code,
            )
        )
    for check_name, aliases, expected, block_code in ANTI_COLLAPSE_CHECKS:
        checks.append(
            _check(
                check_name,
                not _flag_true(sources, aliases),
                expected,
                _flag_snapshot(sources, aliases),
                block_code,
            )
        )
    missing_or_flipped = _missing_or_flipped_non_claims(declared_non_claims)
    checks.append(
        _check(
            "non_claims_remain_false",
            not missing_or_flipped,
            "all required admission non-claims are present and false",
            missing_or_flipped,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _admission_statement(
    outcome: str,
    selected: Mapping[str, Any],
    return_basis: Mapping[str, Any],
    request: Mapping[str, Any],
    block_code: str | None,
    block_reason: str | None,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    admitted = outcome == CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE
    not_admitted = outcome == CARRIER_LOCAL_EMISSION_NOT_ADMITTED
    blocked = outcome == CARRIER_LOCAL_EMISSION_ADMISSION_BLOCKED
    return_available = bool(return_basis.get("return_basis_available"))
    emission_state = _normalize_token(selected.get("emission_state"))
    emitted_local = (not return_available) or emission_state == EMITTED_LOCAL
    returned_to_body_line = return_available or emission_state == RETURNED_TO_BODY_LINE
    integrity_available = bool(_as_mapping(request.get("integrity_evidence")))
    failed_checks = [
        copy.deepcopy(dict(check)) for check in checks if check.get("passed") is False
    ]
    return {
        "carrier_local_emission_admitted_as_evidence": admitted,
        "emission_return_admission_distinction": {
            "emitted_local": bool(emitted_local),
            "returned_to_body_line": bool(returned_to_body_line),
            "admitted_as_evidence": admitted,
            "not_admitted": not_admitted,
            "admission_blocked": blocked,
        },
        "admitted_evidence_remains_downstream": admitted,
        "emitting_carrier_identity_preserved": admitted,
        "carrier_role_preserved": admitted,
        "emission_class_preserved": admitted,
        "emission_identity_preserved": admitted,
        "emission_outcome_preserved": admitted,
        "return_basis_preserved": return_available,
        "integrity_evidence_preserved": integrity_available,
        "source_not_replaced": True,
        "currentness_not_created": True,
        "authority_not_created": True,
        "permission_not_created": True,
        "successor_not_created": True,
        "body_not_created": True,
        "multi_carrier_law_not_created": True,
        "distributed_standing_not_created": True,
        "presence_threshold_truth_action_consequence_not_created": True,
        "continuation_not_authorized": True,
        "refusal_not_hidden": True,
        "divergence_not_hidden": True,
        "carrier_local_emission_preserved_without_admission": not_admitted,
        "not_admitted_reason": _not_admitted_reason(request, selected)
        if not_admitted
        else None,
        "admission_blocked": blocked,
        "block_code": block_code,
        "block_reason": block_reason,
        "failed_checks": failed_checks if blocked else [],
        "selected_basis_preserved_where_available": blocked,
    }


def _declared_admission_question(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
    intent: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "admission_request_id": request.get("admission_request_id"),
        "declared_admission_question": request.get("declared_admission_question"),
        "admission_purpose": request.get("admission_purpose"),
        "admission_intent": intent.get("admission_intent"),
        "normalized_admission_intent": intent.get("normalized_admission_intent"),
        "declared_scope": request.get("declared_scope"),
        "selected_emission_reference": selected.get("emission_id"),
        "selected_carrier_reference": selected.get("emitting_carrier_id"),
        "declared_non_claims": copy.deepcopy(request.get("declared_non_claims")),
        "declared_admission_request_path": request.get(
            "_declared_admission_request_path"
        ),
    }


def _normalize_selected_emission(raw_selected: Any, request: Mapping[str, Any]) -> dict[str, Any]:
    selected = _as_mapping(raw_selected)
    emitting_carrier = _as_mapping(
        selected.get("emitting_carrier") or request.get("emitting_carrier")
    )
    emission_id = _first_text(
        selected,
        ("emission_id", "id", "emission_identity", "selected_emission_id"),
    ) or _first_text(request, ("emission_id", "emission_identity", "selected_emission_id"))
    emission_outcome = _first_text(
        selected,
        ("emission_outcome", "outcome", "status", "emission_status"),
    ) or _first_text(request, ("emission_outcome", "outcome", "status", "emission_status"))
    emitting_carrier_id = (
        _first_text(
            selected,
            (
                "emitting_carrier_id",
                "carrier_id",
                "selected_carrier_id",
                "carrier_identifier",
            ),
        )
        or _first_text(emitting_carrier, ("carrier_id", "id", "carrier_identifier"))
        or _first_text(request, ("emitting_carrier_id", "carrier_id"))
    )
    return {
        "emission_id": emission_id,
        "emission_outcome": emission_outcome,
        "emitting_carrier_id": emitting_carrier_id,
        "carrier_role": _resolve_carrier_role(request, selected),
        "emission_class": _resolve_emission_class(request, selected),
        "emission_state": _normalize_token(
            _first_text(selected, ("emission_state", "state", "emission_admission_state"))
            or _first_text(request, ("emission_state", "carrier_local_emission_state"))
        ),
        "source_or_carried_basis": copy.deepcopy(request.get("source_or_carried_basis")),
        "selected_packet_or_surface": copy.deepcopy(request.get("selected_packet_or_surface")),
        "selected_receipt_or_refusal": copy.deepcopy(request.get("selected_receipt_or_refusal")),
        "raw_selected_carrier_emission": copy.deepcopy(raw_selected),
    }


def _carrier_role_basis(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
    role: str | None,
) -> dict[str, Any]:
    return {
        "carrier_role": role,
        "carrier_role_declared": bool(role),
        "carrier_role_bounded": role in ADMITTED_CARRIER_ROLES,
        "admitted_carrier_roles": sorted(ADMITTED_CARRIER_ROLES),
        "raw_carrier_role_basis": _as_mapping(request.get("carrier_role_basis")),
        "selected_emission_carrier_role": selected.get("carrier_role"),
        "role_does_not_create_source_currentness_authority_permission_successor_body": True,
    }


def _emission_basis(request: Mapping[str, Any], emission_class: str | None) -> dict[str, Any]:
    return {
        "emission_class": emission_class,
        "emission_class_declared": bool(emission_class),
        "emission_class_admissible": emission_class in ADMISSIBLE_EMISSION_CLASSES,
        "emission_class_not_admitted_by_default": emission_class
        in NOT_ADMITTED_EMISSION_CLASSES,
        "admissible_emission_classes": sorted(ADMISSIBLE_EMISSION_CLASSES),
        "not_admitted_emission_classes": sorted(NOT_ADMITTED_EMISSION_CLASSES),
        "source_or_carried_basis": copy.deepcopy(request.get("source_or_carried_basis")),
        "selected_packet_or_surface": copy.deepcopy(request.get("selected_packet_or_surface")),
        "selected_receipt_or_refusal": copy.deepcopy(request.get("selected_receipt_or_refusal")),
        "integrity_evidence": copy.deepcopy(request.get("integrity_evidence")),
        "raw_emission_basis": _as_mapping(request.get("emission_basis")),
        "body_line_admission_status": "requires_declared_admission_boundary",
        "emission_may_be_admitted_only_as_evidence": emission_class
        in ADMISSIBLE_EMISSION_CLASSES,
    }


def _return_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    raw_basis = _as_mapping(request.get("return_basis"))
    return_path = _first_text(raw_basis, ("return_path", "path")) or _first_text(
        request,
        ("return_path",),
    )
    return_context = copy.deepcopy(
        raw_basis.get("return_context")
        if "return_context" in raw_basis
        else request.get("return_context")
    )
    return_available = bool(return_path or return_context or raw_basis)
    return {
        "return_basis_available": return_available,
        "return_path": return_path,
        "return_context": return_context,
        "raw_return_basis": raw_basis,
        "return_does_not_self_admit": True,
        "returned_to_body_line_is_not_admitted_by_default": True,
    }


def _admission_basis(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
    intent: Mapping[str, Any],
    return_basis: Mapping[str, Any],
) -> dict[str, Any]:
    emission_state = _normalize_token(selected.get("emission_state"))
    returned = bool(return_basis.get("return_basis_available")) or (
        emission_state == RETURNED_TO_BODY_LINE
    )
    emitted_local = (not returned) or emission_state == EMITTED_LOCAL
    positive_requested = bool(intent.get("positive_admission_requested"))
    return {
        "admission_purpose": request.get("admission_purpose"),
        "admission_intent": intent.get("admission_intent"),
        "normalized_admission_intent": intent.get("normalized_admission_intent"),
        "positive_admission_requested": positive_requested,
        "explicit_non_admission_requested": bool(
            intent.get("explicit_non_admission_requested")
        ),
        "emitted_local_state_preserved": bool(emitted_local),
        "returned_to_body_line_state_preserved": bool(returned),
        "admitted_as_evidence_state_requested": positive_requested,
        "not_admitted_state_available": True,
        "admission_blocked_state_available": True,
        "admission_is_not_currentness": True,
        "admission_non_claims": copy.deepcopy(request.get("declared_non_claims")),
    }


def _admission_intent_basis(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
) -> dict[str, Any]:
    raw_intent = _first_text(
        request,
        ("admission_intent", "intent", "admission_request_intent"),
    )
    admission_requested = request.get("admission_requested")
    if raw_intent is None and admission_requested is True:
        raw_intent = "ADMIT_AS_EVIDENCE"
    elif raw_intent is None and admission_requested is False:
        raw_intent = "NOT_ADMITTED"
    normalized = _normalize_token(raw_intent)
    emission_state = _normalize_token(selected.get("emission_state"))
    if normalized is None and emission_state in {EMITTED_LOCAL, RETURNED_TO_BODY_LINE}:
        normalized = emission_state
        raw_intent = str(emission_state)
    return {
        "admission_intent": raw_intent,
        "normalized_admission_intent": normalized,
        "intent_declared": normalized is not None,
        "positive_admission_requested": normalized in POSITIVE_ADMISSION_INTENTS,
        "explicit_non_admission_requested": (
            normalized in NON_ADMISSION_INTENTS
            or normalized in {EMITTED_LOCAL, RETURNED_TO_BODY_LINE, NOT_ADMITTED}
        ),
    }


def _resolve_carrier_role(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
) -> str | None:
    role_basis = _as_mapping(request.get("carrier_role_basis"))
    return _normalize_token(
        _first_text(selected, ("carrier_role", "role", "declared_carrier_role"))
        or _first_text(role_basis, ("carrier_role", "role_name", "role"))
        or _first_text(request, ("carrier_role", "declared_carrier_role"))
    )


def _resolve_emission_class(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
) -> str | None:
    emission_basis = _as_mapping(request.get("emission_basis"))
    return _normalize_token(
        _first_text(selected, ("emission_class", "class", "declared_emission_class"))
        or _first_text(emission_basis, ("emission_class", "class"))
        or _first_text(request, ("emission_class", "declared_emission_class"))
    )


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
        raise CarrierLocalEmissionAdmissionBoundaryError(
            "DECLARED_ADMISSION_REQUEST_UNREADABLE",
            f"{BLOCK_REASONS['DECLARED_ADMISSION_REQUEST_UNREADABLE']} path={selected_path} detail={exc}",
        ) from exc
    try:
        loaded = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CarrierLocalEmissionAdmissionBoundaryError(
            "DECLARED_ADMISSION_REQUEST_MALFORMED",
            f"{BLOCK_REASONS['DECLARED_ADMISSION_REQUEST_MALFORMED']} path={selected_path} detail={exc}",
        ) from exc
    if not isinstance(loaded, Mapping):
        raise CarrierLocalEmissionAdmissionBoundaryError(
            "DECLARED_ADMISSION_REQUEST_MALFORMED",
            f"{BLOCK_REASONS['DECLARED_ADMISSION_REQUEST_MALFORMED']} path={selected_path} expected object",
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
    reason = BLOCK_REASONS.get(block_code, "Carrier-local emission admission blocked.")
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


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "source_replaced",
        "carrier_emission_self_admitted",
        "returned_emission_self_admitted",
        "emission_admission_created_source",
        "emission_admission_created_currentness",
        "emission_admission_created_authority",
        "emission_admission_created_permission",
        "emission_admission_created_successor",
        "emission_admission_created_body",
        "emission_admission_created_signal_by_default",
        "presence_established",
        "threshold_met",
        "truth_created",
        "action_authorized",
        "consequence_created",
        "multi_carrier_law_created",
        "distributed_standing_created",
        "continuation_authorized",
        "refusal_hidden",
        "divergence_hidden",
    )
    return {key: non_claims.get(key) for key in keys}


def _not_admitted_reason(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
) -> str:
    intent = _admission_intent_basis(request, selected)
    normalized = intent.get("normalized_admission_intent")
    if normalized in {EMITTED_LOCAL, "EMITTED_LOCAL_ONLY"}:
        return "emission_preserved_as_emitted_local_without_admission"
    if normalized in {RETURNED_TO_BODY_LINE, "RETURNED_ONLY", "RETURNED_TO_BODY_LINE_ONLY"}:
        return "returned_emission_preserved_without_admission"
    if intent.get("explicit_non_admission_requested"):
        return "request_explicitly_declared_non_admission"
    return "no_positive_admission_claim_declared"


def _result_id(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
    outcome: str,
) -> str:
    base = (
        request.get("admission_request_id")
        or selected.get("emission_id")
        or "carrier_local_emission_admission"
    )
    return (
        f"{_safe_filename_part(base)}__{outcome.lower()}"
        "__carrier_local_emission_admission_result"
    )


def _safe_filename_part(value: Any) -> str:
    text = str(value or "carrier_local_emission_admission")
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
    return stem[:180] or "carrier_local_emission_admission"


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
