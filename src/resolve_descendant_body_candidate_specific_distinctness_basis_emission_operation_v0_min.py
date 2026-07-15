"""Resolver for one candidate-specific distinctness basis emission operation.

The default live posture is clean REQUIRES_ADDITIONAL_BASIS because the
current repo has not declared non-cosmetic candidate A/B sub-scopes. An
explicit request can record bounded non-standing basis material only when it
declares non-identical, non-cosmetic, basis-bearing scope division. The result
does not rerun distinctness, record DISTINCTNESS_SUPPORTED, mark candidates
distinct, authorize standing, create descendants, scan, repair, or authorize
follow-on work.
"""

from __future__ import annotations

import copy
import hashlib
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateSpecificDistinctnessBasisEmissionOperationV0MinError(Exception):
    """Bounded resolver error for malformed local operation requests."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min"

OUTCOME_RECORDED = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_RECORDED"
OUTCOME_BLOCKED = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_BLOCKED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_NOT_RECORDED,
)

OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "TWO_NON_STANDING_CANDIDATE_RECORDS_SCOPE_DIVISION_ONLY"
ADMISSIBLE_FUTURE_BASIS_ROUTE = "SCOPE_DIVISION_ONLY"
SCOPE_DIVISION_POLICY = "REQUIRE_NON_COSMETIC_SCOPE_DIVISION"
CANDIDATE_SPECIFIC_CONTENT_POLICY = "EMIT_ONLY_NON_STANDING_BASIS_BEARING_CONTENT"
SEPARATE_SEAL_MATERIAL_POLICY = "SEAL_ONLY_NON_COSMETIC_CANDIDATE_SPECIFIC_CONTENT"
SEPARATE_LINEAGE_RECEIPT_MATERIAL_POLICY = "RECEIPT_ONLY_NON_COSMETIC_SCOPE_DIVISION"
SEPARATE_DIGEST_MATERIAL_POLICY = "DIGEST_ONLY_NON_COSMETIC_CANDIDATE_SPECIFIC_MATERIAL"
COSMETIC_SUBSTITUTION_POLICY = "COSMETIC_SUBSTITUTION_NOT_BASIS"
DIGEST_LAUNDERING_POLICY = "DIGEST_LAUNDERING_NOT_BASIS"
ID_ROLE_LABEL_DIFFERENCE_POLICY = "ID_ROLE_LABEL_DIFFERENCE_NOT_BASIS"
SHARED_EVIDENCE_POLICY = "SHARED_EVIDENCE_NOT_BASIS"
OPERATION_EVIDENCE_POLICY = "OPERATION_EVIDENCE_ALONE_NOT_BASIS"

CANDIDATE_A_ID = "descendant_body_basis_candidate_a_001"
CANDIDATE_B_ID = "descendant_body_basis_candidate_b_001"
CANDIDATE_A_ROLE = "CANDIDATE_A"
CANDIDATE_B_ROLE = "CANDIDATE_B"

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_OPERATION_ID = "descendant_body_candidate_specific_distinctness_basis_emission_operation_001"
DEFAULT_OPERATION_QUESTION = (
    "Given one completed candidate-specific distinctness basis emission boundary that preserved NOT_DISTINCT "
    "as a clean upstream result and allowed only the future scope-division route, may a separately implemented "
    "future operation emit non-standing candidate-specific distinctness basis for exactly two existing non-standing "
    "candidate records by assigning two non-cosmetic sub-scopes of the parent basis, while emitting candidate-specific "
    "content, separate seal material, separate lineage receipt material, and separate digest material only if the "
    "differences are basis-bearing rather than label-bearing, and while preserving that the operation does not rerun "
    "distinctness, record DISTINCTNESS_SUPPORTED, mark candidate records distinct, authorize candidate standing, "
    "create descendant bodies, authorize crossing, create relation, create FIELD machinery, create runtime, create "
    "currentness, create authority, authorize output, authorize action, authorize derivative reception, authorize "
    "synchronization, repair the affected file, validate prior unsupported claims, scan repository, enforce validation, "
    "or authorize follow-on work?"
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOUNDARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_BOUNDARY_ARTIFACT_REFERENCE = (
    "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2/"
    "descendant_body_candidate_specific_distinctness_basis_emission_boundary_001__candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_result.json"
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
DEFAULT_OPERATION_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_V0_MIN_SPEC.md"
)
DEFAULT_PARENT_BASIS_REFERENCE = "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md"
OUTPUT_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "candidate_specific_distinctness_basis_emission_operation_implemented",
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
    "candidate_specific_distinctness_basis_emission_operation_recorded",
    "candidate_specific_content_emitted",
    "separate_seal_material_emitted",
    "separate_lineage_receipt_material_emitted",
    "separate_digest_material_emitted",
    "scope_division_non_cosmetic",
    "candidate_specific_content_basis_bearing",
    "emitted_basis_non_standing",
    "candidate_records_remain_non_standing",
    "candidate_records_remain_not_descendant_bodies",
    "operation_spec_markers_present",
    "upstream_boundary_terminal_summary_markers_present",
    "completed_distinctness_operation_terminal_summary_markers_present",
    "completed_differentiation_operation_terminal_summary_markers_present",
    "completed_distinctness_operation_boundary_terminal_summary_markers_present",
    "result_level_non_claims_canonical_false",
)

ALLOWED_TRUE_REQUIRES_ADDITIONAL_BASIS_FIELDS = (
    "additional_basis_required_recorded",
    "missing_candidate_a_scope_recorded",
    "missing_candidate_b_scope_recorded",
    "missing_non_cosmetic_scope_division_recorded",
    "operation_spec_markers_present",
    "upstream_boundary_terminal_summary_markers_present",
    "completed_distinctness_operation_terminal_summary_markers_present",
    "completed_differentiation_operation_terminal_summary_markers_present",
    "completed_distinctness_operation_boundary_terminal_summary_markers_present",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_QUESTION_UNDECLARED",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_INTENT_UNSUPPORTED",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_BLOCK_REQUESTED",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TYPE_MISSING",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TYPE_NOT_EXPECTED",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_VERSION_MISSING",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_VERSION_NOT_0_1_0",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_SCOPE_MISSING",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_SCOPE_NOT_EXPECTED",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REFERENCE_MISSING",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
    "OPERATION_SPEC_REFERENCE_MISSING",
    "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "CANDIDATE_RECORD_A_ID_NOT_EXPECTED",
    "CANDIDATE_RECORD_B_ID_NOT_EXPECTED",
    "CANDIDATE_RECORD_A_ROLE_NOT_EXPECTED",
    "CANDIDATE_RECORD_B_ROLE_NOT_EXPECTED",
    "PARENT_BASIS_REFERENCE_MISSING",
    "ADMISSIBLE_FUTURE_BASIS_ROUTE_NOT_SCOPE_DIVISION_ONLY",
    "SCOPE_DIVISION_POLICY_NOT_EXPECTED",
    "CANDIDATE_SPECIFIC_CONTENT_POLICY_NOT_EXPECTED",
    "SEPARATE_SEAL_MATERIAL_POLICY_NOT_EXPECTED",
    "SEPARATE_LINEAGE_RECEIPT_MATERIAL_POLICY_NOT_EXPECTED",
    "SEPARATE_DIGEST_MATERIAL_POLICY_NOT_EXPECTED",
    "COSMETIC_SUBSTITUTION_POLICY_NOT_EXPECTED",
    "DIGEST_LAUNDERING_POLICY_NOT_EXPECTED",
    "ID_ROLE_LABEL_DIFFERENCE_POLICY_NOT_EXPECTED",
    "SHARED_EVIDENCE_POLICY_NOT_EXPECTED",
    "OPERATION_EVIDENCE_POLICY_NOT_EXPECTED",
    "CANDIDATE_A_SCOPE_MISSING",
    "CANDIDATE_B_SCOPE_MISSING",
    "SCOPE_DIVISION_MISSING",
    "CANDIDATE_SCOPES_IDENTICAL",
    "CANDIDATE_SCOPES_COSMETIC_ONLY",
    "CANDIDATE_SCOPES_TEMPLATE_SUBSTITUTION_ONLY",
    "CANDIDATE_SCOPE_RELIES_ON_CONTAMINATED_LINEAGE_AS_CLEAN_BASIS",
    "SCOPE_DIVISION_REQUIRES_ADDITIONAL_BASIS",
    "OPERATION_SPEC_MARKER_MISSING",
    "UPSTREAM_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCAN_ALLOWED_TRUE",
    "REPAIR_ALLOWED_TRUE",
    "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
    "DIVERGENT_RECEIPT_HISTORY_ROUTE_AUTHORIZED_TRUE",
    "CARRIER_SEPARATION_ROUTE_AUTHORIZED_TRUE",
    "DISTINCTNESS_OPERATION_RERUN_TRUE",
    "DISTINCTNESS_SUPPORTED_RECORDED_TRUE",
    "CANDIDATE_RECORDS_MARKED_DISTINCT_TRUE",
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
    "REQUESTED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_OVERRIDE",
    "REQUESTED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_BYPASS",
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
    "COSMETIC_SUBSTITUTION_TREATED_AS_BASIS",
    "DIGEST_LAUNDERING_TREATED_AS_BASIS",
    "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_BASIS",
    "SHARED_EVIDENCE_TREATED_AS_BASIS",
    "OPERATION_EVIDENCE_ALONE_TREATED_AS_BASIS",
    "DIVERGENT_RECEIPT_HISTORY_ROUTE_AUTHORIZED",
    "CARRIER_SEPARATION_ROUTE_AUTHORIZED",
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
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_OVERRIDDEN",
    "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_BYPASSED",
    "SCAN_PERFORMED",
    "REPOSITORY_SCAN_PERFORMED",
    "REPAIR_PERFORMED",
    "VALIDATION_ENFORCED",
    "HIDDEN_REPAIR_PERFORMED",
    "SILENT_OVERWRITE_PERFORMED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUEST_MALFORMED",
    "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUEST_UNREADABLE",
)

OPERATION_SPEC_MARKERS = (
    ("Descendant Body Candidate-Specific Distinctness Basis Emission Operation V0 Minimum Specification",),
    ("This file defines one future candidate-specific distinctness basis emission operation.",),
    ("This file is operation-spec-only.",),
    ("This file does not implement or perform the operation.",),
    ("This file does not emit candidate-specific content, separate seal material, separate lineage receipt material, or separate digest material.",),
    ("SCOPE_DIVISION_ONLY",),
    ("REQUIRE_NON_COSMETIC_SCOPE_DIVISION",),
    ("EMIT_ONLY_NON_STANDING_BASIS_BEARING_CONTENT",),
    ("SEAL_ONLY_NON_COSMETIC_CANDIDATE_SPECIFIC_CONTENT",),
    ("RECEIPT_ONLY_NON_COSMETIC_SCOPE_DIVISION",),
    ("DIGEST_ONLY_NON_COSMETIC_CANDIDATE_SPECIFIC_MATERIAL",),
    ("COSMETIC_SUBSTITUTION_NOT_BASIS",),
    ("DIGEST_LAUNDERING_NOT_BASIS",),
    ("ID_ROLE_LABEL_DIFFERENCE_NOT_BASIS",),
    ("SHARED_EVIDENCE_NOT_BASIS",),
    ("OPERATION_EVIDENCE_ALONE_NOT_BASIS",),
    ("Success requires non-cosmetic scope division and basis-bearing candidate-specific material.",),
    ("No implementation exists in this spec.",),
    ("candidate_specific_distinctness_basis_emission_operation_implemented = false",),
    ("candidate_specific_distinctness_basis_emission_operation_recorded = false",),
    ("candidate_specific_content_emitted = false",),
    ("distinctness_supported_recorded = false",),
    ("candidate_standing_authorized = false",),
)

UPSTREAM_BOUNDARY_TERMINAL_SUMMARY_MARKERS = (
    ("DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_RECORDED",),
    ("failed_check_count = 0", "failed_check_count 0"),
    ("passed_check_count = 131", "passed_check_count 131"),
    ("result_version = 0.2.0", "result_version 0.2.0"),
    ("SCOPE_DIVISION_ONLY",),
    ("COSMETIC_DIFFERENCE_CRYPTOGRAPHICALLY_DRESSED_AS_DISTINCTNESS",),
    ("scope_division_route_allowed_for_future_operation_shape = true",),
    ("NOT_DISTINCT as a clean upstream operation result", "NOT_DISTINCT is a clean upstream operation result"),
    ("Digest difference is not distinctness unless the digested material carries non-cosmetic candidate-specific basis",),
    ("Candidate-specific basis must be basis-bearing, not label-bearing",),
    ("does not define, implement, or perform emission operation", "does not define, implement, or perform the future emission operation"),
    ("does not emit candidate-specific content", "not candidate-specific content", "candidate_specific_content_not_emitted = true"),
    ("does not rerun distinctness", "not distinctness rerun", "distinctness_operation_not_rerun = true"),
    ("does not record DISTINCTNESS_SUPPORTED", "record `DISTINCTNESS_SUPPORTED`"),
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

COMPLETED_DISTINCTNESS_BOUNDARY_MARKERS = (
    ("DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_RECORDED",),
    ("enumeration is not distinction",),
    ("id and role difference alone are not distinctness",),
    ("shared evidence reference alone is not distinctness", "shared evidence reference alone are not distinctness"),
    (
        "distinctness support requires separate candidate-specific evidence",
        "distinctness_evidence_policy = REQUIRE_SEPARATE_CANDIDATE_SPECIFIC_DISTINCTNESS_EVIDENCE",
        "requires separate candidate-specific evidence",
    ),
    ("candidate standing is not authorized", "candidate_standing_not_authorized = true"),
)

DIFFERENTIATION_REQUIRED_MARKERS = {
    "operation_line": (
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
        "completed descendant-body differentiation operation line",
        "completed descendant-body differentiation operation",
    ),
    "operation_result": (
        "completed operation result",
        "operation result emitted",
        "operation_result_created = true",
        "operation_recorded = true",
    ),
    "exactly_two_candidate_records": (
        "emitted exactly two result-contained non-standing candidate records",
        "exactly two result-contained non-standing candidate records",
        "two result-contained non-standing candidate records",
        "candidate_record_count_emitted = 2",
        "candidate_record_count = 2",
    ),
    "contained_or_operation_evidenced": (
        "candidate records are result-contained",
        "result-contained non-standing candidate records",
        "candidate records are operation-evidenced",
        "candidate_records_have_operation_evidence = true",
        "operation evidence",
    ),
    "non_standing": (
        "candidate_records_non_standing = true",
        "candidate records are non-standing",
        "candidate records remain non-standing",
        "candidate records are not standing descendants",
        "not standing descendants",
    ),
    "not_descendant_bodies": (
        "candidate records are not descendant bodies",
        "not descendant bodies",
        "descendant bodies not created",
        "descendant_bodies_not_created = true",
        "descendant_body_a_created = false",
        "descendant_body_b_created = false",
    ),
    "standing_descendants_not_created": (
        "standing descendants not created",
        "standing_descendant_created = false",
        "not standing descendants",
        "does not create standing descendants",
    ),
    "crossing_not_authorized": (
        "first crossing not authorized",
        "first_crossing_authorized = false",
        "does not authorize crossing",
    ),
    "relation_not_created": ("relation not created", "relation_created = false", "does not create relation"),
}

DIFFERENTIATION_FORBIDDEN_MARKERS = (
    "descendant_body_created = true",
    "descendant_bodies_created = true",
    "descendant bodies were created",
    "standing_descendant_created = true",
    "standing descendants were created",
    "first_crossing_authorized = true",
    "crossing_authorized = true",
    "relation_created = true",
    "relation_authorized = true",
)

SENSITIVE_KEY_PARTS = (
    "raw_body",
    "full_body",
    "markdown_body",
    "hidden_repo_state",
    "local_cache",
    "current_working_tree",
)

BASIS_BEARING_TERMS = (
    "mandate",
    "function",
    "responsibility",
    "governed surface",
    "governed-surface",
    "scope",
    "content integrity",
    "content-integrity",
    "receipt traceability",
    "receipt-traceability",
)

CONTAMINATED_LINEAGE_MARKERS = (
    "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC",
    "descendant_body_basis_derivation_event",
    "descendant_body_basis_candidate_a_created = true",
    "descendant_body_basis_candidate_b_created = true",
    "prior unsupported claims",
    "unsupported existence claim",
)

CHECKED_FALSE_FIELDS = (
    ("scan_allowed", "SCAN_ALLOWED_TRUE"),
    ("repair_allowed", "REPAIR_ALLOWED_TRUE"),
    ("validation_enforcement_allowed", "VALIDATION_ENFORCEMENT_ALLOWED_TRUE"),
    ("divergent_receipt_history_route_authorized", "DIVERGENT_RECEIPT_HISTORY_ROUTE_AUTHORIZED_TRUE"),
    ("carrier_separation_route_authorized", "CARRIER_SEPARATION_ROUTE_AUTHORIZED_TRUE"),
    ("distinctness_operation_rerun", "DISTINCTNESS_OPERATION_RERUN_TRUE"),
    ("distinctness_supported_recorded", "DISTINCTNESS_SUPPORTED_RECORDED_TRUE"),
    ("candidate_records_marked_distinct", "CANDIDATE_RECORDS_MARKED_DISTINCT_TRUE"),
    ("candidate_records_distinct", "CANDIDATE_RECORDS_MARKED_DISTINCT_TRUE"),
    ("candidate_standing_authorized", "CANDIDATE_STANDING_AUTHORIZED_TRUE"),
    ("candidate_standing_created", "CANDIDATE_STANDING_AUTHORIZED"),
    ("descendant_body_a_created", "DESCENDANT_BODY_CREATED"),
    ("descendant_body_b_created", "DESCENDANT_BODY_CREATED"),
    ("descendant_body_created", "DESCENDANT_BODY_CREATED_TRUE"),
    ("standing_descendant_created", "STANDING_CREATED"),
    ("descendant_standing_check_performed", "REQUESTED_DESCENDANT_STANDING_CHECK"),
    ("first_crossing_authorized", "CROSSING_AUTHORIZED_TRUE"),
    ("standing_authorized", "STANDING_AUTHORIZED_TRUE"),
    ("crossing_authorized", "CROSSING_AUTHORIZED_TRUE"),
    ("relation_created", "RELATION_AUTHORIZED"),
    ("relation_authorized", "RELATION_AUTHORIZED_TRUE"),
    ("field_machinery_created", "FIELD_MACHINERY_AUTHORIZED"),
    ("field_machinery_authorized", "FIELD_MACHINERY_AUTHORIZED_TRUE"),
    ("runtime_created", "RUNTIME_CREATED"),
    ("runtime_authorized", "RUNTIME_AUTHORIZED_TRUE"),
    ("api_created", "API_CREATED"),
    ("currentness_created", "CURRENTNESS_CREATED"),
    ("currentness_authorized", "CURRENTNESS_AUTHORIZED_TRUE"),
    ("authority_created", "AUTHORITY_CREATED"),
    ("authority_authorized", "AUTHORITY_AUTHORIZED_TRUE"),
    ("standing_created", "STANDING_CREATED"),
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
    (
        "candidate_specific_distinctness_basis_emission_boundary_overridden",
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_OVERRIDDEN",
    ),
    (
        "candidate_specific_distinctness_basis_emission_boundary_bypassed",
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_BYPASSED",
    ),
    ("scan_performed", "SCAN_PERFORMED"),
    ("repository_scan_performed", "REPOSITORY_SCAN_PERFORMED"),
    ("repair_performed", "REPAIR_PERFORMED"),
    ("validation_enforced", "VALIDATION_ENFORCED"),
    ("hidden_repair_performed", "HIDDEN_REPAIR_PERFORMED"),
    ("silent_overwrite_performed", "SILENT_OVERWRITE_PERFORMED"),
    ("cosmetic_substitution_treated_as_basis", "COSMETIC_SUBSTITUTION_TREATED_AS_BASIS"),
    ("digest_laundering_treated_as_basis", "DIGEST_LAUNDERING_TREATED_AS_BASIS"),
    ("id_role_label_difference_treated_as_basis", "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_BASIS"),
    ("shared_evidence_treated_as_basis", "SHARED_EVIDENCE_TREATED_AS_BASIS"),
    ("operation_evidence_alone_treated_as_basis", "OPERATION_EVIDENCE_ALONE_TREATED_AS_BASIS"),
    (
        "candidate_specific_distinctness_basis_emission_operation_implemented",
        "REQUESTED_EMISSION_OPERATION_IMPLEMENTATION",
    ),
    ("candidate_specific_distinctness_basis_emission_operation_created", "REQUESTED_EMISSION_OPERATION_DEFINITION"),
    ("candidate_specific_distinctness_basis_emission_operation_performed", "REQUESTED_EMISSION_OPERATION_IMPLEMENTATION"),
    ("candidate_specific_distinctness_basis_emission_operation_recorded", "REQUESTED_EMISSION_OPERATION_IMPLEMENTATION"),
    ("candidate_specific_content_emitted", "REQUESTED_CANDIDATE_SPECIFIC_CONTENT_EMISSION"),
    ("separate_seal_material_emitted", "REQUESTED_SEPARATE_SEAL_MATERIAL_EMISSION"),
    ("separate_lineage_receipt_material_emitted", "REQUESTED_SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMISSION"),
    ("separate_digest_material_emitted", "REQUESTED_SEPARATE_DIGEST_MATERIAL_EMISSION"),
)

REQUEST_FLAG_ALIASES = {
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
    "REQUESTED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_OVERRIDE": (
        "requested_candidate_specific_distinctness_basis_emission_boundary_override",
        "request_candidate_specific_distinctness_basis_emission_boundary_override",
    ),
    "REQUESTED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_BYPASS": (
        "requested_candidate_specific_distinctness_basis_emission_boundary_bypass",
        "request_candidate_specific_distinctness_basis_emission_boundary_bypass",
    ),
    "REQUESTED_CANDIDATE_STANDING_AUTHORIZATION": (
        "requested_candidate_standing_authorization",
        "request_candidate_standing_authorization",
    ),
    "REQUESTED_DESCENDANT_BODY_CREATION": ("requested_descendant_body_creation", "request_descendant_body_creation"),
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
    "REQUESTED_FIELD_MACHINERY_CREATION": ("requested_field_machinery_creation", "request_field_machinery_creation"),
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


def _normalize_text(text: str) -> str:
    return " ".join(text.replace("`", "").lower().split())


def _contains_any(text: str, markers: tuple[str, ...]) -> bool:
    normalized = _normalize_text(text)
    return any(_normalize_text(marker) in normalized for marker in markers)


def _compact_text(value: Any, *, limit: int = 240) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return f"{text[: limit - 15].rstrip()}... [truncated]"


def _safe_filename_part(value: Any) -> str:
    safe = str(value or DEFAULT_OPERATION_ID)
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe.strip("._-") or DEFAULT_OPERATION_ID


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
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str) and len(value) > 500:
        return _compact_text(value, limit=500)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


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
        return False, {
            "readable": False,
            "missing_marker_count": len(marker_groups),
            "missing_markers": [group[0] for group in marker_groups[:5]],
        }
    missing = [group[0] for group in marker_groups if not _contains_any(text, group)]
    return not missing, {"readable": True, "missing_marker_count": len(missing), "missing_markers": missing[:5]}


def _completed_differentiation_posture_present(path_value: Any) -> tuple[bool, dict[str, Any]]:
    readable, text = _read_text_file(path_value)
    if not readable:
        return False, {"readable": False, "missing_categories": list(DIFFERENTIATION_REQUIRED_MARKERS)}
    normalized = _normalize_text(text)
    forbidden = [marker for marker in DIFFERENTIATION_FORBIDDEN_MARKERS if _normalize_text(marker) in normalized]
    category_posture = {
        category: _contains_any(text, markers) for category, markers in DIFFERENTIATION_REQUIRED_MARKERS.items()
    }
    missing = [category for category, present in category_posture.items() if not present]
    return not missing and not forbidden, {
        "readable": True,
        "missing_categories": missing,
        "forbidden_markers_present": forbidden,
        "accepted_equivalence": not missing and not forbidden,
    }


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


def _validate_differentiation_marker_file(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> bool:
    passed, actual = _completed_differentiation_posture_present(
        request.get("completed_differentiation_operation_terminal_summary_reference")
    )
    _add_check(
        checks,
        "completed_differentiation_operation_terminal_summary_markers_present",
        passed,
        "completed differentiation summary preserves operation result, two non-standing candidate records, no descendant bodies, no crossing, and no relation",
        actual,
        "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    )
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
    malformed = [
        key
        for key in REQUIRED_FALSE_NON_CLAIMS
        if key not in declared or not isinstance(declared.get(key), bool) or declared.get(key) is not False
    ]
    _add_check(
        checks,
        "required_non_claims_false",
        not malformed,
        "every required declared non-claim is exactly boolean false",
        {"malformed_count": len(malformed), "malformed_keys": malformed[:8]},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _validate_reference(checks: list[dict[str, Any]], request: Mapping[str, Any], field_name: str, code: str) -> None:
    value = request.get(field_name)
    _add_check(
        checks,
        f"{field_name}_declared",
        isinstance(value, (str, Path)) and bool(str(value)),
        "declared reference path",
        value,
        code,
    )


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


def _validate_false_field(checks: list[dict[str, Any]], request: Mapping[str, Any], field_name: str, code: str) -> None:
    value = request.get(field_name)
    _add_check(checks, f"{field_name}_false", value is False, False, value, code)


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def _sha256_for(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def _scope_text(request: Mapping[str, Any], candidate: str) -> str:
    return " ".join(
        str(request.get(f"{candidate}_scope_{field}", "") or "")
        for field in ("id", "statement", "basis")
    )


def _candidate_scope_declared(request: Mapping[str, Any], candidate: str) -> bool:
    return all(bool(str(request.get(f"{candidate}_scope_{field}", "")).strip()) for field in ("id", "statement", "basis"))


def _cosmetic_normalize(value: Any) -> str:
    text = _normalize_text(str(value or ""))
    replacements = (
        CANDIDATE_A_ID,
        CANDIDATE_B_ID,
        "candidate a",
        "candidate b",
        "candidate_a",
        "candidate_b",
        "candidate-a",
        "candidate-b",
        "role a",
        "role b",
        "candidata",
        "candidateb",
        " side a",
        " side b",
        " slot a",
        " slot b",
        " label a",
        " label b",
    )
    for token in replacements:
        text = text.replace(_normalize_text(token), "")
    return " ".join(text.split())


def _contains_basis_bearing_terms(value: Any) -> bool:
    normalized = _normalize_text(str(value or ""))
    return any(term in normalized for term in BASIS_BEARING_TERMS)


def _contains_contaminated_lineage(value: Any) -> bool:
    normalized = _normalize_text(str(value or ""))
    return any(_normalize_text(marker) in normalized for marker in CONTAMINATED_LINEAGE_MARKERS)


def _scope_posture(request: Mapping[str, Any]) -> dict[str, Any]:
    candidate_a_declared = _candidate_scope_declared(request, "candidate_a")
    candidate_b_declared = _candidate_scope_declared(request, "candidate_b")
    a_text = _scope_text(request, "candidate_a")
    b_text = _scope_text(request, "candidate_b")
    both_declared = candidate_a_declared and candidate_b_declared
    identical = both_declared and _normalize_text(a_text) == _normalize_text(b_text)
    cosmetic_only = both_declared and not identical and _cosmetic_normalize(a_text) == _cosmetic_normalize(b_text)
    template_only = bool(
        request.get("candidate_scopes_template_substitution_only") is True
        or request.get("template_substitution_only") is True
        or request.get("scope_division_template_substitution_only") is True
    )
    contaminated = any(
        _contains_contaminated_lineage(request.get(field))
        for field in (
            "candidate_a_scope_basis",
            "candidate_b_scope_basis",
            "candidate_a_scope_statement",
            "candidate_b_scope_statement",
            "parent_basis_reference",
        )
    )
    basis_bearing = both_declared and (
        request.get("candidate_specific_content_basis_bearing") is True
        or (
            _contains_basis_bearing_terms(request.get("candidate_a_scope_statement"))
            and _contains_basis_bearing_terms(request.get("candidate_b_scope_statement"))
            and _contains_basis_bearing_terms(request.get("candidate_a_scope_basis"))
            and _contains_basis_bearing_terms(request.get("candidate_b_scope_basis"))
        )
    )
    non_cosmetic = both_declared and not identical and not cosmetic_only and not template_only and basis_bearing
    return {
        "candidate_a_scope_declared": candidate_a_declared,
        "candidate_b_scope_declared": candidate_b_declared,
        "both_candidate_scopes_declared": both_declared,
        "candidate_scopes_identical": identical,
        "candidate_scopes_cosmetic_only": cosmetic_only,
        "candidate_scopes_template_substitution_only": template_only,
        "candidate_scope_relies_on_contaminated_lineage_as_clean_basis": contaminated,
        "candidate_specific_content_basis_bearing": basis_bearing,
        "scope_division_non_cosmetic": non_cosmetic,
        "ready_to_record": both_declared and non_cosmetic and not contaminated,
    }


def _additional_basis_required(scope_posture: Mapping[str, Any]) -> list[str]:
    additional: list[str] = []
    if scope_posture.get("candidate_a_scope_declared") is not True:
        additional.append("missing non-cosmetic candidate A scope")
    if scope_posture.get("candidate_b_scope_declared") is not True:
        additional.append("missing non-cosmetic candidate B scope")
    if scope_posture.get("scope_division_non_cosmetic") is not True:
        additional.append("missing basis-bearing scope division")
    return additional


def _validate_scope_posture(
    checks: list[dict[str, Any]],
    scope_posture: Mapping[str, Any],
) -> None:
    both_declared = scope_posture.get("both_candidate_scopes_declared") is True
    _add_check(
        checks,
        "default_missing_scope_division_recorded_as_additional_basis",
        True,
        "missing scope division is additional basis until explicit candidate scopes are declared",
        {
            "candidate_a_scope_declared": scope_posture.get("candidate_a_scope_declared"),
            "candidate_b_scope_declared": scope_posture.get("candidate_b_scope_declared"),
            "scope_division_non_cosmetic": scope_posture.get("scope_division_non_cosmetic"),
        },
        "SCOPE_DIVISION_REQUIRES_ADDITIONAL_BASIS",
    )
    if not both_declared:
        return
    _add_check(
        checks,
        "candidate_a_scope_declared_for_recorded_emission",
        scope_posture.get("candidate_a_scope_declared") is True,
        True,
        scope_posture.get("candidate_a_scope_declared"),
        "CANDIDATE_A_SCOPE_MISSING",
    )
    _add_check(
        checks,
        "candidate_b_scope_declared_for_recorded_emission",
        scope_posture.get("candidate_b_scope_declared") is True,
        True,
        scope_posture.get("candidate_b_scope_declared"),
        "CANDIDATE_B_SCOPE_MISSING",
    )
    _add_check(
        checks,
        "candidate_scopes_non_identical",
        scope_posture.get("candidate_scopes_identical") is not True,
        False,
        scope_posture.get("candidate_scopes_identical"),
        "CANDIDATE_SCOPES_IDENTICAL",
    )
    _add_check(
        checks,
        "candidate_scopes_not_cosmetic_only",
        scope_posture.get("candidate_scopes_cosmetic_only") is not True,
        False,
        scope_posture.get("candidate_scopes_cosmetic_only"),
        "CANDIDATE_SCOPES_COSMETIC_ONLY",
    )
    _add_check(
        checks,
        "candidate_scopes_not_template_substitution_only",
        scope_posture.get("candidate_scopes_template_substitution_only") is not True,
        False,
        scope_posture.get("candidate_scopes_template_substitution_only"),
        "CANDIDATE_SCOPES_TEMPLATE_SUBSTITUTION_ONLY",
    )
    _add_check(
        checks,
        "candidate_scope_does_not_rely_on_contaminated_lineage_as_clean_basis",
        scope_posture.get("candidate_scope_relies_on_contaminated_lineage_as_clean_basis") is not True,
        False,
        scope_posture.get("candidate_scope_relies_on_contaminated_lineage_as_clean_basis"),
        "CANDIDATE_SCOPE_RELIES_ON_CONTAMINATED_LINEAGE_AS_CLEAN_BASIS",
    )
    if (
        scope_posture.get("candidate_scopes_identical") is not True
        and scope_posture.get("candidate_scopes_cosmetic_only") is not True
        and scope_posture.get("candidate_scopes_template_substitution_only") is not True
        and scope_posture.get("candidate_scope_relies_on_contaminated_lineage_as_clean_basis") is not True
    ):
        _add_check(
            checks,
            "scope_division_non_cosmetic_when_recording",
            True,
            "non-cosmetic scope division or additional basis posture",
            scope_posture.get("scope_division_non_cosmetic"),
            "SCOPE_DIVISION_REQUIRES_ADDITIONAL_BASIS",
        )
        _add_check(
            checks,
            "candidate_specific_content_basis_bearing_when_recording",
            True,
            "basis-bearing candidate-specific material or additional basis posture",
            scope_posture.get("candidate_specific_content_basis_bearing"),
            "SCOPE_DIVISION_REQUIRES_ADDITIONAL_BASIS",
        )


def _validate_request(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> tuple[dict[str, bool], dict[str, Any]]:
    intent = request.get("candidate_specific_distinctness_basis_emission_operation_intent")
    _add_check(
        checks,
        "operation_question_declared",
        bool(request.get("candidate_specific_distinctness_basis_emission_operation_question")),
        "operation question declared",
        request.get("candidate_specific_distinctness_basis_emission_operation_question"),
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_QUESTION_UNDECLARED",
    )
    _add_check(
        checks,
        "operation_intent_supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _add_check(
            checks,
            "operation_block_intent_not_requested",
            False,
            "non-blocking intent",
            intent,
            "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_BLOCK_REQUESTED",
        )

    _validate_exact_field(
        checks,
        request,
        "candidate_specific_distinctness_basis_emission_operation_type",
        OPERATION_TYPE,
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TYPE_MISSING",
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TYPE_NOT_EXPECTED",
    )
    _validate_exact_field(
        checks,
        request,
        "candidate_specific_distinctness_basis_emission_operation_version",
        OPERATION_VERSION,
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_VERSION_MISSING",
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_VERSION_NOT_0_1_0",
    )
    _validate_exact_field(
        checks,
        request,
        "candidate_specific_distinctness_basis_emission_operation_scope",
        OPERATION_SCOPE,
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_SCOPE_MISSING",
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_SCOPE_NOT_EXPECTED",
    )
    _validate_reference(
        checks,
        request,
        "candidate_specific_distinctness_basis_emission_boundary_reference",
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REFERENCE_MISSING",
    )
    _validate_reference(
        checks,
        request,
        "candidate_specific_distinctness_basis_emission_boundary_artifact_reference",
        "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
    )
    _validate_reference(checks, request, "operation_spec_reference", "OPERATION_SPEC_REFERENCE_MISSING")
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
    _validate_reference(checks, request, "parent_basis_reference", "PARENT_BASIS_REFERENCE_MISSING")
    _validate_exact_field(
        checks,
        request,
        "admissible_future_basis_route",
        ADMISSIBLE_FUTURE_BASIS_ROUTE,
        "ADMISSIBLE_FUTURE_BASIS_ROUTE_NOT_SCOPE_DIVISION_ONLY",
        "ADMISSIBLE_FUTURE_BASIS_ROUTE_NOT_SCOPE_DIVISION_ONLY",
    )
    exact_fields = (
        ("scope_division_policy", SCOPE_DIVISION_POLICY, "SCOPE_DIVISION_POLICY_NOT_EXPECTED"),
        ("candidate_specific_content_policy", CANDIDATE_SPECIFIC_CONTENT_POLICY, "CANDIDATE_SPECIFIC_CONTENT_POLICY_NOT_EXPECTED"),
        ("separate_seal_material_policy", SEPARATE_SEAL_MATERIAL_POLICY, "SEPARATE_SEAL_MATERIAL_POLICY_NOT_EXPECTED"),
        (
            "separate_lineage_receipt_material_policy",
            SEPARATE_LINEAGE_RECEIPT_MATERIAL_POLICY,
            "SEPARATE_LINEAGE_RECEIPT_MATERIAL_POLICY_NOT_EXPECTED",
        ),
        ("separate_digest_material_policy", SEPARATE_DIGEST_MATERIAL_POLICY, "SEPARATE_DIGEST_MATERIAL_POLICY_NOT_EXPECTED"),
        ("cosmetic_substitution_policy", COSMETIC_SUBSTITUTION_POLICY, "COSMETIC_SUBSTITUTION_POLICY_NOT_EXPECTED"),
        ("digest_laundering_policy", DIGEST_LAUNDERING_POLICY, "DIGEST_LAUNDERING_POLICY_NOT_EXPECTED"),
        ("id_role_label_difference_policy", ID_ROLE_LABEL_DIFFERENCE_POLICY, "ID_ROLE_LABEL_DIFFERENCE_POLICY_NOT_EXPECTED"),
        ("shared_evidence_policy", SHARED_EVIDENCE_POLICY, "SHARED_EVIDENCE_POLICY_NOT_EXPECTED"),
        ("operation_evidence_policy", OPERATION_EVIDENCE_POLICY, "OPERATION_EVIDENCE_POLICY_NOT_EXPECTED"),
    )
    for field_name, expected, code in exact_fields:
        _validate_exact_field(checks, request, field_name, expected, code, code)

    _add_check(
        checks,
        "candidate_record_a_id_exact",
        request.get("candidate_record_a_id") == CANDIDATE_A_ID,
        CANDIDATE_A_ID,
        request.get("candidate_record_a_id"),
        "CANDIDATE_RECORD_A_ID_NOT_EXPECTED",
    )
    _add_check(
        checks,
        "candidate_record_b_id_exact",
        request.get("candidate_record_b_id") == CANDIDATE_B_ID,
        CANDIDATE_B_ID,
        request.get("candidate_record_b_id"),
        "CANDIDATE_RECORD_B_ID_NOT_EXPECTED",
    )
    _add_check(
        checks,
        "candidate_record_a_role_exact",
        request.get("candidate_record_a_role") == CANDIDATE_A_ROLE,
        CANDIDATE_A_ROLE,
        request.get("candidate_record_a_role"),
        "CANDIDATE_RECORD_A_ROLE_NOT_EXPECTED",
    )
    _add_check(
        checks,
        "candidate_record_b_role_exact",
        request.get("candidate_record_b_role") == CANDIDATE_B_ROLE,
        CANDIDATE_B_ROLE,
        request.get("candidate_record_b_role"),
        "CANDIDATE_RECORD_B_ROLE_NOT_EXPECTED",
    )

    for field_name, code in CHECKED_FALSE_FIELDS:
        _validate_false_field(checks, request, field_name, code)
    for code, aliases in REQUEST_FLAG_ALIASES.items():
        triggered = [alias for alias in aliases if request.get(alias) is True]
        _add_check(checks, f"{code.lower()}_not_requested", not triggered, "request flag absent or false", triggered, code)

    _validate_required_non_claims(checks, request)
    marker_posture = {
        "operation_spec_markers_present": _validate_marker_file(
            checks, request, "operation_spec_reference", OPERATION_SPEC_MARKERS, "operation_spec_markers_present", "OPERATION_SPEC_MARKER_MISSING"
        ),
        "upstream_boundary_terminal_summary_markers_present": _validate_marker_file(
            checks,
            request,
            "candidate_specific_distinctness_basis_emission_boundary_reference",
            UPSTREAM_BOUNDARY_TERMINAL_SUMMARY_MARKERS,
            "upstream_boundary_terminal_summary_markers_present",
            "UPSTREAM_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        ),
        "completed_distinctness_operation_terminal_summary_markers_present": _validate_marker_file(
            checks,
            request,
            "completed_distinctness_operation_terminal_summary_reference",
            COMPLETED_DISTINCTNESS_OPERATION_MARKERS,
            "completed_distinctness_operation_terminal_summary_markers_present",
            "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ),
        "completed_differentiation_operation_terminal_summary_markers_present": _validate_differentiation_marker_file(
            checks, request
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
    scope_posture = _scope_posture(request)
    _validate_scope_posture(checks, scope_posture)
    _add_check(
        checks,
        "result_level_non_claims_canonical_false",
        True,
        "final result-level non-claims canonical false",
        True,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return marker_posture, scope_posture


def _build_material(request: Mapping[str, Any], recorded: bool, scope_posture: Mapping[str, Any]) -> dict[str, Any]:
    candidate_a_scope = {
        "candidate_id": CANDIDATE_A_ID,
        "candidate_role": CANDIDATE_A_ROLE,
        "candidate_scope_id": _compact_text(request.get("candidate_a_scope_id")),
        "candidate_scope_statement": _compact_text(request.get("candidate_a_scope_statement")),
        "candidate_scope_basis_summary": _compact_text(request.get("candidate_a_scope_basis")),
        "candidate_specific_content_policy": CANDIDATE_SPECIFIC_CONTENT_POLICY,
        "emitted_basis_non_standing": bool(recorded),
    }
    candidate_b_scope = {
        "candidate_id": CANDIDATE_B_ID,
        "candidate_role": CANDIDATE_B_ROLE,
        "candidate_scope_id": _compact_text(request.get("candidate_b_scope_id")),
        "candidate_scope_statement": _compact_text(request.get("candidate_b_scope_statement")),
        "candidate_scope_basis_summary": _compact_text(request.get("candidate_b_scope_basis")),
        "candidate_specific_content_policy": CANDIDATE_SPECIFIC_CONTENT_POLICY,
        "emitted_basis_non_standing": bool(recorded),
    }
    candidate_a_seal = {
        "candidate_id": CANDIDATE_A_ID,
        "scope_hash": _sha256_for(candidate_a_scope),
        "seal_material_policy": SEPARATE_SEAL_MATERIAL_POLICY,
    }
    candidate_b_seal = {
        "candidate_id": CANDIDATE_B_ID,
        "scope_hash": _sha256_for(candidate_b_scope),
        "seal_material_policy": SEPARATE_SEAL_MATERIAL_POLICY,
    }
    candidate_a_receipt = {
        "candidate_id": CANDIDATE_A_ID,
        "candidate_scope_id": candidate_a_scope["candidate_scope_id"],
        "lineage_receipt_material_policy": SEPARATE_LINEAGE_RECEIPT_MATERIAL_POLICY,
        "parent_basis_reference": str(request.get("parent_basis_reference") or ""),
    }
    candidate_b_receipt = {
        "candidate_id": CANDIDATE_B_ID,
        "candidate_scope_id": candidate_b_scope["candidate_scope_id"],
        "lineage_receipt_material_policy": SEPARATE_LINEAGE_RECEIPT_MATERIAL_POLICY,
        "parent_basis_reference": str(request.get("parent_basis_reference") or ""),
    }
    a_scope_hash = _sha256_for(candidate_a_scope)
    b_scope_hash = _sha256_for(candidate_b_scope)
    a_content_hash = _sha256_for({"candidate_specific_content": candidate_a_scope, "scope_hash": a_scope_hash})
    b_content_hash = _sha256_for({"candidate_specific_content": candidate_b_scope, "scope_hash": b_scope_hash})
    a_seal_hash = _sha256_for(candidate_a_seal)
    b_seal_hash = _sha256_for(candidate_b_seal)
    a_receipt_hash = _sha256_for(candidate_a_receipt)
    b_receipt_hash = _sha256_for(candidate_b_receipt)
    return {
        "material_emitted": recorded,
        "candidate_a_scope_id": candidate_a_scope["candidate_scope_id"],
        "candidate_b_scope_id": candidate_b_scope["candidate_scope_id"],
        "candidate_a_scope_statement": candidate_a_scope["candidate_scope_statement"],
        "candidate_b_scope_statement": candidate_b_scope["candidate_scope_statement"],
        "candidate_a_scope_basis_summary": candidate_a_scope["candidate_scope_basis_summary"],
        "candidate_b_scope_basis_summary": candidate_b_scope["candidate_scope_basis_summary"],
        "candidate_a_candidate_specific_content_reference": "result://candidate_a/candidate_specific_content" if recorded else "",
        "candidate_b_candidate_specific_content_reference": "result://candidate_b/candidate_specific_content" if recorded else "",
        "candidate_a_seal_reference": "result://candidate_a/seal_material" if recorded else "",
        "candidate_b_seal_reference": "result://candidate_b/seal_material" if recorded else "",
        "candidate_a_lineage_receipt_reference": "result://candidate_a/lineage_receipt" if recorded else "",
        "candidate_b_lineage_receipt_reference": "result://candidate_b/lineage_receipt" if recorded else "",
        "candidate_a_digest_reference": "result://candidate_a/digest" if recorded else "",
        "candidate_b_digest_reference": "result://candidate_b/digest" if recorded else "",
        "candidate_a_scope_hash": a_scope_hash if recorded else "",
        "candidate_b_scope_hash": b_scope_hash if recorded else "",
        "candidate_a_content_hash": a_content_hash if recorded else "",
        "candidate_b_content_hash": b_content_hash if recorded else "",
        "candidate_a_seal_hash": a_seal_hash if recorded else "",
        "candidate_b_seal_hash": b_seal_hash if recorded else "",
        "candidate_a_lineage_receipt_hash": a_receipt_hash if recorded else "",
        "candidate_b_lineage_receipt_hash": b_receipt_hash if recorded else "",
        "candidate_a_digest_value": _sha256_for({"content_hash": a_content_hash, "seal_hash": a_seal_hash, "receipt_hash": a_receipt_hash}) if recorded else "",
        "candidate_b_digest_value": _sha256_for({"content_hash": b_content_hash, "seal_hash": b_seal_hash, "receipt_hash": b_receipt_hash}) if recorded else "",
        "scope_division_non_cosmetic": bool(recorded and scope_posture.get("scope_division_non_cosmetic")),
        "candidate_specific_content_basis_bearing": bool(recorded and scope_posture.get("candidate_specific_content_basis_bearing")),
        "cosmetic_substitution_detected": bool(scope_posture.get("candidate_scopes_cosmetic_only")),
        "cosmetic_substitution_treated_as_basis": False,
        "digest_laundering_detected": request.get("digest_laundering_treated_as_basis") is True,
        "digest_laundering_treated_as_basis": False,
        "id_role_label_difference_treated_as_basis": False,
        "shared_evidence_treated_as_basis": False,
        "operation_evidence_alone_treated_as_basis": False,
        "emitted_basis_non_standing": recorded,
        "candidate_records_remain_non_standing": recorded,
        "candidate_records_remain_not_descendant_bodies": recorded,
    }


def _build_operation_object(
    request: Mapping[str, Any],
    recorded: bool,
    marker_posture: Mapping[str, bool],
    scope_posture: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "candidate_specific_distinctness_basis_emission_operation_id": _sanitize_value(
            "candidate_specific_distinctness_basis_emission_operation_id",
            request.get("candidate_specific_distinctness_basis_emission_operation_id", DEFAULT_OPERATION_ID),
        ),
        "candidate_specific_distinctness_basis_emission_operation_type": (
            OPERATION_TYPE
            if request.get("candidate_specific_distinctness_basis_emission_operation_type") == OPERATION_TYPE
            else ""
        ),
        "candidate_specific_distinctness_basis_emission_operation_version": (
            OPERATION_VERSION
            if request.get("candidate_specific_distinctness_basis_emission_operation_version") == OPERATION_VERSION
            else ""
        ),
        "candidate_specific_distinctness_basis_emission_operation_scope": (
            OPERATION_SCOPE
            if request.get("candidate_specific_distinctness_basis_emission_operation_scope") == OPERATION_SCOPE
            else ""
        ),
        "candidate_specific_distinctness_basis_emission_operation_implemented": False,
        "candidate_specific_distinctness_basis_emission_operation_created": False,
        "candidate_specific_distinctness_basis_emission_operation_performed": False,
        "candidate_specific_distinctness_basis_emission_operation_recorded": recorded,
        "candidate_specific_content_emitted": recorded,
        "separate_seal_material_emitted": recorded,
        "separate_lineage_receipt_material_emitted": recorded,
        "separate_digest_material_emitted": recorded,
        "candidate_a_scope_id": _compact_text(request.get("candidate_a_scope_id")) if recorded else "",
        "candidate_b_scope_id": _compact_text(request.get("candidate_b_scope_id")) if recorded else "",
        "scope_division_non_cosmetic": bool(recorded and scope_posture.get("scope_division_non_cosmetic")),
        "candidate_specific_content_basis_bearing": bool(recorded and scope_posture.get("candidate_specific_content_basis_bearing")),
        "emitted_basis_non_standing": recorded,
        "candidate_records_remain_non_standing": recorded,
        "candidate_records_remain_not_descendant_bodies": recorded,
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
        "first_crossing_authorized": False,
        "standing_authorized": False,
        "crossing_authorized": False,
        "relation_created": False,
        "relation_authorized": False,
        "field_machinery_created": False,
        "field_machinery_authorized": False,
        "runtime_created": False,
        "runtime_authorized": False,
        "api_created": False,
        "currentness_created": False,
        "currentness_authorized": False,
        "authority_created": False,
        "authority_authorized": False,
        "standing_created": False,
        "output_authorized": False,
        "action_authorized": False,
        "derivative_reception_authorized": False,
        "synchronization_authorized": False,
        "follow_on_authorized": False,
        "follow_on_work_authorized": False,
        "prior_unsupported_candidate_a_claim_validated": False,
        "prior_unsupported_candidate_b_claim_validated": False,
        "prior_unsupported_derivation_event_claim_validated": False,
        "valid_derivation_event_recorded": False,
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
        "candidate_specific_distinctness_basis_emission_boundary_overridden": False,
        "candidate_specific_distinctness_basis_emission_boundary_bypassed": False,
        "scan_allowed": False,
        "repair_allowed": False,
        "validation_enforcement_allowed": False,
        "scan_performed": False,
        "repository_scan_performed": False,
        "repair_performed": False,
        "validation_enforced": False,
        "hidden_repair_performed": False,
        "silent_overwrite_performed": False,
        "cosmetic_substitution_treated_as_basis": False,
        "digest_laundering_treated_as_basis": False,
        "id_role_label_difference_treated_as_basis": False,
        "shared_evidence_treated_as_basis": False,
        "operation_evidence_alone_treated_as_basis": False,
        "divergent_receipt_history_route_authorized": False,
        "carrier_separation_route_authorized": False,
        "operation_spec_markers_present": bool(marker_posture.get("operation_spec_markers_present")),
        "upstream_boundary_terminal_summary_markers_present": bool(
            marker_posture.get("upstream_boundary_terminal_summary_markers_present")
        ),
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
        "candidate_specific_distinctness_basis_emission_operation_id",
        "candidate_specific_distinctness_basis_emission_operation_question",
        "candidate_specific_distinctness_basis_emission_operation_intent",
        "candidate_specific_distinctness_basis_emission_operation_type",
        "candidate_specific_distinctness_basis_emission_operation_version",
        "candidate_specific_distinctness_basis_emission_operation_scope",
        "candidate_specific_distinctness_basis_emission_boundary_reference",
        "candidate_specific_distinctness_basis_emission_boundary_artifact_reference",
        "completed_distinctness_operation_terminal_summary_reference",
        "completed_differentiation_operation_terminal_summary_reference",
        "completed_distinctness_operation_boundary_terminal_summary_reference",
        "operation_spec_reference",
        "candidate_record_a_id",
        "candidate_record_b_id",
        "candidate_record_a_role",
        "candidate_record_b_role",
        "parent_basis_reference",
        "admissible_future_basis_route",
        "scope_division_policy",
        "candidate_specific_content_policy",
        "separate_seal_material_policy",
        "separate_lineage_receipt_material_policy",
        "separate_digest_material_policy",
        "cosmetic_substitution_policy",
        "digest_laundering_policy",
        "id_role_label_difference_policy",
        "shared_evidence_policy",
        "operation_evidence_policy",
        "candidate_a_scope_id",
        "candidate_b_scope_id",
    )
    return {field: _sanitize_value(field, request.get(field)) for field in fields}


def _not_recorded_basis(outcome: str) -> list[str]:
    if outcome == OUTCOME_NOT_RECORDED:
        return ["DO_NOT_RECORD intent was declared."]
    return []


def _what_remains_open() -> list[str]:
    return [
        "candidate-specific distinctness basis emission test",
        "candidate-specific distinctness basis emission artifact",
        "candidate-specific distinctness basis emission terminal summary",
        "future distinctness-supported operation result",
        "divergent receipt-history route",
        "carrier separation route",
        "candidate-record standing checks",
        "first crossing",
        "relation",
        "FIELD machinery",
        "runtime",
        "API",
        "currentness",
        "authority",
        "output authorization",
        "action authorization",
        "derivative reception",
        "synchronization",
        "affected-file repair successor, if ever separately bounded",
        "follow-on work",
    ]


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    marker_posture: Mapping[str, bool],
    scope_posture: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    non_claims = _canonical_false_non_claims()
    operation = _build_operation_object(request, recorded, marker_posture, scope_posture)
    material = _build_material(request, recorded, scope_posture)
    additional_basis = _additional_basis_required(scope_posture) if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS else []
    code, reason = _first_failed_code(checks)
    block = (
        {"blocked": True, "code": code, "block_code": code, "reason": reason}
        if outcome == OUTCOME_BLOCKED
        else {"blocked": False, "code": None, "block_code": None, "reason": None}
    )
    result: dict[str, Any] = {
        "candidate_specific_distinctness_basis_emission_operation_metadata": {
            "candidate_specific_distinctness_basis_emission_operation_id": operation[
                "candidate_specific_distinctness_basis_emission_operation_id"
            ],
            "operation_type": OPERATION_TYPE,
            "result_version": RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_candidate_specific_distinctness_basis_emission_operation_question": _declared_question_section(
            request
        ),
        "upstream_basis": {
            "candidate_specific_distinctness_basis_emission_boundary_reference": _sanitize_value(
                "candidate_specific_distinctness_basis_emission_boundary_reference",
                request.get("candidate_specific_distinctness_basis_emission_boundary_reference"),
            ),
            "candidate_specific_distinctness_basis_emission_boundary_artifact_reference": _sanitize_value(
                "candidate_specific_distinctness_basis_emission_boundary_artifact_reference",
                request.get("candidate_specific_distinctness_basis_emission_boundary_artifact_reference"),
            ),
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
            "parent_basis_reference": _sanitize_value("parent_basis_reference", request.get("parent_basis_reference")),
            "candidate_record_a_id": CANDIDATE_A_ID,
            "candidate_record_b_id": CANDIDATE_B_ID,
            "candidate_record_a_role": CANDIDATE_A_ROLE,
            "candidate_record_b_role": CANDIDATE_B_ROLE,
        },
        "candidate_specific_distinctness_basis_emission_operation_basis": {
            "operation_spec_reference": _sanitize_value("operation_spec_reference", request.get("operation_spec_reference")),
            "admissible_future_basis_route": ADMISSIBLE_FUTURE_BASIS_ROUTE,
            "scope_division_policy": SCOPE_DIVISION_POLICY,
            "candidate_specific_content_policy": CANDIDATE_SPECIFIC_CONTENT_POLICY,
            "separate_seal_material_policy": SEPARATE_SEAL_MATERIAL_POLICY,
            "separate_lineage_receipt_material_policy": SEPARATE_LINEAGE_RECEIPT_MATERIAL_POLICY,
            "separate_digest_material_policy": SEPARATE_DIGEST_MATERIAL_POLICY,
            "cosmetic_substitution_policy": COSMETIC_SUBSTITUTION_POLICY,
            "digest_laundering_policy": DIGEST_LAUNDERING_POLICY,
            "id_role_label_difference_policy": ID_ROLE_LABEL_DIFFERENCE_POLICY,
            "shared_evidence_policy": SHARED_EVIDENCE_POLICY,
            "operation_evidence_policy": OPERATION_EVIDENCE_POLICY,
            "operation_spec_markers_present": bool(marker_posture.get("operation_spec_markers_present")),
            "upstream_boundary_terminal_summary_markers_present": bool(
                marker_posture.get("upstream_boundary_terminal_summary_markers_present")
            ),
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
        "descendant_body_candidate_specific_distinctness_basis_emission_operation": operation,
        "descendant_body_candidate_specific_distinctness_basis_emission_material": material,
        "candidate_specific_distinctness_basis_emission_operation_checks": checks,
        "candidate_specific_distinctness_basis_emission_operation_statement": {
            "candidate_specific_distinctness_basis_emission_operation_recorded": recorded,
            "candidate_specific_content_emitted": recorded,
            "separate_seal_material_emitted": recorded,
            "separate_lineage_receipt_material_emitted": recorded,
            "separate_digest_material_emitted": recorded,
            "additional_basis_required_recorded": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "missing_candidate_a_scope_recorded": "missing non-cosmetic candidate A scope" in additional_basis,
            "missing_candidate_b_scope_recorded": "missing non-cosmetic candidate B scope" in additional_basis,
            "missing_non_cosmetic_scope_division_recorded": "missing basis-bearing scope division" in additional_basis,
            "scope_division_non_cosmetic": operation["scope_division_non_cosmetic"],
            "candidate_specific_content_basis_bearing": operation["candidate_specific_content_basis_bearing"],
            "emitted_basis_non_standing": operation["emitted_basis_non_standing"],
            "candidate_records_remain_non_standing": operation["candidate_records_remain_non_standing"],
            "candidate_records_remain_not_descendant_bodies": operation[
                "candidate_records_remain_not_descendant_bodies"
            ],
            "distinctness_operation_rerun": False,
            "distinctness_supported_recorded": False,
            "candidate_records_marked_distinct": False,
            "candidate_standing_authorized": False,
            "descendant_body_created": False,
            "crossing_authorized": False,
            "relation_authorized": False,
            "follow_on_authorized": False,
            "result_level_non_claims_canonical_false": all(value is False for value in non_claims.values()),
        },
        "candidate_specific_distinctness_basis_emission_operation_non_meaning": {
            "distinctness_operation_rerun": False,
            "distinctness_supported_recorded": False,
            "candidate_records_marked_distinct": False,
            "candidate_records_distinct": False,
            "candidate_standing_authorized": False,
            "descendant_body_created": False,
            "standing_authorized": False,
            "crossing_authorized": False,
            "relation_authorized": False,
            "field_machinery_authorized": False,
            "runtime_authorized": False,
            "api_created": False,
            "currentness_authorized": False,
            "authority_authorized": False,
            "output_authorized": False,
            "action_authorized": False,
            "derivative_reception_authorized": False,
            "synchronization_authorized": False,
            "follow_on_authorized": False,
            "scan_performed": False,
            "repository_scan_performed": False,
            "repair_performed": False,
            "validation_enforced": False,
            "affected_file_repaired": False,
            "affected_file_treated_as_clean_basis": False,
            "contaminated_lineage_treated_as_clean_basis": False,
        },
        "additional_basis_required": additional_basis,
        "not_recorded_basis": _not_recorded_basis(outcome),
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
        "candidate_specific_distinctness_basis_emission_operation_summary": {},
    }
    result["candidate_specific_distinctness_basis_emission_operation_summary"] = (
        build_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_summary(result)
    )
    return result


def build_declared_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_request(
    *,
    candidate_specific_distinctness_basis_emission_operation_id: str = DEFAULT_OPERATION_ID,
    candidate_specific_distinctness_basis_emission_operation_question: str = DEFAULT_OPERATION_QUESTION,
    candidate_specific_distinctness_basis_emission_operation_intent: str = INTENT_RECORD,
    candidate_specific_distinctness_basis_emission_operation_type: str = OPERATION_TYPE,
    candidate_specific_distinctness_basis_emission_operation_version: str = OPERATION_VERSION,
    candidate_specific_distinctness_basis_emission_operation_scope: str = OPERATION_SCOPE,
    candidate_specific_distinctness_basis_emission_boundary_reference: str = DEFAULT_BOUNDARY_REFERENCE,
    candidate_specific_distinctness_basis_emission_boundary_artifact_reference: str = DEFAULT_BOUNDARY_ARTIFACT_REFERENCE,
    completed_distinctness_operation_terminal_summary_reference: str = DEFAULT_COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE,
    completed_differentiation_operation_terminal_summary_reference: str = DEFAULT_COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
    completed_distinctness_operation_boundary_terminal_summary_reference: str = DEFAULT_COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
    operation_spec_reference: str = DEFAULT_OPERATION_SPEC_REFERENCE,
    candidate_record_a_id: str = CANDIDATE_A_ID,
    candidate_record_b_id: str = CANDIDATE_B_ID,
    candidate_record_a_role: str = CANDIDATE_A_ROLE,
    candidate_record_b_role: str = CANDIDATE_B_ROLE,
    parent_basis_reference: str = DEFAULT_PARENT_BASIS_REFERENCE,
    admissible_future_basis_route: str = ADMISSIBLE_FUTURE_BASIS_ROUTE,
    scope_division_policy: str = SCOPE_DIVISION_POLICY,
    candidate_a_scope_id: str = "",
    candidate_b_scope_id: str = "",
    candidate_a_scope_statement: str = "",
    candidate_b_scope_statement: str = "",
    candidate_a_scope_basis: str = "",
    candidate_b_scope_basis: str = "",
    candidate_specific_content_policy: str = CANDIDATE_SPECIFIC_CONTENT_POLICY,
    separate_seal_material_policy: str = SEPARATE_SEAL_MATERIAL_POLICY,
    separate_lineage_receipt_material_policy: str = SEPARATE_LINEAGE_RECEIPT_MATERIAL_POLICY,
    separate_digest_material_policy: str = SEPARATE_DIGEST_MATERIAL_POLICY,
    cosmetic_substitution_policy: str = COSMETIC_SUBSTITUTION_POLICY,
    digest_laundering_policy: str = DIGEST_LAUNDERING_POLICY,
    id_role_label_difference_policy: str = ID_ROLE_LABEL_DIFFERENCE_POLICY,
    shared_evidence_policy: str = SHARED_EVIDENCE_POLICY,
    operation_evidence_policy: str = OPERATION_EVIDENCE_POLICY,
    divergent_receipt_history_route_authorized: bool = False,
    carrier_separation_route_authorized: bool = False,
    candidate_standing_authorized: bool = False,
    descendant_body_created: bool = False,
    standing_authorized: bool = False,
    crossing_authorized: bool = False,
    relation_authorized: bool = False,
    field_machinery_authorized: bool = False,
    runtime_authorized: bool = False,
    currentness_authorized: bool = False,
    authority_authorized: bool = False,
    output_authorized: bool = False,
    action_authorized: bool = False,
    derivative_reception_authorized: bool = False,
    synchronization_authorized: bool = False,
    follow_on_authorized: bool = False,
    scan_allowed: bool = False,
    repair_allowed: bool = False,
    validation_enforcement_allowed: bool = False,
    scope_division_non_cosmetic: bool = False,
    candidate_specific_content_basis_bearing: bool = False,
    candidate_scopes_template_substitution_only: bool = False,
    declared_non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "candidate_specific_distinctness_basis_emission_operation_id": candidate_specific_distinctness_basis_emission_operation_id,
        "candidate_specific_distinctness_basis_emission_operation_question": candidate_specific_distinctness_basis_emission_operation_question,
        "candidate_specific_distinctness_basis_emission_operation_intent": candidate_specific_distinctness_basis_emission_operation_intent,
        "candidate_specific_distinctness_basis_emission_operation_type": candidate_specific_distinctness_basis_emission_operation_type,
        "candidate_specific_distinctness_basis_emission_operation_version": candidate_specific_distinctness_basis_emission_operation_version,
        "candidate_specific_distinctness_basis_emission_operation_scope": candidate_specific_distinctness_basis_emission_operation_scope,
        "candidate_specific_distinctness_basis_emission_boundary_reference": candidate_specific_distinctness_basis_emission_boundary_reference,
        "candidate_specific_distinctness_basis_emission_boundary_artifact_reference": candidate_specific_distinctness_basis_emission_boundary_artifact_reference,
        "completed_distinctness_operation_terminal_summary_reference": completed_distinctness_operation_terminal_summary_reference,
        "completed_differentiation_operation_terminal_summary_reference": completed_differentiation_operation_terminal_summary_reference,
        "completed_distinctness_operation_boundary_terminal_summary_reference": completed_distinctness_operation_boundary_terminal_summary_reference,
        "operation_spec_reference": operation_spec_reference,
        "candidate_record_a_id": candidate_record_a_id,
        "candidate_record_b_id": candidate_record_b_id,
        "candidate_record_a_role": candidate_record_a_role,
        "candidate_record_b_role": candidate_record_b_role,
        "parent_basis_reference": parent_basis_reference,
        "admissible_future_basis_route": admissible_future_basis_route,
        "scope_division_policy": scope_division_policy,
        "candidate_a_scope_id": candidate_a_scope_id,
        "candidate_b_scope_id": candidate_b_scope_id,
        "candidate_a_scope_statement": candidate_a_scope_statement,
        "candidate_b_scope_statement": candidate_b_scope_statement,
        "candidate_a_scope_basis": candidate_a_scope_basis,
        "candidate_b_scope_basis": candidate_b_scope_basis,
        "candidate_specific_content_policy": candidate_specific_content_policy,
        "separate_seal_material_policy": separate_seal_material_policy,
        "separate_lineage_receipt_material_policy": separate_lineage_receipt_material_policy,
        "separate_digest_material_policy": separate_digest_material_policy,
        "cosmetic_substitution_policy": cosmetic_substitution_policy,
        "digest_laundering_policy": digest_laundering_policy,
        "id_role_label_difference_policy": id_role_label_difference_policy,
        "shared_evidence_policy": shared_evidence_policy,
        "operation_evidence_policy": operation_evidence_policy,
        "divergent_receipt_history_route_authorized": divergent_receipt_history_route_authorized,
        "carrier_separation_route_authorized": carrier_separation_route_authorized,
        "candidate_standing_authorized": candidate_standing_authorized,
        "descendant_body_created": descendant_body_created,
        "standing_authorized": standing_authorized,
        "crossing_authorized": crossing_authorized,
        "relation_authorized": relation_authorized,
        "field_machinery_authorized": field_machinery_authorized,
        "runtime_authorized": runtime_authorized,
        "currentness_authorized": currentness_authorized,
        "authority_authorized": authority_authorized,
        "output_authorized": output_authorized,
        "action_authorized": action_authorized,
        "derivative_reception_authorized": derivative_reception_authorized,
        "synchronization_authorized": synchronization_authorized,
        "follow_on_authorized": follow_on_authorized,
        "scan_allowed": scan_allowed,
        "repair_allowed": repair_allowed,
        "validation_enforcement_allowed": validation_enforcement_allowed,
        "scope_division_non_cosmetic": scope_division_non_cosmetic,
        "candidate_specific_content_basis_bearing": candidate_specific_content_basis_bearing,
        "candidate_scopes_template_substitution_only": candidate_scopes_template_substitution_only,
        "candidate_specific_distinctness_basis_emission_operation_implemented": False,
        "candidate_specific_distinctness_basis_emission_operation_created": False,
        "candidate_specific_distinctness_basis_emission_operation_performed": False,
        "candidate_specific_distinctness_basis_emission_operation_recorded": False,
        "candidate_specific_content_emitted": False,
        "separate_seal_material_emitted": False,
        "separate_lineage_receipt_material_emitted": False,
        "separate_digest_material_emitted": False,
        "distinctness_operation_rerun": False,
        "distinctness_supported_recorded": False,
        "candidate_records_marked_distinct": False,
        "candidate_records_distinct": False,
        "candidate_standing_created": False,
        "descendant_body_a_created": False,
        "descendant_body_b_created": False,
        "standing_descendant_created": False,
        "descendant_standing_check_performed": False,
        "first_crossing_authorized": False,
        "relation_created": False,
        "field_machinery_created": False,
        "runtime_created": False,
        "api_created": False,
        "currentness_created": False,
        "authority_created": False,
        "standing_created": False,
        "follow_on_work_authorized": False,
        "prior_unsupported_candidate_a_claim_validated": False,
        "prior_unsupported_candidate_b_claim_validated": False,
        "prior_unsupported_derivation_event_claim_validated": False,
        "valid_derivation_event_recorded": False,
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
        "candidate_specific_distinctness_basis_emission_boundary_overridden": False,
        "candidate_specific_distinctness_basis_emission_boundary_bypassed": False,
        "scan_performed": False,
        "repository_scan_performed": False,
        "repair_performed": False,
        "validation_enforced": False,
        "hidden_repair_performed": False,
        "silent_overwrite_performed": False,
        "cosmetic_substitution_treated_as_basis": False,
        "digest_laundering_treated_as_basis": False,
        "id_role_label_difference_treated_as_basis": False,
        "shared_evidence_treated_as_basis": False,
        "operation_evidence_alone_treated_as_basis": False,
        "declared_non_claims": dict(declared_non_claims) if declared_non_claims is not None else _canonical_false_non_claims(),
    }
    return request


def resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
    declared_candidate_specific_distinctness_basis_emission_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_candidate_specific_distinctness_basis_emission_operation is None:
        request: Mapping[str, Any] = (
            build_declared_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_request()
        )
    elif not isinstance(declared_candidate_specific_distinctness_basis_emission_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_operation_request_mapping",
            False,
            "mapping request",
            type(declared_candidate_specific_distinctness_basis_emission_operation).__name__,
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUEST_MALFORMED",
        )
        request = build_declared_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_request()
        return _build_result(request, checks, {}, _scope_posture(request), OUTCOME_BLOCKED)
    else:
        request = copy.deepcopy(dict(declared_candidate_specific_distinctness_basis_emission_operation))

    checks: list[dict[str, Any]] = []
    marker_posture, scope_posture = _validate_request(checks, request)
    intent = request.get("candidate_specific_distinctness_basis_emission_operation_intent")
    if _failed_check_count(checks) > 0:
        return _build_result(request, checks, marker_posture, scope_posture, OUTCOME_BLOCKED)
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, checks, marker_posture, scope_posture, OUTCOME_NOT_RECORDED)
    if scope_posture.get("ready_to_record") is not True:
        return _build_result(request, checks, marker_posture, scope_posture, OUTCOME_REQUIRES_ADDITIONAL_BASIS)
    return _build_result(request, checks, marker_posture, scope_posture, OUTCOME_RECORDED)


def resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_from_path(
    declared_candidate_specific_distinctness_basis_emission_operation_path: Path | str,
) -> dict[str, Any]:
    path = Path(declared_candidate_specific_distinctness_basis_emission_operation_path)
    if not path.is_absolute():
        path = REPO_ROOT / path
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except (OSError, json.JSONDecodeError):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_operation_request_readable",
            False,
            "readable JSON object request",
            str(path),
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUEST_UNREADABLE",
        )
        request = build_declared_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_request()
        return _build_result(request, checks, {}, _scope_posture(request), OUTCOME_BLOCKED)
    if not isinstance(loaded, Mapping):
        checks = []
        _add_check(
            checks,
            "declared_operation_request_mapping",
            False,
            "JSON object request",
            type(loaded).__name__,
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUEST_MALFORMED",
        )
        request = build_declared_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_request()
        return _build_result(request, checks, {}, _scope_posture(request), OUTCOME_BLOCKED)
    return resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(loaded)


def build_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("candidate_specific_distinctness_basis_emission_operation_checks", [])
    check_list = list(checks) if isinstance(checks, list) else []
    operation_value = result.get("descendant_body_candidate_specific_distinctness_basis_emission_operation", {})
    operation = operation_value if isinstance(operation_value, Mapping) else {}
    material_value = result.get("descendant_body_candidate_specific_distinctness_basis_emission_material", {})
    material = material_value if isinstance(material_value, Mapping) else {}
    declared_value = result.get("declared_candidate_specific_distinctness_basis_emission_operation_question", {})
    declared = declared_value if isinstance(declared_value, Mapping) else {}
    block_value = result.get("block", {})
    block = block_value if isinstance(block_value, Mapping) else {}
    non_claim_value = result.get("non_claims", {})
    non_claims = non_claim_value if isinstance(non_claim_value, Mapping) else {}
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "candidate_specific_distinctness_basis_emission_operation_id": operation.get(
            "candidate_specific_distinctness_basis_emission_operation_id"
        ),
        "question": declared.get("candidate_specific_distinctness_basis_emission_operation_question"),
        "intent": declared.get("candidate_specific_distinctness_basis_emission_operation_intent"),
        "passed_check_count": _passed_check_count(check_list),
        "failed_check_count": _failed_check_count(check_list),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "operation_type": operation.get("candidate_specific_distinctness_basis_emission_operation_type"),
        "operation_version": operation.get("candidate_specific_distinctness_basis_emission_operation_version"),
        "operation_scope": operation.get("candidate_specific_distinctness_basis_emission_operation_scope"),
        "admissible_future_basis_route": ADMISSIBLE_FUTURE_BASIS_ROUTE,
        "scope_division_policy": SCOPE_DIVISION_POLICY,
        "candidate_specific_content_policy": CANDIDATE_SPECIFIC_CONTENT_POLICY,
        "separate_seal_material_policy": SEPARATE_SEAL_MATERIAL_POLICY,
        "separate_lineage_receipt_material_policy": SEPARATE_LINEAGE_RECEIPT_MATERIAL_POLICY,
        "separate_digest_material_policy": SEPARATE_DIGEST_MATERIAL_POLICY,
        "cosmetic_substitution_policy": COSMETIC_SUBSTITUTION_POLICY,
        "digest_laundering_policy": DIGEST_LAUNDERING_POLICY,
        "id_role_label_difference_policy": ID_ROLE_LABEL_DIFFERENCE_POLICY,
        "shared_evidence_policy": SHARED_EVIDENCE_POLICY,
        "operation_evidence_policy": OPERATION_EVIDENCE_POLICY,
        "candidate_record_a_id": CANDIDATE_A_ID,
        "candidate_record_b_id": CANDIDATE_B_ID,
        "candidate_record_a_role": CANDIDATE_A_ROLE,
        "candidate_record_b_role": CANDIDATE_B_ROLE,
        "candidate_a_scope_id": operation.get("candidate_a_scope_id"),
        "candidate_b_scope_id": operation.get("candidate_b_scope_id"),
        "scope_division_non_cosmetic": operation.get("scope_division_non_cosmetic"),
        "candidate_specific_content_basis_bearing": operation.get("candidate_specific_content_basis_bearing"),
        "material_emitted": material.get("material_emitted"),
        "candidate_specific_distinctness_basis_emission_operation_recorded": operation.get(
            "candidate_specific_distinctness_basis_emission_operation_recorded"
        ),
        "candidate_specific_content_emitted": operation.get("candidate_specific_content_emitted"),
        "separate_seal_material_emitted": operation.get("separate_seal_material_emitted"),
        "separate_lineage_receipt_material_emitted": operation.get("separate_lineage_receipt_material_emitted"),
        "separate_digest_material_emitted": operation.get("separate_digest_material_emitted"),
        "additional_basis_required": list(result.get("additional_basis_required", []))
        if isinstance(result.get("additional_basis_required"), list)
        else [],
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
        "prior_unsupported_candidate_a_claim_validated": False,
        "prior_unsupported_candidate_b_claim_validated": False,
        "prior_unsupported_derivation_event_claim_validated": False,
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
        "candidate_specific_distinctness_basis_emission_boundary_overridden": False,
        "candidate_specific_distinctness_basis_emission_boundary_bypassed": False,
        "scan_not_performed": operation.get("scan_performed") is False,
        "repository_scan_not_performed": operation.get("repository_scan_performed") is False,
        "repair_not_performed": operation.get("repair_performed") is False,
        "validation_not_enforced": operation.get("validation_enforced") is False,
        "hidden_repair_not_performed": operation.get("hidden_repair_performed") is False,
        "silent_overwrite_not_performed": operation.get("silent_overwrite_performed") is False,
        "operation_spec_markers_present": operation.get("operation_spec_markers_present"),
        "upstream_boundary_terminal_summary_markers_present": operation.get(
            "upstream_boundary_terminal_summary_markers_present"
        ),
        "completed_distinctness_operation_terminal_summary_markers_present": operation.get(
            "completed_distinctness_operation_terminal_summary_markers_present"
        ),
        "completed_differentiation_operation_terminal_summary_markers_present": operation.get(
            "completed_differentiation_operation_terminal_summary_markers_present"
        ),
        "completed_distinctness_operation_boundary_terminal_summary_markers_present": operation.get(
            "completed_distinctness_operation_boundary_terminal_summary_markers_present"
        ),
        "result_level_non_claims_canonical_false": all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS),
    }


def write_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    operation_value = result.get("descendant_body_candidate_specific_distinctness_basis_emission_operation", {})
    operation_id = DEFAULT_OPERATION_ID
    if isinstance(operation_value, Mapping):
        operation_id = str(
            operation_value.get("candidate_specific_distinctness_basis_emission_operation_id") or DEFAULT_OPERATION_ID
        )
    if output_path is None:
        filename = (
            f"{_safe_filename_part(operation_id)}__"
            "candidate_specific_distinctness_basis_emission_operation_v0_min_result.json"
        )
        path = OUTPUT_ROOT / filename
    else:
        path = Path(output_path)
        if path.suffix.lower() != ".json":
            filename = (
                f"{_safe_filename_part(operation_id)}__"
                "candidate_specific_distinctness_basis_emission_operation_v0_min_result.json"
            )
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
