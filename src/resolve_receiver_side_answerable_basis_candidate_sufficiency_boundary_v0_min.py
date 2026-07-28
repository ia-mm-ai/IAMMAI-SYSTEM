"""Resolve one bounded candidate-sufficiency consideration boundary.

This module consumes only the selected completed V3 evaluation result.  It may
record consideration admission; it never decides candidate sufficiency.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min"

BOUNDARY_ID = "receiver_side_answerable_basis_candidate_sufficiency_boundary_001"
BOUNDARY_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = (
    "CONSIDER_SUFFICIENCY_OF_ONE_COMPLETEDLY_EVALUATED_"
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)

SELECTED_EVALUATION_OPERATION_ID = "receiver_side_answerable_basis_candidate_evaluation_operation_001"
SELECTED_EVALUATION_OPERATION_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION"
SELECTED_EVALUATION_OPERATION_VERSION = "0.1.0"
SELECTED_EVALUATION_OPERATION_SCOPE = (
    "EVALUATE_ONE_RECORDED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_"
    "ACROSS_EIGHT_SEPARATE_DIMENSIONS_ONLY"
)
SELECTED_EVALUATION_RESULT_REQUIRED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATED"
SELECTED_V3_RESULT_VERSION = "0.2.0"
SELECTED_V3_RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3"

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
SELECTED_RECEPTION_OPERATION_ID = "receiver_side_answerable_basis_reception_operation_001"
SELECTED_EVALUATION_BOUNDARY_ID = "receiver_side_answerable_basis_candidate_evaluation_boundary_001"

ADMISSIBLE_FUTURE_ROUTE = "CANDIDATE_SUFFICIENCY_BOUNDARY_THEN_CANDIDATE_SUFFICIENCY_OPERATION_ONLY"

REQUIRED_DIMENSION_IDS = (
    "candidate_structural_correspondence",
    "declared_provenance_posture",
    "receiver_authorship_posture",
    "separate_custody_posture",
    "refusability_posture",
    "could_have_been_withheld_posture",
    "prior_knock_correspondence_posture",
    "capture_record_posture",
)
DIMENSION_RESULT_SATISFIED = "SATISFIED"
DIMENSION_RESULT_NOT_SATISFIED = "NOT_SATISFIED"
DIMENSION_RESULT_INDETERMINATE = "INDETERMINATE"
DIMENSION_RESULT_NOT_EVALUATED = "NOT_EVALUATED"

OUTCOME_ALLOWED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY_ALLOWED"
OUTCOME_BLOCKED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY_BLOCKED"
OUTCOME_NOT_RECORDED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY_NOT_RECORDED"
OUTCOME_FAMILY = (OUTCOME_ALLOWED, OUTCOME_BLOCKED, OUTCOME_NOT_RECORDED)
OUTCOME_RECORDED = OUTCOME_ALLOWED

BOUNDARY_RESULT_ALLOWED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_CONSIDERATION_ALLOWED"
BOUNDARY_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
BOUNDARY_RESULT_FAMILY = (BOUNDARY_RESULT_ALLOWED, BOUNDARY_RESULT_NOT_EVALUATED)

INTENT_RECORD = "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY"
INTENT_BLOCK = "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SUFFICIENCY_BOUNDARY_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY_V0_MIN_SPEC.md"
)
SELECTED_V3_EVALUATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3/"
    "receiver_side_answerable_basis_candidate_evaluation_operation_001__"
    "receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result.json"
)
GOVERNING_SUFFICIENCY_BOUNDARY_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_SUFFICIENCY_BOUNDARY_SPECIFICATION_RELATIVE_PATH
)
SELECTED_V3_EVALUATION_ARTIFACT_PATH = REPO_ROOT / SELECTED_V3_EVALUATION_ARTIFACT_RELATIVE_PATH
GOVERNING_SPEC_RELATIVE_PATH = GOVERNING_SUFFICIENCY_BOUNDARY_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPEC_PATH = GOVERNING_SUFFICIENCY_BOUNDARY_SPECIFICATION_PATH
OUTPUT_ROOT = REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min"
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_candidate_sufficiency_boundary_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result.json"
)

SPEC_MARKERS = (
    "# Receiver-Side Answerable Basis Candidate Sufficiency Boundary V0 Minimum Specification",
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_CONSIDERATION_ALLOWED",
    "CANDIDATE_SUFFICIENCY_BOUNDARY_THEN_CANDIDATE_SUFFICIENCY_OPERATION_ONLY",
)

REQUIRED_UPSTREAM_POSTURES = {
    "evaluation_operation_recorded": True,
    "evaluation_operation_result_recorded": True,
    "evaluation_basis_supplied": True,
    "evaluation_basis_complete": True,
    "all_dimension_basis_records_present": True,
    "all_dimension_basis_records_bounded": True,
    "all_dimension_basis_records_reference_selected_candidate": True,
    "all_dimension_basis_records_reference_selected_boundary": True,
    "all_dimension_basis_records_non_result_preclaiming": True,
    "all_dimension_basis_records_admissible": True,
    "candidate_evaluated": True,
    "all_dimensions_satisfied": True,
    "any_dimension_not_satisfied": False,
    "any_dimension_indeterminate": False,
    "evaluation_operation_exhausted": True,
}
REQUIRED_DIMENSION_RESULTS = {dimension_id: DIMENSION_RESULT_SATISFIED for dimension_id in REQUIRED_DIMENSION_IDS}

REQUIRED_FALSE_NON_CLAIMS = (
    "receiver_side_answerable_basis_candidate_sufficient",
    "receiver_side_answerable_basis_candidate_insufficient",
    "receiver_side_answerable_basis_candidate_indeterminate",
    "candidate_sufficiency_decided",
    "candidate_sufficiency_established",
    "candidate_insufficiency_established",
    "candidate_indeterminacy_established",
    "candidate_sufficiency_operation_created",
    "candidate_sufficiency_operation_authorized",
    "candidate_sufficiency_operation_executed",
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_answerable_receipt_present",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "receiver_attestation_boundary_created",
    "receiver_answerable_receipt_boundary_created",
    "presence_re_evaluation_boundary_created",
    "identity_created",
    "relation_created",
    "coupling_assigned",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "public_intake_created",
    "authority_created",
    "standing_created",
    "truth_created",
    "continuity_memory_written",
    "output_authorized",
    "action_authorized",
    "synchronization_authorized",
    "repeated_candidate_sufficiency_boundary_permission_created",
    "reusable_candidate_sufficiency_route_created",
    "same_candidate_sufficiency_boundary_rerun_authorized",
    "automatic_candidate_sufficiency_boundary_retry_created",
    "candidate_sufficiency_boundary_debt_created",
    "candidate_sufficiency_boundary_obligation_created",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_candidate_sufficiency_decision": "PROHIBITED_CANDIDATE_SUFFICIENCY_DECISION_REQUESTED",
    "request_candidate_sufficient": "PROHIBITED_CANDIDATE_SUFFICIENCY_DECISION_REQUESTED",
    "request_candidate_insufficient": "PROHIBITED_CANDIDATE_SUFFICIENCY_DECISION_REQUESTED",
    "request_candidate_indeterminate": "PROHIBITED_CANDIDATE_SUFFICIENCY_DECISION_REQUESTED",
    "request_candidate_sufficiency_operation_creation": "PROHIBITED_CANDIDATE_SUFFICIENCY_OPERATION_REQUESTED",
    "request_candidate_sufficiency_operation_authorization": "PROHIBITED_CANDIDATE_SUFFICIENCY_OPERATION_REQUESTED",
    "request_candidate_sufficiency_operation_execution": "PROHIBITED_CANDIDATE_SUFFICIENCY_OPERATION_REQUESTED",
    "request_receiver_attestation_creation": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_receiver_attestation_support": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_receiver_answerable_receipt_creation": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_presence_support": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_presence_authorization": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_presence_establishment": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_presence_recording": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_receiver_attestation_boundary_creation": "PROHIBITED_DOWNSTREAM_BOUNDARY_REQUESTED",
    "request_receiver_answerable_receipt_boundary_creation": "PROHIBITED_DOWNSTREAM_BOUNDARY_REQUESTED",
    "request_presence_re_evaluation_boundary_creation": "PROHIBITED_DOWNSTREAM_BOUNDARY_REQUESTED",
    "request_identity_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_relation_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_coupling_assignment": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_coupling_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_api_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_public_interface_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_public_intake_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_authority_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_standing_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_truth_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_continuity_memory_write": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_output_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_action_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_repeated_boundary_permission_creation": "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED",
    "request_reusable_candidate_sufficiency_route_creation": "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED",
    "request_same_candidate_boundary_rerun": "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED",
    "request_automatic_boundary_retry_creation": "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED",
    "request_boundary_debt_creation": "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED",
    "request_boundary_obligation_creation": "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED",
    "request_follow_on_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_follow_on_work_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
}

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "UNSUPPORTED_INTENT",
        "SUFFICIENCY_BOUNDARY_SPEC_REFERENCE_MISSING",
        "SUFFICIENCY_BOUNDARY_SPEC_MARKER_MISSING",
        "SELECTED_V3_EVALUATION_ARTIFACT_REFERENCE_MISSING",
        "SELECTED_V3_EVALUATION_ARTIFACT_NOT_PARSEABLE",
        "SELECTED_V3_EVALUATION_ARTIFACT_NOT_MAPPING",
        "REQUEST_VALUE_MISMATCH",
        "SELECTED_EVALUATION_IDENTITY_MISMATCH",
        "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
        "UPSTREAM_EVALUATION_NOT_RECORDED",
        "UPSTREAM_EVALUATION_RESULT_NOT_RECORDED",
        "UPSTREAM_EVALUATION_OUTCOME_MISMATCH",
        "UPSTREAM_EVALUATION_RESULT_MISMATCH",
        "UPSTREAM_EVALUATION_FAILED_CHECKS_PRESENT",
        "UPSTREAM_EVALUATION_BASIS_INCOMPLETE",
        "UPSTREAM_EVALUATION_ATOMIC_GATE_INCOMPLETE",
        "UPSTREAM_CANDIDATE_NOT_EVALUATED",
        "UPSTREAM_ALL_DIMENSIONS_NOT_SATISFIED",
        "UPSTREAM_DIMENSION_NOT_SATISFIED",
        "UPSTREAM_DIMENSION_INDETERMINATE",
        "UPSTREAM_DIMENSION_NOT_EVALUATED",
        "UPSTREAM_DIMENSION_NOT_ESTABLISHED",
        "UPSTREAM_DIMENSION_BASIS_NOT_REFERENCED",
        "UPSTREAM_DIMENSION_BASIS_INCONSISTENT",
        "UPSTREAM_DIMENSION_ID_MISMATCH",
        "UPSTREAM_OPERATION_NOT_EXHAUSTED",
        "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
        "UPSTREAM_SUFFICIENCY_BOUNDARY_ALREADY_CREATED",
        "UPSTREAM_DOWNSTREAM_POSTURE_ALREADY_PRESENT",
        "UPSTREAM_RERUN_OR_REUSABLE_ROUTE_PRESENT",
        "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
        "PROHIBITED_CANDIDATE_SUFFICIENCY_DECISION_REQUESTED",
        "PROHIBITED_CANDIDATE_SUFFICIENCY_OPERATION_REQUESTED",
        "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
        "PROHIBITED_DOWNSTREAM_BOUNDARY_REQUESTED",
        "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
        "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
        "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
        "PROHIBITED_REPEATED_REUSABLE_RERUN_RETRY_DEBT_OR_OBLIGATION_REQUESTED",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "EXPLICIT_BLOCK_REQUESTED",
        "WRITE_REFUSED",
    }
)

ALLOWED_WHAT_REMAINS_OPEN = (
    "candidate-sufficiency operation specification, if separately selected",
    "candidate-sufficiency operation resolver and test, if separately selected",
    "candidate-sufficiency decision",
    "receiver-attestation boundary, only after lawful candidate-sufficiency standing",
    "receiver-answerable-receipt boundary, only after later lawful basis",
    "presence re-evaluation, only after later lawful basis",
    "identity",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "authority",
    "standing",
    "output",
    "action",
    "synchronization",
    "follow-on work",
)
WHAT_REMAINS_OPEN = ALLOWED_WHAT_REMAINS_OPEN
_EXPECTED_V3_OPEN = (
    "candidate-sufficiency boundary, if separately selected",
    "receiver-attestation boundary, only after later lawful basis",
    "receiver-answerable-receipt boundary, only after later lawful basis",
    "presence re-evaluation, only after later lawful basis",
    "identity",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "authority",
    "standing",
    "output",
    "action",
    "synchronization",
    "follow-on work",
)
_STALE_V3_OPEN_ITEMS = (
    "separately supplied eight-dimension evaluation basis",
    "actual candidate evaluation",
    "dimension-specific derived results",
    "evaluation-basis completion",
    "operation admission",
    "operation exhaustion",
    "later dimension completion",
    "automatic re-evaluation",
    "same-candidate retry",
)


class ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError(Exception):
    """Raised when a bounded boundary result cannot be written."""


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _check(name: str, passed: bool, code: str | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"name": name, "passed": passed}
    if not passed and code is not None:
        result["failure_code"] = code
        result["block_code"] = code
    return result


def _add_failure(checks: list[dict[str, Any]], name: str, code: str) -> None:
    checks.append(_check(name, False, code))


def _as_repo_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_text(value: Path | str) -> tuple[str | None, str | None]:
    try:
        path = _as_repo_path(value)
        if not path.is_file():
            return None, "not_a_file"
        return path.read_text(encoding="utf-8"), None
    except OSError:
        return None, "unreadable"


def _read_json(value: Path | str) -> tuple[Any | None, str | None]:
    text, error = _read_text(value)
    if error is not None or text is None:
        return None, error
    try:
        return json.loads(text), None
    except (TypeError, ValueError, json.JSONDecodeError):
        return None, "not_parseable"


def _declared_non_claims_valid(value: Any) -> bool:
    return isinstance(value, Mapping) and set(value) == set(REQUIRED_FALSE_NON_CLAIMS) and all(
        value.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS
    )


def _expected_request_values() -> dict[str, Any]:
    return {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "selected_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "selected_candidate_evaluation_operation_type": SELECTED_EVALUATION_OPERATION_TYPE,
        "selected_candidate_evaluation_operation_version": SELECTED_EVALUATION_OPERATION_VERSION,
        "selected_candidate_evaluation_result_required": SELECTED_EVALUATION_RESULT_REQUIRED,
        "governing_sufficiency_boundary_specification_path": str(
            GOVERNING_SUFFICIENCY_BOUNDARY_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_v3_evaluation_artifact_path": str(SELECTED_V3_EVALUATION_ARTIFACT_RELATIVE_PATH),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "required_upstream_postures": copy.deepcopy(REQUIRED_UPSTREAM_POSTURES),
        "required_dimension_results": copy.deepcopy(REQUIRED_DIMENSION_RESULTS),
    }


def build_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build the only canonical request shape for one selected boundary."""
    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **_expected_request_values(),
        "declared_non_claims": _canonical_non_claims(),
    }
    request.update({field: False for field in PROHIBITED_REQUEST_FLAGS})
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build the declared request using the same canonical bounded shape."""
    return build_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_request(
        **overrides
    )


def _preclaim_fields() -> set[str]:
    return {
        "candidate_sufficiency_boundary_recorded",
        "candidate_sufficiency_boundary_result_recorded",
        "candidate_sufficiency_boundary_result",
        "candidate_sufficiency_consideration_allowed",
        "candidate_sufficiency_boundary_exhausted",
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_recorded",
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_result_recorded",
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_result",
        "candidate_sufficiency_boundary_created",
        "selected_v3_evaluation_result",
        "selected_v3_artifact",
        "complete_v3_artifact",
        "receiver_side_answerable_basis_candidate_evaluation_operation",
        "receiver_side_answerable_basis_candidate_evaluation_operation_checks",
        *REQUIRED_FALSE_NON_CLAIMS,
    }


def _request_mismatch_code(field: str) -> str:
    if field in {
        "receiver_side_answerable_basis_candidate_id",
        "receiver_side_answerable_basis_candidate_type",
        "receiver_side_answerable_basis_candidate_scope",
        "selected_candidate_reception_operation_id",
        "selected_candidate_evaluation_boundary_id",
    }:
        return "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
    if field.startswith("selected_candidate_evaluation_"):
        return "SELECTED_EVALUATION_IDENTITY_MISMATCH"
    return "REQUEST_VALUE_MISMATCH"


def _validate_request(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> tuple[str | None, str | None]:
    intent = request.get("intent")
    if intent == INTENT_BLOCK:
        return "EXPLICIT_BLOCK_REQUESTED", "explicit block intent was requested"
    if intent not in SUPPORTED_INTENTS:
        return "UNSUPPORTED_INTENT", "intent is not supported"
    for field, expected in _expected_request_values().items():
        valid = request.get(field) == expected
        code = _request_mismatch_code(field)
        checks.append(_check(field, valid, code))
        if not valid:
            return code, field + " does not match the canonical boundary request"
    if not _declared_non_claims_valid(request.get("declared_non_claims")):
        return "NON_CLAIM_MISSING_OR_FLIPPED", "declared_non_claims must contain exact false postures"
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        valid = field in request and request.get(field) is False
        checks.append(_check(field, valid, code if field in request else "REQUEST_VALUE_MISMATCH"))
        if not valid:
            return (code if field in request else "REQUEST_VALUE_MISMATCH"), field + " is not a false bounded request flag"
    for field in _preclaim_fields():
        if field in request:
            return "RESULT_POSTURE_PRECLAIMED", field + " may not be caller-supplied"
    allowed = {"intent", "declared_non_claims", *tuple(_expected_request_values()), *tuple(PROHIBITED_REQUEST_FLAGS)}
    unknown = set(request).difference(allowed)
    if unknown:
        return "REQUEST_VALUE_MISMATCH", "declared request contains unknown fields"
    return None, None


def _empty_upstream_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "governing_paths": {
            "governing_sufficiency_boundary_specification_path": request.get(
                "governing_sufficiency_boundary_specification_path"
            ),
            "selected_v3_evaluation_artifact_path": request.get(
                "selected_v3_evaluation_artifact_path"
            ),
        },
        "marker_validation": {"governing_sufficiency_boundary_specification": False},
        "selected_v3_metadata": {},
        "selected_evaluation_identity": {},
        "selected_candidate_identity": {},
        "atomic_gate_validation": {},
        "dimension_validation": {},
        "candidate_aggregate_validation": {},
        "current_false_posture_validation": {},
        "corrected_open_state_validation": False,
    }


def _require(
    checks: list[dict[str, Any]], name: str, condition: bool, code: str, reason: str
) -> tuple[str | None, str | None]:
    checks.append(_check(name, condition, code))
    return (None, None) if condition else (code, reason)


def _validate_upstream(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    upstream = _empty_upstream_basis(request)
    spec_text, spec_error = _read_text(request["governing_sufficiency_boundary_specification_path"])
    if spec_error is not None or spec_text is None:
        return (
            "SUFFICIENCY_BOUNDARY_SPEC_REFERENCE_MISSING",
            "governing sufficiency-boundary specification is unavailable",
            upstream,
        )
    markers_valid = all(marker in spec_text for marker in SPEC_MARKERS)
    upstream["marker_validation"]["governing_sufficiency_boundary_specification"] = markers_valid
    code, reason = _require(
        checks,
        "governing_sufficiency_boundary_specification_markers",
        markers_valid,
        "SUFFICIENCY_BOUNDARY_SPEC_MARKER_MISSING",
        "governing sufficiency-boundary specification markers are incomplete",
    )
    if code is not None:
        return code, reason, upstream

    artifact, artifact_error = _read_json(request["selected_v3_evaluation_artifact_path"])
    if artifact_error in {"not_a_file", "unreadable"}:
        return (
            "SELECTED_V3_EVALUATION_ARTIFACT_REFERENCE_MISSING",
            "selected V3 evaluation artifact is unavailable",
            upstream,
        )
    if artifact_error == "not_parseable":
        return (
            "SELECTED_V3_EVALUATION_ARTIFACT_NOT_PARSEABLE",
            "selected V3 evaluation artifact is not parseable JSON",
            upstream,
        )
    if not isinstance(artifact, Mapping):
        return (
            "SELECTED_V3_EVALUATION_ARTIFACT_NOT_MAPPING",
            "selected V3 evaluation artifact is not a mapping",
            upstream,
        )

    operation = artifact.get("receiver_side_answerable_basis_candidate_evaluation_operation")
    declared = artifact.get("declared_receiver_side_answerable_basis_candidate_evaluation_operation_basis")
    dimensions = artifact.get("receiver_side_answerable_basis_candidate_evaluation_operation_dimensions")
    if not isinstance(operation, Mapping) or not isinstance(declared, Mapping) or not isinstance(dimensions, Mapping):
        return (
            "SELECTED_V3_EVALUATION_ARTIFACT_NOT_MAPPING",
            "selected V3 artifact lacks required bounded sections",
            upstream,
        )

    upstream["selected_v3_metadata"] = {
        "resolver_module": artifact.get("resolver_module"),
        "result_version": artifact.get("result_version"),
        "outcome": artifact.get("outcome"),
        "failed_check_count": artifact.get("failed_check_count"),
    }
    upstream["selected_evaluation_identity"] = {
        "operation_id": operation.get("receiver_side_answerable_basis_candidate_evaluation_operation_id"),
        "operation_type": operation.get("receiver_side_answerable_basis_candidate_evaluation_operation_type"),
        "operation_version": operation.get("receiver_side_answerable_basis_candidate_evaluation_operation_version"),
        "operation_scope": operation.get("receiver_side_answerable_basis_candidate_evaluation_operation_scope"),
        "operation_result": operation.get(
            "receiver_side_answerable_basis_candidate_evaluation_operation_result"
        ),
    }
    upstream["selected_candidate_identity"] = {
        "candidate_id": declared.get("receiver_side_answerable_basis_candidate_id"),
        "candidate_type": declared.get("receiver_side_answerable_basis_candidate_type"),
        "candidate_scope": declared.get("receiver_side_answerable_basis_candidate_scope"),
        "reception_operation_id": declared.get("selected_candidate_reception_operation_id"),
        "evaluation_boundary_id": declared.get("selected_candidate_evaluation_boundary_id"),
    }

    metadata_requirements = {
        "resolver_module": SELECTED_V3_RESOLVER_MODULE,
        "result_version": SELECTED_V3_RESULT_VERSION,
    }
    for field, expected in metadata_requirements.items():
        code, reason = _require(
            checks,
            "upstream." + field,
            artifact.get(field) == expected,
            "SELECTED_EVALUATION_IDENTITY_MISMATCH",
            "selected V3 " + field + " does not match",
        )
        if code is not None:
            return code, reason, upstream
    for field, expected, failure_code in (
        ("receiver_side_answerable_basis_candidate_evaluation_operation_recorded", True, "UPSTREAM_EVALUATION_NOT_RECORDED"),
        ("receiver_side_answerable_basis_candidate_evaluation_operation_result_recorded", True, "UPSTREAM_EVALUATION_RESULT_NOT_RECORDED"),
        ("outcome", "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_RECORDED", "UPSTREAM_EVALUATION_OUTCOME_MISMATCH"),
        ("receiver_side_answerable_basis_candidate_evaluation_operation_result", SELECTED_EVALUATION_RESULT_REQUIRED, "UPSTREAM_EVALUATION_RESULT_MISMATCH"),
    ):
        actual = artifact.get(field) if field == "outcome" else operation.get(field)
        code, reason = _require(
            checks, "upstream." + field, actual == expected, failure_code, "selected V3 upstream " + field + " does not match"
        )
        if code is not None:
            return code, reason, upstream
    code, reason = _require(
        checks,
        "upstream.failed_check_count",
        artifact.get("failed_check_count") == 0,
        "UPSTREAM_EVALUATION_FAILED_CHECKS_PRESENT",
        "selected V3 evaluation has failed checks",
    )
    if code is not None:
        return code, reason, upstream

    identity_requirements = {
        "operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "operation_type": SELECTED_EVALUATION_OPERATION_TYPE,
        "operation_version": SELECTED_EVALUATION_OPERATION_VERSION,
        "operation_scope": SELECTED_EVALUATION_OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "receiver_side_answerable_basis_candidate_evaluation_operation_type": SELECTED_EVALUATION_OPERATION_TYPE,
        "receiver_side_answerable_basis_candidate_evaluation_operation_version": SELECTED_EVALUATION_OPERATION_VERSION,
        "receiver_side_answerable_basis_candidate_evaluation_operation_scope": SELECTED_EVALUATION_OPERATION_SCOPE,
    }
    for field, expected in identity_requirements.items():
        code, reason = _require(
            checks,
            "upstream." + field,
            operation.get(field) == expected,
            "SELECTED_EVALUATION_IDENTITY_MISMATCH",
            "selected V3 evaluation identity does not match " + field,
        )
        if code is not None:
            return code, reason, upstream
    candidate_requirements = {
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
    }
    for field, expected in candidate_requirements.items():
        code, reason = _require(
            checks,
            "upstream." + field,
            declared.get(field) == expected,
            "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            "selected V3 candidate identity does not match " + field,
        )
        if code is not None:
            return code, reason, upstream

    atomic_gate_fields = (
        "evaluation_basis_supplied",
        "evaluation_basis_complete",
        "all_dimension_basis_records_present",
        "all_dimension_basis_records_bounded",
        "all_dimension_basis_records_reference_selected_candidate",
        "all_dimension_basis_records_reference_selected_boundary",
        "all_dimension_basis_records_non_result_preclaiming",
        "all_dimension_basis_records_admissible",
    )
    atomic_gate = {field: operation.get(field) is True for field in atomic_gate_fields}
    upstream["atomic_gate_validation"] = atomic_gate
    code, reason = _require(
        checks,
        "upstream.atomic_evaluation_gate",
        all(atomic_gate.values()),
        "UPSTREAM_EVALUATION_ATOMIC_GATE_INCOMPLETE",
        "selected V3 evaluation atomic gate is incomplete",
    )
    if code is not None:
        return code, reason, upstream
    code, reason = _require(
        checks,
        "upstream.evaluation_basis_complete",
        operation.get("evaluation_basis_complete") is True,
        "UPSTREAM_EVALUATION_BASIS_INCOMPLETE",
        "selected V3 evaluation basis is incomplete",
    )
    if code is not None:
        return code, reason, upstream

    aggregate = {
        "candidate_evaluated": operation.get("receiver_side_answerable_basis_candidate_evaluated") is True,
        "all_dimensions_satisfied": operation.get("receiver_side_answerable_basis_candidate_all_dimensions_satisfied") is True,
        "any_dimension_not_satisfied": operation.get("receiver_side_answerable_basis_candidate_any_dimension_not_satisfied") is False,
        "any_dimension_indeterminate": operation.get("receiver_side_answerable_basis_candidate_any_dimension_indeterminate") is False,
        "evaluation_operation_exhausted": operation.get("candidate_evaluation_operation_exhausted") is True,
    }
    upstream["candidate_aggregate_validation"] = aggregate
    for field, condition, failure_code in (
        ("candidate_evaluated", aggregate["candidate_evaluated"], "UPSTREAM_CANDIDATE_NOT_EVALUATED"),
        ("all_dimensions_satisfied", aggregate["all_dimensions_satisfied"], "UPSTREAM_ALL_DIMENSIONS_NOT_SATISFIED"),
        ("any_dimension_not_satisfied", aggregate["any_dimension_not_satisfied"], "UPSTREAM_DIMENSION_NOT_SATISFIED"),
        ("any_dimension_indeterminate", aggregate["any_dimension_indeterminate"], "UPSTREAM_DIMENSION_INDETERMINATE"),
        ("evaluation_operation_exhausted", aggregate["evaluation_operation_exhausted"], "UPSTREAM_OPERATION_NOT_EXHAUSTED"),
    ):
        code, reason = _require(checks, "upstream." + field, condition, failure_code, "selected V3 aggregate posture is invalid: " + field)
        if code is not None:
            return code, reason, upstream

    candidate_result_false = {
        "receiver_side_answerable_basis_candidate_sufficient": operation.get("receiver_side_answerable_basis_candidate_sufficient") is False,
        "receiver_side_answerable_basis_candidate_insufficient": operation.get("receiver_side_answerable_basis_candidate_insufficient") is False,
        "receiver_side_answerable_basis_candidate_indeterminate": operation.get("receiver_side_answerable_basis_candidate_indeterminate") is False,
    }
    upstream["current_false_posture_validation"] = dict(candidate_result_false)
    code, reason = _require(
        checks,
        "upstream.candidate_results_absent",
        all(candidate_result_false.values()),
        "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
        "selected V3 result already contains a candidate result",
    )
    if code is not None:
        return code, reason, upstream
    code, reason = _require(
        checks,
        "upstream.candidate_sufficiency_boundary_created",
        operation.get("candidate_sufficiency_boundary_created") is False,
        "UPSTREAM_SUFFICIENCY_BOUNDARY_ALREADY_CREATED",
        "selected V3 result already contains a sufficiency boundary",
    )
    if code is not None:
        return code, reason, upstream
    upstream["current_false_posture_validation"]["candidate_sufficiency_boundary_created"] = True

    rerun_false_fields = (
        "repeated_evaluation_permission_created",
        "reusable_route_created",
        "same_candidate_re_evaluation_authorized",
        "dimension_completion_route_created",
        "second_candidate_received",
        "second_candidate_evaluated",
    )
    downstream_false_fields = (
        "receiver_attestation_created",
        "receiver_attestation_supported",
        "receiver_answerable_receipt_present",
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
        "follow_on_authorized",
        "follow_on_work_authorized",
    )
    rerun_valid = all(operation.get(field) is False for field in rerun_false_fields)
    downstream_valid = all(operation.get(field) is False for field in downstream_false_fields)
    upstream["current_false_posture_validation"].update(
        {field: operation.get(field) is False for field in (*rerun_false_fields, *downstream_false_fields)}
    )
    code, reason = _require(
        checks, "upstream.rerun_route_postures", rerun_valid, "UPSTREAM_RERUN_OR_REUSABLE_ROUTE_PRESENT", "selected V3 result contains a rerun or reusable route"
    )
    if code is not None:
        return code, reason, upstream
    code, reason = _require(
        checks, "upstream.downstream_postures", downstream_valid, "UPSTREAM_DOWNSTREAM_POSTURE_ALREADY_PRESENT", "selected V3 result contains a downstream posture"
    )
    if code is not None:
        return code, reason, upstream

    if set(dimensions) != set(REQUIRED_DIMENSION_IDS):
        _add_failure(checks, "upstream.dimension_keys", "UPSTREAM_DIMENSION_NOT_EVALUATED")
        return "UPSTREAM_DIMENSION_NOT_EVALUATED", "selected V3 dimensions are not exact", upstream
    dimension_validation: dict[str, dict[str, Any]] = {}
    for dimension_id in REQUIRED_DIMENSION_IDS:
        entry = dimensions.get(dimension_id)
        if not isinstance(entry, Mapping):
            _add_failure(checks, "upstream.dimension." + dimension_id, "UPSTREAM_DIMENSION_NOT_EVALUATED")
            return "UPSTREAM_DIMENSION_NOT_EVALUATED", "selected V3 dimension is malformed", upstream
        safe_entry = {
            "dimension_result": entry.get("dimension_result"),
            "dimension_evaluated": entry.get("dimension_evaluated"),
            "dimension_established": entry.get("dimension_established"),
            "basis_referenced": entry.get("basis_referenced"),
            "missing_or_inconsistent_dimension_basis_count": (
                len(entry.get("missing_or_inconsistent_dimension_basis"))
                if isinstance(entry.get("missing_or_inconsistent_dimension_basis"), list)
                else None
            ),
        }
        dimension_validation[dimension_id] = safe_entry
        if entry.get("dimension_id") != dimension_id:
            _add_failure(checks, "upstream.dimension_id." + dimension_id, "UPSTREAM_DIMENSION_ID_MISMATCH")
            return "UPSTREAM_DIMENSION_ID_MISMATCH", "selected V3 dimension id does not match", upstream
        result = entry.get("dimension_result")
        if result == DIMENSION_RESULT_NOT_SATISFIED:
            _add_failure(checks, "upstream.dimension_result." + dimension_id, "UPSTREAM_DIMENSION_NOT_SATISFIED")
            return "UPSTREAM_DIMENSION_NOT_SATISFIED", "selected V3 dimension is not satisfied", upstream
        if result == DIMENSION_RESULT_INDETERMINATE:
            _add_failure(checks, "upstream.dimension_result." + dimension_id, "UPSTREAM_DIMENSION_INDETERMINATE")
            return "UPSTREAM_DIMENSION_INDETERMINATE", "selected V3 dimension is indeterminate", upstream
        if result != DIMENSION_RESULT_SATISFIED or entry.get("dimension_evaluated") is not True:
            _add_failure(checks, "upstream.dimension_result." + dimension_id, "UPSTREAM_DIMENSION_NOT_EVALUATED")
            return "UPSTREAM_DIMENSION_NOT_EVALUATED", "selected V3 dimension is not lawfully evaluated", upstream
        if entry.get("dimension_established") is not True:
            _add_failure(checks, "upstream.dimension_established." + dimension_id, "UPSTREAM_DIMENSION_NOT_ESTABLISHED")
            return "UPSTREAM_DIMENSION_NOT_ESTABLISHED", "selected V3 dimension is not established", upstream
        if entry.get("basis_referenced") is not True:
            _add_failure(checks, "upstream.dimension_basis." + dimension_id, "UPSTREAM_DIMENSION_BASIS_NOT_REFERENCED")
            return "UPSTREAM_DIMENSION_BASIS_NOT_REFERENCED", "selected V3 dimension basis is not referenced", upstream
        missing = entry.get("missing_or_inconsistent_dimension_basis")
        if not isinstance(missing, list) or missing:
            _add_failure(checks, "upstream.dimension_missing_basis." + dimension_id, "UPSTREAM_DIMENSION_BASIS_INCONSISTENT")
            return "UPSTREAM_DIMENSION_BASIS_INCONSISTENT", "selected V3 dimension has missing or inconsistent basis", upstream
    upstream["dimension_validation"] = dimension_validation

    open_state = artifact.get("what_remains_open")
    corrected_open_state = isinstance(open_state, list) and tuple(open_state) == _EXPECTED_V3_OPEN and not any(
        item in open_state for item in _STALE_V3_OPEN_ITEMS
    )
    upstream["corrected_open_state_validation"] = corrected_open_state
    code, reason = _require(
        checks,
        "upstream.corrected_what_remains_open",
        corrected_open_state,
        "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
        "selected V3 open state is stale or mismatched",
    )
    if code is not None:
        return code, reason, upstream
    return None, None, upstream


def _boundary_statement(allowed: bool) -> dict[str, bool]:
    return {
        "one_selected_completed_evaluation_consumed_as_upstream_standing": allowed,
        "evaluation_not_reopened": True,
        "evaluation_not_rerun": True,
        "candidate_sufficiency_not_decided": True,
        "candidate_sufficiency_operation_not_created": True,
        "consideration_allowed_only": allowed,
        "boundary_single_use": allowed,
        "boundary_exhausted_after_allowed_result": allowed,
        "result_level_non_claims_canonical_false": True,
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
        "open_does_not_mean_next_unless_separately_selected": True,
    }


def _boundary_non_meaning() -> dict[str, bool]:
    return {
        "evaluation_completion_is_not_candidate_sufficiency": True,
        "all_dimensions_satisfied_is_not_candidate_sufficiency": True,
        "consideration_allowed_is_not_sufficiency_decided": True,
        "boundary_result_is_not_candidate_sufficiency_operation": True,
        "boundary_exhaustion_is_not_operation_authorization": True,
        "candidate_sufficiency_is_not_receiver_attestation": True,
        "receiver_attestation_is_not_receiver_answerable_receipt": True,
        "receiver_answerable_receipt_is_not_presence_support": True,
    }


def _boundary_object(allowed: bool, upstream: Mapping[str, Any]) -> dict[str, Any]:
    aggregate = upstream.get("candidate_aggregate_validation")
    aggregate = aggregate if isinstance(aggregate, Mapping) else {}
    boundary_result = BOUNDARY_RESULT_ALLOWED if allowed else BOUNDARY_RESULT_NOT_EVALUATED
    boundary = {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_id": BOUNDARY_ID,
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_type": BOUNDARY_TYPE,
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_version": BOUNDARY_VERSION,
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_scope": BOUNDARY_SCOPE,
        "selected_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "selected_candidate_evaluation_operation_type": SELECTED_EVALUATION_OPERATION_TYPE,
        "selected_candidate_evaluation_operation_version": SELECTED_EVALUATION_OPERATION_VERSION,
        "selected_candidate_evaluation_result_required": SELECTED_EVALUATION_RESULT_REQUIRED,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "receiver_side_answerable_basis_candidate_evaluated": aggregate.get("candidate_evaluated") is True,
        "receiver_side_answerable_basis_candidate_all_dimensions_satisfied": aggregate.get("all_dimensions_satisfied") is True,
        "receiver_side_answerable_basis_candidate_any_dimension_not_satisfied": False,
        "receiver_side_answerable_basis_candidate_any_dimension_indeterminate": False,
        "candidate_sufficiency_boundary_recorded": allowed,
        "candidate_sufficiency_boundary_result_recorded": allowed,
        "candidate_sufficiency_boundary_result": boundary_result,
        "candidate_sufficiency_consideration_allowed": allowed,
        "candidate_sufficiency_boundary_exhausted": allowed,
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_recorded": allowed,
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_result_recorded": allowed,
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_result": boundary_result,
        **_canonical_non_claims(),
    }
    return boundary


def _declared_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "intent": request.get("intent"),
        "boundary_id": request.get("boundary_id"),
        "boundary_type": request.get("boundary_type"),
        "boundary_version": request.get("boundary_version"),
        "boundary_scope": request.get("boundary_scope"),
        "receiver_side_answerable_basis_candidate_id": request.get(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "receiver_side_answerable_basis_candidate_type": request.get(
            "receiver_side_answerable_basis_candidate_type"
        ),
        "receiver_side_answerable_basis_candidate_scope": request.get(
            "receiver_side_answerable_basis_candidate_scope"
        ),
        "selected_candidate_reception_operation_id": request.get(
            "selected_candidate_reception_operation_id"
        ),
        "selected_candidate_evaluation_boundary_id": request.get(
            "selected_candidate_evaluation_boundary_id"
        ),
        "selected_candidate_evaluation_operation_id": request.get(
            "selected_candidate_evaluation_operation_id"
        ),
        "selected_candidate_evaluation_operation_type": request.get(
            "selected_candidate_evaluation_operation_type"
        ),
        "selected_candidate_evaluation_operation_version": request.get(
            "selected_candidate_evaluation_operation_version"
        ),
        "governing_sufficiency_boundary_specification_path": request.get(
            "governing_sufficiency_boundary_specification_path"
        ),
        "selected_v3_evaluation_artifact_path": request.get("selected_v3_evaluation_artifact_path"),
        "admissible_future_route": request.get("admissible_future_route"),
        "declared_non_claims_validated": _declared_non_claims_valid(request.get("declared_non_claims")),
        "prohibited_request_flags_validated": all(
            request.get(field) is False for field in PROHIBITED_REQUEST_FLAGS
        ),
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get("receiver_side_answerable_basis_candidate_sufficiency_boundary")
    upstream = result.get("upstream_basis")
    boundary = boundary if isinstance(boundary, Mapping) else {}
    upstream = upstream if isinstance(upstream, Mapping) else {}
    return {
        "outcome": result.get("outcome"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "result_version": result.get("result_version"),
        "resolver_module": result.get("resolver_module"),
        "boundary_id": boundary.get("boundary_id"),
        "boundary_type": boundary.get("boundary_type"),
        "boundary_version": boundary.get("boundary_version"),
        "boundary_scope": boundary.get("boundary_scope"),
        "boundary_result": boundary.get("candidate_sufficiency_boundary_result"),
        "selected_candidate_id": boundary.get("receiver_side_answerable_basis_candidate_id"),
        "selected_evaluation_operation_id": boundary.get("selected_candidate_evaluation_operation_id"),
        "upstream_evaluation_outcome": upstream.get("selected_v3_metadata", {}).get("outcome") if isinstance(upstream.get("selected_v3_metadata"), Mapping) else None,
        "upstream_evaluation_result": upstream.get("selected_evaluation_identity", {}).get("operation_result") if isinstance(upstream.get("selected_evaluation_identity"), Mapping) else SELECTED_EVALUATION_RESULT_REQUIRED,
        "atomic_gate_validated": all(upstream.get("atomic_gate_validation", {}).values()) if isinstance(upstream.get("atomic_gate_validation"), Mapping) else False,
        "eight_dimensions_validated": len(upstream.get("dimension_validation", {})) == len(REQUIRED_DIMENSION_IDS) if isinstance(upstream.get("dimension_validation"), Mapping) else False,
        "candidate_aggregate_validated": all(upstream.get("candidate_aggregate_validation", {}).values()) if isinstance(upstream.get("candidate_aggregate_validation"), Mapping) else False,
        "exhaustion_validated": boundary.get("candidate_sufficiency_boundary_exhausted") is True,
        "current_false_posture_validated": all(upstream.get("current_false_posture_validation", {}).values()) if isinstance(upstream.get("current_false_posture_validation"), Mapping) else False,
        "candidate_sufficiency_consideration_allowed": boundary.get("candidate_sufficiency_consideration_allowed"),
        "candidate_results_false": all(boundary.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS[:3]),
        "repeated_reusable_rerun_false": all(
            boundary.get(field) is False
            for field in (
                "repeated_candidate_sufficiency_boundary_permission_created",
                "reusable_candidate_sufficiency_route_created",
                "same_candidate_sufficiency_boundary_rerun_authorized",
            )
        ),
        "receiver_receipt_presence_downstream_false": all(
            boundary.get(field) is False
            for field in (
                "receiver_attestation_created",
                "receiver_answerable_receipt_present",
                "presence_supported",
                "follow_on_work_authorized",
            )
        ),
        "governing_paths": copy.deepcopy(upstream.get("governing_paths", {})),
        "marker_validation": copy.deepcopy(upstream.get("marker_validation", {})),
    }


def _result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    *,
    upstream: Mapping[str, Any] | None = None,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    bounded_upstream = copy.deepcopy(dict(upstream)) if isinstance(upstream, Mapping) else _empty_upstream_basis(request)
    boundary = _boundary_object(allowed, bounded_upstream)
    result: dict[str, Any] = {
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_metadata": {
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
            "selected_v3_evaluation_artifact_path": request.get("selected_v3_evaluation_artifact_path"),
        },
        "declared_receiver_side_answerable_basis_candidate_sufficiency_boundary_basis": _declared_basis(request),
        "upstream_basis": bounded_upstream,
        "receiver_side_answerable_basis_candidate_sufficiency_boundary": boundary,
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_checks": copy.deepcopy(checks),
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_statement": _boundary_statement(allowed),
        "receiver_side_answerable_basis_candidate_sufficiency_boundary_non_meaning": _boundary_non_meaning(),
        "boundary_result_detail": {
            "boundary_result": boundary["candidate_sufficiency_boundary_result"],
            "candidate_sufficiency_boundary_exhausted": boundary["candidate_sufficiency_boundary_exhausted"],
            "selected_completed_evaluation_consumed": allowed,
        },
        "permitted_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "blocked_routes": [
            "evaluation_result_to_candidate_sufficiency",
            "all_dimensions_satisfied_to_candidate_sufficiency",
            "boundary_consideration_to_sufficiency_decision",
            "boundary_result_to_receiver_attestation_or_presence",
            "allowed_boundary_to_repeated_or_reusable_route",
            "candidate_sufficiency_boundary_to_contaminated_lineage_validation",
        ],
        "what_remains_open": list(ALLOWED_WHAT_REMAINS_OPEN) if allowed else [
            "candidate-sufficiency boundary, if separately selected"
        ],
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": code if outcome == OUTCOME_BLOCKED else None,
            "block_code": code if outcome == OUTCOME_BLOCKED else None,
            "reason": reason if outcome == OUTCOME_BLOCKED else None,
        },
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "failed_check_count": sum(check.get("passed") is False for check in checks),
        "passed_check_count": sum(check.get("passed") is True for check in checks),
    }
    result["receiver_side_answerable_basis_candidate_sufficiency_boundary_summary"] = _summary_from_result(result)
    return result


def resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one selected candidate-sufficiency consideration boundary."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared_request = build_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_request()
    elif not isinstance(request, Mapping):
        declared_request = build_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_request()
        _add_failure(checks, "declared_request_mapping", "REQUEST_NOT_MAPPING")
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="declared boundary request is not a mapping",
        )
    else:
        declared_request = copy.deepcopy(dict(request))

    code, reason = _validate_request(declared_request, checks)
    if code is not None:
        _add_failure(checks, "declared_request", code)
        return _result(declared_request, OUTCOME_BLOCKED, checks, code=code, reason=reason)
    if declared_request["intent"] == INTENT_DO_NOT_RECORD:
        return _result(declared_request, OUTCOME_NOT_RECORDED, checks)

    code, reason, upstream = _validate_upstream(declared_request, checks)
    if code is not None:
        _add_failure(checks, "upstream_basis", code)
        return _result(declared_request, OUTCOME_BLOCKED, checks, upstream=upstream, code=code, reason=reason)
    return _result(declared_request, OUTCOME_ALLOWED, checks, upstream=upstream)


def resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Read one declared request file without discovery and resolve it."""
    payload, error = _read_json(request_path)
    if error is not None or not isinstance(payload, Mapping):
        request = build_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_request()
        checks = [_check("declared_request_path", False, "REQUEST_NOT_MAPPING")]
        return _result(
            request,
            OUTCOME_BLOCKED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="declared boundary request path is unavailable, not parseable, or not a mapping",
        )
    return resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min(payload)


def build_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact, material-omitting summary for one boundary result."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    return _summary_from_result(result)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(path.stem + "_" + f"{index:03d}" + path.suffix)
        if not candidate.exists():
            return candidate
    raise ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def _contains_copied_material(value: Any) -> bool:
    forbidden_keys = {
        "candidate_material",
        "candidate_packet",
        "basis_items",
        "basis_references",
        "capture_material",
        "complete_v3_artifact",
        "selected_v3_artifact",
        "receiver_side_answerable_basis_candidate_evaluation_operation_basis",
        "receiver_side_answerable_basis_candidate_evaluation_operation_checks",
        "receiver_side_answerable_basis_candidate_evaluation_operation_dimensions",
    }
    if isinstance(value, Mapping):
        return any(key in forbidden_keys or _contains_copied_material(nested) for key, nested in value.items())
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_copied_material(item) for item in value)
    return False


def _output_path_is_forbidden(path: Path) -> bool:
    forbidden_fragments = (
        "spec",
        "tests",
        "reference",
        "presence",
        "relation",
        "identity",
        "field",
        "runtime",
        "api",
        "public-intake",
        "public_intake",
        "descendant",
        "receiver-capture",
        "receiver_capture",
        "candidate-reception",
        "candidate_reception",
        "evaluation-boundary",
        "evaluation_boundary",
        "evaluation-operation",
        "evaluation_operation",
        "evaluation-basis-declaration",
        "evaluation_basis_declaration",
    )
    return any(any(fragment in part.lower() for fragment in forbidden_fragments) for part in path.resolve().parts)


def write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write one valid material-omitting boundary result without overwrite."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    if result.get("resolver_module") != RESOLVER_MODULE or result.get("result_version") != RESULT_VERSION:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError(
            "WRITE_REFUSED: incompatible result metadata"
        )
    if result.get("outcome") not in OUTCOME_FAMILY:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError(
            "WRITE_REFUSED: unsupported result outcome"
        )
    if not _declared_non_claims_valid(result.get("non_claims")):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError(
            "WRITE_REFUSED: non-claims are not canonical false"
        )
    boundary = result.get("receiver_side_answerable_basis_candidate_sufficiency_boundary")
    if result.get("outcome") == OUTCOME_ALLOWED and (
        not isinstance(boundary, Mapping)
        or boundary.get("candidate_sufficiency_boundary_result") != BOUNDARY_RESULT_ALLOWED
        or boundary.get("candidate_sufficiency_consideration_allowed") is not True
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError(
            "WRITE_REFUSED: allowed outcome lacks the allowed boundary result"
        )
    if _contains_copied_material(result):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError(
            "WRITE_REFUSED: copied V3, basis, candidate, capture, or checks material"
        )
    target = _as_repo_path(output_path) if output_path is not None else OUTPUT_ROOT / OUTPUT_FILENAME
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError(
            "WRITE_REFUSED: output path is forbidden"
        )
    target = _next_available_output_path(target)
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as handle:
            json.dump(dict(result), handle, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False)
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
