"""Resolve one bounded authored declaration digest/custody operation result.

Only explicitly supplied V2 and optional V1 files may be streamed to SHA-256.
No PDF bytes, extracted text, standing, audit change, or downstream authority is
returned or created.
"""

from __future__ import annotations

import copy
import hashlib
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateAuthoredScopeDivisionDeclarationDigestCustodyOperationV0MinError(Exception):
    """Raised for bounded digest/custody path and write failures."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min"

OPERATION_ID = "descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_001"
OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EXACT_AUTHORED_DECLARATION_FILE_DIGEST_AND_CUSTODY_POSTURE_ONLY"
UPSTREAM_RECEIPT_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION"
UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_RECORDED"
UPSTREAM_RECEIPT_STATUS_REQUIRED = "RECEIVED_AS_METADATA_FOR_AUDIT_ONLY"
UPSTREAM_AUDIT_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION"
UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_SATISFIES_MISSING_BASIS_REQUIREMENTS"
UPSTREAM_AUDIT_RESULT_REQUIRED = "SATISFIES_MISSING_BASIS_REQUIREMENTS"
UPSTREAM_DECLARATION_ACCEPTED_AS_BASIS_REQUIRED = True
TARGET_PRIMARY_MATERIAL_FILENAME = "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION V.2.pdf"
TARGET_PRIMARY_MATERIAL_VERSION = "v2"
TARGET_PRIMARY_MATERIAL_DATE = "10 July 2026"
TARGET_PRIMARY_MATERIAL_AUTHOR = "Marko Markota"
TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE = "AUTHORSHIP_ATTESTATION_ONLY"
TARGET_PREDECESSOR_MATERIAL_FILENAME = "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION v1"
TARGET_PREDECESSOR_MATERIAL_ROLE = "REFERENCED_PREDECESSOR_ONLY"
DIGEST_ALGORITHM_ALLOWED = "SHA-256"
CUSTODY_POSTURE_SCOPE = "FILE_IDENTITY_AND_LOCAL_CUSTODY_POSTURE_ONLY"
ADMISSIBLE_FUTURE_ROUTE = "DIGEST_CUSTODY_THEN_SUCCESSOR_CLOSURE_ONLY"

OUTCOME_RECORDED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION_RECORDED"
OUTCOME_REQUIRES_MATERIAL = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION_REQUIRES_MATERIAL"
OUTCOME_BLOCKED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (OUTCOME_RECORDED, OUTCOME_REQUIRES_MATERIAL, OUTCOME_BLOCKED, OUTCOME_NOT_RECORDED)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min")
DETERMINISTIC_FILENAME = "descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_001__authored_scope_division_declaration_digest_custody_operation_v0_min_result.json"

DEFAULT_OPERATION_SPEC_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION_V0_MIN_SPEC.md"
DEFAULT_RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"

CUSTODY_POSTURES = (
    "LOCAL_OPERATOR_HELD_SOURCE_ARTIFACT",
    "LOCAL_OPERATOR_HELD_SIGNED_SOURCE_ARTIFACT",
    "LOCAL_OPERATOR_HELD_PREDECESSOR_SOURCE_ARTIFACT",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "digest_custody_operation_recorded",
    "digest_computed",
    "digest_recorded",
    "custody_posture_recorded",
    "primary_material_digest_recorded",
    "primary_material_custody_recorded",
    "predecessor_material_digest_recorded",
    "predecessor_material_custody_recorded",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "digest_treated_as_truth",
    "hash_treated_as_standing",
    "custody_treated_as_standing",
    "pdf_ingested",
    "pdf_copied_to_repo",
    "text_extracted",
    "raw_pdf_returned",
    "raw_extracted_text_returned",
    "audit_performed",
    "audit_result_changed",
    "declaration_accepted_as_basis_changed",
    "declaration_admitted_as_standing_basis",
    "candidate_a_scope_declared",
    "candidate_b_scope_declared",
    "basis_bearing_scope_division_declared",
    "basis_gap_closed",
    "candidate_specific_content_emitted",
    "separate_seal_material_emitted",
    "separate_lineage_receipt_material_emitted",
    "separate_digest_material_emitted",
    "candidate_specific_distinctness_basis_emission_operation_rerun",
    "distinctness_operation_rerun",
    "distinctness_supported_recorded",
    "candidate_records_marked_distinct",
    "candidate_records_distinct",
    "candidate_standing_authorized",
    "candidate_standing_created",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_created",
    "standing_authorized",
    "standing_descendant_created",
    "descendant_standing_check_performed",
    "crossing_authorized",
    "first_crossing_authorized",
    "relation_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "currentness_created",
    "authority_created",
    "standing_created",
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
    "synchronization_authorized",
    "coupling_assigned_to_candidate_a",
    "coupling_assigned_to_candidate_b",
    "coupling_created",
    "third_candidate_created",
    "third_model_admitted",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "valid_derivation_event_recorded",
    "affected_file_repaired",
    "affected_file_edited",
    "affected_file_deleted",
    "affected_file_overwritten",
    "affected_file_replaced",
    "affected_file_redeemed",
    "affected_file_treated_as_clean_basis",
    "contaminated_lineage_treated_as_clean_basis",
    "authored_scope_division_declaration_receipt_operation_overridden",
    "authored_scope_division_declaration_receipt_operation_bypassed",
    "authored_scope_division_declaration_audit_operation_overridden",
    "authored_scope_division_declaration_audit_operation_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_digest_permission_to_digest_completion_conversion",
    "direct_custody_permission_to_custody_completion_conversion",
    "direct_digest_result_to_truth_conversion",
    "direct_hash_result_to_standing_conversion",
    "direct_custody_posture_to_standing_conversion",
    "direct_file_identity_to_standing_conversion",
    "direct_digest_custody_to_audit_result_conversion",
    "direct_digest_custody_to_accepted_basis_conversion",
    "direct_digest_custody_to_standing_basis_conversion",
    "direct_digest_custody_to_scope_declaration_conversion",
    "direct_digest_custody_to_basis_gap_closure_conversion",
    "direct_digest_custody_to_candidate_specific_basis_emission_conversion",
    "direct_digest_custody_to_distinctness_support_conversion",
    "direct_digest_custody_to_candidate_records_distinct_conversion",
    "direct_digest_custody_to_candidate_standing_conversion",
    "direct_digest_custody_to_descendant_body_creation",
    "direct_digest_custody_to_relation_creation",
    "direct_digest_custody_to_runtime_creation",
    "direct_digest_custody_to_authority_currentness_creation",
    "direct_digest_custody_to_coupling_creation",
    "direct_digest_custody_to_third_candidate_route",
    "direct_digest_custody_to_third_model_route",
    "direct_digest_custody_to_follow_on_work",
    "raw_pdf_return_route",
    "raw_extracted_text_return_route",
    "copy_pdf_into_repo_route",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING", "UNSUPPORTED_INTENT", "DIGEST_CUSTODY_OPERATION_SPEC_REFERENCE_MISSING", "DIGEST_CUSTODY_OPERATION_SPEC_MARKER_MISSING",
    "RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "RECEIPT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "AUDIT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING", "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING", "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "MATERIAL_REFERENCE_MISSING", "MATERIAL_REFERENCE_INVALID", "MATERIAL_FILE_NOT_FOUND", "MATERIAL_REFERENCE_NOT_FILE", "MATERIAL_FILENAME_MISMATCH",
    "DIGEST_ALGORITHM_UNSUPPORTED", "CUSTODY_POSTURE_MISSING_OR_UNSUPPORTED", "NON_CLAIM_MISSING_OR_FLIPPED",
    "PROHIBITED_DIGEST_TO_TRUTH_REQUESTED", "PROHIBITED_HASH_OR_CUSTODY_TO_STANDING_REQUESTED", "PROHIBITED_DIGEST_CUSTODY_TO_AUDIT_OR_ACCEPTED_BASIS_REQUESTED",
    "PROHIBITED_SCOPE_OR_BASIS_GAP_CLOSURE_REQUESTED", "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED", "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED", "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED", "REQUESTED_RAW_PDF_RETURN",
    "REQUESTED_RAW_EXTRACTED_TEXT_RETURN", "REQUESTED_PDF_COPY_INTO_REPO", "EXPLICIT_BLOCK_REQUESTED", "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_digest_as_truth": "PROHIBITED_DIGEST_TO_TRUTH_REQUESTED",
    "request_hash_as_standing": "PROHIBITED_HASH_OR_CUSTODY_TO_STANDING_REQUESTED",
    "request_custody_as_standing": "PROHIBITED_HASH_OR_CUSTODY_TO_STANDING_REQUESTED",
    "request_file_identity_as_standing": "PROHIBITED_HASH_OR_CUSTODY_TO_STANDING_REQUESTED",
    "request_digest_custody_to_audit_result": "PROHIBITED_DIGEST_CUSTODY_TO_AUDIT_OR_ACCEPTED_BASIS_REQUESTED",
    "request_digest_custody_to_accepted_basis": "PROHIBITED_DIGEST_CUSTODY_TO_AUDIT_OR_ACCEPTED_BASIS_REQUESTED",
    "request_digest_custody_to_standing_basis": "PROHIBITED_DIGEST_CUSTODY_TO_AUDIT_OR_ACCEPTED_BASIS_REQUESTED",
    "request_candidate_a_scope_declaration": "PROHIBITED_SCOPE_OR_BASIS_GAP_CLOSURE_REQUESTED",
    "request_candidate_b_scope_declaration": "PROHIBITED_SCOPE_OR_BASIS_GAP_CLOSURE_REQUESTED",
    "request_basis_bearing_scope_division_declaration": "PROHIBITED_SCOPE_OR_BASIS_GAP_CLOSURE_REQUESTED",
    "request_basis_gap_closure": "PROHIBITED_SCOPE_OR_BASIS_GAP_CLOSURE_REQUESTED",
    "request_candidate_specific_content_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_separate_seal_material_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_separate_lineage_receipt_material_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_separate_digest_material_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_basis_emission_operation_rerun": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_distinctness_operation_rerun": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_distinctness_supported_recording": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_candidate_records_marked_distinct": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_candidate_standing_authorization": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_descendant_body_creation": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_crossing_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_relation_creation": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_runtime_creation": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_api_creation": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_currentness_creation": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_authority_creation": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_output_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_action_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_derivative_reception_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_coupling_assignment_to_candidate_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_candidate_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_model_admission": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_follow_on_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "return_raw_pdf": "REQUESTED_RAW_PDF_RETURN",
    "return_raw_extracted_text": "REQUESTED_RAW_EXTRACTED_TEXT_RETURN",
    "copy_pdf_into_repo": "REQUESTED_PDF_COPY_INTO_REPO",
}

SENSITIVE_BODY_KEYS = {"raw_pdf", "raw_pdf_body", "raw_material_body", "raw_extracted_text", "extracted_text", "full_text", "full_body", "source_body", "hidden_repo_state", "current_working_tree"}

OPERATION_SPEC_MARKER_CLASSES = (
    ("operation_identity", ("Descendant Body Candidate Authored Scope Division Declaration Digest Custody Operation V0 Minimum Specification", OPERATION_TYPE, OPERATION_ID, OPERATION_SCOPE)),
    ("upstream_receipt", (UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, UPSTREAM_RECEIPT_STATUS_REQUIRED, TARGET_PRIMARY_MATERIAL_FILENAME, TARGET_PRIMARY_MATERIAL_VERSION, TARGET_PRIMARY_MATERIAL_DATE, TARGET_PRIMARY_MATERIAL_AUTHOR, TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE, TARGET_PREDECESSOR_MATERIAL_FILENAME, TARGET_PREDECESSOR_MATERIAL_ROLE)),
    ("upstream_audit", (UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "SATISFIES_MISSING_BASIS_REQUIREMENTS", "declaration_accepted_as_basis = true", "declaration_admitted_as_standing_basis = false", "candidate_a_scope_declared = false", "candidate_b_scope_declared = false", "basis_bearing_scope_division_declared = false", "basis_gap_closed = false")),
    ("digest_custody_non_standing", ("Digest/custody permission is not digest/custody completion", "Digest is not truth.", "Hash, custody, and file identity are not standing.", "File custody is not audit result, accepted basis, standing basis, scope declaration, or basis-gap closure.", "Digest/custody result is not standing, scope declaration, basis-gap closure", "Accepted basis remains non-standing")),
    ("permitted_route", ("A future digest/custody resolver may compute SHA-256 for a supplied V2 declaration file.", "It may optionally compute SHA-256 for a supplied V1 predecessor file.", "It must not return PDF bytes or raw extracted text and must preserve digest, hash, and custody as non-standing.")),
    ("receipt_relation", (UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 91", UPSTREAM_RECEIPT_STATUS_REQUIRED, "digest_recorded = false", "custody_posture_recorded = false", "text_extraction_posture_recorded = false")),
    ("audit_relation", (UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "passed_check_count = 83", "audit_result = SATISFIES_MISSING_BASIS_REQUIREMENTS", "declaration_accepted_as_basis = true", "an empty missing-criteria list", "false standing, scope-declaration, and basis-gap-closure postures")),
    ("scope_relation", ("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS", "non-cosmetic candidate A scope declaration", "non-cosmetic candidate B scope declaration", "basis-bearing scope division declaration", "does not close the gap")),
    ("contaminated_lineage", ("DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md", "preserved contaminated lineage", "descendant_body_basis_candidate_a_created = true", "descendant_body_basis_candidate_b_created = true", "descendant_body_basis_derivation_event_recorded = true", "UNSUPPORTED", "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file")),
    ("blocked_routes", ("direct digest permission to digest completion; direct custody permission to custody completion", "direct digest result to truth; hash result to standing; custody posture or file identity to standing", "direct digest/custody to audit result, accepted basis, standing basis, scope declaration, basis-gap closure", "raw PDF return, raw extracted-text return, and copy-PDF-into-repo routes", "repository scan, affected-file repair, and prior unsupported-claim validation routes")),
    ("closing_lock", ("This operation spec defines only a future digest/custody operation shape", "Digest/custody permission is not digest/custody completion", "Digest is not truth", "Hash is not standing", "Custody is not standing", "File identity is not standing", "Accepted basis remains non-standing", "Open means not scheduled, not authorized, and not executed")),
)

UPSTREAM_REQUIREMENTS = (
    ("receipt_operation_terminal_summary_reference", DEFAULT_RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE, "RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "RECEIPT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", (UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 91", UPSTREAM_RECEIPT_STATUS_REQUIRED, "digest_recorded = false", "custody_posture_recorded = false", "text_extraction_posture_recorded = false"), "receipt_operation_terminal_summary_markers_present"),
    ("audit_operation_terminal_summary_reference", DEFAULT_AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE, "AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "AUDIT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", (UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 83", "audit_result = SATISFIES_MISSING_BASIS_REQUIREMENTS", "declaration_accepted_as_basis = true", "missing_or_insufficient_audit_criteria = []", "Accepted basis is not standing basis.", "Candidate A scope, Candidate B scope, and basis-bearing scope division were not declared as standing. The basis gap was not closed."), "audit_operation_terminal_summary_markers_present"),
    ("scope_division_declaration_operation_terminal_summary_reference", DEFAULT_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE, "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", ("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS", "missing non-cosmetic candidate A scope declaration", "missing non-cosmetic candidate B scope declaration", "missing basis-bearing scope division declaration"), "scope_division_declaration_operation_terminal_summary_markers_present"),
    ("existence_claim_evidence_check_terminal_summary_reference", DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE, "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING", "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING", ("UNSUPPORTED",), "existence_claim_evidence_check_terminal_summary_markers_present"),
    ("distinctness_operation_terminal_summary_reference", DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE, "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", ("NOT_DISTINCT",), "distinctness_operation_terminal_summary_markers_present"),
    ("basis_emission_operation_terminal_summary_reference", DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE, "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", ("REQUIRES_ADDITIONAL_BASIS",), "basis_emission_operation_terminal_summary_markers_present"),
    ("scope_division_declaration_boundary_terminal_summary_reference", DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE, "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING", "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING", ("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",), "scope_division_declaration_boundary_terminal_summary_markers_present"),
)

WHAT_REMAINS_OPEN = (
    "successor operation to close additional-basis gap, if separately bounded after audit and digest/custody if recorded", "candidate-specific distinctness basis emission operation successor", "actual candidate-specific content emission", "actual separate seal material emission", "actual separate lineage receipt material emission", "actual separate digest material emission", "future distinctness-supported operation result", "divergent receipt-history route, if separately bounded", "carrier separation route, if separately bounded", "candidate standing checks", "first crossing", "relation", "FIELD machinery", "runtime", "API", "currentness", "authority", "standing", "output authorization", "action authorization", "derivative reception", "synchronization", "externalization boundary", "follow-on work",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _resolve_path(value: Any) -> Path | None:
    if isinstance(value, Path):
        path = value
    elif _is_non_empty_string(value):
        path = Path(value)
    else:
        return None
    return path if path.is_absolute() else REPO_ROOT / path


def _read_text(value: Any) -> str | None:
    path = _resolve_path(value)
    if path is None or not path.is_file():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def _is_sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return (
        lowered in SENSITIVE_BODY_KEYS
        or lowered.endswith("_body")
        or "raw_" in lowered
        or any(token in lowered for token in ("extracted_text", "file_bytes", "pdf_bytes", "binary", "payload"))
    )


def _sanitize(value: Any, key: str = "") -> Any:
    if _is_sensitive_key(key):
        return "[REDACTED_SENSITIVE_BODY]"
    if isinstance(value, (bytes, bytearray, memoryview)):
        return "[REDACTED_BINARY_CONTENT]"
    if isinstance(value, Mapping):
        return {str(item_key): _sanitize(item, str(item_key)) for item_key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        text = value.strip()
        return text if len(text) <= 420 else f"{text[:420]}...[truncated]"
    return value


def _json_ready(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value


def _add_check(checks: list[dict[str, Any]], name: str, passed: bool, expected: Any, actual: Any, code: str | None = None) -> None:
    check: dict[str, Any] = {"check_name": name, "passed": bool(passed), "expected_posture": _sanitize(expected), "actual_posture": _sanitize(actual)}
    if not passed and code:
        check["block_code"] = code
        check["failure_code"] = code
    checks.append(check)


def _failed_codes(checks: list[dict[str, Any]]) -> list[str]:
    return [str(check.get("block_code") or check.get("failure_code")) for check in checks if check.get("passed") is False and isinstance(check.get("block_code") or check.get("failure_code"), str) and (check.get("block_code") or check.get("failure_code")) in BLOCK_CODES]


def _validate_reference(checks: list[dict[str, Any]], request: Mapping[str, Any], field: str, code: str) -> None:
    path = _resolve_path(request.get(field))
    _add_check(checks, f"{field} readable file reference", path is not None and path.is_file(), "declared readable file path", str(path) if path else request.get(field), code)


def _validate_non_claims(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    declared = request.get("declared_non_claims")
    malformed = list(REQUIRED_FALSE_NON_CLAIMS) if not isinstance(declared, Mapping) else [key for key in REQUIRED_FALSE_NON_CLAIMS if declared.get(key) is not False]
    _add_check(checks, "required non-claims false", not malformed, "mapping with every required false key exactly false", {"malformed_keys": malformed}, "NON_CLAIM_MISSING_OR_FLIPPED")


def _forbidden_code(key: str) -> str:
    if key in {"digest_treated_as_truth", "direct_digest_result_to_truth_conversion"}:
        return "PROHIBITED_DIGEST_TO_TRUTH_REQUESTED"
    if key in {"hash_treated_as_standing", "custody_treated_as_standing", "direct_hash_result_to_standing_conversion", "direct_custody_posture_to_standing_conversion", "direct_file_identity_to_standing_conversion"}:
        return "PROHIBITED_HASH_OR_CUSTODY_TO_STANDING_REQUESTED"
    if "audit_result" in key or "accepted_basis" in key:
        return "PROHIBITED_DIGEST_CUSTODY_TO_AUDIT_OR_ACCEPTED_BASIS_REQUESTED"
    if key in {"candidate_a_scope_declared", "candidate_b_scope_declared", "basis_bearing_scope_division_declared", "basis_gap_closed"} or "scope_declaration" in key or "basis_gap" in key:
        return "PROHIBITED_SCOPE_OR_BASIS_GAP_CLOSURE_REQUESTED"
    if any(token in key for token in ("coupling", "third_candidate", "third_model")):
        return "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    if any(token in key for token in ("repair", "scan", "discovery", "validation", "unsupported", "overwrite", "edited", "deleted", "replaced", "redeemed")):
        return "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED"
    if any(token in key for token in ("standing", "distinct", "descendant_body")):
        return "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED"
    return "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED"


def _validate_top_level_postures(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if request.get(key) is True:
            _add_check(checks, f"top-level required false posture {key} not pre-claimed", False, False, True, _forbidden_code(key))
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        if request.get(key) is True:
            _add_check(checks, f"result-only posture {key} not pre-claimed", False, "resolver result posture only", True, "MATERIAL_REFERENCE_INVALID")


def _validate_prohibited_requests(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        _add_check(checks, f"{field} not requested", request.get(field) is not True, False, request.get(field), code)


def _marker_classes_present(text: str | None) -> tuple[bool, list[str]]:
    if text is None:
        return False, [name for name, _ in OPERATION_SPEC_MARKER_CLASSES]
    missing = [name for name, markers in OPERATION_SPEC_MARKER_CLASSES if not all(marker in text for marker in markers)]
    return not missing, missing


def _validate_spec_and_upstream(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> dict[str, bool]:
    text = _read_text(request.get("operation_spec_reference"))
    passed, missing = _marker_classes_present(text)
    _add_check(checks, "target digest/custody operation spec posture classes present", passed, "all target digest/custody posture classes", {"missing_posture_classes": missing}, "DIGEST_CUSTODY_OPERATION_SPEC_MARKER_MISSING")
    flags = {"target_digest_custody_operation_spec_markers_present": passed}
    for field, _, missing_code, marker_code, markers, flag in UPSTREAM_REQUIREMENTS:
        upstream_text = _read_text(request.get(field))
        found = upstream_text is not None and all(marker in upstream_text for marker in markers)
        _add_check(checks, f"{field} expected markers present", found, markers, {"reference_readable": upstream_text is not None, "missing_markers": [] if found else list(markers)}, missing_code if upstream_text is None else marker_code)
        flags[flag] = found
    return flags


def _validate_exact_values(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    expected = (
        ("operation_id", OPERATION_ID), ("operation_type", OPERATION_TYPE), ("operation_version", OPERATION_VERSION), ("operation_scope", OPERATION_SCOPE),
        ("authored_scope_division_declaration_digest_custody_operation_id", OPERATION_ID), ("authored_scope_division_declaration_digest_custody_operation_type", OPERATION_TYPE), ("authored_scope_division_declaration_digest_custody_operation_version", OPERATION_VERSION), ("authored_scope_division_declaration_digest_custody_operation_scope", OPERATION_SCOPE),
        ("upstream_receipt_operation_type", UPSTREAM_RECEIPT_OPERATION_TYPE), ("upstream_receipt_operation_outcome_required", UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED), ("upstream_receipt_status_required", UPSTREAM_RECEIPT_STATUS_REQUIRED),
        ("upstream_audit_operation_type", UPSTREAM_AUDIT_OPERATION_TYPE), ("upstream_audit_operation_outcome_required", UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED), ("upstream_audit_result_required", UPSTREAM_AUDIT_RESULT_REQUIRED), ("upstream_declaration_accepted_as_basis_required", UPSTREAM_DECLARATION_ACCEPTED_AS_BASIS_REQUIRED),
        ("target_primary_material_filename", TARGET_PRIMARY_MATERIAL_FILENAME), ("target_primary_material_version", TARGET_PRIMARY_MATERIAL_VERSION), ("target_primary_material_date", TARGET_PRIMARY_MATERIAL_DATE), ("target_primary_material_author", TARGET_PRIMARY_MATERIAL_AUTHOR), ("target_primary_material_signature_role", TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE), ("target_predecessor_material_filename", TARGET_PREDECESSOR_MATERIAL_FILENAME), ("target_predecessor_material_role", TARGET_PREDECESSOR_MATERIAL_ROLE), ("digest_algorithm", DIGEST_ALGORITHM_ALLOWED), ("custody_posture_scope", CUSTODY_POSTURE_SCOPE), ("admissible_future_route", ADMISSIBLE_FUTURE_ROUTE),
    )
    for field, value in expected:
        code = "DIGEST_ALGORITHM_UNSUPPORTED" if field == "digest_algorithm" else "MATERIAL_REFERENCE_INVALID"
        _add_check(checks, f"{field} exact", request.get(field) == value, value, request.get(field), code)


def _stream_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_material(
    checks: list[dict[str, Any]], value: Any, expected_name: str, custody: Any, required: bool
) -> tuple[Path | None, str | None, str | None]:
    if value is None and not required:
        return None, None, None
    if value is None:
        return None, None, None
    path = _resolve_path(value)
    _add_check(checks, f"{expected_name} material reference valid", path is not None, "explicit path string", value, "MATERIAL_REFERENCE_INVALID")
    if path is None:
        return None, None, None
    _add_check(checks, f"{expected_name} material file exists", path.exists(), "existing explicit path", str(path), "MATERIAL_FILE_NOT_FOUND")
    _add_check(checks, f"{expected_name} material reference is file", path.is_file(), "file", str(path), "MATERIAL_REFERENCE_NOT_FILE")
    expected = request_name = expected_name
    if isinstance(value, Mapping):
        request_name = str(value.get("filename", expected_name))
    _add_check(checks, f"{expected_name} material filename exact", path.name == request_name, request_name, path.name, "MATERIAL_FILENAME_MISMATCH")
    custody_value = custody
    _add_check(checks, f"{expected_name} custody posture bounded", custody_value in CUSTODY_POSTURES, CUSTODY_POSTURES, custody_value, "CUSTODY_POSTURE_MISSING_OR_UNSUPPORTED")
    if not (path.exists() and path.is_file() and path.name == request_name and custody_value in CUSTODY_POSTURES):
        return None, None, None
    try:
        return path, _stream_sha256(path), str(custody_value)
    except OSError as exc:
        _add_check(checks, f"{expected_name} material bytes streamable", False, "streamable explicit file", str(exc), "MATERIAL_FILE_NOT_FOUND")
        return None, None, None


def _material_reference(value: Any) -> Any:
    if isinstance(value, Mapping):
        return value.get("path")
    return value


def _material_name(request: Mapping[str, Any], field: str, default: str) -> str:
    value = request.get(field)
    if isinstance(value, Mapping) and _is_non_empty_string(value.get("filename")):
        return str(value["filename"])
    return default


def _material_details(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> dict[str, Any]:
    primary_reference = request.get("primary_material_path")
    predecessor_reference = request.get("predecessor_material_path")
    primary_value = _material_reference(primary_reference)
    predecessor_value = _material_reference(predecessor_reference)
    predecessor_name = _material_name(request, "predecessor_material_path", TARGET_PREDECESSOR_MATERIAL_FILENAME)
    if primary_reference is None:
        predecessor_path, predecessor_digest, predecessor_custody = _validate_material(
            checks,
            predecessor_value,
            predecessor_name,
            request.get("predecessor_material_custody_posture"),
            False,
        )
        return {"primary_missing": True, "primary_path": None, "primary_digest": None, "primary_custody": None, "predecessor_path": predecessor_path, "predecessor_digest": predecessor_digest, "predecessor_custody": predecessor_custody}
    primary_path, primary_digest, primary_custody = _validate_material(
        checks,
        primary_value,
        TARGET_PRIMARY_MATERIAL_FILENAME,
        request.get("primary_material_custody_posture"),
        True,
    )
    predecessor_path, predecessor_digest, predecessor_custody = _validate_material(checks, predecessor_value, predecessor_name, request.get("predecessor_material_custody_posture"), False)
    return {"primary_missing": False, "primary_path": primary_path, "primary_digest": primary_digest, "primary_custody": primary_custody, "predecessor_path": predecessor_path, "predecessor_digest": predecessor_digest, "predecessor_custody": predecessor_custody}


def _marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    names = {"target_digest_custody_operation_spec_markers_present": "target digest/custody operation spec posture classes present"}
    names.update({flag: f"{field} expected markers present" for field, *_, flag in UPSTREAM_REQUIREMENTS})
    return {key: any(check.get("check_name") == name and check.get("passed") is True for check in checks) for key, name in names.items()}


def _operation_object(request: Mapping[str, Any], outcome: str, material: Mapping[str, Any], flags: Mapping[str, bool]) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    primary_recorded = bool(recorded and material.get("primary_digest"))
    predecessor_recorded = bool(recorded and material.get("predecessor_digest"))
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID, "operation_type": OPERATION_TYPE, "operation_version": OPERATION_VERSION, "operation_scope": OPERATION_SCOPE,
        "authored_scope_division_declaration_digest_custody_operation_id": OPERATION_ID, "authored_scope_division_declaration_digest_custody_operation_type": OPERATION_TYPE, "authored_scope_division_declaration_digest_custody_operation_version": OPERATION_VERSION, "authored_scope_division_declaration_digest_custody_operation_scope": OPERATION_SCOPE,
        "upstream_receipt_operation_type": UPSTREAM_RECEIPT_OPERATION_TYPE, "upstream_receipt_operation_outcome_required": UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "upstream_receipt_status_required": UPSTREAM_RECEIPT_STATUS_REQUIRED,
        "upstream_audit_operation_type": UPSTREAM_AUDIT_OPERATION_TYPE, "upstream_audit_operation_outcome_required": UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "upstream_audit_result_required": UPSTREAM_AUDIT_RESULT_REQUIRED, "upstream_declaration_accepted_as_basis_required": UPSTREAM_DECLARATION_ACCEPTED_AS_BASIS_REQUIRED,
        "target_primary_material_filename": TARGET_PRIMARY_MATERIAL_FILENAME, "target_primary_material_version": TARGET_PRIMARY_MATERIAL_VERSION, "target_primary_material_date": TARGET_PRIMARY_MATERIAL_DATE, "target_primary_material_author": TARGET_PRIMARY_MATERIAL_AUTHOR, "target_primary_material_signature_role": TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE,
        "target_predecessor_material_filename": TARGET_PREDECESSOR_MATERIAL_FILENAME, "target_predecessor_material_role": TARGET_PREDECESSOR_MATERIAL_ROLE,
        "digest_algorithm": DIGEST_ALGORITHM_ALLOWED, "custody_posture_scope": CUSTODY_POSTURE_SCOPE, "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        **_canonical_non_claims(), **flags,
    }
    operation.update({
        "digest_custody_operation_recorded": recorded, "digest_computed": recorded, "digest_recorded": recorded, "custody_posture_recorded": recorded,
        "primary_material_digest_recorded": primary_recorded, "primary_material_custody_recorded": primary_recorded,
        "predecessor_material_digest_recorded": predecessor_recorded, "predecessor_material_custody_recorded": predecessor_recorded,
        "primary_material_digest_sha256": material.get("primary_digest") if primary_recorded else None,
        "predecessor_material_digest_sha256": material.get("predecessor_digest") if predecessor_recorded else None,
        "primary_material_custody_posture": material.get("primary_custody") if primary_recorded else None,
        "predecessor_material_custody_posture": material.get("predecessor_custody") if predecessor_recorded else None,
        "primary_material_path_basename": material["primary_path"].name if primary_recorded else None,
        "predecessor_material_path_basename": material["predecessor_path"].name if predecessor_recorded else None,
    })
    return operation


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation")
    op = operation if isinstance(operation, Mapping) else {}
    checks = result.get("authored_scope_division_declaration_digest_custody_operation_checks")
    records = checks if isinstance(checks, list) else []
    upstream = result.get("upstream_basis")
    upstream_map = upstream if isinstance(upstream, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"), "failed_check_count": sum(1 for check in records if isinstance(check, Mapping) and check.get("passed") is False), "passed_check_count": sum(1 for check in records if isinstance(check, Mapping) and check.get("passed") is True),
        "result_version": RESULT_VERSION, "resolver_module": RESOLVER_MODULE,
        "operation_id": op.get("operation_id"), "operation_type": op.get("operation_type"), "operation_version": op.get("operation_version"), "operation_scope": op.get("operation_scope"),
        "upstream_receipt_operation_type": op.get("upstream_receipt_operation_type"), "upstream_receipt_operation_outcome_required": op.get("upstream_receipt_operation_outcome_required"), "upstream_receipt_status_required": op.get("upstream_receipt_status_required"),
        "upstream_audit_operation_type": op.get("upstream_audit_operation_type"), "upstream_audit_operation_outcome_required": op.get("upstream_audit_operation_outcome_required"), "upstream_audit_result_required": op.get("upstream_audit_result_required"),
        "selected_target_spec_path": upstream_map.get("operation_spec_reference"), "completed_receipt_operation_terminal_summary_path": upstream_map.get("receipt_operation_terminal_summary_reference"), "completed_audit_operation_terminal_summary_path": upstream_map.get("audit_operation_terminal_summary_reference"),
        "result_level_non_claims_canonical_false": all(isinstance(result.get("non_claims"), Mapping) and result["non_claims"].get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS),
    }
    for key in ("target_primary_material_filename", "target_primary_material_version", "target_primary_material_date", "target_primary_material_author", "target_primary_material_signature_role", "target_predecessor_material_filename", "target_predecessor_material_role", "digest_algorithm", "digest_custody_operation_recorded", "digest_computed", "digest_recorded", "custody_posture_recorded", "primary_material_digest_recorded", "predecessor_material_digest_recorded", "primary_material_custody_recorded", "predecessor_material_custody_recorded", "primary_material_digest_sha256", "predecessor_material_digest_sha256", "primary_material_custody_posture", "predecessor_material_custody_posture", *REQUIRED_FALSE_NON_CLAIMS, "target_digest_custody_operation_spec_markers_present", *[flag for *_, flag in UPSTREAM_REQUIREMENTS]):
        summary[key] = op.get(key)
    return _sanitize(summary)


def build_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return compact digest/custody result metadata without file bodies."""

    return _build_summary(result)


def _build_result(request: Mapping[str, Any], outcome: str, checks: list[dict[str, Any]], material: Mapping[str, Any], block_code: str | None = None, block_reason: str | None = None) -> dict[str, Any]:
    flags = _marker_flags(checks)
    operation = _operation_object(request, outcome, material, flags)
    result: dict[str, Any] = {
        "authored_scope_division_declaration_digest_custody_operation_metadata": {"operation_id": OPERATION_ID, "result_version": RESULT_VERSION, "resolver_module": RESOLVER_MODULE, "generated_at": _utc_now()},
        "declared_authored_scope_division_declaration_digest_custody_operation_basis": _sanitize(request),
        "upstream_basis": {"operation_spec_reference": request.get("operation_spec_reference"), **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS}, **flags},
        "descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation": operation,
        "authored_scope_division_declaration_digest_custody_operation_checks": checks,
        "authored_scope_division_declaration_digest_custody_operation_statement": {"outcome": outcome, "digest_custody_operation_recorded": operation["digest_custody_operation_recorded"], "digest_computed": operation["digest_computed"], "digest_recorded": operation["digest_recorded"], "custody_posture_recorded": operation["custody_posture_recorded"], "result_level_non_claims_canonical_false": True},
        "authored_scope_division_declaration_digest_custody_operation_non_meaning": {"not_truth": True, "not_standing": True, "not_audit_change": True, "not_scope_declaration": True, "not_basis_gap_closure": True, "not_distinctness": True, "not_candidate_standing": True, "not_descendant_body_creation": True, "not_relation": True, "not_runtime": True, "not_authority": True, "not_coupling": True, "not_third_candidate_or_model": True, "not_follow_on": True},
        "material_identity": {"primary_material_path_basename": operation["primary_material_path_basename"], "predecessor_material_path_basename": operation["predecessor_material_path_basename"], "pdf_ingested": False, "pdf_copied_to_repo": False, "text_extracted": False},
        "digest_custody_result_detail": {"digest_algorithm": operation["digest_algorithm"], "primary_material_digest_sha256": operation["primary_material_digest_sha256"], "predecessor_material_digest_sha256": operation["predecessor_material_digest_sha256"], "primary_material_custody_posture": operation["primary_material_custody_posture"], "predecessor_material_custody_posture": operation["predecessor_material_custody_posture"], "primary_material_required": True, "primary_material_supplied": not material.get("primary_missing", False)},
        "permitted_future_route": ["digest/custody may stream explicitly supplied declaration files for SHA-256 only", "digest, hash, and custody remain non-standing", "only a separately bounded successor closure may later consider the gap"],
        "blocked_routes": ["truth, standing, audit-change, scope, basis-gap, distinctness, downstream, raw-return, copy, repair, scan, and validation conversion routes"],
        "what_remains_open": list(WHAT_REMAINS_OPEN), "non_claims": _canonical_non_claims(), "outcome": outcome,
        "block": {"blocked": outcome == OUTCOME_BLOCKED, "code": block_code if outcome == OUTCOME_BLOCKED else None, "block_code": block_code if outcome == OUTCOME_BLOCKED else None, "reason": block_reason if outcome == OUTCOME_BLOCKED else None},
    }
    result["authored_scope_division_declaration_digest_custody_operation_summary"] = _build_summary(result)
    return result


def _blocked_result(request: Mapping[str, Any], checks: list[dict[str, Any]], code: str, reason: str) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(request, OUTCOME_BLOCKED, checks, {"primary_missing": True}, code, reason)


def build_declared_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_request(**overrides: Any) -> dict[str, Any]:
    """Build a no-discovery digest/custody request with no material path by default."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD, "operation_id": OPERATION_ID, "operation_type": OPERATION_TYPE, "operation_version": OPERATION_VERSION, "operation_scope": OPERATION_SCOPE,
        "authored_scope_division_declaration_digest_custody_operation_id": OPERATION_ID, "authored_scope_division_declaration_digest_custody_operation_type": OPERATION_TYPE, "authored_scope_division_declaration_digest_custody_operation_version": OPERATION_VERSION, "authored_scope_division_declaration_digest_custody_operation_scope": OPERATION_SCOPE,
        "upstream_receipt_operation_type": UPSTREAM_RECEIPT_OPERATION_TYPE, "upstream_receipt_operation_outcome_required": UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "upstream_receipt_status_required": UPSTREAM_RECEIPT_STATUS_REQUIRED,
        "upstream_audit_operation_type": UPSTREAM_AUDIT_OPERATION_TYPE, "upstream_audit_operation_outcome_required": UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "upstream_audit_result_required": UPSTREAM_AUDIT_RESULT_REQUIRED, "upstream_declaration_accepted_as_basis_required": UPSTREAM_DECLARATION_ACCEPTED_AS_BASIS_REQUIRED,
        "target_primary_material_filename": TARGET_PRIMARY_MATERIAL_FILENAME, "target_primary_material_version": TARGET_PRIMARY_MATERIAL_VERSION, "target_primary_material_date": TARGET_PRIMARY_MATERIAL_DATE, "target_primary_material_author": TARGET_PRIMARY_MATERIAL_AUTHOR, "target_primary_material_signature_role": TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE, "target_predecessor_material_filename": TARGET_PREDECESSOR_MATERIAL_FILENAME, "target_predecessor_material_role": TARGET_PREDECESSOR_MATERIAL_ROLE,
        "digest_algorithm": DIGEST_ALGORITHM_ALLOWED, "custody_posture_scope": CUSTODY_POSTURE_SCOPE, "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "operation_spec_reference": DEFAULT_OPERATION_SPEC_REFERENCE, **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "primary_material_path": None, "predecessor_material_path": None, "primary_material_custody_posture": "LOCAL_OPERATOR_HELD_SIGNED_SOURCE_ARTIFACT", "predecessor_material_custody_posture": "LOCAL_OPERATOR_HELD_PREDECESSOR_SOURCE_ARTIFACT",
        "declared_non_claims": _canonical_non_claims(), **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    aliases = {"target_spec_path": "operation_spec_reference", "operation_spec_path": "operation_spec_reference", "receipt_operation_terminal_summary_path": "receipt_operation_terminal_summary_reference", "audit_operation_terminal_summary_path": "audit_operation_terminal_summary_reference"}
    for alias, target in aliases.items():
        if alias in overrides and target not in overrides:
            overrides[target] = overrides[alias]
    request.update(overrides)
    return request


def resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min(declared_authored_scope_division_declaration_digest_custody_operation: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Resolve one explicit-file digest/custody result without discovery or copying."""

    if declared_authored_scope_division_declaration_digest_custody_operation is None:
        request = build_declared_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_request()
    elif not isinstance(declared_authored_scope_division_declaration_digest_custody_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request mapping", False, "mapping", type(declared_authored_scope_division_declaration_digest_custody_operation).__name__, "REQUEST_NOT_MAPPING")
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_authored_scope_division_declaration_digest_custody_operation))
    checks: list[dict[str, Any]] = []
    intent = request.get("intent")
    _add_check(checks, "intent supported", intent in SUPPORTED_INTENTS, SUPPORTED_INTENTS, intent, "UNSUPPORTED_INTENT")
    if intent == INTENT_BLOCK:
        return _blocked_result(request, checks, "EXPLICIT_BLOCK_REQUESTED", "explicit block intent requested")
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(request, checks, "UNSUPPORTED_INTENT", "intent is unsupported")
    _validate_exact_values(checks, request)
    _validate_reference(checks, request, "operation_spec_reference", "DIGEST_CUSTODY_OPERATION_SPEC_REFERENCE_MISSING")
    _validate_spec_and_upstream(checks, request)
    _validate_non_claims(checks, request)
    _validate_top_level_postures(checks, request)
    _validate_prohibited_requests(checks, request)
    material = _material_details(checks, request)
    _add_check(checks, "result-level required false non-claims canonical false", True, "canonical final false non-claims", "canonical false emitted by resolver")
    failed = _failed_codes(checks)
    if failed:
        return _blocked_result(request, checks, failed[0], f"blocked by failed check {failed[0]}")
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, {"primary_missing": True})
    if material.get("primary_missing"):
        return _build_result(request, OUTCOME_REQUIRES_MATERIAL, checks, material)
    if material.get("primary_digest") is None:
        return _blocked_result(request, checks, "MATERIAL_REFERENCE_INVALID", "primary material was not streamable")
    return _build_result(request, OUTCOME_RECORDED, checks, material)


def resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_from_path(declared_authored_scope_division_declaration_digest_custody_operation_path: Path | str) -> dict[str, Any]:
    """Read one explicit JSON request object and resolve it."""

    path = Path(declared_authored_scope_division_declaration_digest_custody_operation_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            request = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request path readable JSON", False, "readable JSON object", str(exc), "REQUEST_NOT_MAPPING")
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request path is unreadable or not JSON")
    return resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min(request)


def write_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_result(result: Mapping[str, Any], output_path: Path | str | None = None) -> Path:
    """Write deterministic sanitized JSON without silent overwrite or file copying."""

    if output_path is None:
        path = REPO_ROOT / OUTPUT_ROOT / DETERMINISTIC_FILENAME
    else:
        candidate = Path(output_path)
        base = candidate if candidate.is_absolute() else REPO_ROOT / candidate
        path = base if base.suffix else base / DETERMINISTIC_FILENAME
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        final_path = path
        suffix = 1
        while final_path.exists():
            final_path = path.with_name(f"{path.stem}_{suffix:03d}{path.suffix}")
            suffix += 1
        with final_path.open("w", encoding="utf-8") as handle:
            json.dump(_json_ready(_sanitize(result)), handle, ensure_ascii=True, indent=2, sort_keys=True)
            handle.write("\n")
        return final_path
    except OSError as exc:
        raise DescendantBodyCandidateAuthoredScopeDivisionDeclarationDigestCustodyOperationV0MinError(f"WRITE_REFUSED: {exc}") from exc
