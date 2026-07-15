"""Resolve one bounded descendant-body creation operation result.

The resolver creates descendant-body records only after the recorded boundary
allowance and candidate-standing basis are present. It does not create standing
descendants, crossing, relation, runtime, authority, coupling, presence,
identity, repair, scan, validation, or follow-on authorization.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCreationOperationV0MinError(Exception):
    """Raised when a bounded operation result cannot be written safely."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_creation_operation_v0_min"

OPERATION_ID = "descendant_body_creation_operation_001"
OPERATION_TYPE = "DESCENDANT_BODY_CREATION_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EVALUATE_DESCENDANT_BODY_CREATION_AFTER_BOUNDARY_ALLOWANCE_ONLY"
PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_TYPE = "DESCENDANT_BODY_CREATION_BOUNDARY"
PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_OUTCOME_REQUIRED = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED"
)
PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_RESULT_REQUIRED = (
    "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED"
)
PRIOR_DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED_REQUIRED = True
PRIOR_CANDIDATE_STANDING_REFERENCED_REQUIRED = True
PRIOR_CANDIDATE_A_STANDING_REFERENCED_REQUIRED = True
PRIOR_CANDIDATE_B_STANDING_REFERENCED_REQUIRED = True
PRIOR_CANDIDATE_STANDING_CREATED_REFERENCED_REQUIRED = True
PRIOR_DESCENDANT_BODY_CREATION_PERFORMED_REQUIRED = False
PRIOR_DESCENDANT_BODY_CREATED_REQUIRED = False
PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED = False
PRIOR_CROSSING_AUTHORIZED_REQUIRED = False
PRIOR_RELATION_CREATED_REQUIRED = False
PRIOR_COUPLING_CREATED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_IDENTITY_CREATED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = (
    "DESCENDANT_BODY_CREATION_OPERATION_THEN_FIRST_CROSSING_BOUNDARY_ONLY"
)

CANDIDATE_A_STANDING_SOURCE_ID = "descendant_body_basis_candidate_a_001"
CANDIDATE_B_STANDING_SOURCE_ID = "descendant_body_basis_candidate_b_001"
CANDIDATE_A_BASIS_ID = (
    "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis"
)
CANDIDATE_B_BASIS_ID = (
    "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis"
)
CANDIDATE_A_ROLE = "CANDIDATE_A"
CANDIDATE_B_ROLE = "CANDIDATE_B"
CANDIDATE_A_STANDING_LABEL = "CANDIDATE_A_STANDING"
CANDIDATE_B_STANDING_LABEL = "CANDIDATE_B_STANDING"
CANDIDATE_A_BASIS_LABEL = "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS"
CANDIDATE_B_BASIS_LABEL = "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
BASIS_PAIR_SCOPE = "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY"
DESCENDANT_BODY_A_ID = "descendant_body_a_001"
DESCENDANT_BODY_B_ID = "descendant_body_b_001"
DESCENDANT_BODY_PAIR_SCOPE = "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY"

OUTCOME_CREATED = "DESCENDANT_BODY_CREATION_OPERATION_CREATED"
OUTCOME_NOT_CREATED = "DESCENDANT_BODY_CREATION_OPERATION_NOT_CREATED"
OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE = (
    "DESCENDANT_BODY_CREATION_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE"
)
OUTCOME_BLOCKED = "DESCENDANT_BODY_CREATION_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CREATION_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_CREATED,
    OUTCOME_NOT_CREATED,
    OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CREATION_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CREATION_OPERATION"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CREATION_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_descendant_body_creation_operation_v0_min"
)
DETERMINISTIC_FILENAME = (
    "descendant_body_creation_operation_001__descendant_body_creation_operation_v0_min_result.json"
)

DEFAULT_DESCENDANT_BODY_CREATION_OPERATION_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CREATION_OPERATION_V0_MIN_SPEC.md"
)
DEFAULT_DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "descendant_body_creation_operation_recorded",
    "descendant_body_creation_evaluation_performed",
    "descendant_body_creation_result_recorded",
    "descendant_body_a_creation_evaluated",
    "descendant_body_b_creation_evaluated",
    "descendant_body_a_creation_supported",
    "descendant_body_b_creation_supported",
    "descendant_body_creation_supported",
    "descendant_body_creation_authorized",
    "descendant_body_creation_performed",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_created",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "descendant_body_creation_operation_recorded",
    "descendant_body_creation_evaluation_performed",
    "descendant_body_creation_result_recorded",
    "descendant_body_a_creation_evaluated",
    "descendant_body_b_creation_evaluated",
    "descendant_body_a_creation_supported",
    "descendant_body_b_creation_supported",
    "descendant_body_creation_supported",
    "descendant_body_creation_authorized",
    "descendant_body_creation_performed",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_created",
    "standing_descendant_created",
    "descendant_body_a_is_standing_descendant",
    "descendant_body_b_is_standing_descendant",
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
    "descendant_body_creation_boundary_overridden",
    "descendant_body_creation_boundary_bypassed",
    "candidate_standing_operation_overridden",
    "candidate_standing_operation_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_descendant_body_creation_operation_spec_to_descendant_body_creation_operation_completion",
    "direct_boundary_allowance_to_descendant_body_creation_without_operation",
    "direct_candidate_standing_to_descendant_body_creation_without_boundary_and_operation",
    "direct_descendant_body_creation_to_standing_descendant",
    "direct_descendant_body_creation_to_descendant_standing",
    "direct_descendant_body_creation_to_crossing",
    "direct_descendant_body_creation_to_relation",
    "direct_descendant_body_creation_to_runtime",
    "direct_descendant_body_creation_to_authority_currentness",
    "direct_descendant_body_creation_to_coupling_creation",
    "direct_descendant_body_creation_to_third_candidate_route",
    "direct_descendant_body_creation_to_third_model_route",
    "direct_descendant_body_creation_to_presence",
    "direct_descendant_body_creation_to_identity",
    "direct_descendant_body_creation_to_output_action",
    "direct_descendant_body_creation_to_follow_on_work",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "REQUEST_PATH_UNREADABLE",
    "REQUEST_JSON_INVALID",
    "UNSUPPORTED_INTENT",
    "REQUEST_VALUE_MISMATCH",
    "DESCENDANT_BODY_CREATION_OPERATION_SPEC_REFERENCE_MISSING",
    "DESCENDANT_BODY_CREATION_OPERATION_SPEC_MARKER_MISSING",
    "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "BOUNDARY_ALLOWANCE_MISSING_OR_INSUFFICIENT",
    "DESCENDANT_BODY_CREATION_NOT_SUPPORTED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "RESULT_POSTURE_PRECLAIMED",
    "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "PROHIBITED_CROSSING_REQUESTED",
    "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_standing_descendant_creation": "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "request_descendant_standing": "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "request_descendant_standing_check": "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "request_crossing_authorization": "PROHIBITED_CROSSING_REQUESTED",
    "request_first_crossing_authorization": "PROHIBITED_CROSSING_REQUESTED",
    "request_relation_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
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
    "descendant_body_creation_operation_id": OPERATION_ID,
    "descendant_body_creation_operation_type": OPERATION_TYPE,
    "descendant_body_creation_operation_version": OPERATION_VERSION,
    "descendant_body_creation_operation_scope": OPERATION_SCOPE,
    "prior_descendant_body_creation_boundary_type": (
        PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_TYPE
    ),
    "prior_descendant_body_creation_boundary_outcome_required": (
        PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_OUTCOME_REQUIRED
    ),
    "prior_descendant_body_creation_boundary_result_required": (
        PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_RESULT_REQUIRED
    ),
    "prior_descendant_body_creation_operation_consideration_allowed_required": (
        PRIOR_DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED_REQUIRED
    ),
    "prior_candidate_standing_referenced_required": (
        PRIOR_CANDIDATE_STANDING_REFERENCED_REQUIRED
    ),
    "prior_candidate_a_standing_referenced_required": (
        PRIOR_CANDIDATE_A_STANDING_REFERENCED_REQUIRED
    ),
    "prior_candidate_b_standing_referenced_required": (
        PRIOR_CANDIDATE_B_STANDING_REFERENCED_REQUIRED
    ),
    "prior_candidate_standing_created_referenced_required": (
        PRIOR_CANDIDATE_STANDING_CREATED_REFERENCED_REQUIRED
    ),
    "prior_descendant_body_creation_performed_required": (
        PRIOR_DESCENDANT_BODY_CREATION_PERFORMED_REQUIRED
    ),
    "prior_descendant_body_created_required": PRIOR_DESCENDANT_BODY_CREATED_REQUIRED,
    "prior_standing_descendant_created_required": (
        PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED
    ),
    "prior_crossing_authorized_required": PRIOR_CROSSING_AUTHORIZED_REQUIRED,
    "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
    "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
    "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
    "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
    "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    "candidate_a_standing_source_id": CANDIDATE_A_STANDING_SOURCE_ID,
    "candidate_b_standing_source_id": CANDIDATE_B_STANDING_SOURCE_ID,
    "candidate_a_basis_id": CANDIDATE_A_BASIS_ID,
    "candidate_b_basis_id": CANDIDATE_B_BASIS_ID,
    "candidate_a_role": CANDIDATE_A_ROLE,
    "candidate_b_role": CANDIDATE_B_ROLE,
    "candidate_a_standing_label": CANDIDATE_A_STANDING_LABEL,
    "candidate_b_standing_label": CANDIDATE_B_STANDING_LABEL,
    "candidate_a_basis_label": CANDIDATE_A_BASIS_LABEL,
    "candidate_b_basis_label": CANDIDATE_B_BASIS_LABEL,
    "basis_pair_scope": BASIS_PAIR_SCOPE,
    "descendant_body_a_id": DESCENDANT_BODY_A_ID,
    "descendant_body_b_id": DESCENDANT_BODY_B_ID,
    "descendant_body_pair_scope": DESCENDANT_BODY_PAIR_SCOPE,
    "descendant_body_creation_result": "NOT_EVALUATED",
}

TARGET_SPEC_MARKER_CLASSES = (
    (
        "operation_identity",
        ((
            "Descendant Body Creation Operation V0 Minimum Specification",
            OPERATION_TYPE,
            OPERATION_ID,
            OPERATION_SCOPE,
        ),),
    ),
    (
        "boundary_allowance",
        ((
            PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_OUTCOME_REQUIRED,
            PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_RESULT_REQUIRED,
            "descendant_body_creation_operation_consideration_allowed = true",
            "candidate_standing_referenced = true",
            "candidate_a_standing_referenced = true",
            "candidate_b_standing_referenced = true",
            "candidate_standing_created_referenced = true",
            "descendant_body_creation_performed = false",
            "descendant_body_created = false",
            "standing_descendant_created = false",
            "crossing_authorized = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ),),
    ),
    (
        "candidate_standing_operation",
        ((
            "CANDIDATE_STANDING_SUPPORTED",
            "candidate_standing_supported = true",
            "candidate_standing_authorized = true",
            "candidate_standing_created = true",
            "candidate_a_standing_created = true",
            "candidate_b_standing_created = true",
            "candidate standing is not descendant-body creation",
            "candidate standing is not relation",
            "candidate standing is not presence",
            "candidate standing is not identity",
        ),),
    ),
    (
        "descendant_body_material",
        ((
            "descendant_body_a_creation_evaluation",
            "descendant_body_b_creation_evaluation",
            "descendant_body_pair_evaluation",
            DESCENDANT_BODY_A_ID,
            DESCENDANT_BODY_B_ID,
            DESCENDANT_BODY_PAIR_SCOPE,
            "DESCENDANT_BODY_CREATION_SUPPORTED",
            "descendant_body_creation_supported = true",
            "descendant_body_creation_authorized = true",
            "descendant_body_creation_performed = true",
            "descendant_body_a_created = true",
            "descendant_body_b_created = true",
            "descendant_body_created = true",
        ),),
    ),
    (
        "descendant_body_non_conversion",
        ((
            "Descendant-body creation is not standing descendant creation",
            "Descendant body is not standing descendant",
            "Descendant body is not descendant standing",
            "Descendant body is not crossing",
            "Descendant body is not relation",
            "Descendant body is not runtime",
            "Descendant body is not currentness",
            "Descendant body is not authority",
            "Descendant body is not coupling",
            "Descendant body is not presence",
            "Descendant body is not identity",
            "Descendant body is not follow-on authorization",
            "Descendant body is not relation participation",
            "Descendant body is not presence-bearing",
            "Descendant body is not identity-bearing",
        ),),
    ),
    (
        "sibling_non_hierarchy",
        (
            (
                "Descendant Body A and Descendant Body B remain sibling records",
                "neither descendant body ranks above the other",
                "Candidate A and Candidate B remain sibling candidate standings",
                "neither candidate standing ranks above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
                "coupling remains unassigned",
            ),
            (
                "Descendant Body A and Descendant Body B remain sibling records",
                "neither ranks above the other",
                "Candidate A and Candidate B remain sibling candidate standings",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
                "coupling remains unassigned",
            ),
        ),
    ),
    (
        "permitted_route",
        (
            (
                ADMISSIBLE_FUTURE_ROUTE,
                "Only after a future descendant-body creation operation records DESCENDANT_BODY_CREATION_SUPPORTED may a separately bounded first-crossing boundary be considered",
                "No later operation is authorized by this operation specification alone",
            ),
            (
                ADMISSIBLE_FUTURE_ROUTE,
                "Only after a future descendant-body creation operation records DESCENDANT_BODY_CREATION_SUPPORTED may a separately bounded first-crossing boundary be considered",
                "No later operation is authorized by this specification alone",
            ),
        ),
    ),
    (
        "contaminated_lineage",
        (
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
        ),
    ),
    (
        "blocked_routes",
        ((
            "direct descendant-body creation operation spec to descendant-body creation operation completion",
            "direct boundary allowance to descendant-body creation without operation",
            "direct candidate standing to descendant-body creation without boundary and operation",
            "direct descendant-body creation to standing descendant",
            "direct descendant-body creation to descendant standing",
            "direct descendant-body creation to crossing",
            "direct descendant-body creation to relation",
            "direct descendant-body creation to runtime",
            "direct descendant-body creation to authority/currentness",
            "direct descendant-body creation to coupling creation",
            "direct descendant-body creation to third-candidate route",
            "direct descendant-body creation to third-model route",
            "direct descendant-body creation to presence",
            "direct descendant-body creation to identity",
            "direct descendant-body creation to output/action",
            "direct descendant-body creation to follow-on work",
            "repository scan route",
            "file discovery route",
            "affected-file repair route",
            "prior unsupported-claim validation route",
        ),),
    ),
    (
        "closing_lock",
        ((
            "This operation spec defines only a future descendant-body creation operation shape",
            "It does not perform descendant-body creation",
            "Descendant-body creation operation spec is not descendant-body creation operation result",
            "Descendant-body creation operation permission is not descendant-body creation completion",
            "Descendant-body creation is not standing descendant creation",
            "Descendant body is not standing descendant",
            "Descendant body is not crossing",
            "Descendant body is not relation",
            "Descendant body is not presence",
            "Descendant body is not identity",
            "Descendant-body creation, if later supported, remains prior to any first-crossing boundary",
            "Open means not scheduled, not authorized, and not executed",
        ),),
    ),
)

UPSTREAM_REQUIREMENTS = (
    (
        "descendant_body_creation_boundary_terminal_summary_reference",
        DEFAULT_DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 153",
            PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_RESULT_REQUIRED,
            "descendant_body_creation_operation_consideration_allowed = true",
            "candidate_standing_referenced = true",
            "candidate_a_standing_referenced = true",
            "candidate_b_standing_referenced = true",
            "candidate_standing_created_referenced = true",
            "descendant_body_creation_performed = false",
            "descendant_body_created = false",
            "standing_descendant_created = false",
            "crossing_authorized = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ),),
        "completed_descendant_body_creation_boundary_terminal_summary_markers_present",
        True,
    ),
    (
        "candidate_standing_operation_terminal_summary_reference",
        DEFAULT_CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            "CANDIDATE_STANDING_SUPPORTED",
            "candidate_standing_supported = true",
            "candidate_standing_authorized = true",
            "candidate_standing_created = true",
            "candidate_a_standing_created = true",
            "candidate_b_standing_created = true",
            "Candidate standing is not descendant-body creation",
            "Candidate standing is not relation",
            "Candidate standing is not presence",
            "Candidate standing is not identity",
        ),),
        "completed_candidate_standing_operation_terminal_summary_markers_present",
        True,
    ),
    (
        "candidate_standing_boundary_terminal_summary_reference",
        DEFAULT_CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        (("CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED",),),
        "completed_candidate_standing_boundary_terminal_summary_markers_present",
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
    "first-crossing boundary, if separately bounded after descendant-body creation support",
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


def _json_ready(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value


def _sanitize(value: Any, key: str = "") -> Any:
    lowered_key = key.casefold()
    sensitive_keys = {
        "raw_body",
        "raw_state_body",
        "raw_request_payload",
        "hidden_repo_state",
        "hidden_repo_content",
        "hidden_state_payload",
    }
    if lowered_key in sensitive_keys:
        return "[redacted]"
    if isinstance(value, str):
        if any(token in value for token in ("RAW_", "HIDDEN_REPO_", "MUST_NOT_RETURN")):
            return "[redacted]"
        return value
    if isinstance(value, Mapping):
        return {str(name): _sanitize(item, str(name)) for name, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, key) for item in value]
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


def _path_from_reference(reference: Any) -> Path | None:
    if not isinstance(reference, (str, Path)) or not str(reference):
        return None
    path = Path(reference)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_text(reference: Any) -> str | None:
    path = _path_from_reference(reference)
    if path is None or not path.is_file():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return None


def _markers_present(text: str | None, variants: tuple[tuple[str, ...], ...]) -> bool:
    if text is None:
        return False
    normalized = text.casefold()
    return any(all(marker.casefold() in normalized for marker in markers) for markers in variants)


def _marker_flags(checks: list[Mapping[str, Any]]) -> dict[str, bool]:
    flags: dict[str, bool] = {}
    for check in checks:
        name = check.get("check_name")
        if isinstance(name, str) and name.endswith("markers present"):
            flags[name.replace(" ", "_")] = check.get("passed") is True
    return flags


def _failed_codes(checks: list[Mapping[str, Any]]) -> list[str]:
    return [
        str(check["block_code"])
        for check in checks
        if check.get("passed") is False and isinstance(check.get("block_code"), str)
    ]


def _validate_exact_values(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    for field, expected in EXPECTED_REQUEST_VALUES.items():
        actual = request.get(field)
        _add_check(
            checks,
            f"declared {field}",
            actual == expected,
            expected,
            actual,
            "REQUEST_VALUE_MISMATCH",
        )


def _validate_declared_non_claims(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> None:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        _add_check(
            checks,
            "declared non-claims mapping",
            False,
            "mapping with canonical false posture",
            type(declared).__name__,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return
    for field in REQUIRED_FALSE_NON_CLAIMS:
        value = declared.get(field)
        _add_check(
            checks,
            f"declared non-claim {field}",
            value is False,
            False,
            value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _request_posture_failure(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> str | None:
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        value = request.get(field)
        _add_check(checks, f"prohibited request flag {field}", value is not True, False, value, code)
        if value is True:
            return code
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        value = request.get(field)
        _add_check(
            checks,
            f"result posture not pre-claimed {field}",
            value is not True,
            False,
            value,
            "RESULT_POSTURE_PRECLAIMED",
        )
        if value is True:
            return "RESULT_POSTURE_PRECLAIMED"
    for field in REQUIRED_FALSE_NON_CLAIMS:
        if field in ALLOWED_TRUE_RECORDED_FIELDS:
            continue
        if field not in request:
            continue
        value = request.get(field)
        _add_check(
            checks,
            f"top-level false posture {field}",
            value is False,
            False,
            value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        if value is not False:
            return "NON_CLAIM_MISSING_OR_FLIPPED"
    return None


def _validate_target_spec(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> str | None:
    reference = request.get("descendant_body_creation_operation_spec_reference")
    text = _read_text(reference)
    _add_check(
        checks,
        "descendant-body creation operation specification reference readable",
        text is not None,
        "readable Markdown file",
        reference,
        "DESCENDANT_BODY_CREATION_OPERATION_SPEC_REFERENCE_MISSING",
    )
    if text is None:
        return "DESCENDANT_BODY_CREATION_OPERATION_SPEC_REFERENCE_MISSING"
    failure: str | None = None
    for class_name, variants in TARGET_SPEC_MARKER_CLASSES:
        present = _markers_present(text, variants)
        _add_check(
            checks,
            f"descendant-body creation operation specification {class_name} markers present",
            present,
            "posture marker class present",
            present,
            "DESCENDANT_BODY_CREATION_OPERATION_SPEC_MARKER_MISSING",
        )
        if not present and failure is None:
            failure = "DESCENDANT_BODY_CREATION_OPERATION_SPEC_MARKER_MISSING"
    return failure


def _validate_upstream(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> tuple[list[str], str | None]:
    missing_allowance: list[str] = []
    blocking_failure: str | None = None
    for field, _, missing_code, marker_code, variants, flag, allowance_class in UPSTREAM_REQUIREMENTS:
        reference = request.get(field)
        text = _read_text(reference)
        readable = text is not None
        _add_check(
            checks,
            f"{field} readable",
            readable,
            "readable terminal summary",
            reference,
            missing_code,
            True,
        )
        if not readable:
            if allowance_class:
                missing_allowance.append(field)
            elif blocking_failure is None:
                blocking_failure = missing_code
            continue
        present = _markers_present(text, variants)
        _add_check(
            checks,
            f"{flag.replace('_', ' ')}",
            present,
            "required terminal-summary posture markers",
            present,
            marker_code,
            True,
        )
        if not present:
            if allowance_class:
                missing_allowance.append(field)
            elif blocking_failure is None:
                blocking_failure = marker_code
    return missing_allowance, blocking_failure


def _support_is_available(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> bool:
    value = request.get("descendant_body_creation_support_evidence_present")
    available = value is True
    _add_check(
        checks,
        "descendant-body creation support evidence present",
        available,
        True,
        value,
        "DESCENDANT_BODY_CREATION_NOT_SUPPORTED",
    )
    return available


def _operation_object(outcome: str, marker_flags: Mapping[str, bool]) -> dict[str, Any]:
    created = outcome == OUTCOME_CREATED
    not_created = outcome == OUTCOME_NOT_CREATED
    requires_allowance = outcome == OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "descendant_body_creation_operation_id": OPERATION_ID,
        "descendant_body_creation_operation_type": OPERATION_TYPE,
        "descendant_body_creation_operation_version": OPERATION_VERSION,
        "descendant_body_creation_operation_scope": OPERATION_SCOPE,
        "prior_descendant_body_creation_boundary_type": PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_TYPE,
        "prior_descendant_body_creation_boundary_outcome_required": PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_OUTCOME_REQUIRED,
        "prior_descendant_body_creation_boundary_result_required": PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_RESULT_REQUIRED,
        "prior_descendant_body_creation_operation_consideration_allowed_required": PRIOR_DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED_REQUIRED,
        "prior_candidate_standing_referenced_required": PRIOR_CANDIDATE_STANDING_REFERENCED_REQUIRED,
        "prior_candidate_a_standing_referenced_required": PRIOR_CANDIDATE_A_STANDING_REFERENCED_REQUIRED,
        "prior_candidate_b_standing_referenced_required": PRIOR_CANDIDATE_B_STANDING_REFERENCED_REQUIRED,
        "prior_candidate_standing_created_referenced_required": PRIOR_CANDIDATE_STANDING_CREATED_REFERENCED_REQUIRED,
        "prior_descendant_body_creation_performed_required": PRIOR_DESCENDANT_BODY_CREATION_PERFORMED_REQUIRED,
        "prior_descendant_body_created_required": PRIOR_DESCENDANT_BODY_CREATED_REQUIRED,
        "prior_standing_descendant_created_required": PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED,
        "prior_crossing_authorized_required": PRIOR_CROSSING_AUTHORIZED_REQUIRED,
        "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
        "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
        "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
        "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
        "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "candidate_a_standing_source_id": CANDIDATE_A_STANDING_SOURCE_ID,
        "candidate_b_standing_source_id": CANDIDATE_B_STANDING_SOURCE_ID,
        "candidate_a_basis_id": CANDIDATE_A_BASIS_ID,
        "candidate_b_basis_id": CANDIDATE_B_BASIS_ID,
        "candidate_a_role": CANDIDATE_A_ROLE,
        "candidate_b_role": CANDIDATE_B_ROLE,
        "candidate_a_standing_label": CANDIDATE_A_STANDING_LABEL,
        "candidate_b_standing_label": CANDIDATE_B_STANDING_LABEL,
        "candidate_a_basis_label": CANDIDATE_A_BASIS_LABEL,
        "candidate_b_basis_label": CANDIDATE_B_BASIS_LABEL,
        "basis_pair_scope": BASIS_PAIR_SCOPE,
        "descendant_body_a_id": DESCENDANT_BODY_A_ID,
        "descendant_body_b_id": DESCENDANT_BODY_B_ID,
        "descendant_body_pair_scope": DESCENDANT_BODY_PAIR_SCOPE,
        "descendant_body_creation_result": (
            "DESCENDANT_BODY_CREATION_SUPPORTED"
            if created
            else "DESCENDANT_BODY_CREATION_NOT_SUPPORTED"
            if not_created
            else "REQUIRES_BOUNDARY_ALLOWANCE"
            if requires_allowance
            else "NOT_EVALUATED"
        ),
    }
    operation.update({field: False for field in REQUIRED_FALSE_NON_CLAIMS})
    if created:
        operation.update({field: True for field in ALLOWED_TRUE_RECORDED_FIELDS})
    operation.update(marker_flags)
    return operation


def _operation_material(outcome: str) -> dict[str, Any]:
    created = outcome == OUTCOME_CREATED
    evaluation_a = {
        "descendant_body_id": DESCENDANT_BODY_A_ID,
        "candidate_standing_source_id": CANDIDATE_A_STANDING_SOURCE_ID,
        "candidate_role": CANDIDATE_A_ROLE,
        "candidate_standing_label": CANDIDATE_A_STANDING_LABEL,
        "candidate_basis_id": CANDIDATE_A_BASIS_ID,
        "candidate_basis_label": CANDIDATE_A_BASIS_LABEL,
        "candidate_basis_scope": "Motion-side admissible variation",
        "candidate_standing_created": created,
        "candidate_standing_is_descendant_body": False,
        "descendant_body_creation_supported": created,
        "descendant_body_creation_authorized": created,
        "descendant_body_created": created,
        "standing_descendant_created": False,
        "descendant_body_is_standing_descendant": False,
        "crossing_authorized": False,
        "relation_created": False,
        "presence_established": False,
        "identity_created": False,
    }
    evaluation_b = {
        "descendant_body_id": DESCENDANT_BODY_B_ID,
        "candidate_standing_source_id": CANDIDATE_B_STANDING_SOURCE_ID,
        "candidate_role": CANDIDATE_B_ROLE,
        "candidate_standing_label": CANDIDATE_B_STANDING_LABEL,
        "candidate_basis_id": CANDIDATE_B_BASIS_ID,
        "candidate_basis_label": CANDIDATE_B_BASIS_LABEL,
        "candidate_basis_scope": "Regulation-side admissibility bounds",
        "candidate_standing_created": created,
        "candidate_standing_is_descendant_body": False,
        "descendant_body_creation_supported": created,
        "descendant_body_creation_authorized": created,
        "descendant_body_created": created,
        "standing_descendant_created": False,
        "descendant_body_is_standing_descendant": False,
        "crossing_authorized": False,
        "relation_created": False,
        "presence_established": False,
        "identity_created": False,
    }
    pair = {
        "both_descendant_body_creations_supported": created,
        "both_descendant_body_creations_authorized": created,
        "both_descendant_bodies_created": created,
        "descendant_body_a_created": created,
        "descendant_body_b_created": created,
        "descendant_body_created": created,
        "descendant_bodies_remain_sibling": created,
        "descendant_body_non_hierarchy_preserved": created,
        "candidate_standing_non_hierarchy_preserved": created,
        "candidate_basis_non_hierarchy_preserved": created,
        "regulation_not_sovereign_over_motion": created,
        "motion_does_not_erase_regulation": created,
        "standing_descendant_created": False,
        "descendant_standing_check_performed": False,
        "crossing_authorized": False,
        "first_crossing_authorized": False,
        "coupling_assigned": False,
        "coupling_created": False,
        "third_candidate_created": False,
        "third_model_admitted": False,
        "relation_created": False,
        "presence_established": False,
        "identity_created": False,
        "follow_on_authorized": False,
    }
    return {
        "descendant_body_a_creation_evaluation": evaluation_a,
        "descendant_body_b_creation_evaluation": evaluation_b,
        "descendant_body_pair_evaluation": pair,
    }


def _declared_basis_projection(request: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "intent",
        *EXPECTED_REQUEST_VALUES,
        "descendant_body_creation_operation_spec_reference",
        *(item[0] for item in UPSTREAM_REQUIREMENTS),
    )
    return {key: _sanitize(request.get(key), key) for key in keys}


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("descendant_body_creation_operation")
    basis = result.get("declared_descendant_body_creation_operation_basis")
    checks = result.get("descendant_body_creation_operation_checks")
    detail = result.get("descendant_body_creation_result_detail")
    operation_map = operation if isinstance(operation, Mapping) else {}
    basis_map = basis if isinstance(basis, Mapping) else {}
    detail_map = detail if isinstance(detail, Mapping) else {}
    records = checks if isinstance(checks, list) else []
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "failed_check_count": sum(
            isinstance(item, Mapping) and item.get("passed") is False for item in records
        ),
        "passed_check_count": sum(
            isinstance(item, Mapping) and item.get("passed") is True for item in records
        ),
        "result_version": result.get("result_version"),
        "resolver_module": result.get("resolver_module"),
        "selected_target_spec_path": basis_map.get(
            "descendant_body_creation_operation_spec_reference"
        ),
        "completed_descendant_body_creation_boundary_terminal_summary_path": basis_map.get(
            "descendant_body_creation_boundary_terminal_summary_reference"
        ),
        "completed_candidate_standing_operation_terminal_summary_path": basis_map.get(
            "candidate_standing_operation_terminal_summary_reference"
        ),
        "missing_or_insufficient_boundary_allowance": list(
            detail_map.get("missing_or_insufficient_boundary_allowance", [])
        ),
        "not_created_reasons": list(detail_map.get("not_created_reasons", [])),
    }
    summary.update({key: operation_map.get(key) for key in EXPECTED_REQUEST_VALUES})
    summary.update(
        {
            key: operation_map.get(key)
            for key in (
                "descendant_body_creation_result",
                "descendant_body_creation_supported",
                "descendant_body_creation_authorized",
                "descendant_body_creation_performed",
                "descendant_body_a_created",
                "descendant_body_b_created",
                "descendant_body_created",
                "standing_descendant_created",
                "descendant_standing_check_performed",
                "crossing_authorized",
                "relation_created",
                "runtime_created",
                "coupling_created",
                "presence_established",
                "identity_created",
                "follow_on_authorized",
            )
        }
    )
    for field in REQUIRED_FALSE_NON_CLAIMS:
        summary[field] = operation_map.get(field)
    summary.update(_marker_flags([item for item in records if isinstance(item, Mapping)]))
    return _sanitize(summary)


def build_descendant_body_creation_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build the compact, JSON-safe summary for one operation result."""

    return _build_summary(result)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_allowance: list[str] | None = None,
    not_created_reasons: list[str] | None = None,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    marker_flags = _marker_flags(checks)
    operation = _operation_object(outcome, marker_flags)
    result: dict[str, Any] = {
        "descendant_body_creation_operation_metadata": {
            "operation_id": OPERATION_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_descendant_body_creation_operation_basis": _declared_basis_projection(request),
        "upstream_basis": {
            "descendant_body_creation_operation_spec_reference": request.get(
                "descendant_body_creation_operation_spec_reference"
            ),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **marker_flags,
        },
        "descendant_body_creation_operation": operation,
        "descendant_body_creation_operation_material": _operation_material(outcome),
        "descendant_body_creation_operation_checks": checks,
        "descendant_body_creation_operation_statement": {
            "outcome": outcome,
            **{field: operation.get(field) for field in ALLOWED_TRUE_RECORDED_FIELDS},
            "descendant_body_creation_result": operation[
                "descendant_body_creation_result"
            ],
            "standing_descendant_created": False,
            "crossing_authorized": False,
            "relation_created": False,
            "runtime_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
            "result_level_non_claims_canonical_false": True,
        },
        "descendant_body_creation_operation_non_meaning": {
            "not_standing_descendant_creation": True,
            "not_descendant_standing": True,
            "not_crossing": True,
            "not_relation": True,
            "not_runtime": True,
            "not_authority": True,
            "not_coupling": True,
            "not_presence": True,
            "not_identity": True,
            "not_follow_on": True,
        },
        "descendant_body_creation_result_detail": {
            "descendant_body_creation_result": operation[
                "descendant_body_creation_result"
            ],
            "missing_or_insufficient_boundary_allowance": list(missing_allowance or []),
            "not_created_reasons": list(not_created_reasons or []),
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "first_crossing_boundary_requires_separate_bounded_step": True,
        },
        "blocked_routes": [
            "standing descendant, descendant standing, crossing, relation, runtime, authority, coupling, third model, presence, identity, repair, discovery, validation, and downstream authorization",
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
    result["descendant_body_creation_operation_summary"] = _build_summary(result)
    return _sanitize(result)


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    missing_allowance: list[str] | None = None,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        missing_allowance=missing_allowance,
        block_code=code,
        block_reason=reason,
    )


def build_declared_descendant_body_creation_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one explicit request without repository discovery."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **EXPECTED_REQUEST_VALUES,
        "descendant_body_creation_support_evidence_present": True,
        "descendant_body_creation_operation_spec_reference": (
            DEFAULT_DESCENDANT_BODY_CREATION_OPERATION_SPEC_REFERENCE
        ),
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in REQUIRED_FALSE_NON_CLAIMS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


def resolve_descendant_body_creation_operation_v0_min(
    declared_descendant_body_creation_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one creation result after bounded boundary allowance only."""

    if declared_descendant_body_creation_operation is None:
        request = build_declared_descendant_body_creation_operation_v0_min_request()
    elif not isinstance(declared_descendant_body_creation_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_descendant_body_creation_operation).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_descendant_body_creation_operation))

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
    request_failure = _request_posture_failure(checks, request)
    _validate_declared_non_claims(checks, request)
    failed = _failed_codes(checks)
    if request_failure:
        return _blocked_result(request, checks, request_failure, "request asks for prohibited posture")
    if failed:
        code = failed[0]
        return _blocked_result(request, checks, code, f"blocked by failed check {code}")

    target_failure = _validate_target_spec(checks, request)
    if target_failure:
        return _blocked_result(request, checks, target_failure, "target operation specification is insufficient")

    missing_allowance, upstream_failure = _validate_upstream(checks, request)
    if upstream_failure:
        return _blocked_result(
            request,
            checks,
            upstream_failure,
            "required non-boundary upstream summary is insufficient",
            missing_allowance,
        )
    if missing_allowance:
        return _build_result(
            request,
            OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
            checks,
            missing_allowance=missing_allowance,
        )

    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks)

    if not _support_is_available(checks, request):
        return _build_result(
            request,
            OUTCOME_NOT_CREATED,
            checks,
            not_created_reasons=["descendant-body creation support evidence is insufficient"],
        )
    return _build_result(request, OUTCOME_CREATED, checks)


def resolve_descendant_body_creation_operation_v0_min_from_path(
    declared_descendant_body_creation_operation_path: Path | str,
) -> dict[str, Any]:
    """Resolve one explicit JSON request path without discovery."""

    path = Path(declared_descendant_body_creation_operation_path)
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request path readable",
            False,
            "readable JSON request",
            str(path),
            "REQUEST_PATH_UNREADABLE",
        )
        return _blocked_result({}, checks, "REQUEST_PATH_UNREADABLE", "request path is unreadable")
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        checks = []
        _add_check(
            checks,
            "request JSON parseable",
            False,
            "JSON object",
            "invalid JSON",
            "REQUEST_JSON_INVALID",
        )
        return _blocked_result({}, checks, "REQUEST_JSON_INVALID", "request JSON is invalid")
    return resolve_descendant_body_creation_operation_v0_min(payload)


def _next_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise DescendantBodyCreationOperationV0MinError("no deterministic output suffix available")


def write_descendant_body_creation_operation_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write one JSON-safe result without overwriting a prior artifact."""

    if not isinstance(result, Mapping):
        raise DescendantBodyCreationOperationV0MinError("WRITE_REFUSED: result is not a mapping")
    if output_path is None:
        destination = REPO_ROOT / OUTPUT_ROOT / DETERMINISTIC_FILENAME
    else:
        candidate = Path(output_path)
        destination = candidate if candidate.is_absolute() else REPO_ROOT / candidate
    if destination.exists() and destination.is_dir():
        raise DescendantBodyCreationOperationV0MinError("WRITE_REFUSED: destination is a directory")
    destination = _next_output_path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        serialized = json.dumps(_json_ready(_sanitize(dict(result))), indent=2, sort_keys=True)
        destination.write_text(serialized + "\n", encoding="utf-8")
    except (OSError, TypeError, ValueError) as error:
        raise DescendantBodyCreationOperationV0MinError(
            f"WRITE_REFUSED: {type(error).__name__}"
        ) from error
    return destination
