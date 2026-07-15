"""Resolver for one descendant-body candidate non-cosmetic scope declaration operation.

This resolver records only the bounded operation object described by
DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION.
The default live repository posture returns REQUIRES_ADDITIONAL_BASIS because
the current basis line still lacks declared non-cosmetic candidate A scope,
declared non-cosmetic candidate B scope, and a declared basis-bearing scope
division.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateNonCosmeticScopeDivisionDeclarationOperationV0MinError(Exception):
    """Raised for bounded resolver path and JSON handling errors."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min"
)

OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "TWO_NON_STANDING_CANDIDATE_RECORDS_SCOPE_DIVISION_DECLARATION_ONLY"
ADMISSIBLE_FUTURE_ROUTE = "NON_COSMETIC_SCOPE_DIVISION_DECLARATION_ONLY"

OUTCOME_RECORDED = (
    "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_RECORDED"
)
OUTCOME_BLOCKED = (
    "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_BLOCKED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_NOT_RECORDED = (
    "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_NOT_RECORDED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION"
)
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_OPERATION_ID = "descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_001"
DEFAULT_CANDIDATE_A_ID = "descendant_body_basis_candidate_a_001"
DEFAULT_CANDIDATE_B_ID = "descendant_body_basis_candidate_b_001"
DEFAULT_CANDIDATE_A_ROLE = "CANDIDATE_A"
DEFAULT_CANDIDATE_B_ROLE = "CANDIDATE_B"
UPSTREAM_EMISSION_OPERATION_RESULT = "REQUIRES_ADDITIONAL_BASIS"

SCOPE_DECLARATION_POLICY = "REQUIRE_BASIS_BEARING_SCOPE_DIVISION"
SCOPE_LABEL_LAUNDERING_POLICY = "SCOPE_LABEL_LAUNDERING_NOT_BASIS"
COSMETIC_SCOPE_NAMING_POLICY = "COSMETIC_SCOPE_NAMING_NOT_BASIS"
ID_ROLE_LABEL_DIFFERENCE_POLICY = "ID_ROLE_LABEL_DIFFERENCE_NOT_SCOPE_BASIS"
SHARED_EVIDENCE_POLICY = "SHARED_EVIDENCE_NOT_SCOPE_BASIS"
OPERATION_EVIDENCE_POLICY = "OPERATION_EVIDENCE_ALONE_NOT_SCOPE_BASIS"
CONTAMINATED_LINEAGE_POLICY = "CONTAMINATED_LINEAGE_NOT_CLEAN_SCOPE_BASIS"

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_"
    "scope_division_declaration_operation_v0_min"
)

DEFAULT_OPERATION_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_"
    "OPERATION_V0_MIN_SPEC.md"
)
DEFAULT_SCOPE_DIVISION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_"
    "BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SCOPE_DIVISION_BOUNDARY_ARTIFACT_REFERENCE = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_"
    "scope_division_declaration_boundary_v0_min_v3/"
    "descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_001__"
    "candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_result.json"
)
DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_"
    "TERMINAL_SUMMARY_V0.md"
)
DEFAULT_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_"
    "TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "candidate_non_cosmetic_scope_division_declaration_operation_implemented",
    "candidate_non_cosmetic_scope_division_declaration_operation_performed",
    "candidate_non_cosmetic_scope_division_declaration_operation_recorded",
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
    "crossing_authorized",
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
    "candidate_non_cosmetic_scope_division_declaration_operation_recorded",
    "candidate_a_scope_declared",
    "candidate_b_scope_declared",
    "basis_bearing_scope_division_declared",
    "candidate_a_scope_non_cosmetic",
    "candidate_b_scope_non_cosmetic",
    "scope_division_basis_bearing",
    "candidate_a_scope_differs_by_mandate_or_function_or_responsibility_or_governed_surface",
    "candidate_b_scope_differs_by_mandate_or_function_or_responsibility_or_governed_surface",
    "candidate_records_remain_non_standing",
    "candidate_records_remain_not_descendant_bodies",
)

BLOCK_CODES = (
    "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_MALFORMED",
    "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_UNREADABLE",
    "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_INTENT_UNSUPPORTED",
    "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_BLOCK_REQUESTED",
    "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TYPE_MISSING",
    "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TYPE_NOT_EXPECTED",
    "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_VERSION_MISSING",
    "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_VERSION_NOT_0_1_0",
    "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_SCOPE_MISSING",
    "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_SCOPE_NOT_EXPECTED",
    "ADMISSIBLE_FUTURE_ROUTE_MISSING",
    "ADMISSIBLE_FUTURE_ROUTE_NOT_EXPECTED",
    "OPERATION_SPEC_REFERENCE_MISSING",
    "COMPLETED_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "COMPLETED_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "COMPLETED_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "OPERATION_SPEC_MARKER_MISSING",
    "COMPLETED_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "COMPLETED_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "CANDIDATE_RECORD_A_ID_NOT_EXPECTED",
    "CANDIDATE_RECORD_B_ID_NOT_EXPECTED",
    "CANDIDATE_RECORD_A_ROLE_NOT_EXPECTED",
    "CANDIDATE_RECORD_B_ROLE_NOT_EXPECTED",
    "UPSTREAM_EMISSION_OPERATION_RESULT_NOT_REQUIRES_ADDITIONAL_BASIS",
    "REQUIRES_ADDITIONAL_BASIS_NOT_PRESERVED_AS_CLEAN_RESULT",
    "CANDIDATE_A_SCOPE_MISSING_UPSTREAM_NOT_TRUE",
    "CANDIDATE_B_SCOPE_MISSING_UPSTREAM_NOT_TRUE",
    "BASIS_BEARING_SCOPE_DIVISION_MISSING_UPSTREAM_NOT_TRUE",
    "SCOPE_DECLARATION_POLICY_NOT_EXPECTED",
    "SCOPE_LABEL_LAUNDERING_POLICY_NOT_EXPECTED",
    "COSMETIC_SCOPE_NAMING_POLICY_NOT_EXPECTED",
    "ID_ROLE_LABEL_DIFFERENCE_POLICY_NOT_EXPECTED",
    "SHARED_EVIDENCE_POLICY_NOT_EXPECTED",
    "OPERATION_EVIDENCE_POLICY_NOT_EXPECTED",
    "CONTAMINATED_LINEAGE_POLICY_NOT_EXPECTED",
    "CANDIDATE_A_SCOPE_DECLARATION_MISSING",
    "CANDIDATE_B_SCOPE_DECLARATION_MISSING",
    "BASIS_BEARING_SCOPE_DIVISION_DECLARATION_MISSING",
    "CANDIDATE_SCOPE_DECLARATIONS_IDENTICAL",
    "CANDIDATE_SCOPE_DECLARATIONS_COSMETIC_ONLY",
    "BASIS_BEARING_SCOPE_DIVISION_BASIS_MISSING",
    "BASIS_BEARING_SCOPE_DIVISION_BASIS_NOT_NON_COSMETIC",
    "SCOPE_LABEL_LAUNDERING_DETECTED",
    "COSMETIC_SCOPE_NAMING_DETECTED",
    "SCOPE_LABEL_LAUNDERING_TREATED_AS_BASIS_TRUE",
    "COSMETIC_SCOPE_NAMING_TREATED_AS_BASIS_TRUE",
    "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_SCOPE_BASIS_TRUE",
    "SHARED_EVIDENCE_TREATED_AS_SCOPE_BASIS_TRUE",
    "OPERATION_EVIDENCE_ALONE_TREATED_AS_SCOPE_BASIS_TRUE",
    "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_SCOPE_BASIS_TRUE",
    "CANDIDATE_SPECIFIC_CONTENT_EMISSION_ALLOWED_TRUE",
    "SEPARATE_SEAL_MATERIAL_EMISSION_ALLOWED_TRUE",
    "SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMISSION_ALLOWED_TRUE",
    "SEPARATE_DIGEST_MATERIAL_EMISSION_ALLOWED_TRUE",
    "BASIS_EMISSION_OPERATION_RERUN_ALLOWED_TRUE",
    "DISTINCTNESS_OPERATION_RERUN_ALLOWED_TRUE",
    "DISTINCTNESS_SUPPORTED_RECORDING_ALLOWED_TRUE",
    "CANDIDATE_RECORDS_MARKED_DISTINCT_ALLOWED_TRUE",
    "CANDIDATE_STANDING_AUTHORIZED_TRUE",
    "DESCENDANT_BODY_CREATED_TRUE",
    "STANDING_AUTHORIZED_TRUE",
    "CROSSING_AUTHORIZED_TRUE",
    "RELATION_AUTHORIZED_TRUE",
    "FIELD_MACHINERY_AUTHORIZED_TRUE",
    "RUNTIME_AUTHORIZED_TRUE",
    "CURRENTNESS_AUTHORIZED_TRUE",
    "AUTHORITY_AUTHORIZED_TRUE",
    "OUTPUT_AUTHORIZED_TRUE",
    "ACTION_AUTHORIZED_TRUE",
    "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE",
    "SYNCHRONIZATION_AUTHORIZED_TRUE",
    "FOLLOW_ON_AUTHORIZED_TRUE",
    "SCAN_ALLOWED_TRUE",
    "REPAIR_ALLOWED_TRUE",
    "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
    "REQUESTED_CANDIDATE_SPECIFIC_CONTENT_EMISSION",
    "REQUESTED_SEPARATE_SEAL_MATERIAL_EMISSION",
    "REQUESTED_SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMISSION",
    "REQUESTED_SEPARATE_DIGEST_MATERIAL_EMISSION",
    "REQUESTED_BASIS_EMISSION_OPERATION_RERUN",
    "REQUESTED_DISTINCTNESS_OPERATION_RERUN",
    "REQUESTED_DISTINCTNESS_SUPPORTED_RECORDING",
    "REQUESTED_CANDIDATE_RECORDS_MARKED_DISTINCT",
    "REQUESTED_CANDIDATE_STANDING_AUTHORIZATION",
    "REQUESTED_DESCENDANT_BODY_CREATION",
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
    "REQUESTED_REPOSITORY_SCAN",
    "REQUESTED_FILE_DISCOVERY",
    "REQUESTED_AFFECTED_FILE_REPAIR",
    "REQUESTED_AFFECTED_FILE_MUTATION",
    "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION",
    "REQUESTED_UPSTREAM_OVERRIDE_OR_BYPASS",
    "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
    "NON_CLAIM_MISSING_OR_FLIPPED",
)

REFERENCE_FIELDS_AND_CODES = (
    ("operation_spec_reference", "OPERATION_SPEC_REFERENCE_MISSING"),
    (
        "completed_scope_division_declaration_boundary_terminal_summary_reference",
        "COMPLETED_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    ),
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

FALSE_FIELD_CODES = {
    "candidate_specific_content_emission_allowed": "CANDIDATE_SPECIFIC_CONTENT_EMISSION_ALLOWED_TRUE",
    "separate_seal_material_emission_allowed": "SEPARATE_SEAL_MATERIAL_EMISSION_ALLOWED_TRUE",
    "separate_lineage_receipt_material_emission_allowed": (
        "SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMISSION_ALLOWED_TRUE"
    ),
    "separate_digest_material_emission_allowed": "SEPARATE_DIGEST_MATERIAL_EMISSION_ALLOWED_TRUE",
    "basis_emission_operation_rerun_allowed": "BASIS_EMISSION_OPERATION_RERUN_ALLOWED_TRUE",
    "distinctness_operation_rerun_allowed": "DISTINCTNESS_OPERATION_RERUN_ALLOWED_TRUE",
    "distinctness_supported_recording_allowed": "DISTINCTNESS_SUPPORTED_RECORDING_ALLOWED_TRUE",
    "candidate_records_marked_distinct_allowed": "CANDIDATE_RECORDS_MARKED_DISTINCT_ALLOWED_TRUE",
    "candidate_standing_authorized": "CANDIDATE_STANDING_AUTHORIZED_TRUE",
    "descendant_body_created": "DESCENDANT_BODY_CREATED_TRUE",
    "standing_authorized": "STANDING_AUTHORIZED_TRUE",
    "crossing_authorized": "CROSSING_AUTHORIZED_TRUE",
    "relation_authorized": "RELATION_AUTHORIZED_TRUE",
    "field_machinery_authorized": "FIELD_MACHINERY_AUTHORIZED_TRUE",
    "runtime_authorized": "RUNTIME_AUTHORIZED_TRUE",
    "currentness_authorized": "CURRENTNESS_AUTHORIZED_TRUE",
    "authority_authorized": "AUTHORITY_AUTHORIZED_TRUE",
    "output_authorized": "OUTPUT_AUTHORIZED_TRUE",
    "action_authorized": "ACTION_AUTHORIZED_TRUE",
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE",
    "synchronization_authorized": "SYNCHRONIZATION_AUTHORIZED_TRUE",
    "follow_on_authorized": "FOLLOW_ON_AUTHORIZED_TRUE",
    "scan_allowed": "SCAN_ALLOWED_TRUE",
    "repair_allowed": "REPAIR_ALLOWED_TRUE",
    "validation_enforcement_allowed": "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
}

PROHIBITED_REQUEST_CODES = {
    "define_or_implement_another_operation": "REQUESTED_UPSTREAM_OVERRIDE_OR_BYPASS",
    "requested_candidate_specific_content_emission": "REQUESTED_CANDIDATE_SPECIFIC_CONTENT_EMISSION",
    "requested_separate_seal_material_emission": "REQUESTED_SEPARATE_SEAL_MATERIAL_EMISSION",
    "requested_separate_lineage_receipt_material_emission": (
        "REQUESTED_SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMISSION"
    ),
    "requested_separate_digest_material_emission": "REQUESTED_SEPARATE_DIGEST_MATERIAL_EMISSION",
    "requested_basis_emission_operation_rerun": "REQUESTED_BASIS_EMISSION_OPERATION_RERUN",
    "requested_distinctness_operation_rerun": "REQUESTED_DISTINCTNESS_OPERATION_RERUN",
    "requested_distinctness_supported_recording": "REQUESTED_DISTINCTNESS_SUPPORTED_RECORDING",
    "requested_candidate_records_marked_distinct": "REQUESTED_CANDIDATE_RECORDS_MARKED_DISTINCT",
    "requested_candidate_standing_authorization": "REQUESTED_CANDIDATE_STANDING_AUTHORIZATION",
    "requested_descendant_body_creation": "REQUESTED_DESCENDANT_BODY_CREATION",
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
    "requested_repository_scan": "REQUESTED_REPOSITORY_SCAN",
    "requested_file_discovery": "REQUESTED_FILE_DISCOVERY",
    "requested_affected_file_repair": "REQUESTED_AFFECTED_FILE_REPAIR",
    "requested_affected_file_mutation": "REQUESTED_AFFECTED_FILE_MUTATION",
    "requested_prior_unsupported_claim_validation": "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION",
    "requested_upstream_override_or_bypass": "REQUESTED_UPSTREAM_OVERRIDE_OR_BYPASS",
    "requested_raw_markdown_body_return": "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
}

SCOPE_FIELDS = (
    "candidate_a_scope_id",
    "candidate_b_scope_id",
    "candidate_a_scope_statement",
    "candidate_b_scope_statement",
    "candidate_a_scope_basis",
    "candidate_b_scope_basis",
    "basis_bearing_scope_division_statement",
    "basis_bearing_scope_division_basis",
)

NON_COSMETIC_BASIS_TERMS = ("mandate", "function", "responsibility", "governed surface")
COSMETIC_ONLY_TERMS = (
    "candidate id",
    "candidate role",
    "role label",
    "label only",
    "side only",
    "order only",
    "filename",
    "display name",
    "variable name",
    "assigned name",
    "template slot",
    "string replacement",
)

SENSITIVE_BODY_KEYS = {
    "raw_body",
    "full_body",
    "markdown_body",
    "hidden_repo_state",
    "local_cache",
    "current_working_tree",
}

OPERATION_SPEC_MARKERS: tuple[tuple[str | tuple[str, ...], ...], ...] = (
    ("Descendant Body Candidate Non-Cosmetic Scope Division Declaration Operation V0 Minimum Specification",),
    ("This file defines one future candidate non-cosmetic scope-division declaration operation.",),
    ("This file is operation-spec-only.",),
    (
        "This file does not implement or perform the operation.",
        ("This file does not implement the operation.", "This file does not perform the operation."),
    ),
    (
        "This file does not declare candidate A scope, candidate B scope, or basis-bearing scope division.",
        (
            "This file does not declare candidate A scope.",
            "This file does not declare candidate B scope.",
            "This file does not declare basis-bearing scope division.",
        ),
    ),
    ("Scope declaration is not scope standing.",),
    ("Scope declaration is not candidate-specific basis emission.",),
    ("Scope declaration is not distinctness support.",),
    ("A scope label is not a scope.",),
    ("A scope title is not a mandate.",),
    ("A scope id is not a governed surface.",),
    ("Scope division must be basis-bearing, not label-bearing.",),
    ("Candidate-specific basis must be basis-bearing, not label-bearing.",),
    (
        "candidate_non_cosmetic_scope_division_declaration_operation_type = "
        "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION",
    ),
    (
        "candidate_non_cosmetic_scope_division_declaration_operation_scope = "
        "TWO_NON_STANDING_CANDIDATE_RECORDS_SCOPE_DIVISION_DECLARATION_ONLY",
    ),
    ("admissible_future_route = NON_COSMETIC_SCOPE_DIVISION_DECLARATION_ONLY",),
    ("candidate_non_cosmetic_scope_division_declaration_operation_recorded = false",),
    ("candidate_a_scope_declared = false",),
    ("candidate_b_scope_declared = false",),
    ("basis_bearing_scope_division_declared = false",),
    ("scope_label_laundering_treated_as_basis = false",),
    ("cosmetic_scope_naming_treated_as_basis = false",),
    ("id_role_label_difference_treated_as_scope_basis = false",),
    ("shared_evidence_treated_as_scope_basis = false",),
    ("operation_evidence_alone_treated_as_scope_basis = false",),
    ("contaminated_lineage_treated_as_clean_scope_basis = false",),
)

BOUNDARY_SUMMARY_MARKERS: tuple[tuple[str | tuple[str, ...], ...], ...] = (
    ("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",),
    ("RECORDED as the live v3 boundary outcome",),
    ("failed_check_count = 0", "failed_check_count 0"),
    ("result_version = 0.3.0", "result_version 0.3.0"),
    (
        "resolver_module = resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3",
        "resolver_module resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3",
    ),
    (
        "future_scope_declaration_operation_type = "
        "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION",
        "future_scope_declaration_operation_type "
        "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION",
    ),
    ("rupture_class_blocked = SCOPE_LABEL_LAUNDERING", "rupture_class_blocked SCOPE_LABEL_LAUNDERING"),
    ("candidate_a_scope_missing_upstream = true", "candidate_a_scope_missing_upstream true"),
    ("candidate_b_scope_missing_upstream = true", "candidate_b_scope_missing_upstream true"),
    (
        "basis_bearing_scope_division_missing_upstream = true",
        "basis_bearing_scope_division_missing_upstream true",
    ),
    (
        "future_scope_declaration_operation_shape_allowed = true",
        "future_scope_declaration_operation_shape_allowed true",
    ),
    ("candidate_a_scope_not_declared = true", "candidate_a_scope_not_declared true"),
    ("candidate_b_scope_not_declared = true", "candidate_b_scope_not_declared true"),
    (
        "basis_bearing_scope_division_not_declared = true",
        "basis_bearing_scope_division_not_declared true",
    ),
    ("scope_label_laundering_not_allowed = true", "scope_label_laundering_not_allowed true"),
    ("Scope declaration is not scope standing",),
    ("A scope label is not a scope",),
    ("Scope division must be basis-bearing, not label-bearing",),
)

BASIS_EMISSION_OPERATION_MARKERS: tuple[tuple[str | tuple[str, ...], ...], ...] = (
    ("DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS",),
    ("REQUIRES_ADDITIONAL_BASIS",),
    ("missing non-cosmetic candidate A scope",),
    ("missing non-cosmetic candidate B scope",),
    ("missing basis-bearing scope division",),
    ("material_emitted = false", "material_emitted false", "candidate_specific_content_emitted = false"),
    ("candidate_specific_content_emitted = false", "candidate_specific_content_emitted false"),
    ("distinctness_operation_rerun = false", "distinctness_operation_rerun false"),
    ("distinctness_supported_recorded = false", "distinctness_supported_recorded false"),
    ("candidate_records_marked_distinct = false", "candidate_records_marked_distinct false"),
    ("candidate_standing_authorized = false", "candidate_standing_authorized false"),
    ("descendant_body_created = false", "descendant_body_created false"),
)

DISTINCTNESS_OPERATION_MARKERS: tuple[tuple[str | tuple[str, ...], ...], ...] = (
    ("DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",),
    ("distinctness_result = NOT_DISTINCT", "distinctness_result NOT_DISTINCT"),
    ("failed_check_count = 0", "failed_check_count 0"),
    ("candidate_record_count_compared = 2", "candidate_record_count_compared 2"),
    ("distinctness_supported = false", "distinctness_supported false"),
    ("NOT_DISTINCT is a clean operation result, not a failure",),
    ("id and role difference alone is not distinctness", "Id and role difference alone are not distinctness"),
    ("shared evidence reference alone is not distinctness", "Shared evidence reference alone is not distinctness"),
    ("Operation evidence alone is not distinctness", "operation evidence alone is not distinctness"),
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _deepcopy_mapping(value: Mapping[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(dict(value))


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _safe_json_filename_part(value: Any) -> str:
    text = str(value or DEFAULT_OPERATION_ID)
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in text)
    safe = safe.strip("._-") or DEFAULT_OPERATION_ID
    return safe[:160]


def _resolve_declared_path(value: Any) -> Path | None:
    if not _is_non_empty_string(value):
        return None
    path = Path(str(value))
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def _read_declared_text(value: Any) -> str | None:
    path = _resolve_declared_path(value)
    if path is None:
        return None
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def _marker_alternative_present(text: str, alternative: str | tuple[str, ...]) -> bool:
    if isinstance(alternative, tuple):
        return all(part in text for part in alternative)
    return alternative in text


def _marker_group_present(text: str, group: tuple[str | tuple[str, ...], ...]) -> bool:
    return any(_marker_alternative_present(text, alternative) for alternative in group)


def _all_marker_groups_present(
    text: str | None,
    groups: tuple[tuple[str | tuple[str, ...], ...], ...],
) -> tuple[bool, list[int]]:
    if text is None:
        return False, list(range(len(groups)))
    missing = [index for index, group in enumerate(groups) if not _marker_group_present(text, group)]
    return not missing, missing


def _differentiation_posture_classes_present(text: str | None) -> tuple[bool, list[str]]:
    if text is None:
        return False, [
            "completion",
            "exactly_two_candidates",
            "non_standing_not_descendant_bodies",
            "standing_descendant_creation_not_authorized",
            "crossing_relation_not_authorized",
        ]
    lowered = text.lower()
    classes = {
        "completion": "descendant_body_differentiation_operation" in lowered
        or "differentiation operation" in lowered,
        "exactly_two_candidates": "exactly two" in lowered and "candidate" in lowered,
        "non_standing_not_descendant_bodies": "non-standing" in lowered
        and ("not descendant bodies" in lowered or "descendant_body_created = false" in lowered),
        "standing_descendant_creation_not_authorized": (
            "standing_authorized = false" in lowered
            or "candidate standing not authorized" in lowered
            or "standing not authorized" in lowered
        )
        and ("descendant" in lowered),
        "crossing_relation_not_authorized": "crossing" in lowered
        and "relation" in lowered
        and ("not authorized" in lowered or "= false" in lowered),
    }
    missing = [name for name, present in classes.items() if not present]
    return not missing, missing


def _is_sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return lowered in SENSITIVE_BODY_KEYS or lowered.endswith("_body")


def _compact_text(value: str, limit: int = 420) -> str:
    text = value.strip()
    if len(text) <= limit:
        return text
    return f"{text[:limit]}...[truncated]"


def _sanitize_json_value(value: Any, key: str = "") -> Any:
    if _is_sensitive_key(key):
        return "[REDACTED_SENSITIVE_BODY]"
    if isinstance(value, Mapping):
        return {str(k): _sanitize_json_value(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize_json_value(item, key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize_json_value(item, key) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        return _compact_text(value)
    return value


def _json_ready(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(k): _json_ready(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize_json_value(expected_posture),
        "actual_posture": _sanitize_json_value(actual_posture),
    }
    if not passed and code:
        record["block_code"] = code
        record["failure_code"] = code
    checks.append(record)


def _failed_codes(checks: list[dict[str, Any]]) -> list[str]:
    codes: list[str] = []
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code in BLOCK_CODES:
                codes.append(code)
    return codes


def _validate_exact(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    field: str,
    expected: Any,
    check_name: str,
    missing_code: str,
    mismatch_code: str,
) -> None:
    actual = request.get(field)
    if actual is None:
        _add_check(checks, check_name, False, expected, actual, missing_code)
        return
    _add_check(checks, check_name, actual == expected, expected, actual, mismatch_code)


def _validate_bool_exact(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    field: str,
    expected: bool,
    check_name: str,
    code: str,
) -> None:
    actual = request.get(field)
    _add_check(checks, check_name, actual is expected, expected, actual, code)


def _validate_reference_declared(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    field: str,
    code: str,
) -> None:
    actual = request.get(field)
    _add_check(
        checks,
        f"{field} declared",
        _is_non_empty_string(actual),
        "non-empty declared path reference",
        actual,
        code,
    )


def _validate_marker_file(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    field: str,
    check_name: str,
    marker_groups: tuple[tuple[str | tuple[str, ...], ...], ...],
    code: str,
) -> bool:
    text = _read_declared_text(request.get(field))
    passed, missing = _all_marker_groups_present(text, marker_groups)
    _add_check(
        checks,
        check_name,
        passed,
        "all required marker groups present",
        {"missing_marker_group_indexes": missing},
        code,
    )
    return passed


def _validate_differentiation_file(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
) -> bool:
    text = _read_declared_text(request.get("completed_differentiation_operation_terminal_summary_reference"))
    passed, missing = _differentiation_posture_classes_present(text)
    _add_check(
        checks,
        "differentiation operation terminal summary posture classes present",
        passed,
        "completion, exactly-two, non-standing, no standing, no crossing/relation classes",
        {"missing_posture_classes": missing},
        "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    )
    return passed


def _scope_value(request: Mapping[str, Any], field: str) -> str:
    value = request.get(field)
    if not isinstance(value, str):
        return ""
    return value.strip()


def _missing_scope_basis(request: Mapping[str, Any]) -> list[str]:
    missing: list[str] = []
    if not _scope_value(request, "candidate_a_scope_id") or not _scope_value(
        request, "candidate_a_scope_statement"
    ) or not _scope_value(request, "candidate_a_scope_basis"):
        missing.append("missing non-cosmetic candidate A scope declaration")
    if not _scope_value(request, "candidate_b_scope_id") or not _scope_value(
        request, "candidate_b_scope_statement"
    ) or not _scope_value(request, "candidate_b_scope_basis"):
        missing.append("missing non-cosmetic candidate B scope declaration")
    if not _scope_value(request, "basis_bearing_scope_division_statement") or not _scope_value(
        request, "basis_bearing_scope_division_basis"
    ):
        missing.append("missing basis-bearing scope division declaration")
    return missing


def _normalized_scope_text(value: str) -> str:
    lowered = " ".join(value.lower().split())
    replacements = (
        ("candidate a", "candidate"),
        ("candidate b", "candidate"),
        ("candidate_a", "candidate"),
        ("candidate_b", "candidate"),
        ("record a", "record"),
        ("record b", "record"),
        ("_a_", "_x_"),
        ("_b_", "_x_"),
        (" a ", " x "),
        (" b ", " x "),
    )
    for old, new in replacements:
        lowered = lowered.replace(old, new)
    return lowered


def _combined_scope_basis_text(request: Mapping[str, Any]) -> str:
    parts = [
        _scope_value(request, "candidate_a_scope_statement"),
        _scope_value(request, "candidate_b_scope_statement"),
        _scope_value(request, "candidate_a_scope_basis"),
        _scope_value(request, "candidate_b_scope_basis"),
        _scope_value(request, "basis_bearing_scope_division_statement"),
        _scope_value(request, "basis_bearing_scope_division_basis"),
    ]
    value = request.get("declared_scope_basis")
    if isinstance(value, str):
        parts.append(value)
    return "\n".join(parts).lower()


def _basis_names_non_cosmetic_category(request: Mapping[str, Any]) -> bool:
    text = _combined_scope_basis_text(request)
    return any(term in text for term in NON_COSMETIC_BASIS_TERMS)


def _basis_is_cosmetic_only(request: Mapping[str, Any]) -> bool:
    text = _combined_scope_basis_text(request)
    return any(term in text for term in COSMETIC_ONLY_TERMS) and not _basis_names_non_cosmetic_category(request)


def _basis_references_contaminated_lineage(request: Mapping[str, Any]) -> bool:
    text = _combined_scope_basis_text(request)
    return "descendant_body_basis_derivation_event_v0_min_spec" in text or "contaminated lineage" in text


def _basis_references_shared_evidence_alone(request: Mapping[str, Any]) -> bool:
    text = _combined_scope_basis_text(request)
    return "shared evidence alone" in text or "shared evidence reference alone" in text


def _basis_references_operation_evidence_alone(request: Mapping[str, Any]) -> bool:
    text = _combined_scope_basis_text(request)
    return "operation evidence alone" in text


def _operation_marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    names = {
        "operation_spec_markers_present": "operation spec markers present",
        "completed_scope_division_declaration_boundary_terminal_summary_markers_present": (
            "scope-division declaration boundary terminal summary markers present"
        ),
        "completed_basis_emission_operation_terminal_summary_markers_present": (
            "basis emission operation terminal summary markers present"
        ),
        "completed_distinctness_operation_terminal_summary_markers_present": (
            "distinctness operation terminal summary markers present"
        ),
        "completed_differentiation_operation_terminal_summary_markers_present": (
            "differentiation operation terminal summary posture classes present"
        ),
    }
    flags: dict[str, bool] = {}
    for field, check_name in names.items():
        flags[field] = any(
            check.get("check_name") == check_name and check.get("passed") is True for check in checks
        )
    return flags


def _build_operation_object(
    request: Mapping[str, Any],
    recorded: bool,
    marker_flags: Mapping[str, bool],
) -> dict[str, Any]:
    candidate_a_scope_declared = recorded
    candidate_b_scope_declared = recorded
    scope_division_declared = recorded
    return {
        "candidate_non_cosmetic_scope_division_declaration_operation_id": request.get(
            "candidate_non_cosmetic_scope_division_declaration_operation_id", DEFAULT_OPERATION_ID
        ),
        "candidate_non_cosmetic_scope_division_declaration_operation_type": request.get(
            "candidate_non_cosmetic_scope_division_declaration_operation_type", OPERATION_TYPE
        ),
        "candidate_non_cosmetic_scope_division_declaration_operation_version": request.get(
            "candidate_non_cosmetic_scope_division_declaration_operation_version", OPERATION_VERSION
        ),
        "candidate_non_cosmetic_scope_division_declaration_operation_scope": request.get(
            "candidate_non_cosmetic_scope_division_declaration_operation_scope", OPERATION_SCOPE
        ),
        "admissible_future_route": request.get("admissible_future_route", ADMISSIBLE_FUTURE_ROUTE),
        "upstream_emission_operation_result": request.get(
            "upstream_emission_operation_result", UPSTREAM_EMISSION_OPERATION_RESULT
        ),
        "requires_additional_basis_preserved_as_clean_result": request.get(
            "requires_additional_basis_preserved_as_clean_result", True
        )
        is True,
        "candidate_a_scope_missing_upstream": request.get("candidate_a_scope_missing_upstream", True)
        is True,
        "candidate_b_scope_missing_upstream": request.get("candidate_b_scope_missing_upstream", True)
        is True,
        "basis_bearing_scope_division_missing_upstream": request.get(
            "basis_bearing_scope_division_missing_upstream", True
        )
        is True,
        "candidate_non_cosmetic_scope_division_declaration_operation_recorded": recorded,
        "candidate_a_scope_declared": candidate_a_scope_declared,
        "candidate_b_scope_declared": candidate_b_scope_declared,
        "basis_bearing_scope_division_declared": scope_division_declared,
        "candidate_a_scope_id": _sanitize_json_value(request.get("candidate_a_scope_id", "")),
        "candidate_b_scope_id": _sanitize_json_value(request.get("candidate_b_scope_id", "")),
        "candidate_a_scope_statement_reference": _sanitize_json_value(
            request.get("candidate_a_scope_statement", "")
        ),
        "candidate_b_scope_statement_reference": _sanitize_json_value(
            request.get("candidate_b_scope_statement", "")
        ),
        "candidate_a_scope_basis_reference": _sanitize_json_value(
            request.get("candidate_a_scope_basis", "")
        ),
        "candidate_b_scope_basis_reference": _sanitize_json_value(
            request.get("candidate_b_scope_basis", "")
        ),
        "basis_bearing_scope_division_statement_reference": _sanitize_json_value(
            request.get("basis_bearing_scope_division_statement", "")
        ),
        "basis_bearing_scope_division_basis_reference": _sanitize_json_value(
            request.get("basis_bearing_scope_division_basis", "")
        ),
        "candidate_a_scope_non_cosmetic": recorded,
        "candidate_b_scope_non_cosmetic": recorded,
        "scope_division_basis_bearing": recorded,
        "candidate_a_scope_differs_by_mandate_or_function_or_responsibility_or_governed_surface": recorded,
        "candidate_b_scope_differs_by_mandate_or_function_or_responsibility_or_governed_surface": recorded,
        "scope_label_laundering_detected": bool(request.get("scope_label_laundering_detected") is True),
        "scope_label_laundering_treated_as_basis": False,
        "cosmetic_scope_naming_detected": bool(request.get("cosmetic_scope_naming_detected") is True),
        "cosmetic_scope_naming_treated_as_basis": False,
        "id_role_label_difference_treated_as_scope_basis": False,
        "shared_evidence_treated_as_scope_basis": False,
        "operation_evidence_alone_treated_as_scope_basis": False,
        "contaminated_lineage_treated_as_clean_scope_basis": False,
        "candidate_specific_content_emitted": False,
        "separate_seal_material_emitted": False,
        "separate_lineage_receipt_material_emitted": False,
        "separate_digest_material_emitted": False,
        "basis_emission_operation_rerun": False,
        "distinctness_operation_rerun": False,
        "distinctness_supported_recorded": False,
        "candidate_records_marked_distinct": False,
        "candidate_records_remain_non_standing": True,
        "candidate_records_remain_not_descendant_bodies": True,
        "candidate_standing_authorized": False,
        "descendant_body_created": False,
        "standing_authorized": False,
        "crossing_authorized": False,
        "relation_authorized": False,
        "field_machinery_authorized": False,
        "runtime_authorized": False,
        "currentness_authorized": False,
        "authority_authorized": False,
        "output_authorized": False,
        "action_authorized": False,
        "derivative_reception_authorized": False,
        "synchronization_authorized": False,
        "follow_on_authorized": False,
        "operation_spec_markers_present": bool(marker_flags.get("operation_spec_markers_present")),
        "completed_scope_division_declaration_boundary_terminal_summary_markers_present": bool(
            marker_flags.get(
                "completed_scope_division_declaration_boundary_terminal_summary_markers_present"
            )
        ),
        "completed_basis_emission_operation_terminal_summary_markers_present": bool(
            marker_flags.get("completed_basis_emission_operation_terminal_summary_markers_present")
        ),
        "completed_distinctness_operation_terminal_summary_markers_present": bool(
            marker_flags.get("completed_distinctness_operation_terminal_summary_markers_present")
        ),
        "completed_differentiation_operation_terminal_summary_markers_present": bool(
            marker_flags.get("completed_differentiation_operation_terminal_summary_markers_present")
        ),
    }


def _build_statement(operation: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    return {
        "outcome": outcome,
        "candidate_non_cosmetic_scope_division_declaration_operation_recorded": operation[
            "candidate_non_cosmetic_scope_division_declaration_operation_recorded"
        ],
        "candidate_a_scope_declared": operation["candidate_a_scope_declared"],
        "candidate_b_scope_declared": operation["candidate_b_scope_declared"],
        "basis_bearing_scope_division_declared": operation["basis_bearing_scope_division_declared"],
        "candidate_specific_content_emitted": False,
        "separate_seal_material_emitted": False,
        "separate_lineage_receipt_material_emitted": False,
        "separate_digest_material_emitted": False,
        "basis_emission_operation_rerun": False,
        "distinctness_operation_rerun": False,
        "distinctness_supported_recorded": False,
        "candidate_records_marked_distinct": False,
        "candidate_records_remain_non_standing": True,
        "candidate_records_remain_not_descendant_bodies": True,
        "candidate_standing_authorized": False,
        "descendant_body_created": False,
        "crossing_authorized": False,
        "relation_authorized": False,
        "runtime_authorized": False,
        "currentness_authorized": False,
        "authority_authorized": False,
        "follow_on_authorized": False,
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "not_candidate_specific_content_emission": True,
        "not_seal_material_emission": True,
        "not_lineage_receipt_material_emission": True,
        "not_digest_material_emission": True,
        "not_basis_emission_rerun": True,
        "not_distinctness_rerun": True,
        "not_distinctness_supported": True,
        "not_candidate_records_marked_distinct": True,
        "not_candidate_standing": True,
        "not_descendant_body_creation": True,
        "not_crossing": True,
        "not_relation": True,
        "not_field_machinery": True,
        "not_runtime": True,
        "not_currentness": True,
        "not_authority": True,
        "not_follow_on": True,
    }


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    additional_basis_required: list[str] | None = None,
    not_recorded_basis: list[str] | None = None,
    recorded: bool = False,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    marker_flags = _operation_marker_flags(checks)
    operation = _build_operation_object(request, recorded, marker_flags)
    failed_check_count = sum(1 for check in checks if check.get("passed") is False)
    passed_check_count = sum(1 for check in checks if check.get("passed") is True)
    operation_id = operation["candidate_non_cosmetic_scope_division_declaration_operation_id"]
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": block_code if outcome == OUTCOME_BLOCKED else None,
        "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
        "reason": block_reason if outcome == OUTCOME_BLOCKED else None,
    }
    result: dict[str, Any] = {
        "candidate_non_cosmetic_scope_division_declaration_operation_metadata": {
            "candidate_non_cosmetic_scope_division_declaration_operation_id": operation_id,
            "operation_type": OPERATION_TYPE,
            "result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_candidate_non_cosmetic_scope_division_declaration_operation_basis": _sanitize_json_value(
            request
        ),
        "upstream_basis": {
            "operation_spec_reference": request.get("operation_spec_reference"),
            "completed_scope_division_declaration_boundary_terminal_summary_reference": request.get(
                "completed_scope_division_declaration_boundary_terminal_summary_reference"
            ),
            "completed_scope_division_declaration_boundary_artifact_reference": request.get(
                "completed_scope_division_declaration_boundary_artifact_reference"
            ),
            "completed_basis_emission_operation_terminal_summary_reference": request.get(
                "completed_basis_emission_operation_terminal_summary_reference"
            ),
            "completed_basis_emission_boundary_terminal_summary_reference": request.get(
                "completed_basis_emission_boundary_terminal_summary_reference"
            ),
            "completed_distinctness_operation_terminal_summary_reference": request.get(
                "completed_distinctness_operation_terminal_summary_reference"
            ),
            "completed_differentiation_operation_terminal_summary_reference": request.get(
                "completed_differentiation_operation_terminal_summary_reference"
            ),
            **marker_flags,
        },
        "descendant_body_candidate_non_cosmetic_scope_division_declaration_operation": operation,
        "candidate_non_cosmetic_scope_division_declaration_operation_checks": checks,
        "candidate_non_cosmetic_scope_division_declaration_operation_statement": _build_statement(
            operation, outcome
        ),
        "candidate_non_cosmetic_scope_division_declaration_operation_non_meaning": _build_non_meaning(),
        "additional_basis_required": additional_basis_required or [],
        "not_recorded_basis": not_recorded_basis or [],
        "what_remains_open": [
            "candidate non-cosmetic scope-division declaration resolver successor work if separately selected",
            "candidate-specific distinctness basis emission operation successor if separately bounded",
            "actual candidate-specific content emission",
            "actual separate seal material emission",
            "actual separate lineage receipt material emission",
            "actual separate digest material emission",
            "future distinctness-supported operation result if separately supported",
            "candidate standing check",
            "first crossing",
            "relation",
            "FIELD machinery",
            "runtime",
            "currentness",
            "authority",
            "output authorization",
            "action authorization",
            "derivative reception",
            "synchronization",
            "follow-on work",
        ],
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["candidate_non_cosmetic_scope_division_declaration_operation_summary"] = (
        build_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_summary(
            {
                **result,
                "candidate_non_cosmetic_scope_division_declaration_operation_summary": {},
                "_passed_check_count": passed_check_count,
                "_failed_check_count": failed_check_count,
            }
        )
    )
    return result


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        additional_basis_required=[],
        not_recorded_basis=[],
        recorded=False,
        block_code=code,
        block_reason=reason,
    )


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
    malformed = [
        key for key in REQUIRED_FALSE_NON_CLAIMS if key not in declared or declared.get(key) is not False
    ]
    _add_check(
        checks,
        "required non-claims false",
        not malformed,
        "every required false non-claim present and exactly false",
        {"malformed_keys": malformed},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _validate_request(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    _validate_exact(
        checks,
        request,
        "candidate_non_cosmetic_scope_division_declaration_operation_type",
        OPERATION_TYPE,
        "operation type exact",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TYPE_MISSING",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TYPE_NOT_EXPECTED",
    )
    _validate_exact(
        checks,
        request,
        "candidate_non_cosmetic_scope_division_declaration_operation_version",
        OPERATION_VERSION,
        "operation version exact",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_VERSION_MISSING",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_VERSION_NOT_0_1_0",
    )
    _validate_exact(
        checks,
        request,
        "candidate_non_cosmetic_scope_division_declaration_operation_scope",
        OPERATION_SCOPE,
        "operation scope exact",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_SCOPE_MISSING",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_SCOPE_NOT_EXPECTED",
    )
    _validate_exact(
        checks,
        request,
        "admissible_future_route",
        ADMISSIBLE_FUTURE_ROUTE,
        "admissible future route exact",
        "ADMISSIBLE_FUTURE_ROUTE_MISSING",
        "ADMISSIBLE_FUTURE_ROUTE_NOT_EXPECTED",
    )
    for field, code in REFERENCE_FIELDS_AND_CODES:
        _validate_reference_declared(checks, request, field, code)
    _validate_marker_file(
        checks,
        request,
        "operation_spec_reference",
        "operation spec markers present",
        OPERATION_SPEC_MARKERS,
        "OPERATION_SPEC_MARKER_MISSING",
    )
    _validate_marker_file(
        checks,
        request,
        "completed_scope_division_declaration_boundary_terminal_summary_reference",
        "scope-division declaration boundary terminal summary markers present",
        BOUNDARY_SUMMARY_MARKERS,
        "COMPLETED_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    )
    _validate_marker_file(
        checks,
        request,
        "completed_basis_emission_operation_terminal_summary_reference",
        "basis emission operation terminal summary markers present",
        BASIS_EMISSION_OPERATION_MARKERS,
        "COMPLETED_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    )
    _validate_marker_file(
        checks,
        request,
        "completed_distinctness_operation_terminal_summary_reference",
        "distinctness operation terminal summary markers present",
        DISTINCTNESS_OPERATION_MARKERS,
        "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    )
    _validate_differentiation_file(checks, request)
    _validate_exact(
        checks,
        request,
        "candidate_record_a_id",
        DEFAULT_CANDIDATE_A_ID,
        "candidate record A id exact",
        "CANDIDATE_RECORD_A_ID_NOT_EXPECTED",
        "CANDIDATE_RECORD_A_ID_NOT_EXPECTED",
    )
    _validate_exact(
        checks,
        request,
        "candidate_record_b_id",
        DEFAULT_CANDIDATE_B_ID,
        "candidate record B id exact",
        "CANDIDATE_RECORD_B_ID_NOT_EXPECTED",
        "CANDIDATE_RECORD_B_ID_NOT_EXPECTED",
    )
    _validate_exact(
        checks,
        request,
        "candidate_record_a_role",
        DEFAULT_CANDIDATE_A_ROLE,
        "candidate record A role exact",
        "CANDIDATE_RECORD_A_ROLE_NOT_EXPECTED",
        "CANDIDATE_RECORD_A_ROLE_NOT_EXPECTED",
    )
    _validate_exact(
        checks,
        request,
        "candidate_record_b_role",
        DEFAULT_CANDIDATE_B_ROLE,
        "candidate record B role exact",
        "CANDIDATE_RECORD_B_ROLE_NOT_EXPECTED",
        "CANDIDATE_RECORD_B_ROLE_NOT_EXPECTED",
    )
    _validate_exact(
        checks,
        request,
        "upstream_emission_operation_result",
        UPSTREAM_EMISSION_OPERATION_RESULT,
        "upstream emission operation result is REQUIRES_ADDITIONAL_BASIS",
        "UPSTREAM_EMISSION_OPERATION_RESULT_NOT_REQUIRES_ADDITIONAL_BASIS",
        "UPSTREAM_EMISSION_OPERATION_RESULT_NOT_REQUIRES_ADDITIONAL_BASIS",
    )
    _validate_bool_exact(
        checks,
        request,
        "requires_additional_basis_preserved_as_clean_result",
        True,
        "REQUIRES_ADDITIONAL_BASIS preserved as clean result",
        "REQUIRES_ADDITIONAL_BASIS_NOT_PRESERVED_AS_CLEAN_RESULT",
    )
    _validate_bool_exact(
        checks,
        request,
        "candidate_a_scope_missing_upstream",
        True,
        "candidate A scope missing upstream true",
        "CANDIDATE_A_SCOPE_MISSING_UPSTREAM_NOT_TRUE",
    )
    _validate_bool_exact(
        checks,
        request,
        "candidate_b_scope_missing_upstream",
        True,
        "candidate B scope missing upstream true",
        "CANDIDATE_B_SCOPE_MISSING_UPSTREAM_NOT_TRUE",
    )
    _validate_bool_exact(
        checks,
        request,
        "basis_bearing_scope_division_missing_upstream",
        True,
        "basis-bearing scope division missing upstream true",
        "BASIS_BEARING_SCOPE_DIVISION_MISSING_UPSTREAM_NOT_TRUE",
    )
    exact_policy_checks = (
        ("scope_declaration_policy", SCOPE_DECLARATION_POLICY, "SCOPE_DECLARATION_POLICY_NOT_EXPECTED"),
        (
            "scope_label_laundering_policy",
            SCOPE_LABEL_LAUNDERING_POLICY,
            "SCOPE_LABEL_LAUNDERING_POLICY_NOT_EXPECTED",
        ),
        (
            "cosmetic_scope_naming_policy",
            COSMETIC_SCOPE_NAMING_POLICY,
            "COSMETIC_SCOPE_NAMING_POLICY_NOT_EXPECTED",
        ),
        (
            "id_role_label_difference_policy",
            ID_ROLE_LABEL_DIFFERENCE_POLICY,
            "ID_ROLE_LABEL_DIFFERENCE_POLICY_NOT_EXPECTED",
        ),
        ("shared_evidence_policy", SHARED_EVIDENCE_POLICY, "SHARED_EVIDENCE_POLICY_NOT_EXPECTED"),
        ("operation_evidence_policy", OPERATION_EVIDENCE_POLICY, "OPERATION_EVIDENCE_POLICY_NOT_EXPECTED"),
        (
            "contaminated_lineage_policy",
            CONTAMINATED_LINEAGE_POLICY,
            "CONTAMINATED_LINEAGE_POLICY_NOT_EXPECTED",
        ),
    )
    for field, expected, code in exact_policy_checks:
        _validate_exact(checks, request, field, expected, f"{field} exact", code, code)
    for field, code in FALSE_FIELD_CODES.items():
        _validate_bool_exact(checks, request, field, False, f"{field} false", code)
    _validate_non_claims(checks, request)
    _add_check(
        checks,
        "result-level required false non-claims canonical false",
        True,
        "final result canonicalizes required false non-claims",
        "canonical false emitted by resolver",
    )


def _validate_prohibited_requests(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    for field, code in PROHIBITED_REQUEST_CODES.items():
        actual = request.get(field)
        _add_check(checks, f"{field} not requested", actual is not True, False, actual, code)
    exact_true_blockers = {
        "scope_label_laundering_detected": "SCOPE_LABEL_LAUNDERING_DETECTED",
        "cosmetic_scope_naming_detected": "COSMETIC_SCOPE_NAMING_DETECTED",
        "scope_label_laundering_treated_as_basis": "SCOPE_LABEL_LAUNDERING_TREATED_AS_BASIS_TRUE",
        "cosmetic_scope_naming_treated_as_basis": "COSMETIC_SCOPE_NAMING_TREATED_AS_BASIS_TRUE",
        "id_role_label_difference_treated_as_scope_basis": (
            "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_SCOPE_BASIS_TRUE"
        ),
        "shared_evidence_treated_as_scope_basis": "SHARED_EVIDENCE_TREATED_AS_SCOPE_BASIS_TRUE",
        "operation_evidence_alone_treated_as_scope_basis": (
            "OPERATION_EVIDENCE_ALONE_TREATED_AS_SCOPE_BASIS_TRUE"
        ),
        "contaminated_lineage_treated_as_clean_scope_basis": (
            "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_SCOPE_BASIS_TRUE"
        ),
    }
    for field, code in exact_true_blockers.items():
        actual = request.get(field)
        _add_check(checks, f"{field} not true", actual is not True, False, actual, code)


def _validate_recordable_scope(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    a_scope = _scope_value(request, "candidate_a_scope_statement")
    b_scope = _scope_value(request, "candidate_b_scope_statement")
    division_basis = _scope_value(request, "basis_bearing_scope_division_basis")
    _add_check(
        checks,
        "candidate scope declarations not identical",
        bool(a_scope and b_scope and a_scope != b_scope),
        "declared candidate A and B scopes differ",
        {"candidate_a_scope_statement": a_scope, "candidate_b_scope_statement": b_scope},
        "CANDIDATE_SCOPE_DECLARATIONS_IDENTICAL",
    )
    _add_check(
        checks,
        "candidate scope declarations not cosmetic-only",
        _normalized_scope_text(a_scope) != _normalized_scope_text(b_scope) and not _basis_is_cosmetic_only(request),
        "scope difference is not id/role/label/template-only",
        "conservative string comparison",
        "CANDIDATE_SCOPE_DECLARATIONS_COSMETIC_ONLY",
    )
    _add_check(
        checks,
        "basis-bearing scope division basis present",
        bool(division_basis),
        "basis-bearing scope division basis declared",
        division_basis,
        "BASIS_BEARING_SCOPE_DIVISION_BASIS_MISSING",
    )
    _add_check(
        checks,
        "basis-bearing scope division basis non-cosmetic",
        _basis_names_non_cosmetic_category(request),
        "basis explicitly names mandate, function, responsibility, or governed surface",
        _combined_scope_basis_text(request),
        "BASIS_BEARING_SCOPE_DIVISION_BASIS_NOT_NON_COSMETIC",
    )
    _add_check(
        checks,
        "scope declaration basis does not rely on contaminated lineage",
        not _basis_references_contaminated_lineage(request),
        "contaminated lineage is not clean scope basis",
        _combined_scope_basis_text(request),
        "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_SCOPE_BASIS_TRUE",
    )
    _add_check(
        checks,
        "scope declaration basis does not rely on shared evidence alone",
        not _basis_references_shared_evidence_alone(request),
        "shared evidence alone is not scope basis",
        _combined_scope_basis_text(request),
        "SHARED_EVIDENCE_TREATED_AS_SCOPE_BASIS_TRUE",
    )
    _add_check(
        checks,
        "scope declaration basis does not rely on operation evidence alone",
        not _basis_references_operation_evidence_alone(request),
        "operation evidence alone is not scope basis",
        _combined_scope_basis_text(request),
        "OPERATION_EVIDENCE_ALONE_TREATED_AS_SCOPE_BASIS_TRUE",
    )


def build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared request using the current live basis default posture."""

    request: dict[str, Any] = {
        "candidate_non_cosmetic_scope_division_declaration_operation_id": DEFAULT_OPERATION_ID,
        "candidate_non_cosmetic_scope_division_declaration_operation_type": OPERATION_TYPE,
        "candidate_non_cosmetic_scope_division_declaration_operation_version": OPERATION_VERSION,
        "candidate_non_cosmetic_scope_division_declaration_operation_scope": OPERATION_SCOPE,
        "candidate_non_cosmetic_scope_division_declaration_operation_intent": INTENT_RECORD,
        "operation_spec_reference": DEFAULT_OPERATION_SPEC_REFERENCE,
        "completed_scope_division_declaration_boundary_terminal_summary_reference": (
            DEFAULT_SCOPE_DIVISION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE
        ),
        "completed_scope_division_declaration_boundary_artifact_reference": (
            DEFAULT_SCOPE_DIVISION_BOUNDARY_ARTIFACT_REFERENCE
        ),
        "completed_basis_emission_operation_terminal_summary_reference": (
            DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE
        ),
        "completed_basis_emission_boundary_terminal_summary_reference": (
            DEFAULT_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE
        ),
        "completed_distinctness_operation_terminal_summary_reference": (
            DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE
        ),
        "completed_differentiation_operation_terminal_summary_reference": (
            DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE
        ),
        "candidate_record_a_id": DEFAULT_CANDIDATE_A_ID,
        "candidate_record_b_id": DEFAULT_CANDIDATE_B_ID,
        "candidate_record_a_role": DEFAULT_CANDIDATE_A_ROLE,
        "candidate_record_b_role": DEFAULT_CANDIDATE_B_ROLE,
        "upstream_emission_operation_result": UPSTREAM_EMISSION_OPERATION_RESULT,
        "requires_additional_basis_preserved_as_clean_result": True,
        "candidate_a_scope_missing_upstream": True,
        "candidate_b_scope_missing_upstream": True,
        "basis_bearing_scope_division_missing_upstream": True,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "scope_declaration_policy": SCOPE_DECLARATION_POLICY,
        "candidate_a_scope_id": "",
        "candidate_b_scope_id": "",
        "candidate_a_scope_statement": "",
        "candidate_b_scope_statement": "",
        "candidate_a_scope_basis": "",
        "candidate_b_scope_basis": "",
        "basis_bearing_scope_division_statement": "",
        "basis_bearing_scope_division_basis": "",
        "scope_label_laundering_policy": SCOPE_LABEL_LAUNDERING_POLICY,
        "cosmetic_scope_naming_policy": COSMETIC_SCOPE_NAMING_POLICY,
        "id_role_label_difference_policy": ID_ROLE_LABEL_DIFFERENCE_POLICY,
        "shared_evidence_policy": SHARED_EVIDENCE_POLICY,
        "operation_evidence_policy": OPERATION_EVIDENCE_POLICY,
        "contaminated_lineage_policy": CONTAMINATED_LINEAGE_POLICY,
        "candidate_specific_content_emission_allowed": False,
        "separate_seal_material_emission_allowed": False,
        "separate_lineage_receipt_material_emission_allowed": False,
        "separate_digest_material_emission_allowed": False,
        "basis_emission_operation_rerun_allowed": False,
        "distinctness_operation_rerun_allowed": False,
        "distinctness_supported_recording_allowed": False,
        "candidate_records_marked_distinct_allowed": False,
        "candidate_standing_authorized": False,
        "descendant_body_created": False,
        "standing_authorized": False,
        "crossing_authorized": False,
        "relation_authorized": False,
        "field_machinery_authorized": False,
        "runtime_authorized": False,
        "currentness_authorized": False,
        "authority_authorized": False,
        "output_authorized": False,
        "action_authorized": False,
        "derivative_reception_authorized": False,
        "synchronization_authorized": False,
        "follow_on_authorized": False,
        "scan_allowed": False,
        "repair_allowed": False,
        "validation_enforcement_allowed": False,
        "declared_non_claims": _canonical_non_claims(),
    }
    for key, value in overrides.items():
        request[key] = value
    return request


def resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(
    declared_candidate_non_cosmetic_scope_division_declaration_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded candidate non-cosmetic scope-division declaration operation request."""

    if declared_candidate_non_cosmetic_scope_division_declaration_operation is None:
        request = build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_request()
    elif not isinstance(declared_candidate_non_cosmetic_scope_division_declaration_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_candidate_non_cosmetic_scope_division_declaration_operation).__name__,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_MALFORMED",
        )
        return _blocked_result(
            {},
            checks,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_MALFORMED",
            "request is not a mapping",
        )
    else:
        request = _deepcopy_mapping(declared_candidate_non_cosmetic_scope_division_declaration_operation)

    checks: list[dict[str, Any]] = []
    intent = request.get("candidate_non_cosmetic_scope_division_declaration_operation_intent")
    _add_check(
        checks,
        "operation intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        return _blocked_result(
            request,
            checks,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_BLOCK_REQUESTED",
            "block intent requested",
        )
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(
            request,
            checks,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_INTENT_UNSUPPORTED",
            "operation intent is unsupported",
        )

    _validate_request(checks, request)
    _validate_prohibited_requests(checks, request)
    preliminary_codes = _failed_codes(checks)
    if preliminary_codes:
        code = preliminary_codes[0]
        return _blocked_result(request, checks, code, f"blocked by failed check {code}")

    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(
            request,
            OUTCOME_NOT_RECORDED,
            checks,
            additional_basis_required=[],
            not_recorded_basis=["DO_NOT_RECORD intent requested"],
            recorded=False,
        )

    additional_basis_required = _missing_scope_basis(request)
    if additional_basis_required:
        return _build_result(
            request,
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            checks,
            additional_basis_required=additional_basis_required,
            not_recorded_basis=[],
            recorded=False,
        )

    _validate_recordable_scope(checks, request)
    recordable_codes = _failed_codes(checks)
    if recordable_codes:
        code = recordable_codes[0]
        return _blocked_result(request, checks, code, f"blocked by failed check {code}")

    return _build_result(
        request,
        OUTCOME_RECORDED,
        checks,
        additional_basis_required=[],
        not_recorded_basis=[],
        recorded=True,
    )


def resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_from_path(
    declared_candidate_non_cosmetic_scope_division_declaration_operation_path: Path | str,
) -> dict[str, Any]:
    """Read a declared operation request JSON object and resolve it."""

    path = Path(declared_candidate_non_cosmetic_scope_division_declaration_operation_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request path readable JSON",
            False,
            "readable JSON object",
            str(exc),
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_UNREADABLE",
        )
        return _blocked_result(
            {},
            checks,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_UNREADABLE",
            "request path is unreadable or not JSON",
        )
    if not isinstance(data, Mapping):
        checks = []
        _add_check(
            checks,
            "request JSON object",
            False,
            "JSON object mapping",
            type(data).__name__,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_MALFORMED",
        )
        return _blocked_result(
            {},
            checks,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_MALFORMED",
            "request JSON is not an object",
        )
    return resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(data)


def build_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary from a resolver result without raw body material."""

    operation = result.get("descendant_body_candidate_non_cosmetic_scope_division_declaration_operation", {})
    if not isinstance(operation, Mapping):
        operation = {}
    checks = result.get("candidate_non_cosmetic_scope_division_declaration_operation_checks", [])
    if isinstance(checks, list):
        passed_check_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True)
        failed_check_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is False)
    else:
        passed_check_count = int(result.get("_passed_check_count", 0) or 0)
        failed_check_count = int(result.get("_failed_check_count", 0) or 0)
    block = result.get("block")
    block_code = None
    block_reason = None
    if isinstance(block, Mapping):
        block_code = block.get("code") or block.get("block_code")
        block_reason = block.get("reason")
    non_claims = result.get("non_claims")
    canonical_false = isinstance(non_claims, Mapping) and all(
        non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
    )
    summary = {
        "outcome": result.get("outcome"),
        "block_code": block_code,
        "block_reason": block_reason,
        "candidate_non_cosmetic_scope_division_declaration_operation_id": operation.get(
            "candidate_non_cosmetic_scope_division_declaration_operation_id"
        ),
        "intent": (
            result.get("declared_candidate_non_cosmetic_scope_division_declaration_operation_basis", {})
            if isinstance(
                result.get("declared_candidate_non_cosmetic_scope_division_declaration_operation_basis"), Mapping
            )
            else {}
        ).get("candidate_non_cosmetic_scope_division_declaration_operation_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "operation_type": operation.get(
            "candidate_non_cosmetic_scope_division_declaration_operation_type"
        ),
        "operation_version": operation.get(
            "candidate_non_cosmetic_scope_division_declaration_operation_version"
        ),
        "operation_scope": operation.get(
            "candidate_non_cosmetic_scope_division_declaration_operation_scope"
        ),
        "admissible_future_route": operation.get("admissible_future_route"),
        "upstream_emission_operation_result": operation.get("upstream_emission_operation_result"),
        "requires_additional_basis_preserved_as_clean_result": operation.get(
            "requires_additional_basis_preserved_as_clean_result"
        ),
        "candidate_a_scope_missing_upstream": operation.get("candidate_a_scope_missing_upstream"),
        "candidate_b_scope_missing_upstream": operation.get("candidate_b_scope_missing_upstream"),
        "basis_bearing_scope_division_missing_upstream": operation.get(
            "basis_bearing_scope_division_missing_upstream"
        ),
        "candidate_non_cosmetic_scope_division_declaration_operation_recorded": operation.get(
            "candidate_non_cosmetic_scope_division_declaration_operation_recorded"
        ),
        "candidate_a_scope_declared": operation.get("candidate_a_scope_declared"),
        "candidate_b_scope_declared": operation.get("candidate_b_scope_declared"),
        "basis_bearing_scope_division_declared": operation.get("basis_bearing_scope_division_declared"),
        "candidate_a_scope_non_cosmetic": operation.get("candidate_a_scope_non_cosmetic"),
        "candidate_b_scope_non_cosmetic": operation.get("candidate_b_scope_non_cosmetic"),
        "scope_division_basis_bearing": operation.get("scope_division_basis_bearing"),
        "additional_basis_required": result.get("additional_basis_required", []),
        "scope_label_laundering_treated_as_basis": operation.get("scope_label_laundering_treated_as_basis"),
        "cosmetic_scope_naming_treated_as_basis": operation.get("cosmetic_scope_naming_treated_as_basis"),
        "id_role_label_difference_treated_as_scope_basis": operation.get(
            "id_role_label_difference_treated_as_scope_basis"
        ),
        "shared_evidence_treated_as_scope_basis": operation.get("shared_evidence_treated_as_scope_basis"),
        "operation_evidence_alone_treated_as_scope_basis": operation.get(
            "operation_evidence_alone_treated_as_scope_basis"
        ),
        "contaminated_lineage_treated_as_clean_scope_basis": operation.get(
            "contaminated_lineage_treated_as_clean_scope_basis"
        ),
        "candidate_specific_content_emitted": operation.get("candidate_specific_content_emitted"),
        "separate_seal_material_emitted": operation.get("separate_seal_material_emitted"),
        "separate_lineage_receipt_material_emitted": operation.get(
            "separate_lineage_receipt_material_emitted"
        ),
        "separate_digest_material_emitted": operation.get("separate_digest_material_emitted"),
        "basis_emission_operation_rerun": operation.get("basis_emission_operation_rerun"),
        "distinctness_operation_rerun": operation.get("distinctness_operation_rerun"),
        "distinctness_supported_recorded": operation.get("distinctness_supported_recorded"),
        "candidate_records_marked_distinct": operation.get("candidate_records_marked_distinct"),
        "candidate_records_remain_non_standing": operation.get("candidate_records_remain_non_standing"),
        "candidate_records_remain_not_descendant_bodies": operation.get(
            "candidate_records_remain_not_descendant_bodies"
        ),
        "candidate_standing_authorized": operation.get("candidate_standing_authorized"),
        "descendant_body_created": operation.get("descendant_body_created"),
        "standing_authorized": operation.get("standing_authorized"),
        "crossing_authorized": operation.get("crossing_authorized"),
        "relation_authorized": operation.get("relation_authorized"),
        "field_machinery_authorized": operation.get("field_machinery_authorized"),
        "runtime_authorized": operation.get("runtime_authorized"),
        "currentness_authorized": operation.get("currentness_authorized"),
        "authority_authorized": operation.get("authority_authorized"),
        "output_authorized": operation.get("output_authorized"),
        "action_authorized": operation.get("action_authorized"),
        "derivative_reception_authorized": operation.get("derivative_reception_authorized"),
        "synchronization_authorized": operation.get("synchronization_authorized"),
        "follow_on_authorized": operation.get("follow_on_authorized"),
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
        "basis_emission_boundary_overridden": False,
        "basis_emission_boundary_bypassed": False,
        "basis_emission_operation_overridden": False,
        "basis_emission_operation_bypassed": False,
        "scope_division_declaration_boundary_overridden": False,
        "scope_division_declaration_boundary_bypassed": False,
        "scan_performed": False,
        "repository_scan_performed": False,
        "repair_performed": False,
        "validation_enforced": False,
        "hidden_repair_performed": False,
        "silent_overwrite_performed": False,
        "operation_spec_markers_present": operation.get("operation_spec_markers_present"),
        "completed_scope_division_declaration_boundary_terminal_summary_markers_present": operation.get(
            "completed_scope_division_declaration_boundary_terminal_summary_markers_present"
        ),
        "completed_basis_emission_operation_terminal_summary_markers_present": operation.get(
            "completed_basis_emission_operation_terminal_summary_markers_present"
        ),
        "completed_distinctness_operation_terminal_summary_markers_present": operation.get(
            "completed_distinctness_operation_terminal_summary_markers_present"
        ),
        "completed_differentiation_operation_terminal_summary_markers_present": operation.get(
            "completed_differentiation_operation_terminal_summary_markers_present"
        ),
        "result_level_non_claims_canonical_false": canonical_false,
    }
    return _sanitize_json_value(summary)


def write_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result to deterministic UTF-8 JSON without overwriting."""

    operation = result.get("descendant_body_candidate_non_cosmetic_scope_division_declaration_operation", {})
    operation_id = DEFAULT_OPERATION_ID
    if isinstance(operation, Mapping):
        operation_id = str(
            operation.get("candidate_non_cosmetic_scope_division_declaration_operation_id")
            or DEFAULT_OPERATION_ID
        )
    filename = (
        f"{_safe_json_filename_part(operation_id)}__"
        "candidate_non_cosmetic_scope_division_declaration_operation_v0_min_result.json"
    )
    if output_path is None:
        path = REPO_ROOT / OUTPUT_ROOT / filename
    else:
        candidate = Path(output_path)
        if candidate.suffix:
            path = candidate if candidate.is_absolute() else REPO_ROOT / candidate
        else:
            path = (candidate if candidate.is_absolute() else REPO_ROOT / candidate) / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = path
    counter = 1
    while final_path.exists():
        final_path = path.with_name(f"{path.stem}_{counter:03d}{path.suffix}")
        counter += 1
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_json_ready(result), handle, ensure_ascii=True, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path
