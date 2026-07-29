"""Validate one bounded candidate-sufficiency basis preparation request.

This resolver records only whether preparation of the exact eight declaration
records was requested. It does not perform preparation, create records, admit
basis, execute the candidate-sufficiency operation, or derive a result.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_"
    "preparation_request_declaration_v0_min"
)

REQUEST_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_basis_"
    "preparation_request_declaration_001"
)
REQUEST_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "PREPARATION_REQUEST_DECLARATION"
)
REQUEST_VERSION = "0.1.0"
REQUEST_SCOPE = (
    "REQUEST_PREPARATION_OF_ONE_EXACT_EIGHT_RECORD_CANDIDATE_SUFFICIENCY_"
    "BASIS_DECLARATION_ONLY"
)

SELECTED_DECLARATION_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_001"
)
SELECTED_DECLARATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_DECLARATION"
)
SELECTED_DECLARATION_VERSION = "0.1.0"
SELECTED_DECLARATION_SCOPE = (
    "DECLARE_ONE_BOUNDED_EIGHT_DIMENSION_CANDIDATE_SUFFICIENCY_BASIS_ONLY"
)
SELECTED_DECLARATION_RESULT_REQUIRED = (
    "REQUIRES_COMPLETE_CANDIDATE_SUFFICIENCY_BASIS_DECLARATION"
)

SELECTED_SUFFICIENCY_OPERATION_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001"
)
CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
SELECTED_SUFFICIENCY_BOUNDARY_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_boundary_001"
)
SELECTED_RECEPTION_OPERATION_ID = (
    "receiver_side_answerable_basis_reception_operation_001"
)
SELECTED_EVALUATION_BOUNDARY_ID = (
    "receiver_side_answerable_basis_candidate_evaluation_boundary_001"
)
SELECTED_EVALUATION_OPERATION_ID = (
    "receiver_side_answerable_basis_candidate_evaluation_operation_001"
)

PREPARER_REFERENCE = "marko_markota__source_body_human_governor"
PREPARER_RELATION_TO_SOURCE_BODY = "SOURCE_BODY_ORIGINATING_PREPARER"

REQUESTED_PREPARATION_DIMENSION_IDS = (
    "receiver_answerability_fit",
    "selected_purpose_adequacy",
    "bounded_material_completeness",
    "unresolved_contradiction_posture",
    "unsupported_assumption_dependency",
    "scope_constrained_usability",
    "refusal_withholding_compatibility",
    "provenance_capture_limitation_posture",
)

OUTCOME_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "PREPARATION_REQUEST_DECLARATION_RECORDED"
)
OUTCOME_REQUIRES_COMPLETE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "PREPARATION_REQUEST_DECLARATION_REQUIRES_COMPLETE_DECLARATION"
)
OUTCOME_BLOCKED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "PREPARATION_REQUEST_DECLARATION_BLOCKED"
)
OUTCOME_NOT_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "PREPARATION_REQUEST_DECLARATION_NOT_RECORDED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_REQUIRES_COMPLETE,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

REQUEST_RESULT_RECORDED = (
    "CANDIDATE_SUFFICIENCY_BASIS_PREPARATION_REQUEST_DECLARATION_RECORDED"
)
REQUEST_RESULT_REQUIRES_COMPLETE = (
    "REQUIRES_COMPLETE_CANDIDATE_SUFFICIENCY_BASIS_"
    "PREPARATION_REQUEST_DECLARATION"
)
REQUEST_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
REQUEST_RESULT_FAMILY = (
    REQUEST_RESULT_RECORDED,
    REQUEST_RESULT_REQUIRES_COMPLETE,
    REQUEST_RESULT_NOT_EVALUATED,
)

INTENT_RECORD = (
    "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "PREPARATION_REQUEST_DECLARATION"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_"
    "BASIS_PREPARATION_REQUEST_DECLARATION"
)
INTENT_BLOCK = (
    "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "PREPARATION_REQUEST_DECLARATION"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
PREPARATION_REQUEST_SPEC_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "PREPARATION_REQUEST_DECLARATION_V0_MIN_SPEC.md"
)
SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_"
    "candidate_sufficiency_basis_declaration_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_"
    "v0_min_result.json"
)
GOVERNING_PREPARATION_REQUEST_SPEC_RELATIVE_PATH = (
    PREPARATION_REQUEST_SPEC_RELATIVE_PATH
)
SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_PATH = (
    SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_RELATIVE_PATH
)
OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_"
    "candidate_sufficiency_basis_preparation_request_declaration_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_candidate_sufficiency_basis_"
    "preparation_request_declaration_001__receiver_side_answerable_basis_"
    "candidate_sufficiency_basis_preparation_request_declaration_v0_min_result.json"
)

MAX_SERIALIZED_REQUEST_SIZE = 131_072
MAX_MAPPING_ITEMS = 128
MAX_SEQUENCE_ITEMS = 64
MAX_NESTING_DEPTH = 8
MAX_TEXT_LENGTH = 2_048
MAX_PREPARER_POSTURE_ITEMS = 9
MAX_SERIALIZED_PREPARATION_REQUEST_MATERIAL_SIZE = MAX_SERIALIZED_REQUEST_SIZE
MAX_PREPARER_REFERENCE_LENGTH = 256
MAX_PREPARER_RELATION_LENGTH = 256
MAX_REQUESTED_PREPARATION_DIMENSIONS = len(REQUESTED_PREPARATION_DIMENSION_IDS)


class ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
    Exception
):
    """Raised when a result cannot be written under this resolver contract."""


REQUIRED_FALSE_NON_CLAIMS = (
    "preparation_started",
    "preparation_completed",
    "declaration_records_created",
    "declaration_ready_for_supply",
    "basis_separately_supplied",
    "basis_admitted_by_operation",
    "operation_executed",
    "operation_exhausted",
    "caller_supplied_dimension_result",
    "caller_supplied_candidate_result",
    "receiver_side_answerable_basis_candidate_sufficient",
    "receiver_side_answerable_basis_candidate_insufficient",
    "receiver_side_answerable_basis_candidate_indeterminate",
    "candidate_sufficiency_decided",
    "candidate_sufficiency_established",
    "candidate_insufficiency_established",
    "candidate_indeterminacy_established",
    "dimension_results_derived",
    "candidate_result_derived",
    "receiver_attestation_created",
    "receiver_answerable_receipt_present",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "identity_created",
    "relation_created",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_intake_created",
    "authority_created",
    "standing_created",
    "truth_created",
    "output_authorized",
    "action_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "source_body_preparer_to_independent_custody",
    "preparer_reference_to_authority",
    "preparer_reference_to_identity",
    "preparer_reference_to_standing",
    "preparer_reference_to_truth",
    "request_recorded_to_preparation_completed",
    "request_recorded_to_declaration_readiness",
    "request_recorded_to_operation_authorization",
    "preparation_request_debt_created",
    "preparation_request_obligation_created",
    "repeated_preparation_request_permission_created",
    "reusable_preparation_request_route_created",
    "automatic_preparation_request_created",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)
REQUEST_REQUIRED_FALSE_NON_CLAIMS = REQUIRED_FALSE_NON_CLAIMS

PROHIBITED_REQUEST_FLAGS = {
    "request_preparation_started": "PROHIBITED_PREPARATION_PERFORMANCE_REQUESTED",
    "request_preparation_completed": "PROHIBITED_PREPARATION_PERFORMANCE_REQUESTED",
    "request_declaration_records_creation": (
        "PROHIBITED_PREPARATION_PERFORMANCE_REQUESTED"
    ),
    "request_declaration_readiness": (
        "PROHIBITED_READINESS_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED"
    ),
    "request_basis_separate_supply": (
        "PROHIBITED_READINESS_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED"
    ),
    "request_basis_operation_admission": (
        "PROHIBITED_READINESS_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED"
    ),
    "request_operation_execution": (
        "PROHIBITED_READINESS_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED"
    ),
    "request_operation_exhaustion": (
        "PROHIBITED_READINESS_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED"
    ),
    "request_dimension_result": (
        "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED"
    ),
    "request_candidate_sufficient": (
        "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED"
    ),
    "request_candidate_insufficient": (
        "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED"
    ),
    "request_candidate_indeterminate": (
        "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED"
    ),
    "request_receiver_attestation_creation": (
        "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
    ),
    "request_receiver_answerable_receipt_creation": (
        "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
    ),
    "request_presence_support": "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED",
    "request_presence_authorization": (
        "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
    ),
    "request_presence_establishment": (
        "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
    ),
    "request_presence_recording": (
        "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED"
    ),
    "request_identity_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
    "request_relation_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
    "request_coupling_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
    "request_runtime_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
    "request_api_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
    "request_authority_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
    "request_standing_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
    "request_truth_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
    "request_output_authorization": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
    "request_action_authorization": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
    "request_synchronization_authorization": (
        "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
    ),
    "request_follow_on_authorization": (
        "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
    ),
    "request_follow_on_work_authorization": (
        "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
    ),
    "request_preparation_request_debt_creation": (
        "PROHIBITED_DEBT_OBLIGATION_REPEATED_REUSABLE_OR_AUTOMATIC_REQUESTED"
    ),
    "request_preparation_request_obligation_creation": (
        "PROHIBITED_DEBT_OBLIGATION_REPEATED_REUSABLE_OR_AUTOMATIC_REQUESTED"
    ),
    "request_repeated_preparation_request_permission_creation": (
        "PROHIBITED_DEBT_OBLIGATION_REPEATED_REUSABLE_OR_AUTOMATIC_REQUESTED"
    ),
    "request_reusable_preparation_request_route_creation": (
        "PROHIBITED_DEBT_OBLIGATION_REPEATED_REUSABLE_OR_AUTOMATIC_REQUESTED"
    ),
    "request_automatic_preparation_request_creation": (
        "PROHIBITED_DEBT_OBLIGATION_REPEATED_REUSABLE_OR_AUTOMATIC_REQUESTED"
    ),
    "request_repository_scan": (
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
    ),
    "request_file_discovery": (
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
    ),
    "request_affected_file_repair": (
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
    ),
    "request_affected_file_mutation": (
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
    ),
    "request_prior_unsupported_claim_validation": (
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
    ),
    "request_validation_enforcement": (
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
    ),
}

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "UNSUPPORTED_INTENT",
        "PREPARATION_REQUEST_SPEC_REFERENCE_MISSING",
        "PREPARATION_REQUEST_SPEC_MARKER_MISSING",
        "SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_REFERENCE_MISSING",
        "SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_NOT_PARSEABLE",
        "SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_NOT_MAPPING",
        "REQUEST_VALUE_MISMATCH",
        "SELECTED_REQUEST_IDENTITY_MISMATCH",
        "SELECTED_DECLARATION_IDENTITY_MISMATCH",
        "SELECTED_OPERATION_IDENTITY_MISMATCH",
        "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
        "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
        "UPSTREAM_DECLARATION_NOT_INCOMPLETE",
        "UPSTREAM_DECLARATION_RESULT_MISMATCH",
        "UPSTREAM_DECLARATION_FAILED_CHECKS_PRESENT",
        "UPSTREAM_WAITING_OPERATION_NOT_VALIDATED",
        "UPSTREAM_DECLARATION_RECORDS_ALREADY_SUPPLIED",
        "UPSTREAM_DECLARATION_ALREADY_COMPLETE_OR_READY",
        "UPSTREAM_DECLARATION_ALREADY_RECORDED",
        "UPSTREAM_DECLARATION_RESULT_ALREADY_RECORDED",
        "UPSTREAM_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
        "UPSTREAM_OPERATION_ALREADY_EXECUTED_OR_EXHAUSTED",
        "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
        "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
        "UPSTREAM_ROUTE_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
        "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
        "REQUESTED_DIMENSION_SET_MISMATCH",
        "PREPARER_POSTURE_NOT_MAPPING",
        "PREPARER_REFERENCE_INVALID",
        "PREPARER_RELATION_INVALID",
        "PREPARER_POSTURE_INVALID",
        "FALSE_INDEPENDENT_PREPARER_CLAIM",
        "FALSE_SEPARATE_CUSTODY_CLAIM",
        "REQUEST_PAYLOAD_CONTAINS_DECLARATION_OR_BASIS_MATERIAL",
        "PREPARATION_PERFORMANCE_PRECLAIMED",
        "DECLARATION_READINESS_PRECLAIMED",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "PROHIBITED_PREPARATION_PERFORMANCE_REQUESTED",
        "PROHIBITED_READINESS_SUPPLY_ADMISSION_EXECUTION_OR_EXHAUSTION_REQUESTED",
        "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED",
        "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED",
        "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "PROHIBITED_DEBT_OBLIGATION_REPEATED_REUSABLE_OR_AUTOMATIC_REQUESTED",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "EXPLICIT_BLOCK_REQUESTED",
        "WRITE_REFUSED",
        "REQUEST_OVERSIZED",
        "REQUEST_NESTING_EXCEEDED",
        "REQUEST_FIELD_UNKNOWN",
    }
)

PREPARATION_REQUEST_SPEC_MARKER_CLASSES = {
    "title": (
        "# Receiver-Side Answerable Basis Candidate Sufficiency Basis "
        "Preparation Request Declaration V0 Minimum Specification",
    ),
    "request_identity": (REQUEST_ID, REQUEST_TYPE, REQUEST_SCOPE),
    "selected_declaration_identity": (
        SELECTED_DECLARATION_ID,
        SELECTED_DECLARATION_TYPE,
        SELECTED_DECLARATION_SCOPE,
        SELECTED_DECLARATION_RESULT_REQUIRED,
    ),
    "dimension_set": REQUESTED_PREPARATION_DIMENSION_IDS,
    "preparer_posture": (
        PREPARER_REFERENCE,
        PREPARER_RELATION_TO_SOURCE_BODY,
        "source_body_preparer = true",
        "independent_preparer_claimed = false",
        "separate_custody_claimed_by_preparer = false",
    ),
    "result_family": (
        REQUEST_RESULT_RECORDED,
        REQUEST_RESULT_REQUIRES_COMPLETE,
        REQUEST_RESULT_NOT_EVALUATED,
    ),
    "outcome_family": OUTCOME_FAMILY,
    "separation": (
        "Request is not preparation.",
        "Preparation requested is not preparation completed.",
        "Request recorded is not declaration readiness or operation authorization.",
    ),
}

PREPARER_POSTURE_KEYS = frozenset(
    {
        "preparer_reference",
        "preparer_relation_to_source_body",
        "source_body_preparer",
        "independent_preparer_claimed",
        "separate_custody_claimed_by_preparer",
        "preparer_authority_claimed",
        "preparer_identity_established",
        "preparer_standing_claimed",
        "preparer_truth_claimed",
    }
)

RESULT_PRECLAIM_FIELDS = frozenset(
    {
        "outcome",
        "request_result",
        "preparation_request_recorded",
        "preparation_request_result_recorded",
        "preparation_request_complete",
        "preparation_requested",
        "preparation_started",
        "preparation_completed",
        "declaration_records_created",
        "declaration_ready_for_supply",
        "basis_separately_supplied",
        "basis_admitted_by_operation",
        "operation_executed",
        "operation_exhausted",
        "dimension_result",
        "dimension_results",
        "candidate_result",
        "candidate_sufficiency_basis_preparation_request_declaration_recorded",
        "candidate_sufficiency_basis_preparation_request_declaration_result_recorded",
        "candidate_sufficiency_basis_preparation_request_declaration_result",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_recorded",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_result_recorded",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_result",
        "candidate_sufficiency_basis_preparation_requested",
        "candidate_sufficiency_basis_preparation_started",
        "candidate_sufficiency_basis_preparation_completed",
        "candidate_sufficiency_basis_declaration_records_created",
        "candidate_sufficiency_basis_declaration_ready_for_supply",
        "candidate_sufficiency_basis_separately_supplied",
        "candidate_sufficiency_basis_admitted_by_operation",
        "candidate_sufficiency_operation_executed",
        "candidate_sufficiency_operation_exhausted",
        *REQUIRED_FALSE_NON_CLAIMS,
    }
)

FORBIDDEN_PAYLOAD_KEYS = frozenset(
    {
        "declaration_record",
        "declaration_records",
        "candidate_sufficiency_basis_declaration_records",
        "basis_item",
        "basis_items",
        "basis_reference",
        "basis_references",
        "declarant_reference",
        "evaluator_reference",
        "rule_input",
        "rule_inputs",
        "rule_input_postures",
        "support_postures",
        "contradiction_postures",
        "unresolved_postures",
        "dimension_result",
        "dimension_results",
        "candidate_result",
        "candidate_material",
        "candidate_packet",
        "capture_material",
        "capture_packet",
        "complete_upstream_artifact",
        "upstream_artifact",
        "upstream_checks",
    }
)

INCOMPLETE_WHAT_REMAINS_OPEN = (
    "complete preparation-request declaration",
    "preparation-request declaration live standing",
    "source-body preparation of the eight declaration records, if separately performed",
    "declaration resolver execution against prepared records",
    "declaration readiness",
    "separate operation-request supply of the prepared basis",
    "actual candidate-sufficiency evaluation",
    "candidate-sufficiency result",
    "receiver-attestation boundary, only after candidate sufficient",
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
RECORDED_WHAT_REMAINS_OPEN = INCOMPLETE_WHAT_REMAINS_OPEN[2:]

PERMITTED_FUTURE_ROUTE = (
    "One preparation-request resolver may later validate this request.",
    "If recorded, source-body preparation of the eight records may be separately performed.",
    "Prepared records must later be supplied to the declaration resolver for readiness validation.",
    "A ready declaration must later be separately supplied through one operation request.",
    "Only the operation resolver may admit basis and derive dimension and candidate results.",
    "No request or preparation step preselects any dimension or candidate result.",
)

BLOCKED_ROUTES = (
    "preparation request directly to preparation performance or declaration records",
    "preparation request directly to declaration readiness, basis supply, or admission",
    "preparation request directly to operation execution or exhaustion",
    "preparation request directly to dimension or candidate result",
    "source-body preparer directly to independent custody",
    "preparer reference directly to authority, identity, standing, or truth",
    "request existence directly to debt or obligation",
    "one request to repeated permission, reusable route, or automatic request",
    "changed files or newly noticed evidence to automatic preparation request",
    "preparation request to contaminated-lineage validation",
)

RESULT_SECTIONS = frozenset(
    {
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_metadata",
        "declared_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_basis",
        "upstream_basis",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_checks",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_statement",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_non_meaning",
        "request_result_detail",
        "permitted_future_route",
        "blocked_routes",
        "what_remains_open",
        "non_claims",
        "outcome",
        "block",
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_summary",
        "resolver_module",
        "result_version",
        "failed_check_count",
        "passed_check_count",
    }
)


def _exact_bool(value: Any) -> bool:
    return value is True or value is False


def _serialized_size(value: Any) -> int | None:
    try:
        serialized = json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=True,
            allow_nan=False,
        )
    except (TypeError, ValueError):
        return None
    return len(serialized.encode("utf-8"))


def _bounded_json(value: Any, depth: int = 0) -> bool:
    if depth > MAX_NESTING_DEPTH:
        return False
    if value is None or isinstance(value, (bool, int, float)):
        return not isinstance(value, float) or (
            value == value and value not in (float("inf"), float("-inf"))
        )
    if isinstance(value, str):
        return len(value) <= MAX_TEXT_LENGTH
    if isinstance(value, Mapping):
        return len(value) <= MAX_MAPPING_ITEMS and all(
            isinstance(key, str)
            and len(key) <= MAX_TEXT_LENGTH
            and _bounded_json(nested, depth + 1)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return len(value) <= MAX_SEQUENCE_ITEMS and all(
            _bounded_json(item, depth + 1) for item in value
        )
    return False


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


def _failure(
    checks: list[dict[str, Any]],
    name: str,
    code: str,
) -> tuple[str, str]:
    checks.append(_check(name, False, code))
    return code, name.replace("_", " ")


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _all_false_mapping(value: Any, keys: Sequence[str]) -> bool:
    return (
        isinstance(value, Mapping)
        and set(keys).issubset(value)
        and all(value.get(key) is False for key in keys)
    )


def _marker_status(
    text: str,
    marker_classes: Mapping[str, Sequence[str]],
) -> dict[str, bool]:
    return {
        name: all(marker in text for marker in markers)
        for name, markers in marker_classes.items()
    }


def _expected_request_values() -> dict[str, Any]:
    return {
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_id": REQUEST_ID,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_type": REQUEST_TYPE,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_version": REQUEST_VERSION,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_scope": REQUEST_SCOPE,
        "selected_candidate_sufficiency_basis_declaration_id": SELECTED_DECLARATION_ID,
        "selected_candidate_sufficiency_basis_declaration_type": SELECTED_DECLARATION_TYPE,
        "selected_candidate_sufficiency_basis_declaration_version": SELECTED_DECLARATION_VERSION,
        "selected_candidate_sufficiency_basis_declaration_scope": SELECTED_DECLARATION_SCOPE,
        "selected_candidate_sufficiency_basis_declaration_result_required": SELECTED_DECLARATION_RESULT_REQUIRED,
        "selected_candidate_sufficiency_operation_id": SELECTED_SUFFICIENCY_OPERATION_ID,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "selected_candidate_sufficiency_boundary_id": SELECTED_SUFFICIENCY_BOUNDARY_ID,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "selected_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "governing_preparation_request_specification_path": _display_path(
            PREPARATION_REQUEST_SPEC_RELATIVE_PATH
        ),
        "selected_incomplete_declaration_artifact_path": _display_path(
            SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_RELATIVE_PATH
        ),
    }


def _request_allowed_keys() -> frozenset[str]:
    return frozenset(
        {
            "intent",
            "preparation_request_material_supplied",
            "requested_dimension_ids",
            "preparer_posture",
            "declared_non_claims",
            *tuple(_expected_request_values()),
            *tuple(PROHIBITED_REQUEST_FLAGS),
        }
    )


def _identity_code(key: str) -> str:
    if "preparation_request_declaration_" in key:
        return "SELECTED_REQUEST_IDENTITY_MISMATCH"
    if "selected_candidate_sufficiency_basis_declaration_" in key:
        return "SELECTED_DECLARATION_IDENTITY_MISMATCH"
    if key == "receiver_side_answerable_basis_candidate_id":
        return "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
    if "boundary_id" in key:
        return "SELECTED_BOUNDARY_IDENTITY_MISMATCH"
    if "operation_id" in key:
        return "SELECTED_OPERATION_IDENTITY_MISMATCH"
    return "REQUEST_VALUE_MISMATCH"


def _contains_key(value: Any, keys: frozenset[str]) -> bool:
    if isinstance(value, Mapping):
        return any(
            key in keys or _contains_key(nested, keys)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_key(item, keys) for item in value)
    return False


def _complete_preparer_posture() -> dict[str, Any]:
    return {
        "preparer_reference": PREPARER_REFERENCE,
        "preparer_relation_to_source_body": PREPARER_RELATION_TO_SOURCE_BODY,
        "source_body_preparer": True,
        "independent_preparer_claimed": False,
        "separate_custody_claimed_by_preparer": False,
        "preparer_authority_claimed": False,
        "preparer_identity_established": False,
        "preparer_standing_claimed": False,
        "preparer_truth_claimed": False,
    }


def _safe_preparer_posture(
    posture: Mapping[str, Any] | None,
    complete: bool,
) -> dict[str, Any]:
    if not complete or not isinstance(posture, Mapping):
        return {
            "preparer_reference": None,
            "preparer_relation_to_source_body": None,
            "source_body_preparer": False,
            "independent_preparer_claimed": False,
            "separate_custody_claimed_by_preparer": False,
            "preparer_authority_claimed": False,
            "preparer_identity_established": False,
            "preparer_standing_claimed": False,
            "preparer_truth_claimed": False,
        }
    return copy.deepcopy(_complete_preparer_posture())


def _request_state(
    outcome: str,
    request_result: str,
    *,
    material_supplied: bool,
    complete: bool,
    upstream_validated: bool,
    preparer_posture: Mapping[str, Any] | None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED and complete
    state: dict[str, Any] = {
        "request_id": REQUEST_ID,
        "request_type": REQUEST_TYPE,
        "request_version": REQUEST_VERSION,
        "request_scope": REQUEST_SCOPE,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_id": REQUEST_ID,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_type": REQUEST_TYPE,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_version": REQUEST_VERSION,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_scope": REQUEST_SCOPE,
        "request_result": request_result,
        "selected_candidate_sufficiency_basis_declaration_id": SELECTED_DECLARATION_ID,
        "selected_candidate_sufficiency_operation_id": SELECTED_SUFFICIENCY_OPERATION_ID,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "selected_candidate_sufficiency_boundary_id": SELECTED_SUFFICIENCY_BOUNDARY_ID,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "selected_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "upstream_incomplete_declaration_validated": upstream_validated,
        "preparation_request_material_supplied": material_supplied,
        "preparation_request_complete": recorded,
        "requested_dimension_ids": (
            list(REQUESTED_PREPARATION_DIMENSION_IDS) if recorded else []
        ),
        "requested_dimension_count": (
            len(REQUESTED_PREPARATION_DIMENSION_IDS) if recorded else 0
        ),
        **_safe_preparer_posture(preparer_posture, recorded),
        "candidate_sufficiency_basis_preparation_request_declaration_recorded": recorded,
        "candidate_sufficiency_basis_preparation_request_declaration_result_recorded": recorded,
        "candidate_sufficiency_basis_preparation_requested": recorded,
        "candidate_sufficiency_basis_preparation_started": False,
        "candidate_sufficiency_basis_preparation_completed": False,
        "candidate_sufficiency_basis_declaration_records_created": False,
        "candidate_sufficiency_basis_declaration_ready_for_supply": False,
        "candidate_sufficiency_basis_separately_supplied": False,
        "candidate_sufficiency_basis_admitted_by_operation": False,
        "candidate_sufficiency_operation_executed": False,
        "candidate_sufficiency_operation_exhausted": False,
    }
    state.update(_canonical_non_claims())
    return state


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    name = (
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "preparation_request_declaration"
    )
    state = result.get(name)
    state = state if isinstance(state, Mapping) else {}
    upstream = result.get("upstream_basis")
    upstream = upstream if isinstance(upstream, Mapping) else {}
    return {
        "outcome": result.get("outcome"),
        "request_result": state.get("request_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "request_identity": {
            "request_id": state.get("request_id"),
            "request_type": state.get("request_type"),
            "request_version": state.get("request_version"),
            "request_scope": state.get("request_scope"),
        },
        "selected_identity": {
            "declaration_id": state.get(
                "selected_candidate_sufficiency_basis_declaration_id"
            ),
            "operation_id": state.get(
                "selected_candidate_sufficiency_operation_id"
            ),
            "candidate_id": state.get(
                "receiver_side_answerable_basis_candidate_id"
            ),
            "boundary_id": state.get(
                "selected_candidate_sufficiency_boundary_id"
            ),
        },
        "upstream_incomplete_declaration_validated": state.get(
            "upstream_incomplete_declaration_validated"
        ),
        "preparation_request_material_supplied": state.get(
            "preparation_request_material_supplied"
        ),
        "preparation_request_complete": state.get("preparation_request_complete"),
        "requested_dimension_count": state.get("requested_dimension_count"),
        "requested_dimension_ids": copy.deepcopy(
            state.get("requested_dimension_ids", [])
        ),
        "preparer_posture": {
            key: state.get(key) for key in sorted(PREPARER_POSTURE_KEYS)
        },
        "request_recorded": state.get(
            "candidate_sufficiency_basis_preparation_request_declaration_recorded"
        ),
        "preparation_requested": state.get(
            "candidate_sufficiency_basis_preparation_requested"
        ),
        "preparation_and_record_creation_locks": {
            key: state.get(key)
            for key in (
                "candidate_sufficiency_basis_preparation_started",
                "candidate_sufficiency_basis_preparation_completed",
                "candidate_sufficiency_basis_declaration_records_created",
            )
        },
        "readiness_supply_admission_execution_exhaustion_locks": {
            key: state.get(key)
            for key in (
                "candidate_sufficiency_basis_declaration_ready_for_supply",
                "candidate_sufficiency_basis_separately_supplied",
                "candidate_sufficiency_basis_admitted_by_operation",
                "candidate_sufficiency_operation_executed",
                "candidate_sufficiency_operation_exhausted",
            )
        },
        "candidate_receiver_receipt_presence_route_retry_debt_obligation_and_downstream_locks_false": (
            _all_false_mapping(result.get("non_claims"), REQUIRED_FALSE_NON_CLAIMS)
        ),
        "governing_paths": copy.deepcopy(upstream.get("governing_paths", {})),
        "marker_validation": copy.deepcopy(
            upstream.get("marker_validation", {})
        ),
        "non_claims_canonical_false": _all_false_mapping(
            result.get("non_claims"), REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _bounded_declared_basis(
    request: Mapping[str, Any],
    complete: bool,
) -> dict[str, Any]:
    basis = {
        key: copy.deepcopy(request.get(key))
        for key in (
            "intent",
            "preparation_request_material_supplied",
            *tuple(_expected_request_values()),
        )
    }
    basis["requested_dimension_ids"] = (
        list(REQUESTED_PREPARATION_DIMENSION_IDS) if complete else []
    )
    basis["preparer_posture"] = _safe_preparer_posture(
        request.get("preparer_posture")
        if isinstance(request.get("preparer_posture"), Mapping)
        else None,
        complete,
    )
    basis["complete_request_payload_omitted"] = True
    return basis


def _result(
    request: Mapping[str, Any],
    outcome: str,
    request_result: str,
    checks: list[dict[str, Any]],
    *,
    upstream: Mapping[str, Any] | None = None,
    complete: bool = False,
    missing: Sequence[str] = (),
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    supplied = request.get("preparation_request_material_supplied") is True
    upstream_mapping = copy.deepcopy(dict(upstream or {}))
    upstream_validated = (
        upstream_mapping.get("selected_incomplete_declaration_validated") is True
    )
    posture = (
        request.get("preparer_posture")
        if isinstance(request.get("preparer_posture"), Mapping)
        else None
    )
    state = _request_state(
        outcome,
        request_result,
        material_supplied=supplied,
        complete=complete,
        upstream_validated=upstream_validated,
        preparer_posture=posture,
    )
    what_remains_open = (
        RECORDED_WHAT_REMAINS_OPEN
        if outcome == OUTCOME_RECORDED and complete
        else INCOMPLETE_WHAT_REMAINS_OPEN
    )
    prefix = (
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "preparation_request_declaration"
    )
    result: dict[str, Any] = {
        f"{prefix}_metadata": {
            "request_id": REQUEST_ID,
            "request_type": REQUEST_TYPE,
            "request_version": REQUEST_VERSION,
            "request_scope": REQUEST_SCOPE,
        },
        f"declared_{prefix}_basis": _bounded_declared_basis(request, complete),
        "upstream_basis": upstream_mapping,
        prefix: state,
        f"{prefix}_checks": copy.deepcopy(checks),
        f"{prefix}_statement": {
            "one_selected_incomplete_declaration_consumed_as_upstream_standing": upstream_validated,
            "incomplete_declaration_not_completed": True,
            "request_is_not_preparation": True,
            "requested_preparer_is_not_preparer_performance": True,
            "preparation_requested_is_not_preparation_completed": True,
            "request_recorded_is_not_declaration_readiness": True,
            "source_body_preparer_is_not_independent_custody": True,
            "preparer_reference_is_not_authority_identity_standing_or_truth": True,
            "request_recorded_is_not_operation_authorization": True,
            "request_existence_is_not_debt_or_obligation": True,
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
            "open_does_not_mean_next_unless_separately_selected": True,
        },
        f"{prefix}_non_meaning": {
            "preparation_request_is_not_preparation_started": True,
            "preparation_request_is_not_preparation_completed": True,
            "preparation_request_is_not_records_created": True,
            "preparation_request_is_not_declaration_ready": True,
            "preparation_request_is_not_basis_supplied": True,
            "preparation_request_is_not_basis_admitted": True,
            "preparation_request_is_not_operation_execution": True,
            "preparation_request_is_not_operation_exhaustion": True,
            "preparation_request_is_not_dimension_result": True,
            "preparation_request_is_not_candidate_result": True,
            "source_body_origin_is_not_independent_custody": True,
            "preparer_reference_is_not_authority_identity_standing_or_truth": True,
            "request_recording_is_not_debt_obligation_or_automatic_nextness": True,
        },
        "request_result_detail": {
            "request_result": request_result,
            "preparation_request_material_supplied": supplied,
            "preparation_request_complete": outcome == OUTCOME_RECORDED and complete,
            "missing_or_incomplete_request_material": list(missing),
            "request_recorded": state[
                "candidate_sufficiency_basis_preparation_request_declaration_recorded"
            ],
            "request_result_recorded": state[
                "candidate_sufficiency_basis_preparation_request_declaration_result_recorded"
            ],
            "preparation_requested": state[
                "candidate_sufficiency_basis_preparation_requested"
            ],
            "preparation_started": False,
            "preparation_completed": False,
            "declaration_records_created": False,
            "declaration_ready_for_supply": False,
            "basis_separately_supplied": False,
            "basis_admitted_by_operation": False,
            "operation_executed": False,
            "operation_exhausted": False,
            "dimension_result_exists": False,
            "candidate_result_exists": False,
        },
        "permitted_future_route": list(PERMITTED_FUTURE_ROUTE),
        "blocked_routes": list(BLOCKED_ROUTES),
        "what_remains_open": list(what_remains_open),
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
    result["failed_check_count"] = sum(
        check.get("passed") is False for check in checks
    )
    result["passed_check_count"] = sum(
        check.get("passed") is True for check in checks
    )
    result[f"{prefix}_summary"] = _summary_from_result(result)
    return result


def _preclaim_code(key: str) -> str:
    if key in {
        "preparation_started",
        "preparation_completed",
        "declaration_records_created",
        "candidate_sufficiency_basis_preparation_started",
        "candidate_sufficiency_basis_preparation_completed",
        "candidate_sufficiency_basis_declaration_records_created",
    }:
        return "PREPARATION_PERFORMANCE_PRECLAIMED"
    if key in {
        "declaration_ready_for_supply",
        "candidate_sufficiency_basis_declaration_ready_for_supply",
    }:
        return "DECLARATION_READINESS_PRECLAIMED"
    return "RESULT_POSTURE_PRECLAIMED"


def _validate_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    size = _serialized_size(request)
    if size is None or size > MAX_SERIALIZED_REQUEST_SIZE:
        return _failure(checks, "request_within_bounded_size", "REQUEST_OVERSIZED")
    if not _bounded_json(request):
        return _failure(
            checks, "request_within_bounded_nesting", "REQUEST_NESTING_EXCEEDED"
        )
    for key in RESULT_PRECLAIM_FIELDS:
        if key in request:
            return _failure(
                checks, f"request_{key}_not_preclaimed", _preclaim_code(key)
            )
    if _contains_key(request, FORBIDDEN_PAYLOAD_KEYS):
        return _failure(
            checks,
            "request_contains_no_declaration_or_basis_material",
            "REQUEST_PAYLOAD_CONTAINS_DECLARATION_OR_BASIS_MATERIAL",
        )
    unknown = set(request) - _request_allowed_keys()
    if unknown:
        return _failure(
            checks, "request_has_only_supported_fields", "REQUEST_FIELD_UNKNOWN"
        )
    intent = request.get("intent")
    if intent not in SUPPORTED_INTENTS:
        return _failure(checks, "intent_supported", "UNSUPPORTED_INTENT")
    if intent == INTENT_BLOCK:
        return _failure(
            checks, "explicit_block_not_requested", "EXPLICIT_BLOCK_REQUESTED"
        )
    for key, expected in _expected_request_values().items():
        if request.get(key) != expected:
            code = _identity_code(key)
            return _failure(checks, f"{key}_matches_selected_line", code)
    if not _exact_bool(request.get("preparation_request_material_supplied")):
        return _failure(
            checks,
            "preparation_request_material_supplied_is_boolean",
            "REQUEST_VALUE_MISMATCH",
        )
    if not _all_false_mapping(
        request.get("declared_non_claims"), REQUIRED_FALSE_NON_CLAIMS
    ):
        return _failure(
            checks,
            "declared_non_claims_are_canonical_false",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    for key, code in PROHIBITED_REQUEST_FLAGS.items():
        value = request.get(key)
        if value is True:
            return _failure(checks, f"{key}_not_requested", code)
        if value is not False:
            return _failure(checks, f"{key}_is_false", "REQUEST_VALUE_MISMATCH")
    dimensions = request.get("requested_dimension_ids")
    posture = request.get("preparer_posture")
    if request.get("preparation_request_material_supplied") is False:
        dimensions_empty = (
            isinstance(dimensions, Sequence)
            and not isinstance(dimensions, (str, bytes, bytearray))
            and len(dimensions) == 0
        )
        posture_empty = posture is None or (
            isinstance(posture, Mapping) and len(posture) == 0
        )
        if not dimensions_empty or not posture_empty:
            return _failure(
                checks,
                "absent_material_has_no_payload",
                "REQUEST_VALUE_MISMATCH",
            )
    checks.append(_check("request_shape_bounded_and_exact", True))
    return None, None


def _validate_false_keys(
    value: Mapping[str, Any],
    keys: Sequence[str],
) -> bool:
    return all(value.get(key) is False for key in keys)


def _validate_upstream(
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], str | None, str | None]:
    upstream: dict[str, Any] = {
        "governing_paths": {
            "governing_preparation_request_specification_path": _display_path(
                PREPARATION_REQUEST_SPEC_RELATIVE_PATH
            ),
            "selected_incomplete_declaration_artifact_path": _display_path(
                SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_RELATIVE_PATH
            ),
        },
        "marker_validation": {},
        "selected_incomplete_declaration_validated": False,
        "complete_upstream_artifact_omitted": True,
        "complete_upstream_checks_omitted": True,
    }
    spec_text, error = _read_text(PREPARATION_REQUEST_SPEC_RELATIVE_PATH)
    if error is not None or spec_text is None:
        code, reason = _failure(
            checks,
            "preparation_request_specification_exists",
            "PREPARATION_REQUEST_SPEC_REFERENCE_MISSING",
        )
        return upstream, code, reason
    markers = _marker_status(spec_text, PREPARATION_REQUEST_SPEC_MARKER_CLASSES)
    upstream["marker_validation"]["governing_preparation_request_specification"] = (
        markers
    )
    if not all(markers.values()):
        code, reason = _failure(
            checks,
            "preparation_request_specification_markers_present",
            "PREPARATION_REQUEST_SPEC_MARKER_MISSING",
        )
        return upstream, code, reason
    checks.append(_check("preparation_request_specification_markers_present", True))

    artifact, error = _read_json(
        SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_RELATIVE_PATH
    )
    if error in ("not_a_file", "unreadable"):
        code, reason = _failure(
            checks,
            "selected_incomplete_declaration_artifact_exists",
            "SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_REFERENCE_MISSING",
        )
        return upstream, code, reason
    if error is not None:
        code, reason = _failure(
            checks,
            "selected_incomplete_declaration_artifact_parseable",
            "SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_NOT_PARSEABLE",
        )
        return upstream, code, reason
    if not isinstance(artifact, Mapping):
        code, reason = _failure(
            checks,
            "selected_incomplete_declaration_artifact_mapping",
            "SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_NOT_MAPPING",
        )
        return upstream, code, reason
    declaration = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration"
    )
    summary = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_summary"
    )
    open_state = artifact.get("what_remains_open")
    if (
        not isinstance(declaration, Mapping)
        or not isinstance(summary, Mapping)
        or not isinstance(open_state, Sequence)
        or isinstance(open_state, (str, bytes, bytearray))
    ):
        code, reason = _failure(
            checks,
            "selected_incomplete_declaration_artifact_shape",
            "SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_NOT_MAPPING",
        )
        return upstream, code, reason
    if (
        artifact.get("resolver_module")
        != "resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min"
        or artifact.get("result_version") != RESULT_VERSION
        or artifact.get("outcome")
        != (
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
            "DECLARATION_REQUIRES_COMPLETE_DECLARATION"
        )
    ):
        code, reason = _failure(
            checks,
            "upstream_declaration_is_exact_incomplete_result",
            "UPSTREAM_DECLARATION_NOT_INCOMPLETE",
        )
        return upstream, code, reason
    if artifact.get("failed_check_count") != 0:
        code, reason = _failure(
            checks,
            "upstream_declaration_has_zero_failed_checks",
            "UPSTREAM_DECLARATION_FAILED_CHECKS_PRESENT",
        )
        return upstream, code, reason
    if (
        declaration.get("declaration_result")
        != SELECTED_DECLARATION_RESULT_REQUIRED
        or declaration.get(
            "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_result"
        )
        != SELECTED_DECLARATION_RESULT_REQUIRED
    ):
        code, reason = _failure(
            checks,
            "upstream_declaration_result_matches",
            "UPSTREAM_DECLARATION_RESULT_MISMATCH",
        )
        return upstream, code, reason
    declaration_identity = {
        "declaration_id": SELECTED_DECLARATION_ID,
        "declaration_type": SELECTED_DECLARATION_TYPE,
        "declaration_version": SELECTED_DECLARATION_VERSION,
        "declaration_scope": SELECTED_DECLARATION_SCOPE,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_id": SELECTED_DECLARATION_ID,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_type": SELECTED_DECLARATION_TYPE,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_version": SELECTED_DECLARATION_VERSION,
        "receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_scope": SELECTED_DECLARATION_SCOPE,
    }
    if any(
        declaration.get(key) != expected
        for key, expected in declaration_identity.items()
    ):
        code, reason = _failure(
            checks,
            "upstream_declaration_identity_matches",
            "SELECTED_DECLARATION_IDENTITY_MISMATCH",
        )
        return upstream, code, reason
    selected_identity = {
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "selected_candidate_sufficiency_boundary_id": SELECTED_SUFFICIENCY_BOUNDARY_ID,
        "selected_candidate_sufficiency_operation_id": SELECTED_SUFFICIENCY_OPERATION_ID,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "selected_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
    }
    for key, expected in selected_identity.items():
        if declaration.get(key) != expected:
            code = _identity_code(key)
            failure, reason = _failure(
                checks, f"upstream_{key}_matches", code
            )
            return upstream, failure, reason
    if summary.get("upstream_waiting_operation_validated") is not True:
        code, reason = _failure(
            checks,
            "upstream_waiting_operation_validated",
            "UPSTREAM_WAITING_OPERATION_NOT_VALIDATED",
        )
        return upstream, code, reason
    if (
        declaration.get("declaration_records_supplied") is not False
        or declaration.get("declaration_record_count") != 0
    ):
        code, reason = _failure(
            checks,
            "upstream_declaration_records_absent",
            "UPSTREAM_DECLARATION_RECORDS_ALREADY_SUPPLIED",
        )
        return upstream, code, reason
    if (
        declaration.get("declaration_complete") is not False
        or declaration.get(
            "candidate_sufficiency_basis_declaration_ready_for_supply"
        )
        is not False
    ):
        code, reason = _failure(
            checks,
            "upstream_declaration_incomplete_and_not_ready",
            "UPSTREAM_DECLARATION_ALREADY_COMPLETE_OR_READY",
        )
        return upstream, code, reason
    if (
        declaration.get(
            "candidate_sufficiency_basis_declaration_recorded"
        )
        is not False
    ):
        code, reason = _failure(
            checks,
            "upstream_declaration_not_recorded",
            "UPSTREAM_DECLARATION_ALREADY_RECORDED",
        )
        return upstream, code, reason
    if (
        declaration.get(
            "candidate_sufficiency_basis_declaration_result_recorded"
        )
        is not False
    ):
        code, reason = _failure(
            checks,
            "upstream_declaration_result_not_recorded",
            "UPSTREAM_DECLARATION_RESULT_ALREADY_RECORDED",
        )
        return upstream, code, reason
    if not _validate_false_keys(
        declaration,
        (
            "candidate_sufficiency_basis_separately_supplied",
            "candidate_sufficiency_basis_admitted_by_operation",
        ),
    ):
        code, reason = _failure(
            checks,
            "upstream_basis_not_supplied_or_admitted",
            "UPSTREAM_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
        )
        return upstream, code, reason
    if not _validate_false_keys(
        declaration,
        (
            "candidate_sufficiency_operation_recorded",
            "candidate_sufficiency_operation_result_recorded",
            "candidate_sufficiency_operation_executed",
            "candidate_sufficiency_operation_exhausted",
        ),
    ):
        code, reason = _failure(
            checks,
            "upstream_operation_not_executed_or_exhausted",
            "UPSTREAM_OPERATION_ALREADY_EXECUTED_OR_EXHAUSTED",
        )
        return upstream, code, reason
    if not _validate_false_keys(
        declaration,
        (
            "receiver_side_answerable_basis_candidate_sufficient",
            "receiver_side_answerable_basis_candidate_insufficient",
            "receiver_side_answerable_basis_candidate_indeterminate",
            "candidate_sufficiency_decided",
            "candidate_sufficiency_established",
            "candidate_insufficiency_established",
            "candidate_indeterminacy_established",
            "dimension_results_derived",
            "candidate_result_derived",
        ),
    ):
        code, reason = _failure(
            checks,
            "upstream_candidate_result_absent",
            "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
        )
        return upstream, code, reason
    receiver_keys = (
        "receiver_attestation_created",
        "receiver_attestation_supported",
        "receiver_attestation_boundary_created",
        "receiver_answerable_receipt_present",
        "receiver_answerable_receipt_boundary_created",
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
        "presence_re_evaluation_boundary_created",
    )
    if not _validate_false_keys(declaration, receiver_keys):
        code, reason = _failure(
            checks,
            "upstream_receiver_receipt_presence_absent",
            "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
        )
        return upstream, code, reason
    route_keys = (
        "repeated_declaration_permission_created",
        "reusable_declaration_route_created",
        "silent_declaration_replacement_authorized",
        "automatic_redeclaration_created",
        "declaration_debt_created",
        "declaration_obligation_created",
        "candidate_sufficiency_operation_authorized",
        "candidate_sufficiency_operation_created",
        "identity_created",
        "relation_created",
        "coupling_assigned",
        "coupling_created",
        "field_machinery_created",
        "runtime_created",
        "api_created",
        "public_intake_created",
        "public_interface_created",
        "authority_created",
        "standing_created",
        "truth_created",
        "continuity_memory_written",
        "output_authorized",
        "action_authorized",
        "synchronization_authorized",
        "follow_on_authorized",
        "follow_on_work_authorized",
    )
    if not _validate_false_keys(declaration, route_keys):
        code, reason = _failure(
            checks,
            "upstream_route_retry_debt_obligation_downstream_absent",
            "UPSTREAM_ROUTE_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
        )
        return upstream, code, reason
    open_values = list(open_state)
    stale_open_markers = {
        "candidate-sufficiency basis declaration specification",
        "candidate-sufficiency basis declaration resolver",
        "candidate-sufficiency basis declaration test",
        "selected incomplete declaration artifact",
    }
    if (
        not open_values
        or open_values[0]
        != "complete eight-record candidate-sufficiency basis declaration"
        or "preparation-request declaration, if separately selected"
        not in open_values
        or any(marker in open_values for marker in stale_open_markers)
    ):
        code, reason = _failure(
            checks,
            "upstream_open_state_matches_incomplete_declaration",
            "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
        )
        return upstream, code, reason
    upstream.update(
        {
            "selected_incomplete_declaration_validated": True,
            "selected_incomplete_declaration_identity": {
                "declaration_id": SELECTED_DECLARATION_ID,
                "declaration_type": SELECTED_DECLARATION_TYPE,
                "declaration_version": SELECTED_DECLARATION_VERSION,
                "declaration_scope": SELECTED_DECLARATION_SCOPE,
                "declaration_result": SELECTED_DECLARATION_RESULT_REQUIRED,
                "candidate_id": CANDIDATE_ID,
                "sufficiency_boundary_id": SELECTED_SUFFICIENCY_BOUNDARY_ID,
                "sufficiency_operation_id": SELECTED_SUFFICIENCY_OPERATION_ID,
            },
            "selected_incomplete_declaration_metadata": {
                "outcome": artifact.get("outcome"),
                "failed_check_count": artifact.get("failed_check_count"),
                "passed_check_count": artifact.get("passed_check_count"),
                "resolver_module": artifact.get("resolver_module"),
                "result_version": artifact.get("result_version"),
            },
            "selected_incomplete_declaration_posture": {
                "declaration_records_supplied": False,
                "declaration_record_count": 0,
                "declaration_complete": False,
                "declaration_ready_for_supply": False,
                "basis_separately_supplied": False,
                "basis_admitted_by_operation": False,
                "operation_executed": False,
                "operation_exhausted": False,
                "candidate_result_present": False,
                "receiver_receipt_presence_present": False,
                "route_retry_debt_obligation_or_downstream_present": False,
                "what_remains_open_validated": True,
            },
        }
    )
    checks.append(_check("selected_incomplete_declaration_validated", True))
    return upstream, None, None


def _validate_preparer_posture(
    posture: Any,
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, bool, list[str]]:
    missing: list[str] = []
    if posture is None or posture == {}:
        return None, None, False, ["preparer_posture"]
    if not isinstance(posture, Mapping):
        code, reason = _failure(
            checks, "preparer_posture_is_mapping", "PREPARER_POSTURE_NOT_MAPPING"
        )
        return code, reason, False, missing
    if len(posture) > MAX_PREPARER_POSTURE_ITEMS or not _bounded_json(posture):
        code, reason = _failure(
            checks, "preparer_posture_is_bounded", "PREPARER_POSTURE_INVALID"
        )
        return code, reason, False, missing
    if _contains_key(posture, FORBIDDEN_PAYLOAD_KEYS):
        code, reason = _failure(
            checks,
            "preparer_posture_contains_no_basis_material",
            "REQUEST_PAYLOAD_CONTAINS_DECLARATION_OR_BASIS_MATERIAL",
        )
        return code, reason, False, missing
    unknown = set(posture) - PREPARER_POSTURE_KEYS
    if unknown:
        code, reason = _failure(
            checks,
            "preparer_posture_has_only_supported_fields",
            "PREPARER_POSTURE_INVALID",
        )
        return code, reason, False, missing
    for key in PREPARER_POSTURE_KEYS - set(posture):
        missing.append(f"preparer_posture:{key}")
    if (
        "preparer_reference" in posture
        and posture.get("preparer_reference") != PREPARER_REFERENCE
    ):
        code, reason = _failure(
            checks, "preparer_reference_exact", "PREPARER_REFERENCE_INVALID"
        )
        return code, reason, False, missing
    if (
        isinstance(posture.get("preparer_reference"), str)
        and len(posture["preparer_reference"]) > MAX_PREPARER_REFERENCE_LENGTH
    ):
        code, reason = _failure(
            checks, "preparer_reference_bounded", "PREPARER_REFERENCE_INVALID"
        )
        return code, reason, False, missing
    if (
        "preparer_relation_to_source_body" in posture
        and posture.get("preparer_relation_to_source_body")
        != PREPARER_RELATION_TO_SOURCE_BODY
    ):
        code, reason = _failure(
            checks, "preparer_relation_exact", "PREPARER_RELATION_INVALID"
        )
        return code, reason, False, missing
    if (
        isinstance(posture.get("preparer_relation_to_source_body"), str)
        and len(posture["preparer_relation_to_source_body"])
        > MAX_PREPARER_RELATION_LENGTH
    ):
        code, reason = _failure(
            checks, "preparer_relation_bounded", "PREPARER_RELATION_INVALID"
        )
        return code, reason, False, missing
    if posture.get("independent_preparer_claimed") is True:
        code, reason = _failure(
            checks,
            "independent_preparer_not_claimed",
            "FALSE_INDEPENDENT_PREPARER_CLAIM",
        )
        return code, reason, False, missing
    if posture.get("separate_custody_claimed_by_preparer") is True:
        code, reason = _failure(
            checks,
            "separate_custody_not_claimed",
            "FALSE_SEPARATE_CUSTODY_CLAIM",
        )
        return code, reason, False, missing
    expected_booleans = {
        "source_body_preparer": True,
        "independent_preparer_claimed": False,
        "separate_custody_claimed_by_preparer": False,
        "preparer_authority_claimed": False,
        "preparer_identity_established": False,
        "preparer_standing_claimed": False,
        "preparer_truth_claimed": False,
    }
    for key, expected in expected_booleans.items():
        if key not in posture:
            continue
        if not _exact_bool(posture.get(key)) or posture.get(key) is not expected:
            code, reason = _failure(
                checks, f"{key}_exact", "PREPARER_POSTURE_INVALID"
            )
            return code, reason, False, missing
    if missing:
        return None, None, False, missing
    checks.append(_check("preparer_posture_exact_and_bounded", True))
    return None, None, True, missing


def _validate_material(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, bool, list[str]]:
    missing: list[str] = []
    dimensions = request.get("requested_dimension_ids")
    dimension_complete = False
    if not isinstance(dimensions, Sequence) or isinstance(
        dimensions, (str, bytes, bytearray)
    ):
        code, reason = _failure(
            checks,
            "requested_dimension_ids_are_ordered_sequence",
            "REQUESTED_DIMENSION_SET_MISMATCH",
        )
        return code, reason, False, missing
    values = tuple(dimensions)
    if not values:
        missing.append("requested_dimension_ids")
    elif values == REQUESTED_PREPARATION_DIMENSION_IDS:
        dimension_complete = True
        checks.append(_check("requested_dimension_ids_exact_and_ordered", True))
    elif (
        len(values) < len(REQUESTED_PREPARATION_DIMENSION_IDS)
        and values == REQUESTED_PREPARATION_DIMENSION_IDS[: len(values)]
    ):
        missing.append("requested_dimension_ids:complete_exact_eight_dimension_set")
    else:
        code, reason = _failure(
            checks,
            "requested_dimension_ids_exact_and_ordered",
            "REQUESTED_DIMENSION_SET_MISMATCH",
        )
        return code, reason, False, missing
    code, reason, preparer_complete, preparer_missing = _validate_preparer_posture(
        request.get("preparer_posture"), checks
    )
    missing.extend(preparer_missing)
    if code is not None:
        return code, reason, False, missing
    complete = dimension_complete and preparer_complete and not missing
    if complete:
        checks.append(_check("preparation_request_material_complete", True))
    return None, None, complete, missing


def build_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_request(
    *,
    intent: str = INTENT_RECORD,
    preparation_request_material_supplied: bool | None = None,
    requested_dimension_ids: Sequence[str] | None = None,
    preparer_posture: Mapping[str, Any] | None = None,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one bounded request without fabricating complete request material."""
    material_present = requested_dimension_ids is not None or preparer_posture is not None
    supplied = (
        material_present
        if preparation_request_material_supplied is None
        else preparation_request_material_supplied
    )
    request: dict[str, Any] = {
        "intent": intent,
        **_expected_request_values(),
        "preparation_request_material_supplied": supplied,
        "requested_dimension_ids": (
            copy.deepcopy(list(requested_dimension_ids))
            if requested_dimension_ids is not None
            else []
        ),
        "preparer_posture": copy.deepcopy(preparer_posture),
        "declared_non_claims": copy.deepcopy(
            declared_non_claims
            if declared_non_claims is not None
            else _canonical_non_claims()
        ),
        **{key: False for key in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_request(
    *,
    intent: str = INTENT_RECORD,
    requested_dimension_ids: Sequence[str] | None = None,
    preparer_posture: Mapping[str, Any] | None = None,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one exact complete declaration request without performing it."""
    return build_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_request(
        intent=intent,
        preparation_request_material_supplied=True,
        requested_dimension_ids=(
            REQUESTED_PREPARATION_DIMENSION_IDS
            if requested_dimension_ids is None
            else requested_dimension_ids
        ),
        preparer_posture=(
            _complete_preparer_posture()
            if preparer_posture is None
            else preparer_posture
        ),
        declared_non_claims=declared_non_claims,
        **overrides,
    )


def resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate one preparation-request declaration without performing it."""
    if request is None:
        working: Mapping[str, Any] = (
            build_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_request()
        )
    elif not isinstance(request, Mapping):
        checks = [_check("request_is_mapping", False, "REQUEST_NOT_MAPPING")]
        return _result(
            {},
            OUTCOME_BLOCKED,
            REQUEST_RESULT_NOT_EVALUATED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="request is not a mapping",
        )
    else:
        working = copy.deepcopy(dict(request))
    checks: list[dict[str, Any]] = []
    code, reason = _validate_request(working, checks)
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            REQUEST_RESULT_NOT_EVALUATED,
            checks,
            code=code,
            reason=reason,
        )
    if working.get("intent") == INTENT_DO_NOT_RECORD:
        checks.append(_check("do_not_record_intent_honored", True))
        return _result(
            working,
            OUTCOME_NOT_RECORDED,
            REQUEST_RESULT_NOT_EVALUATED,
            checks,
        )
    upstream, code, reason = _validate_upstream(checks)
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            REQUEST_RESULT_NOT_EVALUATED,
            checks,
            upstream=upstream,
            code=code,
            reason=reason,
        )
    if working.get("preparation_request_material_supplied") is False:
        checks.append(_check("request_material_absence_is_lawful_waiting", True))
        return _result(
            working,
            OUTCOME_REQUIRES_COMPLETE,
            REQUEST_RESULT_REQUIRES_COMPLETE,
            checks,
            upstream=upstream,
            missing=["complete preparation-request declaration"],
        )
    code, reason, complete, missing = _validate_material(working, checks)
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            REQUEST_RESULT_NOT_EVALUATED,
            checks,
            upstream=upstream,
            missing=missing,
            code=code,
            reason=reason,
        )
    if not complete:
        checks.append(_check("partial_request_material_is_lawful_waiting", True))
        return _result(
            working,
            OUTCOME_REQUIRES_COMPLETE,
            REQUEST_RESULT_REQUIRES_COMPLETE,
            checks,
            upstream=upstream,
            missing=missing,
        )
    checks.append(_check("preparation_request_recorded_without_performance", True))
    return _result(
        working,
        OUTCOME_RECORDED,
        REQUEST_RESULT_RECORDED,
        checks,
        upstream=upstream,
        complete=True,
    )


def resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one explicit JSON request path without filesystem discovery."""
    value, error = _read_json(request_path)
    if error is not None or not isinstance(value, Mapping):
        checks = [_check("request_path_is_mapping_json", False, "REQUEST_NOT_MAPPING")]
        return _result(
            {},
            OUTCOME_BLOCKED,
            REQUEST_RESULT_NOT_EVALUATED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="request path is missing, malformed, or not a mapping",
        )
    return resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min(
        value
    )


def build_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build the compact bounded summary for one resolver result."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
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


def _contains_forbidden_result_material(value: Any) -> bool:
    forbidden = FORBIDDEN_PAYLOAD_KEYS | {
        "complete_incomplete_declaration_artifact",
        "complete_selected_declaration_artifact",
        "complete_selected_declaration_checks",
    }
    return _contains_key(value, forbidden)


def _output_path_is_forbidden(path: Path) -> bool:
    resolved = path.resolve(strict=False)
    parts = {part.lower().replace("-", "_") for part in resolved.parts}
    if parts & {"spec", "tests", "reference"}:
        return True
    parent_rendered = "/".join(
        part.lower().replace("-", "_") for part in resolved.parent.parts
    )
    forbidden_markers = (
        "candidate_reception",
        "candidate_evaluation",
        "evaluation_basis",
        "sufficiency_boundary",
        "sufficiency_operation",
        "sufficiency_basis_declaration_v0_min",
        "presence",
        "relation",
        "identity",
        "field",
        "runtime",
        "api",
        "public_intake",
        "descendant",
        "receiver_capture",
    )
    return any(marker in parent_rendered for marker in forbidden_markers)


def _validate_write_result(result: Mapping[str, Any]) -> None:
    if set(result) != set(RESULT_SECTIONS):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result sections do not match resolver contract"
        )
    if result.get("resolver_module") != RESOLVER_MODULE:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result resolver module does not match"
        )
    if result.get("result_version") != RESULT_VERSION:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result version does not match"
        )
    outcome = result.get("outcome")
    if outcome not in OUTCOME_FAMILY:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result outcome is unsupported"
        )
    prefix = (
        "receiver_side_answerable_basis_candidate_sufficiency_basis_"
        "preparation_request_declaration"
    )
    state = result.get(prefix)
    if not isinstance(state, Mapping):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result request object is missing"
        )
    wrapper_keys = {
        "outcome",
        "block",
        "non_claims",
        f"{prefix}_checks",
        f"{prefix}_summary",
        f"{prefix}_metadata",
    }
    if set(state) & wrapper_keys:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "request object contains wrapper sections"
        )
    expected_result = {
        OUTCOME_RECORDED: REQUEST_RESULT_RECORDED,
        OUTCOME_REQUIRES_COMPLETE: REQUEST_RESULT_REQUIRES_COMPLETE,
        OUTCOME_BLOCKED: REQUEST_RESULT_NOT_EVALUATED,
        OUTCOME_NOT_RECORDED: REQUEST_RESULT_NOT_EVALUATED,
    }[outcome]
    if state.get("request_result") != expected_result:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "request-result branch does not match outcome"
        )
    if not _all_false_mapping(
        result.get("non_claims"), REQUIRED_FALSE_NON_CLAIMS
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result non-claims are not canonical false"
        )
    if not _all_false_mapping(state, REQUIRED_FALSE_NON_CLAIMS):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "request-object non-claims are not canonical false"
        )
    checks = result.get(f"{prefix}_checks")
    if not isinstance(checks, list) or not all(
        isinstance(check, Mapping) for check in checks
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result checks are malformed"
        )
    failed = sum(check.get("passed") is False for check in checks)
    passed = sum(check.get("passed") is True for check in checks)
    if (
        result.get("failed_check_count") != failed
        or result.get("passed_check_count") != passed
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result check counts are inconsistent"
        )
    for check in checks:
        for code_key in ("block_code", "failure_code"):
            emitted = check.get(code_key)
            if emitted is not None and emitted not in BLOCK_CODES:
                raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
                    "result contains a non-public failure code"
                )
    block = result.get("block")
    if not isinstance(block, Mapping):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result block posture is malformed"
        )
    if outcome == OUTCOME_BLOCKED:
        emitted = block.get("code") or block.get("block_code")
        if (
            block.get("blocked") is not True
            or emitted not in BLOCK_CODES
            or failed <= 0
        ):
            raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
                "blocked result posture is inconsistent"
            )
    elif (
        block.get("blocked") is not False
        or block.get("code") is not None
        or block.get("block_code") is not None
        or block.get("reason") is not None
        or failed != 0
    ):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "non-blocked result posture is inconsistent"
        )
    false_state_keys = (
        "candidate_sufficiency_basis_preparation_started",
        "candidate_sufficiency_basis_preparation_completed",
        "candidate_sufficiency_basis_declaration_records_created",
        "candidate_sufficiency_basis_declaration_ready_for_supply",
        "candidate_sufficiency_basis_separately_supplied",
        "candidate_sufficiency_basis_admitted_by_operation",
        "candidate_sufficiency_operation_executed",
        "candidate_sufficiency_operation_exhausted",
    )
    if not _validate_false_keys(state, false_state_keys):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result claims prohibited performance or later posture"
        )
    recorded = outcome == OUTCOME_RECORDED
    recorded_keys = (
        "preparation_request_complete",
        "candidate_sufficiency_basis_preparation_request_declaration_recorded",
        "candidate_sufficiency_basis_preparation_request_declaration_result_recorded",
        "candidate_sufficiency_basis_preparation_requested",
    )
    if any(state.get(key) is not recorded for key in recorded_keys):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "recorded-request posture is inconsistent"
        )
    if recorded:
        if (
            state.get("preparation_request_material_supplied") is not True
            or tuple(state.get("requested_dimension_ids", ()))
            != REQUESTED_PREPARATION_DIMENSION_IDS
            or state.get("requested_dimension_count")
            != len(REQUESTED_PREPARATION_DIMENSION_IDS)
            or any(
                state.get(key) != expected
                for key, expected in _complete_preparer_posture().items()
            )
        ):
            raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
                "recorded request material is inconsistent"
            )
    if not _bounded_json(result) or _serialized_size(result) is None:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result is not bounded JSON"
        )
    if _contains_forbidden_result_material(result):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result contains copied declaration, basis, candidate, capture, or upstream material"
        )


def write_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one validated bounded result without silent overwrite."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result must be a mapping"
        )
    _validate_write_result(result)
    target = (
        OUTPUT_ROOT / OUTPUT_FILENAME
        if output_path is None
        else _as_path(output_path)
    )
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "output path is forbidden"
        )
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _next_available_output_path(target)
    try:
        target.write_text(
            json.dumps(
                copy.deepcopy(dict(result)),
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            + "\n",
            encoding="utf-8",
        )
    except (OSError, TypeError, ValueError) as error:
        raise ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError(
            "result write refused"
        ) from error
    return target
