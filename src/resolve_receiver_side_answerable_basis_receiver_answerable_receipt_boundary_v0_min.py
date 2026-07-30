"""Resolve one bounded receiver-answerable-receipt consideration boundary.

The resolver consumes only the exact completed receiver-attestation operation
artifact.  It may record whether receipt consideration is allowed; it never
creates receipt, re-evaluates attestation, reads capture bodies, or authorizes
downstream work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from types import MappingProxyType
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_v0_min"
)

BOUNDARY_ID = (
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_001"
)
BOUNDARY_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY"
)
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = (
    "CONSIDER_ONE_RECEIVER_ANSWERABLE_RECEIPT_FOR_ONE_"
    "RECORDED_RECEIVER_ATTESTATION_RESULT_ONLY"
)

SELECTED_RECEIVER_ATTESTATION_OPERATION_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_001"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION = "0.1.0"
SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE = (
    "ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_"
    "FOR_ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_RECORDED"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_VERSION = "0.1.0"
SELECTED_RECEIVER_ATTESTATION_OPERATION_PASSED_CHECK_COUNT = 160

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = (
    "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)

ADMISSIBLE_FUTURE_ROUTE = (
    "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_THEN_SEPARATE_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OR_DECLARATION_ONLY"
)

OUTCOME_ALLOWED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ALLOWED"
)
OUTCOME_NOT_ALLOWED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_NOT_ALLOWED"
)
OUTCOME_BLOCKED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED, OUTCOME_BLOCKED)

RESULT_ALLOWED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_CONSIDERATION_ALLOWED"
)
RESULT_NOT_ALLOWED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_CONSIDERATION_NOT_ALLOWED"
)
RESULT_NOT_EVALUATED = "NOT_EVALUATED"
RESULT_FAMILY = (RESULT_ALLOWED, RESULT_NOT_ALLOWED, RESULT_NOT_EVALUATED)
BOUNDARY_RESULT_FAMILY = RESULT_FAMILY

DECISION_CODE_ALLOWED = "RECEIPT_CONSIDERATION_ALLOWED"
DECISION_REASON_ALLOWED = (
    "exact recorded receiver-attestation result admitted for "
    "receiver-answerable-receipt consideration only"
)
DECISION_CODE_NOT_ALLOWED = "RECEIPT_CONSIDERATION_NOT_ALLOWED"
DECISION_REASON_NOT_ALLOWED = (
    "receiver-answerable-receipt consideration not selected"
)

INTENT_RECORD = (
    "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_V0_MIN_SPEC.md"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_attestation_operation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_001__"
    "receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min_result_001.json"
)
WAITING_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_attestation_operation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_001__"
    "receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min_result.json"
)
GOVERNING_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
)
GOVERNING_SPEC_RELATIVE_PATH = GOVERNING_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPEC_PATH = GOVERNING_SPECIFICATION_PATH
SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_PATH = (
    REPO_ROOT
    / SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
)
CANONICAL_OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_v0_min"
)
OUTPUT_ROOT = CANONICAL_OUTPUT_ROOT
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_001__"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_v0_min_result.json"
)

SPEC_MARKER_FAMILIES = MappingProxyType(
    {
        "title": (
            "# Receiver-Side Answerable Basis Receiver-Answerable "
            "Receipt Boundary V0 Minimum Specification",
        ),
        "boundary_identity": (
            (
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_boundary_id = "
                + BOUNDARY_ID
            ),
            (
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_boundary_type = "
                + BOUNDARY_TYPE
            ),
            (
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_boundary_version = "
                + BOUNDARY_VERSION
            ),
            (
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_boundary_scope = "
                + BOUNDARY_SCOPE
            ),
        ),
        "selected_operation": (
            (
                "selected_receiver_attestation_operation_id = "
                + SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
            ),
            (
                "selected_receiver_attestation_operation_result_required = "
                + SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
            ),
        ),
        "selected_artifact": (
            str(
                SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
            ),
        ),
        "outcome_family": OUTCOME_FAMILY,
        "result_family": RESULT_FAMILY,
        "decision_rules": (
            "## 10. Request and Decision Rules",
            "Consideration may be allowed only when:",
            "Consideration may be not allowed only when",
            "The boundary must block when:",
        ),
        "separation": (
            (
                "Receiver attestation recorded is not "
                "receiver-answerable receipt."
            ),
            "Receipt consideration allowed is not receipt.",
            "Receipt is not presence.",
            "boundary exhaustion is not downstream authorization",
        ),
        "future_contract": (
            "Any later receipt work requires separate selection",
            "a separate bounded contract",
        ),
        "lineage": (
            "All contaminated lineage remains unchanged.",
            "Open does not mean next.",
        ),
    }
)
SPEC_MARKERS = tuple(
    marker
    for family in SPEC_MARKER_FAMILIES.values()
    for marker in family
)

REQUIRED_UPSTREAM_TRUE_POSTURES = (
    "operation_basis_supplied",
    "operation_basis_admitted",
    "receiver_attestation_operation_recorded",
    "receiver_attestation_operation_result_recorded",
    "receiver_attestation_operation_exhausted",
    "receiver_attestation_decided",
    "receiver_attestation_recorded",
    "operation_result_present",
    "minimum_admission_checks_passed",
    "archive_correspondence_validated",
    "text_components_validated",
    "timestamp_validated",
    "trace_paths_validated",
    "recorded_signal_artifact_existence_validated",
    "result_level_non_claims_canonical_false",
)

REQUIRED_UPSTREAM_FALSE_POSTURES = (
    "receiver_attestation_not_recorded",
    "receiver_attestation_indeterminate",
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_answerable_receipt_present",
    "receiver_answerable_receipt_boundary_created",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "presence_re_evaluation_boundary_created",
    "identity_created",
    "authority_created",
    "truth_created",
    "standing_created",
    "relation_created",
    "coupling_assigned",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "public_intake_created",
    "output_authorized",
    "action_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "repeated_receiver_attestation_operation_permission_created",
    "reusable_receiver_attestation_operation_route_created",
    "same_receiver_attestation_operation_rerun_authorized",
    "automatic_receiver_attestation_operation_retry_created",
    "receiver_attestation_operation_debt_created",
    "receiver_attestation_operation_obligation_created",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_answerable_receipt_boundary_created",
    "receiver_answerable_receipt_present",
    "receiver_answerable_receipt_operation_created",
    "receiver_answerable_receipt_operation_executed",
    "receiver_answerable_receipt_result_recorded",
    "receiver_answerable_receipt_supported",
    "presence_re_evaluation_boundary_created",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "identity_created",
    "custody_created",
    "provenance_created",
    "physical_validity_created",
    "authority_created",
    "truth_created",
    "standing_created",
    "relation_created",
    "coupling_assigned",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "public_intake_created",
    "output_authorized",
    "action_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "repeated_receiver_answerable_receipt_boundary_permission_created",
    "reusable_receiver_answerable_receipt_route_created",
    "same_receiver_answerable_receipt_boundary_rerun_authorized",
    "automatic_receiver_answerable_receipt_boundary_retry_created",
    "receiver_answerable_receipt_boundary_debt_created",
    "receiver_answerable_receipt_boundary_obligation_created",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

OMISSION_POSTURE_FIELDS = (
    "complete_selected_upstream_operation_artifact_omitted",
    "complete_operation_basis_omitted",
    "complete_candidate_sufficiency_artifact_omitted",
    "complete_candidate_sufficiency_basis_omitted",
    "complete_receiver_attestation_boundary_artifact_omitted",
    "archive_bytes_omitted",
    "hash_record_body_omitted",
    "text_component_bodies_omitted",
    "recorded_signal_body_omitted",
)

PROHIBITED_REQUEST_FLAGS = MappingProxyType(
    {
        "request_receiver_answerable_receipt_present": (
            "PROHIBITED_RECEIPT_REQUESTED"
        ),
        "request_receiver_answerable_receipt_operation_created": (
            "PROHIBITED_RECEIPT_OPERATION_REQUESTED"
        ),
        "request_receiver_answerable_receipt_operation_executed": (
            "PROHIBITED_RECEIPT_OPERATION_REQUESTED"
        ),
        "request_receiver_answerable_receipt_result_recorded": (
            "PROHIBITED_RECEIPT_RESULT_REQUESTED"
        ),
        "request_receiver_answerable_receipt_supported": (
            "PROHIBITED_RECEIPT_REQUESTED"
        ),
        "request_presence_re_evaluation_boundary_created": (
            "PROHIBITED_PRESENCE_REQUESTED"
        ),
        "request_presence_supported": "PROHIBITED_PRESENCE_REQUESTED",
        "request_presence_authorized": "PROHIBITED_PRESENCE_REQUESTED",
        "request_presence_established": "PROHIBITED_PRESENCE_REQUESTED",
        "request_presence_recorded": "PROHIBITED_PRESENCE_REQUESTED",
        "request_identity_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_custody_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_provenance_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_physical_validity_created": (
            "PROHIBITED_DOWNSTREAM_REQUESTED"
        ),
        "request_authority_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_truth_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_standing_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_relation_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_coupling_assigned": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_coupling_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_field_machinery_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_runtime_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_api_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_public_interface_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_public_intake_created": "PROHIBITED_DOWNSTREAM_REQUESTED",
        "request_output_authorized": "PROHIBITED_AUTHORIZATION_REQUESTED",
        "request_action_authorized": "PROHIBITED_AUTHORIZATION_REQUESTED",
        "request_synchronization_authorized": (
            "PROHIBITED_AUTHORIZATION_REQUESTED"
        ),
        "request_follow_on_authorized": "PROHIBITED_AUTHORIZATION_REQUESTED",
        "request_follow_on_work_authorized": (
            "PROHIBITED_AUTHORIZATION_REQUESTED"
        ),
        "request_repeated_boundary_permission_created": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_reusable_receipt_route_created": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_same_boundary_rerun_authorized": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_automatic_boundary_retry_created": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_boundary_debt_created": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_boundary_obligation_created": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_scheduled_receipt_operation": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_automatic_next_step": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_affected_file_repair": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_repository_scan": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_file_discovery": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_validation_enforcement": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_contaminated_lineage_validation": (
            "PROHIBITED_CONTAMINATED_LINEAGE_VALIDATION_REQUESTED"
        ),
        "request_complete_upstream_artifact_embedding": (
            "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
        ),
        "request_bounded_capture_reread": (
            "PROHIBITED_CAPTURE_BODY_READ_REQUESTED"
        ),
        "request_archive_body_read": (
            "PROHIBITED_CAPTURE_BODY_READ_REQUESTED"
        ),
        "request_hash_record_body_read": (
            "PROHIBITED_CAPTURE_BODY_READ_REQUESTED"
        ),
        "request_text_component_body_read": (
            "PROHIBITED_CAPTURE_BODY_READ_REQUESTED"
        ),
        "request_recorded_signal_body_read": (
            "PROHIBITED_CAPTURE_BODY_READ_REQUESTED"
        ),
        "request_outcome_preclaim": "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "request_result_preclaim": "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
    }
)

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "REQUEST_FIELD_MISSING",
        "REQUEST_UNKNOWN_FIELD",
        "REQUEST_VALUE_MISMATCH",
        "REQUEST_BOOLEAN_REQUIRED",
        "UNSUPPORTED_INTENT",
        "EXPLICIT_BLOCK_REQUESTED",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "RECEIPT_BOUNDARY_SPEC_REFERENCE_MISSING",
        "RECEIPT_BOUNDARY_SPEC_MARKER_MISSING",
        "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_MISSING",
        "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_NOT_PARSEABLE",
        "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_DUPLICATE_KEYED",
        "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_NOT_MAPPING",
        "UPSTREAM_METADATA_MISMATCH",
        "UPSTREAM_FAILED_CHECKS_PRESENT",
        "UPSTREAM_BLOCKED",
        "UPSTREAM_OPERATION_IDENTITY_MISMATCH",
        "UPSTREAM_CANDIDATE_IDENTITY_MISMATCH",
        "UPSTREAM_RESULT_MISMATCH",
        "UPSTREAM_RESULT_CARDINALITY_MISMATCH",
        "UPSTREAM_TRUE_POSTURE_NOT_TRUE",
        "UPSTREAM_FALSE_LOCK_NOT_FALSE",
        "UPSTREAM_NON_CLAIMS_NOT_CANONICAL_FALSE",
        "PROHIBITED_RECEIPT_REQUESTED",
        "PROHIBITED_RECEIPT_OPERATION_REQUESTED",
        "PROHIBITED_RECEIPT_RESULT_REQUESTED",
        "PROHIBITED_PRESENCE_REQUESTED",
        "PROHIBITED_DOWNSTREAM_REQUESTED",
        "PROHIBITED_AUTHORIZATION_REQUESTED",
        "PROHIBITED_REPEATED_USE_REQUESTED",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "PROHIBITED_CONTAMINATED_LINEAGE_VALIDATION_REQUESTED",
        "PROHIBITED_COMPLETE_MATERIAL_REQUESTED",
        "PROHIBITED_CAPTURE_BODY_READ_REQUESTED",
        "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "WRITE_REFUSED",
    }
)

BLOCKED_ROUTES = (
    "candidate_sufficiency_to_receiver_answerable_receipt",
    "receiver_attestation_consideration_to_receipt",
    "receiver_attestation_recording_to_receipt_presence",
    "archive_hash_text_or_signal_correspondence_to_receipt",
    "attestation_result_to_presence",
    "receipt_consideration_to_receipt_result",
    "boundary_result_to_presence_re_evaluation",
    "receipt_to_identity_custody_provenance_physical_validity_authority_truth_or_standing",
    "boundary_result_to_relation_coupling_field_runtime_api_public_output_action_synchronization_or_follow_on",
    "boundary_result_to_repeat_reusable_rerun_retry_debt_obligation_or_scheduled_work",
    "receipt_boundary_to_contaminated_lineage_repair_or_validation",
)

WHAT_REMAINS_OPEN = (
    "receipt-boundary tests",
    "receipt-boundary live result",
    "receipt-boundary terminal summary",
    (
        "receiver-answerable-receipt operation or declaration, only after "
        "a separately recorded allowed boundary"
    ),
    "receiver-answerable-receipt result",
    "presence re-evaluation",
    "presence support, authorization, establishment, and recording",
    "identity",
    "custody",
    "provenance",
    "physical validity",
    "authority",
    "truth",
    "standing",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "public interface",
    "public intake",
    "output",
    "action",
    "synchronization",
    "repair",
    "validation",
    "follow-on work",
)

RESULT_SECTIONS = frozenset(
    {
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_metadata"
        ),
        "selected_operation_and_candidate_identity",
        "declared_request_posture",
        "specification_validation",
        "upstream_artifact_validation",
        "compact_upstream_standing",
        "boundary_decision",
        "block",
        "boundary_posture",
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary"
        ),
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_checks"
        ),
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_statement"
        ),
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_non_meaning"
        ),
        "omission_posture",
        "blocked_routes",
        "admissible_future_route",
        "what_remains_open",
        "non_claims",
        "result_level_non_claims_canonical_false",
        "outcome",
        "boundary_result",
        "failed_check_count",
        "passed_check_count",
        "resolver_module",
        "result_version",
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_summary"
        ),
    }
)


class ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
    Exception
):
    """Raised for invalid path input, result writing, or protected output."""


class _DuplicateJsonKeyError(ValueError):
    """Raised when a JSON object repeats one member name."""


def _reject_duplicate_json_keys(
    pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKeyError(key)
        result[key] = value
    return result


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_omission_posture() -> dict[str, bool]:
    return {field: True for field in OMISSION_POSTURE_FIELDS}


def _identity_request_values() -> dict[str, Any]:
    return {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "selected_receiver_attestation_operation_id": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
        ),
        "selected_receiver_attestation_operation_type": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
        ),
        "selected_receiver_attestation_operation_version": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
        ),
        "selected_receiver_attestation_operation_scope": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE
        ),
        "selected_receiver_attestation_operation_result_required": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "governing_receiver_answerable_receipt_boundary_specification_path": (
            str(GOVERNING_SPECIFICATION_RELATIVE_PATH)
        ),
        "selected_receiver_attestation_operation_artifact_path": str(
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    }


def _new_canonical_request() -> dict[str, Any]:
    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **_identity_request_values(),
        "receiver_answerable_receipt_consideration_selected": True,
        "declared_non_claims": _canonical_non_claims(),
    }
    request.update({field: False for field in PROHIBITED_REQUEST_FLAGS})
    return request


def build_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_request(
) -> dict[str, Any]:
    """Return one fresh canonical selected receipt-consideration request."""
    return _new_canonical_request()


def build_declared_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Return one fresh request with every override left visible."""
    request = _new_canonical_request()
    request.update(copy.deepcopy(overrides))
    return request


def _canonical_request_keys() -> set[str]:
    return {
        "intent",
        *_identity_request_values(),
        "receiver_answerable_receipt_consideration_selected",
        "declared_non_claims",
        *PROHIBITED_REQUEST_FLAGS,
    }


def _direct_preclaim_fields() -> set[str]:
    return {
        "outcome",
        "boundary_result",
        "decision_code",
        "decision_reason",
        "receiver_answerable_receipt_boundary_recorded",
        "receiver_answerable_receipt_boundary_result_recorded",
        "receiver_answerable_receipt_consideration_allowed",
        "receiver_answerable_receipt_consideration_not_allowed",
        "receiver_answerable_receipt_boundary_exhausted",
        *REQUIRED_FALSE_NON_CLAIMS,
    }


def _as_repo_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_text(value: Path | str) -> tuple[str | None, str | None]:
    try:
        path = _as_repo_path(value)
        if not path.is_file():
            return None, "not_a_file"
        return path.read_text(encoding="utf-8"), None
    except (OSError, TypeError, UnicodeError, ValueError):
        return None, "unreadable"


def _read_json(value: Path | str) -> tuple[Any | None, str | None]:
    text, error = _read_text(value)
    if error is not None or text is None:
        return None, error
    try:
        return (
            json.loads(text, object_pairs_hook=_reject_duplicate_json_keys),
            None,
        )
    except _DuplicateJsonKeyError:
        return None, "duplicate_key"
    except (TypeError, ValueError, json.JSONDecodeError):
        return None, "not_parseable"


def _check(
    name: str,
    passed: bool,
    code: str | None = None,
    *,
    expected: Any = None,
    actual: Any = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {"name": name, "passed": passed}
    if expected is not None:
        item["expected"] = copy.deepcopy(expected)
    if actual is not None:
        item["actual"] = copy.deepcopy(actual)
    if not passed and code is not None:
        item["failure_code"] = code
        item["block_code"] = code
    return item


def _require(
    checks: list[dict[str, Any]],
    name: str,
    condition: bool,
    code: str,
    reason: str,
    *,
    expected: Any = None,
    actual: Any = None,
) -> tuple[str | None, str | None]:
    checks.append(
        _check(
            name,
            condition,
            code,
            expected=expected,
            actual=actual,
        )
    )
    return (None, None) if condition else (code, reason)


def _add_failure(
    checks: list[dict[str, Any]],
    name: str,
    code: str,
) -> None:
    checks.append(_check(name, False, code))


def _non_claims_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_FALSE_NON_CLAIMS)
        and all(value.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS)
    )


def _omission_posture_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(OMISSION_POSTURE_FIELDS)
        and all(value.get(field) is True for field in OMISSION_POSTURE_FIELDS)
    )


def _validate_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    if request.get("intent") == INTENT_BLOCK:
        _add_failure(checks, "request.intent", "EXPLICIT_BLOCK_REQUESTED")
        return (
            "EXPLICIT_BLOCK_REQUESTED",
            "explicit block intent was requested",
        )
    if request.get("intent") not in SUPPORTED_INTENTS:
        _add_failure(checks, "request.intent", "UNSUPPORTED_INTENT")
        return "UNSUPPORTED_INTENT", "request intent is unsupported"
    checks.append(_check("request.intent", True))

    direct_preclaims = set(request).intersection(_direct_preclaim_fields())
    if direct_preclaims:
        _add_failure(
            checks,
            "request.direct_result_preclaim",
            "RESULT_POSTURE_PRECLAIMED",
        )
        return (
            "RESULT_POSTURE_PRECLAIMED",
            "caller supplied a direct result or downstream posture",
        )

    canonical_keys = _canonical_request_keys()
    missing = canonical_keys.difference(request)
    if missing:
        _add_failure(checks, "request.schema", "REQUEST_FIELD_MISSING")
        return "REQUEST_FIELD_MISSING", "canonical request fields are missing"
    unknown = set(request).difference(canonical_keys)
    if unknown:
        _add_failure(checks, "request.schema", "REQUEST_UNKNOWN_FIELD")
        return (
            "REQUEST_UNKNOWN_FIELD",
            "declared request contains unknown fields",
        )
    checks.append(_check("request.schema", True))

    for field, expected in _identity_request_values().items():
        actual = request.get(field)
        code, reason = _require(
            checks,
            "request." + field,
            actual == expected,
            "REQUEST_VALUE_MISMATCH",
            field + " does not match the canonical request",
            expected=expected,
            actual=actual,
        )
        if code is not None:
            return code, reason

    selection = request.get(
        "receiver_answerable_receipt_consideration_selected"
    )
    code, reason = _require(
        checks,
        "request.receiver_answerable_receipt_consideration_selected",
        type(selection) is bool,
        "REQUEST_BOOLEAN_REQUIRED",
        "receipt-consideration selection must be an exact Boolean",
        expected="boolean",
        actual=selection,
    )
    if code is not None:
        return code, reason

    if not _non_claims_valid(request.get("declared_non_claims")):
        _add_failure(
            checks,
            "request.declared_non_claims",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return (
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared non-claims must be the exact canonical false set",
        )
    checks.append(_check("request.declared_non_claims", True))

    for field, block_code in PROHIBITED_REQUEST_FLAGS.items():
        actual = request.get(field)
        valid = type(actual) is bool and actual is False
        code, reason = _require(
            checks,
            "request." + field,
            valid,
            block_code,
            field + " must remain exact Boolean false",
            expected=False,
            actual=actual,
        )
        if code is not None:
            return code, reason
    return None, None


def _empty_specification_validation(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "specification_path": request.get(
            "governing_receiver_answerable_receipt_boundary_specification_path"
        ),
        "marker_validation": {
            family: False for family in SPEC_MARKER_FAMILIES
        },
        "specification_validated": False,
    }


def _validate_specification(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_specification_validation(request)
    text, error = _read_text(
        request[
            "governing_receiver_answerable_receipt_boundary_specification_path"
        ]
    )
    if error is not None or text is None:
        _add_failure(
            checks,
            "specification.reference",
            "RECEIPT_BOUNDARY_SPEC_REFERENCE_MISSING",
        )
        return (
            "RECEIPT_BOUNDARY_SPEC_REFERENCE_MISSING",
            "governing receipt-boundary specification is unavailable",
            validation,
        )
    checks.append(_check("specification.reference", True))
    for family, markers in SPEC_MARKER_FAMILIES.items():
        valid = all(marker in text for marker in markers)
        validation["marker_validation"][family] = valid
        code, reason = _require(
            checks,
            "specification." + family,
            valid,
            "RECEIPT_BOUNDARY_SPEC_MARKER_MISSING",
            "governing specification marker family is incomplete: " + family,
        )
        if code is not None:
            return code, reason, validation
    validation["specification_validated"] = True
    return None, None, validation


def _empty_upstream_validation(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "selected_upstream_artifact_path": request.get(
            "selected_receiver_attestation_operation_artifact_path"
        ),
        "artifact_validated": False,
        "exact_recorded_result_validated": False,
        "result_cardinality_validated": False,
        "operation_completed_and_exhausted": False,
        "receiver_attestation_recorded": False,
        "upstream_false_locks_validated": False,
        "source_bodies_not_read": True,
        "complete_material_not_embedded": True,
        "metadata": {},
        "selected_operation_identity": {},
        "selected_candidate_identity": {},
        "result_standing": {},
        "true_posture_validation": {
            field: False for field in REQUIRED_UPSTREAM_TRUE_POSTURES
        },
        "false_lock_validation": {
            field: False for field in REQUIRED_UPSTREAM_FALSE_POSTURES
        },
    }


def _upstream_true_values(
    artifact: Mapping[str, Any],
    operation: Mapping[str, Any],
) -> dict[str, Any]:
    non_meaning = artifact.get(
        "receiver_side_answerable_basis_"
        "receiver_attestation_operation_non_meaning"
    )
    components = artifact.get("bounded_component_validation")
    summary = artifact.get(
        "receiver_side_answerable_basis_"
        "receiver_attestation_operation_summary"
    )
    non_meaning = non_meaning if isinstance(non_meaning, Mapping) else {}
    components = components if isinstance(components, Mapping) else {}
    summary = summary if isinstance(summary, Mapping) else {}
    return {
        "operation_basis_supplied": operation.get("operation_basis_supplied"),
        "operation_basis_admitted": operation.get("operation_basis_admitted"),
        "receiver_attestation_operation_recorded": operation.get(
            "receiver_attestation_operation_recorded"
        ),
        "receiver_attestation_operation_result_recorded": operation.get(
            "receiver_attestation_operation_result_recorded"
        ),
        "receiver_attestation_operation_exhausted": operation.get(
            "receiver_attestation_operation_exhausted"
        ),
        "receiver_attestation_decided": operation.get(
            "receiver_attestation_decided"
        ),
        "receiver_attestation_recorded": operation.get(
            "receiver_attestation_recorded"
        ),
        "operation_result_present": non_meaning.get(
            "operation_result_present"
        ),
        "minimum_admission_checks_passed": components.get(
            "minimum_admission_checks_passed"
        ),
        "archive_correspondence_validated": summary.get(
            "archive_correspondence_validated"
        ),
        "text_components_validated": summary.get(
            "text_components_validated"
        ),
        "timestamp_validated": summary.get("timestamp_validated"),
        "trace_paths_validated": summary.get("trace_paths_validated"),
        "recorded_signal_artifact_existence_validated": summary.get(
            "recorded_signal_artifact_existence_validated"
        ),
        "result_level_non_claims_canonical_false": summary.get(
            "result_level_non_claims_canonical_false"
        ),
    }


def _validate_upstream_artifact(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    validation = _empty_upstream_validation(request)
    artifact, error = _read_json(
        request["selected_receiver_attestation_operation_artifact_path"]
    )
    if error in {"not_a_file", "unreadable"}:
        _add_failure(
            checks,
            "upstream.reference",
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_MISSING",
        )
        return (
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_MISSING",
            "selected receiver-attestation operation artifact is unavailable",
            validation,
        )
    if error == "duplicate_key":
        _add_failure(
            checks,
            "upstream.strict_json",
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_DUPLICATE_KEYED",
        )
        return (
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_DUPLICATE_KEYED",
            "selected upstream artifact contains duplicate JSON keys",
            validation,
        )
    if error == "not_parseable":
        _add_failure(
            checks,
            "upstream.strict_json",
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_NOT_PARSEABLE",
        )
        return (
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_NOT_PARSEABLE",
            "selected upstream artifact is not parseable JSON",
            validation,
        )
    if not isinstance(artifact, Mapping):
        _add_failure(
            checks,
            "upstream.mapping",
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_NOT_MAPPING",
        )
        return (
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_NOT_MAPPING",
            "selected upstream artifact is not a mapping",
            validation,
        )
    checks.append(_check("upstream.strict_json_mapping", True))

    operation = artifact.get(
        "receiver_side_answerable_basis_receiver_attestation_operation"
    )
    selected_identity = artifact.get(
        "selected_operation_and_candidate_identity"
    )
    result_detail = artifact.get("operation_result_detail")
    operation_posture = artifact.get("operation_posture")
    summary = artifact.get(
        "receiver_side_answerable_basis_"
        "receiver_attestation_operation_summary"
    )
    block = artifact.get("block")
    if not all(
        isinstance(value, Mapping)
        for value in (
            operation,
            selected_identity,
            result_detail,
            operation_posture,
            summary,
            block,
        )
    ):
        _add_failure(
            checks,
            "upstream.required_sections",
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_NOT_MAPPING",
        )
        return (
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_NOT_MAPPING",
            "selected upstream artifact lacks canonical bounded sections",
            validation,
        )
    checks.append(_check("upstream.required_sections", True))

    metadata_expectations = {
        "resolver_module": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESOLVER_MODULE
        ),
        "result_version": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_VERSION
        ),
        "outcome": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_OUTCOME_REQUIRED
        ),
        "failed_check_count": 0,
        "passed_check_count": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_PASSED_CHECK_COUNT
        ),
    }
    validation["metadata"] = {
        field: artifact.get(field) for field in metadata_expectations
    }
    for field, expected in metadata_expectations.items():
        actual = artifact.get(field)
        if field in {"failed_check_count", "passed_check_count"}:
            valid = type(actual) is int and actual == expected
            failure_code = (
                "UPSTREAM_FAILED_CHECKS_PRESENT"
                if field == "failed_check_count"
                else "UPSTREAM_METADATA_MISMATCH"
            )
        else:
            valid = actual == expected
            failure_code = "UPSTREAM_METADATA_MISMATCH"
        code, reason = _require(
            checks,
            "upstream." + field,
            valid,
            failure_code,
            "selected upstream metadata does not match " + field,
            expected=expected,
            actual=actual,
        )
        if code is not None:
            return code, reason, validation

    blocked = block.get("blocked")
    summary_blocked = summary.get("blocked")
    valid_not_blocked = (
        type(blocked) is bool
        and blocked is False
        and type(summary_blocked) is bool
        and summary_blocked is False
    )
    code, reason = _require(
        checks,
        "upstream.blocked",
        valid_not_blocked,
        "UPSTREAM_BLOCKED",
        "selected upstream artifact is blocked or lacks exact false posture",
        expected=False,
        actual=blocked,
    )
    if code is not None:
        return code, reason, validation

    operation_identity = {
        "operation_id": SELECTED_RECEIVER_ATTESTATION_OPERATION_ID,
        "operation_type": SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE,
        "operation_version": SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION,
        "operation_scope": SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE,
        (
            "receiver_side_answerable_basis_"
            "receiver_attestation_operation_id"
        ): SELECTED_RECEIVER_ATTESTATION_OPERATION_ID,
        (
            "receiver_side_answerable_basis_"
            "receiver_attestation_operation_type"
        ): SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE,
        (
            "receiver_side_answerable_basis_"
            "receiver_attestation_operation_version"
        ): SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION,
        (
            "receiver_side_answerable_basis_"
            "receiver_attestation_operation_scope"
        ): SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE,
    }
    validation["selected_operation_identity"] = {
        field: operation.get(field) for field in operation_identity
    }
    for field, expected in operation_identity.items():
        actual = operation.get(field)
        code, reason = _require(
            checks,
            "upstream.operation_identity." + field,
            actual == expected,
            "UPSTREAM_OPERATION_IDENTITY_MISMATCH",
            "selected operation identity does not match " + field,
            expected=expected,
            actual=actual,
        )
        if code is not None:
            return code, reason, validation

    selected_identity_expectations = {
        "operation_id": SELECTED_RECEIVER_ATTESTATION_OPERATION_ID,
        "operation_type": SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE,
        "operation_version": SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION,
        "operation_scope": SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE,
        "selected_candidate_id": CANDIDATE_ID,
        "selected_candidate_type": CANDIDATE_TYPE,
        "selected_candidate_scope": CANDIDATE_SCOPE,
    }
    for field, expected in selected_identity_expectations.items():
        actual = selected_identity.get(field)
        failure_code = (
            "UPSTREAM_CANDIDATE_IDENTITY_MISMATCH"
            if field.startswith("selected_candidate_")
            else "UPSTREAM_OPERATION_IDENTITY_MISMATCH"
        )
        code, reason = _require(
            checks,
            "upstream.selected_identity." + field,
            actual == expected,
            failure_code,
            "selected identity does not match " + field,
            expected=expected,
            actual=actual,
        )
        if code is not None:
            return code, reason, validation

    candidate_identity = {
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
    }
    validation["selected_candidate_identity"] = {
        field: operation.get(field) for field in candidate_identity
    }
    for field, expected in candidate_identity.items():
        actual = operation.get(field)
        code, reason = _require(
            checks,
            "upstream.candidate_identity." + field,
            actual == expected,
            "UPSTREAM_CANDIDATE_IDENTITY_MISMATCH",
            "selected candidate identity does not match " + field,
            expected=expected,
            actual=actual,
        )
        if code is not None:
            return code, reason, validation

    result_expectations = {
        "operation_result_detail.operation_result": (
            result_detail.get("operation_result")
        ),
        "operation.operation_result": operation.get(
            "receiver_attestation_operation_result"
        ),
        "summary.operation_result": summary.get("operation_result"),
    }
    for name, actual in result_expectations.items():
        code, reason = _require(
            checks,
            "upstream." + name,
            actual
            == SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED,
            "UPSTREAM_RESULT_MISMATCH",
            "selected upstream result does not record exact RECORDED posture",
            expected=(
                SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
            ),
            actual=actual,
        )
        if code is not None:
            return code, reason, validation

    count = result_detail.get("completed_result_posture_count")
    code, reason = _require(
        checks,
        "upstream.completed_result_posture_count",
        type(count) is int and count == 1,
        "UPSTREAM_RESULT_CARDINALITY_MISMATCH",
        "exactly one completed attestation result must stand",
        expected=1,
        actual=count,
    )
    if code is not None:
        return code, reason, validation

    posture_aliases = {
        "operation_recorded": True,
        "operation_result_recorded": True,
        "operation_exhausted": True,
        "receiver_attestation_decided": True,
    }
    for field, expected in posture_aliases.items():
        actual = operation_posture.get(field)
        code, reason = _require(
            checks,
            "upstream.operation_posture." + field,
            type(actual) is bool and actual is expected,
            "UPSTREAM_TRUE_POSTURE_NOT_TRUE",
            "completed operation posture is not exact true: " + field,
            expected=expected,
            actual=actual,
        )
        if code is not None:
            return code, reason, validation

    true_values = _upstream_true_values(artifact, operation)
    for field in REQUIRED_UPSTREAM_TRUE_POSTURES:
        actual = true_values.get(field)
        valid = type(actual) is bool and actual is True
        validation["true_posture_validation"][field] = valid
        code, reason = _require(
            checks,
            "upstream.true_posture." + field,
            valid,
            "UPSTREAM_TRUE_POSTURE_NOT_TRUE",
            "required upstream posture is not exact true: " + field,
            expected=True,
            actual=actual,
        )
        if code is not None:
            return code, reason, validation

    for field in REQUIRED_UPSTREAM_FALSE_POSTURES:
        actual = operation.get(field)
        valid = type(actual) is bool and actual is False
        validation["false_lock_validation"][field] = valid
        code, reason = _require(
            checks,
            "upstream.false_lock." + field,
            valid,
            "UPSTREAM_FALSE_LOCK_NOT_FALSE",
            "required upstream false lock is missing or not false: " + field,
            expected=False,
            actual=actual,
        )
        if code is not None:
            return code, reason, validation

    upstream_non_claims = artifact.get("non_claims")
    valid_upstream_non_claims = (
        isinstance(upstream_non_claims, Mapping)
        and bool(upstream_non_claims)
        and all(value is False for value in upstream_non_claims.values())
    )
    code, reason = _require(
        checks,
        "upstream.result_level_non_claims",
        valid_upstream_non_claims,
        "UPSTREAM_NON_CLAIMS_NOT_CANONICAL_FALSE",
        "upstream result-level non-claims are not canonical false",
    )
    if code is not None:
        return code, reason, validation

    validation["result_standing"] = {
        "operation_result": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
        ),
        "completed_result_posture_count": 1,
        "receiver_attestation_recorded": True,
        "receiver_attestation_not_recorded": False,
        "receiver_attestation_indeterminate": False,
    }
    validation["exact_recorded_result_validated"] = True
    validation["result_cardinality_validated"] = True
    validation["operation_completed_and_exhausted"] = True
    validation["receiver_attestation_recorded"] = True
    validation["upstream_false_locks_validated"] = True
    validation["artifact_validated"] = True
    return None, None, validation


def _boundary_result_for_outcome(outcome: str) -> str:
    if outcome == OUTCOME_ALLOWED:
        return RESULT_ALLOWED
    if outcome == OUTCOME_NOT_ALLOWED:
        return RESULT_NOT_ALLOWED
    return RESULT_NOT_EVALUATED


def _decision_for_outcome(outcome: str) -> dict[str, Any]:
    if outcome == OUTCOME_ALLOWED:
        return {
            "decision_code": DECISION_CODE_ALLOWED,
            "decision_reason": DECISION_REASON_ALLOWED,
        }
    if outcome == OUTCOME_NOT_ALLOWED:
        return {
            "decision_code": DECISION_CODE_NOT_ALLOWED,
            "decision_reason": DECISION_REASON_NOT_ALLOWED,
        }
    return {"decision_code": None, "decision_reason": None}


def _boundary_object(
    outcome: str,
    request: Mapping[str, Any],
) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    not_allowed = outcome == OUTCOME_NOT_ALLOWED
    completed = allowed or not_allowed
    return {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_id"
        ): BOUNDARY_ID,
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_type"
        ): BOUNDARY_TYPE,
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_version"
        ): BOUNDARY_VERSION,
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_scope"
        ): BOUNDARY_SCOPE,
        "selected_receiver_attestation_operation_id": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
        ),
        "selected_receiver_attestation_operation_type": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
        ),
        "selected_receiver_attestation_operation_version": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
        ),
        "selected_receiver_attestation_operation_scope": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE
        ),
        "selected_receiver_attestation_operation_result_required": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "receiver_answerable_receipt_consideration_selected": (
            request.get(
                "receiver_answerable_receipt_consideration_selected"
            )
            if completed
            else False
        ),
        "receiver_answerable_receipt_boundary_recorded": completed,
        "receiver_answerable_receipt_boundary_result_recorded": completed,
        "receiver_answerable_receipt_consideration_allowed": allowed,
        "receiver_answerable_receipt_consideration_not_allowed": not_allowed,
        "receiver_answerable_receipt_boundary_exhausted": completed,
        "receiver_answerable_receipt_boundary_result": (
            _boundary_result_for_outcome(outcome)
        ),
        **_canonical_non_claims(),
    }


def _declared_request_posture(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "intent": request.get("intent"),
        **{
            field: copy.deepcopy(request.get(field))
            for field in _identity_request_values()
        },
        "receiver_answerable_receipt_consideration_selected": request.get(
            "receiver_answerable_receipt_consideration_selected"
        ),
        "declared_non_claims_validated": _non_claims_valid(
            request.get("declared_non_claims")
        ),
        "prohibited_request_flags_validated": all(
            request.get(field) is False for field in PROHIBITED_REQUEST_FLAGS
        ),
    }


def _statement(outcome: str) -> dict[str, bool]:
    completed = outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
    return {
        "one_exact_completed_receiver_attestation_operation_consumed": (
            completed
        ),
        "receiver_attestation_operation_not_reopened": True,
        "candidate_sufficiency_not_re_evaluated": True,
        "receiver_attestation_not_re_evaluated": True,
        "receiver_answerable_receipt_consideration_only": completed,
        "receiver_answerable_receipt_not_created": True,
        "receipt_operation_not_created_or_executed": True,
        "presence_re_evaluation_not_created": True,
        "boundary_single_use": completed,
        "boundary_exhausted_only_after_completed_result": completed,
        "result_level_non_claims_canonical_false": True,
        "open_does_not_mean_next": True,
    }


def _non_meaning() -> dict[str, bool]:
    return {
        "receiver_attestation_recorded_is_not_receiver_answerable_receipt": (
            True
        ),
        "receipt_consideration_allowed_is_not_receipt": True,
        "receipt_is_not_presence": True,
        "receipt_boundary_is_not_receipt_operation": True,
        "completed_boundary_result_is_not_downstream_authorization": True,
        "selected_upstream_result_is_not_independently_re_evaluated": True,
        "source_bodies_were_not_read": True,
        "open_does_not_mean_next": True,
        "not_allowed_is_not_attestation_falsity": True,
        "not_allowed_is_not_receiver_dishonesty": True,
        "not_allowed_is_not_occurrence_denial": True,
        "not_allowed_is_not_candidate_insufficiency": True,
        "not_allowed_is_not_operation_failure": True,
        "not_allowed_is_not_receipt_refusal": True,
        "not_allowed_is_not_presence_denial": True,
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_boundary"
    )
    boundary = boundary if isinstance(boundary, Mapping) else {}
    specification = result.get("specification_validation")
    specification = (
        specification if isinstance(specification, Mapping) else {}
    )
    upstream = result.get("upstream_artifact_validation")
    upstream = upstream if isinstance(upstream, Mapping) else {}
    decision = result.get("boundary_decision")
    decision = decision if isinstance(decision, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    omission = result.get("omission_posture")
    omission = omission if isinstance(omission, Mapping) else {}
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "boundary_id": boundary.get("boundary_id"),
        "boundary_type": boundary.get("boundary_type"),
        "boundary_version": boundary.get("boundary_version"),
        "boundary_scope": boundary.get("boundary_scope"),
        "selected_receiver_attestation_operation_id": boundary.get(
            "selected_receiver_attestation_operation_id"
        ),
        "selected_candidate_id": boundary.get(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "selected_upstream_artifact_path": str(
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
        "outcome": result.get("outcome"),
        "boundary_result": result.get("boundary_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": block.get("blocked"),
        "decision_code": decision.get("decision_code"),
        "decision_reason": decision.get("decision_reason"),
        "selection": boundary.get(
            "receiver_answerable_receipt_consideration_selected"
        ),
        "specification_validated": specification.get(
            "specification_validated"
        ),
        "upstream_artifact_validated": upstream.get("artifact_validated"),
        "exact_recorded_result_validated": upstream.get(
            "exact_recorded_result_validated"
        ),
        "result_cardinality_validated": upstream.get(
            "result_cardinality_validated"
        ),
        "upstream_false_locks_validated": upstream.get(
            "upstream_false_locks_validated"
        ),
        "operation_completed_and_exhausted": upstream.get(
            "operation_completed_and_exhausted"
        ),
        "receiver_attestation_recorded": upstream.get(
            "receiver_attestation_recorded"
        ),
        "boundary_recorded": boundary.get(
            "receiver_answerable_receipt_boundary_recorded"
        ),
        "boundary_result_recorded": boundary.get(
            "receiver_answerable_receipt_boundary_result_recorded"
        ),
        "boundary_exhausted": boundary.get(
            "receiver_answerable_receipt_boundary_exhausted"
        ),
        "consideration_allowed": boundary.get(
            "receiver_answerable_receipt_consideration_allowed"
        ),
        "consideration_not_allowed": boundary.get(
            "receiver_answerable_receipt_consideration_not_allowed"
        ),
        "receipt_absent": (
            boundary.get("receiver_answerable_receipt_present") is False
        ),
        "receipt_operation_absent": (
            boundary.get("receiver_answerable_receipt_operation_created")
            is False
            and boundary.get(
                "receiver_answerable_receipt_operation_executed"
            )
            is False
        ),
        "presence_absent": (
            boundary.get("presence_supported") is False
            and boundary.get("presence_authorized") is False
            and boundary.get("presence_established") is False
            and boundary.get("presence_recorded") is False
        ),
        "downstream_non_claims_canonical_false": _non_claims_valid(
            result.get("non_claims")
        ),
        "result_level_non_claims_canonical_false": result.get(
            "result_level_non_claims_canonical_false"
        ),
        "complete_material_omission_posture": (
            bool(omission)
            and all(value is True for value in omission.values())
        ),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    }


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    *,
    specification_validation: Mapping[str, Any] | None = None,
    upstream_validation: Mapping[str, Any] | None = None,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    specification = (
        copy.deepcopy(dict(specification_validation))
        if isinstance(specification_validation, Mapping)
        else _empty_specification_validation(request)
    )
    upstream = (
        copy.deepcopy(dict(upstream_validation))
        if isinstance(upstream_validation, Mapping)
        else _empty_upstream_validation(request)
    )
    boundary = _boundary_object(outcome, request)
    boundary_result = _boundary_result_for_outcome(outcome)
    decision = _decision_for_outcome(outcome)
    if outcome == OUTCOME_BLOCKED:
        decision = {
            "decision_code": code,
            "decision_reason": reason,
        }
    allowed = outcome == OUTCOME_ALLOWED
    not_allowed = outcome == OUTCOME_NOT_ALLOWED
    completed = allowed or not_allowed
    result: dict[str, Any] = {
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_metadata"
        ): {
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
            "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
            "selected_upstream_artifact_path": str(
                SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
            ),
        },
        "selected_operation_and_candidate_identity": {
            "selected_receiver_attestation_operation_id": (
                SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
            ),
            "selected_receiver_attestation_operation_type": (
                SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
            ),
            "selected_receiver_attestation_operation_version": (
                SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
            ),
            "selected_receiver_attestation_operation_scope": (
                SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE
            ),
            "selected_receiver_attestation_operation_result_required": (
                SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
            ),
            "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
            "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
            "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        },
        "declared_request_posture": _declared_request_posture(request),
        "specification_validation": specification,
        "upstream_artifact_validation": upstream,
        "compact_upstream_standing": {
            "metadata": copy.deepcopy(upstream.get("metadata", {})),
            "selected_operation_identity": copy.deepcopy(
                upstream.get("selected_operation_identity", {})
            ),
            "selected_candidate_identity": copy.deepcopy(
                upstream.get("selected_candidate_identity", {})
            ),
            "result_standing": copy.deepcopy(
                upstream.get("result_standing", {})
            ),
            "artifact_validated": upstream.get("artifact_validated") is True,
            "source_bodies_not_read": True,
            "complete_material_not_embedded": True,
        },
        "boundary_decision": {
            **decision,
            "selection": (
                request.get(
                    "receiver_answerable_receipt_consideration_selected"
                )
                if completed
                else False
            ),
        },
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": code if outcome == OUTCOME_BLOCKED else None,
            "block_code": code if outcome == OUTCOME_BLOCKED else None,
            "reason": reason if outcome == OUTCOME_BLOCKED else None,
        },
        "boundary_posture": {
            "receiver_answerable_receipt_boundary_recorded": completed,
            "receiver_answerable_receipt_boundary_result_recorded": completed,
            "receiver_answerable_receipt_consideration_allowed": allowed,
            "receiver_answerable_receipt_consideration_not_allowed": (
                not_allowed
            ),
            "receiver_answerable_receipt_boundary_exhausted": completed,
            "completed_consideration_posture_count": sum(
                (allowed, not_allowed)
            ),
            "single_use_only": True,
        },
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary"
        ): boundary,
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_checks"
        ): copy.deepcopy(checks),
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_statement"
        ): _statement(outcome),
        (
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_non_meaning"
        ): _non_meaning(),
        "omission_posture": _canonical_omission_posture(),
        "blocked_routes": list(BLOCKED_ROUTES),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "result_level_non_claims_canonical_false": True,
        "outcome": outcome,
        "boundary_result": boundary_result,
        "failed_check_count": sum(
            check.get("passed") is False for check in checks
        ),
        "passed_check_count": sum(
            check.get("passed") is True for check in checks
        ),
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
    }
    result[
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_boundary_summary"
    ] = _summary_from_result(result)
    return result


def resolve_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one exact receipt-consideration boundary without side effects."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared_request = _new_canonical_request()
    elif not isinstance(request, Mapping):
        declared_request = _new_canonical_request()
        _add_failure(checks, "request.mapping", "REQUEST_NOT_MAPPING")
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="declared request is not a mapping",
        )
    else:
        declared_request = copy.deepcopy(dict(request))

    code, reason = _validate_request(declared_request, checks)
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            code=code,
            reason=reason,
        )

    code, reason, specification = _validate_specification(
        declared_request,
        checks,
    )
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            specification_validation=specification,
            code=code,
            reason=reason,
        )

    code, reason, upstream = _validate_upstream_artifact(
        declared_request,
        checks,
    )
    if code is not None:
        return _build_result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            specification_validation=specification,
            upstream_validation=upstream,
            code=code,
            reason=reason,
        )

    selected = declared_request[
        "receiver_answerable_receipt_consideration_selected"
    ]
    checks.append(
        _check(
            "decision.receipt_consideration_selection",
            True,
            expected=selected,
            actual=selected,
        )
    )
    outcome = OUTCOME_ALLOWED if selected else OUTCOME_NOT_ALLOWED
    return _build_result(
        declared_request,
        outcome,
        checks,
        specification_validation=specification,
        upstream_validation=upstream,
    )


def resolve_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Strictly load one request path and resolve it without discovery."""
    payload, error = _read_json(request_path)
    if error is not None:
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
            "invalid request path JSON: " + error
        )
    if not isinstance(payload, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
            "invalid request path JSON: top-level value must be a mapping"
        )
    return (
        resolve_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min(
            payload
        )
    )


def build_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic summary without complete materials."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
            "summary requires a result mapping"
        )
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
        or set(result) != RESULT_SECTIONS
        or not _branch_valid(result)
        or not _checks_valid(result)
        or not _supporting_sections_valid(result)
        or not _non_claims_valid(result.get("non_claims"))
        or result.get("result_level_non_claims_canonical_false") is not True
        or not _omission_posture_valid(result.get("omission_posture"))
        or _contains_prohibited_complete_material(result)
    ):
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
            "summary requires a compatible resolver result"
        )
    return _summary_from_result(result)


def _contains_prohibited_complete_material(value: Any) -> bool:
    forbidden_keys = {
        "selected_upstream_operation_artifact",
        "complete_selected_upstream_operation_artifact",
        "complete_upstream_artifact",
        "complete_operation_basis",
        "supplied_operation_basis",
        "sufficiency_basis_records",
        "basis_items",
        "basis_references",
        "complete_candidate_sufficiency_artifact",
        "complete_candidate_sufficiency_basis",
        "complete_receiver_attestation_boundary_artifact",
        "archive_bytes",
        "archive_body",
        "hash_record_body",
        "text_component_bodies",
        "recorded_signal_body",
        "capture_signal_data",
        "signal_samples",
        "raw_signal_data",
    }
    if isinstance(value, Mapping):
        return any(
            key in forbidden_keys
            or _contains_prohibited_complete_material(nested)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(
        value,
        (str, bytes, bytearray),
    ):
        return any(
            _contains_prohibited_complete_material(item) for item in value
        )
    return False


def _branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    boundary_result = result.get("boundary_result")
    boundary = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_boundary"
    )
    posture = result.get("boundary_posture")
    block = result.get("block")
    decision = result.get("boundary_decision")
    if (
        outcome not in OUTCOME_FAMILY
        or not isinstance(boundary, Mapping)
        or not isinstance(posture, Mapping)
        or not isinstance(block, Mapping)
        or not isinstance(decision, Mapping)
    ):
        return False
    common = (
        boundary.get("boundary_id") == BOUNDARY_ID
        and boundary.get("boundary_type") == BOUNDARY_TYPE
        and boundary.get("boundary_version") == BOUNDARY_VERSION
        and boundary.get("boundary_scope") == BOUNDARY_SCOPE
        and all(
            boundary.get(field) is False
            for field in REQUIRED_FALSE_NON_CLAIMS
        )
    )
    if not common:
        return False
    allowed = boundary.get(
        "receiver_answerable_receipt_consideration_allowed"
    )
    not_allowed = boundary.get(
        "receiver_answerable_receipt_consideration_not_allowed"
    )
    recorded = boundary.get("receiver_answerable_receipt_boundary_recorded")
    result_recorded = boundary.get(
        "receiver_answerable_receipt_boundary_result_recorded"
    )
    exhausted = boundary.get(
        "receiver_answerable_receipt_boundary_exhausted"
    )
    embedded_result = boundary.get(
        "receiver_answerable_receipt_boundary_result"
    )
    count = posture.get("completed_consideration_posture_count")
    mirrored = (
        posture.get("receiver_answerable_receipt_boundary_recorded")
        is recorded
        and posture.get(
            "receiver_answerable_receipt_boundary_result_recorded"
        )
        is result_recorded
        and posture.get(
            "receiver_answerable_receipt_consideration_allowed"
        )
        is allowed
        and posture.get(
            "receiver_answerable_receipt_consideration_not_allowed"
        )
        is not_allowed
        and posture.get("receiver_answerable_receipt_boundary_exhausted")
        is exhausted
        and posture.get("single_use_only") is True
    )
    if not mirrored:
        return False
    if outcome == OUTCOME_ALLOWED:
        return (
            boundary_result == RESULT_ALLOWED
            and embedded_result == RESULT_ALLOWED
            and allowed is True
            and not_allowed is False
            and recorded is True
            and result_recorded is True
            and exhausted is True
            and count == 1
            and block.get("blocked") is False
            and block.get("code") is None
            and block.get("block_code") is None
            and block.get("reason") is None
            and decision.get("decision_code") == DECISION_CODE_ALLOWED
            and decision.get("decision_reason") == DECISION_REASON_ALLOWED
            and decision.get("selection") is True
        )
    if outcome == OUTCOME_NOT_ALLOWED:
        return (
            boundary_result == RESULT_NOT_ALLOWED
            and embedded_result == RESULT_NOT_ALLOWED
            and allowed is False
            and not_allowed is True
            and recorded is True
            and result_recorded is True
            and exhausted is True
            and count == 1
            and block.get("blocked") is False
            and block.get("code") is None
            and block.get("block_code") is None
            and block.get("reason") is None
            and decision.get("decision_code")
            == DECISION_CODE_NOT_ALLOWED
            and decision.get("decision_reason")
            == DECISION_REASON_NOT_ALLOWED
            and decision.get("selection") is False
        )
    return (
        boundary_result == RESULT_NOT_EVALUATED
        and embedded_result == RESULT_NOT_EVALUATED
        and allowed is False
        and not_allowed is False
        and recorded is False
        and result_recorded is False
        and exhausted is False
        and count == 0
        and block.get("blocked") is True
        and block.get("code") in BLOCK_CODES
        and block.get("block_code") == block.get("code")
        and isinstance(block.get("reason"), str)
        and bool(block.get("reason"))
        and decision.get("decision_code") == block.get("code")
        and decision.get("decision_reason") == block.get("reason")
        and decision.get("selection") is False
    )


def _checks_valid(result: Mapping[str, Any]) -> bool:
    checks = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_boundary_checks"
    )
    if not isinstance(checks, list):
        return False
    if not all(
        isinstance(check, Mapping) and type(check.get("passed")) is bool
        for check in checks
    ):
        return False
    failed = sum(check.get("passed") is False for check in checks)
    passed = sum(check.get("passed") is True for check in checks)
    if (
        type(result.get("failed_check_count")) is not int
        or type(result.get("passed_check_count")) is not int
        or result.get("failed_check_count") != failed
        or result.get("passed_check_count") != passed
    ):
        return False
    for check in checks:
        for field in ("failure_code", "block_code"):
            if field in check and check[field] not in BLOCK_CODES:
                return False
    if result.get("outcome") in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}:
        return failed == 0
    return failed > 0


def _supporting_sections_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    metadata = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_boundary_metadata"
    )
    selected = result.get("selected_operation_and_candidate_identity")
    declared = result.get("declared_request_posture")
    specification = result.get("specification_validation")
    upstream = result.get("upstream_artifact_validation")
    compact = result.get("compact_upstream_standing")
    statement = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_boundary_statement"
    )
    non_meaning = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_boundary_non_meaning"
    )
    if not all(
        isinstance(value, Mapping)
        for value in (
            metadata,
            selected,
            declared,
            specification,
            upstream,
            compact,
            statement,
            non_meaning,
        )
    ):
        return False
    expected_metadata = {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "specification_path": str(GOVERNING_SPECIFICATION_RELATIVE_PATH),
        "selected_upstream_artifact_path": str(
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
    }
    expected_selected = {
        "selected_receiver_attestation_operation_id": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
        ),
        "selected_receiver_attestation_operation_type": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
        ),
        "selected_receiver_attestation_operation_version": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
        ),
        "selected_receiver_attestation_operation_scope": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE
        ),
        "selected_receiver_attestation_operation_result_required": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
    }
    if (
        dict(metadata) != expected_metadata
        or dict(selected) != expected_selected
        or dict(statement) != _statement(str(outcome))
        or dict(non_meaning) != _non_meaning()
        or result.get("blocked_routes") != list(BLOCKED_ROUTES)
        or result.get("what_remains_open") != list(WHAT_REMAINS_OPEN)
        or result.get("admissible_future_route") != ADMISSIBLE_FUTURE_ROUTE
        or compact.get("source_bodies_not_read") is not True
        or compact.get("complete_material_not_embedded") is not True
    ):
        return False

    completed = outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
    if completed:
        markers = specification.get("marker_validation")
        true_postures = upstream.get("true_posture_validation")
        false_locks = upstream.get("false_lock_validation")
        selection = declared.get(
            "receiver_answerable_receipt_consideration_selected"
        )
        expected_selection = outcome == OUTCOME_ALLOWED
        return (
            declared.get("declared_non_claims_validated") is True
            and declared.get("prohibited_request_flags_validated") is True
            and selection is expected_selection
            and specification.get("specification_validated") is True
            and isinstance(markers, Mapping)
            and bool(markers)
            and all(value is True for value in markers.values())
            and upstream.get("artifact_validated") is True
            and upstream.get("exact_recorded_result_validated") is True
            and upstream.get("result_cardinality_validated") is True
            and upstream.get("operation_completed_and_exhausted") is True
            and upstream.get("receiver_attestation_recorded") is True
            and upstream.get("upstream_false_locks_validated") is True
            and upstream.get("source_bodies_not_read") is True
            and upstream.get("complete_material_not_embedded") is True
            and isinstance(true_postures, Mapping)
            and set(true_postures) == set(REQUIRED_UPSTREAM_TRUE_POSTURES)
            and all(value is True for value in true_postures.values())
            and isinstance(false_locks, Mapping)
            and set(false_locks) == set(REQUIRED_UPSTREAM_FALSE_POSTURES)
            and all(value is True for value in false_locks.values())
            and compact.get("artifact_validated") is True
        )
    return outcome == OUTCOME_BLOCKED


def _result_valid_for_write(result: Mapping[str, Any]) -> bool:
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
        or set(result) != RESULT_SECTIONS
        or not _branch_valid(result)
        or not _checks_valid(result)
        or not _supporting_sections_valid(result)
        or not _non_claims_valid(result.get("non_claims"))
        or result.get("result_level_non_claims_canonical_false") is not True
        or not _omission_posture_valid(result.get("omission_posture"))
        or _contains_prohibited_complete_material(result)
    ):
        return False
    summary_key = (
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_boundary_summary"
    )
    return result.get(summary_key) == _summary_from_result(result)


def _path_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _output_path_allowed(path: Path) -> bool:
    try:
        resolved = path.resolve()
        repo = REPO_ROOT.resolve()
        canonical_output_root = CANONICAL_OUTPUT_ROOT.resolve()
        if _path_within(resolved, repo):
            return _path_within(resolved, canonical_output_root)
        return True
    except (OSError, RuntimeError, ValueError):
        return False


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(
            path.stem + "_" + f"{index:03d}" + path.suffix
        )
        if not candidate.exists():
            return candidate
    raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def write_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid result deterministically without overwriting."""
    if not isinstance(result, Mapping) or not _result_valid_for_write(result):
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
            "WRITE_REFUSED: malformed or inconsistent boundary result"
        )
    explicit = output_path is not None
    try:
        target = (
            _as_repo_path(output_path)
            if explicit
            else OUTPUT_ROOT / OUTPUT_FILENAME
        )
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
            "WRITE_REFUSED: invalid output path"
        ) from exc
    if not _output_path_allowed(target):
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
            "WRITE_REFUSED: output path is protected or outside the "
            "receipt-boundary output family"
        )
    if target.exists() and explicit:
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
            "WRITE_REFUSED: explicit output path already exists"
        )
    if target.is_dir():
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
            "WRITE_REFUSED: output path is a directory"
        )
    if not explicit:
        target = _next_available_output_path(target)
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as handle:
            json.dump(
                dict(result),
                handle,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError(
            "WRITE_REFUSED: unable to write boundary result"
        ) from exc
    return target
