"""Resolver for the candidate-specific distinctness basis emission boundary.

This module records one boundary result only. It preserves the completed
candidate-record distinctness operation's clean NOT_DISTINCT outcome and permits
only a future scope-division operation shape to be considered. It does not
define or implement that future operation, emit evidence, rerun distinctness,
authorize standing, repair contaminated lineage, scan the repository, or
authorize follow-on work.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateSpecificDistinctnessBasisEmissionBoundaryV0MinError(Exception):
    """Bounded resolver error for malformed local boundary requests."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min"

OUTCOME_RECORDED = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_RECORDED"
OUTCOME_BLOCKED = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_BLOCKED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_NOT_RECORDED,
)

BOUNDARY_TYPE = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY"
FUTURE_EMISSION_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION"
BOUNDARY_VERSION = "0.1.0"
ADMISSIBLE_FUTURE_BASIS_ROUTE = "SCOPE_DIVISION_ONLY"
RUPTURE_CLASS_BLOCKED = "COSMETIC_DIFFERENCE_CRYPTOGRAPHICALLY_DRESSED_AS_DISTINCTNESS"
UPSTREAM_DISTINCTNESS_OPERATION_RESULT = "NOT_DISTINCT"

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_BOUNDARY_ID = "descendant_body_candidate_specific_distinctness_basis_emission_boundary_001"
DEFAULT_BOUNDARY_QUESTION = (
    "Given one completed candidate-record distinctness operation that compared exactly two non-standing "
    "candidate records and recorded NOT_DISTINCT because candidate-specific content, separate seal material, "
    "separate lineage receipt material, and separate digest material were missing, may the body define a future "
    "operation that emits non-standing candidate-specific distinctness basis using non-cosmetic scope division, "
    "while forbidding id/role/label/template substitution, digest-laundered label difference, candidate standing, "
    "descendant-body creation, crossing, relation, FIELD machinery, runtime, currentness, authority, output, action, "
    "derivative reception, synchronization, repair, scan, validation enforcement, prior unsupported claim validation, "
    "and follow-on authorization?"
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOUNDARY_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_V0_MIN_SPEC.md"
)
DEFAULT_COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
OUTPUT_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "candidate_specific_distinctness_basis_emission_operation_created",
    "candidate_specific_distinctness_basis_emission_operation_performed",
    "candidate_specific_distinctness_basis_emission_operation_recorded",
    "candidate_specific_content_emitted",
    "separate_seal_material_emitted",
    "separate_lineage_receipt_material_emitted",
    "separate_digest_material_emitted",
    "distinctness_operation_rerun",
    "distinctness_supported_recorded",
    "candidate_records_marked_distinct",
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
    "scan_performed",
    "repository_scan_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "cosmetic_substitution_treated_as_basis",
    "digest_laundering_treated_as_basis",
    "id_role_label_difference_treated_as_basis",
    "shared_evidence_treated_as_basis",
    "operation_evidence_alone_treated_as_basis",
    "divergent_receipt_history_route_authorized",
    "carrier_separation_route_authorized",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "candidate_specific_distinctness_basis_emission_boundary_recorded",
    "boundary_created",
    "upstream_distinctness_operation_result_is_not_distinct",
    "not_distinct_preserved_as_clean_result",
    "candidate_specific_content_missing_upstream",
    "separate_seal_material_missing_upstream",
    "separate_lineage_receipt_material_missing_upstream",
    "separate_digest_material_missing_upstream",
    "scope_division_route_allowed_for_future_operation_shape",
    "divergent_receipt_history_route_not_authorized",
    "carrier_separation_route_not_authorized",
    "cosmetic_substitution_not_allowed",
    "digest_laundering_not_allowed",
    "id_role_label_difference_not_allowed_as_basis",
    "shared_evidence_not_allowed_as_basis",
    "operation_evidence_alone_not_allowed_as_basis",
    "future_emission_operation_not_created",
    "candidate_specific_content_not_emitted",
    "separate_seal_material_not_emitted",
    "separate_lineage_receipt_material_not_emitted",
    "separate_digest_material_not_emitted",
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
    "scan_not_performed",
    "repository_scan_not_performed",
    "repair_not_performed",
    "validation_not_enforced",
    "hidden_repair_not_performed",
    "silent_overwrite_not_performed",
    "boundary_spec_markers_present",
    "completed_distinctness_operation_terminal_summary_markers_present",
    "completed_differentiation_operation_terminal_summary_markers_present",
    "completed_distinctness_operation_boundary_terminal_summary_markers_present",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_QUESTION_UNDECLARED",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_INTENT_UNSUPPORTED",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_BLOCK_REQUESTED",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_TYPE_MISSING",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_TYPE_NOT_EXPECTED",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_VERSION_MISSING",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_VERSION_NOT_0_1_0",
    "FUTURE_EMISSION_OPERATION_TYPE_MISSING",
    "FUTURE_EMISSION_OPERATION_TYPE_NOT_EXPECTED",
    "ADMISSIBLE_FUTURE_BASIS_ROUTE_MISSING",
    "ADMISSIBLE_FUTURE_BASIS_ROUTE_NOT_SCOPE_DIVISION_ONLY",
    "RUPTURE_CLASS_BLOCKED_MISSING",
    "RUPTURE_CLASS_BLOCKED_NOT_EXPECTED",
    "BOUNDARY_SPEC_REFERENCE_MISSING",
    "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "UPSTREAM_DISTINCTNESS_OPERATION_RESULT_NOT_NOT_DISTINCT",
    "NOT_DISTINCT_NOT_PRESERVED_AS_CLEAN_RESULT",
    "CANDIDATE_SPECIFIC_CONTENT_MISSING_UPSTREAM_NOT_TRUE",
    "SEPARATE_SEAL_MATERIAL_MISSING_UPSTREAM_NOT_TRUE",
    "SEPARATE_LINEAGE_RECEIPT_MATERIAL_MISSING_UPSTREAM_NOT_TRUE",
    "SEPARATE_DIGEST_MATERIAL_MISSING_UPSTREAM_NOT_TRUE",
    "SCOPE_DIVISION_ROUTE_NOT_ALLOWED",
    "DIVERGENT_RECEIPT_HISTORY_ROUTE_AUTHORIZED_TRUE",
    "CARRIER_SEPARATION_ROUTE_AUTHORIZED_TRUE",
    "COSMETIC_SUBSTITUTION_TREATED_AS_BASIS_TRUE",
    "DIGEST_LAUNDERING_TREATED_AS_BASIS_TRUE",
    "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_BASIS_TRUE",
    "SHARED_EVIDENCE_TREATED_AS_BASIS_TRUE",
    "OPERATION_EVIDENCE_ALONE_TREATED_AS_BASIS_TRUE",
    "FUTURE_EMISSION_OPERATION_CREATED_TRUE",
    "CANDIDATE_SPECIFIC_CONTENT_EMITTED_TRUE",
    "SEPARATE_SEAL_MATERIAL_EMITTED_TRUE",
    "SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMITTED_TRUE",
    "SEPARATE_DIGEST_MATERIAL_EMITTED_TRUE",
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
    "REQUESTED_EMISSION_OPERATION_DEFINITION",
    "REQUESTED_EMISSION_OPERATION_IMPLEMENTATION",
    "REQUESTED_CANDIDATE_SPECIFIC_CONTENT_EMISSION",
    "REQUESTED_SEPARATE_SEAL_MATERIAL_EMISSION",
    "REQUESTED_SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMISSION",
    "REQUESTED_SEPARATE_DIGEST_MATERIAL_EMISSION",
    "REQUESTED_DISTINCTNESS_OPERATION_RERUN",
    "REQUESTED_DISTINCTNESS_SUPPORTED_RECORDING",
    "REQUESTED_CANDIDATE_RECORDS_MARKED_DISTINCT",
    "REQUESTED_REPOSITORY_SCAN",
    "REQUESTED_FILE_DISCOVERY",
    "REQUESTED_AFFECTED_FILE_REPAIR",
    "REQUESTED_AFFECTED_FILE_MUTATION",
    "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION",
    "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDE",
    "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASS",
    "REQUESTED_DIFFERENTIATION_OPERATION_OVERRIDE",
    "REQUESTED_DIFFERENTIATION_OPERATION_BYPASS",
    "REQUESTED_DISTINCTNESS_OPERATION_BOUNDARY_OVERRIDE",
    "REQUESTED_DISTINCTNESS_OPERATION_BOUNDARY_BYPASS",
    "REQUESTED_DISTINCTNESS_OPERATION_OVERRIDE",
    "REQUESTED_DISTINCTNESS_OPERATION_BYPASS",
    "REQUESTED_CANDIDATE_STANDING_AUTHORIZATION",
    "REQUESTED_DESCENDANT_BODY_CREATION",
    "REQUESTED_STANDING_DESCENDANT_CREATION",
    "REQUESTED_DESCENDANT_STANDING_CHECK",
    "REQUESTED_CROSSING_AUTHORIZATION",
    "REQUESTED_RELATION_CREATION",
    "REQUESTED_FIELD_MACHINERY_CREATION",
    "REQUESTED_RUNTIME_CREATION",
    "REQUESTED_CURRENTNESS_CREATION",
    "REQUESTED_AUTHORITY_CREATION",
    "REQUESTED_OUTPUT_AUTHORIZATION",
    "REQUESTED_ACTION_AUTHORIZATION",
    "REQUESTED_DERIVATIVE_RECEPTION_AUTHORIZATION",
    "REQUESTED_SYNCHRONIZATION_AUTHORIZATION",
    "REQUESTED_FOLLOW_ON_AUTHORIZATION",
    "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
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
    "SCAN_PERFORMED",
    "REPOSITORY_SCAN_PERFORMED",
    "REPAIR_PERFORMED",
    "VALIDATION_ENFORCED",
    "HIDDEN_REPAIR_PERFORMED",
    "SILENT_OVERWRITE_PERFORMED",
    "COSMETIC_SUBSTITUTION_TREATED_AS_BASIS",
    "DIGEST_LAUNDERING_TREATED_AS_BASIS",
    "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_BASIS",
    "SHARED_EVIDENCE_TREATED_AS_BASIS",
    "OPERATION_EVIDENCE_ALONE_TREATED_AS_BASIS",
    "DIVERGENT_RECEIPT_HISTORY_ROUTE_AUTHORIZED",
    "CARRIER_SEPARATION_ROUTE_AUTHORIZED",
    "BOUNDARY_SPEC_MARKER_MISSING",
    "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REQUEST_UNREADABLE",
)

BOUNDARY_SPEC_MARKERS = (
    ("Descendant Body Candidate-Specific Distinctness Basis Emission Boundary V0 Minimum Specification",),
    ("This file defines one boundary for a future candidate-specific distinctness basis emission operation.",),
    ("This file is boundary-only.",),
    ("This file does not define, implement, or perform the future emission operation.",),
    ("This file does not emit candidate-specific content, separate seal material, separate lineage receipt material, or separate digest material.",),
    ("This boundary exists to prevent a future emission operation from laundering cosmetic label differences into hash, seal, receipt, or digest difference.",),
    ("Digest difference is not distinctness unless the digested material carries non-cosmetic candidate-specific basis.",),
    ("Hash difference is not distinctness unless the hashed material carries non-cosmetic candidate-specific basis.",),
    ("Seal difference is not distinctness unless the sealed material carries non-cosmetic candidate-specific basis.",),
    ("Lineage receipt difference is not distinctness unless the receipt material carries non-cosmetic candidate-specific basis.",),
    ("Candidate-specific distinctness basis must be basis-bearing, not label-bearing.",),
    ("For the immediate next repo-local step, this boundary permits only a scope-division-based future operation shape to be defined.",),
    ("Divergent receipt-history and carrier separation remain open but are not authorized here.",),
    ("Scope division must be non-cosmetic and basis-bearing.",),
    ("cosmetic_substitution_treated_as_basis = false",),
    ("digest_laundering_treated_as_basis = false",),
    ("id_role_label_difference_treated_as_basis = false",),
    ("shared_evidence_treated_as_basis = false",),
    ("operation_evidence_alone_treated_as_basis = false",),
    ("divergent_receipt_history_route_authorized = false",),
    ("carrier_separation_route_authorized = false",),
)
COMPLETED_DISTINCTNESS_OPERATION_MARKERS = (
    ("DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",),
    ("distinctness_result = NOT_DISTINCT",),
    ("failed_check_count = 0",),
    ("candidate_record_count_compared = 2",),
    ("candidate_ids_distinct = true",),
    ("candidate_roles_distinct = true",),
    ("id_and_role_difference_only = true",),
    ("candidate_specific_content_present = false",),
    ("separate_seal_material_present = false",),
    ("separate_lineage_receipt_material_present = false",),
    ("separate_digest_material_present = false",),
    ("distinctness_supported = false",),
    ("NOT_DISTINCT is a clean operation result, not a failure.",),
    ("missing candidate-specific content",),
    ("missing separate seal material",),
    ("missing separate lineage receipt material",),
    ("missing separate digest material",),
    ("id and role difference alone is not distinctness",),
    ("shared evidence reference alone is not distinctness",),
    ("Operation evidence alone is not distinctness.",),
)
COMPLETED_DIFFERENTIATION_MARKERS = (
    ("DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",),
    ("exactly two result-contained non-standing candidate records",),
    ("candidate records are not descendant bodies", "candidate records remain non-standing and are not descendant bodies"),
    ("candidate records remain non-standing", "candidate_records_non_standing = true"),
)
COMPLETED_DISTINCTNESS_BOUNDARY_MARKERS = (
    ("DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_RECORDED",),
    ("enumeration is not distinction",),
    ("id and role difference alone are not distinctness",),
    ("shared evidence reference alone are not distinctness", "shared evidence reference alone is not distinctness"),
    ("distinctness support requires separate candidate-specific evidence",),
    ("candidate standing is not authorized",),
)

CHECKED_FALSE_FIELDS = (
    (
        "candidate_specific_distinctness_basis_emission_operation_created",
        "FUTURE_EMISSION_OPERATION_CREATED_TRUE",
    ),
    (
        "candidate_specific_distinctness_basis_emission_operation_performed",
        "REQUESTED_EMISSION_OPERATION_IMPLEMENTATION",
    ),
    (
        "candidate_specific_distinctness_basis_emission_operation_recorded",
        "REQUESTED_EMISSION_OPERATION_IMPLEMENTATION",
    ),
    ("divergent_receipt_history_route_authorized", "DIVERGENT_RECEIPT_HISTORY_ROUTE_AUTHORIZED_TRUE"),
    ("carrier_separation_route_authorized", "CARRIER_SEPARATION_ROUTE_AUTHORIZED_TRUE"),
    ("cosmetic_substitution_treated_as_basis", "COSMETIC_SUBSTITUTION_TREATED_AS_BASIS_TRUE"),
    ("digest_laundering_treated_as_basis", "DIGEST_LAUNDERING_TREATED_AS_BASIS_TRUE"),
    ("id_role_label_difference_treated_as_basis", "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_BASIS_TRUE"),
    ("shared_evidence_treated_as_basis", "SHARED_EVIDENCE_TREATED_AS_BASIS_TRUE"),
    ("operation_evidence_alone_treated_as_basis", "OPERATION_EVIDENCE_ALONE_TREATED_AS_BASIS_TRUE"),
    ("future_emission_operation_created", "FUTURE_EMISSION_OPERATION_CREATED_TRUE"),
    ("candidate_specific_content_emitted", "CANDIDATE_SPECIFIC_CONTENT_EMITTED_TRUE"),
    ("separate_seal_material_emitted", "SEPARATE_SEAL_MATERIAL_EMITTED_TRUE"),
    ("separate_lineage_receipt_material_emitted", "SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMITTED_TRUE"),
    ("separate_digest_material_emitted", "SEPARATE_DIGEST_MATERIAL_EMITTED_TRUE"),
    ("distinctness_operation_rerun", "DISTINCTNESS_OPERATION_RERUN_TRUE"),
    ("distinctness_supported_recorded", "DISTINCTNESS_SUPPORTED_RECORDED_TRUE"),
    ("candidate_records_marked_distinct", "CANDIDATE_RECORDS_MARKED_DISTINCT_TRUE"),
    ("scan_allowed", "SCAN_ALLOWED_TRUE"),
    ("repair_allowed", "REPAIR_ALLOWED_TRUE"),
    ("validation_enforcement_allowed", "VALIDATION_ENFORCEMENT_ALLOWED_TRUE"),
    ("candidate_standing_authorized", "CANDIDATE_STANDING_AUTHORIZED_TRUE"),
    ("descendant_body_created", "DESCENDANT_BODY_CREATED_TRUE"),
    ("standing_authorized", "STANDING_AUTHORIZED_TRUE"),
    ("crossing_authorized", "CROSSING_AUTHORIZED_TRUE"),
    ("relation_authorized", "RELATION_AUTHORIZED_TRUE"),
    ("field_machinery_authorized", "FIELD_MACHINERY_AUTHORIZED_TRUE"),
    ("runtime_created", "RUNTIME_CREATED_TRUE"),
    ("api_created", "API_CREATED_TRUE"),
    ("currentness_created", "CURRENTNESS_CREATED_TRUE"),
    ("authority_created", "AUTHORITY_CREATED_TRUE"),
    ("standing_created", "STANDING_CREATED_TRUE"),
    ("output_authorized", "OUTPUT_AUTHORIZED_TRUE"),
    ("action_authorized", "ACTION_AUTHORIZED_TRUE"),
    ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE"),
    ("synchronization_authorized", "SYNCHRONIZATION_AUTHORIZED_TRUE"),
    ("follow_on_authorized", "FOLLOW_ON_AUTHORIZED_TRUE"),
    ("follow_on_work_authorized", "FOLLOW_ON_AUTHORIZED"),
    ("prior_unsupported_candidate_a_claim_validated", "PRIOR_UNSUPPORTED_CANDIDATE_A_CLAIM_VALIDATED"),
    ("prior_unsupported_candidate_b_claim_validated", "PRIOR_UNSUPPORTED_CANDIDATE_B_CLAIM_VALIDATED"),
    ("prior_unsupported_derivation_event_claim_validated", "PRIOR_UNSUPPORTED_DERIVATION_EVENT_CLAIM_VALIDATED"),
    ("valid_derivation_event_recorded", "VALID_DERIVATION_EVENT_RECORDED"),
    ("affected_file_repaired", "AFFECTED_FILE_REPAIRED"),
    ("affected_file_edited", "AFFECTED_FILE_EDITED"),
    ("affected_file_deleted", "AFFECTED_FILE_DELETED"),
    ("affected_file_overwritten", "AFFECTED_FILE_OVERWRITTEN"),
    ("affected_file_replaced", "AFFECTED_FILE_REPLACED"),
    ("affected_file_redeemed", "AFFECTED_FILE_REDEEMED"),
    ("affected_file_treated_as_clean_basis", "AFFECTED_FILE_TREATED_AS_CLEAN_BASIS"),
    ("contaminated_lineage_treated_as_clean_basis", "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS"),
    ("existence_claim_evidence_check_overridden", "EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDDEN"),
    ("existence_claim_evidence_check_bypassed", "EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASSED"),
    ("differentiation_operation_overridden", "DIFFERENTIATION_OPERATION_OVERRIDDEN"),
    ("differentiation_operation_bypassed", "DIFFERENTIATION_OPERATION_BYPASSED"),
    ("distinctness_operation_boundary_overridden", "DISTINCTNESS_OPERATION_BOUNDARY_OVERRIDDEN"),
    ("distinctness_operation_boundary_bypassed", "DISTINCTNESS_OPERATION_BOUNDARY_BYPASSED"),
    ("distinctness_operation_overridden", "DISTINCTNESS_OPERATION_OVERRIDDEN"),
    ("distinctness_operation_bypassed", "DISTINCTNESS_OPERATION_BYPASSED"),
    ("scan_performed", "SCAN_PERFORMED"),
    ("repository_scan_performed", "REPOSITORY_SCAN_PERFORMED"),
    ("repair_performed", "REPAIR_PERFORMED"),
    ("validation_enforced", "VALIDATION_ENFORCED"),
    ("hidden_repair_performed", "HIDDEN_REPAIR_PERFORMED"),
    ("silent_overwrite_performed", "SILENT_OVERWRITE_PERFORMED"),
)

FORBIDDEN_TRUE_FIELD_CODES = {
    "candidate_specific_distinctness_basis_emission_operation_created": "FUTURE_EMISSION_OPERATION_CREATED_TRUE",
    "candidate_specific_distinctness_basis_emission_operation_performed": "REQUESTED_EMISSION_OPERATION_IMPLEMENTATION",
    "candidate_specific_distinctness_basis_emission_operation_recorded": "REQUESTED_EMISSION_OPERATION_IMPLEMENTATION",
    "candidate_specific_content_emitted": "CANDIDATE_SPECIFIC_CONTENT_EMITTED_TRUE",
    "separate_seal_material_emitted": "SEPARATE_SEAL_MATERIAL_EMITTED_TRUE",
    "separate_lineage_receipt_material_emitted": "SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMITTED_TRUE",
    "separate_digest_material_emitted": "SEPARATE_DIGEST_MATERIAL_EMITTED_TRUE",
    "distinctness_operation_rerun": "DISTINCTNESS_OPERATION_RERUN_TRUE",
    "distinctness_supported_recorded": "DISTINCTNESS_SUPPORTED_RECORDED_TRUE",
    "candidate_records_marked_distinct": "CANDIDATE_RECORDS_MARKED_DISTINCT_TRUE",
    "candidate_standing_authorized": "CANDIDATE_STANDING_AUTHORIZED",
    "descendant_body_created": "DESCENDANT_BODY_CREATED",
    "standing_authorized": "STANDING_AUTHORIZED",
    "crossing_authorized": "CROSSING_AUTHORIZED",
    "relation_authorized": "RELATION_AUTHORIZED",
    "field_machinery_created": "FIELD_MACHINERY_AUTHORIZED",
    "field_machinery_authorized": "FIELD_MACHINERY_AUTHORIZED",
    "runtime_created": "RUNTIME_CREATED",
    "api_created": "API_CREATED",
    "currentness_created": "CURRENTNESS_CREATED",
    "authority_created": "AUTHORITY_CREATED",
    "standing_created": "STANDING_CREATED",
    "output_authorized": "OUTPUT_AUTHORIZED",
    "action_authorized": "ACTION_AUTHORIZED",
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "synchronization_authorized": "SYNCHRONIZATION_AUTHORIZED",
    "follow_on_authorized": "FOLLOW_ON_AUTHORIZED",
    "follow_on_work_authorized": "FOLLOW_ON_AUTHORIZED",
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
    "scan_performed": "SCAN_PERFORMED",
    "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
    "repair_performed": "REPAIR_PERFORMED",
    "validation_enforced": "VALIDATION_ENFORCED",
    "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
    "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
    "cosmetic_substitution_treated_as_basis": "COSMETIC_SUBSTITUTION_TREATED_AS_BASIS",
    "digest_laundering_treated_as_basis": "DIGEST_LAUNDERING_TREATED_AS_BASIS",
    "id_role_label_difference_treated_as_basis": "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_BASIS",
    "shared_evidence_treated_as_basis": "SHARED_EVIDENCE_TREATED_AS_BASIS",
    "operation_evidence_alone_treated_as_basis": "OPERATION_EVIDENCE_ALONE_TREATED_AS_BASIS",
    "divergent_receipt_history_route_authorized": "DIVERGENT_RECEIPT_HISTORY_ROUTE_AUTHORIZED",
    "carrier_separation_route_authorized": "CARRIER_SEPARATION_ROUTE_AUTHORIZED",
}

REQUEST_FLAG_ALIASES = {
    "REQUESTED_EMISSION_OPERATION_DEFINITION": (
        "requested_emission_operation_definition",
        "request_emission_operation_definition",
        "define_future_emission_operation",
        "future_emission_operation_definition_requested",
    ),
    "REQUESTED_EMISSION_OPERATION_IMPLEMENTATION": (
        "requested_emission_operation_implementation",
        "request_emission_operation_implementation",
        "implement_future_emission_operation",
        "future_emission_operation_implementation_requested",
    ),
    "REQUESTED_CANDIDATE_SPECIFIC_CONTENT_EMISSION": (
        "requested_candidate_specific_content_emission",
        "request_candidate_specific_content_emission",
        "emit_candidate_specific_content",
    ),
    "REQUESTED_SEPARATE_SEAL_MATERIAL_EMISSION": (
        "requested_separate_seal_material_emission",
        "request_separate_seal_material_emission",
        "emit_separate_seal_material",
    ),
    "REQUESTED_SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMISSION": (
        "requested_separate_lineage_receipt_material_emission",
        "request_separate_lineage_receipt_material_emission",
        "emit_separate_lineage_receipt_material",
    ),
    "REQUESTED_SEPARATE_DIGEST_MATERIAL_EMISSION": (
        "requested_separate_digest_material_emission",
        "request_separate_digest_material_emission",
        "emit_separate_digest_material",
    ),
    "REQUESTED_DISTINCTNESS_OPERATION_RERUN": (
        "requested_distinctness_operation_rerun",
        "request_distinctness_operation_rerun",
        "rerun_distinctness_operation",
    ),
    "REQUESTED_DISTINCTNESS_SUPPORTED_RECORDING": (
        "requested_distinctness_supported_recording",
        "request_distinctness_supported_recording",
        "record_distinctness_supported",
    ),
    "REQUESTED_CANDIDATE_RECORDS_MARKED_DISTINCT": (
        "requested_candidate_records_marked_distinct",
        "request_candidate_records_marked_distinct",
        "mark_candidate_records_distinct",
    ),
    "REQUESTED_REPOSITORY_SCAN": ("requested_repository_scan", "request_repository_scan"),
    "REQUESTED_FILE_DISCOVERY": ("requested_file_discovery", "request_file_discovery"),
    "REQUESTED_AFFECTED_FILE_REPAIR": ("requested_affected_file_repair", "request_affected_file_repair"),
    "REQUESTED_AFFECTED_FILE_MUTATION": ("requested_affected_file_mutation", "request_affected_file_mutation"),
    "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION": (
        "requested_prior_unsupported_claim_validation",
        "request_prior_unsupported_claim_validation",
    ),
    "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDE": (
        "requested_existence_claim_evidence_check_override",
        "request_existence_claim_evidence_check_override",
    ),
    "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASS": (
        "requested_existence_claim_evidence_check_bypass",
        "request_existence_claim_evidence_check_bypass",
    ),
    "REQUESTED_DIFFERENTIATION_OPERATION_OVERRIDE": (
        "requested_differentiation_operation_override",
        "request_differentiation_operation_override",
    ),
    "REQUESTED_DIFFERENTIATION_OPERATION_BYPASS": (
        "requested_differentiation_operation_bypass",
        "request_differentiation_operation_bypass",
    ),
    "REQUESTED_DISTINCTNESS_OPERATION_BOUNDARY_OVERRIDE": (
        "requested_distinctness_operation_boundary_override",
        "request_distinctness_operation_boundary_override",
    ),
    "REQUESTED_DISTINCTNESS_OPERATION_BOUNDARY_BYPASS": (
        "requested_distinctness_operation_boundary_bypass",
        "request_distinctness_operation_boundary_bypass",
    ),
    "REQUESTED_DISTINCTNESS_OPERATION_OVERRIDE": (
        "requested_distinctness_operation_override",
        "request_distinctness_operation_override",
    ),
    "REQUESTED_DISTINCTNESS_OPERATION_BYPASS": (
        "requested_distinctness_operation_bypass",
        "request_distinctness_operation_bypass",
    ),
    "REQUESTED_CANDIDATE_STANDING_AUTHORIZATION": (
        "requested_candidate_standing_authorization",
        "request_candidate_standing_authorization",
    ),
    "REQUESTED_DESCENDANT_BODY_CREATION": (
        "requested_descendant_body_creation",
        "request_descendant_body_creation",
    ),
    "REQUESTED_STANDING_DESCENDANT_CREATION": (
        "requested_standing_descendant_creation",
        "request_standing_descendant_creation",
    ),
    "REQUESTED_DESCENDANT_STANDING_CHECK": (
        "requested_descendant_standing_check",
        "request_descendant_standing_check",
    ),
    "REQUESTED_CROSSING_AUTHORIZATION": ("requested_crossing_authorization", "request_crossing_authorization"),
    "REQUESTED_RELATION_CREATION": ("requested_relation_creation", "request_relation_creation"),
    "REQUESTED_FIELD_MACHINERY_CREATION": (
        "requested_field_machinery_creation",
        "request_field_machinery_creation",
    ),
    "REQUESTED_RUNTIME_CREATION": ("requested_runtime_creation", "request_runtime_creation"),
    "REQUESTED_CURRENTNESS_CREATION": ("requested_currentness_creation", "request_currentness_creation"),
    "REQUESTED_AUTHORITY_CREATION": ("requested_authority_creation", "request_authority_creation"),
    "REQUESTED_OUTPUT_AUTHORIZATION": ("requested_output_authorization", "request_output_authorization"),
    "REQUESTED_ACTION_AUTHORIZATION": ("requested_action_authorization", "request_action_authorization"),
    "REQUESTED_DERIVATIVE_RECEPTION_AUTHORIZATION": (
        "requested_derivative_reception_authorization",
        "request_derivative_reception_authorization",
    ),
    "REQUESTED_SYNCHRONIZATION_AUTHORIZATION": (
        "requested_synchronization_authorization",
        "request_synchronization_authorization",
    ),
    "REQUESTED_FOLLOW_ON_AUTHORIZATION": ("requested_follow_on_authorization", "request_follow_on_authorization"),
    "REQUESTED_RAW_MARKDOWN_BODY_RETURN": (
        "requested_raw_markdown_body_return",
        "return_raw_full_markdown_bodies",
        "return_raw_markdown_body",
        "request_raw_markdown_body_return",
    ),
}

SENSITIVE_KEY_PARTS = ("raw_body", "full_body", "markdown_body", "hidden_repo_state", "local_cache", "current_working_tree")


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _as_repo_path(path_value: Any) -> Path:
    path = Path(str(path_value))
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def _read_text_file(path_value: Any) -> tuple[bool, str]:
    if not isinstance(path_value, (str, Path)) or not str(path_value):
        return False, ""
    path = _as_repo_path(path_value)
    if not path.is_file():
        return False, ""
    try:
        return True, path.read_text(encoding="utf-8")
    except OSError:
        return False, ""


def _safe_filename_part(value: Any) -> str:
    safe = str(value or DEFAULT_BOUNDARY_ID)
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe.strip("._-") or DEFAULT_BOUNDARY_ID


def _sanitize_value(key: str, value: Any) -> Any:
    lowered = key.lower()
    if any(part in lowered for part in SENSITIVE_KEY_PARTS) or lowered.endswith("_body"):
        return "[redacted]"
    if isinstance(value, Mapping):
        return {str(child_key): _sanitize_value(str(child_key), child_value) for child_key, child_value in value.items()}
    if isinstance(value, list):
        return [_sanitize_value(key, item) for item in value[:20]]
    if isinstance(value, tuple):
        return [_sanitize_value(key, item) for item in value[:20]]
    return value


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> None:
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": expected_posture,
            "actual_posture": _sanitize_value(check_name, actual_posture),
            "block_code": code,
            "failure_code": code,
        }
    )


def _failed_check_count(checks: list[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is not True)


def _passed_check_count(checks: list[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is True)


def _first_failed_code(checks: list[Mapping[str, Any]]) -> tuple[str | None, str | None]:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            return str(code) if code else None, str(check.get("check_name", "blocked"))
    return None, None


def _marker_groups_present(path_value: Any, marker_groups: tuple[tuple[str, ...], ...]) -> tuple[bool, dict[str, Any]]:
    readable, text = _read_text_file(path_value)
    if not readable:
        return False, {"readable": False, "missing_marker_count": len(marker_groups), "missing_markers": [group[0] for group in marker_groups[:5]]}
    missing = [group[0] for group in marker_groups if not any(marker in text for marker in group)]
    return not missing, {"readable": True, "missing_marker_count": len(missing), "missing_markers": missing[:5]}


def _validate_marker_file(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    field_name: str,
    marker_groups: tuple[tuple[str, ...], ...],
    check_name: str,
    code: str,
) -> bool:
    passed, actual = _marker_groups_present(request.get(field_name), marker_groups)
    _add_check(checks, check_name, passed, "declared markdown basis contains required markers", actual, code)
    return passed


def _validate_required_non_claims(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        _add_check(
            checks,
            "required_non_claims_false",
            False,
            "declared_non_claims mapping with every required key set to false",
            type(declared).__name__,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return
    malformed: list[str] = []
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared or declared.get(key) is not False:
            malformed.append(key)
    _add_check(
        checks,
        "required_non_claims_false",
        not malformed,
        "every required declared non-claim is exactly false",
        {"malformed_count": len(malformed), "malformed_keys": malformed[:8]},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _validate_request(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> dict[str, bool]:
    intent = request.get("candidate_specific_distinctness_basis_emission_boundary_intent")
    _add_check(
        checks,
        "boundary_question_declared",
        bool(request.get("candidate_specific_distinctness_basis_emission_boundary_question")),
        "boundary question declared",
        request.get("candidate_specific_distinctness_basis_emission_boundary_question"),
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_QUESTION_UNDECLARED",
    )
    _add_check(
        checks,
        "boundary_intent_supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _add_check(
            checks,
            "boundary_block_intent_not_requested",
            False,
            "non-blocking intent",
            intent,
            "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_BLOCK_REQUESTED",
        )

    boundary_type = request.get("candidate_specific_distinctness_basis_emission_boundary_type")
    _add_check(
        checks,
        "boundary_type_declared",
        bool(boundary_type),
        BOUNDARY_TYPE,
        boundary_type,
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_TYPE_MISSING",
    )
    _add_check(
        checks,
        "boundary_type_exact",
        boundary_type == BOUNDARY_TYPE,
        BOUNDARY_TYPE,
        boundary_type,
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_TYPE_NOT_EXPECTED",
    )

    boundary_version = request.get("candidate_specific_distinctness_basis_emission_boundary_version")
    _add_check(
        checks,
        "boundary_version_declared",
        bool(boundary_version),
        BOUNDARY_VERSION,
        boundary_version,
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_VERSION_MISSING",
    )
    _add_check(
        checks,
        "boundary_version_exact",
        boundary_version == BOUNDARY_VERSION,
        BOUNDARY_VERSION,
        boundary_version,
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_VERSION_NOT_0_1_0",
    )

    _validate_exact_field(checks, request, "future_emission_operation_type", FUTURE_EMISSION_OPERATION_TYPE, "FUTURE_EMISSION_OPERATION_TYPE_MISSING", "FUTURE_EMISSION_OPERATION_TYPE_NOT_EXPECTED")
    _validate_exact_field(checks, request, "admissible_future_basis_route", ADMISSIBLE_FUTURE_BASIS_ROUTE, "ADMISSIBLE_FUTURE_BASIS_ROUTE_MISSING", "ADMISSIBLE_FUTURE_BASIS_ROUTE_NOT_SCOPE_DIVISION_ONLY")
    _validate_exact_field(checks, request, "rupture_class_blocked", RUPTURE_CLASS_BLOCKED, "RUPTURE_CLASS_BLOCKED_MISSING", "RUPTURE_CLASS_BLOCKED_NOT_EXPECTED")

    _validate_reference(checks, request, "boundary_spec_reference", "BOUNDARY_SPEC_REFERENCE_MISSING")
    _validate_reference(
        checks,
        request,
        "completed_distinctness_operation_terminal_summary_reference",
        "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    )
    _validate_reference(
        checks,
        request,
        "completed_differentiation_operation_terminal_summary_reference",
        "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    )
    _validate_reference(
        checks,
        request,
        "completed_distinctness_operation_boundary_terminal_summary_reference",
        "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    )

    _validate_exact_bool(checks, request, "upstream_distinctness_operation_result", UPSTREAM_DISTINCTNESS_OPERATION_RESULT, "UPSTREAM_DISTINCTNESS_OPERATION_RESULT_NOT_NOT_DISTINCT")
    _validate_true_field(checks, request, "not_distinct_preserved_as_clean_result", "NOT_DISTINCT_NOT_PRESERVED_AS_CLEAN_RESULT")
    _validate_true_field(checks, request, "candidate_specific_content_missing_upstream", "CANDIDATE_SPECIFIC_CONTENT_MISSING_UPSTREAM_NOT_TRUE")
    _validate_true_field(checks, request, "separate_seal_material_missing_upstream", "SEPARATE_SEAL_MATERIAL_MISSING_UPSTREAM_NOT_TRUE")
    _validate_true_field(checks, request, "separate_lineage_receipt_material_missing_upstream", "SEPARATE_LINEAGE_RECEIPT_MATERIAL_MISSING_UPSTREAM_NOT_TRUE")
    _validate_true_field(checks, request, "separate_digest_material_missing_upstream", "SEPARATE_DIGEST_MATERIAL_MISSING_UPSTREAM_NOT_TRUE")
    _validate_true_field(checks, request, "scope_division_route_allowed_for_future_operation_shape", "SCOPE_DIVISION_ROUTE_NOT_ALLOWED")

    for field_name, code in CHECKED_FALSE_FIELDS:
        _validate_false_field(checks, request, field_name, code)
    for field_name, code in FORBIDDEN_TRUE_FIELD_CODES.items():
        if request.get(field_name) is True:
            _add_check(checks, f"{field_name}_not_true", False, False, True, code)
    for code, aliases in REQUEST_FLAG_ALIASES.items():
        triggered = [alias for alias in aliases if request.get(alias) is True]
        _add_check(
            checks,
            f"{code.lower()}_not_requested",
            not triggered,
            "request flag absent or false",
            {"triggered_aliases": triggered},
            code,
        )

    _validate_required_non_claims(checks, request)
    marker_posture = {
        "boundary_spec_markers_present": _validate_marker_file(
            checks,
            request,
            "boundary_spec_reference",
            BOUNDARY_SPEC_MARKERS,
            "boundary_spec_markers_present",
            "BOUNDARY_SPEC_MARKER_MISSING",
        ),
        "completed_distinctness_operation_terminal_summary_markers_present": _validate_marker_file(
            checks,
            request,
            "completed_distinctness_operation_terminal_summary_reference",
            COMPLETED_DISTINCTNESS_OPERATION_MARKERS,
            "completed_distinctness_operation_terminal_summary_markers_present",
            "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ),
        "completed_differentiation_operation_terminal_summary_markers_present": _validate_marker_file(
            checks,
            request,
            "completed_differentiation_operation_terminal_summary_reference",
            COMPLETED_DIFFERENTIATION_MARKERS,
            "completed_differentiation_operation_terminal_summary_markers_present",
            "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ),
        "completed_distinctness_operation_boundary_terminal_summary_markers_present": _validate_marker_file(
            checks,
            request,
            "completed_distinctness_operation_boundary_terminal_summary_reference",
            COMPLETED_DISTINCTNESS_BOUNDARY_MARKERS,
            "completed_distinctness_operation_boundary_terminal_summary_markers_present",
            "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        ),
    }
    _add_check(
        checks,
        "result_level_non_claims_canonical_false",
        True,
        "final result-level non-claims canonical false",
        True,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return marker_posture


def _validate_reference(checks: list[dict[str, Any]], request: Mapping[str, Any], field_name: str, code: str) -> None:
    value = request.get(field_name)
    _add_check(checks, f"{field_name}_declared", isinstance(value, (str, Path)) and bool(str(value)), "declared reference path", value, code)


def _validate_exact_field(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    field_name: str,
    expected: str,
    missing_code: str,
    mismatch_code: str,
) -> None:
    value = request.get(field_name)
    _add_check(checks, f"{field_name}_declared", bool(value), expected, value, missing_code)
    _add_check(checks, f"{field_name}_exact", value == expected, expected, value, mismatch_code)


def _validate_exact_bool(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    field_name: str,
    expected: str,
    code: str,
) -> None:
    value = request.get(field_name)
    _add_check(checks, f"{field_name}_exact", value == expected, expected, value, code)


def _validate_true_field(checks: list[dict[str, Any]], request: Mapping[str, Any], field_name: str, code: str) -> None:
    value = request.get(field_name)
    _add_check(checks, f"{field_name}_true", value is True, True, value, code)


def _validate_false_field(checks: list[dict[str, Any]], request: Mapping[str, Any], field_name: str, code: str) -> None:
    value = request.get(field_name)
    _add_check(checks, f"{field_name}_false", value is False, False, value, code)


def _safe_official_value(request: Mapping[str, Any], field_name: str, expected: str) -> str:
    return expected if request.get(field_name) == expected else ""


def _build_boundary_object(request: Mapping[str, Any], recorded: bool, marker_posture: Mapping[str, bool]) -> dict[str, Any]:
    return {
        "candidate_specific_distinctness_basis_emission_boundary_id": _sanitize_value(
            "candidate_specific_distinctness_basis_emission_boundary_id",
            request.get("candidate_specific_distinctness_basis_emission_boundary_id", DEFAULT_BOUNDARY_ID),
        ),
        "candidate_specific_distinctness_basis_emission_boundary_type": _safe_official_value(
            request, "candidate_specific_distinctness_basis_emission_boundary_type", BOUNDARY_TYPE
        ),
        "candidate_specific_distinctness_basis_emission_boundary_version": _safe_official_value(
            request, "candidate_specific_distinctness_basis_emission_boundary_version", BOUNDARY_VERSION
        ),
        "future_emission_operation_type": _safe_official_value(
            request, "future_emission_operation_type", FUTURE_EMISSION_OPERATION_TYPE
        ),
        "admissible_future_basis_route": _safe_official_value(
            request, "admissible_future_basis_route", ADMISSIBLE_FUTURE_BASIS_ROUTE
        ),
        "rupture_class_blocked": _safe_official_value(request, "rupture_class_blocked", RUPTURE_CLASS_BLOCKED),
        "upstream_distinctness_operation_result": _safe_official_value(
            request, "upstream_distinctness_operation_result", UPSTREAM_DISTINCTNESS_OPERATION_RESULT
        ),
        "candidate_specific_distinctness_basis_emission_boundary_recorded": recorded,
        "boundary_created": recorded,
        "upstream_distinctness_operation_result_is_not_distinct": request.get("upstream_distinctness_operation_result")
        == UPSTREAM_DISTINCTNESS_OPERATION_RESULT,
        "not_distinct_preserved_as_clean_result": request.get("not_distinct_preserved_as_clean_result") is True,
        "candidate_specific_content_missing_upstream": request.get("candidate_specific_content_missing_upstream") is True,
        "separate_seal_material_missing_upstream": request.get("separate_seal_material_missing_upstream") is True,
        "separate_lineage_receipt_material_missing_upstream": request.get("separate_lineage_receipt_material_missing_upstream")
        is True,
        "separate_digest_material_missing_upstream": request.get("separate_digest_material_missing_upstream") is True,
        "scope_division_route_allowed_for_future_operation_shape": (
            request.get("scope_division_route_allowed_for_future_operation_shape") is True
        ),
        "divergent_receipt_history_route_not_authorized": True,
        "carrier_separation_route_not_authorized": True,
        "cosmetic_substitution_not_allowed": True,
        "digest_laundering_not_allowed": True,
        "id_role_label_difference_not_allowed_as_basis": True,
        "shared_evidence_not_allowed_as_basis": True,
        "operation_evidence_alone_not_allowed_as_basis": True,
        "future_emission_operation_not_created": True,
        "candidate_specific_content_not_emitted": True,
        "separate_seal_material_not_emitted": True,
        "separate_lineage_receipt_material_not_emitted": True,
        "separate_digest_material_not_emitted": True,
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
        "scan_not_performed": True,
        "repository_scan_not_performed": True,
        "repair_not_performed": True,
        "validation_not_enforced": True,
        "hidden_repair_not_performed": True,
        "silent_overwrite_not_performed": True,
        "boundary_spec_markers_present": bool(marker_posture.get("boundary_spec_markers_present")),
        "completed_distinctness_operation_terminal_summary_markers_present": bool(
            marker_posture.get("completed_distinctness_operation_terminal_summary_markers_present")
        ),
        "completed_differentiation_operation_terminal_summary_markers_present": bool(
            marker_posture.get("completed_differentiation_operation_terminal_summary_markers_present")
        ),
        "completed_distinctness_operation_boundary_terminal_summary_markers_present": bool(
            marker_posture.get("completed_distinctness_operation_boundary_terminal_summary_markers_present")
        ),
    }


def _declared_question_section(request: Mapping[str, Any]) -> dict[str, Any]:
    fields = (
        "candidate_specific_distinctness_basis_emission_boundary_id",
        "candidate_specific_distinctness_basis_emission_boundary_question",
        "candidate_specific_distinctness_basis_emission_boundary_intent",
        "candidate_specific_distinctness_basis_emission_boundary_type",
        "candidate_specific_distinctness_basis_emission_boundary_version",
        "future_emission_operation_type",
        "admissible_future_basis_route",
        "rupture_class_blocked",
        "boundary_spec_reference",
        "completed_distinctness_operation_terminal_summary_reference",
        "completed_differentiation_operation_terminal_summary_reference",
        "completed_distinctness_operation_boundary_terminal_summary_reference",
        "upstream_distinctness_operation_result",
    )
    return {field: _sanitize_value(field, request.get(field)) for field in fields}


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    marker_posture: Mapping[str, bool],
    outcome: str,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    boundary = _build_boundary_object(request, recorded, marker_posture)
    non_claims = _canonical_false_non_claims()
    code, reason = _first_failed_code(checks)
    block = (
        {"blocked": True, "code": code, "block_code": code, "reason": reason}
        if outcome == OUTCOME_BLOCKED
        else {"blocked": False, "code": None, "block_code": None, "reason": None}
    )
    result: dict[str, Any] = {
        "candidate_specific_distinctness_basis_emission_boundary_metadata": {
            "candidate_specific_distinctness_basis_emission_boundary_id": boundary[
                "candidate_specific_distinctness_basis_emission_boundary_id"
            ],
            "boundary_type": BOUNDARY_TYPE,
            "result_version": RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_candidate_specific_distinctness_basis_emission_boundary_question": _declared_question_section(
            request
        ),
        "upstream_basis": {
            "completed_distinctness_operation_result": UPSTREAM_DISTINCTNESS_OPERATION_RESULT,
            "not_distinct_preserved_as_clean_result": request.get("not_distinct_preserved_as_clean_result") is True,
            "candidate_specific_content_missing_upstream": request.get("candidate_specific_content_missing_upstream")
            is True,
            "separate_seal_material_missing_upstream": request.get("separate_seal_material_missing_upstream") is True,
            "separate_lineage_receipt_material_missing_upstream": request.get(
                "separate_lineage_receipt_material_missing_upstream"
            )
            is True,
            "separate_digest_material_missing_upstream": request.get("separate_digest_material_missing_upstream")
            is True,
            "completed_distinctness_operation_terminal_summary_reference": _sanitize_value(
                "completed_distinctness_operation_terminal_summary_reference",
                request.get("completed_distinctness_operation_terminal_summary_reference"),
            ),
            "completed_differentiation_operation_terminal_summary_reference": _sanitize_value(
                "completed_differentiation_operation_terminal_summary_reference",
                request.get("completed_differentiation_operation_terminal_summary_reference"),
            ),
            "completed_distinctness_operation_boundary_terminal_summary_reference": _sanitize_value(
                "completed_distinctness_operation_boundary_terminal_summary_reference",
                request.get("completed_distinctness_operation_boundary_terminal_summary_reference"),
            ),
        },
        "candidate_specific_distinctness_basis_emission_boundary_basis": {
            "boundary_spec_reference": _sanitize_value(
                "boundary_spec_reference", request.get("boundary_spec_reference")
            ),
            "boundary_spec_markers_present": bool(marker_posture.get("boundary_spec_markers_present")),
            "completed_distinctness_operation_terminal_summary_markers_present": bool(
                marker_posture.get("completed_distinctness_operation_terminal_summary_markers_present")
            ),
            "completed_differentiation_operation_terminal_summary_markers_present": bool(
                marker_posture.get("completed_differentiation_operation_terminal_summary_markers_present")
            ),
            "completed_distinctness_operation_boundary_terminal_summary_markers_present": bool(
                marker_posture.get("completed_distinctness_operation_boundary_terminal_summary_markers_present")
            ),
        },
        "descendant_body_candidate_specific_distinctness_basis_emission_boundary": boundary,
        "candidate_specific_distinctness_basis_emission_boundary_checks": checks,
        "candidate_specific_distinctness_basis_emission_boundary_statement": {
            "candidate_specific_distinctness_basis_emission_boundary_recorded": recorded,
            "boundary_created": recorded,
            "scope_division_route_allowed_for_future_operation_shape": boundary[
                "scope_division_route_allowed_for_future_operation_shape"
            ],
            "not_distinct_preserved_as_clean_result": boundary["not_distinct_preserved_as_clean_result"],
            "cosmetic_difference_cryptographically_dressed_as_distinctness_blocked": True,
            "result_level_non_claims_canonical_false": all(value is False for value in non_claims.values()),
        },
        "candidate_specific_distinctness_basis_emission_boundary_non_meaning": {
            "future_emission_operation_created": False,
            "candidate_specific_content_emitted": False,
            "separate_seal_material_emitted": False,
            "separate_lineage_receipt_material_emitted": False,
            "separate_digest_material_emitted": False,
            "distinctness_operation_rerun": False,
            "distinctness_supported_recorded": False,
            "candidate_records_marked_distinct": False,
            "candidate_standing_authorized": False,
            "descendant_body_created": False,
            "follow_on_authorized": False,
        },
        "not_recorded_basis": [] if outcome != OUTCOME_NOT_RECORDED else ["DO_NOT_RECORD intent was declared."],
        "what_remains_open": [
            "candidate-specific distinctness basis emission operation spec",
            "candidate-specific distinctness basis emission resolver",
            "candidate-specific distinctness basis emission test",
            "candidate-specific distinctness basis emission artifact",
            "actual candidate-specific content emission",
            "actual separate seal material emission",
            "actual separate lineage receipt material emission",
            "actual separate digest material emission",
            "future distinctness-supported operation result",
            "divergent receipt-history route",
            "carrier separation route",
            "candidate-record standing checks",
            "follow-on work",
        ],
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
        "candidate_specific_distinctness_basis_emission_boundary_summary": {},
    }
    result["candidate_specific_distinctness_basis_emission_boundary_summary"] = (
        build_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_summary(result)
    )
    return result


def build_declared_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_request(
    *,
    candidate_specific_distinctness_basis_emission_boundary_id: str = DEFAULT_BOUNDARY_ID,
    candidate_specific_distinctness_basis_emission_boundary_question: str = DEFAULT_BOUNDARY_QUESTION,
    candidate_specific_distinctness_basis_emission_boundary_intent: str = INTENT_RECORD,
    candidate_specific_distinctness_basis_emission_boundary_type: str = BOUNDARY_TYPE,
    candidate_specific_distinctness_basis_emission_boundary_version: str = BOUNDARY_VERSION,
    future_emission_operation_type: str = FUTURE_EMISSION_OPERATION_TYPE,
    admissible_future_basis_route: str = ADMISSIBLE_FUTURE_BASIS_ROUTE,
    rupture_class_blocked: str = RUPTURE_CLASS_BLOCKED,
    boundary_spec_reference: str = DEFAULT_BOUNDARY_SPEC_REFERENCE,
    completed_distinctness_operation_terminal_summary_reference: str = (
        DEFAULT_COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE
    ),
    completed_differentiation_operation_terminal_summary_reference: str = (
        DEFAULT_COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE
    ),
    completed_distinctness_operation_boundary_terminal_summary_reference: str = (
        DEFAULT_COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE
    ),
    upstream_distinctness_operation_result: str = UPSTREAM_DISTINCTNESS_OPERATION_RESULT,
    candidate_specific_content_missing_upstream: bool = True,
    separate_seal_material_missing_upstream: bool = True,
    separate_lineage_receipt_material_missing_upstream: bool = True,
    separate_digest_material_missing_upstream: bool = True,
    not_distinct_preserved_as_clean_result: bool = True,
    scope_division_route_allowed_for_future_operation_shape: bool = True,
    divergent_receipt_history_route_authorized: bool = False,
    carrier_separation_route_authorized: bool = False,
    cosmetic_substitution_treated_as_basis: bool = False,
    digest_laundering_treated_as_basis: bool = False,
    id_role_label_difference_treated_as_basis: bool = False,
    shared_evidence_treated_as_basis: bool = False,
    operation_evidence_alone_treated_as_basis: bool = False,
    candidate_specific_distinctness_basis_emission_operation_created: bool = False,
    candidate_specific_distinctness_basis_emission_operation_performed: bool = False,
    candidate_specific_distinctness_basis_emission_operation_recorded: bool = False,
    future_emission_operation_created: bool = False,
    candidate_specific_content_emitted: bool = False,
    separate_seal_material_emitted: bool = False,
    separate_lineage_receipt_material_emitted: bool = False,
    separate_digest_material_emitted: bool = False,
    distinctness_operation_rerun: bool = False,
    distinctness_supported_recorded: bool = False,
    candidate_records_marked_distinct: bool = False,
    candidate_standing_authorized: bool = False,
    descendant_body_created: bool = False,
    standing_authorized: bool = False,
    crossing_authorized: bool = False,
    relation_authorized: bool = False,
    field_machinery_authorized: bool = False,
    runtime_created: bool = False,
    api_created: bool = False,
    currentness_created: bool = False,
    authority_created: bool = False,
    standing_created: bool = False,
    output_authorized: bool = False,
    action_authorized: bool = False,
    derivative_reception_authorized: bool = False,
    synchronization_authorized: bool = False,
    follow_on_authorized: bool = False,
    scan_allowed: bool = False,
    repair_allowed: bool = False,
    validation_enforcement_allowed: bool = False,
    follow_on_work_authorized: bool = False,
    prior_unsupported_candidate_a_claim_validated: bool = False,
    prior_unsupported_candidate_b_claim_validated: bool = False,
    prior_unsupported_derivation_event_claim_validated: bool = False,
    valid_derivation_event_recorded: bool = False,
    affected_file_repaired: bool = False,
    affected_file_edited: bool = False,
    affected_file_deleted: bool = False,
    affected_file_overwritten: bool = False,
    affected_file_replaced: bool = False,
    affected_file_redeemed: bool = False,
    affected_file_treated_as_clean_basis: bool = False,
    contaminated_lineage_treated_as_clean_basis: bool = False,
    existence_claim_evidence_check_overridden: bool = False,
    existence_claim_evidence_check_bypassed: bool = False,
    differentiation_operation_overridden: bool = False,
    differentiation_operation_bypassed: bool = False,
    distinctness_operation_boundary_overridden: bool = False,
    distinctness_operation_boundary_bypassed: bool = False,
    distinctness_operation_overridden: bool = False,
    distinctness_operation_bypassed: bool = False,
    scan_performed: bool = False,
    repository_scan_performed: bool = False,
    repair_performed: bool = False,
    validation_enforced: bool = False,
    hidden_repair_performed: bool = False,
    silent_overwrite_performed: bool = False,
    declared_non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    request = {
        "candidate_specific_distinctness_basis_emission_boundary_id": candidate_specific_distinctness_basis_emission_boundary_id,
        "candidate_specific_distinctness_basis_emission_boundary_question": candidate_specific_distinctness_basis_emission_boundary_question,
        "candidate_specific_distinctness_basis_emission_boundary_intent": candidate_specific_distinctness_basis_emission_boundary_intent,
        "candidate_specific_distinctness_basis_emission_boundary_type": candidate_specific_distinctness_basis_emission_boundary_type,
        "candidate_specific_distinctness_basis_emission_boundary_version": candidate_specific_distinctness_basis_emission_boundary_version,
        "future_emission_operation_type": future_emission_operation_type,
        "admissible_future_basis_route": admissible_future_basis_route,
        "rupture_class_blocked": rupture_class_blocked,
        "boundary_spec_reference": boundary_spec_reference,
        "completed_distinctness_operation_terminal_summary_reference": completed_distinctness_operation_terminal_summary_reference,
        "completed_differentiation_operation_terminal_summary_reference": completed_differentiation_operation_terminal_summary_reference,
        "completed_distinctness_operation_boundary_terminal_summary_reference": completed_distinctness_operation_boundary_terminal_summary_reference,
        "upstream_distinctness_operation_result": upstream_distinctness_operation_result,
        "candidate_specific_content_missing_upstream": candidate_specific_content_missing_upstream,
        "separate_seal_material_missing_upstream": separate_seal_material_missing_upstream,
        "separate_lineage_receipt_material_missing_upstream": separate_lineage_receipt_material_missing_upstream,
        "separate_digest_material_missing_upstream": separate_digest_material_missing_upstream,
        "not_distinct_preserved_as_clean_result": not_distinct_preserved_as_clean_result,
        "scope_division_route_allowed_for_future_operation_shape": scope_division_route_allowed_for_future_operation_shape,
        "divergent_receipt_history_route_authorized": divergent_receipt_history_route_authorized,
        "carrier_separation_route_authorized": carrier_separation_route_authorized,
        "cosmetic_substitution_treated_as_basis": cosmetic_substitution_treated_as_basis,
        "digest_laundering_treated_as_basis": digest_laundering_treated_as_basis,
        "id_role_label_difference_treated_as_basis": id_role_label_difference_treated_as_basis,
        "shared_evidence_treated_as_basis": shared_evidence_treated_as_basis,
        "operation_evidence_alone_treated_as_basis": operation_evidence_alone_treated_as_basis,
        "candidate_specific_distinctness_basis_emission_operation_created": (
            candidate_specific_distinctness_basis_emission_operation_created
        ),
        "candidate_specific_distinctness_basis_emission_operation_performed": (
            candidate_specific_distinctness_basis_emission_operation_performed
        ),
        "candidate_specific_distinctness_basis_emission_operation_recorded": (
            candidate_specific_distinctness_basis_emission_operation_recorded
        ),
        "future_emission_operation_created": future_emission_operation_created,
        "candidate_specific_content_emitted": candidate_specific_content_emitted,
        "separate_seal_material_emitted": separate_seal_material_emitted,
        "separate_lineage_receipt_material_emitted": separate_lineage_receipt_material_emitted,
        "separate_digest_material_emitted": separate_digest_material_emitted,
        "distinctness_operation_rerun": distinctness_operation_rerun,
        "distinctness_supported_recorded": distinctness_supported_recorded,
        "candidate_records_marked_distinct": candidate_records_marked_distinct,
        "candidate_standing_authorized": candidate_standing_authorized,
        "descendant_body_created": descendant_body_created,
        "standing_authorized": standing_authorized,
        "crossing_authorized": crossing_authorized,
        "relation_authorized": relation_authorized,
        "field_machinery_authorized": field_machinery_authorized,
        "runtime_created": runtime_created,
        "api_created": api_created,
        "currentness_created": currentness_created,
        "authority_created": authority_created,
        "standing_created": standing_created,
        "output_authorized": output_authorized,
        "action_authorized": action_authorized,
        "derivative_reception_authorized": derivative_reception_authorized,
        "synchronization_authorized": synchronization_authorized,
        "follow_on_authorized": follow_on_authorized,
        "scan_allowed": scan_allowed,
        "repair_allowed": repair_allowed,
        "validation_enforcement_allowed": validation_enforcement_allowed,
        "follow_on_work_authorized": follow_on_work_authorized,
        "prior_unsupported_candidate_a_claim_validated": prior_unsupported_candidate_a_claim_validated,
        "prior_unsupported_candidate_b_claim_validated": prior_unsupported_candidate_b_claim_validated,
        "prior_unsupported_derivation_event_claim_validated": prior_unsupported_derivation_event_claim_validated,
        "valid_derivation_event_recorded": valid_derivation_event_recorded,
        "affected_file_repaired": affected_file_repaired,
        "affected_file_edited": affected_file_edited,
        "affected_file_deleted": affected_file_deleted,
        "affected_file_overwritten": affected_file_overwritten,
        "affected_file_replaced": affected_file_replaced,
        "affected_file_redeemed": affected_file_redeemed,
        "affected_file_treated_as_clean_basis": affected_file_treated_as_clean_basis,
        "contaminated_lineage_treated_as_clean_basis": contaminated_lineage_treated_as_clean_basis,
        "existence_claim_evidence_check_overridden": existence_claim_evidence_check_overridden,
        "existence_claim_evidence_check_bypassed": existence_claim_evidence_check_bypassed,
        "differentiation_operation_overridden": differentiation_operation_overridden,
        "differentiation_operation_bypassed": differentiation_operation_bypassed,
        "distinctness_operation_boundary_overridden": distinctness_operation_boundary_overridden,
        "distinctness_operation_boundary_bypassed": distinctness_operation_boundary_bypassed,
        "distinctness_operation_overridden": distinctness_operation_overridden,
        "distinctness_operation_bypassed": distinctness_operation_bypassed,
        "scan_performed": scan_performed,
        "repository_scan_performed": repository_scan_performed,
        "repair_performed": repair_performed,
        "validation_enforced": validation_enforced,
        "hidden_repair_performed": hidden_repair_performed,
        "silent_overwrite_performed": silent_overwrite_performed,
        "declared_non_claims": dict(declared_non_claims) if declared_non_claims is not None else _canonical_false_non_claims(),
    }
    return request


def resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
    declared_candidate_specific_distinctness_basis_emission_boundary: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_candidate_specific_distinctness_basis_emission_boundary is None:
        request: Mapping[str, Any] = (
            build_declared_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_request()
        )
    elif not isinstance(declared_candidate_specific_distinctness_basis_emission_boundary, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_boundary_request_mapping",
            False,
            "mapping request",
            type(declared_candidate_specific_distinctness_basis_emission_boundary).__name__,
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REQUEST_MALFORMED",
        )
        request = build_declared_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_request()
        return _build_result(request, checks, {}, OUTCOME_BLOCKED)
    else:
        request = dict(declared_candidate_specific_distinctness_basis_emission_boundary)

    checks = []
    marker_posture = _validate_request(checks, request)
    intent = request.get("candidate_specific_distinctness_basis_emission_boundary_intent")
    if _failed_check_count(checks) > 0:
        return _build_result(request, checks, marker_posture, OUTCOME_BLOCKED)
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, checks, marker_posture, OUTCOME_NOT_RECORDED)
    return _build_result(request, checks, marker_posture, OUTCOME_RECORDED)


def resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_from_path(
    declared_candidate_specific_distinctness_basis_emission_boundary_path: Path | str,
) -> dict[str, Any]:
    path = Path(declared_candidate_specific_distinctness_basis_emission_boundary_path)
    if not path.is_absolute():
        path = REPO_ROOT / path
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except (OSError, json.JSONDecodeError):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_boundary_request_readable",
            False,
            "readable JSON object request",
            str(path),
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REQUEST_UNREADABLE",
        )
        request = build_declared_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_request()
        return _build_result(request, checks, {}, OUTCOME_BLOCKED)
    if not isinstance(loaded, Mapping):
        checks = []
        _add_check(
            checks,
            "declared_boundary_request_mapping",
            False,
            "JSON object request",
            type(loaded).__name__,
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REQUEST_MALFORMED",
        )
        request = build_declared_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_request()
        return _build_result(request, checks, {}, OUTCOME_BLOCKED)
    return resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(loaded)


def build_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("candidate_specific_distinctness_basis_emission_boundary_checks", [])
    check_list = list(checks) if isinstance(checks, list) else []
    boundary = result.get("descendant_body_candidate_specific_distinctness_basis_emission_boundary", {})
    boundary_map = boundary if isinstance(boundary, Mapping) else {}
    declared = result.get("declared_candidate_specific_distinctness_basis_emission_boundary_question", {})
    declared_map = declared if isinstance(declared, Mapping) else {}
    block = result.get("block", {})
    block_map = block if isinstance(block, Mapping) else {}
    non_claims = result.get("non_claims", {})
    non_claim_map = non_claims if isinstance(non_claims, Mapping) else {}
    return {
        "outcome": result.get("outcome"),
        "block_code": block_map.get("code") or block_map.get("block_code"),
        "block_reason": block_map.get("reason"),
        "candidate_specific_distinctness_basis_emission_boundary_id": boundary_map.get(
            "candidate_specific_distinctness_basis_emission_boundary_id"
        ),
        "question": declared_map.get("candidate_specific_distinctness_basis_emission_boundary_question"),
        "intent": declared_map.get("candidate_specific_distinctness_basis_emission_boundary_intent"),
        "passed_check_count": _passed_check_count(check_list),
        "failed_check_count": _failed_check_count(check_list),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "boundary_type": boundary_map.get("candidate_specific_distinctness_basis_emission_boundary_type"),
        "boundary_version": boundary_map.get("candidate_specific_distinctness_basis_emission_boundary_version"),
        "future_emission_operation_type": boundary_map.get("future_emission_operation_type"),
        "admissible_future_basis_route": boundary_map.get("admissible_future_basis_route"),
        "rupture_class_blocked": boundary_map.get("rupture_class_blocked"),
        "upstream_distinctness_operation_result": boundary_map.get("upstream_distinctness_operation_result"),
        "not_distinct_preserved_as_clean_result": boundary_map.get("not_distinct_preserved_as_clean_result"),
        "candidate_specific_content_missing_upstream": boundary_map.get("candidate_specific_content_missing_upstream"),
        "separate_seal_material_missing_upstream": boundary_map.get("separate_seal_material_missing_upstream"),
        "separate_lineage_receipt_material_missing_upstream": boundary_map.get(
            "separate_lineage_receipt_material_missing_upstream"
        ),
        "separate_digest_material_missing_upstream": boundary_map.get("separate_digest_material_missing_upstream"),
        "scope_division_route_allowed_for_future_operation_shape": boundary_map.get(
            "scope_division_route_allowed_for_future_operation_shape"
        ),
        "divergent_receipt_history_route_authorized": False,
        "carrier_separation_route_authorized": False,
        "cosmetic_substitution_treated_as_basis": False,
        "digest_laundering_treated_as_basis": False,
        "id_role_label_difference_treated_as_basis": False,
        "shared_evidence_treated_as_basis": False,
        "operation_evidence_alone_treated_as_basis": False,
        "future_emission_operation_not_created": boundary_map.get("future_emission_operation_not_created"),
        "candidate_specific_content_not_emitted": boundary_map.get("candidate_specific_content_not_emitted"),
        "separate_seal_material_not_emitted": boundary_map.get("separate_seal_material_not_emitted"),
        "separate_lineage_receipt_material_not_emitted": boundary_map.get(
            "separate_lineage_receipt_material_not_emitted"
        ),
        "separate_digest_material_not_emitted": boundary_map.get("separate_digest_material_not_emitted"),
        "distinctness_operation_not_rerun": boundary_map.get("distinctness_operation_not_rerun"),
        "distinctness_supported_not_recorded": boundary_map.get("distinctness_supported_not_recorded"),
        "candidate_records_not_marked_distinct": boundary_map.get("candidate_records_not_marked_distinct"),
        "candidate_standing_not_authorized": boundary_map.get("candidate_standing_not_authorized"),
        "descendant_bodies_not_created": boundary_map.get("descendant_bodies_not_created"),
        "standing_descendants_not_created": boundary_map.get("standing_descendants_not_created"),
        "first_crossing_not_authorized": boundary_map.get("first_crossing_not_authorized"),
        "relation_not_created": boundary_map.get("relation_not_created"),
        "field_machinery_not_created": boundary_map.get("field_machinery_not_created"),
        "runtime_not_created": boundary_map.get("runtime_not_created"),
        "api_not_created": boundary_map.get("api_not_created"),
        "currentness_not_created": boundary_map.get("currentness_not_created"),
        "authority_not_created": boundary_map.get("authority_not_created"),
        "standing_not_created": boundary_map.get("standing_not_created"),
        "output_not_authorized": boundary_map.get("output_not_authorized"),
        "action_not_authorized": boundary_map.get("action_not_authorized"),
        "derivative_reception_not_authorized": boundary_map.get("derivative_reception_not_authorized"),
        "synchronization_not_authorized": boundary_map.get("synchronization_not_authorized"),
        "follow_on_not_authorized": boundary_map.get("follow_on_not_authorized"),
        "prior_unsupported_claims_validated": False,
        "affected_file_repaired": False,
        "affected_file_edited": False,
        "affected_file_deleted": False,
        "affected_file_overwritten": False,
        "affected_file_replaced": False,
        "affected_file_redeemed": False,
        "affected_file_treated_as_clean_basis": False,
        "contaminated_lineage_treated_as_clean_basis": False,
        "existence_claim_evidence_check_overridden": False,
        "existence_claim_evidence_check_bypassed": False,
        "differentiation_operation_overridden": False,
        "differentiation_operation_bypassed": False,
        "distinctness_operation_boundary_overridden": False,
        "distinctness_operation_boundary_bypassed": False,
        "distinctness_operation_overridden": False,
        "distinctness_operation_bypassed": False,
        "scan_not_performed": boundary_map.get("scan_not_performed"),
        "repository_scan_not_performed": boundary_map.get("repository_scan_not_performed"),
        "repair_not_performed": boundary_map.get("repair_not_performed"),
        "validation_not_enforced": boundary_map.get("validation_not_enforced"),
        "hidden_repair_not_performed": boundary_map.get("hidden_repair_not_performed"),
        "silent_overwrite_not_performed": boundary_map.get("silent_overwrite_not_performed"),
        "boundary_spec_markers_present": boundary_map.get("boundary_spec_markers_present"),
        "completed_distinctness_operation_terminal_summary_markers_present": boundary_map.get(
            "completed_distinctness_operation_terminal_summary_markers_present"
        ),
        "completed_differentiation_operation_terminal_summary_markers_present": boundary_map.get(
            "completed_differentiation_operation_terminal_summary_markers_present"
        ),
        "completed_distinctness_operation_boundary_terminal_summary_markers_present": boundary_map.get(
            "completed_distinctness_operation_boundary_terminal_summary_markers_present"
        ),
        "result_level_non_claims_canonical_false": all(
            non_claim_map.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def write_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    boundary = result.get("descendant_body_candidate_specific_distinctness_basis_emission_boundary", {})
    boundary_id = DEFAULT_BOUNDARY_ID
    if isinstance(boundary, Mapping):
        boundary_id = str(
            boundary.get("candidate_specific_distinctness_basis_emission_boundary_id") or DEFAULT_BOUNDARY_ID
        )
    if output_path is None:
        filename = f"{_safe_filename_part(boundary_id)}__candidate_specific_distinctness_basis_emission_boundary_v0_min_result.json"
        path = OUTPUT_ROOT / filename
    else:
        path = Path(output_path)
        if path.suffix.lower() != ".json":
            filename = f"{_safe_filename_part(boundary_id)}__candidate_specific_distinctness_basis_emission_boundary_v0_min_result.json"
            path = path / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = path
    if final_path.exists():
        stem = final_path.stem
        suffix = final_path.suffix
        index = 1
        while True:
            candidate = final_path.with_name(f"{stem}_{index:03d}{suffix}")
            if not candidate.exists():
                final_path = candidate
                break
            index += 1
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path
