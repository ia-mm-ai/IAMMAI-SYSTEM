"""Validate one bounded preparation-request declaration without issuing it.

This module records structural readiness for one later issuance attempt only.
It neither identifies a preparer nor creates request delivery, response,
declaration, evaluation, or downstream standing.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min"

REQUEST_ID = "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_001"
REQUEST_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_PREPARATION_REQUEST"
REQUEST_VERSION = "0.1.0"
REQUEST_SCOPE = "REQUEST_ONE_SEPARATELY_PREPARED_EVALUATION_BASIS_DECLARATION_FOR_ONE_SELECTED_CANDIDATE_ONLY"

REQUIRED_RESPONSE_DECLARATION_ID = "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_001"
REQUIRED_RESPONSE_DECLARATION_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION"
REQUIRED_RESPONSE_DECLARATION_VERSION = "0.1.0"
REQUIRED_RESPONSE_DECLARATION_SCOPE = "DECLARE_BOUNDED_EVALUATION_BASIS_FOR_ONE_SELECTED_CANDIDATE_ACROSS_EIGHT_DIMENSIONS_ONLY"

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
SELECTED_RECEPTION_OPERATION_ID = "receiver_side_answerable_basis_reception_operation_001"
SELECTED_EVALUATION_BOUNDARY_ID = "receiver_side_answerable_basis_candidate_evaluation_boundary_001"
SELECTED_EVALUATION_OPERATION_ID = "receiver_side_answerable_basis_candidate_evaluation_operation_001"
SELECTED_EVALUATION_BASIS_DECLARATION_ID = "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_001"
ADMISSIBLE_FUTURE_ROUTE = "PREPARATION_REQUEST_THEN_OPTIONAL_SEPARATELY_PREPARED_DECLARATION_RESPONSE_ONLY"

REQUIRED_RESPONSE_DIMENSION_IDS = (
    "candidate_structural_correspondence",
    "declared_provenance_posture",
    "receiver_authorship_posture",
    "separate_custody_posture",
    "refusability_posture",
    "could_have_been_withheld_posture",
    "prior_knock_correspondence_posture",
    "capture_record_posture",
)

OUTCOME_RECORDED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_PREPARATION_REQUEST_DECLARATION_RECORDED"
OUTCOME_REQUIRES_REQUEST_MATERIAL = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_PREPARATION_REQUEST_DECLARATION_REQUIRES_REQUEST_MATERIAL"
OUTCOME_BLOCKED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_PREPARATION_REQUEST_DECLARATION_BLOCKED"
OUTCOME_NOT_RECORDED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_PREPARATION_REQUEST_DECLARATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_REQUIRES_REQUEST_MATERIAL,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

REQUEST_RESULT_READY_FOR_ISSUANCE = "PREPARATION_REQUEST_READY_FOR_ISSUANCE"
REQUEST_RESULT_REQUIRES_REQUEST_MATERIAL = "REQUIRES_PREPARATION_REQUEST_MATERIAL"
REQUEST_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
REQUEST_RESULT_FAMILY = (
    REQUEST_RESULT_READY_FOR_ISSUANCE,
    REQUEST_RESULT_REQUIRES_REQUEST_MATERIAL,
    REQUEST_RESULT_NOT_EVALUATED,
)

INTENT_RECORD = "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_PREPARATION_REQUEST_DECLARATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_PREPARATION_REQUEST_DECLARATION"
INTENT_BLOCK = "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_PREPARATION_REQUEST_DECLARATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
PREPARATION_REQUEST_SPEC_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_PREPARATION_REQUEST_DECLARATION_V0_MIN_SPEC.md"
)
DECLARATION_TERMINAL_SUMMARY_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION_TERMINAL_SUMMARY_V0.md"
)
DECLARATION_WAITING_RESULT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min/"
    "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_001__"
    "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_result.json"
)
OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_001__"
    "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_result.json"
)

MAX_SERIALIZED_PREPARATION_REQUEST_MATERIAL_SIZE = 131_072
MAX_INTENDED_PREPARER_REFERENCE_LENGTH = 1_024
MAX_INTENDED_PREPARER_ROLE_DECLARATION_LENGTH = 1_024
MAX_INTENDED_PREPARER_CANDIDATE_RELATION_DECLARATION_LENGTH = 2_048
MAX_INTENDED_PREPARER_SOURCE_BODY_RELATION_DECLARATION_LENGTH = 2_048
MAX_INTENDED_PREPARER_CUSTODY_POSTURE_DECLARATION_LENGTH = 2_048
MAX_REQUEST_ORIGIN_REFERENCE_LENGTH = 1_024
MAX_REQUEST_TIMESTAMP_LENGTH = 256
MAX_REQUIRED_RESPONSE_DECLARATION_REFERENCE_LENGTH = 1_024
MAX_SERIALIZED_RESPONSE_SHAPE_REQUIREMENTS_SIZE = 16_384
MAX_SERIALIZED_REQUEST_STATEMENT_SIZE = 8_192
MAX_SERIALIZED_REQUEST_NON_MEANING_SIZE = 8_192
MAX_REQUIRED_RESPONSE_DIMENSIONS = len(REQUIRED_RESPONSE_DIMENSION_IDS)


class ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError(Exception):
    """Raised when a preparation-request result cannot be written lawfully."""


REQUEST_REQUIRED_FALSE_NON_CLAIMS = (
    "preparer_identity_established",
    "preparer_role_admitted",
    "preparer_authority_created",
    "preparer_standing_created",
    "evaluator_identity_established",
    "evaluator_authority_created",
    "evaluator_standing_created",
    "evaluator_truth_created",
    "preparer_independence_established",
    "preparer_separate_custody_established",
    "request_delivery_created",
    "preparer_reception_created",
    "preparer_acceptance_created",
    "preparer_obligation_created",
    "preparer_debt_created",
    "preparer_deadline_created",
    "declaration_created",
    "declaration_prepared",
    "declaration_recorded",
    "declaration_validated",
    "declaration_ready_for_supply",
    "declaration_supplied_to_operation",
    "declaration_admitted_by_operation",
    "evaluation_basis_created",
    "dimension_basis_records_created",
    "dimension_results_created",
    "candidate_evaluation_authorized",
    "candidate_evaluation_completed",
    "candidate_sufficiency_created",
    "receiver_attestation_created",
    "receiver_answerable_receipt_present",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "repeated_request_permission_created",
    "reusable_request_route_created",
    "alternate_preparer_route_created",
    "second_preparer_request_authorized",
    "automatic_reminder_created",
    "automatic_retry_created",
    "follow_on_authorized",
    "follow_on_work_authorized",
)

REQUIRED_FALSE_NON_CLAIMS = tuple(
    dict.fromkeys(
        (
            "preparation_request_recorded",
            "preparation_request_issued",
            "preparation_request_delivered",
            "preparation_request_received_by_preparer",
            "preparation_request_exhausted",
            "preparer_response_required",
            "preparer_response_due",
            "preparer_response_scheduled",
            "preparer_response_pending",
            "preparer_response_debt_created",
            "preparer_refusal_recorded",
            "preparer_silence_recorded",
            "declaration_response_received",
            "declaration_response_recorded",
            "declaration_response_validated",
            "declaration_response_ready_for_supply",
            "declaration_response_supplied_to_operation",
            "declaration_response_admitted_by_operation",
            *REQUEST_REQUIRED_FALSE_NON_CLAIMS,
            "shared_preparer_route_created",
            "identity_created",
            "relation_created",
            "coupling_created",
            "field_machinery_created",
            "runtime_created",
            "api_created",
            "public_intake_created",
            "authority_created",
            "standing_created",
            "output_authorized",
            "action_authorized",
            "synchronization_authorized",
            "prior_unsupported_candidate_a_claim_validated",
            "prior_unsupported_candidate_b_claim_validated",
            "prior_unsupported_derivation_event_claim_validated",
            "affected_file_repaired",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
        )
    )
)

PROHIBITED_REQUEST_FLAGS = {
    "request_live_issuance": "PROHIBITED_LIVE_ISSUANCE_DELIVERY_RECEPTION_OR_ACCEPTANCE_REQUESTED",
    "request_delivery": "PROHIBITED_LIVE_ISSUANCE_DELIVERY_RECEPTION_OR_ACCEPTANCE_REQUESTED",
    "request_preparer_reception": "PROHIBITED_LIVE_ISSUANCE_DELIVERY_RECEPTION_OR_ACCEPTANCE_REQUESTED",
    "request_preparer_acceptance": "PROHIBITED_LIVE_ISSUANCE_DELIVERY_RECEPTION_OR_ACCEPTANCE_REQUESTED",
    "request_preparer_role_admission": "PROHIBITED_PREPARER_IDENTITY_ROLE_CUSTODY_INDEPENDENCE_AUTHORITY_OR_STANDING_REQUESTED",
    "request_preparer_identity_establishment": "PROHIBITED_PREPARER_IDENTITY_ROLE_CUSTODY_INDEPENDENCE_AUTHORITY_OR_STANDING_REQUESTED",
    "request_preparer_independence_establishment": "PROHIBITED_PREPARER_IDENTITY_ROLE_CUSTODY_INDEPENDENCE_AUTHORITY_OR_STANDING_REQUESTED",
    "request_preparer_separate_custody_establishment": "PROHIBITED_PREPARER_IDENTITY_ROLE_CUSTODY_INDEPENDENCE_AUTHORITY_OR_STANDING_REQUESTED",
    "request_preparer_authority_creation": "PROHIBITED_PREPARER_IDENTITY_ROLE_CUSTODY_INDEPENDENCE_AUTHORITY_OR_STANDING_REQUESTED",
    "request_preparer_standing_creation": "PROHIBITED_PREPARER_IDENTITY_ROLE_CUSTODY_INDEPENDENCE_AUTHORITY_OR_STANDING_REQUESTED",
    "request_evaluator_identity_establishment": "PROHIBITED_EVALUATOR_IDENTITY_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_evaluator_authority_creation": "PROHIBITED_EVALUATOR_IDENTITY_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_evaluator_standing_creation": "PROHIBITED_EVALUATOR_IDENTITY_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_evaluator_truth_creation": "PROHIBITED_EVALUATOR_IDENTITY_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_preparer_obligation_creation": "PROHIBITED_OBLIGATION_DEADLINE_DEBT_OR_RESPONSE_REQUIREMENT_REQUESTED",
    "request_preparer_deadline_creation": "PROHIBITED_OBLIGATION_DEADLINE_DEBT_OR_RESPONSE_REQUIREMENT_REQUESTED",
    "request_preparer_debt_creation": "PROHIBITED_OBLIGATION_DEADLINE_DEBT_OR_RESPONSE_REQUIREMENT_REQUESTED",
    "request_response_required": "PROHIBITED_OBLIGATION_DEADLINE_DEBT_OR_RESPONSE_REQUIREMENT_REQUESTED",
    "request_response_due": "PROHIBITED_OBLIGATION_DEADLINE_DEBT_OR_RESPONSE_REQUIREMENT_REQUESTED",
    "request_response_scheduled": "PROHIBITED_OBLIGATION_DEADLINE_DEBT_OR_RESPONSE_REQUIREMENT_REQUESTED",
    "request_response_pending": "PROHIBITED_OBLIGATION_DEADLINE_DEBT_OR_RESPONSE_REQUIREMENT_REQUESTED",
    "request_automatic_reminder_creation": "PROHIBITED_REMINDER_RETRY_REPEATED_REUSABLE_ALTERNATE_SECOND_OR_SHARED_ROUTE_REQUESTED",
    "request_automatic_retry_creation": "PROHIBITED_REMINDER_RETRY_REPEATED_REUSABLE_ALTERNATE_SECOND_OR_SHARED_ROUTE_REQUESTED",
    "request_repeated_request_permission_creation": "PROHIBITED_REMINDER_RETRY_REPEATED_REUSABLE_ALTERNATE_SECOND_OR_SHARED_ROUTE_REQUESTED",
    "request_reusable_request_route_creation": "PROHIBITED_REMINDER_RETRY_REPEATED_REUSABLE_ALTERNATE_SECOND_OR_SHARED_ROUTE_REQUESTED",
    "request_alternate_preparer_route_creation": "PROHIBITED_REMINDER_RETRY_REPEATED_REUSABLE_ALTERNATE_SECOND_OR_SHARED_ROUTE_REQUESTED",
    "request_second_preparer_authorization": "PROHIBITED_REMINDER_RETRY_REPEATED_REUSABLE_ALTERNATE_SECOND_OR_SHARED_ROUTE_REQUESTED",
    "request_shared_preparer_route_creation": "PROHIBITED_REMINDER_RETRY_REPEATED_REUSABLE_ALTERNATE_SECOND_OR_SHARED_ROUTE_REQUESTED",
    "request_declaration_creation": "PROHIBITED_DECLARATION_CREATION_PREPARATION_VALIDATION_SUPPLY_OR_ADMISSION_REQUESTED",
    "request_declaration_preparation": "PROHIBITED_DECLARATION_CREATION_PREPARATION_VALIDATION_SUPPLY_OR_ADMISSION_REQUESTED",
    "request_declaration_validation": "PROHIBITED_DECLARATION_CREATION_PREPARATION_VALIDATION_SUPPLY_OR_ADMISSION_REQUESTED",
    "request_declaration_ready_for_supply": "PROHIBITED_DECLARATION_CREATION_PREPARATION_VALIDATION_SUPPLY_OR_ADMISSION_REQUESTED",
    "request_declaration_supply_to_operation": "PROHIBITED_DECLARATION_CREATION_PREPARATION_VALIDATION_SUPPLY_OR_ADMISSION_REQUESTED",
    "request_declaration_admission_by_operation": "PROHIBITED_DECLARATION_CREATION_PREPARATION_VALIDATION_SUPPLY_OR_ADMISSION_REQUESTED",
    "request_evaluation_basis_creation": "PROHIBITED_EVALUATION_BASIS_DIMENSION_RESULT_OR_CANDIDATE_RESULT_REQUESTED",
    "request_dimension_basis_record_creation": "PROHIBITED_EVALUATION_BASIS_DIMENSION_RESULT_OR_CANDIDATE_RESULT_REQUESTED",
    "request_dimension_result_derivation": "PROHIBITED_EVALUATION_BASIS_DIMENSION_RESULT_OR_CANDIDATE_RESULT_REQUESTED",
    "request_candidate_evaluation": "PROHIBITED_EVALUATION_BASIS_DIMENSION_RESULT_OR_CANDIDATE_RESULT_REQUESTED",
    "request_candidate_sufficiency": "PROHIBITED_EVALUATION_BASIS_DIMENSION_RESULT_OR_CANDIDATE_RESULT_REQUESTED",
    "request_receiver_attestation_creation": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_receiver_answerable_receipt_creation": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_presence_support": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_presence_authorization": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_presence_establishment": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_presence_recording": "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_identity_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_relation_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_coupling_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_OR_STANDING_REQUESTED",
    "request_api_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_OR_STANDING_REQUESTED",
    "request_public_intake_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_OR_STANDING_REQUESTED",
    "request_authority_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_OR_STANDING_REQUESTED",
    "request_standing_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_OR_STANDING_REQUESTED",
    "request_output_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_action_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
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
        "PREPARATION_REQUEST_SPEC_REFERENCE_MISSING",
        "PREPARATION_REQUEST_SPEC_MARKER_MISSING",
        "DECLARATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DECLARATION_TERMINAL_SUMMARY_MARKER_MISSING",
        "DECLARATION_WAITING_RESULT_REFERENCE_MISSING",
        "DECLARATION_WAITING_RESULT_NOT_PARSEABLE",
        "DECLARATION_WAITING_RESULT_NOT_MAPPING",
        "REQUEST_VALUE_MISMATCH",
        "PREPARATION_REQUEST_MATERIAL_NOT_MAPPING",
        "PREPARATION_REQUEST_MATERIAL_OVERSIZED",
        "PREPARATION_REQUEST_TOP_LEVEL_FIELD_UNKNOWN",
        "PREPARATION_REQUEST_REQUIRED_FIELD_MISSING",
        "PREPARATION_REQUEST_FIELD_MALFORMED",
        "PREPARATION_REQUEST_SELECTED_IDENTITY_MISMATCH",
        "PREPARATION_REQUEST_RESPONSE_DIMENSION_SCOPE_MISMATCH",
        "PREPARATION_REQUEST_NON_CLAIM_MISSING_OR_FLIPPED",
        "PREPARATION_REQUEST_RESPONSE_NOT_OPTIONAL",
        "PREPARATION_REQUEST_NOT_SINGLE_USE",
        "PREPARATION_REQUEST_RESULT_PRECLAIMED",
        "PROHIBITED_LIVE_ISSUANCE_DELIVERY_RECEPTION_OR_ACCEPTANCE_REQUESTED",
        "PROHIBITED_PREPARER_IDENTITY_ROLE_CUSTODY_INDEPENDENCE_AUTHORITY_OR_STANDING_REQUESTED",
        "PROHIBITED_EVALUATOR_IDENTITY_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
        "PROHIBITED_OBLIGATION_DEADLINE_DEBT_OR_RESPONSE_REQUIREMENT_REQUESTED",
        "PROHIBITED_REMINDER_RETRY_REPEATED_REUSABLE_ALTERNATE_SECOND_OR_SHARED_ROUTE_REQUESTED",
        "PROHIBITED_DECLARATION_CREATION_PREPARATION_VALIDATION_SUPPLY_OR_ADMISSION_REQUESTED",
        "PROHIBITED_EVALUATION_BASIS_DIMENSION_RESULT_OR_CANDIDATE_RESULT_REQUESTED",
        "PROHIBITED_RECEIVER_ATTESTATION_ANSWERABLE_RECEIPT_OR_PRESENCE_REQUESTED",
        "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
        "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_AUTHORITY_OR_STANDING_REQUESTED",
        "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "EXPLICIT_BLOCK_REQUESTED",
        "WRITE_REFUSED",
    }
)

PREPARATION_REQUEST_SPEC_MARKER_CLASSES = {
    "title": ("# Receiver-Side Answerable Basis Candidate Evaluation Basis Preparation Request Declaration V0 Minimum Specification",),
    "identity": (REQUEST_ID, REQUEST_TYPE, REQUEST_SCOPE),
    "response": (REQUIRED_RESPONSE_DECLARATION_ID, ADMISSIBLE_FUTURE_ROUTE),
    "optional_single_use": ("Response remains optional.", "preparation_request_single_use = true"),
    "dimensions": REQUIRED_RESPONSE_DIMENSION_IDS,
}
DECLARATION_SUMMARY_MARKER_CLASSES = {
    "title": ("# Receiver-Side Answerable Basis Candidate Evaluation Basis Declaration Terminal Summary V0",),
    "waiting": (
        "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION_REQUIRES_DECLARATION_MATERIAL",
        "declaration_result = REQUIRES_DECLARATION_MATERIAL",
    ),
    "absence": ("No declaration material", "dimension_record_count = 0"),
}

RESULT_PRECLAIM_FIELDS = frozenset(
    {
        "preparation_request_declaration_recorded",
        "preparation_request_declaration_result_recorded",
        "request_result",
        "preparation_request_material_received",
        "preparation_request_material_recorded",
        "preparation_request_declaration_complete",
        "all_selected_identities_match",
        "intended_preparer_reference_supplied",
        "intended_preparer_role_declared",
        "intended_preparer_relation_to_candidate_declared",
        "intended_preparer_relation_to_source_body_declared",
        "intended_preparer_custody_posture_declared",
        "request_origin_reference_supplied",
        "request_timestamp_supplied",
        "required_response_declaration_reference_supplied",
        "exact_eight_dimension_response_scope",
        "request_non_claims_false",
        "preparation_request_ready_for_issuance",
        *REQUIRED_FALSE_NON_CLAIMS,
    }
)

ALLOWED_PREPARATION_REQUEST_MATERIAL_KEYS = frozenset(
    {
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_id",
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_type",
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_version",
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_scope",
        "receiver_side_answerable_basis_candidate_id",
        "receiver_side_answerable_basis_candidate_type",
        "receiver_side_answerable_basis_candidate_scope",
        "selected_candidate_reception_operation_id",
        "selected_candidate_evaluation_boundary_id",
        "selected_candidate_evaluation_operation_id",
        "selected_evaluation_basis_declaration_id",
        "required_response_declaration_id",
        "required_response_declaration_type",
        "required_response_declaration_version",
        "required_response_declaration_scope",
        "admissible_future_route",
        "intended_preparer_reference",
        "intended_preparer_role_declaration",
        "intended_preparer_relation_to_candidate_declaration",
        "intended_preparer_relation_to_source_body_declaration",
        "intended_preparer_custody_posture_declaration",
        "request_origin_reference",
        "request_timestamp",
        "required_response_declaration_reference",
        "response_shape_requirements",
        "required_response_dimension_ids",
        "request_statement",
        "request_non_meaning",
        "request_non_claims",
        "response_optional",
        "preparation_request_single_use",
    }
)
REQUIRED_PREPARATION_REQUEST_MATERIAL_KEYS = ALLOWED_PREPARATION_REQUEST_MATERIAL_KEYS

WHAT_REMAINS_OPEN = (
    "one complete bounded preparation-request declaration",
    "intended preparer reference",
    "intended preparer role declaration",
    "relation-to-candidate declaration",
    "relation-to-source-body declaration",
    "custody-posture declaration",
    "request-origin reference",
    "request timestamp",
    "required response declaration reference",
    "response-shape requirements",
    "exact eight-dimension response scope",
    "request structural validation",
    "request ready-for-issuance result",
    "one later issuance attempt",
    "issuance trace",
    "optional delivery",
    "optional preparer reception",
    "optional preparer response",
    "one separately prepared evaluation-basis declaration",
    "declaration validation",
    "separate supply to evaluation operation",
    "operation admission",
    "candidate evaluation",
    "dimension results",
    "candidate-sufficiency boundary after completed evaluation",
    "later attestation, receipt, and presence questions only after lawful basis",
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


def _exact_bool(value: Any) -> bool:
    return value is True or value is False


def _serialized_size(value: Any) -> int | None:
    try:
        return len(json.dumps(value, ensure_ascii=True, sort_keys=True, allow_nan=False).encode("utf-8"))
    except (TypeError, ValueError):
        return None


def _json_compatible(value: Any) -> bool:
    return _serialized_size(value) is not None


def _as_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _display_path(value: Path | str) -> str:
    path = _as_path(value)
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _read_text(value: Path | str) -> tuple[str | None, str | None]:
    try:
        path = _as_path(value)
        if not path.is_file():
            return None, "not_a_file"
        return path.read_text(encoding="utf-8"), None
    except (OSError, UnicodeDecodeError):
        return None, "unreadable"


def _read_json(value: Path | str) -> tuple[Any | None, str | None]:
    text, error = _read_text(value)
    if error is not None or text is None:
        return None, error
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        return None, "not_parseable"


def _check(name: str, passed: bool, code: str | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {"name": name, "passed": passed}
    if not passed and code is not None:
        item["block_code"] = code
        item["failure_code"] = code
    return item


def _failure(checks: list[dict[str, Any]], name: str, code: str) -> None:
    checks.append(_check(name, False, code))


def _all_false_mapping(value: Any, keys: Sequence[str]) -> bool:
    return isinstance(value, Mapping) and all(value.get(key) is False for key in keys)


def _canonical_request_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUEST_REQUIRED_FALSE_NON_CLAIMS}


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _marker_status(text: str, marker_classes: Mapping[str, Sequence[str]]) -> dict[str, bool]:
    return {name: all(marker in text for marker in markers) for name, markers in marker_classes.items()}


def _expected_request_values() -> dict[str, str]:
    return {
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_id": REQUEST_ID,
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_type": REQUEST_TYPE,
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_version": REQUEST_VERSION,
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_scope": REQUEST_SCOPE,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "selected_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "selected_evaluation_basis_declaration_id": SELECTED_EVALUATION_BASIS_DECLARATION_ID,
        "required_response_declaration_id": REQUIRED_RESPONSE_DECLARATION_ID,
        "required_response_declaration_type": REQUIRED_RESPONSE_DECLARATION_TYPE,
        "required_response_declaration_version": REQUIRED_RESPONSE_DECLARATION_VERSION,
        "required_response_declaration_scope": REQUIRED_RESPONSE_DECLARATION_SCOPE,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    }


def _request_allowed_keys() -> frozenset[str]:
    return frozenset(
        {
            "intent",
            "preparation_request_material_supplied",
            "preparation_request_material",
            "declared_non_claims",
            *tuple(_expected_request_values()),
            *tuple(PROHIBITED_REQUEST_FLAGS),
        }
    )


def _string_within(value: Any, maximum: int) -> bool:
    return isinstance(value, str) and bool(value.strip()) and len(value) <= maximum


def _metadata_for_material(material: Mapping[str, Any] | None, complete: bool) -> dict[str, Any]:
    if not isinstance(material, Mapping):
        return {
            "preparation_request_material_present": False,
            "intended_preparer_reference_supplied": False,
            "intended_preparer_role_declared": False,
            "relation_to_candidate_declared": False,
            "relation_to_source_body_declared": False,
            "custody_posture_declared": False,
            "request_origin_reference_supplied": False,
            "request_timestamp_supplied": False,
            "required_response_declaration_reference_supplied": False,
            "required_response_dimension_ids": [],
            "response_shape_requirement_key_names": [],
            "request_non_claims_validated": False,
            "complete_preparation_request_material_omitted_from_result": True,
            "sensitive_preparer_address_declarations_omitted_from_result": True,
            "candidate_material_omitted_from_result": True,
        }
    response_shape = material.get("response_shape_requirements")
    dimensions = material.get("required_response_dimension_ids")
    return {
        "preparation_request_material_present": True,
        "request_identifiers": {
            key: material.get(key)
            for key in (
                "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_id",
                "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_type",
                "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_version",
                "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_scope",
            )
        },
        "selected_identifiers": {
            key: material.get(key)
            for key in (
                "receiver_side_answerable_basis_candidate_id",
                "receiver_side_answerable_basis_candidate_type",
                "receiver_side_answerable_basis_candidate_scope",
                "selected_candidate_reception_operation_id",
                "selected_candidate_evaluation_boundary_id",
                "selected_candidate_evaluation_operation_id",
                "selected_evaluation_basis_declaration_id",
            )
        },
        "required_response_identifiers": {
            key: material.get(key)
            for key in (
                "required_response_declaration_id",
                "required_response_declaration_type",
                "required_response_declaration_version",
                "required_response_declaration_scope",
            )
        },
        "intended_preparer_reference_supplied": _string_within(
            material.get("intended_preparer_reference"), MAX_INTENDED_PREPARER_REFERENCE_LENGTH
        ),
        "intended_preparer_role_declared": _string_within(
            material.get("intended_preparer_role_declaration"), MAX_INTENDED_PREPARER_ROLE_DECLARATION_LENGTH
        ),
        "relation_to_candidate_declared": _string_within(
            material.get("intended_preparer_relation_to_candidate_declaration"),
            MAX_INTENDED_PREPARER_CANDIDATE_RELATION_DECLARATION_LENGTH,
        ),
        "relation_to_source_body_declared": _string_within(
            material.get("intended_preparer_relation_to_source_body_declaration"),
            MAX_INTENDED_PREPARER_SOURCE_BODY_RELATION_DECLARATION_LENGTH,
        ),
        "custody_posture_declared": _string_within(
            material.get("intended_preparer_custody_posture_declaration"),
            MAX_INTENDED_PREPARER_CUSTODY_POSTURE_DECLARATION_LENGTH,
        ),
        "request_origin_reference_supplied": _string_within(
            material.get("request_origin_reference"), MAX_REQUEST_ORIGIN_REFERENCE_LENGTH
        ),
        "request_timestamp_supplied": _string_within(material.get("request_timestamp"), MAX_REQUEST_TIMESTAMP_LENGTH),
        "required_response_declaration_reference_supplied": _string_within(
            material.get("required_response_declaration_reference"), MAX_REQUIRED_RESPONSE_DECLARATION_REFERENCE_LENGTH
        ),
        "required_response_dimension_ids": list(dimensions)
        if isinstance(dimensions, Sequence) and not isinstance(dimensions, (str, bytes))
        else [],
        "response_shape_requirement_key_names": sorted(response_shape)
        if isinstance(response_shape, Mapping)
        else [],
        "request_non_claims_validated": _all_false_mapping(
            material.get("request_non_claims"), REQUEST_REQUIRED_FALSE_NON_CLAIMS
        ),
        "response_optional": material.get("response_optional") is True,
        "preparation_request_single_use": material.get("preparation_request_single_use") is True,
        "complete_preparation_request_validated": complete,
        "complete_preparation_request_material_omitted_from_result": True,
        "sensitive_preparer_address_declarations_omitted_from_result": True,
        "candidate_material_omitted_from_result": True,
    }


def _request_state(
    outcome: str,
    request_result: str,
    *,
    material_supplied: bool,
    complete: bool = False,
) -> dict[str, Any]:
    recorded = outcome in (OUTCOME_RECORDED, OUTCOME_REQUIRES_REQUEST_MATERIAL)
    ready = outcome == OUTCOME_RECORDED
    state: dict[str, Any] = {
        "request_id": REQUEST_ID,
        "request_type": REQUEST_TYPE,
        "request_version": REQUEST_VERSION,
        "request_scope": REQUEST_SCOPE,
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_id": REQUEST_ID,
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_type": REQUEST_TYPE,
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_version": REQUEST_VERSION,
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_scope": REQUEST_SCOPE,
        "preparation_request_declaration_recorded": recorded,
        "preparation_request_declaration_result_recorded": recorded,
        "request_result": request_result,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "preparation_request_material_supplied": material_supplied,
        "preparation_request_material_received": ready,
        "preparation_request_material_recorded": ready,
        "preparation_request_declaration_complete": complete,
        "all_selected_identities_match": complete,
        "intended_preparer_reference_supplied": complete,
        "intended_preparer_role_declared": complete,
        "intended_preparer_relation_to_candidate_declared": complete,
        "intended_preparer_relation_to_source_body_declared": complete,
        "intended_preparer_custody_posture_declared": complete,
        "request_origin_reference_supplied": complete,
        "request_timestamp_supplied": complete,
        "required_response_declaration_reference_supplied": complete,
        "exact_eight_dimension_response_scope": complete,
        "request_non_claims_false": complete,
        "response_optional": ready,
        "preparation_request_single_use": ready,
        "preparation_request_ready_for_issuance": ready,
    }
    state.update(_canonical_non_claims())
    return state


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    declaration = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration")
    material = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_material")
    upstream = result.get("upstream_basis")
    declaration = declaration if isinstance(declaration, Mapping) else {}
    material = material if isinstance(material, Mapping) else {}
    upstream = upstream if isinstance(upstream, Mapping) else {}
    return {
        "outcome": result.get("outcome"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "result_version": result.get("result_version"),
        "resolver_module": result.get("resolver_module"),
        "request_id": declaration.get("request_id"),
        "request_type": declaration.get("request_type"),
        "request_version": declaration.get("request_version"),
        "request_scope": declaration.get("request_scope"),
        "request_result": declaration.get("request_result"),
        "selected_identities": copy.deepcopy(material.get("selected_identifiers", {})),
        "required_response_identities": copy.deepcopy(material.get("required_response_identifiers", {})),
        "request_material_postures": {
            key: declaration.get(key)
            for key in (
                "preparation_request_material_supplied",
                "preparation_request_material_received",
                "preparation_request_material_recorded",
                "intended_preparer_reference_supplied",
                "intended_preparer_role_declared",
                "intended_preparer_relation_to_candidate_declared",
                "intended_preparer_relation_to_source_body_declared",
                "intended_preparer_custody_posture_declared",
                "preparation_request_declaration_complete",
                "preparation_request_ready_for_issuance",
                "preparation_request_recorded",
                "preparation_request_issued",
                "preparation_request_delivered",
                "preparation_request_received_by_preparer",
                "preparation_request_exhausted",
                "response_optional",
                "preparation_request_single_use",
            )
        },
        "required_response_dimension_ids": copy.deepcopy(material.get("required_response_dimension_ids", [])),
        "bounded_request_material_metadata": copy.deepcopy(material),
        "missing_or_incomplete_request_material": copy.deepcopy(result.get("missing_or_incomplete_request_material", [])),
        "governing_paths": copy.deepcopy(upstream.get("governing_paths", {})),
        "marker_validation": copy.deepcopy(upstream.get("marker_validation", {})),
        "non_claims_canonical_false": _all_false_mapping(result.get("non_claims"), REQUIRED_FALSE_NON_CLAIMS),
    }


def _result(
    request: Mapping[str, Any],
    outcome: str,
    request_result: str,
    checks: list[dict[str, Any]],
    *,
    upstream: Mapping[str, Any] | None = None,
    material: Mapping[str, Any] | None = None,
    complete: bool = False,
    missing: Sequence[str] = (),
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    supplied = request.get("preparation_request_material_supplied") is True
    state = _request_state(outcome, request_result, material_supplied=supplied, complete=complete)
    declared = {
        key: copy.deepcopy(request[key])
        for key in ("intent", "preparation_request_material_supplied", *tuple(_expected_request_values()))
        if key in request
    }
    declared["complete_preparation_request_material_omitted_from_result"] = True
    result: dict[str, Any] = {
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_metadata": {
            "request_id": REQUEST_ID,
            "request_type": REQUEST_TYPE,
            "request_version": REQUEST_VERSION,
            "request_scope": REQUEST_SCOPE,
        },
        "declared_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_basis": declared,
        "upstream_basis": copy.deepcopy(dict(upstream or {})),
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration": state,
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_material": _metadata_for_material(
            material, complete
        ),
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_checks": copy.deepcopy(checks),
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_statement": {
            "request_structure_only": outcome in (OUTCOME_RECORDED, OUTCOME_REQUIRES_REQUEST_MATERIAL),
            "complete_preparation_request_material_omitted_from_result": True,
            "sensitive_preparer_address_declarations_omitted_from_result": True,
            "candidate_material_omitted_from_result": True,
            "request_not_issued": True,
            "response_not_created": True,
            "operation_not_invoked": True,
            "no_dimension_result_derived": True,
            "result_level_non_claims_canonical_false": True,
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
            "open_does_not_mean_next_unless_separately_selected": True,
        },
        "receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_non_meaning": {
            "preparer_reference_is_not_identity_or_authority": True,
            "request_is_not_issuance_or_obligation": True,
            "response_optional_is_not_pending_obligation": True,
            "ready_for_issuance_is_not_issuance": True,
            "request_is_not_declaration_or_evaluation": True,
        },
        "request_result_detail": {
            "request_result": request_result,
            "preparation_request_material_supplied": supplied,
            "preparation_request_material_received": outcome == OUTCOME_RECORDED and complete,
            "preparation_request_material_recorded": outcome == OUTCOME_RECORDED and complete,
            "preparation_request_declaration_complete": complete,
            "ready_for_issuance": outcome == OUTCOME_RECORDED,
            "request_recorded": False,
            "request_issued": False,
            "request_delivered": False,
            "request_received_by_preparer": False,
            "request_exhausted": False,
            "response_exists": False,
            "operation_invocation_exists": False,
            "dimension_result_exists": False,
        },
        "permitted_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "blocked_routes": [
            "live issuance, delivery, preparer reception, or acceptance",
            "preparer identity, role admission, custody, independence, authority, or standing",
            "obligation, deadline, debt, reminder, retry, or reusable route",
            "declaration creation, validation, supply, admission, evaluation, or result derivation",
            "repair, scan, discovery, or validation enforcement",
        ],
        "missing_or_incomplete_request_material": list(missing),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
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
    }
    result["failed_check_count"] = sum(check.get("passed") is False for check in checks)
    result["passed_check_count"] = sum(check.get("passed") is True for check in checks)
    result["receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_summary"] = _summary_from_result(result)
    return result


def _validate_request(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> tuple[str | None, str | None]:
    for key in RESULT_PRECLAIM_FIELDS:
        if key in request:
            _failure(checks, f"request_{key}_not_preclaimed", "RESULT_POSTURE_PRECLAIMED")
            return "RESULT_POSTURE_PRECLAIMED", f"{key} is a result or downstream posture preclaim"
    unknown = set(request) - _request_allowed_keys()
    if unknown:
        _failure(checks, "request_has_only_supported_fields", "REQUEST_VALUE_MISMATCH")
        return "REQUEST_VALUE_MISMATCH", "request contains unsupported fields"
    intent = request.get("intent")
    if intent not in SUPPORTED_INTENTS:
        _failure(checks, "intent_supported", "UNSUPPORTED_INTENT")
        return "UNSUPPORTED_INTENT", "intent is unsupported"
    if intent == INTENT_BLOCK:
        _failure(checks, "intent_not_explicit_block", "EXPLICIT_BLOCK_REQUESTED")
        return "EXPLICIT_BLOCK_REQUESTED", "explicit block intent"
    for key, expected in _expected_request_values().items():
        if request.get(key) != expected:
            _failure(checks, f"request_{key}_matches", "REQUEST_VALUE_MISMATCH")
            return "REQUEST_VALUE_MISMATCH", f"{key} does not match the selected request line"
    if not _exact_bool(request.get("preparation_request_material_supplied")):
        _failure(checks, "preparation_request_material_supplied_is_boolean", "REQUEST_VALUE_MISMATCH")
        return "REQUEST_VALUE_MISMATCH", "preparation_request_material_supplied must be boolean"
    if not _all_false_mapping(request.get("declared_non_claims"), REQUEST_REQUIRED_FALSE_NON_CLAIMS):
        _failure(checks, "declared_non_claims_are_canonical_false", "NON_CLAIM_MISSING_OR_FLIPPED")
        return "NON_CLAIM_MISSING_OR_FLIPPED", "declared non-claims are missing or flipped"
    for key, code in PROHIBITED_REQUEST_FLAGS.items():
        value = request.get(key)
        if value is True:
            _failure(checks, f"{key}_not_requested", code)
            return code, f"{key} is prohibited"
        if value is not False:
            _failure(checks, f"{key}_is_false", "REQUEST_VALUE_MISMATCH")
            return "REQUEST_VALUE_MISMATCH", f"{key} must be false"
    material = request.get("preparation_request_material")
    if material is not None and request.get("preparation_request_material_supplied") is not True:
        _failure(checks, "material_matches_supplied_posture", "REQUEST_VALUE_MISMATCH")
        return "REQUEST_VALUE_MISMATCH", "material is present while supplied posture is false"
    checks.append(_check("request_is_bounded", True))
    return None, None


def _validate_upstream(checks: list[dict[str, Any]]) -> tuple[dict[str, Any], str | None, str | None]:
    upstream: dict[str, Any] = {
        "governing_paths": {
            "preparation_request_spec": _display_path(PREPARATION_REQUEST_SPEC_RELATIVE_PATH),
            "declaration_terminal_summary": _display_path(DECLARATION_TERMINAL_SUMMARY_RELATIVE_PATH),
            "declaration_waiting_result": _display_path(DECLARATION_WAITING_RESULT_RELATIVE_PATH),
        },
        "marker_validation": {},
    }
    spec_text, error = _read_text(PREPARATION_REQUEST_SPEC_RELATIVE_PATH)
    if error is not None or spec_text is None:
        _failure(checks, "preparation_request_spec_reference_exists", "PREPARATION_REQUEST_SPEC_REFERENCE_MISSING")
        return upstream, "PREPARATION_REQUEST_SPEC_REFERENCE_MISSING", "governing preparation-request specification is unavailable"
    markers = _marker_status(spec_text, PREPARATION_REQUEST_SPEC_MARKER_CLASSES)
    upstream["marker_validation"]["preparation_request_spec"] = markers
    if not all(markers.values()):
        _failure(checks, "preparation_request_spec_markers_present", "PREPARATION_REQUEST_SPEC_MARKER_MISSING")
        return upstream, "PREPARATION_REQUEST_SPEC_MARKER_MISSING", "governing preparation-request specification markers are incomplete"
    checks.append(_check("preparation_request_spec_markers_present", True))

    summary_text, error = _read_text(DECLARATION_TERMINAL_SUMMARY_RELATIVE_PATH)
    if error is not None or summary_text is None:
        _failure(checks, "declaration_terminal_summary_reference_exists", "DECLARATION_TERMINAL_SUMMARY_REFERENCE_MISSING")
        return upstream, "DECLARATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "declaration terminal summary is unavailable"
    markers = _marker_status(summary_text, DECLARATION_SUMMARY_MARKER_CLASSES)
    upstream["marker_validation"]["declaration_terminal_summary"] = markers
    if not all(markers.values()):
        _failure(checks, "declaration_terminal_summary_markers_present", "DECLARATION_TERMINAL_SUMMARY_MARKER_MISSING")
        return upstream, "DECLARATION_TERMINAL_SUMMARY_MARKER_MISSING", "declaration terminal summary markers are incomplete"
    checks.append(_check("declaration_terminal_summary_markers_present", True))

    artifact, error = _read_json(DECLARATION_WAITING_RESULT_RELATIVE_PATH)
    if error in ("not_a_file", "unreadable"):
        _failure(checks, "declaration_waiting_result_exists", "DECLARATION_WAITING_RESULT_REFERENCE_MISSING")
        return upstream, "DECLARATION_WAITING_RESULT_REFERENCE_MISSING", "declaration waiting result is unavailable"
    if error is not None:
        _failure(checks, "declaration_waiting_result_parseable", "DECLARATION_WAITING_RESULT_NOT_PARSEABLE")
        return upstream, "DECLARATION_WAITING_RESULT_NOT_PARSEABLE", "declaration waiting result is not parseable"
    if not isinstance(artifact, Mapping):
        _failure(checks, "declaration_waiting_result_mapping", "DECLARATION_WAITING_RESULT_NOT_MAPPING")
        return upstream, "DECLARATION_WAITING_RESULT_NOT_MAPPING", "declaration waiting result is not a mapping"
    declaration = artifact.get("receiver_side_answerable_basis_candidate_evaluation_basis_declaration")
    material = artifact.get("receiver_side_answerable_basis_candidate_evaluation_basis_declaration_material")
    declared = artifact.get("declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_basis")
    upstream_basis = artifact.get("upstream_basis")
    waiting_identity = upstream_basis.get("waiting_operation_identity") if isinstance(upstream_basis, Mapping) else None
    if not all(isinstance(value, Mapping) for value in (declaration, material, declared, waiting_identity)):
        _failure(checks, "declaration_waiting_result_shape", "DECLARATION_WAITING_RESULT_NOT_MAPPING")
        return upstream, "DECLARATION_WAITING_RESULT_NOT_MAPPING", "declaration waiting result shape is incomplete"
    required_artifact = {
        "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION_REQUIRES_DECLARATION_MATERIAL",
        "failed_check_count": 0,
    }
    for key, expected in required_artifact.items():
        if artifact.get(key) != expected:
            _failure(checks, f"declaration_waiting_{key}_matches", "REQUEST_VALUE_MISMATCH")
            return upstream, "REQUEST_VALUE_MISMATCH", f"declaration waiting artifact {key} does not match"
    declaration_required = {
        "declaration_id": REQUIRED_RESPONSE_DECLARATION_ID,
        "declaration_type": REQUIRED_RESPONSE_DECLARATION_TYPE,
        "declaration_version": REQUIRED_RESPONSE_DECLARATION_VERSION,
        "declaration_scope": REQUIRED_RESPONSE_DECLARATION_SCOPE,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_result": "REQUIRES_DECLARATION_MATERIAL",
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_recorded": True,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_result_recorded": True,
        "declaration_material_supplied": False,
        "declaration_material_received": False,
        "declaration_material_recorded": False,
        "evaluation_basis_declaration_complete": False,
        "evaluation_basis_declaration_ready_for_supply": False,
        "evaluation_basis_declaration_separately_supplied": False,
        "evaluation_basis_declaration_admitted_by_operation": False,
        "dimension_record_count": 0,
    }
    for key, expected in declaration_required.items():
        if declaration.get(key) != expected:
            _failure(checks, f"declaration_waiting_{key}_matches", "REQUEST_VALUE_MISMATCH")
            return upstream, "REQUEST_VALUE_MISMATCH", f"declaration waiting posture {key} does not match"
    if material.get("dimension_record_ids") != []:
        _failure(checks, "declaration_waiting_dimension_record_ids_empty", "REQUEST_VALUE_MISMATCH")
        return upstream, "REQUEST_VALUE_MISMATCH", "declaration waiting dimension records are not empty"
    for key in (
        "evaluation_basis_declaration_resolver_generated",
        "evaluation_basis_declaration_candidate_material_reused_as_basis",
        "evaluation_basis_declaration_repository_access_treated_as_basis",
        "candidate_evaluation_authorized",
        "candidate_evaluation_completed",
        "candidate_sufficiency_created",
        "receiver_attestation_created",
        "receiver_attestation_supported",
        "receiver_answerable_receipt_present",
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
        "second_candidate_basis_created",
        "repeated_supply_permission_created",
        "reusable_basis_route_created",
        "follow_on_work_authorized",
    ):
        if declaration.get(key) is not False:
            _failure(checks, f"declaration_waiting_{key}_false", "REQUEST_VALUE_MISMATCH")
            return upstream, "REQUEST_VALUE_MISMATCH", f"declaration waiting posture {key} is not false"
    identity_required = {
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "selected_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_id": REQUIRED_RESPONSE_DECLARATION_ID,
    }
    if any(declared.get(key) != expected for key, expected in identity_required.items()):
        _failure(checks, "declaration_waiting_selected_identities_match", "REQUEST_VALUE_MISMATCH")
        return upstream, "REQUEST_VALUE_MISMATCH", "declaration waiting selected identities do not match"
    upstream["declaration_waiting_identity"] = {
        "request_response_declaration_id": REQUIRED_RESPONSE_DECLARATION_ID,
        "candidate_id": CANDIDATE_ID,
        "candidate_type": CANDIDATE_TYPE,
        "candidate_scope": CANDIDATE_SCOPE,
        "reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
    }
    checks.append(_check("declaration_waiting_upstream_posture_valid", True))
    return upstream, None, None


def _material_preclaim_code(material: Mapping[str, Any]) -> str | None:
    for key in RESULT_PRECLAIM_FIELDS:
        if key in material:
            return "PREPARATION_REQUEST_RESULT_PRECLAIMED"
    prohibited_by_name = {
        "request_live_issuance": "PROHIBITED_LIVE_ISSUANCE_DELIVERY_RECEPTION_OR_ACCEPTANCE_REQUESTED",
        "request_delivery": "PROHIBITED_LIVE_ISSUANCE_DELIVERY_RECEPTION_OR_ACCEPTANCE_REQUESTED",
        "request_preparer_reception": "PROHIBITED_LIVE_ISSUANCE_DELIVERY_RECEPTION_OR_ACCEPTANCE_REQUESTED",
        "request_preparer_acceptance": "PROHIBITED_LIVE_ISSUANCE_DELIVERY_RECEPTION_OR_ACCEPTANCE_REQUESTED",
        "request_candidate_evaluation": "PROHIBITED_EVALUATION_BASIS_DIMENSION_RESULT_OR_CANDIDATE_RESULT_REQUESTED",
        "request_candidate_sufficiency": "PROHIBITED_EVALUATION_BASIS_DIMENSION_RESULT_OR_CANDIDATE_RESULT_REQUESTED",
    }
    for key, code in prohibited_by_name.items():
        if material.get(key) is True:
            return code
    return None


def _validate_material(
    material: Any,
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, bool, list[str]]:
    missing: list[str] = []
    if material is None:
        return None, None, False, ["preparation_request_material"]
    if not isinstance(material, Mapping):
        _failure(checks, "preparation_request_material_is_mapping", "PREPARATION_REQUEST_MATERIAL_NOT_MAPPING")
        return "PREPARATION_REQUEST_MATERIAL_NOT_MAPPING", "preparation request material is not a mapping", False, missing
    size = _serialized_size(material)
    if size is None or size > MAX_SERIALIZED_PREPARATION_REQUEST_MATERIAL_SIZE:
        _failure(checks, "preparation_request_material_within_size", "PREPARATION_REQUEST_MATERIAL_OVERSIZED")
        return "PREPARATION_REQUEST_MATERIAL_OVERSIZED", "preparation request material exceeds bounded size", False, missing
    preclaim = _material_preclaim_code(material)
    if preclaim is not None:
        _failure(checks, "preparation_request_material_has_no_preclaims", preclaim)
        return preclaim, "preparation request material contains a prohibited result posture", False, missing
    unknown = set(material) - ALLOWED_PREPARATION_REQUEST_MATERIAL_KEYS
    if unknown:
        _failure(checks, "preparation_request_material_has_no_unknown_fields", "PREPARATION_REQUEST_TOP_LEVEL_FIELD_UNKNOWN")
        return "PREPARATION_REQUEST_TOP_LEVEL_FIELD_UNKNOWN", "preparation request material contains unknown fields", False, missing
    absent = REQUIRED_PREPARATION_REQUEST_MATERIAL_KEYS - set(material)
    if absent:
        missing.extend(f"preparation_request_field:{key}" for key in sorted(absent))
        return None, None, False, missing
    expected = _expected_request_values()
    if any(material.get(key) != value for key, value in expected.items()):
        _failure(checks, "preparation_request_selected_identities_match", "PREPARATION_REQUEST_SELECTED_IDENTITY_MISMATCH")
        return "PREPARATION_REQUEST_SELECTED_IDENTITY_MISMATCH", "preparation request identities do not match the selected line", False, missing
    text_fields = (
        ("intended_preparer_reference", MAX_INTENDED_PREPARER_REFERENCE_LENGTH),
        ("intended_preparer_role_declaration", MAX_INTENDED_PREPARER_ROLE_DECLARATION_LENGTH),
        ("intended_preparer_relation_to_candidate_declaration", MAX_INTENDED_PREPARER_CANDIDATE_RELATION_DECLARATION_LENGTH),
        ("intended_preparer_relation_to_source_body_declaration", MAX_INTENDED_PREPARER_SOURCE_BODY_RELATION_DECLARATION_LENGTH),
        ("intended_preparer_custody_posture_declaration", MAX_INTENDED_PREPARER_CUSTODY_POSTURE_DECLARATION_LENGTH),
        ("request_origin_reference", MAX_REQUEST_ORIGIN_REFERENCE_LENGTH),
        ("request_timestamp", MAX_REQUEST_TIMESTAMP_LENGTH),
        ("required_response_declaration_reference", MAX_REQUIRED_RESPONSE_DECLARATION_REFERENCE_LENGTH),
    )
    for key, maximum in text_fields:
        value = material.get(key)
        if _string_within(value, maximum):
            continue
        if value is None or value == "":
            missing.append(f"preparation_request_field:{key}")
            continue
        _failure(checks, f"{key}_bounded", "PREPARATION_REQUEST_FIELD_MALFORMED")
        return "PREPARATION_REQUEST_FIELD_MALFORMED", f"{key} is malformed", False, missing
    if missing:
        return None, None, False, missing
    dimensions = material.get("required_response_dimension_ids")
    if not isinstance(dimensions, Sequence) or isinstance(dimensions, (str, bytes)):
        _failure(checks, "required_response_dimension_ids_sequence", "PREPARATION_REQUEST_RESPONSE_DIMENSION_SCOPE_MISMATCH")
        return "PREPARATION_REQUEST_RESPONSE_DIMENSION_SCOPE_MISMATCH", "required response dimensions are not an ordered sequence", False, missing
    if tuple(dimensions) != REQUIRED_RESPONSE_DIMENSION_IDS or len(dimensions) != MAX_REQUIRED_RESPONSE_DIMENSIONS:
        _failure(checks, "required_response_dimension_ids_exact", "PREPARATION_REQUEST_RESPONSE_DIMENSION_SCOPE_MISMATCH")
        return "PREPARATION_REQUEST_RESPONSE_DIMENSION_SCOPE_MISMATCH", "required response dimensions do not match the exact scope", False, missing
    for key, maximum in (
        ("response_shape_requirements", MAX_SERIALIZED_RESPONSE_SHAPE_REQUIREMENTS_SIZE),
        ("request_statement", MAX_SERIALIZED_REQUEST_STATEMENT_SIZE),
        ("request_non_meaning", MAX_SERIALIZED_REQUEST_NON_MEANING_SIZE),
    ):
        value = material.get(key)
        size = _serialized_size(value)
        if not isinstance(value, Mapping) or size is None or size > maximum:
            _failure(checks, f"{key}_bounded_mapping", "PREPARATION_REQUEST_FIELD_MALFORMED")
            return "PREPARATION_REQUEST_FIELD_MALFORMED", f"{key} is malformed", False, missing
    if not _all_false_mapping(material.get("request_non_claims"), REQUEST_REQUIRED_FALSE_NON_CLAIMS):
        _failure(checks, "request_non_claims_canonical_false", "PREPARATION_REQUEST_NON_CLAIM_MISSING_OR_FLIPPED")
        return "PREPARATION_REQUEST_NON_CLAIM_MISSING_OR_FLIPPED", "request non-claims are missing or flipped", False, missing
    if material.get("response_optional") is not True:
        _failure(checks, "response_optional_true", "PREPARATION_REQUEST_RESPONSE_NOT_OPTIONAL")
        return "PREPARATION_REQUEST_RESPONSE_NOT_OPTIONAL", "response_optional must be true", False, missing
    if material.get("preparation_request_single_use") is not True:
        _failure(checks, "preparation_request_single_use_true", "PREPARATION_REQUEST_NOT_SINGLE_USE")
        return "PREPARATION_REQUEST_NOT_SINGLE_USE", "preparation_request_single_use must be true", False, missing
    checks.append(_check("preparation_request_material_structurally_complete", True))
    return None, None, True, missing


def build_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_request(
    *,
    intent: str = INTENT_RECORD,
    preparation_request_material_supplied: bool | None = None,
    preparation_request_material: Mapping[str, Any] | None = None,
    declared_non_claims: Mapping[str, Any] | None = None,
    intended_preparer_reference: str | None = None,
    intended_preparer_role_declaration: str | None = None,
    intended_preparer_relation_to_candidate_declaration: str | None = None,
    intended_preparer_relation_to_source_body_declaration: str | None = None,
    intended_preparer_custody_posture_declaration: str | None = None,
    request_origin_reference: str | None = None,
    request_timestamp: str | None = None,
    required_response_declaration_reference: str | None = None,
    response_shape_requirements: Mapping[str, Any] | None = None,
    required_response_dimension_ids: Sequence[str] | None = None,
    request_statement: Mapping[str, Any] | None = None,
    request_non_meaning: Mapping[str, Any] | None = None,
    request_non_claims: Mapping[str, Any] | None = None,
    response_optional: bool | None = None,
    preparation_request_single_use: bool | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a bounded request without fabricating preparation-request material."""
    direct_material_supplied = any(
        value is not None
        for value in (
            intended_preparer_reference,
            intended_preparer_role_declaration,
            intended_preparer_relation_to_candidate_declaration,
            intended_preparer_relation_to_source_body_declaration,
            intended_preparer_custody_posture_declaration,
            request_origin_reference,
            request_timestamp,
            required_response_declaration_reference,
            response_shape_requirements,
            required_response_dimension_ids,
            request_statement,
            request_non_meaning,
            request_non_claims,
            response_optional,
            preparation_request_single_use,
        )
    )
    if preparation_request_material is None and direct_material_supplied:
        preparation_request_material = {
            **_expected_request_values(),
            "intended_preparer_reference": intended_preparer_reference,
            "intended_preparer_role_declaration": intended_preparer_role_declaration,
            "intended_preparer_relation_to_candidate_declaration": intended_preparer_relation_to_candidate_declaration,
            "intended_preparer_relation_to_source_body_declaration": intended_preparer_relation_to_source_body_declaration,
            "intended_preparer_custody_posture_declaration": intended_preparer_custody_posture_declaration,
            "request_origin_reference": request_origin_reference,
            "request_timestamp": request_timestamp,
            "required_response_declaration_reference": required_response_declaration_reference,
            "response_shape_requirements": copy.deepcopy(response_shape_requirements if response_shape_requirements is not None else {}),
            "required_response_dimension_ids": list(
                required_response_dimension_ids
                if required_response_dimension_ids is not None
                else REQUIRED_RESPONSE_DIMENSION_IDS
            ),
            "request_statement": copy.deepcopy(request_statement if request_statement is not None else {}),
            "request_non_meaning": copy.deepcopy(request_non_meaning if request_non_meaning is not None else {}),
            "request_non_claims": copy.deepcopy(
                request_non_claims if request_non_claims is not None else _canonical_request_non_claims()
            ),
            "response_optional": True if response_optional is None else response_optional,
            "preparation_request_single_use": True
            if preparation_request_single_use is None
            else preparation_request_single_use,
        }
    supplied = preparation_request_material is not None if preparation_request_material_supplied is None else preparation_request_material_supplied
    request: dict[str, Any] = {
        "intent": intent,
        "preparation_request_material_supplied": supplied,
        "preparation_request_material": copy.deepcopy(preparation_request_material),
        "declared_non_claims": copy.deepcopy(
            declared_non_claims if declared_non_claims is not None else _canonical_request_non_claims()
        ),
        **_expected_request_values(),
        **{key: False for key in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_request(
    **kwargs: Any,
) -> dict[str, Any]:
    """Compatibility alias for the bounded preparation-request request builder."""
    return build_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_request(
        **kwargs
    )


def resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min(
    declared_preparation_request_material: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate one preparation-request declaration without issuing it."""
    if declared_preparation_request_material is None:
        request: Mapping[str, Any] = build_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_request()
    elif not isinstance(declared_preparation_request_material, Mapping):
        checks = [_check("request_is_mapping", False, "REQUEST_NOT_MAPPING")]
        return _result(
            {}, OUTCOME_BLOCKED, REQUEST_RESULT_NOT_EVALUATED, checks,
            code="REQUEST_NOT_MAPPING", reason="request is not a mapping"
        )
    else:
        request = copy.deepcopy(dict(declared_preparation_request_material))
    checks: list[dict[str, Any]] = []
    code, reason = _validate_request(request, checks)
    if code is not None:
        return _result(request, OUTCOME_BLOCKED, REQUEST_RESULT_NOT_EVALUATED, checks, code=code, reason=reason)
    if request.get("intent") == INTENT_DO_NOT_RECORD:
        checks.append(_check("do_not_record_intent_honored", True))
        return _result(request, OUTCOME_NOT_RECORDED, REQUEST_RESULT_NOT_EVALUATED, checks)
    upstream, code, reason = _validate_upstream(checks)
    if code is not None:
        return _result(
            request, OUTCOME_BLOCKED, REQUEST_RESULT_NOT_EVALUATED, checks,
            upstream=upstream, code=code, reason=reason
        )
    material = request.get("preparation_request_material")
    if request.get("preparation_request_material_supplied") is False:
        checks.append(_check("preparation_request_material_absent_waiting_posture", True))
        return _result(
            request, OUTCOME_REQUIRES_REQUEST_MATERIAL, REQUEST_RESULT_REQUIRES_REQUEST_MATERIAL, checks,
            upstream=upstream, missing=["preparation_request_material"]
        )
    code, reason, complete, missing = _validate_material(material, checks)
    if code is not None:
        return _result(
            request, OUTCOME_BLOCKED, REQUEST_RESULT_NOT_EVALUATED, checks,
            upstream=upstream, material=material if isinstance(material, Mapping) else None,
            missing=missing, code=code, reason=reason
        )
    if not complete:
        checks.append(_check("preparation_request_material_incomplete_waiting_posture", True))
        return _result(
            request, OUTCOME_REQUIRES_REQUEST_MATERIAL, REQUEST_RESULT_REQUIRES_REQUEST_MATERIAL, checks,
            upstream=upstream, material=material if isinstance(material, Mapping) else None, missing=missing
        )
    checks.append(_check("preparation_request_ready_without_issuance", True))
    return _result(
        request, OUTCOME_RECORDED, REQUEST_RESULT_READY_FOR_ISSUANCE, checks,
        upstream=upstream, material=material if isinstance(material, Mapping) else None, complete=True
    )


def resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_from_path(
    declared_preparation_request_material_path: Path | str,
) -> dict[str, Any]:
    """Resolve one JSON request path without filesystem discovery."""
    value, error = _read_json(declared_preparation_request_material_path)
    if error is not None or not isinstance(value, Mapping):
        checks = [_check("request_path_is_mapping_json", False, "REQUEST_NOT_MAPPING")]
        return _result(
            {}, OUTCOME_BLOCKED, REQUEST_RESULT_NOT_EVALUATED, checks,
            code="REQUEST_NOT_MAPPING", reason="request path is missing, malformed, or not a mapping"
        )
    return resolve_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min(value)


def build_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return compact metadata without request or preparer declaration content."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError(
            "result must be a mapping"
        )
    return _summary_from_result(result)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    index = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
        index += 1


def _contains_forbidden_material(value: Any) -> bool:
    forbidden = {
        "preparation_request_material",
        "intended_preparer_reference",
        "intended_preparer_role_declaration",
        "intended_preparer_relation_to_candidate_declaration",
        "intended_preparer_relation_to_source_body_declaration",
        "intended_preparer_custody_posture_declaration",
        "request_origin_reference",
        "request_timestamp",
        "required_response_declaration_reference",
        "request_statement",
        "request_non_meaning",
        "candidate_material",
        "candidate_packet",
        "declaration_response",
    }
    if isinstance(value, Mapping):
        return any(key in forbidden or _contains_forbidden_material(nested) for key, nested in value.items())
    if isinstance(value, list):
        return any(_contains_forbidden_material(item) for item in value)
    return False


def _output_path_is_forbidden(path: Path) -> bool:
    lowered = {part.lower() for part in path.parts}
    forbidden = {
        "spec", "tests", "reference", "presence", "relation", "identity", "field", "runtime", "api",
        "public-intake", "descendant", "receiver-capture", "candidate-reception", "evaluation-operation",
        "evaluation-basis-declaration",
    }
    if lowered & forbidden:
        return True
    rendered = "/".join(part.lower() for part in path.parts)
    return any(
        marker in rendered
        for marker in (
            "receiver_side_answerable_basis_candidate_evaluation_operation",
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min",
        )
    )


def write_receiver_side_answerable_basis_candidate_evaluation_basis_preparation_request_declaration_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None,
) -> Path:
    """Write a validated preparation-request result with deterministic suffixing."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError(
            "result must be a mapping"
        )
    if result.get("resolver_module") != RESOLVER_MODULE or result.get("result_version") != RESULT_VERSION:
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError(
            "result identity does not match resolver"
        )
    if result.get("outcome") not in OUTCOME_FAMILY:
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError(
            "result outcome is unsupported"
        )
    if not _all_false_mapping(result.get("non_claims"), REQUIRED_FALSE_NON_CLAIMS):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError(
            "result non-claims are not canonical false"
        )
    if _contains_forbidden_material(result):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError(
            "result contains copied preparation-request or candidate material"
        )
    target = Path(output_path) if output_path is not None else OUTPUT_ROOT / OUTPUT_FILENAME
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError(
            "output path is forbidden"
        )
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _next_available_output_path(target)
    try:
        target.write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n", encoding="utf-8")
    except OSError as error:
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisPreparationRequestDeclarationV0MinError(
            "result write refused"
        ) from error
    return target
