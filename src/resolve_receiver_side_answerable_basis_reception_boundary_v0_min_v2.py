"""V2 successor for one receiver-side answerable-basis reception consideration.

This resolver records only a local boundary result.  It can allow later
candidate-reception consideration after the completed presence operation's
waiting posture; it never receives or evaluates candidate material, creates
attestation, or creates any runtime, public, or downstream surface.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any


class ReceiverSideAnswerableBasisReceptionBoundaryV0MinV2Error(Exception):
    """Raised when a requested boundary result cannot be written safely."""


RESULT_VERSION = "0.2.0"
RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_reception_boundary_v0_min_v2"

BOUNDARY_ID = "receiver_side_answerable_basis_reception_boundary_001"
BOUNDARY_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = (
    "CONSIDER_ONE_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_AFTER_"
    "PRESENCE_REQUIRES_RECEIVER_ATTESTATION_ONLY"
)
PRIOR_PRESENCE_OPERATION_TYPE = "PRESENCE_OPERATION"
PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED = "PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION"
PRIOR_PRESENCE_RESULT_REQUIRED = "REQUIRES_RECEIVER_ATTESTATION"
PRIOR_PRESENCE_OPERATION_RECORDED_REQUIRED = True
PRIOR_PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION_REQUIRED = True
PRIOR_RECEIVER_ATTESTATION_REQUIRED = True
PRIOR_RECEIVER_ANSWERABLE_BASIS_REQUIRED = True
PRIOR_REPO_LOCAL_EXECUTION_ONLY_REQUIRED = True
PRIOR_PRESENCE_SUPPORTED_REQUIRED = False
PRIOR_PRESENCE_AUTHORIZED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_PRESENCE_RECORDED_REQUIRED = False
PRIOR_RECEIVER_ATTESTED_REQUIRED = False
PRIOR_RECEIVER_ANSWERABLE_RECEIPT_PRESENT_REQUIRED = False
PRIOR_RECEIVER_ANSWERABLE_BASIS_CUSTODY_DISTINCT_REQUIRED = False
PRIOR_RECEIVER_ANSWERABLE_BASIS_REFUSABLE_REQUIRED = False
PRIOR_RECEIVER_ANSWERABLE_BASIS_COULD_HAVE_BEEN_WITHHELD_REQUIRED = False
PRIOR_OPERATOR_ONLY_ATTESTATION_ADMISSIBLE_REQUIRED = False
PRIOR_DERIVATIVE_RENDERING_ADMISSIBLE_REQUIRED = False
PRIOR_SAME_CUSTODY_COUNTERSIGNATURE_ADMISSIBLE_REQUIRED = False
PRIOR_AUTOMATIC_ACKNOWLEDGEMENT_ADMISSIBLE_REQUIRED = False
PRIOR_GENERATED_AFFIRMATION_ADMISSIBLE_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_THEN_"
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_ONLY"
)

OUTCOME_ALLOWED = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_ALLOWED"
OUTCOME_REQUIRES_PRESENCE_WAITING_BASIS = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_"
    "REQUIRES_PRESENCE_WAITING_BASIS"
)
OUTCOME_BLOCKED = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_BLOCKED"
OUTCOME_NOT_RECORDED = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_ALLOWED,
    OUTCOME_REQUIRES_PRESENCE_WAITING_BASIS,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY"
INTENT_BLOCK = "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_receiver_side_answerable_basis_reception_boundary_v0_min_v2"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_reception_boundary_001__"
    "receiver_side_answerable_basis_reception_boundary_v0_min_v2_result.json"
)

DEFAULT_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_SPEC_REFERENCE = (
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_V0_MIN_SPEC.md"
)
DEFAULT_PRESENCE_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/PRESENCE_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_PRESENCE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = "spec/PRESENCE_BOUNDARY_TERMINAL_SUMMARY_V0.md"
DEFAULT_RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)

ALLOWED_TRUE_ALLOWED_FIELDS = (
    "receiver_side_answerable_basis_reception_boundary_recorded",
    "receiver_side_answerable_basis_reception_boundary_result_recorded",
    "receiver_side_answerable_basis_candidate_reception_consideration_allowed",
    "prior_presence_operation_referenced",
    "presence_requires_receiver_attestation_referenced",
    "receiver_answerable_basis_requirement_referenced",
)
ALLOWED_TRUE_RECORDED_FIELDS = ALLOWED_TRUE_ALLOWED_FIELDS

# The tuple mirrors the target specification's preserved non-claim set.  It is
# intentionally explicit: input posture is never widened from incidental text.
REQUIRED_FALSE_NON_CLAIMS = tuple(
    """
receiver_side_answerable_basis_reception_boundary_recorded
receiver_side_answerable_basis_reception_boundary_result_recorded
receiver_side_answerable_basis_candidate_reception_consideration_allowed
prior_presence_operation_referenced
presence_requires_receiver_attestation_referenced
receiver_answerable_basis_requirement_referenced
receiver_side_answerable_basis_candidate_received
receiver_side_answerable_basis_candidate_recorded
receiver_side_answerable_basis_candidate_evaluated
receiver_attestation_created
receiver_attestation_supported
receiver_answerable_receipt_present
receiver_answerable_basis_custody_distinct
receiver_answerable_basis_refusable
receiver_answerable_basis_could_have_been_withheld
presence_supported
presence_authorized
presence_established
presence_recorded
identity_created
relation_created
coupling_assigned
coupling_created
field_machinery_created
runtime_created
api_created
public_interface_created
public_intake_created
mailbox_created
listener_created
queue_created
endpoint_created
shared_intake_lane_created
reusable_route_created
repeated_reception_permission_created
currentness_created
authority_created
standing_created
truth_created
continuity_memory_written
output_authorized
action_authorized
derivative_reception_authorized
synchronization_authorized
follow_on_authorized
follow_on_work_authorized
prior_unsupported_candidate_a_claim_validated
prior_unsupported_candidate_b_claim_validated
prior_unsupported_derivation_event_claim_validated
affected_file_repaired
affected_file_edited
affected_file_deleted
affected_file_overwritten
affected_file_replaced
affected_file_redeemed
affected_file_treated_as_clean_basis
contaminated_lineage_treated_as_clean_basis
repository_scan_performed
file_discovery_performed
repair_performed
validation_enforced
hidden_repair_performed
silent_overwrite_performed
direct_receiver_side_answerable_basis_reception_boundary_to_candidate_reception_completion
direct_receiver_side_answerable_basis_reception_boundary_to_receiver_attestation
direct_receiver_side_answerable_basis_reception_boundary_to_receiver_answerable_receipt
direct_receiver_side_answerable_basis_reception_boundary_to_custody_distinctness_decision
direct_receiver_side_answerable_basis_reception_boundary_to_refusability_decision
direct_receiver_side_answerable_basis_reception_boundary_to_could_have_been_withheld_decision
direct_receiver_side_answerable_basis_reception_boundary_to_presence_support
direct_receiver_side_answerable_basis_reception_boundary_to_presence_authorization
direct_receiver_side_answerable_basis_reception_boundary_to_presence_establishment
direct_receiver_side_answerable_basis_reception_boundary_to_presence_recording
direct_receiver_side_answerable_basis_reception_boundary_to_identity
direct_receiver_side_answerable_basis_reception_boundary_to_relation
direct_receiver_side_answerable_basis_reception_boundary_to_coupling_assignment
direct_receiver_side_answerable_basis_reception_boundary_to_coupling_creation
direct_receiver_side_answerable_basis_reception_boundary_to_field_machinery
direct_receiver_side_answerable_basis_reception_boundary_to_runtime
direct_receiver_side_answerable_basis_reception_boundary_to_api
direct_receiver_side_answerable_basis_reception_boundary_to_public_interface
direct_receiver_side_answerable_basis_reception_boundary_to_public_intake
direct_receiver_side_answerable_basis_reception_boundary_to_mailbox
direct_receiver_side_answerable_basis_reception_boundary_to_listener
direct_receiver_side_answerable_basis_reception_boundary_to_queue
direct_receiver_side_answerable_basis_reception_boundary_to_endpoint
direct_receiver_side_answerable_basis_reception_boundary_to_shared_intake_lane
direct_receiver_side_answerable_basis_reception_boundary_to_reusable_route
direct_receiver_side_answerable_basis_reception_boundary_to_repeated_reception_permission
direct_receiver_side_answerable_basis_reception_boundary_to_currentness
direct_receiver_side_answerable_basis_reception_boundary_to_authority
direct_receiver_side_answerable_basis_reception_boundary_to_standing
direct_receiver_side_answerable_basis_reception_boundary_to_truth_creation
direct_receiver_side_answerable_basis_reception_boundary_to_continuity_memory
direct_receiver_side_answerable_basis_reception_boundary_to_output_authorization
direct_receiver_side_answerable_basis_reception_boundary_to_action_authorization
direct_receiver_side_answerable_basis_reception_boundary_to_derivative_reception
direct_receiver_side_answerable_basis_reception_boundary_to_synchronization
direct_receiver_side_answerable_basis_reception_boundary_to_follow_on_work
direct_presence_operation_to_presence_support_without_receiver_side_answerable_basis_reception_boundary_operation_and_presence_reevaluation
direct_presence_operation_to_receiver_attestation
direct_presence_operation_to_public_interface
repository_access_to_presence
repository_clone_to_presence
repository_read_access_to_understanding
forwarded_derivative_material_to_personal_attestation
generated_affirmation_to_answerable_basis
automatic_acknowledgement_to_answerable_basis
operator_only_statement_to_receiver_side_basis
same_custody_countersignature_to_custody_distinction
no_return_to_failure
silence_to_rejection
silence_to_refusal
silence_to_support
possible_future_return_to_pending_obligation
body_local_reception_to_ownership_of_between
""".split()
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_SPEC_REFERENCE_MISSING",
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_SPEC_MARKER_MISSING",
    "PRESENCE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "PRESENCE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "PRESENCE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "PRESENCE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "PRESENCE_WAITING_BASIS_MISSING_OR_INSUFFICIENT",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PROHIBITED_CANDIDATE_RECEPTION_REQUESTED",
    "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
    "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED",
    "PROHIBITED_CUSTODY_DISTINCTNESS_DECISION_REQUESTED",
    "PROHIBITED_REFUSABILITY_DECISION_REQUESTED",
    "PROHIBITED_COULD_HAVE_BEEN_WITHHELD_DECISION_REQUESTED",
    "PROHIBITED_PRESENCE_SUPPORT_REQUESTED",
    "PROHIBITED_PRESENCE_AUTHORIZATION_OR_RECORDING_REQUESTED",
    "PROHIBITED_IDENTITY_OR_RELATION_REQUESTED",
    "PROHIBITED_COUPLING_REQUESTED",
    "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "PROHIBITED_REUSABLE_OR_REPEATED_RECEPTION_ROUTE_REQUESTED",
    "PROHIBITED_TRUTH_OR_CONTINUITY_MEMORY_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
    "REQUEST_PATH_UNREADABLE",
    "REQUEST_JSON_INVALID",
    "REQUEST_VALUE_MISMATCH",
    "RESULT_POSTURE_PRECLAIMED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_receiver_side_answerable_basis_candidate_reception": "PROHIBITED_CANDIDATE_RECEPTION_REQUESTED",
    "request_receiver_side_answerable_basis_candidate_recording": "PROHIBITED_CANDIDATE_RECEPTION_REQUESTED",
    "request_receiver_attestation_creation": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "request_receiver_attestation_support": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "request_receiver_answerable_receipt_creation": "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
    "request_receiver_side_answerable_basis_candidate_evaluation": "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED",
    "request_custody_distinctness_decision": "PROHIBITED_CUSTODY_DISTINCTNESS_DECISION_REQUESTED",
    "request_refusability_decision": "PROHIBITED_REFUSABILITY_DECISION_REQUESTED",
    "request_could_have_been_withheld_decision": "PROHIBITED_COULD_HAVE_BEEN_WITHHELD_DECISION_REQUESTED",
    "request_presence_support": "PROHIBITED_PRESENCE_SUPPORT_REQUESTED",
    "request_presence_authorization": "PROHIBITED_PRESENCE_AUTHORIZATION_OR_RECORDING_REQUESTED",
    "request_presence_establishment": "PROHIBITED_PRESENCE_AUTHORIZATION_OR_RECORDING_REQUESTED",
    "request_presence_recording": "PROHIBITED_PRESENCE_AUTHORIZATION_OR_RECORDING_REQUESTED",
    "request_identity_creation": "PROHIBITED_IDENTITY_OR_RELATION_REQUESTED",
    "request_relation_creation": "PROHIBITED_IDENTITY_OR_RELATION_REQUESTED",
    "request_coupling_assignment": "PROHIBITED_COUPLING_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_public_interface_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_public_intake_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_mailbox_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_listener_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_queue_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_endpoint_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_shared_intake_lane_creation": "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "request_reusable_route_creation": "PROHIBITED_REUSABLE_OR_REPEATED_RECEPTION_ROUTE_REQUESTED",
    "request_repeated_reception_permission_creation": "PROHIBITED_REUSABLE_OR_REPEATED_RECEPTION_ROUTE_REQUESTED",
    "request_truth_creation": "PROHIBITED_TRUTH_OR_CONTINUITY_MEMORY_REQUESTED",
    "request_continuity_memory_write": "PROHIBITED_TRUTH_OR_CONTINUITY_MEMORY_REQUESTED",
    "request_output_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_action_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_derivative_reception_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
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
    "receiver_side_answerable_basis_reception_boundary_id": BOUNDARY_ID,
    "receiver_side_answerable_basis_reception_boundary_type": BOUNDARY_TYPE,
    "receiver_side_answerable_basis_reception_boundary_version": BOUNDARY_VERSION,
    "receiver_side_answerable_basis_reception_boundary_scope": BOUNDARY_SCOPE,
    "prior_presence_operation_type": PRIOR_PRESENCE_OPERATION_TYPE,
    "prior_presence_operation_outcome_required": PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED,
    "prior_presence_result_required": PRIOR_PRESENCE_RESULT_REQUIRED,
    "prior_presence_operation_recorded_required": PRIOR_PRESENCE_OPERATION_RECORDED_REQUIRED,
    "prior_presence_operation_requires_receiver_attestation_required": (
        PRIOR_PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION_REQUIRED
    ),
    "prior_receiver_attestation_required": PRIOR_RECEIVER_ATTESTATION_REQUIRED,
    "prior_receiver_answerable_basis_required": PRIOR_RECEIVER_ANSWERABLE_BASIS_REQUIRED,
    "prior_repo_local_execution_only_required": PRIOR_REPO_LOCAL_EXECUTION_ONLY_REQUIRED,
    "prior_presence_supported_required": PRIOR_PRESENCE_SUPPORTED_REQUIRED,
    "prior_presence_authorized_required": PRIOR_PRESENCE_AUTHORIZED_REQUIRED,
    "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_presence_recorded_required": PRIOR_PRESENCE_RECORDED_REQUIRED,
    "prior_receiver_attested_required": PRIOR_RECEIVER_ATTESTED_REQUIRED,
    "prior_receiver_answerable_receipt_present_required": (
        PRIOR_RECEIVER_ANSWERABLE_RECEIPT_PRESENT_REQUIRED
    ),
    "prior_receiver_answerable_basis_custody_distinct_required": (
        PRIOR_RECEIVER_ANSWERABLE_BASIS_CUSTODY_DISTINCT_REQUIRED
    ),
    "prior_receiver_answerable_basis_refusable_required": (
        PRIOR_RECEIVER_ANSWERABLE_BASIS_REFUSABLE_REQUIRED
    ),
    "prior_receiver_answerable_basis_could_have_been_withheld_required": (
        PRIOR_RECEIVER_ANSWERABLE_BASIS_COULD_HAVE_BEEN_WITHHELD_REQUIRED
    ),
    "prior_operator_only_attestation_admissible_required": (
        PRIOR_OPERATOR_ONLY_ATTESTATION_ADMISSIBLE_REQUIRED
    ),
    "prior_derivative_rendering_admissible_required": PRIOR_DERIVATIVE_RENDERING_ADMISSIBLE_REQUIRED,
    "prior_same_custody_countersignature_admissible_required": (
        PRIOR_SAME_CUSTODY_COUNTERSIGNATURE_ADMISSIBLE_REQUIRED
    ),
    "prior_automatic_acknowledgement_admissible_required": (
        PRIOR_AUTOMATIC_ACKNOWLEDGEMENT_ADMISSIBLE_REQUIRED
    ),
    "prior_generated_affirmation_admissible_required": PRIOR_GENERATED_AFFIRMATION_ADMISSIBLE_REQUIRED,
    "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
}

PRESENCE_REFERENCE_VALUES = {
    "prior_presence_operation_recorded": PRIOR_PRESENCE_OPERATION_RECORDED_REQUIRED,
    "prior_presence_operation_requires_receiver_attestation": (
        PRIOR_PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION_REQUIRED
    ),
    "prior_receiver_attestation_required": PRIOR_RECEIVER_ATTESTATION_REQUIRED,
    "prior_receiver_answerable_basis_required": PRIOR_RECEIVER_ANSWERABLE_BASIS_REQUIRED,
    "prior_repo_local_execution_only": PRIOR_REPO_LOCAL_EXECUTION_ONLY_REQUIRED,
    "prior_presence_supported": PRIOR_PRESENCE_SUPPORTED_REQUIRED,
    "prior_presence_authorized": PRIOR_PRESENCE_AUTHORIZED_REQUIRED,
    "prior_presence_established": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_presence_recorded": PRIOR_PRESENCE_RECORDED_REQUIRED,
    "prior_receiver_attested": PRIOR_RECEIVER_ATTESTED_REQUIRED,
    "prior_receiver_answerable_receipt_present": PRIOR_RECEIVER_ANSWERABLE_RECEIPT_PRESENT_REQUIRED,
    "prior_receiver_answerable_basis_custody_distinct": (
        PRIOR_RECEIVER_ANSWERABLE_BASIS_CUSTODY_DISTINCT_REQUIRED
    ),
    "prior_receiver_answerable_basis_refusable": PRIOR_RECEIVER_ANSWERABLE_BASIS_REFUSABLE_REQUIRED,
    "prior_receiver_answerable_basis_could_have_been_withheld": (
        PRIOR_RECEIVER_ANSWERABLE_BASIS_COULD_HAVE_BEEN_WITHHELD_REQUIRED
    ),
    "prior_operator_only_attestation_admissible": PRIOR_OPERATOR_ONLY_ATTESTATION_ADMISSIBLE_REQUIRED,
    "prior_derivative_rendering_admissible": PRIOR_DERIVATIVE_RENDERING_ADMISSIBLE_REQUIRED,
    "prior_same_custody_countersignature_admissible": (
        PRIOR_SAME_CUSTODY_COUNTERSIGNATURE_ADMISSIBLE_REQUIRED
    ),
    "prior_automatic_acknowledgement_admissible": (
        PRIOR_AUTOMATIC_ACKNOWLEDGEMENT_ADMISSIBLE_REQUIRED
    ),
    "prior_generated_affirmation_admissible": PRIOR_GENERATED_AFFIRMATION_ADMISSIBLE_REQUIRED,
    "prior_identity_created": False,
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

TARGET_SPEC_MARKER_CLASSES = (
    (
        "boundary_identity",
        (
            "Receiver-Side Answerable Basis Reception Boundary V0 Minimum Specification",
            BOUNDARY_TYPE,
            BOUNDARY_ID,
            BOUNDARY_SCOPE,
        ),
    ),
    (
        "presence_operation_waiting_basis",
        (
            PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED,
            PRIOR_PRESENCE_RESULT_REQUIRED,
            "presence_operation_recorded = true",
            "presence_operation_requires_receiver_attestation = true",
            "receiver_attestation_required = true",
            "receiver_answerable_basis_required = true",
            "repo_local_execution_only = true",
            "presence_supported = false",
            "presence_authorized = false",
            "presence_established = false",
            "presence_recorded = false",
            "receiver_attested = false",
            "receiver_answerable_receipt_present = false",
            "receiver_answerable_basis_custody_distinct = false",
            "receiver_answerable_basis_refusable = false",
            "receiver_answerable_basis_could_have_been_withheld = false",
        ),
    ),
    (
        "presence_insufficiency",
        (
            "repo-local execution alone",
            "operator-only attestation",
            "derivative rendering",
            "same-custody countersignature",
            "automatic acknowledgement",
            "generated affirmation",
            "insufficient",
        ),
    ),
    (
        "permitted_result",
        (
            OUTCOME_ALLOWED,
            OUTCOME_REQUIRES_PRESENCE_WAITING_BASIS,
            OUTCOME_BLOCKED,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEPTION_CONSIDERATION_ALLOWED",
            "REQUIRES_PRESENCE_WAITING_BASIS",
        ),
    ),
    (
        "candidate_reception_non_conversion",
        (
            "Receiver-side answerable-basis reception boundary is not receiver-side answerable-basis reception operation",
            "Receiver-side answerable-basis reception boundary permission is not candidate reception",
            "Candidate reception consideration is not candidate reception",
            "Candidate reception is not receiver attestation",
            "Candidate reception is not receiver answerable receipt",
            "Candidate reception is not custody-distinctness proof",
            "Candidate reception is not refusability proof",
            "Candidate reception is not proof that basis could have been withheld",
            "Candidate reception is not presence support",
            "Candidate reception is not presence authorization",
            "Candidate reception is not presence establishment",
            "Candidate reception is not presence recording",
            "Candidate reception is not identity",
            "Candidate reception is not relation",
            "Candidate reception is not coupling",
            "Candidate reception is not FIELD machinery",
            "Candidate reception is not runtime",
            "Candidate reception is not API",
            "Candidate reception is not public interface",
            "Candidate reception is not public intake",
            "Candidate reception is not mailbox",
            "Candidate reception is not listener",
            "Candidate reception is not queue",
            "Candidate reception is not endpoint",
            "Candidate reception is not shared intake lane",
            "Candidate reception is not reusable route",
            "Candidate reception is not repeated reception permission",
            "Candidate reception is not currentness",
            "Candidate reception is not authority",
            "Candidate reception is not standing",
            "Candidate reception is not truth creation",
            "Candidate reception is not continuity memory",
            "Candidate reception is not output authorization",
            "Candidate reception is not action authorization",
            "Candidate reception is not derivative reception",
            "Candidate reception is not synchronization",
            "Candidate reception is not follow-on authorization",
            "Candidate reception is not follow-on work",
        ),
    ),
    (
        "silence_non_conversion",
        (
            "No return is not failure",
            "Silence is not rejection",
            "Silence is not refusal",
            "Silence is not support",
            "Silence is not receiver attestation",
            "Silence is not debt",
            "Possible future return is not pending obligation",
        ),
    ),
    (
        "repository_and_generated_route_block",
        (
            "Repository access is not presence",
            "Repository clone or copy is not presence",
            "Repository read access is not understanding",
            "Understanding is not receiver attestation",
            "Forwarded derivative material is not personal attestation",
            "Generated affirmation is not answerable basis",
            "Automatic acknowledgement is not answerable basis",
            "Operator-only statement is not receiver-side basis",
            "Same-custody countersignature is not custody distinction",
            "Admission of candidate material is not presence support",
            "Admission of candidate material is not follow-on permission",
            "One candidate reception is not repeated reception permission",
            "Body-local reception is not ownership of the between",
            "No public surface is authorized",
            "No named receiver route is authorized",
            "No social ritual is authorized",
            "No downstream route is authorized by boundary",
        ),
    ),
    (
        "permitted_route",
        (
            ADMISSIBLE_FUTURE_ROUTE,
            "Only after a future receiver-side answerable-basis reception boundary records RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEPTION_CONSIDERATION_ALLOWED may a separately bounded receiver-side answerable-basis reception operation be considered",
            "No receiver-side answerable-basis candidate reception, receiver attestation, candidate evaluation, presence support, presence authorization, presence establishment, presence recording, identity, relation, coupling, FIELD machinery, runtime, API, currentness, authority, public interface, repeated route, continuity write, or later operation is authorized by this boundary spec alone",
        ),
    ),
    (
        "contaminated_lineage_preservation",
        (
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md",
            "remains preserved contaminated lineage",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        ),
    ),
    (
        "blocked_routes",
        (
            "direct receiver-side answerable-basis reception boundary to candidate reception completion",
            "direct receiver-side answerable-basis reception boundary to receiver attestation",
            "direct receiver-side answerable-basis reception boundary to receiver answerable receipt",
            "direct receiver-side answerable-basis reception boundary to custody-distinctness decision",
            "direct receiver-side answerable-basis reception boundary to refusability decision",
            "direct receiver-side answerable-basis reception boundary to could-have-been-withheld decision",
            "direct receiver-side answerable-basis reception boundary to presence support",
            "direct receiver-side answerable-basis reception boundary to presence authorization",
            "direct receiver-side answerable-basis reception boundary to presence establishment",
            "direct receiver-side answerable-basis reception boundary to presence recording",
            "direct receiver-side answerable-basis reception boundary to identity",
            "direct receiver-side answerable-basis reception boundary to relation",
            "direct receiver-side answerable-basis reception boundary to coupling assignment",
            "direct receiver-side answerable-basis reception boundary to coupling creation",
            "direct receiver-side answerable-basis reception boundary to FIELD machinery",
            "direct receiver-side answerable-basis reception boundary to runtime",
            "direct receiver-side answerable-basis reception boundary to API",
            "direct receiver-side answerable-basis reception boundary to public interface",
            "direct receiver-side answerable-basis reception boundary to public intake",
            "direct receiver-side answerable-basis reception boundary to mailbox",
            "direct receiver-side answerable-basis reception boundary to listener",
            "direct receiver-side answerable-basis reception boundary to queue",
            "direct receiver-side answerable-basis reception boundary to endpoint",
            "direct receiver-side answerable-basis reception boundary to shared intake lane",
            "direct receiver-side answerable-basis reception boundary to reusable route",
            "direct receiver-side answerable-basis reception boundary to repeated reception permission",
            "direct receiver-side answerable-basis reception boundary to currentness",
            "direct receiver-side answerable-basis reception boundary to authority",
            "direct receiver-side answerable-basis reception boundary to standing",
            "direct receiver-side answerable-basis reception boundary to truth creation",
            "direct receiver-side answerable-basis reception boundary to continuity memory",
            "direct receiver-side answerable-basis reception boundary to output authorization",
            "direct receiver-side answerable-basis reception boundary to action authorization",
            "direct receiver-side answerable-basis reception boundary to derivative reception",
            "direct receiver-side answerable-basis reception boundary to synchronization",
            "direct receiver-side answerable-basis reception boundary to follow-on work",
            "direct presence operation to presence support without receiver-side answerable-basis reception boundary, receiver-side answerable-basis reception operation, and separately bounded presence re-evaluation",
            "direct presence operation to receiver attestation",
            "direct presence operation to public interface",
            "repository access to presence",
            "repository clone route",
            "repository read route",
            "forwarded derivative material to personal attestation",
            "generated affirmation route",
            "automatic acknowledgement route",
            "operator-only attestation route",
            "same-custody countersignature route",
            "no-return-to-failure route",
            "silence-to-rejection route",
            "silence-to-refusal route",
            "silence-to-support route",
            "possible-future-return-to-pending-obligation route",
            "repository scan route",
            "file discovery route",
            "affected-file repair route",
            "prior unsupported-claim validation route",
        ),
    ),
)

PRESENCE_WAITING_MARKER_CLASSES = (
    (
        "presence_operation_waiting_posture",
        (
            PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED,
            PRIOR_PRESENCE_RESULT_REQUIRED,
            "presence_operation_recorded = true",
            "presence_operation_requires_receiver_attestation = true",
            "receiver_attestation_required = true",
            "receiver_answerable_basis_required = true",
            "repo_local_execution_only = true",
            "presence_supported = false",
            "presence_authorized = false",
            "presence_established = false",
            "presence_recorded = false",
            "receiver_attested = false",
            "receiver_answerable_receipt_present = false",
            "receiver_answerable_basis_custody_distinct = false",
            "receiver_answerable_basis_refusable = false",
            "receiver_answerable_basis_could_have_been_withheld = false",
        ),
    ),
    (
        "presence_waiting_insufficiency",
        (
            "repo-local execution alone",
            "operator-only attestation",
            "derivative rendering",
            "same-custody countersignature",
            "automatic acknowledgement",
            "generated affirmation",
        ),
    ),
)

UPSTREAM_REQUIREMENTS = (
    (
        "presence_operation_terminal_summary_path",
        "completed_presence_operation_terminal_summary_path",
        "PRESENCE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "PRESENCE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        PRESENCE_WAITING_MARKER_CLASSES,
        True,
    ),
    (
        "presence_boundary_terminal_summary_path",
        "completed_presence_boundary_terminal_summary_path",
        "PRESENCE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "PRESENCE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        (("presence_boundary", ("PRESENCE_BOUNDARY_ALLOWED", "PRESENCE_OPERATION_CONSIDERATION_ALLOWED")),),
        False,
    ),
    (
        "relation_lapse_operation_terminal_summary_path",
        "completed_relation_lapse_operation_terminal_summary_path",
        "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("relation_lapse_operation", ("RELATION_LAPSE_OPERATION_RECORDED", "RELATION_LAPSE_SUPPORTED")),),
        False,
    ),
    (
        "existence_claim_evidence_check_terminal_summary_path",
        "existence_claim_evidence_check_terminal_summary_path",
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
        (("unsupported_existence_claim_evidence", ("UNSUPPORTED",)),),
        False,
    ),
)

PATH_ALIASES = {
    "target_boundary_spec_path": (
        "receiver_side_answerable_basis_reception_boundary_spec_reference",
        "target_boundary_spec_path",
    ),
    "presence_operation_terminal_summary_path": (
        "presence_operation_terminal_summary_reference",
        "presence_operation_terminal_summary_path",
    ),
    "presence_boundary_terminal_summary_path": (
        "presence_boundary_terminal_summary_reference",
        "presence_boundary_terminal_summary_path",
    ),
    "relation_lapse_operation_terminal_summary_path": (
        "relation_lapse_operation_terminal_summary_reference",
        "relation_lapse_operation_terminal_summary_path",
    ),
    "existence_claim_evidence_check_terminal_summary_path": (
        "existence_claim_evidence_check_terminal_summary_reference",
        "existence_claim_evidence_check_terminal_summary_path",
    ),
}

BLOCKED_ROUTES = (
    "candidate reception completion",
    "receiver attestation",
    "receiver answerable receipt",
    "candidate evaluation",
    "custody-distinctness, refusability, or could-have-been-withheld decision",
    "presence support, authorization, establishment, or recording",
    "identity, relation, coupling, FIELD machinery, runtime, or API",
    "public interface or public intake route",
    "reusable or repeated reception route",
    "currentness, authority, standing, truth, or continuity memory",
    "output, action, derivative reception, synchronization, or follow-on authorization",
    "repository scan, discovery, repair, or prior-claim validation",
)

WHAT_REMAINS_OPEN = (
    "receiver-side answerable-basis reception operation, if separately bounded after boundary",
    "receiver-side answerable-basis candidate reception",
    "receiver-side answerable-basis candidate evaluation",
    "custody-distinctness evaluation",
    "refusability evaluation",
    "could-have-been-withheld evaluation",
    "receiver attestation",
    "receiver answerable receipt",
    "presence re-evaluation, if separately bounded",
    "presence support",
    "presence authorization",
    "presence establishment",
    "presence recording",
    "identity boundary",
    "relation boundary",
    "coupling boundary",
    "FIELD machinery",
    "runtime",
    "API",
    "public interface",
    "public intake",
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


def _as_path(value: Path | str) -> Path:
    """Resolve relative declared paths from the repository root."""

    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_text(path_value: Path | str) -> tuple[str | None, str | None]:
    path = _as_path(path_value)
    try:
        if not path.is_file():
            return None, "not_a_file"
        return path.read_text(encoding="utf-8"), None
    except OSError:
        return None, "unreadable"


def _source_path_value(request: Mapping[str, Any], canonical_key: str) -> Any:
    """Accept the repository-native reference aliases without discovery."""

    for key in PATH_ALIASES[canonical_key]:
        if key in request:
            return request[key]
    return None


def _marker_status(text: str, marker_classes: tuple[tuple[str, tuple[str, ...]], ...]) -> dict[str, bool]:
    return {
        class_name: all(marker in text for marker in markers)
        for class_name, markers in marker_classes
    }


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _check(name: str, passed: bool, block_code: str | None = None, detail: str | None = None) -> dict[str, Any]:
    record: dict[str, Any] = {"name": name, "passed": passed}
    if block_code is not None:
        record["block_code"] = block_code
    if detail is not None:
        record["detail"] = detail
    return record


def _safe_declared_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "intent",
        *EXPECTED_REQUEST_VALUES,
        "target_boundary_spec_path",
        "presence_operation_terminal_summary_path",
        "presence_boundary_terminal_summary_path",
        "relation_lapse_operation_terminal_summary_path",
        "existence_claim_evidence_check_terminal_summary_path",
        *PROHIBITED_REQUEST_FLAGS,
    )
    return {key: request.get(key) for key in keys if key in request}


def _prior_presence_reference() -> dict[str, Any]:
    return {
        "prior_presence_operation_type": PRIOR_PRESENCE_OPERATION_TYPE,
        "prior_presence_operation_outcome": PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED,
        "prior_presence_result": PRIOR_PRESENCE_RESULT_REQUIRED,
        **PRESENCE_REFERENCE_VALUES,
    }


def _boundary_reference() -> dict[str, str]:
    return {
        "receiver_side_answerable_basis_reception_boundary_id": BOUNDARY_ID,
        "receiver_side_answerable_basis_reception_boundary_type": BOUNDARY_TYPE,
        "receiver_side_answerable_basis_reception_boundary_version": BOUNDARY_VERSION,
        "receiver_side_answerable_basis_reception_boundary_scope": BOUNDARY_SCOPE,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    }


def _boundary_state(outcome: str) -> dict[str, Any]:
    state: dict[str, Any] = {**EXPECTED_REQUEST_VALUES, **_canonical_non_claims()}
    state.update(
        {
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
            "receiver_side_answerable_basis_reception_boundary_result": "NOT_RECORDED",
        }
    )
    if outcome == OUTCOME_ALLOWED:
        state.update(
            {
                "receiver_side_answerable_basis_reception_boundary_recorded": True,
                "receiver_side_answerable_basis_reception_boundary_result_recorded": True,
                "receiver_side_answerable_basis_reception_boundary_result": (
                    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEPTION_CONSIDERATION_ALLOWED"
                ),
                "receiver_side_answerable_basis_candidate_reception_consideration_allowed": True,
                "prior_presence_operation_referenced": True,
                "presence_requires_receiver_attestation_referenced": True,
                "receiver_answerable_basis_requirement_referenced": True,
            }
        )
    elif outcome == OUTCOME_REQUIRES_PRESENCE_WAITING_BASIS:
        state["receiver_side_answerable_basis_reception_boundary_result"] = (
            "REQUIRES_PRESENCE_WAITING_BASIS"
        )
    elif outcome == OUTCOME_BLOCKED:
        state["receiver_side_answerable_basis_reception_boundary_result"] = "BLOCKED"
    return state


def _boundary_material(state: Mapping[str, Any]) -> dict[str, Any]:
    evaluation_keys = (
        "receiver_side_answerable_basis_reception_boundary_result",
        *ALLOWED_TRUE_ALLOWED_FIELDS[2:],
        "receiver_side_answerable_basis_candidate_received",
        "receiver_side_answerable_basis_candidate_recorded",
        "receiver_side_answerable_basis_candidate_evaluated",
        "receiver_attestation_created",
        "receiver_attestation_supported",
        "receiver_answerable_receipt_present",
        "receiver_answerable_basis_custody_distinct",
        "receiver_answerable_basis_refusable",
        "receiver_answerable_basis_could_have_been_withheld",
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
        "identity_created",
        "relation_created",
        "coupling_assigned",
        "coupling_created",
        "field_machinery_created",
        "runtime_created",
        "api_created",
        "public_interface_created",
        "public_intake_created",
        "mailbox_created",
        "listener_created",
        "queue_created",
        "endpoint_created",
        "shared_intake_lane_created",
        "reusable_route_created",
        "repeated_reception_permission_created",
        "currentness_created",
        "authority_created",
        "standing_created",
        "truth_created",
        "continuity_memory_written",
        "output_authorized",
        "action_authorized",
        "derivative_reception_authorized",
        "synchronization_authorized",
        "follow_on_authorized",
        "follow_on_work_authorized",
    )
    return {
        "prior_presence_operation_reference": _prior_presence_reference(),
        "receiver_side_answerable_basis_reception_boundary_reference": _boundary_reference(),
        "receiver_side_answerable_basis_reception_boundary_evaluation": {
            key: state[key] for key in evaluation_keys
        },
    }


def _build_summary(
    outcome: str,
    state: Mapping[str, Any],
    checks: list[dict[str, Any]],
    upstream_basis: Mapping[str, Any],
    missing_presence_basis: list[str],
) -> dict[str, Any]:
    failed = sum(not check["passed"] for check in checks)
    summary: dict[str, Any] = {
        "outcome": outcome,
        "failed_check_count": failed,
        "passed_check_count": len(checks) - failed,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        **EXPECTED_REQUEST_VALUES,
        "prior_presence_operation_type_required": PRIOR_PRESENCE_OPERATION_TYPE,
        "prior_presence_operation_outcome_required": PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED,
        "prior_presence_result_required": PRIOR_PRESENCE_RESULT_REQUIRED,
        **PRESENCE_REFERENCE_VALUES,
        "receiver_side_answerable_basis_reception_boundary_result": state[
            "receiver_side_answerable_basis_reception_boundary_result"
        ],
        "receiver_side_answerable_basis_candidate_reception_consideration_allowed": state[
            "receiver_side_answerable_basis_candidate_reception_consideration_allowed"
        ],
        "prior_presence_operation_referenced": state["prior_presence_operation_referenced"],
        "presence_requires_receiver_attestation_referenced": state[
            "presence_requires_receiver_attestation_referenced"
        ],
        "receiver_answerable_basis_requirement_referenced": state[
            "receiver_answerable_basis_requirement_referenced"
        ],
        "selected_target_boundary_spec_path": upstream_basis.get("target_boundary_spec_path"),
        "completed_presence_operation_terminal_summary_path": upstream_basis.get(
            "presence_operation_terminal_summary_path"
        ),
        "missing_or_insufficient_presence_waiting_basis": list(missing_presence_basis),
        "upstream_marker_classes": {
            key: value
            for key, value in upstream_basis.items()
            if key.endswith("_marker_classes")
        },
    }
    for key in REQUIRED_FALSE_NON_CLAIMS:
        summary[key] = state[key]
    return summary


def build_receiver_side_answerable_basis_reception_boundary_v0_min_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact, JSON-safe summary of an existing resolver result."""

    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceptionBoundaryV0MinV2Error("WRITE_REFUSED: result is not a mapping")
    summary = result.get("receiver_side_answerable_basis_reception_boundary_summary")
    if isinstance(summary, Mapping):
        return copy.deepcopy(dict(summary))
    state = result.get("receiver_side_answerable_basis_reception_boundary")
    checks = result.get("receiver_side_answerable_basis_reception_boundary_checks")
    upstream = result.get("upstream_basis")
    if not isinstance(state, Mapping) or not isinstance(checks, list) or not isinstance(upstream, Mapping):
        raise ReceiverSideAnswerableBasisReceptionBoundaryV0MinV2Error("WRITE_REFUSED: result lacks boundary sections")
    return _build_summary(
        str(result.get("outcome", OUTCOME_NOT_RECORDED)),
        state,
        [dict(check) for check in checks if isinstance(check, Mapping)],
        upstream,
        list(result.get("missing_or_insufficient_presence_waiting_basis", [])),
    )


def _result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    upstream_basis: Mapping[str, Any],
    missing_presence_basis: list[str],
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    state = _boundary_state(outcome)
    material = _boundary_material(state)
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": block_code,
        "block_code": block_code,
        "reason": block_reason,
    }
    statement = {
        "receiver_side_answerable_basis_reception_boundary_recorded": state[
            "receiver_side_answerable_basis_reception_boundary_recorded"
        ],
        "receiver_side_answerable_basis_reception_boundary_result_recorded": state[
            "receiver_side_answerable_basis_reception_boundary_result_recorded"
        ],
        "receiver_side_answerable_basis_reception_boundary_result": state[
            "receiver_side_answerable_basis_reception_boundary_result"
        ],
        "receiver_side_answerable_basis_candidate_reception_consideration_allowed": state[
            "receiver_side_answerable_basis_candidate_reception_consideration_allowed"
        ],
        "prior_presence_operation_referenced": state["prior_presence_operation_referenced"],
        "presence_requires_receiver_attestation_referenced": state[
            "presence_requires_receiver_attestation_referenced"
        ],
        "receiver_answerable_basis_requirement_referenced": state[
            "receiver_answerable_basis_requirement_referenced"
        ],
        "result_level_non_claims_canonical_false": True,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE if outcome == OUTCOME_ALLOWED else None,
    }
    non_meaning = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    summary = _build_summary(outcome, state, checks, upstream_basis, missing_presence_basis)
    return {
        "receiver_side_answerable_basis_reception_boundary_metadata": {
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
        },
        "declared_receiver_side_answerable_basis_reception_boundary_basis": _safe_declared_basis(request),
        "upstream_basis": copy.deepcopy(dict(upstream_basis)),
        "receiver_side_answerable_basis_reception_boundary": state,
        "receiver_side_answerable_basis_reception_boundary_material": material,
        "receiver_side_answerable_basis_reception_boundary_checks": checks,
        "receiver_side_answerable_basis_reception_boundary_statement": statement,
        "receiver_side_answerable_basis_reception_boundary_non_meaning": non_meaning,
        "boundary_result_detail": {
            "result": state["receiver_side_answerable_basis_reception_boundary_result"],
            "missing_or_insufficient_presence_waiting_basis": list(missing_presence_basis),
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "receiver_side_answerable_basis_reception_operation_requires_separate_bounded_step": True,
            "candidate_reception_authorized_here": False,
            "candidate_reception_consideration_allowed": outcome == OUTCOME_ALLOWED,
        },
        "blocked_routes": list(BLOCKED_ROUTES),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "block": block,
        "receiver_side_answerable_basis_reception_boundary_summary": summary,
    }


def _add_failure(
    checks: list[dict[str, Any]], name: str, code: str, detail: str
) -> tuple[str, str]:
    checks.append(_check(name, False, code, detail))
    return code, detail


def _validate_request_posture(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None]:
    intent = request.get("intent")
    if intent not in SUPPORTED_INTENTS:
        return _add_failure(checks, "supported_intent", "UNSUPPORTED_INTENT", "intent is not supported")
    checks.append(_check("supported_intent", True))
    if intent == INTENT_BLOCK:
        return _add_failure(checks, "explicit_block_intent", "EXPLICIT_BLOCK_REQUESTED", "explicit block intent")

    for key, expected in EXPECTED_REQUEST_VALUES.items():
        actual = request.get(key)
        passed = actual == expected
        checks.append(_check("request_" + key, passed, None if passed else "REQUEST_VALUE_MISMATCH"))
        if not passed:
            return "REQUEST_VALUE_MISMATCH", key + " differs from its exact bounded value"

    declared_non_claims = request.get("declared_non_claims")
    valid_non_claims = isinstance(declared_non_claims, Mapping) and all(
        declared_non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
    )
    checks.append(
        _check(
            "declared_non_claims_canonical_false",
            valid_non_claims,
            None if valid_non_claims else "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    if not valid_non_claims:
        return "NON_CLAIM_MISSING_OR_FLIPPED", "declared_non_claims must contain every required key as false"

    for flag, code in PROHIBITED_REQUEST_FLAGS.items():
        passed = request.get(flag, False) is False
        checks.append(_check(flag, passed, None if passed else code))
        if not passed:
            return code, flag + " requests a prohibited conversion"

    for field in REQUIRED_FALSE_NON_CLAIMS:
        if field in request and request[field] is not False:
            return _add_failure(
                checks,
                "top_level_" + field,
                "RESULT_POSTURE_PRECLAIMED",
                field + " may not be pre-claimed by the request",
            )
    return None, None


def _evaluate_sources(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[dict[str, Any], list[str], str | None, str | None]:
    upstream_basis: dict[str, Any] = {}
    missing_presence_basis: list[str] = []

    target_path_value = _source_path_value(request, "target_boundary_spec_path")
    if not isinstance(target_path_value, (str, Path)):
        code, reason = _add_failure(
            checks,
            "target_boundary_spec_reference",
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_SPEC_REFERENCE_MISSING",
            "target boundary spec path is not declared",
        )
        return upstream_basis, missing_presence_basis, code, reason
    target_text, target_error = _read_text(target_path_value)
    upstream_basis["target_boundary_spec_path"] = str(_as_path(target_path_value))
    if target_error is not None or target_text is None:
        code, reason = _add_failure(
            checks,
            "target_boundary_spec_reference",
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_SPEC_REFERENCE_MISSING",
            "target boundary spec is unavailable",
        )
        return upstream_basis, missing_presence_basis, code, reason
    target_status = _marker_status(target_text, TARGET_SPEC_MARKER_CLASSES)
    upstream_basis["target_boundary_spec_marker_classes"] = target_status
    for name, passed in target_status.items():
        checks.append(
            _check(
                "target_spec_" + name,
                passed,
                None if passed else "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_SPEC_MARKER_MISSING",
            )
        )
    if not all(target_status.values()):
        return (
            upstream_basis,
            missing_presence_basis,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_SPEC_MARKER_MISSING",
            "target boundary specification is missing a required marker class",
        )

    for path_key, result_key, reference_code, marker_code, marker_classes, is_presence in UPSTREAM_REQUIREMENTS:
        path_value = _source_path_value(request, path_key)
        if not isinstance(path_value, (str, Path)):
            checks.append(_check(result_key + "_reference", False, reference_code))
            if is_presence:
                missing_presence_basis.append(result_key + ":reference")
                upstream_basis[path_key] = None
                continue
            return upstream_basis, missing_presence_basis, reference_code, path_key + " is not declared"
        text, error = _read_text(path_value)
        upstream_basis[path_key] = str(_as_path(path_value))
        if error is not None or text is None:
            checks.append(_check(result_key + "_reference", False, reference_code))
            if is_presence:
                missing_presence_basis.append(result_key + ":reference")
                continue
            return upstream_basis, missing_presence_basis, reference_code, path_key + " is unavailable"
        status = _marker_status(text, marker_classes)
        upstream_basis[result_key + "_marker_classes"] = status
        for name, passed in status.items():
            checks.append(_check(result_key + "_" + name, passed, None if passed else marker_code))
        if not all(status.values()):
            if is_presence:
                missing_presence_basis.extend(name for name, passed in status.items() if not passed)
                continue
            return upstream_basis, missing_presence_basis, marker_code, result_key + " lacks a required marker class"
    if missing_presence_basis:
        return (
            upstream_basis,
            missing_presence_basis,
            "PRESENCE_WAITING_BASIS_MISSING_OR_INSUFFICIENT",
            "presence-operation waiting basis is missing or insufficient",
        )
    return upstream_basis, missing_presence_basis, None, None


def build_receiver_side_answerable_basis_reception_boundary_v0_min_v2_request(
    *,
    target_boundary_spec_path: Path | str | None = None,
    presence_operation_terminal_summary_path: Path | str | None = None,
    presence_boundary_terminal_summary_path: Path | str | None = None,
    relation_lapse_operation_terminal_summary_path: Path | str | None = None,
    existence_claim_evidence_check_terminal_summary_path: Path | str | None = None,
    intent: str = INTENT_RECORD,
    expected_boundary_id: str = BOUNDARY_ID,
    expected_boundary_type: str = BOUNDARY_TYPE,
    expected_boundary_version: str = BOUNDARY_VERSION,
    expected_boundary_scope: str = BOUNDARY_SCOPE,
    expected_prior_presence_operation_type: str = PRIOR_PRESENCE_OPERATION_TYPE,
    expected_prior_presence_operation_outcome: str = PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED,
    expected_prior_presence_result: str = PRIOR_PRESENCE_RESULT_REQUIRED,
    expected_admissible_future_route: str = ADMISSIBLE_FUTURE_ROUTE,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one bounded declared request without discovering any files."""

    request: dict[str, Any] = {
        "intent": intent,
        "target_boundary_spec_path": str(
            target_boundary_spec_path
            if target_boundary_spec_path is not None
            else REPO_ROOT / "spec" / "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_V0_MIN_SPEC.md"
        ),
        "presence_operation_terminal_summary_path": str(
            presence_operation_terminal_summary_path
            if presence_operation_terminal_summary_path is not None
            else REPO_ROOT / "spec" / "PRESENCE_OPERATION_TERMINAL_SUMMARY_V0.md"
        ),
        "presence_boundary_terminal_summary_path": str(
            presence_boundary_terminal_summary_path
            if presence_boundary_terminal_summary_path is not None
            else REPO_ROOT / "spec" / "PRESENCE_BOUNDARY_TERMINAL_SUMMARY_V0.md"
        ),
        "relation_lapse_operation_terminal_summary_path": str(
            relation_lapse_operation_terminal_summary_path
            if relation_lapse_operation_terminal_summary_path is not None
            else REPO_ROOT / "spec" / "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_V0.md"
        ),
        "existence_claim_evidence_check_terminal_summary_path": str(
            existence_claim_evidence_check_terminal_summary_path
            if existence_claim_evidence_check_terminal_summary_path is not None
            else REPO_ROOT / "spec" / "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
        ),
        "expected_boundary_id": expected_boundary_id,
        "expected_boundary_type": expected_boundary_type,
        "expected_boundary_version": expected_boundary_version,
        "expected_boundary_scope": expected_boundary_scope,
        "expected_prior_presence_operation_type": expected_prior_presence_operation_type,
        "expected_prior_presence_operation_outcome": expected_prior_presence_operation_outcome,
        "expected_prior_presence_result": expected_prior_presence_result,
        "expected_admissible_future_route": expected_admissible_future_route,
        "declared_non_claims": (
            _canonical_non_claims() if declared_non_claims is None else copy.deepcopy(dict(declared_non_claims))
        ),
    }
    request.update(EXPECTED_REQUEST_VALUES)
    request.update(
        {
            "boundary_id": expected_boundary_id,
            "boundary_type": expected_boundary_type,
            "boundary_version": expected_boundary_version,
            "boundary_scope": expected_boundary_scope,
            "receiver_side_answerable_basis_reception_boundary_id": expected_boundary_id,
            "receiver_side_answerable_basis_reception_boundary_type": expected_boundary_type,
            "receiver_side_answerable_basis_reception_boundary_version": expected_boundary_version,
            "receiver_side_answerable_basis_reception_boundary_scope": expected_boundary_scope,
            "prior_presence_operation_type": expected_prior_presence_operation_type,
            "prior_presence_operation_outcome_required": expected_prior_presence_operation_outcome,
            "prior_presence_result_required": expected_prior_presence_result,
            "admissible_future_route": expected_admissible_future_route,
        }
    )
    request.update({field: False for field in REQUIRED_FALSE_NON_CLAIMS})
    request.update({flag: False for flag in PROHIBITED_REQUEST_FLAGS})
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_reception_boundary_v0_min_v2_request(
    **kwargs: Any,
) -> dict[str, Any]:
    """Compatibility wrapper for the declared boundary-request builder."""

    return build_receiver_side_answerable_basis_reception_boundary_v0_min_v2_request(**kwargs)


# V1 builder spellings remain request-compatible, but build v2 requests.
build_receiver_side_answerable_basis_reception_boundary_v0_min_request = (
    build_receiver_side_answerable_basis_reception_boundary_v0_min_v2_request
)
build_declared_receiver_side_answerable_basis_reception_boundary_v0_min_request = (
    build_receiver_side_answerable_basis_reception_boundary_v0_min_v2_request
)


def resolve_receiver_side_answerable_basis_reception_boundary_v0_min_v2(
    declared_receiver_side_answerable_basis_reception_boundary: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve exactly one bounded receiver-side reception consideration result."""

    if declared_receiver_side_answerable_basis_reception_boundary is None:
        request: Mapping[str, Any] = build_receiver_side_answerable_basis_reception_boundary_v0_min_v2_request()
    elif not isinstance(declared_receiver_side_answerable_basis_reception_boundary, Mapping):
        return _result(
            {},
            OUTCOME_BLOCKED,
            [_check("request_mapping", False, "REQUEST_NOT_MAPPING")],
            {},
            [],
            "REQUEST_NOT_MAPPING",
            "declared receiver-side boundary request is not a mapping",
        )
    else:
        request = copy.deepcopy(dict(declared_receiver_side_answerable_basis_reception_boundary))

    checks: list[dict[str, Any]] = [_check("request_mapping", True)]
    code, reason = _validate_request_posture(request, checks)
    if code is not None:
        return _result(request, OUTCOME_BLOCKED, checks, {}, [], code, reason)

    if request.get("intent") == INTENT_DO_NOT_RECORD:
        return _result(request, OUTCOME_NOT_RECORDED, checks, {}, [], None, None)

    upstream_basis, missing_presence_basis, code, reason = _evaluate_sources(request, checks)
    if code == "PRESENCE_WAITING_BASIS_MISSING_OR_INSUFFICIENT":
        return _result(
            request,
            OUTCOME_REQUIRES_PRESENCE_WAITING_BASIS,
            checks,
            upstream_basis,
            missing_presence_basis,
            None,
            None,
        )
    if code is not None:
        return _result(
            request,
            OUTCOME_BLOCKED,
            checks,
            upstream_basis,
            missing_presence_basis,
            code,
            reason,
        )
    return _result(request, OUTCOME_ALLOWED, checks, upstream_basis, [], None, None)


def resolve_receiver_side_answerable_basis_reception_boundary_v0_min_v2_from_path(
    declared_receiver_side_answerable_basis_reception_boundary_path: Path | str,
) -> dict[str, Any]:
    """Read one declared JSON request path without broad filesystem discovery."""

    path = Path(declared_receiver_side_answerable_basis_reception_boundary_path)
    try:
        if not path.is_file():
            raise OSError("request path is not a file")
        payload = json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        return _result(
            {},
            OUTCOME_BLOCKED,
            [_check("declared_request_path", False, "REQUEST_PATH_UNREADABLE")],
            {},
            [],
            "REQUEST_PATH_UNREADABLE",
            "declared request path is unavailable",
        )
    except (UnicodeDecodeError, json.JSONDecodeError):
        return _result(
            {},
            OUTCOME_BLOCKED,
            [_check("declared_request_json", False, "REQUEST_JSON_INVALID")],
            {},
            [],
            "REQUEST_JSON_INVALID",
            "declared request JSON is invalid",
        )
    return resolve_receiver_side_answerable_basis_reception_boundary_v0_min_v2(payload)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem, suffix = path.stem, path.suffix
    index = 1
    while True:
        candidate = path.with_name(f"{stem}_{index:03d}{suffix}")
        if not candidate.exists():
            return candidate
        index += 1


def write_receiver_side_answerable_basis_reception_boundary_v0_min_v2_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a result deterministically without silently replacing an artifact."""

    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceptionBoundaryV0MinV2Error("WRITE_REFUSED: result is not a mapping")
    requested_path = OUTPUT_ROOT / OUTPUT_FILENAME if output_path is None else Path(output_path)
    target = _next_available_output_path(requested_path)
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as handle:
            json.dump(dict(result), handle, indent=2, sort_keys=True, ensure_ascii=True)
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisReceptionBoundaryV0MinV2Error(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
