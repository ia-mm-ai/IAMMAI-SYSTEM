"""Declare one exact prepared receiver-attestation operation basis.

The resolver consumes one exact PREPARED preparation artifact and may record
its exact 21-field candidate as declared basis. It does not reread capture
material, supply or admit basis, execute the operation, or create downstream
standing.
"""

from __future__ import annotations

import copy
import hashlib
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from types import MappingProxyType
from typing import Any


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_receiver_attestation_operation_"
    "basis_declaration_v0_min"
)

DECLARATION_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_001"
)
DECLARATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION"
)
DECLARATION_VERSION = "0.1.0"
DECLARATION_SCOPE = (
    "DECLARE_ONE_EXACT_PREPARED_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "CANDIDATE_ONLY"
)

SELECTED_PREPARATION_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_001"
)
SELECTED_PREPARATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION"
)
SELECTED_PREPARATION_VERSION = "0.1.0"
SELECTED_PREPARATION_SCOPE = (
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

PREPARATION_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_receiver_attestation_operation_"
    "basis_declaration_preparation_v0_min"
)
PREPARATION_RESULT_VERSION = "0.1.0"
PREPARATION_OUTCOME_PREPARED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_PREPARATION_PREPARED"
)
PREPARATION_RESULT_PREPARED = (
    "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_CANDIDATE_PREPARED"
)
PREPARATION_DECISION_CODE = "CANDIDATE_PREPARED"

OUTCOME_DECLARED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_DECLARED"
)
OUTCOME_NOT_DECLARED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_NOT_DECLARED"
)
OUTCOME_BLOCKED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_DECLARED,
    OUTCOME_NOT_DECLARED,
    OUTCOME_BLOCKED,
)

DECLARATION_RESULT_DECLARED = "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARED"
DECLARATION_RESULT_NOT_DECLARED = (
    "RECEIVER_ATTESTATION_OPERATION_BASIS_NOT_DECLARED"
)
DECLARATION_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
DECLARATION_RESULT_FAMILY = (
    DECLARATION_RESULT_DECLARED,
    DECLARATION_RESULT_NOT_DECLARED,
    DECLARATION_RESULT_NOT_EVALUATED,
)
RESULT_FAMILY = DECLARATION_RESULT_FAMILY

REQUEST_SELECTION_FIELD = "basis_declaration_selected"
CANDIDATE_DIGEST_ALGORITHM = "SHA-256"

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_DECLARATION_V0_MIN_SPEC.md"
)
SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_declaration_"
    "preparation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_001__receiver_side_answerable_basis_receiver_"
    "attestation_operation_basis_declaration_"
    "preparation_v0_min_result.json"
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
SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
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
SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_candidate_sufficiency_operation_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_"
    "operation_v0_min_result_001.json"
)
BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH = Path(
    "artifacts/actual_receiver_attestation_capture/"
    "receiver_attestation_capture_001"
)

GOVERNING_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
)
SELECTED_PREPARATION_ARTIFACT_PATH = (
    REPO_ROOT / SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH
)

OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_declaration_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_001__receiver_side_answerable_basis_receiver_attestation_"
    "operation_basis_declaration_v0_min_result.json"
)

EXPECTED_ARCHIVE_SHA256 = (
    "a45a621c5c6c2f37daefd7e896f32cdb50bff21ab69ec9281912049bd326724c"
)
EXACT_CANDIDATE_REFERENCES = MappingProxyType(
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

EXPECTED_EVALUATOR_REFERENCE = (
    "resolve_receiver_side_answerable_basis_receiver_attestation_operation_"
    "basis_declaration_preparation_v0_min:"
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_001:"
    "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_CANDIDATE_PREPARED"
)

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

EXPECTED_TRACE_INTEGRITY_POSTURES = MappingProxyType(
    {key: True for key in TRACE_INTEGRITY_POSTURE_KEYS}
)
EXPECTED_AMBIGUITY_POSTURES = MappingProxyType(
    {key: False for key in AMBIGUITY_POSTURE_KEYS}
)
EXPECTED_CONTRADICTION_POSTURES = MappingProxyType(
    {key: False for key in CONTRADICTION_POSTURE_KEYS}
)
EXPECTED_UNRESOLVED_POSTURES = MappingProxyType(
    {key: False for key in UNRESOLVED_POSTURE_KEYS}
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
    "permission_created",
    "reusable_receiver_attestation_operation_basis_declaration_"
    "route_created",
    "same_receiver_attestation_operation_basis_declaration_rerun_authorized",
    "automatic_receiver_attestation_operation_basis_declaration_"
    "retry_created",
    "receiver_attestation_operation_basis_declaration_debt_created",
    "receiver_attestation_operation_basis_declaration_obligation_created",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

EXTRA_REQUIRED_FALSE_POSTURES = (
    "receiver_attestation_operation_basis_supplied",
    "receiver_attestation_operation_basis_admitted",
    "receiver_attestation_operation_recorded",
    "receiver_attestation_operation_result_recorded",
    "receiver_attestation_operation_executed",
    "receiver_attestation_operation_exhausted",
    "receiver_attestation_decided",
    "custody_created",
    "provenance_created",
    "physical_validity_created",
)

REQUEST_REQUIRED_FALSE_NON_CLAIMS = tuple(
    dict.fromkeys(
        (
            *REQUIRED_FALSE_NON_CLAIMS,
            *EXTRA_REQUIRED_FALSE_POSTURES,
            "declaration_recorded",
            "declaration_result_recorded",
            "declaration_exhausted",
            "receiver_attestation_operation_basis_declaration_recorded",
            "receiver_attestation_operation_basis_declared",
        )
    )
)

UPSTREAM_PREPARATION_FALSE_NON_CLAIMS = (
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

PROHIBITED_INPUT_FLAGS = MappingProxyType(
    {
        "replacement_candidate_supplied": "PROHIBITED_CALLER_CANDIDATE",
        "candidate_digest_supplied": "PROHIBITED_CALLER_DIGEST",
        "candidate_posture_maps_supplied": (
            "PROHIBITED_CALLER_POSTURE_MAPS"
        ),
        "declaration_outcome_selected_by_caller": (
            "PROHIBITED_RESULT_PRECLAIM"
        ),
        "declaration_result_selected_by_caller": (
            "PROHIBITED_RESULT_PRECLAIM"
        ),
        "operation_outcome_selected_by_caller": (
            "PROHIBITED_RESULT_PRECLAIM"
        ),
        "operation_result_selected_by_caller": (
            "PROHIBITED_RESULT_PRECLAIM"
        ),
        "preparation_replay_requested": (
            "PROHIBITED_PREPARATION_OR_EVIDENCE_REEVALUATION"
        ),
        "evidence_reevaluation_requested": (
            "PROHIBITED_PREPARATION_OR_EVIDENCE_REEVALUATION"
        ),
        "archive_rehash_requested": (
            "PROHIBITED_PREPARATION_OR_EVIDENCE_REEVALUATION"
        ),
        "bounded_capture_read_requested": (
            "PROHIBITED_PREPARATION_OR_EVIDENCE_REEVALUATION"
        ),
        "basis_supply_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "basis_admission_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "operation_execution_preclaimed": (
            "PROHIBITED_DOWNSTREAM_CONVERSION"
        ),
        "operation_result_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "receiver_attestation_preclaimed": (
            "PROHIBITED_DOWNSTREAM_CONVERSION"
        ),
        "receiver_answerable_receipt_preclaimed": (
            "PROHIBITED_DOWNSTREAM_CONVERSION"
        ),
        "presence_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "identity_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "custody_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "provenance_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "physical_validity_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "authority_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "truth_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "standing_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "relation_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "coupling_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "runtime_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "api_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "output_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "action_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "synchronization_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "follow_on_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "repeat_permission_requested": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "reusable_route_requested": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "rerun_requested": "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION",
        "retry_requested": "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION",
        "debt_created": "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION",
        "obligation_created": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "scheduled_supply_requested": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "automatic_next_step_requested": (
            "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION"
        ),
        "repository_scan_requested": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "globbing_requested": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "sibling_discovery_requested": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "fallback_search_requested": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "file_discovery_requested": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "repair_requested": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "validation_enforcement_requested": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "contaminated_lineage_validation_requested": (
            "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION"
        ),
        "complete_preparation_artifact_embedded": (
            "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING"
        ),
        "complete_preparation_request_artifact_embedded": (
            "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING"
        ),
        "complete_waiting_operation_artifact_embedded": (
            "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING"
        ),
        "complete_boundary_artifact_embedded": (
            "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING"
        ),
        "complete_candidate_sufficiency_artifact_embedded": (
            "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING"
        ),
        "complete_candidate_sufficiency_basis_embedded": (
            "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING"
        ),
        "archive_bytes_embedded": (
            "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING"
        ),
        "text_component_bodies_embedded": (
            "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING"
        ),
        "recorded_signal_body_embedded": (
            "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING"
        ),
    }
)
PROHIBITED_REQUEST_FLAGS = PROHIBITED_INPUT_FLAGS

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "REQUEST_PATH_NOT_AVAILABLE",
        "REQUEST_PATH_NOT_PARSEABLE",
        "REQUEST_OVERSIZED",
        "REQUEST_NESTING_EXCEEDED",
        "REQUEST_FIELD_MISSING",
        "REQUEST_FIELD_UNKNOWN",
        "REQUEST_VALUE_MISMATCH",
        "DECLARATION_IDENTITY_MISMATCH",
        "PREPARATION_IDENTITY_MISMATCH",
        "PREPARATION_REQUEST_IDENTITY_MISMATCH",
        "SELECTED_OPERATION_IDENTITY_MISMATCH",
        "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
        "GOVERNING_SPECIFICATION_PATH_MISMATCH",
        "PREPARATION_ARTIFACT_PATH_MISMATCH",
        "DECLARATION_SELECTION_INVALID",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "PROHIBITED_CALLER_CANDIDATE",
        "PROHIBITED_CALLER_DIGEST",
        "PROHIBITED_CALLER_POSTURE_MAPS",
        "PROHIBITED_RESULT_PRECLAIM",
        "PROHIBITED_PREPARATION_OR_EVIDENCE_REEVALUATION",
        "PROHIBITED_DOWNSTREAM_CONVERSION",
        "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION",
        "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING",
        "SPECIFICATION_NOT_AVAILABLE",
        "SPECIFICATION_MARKER_MISSING",
        "PREPARATION_ARTIFACT_NOT_AVAILABLE",
        "PREPARATION_ARTIFACT_NOT_PARSEABLE",
        "PREPARATION_ARTIFACT_NOT_MAPPING",
        "PREPARATION_ARTIFACT_METADATA_MISMATCH",
        "PREPARATION_ARTIFACT_FAILED_CHECKS_PRESENT",
        "PREPARATION_ARTIFACT_IDENTITY_MISMATCH",
        "PREPARATION_ARTIFACT_NOT_PREPARED",
        "PREPARATION_ARTIFACT_BLOCKED",
        "PREPARATION_ARTIFACT_POSTURE_INVALID",
        "PREPARATION_ARTIFACT_NON_CLAIM_NOT_FALSE",
        "PREPARATION_ARTIFACT_OMISSION_INVALID",
        "PREPARED_CANDIDATE_MISSING",
        "PREPARED_CANDIDATE_SCHEMA_MISMATCH",
        "PREPARED_CANDIDATE_REFERENCE_MISMATCH",
        "PREPARED_CANDIDATE_EVALUATOR_REFERENCE_MISMATCH",
        "PREPARED_CANDIDATE_POSTURE_MISMATCH",
        "PREPARED_CANDIDATE_NON_CONVERSION_MISMATCH",
        "PREPARED_CANDIDATE_NON_CLAIM_MISMATCH",
        "PREPARED_CANDIDATE_FORBIDDEN_MATERIAL",
        "CANDIDATE_DIGEST_FAILED",
        "WRITE_REFUSED",
    }
)

MAX_SERIALIZED_REQUEST_SIZE = 262_144
MAX_SERIALIZED_RESULT_SIZE = 524_288
MAX_MAPPING_ITEMS = 256
MAX_SEQUENCE_ITEMS = 256
MAX_NESTING_DEPTH = 12
MAX_TEXT_LENGTH = 16_384

PREFIX = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration"
)
PREPARATION_PREFIX = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation"
)

SPECIFICATION_MARKER_CLASSES = MappingProxyType(
    {
        "title": (
            "# Receiver-Side Answerable Basis Receiver Attestation Operation "
            "Basis Declaration V0 Minimum Specification",
        ),
        "declaration_identity": (
            DECLARATION_ID,
            DECLARATION_TYPE,
            DECLARATION_VERSION,
            DECLARATION_SCOPE,
        ),
        "selected_preparation_identity": (
            SELECTED_PREPARATION_ID,
            SELECTED_PREPARATION_TYPE,
            SELECTED_PREPARATION_VERSION,
            SELECTED_PREPARATION_SCOPE,
        ),
        "selected_preparation_request_identity": (
            SELECTED_PREPARATION_REQUEST_ID,
            SELECTED_PREPARATION_REQUEST_TYPE,
            SELECTED_PREPARATION_REQUEST_VERSION,
            SELECTED_PREPARATION_REQUEST_SCOPE,
        ),
        "selected_operation_and_candidate_identity": (
            OPERATION_ID,
            OPERATION_TYPE,
            OPERATION_VERSION,
            OPERATION_SCOPE,
            CANDIDATE_ID,
            CANDIDATE_TYPE,
            CANDIDATE_SCOPE,
        ),
        "selected_preparation_artifact": (
            str(SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH),
        ),
        "candidate_schema": CANDIDATE_FIELDS,
        "posture_maps": (
            *TRACE_INTEGRITY_POSTURE_KEYS,
            *AMBIGUITY_POSTURE_KEYS,
            *CONTRADICTION_POSTURE_KEYS,
            *UNRESOLVED_POSTURE_KEYS,
        ),
        "non_conversion": (NON_CONVERSION_STATEMENT,),
        "basis_non_claims": REQUIRED_BASIS_NON_CLAIMS,
        "outcomes": OUTCOME_FAMILY,
        "results": DECLARATION_RESULT_FAMILY,
        "precedence": (
            "structural or constitutional invalidity produces `BLOCKED` "
            "and `NOT_EVALUATED`",
            "`basis_declaration_selected = false` produces `NOT_DECLARED`",
            "`basis_declaration_selected = true` produces `DECLARED`",
        ),
        "separation": (
            "prepared candidate is not declared basis;",
            "declared basis is not supplied basis;",
            "supplied basis is not admitted basis;",
            "admitted basis is not operation execution;",
        ),
        "no_evidence_reevaluation": (
            "The declaration must not independently recompute any candidate "
            "finding.",
        ),
        "exhaustion_non_authorization": (
            "Exhaustion does not authorize basis supply, basis admission, "
            "operation execution",
        ),
        "open_not_next": ("Open does not mean next.",),
    }
)

RESULT_OMISSION_FIELDS = (
    "complete_preparation_artifact_omitted",
    "complete_preparation_request_artifact_omitted",
    "complete_waiting_operation_artifact_omitted",
    "complete_upstream_boundary_artifact_omitted",
    "complete_candidate_sufficiency_artifact_omitted",
    "complete_candidate_sufficiency_basis_omitted",
    "archive_bytes_omitted",
    "text_component_bodies_omitted",
    "recorded_signal_body_omitted",
)

UPSTREAM_OMISSION_FIELDS = (
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
        "complete_preparation_artifact",
        "complete_preparation_request_artifact",
        "complete_waiting_operation_artifact",
        "complete_boundary_artifact",
        "complete_upstream_boundary_artifact",
        "complete_candidate_sufficiency_artifact",
        "complete_candidate_sufficiency_basis",
        "archive_bytes",
        "text_component_bodies",
        "recorded_signal_body",
        "complete_recorded_signal_data",
        "raw_samples",
        "samples",
        "raw_source_body",
    }
)

BLOCKED_ROUTES = (
    "prepared candidate directly to supplied basis",
    "prepared candidate directly to admitted basis",
    "declaration directly to operation execution or result",
    "declaration directly to receiver-attestation recording",
    "candidate posture directly to identity, provenance, truth, authority, presence, or standing",
    "archive correspondence directly to verified provenance or occurrence truth",
    "declaration exhaustion directly to supply authorization",
    "completed declaration directly to reusable route, retry, debt, obligation, or automatic next step",
    "declaration directly to repair or contaminated-lineage validation",
)

WHAT_REMAINS_OPEN = (
    "declaration test",
    "declaration live artifact",
    "basis supply",
    "supply resolver and test",
    "basis admission",
    "receiver-attestation operation execution",
    "receiver-attestation operation result",
    "receiver attestation",
    "receiver-answerable receipt",
    "presence re-evaluation",
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
    "output",
    "action",
    "synchronization",
    "follow-on work",
)

RESULT_BASE_SECTIONS = frozenset(
    {
        f"{PREFIX}_metadata",
        f"declared_{PREFIX}_request",
        "selected_declaration_preparation_request_operation_candidate_identity",
        "specification_marker_validation",
        "selected_preparation_artifact_validation",
        "prepared_candidate_validation",
        "candidate_digest",
        "declaration_decision",
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
DECLARED_BASIS_SECTION = "declared_receiver_attestation_operation_basis"
RESULT_SECTIONS = RESULT_BASE_SECTIONS


class ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationV0MinError(
    Exception
):
    """Raised when a declaration result cannot be summarized or written."""


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
        text = json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            allow_nan=False,
        )
    except (TypeError, ValueError):
        return None
    return len(text.encode("utf-8"))


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


def _require(
    checks: list[dict[str, Any]],
    name: str,
    condition: bool,
    code: str,
    reason: str,
) -> tuple[str | None, str | None]:
    checks.append(_check(name, condition, code if not condition else None))
    if condition:
        return None, None
    return code, reason


def _canonical_result_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_request_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUEST_REQUIRED_FALSE_NON_CLAIMS}


def _canonical_basis_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_BASIS_NON_CLAIMS}


def _exact_false_mapping(
    value: Any,
    fields: Sequence[str],
) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(fields)
        and all(value.get(field) is False for field in fields)
    )


def _exact_mapping(value: Any, expected: Mapping[str, Any]) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(expected)
        and all(value.get(key) == expected[key] for key in expected)
        and all(
            type(value.get(key)) is type(expected[key])
            for key in expected
            if type(expected[key]) is bool
        )
    )


def _expected_request_values() -> dict[str, str]:
    return {
        "declaration_id": DECLARATION_ID,
        "declaration_type": DECLARATION_TYPE,
        "declaration_version": DECLARATION_VERSION,
        "declaration_scope": DECLARATION_SCOPE,
        "selected_preparation_id": SELECTED_PREPARATION_ID,
        "selected_preparation_type": SELECTED_PREPARATION_TYPE,
        "selected_preparation_version": SELECTED_PREPARATION_VERSION,
        "selected_preparation_scope": SELECTED_PREPARATION_SCOPE,
        "selected_preparation_request_id": SELECTED_PREPARATION_REQUEST_ID,
        "selected_preparation_request_type": (
            SELECTED_PREPARATION_REQUEST_TYPE
        ),
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
        "governing_declaration_specification_path": str(
            GOVERNING_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_preparation_artifact_path": str(
            SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH
        ),
    }


def _request_allowed_keys() -> frozenset[str]:
    return frozenset(
        {
            REQUEST_SELECTION_FIELD,
            "declared_non_claims",
            *tuple(_expected_request_values()),
            *tuple(PROHIBITED_INPUT_FLAGS),
        }
    )


def build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_request(
    *,
    basis_declaration_selected: bool = True,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one canonical declaration request with visible overrides."""
    request: dict[str, Any] = {
        **_expected_request_values(),
        REQUEST_SELECTION_FIELD: basis_declaration_selected,
        "declared_non_claims": copy.deepcopy(
            _canonical_request_non_claims()
            if declared_non_claims is None
            else declared_non_claims
        ),
        **{field: False for field in PROHIBITED_INPUT_FLAGS},
    }
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_request(
    *,
    basis_declaration_selected: bool = True,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one declaration request while retaining all visible overrides."""
    return build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_request(
        basis_declaration_selected=basis_declaration_selected,
        **overrides,
    )


def _identity_failure_code(field: str) -> str:
    if field.startswith("declaration_"):
        return "DECLARATION_IDENTITY_MISMATCH"
    if field.startswith("selected_preparation_request_"):
        return "PREPARATION_REQUEST_IDENTITY_MISMATCH"
    if field.startswith("selected_preparation_"):
        return "PREPARATION_IDENTITY_MISMATCH"
    if field.startswith("selected_receiver_attestation_operation_"):
        return "SELECTED_OPERATION_IDENTITY_MISMATCH"
    if field.startswith("receiver_side_answerable_basis_candidate_"):
        return "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
    if field == "governing_declaration_specification_path":
        return "GOVERNING_SPECIFICATION_PATH_MISMATCH"
    if field == "selected_preparation_artifact_path":
        return "PREPARATION_ARTIFACT_PATH_MISMATCH"
    return "REQUEST_VALUE_MISMATCH"


def _validate_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    size = _serialized_size(request)
    if size is None or size > MAX_SERIALIZED_REQUEST_SIZE:
        return _failure(
            checks,
            "request_bounded_size",
            "REQUEST_OVERSIZED",
        )
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

    for field, expected in _expected_request_values().items():
        if request.get(field) != expected:
            code = _identity_failure_code(field)
            return _failure(
                checks,
                f"request_{field}_matches",
                code,
                f"{field} does not match the selected declaration line",
            )

    selection = request.get(REQUEST_SELECTION_FIELD)
    if not _exact_bool(selection):
        return _failure(
            checks,
            "basis_declaration_selected_is_boolean",
            "DECLARATION_SELECTION_INVALID",
            "basis_declaration_selected must be exactly Boolean",
        )

    if not _exact_false_mapping(
        request.get("declared_non_claims"),
        REQUEST_REQUIRED_FALSE_NON_CLAIMS,
    ):
        return _failure(
            checks,
            "declared_non_claims_are_canonical_false",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared non-claims are missing, additional, malformed, or flipped",
        )

    for field, code in PROHIBITED_INPUT_FLAGS.items():
        value = request.get(field)
        if value is True:
            return _failure(
                checks,
                f"{field}_not_requested",
                code,
                f"{field} is prohibited",
            )
        if value is not False:
            return _failure(
                checks,
                f"{field}_is_false",
                "REQUEST_VALUE_MISMATCH",
                f"{field} must be exactly false",
            )

    checks.append(_check("request_contract_validated", True))
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
            "governing declaration specification is unavailable",
        )
        return validation, code, reason
    markers = _marker_status(text)
    validation["marker_status"] = markers
    if not all(markers.values()):
        code, reason = _failure(
            checks,
            "governing_specification_markers_exact",
            "SPECIFICATION_MARKER_MISSING",
            "governing declaration specification markers are incomplete",
        )
        return validation, code, reason
    validation["specification_markers_validated"] = True
    checks.append(_check("governing_specification_markers_exact", True))
    return validation, None, None


def _upstream_validation_base() -> dict[str, Any]:
    return {
        "selected_preparation_artifact_path": str(
            SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH
        ),
        "preparation_artifact_validated": False,
        "metadata_validated": False,
        "identity_validated": False,
        "prepared_posture_validated": False,
        "non_claims_validated": False,
        "omission_posture_validated": False,
        "candidate_present": False,
        "complete_preparation_artifact_omitted": True,
    }


def _validate_preparation_artifact(
    checks: list[dict[str, Any]],
) -> tuple[
    dict[str, Any],
    dict[str, Any] | None,
    str | None,
    str | None,
]:
    validation = _upstream_validation_base()
    artifact, error = _read_json(SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH)
    if error in {"not_a_file", "unreadable"}:
        code, reason = _failure(
            checks,
            "selected_preparation_artifact_available",
            "PREPARATION_ARTIFACT_NOT_AVAILABLE",
            "selected preparation artifact is unavailable",
        )
        return validation, None, code, reason
    if error is not None:
        code, reason = _failure(
            checks,
            "selected_preparation_artifact_parseable",
            "PREPARATION_ARTIFACT_NOT_PARSEABLE",
            "selected preparation artifact is not strict parseable JSON",
        )
        return validation, None, code, reason
    if not isinstance(artifact, Mapping):
        code, reason = _failure(
            checks,
            "selected_preparation_artifact_mapping",
            "PREPARATION_ARTIFACT_NOT_MAPPING",
            "selected preparation artifact is not a mapping",
        )
        return validation, None, code, reason

    metadata = artifact.get(f"{PREPARATION_PREFIX}_metadata")
    state = artifact.get(PREPARATION_PREFIX)
    identity = artifact.get(
        "selected_preparation_request_operation_candidate_identity"
    )
    specification = artifact.get("specification_marker_validation")
    request_validation = artifact.get(
        "preparation_request_artifact_validation"
    )
    boundary_validation = artifact.get(
        "selected_boundary_reference_validation"
    )
    bounded_evaluation = artifact.get("bounded_path_and_file_evaluation")
    decision = artifact.get("preparation_decision")
    summary = artifact.get(f"{PREPARATION_PREFIX}_summary")
    non_claims = artifact.get("non_claims")
    omission = artifact.get("omission_posture")
    block = artifact.get("block")
    candidate = artifact.get("prepared_declaration_candidate")
    required_mappings = (
        metadata,
        state,
        identity,
        specification,
        request_validation,
        boundary_validation,
        bounded_evaluation,
        decision,
        summary,
        non_claims,
        omission,
        block,
    )
    if not all(isinstance(value, Mapping) for value in required_mappings):
        code, reason = _failure(
            checks,
            "selected_preparation_artifact_shape",
            "PREPARATION_ARTIFACT_NOT_MAPPING",
            "selected preparation artifact canonical sections are incomplete",
        )
        return validation, None, code, reason

    root_requirements = (
        (
            "resolver_module",
            artifact.get("resolver_module") == PREPARATION_RESOLVER_MODULE,
            "PREPARATION_ARTIFACT_METADATA_MISMATCH",
        ),
        (
            "result_version",
            artifact.get("result_version") == PREPARATION_RESULT_VERSION,
            "PREPARATION_ARTIFACT_METADATA_MISMATCH",
        ),
        (
            "failed_check_count",
            type(artifact.get("failed_check_count")) is int
            and artifact.get("failed_check_count") == 0,
            "PREPARATION_ARTIFACT_FAILED_CHECKS_PRESENT",
        ),
        (
            "outcome",
            artifact.get("outcome") == PREPARATION_OUTCOME_PREPARED,
            "PREPARATION_ARTIFACT_NOT_PREPARED",
        ),
        (
            "block",
            block.get("blocked") is False
            and block.get("code") is None
            and block.get("block_code") is None
            and block.get("reason") is None,
            "PREPARATION_ARTIFACT_BLOCKED",
        ),
    )
    for name, condition, code in root_requirements:
        failure_code, failure_reason = _require(
            checks,
            f"preparation_artifact_{name}",
            condition,
            code,
            f"selected preparation artifact {name} is invalid",
        )
        if failure_code is not None:
            return validation, None, failure_code, failure_reason
    validation["metadata_validated"] = True

    expected_metadata = {
        "preparation_id": SELECTED_PREPARATION_ID,
        "preparation_type": SELECTED_PREPARATION_TYPE,
        "preparation_version": SELECTED_PREPARATION_VERSION,
        "preparation_scope": SELECTED_PREPARATION_SCOPE,
    }
    if not _exact_mapping(metadata, expected_metadata):
        code, reason = _failure(
            checks,
            "preparation_artifact_identity_metadata",
            "PREPARATION_ARTIFACT_IDENTITY_MISMATCH",
            "selected preparation metadata identity is invalid",
        )
        return validation, None, code, reason

    expected_identity = {
        "selected_preparation_request_id": SELECTED_PREPARATION_REQUEST_ID,
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
    }
    if any(identity.get(key) != value for key, value in expected_identity.items()):
        code, reason = _failure(
            checks,
            "preparation_artifact_selected_identity",
            "PREPARATION_ARTIFACT_IDENTITY_MISMATCH",
            "selected preparation request, operation, or candidate identity is invalid",
        )
        return validation, None, code, reason

    state_identity = {
        "preparation_id": SELECTED_PREPARATION_ID,
        "preparation_type": SELECTED_PREPARATION_TYPE,
        "preparation_version": SELECTED_PREPARATION_VERSION,
        "preparation_scope": SELECTED_PREPARATION_SCOPE,
        "selected_preparation_request_id": SELECTED_PREPARATION_REQUEST_ID,
        "selected_receiver_attestation_operation_id": OPERATION_ID,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
    }
    if any(state.get(key) != value for key, value in state_identity.items()):
        code, reason = _failure(
            checks,
            "preparation_artifact_state_identity",
            "PREPARATION_ARTIFACT_IDENTITY_MISMATCH",
            "selected preparation state identity is invalid",
        )
        return validation, None, code, reason
    validation["identity_validated"] = True
    checks.append(_check("preparation_artifact_identity_validated", True))

    required_state_true = (
        "basis_declaration_preparation_selected",
        "specification_markers_validated",
        "preparation_request_artifact_validated",
        "selected_boundary_reference_validated",
        "bounded_paths_validated",
        "required_bounded_components_available",
        "archive_hash_record_validated",
        "archive_correspondence_validated",
        "required_text_components_validated",
        "timestamp_validated",
        "recorded_signal_artifact_validated",
        "complete_21_field_candidate_prepared",
        "preparation_recorded",
        "preparation_result_recorded",
        "preparation_exhausted",
        "basis_declaration_preparation_started",
        "basis_declaration_preparation_completed",
        "receiver_attestation_operation_basis_declaration_candidate_prepared",
        "receiver_attestation_operation_basis_prepared",
    )
    for field in required_state_true:
        code, reason = _require(
            checks,
            f"preparation_artifact_{field}_true",
            state.get(field) is True,
            "PREPARATION_ARTIFACT_POSTURE_INVALID",
            f"selected preparation posture must be true: {field}",
        )
        if code is not None:
            return validation, None, code, reason

    required_state_false = (
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
        "prior_unsupported_candidate_a_claim_validated",
        "prior_unsupported_candidate_b_claim_validated",
        "prior_unsupported_derivation_event_claim_validated",
        "affected_file_repaired",
        "repository_scan_performed",
        "file_discovery_performed",
        "validation_enforced",
    )
    for field in required_state_false:
        code, reason = _require(
            checks,
            f"preparation_artifact_{field}_false",
            state.get(field) is False,
            "PREPARATION_ARTIFACT_POSTURE_INVALID",
            f"selected preparation posture must be false: {field}",
        )
        if code is not None:
            return validation, None, code, reason

    if (
        state.get("preparation_result") != PREPARATION_RESULT_PREPARED
        or state.get("decision_code") != PREPARATION_DECISION_CODE
        or decision.get("code") != PREPARATION_DECISION_CODE
        or decision.get("caller_selected_result") is not False
    ):
        code, reason = _failure(
            checks,
            "preparation_artifact_prepared_decision",
            "PREPARATION_ARTIFACT_NOT_PREPARED",
            "selected preparation artifact does not contain the prepared decision",
        )
        return validation, None, code, reason

    compact_true = (
        "preparation_selection",
        "specification_markers_validated",
        "preparation_request_artifact_validated",
        "selected_boundary_reference_validated",
        "bounded_paths_validated",
        "required_bounded_components_available",
        "archive_hash_record_validated",
        "archive_correspondence_validated",
        "required_text_components_validated",
        "timestamp_validated",
        "recorded_signal_artifact_validated",
        "complete_21_field_candidate_prepared",
        "preparation_recorded",
        "preparation_result_recorded",
        "preparation_exhausted",
        "basis_declaration_preparation_started",
        "basis_declaration_preparation_completed",
        "declaration_candidate_prepared",
        "operation_basis_prepared",
        "result_level_non_claims_canonical_false",
        "complete_material_omitted",
    )
    compact_false = (
        "archive_correspondence_contradicted",
        "timestamp_ambiguous",
        "operation_basis_declared",
        "operation_basis_supplied",
        "operation_basis_admitted",
        "operation_recorded",
        "operation_result_recorded",
        "operation_exhausted",
        "receiver_attestation_recorded",
    )
    if (
        summary.get("preparation_result") != PREPARATION_RESULT_PREPARED
        or any(summary.get(field) is not True for field in compact_true)
        or any(summary.get(field) is not False for field in compact_false)
    ):
        code, reason = _failure(
            checks,
            "preparation_artifact_summary_posture",
            "PREPARATION_ARTIFACT_POSTURE_INVALID",
            "selected preparation summary posture is invalid",
        )
        return validation, None, code, reason

    if (
        specification.get("specification_markers_validated") is not True
        or request_validation.get("preparation_request_artifact_validated")
        is not True
        or boundary_validation.get("selected_boundary_reference_validated")
        is not True
        or bounded_evaluation.get("bounded_paths_validated") is not True
        or bounded_evaluation.get("required_bounded_components_available")
        is not True
        or bounded_evaluation.get("complete_21_field_candidate_preparable")
        is not True
    ):
        code, reason = _failure(
            checks,
            "preparation_artifact_validation_sections",
            "PREPARATION_ARTIFACT_POSTURE_INVALID",
            "selected preparation validation sections are invalid",
        )
        return validation, None, code, reason

    validation["prepared_posture_validated"] = True
    checks.append(_check("preparation_artifact_prepared_posture_validated", True))

    if not _exact_false_mapping(
        non_claims,
        UPSTREAM_PREPARATION_FALSE_NON_CLAIMS,
    ):
        code, reason = _failure(
            checks,
            "preparation_artifact_non_claims_false",
            "PREPARATION_ARTIFACT_NON_CLAIM_NOT_FALSE",
            "selected preparation non-claims are not canonical false",
        )
        return validation, None, code, reason
    validation["non_claims_validated"] = True
    checks.append(_check("preparation_artifact_non_claims_false", True))

    if not (
        set(omission) == set(UPSTREAM_OMISSION_FIELDS)
        and all(omission.get(field) is True for field in UPSTREAM_OMISSION_FIELDS)
    ):
        code, reason = _failure(
            checks,
            "preparation_artifact_omission_posture",
            "PREPARATION_ARTIFACT_OMISSION_INVALID",
            "selected preparation omission posture is invalid",
        )
        return validation, None, code, reason
    validation["omission_posture_validated"] = True

    if not isinstance(candidate, Mapping):
        code, reason = _failure(
            checks,
            "prepared_candidate_present",
            "PREPARED_CANDIDATE_MISSING",
            "selected preparation artifact has no prepared candidate",
        )
        return validation, None, code, reason
    validation["candidate_present"] = True
    validation["preparation_artifact_validated"] = True
    validation["metadata"] = {
        "resolver_module": artifact.get("resolver_module"),
        "result_version": artifact.get("result_version"),
        "outcome": artifact.get("outcome"),
        "failed_check_count": artifact.get("failed_check_count"),
        "preparation_result": state.get("preparation_result"),
        "decision_code": state.get("decision_code"),
    }
    validation["identity"] = {
        **expected_metadata,
        **expected_identity,
    }
    validation["posture"] = {
        "preparation_recorded": True,
        "preparation_result_recorded": True,
        "preparation_exhausted": True,
        "basis_declaration_preparation_started": True,
        "basis_declaration_preparation_completed": True,
        "declaration_candidate_prepared": True,
        "operation_basis_prepared": True,
        "operation_basis_declared": False,
        "operation_basis_supplied": False,
        "operation_basis_admitted": False,
        "operation_recorded": False,
        "operation_result_recorded": False,
        "operation_exhausted": False,
        "receiver_attestation_recorded": False,
        "result_level_non_claims_canonical_false": True,
        "complete_material_omitted": True,
    }
    checks.append(_check("selected_preparation_artifact_validated", True))
    return validation, copy.deepcopy(dict(candidate)), None, None


def _candidate_digest(candidate: Mapping[str, Any]) -> str:
    rendered = json.dumps(
        candidate,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    return hashlib.sha256(rendered.encode("utf-8")).hexdigest()


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


def _validate_candidate(
    candidate: Any,
    checks: list[dict[str, Any]],
) -> tuple[
    dict[str, Any],
    str | None,
    str | None,
    str | None,
]:
    validation: dict[str, Any] = {
        "candidate_received_from_selected_preparation_artifact": False,
        "exact_21_field_candidate_validated": False,
        "candidate_references_validated": False,
        "evaluator_reference_validated": False,
        "candidate_posture_maps_validated": False,
        "non_conversion_statement_validated": False,
        "basis_non_claims_validated": False,
        "complete_source_material_omitted": False,
        "candidate_digest_algorithm": None,
        "candidate_sha256": None,
    }
    if not isinstance(candidate, Mapping):
        code, reason = _failure(
            checks,
            "prepared_candidate_mapping",
            "PREPARED_CANDIDATE_MISSING",
            "prepared candidate is absent or not a mapping",
        )
        return validation, None, code, reason
    validation["candidate_received_from_selected_preparation_artifact"] = True

    if set(candidate) != set(CANDIDATE_FIELDS) or len(candidate) != 21:
        code, reason = _failure(
            checks,
            "prepared_candidate_exact_schema",
            "PREPARED_CANDIDATE_SCHEMA_MISMATCH",
            "prepared candidate does not contain exactly 21 canonical fields",
        )
        return validation, None, code, reason
    validation["exact_21_field_candidate_validated"] = True
    checks.append(_check("prepared_candidate_exact_schema", True))

    if any(
        candidate.get(field) != expected
        for field, expected in EXACT_CANDIDATE_REFERENCES.items()
    ):
        code, reason = _failure(
            checks,
            "prepared_candidate_reference_values",
            "PREPARED_CANDIDATE_REFERENCE_MISMATCH",
            "prepared candidate reference value is not exact",
        )
        return validation, None, code, reason
    validation["candidate_references_validated"] = True
    checks.append(_check("prepared_candidate_reference_values", True))

    if candidate.get("evaluator_reference") != EXPECTED_EVALUATOR_REFERENCE:
        code, reason = _failure(
            checks,
            "prepared_candidate_evaluator_reference",
            "PREPARED_CANDIDATE_EVALUATOR_REFERENCE_MISMATCH",
            "prepared candidate evaluator reference is not exact",
        )
        return validation, None, code, reason
    validation["evaluator_reference_validated"] = True
    checks.append(_check("prepared_candidate_evaluator_reference", True))

    expected_postures = {
        "trace_integrity_postures": EXPECTED_TRACE_INTEGRITY_POSTURES,
        "ambiguity_postures": EXPECTED_AMBIGUITY_POSTURES,
        "contradiction_postures": EXPECTED_CONTRADICTION_POSTURES,
        "unresolved_postures": EXPECTED_UNRESOLVED_POSTURES,
    }
    if any(
        not _exact_mapping(candidate.get(field), expected)
        for field, expected in expected_postures.items()
    ):
        code, reason = _failure(
            checks,
            "prepared_candidate_posture_maps",
            "PREPARED_CANDIDATE_POSTURE_MISMATCH",
            "prepared candidate posture map is not exact",
        )
        return validation, None, code, reason
    validation["candidate_posture_maps_validated"] = True
    checks.append(_check("prepared_candidate_posture_maps", True))

    if candidate.get("non_conversion_statement") != NON_CONVERSION_STATEMENT:
        code, reason = _failure(
            checks,
            "prepared_candidate_non_conversion_statement",
            "PREPARED_CANDIDATE_NON_CONVERSION_MISMATCH",
            "prepared candidate non-conversion statement is not exact",
        )
        return validation, None, code, reason
    validation["non_conversion_statement_validated"] = True
    checks.append(_check("prepared_candidate_non_conversion_statement", True))

    if not _exact_false_mapping(
        candidate.get("basis_non_claims"),
        REQUIRED_BASIS_NON_CLAIMS,
    ):
        code, reason = _failure(
            checks,
            "prepared_candidate_basis_non_claims",
            "PREPARED_CANDIDATE_NON_CLAIM_MISMATCH",
            "prepared candidate basis non-claims are not exact false",
        )
        return validation, None, code, reason
    if "receiver_attestation_recorded" in _mapping(
        candidate.get("basis_non_claims")
    ):
        code, reason = _failure(
            checks,
            "prepared_candidate_branch_posture_absent",
            "PREPARED_CANDIDATE_NON_CLAIM_MISMATCH",
            "receiver_attestation_recorded is not a basis non-claim",
        )
        return validation, None, code, reason
    validation["basis_non_claims_validated"] = True
    checks.append(_check("prepared_candidate_basis_non_claims", True))

    if _contains_forbidden_material(candidate):
        code, reason = _failure(
            checks,
            "prepared_candidate_complete_material_omitted",
            "PREPARED_CANDIDATE_FORBIDDEN_MATERIAL",
            "prepared candidate contains complete source material",
        )
        return validation, None, code, reason
    validation["complete_source_material_omitted"] = True

    try:
        digest = _candidate_digest(candidate)
    except (TypeError, ValueError):
        code, reason = _failure(
            checks,
            "prepared_candidate_digest_computable",
            "CANDIDATE_DIGEST_FAILED",
            "prepared candidate canonical digest could not be computed",
        )
        return validation, None, code, reason
    validation["candidate_digest_algorithm"] = CANDIDATE_DIGEST_ALGORITHM
    validation["candidate_sha256"] = digest
    checks.append(_check("prepared_candidate_digest_computable", True))
    return validation, digest, None, None


def _safe_declared_request(request: Mapping[str, Any]) -> dict[str, Any]:
    safe: dict[str, Any] = {
        **_expected_request_values(),
        REQUEST_SELECTION_FIELD: (
            request.get(REQUEST_SELECTION_FIELD)
            if _exact_bool(request.get(REQUEST_SELECTION_FIELD))
            else None
        ),
        "declared_non_claims_validated": _exact_false_mapping(
            request.get("declared_non_claims"),
            REQUEST_REQUIRED_FALSE_NON_CLAIMS,
        ),
        "prohibited_input_flags_validated": all(
            request.get(field) is False for field in PROHIBITED_INPUT_FLAGS
        ),
    }
    return safe


def _state(
    outcome: str,
    declaration_result: str,
    request: Mapping[str, Any],
    *,
    specification_validated: bool,
    preparation_artifact_validated: bool,
    candidate_validated: bool,
    digest: str | None,
    decision_code: str,
    decision_reason: str,
) -> dict[str, Any]:
    completed = outcome in {OUTCOME_DECLARED, OUTCOME_NOT_DECLARED}
    declared = outcome == OUTCOME_DECLARED
    state: dict[str, Any] = {
        "declaration_id": DECLARATION_ID,
        "declaration_type": DECLARATION_TYPE,
        "declaration_version": DECLARATION_VERSION,
        "declaration_scope": DECLARATION_SCOPE,
        "selected_preparation_id": SELECTED_PREPARATION_ID,
        "selected_preparation_request_id": SELECTED_PREPARATION_REQUEST_ID,
        "selected_receiver_attestation_operation_id": OPERATION_ID,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        REQUEST_SELECTION_FIELD: (
            request.get(REQUEST_SELECTION_FIELD)
            if _exact_bool(request.get(REQUEST_SELECTION_FIELD))
            else None
        ),
        "declaration_result": declaration_result,
        "decision_code": decision_code,
        "decision_reason": decision_reason,
        "specification_markers_validated": specification_validated,
        "selected_preparation_artifact_validated": (
            preparation_artifact_validated
        ),
        "declaration_candidate_received": candidate_validated,
        "exact_21_field_candidate_validated": candidate_validated,
        "candidate_digest_algorithm": (
            CANDIDATE_DIGEST_ALGORITHM if digest is not None else None
        ),
        "candidate_sha256": digest,
        "declaration_recorded": completed,
        "declaration_result_recorded": completed,
        "declaration_exhausted": completed,
        "receiver_attestation_operation_basis_declaration_recorded": declared,
        "receiver_attestation_operation_basis_declared": declared,
        **{field: False for field in EXTRA_REQUIRED_FALSE_POSTURES},
        **_canonical_result_non_claims(),
        **{field: True for field in RESULT_OMISSION_FIELDS},
    }
    return state


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    state = _mapping(result.get(PREFIX))
    decision = _mapping(result.get("declaration_decision"))
    digest = _mapping(result.get("candidate_digest"))
    candidate_validation = _mapping(result.get("prepared_candidate_validation"))
    omission = _mapping(result.get("omission_posture"))
    block = _mapping(result.get("block"))
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "declaration_id": state.get("declaration_id"),
        "declaration_type": state.get("declaration_type"),
        "declaration_version": state.get("declaration_version"),
        "declaration_scope": state.get("declaration_scope"),
        "selected_preparation_id": state.get("selected_preparation_id"),
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
        "selected_preparation_artifact_path": str(
            SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH
        ),
        "outcome": result.get("outcome"),
        "declaration_result": state.get("declaration_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": block.get("blocked"),
        "decision_code": decision.get("code"),
        "decision_reason": decision.get("reason"),
        "declaration_selection": state.get(REQUEST_SELECTION_FIELD),
        "specification_markers_validated": state.get(
            "specification_markers_validated"
        ),
        "preparation_artifact_validated": state.get(
            "selected_preparation_artifact_validated"
        ),
        "exact_21_field_candidate_validated": state.get(
            "exact_21_field_candidate_validated"
        ),
        "candidate_digest_algorithm": digest.get(
            "candidate_digest_algorithm"
        ),
        "candidate_sha256": digest.get("candidate_sha256"),
        "candidate_posture_maps_validated": candidate_validation.get(
            "candidate_posture_maps_validated"
        ),
        "non_conversion_statement_validated": candidate_validation.get(
            "non_conversion_statement_validated"
        ),
        "basis_non_claims_validated": candidate_validation.get(
            "basis_non_claims_validated"
        ),
        "declaration_recorded": state.get("declaration_recorded"),
        "declaration_result_recorded": state.get(
            "declaration_result_recorded"
        ),
        "declaration_exhausted": state.get("declaration_exhausted"),
        "declaration_candidate_received": state.get(
            "declaration_candidate_received"
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
        "operation_executed": state.get(
            "receiver_attestation_operation_executed"
        ),
        "operation_result_recorded": state.get(
            "receiver_attestation_operation_result_recorded"
        ),
        "result_level_non_claims_canonical_false": _exact_false_mapping(
            result.get("non_claims"),
            REQUIRED_FALSE_NON_CLAIMS,
        ),
        "complete_material_omitted": all(
            omission.get(field) is True for field in RESULT_OMISSION_FIELDS
        ),
    }


def _result(
    request: Mapping[str, Any],
    outcome: str,
    declaration_result: str,
    checks: list[dict[str, Any]],
    *,
    specification_validation: Mapping[str, Any] | None = None,
    preparation_validation: Mapping[str, Any] | None = None,
    candidate_validation: Mapping[str, Any] | None = None,
    candidate: Mapping[str, Any] | None = None,
    digest: str | None = None,
    decision_code: str,
    decision_reason: str,
    block_code: str | None = None,
) -> dict[str, Any]:
    specification = copy.deepcopy(dict(specification_validation or {}))
    preparation = copy.deepcopy(dict(preparation_validation or {}))
    candidate_detail = copy.deepcopy(dict(candidate_validation or {}))
    specification_validated = (
        specification.get("specification_markers_validated") is True
    )
    preparation_validated = (
        preparation.get("preparation_artifact_validated") is True
    )
    candidate_validated = (
        candidate_detail.get("exact_21_field_candidate_validated") is True
        and candidate_detail.get("candidate_references_validated") is True
        and candidate_detail.get("evaluator_reference_validated") is True
        and candidate_detail.get("candidate_posture_maps_validated") is True
        and candidate_detail.get("non_conversion_statement_validated") is True
        and candidate_detail.get("basis_non_claims_validated") is True
        and candidate_detail.get("complete_source_material_omitted") is True
        and digest is not None
    )
    state = _state(
        outcome,
        declaration_result,
        request,
        specification_validated=specification_validated,
        preparation_artifact_validated=preparation_validated,
        candidate_validated=candidate_validated,
        digest=digest,
        decision_code=decision_code,
        decision_reason=decision_reason,
    )
    omission = {field: True for field in RESULT_OMISSION_FIELDS}
    result: dict[str, Any] = {
        f"{PREFIX}_metadata": {
            "declaration_id": DECLARATION_ID,
            "declaration_type": DECLARATION_TYPE,
            "declaration_version": DECLARATION_VERSION,
            "declaration_scope": DECLARATION_SCOPE,
        },
        f"declared_{PREFIX}_request": _safe_declared_request(request),
        "selected_declaration_preparation_request_operation_candidate_identity": {
            "declaration_id": DECLARATION_ID,
            "declaration_type": DECLARATION_TYPE,
            "declaration_version": DECLARATION_VERSION,
            "declaration_scope": DECLARATION_SCOPE,
            "selected_preparation_id": SELECTED_PREPARATION_ID,
            "selected_preparation_type": SELECTED_PREPARATION_TYPE,
            "selected_preparation_version": SELECTED_PREPARATION_VERSION,
            "selected_preparation_scope": SELECTED_PREPARATION_SCOPE,
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
            "selected_preparation_artifact_path": str(
                SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH
            ),
        },
        "specification_marker_validation": specification,
        "selected_preparation_artifact_validation": preparation,
        "prepared_candidate_validation": candidate_detail,
        "candidate_digest": {
            "candidate_digest_algorithm": (
                CANDIDATE_DIGEST_ALGORITHM if digest is not None else None
            ),
            "candidate_sha256": digest,
            "canonical_json_utf8": digest is not None,
            "canonical_json_sorted_keys": digest is not None,
            "canonical_json_compact_separators": digest is not None,
            "canonical_json_ensure_ascii_false": digest is not None,
            "caller_supplied_digest_used": False,
            "digest_is_correspondence_only": True,
        },
        "declaration_decision": {
            "code": decision_code,
            "reason": decision_reason,
            "precedence": "BLOCKED_THEN_NOT_DECLARED_THEN_DECLARED",
            "caller_selected_result": False,
        },
        PREFIX: state,
        f"{PREFIX}_checks": copy.deepcopy(checks),
        f"{PREFIX}_statement": {
            "one_exact_prepared_candidate_consumed": candidate_validated,
            "prepared_candidate_is_not_declared_basis": True,
            "declaration_records_repository_standing_only": True,
            "declared_basis_is_not_supplied_basis": True,
            "supplied_basis_is_not_admitted_basis": True,
            "admitted_basis_is_not_operation_execution": True,
            "operation_execution_is_not_operation_result": True,
            "open_does_not_mean_next": True,
        },
        f"{PREFIX}_non_meaning": {
            "declaration_does_not_repeat_preparation": True,
            "declaration_does_not_reread_capture_material": True,
            "declaration_does_not_recompute_archive_correspondence": True,
            "candidate_digest_is_not_provenance_or_truth": True,
            "clean_postures_are_not_identity_provenance_or_standing": True,
            "declaration_does_not_supply_or_admit_basis": True,
            "declaration_does_not_execute_operation": True,
            "declaration_does_not_record_receiver_attestation": True,
            "declaration_does_not_create_receipt_or_presence": True,
            "declaration_exhaustion_does_not_authorize_supply": True,
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
    if outcome == OUTCOME_DECLARED and candidate is not None:
        result[DECLARED_BASIS_SECTION] = copy.deepcopy(dict(candidate))
    result["failed_check_count"] = sum(
        check.get("passed") is False for check in checks
    )
    result["passed_check_count"] = sum(
        check.get("passed") is True for check in checks
    )
    result[f"{PREFIX}_summary"] = _summary_from_result(result)
    return result


def resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one declaration without supplying or executing its basis."""
    if request is None:
        working: Mapping[str, Any] = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_request()
        )
    elif not isinstance(request, Mapping):
        baseline = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_request()
        )
        checks = [_check("request_is_mapping", False, "REQUEST_NOT_MAPPING")]
        return _result(
            baseline,
            OUTCOME_BLOCKED,
            DECLARATION_RESULT_NOT_EVALUATED,
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
            DECLARATION_RESULT_NOT_EVALUATED,
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
            DECLARATION_RESULT_NOT_EVALUATED,
            checks,
            specification_validation=specification,
            decision_code=code,
            decision_reason=reason or "specification validation failed",
            block_code=code,
        )

    preparation, candidate, code, reason = _validate_preparation_artifact(
        checks
    )
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            DECLARATION_RESULT_NOT_EVALUATED,
            checks,
            specification_validation=specification,
            preparation_validation=preparation,
            decision_code=code,
            decision_reason=reason or "preparation artifact validation failed",
            block_code=code,
        )

    candidate_validation, digest, code, reason = _validate_candidate(
        candidate,
        checks,
    )
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            DECLARATION_RESULT_NOT_EVALUATED,
            checks,
            specification_validation=specification,
            preparation_validation=preparation,
            candidate_validation=candidate_validation,
            decision_code=code,
            decision_reason=reason or "prepared candidate validation failed",
            block_code=code,
        )

    checks.append(_check("declaration_precedence_applied", True))
    if working.get(REQUEST_SELECTION_FIELD) is False:
        return _result(
            working,
            OUTCOME_NOT_DECLARED,
            DECLARATION_RESULT_NOT_DECLARED,
            checks,
            specification_validation=specification,
            preparation_validation=preparation,
            candidate_validation=candidate_validation,
            digest=digest,
            decision_code="DECLARATION_NOT_SELECTED",
            decision_reason="exact prepared basis declaration was not selected",
        )

    return _result(
        working,
        OUTCOME_DECLARED,
        DECLARATION_RESULT_DECLARED,
        checks,
        specification_validation=specification,
        preparation_validation=preparation,
        candidate_validation=candidate_validation,
        candidate=candidate,
        digest=digest,
        decision_code="BASIS_DECLARED",
        decision_reason="exact prepared basis candidate declared",
    )


def resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Load one explicit strict JSON request mapping and resolve it."""
    value, error = _read_json(request_path)
    if error is not None or not isinstance(value, Mapping):
        baseline = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_request()
        )
        if error in {"not_a_file", "unreadable"}:
            code = "REQUEST_PATH_NOT_AVAILABLE"
            reason = "request path is unavailable or unreadable"
        elif error is not None:
            code = "REQUEST_PATH_NOT_PARSEABLE"
            reason = "request path is not strict parseable JSON"
        else:
            code = "REQUEST_NOT_MAPPING"
            reason = "request path JSON is not a mapping"
        checks = [_check("request_path_is_mapping_json", False, code)]
        return _result(
            baseline,
            OUTCOME_BLOCKED,
            DECLARATION_RESULT_NOT_EVALUATED,
            checks,
            decision_code=code,
            decision_reason=reason,
            block_code=code,
        )
    return resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min(
        value
    )


def build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic declaration summary."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    return _summary_from_result(result)


def _branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    state = _mapping(result.get(PREFIX))
    block = _mapping(result.get("block"))
    decision = _mapping(result.get("declaration_decision"))
    digest_metadata = _mapping(result.get("candidate_digest"))
    omission = _mapping(result.get("omission_posture"))
    declared_basis = result.get(DECLARED_BASIS_SECTION)
    expected_sections = set(RESULT_BASE_SECTIONS)
    if outcome == OUTCOME_DECLARED:
        expected_sections.add(DECLARED_BASIS_SECTION)
    if set(result) != expected_sections:
        return False
    if (
        outcome not in OUTCOME_FAMILY
        or state.get("declaration_id") != DECLARATION_ID
        or state.get("declaration_type") != DECLARATION_TYPE
        or state.get("declaration_version") != DECLARATION_VERSION
        or state.get("declaration_scope") != DECLARATION_SCOPE
        or state.get("selected_preparation_id") != SELECTED_PREPARATION_ID
        or state.get("selected_preparation_request_id")
        != SELECTED_PREPARATION_REQUEST_ID
        or state.get("selected_receiver_attestation_operation_id")
        != OPERATION_ID
        or state.get("receiver_side_answerable_basis_candidate_id")
        != CANDIDATE_ID
        or decision.get("caller_selected_result") is not False
        or not _exact_false_mapping(
            result.get("non_claims"),
            REQUIRED_FALSE_NON_CLAIMS,
        )
        or any(
            state.get(field) is not False
            for field in EXTRA_REQUIRED_FALSE_POSTURES
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
    ):
        return False

    if outcome == OUTCOME_DECLARED:
        if not isinstance(declared_basis, Mapping):
            return False
        try:
            actual_digest = _candidate_digest(declared_basis)
        except (TypeError, ValueError):
            return False
        return (
            state.get("declaration_result") == DECLARATION_RESULT_DECLARED
            and state.get("declaration_recorded") is True
            and state.get("declaration_result_recorded") is True
            and state.get("declaration_exhausted") is True
            and state.get(
                "receiver_attestation_operation_basis_declaration_recorded"
            )
            is True
            and state.get("receiver_attestation_operation_basis_declared")
            is True
            and state.get("declaration_candidate_received") is True
            and _candidate_shape_valid(declared_basis)
            and digest_metadata.get("candidate_digest_algorithm")
            == CANDIDATE_DIGEST_ALGORITHM
            and digest_metadata.get("candidate_sha256") == actual_digest
            and state.get("candidate_sha256") == actual_digest
            and block.get("blocked") is False
            and block.get("code") is None
        )
    if outcome == OUTCOME_NOT_DECLARED:
        return (
            DECLARED_BASIS_SECTION not in result
            and state.get("declaration_result")
            == DECLARATION_RESULT_NOT_DECLARED
            and state.get("declaration_recorded") is True
            and state.get("declaration_result_recorded") is True
            and state.get("declaration_exhausted") is True
            and state.get(
                "receiver_attestation_operation_basis_declaration_recorded"
            )
            is False
            and state.get("receiver_attestation_operation_basis_declared")
            is False
            and state.get("declaration_candidate_received") is True
            and digest_metadata.get("candidate_digest_algorithm")
            == CANDIDATE_DIGEST_ALGORITHM
            and isinstance(digest_metadata.get("candidate_sha256"), str)
            and len(digest_metadata.get("candidate_sha256")) == 64
            and block.get("blocked") is False
            and block.get("code") is None
            and decision.get("code") == "DECLARATION_NOT_SELECTED"
        )
    return (
        DECLARED_BASIS_SECTION not in result
        and state.get("declaration_result")
        == DECLARATION_RESULT_NOT_EVALUATED
        and state.get("declaration_recorded") is False
        and state.get("declaration_result_recorded") is False
        and state.get("declaration_exhausted") is False
        and state.get(
            "receiver_attestation_operation_basis_declaration_recorded"
        )
        is False
        and state.get("receiver_attestation_operation_basis_declared")
        is False
        and block.get("blocked") is True
        and block.get("code") in BLOCK_CODES
        and block.get("block_code") == block.get("code")
        and isinstance(block.get("reason"), str)
        and bool(block.get("reason"))
    )


def _candidate_shape_valid(candidate: Any) -> bool:
    if not isinstance(candidate, Mapping):
        return False
    if set(candidate) != set(CANDIDATE_FIELDS) or len(candidate) != 21:
        return False
    if any(
        candidate.get(field) != expected
        for field, expected in EXACT_CANDIDATE_REFERENCES.items()
    ):
        return False
    if candidate.get("evaluator_reference") != EXPECTED_EVALUATOR_REFERENCE:
        return False
    expected_postures = {
        "trace_integrity_postures": EXPECTED_TRACE_INTEGRITY_POSTURES,
        "ambiguity_postures": EXPECTED_AMBIGUITY_POSTURES,
        "contradiction_postures": EXPECTED_CONTRADICTION_POSTURES,
        "unresolved_postures": EXPECTED_UNRESOLVED_POSTURES,
    }
    if any(
        not _exact_mapping(candidate.get(field), expected)
        for field, expected in expected_postures.items()
    ):
        return False
    return (
        candidate.get("non_conversion_statement")
        == NON_CONVERSION_STATEMENT
        and _exact_false_mapping(
            candidate.get("basis_non_claims"),
            REQUIRED_BASIS_NON_CLAIMS,
        )
        and not _contains_forbidden_material(candidate)
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
    raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationV0MinError(
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
            REPO_ROOT / SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH
        ).parent.resolve(strict=False),
        (
            REPO_ROOT / SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH
        ).parent.resolve(strict=False),
        (
            REPO_ROOT / SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH
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
        ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationV0MinError
    )
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
    ):
        raise error("WRITE_REFUSED: incompatible result metadata")
    size = _serialized_size(result)
    if (
        size is None
        or size > MAX_SERIALIZED_RESULT_SIZE
        or not _bounded_json(result)
    ):
        raise error("WRITE_REFUSED: result is not bounded JSON")
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
        raise error("WRITE_REFUSED: clean result has a failed check")
    if not _branch_valid(result):
        raise error("WRITE_REFUSED: branch posture is inconsistent")
    if _contains_forbidden_material(result):
        raise error("WRITE_REFUSED: complete source material is present")
    summary = result.get(f"{PREFIX}_summary")
    if (
        not isinstance(summary, Mapping)
        or dict(summary) != _summary_from_result(result)
    ):
        raise error("WRITE_REFUSED: summary is inconsistent")


def write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid declaration result without silent overwrite."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    _validate_write_result(result)
    target = (
        _as_repo_path(output_path)
        if output_path is not None
        else OUTPUT_ROOT / OUTPUT_FILENAME
    )
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationV0MinError(
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
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationV0MinError(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
