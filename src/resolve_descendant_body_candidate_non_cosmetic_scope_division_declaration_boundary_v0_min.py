"""Resolve one candidate non-cosmetic scope-division declaration boundary.

This module records a boundary only. It preserves the completed
candidate-specific distinctness basis emission operation's
REQUIRES_ADDITIONAL_BASIS result as clean, allows only a future scope
declaration operation shape to be considered, and refuses scope-label
laundering, cosmetic naming, standing, runtime, repair, scanning, emission,
distinctness rerun, and follow-on authorization.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateNonCosmeticScopeDivisionDeclarationBoundaryV0MinError(
    Exception
):
    """Raised when bounded result writing cannot be completed."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min"
)

OUTCOME_RECORDED = (
    "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED"
)
OUTCOME_BLOCKED = (
    "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_BLOCKED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_NOT_RECORDED = (
    "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_NOT_RECORDED,
)

BOUNDARY_TYPE = "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY"
FUTURE_DECLARATION_OPERATION_TYPE = (
    "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION"
)
BOUNDARY_VERSION = "0.1.0"
RUPTURE_CLASS_BLOCKED = "SCOPE_LABEL_LAUNDERING"
UPSTREAM_EMISSION_OPERATION_RESULT = "REQUIRES_ADDITIONAL_BASIS"

INTENT_RECORD = (
    "RECORD_DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min"
)

DEFAULT_BOUNDARY_ID = (
    "descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_001"
)
DEFAULT_BOUNDARY_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_V0_MIN_SPEC.md"
)
DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)

CORE_BOUNDARY_QUESTION = (
    "Given one completed candidate-specific distinctness basis emission operation that recorded "
    "REQUIRES_ADDITIONAL_BASIS because non-cosmetic candidate A scope, non-cosmetic candidate B "
    "scope, and basis-bearing scope division are missing from the current live repo basis, may "
    "the body define a future operation that declares non-cosmetic candidate A scope, "
    "non-cosmetic candidate B scope, and basis-bearing scope division, while forbidding "
    "scope-label laundering, cosmetic scope naming, id/role/label/template substitution, "
    "candidate-specific content emission, seal material emission, lineage receipt material "
    "emission, digest material emission, distinctness rerun, DISTINCTNESS_SUPPORTED, candidate "
    "records marked distinct, candidate standing, descendant-body creation, crossing, relation, "
    "FIELD machinery, runtime, currentness, authority, output, action, derivative reception, "
    "synchronization, repair, scan, validation enforcement, prior unsupported claim validation, "
    "and follow-on authorization?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "candidate_non_cosmetic_scope_division_declaration_operation_created",
    "candidate_non_cosmetic_scope_division_declaration_operation_performed",
    "candidate_non_cosmetic_scope_division_declaration_operation_recorded",
    "candidate_a_scope_declared",
    "candidate_b_scope_declared",
    "basis_bearing_scope_division_declared",
    "candidate_specific_distinctness_basis_emission_operation_rerun",
    "candidate_specific_distinctness_basis_emission_operation_recorded",
    "candidate_specific_content_emitted",
    "separate_seal_material_emitted",
    "separate_lineage_receipt_material_emitted",
    "separate_digest_material_emitted",
    "distinctness_operation_rerun",
    "distinctness_supported_recorded",
    "candidate_records_marked_distinct",
    "candidate_records_distinct",
    "candidate_standing_authorized",
    "candidate_standing_created",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_created",
    "standing_descendant_created",
    "descendant_standing_check_performed",
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
    "scan_performed",
    "repository_scan_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "scope_label_laundering_treated_as_basis",
    "cosmetic_scope_naming_treated_as_basis",
    "id_role_label_difference_treated_as_scope_basis",
    "shared_evidence_treated_as_scope_basis",
    "operation_evidence_alone_treated_as_scope_basis",
    "contaminated_lineage_treated_as_clean_scope_basis",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "candidate_non_cosmetic_scope_division_declaration_boundary_recorded",
    "boundary_created",
    "upstream_emission_operation_result_is_requires_additional_basis",
    "requires_additional_basis_preserved_as_clean_result",
    "candidate_a_scope_missing_upstream",
    "candidate_b_scope_missing_upstream",
    "basis_bearing_scope_division_missing_upstream",
    "future_scope_declaration_operation_shape_allowed",
    "scope_label_laundering_not_allowed",
    "cosmetic_scope_naming_not_allowed",
    "id_role_label_difference_not_allowed_as_scope_basis",
    "shared_evidence_not_allowed_as_scope_basis",
    "operation_evidence_alone_not_allowed_as_scope_basis",
    "contaminated_lineage_not_allowed_as_clean_scope_basis",
    "future_scope_declaration_operation_not_created",
    "candidate_a_scope_not_declared",
    "candidate_b_scope_not_declared",
    "basis_bearing_scope_division_not_declared",
    "candidate_specific_content_not_emitted",
    "separate_seal_material_not_emitted",
    "separate_lineage_receipt_material_not_emitted",
    "separate_digest_material_not_emitted",
    "emission_operation_not_rerun",
    "distinctness_operation_not_rerun",
    "distinctness_supported_not_recorded",
    "candidate_records_not_marked_distinct",
    "candidate_standing_not_authorized",
    "descendant_bodies_not_created",
    "standing_descendants_not_created",
    "first_crossing_not_authorized",
    "relation_not_created",
    "field_machinery_not_created",
    "runtime_not_created",
    "api_not_created",
    "currentness_not_created",
    "authority_not_created",
    "standing_not_created",
    "output_not_authorized",
    "action_not_authorized",
    "derivative_reception_not_authorized",
    "synchronization_not_authorized",
    "follow_on_not_authorized",
    "prior_unsupported_claims_not_validated",
    "affected_file_not_repaired",
    "affected_file_not_treated_as_clean_basis",
    "contaminated_lineage_not_treated_as_clean_basis",
    "existence_claim_evidence_check_not_overridden",
    "existence_claim_evidence_check_not_bypassed",
    "differentiation_operation_not_overridden",
    "differentiation_operation_not_bypassed",
    "distinctness_operation_boundary_not_overridden",
    "distinctness_operation_boundary_not_bypassed",
    "distinctness_operation_not_overridden",
    "distinctness_operation_not_bypassed",
    "basis_emission_boundary_not_overridden",
    "basis_emission_boundary_not_bypassed",
    "basis_emission_operation_not_overridden",
    "basis_emission_operation_not_bypassed",
    "scan_not_performed",
    "repository_scan_not_performed",
    "repair_not_performed",
    "validation_not_enforced",
    "hidden_repair_not_performed",
    "silent_overwrite_not_performed",
    "boundary_spec_markers_present",
    "completed_basis_emission_operation_terminal_summary_markers_present",
    "completed_basis_emission_boundary_terminal_summary_markers_present",
    "completed_distinctness_operation_terminal_summary_markers_present",
    "completed_differentiation_operation_terminal_summary_markers_present",
    "result_level_non_claims_canonical_false",
)

REQUESTED_ACTION_FIELD_CODES = {
    "requested_scope_declaration_operation_definition": "REQUESTED_SCOPE_DECLARATION_OPERATION_DEFINITION",
    "requested_scope_declaration_operation_implementation": "REQUESTED_SCOPE_DECLARATION_OPERATION_IMPLEMENTATION",
    "requested_candidate_a_scope_declaration": "REQUESTED_CANDIDATE_A_SCOPE_DECLARATION",
    "requested_candidate_b_scope_declaration": "REQUESTED_CANDIDATE_B_SCOPE_DECLARATION",
    "requested_basis_bearing_scope_division_declaration": "REQUESTED_BASIS_BEARING_SCOPE_DIVISION_DECLARATION",
    "requested_candidate_specific_content_emission": "REQUESTED_CANDIDATE_SPECIFIC_CONTENT_EMISSION",
    "requested_separate_seal_material_emission": "REQUESTED_SEPARATE_SEAL_MATERIAL_EMISSION",
    "requested_separate_lineage_receipt_material_emission": "REQUESTED_SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMISSION",
    "requested_separate_digest_material_emission": "REQUESTED_SEPARATE_DIGEST_MATERIAL_EMISSION",
    "requested_basis_emission_operation_rerun": "REQUESTED_BASIS_EMISSION_OPERATION_RERUN",
    "requested_distinctness_operation_rerun": "REQUESTED_DISTINCTNESS_OPERATION_RERUN",
    "requested_distinctness_supported_recording": "REQUESTED_DISTINCTNESS_SUPPORTED_RECORDING",
    "requested_candidate_records_marked_distinct": "REQUESTED_CANDIDATE_RECORDS_MARKED_DISTINCT",
    "requested_repository_scan": "REQUESTED_REPOSITORY_SCAN",
    "requested_file_discovery": "REQUESTED_FILE_DISCOVERY",
    "requested_affected_file_repair": "REQUESTED_AFFECTED_FILE_REPAIR",
    "requested_affected_file_mutation": "REQUESTED_AFFECTED_FILE_MUTATION",
    "requested_prior_unsupported_claim_validation": "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION",
    "requested_existence_claim_evidence_check_override": "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDE",
    "requested_existence_claim_evidence_check_bypass": "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASS",
    "requested_differentiation_operation_override": "REQUESTED_DIFFERENTIATION_OPERATION_OVERRIDE",
    "requested_differentiation_operation_bypass": "REQUESTED_DIFFERENTIATION_OPERATION_BYPASS",
    "requested_distinctness_operation_boundary_override": "REQUESTED_DISTINCTNESS_OPERATION_BOUNDARY_OVERRIDE",
    "requested_distinctness_operation_boundary_bypass": "REQUESTED_DISTINCTNESS_OPERATION_BOUNDARY_BYPASS",
    "requested_distinctness_operation_override": "REQUESTED_DISTINCTNESS_OPERATION_OVERRIDE",
    "requested_distinctness_operation_bypass": "REQUESTED_DISTINCTNESS_OPERATION_BYPASS",
    "requested_basis_emission_boundary_override": "REQUESTED_BASIS_EMISSION_BOUNDARY_OVERRIDE",
    "requested_basis_emission_boundary_bypass": "REQUESTED_BASIS_EMISSION_BOUNDARY_BYPASS",
    "requested_basis_emission_operation_override": "REQUESTED_BASIS_EMISSION_OPERATION_OVERRIDE",
    "requested_basis_emission_operation_bypass": "REQUESTED_BASIS_EMISSION_OPERATION_BYPASS",
    "requested_candidate_standing_authorization": "REQUESTED_CANDIDATE_STANDING_AUTHORIZATION",
    "requested_descendant_body_creation": "REQUESTED_DESCENDANT_BODY_CREATION",
    "requested_standing_descendant_creation": "REQUESTED_STANDING_DESCENDANT_CREATION",
    "requested_descendant_standing_check": "REQUESTED_DESCENDANT_STANDING_CHECK",
    "requested_crossing_authorization": "REQUESTED_CROSSING_AUTHORIZATION",
    "requested_relation_creation": "REQUESTED_RELATION_CREATION",
    "requested_field_machinery_creation": "REQUESTED_FIELD_MACHINERY_CREATION",
    "requested_runtime_creation": "REQUESTED_RUNTIME_CREATION",
    "requested_currentness_creation": "REQUESTED_CURRENTNESS_CREATION",
    "requested_authority_creation": "REQUESTED_AUTHORITY_CREATION",
    "requested_output_authorization": "REQUESTED_OUTPUT_AUTHORIZATION",
    "requested_action_authorization": "REQUESTED_ACTION_AUTHORIZATION",
    "requested_derivative_reception_authorization": "REQUESTED_DERIVATIVE_RECEPTION_AUTHORIZATION",
    "requested_synchronization_authorization": "REQUESTED_SYNCHRONIZATION_AUTHORIZATION",
    "requested_follow_on_authorization": "REQUESTED_FOLLOW_ON_AUTHORIZATION",
    "requested_raw_markdown_body_return": "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
}

TOP_LEVEL_FALSE_FIELD_CODES = {
    "future_scope_declaration_operation_created": "FUTURE_SCOPE_DECLARATION_OPERATION_CREATED_TRUE",
    "candidate_specific_distinctness_basis_emission_operation_rerun": "BASIS_EMISSION_OPERATION_RERUN_TRUE",
    "scan_allowed": "SCAN_ALLOWED_TRUE",
    "repair_allowed": "REPAIR_ALLOWED_TRUE",
    "validation_enforcement_allowed": "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
    "standing_authorized": "STANDING_AUTHORIZED_TRUE",
    "crossing_authorized": "CROSSING_AUTHORIZED_TRUE",
    "relation_authorized": "RELATION_AUTHORIZED_TRUE",
    "field_machinery_authorized": "FIELD_MACHINERY_AUTHORIZED_TRUE",
    "follow_on_authorized": "FOLLOW_ON_AUTHORIZED_TRUE",
    "follow_on_work_authorized": "FOLLOW_ON_AUTHORIZED_TRUE",
    "prior_unsupported_candidate_a_claim_validated": "PRIOR_UNSUPPORTED_CANDIDATE_A_CLAIM_VALIDATED",
    "prior_unsupported_candidate_b_claim_validated": "PRIOR_UNSUPPORTED_CANDIDATE_B_CLAIM_VALIDATED",
    "prior_unsupported_derivation_event_claim_validated": "PRIOR_UNSUPPORTED_DERIVATION_EVENT_CLAIM_VALIDATED",
    "valid_derivation_event_recorded": "VALID_DERIVATION_EVENT_RECORDED",
    "affected_file_repaired": "AFFECTED_FILE_REPAIRED",
    "affected_file_edited": "AFFECTED_FILE_EDITED",
    "affected_file_deleted": "AFFECTED_FILE_DELETED",
    "affected_file_overwritten": "AFFECTED_FILE_OVERWRITTEN",
    "affected_file_replaced": "AFFECTED_FILE_REPLACED",
    "affected_file_redeemed": "AFFECTED_FILE_REDEEMED",
    "affected_file_treated_as_clean_basis": "AFFECTED_FILE_TREATED_AS_CLEAN_BASIS",
    "contaminated_lineage_treated_as_clean_basis": "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS",
    "existence_claim_evidence_check_overridden": "EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDDEN",
    "existence_claim_evidence_check_bypassed": "EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASSED",
    "differentiation_operation_overridden": "DIFFERENTIATION_OPERATION_OVERRIDDEN",
    "differentiation_operation_bypassed": "DIFFERENTIATION_OPERATION_BYPASSED",
    "distinctness_operation_boundary_overridden": "DISTINCTNESS_OPERATION_BOUNDARY_OVERRIDDEN",
    "distinctness_operation_boundary_bypassed": "DISTINCTNESS_OPERATION_BOUNDARY_BYPASSED",
    "distinctness_operation_overridden": "DISTINCTNESS_OPERATION_OVERRIDDEN",
    "distinctness_operation_bypassed": "DISTINCTNESS_OPERATION_BYPASSED",
    "candidate_specific_distinctness_basis_emission_boundary_overridden": "BASIS_EMISSION_BOUNDARY_OVERRIDDEN",
    "candidate_specific_distinctness_basis_emission_boundary_bypassed": "BASIS_EMISSION_BOUNDARY_BYPASSED",
    "candidate_specific_distinctness_basis_emission_operation_overridden": "BASIS_EMISSION_OPERATION_OVERRIDDEN",
    "candidate_specific_distinctness_basis_emission_operation_bypassed": "BASIS_EMISSION_OPERATION_BYPASSED",
    "scan_performed": "SCAN_PERFORMED",
    "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
    "repair_performed": "REPAIR_PERFORMED",
    "validation_enforced": "VALIDATION_ENFORCED",
    "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
    "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
}

for _false_key in REQUIRED_FALSE_NON_CLAIMS:
    TOP_LEVEL_FALSE_FIELD_CODES.setdefault(_false_key, f"{_false_key.upper()}_TRUE")

BLOCK_CODES = tuple(
    dict.fromkeys(
        (
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_QUESTION_UNDECLARED",
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_INTENT_UNSUPPORTED",
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_BLOCK_REQUESTED",
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_TYPE_MISSING",
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_TYPE_NOT_EXPECTED",
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_VERSION_MISSING",
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_VERSION_NOT_0_1_0",
            "FUTURE_DECLARATION_OPERATION_TYPE_MISSING",
            "FUTURE_DECLARATION_OPERATION_TYPE_NOT_EXPECTED",
            "RUPTURE_CLASS_BLOCKED_MISSING",
            "RUPTURE_CLASS_BLOCKED_NOT_EXPECTED",
            "BOUNDARY_SPEC_REFERENCE_MISSING",
            "COMPLETED_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "COMPLETED_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "UPSTREAM_EMISSION_OPERATION_RESULT_NOT_REQUIRES_ADDITIONAL_BASIS",
            "REQUIRES_ADDITIONAL_BASIS_NOT_PRESERVED_AS_CLEAN_RESULT",
            "CANDIDATE_A_SCOPE_MISSING_UPSTREAM_NOT_TRUE",
            "CANDIDATE_B_SCOPE_MISSING_UPSTREAM_NOT_TRUE",
            "BASIS_BEARING_SCOPE_DIVISION_MISSING_UPSTREAM_NOT_TRUE",
            "FUTURE_SCOPE_DECLARATION_OPERATION_SHAPE_NOT_ALLOWED",
            "SCOPE_LABEL_LAUNDERING_TREATED_AS_BASIS_TRUE",
            "COSMETIC_SCOPE_NAMING_TREATED_AS_BASIS_TRUE",
            "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_SCOPE_BASIS_TRUE",
            "SHARED_EVIDENCE_TREATED_AS_SCOPE_BASIS_TRUE",
            "OPERATION_EVIDENCE_ALONE_TREATED_AS_SCOPE_BASIS_TRUE",
            "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_SCOPE_BASIS_TRUE",
            "FUTURE_SCOPE_DECLARATION_OPERATION_CREATED_TRUE",
            "CANDIDATE_A_SCOPE_DECLARED_TRUE",
            "CANDIDATE_B_SCOPE_DECLARED_TRUE",
            "BASIS_BEARING_SCOPE_DIVISION_DECLARED_TRUE",
            "CANDIDATE_SPECIFIC_CONTENT_EMITTED_TRUE",
            "SEPARATE_SEAL_MATERIAL_EMITTED_TRUE",
            "SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMITTED_TRUE",
            "SEPARATE_DIGEST_MATERIAL_EMITTED_TRUE",
            "BASIS_EMISSION_OPERATION_RERUN_TRUE",
            "DISTINCTNESS_OPERATION_RERUN_TRUE",
            "DISTINCTNESS_SUPPORTED_RECORDED_TRUE",
            "CANDIDATE_RECORDS_MARKED_DISTINCT_TRUE",
            "SCAN_ALLOWED_TRUE",
            "REPAIR_ALLOWED_TRUE",
            "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
            "CANDIDATE_STANDING_AUTHORIZED_TRUE",
            "DESCENDANT_BODY_CREATED_TRUE",
            "STANDING_AUTHORIZED_TRUE",
            "CROSSING_AUTHORIZED_TRUE",
            "RELATION_AUTHORIZED_TRUE",
            "FIELD_MACHINERY_AUTHORIZED_TRUE",
            "RUNTIME_CREATED_TRUE",
            "API_CREATED_TRUE",
            "CURRENTNESS_CREATED_TRUE",
            "AUTHORITY_CREATED_TRUE",
            "STANDING_CREATED_TRUE",
            "OUTPUT_AUTHORIZED_TRUE",
            "ACTION_AUTHORIZED_TRUE",
            "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE",
            "SYNCHRONIZATION_AUTHORIZED_TRUE",
            "FOLLOW_ON_AUTHORIZED_TRUE",
            "CANDIDATE_STANDING_AUTHORIZED",
            "DESCENDANT_BODY_CREATED",
            "STANDING_AUTHORIZED",
            "CROSSING_AUTHORIZED",
            "RELATION_AUTHORIZED",
            "FIELD_MACHINERY_AUTHORIZED",
            "RUNTIME_CREATED",
            "API_CREATED",
            "CURRENTNESS_CREATED",
            "AUTHORITY_CREATED",
            "STANDING_CREATED",
            "OUTPUT_AUTHORIZED",
            "ACTION_AUTHORIZED",
            "DERIVATIVE_RECEPTION_AUTHORIZED",
            "SYNCHRONIZATION_AUTHORIZED",
            "FOLLOW_ON_AUTHORIZED",
            "PRIOR_UNSUPPORTED_CANDIDATE_A_CLAIM_VALIDATED",
            "PRIOR_UNSUPPORTED_CANDIDATE_B_CLAIM_VALIDATED",
            "PRIOR_UNSUPPORTED_DERIVATION_EVENT_CLAIM_VALIDATED",
            "VALID_DERIVATION_EVENT_RECORDED",
            "AFFECTED_FILE_REPAIRED",
            "AFFECTED_FILE_EDITED",
            "AFFECTED_FILE_DELETED",
            "AFFECTED_FILE_OVERWRITTEN",
            "AFFECTED_FILE_REPLACED",
            "AFFECTED_FILE_REDEEMED",
            "AFFECTED_FILE_TREATED_AS_CLEAN_BASIS",
            "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDDEN",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASSED",
            "DIFFERENTIATION_OPERATION_OVERRIDDEN",
            "DIFFERENTIATION_OPERATION_BYPASSED",
            "DISTINCTNESS_OPERATION_BOUNDARY_OVERRIDDEN",
            "DISTINCTNESS_OPERATION_BOUNDARY_BYPASSED",
            "DISTINCTNESS_OPERATION_OVERRIDDEN",
            "DISTINCTNESS_OPERATION_BYPASSED",
            "BASIS_EMISSION_BOUNDARY_OVERRIDDEN",
            "BASIS_EMISSION_BOUNDARY_BYPASSED",
            "BASIS_EMISSION_OPERATION_OVERRIDDEN",
            "BASIS_EMISSION_OPERATION_BYPASSED",
            "SCAN_PERFORMED",
            "REPOSITORY_SCAN_PERFORMED",
            "REPAIR_PERFORMED",
            "VALIDATION_ENFORCED",
            "HIDDEN_REPAIR_PERFORMED",
            "SILENT_OVERWRITE_PERFORMED",
            "SCOPE_LABEL_LAUNDERING_TREATED_AS_BASIS",
            "COSMETIC_SCOPE_NAMING_TREATED_AS_BASIS",
            "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_SCOPE_BASIS",
            "SHARED_EVIDENCE_TREATED_AS_SCOPE_BASIS",
            "OPERATION_EVIDENCE_ALONE_TREATED_AS_SCOPE_BASIS",
            "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_SCOPE_BASIS",
            "BOUNDARY_SPEC_MARKER_MISSING",
            "COMPLETED_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "DECLARED_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_REQUEST_MALFORMED",
            "DECLARED_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_REQUEST_UNREADABLE",
            *REQUESTED_ACTION_FIELD_CODES.values(),
            *TOP_LEVEL_FALSE_FIELD_CODES.values(),
        )
    )
)

SENSITIVE_KEY_FRAGMENTS = (
    "raw_body",
    "full_body",
    "markdown_body",
    "hidden_repo_state",
    "local_cache",
    "current_working_tree",
)

FORBIDDEN_OUTPUT_ROOT_PARTS = (
    "integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_operation",
    "integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_boundary",
    "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation",
    "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_boundary",
    "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation",
    "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_boundary",
    "integrity_host_v0_min_coexistence_existence_claim_evidence_check",
    "integrity_host_v0_min_coexistence_existence_claim_evidence_requirement_boundary",
    "integrity_host_v0_min_coexistence_descendant_body_basis",
    "integrity_host_v0_min_coexistence_seam_case",
    "integrity_host_v0_min_coexistence_local_relevance_medium",
    "integrity_host_v0_min_coexistence_source_transfer",
    "integrity_host_v0_min_coexistence_source_receipt",
    "integrity_host_v0_min_coexistence_public_api",
    "integrity_host_v0_min_coexistence_participant_facing_interface",
    "integrity_host_v0_min_coexistence_distributed_network",
    "integrity_host_v0_min_coexistence_runtime_hosting",
    "integrity_host_v0_min_coexistence_runtime_loop",
    "integrity_host_v0_min_coexistence_daemon",
)


def _marker_groups(*markers: str | tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    groups: list[tuple[str, ...]] = []
    for marker in markers:
        if isinstance(marker, tuple):
            groups.append(marker)
        else:
            groups.append((marker,))
    return tuple(groups)


BOUNDARY_SPEC_MARKERS = _marker_groups(
    "Descendant Body Candidate Non-Cosmetic Scope Division Declaration Boundary V0 Minimum Specification",
    "This file defines one boundary for a future candidate non-cosmetic scope-division declaration operation.",
    "This file is boundary-only.",
    "This file does not define, implement, or perform the future declaration operation.",
    "This file does not declare candidate A scope, candidate B scope, or basis-bearing scope division.",
    "This boundary exists to prevent a future scope declaration operation from laundering labels into scope division.",
    "Scope declaration is not scope standing.",
    "Scope declaration is not candidate-specific basis emission.",
    "Scope declaration is not distinctness support.",
    "A scope label is not a scope.",
    "A scope title is not a mandate.",
    "A scope id is not a governed surface.",
    "Scope division must be basis-bearing, not label-bearing.",
    "Candidate-specific basis must be basis-bearing, not label-bearing.",
    "For the immediate next repo-local step, this boundary permits only a future non-cosmetic scope-division declaration operation shape to be defined.",
    "candidate_a_scope_declared = false",
    "candidate_b_scope_declared = false",
    "basis_bearing_scope_division_declared = false",
    "scope_label_laundering_treated_as_basis = false",
    "cosmetic_scope_naming_treated_as_basis = false",
    "id_role_label_difference_treated_as_scope_basis = false",
    "shared_evidence_treated_as_scope_basis = false",
    "operation_evidence_alone_treated_as_scope_basis = false",
    "contaminated_lineage_treated_as_clean_scope_basis = false",
)

BASIS_EMISSION_OPERATION_MARKERS = _marker_groups(
    "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
    "REQUIRES_ADDITIONAL_BASIS",
    ("failed_check_count = 0", "failed_check_count 0"),
    "missing non-cosmetic candidate A scope",
    "missing non-cosmetic candidate B scope",
    "missing basis-bearing scope division",
    "material_emitted = false",
    "candidate_specific_content_emitted = false",
    "separate_seal_material_emitted = false",
    "separate_lineage_receipt_material_emitted = false",
    "separate_digest_material_emitted = false",
    "distinctness_operation_rerun = false",
    "distinctness_supported_recorded = false",
    "candidate_records_marked_distinct = false",
    "candidate_standing_authorized = false",
    "descendant_body_created = false",
)

BASIS_EMISSION_BOUNDARY_MARKERS = _marker_groups(
    "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_RECORDED",
    "SCOPE_DIVISION_ONLY",
    (
        "scope division is the only immediate admissible future repo-local route",
        "The boundary allowed only future scope-division operation shape",
        "scope_division_route_allowed_for_future_operation_shape = true",
    ),
    ("scope division route allowed", "scope_division_route_allowed"),
    (
        "Candidate-specific basis must be basis-bearing, not label-bearing",
        "candidate_specific_content_basis_bearing",
    ),
    (
        "Digest difference is not distinctness unless the digested material carries non-cosmetic candidate-specific basis",
        "digest_laundering_not_allowed = true",
    ),
)

DISTINCTNESS_OPERATION_MARKERS = _marker_groups(
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
    "distinctness_result = NOT_DISTINCT",
    "failed_check_count = 0",
    "candidate_record_count_compared = 2",
    "distinctness_supported = false",
    "NOT_DISTINCT is a clean operation result, not a failure",
    "id and role difference alone is not distinctness",
    "shared evidence reference alone is not distinctness",
    "Operation evidence alone is not distinctness",
)

DIFFERENTIATION_OPERATION_MARKERS = _marker_groups(
    (
        "Descendant Body Differentiation Operation Terminal Summary V0",
        "completed descendant-body differentiation operation line",
    ),
    ("exactly two candidate records emitted", "candidate_record_count_emitted = 2"),
    ("candidate records are non-standing", "candidate_records_non_standing = true"),
    ("candidate records are not descendant bodies", "not descendant bodies"),
    ("descendant bodies were not created", "descendant_bodies_not_created = true"),
    (
        "standing descendants were not created",
        "standing_descendants_not_created = true",
    ),
    ("crossing was not authorized", "crossing_authorized = false"),
    ("relation was not created", "relation_authorized = false"),
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _repo_path(path_value: Path | str) -> Path:
    path = Path(path_value)
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def _safe_string(value: Any, *, max_length: int = 1000) -> str:
    if value is None:
        return ""
    text = str(value)
    lowered = text.lower()
    if any(fragment in lowered for fragment in SENSITIVE_KEY_FRAGMENTS):
        return "[redacted-sensitive-content]"
    if len(text) > max_length:
        return text[:max_length] + "...[truncated]"
    return text


def _safe_value(value: Any) -> Any:
    if isinstance(value, (bool, int, float)) or value is None:
        return value
    if isinstance(value, str):
        return _safe_string(value)
    if isinstance(value, Path):
        return _safe_string(value.as_posix())
    if isinstance(value, Mapping):
        safe: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text.endswith("_body") or any(
                fragment in key_text.lower() for fragment in SENSITIVE_KEY_FRAGMENTS
            ):
                safe[key_text] = "[redacted-sensitive-content]"
            else:
                safe[key_text] = _safe_value(item)
        return safe
    if isinstance(value, (list, tuple)):
        return [_safe_value(item) for item in value[:20]]
    return _safe_string(value)


def _safe_filename(value: str) -> str:
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in value)
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe.strip("._-") or DEFAULT_BOUNDARY_ID


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    code = None if passed else block_code
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _safe_value(expected_posture),
        "actual_posture": _safe_value(actual_posture),
        "block_code": code,
        "failure_code": code,
    }


def _first_block_code(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code:
                return code
    return None


def _passed_failed_counts(checks: list[dict[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _contains_marker_group(text: str, group: tuple[str, ...]) -> bool:
    haystack = text.lower()
    return any(marker.lower() in haystack for marker in group)


def _read_declared_text(reference: Any) -> tuple[str, bool]:
    if not isinstance(reference, str) or not reference.strip():
        return "", False
    path = _repo_path(reference)
    try:
        return path.read_text(encoding="utf-8"), True
    except OSError:
        return "", False


def _markers_present(reference: Any, marker_groups: tuple[tuple[str, ...], ...]) -> dict[str, Any]:
    text, readable = _read_declared_text(reference)
    present_count = 0
    if readable:
        present_count = sum(1 for group in marker_groups if _contains_marker_group(text, group))
    return {
        "reference": _safe_string(reference),
        "readable": readable,
        "required_marker_count": len(marker_groups),
        "present_marker_count": present_count,
        "markers_present": readable and present_count == len(marker_groups),
    }


def _result_level_non_claims_canonical_false(non_claims: Mapping[str, Any]) -> bool:
    return all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build the default declared request for the current repo-local boundary."""

    request: dict[str, Any] = {
        "candidate_non_cosmetic_scope_division_declaration_boundary_id": DEFAULT_BOUNDARY_ID,
        "candidate_non_cosmetic_scope_division_declaration_boundary_question": CORE_BOUNDARY_QUESTION,
        "candidate_non_cosmetic_scope_division_declaration_boundary_intent": INTENT_RECORD,
        "candidate_non_cosmetic_scope_division_declaration_boundary_type": BOUNDARY_TYPE,
        "candidate_non_cosmetic_scope_division_declaration_boundary_version": BOUNDARY_VERSION,
        "future_scope_declaration_operation_type": FUTURE_DECLARATION_OPERATION_TYPE,
        "rupture_class_blocked": RUPTURE_CLASS_BLOCKED,
        "boundary_spec_reference": DEFAULT_BOUNDARY_SPEC_REFERENCE,
        "completed_basis_emission_operation_terminal_summary_reference": DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "completed_basis_emission_boundary_terminal_summary_reference": DEFAULT_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "completed_distinctness_operation_terminal_summary_reference": DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "completed_differentiation_operation_terminal_summary_reference": DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "upstream_emission_operation_result": UPSTREAM_EMISSION_OPERATION_RESULT,
        "requires_additional_basis_preserved_as_clean_result": True,
        "candidate_a_scope_missing_upstream": True,
        "candidate_b_scope_missing_upstream": True,
        "basis_bearing_scope_division_missing_upstream": True,
        "future_scope_declaration_operation_shape_allowed": True,
        "scope_label_laundering_treated_as_basis": False,
        "cosmetic_scope_naming_treated_as_basis": False,
        "id_role_label_difference_treated_as_scope_basis": False,
        "shared_evidence_treated_as_scope_basis": False,
        "operation_evidence_alone_treated_as_scope_basis": False,
        "contaminated_lineage_treated_as_clean_scope_basis": False,
        "future_scope_declaration_operation_created": False,
        "candidate_a_scope_declared": False,
        "candidate_b_scope_declared": False,
        "basis_bearing_scope_division_declared": False,
        "candidate_specific_content_emitted": False,
        "separate_seal_material_emitted": False,
        "separate_lineage_receipt_material_emitted": False,
        "separate_digest_material_emitted": False,
        "candidate_specific_distinctness_basis_emission_operation_rerun": False,
        "candidate_specific_distinctness_basis_emission_operation_recorded": False,
        "distinctness_operation_rerun": False,
        "distinctness_supported_recorded": False,
        "candidate_records_marked_distinct": False,
        "candidate_records_distinct": False,
        "candidate_standing_authorized": False,
        "candidate_standing_created": False,
        "descendant_body_a_created": False,
        "descendant_body_b_created": False,
        "descendant_body_created": False,
        "standing_descendant_created": False,
        "descendant_standing_check_performed": False,
        "standing_authorized": False,
        "crossing_authorized": False,
        "relation_authorized": False,
        "field_machinery_authorized": False,
        "runtime_created": False,
        "api_created": False,
        "currentness_created": False,
        "authority_created": False,
        "standing_created": False,
        "output_authorized": False,
        "action_authorized": False,
        "derivative_reception_authorized": False,
        "synchronization_authorized": False,
        "follow_on_authorized": False,
        "follow_on_work_authorized": False,
        "scan_allowed": False,
        "repair_allowed": False,
        "validation_enforcement_allowed": False,
        "declared_non_claims": _canonical_non_claims(),
    }
    for key in REQUIRED_FALSE_NON_CLAIMS:
        request.setdefault(key, False)
    request.update(overrides)
    return request


def _append_required_value_checks(
    declared: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    question = declared.get("candidate_non_cosmetic_scope_division_declaration_boundary_question")
    checks.append(
        _check(
            "boundary question declared",
            isinstance(question, str) and bool(question.strip()),
            "non-empty boundary question",
            question,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_QUESTION_UNDECLARED",
        )
    )

    intent = declared.get("candidate_non_cosmetic_scope_division_declaration_boundary_intent")
    checks.append(
        _check(
            "boundary intent supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "boundary block intent not requested",
            intent != INTENT_BLOCK,
            f"not {INTENT_BLOCK}",
            intent,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_BLOCK_REQUESTED",
        )
    )

    boundary_type = declared.get("candidate_non_cosmetic_scope_division_declaration_boundary_type")
    checks.append(
        _check(
            "boundary type declared",
            boundary_type is not None,
            BOUNDARY_TYPE,
            boundary_type,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_TYPE_MISSING",
        )
    )
    checks.append(
        _check(
            "boundary type exact",
            boundary_type == BOUNDARY_TYPE,
            BOUNDARY_TYPE,
            boundary_type,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_TYPE_NOT_EXPECTED",
        )
    )

    boundary_version = declared.get(
        "candidate_non_cosmetic_scope_division_declaration_boundary_version"
    )
    checks.append(
        _check(
            "boundary version declared",
            boundary_version is not None,
            BOUNDARY_VERSION,
            boundary_version,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_VERSION_MISSING",
        )
    )
    checks.append(
        _check(
            "boundary version exact",
            boundary_version == BOUNDARY_VERSION,
            BOUNDARY_VERSION,
            boundary_version,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_VERSION_NOT_0_1_0",
        )
    )

    future_type = declared.get("future_scope_declaration_operation_type")
    checks.append(
        _check(
            "future declaration operation type declared",
            future_type is not None,
            FUTURE_DECLARATION_OPERATION_TYPE,
            future_type,
            "FUTURE_DECLARATION_OPERATION_TYPE_MISSING",
        )
    )
    checks.append(
        _check(
            "future declaration operation type exact",
            future_type == FUTURE_DECLARATION_OPERATION_TYPE,
            FUTURE_DECLARATION_OPERATION_TYPE,
            future_type,
            "FUTURE_DECLARATION_OPERATION_TYPE_NOT_EXPECTED",
        )
    )

    rupture_class = declared.get("rupture_class_blocked")
    checks.append(
        _check(
            "rupture class blocked declared",
            rupture_class is not None,
            RUPTURE_CLASS_BLOCKED,
            rupture_class,
            "RUPTURE_CLASS_BLOCKED_MISSING",
        )
    )
    checks.append(
        _check(
            "rupture class blocked exact",
            rupture_class == RUPTURE_CLASS_BLOCKED,
            RUPTURE_CLASS_BLOCKED,
            rupture_class,
            "RUPTURE_CLASS_BLOCKED_NOT_EXPECTED",
        )
    )

    reference_checks = (
        ("boundary_spec_reference", "BOUNDARY_SPEC_REFERENCE_MISSING"),
        (
            "completed_basis_emission_operation_terminal_summary_reference",
            "COMPLETED_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        ),
        (
            "completed_basis_emission_boundary_terminal_summary_reference",
            "COMPLETED_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        ),
        (
            "completed_distinctness_operation_terminal_summary_reference",
            "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        ),
        (
            "completed_differentiation_operation_terminal_summary_reference",
            "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        ),
    )
    for field, code in reference_checks:
        value = declared.get(field)
        checks.append(
            _check(
                field.replace("_", " ") + " declared",
                isinstance(value, str) and bool(value.strip()),
                "declared Markdown reference path",
                value,
                code,
            )
        )


def _append_positive_basis_checks(
    declared: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    positive_checks = (
        (
            "upstream emission operation result is REQUIRES_ADDITIONAL_BASIS",
            "upstream_emission_operation_result",
            UPSTREAM_EMISSION_OPERATION_RESULT,
            "UPSTREAM_EMISSION_OPERATION_RESULT_NOT_REQUIRES_ADDITIONAL_BASIS",
        ),
        (
            "REQUIRES_ADDITIONAL_BASIS preserved as clean result",
            "requires_additional_basis_preserved_as_clean_result",
            True,
            "REQUIRES_ADDITIONAL_BASIS_NOT_PRESERVED_AS_CLEAN_RESULT",
        ),
        (
            "candidate A scope missing upstream true",
            "candidate_a_scope_missing_upstream",
            True,
            "CANDIDATE_A_SCOPE_MISSING_UPSTREAM_NOT_TRUE",
        ),
        (
            "candidate B scope missing upstream true",
            "candidate_b_scope_missing_upstream",
            True,
            "CANDIDATE_B_SCOPE_MISSING_UPSTREAM_NOT_TRUE",
        ),
        (
            "basis-bearing scope division missing upstream true",
            "basis_bearing_scope_division_missing_upstream",
            True,
            "BASIS_BEARING_SCOPE_DIVISION_MISSING_UPSTREAM_NOT_TRUE",
        ),
        (
            "future scope declaration operation shape allowed true",
            "future_scope_declaration_operation_shape_allowed",
            True,
            "FUTURE_SCOPE_DECLARATION_OPERATION_SHAPE_NOT_ALLOWED",
        ),
    )
    for name, field, expected, code in positive_checks:
        actual = declared.get(field)
        checks.append(_check(name, actual == expected, expected, actual, code))


def _append_false_posture_checks(
    declared: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    for field, code in TOP_LEVEL_FALSE_FIELD_CODES.items():
        actual = declared.get(field, False)
        checks.append(
            _check(
                field.replace("_", " ") + " false",
                actual is False,
                False,
                actual,
                code,
            )
        )

    for field, code in REQUESTED_ACTION_FIELD_CODES.items():
        actual = declared.get(field, False)
        checks.append(
            _check(
                field.replace("_", " ") + " not requested",
                actual is not True,
                False,
                actual,
                code,
            )
        )


def _append_non_claim_checks(
    declared: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    declared_non_claims = declared.get("declared_non_claims")
    invalid_keys: list[str] = []
    if not isinstance(declared_non_claims, Mapping):
        invalid_keys = list(REQUIRED_FALSE_NON_CLAIMS)
    else:
        for key in REQUIRED_FALSE_NON_CLAIMS:
            if declared_non_claims.get(key) is not False:
                invalid_keys.append(key)

    checks.append(
        _check(
            "required non-claims false",
            not invalid_keys,
            "all required declared non-claims present as bool false",
            invalid_keys,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )


def _basis_marker_summaries(
    declared: Mapping[str, Any], checks: list[dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    marker_specs = {
        "boundary_spec": (
            "boundary_spec_reference",
            BOUNDARY_SPEC_MARKERS,
            "boundary spec markers present",
            "BOUNDARY_SPEC_MARKER_MISSING",
        ),
        "completed_basis_emission_operation_terminal_summary": (
            "completed_basis_emission_operation_terminal_summary_reference",
            BASIS_EMISSION_OPERATION_MARKERS,
            "completed basis emission operation terminal summary markers present",
            "COMPLETED_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ),
        "completed_basis_emission_boundary_terminal_summary": (
            "completed_basis_emission_boundary_terminal_summary_reference",
            BASIS_EMISSION_BOUNDARY_MARKERS,
            "completed basis emission boundary terminal summary markers present",
            "COMPLETED_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        ),
        "completed_distinctness_operation_terminal_summary": (
            "completed_distinctness_operation_terminal_summary_reference",
            DISTINCTNESS_OPERATION_MARKERS,
            "completed distinctness operation terminal summary markers present",
            "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ),
        "completed_differentiation_operation_terminal_summary": (
            "completed_differentiation_operation_terminal_summary_reference",
            DIFFERENTIATION_OPERATION_MARKERS,
            "completed differentiation operation terminal summary markers present",
            "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ),
    }

    summaries: dict[str, dict[str, Any]] = {}
    for summary_key, (field, marker_groups, check_name, code) in marker_specs.items():
        summary = _markers_present(declared.get(field), marker_groups)
        summaries[summary_key] = summary
        checks.append(
            _check(
                check_name,
                summary["markers_present"] is True,
                "all required markers present",
                {
                    "reference": summary["reference"],
                    "readable": summary["readable"],
                    "present_marker_count": summary["present_marker_count"],
                    "required_marker_count": summary["required_marker_count"],
                },
                code,
            )
        )
    return summaries


def _make_boundary_object(
    declared: Mapping[str, Any],
    *,
    recorded: bool,
    marker_summaries: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    return {
        "candidate_non_cosmetic_scope_division_declaration_boundary_id": _safe_string(
            declared.get(
                "candidate_non_cosmetic_scope_division_declaration_boundary_id",
                DEFAULT_BOUNDARY_ID,
            )
            or DEFAULT_BOUNDARY_ID
        ),
        "candidate_non_cosmetic_scope_division_declaration_boundary_type": _safe_string(
            declared.get("candidate_non_cosmetic_scope_division_declaration_boundary_type")
            or BOUNDARY_TYPE
        ),
        "candidate_non_cosmetic_scope_division_declaration_boundary_version": _safe_string(
            declared.get("candidate_non_cosmetic_scope_division_declaration_boundary_version")
            or BOUNDARY_VERSION
        ),
        "future_scope_declaration_operation_type": _safe_string(
            declared.get("future_scope_declaration_operation_type")
            or FUTURE_DECLARATION_OPERATION_TYPE
        ),
        "rupture_class_blocked": _safe_string(
            declared.get("rupture_class_blocked") or RUPTURE_CLASS_BLOCKED
        ),
        "upstream_emission_operation_result": _safe_string(
            declared.get("upstream_emission_operation_result")
            or UPSTREAM_EMISSION_OPERATION_RESULT
        ),
        "candidate_non_cosmetic_scope_division_declaration_boundary_recorded": recorded,
        "boundary_created": recorded,
        "upstream_emission_operation_result_is_requires_additional_basis": declared.get(
            "upstream_emission_operation_result"
        )
        == UPSTREAM_EMISSION_OPERATION_RESULT,
        "requires_additional_basis_preserved_as_clean_result": declared.get(
            "requires_additional_basis_preserved_as_clean_result"
        )
        is True,
        "candidate_a_scope_missing_upstream": declared.get("candidate_a_scope_missing_upstream")
        is True,
        "candidate_b_scope_missing_upstream": declared.get("candidate_b_scope_missing_upstream")
        is True,
        "basis_bearing_scope_division_missing_upstream": declared.get(
            "basis_bearing_scope_division_missing_upstream"
        )
        is True,
        "future_scope_declaration_operation_shape_allowed": declared.get(
            "future_scope_declaration_operation_shape_allowed"
        )
        is True,
        "scope_label_laundering_not_allowed": True,
        "cosmetic_scope_naming_not_allowed": True,
        "id_role_label_difference_not_allowed_as_scope_basis": True,
        "shared_evidence_not_allowed_as_scope_basis": True,
        "operation_evidence_alone_not_allowed_as_scope_basis": True,
        "contaminated_lineage_not_allowed_as_clean_scope_basis": True,
        "future_scope_declaration_operation_not_created": True,
        "candidate_a_scope_not_declared": True,
        "candidate_b_scope_not_declared": True,
        "basis_bearing_scope_division_not_declared": True,
        "candidate_specific_content_not_emitted": True,
        "separate_seal_material_not_emitted": True,
        "separate_lineage_receipt_material_not_emitted": True,
        "separate_digest_material_not_emitted": True,
        "emission_operation_not_rerun": True,
        "distinctness_operation_not_rerun": True,
        "distinctness_supported_not_recorded": True,
        "candidate_records_not_marked_distinct": True,
        "candidate_standing_not_authorized": True,
        "descendant_bodies_not_created": True,
        "standing_descendants_not_created": True,
        "first_crossing_not_authorized": True,
        "relation_not_created": True,
        "field_machinery_not_created": True,
        "runtime_not_created": True,
        "api_not_created": True,
        "currentness_not_created": True,
        "authority_not_created": True,
        "standing_not_created": True,
        "output_not_authorized": True,
        "action_not_authorized": True,
        "derivative_reception_not_authorized": True,
        "synchronization_not_authorized": True,
        "follow_on_not_authorized": True,
        "prior_unsupported_claims_not_validated": True,
        "affected_file_not_repaired": True,
        "affected_file_not_treated_as_clean_basis": True,
        "contaminated_lineage_not_treated_as_clean_basis": True,
        "existence_claim_evidence_check_not_overridden": True,
        "existence_claim_evidence_check_not_bypassed": True,
        "differentiation_operation_not_overridden": True,
        "differentiation_operation_not_bypassed": True,
        "distinctness_operation_boundary_not_overridden": True,
        "distinctness_operation_boundary_not_bypassed": True,
        "distinctness_operation_not_overridden": True,
        "distinctness_operation_not_bypassed": True,
        "basis_emission_boundary_not_overridden": True,
        "basis_emission_boundary_not_bypassed": True,
        "basis_emission_operation_not_overridden": True,
        "basis_emission_operation_not_bypassed": True,
        "scan_not_performed": True,
        "repository_scan_not_performed": True,
        "repair_not_performed": True,
        "validation_not_enforced": True,
        "hidden_repair_not_performed": True,
        "silent_overwrite_not_performed": True,
        "boundary_spec_markers_present": bool(
            marker_summaries.get("boundary_spec", {}).get("markers_present")
        ),
        "completed_basis_emission_operation_terminal_summary_markers_present": bool(
            marker_summaries.get(
                "completed_basis_emission_operation_terminal_summary", {}
            ).get("markers_present")
        ),
        "completed_basis_emission_boundary_terminal_summary_markers_present": bool(
            marker_summaries.get(
                "completed_basis_emission_boundary_terminal_summary", {}
            ).get("markers_present")
        ),
        "completed_distinctness_operation_terminal_summary_markers_present": bool(
            marker_summaries.get(
                "completed_distinctness_operation_terminal_summary", {}
            ).get("markers_present")
        ),
        "completed_differentiation_operation_terminal_summary_markers_present": bool(
            marker_summaries.get(
                "completed_differentiation_operation_terminal_summary", {}
            ).get("markers_present")
        ),
    }


def _open_items() -> list[str]:
    return [
        "candidate non-cosmetic scope-division declaration operation spec",
        "candidate non-cosmetic scope-division declaration resolver",
        "candidate non-cosmetic scope-division declaration test",
        "candidate non-cosmetic scope-division declaration artifact",
        "candidate non-cosmetic scope-division declaration terminal summary",
        "actual non-cosmetic candidate A scope declaration",
        "actual non-cosmetic candidate B scope declaration",
        "actual basis-bearing scope division declaration",
        "candidate-specific distinctness basis emission operation successor, if separately bounded",
        "actual candidate-specific content emission",
        "actual separate seal material emission",
        "actual separate lineage receipt material emission",
        "actual separate digest material emission",
        "future distinctness-supported operation result, if separately supported",
        "divergent receipt-history route, if separately bounded",
        "carrier separation route, if separately bounded",
        "candidate-record standing checks",
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
        "repair or successor handling of the affected file, if ever separately bounded",
        "prose-shaped existence-claim handling, if ever separately bounded",
        "automated repository scan, if ever separately bounded",
        "contribution/provenance trace handling, if ever separately bounded",
        "follow-on work",
    ]


def _finalize_result(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
    marker_summaries: Mapping[str, Mapping[str, Any]],
    *,
    outcome_override: str | None = None,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    checks.append(
        _check(
            "result-level required false non-claims canonical false",
            _result_level_non_claims_canonical_false(non_claims),
            "all result-level required non-claims false",
            "canonical false",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )

    first_code = _first_block_code(checks)
    intent = declared.get("candidate_non_cosmetic_scope_division_declaration_boundary_intent")
    if outcome_override is not None:
        outcome = outcome_override
    elif first_code is not None:
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    else:
        outcome = OUTCOME_RECORDED

    recorded = outcome == OUTCOME_RECORDED
    boundary = _make_boundary_object(declared, recorded=recorded, marker_summaries=marker_summaries)
    passed_count, failed_count = _passed_failed_counts(checks)
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": first_code if outcome == OUTCOME_BLOCKED else None,
        "block_code": first_code if outcome == OUTCOME_BLOCKED else None,
        "reason": first_code if outcome == OUTCOME_BLOCKED else None,
    }

    metadata = {
        "candidate_non_cosmetic_scope_division_declaration_boundary_id": boundary[
            "candidate_non_cosmetic_scope_division_declaration_boundary_id"
        ],
        "boundary_type": BOUNDARY_TYPE,
        "result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
    }

    result: dict[str, Any] = {
        "candidate_non_cosmetic_scope_division_declaration_boundary_metadata": metadata,
        "declared_candidate_non_cosmetic_scope_division_declaration_boundary_question": {
            "question": _safe_string(
                declared.get(
                    "candidate_non_cosmetic_scope_division_declaration_boundary_question",
                    "",
                )
            ),
            "intent": _safe_string(intent),
            "boundary_spec_reference": _safe_string(declared.get("boundary_spec_reference")),
            "completed_basis_emission_operation_terminal_summary_reference": _safe_string(
                declared.get("completed_basis_emission_operation_terminal_summary_reference")
            ),
            "completed_basis_emission_boundary_terminal_summary_reference": _safe_string(
                declared.get("completed_basis_emission_boundary_terminal_summary_reference")
            ),
            "completed_distinctness_operation_terminal_summary_reference": _safe_string(
                declared.get("completed_distinctness_operation_terminal_summary_reference")
            ),
            "completed_differentiation_operation_terminal_summary_reference": _safe_string(
                declared.get("completed_differentiation_operation_terminal_summary_reference")
            ),
        },
        "upstream_basis": {
            "completed_basis_emission_operation_result": _safe_string(
                declared.get("upstream_emission_operation_result")
            ),
            "requires_additional_basis_preserved_as_clean_result": declared.get(
                "requires_additional_basis_preserved_as_clean_result"
            )
            is True,
            "candidate_a_scope_missing_upstream": declared.get(
                "candidate_a_scope_missing_upstream"
            )
            is True,
            "candidate_b_scope_missing_upstream": declared.get(
                "candidate_b_scope_missing_upstream"
            )
            is True,
            "basis_bearing_scope_division_missing_upstream": declared.get(
                "basis_bearing_scope_division_missing_upstream"
            )
            is True,
            "basis_summaries": copy.deepcopy(marker_summaries),
        },
        "candidate_non_cosmetic_scope_division_declaration_boundary_basis": {
            "boundary_spec_reference": _safe_string(declared.get("boundary_spec_reference")),
            "completed_basis_emission_operation_terminal_summary_reference": _safe_string(
                declared.get("completed_basis_emission_operation_terminal_summary_reference")
            ),
            "completed_basis_emission_boundary_terminal_summary_reference": _safe_string(
                declared.get("completed_basis_emission_boundary_terminal_summary_reference")
            ),
            "completed_distinctness_operation_terminal_summary_reference": _safe_string(
                declared.get("completed_distinctness_operation_terminal_summary_reference")
            ),
            "completed_differentiation_operation_terminal_summary_reference": _safe_string(
                declared.get("completed_differentiation_operation_terminal_summary_reference")
            ),
            "raw_markdown_bodies_returned": False,
            "repository_scan_performed": False,
            "file_discovery_performed": False,
        },
        "descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary": boundary,
        "candidate_non_cosmetic_scope_division_declaration_boundary_checks": checks,
        "candidate_non_cosmetic_scope_division_declaration_boundary_statement": {
            "candidate_non_cosmetic_scope_division_declaration_boundary_recorded": recorded,
            "boundary_created": recorded,
            "upstream_emission_operation_result": boundary[
                "upstream_emission_operation_result"
            ],
            "requires_additional_basis_preserved_as_clean_result": boundary[
                "requires_additional_basis_preserved_as_clean_result"
            ],
            "scope_label_laundering_not_allowed": True,
            "cosmetic_scope_naming_not_allowed": True,
            "future_scope_declaration_operation_shape_allowed": boundary[
                "future_scope_declaration_operation_shape_allowed"
            ],
            "candidate_a_scope_not_declared": True,
            "candidate_b_scope_not_declared": True,
            "basis_bearing_scope_division_not_declared": True,
            "candidate_specific_content_not_emitted": True,
            "emission_operation_not_rerun": True,
            "distinctness_operation_not_rerun": True,
            "distinctness_supported_not_recorded": True,
            "candidate_standing_not_authorized": True,
            "descendant_bodies_not_created": True,
            "runtime_not_created": True,
            "authority_not_created": True,
            "follow_on_not_authorized": True,
            "result_level_non_claims_canonical_false": True,
        },
        "candidate_non_cosmetic_scope_division_declaration_boundary_non_meaning": {
            "this_is_not_scope_declaration_operation": True,
            "this_is_not_candidate_a_scope_declaration": True,
            "this_is_not_candidate_b_scope_declaration": True,
            "this_is_not_basis_bearing_scope_division_declaration": True,
            "this_is_not_candidate_specific_content_emission": True,
            "this_is_not_distinctness_support": True,
            "this_is_not_candidate_standing": True,
            "this_is_not_descendant_body_creation": True,
            "this_is_not_runtime": True,
            "this_is_not_authority": True,
            "this_is_not_follow_on_authorization": True,
        },
        "not_recorded_basis": []
        if outcome != OUTCOME_NOT_RECORDED
        else ["declared intent requested boundary not be recorded"],
        "what_remains_open": _open_items(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    result[
        "candidate_non_cosmetic_scope_division_declaration_boundary_summary"
    ] = build_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_summary(
        result
    )
    return result


def resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min(
    declared_candidate_non_cosmetic_scope_division_declaration_boundary: Mapping[str, Any]
    | None = None,
) -> dict[str, Any]:
    """Resolve one boundary result from a declared request mapping."""

    if declared_candidate_non_cosmetic_scope_division_declaration_boundary is None:
        declared: Mapping[str, Any] = (
            build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_request()
        )
    elif not isinstance(
        declared_candidate_non_cosmetic_scope_division_declaration_boundary, Mapping
    ):
        checks = [
            _check(
                "declared boundary request mapping",
                False,
                "mapping request",
                type(declared_candidate_non_cosmetic_scope_division_declaration_boundary).__name__,
                "DECLARED_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result({}, checks, {})
    else:
        declared = copy.deepcopy(
            dict(declared_candidate_non_cosmetic_scope_division_declaration_boundary)
        )

    checks: list[dict[str, Any]] = []
    _append_required_value_checks(declared, checks)
    _append_positive_basis_checks(declared, checks)
    _append_false_posture_checks(declared, checks)
    _append_non_claim_checks(declared, checks)
    marker_summaries = _basis_marker_summaries(declared, checks)
    return _finalize_result(declared, checks, marker_summaries)


def resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_from_path(
    declared_candidate_non_cosmetic_scope_division_declaration_boundary_path: Path | str,
) -> dict[str, Any]:
    """Resolve one boundary result from a JSON request path."""

    path = Path(declared_candidate_non_cosmetic_scope_division_declaration_boundary_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        checks = [
            _check(
                "declared boundary request path readable JSON",
                False,
                "readable JSON object",
                {"path": path.as_posix(), "error": type(exc).__name__},
                "DECLARED_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_REQUEST_UNREADABLE",
            )
        ]
        return _finalize_result({}, checks, {})

    if not isinstance(loaded, Mapping):
        checks = [
            _check(
                "declared boundary request JSON object",
                False,
                "JSON object",
                type(loaded).__name__,
                "DECLARED_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result({}, checks, {})

    return resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min(
        loaded
    )


def build_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary without raw Markdown bodies."""

    checks = result.get("candidate_non_cosmetic_scope_division_declaration_boundary_checks", [])
    if not isinstance(checks, list):
        checks = []
    passed_count, failed_count = _passed_failed_counts(checks)
    boundary_raw = result.get(
        "descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary", {}
    )
    boundary = boundary_raw if isinstance(boundary_raw, Mapping) else {}
    declared_raw = result.get(
        "declared_candidate_non_cosmetic_scope_division_declaration_boundary_question", {}
    )
    declared = declared_raw if isinstance(declared_raw, Mapping) else {}
    metadata_raw = result.get(
        "candidate_non_cosmetic_scope_division_declaration_boundary_metadata", {}
    )
    metadata = metadata_raw if isinstance(metadata_raw, Mapping) else {}
    block_raw = result.get("block")
    block = block_raw if isinstance(block_raw, Mapping) else {}

    return {
        "outcome": _safe_string(result.get("outcome")),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "candidate_non_cosmetic_scope_division_declaration_boundary_id": boundary.get(
            "candidate_non_cosmetic_scope_division_declaration_boundary_id"
        )
        or metadata.get("candidate_non_cosmetic_scope_division_declaration_boundary_id"),
        "question": _safe_string(declared.get("question")),
        "intent": _safe_string(declared.get("intent")),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get("result_version", RESULT_VERSION),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "boundary_type": boundary.get(
            "candidate_non_cosmetic_scope_division_declaration_boundary_type"
        ),
        "boundary_version": boundary.get(
            "candidate_non_cosmetic_scope_division_declaration_boundary_version"
        ),
        "future_declaration_operation_type": boundary.get(
            "future_scope_declaration_operation_type"
        ),
        "rupture_class_blocked": boundary.get("rupture_class_blocked"),
        "upstream_emission_operation_result": boundary.get(
            "upstream_emission_operation_result"
        ),
        "requires_additional_basis_preserved_as_clean_result": boundary.get(
            "requires_additional_basis_preserved_as_clean_result"
        ),
        "candidate_a_scope_missing_upstream": boundary.get(
            "candidate_a_scope_missing_upstream"
        ),
        "candidate_b_scope_missing_upstream": boundary.get(
            "candidate_b_scope_missing_upstream"
        ),
        "basis_bearing_scope_division_missing_upstream": boundary.get(
            "basis_bearing_scope_division_missing_upstream"
        ),
        "future_scope_declaration_operation_shape_allowed": boundary.get(
            "future_scope_declaration_operation_shape_allowed"
        ),
        "scope_label_laundering_treated_as_basis": False,
        "cosmetic_scope_naming_treated_as_basis": False,
        "id_role_label_difference_treated_as_scope_basis": False,
        "shared_evidence_treated_as_scope_basis": False,
        "operation_evidence_alone_treated_as_scope_basis": False,
        "contaminated_lineage_treated_as_clean_scope_basis": False,
        "future_scope_declaration_operation_not_created": boundary.get(
            "future_scope_declaration_operation_not_created"
        ),
        "candidate_a_scope_not_declared": boundary.get("candidate_a_scope_not_declared"),
        "candidate_b_scope_not_declared": boundary.get("candidate_b_scope_not_declared"),
        "basis_bearing_scope_division_not_declared": boundary.get(
            "basis_bearing_scope_division_not_declared"
        ),
        "candidate_specific_content_not_emitted": boundary.get(
            "candidate_specific_content_not_emitted"
        ),
        "separate_seal_material_not_emitted": boundary.get(
            "separate_seal_material_not_emitted"
        ),
        "separate_lineage_receipt_material_not_emitted": boundary.get(
            "separate_lineage_receipt_material_not_emitted"
        ),
        "separate_digest_material_not_emitted": boundary.get(
            "separate_digest_material_not_emitted"
        ),
        "emission_operation_not_rerun": boundary.get("emission_operation_not_rerun"),
        "distinctness_operation_not_rerun": boundary.get(
            "distinctness_operation_not_rerun"
        ),
        "distinctness_supported_not_recorded": boundary.get(
            "distinctness_supported_not_recorded"
        ),
        "candidate_records_not_marked_distinct": boundary.get(
            "candidate_records_not_marked_distinct"
        ),
        "candidate_standing_not_authorized": boundary.get(
            "candidate_standing_not_authorized"
        ),
        "descendant_bodies_not_created": boundary.get("descendant_bodies_not_created"),
        "standing_descendants_not_created": boundary.get(
            "standing_descendants_not_created"
        ),
        "first_crossing_not_authorized": boundary.get(
            "first_crossing_not_authorized"
        ),
        "relation_not_created": boundary.get("relation_not_created"),
        "field_machinery_not_created": boundary.get("field_machinery_not_created"),
        "runtime_not_created": boundary.get("runtime_not_created"),
        "api_not_created": boundary.get("api_not_created"),
        "currentness_not_created": boundary.get("currentness_not_created"),
        "authority_not_created": boundary.get("authority_not_created"),
        "standing_not_created": boundary.get("standing_not_created"),
        "output_not_authorized": boundary.get("output_not_authorized"),
        "action_not_authorized": boundary.get("action_not_authorized"),
        "derivative_reception_not_authorized": boundary.get(
            "derivative_reception_not_authorized"
        ),
        "synchronization_not_authorized": boundary.get(
            "synchronization_not_authorized"
        ),
        "follow_on_not_authorized": boundary.get("follow_on_not_authorized"),
        "prior_unsupported_claims_not_validated": boundary.get(
            "prior_unsupported_claims_not_validated"
        ),
        "affected_file_not_repaired": boundary.get("affected_file_not_repaired"),
        "affected_file_treated_as_clean_basis": False,
        "contaminated_lineage_treated_as_clean_basis": False,
        "existence_claim_evidence_check_not_overridden": boundary.get(
            "existence_claim_evidence_check_not_overridden"
        ),
        "existence_claim_evidence_check_not_bypassed": boundary.get(
            "existence_claim_evidence_check_not_bypassed"
        ),
        "differentiation_operation_not_overridden": boundary.get(
            "differentiation_operation_not_overridden"
        ),
        "differentiation_operation_not_bypassed": boundary.get(
            "differentiation_operation_not_bypassed"
        ),
        "distinctness_operation_boundary_not_overridden": boundary.get(
            "distinctness_operation_boundary_not_overridden"
        ),
        "distinctness_operation_boundary_not_bypassed": boundary.get(
            "distinctness_operation_boundary_not_bypassed"
        ),
        "distinctness_operation_not_overridden": boundary.get(
            "distinctness_operation_not_overridden"
        ),
        "distinctness_operation_not_bypassed": boundary.get(
            "distinctness_operation_not_bypassed"
        ),
        "basis_emission_boundary_not_overridden": boundary.get(
            "basis_emission_boundary_not_overridden"
        ),
        "basis_emission_boundary_not_bypassed": boundary.get(
            "basis_emission_boundary_not_bypassed"
        ),
        "basis_emission_operation_not_overridden": boundary.get(
            "basis_emission_operation_not_overridden"
        ),
        "basis_emission_operation_not_bypassed": boundary.get(
            "basis_emission_operation_not_bypassed"
        ),
        "scan_not_performed": boundary.get("scan_not_performed"),
        "repository_scan_not_performed": boundary.get("repository_scan_not_performed"),
        "repair_not_performed": boundary.get("repair_not_performed"),
        "validation_not_enforced": boundary.get("validation_not_enforced"),
        "hidden_repair_not_performed": boundary.get("hidden_repair_not_performed"),
        "silent_overwrite_not_performed": boundary.get(
            "silent_overwrite_not_performed"
        ),
        "boundary_spec_markers_present": boundary.get("boundary_spec_markers_present"),
        "completed_basis_emission_operation_terminal_summary_markers_present": boundary.get(
            "completed_basis_emission_operation_terminal_summary_markers_present"
        ),
        "completed_basis_emission_boundary_terminal_summary_markers_present": boundary.get(
            "completed_basis_emission_boundary_terminal_summary_markers_present"
        ),
        "completed_distinctness_operation_terminal_summary_markers_present": boundary.get(
            "completed_distinctness_operation_terminal_summary_markers_present"
        ),
        "completed_differentiation_operation_terminal_summary_markers_present": boundary.get(
            "completed_differentiation_operation_terminal_summary_markers_present"
        ),
        "result_level_non_claims_canonical_false": _result_level_non_claims_canonical_false(
            result.get("non_claims", {})
            if isinstance(result.get("non_claims"), Mapping)
            else {}
        ),
    }


def _next_available_path(path: Path) -> Path:
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


def _assert_output_path_allowed(path: Path) -> None:
    parts = set(path.parts)
    for forbidden in FORBIDDEN_OUTPUT_ROOT_PARTS:
        if forbidden in parts:
            raise DescendantBodyCandidateNonCosmeticScopeDivisionDeclarationBoundaryV0MinError(
                f"Refusing to write boundary result under forbidden prior root: {forbidden}"
            )


def write_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a stable JSON result without silently overwriting existing files."""

    boundary_raw = result.get(
        "descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary", {}
    )
    boundary = boundary_raw if isinstance(boundary_raw, Mapping) else {}
    boundary_id = _safe_filename(
        str(
            boundary.get("candidate_non_cosmetic_scope_division_declaration_boundary_id")
            or DEFAULT_BOUNDARY_ID
        )
    )

    if output_path is None:
        destination = (
            _repo_path(OUTPUT_ROOT)
            / f"{boundary_id}__candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_result.json"
        )
    else:
        destination = Path(output_path)
        if destination.suffix != ".json":
            destination = (
                destination
                / f"{boundary_id}__candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_result.json"
            )
        if not destination.is_absolute():
            destination = REPO_ROOT / destination

    _assert_output_path_allowed(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    writable_destination = _next_available_path(destination)
    with writable_destination.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return writable_destination
