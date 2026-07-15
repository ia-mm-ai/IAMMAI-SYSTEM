"""Resolve one local read-only selected-state lookup performed event.

This resolver records one ``LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED``
object from one clean lookup performed boundary artifact and one clean
selected-state lookup command execution artifact. It is lookup-performed-shaped
only: no lookup result, operation permission, runtime permission, public API,
participant-facing interface, distributed behavior, registry, search, query
surface, ranking, filesystem discovery, source movement, or follow-on work is
created here.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyLookupPerformedV0MinError(RuntimeError):
    """Raised when a lookup-performed request or result cannot be handled."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_lookup_performed_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_performed_v0_min"
)
DEFAULT_LOOKUP_PERFORMED_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_performed_boundary_v0_min/"
    "local_relevance_medium_read_only_lookup_performed_boundary_reference_review_001__"
    "local_relevance_medium_read_only_lookup_performed_boundary_v0_min_result.json"
)
DEFAULT_LOOKUP_COMMAND_EXECUTION_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_command_execution_v0_min/"
    "local_relevance_medium_read_only_lookup_command_execution_reference_review_001__"
    "local_relevance_medium_read_only_lookup_command_execution_v0_min_result.json"
)

DEFAULT_LOOKUP_PERFORMED_ID = "local_relevance_medium_read_only_lookup_performed_001"
LOOKUP_PERFORMED_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED"
LOOKUP_PERFORMED_SCOPE = "SELECTED_LOOKUP_PERFORMED_ONLY"
SUPPORTED_LOOKUP_PERFORMED_TYPE_VALUES = (LOOKUP_PERFORMED_TYPE,)
SUPPORTED_LOOKUP_PERFORMED_SCOPE_VALUES = (LOOKUP_PERFORMED_SCOPE,)
SELECTED_COMMAND = "state"

LOOKUP_PERFORMED_BOUNDARY_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY_RECORDED"
)
LOOKUP_COMMAND_EXECUTION_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_RECORDED"
)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY "
    "for selected command state, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION, existing reusable "
    "read-only lookup permission, prior lookup-pair coverage, and prior local "
    "carrier command surface, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED be recorded for selected "
    "command state, without creating lookup result, creating operation permission, "
    "creating runtime permission, creating public API, creating participant-facing "
    "interface, creating distributed network behavior, creating general lookup "
    "permission, creating arbitrary lookup permission, permitting unsupported "
    "commands, permitting unsupported lookup keys, creating new lookup entry, "
    "accepting new entries, accepting new signals, performing filesystem discovery, "
    "creating query surface, registry, search, ranking, scoring, priority, validity "
    "judgment, truth judgment, authority, currentness, synchronization, participation "
    "authorization, participant role, repeated reception permission, arbitrary "
    "reception, feed, source transfer, source receipt, or follow-on work?"
)

LOOKUP_PERFORMED_OBJECT_FALSE_FIELDS = (
    "lookup_result_created",
    "operation_permission_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_commands_permitted",
    "unsupported_lookup_keys_permitted",
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
    "consumed_request_reopened",
    "authorization_token_reused",
    "follow_on_work_authorized",
)

REQUEST_ONLY_FALSE_FIELDS = (
    "source_created",
    "deployment_created",
    "public_release_created",
    "broader_reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "artifact_existence_treated_as_lookup_performed_authority",
    "latest_file_posture_treated_as_lookup_performed_authority",
    "repo_local_availability_treated_as_lookup_performed_authority",
    "hidden_repo_state_used_as_lookup_performed_content",
    "hidden_repo_state_used_as_lookup_performed_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

REQUIRED_FALSE_NON_CLAIMS = LOOKUP_PERFORMED_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_lookup_performed_recorded",
    "basis_lookup_performed_boundary_artifact_preserved",
    "basis_lookup_command_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_lookup_command_execution_recorded",
    "lookup_command_executed",
    "lookup_command_execution_local_only",
    "lookup_command_execution_read_only",
    "lookup_performed",
    "lookup_performed_local_only",
    "lookup_performed_read_only",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BLOCK_REQUESTED",
    "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_PATH_MISSING",
    "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_UNREADABLE",
    "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "LOOKUP_COMMAND_EXECUTION_ARTIFACT_PATH_MISSING",
    "LOOKUP_COMMAND_EXECUTION_ARTIFACT_UNREADABLE",
    "LOOKUP_COMMAND_EXECUTION_ARTIFACT_NOT_JSON_OBJECT",
    "LOOKUP_COMMAND_EXECUTION_ARTIFACT_NOT_RECORDED",
    "LOOKUP_COMMAND_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOOKUP_COMMAND_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_LOOKUP_COMMAND_EXECUTION_NOT_RECORDED",
    "LOOKUP_COMMAND_NOT_EXECUTED",
    "LOOKUP_COMMAND_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    "LOOKUP_COMMAND_EXECUTION_READ_ONLY_NOT_TRUE",
    "LOOKUP_PERFORMED_TYPE_MISSING",
    "LOOKUP_PERFORMED_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED",
    "LOOKUP_PERFORMED_SCOPE_MISSING",
    "LOOKUP_PERFORMED_SCOPE_NOT_SELECTED_LOOKUP_PERFORMED_ONLY",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_NOT_RECORDED",
    "LOOKUP_NOT_PERFORMED",
    "LOOKUP_PERFORMED_LOCAL_ONLY_NOT_TRUE",
    "LOOKUP_PERFORMED_READ_ONLY_NOT_TRUE",
    "LOOKUP_RESULT_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "RUNTIME_PERMISSION_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "GENERAL_LOOKUP_PERMISSION_CREATED",
    "ARBITRARY_LOOKUP_PERMISSION_CREATED",
    "UNSUPPORTED_COMMANDS_PERMITTED",
    "UNSUPPORTED_LOOKUP_KEYS_PERMITTED",
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
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "ARTIFACT_EXISTENCE_TREATED_AS_LOOKUP_PERFORMED_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_LOOKUP_PERFORMED_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_LOOKUP_PERFORMED_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_LOOKUP_PERFORMED_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_LOOKUP_PERFORMED_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_REQUEST_UNREADABLE",
)

FALSE_FIELD_BLOCK_CODES = {
    "lookup_result_created": "LOOKUP_RESULT_CREATED",
    "operation_permission_created": "OPERATION_PERMISSION_CREATED",
    "runtime_permission_created": "RUNTIME_PERMISSION_CREATED",
    "public_api_created": "PUBLIC_API_CREATED",
    "participant_facing_interface_created": "PARTICIPANT_FACING_INTERFACE_CREATED",
    "distributed_network_behavior_created": "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "general_lookup_permission_created": "GENERAL_LOOKUP_PERMISSION_CREATED",
    "arbitrary_lookup_permission_created": "ARBITRARY_LOOKUP_PERMISSION_CREATED",
    "unsupported_commands_permitted": "UNSUPPORTED_COMMANDS_PERMITTED",
    "unsupported_lookup_keys_permitted": "UNSUPPORTED_LOOKUP_KEYS_PERMITTED",
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
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
    "adoption_created": "ADOPTION_CREATED",
    "receiving_context_governance_created": "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "publication_flow_created": "PUBLICATION_FLOW_CREATED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "artifact_existence_treated_as_lookup_performed_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_LOOKUP_PERFORMED_AUTHORITY"
    ),
    "latest_file_posture_treated_as_lookup_performed_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_LOOKUP_PERFORMED_AUTHORITY"
    ),
    "repo_local_availability_treated_as_lookup_performed_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_LOOKUP_PERFORMED_AUTHORITY"
    ),
    "hidden_repo_state_used_as_lookup_performed_content": (
        "HIDDEN_REPO_STATE_USED_AS_LOOKUP_PERFORMED_CONTENT"
    ),
    "hidden_repo_state_used_as_lookup_performed_authority": (
        "HIDDEN_REPO_STATE_USED_AS_LOOKUP_PERFORMED_AUTHORITY"
    ),
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "prior_artifacts_mutated": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
}

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_lookup_performed_body",
    "raw_lookup_result_body",
    "raw_lookup_performed_boundary_body",
    "raw_lookup_command_execution_body",
    "raw_lookup_command_execution_boundary_body",
    "raw_full_state_packet_body_exposure_body",
    "raw_full_state_packet_body",
    "raw_state_packet_body_exposure_body",
    "raw_state_packet_body",
    "raw_state_result_object_body",
    "raw_state_result_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "lookup_performed_body",
    "lookup_result_body",
    "lookup_performed_boundary_body",
    "lookup_command_execution_body",
    "lookup_command_execution_boundary_body",
    "full_state_packet_body",
    "state_packet_body_exposure_body",
    "state_packet_body",
    "state_result_object_body",
    "state_result_body",
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

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_COMMAND_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_OBJECT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
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

OFFICIAL_VALUES = {
    RESULT_VERSION,
    RESOLVER_MODULE,
    LOOKUP_PERFORMED_TYPE,
    LOOKUP_PERFORMED_SCOPE,
    SELECTED_COMMAND,
    LOOKUP_PERFORMED_BOUNDARY_RECORDED_OUTCOME,
    LOOKUP_COMMAND_EXECUTION_RECORDED_OUTCOME,
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
    *OUTCOME_FAMILY,
    *BLOCK_CODES,
    *REQUIRED_FALSE_NON_CLAIMS,
    *ALLOWED_TRUE_RECORDED_FIELDS,
}


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    return key in SENSITIVE_CONTENT_KEYS or key.endswith("_body")


def _sanitize(value: Any, key: str | None = None) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if value in OFFICIAL_VALUES:
            return value
        if _is_sensitive_key(key):
            return "[REDACTED_SENSITIVE_CONTENT]"
        sanitized = value
        for sentinel in HOSTILE_SENTINELS:
            sanitized = sanitized.replace(sentinel, "[REDACTED_HOSTILE_SENTINEL]")
        return sanitized
    if isinstance(value, MappingABC):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, key) for item in value]
    return value


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _as_path(value: Any) -> Path | None:
    if value is None or value == "":
        return None
    if isinstance(value, Path):
        return value
    if isinstance(value, str):
        return Path(value)
    return None


def _mapping_section(value: Any, key: str) -> dict[str, Any]:
    if isinstance(value, MappingABC):
        section = value.get(key)
        if isinstance(section, MappingABC):
            return dict(section)
    return {}


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _read_json_object(
    path: Path | None,
    unreadable_code: str,
    not_object_code: str,
) -> tuple[dict[str, Any] | None, str | None]:
    if path is None:
        return None, unreadable_code
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None, unreadable_code
    if not isinstance(parsed, MappingABC):
        return None, not_object_code
    return dict(parsed), None


def _count_failed_checks(checks: Any) -> int | None:
    if not isinstance(checks, list):
        return None
    count = 0
    for check in checks:
        if isinstance(check, MappingABC) and check.get("passed") is False:
            count += 1
    return count


def _artifact_failed_check_count(artifact: Mapping[str, Any], checks_key: str) -> int | None:
    summary_key = checks_key.replace("_checks", "_summary")
    summary = _mapping_section(artifact, summary_key)
    explicit = _first_present(
        artifact.get("failed_check_count"),
        summary.get("failed_check_count"),
        artifact.get("failed_checks"),
        summary.get("failed_checks"),
    )
    if isinstance(explicit, bool):
        return None
    if isinstance(explicit, int):
        return explicit
    return _count_failed_checks(artifact.get(checks_key))


def _artifact_bool(*values: Any) -> bool:
    return any(value is True for value in values)


def _extract_lookup_performed_boundary_basis(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if artifact is None:
        return {}
    boundary = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_performed_boundary"
    )
    statement = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_performed_boundary_statement"
    )
    summary = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_performed_boundary_summary"
    )
    metadata = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_performed_boundary_metadata"
    )
    return {
        "outcome": _first_present(artifact.get("outcome"), summary.get("outcome")),
        "result_version": _first_present(
            summary.get("result_version"),
            metadata.get("result_version"),
            metadata.get("local_relevance_medium_read_only_lookup_performed_boundary_version"),
            boundary.get("boundary_version"),
            artifact.get("result_version"),
        ),
        "failed_check_count": _artifact_failed_check_count(
            artifact, "local_relevance_medium_read_only_lookup_performed_boundary_checks"
        ),
        "boundary_type": boundary.get("boundary_type"),
        "boundary_scope": boundary.get("boundary_scope"),
        "selected_command": _first_present(
            boundary.get("selected_command"),
            summary.get("selected_command"),
            statement.get("selected_command"),
        ),
        "future_lookup_performed_may_be_considered": _artifact_bool(
            boundary.get("future_lookup_performed_may_be_considered"),
            summary.get("future_lookup_performed_may_be_considered"),
            statement.get("future_lookup_performed_may_be_considered"),
        ),
        "selected_command_is_state": _artifact_bool(
            boundary.get("selected_command_is_state"),
            summary.get("selected_command_is_state"),
            statement.get("selected_command_is_state"),
        ),
        "boundary_object": boundary,
    }


def _extract_lookup_command_execution_basis(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if artifact is None:
        return {}
    execution = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_command_execution"
    )
    statement = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_command_execution_statement"
    )
    summary = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_command_execution_summary"
    )
    metadata = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_command_execution_metadata"
    )
    return {
        "outcome": _first_present(artifact.get("outcome"), summary.get("outcome")),
        "result_version": _first_present(
            summary.get("result_version"),
            metadata.get("result_version"),
            metadata.get("local_relevance_medium_read_only_lookup_command_execution_version"),
            execution.get("lookup_command_execution_version"),
            artifact.get("result_version"),
        ),
        "failed_check_count": _artifact_failed_check_count(
            artifact, "local_relevance_medium_read_only_lookup_command_execution_checks"
        ),
        "lookup_command_execution_type": execution.get("lookup_command_execution_type"),
        "lookup_command_execution_scope": execution.get("lookup_command_execution_scope"),
        "selected_command": _first_present(
            execution.get("selected_command"),
            summary.get("selected_command"),
            statement.get("selected_command"),
        ),
        "selected_command_is_state": _artifact_bool(
            execution.get("selected_command_is_state"),
            summary.get("selected_command_is_state"),
            statement.get("selected_command_is_state"),
        ),
        "selected_lookup_command_execution_recorded": _artifact_bool(
            execution.get("selected_lookup_command_execution_recorded"),
            execution.get("local_relevance_medium_read_only_lookup_command_execution_recorded"),
            summary.get("selected_lookup_command_execution_recorded"),
            summary.get("lookup_command_execution_recorded"),
            statement.get("selected_lookup_command_execution_recorded"),
            statement.get("local_relevance_medium_read_only_lookup_command_execution_recorded"),
        ),
        "lookup_command_executed": _artifact_bool(
            execution.get("lookup_command_executed"),
            summary.get("lookup_command_executed"),
            statement.get("lookup_command_executed"),
        ),
        "lookup_command_execution_local_only": _artifact_bool(
            execution.get("lookup_command_execution_local_only"),
            summary.get("lookup_command_execution_local_only"),
            statement.get("lookup_command_execution_local_only"),
        ),
        "lookup_command_execution_read_only": _artifact_bool(
            execution.get("lookup_command_execution_read_only"),
            summary.get("lookup_command_execution_read_only"),
            statement.get("lookup_command_execution_read_only"),
        ),
        "execution_object": execution,
    }


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
    }
    if not passed and code is not None:
        record["block_code"] = code
        record["failure_code"] = code
    return record


def _failed_check_count(result_or_checks: Mapping[str, Any] | list[Any]) -> int:
    checks: Any
    if isinstance(result_or_checks, MappingABC):
        checks = result_or_checks.get("local_relevance_medium_read_only_lookup_performed_checks")
    else:
        checks = result_or_checks
    if not isinstance(checks, list):
        return 0
    return sum(
        1 for check in checks if isinstance(check, MappingABC) and check.get("passed") is False
    )


def _passed_check_count(result_or_checks: Mapping[str, Any] | list[Any]) -> int:
    checks: Any
    if isinstance(result_or_checks, MappingABC):
        checks = result_or_checks.get("local_relevance_medium_read_only_lookup_performed_checks")
    else:
        checks = result_or_checks
    if not isinstance(checks, list):
        return 0
    return sum(
        1 for check in checks if isinstance(check, MappingABC) and check.get("passed") is True
    )


def _first_failure_code(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _block_record(code: str | None, reason: Any = None) -> dict[str, Any]:
    if code is None:
        return {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        }
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": _sanitize(reason if reason is not None else code),
    }


def _declared_non_claims(request: Mapping[str, Any]) -> dict[str, Any]:
    value = request.get("declared_non_claims")
    if isinstance(value, MappingABC):
        return dict(value)
    return {}


def _required_non_claims_false(request: Mapping[str, Any]) -> bool:
    declared = _declared_non_claims(request)
    return all(declared.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _false_field_actual(request: Mapping[str, Any], field: str, *basis_maps: Mapping[str, Any]) -> Any:
    if request.get(field) is True:
        return True
    for basis in basis_maps:
        if basis.get(field) is True:
            return True
    return False


def _build_lookup_performed_object(
    *,
    lookup_performed_id: str,
    recorded: bool,
    selected_lookup_performed_boundary_artifact: Path | None,
    lookup_performed_boundary_basis: Mapping[str, Any],
    selected_lookup_command_execution_artifact: Path | None,
    lookup_command_execution_basis: Mapping[str, Any],
    selected_command: Any,
) -> dict[str, Any]:
    selected_command_value = SELECTED_COMMAND if selected_command == SELECTED_COMMAND else None
    performed = {
        "lookup_performed_id": lookup_performed_id,
        "lookup_performed_type": LOOKUP_PERFORMED_TYPE,
        "lookup_performed_version": RESULT_VERSION,
        "lookup_performed_scope": LOOKUP_PERFORMED_SCOPE,
        "basis_lookup_performed_boundary_artifact": (
            str(selected_lookup_performed_boundary_artifact)
            if selected_lookup_performed_boundary_artifact is not None
            else None
        ),
        "basis_lookup_performed_boundary_outcome": lookup_performed_boundary_basis.get("outcome"),
        "basis_lookup_performed_boundary_result_version": lookup_performed_boundary_basis.get(
            "result_version"
        ),
        "basis_lookup_performed_boundary_failed_check_count": lookup_performed_boundary_basis.get(
            "failed_check_count"
        ),
        "basis_lookup_command_execution_artifact": (
            str(selected_lookup_command_execution_artifact)
            if selected_lookup_command_execution_artifact is not None
            else None
        ),
        "basis_lookup_command_execution_outcome": lookup_command_execution_basis.get("outcome"),
        "basis_lookup_command_execution_result_version": lookup_command_execution_basis.get(
            "result_version"
        ),
        "basis_lookup_command_execution_failed_check_count": lookup_command_execution_basis.get(
            "failed_check_count"
        ),
        "selected_command": selected_command_value,
        "selected_command_is_state": recorded and selected_command_value == SELECTED_COMMAND,
        "selected_lookup_command_execution_recorded": recorded
        and lookup_command_execution_basis.get("selected_lookup_command_execution_recorded") is True,
        "lookup_command_executed": recorded
        and lookup_command_execution_basis.get("lookup_command_executed") is True,
        "lookup_command_execution_local_only": recorded
        and lookup_command_execution_basis.get("lookup_command_execution_local_only") is True,
        "lookup_command_execution_read_only": recorded
        and lookup_command_execution_basis.get("lookup_command_execution_read_only") is True,
        "local_relevance_medium_read_only_lookup_performed_recorded": recorded,
        "lookup_performed": recorded,
        "lookup_performed_local_only": recorded,
        "lookup_performed_read_only": recorded,
    }
    for field in LOOKUP_PERFORMED_OBJECT_FALSE_FIELDS:
        performed[field] = False
    return performed


def _build_statement(
    *,
    recorded: bool,
    lookup_performed_boundary_artifact_preserved: bool,
    lookup_command_execution_artifact_preserved: bool,
    selected_command: Any,
    lookup_command_execution_basis: Mapping[str, Any],
) -> dict[str, bool]:
    if not recorded:
        return {key: False for key in ALLOWED_TRUE_RECORDED_FIELDS}
    selected_command_is_state = selected_command == SELECTED_COMMAND
    return {
        "local_relevance_medium_read_only_lookup_performed_recorded": True,
        "basis_lookup_performed_boundary_artifact_preserved": (
            lookup_performed_boundary_artifact_preserved
        ),
        "basis_lookup_command_execution_artifact_preserved": (
            lookup_command_execution_artifact_preserved
        ),
        "selected_command_preserved": selected_command_is_state,
        "selected_command_is_state": selected_command_is_state,
        "selected_lookup_command_execution_recorded": lookup_command_execution_basis.get(
            "selected_lookup_command_execution_recorded"
        )
        is True,
        "lookup_command_executed": lookup_command_execution_basis.get("lookup_command_executed")
        is True,
        "lookup_command_execution_local_only": lookup_command_execution_basis.get(
            "lookup_command_execution_local_only"
        )
        is True,
        "lookup_command_execution_read_only": lookup_command_execution_basis.get(
            "lookup_command_execution_read_only"
        )
        is True,
        "lookup_performed": True,
        "lookup_performed_local_only": True,
        "lookup_performed_read_only": True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "lookup_performed_only": True,
        "not_lookup_result": True,
        "not_operation_permission": True,
        "not_runtime_permission": True,
        "not_public_api": True,
        "not_participant_facing_interface": True,
        "not_distributed_network_behavior": True,
        "not_general_lookup_permission": True,
        "not_arbitrary_lookup_permission": True,
        "not_unsupported_command_permission": True,
        "not_unsupported_lookup_key_permission": True,
        "not_new_lookup_entry": True,
        "not_registry": True,
        "not_search": True,
        "not_query_surface": True,
        "not_ranking": True,
        "not_filesystem_discovery": True,
        "not_source_transfer": True,
        "not_source_receipt": True,
        "not_follow_on_work": True,
    }


def _build_declared_question_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return _sanitize(
        {
            "local_relevance_medium_read_only_lookup_performed_id": request.get(
                "local_relevance_medium_read_only_lookup_performed_id"
            ),
            "local_relevance_medium_read_only_lookup_performed_question": request.get(
                "local_relevance_medium_read_only_lookup_performed_question"
            ),
            "local_relevance_medium_read_only_lookup_performed_intent": request.get(
                "local_relevance_medium_read_only_lookup_performed_intent"
            ),
            "selected_lookup_performed_boundary_artifact": request.get(
                "selected_lookup_performed_boundary_artifact"
            ),
            "selected_lookup_command_execution_artifact": request.get(
                "selected_lookup_command_execution_artifact"
            ),
            "selected_command": request.get("selected_command"),
            "lookup_performed_type": request.get("lookup_performed_type"),
            "lookup_performed_scope": request.get("lookup_performed_scope"),
        }
    )


def _build_boundary_basis_section(
    path: Path | None,
    basis: Mapping[str, Any],
    artifact_preserved: bool,
) -> dict[str, Any]:
    return {
        "selected_lookup_performed_boundary_artifact": str(path) if path is not None else None,
        "basis_lookup_performed_boundary_artifact_preserved": artifact_preserved,
        "basis_lookup_performed_boundary_outcome": basis.get("outcome"),
        "basis_lookup_performed_boundary_result_version": basis.get("result_version"),
        "basis_lookup_performed_boundary_failed_check_count": basis.get("failed_check_count"),
        "basis_lookup_performed_boundary_selected_command": basis.get("selected_command"),
        "future_lookup_performed_may_be_considered": basis.get(
            "future_lookup_performed_may_be_considered"
        )
        is True,
    }


def _build_command_execution_basis_section(
    path: Path | None,
    basis: Mapping[str, Any],
    artifact_preserved: bool,
) -> dict[str, Any]:
    return {
        "selected_lookup_command_execution_artifact": str(path) if path is not None else None,
        "basis_lookup_command_execution_artifact_preserved": artifact_preserved,
        "basis_lookup_command_execution_outcome": basis.get("outcome"),
        "basis_lookup_command_execution_result_version": basis.get("result_version"),
        "basis_lookup_command_execution_failed_check_count": basis.get("failed_check_count"),
        "basis_lookup_command_execution_selected_command": basis.get("selected_command"),
        "selected_lookup_command_execution_recorded": basis.get(
            "selected_lookup_command_execution_recorded"
        )
        is True,
        "lookup_command_executed": basis.get("lookup_command_executed") is True,
        "lookup_command_execution_local_only": basis.get("lookup_command_execution_local_only")
        is True,
        "lookup_command_execution_read_only": basis.get("lookup_command_execution_read_only")
        is True,
    }


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium read-only lookup result",
        "operation permission",
        "runtime permission",
        "public API",
        "participant-facing interface",
        "distributed network behavior",
        "general lookup permission",
        "arbitrary lookup permission",
        "unsupported-command permission",
        "unsupported-key permission",
        "new lookup entry",
        "registry",
        "search surface",
        "query surface",
        "ranking surface",
        "source transfer",
        "source receipt",
        "authority creation",
        "currentness creation",
        "truth creation",
        "synchronization",
        "participation authorization",
        "participant role",
        "deployment",
        "public release",
        "broader reusable permission",
        "repeated reception permission",
        "arbitrary reception",
        "feed",
        "follow-on work",
    ]


def _build_summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    performed = _mapping_section(result, "local_relevance_medium_read_only_lookup_performed")
    statement = _mapping_section(result, "local_relevance_medium_read_only_lookup_performed_statement")
    question = _mapping_section(
        result, "declared_local_relevance_medium_read_only_lookup_performed_question"
    )
    non_claims = _mapping_section(result, "non_claims")
    block = _mapping_section(result, "block")
    failed_count = _failed_check_count(result)
    passed_count = _passed_check_count(result)
    key_non_claims = {
        "lookup_result_created": non_claims.get("lookup_result_created") is False,
        "operation_permission_created": non_claims.get("operation_permission_created") is False,
        "runtime_permission_created": non_claims.get("runtime_permission_created") is False,
        "public_api_created": non_claims.get("public_api_created") is False,
        "participant_facing_interface_created": (
            non_claims.get("participant_facing_interface_created") is False
        ),
        "distributed_network_behavior_created": (
            non_claims.get("distributed_network_behavior_created") is False
        ),
        "follow_on_work_authorized": non_claims.get("follow_on_work_authorized") is False,
        "consumed_request_reopened": non_claims.get("consumed_request_reopened") is False,
        "authorization_token_reused": non_claims.get("authorization_token_reused") is False,
    }
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "lookup_performed_id": performed.get("lookup_performed_id"),
        "question": question.get("local_relevance_medium_read_only_lookup_performed_question"),
        "intent": question.get("local_relevance_medium_read_only_lookup_performed_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "lookup_performed_recorded": statement.get(
            "local_relevance_medium_read_only_lookup_performed_recorded"
        )
        is True,
        "basis_lookup_performed_boundary_artifact_preserved": statement.get(
            "basis_lookup_performed_boundary_artifact_preserved"
        )
        is True,
        "basis_lookup_command_execution_artifact_preserved": statement.get(
            "basis_lookup_command_execution_artifact_preserved"
        )
        is True,
        "selected_command": performed.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved") is True,
        "selected_command_is_state": statement.get("selected_command_is_state") is True,
        "selected_lookup_command_execution_recorded": statement.get(
            "selected_lookup_command_execution_recorded"
        )
        is True,
        "lookup_command_executed": statement.get("lookup_command_executed") is True,
        "lookup_command_execution_local_only": statement.get(
            "lookup_command_execution_local_only"
        )
        is True,
        "lookup_command_execution_read_only": statement.get("lookup_command_execution_read_only")
        is True,
        "lookup_performed": statement.get("lookup_performed") is True,
        "lookup_performed_local_only": statement.get("lookup_performed_local_only") is True,
        "lookup_performed_read_only": statement.get("lookup_performed_read_only") is True,
        "lookup_performed_object_summary": {
            "lookup_performed_type": performed.get("lookup_performed_type"),
            "lookup_performed_scope": performed.get("lookup_performed_scope"),
            "basis_lookup_performed_boundary_artifact": performed.get(
                "basis_lookup_performed_boundary_artifact"
            ),
            "basis_lookup_command_execution_artifact": performed.get(
                "basis_lookup_command_execution_artifact"
            ),
            "selected_command": performed.get("selected_command"),
            "lookup_performed": performed.get("lookup_performed") is True,
            "lookup_result_created": performed.get("lookup_result_created") is True,
        },
        "lookup_result_not_created": non_claims.get("lookup_result_created") is False,
        "operation_permission_not_created": non_claims.get("operation_permission_created")
        is False,
        "runtime_permission_not_created": non_claims.get("runtime_permission_created") is False,
        "public_api_not_created": non_claims.get("public_api_created") is False,
        "participant_facing_interface_not_created": non_claims.get(
            "participant_facing_interface_created"
        )
        is False,
        "distributed_network_behavior_not_created": non_claims.get(
            "distributed_network_behavior_created"
        )
        is False,
        "general_lookup_permission_not_created": non_claims.get(
            "general_lookup_permission_created"
        )
        is False,
        "arbitrary_lookup_permission_not_created": non_claims.get(
            "arbitrary_lookup_permission_created"
        )
        is False,
        "unsupported_commands_not_permitted": non_claims.get("unsupported_commands_permitted")
        is False,
        "unsupported_lookup_keys_not_permitted": non_claims.get(
            "unsupported_lookup_keys_permitted"
        )
        is False,
        "no_new_lookup_entry_created": non_claims.get("new_lookup_entry_created") is False,
        "no_new_signal_entry_relevance_object_index_entry_created": all(
            non_claims.get(key) is False
            for key in (
                "new_signal_accepted",
                "new_entry_accepted",
                "new_relevance_object_created",
                "new_index_entry_created",
            )
        ),
        "filesystem_discovery_not_performed": non_claims.get(
            "filesystem_discovery_performed"
        )
        is False,
        "registry_search_query_ranking_not_created": all(
            non_claims.get(key) is False
            for key in (
                "registry_created",
                "search_surface_created",
                "query_surface_created",
                "ranking_surface_created",
            )
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": all(
            non_claims.get(key) is False
            for key in (
                "scoring_surface_created",
                "priority_surface_created",
                "validity_judgment_created",
                "truth_judgment_created",
                "authority_judgment_created",
                "currentness_judgment_created",
            )
        ),
        "repeated_reception_permission_arbitrary_reception_feed_not_created": all(
            non_claims.get(key) is False
            for key in (
                "repeated_reception_permission_created",
                "arbitrary_reception_created",
                "feed_created",
            )
        ),
        "source_authority_currentness_truth_synchronization_participation_participant_role_not_created": all(
            non_claims.get(key) is False
            for key in (
                "source_created",
                "authority_created",
                "currentness_created",
                "truth_created",
                "synchronization_created",
                "participation_authorized",
                "participant_role_created",
            )
        ),
        "consumed_request_token_remains_closed": statement.get(
            "consumed_request_token_remains_closed"
        )
        is True,
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked")
        is True,
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved"
        )
        is True,
        "follow_on_not_created": non_claims.get("follow_on_work_authorized") is False,
        "key_non_claims": key_non_claims,
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def build_local_relevance_medium_read_only_lookup_performed_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact deterministic summary for a lookup-performed result."""

    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyLookupPerformedV0MinError(
            "result must be a mapping"
        )
    return _build_summary_from_result(result)


def _add_checks(
    *,
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    selected_lookup_performed_boundary_artifact: Path | None,
    boundary_read_code: str | None,
    lookup_performed_boundary_basis: Mapping[str, Any],
    selected_lookup_command_execution_artifact: Path | None,
    command_read_code: str | None,
    lookup_command_execution_basis: Mapping[str, Any],
) -> None:
    question = request.get("local_relevance_medium_read_only_lookup_performed_question")
    intent = request.get("local_relevance_medium_read_only_lookup_performed_intent")
    selected_command = request.get("selected_command")
    lookup_performed_type = request.get("lookup_performed_type")
    lookup_performed_scope = request.get("lookup_performed_scope")
    boundary_object = lookup_performed_boundary_basis.get("boundary_object")
    command_object = lookup_command_execution_basis.get("execution_object")
    if not isinstance(boundary_object, MappingABC):
        boundary_object = {}
    if not isinstance(command_object, MappingABC):
        command_object = {}

    checks.append(
        _check(
            "lookup performed question declared",
            isinstance(question, str) and bool(question.strip()),
            "declared lookup performed question",
            question,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "lookup performed intent supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "lookup performed block not requested",
            intent != INTENT_BLOCK,
            "no explicit lookup performed block request",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BLOCK_REQUESTED",
        )
    )
    checks.append(
        _check(
            "lookup performed boundary artifact path declared",
            selected_lookup_performed_boundary_artifact is not None,
            "declared lookup performed boundary artifact path",
            selected_lookup_performed_boundary_artifact,
            "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _check(
            "lookup performed boundary artifact readable JSON object",
            boundary_read_code is None,
            "readable JSON object",
            boundary_read_code,
            boundary_read_code or "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_UNREADABLE",
        )
    )
    boundary_not_recorded = request.get("lookup_performed_boundary_artifact_not_recorded") is True
    checks.append(
        _check(
            "lookup performed boundary artifact outcome recorded",
            (
                not boundary_not_recorded
                and lookup_performed_boundary_basis.get("outcome")
                == LOOKUP_PERFORMED_BOUNDARY_RECORDED_OUTCOME
            ),
            LOOKUP_PERFORMED_BOUNDARY_RECORDED_OUTCOME,
            lookup_performed_boundary_basis.get("outcome"),
            "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_NOT_RECORDED",
        )
    )
    boundary_version_bad = request.get("lookup_performed_boundary_artifact_version_not_0_1_0") is True
    checks.append(
        _check(
            "lookup performed boundary artifact result version 0.1.0",
            (
                not boundary_version_bad
                and lookup_performed_boundary_basis.get("result_version") == RESULT_VERSION
            ),
            RESULT_VERSION,
            lookup_performed_boundary_basis.get("result_version"),
            "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    boundary_failed = request.get("lookup_performed_boundary_artifact_failed_checks_present") is True
    checks.append(
        _check(
            "lookup performed boundary artifact failed check count zero",
            (
                not boundary_failed
                and lookup_performed_boundary_basis.get("failed_check_count") == 0
            ),
            0,
            lookup_performed_boundary_basis.get("failed_check_count"),
            "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "lookup command execution artifact path declared",
            selected_lookup_command_execution_artifact is not None,
            "declared lookup command execution artifact path",
            selected_lookup_command_execution_artifact,
            "LOOKUP_COMMAND_EXECUTION_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _check(
            "lookup command execution artifact readable JSON object",
            command_read_code is None,
            "readable JSON object",
            command_read_code,
            command_read_code or "LOOKUP_COMMAND_EXECUTION_ARTIFACT_UNREADABLE",
        )
    )
    command_not_recorded = request.get("lookup_command_execution_artifact_not_recorded") is True
    checks.append(
        _check(
            "lookup command execution artifact outcome recorded",
            (
                not command_not_recorded
                and lookup_command_execution_basis.get("outcome")
                == LOOKUP_COMMAND_EXECUTION_RECORDED_OUTCOME
            ),
            LOOKUP_COMMAND_EXECUTION_RECORDED_OUTCOME,
            lookup_command_execution_basis.get("outcome"),
            "LOOKUP_COMMAND_EXECUTION_ARTIFACT_NOT_RECORDED",
        )
    )
    command_version_bad = (
        request.get("lookup_command_execution_artifact_version_not_0_1_0") is True
    )
    checks.append(
        _check(
            "lookup command execution artifact result version 0.1.0",
            (
                not command_version_bad
                and lookup_command_execution_basis.get("result_version") == RESULT_VERSION
            ),
            RESULT_VERSION,
            lookup_command_execution_basis.get("result_version"),
            "LOOKUP_COMMAND_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    command_failed = request.get("lookup_command_execution_artifact_failed_checks_present") is True
    checks.append(
        _check(
            "lookup command execution artifact failed check count zero",
            (
                not command_failed
                and lookup_command_execution_basis.get("failed_check_count") == 0
            ),
            0,
            lookup_command_execution_basis.get("failed_check_count"),
            "LOOKUP_COMMAND_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "selected command declared",
            request.get("selected_command_missing") is not True and selected_command is not None,
            "state",
            selected_command,
            "SELECTED_COMMAND_MISSING",
        )
    )
    selected_command_is_state = (
        request.get("selected_command_not_state") is not True and selected_command == SELECTED_COMMAND
    )
    checks.append(
        _check(
            "selected command exactly state",
            selected_command_is_state,
            SELECTED_COMMAND,
            selected_command,
            "SELECTED_COMMAND_NOT_STATE",
        )
    )
    checks.append(
        _check(
            "selected command is state",
            (
                selected_command_is_state
                and lookup_command_execution_basis.get("selected_command") == SELECTED_COMMAND
                and lookup_command_execution_basis.get("selected_command_is_state") is True
            ),
            "selected command state in request and lookup command execution basis",
            {
                "request_selected_command": selected_command,
                "basis_selected_command": lookup_command_execution_basis.get("selected_command"),
                "basis_selected_command_is_state": lookup_command_execution_basis.get(
                    "selected_command_is_state"
                ),
            },
            "SELECTED_COMMAND_NOT_STATE",
        )
    )
    checks.append(
        _check(
            "selected lookup command execution recorded",
            (
                request.get("selected_lookup_command_execution_not_recorded") is not True
                and lookup_command_execution_basis.get("selected_lookup_command_execution_recorded")
                is True
            ),
            True,
            lookup_command_execution_basis.get("selected_lookup_command_execution_recorded"),
            "SELECTED_LOOKUP_COMMAND_EXECUTION_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "lookup command executed",
            (
                request.get("lookup_command_not_executed") is not True
                and lookup_command_execution_basis.get("lookup_command_executed") is True
            ),
            True,
            lookup_command_execution_basis.get("lookup_command_executed"),
            "LOOKUP_COMMAND_NOT_EXECUTED",
        )
    )
    checks.append(
        _check(
            "lookup command execution local only",
            (
                request.get("lookup_command_execution_local_only_not_true") is not True
                and lookup_command_execution_basis.get("lookup_command_execution_local_only") is True
            ),
            True,
            lookup_command_execution_basis.get("lookup_command_execution_local_only"),
            "LOOKUP_COMMAND_EXECUTION_LOCAL_ONLY_NOT_TRUE",
        )
    )
    checks.append(
        _check(
            "lookup command execution read only",
            (
                request.get("lookup_command_execution_read_only_not_true") is not True
                and lookup_command_execution_basis.get("lookup_command_execution_read_only") is True
            ),
            True,
            lookup_command_execution_basis.get("lookup_command_execution_read_only"),
            "LOOKUP_COMMAND_EXECUTION_READ_ONLY_NOT_TRUE",
        )
    )
    checks.append(
        _check(
            "lookup performed type declared",
            lookup_performed_type is not None,
            LOOKUP_PERFORMED_TYPE,
            lookup_performed_type,
            "LOOKUP_PERFORMED_TYPE_MISSING",
        )
    )
    checks.append(
        _check(
            "lookup performed type exact",
            (
                request.get(
                    "lookup_performed_type_not_local_relevance_medium_read_only_lookup_performed"
                )
                is not True
                and lookup_performed_type == LOOKUP_PERFORMED_TYPE
            ),
            LOOKUP_PERFORMED_TYPE,
            lookup_performed_type,
            "LOOKUP_PERFORMED_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED",
        )
    )
    checks.append(
        _check(
            "lookup performed scope declared",
            lookup_performed_scope is not None,
            LOOKUP_PERFORMED_SCOPE,
            lookup_performed_scope,
            "LOOKUP_PERFORMED_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "lookup performed scope selected lookup performed only",
            (
                request.get("lookup_performed_scope_not_selected_lookup_performed_only") is not True
                and lookup_performed_scope == LOOKUP_PERFORMED_SCOPE
            ),
            LOOKUP_PERFORMED_SCOPE,
            lookup_performed_scope,
            "LOOKUP_PERFORMED_SCOPE_NOT_SELECTED_LOOKUP_PERFORMED_ONLY",
        )
    )
    checks.append(
        _check(
            "local relevance medium read-only lookup performed recorded",
            request.get("local_relevance_medium_read_only_lookup_performed_not_recorded")
            is not True,
            True,
            request.get("local_relevance_medium_read_only_lookup_performed_not_recorded") is not True,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "lookup performed true",
            request.get("lookup_not_performed") is not True,
            True,
            request.get("lookup_not_performed") is not True,
            "LOOKUP_NOT_PERFORMED",
        )
    )
    checks.append(
        _check(
            "lookup performed local only",
            request.get("lookup_performed_local_only_not_true") is not True,
            True,
            request.get("lookup_performed_local_only_not_true") is not True,
            "LOOKUP_PERFORMED_LOCAL_ONLY_NOT_TRUE",
        )
    )
    checks.append(
        _check(
            "lookup performed read only",
            request.get("lookup_performed_read_only_not_true") is not True,
            True,
            request.get("lookup_performed_read_only_not_true") is not True,
            "LOOKUP_PERFORMED_READ_ONLY_NOT_TRUE",
        )
    )
    checks.append(
        _check(
            "consumed request not reopened",
            request.get("consumed_request_reopened") is not True,
            False,
            request.get("consumed_request_reopened") is True,
            "CONSUMED_REQUEST_REOPENED",
        )
    )
    checks.append(
        _check(
            "authorization token not reused",
            request.get("authorization_token_reused") is not True,
            False,
            request.get("authorization_token_reused") is True,
            "AUTHORIZATION_TOKEN_REUSED",
        )
    )

    for field in REQUIRED_FALSE_NON_CLAIMS:
        actual = _false_field_actual(request, field, boundary_object, command_object)
        checks.append(
            _check(
                f"required false posture preserved: {field}",
                actual is False,
                False,
                actual,
                FALSE_FIELD_BLOCK_CODES[field],
            )
        )

    predecessor_repaired_or_hidden = any(
        request.get(field) is True
        for field in (
            "prior_artifacts_mutated",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
    )
    checks.append(
        _check(
            "predecessor failure evidence preserved",
            not predecessor_repaired_or_hidden,
            "preserved failed-lineage evidence only",
            predecessor_repaired_or_hidden,
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    )
    emitted_non_claims = _canonical_false_non_claims()
    checks.append(
        _check(
            "result-level required false non-claims canonical false",
            all(emitted_non_claims[key] is False for key in REQUIRED_FALSE_NON_CLAIMS),
            "all result-level required false non-claims are false",
            emitted_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    checks.append(
        _check(
            "declared required non-claims false",
            _required_non_claims_false(request),
            "declared required non-claims are present and false",
            _declared_non_claims(request),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )


def _resolve_from_mapping(request: Mapping[str, Any]) -> dict[str, Any]:
    request_copy = copy.deepcopy(dict(request))
    lookup_performed_id = str(
        request_copy.get(
            "local_relevance_medium_read_only_lookup_performed_id",
            DEFAULT_LOOKUP_PERFORMED_ID,
        )
        or DEFAULT_LOOKUP_PERFORMED_ID
    )
    selected_boundary_path = None
    if request_copy.get("lookup_performed_boundary_artifact_missing") is not True:
        selected_boundary_path = _as_path(
            request_copy.get("selected_lookup_performed_boundary_artifact")
        )
    selected_command_path = None
    if request_copy.get("lookup_command_execution_artifact_missing") is not True:
        selected_command_path = _as_path(
            request_copy.get("selected_lookup_command_execution_artifact")
        )

    boundary_artifact: dict[str, Any] | None = None
    boundary_read_code: str | None = "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_PATH_MISSING"
    if selected_boundary_path is not None:
        boundary_artifact, boundary_read_code = _read_json_object(
            selected_boundary_path,
            "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_UNREADABLE",
            "LOOKUP_PERFORMED_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
        )
    command_artifact: dict[str, Any] | None = None
    command_read_code: str | None = "LOOKUP_COMMAND_EXECUTION_ARTIFACT_PATH_MISSING"
    if selected_command_path is not None:
        command_artifact, command_read_code = _read_json_object(
            selected_command_path,
            "LOOKUP_COMMAND_EXECUTION_ARTIFACT_UNREADABLE",
            "LOOKUP_COMMAND_EXECUTION_ARTIFACT_NOT_JSON_OBJECT",
        )

    boundary_basis = _extract_lookup_performed_boundary_basis(boundary_artifact)
    command_basis = _extract_lookup_command_execution_basis(command_artifact)
    checks: list[dict[str, Any]] = []
    _add_checks(
        request=request_copy,
        checks=checks,
        selected_lookup_performed_boundary_artifact=selected_boundary_path,
        boundary_read_code=boundary_read_code,
        lookup_performed_boundary_basis=boundary_basis,
        selected_lookup_command_execution_artifact=selected_command_path,
        command_read_code=command_read_code,
        lookup_command_execution_basis=command_basis,
    )

    failure_code = _first_failure_code(checks)
    if failure_code is not None:
        outcome = OUTCOME_BLOCKED
    elif request_copy.get("requested_local_relevance_medium_read_only_lookup_performed_outcome") == (
        OUTCOME_REQUIRES_ADDITIONAL_BASIS
    ) or bool(request_copy.get("additional_basis_context")):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif request_copy.get("local_relevance_medium_read_only_lookup_performed_intent") == (
        INTENT_DO_NOT_RECORD
    ):
        outcome = OUTCOME_NOT_RECORDED
    else:
        outcome = OUTCOME_RECORDED

    recorded = outcome == OUTCOME_RECORDED
    selected_command = request_copy.get("selected_command")
    performed = _build_lookup_performed_object(
        lookup_performed_id=lookup_performed_id,
        recorded=recorded,
        selected_lookup_performed_boundary_artifact=selected_boundary_path,
        lookup_performed_boundary_basis=boundary_basis,
        selected_lookup_command_execution_artifact=selected_command_path,
        lookup_command_execution_basis=command_basis,
        selected_command=selected_command,
    )
    statement = _build_statement(
        recorded=recorded,
        lookup_performed_boundary_artifact_preserved=selected_boundary_path is not None
        and boundary_read_code is None,
        lookup_command_execution_artifact_preserved=selected_command_path is not None
        and command_read_code is None,
        selected_command=selected_command,
        lookup_command_execution_basis=command_basis,
    )
    block = _block_record(failure_code, request_copy.get("block_reason"))
    metadata = {
        "local_relevance_medium_read_only_lookup_performed_id": lookup_performed_id,
        "local_relevance_medium_read_only_lookup_performed_type": LOOKUP_PERFORMED_TYPE,
        "local_relevance_medium_read_only_lookup_performed_version": RESULT_VERSION,
        "generated_at": _utc_timestamp(),
        "resolver_module": RESOLVER_MODULE,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_lookup_performed_metadata": metadata,
        "declared_local_relevance_medium_read_only_lookup_performed_question": (
            _build_declared_question_section(request_copy)
        ),
        "selected_lookup_performed_boundary_artifact_basis": _build_boundary_basis_section(
            selected_boundary_path,
            boundary_basis,
            selected_boundary_path is not None and boundary_read_code is None,
        ),
        "selected_lookup_command_execution_artifact_basis": (
            _build_command_execution_basis_section(
                selected_command_path,
                command_basis,
                selected_command_path is not None and command_read_code is None,
            )
        ),
        "local_relevance_medium_read_only_lookup_performed": performed,
        "local_relevance_medium_read_only_lookup_performed_checks": checks,
        "local_relevance_medium_read_only_lookup_performed_statement": statement,
        "local_relevance_medium_read_only_lookup_performed_non_meaning": _build_non_meaning(),
        "additional_basis_required": (
            _sanitize(request_copy.get("additional_basis_context"))
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else None
        ),
        "not_recorded_basis": (
            _sanitize(
                request_copy.get(
                    "not_recorded_basis",
                    "lookup performed not recorded by request",
                )
            )
            if outcome == OUTCOME_NOT_RECORDED
            else None
        ),
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["local_relevance_medium_read_only_lookup_performed_summary"] = (
        _build_summary_from_result(result)
    )
    return result


def _blocked_malformed_result(code: str, reason: str) -> dict[str, Any]:
    checks = [
        _check(
            "declared local relevance medium read-only lookup performed request mapping",
            False,
            "mapping request",
            reason,
            code,
        )
    ]
    performed = _build_lookup_performed_object(
        lookup_performed_id=DEFAULT_LOOKUP_PERFORMED_ID,
        recorded=False,
        selected_lookup_performed_boundary_artifact=None,
        lookup_performed_boundary_basis={},
        selected_lookup_command_execution_artifact=None,
        lookup_command_execution_basis={},
        selected_command=None,
    )
    statement = _build_statement(
        recorded=False,
        lookup_performed_boundary_artifact_preserved=False,
        lookup_command_execution_artifact_preserved=False,
        selected_command=None,
        lookup_command_execution_basis={},
    )
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_lookup_performed_metadata": {
            "local_relevance_medium_read_only_lookup_performed_id": DEFAULT_LOOKUP_PERFORMED_ID,
            "local_relevance_medium_read_only_lookup_performed_type": LOOKUP_PERFORMED_TYPE,
            "local_relevance_medium_read_only_lookup_performed_version": RESULT_VERSION,
            "generated_at": _utc_timestamp(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_local_relevance_medium_read_only_lookup_performed_question": {},
        "selected_lookup_performed_boundary_artifact_basis": _build_boundary_basis_section(
            None, {}, False
        ),
        "selected_lookup_command_execution_artifact_basis": _build_command_execution_basis_section(
            None, {}, False
        ),
        "local_relevance_medium_read_only_lookup_performed": performed,
        "local_relevance_medium_read_only_lookup_performed_checks": checks,
        "local_relevance_medium_read_only_lookup_performed_statement": statement,
        "local_relevance_medium_read_only_lookup_performed_non_meaning": _build_non_meaning(),
        "additional_basis_required": None,
        "not_recorded_basis": None,
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_false_non_claims(),
        "outcome": OUTCOME_BLOCKED,
        "block": _block_record(code, reason),
    }
    result["local_relevance_medium_read_only_lookup_performed_summary"] = (
        _build_summary_from_result(result)
    )
    return result


def resolve_local_relevance_medium_read_only_lookup_performed_v0_min(
    declared_local_relevance_medium_read_only_lookup_performed: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one selected-state local read-only lookup performed request."""

    if declared_local_relevance_medium_read_only_lookup_performed is None:
        declared_local_relevance_medium_read_only_lookup_performed = (
            build_declared_local_relevance_medium_read_only_lookup_performed_v0_min_request()
        )
    if not isinstance(declared_local_relevance_medium_read_only_lookup_performed, MappingABC):
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_REQUEST_MALFORMED",
            "declared request is not a mapping",
        )
    return _resolve_from_mapping(declared_local_relevance_medium_read_only_lookup_performed)


def resolve_local_relevance_medium_read_only_lookup_performed_v0_min_from_path(
    declared_local_relevance_medium_read_only_lookup_performed_path: Path | str,
) -> dict[str, Any]:
    """Read a declared lookup-performed request JSON file and resolve it."""

    try:
        parsed = json.loads(
            Path(declared_local_relevance_medium_read_only_lookup_performed_path).read_text(
                encoding="utf-8"
            )
        )
    except (OSError, json.JSONDecodeError) as exc:
        raise LocalRelevanceMediumReadOnlyLookupPerformedV0MinError(
            "declared lookup performed request path is unreadable"
        ) from exc
    if not isinstance(parsed, MappingABC):
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_REQUEST_MALFORMED",
            "declared request JSON is not an object",
        )
    return resolve_local_relevance_medium_read_only_lookup_performed_v0_min(parsed)


def _result_lookup_performed_id(result: Mapping[str, Any]) -> str:
    performed = _mapping_section(result, "local_relevance_medium_read_only_lookup_performed")
    metadata = _mapping_section(result, "local_relevance_medium_read_only_lookup_performed_metadata")
    value = _first_present(
        performed.get("lookup_performed_id"),
        metadata.get("local_relevance_medium_read_only_lookup_performed_id"),
        DEFAULT_LOOKUP_PERFORMED_ID,
    )
    return str(value)


def _unique_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def write_local_relevance_medium_read_only_lookup_performed_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a lookup-performed resolver result without silently overwriting."""

    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyLookupPerformedV0MinError(
            "result must be a mapping"
        )
    filename = (
        f"{_result_lookup_performed_id(result)}__"
        "local_relevance_medium_read_only_lookup_performed_v0_min_result.json"
    )
    if output_path is None:
        target = OUTPUT_ROOT / filename
    else:
        requested = Path(output_path)
        target = requested if requested.suffix.lower() == ".json" else requested / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _unique_output_path(target)
    target.write_text(
        json.dumps(_sanitize(dict(result)), ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )
    return target


def build_declared_local_relevance_medium_read_only_lookup_performed_v0_min_request(
    *,
    local_relevance_medium_read_only_lookup_performed_id: str = DEFAULT_LOOKUP_PERFORMED_ID,
    selected_lookup_performed_boundary_artifact: Path | str = (
        DEFAULT_LOOKUP_PERFORMED_BOUNDARY_ARTIFACT
    ),
    selected_lookup_command_execution_artifact: Path | str = (
        DEFAULT_LOOKUP_COMMAND_EXECUTION_ARTIFACT
    ),
    selected_command: str = SELECTED_COMMAND,
    lookup_performed_type: str = LOOKUP_PERFORMED_TYPE,
    lookup_performed_scope: str = LOOKUP_PERFORMED_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared request for one selected-state lookup performed event."""

    override_selected_command = overrides.get("selected_command", selected_command)
    if override_selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyLookupPerformedV0MinError(
            "selected command must be exactly state"
        )
    non_claims = _canonical_false_non_claims()
    if declared_non_claims is not None:
        non_claims.update(dict(declared_non_claims))
    request: dict[str, Any] = {
        "local_relevance_medium_read_only_lookup_performed_id": (
            local_relevance_medium_read_only_lookup_performed_id
        ),
        "local_relevance_medium_read_only_lookup_performed_question": CORE_QUESTION,
        "local_relevance_medium_read_only_lookup_performed_intent": intent,
        "selected_lookup_performed_boundary_artifact": str(
            selected_lookup_performed_boundary_artifact
        ),
        "selected_lookup_command_execution_artifact": str(
            selected_lookup_command_execution_artifact
        ),
        "selected_command": SELECTED_COMMAND,
        "lookup_performed_type": lookup_performed_type,
        "lookup_performed_scope": lookup_performed_scope,
        "declared_non_claims": non_claims,
    }
    request.update(overrides)
    request["selected_command"] = SELECTED_COMMAND
    return request
