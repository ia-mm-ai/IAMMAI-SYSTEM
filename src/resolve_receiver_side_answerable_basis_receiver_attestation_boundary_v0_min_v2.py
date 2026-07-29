"""Resolve the v2 bounded receiver-attestation consideration boundary.

The resolver consumes one completed sufficient candidate operation as upstream
standing.  It may record whether consideration is allowed; it never creates,
supports, validates, admits, or records receiver attestation.  V2 preserves
the v1 contract and closes its seven-field upstream false-lock omission.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from types import MappingProxyType
from typing import Any


RESULT_VERSION = "0.2.0"
RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2"
)

BOUNDARY_ID = "receiver_side_answerable_basis_receiver_attestation_boundary_001"
BOUNDARY_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = (
    "CONSIDER_RECEIVER_ATTESTATION_FOR_ONE_SUFFICIENT_"
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = (
    "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
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
SELECTED_SUFFICIENCY_BOUNDARY_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_boundary_001"
)
SELECTED_SUFFICIENCY_OPERATION_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001"
)
SELECTED_SUFFICIENCY_OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION"
)
SELECTED_SUFFICIENCY_OPERATION_VERSION = "0.1.0"
SELECTED_SUFFICIENCY_OPERATION_RESULT_VERSION = "0.1.0"
SELECTED_SUFFICIENCY_OPERATION_SCOPE = (
    "DECIDE_SUFFICIENCY_POSTURE_OF_ONE_SELECTED_"
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)
SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT"
)
SELECTED_SUFFICIENCY_OPERATION_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_RECORDED"
)
SELECTED_SUFFICIENCY_OPERATION_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min"
)

ADMISSIBLE_FUTURE_ROUTE = (
    "RECEIVER_ATTESTATION_BOUNDARY_THEN_SEPARATE_"
    "RECEIVER_ATTESTATION_OPERATION_OR_DECLARATION_ONLY"
)

REQUIRED_DIMENSION_IDS = (
    "receiver_answerability_fit",
    "selected_purpose_adequacy",
    "bounded_material_completeness",
    "unresolved_contradiction_posture",
    "unsupported_assumption_dependency",
    "scope_constrained_usability",
    "refusal_withholding_compatibility",
    "provenance_capture_limitation_posture",
)
DIMENSION_RESULT_SATISFIED = "SATISFIED"

OUTCOME_ALLOWED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY_ALLOWED"
)
OUTCOME_NOT_ALLOWED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY_NOT_ALLOWED"
)
OUTCOME_BLOCKED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED, OUTCOME_BLOCKED)
OUTCOME_RECORDED = OUTCOME_ALLOWED

BOUNDARY_RESULT_ALLOWED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_CONSIDERATION_ALLOWED"
)
BOUNDARY_RESULT_NOT_ALLOWED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_CONSIDERATION_NOT_ALLOWED"
)
BOUNDARY_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
BOUNDARY_RESULT_FAMILY = (
    BOUNDARY_RESULT_ALLOWED,
    BOUNDARY_RESULT_NOT_ALLOWED,
    BOUNDARY_RESULT_NOT_EVALUATED,
)

INTENT_RECORD = (
    "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_BLOCK)

BOUNDED_MATERIAL_SELECTED = (
    "BOUNDED_EXISTING_MATERIAL_SELECTED_FOR_CONSIDERATION"
)
BOUNDED_MATERIAL_NOT_SELECTED = (
    "BOUNDED_EXISTING_MATERIAL_NOT_SELECTED_FOR_CONSIDERATION"
)
BOUNDED_MATERIAL_SELECTION_POSTURES = (
    BOUNDED_MATERIAL_SELECTED,
    BOUNDED_MATERIAL_NOT_SELECTED,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_RECEIVER_ATTESTATION_BOUNDARY_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY_V0_MIN_SPEC.md"
)
SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result_001.json"
)
BOUNDED_CAPTURE_MATERIAL_RELATIVE_PATH = Path(
    "artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001"
)
GOVERNING_RECEIVER_ATTESTATION_BOUNDARY_SPECIFICATION_PATH = (
    REPO_ROOT
    / GOVERNING_RECEIVER_ATTESTATION_BOUNDARY_SPECIFICATION_RELATIVE_PATH
)
SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_PATH = (
    REPO_ROOT / SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_RELATIVE_PATH
)
BOUNDED_CAPTURE_MATERIAL_PATH = REPO_ROOT / BOUNDED_CAPTURE_MATERIAL_RELATIVE_PATH
GOVERNING_SPEC_RELATIVE_PATH = (
    GOVERNING_RECEIVER_ATTESTATION_BOUNDARY_SPECIFICATION_RELATIVE_PATH
)
GOVERNING_SPEC_PATH = GOVERNING_RECEIVER_ATTESTATION_BOUNDARY_SPECIFICATION_PATH
OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_receiver_attestation_boundary_001__"
    "receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_result.json"
)

SPEC_MARKER_FAMILIES = MappingProxyType(
    {
        "title_and_boundary_identity": (
            "# Receiver-Side Answerable Basis Receiver Attestation Boundary V0 Minimum Specification",
            (
                "receiver_side_answerable_basis_receiver_attestation_boundary_id = "
                "receiver_side_answerable_basis_receiver_attestation_boundary_001"
            ),
            BOUNDARY_TYPE,
            BOUNDARY_SCOPE,
        ),
        "selected_operation_and_result": (
            (
                "selected_candidate_sufficiency_operation_id = "
                "receiver_side_answerable_basis_candidate_sufficiency_operation_001"
            ),
            (
                "selected_candidate_sufficiency_operation_result_required = "
                "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT"
            ),
        ),
        "outcome_family": OUTCOME_FAMILY,
        "result_family": BOUNDARY_RESULT_FAMILY,
        "eight_dimension_requirement": (
            "exactly these eight sufficiency dimensions",
            *REQUIRED_DIMENSION_IDS,
        ),
        "separation": (
            "Candidate sufficient is not receiver attestation.",
            "Captured material is not receiver attestation.",
            (
                "Receiver-attestation consideration allowed is not receiver "
                "attestation."
            ),
            "A boundary result is not operation execution.",
        ),
        "blocked_not_exhausted": (
            "A blocked boundary retains `NOT_EVALUATED` and does not become exhausted.",
        ),
        "open_not_next": (
            "Open does not mean next.",
            "Open means not scheduled, not authorized, and not executed.",
        ),
        "single_use_and_non_conversion": (
            "## 12. Single-Use Posture",
            "## 14. Blocked Conversions",
            "repeated_receiver_attestation_boundary_permission_created",
            "silent rerun",
        ),
    }
)
SPEC_MARKERS = tuple(
    marker
    for family in SPEC_MARKER_FAMILIES.values()
    for marker in family
)

REQUIRED_UPSTREAM_DECLARATIONS = MappingProxyType(
    {
        "resolver_module": SELECTED_SUFFICIENCY_OPERATION_RESOLVER_MODULE,
        "result_version": SELECTED_SUFFICIENCY_OPERATION_RESULT_VERSION,
        "outcome": SELECTED_SUFFICIENCY_OPERATION_OUTCOME_REQUIRED,
        "operation_id": SELECTED_SUFFICIENCY_OPERATION_ID,
        "operation_type": SELECTED_SUFFICIENCY_OPERATION_TYPE,
        "operation_version": SELECTED_SUFFICIENCY_OPERATION_VERSION,
        "operation_scope": SELECTED_SUFFICIENCY_OPERATION_SCOPE,
        "operation_result": SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED,
        "failed_check_count": 0,
        "candidate_sufficiency_operation_recorded": True,
        "candidate_sufficiency_operation_result_recorded": True,
        "candidate_sufficiency_operation_exhausted": True,
        "candidate_sufficiency_decided": True,
        "candidate_sufficiency_established": True,
        "receiver_side_answerable_basis_candidate_sufficient": True,
        "receiver_side_answerable_basis_candidate_insufficient": False,
        "receiver_side_answerable_basis_candidate_indeterminate": False,
        "sufficiency_basis_supplied": True,
        "sufficiency_basis_complete": True,
        "atomic_sufficiency_basis_gate_passed": True,
        "required_dimension_ids": REQUIRED_DIMENSION_IDS,
        "required_dimension_result": DIMENSION_RESULT_SATISFIED,
    }
)

REQUIRED_UPSTREAM_TRUE_POSTURES = (
    "candidate_sufficiency_operation_recorded",
    "candidate_sufficiency_operation_result_recorded",
    "candidate_sufficiency_operation_exhausted",
    "candidate_sufficiency_decided",
    "candidate_sufficiency_established",
    "receiver_side_answerable_basis_candidate_sufficient",
    "sufficiency_basis_supplied",
    "sufficiency_basis_complete",
    "atomic_sufficiency_basis_gate_passed",
)
CORRECTED_UPSTREAM_FALSE_POSTURES = (
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

REQUIRED_UPSTREAM_FALSE_POSTURES = (
    "receiver_side_answerable_basis_candidate_insufficient",
    "receiver_side_answerable_basis_candidate_indeterminate",
    "candidate_insufficiency_established",
    "candidate_indeterminacy_established",
    "partial_evaluation_recorded",
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
    "follow_on_authorized",
    "follow_on_work_authorized",
    "repeated_candidate_sufficiency_operation_permission_created",
    "reusable_candidate_sufficiency_operation_route_created",
    "same_candidate_sufficiency_operation_rerun_authorized",
    "automatic_candidate_sufficiency_operation_retry_created",
    "candidate_sufficiency_operation_debt_created",
    "candidate_sufficiency_operation_obligation_created",
    *CORRECTED_UPSTREAM_FALSE_POSTURES,
)

REQUIRED_FALSE_NON_CLAIMS = (
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_attestation_recorded",
    "receiver_answerable_receipt_present",
    "receiver_answerable_receipt_boundary_created",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "presence_re_evaluation_boundary_created",
    "identity_created",
    "authority_created",
    "standing_created",
    "truth_created",
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
    "repeated_receiver_attestation_boundary_permission_created",
    "reusable_receiver_attestation_route_created",
    "same_receiver_attestation_boundary_rerun_authorized",
    "automatic_receiver_attestation_boundary_retry_created",
    "receiver_attestation_boundary_debt_created",
    "receiver_attestation_boundary_obligation_created",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

PROHIBITED_REQUEST_FLAGS = MappingProxyType(
    {
        "request_boundary_outcome_preclaim": "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "request_boundary_result_preclaim": "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "request_consideration_allowed_preclaim": "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "request_consideration_not_allowed_preclaim": "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "request_receiver_attestation_creation": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
        "request_receiver_attestation_support": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
        "request_receiver_attestation_admission": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
        "request_receiver_attestation_validation": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
        "request_receiver_attestation_recording": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
        "request_receiver_answerable_receipt_creation": "PROHIBITED_RECEIPT_OR_PRESENCE_REQUESTED",
        "request_receiver_answerable_receipt_boundary_creation": "PROHIBITED_RECEIPT_OR_PRESENCE_REQUESTED",
        "request_presence_support": "PROHIBITED_RECEIPT_OR_PRESENCE_REQUESTED",
        "request_presence_authorization": "PROHIBITED_RECEIPT_OR_PRESENCE_REQUESTED",
        "request_presence_establishment": "PROHIBITED_RECEIPT_OR_PRESENCE_REQUESTED",
        "request_presence_recording": "PROHIBITED_RECEIPT_OR_PRESENCE_REQUESTED",
        "request_presence_re_evaluation_boundary_creation": "PROHIBITED_RECEIPT_OR_PRESENCE_REQUESTED",
        "request_receiver_identity_inference": "PROHIBITED_CAPTURE_CONVERSION_REQUESTED",
        "request_independent_custody_inference": "PROHIBITED_CAPTURE_CONVERSION_REQUESTED",
        "request_verified_provenance_inference": "PROHIBITED_CAPTURE_CONVERSION_REQUESTED",
        "request_physical_validity_inference": "PROHIBITED_CAPTURE_CONVERSION_REQUESTED",
        "request_current_presence_inference": "PROHIBITED_CAPTURE_CONVERSION_REQUESTED",
        "request_identity_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_authority_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_standing_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_truth_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_relation_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_coupling_assignment": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_coupling_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_field_machinery_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_runtime_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_api_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_public_interface_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_public_intake_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_output_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        "request_action_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        "request_synchronization_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        "request_follow_on_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        "request_follow_on_work_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        "request_repeated_boundary_permission_creation": "PROHIBITED_REPEATED_USE_REQUESTED",
        "request_reusable_receiver_attestation_route_creation": "PROHIBITED_REPEATED_USE_REQUESTED",
        "request_same_receiver_attestation_boundary_rerun": "PROHIBITED_REPEATED_USE_REQUESTED",
        "request_automatic_boundary_retry_creation": "PROHIBITED_REPEATED_USE_REQUESTED",
        "request_boundary_debt_creation": "PROHIBITED_REPEATED_USE_REQUESTED",
        "request_boundary_obligation_creation": "PROHIBITED_REPEATED_USE_REQUESTED",
        "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "request_repository_scan": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "request_file_discovery": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "request_prior_unsupported_claim_validation": "PROHIBITED_CONTAMINATED_LINEAGE_VALIDATION_REQUESTED",
        "request_contaminated_lineage_validation": "PROHIBITED_CONTAMINATED_LINEAGE_VALIDATION_REQUESTED",
    }
)

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "REQUEST_FIELD_MISSING",
        "REQUEST_UNKNOWN_FIELD",
        "REQUEST_VALUE_MISMATCH",
        "UNSUPPORTED_INTENT",
        "EXPLICIT_BLOCK_REQUESTED",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "RECEIVER_ATTESTATION_BOUNDARY_SPEC_REFERENCE_MISSING",
        "RECEIVER_ATTESTATION_BOUNDARY_SPEC_MARKER_MISSING",
        "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_REFERENCE_MISSING",
        "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_NOT_PARSEABLE",
        "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_NOT_MAPPING",
        "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH",
        "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
        "UPSTREAM_OPERATION_OUTCOME_MISMATCH",
        "UPSTREAM_OPERATION_FAILED_CHECKS_PRESENT",
        "UPSTREAM_OPERATION_NOT_RECORDED",
        "UPSTREAM_OPERATION_RESULT_NOT_RECORDED",
        "UPSTREAM_OPERATION_NOT_EXHAUSTED",
        "UPSTREAM_OPERATION_RESULT_MISMATCH",
        "UPSTREAM_CANDIDATE_NOT_SUFFICIENT",
        "UPSTREAM_CANDIDATE_RESULT_CONFLICT",
        "UPSTREAM_SUFFICIENCY_BASIS_INCOMPLETE",
        "UPSTREAM_ATOMIC_SUFFICIENCY_GATE_INCOMPLETE",
        "UPSTREAM_DIMENSION_SET_MISMATCH",
        "UPSTREAM_DIMENSION_DUPLICATED",
        "UPSTREAM_DIMENSION_MALFORMED",
        "UPSTREAM_DIMENSION_NOT_SATISFIED",
        "UPSTREAM_DIMENSION_NOT_EVALUATED",
        "UPSTREAM_DIMENSION_NOT_ESTABLISHED",
        "UPSTREAM_FALSE_LOCK_NOT_FALSE",
        "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
        "PROHIBITED_RECEIPT_OR_PRESENCE_REQUESTED",
        "PROHIBITED_CAPTURE_CONVERSION_REQUESTED",
        "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        "PROHIBITED_REPEATED_USE_REQUESTED",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "PROHIBITED_CONTAMINATED_LINEAGE_VALIDATION_REQUESTED",
        "WRITE_REFUSED",
    }
)

ALLOWED_WHAT_REMAINS_OPEN = (
    "separate receiver-attestation operation or declaration, if separately selected",
    "receiver-attestation result",
    "receiver-answerable-receipt boundary and operation",
    "presence re-evaluation",
    "identity",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "public interface",
    "public intake",
    "authority",
    "standing",
    "truth",
    "output",
    "action",
    "synchronization",
    "follow-on work",
)
NOT_ALLOWED_WHAT_REMAINS_OPEN = (
    "receiver-attestation consideration under a separately selected bounded request",
    "receiver-attestation operation or declaration remains unauthorized",
    "receiver-answerable-receipt boundary and operation",
    "presence re-evaluation",
    "identity",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "authority",
    "standing",
    "truth",
    "follow-on work",
)
BLOCKED_WHAT_REMAINS_OPEN = (
    "receiver-attestation boundary under a separately valid bounded request",
)
WHAT_REMAINS_OPEN = ALLOWED_WHAT_REMAINS_OPEN

BLOCKED_ROUTES = (
    "candidate_sufficient_to_receiver_attestation",
    "captured_material_to_receiver_attestation_or_receiver_identity",
    "consideration_allowed_to_receiver_attestation",
    "boundary_result_to_operation_execution",
    "boundary_result_to_receiver_answerable_receipt_or_presence",
    "boundary_result_to_identity_authority_standing_or_truth",
    "boundary_result_to_relation_coupling_field_runtime_api_or_public_surface",
    "boundary_result_to_output_action_synchronization_or_follow_on",
    "completed_boundary_to_repeated_reusable_rerun_retry_debt_or_obligation",
    "candidate_sufficiency_or_capture_to_contaminated_lineage_validation",
)


class ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error(Exception):
    """Raised when one bounded result cannot be summarized or written."""


class _DuplicateJsonKeyError(ValueError):
    """Raised when a JSON object contains a duplicate member name."""


def _reject_duplicate_json_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKeyError(key)
        result[key] = value
    return result


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_required_upstream_declarations() -> dict[str, Any]:
    declarations = copy.deepcopy(dict(REQUIRED_UPSTREAM_DECLARATIONS))
    declarations["required_dimension_ids"] = list(REQUIRED_DIMENSION_IDS)
    return declarations


def _check(
    name: str,
    passed: bool,
    code: str | None = None,
    *,
    expected: Any = None,
    actual: Any = None,
) -> dict[str, Any]:
    check: dict[str, Any] = {"name": name, "passed": passed}
    if expected is not None:
        check["expected"] = copy.deepcopy(expected)
    if actual is not None:
        check["actual"] = copy.deepcopy(actual)
    if not passed and code is not None:
        check["failure_code"] = code
        check["block_code"] = code
    return check


def _add_failure(
    checks: list[dict[str, Any]], name: str, code: str
) -> None:
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
    except (OSError, UnicodeError):
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


def _declared_non_claims_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_FALSE_NON_CLAIMS)
        and all(value.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS)
    )


def _selection_values(selected: bool) -> dict[str, Any]:
    return {
        "bounded_material_selected_for_consideration": selected,
        "bounded_material_selection_posture": (
            BOUNDED_MATERIAL_SELECTED if selected else BOUNDED_MATERIAL_NOT_SELECTED
        ),
        "bounded_existing_material_path": (
            str(BOUNDED_CAPTURE_MATERIAL_RELATIVE_PATH) if selected else None
        ),
    }


def _expected_request_values(selected: bool) -> dict[str, Any]:
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
        "selected_candidate_sufficiency_boundary_id": SELECTED_SUFFICIENCY_BOUNDARY_ID,
        "selected_candidate_sufficiency_operation_id": SELECTED_SUFFICIENCY_OPERATION_ID,
        "selected_candidate_sufficiency_operation_type": SELECTED_SUFFICIENCY_OPERATION_TYPE,
        "selected_candidate_sufficiency_operation_version": SELECTED_SUFFICIENCY_OPERATION_VERSION,
        "selected_candidate_sufficiency_operation_scope": SELECTED_SUFFICIENCY_OPERATION_SCOPE,
        "selected_candidate_sufficiency_operation_result_required": (
            SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
        ),
        "governing_receiver_attestation_boundary_specification_path": str(
            GOVERNING_RECEIVER_ATTESTATION_BOUNDARY_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_sufficiency_operation_artifact_path": str(
            SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "required_upstream_declarations": (
            _canonical_required_upstream_declarations()
        ),
        **_selection_values(selected),
    }


def build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one canonical request, with bounded selection true by default."""
    selected = True
    if overrides.get("bounded_material_selected_for_consideration") is False:
        selected = False
    elif (
        "bounded_material_selected_for_consideration" not in overrides
        and (
            overrides.get("bounded_material_selection_posture")
            == BOUNDED_MATERIAL_NOT_SELECTED
            or overrides.get("bounded_existing_material_path") is None
            and "bounded_existing_material_path" in overrides
        )
    ):
        selected = False
    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **_expected_request_values(selected),
        "declared_non_claims": _canonical_non_claims(),
    }
    request.update({field: False for field in PROHIBITED_REQUEST_FLAGS})
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build the declared request using the same exact bounded contract."""
    return (
        build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request(
            **overrides
        )
    )


def _preclaim_fields() -> set[str]:
    return {
        "outcome",
        "boundary_result",
        "receiver_attestation_boundary_result",
        "receiver_attestation_boundary_recorded",
        "receiver_attestation_boundary_result_recorded",
        "receiver_attestation_consideration_allowed",
        "receiver_attestation_consideration_not_allowed",
        "receiver_attestation_boundary_exhausted",
        "receiver_side_answerable_basis_receiver_attestation_boundary_recorded",
        "receiver_side_answerable_basis_receiver_attestation_boundary_result_recorded",
        "receiver_side_answerable_basis_receiver_attestation_boundary_result",
        "selected_sufficiency_operation_artifact",
        "complete_sufficiency_operation_artifact",
        "sufficiency_basis_records",
        "receiver_side_answerable_basis_candidate_sufficiency_operation",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions",
        "capture_signal_data",
        "complete_capture_material",
        *REQUIRED_FALSE_NON_CLAIMS,
    }


def _canonical_request_keys() -> set[str]:
    return {
        "intent",
        "declared_non_claims",
        *_expected_request_values(True),
        *PROHIBITED_REQUEST_FLAGS,
    }


def _request_mismatch_code(field: str) -> str:
    if field.startswith("selected_candidate_sufficiency_operation_"):
        return "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH"
    if field in {
        "receiver_side_answerable_basis_candidate_id",
        "receiver_side_answerable_basis_candidate_type",
        "receiver_side_answerable_basis_candidate_scope",
        "selected_candidate_reception_operation_id",
        "selected_candidate_evaluation_boundary_id",
        "selected_candidate_evaluation_operation_id",
        "selected_candidate_sufficiency_boundary_id",
    }:
        return "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
    return "REQUEST_VALUE_MISMATCH"


def _validate_request(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None]:
    if request.get("intent") == INTENT_BLOCK:
        return "EXPLICIT_BLOCK_REQUESTED", "explicit block intent was requested"
    if request.get("intent") not in SUPPORTED_INTENTS:
        return "UNSUPPORTED_INTENT", "intent is not supported"

    preclaimed = set(request).intersection(_preclaim_fields())
    if preclaimed:
        return (
            "RESULT_POSTURE_PRECLAIMED",
            "caller supplied a result, material body, or non-claim posture",
        )

    expected_keys = _canonical_request_keys()
    missing = expected_keys.difference(request)
    if missing:
        return "REQUEST_FIELD_MISSING", "canonical request fields are missing"
    unknown = set(request).difference(expected_keys)
    if unknown:
        return "REQUEST_UNKNOWN_FIELD", "declared request contains unknown fields"

    selected = request.get("bounded_material_selected_for_consideration")
    if type(selected) is not bool:
        return (
            "REQUEST_VALUE_MISMATCH",
            "bounded material selection must be a boolean",
        )
    for field, expected in _expected_request_values(selected).items():
        actual = request.get(field)
        valid = actual == expected
        code = _request_mismatch_code(field)
        checks.append(
            _check(
                "request." + field,
                valid,
                code,
                expected=expected,
                actual=actual,
            )
        )
        if not valid:
            return code, field + " does not match the bounded request contract"

    if not _declared_non_claims_valid(request.get("declared_non_claims")):
        return (
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared_non_claims must contain the exact canonical false set",
        )
    checks.append(_check("request.declared_non_claims", True))

    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        valid = request.get(field) is False
        checks.append(_check("request." + field, valid, code))
        if not valid:
            return code, field + " must remain false"
    return None, None


def _empty_upstream_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "governing_paths": {
            "governing_receiver_attestation_boundary_specification_path": (
                request.get(
                    "governing_receiver_attestation_boundary_specification_path"
                )
            ),
            "selected_sufficiency_operation_artifact_path": request.get(
                "selected_sufficiency_operation_artifact_path"
            ),
            "bounded_existing_material_path": request.get(
                "bounded_existing_material_path"
            ),
        },
        "marker_validation": {
            family: False for family in SPEC_MARKER_FAMILIES
        },
        "selected_operation_metadata": {},
        "selected_operation_identity": {},
        "selected_candidate_identity": {},
        "recording_validation": {},
        "sufficiency_validation": {},
        "dimension_validation": {},
        "false_lock_validation": {},
        "required_upstream_false_lock_fields": list(
            REQUIRED_UPSTREAM_FALSE_POSTURES
        ),
        "corrected_upstream_false_lock_fields": list(
            CORRECTED_UPSTREAM_FALSE_POSTURES
        ),
        "corrected_upstream_false_lock_validation": {
            field: False for field in CORRECTED_UPSTREAM_FALSE_POSTURES
        },
        "bounded_material_validation": {
            "selected_for_consideration": (
                request.get("bounded_material_selected_for_consideration")
                is True
            ),
            "reference_is_canonical": (
                request.get("bounded_existing_material_path")
                == str(BOUNDED_CAPTURE_MATERIAL_RELATIVE_PATH)
            ),
            "path_existence_not_used_as_authority": True,
            "capture_body_not_read": True,
        },
        "complete_operation_artifact_omitted": True,
        "complete_sufficiency_basis_omitted": True,
        "complete_capture_signal_data_omitted": True,
    }


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


def _validate_specification(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    upstream: dict[str, Any],
) -> tuple[str | None, str | None]:
    text, error = _read_text(
        request["governing_receiver_attestation_boundary_specification_path"]
    )
    if error is not None or text is None:
        return (
            "RECEIVER_ATTESTATION_BOUNDARY_SPEC_REFERENCE_MISSING",
            "governing receiver-attestation boundary specification is unavailable",
        )
    for family, markers in SPEC_MARKER_FAMILIES.items():
        valid = all(marker in text for marker in markers)
        upstream["marker_validation"][family] = valid
        code, reason = _require(
            checks,
            "specification." + family,
            valid,
            "RECEIVER_ATTESTATION_BOUNDARY_SPEC_MARKER_MISSING",
            "governing specification marker family is incomplete: " + family,
        )
        if code is not None:
            return code, reason
    return None, None


def _validate_upstream(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    upstream = _empty_upstream_basis(request)
    code, reason = _validate_specification(request, checks, upstream)
    if code is not None:
        return code, reason, upstream

    artifact, error = _read_json(
        request["selected_sufficiency_operation_artifact_path"]
    )
    if error in {"not_a_file", "unreadable"}:
        return (
            "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_REFERENCE_MISSING",
            "selected sufficiency-operation artifact is unavailable",
            upstream,
        )
    if error == "duplicate_key":
        return (
            "UPSTREAM_DIMENSION_DUPLICATED",
            "selected sufficiency-operation artifact contains duplicate JSON keys",
            upstream,
        )
    if error == "not_parseable":
        return (
            "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_NOT_PARSEABLE",
            "selected sufficiency-operation artifact is not parseable JSON",
            upstream,
        )
    if not isinstance(artifact, Mapping):
        return (
            "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_NOT_MAPPING",
            "selected sufficiency-operation artifact is not a mapping",
            upstream,
        )

    operation = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation"
    )
    dimensions = artifact.get(
        "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions"
    )
    if not isinstance(operation, Mapping) or not isinstance(dimensions, Mapping):
        return (
            "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_NOT_MAPPING",
            "selected artifact lacks required bounded operation sections",
            upstream,
        )

    upstream["selected_operation_metadata"] = {
        "resolver_module": artifact.get("resolver_module"),
        "result_version": artifact.get("result_version"),
        "outcome": artifact.get("outcome"),
        "failed_check_count": artifact.get("failed_check_count"),
    }
    upstream["selected_operation_identity"] = {
        "operation_id": operation.get("operation_id"),
        "operation_type": operation.get("operation_type"),
        "operation_version": operation.get("operation_version"),
        "operation_scope": operation.get("operation_scope"),
        "operation_result": operation.get("operation_result"),
    }
    upstream["selected_candidate_identity"] = {
        "candidate_id": operation.get(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "candidate_type": operation.get(
            "receiver_side_answerable_basis_candidate_type"
        ),
        "candidate_scope": operation.get(
            "receiver_side_answerable_basis_candidate_scope"
        ),
        "reception_operation_id": operation.get(
            "selected_candidate_reception_operation_id"
        ),
        "evaluation_boundary_id": operation.get(
            "selected_candidate_evaluation_boundary_id"
        ),
        "evaluation_operation_id": operation.get(
            "selected_candidate_evaluation_operation_id"
        ),
        "sufficiency_boundary_id": operation.get(
            "selected_candidate_sufficiency_boundary_id"
        ),
    }

    for field, expected, failure_code in (
        (
            "resolver_module",
            SELECTED_SUFFICIENCY_OPERATION_RESOLVER_MODULE,
            "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH",
        ),
        (
            "result_version",
            SELECTED_SUFFICIENCY_OPERATION_RESULT_VERSION,
            "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH",
        ),
        (
            "outcome",
            SELECTED_SUFFICIENCY_OPERATION_OUTCOME_REQUIRED,
            "UPSTREAM_OPERATION_OUTCOME_MISMATCH",
        ),
    ):
        actual = artifact.get(field)
        code, reason = _require(
            checks,
            "upstream." + field,
            actual == expected,
            failure_code,
            "selected sufficiency-operation " + field + " does not match",
            expected=expected,
            actual=actual,
        )
        if code is not None:
            return code, reason, upstream

    failed_count = artifact.get("failed_check_count")
    code, reason = _require(
        checks,
        "upstream.failed_check_count",
        type(failed_count) is int and failed_count == 0,
        "UPSTREAM_OPERATION_FAILED_CHECKS_PRESENT",
        "selected sufficiency operation has failed checks",
        expected=0,
        actual=failed_count,
    )
    if code is not None:
        return code, reason, upstream

    operation_identity = {
        "operation_id": SELECTED_SUFFICIENCY_OPERATION_ID,
        "operation_type": SELECTED_SUFFICIENCY_OPERATION_TYPE,
        "operation_version": SELECTED_SUFFICIENCY_OPERATION_VERSION,
        "operation_scope": SELECTED_SUFFICIENCY_OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_sufficiency_operation_id": (
            SELECTED_SUFFICIENCY_OPERATION_ID
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_type": (
            SELECTED_SUFFICIENCY_OPERATION_TYPE
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_version": (
            SELECTED_SUFFICIENCY_OPERATION_VERSION
        ),
        "receiver_side_answerable_basis_candidate_sufficiency_operation_scope": (
            SELECTED_SUFFICIENCY_OPERATION_SCOPE
        ),
    }
    for field, expected in operation_identity.items():
        actual = operation.get(field)
        code, reason = _require(
            checks,
            "upstream." + field,
            actual == expected,
            "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH",
            "selected sufficiency-operation identity does not match " + field,
            expected=expected,
            actual=actual,
        )
        if code is not None:
            return code, reason, upstream

    candidate_identity = {
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": (
            SELECTED_RECEPTION_OPERATION_ID
        ),
        "selected_candidate_evaluation_boundary_id": (
            SELECTED_EVALUATION_BOUNDARY_ID
        ),
        "selected_candidate_evaluation_operation_id": (
            SELECTED_EVALUATION_OPERATION_ID
        ),
        "selected_candidate_sufficiency_boundary_id": (
            SELECTED_SUFFICIENCY_BOUNDARY_ID
        ),
    }
    for field, expected in candidate_identity.items():
        actual = operation.get(field)
        code, reason = _require(
            checks,
            "upstream." + field,
            actual == expected,
            "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            "selected candidate lineage does not match " + field,
            expected=expected,
            actual=actual,
        )
        if code is not None:
            return code, reason, upstream

    result_fields = (
        "operation_result",
        "candidate_sufficiency_operation_result",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_result",
    )
    for field in result_fields:
        actual = operation.get(field)
        code, reason = _require(
            checks,
            "upstream." + field,
            actual == SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED,
            "UPSTREAM_OPERATION_RESULT_MISMATCH",
            "selected operation does not record the required sufficient result",
            expected=SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED,
            actual=actual,
        )
        if code is not None:
            return code, reason, upstream

    recording_validation = {
        "candidate_sufficiency_operation_recorded": (
            operation.get("candidate_sufficiency_operation_recorded") is True
        ),
        "candidate_sufficiency_operation_result_recorded": (
            operation.get("candidate_sufficiency_operation_result_recorded")
            is True
        ),
        "candidate_sufficiency_operation_exhausted": (
            operation.get("candidate_sufficiency_operation_exhausted") is True
        ),
    }
    upstream["recording_validation"] = recording_validation
    for field, failure_code in (
        (
            "candidate_sufficiency_operation_recorded",
            "UPSTREAM_OPERATION_NOT_RECORDED",
        ),
        (
            "candidate_sufficiency_operation_result_recorded",
            "UPSTREAM_OPERATION_RESULT_NOT_RECORDED",
        ),
        (
            "candidate_sufficiency_operation_exhausted",
            "UPSTREAM_OPERATION_NOT_EXHAUSTED",
        ),
    ):
        code, reason = _require(
            checks,
            "upstream." + field,
            recording_validation[field],
            failure_code,
            "selected operation recording posture is incomplete: " + field,
        )
        if code is not None:
            return code, reason, upstream

    sufficiency_validation = {
        field: operation.get(field) is True
        for field in REQUIRED_UPSTREAM_TRUE_POSTURES
    }
    upstream["sufficiency_validation"] = sufficiency_validation
    for field in (
        "candidate_sufficiency_decided",
        "candidate_sufficiency_established",
        "receiver_side_answerable_basis_candidate_sufficient",
    ):
        code, reason = _require(
            checks,
            "upstream." + field,
            sufficiency_validation[field],
            "UPSTREAM_CANDIDATE_NOT_SUFFICIENT",
            "selected candidate is not recorded as sufficient: " + field,
        )
        if code is not None:
            return code, reason, upstream
    for field in ("sufficiency_basis_supplied", "sufficiency_basis_complete"):
        code, reason = _require(
            checks,
            "upstream." + field,
            sufficiency_validation[field],
            "UPSTREAM_SUFFICIENCY_BASIS_INCOMPLETE",
            "selected operation sufficiency basis is incomplete: " + field,
        )
        if code is not None:
            return code, reason, upstream
    code, reason = _require(
        checks,
        "upstream.atomic_sufficiency_basis_gate_passed",
        sufficiency_validation["atomic_sufficiency_basis_gate_passed"],
        "UPSTREAM_ATOMIC_SUFFICIENCY_GATE_INCOMPLETE",
        "selected operation atomic sufficiency gate is incomplete",
    )
    if code is not None:
        return code, reason, upstream

    conflicting_candidate_result = (
        operation.get("receiver_side_answerable_basis_candidate_insufficient")
        is not False
        or operation.get(
            "receiver_side_answerable_basis_candidate_indeterminate"
        )
        is not False
    )
    code, reason = _require(
        checks,
        "upstream.candidate_result_non_conflicting",
        not conflicting_candidate_result,
        "UPSTREAM_CANDIDATE_RESULT_CONFLICT",
        "selected operation contains a conflicting candidate result posture",
    )
    if code is not None:
        return code, reason, upstream

    if set(dimensions) != set(REQUIRED_DIMENSION_IDS):
        _add_failure(
            checks,
            "upstream.dimension_set",
            "UPSTREAM_DIMENSION_SET_MISMATCH",
        )
        return (
            "UPSTREAM_DIMENSION_SET_MISMATCH",
            "selected operation does not contain exactly eight required dimensions",
            upstream,
        )
    dimension_validation: dict[str, dict[str, Any]] = {}
    for dimension_id in REQUIRED_DIMENSION_IDS:
        entry = dimensions.get(dimension_id)
        if not isinstance(entry, Mapping):
            _add_failure(
                checks,
                "upstream.dimension." + dimension_id,
                "UPSTREAM_DIMENSION_MALFORMED",
            )
            return (
                "UPSTREAM_DIMENSION_MALFORMED",
                "selected operation dimension is not a mapping",
                upstream,
            )
        summary = {
            "dimension_id": entry.get("dimension_id"),
            "dimension_result": entry.get("dimension_result"),
            "dimension_evaluated": entry.get("dimension_evaluated"),
            "dimension_established": entry.get("dimension_established"),
        }
        dimension_validation[dimension_id] = summary
        if entry.get("dimension_id") != dimension_id:
            _add_failure(
                checks,
                "upstream.dimension_id." + dimension_id,
                "UPSTREAM_DIMENSION_MALFORMED",
            )
            return (
                "UPSTREAM_DIMENSION_MALFORMED",
                "selected operation dimension identity does not match",
                upstream,
            )
        if entry.get("dimension_result") != DIMENSION_RESULT_SATISFIED:
            _add_failure(
                checks,
                "upstream.dimension_result." + dimension_id,
                "UPSTREAM_DIMENSION_NOT_SATISFIED",
            )
            return (
                "UPSTREAM_DIMENSION_NOT_SATISFIED",
                "selected operation dimension is not SATISFIED",
                upstream,
            )
        if entry.get("dimension_evaluated") is not True:
            _add_failure(
                checks,
                "upstream.dimension_evaluated." + dimension_id,
                "UPSTREAM_DIMENSION_NOT_EVALUATED",
            )
            return (
                "UPSTREAM_DIMENSION_NOT_EVALUATED",
                "selected operation dimension is not evaluated",
                upstream,
            )
        if entry.get("dimension_established") is not True:
            _add_failure(
                checks,
                "upstream.dimension_established." + dimension_id,
                "UPSTREAM_DIMENSION_NOT_ESTABLISHED",
            )
            return (
                "UPSTREAM_DIMENSION_NOT_ESTABLISHED",
                "selected operation dimension is not established",
                upstream,
            )
        checks.append(
            _check("upstream.dimension." + dimension_id, True)
        )
    upstream["dimension_validation"] = dimension_validation

    false_lock_validation = {
        field: operation.get(field) is False
        for field in REQUIRED_UPSTREAM_FALSE_POSTURES
    }
    upstream["false_lock_validation"] = false_lock_validation
    upstream["corrected_upstream_false_lock_validation"] = {
        field: false_lock_validation[field]
        for field in CORRECTED_UPSTREAM_FALSE_POSTURES
    }
    for field, valid in false_lock_validation.items():
        code, reason = _require(
            checks,
            "upstream.false_lock." + field,
            valid,
            "UPSTREAM_FALSE_LOCK_NOT_FALSE",
            "selected operation false lock is missing or not false: " + field,
        )
        if code is not None:
            return code, reason, upstream
    return None, None, upstream


def _boundary_result_for_outcome(outcome: str) -> str:
    if outcome == OUTCOME_ALLOWED:
        return BOUNDARY_RESULT_ALLOWED
    if outcome == OUTCOME_NOT_ALLOWED:
        return BOUNDARY_RESULT_NOT_ALLOWED
    return BOUNDARY_RESULT_NOT_EVALUATED


def _boundary_object(
    outcome: str, request: Mapping[str, Any], upstream: Mapping[str, Any]
) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    not_allowed = outcome == OUTCOME_NOT_ALLOWED
    completed = allowed or not_allowed
    boundary_result = _boundary_result_for_outcome(outcome)
    operation_valid = (
        isinstance(upstream.get("sufficiency_validation"), Mapping)
        and bool(upstream.get("sufficiency_validation"))
        and all(upstream["sufficiency_validation"].values())
    )
    return {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "receiver_side_answerable_basis_receiver_attestation_boundary_id": (
            BOUNDARY_ID
        ),
        "receiver_side_answerable_basis_receiver_attestation_boundary_type": (
            BOUNDARY_TYPE
        ),
        "receiver_side_answerable_basis_receiver_attestation_boundary_version": (
            BOUNDARY_VERSION
        ),
        "receiver_side_answerable_basis_receiver_attestation_boundary_scope": (
            BOUNDARY_SCOPE
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": (
            SELECTED_RECEPTION_OPERATION_ID
        ),
        "selected_candidate_evaluation_boundary_id": (
            SELECTED_EVALUATION_BOUNDARY_ID
        ),
        "selected_candidate_evaluation_operation_id": (
            SELECTED_EVALUATION_OPERATION_ID
        ),
        "selected_candidate_sufficiency_boundary_id": (
            SELECTED_SUFFICIENCY_BOUNDARY_ID
        ),
        "selected_candidate_sufficiency_operation_id": (
            SELECTED_SUFFICIENCY_OPERATION_ID
        ),
        "selected_candidate_sufficiency_operation_type": (
            SELECTED_SUFFICIENCY_OPERATION_TYPE
        ),
        "selected_candidate_sufficiency_operation_version": (
            SELECTED_SUFFICIENCY_OPERATION_VERSION
        ),
        "selected_candidate_sufficiency_operation_scope": (
            SELECTED_SUFFICIENCY_OPERATION_SCOPE
        ),
        "selected_candidate_sufficiency_operation_result_required": (
            SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
        ),
        "selected_candidate_sufficiency_operation_validated": operation_valid,
        "selected_candidate_sufficient": operation_valid,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "bounded_material_selected_for_consideration": (
            request.get("bounded_material_selected_for_consideration") is True
        ),
        "bounded_material_selection_posture": request.get(
            "bounded_material_selection_posture"
        ),
        "bounded_existing_material_reference_only": completed,
        "bounded_material_path_existence_not_used_as_authority": True,
        "receiver_attestation_boundary_recorded": completed,
        "receiver_attestation_boundary_result_recorded": completed,
        "receiver_attestation_boundary_result": boundary_result,
        "receiver_attestation_consideration_allowed": allowed,
        "receiver_attestation_consideration_not_allowed": not_allowed,
        "receiver_attestation_boundary_exhausted": completed,
        "receiver_side_answerable_basis_receiver_attestation_boundary_recorded": (
            completed
        ),
        "receiver_side_answerable_basis_receiver_attestation_boundary_result_recorded": (
            completed
        ),
        "receiver_side_answerable_basis_receiver_attestation_boundary_result": (
            boundary_result
        ),
        **_canonical_non_claims(),
    }


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
        "selected_candidate_sufficiency_operation_id": request.get(
            "selected_candidate_sufficiency_operation_id"
        ),
        "selected_candidate_sufficiency_operation_result_required": request.get(
            "selected_candidate_sufficiency_operation_result_required"
        ),
        "governing_receiver_attestation_boundary_specification_path": (
            request.get(
                "governing_receiver_attestation_boundary_specification_path"
            )
        ),
        "selected_sufficiency_operation_artifact_path": request.get(
            "selected_sufficiency_operation_artifact_path"
        ),
        "bounded_material_selected_for_consideration": request.get(
            "bounded_material_selected_for_consideration"
        ),
        "bounded_material_selection_posture": request.get(
            "bounded_material_selection_posture"
        ),
        "bounded_existing_material_path": request.get(
            "bounded_existing_material_path"
        ),
        "required_upstream_declarations_validated": (
            request.get("required_upstream_declarations")
            == _canonical_required_upstream_declarations()
        ),
        "declared_non_claims_validated": _declared_non_claims_valid(
            request.get("declared_non_claims")
        ),
        "prohibited_request_flags_validated": all(
            request.get(field) is False for field in PROHIBITED_REQUEST_FLAGS
        ),
    }


def _boundary_statement(outcome: str) -> dict[str, bool]:
    completed = outcome in {OUTCOME_ALLOWED, OUTCOME_NOT_ALLOWED}
    return {
        "one_selected_completed_sufficient_operation_consumed_as_upstream_standing": (
            completed
        ),
        "sufficiency_basis_not_reopened": True,
        "sufficiency_basis_not_re_evaluated": True,
        "receiver_attestation_consideration_only": completed,
        "receiver_attestation_not_created": True,
        "receiver_attestation_not_supported": True,
        "receiver_attestation_not_recorded": True,
        "capture_path_existence_not_used_as_authority": True,
        "boundary_single_use": completed,
        "boundary_exhausted_only_after_completed_result": completed,
        "result_level_non_claims_canonical_false": True,
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
        "open_does_not_mean_next": True,
    }


def _boundary_non_meaning() -> dict[str, bool]:
    return {
        "candidate_sufficient_is_not_receiver_attestation": True,
        "captured_material_is_not_receiver_attestation": True,
        "consideration_allowed_is_not_receiver_attestation": True,
        "consideration_not_allowed_is_not_candidate_insufficiency": True,
        "consideration_not_allowed_is_not_receiver_refusal": True,
        "consideration_not_allowed_is_not_invalid_evidence": True,
        "consideration_not_allowed_is_not_failed_attestation": True,
        "consideration_not_allowed_is_not_receiver_absence": True,
        "boundary_result_is_not_operation_execution": True,
        "boundary_exhaustion_is_not_downstream_authorization": True,
        "receiver_attestation_is_not_receiver_answerable_receipt": True,
        "receiver_answerable_receipt_is_not_presence": True,
        "presence_is_not_identity_authority_standing_or_truth": True,
    }


def _what_remains_open(outcome: str) -> list[str]:
    if outcome == OUTCOME_ALLOWED:
        return list(ALLOWED_WHAT_REMAINS_OPEN)
    if outcome == OUTCOME_NOT_ALLOWED:
        return list(NOT_ALLOWED_WHAT_REMAINS_OPEN)
    return list(BLOCKED_WHAT_REMAINS_OPEN)


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get(
        "receiver_side_answerable_basis_receiver_attestation_boundary"
    )
    upstream = result.get("upstream_basis")
    boundary = boundary if isinstance(boundary, Mapping) else {}
    upstream = upstream if isinstance(upstream, Mapping) else {}
    dimensions = upstream.get("dimension_validation")
    false_locks = upstream.get("false_lock_validation")
    markers = upstream.get("marker_validation")
    return {
        "outcome": result.get("outcome"),
        "boundary_result": boundary.get("receiver_attestation_boundary_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "boundary_id": boundary.get("boundary_id"),
        "boundary_type": boundary.get("boundary_type"),
        "boundary_version": boundary.get("boundary_version"),
        "boundary_scope": boundary.get("boundary_scope"),
        "selected_candidate_id": boundary.get(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "selected_sufficiency_operation_id": boundary.get(
            "selected_candidate_sufficiency_operation_id"
        ),
        "selected_sufficiency_operation_result_required": boundary.get(
            "selected_candidate_sufficiency_operation_result_required"
        ),
        "bounded_material_selected_for_consideration": boundary.get(
            "bounded_material_selected_for_consideration"
        ),
        "receiver_attestation_boundary_recorded": boundary.get(
            "receiver_attestation_boundary_recorded"
        ),
        "receiver_attestation_boundary_result_recorded": boundary.get(
            "receiver_attestation_boundary_result_recorded"
        ),
        "receiver_attestation_consideration_allowed": boundary.get(
            "receiver_attestation_consideration_allowed"
        ),
        "receiver_attestation_consideration_not_allowed": boundary.get(
            "receiver_attestation_consideration_not_allowed"
        ),
        "receiver_attestation_boundary_exhausted": boundary.get(
            "receiver_attestation_boundary_exhausted"
        ),
        "specification_markers_validated": (
            isinstance(markers, Mapping)
            and bool(markers)
            and all(markers.values())
        ),
        "selected_operation_validated": boundary.get(
            "selected_candidate_sufficiency_operation_validated"
        ),
        "eight_dimensions_validated": (
            isinstance(dimensions, Mapping)
            and len(dimensions) == len(REQUIRED_DIMENSION_IDS)
            and all(
                isinstance(entry, Mapping)
                and entry.get("dimension_result")
                == DIMENSION_RESULT_SATISFIED
                and entry.get("dimension_evaluated") is True
                and entry.get("dimension_established") is True
                for entry in dimensions.values()
            )
        ),
        "upstream_false_locks_validated": (
            isinstance(false_locks, Mapping)
            and bool(false_locks)
            and all(false_locks.values())
        ),
        "result_level_non_claims_canonical_false": (
            _declared_non_claims_valid(result.get("non_claims"))
        ),
        "complete_operation_artifact_omitted": upstream.get(
            "complete_operation_artifact_omitted"
        )
        is True,
        "complete_sufficiency_basis_omitted": upstream.get(
            "complete_sufficiency_basis_omitted"
        )
        is True,
        "complete_capture_signal_data_omitted": upstream.get(
            "complete_capture_signal_data_omitted"
        )
        is True,
        "governing_paths": copy.deepcopy(upstream.get("governing_paths", {})),
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
    bounded_upstream = (
        copy.deepcopy(dict(upstream))
        if isinstance(upstream, Mapping)
        else _empty_upstream_basis(request)
    )
    boundary = _boundary_object(outcome, request, bounded_upstream)
    result: dict[str, Any] = {
        "receiver_side_answerable_basis_receiver_attestation_boundary_metadata": {
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
            "selected_sufficiency_operation_artifact_path": request.get(
                "selected_sufficiency_operation_artifact_path"
            ),
        },
        "declared_receiver_side_answerable_basis_receiver_attestation_boundary_basis": (
            _declared_basis(request)
        ),
        "upstream_basis": bounded_upstream,
        "receiver_side_answerable_basis_receiver_attestation_boundary": boundary,
        "receiver_side_answerable_basis_receiver_attestation_boundary_checks": (
            copy.deepcopy(checks)
        ),
        "receiver_side_answerable_basis_receiver_attestation_boundary_statement": (
            _boundary_statement(outcome)
        ),
        "receiver_side_answerable_basis_receiver_attestation_boundary_non_meaning": (
            _boundary_non_meaning()
        ),
        "boundary_result_detail": {
            "boundary_result": boundary["receiver_attestation_boundary_result"],
            "receiver_attestation_boundary_recorded": boundary[
                "receiver_attestation_boundary_recorded"
            ],
            "receiver_attestation_boundary_result_recorded": boundary[
                "receiver_attestation_boundary_result_recorded"
            ],
            "receiver_attestation_consideration_allowed": boundary[
                "receiver_attestation_consideration_allowed"
            ],
            "receiver_attestation_consideration_not_allowed": boundary[
                "receiver_attestation_consideration_not_allowed"
            ],
            "receiver_attestation_boundary_exhausted": boundary[
                "receiver_attestation_boundary_exhausted"
            ],
            "completed_consideration_posture_count": sum(
                boundary[field] is True
                for field in (
                    "receiver_attestation_consideration_allowed",
                    "receiver_attestation_consideration_not_allowed",
                )
            ),
        },
        "boundary_posture": {
            "bounded_material_selected_for_consideration": boundary[
                "bounded_material_selected_for_consideration"
            ],
            "bounded_existing_material_reference_only": boundary[
                "bounded_existing_material_reference_only"
            ],
            "candidate_sufficiency_not_reopened": True,
            "receiver_attestation_not_created": True,
            "receiver_answerable_receipt_not_created": True,
            "presence_not_established": True,
            "single_use_only": True,
        },
        "permitted_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "blocked_routes": list(BLOCKED_ROUTES),
        "what_remains_open": _what_remains_open(outcome),
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
        "failed_check_count": sum(
            check.get("passed") is False for check in checks
        ),
        "passed_check_count": sum(
            check.get("passed") is True for check in checks
        ),
    }
    result[
        "receiver_side_answerable_basis_receiver_attestation_boundary_summary"
    ] = _summary_from_result(result)
    return result


def resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one exact receiver-attestation consideration boundary."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared_request = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request()
        )
    elif not isinstance(request, Mapping):
        declared_request = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request()
        )
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
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            code=code,
            reason=reason,
        )

    code, reason, upstream = _validate_upstream(declared_request, checks)
    if code is not None:
        _add_failure(checks, "upstream_basis", code)
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            checks,
            upstream=upstream,
            code=code,
            reason=reason,
        )

    outcome = (
        OUTCOME_ALLOWED
        if declared_request["bounded_material_selected_for_consideration"]
        is True
        else OUTCOME_NOT_ALLOWED
    )
    return _result(
        declared_request,
        outcome,
        checks,
        upstream=upstream,
    )


def resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Read one exact request path without discovery and resolve it."""
    payload, error = _read_json(request_path)
    if error is not None or not isinstance(payload, Mapping):
        request = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request()
        )
        checks = [_check("declared_request_path", False, "REQUEST_NOT_MAPPING")]
        return _result(
            request,
            OUTCOME_BLOCKED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason=(
                "request path is unavailable, not parseable, duplicated, "
                "or not a mapping"
            ),
        )
    return (
        resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2(
            payload
        )
    )


def build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic material-omitting summary."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error(
            "WRITE_REFUSED: result must be a mapping"
        )
    return _summary_from_result(result)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(
            path.stem + "_" + f"{index:03d}" + path.suffix
        )
        if not candidate.exists():
            return candidate
    raise ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def _contains_complete_material(value: Any) -> bool:
    forbidden_keys = {
        "selected_sufficiency_operation_artifact",
        "complete_sufficiency_operation_artifact",
        "sufficiency_basis_records",
        "basis_items",
        "basis_references",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_basis",
        "receiver_side_answerable_basis_candidate_sufficiency_operation_checks",
        "capture_signal_data",
        "signal_samples",
        "raw_signal_data",
        "complete_capture_material",
    }
    if isinstance(value, Mapping):
        return any(
            key in forbidden_keys or _contains_complete_material(nested)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        return any(_contains_complete_material(item) for item in value)
    return False


def _path_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _output_path_is_forbidden(path: Path) -> bool:
    resolved = path.resolve()
    protected_roots = (
        (REPO_ROOT / "reference").resolve(),
        (REPO_ROOT / "spec").resolve(),
        (REPO_ROOT / "src").resolve(),
        (REPO_ROOT / "tests").resolve(),
        BOUNDED_CAPTURE_MATERIAL_PATH.resolve(),
        SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_PATH.parent.resolve(),
    )
    return any(_path_within(resolved, root) for root in protected_roots)


def _result_branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    boundary = result.get(
        "receiver_side_answerable_basis_receiver_attestation_boundary"
    )
    if outcome not in OUTCOME_FAMILY or not isinstance(boundary, Mapping):
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
    if outcome == OUTCOME_ALLOWED:
        return (
            boundary.get("receiver_attestation_boundary_result")
            == BOUNDARY_RESULT_ALLOWED
            and boundary.get("receiver_attestation_boundary_recorded") is True
            and boundary.get("receiver_attestation_boundary_result_recorded")
            is True
            and boundary.get("receiver_attestation_consideration_allowed")
            is True
            and boundary.get(
                "receiver_attestation_consideration_not_allowed"
            )
            is False
            and boundary.get("receiver_attestation_boundary_exhausted") is True
        )
    if outcome == OUTCOME_NOT_ALLOWED:
        return (
            boundary.get("receiver_attestation_boundary_result")
            == BOUNDARY_RESULT_NOT_ALLOWED
            and boundary.get("receiver_attestation_boundary_recorded") is True
            and boundary.get("receiver_attestation_boundary_result_recorded")
            is True
            and boundary.get("receiver_attestation_consideration_allowed")
            is False
            and boundary.get(
                "receiver_attestation_consideration_not_allowed"
            )
            is True
            and boundary.get("receiver_attestation_boundary_exhausted") is True
        )
    return (
        boundary.get("receiver_attestation_boundary_result")
        == BOUNDARY_RESULT_NOT_EVALUATED
        and boundary.get("receiver_attestation_boundary_recorded") is False
        and boundary.get("receiver_attestation_boundary_result_recorded")
        is False
        and boundary.get("receiver_attestation_consideration_allowed") is False
        and boundary.get("receiver_attestation_consideration_not_allowed")
        is False
        and boundary.get("receiver_attestation_boundary_exhausted") is False
    )


def write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid deterministic result without silent overwrite."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error(
            "WRITE_REFUSED: result must be a mapping"
        )
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
    ):
        raise ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error(
            "WRITE_REFUSED: incompatible result metadata"
        )
    if not _declared_non_claims_valid(result.get("non_claims")):
        raise ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error(
            "WRITE_REFUSED: non-claims are not canonical false"
        )
    if not _result_branch_valid(result):
        raise ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error(
            "WRITE_REFUSED: result branch posture is inconsistent"
        )
    if _contains_complete_material(result):
        raise ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error(
            "WRITE_REFUSED: complete operation, basis, or capture material present"
        )
    target = (
        _as_repo_path(output_path)
        if output_path is not None
        else OUTPUT_ROOT / OUTPUT_FILENAME
    )
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error(
            "WRITE_REFUSED: output path is protected or belongs to upstream lineage"
        )
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
        raise ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
