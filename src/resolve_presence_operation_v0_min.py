"""Resolve one bounded presence-operation result.

The resolver evaluates completed presence-boundary allowance and receiver-side
answerable basis.  It records a lawful receiver-attestation waiting state by
default and records presence support only when every receiver-basis condition
is satisfied.  It does not create identity, coupling, runtime, authority,
standing, relation change, repair, scanning, or downstream authorization.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class PresenceOperationV0MinError(Exception):
    """Raised when a presence-operation result cannot be written."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_presence_operation_v0_min"

OPERATION_ID = "presence_operation_001"
OPERATION_TYPE = "PRESENCE_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = (
    "EVALUATE_PRESENCE_AFTER_BOUNDARY_ALLOWANCE_WITH_RECEIVER_ATTESTATION_REQUIREMENT_ONLY"
)

PRIOR_PRESENCE_BOUNDARY_TYPE = "PRESENCE_BOUNDARY"
PRIOR_PRESENCE_BOUNDARY_OUTCOME_REQUIRED = "PRESENCE_BOUNDARY_ALLOWED"
PRIOR_PRESENCE_BOUNDARY_RESULT_REQUIRED = "PRESENCE_OPERATION_CONSIDERATION_ALLOWED"
PRIOR_PRESENCE_OPERATION_CONSIDERATION_ALLOWED_REQUIRED = True
PRIOR_RELATION_LAPSE_OPERATION_REFERENCED_REQUIRED = True
PRIOR_RELATION_RECORD_REFERENCED_REQUIRED = True
PRIOR_RELATION_BASIS_REFERENCED_REQUIRED = True
PRIOR_PRESENCE_SUPPORTED_REQUIRED = False
PRIOR_PRESENCE_AUTHORIZED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_PRESENCE_RECORDED_REQUIRED = False
PRIOR_IDENTITY_CREATED_REQUIRED = False
PRIOR_IDENTITY_AUTHORIZED_REQUIRED = False
PRIOR_COUPLING_CREATED_REQUIRED = False
PRIOR_FIELD_MACHINERY_CREATED_REQUIRED = False
PRIOR_RUNTIME_CREATED_REQUIRED = False
PRIOR_API_CREATED_REQUIRED = False
PRIOR_CURRENTNESS_CREATED_REQUIRED = False
PRIOR_AUTHORITY_CREATED_REQUIRED = False
PRIOR_STANDING_CREATED_REQUIRED = False
PRIOR_OUTPUT_AUTHORIZED_REQUIRED = False
PRIOR_ACTION_AUTHORIZED_REQUIRED = False
PRIOR_DERIVATIVE_RECEPTION_AUTHORIZED_REQUIRED = False
PRIOR_SYNCHRONIZATION_AUTHORIZED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED = False
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
PRIOR_THIRD_CANDIDATE_CREATED_REQUIRED = False
PRIOR_THIRD_MODEL_ADMITTED_REQUIRED = False
PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED = False
PRIOR_DESCENDANT_STANDING_CHECK_PERFORMED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = (
    "PRESENCE_OPERATION_WITH_RECEIVER_ATTESTATION_THEN_IDENTITY_OR_COUPLING_"
    "BOUNDARY_CONSIDERATION_ONLY"
)

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
PRESENCE_SCOPE = "PRESENCE_AFTER_RELATION_LAPSE_WITH_RECEIVER_ATTESTATION_ONLY"
PRESENCE_RESULT = "PRESENCE_SUPPORTED"

RECEIVER_ANSWERABLE_BASIS_ID = "receiver_answerable_basis_001"
RECEIVER_ANSWERABLE_BASIS_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS"
RECEIVER_ANSWERABLE_BASIS_SCOPE = (
    "CUSTODY_DISTINCT_REFUSABLE_RECEIVER_ATTESTATION_OR_EXTERNAL_ANSWERABLE_RECEIPT_ONLY"
)

OUTCOME_SUPPORTED = "PRESENCE_OPERATION_SUPPORTED"
OUTCOME_REQUIRES_RECEIVER_ATTESTATION = "PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION"
OUTCOME_BLOCKED = "PRESENCE_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = "PRESENCE_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_SUPPORTED,
    OUTCOME_REQUIRES_RECEIVER_ATTESTATION,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_PRESENCE_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PRESENCE_OPERATION"
INTENT_BLOCK = "BLOCK_PRESENCE_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_presence_operation_v0_min")
DETERMINISTIC_FILENAME = "presence_operation_001__presence_operation_v0_min_result.json"

DEFAULT_PRESENCE_OPERATION_SPEC_REFERENCE = "spec/PRESENCE_OPERATION_V0_MIN_SPEC.md"
DEFAULT_PRESENCE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/PRESENCE_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/RELATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE = (
    "spec/FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)

RECEIVER_BASIS_DEFAULTS = {
    "receiver_attested": False,
    "receiver_answerable_receipt_present": False,
    "receiver_answerable_basis_custody_distinct": False,
    "receiver_answerable_basis_controlled_by_declaring_side": False,
    "receiver_answerable_basis_refusable": False,
    "receiver_answerable_basis_could_have_been_withheld": False,
    "repo_local_execution_only": True,
    "operator_only_attestation": False,
    "derivative_rendering_attestation": False,
    "same_custody_countersignature": False,
    "automatic_acknowledgement": False,
    "generated_affirmation": False,
    "forged_receiver_attestation": False,
    "inadmissible_receiver_basis": False,
}

RECEIVER_BASIS_FIELDS = tuple(RECEIVER_BASIS_DEFAULTS)
ADMISSIBLE_RECEIVER_TRUE_INPUT_FIELDS = {
    "receiver_attested",
    "receiver_answerable_receipt_present",
    "receiver_answerable_basis_custody_distinct",
    "receiver_answerable_basis_refusable",
    "receiver_answerable_basis_could_have_been_withheld",
}

ALLOWED_TRUE_REQUIRES_RECEIVER_ATTESTATION_FIELDS = (
    "presence_operation_recorded",
    "presence_evaluation_performed",
    "presence_result_recorded",
    "presence_operation_requires_receiver_attestation",
    "receiver_attestation_required",
    "repo_local_execution_only",
    "relation_record_referenced",
    "relation_basis_referenced",
    "presence_boundary_referenced",
    "receiver_answerable_basis_required",
)

ALLOWED_TRUE_SUPPORTED_FIELDS = (
    "presence_operation_recorded",
    "presence_evaluation_performed",
    "presence_result_recorded",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "receiver_attested",
    "receiver_answerable_receipt_present",
    "receiver_answerable_basis_custody_distinct",
    "receiver_answerable_basis_refusable",
    "receiver_answerable_basis_could_have_been_withheld",
    "relation_record_referenced",
    "relation_basis_referenced",
    "presence_boundary_referenced",
)

PURE_OUTPUT_PRECLAIM_FIELDS = (
    "presence_operation_requires_receiver_attestation",
    "receiver_attestation_required",
    "relation_record_referenced",
    "relation_basis_referenced",
    "presence_boundary_referenced",
    "receiver_answerable_basis_required",
)

REQUIRED_FALSE_NON_CLAIMS = tuple(
    """
    presence_operation_recorded
    presence_evaluation_performed
    presence_result_recorded
    presence_supported
    presence_authorized
    presence_established
    presence_recorded
    receiver_attested
    receiver_answerable_receipt_present
    receiver_answerable_basis_custody_distinct
    receiver_answerable_basis_controlled_by_declaring_side
    receiver_answerable_basis_refusable
    receiver_answerable_basis_could_have_been_withheld
    operator_only_attestation
    derivative_rendering_attestation
    same_custody_countersignature
    automatic_acknowledgement
    generated_affirmation
    forged_receiver_attestation
    inadmissible_receiver_basis
    presence_is_identity
    presence_is_coupling
    presence_is_field_machinery
    presence_is_runtime
    presence_is_api
    presence_is_currentness
    presence_is_authority
    presence_is_standing
    presence_is_output_authorization
    presence_is_action_authorization
    presence_is_derivative_reception
    presence_is_synchronization
    presence_is_follow_on_authorization
    presence_is_follow_on_work
    identity_created
    identity_authorized
    coupling_assigned_to_relation
    coupling_assigned_to_first_crossing_a
    coupling_assigned_to_first_crossing_b
    coupling_assigned_to_descendant_body_a
    coupling_assigned_to_descendant_body_b
    coupling_assigned_to_candidate_a
    coupling_assigned_to_candidate_b
    coupling_created
    field_machinery_created
    runtime_created
    api_created
    currentness_created
    authority_created
    standing_created
    output_authorized
    action_authorized
    derivative_reception_authorized
    synchronization_authorized
    follow_on_authorized
    follow_on_work_authorized
    relation_dissolution_authorized
    relation_dissolution_performed
    relation_reversed
    relation_terminated
    relation_erased
    relation_mutated
    relation_invalidated
    relation_punished
    relation_teardown_created
    living_relation_state_created
    living_relation_state_lapsed
    living_relation_state_dissolved
    historical_receipt_preservation_authorized
    historical_receipt_preserved
    third_candidate_created
    third_model_admitted
    standing_descendant_created
    descendant_standing_check_performed
    prior_unsupported_candidate_a_claim_validated
    prior_unsupported_candidate_b_claim_validated
    prior_unsupported_derivation_event_claim_validated
    valid_derivation_event_recorded
    affected_file_repaired
    affected_file_edited
    affected_file_deleted
    affected_file_overwritten
    affected_file_replaced
    affected_file_redeemed
    affected_file_treated_as_clean_basis
    contaminated_lineage_treated_as_clean_basis
    presence_boundary_overridden
    presence_boundary_bypassed
    presence_boundary_invalidated
    relation_lapse_operation_overridden
    relation_lapse_operation_bypassed
    relation_lapse_operation_invalidated
    relation_operation_overridden
    relation_operation_bypassed
    relation_operation_invalidated
    relation_record_erased
    relation_record_mutated
    scan_performed
    repository_scan_performed
    file_discovery_performed
    repair_performed
    validation_enforced
    hidden_repair_performed
    silent_overwrite_performed
    direct_presence_operation_spec_to_presence_supported
    repo_local_execution_to_presence_supported
    operator_only_attestation_to_presence_supported
    derivative_rendering_attestation_to_presence_supported
    same_custody_countersignature_to_presence_supported
    automatic_acknowledgement_to_presence_supported
    generated_affirmation_to_presence_supported
    forged_receiver_attestation_to_presence_supported
    non_refusable_answer_to_presence_supported
    answer_that_could_not_have_been_withheld_to_presence_supported
    declaring_side_controlled_receiver_basis_to_presence_supported
    direct_presence_boundary_to_presence_support
    direct_relation_lapse_operation_to_presence_support
    direct_historical_relation_record_to_presence_support
    direct_relation_001_to_presence_support
    direct_presence_operation_to_identity
    direct_presence_operation_to_coupling_assignment
    direct_presence_operation_to_coupling_creation
    direct_presence_operation_to_field_machinery
    direct_presence_operation_to_runtime
    direct_presence_operation_to_api
    direct_presence_operation_to_authority_currentness
    direct_presence_operation_to_standing
    direct_presence_operation_to_output_authorization
    direct_presence_operation_to_action_authorization
    direct_presence_operation_to_derivative_reception
    direct_presence_operation_to_synchronization
    direct_presence_operation_to_follow_on_work
    direct_presence_operation_to_relation_dissolution
    direct_presence_operation_to_relation_reversal
    direct_presence_operation_to_relation_termination
    direct_presence_operation_to_relation_erasure
    direct_presence_operation_to_relation_mutation
    direct_presence_operation_to_relation_invalidation
    direct_presence_operation_to_punitive_interpretation
    direct_presence_operation_to_teardown_logic
    direct_presence_operation_to_living_relation_state
    direct_presence_operation_to_historical_receipt_preservation
    """.split()
)

BLOCK_CODES = tuple(
    """
    REQUEST_NOT_MAPPING
    REQUEST_PATH_UNREADABLE
    REQUEST_JSON_INVALID
    UNSUPPORTED_INTENT
    REQUEST_VALUE_MISMATCH
    RESULT_POSTURE_PRECLAIMED
    PRESENCE_OPERATION_SPEC_REFERENCE_MISSING
    PRESENCE_OPERATION_SPEC_MARKER_MISSING
    PRESENCE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING
    PRESENCE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING
    RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING
    RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING
    RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING
    RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING
    RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING
    RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING
    RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING
    RELATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING
    FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING
    FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING
    EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING
    EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING
    RECEIVER_ANSWERABLE_BASIS_MISSING_OR_INSUFFICIENT
    NON_CLAIM_MISSING_OR_FLIPPED
    PROHIBITED_SELF_SATISFYING_PRESENCE_REQUESTED
    PROHIBITED_REPO_LOCAL_PRESENCE_SUPPORT_REQUESTED
    PROHIBITED_OPERATOR_ONLY_ATTESTATION_REQUESTED
    PROHIBITED_DERIVATIVE_RENDERING_ATTESTATION_REQUESTED
    PROHIBITED_SAME_CUSTODY_COUNTERSIGNATURE_REQUESTED
    PROHIBITED_AUTOMATIC_ACKNOWLEDGEMENT_REQUESTED
    PROHIBITED_GENERATED_AFFIRMATION_REQUESTED
    PROHIBITED_FORGED_RECEIVER_ATTESTATION_REQUESTED
    PROHIBITED_NON_REFUSABLE_ANSWER_REQUESTED
    PROHIBITED_DECLARING_SIDE_CONTROLLED_BASIS_REQUESTED
    PROHIBITED_IDENTITY_REQUESTED
    PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED
    PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED
    PROHIBITED_STANDING_REQUESTED
    PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED
    PROHIBITED_RELATION_DISSOLUTION_REQUESTED
    PROHIBITED_RELATION_REVERSAL_OR_TERMINATION_REQUESTED
    PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED
    PROHIBITED_PUNITIVE_LAPSE_OR_TEARDOWN_REQUESTED
    PROHIBITED_LIVING_RELATION_STATE_REQUESTED
    PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED
    PROHIBITED_STANDING_DESCENDANT_REQUESTED
    PROHIBITED_DESCENDANT_STANDING_REQUESTED
    PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED
    PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED
    EXPLICIT_BLOCK_REQUESTED
    WRITE_REFUSED
    """.split()
)

PROHIBITED_REQUEST_FLAGS = {
    "request_presence_support_without_receiver_answerable_basis": (
        "PROHIBITED_SELF_SATISFYING_PRESENCE_REQUESTED"
    ),
    "request_presence_support_by_repo_local_execution": (
        "PROHIBITED_REPO_LOCAL_PRESENCE_SUPPORT_REQUESTED"
    ),
    "request_presence_support_by_operator_only_attestation": (
        "PROHIBITED_OPERATOR_ONLY_ATTESTATION_REQUESTED"
    ),
    "request_presence_support_by_derivative_rendering": (
        "PROHIBITED_DERIVATIVE_RENDERING_ATTESTATION_REQUESTED"
    ),
    "request_presence_support_by_same_custody_countersignature": (
        "PROHIBITED_SAME_CUSTODY_COUNTERSIGNATURE_REQUESTED"
    ),
    "request_presence_support_by_automatic_acknowledgement": (
        "PROHIBITED_AUTOMATIC_ACKNOWLEDGEMENT_REQUESTED"
    ),
    "request_presence_support_by_generated_affirmation": (
        "PROHIBITED_GENERATED_AFFIRMATION_REQUESTED"
    ),
    "request_presence_support_by_forged_receiver_attestation": (
        "PROHIBITED_FORGED_RECEIVER_ATTESTATION_REQUESTED"
    ),
    "request_presence_support_by_non_refusable_answer": (
        "PROHIBITED_NON_REFUSABLE_ANSWER_REQUESTED"
    ),
    "request_presence_support_by_declaring_side_controlled_basis": (
        "PROHIBITED_DECLARING_SIDE_CONTROLLED_BASIS_REQUESTED"
    ),
    "request_identity_creation": "PROHIBITED_IDENTITY_REQUESTED",
    "request_identity_authorization": "PROHIBITED_IDENTITY_REQUESTED",
    "request_coupling_assignment_to_relation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_first_crossing_a": (
        "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    ),
    "request_coupling_assignment_to_first_crossing_b": (
        "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    ),
    "request_coupling_assignment_to_descendant_body_a": (
        "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    ),
    "request_coupling_assignment_to_descendant_body_b": (
        "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    ),
    "request_coupling_assignment_to_candidate_a": (
        "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    ),
    "request_coupling_assignment_to_candidate_b": (
        "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    ),
    "request_coupling_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_STANDING_REQUESTED",
    "request_output_authorization": "PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED",
    "request_action_authorization": "PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED",
    "request_derivative_reception_authorization": (
        "PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED"
    ),
    "request_synchronization_authorization": (
        "PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED"
    ),
    "request_relation_dissolution_authorization": "PROHIBITED_RELATION_DISSOLUTION_REQUESTED",
    "request_relation_dissolution_performed": "PROHIBITED_RELATION_DISSOLUTION_REQUESTED",
    "request_relation_reversal": "PROHIBITED_RELATION_REVERSAL_OR_TERMINATION_REQUESTED",
    "request_relation_termination": "PROHIBITED_RELATION_REVERSAL_OR_TERMINATION_REQUESTED",
    "request_relation_erasure": "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED",
    "request_relation_mutation": "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED",
    "request_relation_invalidation": (
        "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED"
    ),
    "request_relation_punishment": "PROHIBITED_PUNITIVE_LAPSE_OR_TEARDOWN_REQUESTED",
    "request_relation_teardown_creation": "PROHIBITED_PUNITIVE_LAPSE_OR_TEARDOWN_REQUESTED",
    "request_living_relation_state_creation": "PROHIBITED_LIVING_RELATION_STATE_REQUESTED",
    "request_living_relation_state_lapse": "PROHIBITED_LIVING_RELATION_STATE_REQUESTED",
    "request_living_relation_state_dissolution": "PROHIBITED_LIVING_RELATION_STATE_REQUESTED",
    "request_historical_receipt_preservation_authorization": (
        "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED"
    ),
    "request_historical_receipt_preservation": (
        "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED"
    ),
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
    "request_prior_unsupported_claim_validation": (
        "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED"
    ),
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
}

BASIS_PROHIBITED_TRUE_CODES = {
    "receiver_answerable_basis_controlled_by_declaring_side": (
        "PROHIBITED_DECLARING_SIDE_CONTROLLED_BASIS_REQUESTED"
    ),
    "operator_only_attestation": "PROHIBITED_OPERATOR_ONLY_ATTESTATION_REQUESTED",
    "derivative_rendering_attestation": "PROHIBITED_DERIVATIVE_RENDERING_ATTESTATION_REQUESTED",
    "same_custody_countersignature": "PROHIBITED_SAME_CUSTODY_COUNTERSIGNATURE_REQUESTED",
    "automatic_acknowledgement": "PROHIBITED_AUTOMATIC_ACKNOWLEDGEMENT_REQUESTED",
    "generated_affirmation": "PROHIBITED_GENERATED_AFFIRMATION_REQUESTED",
    "forged_receiver_attestation": "PROHIBITED_FORGED_RECEIVER_ATTESTATION_REQUESTED",
    "inadmissible_receiver_basis": "RESULT_POSTURE_PRECLAIMED",
}

EXPECTED_REQUEST_VALUES = {
    "operation_id": OPERATION_ID,
    "operation_type": OPERATION_TYPE,
    "operation_version": OPERATION_VERSION,
    "operation_scope": OPERATION_SCOPE,
    "presence_operation_id": OPERATION_ID,
    "presence_operation_type": OPERATION_TYPE,
    "presence_operation_version": OPERATION_VERSION,
    "presence_operation_scope": OPERATION_SCOPE,
    "prior_presence_boundary_type": PRIOR_PRESENCE_BOUNDARY_TYPE,
    "prior_presence_boundary_outcome_required": PRIOR_PRESENCE_BOUNDARY_OUTCOME_REQUIRED,
    "prior_presence_boundary_result_required": PRIOR_PRESENCE_BOUNDARY_RESULT_REQUIRED,
    "prior_presence_operation_consideration_allowed_required": (
        PRIOR_PRESENCE_OPERATION_CONSIDERATION_ALLOWED_REQUIRED
    ),
    "prior_relation_lapse_operation_referenced_required": (
        PRIOR_RELATION_LAPSE_OPERATION_REFERENCED_REQUIRED
    ),
    "prior_relation_record_referenced_required": PRIOR_RELATION_RECORD_REFERENCED_REQUIRED,
    "prior_relation_basis_referenced_required": PRIOR_RELATION_BASIS_REFERENCED_REQUIRED,
    "prior_presence_supported_required": PRIOR_PRESENCE_SUPPORTED_REQUIRED,
    "prior_presence_authorized_required": PRIOR_PRESENCE_AUTHORIZED_REQUIRED,
    "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_presence_recorded_required": PRIOR_PRESENCE_RECORDED_REQUIRED,
    "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
    "prior_identity_authorized_required": PRIOR_IDENTITY_AUTHORIZED_REQUIRED,
    "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
    "prior_field_machinery_created_required": PRIOR_FIELD_MACHINERY_CREATED_REQUIRED,
    "prior_runtime_created_required": PRIOR_RUNTIME_CREATED_REQUIRED,
    "prior_api_created_required": PRIOR_API_CREATED_REQUIRED,
    "prior_currentness_created_required": PRIOR_CURRENTNESS_CREATED_REQUIRED,
    "prior_authority_created_required": PRIOR_AUTHORITY_CREATED_REQUIRED,
    "prior_standing_created_required": PRIOR_STANDING_CREATED_REQUIRED,
    "prior_output_authorized_required": PRIOR_OUTPUT_AUTHORIZED_REQUIRED,
    "prior_action_authorized_required": PRIOR_ACTION_AUTHORIZED_REQUIRED,
    "prior_derivative_reception_authorized_required": (
        PRIOR_DERIVATIVE_RECEPTION_AUTHORIZED_REQUIRED
    ),
    "prior_synchronization_authorized_required": PRIOR_SYNCHRONIZATION_AUTHORIZED_REQUIRED,
    "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
    "prior_follow_on_work_authorized_required": PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED,
    "prior_relation_dissolution_authorized_required": (
        PRIOR_RELATION_DISSOLUTION_AUTHORIZED_REQUIRED
    ),
    "prior_relation_dissolution_performed_required": (
        PRIOR_RELATION_DISSOLUTION_PERFORMED_REQUIRED
    ),
    "prior_relation_reversed_required": PRIOR_RELATION_REVERSED_REQUIRED,
    "prior_relation_terminated_required": PRIOR_RELATION_TERMINATED_REQUIRED,
    "prior_relation_erased_required": PRIOR_RELATION_ERASED_REQUIRED,
    "prior_relation_mutated_required": PRIOR_RELATION_MUTATED_REQUIRED,
    "prior_relation_invalidated_required": PRIOR_RELATION_INVALIDATED_REQUIRED,
    "prior_relation_punished_required": PRIOR_RELATION_PUNISHED_REQUIRED,
    "prior_relation_teardown_created_required": PRIOR_RELATION_TEARDOWN_CREATED_REQUIRED,
    "prior_living_relation_state_created_required": PRIOR_LIVING_RELATION_STATE_CREATED_REQUIRED,
    "prior_living_relation_state_lapsed_required": PRIOR_LIVING_RELATION_STATE_LAPSED_REQUIRED,
    "prior_living_relation_state_dissolved_required": (
        PRIOR_LIVING_RELATION_STATE_DISSOLVED_REQUIRED
    ),
    "prior_historical_receipt_preservation_authorized_required": (
        PRIOR_HISTORICAL_RECEIPT_PRESERVATION_AUTHORIZED_REQUIRED
    ),
    "prior_historical_receipt_preserved_required": PRIOR_HISTORICAL_RECEIPT_PRESERVED_REQUIRED,
    "prior_third_candidate_created_required": PRIOR_THIRD_CANDIDATE_CREATED_REQUIRED,
    "prior_third_model_admitted_required": PRIOR_THIRD_MODEL_ADMITTED_REQUIRED,
    "prior_standing_descendant_created_required": PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED,
    "prior_descendant_standing_check_performed_required": (
        PRIOR_DESCENDANT_STANDING_CHECK_PERFORMED_REQUIRED
    ),
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
    "receiver_answerable_basis_id": RECEIVER_ANSWERABLE_BASIS_ID,
    "receiver_answerable_basis_type": RECEIVER_ANSWERABLE_BASIS_TYPE,
    "receiver_answerable_basis_scope": RECEIVER_ANSWERABLE_BASIS_SCOPE,
}

TARGET_SPEC_MARKER_CLASSES = (
    (
        "operation identity",
        (("Presence Operation V0 Minimum Specification", OPERATION_TYPE, OPERATION_ID, OPERATION_SCOPE),),
    ),
    (
        "boundary allowance",
        ((
            "PRESENCE_BOUNDARY_ALLOWED",
            "PRESENCE_OPERATION_CONSIDERATION_ALLOWED",
            "presence_operation_consideration_allowed = true",
            "relation_lapse_operation_referenced = true",
            "relation_record_referenced = true",
            "relation_basis_referenced = true",
            "presence_supported = false",
            "presence_authorized = false",
            "presence_established = false",
            "presence_recorded = false",
            "identity_created = false",
            "identity_authorized = false",
            "coupling_created = false",
            "field_machinery_created = false",
            "runtime_created = false",
            "api_created = false",
            "currentness_created = false",
            "authority_created = false",
            "standing_created = false",
            "output_authorized = false",
            "action_authorized = false",
            "derivative_reception_authorized = false",
            "synchronization_authorized = false",
            "follow_on_authorized = false",
            "follow_on_work_authorized = false",
        ),),
    ),
    (
        "receiver-side answerable basis",
        ((
            RECEIVER_ANSWERABLE_BASIS_TYPE,
            RECEIVER_ANSWERABLE_BASIS_SCOPE,
            "receiver_attested = false",
            "receiver_answerable_receipt_present = false",
            "receiver_answerable_basis_custody_distinct = false",
            "receiver_answerable_basis_controlled_by_declaring_side = false",
            "receiver_answerable_basis_refusable = false",
            "receiver_answerable_basis_could_have_been_withheld = false",
            "repo_local_execution_only = true",
            "receiver_attestation_required = true",
        ),),
    ),
    (
        "receiver insufficiency",
        ((
            "repo-local execution alone is insufficient",
            "operator-only attestation",
            "derivative rendering",
            "same-custody countersignature",
            "automatic acknowledgement",
            "generated affirmation",
            "forged receiver attestation",
            "answer controlled by the declaring side",
            "answer that could not have been withheld",
            "Presence support requires receiver-side answerable basis",
            "An answerable basis that could not have been withheld is not an answer",
            OUTCOME_REQUIRES_RECEIVER_ATTESTATION,
            "not failure",
            "not blocked",
            "not support",
            "lawful waiting state",
        ),),
    ),
    (
        "presence support admissibility",
        ((
            PRESENCE_RESULT,
            "receiver_attested = true",
            "receiver_answerable_receipt_present = true",
            "receiver_answerable_basis_custody_distinct = true",
            "receiver_answerable_basis_controlled_by_declaring_side = false",
            "receiver_answerable_basis_refusable = true",
            "receiver_answerable_basis_could_have_been_withheld = true",
            "repo_local_execution_only = false",
            "operator_only_attestation = false",
            "derivative_rendering_attestation = false",
            "same_custody_countersignature = false",
            "automatic_acknowledgement = false",
            "generated_affirmation = false",
            "forged_receiver_attestation = false",
            "inadmissible_receiver_basis = false",
        ),),
    ),
    (
        "presence non-conversion",
        ((
            "Presence is receiver-allocated",
            "Presence cannot be emitted as self-proof",
            "Presence cannot be inherited from relation_001",
            "Presence cannot be inherited from relation lapse",
            "Presence cannot be derived from historical relation record",
            "Presence must be recorded, if ever supported, as a fresh answerable event",
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
            "Presence is not follow-on authorization",
            "Presence is not follow-on work",
        ),),
    ),
    (
        "landlord and rank",
        ((
            "Historical relation record is not presence",
            "Historical relation record is not identity",
            "Historical relation record is not coupling",
            "relation_001 must not become landlord of the between",
            "relation_001 must not outrank First Crossing A",
            "relation_001 must not outrank First Crossing B",
            "relation_001 must not outrank the related first-crossing pair",
            "Coupling remains unassigned unless separately bounded",
            "Coupling must not be treated as third candidate",
            "Coupling must not be treated as third model",
            "No third candidate is admitted",
            "No third model is admitted",
        ),),
    ),
    (
        "separately bounded downstream",
        ((
            "Identity requires a separately bounded operation",
            "Coupling requires a separately bounded operation",
            "FIELD machinery requires a separately bounded operation",
            "Runtime requires a separately bounded operation",
            "API requires a separately bounded operation",
            "Currentness requires a separately bounded operation",
            "Authority requires a separately bounded operation",
            "Standing requires a separately bounded operation",
            "No orphaned state is authorized",
            "No silent reset is authorized",
            "No overwrite is authorized",
        ),),
    ),
    (
        "permitted route",
        ((
            ADMISSIBLE_FUTURE_ROUTE,
            "Only after a future presence operation records PRESENCE_SUPPORTED with admissible "
            "receiver-side answerable basis may a separately bounded identity boundary, coupling "
            "boundary, or later boundary be considered",
            "No identity, coupling, FIELD machinery, runtime, API, currentness, authority, standing, "
            "output, action, derivative reception, synchronization, or later operation is authorized "
            "by this operation specification alone",
        ),),
    ),
    (
        "contaminated lineage preservation",
        ((
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        ),),
    ),
    (
        "blocked route",
        ((
            "direct presence operation spec to PRESENCE_SUPPORTED",
            "repo-local execution to PRESENCE_SUPPORTED",
            "operator-only attestation to PRESENCE_SUPPORTED",
            "derivative rendering attestation to PRESENCE_SUPPORTED",
            "same-custody countersignature to PRESENCE_SUPPORTED",
            "automatic acknowledgement to PRESENCE_SUPPORTED",
            "generated affirmation to PRESENCE_SUPPORTED",
            "forged receiver attestation to PRESENCE_SUPPORTED",
            "non-refusable answer to PRESENCE_SUPPORTED",
            "answer that could not have been withheld to PRESENCE_SUPPORTED",
            "declaring-side-controlled receiver basis to PRESENCE_SUPPORTED",
            "direct presence boundary to presence support",
            "direct relation lapse operation to presence support",
            "direct historical relation record to presence support",
            "direct relation_001 to presence support",
            "direct presence operation to identity",
            "direct presence operation to coupling assignment",
            "direct presence operation to coupling creation",
            "direct presence operation to FIELD machinery",
            "direct presence operation to runtime",
            "direct presence operation to API",
            "direct presence operation to authority/currentness",
            "direct presence operation to standing",
            "direct presence operation to output authorization",
            "direct presence operation to action authorization",
            "direct presence operation to derivative reception",
            "direct presence operation to synchronization",
            "direct presence operation to follow-on work",
            "direct presence operation to relation dissolution",
            "direct presence operation to relation reversal",
            "direct presence operation to relation termination",
            "direct presence operation to relation erasure",
            "direct presence operation to relation mutation",
            "direct presence operation to relation invalidation",
            "direct presence operation to punitive interpretation",
            "direct presence operation to teardown logic",
            "direct presence operation to living relation state",
            "direct presence operation to historical receipt preservation",
            "repository scan route",
            "file discovery route",
            "affected-file repair route",
            "prior unsupported-claim validation route",
        ),),
    ),
    (
        "closing lock",
        ((
            "This operation spec defines only a future presence operation shape",
            "It does not itself execute presence or record an operation result",
            "Presence operation is not self-satisfying",
            "Presence support cannot be recorded from repo-local execution alone, operator-only "
            "attestation, derivative rendering, same-custody countersignature, automatic "
            "acknowledgement, generated affirmation, or any answerable basis controlled by the declaring side",
            "Presence support requires receiver-side answerable basis that is custody-distinct, not "
            "controlled by the declaring side, refusable, and capable of being withheld",
            "Until admissible receiver-side answerable basis is supplied, a future presence operation "
            "must record PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION rather than PRESENCE_SUPPORTED",
            "PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION is not failure, not blocked, and not support",
            "Presence is receiver-allocated and cannot be emitted as self-proof, inherited from "
            "relation_001, inherited from relation lapse, or derived from historical relation record",
            "Presence must be recorded, if ever supported, as a fresh answerable event",
            "Open means not scheduled, not authorized, and not executed",
        ),),
    ),
)

PRESENCE_BOUNDARY_TERMINAL_SUMMARY_MARKERS = (
    "PRESENCE_BOUNDARY_ALLOWED",
    "failed_check_count = 0",
    "passed_check_count = 381",
    "PRESENCE_OPERATION_CONSIDERATION_ALLOWED",
    "presence_operation_consideration_allowed = true",
    "relation_lapse_operation_referenced = true",
    "relation_record_referenced = true",
    "relation_basis_referenced = true",
    "presence_supported = false",
    "presence_authorized = false",
    "presence_established = false",
    "presence_recorded = false",
    "identity_created = false",
    "identity_authorized = false",
    "coupling_created = false",
    "field_machinery_created = false",
    "runtime_created = false",
    "api_created = false",
    "currentness_created = false",
    "authority_created = false",
    "standing_created = false",
    "output_authorized = false",
    "action_authorized = false",
    "derivative_reception_authorized = false",
    "synchronization_authorized = false",
    "follow_on_authorized = false",
    "follow_on_work_authorized = false",
)

UPSTREAM_REQUIREMENTS = (
    (
        "presence_boundary_terminal_summary_reference",
        DEFAULT_PRESENCE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "PRESENCE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "PRESENCE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        (PRESENCE_BOUNDARY_TERMINAL_SUMMARY_MARKERS,),
        "completed_presence_boundary_terminal_summary_markers_present",
    ),
    (
        "relation_lapse_operation_terminal_summary_reference",
        DEFAULT_RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("RELATION_LAPSE_OPERATION_RECORDED", "RELATION_LAPSE_SUPPORTED"),),
        "completed_relation_lapse_operation_terminal_summary_markers_present",
    ),
    (
        "relation_lapse_boundary_terminal_summary_reference",
        DEFAULT_RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        (("RELATION_LAPSE_BOUNDARY_ALLOWED", "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED"),),
        "completed_relation_lapse_boundary_terminal_summary_markers_present",
    ),
    (
        "relation_reversibility_operation_terminal_summary_reference",
        DEFAULT_RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("RELATION_REVERSIBILITY_OPERATION_RECORDED", "RELATION_REVERSIBILITY_SUPPORTED"),),
        "completed_relation_reversibility_operation_terminal_summary_markers_present",
    ),
    (
        "relation_operation_terminal_summary_reference",
        DEFAULT_RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RELATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("RELATION_OPERATION_RECORDED", "RELATION_SUPPORTED"),),
        "completed_relation_operation_terminal_summary_markers_present",
    ),
    (
        "first_crossing_operation_v2_terminal_summary_reference",
        DEFAULT_FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE,
        "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING",
        (("FIRST_CROSSING_SUPPORTED",),),
        "completed_first_crossing_operation_v2_terminal_summary_markers_present",
    ),
    (
        "existence_claim_evidence_check_terminal_summary_reference",
        DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE,
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
        (("UNSUPPORTED",),),
        "existence_claim_evidence_check_terminal_summary_markers_present",
    ),
)

BLOCKED_ROUTES = (
    "direct presence operation spec to PRESENCE_SUPPORTED",
    "repo-local execution to PRESENCE_SUPPORTED",
    "operator-only attestation to PRESENCE_SUPPORTED",
    "derivative rendering attestation to PRESENCE_SUPPORTED",
    "same-custody countersignature to PRESENCE_SUPPORTED",
    "automatic acknowledgement to PRESENCE_SUPPORTED",
    "generated affirmation to PRESENCE_SUPPORTED",
    "forged receiver attestation to PRESENCE_SUPPORTED",
    "non-refusable answer to PRESENCE_SUPPORTED",
    "answer that could not have been withheld to PRESENCE_SUPPORTED",
    "declaring-side-controlled receiver basis to PRESENCE_SUPPORTED",
    "direct presence boundary to presence support",
    "direct relation lapse operation to presence support",
    "direct historical relation record to presence support",
    "direct relation_001 to presence support",
    "direct presence operation to identity",
    "direct presence operation to coupling assignment",
    "direct presence operation to coupling creation",
    "direct presence operation to FIELD machinery",
    "direct presence operation to runtime",
    "direct presence operation to API",
    "direct presence operation to authority/currentness",
    "direct presence operation to standing",
    "direct presence operation to output authorization",
    "direct presence operation to action authorization",
    "direct presence operation to derivative reception",
    "direct presence operation to synchronization",
    "direct presence operation to follow-on work",
    "direct presence operation to relation dissolution",
    "direct presence operation to relation reversal",
    "direct presence operation to relation termination",
    "direct presence operation to relation erasure",
    "direct presence operation to relation mutation",
    "direct presence operation to relation invalidation",
    "direct presence operation to punitive interpretation",
    "direct presence operation to teardown logic",
    "direct presence operation to living relation state",
    "direct presence operation to historical receipt preservation",
    "repository scan route",
    "file discovery route",
    "affected-file repair route",
    "prior unsupported-claim validation route",
)

WHAT_REMAINS_OPEN = (
    "presence operation test",
    "presence operation live artifact",
    "actual presence operation",
    "receiver-side answerable basis, if separately supplied",
    "receiver-side answerable basis custody check",
    "receiver-side answerable basis refusability check",
    "receiver-side answerable basis could-have-been-withheld check",
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

SUMMARY_POSTURE_FIELDS = (
    "presence_operation_recorded",
    "presence_evaluation_performed",
    "presence_result_recorded",
    "presence_result",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "presence_operation_requires_receiver_attestation",
    "receiver_attestation_required",
    "receiver_answerable_basis_required",
    "receiver_attested",
    "receiver_answerable_receipt_present",
    "receiver_answerable_basis_custody_distinct",
    "receiver_answerable_basis_controlled_by_declaring_side",
    "receiver_answerable_basis_refusable",
    "receiver_answerable_basis_could_have_been_withheld",
    "repo_local_execution_only",
    "relation_record_referenced",
    "relation_basis_referenced",
    "presence_boundary_referenced",
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


def _normalize_marker_text(value: str) -> str:
    return " ".join(value.casefold().replace("`", "").split())


def _markers_present(text: str | None, variants: tuple[tuple[str, ...], ...]) -> bool:
    if text is None:
        return False
    normalized = _normalize_marker_text(text)
    return any(
        all(_normalize_marker_text(marker) in normalized for marker in group)
        for group in variants
    )


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
        if isinstance(item.get("check_name"), str)
        and str(item["check_name"]).endswith("markers present")
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
    failure: str | None = None
    for flag, code in PROHIBITED_REQUEST_FLAGS.items():
        actual = request.get(flag)
        passed = actual is not True
        _add_check(checks, f"prohibited request {flag}", passed, False, actual, code)
        if not passed and failure is None:
            failure = code

    for field, code in BASIS_PROHIBITED_TRUE_CODES.items():
        actual = request.get(field)
        passed = actual is not True
        _add_check(checks, f"prohibited receiver basis {field}", passed, False, actual, code)
        if not passed and failure is None:
            failure = code

    for field in PURE_OUTPUT_PRECLAIM_FIELDS:
        if field not in request:
            continue
        actual = request[field]
        passed = actual is not True
        _add_check(
            checks,
            f"top-level output preclaim {field}",
            passed,
            False,
            actual,
            "RESULT_POSTURE_PRECLAIMED",
        )
        if not passed and failure is None:
            failure = "RESULT_POSTURE_PRECLAIMED"

    exempt = ADMISSIBLE_RECEIVER_TRUE_INPUT_FIELDS | set(BASIS_PROHIBITED_TRUE_CODES)
    for field in REQUIRED_FALSE_NON_CLAIMS:
        if field not in request or field in exempt:
            continue
        actual = request[field]
        passed = actual is not True
        _add_check(
            checks,
            f"top-level false posture {field}",
            passed,
            False,
            actual,
            "RESULT_POSTURE_PRECLAIMED",
        )
        if not passed and failure is None:
            failure = "RESULT_POSTURE_PRECLAIMED"
    return failure


def _validate_target_spec(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> str | None:
    reference = request.get("presence_operation_spec_reference")
    text = _read_text(reference)
    _add_check(
        checks,
        "presence operation specification reference readable",
        text is not None,
        "readable Markdown file",
        reference,
        "PRESENCE_OPERATION_SPEC_REFERENCE_MISSING",
    )
    if text is None:
        return "PRESENCE_OPERATION_SPEC_REFERENCE_MISSING"
    failure: str | None = None
    for name, variants in TARGET_SPEC_MARKER_CLASSES:
        passed = _markers_present(text, variants)
        _add_check(
            checks,
            f"presence operation specification {name} markers present",
            passed,
            "posture marker class present",
            passed,
            "PRESENCE_OPERATION_SPEC_MARKER_MISSING",
        )
        if not passed and failure is None:
            failure = "PRESENCE_OPERATION_SPEC_MARKER_MISSING"
    return failure


def _validate_upstream(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> str | None:
    failure: str | None = None
    for field, _, missing_code, marker_code, variants, flag in UPSTREAM_REQUIREMENTS:
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
            if failure is None:
                failure = missing_code
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
        if not passed and failure is None:
            failure = marker_code
    return failure


def _receiver_basis_values(request: Mapping[str, Any]) -> dict[str, Any]:
    return {field: request.get(field) for field in RECEIVER_BASIS_FIELDS}


def _receiver_basis_missing(request: Mapping[str, Any]) -> list[str]:
    requirements = (
        ("receiver_attested", True),
        ("receiver_answerable_receipt_present", True),
        ("receiver_answerable_basis_custody_distinct", True),
        ("receiver_answerable_basis_controlled_by_declaring_side", False),
        ("receiver_answerable_basis_refusable", True),
        ("receiver_answerable_basis_could_have_been_withheld", True),
        ("repo_local_execution_only", False),
        ("operator_only_attestation", False),
        ("derivative_rendering_attestation", False),
        ("same_custody_countersignature", False),
        ("automatic_acknowledgement", False),
        ("generated_affirmation", False),
        ("forged_receiver_attestation", False),
        ("inadmissible_receiver_basis", False),
    )
    return [field for field, expected in requirements if request.get(field) is not expected]


def _presence_result_for_outcome(outcome: str) -> str:
    if outcome == OUTCOME_SUPPORTED:
        return PRESENCE_RESULT
    if outcome == OUTCOME_REQUIRES_RECEIVER_ATTESTATION:
        return "REQUIRES_RECEIVER_ATTESTATION"
    return "NOT_EVALUATED"


def _operation_object(outcome: str, missing_receiver_basis: list[str]) -> dict[str, Any]:
    operation = {
        **EXPECTED_REQUEST_VALUES,
        "presence_result": _presence_result_for_outcome(outcome),
        "presence_operation_requires_receiver_attestation": False,
        "receiver_attestation_required": False,
        "receiver_answerable_basis_required": False,
        "repo_local_execution_only": False,
        "relation_record_referenced": False,
        "relation_basis_referenced": False,
        "presence_boundary_referenced": False,
        "missing_or_insufficient_receiver_answerable_basis": list(missing_receiver_basis),
    }
    operation.update({field: False for field in REQUIRED_FALSE_NON_CLAIMS})
    if outcome == OUTCOME_REQUIRES_RECEIVER_ATTESTATION:
        operation.update(
            {field: True for field in ALLOWED_TRUE_REQUIRES_RECEIVER_ATTESTATION_FIELDS}
        )
    elif outcome == OUTCOME_SUPPORTED:
        operation.update({field: True for field in ALLOWED_TRUE_SUPPORTED_FIELDS})
    return operation


def _presence_boundary_reference(boundary_allowed: bool) -> dict[str, Any]:
    return {
        "prior_presence_boundary_type": PRIOR_PRESENCE_BOUNDARY_TYPE,
        "prior_presence_boundary_outcome": PRIOR_PRESENCE_BOUNDARY_OUTCOME_REQUIRED,
        "prior_presence_boundary_result": PRIOR_PRESENCE_BOUNDARY_RESULT_REQUIRED,
        "prior_presence_operation_consideration_allowed": boundary_allowed,
        "prior_relation_lapse_operation_referenced": boundary_allowed,
        "prior_relation_record_referenced": boundary_allowed,
        "prior_relation_basis_referenced": boundary_allowed,
        "prior_presence_supported": False,
        "prior_presence_authorized": False,
        "prior_presence_established": False,
        "prior_presence_recorded": False,
        "prior_identity_created": False,
        "prior_identity_authorized": False,
        "prior_coupling_created": False,
        "prior_field_machinery_created": False,
        "prior_runtime_created": False,
        "prior_api_created": False,
        "prior_currentness_created": False,
        "prior_authority_created": False,
        "prior_standing_created": False,
        "prior_output_authorized": False,
        "prior_action_authorized": False,
        "prior_derivative_reception_authorized": False,
        "prior_synchronization_authorized": False,
        "prior_follow_on_authorized": False,
        "prior_follow_on_work_authorized": False,
    }


def _operation_material(
    request: Mapping[str, Any],
    operation: Mapping[str, Any],
    missing_receiver_basis: list[str],
    boundary_allowed: bool,
) -> dict[str, Any]:
    receiver_evaluation = {
        "receiver_answerable_basis_id": RECEIVER_ANSWERABLE_BASIS_ID,
        "receiver_answerable_basis_type": RECEIVER_ANSWERABLE_BASIS_TYPE,
        "receiver_answerable_basis_scope": RECEIVER_ANSWERABLE_BASIS_SCOPE,
        "receiver_attestation_required": True,
        "receiver_answerable_basis_required": True,
        **_receiver_basis_values(request),
        "missing_or_insufficient_receiver_answerable_basis": list(missing_receiver_basis),
    }
    presence_evaluation_fields = (
        "presence_operation_requires_receiver_attestation",
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
        "presence_is_identity",
        "presence_is_coupling",
        "presence_is_field_machinery",
        "presence_is_runtime",
        "presence_is_api",
        "presence_is_currentness",
        "presence_is_authority",
        "presence_is_standing",
        "presence_is_output_authorization",
        "presence_is_action_authorization",
        "presence_is_derivative_reception",
        "presence_is_synchronization",
        "presence_is_follow_on_authorization",
        "presence_is_follow_on_work",
    )
    return {
        "presence_boundary_reference": _presence_boundary_reference(boundary_allowed),
        "receiver_answerable_basis_evaluation": receiver_evaluation,
        "presence_result_evaluation": {
            "presence_id": PRESENCE_ID,
            "presence_scope": PRESENCE_SCOPE,
            "presence_result": operation.get("presence_result"),
            **{field: operation.get(field) for field in presence_evaluation_fields},
        },
    }


def _declared_basis_projection(request: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "intent",
        *EXPECTED_REQUEST_VALUES,
        "presence_operation_spec_reference",
        *(item[0] for item in UPSTREAM_REQUIREMENTS),
        *RECEIVER_BASIS_FIELDS,
        *PROHIBITED_REQUEST_FLAGS,
    )
    return {key: _json_ready(request.get(key)) for key in keys}


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("presence_operation")
    operation_map = operation if isinstance(operation, Mapping) else {}
    checks = result.get("presence_operation_checks")
    records = checks if isinstance(checks, list) else []
    detail = result.get("operation_result_detail")
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
        "operation_id": operation_map.get("operation_id"),
        "operation_type": operation_map.get("operation_type"),
        "operation_version": operation_map.get("operation_version"),
        "operation_scope": operation_map.get("operation_scope"),
        "prior_presence_boundary_type": operation_map.get("prior_presence_boundary_type"),
        "prior_presence_boundary_outcome_required": operation_map.get(
            "prior_presence_boundary_outcome_required"
        ),
        "prior_presence_boundary_result_required": operation_map.get(
            "prior_presence_boundary_result_required"
        ),
        "prior_presence_operation_consideration_allowed_required": operation_map.get(
            "prior_presence_operation_consideration_allowed_required"
        ),
        "relation_id": operation_map.get("relation_id"),
        "relation_pair_scope": operation_map.get("relation_pair_scope"),
        "selected_presence_operation_spec_path": upstream_map.get(
            "presence_operation_spec_reference"
        ),
        "completed_presence_boundary_terminal_summary_path": upstream_map.get(
            "presence_boundary_terminal_summary_reference"
        ),
        "missing_or_insufficient_receiver_answerable_basis": list(
            detail_map.get("missing_or_insufficient_receiver_answerable_basis", [])
        ),
        "not_recorded_reasons": list(detail_map.get("not_recorded_reasons", [])),
    }
    summary.update({field: operation_map.get(field) for field in SUMMARY_POSTURE_FIELDS})
    summary.update(_marker_flags([item for item in records if isinstance(item, Mapping)]))
    return _json_ready(summary)


def build_presence_operation_v0_min_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build the compact JSON-safe summary for one presence operation."""
    return _build_summary(result)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_receiver_basis: list[str] | None = None,
    not_recorded: list[str] | None = None,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    missing = (
        list(missing_receiver_basis)
        if missing_receiver_basis is not None
        else _receiver_basis_missing(request)
    )
    operation = _operation_object(outcome, missing)
    flags = _marker_flags(checks)
    boundary_allowed = outcome in {
        OUTCOME_SUPPORTED,
        OUTCOME_REQUIRES_RECEIVER_ATTESTATION,
        OUTCOME_NOT_RECORDED,
    }
    result: dict[str, Any] = {
        "presence_operation_metadata": {
            "operation_id": OPERATION_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_presence_operation_basis": _declared_basis_projection(request),
        "upstream_basis": {
            "presence_operation_spec_reference": request.get("presence_operation_spec_reference"),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **flags,
        },
        "presence_operation": operation,
        "presence_operation_material": _operation_material(
            request, operation, missing, boundary_allowed
        ),
        "presence_operation_checks": checks,
        "presence_operation_statement": {
            "outcome": outcome,
            "presence_result": operation["presence_result"],
            "presence_operation_recorded": operation["presence_operation_recorded"],
            "presence_evaluation_performed": operation["presence_evaluation_performed"],
            "presence_result_recorded": operation["presence_result_recorded"],
            "presence_supported": operation["presence_supported"],
            "presence_operation_requires_receiver_attestation": operation[
                "presence_operation_requires_receiver_attestation"
            ],
            "result_level_non_claims_canonical_false": True,
        },
        "presence_operation_non_meaning": {
            "not_identity": True,
            "not_coupling": True,
            "not_field_machinery": True,
            "not_runtime": True,
            "not_api": True,
            "not_currentness": True,
            "not_authority": True,
            "not_standing": True,
            "not_output_authorization": True,
            "not_action_authorization": True,
            "not_derivative_reception": True,
            "not_synchronization": True,
            "not_follow_on_authorization": True,
            "not_follow_on_work": True,
            "not_relation_dissolution": True,
            "not_relation_reversal": True,
            "not_relation_termination": True,
            "not_relation_erasure": True,
            "not_relation_mutation": True,
            "not_relation_invalidation": True,
            "not_relation_punishment": True,
            "not_teardown": True,
            "not_living_relation_state": True,
            "not_historical_receipt_preservation": True,
            "not_self_proof": True,
        },
        "operation_result_detail": {
            "presence_result": operation["presence_result"],
            "missing_or_insufficient_receiver_answerable_basis": missing,
            "not_recorded_reasons": list(not_recorded or []),
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "presence_supported": operation["presence_supported"],
            "admissible_receiver_answerable_basis_required": True,
            "identity_or_coupling_boundary_consideration_may_follow": (
                outcome == OUTCOME_SUPPORTED
            ),
            "identity_created": False,
            "coupling_created": False,
            "field_machinery_created": False,
            "runtime_created": False,
            "authority_created": False,
            "standing_created": False,
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
    result["presence_operation_summary"] = _build_summary(result)
    return _json_ready(result)


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
        block_code=code,
        block_reason=reason,
    )


def build_presence_operation_v0_min_request(**overrides: Any) -> dict[str, Any]:
    """Build one explicit presence-operation request without discovery."""
    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **EXPECTED_REQUEST_VALUES,
        "presence_operation_spec_reference": DEFAULT_PRESENCE_OPERATION_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        **{field: False for field in REQUIRED_FALSE_NON_CLAIMS},
        **{field: False for field in PURE_OUTPUT_PRECLAIM_FIELDS},
        **RECEIVER_BASIS_DEFAULTS,
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
        "declared_non_claims": _canonical_non_claims(),
    }
    request.update(overrides)
    return request


def build_declared_presence_operation_v0_min_request(**overrides: Any) -> dict[str, Any]:
    """Compatibility wrapper for the declared presence-operation request builder."""
    return build_presence_operation_v0_min_request(**overrides)


def resolve_presence_operation_v0_min(
    declared_presence_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one presence operation without self-satisfying presence support."""
    if declared_presence_operation is None:
        request = build_presence_operation_v0_min_request()
    elif not isinstance(declared_presence_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_presence_operation).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_presence_operation))

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
        return _blocked_result(
            request, checks, "EXPLICIT_BLOCK_REQUESTED", "explicit block intent requested"
        )
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(request, checks, "UNSUPPORTED_INTENT", "intent is unsupported")

    _validate_exact_values(checks, request)
    _validate_declared_non_claims(checks, request)
    posture_failure = _request_posture_failure(checks, request)
    failed = _failed_codes(checks)
    if posture_failure:
        return _blocked_result(request, checks, posture_failure, "request asks for prohibited posture")
    if failed:
        return _blocked_result(request, checks, failed[0], f"blocked by failed check {failed[0]}")

    target_failure = _validate_target_spec(checks, request)
    if target_failure:
        return _blocked_result(
            request,
            checks,
            target_failure,
            "target presence-operation specification is insufficient",
        )

    upstream_failure = _validate_upstream(checks, request)
    if upstream_failure:
        return _blocked_result(
            request,
            checks,
            upstream_failure,
            "required completed boundary or upstream summary is insufficient",
        )

    missing_receiver_basis = _receiver_basis_missing(request)
    _add_check(
        checks,
        "receiver answerable basis evaluation completed",
        True,
        "admissible support basis or lawful waiting state",
        "admissible" if not missing_receiver_basis else list(missing_receiver_basis),
        "RECEIVER_ANSWERABLE_BASIS_MISSING_OR_INSUFFICIENT",
    )

    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(
            request,
            OUTCOME_NOT_RECORDED,
            checks,
            missing_receiver_basis,
            not_recorded=["request_intent_do_not_record"],
        )
    if missing_receiver_basis:
        return _build_result(
            request,
            OUTCOME_REQUIRES_RECEIVER_ATTESTATION,
            checks,
            missing_receiver_basis,
        )
    return _build_result(request, OUTCOME_SUPPORTED, checks, [])


def resolve_presence_operation_v0_min_from_path(
    declared_presence_operation_path: Path | str,
) -> dict[str, Any]:
    """Resolve one explicit JSON presence-operation request without discovery."""
    path = Path(declared_presence_operation_path)
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
        return _blocked_result(
            {}, checks, "REQUEST_PATH_UNREADABLE", "request path is unreadable"
        )
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
    return resolve_presence_operation_v0_min(payload)


def _next_output_path(path: Path) -> Path:
    if path.exists() and path.is_dir():
        raise PresenceOperationV0MinError("WRITE_REFUSED: output path is a directory")
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise PresenceOperationV0MinError(
        "WRITE_REFUSED: no deterministic output suffix available"
    )


def write_presence_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one presence-operation result without overwriting a prior result."""
    if not isinstance(result, Mapping):
        raise PresenceOperationV0MinError("WRITE_REFUSED: result must be a mapping")
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
        raise PresenceOperationV0MinError(f"WRITE_REFUSED: {error}") from error
    return destination
