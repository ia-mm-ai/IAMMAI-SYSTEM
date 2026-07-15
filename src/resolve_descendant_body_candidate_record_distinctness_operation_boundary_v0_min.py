"""Resolve one descendant-body candidate-record distinctness boundary.

This resolver records one
DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY result only.
It does not perform distinctness checking, create distinctness evidence, make
candidate records distinct, authorize standing, create descendant bodies,
repair contaminated lineage, scan the repository, or authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class DescendantBodyCandidateRecordDistinctnessOperationBoundaryV0MinError(
    RuntimeError
):
    """Bounded resolver error for request/path/write handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min"
)

OUTCOME_RECORDED = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

BOUNDARY_TYPE = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY"
FUTURE_DISTINCTNESS_OPERATION_TYPE = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION"
)
FUTURE_DISTINCTNESS_OPERATION_SCOPE = (
    "TWO_NON_STANDING_CANDIDATE_RECORDS_DECLARED_ONLY"
)
DISTINCTNESS_EVIDENCE_POLICY = (
    "REQUIRE_SEPARATE_CANDIDATE_SPECIFIC_DISTINCTNESS_EVIDENCE"
)
COSMETIC_DIFFERENCE_POLICY = "ID_AND_ROLE_DIFFERENCE_ALONE_NOT_SUFFICIENT"
SHARED_EVIDENCE_POLICY = "SHARED_EVIDENCE_REFERENCE_ALONE_NOT_SUFFICIENT"
NOT_DISTINCT_POLICY = (
    "RECORD_NOT_DISTINCT_OR_BLOCK_WHEN_DISTINCTNESS_EVIDENCE_FAILS"
)
FAILURE_VISIBILITY_POLICY = "BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL"

FUTURE_DISTINCTNESS_OPERATION_OUTCOME_FAMILY = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_RECORDED",
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BLOCKED",
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_REQUIRES_ADDITIONAL_BASIS",
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_RECORDED",
)

INTENT_RECORD = (
    "RECORD_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_descendant_body_candidate_record_"
    "distinctness_operation_boundary_v0_min"
)

DEFAULT_BOUNDARY_ID = (
    "descendant_body_candidate_record_distinctness_operation_boundary_001"
)
DEFAULT_BOUNDARY_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_"
    "V0_MIN_SPEC.md"
)
DEFAULT_COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_COMPLETED_OPERATION_ARTIFACT_REFERENCE = (
    "artifacts/integrity_host_v0_min_coexistence_descendant_body_differentiation_"
    "operation_v0_min/descendant_body_differentiation_operation_001__"
    "descendant_body_differentiation_operation_v0_min_result.json"
)
DEFAULT_CONTAMINATED_LINEAGE_REFERENCE = (
    "spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_CANDIDATE_RECORD_A_ID = "descendant_body_basis_candidate_a_001"
DEFAULT_CANDIDATE_RECORD_B_ID = "descendant_body_basis_candidate_b_001"
DEFAULT_CANDIDATE_RECORD_A_ROLE = "CANDIDATE_A"
DEFAULT_CANDIDATE_RECORD_B_ROLE = "CANDIDATE_B"
DEFAULT_OPERATION_ID = "descendant_body_differentiation_operation_001"
DEFAULT_SOURCE_OPERATION_TYPE = "DESCENDANT_BODY_DIFFERENTIATION_OPERATION"
DEFAULT_SOURCE_OPERATION_SCOPE = "ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY"
DEFAULT_SOURCE_CANDIDATE_RECORD_POLICY = (
    "EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS"
)

DEFAULT_BOUNDARY_QUESTION = (
    "Given one completed descendant-body differentiation operation result that "
    "emitted exactly two result-contained non-standing candidate records with "
    "operation evidence, may the repo record a boundary allowing future "
    "consideration of exactly one separately implemented candidate-record "
    "distinctness operation that can determine whether the two candidate records "
    "are distinguishable beyond id and role by checking separately emitted "
    "distinctness evidence, and can visibly block or record NOT_DISTINCT if "
    "distinctness evidence is absent, duplicated, shared, cosmetic, or "
    "insufficient, while preserving that this boundary does not itself perform "
    "distinctness checking, create distinctness evidence, create candidate "
    "standing, create descendant bodies, authorize crossing, create relation, "
    "create FIELD machinery, create runtime, create currentness, create "
    "authority, authorize output, authorize action, authorize derivative "
    "reception, authorize synchronization, repair the affected file, validate "
    "prior unsupported claims, or authorize follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "distinctness_operation_created",
    "distinctness_operation_performed",
    "distinctness_operation_recorded",
    "distinctness_result_recorded",
    "distinctness_supported",
    "candidate_records_distinct",
    "candidate_specific_content_created",
    "separate_seal_material_created",
    "separate_lineage_receipt_material_created",
    "separate_digest_material_created",
    "candidate_standing_authorized",
    "candidate_standing_created",
    "descendant_body_a_created",
    "descendant_body_b_created",
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
    "scan_performed",
    "repository_scan_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "enumeration_treated_as_distinction",
    "id_and_role_difference_treated_as_distinctness",
    "shared_evidence_reference_treated_as_distinctness",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "descendant_body_candidate_record_distinctness_operation_boundary_recorded",
    "boundary_created",
    "completed_operation_terminal_summary_reference_declared",
    "completed_operation_artifact_reference_declared",
    "contaminated_lineage_reference_declared",
    "existence_claim_evidence_check_terminal_summary_reference_declared",
    "candidate_record_a_reference_declared",
    "candidate_record_b_reference_declared",
    "candidate_record_a_id_accepted",
    "candidate_record_b_id_accepted",
    "candidate_record_a_role_accepted",
    "candidate_record_b_role_accepted",
    "future_distinctness_operation_type_accepted",
    "future_distinctness_operation_scope_accepted",
    "distinctness_evidence_policy_accepted",
    "cosmetic_difference_policy_accepted",
    "shared_evidence_policy_accepted",
    "not_distinct_policy_accepted",
    "failure_visibility_policy_accepted",
    "future_operation_shape_declared",
    "boundary_spec_markers_present",
    "completed_operation_terminal_summary_markers_present",
    "completed_operation_artifact_markers_present",
    "contaminated_lineage_markers_present",
    "existence_claim_evidence_check_terminal_summary_markers_present",
    "completed_operation_emitted_two_candidate_records",
    "completed_operation_did_not_prove_distinctness_beyond_id_and_role",
    "distinctness_operation_not_created",
    "distinctness_operation_not_performed",
    "distinctness_operation_not_recorded",
    "distinctness_result_not_recorded",
    "distinctness_not_supported",
    "candidate_records_not_distinct",
    "candidate_specific_content_not_created",
    "separate_seal_material_not_created",
    "separate_lineage_receipt_material_not_created",
    "separate_digest_material_not_created",
    "enumeration_not_treated_as_distinction",
    "id_and_role_difference_alone_not_treated_as_distinctness",
    "shared_evidence_reference_alone_not_treated_as_distinctness",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_QUESTION_UNDECLARED",
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_INTENT_UNSUPPORTED",
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_BLOCK_REQUESTED",
    "COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "COMPLETED_OPERATION_ARTIFACT_REFERENCE_MISSING",
    "CONTAMINATED_LINEAGE_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "CANDIDATE_RECORD_A_REFERENCE_MISSING",
    "CANDIDATE_RECORD_B_REFERENCE_MISSING",
    "CANDIDATE_RECORD_A_ID_NOT_EXPECTED",
    "CANDIDATE_RECORD_B_ID_NOT_EXPECTED",
    "CANDIDATE_RECORD_A_ROLE_NOT_EXPECTED",
    "CANDIDATE_RECORD_B_ROLE_NOT_EXPECTED",
    "FUTURE_DISTINCTNESS_OPERATION_TYPE_MISSING",
    "FUTURE_DISTINCTNESS_OPERATION_TYPE_NOT_EXPECTED",
    "FUTURE_DISTINCTNESS_OPERATION_SCOPE_MISSING",
    "FUTURE_DISTINCTNESS_OPERATION_SCOPE_NOT_EXPECTED",
    "DISTINCTNESS_EVIDENCE_POLICY_MISSING",
    "DISTINCTNESS_EVIDENCE_POLICY_NOT_EXPECTED",
    "COSMETIC_DIFFERENCE_POLICY_MISSING",
    "COSMETIC_DIFFERENCE_POLICY_NOT_EXPECTED",
    "SHARED_EVIDENCE_POLICY_MISSING",
    "SHARED_EVIDENCE_POLICY_NOT_EXPECTED",
    "NOT_DISTINCT_POLICY_MISSING",
    "NOT_DISTINCT_POLICY_NOT_EXPECTED",
    "FAILURE_VISIBILITY_POLICY_MISSING",
    "FAILURE_VISIBILITY_POLICY_NOT_EXPECTED",
    "CANDIDATE_RECORD_COUNT_REQUIRED_NOT_TWO",
    "FUTURE_OPERATION_SHAPE_MISSING",
    "FUTURE_OPERATION_SHAPE_MALFORMED",
    "SCAN_ALLOWED_TRUE",
    "REPAIR_ALLOWED_TRUE",
    "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
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
    "REQUESTED_REPOSITORY_SCAN",
    "REQUESTED_FILE_DISCOVERY",
    "REQUESTED_AFFECTED_FILE_REPAIR",
    "REQUESTED_AFFECTED_FILE_MUTATION",
    "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION",
    "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDE",
    "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASS",
    "REQUESTED_DIFFERENTIATION_OPERATION_OVERRIDE",
    "REQUESTED_DIFFERENTIATION_OPERATION_BYPASS",
    "REQUESTED_DISTINCTNESS_OPERATION_PERFORMANCE",
    "REQUESTED_DISTINCTNESS_RESULT_RECORDING",
    "REQUESTED_DISTINCTNESS_EVIDENCE_CREATION",
    "REQUESTED_CANDIDATE_SPECIFIC_CONTENT_CREATION",
    "REQUESTED_SEPARATE_SEAL_MATERIAL_CREATION",
    "REQUESTED_SEPARATE_LINEAGE_RECEIPT_MATERIAL_CREATION",
    "REQUESTED_SEPARATE_DIGEST_MATERIAL_CREATION",
    "REQUESTED_CANDIDATE_RECORDS_DISTINCT",
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
    "BOUNDARY_SPEC_MARKER_MISSING",
    "COMPLETED_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
    "CONTAMINATED_LINEAGE_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "DISTINCTNESS_OPERATION_CREATED",
    "DISTINCTNESS_OPERATION_PERFORMED",
    "DISTINCTNESS_OPERATION_RECORDED",
    "DISTINCTNESS_RESULT_RECORDED",
    "DISTINCTNESS_SUPPORTED",
    "CANDIDATE_RECORDS_DISTINCT",
    "CANDIDATE_SPECIFIC_CONTENT_CREATED",
    "SEPARATE_SEAL_MATERIAL_CREATED",
    "SEPARATE_LINEAGE_RECEIPT_MATERIAL_CREATED",
    "SEPARATE_DIGEST_MATERIAL_CREATED",
    "CANDIDATE_STANDING_AUTHORIZED",
    "CANDIDATE_STANDING_CREATED",
    "DESCENDANT_BODY_A_CREATED",
    "DESCENDANT_BODY_B_CREATED",
    "STANDING_DESCENDANT_CREATED",
    "DESCENDANT_STANDING_CHECK_PERFORMED",
    "FIRST_CROSSING_AUTHORIZED",
    "RELATION_CREATED",
    "FIELD_MACHINERY_CREATED",
    "RUNTIME_CREATED",
    "API_CREATED",
    "CURRENTNESS_CREATED",
    "AUTHORITY_CREATED",
    "STANDING_CREATED",
    "OUTPUT_AUTHORIZED",
    "ACTION_AUTHORIZED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "SYNCHRONIZATION_AUTHORIZED",
    "FOLLOW_ON_WORK_AUTHORIZED",
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
    "SCAN_PERFORMED",
    "REPOSITORY_SCAN_PERFORMED",
    "REPAIR_PERFORMED",
    "VALIDATION_ENFORCED",
    "HIDDEN_REPAIR_PERFORMED",
    "SILENT_OVERWRITE_PERFORMED",
    "ENUMERATION_TREATED_AS_DISTINCTION",
    "ID_AND_ROLE_DIFFERENCE_TREATED_AS_DISTINCTNESS",
    "SHARED_EVIDENCE_REFERENCE_TREATED_AS_DISTINCTNESS",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_REQUEST_UNREADABLE",
)

FALSE_NON_CLAIM_BLOCK_CODES = {
    "distinctness_operation_created": "DISTINCTNESS_OPERATION_CREATED",
    "distinctness_operation_performed": "DISTINCTNESS_OPERATION_PERFORMED",
    "distinctness_operation_recorded": "DISTINCTNESS_OPERATION_RECORDED",
    "distinctness_result_recorded": "DISTINCTNESS_RESULT_RECORDED",
    "distinctness_supported": "DISTINCTNESS_SUPPORTED",
    "candidate_records_distinct": "CANDIDATE_RECORDS_DISTINCT",
    "candidate_specific_content_created": "CANDIDATE_SPECIFIC_CONTENT_CREATED",
    "separate_seal_material_created": "SEPARATE_SEAL_MATERIAL_CREATED",
    "separate_lineage_receipt_material_created": "SEPARATE_LINEAGE_RECEIPT_MATERIAL_CREATED",
    "separate_digest_material_created": "SEPARATE_DIGEST_MATERIAL_CREATED",
    "candidate_standing_authorized": "CANDIDATE_STANDING_AUTHORIZED",
    "candidate_standing_created": "CANDIDATE_STANDING_CREATED",
    "descendant_body_a_created": "DESCENDANT_BODY_A_CREATED",
    "descendant_body_b_created": "DESCENDANT_BODY_B_CREATED",
    "standing_descendant_created": "STANDING_DESCENDANT_CREATED",
    "descendant_standing_check_performed": "DESCENDANT_STANDING_CHECK_PERFORMED",
    "first_crossing_authorized": "FIRST_CROSSING_AUTHORIZED",
    "relation_created": "RELATION_CREATED",
    "field_machinery_created": "FIELD_MACHINERY_CREATED",
    "runtime_created": "RUNTIME_CREATED",
    "api_created": "API_CREATED",
    "currentness_created": "CURRENTNESS_CREATED",
    "authority_created": "AUTHORITY_CREATED",
    "standing_created": "STANDING_CREATED",
    "output_authorized": "OUTPUT_AUTHORIZED",
    "action_authorized": "ACTION_AUTHORIZED",
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "synchronization_authorized": "SYNCHRONIZATION_AUTHORIZED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "prior_unsupported_candidate_a_claim_validated": (
        "PRIOR_UNSUPPORTED_CANDIDATE_A_CLAIM_VALIDATED"
    ),
    "prior_unsupported_candidate_b_claim_validated": (
        "PRIOR_UNSUPPORTED_CANDIDATE_B_CLAIM_VALIDATED"
    ),
    "prior_unsupported_derivation_event_claim_validated": (
        "PRIOR_UNSUPPORTED_DERIVATION_EVENT_CLAIM_VALIDATED"
    ),
    "valid_derivation_event_recorded": "VALID_DERIVATION_EVENT_RECORDED",
    "affected_file_repaired": "AFFECTED_FILE_REPAIRED",
    "affected_file_edited": "AFFECTED_FILE_EDITED",
    "affected_file_deleted": "AFFECTED_FILE_DELETED",
    "affected_file_overwritten": "AFFECTED_FILE_OVERWRITTEN",
    "affected_file_replaced": "AFFECTED_FILE_REPLACED",
    "affected_file_redeemed": "AFFECTED_FILE_REDEEMED",
    "affected_file_treated_as_clean_basis": "AFFECTED_FILE_TREATED_AS_CLEAN_BASIS",
    "contaminated_lineage_treated_as_clean_basis": (
        "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS"
    ),
    "existence_claim_evidence_check_overridden": (
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDDEN"
    ),
    "existence_claim_evidence_check_bypassed": (
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASSED"
    ),
    "differentiation_operation_overridden": "DIFFERENTIATION_OPERATION_OVERRIDDEN",
    "differentiation_operation_bypassed": "DIFFERENTIATION_OPERATION_BYPASSED",
    "scan_performed": "SCAN_PERFORMED",
    "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
    "repair_performed": "REPAIR_PERFORMED",
    "validation_enforced": "VALIDATION_ENFORCED",
    "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
    "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
    "enumeration_treated_as_distinction": "ENUMERATION_TREATED_AS_DISTINCTION",
    "id_and_role_difference_treated_as_distinctness": (
        "ID_AND_ROLE_DIFFERENCE_TREATED_AS_DISTINCTNESS"
    ),
    "shared_evidence_reference_treated_as_distinctness": (
        "SHARED_EVIDENCE_REFERENCE_TREATED_AS_DISTINCTNESS"
    ),
}

REQUESTED_TRUE_BLOCK_CODES = {
    "repository_scan_requested": "REQUESTED_REPOSITORY_SCAN",
    "file_discovery_requested": "REQUESTED_FILE_DISCOVERY",
    "affected_file_repair_requested": "REQUESTED_AFFECTED_FILE_REPAIR",
    "affected_file_mutation_requested": "REQUESTED_AFFECTED_FILE_MUTATION",
    "prior_unsupported_claim_validation_requested": (
        "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION"
    ),
    "existence_claim_evidence_check_override_requested": (
        "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDE"
    ),
    "existence_claim_evidence_check_bypass_requested": (
        "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASS"
    ),
    "differentiation_operation_override_requested": (
        "REQUESTED_DIFFERENTIATION_OPERATION_OVERRIDE"
    ),
    "differentiation_operation_bypass_requested": (
        "REQUESTED_DIFFERENTIATION_OPERATION_BYPASS"
    ),
    "distinctness_operation_performance_requested": (
        "REQUESTED_DISTINCTNESS_OPERATION_PERFORMANCE"
    ),
    "distinctness_result_recording_requested": (
        "REQUESTED_DISTINCTNESS_RESULT_RECORDING"
    ),
    "distinctness_evidence_creation_requested": (
        "REQUESTED_DISTINCTNESS_EVIDENCE_CREATION"
    ),
    "candidate_specific_content_creation_requested": (
        "REQUESTED_CANDIDATE_SPECIFIC_CONTENT_CREATION"
    ),
    "separate_seal_material_creation_requested": (
        "REQUESTED_SEPARATE_SEAL_MATERIAL_CREATION"
    ),
    "separate_lineage_receipt_material_creation_requested": (
        "REQUESTED_SEPARATE_LINEAGE_RECEIPT_MATERIAL_CREATION"
    ),
    "separate_digest_material_creation_requested": (
        "REQUESTED_SEPARATE_DIGEST_MATERIAL_CREATION"
    ),
    "candidate_records_distinct_requested": "REQUESTED_CANDIDATE_RECORDS_DISTINCT",
    "candidate_standing_authorization_requested": (
        "REQUESTED_CANDIDATE_STANDING_AUTHORIZATION"
    ),
    "descendant_body_creation_requested": "REQUESTED_DESCENDANT_BODY_CREATION",
    "standing_descendant_creation_requested": (
        "REQUESTED_STANDING_DESCENDANT_CREATION"
    ),
    "descendant_standing_check_requested": "REQUESTED_DESCENDANT_STANDING_CHECK",
    "crossing_authorization_requested": "REQUESTED_CROSSING_AUTHORIZATION",
    "relation_creation_requested": "REQUESTED_RELATION_CREATION",
    "field_machinery_creation_requested": "REQUESTED_FIELD_MACHINERY_CREATION",
    "runtime_creation_requested": "REQUESTED_RUNTIME_CREATION",
    "currentness_creation_requested": "REQUESTED_CURRENTNESS_CREATION",
    "authority_creation_requested": "REQUESTED_AUTHORITY_CREATION",
    "output_authorization_requested": "REQUESTED_OUTPUT_AUTHORIZATION",
    "action_authorization_requested": "REQUESTED_ACTION_AUTHORIZATION",
    "derivative_reception_authorization_requested": (
        "REQUESTED_DERIVATIVE_RECEPTION_AUTHORIZATION"
    ),
    "synchronization_authorization_requested": "REQUESTED_SYNCHRONIZATION_AUTHORIZATION",
    "follow_on_authorization_requested": "REQUESTED_FOLLOW_ON_AUTHORIZATION",
    "raw_markdown_body_return_requested": "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
    "return_raw_full_markdown_bodies": "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
}

STRICT_FALSE_REQUEST_FIELDS = {
    "scan_allowed": "SCAN_ALLOWED_TRUE",
    "repair_allowed": "REPAIR_ALLOWED_TRUE",
    "validation_enforcement_allowed": "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
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
}

BOUNDARY_SPEC_MARKERS = (
    "Descendant Body Candidate Record Distinctness Operation Boundary V0 Minimum Specification",
    "This file defines one boundary for a future descendant-body candidate-record distinctness operation.",
    "This file does not perform distinctness checking.",
    (
        "The completed operation result emitted candidate records but did not prove "
        "candidate-record distinctness beyond id and role."
    ),
    "Enumeration is not distinction.",
    "Id and role difference alone are not distinctness.",
    "Shared evidence reference alone is not distinctness.",
    "boundary_created = true",
    "distinctness_operation_created = false",
    "distinctness_supported = false",
    "candidate_records_distinct = false",
    "separate_seal_material_created = false",
    "separate_lineage_receipt_material_created = false",
    "separate_digest_material_created = false",
)

COMPLETED_OPERATION_TERMINAL_SUMMARY_MARKERS = (
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
    "failed_check_count = 0",
    "passed_check_count = 161",
    "operation_id = descendant_body_differentiation_operation_001",
    "candidate_record_count_emitted = 2",
    "candidate_record_ids = descendant_body_basis_candidate_a_001, descendant_body_basis_candidate_b_001",
    "Candidate records are result-contained, non-standing, operation-evidenced records only",
    "Candidate records are not descendant bodies",
    "Candidate records are not standing descendants",
    "Candidate records are not crossing authorization",
    (
        "The completed existence-claim evidence check line remains standing as the "
        "mechanical classification that the three prior descendant existence claims "
        "are UNSUPPORTED"
    ),
)

CONTAMINATED_LINEAGE_MARKERS = (
    "descendant_body_basis_candidate_a_created = true",
    "descendant_body_basis_candidate_b_created = true",
    "descendant_body_basis_derivation_event_recorded = true",
)

EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKERS = (
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_RECORDED",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_CONTAMINATED_CLASS",
    "descendant_body_basis_candidate_a_created = UNSUPPORTED",
    "descendant_body_basis_candidate_b_created = UNSUPPORTED",
    "descendant_body_basis_derivation_event_recorded = UNSUPPORTED",
    "Contaminated lineage is not clean basis",
)

MARKER_ALTERNATIVES = {
    "Candidate records are not crossing authorization": (
        (
            "Candidate records are not descendant bodies, not standing descendants, "
            "not crossing authorization"
        ),
    ),
}

FUTURE_OPERATION_SHAPE_FIELDS = (
    "distinctness_operation_id",
    "distinctness_operation_type",
    "distinctness_operation_version",
    "distinctness_operation_scope",
    "distinctness_operation_intent",
    "candidate_record_a_reference",
    "candidate_record_b_reference",
    "candidate_record_source_operation_reference",
    "candidate_record_source_operation_artifact_reference",
    "candidate_record_a_id",
    "candidate_record_b_id",
    "candidate_record_a_role",
    "candidate_record_b_role",
    "distinctness_evidence_policy",
    "cosmetic_difference_policy",
    "shared_evidence_policy",
    "not_distinct_policy",
    "failure_visibility_policy",
    "candidate_record_count_required",
    "scan_allowed",
    "repair_allowed",
    "validation_enforcement_allowed",
    "candidate_standing_authorized",
    "descendant_body_created",
    "standing_authorized",
    "crossing_authorized",
    "relation_authorized",
    "field_machinery_authorized",
    "runtime_authorized",
    "currentness_authorized",
    "authority_authorized",
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "declared_non_claims",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_mapping(value: Any) -> bool:
    return isinstance(value, MappingABC)


def _resolve_reference_path(reference: Any) -> Path:
    path = Path(str(reference))
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def _read_text(reference: Any) -> str:
    path = _resolve_reference_path(reference)
    return path.read_text(encoding="utf-8")


def _read_json(reference: Any) -> Any:
    path = _resolve_reference_path(reference)
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _sanitize_json_value(value: Any, key: str | None = None) -> Any:
    key_text = (key or "").lower()
    sensitive = {
        "raw_body",
        "full_body",
        "markdown_body",
        "hidden_repo_state",
        "local_cache",
        "current_working_tree",
    }
    if key_text in sensitive or key_text.endswith("_body"):
        return "[REDACTED_RAW_BODY]"
    if _is_mapping(value):
        return {
            str(item_key): _sanitize_json_value(item_value, str(item_key))
            for item_key, item_value in value.items()
        }
    if isinstance(value, list):
        return [_sanitize_json_value(item, key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize_json_value(item, key) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> None:
    public_code = block_code if block_code in BLOCK_CODES else "NON_CLAIM_MISSING_OR_FLIPPED"
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _sanitize_json_value(expected_posture),
            "actual_posture": _sanitize_json_value(actual_posture),
            "block_code": None if passed else public_code,
            "failure_code": None if passed else public_code,
        }
    )


def _check_counts(checks: list[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code in BLOCK_CODES:
                return code
    return None


def _reference_declared(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    key: str,
    code: str,
) -> bool:
    value = request.get(key)
    passed = isinstance(value, str) and bool(value.strip())
    _add_check(checks, f"{key}_declared", passed, "non-empty string", value, code)
    return passed


def _required_false_request_check(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    key: str,
    code: str,
) -> bool:
    value = request.get(key, False)
    passed = value is False
    _add_check(checks, f"{key}_false", passed, False, value, code)
    return passed


def _validate_marker_text(
    checks: list[dict[str, Any]],
    check_name: str,
    reference: Any,
    markers: tuple[str, ...],
    code: str,
) -> bool:
    try:
        text = _read_text(reference)
    except OSError as exc:
        _add_check(checks, check_name, False, list(markers), str(exc), code)
        return False
    missing = []
    for marker in markers:
        alternatives = MARKER_ALTERNATIVES.get(marker, ())
        if marker not in text and not any(alternative in text for alternative in alternatives):
            missing.append(marker)
    _add_check(checks, check_name, not missing, list(markers), {"missing": missing}, code)
    return not missing


def _extract_failed_check_count(artifact: Mapping[str, Any]) -> Any:
    summary = artifact.get("descendant_body_differentiation_operation_summary")
    if _is_mapping(summary) and "failed_check_count" in summary:
        return summary.get("failed_check_count")
    checks = artifact.get("descendant_body_differentiation_operation_checks")
    if isinstance(checks, list):
        return sum(1 for check in checks if _is_mapping(check) and check.get("passed") is not True)
    return None


def _validate_completed_operation_artifact(
    checks: list[dict[str, Any]],
    reference: Any,
) -> bool:
    try:
        artifact = _read_json(reference)
    except (OSError, json.JSONDecodeError) as exc:
        _add_check(
            checks,
            "completed_operation_artifact_markers_present",
            False,
            "readable operation artifact JSON",
            str(exc),
            "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
        )
        return False
    if not _is_mapping(artifact):
        _add_check(
            checks,
            "completed_operation_artifact_markers_present",
            False,
            "artifact JSON object",
            type(artifact).__name__,
            "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
        )
        return False

    operation = artifact.get("descendant_body_differentiation_operation")
    candidate_records = artifact.get("descendant_body_differentiation_candidate_records")
    operation_mapping = operation if _is_mapping(operation) else {}
    records = candidate_records if isinstance(candidate_records, list) else []
    records_by_id = {
        record.get("candidate_record_id"): record
        for record in records
        if _is_mapping(record)
    }

    expected_records = {
        DEFAULT_CANDIDATE_RECORD_A_ID: DEFAULT_CANDIDATE_RECORD_A_ROLE,
        DEFAULT_CANDIDATE_RECORD_B_ID: DEFAULT_CANDIDATE_RECORD_B_ROLE,
    }
    record_checks: list[bool] = []
    for candidate_id, role in expected_records.items():
        record = records_by_id.get(candidate_id)
        record_checks.extend(
            [
                _is_mapping(record),
                _is_mapping(record) and record.get("candidate_role") == role,
                _is_mapping(record)
                and record.get("candidate_record_created_by_operation") is True,
                _is_mapping(record) and record.get("candidate_record_standing") is False,
                _is_mapping(record) and record.get("descendant_body_created") is False,
                _is_mapping(record)
                and record.get("inherited_from_contaminated_lineage") is False,
                _is_mapping(record)
                and record.get("prior_unsupported_claim_validated") is False,
            ]
        )

    expected_postures = {
        "outcome": artifact.get("outcome") == "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
        "failed_check_count": _extract_failed_check_count(artifact) == 0,
        "operation_type": operation_mapping.get("operation_type")
        == DEFAULT_SOURCE_OPERATION_TYPE,
        "operation_scope": operation_mapping.get("operation_scope")
        == DEFAULT_SOURCE_OPERATION_SCOPE,
        "candidate_record_policy": operation_mapping.get("candidate_record_policy")
        == DEFAULT_SOURCE_CANDIDATE_RECORD_POLICY,
        "operation_result_created": operation_mapping.get("operation_result_created") is True,
        "operation_recorded": operation_mapping.get("operation_recorded") is True,
        "differentiation_performed": operation_mapping.get("differentiation_performed") is True,
        "candidate_records_created": operation_mapping.get("candidate_records_created") is True,
        "candidate_record_count_emitted": operation_mapping.get("candidate_record_count_emitted")
        == 2,
        "exactly_two_candidate_records_emitted": operation_mapping.get(
            "exactly_two_candidate_records_emitted"
        )
        is True,
        "candidate_records_have_operation_evidence": operation_mapping.get(
            "candidate_records_have_operation_evidence"
        )
        is True,
        "candidate_records_non_standing": operation_mapping.get(
            "candidate_records_non_standing"
        )
        is True,
        "candidate_records_do_not_inherit_from_contaminated_lineage": operation_mapping.get(
            "candidate_records_do_not_inherit_from_contaminated_lineage"
        )
        is True,
        "descendant_body_a_created": operation_mapping.get("descendant_body_a_created")
        is False,
        "descendant_body_b_created": operation_mapping.get("descendant_body_b_created")
        is False,
        "standing_descendant_created": operation_mapping.get("standing_descendant_created")
        is False,
        "first_crossing_authorized": operation_mapping.get("first_crossing_authorized")
        is False,
        "relation_created": operation_mapping.get("relation_created") is False,
        "candidate_records": len(records) == 2 and all(record_checks),
    }
    passed = all(expected_postures.values())
    _add_check(
        checks,
        "completed_operation_artifact_markers_present",
        passed,
        "recorded operation artifact with two non-standing operation-evidenced candidates",
        expected_postures,
        "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
    )
    return passed


def _validate_declared_non_claims(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
) -> bool:
    value = request.get("declared_non_claims")
    if not _is_mapping(value):
        _add_check(
            checks,
            "declared_non_claims_mapping",
            False,
            "mapping with every required false non-claim set to false",
            value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return False
    invalid: dict[str, Any] = {}
    for key in REQUIRED_FALSE_NON_CLAIMS:
        item = value.get(key, None)
        if item is not False or not isinstance(item, bool):
            invalid[key] = item
    _add_check(
        checks,
        "declared_non_claims_false",
        not invalid,
        "all required false non-claims present as bool false",
        invalid,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return not invalid


def _validate_future_operation_shape(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
) -> bool:
    value = request.get("future_operation_shape")
    if value is None:
        _add_check(
            checks,
            "future_operation_shape_declared",
            False,
            "future operation shape mapping",
            None,
            "FUTURE_OPERATION_SHAPE_MISSING",
        )
        return False
    if not _is_mapping(value):
        _add_check(
            checks,
            "future_operation_shape_malformed",
            False,
            "future operation shape mapping",
            value,
            "FUTURE_OPERATION_SHAPE_MALFORMED",
        )
        return False
    fields = value.get("required_input_fields")
    if not isinstance(fields, list):
        _add_check(
            checks,
            "future_operation_shape_malformed",
            False,
            "required_input_fields list",
            value,
            "FUTURE_OPERATION_SHAPE_MALFORMED",
        )
        return False
    missing = [field for field in FUTURE_OPERATION_SHAPE_FIELDS if field not in fields]
    _add_check(
        checks,
        "future_operation_shape_declared",
        not missing,
        list(FUTURE_OPERATION_SHAPE_FIELDS),
        {"missing": missing},
        "FUTURE_OPERATION_SHAPE_MALFORMED",
    )
    return not missing


def _validate_request(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    question = request.get(
        "descendant_body_candidate_record_distinctness_operation_boundary_question"
    )
    _add_check(
        checks,
        "boundary_question_declared",
        isinstance(question, str) and bool(question.strip()),
        "non-empty boundary question",
        question,
        "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_QUESTION_UNDECLARED",
    )

    intent = request.get(
        "descendant_body_candidate_record_distinctness_operation_boundary_intent"
    )
    _add_check(
        checks,
        "boundary_intent_supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _add_check(
        checks,
        "boundary_block_not_requested",
        intent != INTENT_BLOCK,
        f"intent is not {INTENT_BLOCK}",
        intent,
        "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_BLOCK_REQUESTED",
    )

    _reference_declared(
        checks,
        request,
        "completed_operation_terminal_summary_reference",
        "COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    )
    _reference_declared(
        checks,
        request,
        "completed_operation_artifact_reference",
        "COMPLETED_OPERATION_ARTIFACT_REFERENCE_MISSING",
    )
    _reference_declared(
        checks,
        request,
        "contaminated_lineage_reference",
        "CONTAMINATED_LINEAGE_REFERENCE_MISSING",
    )
    _reference_declared(
        checks,
        request,
        "existence_claim_evidence_check_terminal_summary_reference",
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    )
    _reference_declared(
        checks,
        request,
        "candidate_record_a_reference",
        "CANDIDATE_RECORD_A_REFERENCE_MISSING",
    )
    _reference_declared(
        checks,
        request,
        "candidate_record_b_reference",
        "CANDIDATE_RECORD_B_REFERENCE_MISSING",
    )

    exact_checks = (
        (
            "candidate_record_a_id",
            DEFAULT_CANDIDATE_RECORD_A_ID,
            "CANDIDATE_RECORD_A_ID_NOT_EXPECTED",
        ),
        (
            "candidate_record_b_id",
            DEFAULT_CANDIDATE_RECORD_B_ID,
            "CANDIDATE_RECORD_B_ID_NOT_EXPECTED",
        ),
        (
            "candidate_record_a_role",
            DEFAULT_CANDIDATE_RECORD_A_ROLE,
            "CANDIDATE_RECORD_A_ROLE_NOT_EXPECTED",
        ),
        (
            "candidate_record_b_role",
            DEFAULT_CANDIDATE_RECORD_B_ROLE,
            "CANDIDATE_RECORD_B_ROLE_NOT_EXPECTED",
        ),
        (
            "future_distinctness_operation_type",
            FUTURE_DISTINCTNESS_OPERATION_TYPE,
            "FUTURE_DISTINCTNESS_OPERATION_TYPE_NOT_EXPECTED",
        ),
        (
            "future_distinctness_operation_scope",
            FUTURE_DISTINCTNESS_OPERATION_SCOPE,
            "FUTURE_DISTINCTNESS_OPERATION_SCOPE_NOT_EXPECTED",
        ),
        (
            "distinctness_evidence_policy",
            DISTINCTNESS_EVIDENCE_POLICY,
            "DISTINCTNESS_EVIDENCE_POLICY_NOT_EXPECTED",
        ),
        (
            "cosmetic_difference_policy",
            COSMETIC_DIFFERENCE_POLICY,
            "COSMETIC_DIFFERENCE_POLICY_NOT_EXPECTED",
        ),
        (
            "shared_evidence_policy",
            SHARED_EVIDENCE_POLICY,
            "SHARED_EVIDENCE_POLICY_NOT_EXPECTED",
        ),
        ("not_distinct_policy", NOT_DISTINCT_POLICY, "NOT_DISTINCT_POLICY_NOT_EXPECTED"),
        (
            "failure_visibility_policy",
            FAILURE_VISIBILITY_POLICY,
            "FAILURE_VISIBILITY_POLICY_NOT_EXPECTED",
        ),
    )
    for key, expected, code in exact_checks:
        value = request.get(key)
        missing_code = code.replace("_NOT_EXPECTED", "_MISSING")
        block_code = missing_code if value is None and missing_code in BLOCK_CODES else code
        _add_check(checks, f"{key}_exact", value == expected, expected, value, block_code)

    _add_check(
        checks,
        "candidate_record_count_required_equals_two",
        request.get("candidate_record_count_required") == 2,
        2,
        request.get("candidate_record_count_required"),
        "CANDIDATE_RECORD_COUNT_REQUIRED_NOT_TWO",
    )
    _validate_future_operation_shape(checks, request)

    for key, code in STRICT_FALSE_REQUEST_FIELDS.items():
        _required_false_request_check(checks, request, key, code)

    for key, code in FALSE_NON_CLAIM_BLOCK_CODES.items():
        value = request.get(key, False)
        _add_check(checks, f"{key}_not_claimed", value is not True, "not true", value, code)

    for key, code in REQUESTED_TRUE_BLOCK_CODES.items():
        value = request.get(key, False)
        _add_check(checks, f"{key}_not_requested", value is not True, "not true", value, code)

    _validate_declared_non_claims(checks, request)

    boundary_markers_present = _validate_marker_text(
        checks,
        "boundary_spec_markers_present",
        request.get("boundary_spec_reference", DEFAULT_BOUNDARY_SPEC_REFERENCE),
        BOUNDARY_SPEC_MARKERS,
        "BOUNDARY_SPEC_MARKER_MISSING",
    )
    _validate_marker_text(
        checks,
        "completed_operation_terminal_summary_markers_present",
        request.get("completed_operation_terminal_summary_reference"),
        COMPLETED_OPERATION_TERMINAL_SUMMARY_MARKERS,
        "COMPLETED_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    )
    artifact_markers_present = _validate_completed_operation_artifact(
        checks,
        request.get("completed_operation_artifact_reference"),
    )
    _validate_marker_text(
        checks,
        "contaminated_lineage_markers_present",
        request.get("contaminated_lineage_reference"),
        CONTAMINATED_LINEAGE_MARKERS,
        "CONTAMINATED_LINEAGE_MARKER_MISSING",
    )
    _validate_marker_text(
        checks,
        "existence_claim_evidence_check_terminal_summary_markers_present",
        request.get("existence_claim_evidence_check_terminal_summary_reference"),
        EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKERS,
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    )
    _add_check(
        checks,
        "completed_operation_emitted_two_candidate_records",
        artifact_markers_present,
        True,
        artifact_markers_present,
        "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
    )
    _add_check(
        checks,
        "completed_operation_did_not_prove_distinctness_beyond_id_and_role",
        boundary_markers_present,
        True,
        boundary_markers_present,
        "BOUNDARY_SPEC_MARKER_MISSING",
    )

    return checks


def _basis_flags(checks: list[Mapping[str, Any]]) -> dict[str, bool]:
    return {
        str(check.get("check_name")): bool(check.get("passed") is True)
        for check in checks
    }


def _boundary_object(
    request: Mapping[str, Any],
    checks: list[Mapping[str, Any]],
    recorded: bool,
) -> dict[str, Any]:
    flags = _basis_flags(checks)
    marker_recorded = recorded
    future_operation_shape = request.get("future_operation_shape")
    if not _is_mapping(future_operation_shape):
        future_operation_shape = {}

    boundary = {
        "boundary_id": request.get(
            "descendant_body_candidate_record_distinctness_operation_boundary_id",
            DEFAULT_BOUNDARY_ID,
        ),
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "completed_operation_terminal_summary_reference": request.get(
            "completed_operation_terminal_summary_reference",
            DEFAULT_COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        ),
        "completed_operation_artifact_reference": request.get(
            "completed_operation_artifact_reference",
            DEFAULT_COMPLETED_OPERATION_ARTIFACT_REFERENCE,
        ),
        "contaminated_lineage_reference": request.get(
            "contaminated_lineage_reference", DEFAULT_CONTAMINATED_LINEAGE_REFERENCE
        ),
        "existence_claim_evidence_check_terminal_summary_reference": request.get(
            "existence_claim_evidence_check_terminal_summary_reference",
            DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE,
        ),
        "candidate_record_a_reference": request.get(
            "candidate_record_a_reference", DEFAULT_CANDIDATE_RECORD_A_ID
        ),
        "candidate_record_b_reference": request.get(
            "candidate_record_b_reference", DEFAULT_CANDIDATE_RECORD_B_ID
        ),
        "candidate_record_a_id": request.get(
            "candidate_record_a_id", DEFAULT_CANDIDATE_RECORD_A_ID
        ),
        "candidate_record_b_id": request.get(
            "candidate_record_b_id", DEFAULT_CANDIDATE_RECORD_B_ID
        ),
        "candidate_record_a_role": request.get(
            "candidate_record_a_role", DEFAULT_CANDIDATE_RECORD_A_ROLE
        ),
        "candidate_record_b_role": request.get(
            "candidate_record_b_role", DEFAULT_CANDIDATE_RECORD_B_ROLE
        ),
        "future_distinctness_operation_type": request.get(
            "future_distinctness_operation_type", FUTURE_DISTINCTNESS_OPERATION_TYPE
        ),
        "future_distinctness_operation_scope": request.get(
            "future_distinctness_operation_scope", FUTURE_DISTINCTNESS_OPERATION_SCOPE
        ),
        "distinctness_evidence_policy": request.get(
            "distinctness_evidence_policy", DISTINCTNESS_EVIDENCE_POLICY
        ),
        "cosmetic_difference_policy": request.get(
            "cosmetic_difference_policy", COSMETIC_DIFFERENCE_POLICY
        ),
        "shared_evidence_policy": request.get(
            "shared_evidence_policy", SHARED_EVIDENCE_POLICY
        ),
        "not_distinct_policy": request.get("not_distinct_policy", NOT_DISTINCT_POLICY),
        "failure_visibility_policy": request.get(
            "failure_visibility_policy", FAILURE_VISIBILITY_POLICY
        ),
        "candidate_record_count_required": request.get("candidate_record_count_required", 2),
        "future_operation_shape": _sanitize_json_value(future_operation_shape),
        "descendant_body_candidate_record_distinctness_operation_boundary_recorded": recorded,
        "boundary_created": recorded,
        "completed_operation_terminal_summary_reference_declared": marker_recorded,
        "completed_operation_artifact_reference_declared": marker_recorded,
        "contaminated_lineage_reference_declared": marker_recorded,
        "existence_claim_evidence_check_terminal_summary_reference_declared": marker_recorded,
        "candidate_record_a_reference_declared": marker_recorded,
        "candidate_record_b_reference_declared": marker_recorded,
        "candidate_record_a_id_accepted": marker_recorded,
        "candidate_record_b_id_accepted": marker_recorded,
        "candidate_record_a_role_accepted": marker_recorded,
        "candidate_record_b_role_accepted": marker_recorded,
        "future_distinctness_operation_type_accepted": marker_recorded,
        "future_distinctness_operation_scope_accepted": marker_recorded,
        "distinctness_evidence_policy_accepted": marker_recorded,
        "cosmetic_difference_policy_accepted": marker_recorded,
        "shared_evidence_policy_accepted": marker_recorded,
        "not_distinct_policy_accepted": marker_recorded,
        "failure_visibility_policy_accepted": marker_recorded,
        "future_operation_shape_declared": marker_recorded,
        "scan_allowed": False,
        "repair_allowed": False,
        "validation_enforcement_allowed": False,
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
        "boundary_spec_markers_present": recorded
        and flags.get("boundary_spec_markers_present", False),
        "completed_operation_terminal_summary_markers_present": recorded
        and flags.get("completed_operation_terminal_summary_markers_present", False),
        "completed_operation_artifact_markers_present": recorded
        and flags.get("completed_operation_artifact_markers_present", False),
        "contaminated_lineage_markers_present": recorded
        and flags.get("contaminated_lineage_markers_present", False),
        "existence_claim_evidence_check_terminal_summary_markers_present": recorded
        and flags.get(
            "existence_claim_evidence_check_terminal_summary_markers_present", False
        ),
        "completed_operation_emitted_two_candidate_records": recorded
        and flags.get("completed_operation_artifact_markers_present", False),
        "completed_operation_did_not_prove_distinctness_beyond_id_and_role": recorded
        and flags.get("boundary_spec_markers_present", False),
        "distinctness_operation_not_created": True,
        "distinctness_operation_not_performed": True,
        "distinctness_operation_not_recorded": True,
        "distinctness_result_not_recorded": True,
        "distinctness_not_supported": True,
        "candidate_records_not_distinct": True,
        "candidate_specific_content_not_created": True,
        "separate_seal_material_not_created": True,
        "separate_lineage_receipt_material_not_created": True,
        "separate_digest_material_not_created": True,
        "candidate_standing_not_authorized": True,
        "candidate_standing_not_created": True,
        "descendant_bodies_not_created": True,
        "standing_descendant_not_created": True,
        "descendant_standing_check_not_performed": True,
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
        "scan_not_performed": True,
        "repository_scan_not_performed": True,
        "repair_not_performed": True,
        "validation_not_enforced": True,
        "hidden_repair_not_performed": True,
        "silent_overwrite_not_performed": True,
        "enumeration_not_treated_as_distinction": True,
        "id_and_role_difference_alone_not_treated_as_distinctness": True,
        "shared_evidence_reference_alone_not_treated_as_distinctness": True,
    }
    return _sanitize_json_value(boundary)


def _open_items() -> list[str]:
    return [
        "candidate-record distinctness operation resolver",
        "candidate-record distinctness operation test",
        "candidate-record distinctness operation artifact",
        "candidate-record distinctness operation terminal summary",
        "separate candidate-specific content emission, if ever separately bounded",
        "separate seal material emission, if ever separately bounded",
        "separate lineage receipt material emission, if ever separately bounded",
        "separate digest material emission, if ever separately bounded",
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


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
) -> dict[str, Any]:
    passed_count, failed_count = _check_counts(checks)
    block_code = _first_failed_code(checks) if outcome == OUTCOME_BLOCKED else None
    recorded = outcome == OUTCOME_RECORDED
    boundary = _boundary_object(request, checks, recorded)
    metadata = {
        "descendant_body_candidate_record_distinctness_operation_boundary_id": boundary[
            "boundary_id"
        ],
        "boundary_type": BOUNDARY_TYPE,
        "result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }
    result: dict[str, Any] = {
        "descendant_body_candidate_record_distinctness_operation_boundary_metadata": metadata,
        "declared_descendant_body_candidate_record_distinctness_operation_boundary_question": _sanitize_json_value(
            copy.deepcopy(dict(request))
        ),
        "upstream_basis": {
            "completed_operation_terminal_summary_reference": boundary[
                "completed_operation_terminal_summary_reference"
            ],
            "completed_operation_artifact_reference": boundary[
                "completed_operation_artifact_reference"
            ],
            "contaminated_lineage_reference": boundary["contaminated_lineage_reference"],
            "existence_claim_evidence_check_terminal_summary_reference": boundary[
                "existence_claim_evidence_check_terminal_summary_reference"
            ],
            "completed_operation_emitted_two_candidate_records": boundary[
                "completed_operation_emitted_two_candidate_records"
            ],
            "completed_operation_did_not_prove_distinctness_beyond_id_and_role": boundary[
                "completed_operation_did_not_prove_distinctness_beyond_id_and_role"
            ],
        },
        "distinctness_operation_boundary_basis": {
            "boundary_type": BOUNDARY_TYPE,
            "future_distinctness_operation_type": FUTURE_DISTINCTNESS_OPERATION_TYPE,
            "future_distinctness_operation_scope": FUTURE_DISTINCTNESS_OPERATION_SCOPE,
            "distinctness_evidence_policy": DISTINCTNESS_EVIDENCE_POLICY,
            "cosmetic_difference_policy": COSMETIC_DIFFERENCE_POLICY,
            "shared_evidence_policy": SHARED_EVIDENCE_POLICY,
            "not_distinct_policy": NOT_DISTINCT_POLICY,
            "failure_visibility_policy": FAILURE_VISIBILITY_POLICY,
            "future_distinctness_operation_outcome_family": list(
                FUTURE_DISTINCTNESS_OPERATION_OUTCOME_FAMILY
            ),
        },
        "descendant_body_candidate_record_distinctness_operation_boundary": boundary,
        "descendant_body_candidate_record_distinctness_operation_boundary_checks": checks,
        "descendant_body_candidate_record_distinctness_operation_boundary_statement": {
            "descendant_body_candidate_record_distinctness_operation_boundary_recorded": boundary[
                "descendant_body_candidate_record_distinctness_operation_boundary_recorded"
            ],
            "boundary_created": boundary["boundary_created"],
            "completed_operation_emitted_two_candidate_records": boundary[
                "completed_operation_emitted_two_candidate_records"
            ],
            "completed_operation_did_not_prove_distinctness_beyond_id_and_role": boundary[
                "completed_operation_did_not_prove_distinctness_beyond_id_and_role"
            ],
            "distinctness_operation_not_created": True,
            "distinctness_operation_not_performed": True,
            "distinctness_operation_not_recorded": True,
            "distinctness_not_supported": True,
            "candidate_records_not_distinct": True,
            "enumeration_not_treated_as_distinction": True,
            "id_and_role_difference_alone_not_treated_as_distinctness": True,
            "shared_evidence_reference_alone_not_treated_as_distinctness": True,
            "result_level_non_claims_canonical_false": True,
        },
        "descendant_body_candidate_record_distinctness_operation_boundary_non_meaning": {
            "not_distinctness_operation": True,
            "not_distinctness_checking": True,
            "not_distinctness_evidence_creation": True,
            "not_candidate_standing": True,
            "not_descendant_body_creation": True,
            "not_repair": True,
            "not_repository_scan": True,
            "not_follow_on_authorization": True,
        },
        "additional_basis_required": []
        if outcome == OUTCOME_RECORDED
        else ["resolve failed boundary checks before recording this boundary"],
        "not_recorded_basis": []
        if outcome == OUTCOME_RECORDED
        else [check for check in checks if check.get("passed") is not True],
        "what_remains_open": _open_items(),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code,
            "block_code": block_code,
            "reason": None if block_code is None else "one or more boundary checks failed",
        },
    }
    result[
        "descendant_body_candidate_record_distinctness_operation_boundary_summary"
    ] = build_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_summary(
        result
    )
    return _sanitize_json_value(result)


def resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
    declared_descendant_body_candidate_record_distinctness_operation_boundary: Mapping[
        str, Any
    ]
    | None = None,
) -> dict[str, Any]:
    if declared_descendant_body_candidate_record_distinctness_operation_boundary is None:
        request = (
            build_declared_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_request()
        )
    elif not _is_mapping(
        declared_descendant_body_candidate_record_distinctness_operation_boundary
    ):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_request_mapping",
            False,
            "mapping request",
            type(
                declared_descendant_body_candidate_record_distinctness_operation_boundary
            ).__name__,
            "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_REQUEST_MALFORMED",
        )
        return _build_result({}, checks, OUTCOME_BLOCKED)
    else:
        request = copy.deepcopy(
            dict(declared_descendant_body_candidate_record_distinctness_operation_boundary)
        )

    checks = _validate_request(request)
    if any(check.get("passed") is not True for check in checks):
        return _build_result(request, checks, OUTCOME_BLOCKED)

    intent = request.get(
        "descendant_body_candidate_record_distinctness_operation_boundary_intent"
    )
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, checks, OUTCOME_NOT_RECORDED)
    return _build_result(request, checks, OUTCOME_RECORDED)


def resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_from_path(
    declared_descendant_body_candidate_record_distinctness_operation_boundary_path: Path
    | str,
) -> dict[str, Any]:
    try:
        payload = _read_json(
            declared_descendant_body_candidate_record_distinctness_operation_boundary_path
        )
    except (OSError, json.JSONDecodeError) as exc:
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_request_readable",
            False,
            "readable JSON request object",
            str(exc),
            "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_REQUEST_UNREADABLE",
        )
        return _build_result({}, checks, OUTCOME_BLOCKED)
    if not _is_mapping(payload):
        checks = []
        _add_check(
            checks,
            "declared_request_mapping",
            False,
            "JSON object request",
            type(payload).__name__,
            "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_REQUEST_MALFORMED",
        )
        return _build_result({}, checks, OUTCOME_BLOCKED)
    return resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
        payload
    )


def build_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get(
        "descendant_body_candidate_record_distinctness_operation_boundary_checks", []
    )
    check_list = checks if isinstance(checks, list) else []
    passed_count, failed_count = _check_counts(check_list)
    boundary = result.get(
        "descendant_body_candidate_record_distinctness_operation_boundary", {}
    )
    boundary_mapping = boundary if _is_mapping(boundary) else {}
    block = result.get("block", {})
    block_mapping = block if _is_mapping(block) else {}
    non_claims = result.get("non_claims", {})
    non_claim_mapping = non_claims if _is_mapping(non_claims) else {}
    return {
        "outcome": result.get("outcome"),
        "block_code": block_mapping.get("code") or block_mapping.get("block_code"),
        "block_reason": block_mapping.get("reason"),
        "boundary_id": boundary_mapping.get("boundary_id"),
        "question": result.get(
            "declared_descendant_body_candidate_record_distinctness_operation_boundary_question",
            {},
        ).get(
            "descendant_body_candidate_record_distinctness_operation_boundary_question"
        )
        if _is_mapping(
            result.get(
                "declared_descendant_body_candidate_record_distinctness_operation_boundary_question",
                {},
            )
        )
        else None,
        "intent": result.get(
            "declared_descendant_body_candidate_record_distinctness_operation_boundary_question",
            {},
        ).get(
            "descendant_body_candidate_record_distinctness_operation_boundary_intent"
        )
        if _is_mapping(
            result.get(
                "declared_descendant_body_candidate_record_distinctness_operation_boundary_question",
                {},
            )
        )
        else None,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "boundary_type": boundary_mapping.get("boundary_type"),
        "future_distinctness_operation_type": boundary_mapping.get(
            "future_distinctness_operation_type"
        ),
        "future_distinctness_operation_scope": boundary_mapping.get(
            "future_distinctness_operation_scope"
        ),
        "distinctness_evidence_policy": boundary_mapping.get(
            "distinctness_evidence_policy"
        ),
        "cosmetic_difference_policy": boundary_mapping.get("cosmetic_difference_policy"),
        "shared_evidence_policy": boundary_mapping.get("shared_evidence_policy"),
        "not_distinct_policy": boundary_mapping.get("not_distinct_policy"),
        "failure_visibility_policy": boundary_mapping.get("failure_visibility_policy"),
        "boundary_recorded": boundary_mapping.get(
            "descendant_body_candidate_record_distinctness_operation_boundary_recorded",
            False,
        ),
        "boundary_created": boundary_mapping.get("boundary_created", False),
        "completed_operation_emitted_two_candidate_records": boundary_mapping.get(
            "completed_operation_emitted_two_candidate_records", False
        ),
        "completed_operation_did_not_prove_distinctness_beyond_id_and_role": boundary_mapping.get(
            "completed_operation_did_not_prove_distinctness_beyond_id_and_role",
            False,
        ),
        "distinctness_operation_created": non_claim_mapping.get(
            "distinctness_operation_created", False
        ),
        "distinctness_operation_performed": non_claim_mapping.get(
            "distinctness_operation_performed", False
        ),
        "distinctness_operation_recorded": non_claim_mapping.get(
            "distinctness_operation_recorded", False
        ),
        "distinctness_supported": non_claim_mapping.get("distinctness_supported", False),
        "candidate_records_distinct": non_claim_mapping.get(
            "candidate_records_distinct", False
        ),
        "candidate_specific_content_created": non_claim_mapping.get(
            "candidate_specific_content_created", False
        ),
        "separate_seal_material_created": non_claim_mapping.get(
            "separate_seal_material_created", False
        ),
        "separate_lineage_receipt_material_created": non_claim_mapping.get(
            "separate_lineage_receipt_material_created", False
        ),
        "separate_digest_material_created": non_claim_mapping.get(
            "separate_digest_material_created", False
        ),
        "candidate_standing_authorized": boundary_mapping.get(
            "candidate_standing_authorized", False
        ),
        "descendant_body_created": boundary_mapping.get("descendant_body_created", False),
        "prior_unsupported_claims_validated": False,
        "affected_file_repaired": non_claim_mapping.get("affected_file_repaired", False),
        "affected_file_edited": non_claim_mapping.get("affected_file_edited", False),
        "affected_file_deleted": non_claim_mapping.get("affected_file_deleted", False),
        "affected_file_overwritten": non_claim_mapping.get(
            "affected_file_overwritten", False
        ),
        "affected_file_replaced": non_claim_mapping.get("affected_file_replaced", False),
        "affected_file_redeemed": non_claim_mapping.get("affected_file_redeemed", False),
        "affected_file_treated_as_clean_basis": non_claim_mapping.get(
            "affected_file_treated_as_clean_basis", False
        ),
        "contaminated_lineage_treated_as_clean_basis": non_claim_mapping.get(
            "contaminated_lineage_treated_as_clean_basis", False
        ),
        "existence_claim_evidence_check_overridden": non_claim_mapping.get(
            "existence_claim_evidence_check_overridden", False
        ),
        "existence_claim_evidence_check_bypassed": non_claim_mapping.get(
            "existence_claim_evidence_check_bypassed", False
        ),
        "differentiation_operation_overridden": non_claim_mapping.get(
            "differentiation_operation_overridden", False
        ),
        "differentiation_operation_bypassed": non_claim_mapping.get(
            "differentiation_operation_bypassed", False
        ),
        "scan_allowed": boundary_mapping.get("scan_allowed", False),
        "repair_allowed": boundary_mapping.get("repair_allowed", False),
        "validation_enforcement_allowed": boundary_mapping.get(
            "validation_enforcement_allowed", False
        ),
        "standing_authorized": boundary_mapping.get("standing_authorized", False),
        "crossing_authorized": boundary_mapping.get("crossing_authorized", False),
        "relation_authorized": boundary_mapping.get("relation_authorized", False),
        "field_machinery_authorized": boundary_mapping.get(
            "field_machinery_authorized", False
        ),
        "runtime_authorized": boundary_mapping.get("runtime_authorized", False),
        "currentness_authorized": boundary_mapping.get("currentness_authorized", False),
        "authority_authorized": boundary_mapping.get("authority_authorized", False),
        "output_authorized": boundary_mapping.get("output_authorized", False),
        "action_authorized": boundary_mapping.get("action_authorized", False),
        "derivative_reception_authorized": boundary_mapping.get(
            "derivative_reception_authorized", False
        ),
        "synchronization_authorized": boundary_mapping.get(
            "synchronization_authorized", False
        ),
        "follow_on_authorized": boundary_mapping.get("follow_on_authorized", False),
        "scan_not_performed": boundary_mapping.get("scan_not_performed", False),
        "repository_scan_not_performed": boundary_mapping.get(
            "repository_scan_not_performed", False
        ),
        "repair_not_performed": boundary_mapping.get("repair_not_performed", False),
        "validation_not_enforced": boundary_mapping.get("validation_not_enforced", False),
        "hidden_repair_not_performed": boundary_mapping.get(
            "hidden_repair_not_performed", False
        ),
        "silent_overwrite_not_performed": boundary_mapping.get(
            "silent_overwrite_not_performed", False
        ),
        "boundary_spec_markers_present": boundary_mapping.get(
            "boundary_spec_markers_present", False
        ),
        "completed_operation_terminal_summary_markers_present": boundary_mapping.get(
            "completed_operation_terminal_summary_markers_present", False
        ),
        "completed_operation_artifact_markers_present": boundary_mapping.get(
            "completed_operation_artifact_markers_present", False
        ),
        "contaminated_lineage_markers_present": boundary_mapping.get(
            "contaminated_lineage_markers_present", False
        ),
        "existence_claim_evidence_check_terminal_summary_markers_present": boundary_mapping.get(
            "existence_claim_evidence_check_terminal_summary_markers_present",
            False,
        ),
        "enumeration_not_treated_as_distinction": boundary_mapping.get(
            "enumeration_not_treated_as_distinction", False
        ),
        "id_and_role_difference_alone_not_treated_as_distinctness": boundary_mapping.get(
            "id_and_role_difference_alone_not_treated_as_distinctness", False
        ),
        "shared_evidence_reference_alone_not_treated_as_distinctness": boundary_mapping.get(
            "shared_evidence_reference_alone_not_treated_as_distinctness", False
        ),
        "result_level_non_claims_canonical_false": all(
            non_claim_mapping.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _safe_filename_part(value: Any) -> str:
    safe = str(value)
    safe = safe.replace("/", "_").replace("\\", "_").replace(" ", "_")
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
    safe = safe.strip("._-")
    return safe or DEFAULT_BOUNDARY_ID


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


def write_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not _is_mapping(result):
        raise DescendantBodyCandidateRecordDistinctnessOperationBoundaryV0MinError(
            "result must be a mapping"
        )
    boundary = result.get(
        "descendant_body_candidate_record_distinctness_operation_boundary", {}
    )
    boundary_mapping = boundary if _is_mapping(boundary) else {}
    boundary_id = boundary_mapping.get("boundary_id", DEFAULT_BOUNDARY_ID)
    filename = (
        f"{_safe_filename_part(boundary_id)}__"
        "descendant_body_candidate_record_distinctness_operation_boundary_v0_min_result.json"
    )
    if output_path is None:
        path = REPO_ROOT / OUTPUT_ROOT / filename
    else:
        path = Path(output_path)
        if path.is_dir() or str(output_path).endswith(("/", "\\")):
            path = path / filename
        if not path.is_absolute():
            path = REPO_ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _next_available_path(path)
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize_json_value(dict(result)), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path


def build_declared_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_request(
    *,
    descendant_body_candidate_record_distinctness_operation_boundary_id: str = DEFAULT_BOUNDARY_ID,
    descendant_body_candidate_record_distinctness_operation_boundary_question: str = DEFAULT_BOUNDARY_QUESTION,
    descendant_body_candidate_record_distinctness_operation_boundary_intent: str = INTENT_RECORD,
    boundary_spec_reference: str = DEFAULT_BOUNDARY_SPEC_REFERENCE,
    completed_operation_terminal_summary_reference: str = DEFAULT_COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE,
    completed_operation_artifact_reference: str = DEFAULT_COMPLETED_OPERATION_ARTIFACT_REFERENCE,
    contaminated_lineage_reference: str = DEFAULT_CONTAMINATED_LINEAGE_REFERENCE,
    existence_claim_evidence_check_terminal_summary_reference: str = DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE,
    candidate_record_a_reference: str = DEFAULT_CANDIDATE_RECORD_A_ID,
    candidate_record_b_reference: str = DEFAULT_CANDIDATE_RECORD_B_ID,
    candidate_record_a_id: str = DEFAULT_CANDIDATE_RECORD_A_ID,
    candidate_record_b_id: str = DEFAULT_CANDIDATE_RECORD_B_ID,
    candidate_record_a_role: str = DEFAULT_CANDIDATE_RECORD_A_ROLE,
    candidate_record_b_role: str = DEFAULT_CANDIDATE_RECORD_B_ROLE,
    future_distinctness_operation_type: str = FUTURE_DISTINCTNESS_OPERATION_TYPE,
    future_distinctness_operation_scope: str = FUTURE_DISTINCTNESS_OPERATION_SCOPE,
    distinctness_evidence_policy: str = DISTINCTNESS_EVIDENCE_POLICY,
    cosmetic_difference_policy: str = COSMETIC_DIFFERENCE_POLICY,
    shared_evidence_policy: str = SHARED_EVIDENCE_POLICY,
    not_distinct_policy: str = NOT_DISTINCT_POLICY,
    failure_visibility_policy: str = FAILURE_VISIBILITY_POLICY,
    candidate_record_count_required: int = 2,
    future_operation_shape: Mapping[str, Any] | None = None,
    declared_non_claims: Mapping[str, bool] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    if future_operation_shape is None:
        future_operation_shape = {
            "required_input_fields": list(FUTURE_OPERATION_SHAPE_FIELDS),
            "future_operation_outcome_family": list(
                FUTURE_DISTINCTNESS_OPERATION_OUTCOME_FAMILY
            ),
        }
    non_claims = (
        _canonical_non_claims()
        if declared_non_claims is None
        else copy.deepcopy(dict(declared_non_claims))
    )
    request: dict[str, Any] = {
        "descendant_body_candidate_record_distinctness_operation_boundary_id": (
            descendant_body_candidate_record_distinctness_operation_boundary_id
        ),
        "descendant_body_candidate_record_distinctness_operation_boundary_question": (
            descendant_body_candidate_record_distinctness_operation_boundary_question
        ),
        "descendant_body_candidate_record_distinctness_operation_boundary_intent": (
            descendant_body_candidate_record_distinctness_operation_boundary_intent
        ),
        "boundary_spec_reference": boundary_spec_reference,
        "completed_operation_terminal_summary_reference": (
            completed_operation_terminal_summary_reference
        ),
        "completed_operation_artifact_reference": completed_operation_artifact_reference,
        "contaminated_lineage_reference": contaminated_lineage_reference,
        "existence_claim_evidence_check_terminal_summary_reference": (
            existence_claim_evidence_check_terminal_summary_reference
        ),
        "candidate_record_a_reference": candidate_record_a_reference,
        "candidate_record_b_reference": candidate_record_b_reference,
        "candidate_record_a_id": candidate_record_a_id,
        "candidate_record_b_id": candidate_record_b_id,
        "candidate_record_a_role": candidate_record_a_role,
        "candidate_record_b_role": candidate_record_b_role,
        "future_distinctness_operation_type": future_distinctness_operation_type,
        "future_distinctness_operation_scope": future_distinctness_operation_scope,
        "distinctness_evidence_policy": distinctness_evidence_policy,
        "cosmetic_difference_policy": cosmetic_difference_policy,
        "shared_evidence_policy": shared_evidence_policy,
        "not_distinct_policy": not_distinct_policy,
        "failure_visibility_policy": failure_visibility_policy,
        "candidate_record_count_required": candidate_record_count_required,
        "future_operation_shape": copy.deepcopy(dict(future_operation_shape)),
        "scan_allowed": False,
        "repair_allowed": False,
        "validation_enforcement_allowed": False,
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
        "declared_non_claims": non_claims,
    }
    request.update(copy.deepcopy(overrides))
    return _sanitize_json_value(request)
