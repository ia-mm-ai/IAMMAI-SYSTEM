"""Resolve one bounded receiver-attestation basis preparation request.

The resolver records only whether preparation of one declaration candidate
was requested. It validates schema metadata and one exact waiting artifact;
it does not prepare, declare, supply, admit, or evaluate an operation basis.
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
    "resolve_receiver_side_answerable_basis_receiver_attestation_operation_"
    "basis_declaration_preparation_request_v0_min"
)

PREPARATION_REQUEST_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_request_001"
)
PREPARATION_REQUEST_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION_REQUEST"
)
PREPARATION_REQUEST_VERSION = "0.1.0"
PREPARATION_REQUEST_SCOPE = (
    "REQUEST_PREPARATION_OF_ONE_SOURCE_BODY_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_DECLARATION_CANDIDATE_ONLY"
)

REQUEST_ID = PREPARATION_REQUEST_ID
REQUEST_TYPE = PREPARATION_REQUEST_TYPE
REQUEST_VERSION = PREPARATION_REQUEST_VERSION
REQUEST_SCOPE = PREPARATION_REQUEST_SCOPE

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

OPERATION_ID = SELECTED_RECEIVER_ATTESTATION_OPERATION_ID
OPERATION_TYPE = SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE
OPERATION_VERSION = SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION
OPERATION_SCOPE = SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = (
    "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)
SELECTED_BOUNDARY_ID = (
    "receiver_side_answerable_basis_receiver_attestation_boundary_001"
)

WAITING_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min"
)
WAITING_RESULT_VERSION = "0.1.0"
WAITING_OUTCOME = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "REQUIRES_OPERATION_BASIS"
)

OUTCOME_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION_REQUEST_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION_REQUEST_NOT_RECORDED"
)
OUTCOME_BLOCKED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION_REQUEST_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_BLOCKED,
)

REQUEST_RESULT_RECORDED = (
    "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_"
    "PREPARATION_REQUEST_RECORDED"
)
REQUEST_RESULT_NOT_RECORDED = (
    "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_"
    "PREPARATION_REQUEST_NOT_RECORDED"
)
REQUEST_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
REQUEST_RESULT_FAMILY = (
    REQUEST_RESULT_RECORDED,
    REQUEST_RESULT_NOT_RECORDED,
    REQUEST_RESULT_NOT_EVALUATED,
)

INTENT_RECORD = (
    "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_DECLARATION_PREPARATION_REQUEST"
)
INTENT_BLOCK = (
    "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_DECLARATION_PREPARATION_REQUEST"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_DECLARATION_PREPARATION_REQUEST_V0_MIN_SPEC.md"
)
SELECTED_WAITING_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_001__"
    "receiver_side_answerable_basis_receiver_attestation_"
    "operation_v0_min_result.json"
)
SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_boundary_v0_min_v2/"
    "receiver_side_answerable_basis_receiver_attestation_boundary_001__"
    "receiver_side_answerable_basis_receiver_attestation_"
    "boundary_v0_min_v2_result.json"
)
BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH = Path(
    "artifacts/actual_receiver_attestation_capture/"
    "receiver_attestation_capture_001"
)
SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_candidate_sufficiency_operation_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_"
    "operation_v0_min_result_001.json"
)

GOVERNING_PREPARATION_REQUEST_SPECIFICATION_RELATIVE_PATH = (
    GOVERNING_SPECIFICATION_RELATIVE_PATH
)
SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH = (
    SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
)
GOVERNING_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
)
GOVERNING_PREPARATION_REQUEST_SPECIFICATION_PATH = (
    GOVERNING_SPECIFICATION_PATH
)
SELECTED_WAITING_ARTIFACT_PATH = (
    REPO_ROOT / SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
)
SELECTED_WAITING_OPERATION_ARTIFACT_PATH = SELECTED_WAITING_ARTIFACT_PATH

OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_declaration_"
    "preparation_request_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_request_001__receiver_side_answerable_basis_"
    "receiver_attestation_operation_basis_declaration_"
    "preparation_request_v0_min_result.json"
)

EXPECTED_ARCHIVE_SHA256 = (
    "a45a621c5c6c2f37daefd7e896f32cdb50bff21ab69ec9281912049bd326724c"
)

REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES = (
    "selected_receiver_attestation_boundary_artifact_path",
    "bounded_capture_directory_path",
    "preserved_archive_path",
    "archive_hash_record_path",
    "expected_archive_sha256",
    "attestation_statement_path",
    "attestation_timestamp_path",
    "capture_method_path",
    "capture_only_statement_path",
    "freely_given_statement_path",
    "knock_reference_path",
    "receiver_label_path",
    "receiver_working_directory_path",
    "recorded_signal_path",
    "evaluator_reference",
    "trace_integrity_postures",
    "ambiguity_postures",
    "contradiction_postures",
    "unresolved_postures",
    "non_conversion_statement",
    "basis_non_claims",
)
REQUESTED_OPERATION_BASIS_FIELD_NAMES = (
    REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES
)
REQUESTED_DECLARATION_CANDIDATE_FIELDS = (
    REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES
)
REQUEST_SELECTION_FIELD = "basis_declaration_preparation_selected"

BOUNDED_FUTURE_REFERENCES = MappingProxyType(
    {
        "selected_receiver_attestation_boundary_artifact_path": str(
            SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
        ),
        "bounded_capture_directory_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
        ),
        "preserved_archive_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "original_zip/receiver_attestation_001.zip"
        ),
        "archive_hash_record_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "hashes/receiver_attestation_001.sha256"
        ),
        "expected_archive_sha256": EXPECTED_ARCHIVE_SHA256,
        "attestation_statement_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/attestation_statement.txt"
        ),
        "attestation_timestamp_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/attested_at.txt"
        ),
        "capture_method_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/capture_method.txt"
        ),
        "capture_only_statement_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/capture_only_statement.txt"
        ),
        "freely_given_statement_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/freely_given_statement.txt"
        ),
        "knock_reference_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/knock_reference.txt"
        ),
        "receiver_label_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/receiver_label.txt"
        ),
        "receiver_working_directory_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/"
            "receiver_working_directory.txt"
        ),
        "recorded_signal_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/"
            "knock_20260727_215052.json"
        ),
    }
)
EXACT_BOUNDED_FUTURE_REFERENCES = BOUNDED_FUTURE_REFERENCES
BOUNDED_FUTURE_REFERENCE_FAMILY = BOUNDED_FUTURE_REFERENCES

TRACE_INTEGRITY_POSTURE_KEYS = (
    "exact_boundary_reference_preserved",
    "exact_capture_directory_reference_preserved",
    "exact_component_references_preserved",
    "archive_correspondence_claimed",
    "required_text_components_declared_complete",
    "recorded_signal_artifact_declared_present",
    "complete_archive_not_embedded",
    "complete_signal_body_not_embedded",
)
AMBIGUITY_POSTURE_KEYS = (
    "material_trace_ambiguity_present",
    "timestamp_interpretation_ambiguous",
    "component_correspondence_ambiguous",
)
CONTRADICTION_POSTURE_KEYS = (
    "material_trace_contradiction_present",
    "archive_correspondence_contradicted",
    "component_correspondence_contradicted",
)
UNRESOLVED_POSTURE_KEYS = (
    "trace_integrity_materially_unresolved",
    "archive_correspondence_materially_unresolved",
    "component_correspondence_materially_unresolved",
)

REQUESTED_POSTURE_KEY_FAMILIES = MappingProxyType(
    {
        "trace_integrity_postures": TRACE_INTEGRITY_POSTURE_KEYS,
        "ambiguity_postures": AMBIGUITY_POSTURE_KEYS,
        "contradiction_postures": CONTRADICTION_POSTURE_KEYS,
        "unresolved_postures": UNRESOLVED_POSTURE_KEYS,
    }
)
POSTURE_KEY_FAMILIES = REQUESTED_POSTURE_KEY_FAMILIES
REQUIRED_POSTURE_KEY_FAMILIES = REQUESTED_POSTURE_KEY_FAMILIES

CANONICAL_NON_CONVERSION_STATEMENT = (
    "bounded trace admission and recording do not establish occurrence "
    "creation, identity, independent custody, verified provenance, physical "
    "validity, current presence, receiver-answerable receipt, truth, "
    "authority, or standing."
)
NON_CONVERSION_STATEMENT = CANONICAL_NON_CONVERSION_STATEMENT

SPECIFICATION_SECTION_12_FALSE_NON_CLAIMS = (
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_attestation_recorded",
    "receiver_attestation_not_recorded",
    "receiver_attestation_indeterminate",
    "receiver_answerable_receipt_present",
    "receiver_answerable_receipt_boundary_created",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "presence_re_evaluation_boundary_created",
    "identity_created",
    "authority_created",
    "standing_created",
    "truth_created",
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
    "repeated_receiver_attestation_operation_basis_declaration_"
    "preparation_request_permission_created",
    "reusable_receiver_attestation_operation_basis_declaration_"
    "preparation_route_created",
    "same_receiver_attestation_operation_basis_declaration_"
    "preparation_request_rerun_authorized",
    "automatic_receiver_attestation_operation_basis_declaration_"
    "preparation_request_retry_created",
    "receiver_attestation_operation_basis_declaration_"
    "preparation_request_debt_created",
    "receiver_attestation_operation_basis_declaration_"
    "preparation_request_obligation_created",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

ADDITIONAL_EXACT_FALSE_NON_CLAIMS = (
    "basis_declaration_preparation_started",
    "basis_declaration_preparation_completed",
    "receiver_attestation_operation_basis_prepared",
    "receiver_attestation_operation_basis_declared",
    "receiver_attestation_operation_basis_supplied",
    "receiver_attestation_operation_basis_admitted",
)

REQUIRED_FALSE_NON_CLAIMS = (
    SPECIFICATION_SECTION_12_FALSE_NON_CLAIMS
    + ADDITIONAL_EXACT_FALSE_NON_CLAIMS
)
REQUEST_REQUIRED_FALSE_NON_CLAIMS = REQUIRED_FALSE_NON_CLAIMS

WAITING_REQUIRED_FALSE_NON_CLAIMS = (
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_answerable_receipt_present",
    "receiver_answerable_receipt_boundary_created",
    "presence_supported",
    "presence_authorized",
    "presence_established",
    "presence_recorded",
    "presence_re_evaluation_boundary_created",
    "identity_created",
    "authority_created",
    "standing_created",
    "truth_created",
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
    "repeated_receiver_attestation_operation_permission_created",
    "reusable_receiver_attestation_operation_route_created",
    "same_receiver_attestation_operation_rerun_authorized",
    "automatic_receiver_attestation_operation_retry_created",
    "receiver_attestation_operation_debt_created",
    "receiver_attestation_operation_obligation_created",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

PROHIBITED_REQUEST_FLAGS = MappingProxyType(
    {
        "request_preparation_started": (
            "PROHIBITED_PREPARATION_PERFORMANCE_REQUESTED"
        ),
        "request_preparation_completed": (
            "PROHIBITED_PREPARATION_PERFORMANCE_REQUESTED"
        ),
        "request_operation_basis_prepared": (
            "PROHIBITED_BASIS_STANDING_REQUESTED"
        ),
        "request_operation_basis_declared": (
            "PROHIBITED_BASIS_STANDING_REQUESTED"
        ),
        "request_operation_basis_supplied": (
            "PROHIBITED_OPERATION_SUPPLY_ADMISSION_OR_EXECUTION_REQUESTED"
        ),
        "request_operation_basis_admitted": (
            "PROHIBITED_OPERATION_SUPPLY_ADMISSION_OR_EXECUTION_REQUESTED"
        ),
        "request_receiver_attestation_operation_execution": (
            "PROHIBITED_OPERATION_SUPPLY_ADMISSION_OR_EXECUTION_REQUESTED"
        ),
        "request_receiver_attestation_operation_exhaustion": (
            "PROHIBITED_OPERATION_SUPPLY_ADMISSION_OR_EXECUTION_REQUESTED"
        ),
        "request_receiver_attestation_operation_result": (
            "PROHIBITED_OPERATION_RESULT_REQUESTED"
        ),
        "request_receiver_attestation_recording": (
            "PROHIBITED_ATTESTATION_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_receiver_answerable_receipt_creation": (
            "PROHIBITED_ATTESTATION_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_presence_support": (
            "PROHIBITED_ATTESTATION_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_presence_authorization": (
            "PROHIBITED_ATTESTATION_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_presence_establishment": (
            "PROHIBITED_ATTESTATION_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_presence_recording": (
            "PROHIBITED_ATTESTATION_RECEIPT_OR_PRESENCE_REQUESTED"
        ),
        "request_identity_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_authority_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_truth_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_standing_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_relation_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_coupling_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_field_machinery_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_runtime_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "request_api_creation": "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
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
        "request_repeated_preparation_request_permission_creation": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OBLIGATION_OR_SCHEDULING_REQUESTED"
        ),
        "request_reusable_preparation_route_creation": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OBLIGATION_OR_SCHEDULING_REQUESTED"
        ),
        "request_same_preparation_request_rerun": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OBLIGATION_OR_SCHEDULING_REQUESTED"
        ),
        "request_automatic_preparation_request_retry": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OBLIGATION_OR_SCHEDULING_REQUESTED"
        ),
        "request_preparation_request_debt_creation": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OBLIGATION_OR_SCHEDULING_REQUESTED"
        ),
        "request_preparation_request_obligation_creation": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OBLIGATION_OR_SCHEDULING_REQUESTED"
        ),
        "request_scheduled_preparation": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OBLIGATION_OR_SCHEDULING_REQUESTED"
        ),
        "request_automatic_next_step": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OBLIGATION_OR_SCHEDULING_REQUESTED"
        ),
        "request_affected_file_repair": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_repository_scan": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_file_discovery": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_validation_enforcement": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
        "request_prior_unsupported_claim_validation": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED"
        ),
    }
)

RESULT_PRECLAIM_FIELDS = frozenset(
    {
        "outcome",
        "request_result",
        "preparation_request_recorded",
        "preparation_request_result_recorded",
        "preparation_request_exhausted",
        "basis_declaration_preparation_requested",
        "basis_declaration_preparation_started",
        "basis_declaration_preparation_completed",
        "receiver_attestation_operation_basis_prepared",
        "receiver_attestation_operation_basis_declared",
        "receiver_attestation_operation_basis_supplied",
        "receiver_attestation_operation_basis_admitted",
        "receiver_attestation_operation_recorded",
        "receiver_attestation_operation_result_recorded",
        "receiver_attestation_operation_exhausted",
        "receiver_attestation_decided",
        "receiver_attestation_recorded",
        "receiver_attestation_not_recorded",
        "receiver_attestation_indeterminate",
        "receiver_attestation_operation_result",
        "operation_result",
    }
)

FORBIDDEN_PAYLOAD_KEYS = frozenset(
    {
        "receiver_attestation_operation_basis",
        "completed_receiver_attestation_operation_basis",
        "operation_basis",
        "prepared_operation_basis",
        "declared_operation_basis",
        "archive_bytes",
        "archive_body",
        "complete_archive",
        "source_body",
        "source_bodies",
        "raw_source_body",
        "hash_record_body",
        "attestation_statement",
        "attestation_statement_body",
        "attestation_timestamp",
        "attestation_timestamp_body",
        "capture_method",
        "capture_method_body",
        "capture_only_statement",
        "capture_only_statement_body",
        "freely_given_statement",
        "freely_given_statement_body",
        "knock_reference",
        "knock_reference_body",
        "receiver_label",
        "receiver_label_body",
        "receiver_working_directory",
        "receiver_working_directory_body",
        "recorded_signal",
        "recorded_signal_data",
        "complete_recorded_signal_data",
        "recorded_signal_body",
        "complete_signal_body",
        "complete_text_component_bodies",
        "text_component_bodies",
        "signal_samples",
        "raw_signal_data",
        "complete_waiting_artifact",
        "waiting_artifact",
        "complete_upstream_artifacts",
        "complete_upstream_boundary_artifact",
        "upstream_boundary_artifact",
        "complete_candidate_sufficiency_artifact",
        "candidate_sufficiency_artifact",
        "complete_candidate_sufficiency_basis",
        "candidate_sufficiency_basis",
        "completed_operation_basis_values",
        "basis_items",
        "basis_references",
        "evaluator_reference",
        "operation_result",
    }
)

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "REQUEST_OVERSIZED",
        "REQUEST_NESTING_EXCEEDED",
        "REQUEST_FIELD_MISSING",
        "REQUEST_FIELD_UNKNOWN",
        "UNSUPPORTED_INTENT",
        "EXPLICIT_BLOCK_REQUESTED",
        "REQUEST_VALUE_MISMATCH",
        "PREPARATION_REQUEST_IDENTITY_MISMATCH",
        "SELECTED_OPERATION_IDENTITY_MISMATCH",
        "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
        "GOVERNING_SPECIFICATION_PATH_MISMATCH",
        "WAITING_ARTIFACT_PATH_MISMATCH",
        "REQUESTED_DECLARATION_CANDIDATE_SCHEMA_MISMATCH",
        "BOUNDED_FUTURE_REFERENCE_FAMILY_MISMATCH",
        "REQUESTED_POSTURE_KEY_FAMILY_MISMATCH",
        "NON_CONVERSION_STATEMENT_MISMATCH",
        "REQUEST_SELECTION_NOT_BOOLEAN",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "RESULT_POSTURE_PRECLAIMED",
        "REQUEST_PAYLOAD_CONTAINS_COMPLETED_BASIS_OR_SOURCE_MATERIAL",
        "PROHIBITED_PREPARATION_PERFORMANCE_REQUESTED",
        "PROHIBITED_BASIS_STANDING_REQUESTED",
        "PROHIBITED_OPERATION_SUPPLY_ADMISSION_OR_EXECUTION_REQUESTED",
        "PROHIBITED_OPERATION_RESULT_REQUESTED",
        "PROHIBITED_ATTESTATION_RECEIPT_OR_PRESENCE_REQUESTED",
        "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "PROHIBITED_REPEAT_RETRY_DEBT_OBLIGATION_OR_SCHEDULING_REQUESTED",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "PREPARATION_REQUEST_SPECIFICATION_REFERENCE_MISSING",
        "PREPARATION_REQUEST_SPECIFICATION_MARKER_MISSING",
        "SELECTED_WAITING_ARTIFACT_REFERENCE_MISSING",
        "SELECTED_WAITING_ARTIFACT_NOT_PARSEABLE",
        "SELECTED_WAITING_ARTIFACT_NOT_MAPPING",
        "WAITING_ARTIFACT_METADATA_MISMATCH",
        "WAITING_ARTIFACT_FAILED_CHECKS_PRESENT",
        "WAITING_ARTIFACT_IDENTITY_MISMATCH",
        "WAITING_ARTIFACT_NOT_WAITING",
        "WAITING_ARTIFACT_OPERATION_RESULT_PRESENT",
        "WAITING_ARTIFACT_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
        "WAITING_ARTIFACT_BLOCKED",
        "WAITING_ARTIFACT_UPSTREAM_BOUNDARY_NOT_VALIDATED",
        "WAITING_ARTIFACT_OPERATION_ALREADY_RECORDED_DECIDED_OR_EXHAUSTED",
        "WAITING_ARTIFACT_NON_CLAIM_NOT_FALSE",
        "WAITING_ARTIFACT_OMISSION_POSTURE_INVALID",
        "WRITE_REFUSED",
    }
)

MAX_SERIALIZED_REQUEST_SIZE = 262_144
MAX_MAPPING_ITEMS = 256
MAX_SEQUENCE_ITEMS = 128
MAX_NESTING_DEPTH = 10
MAX_TEXT_LENGTH = 8_192

PREFIX = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_request"
)

PREPARATION_REQUEST_SPEC_MARKER_CLASSES = MappingProxyType(
    {
        "title": (
            "# Receiver-Side Answerable Basis Receiver Attestation Operation "
            "Basis Declaration Preparation Request V0 Minimum Specification",
        ),
        "preparation_request_identity": (
            PREPARATION_REQUEST_ID,
            PREPARATION_REQUEST_TYPE,
            PREPARATION_REQUEST_VERSION,
            PREPARATION_REQUEST_SCOPE,
        ),
        "selected_operation_and_candidate_identity": (
            OPERATION_ID,
            OPERATION_TYPE,
            OPERATION_SCOPE,
            CANDIDATE_ID,
            CANDIDATE_TYPE,
            CANDIDATE_SCOPE,
        ),
        "waiting_artifact_markers": (
            str(SELECTED_WAITING_ARTIFACT_RELATIVE_PATH),
            WAITING_OUTCOME,
        ),
        "requested_schema": REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES,
        "bounded_future_references": tuple(
            dict.fromkeys(BOUNDED_FUTURE_REFERENCES.values())
        ),
        "posture_key_families": (
            *tuple(REQUESTED_POSTURE_KEY_FAMILIES),
            *tuple(
                key
                for family in REQUESTED_POSTURE_KEY_FAMILIES.values()
                for key in family
            ),
        ),
        "non_conversion": (CANONICAL_NON_CONVERSION_STATEMENT,),
        "outcome_family": OUTCOME_FAMILY,
        "result_family": REQUEST_RESULT_FAMILY,
        "separation": (
            "request is not preparation completion;",
            "preparation is not declaration;",
            "declaration is not operation supply;",
            "operation supply is not basis admission;",
            "operation execution is not operation result;",
        ),
        "source_body_non_verification": (
            "Source-body preparation does not make the trace receiver-originating and does not independently verify the occurrence.",
        ),
        "recorded_request_non_performance": (
            "A recorded preparation request means only that one later bounded preparation act may be considered.",
            "It does not mean a preparer accepted the request, preparation began or completed",
        ),
        "exhaustion_non_authorization": (
            "Request exhaustion does not mean preparation has begun or completed",
            "another step is authorized",
        ),
        "open_not_next": ("Open does not mean next.",),
    }
)
SPECIFICATION_MARKER_CLASSES = PREPARATION_REQUEST_SPEC_MARKER_CLASSES

BLOCKED_ROUTES = (
    "waiting operation directly to prepared basis or basis declaration",
    "preparation request directly to preparation completion or basis standing",
    "preparation request directly to operation supply, admission, execution, exhaustion, or result",
    "capture-package existence directly to prepared or declared basis",
    "path or hash reference directly to provenance, identity, truth, presence, authority, or standing",
    "preparation request directly to receiver attestation, receipt, or presence",
    "completed request directly to repeat permission, reusable route, rerun, retry, debt, obligation, or scheduling",
    "preparation request directly to repair or contaminated-lineage validation",
)

PERMITTED_FUTURE_ROUTE = (
    "A separately bounded source-body preparation artifact may be considered only after a recorded request result.",
    "Any later preparation remains optional and separately selected.",
    "A prepared declaration remains separate from operation supply and admission.",
    "Only the receiver-attestation operation resolver may derive an operation result after separate basis supply.",
)

WHAT_REMAINS_OPEN = (
    "preparation-request test",
    "preparation-request live artifact",
    "source-body basis preparation",
    "basis declaration",
    "basis submission",
    "receiver-attestation operation execution with separately supplied basis",
    "receiver-attestation operation result",
    "receiver-answerable receipt",
    "presence re-evaluation",
    "identity",
    "authority",
    "truth",
    "standing",
    "relation",
    "coupling",
    "FIELD machinery",
    "runtime",
    "API",
    "output",
    "action",
    "synchronization",
    "follow-on work",
)

RESULT_SECTIONS = frozenset(
    {
        f"{PREFIX}_metadata",
        f"declared_{PREFIX}",
        "selected_request_operation_candidate_and_waiting_artifact_identity",
        "specification_marker_validation",
        "waiting_artifact_basis_and_validation",
        "requested_declaration_candidate_schema_validation",
        "bounded_future_reference_validation",
        "requested_posture_key_family_validation",
        "non_conversion_validation",
        "request_result_detail",
        PREFIX,
        f"{PREFIX}_checks",
        f"{PREFIX}_statement",
        f"{PREFIX}_non_meaning",
        "permitted_future_route",
        "blocked_routes",
        "what_remains_open",
        "non_claims",
        "outcome",
        "block",
        "resolver_module",
        "result_version",
        "failed_check_count",
        "passed_check_count",
        f"{PREFIX}_summary",
    }
)


class ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationRequestV0MinError(
    Exception
):
    """Raised when one bounded resolver result cannot be summarized or written."""


class _DuplicateJsonKeyError(ValueError):
    """Raised when a JSON object contains a duplicate member name."""


def _reject_duplicate_json_keys(
    pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKeyError(key)
        result[key] = value
    return result


def _exact_bool(value: Any) -> bool:
    return type(value) is bool


def _serialized_size(value: Any) -> int | None:
    try:
        rendered = json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=True,
            allow_nan=False,
        )
    except (TypeError, ValueError):
        return None
    return len(rendered.encode("utf-8"))


def _bounded_json(value: Any, depth: int = 0) -> bool:
    if depth > MAX_NESTING_DEPTH:
        return False
    if value is None or type(value) in (bool, int):
        return True
    if type(value) is float:
        return value == value and value not in (
            float("inf"),
            float("-inf"),
        )
    if isinstance(value, str):
        return len(value) <= MAX_TEXT_LENGTH
    if isinstance(value, Mapping):
        return len(value) <= MAX_MAPPING_ITEMS and all(
            isinstance(key, str)
            and len(key) <= MAX_TEXT_LENGTH
            and _bounded_json(nested, depth + 1)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(
        value,
        (str, bytes, bytearray),
    ):
        return len(value) <= MAX_SEQUENCE_ITEMS and all(
            _bounded_json(item, depth + 1) for item in value
        )
    return False


def _as_repo_path(value: Path | str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def _display_path(value: Path | str) -> str:
    path = _as_repo_path(value)
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


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


def _check(
    name: str,
    passed: bool,
    code: str | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {
        "check": name,
        "passed": bool(passed),
    }
    if not passed and code is not None:
        item["failure_code"] = code
        item["block_code"] = code
    return item


def _failure(
    checks: list[dict[str, Any]],
    name: str,
    code: str,
) -> tuple[str, str]:
    checks.append(_check(name, False, code))
    return code, name.replace("_", " ")


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _non_claims_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_FALSE_NON_CLAIMS)
        and all(
            value.get(field) is False
            for field in REQUIRED_FALSE_NON_CLAIMS
        )
    )


def _required_fields_false(value: Any, fields: Sequence[str]) -> bool:
    return (
        isinstance(value, Mapping)
        and all(value.get(field) is False for field in fields)
    )


def _waiting_non_claims_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(WAITING_REQUIRED_FALSE_NON_CLAIMS)
        and all(
            value.get(field) is False
            for field in WAITING_REQUIRED_FALSE_NON_CLAIMS
        )
    )


def _canonical_bounded_future_references() -> dict[str, str]:
    return dict(BOUNDED_FUTURE_REFERENCES)


def _canonical_requested_posture_key_families() -> dict[str, list[str]]:
    return {
        family: list(keys)
        for family, keys in REQUESTED_POSTURE_KEY_FAMILIES.items()
    }


def _expected_request_values() -> dict[str, Any]:
    return {
        "preparation_request_id": PREPARATION_REQUEST_ID,
        "preparation_request_type": PREPARATION_REQUEST_TYPE,
        "preparation_request_version": PREPARATION_REQUEST_VERSION,
        "preparation_request_scope": PREPARATION_REQUEST_SCOPE,
        "selected_receiver_attestation_operation_id": OPERATION_ID,
        "selected_receiver_attestation_operation_type": OPERATION_TYPE,
        "selected_receiver_attestation_operation_version": OPERATION_VERSION,
        "selected_receiver_attestation_operation_scope": OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "governing_preparation_request_specification_path": str(
            GOVERNING_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_waiting_operation_artifact_path": str(
            SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
        ),
    }


def _request_allowed_keys() -> frozenset[str]:
    return frozenset(
        {
            "intent",
            "basis_declaration_preparation_selected",
            "requested_declaration_candidate_field_names",
            "bounded_future_references",
            "requested_posture_key_families",
            "requested_non_conversion_statement",
            "declared_non_claims",
            *tuple(_expected_request_values()),
            *tuple(PROHIBITED_REQUEST_FLAGS),
        }
    )


def _contains_key(value: Any, keys: frozenset[str]) -> bool:
    if isinstance(value, Mapping):
        return any(
            key in keys or _contains_key(nested, keys)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(
        value,
        (str, bytes, bytearray),
    ):
        return any(_contains_key(item, keys) for item in value)
    return isinstance(value, (bytes, bytearray))


def _marker_status(text: str) -> dict[str, bool]:
    return {
        marker_class: all(marker in text for marker in markers)
        for marker_class, markers in PREPARATION_REQUEST_SPEC_MARKER_CLASSES.items()
    }


def build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_request(
    *,
    intent: str = INTENT_RECORD,
    basis_declaration_preparation_selected: bool = True,
    requested_declaration_candidate_field_names: Sequence[str] | None = None,
    bounded_future_references: Mapping[str, Any] | None = None,
    requested_posture_key_families: Mapping[str, Any] | None = None,
    requested_non_conversion_statement: str = (
        CANONICAL_NON_CONVERSION_STATEMENT
    ),
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one canonical schema-only preparation request."""
    request: dict[str, Any] = {
        "intent": intent,
        **_expected_request_values(),
        "requested_declaration_candidate_field_names": copy.deepcopy(
            list(REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES)
            if requested_declaration_candidate_field_names is None
            else requested_declaration_candidate_field_names
        ),
        "bounded_future_references": copy.deepcopy(
            _canonical_bounded_future_references()
            if bounded_future_references is None
            else bounded_future_references
        ),
        "requested_posture_key_families": copy.deepcopy(
            _canonical_requested_posture_key_families()
            if requested_posture_key_families is None
            else requested_posture_key_families
        ),
        "requested_non_conversion_statement": (
            requested_non_conversion_statement
        ),
        "basis_declaration_preparation_selected": (
            basis_declaration_preparation_selected
        ),
        "declared_non_claims": copy.deepcopy(
            _canonical_non_claims()
            if declared_non_claims is None
            else declared_non_claims
        ),
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_request(
    *,
    basis_declaration_preparation_selected: bool = True,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one exact declared request while retaining bounded overrides."""
    return build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_request(
        basis_declaration_preparation_selected=(
            basis_declaration_preparation_selected
        ),
        **overrides,
    )


def _identity_failure_code(field: str) -> str:
    if field.startswith("preparation_request_"):
        return "PREPARATION_REQUEST_IDENTITY_MISMATCH"
    if "selected_receiver_attestation_operation_" in field:
        return "SELECTED_OPERATION_IDENTITY_MISMATCH"
    if "candidate_" in field:
        return "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
    if field == "governing_preparation_request_specification_path":
        return "GOVERNING_SPECIFICATION_PATH_MISMATCH"
    if field == "selected_waiting_operation_artifact_path":
        return "WAITING_ARTIFACT_PATH_MISMATCH"
    return "REQUEST_VALUE_MISMATCH"


def _validate_requested_schema(value: Any) -> bool:
    return (
        isinstance(value, Sequence)
        and not isinstance(value, (str, bytes, bytearray))
        and tuple(value) == REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES
    )


def _validate_bounded_future_references(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(BOUNDED_FUTURE_REFERENCES)
        and all(
            value.get(field) == expected
            for field, expected in BOUNDED_FUTURE_REFERENCES.items()
        )
    )


def _validate_requested_posture_key_families(value: Any) -> bool:
    if (
        not isinstance(value, Mapping)
        or set(value) != set(REQUESTED_POSTURE_KEY_FAMILIES)
    ):
        return False
    for family, expected in REQUESTED_POSTURE_KEY_FAMILIES.items():
        supplied = value.get(family)
        if (
            not isinstance(supplied, Sequence)
            or isinstance(supplied, (str, bytes, bytearray))
            or tuple(supplied) != expected
            or any(not isinstance(item, str) for item in supplied)
        ):
            return False
    return True


def _validate_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    size = _serialized_size(request)
    if size is None or size > MAX_SERIALIZED_REQUEST_SIZE:
        return _failure(
            checks,
            "request_within_bounded_size",
            "REQUEST_OVERSIZED",
        )
    if not _bounded_json(request):
        return _failure(
            checks,
            "request_within_bounded_nesting",
            "REQUEST_NESTING_EXCEEDED",
        )

    allowed = _request_allowed_keys()
    missing = allowed - set(request)
    if missing:
        return _failure(
            checks,
            "request_contains_every_canonical_field",
            "REQUEST_FIELD_MISSING",
        )
    unknown = set(request) - allowed
    if unknown:
        return _failure(
            checks,
            "request_contains_no_unknown_field",
            "REQUEST_FIELD_UNKNOWN",
        )

    for field in RESULT_PRECLAIM_FIELDS:
        if field in request:
            return _failure(
                checks,
                f"{field}_not_preclaimed",
                "RESULT_POSTURE_PRECLAIMED",
            )

    if _contains_key(request, FORBIDDEN_PAYLOAD_KEYS):
        return _failure(
            checks,
            "request_contains_no_completed_basis_or_source_material",
            "REQUEST_PAYLOAD_CONTAINS_COMPLETED_BASIS_OR_SOURCE_MATERIAL",
        )

    intent = request.get("intent")
    if intent not in SUPPORTED_INTENTS:
        return _failure(
            checks,
            "intent_supported",
            "UNSUPPORTED_INTENT",
        )
    if intent == INTENT_BLOCK:
        return _failure(
            checks,
            "explicit_block_not_requested",
            "EXPLICIT_BLOCK_REQUESTED",
        )

    for field, expected in _expected_request_values().items():
        if request.get(field) != expected:
            return _failure(
                checks,
                f"{field}_matches",
                _identity_failure_code(field),
            )
    checks.append(_check("request_identity_and_paths_exact", True))

    if not _validate_requested_schema(
        request.get("requested_declaration_candidate_field_names")
    ):
        return _failure(
            checks,
            "requested_declaration_candidate_schema_exact",
            "REQUESTED_DECLARATION_CANDIDATE_SCHEMA_MISMATCH",
        )
    checks.append(_check("requested_declaration_candidate_schema_exact", True))

    if not _validate_bounded_future_references(
        request.get("bounded_future_references")
    ):
        return _failure(
            checks,
            "bounded_future_reference_family_exact",
            "BOUNDED_FUTURE_REFERENCE_FAMILY_MISMATCH",
        )
    checks.append(_check("bounded_future_reference_family_exact", True))

    if not _validate_requested_posture_key_families(
        request.get("requested_posture_key_families")
    ):
        return _failure(
            checks,
            "requested_posture_key_families_exact",
            "REQUESTED_POSTURE_KEY_FAMILY_MISMATCH",
        )
    checks.append(_check("requested_posture_key_families_exact", True))

    if (
        request.get("requested_non_conversion_statement")
        != CANONICAL_NON_CONVERSION_STATEMENT
    ):
        return _failure(
            checks,
            "requested_non_conversion_statement_exact",
            "NON_CONVERSION_STATEMENT_MISMATCH",
        )
    checks.append(_check("requested_non_conversion_statement_exact", True))

    if not _exact_bool(
        request.get("basis_declaration_preparation_selected")
    ):
        return _failure(
            checks,
            "basis_declaration_preparation_selected_boolean",
            "REQUEST_SELECTION_NOT_BOOLEAN",
        )
    checks.append(_check("basis_declaration_preparation_selected_boolean", True))

    if not _non_claims_valid(request.get("declared_non_claims")):
        return _failure(
            checks,
            "declared_non_claims_canonical_false",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    checks.append(_check("declared_non_claims_canonical_false", True))

    for field, block_code in PROHIBITED_REQUEST_FLAGS.items():
        value = request.get(field)
        if value is True:
            return _failure(
                checks,
                f"{field}_not_requested",
                block_code,
            )
        if value is not False:
            return _failure(
                checks,
                f"{field}_exact_false",
                "REQUEST_VALUE_MISMATCH",
            )
    checks.append(_check("prohibited_request_flags_exact_false", True))
    checks.append(_check("request_shape_bounded_and_exact", True))
    return None, None


def _validate_specification(
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], str | None, str | None]:
    validation: dict[str, Any] = {
        "governing_specification_path": str(
            GOVERNING_SPECIFICATION_RELATIVE_PATH
        ),
        "marker_status": {},
        "specification_markers_validated": False,
        "complete_specification_body_omitted": True,
    }
    text, error = _read_text(GOVERNING_SPECIFICATION_RELATIVE_PATH)
    if error is not None or text is None:
        code, reason = _failure(
            checks,
            "preparation_request_specification_exists",
            "PREPARATION_REQUEST_SPECIFICATION_REFERENCE_MISSING",
        )
        return validation, code, reason
    markers = _marker_status(text)
    validation["marker_status"] = markers
    if not all(markers.values()):
        code, reason = _failure(
            checks,
            "preparation_request_specification_markers_exact",
            "PREPARATION_REQUEST_SPECIFICATION_MARKER_MISSING",
        )
        return validation, code, reason
    validation["specification_markers_validated"] = True
    checks.append(_check("preparation_request_specification_markers_exact", True))
    return validation, None, None


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _validate_waiting_artifact(
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], str | None, str | None]:
    validation: dict[str, Any] = {
        "selected_waiting_artifact_path": str(
            SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
        ),
        "waiting_artifact_validated": False,
        "waiting_artifact_identity": {
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "candidate_id": CANDIDATE_ID,
            "candidate_type": CANDIDATE_TYPE,
            "candidate_scope": CANDIDATE_SCOPE,
            "boundary_id": SELECTED_BOUNDARY_ID,
        },
        "waiting_artifact_metadata": {},
        "waiting_posture_validation": {},
        "result_level_non_claims_canonical_false": False,
        "complete_waiting_artifact_omitted": True,
        "complete_waiting_checks_omitted": True,
        "complete_upstream_boundary_artifact_omitted": True,
        "complete_candidate_sufficiency_artifact_omitted": True,
        "complete_candidate_sufficiency_basis_omitted": True,
        "complete_operation_basis_omitted": True,
        "archive_bytes_omitted": True,
        "text_component_bodies_omitted": True,
        "recorded_signal_body_omitted": True,
    }
    artifact, error = _read_json(SELECTED_WAITING_ARTIFACT_RELATIVE_PATH)
    if error in ("not_a_file", "unreadable"):
        code, reason = _failure(
            checks,
            "selected_waiting_artifact_exists",
            "SELECTED_WAITING_ARTIFACT_REFERENCE_MISSING",
        )
        return validation, code, reason
    if error is not None:
        code, reason = _failure(
            checks,
            "selected_waiting_artifact_parseable",
            "SELECTED_WAITING_ARTIFACT_NOT_PARSEABLE",
        )
        return validation, code, reason
    if not isinstance(artifact, Mapping):
        code, reason = _failure(
            checks,
            "selected_waiting_artifact_mapping",
            "SELECTED_WAITING_ARTIFACT_NOT_MAPPING",
        )
        return validation, code, reason

    operation = _mapping(
        artifact.get(
            "receiver_side_answerable_basis_receiver_attestation_operation"
        )
    )
    summary = _mapping(
        artifact.get(
            "receiver_side_answerable_basis_receiver_attestation_operation_summary"
        )
    )
    selected = _mapping(
        artifact.get("selected_operation_and_candidate_identity")
    )
    basis = _mapping(
        artifact.get("supplied_operation_basis_admission_metadata")
    )
    block = _mapping(artifact.get("block"))
    component = _mapping(artifact.get("bounded_component_validation"))
    upstream = _mapping(artifact.get("upstream_boundary_basis"))
    detail = _mapping(artifact.get("operation_result_detail"))

    if (
        artifact.get("resolver_module") != WAITING_RESOLVER_MODULE
        or artifact.get("result_version") != WAITING_RESULT_VERSION
    ):
        code, reason = _failure(
            checks,
            "waiting_artifact_metadata_exact",
            "WAITING_ARTIFACT_METADATA_MISMATCH",
        )
        return validation, code, reason
    if (
        type(artifact.get("failed_check_count")) is not int
        or artifact.get("failed_check_count") != 0
    ):
        code, reason = _failure(
            checks,
            "waiting_artifact_failed_check_count_zero",
            "WAITING_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
        return validation, code, reason
    checks.append(_check("waiting_artifact_metadata_exact", True))

    operation_identity = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "receiver_side_answerable_basis_receiver_attestation_operation_id": (
            OPERATION_ID
        ),
        "receiver_side_answerable_basis_receiver_attestation_operation_type": (
            OPERATION_TYPE
        ),
        "receiver_side_answerable_basis_receiver_attestation_operation_version": (
            OPERATION_VERSION
        ),
        "receiver_side_answerable_basis_receiver_attestation_operation_scope": (
            OPERATION_SCOPE
        ),
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_receiver_attestation_boundary_id": SELECTED_BOUNDARY_ID,
    }
    selected_identity = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "selected_candidate_id": CANDIDATE_ID,
        "selected_candidate_type": CANDIDATE_TYPE,
        "selected_candidate_scope": CANDIDATE_SCOPE,
        "selected_boundary_id": SELECTED_BOUNDARY_ID,
    }
    if (
        not operation
        or not selected
        or any(
            operation.get(field) != expected
            for field, expected in operation_identity.items()
        )
        or any(
            selected.get(field) != expected
            for field, expected in selected_identity.items()
        )
    ):
        code, reason = _failure(
            checks,
            "waiting_artifact_identity_exact",
            "WAITING_ARTIFACT_IDENTITY_MISMATCH",
        )
        return validation, code, reason
    checks.append(_check("waiting_artifact_identity_exact", True))

    if artifact.get("outcome") != WAITING_OUTCOME:
        code, reason = _failure(
            checks,
            "waiting_artifact_outcome_exact",
            "WAITING_ARTIFACT_NOT_WAITING",
        )
        return validation, code, reason
    if (
        "receiver_attestation_operation_result" not in operation
        or "operation_result" not in summary
        or "operation_result" not in detail
        or operation.get("receiver_attestation_operation_result") is not None
        or summary.get("operation_result") is not None
        or detail.get("operation_result") is not None
    ):
        code, reason = _failure(
            checks,
            "waiting_artifact_operation_result_null",
            "WAITING_ARTIFACT_OPERATION_RESULT_PRESENT",
        )
        return validation, code, reason
    checks.append(_check("waiting_artifact_outcome_and_null_result_exact", True))

    if (
        basis.get("basis_supplied") is not False
        or basis.get("basis_admitted") is not False
        or operation.get("operation_basis_supplied") is not False
        or operation.get("operation_basis_admitted") is not False
        or summary.get("basis_supplied") is not False
        or summary.get("basis_admitted") is not False
    ):
        code, reason = _failure(
            checks,
            "waiting_artifact_basis_absent",
            "WAITING_ARTIFACT_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
        )
        return validation, code, reason
    checks.append(_check("waiting_artifact_basis_absent", True))

    if (
        block.get("blocked") is not False
        or block.get("code") is not None
        or block.get("block_code") is not None
        or block.get("reason") is not None
        or summary.get("blocked") is not False
    ):
        code, reason = _failure(
            checks,
            "waiting_artifact_not_blocked",
            "WAITING_ARTIFACT_BLOCKED",
        )
        return validation, code, reason
    checks.append(_check("waiting_artifact_not_blocked", True))

    if (
        summary.get("upstream_boundary_validated") is not True
        or upstream.get("upstream_boundary_validated") is not True
        or operation.get(
            "selected_receiver_attestation_boundary_validated"
        )
        is not True
    ):
        code, reason = _failure(
            checks,
            "waiting_artifact_upstream_boundary_validated",
            "WAITING_ARTIFACT_UPSTREAM_BOUNDARY_NOT_VALIDATED",
        )
        return validation, code, reason
    checks.append(_check("waiting_artifact_upstream_boundary_validated", True))

    operation_false_fields = (
        "receiver_attestation_operation_recorded",
        "receiver_attestation_operation_result_recorded",
        "receiver_attestation_operation_exhausted",
        "receiver_attestation_decided",
        "receiver_attestation_recorded",
        "receiver_attestation_not_recorded",
        "receiver_attestation_indeterminate",
    )
    if any(operation.get(field) is not False for field in operation_false_fields):
        code, reason = _failure(
            checks,
            "waiting_artifact_operation_unrecorded_undecided_unexhausted",
            "WAITING_ARTIFACT_OPERATION_ALREADY_RECORDED_DECIDED_OR_EXHAUSTED",
        )
        return validation, code, reason
    summary_false_fields = (
        "receiver_attestation_operation_recorded",
        "receiver_attestation_operation_exhausted",
        "receiver_attestation_recorded",
        "receiver_attestation_not_recorded",
        "receiver_attestation_indeterminate",
    )
    if any(summary.get(field) is not False for field in summary_false_fields):
        code, reason = _failure(
            checks,
            "waiting_artifact_summary_operation_posture_false",
            "WAITING_ARTIFACT_OPERATION_ALREADY_RECORDED_DECIDED_OR_EXHAUSTED",
        )
        return validation, code, reason
    checks.append(
        _check(
            "waiting_artifact_operation_unrecorded_undecided_unexhausted",
            True,
        )
    )

    if (
        not _waiting_non_claims_valid(artifact.get("non_claims"))
        or any(
            operation.get(field) is not False
            for field in WAITING_REQUIRED_FALSE_NON_CLAIMS
        )
        or summary.get("result_level_non_claims_canonical_false") is not True
    ):
        code, reason = _failure(
            checks,
            "waiting_artifact_non_claims_exact_false",
            "WAITING_ARTIFACT_NON_CLAIM_NOT_FALSE",
        )
        return validation, code, reason
    checks.append(_check("waiting_artifact_non_claims_exact_false", True))

    omission_expectations = {
        "complete_upstream_boundary_artifact_omitted": (
            summary.get("complete_upstream_boundary_artifact_omitted")
        ),
        "complete_candidate_sufficiency_artifact_omitted": (
            summary.get("complete_candidate_sufficiency_artifact_omitted")
        ),
        "complete_candidate_sufficiency_basis_omitted": (
            summary.get("complete_candidate_sufficiency_basis_omitted")
        ),
        "complete_operation_basis_omitted": (
            summary.get("complete_operation_basis_omitted")
        ),
        "archive_bytes_omitted": summary.get("archive_bytes_omitted"),
        "text_component_bodies_omitted": summary.get(
            "text_component_bodies_omitted"
        ),
        "recorded_signal_body_omitted": summary.get(
            "recorded_signal_body_omitted"
        ),
    }
    if (
        any(value is not True for value in omission_expectations.values())
        or basis.get("complete_operation_basis_omitted") is not True
        or component.get("archive_bytes_omitted") is not True
        or component.get("text_component_bodies_omitted") is not True
        or component.get("recorded_signal_body_omitted") is not True
    ):
        code, reason = _failure(
            checks,
            "waiting_artifact_complete_material_omitted",
            "WAITING_ARTIFACT_OMISSION_POSTURE_INVALID",
        )
        return validation, code, reason
    checks.append(_check("waiting_artifact_complete_material_omitted", True))

    validation.update(
        {
            "waiting_artifact_validated": True,
            "waiting_artifact_metadata": {
                "resolver_module": artifact.get("resolver_module"),
                "result_version": artifact.get("result_version"),
                "outcome": artifact.get("outcome"),
                "failed_check_count": artifact.get("failed_check_count"),
                "passed_check_count": artifact.get("passed_check_count"),
            },
            "waiting_posture_validation": {
                "operation_result_null": True,
                "basis_supplied": False,
                "basis_admitted": False,
                "blocked": False,
                "upstream_boundary_validated": True,
                "operation_recorded": False,
                "operation_result_recorded": False,
                "operation_exhausted": False,
                "receiver_attestation_decided": False,
                "receiver_attestation_recorded": False,
                "receiver_attestation_not_recorded": False,
                "receiver_attestation_indeterminate": False,
            },
            "result_level_non_claims_canonical_false": True,
        }
    )
    return validation, None, None


def _safe_declared_request(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    schema_valid = _validate_requested_schema(
        request.get("requested_declaration_candidate_field_names")
    )
    references_valid = _validate_bounded_future_references(
        request.get("bounded_future_references")
    )
    postures_valid = _validate_requested_posture_key_families(
        request.get("requested_posture_key_families")
    )
    non_conversion_valid = (
        request.get("requested_non_conversion_statement")
        == CANONICAL_NON_CONVERSION_STATEMENT
    )
    selection = request.get("basis_declaration_preparation_selected")
    return {
        "intent": (
            request.get("intent")
            if request.get("intent") in SUPPORTED_INTENTS
            else None
        ),
        **_expected_request_values(),
        "basis_declaration_preparation_selected": (
            selection if _exact_bool(selection) else None
        ),
        "requested_declaration_candidate_field_names": (
            list(REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES)
            if schema_valid
            else []
        ),
        "bounded_future_references": (
            _canonical_bounded_future_references()
            if references_valid
            else {}
        ),
        "requested_posture_key_families": (
            _canonical_requested_posture_key_families()
            if postures_valid
            else {}
        ),
        "requested_non_conversion_statement": (
            CANONICAL_NON_CONVERSION_STATEMENT
            if non_conversion_valid
            else None
        ),
        "declared_non_claims_canonical_false": _non_claims_valid(
            request.get("declared_non_claims")
        ),
        "prohibited_request_flags_canonical_false": all(
            request.get(field) is False
            for field in PROHIBITED_REQUEST_FLAGS
        ),
        "complete_request_payload_omitted": True,
        "completed_operation_basis_omitted": True,
        "source_bodies_omitted": True,
    }


def _state(
    outcome: str,
    request_result: str,
    request: Mapping[str, Any],
    specification_validation: Mapping[str, Any],
    waiting_validation: Mapping[str, Any],
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    completed = recorded or not_recorded
    selection = request.get("basis_declaration_preparation_selected")
    selection_value = selection if _exact_bool(selection) else False
    schema_validated = _validate_requested_schema(
        request.get("requested_declaration_candidate_field_names")
    )
    references_validated = _validate_bounded_future_references(
        request.get("bounded_future_references")
    )
    posture_keys_validated = _validate_requested_posture_key_families(
        request.get("requested_posture_key_families")
    )
    non_conversion_validated = (
        request.get("requested_non_conversion_statement")
        == CANONICAL_NON_CONVERSION_STATEMENT
    )
    state: dict[str, Any] = {
        "preparation_request_id": PREPARATION_REQUEST_ID,
        "preparation_request_type": PREPARATION_REQUEST_TYPE,
        "preparation_request_version": PREPARATION_REQUEST_VERSION,
        "preparation_request_scope": PREPARATION_REQUEST_SCOPE,
        "selected_receiver_attestation_operation_id": OPERATION_ID,
        "selected_receiver_attestation_operation_type": OPERATION_TYPE,
        "selected_receiver_attestation_operation_version": OPERATION_VERSION,
        "selected_receiver_attestation_operation_scope": OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_waiting_operation_artifact_path": str(
            SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
        ),
        "request_result": request_result,
        "basis_declaration_preparation_selected": selection_value,
        "specification_markers_validated": (
            specification_validation.get(
                "specification_markers_validated"
            )
            is True
        ),
        "waiting_artifact_validated": (
            waiting_validation.get("waiting_artifact_validated") is True
        ),
        "requested_declaration_candidate_schema_validated": (
            schema_validated
        ),
        "bounded_future_references_validated": references_validated,
        "requested_posture_key_families_validated": (
            posture_keys_validated
        ),
        "non_conversion_statement_validated": non_conversion_validated,
        "preparation_request_recorded": recorded,
        "preparation_request_result_recorded": completed,
        "preparation_request_exhausted": completed,
        "basis_declaration_preparation_requested": recorded,
        "basis_declaration_preparation_started": False,
        "basis_declaration_preparation_completed": False,
        "receiver_attestation_operation_basis_prepared": False,
        "receiver_attestation_operation_basis_declared": False,
        "receiver_attestation_operation_basis_supplied": False,
        "receiver_attestation_operation_basis_admitted": False,
        "receiver_attestation_operation_recorded": False,
        "receiver_attestation_operation_result_recorded": False,
        "receiver_attestation_operation_exhausted": False,
        "receiver_attestation_decided": False,
        "receiver_attestation_recorded": False,
        "receiver_attestation_not_recorded": False,
        "receiver_attestation_indeterminate": False,
        "complete_waiting_artifact_omitted": True,
        "complete_upstream_boundary_artifact_omitted": True,
        "complete_candidate_sufficiency_artifact_omitted": True,
        "complete_candidate_sufficiency_basis_omitted": True,
        "complete_operation_basis_omitted": True,
        "archive_bytes_omitted": True,
        "text_component_bodies_omitted": True,
        "recorded_signal_body_omitted": True,
    }
    state.update(_canonical_non_claims())
    return state


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    state = _mapping(result.get(PREFIX))
    waiting = _mapping(result.get("waiting_artifact_basis_and_validation"))
    specification = _mapping(result.get("specification_marker_validation"))
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "preparation_request_id": state.get("preparation_request_id"),
        "preparation_request_type": state.get("preparation_request_type"),
        "preparation_request_version": state.get(
            "preparation_request_version"
        ),
        "preparation_request_scope": state.get("preparation_request_scope"),
        "selected_operation_id": state.get(
            "selected_receiver_attestation_operation_id"
        ),
        "selected_candidate_id": state.get(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "selected_waiting_artifact_path": state.get(
            "selected_waiting_operation_artifact_path"
        ),
        "outcome": result.get("outcome"),
        "request_result": state.get("request_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": _mapping(result.get("block")).get("blocked"),
        "request_selection": state.get(
            "basis_declaration_preparation_selected"
        ),
        "specification_markers_validated": specification.get(
            "specification_markers_validated"
        ),
        "waiting_artifact_validated": waiting.get(
            "waiting_artifact_validated"
        ),
        "requested_21_field_schema_validated": state.get(
            "requested_declaration_candidate_schema_validated"
        ),
        "bounded_future_references_validated": state.get(
            "bounded_future_references_validated"
        ),
        "posture_key_families_validated": state.get(
            "requested_posture_key_families_validated"
        ),
        "non_conversion_statement_validated": state.get(
            "non_conversion_statement_validated"
        ),
        "preparation_request_recorded": state.get(
            "preparation_request_recorded"
        ),
        "preparation_request_result_recorded": state.get(
            "preparation_request_result_recorded"
        ),
        "preparation_request_exhausted": state.get(
            "preparation_request_exhausted"
        ),
        "basis_declaration_preparation_requested": state.get(
            "basis_declaration_preparation_requested"
        ),
        "basis_declaration_preparation_started": state.get(
            "basis_declaration_preparation_started"
        ),
        "basis_declaration_preparation_completed": state.get(
            "basis_declaration_preparation_completed"
        ),
        "receiver_attestation_operation_basis_prepared": state.get(
            "receiver_attestation_operation_basis_prepared"
        ),
        "receiver_attestation_operation_basis_declared": state.get(
            "receiver_attestation_operation_basis_declared"
        ),
        "receiver_attestation_operation_basis_supplied": state.get(
            "receiver_attestation_operation_basis_supplied"
        ),
        "receiver_attestation_operation_basis_admitted": state.get(
            "receiver_attestation_operation_basis_admitted"
        ),
        "receiver_attestation_operation_recorded": state.get(
            "receiver_attestation_operation_recorded"
        ),
        "receiver_attestation_operation_result_recorded": state.get(
            "receiver_attestation_operation_result_recorded"
        ),
        "receiver_attestation_operation_exhausted": state.get(
            "receiver_attestation_operation_exhausted"
        ),
        "receiver_attestation_decided": state.get(
            "receiver_attestation_decided"
        ),
        "receiver_attestation_recorded": state.get(
            "receiver_attestation_recorded"
        ),
        "receiver_attestation_not_recorded": state.get(
            "receiver_attestation_not_recorded"
        ),
        "receiver_attestation_indeterminate": state.get(
            "receiver_attestation_indeterminate"
        ),
        "result_level_non_claims_canonical_false": _non_claims_valid(
            result.get("non_claims")
        ),
        "complete_material_omitted": all(
            state.get(field) is True
            for field in (
                "complete_waiting_artifact_omitted",
                "complete_upstream_boundary_artifact_omitted",
                "complete_candidate_sufficiency_artifact_omitted",
                "complete_candidate_sufficiency_basis_omitted",
                "complete_operation_basis_omitted",
                "archive_bytes_omitted",
                "text_component_bodies_omitted",
                "recorded_signal_body_omitted",
            )
        ),
        "governing_paths": {
            "governing_preparation_request_specification_path": str(
                GOVERNING_SPECIFICATION_RELATIVE_PATH
            ),
            "selected_waiting_operation_artifact_path": str(
                SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
            ),
        },
    }


def _result(
    request: Mapping[str, Any],
    outcome: str,
    request_result: str,
    checks: list[dict[str, Any]],
    *,
    specification_validation: Mapping[str, Any] | None = None,
    waiting_validation: Mapping[str, Any] | None = None,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    specification = copy.deepcopy(dict(specification_validation or {}))
    waiting = copy.deepcopy(dict(waiting_validation or {}))
    state = _state(
        outcome,
        request_result,
        request,
        specification,
        waiting,
    )
    selected = request.get("basis_declaration_preparation_selected")
    selected_value = selected if _exact_bool(selected) else None
    schema_validated = _validate_requested_schema(
        request.get("requested_declaration_candidate_field_names")
    )
    references_validated = _validate_bounded_future_references(
        request.get("bounded_future_references")
    )
    posture_keys_validated = _validate_requested_posture_key_families(
        request.get("requested_posture_key_families")
    )
    non_conversion_validated = (
        request.get("requested_non_conversion_statement")
        == CANONICAL_NON_CONVERSION_STATEMENT
    )
    result: dict[str, Any] = {
        f"{PREFIX}_metadata": {
            "preparation_request_id": PREPARATION_REQUEST_ID,
            "preparation_request_type": PREPARATION_REQUEST_TYPE,
            "preparation_request_version": PREPARATION_REQUEST_VERSION,
            "preparation_request_scope": PREPARATION_REQUEST_SCOPE,
        },
        f"declared_{PREFIX}": _safe_declared_request(request),
        "selected_request_operation_candidate_and_waiting_artifact_identity": {
            "preparation_request_id": PREPARATION_REQUEST_ID,
            "preparation_request_type": PREPARATION_REQUEST_TYPE,
            "preparation_request_version": PREPARATION_REQUEST_VERSION,
            "preparation_request_scope": PREPARATION_REQUEST_SCOPE,
            "selected_operation_id": OPERATION_ID,
            "selected_operation_type": OPERATION_TYPE,
            "selected_operation_version": OPERATION_VERSION,
            "selected_operation_scope": OPERATION_SCOPE,
            "selected_candidate_id": CANDIDATE_ID,
            "selected_candidate_type": CANDIDATE_TYPE,
            "selected_candidate_scope": CANDIDATE_SCOPE,
            "selected_waiting_artifact_path": str(
                SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
            ),
        },
        "specification_marker_validation": specification,
        "waiting_artifact_basis_and_validation": waiting,
        "requested_declaration_candidate_schema_validation": {
            "requested_field_count": len(
                REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES
            ),
            "requested_field_names": list(
                REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES
            ),
            "schema_validated": schema_validated,
            "schema_metadata_only": True,
            "completed_operation_basis_values_supplied": False,
        },
        "bounded_future_reference_validation": {
            "bounded_future_references": (
                _canonical_bounded_future_references()
                if references_validated
                else {}
            ),
            "bounded_future_references_validated": references_validated,
            "capture_file_existence_validated": False,
            "archive_hash_computed": False,
            "timestamp_parsed": False,
            "recorded_signal_inspected": False,
            "references_are_schema_metadata_only": True,
        },
        "requested_posture_key_family_validation": {
            "requested_posture_key_families": (
                _canonical_requested_posture_key_families()
                if posture_keys_validated
                else {}
            ),
            "posture_key_families_validated": posture_keys_validated,
            "completed_boolean_posture_values_supplied": False,
        },
        "non_conversion_validation": {
            "requested_non_conversion_statement": (
                CANONICAL_NON_CONVERSION_STATEMENT
                if non_conversion_validated
                else None
            ),
            "non_conversion_statement_validated": non_conversion_validated,
            "operation_basis_declared": False,
        },
        "request_result_detail": {
            "request_result": request_result,
            "basis_declaration_preparation_selected": selected_value,
            "preparation_request_recorded": state[
                "preparation_request_recorded"
            ],
            "preparation_request_result_recorded": state[
                "preparation_request_result_recorded"
            ],
            "preparation_request_exhausted": state[
                "preparation_request_exhausted"
            ],
            "basis_declaration_preparation_requested": state[
                "basis_declaration_preparation_requested"
            ],
            "basis_declaration_preparation_started": False,
            "basis_declaration_preparation_completed": False,
            "operation_basis_prepared": False,
            "operation_basis_declared": False,
            "operation_basis_supplied": False,
            "operation_basis_admitted": False,
            "receiver_attestation_operation_executed": False,
            "receiver_attestation_operation_result_exists": False,
        },
        PREFIX: state,
        f"{PREFIX}_checks": copy.deepcopy(checks),
        f"{PREFIX}_statement": {
            "one_waiting_operation_consumed_as_upstream_standing": (
                waiting.get("waiting_artifact_validated") is True
            ),
            "request_records_request_posture_only": True,
            "request_is_not_preparation_completion": True,
            "preparation_is_not_declaration": True,
            "declaration_is_not_operation_supply": True,
            "operation_supply_is_not_operation_result": True,
            "source_body_preparation_is_not_independent_verification": True,
            "request_exhaustion_is_not_preparation_completion": True,
            "request_exhaustion_is_not_next_step_authorization": True,
            "open_does_not_mean_next": True,
        },
        f"{PREFIX}_non_meaning": {
            "recorded_request_is_not_preparer_acceptance": True,
            "recorded_request_is_not_preparation_started": True,
            "recorded_request_is_not_preparation_completed": True,
            "recorded_request_is_not_basis_prepared": True,
            "recorded_request_is_not_basis_declared": True,
            "recorded_request_is_not_basis_supplied": True,
            "recorded_request_is_not_basis_admitted": True,
            "recorded_request_is_not_operation_execution": True,
            "recorded_request_is_not_operation_result": True,
            "recorded_request_is_not_receiver_attestation": True,
            "recorded_request_is_not_receiver_answerable_receipt": True,
            "recorded_request_is_not_presence_identity_authority_truth_or_standing": True,
            "not_recorded_is_not_preparer_refusal_or_preparation_failure": True,
            "not_recorded_is_not_basis_invalidity": True,
            "not_recorded_is_not_receiver_attestation_failure": True,
            "not_recorded_is_not_candidate_insufficiency": True,
        },
        "permitted_future_route": list(PERMITTED_FUTURE_ROUTE),
        "blocked_routes": list(BLOCKED_ROUTES),
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
    result["failed_check_count"] = sum(
        check.get("passed") is False for check in checks
    )
    result["passed_check_count"] = sum(
        check.get("passed") is True for check in checks
    )
    result[f"{PREFIX}_summary"] = _summary_from_result(result)
    return result


def resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one request decision without performing preparation."""
    if request is None:
        working: Mapping[str, Any] = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_request()
        )
    elif not isinstance(request, Mapping):
        baseline = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_request()
        )
        checks = [_check("request_is_mapping", False, "REQUEST_NOT_MAPPING")]
        return _result(
            baseline,
            OUTCOME_BLOCKED,
            REQUEST_RESULT_NOT_EVALUATED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="request is not a mapping",
        )
    else:
        working = copy.deepcopy(dict(request))

    checks: list[dict[str, Any]] = []
    code, reason = _validate_request(working, checks)
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            REQUEST_RESULT_NOT_EVALUATED,
            checks,
            code=code,
            reason=reason,
        )

    specification, code, reason = _validate_specification(checks)
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            REQUEST_RESULT_NOT_EVALUATED,
            checks,
            specification_validation=specification,
            code=code,
            reason=reason,
        )

    waiting, code, reason = _validate_waiting_artifact(checks)
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            REQUEST_RESULT_NOT_EVALUATED,
            checks,
            specification_validation=specification,
            waiting_validation=waiting,
            code=code,
            reason=reason,
        )

    if working.get("basis_declaration_preparation_selected") is False:
        checks.append(_check("preparation_request_selection_not_recorded", True))
        return _result(
            working,
            OUTCOME_NOT_RECORDED,
            REQUEST_RESULT_NOT_RECORDED,
            checks,
            specification_validation=specification,
            waiting_validation=waiting,
        )

    checks.append(_check("preparation_request_recorded_without_performance", True))
    return _result(
        working,
        OUTCOME_RECORDED,
        REQUEST_RESULT_RECORDED,
        checks,
        specification_validation=specification,
        waiting_validation=waiting,
    )


def resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Read one explicit JSON path without discovery and resolve it."""
    value, error = _read_json(request_path)
    if error is not None or not isinstance(value, Mapping):
        baseline = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_request()
        )
        checks = [
            _check(
                "request_path_is_mapping_json",
                False,
                "REQUEST_NOT_MAPPING",
            )
        ]
        return _result(
            baseline,
            OUTCOME_BLOCKED,
            REQUEST_RESULT_NOT_EVALUATED,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason=(
                "request path is unavailable, duplicated, unparseable, "
                "or not a mapping"
            ),
        )
    return resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min(
        value
    )


def build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic summary."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationRequestV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    return _summary_from_result(result)


def _branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    state = _mapping(result.get(PREFIX))
    block = _mapping(result.get("block"))
    metadata = _mapping(result.get(f"{PREFIX}_metadata"))
    detail = _mapping(result.get("request_result_detail"))
    identity = _mapping(
        result.get(
            "selected_request_operation_candidate_and_waiting_artifact_identity"
        )
    )
    omission_fields = (
        "complete_waiting_artifact_omitted",
        "complete_upstream_boundary_artifact_omitted",
        "complete_candidate_sufficiency_artifact_omitted",
        "complete_candidate_sufficiency_basis_omitted",
        "complete_operation_basis_omitted",
        "archive_bytes_omitted",
        "text_component_bodies_omitted",
        "recorded_signal_body_omitted",
    )
    detail_false_fields = (
        "basis_declaration_preparation_started",
        "basis_declaration_preparation_completed",
        "operation_basis_prepared",
        "operation_basis_declared",
        "operation_basis_supplied",
        "operation_basis_admitted",
        "receiver_attestation_operation_executed",
        "receiver_attestation_operation_result_exists",
    )
    if (
        outcome not in OUTCOME_FAMILY
        or metadata
        != {
            "preparation_request_id": PREPARATION_REQUEST_ID,
            "preparation_request_type": PREPARATION_REQUEST_TYPE,
            "preparation_request_version": PREPARATION_REQUEST_VERSION,
            "preparation_request_scope": PREPARATION_REQUEST_SCOPE,
        }
        or state.get("preparation_request_id") != PREPARATION_REQUEST_ID
        or state.get("preparation_request_type") != PREPARATION_REQUEST_TYPE
        or state.get("preparation_request_version") != PREPARATION_REQUEST_VERSION
        or state.get("preparation_request_scope") != PREPARATION_REQUEST_SCOPE
        or state.get("selected_receiver_attestation_operation_id")
        != OPERATION_ID
        or state.get("selected_receiver_attestation_operation_type")
        != OPERATION_TYPE
        or state.get("selected_receiver_attestation_operation_version")
        != OPERATION_VERSION
        or state.get("selected_receiver_attestation_operation_scope")
        != OPERATION_SCOPE
        or state.get("receiver_side_answerable_basis_candidate_id")
        != CANDIDATE_ID
        or state.get("receiver_side_answerable_basis_candidate_type")
        != CANDIDATE_TYPE
        or state.get("receiver_side_answerable_basis_candidate_scope")
        != CANDIDATE_SCOPE
        or identity.get("preparation_request_id") != PREPARATION_REQUEST_ID
        or identity.get("selected_operation_id") != OPERATION_ID
        or identity.get("selected_candidate_id") != CANDIDATE_ID
        or identity.get("selected_waiting_artifact_path")
        != str(SELECTED_WAITING_ARTIFACT_RELATIVE_PATH)
        or any(
            state.get(field) is not False
            for field in (
                "basis_declaration_preparation_started",
                "basis_declaration_preparation_completed",
                "receiver_attestation_operation_basis_prepared",
                "receiver_attestation_operation_basis_declared",
                "receiver_attestation_operation_basis_supplied",
                "receiver_attestation_operation_basis_admitted",
                "receiver_attestation_operation_recorded",
                "receiver_attestation_operation_result_recorded",
                "receiver_attestation_operation_exhausted",
                "receiver_attestation_decided",
                "receiver_attestation_recorded",
                "receiver_attestation_not_recorded",
                "receiver_attestation_indeterminate",
            )
        )
        or not _required_fields_false(state, REQUIRED_FALSE_NON_CLAIMS)
        or any(state.get(field) is not True for field in omission_fields)
        or any(detail.get(field) is not False for field in detail_false_fields)
        or detail.get("request_result") != state.get("request_result")
        or detail.get("preparation_request_recorded")
        is not state.get("preparation_request_recorded")
        or detail.get("preparation_request_result_recorded")
        is not state.get("preparation_request_result_recorded")
        or detail.get("preparation_request_exhausted")
        is not state.get("preparation_request_exhausted")
        or detail.get("basis_declaration_preparation_requested")
        is not state.get("basis_declaration_preparation_requested")
    ):
        return False

    nonblocked_validation = (
        state.get("specification_markers_validated") is True
        and state.get("waiting_artifact_validated") is True
        and state.get(
            "requested_declaration_candidate_schema_validated"
        )
        is True
        and state.get("bounded_future_references_validated") is True
        and state.get("requested_posture_key_families_validated") is True
        and state.get("non_conversion_statement_validated") is True
        and _mapping(
            result.get("specification_marker_validation")
        ).get("specification_markers_validated")
        is True
        and _mapping(
            result.get("waiting_artifact_basis_and_validation")
        ).get("waiting_artifact_validated")
        is True
        and _mapping(
            result.get(
                "requested_declaration_candidate_schema_validation"
            )
        ).get("schema_validated")
        is True
        and _mapping(
            result.get("bounded_future_reference_validation")
        ).get("bounded_future_references_validated")
        is True
        and _mapping(
            result.get("requested_posture_key_family_validation")
        ).get("posture_key_families_validated")
        is True
        and _mapping(
            result.get("non_conversion_validation")
        ).get("non_conversion_statement_validated")
        is True
    )
    clean_block = (
        block.get("blocked") is False
        and block.get("code") is None
        and block.get("block_code") is None
        and block.get("reason") is None
    )
    if outcome == OUTCOME_RECORDED:
        return (
            clean_block
            and nonblocked_validation
            and state.get("request_result") == REQUEST_RESULT_RECORDED
            and state.get("basis_declaration_preparation_selected") is True
            and state.get("preparation_request_recorded") is True
            and state.get("preparation_request_result_recorded") is True
            and state.get("preparation_request_exhausted") is True
            and state.get("basis_declaration_preparation_requested") is True
            and state.get("specification_markers_validated") is True
            and state.get("waiting_artifact_validated") is True
        )
    if outcome == OUTCOME_NOT_RECORDED:
        return (
            clean_block
            and nonblocked_validation
            and state.get("request_result") == REQUEST_RESULT_NOT_RECORDED
            and state.get("basis_declaration_preparation_selected") is False
            and state.get("preparation_request_recorded") is False
            and state.get("preparation_request_result_recorded") is True
            and state.get("preparation_request_exhausted") is True
            and state.get("basis_declaration_preparation_requested") is False
            and state.get("specification_markers_validated") is True
            and state.get("waiting_artifact_validated") is True
        )
    return (
        state.get("request_result") == REQUEST_RESULT_NOT_EVALUATED
        and state.get("preparation_request_recorded") is False
        and state.get("preparation_request_result_recorded") is False
        and state.get("preparation_request_exhausted") is False
        and state.get("basis_declaration_preparation_requested") is False
        and block.get("blocked") is True
        and block.get("code") in BLOCK_CODES
        and block.get("block_code") == block.get("code")
        and isinstance(block.get("reason"), str)
        and bool(block.get("reason"))
    )


def _contains_forbidden_result_material(value: Any) -> bool:
    forbidden = FORBIDDEN_PAYLOAD_KEYS | {
        "declared_non_claims",
        "complete_specification_body",
        "complete_waiting_artifact_checks",
    }
    return _contains_key(value, forbidden)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(
            f"{path.stem}_{index:03d}{path.suffix}"
        )
        if not candidate.exists():
            return candidate
    raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationRequestV0MinError(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def _path_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _output_path_is_forbidden(path: Path) -> bool:
    resolved = path.resolve(strict=False)
    protected_roots = (
        (REPO_ROOT / "reference").resolve(strict=False),
        (REPO_ROOT / "spec").resolve(strict=False),
        (REPO_ROOT / "src").resolve(strict=False),
        (REPO_ROOT / "tests").resolve(strict=False),
        (
            REPO_ROOT / SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
        ).parent.resolve(strict=False),
        (
            REPO_ROOT / SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
        ).parent.resolve(strict=False),
        (
            REPO_ROOT / SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
        ).parent.resolve(strict=False),
        (
            REPO_ROOT / BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
        ).resolve(strict=False),
    )
    return any(_path_within(resolved, root) for root in protected_roots)


def _validate_write_result(result: Mapping[str, Any]) -> None:
    error = (
        ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationRequestV0MinError
    )
    if set(result) != RESULT_SECTIONS:
        raise error("WRITE_REFUSED: result sections are incomplete or unexpected")
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
    ):
        raise error("WRITE_REFUSED: incompatible result metadata")
    if not _non_claims_valid(result.get("non_claims")):
        raise error("WRITE_REFUSED: result non-claims are not canonical false")

    checks = result.get(f"{PREFIX}_checks")
    if not isinstance(checks, list) or not all(
        isinstance(check, Mapping)
        and type(check.get("passed")) is bool
        for check in checks
    ):
        raise error("WRITE_REFUSED: result checks are malformed")
    for check in checks:
        for field in ("failure_code", "block_code"):
            if (
                check.get(field) is not None
                and check.get(field) not in BLOCK_CODES
            ):
                raise error("WRITE_REFUSED: non-public check code")

    failed = sum(check.get("passed") is False for check in checks)
    passed = sum(check.get("passed") is True for check in checks)
    if (
        type(result.get("failed_check_count")) is not int
        or type(result.get("passed_check_count")) is not int
        or result.get("failed_check_count") != failed
        or result.get("passed_check_count") != passed
    ):
        raise error("WRITE_REFUSED: check counts are inconsistent")
    if result.get("outcome") == OUTCOME_BLOCKED:
        if failed <= 0:
            raise error("WRITE_REFUSED: blocked result lacks a failed check")
    elif failed != 0:
        raise error("WRITE_REFUSED: non-blocked result has a failed check")

    if not _branch_valid(result):
        raise error("WRITE_REFUSED: branch posture is inconsistent")
    summary = result.get(f"{PREFIX}_summary")
    if (
        not isinstance(summary, Mapping)
        or dict(summary) != _summary_from_result(result)
    ):
        raise error("WRITE_REFUSED: summary is inconsistent")
    if _contains_forbidden_result_material(result):
        raise error(
            "WRITE_REFUSED: complete waiting, upstream, basis, or source material present"
        )
    if not _bounded_json(result) or _serialized_size(result) is None:
        raise error("WRITE_REFUSED: result is not bounded JSON")


def write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid deterministic result without silent overwrite."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationRequestV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    _validate_write_result(result)
    target = (
        _as_repo_path(output_path)
        if output_path is not None
        else OUTPUT_ROOT / OUTPUT_FILENAME
    )
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationRequestV0MinError(
            "WRITE_REFUSED: output path is protected or belongs to upstream lineage"
        )
    target = _next_available_output_path(target)
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as handle:
            json.dump(
                copy.deepcopy(dict(result)),
                handle,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            handle.write("\n")
    except (OSError, TypeError, ValueError) as exc:
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationRequestV0MinError(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
