"""Supply one exact declared receiver-attestation operation basis.

The resolver consumes one exact DECLARED declaration artifact and may record
its exact 21-field basis as supplied material for one selected operation. It
does not reread capture material, admit the basis, execute the operation, or
create downstream standing.
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
    "basis_supply_v0_min"
)

SUPPLY_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "supply_001"
)
SUPPLY_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "SUPPLY"
)
SUPPLY_VERSION = "0.1.0"
SUPPLY_SCOPE = (
    "SUPPLY_ONE_EXACT_DECLARED_RECEIVER_ATTESTATION_OPERATION_BASIS_TO_ONE_"
    "SELECTED_OPERATION_ONLY"
)

SELECTED_DECLARATION_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_001"
)
SELECTED_DECLARATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION"
)
SELECTED_DECLARATION_VERSION = "0.1.0"
SELECTED_DECLARATION_SCOPE = (
    "DECLARE_ONE_EXACT_PREPARED_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "CANDIDATE_ONLY"
)
DECLARATION_ID = SELECTED_DECLARATION_ID
DECLARATION_TYPE = SELECTED_DECLARATION_TYPE
DECLARATION_VERSION = SELECTED_DECLARATION_VERSION
DECLARATION_SCOPE = SELECTED_DECLARATION_SCOPE

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

DECLARATION_RESOLVER_MODULE = (
    "resolve_receiver_side_answerable_basis_receiver_attestation_operation_"
    "basis_declaration_v0_min"
)
DECLARATION_RESULT_VERSION = "0.1.0"
DECLARATION_OUTCOME_DECLARED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "DECLARATION_DECLARED"
)
DECLARATION_RESULT_DECLARED = "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARED"
DECLARATION_DECISION_CODE = "BASIS_DECLARED"
DECLARATION_DECISION_REASON = "exact prepared basis candidate declared"
DECLARATION_DECISION_PRECEDENCE = (
    "BLOCKED_THEN_NOT_DECLARED_THEN_DECLARED"
)
DECLARATION_GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_DECLARATION_V0_MIN_SPEC.md"
)

OUTCOME_SUPPLIED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "SUPPLY_SUPPLIED"
)
OUTCOME_NOT_SUPPLIED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "SUPPLY_NOT_SUPPLIED"
)
OUTCOME_BLOCKED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_BASIS_"
    "SUPPLY_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_SUPPLIED,
    OUTCOME_NOT_SUPPLIED,
    OUTCOME_BLOCKED,
)

SUPPLY_RESULT_SUPPLIED = "RECEIVER_ATTESTATION_OPERATION_BASIS_SUPPLIED"
SUPPLY_RESULT_NOT_SUPPLIED = (
    "RECEIVER_ATTESTATION_OPERATION_BASIS_NOT_SUPPLIED"
)
SUPPLY_RESULT_NOT_EVALUATED = "NOT_EVALUATED"
SUPPLY_RESULT_FAMILY = (
    SUPPLY_RESULT_SUPPLIED,
    SUPPLY_RESULT_NOT_SUPPLIED,
    SUPPLY_RESULT_NOT_EVALUATED,
)
RESULT_FAMILY = SUPPLY_RESULT_FAMILY

REQUEST_SELECTION_FIELD = "basis_supply_selected"
CANDIDATE_DIGEST_ALGORITHM = "SHA-256"
EXPECTED_CANDIDATE_SHA256 = (
    "8e1bf1eba4e2916078f83ad2afe1f66d8d4c4dfd7b7955674a20b5ed730f2165"
)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "BASIS_SUPPLY_V0_MIN_SPEC.md"
)
SELECTED_DECLARATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_declaration_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_001__receiver_side_answerable_basis_receiver_attestation_"
    "operation_basis_declaration_v0_min_result.json"
)
SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_declaration_"
    "preparation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_001__receiver_side_answerable_basis_receiver_"
    "attestation_operation_basis_declaration_preparation_v0_min_result.json"
)
SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_declaration_"
    "preparation_request_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_request_001__receiver_side_answerable_basis_"
    "receiver_attestation_operation_basis_declaration_preparation_request_"
    "v0_min_result.json"
)
SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_001__"
    "receiver_side_answerable_basis_receiver_attestation_operation_v0_min_"
    "result.json"
)
SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_boundary_v0_min_v2/"
    "receiver_side_answerable_basis_receiver_attestation_boundary_001__"
    "receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_"
    "v2_result.json"
)
SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_candidate_sufficiency_operation_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_"
    "result_001.json"
)
BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH = Path(
    "artifacts/actual_receiver_attestation_capture/"
    "receiver_attestation_capture_001"
)

GOVERNING_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_SPECIFICATION_RELATIVE_PATH
)
SELECTED_DECLARATION_ARTIFACT_PATH = (
    REPO_ROOT / SELECTED_DECLARATION_ARTIFACT_RELATIVE_PATH
)

OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_receiver_attestation_operation_basis_supply_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "supply_001__receiver_side_answerable_basis_receiver_attestation_"
    "operation_basis_supply_v0_min_result.json"
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
DECLARED_BASIS_FIELDS = CANDIDATE_FIELDS
BASIS_FIELDS = CANDIDATE_FIELDS

REFERENCE_FIELDS = CANDIDATE_FIELDS[:14]
EXPECTED_EVALUATOR_REFERENCE = (
    "resolve_receiver_side_answerable_basis_receiver_attestation_operation_"
    "basis_declaration_preparation_v0_min:"
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration_preparation_001:"
    "RECEIVER_ATTESTATION_OPERATION_BASIS_DECLARATION_CANDIDATE_PREPARED"
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
    {field: True for field in TRACE_INTEGRITY_POSTURE_KEYS}
)
EXPECTED_AMBIGUITY_POSTURES = MappingProxyType(
    {field: False for field in AMBIGUITY_POSTURE_KEYS}
)
EXPECTED_CONTRADICTION_POSTURES = MappingProxyType(
    {field: False for field in CONTRADICTION_POSTURE_KEYS}
)
EXPECTED_UNRESOLVED_POSTURES = MappingProxyType(
    {field: False for field in UNRESOLVED_POSTURE_KEYS}
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
    "receiver_attestation_operation_basis_admitted",
    "receiver_attestation_operation_basis_admission_gate_passed",
    "receiver_attestation_operation_basis_admission_scheduled",
    "receiver_attestation_operation_executed",
    "receiver_attestation_operation_recorded",
    "receiver_attestation_operation_result_recorded",
    "receiver_attestation_operation_exhausted",
    "receiver_attestation_decided",
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
    "custody_created",
    "provenance_created",
    "physical_validity_created",
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
    "repeated_receiver_attestation_operation_basis_supply_permission_created",
    "reusable_receiver_attestation_operation_basis_supply_route_created",
    "same_receiver_attestation_operation_basis_supply_rerun_authorized",
    "automatic_receiver_attestation_operation_basis_supply_retry_created",
    "receiver_attestation_operation_basis_supply_debt_created",
    "receiver_attestation_operation_basis_supply_obligation_created",
    "declaration_artifact_stale_open_list_repaired",
    "declaration_artifact_stale_open_list_normalized",
    "contaminated_lineage_validated",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)
EXTRA_REQUIRED_FALSE_POSTURES = (
    "receiver_attestation_operation_basis_admitted",
    "receiver_attestation_operation_basis_admission_gate_passed",
    "receiver_attestation_operation_basis_admission_scheduled",
    "receiver_attestation_operation_executed",
    "receiver_attestation_operation_recorded",
    "receiver_attestation_operation_result_recorded",
    "receiver_attestation_operation_exhausted",
    "receiver_attestation_decided",
    "receiver_attestation_recorded",
    "receiver_attestation_not_recorded",
    "receiver_attestation_indeterminate",
    "custody_created",
    "provenance_created",
    "physical_validity_created",
)
REQUEST_REQUIRED_FALSE_NON_CLAIMS = tuple(
    dict.fromkeys(
        (
            *REQUIRED_FALSE_NON_CLAIMS,
            "supply_recorded",
            "supply_result_recorded",
            "supply_exhausted",
            "receiver_attestation_operation_basis_supply_recorded",
            "receiver_attestation_operation_basis_supplied",
        )
    )
)

UPSTREAM_DECLARATION_FALSE_NON_CLAIMS = (
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

PROHIBITED_INPUT_FLAGS = MappingProxyType(
    {
        "replacement_declared_basis_supplied": "PROHIBITED_CALLER_BASIS",
        "candidate_digest_supplied": "PROHIBITED_CALLER_DIGEST",
        "basis_posture_maps_supplied": "PROHIBITED_CALLER_POSTURE_MAPS",
        "supply_outcome_selected_by_caller": "PROHIBITED_RESULT_PRECLAIM",
        "supply_result_selected_by_caller": "PROHIBITED_RESULT_PRECLAIM",
        "operation_outcome_selected_by_caller": "PROHIBITED_RESULT_PRECLAIM",
        "operation_result_selected_by_caller": "PROHIBITED_RESULT_PRECLAIM",
        "declaration_replay_requested": (
            "PROHIBITED_DECLARATION_OR_EVIDENCE_REEVALUATION"
        ),
        "evidence_reevaluation_requested": (
            "PROHIBITED_DECLARATION_OR_EVIDENCE_REEVALUATION"
        ),
        "archive_rehash_requested": (
            "PROHIBITED_DECLARATION_OR_EVIDENCE_REEVALUATION"
        ),
        "bounded_capture_read_requested": (
            "PROHIBITED_DECLARATION_OR_EVIDENCE_REEVALUATION"
        ),
        "basis_admission_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "admission_gate_success_preclaimed": (
            "PROHIBITED_DOWNSTREAM_CONVERSION"
        ),
        "operation_execution_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "operation_result_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
        "receiver_attestation_preclaimed": "PROHIBITED_DOWNSTREAM_CONVERSION",
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
        "obligation_created": "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION",
        "scheduled_admission_requested": (
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
        "stale_open_list_repair_requested": (
            "PROHIBITED_STALE_OPEN_LIST_CHANGE"
        ),
        "stale_open_list_normalization_requested": (
            "PROHIBITED_STALE_OPEN_LIST_CHANGE"
        ),
        "complete_declaration_artifact_embedded": (
            "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING"
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
        "archive_bytes_embedded": "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING",
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
        "SUPPLY_IDENTITY_MISMATCH",
        "DECLARATION_IDENTITY_MISMATCH",
        "PREPARATION_IDENTITY_MISMATCH",
        "PREPARATION_REQUEST_IDENTITY_MISMATCH",
        "SELECTED_OPERATION_IDENTITY_MISMATCH",
        "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
        "GOVERNING_SPECIFICATION_PATH_MISMATCH",
        "DECLARATION_ARTIFACT_PATH_MISMATCH",
        "SUPPLY_SELECTION_INVALID",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "PROHIBITED_CALLER_BASIS",
        "PROHIBITED_CALLER_DIGEST",
        "PROHIBITED_CALLER_POSTURE_MAPS",
        "PROHIBITED_RESULT_PRECLAIM",
        "PROHIBITED_DECLARATION_OR_EVIDENCE_REEVALUATION",
        "PROHIBITED_DOWNSTREAM_CONVERSION",
        "PROHIBITED_REPEAT_RETRY_DEBT_OR_OBLIGATION",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION",
        "PROHIBITED_STALE_OPEN_LIST_CHANGE",
        "PROHIBITED_COMPLETE_MATERIAL_EMBEDDING",
        "SPECIFICATION_NOT_AVAILABLE",
        "SPECIFICATION_MARKER_MISSING",
        "DECLARATION_ARTIFACT_NOT_AVAILABLE",
        "DECLARATION_ARTIFACT_NOT_PARSEABLE",
        "DECLARATION_ARTIFACT_NOT_MAPPING",
        "DECLARATION_ARTIFACT_METADATA_MISMATCH",
        "DECLARATION_ARTIFACT_FAILED_CHECKS_PRESENT",
        "DECLARATION_ARTIFACT_IDENTITY_MISMATCH",
        "DECLARATION_ARTIFACT_NOT_DECLARED",
        "DECLARATION_ARTIFACT_BLOCKED",
        "DECLARATION_ARTIFACT_POSTURE_INVALID",
        "DECLARATION_ARTIFACT_NON_CLAIM_NOT_FALSE",
        "DECLARATION_ARTIFACT_OMISSION_INVALID",
        "DECLARATION_ARTIFACT_STALE_OPEN_LIST_INVALID",
        "DECLARED_BASIS_MISSING",
        "DECLARED_BASIS_SCHEMA_MISMATCH",
        "DECLARED_BASIS_REFERENCE_MISMATCH",
        "DECLARED_BASIS_EVALUATOR_REFERENCE_MISMATCH",
        "DECLARED_BASIS_POSTURE_MISMATCH",
        "DECLARED_BASIS_NON_CONVERSION_MISMATCH",
        "DECLARED_BASIS_NON_CLAIM_MISMATCH",
        "DECLARED_BASIS_FORBIDDEN_MATERIAL",
        "DECLARED_BASIS_DIGEST_METADATA_MISMATCH",
        "DECLARED_BASIS_DIGEST_FAILED",
        "DECLARED_BASIS_DIGEST_MISMATCH",
        "WRITE_REFUSED",
    }
)

MAX_SERIALIZED_REQUEST_SIZE = 262_144
MAX_SERIALIZED_RESULT_SIZE = 1_048_576
MAX_MAPPING_ITEMS = 256
MAX_SEQUENCE_ITEMS = 256
MAX_NESTING_DEPTH = 12
MAX_TEXT_LENGTH = 16_384

PREFIX = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "supply"
)
DECLARATION_PREFIX = (
    "receiver_side_answerable_basis_receiver_attestation_operation_basis_"
    "declaration"
)

RESULT_OMISSION_FIELDS = (
    "complete_declaration_artifact_omitted",
    "complete_preparation_artifact_omitted",
    "complete_preparation_request_artifact_omitted",
    "complete_waiting_operation_artifact_omitted",
    "complete_upstream_boundary_artifact_omitted",
    "complete_candidate_sufficiency_artifact_omitted",
    "complete_candidate_sufficiency_basis_omitted",
    "archive_bytes_omitted",
    "text_component_bodies_omitted",
    "recorded_signal_body_omitted",
    "complete_material_omitted",
)
UPSTREAM_DECLARATION_OMISSION_FIELDS = (
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

FORBIDDEN_PAYLOAD_KEYS = frozenset(
    {
        "complete_declaration_artifact",
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

STALE_OPEN_LIST_ENTRIES = (
    "declaration test",
    "declaration live artifact",
)

BLOCKED_ROUTES = (
    "declared basis directly to admitted basis",
    "basis supply directly to admission-gate success",
    "basis supply directly to operation execution",
    "basis supply directly to operation result",
    "basis supply directly to receiver-attestation recording",
    "supplied basis directly to receiver-answerable receipt or presence",
    "candidate digest directly to provenance, custody, identity, truth, authority, presence, or standing",
    "clean posture maps directly to independent occurrence verification",
    "supply exhaustion directly to admission authorization",
    "completed supply directly to reusable route, retry, debt, obligation, scheduled admission, or automatic next step",
    "supply directly to repair or normalization of stale declaration-artifact open-list entries",
    "supply directly to repair or validation of contaminated lineage",
)

WHAT_REMAINS_OPEN = (
    "supply tests",
    "supply live artifact",
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
    "repair",
    "validation",
    "follow-on work",
)

SPECIFICATION_MARKER_CLASSES = MappingProxyType(
    {
        "title": (
            "# Receiver-Side Answerable Basis Receiver Attestation Operation "
            "Basis Supply V0 Minimum Specification",
        ),
        "supply_identity": (
            SUPPLY_ID,
            SUPPLY_TYPE,
            SUPPLY_VERSION,
            SUPPLY_SCOPE,
        ),
        "selected_declaration_identity": (
            DECLARATION_ID,
            DECLARATION_TYPE,
            DECLARATION_VERSION,
            DECLARATION_SCOPE,
        ),
        "selected_line_identity": (
            SELECTED_PREPARATION_ID,
            SELECTED_PREPARATION_REQUEST_ID,
            OPERATION_ID,
            OPERATION_TYPE,
            OPERATION_VERSION,
            OPERATION_SCOPE,
            CANDIDATE_ID,
            CANDIDATE_TYPE,
            CANDIDATE_SCOPE,
        ),
        "selected_declaration_artifact": (
            str(SELECTED_DECLARATION_ARTIFACT_RELATIVE_PATH),
        ),
        "declared_basis_schema": CANDIDATE_FIELDS,
        "posture_maps": (
            *TRACE_INTEGRITY_POSTURE_KEYS,
            *AMBIGUITY_POSTURE_KEYS,
            *CONTRADICTION_POSTURE_KEYS,
            *UNRESOLVED_POSTURE_KEYS,
        ),
        "non_conversion": (NON_CONVERSION_STATEMENT,),
        "basis_non_claims": REQUIRED_BASIS_NON_CLAIMS,
        "digest": (
            CANDIDATE_DIGEST_ALGORITHM,
            EXPECTED_CANDIDATE_SHA256,
            "digest_is_correspondence_only",
        ),
        "outcomes": OUTCOME_FAMILY,
        "results": SUPPLY_RESULT_FAMILY,
        "precedence": (
            "structural or constitutional invalidity produces `BLOCKED` "
            "and `NOT_EVALUATED`",
            "`basis_supply_selected = false` produces `NOT_SUPPLIED`",
            "`basis_supply_selected = true` produces `SUPPLIED`",
        ),
        "separation": (
            "declared basis is not supplied basis;",
            "supplied basis is not admitted basis;",
            "supply does not satisfy the operation's admission gate;",
        ),
        "no_evidence_reevaluation": (
            "The supply must not independently reevaluate the findings "
            "represented by the declared basis.",
        ),
        "exhaustion_non_authorization": (
            "Exhaustion does not authorize basis admission, operation "
            "execution",
        ),
        "stale_open_list": (
            "The supply must not block solely because the declaration "
            "artifact retains the disclosed stale artifact-local",
        ),
        "open_not_next": ("Open does not mean next.",),
    }
)

RESULT_BASE_SECTIONS = frozenset(
    {
        f"{PREFIX}_metadata",
        f"declared_{PREFIX}_request",
        "selected_supply_declaration_preparation_request_operation_candidate_identity",
        "specification_marker_validation",
        "selected_declaration_artifact_validation",
        "declaration_artifact_stale_open_list_validation",
        "declared_basis_validation",
        "declared_basis_digest",
        "supply_decision",
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
SUPPLIED_BASIS_SECTION = "supplied_receiver_attestation_operation_basis"
RESULT_SECTIONS = RESULT_BASE_SECTIONS


class ReceiverSideAnswerableBasisReceiverAttestationOperationBasisSupplyV0MinError(
    Exception
):
    """Raised when a supply result cannot be summarized or written."""


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


def _expected_request_values() -> dict[str, str]:
    return {
        "supply_id": SUPPLY_ID,
        "supply_type": SUPPLY_TYPE,
        "supply_version": SUPPLY_VERSION,
        "supply_scope": SUPPLY_SCOPE,
        "selected_declaration_id": DECLARATION_ID,
        "selected_declaration_type": DECLARATION_TYPE,
        "selected_declaration_version": DECLARATION_VERSION,
        "selected_declaration_scope": DECLARATION_SCOPE,
        "selected_preparation_id": SELECTED_PREPARATION_ID,
        "selected_preparation_request_id": SELECTED_PREPARATION_REQUEST_ID,
        "selected_receiver_attestation_operation_id": OPERATION_ID,
        "selected_receiver_attestation_operation_type": OPERATION_TYPE,
        "selected_receiver_attestation_operation_version": OPERATION_VERSION,
        "selected_receiver_attestation_operation_scope": OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "governing_supply_specification_path": str(
            GOVERNING_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_declaration_artifact_path": str(
            SELECTED_DECLARATION_ARTIFACT_RELATIVE_PATH
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


def build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request(
    *,
    basis_supply_selected: bool = True,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one canonical supply request with visible overrides."""
    request: dict[str, Any] = {
        **_expected_request_values(),
        REQUEST_SELECTION_FIELD: basis_supply_selected,
        "declared_non_claims": copy.deepcopy(
            _canonical_request_non_claims()
            if declared_non_claims is None
            else declared_non_claims
        ),
        **{field: False for field in PROHIBITED_INPUT_FLAGS},
    }
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request(
    *,
    basis_supply_selected: bool = True,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one supply request while retaining all visible overrides."""
    return build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request(
        basis_supply_selected=basis_supply_selected,
        **overrides,
    )


def _identity_failure_code(field: str) -> str:
    if field.startswith("supply_"):
        return "SUPPLY_IDENTITY_MISMATCH"
    if field.startswith("selected_declaration_"):
        if field == "selected_declaration_artifact_path":
            return "DECLARATION_ARTIFACT_PATH_MISMATCH"
        return "DECLARATION_IDENTITY_MISMATCH"
    if field == "selected_preparation_request_id":
        return "PREPARATION_REQUEST_IDENTITY_MISMATCH"
    if field == "selected_preparation_id":
        return "PREPARATION_IDENTITY_MISMATCH"
    if field.startswith("selected_receiver_attestation_operation_"):
        return "SELECTED_OPERATION_IDENTITY_MISMATCH"
    if field.startswith("receiver_side_answerable_basis_candidate_"):
        return "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
    if field == "governing_supply_specification_path":
        return "GOVERNING_SPECIFICATION_PATH_MISMATCH"
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
                f"{field} does not match the selected supply line",
            )

    selection = request.get(REQUEST_SELECTION_FIELD)
    if not _exact_bool(selection):
        return _failure(
            checks,
            "basis_supply_selected_is_boolean",
            "SUPPLY_SELECTION_INVALID",
            "basis_supply_selected must be exactly Boolean",
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


def _specification_validation_base() -> dict[str, Any]:
    return {
        "governing_specification_path": str(
            GOVERNING_SPECIFICATION_RELATIVE_PATH
        ),
        "marker_status": {},
        "specification_markers_validated": False,
        "complete_specification_body_omitted": True,
    }


def _validate_specification(
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], str | None, str | None]:
    validation = _specification_validation_base()
    text, error = _read_text(GOVERNING_SPECIFICATION_PATH)
    if error is not None or text is None:
        code, reason = _failure(
            checks,
            "governing_specification_available",
            "SPECIFICATION_NOT_AVAILABLE",
            "governing supply specification is unavailable",
        )
        return validation, code, reason
    markers = _marker_status(text)
    validation["marker_status"] = markers
    if not all(markers.values()):
        code, reason = _failure(
            checks,
            "governing_specification_markers_exact",
            "SPECIFICATION_MARKER_MISSING",
            "governing supply specification markers are incomplete",
        )
        return validation, code, reason
    validation["specification_markers_validated"] = True
    checks.append(_check("governing_specification_markers_exact", True))
    return validation, None, None


def _declaration_validation_base() -> dict[str, Any]:
    return {
        "selected_declaration_artifact_path": str(
            SELECTED_DECLARATION_ARTIFACT_RELATIVE_PATH
        ),
        "metadata_validated": False,
        "identity_validated": False,
        "declared_posture_validated": False,
        "validation_sections_validated": False,
        "non_claims_validated": False,
        "omission_posture_validated": False,
        "declared_basis_present": False,
        "selected_declaration_artifact_validated": False,
        "complete_declaration_artifact_omitted": True,
        "metadata": {},
        "identity": {},
        "posture": {},
    }


def _stale_open_list_validation_base() -> dict[str, Any]:
    return {
        "declaration_artifact_stale_open_list_entries": list(
            STALE_OPEN_LIST_ENTRIES
        ),
        "declaration_artifact_stale_open_list_entries_disclosed": False,
        "declaration_artifact_stale_open_list_entries_preserved": False,
        "declaration_artifact_stale_open_list_entries_not_used_as_supply_block": (
            False
        ),
        "declaration_artifact_stale_open_list_repaired": False,
        "declaration_artifact_stale_open_list_normalized": False,
    }


def _validate_declaration_artifact(
    checks: list[dict[str, Any]],
) -> tuple[
    dict[str, Any],
    dict[str, Any],
    dict[str, Any] | None,
    str | None,
    str | None,
]:
    validation = _declaration_validation_base()
    stale_validation = _stale_open_list_validation_base()
    artifact, error = _read_json(SELECTED_DECLARATION_ARTIFACT_PATH)
    if error in {"not_a_file", "unreadable"}:
        code, reason = _failure(
            checks,
            "selected_declaration_artifact_available",
            "DECLARATION_ARTIFACT_NOT_AVAILABLE",
            "selected declaration artifact is unavailable",
        )
        return validation, stale_validation, None, code, reason
    if error is not None:
        code, reason = _failure(
            checks,
            "selected_declaration_artifact_parseable",
            "DECLARATION_ARTIFACT_NOT_PARSEABLE",
            "selected declaration artifact is not strict parseable JSON",
        )
        return validation, stale_validation, None, code, reason
    if not isinstance(artifact, Mapping):
        code, reason = _failure(
            checks,
            "selected_declaration_artifact_mapping",
            "DECLARATION_ARTIFACT_NOT_MAPPING",
            "selected declaration artifact is not a mapping",
        )
        return validation, stale_validation, None, code, reason

    metadata = artifact.get(f"{DECLARATION_PREFIX}_metadata")
    declared_request = artifact.get(f"declared_{DECLARATION_PREFIX}_request")
    state = artifact.get(DECLARATION_PREFIX)
    identity = artifact.get(
        "selected_declaration_preparation_request_operation_candidate_identity"
    )
    specification = artifact.get("specification_marker_validation")
    preparation = artifact.get("selected_preparation_artifact_validation")
    candidate_validation = artifact.get("prepared_candidate_validation")
    digest = artifact.get("candidate_digest")
    decision = artifact.get("declaration_decision")
    summary = artifact.get(f"{DECLARATION_PREFIX}_summary")
    non_claims = artifact.get("non_claims")
    omission = artifact.get("omission_posture")
    block = artifact.get("block")
    candidate = artifact.get("declared_receiver_attestation_operation_basis")
    required_mappings = (
        metadata,
        declared_request,
        state,
        identity,
        specification,
        preparation,
        candidate_validation,
        digest,
        decision,
        summary,
        non_claims,
        omission,
        block,
    )
    if not all(isinstance(value, Mapping) for value in required_mappings):
        code, reason = _failure(
            checks,
            "selected_declaration_artifact_shape",
            "DECLARATION_ARTIFACT_NOT_MAPPING",
            "selected declaration artifact canonical sections are incomplete",
        )
        return validation, stale_validation, None, code, reason

    root_requirements = (
        (
            "resolver_module",
            artifact.get("resolver_module") == DECLARATION_RESOLVER_MODULE,
            "DECLARATION_ARTIFACT_METADATA_MISMATCH",
        ),
        (
            "result_version",
            artifact.get("result_version") == DECLARATION_RESULT_VERSION,
            "DECLARATION_ARTIFACT_METADATA_MISMATCH",
        ),
        (
            "failed_check_count",
            type(artifact.get("failed_check_count")) is int
            and artifact.get("failed_check_count") == 0,
            "DECLARATION_ARTIFACT_FAILED_CHECKS_PRESENT",
        ),
        (
            "passed_check_count",
            type(artifact.get("passed_check_count")) is int
            and artifact.get("passed_check_count") == 55,
            "DECLARATION_ARTIFACT_METADATA_MISMATCH",
        ),
        (
            "outcome",
            artifact.get("outcome") == DECLARATION_OUTCOME_DECLARED,
            "DECLARATION_ARTIFACT_NOT_DECLARED",
        ),
        (
            "block",
            block.get("blocked") is False
            and block.get("code") is None
            and block.get("block_code") is None
            and block.get("reason") is None,
            "DECLARATION_ARTIFACT_BLOCKED",
        ),
    )
    for name, condition, code in root_requirements:
        failure_code, failure_reason = _require(
            checks,
            f"declaration_artifact_{name}",
            condition,
            code,
            f"selected declaration artifact {name} is invalid",
        )
        if failure_code is not None:
            return (
                validation,
                stale_validation,
                None,
                failure_code,
                failure_reason,
            )
    validation["metadata_validated"] = True

    expected_metadata = {
        "declaration_id": DECLARATION_ID,
        "declaration_type": DECLARATION_TYPE,
        "declaration_version": DECLARATION_VERSION,
        "declaration_scope": DECLARATION_SCOPE,
    }
    if not _exact_mapping(metadata, expected_metadata):
        code, reason = _failure(
            checks,
            "declaration_artifact_identity_metadata",
            "DECLARATION_ARTIFACT_IDENTITY_MISMATCH",
            "selected declaration metadata identity is invalid",
        )
        return validation, stale_validation, None, code, reason

    expected_identity = {
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
        "selected_operation_id": OPERATION_ID,
        "selected_operation_type": OPERATION_TYPE,
        "selected_operation_version": OPERATION_VERSION,
        "selected_operation_scope": OPERATION_SCOPE,
        "selected_candidate_id": CANDIDATE_ID,
        "selected_candidate_type": CANDIDATE_TYPE,
        "selected_candidate_scope": CANDIDATE_SCOPE,
        "governing_specification_path": str(
            DECLARATION_GOVERNING_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_preparation_artifact_path": str(
            SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH
        ),
    }
    if any(identity.get(key) != value for key, value in expected_identity.items()):
        code, reason = _failure(
            checks,
            "declaration_artifact_selected_identity",
            "DECLARATION_ARTIFACT_IDENTITY_MISMATCH",
            "selected declaration lineage identity is invalid",
        )
        return validation, stale_validation, None, code, reason

    state_identity = {
        "declaration_id": DECLARATION_ID,
        "declaration_type": DECLARATION_TYPE,
        "declaration_version": DECLARATION_VERSION,
        "declaration_scope": DECLARATION_SCOPE,
        "selected_preparation_id": SELECTED_PREPARATION_ID,
        "selected_preparation_request_id": SELECTED_PREPARATION_REQUEST_ID,
        "selected_receiver_attestation_operation_id": OPERATION_ID,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
    }
    if any(state.get(key) != value for key, value in state_identity.items()):
        code, reason = _failure(
            checks,
            "declaration_artifact_state_identity",
            "DECLARATION_ARTIFACT_IDENTITY_MISMATCH",
            "selected declaration state identity is invalid",
        )
        return validation, stale_validation, None, code, reason
    validation["identity_validated"] = True
    checks.append(_check("declaration_artifact_identity_validated", True))

    expected_declared_request = {
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
            DECLARATION_GOVERNING_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_preparation_artifact_path": str(
            SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH
        ),
    }
    if any(
        declared_request.get(key) != value
        for key, value in expected_declared_request.items()
    ):
        code, reason = _failure(
            checks,
            "declaration_artifact_declared_request_identity",
            "DECLARATION_ARTIFACT_IDENTITY_MISMATCH",
            "selected declaration request identity is invalid",
        )
        return validation, stale_validation, None, code, reason
    checks.append(_check("declaration_artifact_declared_request_identity", True))

    required_state_true = (
        "basis_declaration_selected",
        "specification_markers_validated",
        "selected_preparation_artifact_validated",
        "declaration_candidate_received",
        "exact_21_field_candidate_validated",
        "declaration_recorded",
        "declaration_result_recorded",
        "declaration_exhausted",
        "receiver_attestation_operation_basis_declaration_recorded",
        "receiver_attestation_operation_basis_declared",
    )
    required_state_false = (
        "receiver_attestation_operation_basis_supplied",
        "receiver_attestation_operation_basis_admitted",
        "receiver_attestation_operation_executed",
        "receiver_attestation_operation_recorded",
        "receiver_attestation_operation_result_recorded",
        "receiver_attestation_operation_exhausted",
        "receiver_attestation_decided",
        "receiver_attestation_recorded",
        "receiver_attestation_not_recorded",
        "receiver_attestation_indeterminate",
        "custody_created",
        "provenance_created",
        "physical_validity_created",
    )
    required_state_true = tuple(
        dict.fromkeys((*required_state_true, *UPSTREAM_DECLARATION_OMISSION_FIELDS))
    )
    required_state_false = tuple(
        dict.fromkeys(
            (*required_state_false, *UPSTREAM_DECLARATION_FALSE_NON_CLAIMS)
        )
    )
    for field in required_state_true:
        if state.get(field) is not True:
            code, reason = _failure(
                checks,
                f"declaration_artifact_{field}_true",
                "DECLARATION_ARTIFACT_POSTURE_INVALID",
                f"selected declaration posture must be true: {field}",
            )
            return validation, stale_validation, None, code, reason
        checks.append(_check(f"declaration_artifact_{field}_true", True))
    for field in required_state_false:
        if state.get(field) is not False:
            code, reason = _failure(
                checks,
                f"declaration_artifact_{field}_false",
                "DECLARATION_ARTIFACT_POSTURE_INVALID",
                f"selected declaration posture must be false: {field}",
            )
            return validation, stale_validation, None, code, reason
        checks.append(_check(f"declaration_artifact_{field}_false", True))

    if (
        state.get("declaration_result") != DECLARATION_RESULT_DECLARED
        or state.get("decision_code") != DECLARATION_DECISION_CODE
        or state.get("decision_reason") != DECLARATION_DECISION_REASON
        or decision.get("code") != DECLARATION_DECISION_CODE
        or decision.get("reason") != DECLARATION_DECISION_REASON
        or decision.get("precedence") != DECLARATION_DECISION_PRECEDENCE
        or decision.get("caller_selected_result") is not False
        or declared_request.get("basis_declaration_selected") is not True
        or declared_request.get("declared_non_claims_validated") is not True
        or declared_request.get("prohibited_input_flags_validated") is not True
    ):
        code, reason = _failure(
            checks,
            "declaration_artifact_declared_decision",
            "DECLARATION_ARTIFACT_NOT_DECLARED",
            "selected declaration artifact does not contain the exact declared decision",
        )
        return validation, stale_validation, None, code, reason
    validation["declared_posture_validated"] = True
    checks.append(_check("declaration_artifact_declared_posture", True))

    validation_true = (
        "exact_21_field_candidate_validated",
        "candidate_received_from_selected_preparation_artifact",
        "candidate_references_validated",
        "evaluator_reference_validated",
        "candidate_posture_maps_validated",
        "non_conversion_statement_validated",
        "basis_non_claims_validated",
        "complete_source_material_omitted",
    )
    if (
        specification.get("specification_markers_validated") is not True
        or preparation.get("preparation_artifact_validated") is not True
        or any(
            candidate_validation.get(field) is not True
            for field in validation_true
        )
        or candidate_validation.get("candidate_digest_algorithm")
        != CANDIDATE_DIGEST_ALGORITHM
        or candidate_validation.get("candidate_sha256")
        != EXPECTED_CANDIDATE_SHA256
    ):
        code, reason = _failure(
            checks,
            "declaration_artifact_validation_sections",
            "DECLARATION_ARTIFACT_POSTURE_INVALID",
            "selected declaration validation sections are invalid",
        )
        return validation, stale_validation, None, code, reason
    validation["validation_sections_validated"] = True
    checks.append(_check("declaration_artifact_validation_sections", True))

    if (
        digest.get("candidate_digest_algorithm")
        != CANDIDATE_DIGEST_ALGORITHM
        or digest.get("candidate_sha256") != EXPECTED_CANDIDATE_SHA256
        or digest.get("caller_supplied_digest_used") is not False
        or digest.get("digest_is_correspondence_only") is not True
    ):
        code, reason = _failure(
            checks,
            "declaration_artifact_digest_metadata",
            "DECLARED_BASIS_DIGEST_METADATA_MISMATCH",
            "selected declaration candidate digest metadata is invalid",
        )
        return validation, stale_validation, None, code, reason
    checks.append(_check("declaration_artifact_digest_metadata", True))

    summary_true = (
        "declaration_selection",
        "specification_markers_validated",
        "preparation_artifact_validated",
        "exact_21_field_candidate_validated",
        "candidate_posture_maps_validated",
        "non_conversion_statement_validated",
        "basis_non_claims_validated",
        "declaration_recorded",
        "declaration_result_recorded",
        "declaration_exhausted",
        "declaration_candidate_received",
        "operation_basis_declared",
        "result_level_non_claims_canonical_false",
        "complete_material_omitted",
    )
    summary_false = (
        "blocked",
        "operation_basis_supplied",
        "operation_basis_admitted",
        "operation_executed",
        "operation_result_recorded",
    )
    if (
        summary.get("resolver_module") != DECLARATION_RESOLVER_MODULE
        or summary.get("result_version") != DECLARATION_RESULT_VERSION
        or summary.get("outcome") != DECLARATION_OUTCOME_DECLARED
        or summary.get("declaration_id") != DECLARATION_ID
        or summary.get("declaration_type") != DECLARATION_TYPE
        or summary.get("declaration_version") != DECLARATION_VERSION
        or summary.get("declaration_scope") != DECLARATION_SCOPE
        or summary.get("selected_preparation_id") != SELECTED_PREPARATION_ID
        or summary.get("selected_preparation_request_id")
        != SELECTED_PREPARATION_REQUEST_ID
        or summary.get("selected_operation_id") != OPERATION_ID
        or summary.get("selected_candidate_id") != CANDIDATE_ID
        or summary.get("declaration_result") != DECLARATION_RESULT_DECLARED
        or summary.get("decision_code") != DECLARATION_DECISION_CODE
        or summary.get("decision_reason") != DECLARATION_DECISION_REASON
        or summary.get("candidate_digest_algorithm")
        != CANDIDATE_DIGEST_ALGORITHM
        or summary.get("candidate_sha256") != EXPECTED_CANDIDATE_SHA256
        or any(summary.get(field) is not True for field in summary_true)
        or any(summary.get(field) is not False for field in summary_false)
    ):
        code, reason = _failure(
            checks,
            "declaration_artifact_summary_posture",
            "DECLARATION_ARTIFACT_POSTURE_INVALID",
            "selected declaration summary posture is invalid",
        )
        return validation, stale_validation, None, code, reason
    checks.append(_check("declaration_artifact_summary_posture", True))

    if not _exact_false_mapping(
        non_claims,
        UPSTREAM_DECLARATION_FALSE_NON_CLAIMS,
    ):
        code, reason = _failure(
            checks,
            "declaration_artifact_non_claims_false",
            "DECLARATION_ARTIFACT_NON_CLAIM_NOT_FALSE",
            "selected declaration non-claims are not canonical false",
        )
        return validation, stale_validation, None, code, reason
    validation["non_claims_validated"] = True
    checks.append(_check("declaration_artifact_non_claims_false", True))

    if not (
        set(omission) == set(UPSTREAM_DECLARATION_OMISSION_FIELDS)
        and all(
            omission.get(field) is True
            for field in UPSTREAM_DECLARATION_OMISSION_FIELDS
        )
    ):
        code, reason = _failure(
            checks,
            "declaration_artifact_omission_posture",
            "DECLARATION_ARTIFACT_OMISSION_INVALID",
            "selected declaration omission posture is invalid",
        )
        return validation, stale_validation, None, code, reason
    validation["omission_posture_validated"] = True
    checks.append(_check("declaration_artifact_omission_posture", True))

    open_items = artifact.get("what_remains_open")
    if not (
        isinstance(open_items, list)
        and all(isinstance(item, str) for item in open_items)
        and all(item in open_items for item in STALE_OPEN_LIST_ENTRIES)
    ):
        code, reason = _failure(
            checks,
            "declaration_artifact_stale_open_list_disclosed",
            "DECLARATION_ARTIFACT_STALE_OPEN_LIST_INVALID",
            "selected declaration stale open-list disclosure is invalid",
        )
        return validation, stale_validation, None, code, reason
    stale_validation.update(
        {
            "declaration_artifact_stale_open_list_entries_disclosed": True,
            "declaration_artifact_stale_open_list_entries_preserved": True,
            "declaration_artifact_stale_open_list_entries_not_used_as_supply_block": (
                True
            ),
        }
    )
    checks.append(_check("declaration_artifact_stale_open_list_disclosed", True))

    if not isinstance(candidate, Mapping):
        code, reason = _failure(
            checks,
            "declared_basis_present",
            "DECLARED_BASIS_MISSING",
            "selected declaration artifact has no declared basis",
        )
        return validation, stale_validation, None, code, reason
    validation["declared_basis_present"] = True
    validation["selected_declaration_artifact_validated"] = True
    validation["metadata"] = {
        "resolver_module": artifact.get("resolver_module"),
        "result_version": artifact.get("result_version"),
        "outcome": artifact.get("outcome"),
        "failed_check_count": artifact.get("failed_check_count"),
        "passed_check_count": artifact.get("passed_check_count"),
        "declaration_result": state.get("declaration_result"),
        "decision_code": state.get("decision_code"),
    }
    validation["identity"] = copy.deepcopy(expected_identity)
    validation["posture"] = {
        "declaration_recorded": True,
        "declaration_result_recorded": True,
        "declaration_exhausted": True,
        "receiver_attestation_operation_basis_declaration_recorded": True,
        "receiver_attestation_operation_basis_declared": True,
        "receiver_attestation_operation_basis_supplied": False,
        "receiver_attestation_operation_basis_admitted": False,
        "receiver_attestation_operation_executed": False,
        "receiver_attestation_operation_result_recorded": False,
        "result_level_non_claims_canonical_false": True,
        "complete_material_omitted": True,
    }
    checks.append(_check("selected_declaration_artifact_validated", True))
    return (
        validation,
        stale_validation,
        copy.deepcopy(dict(candidate)),
        None,
        None,
    )


def _basis_shape_valid(basis: Any) -> bool:
    if not isinstance(basis, Mapping):
        return False
    if set(basis) != set(CANDIDATE_FIELDS) or len(basis) != 21:
        return False
    if any(
        basis.get(field) != expected
        for field, expected in EXACT_CANDIDATE_REFERENCES.items()
    ):
        return False
    if basis.get("evaluator_reference") != EXPECTED_EVALUATOR_REFERENCE:
        return False
    expected_postures = {
        "trace_integrity_postures": EXPECTED_TRACE_INTEGRITY_POSTURES,
        "ambiguity_postures": EXPECTED_AMBIGUITY_POSTURES,
        "contradiction_postures": EXPECTED_CONTRADICTION_POSTURES,
        "unresolved_postures": EXPECTED_UNRESOLVED_POSTURES,
    }
    if any(
        not _exact_mapping(basis.get(field), expected)
        for field, expected in expected_postures.items()
    ):
        return False
    return (
        basis.get("non_conversion_statement") == NON_CONVERSION_STATEMENT
        and _exact_false_mapping(
            basis.get("basis_non_claims"),
            REQUIRED_BASIS_NON_CLAIMS,
        )
        and "receiver_attestation_recorded"
        not in _mapping(basis.get("basis_non_claims"))
        and not _contains_forbidden_material(basis)
    )


def _basis_validation_base() -> dict[str, Any]:
    return {
        "exact_21_field_declared_basis_validated": False,
        "declared_basis_references_validated": False,
        "evaluator_reference_validated": False,
        "declared_basis_posture_maps_validated": False,
        "non_conversion_statement_validated": False,
        "basis_non_claims_validated": False,
        "complete_source_material_omitted": True,
        "declared_basis_digest_correspondence_validated": False,
    }


def _validate_declared_basis(
    basis: Mapping[str, Any] | None,
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], str | None, str | None, str | None]:
    validation = _basis_validation_base()
    if not isinstance(basis, Mapping):
        code, reason = _failure(
            checks,
            "declared_basis_mapping",
            "DECLARED_BASIS_MISSING",
            "selected declaration artifact has no declared basis mapping",
        )
        return validation, None, code, reason
    if set(basis) != set(CANDIDATE_FIELDS) or len(basis) != 21:
        code, reason = _failure(
            checks,
            "declared_basis_exact_21_field_schema",
            "DECLARED_BASIS_SCHEMA_MISMATCH",
            "declared basis does not contain the exact 21-field schema",
        )
        return validation, None, code, reason
    validation["exact_21_field_declared_basis_validated"] = True
    checks.append(_check("declared_basis_exact_21_field_schema", True))

    if any(
        basis.get(field) != expected
        for field, expected in EXACT_CANDIDATE_REFERENCES.items()
    ):
        code, reason = _failure(
            checks,
            "declared_basis_exact_references",
            "DECLARED_BASIS_REFERENCE_MISMATCH",
            "declared basis references differ from the selected line",
        )
        return validation, None, code, reason
    validation["declared_basis_references_validated"] = True
    checks.append(_check("declared_basis_exact_references", True))

    if basis.get("evaluator_reference") != EXPECTED_EVALUATOR_REFERENCE:
        code, reason = _failure(
            checks,
            "declared_basis_evaluator_reference",
            "DECLARED_BASIS_EVALUATOR_REFERENCE_MISMATCH",
            "declared basis evaluator reference is invalid",
        )
        return validation, None, code, reason
    validation["evaluator_reference_validated"] = True
    checks.append(_check("declared_basis_evaluator_reference", True))

    expected_postures = {
        "trace_integrity_postures": EXPECTED_TRACE_INTEGRITY_POSTURES,
        "ambiguity_postures": EXPECTED_AMBIGUITY_POSTURES,
        "contradiction_postures": EXPECTED_CONTRADICTION_POSTURES,
        "unresolved_postures": EXPECTED_UNRESOLVED_POSTURES,
    }
    for field, expected in expected_postures.items():
        if not _exact_mapping(basis.get(field), expected):
            code, reason = _failure(
                checks,
                f"declared_basis_{field}_exact",
                "DECLARED_BASIS_POSTURE_MISMATCH",
                f"declared basis {field} is not exact",
            )
            return validation, None, code, reason
        checks.append(_check(f"declared_basis_{field}_exact", True))
    validation["declared_basis_posture_maps_validated"] = True

    if basis.get("non_conversion_statement") != NON_CONVERSION_STATEMENT:
        code, reason = _failure(
            checks,
            "declared_basis_non_conversion_statement",
            "DECLARED_BASIS_NON_CONVERSION_MISMATCH",
            "declared basis non-conversion statement is not exact",
        )
        return validation, None, code, reason
    validation["non_conversion_statement_validated"] = True
    checks.append(_check("declared_basis_non_conversion_statement", True))

    if not _exact_false_mapping(
        basis.get("basis_non_claims"),
        REQUIRED_BASIS_NON_CLAIMS,
    ):
        code, reason = _failure(
            checks,
            "declared_basis_non_claims",
            "DECLARED_BASIS_NON_CLAIM_MISMATCH",
            "declared basis non-claims are not exact canonical false",
        )
        return validation, None, code, reason
    validation["basis_non_claims_validated"] = True
    checks.append(_check("declared_basis_non_claims", True))

    if _contains_forbidden_material(basis):
        code, reason = _failure(
            checks,
            "declared_basis_complete_material_omitted",
            "DECLARED_BASIS_FORBIDDEN_MATERIAL",
            "declared basis contains complete source material",
        )
        return validation, None, code, reason
    checks.append(_check("declared_basis_complete_material_omitted", True))

    try:
        digest = _candidate_digest(basis)
    except (TypeError, ValueError):
        code, reason = _failure(
            checks,
            "declared_basis_digest_computable",
            "DECLARED_BASIS_DIGEST_FAILED",
            "declared basis canonical digest could not be computed",
        )
        return validation, None, code, reason
    if digest != EXPECTED_CANDIDATE_SHA256:
        code, reason = _failure(
            checks,
            "declared_basis_digest_correspondence",
            "DECLARED_BASIS_DIGEST_MISMATCH",
            "declared basis digest does not match declaration metadata",
        )
        return validation, digest, code, reason
    validation["declared_basis_digest_correspondence_validated"] = True
    checks.append(_check("declared_basis_digest_correspondence", True))
    return validation, digest, None, None


def _safe_declared_request(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
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


def _state(
    outcome: str,
    supply_result: str,
    request: Mapping[str, Any],
    *,
    specification_validated: bool,
    declaration_artifact_validated: bool,
    stale_open_list_validated: bool,
    basis_validated: bool,
    digest: str | None,
    decision_code: str,
    decision_reason: str,
) -> dict[str, Any]:
    completed = outcome in {OUTCOME_SUPPLIED, OUTCOME_NOT_SUPPLIED}
    supplied = outcome == OUTCOME_SUPPLIED
    return {
        "supply_id": SUPPLY_ID,
        "supply_type": SUPPLY_TYPE,
        "supply_version": SUPPLY_VERSION,
        "supply_scope": SUPPLY_SCOPE,
        "selected_declaration_id": DECLARATION_ID,
        "selected_preparation_id": SELECTED_PREPARATION_ID,
        "selected_preparation_request_id": SELECTED_PREPARATION_REQUEST_ID,
        "selected_receiver_attestation_operation_id": OPERATION_ID,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        REQUEST_SELECTION_FIELD: (
            request.get(REQUEST_SELECTION_FIELD)
            if _exact_bool(request.get(REQUEST_SELECTION_FIELD))
            else None
        ),
        "supply_result": supply_result,
        "decision_code": decision_code,
        "decision_reason": decision_reason,
        "specification_markers_validated": specification_validated,
        "selected_declaration_artifact_validated": (
            declaration_artifact_validated
        ),
        "declaration_artifact_stale_open_list_entries_disclosed": (
            stale_open_list_validated
        ),
        "declaration_artifact_stale_open_list_entries_preserved": (
            stale_open_list_validated
        ),
        "declaration_artifact_stale_open_list_entries_not_used_as_supply_block": (
            stale_open_list_validated
        ),
        "exact_21_field_declared_basis_validated": basis_validated,
        "declared_basis_digest_algorithm": (
            CANDIDATE_DIGEST_ALGORITHM if digest is not None else None
        ),
        "declared_basis_sha256": digest,
        "declared_basis_digest_correspondence_validated": (
            basis_validated and digest == EXPECTED_CANDIDATE_SHA256
        ),
        "supply_basis_received": basis_validated,
        "supply_recorded": completed,
        "supply_result_recorded": completed,
        "supply_exhausted": completed,
        "receiver_attestation_operation_basis_supply_recorded": supplied,
        "receiver_attestation_operation_basis_declared": completed,
        "receiver_attestation_operation_basis_supplied": supplied,
        "result_level_non_claims_canonical_false": True,
        **_canonical_result_non_claims(),
        **{field: True for field in RESULT_OMISSION_FIELDS},
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    state = _mapping(result.get(PREFIX))
    decision = _mapping(result.get("supply_decision"))
    specification = _mapping(result.get("specification_marker_validation"))
    declaration = _mapping(
        result.get("selected_declaration_artifact_validation")
    )
    stale = _mapping(
        result.get("declaration_artifact_stale_open_list_validation")
    )
    basis = _mapping(result.get("declared_basis_validation"))
    digest = _mapping(result.get("declared_basis_digest"))
    omission = _mapping(result.get("omission_posture"))
    block = _mapping(result.get("block"))
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "supply_id": state.get("supply_id"),
        "supply_type": state.get("supply_type"),
        "supply_version": state.get("supply_version"),
        "supply_scope": state.get("supply_scope"),
        "selected_declaration_id": state.get("selected_declaration_id"),
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
        "selected_declaration_artifact_path": str(
            SELECTED_DECLARATION_ARTIFACT_RELATIVE_PATH
        ),
        "outcome": result.get("outcome"),
        "supply_result": state.get("supply_result"),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": block.get("blocked"),
        "decision_code": decision.get("code"),
        "decision_reason": decision.get("reason"),
        "basis_supply_selected": state.get(REQUEST_SELECTION_FIELD),
        "specification_markers_validated": specification.get(
            "specification_markers_validated"
        ),
        "declaration_artifact_validated": declaration.get(
            "selected_declaration_artifact_validated"
        ),
        "stale_open_list_entries_disclosed": stale.get(
            "declaration_artifact_stale_open_list_entries_disclosed"
        ),
        "stale_open_list_entries_preserved": stale.get(
            "declaration_artifact_stale_open_list_entries_preserved"
        ),
        "stale_open_list_entries_not_used_as_sole_block": stale.get(
            "declaration_artifact_stale_open_list_entries_not_used_as_supply_block"
        ),
        "exact_21_field_declared_basis_validated": basis.get(
            "exact_21_field_declared_basis_validated"
        ),
        "declared_basis_digest_algorithm": digest.get(
            "declared_basis_digest_algorithm"
        ),
        "declared_basis_sha256": digest.get("declared_basis_sha256"),
        "declared_basis_digest_correspondence_validated": digest.get(
            "declared_basis_digest_correspondence_validated"
        ),
        "declared_basis_posture_maps_validated": basis.get(
            "declared_basis_posture_maps_validated"
        ),
        "non_conversion_statement_validated": basis.get(
            "non_conversion_statement_validated"
        ),
        "basis_non_claims_validated": basis.get(
            "basis_non_claims_validated"
        ),
        "supply_recorded": state.get("supply_recorded"),
        "supply_result_recorded": state.get("supply_result_recorded"),
        "supply_exhausted": state.get("supply_exhausted"),
        "supply_basis_received": state.get("supply_basis_received"),
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
    supply_result: str,
    checks: list[dict[str, Any]],
    *,
    specification_validation: Mapping[str, Any] | None = None,
    declaration_validation: Mapping[str, Any] | None = None,
    stale_open_list_validation: Mapping[str, Any] | None = None,
    basis_validation: Mapping[str, Any] | None = None,
    basis: Mapping[str, Any] | None = None,
    digest: str | None = None,
    decision_code: str,
    decision_reason: str,
    block_code: str | None = None,
) -> dict[str, Any]:
    specification = copy.deepcopy(
        dict(
            _specification_validation_base()
            if specification_validation is None
            else specification_validation
        )
    )
    declaration = copy.deepcopy(
        dict(
            _declaration_validation_base()
            if declaration_validation is None
            else declaration_validation
        )
    )
    stale = copy.deepcopy(
        dict(
            _stale_open_list_validation_base()
            if stale_open_list_validation is None
            else stale_open_list_validation
        )
    )
    basis_detail = copy.deepcopy(
        dict(
            _basis_validation_base()
            if basis_validation is None
            else basis_validation
        )
    )
    specification_validated = (
        specification.get("specification_markers_validated") is True
    )
    declaration_validated = (
        declaration.get("selected_declaration_artifact_validated") is True
    )
    stale_validated = (
        stale.get(
            "declaration_artifact_stale_open_list_entries_disclosed"
        )
        is True
        and stale.get(
            "declaration_artifact_stale_open_list_entries_preserved"
        )
        is True
        and stale.get(
            "declaration_artifact_stale_open_list_entries_not_used_as_supply_block"
        )
        is True
    )
    basis_validated = (
        basis_detail.get("exact_21_field_declared_basis_validated") is True
        and basis_detail.get("declared_basis_references_validated") is True
        and basis_detail.get("evaluator_reference_validated") is True
        and basis_detail.get("declared_basis_posture_maps_validated") is True
        and basis_detail.get("non_conversion_statement_validated") is True
        and basis_detail.get("basis_non_claims_validated") is True
        and basis_detail.get("complete_source_material_omitted") is True
        and basis_detail.get(
            "declared_basis_digest_correspondence_validated"
        )
        is True
        and digest == EXPECTED_CANDIDATE_SHA256
    )
    state = _state(
        outcome,
        supply_result,
        request,
        specification_validated=specification_validated,
        declaration_artifact_validated=declaration_validated,
        stale_open_list_validated=stale_validated,
        basis_validated=basis_validated,
        digest=digest,
        decision_code=decision_code,
        decision_reason=decision_reason,
    )
    omission = {field: True for field in RESULT_OMISSION_FIELDS}
    result: dict[str, Any] = {
        f"{PREFIX}_metadata": {
            "supply_id": SUPPLY_ID,
            "supply_type": SUPPLY_TYPE,
            "supply_version": SUPPLY_VERSION,
            "supply_scope": SUPPLY_SCOPE,
        },
        f"declared_{PREFIX}_request": _safe_declared_request(request),
        "selected_supply_declaration_preparation_request_operation_candidate_identity": {
            "supply_id": SUPPLY_ID,
            "supply_type": SUPPLY_TYPE,
            "supply_version": SUPPLY_VERSION,
            "supply_scope": SUPPLY_SCOPE,
            "selected_declaration_id": DECLARATION_ID,
            "selected_declaration_type": DECLARATION_TYPE,
            "selected_declaration_version": DECLARATION_VERSION,
            "selected_declaration_scope": DECLARATION_SCOPE,
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
            "selected_declaration_artifact_path": str(
                SELECTED_DECLARATION_ARTIFACT_RELATIVE_PATH
            ),
        },
        "specification_marker_validation": specification,
        "selected_declaration_artifact_validation": declaration,
        "declaration_artifact_stale_open_list_validation": stale,
        "declared_basis_validation": basis_detail,
        "declared_basis_digest": {
            "declared_basis_digest_algorithm": (
                CANDIDATE_DIGEST_ALGORITHM if digest is not None else None
            ),
            "declared_basis_sha256": digest,
            "declared_basis_digest_correspondence_validated": (
                basis_validated
            ),
            "canonical_json_utf8": digest is not None,
            "canonical_json_sorted_keys": digest is not None,
            "canonical_json_compact_separators": digest is not None,
            "canonical_json_ensure_ascii_false": digest is not None,
            "caller_supplied_digest_used": False,
            "digest_is_correspondence_only": True,
        },
        "supply_decision": {
            "code": decision_code,
            "reason": decision_reason,
            "precedence": "BLOCKED_THEN_NOT_SUPPLIED_THEN_SUPPLIED",
            "caller_selected_result": False,
        },
        PREFIX: state,
        f"{PREFIX}_checks": copy.deepcopy(checks),
        f"{PREFIX}_statement": {
            "one_exact_declared_basis_consumed": basis_validated,
            "prepared_candidate_is_not_declared_basis": True,
            "declared_basis_is_not_supplied_basis": True,
            "supply_records_delivery_only": True,
            "supplied_basis_is_not_admitted_basis": True,
            "admitted_basis_is_not_operation_execution": True,
            "operation_execution_is_not_operation_result": True,
            "open_does_not_mean_next": True,
        },
        f"{PREFIX}_non_meaning": {
            "supply_does_not_repeat_declaration": True,
            "supply_does_not_reread_capture_material": True,
            "supply_does_not_recompute_archive_correspondence": True,
            "supply_does_not_independently_verify_occurrence": True,
            "supply_does_not_admit_basis": True,
            "supply_does_not_satisfy_admission_gate": True,
            "supply_does_not_execute_operation": True,
            "supply_does_not_record_operation_result": True,
            "supply_does_not_record_receiver_attestation": True,
            "supply_does_not_create_receipt_or_presence": True,
            "supply_does_not_repair_stale_open_list": True,
            "supply_exhaustion_does_not_authorize_admission": True,
            "declared_basis_digest_is_correspondence_only": True,
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
    if outcome == OUTCOME_SUPPLIED and basis is not None:
        result[SUPPLIED_BASIS_SECTION] = copy.deepcopy(dict(basis))
    result["failed_check_count"] = sum(
        check.get("passed") is False for check in checks
    )
    result["passed_check_count"] = sum(
        check.get("passed") is True for check in checks
    )
    result[f"{PREFIX}_summary"] = _summary_from_result(result)
    return result


def resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one exact declared-basis supply decision."""
    if request is None:
        working: Mapping[str, Any] = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request()
        )
    elif not isinstance(request, Mapping):
        baseline = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request()
        )
        checks = [_check("request_is_mapping", False, "REQUEST_NOT_MAPPING")]
        return _result(
            baseline,
            OUTCOME_BLOCKED,
            SUPPLY_RESULT_NOT_EVALUATED,
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
            SUPPLY_RESULT_NOT_EVALUATED,
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
            SUPPLY_RESULT_NOT_EVALUATED,
            checks,
            specification_validation=specification,
            decision_code=code,
            decision_reason=reason or "specification validation failed",
            block_code=code,
        )

    (
        declaration,
        stale_open_list,
        basis,
        code,
        reason,
    ) = _validate_declaration_artifact(checks)
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            SUPPLY_RESULT_NOT_EVALUATED,
            checks,
            specification_validation=specification,
            declaration_validation=declaration,
            stale_open_list_validation=stale_open_list,
            decision_code=code,
            decision_reason=reason or "declaration artifact validation failed",
            block_code=code,
        )

    basis_validation, digest, code, reason = _validate_declared_basis(
        basis,
        checks,
    )
    if code is not None:
        return _result(
            working,
            OUTCOME_BLOCKED,
            SUPPLY_RESULT_NOT_EVALUATED,
            checks,
            specification_validation=specification,
            declaration_validation=declaration,
            stale_open_list_validation=stale_open_list,
            basis_validation=basis_validation,
            digest=digest,
            decision_code=code,
            decision_reason=reason or "declared basis validation failed",
            block_code=code,
        )

    checks.append(_check("supply_precedence_applied", True))
    if working.get(REQUEST_SELECTION_FIELD) is False:
        return _result(
            working,
            OUTCOME_NOT_SUPPLIED,
            SUPPLY_RESULT_NOT_SUPPLIED,
            checks,
            specification_validation=specification,
            declaration_validation=declaration,
            stale_open_list_validation=stale_open_list,
            basis_validation=basis_validation,
            digest=digest,
            decision_code="BASIS_NOT_SUPPLIED",
            decision_reason="exact declared basis supply not selected",
        )

    return _result(
        working,
        OUTCOME_SUPPLIED,
        SUPPLY_RESULT_SUPPLIED,
        checks,
        specification_validation=specification,
        declaration_validation=declaration,
        stale_open_list_validation=stale_open_list,
        basis_validation=basis_validation,
        basis=basis,
        digest=digest,
        decision_code="BASIS_SUPPLIED",
        decision_reason="exact declared basis supplied",
    )


def resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Load one explicit strict JSON request mapping and resolve it."""
    value, error = _read_json(request_path)
    if error is not None or not isinstance(value, Mapping):
        baseline = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request()
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
            SUPPLY_RESULT_NOT_EVALUATED,
            checks,
            decision_code=code,
            decision_reason=reason,
            block_code=code,
        )
    return resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min(
        value
    )


def build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic supply summary."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisSupplyV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    return _summary_from_result(result)


def _expected_identity_section() -> dict[str, str]:
    return {
        "supply_id": SUPPLY_ID,
        "supply_type": SUPPLY_TYPE,
        "supply_version": SUPPLY_VERSION,
        "supply_scope": SUPPLY_SCOPE,
        "selected_declaration_id": DECLARATION_ID,
        "selected_declaration_type": DECLARATION_TYPE,
        "selected_declaration_version": DECLARATION_VERSION,
        "selected_declaration_scope": DECLARATION_SCOPE,
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
        "selected_declaration_artifact_path": str(
            SELECTED_DECLARATION_ARTIFACT_RELATIVE_PATH
        ),
    }


def _branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    state = _mapping(result.get(PREFIX))
    block = _mapping(result.get("block"))
    decision = _mapping(result.get("supply_decision"))
    digest = _mapping(result.get("declared_basis_digest"))
    omission = _mapping(result.get("omission_posture"))
    metadata = _mapping(result.get(f"{PREFIX}_metadata"))
    declared_request = _mapping(
        result.get(f"declared_{PREFIX}_request")
    )
    specification = _mapping(result.get("specification_marker_validation"))
    declaration = _mapping(
        result.get("selected_declaration_artifact_validation")
    )
    stale = _mapping(
        result.get("declaration_artifact_stale_open_list_validation")
    )
    basis_validation = _mapping(result.get("declared_basis_validation"))
    identity = _mapping(
        result.get(
            "selected_supply_declaration_preparation_request_operation_candidate_identity"
        )
    )
    statement = _mapping(result.get(f"{PREFIX}_statement"))
    non_meaning = _mapping(result.get(f"{PREFIX}_non_meaning"))
    supplied_basis = result.get(SUPPLIED_BASIS_SECTION)
    expected_sections = set(RESULT_BASE_SECTIONS)
    if outcome == OUTCOME_SUPPLIED:
        expected_sections.add(SUPPLIED_BASIS_SECTION)
    if set(result) != expected_sections:
        return False
    if not _exact_mapping(
        metadata,
        {
            "supply_id": SUPPLY_ID,
            "supply_type": SUPPLY_TYPE,
            "supply_version": SUPPLY_VERSION,
            "supply_scope": SUPPLY_SCOPE,
        },
    ):
        return False
    if not _exact_mapping(identity, _expected_identity_section()):
        return False
    required_non_meaning = (
        "supply_does_not_repeat_declaration",
        "supply_does_not_reread_capture_material",
        "supply_does_not_recompute_archive_correspondence",
        "supply_does_not_independently_verify_occurrence",
        "supply_does_not_admit_basis",
        "supply_does_not_satisfy_admission_gate",
        "supply_does_not_execute_operation",
        "supply_does_not_record_operation_result",
        "supply_does_not_record_receiver_attestation",
        "supply_does_not_create_receipt_or_presence",
        "supply_does_not_repair_stale_open_list",
        "supply_exhaustion_does_not_authorize_admission",
        "declared_basis_digest_is_correspondence_only",
    )
    required_statement = (
        "one_exact_declared_basis_consumed",
        "prepared_candidate_is_not_declared_basis",
        "declared_basis_is_not_supplied_basis",
        "supply_records_delivery_only",
        "supplied_basis_is_not_admitted_basis",
        "admitted_basis_is_not_operation_execution",
        "operation_execution_is_not_operation_result",
        "open_does_not_mean_next",
    )
    if (
        outcome not in OUTCOME_FAMILY
        or state.get("supply_id") != SUPPLY_ID
        or state.get("supply_type") != SUPPLY_TYPE
        or state.get("supply_version") != SUPPLY_VERSION
        or state.get("supply_scope") != SUPPLY_SCOPE
        or state.get("selected_declaration_id") != DECLARATION_ID
        or state.get("selected_preparation_id") != SELECTED_PREPARATION_ID
        or state.get("selected_preparation_request_id")
        != SELECTED_PREPARATION_REQUEST_ID
        or state.get("selected_receiver_attestation_operation_id")
        != OPERATION_ID
        or state.get("receiver_side_answerable_basis_candidate_id")
        != CANDIDATE_ID
        or decision.get("precedence")
        != "BLOCKED_THEN_NOT_SUPPLIED_THEN_SUPPLIED"
        or decision.get("caller_selected_result") is not False
        or decision.get("code") != state.get("decision_code")
        or decision.get("reason") != state.get("decision_reason")
        or declared_request.get(REQUEST_SELECTION_FIELD)
        != state.get(REQUEST_SELECTION_FIELD)
        or specification.get("specification_markers_validated")
        is not state.get("specification_markers_validated")
        or declaration.get("selected_declaration_artifact_validated")
        is not state.get("selected_declaration_artifact_validated")
        or stale.get(
            "declaration_artifact_stale_open_list_entries_disclosed"
        )
        is not state.get(
            "declaration_artifact_stale_open_list_entries_disclosed"
        )
        or stale.get(
            "declaration_artifact_stale_open_list_entries_preserved"
        )
        is not state.get(
            "declaration_artifact_stale_open_list_entries_preserved"
        )
        or stale.get(
            "declaration_artifact_stale_open_list_entries_not_used_as_supply_block"
        )
        is not state.get(
            "declaration_artifact_stale_open_list_entries_not_used_as_supply_block"
        )
        or stale.get("declaration_artifact_stale_open_list_entries")
        != list(STALE_OPEN_LIST_ENTRIES)
        or stale.get(
            "declaration_artifact_stale_open_list_repaired"
        )
        is not False
        or stale.get(
            "declaration_artifact_stale_open_list_normalized"
        )
        is not False
        or digest.get("declared_basis_sha256")
        != state.get("declared_basis_sha256")
        or digest.get("declared_basis_digest_algorithm")
        != state.get("declared_basis_digest_algorithm")
        or digest.get(
            "declared_basis_digest_correspondence_validated"
        )
        is not state.get(
            "declared_basis_digest_correspondence_validated"
        )
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
        or set(non_meaning) != set(required_non_meaning)
        or any(non_meaning.get(field) is not True for field in required_non_meaning)
        or set(statement) != set(required_statement)
        or any(
            statement.get(field) is not True
            for field in required_statement
            if field != "one_exact_declared_basis_consumed"
        )
        or statement.get("one_exact_declared_basis_consumed")
        is not (
            basis_validation.get(
                "declared_basis_digest_correspondence_validated"
            )
            is True
        )
        or state.get("result_level_non_claims_canonical_false") is not True
    ):
        return False

    if outcome in {OUTCOME_SUPPLIED, OUTCOME_NOT_SUPPLIED}:
        common = (
            state.get("supply_recorded") is True
            and state.get("supply_result_recorded") is True
            and state.get("supply_exhausted") is True
            and state.get("supply_basis_received") is True
            and state.get("receiver_attestation_operation_basis_declared")
            is True
            and state.get("specification_markers_validated") is True
            and state.get("selected_declaration_artifact_validated") is True
            and state.get("exact_21_field_declared_basis_validated") is True
            and state.get(
                "declared_basis_digest_correspondence_validated"
            )
            is True
            and digest.get("declared_basis_digest_algorithm")
            == CANDIDATE_DIGEST_ALGORITHM
            and digest.get("declared_basis_sha256")
            == EXPECTED_CANDIDATE_SHA256
            and digest.get(
                "declared_basis_digest_correspondence_validated"
            )
            is True
            and block.get("blocked") is False
            and block.get("code") is None
            and block.get("block_code") is None
            and block.get("reason") is None
        )
        if not common:
            return False
    if outcome == OUTCOME_SUPPLIED:
        return (
            state.get("supply_result") == SUPPLY_RESULT_SUPPLIED
            and state.get(REQUEST_SELECTION_FIELD) is True
            and state.get(
                "receiver_attestation_operation_basis_supply_recorded"
            )
            is True
            and state.get("receiver_attestation_operation_basis_supplied")
            is True
            and decision.get("code") == "BASIS_SUPPLIED"
            and decision.get("reason") == "exact declared basis supplied"
            and _basis_shape_valid(supplied_basis)
            and _candidate_digest(_mapping(supplied_basis))
            == EXPECTED_CANDIDATE_SHA256
        )
    if outcome == OUTCOME_NOT_SUPPLIED:
        return (
            SUPPLIED_BASIS_SECTION not in result
            and state.get("supply_result") == SUPPLY_RESULT_NOT_SUPPLIED
            and state.get(REQUEST_SELECTION_FIELD) is False
            and state.get(
                "receiver_attestation_operation_basis_supply_recorded"
            )
            is False
            and state.get("receiver_attestation_operation_basis_supplied")
            is False
            and decision.get("code") == "BASIS_NOT_SUPPLIED"
            and decision.get("reason")
            == "exact declared basis supply not selected"
        )
    return (
        SUPPLIED_BASIS_SECTION not in result
        and state.get("supply_result") == SUPPLY_RESULT_NOT_EVALUATED
        and state.get("supply_recorded") is False
        and state.get("supply_result_recorded") is False
        and state.get("supply_exhausted") is False
        and state.get(
            "receiver_attestation_operation_basis_supply_recorded"
        )
        is False
        and state.get("receiver_attestation_operation_basis_supplied")
        is False
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
    raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisSupplyV0MinError(
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
        SELECTED_DECLARATION_ARTIFACT_PATH.parent.resolve(strict=False),
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
        ReceiverSideAnswerableBasisReceiverAttestationOperationBasisSupplyV0MinError
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
    if result.get("blocked_routes") != list(BLOCKED_ROUTES):
        raise error("WRITE_REFUSED: blocked routes are inconsistent")
    if result.get("what_remains_open") != list(WHAT_REMAINS_OPEN):
        raise error("WRITE_REFUSED: open posture is inconsistent")

    declared_request = _mapping(result.get(f"declared_{PREFIX}_request"))
    expected_request_keys = {
        *_expected_request_values(),
        REQUEST_SELECTION_FIELD,
        "declared_non_claims_validated",
        "prohibited_input_flags_validated",
    }
    if (
        set(declared_request) != expected_request_keys
        or any(
            declared_request.get(field) != expected
            for field, expected in _expected_request_values().items()
        )
    ):
        raise error("WRITE_REFUSED: declared request posture is inconsistent")
    if result.get("outcome") != OUTCOME_BLOCKED and (
        declared_request.get("declared_non_claims_validated") is not True
        or declared_request.get("prohibited_input_flags_validated") is not True
    ):
        raise error("WRITE_REFUSED: lawful request posture is inconsistent")

    digest = _mapping(result.get("declared_basis_digest"))
    if (
        digest.get("caller_supplied_digest_used") is not False
        or digest.get("digest_is_correspondence_only") is not True
    ):
        raise error("WRITE_REFUSED: digest posture is inconsistent")
    omission = _mapping(result.get("omission_posture"))
    if (
        set(omission) != set(RESULT_OMISSION_FIELDS)
        or any(
            omission.get(field) is not True
            for field in RESULT_OMISSION_FIELDS
        )
    ):
        raise error("WRITE_REFUSED: omission posture is inconsistent")

    stale = _mapping(
        result.get("declaration_artifact_stale_open_list_validation")
    )
    if (
        stale.get("declaration_artifact_stale_open_list_repaired") is not False
        or stale.get("declaration_artifact_stale_open_list_normalized")
        is not False
    ):
        raise error("WRITE_REFUSED: stale open-list change is present")

    outcome = result.get("outcome")
    if outcome in {OUTCOME_SUPPLIED, OUTCOME_NOT_SUPPLIED}:
        basis_validation = _mapping(result.get("declared_basis_validation"))
        required_basis_validation = (
            "exact_21_field_declared_basis_validated",
            "declared_basis_references_validated",
            "evaluator_reference_validated",
            "declared_basis_posture_maps_validated",
            "non_conversion_statement_validated",
            "basis_non_claims_validated",
            "complete_source_material_omitted",
            "declared_basis_digest_correspondence_validated",
        )
        if any(
            basis_validation.get(field) is not True
            for field in required_basis_validation
        ):
            raise error("WRITE_REFUSED: declared basis validation is incomplete")
        declaration_validation = _mapping(
            result.get("selected_declaration_artifact_validation")
        )
        if declaration_validation.get(
            "selected_declaration_artifact_validated"
        ) is not True:
            raise error(
                "WRITE_REFUSED: declaration artifact validation is incomplete"
            )
        if any(
            stale.get(field) is not True
            for field in (
                "declaration_artifact_stale_open_list_entries_disclosed",
                "declaration_artifact_stale_open_list_entries_preserved",
                "declaration_artifact_stale_open_list_entries_not_used_as_supply_block",
            )
        ):
            raise error(
                "WRITE_REFUSED: stale open-list disclosure posture is incomplete"
            )

    if outcome == OUTCOME_SUPPLIED:
        supplied_basis = result.get(SUPPLIED_BASIS_SECTION)
        if not _basis_shape_valid(supplied_basis):
            raise error("WRITE_REFUSED: supplied basis is malformed")
        try:
            supplied_digest = _candidate_digest(_mapping(supplied_basis))
        except (TypeError, ValueError) as exc:
            raise error("WRITE_REFUSED: supplied basis digest failed") from exc
        if (
            supplied_digest != EXPECTED_CANDIDATE_SHA256
            or digest.get("declared_basis_sha256") != supplied_digest
        ):
            raise error("WRITE_REFUSED: supplied basis digest mismatch")

        upstream_checks: list[dict[str, Any]] = []
        (
            _declaration,
            _stale,
            upstream_basis,
            upstream_code,
            _upstream_reason,
        ) = _validate_declaration_artifact(upstream_checks)
        if (
            upstream_code is not None
            or not isinstance(upstream_basis, Mapping)
            or dict(supplied_basis) != dict(upstream_basis)
        ):
            raise error(
                "WRITE_REFUSED: supplied basis differs from declared basis"
            )

    summary = result.get(f"{PREFIX}_summary")
    if (
        not isinstance(summary, Mapping)
        or dict(summary) != _summary_from_result(result)
    ):
        raise error("WRITE_REFUSED: summary is inconsistent")


def write_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid supply result without silent overwrite."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisSupplyV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    _validate_write_result(result)
    target = (
        _as_repo_path(output_path)
        if output_path is not None
        else OUTPUT_ROOT / OUTPUT_FILENAME
    )
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisSupplyV0MinError(
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
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationBasisSupplyV0MinError(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
