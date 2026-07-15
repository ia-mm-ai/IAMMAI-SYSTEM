"""Resolve one bounded descendant-body candidate-standing operation result.

This resolver evaluates only Candidate A and Candidate B after a completed
candidate-standing boundary allows that consideration. Candidate standing may
be supported, authorized, and created only as candidate standing. It does not
create descendant bodies, relation, runtime, authority, coupling, presence,
identity, or any downstream authorization.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateStandingOperationV0MinError(Exception):
    """Raised when a bounded candidate-standing operation result cannot be written."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_standing_operation_v0_min"

OPERATION_ID = "descendant_body_candidate_standing_operation_001"
OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EVALUATE_CANDIDATE_STANDING_AFTER_BOUNDARY_ALLOWANCE_ONLY"
PRIOR_CANDIDATE_STANDING_BOUNDARY_TYPE = "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY"
PRIOR_CANDIDATE_STANDING_BOUNDARY_OUTCOME_REQUIRED = (
    "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_ALLOWED"
)
PRIOR_CANDIDATE_STANDING_BOUNDARY_RESULT_REQUIRED = (
    "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED"
)
PRIOR_CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED_REQUIRED = True
PRIOR_SUPPORTED_DISTINCTNESS_REFERENCED_REQUIRED = True
PRIOR_CANDIDATE_RECORDS_DISTINCT_REFERENCED_REQUIRED = True
PRIOR_CANDIDATE_STANDING_CHECK_PERFORMED_REQUIRED = False
PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED = False
PRIOR_CANDIDATE_STANDING_CREATED_REQUIRED = False
PRIOR_DESCENDANT_BODY_CREATED_REQUIRED = False
PRIOR_RELATION_CREATED_REQUIRED = False
PRIOR_COUPLING_CREATED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_IDENTITY_CREATED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = (
    "CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY"
)

CANDIDATE_A_RECORD_ID = "descendant_body_basis_candidate_a_001"
CANDIDATE_B_RECORD_ID = "descendant_body_basis_candidate_b_001"
CANDIDATE_A_BASIS_ID = (
    "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis"
)
CANDIDATE_B_BASIS_ID = (
    "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis"
)
CANDIDATE_A_ROLE = "CANDIDATE_A"
CANDIDATE_B_ROLE = "CANDIDATE_B"
CANDIDATE_A_BASIS_LABEL = "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS"
CANDIDATE_B_BASIS_LABEL = "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
BASIS_PAIR_SCOPE = "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY"

OUTCOME_SUPPORTED = "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_SUPPORTED"
OUTCOME_NOT_SUPPORTED = "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_NOT_SUPPORTED"
OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE = (
    "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE"
)
OUTCOME_BLOCKED = "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_SUPPORTED,
    OUTCOME_NOT_SUPPORTED,
    OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_standing_operation_v0_min"
)
DETERMINISTIC_FILENAME = (
    "descendant_body_candidate_standing_operation_001__candidate_standing_operation_v0_min_result.json"
)

DEFAULT_CANDIDATE_STANDING_OPERATION_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_V0_MIN_SPEC.md"
)
DEFAULT_CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "candidate_standing_operation_recorded",
    "candidate_standing_check_performed",
    "candidate_standing_result_recorded",
    "candidate_a_standing_evaluated",
    "candidate_b_standing_evaluated",
    "candidate_a_standing_supported",
    "candidate_b_standing_supported",
    "candidate_standing_supported",
    "candidate_standing_authorized",
    "candidate_standing_created",
    "candidate_a_standing_created",
    "candidate_b_standing_created",
)

REQUIRED_FALSE_NON_CLAIMS = (
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
    "candidate_standing_boundary_overridden",
    "candidate_standing_boundary_bypassed",
    "distinctness_support_recheck_operation_overridden",
    "distinctness_support_recheck_operation_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_candidate_standing_operation_spec_to_candidate_standing_operation_completion",
    "direct_boundary_allowance_to_candidate_standing_without_operation",
    "direct_supported_distinctness_to_candidate_standing_without_boundary_and_operation",
    "direct_candidate_standing_to_descendant_body_creation",
    "direct_candidate_standing_to_crossing",
    "direct_candidate_standing_to_relation",
    "direct_candidate_standing_to_runtime",
    "direct_candidate_standing_to_authority_currentness",
    "direct_candidate_standing_to_coupling_creation",
    "direct_candidate_standing_to_third_candidate_route",
    "direct_candidate_standing_to_third_model_route",
    "direct_candidate_standing_to_presence",
    "direct_candidate_standing_to_identity",
    "direct_candidate_standing_to_follow_on_work",
    "direct_candidate_standing_to_standing_descendant",
    "direct_candidate_standing_to_descendant_standing",
    "direct_candidate_standing_to_output_action",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "CANDIDATE_STANDING_OPERATION_SPEC_REFERENCE_MISSING",
    "CANDIDATE_STANDING_OPERATION_SPEC_MARKER_MISSING",
    "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "BOUNDARY_ALLOWANCE_MISSING_OR_INSUFFICIENT",
    "CANDIDATE_STANDING_NOT_SUPPORTED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "RESULT_POSTURE_PRECLAIMED",
    "PROHIBITED_DESCENDANT_BODY_REQUESTED",
    "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_descendant_body_a_creation": "PROHIBITED_DESCENDANT_BODY_REQUESTED",
    "request_descendant_body_b_creation": "PROHIBITED_DESCENDANT_BODY_REQUESTED",
    "request_descendant_body_creation": "PROHIBITED_DESCENDANT_BODY_REQUESTED",
    "request_standing_authorization": "PROHIBITED_DESCENDANT_BODY_REQUESTED",
    "request_standing_descendant_creation": "PROHIBITED_DESCENDANT_BODY_REQUESTED",
    "request_descendant_standing_check": "PROHIBITED_DESCENDANT_BODY_REQUESTED",
    "request_crossing_authorization": "PROHIBITED_DESCENDANT_BODY_REQUESTED",
    "request_first_crossing_authorization": "PROHIBITED_DESCENDANT_BODY_REQUESTED",
    "request_relation_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_DESCENDANT_BODY_REQUESTED",
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
    "request_follow_on_work_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
}

EXPECTED_REQUEST_VALUES = {
    "operation_id": OPERATION_ID,
    "operation_type": OPERATION_TYPE,
    "operation_version": OPERATION_VERSION,
    "operation_scope": OPERATION_SCOPE,
    "candidate_standing_operation_id": OPERATION_ID,
    "candidate_standing_operation_type": OPERATION_TYPE,
    "candidate_standing_operation_version": OPERATION_VERSION,
    "candidate_standing_operation_scope": OPERATION_SCOPE,
    "prior_candidate_standing_boundary_type": PRIOR_CANDIDATE_STANDING_BOUNDARY_TYPE,
    "prior_candidate_standing_boundary_outcome_required": PRIOR_CANDIDATE_STANDING_BOUNDARY_OUTCOME_REQUIRED,
    "prior_candidate_standing_boundary_result_required": PRIOR_CANDIDATE_STANDING_BOUNDARY_RESULT_REQUIRED,
    "prior_candidate_standing_operation_consideration_allowed_required": PRIOR_CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED_REQUIRED,
    "prior_supported_distinctness_referenced_required": PRIOR_SUPPORTED_DISTINCTNESS_REFERENCED_REQUIRED,
    "prior_candidate_records_distinct_referenced_required": PRIOR_CANDIDATE_RECORDS_DISTINCT_REFERENCED_REQUIRED,
    "prior_candidate_standing_check_performed_required": PRIOR_CANDIDATE_STANDING_CHECK_PERFORMED_REQUIRED,
    "prior_candidate_standing_authorized_required": PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED,
    "prior_candidate_standing_created_required": PRIOR_CANDIDATE_STANDING_CREATED_REQUIRED,
    "prior_descendant_body_created_required": PRIOR_DESCENDANT_BODY_CREATED_REQUIRED,
    "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
    "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
    "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
    "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
    "candidate_a_record_id": CANDIDATE_A_RECORD_ID,
    "candidate_b_record_id": CANDIDATE_B_RECORD_ID,
    "candidate_a_basis_id": CANDIDATE_A_BASIS_ID,
    "candidate_b_basis_id": CANDIDATE_B_BASIS_ID,
    "candidate_a_role": CANDIDATE_A_ROLE,
    "candidate_b_role": CANDIDATE_B_ROLE,
    "candidate_a_basis_label": CANDIDATE_A_BASIS_LABEL,
    "candidate_b_basis_label": CANDIDATE_B_BASIS_LABEL,
    "basis_pair_scope": BASIS_PAIR_SCOPE,
    "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
}

OPERATION_SPEC_MARKER_CLASSES = (
    ("operation_identity", ((
        "Descendant Body Candidate Standing Operation V0 Minimum Specification",
        OPERATION_TYPE,
        OPERATION_ID,
        OPERATION_SCOPE,
    ),)),
    ("boundary_allowance", ((
        PRIOR_CANDIDATE_STANDING_BOUNDARY_OUTCOME_REQUIRED,
        PRIOR_CANDIDATE_STANDING_BOUNDARY_RESULT_REQUIRED,
        "candidate_standing_operation_consideration_allowed = true",
        "supported_distinctness_referenced = true",
        "candidate_records_distinct_referenced = true",
        "candidate_standing_check_performed = false",
        "candidate_standing_authorized = false",
        "candidate_standing_created = false",
        "descendant_body_created = false",
        "relation_created = false",
        "coupling_created = false",
        "presence_established = false",
        "identity_created = false",
        "follow_on_authorized = false",
    ),)),
    ("distinctness_support", (
        (
            "DISTINCTNESS_SUPPORTED",
            "candidate_records_marked_distinct = true",
            "candidate_records_distinct = true",
            "candidate records marked distinct are not standing candidates",
        ),
        (
            "DISTINCTNESS_SUPPORTED",
            "candidate_records_marked_distinct = true",
            "candidate_records_distinct = true",
            "marked-distinct candidate records are not standing candidates",
        ),
    )),
    ("successor_basis_emission", ((
        "separate non-standing Candidate A and Candidate B basis material",
        "basis-pair non-hierarchy",
        CANDIDATE_A_BASIS_ID,
        CANDIDATE_B_BASIS_ID,
        CANDIDATE_A_BASIS_LABEL,
        CANDIDATE_B_BASIS_LABEL,
        BASIS_PAIR_SCOPE,
    ),)),
    ("candidate_identity", ((
        CANDIDATE_A_RECORD_ID,
        CANDIDATE_B_RECORD_ID,
        CANDIDATE_A_ROLE,
        CANDIDATE_B_ROLE,
        "Motion-side admissible variation",
        "Regulation-side admissibility bounds",
    ),)),
    ("standing_evaluation_material", ((
        "candidate_a_standing_evaluation",
        "candidate_b_standing_evaluation",
        "standing_pair_evaluation",
        "candidate_standing_supported = true",
        "candidate_standing_authorized = true",
        "candidate_standing_created = true",
        "descendant_body_created = false",
        "relation_created = false",
        "presence_established = false",
        "identity_created = false",
    ),)),
    ("standing_non_conversion", (
        (
            "Candidate standing is not descendant-body creation",
            "Candidate standing is not crossing",
            "Candidate standing is not relation",
            "Candidate standing is not runtime",
            "Candidate standing is not currentness",
            "Candidate standing is not authority",
            "Candidate standing is not coupling",
            "Candidate standing is not presence",
            "Candidate standing is not identity",
            "Candidate standing is not follow-on authorization",
            "Candidate standing is not standing descendant",
            "Candidate standing is not descendant body",
            "Candidate standing is not relation participation",
            "Candidate standing is not presence-bearing",
            "Candidate standing is not identity-bearing",
        ),
        (
            "Candidate standing is not descendant-body creation, crossing, relation, runtime, currentness, authority, coupling, presence, identity, follow-on authorization, standing descendant, descendant body, relation participation, presence-bearing, or identity-bearing",
        ),
    )),
    ("sibling_non_hierarchy", ((
        "Candidate A and Candidate B remain sibling candidate records",
        "Neither candidate standing ranks above the other",
        "Regulation may not become sovereign over Motion",
        "Motion may not erase Regulation",
        "Coupling remains unassigned",
    ),)),
    ("permitted_route", ((
        ADMISSIBLE_FUTURE_ROUTE,
        "Only after a future candidate-standing operation records CANDIDATE_STANDING_SUPPORTED may a separately bounded descendant-body creation boundary be considered",
        "No later operation is authorized by this specification alone",
    ),)),
    ("contaminated_lineage", (
        (
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        ),
        (
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` remains preserved contaminated lineage",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        ),
    )),
    ("blocked_routes", (
        (
            "direct candidate-standing operation spec to candidate-standing operation completion",
            "direct boundary allowance to candidate standing without operation",
            "direct supported distinctness to candidate standing without boundary and operation",
            "direct candidate standing to descendant-body creation",
            "direct candidate standing to crossing",
            "direct candidate standing to relation",
            "direct candidate standing to runtime",
            "direct candidate standing to authority/currentness",
            "direct candidate standing to coupling creation",
            "direct candidate standing to third-candidate route",
            "direct candidate standing to third-model route",
            "direct candidate standing to presence",
            "direct candidate standing to identity",
            "direct candidate standing to follow-on work",
            "direct candidate standing to standing descendant",
            "direct candidate standing to descendant standing",
            "direct candidate standing to output/action",
            "repository scan route",
            "file discovery route",
            "affected-file repair route",
            "prior unsupported-claim validation route",
        ),
        (
            "direct candidate-standing operation spec to candidate-standing operation completion",
            "direct boundary allowance to candidate standing without operation",
            "direct supported distinctness to candidate standing without boundary and operation",
            "direct candidate standing to descendant-body creation, crossing, relation, runtime, authority/currentness, coupling creation, third-candidate route, third-model route, presence, identity, follow-on work, standing descendant, descendant standing, or output/action",
            "repository scan",
            "file discovery",
            "affected-file repair",
            "prior unsupported-claim validation",
        ),
    )),
    ("closing_lock", ((
        "This operation spec defines only a future candidate-standing operation shape",
        "It does not perform candidate-standing checks",
        "Candidate-standing operation spec is not candidate-standing operation result",
        "Candidate-standing operation permission is not candidate-standing completion",
        "Candidate standing is not descendant-body creation",
        "Candidate standing is not presence",
        "Candidate standing is not identity",
        "Candidate standing, if later supported, remains prior to any descendant-body creation boundary",
        "Open means not scheduled, not authorized, and not executed",
    ),)),
)

UPSTREAM_REQUIREMENTS = (
    (
        "candidate_standing_boundary_terminal_summary_reference",
        DEFAULT_CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            PRIOR_CANDIDATE_STANDING_BOUNDARY_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 170",
            PRIOR_CANDIDATE_STANDING_BOUNDARY_RESULT_REQUIRED,
            "candidate_standing_operation_consideration_allowed = true",
            "supported_distinctness_referenced = true",
            "candidate_records_distinct_referenced = true",
            "candidate_standing_check_performed = false",
            "candidate_standing_authorized = false",
            "candidate_standing_created = false",
            "descendant_body_created = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ),),
        "candidate_standing_boundary_terminal_summary_markers_present",
        True,
    ),
    (
        "distinctness_support_recheck_terminal_summary_reference",
        DEFAULT_DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE,
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_MARKER_MISSING",
        (
            (
                "DISTINCTNESS_SUPPORTED",
                "candidate_records_marked_distinct = true",
                "candidate_records_distinct = true",
                "candidate records marked distinct are not standing candidates",
                "candidate_standing_authorized = false",
                "descendant_body_created = false",
                "relation_created = false",
                "presence_established = false",
                "identity_created = false",
                "follow_on_authorized = false",
            ),
            (
                "DISTINCTNESS_SUPPORTED",
                "candidate_records_marked_distinct = true",
                "candidate_records_distinct = true",
                "Candidate records marked distinct are still not standing candidates",
                "candidate_standing_authorized = false",
                "descendant_body_created = false",
                "relation_created = false",
                "presence_established = false",
                "identity_created = false",
                "follow_on_authorized = false",
            ),
        ),
        "distinctness_support_recheck_terminal_summary_markers_present",
        True,
    ),
    (
        "successor_basis_emission_terminal_summary_reference",
        DEFAULT_SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE,
        "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_MARKER_MISSING",
        (
            (
                "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_EMITTED",
                "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED",
                "Separate non-standing Candidate A and Candidate B basis material",
                "basis-pair non-hierarchy",
                CANDIDATE_A_BASIS_ID,
                CANDIDATE_B_BASIS_ID,
            ),
            (
                "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_EMITTED",
                "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED",
                "Separate non-standing Candidate A and Candidate B basis material",
                "candidate_a_and_b_are_sibling_non_standing_basis_materials",
                "neither_candidate_ranks_above_the_other",
                CANDIDATE_A_BASIS_ID,
                CANDIDATE_B_BASIS_ID,
            ),
        ),
        "successor_basis_emission_terminal_summary_markers_present",
        True,
    ),
    (
        "existence_claim_evidence_check_terminal_summary_reference",
        DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE,
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
        (("UNSUPPORTED",),),
        "existence_claim_evidence_check_terminal_summary_markers_present",
        False,
    ),
    (
        "prior_distinctness_operation_terminal_summary_reference",
        DEFAULT_PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("NOT_DISTINCT",),),
        "prior_distinctness_operation_terminal_summary_markers_present",
        False,
    ),
    (
        "successor_closure_operation_terminal_summary_reference",
        DEFAULT_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("CLOSED",),),
        "successor_closure_operation_terminal_summary_markers_present",
        False,
    ),
    (
        "scope_division_operation_terminal_summary_reference",
        DEFAULT_SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("REQUIRES_ADDITIONAL_BASIS",),),
        "scope_division_operation_terminal_summary_markers_present",
        False,
    ),
)

WHAT_REMAINS_OPEN = (
    "descendant-body creation boundary, if separately bounded after candidate standing support",
    "descendant-body creation operation, if separately bounded after boundary",
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
        or normalized.startswith("hidden_")
        or normalized.endswith("_body")
        or normalized in {"payload", "file_bytes", "full_body", "full_text", "source_body"}
    )


def _sanitize(value: Any, key: str = "") -> Any:
    if isinstance(value, (bytes, bytearray, memoryview)):
        return "[REDACTED_BINARY_CONTENT]"
    if isinstance(value, Mapping):
        return {str(name): _sanitize(item, str(name)) for name, item in value.items()}
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


def _markers_present(text: str | None, variants: tuple[tuple[str, ...], ...]) -> bool:
    if text is None:
        return False
    normalized = text.casefold()
    return any(all(marker.casefold() in normalized for marker in markers) for markers in variants)


def _failed_codes(
    checks: list[dict[str, Any]], upstream: bool | None = None
) -> list[str]:
    return [
        str(check["block_code"])
        for check in checks
        if check.get("passed") is False
        and isinstance(check.get("block_code"), str)
        and check["block_code"] in BLOCK_CODES
        and (upstream is None or check.get("upstream_basis_check") is upstream)
    ]


def _marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    flags: dict[str, bool] = {}
    for check in checks:
        name = check.get("check_name")
        if isinstance(name, str) and name.endswith("markers present"):
            flags[name.replace(" ", "_")] = check.get("passed") is True
    return flags


def _code_for_false_posture(key: str) -> str:
    if key in {
        "descendant_body_a_created", "descendant_body_b_created", "descendant_body_created",
        "standing_authorized", "standing_descendant_created", "descendant_standing_check_performed",
        "crossing_authorized", "first_crossing_authorized", "standing_created",
    }:
        return "PROHIBITED_DESCENDANT_BODY_REQUESTED"
    if key in {
        "relation_created", "field_machinery_created", "runtime_created", "api_created",
        "currentness_created", "authority_created",
    }:
        return "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED"
    if key in {
        "coupling_assigned_to_candidate_a", "coupling_assigned_to_candidate_b", "coupling_created",
        "third_candidate_created", "third_model_admitted",
    }:
        return "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    if key in {"presence_established", "identity_created"}:
        return "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED"
    if key in {
        "output_authorized", "action_authorized", "derivative_reception_authorized",
        "synchronization_authorized", "follow_on_authorized", "follow_on_work_authorized",
    }:
        return "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED"
    if key in {
        "scan_performed", "repository_scan_performed", "file_discovery_performed",
        "repair_performed", "validation_enforced", "hidden_repair_performed",
        "silent_overwrite_performed", "affected_file_repaired", "affected_file_edited",
        "affected_file_deleted", "affected_file_overwritten", "affected_file_replaced",
        "affected_file_redeemed", "affected_file_treated_as_clean_basis",
        "prior_unsupported_candidate_a_claim_validated",
        "prior_unsupported_candidate_b_claim_validated",
        "prior_unsupported_derivation_event_claim_validated",
    }:
        return "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED"
    return "NON_CLAIM_MISSING_OR_FLIPPED"


def _validate_exact_values(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    for key, expected in EXPECTED_REQUEST_VALUES.items():
        _add_check(
            checks,
            f"declared {key} exact",
            request.get(key) == expected,
            expected,
            request.get(key),
            "UNSUPPORTED_INTENT",
        )


def _validate_request_posture(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    declared_non_claims = request.get("declared_non_claims")
    if not isinstance(declared_non_claims, Mapping):
        _add_check(
            checks,
            "declared non-claims mapping",
            False,
            "mapping with canonical false posture",
            type(declared_non_claims).__name__,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    else:
        for key in REQUIRED_FALSE_NON_CLAIMS:
            value = declared_non_claims.get(key)
            _add_check(
                checks,
                f"declared non-claim {key} false",
                value is False,
                False,
                value,
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )

    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        if key in request:
            _add_check(
                checks,
                f"result posture {key} not pre-claimed",
                request.get(key) is False,
                False,
                request.get(key),
                "RESULT_POSTURE_PRECLAIMED",
            )
    if "candidate_standing_result" in request:
        _add_check(
            checks,
            "candidate-standing result not pre-claimed",
            False,
            "resolver-derived result only",
            request.get("candidate_standing_result"),
            "RESULT_POSTURE_PRECLAIMED",
        )
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key in request:
            _add_check(
                checks,
                f"top-level false posture {key}",
                request.get(key) is False,
                False,
                request.get(key),
                _code_for_false_posture(key),
            )
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        _add_check(
            checks,
            f"prohibited request flag {field} false",
            request.get(field) is False,
            False,
            request.get(field),
            code,
        )


def _validate_target_spec(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    reference = request.get("candidate_standing_operation_spec_reference")
    text = _read_text(reference)
    _add_check(
        checks,
        "candidate-standing operation specification reference readable",
        text is not None,
        "readable declared specification",
        reference,
        "CANDIDATE_STANDING_OPERATION_SPEC_REFERENCE_MISSING",
    )
    if text is None:
        return
    for class_name, variants in OPERATION_SPEC_MARKER_CLASSES:
        _add_check(
            checks,
            f"candidate-standing operation specification {class_name} markers present",
            _markers_present(text, variants),
            "posture marker class present",
            class_name,
            "CANDIDATE_STANDING_OPERATION_SPEC_MARKER_MISSING",
        )


def _validate_upstream(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> list[str]:
    missing_boundary_allowance: list[str] = []
    for field, _, missing_code, marker_code, variants, flag, is_allowance in UPSTREAM_REQUIREMENTS:
        reference = request.get(field)
        text = _read_text(reference)
        _add_check(
            checks,
            f"{field} readable",
            text is not None,
            "readable declared terminal summary",
            reference,
            missing_code,
            upstream=True,
        )
        present = _markers_present(text, variants)
        _add_check(
            checks,
            f"{flag}",
            present,
            "required terminal-summary posture markers",
            reference if text is None else flag,
            marker_code,
            upstream=True,
        )
        if is_allowance and not present:
            missing_boundary_allowance.append(flag)
    return missing_boundary_allowance


def _operation_result_value(outcome: str) -> str:
    if outcome == OUTCOME_SUPPORTED:
        return "CANDIDATE_STANDING_SUPPORTED"
    if outcome == OUTCOME_NOT_SUPPORTED:
        return "CANDIDATE_STANDING_NOT_SUPPORTED"
    if outcome == OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE:
        return "REQUIRES_BOUNDARY_ALLOWANCE"
    if outcome == OUTCOME_BLOCKED:
        return "BLOCKED"
    return "NOT_RECORDED"


def _operation_object(outcome: str, marker_flags: Mapping[str, bool]) -> dict[str, Any]:
    evaluated = outcome in {OUTCOME_SUPPORTED, OUTCOME_NOT_SUPPORTED}
    supported = outcome == OUTCOME_SUPPORTED
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "candidate_standing_operation_id": OPERATION_ID,
        "candidate_standing_operation_type": OPERATION_TYPE,
        "candidate_standing_operation_version": OPERATION_VERSION,
        "candidate_standing_operation_scope": OPERATION_SCOPE,
        "prior_candidate_standing_boundary_type": PRIOR_CANDIDATE_STANDING_BOUNDARY_TYPE,
        "prior_candidate_standing_boundary_outcome_required": PRIOR_CANDIDATE_STANDING_BOUNDARY_OUTCOME_REQUIRED,
        "prior_candidate_standing_boundary_result_required": PRIOR_CANDIDATE_STANDING_BOUNDARY_RESULT_REQUIRED,
        "prior_candidate_standing_operation_consideration_allowed_required": PRIOR_CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED_REQUIRED,
        "prior_supported_distinctness_referenced_required": PRIOR_SUPPORTED_DISTINCTNESS_REFERENCED_REQUIRED,
        "prior_candidate_records_distinct_referenced_required": PRIOR_CANDIDATE_RECORDS_DISTINCT_REFERENCED_REQUIRED,
        "prior_candidate_standing_check_performed_required": PRIOR_CANDIDATE_STANDING_CHECK_PERFORMED_REQUIRED,
        "prior_candidate_standing_authorized_required": PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED,
        "prior_candidate_standing_created_required": PRIOR_CANDIDATE_STANDING_CREATED_REQUIRED,
        "prior_descendant_body_created_required": PRIOR_DESCENDANT_BODY_CREATED_REQUIRED,
        "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
        "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
        "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
        "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
        "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
        "candidate_a_record_id": CANDIDATE_A_RECORD_ID,
        "candidate_b_record_id": CANDIDATE_B_RECORD_ID,
        "candidate_a_basis_id": CANDIDATE_A_BASIS_ID,
        "candidate_b_basis_id": CANDIDATE_B_BASIS_ID,
        "candidate_a_role": CANDIDATE_A_ROLE,
        "candidate_b_role": CANDIDATE_B_ROLE,
        "candidate_a_basis_label": CANDIDATE_A_BASIS_LABEL,
        "candidate_b_basis_label": CANDIDATE_B_BASIS_LABEL,
        "basis_pair_scope": BASIS_PAIR_SCOPE,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        **_canonical_non_claims(),
        **marker_flags,
        "candidate_standing_operation_recorded": evaluated,
        "candidate_standing_check_performed": evaluated,
        "candidate_standing_result_recorded": evaluated,
        "candidate_standing_result": _operation_result_value(outcome),
        "candidate_a_standing_evaluated": evaluated,
        "candidate_b_standing_evaluated": evaluated,
        "candidate_a_standing_supported": supported,
        "candidate_b_standing_supported": supported,
        "candidate_standing_supported": supported,
        "candidate_standing_authorized": supported,
        "candidate_standing_created": supported,
        "candidate_a_standing_created": supported,
        "candidate_b_standing_created": supported,
    }
    return operation


def _operation_material(outcome: str, allowance_present: bool) -> dict[str, Any]:
    supported = outcome == OUTCOME_SUPPORTED
    evaluated = outcome in {OUTCOME_SUPPORTED, OUTCOME_NOT_SUPPORTED}
    candidate_distinct = allowance_present
    return {
        "candidate_a_standing_evaluation": {
            "candidate_record_id": CANDIDATE_A_RECORD_ID,
            "candidate_role": CANDIDATE_A_ROLE,
            "candidate_basis_id": CANDIDATE_A_BASIS_ID,
            "candidate_basis_label": CANDIDATE_A_BASIS_LABEL,
            "candidate_basis_scope": "Motion-side admissible variation",
            "candidate_record_distinct": candidate_distinct,
            "candidate_basis_separate": allowance_present,
            "candidate_basis_non_standing_at_emission": allowance_present,
            "candidate_standing_supported": supported,
            "candidate_standing_authorized": supported,
            "candidate_standing_created": supported,
            "descendant_body_created": False,
            "relation_created": False,
            "presence_established": False,
            "identity_created": False,
        },
        "candidate_b_standing_evaluation": {
            "candidate_record_id": CANDIDATE_B_RECORD_ID,
            "candidate_role": CANDIDATE_B_ROLE,
            "candidate_basis_id": CANDIDATE_B_BASIS_ID,
            "candidate_basis_label": CANDIDATE_B_BASIS_LABEL,
            "candidate_basis_scope": "Regulation-side admissibility bounds",
            "candidate_record_distinct": candidate_distinct,
            "candidate_basis_separate": allowance_present,
            "candidate_basis_non_standing_at_emission": allowance_present,
            "candidate_standing_supported": supported,
            "candidate_standing_authorized": supported,
            "candidate_standing_created": supported,
            "descendant_body_created": False,
            "relation_created": False,
            "presence_established": False,
            "identity_created": False,
        },
        "standing_pair_evaluation": {
            "both_candidate_standings_supported": supported,
            "both_candidate_standings_authorized": supported,
            "both_candidate_standings_created": supported,
            "candidate_records_remain_sibling": allowance_present,
            "candidate_record_non_hierarchy_preserved": allowance_present,
            "candidate_basis_non_hierarchy_preserved": allowance_present,
            "regulation_not_sovereign_over_motion": allowance_present,
            "motion_does_not_erase_regulation": allowance_present,
            "coupling_assigned": False,
            "coupling_created": False,
            "third_candidate_created": False,
            "third_model_admitted": False,
            "descendant_body_created": False,
            "relation_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
            "candidate_standing_evaluated": evaluated,
        },
    }


def _declared_basis_projection(request: Mapping[str, Any]) -> dict[str, Any]:
    fields = (
        "intent",
        *EXPECTED_REQUEST_VALUES.keys(),
        "candidate_standing_operation_spec_reference",
        *(item[0] for item in UPSTREAM_REQUIREMENTS),
        "candidate_standing_support_evidence_sufficient",
        *PROHIBITED_REQUEST_FLAGS.keys(),
    )
    projection = {field: request.get(field) for field in fields if field in request}
    declared = request.get("declared_non_claims")
    if isinstance(declared, Mapping):
        projection["declared_non_claims"] = {
            key: declared.get(key) for key in REQUIRED_FALSE_NON_CLAIMS
        }
    else:
        projection["declared_non_claims"] = type(declared).__name__
    return _sanitize(projection)


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("descendant_body_candidate_standing_operation")
    details = operation if isinstance(operation, Mapping) else {}
    checks = result.get("candidate_standing_operation_checks")
    records = checks if isinstance(checks, list) else []
    upstream = result.get("upstream_basis")
    basis = upstream if isinstance(upstream, Mapping) else {}
    result_detail = result.get("candidate_standing_result_detail")
    detail = result_detail if isinstance(result_detail, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "failed_check_count": sum(
            check.get("passed") is False for check in records if isinstance(check, Mapping)
        ),
        "passed_check_count": sum(
            check.get("passed") is True for check in records if isinstance(check, Mapping)
        ),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "operation_id": details.get("operation_id"),
        "operation_type": details.get("operation_type"),
        "operation_version": details.get("operation_version"),
        "operation_scope": details.get("operation_scope"),
        "prior_candidate_standing_boundary_type": details.get("prior_candidate_standing_boundary_type"),
        "prior_candidate_standing_boundary_outcome_required": details.get("prior_candidate_standing_boundary_outcome_required"),
        "prior_candidate_standing_boundary_result_required": details.get("prior_candidate_standing_boundary_result_required"),
        "prior_candidate_standing_operation_consideration_allowed_required": details.get("prior_candidate_standing_operation_consideration_allowed_required"),
        "candidate_a_record_id": details.get("candidate_a_record_id"),
        "candidate_b_record_id": details.get("candidate_b_record_id"),
        "candidate_a_role": details.get("candidate_a_role"),
        "candidate_b_role": details.get("candidate_b_role"),
        "candidate_a_basis_id": details.get("candidate_a_basis_id"),
        "candidate_b_basis_id": details.get("candidate_b_basis_id"),
        "candidate_a_basis_label": details.get("candidate_a_basis_label"),
        "candidate_b_basis_label": details.get("candidate_b_basis_label"),
        "basis_pair_scope": details.get("basis_pair_scope"),
        "candidate_standing_result": details.get("candidate_standing_result"),
        "candidate_standing_supported": details.get("candidate_standing_supported"),
        "candidate_standing_authorized": details.get("candidate_standing_authorized"),
        "candidate_standing_created": details.get("candidate_standing_created"),
        "candidate_a_standing_supported": details.get("candidate_a_standing_supported"),
        "candidate_b_standing_supported": details.get("candidate_b_standing_supported"),
        "candidate_a_standing_created": details.get("candidate_a_standing_created"),
        "candidate_b_standing_created": details.get("candidate_b_standing_created"),
        "selected_target_spec_path": basis.get("candidate_standing_operation_spec_reference"),
        "completed_candidate_standing_boundary_terminal_summary_path": basis.get("candidate_standing_boundary_terminal_summary_reference"),
        "completed_distinctness_support_recheck_terminal_summary_path": basis.get("distinctness_support_recheck_terminal_summary_reference"),
        "completed_successor_basis_emission_terminal_summary_path": basis.get("successor_basis_emission_terminal_summary_reference"),
        "missing_or_insufficient_boundary_allowance": detail.get("missing_or_insufficient_boundary_allowance", []),
        "not_supported_reasons": detail.get("not_supported_reasons", []),
    }
    for key in (*ALLOWED_TRUE_RECORDED_FIELDS, *REQUIRED_FALSE_NON_CLAIMS):
        summary[key] = details.get(key)
    for key, value in _marker_flags([item for item in records if isinstance(item, Mapping)]).items():
        summary[key] = details.get(key, value)
    return _sanitize(summary)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_boundary_allowance: list[str],
    not_supported_reasons: list[str],
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    marker_flags = _marker_flags(checks)
    operation = _operation_object(outcome, marker_flags)
    allowance_present = not missing_boundary_allowance
    result: dict[str, Any] = {
        "candidate_standing_operation_metadata": {
            "operation_id": OPERATION_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_candidate_standing_operation_basis": _declared_basis_projection(request),
        "upstream_basis": {
            "candidate_standing_operation_spec_reference": request.get("candidate_standing_operation_spec_reference"),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **marker_flags,
        },
        "descendant_body_candidate_standing_operation": operation,
        "candidate_standing_operation_material": _operation_material(outcome, allowance_present),
        "candidate_standing_operation_checks": checks,
        "candidate_standing_operation_statement": {
            "outcome": outcome,
            **{key: operation[key] for key in ALLOWED_TRUE_RECORDED_FIELDS},
            "candidate_standing_result": operation["candidate_standing_result"],
            "descendant_body_created": False,
            "relation_created": False,
            "runtime_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
            "result_level_non_claims_canonical_false": True,
        },
        "candidate_standing_operation_non_meaning": {
            "not_descendant_body_creation": True,
            "not_crossing": True,
            "not_relation": True,
            "not_runtime": True,
            "not_authority": True,
            "not_coupling": True,
            "not_presence": True,
            "not_identity": True,
            "not_follow_on": True,
        },
        "candidate_standing_result_detail": {
            "candidate_standing_result": operation["candidate_standing_result"],
            "missing_or_insufficient_boundary_allowance": list(missing_boundary_allowance),
            "not_supported_reasons": list(not_supported_reasons),
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "descendant_body_creation_boundary_requires_separate_bounded_step": True,
        },
        "blocked_routes": [
            "descendant-body creation, crossing, relation, runtime, authority, coupling, third model, presence, identity, repair, discovery, validation, and downstream authorization",
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
    result["candidate_standing_operation_summary"] = _build_summary(result)
    return _sanitize(result)


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    missing_boundary_allowance: list[str] | None = None,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        missing_boundary_allowance or [],
        [],
        code,
        reason,
    )


def build_declared_descendant_body_candidate_standing_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one explicit, no-discovery candidate-standing operation request."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **EXPECTED_REQUEST_VALUES,
        "candidate_standing_operation_spec_reference": DEFAULT_CANDIDATE_STANDING_OPERATION_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "candidate_standing_support_evidence_sufficient": True,
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in ALLOWED_TRUE_RECORDED_FIELDS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


def resolve_descendant_body_candidate_standing_operation_v0_min(
    declared_candidate_standing_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one candidate-standing operation without downstream conversion."""

    if declared_candidate_standing_operation is None:
        request = build_declared_descendant_body_candidate_standing_operation_v0_min_request()
    elif not isinstance(declared_candidate_standing_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_candidate_standing_operation).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_candidate_standing_operation))

    checks: list[dict[str, Any]] = []
    intent = request.get("intent")
    _add_check(
        checks,
        "intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "UNSUPPORTED_INTENT",
    )
    if intent == INTENT_BLOCK:
        return _blocked_result(request, checks, "EXPLICIT_BLOCK_REQUESTED", "explicit block intent requested")
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(request, checks, "UNSUPPORTED_INTENT", "intent is unsupported")

    _validate_exact_values(checks, request)
    _validate_request_posture(checks, request)
    _validate_target_spec(checks, request)
    missing_boundary_allowance = _validate_upstream(checks, request)

    non_upstream_failures = _failed_codes(checks, upstream=False)
    if non_upstream_failures:
        code = non_upstream_failures[0]
        return _blocked_result(
            request,
            checks,
            code,
            f"blocked by failed check {code}",
            missing_boundary_allowance,
        )

    allowance_codes = {
        "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_MARKER_MISSING",
        "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_MARKER_MISSING",
    }
    other_upstream_failures = [
        code for code in _failed_codes(checks, upstream=True) if code not in allowance_codes
    ]
    if other_upstream_failures:
        code = other_upstream_failures[0]
        return _blocked_result(
            request,
            checks,
            code,
            f"blocked by failed upstream check {code}",
            missing_boundary_allowance,
        )
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(
            request,
            OUTCOME_NOT_RECORDED,
            checks,
            missing_boundary_allowance,
            [],
        )
    if missing_boundary_allowance:
        return _build_result(
            request,
            OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
            checks,
            missing_boundary_allowance,
            [],
        )

    sufficient = request.get("candidate_standing_support_evidence_sufficient")
    _add_check(
        checks,
        "candidate-standing support evidence sufficient",
        sufficient is True,
        True,
        sufficient,
        "CANDIDATE_STANDING_NOT_SUPPORTED",
    )
    if sufficient is not True:
        return _build_result(
            request,
            OUTCOME_NOT_SUPPORTED,
            checks,
            [],
            ["candidate-standing support evidence is absent or insufficient"],
        )
    return _build_result(request, OUTCOME_SUPPORTED, checks, [], [])


def resolve_descendant_body_candidate_standing_operation_v0_min_from_path(
    declared_candidate_standing_operation_path: Path | str,
) -> dict[str, Any]:
    """Read one explicit JSON request object and resolve it."""

    path = Path(declared_candidate_standing_operation_path)
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
    return resolve_descendant_body_candidate_standing_operation_v0_min(request)


def build_descendant_body_candidate_standing_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return compact metadata for one bounded candidate-standing operation."""

    return _build_summary(result)


def write_descendant_body_candidate_standing_operation_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
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
            json.dump(
                _json_ready(_sanitize(result)),
                handle,
                ensure_ascii=True,
                indent=2,
                sort_keys=True,
            )
            handle.write("\n")
        return final_path
    except OSError as exc:
        raise DescendantBodyCandidateStandingOperationV0MinError(
            f"WRITE_REFUSED: {exc}"
        ) from exc
