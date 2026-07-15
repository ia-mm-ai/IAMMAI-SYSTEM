"""Resolve one bounded successor closure result for a prior additional-basis gap.

The resolver reads only declared terminal-summary paths.  It may record a
closed prior gap, but never converts that closure into scope declaration,
standing, material emission, distinctness, body creation, or downstream work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateNonCosmeticScopeDivisionDeclarationSuccessorClosureOperationV0MinError(Exception):
    """Raised for bounded successor-closure write failures."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min"

OPERATION_ID = "descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_001"
OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "CLOSE_PRIOR_ADDITIONAL_BASIS_GAP_FROM_RECEIVED_AUDITED_DIGEST_SEALED_AUTHORED_DECLARATION_ONLY"
PRIOR_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION"
PRIOR_OPERATION_OUTCOME_REQUIRED = "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS"
UPSTREAM_RECEIPT_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION"
UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_RECORDED"
UPSTREAM_RECEIPT_STATUS_REQUIRED = "RECEIVED_AS_METADATA_FOR_AUDIT_ONLY"
UPSTREAM_AUDIT_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION"
UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_SATISFIES_MISSING_BASIS_REQUIREMENTS"
UPSTREAM_AUDIT_RESULT_REQUIRED = "SATISFIES_MISSING_BASIS_REQUIREMENTS"
UPSTREAM_DECLARATION_ACCEPTED_AS_BASIS_REQUIRED = True
UPSTREAM_DIGEST_CUSTODY_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION"
UPSTREAM_DIGEST_CUSTODY_OPERATION_OUTCOME_REQUIRED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION_RECORDED"
UPSTREAM_DIGEST_ALGORITHM_REQUIRED = "SHA-256"
UPSTREAM_PRIMARY_MATERIAL_DIGEST_SHA256_REQUIRED = "1ca450ea9762f2b2782b7edf3a1a08df3f292abbbd3aec78aa2890384b720dd0"
UPSTREAM_PRIMARY_MATERIAL_CUSTODY_POSTURE_REQUIRED = "LOCAL_OPERATOR_HELD_SIGNED_SOURCE_ARTIFACT"
TARGET_PRIMARY_MATERIAL_FILENAME = "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION V.2.pdf"
TARGET_PRIMARY_MATERIAL_VERSION = "v2"
TARGET_PRIMARY_MATERIAL_DATE = "10 July 2026"
TARGET_PRIMARY_MATERIAL_AUTHOR = "Marko Markota"
TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE = "AUTHORSHIP_ATTESTATION_ONLY"
TARGET_PREDECESSOR_MATERIAL_FILENAME = "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION v1"
TARGET_PREDECESSOR_MATERIAL_ROLE = "REFERENCED_PREDECESSOR_ONLY"
ADMISSIBLE_FUTURE_ROUTE = "SUCCESSOR_CLOSURE_THEN_BASIS_EMISSION_SUCCESSOR_ONLY"

OUTCOME_CLOSED = "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_CLOSED"
OUTCOME_REQUIRES_UPSTREAM_BASIS = "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_REQUIRES_UPSTREAM_BASIS"
OUTCOME_BLOCKED = "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (OUTCOME_CLOSED, OUTCOME_REQUIRES_UPSTREAM_BASIS, OUTCOME_BLOCKED, OUTCOME_NOT_RECORDED)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min")
DETERMINISTIC_FILENAME = "descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_001__successor_closure_operation_v0_min_result.json"

DEFAULT_OPERATION_SPEC_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_V0_MIN_SPEC.md"
DEFAULT_PRIOR_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"

ALLOWED_TRUE_RECORDED_FIELDS = (
    "successor_closure_operation_recorded", "successor_closure_performed", "successor_closure_result_recorded",
    "prior_additional_basis_gap_closed", "closure_basis_received", "closure_basis_audited",
    "closure_basis_digest_custody_sealed", "candidate_a_missing_basis_resolved",
    "candidate_b_missing_basis_resolved", "basis_bearing_scope_division_missing_basis_resolved",
    "declaration_accepted_as_basis",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "declaration_admitted_as_standing_basis", "candidate_a_scope_declared", "candidate_b_scope_declared",
    "basis_bearing_scope_division_declared", "basis_gap_closed", "candidate_specific_content_emitted",
    "separate_seal_material_emitted", "separate_lineage_receipt_material_emitted", "separate_digest_material_emitted",
    "candidate_specific_distinctness_basis_emission_operation_rerun", "distinctness_operation_rerun",
    "distinctness_supported_recorded", "candidate_records_marked_distinct", "candidate_records_distinct",
    "candidate_standing_authorized", "candidate_standing_created", "descendant_body_a_created",
    "descendant_body_b_created", "descendant_body_created", "standing_authorized", "standing_descendant_created",
    "descendant_standing_check_performed", "crossing_authorized", "first_crossing_authorized", "relation_created",
    "field_machinery_created", "runtime_created", "api_created", "currentness_created", "authority_created",
    "standing_created", "presence_established", "identity_created", "output_authorized", "action_authorized",
    "derivative_reception_authorized", "synchronization_authorized", "coupling_assigned_to_candidate_a",
    "coupling_assigned_to_candidate_b", "coupling_created", "third_candidate_created", "third_model_admitted",
    "follow_on_authorized", "follow_on_work_authorized", "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated", "prior_unsupported_derivation_event_claim_validated",
    "valid_derivation_event_recorded", "affected_file_repaired", "affected_file_edited", "affected_file_deleted",
    "affected_file_overwritten", "affected_file_replaced", "affected_file_redeemed", "affected_file_treated_as_clean_basis",
    "contaminated_lineage_treated_as_clean_basis", "authored_scope_division_declaration_receipt_operation_overridden",
    "authored_scope_division_declaration_receipt_operation_bypassed", "authored_scope_division_declaration_audit_operation_overridden",
    "authored_scope_division_declaration_audit_operation_bypassed", "authored_scope_division_declaration_digest_custody_operation_overridden",
    "authored_scope_division_declaration_digest_custody_operation_bypassed", "scan_performed", "repository_scan_performed",
    "file_discovery_performed", "repair_performed", "validation_enforced", "hidden_repair_performed",
    "silent_overwrite_performed", "direct_successor_closure_permission_to_closure_completion_conversion",
    "direct_gap_closure_to_standing_conversion", "direct_gap_closure_to_standing_basis_conversion",
    "direct_gap_closure_to_candidate_a_scope_declaration", "direct_gap_closure_to_candidate_b_scope_declaration",
    "direct_gap_closure_to_basis_bearing_scope_division_declaration", "direct_gap_closure_to_candidate_specific_basis_emission_conversion",
    "direct_gap_closure_to_distinctness_support_conversion", "direct_gap_closure_to_candidate_records_distinct_conversion",
    "direct_gap_closure_to_candidate_standing_conversion", "direct_gap_closure_to_descendant_body_creation",
    "direct_gap_closure_to_relation_creation", "direct_gap_closure_to_runtime_creation",
    "direct_gap_closure_to_authority_currentness_creation", "direct_gap_closure_to_coupling_creation",
    "direct_gap_closure_to_third_candidate_route", "direct_gap_closure_to_third_model_route",
    "direct_gap_closure_to_follow_on_work", "direct_gap_closure_to_presence", "direct_gap_closure_to_identity",
    "direct_audit_result_to_closure_without_digest_custody", "direct_receipt_to_closure_without_audit",
    "direct_digest_custody_to_closure_without_audit",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING", "UNSUPPORTED_INTENT", "SUCCESSOR_CLOSURE_OPERATION_SPEC_REFERENCE_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_SPEC_MARKER_MISSING", "PRIOR_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "PRIOR_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "RECEIPT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "AUDIT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING", "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING", "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "UPSTREAM_BASIS_MISSING_OR_INSUFFICIENT", "NON_CLAIM_MISSING_OR_FLIPPED", "RESULT_POSTURE_PRECLAIMED",
    "PROHIBITED_GAP_CLOSURE_TO_STANDING_REQUESTED", "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "PROHIBITED_BASIS_EMISSION_OR_DISTINCTNESS_REQUESTED", "PROHIBITED_DESCENDANT_BODY_OR_STANDING_REQUESTED",
    "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED", "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED", "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED", "EXPLICIT_BLOCK_REQUESTED", "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_gap_closure_as_standing": "PROHIBITED_GAP_CLOSURE_TO_STANDING_REQUESTED",
    "request_gap_closure_as_standing_basis": "PROHIBITED_GAP_CLOSURE_TO_STANDING_REQUESTED",
    "request_candidate_a_scope_declaration": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_candidate_b_scope_declaration": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_basis_bearing_scope_division_declaration": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_candidate_specific_content_emission": "PROHIBITED_BASIS_EMISSION_OR_DISTINCTNESS_REQUESTED",
    "request_separate_seal_material_emission": "PROHIBITED_BASIS_EMISSION_OR_DISTINCTNESS_REQUESTED",
    "request_separate_lineage_receipt_material_emission": "PROHIBITED_BASIS_EMISSION_OR_DISTINCTNESS_REQUESTED",
    "request_separate_digest_material_emission": "PROHIBITED_BASIS_EMISSION_OR_DISTINCTNESS_REQUESTED",
    "request_basis_emission_operation_rerun": "PROHIBITED_BASIS_EMISSION_OR_DISTINCTNESS_REQUESTED",
    "request_distinctness_operation_rerun": "PROHIBITED_BASIS_EMISSION_OR_DISTINCTNESS_REQUESTED",
    "request_distinctness_supported_recording": "PROHIBITED_BASIS_EMISSION_OR_DISTINCTNESS_REQUESTED",
    "request_candidate_records_marked_distinct": "PROHIBITED_BASIS_EMISSION_OR_DISTINCTNESS_REQUESTED",
    "request_candidate_standing_authorization": "PROHIBITED_DESCENDANT_BODY_OR_STANDING_REQUESTED",
    "request_descendant_body_creation": "PROHIBITED_DESCENDANT_BODY_OR_STANDING_REQUESTED",
    "request_crossing_authorization": "PROHIBITED_DESCENDANT_BODY_OR_STANDING_REQUESTED",
    "request_relation_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_output_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_action_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_derivative_reception_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_coupling_assignment_to_candidate_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_candidate_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_model_admission": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_presence_establishment": "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "request_identity_creation": "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "request_follow_on_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
}

OPERATION_SPEC_MARKER_CLASSES = (
    ("operation_identity", ("Descendant Body Candidate Non-Cosmetic Scope Division Declaration Successor Closure Operation V0 Minimum Specification", OPERATION_TYPE, OPERATION_ID, OPERATION_SCOPE)),
    ("prior_operation", (PRIOR_OPERATION_OUTCOME_REQUIRED, "missing non-cosmetic candidate A scope declaration", "missing non-cosmetic candidate B scope declaration", "missing basis-bearing scope division declaration", "failed_check_count = 0", "passed_check_count = 96")),
    ("receipt", (UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, UPSTREAM_RECEIPT_STATUS_REQUIRED, TARGET_PRIMARY_MATERIAL_FILENAME, TARGET_PRIMARY_MATERIAL_VERSION, TARGET_PRIMARY_MATERIAL_DATE, TARGET_PRIMARY_MATERIAL_AUTHOR, TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE, TARGET_PREDECESSOR_MATERIAL_FILENAME, TARGET_PREDECESSOR_MATERIAL_ROLE)),
    ("audit", (UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, UPSTREAM_AUDIT_RESULT_REQUIRED, "declaration_accepted_as_basis = true", "missing_or_insufficient_audit_criteria = []", "declaration_admitted_as_standing_basis = false", "candidate_a_scope_declared = false", "candidate_b_scope_declared = false", "basis_bearing_scope_division_declared = false", "basis_gap_closed = false")),
    ("digest_custody", (UPSTREAM_DIGEST_CUSTODY_OPERATION_OUTCOME_REQUIRED, UPSTREAM_DIGEST_ALGORITHM_REQUIRED, UPSTREAM_PRIMARY_MATERIAL_DIGEST_SHA256_REQUIRED, UPSTREAM_PRIMARY_MATERIAL_CUSTODY_POSTURE_REQUIRED, "audit_result_changed = false")),
    ("non_conversion", ("Gap closure is not standing", "Gap closure is not standing basis", "Gap closure is not scope declaration", "Gap closure is not basis-bearing scope division declaration", "Gap closure is not candidate-specific basis emission", "Gap closure is not distinctness support", "Gap closure is not candidate standing", "Gap closure is not descendant-body creation", "Gap closure is not relation", "Gap closure is not runtime", "Gap closure is not currentness", "Gap closure is not authority", "Gap closure is not coupling", "Gap closure is not presence", "Gap closure is not identity", "Accepted basis remains non-standing")),
    ("sibling_coupling", ("Candidate A and Candidate B remain sibling non-standing candidate records", "Neither ranks above the other", "Regulation may not become sovereign over Motion", "Motion may not erase Regulation", "Coupling remains unassigned", "Coupling must not be treated as third candidate", "Coupling must not be treated as third model", "Coupling must not be created by successor closure", "No third candidate is admitted", "No third model is admitted")),
    ("lineage", ("V1 predecessor reference remains lineage only", "V2 receipt does not erase V1", "No orphaned state", "No silent reset", "No overwrite", "Contaminated lineage remains preserved")),
    ("permitted_route", (ADMISSIBLE_FUTURE_ROUTE, "PRIOR_ADDITIONAL_BASIS_GAP_CLOSED", "Only after a future successor closure records PRIOR_ADDITIONAL_BASIS_GAP_CLOSED may a separately bounded candidate-specific distinctness basis emission successor be considered", "No later operation is authorized by this specification alone")),
    ("contaminated_lineage", ("DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage", "descendant_body_basis_candidate_a_created = true", "descendant_body_basis_candidate_b_created = true", "descendant_body_basis_derivation_event_recorded = true", "UNSUPPORTED", "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file")),
    ("blocked_routes", ("Direct successor closure permission to closure completion", "Direct gap closure to standing conversion", "Direct gap closure to standing-basis conversion", "Direct gap closure to candidate A scope declaration", "Direct gap closure to candidate B scope declaration", "Direct gap closure to basis-bearing scope division declaration", "Direct audit result to closure without digest/custody", "Repository scan route")),
    ("closing_lock", ("This operation spec defines only a future successor closure operation shape", "Successor closure permission is not successor closure completion", "Gap closure is not standing", "Gap closure is not presence", "Gap closure is not identity", "Open means not scheduled, not authorized, and not executed")),
)

# Existing completed summaries express some equivalent postures in compact
# prose; synthetic inputs may use the explicit field form from this spec.
OPERATION_SPEC_MARKER_VARIANTS = {
    "prior_operation": (
        (PRIOR_OPERATION_OUTCOME_REQUIRED, "missing non-cosmetic candidate A scope declaration", "missing non-cosmetic candidate B scope declaration", "missing basis-bearing scope division declaration", "failed_check_count = 0", "passed_check_count = 96"),
        (PRIOR_OPERATION_OUTCOME_REQUIRED, "Its additional basis remained: non-cosmetic candidate A scope declaration, non-cosmetic candidate B scope declaration, and basis-bearing scope division declaration.", "failed_check_count = 0", "passed_check_count = 96"),
    ),
    "sibling_coupling": (
        ("Candidate A and Candidate B remain sibling non-standing candidate records", "Neither ranks above the other", "Regulation may not become sovereign over Motion", "Motion may not erase Regulation", "Coupling remains unassigned", "Coupling must not be treated as third candidate", "Coupling must not be treated as third model", "Coupling must not be created by successor closure", "No third candidate is admitted", "No third model is admitted"),
        ("Candidate A and Candidate B remain sibling non-standing candidate records", "Neither ranks above the other", "Regulation may not become sovereign over Motion", "Motion may not erase Regulation", "Coupling remains unassigned, is neither a third candidate nor third model, and is not created by successor closure. No third candidate, third model, or standing body is admitted."),
    ),
    "lineage": (
        ("V1 predecessor reference remains lineage only", "V2 receipt does not erase V1", "No orphaned state", "No silent reset", "No overwrite", "Contaminated lineage remains preserved"),
        ("V1 predecessor reference remains lineage only", "V2 receipt does not erase V1", "No orphaned state, silent reset, overwrite, or downstream route is authorized.", "Contaminated lineage remains preserved"),
    ),
    "contaminated_lineage": (
        ("DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage", "descendant_body_basis_candidate_a_created = true", "descendant_body_basis_candidate_b_created = true", "descendant_body_basis_derivation_event_recorded = true", "UNSUPPORTED", "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file"),
        ("remains preserved contaminated lineage for the unsupported existence-claim class", "descendant_body_basis_candidate_a_created = true", "descendant_body_basis_candidate_b_created = true", "descendant_body_basis_derivation_event_recorded = true", "UNSUPPORTED", "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file"),
    ),
    "blocked_routes": (
        ("direct successor closure permission to closure completion", "direct gap closure to standing conversion", "direct gap closure to standing basis conversion", "direct gap closure to candidate A scope declaration", "direct gap closure to candidate B scope declaration", "direct gap closure to basis-bearing scope division declaration", "direct audit result to closure without digest/custody", "repository scan route"),
        ("Direct successor closure permission to closure completion", "Direct gap closure to standing conversion", "direct gap closure to standing-basis conversion", "Direct gap closure to candidate A scope declaration", "direct gap closure to candidate B scope declaration", "direct gap closure to basis-bearing scope division declaration", "Direct audit result to closure without digest/custody", "Repository scan route"),
    ),
}

UPSTREAM_REQUIREMENTS = (
    ("prior_operation_terminal_summary_reference", DEFAULT_PRIOR_OPERATION_TERMINAL_SUMMARY_REFERENCE, "PRIOR_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "PRIOR_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", (PRIOR_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 96", "missing non-cosmetic candidate A scope declaration", "missing non-cosmetic candidate B scope declaration", "missing basis-bearing scope division declaration"), "prior_operation_terminal_summary_markers_present"),
    ("receipt_operation_terminal_summary_reference", DEFAULT_RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE, "RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "RECEIPT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", (UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 91", UPSTREAM_RECEIPT_STATUS_REQUIRED, TARGET_PRIMARY_MATERIAL_FILENAME, TARGET_PRIMARY_MATERIAL_VERSION, TARGET_PRIMARY_MATERIAL_DATE, TARGET_PRIMARY_MATERIAL_AUTHOR, TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE, TARGET_PREDECESSOR_MATERIAL_FILENAME, TARGET_PREDECESSOR_MATERIAL_ROLE), "receipt_operation_terminal_summary_markers_present"),
    ("audit_operation_terminal_summary_reference", DEFAULT_AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE, "AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "AUDIT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", (UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 83", "audit_result = SATISFIES_MISSING_BASIS_REQUIREMENTS", "declaration_accepted_as_basis = true", "missing_or_insufficient_audit_criteria = []", "declaration_admitted_as_standing_basis = false", "candidate_a_scope_declared = false", "candidate_b_scope_declared = false", "basis_bearing_scope_division_declared = false", "basis_gap_closed = false"), "audit_operation_terminal_summary_markers_present"),
    ("digest_custody_operation_terminal_summary_reference", DEFAULT_DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_REFERENCE, "DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", (UPSTREAM_DIGEST_CUSTODY_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 88", UPSTREAM_DIGEST_ALGORITHM_REQUIRED, UPSTREAM_PRIMARY_MATERIAL_DIGEST_SHA256_REQUIRED, UPSTREAM_PRIMARY_MATERIAL_CUSTODY_POSTURE_REQUIRED, "audit_result_changed = false", "declaration_admitted_as_standing_basis = false", "candidate_a_scope_declared = false", "candidate_b_scope_declared = false", "basis_bearing_scope_division_declared = false", "basis_gap_closed = false"), "digest_custody_operation_terminal_summary_markers_present"),
    ("existence_claim_evidence_check_terminal_summary_reference", DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE, "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING", "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING", ("UNSUPPORTED",), "existence_claim_evidence_check_terminal_summary_markers_present"),
    ("distinctness_operation_terminal_summary_reference", DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE, "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", ("NOT_DISTINCT",), "distinctness_operation_terminal_summary_markers_present"),
    ("basis_emission_operation_terminal_summary_reference", DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE, "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", ("REQUIRES_ADDITIONAL_BASIS",), "basis_emission_operation_terminal_summary_markers_present"),
    ("scope_division_declaration_boundary_terminal_summary_reference", DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE, "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING", "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING", ("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",), "scope_division_declaration_boundary_terminal_summary_markers_present"),
)

UPSTREAM_MARKER_VARIANTS = {
    "audit_operation_terminal_summary_reference": (
        (UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 83", "audit_result = SATISFIES_MISSING_BASIS_REQUIREMENTS", "declaration_accepted_as_basis = true", "missing_or_insufficient_audit_criteria = []", "declaration_admitted_as_standing_basis = false", "candidate_a_scope_declared = false", "candidate_b_scope_declared = false", "basis_bearing_scope_division_declared = false", "basis_gap_closed = false"),
        (UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 83", "audit_result = SATISFIES_MISSING_BASIS_REQUIREMENTS", "declaration_accepted_as_basis = true", "missing_or_insufficient_audit_criteria = []", "Result-level non-claims canonicalized false."),
    ),
}

WHAT_REMAINS_OPEN = (
    "candidate-specific distinctness basis emission operation successor, if successor closure passes", "actual candidate-specific content emission", "actual separate seal material emission", "actual separate lineage receipt material emission", "actual separate digest material emission", "future distinctness-supported operation result", "divergent receipt-history route, if separately bounded", "carrier separation route, if separately bounded", "candidate-standing checks", "first crossing", "relation", "FIELD machinery", "runtime", "API", "currentness", "authority", "standing", "presence boundary", "identity boundary", "output authorization", "action authorization", "derivative reception", "synchronization", "externalization boundary", "follow-on work",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _resolve_path(value: Any) -> Path | None:
    if isinstance(value, Path):
        path = value
    elif isinstance(value, str) and value.strip():
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
    return key.lower() in {"raw_pdf", "raw_pdf_body", "raw_extracted_text", "extracted_text", "pdf_bytes", "file_bytes", "full_text", "full_body", "source_body", "payload"}


def _sanitize(value: Any, key: str = "") -> Any:
    if isinstance(value, (bytes, bytearray, memoryview)):
        return "[REDACTED_BINARY_CONTENT]"
    if isinstance(value, Mapping):
        return {str(item_key): _sanitize(item, str(item_key)) for item_key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if _is_sensitive_key(key) and value.strip():
            return "[REDACTED_SENSITIVE_BODY]"
        return value if len(value) <= 4096 else f"{value[:4096]}...[truncated]"
    return value


def _json_ready(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value


def _add_check(checks: list[dict[str, Any]], name: str, passed: bool, expected: Any, actual: Any, code: str | None = None, upstream: bool = False) -> None:
    check: dict[str, Any] = {"check_name": name, "passed": bool(passed), "expected_posture": _sanitize(expected), "actual_posture": _sanitize(actual), "upstream_basis_check": upstream}
    if not passed and code:
        check["block_code"] = code
        check["failure_code"] = code
    checks.append(check)


def _failed_codes(checks: list[dict[str, Any]], upstream: bool | None = None) -> list[str]:
    return [str(check["block_code"]) for check in checks if check.get("passed") is False and isinstance(check.get("block_code"), str) and check["block_code"] in BLOCK_CODES and (upstream is None or check.get("upstream_basis_check") is upstream)]


def _validate_exact_values(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    expected = (
        ("operation_id", OPERATION_ID), ("operation_type", OPERATION_TYPE), ("operation_version", OPERATION_VERSION), ("operation_scope", OPERATION_SCOPE),
        ("successor_closure_operation_id", OPERATION_ID), ("successor_closure_operation_type", OPERATION_TYPE), ("successor_closure_operation_version", OPERATION_VERSION), ("successor_closure_operation_scope", OPERATION_SCOPE),
        ("prior_operation_type", PRIOR_OPERATION_TYPE), ("prior_operation_outcome_required", PRIOR_OPERATION_OUTCOME_REQUIRED),
        ("prior_missing_candidate_a_scope_required", True), ("prior_missing_candidate_b_scope_required", True), ("prior_missing_basis_bearing_scope_division_required", True),
        ("upstream_receipt_operation_type", UPSTREAM_RECEIPT_OPERATION_TYPE), ("upstream_receipt_operation_outcome_required", UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED), ("upstream_receipt_status_required", UPSTREAM_RECEIPT_STATUS_REQUIRED),
        ("upstream_audit_operation_type", UPSTREAM_AUDIT_OPERATION_TYPE), ("upstream_audit_operation_outcome_required", UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED), ("upstream_audit_result_required", UPSTREAM_AUDIT_RESULT_REQUIRED), ("upstream_declaration_accepted_as_basis_required", True),
        ("upstream_digest_custody_operation_type", UPSTREAM_DIGEST_CUSTODY_OPERATION_TYPE), ("upstream_digest_custody_operation_outcome_required", UPSTREAM_DIGEST_CUSTODY_OPERATION_OUTCOME_REQUIRED), ("upstream_digest_algorithm_required", UPSTREAM_DIGEST_ALGORITHM_REQUIRED), ("upstream_primary_material_digest_sha256_required", UPSTREAM_PRIMARY_MATERIAL_DIGEST_SHA256_REQUIRED), ("upstream_primary_material_custody_posture_required", UPSTREAM_PRIMARY_MATERIAL_CUSTODY_POSTURE_REQUIRED),
        ("target_primary_material_filename", TARGET_PRIMARY_MATERIAL_FILENAME), ("target_primary_material_version", TARGET_PRIMARY_MATERIAL_VERSION), ("target_primary_material_date", TARGET_PRIMARY_MATERIAL_DATE), ("target_primary_material_author", TARGET_PRIMARY_MATERIAL_AUTHOR), ("target_primary_material_signature_role", TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE), ("target_predecessor_material_filename", TARGET_PREDECESSOR_MATERIAL_FILENAME), ("target_predecessor_material_role", TARGET_PREDECESSOR_MATERIAL_ROLE), ("admissible_future_route", ADMISSIBLE_FUTURE_ROUTE),
    )
    for field, value in expected:
        _add_check(checks, f"{field} exact", request.get(field) == value, value, request.get(field), "UPSTREAM_BASIS_MISSING_OR_INSUFFICIENT")


def _validate_request_posture(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    declared = request.get("declared_non_claims")
    bad = list(REQUIRED_FALSE_NON_CLAIMS) if not isinstance(declared, Mapping) else [key for key in REQUIRED_FALSE_NON_CLAIMS if declared.get(key) is not False]
    _add_check(checks, "required declared non-claims false", not bad, "every required key exactly false", {"invalid_keys": bad}, "NON_CLAIM_MISSING_OR_FLIPPED")
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if request.get(key) is True:
            _add_check(checks, f"top-level false posture {key} not pre-claimed", False, False, True, _code_for_non_claim(key))
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        if request.get(key) is True:
            _add_check(checks, f"result-only posture {key} not pre-claimed", False, "resolver output only", True, "RESULT_POSTURE_PRECLAIMED")
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        _add_check(checks, f"{field} not requested", request.get(field) is not True, False, request.get(field), code)


def _code_for_non_claim(key: str) -> str:
    if key in {"declaration_admitted_as_standing_basis", "basis_gap_closed", "direct_gap_closure_to_standing_conversion", "direct_gap_closure_to_standing_basis_conversion"}:
        return "PROHIBITED_GAP_CLOSURE_TO_STANDING_REQUESTED"
    if "scope" in key or "basis_bearing" in key:
        return "PROHIBITED_SCOPE_DECLARATION_REQUESTED"
    if any(token in key for token in ("emission", "distinctness", "records_distinct")):
        return "PROHIBITED_BASIS_EMISSION_OR_DISTINCTNESS_REQUESTED"
    if any(token in key for token in ("descendant", "standing", "crossing")):
        return "PROHIBITED_DESCENDANT_BODY_OR_STANDING_REQUESTED"
    if any(token in key for token in ("relation", "runtime", "api", "currentness", "authority", "field_machinery")):
        return "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED"
    if any(token in key for token in ("coupling", "third_")):
        return "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    if any(token in key for token in ("presence", "identity")):
        return "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED"
    if any(token in key for token in ("repair", "scan", "discovery", "validation", "unsupported", "affected_file", "overwrite", "edited", "deleted", "replaced", "redeemed")):
        return "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED"
    return "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED"


def _validate_target_spec(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    path = _resolve_path(request.get("operation_spec_reference"))
    _add_check(checks, "operation spec reference readable", path is not None and path.is_file(), "declared readable spec path", str(path) if path else request.get("operation_spec_reference"), "SUCCESSOR_CLOSURE_OPERATION_SPEC_REFERENCE_MISSING")
    text = _read_text(request.get("operation_spec_reference"))
    missing = [name for name, markers in OPERATION_SPEC_MARKER_CLASSES if text is None or not _markers_present(text, OPERATION_SPEC_MARKER_VARIANTS.get(name, (markers,)))]
    _add_check(checks, "successor closure operation spec posture classes present", not missing, "all required marker classes", {"missing_posture_classes": missing}, "SUCCESSOR_CLOSURE_OPERATION_SPEC_MARKER_MISSING")


def _validate_upstream(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> list[str]:
    missing_basis: list[str] = []
    for field, _, reference_code, marker_code, markers, flag in UPSTREAM_REQUIREMENTS:
        text = _read_text(request.get(field))
        readable = text is not None
        _add_check(checks, f"{field} readable", readable, "declared readable terminal summary", request.get(field), reference_code, True)
        present = readable and _markers_present(text, UPSTREAM_MARKER_VARIANTS.get(field, (markers,)))
        _add_check(checks, f"{field} expected markers present", present, markers, {"missing_markers": [] if present else list(markers)}, marker_code, True)
        if not present:
            missing_basis.append(flag)
    return missing_basis


def _markers_present(text: str, variants: tuple[tuple[str, ...], ...]) -> bool:
    return any(all(marker in text for marker in markers) for markers in variants)


def _marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    flags = {"successor_closure_operation_spec_markers_present": any(check.get("check_name") == "successor closure operation spec posture classes present" and check.get("passed") is True for check in checks)}
    for field, *_, flag in UPSTREAM_REQUIREMENTS:
        flags[flag] = any(check.get("check_name") == f"{field} expected markers present" and check.get("passed") is True for check in checks)
    return flags


def _operation_object(outcome: str, flags: Mapping[str, bool]) -> dict[str, Any]:
    closed = outcome == OUTCOME_CLOSED
    requires = outcome == OUTCOME_REQUIRES_UPSTREAM_BASIS
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID, "operation_type": OPERATION_TYPE, "operation_version": OPERATION_VERSION, "operation_scope": OPERATION_SCOPE,
        "successor_closure_operation_id": OPERATION_ID, "successor_closure_operation_type": OPERATION_TYPE, "successor_closure_operation_version": OPERATION_VERSION, "successor_closure_operation_scope": OPERATION_SCOPE,
        "prior_operation_type": PRIOR_OPERATION_TYPE, "prior_operation_outcome_required": PRIOR_OPERATION_OUTCOME_REQUIRED, "prior_missing_candidate_a_scope_required": True, "prior_missing_candidate_b_scope_required": True, "prior_missing_basis_bearing_scope_division_required": True,
        "upstream_receipt_operation_type": UPSTREAM_RECEIPT_OPERATION_TYPE, "upstream_receipt_operation_outcome_required": UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "upstream_receipt_status_required": UPSTREAM_RECEIPT_STATUS_REQUIRED,
        "upstream_audit_operation_type": UPSTREAM_AUDIT_OPERATION_TYPE, "upstream_audit_operation_outcome_required": UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "upstream_audit_result_required": UPSTREAM_AUDIT_RESULT_REQUIRED, "upstream_declaration_accepted_as_basis_required": True,
        "upstream_digest_custody_operation_type": UPSTREAM_DIGEST_CUSTODY_OPERATION_TYPE, "upstream_digest_custody_operation_outcome_required": UPSTREAM_DIGEST_CUSTODY_OPERATION_OUTCOME_REQUIRED, "upstream_digest_algorithm_required": UPSTREAM_DIGEST_ALGORITHM_REQUIRED, "upstream_primary_material_digest_sha256_required": UPSTREAM_PRIMARY_MATERIAL_DIGEST_SHA256_REQUIRED, "upstream_primary_material_custody_posture_required": UPSTREAM_PRIMARY_MATERIAL_CUSTODY_POSTURE_REQUIRED,
        "target_primary_material_filename": TARGET_PRIMARY_MATERIAL_FILENAME, "target_primary_material_version": TARGET_PRIMARY_MATERIAL_VERSION, "target_primary_material_date": TARGET_PRIMARY_MATERIAL_DATE, "target_primary_material_author": TARGET_PRIMARY_MATERIAL_AUTHOR, "target_primary_material_signature_role": TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE, "target_predecessor_material_filename": TARGET_PREDECESSOR_MATERIAL_FILENAME, "target_predecessor_material_role": TARGET_PREDECESSOR_MATERIAL_ROLE, "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        **_canonical_non_claims(), **flags,
    }
    operation.update({
        "successor_closure_operation_recorded": closed, "successor_closure_performed": closed, "successor_closure_result_recorded": closed,
        "successor_closure_result": "PRIOR_ADDITIONAL_BASIS_GAP_CLOSED" if closed else "REQUIRES_UPSTREAM_BASIS" if requires else "NOT_CLOSED",
        "prior_additional_basis_gap_closed": closed, "closure_basis_received": closed, "closure_basis_audited": closed,
        "closure_basis_digest_custody_sealed": closed, "candidate_a_missing_basis_resolved": closed,
        "candidate_b_missing_basis_resolved": closed, "basis_bearing_scope_division_missing_basis_resolved": closed,
        "declaration_accepted_as_basis": closed,
    })
    return operation


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation")
    op = operation if isinstance(operation, Mapping) else {}
    checks = result.get("successor_closure_operation_checks")
    records = checks if isinstance(checks, list) else []
    upstream = result.get("upstream_basis")
    basis = upstream if isinstance(upstream, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"), "failed_check_count": sum(check.get("passed") is False for check in records if isinstance(check, Mapping)), "passed_check_count": sum(check.get("passed") is True for check in records if isinstance(check, Mapping)), "result_version": RESULT_VERSION, "resolver_module": RESOLVER_MODULE,
        "operation_id": op.get("operation_id"), "operation_type": op.get("operation_type"), "operation_version": op.get("operation_version"), "operation_scope": op.get("operation_scope"),
        "prior_operation_type": op.get("prior_operation_type"), "prior_operation_outcome_required": op.get("prior_operation_outcome_required"),
        "upstream_receipt_operation_type": op.get("upstream_receipt_operation_type"), "upstream_receipt_operation_outcome_required": op.get("upstream_receipt_operation_outcome_required"), "upstream_receipt_status_required": op.get("upstream_receipt_status_required"),
        "upstream_audit_operation_type": op.get("upstream_audit_operation_type"), "upstream_audit_operation_outcome_required": op.get("upstream_audit_operation_outcome_required"), "upstream_audit_result_required": op.get("upstream_audit_result_required"),
        "upstream_digest_custody_operation_type": op.get("upstream_digest_custody_operation_type"), "upstream_digest_custody_operation_outcome_required": op.get("upstream_digest_custody_operation_outcome_required"), "upstream_digest_algorithm_required": op.get("upstream_digest_algorithm_required"), "upstream_primary_material_digest_sha256_required": op.get("upstream_primary_material_digest_sha256_required"), "upstream_primary_material_custody_posture_required": op.get("upstream_primary_material_custody_posture_required"),
        "selected_target_spec_path": basis.get("operation_spec_reference"), "completed_prior_operation_terminal_summary_path": basis.get("prior_operation_terminal_summary_reference"), "completed_receipt_operation_terminal_summary_path": basis.get("receipt_operation_terminal_summary_reference"), "completed_audit_operation_terminal_summary_path": basis.get("audit_operation_terminal_summary_reference"), "completed_digest_custody_operation_terminal_summary_path": basis.get("digest_custody_operation_terminal_summary_reference"), "missing_or_insufficient_upstream_basis": result.get("closure_result_detail", {}).get("missing_or_insufficient_upstream_basis", []),
    }
    for key in (*ALLOWED_TRUE_RECORDED_FIELDS, "successor_closure_result", *REQUIRED_FALSE_NON_CLAIMS, "successor_closure_operation_spec_markers_present", *[flag for *_, flag in UPSTREAM_REQUIREMENTS]):
        summary[key] = op.get(key)
    return _sanitize(summary)


def _build_result(request: Mapping[str, Any], outcome: str, checks: list[dict[str, Any]], missing_basis: list[str], block_code: str | None = None, block_reason: str | None = None) -> dict[str, Any]:
    flags = _marker_flags(checks)
    operation = _operation_object(outcome, flags)
    result: dict[str, Any] = {
        "successor_closure_operation_metadata": {"operation_id": OPERATION_ID, "result_version": RESULT_VERSION, "resolver_module": RESOLVER_MODULE, "generated_at": _utc_now()},
        "declared_successor_closure_operation_basis": _sanitize(request),
        "upstream_basis": {"operation_spec_reference": request.get("operation_spec_reference"), **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS}, **flags},
        "descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation": operation,
        "successor_closure_operation_checks": checks,
        "successor_closure_operation_statement": {"outcome": outcome, "successor_closure_operation_recorded": operation["successor_closure_operation_recorded"], "prior_additional_basis_gap_closed": operation["prior_additional_basis_gap_closed"], "result_level_non_claims_canonical_false": True},
        "successor_closure_operation_non_meaning": {"not_standing": True, "not_scope_declaration": True, "not_basis_emission": True, "not_distinctness": True, "not_candidate_standing": True, "not_descendant_body_creation": True, "not_relation": True, "not_runtime": True, "not_authority": True, "not_coupling": True, "not_presence": True, "not_identity": True, "not_follow_on": True},
        "closure_result_detail": {"successor_closure_result": operation["successor_closure_result"], "missing_or_insufficient_upstream_basis": list(missing_basis), "closure_basis_received": operation["closure_basis_received"], "closure_basis_audited": operation["closure_basis_audited"], "closure_basis_digest_custody_sealed": operation["closure_basis_digest_custody_sealed"]},
        "permitted_future_route": ["evaluate declared completed summaries only", "record only bounded prior-gap closure", "consider a separately bounded basis-emission successor only after CLOSED"],
        "blocked_routes": ["standing, scope, material, distinctness, body, relation, runtime, authority, coupling, presence, identity, repair, scan, validation, and downstream conversion routes"],
        "what_remains_open": list(WHAT_REMAINS_OPEN), "non_claims": _canonical_non_claims(), "outcome": outcome, "result_version": RESULT_VERSION, "resolver_module": RESOLVER_MODULE,
        "block": {"blocked": outcome == OUTCOME_BLOCKED, "code": block_code if outcome == OUTCOME_BLOCKED else None, "block_code": block_code if outcome == OUTCOME_BLOCKED else None, "reason": block_reason if outcome == OUTCOME_BLOCKED else None},
    }
    result["successor_closure_operation_summary"] = _build_summary(result)
    return result


def _blocked_result(request: Mapping[str, Any], checks: list[dict[str, Any]], code: str, reason: str, missing_basis: list[str] | None = None) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(request, OUTCOME_BLOCKED, checks, missing_basis or [], code, reason)


def build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_request(**overrides: Any) -> dict[str, Any]:
    """Build the bounded no-discovery successor-closure request."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD, "operation_id": OPERATION_ID, "operation_type": OPERATION_TYPE, "operation_version": OPERATION_VERSION, "operation_scope": OPERATION_SCOPE, "successor_closure_operation_id": OPERATION_ID, "successor_closure_operation_type": OPERATION_TYPE, "successor_closure_operation_version": OPERATION_VERSION, "successor_closure_operation_scope": OPERATION_SCOPE,
        "prior_operation_type": PRIOR_OPERATION_TYPE, "prior_operation_outcome_required": PRIOR_OPERATION_OUTCOME_REQUIRED, "prior_missing_candidate_a_scope_required": True, "prior_missing_candidate_b_scope_required": True, "prior_missing_basis_bearing_scope_division_required": True,
        "upstream_receipt_operation_type": UPSTREAM_RECEIPT_OPERATION_TYPE, "upstream_receipt_operation_outcome_required": UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "upstream_receipt_status_required": UPSTREAM_RECEIPT_STATUS_REQUIRED,
        "upstream_audit_operation_type": UPSTREAM_AUDIT_OPERATION_TYPE, "upstream_audit_operation_outcome_required": UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "upstream_audit_result_required": UPSTREAM_AUDIT_RESULT_REQUIRED, "upstream_declaration_accepted_as_basis_required": True,
        "upstream_digest_custody_operation_type": UPSTREAM_DIGEST_CUSTODY_OPERATION_TYPE, "upstream_digest_custody_operation_outcome_required": UPSTREAM_DIGEST_CUSTODY_OPERATION_OUTCOME_REQUIRED, "upstream_digest_algorithm_required": UPSTREAM_DIGEST_ALGORITHM_REQUIRED, "upstream_primary_material_digest_sha256_required": UPSTREAM_PRIMARY_MATERIAL_DIGEST_SHA256_REQUIRED, "upstream_primary_material_custody_posture_required": UPSTREAM_PRIMARY_MATERIAL_CUSTODY_POSTURE_REQUIRED,
        "target_primary_material_filename": TARGET_PRIMARY_MATERIAL_FILENAME, "target_primary_material_version": TARGET_PRIMARY_MATERIAL_VERSION, "target_primary_material_date": TARGET_PRIMARY_MATERIAL_DATE, "target_primary_material_author": TARGET_PRIMARY_MATERIAL_AUTHOR, "target_primary_material_signature_role": TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE, "target_predecessor_material_filename": TARGET_PREDECESSOR_MATERIAL_FILENAME, "target_predecessor_material_role": TARGET_PREDECESSOR_MATERIAL_ROLE, "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "operation_spec_reference": DEFAULT_OPERATION_SPEC_REFERENCE, **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS}, "declared_non_claims": _canonical_non_claims(), **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


def resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(declared_successor_closure_operation: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Resolve one declared successor closure without discovery, mutation, or standing conversion."""

    if declared_successor_closure_operation is None:
        request = build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_request()
    elif not isinstance(declared_successor_closure_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request mapping", False, "mapping", type(declared_successor_closure_operation).__name__, "REQUEST_NOT_MAPPING")
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_successor_closure_operation))
    checks: list[dict[str, Any]] = []
    intent = request.get("intent")
    _add_check(checks, "intent supported", intent in SUPPORTED_INTENTS, SUPPORTED_INTENTS, intent, "UNSUPPORTED_INTENT")
    if intent == INTENT_BLOCK:
        return _blocked_result(request, checks, "EXPLICIT_BLOCK_REQUESTED", "explicit block intent requested")
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(request, checks, "UNSUPPORTED_INTENT", "intent is unsupported")
    _validate_exact_values(checks, request)
    _validate_request_posture(checks, request)
    _validate_target_spec(checks, request)
    missing_basis = _validate_upstream(checks, request)
    non_upstream_failures = _failed_codes(checks, False)
    if non_upstream_failures:
        return _blocked_result(request, checks, non_upstream_failures[0], f"blocked by failed check {non_upstream_failures[0]}", missing_basis)
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, missing_basis)
    if missing_basis:
        return _build_result(request, OUTCOME_REQUIRES_UPSTREAM_BASIS, checks, missing_basis)
    return _build_result(request, OUTCOME_CLOSED, checks, [])


def resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_from_path(declared_successor_closure_operation_path: Path | str) -> dict[str, Any]:
    """Read one explicit JSON request object and resolve it."""

    path = Path(declared_successor_closure_operation_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            request = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request path readable JSON", False, "readable JSON object", str(exc), "REQUEST_NOT_MAPPING")
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request path is unreadable or not JSON")
    return resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(request)


def build_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return compact bounded successor-closure metadata."""

    return _build_summary(result)


def write_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_result(result: Mapping[str, Any], output_path: Path | str | None = None) -> Path:
    """Write deterministic sanitized JSON without silent overwrite."""

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
        raise DescendantBodyCandidateNonCosmeticScopeDivisionDeclarationSuccessorClosureOperationV0MinError(f"WRITE_REFUSED: {exc}") from exc
