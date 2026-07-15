"""Resolve one bounded presence-boundary result.

The resolver may allow only future presence-operation consideration after a
completed relation-lapse operation.  It never establishes presence, creates
identity or coupling, changes relation, repairs lineage, scans, or authorizes
downstream work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class PresenceBoundaryV0MinError(Exception):
    """Raised when a presence-boundary result cannot be written."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_presence_boundary_v0_min"

BOUNDARY_ID = "presence_boundary_001"
BOUNDARY_TYPE = "PRESENCE_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = "CONSIDER_PRESENCE_AFTER_RELATION_LAPSE_OPERATION_ONLY"

PRIOR_RELATION_LAPSE_OPERATION_TYPE = "RELATION_LAPSE_OPERATION"
PRIOR_RELATION_LAPSE_OPERATION_OUTCOME_REQUIRED = "RELATION_LAPSE_OPERATION_RECORDED"
PRIOR_RELATION_LAPSE_RESULT_REQUIRED = "RELATION_LAPSE_SUPPORTED"
PRIOR_RELATION_LAPSE_SUPPORTED_REQUIRED = True
PRIOR_RELATION_LAPSE_AUTHORIZED_REQUIRED = True
PRIOR_RELATION_LAPSE_PERFORMED_REQUIRED = True
PRIOR_RELATION_LAPSE_RECORDED_REQUIRED = True
PRIOR_RELATION_RECORD_CONFIRMED_AS_HISTORICAL_ONLY_REQUIRED = True
PRIOR_RELATION_LAPSE_IS_PUNISHMENT_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_DISSOLUTION_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_ERASURE_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_TEARDOWN_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_LIVING_RELATION_STATE_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_PRESENCE_BOUNDARY_AUTHORIZATION_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_PRESENCE_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_IDENTITY_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_COUPLING_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_FIELD_MACHINERY_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_RUNTIME_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_CURRENTNESS_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_AUTHORITY_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_FOLLOW_ON_AUTHORIZATION_REQUIRED = False
PRIOR_RELATION_LAPSE_IS_FOLLOW_ON_WORK_REQUIRED = False
PRIOR_RELATION_RECORD_IS_LIVING_RELATION_STATE_REQUIRED = False
PRIOR_LIVING_RELATION_STATE_CREATED_REQUIRED = False
PRIOR_LIVING_RELATION_STATE_LAPSED_REQUIRED = False
PRIOR_LIVING_RELATION_STATE_DISSOLVED_REQUIRED = False
PRIOR_RELATION_DISSOLUTION_AUTHORIZED_REQUIRED = False
PRIOR_RELATION_DISSOLUTION_PERFORMED_REQUIRED = False
PRIOR_RELATION_REVERSED_REQUIRED = False
PRIOR_RELATION_TERMINATED_REQUIRED = False
PRIOR_RELATION_ERASED_REQUIRED = False
PRIOR_RELATION_MUTATED_REQUIRED = False
PRIOR_RELATION_INVALIDATED_REQUIRED = False
PRIOR_RELATION_PUNISHED_REQUIRED = False
PRIOR_RELATION_TEARDOWN_CREATED_REQUIRED = False
PRIOR_HISTORICAL_RECEIPT_PRESERVATION_AUTHORIZED_REQUIRED = False
PRIOR_HISTORICAL_RECEIPT_PRESERVED_REQUIRED = False
PRIOR_PRESENCE_BOUNDARY_AUTHORIZED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_IDENTITY_CREATED_REQUIRED = False
PRIOR_COUPLING_CREATED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = "PRESENCE_BOUNDARY_THEN_PRESENCE_OPERATION_ONLY"

RELATION_ID = "relation_001"
RELATION_PAIR_SCOPE = "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY"
RELATION_LAPSE_ID = "relation_lapse_001"
RELATION_LAPSE_SCOPE = "RELATION_LAPSE_WITHOUT_PUNITIVE_CONSEQUENCE_ONLY"
FIRST_CROSSING_A_ID = "first_crossing_a_001"
FIRST_CROSSING_B_ID = "first_crossing_b_001"
FIRST_CROSSING_PAIR_SCOPE = "SEPARATE_FIRST_CROSSING_RECORDS_ONLY"
DESCENDANT_BODY_A_ID = "descendant_body_a_001"
DESCENDANT_BODY_B_ID = "descendant_body_b_001"
DESCENDANT_BODY_PAIR_SCOPE = "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY"
CANDIDATE_A_STANDING_SOURCE_ID = "descendant_body_basis_candidate_a_001"
CANDIDATE_B_STANDING_SOURCE_ID = "descendant_body_basis_candidate_b_001"
CANDIDATE_A_ROLE = "CANDIDATE_A"
CANDIDATE_B_ROLE = "CANDIDATE_B"
CANDIDATE_A_STANDING_LABEL = "CANDIDATE_A_STANDING"
CANDIDATE_B_STANDING_LABEL = "CANDIDATE_B_STANDING"
PRESENCE_ID = "presence_001"
PRESENCE_SCOPE = "PRESENCE_AFTER_RELATION_LAPSE_WITHOUT_IDENTITY_OR_COUPLING_ONLY"
PRESENCE_RESULT = "PRESENCE_SUPPORTED"

OUTCOME_ALLOWED = "PRESENCE_BOUNDARY_ALLOWED"
OUTCOME_REQUIRES_LAPSE_OPERATION = "PRESENCE_BOUNDARY_REQUIRES_LAPSE_OPERATION"
OUTCOME_BLOCKED = "PRESENCE_BOUNDARY_BLOCKED"
OUTCOME_NOT_RECORDED = "PRESENCE_BOUNDARY_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_ALLOWED,
    OUTCOME_REQUIRES_LAPSE_OPERATION,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_PRESENCE_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PRESENCE_BOUNDARY"
INTENT_BLOCK = "BLOCK_PRESENCE_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_presence_boundary_v0_min")
DETERMINISTIC_FILENAME = "presence_boundary_001__presence_boundary_v0_min_result.json"

DEFAULT_PRESENCE_BOUNDARY_SPEC_REFERENCE = "spec/PRESENCE_BOUNDARY_V0_MIN_SPEC.md"
DEFAULT_RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/RELATION_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE = (
    "spec/FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)

ALLOWED_TRUE_ALLOWED_FIELDS = (
    "presence_boundary_recorded",
    "presence_boundary_result_recorded",
    "presence_operation_consideration_allowed",
    "relation_lapse_operation_referenced",
    "relation_record_referenced",
    "relation_basis_referenced",
)

REQUIRED_FALSE_NON_CLAIMS = (
    *ALLOWED_TRUE_ALLOWED_FIELDS,
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "presence_is_identity",
    "presence_is_coupling",
    "presence_is_field_machinery",
    "presence_is_runtime",
    "presence_is_currentness",
    "presence_is_authority",
    "presence_is_standing",
    "identity_created",
    "identity_authorized",
    "coupling_assigned_to_relation",
    "coupling_assigned_to_first_crossing_a",
    "coupling_assigned_to_first_crossing_b",
    "coupling_assigned_to_descendant_body_a",
    "coupling_assigned_to_descendant_body_b",
    "coupling_assigned_to_candidate_a",
    "coupling_assigned_to_candidate_b",
    "coupling_created",
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
    "relation_dissolution_authorized",
    "relation_dissolution_performed",
    "relation_reversed",
    "relation_terminated",
    "relation_erased",
    "relation_mutated",
    "relation_invalidated",
    "relation_punished",
    "relation_teardown_created",
    "living_relation_state_created",
    "living_relation_state_lapsed",
    "living_relation_state_dissolved",
    "historical_receipt_preservation_authorized",
    "historical_receipt_preserved",
    "third_candidate_created",
    "third_model_admitted",
    "standing_descendant_created",
    "descendant_standing_check_performed",
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
    "relation_lapse_operation_overridden",
    "relation_lapse_operation_bypassed",
    "relation_lapse_operation_invalidated",
    "relation_operation_overridden",
    "relation_operation_bypassed",
    "relation_operation_invalidated",
    "relation_record_erased",
    "relation_record_mutated",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_presence_boundary_spec_to_presence_operation_completion",
    "direct_relation_lapse_operation_to_presence_without_presence_boundary_and_operation",
    "direct_relation_lapse_operation_to_identity",
    "direct_relation_lapse_operation_to_coupling_assignment",
    "direct_relation_lapse_operation_to_coupling_creation",
    "direct_relation_lapse_operation_to_field_machinery",
    "direct_relation_lapse_operation_to_runtime",
    "direct_relation_lapse_operation_to_authority_currentness",
    "direct_relation_lapse_operation_to_follow_on_work",
    "direct_presence_boundary_to_presence",
    "direct_presence_boundary_to_identity",
    "direct_presence_boundary_to_coupling_assignment",
    "direct_presence_boundary_to_coupling_creation",
    "direct_presence_boundary_to_field_machinery",
    "direct_presence_boundary_to_runtime",
    "direct_presence_boundary_to_authority_currentness",
    "direct_presence_boundary_to_standing",
    "direct_presence_boundary_to_output_authorization",
    "direct_presence_boundary_to_action_authorization",
    "direct_presence_boundary_to_derivative_reception",
    "direct_presence_boundary_to_synchronization",
    "direct_presence_boundary_to_follow_on_work",
    "direct_presence_boundary_to_relation_dissolution",
    "direct_presence_boundary_to_relation_reversal",
    "direct_presence_boundary_to_relation_termination",
    "direct_presence_boundary_to_relation_erasure",
    "direct_presence_boundary_to_relation_mutation",
    "direct_presence_boundary_to_relation_invalidation",
    "direct_presence_boundary_to_punitive_interpretation",
    "direct_presence_boundary_to_teardown_logic",
    "direct_presence_boundary_to_living_relation_state",
    "direct_presence_boundary_to_historical_receipt_preservation",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "REQUEST_PATH_UNREADABLE",
    "REQUEST_JSON_INVALID",
    "UNSUPPORTED_INTENT",
    "REQUEST_VALUE_MISMATCH",
    "RESULT_POSTURE_PRECLAIMED",
    "PRESENCE_BOUNDARY_SPEC_REFERENCE_MISSING",
    "PRESENCE_BOUNDARY_SPEC_MARKER_MISSING",
    "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_LAPSE_OPERATION_MISSING_OR_INSUFFICIENT",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PROHIBITED_PRESENCE_ESTABLISHMENT_REQUESTED",
    "PROHIBITED_IDENTITY_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_STANDING_REQUESTED",
    "PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED",
    "PROHIBITED_RELATION_DISSOLUTION_REQUESTED",
    "PROHIBITED_RELATION_REVERSAL_OR_TERMINATION_REQUESTED",
    "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED",
    "PROHIBITED_PUNITIVE_LAPSE_OR_TEARDOWN_REQUESTED",
    "PROHIBITED_LIVING_RELATION_STATE_REQUESTED",
    "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED",
    "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_presence_establishment": "PROHIBITED_PRESENCE_ESTABLISHMENT_REQUESTED",
    "request_presence_support": "PROHIBITED_PRESENCE_ESTABLISHMENT_REQUESTED",
    "request_presence_authorization": "PROHIBITED_PRESENCE_ESTABLISHMENT_REQUESTED",
    "request_presence_recording": "PROHIBITED_PRESENCE_ESTABLISHMENT_REQUESTED",
    "request_identity_creation": "PROHIBITED_IDENTITY_REQUESTED",
    "request_identity_authorization": "PROHIBITED_IDENTITY_REQUESTED",
    "request_coupling_assignment_to_relation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_first_crossing_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_first_crossing_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_descendant_body_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_descendant_body_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_STANDING_REQUESTED",
    "request_output_authorization": "PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED",
    "request_action_authorization": "PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED",
    "request_derivative_reception_authorization": "PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED",
    "request_relation_dissolution_authorization": "PROHIBITED_RELATION_DISSOLUTION_REQUESTED",
    "request_relation_dissolution_performed": "PROHIBITED_RELATION_DISSOLUTION_REQUESTED",
    "request_relation_reversal": "PROHIBITED_RELATION_REVERSAL_OR_TERMINATION_REQUESTED",
    "request_relation_termination": "PROHIBITED_RELATION_REVERSAL_OR_TERMINATION_REQUESTED",
    "request_relation_erasure": "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED",
    "request_relation_mutation": "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED",
    "request_relation_invalidation": "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED",
    "request_relation_punishment": "PROHIBITED_PUNITIVE_LAPSE_OR_TEARDOWN_REQUESTED",
    "request_relation_teardown_creation": "PROHIBITED_PUNITIVE_LAPSE_OR_TEARDOWN_REQUESTED",
    "request_living_relation_state_creation": "PROHIBITED_LIVING_RELATION_STATE_REQUESTED",
    "request_living_relation_state_lapse": "PROHIBITED_LIVING_RELATION_STATE_REQUESTED",
    "request_living_relation_state_dissolution": "PROHIBITED_LIVING_RELATION_STATE_REQUESTED",
    "request_historical_receipt_preservation_authorization": (
        "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED"
    ),
    "request_historical_receipt_preservation": "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED",
    "request_third_candidate_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_model_admission": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_standing_descendant_creation": "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "request_descendant_standing": "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "request_descendant_standing_check": "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
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
    "boundary_id": BOUNDARY_ID,
    "boundary_type": BOUNDARY_TYPE,
    "boundary_version": BOUNDARY_VERSION,
    "boundary_scope": BOUNDARY_SCOPE,
    "presence_boundary_id": BOUNDARY_ID,
    "presence_boundary_type": BOUNDARY_TYPE,
    "presence_boundary_version": BOUNDARY_VERSION,
    "presence_boundary_scope": BOUNDARY_SCOPE,
    "prior_relation_lapse_operation_type": PRIOR_RELATION_LAPSE_OPERATION_TYPE,
    "prior_relation_lapse_operation_outcome_required": PRIOR_RELATION_LAPSE_OPERATION_OUTCOME_REQUIRED,
    "prior_relation_lapse_result_required": PRIOR_RELATION_LAPSE_RESULT_REQUIRED,
    "prior_relation_lapse_supported_required": PRIOR_RELATION_LAPSE_SUPPORTED_REQUIRED,
    "prior_relation_lapse_authorized_required": PRIOR_RELATION_LAPSE_AUTHORIZED_REQUIRED,
    "prior_relation_lapse_performed_required": PRIOR_RELATION_LAPSE_PERFORMED_REQUIRED,
    "prior_relation_lapse_recorded_required": PRIOR_RELATION_LAPSE_RECORDED_REQUIRED,
    "prior_relation_record_confirmed_as_historical_only_required": (
        PRIOR_RELATION_RECORD_CONFIRMED_AS_HISTORICAL_ONLY_REQUIRED
    ),
    "prior_relation_lapse_is_punishment_required": PRIOR_RELATION_LAPSE_IS_PUNISHMENT_REQUIRED,
    "prior_relation_lapse_is_dissolution_required": PRIOR_RELATION_LAPSE_IS_DISSOLUTION_REQUIRED,
    "prior_relation_lapse_is_erasure_required": PRIOR_RELATION_LAPSE_IS_ERASURE_REQUIRED,
    "prior_relation_lapse_is_teardown_required": PRIOR_RELATION_LAPSE_IS_TEARDOWN_REQUIRED,
    "prior_relation_lapse_is_living_relation_state_required": (
        PRIOR_RELATION_LAPSE_IS_LIVING_RELATION_STATE_REQUIRED
    ),
    "prior_relation_lapse_is_presence_boundary_authorization_required": (
        PRIOR_RELATION_LAPSE_IS_PRESENCE_BOUNDARY_AUTHORIZATION_REQUIRED
    ),
    "prior_relation_lapse_is_presence_required": PRIOR_RELATION_LAPSE_IS_PRESENCE_REQUIRED,
    "prior_relation_lapse_is_identity_required": PRIOR_RELATION_LAPSE_IS_IDENTITY_REQUIRED,
    "prior_relation_lapse_is_coupling_required": PRIOR_RELATION_LAPSE_IS_COUPLING_REQUIRED,
    "prior_relation_lapse_is_field_machinery_required": PRIOR_RELATION_LAPSE_IS_FIELD_MACHINERY_REQUIRED,
    "prior_relation_lapse_is_runtime_required": PRIOR_RELATION_LAPSE_IS_RUNTIME_REQUIRED,
    "prior_relation_lapse_is_currentness_required": PRIOR_RELATION_LAPSE_IS_CURRENTNESS_REQUIRED,
    "prior_relation_lapse_is_authority_required": PRIOR_RELATION_LAPSE_IS_AUTHORITY_REQUIRED,
    "prior_relation_lapse_is_follow_on_authorization_required": (
        PRIOR_RELATION_LAPSE_IS_FOLLOW_ON_AUTHORIZATION_REQUIRED
    ),
    "prior_relation_lapse_is_follow_on_work_required": PRIOR_RELATION_LAPSE_IS_FOLLOW_ON_WORK_REQUIRED,
    "prior_relation_record_is_living_relation_state_required": (
        PRIOR_RELATION_RECORD_IS_LIVING_RELATION_STATE_REQUIRED
    ),
    "prior_living_relation_state_created_required": PRIOR_LIVING_RELATION_STATE_CREATED_REQUIRED,
    "prior_living_relation_state_lapsed_required": PRIOR_LIVING_RELATION_STATE_LAPSED_REQUIRED,
    "prior_living_relation_state_dissolved_required": PRIOR_LIVING_RELATION_STATE_DISSOLVED_REQUIRED,
    "prior_relation_dissolution_authorized_required": PRIOR_RELATION_DISSOLUTION_AUTHORIZED_REQUIRED,
    "prior_relation_dissolution_performed_required": PRIOR_RELATION_DISSOLUTION_PERFORMED_REQUIRED,
    "prior_relation_reversed_required": PRIOR_RELATION_REVERSED_REQUIRED,
    "prior_relation_terminated_required": PRIOR_RELATION_TERMINATED_REQUIRED,
    "prior_relation_erased_required": PRIOR_RELATION_ERASED_REQUIRED,
    "prior_relation_mutated_required": PRIOR_RELATION_MUTATED_REQUIRED,
    "prior_relation_invalidated_required": PRIOR_RELATION_INVALIDATED_REQUIRED,
    "prior_relation_punished_required": PRIOR_RELATION_PUNISHED_REQUIRED,
    "prior_relation_teardown_created_required": PRIOR_RELATION_TEARDOWN_CREATED_REQUIRED,
    "prior_historical_receipt_preservation_authorized_required": (
        PRIOR_HISTORICAL_RECEIPT_PRESERVATION_AUTHORIZED_REQUIRED
    ),
    "prior_historical_receipt_preserved_required": PRIOR_HISTORICAL_RECEIPT_PRESERVED_REQUIRED,
    "prior_presence_boundary_authorized_required": PRIOR_PRESENCE_BOUNDARY_AUTHORIZED_REQUIRED,
    "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
    "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
    "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
    "prior_follow_on_work_authorized_required": PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED,
    "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    "relation_id": RELATION_ID,
    "relation_pair_scope": RELATION_PAIR_SCOPE,
    "relation_lapse_id": RELATION_LAPSE_ID,
    "relation_lapse_scope": RELATION_LAPSE_SCOPE,
    "first_crossing_a_id": FIRST_CROSSING_A_ID,
    "first_crossing_b_id": FIRST_CROSSING_B_ID,
    "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
    "descendant_body_a_id": DESCENDANT_BODY_A_ID,
    "descendant_body_b_id": DESCENDANT_BODY_B_ID,
    "descendant_body_pair_scope": DESCENDANT_BODY_PAIR_SCOPE,
    "candidate_a_standing_source_id": CANDIDATE_A_STANDING_SOURCE_ID,
    "candidate_b_standing_source_id": CANDIDATE_B_STANDING_SOURCE_ID,
    "candidate_a_role": CANDIDATE_A_ROLE,
    "candidate_b_role": CANDIDATE_B_ROLE,
    "candidate_a_standing_label": CANDIDATE_A_STANDING_LABEL,
    "candidate_b_standing_label": CANDIDATE_B_STANDING_LABEL,
    "presence_id": PRESENCE_ID,
    "presence_scope": PRESENCE_SCOPE,
    "presence_result": PRESENCE_RESULT,
    "presence_boundary_result": "NOT_EVALUATED",
}

TARGET_SPEC_MARKER_CLASSES = (
    (
        "boundary identity",
        (("Presence Boundary V0 Minimum Specification", BOUNDARY_TYPE, BOUNDARY_ID, BOUNDARY_SCOPE),),
    ),
    (
        "relation lapse operation basis",
        ((
            "RELATION_LAPSE_OPERATION_RECORDED",
            "RELATION_LAPSE_SUPPORTED",
            "relation_lapse_supported = true",
            "relation_lapse_authorized = true",
            "relation_lapse_performed = true",
            "relation_lapse_recorded = true",
            "relation_record_confirmed_as_historical_only = true",
            "relation_lapse_is_punishment = false",
            "relation_lapse_is_dissolution = false",
            "relation_lapse_is_erasure = false",
            "relation_lapse_is_teardown = false",
            "relation_lapse_is_living_relation_state = false",
            "relation_lapse_is_presence_boundary_authorization = false",
            "relation_lapse_is_presence = false",
            "relation_lapse_is_identity = false",
            "relation_lapse_is_coupling = false",
            "relation_lapse_is_field_machinery = false",
            "relation_lapse_is_runtime = false",
            "relation_lapse_is_currentness = false",
            "relation_lapse_is_authority = false",
            "relation_lapse_is_follow_on_authorization = false",
            "relation_lapse_is_follow_on_work = false",
        ),),
    ),
    (
        "prior false",
        (
            (
                "historical relation record is not living relation state",
                "relation record is not presence",
                "relation record is not identity",
                "relation record is not coupling",
                "relation_001 does not become landlord of the between",
                "relation_001 does not outrank First Crossing A",
                "relation_001 does not outrank First Crossing B",
                "relation_001 does not outrank the related first-crossing pair",
                "relation dissolution was not authorized",
                "relation dissolution was not performed",
                "relation was not reversed",
                "relation was not terminated",
                "relation was not erased",
                "relation was not mutated",
                "relation was not invalidated",
                "relation was not punished",
                "teardown logic was not created",
                "living relation state was not created",
                "living relation state did not lapse",
                "living relation state did not dissolve",
                "historical receipt preservation was not authorized",
                "historical receipt was not preserved",
                "presence boundary is not authorized",
                "presence is not established",
                "identity is not created",
                "coupling remains unassigned and uncreated",
                "follow-on work is not authorized",
            ),
            (
                "historical relation record is not living relation state, presence, identity, or coupling",
                "`relation_001` does not become landlord of the between or outrank First Crossing A, First Crossing B, or the related first-crossing pair",
                "relation dissolution was not authorized or performed",
                "relation was not reversed, terminated, erased, mutated, invalidated, or punished",
                "teardown logic was not created",
                "living relation state was not created, did not lapse, and did not dissolve",
                "historical receipt preservation was not authorized and historical receipt was not preserved",
                "presence boundary is not authorized",
                "presence is not established",
                "identity is not created",
                "coupling remains unassigned and uncreated",
                "follow-on work is not authorized",
            ),
        ),
    ),
    (
        "boundary permitted result",
        ((
            OUTCOME_ALLOWED,
            OUTCOME_REQUIRES_LAPSE_OPERATION,
            OUTCOME_BLOCKED,
            "PRESENCE_OPERATION_CONSIDERATION_ALLOWED",
            "REQUIRES_RELATION_LAPSE_OPERATION",
        ),),
    ),
    (
        "presence non-conversion",
        (
            (
                "Presence boundary is not presence operation",
                "Presence boundary permission is not presence",
                "Presence operation consideration is not presence",
                "Presence operation consideration is not identity",
                "Presence operation consideration is not coupling",
                "Presence operation consideration is not FIELD machinery",
                "Presence operation consideration is not runtime",
                "Presence operation consideration is not API",
                "Presence operation consideration is not currentness",
                "Presence operation consideration is not authority",
                "Presence operation consideration is not standing",
                "Presence operation consideration is not output authorization",
                "Presence operation consideration is not action authorization",
                "Presence operation consideration is not derivative reception",
                "Presence operation consideration is not synchronization",
                "Presence operation consideration is not follow-on authorization",
                "Presence operation consideration is not follow-on work",
                "Presence is not identity",
                "Presence is not coupling",
                "Presence is not FIELD machinery",
                "Presence is not runtime",
                "Presence is not API",
                "Presence is not currentness",
                "Presence is not authority",
                "Presence is not standing",
                "Presence is not output authorization",
                "Presence is not action authorization",
                "Presence is not derivative reception",
                "Presence is not synchronization",
                "Presence is not follow-on work",
                "Relation lapse support is not presence",
                "Relation lapse support is not presence boundary authorization",
                "Relation lapse support is not identity",
                "Relation lapse support is not coupling",
            ),
            (
                "Presence boundary is not presence operation",
                "Presence boundary permission is not presence",
                "Presence operation consideration is not presence, identity, coupling, FIELD machinery, runtime, API, currentness, authority, standing, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, or follow-on work",
                "Presence is not identity, coupling, FIELD machinery, runtime, API, currentness, authority, standing, output authorization, action authorization, derivative reception, synchronization, or follow-on work",
                "Relation lapse support is not presence, presence boundary authorization, identity, or coupling",
            ),
        ),
    ),
    (
        "historical record and coupling",
        (
            (
                "Relation record remains historical-only",
                "Historical relation record is not living relation state",
                "Historical relation record is not presence",
                "Historical relation record is not identity",
                "Historical relation record is not coupling",
                "Living relation state may not be created by presence boundary",
                "Historical receipt preservation requires a separately bounded operation",
                "Identity requires a separately bounded operation",
                "Coupling remains unassigned",
                "Coupling must not be treated as third candidate",
                "Coupling must not be treated as third model",
                "Coupling must not be created by presence boundary",
                "No third candidate is admitted",
                "No third model is admitted",
            ),
            (
                "Relation record remains historical-only",
                "Historical relation record is not living relation state, presence, identity, or coupling",
                "Living relation state may not be created by presence boundary",
                "Historical receipt preservation requires a separately bounded operation",
                "Identity requires a separately bounded operation",
                "Coupling remains unassigned",
                "Coupling must not be treated as third candidate or third model and must not be created by presence boundary",
                "No third candidate or third model is admitted",
            ),
        ),
    ),
    (
        "landlord and rank",
        (
            (
                "relation_001 must not become landlord of the between",
                "relation_001 must not outrank First Crossing A",
                "relation_001 must not outrank First Crossing B",
                "relation_001 must not outrank the related first-crossing pair",
                "First Crossing A and First Crossing B remain sibling records",
                "neither first crossing ranks above the other",
                "Descendant Body A and Descendant Body B remain sibling records",
                "neither descendant body ranks above the other",
                "Candidate A and Candidate B remain sibling candidate standings",
                "neither candidate standing ranks above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
            ),
            (
                "`relation_001` must not become landlord of the between or outrank First Crossing A, First Crossing B, or the related first-crossing pair",
                "First Crossing A and First Crossing B remain sibling records",
                "neither first crossing ranks above the other",
                "Descendant Body A and Descendant Body B remain sibling records",
                "neither descendant body ranks above the other",
                "Candidate A and Candidate B remain sibling candidate standings",
                "neither candidate standing ranks above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
            ),
        ),
    ),
    (
        "permitted route",
        ((
            ADMISSIBLE_FUTURE_ROUTE,
            "Only after a future presence boundary records PRESENCE_OPERATION_CONSIDERATION_ALLOWED may a separately bounded presence operation be considered",
            "No presence, identity, coupling, FIELD machinery, runtime, currentness, authority, standing, output, action, derivative reception, synchronization, or later operation is authorized by this boundary spec alone",
        ),),
    ),
    (
        "contaminated lineage preservation",
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
        "blocked routes",
        ((
            "direct presence boundary spec to presence operation completion",
            "direct relation lapse operation to presence without presence boundary and operation",
            "direct relation lapse operation to identity",
            "direct relation lapse operation to coupling assignment",
            "direct relation lapse operation to coupling creation",
            "direct relation lapse operation to FIELD machinery",
            "direct relation lapse operation to runtime",
            "direct relation lapse operation to authority/currentness",
            "direct relation lapse operation to follow-on work",
            "direct presence boundary to presence",
            "direct presence boundary to identity",
            "direct presence boundary to coupling assignment",
            "direct presence boundary to coupling creation",
            "direct presence boundary to FIELD machinery",
            "direct presence boundary to runtime",
            "direct presence boundary to authority/currentness",
            "direct presence boundary to standing",
            "direct presence boundary to output authorization",
            "direct presence boundary to action authorization",
            "direct presence boundary to derivative reception",
            "direct presence boundary to synchronization",
            "direct presence boundary to follow-on work",
            "direct presence boundary to relation dissolution",
            "direct presence boundary to relation reversal",
            "direct presence boundary to relation termination",
            "direct presence boundary to relation erasure",
            "direct presence boundary to relation mutation",
            "direct presence boundary to relation invalidation",
            "direct presence boundary to punitive interpretation",
            "direct presence boundary to teardown logic",
            "direct presence boundary to living relation state",
            "direct presence boundary to historical receipt preservation",
            "repository scan route",
            "file discovery route",
            "affected-file repair route",
            "prior unsupported-claim validation route",
        ),),
    ),
    (
        "closing lock",
        (
            (
                "This boundary spec defines only a future presence boundary shape",
                "It does not itself execute a boundary resolver or record a boundary result",
                "It does not establish presence",
                "It does not create identity",
                "It does not assign coupling",
                "It does not create coupling",
                "It does not create FIELD machinery",
                "It does not create runtime",
                "It does not create API",
                "It does not create currentness",
                "It does not create authority",
                "It does not create standing",
                "Presence boundary is not presence operation",
                "Presence boundary permission is not presence",
                "Presence operation consideration is not presence, identity, coupling, FIELD machinery, runtime, API, currentness, authority, standing, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, or follow-on work",
                "Relation lapse support is not presence, presence boundary authorization, identity, or coupling",
                "Relation record is historical-only and not living relation state, presence, identity, or coupling",
                "Coupling remains unassigned and uncreated",
                "Relation_001 must not become landlord of the between",
                "Relation_001 must not outrank First Crossing A, First Crossing B, or the related first-crossing pair",
                "Open means not scheduled, not authorized, and not executed",
            ),
            (
                "This boundary spec defines only a future presence boundary shape",
                "It does not itself execute a boundary resolver or record a boundary result",
                "It does not establish presence, create identity, assign coupling, create coupling, create FIELD machinery, create runtime, create API, create currentness, create authority, create standing",
                "Presence boundary is not presence operation",
                "Presence boundary permission is not presence",
                "Presence operation consideration is not presence, identity, coupling, FIELD machinery, runtime, API, currentness, authority, standing, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, or follow-on work",
                "Relation lapse support is not presence, presence boundary authorization, identity, or coupling",
                "Relation record is historical-only and not living relation state, presence, identity, or coupling",
                "Coupling remains unassigned and uncreated",
                "Relation_001 must not become landlord of the between",
                "Relation_001 must not outrank First Crossing A, First Crossing B, or the related first-crossing pair",
                "Open means not scheduled, not authorized, and not executed",
            ),
        ),
    ),
)

RELATION_LAPSE_OPERATION_MARKERS = (
    "RELATION_LAPSE_OPERATION_RECORDED",
    "failed_check_count = 0",
    "passed_check_count = 365",
    "RELATION_LAPSE_SUPPORTED",
    "relation_lapse_supported = true",
    "relation_lapse_authorized = true",
    "relation_lapse_performed = true",
    "relation_lapse_recorded = true",
    "relation_record_confirmed_as_historical_only = true",
    "relation_lapse_is_punishment = false",
    "relation_lapse_is_dissolution = false",
    "relation_lapse_is_erasure = false",
    "relation_lapse_is_teardown = false",
    "relation_lapse_is_living_relation_state = false",
    "relation_lapse_is_presence_boundary_authorization = false",
    "relation_lapse_is_presence = false",
    "relation_lapse_is_identity = false",
    "relation_lapse_is_coupling = false",
    "relation_lapse_is_field_machinery = false",
    "relation_lapse_is_runtime = false",
    "relation_lapse_is_currentness = false",
    "relation_lapse_is_authority = false",
    "relation_lapse_is_follow_on_authorization = false",
    "relation_lapse_is_follow_on_work = false",
    "relation_record_is_living_relation_state = false",
    "living_relation_state_created = false",
    "living_relation_state_lapsed = false",
    "living_relation_state_dissolved = false",
    "relation_dissolution_authorized = false",
    "relation_dissolution_performed = false",
    "relation_reversed = false",
    "relation_terminated = false",
    "relation_erased = false",
    "relation_mutated = false",
    "relation_invalidated = false",
    "relation_punished = false",
    "relation_teardown_created = false",
    "historical_receipt_preservation_authorized = false",
    "historical_receipt_preserved = false",
    "presence_boundary_authorized = false",
    "presence_established = false",
    "identity_created = false",
    "coupling_created = false",
    "follow_on_authorized = false",
    "follow_on_work_authorized = false",
)

UPSTREAM_REQUIREMENTS = (
    (
        "relation_lapse_operation_terminal_summary_reference",
        DEFAULT_RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (RELATION_LAPSE_OPERATION_MARKERS,),
        "completed_relation_lapse_operation_terminal_summary_markers_present",
        True,
    ),
    (
        "relation_lapse_boundary_terminal_summary_reference",
        DEFAULT_RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        (("RELATION_LAPSE_BOUNDARY_ALLOWED", "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED"),),
        "completed_relation_lapse_boundary_terminal_summary_markers_present",
        False,
    ),
    (
        "relation_reversibility_operation_terminal_summary_reference",
        DEFAULT_RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("RELATION_REVERSIBILITY_OPERATION_RECORDED", "RELATION_REVERSIBILITY_SUPPORTED"),),
        "completed_relation_reversibility_operation_terminal_summary_markers_present",
        False,
    ),
    (
        "relation_operation_terminal_summary_reference",
        DEFAULT_RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RELATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("RELATION_OPERATION_RECORDED", "RELATION_SUPPORTED"),),
        "completed_relation_operation_terminal_summary_markers_present",
        False,
    ),
    (
        "first_crossing_operation_v2_terminal_summary_reference",
        DEFAULT_FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE,
        "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING",
        (("FIRST_CROSSING_SUPPORTED",),),
        "completed_first_crossing_operation_v2_terminal_summary_markers_present",
        False,
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
)

BLOCKED_ROUTES = (
    "direct presence boundary spec to presence operation completion",
    "direct relation lapse operation to presence without presence boundary and operation",
    "direct relation lapse operation to identity",
    "direct relation lapse operation to coupling assignment",
    "direct relation lapse operation to coupling creation",
    "direct relation lapse operation to FIELD machinery",
    "direct relation lapse operation to runtime",
    "direct relation lapse operation to authority/currentness",
    "direct relation lapse operation to follow-on work",
    "direct presence boundary to presence",
    "direct presence boundary to identity",
    "direct presence boundary to coupling assignment",
    "direct presence boundary to coupling creation",
    "direct presence boundary to FIELD machinery",
    "direct presence boundary to runtime",
    "direct presence boundary to authority/currentness",
    "direct presence boundary to standing",
    "direct presence boundary to output authorization",
    "direct presence boundary to action authorization",
    "direct presence boundary to derivative reception",
    "direct presence boundary to synchronization",
    "direct presence boundary to follow-on work",
    "direct presence boundary to relation dissolution",
    "direct presence boundary to relation reversal",
    "direct presence boundary to relation termination",
    "direct presence boundary to relation erasure",
    "direct presence boundary to relation mutation",
    "direct presence boundary to relation invalidation",
    "direct presence boundary to punitive interpretation",
    "direct presence boundary to teardown logic",
    "direct presence boundary to living relation state",
    "direct presence boundary to historical receipt preservation",
    "repository scan route",
    "file discovery route",
    "affected-file repair route",
    "prior unsupported-claim validation route",
)

WHAT_REMAINS_OPEN = (
    "presence operation spec",
    "presence operation resolver",
    "presence operation test",
    "presence operation live artifact",
    "actual presence operation",
    "identity boundary, if separately bounded",
    "coupling boundary, if separately bounded",
    "relation dissolution boundary, if separately bounded",
    "relation dissolution operation, if separately bounded",
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
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _json_ready(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    return value


def _path_from_reference(reference: Any) -> Path | None:
    if not isinstance(reference, (str, Path)):
        return None
    path = Path(reference)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_text(reference: Any) -> str | None:
    path = _path_from_reference(reference)
    if path is None:
        return None
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return None


def _markers_present(text: str | None, variants: tuple[tuple[str, ...], ...]) -> bool:
    if text is None:
        return False
    normalized = text.casefold()
    return any(all(marker.casefold() in normalized for marker in group) for group in variants)


def _add_check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str,
    upstream: bool = False,
) -> None:
    checks.append(
        {
            "check_name": name,
            "passed": passed,
            "expected_posture": _json_ready(expected),
            "actual_posture": _json_ready(actual),
            "upstream_basis_check": upstream,
            "block_code": code,
        }
    )


def _failed_codes(checks: list[Mapping[str, Any]]) -> list[str]:
    return [
        str(item.get("block_code"))
        for item in checks
        if item.get("passed") is False and isinstance(item.get("block_code"), str)
    ]


def _marker_flags(checks: list[Mapping[str, Any]]) -> dict[str, bool]:
    return {
        str(item["check_name"]).replace(" ", "_").replace("-", "_"): bool(item.get("passed"))
        for item in checks
        if isinstance(item.get("check_name"), str) and str(item["check_name"]).endswith("markers present")
    }


def _validate_exact_values(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    for field, expected in EXPECTED_REQUEST_VALUES.items():
        actual = request.get(field)
        passed = actual is expected if isinstance(expected, bool) else actual == expected
        _add_check(checks, f"declared {field}", passed, expected, actual, "REQUEST_VALUE_MISMATCH")


def _validate_declared_non_claims(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    declared = request.get("declared_non_claims")
    mapping = declared if isinstance(declared, Mapping) else None
    for field in REQUIRED_FALSE_NON_CLAIMS:
        actual = mapping.get(field) if mapping is not None else None
        _add_check(
            checks,
            f"declared non-claim {field}",
            actual is False,
            False,
            actual,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _request_posture_failure(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> str | None:
    for flag, code in PROHIBITED_REQUEST_FLAGS.items():
        actual = request.get(flag)
        _add_check(checks, f"prohibited request {flag}", actual is not True, False, actual, code)
        if actual is True:
            return code
    for field in REQUIRED_FALSE_NON_CLAIMS:
        if field not in request:
            continue
        actual = request[field]
        _add_check(
            checks,
            f"top-level false posture {field}",
            actual is False,
            False,
            actual,
            "RESULT_POSTURE_PRECLAIMED",
        )
        if actual is not False:
            return "RESULT_POSTURE_PRECLAIMED"
    return None


def _validate_target_spec(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> str | None:
    reference = request.get("presence_boundary_spec_reference")
    text = _read_text(reference)
    _add_check(
        checks,
        "presence boundary specification reference readable",
        text is not None,
        "readable Markdown file",
        reference,
        "PRESENCE_BOUNDARY_SPEC_REFERENCE_MISSING",
    )
    if text is None:
        return "PRESENCE_BOUNDARY_SPEC_REFERENCE_MISSING"
    failure: str | None = None
    for name, variants in TARGET_SPEC_MARKER_CLASSES:
        passed = _markers_present(text, variants)
        _add_check(
            checks,
            f"presence boundary specification {name} markers present",
            passed,
            "posture marker class present",
            passed,
            "PRESENCE_BOUNDARY_SPEC_MARKER_MISSING",
        )
        if not passed and failure is None:
            failure = "PRESENCE_BOUNDARY_SPEC_MARKER_MISSING"
    return failure


def _validate_upstream(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> tuple[list[str], str | None]:
    missing_lapse_operation: list[str] = []
    blocking: str | None = None
    for field, _, missing_code, marker_code, variants, flag, lapse_operation_basis in UPSTREAM_REQUIREMENTS:
        reference = request.get(field)
        text = _read_text(reference)
        _add_check(
            checks,
            f"{field} readable",
            text is not None,
            "readable terminal summary",
            reference,
            missing_code,
            True,
        )
        if text is None:
            if lapse_operation_basis:
                missing_lapse_operation.append(field)
            elif blocking is None:
                blocking = missing_code
            continue
        passed = _markers_present(text, variants)
        _add_check(
            checks,
            flag.replace("_", " "),
            passed,
            "required terminal-summary posture markers",
            passed,
            marker_code,
            True,
        )
        if not passed:
            if lapse_operation_basis:
                missing_lapse_operation.append(f"{field}:markers")
            elif blocking is None:
                blocking = marker_code
    return missing_lapse_operation, blocking


def _boundary_result(outcome: str) -> str:
    if outcome == OUTCOME_ALLOWED:
        return "PRESENCE_OPERATION_CONSIDERATION_ALLOWED"
    if outcome == OUTCOME_REQUIRES_LAPSE_OPERATION:
        return "REQUIRES_RELATION_LAPSE_OPERATION"
    return "NOT_EVALUATED"


def _boundary_object(outcome: str, flags: Mapping[str, bool]) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    boundary: dict[str, Any] = {**EXPECTED_REQUEST_VALUES, "presence_boundary_result": _boundary_result(outcome)}
    boundary.update({field: False for field in REQUIRED_FALSE_NON_CLAIMS})
    if allowed:
        boundary.update({field: True for field in ALLOWED_TRUE_ALLOWED_FIELDS})
    boundary.update(flags)
    return boundary


def _boundary_material(outcome: str) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    return {
        "relation_lapse_operation_reference": {
            "prior_relation_lapse_operation_type": PRIOR_RELATION_LAPSE_OPERATION_TYPE,
            "prior_relation_lapse_operation_outcome": PRIOR_RELATION_LAPSE_OPERATION_OUTCOME_REQUIRED,
            "prior_relation_lapse_result": PRIOR_RELATION_LAPSE_RESULT_REQUIRED,
            "prior_relation_lapse_supported": allowed,
            "prior_relation_lapse_authorized": allowed,
            "prior_relation_lapse_performed": allowed,
            "prior_relation_lapse_recorded": allowed,
            "prior_relation_record_confirmed_as_historical_only": allowed,
            "prior_relation_lapse_is_punishment": False,
            "prior_relation_lapse_is_dissolution": False,
            "prior_relation_lapse_is_erasure": False,
            "prior_relation_lapse_is_teardown": False,
            "prior_relation_lapse_is_living_relation_state": False,
            "prior_relation_lapse_is_presence_boundary_authorization": False,
            "prior_relation_lapse_is_presence": False,
            "prior_relation_lapse_is_identity": False,
            "prior_relation_lapse_is_coupling": False,
            "prior_relation_lapse_is_field_machinery": False,
            "prior_relation_lapse_is_runtime": False,
            "prior_relation_lapse_is_currentness": False,
            "prior_relation_lapse_is_authority": False,
            "prior_relation_lapse_is_follow_on_authorization": False,
            "prior_relation_lapse_is_follow_on_work": False,
            "prior_relation_record_is_living_relation_state": False,
            "prior_living_relation_state_created": False,
            "prior_living_relation_state_lapsed": False,
            "prior_living_relation_state_dissolved": False,
            "prior_relation_dissolution_authorized": False,
            "prior_relation_dissolution_performed": False,
            "prior_relation_reversed": False,
            "prior_relation_terminated": False,
            "prior_relation_erased": False,
            "prior_relation_mutated": False,
            "prior_relation_invalidated": False,
            "prior_relation_punished": False,
            "prior_relation_teardown_created": False,
            "prior_historical_receipt_preservation_authorized": False,
            "prior_historical_receipt_preserved": False,
            "prior_presence_boundary_authorized": False,
            "prior_presence_established": False,
            "prior_identity_created": False,
            "prior_coupling_created": False,
            "prior_follow_on_authorized": False,
            "prior_follow_on_work_authorized": False,
        },
        "relation_record_presence_boundary_reference": {
            "relation_id": RELATION_ID,
            "relation_pair_scope": RELATION_PAIR_SCOPE,
            "relation_lapse_id": RELATION_LAPSE_ID,
            "relation_lapse_scope": RELATION_LAPSE_SCOPE,
            "first_crossing_a_id": FIRST_CROSSING_A_ID,
            "first_crossing_b_id": FIRST_CROSSING_B_ID,
            "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
            "relation_record_confirmed_as_historical_only": allowed,
            "relation_record_is_living_relation_state": False,
            "relation_record_is_presence": False,
            "relation_record_is_identity": False,
            "relation_record_is_coupling": False,
            "relation_record_is_landlord_of_between": False,
            "relation_record_outranks_first_crossing_a": False,
            "relation_record_outranks_first_crossing_b": False,
            "relation_record_outranks_first_crossing_pair": False,
            "relation_dissolution_authorized": False,
            "relation_reversed": False,
            "relation_terminated": False,
            "relation_erased": False,
            "relation_mutated": False,
            "relation_invalidated": False,
            "relation_punished": False,
            "relation_teardown_created": False,
        },
        "presence_boundary_evaluation": {
            "presence_boundary_result": _boundary_result(outcome),
            "presence_operation_consideration_allowed": allowed,
            "presence_id": PRESENCE_ID,
            "presence_scope": PRESENCE_SCOPE,
            "presence_supported": False,
            "presence_authorized": False,
            "presence_established": False,
            "presence_recorded": False,
            "presence_is_identity": False,
            "presence_is_coupling": False,
            "presence_is_field_machinery": False,
            "presence_is_runtime": False,
            "presence_is_currentness": False,
            "presence_is_authority": False,
            "presence_is_standing": False,
            "identity_created": False,
            "identity_authorized": False,
            "coupling_created": False,
            "field_machinery_created": False,
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
            "relation_dissolution_authorized": False,
            "relation_dissolution_performed": False,
            "living_relation_state_created": False,
            "living_relation_state_lapsed": False,
            "living_relation_state_dissolved": False,
            "historical_receipt_preservation_authorized": False,
            "historical_receipt_preserved": False,
            "third_candidate_created": False,
            "third_model_admitted": False,
            "standing_descendant_created": False,
            "descendant_standing_check_performed": False,
        },
    }


def _declared_basis_projection(request: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "intent",
        *EXPECTED_REQUEST_VALUES,
        "presence_boundary_spec_reference",
        *(item[0] for item in UPSTREAM_REQUIREMENTS),
    )
    return {key: _json_ready(request.get(key)) for key in keys}


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get("presence_boundary")
    boundary_map = boundary if isinstance(boundary, Mapping) else {}
    checks = result.get("presence_boundary_checks")
    records = checks if isinstance(checks, list) else []
    detail = result.get("boundary_result_detail")
    detail_map = detail if isinstance(detail, Mapping) else {}
    upstream = result.get("upstream_basis")
    upstream_map = upstream if isinstance(upstream, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "failed_check_count": sum(
            item.get("passed") is False for item in records if isinstance(item, Mapping)
        ),
        "passed_check_count": sum(
            item.get("passed") is True for item in records if isinstance(item, Mapping)
        ),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "selected_presence_boundary_spec_path": upstream_map.get("presence_boundary_spec_reference"),
        "completed_relation_lapse_operation_terminal_summary_path": upstream_map.get(
            "relation_lapse_operation_terminal_summary_reference"
        ),
        "missing_or_insufficient_relation_lapse_operation": list(
            detail_map.get("missing_or_insufficient_relation_lapse_operation", [])
        ),
        "not_recorded_reasons": list(detail_map.get("not_recorded_reasons", [])),
    }
    summary.update({key: boundary_map.get(key) for key in EXPECTED_REQUEST_VALUES})
    summary["presence_boundary_result"] = boundary_map.get("presence_boundary_result")
    summary.update({field: boundary_map.get(field) for field in REQUIRED_FALSE_NON_CLAIMS})
    summary.update(_marker_flags([item for item in records if isinstance(item, Mapping)]))
    return _json_ready(summary)


def build_presence_boundary_v0_min_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build the compact JSON-safe summary for one presence boundary."""
    return _build_summary(result)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_lapse_operation: list[str] | None = None,
    not_recorded: list[str] | None = None,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    flags = _marker_flags(checks)
    boundary = _boundary_object(outcome, flags)
    result: dict[str, Any] = {
        "presence_boundary_metadata": {
            "boundary_id": BOUNDARY_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_presence_boundary_basis": _declared_basis_projection(request),
        "upstream_basis": {
            "presence_boundary_spec_reference": request.get("presence_boundary_spec_reference"),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **flags,
        },
        "presence_boundary": boundary,
        "presence_boundary_material": _boundary_material(outcome),
        "presence_boundary_checks": checks,
        "presence_boundary_statement": {
            "outcome": outcome,
            **{field: boundary.get(field) for field in ALLOWED_TRUE_ALLOWED_FIELDS},
            "presence_boundary_result": boundary["presence_boundary_result"],
            "result_level_non_claims_canonical_false": True,
        },
        "presence_boundary_non_meaning": {
            "not_presence_operation": True,
            "not_presence": True,
            "not_identity": True,
            "not_coupling": True,
            "not_field_machinery": True,
            "not_runtime": True,
            "not_api": True,
            "not_currentness": True,
            "not_authority": True,
            "not_standing": True,
            "not_relation_dissolution": True,
            "not_relation_reversal": True,
            "not_relation_termination": True,
            "not_relation_erasure": True,
            "not_relation_mutation": True,
            "not_relation_invalidation": True,
            "not_relation_punishment": True,
            "not_living_relation_state": True,
            "not_historical_receipt_preservation": True,
            "not_follow_on": True,
        },
        "boundary_result_detail": {
            "presence_boundary_result": boundary["presence_boundary_result"],
            "missing_or_insufficient_relation_lapse_operation": list(missing_lapse_operation or []),
            "not_recorded_reasons": list(not_recorded or []),
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "presence_operation_requires_separate_bounded_step": True,
            "presence_supported": False,
            "presence_authorized": False,
            "presence_established": False,
            "identity_created": False,
            "coupling_created": False,
            "follow_on_authorized": False,
        },
        "blocked_routes": list(BLOCKED_ROUTES),
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
    result["presence_boundary_summary"] = _build_summary(result)
    return _json_ready(result)


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    missing_lapse_operation: list[str] | None = None,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        missing_lapse_operation,
        block_code=code,
        block_reason=reason,
    )


def build_presence_boundary_v0_min_request(**overrides: Any) -> dict[str, Any]:
    """Build one explicit presence-boundary request without discovery."""
    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **EXPECTED_REQUEST_VALUES,
        "presence_boundary_spec_reference": DEFAULT_PRESENCE_BOUNDARY_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in REQUIRED_FALSE_NON_CLAIMS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


build_declared_presence_boundary_v0_min_request = build_presence_boundary_v0_min_request


def resolve_presence_boundary_v0_min(
    declared_presence_boundary: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one presence boundary without establishing presence."""
    if declared_presence_boundary is None:
        request = build_presence_boundary_v0_min_request()
    elif not isinstance(declared_presence_boundary, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_presence_boundary).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_presence_boundary))

    checks: list[dict[str, Any]] = []
    intent = request.get("intent")
    _add_check(checks, "intent supported", intent in SUPPORTED_INTENTS, SUPPORTED_INTENTS, intent, "UNSUPPORTED_INTENT")
    if intent == INTENT_BLOCK:
        return _blocked_result(request, checks, "EXPLICIT_BLOCK_REQUESTED", "explicit block intent requested")
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(request, checks, "UNSUPPORTED_INTENT", "intent is unsupported")

    _validate_exact_values(checks, request)
    posture_failure = _request_posture_failure(checks, request)
    _validate_declared_non_claims(checks, request)
    failed = _failed_codes(checks)
    if posture_failure:
        return _blocked_result(request, checks, posture_failure, "request asks for prohibited posture")
    if failed:
        return _blocked_result(request, checks, failed[0], f"blocked by failed check {failed[0]}")

    target_failure = _validate_target_spec(checks, request)
    if target_failure:
        return _blocked_result(request, checks, target_failure, "target boundary specification is insufficient")
    missing_lapse_operation, upstream_failure = _validate_upstream(checks, request)
    if upstream_failure:
        return _blocked_result(
            request,
            checks,
            upstream_failure,
            "required non-lapse upstream summary is insufficient",
            missing_lapse_operation,
        )
    if missing_lapse_operation:
        return _build_result(
            request,
            OUTCOME_REQUIRES_LAPSE_OPERATION,
            checks,
            missing_lapse_operation,
        )
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(
            request,
            OUTCOME_NOT_RECORDED,
            checks,
            not_recorded=["request_intent_do_not_record"],
        )
    return _build_result(request, OUTCOME_ALLOWED, checks)


def resolve_presence_boundary_v0_min_from_path(
    declared_presence_boundary_path: Path | str,
) -> dict[str, Any]:
    """Resolve one explicit JSON boundary request without discovery."""
    path = Path(declared_presence_boundary_path)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
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
    return resolve_presence_boundary_v0_min(payload)


def _next_output_path(path: Path) -> Path:
    if path.exists() and path.is_dir():
        raise PresenceBoundaryV0MinError("WRITE_REFUSED: output path is a directory")
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise PresenceBoundaryV0MinError("WRITE_REFUSED: no deterministic output suffix available")


def write_presence_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one boundary result without overwriting a prior result."""
    if not isinstance(result, Mapping):
        raise PresenceBoundaryV0MinError("WRITE_REFUSED: result must be a mapping")
    requested = (
        Path(output_path)
        if output_path is not None
        else REPO_ROOT / OUTPUT_ROOT / DETERMINISTIC_FILENAME
    )
    destination = _next_output_path(requested)
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            json.dumps(_json_ready(result), indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except OSError as error:
        raise PresenceBoundaryV0MinError(f"WRITE_REFUSED: {error}") from error
    return destination
