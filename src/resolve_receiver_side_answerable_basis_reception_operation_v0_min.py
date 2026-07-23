"""Resolve one bounded receiver-side answerable-basis candidate reception.

The resolver can record arrival of one explicitly supplied candidate as opaque
candidate material. It never evaluates that material or turns reception into
attestation, presence, authority, a reusable route, or downstream work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any


class ReceiverSideAnswerableBasisReceptionOperationV0MinError(Exception):
    """Raised when a bounded operation result cannot be safely summarized or written."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_reception_operation_v0_min"

OPERATION_ID = "receiver_side_answerable_basis_reception_operation_001"
OPERATION_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = (
    "RECEIVE_ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "CANDIDATE_AS_CANDIDATE_MATERIAL_ONLY"
)
PRIOR_BOUNDARY_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY"
PRIOR_BOUNDARY_OUTCOME_REQUIRED = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_ALLOWED"
PRIOR_BOUNDARY_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEPTION_CONSIDERATION_ALLOWED"
)
PRIOR_BOUNDARY_RECORDED_REQUIRED = True
PRIOR_BOUNDARY_RESULT_RECORDED_REQUIRED = True
PRIOR_CANDIDATE_RECEPTION_CONSIDERATION_ALLOWED_REQUIRED = True
PRIOR_PRESENCE_OPERATION_REFERENCED_REQUIRED = True
PRIOR_PRESENCE_REQUIRES_RECEIVER_ATTESTATION_REFERENCED_REQUIRED = True
PRIOR_RECEIVER_ANSWERABLE_BASIS_REQUIREMENT_REFERENCED_REQUIRED = True
PRIOR_CANDIDATE_RECEIVED_REQUIRED = False
PRIOR_CANDIDATE_RECORDED_REQUIRED = False
PRIOR_CANDIDATE_EVALUATED_REQUIRED = False
PRIOR_RECEIVER_ATTESTATION_CREATED_REQUIRED = False
PRIOR_RECEIVER_ATTESTATION_SUPPORTED_REQUIRED = False
PRIOR_RECEIVER_ANSWERABLE_RECEIPT_PRESENT_REQUIRED = False
PRIOR_CUSTODY_DISTINCT_REQUIRED = False
PRIOR_REFUSABLE_REQUIRED = False
PRIOR_COULD_HAVE_BEEN_WITHHELD_REQUIRED = False
PRIOR_PRESENCE_SUPPORTED_REQUIRED = False
PRIOR_PRESENCE_AUTHORIZED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_PRESENCE_RECORDED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_THEN_"
    "CANDIDATE_EVALUATION_BOUNDARY_ONLY"
)

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"

OUTCOME_RECORDED = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED"
OUTCOME_REQUIRES_CANDIDATE_MATERIAL = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_REQUIRES_CANDIDATE_MATERIAL"
)
OUTCOME_BLOCKED = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_REQUIRES_CANDIDATE_MATERIAL,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION"
INTENT_BLOCK = "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_receiver_side_answerable_basis_reception_operation_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_reception_operation_001__"
    "receiver_side_answerable_basis_reception_operation_v0_min_result.json"
)

DEFAULT_OPERATION_SPEC_REFERENCE = "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_V0_MIN_SPEC.md"
DEFAULT_RECEPTION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "receiver_side_answerable_basis_reception_operation_recorded",
    "receiver_side_answerable_basis_reception_operation_result_recorded",
    "candidate_material_supplied",
    "candidate_material_received",
    "candidate_material_recorded",
    "candidate_material_preserved",
    "candidate_source_provenance_reference_supplied",
    "receiver_side_answerable_basis_candidate_received",
    "receiver_side_answerable_basis_candidate_recorded",
    "prior_receiver_side_answerable_basis_reception_boundary_referenced",
)
ALLOWED_TRUE_REQUIRES_CANDIDATE_MATERIAL_FIELDS = (
    "receiver_side_answerable_basis_reception_operation_recorded",
    "receiver_side_answerable_basis_reception_operation_result_recorded",
    "prior_receiver_side_answerable_basis_reception_boundary_referenced",
)

# This list follows the operation specification's default and blocked-route
# false posture. Final result-level non-claims are always regenerated from it.
REQUIRED_FALSE_NON_CLAIMS = tuple(
    """
receiver_side_answerable_basis_reception_operation_recorded
receiver_side_answerable_basis_reception_operation_result_recorded
candidate_material_supplied
candidate_material_received
candidate_material_recorded
candidate_material_preserved
candidate_source_provenance_reference_supplied
receiver_side_answerable_basis_candidate_received
receiver_side_answerable_basis_candidate_recorded
receiver_side_answerable_basis_candidate_evaluated
second_candidate_received
repeated_reception_permission_created
reusable_route_created
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
repository_scan_performed
file_discovery_performed
validation_enforced
direct_operation_spec_to_candidate_reception_completion
operation_resolver_to_candidate_material
operation_test_to_candidate_material
operation_artifact_to_candidate_material
terminal_summary_to_candidate_material
generated_affirmation_to_candidate_material
automatic_acknowledgement_to_candidate_material
operator_only_statement_to_receiver_side_candidate_basis
derivative_rendering_to_receiver_side_candidate_basis
same_custody_countersignature_to_custody_distinction
no_input_execution_to_candidate_reception
repository_execution_to_candidate_arrival
repository_access_to_candidate_supply
boundary_permission_to_candidate_reception
candidate_reception_to_candidate_evaluation
candidate_reception_to_answerable_basis_sufficiency
candidate_reception_to_receiver_attestation
candidate_reception_to_receiver_answerable_receipt
candidate_reception_to_custody_distinctness_decision
candidate_reception_to_refusability_decision
candidate_reception_to_could_have_been_withheld_decision
candidate_reception_to_presence_support
candidate_reception_to_presence_authorization
candidate_reception_to_presence_establishment
candidate_reception_to_presence_recording
candidate_reception_to_identity
candidate_reception_to_relation
candidate_reception_to_coupling_assignment
candidate_reception_to_coupling_creation
candidate_reception_to_field_machinery
candidate_reception_to_runtime
candidate_reception_to_api
candidate_reception_to_public_interface
candidate_reception_to_public_intake
candidate_reception_to_mailbox
candidate_reception_to_listener
candidate_reception_to_queue
candidate_reception_to_endpoint
candidate_reception_to_shared_intake_lane
candidate_reception_to_reusable_route
candidate_reception_to_repeated_reception_permission
candidate_reception_to_second_candidate_reception
candidate_reception_to_currentness
candidate_reception_to_authority
candidate_reception_to_standing
candidate_reception_to_truth_creation
candidate_reception_to_continuity_memory
candidate_reception_to_output_authorization
candidate_reception_to_action_authorization
candidate_reception_to_derivative_reception
candidate_reception_to_synchronization
candidate_reception_to_follow_on_authorization
candidate_reception_to_follow_on_work
declared_source_provenance_reference_to_verified_provenance
source_reference_to_source_identity
source_reference_to_authority
source_reference_to_standing
source_reference_to_custody_distinction
missing_candidate_material_to_failure
missing_candidate_material_to_rejection
missing_candidate_material_to_refusal
missing_candidate_material_to_debt
possible_future_candidate_return_to_pending_obligation
""".split()
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "OPERATION_SPEC_REFERENCE_MISSING",
    "OPERATION_SPEC_MARKER_MISSING",
    "RECEPTION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RECEPTION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "REQUEST_VALUE_MISMATCH",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "CANDIDATE_MATERIAL_NOT_JSON_COMPATIBLE",
    "CANDIDATE_MATERIAL_INCOMPLETE",
    "CANDIDATE_SOURCE_PROVENANCE_REFERENCE_MISSING",
    "MULTIPLE_CANDIDATES_REQUESTED",
    "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED",
    "PROHIBITED_ANSWERABLE_BASIS_SUFFICIENCY_REQUESTED",
    "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
    "PROHIBITED_CUSTODY_DISTINCTNESS_DECISION_REQUESTED",
    "PROHIBITED_REFUSABILITY_DECISION_REQUESTED",
    "PROHIBITED_COULD_HAVE_BEEN_WITHHELD_DECISION_REQUESTED",
    "PROHIBITED_PRESENCE_REQUESTED",
    "PROHIBITED_IDENTITY_OR_RELATION_REQUESTED",
    "PROHIBITED_COUPLING_REQUESTED",
    "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_PUBLIC_INTAKE_REQUESTED",
    "PROHIBITED_REUSABLE_OR_REPEATED_RECEPTION_ROUTE_REQUESTED",
    "PROHIBITED_SECOND_CANDIDATE_REQUESTED",
    "PROHIBITED_TRUTH_OR_CONTINUITY_MEMORY_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "RESULT_POSTURE_PRECLAIMED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
    "REQUEST_PATH_UNREADABLE",
    "REQUEST_JSON_INVALID",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_candidate_evaluation": "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED",
    "request_answerable_basis_sufficiency": "PROHIBITED_ANSWERABLE_BASIS_SUFFICIENCY_REQUESTED",
    "request_receiver_attestation_creation": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "request_receiver_attestation_support": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "request_receiver_answerable_receipt_creation": "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
    "request_custody_distinctness_decision": "PROHIBITED_CUSTODY_DISTINCTNESS_DECISION_REQUESTED",
    "request_refusability_decision": "PROHIBITED_REFUSABILITY_DECISION_REQUESTED",
    "request_could_have_been_withheld_decision": "PROHIBITED_COULD_HAVE_BEEN_WITHHELD_DECISION_REQUESTED",
    "request_presence_support": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_authorization": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_establishment": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_recording": "PROHIBITED_PRESENCE_REQUESTED",
    "request_identity_creation": "PROHIBITED_IDENTITY_OR_RELATION_REQUESTED",
    "request_relation_creation": "PROHIBITED_IDENTITY_OR_RELATION_REQUESTED",
    "request_coupling_assignment": "PROHIBITED_COUPLING_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
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
    "request_second_candidate_reception": "PROHIBITED_SECOND_CANDIDATE_REQUESTED",
    "request_currentness_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
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
    "operation_id": OPERATION_ID,
    "operation_type": OPERATION_TYPE,
    "operation_version": OPERATION_VERSION,
    "operation_scope": OPERATION_SCOPE,
    "receiver_side_answerable_basis_reception_operation_id": OPERATION_ID,
    "receiver_side_answerable_basis_reception_operation_type": OPERATION_TYPE,
    "receiver_side_answerable_basis_reception_operation_version": OPERATION_VERSION,
    "receiver_side_answerable_basis_reception_operation_scope": OPERATION_SCOPE,
    "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
    "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
    "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
    "candidate_id": CANDIDATE_ID,
    "candidate_type": CANDIDATE_TYPE,
    "candidate_scope": CANDIDATE_SCOPE,
    "prior_receiver_side_answerable_basis_reception_boundary_type": PRIOR_BOUNDARY_TYPE,
    "prior_receiver_side_answerable_basis_reception_boundary_outcome_required": PRIOR_BOUNDARY_OUTCOME_REQUIRED,
    "prior_receiver_side_answerable_basis_reception_boundary_result_required": PRIOR_BOUNDARY_RESULT_REQUIRED,
    "prior_receiver_side_answerable_basis_reception_boundary_recorded_required": PRIOR_BOUNDARY_RECORDED_REQUIRED,
    "prior_receiver_side_answerable_basis_reception_boundary_result_recorded_required": PRIOR_BOUNDARY_RESULT_RECORDED_REQUIRED,
    "prior_receiver_side_answerable_basis_candidate_reception_consideration_allowed_required": PRIOR_CANDIDATE_RECEPTION_CONSIDERATION_ALLOWED_REQUIRED,
    "prior_presence_operation_referenced_required": PRIOR_PRESENCE_OPERATION_REFERENCED_REQUIRED,
    "prior_presence_requires_receiver_attestation_referenced_required": PRIOR_PRESENCE_REQUIRES_RECEIVER_ATTESTATION_REFERENCED_REQUIRED,
    "prior_receiver_answerable_basis_requirement_referenced_required": PRIOR_RECEIVER_ANSWERABLE_BASIS_REQUIREMENT_REFERENCED_REQUIRED,
    "prior_receiver_side_answerable_basis_candidate_received_required": PRIOR_CANDIDATE_RECEIVED_REQUIRED,
    "prior_receiver_side_answerable_basis_candidate_recorded_required": PRIOR_CANDIDATE_RECORDED_REQUIRED,
    "prior_receiver_side_answerable_basis_candidate_evaluated_required": PRIOR_CANDIDATE_EVALUATED_REQUIRED,
    "prior_receiver_attestation_created_required": PRIOR_RECEIVER_ATTESTATION_CREATED_REQUIRED,
    "prior_receiver_attestation_supported_required": PRIOR_RECEIVER_ATTESTATION_SUPPORTED_REQUIRED,
    "prior_receiver_answerable_receipt_present_required": PRIOR_RECEIVER_ANSWERABLE_RECEIPT_PRESENT_REQUIRED,
    "prior_receiver_answerable_basis_custody_distinct_required": PRIOR_CUSTODY_DISTINCT_REQUIRED,
    "prior_receiver_answerable_basis_refusable_required": PRIOR_REFUSABLE_REQUIRED,
    "prior_receiver_answerable_basis_could_have_been_withheld_required": PRIOR_COULD_HAVE_BEEN_WITHHELD_REQUIRED,
    "prior_presence_supported_required": PRIOR_PRESENCE_SUPPORTED_REQUIRED,
    "prior_presence_authorized_required": PRIOR_PRESENCE_AUTHORIZED_REQUIRED,
    "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_presence_recorded_required": PRIOR_PRESENCE_RECORDED_REQUIRED,
    "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
    "prior_follow_on_work_authorized_required": PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED,
    "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
}

PRIOR_BOUNDARY_REFERENCE_VALUES = {
    "prior_receiver_side_answerable_basis_reception_boundary_type": PRIOR_BOUNDARY_TYPE,
    "prior_receiver_side_answerable_basis_reception_boundary_outcome": PRIOR_BOUNDARY_OUTCOME_REQUIRED,
    "prior_receiver_side_answerable_basis_reception_boundary_result": PRIOR_BOUNDARY_RESULT_REQUIRED,
    "prior_receiver_side_answerable_basis_reception_boundary_recorded": PRIOR_BOUNDARY_RECORDED_REQUIRED,
    "prior_receiver_side_answerable_basis_reception_boundary_result_recorded": PRIOR_BOUNDARY_RESULT_RECORDED_REQUIRED,
    "prior_receiver_side_answerable_basis_candidate_reception_consideration_allowed": PRIOR_CANDIDATE_RECEPTION_CONSIDERATION_ALLOWED_REQUIRED,
    "prior_presence_operation_referenced": PRIOR_PRESENCE_OPERATION_REFERENCED_REQUIRED,
    "prior_presence_requires_receiver_attestation_referenced": PRIOR_PRESENCE_REQUIRES_RECEIVER_ATTESTATION_REFERENCED_REQUIRED,
    "prior_receiver_answerable_basis_requirement_referenced": PRIOR_RECEIVER_ANSWERABLE_BASIS_REQUIREMENT_REFERENCED_REQUIRED,
    "prior_receiver_side_answerable_basis_candidate_received": PRIOR_CANDIDATE_RECEIVED_REQUIRED,
    "prior_receiver_side_answerable_basis_candidate_recorded": PRIOR_CANDIDATE_RECORDED_REQUIRED,
    "prior_receiver_side_answerable_basis_candidate_evaluated": PRIOR_CANDIDATE_EVALUATED_REQUIRED,
    "prior_receiver_attestation_created": PRIOR_RECEIVER_ATTESTATION_CREATED_REQUIRED,
    "prior_receiver_attestation_supported": PRIOR_RECEIVER_ATTESTATION_SUPPORTED_REQUIRED,
    "prior_receiver_answerable_receipt_present": PRIOR_RECEIVER_ANSWERABLE_RECEIPT_PRESENT_REQUIRED,
    "prior_receiver_answerable_basis_custody_distinct": PRIOR_CUSTODY_DISTINCT_REQUIRED,
    "prior_receiver_answerable_basis_refusable": PRIOR_REFUSABLE_REQUIRED,
    "prior_receiver_answerable_basis_could_have_been_withheld": PRIOR_COULD_HAVE_BEEN_WITHHELD_REQUIRED,
    "prior_presence_supported": PRIOR_PRESENCE_SUPPORTED_REQUIRED,
    "prior_presence_authorized": PRIOR_PRESENCE_AUTHORIZED_REQUIRED,
    "prior_presence_established": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_presence_recorded": PRIOR_PRESENCE_RECORDED_REQUIRED,
    "prior_follow_on_authorized": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
    "prior_follow_on_work_authorized": PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED,
}

TARGET_SPEC_MARKER_CLASSES = (
    (
        "operation_identity",
        (
            "Receiver-Side Answerable Basis Reception Operation V0 Minimum Specification",
            OPERATION_TYPE,
            OPERATION_ID,
            OPERATION_SCOPE,
        ),
    ),
    (
        "completed_boundary_basis",
        (
            PRIOR_BOUNDARY_OUTCOME_REQUIRED,
            PRIOR_BOUNDARY_RESULT_REQUIRED,
            "boundary recorded",
            "boundary result recorded",
            "candidate reception consideration allowed",
            "receiver_side_answerable_basis_candidate_received = false",
            "receiver_side_answerable_basis_candidate_recorded = false",
            "receiver_side_answerable_basis_candidate_evaluated = false",
        ),
    ),
    (
        "candidate_identity_and_material_shape",
        (
            CANDIDATE_ID,
            CANDIDATE_TYPE,
            CANDIDATE_SCOPE,
            "candidate identifier",
            "candidate type",
            "candidate scope",
            "candidate material",
            "declared source/provenance reference",
            "explicit supplied-material posture",
        ),
    ),
    (
        "no_input_and_missing_material_posture",
        (
            "No-input execution may not record candidate reception",
            "Missing candidate material preserves candidate reception as false",
            "REQUIRES_CANDIDATE_MATERIAL",
            "Missing candidate material is not failure, refusal, rejection, receiver attestation, receiver answerable receipt, or pending debt",
        ),
    ),
    (
        "opaque_preservation_posture",
        (
            "preserve supplied candidate material without semantic interpretation",
            "It must not rewrite, summarize, normalize, improve, complete, translate, merge, or silently replace",
            "declared source/provenance reference is not verified provenance",
            "It does not become source identity, authority, standing, custody distinction, or receiver attestation",
        ),
    ),
    (
        "operation_outcomes",
        (
            OUTCOME_RECORDED,
            OUTCOME_REQUIRES_CANDIDATE_MATERIAL,
            OUTCOME_BLOCKED,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEIVED",
            "REQUIRES_CANDIDATE_MATERIAL",
        ),
    ),
    (
        "reception_non_conversion",
        (
            "Reception operation is not reception boundary",
            "Boundary permission is not operation execution",
            "Candidate material consideration is not supply",
            "Supply is not reception",
            "Reception is not evaluation or answerable-basis sufficiency",
            "Candidate reception is not receiver attestation, receiver answerable receipt, custody-distinctness proof, refusability proof, proof that candidate material could have been withheld, presence support, presence authorization, presence establishment, or presence recording",
            "Candidate reception is not identity, relation, coupling, FIELD machinery, runtime, API, public interface, public intake, mailbox, listener, queue, endpoint, shared intake lane, reusable route, repeated reception permission, currentness, authority, standing, truth creation, continuity memory, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, or follow-on work",
            "One candidate reception is not permission for a second candidate or reusable reception permission",
            "Repository execution is not candidate arrival",
            "Repository access is not candidate supply",
        ),
    ),
    (
        "permitted_future_route",
        (
            ADMISSIBLE_FUTURE_ROUTE,
            "After one successful candidate reception, the operation terminates",
            "Candidate evaluation requires a separately bounded future boundary",
            "No receiver attestation, receiver answerable receipt, custody-distinctness decision",
        ),
    ),
    (
        "blocked_routes",
        (
            "direct operation specification to candidate reception completion",
            "candidate reception to candidate evaluation, answerable-basis sufficiency, receiver attestation, receiver answerable receipt, custody-distinctness decision, refusability decision, could-have-been-withheld decision, presence support, presence authorization, presence establishment, or presence recording",
            "candidate reception to identity, relation, coupling assignment, coupling creation, FIELD machinery, runtime, API, public interface, public intake, mailbox, listener, queue, endpoint, shared intake lane, reusable route, repeated reception permission, second candidate reception, currentness, authority, standing, truth creation, continuity memory, output authorization, action authorization, derivative reception, synchronization, or follow-on work",
            "repository scan, file discovery, affected-file repair, or prior unsupported-claim validation",
        ),
    ),
    (
        "contaminated_lineage_preservation",
        (
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md",
            "remains preserved contaminated lineage",
            "unsupported existence-claim class",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean",
        ),
    ),
)

RECEPTION_BOUNDARY_TERMINAL_SUMMARY_MARKER_CLASSES = (
    (
        "allowed_boundary_result",
        (
            PRIOR_BOUNDARY_OUTCOME_REQUIRED,
            PRIOR_BOUNDARY_RESULT_REQUIRED,
            "receiver_side_answerable_basis_reception_boundary_recorded = true",
            "receiver_side_answerable_basis_reception_boundary_result_recorded = true",
            "receiver_side_answerable_basis_candidate_reception_consideration_allowed = true",
            "prior_presence_operation_referenced = true",
            "presence_requires_receiver_attestation_referenced = true",
            "receiver_answerable_basis_requirement_referenced = true",
        ),
    ),
    (
        "preserved_no_candidate_or_presence",
        (
            "receiver_side_answerable_basis_candidate_received = false",
            "receiver_side_answerable_basis_candidate_recorded = false",
            "receiver_side_answerable_basis_candidate_evaluated = false",
            "receiver_attestation_created = false",
            "receiver_answerable_receipt_present = false",
            "receiver_answerable_basis_custody_distinct = false",
            "receiver_answerable_basis_refusable = false",
            "receiver_answerable_basis_could_have_been_withheld = false",
            "presence_supported = false",
            "presence_authorized = false",
            "presence_established = false",
            "presence_recorded = false",
            "follow_on_work_authorized = false",
        ),
    ),
)

PATH_ALIASES = {
    "target_operation_spec_path": (
        "receiver_side_answerable_basis_reception_operation_spec_reference",
        "target_operation_spec_path",
    ),
    "reception_boundary_terminal_summary_path": (
        "receiver_side_answerable_basis_reception_boundary_terminal_summary_reference",
        "reception_boundary_terminal_summary_reference",
        "completed_reception_boundary_terminal_summary_path",
        "reception_boundary_terminal_summary_path",
    ),
}

BLOCKED_ROUTES = (
    "candidate evaluation or answerable-basis sufficiency",
    "receiver attestation, receiver answerable receipt, custody distinction, refusability, or withholding decision",
    "presence support, authorization, establishment, or recording",
    "identity, relation, coupling, FIELD machinery, runtime, API, or public intake",
    "reusable, repeated, or second-candidate reception",
    "currentness, authority, standing, truth, continuity memory, output, action, derivative reception, synchronization, or follow-on authorization",
    "repository scan, discovery, repair, or prior-claim validation",
)

WHAT_REMAINS_OPEN = (
    "receiver-side answerable-basis reception operation test",
    "receiver-side answerable-basis reception operation live artifact",
    "actual receiver-side answerable-basis candidate material",
    "actual candidate reception",
    "candidate evaluation boundary",
    "candidate evaluation operation, if separately bounded",
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

SECOND_CANDIDATE_FIELDS = (
    "second_candidate_material",
    "second_candidate_source_provenance_reference",
    "second_candidate_id",
    "second_candidate_type",
    "second_candidate_scope",
    "candidate_material_2",
    "candidate_2",
    "additional_candidate_material",
    "receiver_side_answerable_basis_candidate_002",
)
REQUEST_INPUT_FIELDS = (
    "candidate_material_supplied",
    "candidate_material",
    "candidate_source_provenance_reference_supplied",
    "candidate_source_provenance_reference",
)


def _as_path(value: Path | str) -> Path:
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
    for alias in PATH_ALIASES[canonical_key]:
        if alias in request:
            return request[alias]
    return None


def _marker_status(text: str, marker_classes: tuple[tuple[str, tuple[str, ...]], ...]) -> dict[str, bool]:
    return {
        name: all(marker in text for marker in markers)
        for name, markers in marker_classes
    }


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _check(
    name: str, passed: bool, block_code: str | None = None, detail: str | None = None
) -> dict[str, Any]:
    check: dict[str, Any] = {"name": name, "passed": passed}
    if block_code is not None:
        check["block_code"] = block_code
    if detail is not None:
        check["detail"] = detail
    return check


def _add_failure(
    checks: list[dict[str, Any]], name: str, code: str, detail: str
) -> tuple[str, str]:
    checks.append(_check(name, False, code, detail))
    return code, detail


def _is_json_compatible(value: Any) -> bool:
    try:
        serialized = json.dumps(value, allow_nan=False)
        return json.loads(serialized) == value
    except (TypeError, ValueError):
        return False


def _safe_declared_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "intent",
        "target_operation_spec_path",
        "reception_boundary_terminal_summary_path",
        *EXPECTED_REQUEST_VALUES,
        "candidate_material_supplied",
        "candidate_source_provenance_reference_supplied",
        *PROHIBITED_REQUEST_FLAGS,
    )
    return {key: copy.deepcopy(request[key]) for key in keys if key in request}


def _operation_state(
    outcome: str,
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    state: dict[str, Any] = {**EXPECTED_REQUEST_VALUES, **_canonical_non_claims()}
    state.update(
        {
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "receiver_side_answerable_basis_reception_operation_result": "NOT_RECORDED",
            "prior_receiver_side_answerable_basis_reception_boundary_referenced": False,
        }
    )
    if outcome == OUTCOME_REQUIRES_CANDIDATE_MATERIAL:
        state.update(
            {
                "receiver_side_answerable_basis_reception_operation_recorded": True,
                "receiver_side_answerable_basis_reception_operation_result_recorded": True,
                "receiver_side_answerable_basis_reception_operation_result": "REQUIRES_CANDIDATE_MATERIAL",
                "prior_receiver_side_answerable_basis_reception_boundary_referenced": True,
            }
        )
    elif outcome == OUTCOME_RECORDED:
        state.update(
            {
                "receiver_side_answerable_basis_reception_operation_recorded": True,
                "receiver_side_answerable_basis_reception_operation_result_recorded": True,
                "receiver_side_answerable_basis_reception_operation_result": (
                    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEIVED"
                ),
                "candidate_material_supplied": True,
                "candidate_material_received": True,
                "candidate_material_recorded": True,
                "candidate_material_preserved": True,
                "candidate_source_provenance_reference_supplied": True,
                "receiver_side_answerable_basis_candidate_received": True,
                "receiver_side_answerable_basis_candidate_recorded": True,
                "prior_receiver_side_answerable_basis_reception_boundary_referenced": True,
            }
        )
    elif outcome == OUTCOME_BLOCKED:
        state["receiver_side_answerable_basis_reception_operation_result"] = "BLOCKED"
    return state


def _prior_boundary_reference() -> dict[str, Any]:
    return copy.deepcopy(PRIOR_BOUNDARY_REFERENCE_VALUES)


def _supplied_candidate_material_record(
    state: Mapping[str, Any], request: Mapping[str, Any], outcome: str
) -> dict[str, Any]:
    received = outcome == OUTCOME_RECORDED
    return {
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "candidate_material_supplied": state["candidate_material_supplied"],
        "candidate_material": copy.deepcopy(request.get("candidate_material")) if received else None,
        "candidate_source_provenance_reference_supplied": state[
            "candidate_source_provenance_reference_supplied"
        ],
        "candidate_source_provenance_reference": (
            copy.deepcopy(request.get("candidate_source_provenance_reference")) if received else None
        ),
        "candidate_material_received": state["candidate_material_received"],
        "candidate_material_recorded": state["candidate_material_recorded"],
        "candidate_material_preserved": state["candidate_material_preserved"],
    }


def _operation_material(
    state: Mapping[str, Any], request: Mapping[str, Any], outcome: str
) -> dict[str, Any]:
    evaluation_keys = (
        "receiver_side_answerable_basis_reception_operation_result",
        "receiver_side_answerable_basis_candidate_received",
        "receiver_side_answerable_basis_candidate_recorded",
        "receiver_side_answerable_basis_candidate_evaluated",
        "prior_receiver_side_answerable_basis_reception_boundary_referenced",
        "second_candidate_received",
        "repeated_reception_permission_created",
        "reusable_route_created",
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
    evaluation = {key: state[key] for key in evaluation_keys}
    evaluation.update({key: state[key] for key in REQUIRED_FALSE_NON_CLAIMS})
    return {
        "prior_receiver_side_answerable_basis_reception_boundary_reference": _prior_boundary_reference(),
        "supplied_candidate_material_record": _supplied_candidate_material_record(state, request, outcome),
        "receiver_side_answerable_basis_reception_operation_evaluation": evaluation,
    }


def _build_summary(
    outcome: str,
    state: Mapping[str, Any],
    checks: list[dict[str, Any]],
    upstream_basis: Mapping[str, Any],
    missing_candidate_material: list[str],
) -> dict[str, Any]:
    failed = sum(not check["passed"] for check in checks)
    summary: dict[str, Any] = {
        "outcome": outcome,
        "failed_check_count": failed,
        "passed_check_count": len(checks) - failed,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "prior_boundary_type_required": PRIOR_BOUNDARY_TYPE,
        "prior_boundary_outcome_required": PRIOR_BOUNDARY_OUTCOME_REQUIRED,
        "prior_boundary_result_required": PRIOR_BOUNDARY_RESULT_REQUIRED,
        **PRIOR_BOUNDARY_REFERENCE_VALUES,
        "candidate_id": CANDIDATE_ID,
        "candidate_type": CANDIDATE_TYPE,
        "candidate_scope": CANDIDATE_SCOPE,
        "receiver_side_answerable_basis_reception_operation_result": state[
            "receiver_side_answerable_basis_reception_operation_result"
        ],
        "candidate_material_supplied": state["candidate_material_supplied"],
        "candidate_material_received": state["candidate_material_received"],
        "candidate_material_recorded": state["candidate_material_recorded"],
        "candidate_material_preserved": state["candidate_material_preserved"],
        "candidate_source_provenance_reference_supplied": state[
            "candidate_source_provenance_reference_supplied"
        ],
        "receiver_side_answerable_basis_candidate_received": state[
            "receiver_side_answerable_basis_candidate_received"
        ],
        "receiver_side_answerable_basis_candidate_recorded": state[
            "receiver_side_answerable_basis_candidate_recorded"
        ],
        "receiver_side_answerable_basis_candidate_evaluated": state[
            "receiver_side_answerable_basis_candidate_evaluated"
        ],
        "prior_receiver_side_answerable_basis_reception_boundary_referenced": state[
            "prior_receiver_side_answerable_basis_reception_boundary_referenced"
        ],
        "selected_operation_spec_path": upstream_basis.get("target_operation_spec_path"),
        "completed_reception_boundary_terminal_summary_path": upstream_basis.get(
            "reception_boundary_terminal_summary_path"
        ),
        "upstream_marker_classes": {
            key: copy.deepcopy(value)
            for key, value in upstream_basis.items()
            if key.endswith("_marker_classes")
        },
        "missing_or_insufficient_candidate_material": list(missing_candidate_material),
    }
    for key in REQUIRED_FALSE_NON_CLAIMS:
        summary[key] = state[key]
    return summary


def build_receiver_side_answerable_basis_reception_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact, JSON-safe summary of a resolver result."""

    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceptionOperationV0MinError(
            "WRITE_REFUSED: result is not a mapping"
        )
    existing = result.get("receiver_side_answerable_basis_reception_operation_summary")
    if isinstance(existing, Mapping):
        return copy.deepcopy(dict(existing))
    state = result.get("receiver_side_answerable_basis_reception_operation")
    checks = result.get("receiver_side_answerable_basis_reception_operation_checks")
    upstream_basis = result.get("upstream_basis")
    if not isinstance(state, Mapping) or not isinstance(checks, list) or not isinstance(upstream_basis, Mapping):
        raise ReceiverSideAnswerableBasisReceptionOperationV0MinError(
            "WRITE_REFUSED: result lacks operation sections"
        )
    return _build_summary(
        str(result.get("outcome", OUTCOME_NOT_RECORDED)),
        state,
        [dict(check) for check in checks if isinstance(check, Mapping)],
        upstream_basis,
        list(result.get("missing_or_insufficient_candidate_material", [])),
    )


def _result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    upstream_basis: Mapping[str, Any],
    missing_candidate_material: list[str],
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    state = _operation_state(outcome, request)
    summary = _build_summary(outcome, state, checks, upstream_basis, missing_candidate_material)
    statement = {
        "receiver_side_answerable_basis_reception_operation_recorded": state[
            "receiver_side_answerable_basis_reception_operation_recorded"
        ],
        "receiver_side_answerable_basis_reception_operation_result_recorded": state[
            "receiver_side_answerable_basis_reception_operation_result_recorded"
        ],
        "receiver_side_answerable_basis_reception_operation_result": state[
            "receiver_side_answerable_basis_reception_operation_result"
        ],
        "candidate_material_received": state["candidate_material_received"],
        "candidate_material_recorded": state["candidate_material_recorded"],
        "candidate_material_preserved": state["candidate_material_preserved"],
        "receiver_side_answerable_basis_candidate_evaluated": False,
        "prior_receiver_side_answerable_basis_reception_boundary_referenced": state[
            "prior_receiver_side_answerable_basis_reception_boundary_referenced"
        ],
        "result_level_non_claims_canonical_false": True,
    }
    return {
        "receiver_side_answerable_basis_reception_operation_metadata": {
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
        },
        "declared_receiver_side_answerable_basis_reception_operation_basis": _safe_declared_basis(request),
        "upstream_basis": copy.deepcopy(dict(upstream_basis)),
        "receiver_side_answerable_basis_reception_operation": state,
        "receiver_side_answerable_basis_reception_operation_material": _operation_material(
            state, request, outcome
        ),
        "receiver_side_answerable_basis_reception_operation_checks": checks,
        "receiver_side_answerable_basis_reception_operation_statement": statement,
        "receiver_side_answerable_basis_reception_operation_non_meaning": _canonical_non_claims(),
        "operation_result_detail": {
            "result": state["receiver_side_answerable_basis_reception_operation_result"],
            "missing_or_insufficient_candidate_material": list(missing_candidate_material),
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "candidate_evaluation_requires_separate_bounded_boundary": True,
            "operation_terminates_after_one_successful_candidate_reception": True,
            "candidate_reception_recorded": outcome == OUTCOME_RECORDED,
        },
        "blocked_routes": list(BLOCKED_ROUTES),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code,
            "block_code": block_code,
            "reason": block_reason,
        },
        "receiver_side_answerable_basis_reception_operation_summary": summary,
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "failed_check_count": summary["failed_check_count"],
        "passed_check_count": summary["passed_check_count"],
        "missing_or_insufficient_candidate_material": list(missing_candidate_material),
    }


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
        passed = request.get(key) == expected
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
        return (
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared_non_claims must contain every required key as false",
        )

    for flag, code in PROHIBITED_REQUEST_FLAGS.items():
        passed = request.get(flag, False) is False
        checks.append(_check(flag, passed, None if passed else code))
        if not passed:
            return code, flag + " requests a prohibited conversion"

    for key in SECOND_CANDIDATE_FIELDS:
        if key in request:
            return _add_failure(
                checks,
                key,
                "MULTIPLE_CANDIDATES_REQUESTED",
                key + " supplies an impermissible second candidate shape",
            )

    result_posture_fields = set(REQUIRED_FALSE_NON_CLAIMS) - {
        "candidate_material_supplied",
        "candidate_source_provenance_reference_supplied",
    }
    result_posture_fields.add("prior_receiver_side_answerable_basis_reception_boundary_referenced")
    for field in result_posture_fields:
        if field in request and request[field] is not False:
            return _add_failure(
                checks,
                "top_level_" + field,
                "RESULT_POSTURE_PRECLAIMED",
                field + " may not be pre-claimed by the request",
            )
    operation_result = request.get("receiver_side_answerable_basis_reception_operation_result")
    if operation_result not in (None, "NOT_EVALUATED"):
        return _add_failure(
            checks,
            "top_level_operation_result",
            "RESULT_POSTURE_PRECLAIMED",
            "operation result may not be pre-claimed by the request",
        )
    return None, None


def _evaluate_sources(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[dict[str, Any], str | None, str | None]:
    upstream_basis: dict[str, Any] = {}
    source_requirements = (
        (
            "target_operation_spec_path",
            "OPERATION_SPEC_REFERENCE_MISSING",
            "OPERATION_SPEC_MARKER_MISSING",
            TARGET_SPEC_MARKER_CLASSES,
        ),
        (
            "reception_boundary_terminal_summary_path",
            "RECEPTION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "RECEPTION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            RECEPTION_BOUNDARY_TERMINAL_SUMMARY_MARKER_CLASSES,
        ),
    )
    for canonical_key, reference_code, marker_code, marker_classes in source_requirements:
        value = _source_path_value(request, canonical_key)
        if not isinstance(value, (str, Path)):
            return (
                upstream_basis,
                reference_code,
                canonical_key + " is not a declared source path",
            )
        text, error = _read_text(value)
        upstream_basis[canonical_key] = str(_as_path(value))
        if error is not None or text is None:
            checks.append(_check(canonical_key + "_reference", False, reference_code))
            return upstream_basis, reference_code, canonical_key + " is unavailable"
        checks.append(_check(canonical_key + "_reference", True))
        marker_status = _marker_status(text, marker_classes)
        upstream_basis[canonical_key + "_marker_classes"] = marker_status
        for marker_class, passed in marker_status.items():
            checks.append(
                _check(
                    canonical_key + "_" + marker_class,
                    passed,
                    None if passed else marker_code,
                )
            )
        if not all(marker_status.values()):
            return (
                upstream_basis,
                marker_code,
                canonical_key + " lacks a required posture marker class",
            )
    return upstream_basis, None, None


def _candidate_result_posture(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str, list[str], str | None, str | None]:
    supplied = request.get("candidate_material_supplied")
    provenance_supplied = request.get("candidate_source_provenance_reference_supplied")
    material_present = "candidate_material" in request
    provenance_present = "candidate_source_provenance_reference" in request

    if supplied is False:
        missing = ["candidate_material_supplied"]
        if not material_present or request.get("candidate_material") is None:
            missing.append("candidate_material")
        if provenance_supplied is not True:
            missing.append("candidate_source_provenance_reference_supplied")
        if not provenance_present or request.get("candidate_source_provenance_reference") is None:
            missing.append("candidate_source_provenance_reference")
        checks.append(
            _check(
                "candidate_material_waiting_posture",
                True,
                detail="candidate material is absent without converting absence into failure",
            )
        )
        return OUTCOME_REQUIRES_CANDIDATE_MATERIAL, missing, None, None

    if supplied is not True:
        return (
            OUTCOME_BLOCKED,
            [],
            "CANDIDATE_MATERIAL_INCOMPLETE",
            "candidate_material_supplied must be exactly true or false",
        )
    if not material_present:
        checks.append(
            _check(
                "candidate_material_waiting_posture",
                True,
                detail="candidate_material is required before reception can be recorded",
            )
        )
        return OUTCOME_REQUIRES_CANDIDATE_MATERIAL, ["candidate_material"], None, None
    material = request.get("candidate_material")
    if material is None or material == "" or material == [] or material == {}:
        checks.append(
            _check(
                "candidate_material_waiting_posture",
                True,
                detail="candidate_material is incomplete without becoming a failed reception",
            )
        )
        return OUTCOME_REQUIRES_CANDIDATE_MATERIAL, ["candidate_material"], None, None
    if not _is_json_compatible(material):
        return (
            OUTCOME_BLOCKED,
            [],
            "CANDIDATE_MATERIAL_NOT_JSON_COMPATIBLE",
            "candidate_material is not JSON-compatible",
        )
    if provenance_supplied is not True or not provenance_present:
        checks.append(
            _check(
                "candidate_source_provenance_reference_waiting_posture",
                True,
                detail="declared source/provenance reference is required before reception can be recorded",
            )
        )
        return (
            OUTCOME_REQUIRES_CANDIDATE_MATERIAL,
            ["candidate_source_provenance_reference"],
            None,
            None,
        )
    provenance = request.get("candidate_source_provenance_reference")
    if provenance is None or provenance == "":
        checks.append(
            _check(
                "candidate_source_provenance_reference_waiting_posture",
                True,
                detail="declared source/provenance reference is incomplete",
            )
        )
        return (
            OUTCOME_REQUIRES_CANDIDATE_MATERIAL,
            ["candidate_source_provenance_reference"],
            None,
            None,
        )
    if not isinstance(provenance, str):
        return (
            OUTCOME_BLOCKED,
            [],
            "CANDIDATE_SOURCE_PROVENANCE_REFERENCE_MISSING",
            "candidate source/provenance reference must be a non-empty string",
        )
    checks.append(_check("candidate_material_available", True))
    checks.append(_check("candidate_material_json_compatible", True))
    checks.append(_check("candidate_source_provenance_reference_supplied", True))
    return OUTCOME_RECORDED, [], None, None


def build_receiver_side_answerable_basis_reception_operation_v0_min_request(
    *,
    target_operation_spec_path: Path | str | None = None,
    reception_boundary_terminal_summary_path: Path | str | None = None,
    intent: str = INTENT_RECORD,
    candidate_material_supplied: bool = False,
    candidate_material: Any = None,
    candidate_source_provenance_reference_supplied: bool = False,
    candidate_source_provenance_reference: str | None = None,
    candidate_id: str = CANDIDATE_ID,
    candidate_type: str = CANDIDATE_TYPE,
    candidate_scope: str = CANDIDATE_SCOPE,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one declared request without discovering material or source paths."""

    request: dict[str, Any] = {
        "intent": intent,
        "target_operation_spec_path": str(
            target_operation_spec_path
            if target_operation_spec_path is not None
            else REPO_ROOT / DEFAULT_OPERATION_SPEC_REFERENCE
        ),
        "reception_boundary_terminal_summary_path": str(
            reception_boundary_terminal_summary_path
            if reception_boundary_terminal_summary_path is not None
            else REPO_ROOT / DEFAULT_RECEPTION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE
        ),
        "candidate_material_supplied": candidate_material_supplied,
        "candidate_material": copy.deepcopy(candidate_material),
        "candidate_source_provenance_reference_supplied": candidate_source_provenance_reference_supplied,
        "candidate_source_provenance_reference": copy.deepcopy(candidate_source_provenance_reference),
        "declared_non_claims": (
            _canonical_non_claims() if declared_non_claims is None else copy.deepcopy(dict(declared_non_claims))
        ),
    }
    request.update(EXPECTED_REQUEST_VALUES)
    request.update(
        {
            "candidate_id": candidate_id,
            "candidate_type": candidate_type,
            "candidate_scope": candidate_scope,
            "receiver_side_answerable_basis_candidate_id": candidate_id,
            "receiver_side_answerable_basis_candidate_type": candidate_type,
            "receiver_side_answerable_basis_candidate_scope": candidate_scope,
        }
    )
    request.update({key: False for key in REQUIRED_FALSE_NON_CLAIMS})
    request.update({key: False for key in PROHIBITED_REQUEST_FLAGS})
    request.update(
        {
            "candidate_material_supplied": candidate_material_supplied,
            "candidate_material": copy.deepcopy(candidate_material),
            "candidate_source_provenance_reference_supplied": (
                candidate_source_provenance_reference_supplied
            ),
            "candidate_source_provenance_reference": copy.deepcopy(
                candidate_source_provenance_reference
            ),
        }
    )
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_reception_operation_v0_min_request(
    **kwargs: Any,
) -> dict[str, Any]:
    """Compatibility spelling for the bounded operation request builder."""

    return build_receiver_side_answerable_basis_reception_operation_v0_min_request(**kwargs)


def resolve_receiver_side_answerable_basis_reception_operation_v0_min(
    declared_receiver_side_answerable_basis_reception_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one candidate-material-only receiver-side reception operation."""

    if declared_receiver_side_answerable_basis_reception_operation is None:
        request: Mapping[str, Any] = build_receiver_side_answerable_basis_reception_operation_v0_min_request()
    elif not isinstance(declared_receiver_side_answerable_basis_reception_operation, Mapping):
        return _result(
            {},
            OUTCOME_BLOCKED,
            [_check("request_mapping", False, "REQUEST_NOT_MAPPING")],
            {},
            [],
            "REQUEST_NOT_MAPPING",
            "declared operation request is not a mapping",
        )
    else:
        request = copy.deepcopy(dict(declared_receiver_side_answerable_basis_reception_operation))

    checks: list[dict[str, Any]] = [_check("request_mapping", True)]
    code, reason = _validate_request_posture(request, checks)
    if code is not None:
        return _result(request, OUTCOME_BLOCKED, checks, {}, [], code, reason)

    if request.get("intent") == INTENT_DO_NOT_RECORD:
        return _result(request, OUTCOME_NOT_RECORDED, checks, {}, [], None, None)

    upstream_basis, code, reason = _evaluate_sources(request, checks)
    if code is not None:
        return _result(request, OUTCOME_BLOCKED, checks, upstream_basis, [], code, reason)

    outcome, missing, code, reason = _candidate_result_posture(request, checks)
    if outcome == OUTCOME_REQUIRES_CANDIDATE_MATERIAL:
        return _result(request, outcome, checks, upstream_basis, missing)
    if code is not None:
        checks.append(_check("candidate_material_posture", False, code, reason))
        return _result(request, OUTCOME_BLOCKED, checks, upstream_basis, [], code, reason)
    return _result(request, OUTCOME_RECORDED, checks, upstream_basis, [])


def resolve_receiver_side_answerable_basis_reception_operation_v0_min_from_path(
    declared_receiver_side_answerable_basis_reception_operation_path: Path | str,
) -> dict[str, Any]:
    """Read exactly one declared JSON request without filesystem discovery."""

    path = _as_path(declared_receiver_side_answerable_basis_reception_operation_path)
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
    return resolve_receiver_side_answerable_basis_reception_operation_v0_min(payload)


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


def write_receiver_side_answerable_basis_reception_operation_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a JSON result without replacing an existing artifact."""

    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceptionOperationV0MinError(
            "WRITE_REFUSED: result is not a mapping"
        )
    requested_path = OUTPUT_ROOT / OUTPUT_FILENAME if output_path is None else Path(output_path)
    target = _next_available_output_path(requested_path)
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as handle:
            json.dump(dict(result), handle, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False)
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisReceptionOperationV0MinError(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
