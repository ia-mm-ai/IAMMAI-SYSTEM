"""Resolver for one authored scope-division declaration receipt boundary.

The external signed declaration remains outside the repository and is treated
only as proposed authored audit material. This resolver records a boundary
shape only: it performs no receipt, audit, PDF ingestion, custody, hashing,
transcription, scope declaration, standing, or downstream authorization.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateAuthoredScopeDivisionDeclarationReceiptBoundaryV0MinError(Exception):
    """Raised for bounded request-path and JSON handling errors."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min"
)

BOUNDARY_ID = "descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_001"
BOUNDARY_TYPE = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = "EXTERNAL_AUTHORED_DECLARATION_RECEIPT_FOR_AUDIT_ONLY"
FUTURE_RECEIPT_OPERATION_TYPE = (
    "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION"
)
FUTURE_AUDIT_OPERATION_TYPE = (
    "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION"
)
ADMISSIBLE_FUTURE_ROUTE = "RECEIPT_THEN_AUDIT_ONLY"

EXTERNAL_DECLARATION_STATUS = "EXISTS_OUTSIDE_REPO"
EXTERNAL_DECLARATION_ROLE = "PROPOSED_AUTHORED_AUDIT_MATERIAL"
EXTERNAL_DECLARATION_AUTHOR = "Marko Markota"
EXTERNAL_DECLARATION_SIGNATURE_ROLE = "AUTHORSHIP_ATTESTATION_ONLY"
EXTERNAL_DECLARATION_SCOPE_CLAIM_A = "Motion-side admissible variation"
EXTERNAL_DECLARATION_SCOPE_CLAIM_B = "Regulation-side admissibility bounds"
EXTERNAL_DECLARATION_COUPLING_CLAIM = "COUPLING_NOT_ASSIGNED_NOT_CREATED"
EXTERNAL_DECLARATION_LINEAGE_CLAIM = (
    "LINEAGE_REQUIRED_NO_ORPHANED_STATE_NO_SILENT_RESET_NO_OVERWRITE"
)

OUTCOME_RECORDED = (
    "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY_RECORDED"
)
OUTCOME_BLOCKED = (
    "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY_BLOCKED"
)
OUTCOME_NOT_RECORDED = (
    "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY_NOT_RECORDED"
)
OUTCOME_FAMILY = (OUTCOME_RECORDED, OUTCOME_BLOCKED, OUTCOME_NOT_RECORDED)

INTENT_RECORD = (
    "RECORD_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_"
    "division_declaration_receipt_boundary_v0_min"
)

DEFAULT_BOUNDARY_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_"
    "RECEIPT_BOUNDARY_V0_MIN_SPEC.md"
)
DEFAULT_COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_"
    "OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_"
    "TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_"
    "BOUNDARY_TERMINAL_SUMMARY_V0.md"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "receipt_performed",
    "audit_performed",
    "declaration_admitted_as_standing_basis",
    "external_declaration_hash_recorded",
    "external_declaration_custody_recorded",
    "signature_treated_as_scope_standing",
    "signature_treated_as_candidate_specific_basis_emission",
    "signature_treated_as_distinctness_support",
    "authored_scope_claim_accepted_as_standing",
    "motion_scope_accepted_as_standing",
    "regulation_scope_accepted_as_standing",
    "motion_regulation_division_audited",
    "motion_regulation_division_accepted",
    "coupling_assigned_to_candidate_a",
    "coupling_assigned_to_candidate_b",
    "coupling_created",
    "third_candidate_created",
    "third_model_admitted",
    "candidate_a_scope_declared",
    "candidate_b_scope_declared",
    "basis_bearing_scope_division_declared",
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
    "existence_claim_evidence_check_overridden",
    "existence_claim_evidence_check_bypassed",
    "differentiation_operation_overridden",
    "differentiation_operation_bypassed",
    "distinctness_operation_boundary_overridden",
    "distinctness_operation_boundary_bypassed",
    "distinctness_operation_overridden",
    "distinctness_operation_bypassed",
    "candidate_specific_distinctness_basis_emission_boundary_overridden",
    "candidate_specific_distinctness_basis_emission_boundary_bypassed",
    "candidate_specific_distinctness_basis_emission_operation_overridden",
    "candidate_specific_distinctness_basis_emission_operation_bypassed",
    "candidate_non_cosmetic_scope_division_declaration_boundary_overridden",
    "candidate_non_cosmetic_scope_division_declaration_boundary_bypassed",
    "candidate_non_cosmetic_scope_division_declaration_operation_overridden",
    "candidate_non_cosmetic_scope_division_declaration_operation_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_pdf_ingestion_as_standing_basis",
    "direct_signature_to_standing_conversion",
    "direct_signature_to_distinctness_support_conversion",
    "direct_signature_to_candidate_specific_basis_emission_conversion",
    "direct_declaration_to_scope_standing_conversion",
    "direct_declaration_to_candidate_records_distinct_conversion",
    "direct_declaration_to_descendant_body_creation",
    "direct_declaration_to_relation_creation",
    "direct_declaration_to_runtime_creation",
    "direct_declaration_to_authority_currentness_creation",
    "direct_declaration_to_follow_on_work",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "authored_scope_division_declaration_receipt_boundary_recorded",
    "external_declaration_signed",
    "external_declaration_exists_outside_repo",
    "external_declaration_proposed_audit_material_only",
    "signature_authorship_attestation_only",
    "receipt_then_audit_route_only",
    "coupling_unassigned_and_uncreated",
    "upstream_completed_operation_requires_additional_basis",
    "target_boundary_spec_markers_present",
    "completed_operation_terminal_summary_markers_present",
    "existence_claim_evidence_check_terminal_summary_markers_present",
    "differentiation_operation_terminal_summary_markers_present",
    "distinctness_operation_terminal_summary_markers_present",
    "basis_emission_operation_terminal_summary_markers_present",
    "scope_division_declaration_boundary_terminal_summary_markers_present",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "BOUNDARY_SPEC_REFERENCE_MISSING",
    "BOUNDARY_SPEC_MARKER_MISSING",
    "COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "COMPLETED_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "BOUNDARY_ID_NOT_EXPECTED",
    "BOUNDARY_TYPE_NOT_EXPECTED",
    "BOUNDARY_VERSION_NOT_EXPECTED",
    "BOUNDARY_SCOPE_NOT_EXPECTED",
    "FUTURE_RECEIPT_OPERATION_TYPE_NOT_EXPECTED",
    "FUTURE_AUDIT_OPERATION_TYPE_NOT_EXPECTED",
    "ADMISSIBLE_FUTURE_ROUTE_NOT_EXPECTED",
    "EXTERNAL_DECLARATION_POSTURE_NOT_EXPECTED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PROHIBITED_RECEIPT_OR_AUDIT_REQUESTED",
    "PROHIBITED_DECLARATION_CONVERSION_REQUESTED",
    "PROHIBITED_SIGNATURE_CONVERSION_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

SENSITIVE_BODY_KEYS = {
    "raw_body",
    "full_body",
    "markdown_body",
    "raw_markdown_body",
    "external_pdf_body",
    "hidden_repo_state",
    "current_working_tree",
}

BOUNDARY_SPEC_MARKER_CLASSES = (
    (
        "boundary_identity",
        (
            "Descendant Body Candidate Authored Scope Division Declaration Receipt Boundary V0 Minimum Specification",
            BOUNDARY_TYPE,
            BOUNDARY_ID,
            BOUNDARY_SCOPE,
        ),
    ),
    (
        "future_route",
        (FUTURE_RECEIPT_OPERATION_TYPE, FUTURE_AUDIT_OPERATION_TYPE, ADMISSIBLE_FUTURE_ROUTE),
    ),
    (
        "external_proposed_audit_material",
        (
            EXTERNAL_DECLARATION_STATUS,
            EXTERNAL_DECLARATION_ROLE,
            EXTERNAL_DECLARATION_SIGNATURE_ROLE,
            EXTERNAL_DECLARATION_SCOPE_CLAIM_A,
            EXTERNAL_DECLARATION_SCOPE_CLAIM_B,
            EXTERNAL_DECLARATION_COUPLING_CLAIM,
        ),
    ),
    (
        "non_receipt_non_audit",
        (
            "receipt_performed = false",
            "audit_performed = false",
            "declaration_admitted_as_standing_basis = false",
            "external_declaration_hash_recorded = false",
            "external_declaration_custody_recorded = false",
        ),
    ),
    (
        "signature_non_conversion",
        (
            "signature_treated_as_scope_standing = false",
            "signature_treated_as_candidate_specific_basis_emission = false",
            "signature_treated_as_distinctness_support = false",
        ),
    ),
    (
        "scope_audit_non_standing",
        (
            "authored_scope_claim_accepted_as_standing = false",
            "motion_scope_accepted_as_standing = false",
            "regulation_scope_accepted_as_standing = false",
            "motion_regulation_division_audited = false",
            "motion_regulation_division_accepted = false",
            "candidate_a_scope_declared = false",
            "candidate_b_scope_declared = false",
            "basis_bearing_scope_division_declared = false",
        ),
    ),
    (
        "coupling_and_third_model_blocked",
        (
            "coupling_assigned_to_candidate_a = false",
            "coupling_assigned_to_candidate_b = false",
            "coupling_created = false",
            "third_candidate_created = false",
            "third_model_admitted = false",
            "Coupling is assigned to neither candidate",
            "No third model, third candidate, or standing body is admitted",
        ),
    ),
    (
        "downstream_non_authorization",
        (
            "candidate_specific_content_emitted = false",
            "separate_seal_material_emitted = false",
            "separate_lineage_receipt_material_emitted = false",
            "separate_digest_material_emitted = false",
            "distinctness_supported_recorded = false",
            "candidate_records_marked_distinct = false",
            "candidate_standing_authorized = false",
            "descendant_body_created = false",
            "crossing_authorized = false",
            "relation_created = false",
            "runtime_created = false",
            "currentness_created = false",
            "authority_created = false",
            "follow_on_authorized = false",
        ),
    ),
    (
        "completed_operation_relation",
        (
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
            "failed_check_count = 0",
            "passed_check_count = 96",
            "missing non-cosmetic candidate A scope declaration",
            "missing non-cosmetic candidate B scope declaration",
            "missing basis-bearing scope division declaration",
            "does not close the prior additional-basis gap",
        ),
    ),
    (
        "contaminated_lineage_preservation",
        (
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        ),
    ),
    (
        "blocked_routes",
        (
            "direct PDF ingestion as standing basis",
            "direct signature-to-standing",
            "direct declaration-to-scope-standing",
            "direct coupling instantiation",
            "third-candidate",
            "third-model",
            "repository scan",
            "affected-file repair",
            "prior unsupported-claim validation",
        ),
    ),
    (
        "closing_lock",
        (
            "The prior operation line remains at REQUIRES_ADDITIONAL_BASIS until receipt, audit, and any successor closure are separately bounded and passed.",
        ),
    ),
)

UPSTREAM_REQUIREMENTS = (
    (
        "completed_operation_terminal_summary_reference",
        DEFAULT_COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "COMPLETED_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
            "failed_check_count = 0",
            "passed_check_count = 96",
            "missing non-cosmetic candidate A scope declaration",
            "missing non-cosmetic candidate B scope declaration",
            "missing basis-bearing scope division declaration",
        ),
        "completed_operation_terminal_summary_markers_present",
    ),
    (
        "existence_claim_evidence_check_terminal_summary_reference",
        DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE,
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
        ("UNSUPPORTED",),
        "existence_claim_evidence_check_terminal_summary_markers_present",
    ),
    (
        "differentiation_operation_terminal_summary_reference",
        DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ("DESCENDANT_BODY_DIFFERENTIATION_OPERATION", "non-standing candidate records"),
        "differentiation_operation_terminal_summary_markers_present",
    ),
    (
        "distinctness_operation_terminal_summary_reference",
        DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ("NOT_DISTINCT",),
        "distinctness_operation_terminal_summary_markers_present",
    ),
    (
        "basis_emission_operation_terminal_summary_reference",
        DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ("REQUIRES_ADDITIONAL_BASIS",),
        "basis_emission_operation_terminal_summary_markers_present",
    ),
    (
        "scope_division_declaration_boundary_terminal_summary_reference",
        DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        ("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",),
        "scope_division_declaration_boundary_terminal_summary_markers_present",
    ),
)

PROHIBITED_REQUEST_FLAGS = {
    "request_receipt_performance": "PROHIBITED_RECEIPT_OR_AUDIT_REQUESTED",
    "request_audit_performance": "PROHIBITED_RECEIPT_OR_AUDIT_REQUESTED",
    "request_pdf_ingestion": "PROHIBITED_RECEIPT_OR_AUDIT_REQUESTED",
    "request_pdf_hash_recording": "PROHIBITED_RECEIPT_OR_AUDIT_REQUESTED",
    "request_pdf_custody_recording": "PROHIBITED_RECEIPT_OR_AUDIT_REQUESTED",
    "request_pdf_transcription": "PROHIBITED_RECEIPT_OR_AUDIT_REQUESTED",
    "request_declaration_standing_basis_admission": "PROHIBITED_DECLARATION_CONVERSION_REQUESTED",
    "request_authored_scope_claim_standing_acceptance": "PROHIBITED_DECLARATION_CONVERSION_REQUESTED",
    "request_motion_scope_standing_acceptance": "PROHIBITED_DECLARATION_CONVERSION_REQUESTED",
    "request_regulation_scope_standing_acceptance": "PROHIBITED_DECLARATION_CONVERSION_REQUESTED",
    "request_motion_regulation_division_audit": "PROHIBITED_DECLARATION_CONVERSION_REQUESTED",
    "request_motion_regulation_division_acceptance": "PROHIBITED_DECLARATION_CONVERSION_REQUESTED",
    "request_candidate_a_scope_declaration": "PROHIBITED_DECLARATION_CONVERSION_REQUESTED",
    "request_candidate_b_scope_declaration": "PROHIBITED_DECLARATION_CONVERSION_REQUESTED",
    "request_basis_bearing_scope_division_declaration": "PROHIBITED_DECLARATION_CONVERSION_REQUESTED",
    "request_signature_scope_standing_conversion": "PROHIBITED_SIGNATURE_CONVERSION_REQUESTED",
    "request_signature_candidate_specific_basis_emission_conversion": "PROHIBITED_SIGNATURE_CONVERSION_REQUESTED",
    "request_signature_distinctness_support_conversion": "PROHIBITED_SIGNATURE_CONVERSION_REQUESTED",
    "request_coupling_assignment_to_candidate_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_candidate_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_model_admission": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_candidate_specific_content_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_separate_seal_material_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_separate_lineage_receipt_material_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_separate_digest_material_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_basis_emission_operation_rerun": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_distinctness_operation_rerun": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_distinctness_supported_recording": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_candidate_records_marked_distinct": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_candidate_standing_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_descendant_body_creation": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
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
    "request_follow_on_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "return_raw_markdown_body": "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
}

WHAT_REMAINS_OPEN = [
    "future authored declaration receipt operation",
    "future authored declaration audit operation",
    "external declaration metadata receipt",
    "external declaration custody decision, if separately bounded",
    "external declaration hash decision, if separately bounded",
    "external declaration text extraction or transcription decision, if separately bounded",
    "audit of Candidate A Motion-side scope",
    "audit of Candidate B Regulation-side scope",
    "audit of Motion/Regulation non-cosmetic difference",
    "audit of basis-bearing scope division",
    "audit of coupling-not-assigned condition",
    "audit of no-third-model condition",
    "audit of lineage constraints",
    "candidate-specific distinctness basis emission operation successor",
    "actual candidate-specific content emission",
    "actual separate seal material emission",
    "actual separate lineage receipt material emission",
    "actual separate digest material emission",
    "future distinctness-supported operation result",
    "divergent receipt-history route, if separately bounded",
    "carrier separation route, if separately bounded",
    "candidate standing checks",
    "first crossing",
    "relation",
    "FIELD machinery",
    "runtime",
    "API",
    "currentness",
    "authority",
    "standing",
    "output authorization",
    "action authorization",
    "derivative reception",
    "synchronization",
    "externalization boundary",
    "follow-on work",
]


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _resolve_declared_path(value: Any) -> Path | None:
    if not _is_non_empty_string(value):
        return None
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_declared_text(value: Any) -> str | None:
    path = _resolve_declared_path(value)
    if path is None:
        return None
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def _is_sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return lowered in SENSITIVE_BODY_KEYS or lowered.endswith("_body")


def _sanitize(value: Any, key: str = "") -> Any:
    if _is_sensitive_key(key):
        return "[REDACTED_SENSITIVE_BODY]"
    if isinstance(value, Mapping):
        return {str(item_key): _sanitize(item_value, str(item_key)) for item_key, item_value in value.items()}
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


def _add_check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str | None = None,
) -> None:
    record: dict[str, Any] = {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected),
        "actual_posture": _sanitize(actual),
    }
    if not passed and code:
        record["block_code"] = code
        record["failure_code"] = code
    checks.append(record)


def _failed_codes(checks: list[dict[str, Any]]) -> list[str]:
    return [
        str(check.get("block_code") or check.get("failure_code"))
        for check in checks
        if check.get("passed") is False
        and isinstance(check.get("block_code") or check.get("failure_code"), str)
        and (check.get("block_code") or check.get("failure_code")) in BLOCK_CODES
    ]


def _marker_classes_present(
    text: str | None, classes: tuple[tuple[str, tuple[str, ...]], ...]
) -> tuple[bool, list[str]]:
    if text is None:
        return False, [name for name, _ in classes]
    missing = [name for name, markers in classes if not all(marker in text for marker in markers)]
    return not missing, missing


def _validate_reference(
    checks: list[dict[str, Any],
    ],
    request: Mapping[str, Any],
    field: str,
    missing_code: str,
) -> None:
    _add_check(
        checks,
        f"{field} declared",
        _is_non_empty_string(request.get(field)),
        "non-empty declared path reference",
        request.get(field),
        missing_code,
    )


def _validate_exact(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    field: str,
    expected: Any,
    code: str,
) -> None:
    actual = request.get(field)
    _add_check(checks, f"{field} exact", actual == expected, expected, actual, code)


def _validate_non_claims(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        _add_check(
            checks,
            "required non-claims false",
            False,
            "mapping with every required key set to false",
            declared,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return
    malformed = [key for key in REQUIRED_FALSE_NON_CLAIMS if declared.get(key) is not False]
    _add_check(
        checks,
        "required non-claims false",
        not malformed,
        "every required false non-claim present and exactly false",
        {"malformed_keys": malformed},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _validate_spec_markers(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> bool:
    text = _read_declared_text(request.get("boundary_spec_reference"))
    passed, missing = _marker_classes_present(text, BOUNDARY_SPEC_MARKER_CLASSES)
    _add_check(
        checks,
        "target receipt-boundary spec posture classes present",
        passed,
        "all required target boundary posture classes",
        {"missing_posture_classes": missing},
        "BOUNDARY_SPEC_MARKER_MISSING",
    )
    return passed


def _validate_upstream_markers(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> dict[str, bool]:
    flags: dict[str, bool] = {}
    for field, _, missing_code, marker_code, markers, flag in UPSTREAM_REQUIREMENTS:
        text = _read_declared_text(request.get(field))
        passed = text is not None and all(marker in text for marker in markers)
        _add_check(
            checks,
            f"{field} expected markers present",
            passed,
            markers,
            {"reference_readable": text is not None, "missing_markers": [] if passed else list(markers)},
            missing_code if text is None else marker_code,
        )
        flags[flag] = passed
    return flags


def _validate_prohibited_requests(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        actual = request.get(field)
        _add_check(checks, f"{field} not requested", actual is not True, False, actual, code)


def _marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    names = {
        "target_boundary_spec_markers_present": "target receipt-boundary spec posture classes present",
        "completed_operation_terminal_summary_markers_present": (
            "completed_operation_terminal_summary_reference expected markers present"
        ),
        "existence_claim_evidence_check_terminal_summary_markers_present": (
            "existence_claim_evidence_check_terminal_summary_reference expected markers present"
        ),
        "differentiation_operation_terminal_summary_markers_present": (
            "differentiation_operation_terminal_summary_reference expected markers present"
        ),
        "distinctness_operation_terminal_summary_markers_present": (
            "distinctness_operation_terminal_summary_reference expected markers present"
        ),
        "basis_emission_operation_terminal_summary_markers_present": (
            "basis_emission_operation_terminal_summary_reference expected markers present"
        ),
        "scope_division_declaration_boundary_terminal_summary_markers_present": (
            "scope_division_declaration_boundary_terminal_summary_reference expected markers present"
        ),
    }
    return {
        field: any(check.get("check_name") == name and check.get("passed") is True for check in checks)
        for field, name in names.items()
    }


def _boundary_object(request: Mapping[str, Any], recorded: bool, flags: Mapping[str, bool]) -> dict[str, Any]:
    object_data: dict[str, Any] = {
        "authored_scope_division_declaration_receipt_boundary_id": request.get(
            "authored_scope_division_declaration_receipt_boundary_id", BOUNDARY_ID
        ),
        "authored_scope_division_declaration_receipt_boundary_type": request.get(
            "authored_scope_division_declaration_receipt_boundary_type", BOUNDARY_TYPE
        ),
        "authored_scope_division_declaration_receipt_boundary_version": request.get(
            "authored_scope_division_declaration_receipt_boundary_version", BOUNDARY_VERSION
        ),
        "authored_scope_division_declaration_receipt_boundary_scope": request.get(
            "authored_scope_division_declaration_receipt_boundary_scope", BOUNDARY_SCOPE
        ),
        "future_receipt_operation_type": request.get(
            "future_receipt_operation_type", FUTURE_RECEIPT_OPERATION_TYPE
        ),
        "future_audit_operation_type": request.get(
            "future_audit_operation_type", FUTURE_AUDIT_OPERATION_TYPE
        ),
        "admissible_future_route": request.get("admissible_future_route", ADMISSIBLE_FUTURE_ROUTE),
        "external_declaration_status": request.get(
            "external_declaration_status", EXTERNAL_DECLARATION_STATUS
        ),
        "external_declaration_role": request.get("external_declaration_role", EXTERNAL_DECLARATION_ROLE),
        "external_declaration_author": request.get(
            "external_declaration_author", EXTERNAL_DECLARATION_AUTHOR
        ),
        "external_declaration_signed": request.get("external_declaration_signed") is True,
        "external_declaration_signature_role": request.get(
            "external_declaration_signature_role", EXTERNAL_DECLARATION_SIGNATURE_ROLE
        ),
        "external_declaration_scope_claim_candidate_a": request.get(
            "external_declaration_scope_claim_candidate_a", EXTERNAL_DECLARATION_SCOPE_CLAIM_A
        ),
        "external_declaration_scope_claim_candidate_b": request.get(
            "external_declaration_scope_claim_candidate_b", EXTERNAL_DECLARATION_SCOPE_CLAIM_B
        ),
        "external_declaration_coupling_claim": request.get(
            "external_declaration_coupling_claim", EXTERNAL_DECLARATION_COUPLING_CLAIM
        ),
        "external_declaration_lineage_claim": request.get(
            "external_declaration_lineage_claim", EXTERNAL_DECLARATION_LINEAGE_CLAIM
        ),
        "authored_scope_division_declaration_receipt_boundary_recorded": recorded,
        "external_declaration_exists_outside_repo": recorded,
        "external_declaration_proposed_audit_material_only": recorded,
        "signature_authorship_attestation_only": recorded,
        "receipt_then_audit_route_only": recorded,
        "coupling_unassigned_and_uncreated": recorded,
        "upstream_completed_operation_requires_additional_basis": recorded,
        **_canonical_non_claims(),
        **flags,
    }
    return object_data


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get("descendant_body_candidate_authored_scope_division_declaration_receipt_boundary")
    if not isinstance(boundary, Mapping):
        boundary = {}
    checks = result.get("authored_scope_division_declaration_receipt_boundary_checks")
    check_records = checks if isinstance(checks, list) else []
    summary = {
        "outcome": result.get("outcome"),
        "failed_check_count": sum(
            1 for check in check_records if isinstance(check, Mapping) and check.get("passed") is False
        ),
        "passed_check_count": sum(
            1 for check in check_records if isinstance(check, Mapping) and check.get("passed") is True
        ),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "boundary_id": boundary.get("authored_scope_division_declaration_receipt_boundary_id"),
        "boundary_type": boundary.get("authored_scope_division_declaration_receipt_boundary_type"),
        "boundary_version": boundary.get("authored_scope_division_declaration_receipt_boundary_version"),
        "boundary_scope": boundary.get("authored_scope_division_declaration_receipt_boundary_scope"),
        "future_receipt_operation_type": boundary.get("future_receipt_operation_type"),
        "future_audit_operation_type": boundary.get("future_audit_operation_type"),
        "admissible_future_route": boundary.get("admissible_future_route"),
        "external_declaration_status": boundary.get("external_declaration_status"),
        "external_declaration_role": boundary.get("external_declaration_role"),
        "external_declaration_author": boundary.get("external_declaration_author"),
        "external_declaration_signed": boundary.get("external_declaration_signed"),
        "external_declaration_signature_role": boundary.get("external_declaration_signature_role"),
        "candidate_a_proposed_scope_claim": boundary.get("external_declaration_scope_claim_candidate_a"),
        "candidate_b_proposed_scope_claim": boundary.get("external_declaration_scope_claim_candidate_b"),
        "coupling_claim": boundary.get("external_declaration_coupling_claim"),
        "lineage_claim": boundary.get("external_declaration_lineage_claim"),
        "selected_target_spec_path": result.get("upstream_basis", {}).get("boundary_spec_reference")
        if isinstance(result.get("upstream_basis"), Mapping)
        else None,
        "completed_operation_terminal_summary_path": result.get("upstream_basis", {}).get(
            "completed_operation_terminal_summary_reference"
        )
        if isinstance(result.get("upstream_basis"), Mapping)
        else None,
        "result_level_non_claims_canonical_false": all(
            isinstance(result.get("non_claims"), Mapping)
            and result["non_claims"].get(key) is False
            for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }
    for key in (
        "authored_scope_division_declaration_receipt_boundary_recorded",
        "receipt_performed",
        "audit_performed",
        "declaration_admitted_as_standing_basis",
        "external_declaration_hash_recorded",
        "external_declaration_custody_recorded",
        "signature_treated_as_scope_standing",
        "signature_treated_as_candidate_specific_basis_emission",
        "signature_treated_as_distinctness_support",
        "motion_regulation_division_audited",
        "motion_regulation_division_accepted",
        "candidate_a_scope_declared",
        "candidate_b_scope_declared",
        "basis_bearing_scope_division_declared",
        "coupling_assigned_to_candidate_a",
        "coupling_assigned_to_candidate_b",
        "coupling_created",
        "third_candidate_created",
        "third_model_admitted",
        "candidate_standing_authorized",
        "descendant_body_created",
        "crossing_authorized",
        "relation_created",
        "runtime_created",
        "currentness_created",
        "authority_created",
        "follow_on_authorized",
        "repair_performed",
        "repository_scan_performed",
        "validation_enforced",
        *ALLOWED_TRUE_RECORDED_FIELDS[-7:],
    ):
        summary[key] = boundary.get(key)
    return _sanitize(summary)


def build_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact boundary summary without raw declaration bodies."""

    return _build_summary(result)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    recorded: bool,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    flags = _marker_flags(checks)
    boundary = _boundary_object(request, recorded, flags)
    result: dict[str, Any] = {
        "authored_scope_division_declaration_receipt_boundary_metadata": {
            "authored_scope_division_declaration_receipt_boundary_id": boundary[
                "authored_scope_division_declaration_receipt_boundary_id"
            ],
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_authored_scope_division_declaration_receipt_boundary_basis": _sanitize(request),
        "upstream_basis": {
            "boundary_spec_reference": request.get("boundary_spec_reference"),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **flags,
        },
        "descendant_body_candidate_authored_scope_division_declaration_receipt_boundary": boundary,
        "authored_scope_division_declaration_receipt_boundary_checks": checks,
        "authored_scope_division_declaration_receipt_boundary_statement": {
            "outcome": outcome,
            "authored_scope_division_declaration_receipt_boundary_recorded": recorded,
            "receipt_performed": False,
            "audit_performed": False,
            "declaration_admitted_as_standing_basis": False,
            "result_level_non_claims_canonical_false": True,
        },
        "authored_scope_division_declaration_receipt_boundary_non_meaning": {
            "not_receipt": True,
            "not_audit": True,
            "not_pdf_ingestion": True,
            "not_scope_standing": True,
            "not_candidate_specific_basis_emission": True,
            "not_distinctness_support": True,
            "not_candidate_standing": True,
            "not_descendant_body_creation": True,
            "not_relation": True,
            "not_runtime": True,
            "not_authority": True,
            "not_follow_on": True,
        },
        "permitted_future_route": [
            "future receipt operation may record existence and minimal metadata as proposed audit material",
            "future audit operation may evaluate declared scope-division posture",
            "only separately bounded receipt and audit may precede any later closure consideration",
        ],
        "blocked_routes": [
            "direct PDF, signature, or declaration conversion into standing, emission, distinctness, or downstream authority",
            "direct coupling instantiation, third-candidate, or third-model route",
            "repository scan, affected-file repair, or prior unsupported-claim validation",
        ],
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
            "reason": block_reason if outcome == OUTCOME_BLOCKED else None,
        },
    }
    result["authored_scope_division_declaration_receipt_boundary_summary"] = _build_summary(result)
    return result


def _blocked_result(
    request: Mapping[str, Any], checks: list[dict[str, Any]], code: str, reason: str
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(request, OUTCOME_BLOCKED, checks, False, code, reason)


def build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one declared boundary request using current explicit repo references."""

    request: dict[str, Any] = {
        "authored_scope_division_declaration_receipt_boundary_id": BOUNDARY_ID,
        "authored_scope_division_declaration_receipt_boundary_type": BOUNDARY_TYPE,
        "authored_scope_division_declaration_receipt_boundary_version": BOUNDARY_VERSION,
        "authored_scope_division_declaration_receipt_boundary_scope": BOUNDARY_SCOPE,
        "intent": INTENT_RECORD,
        "future_receipt_operation_type": FUTURE_RECEIPT_OPERATION_TYPE,
        "future_audit_operation_type": FUTURE_AUDIT_OPERATION_TYPE,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "external_declaration_status": EXTERNAL_DECLARATION_STATUS,
        "external_declaration_role": EXTERNAL_DECLARATION_ROLE,
        "external_declaration_author": EXTERNAL_DECLARATION_AUTHOR,
        "external_declaration_signed": True,
        "external_declaration_signature_role": EXTERNAL_DECLARATION_SIGNATURE_ROLE,
        "external_declaration_scope_claim_candidate_a": EXTERNAL_DECLARATION_SCOPE_CLAIM_A,
        "external_declaration_scope_claim_candidate_b": EXTERNAL_DECLARATION_SCOPE_CLAIM_B,
        "external_declaration_coupling_claim": EXTERNAL_DECLARATION_COUPLING_CLAIM,
        "external_declaration_lineage_claim": EXTERNAL_DECLARATION_LINEAGE_CLAIM,
        "boundary_spec_reference": DEFAULT_BOUNDARY_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


def resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(
    declared_authored_scope_division_declaration_receipt_boundary: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one receipt-boundary result without receiving or auditing material."""

    if declared_authored_scope_division_declaration_receipt_boundary is None:
        request = build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_request()
    elif not isinstance(declared_authored_scope_division_declaration_receipt_boundary, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request mapping", False, "mapping", type(declared_authored_scope_division_declaration_receipt_boundary).__name__, "REQUEST_NOT_MAPPING")
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_authored_scope_division_declaration_receipt_boundary))

    checks: list[dict[str, Any]] = []
    intent = request.get("intent")
    _add_check(checks, "intent supported", intent in SUPPORTED_INTENTS, SUPPORTED_INTENTS, intent, "UNSUPPORTED_INTENT")
    if intent == INTENT_BLOCK:
        return _blocked_result(request, checks, "EXPLICIT_BLOCK_REQUESTED", "explicit block intent requested")
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(request, checks, "UNSUPPORTED_INTENT", "intent is unsupported")

    exact_fields = (
        ("authored_scope_division_declaration_receipt_boundary_id", BOUNDARY_ID, "BOUNDARY_ID_NOT_EXPECTED"),
        ("authored_scope_division_declaration_receipt_boundary_type", BOUNDARY_TYPE, "BOUNDARY_TYPE_NOT_EXPECTED"),
        ("authored_scope_division_declaration_receipt_boundary_version", BOUNDARY_VERSION, "BOUNDARY_VERSION_NOT_EXPECTED"),
        ("authored_scope_division_declaration_receipt_boundary_scope", BOUNDARY_SCOPE, "BOUNDARY_SCOPE_NOT_EXPECTED"),
        ("future_receipt_operation_type", FUTURE_RECEIPT_OPERATION_TYPE, "FUTURE_RECEIPT_OPERATION_TYPE_NOT_EXPECTED"),
        ("future_audit_operation_type", FUTURE_AUDIT_OPERATION_TYPE, "FUTURE_AUDIT_OPERATION_TYPE_NOT_EXPECTED"),
        ("admissible_future_route", ADMISSIBLE_FUTURE_ROUTE, "ADMISSIBLE_FUTURE_ROUTE_NOT_EXPECTED"),
        ("external_declaration_status", EXTERNAL_DECLARATION_STATUS, "EXTERNAL_DECLARATION_POSTURE_NOT_EXPECTED"),
        ("external_declaration_role", EXTERNAL_DECLARATION_ROLE, "EXTERNAL_DECLARATION_POSTURE_NOT_EXPECTED"),
        ("external_declaration_author", EXTERNAL_DECLARATION_AUTHOR, "EXTERNAL_DECLARATION_POSTURE_NOT_EXPECTED"),
        ("external_declaration_signed", True, "EXTERNAL_DECLARATION_POSTURE_NOT_EXPECTED"),
        ("external_declaration_signature_role", EXTERNAL_DECLARATION_SIGNATURE_ROLE, "EXTERNAL_DECLARATION_POSTURE_NOT_EXPECTED"),
        ("external_declaration_scope_claim_candidate_a", EXTERNAL_DECLARATION_SCOPE_CLAIM_A, "EXTERNAL_DECLARATION_POSTURE_NOT_EXPECTED"),
        ("external_declaration_scope_claim_candidate_b", EXTERNAL_DECLARATION_SCOPE_CLAIM_B, "EXTERNAL_DECLARATION_POSTURE_NOT_EXPECTED"),
        ("external_declaration_coupling_claim", EXTERNAL_DECLARATION_COUPLING_CLAIM, "EXTERNAL_DECLARATION_POSTURE_NOT_EXPECTED"),
        ("external_declaration_lineage_claim", EXTERNAL_DECLARATION_LINEAGE_CLAIM, "EXTERNAL_DECLARATION_POSTURE_NOT_EXPECTED"),
    )
    for field, expected, code in exact_fields:
        _validate_exact(checks, request, field, expected, code)

    _validate_reference(checks, request, "boundary_spec_reference", "BOUNDARY_SPEC_REFERENCE_MISSING")
    _validate_spec_markers(checks, request)
    for field, _, missing_code, _, _, _ in UPSTREAM_REQUIREMENTS:
        _validate_reference(checks, request, field, missing_code)
    _validate_upstream_markers(checks, request)
    _validate_non_claims(checks, request)
    _validate_prohibited_requests(checks, request)
    _add_check(
        checks,
        "result-level required false non-claims canonical false",
        True,
        "canonical final false non-claims",
        "canonical false emitted by resolver",
    )

    failed_codes = _failed_codes(checks)
    if failed_codes:
        code = failed_codes[0]
        return _blocked_result(request, checks, code, f"blocked by failed check {code}")
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, False)
    return _build_result(request, OUTCOME_RECORDED, checks, True)


def resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_from_path(
    declared_authored_scope_division_declaration_receipt_boundary_path: Path | str,
) -> dict[str, Any]:
    """Read one declared JSON request object and resolve it."""

    path = Path(declared_authored_scope_division_declaration_receipt_boundary_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request path readable JSON", False, "readable JSON object", str(exc), "REQUEST_NOT_MAPPING")
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request path is unreadable or not JSON")
    return resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(data)


def _safe_filename_part(value: Any) -> str:
    text = str(value or BOUNDARY_ID)
    safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in text)
    return safe.strip("._-") or BOUNDARY_ID


def write_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write stable JSON without overwrite; this helper never writes source material."""

    boundary = result.get("descendant_body_candidate_authored_scope_division_declaration_receipt_boundary")
    boundary_id = BOUNDARY_ID
    if isinstance(boundary, Mapping):
        boundary_id = str(boundary.get("authored_scope_division_declaration_receipt_boundary_id") or BOUNDARY_ID)
    filename = f"{_safe_filename_part(boundary_id)}__authored_scope_division_declaration_receipt_boundary_v0_min_result.json"
    if output_path is None:
        path = REPO_ROOT / OUTPUT_ROOT / filename
    else:
        candidate = Path(output_path)
        base = candidate if candidate.is_absolute() else REPO_ROOT / candidate
        path = base if base.suffix else base / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = path
    suffix = 1
    while final_path.exists():
        final_path = path.with_name(f"{path.stem}_{suffix:03d}{path.suffix}")
        suffix += 1
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_json_ready(result), handle, ensure_ascii=True, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path
