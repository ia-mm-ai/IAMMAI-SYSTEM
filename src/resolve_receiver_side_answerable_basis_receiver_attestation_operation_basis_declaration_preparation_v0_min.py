"""Prepare one bounded receiver-attestation operation-basis candidate.

The resolver consumes one exact recorded preparation request and one exact
bounded trace family. It may prepare one 21-field declaration candidate, but
it does not declare, supply, admit, or execute that candidate.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from pathlib import Path
from types import MappingProxyType
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_receiver_attestation_operation_"
    "basis_declaration_preparation_v0_min"
)

PREPARATION_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_001"
)
PREPARATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION"
)
PREPARATION_VERSION = "0.1.0"
PREPARATION_SCOPE = (
    "PREPARE_ONE_SOURCE_BODY_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_CANDIDATE_ONLY"
)

SELECTED_PREPARATION_REQUEST_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_request_001"
)
SELECTED_PREPARATION_REQUEST_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION_REQUEST"
)
SELECTED_PREPARATION_REQUEST_VERSION = "0.1.0"
SELECTED_PREPARATION_REQUEST_SCOPE = (
    "REQUEST_PREPARATION_OF_ONE_SOURCE_BODY_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_DECLARATION_CANDIDATE_ONLY"
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
SELECTED_BOUNDARY_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY"
)
SELECTED_BOUNDARY_VERSION = "0.1.0"
SELECTED_BOUNDARY_SCOPE = (
    "CONSIDER_RECEIVER_ATTESTATION_FOR_ONE_SUFFICIENT_"
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)
SELECTED_BOUNDARY_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_"
    "receiver_attestation_boundary_v0_min_v2"
)
SELECTED_BOUNDARY_RESULT_VERSION = "0.2.0"
SELECTED_BOUNDARY_OUTCOME = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY_ALLOWED"
)
SELECTED_BOUNDARY_RESULT = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_CONSIDERATION_ALLOWED"
)
SELECTED_SUFFICIENCY_OPERATION_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001"
)
SELECTED_SUFFICIENCY_OPERATION_RESULT = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT"
)

PREPARATION_REQUEST_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_receiver_attestation_operation_"
    "basis_declaration_preparation_request_v0_min"
)
PREPARATION_REQUEST_RESULT_VERSION = "0.1.0"
PREPARATION_REQUEST_OUTCOME = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION_REQUEST_RECORDED"
)
PREPARATION_REQUEST_RESULT = (
    "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_"
    "PREPARATION_REQUEST_RECORDED"
)

OUTCOME_PREPARED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION_PREPARED"
)
OUTCOME_NOT_PREPARED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION_NOT_PREPARED"
)
OUTCOME_BLOCKED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_PREPARED,
    OUTCOME_NOT_PREPARED,
    OUTCOME_BLOCKED,
)

PREPARATION_RESULT_PREPARED = (
    "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_CANDIDATE_PREPARED"
)
PREPARATION_RESULT_NOT_PREPARED = (
    "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_"
    "CANDIDATE_NOT_PREPARED"
)
PREPARATION_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
PREPARATION_RESULT_FAMILY = (
    PREPARATION_RESULT_PREPARED,
    PREPARATION_RESULT_NOT_PREPARED,
    PREPARATION_RESULT_NOT_EVALUATED,
)
RESULT_FAMILY = PREPARATION_RESULT_FAMILY

INTENT_PREPARE = (
    "PREPARE_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_DECLARATION_CANDIDATE"
)
INTENT_BLOCK = (
    "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_DECLARATION_PREPARATION"
)
SUPPORTED_INTENTS = (INTENT_PREPARE, INTENT_BLOCK)
REQUEST_SELECTION_FIELD = "basis_declaration_preparation_selected"

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_DECLARATION_PREPARATION_V0_MIN_SPEC.md"
)
SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_declaration_"
    "preparation_request_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_request_001__receiver_side_answerable_basis_"
    "receiver_attestation_operation_basis_declaration_"
    "preparation_request_v0_min_result.json"
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
SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_001__"
    "receiver_side_answerable_basis_receiver_attestation_"
    "operation_v0_min_result.json"
)
SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_candidate_sufficiency_operation_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_"
    "operation_v0_min_result_001.json"
)

GOVERNING_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
)
SELECTED_PREPARATION_REQUEST_ARTIFACT_PATH = (
    REPO_ROOT / SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH
)
SELECTED_BOUNDARY_ARTIFACT_PATH = (
    REPO_ROOT / SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
)
BOUNDED_CAPTURE_DIRECTORY_PATH = (
    REPO_ROOT / BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
)

OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_declaration_"
    "preparation_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_001__receiver_side_answerable_basis_receiver_"
    "attestation_operation_basis_declaration_"
    "preparation_v0_min_result.json"
)

EXPECTED_ARCHIVE_SHA256 = (
    "a45a621c5c6c2f37daefd7e896f32cdb50bff21ab69ec9281912049bd326724c"
)

BOUNDED_SOURCE_REFERENCES = MappingProxyType(
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
            / "extracted/receiver_attestation_001/"
            "capture_only_statement.txt"
        ),
        "freely_given_statement_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/"
            "freely_given_statement.txt"
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
EXACT_BOUNDED_SOURCE_REFERENCES = BOUNDED_SOURCE_REFERENCES
COMPONENT_RELATIVE_PATHS = MappingProxyType(
    {
        key: Path(value)
        for key, value in BOUNDED_SOURCE_REFERENCES.items()
        if key
        not in {
            "selected_receiver_attestation_boundary_artifact_path",
            "bounded_capture_directory_path",
            "expected_archive_sha256",
        }
    }
)

TEXT_COMPONENT_FIELDS = (
    "attestation_statement_path",
    "attestation_timestamp_path",
    "capture_method_path",
    "capture_only_statement_path",
    "freely_given_statement_path",
    "knock_reference_path",
    "receiver_label_path",
    "receiver_working_directory_path",
)

CANDIDATE_FIELDS = (
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
PREPARED_DECLARATION_CANDIDATE_FIELDS = CANDIDATE_FIELDS
BASIS_FIELDS = CANDIDATE_FIELDS

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
POSTURE_KEY_FAMILIES = MappingProxyType(
    {
        "trace_integrity_postures": TRACE_INTEGRITY_POSTURE_KEYS,
        "ambiguity_postures": AMBIGUITY_POSTURE_KEYS,
        "contradiction_postures": CONTRADICTION_POSTURE_KEYS,
        "unresolved_postures": UNRESOLVED_POSTURE_KEYS,
    }
)

NON_CONVERSION_STATEMENT = (
    "bounded trace admission and recording do not establish occurrence "
    "creation, identity, independent custody, verified provenance, physical "
    "validity, current presence, receiver-answerable receipt, truth, "
    "authority, or standing."
)
CANONICAL_NON_CONVERSION_STATEMENT = NON_CONVERSION_STATEMENT

REQUIRED_BASIS_NON_CLAIMS = (
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

REQUIRED_FALSE_NON_CLAIMS = (
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
    "preparation_permission_created",
    "reusable_receiver_attestation_operation_basis_declaration_"
    "preparation_route_created",
    "same_receiver_attestation_operation_basis_declaration_"
    "preparation_rerun_authorized",
    "automatic_receiver_attestation_operation_basis_declaration_"
    "preparation_retry_created",
    "receiver_attestation_operation_basis_declaration_"
    "preparation_debt_created",
    "receiver_attestation_operation_basis_declaration_"
    "preparation_obligation_created",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

REQUEST_REQUIRED_FALSE_NON_CLAIMS = tuple(
    dict.fromkeys(
        (
            *REQUIRED_FALSE_NON_CLAIMS,
            "preparation_recorded",
            "preparation_result_recorded",
            "preparation_exhausted",
            "basis_declaration_preparation_started",
            "basis_declaration_preparation_completed",
            "receiver_attestation_operation_basis_declaration_"
            "candidate_prepared",
            "receiver_attestation_operation_basis_prepared",
            "receiver_attestation_operation_basis_declared",
            "receiver_attestation_operation_basis_supplied",
            "receiver_attestation_operation_basis_admitted",
            "receiver_attestation_operation_recorded",
            "receiver_attestation_operation_result_recorded",
            "receiver_attestation_operation_exhausted",
            "receiver_attestation_decided",
        )
    )
)

UPSTREAM_REQUEST_FALSE_NON_CLAIMS = (
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
    "basis_declaration_preparation_started",
    "basis_declaration_preparation_completed",
    "receiver_attestation_operation_basis_prepared",
    "receiver_attestation_operation_basis_declared",
    "receiver_attestation_operation_basis_supplied",
    "receiver_attestation_operation_basis_admitted",
)

REQUIRED_UPSTREAM_FALSE_POSTURES = (
    "receiver_attestation_created",
    "receiver_attestation_supported",
    "receiver_attestation_recorded",
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
    "repeated_receiver_attestation_boundary_permission_created",
    "reusable_receiver_attestation_route_created",
    "same_receiver_attestation_boundary_rerun_authorized",
    "automatic_receiver_attestation_boundary_retry_created",
    "receiver_attestation_boundary_debt_created",
    "receiver_attestation_boundary_obligation_created",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

PROHIBITED_INPUT_FLAGS = MappingProxyType(
    {
        "request_prepared_declaration_candidate": (
            "PROHIBITED_CALLER_PREPARED_CANDIDATE"
        ),
        "request_caller_selected_posture_maps": (
            "PROHIBITED_CALLER_SELECTED_POSTURE"
        ),
        "request_preparation_outcome": "PROHIBITED_RESULT_PRECLAIM",
        "request_preparation_result": "PROHIBITED_RESULT_PRECLAIM",
        "request_operation_outcome": "PROHIBITED_RESULT_PRECLAIM",
        "request_operation_result": "PROHIBITED_RESULT_PRECLAIM",
        "request_source_body_embedding": "PROHIBITED_SOURCE_BODY_EMBEDDING",
        "request_basis_declaration": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_basis_supply": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_basis_admission": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_operation_execution": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_receiver_attestation_recording": (
            "PROHIBITED_DOWNSTREAM_CONVERSION"
        ),
        "request_receiver_answerable_receipt_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION"
        ),
        "request_presence_establishment": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_identity_creation": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_custody_creation": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_provenance_creation": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_authority_creation": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_truth_creation": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_standing_creation": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_relation_creation": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_coupling_creation": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_output_authorization": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_action_authorization": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_synchronization_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION"
        ),
        "request_follow_on_authorization": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "request_follow_on_work_authorization": (
            "PROHIBITED_DOWNSTREAM_CONVERSION"
        ),
        "request_repeated_preparation_permission_creation": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "request_reusable_preparation_route_creation": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "request_same_preparation_rerun": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "request_automatic_retry": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "request_preparation_debt_creation": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "request_preparation_obligation_creation": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "request_scheduled_action": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "request_automatic_next_step": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "request_repository_scan": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "request_file_discovery": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "request_affected_file_repair": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "request_validation_enforcement": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "request_prior_unsupported_claim_validation": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
    }
)
PROHIBITED_REQUEST_FLAGS = PROHIBITED_INPUT_FLAGS

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "REQUEST_OVERSIZED",
        "REQUEST_NESTING_EXCEEDED",
        "REQUEST_FIELD_MISSING",
        "REQUEST_FIELD_UNKNOWN",
        "REQUEST_VALUE_MISMATCH",
        "UNSUPPORTED_INTENT",
        "EXPLICIT_BLOCK_REQUESTED",
        "PREPARATION_IDENTITY_MISMATCH",
        "PREPARATION_REQUEST_IDENTITY_MISMATCH",
        "SELECTED_OPERATION_IDENTITY_MISMATCH",
        "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
        "GOVERNING_SPECIFICATION_PATH_MISMATCH",
        "PREPARATION_REQUEST_ARTIFACT_PATH_MISMATCH",
        "BOUNDED_SOURCE_REFERENCE_MISMATCH",
        "PREPARATION_SELECTION_INVALID",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "PROHIBITED_CALLER_PREPARED_CANDIDATE",
        "PROHIBITED_CALLER_SELECTED_POSTURE",
        "PROHIBITED_RESULT_PRECLAIM",
        "PROHIBITED_SOURCE_BODY_EMBEDDING",
        "PROHIBITED_DOWNSTREAM_CONVERSION",
        "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION",
        "SPECIFICATION_NOT_AVAILABLE",
        "SPECIFICATION_MARKER_MISSING",
        "PREPARATION_REQUEST_ARTIFACT_NOT_AVAILABLE",
        "PREPARATION_REQUEST_ARTIFACT_NOT_PARSEABLE",
        "PREPARATION_REQUEST_ARTIFACT_NOT_MAPPING",
        "PREPARATION_REQUEST_ARTIFACT_METADATA_MISMATCH",
        "PREPARATION_REQUEST_ARTIFACT_FAILED_CHECKS_PRESENT",
        "PREPARATION_REQUEST_ARTIFACT_IDENTITY_MISMATCH",
        "PREPARATION_REQUEST_ARTIFACT_NOT_RECORDED",
        "PREPARATION_REQUEST_ARTIFACT_BLOCKED",
        "PREPARATION_REQUEST_ARTIFACT_POSTURE_INVALID",
        "PREPARATION_REQUEST_ARTIFACT_NON_CLAIM_NOT_FALSE",
        "PREPARATION_REQUEST_ARTIFACT_OMISSION_INVALID",
        "SELECTED_BOUNDARY_ARTIFACT_NOT_AVAILABLE",
        "SELECTED_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
        "SELECTED_BOUNDARY_ARTIFACT_NOT_MAPPING",
        "SELECTED_BOUNDARY_METADATA_MISMATCH",
        "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
        "SELECTED_BOUNDARY_POSTURE_INVALID",
        "SELECTED_BOUNDARY_NON_CLAIM_NOT_FALSE",
        "WRITE_REFUSED",
    }
)

NOT_PREPARED_CODES = frozenset(
    {
        "PREPARATION_NOT_SELECTED",
        "BOUNDED_COMPONENT_ABSENT",
        "BOUNDED_COMPONENT_UNREADABLE",
        "ARCHIVE_HASH_RECORD_MALFORMED",
        "ARCHIVE_HASH_MISMATCH",
        "TEXT_COMPONENT_INVALID",
        "TIMESTAMP_INVALID",
        "RECORDED_SIGNAL_INVALID",
        "CANDIDATE_NOT_TRUTHFULLY_PREPARABLE",
    }
)

MAX_SERIALIZED_REQUEST_SIZE = 262_144
MAX_MAPPING_ITEMS = 256
MAX_SEQUENCE_ITEMS = 128
MAX_NESTING_DEPTH = 12
MAX_TEXT_LENGTH = 8_192

PREFIX = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation"
)
PREPARATION_REQUEST_PREFIX = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_request"
)
BOUNDARY_PREFIX = (
    "receiver_side_answerable_basis_receiver_attestation_boundary"
)

SPECIFICATION_MARKER_CLASSES = MappingProxyType(
    {
        "title": (
            "# Receiver-Side Answerable Basis Receiver Attestation Operation "
            "Basis Declaration Preparation V0 Minimum Specification",
        ),
        "preparation_identity": (
            PREPARATION_ID,
            PREPARATION_TYPE,
            PREPARATION_VERSION,
            PREPARATION_SCOPE,
        ),
        "selected_identities": (
            SELECTED_PREPARATION_REQUEST_ID,
            SELECTED_PREPARATION_REQUEST_TYPE,
            OPERATION_ID,
            OPERATION_TYPE,
            CANDIDATE_ID,
            CANDIDATE_TYPE,
        ),
        "selected_request_artifact": (
            str(SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH),
        ),
        "bounded_source_family": tuple(
            dict.fromkeys(BOUNDED_SOURCE_REFERENCES.values())
        ),
        "candidate_schema": CANDIDATE_FIELDS,
        "posture_key_families": (
            *TRACE_INTEGRITY_POSTURE_KEYS,
            *AMBIGUITY_POSTURE_KEYS,
            *CONTRADICTION_POSTURE_KEYS,
            *UNRESOLVED_POSTURE_KEYS,
        ),
        "non_conversion": (NON_CONVERSION_STATEMENT,),
        "basis_non_claims": REQUIRED_BASIS_NON_CLAIMS,
        "outcomes": OUTCOME_FAMILY,
        "results": PREPARATION_RESULT_FAMILY,
        "precedence": (
            "structural or constitutional invalidity produces `BLOCKED`",
            "cannot truthfully produce one complete candidate produces `NOT_PREPARED`",
            "one complete truthful candidate produces `PREPARED`",
        ),
        "separation": (
            "a prepared declaration candidate is not declared basis;",
            "declared basis is not supplied basis;",
            "supplied basis is not admitted basis;",
            "admitted basis is not operation execution;",
            "operation execution is not operation result.",
        ),
        "archive_non_conversion": (
            "It does not establish receiver identity, provenance, custody, occurrence truth, physical validity, or presence.",
        ),
        "not_prepared_non_result": (
            "the receiver-attestation operation produced `NOT_RECORDED` or `INDETERMINATE`",
        ),
        "exhaustion_non_authorization": (
            "Exhaustion does not authorize basis declaration, basis supply, basis admission, operation execution",
        ),
        "open_not_next": (
            "Open means not selected, not scheduled, not authorized, and not executed.",
        ),
    }
)

RESULT_OMISSION_FIELDS = (
    "complete_preparation_request_artifact_omitted",
    "complete_waiting_operation_artifact_omitted",
    "complete_upstream_boundary_artifact_omitted",
    "complete_candidate_sufficiency_artifact_omitted",
    "complete_candidate_sufficiency_basis_omitted",
    "archive_bytes_omitted",
    "text_component_bodies_omitted",
    "recorded_signal_body_omitted",
)

FORBIDDEN_PAYLOAD_KEYS = frozenset(
    {
        "complete_preparation_request_artifact",
        "complete_waiting_operation_artifact",
        "complete_upstream_boundary_artifact",
        "complete_candidate_sufficiency_artifact",
        "complete_candidate_sufficiency_basis",
        "archive_bytes",
        "hash_record_body",
        "text_component_bodies",
        "recorded_signal_body",
        "complete_recorded_signal_data",
        "samples",
        "raw_source_body",
    }
)

BLOCKED_ROUTES = (
    "preparation request directly to declared basis",
    "prepared candidate directly to basis supply or admission",
    "prepared candidate directly to operation execution or result",
    "capture existence or hash match directly to occurrence verification",
    "preparation directly to receiver attestation, receipt, or presence",
    "preparation directly to identity, custody, provenance, authority, truth, or standing",
    "completed preparation directly to rerun, retry, debt, obligation, or automatic next step",
    "preparation directly to repair or contaminated-lineage validation",
)

WHAT_REMAINS_OPEN = (
    "preparation test",
    "preparation live artifact",
    "basis declaration",
    "declaration resolver and test",
    "basis submission",
    "basis admission",
    "receiver-attestation operation execution",
    "receiver-attestation operation result",
    "receiver attestation",
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
        "selected_preparation_request_operation_candidate_identity",
        "specification_marker_validation",
        "preparation_request_artifact_validation",
        "selected_boundary_reference_validation",
        "bounded_path_and_file_evaluation",
        "archive_correspondence_metadata",
        "text_component_metadata",
        "timestamp_metadata",
        "recorded_signal_metadata",
        "preparation_decision",
        "prepared_declaration_candidate",
        PREFIX,
        f"{PREFIX}_checks",
        f"{PREFIX}_statement",
        f"{PREFIX}_non_meaning",
        "blocked_routes",
        "what_remains_open",
        "non_claims",
        "omission_posture",
        "outcome",
        "block",
        "resolver_module",
        "result_version",
        "failed_check_count",
        "passed_check_count",
        f"{PREFIX}_summary",
    }
)


class ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationV0MinError(
    Exception
):
    """Raised when a bounded preparation result cannot be summarized or written."""


class _DuplicateJsonKeyError(ValueError):
    """Raised when one JSON mapping repeats a member name."""


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


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


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


def _read_text(value: Path | str) -> tuple[str | None, str | None]:
    path = _as_repo_path(value)
    if not path.is_file():
        return None, "not_a_file"
    try:
        return path.read_text(encoding="utf-8"), None
    except (OSError, UnicodeError):
        return None, "unreadable"


def _loads_json(text: str) -> tuple[Any | None, str | None]:
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


def _read_json(value: Path | str) -> tuple[Any | None, str | None]:
    text, error = _read_text(value)
    if error is not None or text is None:
        return None, error
    return _loads_json(text)


def _sha256_file(path: Path) -> tuple[str | None, int | None, str | None]:
    try:
        digest = hashlib.sha256()
        byte_count = 0
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                digest.update(chunk)
                byte_count += len(chunk)
        return digest.hexdigest(), byte_count, None
    except OSError:
        return None, None, "unreadable"


def _check(
    name: str,
    passed: bool,
    code: str | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {"check": name, "passed": bool(passed)}
    if not passed and code is not None:
        item["failure_code"] = code
        item["block_code"] = code
    return item


def _failure(
    checks: list[dict[str, Any]],
    name: str,
    code: str,
    reason: str | None = None,
) -> tuple[str, str]:
    checks.append(_check(name, False, code))
    return code, reason or name.replace("_", " ")


def _canonical_result_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_request_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUEST_REQUIRED_FALSE_NON_CLAIMS}


def _canonical_basis_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_BASIS_NON_CLAIMS}


def _exact_false_mapping(value: Any, fields: Sequence[str]) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(fields)
        and all(value.get(field) is False for field in fields)
    )


def _exact_boolean_mapping(value: Any, fields: Sequence[str]) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(fields)
        and all(type(value.get(field)) is bool for field in fields)
    )


def _canonical_bounded_source_references() -> dict[str, str]:
    return dict(BOUNDED_SOURCE_REFERENCES)


def _expected_request_values() -> dict[str, Any]:
    return {
        "preparation_id": PREPARATION_ID,
        "preparation_type": PREPARATION_TYPE,
        "preparation_version": PREPARATION_VERSION,
        "preparation_scope": PREPARATION_SCOPE,
        "selected_preparation_request_id": SELECTED_PREPARATION_REQUEST_ID,
        "selected_preparation_request_type": SELECTED_PREPARATION_REQUEST_TYPE,
        "selected_preparation_request_version": (
            SELECTED_PREPARATION_REQUEST_VERSION
        ),
        "selected_preparation_request_scope": (
            SELECTED_PREPARATION_REQUEST_SCOPE
        ),
        "selected_receiver_attestation_operation_id": OPERATION_ID,
        "selected_receiver_attestation_operation_type": OPERATION_TYPE,
        "selected_receiver_attestation_operation_version": OPERATION_VERSION,
        "selected_receiver_attestation_operation_scope": OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "governing_preparation_specification_path": str(
            GOVERNING_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_preparation_request_artifact_path": str(
            SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH
        ),
    }


def _request_allowed_keys() -> frozenset[str]:
    return frozenset(
        {
            "intent",
            REQUEST_SELECTION_FIELD,
            "bounded_source_references",
            "declared_non_claims",
            *tuple(_expected_request_values()),
            *tuple(PROHIBITED_INPUT_FLAGS),
        }
    )


def build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_request(
    *,
    intent: str = INTENT_PREPARE,
    basis_declaration_preparation_selected: bool = True,
    bounded_source_references: Mapping[str, Any] | None = None,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one canonical bounded preparation request."""
    request: dict[str, Any] = {
        "intent": intent,
        **_expected_request_values(),
        "bounded_source_references": copy.deepcopy(
            _canonical_bounded_source_references()
            if bounded_source_references is None
            else bounded_source_references
        ),
        REQUEST_SELECTION_FIELD: basis_declaration_preparation_selected,
        "declared_non_claims": copy.deepcopy(
            _canonical_request_non_claims()
            if declared_non_claims is None
            else declared_non_claims
        ),
        **{field: False for field in PROHIBITED_INPUT_FLAGS},
    }
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_request(
    *,
    basis_declaration_preparation_selected: bool = True,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one declared request while retaining visible overrides."""
    return build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_request(
        basis_declaration_preparation_selected=(
            basis_declaration_preparation_selected
        ),
        **overrides,
    )


def _identity_failure_code(field: str) -> str:
    if field.startswith("preparation_") and not field.startswith(
        "preparation_request"
    ):
        return "PREPARATION_IDENTITY_MISMATCH"
    if field.startswith("selected_preparation_request_"):
        return "PREPARATION_REQUEST_IDENTITY_MISMATCH"
    if field.startswith("selected_receiver_attestation_operation_"):
        return "SELECTED_OPERATION_IDENTITY_MISMATCH"
    if "candidate_" in field:
        return "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
    if field == "governing_preparation_specification_path":
        return "GOVERNING_SPECIFICATION_PATH_MISMATCH"
    if field == "selected_preparation_request_artifact_path":
        return "PREPARATION_REQUEST_ARTIFACT_PATH_MISMATCH"
    return "REQUEST_VALUE_MISMATCH"


def _validate_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    size = _serialized_size(request)
    if size is None or size > MAX_SERIALIZED_REQUEST_SIZE:
        return _failure(checks, "request_bounded_size", "REQUEST_OVERSIZED")
    if not _bounded_json(request):
        return _failure(
            checks,
            "request_bounded_nesting",
            "REQUEST_NESTING_EXCEEDED",
        )

    allowed = _request_allowed_keys()
    missing = allowed - set(request)
    if missing:
        return _failure(
            checks,
            "request_every_field_present",
            "REQUEST_FIELD_MISSING",
        )
    unknown = set(request) - allowed
    if unknown:
        return _failure(
            checks,
            "request_no_unknown_field",
            "REQUEST_FIELD_UNKNOWN",
        )

    intent = request.get("intent")
    if intent not in SUPPORTED_INTENTS:
        return _failure(checks, "intent_supported", "UNSUPPORTED_INTENT")
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
                field + "_exact",
                _identity_failure_code(field),
            )
    checks.append(_check("request_identity_and_paths_exact", True))

    references = request.get("bounded_source_references")
    if (
        not isinstance(references, Mapping)
        or set(references) != set(BOUNDED_SOURCE_REFERENCES)
        or any(
            references.get(field) != expected
            for field, expected in BOUNDED_SOURCE_REFERENCES.items()
        )
    ):
        return _failure(
            checks,
            "bounded_source_references_exact",
            "BOUNDED_SOURCE_REFERENCE_MISMATCH",
        )
    checks.append(_check("bounded_source_references_exact", True))

    if not _exact_bool(request.get(REQUEST_SELECTION_FIELD)):
        return _failure(
            checks,
            "preparation_selection_boolean",
            "PREPARATION_SELECTION_INVALID",
        )
    checks.append(_check("preparation_selection_boolean", True))

    if not _exact_false_mapping(
        request.get("declared_non_claims"),
        REQUEST_REQUIRED_FALSE_NON_CLAIMS,
    ):
        return _failure(
            checks,
            "request_non_claims_exact_false",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    checks.append(_check("request_non_claims_exact_false", True))

    for field, code in PROHIBITED_INPUT_FLAGS.items():
        value = request.get(field)
        if value is True:
            return _failure(checks, field + "_not_requested", code)
        if value is not False:
            return _failure(
                checks,
                field + "_exact_false",
                "REQUEST_VALUE_MISMATCH",
            )
    checks.append(_check("prohibited_input_flags_exact_false", True))
    return None, None


def _marker_status(text: str) -> dict[str, bool]:
    return {
        name: all(marker in text for marker in markers)
        for name, markers in SPECIFICATION_MARKER_CLASSES.items()
    }


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
            "governing_specification_available",
            "SPECIFICATION_NOT_AVAILABLE",
        )
        return validation, code, reason
    markers = _marker_status(text)
    validation["marker_status"] = markers
    if not all(markers.values()):
        code, reason = _failure(
            checks,
            "governing_specification_markers_exact",
            "SPECIFICATION_MARKER_MISSING",
        )
        return validation, code, reason
    validation["specification_markers_validated"] = True
    checks.append(_check("governing_specification_markers_exact", True))
    return validation, None, None


def _validate_preparation_request_artifact(
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], str | None, str | None]:
    validation: dict[str, Any] = {
        "selected_preparation_request_artifact_path": str(
            SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH
        ),
        "preparation_request_artifact_validated": False,
        "metadata": {},
        "identity": {},
        "posture": {},
        "result_level_non_claims_canonical_false": False,
        "complete_preparation_request_artifact_omitted": True,
    }
    artifact, error = _read_json(
        SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH
    )
    if error in {"not_a_file", "unreadable"}:
        code, reason = _failure(
            checks,
            "preparation_request_artifact_available",
            "PREPARATION_REQUEST_ARTIFACT_NOT_AVAILABLE",
        )
        return validation, code, reason
    if error is not None:
        code, reason = _failure(
            checks,
            "preparation_request_artifact_parseable",
            "PREPARATION_REQUEST_ARTIFACT_NOT_PARSEABLE",
        )
        return validation, code, reason
    if not isinstance(artifact, Mapping):
        code, reason = _failure(
            checks,
            "preparation_request_artifact_mapping",
            "PREPARATION_REQUEST_ARTIFACT_NOT_MAPPING",
        )
        return validation, code, reason

    state = _mapping(artifact.get(PREPARATION_REQUEST_PREFIX))
    declared = _mapping(artifact.get("declared_" + PREPARATION_REQUEST_PREFIX))
    summary = _mapping(
        artifact.get(PREPARATION_REQUEST_PREFIX + "_summary")
    )
    block = _mapping(artifact.get("block"))
    non_claims = artifact.get("non_claims")
    if not state or not declared or not summary or not block:
        code, reason = _failure(
            checks,
            "preparation_request_artifact_sections",
            "PREPARATION_REQUEST_ARTIFACT_NOT_MAPPING",
        )
        return validation, code, reason

    validation["metadata"] = {
        "resolver_module": artifact.get("resolver_module"),
        "result_version": artifact.get("result_version"),
        "failed_check_count": artifact.get("failed_check_count"),
        "passed_check_count": artifact.get("passed_check_count"),
        "outcome": artifact.get("outcome"),
    }
    if (
        artifact.get("resolver_module")
        != PREPARATION_REQUEST_RESOLVER_MODULE
        or artifact.get("result_version")
        != PREPARATION_REQUEST_RESULT_VERSION
        or artifact.get("outcome") != PREPARATION_REQUEST_OUTCOME
    ):
        code, reason = _failure(
            checks,
            "preparation_request_artifact_metadata_exact",
            "PREPARATION_REQUEST_ARTIFACT_METADATA_MISMATCH",
        )
        return validation, code, reason
    if (
        type(artifact.get("failed_check_count")) is not int
        or artifact.get("failed_check_count") != 0
    ):
        code, reason = _failure(
            checks,
            "preparation_request_artifact_failed_checks_zero",
            "PREPARATION_REQUEST_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
        return validation, code, reason
    checks.append(_check("preparation_request_artifact_metadata_exact", True))

    identity_expectations = {
        "preparation_request_id": SELECTED_PREPARATION_REQUEST_ID,
        "preparation_request_type": SELECTED_PREPARATION_REQUEST_TYPE,
        "preparation_request_version": SELECTED_PREPARATION_REQUEST_VERSION,
        "preparation_request_scope": SELECTED_PREPARATION_REQUEST_SCOPE,
        "selected_receiver_attestation_operation_id": OPERATION_ID,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
    }
    for field, expected in identity_expectations.items():
        if state.get(field) != expected or declared.get(field) != expected:
            code, reason = _failure(
                checks,
                "preparation_request_artifact_identity_" + field,
                "PREPARATION_REQUEST_ARTIFACT_IDENTITY_MISMATCH",
            )
            return validation, code, reason
    validation["identity"] = dict(identity_expectations)
    checks.append(_check("preparation_request_artifact_identity_exact", True))

    if (
        state.get("request_result") != PREPARATION_REQUEST_RESULT
        or summary.get("request_result") != PREPARATION_REQUEST_RESULT
        or summary.get("request_selection") is not True
    ):
        code, reason = _failure(
            checks,
            "preparation_request_artifact_recorded_result",
            "PREPARATION_REQUEST_ARTIFACT_NOT_RECORDED",
        )
        return validation, code, reason
    if (
        block.get("blocked") is not False
        or block.get("code") is not None
        or block.get("block_code") is not None
        or block.get("reason") is not None
        or summary.get("blocked") is not False
    ):
        code, reason = _failure(
            checks,
            "preparation_request_artifact_not_blocked",
            "PREPARATION_REQUEST_ARTIFACT_BLOCKED",
        )
        return validation, code, reason

    true_fields = (
        "preparation_request_recorded",
        "preparation_request_result_recorded",
        "preparation_request_exhausted",
        "basis_declaration_preparation_requested",
    )
    false_fields = (
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
    if any(state.get(field) is not True for field in true_fields) or any(
        state.get(field) is not False for field in false_fields
    ):
        code, reason = _failure(
            checks,
            "preparation_request_artifact_posture_exact",
            "PREPARATION_REQUEST_ARTIFACT_POSTURE_INVALID",
        )
        return validation, code, reason
    validation["posture"] = {
        **{field: True for field in true_fields},
        **{field: False for field in false_fields},
    }
    checks.append(_check("preparation_request_artifact_posture_exact", True))

    if (
        not _exact_false_mapping(
            non_claims,
            UPSTREAM_REQUEST_FALSE_NON_CLAIMS,
        )
        or summary.get("result_level_non_claims_canonical_false") is not True
    ):
        code, reason = _failure(
            checks,
            "preparation_request_artifact_non_claims_exact_false",
            "PREPARATION_REQUEST_ARTIFACT_NON_CLAIM_NOT_FALSE",
        )
        return validation, code, reason
    validation["result_level_non_claims_canonical_false"] = True

    state_omissions = (
        "complete_waiting_artifact_omitted",
        "complete_upstream_boundary_artifact_omitted",
        "complete_candidate_sufficiency_artifact_omitted",
        "complete_candidate_sufficiency_basis_omitted",
        "complete_operation_basis_omitted",
        "archive_bytes_omitted",
        "text_component_bodies_omitted",
        "recorded_signal_body_omitted",
    )
    if (
        summary.get("complete_material_omitted") is not True
        or any(state.get(field) is not True for field in state_omissions)
    ):
        code, reason = _failure(
            checks,
            "preparation_request_artifact_material_omitted",
            "PREPARATION_REQUEST_ARTIFACT_OMISSION_INVALID",
        )
        return validation, code, reason

    validation["preparation_request_artifact_validated"] = True
    checks.append(_check("preparation_request_artifact_validated", True))
    return validation, None, None


def _validate_selected_boundary(
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], str | None, str | None]:
    validation: dict[str, Any] = {
        "selected_boundary_artifact_path": str(
            SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
        ),
        "selected_boundary_reference_validated": False,
        "metadata": {},
        "identity": {},
        "posture": {},
        "complete_boundary_artifact_omitted": True,
    }
    artifact, error = _read_json(SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH)
    if error in {"not_a_file", "unreadable"}:
        code, reason = _failure(
            checks,
            "selected_boundary_artifact_available",
            "SELECTED_BOUNDARY_ARTIFACT_NOT_AVAILABLE",
        )
        return validation, code, reason
    if error is not None:
        code, reason = _failure(
            checks,
            "selected_boundary_artifact_parseable",
            "SELECTED_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
        )
        return validation, code, reason
    if not isinstance(artifact, Mapping):
        code, reason = _failure(
            checks,
            "selected_boundary_artifact_mapping",
            "SELECTED_BOUNDARY_ARTIFACT_NOT_MAPPING",
        )
        return validation, code, reason

    boundary = _mapping(artifact.get(BOUNDARY_PREFIX))
    summary = _mapping(artifact.get(BOUNDARY_PREFIX + "_summary"))
    non_claims = artifact.get("non_claims")
    if not boundary or not summary:
        code, reason = _failure(
            checks,
            "selected_boundary_artifact_sections",
            "SELECTED_BOUNDARY_ARTIFACT_NOT_MAPPING",
        )
        return validation, code, reason

    validation["metadata"] = {
        "resolver_module": artifact.get("resolver_module"),
        "result_version": artifact.get("result_version"),
        "failed_check_count": artifact.get("failed_check_count"),
        "passed_check_count": artifact.get("passed_check_count"),
        "outcome": artifact.get("outcome"),
    }
    if (
        artifact.get("resolver_module") != SELECTED_BOUNDARY_RESOLVER_MODULE
        or artifact.get("result_version") != SELECTED_BOUNDARY_RESULT_VERSION
        or artifact.get("outcome") != SELECTED_BOUNDARY_OUTCOME
        or type(artifact.get("failed_check_count")) is not int
        or artifact.get("failed_check_count") != 0
    ):
        code, reason = _failure(
            checks,
            "selected_boundary_metadata_exact",
            "SELECTED_BOUNDARY_METADATA_MISMATCH",
        )
        return validation, code, reason

    identity_expectations = {
        "boundary_id": SELECTED_BOUNDARY_ID,
        "boundary_type": SELECTED_BOUNDARY_TYPE,
        "boundary_version": SELECTED_BOUNDARY_VERSION,
        "boundary_scope": SELECTED_BOUNDARY_SCOPE,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "selected_candidate_sufficiency_operation_id": (
            SELECTED_SUFFICIENCY_OPERATION_ID
        ),
        "selected_candidate_sufficiency_operation_result_required": (
            SELECTED_SUFFICIENCY_OPERATION_RESULT
        ),
    }
    if any(
        boundary.get(field) != expected
        for field, expected in identity_expectations.items()
    ):
        code, reason = _failure(
            checks,
            "selected_boundary_identity_exact",
            "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
        )
        return validation, code, reason
    validation["identity"] = dict(identity_expectations)

    boundary_expectations = {
        "receiver_attestation_boundary_result": SELECTED_BOUNDARY_RESULT,
        "receiver_attestation_boundary_recorded": True,
        "receiver_attestation_boundary_result_recorded": True,
        "receiver_attestation_consideration_allowed": True,
        "receiver_attestation_consideration_not_allowed": False,
        "receiver_attestation_boundary_exhausted": True,
        "bounded_material_selected_for_consideration": True,
    }
    summary_expectations = {
        "specification_markers_validated": True,
        "selected_operation_validated": True,
        "eight_dimensions_validated": True,
        "upstream_false_locks_validated": True,
        "result_level_non_claims_canonical_false": True,
        "complete_operation_artifact_omitted": True,
        "complete_sufficiency_basis_omitted": True,
        "complete_capture_signal_data_omitted": True,
    }
    for field, expected in boundary_expectations.items():
        actual = boundary.get(field)
        valid = actual is expected if type(expected) is bool else actual == expected
        if not valid:
            code, reason = _failure(
                checks,
                "selected_boundary_posture_" + field,
                "SELECTED_BOUNDARY_POSTURE_INVALID",
            )
            return validation, code, reason
    if any(
        summary.get(field) is not expected
        for field, expected in summary_expectations.items()
    ):
        code, reason = _failure(
            checks,
            "selected_boundary_summary_posture",
            "SELECTED_BOUNDARY_POSTURE_INVALID",
        )
        return validation, code, reason

    if (
        not _exact_false_mapping(
            non_claims,
            REQUIRED_UPSTREAM_FALSE_POSTURES,
        )
        or any(
            boundary.get(field) is not False
            for field in REQUIRED_UPSTREAM_FALSE_POSTURES
        )
    ):
        code, reason = _failure(
            checks,
            "selected_boundary_non_claims_exact_false",
            "SELECTED_BOUNDARY_NON_CLAIM_NOT_FALSE",
        )
        return validation, code, reason

    validation["posture"] = {
        **boundary_expectations,
        **summary_expectations,
        "upstream_non_claims_exact_false": True,
    }
    validation["selected_boundary_reference_validated"] = True
    checks.append(_check("selected_boundary_reference_validated", True))
    return validation, None, None


_HASH_RECORD_PATTERN = re.compile(
    r"^([0-9a-f]{64})  receiver_attestation_001\.zip\s*$"
)
_TIMESTAMP_PATTERN = re.compile(
    r"^attested_at="
    r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)"
    r"\s*$"
)
_SIGNAL_REQUIRED_KEYS = frozenset(
    {
        "recorded_at",
        "duration_s",
        "sample_rate_hz",
        "units",
        "device",
        "samples",
    }
)


def _timestamp_metadata(text: str) -> tuple[dict[str, Any], bool]:
    metadata: dict[str, Any] = {
        "timestamp_validated": False,
        "timestamp_interpretation_ambiguous": True,
        "parsed_utc": None,
    }
    match = _TIMESTAMP_PATTERN.fullmatch(text)
    if match is None:
        return metadata, False
    try:
        parsed = datetime.fromisoformat(
            match.group(1).replace("Z", "+00:00")
        )
    except ValueError:
        return metadata, False
    if parsed.tzinfo != timezone.utc:
        return metadata, False
    metadata.update(
        {
            "timestamp_validated": True,
            "timestamp_interpretation_ambiguous": False,
            "parsed_utc": match.group(1),
        }
    )
    return metadata, True


def _empty_evaluation() -> dict[str, Any]:
    return {
        "bounded_paths_validated": False,
        "required_bounded_components_available": False,
        "archive_hash_record_validated": False,
        "archive_correspondence_validated": False,
        "required_text_components_validated": False,
        "timestamp_validated": False,
        "recorded_signal_artifact_validated": False,
        "complete_21_field_candidate_preparable": False,
        "archive": {
            "path": BOUNDED_SOURCE_REFERENCES["preserved_archive_path"],
            "regular_file": False,
            "byte_count": None,
            "computed_sha256": None,
            "expected_sha256": EXPECTED_ARCHIVE_SHA256,
        },
        "hash_record": {
            "path": BOUNDED_SOURCE_REFERENCES["archive_hash_record_path"],
            "regular_file": False,
            "readable": False,
            "parsed_sha256": None,
        },
        "text_components": {},
        "timestamp": {
            "timestamp_validated": False,
            "timestamp_interpretation_ambiguous": False,
            "parsed_utc": None,
        },
        "recorded_signal": {
            "path": BOUNDED_SOURCE_REFERENCES["recorded_signal_path"],
            "regular_file": False,
            "readable": False,
            "parseable": False,
            "mapping": False,
            "minimum_structure_validated": False,
            "byte_count": None,
            "top_level_keys": [],
            "sample_count": None,
            "body_omitted": True,
        },
        "trace_integrity_postures": {
            field: False for field in TRACE_INTEGRITY_POSTURE_KEYS
        },
        "ambiguity_postures": {
            field: False for field in AMBIGUITY_POSTURE_KEYS
        },
        "contradiction_postures": {
            field: False for field in CONTRADICTION_POSTURE_KEYS
        },
        "unresolved_postures": {
            field: False for field in UNRESOLVED_POSTURE_KEYS
        },
        "not_prepared_code": None,
        "not_prepared_reason": None,
        "archive_bytes_omitted": True,
        "text_component_bodies_omitted": True,
        "recorded_signal_body_omitted": True,
    }


def _not_prepared(
    state: dict[str, Any],
    code: str,
    reason: str,
) -> tuple[dict[str, Any], str, str]:
    state["not_prepared_code"] = code
    state["not_prepared_reason"] = reason
    state["ambiguity_postures"][
        "material_trace_ambiguity_present"
    ] = code in {
        "BOUNDED_COMPONENT_ABSENT",
        "BOUNDED_COMPONENT_UNREADABLE",
        "TEXT_COMPONENT_INVALID",
        "TIMESTAMP_INVALID",
        "RECORDED_SIGNAL_INVALID",
        "CANDIDATE_NOT_TRUTHFULLY_PREPARABLE",
    }
    state["unresolved_postures"][
        "trace_integrity_materially_unresolved"
    ] = state["ambiguity_postures"]["material_trace_ambiguity_present"]
    return state, code, reason


def _evaluate_bounded_source(
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], str | None, str | None]:
    state = _empty_evaluation()
    state["bounded_paths_validated"] = True
    trace = state["trace_integrity_postures"]
    trace["exact_boundary_reference_preserved"] = True
    trace["exact_capture_directory_reference_preserved"] = True
    trace["exact_component_references_preserved"] = True
    trace["complete_archive_not_embedded"] = True
    trace["complete_signal_body_not_embedded"] = True

    capture_dir = _as_repo_path(
        BOUNDED_SOURCE_REFERENCES["bounded_capture_directory_path"]
    )
    if not capture_dir.is_dir():
        return _not_prepared(
            state,
            "BOUNDED_COMPONENT_ABSENT",
            "exact bounded capture directory is absent",
        )

    archive_path = _as_repo_path(
        BOUNDED_SOURCE_REFERENCES["preserved_archive_path"]
    )
    state["archive"]["regular_file"] = archive_path.is_file()
    if not archive_path.is_file():
        return _not_prepared(
            state,
            "BOUNDED_COMPONENT_ABSENT",
            "exact preserved archive is absent",
        )
    computed_hash, byte_count, hash_error = _sha256_file(archive_path)
    if hash_error is not None or computed_hash is None:
        return _not_prepared(
            state,
            "BOUNDED_COMPONENT_UNREADABLE",
            "exact preserved archive is unreadable",
        )
    state["archive"]["computed_sha256"] = computed_hash
    state["archive"]["byte_count"] = byte_count

    hash_path = _as_repo_path(
        BOUNDED_SOURCE_REFERENCES["archive_hash_record_path"]
    )
    state["hash_record"]["regular_file"] = hash_path.is_file()
    hash_text, hash_text_error = _read_text(
        BOUNDED_SOURCE_REFERENCES["archive_hash_record_path"]
    )
    if hash_text_error == "not_a_file":
        return _not_prepared(
            state,
            "BOUNDED_COMPONENT_ABSENT",
            "exact archive hash record is absent",
        )
    if hash_text_error is not None or hash_text is None:
        return _not_prepared(
            state,
            "BOUNDED_COMPONENT_UNREADABLE",
            "exact archive hash record is unreadable",
        )
    state["hash_record"]["readable"] = True
    match = _HASH_RECORD_PATTERN.fullmatch(hash_text)
    if match is None:
        state["contradiction_postures"][
            "archive_correspondence_contradicted"
        ] = True
        state["contradiction_postures"][
            "material_trace_contradiction_present"
        ] = True
        return _not_prepared(
            state,
            "ARCHIVE_HASH_RECORD_MALFORMED",
            "archive hash record is not in the exact bounded format",
        )
    record_hash = match.group(1)
    state["hash_record"]["parsed_sha256"] = record_hash
    state["archive_hash_record_validated"] = True
    correspondence = (
        computed_hash == record_hash == EXPECTED_ARCHIVE_SHA256
    )
    state["archive_correspondence_validated"] = correspondence
    trace["archive_correspondence_claimed"] = correspondence
    if not correspondence:
        state["contradiction_postures"][
            "archive_correspondence_contradicted"
        ] = True
        state["contradiction_postures"][
            "material_trace_contradiction_present"
        ] = True
        return _not_prepared(
            state,
            "ARCHIVE_HASH_MISMATCH",
            "computed, recorded, and expected archive hashes do not agree",
        )

    text_metadata: dict[str, dict[str, Any]] = {}
    timestamp_text: str | None = None
    for field in TEXT_COMPONENT_FIELDS:
        relative = BOUNDED_SOURCE_REFERENCES[field]
        path = _as_repo_path(relative)
        metadata: dict[str, Any] = {
            "path": relative,
            "regular_file": path.is_file(),
            "readable": False,
            "byte_count": None,
            "non_empty": False,
        }
        text_metadata[field] = metadata
        text, error = _read_text(relative)
        if error == "not_a_file":
            state["text_components"] = text_metadata
            return _not_prepared(
                state,
                "BOUNDED_COMPONENT_ABSENT",
                "exact required text component is absent: " + field,
            )
        if error is not None or text is None:
            state["text_components"] = text_metadata
            return _not_prepared(
                state,
                "BOUNDED_COMPONENT_UNREADABLE",
                "exact required text component is unreadable: " + field,
            )
        metadata["readable"] = True
        metadata["byte_count"] = len(text.encode("utf-8"))
        metadata["non_empty"] = bool(text.strip())
        if not metadata["non_empty"]:
            state["text_components"] = text_metadata
            return _not_prepared(
                state,
                "TEXT_COMPONENT_INVALID",
                "exact required text component is empty: " + field,
            )
        if field == "attestation_timestamp_path":
            timestamp_text = text
    state["text_components"] = text_metadata
    state["required_text_components_validated"] = True
    trace["required_text_components_declared_complete"] = True

    timestamp, timestamp_valid = _timestamp_metadata(timestamp_text or "")
    state["timestamp"] = timestamp
    state["timestamp_validated"] = timestamp_valid
    state["ambiguity_postures"][
        "timestamp_interpretation_ambiguous"
    ] = not timestamp_valid
    if not timestamp_valid:
        return _not_prepared(
            state,
            "TIMESTAMP_INVALID",
            "exact attestation timestamp is not valid RFC3339 UTC posture",
        )

    signal_relative = BOUNDED_SOURCE_REFERENCES["recorded_signal_path"]
    signal_path = _as_repo_path(signal_relative)
    signal_metadata = state["recorded_signal"]
    signal_metadata["regular_file"] = signal_path.is_file()
    signal_text, signal_error = _read_text(signal_relative)
    if signal_error == "not_a_file":
        return _not_prepared(
            state,
            "BOUNDED_COMPONENT_ABSENT",
            "exact recorded-signal artifact is absent",
        )
    if signal_error is not None or signal_text is None:
        return _not_prepared(
            state,
            "BOUNDED_COMPONENT_UNREADABLE",
            "exact recorded-signal artifact is unreadable",
        )
    signal_metadata["readable"] = True
    signal_metadata["byte_count"] = len(signal_text.encode("utf-8"))
    signal, signal_parse_error = _loads_json(signal_text)
    if signal_parse_error is not None or not isinstance(signal, Mapping):
        return _not_prepared(
            state,
            "RECORDED_SIGNAL_INVALID",
            "recorded-signal artifact is not strict mapping JSON",
        )
    signal_metadata["parseable"] = True
    signal_metadata["mapping"] = True
    signal_metadata["top_level_keys"] = sorted(signal)
    samples = signal.get("samples")
    signal_metadata["sample_count"] = (
        len(samples)
        if isinstance(samples, Sequence)
        and not isinstance(samples, (str, bytes, bytearray))
        else None
    )
    numeric = lambda value: type(value) in (int, float)
    minimum_structure = (
        _SIGNAL_REQUIRED_KEYS.issubset(signal)
        and isinstance(signal.get("recorded_at"), str)
        and bool(signal.get("recorded_at"))
        and numeric(signal.get("duration_s"))
        and numeric(signal.get("sample_rate_hz"))
        and isinstance(signal.get("units"), str)
        and bool(signal.get("units"))
        and isinstance(signal.get("device"), Mapping)
        and isinstance(samples, Sequence)
        and not isinstance(samples, (str, bytes, bytearray))
        and len(samples) > 0
    )
    signal_metadata["minimum_structure_validated"] = minimum_structure
    if not minimum_structure:
        return _not_prepared(
            state,
            "RECORDED_SIGNAL_INVALID",
            "recorded-signal artifact lacks the minimum bounded structure",
        )
    state["recorded_signal_artifact_validated"] = True
    trace["recorded_signal_artifact_declared_present"] = True

    state["required_bounded_components_available"] = True
    state["complete_21_field_candidate_preparable"] = True
    checks.append(_check("bounded_source_evaluation_completed", True))
    return state, None, None


def _build_candidate(evaluation: Mapping[str, Any]) -> dict[str, Any]:
    candidate: dict[str, Any] = {
        field: value for field, value in BOUNDED_SOURCE_REFERENCES.items()
    }
    candidate.update(
        {
            "evaluator_reference": (
                RESOLVER_MODULE
                + ":"
                + PREPARATION_ID
                + ":"
                + PREPARATION_RESULT_PREPARED
            ),
            "trace_integrity_postures": copy.deepcopy(
                dict(_mapping(evaluation.get("trace_integrity_postures")))
            ),
            "ambiguity_postures": copy.deepcopy(
                dict(_mapping(evaluation.get("ambiguity_postures")))
            ),
            "contradiction_postures": copy.deepcopy(
                dict(_mapping(evaluation.get("contradiction_postures")))
            ),
            "unresolved_postures": copy.deepcopy(
                dict(_mapping(evaluation.get("unresolved_postures")))
            ),
            "non_conversion_statement": NON_CONVERSION_STATEMENT,
            "basis_non_claims": _canonical_basis_non_claims(),
        }
    )
    return candidate


def _candidate_valid(candidate: Any) -> bool:
    if not isinstance(candidate, Mapping) or set(candidate) != set(
        CANDIDATE_FIELDS
    ):
        return False
    if any(
        candidate.get(field) != expected
        for field, expected in BOUNDED_SOURCE_REFERENCES.items()
    ):
        return False
    evaluator = candidate.get("evaluator_reference")
    if (
        not isinstance(evaluator, str)
        or not evaluator
        or len(evaluator) > 1024
        or RESOLVER_MODULE not in evaluator
        or PREPARATION_ID not in evaluator
        or PREPARATION_RESULT_PREPARED not in evaluator
    ):
        return False
    for family, keys in POSTURE_KEY_FAMILIES.items():
        if not _exact_boolean_mapping(candidate.get(family), keys):
            return False
    return (
        candidate.get("non_conversion_statement")
        == NON_CONVERSION_STATEMENT
        and _exact_false_mapping(
            candidate.get("basis_non_claims"),
            REQUIRED_BASIS_NON_CLAIMS,
        )
    )


def _safe_declared_request(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "intent": request.get("intent"),
        **{
            field: request.get(field)
            for field in _expected_request_values()
        },
        "bounded_source_references": (
            _canonical_bounded_source_references()
            if request.get("bounded_source_references")
            == BOUNDED_SOURCE_REFERENCES
            else None
        ),
        REQUEST_SELECTION_FIELD: (
            request.get(REQUEST_SELECTION_FIELD)
            if _exact_bool(request.get(REQUEST_SELECTION_FIELD))
            else False
        ),
        "declared_non_claims_validated": _exact_false_mapping(
            request.get("declared_non_claims"),
            REQUEST_REQUIRED_FALSE_NON_CLAIMS,
        ),
        "prohibited_input_flags_validated": all(
            request.get(field) is False for field in PROHIBITED_INPUT_FLAGS
        ),
    }


def _state(
    outcome: str,
    preparation_result: str,
    request: Mapping[str, Any],
    *,
    specification_validated: bool,
    preparation_request_validated: bool,
    boundary_validated: bool,
    evaluation: Mapping[str, Any],
    decision_code: str,
    decision_reason: str,
) -> dict[str, Any]:
    completed = outcome in {OUTCOME_PREPARED, OUTCOME_NOT_PREPARED}
    prepared = outcome == OUTCOME_PREPARED
    state: dict[str, Any] = {
        "preparation_id": PREPARATION_ID,
        "preparation_type": PREPARATION_TYPE,
        "preparation_version": PREPARATION_VERSION,
        "preparation_scope": PREPARATION_SCOPE,
        "selected_preparation_request_id": SELECTED_PREPARATION_REQUEST_ID,
        "selected_receiver_attestation_operation_id": OPERATION_ID,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        REQUEST_SELECTION_FIELD: (
            request.get(REQUEST_SELECTION_FIELD)
            if _exact_bool(request.get(REQUEST_SELECTION_FIELD))
            else False
        ),
        "preparation_result": preparation_result,
        "decision_code": decision_code,
        "decision_reason": decision_reason,
        "specification_markers_validated": specification_validated,
        "preparation_request_artifact_validated": (
            preparation_request_validated
        ),
        "selected_boundary_reference_validated": boundary_validated,
        "bounded_paths_validated": evaluation.get(
            "bounded_paths_validated"
        )
        is True,
        "required_bounded_components_available": evaluation.get(
            "required_bounded_components_available"
        )
        is True,
        "archive_hash_record_validated": evaluation.get(
            "archive_hash_record_validated"
        )
        is True,
        "archive_correspondence_validated": evaluation.get(
            "archive_correspondence_validated"
        )
        is True,
        "required_text_components_validated": evaluation.get(
            "required_text_components_validated"
        )
        is True,
        "timestamp_validated": evaluation.get("timestamp_validated") is True,
        "recorded_signal_artifact_validated": evaluation.get(
            "recorded_signal_artifact_validated"
        )
        is True,
        "complete_21_field_candidate_prepared": prepared,
        "preparation_recorded": completed,
        "preparation_result_recorded": completed,
        "preparation_exhausted": completed,
        "basis_declaration_preparation_started": completed,
        "basis_declaration_preparation_completed": completed,
        "receiver_attestation_operation_basis_declaration_candidate_prepared": (
            prepared
        ),
        "receiver_attestation_operation_basis_prepared": prepared,
        "receiver_attestation_operation_basis_declared": False,
        "receiver_attestation_operation_basis_supplied": False,
        "receiver_attestation_operation_basis_admitted": False,
        "receiver_attestation_operation_recorded": False,
        "receiver_attestation_operation_result_recorded": False,
        "receiver_attestation_operation_exhausted": False,
        "receiver_attestation_decided": False,
        **_canonical_result_non_claims(),
        **{field: True for field in RESULT_OMISSION_FIELDS},
    }
    return state


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    state = _mapping(result.get(PREFIX))
    decision = _mapping(result.get("preparation_decision"))
    archive = _mapping(result.get("archive_correspondence_metadata"))
    timestamp = _mapping(result.get("timestamp_metadata"))
    signal = _mapping(result.get("recorded_signal_metadata"))
    omission = _mapping(result.get("omission_posture"))
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "preparation_id": state.get("preparation_id"),
        "preparation_type": state.get("preparation_type"),
        "preparation_version": state.get("preparation_version"),
        "preparation_scope": state.get("preparation_scope"),
        "selected_preparation_request_id": state.get(
            "selected_preparation_request_id"
        ),
        "selected_operation_id": state.get(
            "selected_receiver_attestation_operation_id"
        ),
        "selected_candidate_id": state.get(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "governing_specification_path": str(
            GOVERNING_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_preparation_request_artifact_path": str(
            SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH
        ),
        "outcome": result.get("outcome"),
        "preparation_result": state.get("preparation_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": _mapping(result.get("block")).get("blocked"),
        "decision_code": decision.get("code"),
        "decision_reason": decision.get("reason"),
        "preparation_selection": state.get(REQUEST_SELECTION_FIELD),
        "specification_markers_validated": state.get(
            "specification_markers_validated"
        ),
        "preparation_request_artifact_validated": state.get(
            "preparation_request_artifact_validated"
        ),
        "selected_boundary_reference_validated": state.get(
            "selected_boundary_reference_validated"
        ),
        "bounded_paths_validated": state.get("bounded_paths_validated"),
        "required_bounded_components_available": state.get(
            "required_bounded_components_available"
        ),
        "archive_hash_record_validated": state.get(
            "archive_hash_record_validated"
        ),
        "computed_archive_sha256": archive.get("computed_sha256"),
        "archive_correspondence_validated": state.get(
            "archive_correspondence_validated"
        ),
        "archive_correspondence_contradicted": archive.get(
            "correspondence_contradicted"
        ),
        "required_text_components_validated": state.get(
            "required_text_components_validated"
        ),
        "timestamp_validated": state.get("timestamp_validated"),
        "timestamp_ambiguous": timestamp.get(
            "timestamp_interpretation_ambiguous"
        ),
        "recorded_signal_artifact_validated": state.get(
            "recorded_signal_artifact_validated"
        ),
        "recorded_signal_sample_count": signal.get("sample_count"),
        "complete_21_field_candidate_prepared": state.get(
            "complete_21_field_candidate_prepared"
        ),
        "preparation_recorded": state.get("preparation_recorded"),
        "preparation_result_recorded": state.get(
            "preparation_result_recorded"
        ),
        "preparation_exhausted": state.get("preparation_exhausted"),
        "basis_declaration_preparation_started": state.get(
            "basis_declaration_preparation_started"
        ),
        "basis_declaration_preparation_completed": state.get(
            "basis_declaration_preparation_completed"
        ),
        "declaration_candidate_prepared": state.get(
            "receiver_attestation_operation_basis_declaration_"
            "candidate_prepared"
        ),
        "operation_basis_prepared": state.get(
            "receiver_attestation_operation_basis_prepared"
        ),
        "operation_basis_declared": state.get(
            "receiver_attestation_operation_basis_declared"
        ),
        "operation_basis_supplied": state.get(
            "receiver_attestation_operation_basis_supplied"
        ),
        "operation_basis_admitted": state.get(
            "receiver_attestation_operation_basis_admitted"
        ),
        "operation_recorded": state.get(
            "receiver_attestation_operation_recorded"
        ),
        "operation_result_recorded": state.get(
            "receiver_attestation_operation_result_recorded"
        ),
        "operation_exhausted": state.get(
            "receiver_attestation_operation_exhausted"
        ),
        "receiver_attestation_recorded": state.get(
            "receiver_attestation_recorded"
        ),
        "result_level_non_claims_canonical_false": (
            _exact_false_mapping(
                result.get("non_claims"),
                REQUIRED_FALSE_NON_CLAIMS,
            )
        ),
        "complete_material_omitted": all(
            omission.get(field) is True for field in RESULT_OMISSION_FIELDS
        ),
    }


def _result(
    request: Mapping[str, Any],
    outcome: str,
    preparation_result: str,
    checks: list[dict[str, Any]],
    *,
    specification_validation: Mapping[str, Any] | None = None,
    preparation_request_validation: Mapping[str, Any] | None = None,
    boundary_validation: Mapping[str, Any] | None = None,
    evaluation: Mapping[str, Any] | None = None,
    candidate: Mapping[str, Any] | None = None,
    decision_code: str,
    decision_reason: str,
    block_code: str | None = None,
) -> dict[str, Any]:
    specification = copy.deepcopy(dict(specification_validation or {}))
    preparation_request = copy.deepcopy(
        dict(preparation_request_validation or {})
    )
    boundary = copy.deepcopy(dict(boundary_validation or {}))
    evaluated = copy.deepcopy(dict(evaluation or _empty_evaluation()))
    state = _state(
        outcome,
        preparation_result,
        request,
        specification_validated=(
            specification.get("specification_markers_validated") is True
        ),
        preparation_request_validated=(
            preparation_request.get(
                "preparation_request_artifact_validated"
            )
            is True
        ),
        boundary_validated=(
            boundary.get("selected_boundary_reference_validated") is True
        ),
        evaluation=evaluated,
        decision_code=decision_code,
        decision_reason=decision_reason,
    )
    archive = _mapping(evaluated.get("archive"))
    hash_record = _mapping(evaluated.get("hash_record"))
    timestamp = _mapping(evaluated.get("timestamp"))
    signal = _mapping(evaluated.get("recorded_signal"))
    omission = {field: True for field in RESULT_OMISSION_FIELDS}
    result: dict[str, Any] = {
        f"{PREFIX}_metadata": {
            "preparation_id": PREPARATION_ID,
            "preparation_type": PREPARATION_TYPE,
            "preparation_version": PREPARATION_VERSION,
            "preparation_scope": PREPARATION_SCOPE,
        },
        f"declared_{PREFIX}": _safe_declared_request(request),
        "selected_preparation_request_operation_candidate_identity": {
            "selected_preparation_request_id": (
                SELECTED_PREPARATION_REQUEST_ID
            ),
            "selected_preparation_request_type": (
                SELECTED_PREPARATION_REQUEST_TYPE
            ),
            "selected_preparation_request_version": (
                SELECTED_PREPARATION_REQUEST_VERSION
            ),
            "selected_preparation_request_scope": (
                SELECTED_PREPARATION_REQUEST_SCOPE
            ),
            "selected_operation_id": OPERATION_ID,
            "selected_operation_type": OPERATION_TYPE,
            "selected_operation_version": OPERATION_VERSION,
            "selected_operation_scope": OPERATION_SCOPE,
            "selected_candidate_id": CANDIDATE_ID,
            "selected_candidate_type": CANDIDATE_TYPE,
            "selected_candidate_scope": CANDIDATE_SCOPE,
            "governing_specification_path": str(
                GOVERNING_SPECIFICATION_RELATIVE_PATH
            ),
            "selected_preparation_request_artifact_path": str(
                SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH
            ),
        },
        "specification_marker_validation": specification,
        "preparation_request_artifact_validation": preparation_request,
        "selected_boundary_reference_validation": boundary,
        "bounded_path_and_file_evaluation": {
            "bounded_paths_validated": evaluated.get(
                "bounded_paths_validated"
            ),
            "required_bounded_components_available": evaluated.get(
                "required_bounded_components_available"
            ),
            "complete_21_field_candidate_preparable": evaluated.get(
                "complete_21_field_candidate_preparable"
            ),
            "not_prepared_code": evaluated.get("not_prepared_code"),
            "not_prepared_reason": evaluated.get("not_prepared_reason"),
            "trace_integrity_postures": copy.deepcopy(
                evaluated.get("trace_integrity_postures", {})
            ),
            "ambiguity_postures": copy.deepcopy(
                evaluated.get("ambiguity_postures", {})
            ),
            "contradiction_postures": copy.deepcopy(
                evaluated.get("contradiction_postures", {})
            ),
            "unresolved_postures": copy.deepcopy(
                evaluated.get("unresolved_postures", {})
            ),
        },
        "archive_correspondence_metadata": {
            "path": archive.get("path"),
            "regular_file": archive.get("regular_file"),
            "byte_count": archive.get("byte_count"),
            "computed_sha256": archive.get("computed_sha256"),
            "expected_sha256": archive.get("expected_sha256"),
            "hash_record_path": hash_record.get("path"),
            "hash_record_regular_file": hash_record.get("regular_file"),
            "hash_record_readable": hash_record.get("readable"),
            "hash_record_sha256": hash_record.get("parsed_sha256"),
            "hash_record_validated": evaluated.get(
                "archive_hash_record_validated"
            ),
            "correspondence_validated": evaluated.get(
                "archive_correspondence_validated"
            ),
            "correspondence_contradicted": _mapping(
                evaluated.get("contradiction_postures")
            ).get("archive_correspondence_contradicted", False),
            "archive_bytes_omitted": True,
            "hash_record_body_omitted": True,
        },
        "text_component_metadata": {
            "components": copy.deepcopy(
                evaluated.get("text_components", {})
            ),
            "required_text_components_validated": evaluated.get(
                "required_text_components_validated"
            ),
            "text_component_bodies_omitted": True,
        },
        "timestamp_metadata": copy.deepcopy(dict(timestamp)),
        "recorded_signal_metadata": copy.deepcopy(dict(signal)),
        "preparation_decision": {
            "code": decision_code,
            "reason": decision_reason,
            "precedence": (
                "BLOCKED_THEN_NOT_PREPARED_THEN_PREPARED"
            ),
            "caller_selected_result": False,
        },
        "prepared_declaration_candidate": (
            copy.deepcopy(dict(candidate))
            if outcome == OUTCOME_PREPARED and candidate is not None
            else None
        ),
        PREFIX: state,
        f"{PREFIX}_checks": copy.deepcopy(checks),
        f"{PREFIX}_statement": {
            "preparation_records_one_candidate_only": (
                outcome == OUTCOME_PREPARED
            ),
            "prepared_candidate_is_not_declared_basis": True,
            "declared_basis_is_not_supplied_basis": True,
            "supplied_basis_is_not_admitted_basis": True,
            "admitted_basis_is_not_operation_execution": True,
            "operation_execution_is_not_operation_result": True,
            "archive_correspondence_is_not_occurrence_verification": True,
            "open_does_not_mean_next": True,
        },
        f"{PREFIX}_non_meaning": {
            "preparation_does_not_create_occurrence": True,
            "preparation_does_not_verify_identity_custody_or_provenance": True,
            "preparation_does_not_establish_presence_truth_authority_or_standing": True,
            "not_prepared_is_not_operation_not_recorded": True,
            "not_prepared_is_not_operation_indeterminate": True,
            "completion_does_not_authorize_declaration_or_execution": True,
        },
        "blocked_routes": list(BLOCKED_ROUTES),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_result_non_claims(),
        "omission_posture": omission,
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "block_code": (
                block_code if outcome == OUTCOME_BLOCKED else None
            ),
            "reason": (
                decision_reason if outcome == OUTCOME_BLOCKED else None
            ),
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


def resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded preparation without declaring or supplying basis."""
    if request is None:
        working: Mapping[str, Any] = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_request()
        )
    elif not isinstance(request, Mapping):
        baseline = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_request()
        )
        checks = [_check("request_is_mapping", False, "REQUEST_NOT_MAPPING")]
        return _result(
            baseline,
            OUTCOME_BLOCKED,
            PREPARATION_RESULT_NOT_EVALUATED,
            checks,
            decision_code="REQUEST_NOT_MAPPING",
            decision_reason="request is not a mapping",
            block_code="REQUEST_NOT_MAPPING",
        )
    else:
        working = copy.deepcopy(dict(request))

    checks: list[dict[str, Any]] = []
    code, reason = _validate_request(working, checks)
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            PREPARATION_RESULT_NOT_EVALUATED,
            checks,
            decision_code=code,
            decision_reason=reason or "request validation failed",
            block_code=code,
        )

    specification, code, reason = _validate_specification(checks)
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            PREPARATION_RESULT_NOT_EVALUATED,
            checks,
            specification_validation=specification,
            decision_code=code,
            decision_reason=reason or "specification validation failed",
            block_code=code,
        )

    preparation_request, code, reason = (
        _validate_preparation_request_artifact(checks)
    )
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            PREPARATION_RESULT_NOT_EVALUATED,
            checks,
            specification_validation=specification,
            preparation_request_validation=preparation_request,
            decision_code=code,
            decision_reason=reason or "preparation request validation failed",
            block_code=code,
        )

    boundary, code, reason = _validate_selected_boundary(checks)
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            PREPARATION_RESULT_NOT_EVALUATED,
            checks,
            specification_validation=specification,
            preparation_request_validation=preparation_request,
            boundary_validation=boundary,
            decision_code=code,
            decision_reason=reason or "boundary validation failed",
            block_code=code,
        )

    if working.get(REQUEST_SELECTION_FIELD) is False:
        evaluation = _empty_evaluation()
        evaluation["not_prepared_code"] = "PREPARATION_NOT_SELECTED"
        evaluation["not_prepared_reason"] = (
            "bounded preparation was not selected"
        )
        checks.append(_check("preparation_selection_resolved", True))
        return _result(
            working,
            OUTCOME_NOT_PREPARED,
            PREPARATION_RESULT_NOT_PREPARED,
            checks,
            specification_validation=specification,
            preparation_request_validation=preparation_request,
            boundary_validation=boundary,
            evaluation=evaluation,
            decision_code="PREPARATION_NOT_SELECTED",
            decision_reason="bounded preparation was not selected",
        )

    evaluation, not_prepared_code, not_prepared_reason = (
        _evaluate_bounded_source(checks)
    )
    if not_prepared_code is not None:
        checks.append(_check("bounded_evaluation_completed_truthfully", True))
        return _result(
            working,
            OUTCOME_NOT_PREPARED,
            PREPARATION_RESULT_NOT_PREPARED,
            checks,
            specification_validation=specification,
            preparation_request_validation=preparation_request,
            boundary_validation=boundary,
            evaluation=evaluation,
            decision_code=not_prepared_code,
            decision_reason=(
                not_prepared_reason
                or "complete candidate cannot be prepared truthfully"
            ),
        )

    candidate = _build_candidate(evaluation)
    if not _candidate_valid(candidate):
        evaluation["complete_21_field_candidate_preparable"] = False
        evaluation["not_prepared_code"] = (
            "CANDIDATE_NOT_TRUTHFULLY_PREPARABLE"
        )
        evaluation["not_prepared_reason"] = (
            "exact 21-field candidate could not be constructed"
        )
        checks.append(_check("candidate_construction_evaluated", True))
        return _result(
            working,
            OUTCOME_NOT_PREPARED,
            PREPARATION_RESULT_NOT_PREPARED,
            checks,
            specification_validation=specification,
            preparation_request_validation=preparation_request,
            boundary_validation=boundary,
            evaluation=evaluation,
            decision_code="CANDIDATE_NOT_TRUTHFULLY_PREPARABLE",
            decision_reason=(
                "exact 21-field candidate could not be constructed"
            ),
        )

    checks.append(_check("complete_21_field_candidate_prepared", True))
    return _result(
        working,
        OUTCOME_PREPARED,
        PREPARATION_RESULT_PREPARED,
        checks,
        specification_validation=specification,
        preparation_request_validation=preparation_request,
        boundary_validation=boundary,
        evaluation=evaluation,
        candidate=candidate,
        decision_code="CANDIDATE_PREPARED",
        decision_reason="one complete truthful declaration candidate prepared",
    )


def resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Load one explicit strict JSON mapping and resolve it."""
    value, error = _read_json(request_path)
    if error is not None or not isinstance(value, Mapping):
        baseline = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_request()
        )
        checks = [_check("request_path_is_mapping_json", False, "REQUEST_NOT_MAPPING")]
        return _result(
            baseline,
            OUTCOME_BLOCKED,
            PREPARATION_RESULT_NOT_EVALUATED,
            checks,
            decision_code="REQUEST_NOT_MAPPING",
            decision_reason=(
                "request path is unavailable, duplicated, unparseable, "
                "or not a mapping"
            ),
            block_code="REQUEST_NOT_MAPPING",
        )
    return resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min(
        value
    )


def build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic preparation summary."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    return _summary_from_result(result)


def _contains_forbidden_material(value: Any) -> bool:
    if isinstance(value, Mapping):
        if not set(value).isdisjoint(FORBIDDEN_PAYLOAD_KEYS):
            return True
        return any(_contains_forbidden_material(item) for item in value.values())
    if isinstance(value, Sequence) and not isinstance(
        value,
        (str, bytes, bytearray),
    ):
        return any(_contains_forbidden_material(item) for item in value)
    return isinstance(value, (bytes, bytearray))


def _branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    state = _mapping(result.get(PREFIX))
    block = _mapping(result.get("block"))
    candidate = result.get("prepared_declaration_candidate")
    decision = _mapping(result.get("preparation_decision"))
    omission = _mapping(result.get("omission_posture"))
    if (
        outcome not in OUTCOME_FAMILY
        or state.get("preparation_id") != PREPARATION_ID
        or state.get("preparation_type") != PREPARATION_TYPE
        or state.get("preparation_version") != PREPARATION_VERSION
        or state.get("preparation_scope") != PREPARATION_SCOPE
        or state.get("selected_preparation_request_id")
        != SELECTED_PREPARATION_REQUEST_ID
        or state.get("selected_receiver_attestation_operation_id")
        != OPERATION_ID
        or state.get("receiver_side_answerable_basis_candidate_id")
        != CANDIDATE_ID
        or not _exact_false_mapping(
            result.get("non_claims"),
            REQUIRED_FALSE_NON_CLAIMS,
        )
        or any(
            state.get(field) is not False
            for field in REQUIRED_FALSE_NON_CLAIMS
        )
        or any(
            omission.get(field) is not True
            or state.get(field) is not True
            for field in RESULT_OMISSION_FIELDS
        )
        or decision.get("caller_selected_result") is not False
    ):
        return False

    downstream_false = (
        "receiver_attestation_operation_basis_declared",
        "receiver_attestation_operation_basis_supplied",
        "receiver_attestation_operation_basis_admitted",
        "receiver_attestation_operation_recorded",
        "receiver_attestation_operation_result_recorded",
        "receiver_attestation_operation_exhausted",
        "receiver_attestation_decided",
    )
    if any(state.get(field) is not False for field in downstream_false):
        return False

    if outcome == OUTCOME_PREPARED:
        return (
            state.get("preparation_result") == PREPARATION_RESULT_PREPARED
            and block.get("blocked") is False
            and block.get("code") is None
            and state.get("preparation_recorded") is True
            and state.get("preparation_result_recorded") is True
            and state.get("preparation_exhausted") is True
            and state.get("basis_declaration_preparation_started") is True
            and state.get("basis_declaration_preparation_completed") is True
            and state.get(
                "receiver_attestation_operation_basis_declaration_"
                "candidate_prepared"
            )
            is True
            and state.get("receiver_attestation_operation_basis_prepared")
            is True
            and _candidate_valid(candidate)
        )
    if outcome == OUTCOME_NOT_PREPARED:
        return (
            state.get("preparation_result")
            == PREPARATION_RESULT_NOT_PREPARED
            and block.get("blocked") is False
            and block.get("code") is None
            and state.get("preparation_recorded") is True
            and state.get("preparation_result_recorded") is True
            and state.get("preparation_exhausted") is True
            and state.get("basis_declaration_preparation_started") is True
            and state.get("basis_declaration_preparation_completed") is True
            and state.get(
                "receiver_attestation_operation_basis_declaration_"
                "candidate_prepared"
            )
            is False
            and state.get("receiver_attestation_operation_basis_prepared")
            is False
            and candidate is None
            and decision.get("code") in NOT_PREPARED_CODES
        )
    return (
        state.get("preparation_result") == PREPARATION_RESULT_NOT_EVALUATED
        and state.get("preparation_recorded") is False
        and state.get("preparation_result_recorded") is False
        and state.get("preparation_exhausted") is False
        and state.get("basis_declaration_preparation_started") is False
        and state.get("basis_declaration_preparation_completed") is False
        and state.get(
            "receiver_attestation_operation_basis_declaration_"
            "candidate_prepared"
        )
        is False
        and state.get("receiver_attestation_operation_basis_prepared")
        is False
        and candidate is None
        and block.get("blocked") is True
        and block.get("code") in BLOCK_CODES
        and block.get("block_code") == block.get("code")
        and isinstance(block.get("reason"), str)
        and bool(block.get("reason"))
    )


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(
            f"{path.stem}_{index:03d}{path.suffix}"
        )
        if not candidate.exists():
            return candidate
    raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationV0MinError(
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
            REPO_ROOT / SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH
        ).parent.resolve(strict=False),
        (
            REPO_ROOT / SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
        ).parent.resolve(strict=False),
        (
            REPO_ROOT / SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH
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
        ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationV0MinError
    )
    if set(result) != RESULT_SECTIONS:
        raise error("WRITE_REFUSED: result sections are incomplete or unexpected")
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
    ):
        raise error("WRITE_REFUSED: incompatible result metadata")
    checks = result.get(f"{PREFIX}_checks")
    if not isinstance(checks, list) or not all(
        isinstance(check, Mapping)
        and type(check.get("passed")) is bool
        for check in checks
    ):
        raise error("WRITE_REFUSED: checks are malformed")
    for check in checks:
        for field in ("failure_code", "block_code"):
            if (
                check.get(field) is not None
                and check.get(field) not in BLOCK_CODES
            ):
                raise error("WRITE_REFUSED: check contains a non-public code")
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
    if _contains_forbidden_material(result):
        raise error("WRITE_REFUSED: complete or forbidden source material present")
    summary = result.get(f"{PREFIX}_summary")
    if (
        not isinstance(summary, Mapping)
        or dict(summary) != _summary_from_result(result)
    ):
        raise error("WRITE_REFUSED: summary is inconsistent")
    if not _bounded_json(result) or _serialized_size(result) is None:
        raise error("WRITE_REFUSED: result is not bounded JSON")


def write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid preparation result without silent overwrite."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    _validate_write_result(result)
    target = (
        _as_repo_path(output_path)
        if output_path is not None
        else OUTPUT_ROOT / OUTPUT_FILENAME
    )
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationV0MinError(
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
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationV0MinError(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
