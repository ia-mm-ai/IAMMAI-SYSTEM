"""Resolve one local read-only selected-state result-object boundary.

This resolver records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY object. It reads
one clean selected-state payload return artifact as payload basis and may record
that one future state result object can be considered later as a separately
bounded step.

The boundary object is boundary-shaped, local, read-only,
selected-state-result-object-consideration-only, and non-result-object-shaped.
It does not create a state result object, expose state packet body or raw/full
state packet body, perform lookup, execute lookup commands, create permissions,
create public or distributed surfaces, discover files, accept entries or
signals, create registry/search/query/ranking surfaces, or authorize follow-on
work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyStateResultObjectBoundaryV0MinError(
    RuntimeError
):
    """Raised for bounded path/write errors in this resolver."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_state_result_object_boundary_v0_min"
)

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_result_object_boundary_v0_min"
)
DEFAULT_STATE_PAYLOAD_RETURN_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_payload_return_v0_min/"
    "local_relevance_medium_read_only_state_payload_return_reference_review_001__"
    "local_relevance_medium_read_only_state_payload_return_v0_min_result.json"
)

DEFAULT_BOUNDARY_ID = (
    "local_relevance_medium_read_only_state_result_object_boundary_001"
)
BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_STATE_RESULT_OBJECT_CONSIDERATION_ONLY"
SELECTED_COMMAND = "state"

STATE_PAYLOAD_RETURN_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_RECORDED"
)
STATE_PAYLOAD_RETURN_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN"
STATE_PAYLOAD_RETURN_SCOPE = "SELECTED_STATE_PAYLOAD_RETURN_ONLY"

SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN for "
    "selected command state, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY be recorded "
    "that permits a future state result object for that selected-state payload "
    "return to be considered as a separately bounded step, without creating "
    "state result object, exposing state packet body, exposing raw/full state "
    "packet body, performing lookup, executing lookup command, creating "
    "operation permission, creating runtime permission, creating public API, "
    "creating participant-facing interface, creating distributed network "
    "behavior, creating general lookup permission, creating arbitrary lookup "
    "permission, permitting unsupported commands, permitting unsupported lookup "
    "keys, creating new lookup result, creating new lookup entry, accepting new "
    "entries, accepting new signals, performing filesystem discovery, creating "
    "query surface, registry, search, ranking, scoring, priority, validity "
    "judgment, truth judgment, authority, currentness, synchronization, "
    "participation authorization, participant role, repeated reception "
    "permission, arbitrary reception, feed, source transfer, source receipt, or "
    "follow-on work?"
)

BOUNDARY_OBJECT_FALSE_FIELDS = (
    "state_result_object_created",
    "state_packet_body_exposed",
    "raw_full_state_packet_body_exposed",
    "lookup_performed",
    "lookup_command_executed",
    "operation_permission_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_commands_permitted",
    "unsupported_lookup_keys_permitted",
    "new_lookup_result_created",
    "new_lookup_entry_created",
    "new_signal_accepted",
    "new_entry_accepted",
    "new_relevance_object_created",
    "new_index_entry_created",
    "filesystem_discovery_performed",
    "registry_created",
    "search_surface_created",
    "query_surface_created",
    "ranking_surface_created",
    "scoring_surface_created",
    "priority_surface_created",
    "validity_judgment_created",
    "truth_judgment_created",
    "authority_judgment_created",
    "currentness_judgment_created",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "authority_created",
    "currentness_created",
    "truth_created",
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "follow_on_work_authorized",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "state_result_object_created",
    "state_packet_body_exposed",
    "raw_full_state_packet_body_exposed",
    "lookup_performed",
    "lookup_command_executed",
    "operation_permission_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_commands_permitted",
    "unsupported_lookup_keys_permitted",
    "new_lookup_result_created",
    "new_lookup_entry_created",
    "new_signal_accepted",
    "new_entry_accepted",
    "new_relevance_object_created",
    "new_index_entry_created",
    "filesystem_discovery_performed",
    "registry_created",
    "search_surface_created",
    "query_surface_created",
    "ranking_surface_created",
    "scoring_surface_created",
    "priority_surface_created",
    "validity_judgment_created",
    "truth_judgment_created",
    "authority_judgment_created",
    "currentness_judgment_created",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "source_created",
    "authority_created",
    "currentness_created",
    "truth_created",
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "deployment_created",
    "public_release_created",
    "broader_reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "follow_on_work_authorized",
    "artifact_existence_treated_as_state_result_object_boundary_authority",
    "latest_file_posture_treated_as_state_result_object_boundary_authority",
    "repo_local_availability_treated_as_state_result_object_boundary_authority",
    "hidden_repo_state_used_as_state_result_object_boundary_content",
    "hidden_repo_state_used_as_state_result_object_boundary_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_state_result_object_boundary_recorded",
    "basis_state_payload_return_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_state_payload_return_recorded",
    "state_payload_returned",
    "state_payload_return_local_only",
    "state_payload_return_read_only",
    "future_state_result_object_may_be_considered",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_BLOCK_REQUESTED",
    "STATE_PAYLOAD_RETURN_ARTIFACT_PATH_MISSING",
    "STATE_PAYLOAD_RETURN_ARTIFACT_UNREADABLE",
    "STATE_PAYLOAD_RETURN_ARTIFACT_NOT_JSON_OBJECT",
    "STATE_PAYLOAD_RETURN_ARTIFACT_NOT_RECORDED",
    "STATE_PAYLOAD_RETURN_ARTIFACT_FAILED_CHECKS_PRESENT",
    "STATE_PAYLOAD_RETURN_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_STATE_PAYLOAD_RETURN_NOT_RECORDED",
    "STATE_PAYLOAD_NOT_RETURNED",
    "STATE_PAYLOAD_RETURN_LOCAL_ONLY_NOT_TRUE",
    "STATE_PAYLOAD_RETURN_READ_ONLY_NOT_TRUE",
    "FUTURE_STATE_RESULT_OBJECT_MAY_NOT_BE_CONSIDERED",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_SELECTED_STATE_RESULT_OBJECT_CONSIDERATION_ONLY",
    "STATE_RESULT_OBJECT_CREATED",
    "STATE_PACKET_BODY_EXPOSED",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSED",
    "LOOKUP_PERFORMED",
    "LOOKUP_COMMAND_EXECUTED",
    "OPERATION_PERMISSION_CREATED",
    "RUNTIME_PERMISSION_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "GENERAL_LOOKUP_PERMISSION_CREATED",
    "ARBITRARY_LOOKUP_PERMISSION_CREATED",
    "UNSUPPORTED_COMMANDS_PERMITTED",
    "UNSUPPORTED_LOOKUP_KEYS_PERMITTED",
    "NEW_LOOKUP_RESULT_CREATED",
    "NEW_LOOKUP_ENTRY_CREATED",
    "NEW_SIGNAL_ACCEPTED",
    "NEW_ENTRY_ACCEPTED",
    "NEW_RELEVANCE_OBJECT_CREATED",
    "NEW_INDEX_ENTRY_CREATED",
    "FILESYSTEM_DISCOVERY_PERFORMED",
    "REGISTRY_CREATED",
    "SEARCH_SURFACE_CREATED",
    "QUERY_SURFACE_CREATED",
    "RANKING_SURFACE_CREATED",
    "SCORING_SURFACE_CREATED",
    "PRIORITY_SURFACE_CREATED",
    "VALIDITY_JUDGMENT_CREATED",
    "TRUTH_JUDGMENT_CREATED",
    "AUTHORITY_JUDGMENT_CREATED",
    "CURRENTNESS_JUDGMENT_CREATED",
    "REPEATED_RECEPTION_PERMISSION_CREATED",
    "ARBITRARY_RECEPTION_CREATED",
    "FEED_CREATED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "TRUTH_CREATED",
    "SYNCHRONIZATION_CREATED",
    "PARTICIPATION_AUTHORIZED",
    "PARTICIPANT_ROLE_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_STATE_RESULT_OBJECT_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_STATE_RESULT_OBJECT_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_STATE_RESULT_OBJECT_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_STATE_RESULT_OBJECT_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_STATE_RESULT_OBJECT_BOUNDARY_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_REQUEST_UNREADABLE",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_OBJECT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_RETURN_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_state_result_object_boundary_body",
    "raw_state_result_body",
    "raw_state_packet_body",
    "raw_full_state_packet_body",
    "raw_state_payload_return_body",
    "raw_state_payload_body",
    "raw_lookup_result_body",
    "raw_lookup_performed_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "state_result_object_boundary_body",
    "state_result_body",
    "state_packet_body",
    "full_state_packet_body",
    "state_payload_return_body",
    "state_payload_body",
    "lookup_result_body",
    "lookup_performed_body",
    "source_body",
    "authority_body",
    "currentness_body",
    "synchronization_body",
    "public_api_body",
    "participant_facing_interface_body",
    "distributed_network_behavior_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

OFFICIAL_STRINGS = {
    BOUNDARY_TYPE,
    BOUNDARY_SCOPE,
    SELECTED_COMMAND,
    STATE_PAYLOAD_RETURN_RECORDED_OUTCOME,
    STATE_PAYLOAD_RETURN_TYPE,
    STATE_PAYLOAD_RETURN_SCOPE,
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
    *OUTCOME_FAMILY,
    *BLOCK_CODES,
    *REQUIRED_FALSE_NON_CLAIMS,
    *ALLOWED_TRUE_RECORDED_FIELDS,
}

SHORTCUT_BLOCK_CODES = {
    "state_payload_return_artifact_missing": "STATE_PAYLOAD_RETURN_ARTIFACT_PATH_MISSING",
    "state_payload_return_artifact_not_recorded": "STATE_PAYLOAD_RETURN_ARTIFACT_NOT_RECORDED",
    "state_payload_return_artifact_failed_checks_present": "STATE_PAYLOAD_RETURN_ARTIFACT_FAILED_CHECKS_PRESENT",
    "state_payload_return_artifact_version_not_0_1_0": "STATE_PAYLOAD_RETURN_ARTIFACT_VERSION_NOT_0_1_0",
    "selected_command_missing": "SELECTED_COMMAND_MISSING",
    "selected_command_not_state": "SELECTED_COMMAND_NOT_STATE",
    "selected_state_payload_return_not_recorded": "SELECTED_STATE_PAYLOAD_RETURN_NOT_RECORDED",
    "state_payload_not_returned": "STATE_PAYLOAD_NOT_RETURNED",
    "state_payload_return_local_only_not_true": "STATE_PAYLOAD_RETURN_LOCAL_ONLY_NOT_TRUE",
    "state_payload_return_read_only_not_true": "STATE_PAYLOAD_RETURN_READ_ONLY_NOT_TRUE",
    "future_state_result_object_may_not_be_considered": "FUTURE_STATE_RESULT_OBJECT_MAY_NOT_BE_CONSIDERED",
    "boundary_type_not_local_relevance_medium_read_only_state_result_object_boundary": "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY",
    "boundary_scope_not_selected_state_result_object_consideration_only": "BOUNDARY_SCOPE_NOT_SELECTED_STATE_RESULT_OBJECT_CONSIDERATION_ONLY",
    "state_result_object_created": "STATE_RESULT_OBJECT_CREATED",
    "state_packet_body_exposed": "STATE_PACKET_BODY_EXPOSED",
    "raw_full_state_packet_body_exposed": "RAW_FULL_STATE_PACKET_BODY_EXPOSED",
    "lookup_performed": "LOOKUP_PERFORMED",
    "lookup_command_executed": "LOOKUP_COMMAND_EXECUTED",
    "operation_permission_created": "OPERATION_PERMISSION_CREATED",
    "runtime_permission_created": "RUNTIME_PERMISSION_CREATED",
    "public_api_created": "PUBLIC_API_CREATED",
    "participant_facing_interface_created": "PARTICIPANT_FACING_INTERFACE_CREATED",
    "distributed_network_behavior_created": "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "general_lookup_permission_created": "GENERAL_LOOKUP_PERMISSION_CREATED",
    "arbitrary_lookup_permission_created": "ARBITRARY_LOOKUP_PERMISSION_CREATED",
    "unsupported_commands_permitted": "UNSUPPORTED_COMMANDS_PERMITTED",
    "unsupported_lookup_keys_permitted": "UNSUPPORTED_LOOKUP_KEYS_PERMITTED",
    "new_lookup_result_created": "NEW_LOOKUP_RESULT_CREATED",
    "new_lookup_entry_created": "NEW_LOOKUP_ENTRY_CREATED",
    "new_signal_accepted": "NEW_SIGNAL_ACCEPTED",
    "new_entry_accepted": "NEW_ENTRY_ACCEPTED",
    "new_relevance_object_created": "NEW_RELEVANCE_OBJECT_CREATED",
    "new_index_entry_created": "NEW_INDEX_ENTRY_CREATED",
    "filesystem_discovery_performed": "FILESYSTEM_DISCOVERY_PERFORMED",
    "registry_created": "REGISTRY_CREATED",
    "search_surface_created": "SEARCH_SURFACE_CREATED",
    "query_surface_created": "QUERY_SURFACE_CREATED",
    "ranking_surface_created": "RANKING_SURFACE_CREATED",
    "scoring_surface_created": "SCORING_SURFACE_CREATED",
    "priority_surface_created": "PRIORITY_SURFACE_CREATED",
    "validity_judgment_created": "VALIDITY_JUDGMENT_CREATED",
    "truth_judgment_created": "TRUTH_JUDGMENT_CREATED",
    "authority_judgment_created": "AUTHORITY_JUDGMENT_CREATED",
    "currentness_judgment_created": "CURRENTNESS_JUDGMENT_CREATED",
    "repeated_reception_permission_created": "REPEATED_RECEPTION_PERMISSION_CREATED",
    "arbitrary_reception_created": "ARBITRARY_RECEPTION_CREATED",
    "feed_created": "FEED_CREATED",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "source_created": "SOURCE_CREATED",
    "authority_created": "AUTHORITY_CREATED",
    "currentness_created": "CURRENTNESS_CREATED",
    "truth_created": "TRUTH_CREATED",
    "synchronization_created": "SYNCHRONIZATION_CREATED",
    "participation_authorized": "PARTICIPATION_AUTHORIZED",
    "participant_role_created": "PARTICIPANT_ROLE_CREATED",
    "deployment_created": "DEPLOYMENT_CREATED",
    "public_release_created": "PUBLIC_RELEASE_CREATED",
    "broader_reusable_permission_created": "BROADER_REUSABLE_PERMISSION_CREATED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "artifact_existence_treated_as_state_result_object_boundary_authority": "ARTIFACT_EXISTENCE_TREATED_AS_STATE_RESULT_OBJECT_BOUNDARY_AUTHORITY",
    "latest_file_posture_treated_as_state_result_object_boundary_authority": "LATEST_FILE_POSTURE_TREATED_AS_STATE_RESULT_OBJECT_BOUNDARY_AUTHORITY",
    "repo_local_availability_treated_as_state_result_object_boundary_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_STATE_RESULT_OBJECT_BOUNDARY_AUTHORITY",
    "hidden_repo_state_used_as_state_result_object_boundary_content": "HIDDEN_REPO_STATE_USED_AS_STATE_RESULT_OBJECT_BOUNDARY_CONTENT",
    "hidden_repo_state_used_as_state_result_object_boundary_authority": "HIDDEN_REPO_STATE_USED_AS_STATE_RESULT_OBJECT_BOUNDARY_AUTHORITY",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
}

WHAT_REMAINS_OPEN = (
    "local relevance medium read-only state result object boundary resolver successors",
    "state result object",
    "state packet body exposure",
    "raw/full state packet body exposure",
    "lookup command execution",
    "lookup performed",
    "operation permission",
    "runtime permission",
    "public API",
    "participant-facing interface",
    "distributed network behavior",
    "general lookup permission",
    "arbitrary lookup permission",
    "registry",
    "search surface",
    "query surface",
    "ranking surface",
    "source transfer",
    "source receipt",
    "participation authorization",
    "participant role",
    "follow-on work",
)


def _is_mapping(value: Any) -> bool:
    return hasattr(value, "items")


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    normalized = str(key).lower()
    return normalized in SENSITIVE_CONTENT_KEYS or normalized.endswith("_body")


def _sanitize_value(value: Any, key: str | None = None) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if _is_sensitive_key(key):
            return "[REDACTED_BOUNDARY_BODY]"
        sanitized = value
        for sentinel in HOSTILE_SENTINELS:
            sanitized = sanitized.replace(sentinel, "[REDACTED_BOUNDARY_BODY]")
        return sanitized
    if _is_mapping(value):
        return {
            str(item_key): _sanitize_value(item_value, str(item_key))
            for item_key, item_value in value.items()
        }
    if isinstance(value, list):
        return [_sanitize_value(item, key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize_value(item, key) for item in value]
    return value


def _safe_mapping_copy(value: Mapping[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(dict(value.items()))


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _nested_get(mapping: Mapping[str, Any], path: tuple[str, ...]) -> Any:
    current: Any = mapping
    for key in path:
        if not _is_mapping(current) or key not in current:
            return None
        current = current[key]
    return current


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None]:
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except OSError:
        return None, "STATE_PAYLOAD_RETURN_ARTIFACT_UNREADABLE"
    try:
        decoded = json.loads(raw)
    except json.JSONDecodeError:
        return None, "STATE_PAYLOAD_RETURN_ARTIFACT_UNREADABLE"
    if not _is_mapping(decoded):
        return None, "STATE_PAYLOAD_RETURN_ARTIFACT_NOT_JSON_OBJECT"
    return dict(decoded.items()), None


def _read_declared_request_path(path: Path | str) -> tuple[dict[str, Any] | None, str | None]:
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except OSError:
        return (
            None,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_REQUEST_UNREADABLE",
        )
    try:
        decoded = json.loads(raw)
    except json.JSONDecodeError:
        return (
            None,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_REQUEST_UNREADABLE",
        )
    if not _is_mapping(decoded):
        return (
            None,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_REQUEST_MALFORMED",
        )
    return dict(decoded.items()), None


def _payload_return_object(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_payload_return")
    if _is_mapping(value):
        return dict(value.items())
    return {}


def _payload_return_statement(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_payload_return_statement")
    if _is_mapping(value):
        return dict(value.items())
    return {}


def _payload_return_summary(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_payload_return_summary")
    if _is_mapping(value):
        return dict(value.items())
    return {}


def _payload_return_metadata(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_payload_return_metadata")
    if _is_mapping(value):
        return dict(value.items())
    return {}


def _artifact_outcome(artifact: Mapping[str, Any] | None) -> Any:
    summary = _payload_return_summary(artifact)
    return _first_present(
        artifact.get("outcome") if artifact is not None else None,
        summary.get("outcome"),
    )


def _artifact_result_version(artifact: Mapping[str, Any] | None) -> Any:
    summary = _payload_return_summary(artifact)
    metadata = _payload_return_metadata(artifact)
    payload = _payload_return_object(artifact)
    return _first_present(
        summary.get("result_version"),
        metadata.get("local_relevance_medium_read_only_state_payload_return_version"),
        metadata.get("result_version"),
        payload.get("state_payload_return_version"),
    )


def _artifact_failed_check_count(artifact: Mapping[str, Any] | None) -> Any:
    summary = _payload_return_summary(artifact)
    value = _first_present(
        summary.get("failed_check_count"),
        artifact.get("failed_check_count") if artifact is not None else None,
    )
    if value is not None:
        return value
    if artifact is None:
        return None
    checks = artifact.get("local_relevance_medium_read_only_state_payload_return_checks")
    if isinstance(checks, list):
        return sum(1 for check in checks if _is_mapping(check) and not check.get("passed"))
    return None


def _payload_bool(
    payload: Mapping[str, Any],
    statement: Mapping[str, Any],
    key: str,
) -> Any:
    return _first_present(payload.get(key), statement.get(key))


def _as_bool(value: Any) -> bool:
    return value is True


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> None:
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _sanitize_value(expected_posture),
            "actual_posture": _sanitize_value(actual_posture),
            "block_code": None if passed else code,
            "failure_code": None if passed else code,
        }
    )


def _declared_non_claims_are_false(request: Mapping[str, Any]) -> bool:
    declared = request.get("declared_non_claims")
    if not _is_mapping(declared):
        return False
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared or declared[key] is not False:
            return False
    return True


def _first_failed_code(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            if code in BLOCK_CODES:
                return code
    return None


def _block(code: str | None, reason: Any = None) -> dict[str, Any]:
    if code is None:
        return {"blocked": False, "code": None, "block_code": None, "reason": None}
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": _sanitize_value(reason if reason is not None else code),
    }


def _build_boundary_object(
    *,
    boundary_id: str,
    state_payload_return_artifact: Any,
    basis_outcome: Any,
    basis_result_version: Any,
    basis_failed_check_count: Any,
) -> dict[str, Any]:
    boundary: dict[str, Any] = {
        "boundary_id": boundary_id,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "basis_state_payload_return_artifact": str(state_payload_return_artifact),
        "basis_state_payload_return_outcome": basis_outcome,
        "basis_state_payload_return_result_version": basis_result_version,
        "basis_state_payload_return_failed_check_count": basis_failed_check_count,
        "selected_command": SELECTED_COMMAND,
        "selected_command_is_state": True,
        "selected_state_payload_return_recorded": True,
        "state_payload_returned": True,
        "state_payload_return_local_only": True,
        "state_payload_return_read_only": True,
        "future_state_result_object_may_be_considered": True,
    }
    for field in BOUNDARY_OBJECT_FALSE_FIELDS:
        boundary[field] = False
    return boundary


def _build_statement(recorded: bool) -> dict[str, bool]:
    return {
        "local_relevance_medium_read_only_state_result_object_boundary_recorded": recorded,
        "basis_state_payload_return_artifact_preserved": recorded,
        "selected_command_preserved": recorded,
        "selected_command_is_state": recorded,
        "selected_state_payload_return_recorded": recorded,
        "state_payload_returned": recorded,
        "state_payload_return_local_only": recorded,
        "state_payload_return_read_only": recorded,
        "future_state_result_object_may_be_considered": recorded,
        "result_level_non_claims_canonical_false": True,
        "predecessor_failure_evidence_preserved": True,
        "predecessor_failure_repaired": False,
        "predecessor_failure_hidden": False,
        "predecessor_failure_claimed_passed": False,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "not_state_result_object": True,
        "not_state_packet_body_exposure": True,
        "not_raw_full_state_packet_body_exposure": True,
        "not_lookup_performed": True,
        "not_lookup_command_execution": True,
        "not_operation_permission": True,
        "not_runtime_permission": True,
        "not_public_api": True,
        "not_participant_facing_interface": True,
        "not_distributed_network_behavior": True,
        "not_general_lookup_permission": True,
        "not_arbitrary_lookup_permission": True,
        "not_registry": True,
        "not_search": True,
        "not_query_surface": True,
        "not_ranking": True,
        "not_follow_on_work": True,
    }


def _build_artifact_basis(
    *,
    artifact_path: Any,
    artifact: Mapping[str, Any] | None,
    readable: bool,
    read_error: str | None,
) -> dict[str, Any]:
    return {
        "selected_state_payload_return_artifact": _sanitize_value(str(artifact_path)),
        "artifact_readable_json": readable,
        "artifact_read_error": read_error,
        "basis_state_payload_return_outcome": _artifact_outcome(artifact),
        "basis_state_payload_return_result_version": _artifact_result_version(artifact),
        "basis_state_payload_return_failed_check_count": _artifact_failed_check_count(
            artifact
        ),
        "artifact_preserved": readable and read_error is None,
        "raw_artifact_body_returned": False,
    }


def _result_shell(
    *,
    boundary_id: str,
    question: Any,
    intent: Any,
    artifact_basis: Mapping[str, Any] | None,
    boundary: Mapping[str, Any] | None,
    checks: list[dict[str, Any]],
    outcome: str,
    block_code: str | None,
    additional_basis_required: Any = None,
    not_recorded_basis: Any = None,
    block_reason: Any = None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_state_result_object_boundary_metadata": {
            "local_relevance_medium_read_only_state_result_object_boundary_id": boundary_id,
            "local_relevance_medium_read_only_state_result_object_boundary_type": BOUNDARY_TYPE,
            "local_relevance_medium_read_only_state_result_object_boundary_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
            "declared_intent": _sanitize_value(intent),
        },
        "declared_local_relevance_medium_read_only_state_result_object_boundary_question": _sanitize_value(
            question
        ),
        "selected_state_payload_return_artifact_basis": _sanitize_value(
            artifact_basis or {}
        ),
        "local_relevance_medium_read_only_state_result_object_boundary": _sanitize_value(
            boundary
        )
        if boundary is not None
        else None,
        "local_relevance_medium_read_only_state_result_object_boundary_checks": _sanitize_value(
            checks
        ),
        "local_relevance_medium_read_only_state_result_object_boundary_statement": _build_statement(
            recorded
        ),
        "local_relevance_medium_read_only_state_result_object_boundary_non_meaning": _build_non_meaning(),
        "additional_basis_required": _sanitize_value(additional_basis_required or []),
        "not_recorded_basis": _sanitize_value(not_recorded_basis or []),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": _block(block_code, block_reason),
    }
    result["local_relevance_medium_read_only_state_result_object_boundary_summary"] = (
        build_local_relevance_medium_read_only_state_result_object_boundary_v0_min_summary(
            result
        )
    )
    return _sanitize_value(result)


def _malformed_result(code: str, reason: Any = None) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _check(
        checks,
        "declared local relevance medium read-only state result object boundary request well formed",
        False,
        "mapping request",
        "missing or non-mapping request",
        code,
    )
    return _result_shell(
        boundary_id=DEFAULT_BOUNDARY_ID,
        question=None,
        intent=None,
        artifact_basis={},
        boundary=None,
        checks=checks,
        outcome=OUTCOME_BLOCKED,
        block_code=code,
        block_reason=reason or code,
    )


def resolve_local_relevance_medium_read_only_state_result_object_boundary_v0_min(
    declared_local_relevance_medium_read_only_state_result_object_boundary: Mapping[
        str, Any
    ]
    | None = None,
) -> dict:
    if declared_local_relevance_medium_read_only_state_result_object_boundary is None:
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_REQUEST_MALFORMED",
            "request missing",
        )
    if not _is_mapping(declared_local_relevance_medium_read_only_state_result_object_boundary):
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_REQUEST_MALFORMED",
            "request is not a mapping",
        )

    request = _safe_mapping_copy(
        declared_local_relevance_medium_read_only_state_result_object_boundary
    )
    checks: list[dict[str, Any]] = []

    boundary_id = str(
        request.get("local_relevance_medium_read_only_state_result_object_boundary_id")
        or DEFAULT_BOUNDARY_ID
    )
    question = request.get(
        "local_relevance_medium_read_only_state_result_object_boundary_question"
    )
    intent = request.get(
        "local_relevance_medium_read_only_state_result_object_boundary_intent"
    )
    artifact_path = request.get("selected_state_payload_return_artifact")
    selected_command = request.get("selected_command")
    boundary_type = request.get("boundary_type")
    boundary_scope = request.get("boundary_scope")

    _check(
        checks,
        "state result object boundary question declared",
        bool(question),
        "question declared",
        question if question else "missing",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "boundary intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "boundary block not requested",
        intent != INTENT_BLOCK,
        "not block intent",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_BLOCK_REQUESTED",
    )

    artifact_path_declared = bool(artifact_path) and not request.get(
        "state_payload_return_artifact_missing"
    )
    _check(
        checks,
        "state payload return artifact path declared",
        artifact_path_declared,
        "declared artifact path",
        artifact_path if artifact_path else "missing",
        "STATE_PAYLOAD_RETURN_ARTIFACT_PATH_MISSING",
    )

    artifact: dict[str, Any] | None = None
    read_error: str | None = None
    if artifact_path_declared:
        artifact, read_error = _read_json_object(Path(str(artifact_path)))
    else:
        read_error = "STATE_PAYLOAD_RETURN_ARTIFACT_PATH_MISSING"

    artifact_readable = artifact is not None and read_error is None
    _check(
        checks,
        "state payload return artifact readable JSON",
        artifact_readable,
        "readable JSON object",
        "readable" if artifact_readable else read_error,
        read_error or "STATE_PAYLOAD_RETURN_ARTIFACT_UNREADABLE",
    )

    artifact_basis = _build_artifact_basis(
        artifact_path=artifact_path or "",
        artifact=artifact,
        readable=artifact_readable,
        read_error=read_error,
    )

    payload = _payload_return_object(artifact)
    statement = _payload_return_statement(artifact)
    artifact_outcome = _artifact_outcome(artifact)
    artifact_version = _artifact_result_version(artifact)
    artifact_failed_check_count = _artifact_failed_check_count(artifact)

    _check(
        checks,
        "state payload return artifact outcome recorded",
        artifact_outcome == STATE_PAYLOAD_RETURN_RECORDED_OUTCOME
        and not request.get("state_payload_return_artifact_not_recorded"),
        STATE_PAYLOAD_RETURN_RECORDED_OUTCOME,
        artifact_outcome,
        "STATE_PAYLOAD_RETURN_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "state payload return artifact result version 0.1.0",
        artifact_version == RESULT_VERSION
        and not request.get("state_payload_return_artifact_version_not_0_1_0"),
        RESULT_VERSION,
        artifact_version,
        "STATE_PAYLOAD_RETURN_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "state payload return artifact failed check count zero",
        artifact_failed_check_count == 0
        and not request.get("state_payload_return_artifact_failed_checks_present"),
        0,
        artifact_failed_check_count,
        "STATE_PAYLOAD_RETURN_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    _check(
        checks,
        "selected command declared",
        bool(selected_command) and not request.get("selected_command_missing"),
        "selected command declared",
        selected_command if selected_command else "missing",
        "SELECTED_COMMAND_MISSING",
    )
    artifact_selected_command = payload.get("selected_command")
    selected_command_is_state = (
        selected_command == SELECTED_COMMAND
        and artifact_selected_command in (None, SELECTED_COMMAND)
        and not request.get("selected_command_not_state")
    )
    _check(
        checks,
        "selected command exactly state",
        selected_command_is_state,
        SELECTED_COMMAND,
        {
            "declared_selected_command": selected_command,
            "artifact_selected_command": artifact_selected_command,
        },
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected command is state",
        selected_command_is_state
        and _payload_bool(payload, statement, "selected_command_is_state") is not False,
        True,
        _payload_bool(payload, statement, "selected_command_is_state"),
        "SELECTED_COMMAND_NOT_STATE",
    )

    selected_payload_return_recorded = _payload_bool(
        payload,
        statement,
        "local_relevance_medium_read_only_state_payload_return_recorded",
    )
    if selected_payload_return_recorded is None:
        selected_payload_return_recorded = (
            artifact_outcome == STATE_PAYLOAD_RETURN_RECORDED_OUTCOME
        )
    _check(
        checks,
        "selected-state payload return recorded",
        _as_bool(selected_payload_return_recorded)
        and not request.get("selected_state_payload_return_not_recorded"),
        True,
        selected_payload_return_recorded,
        "SELECTED_STATE_PAYLOAD_RETURN_NOT_RECORDED",
    )
    _check(
        checks,
        "state payload returned",
        _as_bool(_payload_bool(payload, statement, "state_payload_returned"))
        and not request.get("state_payload_not_returned"),
        True,
        _payload_bool(payload, statement, "state_payload_returned"),
        "STATE_PAYLOAD_NOT_RETURNED",
    )
    _check(
        checks,
        "state payload return local only",
        _as_bool(_payload_bool(payload, statement, "state_payload_return_local_only"))
        and not request.get("state_payload_return_local_only_not_true"),
        True,
        _payload_bool(payload, statement, "state_payload_return_local_only"),
        "STATE_PAYLOAD_RETURN_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "state payload return read only",
        _as_bool(_payload_bool(payload, statement, "state_payload_return_read_only"))
        and not request.get("state_payload_return_read_only_not_true"),
        True,
        _payload_bool(payload, statement, "state_payload_return_read_only"),
        "STATE_PAYLOAD_RETURN_READ_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "future state result object may be considered",
        not request.get("future_state_result_object_may_not_be_considered"),
        True,
        not request.get("future_state_result_object_may_not_be_considered"),
        "FUTURE_STATE_RESULT_OBJECT_MAY_NOT_BE_CONSIDERED",
    )

    _check(
        checks,
        "boundary type exact",
        bool(boundary_type) and boundary_type == BOUNDARY_TYPE,
        BOUNDARY_TYPE,
        boundary_type if boundary_type else "missing",
        "BOUNDARY_TYPE_MISSING"
        if not boundary_type
        else "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY",
    )
    _check(
        checks,
        "boundary scope exact",
        bool(boundary_scope) and boundary_scope == BOUNDARY_SCOPE,
        BOUNDARY_SCOPE,
        boundary_scope if boundary_scope else "missing",
        "BOUNDARY_SCOPE_MISSING"
        if not boundary_scope
        else "BOUNDARY_SCOPE_NOT_SELECTED_STATE_RESULT_OBJECT_CONSIDERATION_ONLY",
    )

    for field in BOUNDARY_OBJECT_FALSE_FIELDS:
        code = SHORTCUT_BLOCK_CODES[field]
        actual_posture = _first_present(request.get(field), payload.get(field))
        _check(
            checks,
            field.replace("_", " ") + " false",
            actual_posture is not True,
            False,
            actual_posture if actual_posture is not None else False,
            code,
        )

    for field in (
        "source_created",
        "deployment_created",
        "public_release_created",
        "broader_reusable_permission_created",
    ):
        code = SHORTCUT_BLOCK_CODES[field]
        actual_posture = request.get(field)
        _check(
            checks,
            field.replace("_", " ") + " false",
            actual_posture is not True,
            False,
            actual_posture if actual_posture is not None else False,
            code,
        )

    for field in (
        "artifact_existence_treated_as_state_result_object_boundary_authority",
        "latest_file_posture_treated_as_state_result_object_boundary_authority",
        "repo_local_availability_treated_as_state_result_object_boundary_authority",
        "hidden_repo_state_used_as_state_result_object_boundary_content",
        "hidden_repo_state_used_as_state_result_object_boundary_authority",
    ):
        code = SHORTCUT_BLOCK_CODES[field]
        actual_posture = request.get(field)
        _check(
            checks,
            field.replace("_", " ") + " false",
            actual_posture is not True,
            False,
            actual_posture if actual_posture is not None else False,
            code,
        )

    predecessor_failure_preserved = not (
        request.get("predecessor_failure_repaired")
        or request.get("predecessor_failure_hidden")
        or request.get("predecessor_failure_claimed_passed")
    )
    _check(
        checks,
        "predecessor failure evidence preserved",
        predecessor_failure_preserved,
        "preserved, not repaired, not hidden, not claimed passed",
        {
            "predecessor_failure_repaired": request.get("predecessor_failure_repaired"),
            "predecessor_failure_hidden": request.get("predecessor_failure_hidden"),
            "predecessor_failure_claimed_passed": request.get(
                "predecessor_failure_claimed_passed"
            ),
        },
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _check(
        checks,
        "consumed request not reopened",
        request.get("consumed_request_reopened") is not True,
        False,
        request.get("consumed_request_reopened", False),
        "CONSUMED_REQUEST_REOPENED",
    )
    _check(
        checks,
        "authorization token not reused",
        request.get("authorization_token_reused") is not True,
        False,
        request.get("authorization_token_reused", False),
        "AUTHORIZATION_TOKEN_REUSED",
    )
    _check(
        checks,
        "required non-claims false",
        _declared_non_claims_are_false(request),
        "all required declared non-claims present and false bool",
        "canonical false" if _declared_non_claims_are_false(request) else "missing or flipped",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _check(
        checks,
        "result-level required false non-claims canonical false",
        True,
        "canonical false result-level non-claims",
        "canonical false result-level non-claims",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    block_code = _first_failed_code(checks)
    additional_basis_required: list[Any] = []
    not_recorded_basis: list[Any] = []
    boundary = None

    if block_code is not None:
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
        not_recorded_basis.append(
            "supported do-not-record intent selected; no boundary object recorded"
        )
    elif request.get("additional_basis_context"):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        additional_basis_required.append(request.get("additional_basis_context"))
    else:
        outcome = OUTCOME_RECORDED
        boundary = _build_boundary_object(
            boundary_id=boundary_id,
            state_payload_return_artifact=artifact_path,
            basis_outcome=artifact_outcome,
            basis_result_version=artifact_version,
            basis_failed_check_count=artifact_failed_check_count,
        )

    return _result_shell(
        boundary_id=boundary_id,
        question=question,
        intent=intent,
        artifact_basis=artifact_basis,
        boundary=boundary,
        checks=checks,
        outcome=outcome,
        block_code=block_code,
        additional_basis_required=additional_basis_required,
        not_recorded_basis=not_recorded_basis,
        block_reason=request.get("block_reason") or block_code,
    )


def resolve_local_relevance_medium_read_only_state_result_object_boundary_v0_min_from_path(
    declared_local_relevance_medium_read_only_state_result_object_boundary_path: Path | str,
) -> dict:
    request, error_code = _read_declared_request_path(
        declared_local_relevance_medium_read_only_state_result_object_boundary_path
    )
    if error_code is not None:
        return _malformed_result(error_code, error_code)
    return resolve_local_relevance_medium_read_only_state_result_object_boundary_v0_min(
        request
    )


def build_local_relevance_medium_read_only_state_result_object_boundary_v0_min_summary(
    result: Mapping[str, Any]
) -> dict:
    checks = result.get("local_relevance_medium_read_only_state_result_object_boundary_checks", [])
    if not isinstance(checks, list):
        checks = []
    passed_check_count = sum(
        1 for check in checks if _is_mapping(check) and check.get("passed") is True
    )
    failed_check_count = sum(
        1 for check in checks if _is_mapping(check) and check.get("passed") is not True
    )
    block = result.get("block")
    if not _is_mapping(block):
        block = {}
    metadata = result.get(
        "local_relevance_medium_read_only_state_result_object_boundary_metadata", {}
    )
    if not _is_mapping(metadata):
        metadata = {}
    statement = result.get(
        "local_relevance_medium_read_only_state_result_object_boundary_statement", {}
    )
    if not _is_mapping(statement):
        statement = {}
    boundary = result.get("local_relevance_medium_read_only_state_result_object_boundary")
    if not _is_mapping(boundary):
        boundary = {}
    non_claims = result.get("non_claims", {})
    if not _is_mapping(non_claims):
        non_claims = {}

    def non_claim_false(key: str) -> bool:
        return non_claims.get(key) is False

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("reason"),
        "boundary_id": metadata.get(
            "local_relevance_medium_read_only_state_result_object_boundary_id"
        )
        or boundary.get("boundary_id"),
        "question": result.get(
            "declared_local_relevance_medium_read_only_state_result_object_boundary_question"
        ),
        "intent": metadata.get("declared_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "boundary_recorded": statement.get(
            "local_relevance_medium_read_only_state_result_object_boundary_recorded"
        )
        is True,
        "basis_state_payload_return_artifact_preserved": statement.get(
            "basis_state_payload_return_artifact_preserved"
        )
        is True,
        "selected_command": boundary.get("selected_command") or SELECTED_COMMAND,
        "selected_command_preserved": statement.get("selected_command_preserved")
        is True,
        "selected_command_is_state": statement.get("selected_command_is_state") is True,
        "selected_state_payload_return_recorded": statement.get(
            "selected_state_payload_return_recorded"
        )
        is True,
        "state_payload_returned": statement.get("state_payload_returned") is True,
        "state_payload_return_local_only": statement.get(
            "state_payload_return_local_only"
        )
        is True,
        "state_payload_return_read_only": statement.get(
            "state_payload_return_read_only"
        )
        is True,
        "future_state_result_object_may_be_considered": statement.get(
            "future_state_result_object_may_be_considered"
        )
        is True,
        "boundary_object_summary": {
            "boundary_type": boundary.get("boundary_type"),
            "boundary_scope": boundary.get("boundary_scope"),
            "basis_state_payload_return_outcome": boundary.get(
                "basis_state_payload_return_outcome"
            ),
        },
        "state_result_object_not_created": non_claim_false(
            "state_result_object_created"
        ),
        "state_packet_body_not_exposed": non_claim_false("state_packet_body_exposed"),
        "raw_full_state_packet_body_not_exposed": non_claim_false(
            "raw_full_state_packet_body_exposed"
        ),
        "lookup_not_performed": non_claim_false("lookup_performed"),
        "lookup_command_not_executed": non_claim_false("lookup_command_executed"),
        "operation_permission_not_created": non_claim_false(
            "operation_permission_created"
        ),
        "runtime_permission_not_created": non_claim_false("runtime_permission_created"),
        "public_api_not_created": non_claim_false("public_api_created"),
        "participant_facing_interface_not_created": non_claim_false(
            "participant_facing_interface_created"
        ),
        "distributed_network_behavior_not_created": non_claim_false(
            "distributed_network_behavior_created"
        ),
        "general_lookup_permission_not_created": non_claim_false(
            "general_lookup_permission_created"
        ),
        "arbitrary_lookup_permission_not_created": non_claim_false(
            "arbitrary_lookup_permission_created"
        ),
        "unsupported_commands_not_permitted": non_claim_false(
            "unsupported_commands_permitted"
        ),
        "unsupported_lookup_keys_not_permitted": non_claim_false(
            "unsupported_lookup_keys_permitted"
        ),
        "no_new_lookup_result_or_entry_created": non_claim_false(
            "new_lookup_result_created"
        )
        and non_claim_false("new_lookup_entry_created"),
        "no_new_signal_entry_relevance_object_or_index_entry_created": non_claim_false(
            "new_signal_accepted"
        )
        and non_claim_false("new_entry_accepted")
        and non_claim_false("new_relevance_object_created")
        and non_claim_false("new_index_entry_created"),
        "filesystem_discovery_not_performed": non_claim_false(
            "filesystem_discovery_performed"
        ),
        "source_transfer_source_receipt_not_created": non_claim_false(
            "source_transfer_occurred"
        )
        and non_claim_false("source_receipt_occurred"),
        "registry_search_query_surface_ranking_not_created": non_claim_false(
            "registry_created"
        )
        and non_claim_false("search_surface_created")
        and non_claim_false("query_surface_created")
        and non_claim_false("ranking_surface_created"),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": non_claim_false(
            "scoring_surface_created"
        )
        and non_claim_false("priority_surface_created")
        and non_claim_false("validity_judgment_created")
        and non_claim_false("truth_judgment_created")
        and non_claim_false("authority_judgment_created")
        and non_claim_false("currentness_judgment_created"),
        "repeated_reception_arbitrary_reception_feed_not_created": non_claim_false(
            "repeated_reception_permission_created"
        )
        and non_claim_false("arbitrary_reception_created")
        and non_claim_false("feed_created"),
        "source_authority_currentness_truth_synchronization_participation_participant_role_not_created": non_claim_false(
            "source_created"
        )
        and non_claim_false("authority_created")
        and non_claim_false("currentness_created")
        and non_claim_false("truth_created")
        and non_claim_false("synchronization_created")
        and non_claim_false("participation_authorized")
        and non_claim_false("participant_role_created"),
        "follow_on_not_created": non_claim_false("follow_on_work_authorized"),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "state_result_object_created",
                "state_packet_body_exposed",
                "raw_full_state_packet_body_exposed",
                "lookup_performed",
                "operation_permission_created",
                "runtime_permission_created",
                "public_api_created",
                "distributed_network_behavior_created",
                "follow_on_work_authorized",
            )
        },
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved"
        )
        is True,
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def write_local_relevance_medium_read_only_state_result_object_boundary_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    metadata = result.get(
        "local_relevance_medium_read_only_state_result_object_boundary_metadata", {}
    )
    if not _is_mapping(metadata):
        metadata = {}
    boundary_id = (
        metadata.get("local_relevance_medium_read_only_state_result_object_boundary_id")
        or DEFAULT_BOUNDARY_ID
    )
    filename = (
        f"{boundary_id}__"
        "local_relevance_medium_read_only_state_result_object_boundary_v0_min_result.json"
    )
    if output_path is None:
        candidate = OUTPUT_ROOT / filename
    else:
        supplied = Path(output_path)
        if supplied.suffix:
            candidate = supplied
        else:
            candidate = supplied / filename

    candidate.parent.mkdir(parents=True, exist_ok=True)
    final_path = candidate
    if final_path.exists():
        stem = candidate.stem
        suffix = candidate.suffix
        index = 1
        while True:
            suffixed = candidate.with_name(f"{stem}_{index:03d}{suffix}")
            if not suffixed.exists():
                final_path = suffixed
                break
            index += 1

    final_path.write_text(
        json.dumps(_sanitize_value(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_local_relevance_medium_read_only_state_result_object_boundary_v0_min_request(
    *,
    local_relevance_medium_read_only_state_result_object_boundary_id: str = DEFAULT_BOUNDARY_ID,
    selected_state_payload_return_artifact: Path | str = DEFAULT_STATE_PAYLOAD_RETURN_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    intent: str = INTENT_RECORD,
    question: str = CORE_QUESTION,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    if selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyStateResultObjectBoundaryV0MinError(
            "selected command must be exactly state"
        )
    request = {
        "local_relevance_medium_read_only_state_result_object_boundary_id": (
            local_relevance_medium_read_only_state_result_object_boundary_id
        ),
        "local_relevance_medium_read_only_state_result_object_boundary_question": question,
        "local_relevance_medium_read_only_state_result_object_boundary_intent": intent,
        "selected_state_payload_return_artifact": str(selected_state_payload_return_artifact),
        "selected_command": selected_command,
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "declared_non_claims": _canonical_false_non_claims()
        if declared_non_claims is None
        else copy.deepcopy(dict(declared_non_claims.items())),
    }
    for key, value in overrides.items():
        if key == "selected_command" and value != SELECTED_COMMAND:
            raise LocalRelevanceMediumReadOnlyStateResultObjectBoundaryV0MinError(
                "selected command must be exactly state"
            )
        request[key] = value
    return request
