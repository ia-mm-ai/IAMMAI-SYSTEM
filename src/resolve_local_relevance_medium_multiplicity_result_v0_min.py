"""Resolve one local relevance medium multiplicity result.

This resolver reads one clean first LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY
artifact and one clean second
LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY artifact.
It records one small LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT object stating
that exactly two locally discoverable orientation objects now stand in lineage.

It does not compare or relate the two orientation objects. It does not create a
relation view, comparison view, index system, registry, search, ranking,
repeated reception permission, arbitrary reception, feed, source transfer,
source receipt, source, authority, currentness, truth, action, synchronization,
participation authorization, participant role, runtime permission, public API,
participant-facing interface, distributed behavior, operation permission, or
follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class LocalRelevanceMediumMultiplicityResultV0MinError(Exception):
    """Bounded error for malformed local relevance medium multiplicity requests."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_multiplicity_result_v0_min"

MULTIPLICITY_RESULT_TYPE = "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT"
MULTIPLICITY_RESULT_SCOPE = "TWO_LOCAL_ORIENTATION_LOCATORS_ONLY"
FIRST_LOCATOR_RECORDED_OUTCOME = "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED"
SECOND_LOCATOR_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED"
)

DEFAULT_MULTIPLICITY_RESULT_ID = "local_relevance_medium_multiplicity_result_001"
DEFAULT_FIRST_LOCATOR_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min/"
    "local_relevance_orientation_index_entry_reference_review_001__"
    "local_relevance_orientation_index_entry_v0_min_result.json"
)
DEFAULT_SECOND_LOCATOR_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min/"
    "local_relevance_medium_second_local_relevance_orientation_index_entry_reference_review_001__"
    "local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_result.json"
)

DEFAULT_FIRST_RECEIVED_SIGNAL_ID = "bounded_relevance_signal_001"
DEFAULT_SECOND_RECEIVED_SIGNAL_ID = "bounded_relevance_signal_002"
DEFAULT_FIRST_RELEVANCE_BASIS_ID = "bounded_relevance_basis_001"
DEFAULT_SECOND_RELEVANCE_BASIS_ID = "bounded_relevance_basis_002"
DEFAULT_FIRST_RELEVANCE_SCOPE_ID = "bounded_relevance_scope_001"
DEFAULT_SECOND_RELEVANCE_SCOPE_ID = "bounded_relevance_scope_002"
DEFAULT_FIRST_CARRIER_CONTEXT_ID = "bounded_relevance_signal_carrier_context_001"
DEFAULT_SECOND_CARRIER_CONTEXT_ID = "bounded_relevance_signal_carrier_context_002"
DEFAULT_FIRST_RECEPTION_ENVELOPE_ID = "bounded_relevance_reception_envelope_001"
DEFAULT_SECOND_RECEPTION_ENVELOPE_ID = "bounded_relevance_reception_envelope_002"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_multiplicity_result_v0_min"
)

SUPPORTED_MULTIPLICITY_RESULT_SCOPE_VALUES = (MULTIPLICITY_RESULT_SCOPE,)
SUPPORTED_MULTIPLICITY_RESULT_TYPE_VALUES = (MULTIPLICITY_RESULT_TYPE,)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REQUIRED_FALSE_NON_CLAIMS = (
    "relation_view_created",
    "comparison_view_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "source_created",
    "authority_created",
    "currentness_created",
    "truth_created",
    "action_created",
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "broader_reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "follow_on_work_authorized",
    "artifact_existence_treated_as_multiplicity_result_authority",
    "latest_file_posture_treated_as_multiplicity_result_authority",
    "repo_local_availability_treated_as_multiplicity_result_authority",
    "hidden_repo_state_used_as_multiplicity_result_content",
    "hidden_repo_state_used_as_multiplicity_result_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_multiplicity_result_recorded",
    "basis_first_local_relevance_orientation_index_entry_artifact_preserved",
    "basis_second_local_relevance_orientation_index_entry_artifact_preserved",
    "first_orientation_view_artifact_preserved",
    "second_orientation_view_artifact_preserved",
    "first_receipt_artifact_preserved",
    "second_receipt_artifact_preserved",
    "first_reception_artifact_preserved",
    "second_reception_artifact_preserved",
    "successor_candidate_admission_artifact_preserved",
    "successor_reception_request_artifact_preserved",
    "first_received_signal_id_preserved",
    "second_received_signal_id_preserved",
    "first_and_second_signals_distinct",
    "first_relevance_basis_id_preserved",
    "second_relevance_basis_id_preserved",
    "first_relevance_scope_id_preserved",
    "second_relevance_scope_id_preserved",
    "first_carrier_context_id_preserved",
    "second_carrier_context_id_preserved",
    "first_reception_envelope_id_preserved",
    "second_reception_envelope_id_preserved",
    "multiplicity_count_is_two",
    "two_local_orientation_locators_present",
    "basis_lineage_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_BLOCK_REQUESTED",
    "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
    "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
    "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_UNREADABLE",
    "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_UNREADABLE",
    "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_JSON_OBJECT",
    "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_JSON_OBJECT",
    "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_RECORDED",
    "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_RECORDED",
    "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_VERSION_NOT_0_1_0",
    "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_VERSION_NOT_0_1_0",
    "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_OBJECT_MISSING",
    "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_OBJECT_MISSING",
    "FIRST_LOCATOR_ARTIFACT_MISSING",
    "SECOND_LOCATOR_ARTIFACT_MISSING",
    "FIRST_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "FIRST_RECEIPT_ARTIFACT_MISSING",
    "SECOND_RECEIPT_ARTIFACT_MISSING",
    "FIRST_RECEPTION_ARTIFACT_MISSING",
    "SECOND_RECEPTION_ARTIFACT_MISSING",
    "FIRST_RECEIVED_SIGNAL_ID_MISSING",
    "SECOND_RECEIVED_SIGNAL_ID_MISSING",
    "FIRST_AND_SECOND_RECEIVED_SIGNAL_IDS_NOT_DISTINCT",
    "FIRST_RELEVANCE_BASIS_ID_MISSING",
    "SECOND_RELEVANCE_BASIS_ID_MISSING",
    "FIRST_RELEVANCE_SCOPE_ID_MISSING",
    "SECOND_RELEVANCE_SCOPE_ID_MISSING",
    "FIRST_CARRIER_CONTEXT_ID_MISSING",
    "SECOND_CARRIER_CONTEXT_ID_MISSING",
    "FIRST_RECEPTION_ENVELOPE_ID_MISSING",
    "SECOND_RECEPTION_ENVELOPE_ID_MISSING",
    "MULTIPLICITY_RESULT_SCOPE_MISSING",
    "MULTIPLICITY_RESULT_SCOPE_NOT_TWO_LOCAL_LOCATORS_ONLY",
    "MULTIPLICITY_RESULT_TYPE_MISSING",
    "MULTIPLICITY_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT",
    "MULTIPLICITY_COUNT_NOT_TWO",
    "TWO_LOCAL_ORIENTATION_LOCATORS_NOT_PRESENT",
    "BASIS_LINEAGE_NOT_PRESERVED",
    "MULTIPLICITY_RESULT_NOT_RECORDED",
    "RELATION_VIEW_CREATED",
    "COMPARISON_VIEW_CREATED",
    "INDEX_SYSTEM_CREATED",
    "REGISTRY_CREATED",
    "SEARCH_SURFACE_CREATED",
    "RANKING_SURFACE_CREATED",
    "REPEATED_RECEPTION_PERMISSION_CREATED",
    "ARBITRARY_RECEPTION_CREATED",
    "FEED_CREATED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "TRUTH_CREATED",
    "ACTION_CREATED",
    "SYNCHRONIZATION_CREATED",
    "PARTICIPATION_AUTHORIZED",
    "PARTICIPANT_ROLE_CREATED",
    "RUNTIME_PERMISSION_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_MULTIPLICITY_RESULT_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_MULTIPLICITY_RESULT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_MULTIPLICITY_RESULT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_MULTIPLICITY_RESULT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_MULTIPLICITY_RESULT_AUTHORITY",
    "PRIOR_ARTIFACTS_MUTATED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_REQUEST_UNREADABLE",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_multiplicity_result_body",
    "raw_first_local_index_entry_body",
    "raw_second_local_index_entry_body",
    "raw_first_orientation_body",
    "raw_second_orientation_body",
    "raw_first_receipt_body",
    "raw_second_receipt_body",
    "raw_first_reception_body",
    "raw_second_reception_body",
    "raw_successor_candidate_admission_body",
    "raw_successor_reception_request_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "multiplicity_result_body",
    "first_local_index_entry_body",
    "second_local_index_entry_body",
    "first_orientation_body",
    "second_orientation_body",
    "first_receipt_body",
    "second_receipt_body",
    "first_reception_body",
    "second_reception_body",
    "successor_candidate_admission_body",
    "successor_reception_request_body",
    "source_body",
    "authority_body",
    "currentness_body",
    "action_body",
    "synchronization_body",
    "public_api_body",
    "participant_facing_interface_body",
    "distributed_network_behavior_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_MULTIPLICITY_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_LOCAL_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_LOCAL_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_CANDIDATE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RECEPTION_REQUEST_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

OFFICIAL_STRINGS = frozenset(
    (
        MULTIPLICITY_RESULT_TYPE,
        MULTIPLICITY_RESULT_SCOPE,
        FIRST_LOCATOR_RECORDED_OUTCOME,
        SECOND_LOCATOR_RECORDED_OUTCOME,
        INTENT_RECORD,
        INTENT_DO_NOT_RECORD,
        INTENT_BLOCK,
        RESULT_VERSION,
        RESOLVER_MODULE,
        DEFAULT_FIRST_RECEIVED_SIGNAL_ID,
        DEFAULT_SECOND_RECEIVED_SIGNAL_ID,
        DEFAULT_FIRST_RELEVANCE_BASIS_ID,
        DEFAULT_SECOND_RELEVANCE_BASIS_ID,
        DEFAULT_FIRST_RELEVANCE_SCOPE_ID,
        DEFAULT_SECOND_RELEVANCE_SCOPE_ID,
        DEFAULT_FIRST_CARRIER_CONTEXT_ID,
        DEFAULT_SECOND_CARRIER_CONTEXT_ID,
        DEFAULT_FIRST_RECEPTION_ENVELOPE_ID,
        DEFAULT_SECOND_RECEPTION_ENVELOPE_ID,
    )
    + OUTCOME_FAMILY
    + BLOCK_CODES
    + REQUIRED_FALSE_NON_CLAIMS
    + ALLOWED_TRUE_RECORDED_FIELDS
)

FALSE_REQUEST_BLOCKS = (
    ("relation_view_created", "RELATION_VIEW_CREATED"),
    ("comparison_view_created", "COMPARISON_VIEW_CREATED"),
    ("index_system_created", "INDEX_SYSTEM_CREATED"),
    ("registry_created", "REGISTRY_CREATED"),
    ("search_surface_created", "SEARCH_SURFACE_CREATED"),
    ("ranking_surface_created", "RANKING_SURFACE_CREATED"),
    ("repeated_reception_permission_created", "REPEATED_RECEPTION_PERMISSION_CREATED"),
    ("arbitrary_reception_created", "ARBITRARY_RECEPTION_CREATED"),
    ("feed_created", "FEED_CREATED"),
    ("source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
    ("source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
    ("source_created", "SOURCE_CREATED"),
    ("authority_created", "AUTHORITY_CREATED"),
    ("currentness_created", "CURRENTNESS_CREATED"),
    ("truth_created", "TRUTH_CREATED"),
    ("action_created", "ACTION_CREATED"),
    ("synchronization_created", "SYNCHRONIZATION_CREATED"),
    ("participation_authorized", "PARTICIPATION_AUTHORIZED"),
    ("participant_role_created", "PARTICIPANT_ROLE_CREATED"),
    ("runtime_permission_created", "RUNTIME_PERMISSION_CREATED"),
    ("public_api_created", "PUBLIC_API_CREATED"),
    ("participant_facing_interface_created", "PARTICIPANT_FACING_INTERFACE_CREATED"),
    ("distributed_network_behavior_created", "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
    ("deployment_created", "DEPLOYMENT_CREATED"),
    ("public_release_created", "PUBLIC_RELEASE_CREATED"),
    ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
    ("broader_reusable_permission_created", "BROADER_REUSABLE_PERMISSION_CREATED"),
    ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
    ("adoption_created", "ADOPTION_CREATED"),
    ("receiving_context_governance_created", "RECEIVING_CONTEXT_GOVERNANCE_CREATED"),
    ("publication_flow_created", "PUBLICATION_FLOW_CREATED"),
    ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    (
        "artifact_existence_treated_as_multiplicity_result_authority",
        "ARTIFACT_EXISTENCE_TREATED_AS_MULTIPLICITY_RESULT_AUTHORITY",
    ),
    (
        "latest_file_posture_treated_as_multiplicity_result_authority",
        "LATEST_FILE_POSTURE_TREATED_AS_MULTIPLICITY_RESULT_AUTHORITY",
    ),
    (
        "repo_local_availability_treated_as_multiplicity_result_authority",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_MULTIPLICITY_RESULT_AUTHORITY",
    ),
    (
        "hidden_repo_state_used_as_multiplicity_result_content",
        "HIDDEN_REPO_STATE_USED_AS_MULTIPLICITY_RESULT_CONTENT",
    ),
    (
        "hidden_repo_state_used_as_multiplicity_result_authority",
        "HIDDEN_REPO_STATE_USED_AS_MULTIPLICITY_RESULT_AUTHORITY",
    ),
    ("prior_artifacts_mutated", "PRIOR_ARTIFACTS_MUTATED"),
    ("predecessor_failure_repaired", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
    ("predecessor_failure_hidden", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
    (
        "predecessor_failure_claimed_passed",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    ),
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    return {}


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _is_sensitive_key(key: str) -> bool:
    return key in SENSITIVE_CONTENT_KEYS or key.endswith("_body")


def _sanitize(value: Any, parent_key: str | None = None) -> Any:
    if parent_key is not None and _is_sensitive_key(parent_key):
        return "[REDACTED_RAW_BODY_CONTENT]"
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        sanitized = value
        for sentinel in HOSTILE_SENTINELS:
            sanitized = sanitized.replace(sentinel, "[REDACTED_HOSTILE_SENTINEL]")
        return sanitized
    if isinstance(value, Mapping):
        return {str(key): _sanitize(item, str(key)) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, parent_key) for item in value]
    return value


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> dict[str, Any]:
    failure_code = None if passed else code
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
        "block_code": failure_code,
        "failure_code": failure_code,
    }


def _checks_counts(checks: list[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _read_json_object(
    path_value: Any,
    missing_code: str,
    unreadable_code: str,
    not_json_object_code: str,
) -> tuple[dict[str, Any] | None, str | None]:
    if not path_value:
        return None, missing_code
    try:
        path = Path(str(path_value))
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        return None, unreadable_code
    if not isinstance(loaded, Mapping):
        return None, not_json_object_code
    return dict(loaded), None


def _failed_check_count_from_artifact(
    artifact: Mapping[str, Any],
    metadata_key: str,
    summary_key: str,
    checks_key: str,
) -> Any:
    metadata = _as_mapping(artifact.get(metadata_key))
    summary = _as_mapping(artifact.get(summary_key))
    explicit = _first_present(
        metadata.get("failed_check_count"),
        summary.get("failed_check_count"),
        artifact.get("failed_check_count"),
    )
    if explicit is not None:
        return explicit
    checks = artifact.get(checks_key)
    if isinstance(checks, list):
        return sum(1 for check in checks if _as_mapping(check).get("passed") is not True)
    return None


def _extract_first_locator_facts(
    artifact: Mapping[str, Any] | None,
    artifact_path: str | None,
) -> dict[str, Any]:
    if artifact is None:
        return {
            "basis_first_local_relevance_orientation_index_entry_artifact": artifact_path
        }

    metadata = _as_mapping(artifact.get("local_relevance_orientation_index_entry_metadata"))
    summary = _as_mapping(artifact.get("local_relevance_orientation_index_entry_summary"))
    entry = _as_mapping(artifact.get("index_entry"))

    return {
        "basis_first_local_relevance_orientation_index_entry_artifact": artifact_path,
        "basis_first_local_relevance_orientation_index_entry_outcome": _first_present(
            artifact.get("outcome"),
            summary.get("outcome"),
        ),
        "basis_first_local_relevance_orientation_index_entry_result_version": _first_present(
            metadata.get("local_relevance_orientation_index_entry_version"),
            metadata.get("result_version"),
            summary.get("result_version"),
            entry.get("index_entry_version"),
            artifact.get("result_version"),
        ),
        "basis_first_local_relevance_orientation_index_entry_failed_check_count": (
            _failed_check_count_from_artifact(
                artifact,
                "local_relevance_orientation_index_entry_metadata",
                "local_relevance_orientation_index_entry_summary",
                "local_relevance_orientation_index_entry_checks",
            )
        ),
        "first_local_relevance_orientation_index_entry": entry,
        "first_index_entry_type": entry.get("index_entry_type"),
        "first_index_entry_scope": entry.get("index_entry_scope"),
        "first_orientation_view_artifact": entry.get("orientation_view_artifact"),
        "first_receipt_artifact": entry.get("source_receipt_artifact"),
        "first_reception_artifact": entry.get("referenced_reception_artifact"),
        "first_received_signal_id": entry.get("received_signal_id"),
        "first_relevance_basis_id": entry.get("received_relevance_basis_id"),
        "first_relevance_scope_id": entry.get("received_relevance_scope_id"),
        "first_carrier_context_id": entry.get("received_carrier_context_id"),
        "first_reception_envelope_id": entry.get("received_reception_envelope_id"),
    }


def _extract_second_locator_facts(
    artifact: Mapping[str, Any] | None,
    artifact_path: str | None,
) -> dict[str, Any]:
    if artifact is None:
        return {
            "basis_second_local_relevance_orientation_index_entry_artifact": artifact_path
        }

    metadata = _as_mapping(
        artifact.get(
            "local_relevance_medium_second_local_relevance_orientation_index_entry_metadata"
        )
    )
    summary = _as_mapping(
        artifact.get(
            "local_relevance_medium_second_local_relevance_orientation_index_entry_summary"
        )
    )
    entry = _as_mapping(artifact.get("second_local_relevance_orientation_index_entry"))

    return {
        "basis_second_local_relevance_orientation_index_entry_artifact": artifact_path,
        "basis_second_local_relevance_orientation_index_entry_outcome": _first_present(
            artifact.get("outcome"),
            summary.get("outcome"),
        ),
        "basis_second_local_relevance_orientation_index_entry_result_version": _first_present(
            metadata.get(
                "local_relevance_medium_second_local_relevance_orientation_index_entry_version"
            ),
            metadata.get("result_version"),
            summary.get("result_version"),
            entry.get("second_index_entry_version"),
            artifact.get("result_version"),
        ),
        "basis_second_local_relevance_orientation_index_entry_failed_check_count": (
            _failed_check_count_from_artifact(
                artifact,
                "local_relevance_medium_second_local_relevance_orientation_index_entry_metadata",
                "local_relevance_medium_second_local_relevance_orientation_index_entry_summary",
                "local_relevance_medium_second_local_relevance_orientation_index_entry_checks",
            )
        ),
        "second_local_relevance_orientation_index_entry": entry,
        "second_index_entry_type": entry.get("second_index_entry_type"),
        "second_index_entry_scope": entry.get("second_index_entry_scope"),
        "second_orientation_view_artifact": entry.get(
            "basis_second_relevance_orientation_view_artifact"
        ),
        "second_receipt_artifact": entry.get("basis_second_bounded_relevance_receipt_artifact"),
        "second_reception_artifact": entry.get(
            "basis_second_bounded_relevance_reception_artifact"
        ),
        "successor_candidate_admission_artifact": entry.get(
            "basis_successor_candidate_admission_artifact"
        ),
        "successor_reception_request_artifact": entry.get(
            "basis_successor_reception_request_artifact"
        ),
        "second_received_signal_id": entry.get("second_received_signal_id"),
        "second_relevance_basis_id": entry.get("second_relevance_basis_id"),
        "second_relevance_scope_id": entry.get("second_relevance_scope_id"),
        "second_carrier_context_id": entry.get("second_carrier_context_id"),
        "second_reception_envelope_id": entry.get("second_reception_envelope_id"),
    }


def _merge_locator_facts(
    first_facts: Mapping[str, Any],
    second_facts: Mapping[str, Any],
) -> dict[str, Any]:
    merged = dict(first_facts)
    merged.update(dict(second_facts))
    return merged


def _declared_non_claims_are_clean(request: Mapping[str, Any]) -> bool:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        return False
    return all(declared.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _request_flag(request: Mapping[str, Any], key: str) -> bool:
    return request.get(key) is True


def _declared_or_request_flag(request: Mapping[str, Any], key: str) -> bool:
    declared = request.get("declared_non_claims")
    return _request_flag(request, key) or (
        isinstance(declared, Mapping) and declared.get(key) is True
    )


def _expected_identifier_values() -> dict[str, str]:
    return {
        "first_received_signal_id": DEFAULT_FIRST_RECEIVED_SIGNAL_ID,
        "second_received_signal_id": DEFAULT_SECOND_RECEIVED_SIGNAL_ID,
        "first_relevance_basis_id": DEFAULT_FIRST_RELEVANCE_BASIS_ID,
        "second_relevance_basis_id": DEFAULT_SECOND_RELEVANCE_BASIS_ID,
        "first_relevance_scope_id": DEFAULT_FIRST_RELEVANCE_SCOPE_ID,
        "second_relevance_scope_id": DEFAULT_SECOND_RELEVANCE_SCOPE_ID,
        "first_carrier_context_id": DEFAULT_FIRST_CARRIER_CONTEXT_ID,
        "second_carrier_context_id": DEFAULT_SECOND_CARRIER_CONTEXT_ID,
        "first_reception_envelope_id": DEFAULT_FIRST_RECEPTION_ENVELOPE_ID,
        "second_reception_envelope_id": DEFAULT_SECOND_RECEPTION_ENVELOPE_ID,
    }


def _actual_identifier_values(facts: Mapping[str, Any]) -> dict[str, Any]:
    return {key: facts.get(key) for key in _expected_identifier_values()}


def _basis_lineage_present(facts: Mapping[str, Any]) -> bool:
    required = (
        "basis_first_local_relevance_orientation_index_entry_artifact",
        "basis_second_local_relevance_orientation_index_entry_artifact",
        "first_orientation_view_artifact",
        "second_orientation_view_artifact",
        "first_receipt_artifact",
        "second_receipt_artifact",
        "first_reception_artifact",
        "second_reception_artifact",
        "successor_candidate_admission_artifact",
        "successor_reception_request_artifact",
        "first_received_signal_id",
        "second_received_signal_id",
        "first_relevance_basis_id",
        "second_relevance_basis_id",
        "first_relevance_scope_id",
        "second_relevance_scope_id",
        "first_carrier_context_id",
        "second_carrier_context_id",
        "first_reception_envelope_id",
        "second_reception_envelope_id",
    )
    return all(bool(facts.get(key)) for key in required)


def _build_checks(
    request: Mapping[str, Any],
    first_artifact: Mapping[str, Any] | None,
    first_read_error: str | None,
    second_artifact: Mapping[str, Any] | None,
    second_read_error: str | None,
    facts: Mapping[str, Any],
) -> list[dict[str, Any]]:
    del first_artifact, second_artifact
    question = request.get("local_relevance_medium_multiplicity_result_question")
    intent = request.get("local_relevance_medium_multiplicity_result_intent")
    first_path = request.get("selected_first_local_relevance_orientation_index_entry_artifact")
    second_path = request.get("selected_second_local_relevance_orientation_index_entry_artifact")
    multiplicity_scope = request.get("multiplicity_result_scope")
    multiplicity_type = request.get("multiplicity_result_type")
    checks: list[dict[str, Any]] = []

    checks.append(
        _check(
            "multiplicity_result_question_declared",
            isinstance(question, str) and bool(question.strip()),
            "declared multiplicity result question",
            question,
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "intent_supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "block_intent_not_requested",
            intent != INTENT_BLOCK,
            "block intent absent",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_BLOCK_REQUESTED",
        )
    )
    checks.append(
        _check(
            "selected_first_local_relevance_orientation_index_entry_artifact_path_declared",
            bool(first_path)
            and not _request_flag(
                request,
                "selected_first_local_relevance_orientation_index_entry_artifact_missing",
            ),
            "selected first local relevance orientation index entry artifact path declared",
            first_path,
            "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _check(
            "selected_second_local_relevance_orientation_index_entry_artifact_path_declared",
            bool(second_path)
            and not _request_flag(
                request,
                "selected_second_local_relevance_orientation_index_entry_artifact_missing",
            ),
            "selected second local relevance orientation index entry artifact path declared",
            second_path,
            "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _check(
            "selected_first_local_relevance_orientation_index_entry_artifact_readable_json",
            first_read_error
            not in {
                "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
                "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_UNREADABLE",
            },
            "readable JSON object",
            first_read_error or "readable",
            (
                "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING"
                if first_read_error
                == "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING"
                else "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_UNREADABLE"
            ),
        )
    )
    checks.append(
        _check(
            "selected_second_local_relevance_orientation_index_entry_artifact_readable_json",
            second_read_error
            not in {
                "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
                "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_UNREADABLE",
            },
            "readable JSON object",
            second_read_error or "readable",
            (
                "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING"
                if second_read_error
                == "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING"
                else "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_UNREADABLE"
            ),
        )
    )
    checks.append(
        _check(
            "selected_first_local_relevance_orientation_index_entry_artifact_json_object",
            first_read_error != "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_JSON_OBJECT",
            "JSON object",
            first_read_error or "JSON object",
            "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_JSON_OBJECT",
        )
    )
    checks.append(
        _check(
            "selected_second_local_relevance_orientation_index_entry_artifact_json_object",
            second_read_error
            != "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_JSON_OBJECT",
            "JSON object",
            second_read_error or "JSON object",
            "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_JSON_OBJECT",
        )
    )
    checks.append(
        _check(
            "first_local_relevance_orientation_index_entry_artifact_outcome_recorded",
            facts.get("basis_first_local_relevance_orientation_index_entry_outcome")
            == FIRST_LOCATOR_RECORDED_OUTCOME
            and not _request_flag(
                request,
                "first_local_relevance_orientation_index_entry_artifact_not_recorded",
            ),
            FIRST_LOCATOR_RECORDED_OUTCOME,
            facts.get("basis_first_local_relevance_orientation_index_entry_outcome"),
            "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "second_local_relevance_orientation_index_entry_artifact_outcome_recorded",
            facts.get("basis_second_local_relevance_orientation_index_entry_outcome")
            == SECOND_LOCATOR_RECORDED_OUTCOME
            and not _request_flag(
                request,
                "second_local_relevance_orientation_index_entry_artifact_not_recorded",
            ),
            SECOND_LOCATOR_RECORDED_OUTCOME,
            facts.get("basis_second_local_relevance_orientation_index_entry_outcome"),
            "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "first_local_relevance_orientation_index_entry_artifact_result_version_0_1_0",
            facts.get("basis_first_local_relevance_orientation_index_entry_result_version")
            == RESULT_VERSION
            and not _request_flag(
                request,
                "first_local_relevance_orientation_index_entry_artifact_version_not_0_1_0",
            ),
            RESULT_VERSION,
            facts.get("basis_first_local_relevance_orientation_index_entry_result_version"),
            "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _check(
            "second_local_relevance_orientation_index_entry_artifact_result_version_0_1_0",
            facts.get("basis_second_local_relevance_orientation_index_entry_result_version")
            == RESULT_VERSION
            and not _request_flag(
                request,
                "second_local_relevance_orientation_index_entry_artifact_version_not_0_1_0",
            ),
            RESULT_VERSION,
            facts.get("basis_second_local_relevance_orientation_index_entry_result_version"),
            "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    first_failed_count = facts.get(
        "basis_first_local_relevance_orientation_index_entry_failed_check_count"
    )
    second_failed_count = facts.get(
        "basis_second_local_relevance_orientation_index_entry_failed_check_count"
    )
    checks.append(
        _check(
            "first_local_relevance_orientation_index_entry_artifact_failed_check_count_zero",
            first_failed_count == 0
            and not _request_flag(
                request,
                "first_local_relevance_orientation_index_entry_artifact_failed_checks_present",
            ),
            0,
            first_failed_count,
            "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "second_local_relevance_orientation_index_entry_artifact_failed_check_count_zero",
            second_failed_count == 0
            and not _request_flag(
                request,
                "second_local_relevance_orientation_index_entry_artifact_failed_checks_present",
            ),
            0,
            second_failed_count,
            "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "first_local_relevance_orientation_index_entry_object_present",
            bool(facts.get("first_local_relevance_orientation_index_entry"))
            and not _request_flag(
                request, "first_local_relevance_orientation_index_entry_object_missing"
            ),
            "one first local relevance orientation index entry object",
            "present"
            if facts.get("first_local_relevance_orientation_index_entry")
            else "missing",
            "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_OBJECT_MISSING",
        )
    )
    checks.append(
        _check(
            "second_local_relevance_orientation_index_entry_object_present",
            bool(facts.get("second_local_relevance_orientation_index_entry"))
            and not _request_flag(
                request, "second_local_relevance_orientation_index_entry_object_missing"
            ),
            "one second local relevance orientation index entry object",
            "present"
            if facts.get("second_local_relevance_orientation_index_entry")
            else "missing",
            "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_OBJECT_MISSING",
        )
    )

    presence_checks = (
        (
            "first_locator_artifact_preserved",
            "basis_first_local_relevance_orientation_index_entry_artifact",
            "first_locator_artifact_missing",
            "FIRST_LOCATOR_ARTIFACT_MISSING",
        ),
        (
            "second_locator_artifact_preserved",
            "basis_second_local_relevance_orientation_index_entry_artifact",
            "second_locator_artifact_missing",
            "SECOND_LOCATOR_ARTIFACT_MISSING",
        ),
        (
            "first_orientation_view_artifact_preserved",
            "first_orientation_view_artifact",
            "first_orientation_view_artifact_missing",
            "FIRST_ORIENTATION_VIEW_ARTIFACT_MISSING",
        ),
        (
            "second_orientation_view_artifact_preserved",
            "second_orientation_view_artifact",
            "second_orientation_view_artifact_missing",
            "SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
        ),
        (
            "first_receipt_artifact_preserved",
            "first_receipt_artifact",
            "first_receipt_artifact_missing",
            "FIRST_RECEIPT_ARTIFACT_MISSING",
        ),
        (
            "second_receipt_artifact_preserved",
            "second_receipt_artifact",
            "second_receipt_artifact_missing",
            "SECOND_RECEIPT_ARTIFACT_MISSING",
        ),
        (
            "first_reception_artifact_preserved",
            "first_reception_artifact",
            "first_reception_artifact_missing",
            "FIRST_RECEPTION_ARTIFACT_MISSING",
        ),
        (
            "second_reception_artifact_preserved",
            "second_reception_artifact",
            "second_reception_artifact_missing",
            "SECOND_RECEPTION_ARTIFACT_MISSING",
        ),
    )
    for check_name, fact_key, request_key, code in presence_checks:
        checks.append(
            _check(
                check_name,
                bool(facts.get(fact_key)) and not _request_flag(request, request_key),
                f"{fact_key} present",
                facts.get(fact_key),
                code,
            )
        )

    identifier_checks = (
        (
            "first_received_signal_id_preserved",
            "first_received_signal_id",
            DEFAULT_FIRST_RECEIVED_SIGNAL_ID,
            "first_received_signal_id_missing",
            "FIRST_RECEIVED_SIGNAL_ID_MISSING",
        ),
        (
            "second_received_signal_id_preserved",
            "second_received_signal_id",
            DEFAULT_SECOND_RECEIVED_SIGNAL_ID,
            "second_received_signal_id_missing",
            "SECOND_RECEIVED_SIGNAL_ID_MISSING",
        ),
        (
            "first_relevance_basis_id_preserved",
            "first_relevance_basis_id",
            DEFAULT_FIRST_RELEVANCE_BASIS_ID,
            "first_relevance_basis_id_missing",
            "FIRST_RELEVANCE_BASIS_ID_MISSING",
        ),
        (
            "second_relevance_basis_id_preserved",
            "second_relevance_basis_id",
            DEFAULT_SECOND_RELEVANCE_BASIS_ID,
            "second_relevance_basis_id_missing",
            "SECOND_RELEVANCE_BASIS_ID_MISSING",
        ),
        (
            "first_relevance_scope_id_preserved",
            "first_relevance_scope_id",
            DEFAULT_FIRST_RELEVANCE_SCOPE_ID,
            "first_relevance_scope_id_missing",
            "FIRST_RELEVANCE_SCOPE_ID_MISSING",
        ),
        (
            "second_relevance_scope_id_preserved",
            "second_relevance_scope_id",
            DEFAULT_SECOND_RELEVANCE_SCOPE_ID,
            "second_relevance_scope_id_missing",
            "SECOND_RELEVANCE_SCOPE_ID_MISSING",
        ),
        (
            "first_carrier_context_id_preserved",
            "first_carrier_context_id",
            DEFAULT_FIRST_CARRIER_CONTEXT_ID,
            "first_carrier_context_id_missing",
            "FIRST_CARRIER_CONTEXT_ID_MISSING",
        ),
        (
            "second_carrier_context_id_preserved",
            "second_carrier_context_id",
            DEFAULT_SECOND_CARRIER_CONTEXT_ID,
            "second_carrier_context_id_missing",
            "SECOND_CARRIER_CONTEXT_ID_MISSING",
        ),
        (
            "first_reception_envelope_id_preserved",
            "first_reception_envelope_id",
            DEFAULT_FIRST_RECEPTION_ENVELOPE_ID,
            "first_reception_envelope_id_missing",
            "FIRST_RECEPTION_ENVELOPE_ID_MISSING",
        ),
        (
            "second_reception_envelope_id_preserved",
            "second_reception_envelope_id",
            DEFAULT_SECOND_RECEPTION_ENVELOPE_ID,
            "second_reception_envelope_id_missing",
            "SECOND_RECEPTION_ENVELOPE_ID_MISSING",
        ),
    )
    for check_name, fact_key, expected, request_key, code in identifier_checks:
        checks.append(
            _check(
                check_name,
                facts.get(fact_key) == expected and not _request_flag(request, request_key),
                expected,
                facts.get(fact_key),
                code,
            )
        )

    checks.append(
        _check(
            "first_and_second_received_signal_ids_distinct",
            bool(facts.get("first_received_signal_id"))
            and bool(facts.get("second_received_signal_id"))
            and facts.get("first_received_signal_id") != facts.get("second_received_signal_id")
            and not _request_flag(
                request, "first_and_second_received_signal_ids_not_distinct"
            ),
            "first and second received signal ids distinct",
            {
                "first_received_signal_id": facts.get("first_received_signal_id"),
                "second_received_signal_id": facts.get("second_received_signal_id"),
            },
            "FIRST_AND_SECOND_RECEIVED_SIGNAL_IDS_NOT_DISTINCT",
        )
    )
    checks.append(
        _check(
            "multiplicity_result_type_declared",
            bool(multiplicity_type),
            MULTIPLICITY_RESULT_TYPE,
            multiplicity_type,
            "MULTIPLICITY_RESULT_TYPE_MISSING",
        )
    )
    checks.append(
        _check(
            "multiplicity_result_type_exact",
            multiplicity_type == MULTIPLICITY_RESULT_TYPE
            and not _request_flag(
                request, "multiplicity_result_type_not_local_relevance_medium_multiplicity_result"
            ),
            MULTIPLICITY_RESULT_TYPE,
            multiplicity_type,
            "MULTIPLICITY_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT",
        )
    )
    checks.append(
        _check(
            "multiplicity_result_scope_declared",
            bool(multiplicity_scope),
            MULTIPLICITY_RESULT_SCOPE,
            multiplicity_scope,
            "MULTIPLICITY_RESULT_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "multiplicity_result_scope_two_local_locators_only",
            multiplicity_scope == MULTIPLICITY_RESULT_SCOPE
            and not _request_flag(
                request, "multiplicity_result_scope_not_two_local_orientation_locators_only"
            ),
            MULTIPLICITY_RESULT_SCOPE,
            multiplicity_scope,
            "MULTIPLICITY_RESULT_SCOPE_NOT_TWO_LOCAL_LOCATORS_ONLY",
        )
    )
    checks.append(
        _check(
            "multiplicity_count_exactly_two",
            request.get("multiplicity_count", 2) == 2
            and not _request_flag(request, "multiplicity_count_not_two"),
            2,
            request.get("multiplicity_count", 2),
            "MULTIPLICITY_COUNT_NOT_TWO",
        )
    )
    checks.append(
        _check(
            "two_local_orientation_locators_present",
            bool(facts.get("first_local_relevance_orientation_index_entry"))
            and bool(facts.get("second_local_relevance_orientation_index_entry"))
            and not _request_flag(request, "two_local_orientation_locators_not_present"),
            "two local orientation locator objects present",
            {
                "first_locator_present": bool(
                    facts.get("first_local_relevance_orientation_index_entry")
                ),
                "second_locator_present": bool(
                    facts.get("second_local_relevance_orientation_index_entry")
                ),
            },
            "TWO_LOCAL_ORIENTATION_LOCATORS_NOT_PRESENT",
        )
    )
    checks.append(
        _check(
            "basis_lineage_preserved",
            _basis_lineage_present(facts)
            and not _request_flag(request, "basis_lineage_not_preserved"),
            "basis lineage preserved",
            {key: facts.get(key) for key in sorted(facts) if key.endswith("_artifact")},
            "BASIS_LINEAGE_NOT_PRESERVED",
        )
    )
    checks.append(
        _check(
            "multiplicity_result_recorded",
            not _request_flag(request, "multiplicity_result_not_recorded"),
            True,
            not _request_flag(request, "multiplicity_result_not_recorded"),
            "MULTIPLICITY_RESULT_NOT_RECORDED",
        )
    )

    for field_name, block_code in FALSE_REQUEST_BLOCKS:
        checks.append(
            _check(
                f"{field_name}_false",
                not _declared_or_request_flag(request, field_name),
                False,
                _declared_or_request_flag(request, field_name),
                block_code,
            )
        )

    checks.append(
        _check(
            "predecessor_failure_evidence_preserved",
            not (
                _request_flag(request, "predecessor_failure_repaired")
                or _request_flag(request, "predecessor_failure_hidden")
                or _request_flag(request, "predecessor_failure_claimed_passed")
            ),
            "predecessor failure evidence preserved",
            {
                "predecessor_failure_repaired": request.get(
                    "predecessor_failure_repaired", False
                ),
                "predecessor_failure_hidden": request.get(
                    "predecessor_failure_hidden", False
                ),
                "predecessor_failure_claimed_passed": request.get(
                    "predecessor_failure_claimed_passed", False
                ),
            },
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    )
    checks.append(
        _check(
            "result_level_required_false_non_claims_canonical_false",
            all(value is False for value in _canonical_non_claims().values()),
            "result-level non-claims canonical false",
            _canonical_non_claims(),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    checks.append(
        _check(
            "required_declared_non_claims_false",
            _declared_non_claims_are_clean(request),
            "declared required non-claims present and false",
            request.get("declared_non_claims"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _build_local_relevance_medium_multiplicity_result(
    multiplicity_result_id: str,
    facts: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "multiplicity_result_id": multiplicity_result_id,
        "multiplicity_result_type": MULTIPLICITY_RESULT_TYPE,
        "multiplicity_result_version": RESULT_VERSION,
        "multiplicity_result_scope": MULTIPLICITY_RESULT_SCOPE,
        "basis_first_local_relevance_orientation_index_entry_artifact": facts.get(
            "basis_first_local_relevance_orientation_index_entry_artifact"
        ),
        "basis_first_local_relevance_orientation_index_entry_outcome": facts.get(
            "basis_first_local_relevance_orientation_index_entry_outcome"
        ),
        "basis_first_local_relevance_orientation_index_entry_result_version": facts.get(
            "basis_first_local_relevance_orientation_index_entry_result_version"
        ),
        "basis_first_local_relevance_orientation_index_entry_failed_check_count": facts.get(
            "basis_first_local_relevance_orientation_index_entry_failed_check_count"
        ),
        "basis_second_local_relevance_orientation_index_entry_artifact": facts.get(
            "basis_second_local_relevance_orientation_index_entry_artifact"
        ),
        "basis_second_local_relevance_orientation_index_entry_outcome": facts.get(
            "basis_second_local_relevance_orientation_index_entry_outcome"
        ),
        "basis_second_local_relevance_orientation_index_entry_result_version": facts.get(
            "basis_second_local_relevance_orientation_index_entry_result_version"
        ),
        "basis_second_local_relevance_orientation_index_entry_failed_check_count": facts.get(
            "basis_second_local_relevance_orientation_index_entry_failed_check_count"
        ),
        "first_orientation_view_artifact": facts.get("first_orientation_view_artifact"),
        "second_orientation_view_artifact": facts.get("second_orientation_view_artifact"),
        "first_receipt_artifact": facts.get("first_receipt_artifact"),
        "second_receipt_artifact": facts.get("second_receipt_artifact"),
        "first_reception_artifact": facts.get("first_reception_artifact"),
        "second_reception_artifact": facts.get("second_reception_artifact"),
        "successor_candidate_admission_artifact": facts.get(
            "successor_candidate_admission_artifact"
        ),
        "successor_reception_request_artifact": facts.get(
            "successor_reception_request_artifact"
        ),
        "first_received_signal_id": facts.get("first_received_signal_id"),
        "second_received_signal_id": facts.get("second_received_signal_id"),
        "first_relevance_basis_id": facts.get("first_relevance_basis_id"),
        "second_relevance_basis_id": facts.get("second_relevance_basis_id"),
        "first_relevance_scope_id": facts.get("first_relevance_scope_id"),
        "second_relevance_scope_id": facts.get("second_relevance_scope_id"),
        "first_carrier_context_id": facts.get("first_carrier_context_id"),
        "second_carrier_context_id": facts.get("second_carrier_context_id"),
        "first_reception_envelope_id": facts.get("first_reception_envelope_id"),
        "second_reception_envelope_id": facts.get("second_reception_envelope_id"),
        "multiplicity_count": 2,
        "two_local_orientation_locators_present": True,
        "first_locator_preserved": True,
        "second_locator_preserved": True,
        "first_and_second_signals_distinct": True,
        "basis_lineage_preserved": True,
        "multiplicity_result_recorded": True,
        "relation_view_created": False,
        "comparison_view_created": False,
        "index_system_created": False,
        "registry_created": False,
        "search_surface_created": False,
        "ranking_surface_created": False,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "authority_created": False,
        "currentness_created": False,
        "truth_created": False,
        "action_created": False,
        "synchronization_created": False,
        "participation_authorized": False,
        "participant_role_created": False,
        "runtime_permission_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "follow_on_work_authorized": False,
    }


def _build_statement(
    recorded: bool,
    multiplicity_result: Mapping[str, Any],
    facts: Mapping[str, Any],
) -> dict[str, bool]:
    if recorded:
        return {key: True for key in ALLOWED_TRUE_RECORDED_FIELDS}
    return {
        "local_relevance_medium_multiplicity_result_recorded": False,
        "basis_first_local_relevance_orientation_index_entry_artifact_preserved": bool(
            facts.get("basis_first_local_relevance_orientation_index_entry_artifact")
        ),
        "basis_second_local_relevance_orientation_index_entry_artifact_preserved": bool(
            facts.get("basis_second_local_relevance_orientation_index_entry_artifact")
        ),
        "first_orientation_view_artifact_preserved": bool(
            facts.get("first_orientation_view_artifact")
        ),
        "second_orientation_view_artifact_preserved": bool(
            facts.get("second_orientation_view_artifact")
        ),
        "first_receipt_artifact_preserved": bool(facts.get("first_receipt_artifact")),
        "second_receipt_artifact_preserved": bool(facts.get("second_receipt_artifact")),
        "first_reception_artifact_preserved": bool(facts.get("first_reception_artifact")),
        "second_reception_artifact_preserved": bool(
            facts.get("second_reception_artifact")
        ),
        "successor_candidate_admission_artifact_preserved": bool(
            facts.get("successor_candidate_admission_artifact")
        ),
        "successor_reception_request_artifact_preserved": bool(
            facts.get("successor_reception_request_artifact")
        ),
        "first_received_signal_id_preserved": (
            multiplicity_result.get("first_received_signal_id")
            == DEFAULT_FIRST_RECEIVED_SIGNAL_ID
        ),
        "second_received_signal_id_preserved": (
            multiplicity_result.get("second_received_signal_id")
            == DEFAULT_SECOND_RECEIVED_SIGNAL_ID
        ),
        "first_and_second_signals_distinct": (
            bool(facts.get("first_received_signal_id"))
            and facts.get("first_received_signal_id") != facts.get("second_received_signal_id")
        ),
        "first_relevance_basis_id_preserved": (
            multiplicity_result.get("first_relevance_basis_id")
            == DEFAULT_FIRST_RELEVANCE_BASIS_ID
        ),
        "second_relevance_basis_id_preserved": (
            multiplicity_result.get("second_relevance_basis_id")
            == DEFAULT_SECOND_RELEVANCE_BASIS_ID
        ),
        "first_relevance_scope_id_preserved": (
            multiplicity_result.get("first_relevance_scope_id")
            == DEFAULT_FIRST_RELEVANCE_SCOPE_ID
        ),
        "second_relevance_scope_id_preserved": (
            multiplicity_result.get("second_relevance_scope_id")
            == DEFAULT_SECOND_RELEVANCE_SCOPE_ID
        ),
        "first_carrier_context_id_preserved": (
            multiplicity_result.get("first_carrier_context_id")
            == DEFAULT_FIRST_CARRIER_CONTEXT_ID
        ),
        "second_carrier_context_id_preserved": (
            multiplicity_result.get("second_carrier_context_id")
            == DEFAULT_SECOND_CARRIER_CONTEXT_ID
        ),
        "first_reception_envelope_id_preserved": (
            multiplicity_result.get("first_reception_envelope_id")
            == DEFAULT_FIRST_RECEPTION_ENVELOPE_ID
        ),
        "second_reception_envelope_id_preserved": (
            multiplicity_result.get("second_reception_envelope_id")
            == DEFAULT_SECOND_RECEPTION_ENVELOPE_ID
        ),
        "multiplicity_count_is_two": (
            multiplicity_result.get("multiplicity_count") == 2
        ),
        "two_local_orientation_locators_present": (
            bool(facts.get("first_local_relevance_orientation_index_entry"))
            and bool(facts.get("second_local_relevance_orientation_index_entry"))
        ),
        "basis_lineage_preserved": _basis_lineage_present(facts),
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    non_meaning = {
        "multiplicity_result_is_relation_view": False,
        "multiplicity_result_is_comparison_view": False,
        "multiplicity_result_is_index_system": False,
        "multiplicity_result_is_registry": False,
        "multiplicity_result_is_search_surface": False,
        "multiplicity_result_is_ranking_surface": False,
        "multiplicity_result_authorizes_follow_on_work": False,
    }
    non_meaning.update(_canonical_non_claims())
    return non_meaning


def _build_open_items() -> list[str]:
    return [
        "local relevance medium multiplicity result test",
        "local relevance medium multiplicity result live artifact",
        "local relevance medium multiplicity result terminal summary, if needed",
        "relation view",
        "comparison view",
        "local relevance orientation index system",
        "registry",
        "search surface",
        "ranking surface",
        "source transfer",
        "source receipt",
        "derivative reception",
        "vessel relation",
        "adoption",
        "authority creation",
        "currentness creation",
        "truth creation",
        "action",
        "synchronization",
        "participation authorization",
        "participant role",
        "runtime permission",
        "public API",
        "participant-facing interface",
        "distributed network behavior",
        "operation permission",
        "receiving-context governance",
        "deployment",
        "public release",
        "publication flow",
        "broader reusable permission",
        "repeated reception permission",
        "arbitrary reception",
        "feed",
        "follow-on work",
    ]


def build_local_relevance_medium_multiplicity_result_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("local_relevance_medium_multiplicity_result_checks", [])
    if not isinstance(checks, list):
        checks = []
    passed_count, failed_count = _checks_counts(checks)
    metadata = _as_mapping(result.get("local_relevance_medium_multiplicity_result_metadata"))
    block = _as_mapping(result.get("block"))
    statement = _as_mapping(
        result.get("local_relevance_medium_multiplicity_result_statement")
    )
    multiplicity_result = _as_mapping(result.get("local_relevance_medium_multiplicity_result"))
    question = result.get("declared_local_relevance_medium_multiplicity_result_question")
    non_claims = _as_mapping(result.get("non_claims"))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("reason"),
        "multiplicity_result_id": multiplicity_result.get("multiplicity_result_id")
        or metadata.get("local_relevance_medium_multiplicity_result_id"),
        "question": question,
        "intent": metadata.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get("local_relevance_medium_multiplicity_result_version")
        or RESULT_VERSION,
        "resolver_module": metadata.get("resolver_module") or RESOLVER_MODULE,
        "multiplicity_result_recorded": statement.get(
            "local_relevance_medium_multiplicity_result_recorded", False
        ),
        "first_locator_artifact_preserved": statement.get(
            "basis_first_local_relevance_orientation_index_entry_artifact_preserved", False
        ),
        "second_locator_artifact_preserved": statement.get(
            "basis_second_local_relevance_orientation_index_entry_artifact_preserved", False
        ),
        "first_orientation_view_artifact_preserved": statement.get(
            "first_orientation_view_artifact_preserved", False
        ),
        "second_orientation_view_artifact_preserved": statement.get(
            "second_orientation_view_artifact_preserved", False
        ),
        "first_receipt_artifact_preserved": statement.get(
            "first_receipt_artifact_preserved", False
        ),
        "second_receipt_artifact_preserved": statement.get(
            "second_receipt_artifact_preserved", False
        ),
        "first_reception_artifact_preserved": statement.get(
            "first_reception_artifact_preserved", False
        ),
        "second_reception_artifact_preserved": statement.get(
            "second_reception_artifact_preserved", False
        ),
        "successor_candidate_admission_artifact_preserved": statement.get(
            "successor_candidate_admission_artifact_preserved", False
        ),
        "successor_reception_request_artifact_preserved": statement.get(
            "successor_reception_request_artifact_preserved", False
        ),
        "first_received_signal_id_preserved": statement.get(
            "first_received_signal_id_preserved", False
        ),
        "second_received_signal_id_preserved": statement.get(
            "second_received_signal_id_preserved", False
        ),
        "first_and_second_signals_distinct": statement.get(
            "first_and_second_signals_distinct", False
        ),
        "first_relevance_basis_id_preserved": statement.get(
            "first_relevance_basis_id_preserved", False
        ),
        "second_relevance_basis_id_preserved": statement.get(
            "second_relevance_basis_id_preserved", False
        ),
        "first_relevance_scope_id_preserved": statement.get(
            "first_relevance_scope_id_preserved", False
        ),
        "second_relevance_scope_id_preserved": statement.get(
            "second_relevance_scope_id_preserved", False
        ),
        "first_carrier_context_id_preserved": statement.get(
            "first_carrier_context_id_preserved", False
        ),
        "second_carrier_context_id_preserved": statement.get(
            "second_carrier_context_id_preserved", False
        ),
        "first_reception_envelope_id_preserved": statement.get(
            "first_reception_envelope_id_preserved", False
        ),
        "second_reception_envelope_id_preserved": statement.get(
            "second_reception_envelope_id_preserved", False
        ),
        "multiplicity_count_is_two": statement.get("multiplicity_count_is_two", False),
        "two_local_orientation_locators_present": statement.get(
            "two_local_orientation_locators_present", False
        ),
        "basis_lineage_preserved": statement.get("basis_lineage_preserved", False),
        "multiplicity_result_object_summary": {
            "multiplicity_result_type": multiplicity_result.get("multiplicity_result_type"),
            "multiplicity_result_scope": multiplicity_result.get("multiplicity_result_scope"),
            "multiplicity_count": multiplicity_result.get("multiplicity_count"),
            "first_received_signal_id": multiplicity_result.get("first_received_signal_id"),
            "second_received_signal_id": multiplicity_result.get(
                "second_received_signal_id"
            ),
            "first_and_second_signals_distinct": multiplicity_result.get(
                "first_and_second_signals_distinct"
            ),
        },
        "relation_view_and_comparison_view_not_created": True,
        "index_system_registry_search_ranking_not_created": True,
        "repeated_reception_permission_arbitrary_reception_feed_not_created": True,
        "source_authority_currentness_truth_action_synchronization_participation_runtime_not_created": True,
        "public_api_participant_facing_interface_distributed_network_not_created": True,
        "operation_permission_follow_on_not_created": True,
        "key_non_claims": {key: non_claims.get(key, False) for key in REQUIRED_FALSE_NON_CLAIMS},
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": statement.get(
            "result_level_non_claims_canonical_false", False
        ),
    }


def _assemble_result(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> dict[str, Any]:
    passed_count, failed_count = _checks_counts(checks)
    requested_outcome = request.get(
        "requested_local_relevance_medium_multiplicity_result_outcome"
    )
    intent = request.get("local_relevance_medium_multiplicity_result_intent")

    if failed_count:
        outcome = OUTCOME_BLOCKED
    elif requested_outcome in OUTCOME_FAMILY and requested_outcome != OUTCOME_RECORDED:
        outcome = requested_outcome
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif request.get("additional_basis_context"):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    else:
        outcome = OUTCOME_RECORDED

    recorded = outcome == OUTCOME_RECORDED and failed_count == 0
    result_id = str(
        request.get("local_relevance_medium_multiplicity_result_id")
        or DEFAULT_MULTIPLICITY_RESULT_ID
    )
    multiplicity_result = (
        _build_local_relevance_medium_multiplicity_result(result_id, facts)
        if recorded
        else {}
    )
    statement = _build_statement(recorded, multiplicity_result, facts)
    first_failed_code = _first_failed_code(checks)
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": first_failed_code if outcome == OUTCOME_BLOCKED else None,
        "block_code": first_failed_code if outcome == OUTCOME_BLOCKED else None,
        "reason": _sanitize(request.get("block_reason"))
        if outcome == OUTCOME_BLOCKED and request.get("block_reason")
        else (
            "local relevance medium multiplicity result blocked"
            if outcome == OUTCOME_BLOCKED
            else None
        ),
    }

    result: dict[str, Any] = {
        "local_relevance_medium_multiplicity_result_metadata": {
            "local_relevance_medium_multiplicity_result_id": result_id,
            "local_relevance_medium_multiplicity_result_type": MULTIPLICITY_RESULT_TYPE,
            "local_relevance_medium_multiplicity_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
            "intent": intent,
            "passed_check_count": passed_count,
            "failed_check_count": failed_count,
        },
        "declared_local_relevance_medium_multiplicity_result_question": _sanitize(
            request.get("local_relevance_medium_multiplicity_result_question")
        ),
        "selected_local_relevance_orientation_index_entry_artifact_basis": {
            "selected_first_local_relevance_orientation_index_entry_artifact": _sanitize(
                request.get("selected_first_local_relevance_orientation_index_entry_artifact")
            ),
            "selected_second_local_relevance_orientation_index_entry_artifact": _sanitize(
                request.get("selected_second_local_relevance_orientation_index_entry_artifact")
            ),
            "basis_first_local_relevance_orientation_index_entry_artifact": _sanitize(
                facts.get("basis_first_local_relevance_orientation_index_entry_artifact")
            ),
            "basis_first_local_relevance_orientation_index_entry_outcome": facts.get(
                "basis_first_local_relevance_orientation_index_entry_outcome"
            ),
            "basis_first_local_relevance_orientation_index_entry_result_version": facts.get(
                "basis_first_local_relevance_orientation_index_entry_result_version"
            ),
            "basis_first_local_relevance_orientation_index_entry_failed_check_count": facts.get(
                "basis_first_local_relevance_orientation_index_entry_failed_check_count"
            ),
            "basis_second_local_relevance_orientation_index_entry_artifact": _sanitize(
                facts.get("basis_second_local_relevance_orientation_index_entry_artifact")
            ),
            "basis_second_local_relevance_orientation_index_entry_outcome": facts.get(
                "basis_second_local_relevance_orientation_index_entry_outcome"
            ),
            "basis_second_local_relevance_orientation_index_entry_result_version": facts.get(
                "basis_second_local_relevance_orientation_index_entry_result_version"
            ),
            "basis_second_local_relevance_orientation_index_entry_failed_check_count": facts.get(
                "basis_second_local_relevance_orientation_index_entry_failed_check_count"
            ),
        },
        "local_relevance_medium_multiplicity_result": _sanitize(multiplicity_result),
        "local_relevance_medium_multiplicity_result_checks": _sanitize(checks),
        "local_relevance_medium_multiplicity_result_statement": statement,
        "local_relevance_medium_multiplicity_result_non_meaning": _build_non_meaning(),
        "additional_basis_required": _sanitize(request.get("additional_basis_context") or []),
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis") or []),
        "what_remains_open": _build_open_items(),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["local_relevance_medium_multiplicity_result_summary"] = (
        build_local_relevance_medium_multiplicity_result_v0_min_summary(result)
    )
    return result


def resolve_local_relevance_medium_multiplicity_result_v0_min(
    declared_local_relevance_medium_multiplicity_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_local_relevance_medium_multiplicity_result is None:
        request = build_declared_local_relevance_medium_multiplicity_result_v0_min_request()
    elif isinstance(declared_local_relevance_medium_multiplicity_result, Mapping):
        request = copy.deepcopy(dict(declared_local_relevance_medium_multiplicity_result))
    else:
        request = {
            "local_relevance_medium_multiplicity_result_id": (
                DEFAULT_MULTIPLICITY_RESULT_ID
            ),
            "local_relevance_medium_multiplicity_result_question": None,
            "local_relevance_medium_multiplicity_result_intent": None,
            "selected_first_local_relevance_orientation_index_entry_artifact": None,
            "selected_second_local_relevance_orientation_index_entry_artifact": None,
            "multiplicity_result_scope": None,
            "multiplicity_result_type": None,
            "declared_non_claims": {},
            "block_reason": "declared request was not a mapping",
        }
        first_facts = _extract_first_locator_facts(None, None)
        second_facts = _extract_second_locator_facts(None, None)
        facts = _merge_locator_facts(first_facts, second_facts)
        checks = [
            _check(
                "declared_request_mapping",
                False,
                "mapping request",
                type(declared_local_relevance_medium_multiplicity_result).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_REQUEST_MALFORMED",
            )
        ]
        checks.extend(_build_checks(request, None, None, None, None, facts))
        return _assemble_result(request, facts, checks)

    first_path = request.get("selected_first_local_relevance_orientation_index_entry_artifact")
    second_path = request.get("selected_second_local_relevance_orientation_index_entry_artifact")
    if _request_flag(
        request, "selected_first_local_relevance_orientation_index_entry_artifact_missing"
    ):
        first_artifact, first_read_error = (
            None,
            "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
        )
    else:
        first_artifact, first_read_error = _read_json_object(
            first_path,
            "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
            "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_UNREADABLE",
            "FIRST_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_JSON_OBJECT",
        )
    if _request_flag(
        request, "selected_second_local_relevance_orientation_index_entry_artifact_missing"
    ):
        second_artifact, second_read_error = (
            None,
            "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
        )
    else:
        second_artifact, second_read_error = _read_json_object(
            second_path,
            "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
            "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_UNREADABLE",
            "SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_JSON_OBJECT",
        )

    first_facts = _extract_first_locator_facts(
        first_artifact,
        str(first_path) if first_path else None,
    )
    second_facts = _extract_second_locator_facts(
        second_artifact,
        str(second_path) if second_path else None,
    )
    facts = _merge_locator_facts(first_facts, second_facts)
    checks = _build_checks(
        request,
        first_artifact,
        first_read_error,
        second_artifact,
        second_read_error,
        facts,
    )
    return _assemble_result(request, facts, checks)


def resolve_local_relevance_medium_multiplicity_result_v0_min_from_path(
    declared_local_relevance_medium_multiplicity_result_path: Path | str,
) -> dict[str, Any]:
    path = Path(declared_local_relevance_medium_multiplicity_result_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
        raise LocalRelevanceMediumMultiplicityResultV0MinError(
            "declared local relevance medium multiplicity result request unreadable"
        ) from exc
    if not isinstance(loaded, Mapping):
        request = {
            "local_relevance_medium_multiplicity_result_id": (
                DEFAULT_MULTIPLICITY_RESULT_ID
            ),
            "local_relevance_medium_multiplicity_result_question": None,
            "local_relevance_medium_multiplicity_result_intent": None,
            "selected_first_local_relevance_orientation_index_entry_artifact": None,
            "selected_second_local_relevance_orientation_index_entry_artifact": None,
            "multiplicity_result_scope": None,
            "multiplicity_result_type": None,
            "declared_non_claims": {},
            "block_reason": "declared request JSON was not an object",
        }
        first_facts = _extract_first_locator_facts(None, None)
        second_facts = _extract_second_locator_facts(None, None)
        facts = _merge_locator_facts(first_facts, second_facts)
        checks = [
            _check(
                "declared_request_json_object",
                False,
                "JSON object request",
                type(loaded).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_REQUEST_MALFORMED",
            )
        ]
        checks.extend(_build_checks(request, None, None, None, None, facts))
        return _assemble_result(request, facts, checks)
    return resolve_local_relevance_medium_multiplicity_result_v0_min(loaded)


def _next_available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter:03d}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def write_local_relevance_medium_multiplicity_result_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    result_copy = copy.deepcopy(dict(result))
    metadata = _as_mapping(
        result_copy.get("local_relevance_medium_multiplicity_result_metadata")
    )
    result_id = str(
        metadata.get("local_relevance_medium_multiplicity_result_id")
        or DEFAULT_MULTIPLICITY_RESULT_ID
    )
    if output_path is None:
        target = OUTPUT_ROOT / (
            f"{result_id}__local_relevance_medium_multiplicity_result_v0_min_result.json"
        )
    else:
        target = Path(output_path)
        if target.is_dir() or str(output_path).endswith("/"):
            target = target / (
                f"{result_id}__local_relevance_medium_multiplicity_result_v0_min_result.json"
            )
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _next_available_output_path(target)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(result_copy), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def build_declared_local_relevance_medium_multiplicity_result_v0_min_request(
    local_relevance_medium_multiplicity_result_id: str = DEFAULT_MULTIPLICITY_RESULT_ID,
    selected_first_local_relevance_orientation_index_entry_artifact: (
        Path | str
    ) = DEFAULT_FIRST_LOCATOR_ARTIFACT,
    selected_second_local_relevance_orientation_index_entry_artifact: (
        Path | str
    ) = DEFAULT_SECOND_LOCATOR_ARTIFACT,
    multiplicity_result_type: str = MULTIPLICITY_RESULT_TYPE,
    multiplicity_result_scope: str = MULTIPLICITY_RESULT_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    if declared_non_claims is not None:
        non_claims.update(copy.deepcopy(dict(declared_non_claims)))

    request: dict[str, Any] = {
        "local_relevance_medium_multiplicity_result_id": (
            local_relevance_medium_multiplicity_result_id
        ),
        "local_relevance_medium_multiplicity_result_question": (
            "Given one clean first LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY and one clean "
            "second LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY, "
            "may one LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT be recorded that records "
            "exactly two locally discoverable orientation objects in lineage, preserving "
            "first and second locator artifacts and received identifiers, without creating "
            "relation view, comparison view, index system, registry, search, ranking, "
            "repeated reception permission, arbitrary reception, feed, source transfer, "
            "source receipt, authority, currentness, truth, action, synchronization, "
            "participation authorization, participant role, runtime permission, public API, "
            "participant-facing interface, distributed network behavior, operation "
            "permission, or follow-on work?"
        ),
        "local_relevance_medium_multiplicity_result_intent": intent,
        "selected_first_local_relevance_orientation_index_entry_artifact": str(
            selected_first_local_relevance_orientation_index_entry_artifact
        ),
        "selected_second_local_relevance_orientation_index_entry_artifact": str(
            selected_second_local_relevance_orientation_index_entry_artifact
        ),
        "multiplicity_result_scope": multiplicity_result_scope,
        "multiplicity_result_type": multiplicity_result_type,
        "declared_non_claims": non_claims,
    }
    for key, value in overrides.items():
        request[key] = value
    return request
