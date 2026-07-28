"""Validate one bounded candidate evaluation-basis declaration without evaluation.

This module records declaration structure and readiness for later supply only. It
never reads candidate material, invokes the evaluation operation, or derives a
dimension or candidate result.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min"

DECLARATION_ID = "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_001"
DECLARATION_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION"
DECLARATION_VERSION = "0.1.0"
DECLARATION_SCOPE = (
    "DECLARE_BOUNDED_EVALUATION_BASIS_FOR_ONE_SELECTED_CANDIDATE_ACROSS_"
    "EIGHT_DIMENSIONS_ONLY"
)

SELECTED_EVALUATION_OPERATION_ID = "receiver_side_answerable_basis_candidate_evaluation_operation_001"
SELECTED_EVALUATION_OPERATION_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION"
SELECTED_EVALUATION_OPERATION_WAITING_RESULT_REQUIRED = "REQUIRES_EVALUATION_BASIS"
SELECTED_EVALUATION_OPERATION_WAITING_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_REQUIRES_EVALUATION_BASIS"
)

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
SELECTED_RECEPTION_OPERATION_ID = "receiver_side_answerable_basis_reception_operation_001"
SELECTED_EVALUATION_BOUNDARY_ID = "receiver_side_answerable_basis_candidate_evaluation_boundary_001"
ADMISSIBLE_FUTURE_ROUTE = "EVALUATION_BASIS_DECLARATION_THEN_EXISTING_CANDIDATE_EVALUATION_OPERATION_INVOCATION_ONLY"

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

OUTCOME_RECORDED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION_RECORDED"
OUTCOME_REQUIRES_DECLARATION_MATERIAL = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION_"
    "REQUIRES_DECLARATION_MATERIAL"
)
OUTCOME_BLOCKED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION_BLOCKED"
OUTCOME_NOT_RECORDED = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_REQUIRES_DECLARATION_MATERIAL,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

DECLARATION_RESULT_READY_FOR_SUPPLY = "EVALUATION_BASIS_DECLARATION_READY_FOR_SUPPLY"
DECLARATION_RESULT_REQUIRES_DECLARATION_MATERIAL = "REQUIRES_DECLARATION_MATERIAL"
DECLARATION_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
DECLARATION_RESULT_FAMILY = (
    DECLARATION_RESULT_READY_FOR_SUPPLY,
    DECLARATION_RESULT_REQUIRES_DECLARATION_MATERIAL,
    DECLARATION_RESULT_NOT_EVALUATED,
)

INTENT_RECORD = "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION"
INTENT_BLOCK = "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_DECLARATION_SPEC_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BASIS_DECLARATION_V0_MIN_SPEC.md"
)
WAITING_OPERATION_TERMINAL_SUMMARY_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
WAITING_OPERATION_RESULT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2/"
    "receiver_side_answerable_basis_candidate_evaluation_operation_001__"
    "receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result.json"
)
OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_001__"
    "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_result.json"
)

MAX_SERIALIZED_DECLARATION_SIZE = 131_072
MAX_BASIS_ITEMS_PER_DIMENSION = 32
MAX_BASIS_REFERENCES_PER_DIMENSION = 32
MAX_SERIALIZED_DIMENSION_RECORD_SIZE = 16_384
MAX_DECLARATION_STATEMENT_SIZE = 8_192
MAX_DECLARATION_NON_MEANING_SIZE = 8_192
MAX_ORIGIN_REFERENCE_LENGTH = 1_024
MAX_PREPARER_REFERENCE_LENGTH = 1_024
MAX_PREPARER_ROLE_LENGTH = 512
MAX_PREPARATION_TIMESTAMP_LENGTH = 256
MAX_EVALUATOR_REFERENCE_LENGTH = 1_024


class ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinError(Exception):
    """Raised when a declaration result cannot be written lawfully."""


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

DECLARATION_REQUIRED_FALSE_NON_CLAIMS = (
    "dimension_result_preclaimed",
    "aggregate_result_preclaimed",
    "candidate_sufficiency_preclaimed",
    "candidate_insufficiency_preclaimed",
    "candidate_indeterminacy_preclaimed",
    "receiver_attestation_preclaimed",
    "receiver_answerable_receipt_preclaimed",
    "custody_distinctness_preclaimed",
    "refusability_result_preclaimed",
    "could_have_been_withheld_result_preclaimed",
    "presence_support_preclaimed",
    "presence_authorization_preclaimed",
    "presence_establishment_preclaimed",
    "presence_recording_preclaimed",
    "evaluator_authority_preclaimed",
    "evaluator_identity_preclaimed",
    "evaluator_standing_preclaimed",
    "evaluator_truth_preclaimed",
    "basis_items_are_established_truth",
    "basis_references_are_verified_provenance",
    "source_body_interpretation_is_independent_evidence",
    "repository_access_is_evaluation_basis",
    "candidate_material_is_complete_evaluation_basis",
    "declaration_ready_means_operation_admitted",
    "declaration_supply_means_operation_admitted",
    "partial_declaration_ready_for_supply",
    "repeated_supply_permission_created",
    "reusable_basis_route_created",
    "second_candidate_basis_created",
    "candidate_evaluation_authorized",
    "candidate_evaluation_completed",
    "candidate_sufficiency_boundary_created",
    "receiver_attestation_boundary_created",
    "receiver_answerable_receipt_boundary_created",
    "presence_re_evaluation_boundary_created",
    "follow_on_authorized",
    "follow_on_work_authorized",
)

REQUIRED_FALSE_NON_CLAIMS = tuple(
    dict.fromkeys(
        (
            "evaluation_basis_declaration_separately_supplied",
            "evaluation_basis_declaration_resolver_generated",
            "evaluation_basis_declaration_candidate_material_reused_as_basis",
            "evaluation_basis_declaration_repository_access_treated_as_basis",
            "evaluation_basis_declaration_admitted_by_operation",
            *DECLARATION_REQUIRED_FALSE_NON_CLAIMS,
            "receiver_attestation_created",
            "receiver_attestation_supported",
            "receiver_answerable_receipt_present",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "second_candidate_received",
            "second_candidate_evaluated",
            "same_candidate_re_evaluation_authorized",
            "dimension_completion_route_created",
            "partial_dimension_evaluation_recorded",
            "caller_supplied_dimension_result_accepted",
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
            "operation_invoked",
            "dimension_result_derived",
            "candidate_sufficiency_created",
            "candidate_insufficiency_created",
            "candidate_indeterminacy_created",
            "evaluator_identity_established",
            "evaluator_authority_established",
            "evaluator_standing_created",
            "evaluator_truth_created",
            "repeated_supply_permission_created",
            "reusable_basis_route_created",
            "second_candidate_basis_created",
            "candidate_evaluation_authorized",
            "candidate_evaluation_completed",
            "candidate_sufficiency_boundary_created",
            "receiver_attestation_boundary_created",
            "receiver_answerable_receipt_boundary_created",
            "presence_re_evaluation_boundary_created",
            "follow_on_authorized",
            "follow_on_work_authorized",
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
    )
)

PROHIBITED_REQUEST_FLAGS = {
    "request_operation_admission": "PROHIBITED_OPERATION_ADMISSION_OR_INVOCATION_REQUESTED",
    "request_operation_invocation": "PROHIBITED_OPERATION_ADMISSION_OR_INVOCATION_REQUESTED",
    "request_candidate_evaluation": "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED",
    "request_dimension_result_derivation": "PROHIBITED_CANDIDATE_RESULT_REQUESTED",
    "request_candidate_sufficiency": "PROHIBITED_CANDIDATE_RESULT_REQUESTED",
    "request_candidate_insufficiency": "PROHIBITED_CANDIDATE_RESULT_REQUESTED",
    "request_candidate_indeterminacy": "PROHIBITED_CANDIDATE_RESULT_REQUESTED",
    "request_receiver_attestation_creation": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "request_receiver_attestation_support": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
    "request_receiver_answerable_receipt_creation": "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
    "request_presence_support": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_authorization": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_establishment": "PROHIBITED_PRESENCE_REQUESTED",
    "request_presence_recording": "PROHIBITED_PRESENCE_REQUESTED",
    "request_evaluator_identity_establishment": "PROHIBITED_EVALUATOR_IDENTITY_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_evaluator_authority_establishment": "PROHIBITED_EVALUATOR_IDENTITY_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_evaluator_standing_creation": "PROHIBITED_EVALUATOR_IDENTITY_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_evaluator_truth_creation": "PROHIBITED_EVALUATOR_IDENTITY_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
    "request_repeated_supply_permission_creation": "PROHIBITED_REPEATED_REUSABLE_OR_SECOND_CANDIDATE_BASIS_REQUESTED",
    "request_reusable_basis_route_creation": "PROHIBITED_REPEATED_REUSABLE_OR_SECOND_CANDIDATE_BASIS_REQUESTED",
    "request_second_candidate_basis_creation": "PROHIBITED_REPEATED_REUSABLE_OR_SECOND_CANDIDATE_BASIS_REQUESTED",
    "request_candidate_sufficiency_boundary_creation": "PROHIBITED_DOWNSTREAM_BOUNDARY_REQUESTED",
    "request_receiver_attestation_boundary_creation": "PROHIBITED_DOWNSTREAM_BOUNDARY_REQUESTED",
    "request_receiver_answerable_receipt_boundary_creation": "PROHIBITED_DOWNSTREAM_BOUNDARY_REQUESTED",
    "request_presence_re_evaluation_boundary_creation": "PROHIBITED_DOWNSTREAM_BOUNDARY_REQUESTED",
    "request_identity_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_relation_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_coupling_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_OR_AUTHORITY_REQUESTED",
    "request_public_intake_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_OR_AUTHORITY_REQUESTED",
    "request_output_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_action_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_follow_on_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_follow_on_work_authorization": "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
}

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "UNSUPPORTED_INTENT",
        "DECLARATION_SPEC_REFERENCE_MISSING",
        "DECLARATION_SPEC_MARKER_MISSING",
        "WAITING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "WAITING_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        "WAITING_OPERATION_RESULT_REFERENCE_MISSING",
        "WAITING_OPERATION_RESULT_NOT_PARSEABLE",
        "WAITING_OPERATION_RESULT_NOT_MAPPING",
        "REQUEST_VALUE_MISMATCH",
        "DECLARATION_MATERIAL_NOT_MAPPING",
        "DECLARATION_MATERIAL_OVERSIZED",
        "DECLARATION_TOP_LEVEL_FIELD_UNKNOWN",
        "DECLARATION_REQUIRED_FIELD_MISSING",
        "DECLARATION_FIELD_MALFORMED",
        "DECLARATION_SELECTED_IDENTITY_MISMATCH",
        "DECLARATION_NON_CLAIM_MISSING_OR_FLIPPED",
        "DIMENSION_RECORD_MISSING",
        "DIMENSION_RECORD_UNKNOWN",
        "DIMENSION_RECORD_MALFORMED",
        "DIMENSION_RECORD_OVERSIZED",
        "DIMENSION_RECORD_SELECTED_IDENTITY_MISMATCH",
        "DIMENSION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
        "DECLARATION_RESULT_PRECLAIMED",
        "DIMENSION_RESULT_PRECLAIMED",
        "AGGREGATE_RESULT_PRECLAIMED",
        "PROHIBITED_OPERATION_ADMISSION_OR_INVOCATION_REQUESTED",
        "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED",
        "PROHIBITED_CANDIDATE_RESULT_REQUESTED",
        "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
        "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
        "PROHIBITED_PRESENCE_REQUESTED",
        "PROHIBITED_EVALUATOR_IDENTITY_AUTHORITY_STANDING_OR_TRUTH_REQUESTED",
        "PROHIBITED_REPEATED_REUSABLE_OR_SECOND_CANDIDATE_BASIS_REQUESTED",
        "PROHIBITED_DOWNSTREAM_BOUNDARY_REQUESTED",
        "PROHIBITED_IDENTITY_RELATION_COUPLING_OR_FIELD_REQUESTED",
        "PROHIBITED_RUNTIME_API_PUBLIC_INTAKE_OR_AUTHORITY_REQUESTED",
        "PROHIBITED_OUTPUT_ACTION_SYNCHRONIZATION_OR_FOLLOW_ON_REQUESTED",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "EXPLICIT_BLOCK_REQUESTED",
        "WRITE_REFUSED",
    }
)

DECLARATION_SPEC_MARKER_CLASSES = {
    "title": ("# Receiver-Side Answerable Basis Candidate Evaluation Basis Declaration V0 Minimum Specification",),
    "identity": (DECLARATION_ID, DECLARATION_TYPE, DECLARATION_SCOPE),
    "eight_dimensions": ("Eight-Dimension Declaration", *EVALUATION_DIMENSION_IDS),
    "non_claims": ("Required Non-Claims", "declaration_ready_means_operation_admitted = false"),
}
WAITING_SUMMARY_MARKER_CLASSES = {
    "title": ("# Receiver-Side Answerable Basis Candidate Evaluation Operation Terminal Summary V0",),
    "waiting": (SELECTED_EVALUATION_OPERATION_WAITING_OUTCOME_REQUIRED, "operation_result = REQUIRES_EVALUATION_BASIS"),
    "not_evaluated": ("all eight dimensions", "NOT_EVALUATED"),
}

DIMENSION_RULES = {
    "candidate_structural_correspondence": {
        "support": (
            "candidate_identity_corresponds",
            "reception_operation_corresponds",
            "evaluation_boundary_corresponds",
            "prior_knock_reference_present",
        ),
        "contradiction": (
            "selected_candidate_record_mismatch",
            "selected_reception_operation_mismatch",
            "selected_evaluation_boundary_mismatch",
        ),
        "unresolved": ("prior_knock_reference_unresolved",),
    },
    "declared_provenance_posture": {
        "support": (
            "declared_provenance_reference_present",
            "declared_custody_reference_present",
            "references_internally_addressable",
            "references_structurally_correspond",
        ),
        "contradiction": (
            "declared_provenance_reference_mismatch",
            "declared_custody_reference_mismatch",
            "references_not_addressable",
            "references_not_structurally_correspond",
        ),
        "unresolved": ("provenance_posture_unresolved",),
    },
    "receiver_authorship_posture": {
        "support": (
            "bounded_receiver_authorship_declaration_present",
            "declaration_structurally_attributable_to_selected_packet",
        ),
        "contradiction": (
            "receiver_authorship_declaration_mismatch",
            "declaration_not_structurally_attributable",
        ),
        "unresolved": ("receiver_authorship_posture_unresolved",),
    },
    "separate_custody_posture": {
        "support": (
            "distinct_receiver_controlled_custody_at_occurrence_supported",
            "distinct_receiver_controlled_custody_at_preservation_supported",
            "support_independent_of_filename_directory_working_path_or_declaration_alone",
        ),
        "contradiction": (
            "same_custody_at_occurrence_established",
            "same_custody_at_preservation_established",
            "support_depends_on_filename_directory_working_path_or_declaration_alone",
        ),
        "unresolved": ("separate_custody_posture_unresolved",),
    },
    "refusability_posture": {
        "support": (
            "submission_could_have_been_refused_before_source_body_reception",
            "support_independent_of_declaration_alone",
        ),
        "contradiction": (
            "submission_could_not_have_been_refused_before_source_body_reception",
            "support_depends_on_declaration_alone",
        ),
        "unresolved": ("refusability_posture_unresolved",),
    },
    "could_have_been_withheld_posture": {
        "support": (
            "trace_could_have_remained_outside_source_body_custody",
            "support_distinguished_from_separate_custody",
            "support_distinguished_from_refusability",
        ),
        "contradiction": (
            "trace_could_not_have_remained_outside_source_body_custody",
            "support_not_distinguished_from_separate_custody",
            "support_not_distinguished_from_refusability",
        ),
        "unresolved": ("withholding_posture_unresolved",),
    },
    "prior_knock_correspondence_posture": {
        "support": (
            "exactly_one_selected_prior_knock_reference_present",
            "candidate_trace_structurally_corresponds_to_selected_prior_knock_reference",
            "no_alternate_knock_reference_selected",
        ),
        "contradiction": (
            "multiple_or_no_prior_knock_references_selected",
            "candidate_trace_does_not_correspond_to_selected_prior_knock_reference",
            "alternate_knock_reference_selected",
        ),
        "unresolved": ("prior_knock_correspondence_unresolved",),
    },
    "capture_record_posture": {
        "support": (
            "bounded_capture_record_present",
            "required_hash_record_present",
            "timestamp_record_present",
            "physical_signal_record_present",
            "records_internally_consistent",
            "records_addressable",
        ),
        "contradiction": (
            "bounded_capture_record_absent",
            "required_hash_record_absent",
            "timestamp_record_absent",
            "physical_signal_record_absent",
            "records_internally_inconsistent",
            "records_not_addressable",
        ),
        "unresolved": ("capture_record_posture_unresolved",),
    },
}

ALLOWED_DIMENSION_RECORD_KEYS = frozenset(
    {
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
    }
)
ALLOWED_DECLARATION_MATERIAL_KEYS = frozenset(
    {
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_id",
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_type",
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_version",
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_scope",
        "receiver_side_answerable_basis_candidate_id",
        "receiver_side_answerable_basis_candidate_type",
        "receiver_side_answerable_basis_candidate_scope",
        "selected_candidate_reception_operation_id",
        "selected_candidate_evaluation_boundary_id",
        "selected_candidate_evaluation_operation_id",
        "selected_candidate_evaluation_operation_type",
        "selected_candidate_evaluation_operation_waiting_result_required",
        "selected_candidate_evaluation_operation_waiting_outcome_required",
        "declaration_origin_reference",
        "preparer_reference",
        "preparer_role_declaration",
        "source_body_authored",
        "preparation_timestamp",
        "dimension_basis_records",
        "declaration_non_claims",
        "declaration_statement",
        "declaration_non_meaning",
    }
)
REQUIRED_DECLARATION_MATERIAL_KEYS = ALLOWED_DECLARATION_MATERIAL_KEYS

RESULT_PRECLAIM_FIELDS = frozenset(
    {
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_recorded",
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_result_recorded",
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_result",
        "declaration_material_received",
        "declaration_material_recorded",
        "evaluation_basis_declaration_complete",
        "evaluation_basis_declaration_ready_for_supply",
        "evaluation_basis_declaration_separately_prepared",
        "evaluation_basis_declaration_separately_supplied",
        "evaluation_basis_declaration_admitted_by_operation",
        "all_eight_dimension_records_present",
        "all_dimension_records_structurally_bounded",
        "all_dimension_records_reference_selected_candidate",
        "all_dimension_records_reference_selected_boundary",
        "all_dimension_records_reference_selected_operation",
        "all_dimension_records_non_result_preclaiming",
        "all_dimension_records_non_claims_false",
        "dimension_result",
        "dimension_results",
        "receiver_side_answerable_basis_candidate_evaluated",
    }
)
AGGREGATE_PRECLAIM_FIELDS = frozenset(
    {
        "receiver_side_answerable_basis_candidate_sufficient",
        "receiver_side_answerable_basis_candidate_insufficient",
        "receiver_side_answerable_basis_candidate_indeterminate",
        "candidate_sufficiency",
        "candidate_insufficiency",
        "candidate_indeterminacy",
        "aggregate_result",
    }
)

WHAT_REMAINS_OPEN = (
    "one separately prepared declaration",
    "declaration origin reference",
    "preparer reference",
    "preparer role declaration",
    "explicit source-body-authored posture",
    "eight populated dimension-basis records",
    "declaration readiness validation",
    "separate supply to the existing evaluation operation",
    "operation atomic admission",
    "candidate evaluation",
    "dimension results",
    "candidate-sufficiency boundary after completed evaluation",
    "later attestation, receipt, and presence questions only after lawful basis",
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


def _exact_bool(value: Any) -> bool:
    return value is True or value is False


def _mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


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


def _as_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _display_path(value: Path | str) -> str:
    path = _as_path(value)
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _read_text(value: Path | str) -> tuple[str | None, str | None]:
    try:
        path = _as_path(value)
        if not path.is_file():
            return None, "not_a_file"
        return path.read_text(encoding="utf-8"), None
    except (OSError, UnicodeDecodeError):
        return None, "unreadable"


def _read_json(value: Path | str) -> tuple[Any | None, str | None]:
    text, error = _read_text(value)
    if error is not None or text is None:
        return None, error
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        return None, "not_parseable"


def _check(name: str, passed: bool, code: str | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {"name": name, "passed": passed}
    if not passed and code is not None:
        item["block_code"] = code
        item["failure_code"] = code
    return item


def _failure(checks: list[dict[str, Any]], name: str, code: str) -> None:
    checks.append(_check(name, False, code))


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_declaration_non_claims() -> dict[str, bool]:
    return {key: False for key in DECLARATION_REQUIRED_FALSE_NON_CLAIMS}


def _canonical_dimension_non_claims() -> dict[str, bool]:
    return {key: False for key in DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS}


def _all_false_mapping(value: Any, required: Sequence[str]) -> bool:
    return isinstance(value, Mapping) and all(value.get(key) is False for key in required)


def _marker_status(text: str, marker_classes: Mapping[str, Sequence[str]]) -> dict[str, bool]:
    return {name: all(marker in text for marker in markers) for name, markers in marker_classes.items()}


def _expected_request_values() -> dict[str, str]:
    return {
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_id": DECLARATION_ID,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_type": DECLARATION_TYPE,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_version": DECLARATION_VERSION,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_scope": DECLARATION_SCOPE,
        "selected_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "selected_candidate_evaluation_operation_type": SELECTED_EVALUATION_OPERATION_TYPE,
        "selected_candidate_evaluation_operation_waiting_result_required": SELECTED_EVALUATION_OPERATION_WAITING_RESULT_REQUIRED,
        "selected_candidate_evaluation_operation_waiting_outcome_required": SELECTED_EVALUATION_OPERATION_WAITING_OUTCOME_REQUIRED,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
    }


def _request_allowed_keys() -> frozenset[str]:
    return frozenset(
        {
            "intent",
            "declaration_material_supplied",
            "declaration_material",
            "declared_non_claims",
            *tuple(_expected_request_values()),
            *tuple(PROHIBITED_REQUEST_FLAGS),
        }
    )


def _declaration_state(
    outcome: str,
    declaration_result: str,
    *,
    material_supplied: bool,
    material_received: bool = False,
    material_recorded: bool = False,
    complete: bool = False,
    source_body_authored: bool = False,
) -> dict[str, Any]:
    recorded = outcome in (OUTCOME_RECORDED, OUTCOME_REQUIRES_DECLARATION_MATERIAL)
    ready = outcome == OUTCOME_RECORDED
    state: dict[str, Any] = {
        "declaration_id": DECLARATION_ID,
        "declaration_type": DECLARATION_TYPE,
        "declaration_version": DECLARATION_VERSION,
        "declaration_scope": DECLARATION_SCOPE,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_id": DECLARATION_ID,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_type": DECLARATION_TYPE,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_version": DECLARATION_VERSION,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_scope": DECLARATION_SCOPE,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_recorded": recorded,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_result_recorded": recorded,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_result": declaration_result,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "declaration_material_supplied": material_supplied,
        "declaration_material_received": material_received,
        "declaration_material_recorded": material_recorded,
        "evaluation_basis_declaration_complete": complete,
        "all_eight_dimension_records_present": complete,
        "all_dimension_records_structurally_bounded": complete,
        "all_dimension_records_reference_selected_candidate": complete,
        "all_dimension_records_reference_selected_boundary": complete,
        "all_dimension_records_reference_selected_operation": complete,
        "all_dimension_records_non_result_preclaiming": complete,
        "all_dimension_records_non_claims_false": complete,
        "evaluation_basis_declaration_ready_for_supply": ready,
        "evaluation_basis_declaration_separately_prepared": ready,
        "evaluation_basis_declaration_separately_supplied": False,
        "evaluation_basis_declaration_origin_reference_supplied": ready,
        "evaluation_basis_declaration_preparer_reference_supplied": ready,
        "evaluation_basis_declaration_preparer_role_declared": ready,
        "evaluation_basis_declaration_source_body_authored": source_body_authored if ready else False,
        "evaluation_basis_declaration_resolver_generated": False,
        "evaluation_basis_declaration_candidate_material_reused_as_basis": False,
        "evaluation_basis_declaration_repository_access_treated_as_basis": False,
        "evaluation_basis_declaration_admitted_by_operation": False,
        "dimension_record_count": len(EVALUATION_DIMENSION_IDS) if complete else 0,
    }
    state.update(_canonical_non_claims())
    return state


def _material_metadata(material: Mapping[str, Any] | None, complete: bool) -> dict[str, Any]:
    if not isinstance(material, Mapping):
        return {
            "declaration_material_present": False,
            "dimension_record_count": 0,
            "dimension_record_ids": [],
            "dimension_record_metadata": {},
            "declaration_non_claims_validated": False,
            "complete_declaration_material_omitted_from_result": True,
            "complete_basis_items_omitted_from_result": True,
            "complete_basis_references_omitted_from_result": True,
            "candidate_material_omitted_from_result": True,
        }
    records = material.get("dimension_basis_records")
    record_metadata: dict[str, Any] = {}
    if isinstance(records, Mapping):
        for dimension_id in EVALUATION_DIMENSION_IDS:
            record = records.get(dimension_id)
            if not isinstance(record, Mapping):
                continue
            support = record.get("explicit_support_postures")
            contradiction = record.get("explicit_contradiction_postures")
            unresolved = record.get("unresolved_postures")
            items = record.get("basis_items")
            references = record.get("basis_references")
            record_metadata[dimension_id] = {
                "dimension_id": record.get("dimension_id"),
                "basis_item_count": len(items) if isinstance(items, list) else None,
                "basis_reference_count": len(references) if isinstance(references, list) else None,
                "evaluator_reference_supplied": isinstance(record.get("evaluator_reference"), str)
                and bool(record.get("evaluator_reference").strip()),
                "support_posture_key_names": sorted(support) if isinstance(support, Mapping) else [],
                "contradiction_posture_key_names": sorted(contradiction) if isinstance(contradiction, Mapping) else [],
                "unresolved_posture_key_names": sorted(unresolved) if isinstance(unresolved, Mapping) else [],
                "basis_non_claims_validated": _all_false_mapping(
                    record.get("basis_non_claims"), DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS
                ),
            }
    return {
        "declaration_material_present": True,
        "declaration_identifiers": {
            key: material.get(key)
            for key in (
                "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_id",
                "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_type",
                "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_version",
                "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_scope",
            )
        },
        "selected_identifiers": {
            key: material.get(key)
            for key in (
                "receiver_side_answerable_basis_candidate_id",
                "receiver_side_answerable_basis_candidate_type",
                "receiver_side_answerable_basis_candidate_scope",
                "selected_candidate_reception_operation_id",
                "selected_candidate_evaluation_boundary_id",
                "selected_candidate_evaluation_operation_id",
            )
        },
        "declaration_origin_reference_supplied": isinstance(material.get("declaration_origin_reference"), str)
        and bool(material.get("declaration_origin_reference").strip()),
        "preparer_reference_supplied": isinstance(material.get("preparer_reference"), str)
        and bool(material.get("preparer_reference").strip()),
        "preparer_role_declared": isinstance(material.get("preparer_role_declaration"), str)
        and bool(material.get("preparer_role_declaration").strip()),
        "source_body_authored_declared_value": material.get("source_body_authored")
        if _exact_bool(material.get("source_body_authored"))
        else None,
        "preparation_timestamp_supplied": isinstance(material.get("preparation_timestamp"), str)
        and bool(material.get("preparation_timestamp").strip()),
        "dimension_record_count": len(records) if isinstance(records, Mapping) else None,
        "dimension_record_ids": sorted(records) if isinstance(records, Mapping) else [],
        "dimension_record_metadata": record_metadata,
        "declaration_non_claims_validated": _all_false_mapping(
            material.get("declaration_non_claims"), DECLARATION_REQUIRED_FALSE_NON_CLAIMS
        ),
        "complete_declaration_validated": complete,
        "complete_declaration_material_omitted_from_result": True,
        "complete_basis_items_omitted_from_result": True,
        "complete_basis_references_omitted_from_result": True,
        "candidate_material_omitted_from_result": True,
    }


def _result(
    request: Mapping[str, Any],
    outcome: str,
    declaration_result: str,
    checks: list[dict[str, Any]],
    *,
    upstream: Mapping[str, Any] | None = None,
    material: Mapping[str, Any] | None = None,
    complete: bool = False,
    missing: Sequence[str] = (),
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    supplied = request.get("declaration_material_supplied") is True
    received = outcome == OUTCOME_RECORDED and complete
    state = _declaration_state(
        outcome,
        declaration_result,
        material_supplied=supplied,
        material_received=received,
        material_recorded=received,
        complete=complete,
        source_body_authored=material.get("source_body_authored") is True if isinstance(material, Mapping) else False,
    )
    declared = {
        key: copy.deepcopy(request[key])
        for key in ("intent", "declaration_material_supplied", *tuple(_expected_request_values()))
        if key in request
    }
    declared["complete_declaration_material_omitted_from_result"] = True
    result: dict[str, Any] = {
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_metadata": {
            "declaration_id": DECLARATION_ID,
            "declaration_type": DECLARATION_TYPE,
            "declaration_version": DECLARATION_VERSION,
            "declaration_scope": DECLARATION_SCOPE,
        },
        "declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_basis": declared,
        "upstream_basis": copy.deepcopy(dict(upstream or {})),
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration": state,
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_material": _material_metadata(
            material, complete
        ),
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_checks": copy.deepcopy(checks),
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_statement": {
            "declaration_structure_only": outcome in (OUTCOME_RECORDED, OUTCOME_REQUIRES_DECLARATION_MATERIAL),
            "complete_declaration_material_omitted_from_result": True,
            "basis_items_and_references_omitted_from_result": True,
            "candidate_material_omitted_from_result": True,
            "operation_not_invoked": True,
            "no_dimension_result_derived": True,
            "result_level_non_claims_canonical_false": True,
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
            "open_does_not_mean_next_unless_separately_selected": True,
        },
        "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_non_meaning": {
            "declaration_is_not_operation_admission": True,
            "declaration_supply_is_not_resolver_acceptance": True,
            "support_contradiction_and_unresolved_postures_are_not_results": True,
            "evaluator_reference_is_not_authority_identity_standing_or_truth": True,
            "declaration_is_not_candidate_evaluation_or_sufficiency": True,
            "declaration_is_not_attestation_receipt_or_presence": True,
        },
        "declaration_result_detail": {
            "declaration_result": declaration_result,
            "declaration_material_supplied": supplied,
            "declaration_material_received": received,
            "declaration_material_recorded": received,
            "declaration_complete": complete,
            "ready_for_supply": outcome == OUTCOME_RECORDED,
            "separately_supplied_to_evaluation_operation": False,
            "admitted_by_operation": False,
            "dimension_result_exists": False,
            "operation_invocation_exists": False,
        },
        "permitted_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "blocked_routes": [
            "operation admission or invocation",
            "dimension or candidate result derivation",
            "candidate sufficiency, attestation, receipt, and presence conversion",
            "repeated or reusable basis route",
            "repository scan, repair, discovery, or validation enforcement",
        ],
        "missing_or_incomplete_declaration_material": list(missing),
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
    }
    result["failed_check_count"] = sum(check.get("passed") is False for check in checks)
    result["passed_check_count"] = sum(check.get("passed") is True for check in checks)
    result["receiver_side_answerable_basis_candidate_evaluation_basis_declaration_summary"] = (
        _summary_from_result(result)
    )
    return result


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    declaration = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_declaration")
    material = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_declaration_material")
    upstream = result.get("upstream_basis")
    declaration = declaration if isinstance(declaration, Mapping) else {}
    material = material if isinstance(material, Mapping) else {}
    upstream = upstream if isinstance(upstream, Mapping) else {}
    return {
        "outcome": result.get("outcome"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "result_version": result.get("result_version"),
        "resolver_module": result.get("resolver_module"),
        "declaration_id": declaration.get("declaration_id"),
        "declaration_type": declaration.get("declaration_type"),
        "declaration_version": declaration.get("declaration_version"),
        "declaration_scope": declaration.get("declaration_scope"),
        "declaration_result": declaration.get(
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_result"
        ),
        "selected_identities": copy.deepcopy(material.get("selected_identifiers", {})),
        "declaration_material_postures": {
            key: declaration.get(key)
            for key in (
                "declaration_material_supplied",
                "declaration_material_received",
                "declaration_material_recorded",
                "evaluation_basis_declaration_origin_reference_supplied",
                "evaluation_basis_declaration_preparer_reference_supplied",
                "evaluation_basis_declaration_preparer_role_declared",
                "evaluation_basis_declaration_source_body_authored",
                "evaluation_basis_declaration_complete",
                "evaluation_basis_declaration_ready_for_supply",
                "evaluation_basis_declaration_separately_supplied",
                "evaluation_basis_declaration_admitted_by_operation",
            )
        },
        "dimension_record_count": material.get("dimension_record_count"),
        "dimension_record_ids": copy.deepcopy(material.get("dimension_record_ids", [])),
        "bounded_dimension_metadata": copy.deepcopy(material.get("dimension_record_metadata", {})),
        "missing_or_incomplete_declaration_material": copy.deepcopy(
            result.get("missing_or_incomplete_declaration_material", [])
        ),
        "governing_paths": copy.deepcopy(upstream.get("governing_paths", {})),
        "marker_validation": copy.deepcopy(upstream.get("marker_validation", {})),
        "non_claims_canonical_false": all(value is False for value in result.get("non_claims", {}).values())
        if isinstance(result.get("non_claims"), Mapping)
        else False,
    }


def _validate_request(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> tuple[str | None, str | None]:
    for key in RESULT_PRECLAIM_FIELDS | AGGREGATE_PRECLAIM_FIELDS | set(REQUIRED_FALSE_NON_CLAIMS):
        if key in request:
            code = "AGGREGATE_RESULT_PRECLAIMED" if key in AGGREGATE_PRECLAIM_FIELDS else "RESULT_POSTURE_PRECLAIMED"
            _failure(checks, f"request_{key}_not_preclaimed", code)
            return code, f"{key} is a result or downstream posture preclaim"
    unknown = set(request) - _request_allowed_keys()
    if unknown:
        _failure(checks, "request_has_only_supported_fields", "REQUEST_VALUE_MISMATCH")
        return "REQUEST_VALUE_MISMATCH", "request contains unsupported fields"
    intent = request.get("intent")
    if intent not in SUPPORTED_INTENTS:
        _failure(checks, "intent_supported", "UNSUPPORTED_INTENT")
        return "UNSUPPORTED_INTENT", "intent is unsupported"
    if intent == INTENT_BLOCK:
        _failure(checks, "intent_not_explicit_block", "EXPLICIT_BLOCK_REQUESTED")
        return "EXPLICIT_BLOCK_REQUESTED", "explicit block intent"
    for key, expected in _expected_request_values().items():
        if request.get(key) != expected:
            _failure(checks, f"request_{key}_matches", "REQUEST_VALUE_MISMATCH")
            return "REQUEST_VALUE_MISMATCH", f"{key} does not match the selected declaration line"
    if not _exact_bool(request.get("declaration_material_supplied")):
        _failure(checks, "declaration_material_supplied_is_boolean", "REQUEST_VALUE_MISMATCH")
        return "REQUEST_VALUE_MISMATCH", "declaration_material_supplied must be boolean"
    if not _all_false_mapping(request.get("declared_non_claims"), DECLARATION_REQUIRED_FALSE_NON_CLAIMS):
        _failure(checks, "declared_non_claims_are_canonical_false", "NON_CLAIM_MISSING_OR_FLIPPED")
        return "NON_CLAIM_MISSING_OR_FLIPPED", "declared non-claims are missing or flipped"
    for key, code in PROHIBITED_REQUEST_FLAGS.items():
        value = request.get(key)
        if value is True:
            _failure(checks, f"{key}_not_requested", code)
            return code, f"{key} is prohibited"
        if value is not False:
            _failure(checks, f"{key}_is_false", "REQUEST_VALUE_MISMATCH")
            return "REQUEST_VALUE_MISMATCH", f"{key} must be false"
    for key in RESULT_PRECLAIM_FIELDS | AGGREGATE_PRECLAIM_FIELDS:
        if key in request:
            code = "AGGREGATE_RESULT_PRECLAIMED" if key in AGGREGATE_PRECLAIM_FIELDS else "RESULT_POSTURE_PRECLAIMED"
            _failure(checks, f"request_{key}_not_preclaimed", code)
            return code, f"{key} is a result posture preclaim"
    material = request.get("declaration_material")
    if material is not None and request.get("declaration_material_supplied") is not True:
        _failure(checks, "material_matches_supplied_posture", "REQUEST_VALUE_MISMATCH")
        return "REQUEST_VALUE_MISMATCH", "material is present while supplied posture is false"
    checks.append(_check("request_is_bounded", True))
    return None, None


def _validate_upstream(checks: list[dict[str, Any]]) -> tuple[dict[str, Any], str | None, str | None]:
    upstream: dict[str, Any] = {
        "governing_paths": {
            "declaration_spec": _display_path(GOVERNING_DECLARATION_SPEC_RELATIVE_PATH),
            "waiting_operation_terminal_summary": _display_path(WAITING_OPERATION_TERMINAL_SUMMARY_RELATIVE_PATH),
            "waiting_operation_result": _display_path(WAITING_OPERATION_RESULT_RELATIVE_PATH),
        },
        "marker_validation": {},
    }
    spec_text, error = _read_text(GOVERNING_DECLARATION_SPEC_RELATIVE_PATH)
    if error is not None or spec_text is None:
        _failure(checks, "declaration_spec_reference_exists", "DECLARATION_SPEC_REFERENCE_MISSING")
        return upstream, "DECLARATION_SPEC_REFERENCE_MISSING", "governing declaration specification is unavailable"
    spec_markers = _marker_status(spec_text, DECLARATION_SPEC_MARKER_CLASSES)
    upstream["marker_validation"]["declaration_spec"] = spec_markers
    if not all(spec_markers.values()):
        _failure(checks, "declaration_spec_markers_present", "DECLARATION_SPEC_MARKER_MISSING")
        return upstream, "DECLARATION_SPEC_MARKER_MISSING", "governing declaration specification markers are incomplete"
    checks.append(_check("declaration_spec_markers_present", True))

    summary_text, error = _read_text(WAITING_OPERATION_TERMINAL_SUMMARY_RELATIVE_PATH)
    if error is not None or summary_text is None:
        _failure(checks, "waiting_summary_reference_exists", "WAITING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING")
        return upstream, "WAITING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "waiting operation summary is unavailable"
    summary_markers = _marker_status(summary_text, WAITING_SUMMARY_MARKER_CLASSES)
    upstream["marker_validation"]["waiting_operation_terminal_summary"] = summary_markers
    if not all(summary_markers.values()):
        _failure(checks, "waiting_summary_markers_present", "WAITING_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING")
        return upstream, "WAITING_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", "waiting operation summary markers are incomplete"
    checks.append(_check("waiting_summary_markers_present", True))

    artifact, error = _read_json(WAITING_OPERATION_RESULT_RELATIVE_PATH)
    if error in ("not_a_file", "unreadable"):
        _failure(checks, "waiting_operation_result_exists", "WAITING_OPERATION_RESULT_REFERENCE_MISSING")
        return upstream, "WAITING_OPERATION_RESULT_REFERENCE_MISSING", "waiting operation result is unavailable"
    if error is not None:
        _failure(checks, "waiting_operation_result_parseable", "WAITING_OPERATION_RESULT_NOT_PARSEABLE")
        return upstream, "WAITING_OPERATION_RESULT_NOT_PARSEABLE", "waiting operation result is not parseable"
    if not isinstance(artifact, Mapping):
        _failure(checks, "waiting_operation_result_mapping", "WAITING_OPERATION_RESULT_NOT_MAPPING")
        return upstream, "WAITING_OPERATION_RESULT_NOT_MAPPING", "waiting operation result is not a mapping"
    operation = artifact.get("receiver_side_answerable_basis_candidate_evaluation_operation")
    dimensions = artifact.get("receiver_side_answerable_basis_candidate_evaluation_operation_dimensions")
    if not isinstance(operation, Mapping) or not isinstance(dimensions, Mapping):
        _failure(checks, "waiting_operation_result_shape", "WAITING_OPERATION_RESULT_NOT_MAPPING")
        return upstream, "WAITING_OPERATION_RESULT_NOT_MAPPING", "waiting operation result shape is incomplete"
    required = {
        "outcome": SELECTED_EVALUATION_OPERATION_WAITING_OUTCOME_REQUIRED,
        "failed_check_count": 0,
    }
    for key, expected in required.items():
        if artifact.get(key) != expected:
            _failure(checks, f"waiting_operation_{key}_matches", "REQUEST_VALUE_MISMATCH")
            return upstream, "REQUEST_VALUE_MISMATCH", f"waiting operation {key} does not match"
    operation_required = {
        "receiver_side_answerable_basis_candidate_evaluation_operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "receiver_side_answerable_basis_candidate_evaluation_operation_type": SELECTED_EVALUATION_OPERATION_TYPE,
        "receiver_side_answerable_basis_candidate_evaluation_operation_result": SELECTED_EVALUATION_OPERATION_WAITING_RESULT_REQUIRED,
        "receiver_side_answerable_basis_candidate_evaluation_operation_recorded": True,
        "receiver_side_answerable_basis_candidate_evaluation_operation_result_recorded": True,
        "evaluation_basis_supplied": False,
        "evaluation_basis_complete": False,
        "receiver_side_answerable_basis_candidate_evaluated": False,
        "candidate_evaluation_operation_exhausted": False,
        "second_candidate_evaluated": False,
        "repeated_evaluation_permission_created": False,
        "reusable_route_created": False,
        "dimension_completion_route_created": False,
        "receiver_attestation_created": False,
        "receiver_answerable_receipt_present": False,
        "presence_supported": False,
        "follow_on_work_authorized": False,
    }
    for key, expected in operation_required.items():
        if operation.get(key) != expected:
            _failure(checks, f"waiting_operation_{key}_matches", "REQUEST_VALUE_MISMATCH")
            return upstream, "REQUEST_VALUE_MISMATCH", f"waiting operation {key} does not match"
    for dimension_id in EVALUATION_DIMENSION_IDS:
        dimension = dimensions.get(dimension_id)
        if not isinstance(dimension, Mapping) or dimension.get("dimension_result") != "NOT_EVALUATED":
            _failure(checks, f"waiting_dimension_{dimension_id}_not_evaluated", "REQUEST_VALUE_MISMATCH")
            return upstream, "REQUEST_VALUE_MISMATCH", "waiting operation dimensions are not all NOT_EVALUATED"
    artifact_upstream = artifact.get("upstream_basis")
    candidate_identity = artifact_upstream.get("selected_candidate_identity") if isinstance(artifact_upstream, Mapping) else None
    boundary_identity = artifact_upstream.get("selected_boundary_identity") if isinstance(artifact_upstream, Mapping) else None
    expected_candidate_identity = {
        "candidate_id": CANDIDATE_ID,
        "candidate_type": CANDIDATE_TYPE,
        "candidate_scope": CANDIDATE_SCOPE,
        "reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
    }
    if not isinstance(candidate_identity, Mapping) or any(
        candidate_identity.get(key) != expected for key, expected in expected_candidate_identity.items()
    ):
        _failure(checks, "waiting_operation_selected_candidate_identity_matches", "REQUEST_VALUE_MISMATCH")
        return upstream, "REQUEST_VALUE_MISMATCH", "waiting operation selected candidate identity does not match"
    if not isinstance(boundary_identity, Mapping) or boundary_identity.get("boundary_id") != SELECTED_EVALUATION_BOUNDARY_ID:
        _failure(checks, "waiting_operation_selected_boundary_identity_matches", "REQUEST_VALUE_MISMATCH")
        return upstream, "REQUEST_VALUE_MISMATCH", "waiting operation selected boundary identity does not match"
    upstream["waiting_operation_identity"] = {
        "operation_id": SELECTED_EVALUATION_OPERATION_ID,
        "operation_type": SELECTED_EVALUATION_OPERATION_TYPE,
        "waiting_outcome": SELECTED_EVALUATION_OPERATION_WAITING_OUTCOME_REQUIRED,
        "waiting_result": SELECTED_EVALUATION_OPERATION_WAITING_RESULT_REQUIRED,
        "candidate_id": CANDIDATE_ID,
        "candidate_type": CANDIDATE_TYPE,
        "candidate_scope": CANDIDATE_SCOPE,
        "reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
    }
    checks.append(_check("waiting_operation_upstream_posture_valid", True))
    return upstream, None, None


def _posture_mapping_valid(value: Any, expected_keys: Sequence[str]) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(expected_keys)
        and all(_exact_bool(item) for item in value.values())
    )


def _string_within(value: Any, maximum: int) -> bool:
    return isinstance(value, str) and bool(value.strip()) and len(value) <= maximum


def _material_preclaim_code(material: Mapping[str, Any]) -> str | None:
    for key in RESULT_PRECLAIM_FIELDS:
        if key in material:
            return "DECLARATION_RESULT_PRECLAIMED"
    for key in AGGREGATE_PRECLAIM_FIELDS:
        if key in material:
            return "AGGREGATE_RESULT_PRECLAIMED"
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key in material:
            return "RESULT_POSTURE_PRECLAIMED"
    operation_prohibited = {
        "operation_admitted",
        "evaluation_basis_declaration_admitted_by_operation",
        "operation_invoked",
        "request_operation_invocation",
    }
    if any(material.get(key) is True for key in operation_prohibited):
        return "PROHIBITED_OPERATION_ADMISSION_OR_INVOCATION_REQUESTED"
    candidate_prohibited = {
        "candidate_evaluation_authorized",
        "candidate_evaluation_completed",
        "request_candidate_evaluation",
    }
    if any(material.get(key) is True for key in candidate_prohibited):
        return "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED"
    return None


def _validate_dimension_record(
    dimension_id: str,
    record: Any,
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, bool]:
    if record is None:
        return None, None, False
    if not isinstance(record, Mapping):
        _failure(checks, f"dimension_{dimension_id}_is_mapping", "DIMENSION_RECORD_MALFORMED")
        return "DIMENSION_RECORD_MALFORMED", f"{dimension_id} is not a mapping", False
    size = _serialized_size(record)
    if size is None or size > MAX_SERIALIZED_DIMENSION_RECORD_SIZE:
        _failure(checks, f"dimension_{dimension_id}_within_size", "DIMENSION_RECORD_OVERSIZED")
        return "DIMENSION_RECORD_OVERSIZED", f"{dimension_id} exceeds bounded size", False
    for key in RESULT_PRECLAIM_FIELDS | AGGREGATE_PRECLAIM_FIELDS:
        if key in record:
            code = "AGGREGATE_RESULT_PRECLAIMED" if key in AGGREGATE_PRECLAIM_FIELDS else "DIMENSION_RESULT_PRECLAIMED"
            _failure(checks, f"dimension_{dimension_id}_{key}_not_preclaimed", code)
            return code, f"{dimension_id} contains a result preclaim", False
    unknown = set(record) - ALLOWED_DIMENSION_RECORD_KEYS
    if unknown:
        _failure(checks, f"dimension_{dimension_id}_has_no_unknown_keys", "DIMENSION_RECORD_UNKNOWN")
        return "DIMENSION_RECORD_UNKNOWN", f"{dimension_id} contains unknown fields", False
    missing = ALLOWED_DIMENSION_RECORD_KEYS - set(record)
    if missing:
        return None, None, False
    if record.get("dimension_id") != dimension_id:
        _failure(checks, f"dimension_{dimension_id}_id_matches", "DIMENSION_RECORD_SELECTED_IDENTITY_MISMATCH")
        return "DIMENSION_RECORD_SELECTED_IDENTITY_MISMATCH", f"{dimension_id} id does not match its key", False
    identifiers = {
        "selected_candidate_id": CANDIDATE_ID,
        "selected_candidate_reception_operation_id": SELECTED_RECEPTION_OPERATION_ID,
        "selected_candidate_evaluation_boundary_id": SELECTED_EVALUATION_BOUNDARY_ID,
    }
    if any(record.get(key) != expected for key, expected in identifiers.items()):
        _failure(checks, f"dimension_{dimension_id}_identities_match", "DIMENSION_RECORD_SELECTED_IDENTITY_MISMATCH")
        return "DIMENSION_RECORD_SELECTED_IDENTITY_MISMATCH", f"{dimension_id} selected identity does not match", False
    if record.get("basis_supplied") is not True:
        _failure(checks, f"dimension_{dimension_id}_basis_supplied", "DIMENSION_RECORD_MALFORMED")
        return "DIMENSION_RECORD_MALFORMED", f"{dimension_id} basis_supplied must be true", False
    for key, maximum in (("basis_items", MAX_BASIS_ITEMS_PER_DIMENSION), ("basis_references", MAX_BASIS_REFERENCES_PER_DIMENSION)):
        value = record.get(key)
        if not isinstance(value, list) or len(value) > maximum or not _json_compatible(value):
            _failure(checks, f"dimension_{dimension_id}_{key}_bounded", "DIMENSION_RECORD_MALFORMED")
            return "DIMENSION_RECORD_MALFORMED", f"{dimension_id} {key} is not bounded JSON-compatible list", False
    rule = DIMENSION_RULES[dimension_id]
    for key, expected in (
        ("explicit_support_postures", rule["support"]),
        ("explicit_contradiction_postures", rule["contradiction"]),
        ("unresolved_postures", rule["unresolved"]),
    ):
        if not _posture_mapping_valid(record.get(key), expected):
            _failure(checks, f"dimension_{dimension_id}_{key}_bounded", "DIMENSION_RECORD_MALFORMED")
            return "DIMENSION_RECORD_MALFORMED", f"{dimension_id} {key} is malformed", False
    if not _string_within(record.get("evaluator_reference"), MAX_EVALUATOR_REFERENCE_LENGTH):
        _failure(checks, f"dimension_{dimension_id}_evaluator_reference_bounded", "DIMENSION_RECORD_MALFORMED")
        return "DIMENSION_RECORD_MALFORMED", f"{dimension_id} evaluator reference is malformed", False
    if not _all_false_mapping(record.get("basis_non_claims"), DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS):
        _failure(checks, f"dimension_{dimension_id}_non_claims_false", "DIMENSION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED")
        return "DIMENSION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED", f"{dimension_id} basis non-claims are missing or flipped", False
    checks.append(_check(f"dimension_{dimension_id}_structurally_valid", True))
    return None, None, True


def _validate_material(
    material: Any,
    checks: list[dict[str, Any],],
) -> tuple[str | None, str | None, bool, list[str]]:
    missing: list[str] = []
    if material is None:
        return None, None, False, ["declaration_material"]
    if not isinstance(material, Mapping):
        _failure(checks, "declaration_material_is_mapping", "DECLARATION_MATERIAL_NOT_MAPPING")
        return "DECLARATION_MATERIAL_NOT_MAPPING", "declaration material is not a mapping", False, missing
    size = _serialized_size(material)
    if size is None or size > MAX_SERIALIZED_DECLARATION_SIZE:
        _failure(checks, "declaration_material_within_size", "DECLARATION_MATERIAL_OVERSIZED")
        return "DECLARATION_MATERIAL_OVERSIZED", "declaration material exceeds bounded size", False, missing
    preclaim = _material_preclaim_code(material)
    if preclaim is not None:
        _failure(checks, "declaration_material_has_no_preclaims", preclaim)
        return preclaim, "declaration material contains a prohibited result posture", False, missing
    unknown = set(material) - ALLOWED_DECLARATION_MATERIAL_KEYS
    if unknown:
        _failure(checks, "declaration_material_has_no_unknown_fields", "DECLARATION_TOP_LEVEL_FIELD_UNKNOWN")
        return "DECLARATION_TOP_LEVEL_FIELD_UNKNOWN", "declaration material contains unknown fields", False, missing
    absent = REQUIRED_DECLARATION_MATERIAL_KEYS - set(material)
    if absent:
        missing.extend(f"declaration_field:{key}" for key in sorted(absent))
        return None, None, False, missing
    expected = _expected_request_values()
    material_expected = {
        key: expected[key]
        for key in expected
        if key in material
    }
    if any(material.get(key) != value for key, value in material_expected.items()):
        _failure(checks, "declaration_selected_identities_match", "DECLARATION_SELECTED_IDENTITY_MISMATCH")
        return "DECLARATION_SELECTED_IDENTITY_MISMATCH", "declaration identities do not match the selected line", False, missing
    text_fields = (
        ("declaration_origin_reference", MAX_ORIGIN_REFERENCE_LENGTH),
        ("preparer_reference", MAX_PREPARER_REFERENCE_LENGTH),
        ("preparer_role_declaration", MAX_PREPARER_ROLE_LENGTH),
        ("preparation_timestamp", MAX_PREPARATION_TIMESTAMP_LENGTH),
    )
    for key, maximum in text_fields:
        if not _string_within(material.get(key), maximum):
            if material.get(key) is None or material.get(key) == "":
                missing.append(f"declaration_field:{key}")
                continue
            _failure(checks, f"{key}_bounded", "DECLARATION_FIELD_MALFORMED")
            return "DECLARATION_FIELD_MALFORMED", f"{key} is malformed", False, missing
    if missing:
        return None, None, False, missing
    if not _exact_bool(material.get("source_body_authored")):
        _failure(checks, "source_body_authored_is_boolean", "DECLARATION_FIELD_MALFORMED")
        return "DECLARATION_FIELD_MALFORMED", "source_body_authored must be boolean", False, missing
    for key, maximum in (
        ("declaration_statement", MAX_DECLARATION_STATEMENT_SIZE),
        ("declaration_non_meaning", MAX_DECLARATION_NON_MEANING_SIZE),
    ):
        value = material.get(key)
        size = _serialized_size(value)
        if not isinstance(value, Mapping) or size is None or size > maximum:
            _failure(checks, f"{key}_bounded_mapping", "DECLARATION_FIELD_MALFORMED")
            return "DECLARATION_FIELD_MALFORMED", f"{key} is malformed", False, missing
    if not _all_false_mapping(material.get("declaration_non_claims"), DECLARATION_REQUIRED_FALSE_NON_CLAIMS):
        _failure(checks, "declaration_non_claims_canonical_false", "DECLARATION_NON_CLAIM_MISSING_OR_FLIPPED")
        return "DECLARATION_NON_CLAIM_MISSING_OR_FLIPPED", "declaration non-claims are missing or flipped", False, missing
    records = material.get("dimension_basis_records")
    if not isinstance(records, Mapping):
        _failure(checks, "dimension_basis_records_mapping", "DECLARATION_FIELD_MALFORMED")
        return "DECLARATION_FIELD_MALFORMED", "dimension basis records are not a mapping", False, missing
    unknown_records = set(records) - set(EVALUATION_DIMENSION_IDS)
    if unknown_records:
        _failure(checks, "dimension_record_keys_known", "DIMENSION_RECORD_UNKNOWN")
        return "DIMENSION_RECORD_UNKNOWN", "dimension basis records include unknown dimensions", False, missing
    absent_records = set(EVALUATION_DIMENSION_IDS) - set(records)
    if absent_records:
        missing.extend(f"dimension_basis_record:{key}" for key in EVALUATION_DIMENSION_IDS if key in absent_records)
        return None, None, False, missing
    for dimension_id in EVALUATION_DIMENSION_IDS:
        code, reason, valid = _validate_dimension_record(dimension_id, records.get(dimension_id), checks)
        if code is not None:
            return code, reason, False, missing
        if not valid:
            missing.append(f"dimension_basis_record:{dimension_id}")
    if missing:
        return None, None, False, missing
    checks.append(_check("declaration_material_structurally_complete", True))
    return None, None, True, missing


def build_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_request(
    *,
    intent: str = INTENT_RECORD,
    declaration_material_supplied: bool | None = None,
    declaration_material: Mapping[str, Any] | None = None,
    declared_non_claims: Mapping[str, Any] | None = None,
    declaration_origin_reference: str | None = None,
    preparer_reference: str | None = None,
    preparer_role_declaration: str | None = None,
    source_body_authored: bool | None = None,
    preparation_timestamp: str | None = None,
    dimension_basis_records: Mapping[str, Any] | None = None,
    declaration_non_claims: Mapping[str, Any] | None = None,
    declaration_statement: Mapping[str, Any] | None = None,
    declaration_non_meaning: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a bounded request without fabricating declaration material."""
    direct_material_supplied = any(
        value is not None
        for value in (
            declaration_origin_reference,
            preparer_reference,
            preparer_role_declaration,
            source_body_authored,
            preparation_timestamp,
            dimension_basis_records,
            declaration_non_claims,
            declaration_statement,
            declaration_non_meaning,
        )
    )
    if declaration_material is None and direct_material_supplied:
        declaration_material = {
            **_expected_request_values(),
            "declaration_origin_reference": declaration_origin_reference,
            "preparer_reference": preparer_reference,
            "preparer_role_declaration": preparer_role_declaration,
            "source_body_authored": source_body_authored,
            "preparation_timestamp": preparation_timestamp,
            "dimension_basis_records": copy.deepcopy(dimension_basis_records),
            "declaration_non_claims": copy.deepcopy(
                declaration_non_claims
                if declaration_non_claims is not None
                else _canonical_declaration_non_claims()
            ),
            "declaration_statement": copy.deepcopy(declaration_statement if declaration_statement is not None else {}),
            "declaration_non_meaning": copy.deepcopy(
                declaration_non_meaning if declaration_non_meaning is not None else {}
            ),
        }
    supplied = declaration_material is not None if declaration_material_supplied is None else declaration_material_supplied
    request: dict[str, Any] = {
        "intent": intent,
        "declaration_material_supplied": supplied,
        "declaration_material": copy.deepcopy(declaration_material),
        "declared_non_claims": copy.deepcopy(
            declared_non_claims if declared_non_claims is not None else _canonical_declaration_non_claims()
        ),
        **_expected_request_values(),
        **{key: False for key in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_request(
    **kwargs: Any,
) -> dict[str, Any]:
    """Compatibility alias for the bounded declaration request builder."""
    return build_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_request(**kwargs)


def resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min(
    declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate one declaration structurally and record waiting or ready posture."""
    if declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration is None:
        request: Mapping[str, Any] = build_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_request()
    elif not isinstance(declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration, Mapping):
        checks = [_check("request_is_mapping", False, "REQUEST_NOT_MAPPING")]
        return _result(
            {}, OUTCOME_BLOCKED, DECLARATION_RESULT_NOT_EVALUATED, checks,
            code="REQUEST_NOT_MAPPING", reason="request is not a mapping"
        )
    else:
        request = copy.deepcopy(dict(declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration))

    checks: list[dict[str, Any]] = []
    code, reason = _validate_request(request, checks)
    if code is not None:
        return _result(request, OUTCOME_BLOCKED, DECLARATION_RESULT_NOT_EVALUATED, checks, code=code, reason=reason)
    if request.get("intent") == INTENT_DO_NOT_RECORD:
        checks.append(_check("do_not_record_intent_honored", True))
        return _result(request, OUTCOME_NOT_RECORDED, DECLARATION_RESULT_NOT_EVALUATED, checks)

    upstream, code, reason = _validate_upstream(checks)
    if code is not None:
        return _result(
            request, OUTCOME_BLOCKED, DECLARATION_RESULT_NOT_EVALUATED, checks,
            upstream=upstream, code=code, reason=reason
        )
    material = request.get("declaration_material")
    if request.get("declaration_material_supplied") is False:
        checks.append(_check("declaration_material_absent_waiting_posture", True))
        return _result(
            request, OUTCOME_REQUIRES_DECLARATION_MATERIAL,
            DECLARATION_RESULT_REQUIRES_DECLARATION_MATERIAL, checks, upstream=upstream,
            missing=["declaration_material"]
        )
    code, reason, complete, missing = _validate_material(material, checks)
    if code is not None:
        return _result(
            request, OUTCOME_BLOCKED, DECLARATION_RESULT_NOT_EVALUATED, checks,
            upstream=upstream, material=material if isinstance(material, Mapping) else None,
            missing=missing, code=code, reason=reason
        )
    if not complete:
        checks.append(_check("declaration_material_incomplete_waiting_posture", True))
        return _result(
            request, OUTCOME_REQUIRES_DECLARATION_MATERIAL,
            DECLARATION_RESULT_REQUIRES_DECLARATION_MATERIAL, checks, upstream=upstream,
            material=material if isinstance(material, Mapping) else None, missing=missing
        )
    checks.append(_check("declaration_ready_for_supply_without_operation_admission", True))
    return _result(
        request, OUTCOME_RECORDED, DECLARATION_RESULT_READY_FOR_SUPPLY, checks,
        upstream=upstream, material=material if isinstance(material, Mapping) else None, complete=True
    )


def resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_from_path(
    declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_path: Path | str,
) -> dict[str, Any]:
    """Resolve one JSON request path without filesystem discovery."""
    value, error = _read_json(declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_path)
    if error is not None or not isinstance(value, Mapping):
        checks = [_check("request_path_is_mapping_json", False, "REQUEST_NOT_MAPPING")]
        return _result(
            {}, OUTCOME_BLOCKED, DECLARATION_RESULT_NOT_EVALUATED, checks,
            code="REQUEST_NOT_MAPPING", reason="request path is missing, malformed, or not a mapping"
        )
    return resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min(value)


def build_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return bounded summary metadata without declaration content."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinError("result must be a mapping")
    return _summary_from_result(result)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    index = 1
    while True:
        candidate = path.with_name(f"{stem}_{index:03d}{suffix}")
        if not candidate.exists():
            return candidate
        index += 1


def _contains_forbidden_material(value: Any, *, parent_key: str | None = None) -> bool:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if key in {"basis_items", "basis_references", "candidate_material", "candidate_packet"}:
                return True
            if _contains_forbidden_material(nested, parent_key=str(key)):
                return True
    elif isinstance(value, list):
        return any(_contains_forbidden_material(item, parent_key=parent_key) for item in value)
    return False


def _output_path_is_forbidden(path: Path) -> bool:
    lowered = {part.lower() for part in path.parts}
    forbidden = {
        "spec", "tests", "reference", "presence", "relation", "identity", "field", "runtime", "api",
        "public-intake", "descendant", "receiver-capture", "candidate-reception",
    }
    return bool(lowered & forbidden)


def write_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None,
) -> Path:
    """Write a validated declaration result with deterministic suffixing."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinError("result must be a mapping")
    if result.get("resolver_module") != RESOLVER_MODULE or result.get("result_version") != RESULT_VERSION:
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinError("result identity does not match resolver")
    if result.get("outcome") not in OUTCOME_FAMILY:
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinError("result outcome is unsupported")
    if not _all_false_mapping(result.get("non_claims"), REQUIRED_FALSE_NON_CLAIMS):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinError("result non-claims are not canonical false")
    if _contains_forbidden_material(result):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinError("result contains copied declaration or candidate material")
    target = Path(output_path) if output_path is not None else OUTPUT_ROOT / OUTPUT_FILENAME
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinError("output path is forbidden")
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _next_available_output_path(target)
    try:
        target.write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n", encoding="utf-8")
    except OSError as error:
        raise ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinError("result write refused") from error
    return target
