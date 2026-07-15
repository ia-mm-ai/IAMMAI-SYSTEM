"""Resolve one bounded authored scope-division declaration receipt operation.

The resolver records metadata for one declared external material as proposed
authored audit material only. It never audits the material, treats receipt as
standing, exposes raw material bodies, or authorizes downstream work.
"""

from __future__ import annotations

import copy
import hashlib
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateAuthoredScopeDivisionDeclarationReceiptOperationV0MinError(Exception):
    """Raised for bounded receipt-operation path and JSON failures."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min"

OPERATION_ID = "descendant_body_candidate_authored_scope_division_declaration_receipt_operation_001"
OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EXTERNAL_AUTHORED_DECLARATION_METADATA_RECEIPT_FOR_AUDIT_ONLY"
UPSTREAM_BOUNDARY_TYPE = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY"
UPSTREAM_BOUNDARY_OUTCOME_REQUIRED = (
    "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY_RECORDED"
)
ADMISSIBLE_FUTURE_ROUTE = "RECEIPT_THEN_AUDIT_ONLY"
RECEIVED_MATERIAL_TYPE = "EXTERNAL_AUTHORED_SIGNED_DECLARATION"
RECEIVED_MATERIAL_EXPECTED_FILENAME = "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION V.2.pdf"
RECEIVED_MATERIAL_EXPECTED_TITLE = "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION"
RECEIVED_MATERIAL_EXPECTED_VERSION = "v2"
RECEIVED_MATERIAL_EXPECTED_DATE = "10 July 2026"
RECEIVED_MATERIAL_EXPECTED_AUTHOR = "Marko Markota"
RECEIVED_MATERIAL_EXPECTED_SIGNATURE_PRESENT = True
RECEIVED_MATERIAL_EXPECTED_SIGNATURE_ROLE = "AUTHORSHIP_ATTESTATION_ONLY"
RECEIVED_MATERIAL_EXPECTED_PREDECESSOR = "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION v1"
RECEIVED_MATERIAL_PREDECESSOR_ROLE = "REFERENCED_PREDECESSOR_ONLY"

OUTCOME_RECORDED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_RECORDED"
OUTCOME_BLOCKED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (OUTCOME_RECORDED, OUTCOME_BLOCKED, OUTCOME_NOT_RECORDED)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_"
    "division_declaration_receipt_operation_v0_min"
)
DETERMINISTIC_FILENAME = (
    "descendant_body_candidate_authored_scope_division_declaration_receipt_operation_001"
    "__authored_scope_division_declaration_receipt_operation_v0_min_result.json"
)

DEFAULT_OPERATION_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_"
    "RECEIPT_OPERATION_V0_MIN_SPEC.md"
)
DEFAULT_RECEIPT_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_"
    "RECEIPT_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
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
    "receipt_operation_recorded",
    "receipt_performed",
    "audit_performed",
    "declaration_admitted_as_standing_basis",
    "digest_treated_as_standing",
    "hash_treated_as_standing",
    "custody_treated_as_standing",
    "transcription_treated_as_standing",
    "signature_treated_as_scope_standing",
    "signature_treated_as_candidate_specific_basis_emission",
    "signature_treated_as_distinctness_support",
    "authored_scope_claim_accepted_as_standing",
    "motion_scope_accepted_as_standing",
    "regulation_scope_accepted_as_standing",
    "motion_regulation_division_audited",
    "motion_regulation_division_accepted",
    "sibling_non_monarchy_audited",
    "sibling_non_monarchy_accepted",
    "coupling_not_assigned_audited",
    "coupling_not_assigned_accepted",
    "no_third_model_audited",
    "no_third_model_accepted",
    "lineage_constraints_audited",
    "lineage_constraints_accepted",
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
    "authored_scope_division_declaration_receipt_boundary_overridden",
    "authored_scope_division_declaration_receipt_boundary_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_pdf_ingestion_as_standing_basis",
    "direct_receipt_to_audit_completion_conversion",
    "direct_receipt_to_standing_conversion",
    "direct_receipt_to_scope_declaration_conversion",
    "direct_receipt_to_candidate_specific_basis_emission_conversion",
    "direct_receipt_to_distinctness_support_conversion",
    "direct_digest_to_truth_conversion",
    "direct_hash_to_standing_conversion",
    "direct_custody_to_standing_conversion",
    "direct_transcription_to_standing_conversion",
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
    "receipt_operation_recorded",
    "receipt_performed",
    "contribution_map_present",
    "sibling_non_monarchy_present",
    "receipt_sealing_posture_present",
    "coupling_not_assigned_present",
    "no_third_model_present",
    "lineage_constraints_present",
    "for_audit_only",
    "target_operation_spec_markers_present",
    "receipt_boundary_terminal_summary_markers_present",
    "scope_division_declaration_operation_terminal_summary_markers_present",
    "existence_claim_evidence_check_terminal_summary_markers_present",
    "differentiation_operation_terminal_summary_markers_present",
    "distinctness_operation_terminal_summary_markers_present",
    "basis_emission_operation_terminal_summary_markers_present",
    "scope_division_declaration_boundary_terminal_summary_markers_present",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "OPERATION_SPEC_REFERENCE_MISSING",
    "OPERATION_SPEC_MARKER_MISSING",
    "RECEIPT_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RECEIPT_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
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
    "OPERATION_ID_NOT_EXPECTED",
    "OPERATION_TYPE_NOT_EXPECTED",
    "OPERATION_VERSION_NOT_EXPECTED",
    "OPERATION_SCOPE_NOT_EXPECTED",
    "UPSTREAM_BOUNDARY_NOT_EXPECTED",
    "MATERIAL_METADATA_MISSING_OR_INVALID",
    "DIGEST_REQUEST_MISSING_MATERIAL_PATH",
    "DIGEST_ALGORITHM_UNSUPPORTED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PROHIBITED_AUDIT_OR_STANDING_REQUESTED",
    "PROHIBITED_SIGNATURE_OR_DIGEST_CONVERSION_REQUESTED",
    "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "REQUESTED_RAW_MATERIAL_BODY_RETURN",
    "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_audit_performance": "PROHIBITED_AUDIT_OR_STANDING_REQUESTED",
    "request_declaration_standing_basis_admission": "PROHIBITED_AUDIT_OR_STANDING_REQUESTED",
    "request_digest_truth_conversion": "PROHIBITED_SIGNATURE_OR_DIGEST_CONVERSION_REQUESTED",
    "request_hash_standing_conversion": "PROHIBITED_SIGNATURE_OR_DIGEST_CONVERSION_REQUESTED",
    "request_custody_standing_conversion": "PROHIBITED_SIGNATURE_OR_DIGEST_CONVERSION_REQUESTED",
    "request_transcription_standing_conversion": "PROHIBITED_SIGNATURE_OR_DIGEST_CONVERSION_REQUESTED",
    "request_signature_scope_standing_conversion": "PROHIBITED_SIGNATURE_OR_DIGEST_CONVERSION_REQUESTED",
    "request_signature_candidate_specific_basis_emission_conversion": "PROHIBITED_SIGNATURE_OR_DIGEST_CONVERSION_REQUESTED",
    "request_signature_distinctness_support_conversion": "PROHIBITED_SIGNATURE_OR_DIGEST_CONVERSION_REQUESTED",
    "request_authored_scope_claim_standing_acceptance": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_motion_scope_standing_acceptance": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_regulation_scope_standing_acceptance": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_motion_regulation_division_audit": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_motion_regulation_division_acceptance": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_sibling_non_monarchy_audit": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_sibling_non_monarchy_acceptance": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_coupling_not_assigned_audit": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_coupling_not_assigned_acceptance": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_no_third_model_audit": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_no_third_model_acceptance": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_lineage_constraints_audit": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_lineage_constraints_acceptance": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_candidate_a_scope_declaration": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_candidate_b_scope_declaration": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_basis_bearing_scope_division_declaration": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
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
    "request_coupling_assignment_to_candidate_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_candidate_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_model_admission": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
}

SENSITIVE_BODY_KEYS = {
    "raw_body",
    "raw_material_body",
    "raw_pdf_body",
    "raw_markdown_body",
    "markdown_body",
    "full_body",
    "full_text",
    "extracted_text",
    "source_body",
    "hidden_repo_state",
    "current_working_tree",
}
CUSTODY_POSTURES = ("CUSTODY_RECORDED_FOR_AUDIT_ONLY", "CUSTODY_NOT_RECORDED")
TEXT_EXTRACTION_POSTURES = ("TRANSCRIPTION_NOT_PERFORMED", "TEXT_EXTRACTED_FOR_AUDIT_ONLY")
DIGEST_SCOPE = "RECEIPT_METADATA_ONLY"

OPERATION_SPEC_MARKER_CLASSES = (
    (
        "operation_identity",
        (
            "Descendant Body Candidate Authored Scope Division Declaration Receipt Operation V0 Minimum Specification",
            OPERATION_TYPE,
            OPERATION_ID,
            OPERATION_SCOPE,
        ),
    ),
    (
        "upstream_boundary",
        (UPSTREAM_BOUNDARY_TYPE, UPSTREAM_BOUNDARY_OUTCOME_REQUIRED, ADMISSIBLE_FUTURE_ROUTE),
    ),
    (
        "expected_material_identity",
        (
            RECEIVED_MATERIAL_EXPECTED_FILENAME,
            RECEIVED_MATERIAL_EXPECTED_TITLE,
            RECEIVED_MATERIAL_EXPECTED_VERSION,
            RECEIVED_MATERIAL_EXPECTED_DATE,
            RECEIVED_MATERIAL_EXPECTED_AUTHOR,
            RECEIVED_MATERIAL_EXPECTED_SIGNATURE_ROLE,
            RECEIVED_MATERIAL_EXPECTED_PREDECESSOR,
            RECEIVED_MATERIAL_PREDECESSOR_ROLE,
        ),
    ),
    (
        "required_target_posture",
        (
            "contribution-map",
            "sibling-non-monarchy",
            "receipt-sealing",
            "coupling-not-assigned",
            "no-third-model",
            "lineage-constraints",
        ),
    ),
    (
        "metadata_only_receipt",
        (
            "Receipt is not audit",
            "Receipt metadata is not audit result",
            "Digest is not truth",
            "Hash is not standing",
            "Custody is not standing",
            "Transcription is not standing",
            "Signature is authorship attestation only",
            "V2 receipt does not erase V1",
        ),
    ),
    (
        "non_standing_non_conversion",
        (
            "declaration_admitted_as_standing_basis = false",
            "signature_treated_as_scope_standing = false",
            "signature_treated_as_candidate_specific_basis_emission = false",
            "signature_treated_as_distinctness_support = false",
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
            "No third candidate, third model, or standing body is admitted",
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
            "api_created = false",
            "currentness_created = false",
            "authority_created = false",
            "follow_on_authorized = false",
        ),
    ),
    (
        "completed_receipt_boundary_relation",
        (
            UPSTREAM_BOUNDARY_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 84",
            "future_receipt_operation_type = DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION",
            "external_declaration_role = PROPOSED_AUTHORED_AUDIT_MATERIAL",
        ),
    ),
    (
        "completed_scope_division_operation_relation",
        (
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
            "failed_check_count = 0",
            "passed_check_count = 96",
            "missing non-cosmetic candidate A scope declaration",
            "missing non-cosmetic candidate B scope declaration",
            "missing basis-bearing scope division declaration",
            "does not close that gap",
        ),
    ),
    (
        "contaminated_lineage_preservation",
        (
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md",
            "remains preserved contaminated lineage",
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
            "direct receipt-to-audit-completion",
            "standing, scope-declaration",
            "direct digest-to-truth",
            "hash-to-standing",
            "custody-to-standing",
            "transcription-to-standing",
            "signature-to-standing",
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
            "This operation spec defines only a future receipt operation shape",
            "Receipt is not audit",
            "Receipt metadata is not audit result",
            "The prior operation line remains at REQUIRES_ADDITIONAL_BASIS until receipt, audit, and any successor closure are separately bounded and passed.",
        ),
    ),
)

UPSTREAM_REQUIREMENTS = (
    (
        "receipt_boundary_terminal_summary_reference",
        DEFAULT_RECEIPT_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "RECEIPT_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RECEIPT_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        (
            UPSTREAM_BOUNDARY_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 84",
            "future_receipt_operation_type = DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION",
        ),
        "receipt_boundary_terminal_summary_markers_present",
    ),
    (
        "scope_division_declaration_operation_terminal_summary_reference",
        DEFAULT_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
            "failed_check_count = 0",
            "passed_check_count = 96",
            "missing non-cosmetic candidate A scope declaration",
            "missing non-cosmetic candidate B scope declaration",
            "missing basis-bearing scope division declaration",
        ),
        "scope_division_declaration_operation_terminal_summary_markers_present",
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
        ("DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",),
        "differentiation_operation_terminal_summary_markers_present",
    ),
    (
        "distinctness_operation_terminal_summary_reference",
        DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ("DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",),
        "distinctness_operation_terminal_summary_markers_present",
    ),
    (
        "basis_emission_operation_terminal_summary_reference",
        DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ("DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS",),
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

WHAT_REMAINS_OPEN = (
    "authored declaration audit operation",
    "audit of Candidate A Motion-side scope",
    "audit of Candidate B Regulation-side scope",
    "audit of Motion/Regulation non-cosmetic difference",
    "audit of basis-bearing scope division",
    "audit of sibling non-monarchy condition",
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
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _resolve_declared_path(value: Any) -> Path | None:
    if isinstance(value, Path):
        path = value
    elif _is_non_empty_string(value):
        path = Path(value)
    else:
        return None
    return path if path.is_absolute() else REPO_ROOT / path


def _read_declared_text(value: Any) -> str | None:
    path = _resolve_declared_path(value)
    if path is None or not path.is_file():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def _is_sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return lowered in SENSITIVE_BODY_KEYS or lowered.endswith("_body") or "raw_" in lowered


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
    check: dict[str, Any] = {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected),
        "actual_posture": _sanitize(actual),
    }
    if not passed and code:
        check["block_code"] = code
        check["failure_code"] = code
    checks.append(check)


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
    checks: list[dict[str, Any]], request: Mapping[str, Any], field: str, code: str
) -> None:
    path = _resolve_declared_path(request.get(field))
    _add_check(
        checks,
        f"{field} readable file reference",
        path is not None and path.is_file(),
        "declared readable file path",
        str(path) if path is not None else request.get(field),
        code,
    )


def _validate_exact(
    checks: list[dict[str, Any]], request: Mapping[str, Any], field: str, expected: Any, code: str
) -> None:
    _add_check(checks, f"{field} exact", request.get(field) == expected, expected, request.get(field), code)


def _validate_non_claims(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        _add_check(
            checks,
            "required non-claims false",
            False,
            "mapping with every required key exactly false",
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


def _validate_operation_spec(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> bool:
    text = _read_declared_text(request.get("operation_spec_reference"))
    passed, missing = _marker_classes_present(text, OPERATION_SPEC_MARKER_CLASSES)
    _add_check(
        checks,
        "target operation spec posture classes present",
        passed,
        "all required operation spec posture classes",
        {"missing_posture_classes": missing},
        "OPERATION_SPEC_MARKER_MISSING",
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
        _add_check(checks, f"{field} not requested", request.get(field) is not True, False, request.get(field), code)
    _add_check(
        checks,
        "return_raw_material_body not requested",
        request.get("return_raw_material_body") is not True,
        False,
        request.get("return_raw_material_body"),
        "REQUESTED_RAW_MATERIAL_BODY_RETURN",
    )
    _add_check(
        checks,
        "return_raw_markdown_body not requested",
        request.get("return_raw_markdown_body") is not True,
        False,
        request.get("return_raw_markdown_body"),
        "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
    )


def _validate_metadata(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    expected = (
        ("received_material_type", RECEIVED_MATERIAL_TYPE),
        ("received_material_filename", RECEIVED_MATERIAL_EXPECTED_FILENAME),
        ("received_material_title", RECEIVED_MATERIAL_EXPECTED_TITLE),
        ("received_material_version", RECEIVED_MATERIAL_EXPECTED_VERSION),
        ("received_material_date", RECEIVED_MATERIAL_EXPECTED_DATE),
        ("received_material_author", RECEIVED_MATERIAL_EXPECTED_AUTHOR),
        ("received_material_signature_present", RECEIVED_MATERIAL_EXPECTED_SIGNATURE_PRESENT),
        ("received_material_signature_role", RECEIVED_MATERIAL_EXPECTED_SIGNATURE_ROLE),
        ("received_material_predecessor", RECEIVED_MATERIAL_EXPECTED_PREDECESSOR),
        ("received_material_predecessor_role", RECEIVED_MATERIAL_PREDECESSOR_ROLE),
        ("contribution_map_present", True),
        ("sibling_non_monarchy_present", True),
        ("receipt_sealing_posture_present", True),
        ("coupling_not_assigned_present", True),
        ("no_third_model_present", True),
        ("lineage_constraints_present", True),
        ("for_audit_only", True),
    )
    malformed = [field for field, value in expected if request.get(field) != value]
    _add_check(
        checks,
        "required receipt metadata exact",
        not malformed,
        "all required V2 receipt metadata fields",
        {"malformed_fields": malformed},
        "MATERIAL_METADATA_MISSING_OR_INVALID",
    )


def _validate_optional_metadata(
    checks: list[dict[str, Any]], request: Mapping[str, Any], allow_digest_read: bool
) -> dict[str, Any]:
    metadata: dict[str, Any] = {
        "material_path_recorded": False,
        "material_path": None,
        "digest_recorded": False,
        "digest_algorithm": None,
        "digest_value": None,
        "digest_scope": None,
        "custody_posture_recorded": False,
        "custody_posture": None,
        "text_extraction_posture_recorded": False,
        "text_extraction_posture": None,
    }
    material_path_value = request.get("material_path")
    if material_path_value is not None:
        _add_check(
            checks,
            "optional material path is bounded string",
            _is_non_empty_string(material_path_value),
            "non-empty path string or null",
            material_path_value,
            "MATERIAL_METADATA_MISSING_OR_INVALID",
        )
        if _is_non_empty_string(material_path_value):
            metadata["material_path_recorded"] = True
            metadata["material_path"] = str(material_path_value)

    compute_digest = request.get("request_digest_computation")
    _add_check(
        checks,
        "digest computation request boolean",
        isinstance(compute_digest, bool),
        "boolean",
        compute_digest,
        "MATERIAL_METADATA_MISSING_OR_INVALID",
    )
    if compute_digest is True:
        material_path = _resolve_declared_path(material_path_value)
        _add_check(
            checks,
            "digest request material path readable file",
            material_path is not None and material_path.is_file(),
            "explicit readable material file path",
            str(material_path) if material_path is not None else material_path_value,
            "DIGEST_REQUEST_MISSING_MATERIAL_PATH",
        )
        _add_check(
            checks,
            "digest request algorithm supported",
            request.get("digest_algorithm") == "SHA-256",
            "SHA-256",
            request.get("digest_algorithm"),
            "DIGEST_ALGORITHM_UNSUPPORTED",
        )
        can_compute = (
            allow_digest_read
            and material_path is not None
            and material_path.is_file()
            and request.get("digest_algorithm") == "SHA-256"
        )
        if can_compute:
            try:
                digest = hashlib.sha256()
                with material_path.open("rb") as handle:
                    for chunk in iter(lambda: handle.read(65536), b""):
                        digest.update(chunk)
                metadata.update(
                    {
                        "digest_recorded": True,
                        "digest_algorithm": "SHA-256",
                        "digest_value": digest.hexdigest(),
                        "digest_scope": DIGEST_SCOPE,
                    }
                )
            except OSError as exc:
                _add_check(
                    checks,
                    "digest request material path readable bytes",
                    False,
                    "readable explicit material file",
                    str(exc),
                    "DIGEST_REQUEST_MISSING_MATERIAL_PATH",
                )
    else:
        supplied = any(request.get(key) is not None for key in ("digest_value", "digest_algorithm", "digest_scope"))
        if supplied:
            valid = (
                _is_non_empty_string(request.get("digest_value"))
                and request.get("digest_algorithm") == "SHA-256"
                and request.get("digest_scope") == DIGEST_SCOPE
            )
            _add_check(
                checks,
                "provided digest metadata bounded",
                valid,
                "digest value with SHA-256 and RECEIPT_METADATA_ONLY scope",
                {
                    "digest_value_supplied": _is_non_empty_string(request.get("digest_value")),
                    "digest_algorithm": request.get("digest_algorithm"),
                    "digest_scope": request.get("digest_scope"),
                },
                "MATERIAL_METADATA_MISSING_OR_INVALID",
            )
            if valid:
                metadata.update(
                    {
                        "digest_recorded": True,
                        "digest_algorithm": "SHA-256",
                        "digest_value": str(request.get("digest_value")),
                        "digest_scope": DIGEST_SCOPE,
                    }
                )

    custody = request.get("custody_posture")
    if custody is not None:
        _add_check(
            checks,
            "custody posture bounded",
            custody in CUSTODY_POSTURES,
            CUSTODY_POSTURES,
            custody,
            "MATERIAL_METADATA_MISSING_OR_INVALID",
        )
        if custody in CUSTODY_POSTURES:
            metadata["custody_posture_recorded"] = True
            metadata["custody_posture"] = custody

    text_posture = request.get("text_extraction_posture")
    if text_posture is not None:
        _add_check(
            checks,
            "text extraction posture bounded",
            text_posture in TEXT_EXTRACTION_POSTURES,
            TEXT_EXTRACTION_POSTURES,
            text_posture,
            "MATERIAL_METADATA_MISSING_OR_INVALID",
        )
        if text_posture in TEXT_EXTRACTION_POSTURES:
            metadata["text_extraction_posture_recorded"] = True
            metadata["text_extraction_posture"] = text_posture
    return metadata


def _marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    names = {
        "target_operation_spec_markers_present": "target operation spec posture classes present",
        "receipt_boundary_terminal_summary_markers_present": (
            "receipt_boundary_terminal_summary_reference expected markers present"
        ),
        "scope_division_declaration_operation_terminal_summary_markers_present": (
            "scope_division_declaration_operation_terminal_summary_reference expected markers present"
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
        key: any(check.get("check_name") == name and check.get("passed") is True for check in checks)
        for key, name in names.items()
    }


def _operation_object(
    request: Mapping[str, Any], recorded: bool, metadata: Mapping[str, Any], flags: Mapping[str, bool]
) -> dict[str, Any]:
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "authored_scope_division_declaration_receipt_operation_id": OPERATION_ID,
        "authored_scope_division_declaration_receipt_operation_type": OPERATION_TYPE,
        "authored_scope_division_declaration_receipt_operation_version": OPERATION_VERSION,
        "authored_scope_division_declaration_receipt_operation_scope": OPERATION_SCOPE,
        "upstream_boundary_type": UPSTREAM_BOUNDARY_TYPE,
        "upstream_boundary_outcome_required": UPSTREAM_BOUNDARY_OUTCOME_REQUIRED,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "received_material_status": "RECEIVED_AS_METADATA_FOR_AUDIT_ONLY" if recorded else "NOT_RECEIVED",
        "received_material_type": RECEIVED_MATERIAL_TYPE,
        "received_material_filename": RECEIVED_MATERIAL_EXPECTED_FILENAME,
        "received_material_title": RECEIVED_MATERIAL_EXPECTED_TITLE,
        "received_material_version": RECEIVED_MATERIAL_EXPECTED_VERSION,
        "received_material_date": RECEIVED_MATERIAL_EXPECTED_DATE,
        "received_material_author": RECEIVED_MATERIAL_EXPECTED_AUTHOR,
        "received_material_signature_present": RECEIVED_MATERIAL_EXPECTED_SIGNATURE_PRESENT,
        "received_material_signature_role": RECEIVED_MATERIAL_EXPECTED_SIGNATURE_ROLE,
        "received_material_predecessor": RECEIVED_MATERIAL_EXPECTED_PREDECESSOR,
        "received_material_predecessor_role": RECEIVED_MATERIAL_PREDECESSOR_ROLE,
        "contribution_map_present": recorded,
        "sibling_non_monarchy_present": recorded,
        "receipt_sealing_posture_present": recorded,
        "coupling_not_assigned_present": recorded,
        "no_third_model_present": recorded,
        "lineage_constraints_present": recorded,
        "for_audit_only": recorded,
        **_canonical_non_claims(),
        **flags,
    }
    operation["receipt_operation_recorded"] = recorded
    operation["receipt_performed"] = recorded
    operation["audit_performed"] = False
    operation.update(
        {
            "material_path_recorded": bool(recorded and metadata.get("material_path_recorded")),
            "material_path": metadata.get("material_path") if recorded else None,
            "digest_recorded": bool(recorded and metadata.get("digest_recorded")),
            "digest_algorithm": metadata.get("digest_algorithm") if recorded else None,
            "digest_value": metadata.get("digest_value") if recorded else None,
            "digest_scope": metadata.get("digest_scope") if recorded else None,
            "custody_posture_recorded": bool(recorded and metadata.get("custody_posture_recorded")),
            "custody_posture": metadata.get("custody_posture") if recorded else None,
            "text_extraction_posture_recorded": bool(recorded and metadata.get("text_extraction_posture_recorded")),
            "text_extraction_posture": metadata.get("text_extraction_posture") if recorded else None,
        }
    )
    return operation


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("descendant_body_candidate_authored_scope_division_declaration_receipt_operation")
    operation_map = operation if isinstance(operation, Mapping) else {}
    checks = result.get("authored_scope_division_declaration_receipt_operation_checks")
    check_records = checks if isinstance(checks, list) else []
    upstream = result.get("upstream_basis")
    upstream_map = upstream if isinstance(upstream, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "failed_check_count": sum(
            1 for check in check_records if isinstance(check, Mapping) and check.get("passed") is False
        ),
        "passed_check_count": sum(
            1 for check in check_records if isinstance(check, Mapping) and check.get("passed") is True
        ),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "operation_id": operation_map.get("operation_id"),
        "operation_type": operation_map.get("operation_type"),
        "operation_version": operation_map.get("operation_version"),
        "operation_scope": operation_map.get("operation_scope"),
        "upstream_boundary_type": operation_map.get("upstream_boundary_type"),
        "upstream_boundary_outcome_required": operation_map.get("upstream_boundary_outcome_required"),
        "admissible_future_route": operation_map.get("admissible_future_route"),
        "selected_target_spec_path": upstream_map.get("operation_spec_reference"),
        "completed_receipt_boundary_terminal_summary_path": upstream_map.get(
            "receipt_boundary_terminal_summary_reference"
        ),
        "completed_scope_division_operation_terminal_summary_path": upstream_map.get(
            "scope_division_declaration_operation_terminal_summary_reference"
        ),
        "result_level_non_claims_canonical_false": all(
            isinstance(result.get("non_claims"), Mapping)
            and result["non_claims"].get(key) is False
            for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }
    for key in (
        "received_material_status",
        "received_material_type",
        "received_material_filename",
        "received_material_title",
        "received_material_version",
        "received_material_date",
        "received_material_author",
        "received_material_signature_present",
        "received_material_signature_role",
        "received_material_predecessor",
        "received_material_predecessor_role",
        "contribution_map_present",
        "sibling_non_monarchy_present",
        "receipt_sealing_posture_present",
        "coupling_not_assigned_present",
        "no_third_model_present",
        "lineage_constraints_present",
        "for_audit_only",
        "receipt_operation_recorded",
        "receipt_performed",
        "audit_performed",
        "declaration_admitted_as_standing_basis",
        "digest_recorded",
        "digest_algorithm",
        "digest_scope",
        "material_path_recorded",
        "custody_posture_recorded",
        "text_extraction_posture_recorded",
        *REQUIRED_FALSE_NON_CLAIMS[4:],
        *ALLOWED_TRUE_RECORDED_FIELDS[-8:],
    ):
        summary[key] = operation_map.get(key)
    return _sanitize(summary)


def build_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary without returning source material bodies."""

    return _build_summary(result)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    recorded: bool,
    metadata: Mapping[str, Any],
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    flags = _marker_flags(checks)
    operation = _operation_object(request, recorded, metadata, flags)
    result: dict[str, Any] = {
        "authored_scope_division_declaration_receipt_operation_metadata": {
            "operation_id": OPERATION_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_authored_scope_division_declaration_receipt_operation_basis": _sanitize(request),
        "upstream_basis": {
            "operation_spec_reference": request.get("operation_spec_reference"),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **flags,
        },
        "descendant_body_candidate_authored_scope_division_declaration_receipt_operation": operation,
        "authored_scope_division_declaration_receipt_operation_checks": checks,
        "authored_scope_division_declaration_receipt_operation_statement": {
            "outcome": outcome,
            "receipt_operation_recorded": recorded,
            "receipt_performed": recorded,
            "audit_performed": False,
            "declaration_admitted_as_standing_basis": False,
            "result_level_non_claims_canonical_false": True,
        },
        "authored_scope_division_declaration_receipt_operation_non_meaning": {
            "not_audit": True,
            "not_standing_basis": True,
            "not_scope_declaration": True,
            "not_candidate_specific_basis_emission": True,
            "not_distinctness_support": True,
            "not_candidate_standing": True,
            "not_descendant_body_creation": True,
            "not_relation": True,
            "not_runtime": True,
            "not_authority": True,
            "not_coupling": True,
            "not_third_candidate_or_model": True,
            "not_follow_on": True,
        },
        "receipt_metadata": {
            "received_material_status": operation["received_material_status"],
            "material_path_recorded": operation["material_path_recorded"],
            "material_path": operation["material_path"],
            "digest_recorded": operation["digest_recorded"],
            "digest_algorithm": operation["digest_algorithm"],
            "digest_value": operation["digest_value"],
            "digest_scope": operation["digest_scope"],
            "custody_posture_recorded": operation["custody_posture_recorded"],
            "custody_posture": operation["custody_posture"],
            "text_extraction_posture_recorded": operation["text_extraction_posture_recorded"],
            "text_extraction_posture": operation["text_extraction_posture"],
        },
        "permitted_future_route": [
            "receipt records bounded metadata as proposed authored audit material only",
            "a later separately bounded audit may evaluate the received material",
            "no later closure is authorized by receipt alone",
        ],
        "blocked_routes": [
            "direct conversion of receipt, digest, hash, custody, transcription, signature, or declaration into standing or audit",
            "direct coupling, third-candidate, or third-model route",
            "repair, scan, validation, and downstream authorization routes",
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
    result["authored_scope_division_declaration_receipt_operation_summary"] = _build_summary(result)
    return result


def _blocked_result(
    request: Mapping[str, Any], checks: list[dict[str, Any]], code: str, reason: str
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(request, OUTCOME_BLOCKED, checks, False, {}, code, reason)


def build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one explicit metadata-only receipt request with no source body access."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "authored_scope_division_declaration_receipt_operation_id": OPERATION_ID,
        "authored_scope_division_declaration_receipt_operation_type": OPERATION_TYPE,
        "authored_scope_division_declaration_receipt_operation_version": OPERATION_VERSION,
        "authored_scope_division_declaration_receipt_operation_scope": OPERATION_SCOPE,
        "upstream_boundary_type": UPSTREAM_BOUNDARY_TYPE,
        "upstream_boundary_outcome_required": UPSTREAM_BOUNDARY_OUTCOME_REQUIRED,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "operation_spec_reference": DEFAULT_OPERATION_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "received_material_type": RECEIVED_MATERIAL_TYPE,
        "received_material_filename": RECEIVED_MATERIAL_EXPECTED_FILENAME,
        "received_material_title": RECEIVED_MATERIAL_EXPECTED_TITLE,
        "received_material_version": RECEIVED_MATERIAL_EXPECTED_VERSION,
        "received_material_date": RECEIVED_MATERIAL_EXPECTED_DATE,
        "received_material_author": RECEIVED_MATERIAL_EXPECTED_AUTHOR,
        "received_material_signature_present": RECEIVED_MATERIAL_EXPECTED_SIGNATURE_PRESENT,
        "received_material_signature_role": RECEIVED_MATERIAL_EXPECTED_SIGNATURE_ROLE,
        "received_material_predecessor": RECEIVED_MATERIAL_EXPECTED_PREDECESSOR,
        "received_material_predecessor_role": RECEIVED_MATERIAL_PREDECESSOR_ROLE,
        "contribution_map_present": True,
        "sibling_non_monarchy_present": True,
        "receipt_sealing_posture_present": True,
        "coupling_not_assigned_present": True,
        "no_third_model_present": True,
        "lineage_constraints_present": True,
        "for_audit_only": True,
        "material_path": None,
        "request_digest_computation": False,
        "digest_algorithm": None,
        "digest_value": None,
        "digest_scope": None,
        "custody_posture": None,
        "text_extraction_posture": None,
        "return_raw_material_body": False,
        "return_raw_markdown_body": False,
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    aliases = {
        "target_spec_path": "operation_spec_reference",
        "operation_spec_path": "operation_spec_reference",
        "receipt_boundary_terminal_summary_path": "receipt_boundary_terminal_summary_reference",
        "scope_division_declaration_operation_terminal_summary_path": (
            "scope_division_declaration_operation_terminal_summary_reference"
        ),
    }
    for alias, target in aliases.items():
        if alias in overrides and target not in overrides:
            overrides[target] = overrides[alias]
    request.update(overrides)
    return request


def resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(
    declared_authored_scope_division_declaration_receipt_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Record one metadata-only receipt result or a bounded public block."""

    if declared_authored_scope_division_declaration_receipt_operation is None:
        request = build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_request()
    elif not isinstance(declared_authored_scope_division_declaration_receipt_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_authored_scope_division_declaration_receipt_operation).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_authored_scope_division_declaration_receipt_operation))

    checks: list[dict[str, Any]] = []
    intent = request.get("intent")
    _add_check(checks, "intent supported", intent in SUPPORTED_INTENTS, SUPPORTED_INTENTS, intent, "UNSUPPORTED_INTENT")
    if intent == INTENT_BLOCK:
        return _blocked_result(request, checks, "EXPLICIT_BLOCK_REQUESTED", "explicit block intent requested")
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(request, checks, "UNSUPPORTED_INTENT", "intent is unsupported")

    exact_fields = (
        ("operation_id", OPERATION_ID, "OPERATION_ID_NOT_EXPECTED"),
        ("operation_type", OPERATION_TYPE, "OPERATION_TYPE_NOT_EXPECTED"),
        ("operation_version", OPERATION_VERSION, "OPERATION_VERSION_NOT_EXPECTED"),
        ("operation_scope", OPERATION_SCOPE, "OPERATION_SCOPE_NOT_EXPECTED"),
        ("authored_scope_division_declaration_receipt_operation_id", OPERATION_ID, "OPERATION_ID_NOT_EXPECTED"),
        ("authored_scope_division_declaration_receipt_operation_type", OPERATION_TYPE, "OPERATION_TYPE_NOT_EXPECTED"),
        ("authored_scope_division_declaration_receipt_operation_version", OPERATION_VERSION, "OPERATION_VERSION_NOT_EXPECTED"),
        ("authored_scope_division_declaration_receipt_operation_scope", OPERATION_SCOPE, "OPERATION_SCOPE_NOT_EXPECTED"),
        ("upstream_boundary_type", UPSTREAM_BOUNDARY_TYPE, "UPSTREAM_BOUNDARY_NOT_EXPECTED"),
        ("upstream_boundary_outcome_required", UPSTREAM_BOUNDARY_OUTCOME_REQUIRED, "UPSTREAM_BOUNDARY_NOT_EXPECTED"),
        ("admissible_future_route", ADMISSIBLE_FUTURE_ROUTE, "UPSTREAM_BOUNDARY_NOT_EXPECTED"),
    )
    for field, expected, code in exact_fields:
        _validate_exact(checks, request, field, expected, code)

    _validate_reference(checks, request, "operation_spec_reference", "OPERATION_SPEC_REFERENCE_MISSING")
    _validate_operation_spec(checks, request)
    for field, _, missing_code, _, _, _ in UPSTREAM_REQUIREMENTS:
        _validate_reference(checks, request, field, missing_code)
    _validate_upstream_markers(checks, request)
    _validate_metadata(checks, request)
    _validate_non_claims(checks, request)
    _validate_prohibited_requests(checks, request)
    metadata = _validate_optional_metadata(
        checks, request, allow_digest_read=not bool(_failed_codes(checks))
    )
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
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, False, metadata)
    return _build_result(request, OUTCOME_RECORDED, checks, True, metadata)


def resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_from_path(
    declared_authored_scope_division_declaration_receipt_operation_path: Path | str,
) -> dict[str, Any]:
    """Read one explicit JSON request object and resolve it."""

    path = Path(declared_authored_scope_division_declaration_receipt_operation_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            request = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request path readable JSON",
            False,
            "readable JSON object",
            str(exc),
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request path is unreadable or not JSON")
    return resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)


def write_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write deterministic JSON without overwriting a prior result."""

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
            json.dump(_json_ready(result), handle, ensure_ascii=True, indent=2, sort_keys=True)
            handle.write("\n")
        return final_path
    except OSError as exc:
        raise DescendantBodyCandidateAuthoredScopeDivisionDeclarationReceiptOperationV0MinError(
            f"WRITE_REFUSED: {exc}"
        ) from exc
