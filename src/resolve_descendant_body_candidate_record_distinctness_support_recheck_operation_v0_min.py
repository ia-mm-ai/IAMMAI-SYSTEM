"""Resolve one bounded candidate-record distinctness support recheck.

The resolver reads only declared specification and terminal-summary references.
It can record one local support result for two existing non-standing candidate
records, while refusing standing, body creation, relations, runtime, authority,
coupling, presence, identity, repair, discovery, and downstream authorization.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateRecordDistinctnessSupportRecheckOperationV0MinError(Exception):
    """Raised when bounded result writing cannot be completed."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min"

OPERATION_ID = "descendant_body_candidate_record_distinctness_support_recheck_operation_001"
OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "RECHECK_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_AFTER_CANDIDATE_SPECIFIC_BASIS_EMISSION_ONLY"
PRIOR_DISTINCTNESS_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION"
PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT"
PRIOR_DISTINCTNESS_RESULT_REQUIRED = "NOT_DISTINCT"
PRIOR_DISTINCTNESS_SUPPORTED_REQUIRED = False
UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION"
UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_OUTCOME_REQUIRED = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_EMITTED"
UPSTREAM_BASIS_EMISSION_SUCCESSOR_RESULT_REQUIRED = "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED"
UPSTREAM_CANDIDATE_SPECIFIC_CONTENT_EMITTED_REQUIRED = True
UPSTREAM_CANDIDATE_A_BASIS_MATERIAL_EMITTED_REQUIRED = True
UPSTREAM_CANDIDATE_B_BASIS_MATERIAL_EMITTED_REQUIRED = True
UPSTREAM_SEPARATE_CANDIDATE_BASIS_MATERIAL_EMITTED_REQUIRED = True
UPSTREAM_BASIS_PAIR_EMITTED_REQUIRED = True
UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED = "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis"
UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED = "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis"
UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED = "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS"
UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED = "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
UPSTREAM_BASIS_PAIR_SCOPE_REQUIRED = "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY"
UPSTREAM_CANDIDATE_RECORDS_MARKED_DISTINCT_REQUIRED = False
UPSTREAM_DISTINCTNESS_SUPPORTED_RECORDED_REQUIRED = False
UPSTREAM_CANDIDATE_STANDING_AUTHORIZED_REQUIRED = False
UPSTREAM_DESCENDANT_BODY_CREATED_REQUIRED = False
UPSTREAM_RELATION_CREATED_REQUIRED = False
UPSTREAM_COUPLING_CREATED_REQUIRED = False
UPSTREAM_PRESENCE_ESTABLISHED_REQUIRED = False
UPSTREAM_IDENTITY_CREATED_REQUIRED = False
UPSTREAM_FOLLOW_ON_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = "DISTINCTNESS_SUPPORT_RECHECK_THEN_CANDIDATE_STANDING_BOUNDARY_CONSIDERATION_ONLY"

OUTCOME_SUPPORTED = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_SUPPORTED"
OUTCOME_NOT_SUPPORTED = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_NOT_SUPPORTED"
OUTCOME_REQUIRES_BASIS_EMISSION = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_REQUIRES_BASIS_EMISSION"
OUTCOME_BLOCKED = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_SUPPORTED,
    OUTCOME_NOT_SUPPORTED,
    OUTCOME_REQUIRES_BASIS_EMISSION,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min")
DETERMINISTIC_FILENAME = "descendant_body_candidate_record_distinctness_support_recheck_operation_001__distinctness_support_recheck_operation_v0_min_result.json"

DEFAULT_OPERATION_SPEC_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_V0_MIN_SPEC.md"
DEFAULT_PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_V0.md"

ALLOWED_TRUE_RECORDED_FIELDS = (
    "distinctness_support_recheck_operation_recorded",
    "distinctness_support_recheck_performed",
    "distinctness_support_recheck_result_recorded",
    "prior_not_distinct_result_referenced",
    "emitted_candidate_specific_basis_material_referenced",
    "candidate_a_basis_material_referenced",
    "candidate_b_basis_material_referenced",
    "basis_pair_referenced",
    "candidate_specific_basis_material_compared",
    "distinctness_supported_recorded",
    "candidate_records_marked_distinct",
    "candidate_records_distinct",
)

REQUIRED_FALSE_NON_CLAIMS = (
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
    "presence_established",
    "identity_created",
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
    "basis_emission_successor_operation_overridden",
    "basis_emission_successor_operation_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_recheck_permission_to_recheck_completion_conversion",
    "direct_basis_emission_to_standing",
    "direct_basis_emission_to_descendant_body_creation",
    "direct_basis_emission_to_relation",
    "direct_distinctness_support_to_candidate_standing",
    "direct_distinctness_support_to_descendant_body_creation",
    "direct_distinctness_support_to_crossing",
    "direct_distinctness_support_to_relation",
    "direct_distinctness_support_to_runtime",
    "direct_distinctness_support_to_authority_currentness",
    "direct_distinctness_support_to_coupling_creation",
    "direct_distinctness_support_to_third_candidate_route",
    "direct_distinctness_support_to_third_model_route",
    "direct_distinctness_support_to_presence",
    "direct_distinctness_support_to_identity",
    "direct_distinctness_support_to_follow_on_work",
    "direct_candidate_records_distinct_to_candidate_standing",
    "direct_candidate_records_distinct_to_descendant_body_creation",
    "direct_candidate_records_distinct_to_relation",
    "direct_candidate_records_distinct_to_presence",
    "direct_candidate_records_distinct_to_identity",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "DISTINCTNESS_SUPPORT_RECHECK_OPERATION_SPEC_REFERENCE_MISSING",
    "DISTINCTNESS_SUPPORT_RECHECK_OPERATION_SPEC_MARKER_MISSING",
    "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "BASIS_EMISSION_MATERIAL_MISSING_OR_INSUFFICIENT",
    "BASIS_EMISSION_MATERIAL_NOT_SUPPORTING_DISTINCTNESS",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "RESULT_POSTURE_PRECLAIMED",
    "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_candidate_standing_authorization": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_candidate_standing_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_descendant_body_a_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_descendant_body_b_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_descendant_body_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_standing_authorization": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_standing_descendant_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_descendant_standing_check": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_crossing_authorization": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_first_crossing_authorization": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_relation_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
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
    ("operation_identity", (
        "Descendant Body Candidate Record Distinctness Support Recheck Operation V0 Minimum Specification",
        OPERATION_TYPE,
        OPERATION_ID,
        OPERATION_SCOPE,
    )),
    ("prior_distinctness_operation", (
        PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED,
        "distinctness_result = NOT_DISTINCT",
        "distinctness_supported = false",
        "compared 2 candidate records",
        "ids and roles were distinct",
        "candidate-specific content was absent",
        "separate seal, receipt, and digest material were absent",
    )),
    ("successor_basis_emission", (
        UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_OUTCOME_REQUIRED,
        UPSTREAM_BASIS_EMISSION_SUCCESSOR_RESULT_REQUIRED,
        "candidate_specific_content_emitted = true",
        "candidate_a_basis_material_emitted = true",
        "candidate_b_basis_material_emitted = true",
        "separate_candidate_basis_material_emitted = true",
        "basis_pair_emitted = true",
        UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED,
        UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED,
        UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED,
        UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED,
        "basis_pair_scope = SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
        "candidate_records_marked_distinct = false",
        "candidate_records_distinct = false",
        "distinctness_supported_recorded = false",
        "candidate_standing_authorized = false",
        "descendant_body_created = false",
        "relation_created = false",
        "coupling_created = false",
        "presence_established = false",
        "identity_created = false",
        "follow_on_authorized = false",
    )),
    ("emitted_basis_material", (
        "Candidate A basis material is descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis",
        "candidate_record_id = descendant_body_basis_candidate_a_001",
        "candidate_role = CANDIDATE_A",
        UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED,
        "Motion-side admissible variation",
        "Motion mandate",
        "non_standing_basis = true",
        "distinctness_supported = false at emission time",
        "Candidate B basis material is descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis",
        "candidate_record_id = descendant_body_basis_candidate_b_001",
        "candidate_role = CANDIDATE_B",
        UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED,
        "Regulation-side admissibility bounds",
        "Regulation mandate",
    )),
    ("basis_pair_non_hierarchy", (
        "basis_pair_scope = SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
        "candidate_a_and_b_are_sibling_non_standing_basis_materials = true",
        "neither_candidate_ranks_above_the_other = true",
        "regulation_not_sovereign_over_motion = true",
        "motion_does_not_erase_regulation = true",
        "coupling_assigned = false",
        "coupling_created = false",
        "third_candidate_created = false",
        "third_model_admitted = false",
        "distinctness_supported_recorded = false",
        "candidate_records_marked_distinct = false",
        "candidate_standing_authorized = false",
    )),
    ("recheck_permitted_result", (
        OUTCOME_SUPPORTED,
        OUTCOME_NOT_SUPPORTED,
        OUTCOME_REQUIRES_BASIS_EMISSION,
        OUTCOME_BLOCKED,
        "DISTINCTNESS_SUPPORT_RECHECKED",
        "DISTINCTNESS_SUPPORTED",
        "REQUIRES_BASIS_EMISSION",
        "DISTINCTNESS_NOT_SUPPORTED",
    )),
    ("recheck_non_conversion", (
        "Distinctness support is not candidate standing",
        "Distinctness support is not descendant-body creation",
        "Distinctness support is not relation",
        "Distinctness support is not runtime",
        "Distinctness support is not currentness",
        "Distinctness support is not authority",
        "Distinctness support is not coupling",
        "Distinctness support is not presence",
        "Distinctness support is not identity",
        "Candidate records marked distinct are still not standing candidates",
        "Candidate records marked distinct are still not descendant bodies",
        "Candidate records marked distinct are still not relation participants",
        "Candidate records marked distinct are still not presence-bearing",
        "Candidate records marked distinct are still not identity-bearing",
    )),
    ("permitted_route", (
        ADMISSIBLE_FUTURE_ROUTE,
        "Only after a future recheck records DISTINCTNESS_SUPPORTED may a separately bounded candidate-standing boundary be considered",
        "No later operation is authorized by this operation specification alone",
    )),
    ("contaminated_lineage", (
        "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
        "descendant_body_basis_candidate_a_created = true",
        "descendant_body_basis_candidate_b_created = true",
        "descendant_body_basis_derivation_event_recorded = true",
        "UNSUPPORTED",
        "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
    )),
    ("blocked_routes", (
        "direct recheck permission to recheck completion",
        "direct basis emission to standing",
        "direct basis emission to descendant-body creation",
        "direct basis emission to relation",
        "direct distinctness support to candidate standing",
        "direct distinctness support to descendant-body creation",
        "direct distinctness support to crossing",
        "direct distinctness support to relation",
        "direct distinctness support to runtime",
        "direct distinctness support to authority/currentness",
        "direct distinctness support to coupling creation",
        "direct distinctness support to third-candidate route",
        "direct distinctness support to third-model route",
        "direct distinctness support to presence",
        "direct distinctness support to identity",
        "direct distinctness support to follow-on work",
        "direct candidate records distinct to candidate standing",
        "direct candidate records distinct to descendant-body creation",
        "direct candidate records distinct to relation",
        "direct candidate records distinct to presence",
        "direct candidate records distinct to identity",
        "repository scan route",
        "file discovery route",
        "affected-file repair route",
        "prior unsupported-claim validation route",
    )),
    ("closing_lock", (
        "This operation spec defines only a future candidate-record distinctness support recheck operation shape",
        "Recheck permission is not recheck completion",
        "Distinctness support is not candidate standing",
        "Distinctness support is not presence",
        "Distinctness support is not identity",
        "Candidate records marked distinct, if later supported by recheck, are still not standing candidates",
        "Only after a future recheck records DISTINCTNESS_SUPPORTED may a separately bounded candidate-standing boundary be considered",
        "Open means not scheduled, not authorized, and not executed",
    )),
)

# The standing specification uses compact prose for selected marker classes.
OPERATION_SPEC_MARKER_VARIANTS: dict[str, tuple[tuple[str, ...], ...]] = {
    "prior_distinctness_operation": (
        next(markers for name, markers in OPERATION_SPEC_MARKER_CLASSES if name == "prior_distinctness_operation"),
        (
            PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED,
            "distinctness_result = NOT_DISTINCT",
            "distinctness_supported = false",
            "two compared candidate records",
            "distinct ids and roles",
            "absent candidate-specific content",
            "absent separate seal, receipt, and digest material",
        ),
    ),
    "emitted_basis_material": (
        next(markers for name, markers in OPERATION_SPEC_MARKER_CLASSES if name == "emitted_basis_material"),
        (
            UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED,
            "candidate record `descendant_body_basis_candidate_a_001`",
            "role `CANDIDATE_A`",
            UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED,
            "Motion-side admissible variation",
            "Motion mandate",
            "non_standing_basis = true",
            "distinctness_supported = false",
            UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED,
            "candidate record `descendant_body_basis_candidate_b_001`",
            "role `CANDIDATE_B`",
            UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED,
            "Regulation-side admissibility bounds",
            "Regulation mandate",
        ),
    ),
    "successor_basis_emission": (
        next(markers for name, markers in OPERATION_SPEC_MARKER_CLASSES if name == "successor_basis_emission"),
        (
            UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_OUTCOME_REQUIRED,
            UPSTREAM_BASIS_EMISSION_SUCCESSOR_RESULT_REQUIRED,
            "upstream_candidate_specific_content_emitted_required = true",
            "upstream_candidate_a_basis_material_emitted_required = true",
            "upstream_candidate_b_basis_material_emitted_required = true",
            "upstream_separate_candidate_basis_material_emitted_required = true",
            "upstream_basis_pair_emitted_required = true",
            UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED,
            UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED,
            UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED,
            UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED,
            "upstream_basis_pair_scope_required = SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
            "upstream_candidate_records_marked_distinct_required = false",
            "upstream_distinctness_supported_recorded_required = false",
            "upstream_candidate_standing_authorized_required = false",
            "upstream_descendant_body_created_required = false",
            "upstream_relation_created_required = false",
            "upstream_coupling_created_required = false",
            "upstream_presence_established_required = false",
            "upstream_identity_created_required = false",
            "upstream_follow_on_authorized_required = false",
        ),
    ),
    "recheck_non_conversion": (
        next(markers for name, markers in OPERATION_SPEC_MARKER_CLASSES if name == "recheck_non_conversion"),
        (
            "Distinctness support is not candidate standing, descendant-body creation, crossing, relation, runtime, currentness, authority, coupling, presence, identity, or follow-on authorization.",
            "Candidate records marked distinct are still not standing candidates, descendant bodies, relation participants, presence-bearing, or identity-bearing.",
        ),
    ),
    "blocked_routes": (
        next(markers for name, markers in OPERATION_SPEC_MARKER_CLASSES if name == "blocked_routes"),
        (
            "Direct recheck permission to recheck completion.",
            "Direct basis emission to standing, descendant-body creation, or relation.",
            "Direct distinctness support to candidate standing, descendant-body creation, crossing, relation, runtime, authority/currentness, coupling creation, third-candidate route, third-model route, presence, identity, or follow-on work.",
            "Direct candidate records distinct to candidate standing, descendant-body creation, relation, presence, or identity.",
            "Repository scan, file discovery, affected-file repair, and prior unsupported-claim validation routes.",
        ),
    ),
    "contaminated_lineage": (
        next(markers for name, markers in OPERATION_SPEC_MARKER_CLASSES if name == "contaminated_lineage"),
        (
            "remains preserved contaminated lineage for the unsupported existence-claim class",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        ),
    ),
}

UPSTREAM_REQUIREMENTS = (
    (
        "prior_distinctness_operation_terminal_summary_reference",
        DEFAULT_PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED,
            "distinctness_result = NOT_DISTINCT",
            "distinctness_supported = false",
            "candidate records with distinct ids and roles",
            "candidate-specific content and separate seal, receipt, and digest material were absent",
        ), (
            PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED,
            "distinctness_result = NOT_DISTINCT",
            "distinctness_supported = false",
            "compared exactly two candidate records",
            "candidate-specific content",
            "separate seal material",
            "separate lineage receipt material",
            "separate digest material",
        )),
        "prior_distinctness_operation_terminal_summary_markers_present",
    ),
    (
        "successor_basis_emission_terminal_summary_reference",
        DEFAULT_SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE,
        "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 83",
            UPSTREAM_BASIS_EMISSION_SUCCESSOR_RESULT_REQUIRED,
            "candidate_specific_content_emitted = true",
            "candidate_a_basis_material_emitted = true",
            "candidate_b_basis_material_emitted = true",
            "separate_candidate_basis_material_emitted = true",
            "basis_pair_emitted = true",
            UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED,
            UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED,
            UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED,
            UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED,
            "basis_pair_scope = SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
        ),),
        "successor_basis_emission_terminal_summary_markers_present",
    ),
    (
        "existence_claim_evidence_check_terminal_summary_reference",
        DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE,
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
        (("UNSUPPORTED",),),
        "existence_claim_evidence_check_terminal_summary_markers_present",
    ),
    (
        "basis_emission_operation_terminal_summary_reference",
        DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS",),),
        "basis_emission_operation_terminal_summary_markers_present",
    ),
    (
        "successor_closure_operation_terminal_summary_reference",
        DEFAULT_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_CLOSED",),),
        "successor_closure_operation_terminal_summary_markers_present",
    ),
    (
        "scope_division_operation_terminal_summary_reference",
        DEFAULT_SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",),),
        "scope_division_operation_terminal_summary_markers_present",
    ),
)

WHAT_REMAINS_OPEN = (
    "candidate-standing boundary, if separately bounded after support",
    "candidate-standing checks",
    "divergent receipt-history route, if separately bounded",
    "carrier separation route, if separately bounded",
    "first crossing",
    "relation",
    "FIELD machinery",
    "runtime",
    "API",
    "currentness",
    "authority",
    "standing",
    "presence boundary",
    "identity boundary",
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
    normalized = key.casefold()
    return (
        normalized.startswith("raw_")
        or normalized.endswith("_body")
        or normalized in {
            "payload", "pdf_bytes", "file_bytes", "full_text", "full_body",
            "source_body", "extracted_text", "raw_extracted_text",
        }
    )


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


def _add_check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str | None = None,
    upstream: bool = False,
) -> None:
    check: dict[str, Any] = {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected),
        "actual_posture": _sanitize(actual),
        "upstream_basis_check": upstream,
    }
    if not passed and code:
        check["block_code"] = code
        check["failure_code"] = code
    checks.append(check)


def _failed_codes(checks: list[dict[str, Any]], upstream: bool | None = None) -> list[str]:
    return [
        str(check["block_code"])
        for check in checks
        if check.get("passed") is False
        and isinstance(check.get("block_code"), str)
        and check["block_code"] in BLOCK_CODES
        and (upstream is None or check.get("upstream_basis_check") is upstream)
    ]


def _markers_present(text: str, variants: tuple[tuple[str, ...], ...]) -> bool:
    normalized = text.casefold()
    return any(all(marker.casefold() in normalized for marker in markers) for markers in variants)


def _contains_all(text: str | None, markers: tuple[str, ...]) -> bool:
    if text is None:
        return False
    normalized = text.casefold()
    return all(marker.casefold() in normalized for marker in markers)


def _validate_exact_values(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    expected = (
        ("operation_id", OPERATION_ID),
        ("operation_type", OPERATION_TYPE),
        ("operation_version", OPERATION_VERSION),
        ("operation_scope", OPERATION_SCOPE),
        ("distinctness_support_recheck_operation_id", OPERATION_ID),
        ("distinctness_support_recheck_operation_type", OPERATION_TYPE),
        ("distinctness_support_recheck_operation_version", OPERATION_VERSION),
        ("distinctness_support_recheck_operation_scope", OPERATION_SCOPE),
        ("prior_distinctness_operation_type", PRIOR_DISTINCTNESS_OPERATION_TYPE),
        ("prior_distinctness_operation_outcome_required", PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED),
        ("prior_distinctness_result_required", PRIOR_DISTINCTNESS_RESULT_REQUIRED),
        ("prior_distinctness_supported_required", PRIOR_DISTINCTNESS_SUPPORTED_REQUIRED),
        ("upstream_basis_emission_successor_operation_type", UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_TYPE),
        ("upstream_basis_emission_successor_operation_outcome_required", UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_OUTCOME_REQUIRED),
        ("upstream_basis_emission_successor_result_required", UPSTREAM_BASIS_EMISSION_SUCCESSOR_RESULT_REQUIRED),
        ("upstream_candidate_specific_content_emitted_required", UPSTREAM_CANDIDATE_SPECIFIC_CONTENT_EMITTED_REQUIRED),
        ("upstream_candidate_a_basis_material_emitted_required", UPSTREAM_CANDIDATE_A_BASIS_MATERIAL_EMITTED_REQUIRED),
        ("upstream_candidate_b_basis_material_emitted_required", UPSTREAM_CANDIDATE_B_BASIS_MATERIAL_EMITTED_REQUIRED),
        ("upstream_separate_candidate_basis_material_emitted_required", UPSTREAM_SEPARATE_CANDIDATE_BASIS_MATERIAL_EMITTED_REQUIRED),
        ("upstream_basis_pair_emitted_required", UPSTREAM_BASIS_PAIR_EMITTED_REQUIRED),
        ("upstream_candidate_a_basis_id_required", UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED),
        ("upstream_candidate_b_basis_id_required", UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED),
        ("upstream_candidate_a_basis_label_required", UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED),
        ("upstream_candidate_b_basis_label_required", UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED),
        ("upstream_basis_pair_scope_required", UPSTREAM_BASIS_PAIR_SCOPE_REQUIRED),
        ("upstream_candidate_records_marked_distinct_required", False),
        ("upstream_distinctness_supported_recorded_required", False),
        ("upstream_candidate_standing_authorized_required", False),
        ("upstream_descendant_body_created_required", False),
        ("upstream_relation_created_required", False),
        ("upstream_coupling_created_required", False),
        ("upstream_presence_established_required", False),
        ("upstream_identity_created_required", False),
        ("upstream_follow_on_authorized_required", False),
        ("admissible_future_route", ADMISSIBLE_FUTURE_ROUTE),
    )
    for field, value in expected:
        _add_check(
            checks,
            f"{field} exact",
            request.get(field) == value,
            value,
            request.get(field),
            "BASIS_EMISSION_MATERIAL_MISSING_OR_INSUFFICIENT",
        )


def _code_for_non_claim(key: str) -> str:
    if any(token in key for token in ("candidate_standing", "descendant_body", "standing", "crossing")):
        return "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED"
    if any(token in key for token in ("relation", "runtime", "api", "currentness", "authority", "field_machinery")):
        return "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED"
    if any(token in key for token in ("coupling", "third_")):
        return "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    if any(token in key for token in ("presence", "identity")):
        return "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED"
    if any(token in key for token in ("repair", "scan", "discovery", "validation", "unsupported", "affected_file", "overwrite", "edited", "deleted", "replaced", "redeemed", "contaminated")):
        return "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED"
    return "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED"


def _validate_request_posture(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    declared = request.get("declared_non_claims")
    invalid = (
        list(REQUIRED_FALSE_NON_CLAIMS)
        if not isinstance(declared, Mapping)
        else [key for key in REQUIRED_FALSE_NON_CLAIMS if declared.get(key) is not False]
    )
    _add_check(
        checks,
        "required declared non-claims false",
        not invalid,
        "every required key exactly false",
        {"invalid_keys": invalid},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if request.get(key) is True:
            _add_check(
                checks,
                f"top-level false posture {key} not pre-claimed",
                False,
                False,
                True,
                _code_for_non_claim(key),
            )
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        if request.get(key) is True:
            _add_check(
                checks,
                f"result-only posture {key} not pre-claimed",
                False,
                "resolver output only",
                True,
                "RESULT_POSTURE_PRECLAIMED",
            )
    result_only_values = {
        "distinctness_support_recheck_result": "DISTINCTNESS_SUPPORT_RECHECKED",
        "distinctness_support_result": "DISTINCTNESS_SUPPORTED",
    }
    for field, value in result_only_values.items():
        if request.get(field) == value:
            _add_check(
                checks,
                f"result-only posture {field} not pre-claimed",
                False,
                "resolver output only",
                value,
                "RESULT_POSTURE_PRECLAIMED",
            )
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        _add_check(checks, f"{field} not requested", request.get(field) is not True, False, request.get(field), code)


def _validate_target_spec(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    path = _resolve_path(request.get("operation_spec_reference"))
    _add_check(
        checks,
        "operation spec reference readable",
        path is not None and path.is_file(),
        "declared readable spec path",
        str(path) if path else request.get("operation_spec_reference"),
        "DISTINCTNESS_SUPPORT_RECHECK_OPERATION_SPEC_REFERENCE_MISSING",
    )
    text = _read_text(request.get("operation_spec_reference"))
    missing = [
        name
        for name, markers in OPERATION_SPEC_MARKER_CLASSES
        if text is None or not _markers_present(text, OPERATION_SPEC_MARKER_VARIANTS.get(name, (markers,)))
    ]
    _add_check(
        checks,
        "distinctness support recheck operation spec posture classes present",
        not missing,
        "all required marker classes",
        {"missing_posture_classes": missing},
        "DISTINCTNESS_SUPPORT_RECHECK_OPERATION_SPEC_MARKER_MISSING",
    )


def _validate_upstream(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> list[str]:
    missing_basis: list[str] = []
    for field, _, reference_code, marker_code, variants, flag in UPSTREAM_REQUIREMENTS:
        text = _read_text(request.get(field))
        readable = text is not None
        _add_check(
            checks,
            f"{field} readable",
            readable,
            "declared readable terminal summary",
            request.get(field),
            reference_code,
            True,
        )
        present = readable and _markers_present(text, variants)
        _add_check(
            checks,
            f"{field} expected markers present",
            present,
            variants,
            {"missing_markers": [] if present else list(variants[0])},
            marker_code,
            True,
        )
        if not present:
            missing_basis.append(flag)
    return missing_basis


def _validate_support_quality(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> list[str]:
    """Validate separation and non-hierarchy after material existence is known."""

    text = _read_text(request.get("successor_basis_emission_terminal_summary_reference"))
    requirements = (
        ("candidate_a_non_standing", ("Candidate A basis material", "non_standing_basis = true")),
        ("candidate_b_non_standing", ("Candidate B basis material", "non_standing_basis = true")),
        ("sibling_non_standing_basis_pair", ("candidate_a_and_b_are_sibling_non_standing_basis_materials = true",)),
        ("basis_pair_non_hierarchy", ("neither_candidate_ranks_above_the_other = true",)),
        ("regulation_not_sovereign_over_motion", ("regulation_not_sovereign_over_motion = true",)),
        ("motion_does_not_erase_regulation", ("motion_does_not_erase_regulation = true",)),
        ("coupling_uncreated", ("coupling_assigned = false", "coupling_created = false")),
        ("no_third_candidate_or_model", ("third_candidate_created = false", "third_model_admitted = false")),
        ("upstream_distinctness_not_preclaimed", ("distinctness_supported_recorded = false", "candidate_records_marked_distinct = false")),
        ("upstream_standing_not_authorized", ("candidate_standing_authorized = false", "descendant_body_created = false", "relation_created = false", "presence_established = false", "identity_created = false", "follow_on_authorized = false")),
    )
    reasons: list[str] = []
    for name, markers in requirements:
        passed = _contains_all(text, markers)
        _add_check(
            checks,
            f"support quality {name}",
            passed,
            markers,
            {"missing_markers": [] if passed else list(markers)},
            "BASIS_EMISSION_MATERIAL_NOT_SUPPORTING_DISTINCTNESS",
            True,
        )
        if not passed:
            reasons.append(name)
    return reasons


def _marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    flags = {
        "distinctness_support_recheck_operation_spec_markers_present": any(
            check.get("check_name") == "distinctness support recheck operation spec posture classes present"
            and check.get("passed") is True
            for check in checks
        )
    }
    for field, *_, flag in UPSTREAM_REQUIREMENTS:
        flags[flag] = any(
            check.get("check_name") == f"{field} expected markers present"
            and check.get("passed") is True
            for check in checks
        )
    return flags


def _operation_object(outcome: str, flags: Mapping[str, bool]) -> dict[str, Any]:
    supported = outcome == OUTCOME_SUPPORTED
    requires = outcome == OUTCOME_REQUIRES_BASIS_EMISSION
    not_supported = outcome == OUTCOME_NOT_SUPPORTED
    result_value = (
        "DISTINCTNESS_SUPPORT_RECHECKED" if supported
        else "REQUIRES_BASIS_EMISSION" if requires
        else "DISTINCTNESS_NOT_SUPPORTED" if not_supported
        else "BLOCKED" if outcome == OUTCOME_BLOCKED
        else "NOT_RECHECKED"
    )
    support_value = "DISTINCTNESS_SUPPORTED" if supported else "NOT_SUPPORTED"
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "distinctness_support_recheck_operation_id": OPERATION_ID,
        "distinctness_support_recheck_operation_type": OPERATION_TYPE,
        "distinctness_support_recheck_operation_version": OPERATION_VERSION,
        "distinctness_support_recheck_operation_scope": OPERATION_SCOPE,
        "prior_distinctness_operation_type": PRIOR_DISTINCTNESS_OPERATION_TYPE,
        "prior_distinctness_operation_outcome_required": PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED,
        "prior_distinctness_result_required": PRIOR_DISTINCTNESS_RESULT_REQUIRED,
        "prior_distinctness_supported_required": PRIOR_DISTINCTNESS_SUPPORTED_REQUIRED,
        "upstream_basis_emission_successor_operation_type": UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_TYPE,
        "upstream_basis_emission_successor_operation_outcome_required": UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_OUTCOME_REQUIRED,
        "upstream_basis_emission_successor_result_required": UPSTREAM_BASIS_EMISSION_SUCCESSOR_RESULT_REQUIRED,
        "upstream_candidate_specific_content_emitted_required": True,
        "upstream_candidate_a_basis_material_emitted_required": True,
        "upstream_candidate_b_basis_material_emitted_required": True,
        "upstream_separate_candidate_basis_material_emitted_required": True,
        "upstream_basis_pair_emitted_required": True,
        "upstream_candidate_a_basis_id_required": UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED,
        "upstream_candidate_b_basis_id_required": UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED,
        "upstream_candidate_a_basis_label_required": UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED,
        "upstream_candidate_b_basis_label_required": UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED,
        "upstream_basis_pair_scope_required": UPSTREAM_BASIS_PAIR_SCOPE_REQUIRED,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        **_canonical_non_claims(),
        **flags,
    }
    operation.update({
        "distinctness_support_recheck_operation_recorded": supported,
        "distinctness_support_recheck_performed": supported,
        "distinctness_support_recheck_result_recorded": supported,
        "distinctness_support_recheck_result": result_value,
        "prior_not_distinct_result_referenced": supported,
        "emitted_candidate_specific_basis_material_referenced": supported,
        "candidate_a_basis_material_referenced": supported,
        "candidate_b_basis_material_referenced": supported,
        "basis_pair_referenced": supported,
        "candidate_specific_basis_material_compared": supported,
        "distinctness_supported_recorded": supported,
        "distinctness_support_result": support_value,
        "candidate_records_marked_distinct": supported,
        "candidate_records_distinct": supported,
    })
    return operation


def _support_material(supported: bool) -> dict[str, Any]:
    support_result = "DISTINCTNESS_SUPPORTED" if supported else "NOT_SUPPORTED"
    return {
        "candidate_a_basis_reference": {
            "basis_id": UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED,
            "candidate_record_id": "descendant_body_basis_candidate_a_001",
            "candidate_role": "CANDIDATE_A",
            "basis_label": UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED,
            "source_scope": "Motion-side admissible variation",
            "source_mandate": "Motion mandate",
            "non_standing_basis": True,
            "distinctness_supported_at_emission_time": False,
        },
        "candidate_b_basis_reference": {
            "basis_id": UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED,
            "candidate_record_id": "descendant_body_basis_candidate_b_001",
            "candidate_role": "CANDIDATE_B",
            "basis_label": UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED,
            "source_scope": "Regulation-side admissibility bounds",
            "source_mandate": "Regulation mandate",
            "non_standing_basis": True,
            "distinctness_supported_at_emission_time": False,
        },
        "basis_pair_reference": {
            "basis_pair_scope": UPSTREAM_BASIS_PAIR_SCOPE_REQUIRED,
            "candidate_a_and_b_are_sibling_non_standing_basis_materials": True,
            "neither_candidate_ranks_above_the_other": True,
            "regulation_not_sovereign_over_motion": True,
            "motion_does_not_erase_regulation": True,
            "coupling_assigned": False,
            "coupling_created": False,
            "third_candidate_created": False,
            "third_model_admitted": False,
            "candidate_standing_authorized": False,
        },
        "support_evaluation": {
            "prior_distinctness_result": PRIOR_DISTINCTNESS_RESULT_REQUIRED,
            "prior_distinctness_supported": False,
            "prior_absence_reason": "candidate-specific content and separate seal, receipt, and digest material were absent",
            "candidate_specific_basis_material_present": supported,
            "candidate_specific_basis_material_separate": supported,
            "candidate_specific_basis_material_non_standing": supported,
            "basis_pair_non_hierarchy_preserved": supported,
            "distinctness_support_result": support_result,
            "candidate_records_marked_distinct": supported,
            "candidate_records_distinct": supported,
            "candidate_standing_authorized": False,
            "descendant_body_created": False,
            "relation_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
        },
    }


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("descendant_body_candidate_record_distinctness_support_recheck_operation")
    op = operation if isinstance(operation, Mapping) else {}
    checks = result.get("distinctness_support_recheck_operation_checks")
    records = checks if isinstance(checks, list) else []
    upstream = result.get("upstream_basis")
    basis = upstream if isinstance(upstream, Mapping) else {}
    detail = result.get("recheck_result_detail")
    recheck_detail = detail if isinstance(detail, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "failed_check_count": sum(check.get("passed") is False for check in records if isinstance(check, Mapping)),
        "passed_check_count": sum(check.get("passed") is True for check in records if isinstance(check, Mapping)),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "operation_id": op.get("operation_id"),
        "operation_type": op.get("operation_type"),
        "operation_version": op.get("operation_version"),
        "operation_scope": op.get("operation_scope"),
        "prior_distinctness_operation_type": op.get("prior_distinctness_operation_type"),
        "prior_distinctness_operation_outcome_required": op.get("prior_distinctness_operation_outcome_required"),
        "prior_distinctness_result_required": op.get("prior_distinctness_result_required"),
        "prior_distinctness_supported_required": op.get("prior_distinctness_supported_required"),
        "upstream_basis_emission_successor_operation_type": op.get("upstream_basis_emission_successor_operation_type"),
        "upstream_basis_emission_successor_operation_outcome_required": op.get("upstream_basis_emission_successor_operation_outcome_required"),
        "upstream_basis_emission_successor_result_required": op.get("upstream_basis_emission_successor_result_required"),
        "candidate_a_basis_id": op.get("upstream_candidate_a_basis_id_required"),
        "candidate_b_basis_id": op.get("upstream_candidate_b_basis_id_required"),
        "candidate_a_basis_label": op.get("upstream_candidate_a_basis_label_required"),
        "candidate_b_basis_label": op.get("upstream_candidate_b_basis_label_required"),
        "basis_pair_scope": op.get("upstream_basis_pair_scope_required"),
        "distinctness_support_recheck_result": op.get("distinctness_support_recheck_result"),
        "distinctness_support_result": op.get("distinctness_support_result"),
        "selected_target_spec_path": basis.get("operation_spec_reference"),
        "completed_prior_distinctness_terminal_summary_path": basis.get("prior_distinctness_operation_terminal_summary_reference"),
        "completed_successor_basis_emission_terminal_summary_path": basis.get("successor_basis_emission_terminal_summary_reference"),
        "missing_or_insufficient_basis_emission_material": recheck_detail.get("missing_or_insufficient_basis_emission_material", []),
        "not_supported_reasons": recheck_detail.get("not_supported_reasons", []),
    }
    for key in (*ALLOWED_TRUE_RECORDED_FIELDS, *REQUIRED_FALSE_NON_CLAIMS):
        summary[key] = op.get(key)
    summary["distinctness_support_recheck_operation_spec_markers_present"] = op.get("distinctness_support_recheck_operation_spec_markers_present")
    for _, _, _, _, _, flag in UPSTREAM_REQUIREMENTS:
        summary[flag] = op.get(flag)
    return _sanitize(summary)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_basis: list[str],
    not_supported_reasons: list[str],
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    flags = _marker_flags(checks)
    operation = _operation_object(outcome, flags)
    supported = outcome == OUTCOME_SUPPORTED
    result: dict[str, Any] = {
        "distinctness_support_recheck_operation_metadata": {
            "operation_id": OPERATION_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_distinctness_support_recheck_operation_basis": _sanitize(request),
        "upstream_basis": {
            "operation_spec_reference": request.get("operation_spec_reference"),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **flags,
        },
        "descendant_body_candidate_record_distinctness_support_recheck_operation": operation,
        "distinctness_support_recheck_material": _support_material(supported),
        "distinctness_support_recheck_operation_checks": checks,
        "distinctness_support_recheck_operation_statement": {
            "outcome": outcome,
            "distinctness_support_recheck_operation_recorded": operation["distinctness_support_recheck_operation_recorded"],
            "distinctness_supported_recorded": operation["distinctness_supported_recorded"],
            "candidate_records_marked_distinct": operation["candidate_records_marked_distinct"],
            "candidate_standing_authorized": False,
            "descendant_body_created": False,
            "result_level_non_claims_canonical_false": True,
        },
        "distinctness_support_recheck_operation_non_meaning": {
            "not_candidate_standing": True,
            "not_descendant_body_creation": True,
            "not_relation": True,
            "not_runtime": True,
            "not_authority": True,
            "not_coupling": True,
            "not_presence": True,
            "not_identity": True,
            "not_follow_on": True,
        },
        "recheck_result_detail": {
            "distinctness_support_recheck_result": operation["distinctness_support_recheck_result"],
            "distinctness_support_result": operation["distinctness_support_result"],
            "missing_or_insufficient_basis_emission_material": list(missing_basis),
            "not_supported_reasons": list(not_supported_reasons),
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "candidate_standing_boundary_consideration_requires_separate_bounded_step": True,
        },
        "blocked_routes": [
            "standing, bodies, crossing, relation, runtime, authority, coupling, presence, identity, repair, discovery, and downstream authorization",
        ],
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
            "reason": block_reason if outcome == OUTCOME_BLOCKED else None,
        },
    }
    result["distinctness_support_recheck_operation_summary"] = _build_summary(result)
    return result


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    missing_basis: list[str] | None = None,
    not_supported_reasons: list[str] | None = None,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        missing_basis or [],
        not_supported_reasons or [],
        code,
        reason,
    )


def build_declared_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one declared no-discovery request for the bounded recheck."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "distinctness_support_recheck_operation_id": OPERATION_ID,
        "distinctness_support_recheck_operation_type": OPERATION_TYPE,
        "distinctness_support_recheck_operation_version": OPERATION_VERSION,
        "distinctness_support_recheck_operation_scope": OPERATION_SCOPE,
        "prior_distinctness_operation_type": PRIOR_DISTINCTNESS_OPERATION_TYPE,
        "prior_distinctness_operation_outcome_required": PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED,
        "prior_distinctness_result_required": PRIOR_DISTINCTNESS_RESULT_REQUIRED,
        "prior_distinctness_supported_required": PRIOR_DISTINCTNESS_SUPPORTED_REQUIRED,
        "upstream_basis_emission_successor_operation_type": UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_TYPE,
        "upstream_basis_emission_successor_operation_outcome_required": UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_OUTCOME_REQUIRED,
        "upstream_basis_emission_successor_result_required": UPSTREAM_BASIS_EMISSION_SUCCESSOR_RESULT_REQUIRED,
        "upstream_candidate_specific_content_emitted_required": True,
        "upstream_candidate_a_basis_material_emitted_required": True,
        "upstream_candidate_b_basis_material_emitted_required": True,
        "upstream_separate_candidate_basis_material_emitted_required": True,
        "upstream_basis_pair_emitted_required": True,
        "upstream_candidate_a_basis_id_required": UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED,
        "upstream_candidate_b_basis_id_required": UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED,
        "upstream_candidate_a_basis_label_required": UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED,
        "upstream_candidate_b_basis_label_required": UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED,
        "upstream_basis_pair_scope_required": UPSTREAM_BASIS_PAIR_SCOPE_REQUIRED,
        "upstream_candidate_records_marked_distinct_required": False,
        "upstream_distinctness_supported_recorded_required": False,
        "upstream_candidate_standing_authorized_required": False,
        "upstream_descendant_body_created_required": False,
        "upstream_relation_created_required": False,
        "upstream_coupling_created_required": False,
        "upstream_presence_established_required": False,
        "upstream_identity_created_required": False,
        "upstream_follow_on_authorized_required": False,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "operation_spec_reference": DEFAULT_OPERATION_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in ALLOWED_TRUE_RECORDED_FIELDS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


def resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(
    declared_distinctness_support_recheck_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded recheck without discovery or downstream conversion."""

    if declared_distinctness_support_recheck_operation is None:
        request = build_declared_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_request()
    elif not isinstance(declared_distinctness_support_recheck_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_distinctness_support_recheck_operation).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_distinctness_support_recheck_operation))

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
    not_supported_reasons = _validate_support_quality(checks, request)
    non_upstream_failures = _failed_codes(checks, False)
    if non_upstream_failures:
        code = non_upstream_failures[0]
        return _blocked_result(request, checks, code, f"blocked by failed check {code}", missing_basis, not_supported_reasons)
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, missing_basis, not_supported_reasons)
    if missing_basis:
        return _build_result(request, OUTCOME_REQUIRES_BASIS_EMISSION, checks, missing_basis, not_supported_reasons)
    if not_supported_reasons:
        return _build_result(request, OUTCOME_NOT_SUPPORTED, checks, [], not_supported_reasons)
    return _build_result(request, OUTCOME_SUPPORTED, checks, [], [])


def resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_from_path(
    declared_distinctness_support_recheck_operation_path: Path | str,
) -> dict[str, Any]:
    """Read one explicit JSON request object and resolve it."""

    path = Path(declared_distinctness_support_recheck_operation_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            request = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request path readable JSON", False, "readable JSON object", str(exc), "REQUEST_NOT_MAPPING")
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request path is unreadable or not JSON")
    return resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(request)


def build_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return compact metadata for one bounded distinctness-support recheck."""

    return _build_summary(result)


def write_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write deterministic sanitized JSON without silently overwriting files."""

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
        raise DescendantBodyCandidateRecordDistinctnessSupportRecheckOperationV0MinError(
            f"WRITE_REFUSED: {exc}"
        ) from exc
