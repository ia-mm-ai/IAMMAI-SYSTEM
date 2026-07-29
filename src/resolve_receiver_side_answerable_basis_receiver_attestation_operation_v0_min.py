"""Resolve one bounded receiver-attestation operation.

The resolver consumes one exact allowed and exhausted v2 consideration
boundary.  An absent separately supplied basis is lawful waiting.  A supplied
basis is admitted atomically, and exactly one completed result is derived
without creating the originating occurrence, receipt, presence, or standing.
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
    "resolve_receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min"
)

OPERATION_ID = (
    "receiver_side_answerable_basis_receiver_attestation_operation_001"
)
OPERATION_TYPE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION"
)
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = (
    "ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_"
    "FOR_ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY"
)

CANDIDATE_ID = "receiver_side_answerable_basis_candidate_001"
CANDIDATE_TYPE = "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
CANDIDATE_SCOPE = (
    "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY"
)
SELECTED_SUFFICIENCY_OPERATION_ID = (
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001"
)
SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT"
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
SELECTED_BOUNDARY_OUTCOME_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_BOUNDARY_ALLOWED"
)
SELECTED_BOUNDARY_RESULT_REQUIRED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_CONSIDERATION_ALLOWED"
)

ADMISSIBLE_FUTURE_ROUTE = (
    "RECEIVER_ATTESTATION_OPERATION_THEN_RECEIVER_ANSWERABLE_RECEIPT_"
    "BOUNDARY_ONLY_IF_RECEIVER_ATTESTATION_RECORDED"
)
REQUIRED_FUTURE_ROUTE = ADMISSIBLE_FUTURE_ROUTE

OUTCOME_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_NOT_RECORDED"
)
OUTCOME_INDETERMINATE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_INDETERMINATE"
)
OUTCOME_REQUIRES_BASIS = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
    "REQUIRES_OPERATION_BASIS"
)
OUTCOME_BLOCKED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_INDETERMINATE,
    OUTCOME_REQUIRES_BASIS,
    OUTCOME_BLOCKED,
)

OPERATION_RESULT_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED"
)
OPERATION_RESULT_NOT_RECORDED = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_NOT_RECORDED"
)
OPERATION_RESULT_INDETERMINATE = (
    "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_INDETERMINATE"
)
COMPLETED_OPERATION_RESULT_FAMILY = (
    OPERATION_RESULT_RECORDED,
    OPERATION_RESULT_NOT_RECORDED,
    OPERATION_RESULT_INDETERMINATE,
)
OPERATION_RESULT_FAMILY = COMPLETED_OPERATION_RESULT_FAMILY

INTENT_RECORD = (
    "RECORD_RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION"
)
INTENT_BLOCK = (
    "BLOCK_RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH = Path(
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_V0_MIN_SPEC.md"
)
SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2/"
    "receiver_side_answerable_basis_receiver_attestation_boundary_001__"
    "receiver_side_answerable_basis_receiver_attestation_"
    "boundary_v0_min_v2_result.json"
)
BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH = Path(
    "artifacts/actual_receiver_attestation_capture/"
    "receiver_attestation_capture_001"
)
SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH = Path(
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_"
    "operation_v0_min_result_001.json"
)

GOVERNING_OPERATION_SPECIFICATION_PATH = (
    REPO_ROOT / GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH
)
SELECTED_BOUNDARY_ARTIFACT_PATH = (
    REPO_ROOT / SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
)
BOUNDED_CAPTURE_DIRECTORY_PATH = (
    REPO_ROOT / BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
)
SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_PATH = (
    REPO_ROOT / SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
)
GOVERNING_SPEC_RELATIVE_PATH = GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH
GOVERNING_SPEC_PATH = GOVERNING_OPERATION_SPECIFICATION_PATH

OUTPUT_ROOT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min"
)
OUTPUT_FILENAME = (
    "receiver_side_answerable_basis_receiver_attestation_operation_001__"
    "receiver_side_answerable_basis_receiver_attestation_"
    "operation_v0_min_result.json"
)

EXPECTED_ARCHIVE_SHA256 = (
    "a45a621c5c6c2f37daefd7e896f32cdb50bff21ab69ec9281912049bd326724c"
)

COMPONENT_RELATIVE_PATHS = MappingProxyType(
    {
        "preserved_archive_path": (
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "original_zip/receiver_attestation_001.zip"
        ),
        "archive_hash_record_path": (
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "hashes/receiver_attestation_001.sha256"
        ),
        "attestation_statement_path": (
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/attestation_statement.txt"
        ),
        "attestation_timestamp_path": (
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/attested_at.txt"
        ),
        "capture_method_path": (
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/capture_method.txt"
        ),
        "capture_only_statement_path": (
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/"
            "capture_only_statement.txt"
        ),
        "freely_given_statement_path": (
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/"
            "freely_given_statement.txt"
        ),
        "knock_reference_path": (
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/knock_reference.txt"
        ),
        "receiver_label_path": (
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/receiver_label.txt"
        ),
        "receiver_working_directory_path": (
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/"
            "receiver_working_directory.txt"
        ),
        "recorded_signal_path": (
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "extracted/receiver_attestation_001/"
            "knock_20260727_215052.json"
        ),
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

BASIS_FIELDS = (
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

NON_CONVERSION_STATEMENT = (
    "bounded trace admission and recording do not establish occurrence "
    "creation, identity, independent custody, verified provenance, physical "
    "validity, current presence, receiver-answerable receipt, truth, "
    "authority, or standing."
)

REQUIRED_FALSE_NON_CLAIMS = (
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
REQUIRED_BASIS_NON_CLAIMS = REQUIRED_FALSE_NON_CLAIMS

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

REQUIRED_UPSTREAM_DECLARATIONS = MappingProxyType(
    {
        "resolver_module": SELECTED_BOUNDARY_RESOLVER_MODULE,
        "result_version": SELECTED_BOUNDARY_RESULT_VERSION,
        "failed_check_count": 0,
        "boundary_id": SELECTED_BOUNDARY_ID,
        "boundary_type": SELECTED_BOUNDARY_TYPE,
        "boundary_version": SELECTED_BOUNDARY_VERSION,
        "boundary_scope": SELECTED_BOUNDARY_SCOPE,
        "selected_candidate_id": CANDIDATE_ID,
        "selected_sufficiency_operation_id": (
            SELECTED_SUFFICIENCY_OPERATION_ID
        ),
        "selected_sufficiency_operation_result_required": (
            SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
        ),
        "outcome": SELECTED_BOUNDARY_OUTCOME_REQUIRED,
        "boundary_result": SELECTED_BOUNDARY_RESULT_REQUIRED,
        "receiver_attestation_boundary_recorded": True,
        "receiver_attestation_boundary_result_recorded": True,
        "receiver_attestation_consideration_allowed": True,
        "receiver_attestation_consideration_not_allowed": False,
        "receiver_attestation_boundary_exhausted": True,
        "bounded_material_selected_for_consideration": True,
        "specification_markers_validated": True,
        "selected_operation_validated": True,
        "eight_dimensions_validated": True,
        "upstream_false_locks_validated": True,
        "result_level_non_claims_canonical_false": True,
        "complete_operation_artifact_omitted": True,
        "complete_sufficiency_basis_omitted": True,
        "complete_capture_signal_data_omitted": True,
    }
)

PROHIBITED_REQUEST_FLAGS = MappingProxyType(
    {
        "request_outcome_preclaim": "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "request_operation_result_preclaim": (
            "PROHIBITED_RESULT_PRECLAIM_REQUESTED"
        ),
        "request_receiver_attestation_recorded_preclaim": (
            "PROHIBITED_RESULT_PRECLAIM_REQUESTED"
        ),
        "request_receiver_attestation_not_recorded_preclaim": (
            "PROHIBITED_RESULT_PRECLAIM_REQUESTED"
        ),
        "request_receiver_attestation_indeterminate_preclaim": (
            "PROHIBITED_RESULT_PRECLAIM_REQUESTED"
        ),
        "request_dimension_result": "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "request_complete_archive_embedding": (
            "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
        ),
        "request_complete_signal_body_embedding": (
            "PROHIBITED_COMPLETE_MATERIAL_REQUESTED"
        ),
        "request_receiver_answerable_receipt_creation": (
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
        "request_authority_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_standing_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_truth_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_relation_creation": (
            "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED"
        ),
        "request_coupling_creation": (
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
        "request_contaminated_lineage_validation": (
            "PROHIBITED_CONTAMINATED_LINEAGE_VALIDATION_REQUESTED"
        ),
    }
)

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "REQUEST_FIELD_MISSING",
        "REQUEST_UNKNOWN_FIELD",
        "REQUEST_VALUE_MISMATCH",
        "UNSUPPORTED_INTENT",
        "EXPLICIT_BLOCK_REQUESTED",
        "RESULT_POSTURE_PRECLAIMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "PROHIBITED_RESULT_PRECLAIM_REQUESTED",
        "PROHIBITED_COMPLETE_MATERIAL_REQUESTED",
        "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
        "PROHIBITED_REPEATED_USE_REQUESTED",
        "PROHIBITED_REPAIR_SCAN_DISCOVERY_OR_VALIDATION_REQUESTED",
        "PROHIBITED_CONTAMINATED_LINEAGE_VALIDATION_REQUESTED",
        "OPERATION_SPEC_REFERENCE_MISSING",
        "OPERATION_SPEC_MARKER_MISSING",
        "SELECTED_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
        "SELECTED_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
        "SELECTED_BOUNDARY_ARTIFACT_NOT_MAPPING",
        "SELECTED_BOUNDARY_METADATA_MISMATCH",
        "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
        "SELECTED_BOUNDARY_POSTURE_INVALID",
        "UPSTREAM_FALSE_LOCK_NOT_FALSE",
        "OPERATION_BASIS_NOT_MAPPING",
        "OPERATION_BASIS_FIELD_MISSING",
        "OPERATION_BASIS_UNKNOWN_FIELD",
        "OPERATION_BASIS_PATH_MISMATCH",
        "OPERATION_BASIS_HASH_MISMATCH",
        "OPERATION_BASIS_EVALUATOR_REFERENCE_INVALID",
        "OPERATION_BASIS_POSTURE_MAP_INVALID",
        "OPERATION_BASIS_TRACE_INTEGRITY_NOT_TRUE",
        "OPERATION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
        "OPERATION_BASIS_NON_CONVERSION_INVALID",
        "BOUNDED_COMPONENT_UNAVAILABLE",
        "ARCHIVE_HASH_RECORD_MALFORMED",
        "ARCHIVE_HASH_MISMATCH",
        "WRITE_REFUSED",
    }
)

SPEC_MARKER_FAMILIES = MappingProxyType(
    {
        "title": (
            "# Receiver-Side Answerable Basis Receiver Attestation "
            "Operation V0 Minimum Specification",
        ),
        "operation_identity": (
            f"operation_id = {OPERATION_ID}",
            f"operation_type = {OPERATION_TYPE}",
            f"operation_version = {OPERATION_VERSION}",
            f"operation_scope = {OPERATION_SCOPE}",
        ),
        "upstream_boundary": (
            str(SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH),
            SELECTED_BOUNDARY_OUTCOME_REQUIRED,
            SELECTED_BOUNDARY_RESULT_REQUIRED,
        ),
        "bounded_capture": (
            str(BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH) + "/",
            EXPECTED_ARCHIVE_SHA256,
        ),
        "basis_schema": (
            "The basis must contain exactly:",
            *BASIS_FIELDS,
        ),
        "outcomes": OUTCOME_FAMILY,
        "completed_results": COMPLETED_OPERATION_RESULT_FAMILY,
        "precedence": (
            "`INDETERMINATE` takes precedence over `NOT_RECORDED`",
            "`NOT_RECORDED` takes precedence over `RECORDED`",
        ),
        "separation": (
            "Occurrence is not artifact.",
            "Artifact does not create the occurrence.",
            "Preserved trace is not independent verification.",
            "Consideration allowed is not receiver attestation.",
            (
                "Receiver attestation recorded is not "
                "receiver-answerable receipt."
            ),
            "Receiver attestation recorded is not presence.",
        ),
        "waiting_blocked_not_exhausted": (
            "Waiting and blocked postures are not exhausted.",
        ),
        "open_not_next": ("Open does not mean next.",),
    }
)
SPEC_MARKERS = tuple(
    marker
    for markers in SPEC_MARKER_FAMILIES.values()
    for marker in markers
)

BLOCKED_ROUTES = (
    "candidate_sufficiency_to_attestation_recording",
    "consideration_allowed_to_attestation_recording",
    "capture_package_existence_to_attestation_recording",
    "hash_match_to_identity_truth_presence_authority_or_standing",
    "attestation_recording_to_receiver_answerable_receipt_or_presence",
    "attestation_recording_to_identity_authority_truth_standing_relation_or_coupling",
    "completed_operation_to_repeated_permission_route_rerun_retry_debt_or_obligation",
    "operation_to_contaminated_lineage_repair_or_validation",
)

WAITING_WHAT_REMAINS_OPEN = (
    "separately supplied bounded receiver-attestation operation basis",
)
COMPLETED_WHAT_REMAINS_OPEN = (
    "receiver-answerable-receipt boundary, only after a separately recorded attestation result",
    "presence re-evaluation",
    "identity",
    "authority",
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
BLOCKED_WHAT_REMAINS_OPEN = (
    "receiver-attestation operation under a separately valid bounded request",
)

RESULT_SECTIONS = frozenset(
    {
        "receiver_side_answerable_basis_receiver_attestation_operation_metadata",
        "declared_receiver_side_answerable_basis_receiver_attestation_operation_basis",
        "selected_operation_and_candidate_identity",
        "upstream_boundary_basis",
        "supplied_operation_basis_admission_metadata",
        "bounded_component_validation",
        "trace_posture_metadata",
        "receiver_side_answerable_basis_receiver_attestation_operation",
        "operation_result_detail",
        "operation_posture",
        "receiver_side_answerable_basis_receiver_attestation_operation_checks",
        "receiver_side_answerable_basis_receiver_attestation_operation_statement",
        "receiver_side_answerable_basis_receiver_attestation_operation_non_meaning",
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
        "receiver_side_answerable_basis_receiver_attestation_operation_summary",
    }
)


class ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
    Exception
):
    """Raised when one bounded result cannot be summarized or written."""


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


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _canonical_basis_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_BASIS_NON_CLAIMS}


def _canonical_upstream_declarations() -> dict[str, Any]:
    return copy.deepcopy(dict(REQUIRED_UPSTREAM_DECLARATIONS))


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


def _add_failure(
    checks: list[dict[str, Any]],
    name: str,
    code: str,
) -> None:
    checks.append(_check(name, False, code))


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
        and all(value.get(field) is False for field in REQUIRED_FALSE_NON_CLAIMS)
    )


def _basis_non_claims_valid(value: Any) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(REQUIRED_BASIS_NON_CLAIMS)
        and all(value.get(field) is False for field in REQUIRED_BASIS_NON_CLAIMS)
    )


def _expected_request_values() -> dict[str, Any]:
    return {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "receiver_side_answerable_basis_candidate_id": CANDIDATE_ID,
        "receiver_side_answerable_basis_candidate_type": CANDIDATE_TYPE,
        "receiver_side_answerable_basis_candidate_scope": CANDIDATE_SCOPE,
        "selected_candidate_sufficiency_operation_id": (
            SELECTED_SUFFICIENCY_OPERATION_ID
        ),
        "selected_candidate_sufficiency_operation_result_required": (
            SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
        ),
        "governing_receiver_attestation_operation_specification_path": str(
            GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH
        ),
        "selected_receiver_attestation_boundary_artifact_path": str(
            SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
        ),
        "bounded_capture_directory_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
        ),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "required_upstream_declarations": (
            _canonical_upstream_declarations()
        ),
    }


def build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request(
    receiver_attestation_operation_basis: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one canonical request with no manufactured operation basis."""
    if isinstance(receiver_attestation_operation_basis, Mapping):
        basis: Any = copy.deepcopy(
            dict(receiver_attestation_operation_basis)
        )
    elif receiver_attestation_operation_basis is None:
        basis = None
    else:
        basis = copy.deepcopy(receiver_attestation_operation_basis)
    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **_expected_request_values(),
        "declared_non_claims": _canonical_non_claims(),
        "receiver_attestation_operation_basis": basis,
    }
    request.update({field: False for field in PROHIBITED_REQUEST_FLAGS})
    request.update(copy.deepcopy(overrides))
    return request


def build_declared_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request(
    receiver_attestation_operation_basis: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one declared request while retaining bounded overrides."""
    return (
        build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request(
            receiver_attestation_operation_basis=(
                receiver_attestation_operation_basis
            ),
            **overrides
        )
    )


def _request_keys() -> set[str]:
    return {
        "intent",
        "declared_non_claims",
        "receiver_attestation_operation_basis",
        *_expected_request_values(),
        *PROHIBITED_REQUEST_FLAGS,
    }


def _request_preclaim_fields() -> set[str]:
    return {
        "outcome",
        "operation_result",
        "receiver_attestation_operation_result",
        "receiver_attestation_operation_recorded",
        "receiver_attestation_operation_result_recorded",
        "receiver_attestation_operation_exhausted",
        "receiver_attestation_decided",
        "receiver_attestation_recorded",
        "receiver_attestation_not_recorded",
        "receiver_attestation_indeterminate",
        "dimension_result",
        "complete_archive",
        "archive_bytes",
        "complete_signal_body",
        "signal_samples",
        *REQUIRED_FALSE_NON_CLAIMS,
    }


def _validate_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None]:
    if request.get("intent") == INTENT_BLOCK:
        return "EXPLICIT_BLOCK_REQUESTED", "explicit block intent was requested"
    if request.get("intent") not in SUPPORTED_INTENTS:
        return "UNSUPPORTED_INTENT", "intent is not supported"

    if set(request).intersection(_request_preclaim_fields()):
        return (
            "RESULT_POSTURE_PRECLAIMED",
            "caller supplied a result, branch posture, or complete material",
        )

    expected_keys = _request_keys()
    if expected_keys.difference(request):
        return "REQUEST_FIELD_MISSING", "canonical request fields are missing"
    if set(request).difference(expected_keys):
        return "REQUEST_UNKNOWN_FIELD", "request contains unknown fields"

    for field, expected in _expected_request_values().items():
        actual = request.get(field)
        valid = actual == expected
        checks.append(_check("request." + field, valid, "REQUEST_VALUE_MISMATCH"))
        if not valid:
            return (
                "REQUEST_VALUE_MISMATCH",
                field + " does not match the canonical request",
            )

    if not _non_claims_valid(request.get("declared_non_claims")):
        return (
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "declared non-claims must be the exact canonical false set",
        )
    checks.append(_check("request.declared_non_claims", True))

    basis = request.get("receiver_attestation_operation_basis")
    if basis is not None and not isinstance(basis, Mapping):
        return (
            "OPERATION_BASIS_NOT_MAPPING",
            "supplied operation basis must be a mapping",
        )

    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        valid = request.get(field) is False
        checks.append(_check("request." + field, valid, code))
        if not valid:
            return code, field + " must remain false"
    return None, None


def _empty_upstream_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "governing_paths": {
            "governing_operation_specification_path": request.get(
                "governing_receiver_attestation_operation_specification_path"
            ),
            "selected_boundary_artifact_path": request.get(
                "selected_receiver_attestation_boundary_artifact_path"
            ),
            "bounded_capture_directory_path": request.get(
                "bounded_capture_directory_path"
            ),
        },
        "specification_marker_validation": {
            family: False for family in SPEC_MARKER_FAMILIES
        },
        "selected_boundary_metadata": {},
        "selected_boundary_identity": {},
        "selected_boundary_posture_validation": {},
        "upstream_false_lock_validation": {},
        "upstream_non_claim_validation": {},
        "upstream_boundary_validated": False,
        "complete_upstream_boundary_artifact_omitted": True,
        "complete_candidate_sufficiency_artifact_omitted": True,
        "complete_candidate_sufficiency_basis_omitted": True,
    }


def _validate_specification(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    upstream: dict[str, Any],
) -> tuple[str | None, str | None]:
    text, error = _read_text(
        request[
            "governing_receiver_attestation_operation_specification_path"
        ]
    )
    if error is not None or text is None:
        return (
            "OPERATION_SPEC_REFERENCE_MISSING",
            "governing operation specification is unavailable",
        )
    for family, markers in SPEC_MARKER_FAMILIES.items():
        valid = all(marker in text for marker in markers)
        upstream["specification_marker_validation"][family] = valid
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
            )
    return None, None


def _validate_upstream_boundary(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    upstream = _empty_upstream_basis(request)
    code, reason = _validate_specification(request, checks, upstream)
    if code is not None:
        return code, reason, upstream

    artifact, error = _read_json(
        request["selected_receiver_attestation_boundary_artifact_path"]
    )
    if error in {"not_a_file", "unreadable"}:
        return (
            "SELECTED_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
            "selected boundary artifact is unavailable",
            upstream,
        )
    if error is not None:
        return (
            "SELECTED_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
            "selected boundary artifact is not parseable canonical JSON",
            upstream,
        )
    if not isinstance(artifact, Mapping):
        return (
            "SELECTED_BOUNDARY_ARTIFACT_NOT_MAPPING",
            "selected boundary artifact is not a mapping",
            upstream,
        )

    boundary = artifact.get(
        "receiver_side_answerable_basis_receiver_attestation_boundary"
    )
    summary = artifact.get(
        "receiver_side_answerable_basis_"
        "receiver_attestation_boundary_summary"
    )
    non_claims = artifact.get("non_claims")
    if not all(
        isinstance(value, Mapping)
        for value in (boundary, summary, non_claims)
    ):
        return (
            "SELECTED_BOUNDARY_ARTIFACT_NOT_MAPPING",
            "selected boundary artifact lacks canonical result sections",
            upstream,
        )

    upstream["selected_boundary_metadata"] = {
        "resolver_module": artifact.get("resolver_module"),
        "result_version": artifact.get("result_version"),
        "outcome": artifact.get("outcome"),
        "failed_check_count": artifact.get("failed_check_count"),
    }
    upstream["selected_boundary_identity"] = {
        "boundary_id": boundary.get("boundary_id"),
        "boundary_type": boundary.get("boundary_type"),
        "boundary_version": boundary.get("boundary_version"),
        "boundary_scope": boundary.get("boundary_scope"),
        "selected_candidate_id": boundary.get(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "selected_sufficiency_operation_id": boundary.get(
            "selected_candidate_sufficiency_operation_id"
        ),
        "selected_sufficiency_operation_result_required": boundary.get(
            "selected_candidate_sufficiency_operation_result_required"
        ),
    }

    metadata_expectations = (
        (
            "resolver_module",
            artifact.get("resolver_module"),
            SELECTED_BOUNDARY_RESOLVER_MODULE,
        ),
        (
            "result_version",
            artifact.get("result_version"),
            SELECTED_BOUNDARY_RESULT_VERSION,
        ),
        (
            "outcome",
            artifact.get("outcome"),
            SELECTED_BOUNDARY_OUTCOME_REQUIRED,
        ),
    )
    for field, actual, expected in metadata_expectations:
        valid = actual == expected
        checks.append(
            _check(
                "upstream.metadata." + field,
                valid,
                "SELECTED_BOUNDARY_METADATA_MISMATCH",
            )
        )
        if not valid:
            return (
                "SELECTED_BOUNDARY_METADATA_MISMATCH",
                "selected boundary metadata does not match: " + field,
                upstream,
            )

    failed_count = artifact.get("failed_check_count")
    valid_failed_count = type(failed_count) is int and failed_count == 0
    checks.append(
        _check(
            "upstream.metadata.failed_check_count",
            valid_failed_count,
            "SELECTED_BOUNDARY_METADATA_MISMATCH",
        )
    )
    if not valid_failed_count:
        return (
            "SELECTED_BOUNDARY_METADATA_MISMATCH",
            "selected boundary failed-check count is not exact zero",
            upstream,
        )

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
            SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
        ),
    }
    for field, expected in identity_expectations.items():
        valid = boundary.get(field) == expected
        checks.append(
            _check(
                "upstream.identity." + field,
                valid,
                "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            )
        )
        if not valid:
            return (
                "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
                "selected boundary identity does not match: " + field,
                upstream,
            )

    boundary_expectations = {
        "receiver_attestation_boundary_result": (
            SELECTED_BOUNDARY_RESULT_REQUIRED
        ),
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
    posture_validation: dict[str, bool] = {}
    for field, expected in boundary_expectations.items():
        actual = boundary.get(field)
        valid = actual is expected if type(expected) is bool else actual == expected
        posture_validation[field] = valid
        checks.append(
            _check(
                "upstream.posture." + field,
                valid,
                "SELECTED_BOUNDARY_POSTURE_INVALID",
            )
        )
        if not valid:
            upstream["selected_boundary_posture_validation"] = (
                posture_validation
            )
            return (
                "SELECTED_BOUNDARY_POSTURE_INVALID",
                "selected boundary posture is invalid: " + field,
                upstream,
            )
    for field, expected in summary_expectations.items():
        valid = summary.get(field) is expected
        posture_validation[field] = valid
        checks.append(
            _check(
                "upstream.summary." + field,
                valid,
                "SELECTED_BOUNDARY_POSTURE_INVALID",
            )
        )
        if not valid:
            upstream["selected_boundary_posture_validation"] = (
                posture_validation
            )
            return (
                "SELECTED_BOUNDARY_POSTURE_INVALID",
                "selected boundary summary posture is invalid: " + field,
                upstream,
            )
    upstream["selected_boundary_posture_validation"] = posture_validation

    if set(non_claims) != set(REQUIRED_UPSTREAM_FALSE_POSTURES):
        return (
            "UPSTREAM_FALSE_LOCK_NOT_FALSE",
            "selected boundary non-claims are not the exact false-lock set",
            upstream,
        )

    false_lock_validation = {
        field: boundary.get(field) is False
        for field in REQUIRED_UPSTREAM_FALSE_POSTURES
    }
    non_claim_validation = {
        field: non_claims.get(field) is False
        for field in REQUIRED_UPSTREAM_FALSE_POSTURES
    }
    upstream["upstream_false_lock_validation"] = false_lock_validation
    upstream["upstream_non_claim_validation"] = non_claim_validation
    for field in REQUIRED_UPSTREAM_FALSE_POSTURES:
        valid = (
            false_lock_validation[field]
            and non_claim_validation[field]
        )
        checks.append(
            _check(
                "upstream.false_lock." + field,
                valid,
                "UPSTREAM_FALSE_LOCK_NOT_FALSE",
            )
        )
        if not valid:
            return (
                "UPSTREAM_FALSE_LOCK_NOT_FALSE",
                "upstream false lock is missing or not exact false: " + field,
                upstream,
            )

    upstream["upstream_boundary_validated"] = True
    return None, None, upstream


def _empty_basis_state(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    supplied = isinstance(
        request.get("receiver_attestation_operation_basis"),
        Mapping,
    )
    return {
        "basis_supplied": supplied,
        "basis_admitted": False,
        "schema_validated": False,
        "path_validation": {},
        "hash_declaration_validated": False,
        "evaluator_reference_present": False,
        "trace_integrity_postures": {},
        "ambiguity_postures": {},
        "contradiction_postures": {},
        "unresolved_postures": {},
        "basis_non_claims_validated": False,
        "non_conversion_statement_validated": False,
        "complete_operation_basis_omitted": True,
    }


def _exact_boolean_map(value: Any, keys: Sequence[str]) -> bool:
    return (
        isinstance(value, Mapping)
        and set(value) == set(keys)
        and all(type(value.get(key)) is bool for key in keys)
    )


def _validate_operation_basis(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    state = _empty_basis_state(request)
    basis = request.get("receiver_attestation_operation_basis")
    if basis is None:
        checks.append(_check("operation_basis.absent_waiting", True))
        return None, None, state
    if not isinstance(basis, Mapping):
        return (
            "OPERATION_BASIS_NOT_MAPPING",
            "operation basis is not a mapping",
            state,
        )

    missing = set(BASIS_FIELDS).difference(basis)
    if missing:
        return (
            "OPERATION_BASIS_FIELD_MISSING",
            "operation basis fields are missing",
            state,
        )
    unknown = set(basis).difference(BASIS_FIELDS)
    if unknown:
        return (
            "OPERATION_BASIS_UNKNOWN_FIELD",
            "operation basis contains unknown fields",
            state,
        )
    state["schema_validated"] = True
    checks.append(_check("operation_basis.schema", True))

    path_expectations: dict[str, str] = {
        "selected_receiver_attestation_boundary_artifact_path": str(
            SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
        ),
        "bounded_capture_directory_path": str(
            BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
        ),
        **{
            field: str(path)
            for field, path in COMPONENT_RELATIVE_PATHS.items()
        },
    }
    for field, expected in path_expectations.items():
        valid = basis.get(field) == expected
        state["path_validation"][field] = valid
        checks.append(
            _check(
                "operation_basis.path." + field,
                valid,
                "OPERATION_BASIS_PATH_MISMATCH",
            )
        )
        if not valid:
            return (
                "OPERATION_BASIS_PATH_MISMATCH",
                "operation basis path does not match: " + field,
                state,
            )

    state["hash_declaration_validated"] = (
        basis.get("expected_archive_sha256") == EXPECTED_ARCHIVE_SHA256
    )
    checks.append(
        _check(
            "operation_basis.expected_archive_sha256",
            state["hash_declaration_validated"],
            "OPERATION_BASIS_HASH_MISMATCH",
        )
    )
    if not state["hash_declaration_validated"]:
        return (
            "OPERATION_BASIS_HASH_MISMATCH",
            "operation basis archive hash does not match",
            state,
        )

    evaluator_reference = basis.get("evaluator_reference")
    state["evaluator_reference_present"] = (
        isinstance(evaluator_reference, str)
        and bool(evaluator_reference.strip())
        and len(evaluator_reference) <= 1024
    )
    if not state["evaluator_reference_present"]:
        return (
            "OPERATION_BASIS_EVALUATOR_REFERENCE_INVALID",
            "evaluator reference must be one bounded non-empty string",
            state,
        )
    checks.append(_check("operation_basis.evaluator_reference", True))

    posture_families = (
        (
            "trace_integrity_postures",
            TRACE_INTEGRITY_POSTURE_KEYS,
        ),
        ("ambiguity_postures", AMBIGUITY_POSTURE_KEYS),
        ("contradiction_postures", CONTRADICTION_POSTURE_KEYS),
        ("unresolved_postures", UNRESOLVED_POSTURE_KEYS),
    )
    for family, keys in posture_families:
        value = basis.get(family)
        if not _exact_boolean_map(value, keys):
            return (
                "OPERATION_BASIS_POSTURE_MAP_INVALID",
                family + " is not the exact Boolean posture map",
                state,
            )
        state[family] = copy.deepcopy(dict(value))
        checks.append(_check("operation_basis." + family, True))

    if not all(
        state["trace_integrity_postures"][field] is True
        for field in TRACE_INTEGRITY_POSTURE_KEYS
    ):
        return (
            "OPERATION_BASIS_TRACE_INTEGRITY_NOT_TRUE",
            "required positive trace-integrity posture is not exact true",
            state,
        )
    checks.append(_check("operation_basis.trace_integrity_positive", True))

    if not _basis_non_claims_valid(basis.get("basis_non_claims")):
        return (
            "OPERATION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
            "basis non-claims are not the exact canonical false set",
            state,
        )
    state["basis_non_claims_validated"] = True
    checks.append(_check("operation_basis.basis_non_claims", True))

    if basis.get("non_conversion_statement") != NON_CONVERSION_STATEMENT:
        return (
            "OPERATION_BASIS_NON_CONVERSION_INVALID",
            "operation basis non-conversion statement does not match",
            state,
        )
    state["non_conversion_statement_validated"] = True
    checks.append(_check("operation_basis.non_conversion_statement", True))

    state["basis_admitted"] = True
    return None, None, state


def _empty_component_state() -> dict[str, Any]:
    return {
        "trace_paths_validated": False,
        "archive_validation": {
            "path": str(COMPONENT_RELATIVE_PATHS["preserved_archive_path"]),
            "regular_file": False,
            "byte_count": None,
            "computed_sha256": None,
            "expected_sha256": EXPECTED_ARCHIVE_SHA256,
            "correspondence_validated": False,
        },
        "archive_hash_record_validation": {
            "path": str(
                COMPONENT_RELATIVE_PATHS["archive_hash_record_path"]
            ),
            "regular_file": False,
            "readable": False,
            "parsed_sha256": None,
            "correspondence_validated": False,
        },
        "text_component_validation": {},
        "text_components_validated": False,
        "timestamp_validated": False,
        "recorded_signal_validation": {
            "path": str(COMPONENT_RELATIVE_PATHS["recorded_signal_path"]),
            "regular_file": False,
            "byte_count": None,
            "body_read": False,
        },
        "recorded_signal_artifact_existence_validated": False,
        "minimum_admission_checks_passed": False,
        "archive_bytes_omitted": True,
        "hash_record_body_omitted": True,
        "text_component_bodies_omitted": True,
        "recorded_signal_body_omitted": True,
    }


def _sha256_file(path: Path) -> tuple[str | None, int | None, str | None]:
    try:
        digest = hashlib.sha256()
        byte_count = 0
        with path.open("rb") as handle:
            while True:
                chunk = handle.read(65536)
                if not chunk:
                    break
                digest.update(chunk)
                byte_count += len(chunk)
        return digest.hexdigest(), byte_count, None
    except OSError:
        return None, None, "unreadable"


_TIMESTAMP_PATTERN = re.compile(
    r"^attested_at="
    r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)"
    r"\s*$"
)


def _timestamp_text_valid(text: str) -> bool:
    match = _TIMESTAMP_PATTERN.fullmatch(text)
    if match is None:
        return False
    try:
        parsed = datetime.fromisoformat(
            match.group(1).replace("Z", "+00:00")
        )
    except ValueError:
        return False
    return parsed.tzinfo == timezone.utc


def _validate_bounded_components(
    basis: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, str | None, dict[str, Any]]:
    state = _empty_component_state()
    state["trace_paths_validated"] = all(
        basis.get(field) == str(path)
        for field, path in COMPONENT_RELATIVE_PATHS.items()
    )

    archive_path = _as_repo_path(basis["preserved_archive_path"])
    archive_validation = state["archive_validation"]
    archive_validation["regular_file"] = archive_path.is_file()
    if not archive_validation["regular_file"]:
        return (
            "BOUNDED_COMPONENT_UNAVAILABLE",
            "preserved archive is unavailable",
            state,
        )
    computed_hash, archive_size, archive_error = _sha256_file(archive_path)
    if archive_error is not None or computed_hash is None:
        return (
            "BOUNDED_COMPONENT_UNAVAILABLE",
            "preserved archive is unreadable",
            state,
        )
    archive_validation["byte_count"] = archive_size
    archive_validation["computed_sha256"] = computed_hash

    hash_record_path = _as_repo_path(basis["archive_hash_record_path"])
    hash_validation = state["archive_hash_record_validation"]
    hash_validation["regular_file"] = hash_record_path.is_file()
    if not hash_validation["regular_file"]:
        return (
            "BOUNDED_COMPONENT_UNAVAILABLE",
            "archive hash record is unavailable",
            state,
        )
    try:
        hash_record_text = hash_record_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return (
            "BOUNDED_COMPONENT_UNAVAILABLE",
            "archive hash record is unreadable",
            state,
        )
    hash_validation["readable"] = True
    hash_match = re.fullmatch(
        r"([0-9a-f]{64})  receiver_attestation_001\.zip\s*",
        hash_record_text,
    )
    if hash_match is None:
        return (
            "ARCHIVE_HASH_RECORD_MALFORMED",
            "archive hash record is not in the bounded format",
            state,
        )
    parsed_hash = hash_match.group(1)
    hash_validation["parsed_sha256"] = parsed_hash
    hash_validation["correspondence_validated"] = (
        parsed_hash == EXPECTED_ARCHIVE_SHA256
    )
    archive_validation["correspondence_validated"] = (
        computed_hash == EXPECTED_ARCHIVE_SHA256
        and parsed_hash == EXPECTED_ARCHIVE_SHA256
    )
    if not archive_validation["correspondence_validated"]:
        return (
            "ARCHIVE_HASH_MISMATCH",
            "archive hash does not match claimed correspondence",
            state,
        )
    checks.append(_check("components.archive_correspondence", True))

    text_validations: dict[str, dict[str, Any]] = {}
    all_text_non_empty = True
    timestamp_valid = False
    for field in TEXT_COMPONENT_FIELDS:
        path = _as_repo_path(basis[field])
        metadata: dict[str, Any] = {
            "path": basis[field],
            "regular_file": path.is_file(),
            "readable": False,
            "byte_count": None,
            "non_empty": False,
        }
        text_validations[field] = metadata
        if not metadata["regular_file"]:
            state["text_component_validation"] = text_validations
            return (
                "BOUNDED_COMPONENT_UNAVAILABLE",
                "required text component is unavailable: " + field,
                state,
            )
        try:
            text = path.read_text(encoding="utf-8")
            byte_count = path.stat().st_size
        except (OSError, UnicodeError):
            state["text_component_validation"] = text_validations
            return (
                "BOUNDED_COMPONENT_UNAVAILABLE",
                "required text component is unreadable: " + field,
                state,
            )
        metadata["readable"] = True
        metadata["byte_count"] = byte_count
        metadata["non_empty"] = bool(text.strip())
        all_text_non_empty = all_text_non_empty and metadata["non_empty"]
        if field == "attestation_timestamp_path":
            timestamp_valid = _timestamp_text_valid(text)
            metadata["timestamp_parse_valid"] = timestamp_valid
        checks.append(_check("components.text_evaluated." + field, True))
    state["text_component_validation"] = text_validations
    state["text_components_validated"] = all_text_non_empty
    state["timestamp_validated"] = timestamp_valid

    signal_path = _as_repo_path(basis["recorded_signal_path"])
    signal_validation = state["recorded_signal_validation"]
    signal_validation["regular_file"] = signal_path.is_file()
    if not signal_validation["regular_file"]:
        return (
            "BOUNDED_COMPONENT_UNAVAILABLE",
            "recorded-signal artifact is unavailable",
            state,
        )
    try:
        signal_validation["byte_count"] = signal_path.stat().st_size
    except OSError:
        return (
            "BOUNDED_COMPONENT_UNAVAILABLE",
            "recorded-signal artifact cannot be stat-validated",
            state,
        )
    state["recorded_signal_artifact_existence_validated"] = True
    checks.append(_check("components.recorded_signal_exists", True))

    state["minimum_admission_checks_passed"] = (
        state["trace_paths_validated"]
        and archive_validation["correspondence_validated"]
        and state["text_components_validated"]
        and state["timestamp_validated"]
        and state["recorded_signal_artifact_existence_validated"]
    )
    return None, None, state


def _completed_result_from_states(
    basis_state: Mapping[str, Any],
    component_state: Mapping[str, Any],
) -> tuple[str, str]:
    ambiguity = basis_state.get("ambiguity_postures")
    unresolved = basis_state.get("unresolved_postures")
    contradiction = basis_state.get("contradiction_postures")
    any_ambiguity = (
        isinstance(ambiguity, Mapping)
        and any(value is True for value in ambiguity.values())
    )
    any_unresolved = (
        isinstance(unresolved, Mapping)
        and any(value is True for value in unresolved.values())
    )
    any_contradiction = (
        isinstance(contradiction, Mapping)
        and any(value is True for value in contradiction.values())
    )
    if any_ambiguity or any_unresolved:
        return OUTCOME_INDETERMINATE, OPERATION_RESULT_INDETERMINATE
    if any_contradiction or not component_state.get(
        "minimum_admission_checks_passed"
    ):
        return OUTCOME_NOT_RECORDED, OPERATION_RESULT_NOT_RECORDED
    return OUTCOME_RECORDED, OPERATION_RESULT_RECORDED


def _operation_object(
    outcome: str,
    operation_result: str | None,
    upstream: Mapping[str, Any],
    basis_state: Mapping[str, Any],
) -> dict[str, Any]:
    completed = outcome in {
        OUTCOME_RECORDED,
        OUTCOME_NOT_RECORDED,
        OUTCOME_INDETERMINATE,
    }
    recorded = operation_result == OPERATION_RESULT_RECORDED
    not_recorded = operation_result == OPERATION_RESULT_NOT_RECORDED
    indeterminate = operation_result == OPERATION_RESULT_INDETERMINATE
    return {
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
        "selected_candidate_sufficiency_operation_id": (
            SELECTED_SUFFICIENCY_OPERATION_ID
        ),
        "selected_candidate_sufficiency_operation_result_required": (
            SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
        ),
        "selected_receiver_attestation_boundary_id": SELECTED_BOUNDARY_ID,
        "selected_receiver_attestation_boundary_result_required": (
            SELECTED_BOUNDARY_RESULT_REQUIRED
        ),
        "selected_receiver_attestation_boundary_validated": (
            upstream.get("upstream_boundary_validated") is True
        ),
        "operation_basis_supplied": basis_state.get("basis_supplied") is True,
        "operation_basis_admitted": basis_state.get("basis_admitted") is True,
        "receiver_attestation_operation_result": operation_result,
        "receiver_attestation_operation_recorded": completed,
        "receiver_attestation_operation_result_recorded": completed,
        "receiver_attestation_operation_exhausted": completed,
        "receiver_attestation_decided": completed,
        "receiver_attestation_recorded": recorded,
        "receiver_attestation_not_recorded": not_recorded,
        "receiver_attestation_indeterminate": indeterminate,
        "originating_occurrence_created_by_source_body": False,
        **_canonical_non_claims(),
    }


def _declared_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("receiver_attestation_operation_basis")
    return {
        "intent": request.get("intent"),
        "operation_id": request.get("operation_id"),
        "operation_type": request.get("operation_type"),
        "operation_version": request.get("operation_version"),
        "operation_scope": request.get("operation_scope"),
        "receiver_side_answerable_basis_candidate_id": request.get(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "selected_candidate_sufficiency_operation_id": request.get(
            "selected_candidate_sufficiency_operation_id"
        ),
        "selected_candidate_sufficiency_operation_result_required": (
            request.get(
                "selected_candidate_sufficiency_operation_result_required"
            )
        ),
        "governing_operation_specification_path": request.get(
            "governing_receiver_attestation_operation_specification_path"
        ),
        "selected_boundary_artifact_path": request.get(
            "selected_receiver_attestation_boundary_artifact_path"
        ),
        "bounded_capture_directory_path": request.get(
            "bounded_capture_directory_path"
        ),
        "operation_basis_supplied": isinstance(basis, Mapping),
        "required_upstream_declarations_validated": (
            request.get("required_upstream_declarations")
            == _canonical_upstream_declarations()
        ),
        "declared_non_claims_validated": _non_claims_valid(
            request.get("declared_non_claims")
        ),
        "prohibited_request_flags_validated": all(
            request.get(field) is False for field in PROHIBITED_REQUEST_FLAGS
        ),
    }


def _operation_statement(
    outcome: str,
    operation_result: str | None,
) -> dict[str, bool]:
    completed = operation_result in COMPLETED_OPERATION_RESULT_FAMILY
    return {
        "one_exact_allowed_boundary_consumed_as_upstream_standing": (
            completed or outcome == OUTCOME_REQUIRES_BASIS
        ),
        "occurrence_not_created_by_source_body": True,
        "artifact_does_not_create_occurrence": True,
        "preserved_trace_not_independent_verification": True,
        "candidate_sufficient_not_receiver_attestation": True,
        "consideration_allowed_not_receiver_attestation": True,
        "operation_authorization_not_operation_result": True,
        "receiver_attestation_recorded_not_receiver_answerable_receipt": True,
        "receiver_attestation_recorded_not_presence": True,
        "receiver_attestation_recorded_not_identity_authority_truth_or_standing": (
            True
        ),
        "waiting_and_blocked_not_exhausted": not completed
        if outcome in {OUTCOME_REQUIRES_BASIS, OUTCOME_BLOCKED}
        else True,
        "open_does_not_mean_next": True,
    }


def _operation_non_meaning(
    operation_result: str | None,
) -> dict[str, bool]:
    return {
        "recorded_result_is_not_occurrence_creation": True,
        "recorded_result_is_not_receiver_answerable_receipt": True,
        "recorded_result_is_not_presence": True,
        "recorded_result_is_not_identity_authority_truth_or_standing": True,
        "not_recorded_is_not_occurrence_denial": True,
        "not_recorded_is_not_receiver_dishonesty": True,
        "not_recorded_is_not_candidate_insufficiency": True,
        "not_recorded_is_not_trace_erasure": True,
        "indeterminate_is_not_not_recorded": True,
        "hash_correspondence_is_not_identity_truth_presence_authority_or_standing": (
            True
        ),
        "completed_result_is_not_downstream_authorization": True,
        "operation_result_present": (
            operation_result in COMPLETED_OPERATION_RESULT_FAMILY
        ),
    }


def _what_remains_open(outcome: str) -> list[str]:
    if outcome == OUTCOME_REQUIRES_BASIS:
        return list(WAITING_WHAT_REMAINS_OPEN)
    if outcome == OUTCOME_BLOCKED:
        return list(BLOCKED_WHAT_REMAINS_OPEN)
    return list(COMPLETED_WHAT_REMAINS_OPEN)


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get(
        "receiver_side_answerable_basis_receiver_attestation_operation"
    )
    operation = operation if isinstance(operation, Mapping) else {}
    upstream = result.get("upstream_boundary_basis")
    upstream = upstream if isinstance(upstream, Mapping) else {}
    basis = result.get("supplied_operation_basis_admission_metadata")
    basis = basis if isinstance(basis, Mapping) else {}
    components = result.get("bounded_component_validation")
    components = components if isinstance(components, Mapping) else {}
    trace = result.get("trace_posture_metadata")
    trace = trace if isinstance(trace, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    ambiguity = trace.get("ambiguity_postures")
    contradiction = trace.get("contradiction_postures")
    unresolved = trace.get("unresolved_postures")
    return {
        "resolver_module": result.get("resolver_module"),
        "result_version": result.get("result_version"),
        "operation_id": operation.get("operation_id"),
        "operation_type": operation.get("operation_type"),
        "operation_version": operation.get("operation_version"),
        "operation_scope": operation.get("operation_scope"),
        "selected_candidate_id": operation.get(
            "receiver_side_answerable_basis_candidate_id"
        ),
        "selected_boundary_id": operation.get(
            "selected_receiver_attestation_boundary_id"
        ),
        "outcome": result.get("outcome"),
        "operation_result": operation.get(
            "receiver_attestation_operation_result"
        ),
        "failed_check_count": result.get("failed_check_count"),
        "passed_check_count": result.get("passed_check_count"),
        "blocked": block.get("blocked"),
        "basis_supplied": basis.get("basis_supplied"),
        "basis_admitted": basis.get("basis_admitted"),
        "upstream_boundary_validated": upstream.get(
            "upstream_boundary_validated"
        ),
        "trace_paths_validated": components.get("trace_paths_validated"),
        "archive_correspondence_validated": (
            isinstance(components.get("archive_validation"), Mapping)
            and components["archive_validation"].get(
                "correspondence_validated"
            )
            is True
        ),
        "text_components_validated": components.get(
            "text_components_validated"
        ),
        "timestamp_validated": components.get("timestamp_validated"),
        "recorded_signal_artifact_existence_validated": components.get(
            "recorded_signal_artifact_existence_validated"
        ),
        "any_ambiguity": (
            isinstance(ambiguity, Mapping)
            and any(value is True for value in ambiguity.values())
        ),
        "any_contradiction": (
            isinstance(contradiction, Mapping)
            and any(value is True for value in contradiction.values())
        ),
        "any_unresolved": (
            isinstance(unresolved, Mapping)
            and any(value is True for value in unresolved.values())
        ),
        "receiver_attestation_recorded": operation.get(
            "receiver_attestation_recorded"
        ),
        "receiver_attestation_not_recorded": operation.get(
            "receiver_attestation_not_recorded"
        ),
        "receiver_attestation_indeterminate": operation.get(
            "receiver_attestation_indeterminate"
        ),
        "receiver_attestation_operation_recorded": operation.get(
            "receiver_attestation_operation_recorded"
        ),
        "receiver_attestation_operation_exhausted": operation.get(
            "receiver_attestation_operation_exhausted"
        ),
        "result_level_non_claims_canonical_false": _non_claims_valid(
            result.get("non_claims")
        ),
        "complete_upstream_boundary_artifact_omitted": upstream.get(
            "complete_upstream_boundary_artifact_omitted"
        ),
        "complete_candidate_sufficiency_artifact_omitted": upstream.get(
            "complete_candidate_sufficiency_artifact_omitted"
        ),
        "complete_candidate_sufficiency_basis_omitted": upstream.get(
            "complete_candidate_sufficiency_basis_omitted"
        ),
        "complete_operation_basis_omitted": basis.get(
            "complete_operation_basis_omitted"
        ),
        "archive_bytes_omitted": components.get("archive_bytes_omitted"),
        "text_component_bodies_omitted": components.get(
            "text_component_bodies_omitted"
        ),
        "recorded_signal_body_omitted": components.get(
            "recorded_signal_body_omitted"
        ),
        "governing_paths": copy.deepcopy(
            upstream.get("governing_paths", {})
        ),
    }


def _result(
    request: Mapping[str, Any],
    outcome: str,
    operation_result: str | None,
    checks: list[dict[str, Any]],
    *,
    upstream: Mapping[str, Any] | None = None,
    basis_state: Mapping[str, Any] | None = None,
    component_state: Mapping[str, Any] | None = None,
    code: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    bounded_upstream = (
        copy.deepcopy(dict(upstream))
        if isinstance(upstream, Mapping)
        else _empty_upstream_basis(request)
    )
    bounded_basis = (
        copy.deepcopy(dict(basis_state))
        if isinstance(basis_state, Mapping)
        else _empty_basis_state(request)
    )
    bounded_components = (
        copy.deepcopy(dict(component_state))
        if isinstance(component_state, Mapping)
        else _empty_component_state()
    )
    operation = _operation_object(
        outcome,
        operation_result,
        bounded_upstream,
        bounded_basis,
    )
    result: dict[str, Any] = {
        "receiver_side_answerable_basis_receiver_attestation_operation_metadata": {
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "selected_boundary_artifact_path": request.get(
                "selected_receiver_attestation_boundary_artifact_path"
            ),
            "bounded_capture_directory_path": request.get(
                "bounded_capture_directory_path"
            ),
        },
        "declared_receiver_side_answerable_basis_receiver_attestation_operation_basis": (
            _declared_basis(request)
        ),
        "selected_operation_and_candidate_identity": {
            "operation_id": OPERATION_ID,
            "operation_type": OPERATION_TYPE,
            "operation_version": OPERATION_VERSION,
            "operation_scope": OPERATION_SCOPE,
            "selected_candidate_id": CANDIDATE_ID,
            "selected_candidate_type": CANDIDATE_TYPE,
            "selected_candidate_scope": CANDIDATE_SCOPE,
            "selected_sufficiency_operation_id": (
                SELECTED_SUFFICIENCY_OPERATION_ID
            ),
            "selected_sufficiency_operation_result_required": (
                SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
            ),
            "selected_boundary_id": SELECTED_BOUNDARY_ID,
            "selected_boundary_result_required": (
                SELECTED_BOUNDARY_RESULT_REQUIRED
            ),
        },
        "upstream_boundary_basis": bounded_upstream,
        "supplied_operation_basis_admission_metadata": bounded_basis,
        "bounded_component_validation": bounded_components,
        "trace_posture_metadata": {
            "trace_integrity_postures": copy.deepcopy(
                bounded_basis.get("trace_integrity_postures", {})
            ),
            "ambiguity_postures": copy.deepcopy(
                bounded_basis.get("ambiguity_postures", {})
            ),
            "contradiction_postures": copy.deepcopy(
                bounded_basis.get("contradiction_postures", {})
            ),
            "unresolved_postures": copy.deepcopy(
                bounded_basis.get("unresolved_postures", {})
            ),
        },
        "receiver_side_answerable_basis_receiver_attestation_operation": (
            operation
        ),
        "operation_result_detail": {
            "operation_result": operation_result,
            "completed_result_posture_count": sum(
                operation[field] is True
                for field in (
                    "receiver_attestation_recorded",
                    "receiver_attestation_not_recorded",
                    "receiver_attestation_indeterminate",
                )
            ),
            "result_precedence": [
                OPERATION_RESULT_INDETERMINATE,
                OPERATION_RESULT_NOT_RECORDED,
                OPERATION_RESULT_RECORDED,
            ],
        },
        "operation_posture": {
            "operation_recorded": operation[
                "receiver_attestation_operation_recorded"
            ],
            "operation_result_recorded": operation[
                "receiver_attestation_operation_result_recorded"
            ],
            "operation_exhausted": operation[
                "receiver_attestation_operation_exhausted"
            ],
            "receiver_attestation_decided": operation[
                "receiver_attestation_decided"
            ],
            "single_use_only": True,
            "originating_occurrence_created_by_source_body": False,
        },
        "receiver_side_answerable_basis_receiver_attestation_operation_checks": (
            copy.deepcopy(checks)
        ),
        "receiver_side_answerable_basis_receiver_attestation_operation_statement": (
            _operation_statement(outcome, operation_result)
        ),
        "receiver_side_answerable_basis_receiver_attestation_operation_non_meaning": (
            _operation_non_meaning(operation_result)
        ),
        "permitted_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "blocked_routes": list(BLOCKED_ROUTES),
        "what_remains_open": _what_remains_open(outcome),
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
        "failed_check_count": sum(
            check.get("passed") is False for check in checks
        ),
        "passed_check_count": sum(
            check.get("passed") is True for check in checks
        ),
    }
    result[
        "receiver_side_answerable_basis_"
        "receiver_attestation_operation_summary"
    ] = _summary_from_result(result)
    return result


def resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min(
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one exact bounded receiver-attestation operation."""
    checks: list[dict[str, Any]] = []
    if request is None:
        declared_request = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request()
        )
    elif not isinstance(request, Mapping):
        declared_request = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request()
        )
        _add_failure(checks, "request.mapping", "REQUEST_NOT_MAPPING")
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            None,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason="declared operation request is not a mapping",
        )
    else:
        declared_request = copy.deepcopy(dict(request))

    code, reason = _validate_request(declared_request, checks)
    if code is not None:
        _add_failure(checks, "request.validation", code)
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            None,
            checks,
            code=code,
            reason=reason,
        )

    code, reason, upstream = _validate_upstream_boundary(
        declared_request,
        checks,
    )
    if code is not None:
        _add_failure(checks, "upstream.validation", code)
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            None,
            checks,
            upstream=upstream,
            code=code,
            reason=reason,
        )

    code, reason, basis_state = _validate_operation_basis(
        declared_request,
        checks,
    )
    if code is not None:
        _add_failure(checks, "operation_basis.validation", code)
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            None,
            checks,
            upstream=upstream,
            basis_state=basis_state,
            code=code,
            reason=reason,
        )

    if not basis_state["basis_supplied"]:
        return _result(
            declared_request,
            OUTCOME_REQUIRES_BASIS,
            None,
            checks,
            upstream=upstream,
            basis_state=basis_state,
        )

    basis = declared_request["receiver_attestation_operation_basis"]
    code, reason, component_state = _validate_bounded_components(
        basis,
        checks,
    )
    if code is not None:
        _add_failure(checks, "bounded_components.validation", code)
        return _result(
            declared_request,
            OUTCOME_BLOCKED,
            None,
            checks,
            upstream=upstream,
            basis_state=basis_state,
            component_state=component_state,
            code=code,
            reason=reason,
        )

    outcome, operation_result = _completed_result_from_states(
        basis_state,
        component_state,
    )
    return _result(
        declared_request,
        outcome,
        operation_result,
        checks,
        upstream=upstream,
        basis_state=basis_state,
        component_state=component_state,
    )


def resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_from_path(
    request_path: Path | str,
) -> dict[str, Any]:
    """Read one exact request path without discovery and resolve it."""
    payload, error = _read_json(request_path)
    if error is not None or not isinstance(payload, Mapping):
        request = (
            build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request()
        )
        checks = [_check("request.path", False, "REQUEST_NOT_MAPPING")]
        return _result(
            request,
            OUTCOME_BLOCKED,
            None,
            checks,
            code="REQUEST_NOT_MAPPING",
            reason=(
                "request path is unavailable, duplicated, unparseable, "
                "or not a mapping"
            ),
        )
    return (
        resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min(
            payload
        )
    )


def build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return one compact deterministic material-omitting summary."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    return _summary_from_result(result)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10_000):
        candidate = path.with_name(
            path.stem + "_" + f"{index:03d}" + path.suffix
        )
        if not candidate.exists():
            return candidate
    raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
        "WRITE_REFUSED: deterministic output suffix space exhausted"
    )


def _contains_complete_material(value: Any) -> bool:
    forbidden_keys = {
        "receiver_attestation_operation_basis",
        "complete_receiver_attestation_operation_basis",
        "selected_receiver_attestation_boundary_artifact",
        "complete_upstream_boundary_artifact",
        "candidate_sufficiency_artifact",
        "candidate_sufficiency_basis",
        "sufficiency_basis_records",
        "archive_bytes",
        "archive_body",
        "complete_archive",
        "hash_record_body",
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
            key in forbidden_keys or _contains_complete_material(nested)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(
        value,
        (str, bytes, bytearray),
    ):
        return any(_contains_complete_material(item) for item in value)
    return isinstance(value, (bytes, bytearray))


def _branch_valid(result: Mapping[str, Any]) -> bool:
    outcome = result.get("outcome")
    operation = result.get(
        "receiver_side_answerable_basis_receiver_attestation_operation"
    )
    block = result.get("block")
    basis = result.get("supplied_operation_basis_admission_metadata")
    upstream = result.get("upstream_boundary_basis")
    if (
        outcome not in OUTCOME_FAMILY
        or not isinstance(operation, Mapping)
        or not isinstance(block, Mapping)
        or not isinstance(basis, Mapping)
        or not isinstance(upstream, Mapping)
    ):
        return False
    if (
        operation.get("operation_id") != OPERATION_ID
        or operation.get("operation_type") != OPERATION_TYPE
        or operation.get("operation_version") != OPERATION_VERSION
        or operation.get("operation_scope") != OPERATION_SCOPE
        or any(
            operation.get(field) is not False
            for field in REQUIRED_FALSE_NON_CLAIMS
        )
    ):
        return False

    operation_result = operation.get(
        "receiver_attestation_operation_result"
    )
    recorded = operation.get("receiver_attestation_recorded")
    not_recorded = operation.get("receiver_attestation_not_recorded")
    indeterminate = operation.get("receiver_attestation_indeterminate")
    completed_count = sum(
        value is True for value in (recorded, not_recorded, indeterminate)
    )
    completed = outcome in {
        OUTCOME_RECORDED,
        OUTCOME_NOT_RECORDED,
        OUTCOME_INDETERMINATE,
    }
    common_completed = (
        operation.get("receiver_attestation_operation_recorded") is completed
        and operation.get(
            "receiver_attestation_operation_result_recorded"
        )
        is completed
        and operation.get("receiver_attestation_operation_exhausted")
        is completed
        and operation.get("receiver_attestation_decided") is completed
    )
    if not common_completed:
        return False
    clean_block = (
        block.get("blocked") is False
        and block.get("code") is None
        and block.get("block_code") is None
        and block.get("reason") is None
    )
    completed_basis = (
        basis.get("basis_supplied") is True
        and basis.get("basis_admitted") is True
        and upstream.get("upstream_boundary_validated") is True
    )
    if outcome == OUTCOME_RECORDED:
        return (
            clean_block
            and completed_basis
            and operation_result == OPERATION_RESULT_RECORDED
            and recorded is True
            and not_recorded is False
            and indeterminate is False
            and completed_count == 1
        )
    if outcome == OUTCOME_NOT_RECORDED:
        return (
            clean_block
            and completed_basis
            and operation_result == OPERATION_RESULT_NOT_RECORDED
            and recorded is False
            and not_recorded is True
            and indeterminate is False
            and completed_count == 1
        )
    if outcome == OUTCOME_INDETERMINATE:
        return (
            clean_block
            and completed_basis
            and operation_result == OPERATION_RESULT_INDETERMINATE
            and recorded is False
            and not_recorded is False
            and indeterminate is True
            and completed_count == 1
        )
    if outcome == OUTCOME_REQUIRES_BASIS:
        return (
            operation_result is None
            and completed_count == 0
            and clean_block
            and basis.get("basis_supplied") is False
            and basis.get("basis_admitted") is False
            and upstream.get("upstream_boundary_validated") is True
        )
    return (
        operation_result is None
        and completed_count == 0
        and block.get("blocked") is True
        and block.get("code") in BLOCK_CODES
        and block.get("block_code") == block.get("code")
        and isinstance(block.get("reason"), str)
        and bool(block.get("reason"))
    )


def _path_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _output_path_is_forbidden(path: Path) -> bool:
    resolved = path.resolve()
    protected_roots = (
        (REPO_ROOT / "reference").resolve(),
        (REPO_ROOT / "spec").resolve(),
        (REPO_ROOT / "src").resolve(),
        (REPO_ROOT / "tests").resolve(),
        (
            REPO_ROOT / SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
        ).parent.resolve(),
        (
            REPO_ROOT / SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
        ).parent.resolve(),
        (REPO_ROOT / BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH).resolve(),
    )
    return any(_path_within(resolved, root) for root in protected_roots)


def write_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one valid deterministic result without silent overwrite."""
    if not isinstance(result, Mapping):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: result must be a mapping"
        )
    if set(result) != RESULT_SECTIONS:
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: result sections are incomplete or unexpected"
        )
    if (
        result.get("resolver_module") != RESOLVER_MODULE
        or result.get("result_version") != RESULT_VERSION
    ):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: incompatible result metadata"
        )
    if not _non_claims_valid(result.get("non_claims")):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: result non-claims are not canonical false"
        )
    checks = result.get(
        "receiver_side_answerable_basis_receiver_attestation_operation_checks"
    )
    if not isinstance(checks, list) or not all(
        isinstance(check, Mapping)
        and type(check.get("passed")) is bool
        for check in checks
    ):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: checks are malformed"
        )
    for check in checks:
        for field in ("failure_code", "block_code"):
            if field in check and check.get(field) not in BLOCK_CODES:
                raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
                    "WRITE_REFUSED: check contains a non-public failure code"
                )
    failed_count = result.get("failed_check_count")
    passed_count = result.get("passed_check_count")
    if (
        type(failed_count) is not int
        or type(passed_count) is not int
        or failed_count < 0
        or passed_count < 0
        or failed_count
        != sum(check.get("passed") is False for check in checks)
        or passed_count
        != sum(check.get("passed") is True for check in checks)
    ):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: check counts are malformed or inconsistent"
        )
    if not _branch_valid(result):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: result branch posture is inconsistent"
        )
    if result.get("outcome") != OUTCOME_BLOCKED and failed_count != 0:
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: non-blocked outcome contains failed checks"
        )
    if result.get("outcome") == OUTCOME_BLOCKED and failed_count <= 0:
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: blocked outcome lacks failed checks"
        )
    operation = result.get(
        "receiver_side_answerable_basis_receiver_attestation_operation"
    )
    detail = result.get("operation_result_detail")
    if (
        not isinstance(operation, Mapping)
        or not isinstance(detail, Mapping)
        or detail.get("operation_result")
        != operation.get("receiver_attestation_operation_result")
    ):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: operation result detail is inconsistent"
        )
    summary = result.get(
        "receiver_side_answerable_basis_"
        "receiver_attestation_operation_summary"
    )
    if (
        not isinstance(summary, Mapping)
        or dict(summary) != _summary_from_result(result)
    ):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: operation summary does not match result"
        )
    if _contains_complete_material(result):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: complete upstream, basis, archive, text, or signal material present"
        )

    target = (
        _as_repo_path(output_path)
        if output_path is not None
        else OUTPUT_ROOT / OUTPUT_FILENAME
    )
    if _output_path_is_forbidden(target):
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: output path is protected or belongs to upstream lineage"
        )
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
        raise ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError(
            "WRITE_REFUSED: unable to write result"
        ) from exc
    return target
