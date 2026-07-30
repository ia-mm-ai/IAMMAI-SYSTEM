"""Resolve one bounded receiver-answerable-receipt operation.

The resolver admits one exact allowed receipt boundary together with the
exact recorded receiver-attestation result selected by that boundary.  The
pair is validated atomically before one recorded, not-recorded,
indeterminate, or blocked posture is returned.  No source body, presence
route, proof, authority, runtime, or follow-on permission is created.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from types import MappingProxyType
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_v0_min"
)

OPERATION_ID = (
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_001"
)
OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION"
)
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = (
    "RECORD_ONE_RECEIVER_ANSWERABLE_RECEIPT_FOR_ONE_RECORDED_"
    "RECEIVER_ATTESTATION_RESULT_ONLY"
)

UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ID = (
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_001"
)
UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY"
)
UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_VERSION = "0.1.0"
UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_SCOPE = (
    "CONSIDER_ONE_RECEIVER_ANSWERABLE_RECEIPT_FOR_ONE_RECORDED_"
    "RECEIVER_ATTESTATION_RESULT_ONLY"
)
UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ALLOWED"
)
UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_CONSIDERATION_ALLOWED"
)
UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_v0_min"
)
UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_DECISION_CODE = (
    "RECEIPT_CONSIDERATION_ALLOWED"
)
UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_DECISION_REASON = (
    "exact recorded receiver-attestation result admitted for "
    "receiver-answerable-receipt consideration only"
)
UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_FUTURE_ROUTE = (
    "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_THEN_SEPARATE_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OR_DECLARATION_ONLY"
)

SELECTED_RECEIVER_ATTESTATION_OPERATION_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_001"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION = "0.1.0"
SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE = (
    "ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_"
    "FOR_ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_RECORDED"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min"
)

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = (
    "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)

ADMISSIBLE_FUTURE_ROUTE = (
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_THEN_SEPARATE_"
    "PRESENCE_RE_EVALUATION_BOUNDARY_ONLY_IF_"
    "RECEIVER_ANSWERABLE_RECEIPT_RECORDED"
)
REQUIRED_FUTURE_ROUTE = ADMISSIBLE_FUTURE_ROUTE

OUTCOME_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_NOT_RECORDED"
)
OUTCOME_INDETERMINATE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_INDETERMINATE"
)
OUTCOME_BLOCKED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_INDETERMINATE,
    OUTCOME_BLOCKED,
)

RESULT_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_RECORDED"
)
RESULT_NOT_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_NOT_RECORDED"
)
RESULT_INDETERMINATE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_INDETERMINATE"
)
RESULT_NOT_EVALUATED = "NOT_EVALUATED"
COMPLETED_RESULT_FAMILY = (
    RESULT_RECORDED,
    RESULT_NOT_RECORDED,
    RESULT_INDETERMINATE,
)
COMPLETED_OPERATION_RESULT_FAMILY = COMPLETED_RESULT_FAMILY
RESULT_FAMILY = (*COMPLETED_RESULT_FAMILY, RESULT_NOT_EVALUATED)
OPERATION_RESULT_FAMILY = RESULT_FAMILY
OPERATION_RESULT_RECORDED = RESULT_RECORDED
OPERATION_RESULT_NOT_RECORDED = RESULT_NOT_RECORDED
OPERATION_RESULT_INDETERMINATE = RESULT_INDETERMINATE

INTENT_RECORD = (
    "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION"
)
INTENT_BLOCK = (
    "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_V0_MIN_SPEC.md"
)
UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_v0_min/"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_001__"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_v0_min_result.json"
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_attestation_operation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_001__"
    "receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min_result_001.json"
)
ORIGINAL_WAITING_RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_attestation_operation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_001__"
    "receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min_result.json"
)

GOVERNING_OPERATION_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH
)
UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_PATH = (
    REPO_ROOT
    / UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH
)
SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_PATH = (
    REPO_ROOT
    / SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
)
GOVERNING_SPEC_RELATIVE_PATH = GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPEC_PATH = GOVERNING_OPERATION_SPECIFICATION_PATH

OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_001__"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_operation_v0_min_result.json"
)

DECISION_INPUT_FIELDS = (
    "receiver_answerable_receipt_recording_selected",
    "receipt_recording_ambiguity_present",
    "receipt_recording_contradiction_present",
    "receipt_recording_unresolved",
)
CANONICAL_DECISION_INPUTS = MappingProxyType(
    {
        "receiver_answerable_receipt_recording_selected": True,
        "receipt_recording_ambiguity_present": False,
        "receipt_recording_contradiction_present": False,
        "receipt_recording_unresolved": False,
    }
)

REQUIRED_FALSE_NON_CLAIMS = (
    "receiver_answerable_receipt_created",
    "receiver_answerable_receipt_supported",
    "presence_re_evaluation_boundary_created",
    "presence_re_evaluation_operation_created",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "identity_created",
    "custody_created",
    "custody_proven",
    "provenance_created",
    "provenance_proven",
    "physical_validity_created",
    "physical_validity_proven",
    "authority_created",
    "truth_created",
    "standing_created",
    "relation_created",
    "coupling_assigned",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "public_interface_created",
    "public_intake_created",
    "output_authorized",
    "action_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "repeated_receiver_answerable_receipt_operation_permission_created",
    "reusable_receiver_answerable_receipt_operation_route_created",
    "same_receiver_answerable_receipt_operation_rerun_authorized",
    "automatic_receiver_answerable_receipt_operation_retry_created",
    "receiver_answerable_receipt_operation_debt_created",
    "receiver_answerable_receipt_operation_obligation_created",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
)

OMISSION_POSTURE_FIELDS = (
    "complete_receipt_boundary_artifact_omitted",
    "complete_receiver_attestation_operation_artifact_omitted",
    "complete_operation_basis_omitted",
    "complete_candidate_sufficiency_artifact_omitted",
    "complete_candidate_sufficiency_basis_omitted",
    "complete_receiver_attestation_boundary_artifact_omitted",
    "archive_bytes_omitted",
    "hash_record_body_omitted",
    "text_component_bodies_omitted",
    "recorded_signal_body_omitted",
)

BOUNDARY_REQUIRED_FALSE_LOCKS = (
    "action_authorized",
    "affected_file_repaired",
    "api_created",
    "authority_created",
    "automatic_receiver_answerable_receipt_boundary_retry_created",
    "coupling_assigned",
    "coupling_created",
    "custody_created",
    "field_machinery_created",
    "file_discovery_performed",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "identity_created",
    "output_authorized",
    "physical_validity_created",
    "presence_authorized",
    "presence_established",
    "presence_re_evaluation_boundary_created",
    "presence_recorded",
    "presence_supported",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "provenance_created",
    "public_intake_created",
    "public_interface_created",
    "receiver_answerable_receipt_boundary_created",
    "receiver_answerable_receipt_boundary_debt_created",
    "receiver_answerable_receipt_boundary_obligation_created",
    "receiver_answerable_receipt_operation_created",
    "receiver_answerable_receipt_operation_executed",
    "receiver_answerable_receipt_present",
    "receiver_answerable_receipt_result_recorded",
    "receiver_answerable_receipt_supported",
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "relation_created",
    "repeated_receiver_answerable_receipt_boundary_permission_created",
    "repository_scan_performed",
    "reusable_receiver_answerable_receipt_route_created",
    "runtime_created",
    "same_receiver_answerable_receipt_boundary_rerun_authorized",
    "standing_created",
    "synchronization_authorized",
    "truth_created",
    "validation_enforced",
)

ATTESTATION_REQUIRED_FALSE_LOCKS = (
    "action_authorized",
    "affected_file_repaired",
    "api_created",
    "authority_created",
    "automatic_receiver_attestation_operation_retry_created",
    "coupling_assigned",
    "coupling_created",
    "field_machinery_created",
    "file_discovery_performed",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "identity_created",
    "output_authorized",
    "presence_authorized",
    "presence_established",
    "presence_re_evaluation_boundary_created",
    "presence_recorded",
    "presence_supported",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "public_intake_created",
    "public_interface_created",
    "receiver_answerable_receipt_boundary_created",
    "receiver_answerable_receipt_present",
    "receiver_attestation_created",
    "receiver_attestation_operation_debt_created",
    "receiver_attestation_operation_obligation_created",
    "receiver_attestation_supported",
    "relation_created",
    "repeated_receiver_attestation_operation_permission_created",
    "repository_scan_performed",
    "reusable_receiver_attestation_operation_route_created",
    "runtime_created",
    "same_receiver_attestation_operation_rerun_authorized",
    "standing_created",
    "synchronization_authorized",
    "truth_created",
    "validation_enforced",
)

PROHIBITED_REQUEST_FLAGS = MappingProxyType(
    {
        "request_outcome_preclaim": "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "request_operation_result_preclaim": (
            "PROHIBITED_RESULT_PRECLAIM_REQUESTED"
        ),
        "request_completed_result_posture_preclaim": (
            "PROHIBITED_RESULT_PRECLAIM_REQUESTED"
        ),
        "request_receiver_answerable_receipt_preclaim": (
            "PROHIBITED_RECEIPT_PRECLAIM_REQUESTED"
        ),
        "request_receipt_result_preclaim": (
            "PROHIBITED_RECEIPT_PRECLAIM_REQUESTED"
        ),
        "request_presence_re_evaluation_preclaim": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_presence_support": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_presence_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_presence_establishment": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_presence_recording": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_identity_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_custody_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_custody_proof": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_provenance_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_provenance_proof": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_physical_validity_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_physical_validity_proof": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_authority_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_truth_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_standing_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_relation_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_coupling_assignment": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_coupling_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_field_machinery_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_runtime_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_api_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_public_interface_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_public_intake_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_output_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_action_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_synchronization_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_follow_on_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_follow_on_work_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_complete_receipt_boundary_artifact_embedding": (
            "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
        ),
        "request_complete_receiver_attestation_operation_artifact_embedding": (
            "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
        ),
        "request_complete_operation_basis_embedding": (
            "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
        ),
        "request_complete_candidate_sufficiency_artifact_embedding": (
            "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
        ),
        "request_complete_candidate_sufficiency_basis_embedding": (
            "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
        ),
        "request_complete_receiver_attestation_boundary_artifact_embedding": (
            "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
        ),
        "request_archive_bytes_embedding_or_read": (
            "PROHIBITED_SOURCE_BODY_READ_REQUESTED"
        ),
        "request_hash_record_body_embedding_or_read": (
            "PROHIBITED_SOURCE_BODY_READ_REQUESTED"
        ),
        "request_text_component_bodies_embedding_or_read": (
            "PROHIBITED_SOURCE_BODY_READ_REQUESTED"
        ),
        "request_recorded_signal_body_embedding_or_read": (
            "PROHIBITED_SOURCE_BODY_READ_REQUESTED"
        ),
        "request_repository_scan": (
            "PROHIBITED_DISCOVERY_OR_ALTERNATIVE_REQUESTED"
        ),
        "request_file_discovery": (
            "PROHIBITED_DISCOVERY_OR_ALTERNATIVE_REQUESTED"
        ),
        "request_glob": "PROHIBITED_DISCOVERY_OR_ALTERNATIVE_REQUESTED",
        "request_rglob": "PROHIBITED_DISCOVERY_OR_ALTERNATIVE_REQUESTED",
        "request_alternative_artifact_search": (
            "PROHIBITED_DISCOVERY_OR_ALTERNATIVE_REQUESTED"
        ),
        "request_replacement_result_inference": (
            "PROHIBITED_DISCOVERY_OR_ALTERNATIVE_REQUESTED"
        ),
        "request_affected_file_repair": (
            "PROHIBITED_REPAIR_OR_VALIDATION_REQUESTED"
        ),
        "request_validation_enforcement": (
            "PROHIBITED_REPAIR_OR_VALIDATION_REQUESTED"
        ),
        "request_contaminated_lineage_validation": (
            "PROHIBITED_CONTAMINATED_LINEAGE_VALIDATION_REQUESTED"
        ),
        "request_repeated_operation_permission_creation": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_reusable_operation_route_creation": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_same_operation_rerun": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_automatic_operation_retry_creation": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_operation_debt_creation": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_operation_obligation_creation": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_scheduled_work_creation": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
        "request_automatic_next_creation": (
            "PROHIBITED_REPEATED_USE_REQUESTED"
        ),
    }
)

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "REQUEST_FIELD_MISSING",
        "REQUEST_UNKNOWN_FIELD",
        "REQUEST_VALUE_MISMATCH",
        "REQUEST_BOOLEAN_INVALID",
        "UNSUPPORTED_INTENT",
        "EXPLICIT_BLOCK_REQUESTED",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        *PROHIBITED_REQUEST_FLAGS.values(),
        "OPERATION_SPEC_REFERENCE_MISSING",
        "OPERATION_SPEC_MARKER_MISSING",
        "RECEIPT_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
        "RECEIPT_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
        "RECEIPT_BOUNDARY_ARTIFACT_NOT_MAPPING",
        "RECEIPT_BOUNDARY_METADATA_MISMATCH",
        "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
        "RECEIPT_BOUNDARY_POSTURE_INVALID",
        "RECEIPT_BOUNDARY_FALSE_LOCK_NOT_FALSE",
        "RECEIVER_ATTESTATION_ARTIFACT_REFERENCE_MISSING",
        "RECEIVER_ATTESTATION_ARTIFACT_NOT_PARSEABLE",
        "RECEIVER_ATTESTATION_ARTIFACT_NOT_MAPPING",
        "RECEIVER_ATTESTATION_METADATA_MISMATCH",
        "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
        "RECEIVER_ATTESTATION_POSTURE_INVALID",
        "RECEIVER_ATTESTATION_FALSE_LOCK_NOT_FALSE",
        "UPSTREAM_CORRESPONDENCE_MISMATCH",
        "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
        "WRITE_REFUSED",
    }
)

SPEC_MARKER_FAMILIES = MappingProxyType(
    {
        "title": (
            "# Receiver-Side Answerable Basis Receiver-Answerable "
            "Receipt Operation V0 Minimum Specification",
        ),
        "operation_identity": (
            f"operation_id = {OPERATION_ID}",
            f"operation_type = {OPERATION_TYPE}",
            f"operation_version = {OPERATION_VERSION}",
            f"operation_scope = {OPERATION_SCOPE}",
        ),
        "exact_artifact_pair": (
            str(
                UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH
            ),
            str(
                SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
            ),
            "Neither artifact is sufficient alone.",
        ),
        "upstream_boundary": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_OUTCOME_REQUIRED,
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_RESULT_REQUIRED,
        ),
        "selected_attestation": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED,
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ID,
        ),
        "candidate": (CANDIDATE_ID, CANDIDATE_TYPE, CANDIDATE_SCOPE),
        "decision_inputs": DECISION_INPUT_FIELDS,
        "outcome_family": OUTCOME_FAMILY,
        "result_family": COMPLETED_RESULT_FAMILY,
        "precedence": (
            "`INDETERMINATE` takes precedence over `NOT_RECORDED`",
            "`NOT_RECORDED` takes precedence over `RECORDED`",
        ),
        "atomic_admission": (
            "The operation must admit the exact pair atomically",
            "Basis admission is not receipt.",
        ),
        "separation": (
            "receiver attestation recorded is not receiver-answerable receipt",
            "receipt consideration allowed is not receipt",
            "receipt boundary is not receipt operation",
            "receiver-answerable receipt is not presence",
            "open does not mean next",
        ),
        "no_new_external_or_waiting_basis": (
            "No new external source material",
            "No `REQUIRES_OPERATION_BASIS` waiting outcome is created",
        ),
        "future_route": (ADMISSIBLE_FUTURE_ROUTE,),
        "contaminated_lineage": (
            "All contaminated lineage remains unchanged.",
        ),
    }
)
SPEC_MARKERS = tuple(
    marker
    for family in SPEC_MARKER_FAMILIES.values()
    for marker in family
)

BLOCKED_ROUTES = (
    "candidate_sufficiency_to_receiver_answerable_receipt",
    "attestation_consideration_to_receiver_answerable_receipt",
    "receiver_attestation_recording_to_presence",
    "receipt_consideration_to_receipt_without_operation_evaluation",
    "archive_hash_text_or_signal_correspondence_to_receipt",
    "receipt_recording_to_identity_custody_provenance_physical_validity_authority_truth_standing_or_presence",
    "receipt_operation_result_to_presence_re_evaluation",
    "receipt_operation_result_to_relation_coupling_field_runtime_api_public_output_action_synchronization_or_follow_on",
    "operation_result_to_repeat_permission_reusable_route_rerun_retry_debt_obligation_scheduled_work_or_automatic_next",
    "operation_to_contaminated_lineage_repair_or_validation",
)

WHAT_REMAINS_OPEN = (
    "receiver-answerable-receipt operation tests",
    "receiver-answerable-receipt operation live result",
    "receiver-answerable-receipt operation terminal summary",
    "presence re-evaluation boundary",
    "presence re-evaluation operation",
    "presence support",
    "presence authorization",
    "presence establishment",
    "presence recording",
    "identity",
    "custody",
    "provenance",
    "physical validity",
    "authority",
    "truth",
    "standing",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "public interface",
    "public intake",
    "output",
    "action",
    "synchronization",
    "repair",
    "validation",
    "follow-on work",
)

RESULT_SECTIONS = frozenset(
    {
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_metadata",
        "declared_receiver_side_answerable_basis_receiver_answerable_receipt_operation_request",
        "selected_operation_and_candidate_identity",
        "specification_validation",
        "receiver_answerable_receipt_boundary_validation",
        "receiver_attestation_operation_validation",
        "upstream_correspondence_validation",
        "atomic_operation_basis_posture",
        "compact_upstream_standing",
        "operation_decision",
        "operation_posture",
        "operation_result_detail",
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation",
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_checks",
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_statement",
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_non_meaning",
        "omission_posture",
        "blocked_routes",
        "admissible_future_route",
        "what_remains_open",
        "non_claims",
        "result_level_non_claims_canonical_false",
        "outcome",
        "operation_result",
        "block",
        "resolver_module",
        "result_version",
        "failed_check_count",
        "passed_check_count",
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_summary",
    }
)


class ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError(
    Exception
):
    """Raised when bounded path loading, summarization, or writing fails."""


class _DuplicateJsonKeyError(ValueError):
    """Raised when strict JSON contains a duplicate object member."""


def _reject_duplicate_json_keys(
    pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKeyError(key)
        result[key] = value
    return result


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_omission_posture() -> dict[str, bool]:
    return {field: True for field in OMISSION_POSTURE_FIELDS}


def _check(
    name: str,
    passed: bool,
    code: str | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {"check": name, "passed": bool(passed)}
    if not passed and code is not None:
        result["failure_code"] = code
        result["block_code"] = code
    return result


def _expect(
    checks: list[dict[str, Any]],
    name: str,
    actual: Any,
    expected: Any,
    code: str,
) -> bool:
    if type(expected) is bool:
        passed = actual is expected
    elif type(expected) is int:
        passed = type(actual) is int and actual == expected
    else:
        passed = actual == expected
    checks.append(_check(name, passed, code))
    return passed


def _as_repo_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_text(value: Path | str) -> tuple[str | None, str | None]:
    path = _as_repo_path(value)
    if not path.is_file():
        return None, "not_a_file"
    try:
        return path.read_text(encoding="utf-8"), None
    except (OSError, UnicodeError):
        return None, "unreadable"


def _read_json(value: Path | str) -> tuple[Any | None, str | None]:
    text, error = _read_text(value)
    if error is not None or text is None:
        return None, error
    try:
        return (
            json.loads(
                text,
                object_pairs_hook=_reject_duplicate_json_keys,
                parse_constant=lambda value: (_ for _ in ()).throw(
                    ValueError(value)
                ),
            ),
            None,
        )
    except _DuplicateJsonKeyError:
        return None, "duplicate_key"
    except (json.JSONDecodeError, ValueError):
        return None, "not_parseable"


def _non_claims_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_FALSE_NON_CLAIMS)
        and all(
            value.get(field) is False
            for field in REQUIRED_FALSE_NON_CLAIMS
        )
    )


def _omission_posture_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(OMISSION_POSTURE_FIELDS)
        and all(value.get(field) is True for field in OMISSION_POSTURE_FIELDS)
    )


def _expected_request_values() -> dict[str, Any]:
    return {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "governing_receiver_answerable_receipt_operation_specification_path": (
            str(GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH)
        ),
        "upstream_receiver_answerable_receipt_boundary_artifact_path": str(
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH
        ),
        "selected_receiver_attestation_operation_artifact_path": str(
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
        "upstream_receiver_answerable_receipt_boundary_id": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ID
        ),
        "upstream_receiver_answerable_receipt_boundary_type": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_TYPE
        ),
        "upstream_receiver_answerable_receipt_boundary_version": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_VERSION
        ),
        "upstream_receiver_answerable_receipt_boundary_scope": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_SCOPE
        ),
        "upstream_receiver_answerable_receipt_boundary_outcome_required": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_OUTCOME_REQUIRED
        ),
        "upstream_receiver_answerable_receipt_boundary_result_required": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_RESULT_REQUIRED
        ),
        "selected_receiver_attestation_operation_id": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
        ),
        "selected_receiver_attestation_operation_type": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
        ),
        "selected_receiver_attestation_operation_version": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
        ),
        "selected_receiver_attestation_operation_scope": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE
        ),
        "selected_receiver_attestation_operation_result_required": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        **dict(CANONICAL_DECISION_INPUTS),
    }


def build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one fresh canonical request with visible bounded overrides."""
    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **_expected_request_values(),
        "declared_non_claims": _canonical_non_claims(),
    }
    request.update({field: False for field in PROHIBITED_REQUEST_FLAGS})
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one declared request while retaining all supplied overrides."""
    return (
        build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_request(
            **overrides
        )
    )


def _request_keys() -> set[str]:
    return {
        "intent",
        "declared_non_claims",
        *_expected_request_values(),
        *PROHIBITED_REQUEST_FLAGS,
    }


def _request_preclaim_fields() -> set[str]:
    return {
        "outcome",
        "operation_result",
        "completed_result_posture_count",
        "receiver_answerable_receipt_operation_recorded",
        "receiver_answerable_receipt_operation_result_recorded",
        "receiver_answerable_receipt_operation_exhausted",
        "receiver_answerable_receipt_decided",
        "receiver_answerable_receipt_recorded",
        "receiver_answerable_receipt_not_recorded",
        "receiver_answerable_receipt_indeterminate",
        "receiver_answerable_receipt_present",
        "complete_receipt_boundary_artifact",
        "complete_receiver_attestation_operation_artifact",
        "complete_operation_basis",
        "archive_bytes",
        "hash_record_body",
        "text_component_bodies",
        "recorded_signal_body",
        *REQUIRED_FALSE_NON_CLAIMS,
    }


def _operation_basis_supplied(request: Mapping[str, Any]) -> bool:
    return (
        request.get(
            "upstream_receiver_answerable_receipt_boundary_artifact_path"
        )
        == str(
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH
        )
        and request.get(
            "selected_receiver_attestation_operation_artifact_path"
        )
        == str(
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
        )
    )


def _validate_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    if request.get("intent") == INTENT_BLOCK:
        checks.append(
            _check("request.intent.explicit_block", False, "EXPLICIT_BLOCK_REQUESTED")
        )
        return "EXPLICIT_BLOCK_REQUESTED", "explicit block intent was requested"
    if request.get("intent") not in SUPPORTED_INTENTS:
        checks.append(_check("request.intent", False, "UNSUPPORTED_INTENT"))
        return "UNSUPPORTED_INTENT", "intent is not supported"
    checks.append(_check("request.intent", True))

    if set(request).intersection(_request_preclaim_fields()):
        checks.append(
            _check(
                "request.result_preclaim_absent",
                False,
                "RESULT_POSTURE_PRECLAIMED",
            )
        )
        return (
            "RESULT_POSTURE_PRECLAIMED",
            "caller supplied a result, branch posture, or complete material",
        )
    checks.append(_check("request.result_preclaim_absent", True))

    expected_keys = _request_keys()
    if expected_keys.difference(request):
        checks.append(
            _check(
                "request.canonical_fields_present",
                False,
                "REQUEST_FIELD_MISSING",
            )
        )
        return "REQUEST_FIELD_MISSING", "canonical request fields are missing"
    checks.append(_check("request.canonical_fields_present", True))
    if set(request).difference(expected_keys):
        checks.append(
            _check(
                "request.no_unknown_fields",
                False,
                "REQUEST_UNKNOWN_FIELD",
            )
        )
        return "REQUEST_UNKNOWN_FIELD", "request contains unknown fields"
    checks.append(_check("request.no_unknown_fields", True))

    for field, expected in _expected_request_values().items():
        actual = request.get(field)
        if field in DECISION_INPUT_FIELDS:
            valid = type(actual) is bool
            checks.append(
                _check(
                    "request." + field,
                    valid,
                    "REQUEST_BOOLEAN_INVALID",
                )
            )
            if not valid:
                return (
                    "REQUEST_BOOLEAN_INVALID",
                    field + " must be an exact Boolean",
                )
            continue
        code = "REQUEST_VALUE_MISMATCH"
        if not _expect(checks, "request." + field, actual, expected, code):
            return code, field + " does not match the canonical request"

    if not _non_claims_valid(request.get("declared_non_claims")):
        checks.append(
            _check(
                "request.declared_non_claims",
                False,
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )
        )
        return (
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared non-claims must be the exact canonical false set",
        )
    checks.append(_check("request.declared_non_claims", True))

    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        actual = request.get(field)
        if type(actual) is not bool:
            checks.append(
                _check("request." + field, False, "REQUEST_BOOLEAN_INVALID")
            )
            return (
                "REQUEST_BOOLEAN_INVALID",
                field + " must be an exact Boolean",
            )
        if actual is not False:
            checks.append(_check("request." + field, False, code))
            return code, field + " must remain false"
        checks.append(_check("request." + field, True))
    return None, None


def _empty_specification_validation(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "specification_path": request.get(
            "governing_receiver_answerable_receipt_operation_specification_path"
        ),
        "marker_validation": {
            family: False for family in SPEC_MARKER_FAMILIES
        },
        "specification_validated": False,
    }


def _validate_specification(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    state = _empty_specification_validation(request)
    text, error = _read_text(
        request[
            "governing_receiver_answerable_receipt_operation_specification_path"
        ]
    )
    if error is not None or text is None:
        checks.append(
            _check(
                "specification.readable",
                False,
                "OPERATION_SPEC_REFERENCE_MISSING",
            )
        )
        return (
            "OPERATION_SPEC_REFERENCE_MISSING",
            "governing operation specification is unavailable",
            state,
        )
    checks.append(_check("specification.readable", True))
    for family, markers in SPEC_MARKER_FAMILIES.items():
        valid = all(marker in text for marker in markers)
        state["marker_validation"][family] = valid
        checks.append(
            _check(
                "specification." + family,
                valid,
                "OPERATION_SPEC_MARKER_MISSING",
            )
        )
        if not valid:
            return (
                "OPERATION_SPEC_MARKER_MISSING",
                "governing specification marker family is incomplete: "
                + family,
                state,
            )
    state["specification_validated"] = True
    return None, None, state


def _empty_boundary_validation(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "artifact_path": request.get(
            "upstream_receiver_answerable_receipt_boundary_artifact_path"
        ),
        "metadata": {},
        "boundary_identity": {},
        "selected_operation_identity": {},
        "selected_candidate_identity": {},
        "decision": {},
        "completed_consideration_posture_count": 0,
        "boundary_allowed_validated": False,
        "boundary_cardinality_validated": False,
        "boundary_completion_validated": False,
        "upstream_false_locks_validated": False,
        "omission_posture_validated": False,
        "artifact_validated": False,
        "complete_receipt_boundary_artifact_omitted": True,
    }


def _require_mapping_sections(
    artifact: Mapping[str, Any],
    names: Sequence[str],
) -> bool:
    return all(isinstance(artifact.get(name), Mapping) for name in names)


def _validate_boundary_artifact(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    state = _empty_boundary_validation(request)
    artifact, error = _read_json(
        request[
            "upstream_receiver_answerable_receipt_boundary_artifact_path"
        ]
    )
    if error in {"not_a_file", "unreadable"}:
        checks.append(
            _check(
                "receipt_boundary.readable",
                False,
                "RECEIPT_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
            )
        )
        return (
            "RECEIPT_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
            "exact receipt-boundary artifact is unavailable",
            state,
        )
    if error is not None:
        checks.append(
            _check(
                "receipt_boundary.parseable",
                False,
                "RECEIPT_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
            )
        )
        return (
            "RECEIPT_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
            "exact receipt-boundary artifact is not strict canonical JSON",
            state,
        )
    if not isinstance(artifact, Mapping):
        checks.append(
            _check(
                "receipt_boundary.mapping",
                False,
                "RECEIPT_BOUNDARY_ARTIFACT_NOT_MAPPING",
            )
        )
        return (
            "RECEIPT_BOUNDARY_ARTIFACT_NOT_MAPPING",
            "exact receipt-boundary artifact is not a mapping",
            state,
        )
    checks.append(_check("receipt_boundary.mapping", True))

    section_names = (
        "receiver_side_answerable_basis_receiver_answerable_receipt_boundary_metadata",
        "selected_operation_and_candidate_identity",
        "boundary_decision",
        "boundary_posture",
        "receiver_side_answerable_basis_receiver_answerable_receipt_boundary",
        "specification_validation",
        "upstream_artifact_validation",
        "omission_posture",
        "non_claims",
        "receiver_side_answerable_basis_receiver_answerable_receipt_boundary_summary",
        "block",
    )
    if not _require_mapping_sections(artifact, section_names):
        checks.append(
            _check(
                "receipt_boundary.sections",
                False,
                "RECEIPT_BOUNDARY_ARTIFACT_NOT_MAPPING",
            )
        )
        return (
            "RECEIPT_BOUNDARY_ARTIFACT_NOT_MAPPING",
            "receipt-boundary artifact lacks canonical mapping sections",
            state,
        )
    checks.append(_check("receipt_boundary.sections", True))

    metadata = artifact[
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_boundary_metadata"
    ]
    identity = artifact["selected_operation_and_candidate_identity"]
    decision = artifact["boundary_decision"]
    posture = artifact["boundary_posture"]
    boundary = artifact[
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_boundary"
    ]
    specification = artifact["specification_validation"]
    upstream = artifact["upstream_artifact_validation"]
    omission = artifact["omission_posture"]
    non_claims = artifact["non_claims"]
    summary = artifact[
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_boundary_summary"
    ]
    block = artifact["block"]

    top_expectations = {
        "resolver_module": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_RESOLVER_MODULE
        ),
        "result_version": RESULT_VERSION,
        "outcome": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_OUTCOME_REQUIRED
        ),
        "boundary_result": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_RESULT_REQUIRED
        ),
        "failed_check_count": 0,
        "passed_check_count": 173,
        "result_level_non_claims_canonical_false": True,
    }
    for field, expected in top_expectations.items():
        if not _expect(
            checks,
            "receipt_boundary.metadata." + field,
            artifact.get(field),
            expected,
            "RECEIPT_BOUNDARY_METADATA_MISMATCH",
        ):
            return (
                "RECEIPT_BOUNDARY_METADATA_MISMATCH",
                "receipt-boundary metadata does not match: " + field,
                state,
            )
    for field, expected in {
        "blocked": False,
        "code": None,
        "block_code": None,
        "reason": None,
    }.items():
        if not _expect(
            checks,
            "receipt_boundary.block." + field,
            block.get(field),
            expected,
            "RECEIPT_BOUNDARY_METADATA_MISMATCH",
        ):
            return (
                "RECEIPT_BOUNDARY_METADATA_MISMATCH",
                "receipt-boundary block posture is not clean",
                state,
            )

    metadata_expectations = {
        "boundary_id": UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ID,
        "boundary_type": UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_TYPE,
        "boundary_version": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_VERSION
        ),
        "boundary_scope": UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_SCOPE,
        "selected_upstream_artifact_path": str(
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
        ),
    }
    for field, expected in metadata_expectations.items():
        if not _expect(
            checks,
            "receipt_boundary.identity.metadata." + field,
            metadata.get(field),
            expected,
            "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
        ):
            return (
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
                "receipt-boundary identity does not match: " + field,
                state,
            )

    boundary_identity_expectations = {
        "boundary_id": UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ID,
        "boundary_type": UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_TYPE,
        "boundary_version": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_VERSION
        ),
        "boundary_scope": UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_SCOPE,
        "receiver_side_answerable_basis_receiver_answerable_receipt_boundary_id": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ID
        ),
        "receiver_side_answerable_basis_receiver_answerable_receipt_boundary_type": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_TYPE
        ),
        "receiver_side_answerable_basis_receiver_answerable_receipt_boundary_version": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_VERSION
        ),
        "receiver_side_answerable_basis_receiver_answerable_receipt_boundary_scope": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_SCOPE
        ),
    }
    for field, expected in boundary_identity_expectations.items():
        if not _expect(
            checks,
            "receipt_boundary.identity.boundary." + field,
            boundary.get(field),
            expected,
            "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
        ):
            return (
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
                "receipt-boundary object identity does not match: " + field,
                state,
            )

    selected_expectations = {
        "selected_receiver_attestation_operation_id": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
        ),
        "selected_receiver_attestation_operation_type": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
        ),
        "selected_receiver_attestation_operation_version": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
        ),
        "selected_receiver_attestation_operation_scope": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE
        ),
        "selected_receiver_attestation_operation_result_required": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
    }
    for field, expected in selected_expectations.items():
        for location, value in (
            ("selected_identity", identity),
            ("boundary_object", boundary),
        ):
            if not _expect(
                checks,
                "receipt_boundary.identity."
                + location
                + "."
                + field,
                value.get(field),
                expected,
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ):
                return (
                    "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
                    "receipt-boundary selected identity does not match: "
                    + field,
                    state,
                )

    decision_expectations = {
        "selection": True,
        "decision_code": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_DECISION_CODE
        ),
        "decision_reason": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_DECISION_REASON
        ),
    }
    for field, expected in decision_expectations.items():
        if not _expect(
            checks,
            "receipt_boundary.decision." + field,
            decision.get(field),
            expected,
            "RECEIPT_BOUNDARY_POSTURE_INVALID",
        ):
            return (
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
                "receipt-boundary decision posture is invalid: " + field,
                state,
            )

    posture_expectations = {
        "completed_consideration_posture_count": 1,
        "receiver_answerable_receipt_boundary_recorded": True,
        "receiver_answerable_receipt_boundary_result_recorded": True,
        "receiver_answerable_receipt_boundary_exhausted": True,
        "receiver_answerable_receipt_consideration_allowed": True,
        "receiver_answerable_receipt_consideration_not_allowed": False,
        "single_use_only": True,
    }
    for field, expected in posture_expectations.items():
        if not _expect(
            checks,
            "receipt_boundary.posture." + field,
            posture.get(field),
            expected,
            "RECEIPT_BOUNDARY_POSTURE_INVALID",
        ):
            return (
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
                "receipt-boundary completed posture is invalid: " + field,
                state,
            )

    boundary_posture_expectations = {
        "receiver_answerable_receipt_boundary_result": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_RESULT_REQUIRED
        ),
        "receiver_answerable_receipt_consideration_selected": True,
        "receiver_answerable_receipt_boundary_recorded": True,
        "receiver_answerable_receipt_boundary_result_recorded": True,
        "receiver_answerable_receipt_boundary_exhausted": True,
        "receiver_answerable_receipt_consideration_allowed": True,
        "receiver_answerable_receipt_consideration_not_allowed": False,
        "admissible_future_route": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_FUTURE_ROUTE
        ),
    }
    for field, expected in boundary_posture_expectations.items():
        if not _expect(
            checks,
            "receipt_boundary.object_posture." + field,
            boundary.get(field),
            expected,
            "RECEIPT_BOUNDARY_POSTURE_INVALID",
        ):
            return (
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
                "receipt-boundary object posture is invalid: " + field,
                state,
            )

    summary_expectations = {
        "specification_validated": True,
        "upstream_artifact_validated": True,
        "exact_recorded_result_validated": True,
        "result_cardinality_validated": True,
        "upstream_false_locks_validated": True,
        "operation_completed_and_exhausted": True,
        "receiver_attestation_recorded": True,
        "boundary_recorded": True,
        "boundary_result_recorded": True,
        "boundary_exhausted": True,
        "consideration_allowed": True,
        "consideration_not_allowed": False,
        "receipt_absent": True,
        "receipt_operation_absent": True,
        "presence_absent": True,
        "downstream_non_claims_canonical_false": True,
        "result_level_non_claims_canonical_false": True,
        "complete_material_omission_posture": True,
        "selection": True,
        "decision_code": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_DECISION_CODE
        ),
        "decision_reason": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_DECISION_REASON
        ),
    }
    for field, expected in summary_expectations.items():
        if not _expect(
            checks,
            "receipt_boundary.summary." + field,
            summary.get(field),
            expected,
            "RECEIPT_BOUNDARY_POSTURE_INVALID",
        ):
            return (
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
                "receipt-boundary summary posture is invalid: " + field,
                state,
            )

    for location, value, expectations in (
        (
            "specification_validation",
            specification,
            {"specification_validated": True},
        ),
        (
            "upstream_artifact_validation",
            upstream,
            {
                "artifact_validated": True,
                "exact_recorded_result_validated": True,
                "result_cardinality_validated": True,
                "upstream_false_locks_validated": True,
                "operation_completed_and_exhausted": True,
                "receiver_attestation_recorded": True,
                "complete_material_not_embedded": True,
                "source_bodies_not_read": True,
            },
        ),
    ):
        for field, expected in expectations.items():
            if not _expect(
                checks,
                "receipt_boundary." + location + "." + field,
                value.get(field),
                expected,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ):
                return (
                    "RECEIPT_BOUNDARY_POSTURE_INVALID",
                    "receipt-boundary validation posture is invalid: "
                    + field,
                    state,
                )

    expected_boundary_omissions = {
        "archive_bytes_omitted",
        "complete_candidate_sufficiency_artifact_omitted",
        "complete_candidate_sufficiency_basis_omitted",
        "complete_operation_basis_omitted",
        "complete_receiver_attestation_boundary_artifact_omitted",
        "complete_selected_upstream_operation_artifact_omitted",
        "hash_record_body_omitted",
        "recorded_signal_body_omitted",
        "text_component_bodies_omitted",
    }
    omission_valid = (
        set(omission) == expected_boundary_omissions
        and all(omission.get(field) is True for field in omission)
    )
    checks.append(
        _check(
            "receipt_boundary.omission_posture",
            omission_valid,
            "RECEIPT_BOUNDARY_POSTURE_INVALID",
        )
    )
    if not omission_valid:
        return (
            "RECEIPT_BOUNDARY_POSTURE_INVALID",
            "receipt-boundary omission posture is invalid",
            state,
        )

    false_locks_valid = (
        set(non_claims) == set(BOUNDARY_REQUIRED_FALSE_LOCKS)
        and all(
            non_claims.get(field) is False
            and boundary.get(field) is False
            for field in BOUNDARY_REQUIRED_FALSE_LOCKS
        )
    )
    checks.append(
        _check(
            "receipt_boundary.false_locks",
            false_locks_valid,
            "RECEIPT_BOUNDARY_FALSE_LOCK_NOT_FALSE",
        )
    )
    if not false_locks_valid:
        return (
            "RECEIPT_BOUNDARY_FALSE_LOCK_NOT_FALSE",
            "receipt-boundary false locks are not exact canonical false",
            state,
        )

    state.update(
        {
            "metadata": {
                "resolver_module": artifact.get("resolver_module"),
                "result_version": artifact.get("result_version"),
                "outcome": artifact.get("outcome"),
                "boundary_result": artifact.get("boundary_result"),
                "failed_check_count": artifact.get("failed_check_count"),
                "passed_check_count": artifact.get("passed_check_count"),
            },
            "boundary_identity": {
                field: boundary.get(field)
                for field in (
                    "boundary_id",
                    "boundary_type",
                    "boundary_version",
                    "boundary_scope",
                )
            },
            "selected_operation_identity": {
                field: identity.get(field)
                for field in (
                    "selected_receiver_attestation_operation_id",
                    "selected_receiver_attestation_operation_type",
                    "selected_receiver_attestation_operation_version",
                    "selected_receiver_attestation_operation_scope",
                    "selected_receiver_attestation_operation_result_required",
                )
            },
            "selected_candidate_identity": {
                field: identity.get(field)
                for field in (
                    "receiver_side_answerable_basis_candidate_id",
                    "receiver_side_answerable_basis_candidate_type",
                    "receiver_side_answerable_basis_candidate_scope",
                )
            },
            "selected_upstream_artifact_path": metadata.get(
                "selected_upstream_artifact_path"
            ),
            "decision": copy.deepcopy(dict(decision)),
            "completed_consideration_posture_count": posture.get(
                "completed_consideration_posture_count"
            ),
            "boundary_allowed_validated": True,
            "boundary_cardinality_validated": True,
            "boundary_completion_validated": True,
            "upstream_false_locks_validated": True,
            "omission_posture_validated": True,
            "artifact_validated": True,
        }
    )
    return None, None, state


def _empty_attestation_validation(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "artifact_path": request.get(
            "selected_receiver_attestation_operation_artifact_path"
        ),
        "metadata": {},
        "operation_identity": {},
        "selected_candidate_identity": {},
        "operation_result": RESULT_NOT_EVALUATED,
        "completed_result_posture_count": 0,
        "operation_basis_supplied": False,
        "operation_basis_admitted": False,
        "operation_completed_and_exhausted": False,
        "receiver_attestation_recorded": False,
        "minimum_admission_checks_passed": False,
        "archive_correspondence_validated": False,
        "text_components_validated": False,
        "timestamp_validated": False,
        "trace_paths_validated": False,
        "recorded_signal_artifact_existence_validated": False,
        "upstream_false_locks_validated": False,
        "artifact_validated": False,
        "complete_receiver_attestation_operation_artifact_omitted": True,
    }


def _validate_attestation_artifact(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    state = _empty_attestation_validation(request)
    artifact, error = _read_json(
        request["selected_receiver_attestation_operation_artifact_path"]
    )
    if error in {"not_a_file", "unreadable"}:
        checks.append(
            _check(
                "receiver_attestation.readable",
                False,
                "RECEIVER_ATTESTATION_ARTIFACT_REFERENCE_MISSING",
            )
        )
        return (
            "RECEIVER_ATTESTATION_ARTIFACT_REFERENCE_MISSING",
            "exact receiver-attestation artifact is unavailable",
            state,
        )
    if error is not None:
        checks.append(
            _check(
                "receiver_attestation.parseable",
                False,
                "RECEIVER_ATTESTATION_ARTIFACT_NOT_PARSEABLE",
            )
        )
        return (
            "RECEIVER_ATTESTATION_ARTIFACT_NOT_PARSEABLE",
            "exact receiver-attestation artifact is not strict canonical JSON",
            state,
        )
    if not isinstance(artifact, Mapping):
        checks.append(
            _check(
                "receiver_attestation.mapping",
                False,
                "RECEIVER_ATTESTATION_ARTIFACT_NOT_MAPPING",
            )
        )
        return (
            "RECEIVER_ATTESTATION_ARTIFACT_NOT_MAPPING",
            "exact receiver-attestation artifact is not a mapping",
            state,
        )
    checks.append(_check("receiver_attestation.mapping", True))

    section_names = (
        "receiver_side_answerable_basis_receiver_attestation_operation_metadata",
        "selected_operation_and_candidate_identity",
        "supplied_operation_basis_admission_metadata",
        "bounded_component_validation",
        "receiver_side_answerable_basis_receiver_attestation_operation",
        "operation_result_detail",
        "operation_posture",
        "receiver_side_answerable_basis_receiver_attestation_operation_non_meaning",
        "receiver_side_answerable_basis_receiver_attestation_operation_summary",
        "non_claims",
        "block",
    )
    if not _require_mapping_sections(artifact, section_names):
        checks.append(
            _check(
                "receiver_attestation.sections",
                False,
                "RECEIVER_ATTESTATION_ARTIFACT_NOT_MAPPING",
            )
        )
        return (
            "RECEIVER_ATTESTATION_ARTIFACT_NOT_MAPPING",
            "receiver-attestation artifact lacks canonical mapping sections",
            state,
        )
    checks.append(_check("receiver_attestation.sections", True))

    metadata = artifact[
        "receiver_side_answerable_basis_"
        "receiver_attestation_operation_metadata"
    ]
    identity = artifact["selected_operation_and_candidate_identity"]
    basis = artifact["supplied_operation_basis_admission_metadata"]
    components = artifact["bounded_component_validation"]
    operation = artifact[
        "receiver_side_answerable_basis_receiver_attestation_operation"
    ]
    detail = artifact["operation_result_detail"]
    posture = artifact["operation_posture"]
    non_meaning = artifact[
        "receiver_side_answerable_basis_"
        "receiver_attestation_operation_non_meaning"
    ]
    summary = artifact[
        "receiver_side_answerable_basis_"
        "receiver_attestation_operation_summary"
    ]
    non_claims = artifact["non_claims"]
    block = artifact["block"]

    top_expectations = {
        "resolver_module": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESOLVER_MODULE
        ),
        "result_version": RESULT_VERSION,
        "outcome": SELECTED_RECEIVER_ATTESTATION_OPERATION_OUTCOME_REQUIRED,
        "failed_check_count": 0,
        "passed_check_count": 160,
    }
    for field, expected in top_expectations.items():
        if not _expect(
            checks,
            "receiver_attestation.metadata." + field,
            artifact.get(field),
            expected,
            "RECEIVER_ATTESTATION_METADATA_MISMATCH",
        ):
            return (
                "RECEIVER_ATTESTATION_METADATA_MISMATCH",
                "receiver-attestation metadata does not match: " + field,
                state,
            )
    for field, expected in {
        "blocked": False,
        "code": None,
        "block_code": None,
        "reason": None,
    }.items():
        if not _expect(
            checks,
            "receiver_attestation.block." + field,
            block.get(field),
            expected,
            "RECEIVER_ATTESTATION_METADATA_MISMATCH",
        ):
            return (
                "RECEIVER_ATTESTATION_METADATA_MISMATCH",
                "receiver-attestation block posture is not clean",
                state,
            )

    operation_identity_expectations = {
        "operation_id": SELECTED_RECEIVER_ATTESTATION_OPERATION_ID,
        "operation_type": SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE,
        "operation_version": SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION,
        "operation_scope": SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE,
        "receiver_side_answerable_basis_receiver_attestation_operation_id": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
        ),
        "receiver_side_answerable_basis_receiver_attestation_operation_type": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
        ),
        "receiver_side_answerable_basis_receiver_attestation_operation_version": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
        ),
        "receiver_side_answerable_basis_receiver_attestation_operation_scope": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE
        ),
    }
    for field, expected in operation_identity_expectations.items():
        if not _expect(
            checks,
            "receiver_attestation.operation_identity." + field,
            operation.get(field),
            expected,
            "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
        ):
            return (
                "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
                "receiver-attestation operation identity does not match: "
                + field,
                state,
            )
    for field, expected in {
        "operation_id": SELECTED_RECEIVER_ATTESTATION_OPERATION_ID,
        "operation_type": SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE,
        "operation_version": SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION,
        "operation_scope": SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE,
    }.items():
        if not _expect(
            checks,
            "receiver_attestation.metadata_identity." + field,
            metadata.get(field),
            expected,
            "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
        ):
            return (
                "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
                "receiver-attestation metadata identity does not match: "
                + field,
                state,
            )

    candidate_expectations = {
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
    }
    for field, expected in candidate_expectations.items():
        identity_field = field.replace(
            "receiver_side_answerable_basis_candidate_", "selected_candidate_"
        )
        for location, value, key in (
            ("operation", operation, field),
            ("selected_identity", identity, identity_field),
        ):
            if not _expect(
                checks,
                "receiver_attestation.candidate."
                + location
                + "."
                + key,
                value.get(key),
                expected,
                "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
            ):
                return (
                    "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
                    "receiver-attestation candidate identity does not match: "
                    + key,
                    state,
                )

    operation_posture_expectations = {
        "operation_basis_supplied": True,
        "operation_basis_admitted": True,
        "receiver_attestation_operation_result": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
        ),
        "receiver_attestation_operation_recorded": True,
        "receiver_attestation_operation_result_recorded": True,
        "receiver_attestation_operation_exhausted": True,
        "receiver_attestation_decided": True,
        "receiver_attestation_recorded": True,
        "receiver_attestation_not_recorded": False,
        "receiver_attestation_indeterminate": False,
    }
    for field, expected in operation_posture_expectations.items():
        if not _expect(
            checks,
            "receiver_attestation.operation_posture." + field,
            operation.get(field),
            expected,
            "RECEIVER_ATTESTATION_POSTURE_INVALID",
        ):
            return (
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
                "receiver-attestation operation posture is invalid: " + field,
                state,
            )

    basis_expectations = {
        "basis_supplied": True,
        "basis_admitted": True,
        "schema_validated": True,
        "hash_declaration_validated": True,
        "basis_non_claims_validated": True,
        "non_conversion_statement_validated": True,
        "complete_operation_basis_omitted": True,
    }
    for field, expected in basis_expectations.items():
        if not _expect(
            checks,
            "receiver_attestation.basis." + field,
            basis.get(field),
            expected,
            "RECEIVER_ATTESTATION_POSTURE_INVALID",
        ):
            return (
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
                "receiver-attestation basis posture is invalid: " + field,
                state,
            )

    archive_validation = components.get("archive_validation")
    if not isinstance(archive_validation, Mapping):
        checks.append(
            _check(
                "receiver_attestation.archive_validation",
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            )
        )
        return (
            "RECEIVER_ATTESTATION_POSTURE_INVALID",
            "receiver-attestation archive validation is absent",
            state,
        )
    component_expectations = {
        "trace_paths_validated": True,
        "text_components_validated": True,
        "timestamp_validated": True,
        "recorded_signal_artifact_existence_validated": True,
        "minimum_admission_checks_passed": True,
        "archive_bytes_omitted": True,
        "hash_record_body_omitted": True,
        "text_component_bodies_omitted": True,
        "recorded_signal_body_omitted": True,
    }
    for field, expected in component_expectations.items():
        if not _expect(
            checks,
            "receiver_attestation.components." + field,
            components.get(field),
            expected,
            "RECEIVER_ATTESTATION_POSTURE_INVALID",
        ):
            return (
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
                "receiver-attestation component posture is invalid: " + field,
                state,
            )
    if not _expect(
        checks,
        "receiver_attestation.components.archive_correspondence_validated",
        archive_validation.get("correspondence_validated"),
        True,
        "RECEIVER_ATTESTATION_POSTURE_INVALID",
    ):
        return (
            "RECEIVER_ATTESTATION_POSTURE_INVALID",
            "receiver-attestation archive correspondence is invalid",
            state,
        )

    for location, value, expectations in (
        (
            "detail",
            detail,
            {
                "operation_result": (
                    SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
                ),
                "completed_result_posture_count": 1,
            },
        ),
        (
            "posture",
            posture,
            {
                "operation_recorded": True,
                "operation_result_recorded": True,
                "operation_exhausted": True,
                "receiver_attestation_decided": True,
                "single_use_only": True,
                "originating_occurrence_created_by_source_body": False,
            },
        ),
        (
            "non_meaning",
            non_meaning,
            {"operation_result_present": True},
        ),
        (
            "summary",
            summary,
            {
                "basis_supplied": True,
                "basis_admitted": True,
                "upstream_boundary_validated": True,
                "trace_paths_validated": True,
                "archive_correspondence_validated": True,
                "text_components_validated": True,
                "timestamp_validated": True,
                "recorded_signal_artifact_existence_validated": True,
                "receiver_attestation_recorded": True,
                "receiver_attestation_not_recorded": False,
                "receiver_attestation_indeterminate": False,
                "receiver_attestation_operation_recorded": True,
                "receiver_attestation_operation_exhausted": True,
                "result_level_non_claims_canonical_false": True,
            },
        ),
    ):
        for field, expected in expectations.items():
            if not _expect(
                checks,
                "receiver_attestation." + location + "." + field,
                value.get(field),
                expected,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ):
                return (
                    "RECEIVER_ATTESTATION_POSTURE_INVALID",
                    "receiver-attestation "
                    + location
                    + " posture is invalid: "
                    + field,
                    state,
                )

    false_locks_valid = (
        set(non_claims) == set(ATTESTATION_REQUIRED_FALSE_LOCKS)
        and all(
            non_claims.get(field) is False
            and operation.get(field) is False
            for field in ATTESTATION_REQUIRED_FALSE_LOCKS
        )
    )
    checks.append(
        _check(
            "receiver_attestation.false_locks",
            false_locks_valid,
            "RECEIVER_ATTESTATION_FALSE_LOCK_NOT_FALSE",
        )
    )
    if not false_locks_valid:
        return (
            "RECEIVER_ATTESTATION_FALSE_LOCK_NOT_FALSE",
            "receiver-attestation false locks are not exact canonical false",
            state,
        )

    state.update(
        {
            "metadata": {
                "resolver_module": artifact.get("resolver_module"),
                "result_version": artifact.get("result_version"),
                "outcome": artifact.get("outcome"),
                "failed_check_count": artifact.get("failed_check_count"),
                "passed_check_count": artifact.get("passed_check_count"),
            },
            "operation_identity": {
                field: operation.get(field)
                for field in (
                    "operation_id",
                    "operation_type",
                    "operation_version",
                    "operation_scope",
                )
            },
            "selected_candidate_identity": {
                "receiver_side_answerable_basis_candidate_id": operation.get(
                    "receiver_side_answerable_basis_candidate_id"
                ),
                "receiver_side_answerable_basis_candidate_type": operation.get(
                    "receiver_side_answerable_basis_candidate_type"
                ),
                "receiver_side_answerable_basis_candidate_scope": operation.get(
                    "receiver_side_answerable_basis_candidate_scope"
                ),
            },
            "operation_result": operation.get(
                "receiver_attestation_operation_result"
            ),
            "completed_result_posture_count": detail.get(
                "completed_result_posture_count"
            ),
            "operation_basis_supplied": True,
            "operation_basis_admitted": True,
            "operation_completed_and_exhausted": True,
            "receiver_attestation_recorded": True,
            "minimum_admission_checks_passed": True,
            "archive_correspondence_validated": True,
            "text_components_validated": True,
            "timestamp_validated": True,
            "trace_paths_validated": True,
            "recorded_signal_artifact_existence_validated": True,
            "upstream_false_locks_validated": True,
            "artifact_validated": True,
        }
    )
    return None, None, state


def _empty_correspondence_validation() -> dict[str, Any]:
    return {
        "selected_attestation_operation_identity_corresponds": False,
        "selected_candidate_identity_corresponds": False,
        "selected_attestation_result_corresponds": False,
        "selected_attestation_artifact_path_corresponds": False,
        "boundary_allowed_validated": False,
        "attestation_recorded_validated": False,
        "boundary_cardinality_validated": False,
        "attestation_cardinality_validated": False,
        "operation_completion_and_exhaustion_validated": False,
        "required_false_locks_correspond": False,
        "upstream_correspondence_validated": False,
    }


def _validate_correspondence(
    boundary: Mapping[str, Any],
    attestation: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    state = _empty_correspondence_validation()
    boundary_operation = boundary.get("selected_operation_identity")
    attestation_operation = attestation.get("operation_identity")
    boundary_candidate = boundary.get("selected_candidate_identity")
    attestation_candidate = attestation.get("selected_candidate_identity")
    if not all(
        isinstance(value, Mapping)
        for value in (
            boundary_operation,
            attestation_operation,
            boundary_candidate,
            attestation_candidate,
        )
    ):
        checks.append(
            _check(
                "correspondence.compact_identity",
                False,
                "UPSTREAM_CORRESPONDENCE_MISMATCH",
            )
        )
        return (
            "UPSTREAM_CORRESPONDENCE_MISMATCH",
            "compact upstream identity is unavailable",
            state,
        )

    operation_corresponds = all(
        boundary_operation.get(boundary_field)
        == attestation_operation.get(attestation_field)
        for boundary_field, attestation_field in (
            ("selected_receiver_attestation_operation_id", "operation_id"),
            (
                "selected_receiver_attestation_operation_type",
                "operation_type",
            ),
            (
                "selected_receiver_attestation_operation_version",
                "operation_version",
            ),
            (
                "selected_receiver_attestation_operation_scope",
                "operation_scope",
            ),
        )
    )
    state["selected_attestation_operation_identity_corresponds"] = (
        operation_corresponds
    )
    checks.append(
        _check(
            "correspondence.selected_attestation_operation_identity",
            operation_corresponds,
            "UPSTREAM_CORRESPONDENCE_MISMATCH",
        )
    )
    if not operation_corresponds:
        return (
            "UPSTREAM_CORRESPONDENCE_MISMATCH",
            "selected attestation operation identity does not correspond",
            state,
        )

    candidate_corresponds = dict(boundary_candidate) == dict(
        attestation_candidate
    )
    state["selected_candidate_identity_corresponds"] = candidate_corresponds
    checks.append(
        _check(
            "correspondence.selected_candidate_identity",
            candidate_corresponds,
            "UPSTREAM_CORRESPONDENCE_MISMATCH",
        )
    )
    if not candidate_corresponds:
        return (
            "UPSTREAM_CORRESPONDENCE_MISMATCH",
            "selected candidate identity does not correspond",
            state,
        )

    result_corresponds = (
        boundary_operation.get(
            "selected_receiver_attestation_operation_result_required"
        )
        == attestation.get("operation_result")
        == SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
    )
    state["selected_attestation_result_corresponds"] = result_corresponds
    checks.append(
        _check(
            "correspondence.selected_attestation_result",
            result_corresponds,
            "UPSTREAM_CORRESPONDENCE_MISMATCH",
        )
    )
    if not result_corresponds:
        return (
            "UPSTREAM_CORRESPONDENCE_MISMATCH",
            "selected attestation result does not correspond",
            state,
        )

    path_corresponds = boundary.get(
        "selected_upstream_artifact_path"
    ) == str(SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH)
    state["selected_attestation_artifact_path_corresponds"] = path_corresponds
    checks.append(
        _check(
            "correspondence.selected_attestation_artifact_path",
            path_corresponds,
            "UPSTREAM_CORRESPONDENCE_MISMATCH",
        )
    )
    if not path_corresponds:
        return (
            "UPSTREAM_CORRESPONDENCE_MISMATCH",
            "selected attestation artifact path does not correspond",
            state,
        )

    exact_postures = {
        "boundary_allowed_validated": (
            boundary.get("boundary_allowed_validated") is True
        ),
        "attestation_recorded_validated": (
            attestation.get("receiver_attestation_recorded") is True
        ),
        "boundary_cardinality_validated": (
            boundary.get("completed_consideration_posture_count") == 1
            and boundary.get("boundary_cardinality_validated") is True
        ),
        "attestation_cardinality_validated": (
            attestation.get("completed_result_posture_count") == 1
        ),
        "operation_completion_and_exhaustion_validated": (
            boundary.get("boundary_completion_validated") is True
            and attestation.get("operation_completed_and_exhausted") is True
        ),
        "required_false_locks_correspond": (
            boundary.get("upstream_false_locks_validated") is True
            and attestation.get("upstream_false_locks_validated") is True
        ),
    }
    for field, valid in exact_postures.items():
        state[field] = valid
        checks.append(
            _check(
                "correspondence." + field,
                valid,
                "UPSTREAM_CORRESPONDENCE_MISMATCH",
            )
        )
        if not valid:
            return (
                "UPSTREAM_CORRESPONDENCE_MISMATCH",
                "upstream correspondence posture is invalid: " + field,
                state,
            )

    state["upstream_correspondence_validated"] = True
    return None, None, state


def _decision_for_request(
    request: Mapping[str, Any],
) -> tuple[str, str, str, str]:
    if (
        request["receipt_recording_ambiguity_present"] is True
        or request["receipt_recording_unresolved"] is True
    ):
        return (
            OUTCOME_INDETERMINATE,
            RESULT_INDETERMINATE,
            "RECEIVER_ANSWERABLE_RECEIPT_INDETERMINATE",
            "bounded receipt operation could not lawfully determine whether "
            "a receiver-answerable receipt should be recorded",
        )
    if (
        request["receipt_recording_contradiction_present"] is True
        or request["receiver_answerable_receipt_recording_selected"] is False
    ):
        return (
            OUTCOME_NOT_RECORDED,
            RESULT_NOT_RECORDED,
            "RECEIVER_ANSWERABLE_RECEIPT_NOT_RECORDED",
            "bounded receipt operation completed without recording a "
            "receiver-answerable receipt",
        )
    return (
        OUTCOME_RECORDED,
        RESULT_RECORDED,
        "RECEIVER_ANSWERABLE_RECEIPT_RECORDED",
        "exact allowed receipt boundary and exact recorded receiver "
        "attestation admitted and one receiver-answerable receipt recorded",
    )


def _branch_posture(outcome: str) -> dict[str, Any]:
    completed = outcome in {
        OUTCOME_RECORDED,
        OUTCOME_NOT_RECORDED,
        OUTCOME_INDETERMINATE,
    }
    recorded = outcome == OUTCOME_RECORDED
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    indeterminate = outcome == OUTCOME_INDETERMINATE
    return {
        "receiver_answerable_receipt_operation_recorded": completed,
        "receiver_answerable_receipt_operation_result_recorded": completed,
        "receiver_answerable_receipt_operation_exhausted": completed,
        "receiver_answerable_receipt_decided": completed,
        "receiver_answerable_receipt_recorded": recorded,
        "receiver_answerable_receipt_not_recorded": not_recorded,
        "receiver_answerable_receipt_indeterminate": indeterminate,
        "receiver_answerable_receipt_present": recorded,
        "completed_result_posture_count": 1 if completed else 0,
    }


def _operation_object(
    outcome: str,
    operation_result: str,
    atomic_basis: Mapping[str, Any],
    branch: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_id": (
            OPERATION_ID
        ),
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_type": (
            OPERATION_TYPE
        ),
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_version": (
            OPERATION_VERSION
        ),
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_scope": (
            OPERATION_SCOPE
        ),
        "upstream_receiver_answerable_receipt_boundary_id": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ID
        ),
        "upstream_receiver_answerable_receipt_boundary_type": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_TYPE
        ),
        "upstream_receiver_answerable_receipt_boundary_version": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_VERSION
        ),
        "upstream_receiver_answerable_receipt_boundary_scope": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_SCOPE
        ),
        "selected_receiver_attestation_operation_id": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
        ),
        "selected_receiver_attestation_operation_type": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
        ),
        "selected_receiver_attestation_operation_version": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
        ),
        "selected_receiver_attestation_operation_scope": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE
        ),
        "selected_receiver_attestation_operation_result_required": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "operation_basis_supplied": (
            atomic_basis.get("operation_basis_supplied") is True
        ),
        "operation_basis_admitted": (
            atomic_basis.get("operation_basis_admitted") is True
        ),
        "receiver_answerable_receipt_operation_result": operation_result,
        "originating_occurrence_created_by_source_body": False,
        **copy.deepcopy(dict(branch)),
        **_canonical_non_claims(),
    }


def _declared_request_posture(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "intent": request.get("intent"),
        **{
            field: copy.deepcopy(request.get(field))
            for field in _expected_request_values()
        },
        "declared_non_claims_validated": _non_claims_valid(
            request.get("declared_non_claims")
        ),
        "prohibited_request_flags_validated": all(
            request.get(field) is False for field in PROHIBITED_REQUEST_FLAGS
        ),
    }


def _operation_statement() -> dict[str, bool]:
    return {
        "occurrence_is_not_trace": True,
        "trace_is_not_candidate_reception": True,
        "candidate_sufficiency_is_not_receiver_attestation": True,
        "receiver_attestation_recorded_is_not_receipt": True,
        "receipt_consideration_allowed_is_not_receipt": True,
        "receipt_boundary_is_not_receipt_operation": True,
        "operation_request_is_not_operation_result": True,
        "operation_basis_admission_is_not_receipt": True,
        "receipt_recorded_is_not_independent_occurrence_verification": True,
        "receipt_recorded_is_not_identity_proof": True,
        "receipt_recorded_is_not_custody_proof": True,
        "receipt_recorded_is_not_provenance_proof": True,
        "receipt_recorded_is_not_physical_validity_proof": True,
        "receipt_is_not_presence": True,
        "operation_exhaustion_is_not_presence_re_evaluation": True,
        "completed_operation_is_not_downstream_authorization": True,
        "open_does_not_mean_next": True,
    }


def _operation_non_meaning(operation_result: str) -> dict[str, bool]:
    return {
        "operation_result_present": operation_result in COMPLETED_RESULT_FAMILY,
        "not_recorded_is_not_attestation_falsity": True,
        "not_recorded_is_not_receiver_dishonesty": True,
        "not_recorded_is_not_occurrence_denial": True,
        "not_recorded_is_not_candidate_insufficiency": True,
        "not_recorded_is_not_boundary_failure": True,
        "not_recorded_is_not_presence_denial": True,
        "not_recorded_is_not_refusal": True,
        "not_recorded_is_not_debt_or_obligation": True,
        "indeterminate_does_not_create_retry": True,
        "indeterminate_does_not_create_debt": True,
        "indeterminate_does_not_create_obligation": True,
        "indeterminate_does_not_create_scheduled_work": True,
        "indeterminate_does_not_create_automatic_next": True,
    }


def _empty_atomic_basis(
    request: Mapping[str, Any],
    *,
    supplied: bool | None = None,
) -> dict[str, bool]:
    return {
        "operation_basis_supplied": (
            _operation_basis_supplied(request)
            if supplied is None
            else supplied
        ),
        "operation_basis_admitted": False,
        "basis_admission_is_not_receipt": True,
    }


def _empty_decision(
    code: str | None,
    reason: str | None,
) -> dict[str, Any]:
    return {
        "decision_code": code,
        "decision_reason": reason,
        "decision_evaluated": False,
        "result_precedence": [
            RESULT_INDETERMINATE,
            RESULT_NOT_RECORDED,
            RESULT_RECORDED,
        ],
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation"
    )
    operation = operation if isinstance(operation, Mapping) else {}
    specification = result.get("specification_validation")
    specification = (
        specification if isinstance(specification, Mapping) else {}
    )
    boundary = result.get("receiver_answerable_receipt_boundary_validation")
    boundary = boundary if isinstance(boundary, Mapping) else {}
    attestation = result.get("receiver_attestation_operation_validation")
    attestation = attestation if isinstance(attestation, Mapping) else {}
    correspondence = result.get("upstream_correspondence_validation")
    correspondence = (
        correspondence if isinstance(correspondence, Mapping) else {}
    )
    atomic = result.get("atomic_operation_basis_posture")
    atomic = atomic if isinstance(atomic, Mapping) else {}
    decision = result.get("operation_decision")
    decision = decision if isinstance(decision, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    non_claims = result.get("non_claims")
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}
    omission = result.get("omission_posture")
    omission = omission if isinstance(omission, Mapping) else {}
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "operation_id": operation.get("operation_id"),
        "operation_type": operation.get("operation_type"),
        "operation_version": operation.get("operation_version"),
        "operation_scope": operation.get("operation_scope"),
        "specification_path": specification.get("specification_path"),
        "receipt_boundary_artifact_path": boundary.get("artifact_path"),
        "receiver_attestation_artifact_path": attestation.get("artifact_path"),
        "upstream_boundary_id": operation.get(
            "upstream_receiver_answerable_receipt_boundary_id"
        ),
        "selected_attestation_operation_id": operation.get(
            "selected_receiver_attestation_operation_id"
        ),
        "selected_candidate_id": operation.get(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "outcome": result.get("outcome"),
        "operation_result": result.get("operation_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": block.get("blocked"),
        "decision_code": decision.get("decision_code"),
        "decision_reason": decision.get("decision_reason"),
        "operation_basis_supplied": atomic.get("operation_basis_supplied"),
        "operation_basis_admitted": atomic.get("operation_basis_admitted"),
        "specification_validated": specification.get(
            "specification_validated"
        ),
        "receipt_boundary_artifact_validated": boundary.get(
            "artifact_validated"
        ),
        "receiver_attestation_artifact_validated": attestation.get(
            "artifact_validated"
        ),
        "upstream_correspondence_validated": correspondence.get(
            "upstream_correspondence_validated"
        ),
        "boundary_allowed_validated": correspondence.get(
            "boundary_allowed_validated"
        ),
        "attestation_recorded_validated": correspondence.get(
            "attestation_recorded_validated"
        ),
        "boundary_cardinality_validated": correspondence.get(
            "boundary_cardinality_validated"
        ),
        "attestation_cardinality_validated": correspondence.get(
            "attestation_cardinality_validated"
        ),
        "receiver_answerable_receipt_operation_recorded": operation.get(
            "receiver_answerable_receipt_operation_recorded"
        ),
        "receiver_answerable_receipt_operation_result_recorded": (
            operation.get(
                "receiver_answerable_receipt_operation_result_recorded"
            )
        ),
        "receiver_answerable_receipt_operation_exhausted": operation.get(
            "receiver_answerable_receipt_operation_exhausted"
        ),
        "receiver_answerable_receipt_decided": operation.get(
            "receiver_answerable_receipt_decided"
        ),
        "receiver_answerable_receipt_recorded": operation.get(
            "receiver_answerable_receipt_recorded"
        ),
        "receiver_answerable_receipt_not_recorded": operation.get(
            "receiver_answerable_receipt_not_recorded"
        ),
        "receiver_answerable_receipt_indeterminate": operation.get(
            "receiver_answerable_receipt_indeterminate"
        ),
        "receiver_answerable_receipt_present": operation.get(
            "receiver_answerable_receipt_present"
        ),
        "completed_result_posture_count": operation.get(
            "completed_result_posture_count"
        ),
        "receipt_support_absent": (
            non_claims.get("receiver_answerable_receipt_supported") is False
        ),
        "presence_re_evaluation_absent": (
            non_claims.get("presence_re_evaluation_boundary_created") is False
            and non_claims.get("presence_re_evaluation_operation_created")
            is False
        ),
        "presence_absent": all(
            non_claims.get(field) is False
            for field in (
                "presence_supported",
                "presence_authorized",
                "presence_established",
                "presence_recorded",
            )
        ),
        "identity_absent": non_claims.get("identity_created") is False,
        "custody_proof_absent": non_claims.get("custody_proven") is False,
        "provenance_proof_absent": (
            non_claims.get("provenance_proven") is False
        ),
        "physical_validity_proof_absent": (
            non_claims.get("physical_validity_proven") is False
        ),
        "downstream_non_claims_canonical_false": _non_claims_valid(non_claims),
        "result_level_non_claims_canonical_false": result.get(
            "result_level_non_claims_canonical_false"
        ),
        "complete_material_omission_posture": _omission_posture_valid(
            omission
        ),
        "admissible_future_route": result.get("admissible_future_route"),
    }


def _append_result_safety_checks(
    checks: list[dict[str, Any]],
    outcome: str,
    operation_result: str,
    branch: Mapping[str, Any],
) -> None:
    completed = outcome != OUTCOME_BLOCKED
    expected_count = 1 if completed else 0
    checks.append(
        _check(
            "result.completed_result_posture_count",
            branch.get("completed_result_posture_count") == expected_count,
            "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
        )
    )
    checks.append(
        _check(
            "result.operation_result_family",
            operation_result
            in (
                COMPLETED_RESULT_FAMILY
                if completed
                else (RESULT_NOT_EVALUATED,)
            ),
            "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
        )
    )
    expected_branch = _branch_posture(outcome)
    for field, expected in expected_branch.items():
        actual = branch.get(field)
        valid = (
            actual is expected
            if type(expected) is bool
            else type(actual) is int and actual == expected
        )
        checks.append(
            _check(
                "result.branch." + field,
                valid,
                "ATOMIC_OPERATION_BASIS_ADMISSION_FAILED",
            )
        )
    for field in REQUIRED_FALSE_NON_CLAIMS:
        checks.append(_check("result.non_claim." + field, True))
    for field in OMISSION_POSTURE_FIELDS:
        checks.append(_check("result.omission." + field, True))


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    operation_result: str,
    checks: list[dict[str, Any]],
    *,
    specification: Mapping[str, Any] | None = None,
    boundary: Mapping[str, Any] | None = None,
    attestation: Mapping[str, Any] | None = None,
    correspondence: Mapping[str, Any] | None = None,
    atomic_basis: Mapping[str, Any] | None = None,
    decision_code: str | None = None,
    decision_reason: str | None = None,
) -> dict[str, Any]:
    bounded_checks = copy.deepcopy(checks)
    bounded_specification = (
        copy.deepcopy(dict(specification))
        if isinstance(specification, Mapping)
        else _empty_specification_validation(request)
    )
    bounded_boundary = (
        copy.deepcopy(dict(boundary))
        if isinstance(boundary, Mapping)
        else _empty_boundary_validation(request)
    )
    bounded_attestation = (
        copy.deepcopy(dict(attestation))
        if isinstance(attestation, Mapping)
        else _empty_attestation_validation(request)
    )
    bounded_correspondence = (
        copy.deepcopy(dict(correspondence))
        if isinstance(correspondence, Mapping)
        else _empty_correspondence_validation()
    )
    bounded_atomic = (
        copy.deepcopy(dict(atomic_basis))
        if isinstance(atomic_basis, Mapping)
        else _empty_atomic_basis(request)
    )
    branch = _branch_posture(outcome)
    _append_result_safety_checks(
        bounded_checks, outcome, operation_result, branch
    )
    operation = _operation_object(
        outcome,
        operation_result,
        bounded_atomic,
        branch,
    )
    decision = {
        "decision_code": decision_code,
        "decision_reason": decision_reason,
        "decision_evaluated": outcome != OUTCOME_BLOCKED,
        "receiver_answerable_receipt_recording_selected": request.get(
            "receiver_answerable_receipt_recording_selected"
        ),
        "receipt_recording_ambiguity_present": request.get(
            "receipt_recording_ambiguity_present"
        ),
        "receipt_recording_contradiction_present": request.get(
            "receipt_recording_contradiction_present"
        ),
        "receipt_recording_unresolved": request.get(
            "receipt_recording_unresolved"
        ),
        "result_precedence": [
            RESULT_INDETERMINATE,
            RESULT_NOT_RECORDED,
            RESULT_RECORDED,
        ],
    }
    result: dict[str, Any] = {
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_metadata": {
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "specification_path": request.get(
                "governing_receiver_answerable_receipt_operation_specification_path"
            ),
            "receipt_boundary_artifact_path": request.get(
                "upstream_receiver_answerable_receipt_boundary_artifact_path"
            ),
            "receiver_attestation_operation_artifact_path": request.get(
                "selected_receiver_attestation_operation_artifact_path"
            ),
        },
        "declared_receiver_side_answerable_basis_receiver_answerable_receipt_operation_request": (
            _declared_request_posture(request)
        ),
        "selected_operation_and_candidate_identity": {
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "upstream_boundary_id": (
                UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ID
            ),
            "upstream_boundary_type": (
                UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_TYPE
            ),
            "upstream_boundary_version": (
                UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_VERSION
            ),
            "upstream_boundary_scope": (
                UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_SCOPE
            ),
            "selected_attestation_operation_id": (
                SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
            ),
            "selected_attestation_operation_type": (
                SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
            ),
            "selected_attestation_operation_version": (
                SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
            ),
            "selected_attestation_operation_scope": (
                SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE
            ),
            "selected_attestation_operation_result_required": (
                SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
            ),
            "selected_candidate_id": CANDIDATE_ID,
            "selected_candidate_type": CANDIDATE_TYPE,
            "selected_candidate_scope": CANDIDATE_SCOPE,
        },
        "specification_validation": bounded_specification,
        "receiver_answerable_receipt_boundary_validation": bounded_boundary,
        "receiver_attestation_operation_validation": bounded_attestation,
        "upstream_correspondence_validation": bounded_correspondence,
        "atomic_operation_basis_posture": bounded_atomic,
        "compact_upstream_standing": {
            "receipt_boundary": {
                "artifact_path": bounded_boundary.get("artifact_path"),
                "metadata": copy.deepcopy(
                    bounded_boundary.get("metadata", {})
                ),
                "boundary_identity": copy.deepcopy(
                    bounded_boundary.get("boundary_identity", {})
                ),
                "selected_operation_identity": copy.deepcopy(
                    bounded_boundary.get("selected_operation_identity", {})
                ),
                "selected_candidate_identity": copy.deepcopy(
                    bounded_boundary.get("selected_candidate_identity", {})
                ),
                "artifact_validated": bounded_boundary.get(
                    "artifact_validated"
                ),
            },
            "receiver_attestation": {
                "artifact_path": bounded_attestation.get("artifact_path"),
                "metadata": copy.deepcopy(
                    bounded_attestation.get("metadata", {})
                ),
                "operation_identity": copy.deepcopy(
                    bounded_attestation.get("operation_identity", {})
                ),
                "selected_candidate_identity": copy.deepcopy(
                    bounded_attestation.get(
                        "selected_candidate_identity", {}
                    )
                ),
                "operation_result": bounded_attestation.get(
                    "operation_result"
                ),
                "artifact_validated": bounded_attestation.get(
                    "artifact_validated"
                ),
            },
            "source_bodies_not_read": True,
            "complete_upstream_artifacts_omitted": True,
        },
        "operation_decision": decision,
        "operation_posture": {
            **copy.deepcopy(branch),
            "single_use_only": True,
            "operation_basis_supplied": bounded_atomic.get(
                "operation_basis_supplied"
            ),
            "operation_basis_admitted": bounded_atomic.get(
                "operation_basis_admitted"
            ),
            "originating_occurrence_created_by_source_body": False,
        },
        "operation_result_detail": {
            "operation_result": operation_result,
            "completed_result_posture_count": branch[
                "completed_result_posture_count"
            ],
            "result_precedence": [
                RESULT_INDETERMINATE,
                RESULT_NOT_RECORDED,
                RESULT_RECORDED,
            ],
        },
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation": (
            operation
        ),
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_checks": (
            bounded_checks
        ),
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_statement": (
            _operation_statement()
        ),
        "receiver_side_answerable_basis_receiver_answerable_receipt_operation_non_meaning": (
            _operation_non_meaning(operation_result)
        ),
        "omission_posture": _canonical_omission_posture(),
        "blocked_routes": list(BLOCKED_ROUTES),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "result_level_non_claims_canonical_false": True,
        "outcome": outcome,
        "operation_result": operation_result,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": decision_code if outcome == OUTCOME_BLOCKED else None,
            "block_code": (
                decision_code if outcome == OUTCOME_BLOCKED else None
            ),
            "reason": decision_reason if outcome == OUTCOME_BLOCKED else None,
        },
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "failed_check_count": sum(
            check.get("passed") is False for check in bounded_checks
        ),
        "passed_check_count": sum(
            check.get("passed") is True for check in bounded_checks
        ),
    }
    result[
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation_summary"
    ] = _summary_from_result(result)
    return result


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    *,
    specification: Mapping[str, Any] | None = None,
    boundary: Mapping[str, Any] | None = None,
    attestation: Mapping[str, Any] | None = None,
    correspondence: Mapping[str, Any] | None = None,
    atomic_basis: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        RESULT_NOT_EVALUATED,
        checks,
        specification=specification,
        boundary=boundary,
        attestation=attestation,
        correspondence=correspondence,
        atomic_basis=atomic_basis,
        decision_code=code,
        decision_reason=reason,
    )


def resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one exact receiver-answerable-receipt operation."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared_request = (
            build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_request()
        )
    elif not isinstance(request, Mapping):
        declared_request = (
            build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_request()
        )
        checks.append(
            _check("request.mapping", False, "REQUEST_NOT_MAPPING")
        )
        return _blocked_result(
            declared_request,
            checks,
            "REQUEST_NOT_MAPPING",
            "declared receipt-operation request is not a mapping",
            atomic_basis=_empty_atomic_basis(
                declared_request, supplied=False
            ),
        )
    else:
        declared_request = copy.deepcopy(dict(request))
        checks.append(_check("request.mapping", True))

    atomic_basis = _empty_atomic_basis(declared_request)
    code, reason = _validate_request(declared_request, checks)
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            reason or "request validation failed",
            atomic_basis=atomic_basis,
        )

    code, reason, specification = _validate_specification(
        declared_request, checks
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            reason or "specification validation failed",
            specification=specification,
            atomic_basis=atomic_basis,
        )

    code, reason, boundary = _validate_boundary_artifact(
        declared_request, checks
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            reason or "receipt-boundary validation failed",
            specification=specification,
            boundary=boundary,
            atomic_basis=atomic_basis,
        )

    code, reason, attestation = _validate_attestation_artifact(
        declared_request, checks
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            reason or "receiver-attestation validation failed",
            specification=specification,
            boundary=boundary,
            attestation=attestation,
            atomic_basis=atomic_basis,
        )

    code, reason, correspondence = _validate_correspondence(
        boundary, attestation, checks
    )
    if code is not None:
        return _blocked_result(
            declared_request,
            checks,
            code,
            reason or "upstream correspondence validation failed",
            specification=specification,
            boundary=boundary,
            attestation=attestation,
            correspondence=correspondence,
            atomic_basis=atomic_basis,
        )

    atomic_basis["operation_basis_admitted"] = True
    checks.append(_check("atomic_basis.operation_basis_supplied", True))
    checks.append(_check("atomic_basis.operation_basis_admitted", True))
    outcome, operation_result, decision_code, decision_reason = (
        _decision_for_request(declared_request)
    )
    return _build_result(
        declared_request,
        outcome,
        operation_result,
        checks,
        specification=specification,
        boundary=boundary,
        attestation=attestation,
        correspondence=correspondence,
        atomic_basis=atomic_basis,
        decision_code=decision_code,
        decision_reason=decision_reason,
    )


def resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Strictly load one explicit request path and resolve it."""
    try:
        path = Path(request_path)
    except (TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError(
            "REQUEST_PATH_INVALID: request path is invalid"
        ) from exc
    payload, error = _read_json(path)
    if error is not None:
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError(
            "REQUEST_PATH_INVALID: request JSON is unavailable, malformed, "
            "or duplicate-keyed"
        )
    if not isinstance(payload, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError(
            "REQUEST_PATH_INVALID: request JSON must contain one object"
        )
    return (
        resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min(
            payload
        )
    )


def build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic material-omitting summary."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    return _summary_from_result(result)


def _contains_prohibited_complete_material(value: Any) -> bool:
    forbidden_keys = {
        "complete_receipt_boundary_artifact",
        "receiver_answerable_receipt_boundary_artifact",
        "complete_receiver_attestation_operation_artifact",
        "receiver_attestation_operation_artifact",
        "complete_operation_basis",
        "complete_candidate_sufficiency_artifact",
        "candidate_sufficiency_artifact",
        "complete_candidate_sufficiency_basis",
        "candidate_sufficiency_basis",
        "sufficiency_basis_records",
        "complete_receiver_attestation_boundary_artifact",
        "receiver_attestation_boundary_artifact",
        "bounded_capture_package",
        "archive_bytes",
        "archive_body",
        "complete_archive",
        "hash_record_body",
        "text_component_bodies",
        "attestation_statement_body",
        "attestation_timestamp_body",
        "capture_method_body",
        "capture_only_statement_body",
        "freely_given_statement_body",
        "knock_reference_body",
        "receiver_label_body",
        "receiver_working_directory_body",
        "recorded_signal_body",
        "complete_signal_body",
        "signal_samples",
        "raw_signal_data",
    }
    if isinstance(value, Mapping):
        return any(
            key in forbidden_keys
            or _contains_prohibited_complete_material(nested)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        return any(
            _contains_prohibited_complete_material(item) for item in value
        )
    return isinstance(value, (bytes, bytearray))


def _branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    operation_result = result.get("operation_result")
    operation = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation"
    )
    posture = result.get("operation_posture")
    detail = result.get("operation_result_detail")
    atomic = result.get("atomic_operation_basis_posture")
    block = result.get("block")
    if (
        outcome not in OUTCOME_FAMILY
        or not isinstance(operation, Mapping)
        or not isinstance(posture, Mapping)
        or not isinstance(detail, Mapping)
        or not isinstance(atomic, Mapping)
        or not isinstance(block, Mapping)
    ):
        return False
    if (
        operation.get("operation_id") != OPERATION_ID
        or operation.get("operation_type") != OPERATION_TYPE
        or operation.get("operation_version") != OPERATION_VERSION
        or operation.get("operation_scope") != OPERATION_SCOPE
        or operation.get("receiver_answerable_receipt_operation_result")
        != operation_result
        or detail.get("operation_result") != operation_result
        or any(
            operation.get(field) is not False
            for field in REQUIRED_FALSE_NON_CLAIMS
        )
    ):
        return False

    completed = outcome != OUTCOME_BLOCKED
    expected = _branch_posture(outcome)
    if any(
        operation.get(field) != value
        or posture.get(field) != value
        for field, value in expected.items()
    ):
        return False
    if detail.get("completed_result_posture_count") != expected[
        "completed_result_posture_count"
    ]:
        return False
    if operation.get("operation_basis_supplied") is not (
        atomic.get("operation_basis_supplied") is True
    ):
        return False
    if operation.get("operation_basis_admitted") is not (
        atomic.get("operation_basis_admitted") is True
    ):
        return False

    if completed:
        expected_result = {
            OUTCOME_RECORDED: RESULT_RECORDED,
            OUTCOME_NOT_RECORDED: RESULT_NOT_RECORDED,
            OUTCOME_INDETERMINATE: RESULT_INDETERMINATE,
        }[outcome]
        return (
            operation_result == expected_result
            and atomic.get("operation_basis_supplied") is True
            and atomic.get("operation_basis_admitted") is True
            and block.get("blocked") is False
            and block.get("code") is None
            and block.get("block_code") is None
            and block.get("reason") is None
        )
    return (
        operation_result == RESULT_NOT_EVALUATED
        and atomic.get("operation_basis_admitted") is False
        and block.get("blocked") is True
        and block.get("code") in BLOCK_CODES
        and block.get("block_code") == block.get("code")
        and isinstance(block.get("reason"), str)
        and bool(block.get("reason"))
    )


def _checks_valid(result: Mapping[str, Any]) -> bool:
    checks = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation_checks"
    )
    if not isinstance(checks, list):
        return False
    if not all(
        isinstance(check, Mapping)
        and type(check.get("passed")) is bool
        for check in checks
    ):
        return False
    if any(
        check.get(field) not in BLOCK_CODES
        for check in checks
        for field in ("failure_code", "block_code")
        if field in check
    ):
        return False
    failed = result.get("failed_check_count")
    passed = result.get("passed_check_count")
    return (
        type(failed) is int
        and type(passed) is int
        and failed >= 0
        and passed >= 0
        and failed == sum(check.get("passed") is False for check in checks)
        and passed == sum(check.get("passed") is True for check in checks)
        and (
            (result.get("outcome") == OUTCOME_BLOCKED and failed > 0)
            or (result.get("outcome") != OUTCOME_BLOCKED and failed == 0)
        )
    )


def _result_valid_for_write(result: Mapping[str, Any]) -> bool:
    if (
        set(result) != RESULT_SECTIONS
        or result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
        or result.get("admissible_future_route") != ADMISSIBLE_FUTURE_ROUTE
        or not _non_claims_valid(result.get("non_claims"))
        or result.get("result_level_non_claims_canonical_false") is not True
        or not _omission_posture_valid(result.get("omission_posture"))
        or not _checks_valid(result)
        or not _branch_valid(result)
        or _contains_prohibited_complete_material(result)
    ):
        return False
    operation = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation"
    )
    summary = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation_summary"
    )
    metadata = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation_metadata"
    )
    identity = result.get("selected_operation_and_candidate_identity")
    specification = result.get("specification_validation")
    boundary = result.get(
        "receiver_answerable_receipt_boundary_validation"
    )
    attestation = result.get("receiver_attestation_operation_validation")
    correspondence = result.get("upstream_correspondence_validation")
    atomic = result.get("atomic_operation_basis_posture")
    decision = result.get("operation_decision")
    statement = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation_statement"
    )
    non_meaning = result.get(
        "receiver_side_answerable_basis_"
        "receiver_answerable_receipt_operation_non_meaning"
    )
    if not all(
        isinstance(value, Mapping)
        for value in (
            operation,
            summary,
            metadata,
            identity,
            specification,
            boundary,
            attestation,
            correspondence,
            atomic,
            decision,
            statement,
            non_meaning,
        )
    ):
        return False
    if (
        dict(summary) != _summary_from_result(result)
        or dict(statement) != _operation_statement()
        or dict(non_meaning)
        != _operation_non_meaning(str(result.get("operation_result")))
        or result.get("blocked_routes") != list(BLOCKED_ROUTES)
        or result.get("what_remains_open") != list(WHAT_REMAINS_OPEN)
    ):
        return False
    metadata_valid = (
        metadata.get("operation_id") == OPERATION_ID
        and metadata.get("operation_type") == OPERATION_TYPE
        and metadata.get("operation_version") == OPERATION_VERSION
        and metadata.get("operation_scope") == OPERATION_SCOPE
        and metadata.get("specification_path")
        == str(GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH)
        and metadata.get("receipt_boundary_artifact_path")
        == str(
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH
        )
        and metadata.get("receiver_attestation_operation_artifact_path")
        == str(
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
        )
    )
    identity_expectations = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "upstream_boundary_id": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ID
        ),
        "upstream_boundary_type": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_TYPE
        ),
        "upstream_boundary_version": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_VERSION
        ),
        "upstream_boundary_scope": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_SCOPE
        ),
        "selected_attestation_operation_id": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
        ),
        "selected_attestation_operation_type": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
        ),
        "selected_attestation_operation_version": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
        ),
        "selected_attestation_operation_scope": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE
        ),
        "selected_attestation_operation_result_required": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
        ),
        "selected_candidate_id": CANDIDATE_ID,
        "selected_candidate_type": CANDIDATE_TYPE,
        "selected_candidate_scope": CANDIDATE_SCOPE,
    }
    operation_expectations = {
        "upstream_receiver_answerable_receipt_boundary_id": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ID
        ),
        "upstream_receiver_answerable_receipt_boundary_type": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_TYPE
        ),
        "upstream_receiver_answerable_receipt_boundary_version": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_VERSION
        ),
        "upstream_receiver_answerable_receipt_boundary_scope": (
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_SCOPE
        ),
        "selected_receiver_attestation_operation_id": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
        ),
        "selected_receiver_attestation_operation_type": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
        ),
        "selected_receiver_attestation_operation_version": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
        ),
        "selected_receiver_attestation_operation_scope": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE
        ),
        "selected_receiver_attestation_operation_result_required": (
            SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "originating_occurrence_created_by_source_body": False,
    }
    paths_valid = (
        specification.get("specification_path")
        == str(GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH)
        and boundary.get("artifact_path")
        == str(
            UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH
        )
        and attestation.get("artifact_path")
        == str(
            SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
        )
    )
    outcome = result.get("outcome")
    expected_decision = {
        OUTCOME_RECORDED: (
            "RECEIVER_ANSWERABLE_RECEIPT_RECORDED",
            "exact allowed receipt boundary and exact recorded receiver "
            "attestation admitted and one receiver-answerable receipt "
            "recorded",
        ),
        OUTCOME_NOT_RECORDED: (
            "RECEIVER_ANSWERABLE_RECEIPT_NOT_RECORDED",
            "bounded receipt operation completed without recording a "
            "receiver-answerable receipt",
        ),
        OUTCOME_INDETERMINATE: (
            "RECEIVER_ANSWERABLE_RECEIPT_INDETERMINATE",
            "bounded receipt operation could not lawfully determine whether "
            "a receiver-answerable receipt should be recorded",
        ),
    }
    decision_valid = (
        decision.get("decision_evaluated") is (outcome != OUTCOME_BLOCKED)
        and (
            (
                outcome == OUTCOME_BLOCKED
                and decision.get("decision_code") in BLOCK_CODES
                and isinstance(decision.get("decision_reason"), str)
                and bool(decision.get("decision_reason"))
            )
            or (
                outcome in expected_decision
                and (
                    decision.get("decision_code"),
                    decision.get("decision_reason"),
                )
                == expected_decision[outcome]
            )
        )
    )
    completed = outcome != OUTCOME_BLOCKED
    completed_validation = (
        not completed
        or (
            specification.get("specification_validated") is True
            and boundary.get("artifact_validated") is True
            and attestation.get("artifact_validated") is True
            and correspondence.get("upstream_correspondence_validated")
            is True
            and atomic.get("operation_basis_supplied") is True
            and atomic.get("operation_basis_admitted") is True
        )
    )
    return (
        metadata_valid
        and paths_valid
        and decision_valid
        and completed_validation
        and all(identity.get(field) == expected for field, expected in identity_expectations.items())
        and all(operation.get(field) == expected for field, expected in operation_expectations.items())
    )


def _path_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _output_path_allowed(path: Path) -> bool:
    resolved = path.resolve()
    repo = REPO_ROOT.resolve()
    output_root = OUTPUT_ROOT.resolve()
    if _path_within(resolved, repo):
        return _path_within(resolved, output_root)
    protected_roots = (
        (repo / "reference").resolve(),
        (repo / "spec").resolve(),
        (repo / "src").resolve(),
        (repo / "tests").resolve(),
    )
    return not any(
        _path_within(resolved, root) for root in protected_roots
    )


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(
            path.stem + "_" + f"{index:03d}" + path.suffix
        )
        if not candidate.exists():
            return candidate
    raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def write_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid deterministic result without overwriting."""
    if not isinstance(result, Mapping) or not _result_valid_for_write(result):
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError(
            "WRITE_REFUSED: result is malformed or internally inconsistent"
        )
    try:
        target = (
            _as_repo_path(output_path)
            if output_path is not None
            else OUTPUT_ROOT / OUTPUT_FILENAME
        )
    except (TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError(
            "WRITE_REFUSED: output path is invalid"
        ) from exc
    if not _output_path_allowed(target):
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError(
            "WRITE_REFUSED: output path is protected or outside the "
            "receipt-operation output family"
        )
    if output_path is not None and target.exists():
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError(
            "WRITE_REFUSED: explicit output path already exists"
        )
    if output_path is None:
        target = _next_available_output_path(target)
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as handle:
            json.dump(
                dict(result),
                handle,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
