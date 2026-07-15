"""Resolve one local read-only selected-state result object.

This resolver reads one clean state-result-object boundary artifact and one
clean selected-state payload-return artifact. It records one bounded local
read-only state result object for selected command ``state`` only.

It is not packet-body exposure, raw/full packet-body exposure, lookup,
operation permission, runtime permission, public API, participant-facing
interface, distributed behavior, registry, search, query surface, ranking, or
follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyStateResultObjectV0MinError(Exception):
    """Bounded resolver error for malformed file operations."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_state_result_object_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

STATE_RESULT_OBJECT_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT"
STATE_RESULT_OBJECT_SCOPE = "SELECTED_STATE_RESULT_OBJECT_ONLY"
STATE_RESULT_OBJECT_BOUNDARY_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_RECORDED"
)
STATE_PAYLOAD_RETURN_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_RECORDED"
)

SUPPORTED_STATE_RESULT_OBJECT_TYPE_VALUES = (STATE_RESULT_OBJECT_TYPE,)
SUPPORTED_STATE_RESULT_OBJECT_SCOPE_VALUES = (STATE_RESULT_OBJECT_SCOPE,)

SELECTED_COMMAND = "state"
DEFAULT_STATE_RESULT_OBJECT_ID = "local_relevance_medium_read_only_state_result_object_001"

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_result_object_v0_min"
)
DEFAULT_STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_result_object_boundary_v0_min/"
    "local_relevance_medium_read_only_state_result_object_boundary_reference_review_001__"
    "local_relevance_medium_read_only_state_result_object_boundary_v0_min_result.json"
)
DEFAULT_STATE_PAYLOAD_RETURN_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_payload_return_v0_min/"
    "local_relevance_medium_read_only_state_payload_return_reference_review_001__"
    "local_relevance_medium_read_only_state_payload_return_v0_min_result.json"
)

STATE_RESULT_OBJECT_FALSE_FIELDS = (
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
    "artifact_existence_treated_as_state_result_object_authority",
    "latest_file_posture_treated_as_state_result_object_authority",
    "repo_local_availability_treated_as_state_result_object_authority",
    "hidden_repo_state_used_as_state_result_object_content",
    "hidden_repo_state_used_as_state_result_object_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

REQUIRED_FALSE_NON_CLAIMS = STATE_RESULT_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_state_result_object_recorded",
    "basis_state_result_object_boundary_artifact_preserved",
    "basis_state_payload_return_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_state_payload_return_recorded",
    "state_payload_returned",
    "state_payload_return_local_only",
    "state_payload_return_read_only",
    "state_result_object_created",
    "state_result_object_local_only",
    "state_result_object_read_only",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BLOCK_REQUESTED",
    "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_PATH_MISSING",
    "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_UNREADABLE",
    "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
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
    "STATE_RESULT_OBJECT_TYPE_MISSING",
    "STATE_RESULT_OBJECT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT",
    "STATE_RESULT_OBJECT_SCOPE_MISSING",
    "STATE_RESULT_OBJECT_SCOPE_NOT_SELECTED_STATE_RESULT_OBJECT_ONLY",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_NOT_RECORDED",
    "STATE_RESULT_OBJECT_NOT_CREATED",
    "STATE_RESULT_OBJECT_LOCAL_ONLY_NOT_TRUE",
    "STATE_RESULT_OBJECT_READ_ONLY_NOT_TRUE",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_STATE_RESULT_OBJECT_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_STATE_RESULT_OBJECT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_STATE_RESULT_OBJECT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_STATE_RESULT_OBJECT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_STATE_RESULT_OBJECT_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_REQUEST_UNREADABLE",
)

FALSE_FIELD_BLOCK_CODES = {
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
    "artifact_existence_treated_as_state_result_object_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_STATE_RESULT_OBJECT_AUTHORITY"
    ),
    "latest_file_posture_treated_as_state_result_object_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_STATE_RESULT_OBJECT_AUTHORITY"
    ),
    "repo_local_availability_treated_as_state_result_object_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_STATE_RESULT_OBJECT_AUTHORITY"
    ),
    "hidden_repo_state_used_as_state_result_object_content": (
        "HIDDEN_REPO_STATE_USED_AS_STATE_RESULT_OBJECT_CONTENT"
    ),
    "hidden_repo_state_used_as_state_result_object_authority": (
        "HIDDEN_REPO_STATE_USED_AS_STATE_RESULT_OBJECT_AUTHORITY"
    ),
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
}

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_state_result_object_body",
    "raw_state_result_body",
    "raw_state_packet_body",
    "raw_full_state_packet_body",
    "raw_state_result_object_boundary_body",
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
    "state_result_object_body",
    "state_result_body",
    "state_packet_body",
    "full_state_packet_body",
    "state_result_object_boundary_body",
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

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_OBJECT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_OBJECT_BOUNDARY_BODY_MUST_NOT_RETURN",
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

WHAT_REMAINS_OPEN = (
    "local_relevance_medium_read_only_state_result_object_terminal_summary_if_selected",
    "state_packet_body_exposure",
    "raw_full_state_packet_body_exposure",
    "lookup_command_execution",
    "lookup_performed",
    "operation_permission",
    "runtime_permission",
    "public_api",
    "participant_facing_interface",
    "distributed_network_behavior",
    "general_lookup_permission",
    "arbitrary_lookup_permission",
    "unsupported_command_permission",
    "unsupported_key_permission",
    "registry",
    "search_surface",
    "query_surface",
    "ranking_surface",
    "source_transfer",
    "source_receipt",
    "authority_creation",
    "currentness_creation",
    "truth_creation",
    "synchronization",
    "participation_authorization",
    "participant_role",
    "deployment",
    "public_release",
    "follow_on_work",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _is_sensitive_key(key: str) -> bool:
    return key in SENSITIVE_CONTENT_KEYS or key.endswith("_body")


def _sanitize_value(value: Any, key: str | None = None) -> Any:
    if key is not None and _is_sensitive_key(key):
        return "[REDACTED_SENSITIVE_CONTENT]"
    if isinstance(value, str):
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return "[REDACTED_SENSITIVE_CONTENT]"
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {str(k): _sanitize_value(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize_value(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize_value(item) for item in value]
    return value


def _safe_mapping_copy(value: Mapping[str, Any]) -> dict[str, Any]:
    return _sanitize_value(copy.deepcopy(dict(value)))


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _as_path(value: Any) -> Path | None:
    if isinstance(value, Path):
        return value
    if isinstance(value, str) and value:
        return Path(value)
    return None


def _read_json_object(
    path_value: Any,
    unreadable_code: str,
    not_object_code: str,
) -> tuple[dict[str, Any] | None, str | None]:
    path = _as_path(path_value)
    if path is None:
        return None, unreadable_code
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None, unreadable_code
    if not isinstance(data, dict):
        return None, not_object_code
    return _sanitize_value(data), None


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize_value(expected_posture),
        "actual_posture": _sanitize_value(actual_posture),
    }
    if not passed and code:
        record["block_code"] = code
        record["failure_code"] = code
    checks.append(record)


def _first_failed_code(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _block(code: str | None, reason: str | None = None) -> dict[str, Any]:
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
        "reason": reason or code,
    }


def _failed_check_count(checks: list[dict[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is False)


def _passed_check_count(checks: list[dict[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is True)


def _count_failed_checks(artifact: Mapping[str, Any], key: str) -> int | None:
    checks = artifact.get(key)
    if isinstance(checks, list):
        return sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is False)
    return None


def _boundary_object(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_result_object_boundary")
    return dict(value) if isinstance(value, Mapping) else {}


def _boundary_statement(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_result_object_boundary_statement")
    return dict(value) if isinstance(value, Mapping) else {}


def _boundary_summary(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_result_object_boundary_summary")
    return dict(value) if isinstance(value, Mapping) else {}


def _boundary_metadata(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_result_object_boundary_metadata")
    return dict(value) if isinstance(value, Mapping) else {}


def _payload_return_object(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_payload_return")
    return dict(value) if isinstance(value, Mapping) else {}


def _payload_return_statement(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_payload_return_statement")
    return dict(value) if isinstance(value, Mapping) else {}


def _payload_return_summary(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_payload_return_summary")
    return dict(value) if isinstance(value, Mapping) else {}


def _payload_return_metadata(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_payload_return_metadata")
    return dict(value) if isinstance(value, Mapping) else {}


def _artifact_failed_count(
    artifact: Mapping[str, Any] | None,
    summary: Mapping[str, Any],
    checks_key: str,
) -> int | None:
    if artifact is None:
        return None
    value = _first_present(summary.get("failed_check_count"), artifact.get("failed_check_count"))
    if isinstance(value, int):
        return value
    return _count_failed_checks(artifact, checks_key)


def _artifact_bool(
    primary: Mapping[str, Any],
    statement: Mapping[str, Any],
    key: str,
) -> bool | None:
    value = _first_present(primary.get(key), statement.get(key))
    return value if isinstance(value, bool) else None


def _field_is_true_in_any(field: str, *mappings: Mapping[str, Any]) -> bool:
    return any(mapping.get(field) is True for mapping in mappings)


def _declared_non_claims_are_false(request: Mapping[str, Any]) -> bool:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        return False
    return all(declared.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _build_metadata(state_result_object_id: str) -> dict[str, Any]:
    return {
        "local_relevance_medium_read_only_state_result_object_id": state_result_object_id,
        "local_relevance_medium_read_only_state_result_object_type": STATE_RESULT_OBJECT_TYPE,
        "local_relevance_medium_read_only_state_result_object_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _build_state_result_object(
    request: Mapping[str, Any],
    boundary_artifact: Mapping[str, Any],
    payload_artifact: Mapping[str, Any],
    boundary_path: Path,
    payload_path: Path,
) -> dict[str, Any]:
    boundary = _boundary_object(boundary_artifact)
    boundary_summary = _boundary_summary(boundary_artifact)
    boundary_metadata = _boundary_metadata(boundary_artifact)
    payload = _payload_return_object(payload_artifact)
    payload_summary = _payload_return_summary(payload_artifact)
    payload_metadata = _payload_return_metadata(payload_artifact)

    boundary_outcome = _first_present(boundary_artifact.get("outcome"), boundary_summary.get("outcome"))
    boundary_version = _first_present(
        boundary_summary.get("result_version"),
        boundary_artifact.get("result_version"),
        boundary_metadata.get("local_relevance_medium_read_only_state_result_object_boundary_version"),
        boundary_metadata.get("result_version"),
        boundary.get("boundary_version"),
    )
    boundary_failed_count = _artifact_failed_count(
        boundary_artifact,
        boundary_summary,
        "local_relevance_medium_read_only_state_result_object_boundary_checks",
    )
    payload_outcome = _first_present(payload_artifact.get("outcome"), payload_summary.get("outcome"))
    payload_version = _first_present(
        payload_summary.get("result_version"),
        payload_artifact.get("result_version"),
        payload_metadata.get("local_relevance_medium_read_only_state_payload_return_version"),
        payload_metadata.get("result_version"),
        payload.get("state_payload_return_version"),
    )
    payload_failed_count = _artifact_failed_count(
        payload_artifact,
        payload_summary,
        "local_relevance_medium_read_only_state_payload_return_checks",
    )

    state_result_object: dict[str, Any] = {
        "state_result_object_id": str(
            request.get("local_relevance_medium_read_only_state_result_object_id")
            or DEFAULT_STATE_RESULT_OBJECT_ID
        ),
        "state_result_object_type": STATE_RESULT_OBJECT_TYPE,
        "state_result_object_version": RESULT_VERSION,
        "state_result_object_scope": STATE_RESULT_OBJECT_SCOPE,
        "basis_state_result_object_boundary_artifact": str(boundary_path),
        "basis_state_result_object_boundary_outcome": boundary_outcome,
        "basis_state_result_object_boundary_result_version": boundary_version,
        "basis_state_result_object_boundary_failed_check_count": boundary_failed_count,
        "basis_state_payload_return_artifact": str(payload_path),
        "basis_state_payload_return_outcome": payload_outcome,
        "basis_state_payload_return_result_version": payload_version,
        "basis_state_payload_return_failed_check_count": payload_failed_count,
        "selected_command": SELECTED_COMMAND,
        "selected_command_is_state": True,
        "selected_state_payload_return_recorded": True,
        "state_payload_returned": True,
        "state_payload_return_local_only": True,
        "state_payload_return_read_only": True,
        "local_relevance_medium_read_only_state_result_object_recorded": True,
        "state_result_object_created": True,
        "state_result_object_local_only": True,
        "state_result_object_read_only": True,
    }
    for field in STATE_RESULT_OBJECT_FALSE_FIELDS:
        state_result_object[field] = False
    return state_result_object


def _build_statement(recorded: bool) -> dict[str, bool]:
    return {
        "local_relevance_medium_read_only_state_result_object_recorded": recorded,
        "basis_state_result_object_boundary_artifact_preserved": recorded,
        "basis_state_payload_return_artifact_preserved": recorded,
        "selected_command_preserved": recorded,
        "selected_command_is_state": recorded,
        "selected_state_payload_return_recorded": recorded,
        "state_payload_returned": recorded,
        "state_payload_return_local_only": recorded,
        "state_payload_return_read_only": recorded,
        "state_result_object_created": recorded,
        "state_result_object_local_only": recorded,
        "state_result_object_read_only": recorded,
        "state_packet_body_not_exposed": True,
        "raw_full_state_packet_body_not_exposed": True,
        "lookup_not_performed": True,
        "lookup_command_not_executed": True,
        "operation_permission_not_created": True,
        "runtime_permission_not_created": True,
        "public_api_not_created": True,
        "participant_facing_interface_not_created": True,
        "distributed_network_behavior_not_created": True,
        "general_lookup_permission_not_created": True,
        "arbitrary_lookup_permission_not_created": True,
        "unsupported_commands_not_permitted": True,
        "unsupported_lookup_keys_not_permitted": True,
        "new_lookup_result_not_created": True,
        "new_lookup_entry_not_created": True,
        "predecessor_failure_evidence_preserved": True,
        "predecessor_failure_repaired": False,
        "predecessor_failure_hidden": False,
        "predecessor_failure_claimed_passed": False,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "not_state_packet_body_exposure": True,
        "not_raw_full_state_packet_body_exposure": True,
        "not_lookup": True,
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


def _build_boundary_basis(
    boundary_artifact: Mapping[str, Any] | None,
    boundary_path: Path | None,
) -> dict[str, Any]:
    if boundary_artifact is None:
        return {
            "selected_state_result_object_boundary_artifact": str(boundary_path) if boundary_path else None,
            "basis_artifact_read": False,
        }
    boundary = _boundary_object(boundary_artifact)
    summary = _boundary_summary(boundary_artifact)
    metadata = _boundary_metadata(boundary_artifact)
    return {
        "selected_state_result_object_boundary_artifact": str(boundary_path) if boundary_path else None,
        "basis_artifact_read": True,
        "basis_artifact_preserved": True,
        "outcome": _first_present(boundary_artifact.get("outcome"), summary.get("outcome")),
        "result_version": _first_present(
            summary.get("result_version"),
            boundary_artifact.get("result_version"),
            metadata.get("local_relevance_medium_read_only_state_result_object_boundary_version"),
            metadata.get("result_version"),
            boundary.get("boundary_version"),
        ),
        "failed_check_count": _artifact_failed_count(
            boundary_artifact,
            summary,
            "local_relevance_medium_read_only_state_result_object_boundary_checks",
        ),
        "selected_command": boundary.get("selected_command"),
        "selected_command_is_state": boundary.get("selected_command_is_state"),
        "future_state_result_object_may_be_considered": boundary.get(
            "future_state_result_object_may_be_considered"
        ),
    }


def _build_payload_basis(
    payload_artifact: Mapping[str, Any] | None,
    payload_path: Path | None,
) -> dict[str, Any]:
    if payload_artifact is None:
        return {
            "selected_state_payload_return_artifact": str(payload_path) if payload_path else None,
            "basis_artifact_read": False,
        }
    payload = _payload_return_object(payload_artifact)
    summary = _payload_return_summary(payload_artifact)
    metadata = _payload_return_metadata(payload_artifact)
    return {
        "selected_state_payload_return_artifact": str(payload_path) if payload_path else None,
        "basis_artifact_read": True,
        "basis_artifact_preserved": True,
        "outcome": _first_present(payload_artifact.get("outcome"), summary.get("outcome")),
        "result_version": _first_present(
            summary.get("result_version"),
            payload_artifact.get("result_version"),
            metadata.get("local_relevance_medium_read_only_state_payload_return_version"),
            metadata.get("result_version"),
            payload.get("state_payload_return_version"),
        ),
        "failed_check_count": _artifact_failed_count(
            payload_artifact,
            summary,
            "local_relevance_medium_read_only_state_payload_return_checks",
        ),
        "selected_command": payload.get("selected_command"),
        "selected_command_is_state": payload.get("selected_command_is_state"),
        "selected_state_payload_return_recorded": payload.get(
            "selected_state_payload_return_recorded"
        ),
        "state_payload_returned": payload.get("state_payload_returned"),
        "state_payload_return_local_only": payload.get("state_payload_return_local_only"),
        "state_payload_return_read_only": payload.get("state_payload_return_read_only"),
    }


def _build_declared_question_section(request: Mapping[str, Any] | None) -> dict[str, Any]:
    if request is None:
        return {
            "local_relevance_medium_read_only_state_result_object_question": None,
            "local_relevance_medium_read_only_state_result_object_intent": None,
            "selected_command": None,
            "state_result_object_type": None,
            "state_result_object_scope": None,
        }
    return {
        "local_relevance_medium_read_only_state_result_object_id": request.get(
            "local_relevance_medium_read_only_state_result_object_id"
        ),
        "local_relevance_medium_read_only_state_result_object_question": request.get(
            "local_relevance_medium_read_only_state_result_object_question"
        ),
        "local_relevance_medium_read_only_state_result_object_intent": request.get(
            "local_relevance_medium_read_only_state_result_object_intent"
        ),
        "selected_state_result_object_boundary_artifact": str(
            request.get("selected_state_result_object_boundary_artifact")
        )
        if request.get("selected_state_result_object_boundary_artifact") is not None
        else None,
        "selected_state_payload_return_artifact": str(
            request.get("selected_state_payload_return_artifact")
        )
        if request.get("selected_state_payload_return_artifact") is not None
        else None,
        "selected_command": request.get("selected_command"),
        "state_result_object_type": request.get("state_result_object_type"),
        "state_result_object_scope": request.get("state_result_object_scope"),
    }


def build_local_relevance_medium_read_only_state_result_object_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary for a resolver result."""

    checks = result.get("local_relevance_medium_read_only_state_result_object_checks")
    checks_list = checks if isinstance(checks, list) else []
    state_result_object = result.get("local_relevance_medium_read_only_state_result_object")
    object_map = state_result_object if isinstance(state_result_object, Mapping) else {}
    statement = result.get("local_relevance_medium_read_only_state_result_object_statement")
    statement_map = statement if isinstance(statement, Mapping) else {}
    metadata = result.get("local_relevance_medium_read_only_state_result_object_metadata")
    metadata_map = metadata if isinstance(metadata, Mapping) else {}
    question = result.get("declared_local_relevance_medium_read_only_state_result_object_question")
    question_map = question if isinstance(question, Mapping) else {}
    block = result.get("block")
    block_map = block if isinstance(block, Mapping) else {}
    non_claims = result.get("non_claims")
    non_claims_map = non_claims if isinstance(non_claims, Mapping) else {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block_map.get("block_code") or block_map.get("code"),
        "block_reason": block_map.get("reason"),
        "state_result_object_id": object_map.get("state_result_object_id")
        or metadata_map.get("local_relevance_medium_read_only_state_result_object_id"),
        "question": question_map.get("local_relevance_medium_read_only_state_result_object_question"),
        "intent": question_map.get("local_relevance_medium_read_only_state_result_object_intent"),
        "passed_check_count": _passed_check_count(checks_list),
        "failed_check_count": _failed_check_count(checks_list),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "local_relevance_medium_read_only_state_result_object_recorded": statement_map.get(
            "local_relevance_medium_read_only_state_result_object_recorded",
            False,
        ),
        "basis_state_result_object_boundary_artifact_preserved": statement_map.get(
            "basis_state_result_object_boundary_artifact_preserved",
            False,
        ),
        "basis_state_payload_return_artifact_preserved": statement_map.get(
            "basis_state_payload_return_artifact_preserved",
            False,
        ),
        "selected_command": object_map.get("selected_command") or question_map.get("selected_command"),
        "selected_command_preserved": statement_map.get("selected_command_preserved", False),
        "selected_command_is_state": statement_map.get("selected_command_is_state", False),
        "selected_state_payload_return_recorded": statement_map.get(
            "selected_state_payload_return_recorded",
            False,
        ),
        "state_payload_returned": statement_map.get("state_payload_returned", False),
        "state_payload_return_local_only": statement_map.get("state_payload_return_local_only", False),
        "state_payload_return_read_only": statement_map.get("state_payload_return_read_only", False),
        "state_result_object_created": statement_map.get("state_result_object_created", False),
        "state_result_object_local_only": statement_map.get("state_result_object_local_only", False),
        "state_result_object_read_only": statement_map.get("state_result_object_read_only", False),
        "state_result_object_summary": {
            "state_result_object_type": object_map.get("state_result_object_type"),
            "state_result_object_scope": object_map.get("state_result_object_scope"),
            "state_result_object_version": object_map.get("state_result_object_version"),
        },
        "state_packet_body_not_exposed": non_claims_map.get("state_packet_body_exposed") is False,
        "raw_full_state_packet_body_not_exposed": (
            non_claims_map.get("raw_full_state_packet_body_exposed") is False
        ),
        "lookup_not_performed": non_claims_map.get("lookup_performed") is False,
        "lookup_command_not_executed": non_claims_map.get("lookup_command_executed") is False,
        "operation_permission_not_created": non_claims_map.get("operation_permission_created") is False,
        "runtime_permission_not_created": non_claims_map.get("runtime_permission_created") is False,
        "public_api_not_created": non_claims_map.get("public_api_created") is False,
        "participant_facing_interface_not_created": (
            non_claims_map.get("participant_facing_interface_created") is False
        ),
        "distributed_network_behavior_not_created": (
            non_claims_map.get("distributed_network_behavior_created") is False
        ),
        "general_lookup_permission_not_created": (
            non_claims_map.get("general_lookup_permission_created") is False
        ),
        "arbitrary_lookup_permission_not_created": (
            non_claims_map.get("arbitrary_lookup_permission_created") is False
        ),
        "unsupported_commands_not_permitted": (
            non_claims_map.get("unsupported_commands_permitted") is False
        ),
        "unsupported_lookup_keys_not_permitted": (
            non_claims_map.get("unsupported_lookup_keys_permitted") is False
        ),
        "no_new_lookup_result_created": non_claims_map.get("new_lookup_result_created") is False,
        "no_new_lookup_entry_created": non_claims_map.get("new_lookup_entry_created") is False,
        "no_new_signal_accepted": non_claims_map.get("new_signal_accepted") is False,
        "no_new_entry_accepted": non_claims_map.get("new_entry_accepted") is False,
        "no_new_relevance_object_created": non_claims_map.get("new_relevance_object_created") is False,
        "no_new_index_entry_created": non_claims_map.get("new_index_entry_created") is False,
        "filesystem_discovery_not_performed": (
            non_claims_map.get("filesystem_discovery_performed") is False
        ),
        "registry_search_query_surface_ranking_not_created": all(
            non_claims_map.get(key) is False
            for key in (
                "registry_created",
                "search_surface_created",
                "query_surface_created",
                "ranking_surface_created",
            )
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": all(
            non_claims_map.get(key) is False
            for key in (
                "scoring_surface_created",
                "priority_surface_created",
                "validity_judgment_created",
                "truth_judgment_created",
                "authority_judgment_created",
                "currentness_judgment_created",
            )
        ),
        "repeated_reception_arbitrary_reception_feed_not_created": all(
            non_claims_map.get(key) is False
            for key in (
                "repeated_reception_permission_created",
                "arbitrary_reception_created",
                "feed_created",
            )
        ),
        "source_authority_currentness_truth_synchronization_participation_role_not_created": all(
            non_claims_map.get(key) is False
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
        "follow_on_not_created": non_claims_map.get("follow_on_work_authorized") is False,
        "key_non_claims": {
            key: non_claims_map.get(key)
            for key in (
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
        "predecessor_failure_evidence_preserved": statement_map.get(
            "predecessor_failure_evidence_preserved",
            True,
        ),
        "result_level_non_claims_canonical_false": all(
            non_claims_map.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }
    return _sanitize_value(summary)


def _build_result(
    request: Mapping[str, Any] | None,
    outcome: str,
    checks: list[dict[str, Any]],
    state_result_object: dict[str, Any] | None,
    boundary_artifact: Mapping[str, Any] | None,
    payload_artifact: Mapping[str, Any] | None,
    boundary_path: Path | None,
    payload_path: Path | None,
    additional_basis_required: list[str] | None = None,
    not_recorded_basis: list[str] | None = None,
) -> dict[str, Any]:
    state_result_object_id = (
        str(request.get("local_relevance_medium_read_only_state_result_object_id"))
        if isinstance(request, Mapping)
        and request.get("local_relevance_medium_read_only_state_result_object_id")
        else DEFAULT_STATE_RESULT_OBJECT_ID
    )
    recorded = outcome == OUTCOME_RECORDED and state_result_object is not None
    block_code = _first_failed_code(checks) if outcome == OUTCOME_BLOCKED else None
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_state_result_object_metadata": _build_metadata(
            state_result_object_id
        ),
        "declared_local_relevance_medium_read_only_state_result_object_question": (
            _build_declared_question_section(request)
        ),
        "selected_state_result_object_boundary_artifact_basis": _build_boundary_basis(
            boundary_artifact,
            boundary_path,
        ),
        "selected_state_payload_return_artifact_basis": _build_payload_basis(
            payload_artifact,
            payload_path,
        ),
        "local_relevance_medium_read_only_state_result_object": state_result_object,
        "local_relevance_medium_read_only_state_result_object_checks": checks,
        "local_relevance_medium_read_only_state_result_object_statement": _build_statement(recorded),
        "local_relevance_medium_read_only_state_result_object_non_meaning": _build_non_meaning(),
        "additional_basis_required": additional_basis_required or [],
        "not_recorded_basis": not_recorded_basis or [],
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": _block(block_code),
    }
    result["local_relevance_medium_read_only_state_result_object_summary"] = (
        build_local_relevance_medium_read_only_state_result_object_v0_min_summary(result)
    )
    return _sanitize_value(result)


def _malformed_request_result(code: str) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _check(
        checks,
        "declared local relevance medium read only state result object request is mapping",
        False,
        "mapping",
        "missing_or_non_mapping",
        code,
    )
    return _build_result(
        request=None,
        outcome=OUTCOME_BLOCKED,
        checks=checks,
        state_result_object=None,
        boundary_artifact=None,
        payload_artifact=None,
        boundary_path=None,
        payload_path=None,
    )


def resolve_local_relevance_medium_read_only_state_result_object_v0_min(
    declared_local_relevance_medium_read_only_state_result_object: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one local read-only selected-state result object request."""

    if declared_local_relevance_medium_read_only_state_result_object is None:
        return _malformed_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_REQUEST_MALFORMED"
        )
    if not _is_mapping(declared_local_relevance_medium_read_only_state_result_object):
        return _malformed_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_REQUEST_MALFORMED"
        )

    request = _safe_mapping_copy(declared_local_relevance_medium_read_only_state_result_object)
    checks: list[dict[str, Any]] = []

    question = request.get("local_relevance_medium_read_only_state_result_object_question")
    intent = request.get("local_relevance_medium_read_only_state_result_object_intent")
    boundary_path = _as_path(request.get("selected_state_result_object_boundary_artifact"))
    payload_path = _as_path(request.get("selected_state_payload_return_artifact"))
    selected_command = request.get("selected_command")
    state_result_object_type = request.get("state_result_object_type")
    state_result_object_scope = request.get("state_result_object_scope")

    _check(
        checks,
        "state result object question declared",
        isinstance(question, str) and bool(question.strip()),
        "declared question string",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "state result object intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "state result object block intent not requested",
        intent != INTENT_BLOCK,
        f"not {INTENT_BLOCK}",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BLOCK_REQUESTED",
    )

    boundary_missing_requested = request.get("state_result_object_boundary_artifact_missing") is True
    payload_missing_requested = request.get("state_payload_return_artifact_missing") is True

    _check(
        checks,
        "state result object boundary artifact path declared",
        boundary_path is not None and not boundary_missing_requested,
        "declared boundary artifact path",
        str(boundary_path) if boundary_path else None,
        "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_PATH_MISSING",
    )
    boundary_artifact: dict[str, Any] | None = None
    boundary_read_code: str | None = None
    if boundary_path is not None and not boundary_missing_requested:
        boundary_artifact, boundary_read_code = _read_json_object(
            boundary_path,
            "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_UNREADABLE",
            "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
        )
        _check(
            checks,
            "state result object boundary artifact readable JSON object",
            boundary_read_code is None,
            "readable JSON object",
            boundary_read_code or "readable JSON object",
            boundary_read_code,
        )

    _check(
        checks,
        "state payload return artifact path declared",
        payload_path is not None and not payload_missing_requested,
        "declared payload return artifact path",
        str(payload_path) if payload_path else None,
        "STATE_PAYLOAD_RETURN_ARTIFACT_PATH_MISSING",
    )
    payload_artifact: dict[str, Any] | None = None
    payload_read_code: str | None = None
    if payload_path is not None and not payload_missing_requested:
        payload_artifact, payload_read_code = _read_json_object(
            payload_path,
            "STATE_PAYLOAD_RETURN_ARTIFACT_UNREADABLE",
            "STATE_PAYLOAD_RETURN_ARTIFACT_NOT_JSON_OBJECT",
        )
        _check(
            checks,
            "state payload return artifact readable JSON object",
            payload_read_code is None,
            "readable JSON object",
            payload_read_code or "readable JSON object",
            payload_read_code,
        )

    boundary = _boundary_object(boundary_artifact)
    boundary_statement = _boundary_statement(boundary_artifact)
    boundary_summary = _boundary_summary(boundary_artifact)
    boundary_metadata = _boundary_metadata(boundary_artifact)
    payload = _payload_return_object(payload_artifact)
    payload_statement = _payload_return_statement(payload_artifact)
    payload_summary = _payload_return_summary(payload_artifact)
    payload_metadata = _payload_return_metadata(payload_artifact)

    boundary_outcome = _first_present(
        boundary_artifact.get("outcome") if boundary_artifact else None,
        boundary_summary.get("outcome"),
    )
    boundary_failed_count = _artifact_failed_count(
        boundary_artifact,
        boundary_summary,
        "local_relevance_medium_read_only_state_result_object_boundary_checks",
    )
    boundary_version = _first_present(
        boundary_summary.get("result_version"),
        boundary_artifact.get("result_version") if boundary_artifact else None,
        boundary_metadata.get("local_relevance_medium_read_only_state_result_object_boundary_version"),
        boundary_metadata.get("result_version"),
        boundary.get("boundary_version"),
    )
    payload_outcome = _first_present(
        payload_artifact.get("outcome") if payload_artifact else None,
        payload_summary.get("outcome"),
    )
    payload_failed_count = _artifact_failed_count(
        payload_artifact,
        payload_summary,
        "local_relevance_medium_read_only_state_payload_return_checks",
    )
    payload_version = _first_present(
        payload_summary.get("result_version"),
        payload_artifact.get("result_version") if payload_artifact else None,
        payload_metadata.get("local_relevance_medium_read_only_state_payload_return_version"),
        payload_metadata.get("result_version"),
        payload.get("state_payload_return_version"),
    )

    _check(
        checks,
        "state result object boundary artifact outcome recorded",
        boundary_outcome == STATE_RESULT_OBJECT_BOUNDARY_RECORDED_OUTCOME
        and request.get("state_result_object_boundary_artifact_not_recorded") is not True,
        STATE_RESULT_OBJECT_BOUNDARY_RECORDED_OUTCOME,
        boundary_outcome,
        "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "state result object boundary artifact result version 0.1.0",
        boundary_version == RESULT_VERSION
        and request.get("state_result_object_boundary_artifact_version_not_0_1_0") is not True,
        RESULT_VERSION,
        boundary_version,
        "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "state result object boundary artifact failed check count zero",
        boundary_failed_count == 0
        and request.get("state_result_object_boundary_artifact_failed_checks_present") is not True,
        0,
        boundary_failed_count,
        "STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "state payload return artifact outcome recorded",
        payload_outcome == STATE_PAYLOAD_RETURN_RECORDED_OUTCOME
        and request.get("state_payload_return_artifact_not_recorded") is not True,
        STATE_PAYLOAD_RETURN_RECORDED_OUTCOME,
        payload_outcome,
        "STATE_PAYLOAD_RETURN_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "state payload return artifact result version 0.1.0",
        payload_version == RESULT_VERSION
        and request.get("state_payload_return_artifact_version_not_0_1_0") is not True,
        RESULT_VERSION,
        payload_version,
        "STATE_PAYLOAD_RETURN_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "state payload return artifact failed check count zero",
        payload_failed_count == 0
        and request.get("state_payload_return_artifact_failed_checks_present") is not True,
        0,
        payload_failed_count,
        "STATE_PAYLOAD_RETURN_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    _check(
        checks,
        "selected command declared",
        isinstance(selected_command, str)
        and selected_command != ""
        and request.get("selected_command_missing") is not True,
        "declared selected command",
        selected_command,
        "SELECTED_COMMAND_MISSING",
    )
    artifact_commands_are_state = all(
        command in (None, SELECTED_COMMAND)
        for command in (
            boundary.get("selected_command"),
            payload.get("selected_command"),
        )
    )
    _check(
        checks,
        "selected command exactly state",
        selected_command == SELECTED_COMMAND
        and artifact_commands_are_state
        and request.get("selected_command_not_state") is not True,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected command is state",
        selected_command == SELECTED_COMMAND
        and boundary.get("selected_command_is_state") is not False
        and payload.get("selected_command_is_state") is not False,
        True,
        selected_command == SELECTED_COMMAND,
        "SELECTED_COMMAND_NOT_STATE",
    )

    selected_payload_recorded = _first_present(
        _artifact_bool(payload, payload_statement, "selected_state_payload_return_recorded"),
        _artifact_bool(boundary, boundary_statement, "selected_state_payload_return_recorded"),
    )
    state_payload_returned = _first_present(
        _artifact_bool(payload, payload_statement, "state_payload_returned"),
        _artifact_bool(boundary, boundary_statement, "state_payload_returned"),
    )
    state_payload_return_local_only = _first_present(
        _artifact_bool(payload, payload_statement, "state_payload_return_local_only"),
        _artifact_bool(boundary, boundary_statement, "state_payload_return_local_only"),
    )
    state_payload_return_read_only = _first_present(
        _artifact_bool(payload, payload_statement, "state_payload_return_read_only"),
        _artifact_bool(boundary, boundary_statement, "state_payload_return_read_only"),
    )

    _check(
        checks,
        "selected-state payload return recorded",
        selected_payload_recorded is True
        and request.get("selected_state_payload_return_not_recorded") is not True,
        True,
        selected_payload_recorded,
        "SELECTED_STATE_PAYLOAD_RETURN_NOT_RECORDED",
    )
    _check(
        checks,
        "state payload returned",
        state_payload_returned is True and request.get("state_payload_not_returned") is not True,
        True,
        state_payload_returned,
        "STATE_PAYLOAD_NOT_RETURNED",
    )
    _check(
        checks,
        "state payload return local only",
        state_payload_return_local_only is True
        and request.get("state_payload_return_local_only_not_true") is not True,
        True,
        state_payload_return_local_only,
        "STATE_PAYLOAD_RETURN_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "state payload return read only",
        state_payload_return_read_only is True
        and request.get("state_payload_return_read_only_not_true") is not True,
        True,
        state_payload_return_read_only,
        "STATE_PAYLOAD_RETURN_READ_ONLY_NOT_TRUE",
    )

    _check(
        checks,
        "state result object type declared",
        isinstance(state_result_object_type, str) and bool(state_result_object_type),
        STATE_RESULT_OBJECT_TYPE,
        state_result_object_type,
        "STATE_RESULT_OBJECT_TYPE_MISSING",
    )
    _check(
        checks,
        "state result object type exact",
        state_result_object_type == STATE_RESULT_OBJECT_TYPE
        and request.get(
            "state_result_object_type_not_local_relevance_medium_read_only_state_result_object"
        )
        is not True,
        STATE_RESULT_OBJECT_TYPE,
        state_result_object_type,
        "STATE_RESULT_OBJECT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT",
    )
    _check(
        checks,
        "state result object scope declared",
        isinstance(state_result_object_scope, str) and bool(state_result_object_scope),
        STATE_RESULT_OBJECT_SCOPE,
        state_result_object_scope,
        "STATE_RESULT_OBJECT_SCOPE_MISSING",
    )
    _check(
        checks,
        "state result object scope exact",
        state_result_object_scope == STATE_RESULT_OBJECT_SCOPE
        and request.get("state_result_object_scope_not_selected_state_result_object_only")
        is not True,
        STATE_RESULT_OBJECT_SCOPE,
        state_result_object_scope,
        "STATE_RESULT_OBJECT_SCOPE_NOT_SELECTED_STATE_RESULT_OBJECT_ONLY",
    )

    _check(
        checks,
        "local relevance medium read only state result object recorded",
        request.get("local_relevance_medium_read_only_state_result_object_not_recorded") is not True,
        True,
        request.get("local_relevance_medium_read_only_state_result_object_not_recorded") is not True,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_NOT_RECORDED",
    )
    _check(
        checks,
        "state result object created",
        request.get("state_result_object_not_created") is not True
        and request.get("state_result_object_created") is not False,
        True,
        request.get("state_result_object_created", True),
        "STATE_RESULT_OBJECT_NOT_CREATED",
    )
    _check(
        checks,
        "state result object local only",
        request.get("state_result_object_local_only_not_true") is not True
        and request.get("state_result_object_local_only") is not False,
        True,
        request.get("state_result_object_local_only", True),
        "STATE_RESULT_OBJECT_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "state result object read only",
        request.get("state_result_object_read_only_not_true") is not True
        and request.get("state_result_object_read_only") is not False,
        True,
        request.get("state_result_object_read_only", True),
        "STATE_RESULT_OBJECT_READ_ONLY_NOT_TRUE",
    )

    for field in STATE_RESULT_OBJECT_FALSE_FIELDS:
        code = FALSE_FIELD_BLOCK_CODES[field]
        _check(
            checks,
            field.replace("_", " ") + " false",
            not _field_is_true_in_any(field, request, boundary, payload),
            False,
            True if _field_is_true_in_any(field, request, boundary, payload) else False,
            code,
        )

    for field in REQUEST_ONLY_FALSE_FIELDS:
        code = FALSE_FIELD_BLOCK_CODES.get(field, "NON_CLAIM_MISSING_OR_FLIPPED")
        _check(
            checks,
            field.replace("_", " ") + " false",
            request.get(field) is not True,
            False,
            request.get(field, False),
            code,
        )

    predecessor_failure_ok = (
        request.get("predecessor_failure_repaired") is not True
        and request.get("predecessor_failure_hidden") is not True
        and request.get("predecessor_failure_claimed_passed") is not True
    )
    _check(
        checks,
        "predecessor failure evidence preserved",
        predecessor_failure_ok,
        "preserved evidence only",
        "hidden_or_repaired" if not predecessor_failure_ok else "preserved",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _check(
        checks,
        "consumed request remains closed",
        request.get("consumed_request_reopened") is not True,
        False,
        request.get("consumed_request_reopened", False),
        "CONSUMED_REQUEST_REOPENED",
    )
    _check(
        checks,
        "authorization token reuse blocked",
        request.get("authorization_token_reused") is not True,
        False,
        request.get("authorization_token_reused", False),
        "AUTHORIZATION_TOKEN_REUSED",
    )
    _check(
        checks,
        "required non-claims false",
        _declared_non_claims_are_false(request),
        "all required declared non-claims are false bool",
        "canonical_false" if _declared_non_claims_are_false(request) else "missing_or_flipped",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _check(
        checks,
        "result-level required false non-claims canonical false",
        all(value is False for value in _canonical_false_non_claims().values()),
        "canonical false result-level non-claims",
        "canonical false result-level non-claims",
        None,
    )

    failed_count = _failed_check_count(checks)
    state_result_object: dict[str, Any] | None = None
    additional_basis_required: list[str] = []
    not_recorded_basis: list[str] = []

    if failed_count:
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
        not_recorded_basis.append("declared intent did not record state result object")
    elif request.get("additional_basis_context"):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        additional_basis_required.append(str(request.get("additional_basis_context")))
    else:
        outcome = OUTCOME_RECORDED
        if boundary_artifact is not None and payload_artifact is not None and boundary_path and payload_path:
            state_result_object = _build_state_result_object(
                request,
                boundary_artifact,
                payload_artifact,
                boundary_path,
                payload_path,
            )

    return _build_result(
        request=request,
        outcome=outcome,
        checks=checks,
        state_result_object=state_result_object,
        boundary_artifact=boundary_artifact,
        payload_artifact=payload_artifact,
        boundary_path=boundary_path,
        payload_path=payload_path,
        additional_basis_required=additional_basis_required,
        not_recorded_basis=not_recorded_basis,
    )


def resolve_local_relevance_medium_read_only_state_result_object_v0_min_from_path(
    declared_local_relevance_medium_read_only_state_result_object_path: Path | str,
) -> dict[str, Any]:
    """Read a declared request JSON object and resolve it."""

    path = Path(declared_local_relevance_medium_read_only_state_result_object_path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return _malformed_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_REQUEST_UNREADABLE"
        )
    if not isinstance(data, Mapping):
        return _malformed_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_REQUEST_MALFORMED"
        )
    return resolve_local_relevance_medium_read_only_state_result_object_v0_min(data)


def _candidate_output_path(base_path: Path) -> Path:
    if not base_path.exists():
        return base_path
    stem = base_path.stem
    suffix = base_path.suffix
    parent = base_path.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def write_local_relevance_medium_read_only_state_result_object_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result as stable UTF-8 JSON without overwriting."""

    result_copy = _sanitize_value(copy.deepcopy(dict(result)))
    if output_path is None:
        state_result_object = result_copy.get("local_relevance_medium_read_only_state_result_object")
        if isinstance(state_result_object, Mapping) and state_result_object.get("state_result_object_id"):
            state_result_object_id = str(state_result_object["state_result_object_id"])
        else:
            metadata = result_copy.get("local_relevance_medium_read_only_state_result_object_metadata")
            if isinstance(metadata, Mapping) and metadata.get(
                "local_relevance_medium_read_only_state_result_object_id"
            ):
                state_result_object_id = str(
                    metadata["local_relevance_medium_read_only_state_result_object_id"]
                )
            else:
                state_result_object_id = DEFAULT_STATE_RESULT_OBJECT_ID
        output_path = OUTPUT_ROOT / (
            f"{state_result_object_id}__"
            "local_relevance_medium_read_only_state_result_object_v0_min_result.json"
        )
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _candidate_output_path(path)
    final_path.write_text(
        json.dumps(result_copy, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_local_relevance_medium_read_only_state_result_object_v0_min_request(
    *,
    local_relevance_medium_read_only_state_result_object_id: str = DEFAULT_STATE_RESULT_OBJECT_ID,
    selected_state_result_object_boundary_artifact: Path | str = DEFAULT_STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT,
    selected_state_payload_return_artifact: Path | str = DEFAULT_STATE_PAYLOAD_RETURN_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    state_result_object_type: str = STATE_RESULT_OBJECT_TYPE,
    state_result_object_scope: str = STATE_RESULT_OBJECT_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    """Build a declared request for this resolver."""

    if selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyStateResultObjectV0MinError(
            "selected command must be exactly state"
        )
    non_claims = _canonical_false_non_claims()
    if declared_non_claims is not None:
        incoming = dict(declared_non_claims)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            if incoming.get(key) is False:
                non_claims[key] = False
            elif key in incoming:
                non_claims[key] = incoming[key]
    request: dict[str, Any] = {
        "local_relevance_medium_read_only_state_result_object_id": (
            local_relevance_medium_read_only_state_result_object_id
        ),
        "local_relevance_medium_read_only_state_result_object_question": (
            "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY "
            "for selected command state, and one clean "
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN, may one "
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT be recorded for the "
            "selected-state payload return without packet-body exposure, lookup, "
            "operation permission, runtime permission, public API, distributed behavior, "
            "or follow-on work?"
        ),
        "local_relevance_medium_read_only_state_result_object_intent": intent,
        "selected_state_result_object_boundary_artifact": str(
            selected_state_result_object_boundary_artifact
        ),
        "selected_state_payload_return_artifact": str(selected_state_payload_return_artifact),
        "selected_command": selected_command,
        "state_result_object_type": state_result_object_type,
        "state_result_object_scope": state_result_object_scope,
        "state_result_object_created": True,
        "state_result_object_local_only": True,
        "state_result_object_read_only": True,
        "declared_non_claims": non_claims,
    }
    request.update(_sanitize_value(extra_fields))
    return request
