"""Resolve one bounded relation-lapse operation result.

The resolver may record only bounded non-punitive lapse support for a
historical relation record after completed boundary allowance. It never
performs dissolution, reversal, termination, erasure, mutation, invalidation,
punishment, teardown, living-state creation, presence, runtime, repair,
discovery, or downstream authorization.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class RelationLapseOperationV0MinError(Exception):
    """Raised when a relation-lapse operation result cannot be written."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_relation_lapse_operation_v0_min"

OPERATION_ID = "relation_lapse_operation_001"
OPERATION_TYPE = "RELATION_LAPSE_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EVALUATE_RELATION_LAPSE_AFTER_BOUNDARY_ALLOWANCE_ONLY"

PRIOR_RELATION_LAPSE_BOUNDARY_TYPE = "RELATION_LAPSE_BOUNDARY"
PRIOR_RELATION_LAPSE_BOUNDARY_OUTCOME_REQUIRED = "RELATION_LAPSE_BOUNDARY_ALLOWED"
PRIOR_RELATION_LAPSE_BOUNDARY_RESULT_REQUIRED = "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED"
PRIOR_RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED_REQUIRED = True
PRIOR_RELATION_REVERSIBILITY_OPERATION_REFERENCED_REQUIRED = True
PRIOR_RELATION_RECORD_REFERENCED_REQUIRED = True
PRIOR_RELATION_BASIS_REFERENCED_REQUIRED = True
PRIOR_RELATION_LAPSE_AUTHORIZED_REQUIRED = False
PRIOR_RELATION_LAPSE_PERFORMED_REQUIRED = False
PRIOR_RELATION_LAPSE_RECORDED_REQUIRED = False
PRIOR_RELATION_LAPSE_SUPPORTED_REQUIRED = False
PRIOR_RELATION_DISSOLUTION_AUTHORIZED_REQUIRED = False
PRIOR_RELATION_DISSOLUTION_PERFORMED_REQUIRED = False
PRIOR_RELATION_REVERSED_REQUIRED = False
PRIOR_RELATION_TERMINATED_REQUIRED = False
PRIOR_RELATION_ERASED_REQUIRED = False
PRIOR_RELATION_MUTATED_REQUIRED = False
PRIOR_RELATION_INVALIDATED_REQUIRED = False
PRIOR_RELATION_PUNISHED_REQUIRED = False
PRIOR_RELATION_TEARDOWN_CREATED_REQUIRED = False
PRIOR_LIVING_RELATION_STATE_CREATED_REQUIRED = False
PRIOR_LIVING_RELATION_STATE_LAPSED_REQUIRED = False
PRIOR_LIVING_RELATION_STATE_DISSOLVED_REQUIRED = False
PRIOR_HISTORICAL_RECEIPT_PRESERVATION_AUTHORIZED_REQUIRED = False
PRIOR_HISTORICAL_RECEIPT_PRESERVED_REQUIRED = False
PRIOR_PRESENCE_BOUNDARY_AUTHORIZED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_IDENTITY_CREATED_REQUIRED = False
PRIOR_COUPLING_CREATED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = "RELATION_LAPSE_OPERATION_THEN_PRESENCE_BOUNDARY_OR_DISSOLUTION_BOUNDARY_CONSIDERATION_ONLY"

RELATION_ID = "relation_001"
RELATION_PAIR_SCOPE = "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY"
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

RELATION_LAPSE_ID = "relation_lapse_001"
RELATION_LAPSE_SCOPE = "RELATION_LAPSE_WITHOUT_PUNITIVE_CONSEQUENCE_ONLY"
RELATION_LAPSE_RESULT = "RELATION_LAPSE_SUPPORTED"
RELATION_DISSOLUTION_ID = "relation_dissolution_001"
RELATION_DISSOLUTION_SCOPE = "RELATION_DISSOLUTION_WITHOUT_TEARDOWN_OR_ERASURE_ONLY"

OUTCOME_RECORDED = "RELATION_LAPSE_OPERATION_RECORDED"
OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE = "RELATION_LAPSE_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE"
OUTCOME_BLOCKED = "RELATION_LAPSE_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = "RELATION_LAPSE_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_RELATION_LAPSE_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_RELATION_LAPSE_OPERATION"
INTENT_BLOCK = "BLOCK_RELATION_LAPSE_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_relation_lapse_operation_v0_min")
DETERMINISTIC_FILENAME = "relation_lapse_operation_001__relation_lapse_operation_v0_min_result.json"

DEFAULT_RELATION_LAPSE_OPERATION_SPEC_REFERENCE = "spec/RELATION_LAPSE_OPERATION_V0_MIN_SPEC.md"
DEFAULT_RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = "spec/RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_V0.md"
DEFAULT_RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/RELATION_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE = "spec/FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_V0.md"
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"

ALLOWED_TRUE_RECORDED_FIELDS = (
    "relation_lapse_operation_recorded",
    "relation_lapse_evaluation_performed",
    "relation_lapse_result_recorded",
    "relation_lapse_supported",
    "relation_lapse_authorized",
    "relation_lapse_performed",
    "relation_lapse_recorded",
    "relation_reversibility_operation_referenced",
    "relation_record_referenced",
    "relation_basis_referenced",
    "relation_record_confirmed_as_historical_only",
)

REQUIRED_FALSE_NON_CLAIMS = (
    *ALLOWED_TRUE_RECORDED_FIELDS,
    "relation_lapse_is_punishment",
    "relation_lapse_is_dissolution",
    "relation_lapse_is_erasure",
    "relation_lapse_is_teardown",
    "relation_lapse_is_living_relation_state",
    "relation_lapse_is_presence_boundary_authorization",
    "relation_lapse_is_presence",
    "relation_lapse_is_identity",
    "relation_lapse_is_coupling",
    "relation_lapse_is_field_machinery",
    "relation_lapse_is_runtime",
    "relation_lapse_is_currentness",
    "relation_lapse_is_authority",
    "relation_lapse_is_follow_on_authorization",
    "relation_lapse_is_follow_on_work",
    "relation_record_is_living_relation_state",
    "living_relation_state_created",
    "living_relation_state_lapsed",
    "living_relation_state_dissolved",
    "relation_dissolution_authorized",
    "relation_dissolution_performed",
    "relation_reversed",
    "relation_terminated",
    "relation_erased",
    "relation_mutated",
    "relation_invalidated",
    "relation_punished",
    "relation_teardown_created",
    "historical_receipt_preservation_authorized",
    "historical_receipt_preserved",
    "presence_boundary_authorized",
    "presence_established",
    "identity_created",
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
    "coupling_assigned_to_relation",
    "coupling_assigned_to_first_crossing_a",
    "coupling_assigned_to_first_crossing_b",
    "coupling_assigned_to_descendant_body_a",
    "coupling_assigned_to_descendant_body_b",
    "coupling_assigned_to_candidate_a",
    "coupling_assigned_to_candidate_b",
    "coupling_created",
    "third_candidate_created",
    "third_model_admitted",
    "standing_descendant_created",
    "descendant_standing_check_performed",
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
    "relation_lapse_boundary_overridden",
    "relation_lapse_boundary_bypassed",
    "relation_lapse_boundary_invalidated",
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
    "direct_relation_lapse_operation_spec_to_relation_lapse_completion",
    "direct_relation_lapse_boundary_allowance_to_relation_dissolution",
    "direct_relation_lapse_boundary_allowance_to_relation_reversal",
    "direct_relation_lapse_boundary_allowance_to_relation_termination",
    "direct_relation_lapse_boundary_allowance_to_relation_erasure",
    "direct_relation_lapse_boundary_allowance_to_relation_mutation",
    "direct_relation_lapse_boundary_allowance_to_relation_invalidation",
    "direct_relation_lapse_boundary_allowance_to_punitive_lapse_interpretation",
    "direct_relation_lapse_boundary_allowance_to_teardown_logic",
    "direct_relation_lapse_boundary_allowance_to_living_relation_state",
    "direct_relation_lapse_boundary_allowance_to_historical_receipt_preservation",
    "direct_relation_lapse_boundary_allowance_to_presence_boundary_authorization",
    "direct_relation_lapse_boundary_allowance_to_presence_establishment",
    "direct_relation_lapse_operation_to_relation_dissolution_without_dissolution_boundary",
    "direct_relation_lapse_operation_to_presence_boundary_without_separate_boundary_consideration",
    "direct_relation_to_presence",
    "direct_relation_to_identity",
    "direct_relation_to_coupling_assignment",
    "direct_relation_to_coupling_creation",
    "direct_relation_to_field_machinery",
    "direct_relation_to_runtime",
    "direct_relation_to_authority_currentness",
    "direct_relation_lapse_operation_to_follow_on_work",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "REQUEST_PATH_UNREADABLE",
    "REQUEST_JSON_INVALID",
    "UNSUPPORTED_INTENT",
    "REQUEST_VALUE_MISMATCH",
    "RESULT_POSTURE_PRECLAIMED",
    "RELATION_LAPSE_OPERATION_SPEC_REFERENCE_MISSING",
    "RELATION_LAPSE_OPERATION_SPEC_MARKER_MISSING",
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
    "BOUNDARY_ALLOWANCE_MISSING_OR_INSUFFICIENT",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PROHIBITED_RELATION_DISSOLUTION_REQUESTED",
    "PROHIBITED_RELATION_REVERSAL_OR_TERMINATION_REQUESTED",
    "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED",
    "PROHIBITED_PUNITIVE_LAPSE_OR_TEARDOWN_REQUESTED",
    "PROHIBITED_LIVING_RELATION_STATE_REQUESTED",
    "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED",
    "PROHIBITED_PRESENCE_BOUNDARY_OR_PRESENCE_REQUESTED",
    "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
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
    "request_historical_receipt_preservation_authorization": "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED",
    "request_historical_receipt_preservation": "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED",
    "request_presence_boundary_authorization": "PROHIBITED_PRESENCE_BOUNDARY_OR_PRESENCE_REQUESTED",
    "request_presence_establishment": "PROHIBITED_PRESENCE_BOUNDARY_OR_PRESENCE_REQUESTED",
    "request_identity_creation": "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_output_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_action_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_derivative_reception_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_coupling_assignment_to_relation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_first_crossing_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_first_crossing_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_descendant_body_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_descendant_body_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
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
    "operation_id": OPERATION_ID,
    "operation_type": OPERATION_TYPE,
    "operation_version": OPERATION_VERSION,
    "operation_scope": OPERATION_SCOPE,
    "relation_lapse_operation_id": OPERATION_ID,
    "relation_lapse_operation_type": OPERATION_TYPE,
    "relation_lapse_operation_version": OPERATION_VERSION,
    "relation_lapse_operation_scope": OPERATION_SCOPE,
    "prior_relation_lapse_boundary_type": PRIOR_RELATION_LAPSE_BOUNDARY_TYPE,
    "prior_relation_lapse_boundary_outcome_required": PRIOR_RELATION_LAPSE_BOUNDARY_OUTCOME_REQUIRED,
    "prior_relation_lapse_boundary_result_required": PRIOR_RELATION_LAPSE_BOUNDARY_RESULT_REQUIRED,
    "prior_relation_lapse_operation_consideration_allowed_required": PRIOR_RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED_REQUIRED,
    "prior_relation_reversibility_operation_referenced_required": PRIOR_RELATION_REVERSIBILITY_OPERATION_REFERENCED_REQUIRED,
    "prior_relation_record_referenced_required": PRIOR_RELATION_RECORD_REFERENCED_REQUIRED,
    "prior_relation_basis_referenced_required": PRIOR_RELATION_BASIS_REFERENCED_REQUIRED,
    "prior_relation_lapse_authorized_required": PRIOR_RELATION_LAPSE_AUTHORIZED_REQUIRED,
    "prior_relation_lapse_performed_required": PRIOR_RELATION_LAPSE_PERFORMED_REQUIRED,
    "prior_relation_lapse_recorded_required": PRIOR_RELATION_LAPSE_RECORDED_REQUIRED,
    "prior_relation_lapse_supported_required": PRIOR_RELATION_LAPSE_SUPPORTED_REQUIRED,
    "prior_relation_dissolution_authorized_required": PRIOR_RELATION_DISSOLUTION_AUTHORIZED_REQUIRED,
    "prior_relation_dissolution_performed_required": PRIOR_RELATION_DISSOLUTION_PERFORMED_REQUIRED,
    "prior_relation_reversed_required": PRIOR_RELATION_REVERSED_REQUIRED,
    "prior_relation_terminated_required": PRIOR_RELATION_TERMINATED_REQUIRED,
    "prior_relation_erased_required": PRIOR_RELATION_ERASED_REQUIRED,
    "prior_relation_mutated_required": PRIOR_RELATION_MUTATED_REQUIRED,
    "prior_relation_invalidated_required": PRIOR_RELATION_INVALIDATED_REQUIRED,
    "prior_relation_punished_required": PRIOR_RELATION_PUNISHED_REQUIRED,
    "prior_relation_teardown_created_required": PRIOR_RELATION_TEARDOWN_CREATED_REQUIRED,
    "prior_living_relation_state_created_required": PRIOR_LIVING_RELATION_STATE_CREATED_REQUIRED,
    "prior_living_relation_state_lapsed_required": PRIOR_LIVING_RELATION_STATE_LAPSED_REQUIRED,
    "prior_living_relation_state_dissolved_required": PRIOR_LIVING_RELATION_STATE_DISSOLVED_REQUIRED,
    "prior_historical_receipt_preservation_authorized_required": PRIOR_HISTORICAL_RECEIPT_PRESERVATION_AUTHORIZED_REQUIRED,
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
    "relation_lapse_id": RELATION_LAPSE_ID,
    "relation_lapse_scope": RELATION_LAPSE_SCOPE,
    "relation_dissolution_id": RELATION_DISSOLUTION_ID,
    "relation_dissolution_scope": RELATION_DISSOLUTION_SCOPE,
    "relation_lapse_result": "NOT_EVALUATED",
}

TARGET_SPEC_MARKER_CLASSES = (
    ("operation identity", ((
        "Relation Lapse Operation V0 Minimum Specification",
        OPERATION_TYPE,
        OPERATION_ID,
        OPERATION_SCOPE,
    ),)),
    ("boundary allowance", ((
        "RELATION_LAPSE_BOUNDARY_ALLOWED",
        "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED",
        "relation_lapse_operation_consideration_allowed = true",
        "relation_reversibility_operation_referenced = true",
        "relation_record_referenced = true",
        "relation_basis_referenced = true",
        "relation_lapse_authorized = false",
        "relation_lapse_performed = false",
        "relation_lapse_recorded = false",
        "relation_lapse_supported = false",
        "relation_dissolution_authorized = false",
        "relation_dissolution_performed = false",
        "relation_reversed = false",
        "relation_terminated = false",
        "relation_erased = false",
        "relation_mutated = false",
        "relation_invalidated = false",
        "relation_punished = false",
        "relation_teardown_created = false",
        "living_relation_state_created = false",
        "living_relation_state_lapsed = false",
        "living_relation_state_dissolved = false",
        "historical_receipt_preservation_authorized = false",
        "historical_receipt_preserved = false",
        "presence_boundary_authorized = false",
        "presence_established = false",
        "identity_created = false",
        "coupling_created = false",
        "follow_on_authorized = false",
        "follow_on_work_authorized = false",
    ),)),
    ("operation support", ((
        RELATION_LAPSE_RESULT,
        "relation_lapse_supported = true",
        "relation_lapse_authorized = true",
        "relation_lapse_performed = true",
        "relation_lapse_recorded = true",
        "relation_record_confirmed_as_historical_only = true",
        RELATION_LAPSE_SCOPE,
    ),)),
    ("operation non-conversion", (
        (
            "Relation lapse operation is not relation dissolution",
            "Relation lapse operation is not relation reversal",
            "Relation lapse operation is not relation termination",
            "Relation lapse operation is not relation erasure",
            "Relation lapse operation is not relation mutation",
            "Relation lapse operation is not relation invalidation",
            "Relation lapse operation is not punishment",
            "Relation lapse operation is not teardown",
            "Relation lapse support is not relation dissolution",
            "Relation lapse support is not relation reversal",
            "Relation lapse support is not relation termination",
            "Relation lapse support is not relation erasure",
            "Relation lapse support is not relation mutation",
            "Relation lapse support is not relation invalidation",
            "Relation lapse support is not punishment",
            "Relation lapse support is not teardown",
            "Relation lapse support is not living relation state",
            "Relation lapse support is not historical receipt preservation",
            "Relation lapse support is not presence boundary authorization",
            "Relation lapse support is not presence",
            "Relation lapse support is not identity",
            "Relation lapse support is not coupling",
            "Relation lapse support is not FIELD machinery",
            "Relation lapse support is not runtime",
            "Relation lapse support is not currentness",
            "Relation lapse support is not authority",
            "Relation lapse support is not follow-on authorization",
            "Relation lapse support is not follow-on work",
            "Relation lapse is not punishment",
            "Relation lapse is not dissolution",
            "Relation lapse is not erasure",
            "Relation lapse is not teardown",
        ),
        (
            "Relation lapse operation is not relation dissolution, relation reversal, relation termination, relation erasure, relation mutation, relation invalidation, punishment, or teardown",
            "Relation lapse support is not relation dissolution, relation reversal, relation termination, relation erasure, relation mutation, relation invalidation, punishment, teardown, living relation state, historical receipt preservation, presence boundary authorization, presence, identity, coupling, FIELD machinery, runtime, currentness, authority, follow-on authorization, or follow-on work",
            "Relation lapse is not punishment, dissolution, erasure, or teardown",
        ),
    )),
    ("historical relation record", ((
        "Historical relation record is not living relation state",
        "Relation record remains historical-only",
        "Living relation state may not be created by relation lapse operation",
        "Living relation state may lapse only by a separately bounded operation",
        "Historical receipt preservation requires a separately bounded operation",
    ),)),
    ("landlord and rank", (
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
            "coupling remains unassigned",
        ),
        (
            "`relation_001` must not become landlord of the between",
            "`relation_001` must not outrank First Crossing A, First Crossing B, or the related first-crossing pair",
            "First Crossing A and First Crossing B remain sibling records. Neither first crossing ranks above the other",
            "Descendant Body A and Descendant Body B remain sibling records. Neither descendant body ranks above the other",
            "Candidate A and Candidate B remain sibling candidate standings. Neither candidate standing ranks above the other",
            "Regulation may not become sovereign over Motion",
            "Motion may not erase Regulation",
            "Coupling remains unassigned",
        ),
    )),
    ("permitted route", ((
        ADMISSIBLE_FUTURE_ROUTE,
        "Only after a future relation lapse operation records RELATION_LAPSE_SUPPORTED may a separately bounded presence boundary or relation dissolution boundary be considered",
        "No relation dissolution, presence boundary, or later operation is authorized by this operation specification alone",
    ),)),
    ("contaminated lineage preservation", (
        (
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        ),
        (
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md",
            "remains preserved contaminated lineage",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        ),
    )),
    ("blocked routes", ((
        "direct relation lapse operation spec to relation lapse completion",
        "direct relation lapse boundary allowance to relation dissolution",
        "direct relation lapse boundary allowance to relation reversal",
        "direct relation lapse boundary allowance to relation termination",
        "direct relation lapse boundary allowance to relation erasure",
        "direct relation lapse boundary allowance to relation mutation",
        "direct relation lapse boundary allowance to relation invalidation",
        "direct relation lapse boundary allowance to punitive lapse interpretation",
        "direct relation lapse boundary allowance to teardown logic",
        "direct relation lapse boundary allowance to living relation state",
        "direct relation lapse boundary allowance to historical receipt preservation",
        "direct relation lapse boundary allowance to presence boundary authorization",
        "direct relation lapse boundary allowance to presence establishment",
        "direct relation lapse operation to relation dissolution without dissolution boundary",
        "direct relation lapse operation to presence boundary without separate boundary consideration",
        "direct relation to presence",
        "direct relation to identity",
        "direct relation to coupling assignment",
        "direct relation to coupling creation",
        "direct relation to FIELD machinery",
        "direct relation to runtime",
        "direct relation to authority/currentness",
        "direct relation lapse operation to follow-on work",
        "repository scan route",
        "file discovery route",
        "affected-file repair route",
        "prior unsupported-claim validation route",
    ),)),
    ("closing lock", (
        (
            "This operation spec defines only a future relation lapse operation shape",
            "It does not itself execute relation lapse or record an operation result",
            "It does not dissolve relation",
            "It does not reverse relation",
            "It does not terminate relation",
            "It does not erase relation",
            "It does not mutate relation_001",
            "Relation lapse operation is not relation dissolution, relation reversal, relation termination, relation erasure, relation mutation, relation invalidation, punishment, or teardown",
            "Relation lapse support is not relation dissolution, relation reversal, relation termination, relation erasure, relation mutation, relation invalidation, punishment, teardown, living relation state, historical receipt preservation, presence boundary authorization, presence, identity, coupling, FIELD machinery, runtime, currentness, authority, follow-on authorization, or follow-on work",
            "Relation record is historical-only and not living relation state",
            "Relation_001 must not become landlord of the between",
            "Relation_001 must not outrank First Crossing A, First Crossing B, or the related first-crossing pair",
            "Open means not scheduled, not authorized, and not executed",
        ),
        (
            "This operation spec defines only a future relation lapse operation shape",
            "It does not itself execute relation lapse or record an operation result",
            "It does not dissolve relation, reverse relation, terminate relation, erase relation, mutate relation_001",
            "Relation lapse operation is not relation dissolution, relation reversal, relation termination, relation erasure, relation mutation, relation invalidation, punishment, or teardown",
            "Relation lapse support is not relation dissolution, relation reversal, relation termination, relation erasure, relation mutation, relation invalidation, punishment, teardown, living relation state, historical receipt preservation, presence boundary authorization, presence, identity, coupling, FIELD machinery, runtime, currentness, authority, follow-on authorization, or follow-on work",
            "Relation record is historical-only and not living relation state",
            "Relation_001 must not become landlord of the between",
            "Relation_001 must not outrank First Crossing A, First Crossing B, or the related first-crossing pair",
            "Open means not scheduled, not authorized, and not executed",
        ),
    )),
)

UPSTREAM_REQUIREMENTS = (
    (
        "relation_lapse_boundary_terminal_summary_reference",
        DEFAULT_RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            "RELATION_LAPSE_BOUNDARY_ALLOWED",
            "failed_check_count = 0",
            "passed_check_count = 341",
            "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED",
            "relation_lapse_operation_consideration_allowed = true",
            "relation_reversibility_operation_referenced = true",
            "relation_record_referenced = true",
            "relation_basis_referenced = true",
            "relation_lapse_authorized = false",
            "relation_lapse_performed = false",
            "relation_lapse_recorded = false",
            "relation_lapse_supported = false",
            "relation_dissolution_authorized = false",
            "relation_dissolution_performed = false",
            "relation_reversed = false",
            "relation_terminated = false",
            "relation_erased = false",
            "relation_mutated = false",
            "relation_invalidated = false",
            "relation_punished = false",
            "relation_teardown_created = false",
            "living_relation_state_created = false",
            "living_relation_state_lapsed = false",
            "living_relation_state_dissolved = false",
            "historical_receipt_preservation_authorized = false",
            "historical_receipt_preserved = false",
            "presence_boundary_authorized = false",
            "presence_established = false",
            "identity_created = false",
            "coupling_created = false",
            "follow_on_authorized = false",
            "follow_on_work_authorized = false",
        ),),
        "completed_relation_lapse_boundary_terminal_summary_markers_present",
        True,
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
    "direct relation lapse operation spec to relation lapse completion",
    "direct relation lapse boundary allowance to relation dissolution",
    "direct relation lapse boundary allowance to relation reversal",
    "direct relation lapse boundary allowance to relation termination",
    "direct relation lapse boundary allowance to relation erasure",
    "direct relation lapse boundary allowance to relation mutation",
    "direct relation lapse boundary allowance to relation invalidation",
    "direct relation lapse boundary allowance to punitive lapse interpretation",
    "direct relation lapse boundary allowance to teardown logic",
    "direct relation lapse boundary allowance to living relation state",
    "direct relation lapse boundary allowance to historical receipt preservation",
    "direct relation lapse boundary allowance to presence boundary authorization",
    "direct relation lapse boundary allowance to presence establishment",
    "direct relation lapse operation to relation dissolution without dissolution boundary",
    "direct relation lapse operation to presence boundary without separate boundary consideration",
    "direct relation to presence",
    "direct relation to identity",
    "direct relation to coupling assignment",
    "direct relation to coupling creation",
    "direct relation to FIELD machinery",
    "direct relation to runtime",
    "direct relation to authority/currentness",
    "direct relation lapse operation to follow-on work",
    "repository scan route",
    "file discovery route",
    "affected-file repair route",
    "prior unsupported-claim validation route",
)

WHAT_REMAINS_OPEN = (
    "relation dissolution boundary, if separately bounded",
    "relation dissolution operation, if separately bounded",
    "presence boundary, if separately bounded after lapse operation or dissolution consideration",
    "presence",
    "FIELD machinery",
    "runtime",
    "API",
    "currentness",
    "authority",
    "standing",
    "identity boundary",
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
        str(item["check_name"]).replace(" ", "_"): bool(item.get("passed"))
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
        _add_check(checks, f"declared non-claim {field}", actual is False, False, actual, "NON_CLAIM_MISSING_OR_FLIPPED")


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
        _add_check(checks, f"top-level false posture {field}", actual is False, False, actual, "RESULT_POSTURE_PRECLAIMED")
        if actual is not False:
            return "RESULT_POSTURE_PRECLAIMED"
    return None


def _validate_target_spec(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> str | None:
    reference = request.get("relation_lapse_operation_spec_reference")
    text = _read_text(reference)
    _add_check(
        checks,
        "relation-lapse operation specification reference readable",
        text is not None,
        "readable Markdown file",
        reference,
        "RELATION_LAPSE_OPERATION_SPEC_REFERENCE_MISSING",
    )
    if text is None:
        return "RELATION_LAPSE_OPERATION_SPEC_REFERENCE_MISSING"
    failure: str | None = None
    for name, variants in TARGET_SPEC_MARKER_CLASSES:
        passed = _markers_present(text, variants)
        _add_check(
            checks,
            f"relation-lapse operation specification {name} markers present",
            passed,
            "posture marker class present",
            passed,
            "RELATION_LAPSE_OPERATION_SPEC_MARKER_MISSING",
        )
        if not passed and failure is None:
            failure = "RELATION_LAPSE_OPERATION_SPEC_MARKER_MISSING"
    return failure


def _validate_upstream(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> tuple[list[str], str | None]:
    missing_allowance: list[str] = []
    blocking: str | None = None
    for field, _, missing_code, marker_code, variants, flag, boundary_basis in UPSTREAM_REQUIREMENTS:
        reference = request.get(field)
        text = _read_text(reference)
        _add_check(checks, f"{field} readable", text is not None, "readable terminal summary", reference, missing_code, True)
        if text is None:
            if boundary_basis:
                missing_allowance.append(field)
            elif blocking is None:
                blocking = missing_code
            continue
        passed = _markers_present(text, variants)
        _add_check(checks, flag.replace("_", " "), passed, "required terminal-summary posture markers", passed, marker_code, True)
        if not passed:
            if boundary_basis:
                missing_allowance.append(field)
            elif blocking is None:
                blocking = marker_code
    return missing_allowance, blocking


def _operation_result(outcome: str) -> str:
    if outcome == OUTCOME_RECORDED:
        return RELATION_LAPSE_RESULT
    if outcome == OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE:
        return "REQUIRES_BOUNDARY_ALLOWANCE"
    return "NOT_EVALUATED"


def _operation_object(outcome: str, flags: Mapping[str, bool]) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    operation: dict[str, Any] = {**EXPECTED_REQUEST_VALUES, "relation_lapse_result": _operation_result(outcome)}
    operation.update({field: False for field in REQUIRED_FALSE_NON_CLAIMS})
    if recorded:
        operation.update({field: True for field in ALLOWED_TRUE_RECORDED_FIELDS})
    operation.update(flags)
    return operation


def _operation_material(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    return {
        "boundary_allowance_reference": {
            "prior_relation_lapse_boundary_type": PRIOR_RELATION_LAPSE_BOUNDARY_TYPE,
            "prior_relation_lapse_boundary_outcome": PRIOR_RELATION_LAPSE_BOUNDARY_OUTCOME_REQUIRED,
            "prior_relation_lapse_boundary_result": PRIOR_RELATION_LAPSE_BOUNDARY_RESULT_REQUIRED,
            "prior_relation_lapse_operation_consideration_allowed": recorded,
            "prior_relation_reversibility_operation_referenced": recorded,
            "prior_relation_record_referenced": recorded,
            "prior_relation_basis_referenced": recorded,
            "prior_relation_lapse_authorized": False,
            "prior_relation_lapse_performed": False,
            "prior_relation_lapse_recorded": False,
            "prior_relation_lapse_supported": False,
            "prior_relation_dissolution_authorized": False,
            "prior_relation_dissolution_performed": False,
            "prior_relation_reversed": False,
            "prior_relation_terminated": False,
            "prior_relation_erased": False,
            "prior_relation_mutated": False,
            "prior_relation_invalidated": False,
            "prior_relation_punished": False,
            "prior_relation_teardown_created": False,
            "prior_living_relation_state_created": False,
            "prior_living_relation_state_lapsed": False,
            "prior_living_relation_state_dissolved": False,
            "prior_historical_receipt_preservation_authorized": False,
            "prior_historical_receipt_preserved": False,
            "prior_presence_boundary_authorized": False,
            "prior_presence_established": False,
            "prior_identity_created": False,
            "prior_coupling_created": False,
            "prior_follow_on_authorized": False,
            "prior_follow_on_work_authorized": False,
        },
        "relation_record_lapse_evaluation": {
            "relation_id": RELATION_ID,
            "relation_pair_scope": RELATION_PAIR_SCOPE,
            "first_crossing_a_id": FIRST_CROSSING_A_ID,
            "first_crossing_b_id": FIRST_CROSSING_B_ID,
            "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
            "relation_record_confirmed_as_historical_only": recorded,
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
        "lapse_result_evaluation": {
            "relation_lapse_result": _operation_result(outcome),
            "relation_lapse_supported": recorded,
            "relation_lapse_authorized": recorded,
            "relation_lapse_performed": recorded,
            "relation_lapse_recorded": recorded,
            "relation_lapse_id": RELATION_LAPSE_ID,
            "relation_lapse_scope": RELATION_LAPSE_SCOPE,
            "relation_lapse_is_punishment": False,
            "relation_lapse_is_dissolution": False,
            "relation_lapse_is_erasure": False,
            "relation_lapse_is_teardown": False,
            "relation_lapse_is_living_relation_state": False,
            "relation_lapse_is_presence_boundary_authorization": False,
            "relation_lapse_is_presence": False,
            "relation_lapse_is_identity": False,
            "relation_lapse_is_coupling": False,
            "relation_lapse_is_field_machinery": False,
            "relation_lapse_is_runtime": False,
            "relation_lapse_is_currentness": False,
            "relation_lapse_is_authority": False,
            "relation_lapse_is_follow_on_authorization": False,
            "relation_lapse_is_follow_on_work": False,
            "relation_dissolution_authorized": False,
            "relation_dissolution_performed": False,
            "living_relation_state_created": False,
            "living_relation_state_lapsed": False,
            "living_relation_state_dissolved": False,
            "historical_receipt_preservation_authorized": False,
            "historical_receipt_preserved": False,
            "presence_boundary_authorized": False,
            "presence_established": False,
            "identity_created": False,
            "coupling_created": False,
            "follow_on_authorized": False,
            "follow_on_work_authorized": False,
        },
    }


def _declared_basis_projection(request: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "intent",
        *EXPECTED_REQUEST_VALUES,
        "relation_lapse_operation_spec_reference",
        *(item[0] for item in UPSTREAM_REQUIREMENTS),
    )
    return {key: _json_ready(request.get(key)) for key in keys}


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("relation_lapse_operation")
    operation_map = operation if isinstance(operation, Mapping) else {}
    checks = result.get("relation_lapse_operation_checks")
    records = checks if isinstance(checks, list) else []
    detail = result.get("operation_result_detail")
    detail_map = detail if isinstance(detail, Mapping) else {}
    upstream = result.get("upstream_basis")
    upstream_map = upstream if isinstance(upstream, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "failed_check_count": sum(item.get("passed") is False for item in records if isinstance(item, Mapping)),
        "passed_check_count": sum(item.get("passed") is True for item in records if isinstance(item, Mapping)),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "selected_relation_lapse_operation_spec_path": upstream_map.get("relation_lapse_operation_spec_reference"),
        "completed_relation_lapse_boundary_terminal_summary_path": upstream_map.get("relation_lapse_boundary_terminal_summary_reference"),
        "missing_or_insufficient_boundary_allowance": list(detail_map.get("missing_or_insufficient_boundary_allowance", [])),
        "not_recorded_reasons": list(detail_map.get("not_recorded_reasons", [])),
    }
    summary.update({key: operation_map.get(key) for key in EXPECTED_REQUEST_VALUES})
    summary["relation_lapse_result"] = operation_map.get("relation_lapse_result")
    summary.update({field: operation_map.get(field) for field in REQUIRED_FALSE_NON_CLAIMS})
    summary.update(_marker_flags([item for item in records if isinstance(item, Mapping)]))
    return _json_ready(summary)


def build_relation_lapse_operation_v0_min_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build the compact JSON-safe summary for one operation result."""
    return _build_summary(result)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_allowance: list[str] | None = None,
    not_recorded: list[str] | None = None,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    flags = _marker_flags(checks)
    operation = _operation_object(outcome, flags)
    result: dict[str, Any] = {
        "relation_lapse_operation_metadata": {
            "operation_id": OPERATION_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_relation_lapse_operation_basis": _declared_basis_projection(request),
        "upstream_basis": {
            "relation_lapse_operation_spec_reference": request.get("relation_lapse_operation_spec_reference"),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **flags,
        },
        "relation_lapse_operation": operation,
        "relation_lapse_operation_material": _operation_material(outcome),
        "relation_lapse_operation_checks": checks,
        "relation_lapse_operation_statement": {
            "outcome": outcome,
            **{field: operation.get(field) for field in ALLOWED_TRUE_RECORDED_FIELDS},
            "relation_lapse_result": operation["relation_lapse_result"],
            "result_level_non_claims_canonical_false": True,
        },
        "relation_lapse_operation_non_meaning": {
            "not_relation_dissolution": True,
            "not_relation_reversal": True,
            "not_relation_termination": True,
            "not_relation_erasure": True,
            "not_relation_mutation": True,
            "not_relation_invalidation": True,
            "not_punishment": True,
            "not_teardown": True,
            "not_living_relation_state": True,
            "not_historical_receipt_preservation": True,
            "not_presence_boundary_authorization": True,
            "not_presence": True,
            "not_identity": True,
            "not_coupling": True,
            "not_field_machinery": True,
            "not_runtime": True,
            "not_currentness": True,
            "not_authority": True,
            "not_follow_on": True,
        },
        "operation_result_detail": {
            "relation_lapse_result": operation["relation_lapse_result"],
            "missing_or_insufficient_boundary_allowance": list(missing_allowance or []),
            "not_recorded_reasons": list(not_recorded or []),
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "presence_or_relation_dissolution_boundary_requires_separate_bounded_step": True,
            "relation_dissolution_authorized": False,
            "presence_boundary_authorized": False,
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
    result["relation_lapse_operation_summary"] = _build_summary(result)
    return _json_ready(result)


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    missing_allowance: list[str] | None = None,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(request, OUTCOME_BLOCKED, checks, missing_allowance, block_code=code, block_reason=reason)


def build_relation_lapse_operation_v0_min_request(**overrides: Any) -> dict[str, Any]:
    """Build one explicit operation request without repository discovery."""
    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **EXPECTED_REQUEST_VALUES,
        "relation_lapse_operation_spec_reference": DEFAULT_RELATION_LAPSE_OPERATION_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in REQUIRED_FALSE_NON_CLAIMS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


build_declared_relation_lapse_operation_v0_min_request = build_relation_lapse_operation_v0_min_request


def resolve_relation_lapse_operation_v0_min(
    declared_relation_lapse_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one relation-lapse operation without converting relation."""
    if declared_relation_lapse_operation is None:
        request = build_relation_lapse_operation_v0_min_request()
    elif not isinstance(declared_relation_lapse_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request mapping", False, "mapping", type(declared_relation_lapse_operation).__name__, "REQUEST_NOT_MAPPING")
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_relation_lapse_operation))

    checks = []
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
        return _build_result(request, OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE, checks, missing_allowance)
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, not_recorded=["request_intent_do_not_record"])
    return _build_result(request, OUTCOME_RECORDED, checks)


def resolve_relation_lapse_operation_v0_min_from_path(
    declared_relation_lapse_operation_path: Path | str,
) -> dict[str, Any]:
    """Resolve one explicit JSON request path without filesystem discovery."""
    path = Path(declared_relation_lapse_operation_path)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError):
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request path readable", False, "readable JSON request", str(path), "REQUEST_PATH_UNREADABLE")
        return _blocked_result({}, checks, "REQUEST_PATH_UNREADABLE", "request path is unreadable")
    except json.JSONDecodeError:
        checks = []
        _add_check(checks, "request JSON parseable", False, "JSON object", "invalid JSON", "REQUEST_JSON_INVALID")
        return _blocked_result({}, checks, "REQUEST_JSON_INVALID", "request JSON is invalid")
    return resolve_relation_lapse_operation_v0_min(payload)


def _next_output_path(path: Path) -> Path:
    if path.exists() and path.is_dir():
        raise RelationLapseOperationV0MinError("WRITE_REFUSED: output path is a directory")
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise RelationLapseOperationV0MinError("WRITE_REFUSED: no deterministic output suffix available")


def write_relation_lapse_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one operation result without overwriting a prior result."""
    if not isinstance(result, Mapping):
        raise RelationLapseOperationV0MinError("WRITE_REFUSED: result must be a mapping")
    requested = Path(output_path) if output_path is not None else REPO_ROOT / OUTPUT_ROOT / DETERMINISTIC_FILENAME
    destination = _next_output_path(requested)
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(_json_ready(result), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except OSError as error:
        raise RelationLapseOperationV0MinError(f"WRITE_REFUSED: {error}") from error
    return destination

