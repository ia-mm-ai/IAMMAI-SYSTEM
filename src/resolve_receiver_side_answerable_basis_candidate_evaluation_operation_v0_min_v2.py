"""Resolve one bounded eight-dimension candidate-evaluation operation.

The resolver never reads candidate packets or capture directories.  It accepts
only explicit dimension-basis records, validates the selected upstream line,
and preserves supplied basis by bounded metadata rather than by copying it.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2"

OPERATION_ID = "receiver_side_answerable_basis_candidate_evaluation_operation_001"
OPERATION_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = (
    "EVALUATE_ONE_RECORDED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_"
    "ACROSS_EIGHT_SEPARATE_DIMENSIONS_ONLY"
)

PRIOR_EVALUATION_BOUNDARY_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY"
PRIOR_EVALUATION_BOUNDARY_OUTCOME_REQUIRED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_ALLOWED"
PRIOR_EVALUATION_BOUNDARY_RESULT_REQUIRED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_CONSIDERATION_ALLOWED"
PRIOR_EVALUATION_BOUNDARY_RECORDED_REQUIRED = True
PRIOR_EVALUATION_BOUNDARY_RESULT_RECORDED_REQUIRED = True
PRIOR_EVALUATION_CONSIDERATION_ALLOWED_REQUIRED = True
PRIOR_SELECTED_CANDIDATE_RECEPTION_RESULT_REFERENCED_REQUIRED = True
PRIOR_SELECTED_CANDIDATE_MATERIAL_REFERENCED_REQUIRED = True
PRIOR_CANDIDATE_EVALUATED_REQUIRED = False
PRIOR_CANDIDATE_SUFFICIENT_REQUIRED = False
PRIOR_CANDIDATE_INSUFFICIENT_REQUIRED = False
PRIOR_CANDIDATE_INDETERMINATE_REQUIRED = False
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
PRIOR_SECOND_CANDIDATE_RECEIVED_REQUIRED = False
PRIOR_SECOND_CANDIDATE_EVALUATED_REQUIRED = False
PRIOR_REPEATED_EVALUATION_PERMISSION_CREATED_REQUIRED = False
PRIOR_REUSABLE_ROUTE_CREATED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED = False
PRIOR_FAILED_CHECK_COUNT_REQUIRED = 0

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
SELECTED_RECEPTION_OPERATION_ID = "receiver_side_answerable_basis_reception_operation_001"
SELECTED_EVALUATION_BOUNDARY_ID = "receiver_side_answerable_basis_candidate_evaluation_boundary_001"
ADMISSIBLE_FUTURE_ROUTE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_"
    "THEN_CANDIDATE_SUFFICIENCY_BOUNDARY_ONLY"
)

EVALUATION_DIMENSION_IDS = (
    "candidate_structural_correspondence",
    "declared_provenance_posture",
    "receiver_authorship_posture",
    "separate_custody_posture",
    "refusability_posture",
    "could_have_been_withheld_posture",
    "prior_knock_correspondence_posture",
    "capture_record_posture",
)

DIMENSION_RESULT_SATISFIED = "SATISFIED"
DIMENSION_RESULT_NOT_SATISFIED = "NOT_SATISFIED"
DIMENSION_RESULT_INDETERMINATE = "INDETERMINATE"
DIMENSION_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
DIMENSION_RESULT_FAMILY = (
    DIMENSION_RESULT_SATISFIED,
    DIMENSION_RESULT_NOT_SATISFIED,
    DIMENSION_RESULT_INDETERMINATE,
    DIMENSION_RESULT_NOT_EVALUATED,
)

OUTCOME_RECORDED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_RECORDED"
OUTCOME_REQUIRES_EVALUATION_BASIS = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_REQUIRES_EVALUATION_BASIS"
)
OUTCOME_BLOCKED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_REQUIRES_EVALUATION_BASIS,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

OPERATION_RESULT_EVALUATED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATED"
OPERATION_RESULT_INDETERMINATE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_INDETERMINATE"
OPERATION_RESULT_REQUIRES_EVALUATION_BASIS = "REQUIRES_EVALUATION_BASIS"
OPERATION_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
OPERATION_RESULT_FAMILY = (
    OPERATION_RESULT_EVALUATED,
    OPERATION_RESULT_INDETERMINATE,
    OPERATION_RESULT_REQUIRES_EVALUATION_BASIS,
    OPERATION_RESULT_NOT_EVALUATED,
)

INTENT_RECORD = "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION"
INTENT_BLOCK = "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_V2_OPERATION_SPEC_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_V0_MIN_V2_SPEC.md"
)
EVALUATION_BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
SELECTED_EVALUATION_BOUNDARY_RESULT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2/"
    "receiver_side_answerable_basis_candidate_evaluation_boundary_001__"
    "receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_result.json"
)
SELECTED_CANDIDATE_RECEPTION_RESULT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_reception_operation_v0_min/"
    "receiver_side_answerable_basis_reception_operation_001__"
    "receiver_side_answerable_basis_reception_operation_v0_min_result_001.json"
)
GOVERNING_V2_OPERATION_SPEC_PATH = REPO_ROOT / GOVERNING_V2_OPERATION_SPEC_RELATIVE_PATH
EVALUATION_BOUNDARY_TERMINAL_SUMMARY_PATH = REPO_ROOT / EVALUATION_BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH
SELECTED_EVALUATION_BOUNDARY_RESULT_PATH = REPO_ROOT / SELECTED_EVALUATION_BOUNDARY_RESULT_RELATIVE_PATH
SELECTED_CANDIDATE_RECEPTION_RESULT_PATH = REPO_ROOT / SELECTED_CANDIDATE_RECEPTION_RESULT_RELATIVE_PATH
OUTPUT_ROOT = REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2"
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_candidate_evaluation_operation_001__"
    "receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result.json"
)

MAX_BASIS_ITEMS_PER_DIMENSION = 32
MAX_BASIS_REFERENCES_PER_DIMENSION = 32
MAX_SERIALIZED_DIMENSION_BASIS_RECORD_SIZE = 16_384
MAX_SERIALIZED_EVALUATION_REQUEST_SIZE = 131_072


class ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error(Exception):
    """Raised when writing a bounded V2 operation result is refused."""


DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS = (
    "dimension_result_preclaimed",
    "candidate_sufficiency_preclaimed",
    "candidate_insufficiency_preclaimed",
    "candidate_indeterminacy_preclaimed",
    "receiver_attestation_preclaimed",
    "receiver_answerable_receipt_preclaimed",
    "presence_support_preclaimed",
    "authority_preclaimed",
    "standing_preclaimed",
    "truth_preclaimed",
    "evaluator_authority_preclaimed",
    "evaluator_identity_preclaimed",
    "basis_items_are_established_truth",
    "basis_references_are_verified_provenance",
)

DEFAULT_FALSE_FIELDS = (
    "receiver_side_answerable_basis_candidate_sufficient",
    "receiver_side_answerable_basis_candidate_insufficient",
    "receiver_side_answerable_basis_candidate_indeterminate",
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_answerable_receipt_present",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "second_candidate_received",
    "second_candidate_evaluated",
    "repeated_evaluation_permission_created",
    "reusable_route_created",
    "same_candidate_re_evaluation_authorized",
    "dimension_completion_route_created",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "partial_dimension_evaluation_recorded",
    "caller_supplied_dimension_result_accepted",
    "candidate_sufficiency_boundary_created",
    "receiver_attestation_boundary_created",
    "receiver_answerable_receipt_boundary_created",
    "presence_re_evaluation_boundary_created",
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
    "currentness_created",
    "authority_created",
    "standing_created",
    "truth_created",
    "continuity_memory_written",
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
    "synchronization_authorized",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

CONVERSION_FALSE_FIELDS = (
    "evaluation_boundary_permission_to_evaluation_completion",
    "evaluation_boundary_permission_to_evaluation_result",
    "candidate_reception_to_candidate_evaluation_completion",
    "candidate_reception_to_candidate_sufficiency",
    "candidate_reception_to_candidate_insufficiency",
    "candidate_reception_to_receiver_attestation",
    "candidate_reception_to_receiver_answerable_receipt",
    "candidate_reception_to_presence_support",
    "dimension_result_to_candidate_sufficiency",
    "all_dimensions_satisfied_to_candidate_sufficiency",
    "dimension_result_to_receiver_attestation",
    "dimension_result_to_receiver_answerable_receipt",
    "dimension_result_to_presence_support",
    "evaluator_reference_to_authority",
    "evaluator_reference_to_identity",
    "evaluator_reference_to_standing",
    "evaluator_reference_to_truth",
    "basis_items_to_established_truth",
    "basis_references_to_verified_provenance",
    "candidate_evaluation_to_receiver_attestation",
    "candidate_evaluation_to_receiver_answerable_receipt",
    "candidate_evaluation_to_presence_support",
    "candidate_evaluation_to_presence_authorization",
    "candidate_evaluation_to_presence_establishment",
    "candidate_evaluation_to_presence_recording",
    "candidate_evaluation_to_identity",
    "candidate_evaluation_to_relation",
    "candidate_evaluation_to_coupling",
    "candidate_evaluation_to_field_machinery",
    "candidate_evaluation_to_runtime",
    "candidate_evaluation_to_api",
    "candidate_evaluation_to_public_interface",
    "candidate_evaluation_to_public_intake",
    "candidate_evaluation_to_authority",
    "candidate_evaluation_to_standing",
    "candidate_evaluation_to_truth_creation",
    "candidate_evaluation_to_output_authorization",
    "candidate_evaluation_to_action_authorization",
    "candidate_evaluation_to_synchronization",
    "candidate_evaluation_to_follow_on_authorization",
    "candidate_evaluation_to_follow_on_work",
    "same_candidate_evaluation_to_silent_rerun",
    "complete_evaluation_to_later_dimension_extension",
    "changed_files_to_automatic_re_evaluation",
    "newly_noticed_evidence_to_automatic_re_evaluation",
    "selected_candidate_to_retroactive_contaminated_lineage_validation",
)

REQUIRED_FALSE_NON_CLAIMS = tuple(dict.fromkeys(DEFAULT_FALSE_FIELDS + CONVERSION_FALSE_FIELDS))

PROHIBITED_REQUEST_FLAGS = {
    "request_partial_evaluation": "PARTIAL_EVALUATION_REQUESTED",
    "request_later_dimension_completion": "PARTIAL_EVALUATION_REQUESTED",
    "request_candidate_sufficiency": "PROHIBITED_CANDIDATE_SUFFICIENCY_REQUESTED",
    "request_candidate_insufficiency": "PROHIBITED_CANDIDATE_SUFFICIENCY_REQUESTED",
    "request_candidate_indeterminacy": "PROHIBITED_CANDIDATE_SUFFICIENCY_REQUESTED",
    "request_receiver_attestation_creation": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "request_receiver_attestation_support": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "request_receiver_answerable_receipt_creation": "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
    "request_presence_support": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_authorization": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_establishment": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_recording": "PROHIBITED_PRESENCE_REQUESTED",
    "request_identity_creation": "PROHIBITED_IDENTITY_RELATION_OR_COUPLING_REQUESTED",
    "request_relation_creation": "PROHIBITED_IDENTITY_RELATION_OR_COUPLING_REQUESTED",
    "request_coupling_assignment": "PROHIBITED_IDENTITY_RELATION_OR_COUPLING_REQUESTED",
    "request_coupling_creation": "PROHIBITED_IDENTITY_RELATION_OR_COUPLING_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_FIELD_RUNTIME_API_OR_PUBLIC_INTAKE_REQUESTED",
    "request_runtime_creation": "PROHIBITED_FIELD_RUNTIME_API_OR_PUBLIC_INTAKE_REQUESTED",
    "request_api_creation": "PROHIBITED_FIELD_RUNTIME_API_OR_PUBLIC_INTAKE_REQUESTED",
    "request_public_interface_creation": "PROHIBITED_FIELD_RUNTIME_API_OR_PUBLIC_INTAKE_REQUESTED",
    "request_public_intake_creation": "PROHIBITED_FIELD_RUNTIME_API_OR_PUBLIC_INTAKE_REQUESTED",
    "request_mailbox_creation": "PROHIBITED_FIELD_RUNTIME_API_OR_PUBLIC_INTAKE_REQUESTED",
    "request_listener_creation": "PROHIBITED_FIELD_RUNTIME_API_OR_PUBLIC_INTAKE_REQUESTED",
    "request_queue_creation": "PROHIBITED_FIELD_RUNTIME_API_OR_PUBLIC_INTAKE_REQUESTED",
    "request_endpoint_creation": "PROHIBITED_FIELD_RUNTIME_API_OR_PUBLIC_INTAKE_REQUESTED",
    "request_shared_intake_lane_creation": "PROHIBITED_FIELD_RUNTIME_API_OR_PUBLIC_INTAKE_REQUESTED",
    "request_currentness_creation": "PROHIBITED_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_authority_creation": "PROHIBITED_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_standing_creation": "PROHIBITED_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_truth_creation": "PROHIBITED_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_continuity_memory_write": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_output_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_action_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_derivative_reception_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_follow_on_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_follow_on_work_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_second_candidate_reception": "SECOND_CANDIDATE_OR_EVALUATION_REQUESTED",
    "request_second_candidate_evaluation": "SECOND_CANDIDATE_OR_EVALUATION_REQUESTED",
    "request_same_candidate_re_evaluation": "PROHIBITED_REUSABLE_OR_REPEATED_EVALUATION_REQUESTED",
    "request_repeated_evaluation_permission_creation": "PROHIBITED_REUSABLE_OR_REPEATED_EVALUATION_REQUESTED",
    "request_reusable_route_creation": "PROHIBITED_REUSABLE_OR_REPEATED_EVALUATION_REQUESTED",
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
}

BLOCK_CODES = frozenset({
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "V2_OPERATION_SPEC_REFERENCE_MISSING",
    "V2_OPERATION_SPEC_MARKER_MISSING",
    "EVALUATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EVALUATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "EVALUATION_BOUNDARY_RESULT_REFERENCE_MISSING",
    "EVALUATION_BOUNDARY_RESULT_NOT_PARSEABLE",
    "EVALUATION_BOUNDARY_RESULT_NOT_MAPPING",
    "CANDIDATE_RECEPTION_RESULT_REFERENCE_MISSING",
    "CANDIDATE_RECEPTION_RESULT_NOT_PARSEABLE",
    "CANDIDATE_RECEPTION_RESULT_NOT_MAPPING",
    "REQUEST_VALUE_MISMATCH",
    "EVALUATION_BASIS_NOT_MAPPING",
    "EVALUATION_BASIS_OVERSIZED",
    "DIMENSION_BASIS_RECORD_MISSING",
    "DIMENSION_BASIS_RECORD_MALFORMED",
    "DIMENSION_BASIS_RECORD_OVERSIZED",
    "UNKNOWN_DIMENSION_BASIS_RECORD",
    "DIMENSION_BASIS_SELECTED_CANDIDATE_MISMATCH",
    "DIMENSION_BASIS_SELECTED_RECEPTION_OPERATION_MISMATCH",
    "DIMENSION_BASIS_SELECTED_BOUNDARY_MISMATCH",
    "DIMENSION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
    "DIMENSION_RESULT_PRECLAIMED",
    "AGGREGATE_RESULT_PRECLAIMED",
    "PARTIAL_EVALUATION_REQUESTED",
    "SECOND_CANDIDATE_OR_EVALUATION_REQUESTED",
    "PROHIBITED_CANDIDATE_SUFFICIENCY_REQUESTED",
    "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
    "PROHIBITED_PRESENCE_REQUESTED",
    "PROHIBITED_IDENTITY_RELATION_OR_COUPLING_REQUESTED",
    "PROHIBITED_FIELD_RUNTIME_API_OR_PUBLIC_INTAKE_REQUESTED",
    "PROHIBITED_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "PROHIBITED_REUSABLE_OR_REPEATED_EVALUATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "RESULT_POSTURE_PRECLAIMED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
})

V2_SPEC_MARKER_CLASSES = {
    "title": ("# Receiver-Side Answerable Basis Candidate Evaluation Operation V0 Minimum V2 Specification",),
    "identity": (OPERATION_ID, OPERATION_TYPE, OPERATION_SCOPE),
    "atomic_gate": ("Atomic Evaluation-Basis Gate", "all_dimension_basis_records_admissible"),
    "result_precedence": ("Operation-Result Precedence", OPERATION_RESULT_INDETERMINATE),
    "candidate_sufficiency_route": (ADMISSIBLE_FUTURE_ROUTE,),
}
BOUNDARY_SUMMARY_MARKER_CLASSES = {
    "title": ("# Receiver-Side Answerable Basis Candidate Evaluation Boundary Terminal Summary V0",),
    "allowed": (PRIOR_EVALUATION_BOUNDARY_OUTCOME_REQUIRED, PRIOR_EVALUATION_BOUNDARY_RESULT_REQUIRED),
    "not_evaluated": ("candidate_structural_correspondence = NOT_EVALUATED",),
}

DIMENSION_RULES = {
    "candidate_structural_correspondence": {
        "label": "Candidate Structural Correspondence",
        "required_support_postures": (
            "candidate_identity_corresponds",
            "reception_operation_corresponds",
            "evaluation_boundary_corresponds",
            "prior_knock_reference_present",
        ),
        "recognized_contradiction_postures": (
            "selected_candidate_record_mismatch",
            "selected_reception_operation_mismatch",
            "selected_evaluation_boundary_mismatch",
        ),
        "recognized_unresolved_postures": ("prior_knock_reference_unresolved",),
        "non_conversion_statement": "Structural correspondence is not semantic sufficiency.",
    },
    "declared_provenance_posture": {
        "label": "Declared Provenance Posture",
        "required_support_postures": (
            "declared_provenance_reference_present",
            "declared_custody_reference_present",
            "references_internally_addressable",
            "references_structurally_correspond",
        ),
        "recognized_contradiction_postures": (
            "declared_provenance_reference_mismatch",
            "declared_custody_reference_mismatch",
            "references_not_addressable",
            "references_not_structurally_correspond",
        ),
        "recognized_unresolved_postures": ("provenance_posture_unresolved",),
        "non_conversion_statement": "Declared provenance is not verified provenance, identity, authority, standing, or custody distinction.",
    },
    "receiver_authorship_posture": {
        "label": "Receiver-Authorship Posture",
        "required_support_postures": (
            "bounded_receiver_authorship_declaration_present",
            "declaration_structurally_attributable_to_selected_packet",
        ),
        "recognized_contradiction_postures": (
            "receiver_authorship_declaration_mismatch",
            "declaration_not_structurally_attributable",
        ),
        "recognized_unresolved_postures": ("receiver_authorship_posture_unresolved",),
        "non_conversion_statement": "Receiver-authorship posture is not receiver identity or unrestricted authorship certainty.",
    },
    "separate_custody_posture": {
        "label": "Separate-Custody Posture",
        "required_support_postures": (
            "distinct_receiver_controlled_custody_at_occurrence_supported",
            "distinct_receiver_controlled_custody_at_preservation_supported",
            "support_independent_of_filename_directory_working_path_or_declaration_alone",
        ),
        "recognized_contradiction_postures": (
            "same_custody_at_occurrence_established",
            "same_custody_at_preservation_established",
            "support_depends_on_filename_directory_working_path_or_declaration_alone",
        ),
        "recognized_unresolved_postures": ("separate_custody_posture_unresolved",),
        "non_conversion_statement": "Separate custody is not inferred from filename, directory, working path, or declaration alone.",
    },
    "refusability_posture": {
        "label": "Refusability Posture",
        "required_support_postures": (
            "submission_could_have_been_refused_before_source_body_reception",
            "support_independent_of_declaration_alone",
        ),
        "recognized_contradiction_postures": (
            "submission_could_not_have_been_refused_before_source_body_reception",
            "support_depends_on_declaration_alone",
        ),
        "recognized_unresolved_postures": ("refusability_posture_unresolved",),
        "non_conversion_statement": "Refusability posture is not established by declaration alone.",
    },
    "could_have_been_withheld_posture": {
        "label": "Could-Have-Been-Withheld Posture",
        "required_support_postures": (
            "trace_could_have_remained_outside_source_body_custody",
            "support_distinguished_from_separate_custody",
            "support_distinguished_from_refusability",
        ),
        "recognized_contradiction_postures": (
            "trace_could_not_have_remained_outside_source_body_custody",
            "support_not_distinguished_from_separate_custody",
            "support_not_distinguished_from_refusability",
        ),
        "recognized_unresolved_postures": ("withholding_posture_unresolved",),
        "non_conversion_statement": "Could-have-been-withheld posture remains distinct from custody and refusability.",
    },
    "prior_knock_correspondence_posture": {
        "label": "Prior-Knock Correspondence Posture",
        "required_support_postures": (
            "exactly_one_selected_prior_knock_reference_present",
            "candidate_trace_structurally_corresponds_to_selected_prior_knock_reference",
            "no_alternate_knock_reference_selected",
        ),
        "recognized_contradiction_postures": (
            "multiple_or_no_prior_knock_references_selected",
            "candidate_trace_does_not_correspond_to_selected_prior_knock_reference",
            "alternate_knock_reference_selected",
        ),
        "recognized_unresolved_postures": ("prior_knock_correspondence_unresolved",),
        "non_conversion_statement": "Prior-knock correspondence is not attestation, receipt, or presence support.",
    },
    "capture_record_posture": {
        "label": "Capture-Record Posture",
        "required_support_postures": (
            "bounded_capture_record_present",
            "required_hash_record_present",
            "timestamp_record_present",
            "physical_signal_record_present",
            "records_internally_consistent",
            "records_addressable",
        ),
        "recognized_contradiction_postures": (
            "bounded_capture_record_absent",
            "required_hash_record_absent",
            "timestamp_record_absent",
            "physical_signal_record_absent",
            "records_internally_inconsistent",
            "records_not_addressable",
        ),
        "recognized_unresolved_postures": ("capture_record_posture_unresolved",),
        "non_conversion_statement": "Capture records do not validate physical signals, presence, identity, attestation, or truth.",
    },
}

ALLOWED_DIMENSION_BASIS_RECORD_KEYS = frozenset({
    "dimension_id",
    "selected_candidate_id",
    "selected_candidate_reception_operation_id",
    "selected_candidate_evaluation_boundary_id",
    "basis_supplied",
    "basis_items",
    "basis_references",
    "explicit_support_postures",
    "explicit_contradiction_postures",
    "unresolved_postures",
    "evaluator_reference",
    "basis_non_claims",
})

RESULT_PRECLAIM_FIELDS = frozenset({
    "receiver_side_answerable_basis_candidate_evaluation_operation_recorded",
    "receiver_side_answerable_basis_candidate_evaluation_operation_result_recorded",
    "receiver_side_answerable_basis_candidate_evaluation_operation_result",
    "receiver_side_answerable_basis_candidate_evaluated",
    "receiver_side_answerable_basis_candidate_all_dimensions_satisfied",
    "receiver_side_answerable_basis_candidate_any_dimension_not_satisfied",
    "receiver_side_answerable_basis_candidate_any_dimension_indeterminate",
    "candidate_evaluation_operation_exhausted",
    "dimension_result",
    "dimension_results",
    "dimension_evaluated",
    "dimension_established",
})
AGGREGATE_PRECLAIM_FIELDS = frozenset({
    "receiver_side_answerable_basis_candidate_sufficient",
    "receiver_side_answerable_basis_candidate_insufficient",
    "receiver_side_answerable_basis_candidate_indeterminate",
    "requested_aggregate_result",
    "candidate_sufficiency",
    "candidate_insufficiency",
    "candidate_indeterminacy",
})
SECOND_CANDIDATE_FIELDS = frozenset({
    "candidate_material",
    "candidate_packet",
    "candidate_collection",
    "second_candidate",
    "second_candidate_material",
    "alternate_candidate",
    "alternate_candidate_id",
    "alternate_boundary_id",
    "alternate_reception_operation_id",
})

WHAT_REMAINS_OPEN = (
    "separately supplied eight-dimension evaluation basis",
    "actual candidate evaluation",
    "dimension-specific derived results",
    "candidate-sufficiency boundary, if separately selected",
    "receiver-attestation boundary, only after later lawful basis",
    "receiver-answerable-receipt boundary, only after later lawful basis",
    "presence re-evaluation, only after later lawful basis",
    "identity",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "authority",
    "standing",
    "output",
    "action",
    "synchronization",
    "follow-on work",
)


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _as_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _display_path(value: Path | str) -> str:
    path = _as_path(value)
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _check(name: str, passed: bool, block_code: str | None = None) -> dict[str, Any]:
    check: dict[str, Any] = {"name": name, "passed": passed}
    if not passed and block_code is not None:
        check["block_code"] = block_code
        check["failure_code"] = block_code
    return check


def _read_text(path_value: Path | str) -> tuple[str | None, str | None]:
    try:
        path = _as_path(path_value)
        if not path.is_file():
            return None, "not_a_file"
        return path.read_text(encoding="utf-8"), None
    except (OSError, UnicodeDecodeError):
        return None, "unreadable"


def _read_json(path_value: Path | str) -> tuple[Any | None, str | None]:
    text, error = _read_text(path_value)
    if error is not None or text is None:
        return None, error
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        return None, "not_parseable"


def _json_compatible(value: Any) -> bool:
    try:
        json.dumps(value, ensure_ascii=True, allow_nan=False)
        return True
    except (TypeError, ValueError):
        return False


def _serialized_size(value: Any) -> int | None:
    try:
        return len(json.dumps(value, ensure_ascii=True, sort_keys=True, allow_nan=False).encode("utf-8"))
    except (TypeError, ValueError):
        return None


def _mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _exact_bool(value: Any) -> bool:
    return value is True or value is False


def _marker_status(text: str, marker_classes: Mapping[str, Sequence[str]]) -> dict[str, bool]:
    return {name: all(marker in text for marker in markers) for name, markers in marker_classes.items()}


def _dimensions(
    results: Mapping[str, str] | None = None,
    evaluated: bool = False,
    missing: Mapping[str, Sequence[str]] | None = None,
) -> dict[str, dict[str, Any]]:
    value_map = results or {}
    missing_map = missing or {}
    output: dict[str, dict[str, Any]] = {}
    for dimension_id in EVALUATION_DIMENSION_IDS:
        result = value_map.get(dimension_id, DIMENSION_RESULT_NOT_EVALUATED)
        was_evaluated = evaluated and result in {
            DIMENSION_RESULT_SATISFIED,
            DIMENSION_RESULT_NOT_SATISFIED,
            DIMENSION_RESULT_INDETERMINATE,
        }
        output[dimension_id] = {
            "dimension_id": dimension_id,
            "dimension_label": DIMENSION_RULES[dimension_id]["label"],
            "dimension_result": result,
            "dimension_evaluated": was_evaluated,
            "dimension_established": result == DIMENSION_RESULT_SATISFIED and was_evaluated,
            "basis_referenced": was_evaluated,
            "missing_or_inconsistent_dimension_basis": list(missing_map.get(dimension_id, ())),
            "non_conversion_statement": DIMENSION_RULES[dimension_id]["non_conversion_statement"],
        }
    return output


def _operation_state(
    outcome: str,
    operation_result: str,
    gate: Mapping[str, bool],
    dimensions: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    completed = outcome == OUTCOME_RECORDED
    recorded = outcome in (OUTCOME_RECORDED, OUTCOME_REQUIRES_EVALUATION_BASIS)
    results = [dimensions[key]["dimension_result"] for key in EVALUATION_DIMENSION_IDS]
    state: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_evaluation_operation_id": OPERATION_ID,
        "receiver_side_answerable_basis_candidate_evaluation_operation_type": OPERATION_TYPE,
        "receiver_side_answerable_basis_candidate_evaluation_operation_version": OPERATION_VERSION,
        "receiver_side_answerable_basis_candidate_evaluation_operation_scope": OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_evaluation_operation_recorded": recorded,
        "receiver_side_answerable_basis_candidate_evaluation_operation_result_recorded": recorded,
        "receiver_side_answerable_basis_candidate_evaluation_operation_result": operation_result,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "receiver_side_answerable_basis_candidate_evaluated": completed,
        "receiver_side_answerable_basis_candidate_all_dimensions_satisfied": completed and all(
            result == DIMENSION_RESULT_SATISFIED for result in results
        ),
        "receiver_side_answerable_basis_candidate_any_dimension_not_satisfied": completed and any(
            result == DIMENSION_RESULT_NOT_SATISFIED for result in results
        ),
        "receiver_side_answerable_basis_candidate_any_dimension_indeterminate": completed and any(
            result == DIMENSION_RESULT_INDETERMINATE for result in results
        ),
        "candidate_evaluation_operation_exhausted": completed,
    }
    state.update({key: bool(value) for key, value in gate.items()})
    state.update(_canonical_non_claims())
    return state


def _basis_metadata(records: Mapping[str, Any] | None) -> dict[str, Any]:
    if not isinstance(records, Mapping):
        return {}
    preserved: dict[str, Any] = {}
    for dimension_id in EVALUATION_DIMENSION_IDS:
        record = records.get(dimension_id)
        if not isinstance(record, Mapping):
            continue
        support = record.get("explicit_support_postures")
        contradiction = record.get("explicit_contradiction_postures")
        unresolved = record.get("unresolved_postures")
        items = record.get("basis_items")
        references = record.get("basis_references")
        preserved[dimension_id] = {
            "dimension_id": record.get("dimension_id"),
            "selected_candidate_id": record.get("selected_candidate_id"),
            "selected_candidate_reception_operation_id": record.get("selected_candidate_reception_operation_id"),
            "selected_candidate_evaluation_boundary_id": record.get("selected_candidate_evaluation_boundary_id"),
            "basis_supplied": record.get("basis_supplied") is True,
            "basis_item_count": len(items) if isinstance(items, list) else None,
            "basis_reference_count": len(references) if isinstance(references, list) else None,
            "evaluator_reference_supplied": isinstance(record.get("evaluator_reference"), str)
            and bool(record.get("evaluator_reference").strip()),
            "support_posture_key_names": sorted(support) if isinstance(support, Mapping) else [],
            "contradiction_posture_key_names": sorted(contradiction) if isinstance(contradiction, Mapping) else [],
            "unresolved_posture_key_names": sorted(unresolved) if isinstance(unresolved, Mapping) else [],
            "basis_non_claims_validated": _basis_non_claims_valid(record.get("basis_non_claims")),
            "complete_supplied_basis_omitted_from_operation_result": True,
        }
    return preserved


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("receiver_side_answerable_basis_candidate_evaluation_operation", {})
    upstream = result.get("upstream_basis", {})
    dimensions = result.get("receiver_side_answerable_basis_candidate_evaluation_operation_dimensions", {})
    operation = operation if isinstance(operation, Mapping) else {}
    upstream = upstream if isinstance(upstream, Mapping) else {}
    dimension_results = {
        key: value.get("dimension_result")
        for key, value in dimensions.items()
        if isinstance(dimensions, Mapping) and isinstance(value, Mapping)
    }
    dimension_evaluated = {
        key: value.get("dimension_evaluated")
        for key, value in dimensions.items()
        if isinstance(dimensions, Mapping) and isinstance(value, Mapping)
    }
    dimension_established = {
        key: value.get("dimension_established")
        for key, value in dimensions.items()
        if isinstance(dimensions, Mapping) and isinstance(value, Mapping)
    }
    gate = {key: operation.get(key) for key in _atomic_gate_keys()}
    return {
        "outcome": result.get("outcome"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "result_version": result.get("result_version"),
        "resolver_module": result.get("resolver_module"),
        "operation_id": operation.get("operation_id"),
        "operation_type": operation.get("operation_type"),
        "operation_version": operation.get("operation_version"),
        "operation_scope": operation.get("operation_scope"),
        "operation_result": operation.get("receiver_side_answerable_basis_candidate_evaluation_operation_result"),
        "governing_paths": copy.deepcopy(upstream.get("governing_paths", {})),
        "selected_boundary_identity": copy.deepcopy(upstream.get("selected_boundary_identity", {})),
        "selected_candidate_identity": copy.deepcopy(upstream.get("selected_candidate_identity", {})),
        "atomic_gate_postures": gate,
        "dimension_results": dimension_results,
        "dimension_evaluated": dimension_evaluated,
        "dimension_established": dimension_established,
        "candidate_aggregate_postures": {
            key: operation.get(key)
            for key in (
                "receiver_side_answerable_basis_candidate_evaluated",
                "receiver_side_answerable_basis_candidate_all_dimensions_satisfied",
                "receiver_side_answerable_basis_candidate_any_dimension_not_satisfied",
                "receiver_side_answerable_basis_candidate_any_dimension_indeterminate",
            )
        },
        "candidate_evaluation_operation_exhausted": operation.get("candidate_evaluation_operation_exhausted"),
        "candidate_sufficient": operation.get("receiver_side_answerable_basis_candidate_sufficient"),
        "candidate_insufficient": operation.get("receiver_side_answerable_basis_candidate_insufficient"),
        "candidate_indeterminate": operation.get("receiver_side_answerable_basis_candidate_indeterminate"),
        "receiver_attestation_created": operation.get("receiver_attestation_created"),
        "receiver_answerable_receipt_present": operation.get("receiver_answerable_receipt_present"),
        "presence_postures": {key: operation.get(key) for key in ("presence_supported", "presence_authorized", "presence_established", "presence_recorded")},
        "second_repeated_reusable_routes": {
            key: operation.get(key)
            for key in (
                "second_candidate_received",
                "second_candidate_evaluated",
                "repeated_evaluation_permission_created",
                "reusable_route_created",
                "same_candidate_re_evaluation_authorized",
                "dimension_completion_route_created",
            )
        },
        "missing_evaluation_basis": copy.deepcopy(result.get("missing_or_inconsistent_evaluation_basis", [])),
        "marker_validation": copy.deepcopy(upstream.get("marker_validation", {})),
    }


def _atomic_gate_keys() -> tuple[str, ...]:
    return (
        "evaluation_basis_supplied",
        "evaluation_basis_complete",
        "all_dimension_basis_records_present",
        "all_dimension_basis_records_bounded",
        "all_dimension_basis_records_reference_selected_candidate",
        "all_dimension_basis_records_reference_selected_boundary",
        "all_dimension_basis_records_non_result_preclaiming",
        "all_dimension_basis_records_admissible",
    )


def _default_gate(supplied: bool = False) -> dict[str, bool]:
    return {
        "evaluation_basis_supplied": supplied,
        "evaluation_basis_complete": False,
        "all_dimension_basis_records_present": False,
        "all_dimension_basis_records_bounded": False,
        "all_dimension_basis_records_reference_selected_candidate": False,
        "all_dimension_basis_records_reference_selected_boundary": False,
        "all_dimension_basis_records_non_result_preclaiming": False,
        "all_dimension_basis_records_admissible": False,
    }


def _result(
    request: Mapping[str, Any],
    outcome: str,
    operation_result: str,
    checks: list[dict[str, Any]],
    *,
    upstream_basis: Mapping[str, Any] | None = None,
    records: Mapping[str, Any] | None = None,
    gate: Mapping[str, bool] | None = None,
    dimension_results: Mapping[str, str] | None = None,
    missing: Sequence[str] | None = None,
    missing_by_dimension: Mapping[str, Sequence[str]] | None = None,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    clean_gate = dict(gate or _default_gate())
    evaluated = outcome == OUTCOME_RECORDED
    dimensions = _dimensions(dimension_results, evaluated, missing_by_dimension)
    operation = _operation_state(outcome, operation_result, clean_gate, dimensions)
    declared_keys = ("intent", *tuple(_expected_request_values()), "evaluation_basis_supplied")
    result: dict[str, Any] = {
        "receiver_side_answerable_basis_candidate_evaluation_operation_metadata": {
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "selected_command": None,
        },
        "declared_receiver_side_answerable_basis_candidate_evaluation_operation_basis": {
            **{key: copy.deepcopy(request[key]) for key in declared_keys if key in request},
            "dimension_basis_record_count": len(request.get("dimension_basis_records", {}))
            if isinstance(request.get("dimension_basis_records"), Mapping)
            else None,
            "complete_dimension_basis_omitted_from_operation_result": True,
        },
        "upstream_basis": copy.deepcopy(dict(upstream_basis or {})),
        "receiver_side_answerable_basis_candidate_evaluation_operation": operation,
        "receiver_side_answerable_basis_candidate_evaluation_operation_basis": _basis_metadata(records),
        "receiver_side_answerable_basis_candidate_evaluation_operation_dimensions": dimensions,
        "receiver_side_answerable_basis_candidate_evaluation_operation_checks": copy.deepcopy(checks),
        "receiver_side_answerable_basis_candidate_evaluation_operation_statement": {
            "operation_records_one_selected_candidate_evaluation_only": outcome in (OUTCOME_RECORDED, OUTCOME_REQUIRES_EVALUATION_BASIS),
            "partial_evaluation_does_not_stand": True,
            "complete_supplied_basis_omitted_from_operation_result": True,
            "candidate_material_omitted_from_operation_result": True,
            "candidate_sufficiency_remains_false": True,
            "receiver_attestation_remains_false": True,
            "receiver_answerable_receipt_remains_false": True,
            "presence_remains_false": True,
            "result_level_non_claims_canonical_false": True,
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
            "open_does_not_mean_next_unless_separately_selected": True,
        },
        "receiver_side_answerable_basis_candidate_evaluation_operation_non_meaning": {
            "supplied_evaluation_basis_is_not_dimension_result": True,
            "dimension_result_is_not_candidate_sufficiency": True,
            "all_dimensions_satisfied_is_not_candidate_sufficiency": True,
            "not_satisfied_is_not_candidate_insufficiency": True,
            "dimension_indeterminacy_is_not_candidate_level_indeterminacy": True,
            "evaluation_is_not_attestation_receipt_or_presence": True,
            "evaluator_reference_is_not_authority_identity_standing_or_truth": True,
            "basis_items_and_references_are_not_derived_as_truth": True,
        },
        "operation_result_detail": {
            "operation_result": operation_result,
            "all_eight_dimensions_evaluated": evaluated,
            "candidate_evaluation_operation_exhausted": operation["candidate_evaluation_operation_exhausted"],
        },
        "permitted_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "blocked_routes": list(CONVERSION_FALSE_FIELDS),
        "missing_or_inconsistent_evaluation_basis": list(missing or ()),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": code if outcome == OUTCOME_BLOCKED else None,
            "block_code": code if outcome == OUTCOME_BLOCKED else None,
            "reason": reason if outcome == OUTCOME_BLOCKED else None,
        },
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "failed_check_count": sum(check.get("passed") is False for check in checks),
        "passed_check_count": sum(check.get("passed") is True for check in checks),
    }
    result["receiver_side_answerable_basis_candidate_evaluation_operation_summary"] = _summary_from_result(result)
    return result


def _add_failure(checks: list[dict[str, Any]], name: str, code: str) -> None:
    checks.append(_check(name, False, code))


def _basis_non_claims_valid(value: Any) -> bool:
    return isinstance(value, Mapping) and all(value.get(key) is False for key in DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS)


def _declared_non_claims_valid(value: Any) -> bool:
    return isinstance(value, Mapping) and all(value.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _expected_request_values() -> dict[str, Any]:
    return {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "governing_v2_operation_specification_path": str(GOVERNING_V2_OPERATION_SPEC_RELATIVE_PATH),
        "evaluation_boundary_terminal_summary_path": str(EVALUATION_BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH),
        "selected_evaluation_boundary_artifact_path": str(SELECTED_EVALUATION_BOUNDARY_RESULT_RELATIVE_PATH),
        "selected_candidate_reception_artifact_path": str(SELECTED_CANDIDATE_RECEPTION_RESULT_RELATIVE_PATH),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "prior_evaluation_boundary_type": PRIOR_EVALUATION_BOUNDARY_TYPE,
        "prior_evaluation_boundary_outcome_required": PRIOR_EVALUATION_BOUNDARY_OUTCOME_REQUIRED,
        "prior_evaluation_boundary_result_required": PRIOR_EVALUATION_BOUNDARY_RESULT_REQUIRED,
        "prior_evaluation_boundary_recorded_required": PRIOR_EVALUATION_BOUNDARY_RECORDED_REQUIRED,
        "prior_evaluation_boundary_result_recorded_required": PRIOR_EVALUATION_BOUNDARY_RESULT_RECORDED_REQUIRED,
        "prior_evaluation_consideration_allowed_required": PRIOR_EVALUATION_CONSIDERATION_ALLOWED_REQUIRED,
        "prior_selected_candidate_reception_result_referenced_required": PRIOR_SELECTED_CANDIDATE_RECEPTION_RESULT_REFERENCED_REQUIRED,
        "prior_selected_candidate_material_referenced_required": PRIOR_SELECTED_CANDIDATE_MATERIAL_REFERENCED_REQUIRED,
        "prior_candidate_evaluated_required": PRIOR_CANDIDATE_EVALUATED_REQUIRED,
        "prior_candidate_sufficient_required": PRIOR_CANDIDATE_SUFFICIENT_REQUIRED,
        "prior_candidate_insufficient_required": PRIOR_CANDIDATE_INSUFFICIENT_REQUIRED,
        "prior_candidate_indeterminate_required": PRIOR_CANDIDATE_INDETERMINATE_REQUIRED,
        "prior_receiver_attestation_created_required": PRIOR_RECEIVER_ATTESTATION_CREATED_REQUIRED,
        "prior_receiver_attestation_supported_required": PRIOR_RECEIVER_ATTESTATION_SUPPORTED_REQUIRED,
        "prior_receiver_answerable_receipt_present_required": PRIOR_RECEIVER_ANSWERABLE_RECEIPT_PRESENT_REQUIRED,
        "prior_custody_distinct_required": PRIOR_CUSTODY_DISTINCT_REQUIRED,
        "prior_refusable_required": PRIOR_REFUSABLE_REQUIRED,
        "prior_could_have_been_withheld_required": PRIOR_COULD_HAVE_BEEN_WITHHELD_REQUIRED,
        "prior_presence_supported_required": PRIOR_PRESENCE_SUPPORTED_REQUIRED,
        "prior_presence_authorized_required": PRIOR_PRESENCE_AUTHORIZED_REQUIRED,
        "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
        "prior_presence_recorded_required": PRIOR_PRESENCE_RECORDED_REQUIRED,
        "prior_second_candidate_received_required": PRIOR_SECOND_CANDIDATE_RECEIVED_REQUIRED,
        "prior_second_candidate_evaluated_required": PRIOR_SECOND_CANDIDATE_EVALUATED_REQUIRED,
        "prior_repeated_evaluation_permission_created_required": PRIOR_REPEATED_EVALUATION_PERMISSION_CREATED_REQUIRED,
        "prior_reusable_route_created_required": PRIOR_REUSABLE_ROUTE_CREATED_REQUIRED,
        "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
        "prior_follow_on_work_authorized_required": PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED,
        "prior_failed_check_count_required": PRIOR_FAILED_CHECK_COUNT_REQUIRED,
    }


def _validate_request(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> tuple[str | None, str | None]:
    intent = request.get("intent")
    if intent == INTENT_BLOCK:
        return "EXPLICIT_BLOCK_REQUESTED", "explicit block intent was requested"
    if intent not in SUPPORTED_INTENTS:
        return "UNSUPPORTED_INTENT", "intent is not supported"
    for field, expected in _expected_request_values().items():
        valid = request.get(field) == expected
        checks.append(_check(field, valid, "REQUEST_VALUE_MISMATCH"))
        if not valid:
            return "REQUEST_VALUE_MISMATCH", field + " does not match the bounded operation request"
    if request.get("evaluation_basis_supplied") not in (True, False):
        return "REQUEST_VALUE_MISMATCH", "evaluation_basis_supplied must be an exact boolean"
    if not _declared_non_claims_valid(request.get("declared_non_claims")):
        return "NON_CLAIM_MISSING_OR_FLIPPED", "declared_non_claims must contain every required false posture"
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        value = request.get(field, False)
        valid = value is False
        checks.append(_check(field, valid, code))
        if not valid:
            return code, field + " requests a prohibited conversion"
    for field in RESULT_PRECLAIM_FIELDS:
        if field in {
            "receiver_side_answerable_basis_candidate_evaluation_operation_result",
            "dimension_result",
            "dimension_results",
        } and field in request:
            return "RESULT_POSTURE_PRECLAIMED", field + " may not be supplied by the caller"
        if field in request and request[field] not in (None, False, OPERATION_RESULT_NOT_EVALUATED):
            return "RESULT_POSTURE_PRECLAIMED", field + " may not be pre-claimed"
    for field in AGGREGATE_PRECLAIM_FIELDS:
        if field in request and request[field] not in (None, False):
            return "AGGREGATE_RESULT_PRECLAIMED", field + " may not be pre-claimed"
    for field in REQUIRED_FALSE_NON_CLAIMS:
        if field in request and request[field] not in (None, False):
            return "RESULT_POSTURE_PRECLAIMED", field + " may not be pre-claimed"
    for field in EVALUATION_DIMENSION_IDS:
        if field in request:
            return "RESULT_POSTURE_PRECLAIMED", field + " may not be supplied as a top-level result posture"
    for field in SECOND_CANDIDATE_FIELDS:
        if field in request:
            return "SECOND_CANDIDATE_OR_EVALUATION_REQUESTED", field + " is not an admissible operation input"
    allowed = {
        "intent",
        "evaluation_basis_supplied",
        "dimension_basis_records",
        "declared_non_claims",
        *tuple(_expected_request_values()),
        *tuple(PROHIBITED_REQUEST_FLAGS),
    }
    unknown = set(request).difference(allowed)
    if unknown:
        return "REQUEST_VALUE_MISMATCH", "declared request contains unknown fields"
    return None, None


def _validate_upstream(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str | None, str | None, dict[str, Any]]:
    upstream: dict[str, Any] = {
        "governing_paths": {
            "governing_v2_operation_specification_path": request.get("governing_v2_operation_specification_path"),
            "evaluation_boundary_terminal_summary_path": request.get("evaluation_boundary_terminal_summary_path"),
            "selected_evaluation_boundary_artifact_path": request.get("selected_evaluation_boundary_artifact_path"),
            "selected_candidate_reception_artifact_path": request.get("selected_candidate_reception_artifact_path"),
        },
        "selected_boundary_identity": {},
        "selected_candidate_identity": {},
        "marker_validation": {},
    }
    spec_text, error = _read_text(request["governing_v2_operation_specification_path"])
    if error is not None or spec_text is None:
        return "V2_OPERATION_SPEC_REFERENCE_MISSING", "governing V2 operation specification is unavailable", upstream
    spec_markers = _marker_status(spec_text, V2_SPEC_MARKER_CLASSES)
    upstream["marker_validation"]["governing_v2_operation_specification"] = spec_markers
    checks.append(_check("governing_v2_operation_specification_markers", all(spec_markers.values()), "V2_OPERATION_SPEC_MARKER_MISSING"))
    if not all(spec_markers.values()):
        return "V2_OPERATION_SPEC_MARKER_MISSING", "governing V2 operation specification markers are incomplete", upstream

    terminal_text, error = _read_text(request["evaluation_boundary_terminal_summary_path"])
    if error is not None or terminal_text is None:
        return "EVALUATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING", "completed evaluation-boundary terminal summary is unavailable", upstream
    terminal_markers = _marker_status(terminal_text, BOUNDARY_SUMMARY_MARKER_CLASSES)
    upstream["marker_validation"]["evaluation_boundary_terminal_summary"] = terminal_markers
    checks.append(_check("evaluation_boundary_terminal_summary_markers", all(terminal_markers.values()), "EVALUATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING"))
    if not all(terminal_markers.values()):
        return "EVALUATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING", "completed boundary summary markers are incomplete", upstream

    boundary_artifact, error = _read_json(request["selected_evaluation_boundary_artifact_path"])
    if error in ("not_a_file", "unreadable"):
        return "EVALUATION_BOUNDARY_RESULT_REFERENCE_MISSING", "selected evaluation-boundary result is unavailable", upstream
    if error == "not_parseable":
        return "EVALUATION_BOUNDARY_RESULT_NOT_PARSEABLE", "selected evaluation-boundary result is not parseable JSON", upstream
    if not isinstance(boundary_artifact, Mapping):
        return "EVALUATION_BOUNDARY_RESULT_NOT_MAPPING", "selected evaluation-boundary result is not a mapping", upstream
    boundary = boundary_artifact.get("receiver_side_answerable_basis_candidate_evaluation_boundary")
    dimensions = boundary_artifact.get("receiver_side_answerable_basis_candidate_evaluation_dimensions")
    if not isinstance(boundary, Mapping) or not isinstance(dimensions, Mapping):
        return "EVALUATION_BOUNDARY_RESULT_NOT_MAPPING", "selected evaluation-boundary result lacks bounded sections", upstream
    boundary_requirements = {
        "outcome": PRIOR_EVALUATION_BOUNDARY_OUTCOME_REQUIRED,
        "failed_check_count": PRIOR_FAILED_CHECK_COUNT_REQUIRED,
        "boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
        "boundary_type": PRIOR_EVALUATION_BOUNDARY_TYPE,
        "receiver_side_answerable_basis_candidate_evaluation_boundary_recorded": PRIOR_EVALUATION_BOUNDARY_RECORDED_REQUIRED,
        "receiver_side_answerable_basis_candidate_evaluation_boundary_result_recorded": PRIOR_EVALUATION_BOUNDARY_RESULT_RECORDED_REQUIRED,
        "receiver_side_answerable_basis_candidate_evaluation_boundary_result": PRIOR_EVALUATION_BOUNDARY_RESULT_REQUIRED,
        "receiver_side_answerable_basis_candidate_evaluation_consideration_allowed": PRIOR_EVALUATION_CONSIDERATION_ALLOWED_REQUIRED,
        "selected_candidate_reception_result_referenced": PRIOR_SELECTED_CANDIDATE_RECEPTION_RESULT_REFERENCED_REQUIRED,
        "selected_candidate_material_referenced": PRIOR_SELECTED_CANDIDATE_MATERIAL_REFERENCED_REQUIRED,
        "receiver_side_answerable_basis_candidate_evaluated": PRIOR_CANDIDATE_EVALUATED_REQUIRED,
        "receiver_side_answerable_basis_candidate_sufficient": PRIOR_CANDIDATE_SUFFICIENT_REQUIRED,
        "receiver_side_answerable_basis_candidate_insufficient": PRIOR_CANDIDATE_INSUFFICIENT_REQUIRED,
        "receiver_side_answerable_basis_candidate_indeterminate": PRIOR_CANDIDATE_INDETERMINATE_REQUIRED,
        "receiver_attestation_created": PRIOR_RECEIVER_ATTESTATION_CREATED_REQUIRED,
        "receiver_attestation_supported": PRIOR_RECEIVER_ATTESTATION_SUPPORTED_REQUIRED,
        "receiver_answerable_receipt_present": PRIOR_RECEIVER_ANSWERABLE_RECEIPT_PRESENT_REQUIRED,
        "receiver_answerable_basis_custody_distinct": PRIOR_CUSTODY_DISTINCT_REQUIRED,
        "receiver_answerable_basis_refusable": PRIOR_REFUSABLE_REQUIRED,
        "receiver_answerable_basis_could_have_been_withheld": PRIOR_COULD_HAVE_BEEN_WITHHELD_REQUIRED,
        "presence_supported": PRIOR_PRESENCE_SUPPORTED_REQUIRED,
        "presence_authorized": PRIOR_PRESENCE_AUTHORIZED_REQUIRED,
        "presence_established": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
        "presence_recorded": PRIOR_PRESENCE_RECORDED_REQUIRED,
        "second_candidate_received": PRIOR_SECOND_CANDIDATE_RECEIVED_REQUIRED,
        "second_candidate_evaluated": PRIOR_SECOND_CANDIDATE_EVALUATED_REQUIRED,
        "repeated_evaluation_permission_created": PRIOR_REPEATED_EVALUATION_PERMISSION_CREATED_REQUIRED,
        "reusable_route_created": PRIOR_REUSABLE_ROUTE_CREATED_REQUIRED,
        "follow_on_authorized": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
        "follow_on_work_authorized": PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED,
    }
    for field, expected in boundary_requirements.items():
        actual = boundary_artifact.get(field) if field in ("outcome", "failed_check_count") else boundary.get(field)
        valid = actual == expected
        checks.append(_check("boundary." + field, valid, "REQUEST_VALUE_MISMATCH"))
        if not valid:
            return "REQUEST_VALUE_MISMATCH", "selected boundary posture does not meet " + field, upstream
    for dimension_id in EVALUATION_DIMENSION_IDS:
        entry = dimensions.get(dimension_id)
        valid = isinstance(entry, Mapping) and (
            entry.get("evaluation_status", entry.get("dimension_result")) == DIMENSION_RESULT_NOT_EVALUATED
        ) and entry.get("established", entry.get("dimension_established")) is False
        checks.append(_check("boundary.dimension." + dimension_id, valid, "REQUEST_VALUE_MISMATCH"))
        if not valid:
            return "REQUEST_VALUE_MISMATCH", "upstream dimension is not lawfully not evaluated", upstream
    upstream["selected_boundary_identity"] = {
        "boundary_id": boundary.get("boundary_id"),
        "boundary_type": boundary.get("boundary_type"),
        "boundary_result": boundary.get("receiver_side_answerable_basis_candidate_evaluation_boundary_result"),
    }

    reception_artifact, error = _read_json(request["selected_candidate_reception_artifact_path"])
    if error in ("not_a_file", "unreadable"):
        return "CANDIDATE_RECEPTION_RESULT_REFERENCE_MISSING", "selected candidate-reception result is unavailable", upstream
    if error == "not_parseable":
        return "CANDIDATE_RECEPTION_RESULT_NOT_PARSEABLE", "selected candidate-reception result is not parseable JSON", upstream
    if not isinstance(reception_artifact, Mapping):
        return "CANDIDATE_RECEPTION_RESULT_NOT_MAPPING", "selected candidate-reception result is not a mapping", upstream
    reception = reception_artifact.get("receiver_side_answerable_basis_reception_operation")
    if not isinstance(reception, Mapping):
        return "CANDIDATE_RECEPTION_RESULT_NOT_MAPPING", "selected candidate-reception operation is not a mapping", upstream
    reception_requirements = {
        "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED",
        "failed_check_count": 0,
        "receiver_side_answerable_basis_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "candidate_material_supplied": True,
        "candidate_material_received": True,
        "candidate_material_recorded": True,
        "candidate_material_preserved": True,
        "receiver_side_answerable_basis_candidate_received": True,
        "receiver_side_answerable_basis_candidate_recorded": True,
        "receiver_side_answerable_basis_candidate_evaluated": False,
    }
    for field, expected in reception_requirements.items():
        actual = reception_artifact.get(field) if field in ("outcome", "failed_check_count") else reception.get(field)
        valid = actual == expected
        checks.append(_check("reception." + field, valid, "REQUEST_VALUE_MISMATCH"))
        if not valid:
            return "REQUEST_VALUE_MISMATCH", "selected reception posture does not meet " + field, upstream
    upstream["selected_candidate_identity"] = {
        "candidate_id": reception.get("receiver_side_answerable_basis_candidate_id"),
        "candidate_type": reception.get("receiver_side_answerable_basis_candidate_type"),
        "candidate_scope": reception.get("receiver_side_answerable_basis_candidate_scope"),
        "reception_operation_id": reception.get("receiver_side_answerable_basis_reception_operation_id"),
    }
    upstream["selected_artifacts_validated"] = True
    return None, None, upstream


def _validate_posture_mapping(
    record: Mapping[str, Any],
    field: str,
    expected_keys: Sequence[str],
    missing: list[str],
) -> tuple[bool, str | None]:
    posture = record.get(field)
    if not isinstance(posture, Mapping):
        return False, "DIMENSION_BASIS_RECORD_MALFORMED"
    unknown = set(posture).difference(expected_keys)
    if unknown:
        return False, "DIMENSION_BASIS_RECORD_MALFORMED"
    for key in expected_keys:
        if key not in posture:
            missing.append(field + "." + key)
        elif not _exact_bool(posture.get(key)):
            return False, "DIMENSION_BASIS_RECORD_MALFORMED"
    return True, None


def _dimension_record_preclaim_code(record: Mapping[str, Any]) -> str | None:
    for key in record:
        if key in {"dimension_result", "requested_dimension_result", "result", "requested_result"}:
            return "DIMENSION_RESULT_PRECLAIMED"
        if key in AGGREGATE_PRECLAIM_FIELDS or key in {
            "candidate_sufficiency_preclaimed",
            "candidate_insufficiency_preclaimed",
            "candidate_indeterminacy_preclaimed",
        }:
            return "AGGREGATE_RESULT_PRECLAIMED"
    return None


def _validate_dimension_record(
    dimension_id: str, record: Any
) -> tuple[str | None, str | None, list[str]]:
    missing: list[str] = []
    if not isinstance(record, Mapping):
        return "DIMENSION_BASIS_RECORD_MALFORMED", "dimension basis record is not a mapping", missing
    preclaim = _dimension_record_preclaim_code(record)
    if preclaim is not None:
        return preclaim, "dimension basis record pre-claims a result", missing
    if set(record).difference(ALLOWED_DIMENSION_BASIS_RECORD_KEYS):
        return "DIMENSION_BASIS_RECORD_MALFORMED", "dimension basis record contains unknown keys", missing
    size = _serialized_size(record)
    if size is None:
        return "DIMENSION_BASIS_RECORD_MALFORMED", "dimension basis record is not JSON compatible", missing
    if size > MAX_SERIALIZED_DIMENSION_BASIS_RECORD_SIZE:
        return "DIMENSION_BASIS_RECORD_OVERSIZED", "dimension basis record exceeds its bounded size", missing
    if record.get("dimension_id") != dimension_id:
        return "DIMENSION_BASIS_RECORD_MALFORMED", "dimension_id does not match the record key", missing
    if record.get("selected_candidate_id") != CANDIDATE_ID:
        return "DIMENSION_BASIS_SELECTED_CANDIDATE_MISMATCH", "dimension basis record selects another candidate", missing
    if record.get("selected_candidate_reception_operation_id") != SELECTED_RECEPTION_OPERATION_ID:
        return "DIMENSION_BASIS_SELECTED_RECEPTION_OPERATION_MISMATCH", "dimension basis record selects another reception operation", missing
    if record.get("selected_candidate_evaluation_boundary_id") != SELECTED_EVALUATION_BOUNDARY_ID:
        return "DIMENSION_BASIS_SELECTED_BOUNDARY_MISMATCH", "dimension basis record selects another evaluation boundary", missing
    if record.get("basis_supplied") is not True:
        missing.append("basis_supplied")
    items = record.get("basis_items")
    references = record.get("basis_references")
    if not isinstance(items, list) or not _json_compatible(items):
        return "DIMENSION_BASIS_RECORD_MALFORMED", "basis_items must be a JSON-compatible list", missing
    if not isinstance(references, list) or not _json_compatible(references):
        return "DIMENSION_BASIS_RECORD_MALFORMED", "basis_references must be a JSON-compatible list", missing
    if len(items) > MAX_BASIS_ITEMS_PER_DIMENSION or len(references) > MAX_BASIS_REFERENCES_PER_DIMENSION:
        return "DIMENSION_BASIS_RECORD_OVERSIZED", "dimension basis item or reference count exceeds its maximum", missing
    evaluator_reference = record.get("evaluator_reference")
    if not isinstance(evaluator_reference, str) or not evaluator_reference.strip():
        return "DIMENSION_BASIS_RECORD_MALFORMED", "evaluator_reference must be a non-empty string", missing
    if not _basis_non_claims_valid(record.get("basis_non_claims")):
        return "DIMENSION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED", "dimension basis non-claims must be exact false", missing
    rules = DIMENSION_RULES[dimension_id]
    for field, expected_keys in (
        ("explicit_support_postures", rules["required_support_postures"]),
        ("explicit_contradiction_postures", rules["recognized_contradiction_postures"]),
        ("unresolved_postures", rules["recognized_unresolved_postures"]),
    ):
        valid, code = _validate_posture_mapping(record, field, expected_keys, missing)
        if not valid:
            return code, field + " does not match the bounded rule table", missing
    return None, None, missing


def _evaluate_basis(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[
    str | None,
    str | None,
    dict[str, bool],
    dict[str, str] | None,
    list[str],
    dict[str, list[str]],
]:
    supplied = request.get("evaluation_basis_supplied") is True
    gate = _default_gate(supplied)
    missing: list[str] = []
    missing_by_dimension: dict[str, list[str]] = {}
    records = request.get("dimension_basis_records")
    if not isinstance(records, Mapping):
        return "EVALUATION_BASIS_NOT_MAPPING", "dimension_basis_records must be a mapping", gate, None, missing, missing_by_dimension
    request_size = _serialized_size({
        "evaluation_basis_supplied": request.get("evaluation_basis_supplied"),
        "dimension_basis_records": records,
    })
    if request_size is None:
        return "EVALUATION_BASIS_NOT_MAPPING", "evaluation basis is not JSON compatible", gate, None, missing, missing_by_dimension
    if request_size > MAX_SERIALIZED_EVALUATION_REQUEST_SIZE:
        return "EVALUATION_BASIS_OVERSIZED", "evaluation basis exceeds its bounded size", gate, None, missing, missing_by_dimension
    unknown = sorted(set(records).difference(EVALUATION_DIMENSION_IDS))
    if unknown:
        return "UNKNOWN_DIMENSION_BASIS_RECORD", "unknown dimension basis record supplied", gate, None, missing, missing_by_dimension
    if not supplied:
        missing.extend("dimension_basis_record:" + dimension_id for dimension_id in EVALUATION_DIMENSION_IDS)
        return None, None, gate, None, missing, missing_by_dimension
    absent = [dimension_id for dimension_id in EVALUATION_DIMENSION_IDS if dimension_id not in records]
    if absent:
        for dimension_id in absent:
            item = "dimension_basis_record:" + dimension_id
            missing.append(item)
            missing_by_dimension[dimension_id] = [item]
        return None, None, gate, None, missing, missing_by_dimension
    gate["all_dimension_basis_records_present"] = True
    bounded = True
    selected_candidate = True
    selected_boundary = True
    non_preclaiming = True
    for dimension_id in EVALUATION_DIMENSION_IDS:
        code, reason, record_missing = _validate_dimension_record(dimension_id, records[dimension_id])
        if code is not None:
            if code == "DIMENSION_BASIS_RECORD_MISSING":
                missing_by_dimension[dimension_id] = record_missing or ["dimension_basis_record:" + dimension_id]
                missing.extend(missing_by_dimension[dimension_id])
                continue
            return code, reason, gate, None, missing, missing_by_dimension
        if record_missing:
            bounded = False
            missing_by_dimension[dimension_id] = record_missing
            missing.extend(dimension_id + "." + value for value in record_missing)
    gate["all_dimension_basis_records_bounded"] = bounded
    gate["all_dimension_basis_records_reference_selected_candidate"] = selected_candidate
    gate["all_dimension_basis_records_reference_selected_boundary"] = selected_boundary
    gate["all_dimension_basis_records_non_result_preclaiming"] = non_preclaiming
    complete = bounded and not missing
    gate["evaluation_basis_complete"] = complete
    gate["all_dimension_basis_records_admissible"] = complete
    if not complete:
        return None, None, gate, None, missing, missing_by_dimension
    results: dict[str, str] = {}
    for dimension_id in EVALUATION_DIMENSION_IDS:
        record = records[dimension_id]
        rules = DIMENSION_RULES[dimension_id]
        supports = record["explicit_support_postures"]
        contradictions = record["explicit_contradiction_postures"]
        unresolved = record["unresolved_postures"]
        if all(supports[key] is True for key in rules["required_support_postures"]) and all(
            contradictions[key] is False for key in rules["recognized_contradiction_postures"]
        ) and all(unresolved[key] is False for key in rules["recognized_unresolved_postures"]):
            results[dimension_id] = DIMENSION_RESULT_SATISFIED
        elif any(contradictions[key] is True for key in rules["recognized_contradiction_postures"]):
            results[dimension_id] = DIMENSION_RESULT_NOT_SATISFIED
        else:
            results[dimension_id] = DIMENSION_RESULT_INDETERMINATE
        checks.append(_check("dimension_rule." + dimension_id, True))
    return None, None, gate, results, missing, missing_by_dimension


def build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build the only bounded request shape; no basis is supplied by default."""
    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **_expected_request_values(),
        "evaluation_basis_supplied": False,
        "dimension_basis_records": {},
        "declared_non_claims": _canonical_non_claims(),
    }
    request.update({field: False for field in PROHIBITED_REQUEST_FLAGS})
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build the declared request using the same bounded operation shape."""
    return build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_request(**overrides)


def resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2(
    declared_receiver_side_answerable_basis_candidate_evaluation_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve exactly one bounded operation without discovering evaluation basis."""
    checks: list[dict[str, Any]] = []
    if declared_receiver_side_answerable_basis_candidate_evaluation_operation is None:
        request = build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_request()
    elif not isinstance(declared_receiver_side_answerable_basis_candidate_evaluation_operation, Mapping):
        request = build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_request()
        _add_failure(checks, "declared_request_mapping", "REQUEST_NOT_MAPPING")
        return _result(
            request,
            OUTCOME_BLOCKED,
            OPERATION_RESULT_NOT_EVALUATED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="declared operation request is not a mapping",
        )
    else:
        request = copy.deepcopy(dict(declared_receiver_side_answerable_basis_candidate_evaluation_operation))

    code, reason = _validate_request(request, checks)
    if code is not None:
        _add_failure(checks, "declared_request", code)
        return _result(request, OUTCOME_BLOCKED, OPERATION_RESULT_NOT_EVALUATED, checks, code=code, reason=reason)
    if request["intent"] == INTENT_DO_NOT_RECORD:
        return _result(request, OUTCOME_NOT_RECORDED, OPERATION_RESULT_NOT_EVALUATED, checks)

    code, reason, upstream = _validate_upstream(request, checks)
    if code is not None:
        _add_failure(checks, "upstream_basis", code)
        return _result(request, OUTCOME_BLOCKED, OPERATION_RESULT_NOT_EVALUATED, checks, upstream_basis=upstream, code=code, reason=reason)

    code, reason, gate, results, missing, missing_by_dimension = _evaluate_basis(request, checks)
    records = request.get("dimension_basis_records") if isinstance(request.get("dimension_basis_records"), Mapping) else None
    if code is not None:
        _add_failure(checks, "evaluation_basis", code)
        return _result(
            request,
            OUTCOME_BLOCKED,
            OPERATION_RESULT_NOT_EVALUATED,
            checks,
            upstream_basis=upstream,
            records=records,
            gate=gate,
            missing=missing,
            missing_by_dimension=missing_by_dimension,
            code=code,
            reason=reason,
        )
    if results is None:
        return _result(
            request,
            OUTCOME_REQUIRES_EVALUATION_BASIS,
            OPERATION_RESULT_REQUIRES_EVALUATION_BASIS,
            checks,
            upstream_basis=upstream,
            records=records,
            gate=gate,
            missing=missing,
            missing_by_dimension=missing_by_dimension,
        )
    operation_result = (
        OPERATION_RESULT_INDETERMINATE
        if any(result == DIMENSION_RESULT_INDETERMINATE for result in results.values())
        else OPERATION_RESULT_EVALUATED
    )
    return _result(
        request,
        OUTCOME_RECORDED,
        operation_result,
        checks,
        upstream_basis=upstream,
        records=records,
        gate=gate,
        dimension_results=results,
        missing=missing,
        missing_by_dimension=missing_by_dimension,
    )


def resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_from_path(
    declared_receiver_side_answerable_basis_candidate_evaluation_operation_path: Path | str,
) -> dict[str, Any]:
    """Read one declared JSON request path and resolve it without discovery."""
    payload, error = _read_json(declared_receiver_side_answerable_basis_candidate_evaluation_operation_path)
    if error is not None or not isinstance(payload, Mapping):
        request = build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_request()
        checks = [_check("declared_request_path", False, "REQUEST_NOT_MAPPING")]
        return _result(
            request,
            OUTCOME_BLOCKED,
            OPERATION_RESULT_NOT_EVALUATED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="declared operation request path is unavailable, not parseable, or not a mapping",
        )
    return resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2(payload)


def build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact, material-omitting summary of a bounded result."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error(
            "WRITE_REFUSED: result must be a mapping"
        )
    return _summary_from_result(result)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(path.stem + "_" + f"{index:03d}" + path.suffix)
        if not candidate.exists():
            return candidate
    raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def _contains_copied_material(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if key in {"candidate_material", "candidate_packet", "basis_items", "basis_references"}:
                return True
            if _contains_copied_material(nested):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_copied_material(item) for item in value)
    return False


def _output_path_is_forbidden(path: Path) -> bool:
    forbidden = {
        "spec",
        "tests",
        "reference",
        "presence",
        "relation",
        "identity",
        "field",
        "runtime",
        "api",
        "public-intake",
        "descendant",
        "receiver-capture",
    }
    return any(part.lower() in forbidden for part in path.resolve().parts)


def write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write one valid material-omitting result without silently overwriting."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error("WRITE_REFUSED: result must be a mapping")
    if result.get("resolver_module") != RESOLVER_MODULE or result.get("result_version") != RESULT_VERSION:
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error("WRITE_REFUSED: incompatible result metadata")
    if result.get("outcome") not in OUTCOME_FAMILY:
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error("WRITE_REFUSED: unsupported result outcome")
    if not _declared_non_claims_valid(result.get("non_claims")):
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error("WRITE_REFUSED: non-claims are not canonical false")
    if _contains_copied_material(result):
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error("WRITE_REFUSED: copied candidate or complete basis material")
    target = _as_path(output_path) if output_path is not None else OUTPUT_ROOT / OUTPUT_FILENAME
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error("WRITE_REFUSED: output path is forbidden")
    target = _next_available_output_path(target)
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as handle:
            json.dump(dict(result), handle, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False)
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
