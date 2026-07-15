"""Resolve one local read-only selected-state operation execution.

This resolver reads one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY artifact and one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION artifact. It records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION object only.

The object is operation-execution-shaped, local, read-only, selected-state-only,
closure-token-aware, and non-runtime-shaped. It records one bounded local
read-only operation execution for selected command state. It creates no runtime
permission, public API, participant-facing interface, distributed behavior,
general operation permission, general lookup permission, arbitrary lookup
permission, unsupported command or key permission, new lookup entry,
registry/search/query/ranking surface, source movement, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyOperationExecutionV0MinError(RuntimeError):
    """Bounded resolver error for operation-execution request/path handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_operation_execution_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_execution_v0_min"
)
DEFAULT_OPERATION_EXECUTION_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_execution_boundary_v0_min/"
    "local_relevance_medium_read_only_operation_execution_boundary_reference_review_001__"
    "local_relevance_medium_read_only_operation_execution_boundary_v0_min_result.json"
)
DEFAULT_OPERATION_PERMISSION_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_permission_v0_min/"
    "local_relevance_medium_read_only_operation_permission_reference_review_001__"
    "local_relevance_medium_read_only_operation_permission_v0_min_result.json"
)

DEFAULT_OPERATION_EXECUTION_ID = "local_relevance_medium_read_only_operation_execution_001"
OPERATION_EXECUTION_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION"
OPERATION_EXECUTION_SCOPE = "SELECTED_OPERATION_EXECUTION_ONLY"
SUPPORTED_OPERATION_EXECUTION_TYPE_VALUES = (OPERATION_EXECUTION_TYPE,)
SUPPORTED_OPERATION_EXECUTION_SCOPE_VALUES = (OPERATION_EXECUTION_SCOPE,)
SELECTED_COMMAND = "state"

OPERATION_EXECUTION_BOUNDARY_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_RECORDED"
)
OPERATION_PERMISSION_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_RECORDED"
)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY "
    "for selected command state, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION, existing reusable "
    "read-only lookup permission, prior lookup-pair coverage, and prior local "
    "carrier command surface, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION be recorded for selected "
    "command state, without creating runtime permission, creating public API, "
    "creating participant-facing interface, creating distributed network behavior, "
    "creating general operation permission, creating general lookup permission, "
    "creating arbitrary lookup permission, permitting unsupported commands, "
    "permitting unsupported lookup keys, creating new lookup entry beyond the already "
    "bounded selected-state lookup result object, accepting new entries, accepting "
    "new signals, performing filesystem discovery, creating query surface, registry, "
    "search, ranking, scoring, priority, validity judgment, truth judgment, "
    "authority, currentness, synchronization, participation authorization, "
    "participant role, repeated reception permission, arbitrary reception, feed, "
    "source transfer, source receipt, or follow-on work?"
)

OPERATION_EXECUTION_OBJECT_FALSE_FIELDS = (
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "general_operation_permission_created",
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
    "artifact_existence_treated_as_operation_execution_authority",
    "latest_file_posture_treated_as_operation_execution_authority",
    "repo_local_availability_treated_as_operation_execution_authority",
    "hidden_repo_state_used_as_operation_execution_content",
    "hidden_repo_state_used_as_operation_execution_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

REQUIRED_FALSE_NON_CLAIMS = OPERATION_EXECUTION_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_operation_execution_recorded",
    "basis_operation_execution_boundary_artifact_preserved",
    "basis_operation_permission_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_operation_permission_recorded",
    "operation_permission_created",
    "operation_permission_local_only",
    "operation_permission_read_only",
    "operation_execution_created",
    "operation_execution_performed",
    "operation_execution_local_only",
    "operation_execution_read_only",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BLOCK_REQUESTED",
    "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_PATH_MISSING",
    "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_UNREADABLE",
    "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "OPERATION_PERMISSION_ARTIFACT_PATH_MISSING",
    "OPERATION_PERMISSION_ARTIFACT_UNREADABLE",
    "OPERATION_PERMISSION_ARTIFACT_NOT_JSON_OBJECT",
    "OPERATION_PERMISSION_ARTIFACT_NOT_RECORDED",
    "OPERATION_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "OPERATION_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_OPERATION_PERMISSION_NOT_RECORDED",
    "OPERATION_PERMISSION_NOT_CREATED",
    "OPERATION_PERMISSION_LOCAL_ONLY_NOT_TRUE",
    "OPERATION_PERMISSION_READ_ONLY_NOT_TRUE",
    "OPERATION_EXECUTION_TYPE_MISSING",
    "OPERATION_EXECUTION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
    "OPERATION_EXECUTION_SCOPE_MISSING",
    "OPERATION_EXECUTION_SCOPE_NOT_SELECTED_OPERATION_EXECUTION_ONLY",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_NOT_RECORDED",
    "OPERATION_EXECUTION_NOT_CREATED",
    "OPERATION_EXECUTION_NOT_PERFORMED",
    "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE",
    "RUNTIME_PERMISSION_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "GENERAL_OPERATION_PERMISSION_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_OPERATION_EXECUTION_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_OPERATION_EXECUTION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_OPERATION_EXECUTION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_OPERATION_EXECUTION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_OPERATION_EXECUTION_AUTHORITY",
    "PRIOR_ARTIFACTS_MUTATED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_REQUEST_UNREADABLE",
)

_FALSE_FIELD_BLOCK_CODES = {
    "runtime_permission_created": "RUNTIME_PERMISSION_CREATED",
    "public_api_created": "PUBLIC_API_CREATED",
    "participant_facing_interface_created": "PARTICIPANT_FACING_INTERFACE_CREATED",
    "distributed_network_behavior_created": "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "general_operation_permission_created": "GENERAL_OPERATION_PERMISSION_CREATED",
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
    "artifact_existence_treated_as_operation_execution_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_OPERATION_EXECUTION_AUTHORITY"
    ),
    "latest_file_posture_treated_as_operation_execution_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_OPERATION_EXECUTION_AUTHORITY"
    ),
    "repo_local_availability_treated_as_operation_execution_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_OPERATION_EXECUTION_AUTHORITY"
    ),
    "hidden_repo_state_used_as_operation_execution_content": (
        "HIDDEN_REPO_STATE_USED_AS_OPERATION_EXECUTION_CONTENT"
    ),
    "hidden_repo_state_used_as_operation_execution_authority": (
        "HIDDEN_REPO_STATE_USED_AS_OPERATION_EXECUTION_AUTHORITY"
    ),
    "prior_artifacts_mutated": "PRIOR_ARTIFACTS_MUTATED",
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
    "raw_operation_execution_body",
    "raw_operation_execution_boundary_body",
    "raw_operation_permission_body",
    "raw_operation_permission_boundary_body",
    "raw_lookup_result_body",
    "raw_lookup_result_boundary_body",
    "raw_lookup_performed_body",
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
    "operation_execution_body",
    "operation_execution_boundary_body",
    "operation_permission_body",
    "operation_permission_boundary_body",
    "lookup_result_body",
    "lookup_result_boundary_body",
    "lookup_performed_body",
    "lookup_performed_boundary_body",
    "lookup_command_execution_body",
    "lookup_command_execution_boundary_body",
    "full_state_packet_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
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

HIDDEN_REQUEST_CONTENT_KEYS = (
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _sanitize(value: Any, key: str | None = None) -> Any:
    key_name = str(key or "").lower()
    if key_name in SENSITIVE_CONTENT_KEYS or key_name.endswith("_body"):
        return "[REDACTED_SENSITIVE_CONTENT]"
    if isinstance(value, str):
        if value in HOSTILE_SENTINELS:
            return "[REDACTED_SENSITIVE_CONTENT]"
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, MappingABC):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, key) for item in value]
    return copy.deepcopy(value)


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _as_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        stripped = value.strip()
        if stripped.isdigit():
            return int(stripped)
    return None


def _mapping(value: Any) -> Mapping[str, Any]:
    if isinstance(value, MappingABC):
        return value
    return {}


def _find_first_mapping_value(artifact: Mapping[str, Any], suffix: str) -> Mapping[str, Any]:
    for key, value in artifact.items():
        if str(key).endswith(suffix) and isinstance(value, MappingABC):
            return value
    return {}


def _find_first_checks(artifact: Mapping[str, Any]) -> list[Any]:
    for key, value in artifact.items():
        if str(key).endswith("_checks") and isinstance(value, list):
            return value
    return []


def _failed_count_from_checks(checks: list[Any]) -> int:
    return sum(
        1
        for check in checks
        if isinstance(check, MappingABC) and check.get("passed") is False
    )


def _passed_count_from_checks(checks: list[Any]) -> int:
    return sum(
        1 for check in checks if isinstance(check, MappingABC) and check.get("passed") is True
    )


def _artifact_common(
    artifact: Mapping[str, Any],
    object_key: str,
    object_version_key: str,
) -> dict[str, Any]:
    obj = _mapping(artifact.get(object_key))
    summary = _find_first_mapping_value(artifact, "_summary")
    metadata = _find_first_mapping_value(artifact, "_metadata")
    checks = _find_first_checks(artifact)
    failed_count = _first_present(
        artifact.get("failed_check_count"),
        summary.get("failed_check_count"),
        metadata.get("failed_check_count"),
    )
    passed_count = _first_present(
        artifact.get("passed_check_count"),
        summary.get("passed_check_count"),
        metadata.get("passed_check_count"),
    )
    return {
        "object": obj,
        "summary": summary,
        "metadata": metadata,
        "checks": checks,
        "outcome": _first_present(
            artifact.get("outcome"),
            summary.get("outcome"),
            metadata.get("outcome"),
        ),
        "result_version": _first_present(
            artifact.get("result_version"),
            summary.get("result_version"),
            metadata.get("result_version"),
            obj.get(object_version_key),
        ),
        "failed_check_count": _first_present(
            _as_int(failed_count),
            _failed_count_from_checks(checks) if checks else None,
        ),
        "passed_check_count": _first_present(
            _as_int(passed_count),
            _passed_count_from_checks(checks) if checks else None,
        ),
    }


def _read_json_object(path_value: Any, not_object_code: str) -> tuple[dict[str, Any] | None, str | None]:
    try:
        with Path(path_value).open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return None, not_object_code.replace("_NOT_JSON_OBJECT", "_UNREADABLE")
    if not isinstance(data, MappingABC):
        return None, not_object_code
    return dict(copy.deepcopy(data)), None


def _empty_operation_execution_boundary_basis(path_value: Any) -> dict[str, Any]:
    return {
        "artifact_path": str(path_value) if path_value is not None else None,
        "artifact_outcome": None,
        "artifact_result_version": None,
        "artifact_failed_check_count": None,
        "artifact_passed_check_count": None,
        "selected_command": None,
        "selected_command_is_state": None,
        "selected_operation_permission_recorded": None,
        "operation_permission_created": None,
        "operation_permission_local_only": None,
        "operation_permission_read_only": None,
        "future_operation_execution_may_be_considered": None,
    }


def _extract_operation_execution_boundary_basis(
    artifact: Mapping[str, Any],
    path_value: Any,
) -> dict[str, Any]:
    common = _artifact_common(
        artifact,
        "local_relevance_medium_read_only_operation_execution_boundary",
        "boundary_version",
    )
    obj = common["object"]
    summary = common["summary"]
    statement = _mapping(
        artifact.get("local_relevance_medium_read_only_operation_execution_boundary_statement")
    )
    return {
        "artifact_path": str(path_value),
        "artifact_outcome": common["outcome"],
        "artifact_result_version": common["result_version"],
        "artifact_failed_check_count": common["failed_check_count"],
        "artifact_passed_check_count": common["passed_check_count"],
        "selected_command": _first_present(obj.get("selected_command"), summary.get("selected_command")),
        "selected_command_is_state": _first_present(
            obj.get("selected_command_is_state"),
            statement.get("selected_command_is_state"),
            summary.get("selected_command_is_state"),
        ),
        "selected_operation_permission_recorded": _first_present(
            obj.get("selected_operation_permission_recorded"),
            statement.get("selected_operation_permission_recorded"),
            summary.get("selected_operation_permission_recorded"),
        ),
        "operation_permission_created": _first_present(
            obj.get("operation_permission_created"),
            statement.get("operation_permission_created"),
            summary.get("operation_permission_created"),
        ),
        "operation_permission_local_only": _first_present(
            obj.get("operation_permission_local_only"),
            statement.get("operation_permission_local_only"),
            summary.get("operation_permission_local_only"),
        ),
        "operation_permission_read_only": _first_present(
            obj.get("operation_permission_read_only"),
            statement.get("operation_permission_read_only"),
            summary.get("operation_permission_read_only"),
        ),
        "future_operation_execution_may_be_considered": _first_present(
            obj.get("future_operation_execution_may_be_considered"),
            statement.get("future_operation_execution_may_be_considered"),
            summary.get("future_operation_execution_may_be_considered"),
        ),
    }


def _empty_operation_permission_basis(path_value: Any) -> dict[str, Any]:
    return {
        "artifact_path": str(path_value) if path_value is not None else None,
        "artifact_outcome": None,
        "artifact_result_version": None,
        "artifact_failed_check_count": None,
        "artifact_passed_check_count": None,
        "selected_command": None,
        "selected_command_is_state": None,
        "selected_operation_permission_recorded": None,
        "operation_permission_created": None,
        "operation_permission_local_only": None,
        "operation_permission_read_only": None,
    }


def _extract_operation_permission_basis(
    artifact: Mapping[str, Any],
    path_value: Any,
) -> dict[str, Any]:
    common = _artifact_common(
        artifact,
        "local_relevance_medium_read_only_operation_permission",
        "operation_permission_version",
    )
    obj = common["object"]
    summary = common["summary"]
    statement = _mapping(
        artifact.get("local_relevance_medium_read_only_operation_permission_statement")
    )
    return {
        "artifact_path": str(path_value),
        "artifact_outcome": common["outcome"],
        "artifact_result_version": common["result_version"],
        "artifact_failed_check_count": common["failed_check_count"],
        "artifact_passed_check_count": common["passed_check_count"],
        "selected_command": _first_present(obj.get("selected_command"), summary.get("selected_command")),
        "selected_command_is_state": _first_present(
            obj.get("selected_command_is_state"),
            statement.get("selected_command_is_state"),
            summary.get("selected_command_is_state"),
        ),
        "selected_operation_permission_recorded": _first_present(
            obj.get("selected_operation_permission_recorded"),
            obj.get("local_relevance_medium_read_only_operation_permission_recorded"),
            statement.get("selected_operation_permission_recorded"),
            statement.get("local_relevance_medium_read_only_operation_permission_recorded"),
            summary.get("selected_operation_permission_recorded"),
            summary.get("local_relevance_medium_read_only_operation_permission_recorded"),
        ),
        "operation_permission_created": _first_present(
            obj.get("operation_permission_created"),
            statement.get("operation_permission_created"),
            summary.get("operation_permission_created"),
        ),
        "operation_permission_local_only": _first_present(
            obj.get("operation_permission_local_only"),
            statement.get("operation_permission_local_only"),
            summary.get("operation_permission_local_only"),
        ),
        "operation_permission_read_only": _first_present(
            obj.get("operation_permission_read_only"),
            statement.get("operation_permission_read_only"),
            summary.get("operation_permission_read_only"),
        ),
    }


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    public_code = code if code in BLOCK_CODES else "NON_CLAIM_MISSING_OR_FLIPPED"
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _sanitize(expected_posture),
            "actual_posture": _sanitize(actual_posture),
            "block_code": None if passed else public_code,
            "failure_code": None if passed else public_code,
        }
    )


def _failed_checks(checks: list[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [check for check in checks if check.get("passed") is False]


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if code in BLOCK_CODES:
                return str(code)
    return None


def _check_requested_false_fields(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    for field in REQUIRED_FALSE_NON_CLAIMS:
        value = declared.get(field, False)
        passed = value is False
        _add_check(
            checks,
            f"{field}_not_created_or_authorized",
            passed,
            False,
            value,
            _FALSE_FIELD_BLOCK_CODES.get(field, "NON_CLAIM_MISSING_OR_FLIPPED"),
        )


def _declared_non_claims_passed(declared_non_claims: Any) -> bool:
    if not isinstance(declared_non_claims, MappingABC):
        return False
    return all(declared_non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _raw_or_hidden_content_present(declared: Mapping[str, Any]) -> bool:
    for key in declared:
        key_name = str(key).lower()
        if key_name in HIDDEN_REQUEST_CONTENT_KEYS:
            return True
        if key_name in SENSITIVE_CONTENT_KEYS or key_name.endswith("_body"):
            return True
    return False


def _build_operation_execution_object(
    declared: Mapping[str, Any],
    operation_execution_boundary_basis: Mapping[str, Any],
    operation_permission_basis: Mapping[str, Any],
    recorded: bool,
) -> dict[str, Any]:
    requested_command = declared.get("selected_command")
    selected_command = SELECTED_COMMAND if requested_command == SELECTED_COMMAND else None
    selected_command_is_state = selected_command == SELECTED_COMMAND

    operation_execution: dict[str, Any] = {
        "operation_execution_id": str(
            declared.get(
                "local_relevance_medium_read_only_operation_execution_id",
                DEFAULT_OPERATION_EXECUTION_ID,
            )
            or DEFAULT_OPERATION_EXECUTION_ID
        ),
        "operation_execution_type": OPERATION_EXECUTION_TYPE,
        "operation_execution_version": RESULT_VERSION,
        "operation_execution_scope": OPERATION_EXECUTION_SCOPE,
        "basis_operation_execution_boundary_artifact": operation_execution_boundary_basis.get(
            "artifact_path"
        ),
        "basis_operation_execution_boundary_outcome": operation_execution_boundary_basis.get(
            "artifact_outcome"
        ),
        "basis_operation_execution_boundary_result_version": (
            operation_execution_boundary_basis.get("artifact_result_version")
        ),
        "basis_operation_execution_boundary_failed_check_count": (
            operation_execution_boundary_basis.get("artifact_failed_check_count")
        ),
        "basis_operation_permission_artifact": operation_permission_basis.get("artifact_path"),
        "basis_operation_permission_outcome": operation_permission_basis.get("artifact_outcome"),
        "basis_operation_permission_result_version": operation_permission_basis.get(
            "artifact_result_version"
        ),
        "basis_operation_permission_failed_check_count": operation_permission_basis.get(
            "artifact_failed_check_count"
        ),
        "selected_command": selected_command,
        "selected_command_is_state": selected_command_is_state,
        "selected_operation_permission_recorded": (
            operation_permission_basis.get("selected_operation_permission_recorded") is True
        ),
        "operation_permission_created": (
            operation_permission_basis.get("operation_permission_created") is True
        ),
        "operation_permission_local_only": (
            operation_permission_basis.get("operation_permission_local_only") is True
        ),
        "operation_permission_read_only": (
            operation_permission_basis.get("operation_permission_read_only") is True
        ),
        "local_relevance_medium_read_only_operation_execution_recorded": bool(recorded),
        "operation_execution_created": bool(recorded),
        "operation_execution_performed": bool(recorded),
        "operation_execution_local_only": bool(recorded),
        "operation_execution_read_only": bool(recorded),
    }
    for field in OPERATION_EXECUTION_OBJECT_FALSE_FIELDS:
        operation_execution[field] = False
    return _sanitize(operation_execution)


def _build_statement(operation_execution: Mapping[str, Any], recorded: bool) -> dict[str, bool]:
    return {
        "local_relevance_medium_read_only_operation_execution_recorded": bool(recorded),
        "basis_operation_execution_boundary_artifact_preserved": operation_execution.get(
            "basis_operation_execution_boundary_outcome"
        )
        == OPERATION_EXECUTION_BOUNDARY_RECORDED_OUTCOME,
        "basis_operation_permission_artifact_preserved": operation_execution.get(
            "basis_operation_permission_outcome"
        )
        == OPERATION_PERMISSION_RECORDED_OUTCOME,
        "selected_command_preserved": operation_execution.get("selected_command")
        == SELECTED_COMMAND,
        "selected_command_is_state": operation_execution.get("selected_command_is_state")
        is True,
        "selected_operation_permission_recorded": operation_execution.get(
            "selected_operation_permission_recorded"
        )
        is True,
        "operation_permission_created": operation_execution.get("operation_permission_created")
        is True,
        "operation_permission_local_only": operation_execution.get(
            "operation_permission_local_only"
        )
        is True,
        "operation_permission_read_only": operation_execution.get(
            "operation_permission_read_only"
        )
        is True,
        "operation_execution_created": operation_execution.get("operation_execution_created")
        is True,
        "operation_execution_performed": operation_execution.get(
            "operation_execution_performed"
        )
        is True,
        "operation_execution_local_only": operation_execution.get(
            "operation_execution_local_only"
        )
        is True,
        "operation_execution_read_only": operation_execution.get(
            "operation_execution_read_only"
        )
        is True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    non_meaning = {
        "operation_execution_is_runtime_permission": False,
        "operation_execution_is_public_api": False,
        "operation_execution_is_participant_facing_interface": False,
        "operation_execution_is_distributed_network_behavior": False,
        "operation_execution_is_general_operation_permission": False,
        "operation_execution_is_general_lookup_permission": False,
        "operation_execution_is_arbitrary_lookup_permission": False,
        "operation_execution_permits_unsupported_commands": False,
        "operation_execution_permits_unsupported_lookup_keys": False,
        "operation_execution_creates_new_lookup_entry": False,
        "operation_execution_performs_filesystem_discovery": False,
        "operation_execution_creates_registry_search_query_or_ranking": False,
        "operation_execution_authorizes_follow_on_work": False,
    }
    for field in REQUIRED_FALSE_NON_CLAIMS:
        non_meaning[field] = False
    return non_meaning


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium read-only operation execution test",
        "local relevance medium read-only operation execution live artifact",
        "local relevance medium read-only operation execution terminal summary",
        "runtime permission",
        "public API",
        "participant-facing interface",
        "distributed network behavior",
        "general operation permission",
        "general lookup permission",
        "arbitrary lookup permission",
        "unsupported-command permission",
        "unsupported-key permission",
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
        "publication flow",
        "repeated reception permission",
        "arbitrary reception",
        "feed",
        "follow-on work",
    ]


def _build_result_artifact(
    declared: Mapping[str, Any],
    operation_execution_boundary_basis: Mapping[str, Any],
    operation_permission_basis: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block_reason: Any = None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    operation_execution = _build_operation_execution_object(
        declared,
        operation_execution_boundary_basis,
        operation_permission_basis,
        recorded,
    )
    statement = _build_statement(operation_execution, recorded)
    block_code = _first_failed_code(checks)
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": block_code if outcome == OUTCOME_BLOCKED else None,
        "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
        "reason": _sanitize(block_reason or block_code) if outcome == OUTCOME_BLOCKED else None,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_operation_execution_metadata": {
            "local_relevance_medium_read_only_operation_execution_id": operation_execution[
                "operation_execution_id"
            ],
            "local_relevance_medium_read_only_operation_execution_type": (
                OPERATION_EXECUTION_TYPE
            ),
            "local_relevance_medium_read_only_operation_execution_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
            "result_version": RESULT_VERSION,
        },
        "declared_local_relevance_medium_read_only_operation_execution_question": {
            "question": _sanitize(
                declared.get("local_relevance_medium_read_only_operation_execution_question")
            ),
            "intent": _sanitize(
                declared.get("local_relevance_medium_read_only_operation_execution_intent")
            ),
            "selected_command": _sanitize(declared.get("selected_command")),
            "operation_execution_type": _sanitize(declared.get("operation_execution_type")),
            "operation_execution_scope": _sanitize(declared.get("operation_execution_scope")),
        },
        "selected_operation_execution_boundary_artifact_basis": _sanitize(
            dict(operation_execution_boundary_basis)
        ),
        "selected_operation_permission_artifact_basis": _sanitize(
            dict(operation_permission_basis)
        ),
        "local_relevance_medium_read_only_operation_execution": operation_execution,
        "local_relevance_medium_read_only_operation_execution_checks": _sanitize(checks),
        "local_relevance_medium_read_only_operation_execution_statement": statement,
        "local_relevance_medium_read_only_operation_execution_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": _sanitize(
            declared.get("additional_basis_context", [])
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else []
        ),
        "not_recorded_basis": _sanitize(
            declared.get("not_recorded_basis", [])
            if outcome in (OUTCOME_NOT_RECORDED, OUTCOME_BLOCKED)
            else []
        ),
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["local_relevance_medium_read_only_operation_execution_summary"] = (
        build_local_relevance_medium_read_only_operation_execution_v0_min_summary(result)
    )
    return _sanitize(result)


def _blocked_malformed_result(code: str, reason: Any) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _add_check(
        checks,
        "declared_local_relevance_medium_read_only_operation_execution_request_readable",
        False,
        "mapping JSON object",
        reason,
        code,
    )
    return _build_result_artifact(
        {},
        _empty_operation_execution_boundary_basis(None),
        _empty_operation_permission_basis(None),
        checks,
        OUTCOME_BLOCKED,
        reason,
    )


def resolve_local_relevance_medium_read_only_operation_execution_v0_min(
    declared_local_relevance_medium_read_only_operation_execution: Mapping[str, Any]
    | None = None,
) -> dict:
    """Resolve one bounded local read-only selected-state operation execution."""

    if declared_local_relevance_medium_read_only_operation_execution is None:
        declared = build_declared_local_relevance_medium_read_only_operation_execution_v0_min_request()
    elif isinstance(declared_local_relevance_medium_read_only_operation_execution, MappingABC):
        declared = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_operation_execution)
        )
    else:
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_REQUEST_MALFORMED",
            "declared request is not a mapping",
        )

    checks: list[dict[str, Any]] = []
    question = declared.get("local_relevance_medium_read_only_operation_execution_question")
    intent = declared.get("local_relevance_medium_read_only_operation_execution_intent")

    _add_check(
        checks,
        "operation_execution_question_declared",
        isinstance(question, str) and bool(question.strip()),
        "declared operation execution question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_QUESTION_UNDECLARED",
    )
    _add_check(
        checks,
        "operation_execution_intent_supported",
        intent in SUPPORTED_INTENTS and intent != INTENT_BLOCK,
        f"one of {SUPPORTED_INTENTS[:-1]}",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BLOCK_REQUESTED"
        if intent == INTENT_BLOCK
        else "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_INTENT_UNSUPPORTED",
    )

    boundary_path = declared.get("selected_operation_execution_boundary_artifact")
    boundary_path_declared = (
        boundary_path is not None
        and boundary_path != ""
        and declared.get("operation_execution_boundary_artifact_missing") is not True
    )
    _add_check(
        checks,
        "operation_execution_boundary_artifact_path_declared",
        boundary_path_declared,
        "declared operation execution boundary artifact path",
        boundary_path,
        "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_PATH_MISSING",
    )
    operation_execution_boundary_basis = _empty_operation_execution_boundary_basis(
        boundary_path
    )
    if boundary_path_declared:
        boundary_artifact, boundary_read_code = _read_json_object(
            boundary_path,
            "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
        )
        _add_check(
            checks,
            "operation_execution_boundary_artifact_readable_json_object",
            boundary_read_code is None,
            "readable JSON object",
            boundary_read_code or "readable JSON object",
            boundary_read_code or "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_UNREADABLE",
        )
        if boundary_artifact is not None:
            operation_execution_boundary_basis = _extract_operation_execution_boundary_basis(
                boundary_artifact,
                boundary_path,
            )

    boundary_outcome_ok = (
        operation_execution_boundary_basis.get("artifact_outcome")
        == OPERATION_EXECUTION_BOUNDARY_RECORDED_OUTCOME
        and declared.get("operation_execution_boundary_artifact_not_recorded") is not True
    )
    _add_check(
        checks,
        "operation_execution_boundary_artifact_outcome_recorded",
        boundary_outcome_ok,
        OPERATION_EXECUTION_BOUNDARY_RECORDED_OUTCOME,
        operation_execution_boundary_basis.get("artifact_outcome"),
        "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    boundary_version_ok = (
        operation_execution_boundary_basis.get("artifact_result_version") == RESULT_VERSION
        and declared.get("operation_execution_boundary_artifact_version_not_0_1_0")
        is not True
    )
    _add_check(
        checks,
        "operation_execution_boundary_artifact_result_version_0_1_0",
        boundary_version_ok,
        RESULT_VERSION,
        operation_execution_boundary_basis.get("artifact_result_version"),
        "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    )
    boundary_failed_count = operation_execution_boundary_basis.get(
        "artifact_failed_check_count"
    )
    boundary_failed_count_ok = (
        boundary_failed_count == 0
        and declared.get("operation_execution_boundary_artifact_failed_checks_present")
        is not True
    )
    _add_check(
        checks,
        "operation_execution_boundary_artifact_failed_check_count_zero",
        boundary_failed_count_ok,
        0,
        boundary_failed_count,
        "OPERATION_EXECUTION_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    operation_permission_path = declared.get("selected_operation_permission_artifact")
    operation_permission_path_declared = (
        operation_permission_path is not None
        and operation_permission_path != ""
        and declared.get("operation_permission_artifact_missing") is not True
    )
    _add_check(
        checks,
        "operation_permission_artifact_path_declared",
        operation_permission_path_declared,
        "declared operation permission artifact path",
        operation_permission_path,
        "OPERATION_PERMISSION_ARTIFACT_PATH_MISSING",
    )
    operation_permission_basis = _empty_operation_permission_basis(operation_permission_path)
    if operation_permission_path_declared:
        operation_permission_artifact, operation_permission_read_code = _read_json_object(
            operation_permission_path,
            "OPERATION_PERMISSION_ARTIFACT_NOT_JSON_OBJECT",
        )
        _add_check(
            checks,
            "operation_permission_artifact_readable_json_object",
            operation_permission_read_code is None,
            "readable JSON object",
            operation_permission_read_code or "readable JSON object",
            operation_permission_read_code or "OPERATION_PERMISSION_ARTIFACT_UNREADABLE",
        )
        if operation_permission_artifact is not None:
            operation_permission_basis = _extract_operation_permission_basis(
                operation_permission_artifact,
                operation_permission_path,
            )

    operation_permission_outcome_ok = (
        operation_permission_basis.get("artifact_outcome")
        == OPERATION_PERMISSION_RECORDED_OUTCOME
        and declared.get("operation_permission_artifact_not_recorded") is not True
    )
    _add_check(
        checks,
        "operation_permission_artifact_outcome_recorded",
        operation_permission_outcome_ok,
        OPERATION_PERMISSION_RECORDED_OUTCOME,
        operation_permission_basis.get("artifact_outcome"),
        "OPERATION_PERMISSION_ARTIFACT_NOT_RECORDED",
    )
    operation_permission_version_ok = (
        operation_permission_basis.get("artifact_result_version") == RESULT_VERSION
        and declared.get("operation_permission_artifact_version_not_0_1_0") is not True
    )
    _add_check(
        checks,
        "operation_permission_artifact_result_version_0_1_0",
        operation_permission_version_ok,
        RESULT_VERSION,
        operation_permission_basis.get("artifact_result_version"),
        "OPERATION_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0",
    )
    operation_permission_failed_count = operation_permission_basis.get(
        "artifact_failed_check_count"
    )
    operation_permission_failed_count_ok = (
        operation_permission_failed_count == 0
        and declared.get("operation_permission_artifact_failed_checks_present") is not True
    )
    _add_check(
        checks,
        "operation_permission_artifact_failed_check_count_zero",
        operation_permission_failed_count_ok,
        0,
        operation_permission_failed_count,
        "OPERATION_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    selected_command = declared.get("selected_command")
    selected_command_declared = (
        selected_command is not None and declared.get("selected_command_missing") is not True
    )
    _add_check(
        checks,
        "selected_command_declared",
        selected_command_declared,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_MISSING",
    )
    selected_command_is_state = (
        selected_command == SELECTED_COMMAND
        and declared.get("selected_command_not_state") is not True
    )
    _add_check(
        checks,
        "selected_command_exactly_state",
        selected_command_is_state,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _add_check(
        checks,
        "selected_command_is_state",
        selected_command_is_state,
        True,
        selected_command_is_state,
        "SELECTED_COMMAND_NOT_STATE",
    )

    _add_check(
        checks,
        "selected_operation_permission_recorded",
        operation_permission_basis.get("selected_operation_permission_recorded") is True
        and declared.get("selected_operation_permission_not_recorded") is not True,
        True,
        operation_permission_basis.get("selected_operation_permission_recorded"),
        "SELECTED_OPERATION_PERMISSION_NOT_RECORDED",
    )
    _add_check(
        checks,
        "operation_permission_created",
        operation_permission_basis.get("operation_permission_created") is True
        and declared.get("operation_permission_not_created") is not True,
        True,
        operation_permission_basis.get("operation_permission_created"),
        "OPERATION_PERMISSION_NOT_CREATED",
    )
    _add_check(
        checks,
        "operation_permission_local_only",
        operation_permission_basis.get("operation_permission_local_only") is True
        and declared.get("operation_permission_local_only_not_true") is not True,
        True,
        operation_permission_basis.get("operation_permission_local_only"),
        "OPERATION_PERMISSION_LOCAL_ONLY_NOT_TRUE",
    )
    _add_check(
        checks,
        "operation_permission_read_only",
        operation_permission_basis.get("operation_permission_read_only") is True
        and declared.get("operation_permission_read_only_not_true") is not True,
        True,
        operation_permission_basis.get("operation_permission_read_only"),
        "OPERATION_PERMISSION_READ_ONLY_NOT_TRUE",
    )

    operation_execution_type = declared.get("operation_execution_type")
    _add_check(
        checks,
        "operation_execution_type_declared",
        operation_execution_type is not None
        and declared.get("operation_execution_type_missing") is not True,
        OPERATION_EXECUTION_TYPE,
        operation_execution_type,
        "OPERATION_EXECUTION_TYPE_MISSING",
    )
    _add_check(
        checks,
        "operation_execution_type_exact",
        operation_execution_type == OPERATION_EXECUTION_TYPE
        and declared.get(
            "operation_execution_type_not_local_relevance_medium_read_only_operation_execution"
        )
        is not True,
        OPERATION_EXECUTION_TYPE,
        operation_execution_type,
        "OPERATION_EXECUTION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
    )
    operation_execution_scope = declared.get("operation_execution_scope")
    _add_check(
        checks,
        "operation_execution_scope_declared",
        operation_execution_scope is not None
        and declared.get("operation_execution_scope_missing") is not True,
        OPERATION_EXECUTION_SCOPE,
        operation_execution_scope,
        "OPERATION_EXECUTION_SCOPE_MISSING",
    )
    _add_check(
        checks,
        "operation_execution_scope_exact",
        operation_execution_scope == OPERATION_EXECUTION_SCOPE
        and declared.get("operation_execution_scope_not_selected_operation_execution_only")
        is not True,
        OPERATION_EXECUTION_SCOPE,
        operation_execution_scope,
        "OPERATION_EXECUTION_SCOPE_NOT_SELECTED_OPERATION_EXECUTION_ONLY",
    )

    declared_operation_execution_recorded = declared.get(
        "local_relevance_medium_read_only_operation_execution_recorded",
        True,
    )
    _add_check(
        checks,
        "local_relevance_medium_read_only_operation_execution_recorded",
        declared_operation_execution_recorded is True
        and declared.get("local_relevance_medium_read_only_operation_execution_not_recorded")
        is not True,
        True,
        declared_operation_execution_recorded,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_NOT_RECORDED",
    )
    declared_operation_execution_created = declared.get("operation_execution_created", True)
    _add_check(
        checks,
        "operation_execution_created",
        declared_operation_execution_created is True
        and declared.get("operation_execution_not_created") is not True,
        True,
        declared_operation_execution_created,
        "OPERATION_EXECUTION_NOT_CREATED",
    )
    declared_operation_execution_performed = declared.get("operation_execution_performed", True)
    _add_check(
        checks,
        "operation_execution_performed",
        declared_operation_execution_performed is True
        and declared.get("operation_execution_not_performed") is not True,
        True,
        declared_operation_execution_performed,
        "OPERATION_EXECUTION_NOT_PERFORMED",
    )
    declared_operation_execution_local_only = declared.get(
        "operation_execution_local_only",
        True,
    )
    _add_check(
        checks,
        "operation_execution_local_only",
        declared_operation_execution_local_only is True
        and declared.get("operation_execution_local_only_not_true") is not True,
        True,
        declared_operation_execution_local_only,
        "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    )
    declared_operation_execution_read_only = declared.get(
        "operation_execution_read_only",
        True,
    )
    _add_check(
        checks,
        "operation_execution_read_only",
        declared_operation_execution_read_only is True
        and declared.get("operation_execution_read_only_not_true") is not True,
        True,
        declared_operation_execution_read_only,
        "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE",
    )

    _check_requested_false_fields(declared, checks)

    declared_non_claims = declared.get("declared_non_claims")
    _add_check(
        checks,
        "required_declared_non_claims_false",
        _declared_non_claims_passed(declared_non_claims),
        "all required non-claims present as false bool",
        declared_non_claims,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _add_check(
        checks,
        "raw_or_hidden_request_content_not_used",
        not _raw_or_hidden_content_present(declared),
        False,
        _raw_or_hidden_content_present(declared),
        "HIDDEN_REPO_STATE_USED_AS_OPERATION_EXECUTION_CONTENT",
    )
    predecessor_failure_preserved = not (
        declared.get("predecessor_failure_repaired") is True
        or declared.get("predecessor_failure_hidden") is True
        or declared.get("predecessor_failure_claimed_passed") is True
    )
    _add_check(
        checks,
        "predecessor_failure_evidence_preserved",
        predecessor_failure_preserved,
        True,
        predecessor_failure_preserved,
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _add_check(
        checks,
        "result_level_required_false_non_claims_canonical_false",
        all(value is False for value in _canonical_false_non_claims().values()),
        "canonical false result-level non-claims",
        _canonical_false_non_claims(),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    if _failed_checks(checks):
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif (
        declared.get("requested_local_relevance_medium_read_only_operation_execution_outcome")
        == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    ):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    else:
        outcome = OUTCOME_RECORDED

    return _build_result_artifact(
        declared,
        operation_execution_boundary_basis,
        operation_permission_basis,
        checks,
        outcome,
        declared.get("block_reason"),
    )


def resolve_local_relevance_medium_read_only_operation_execution_v0_min_from_path(
    declared_local_relevance_medium_read_only_operation_execution_path: Path | str,
) -> dict:
    """Resolve a declared operation-execution request from one JSON object path."""

    try:
        with Path(declared_local_relevance_medium_read_only_operation_execution_path).open(
            "r",
            encoding="utf-8",
        ) as handle:
            data = json.load(handle)
    except Exception as exc:
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_REQUEST_UNREADABLE",
            str(exc),
        )
    if not isinstance(data, MappingABC):
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_REQUEST_MALFORMED",
            "declared request JSON is not an object",
        )
    return resolve_local_relevance_medium_read_only_operation_execution_v0_min(data)


def build_local_relevance_medium_read_only_operation_execution_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build the bounded operation-execution summary view for a result artifact."""

    checks = list(
        result.get("local_relevance_medium_read_only_operation_execution_checks", [])
        if isinstance(
            result.get("local_relevance_medium_read_only_operation_execution_checks"),
            list,
        )
        else []
    )
    operation_execution = _mapping(
        result.get("local_relevance_medium_read_only_operation_execution")
    )
    statement = _mapping(
        result.get("local_relevance_medium_read_only_operation_execution_statement")
    )
    declared_question = _mapping(
        result.get("declared_local_relevance_medium_read_only_operation_execution_question")
    )
    block = _mapping(result.get("block"))
    non_claims = _mapping(result.get("non_claims"))
    failed_check_count = len(_failed_checks(checks))
    passed_check_count = _passed_count_from_checks(checks)

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "operation_execution_id": operation_execution.get("operation_execution_id"),
        "question": declared_question.get("question"),
        "intent": declared_question.get("intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "local_relevance_medium_read_only_operation_execution_recorded": statement.get(
            "local_relevance_medium_read_only_operation_execution_recorded"
        )
        is True,
        "basis_operation_execution_boundary_artifact_preserved": statement.get(
            "basis_operation_execution_boundary_artifact_preserved"
        )
        is True,
        "basis_operation_permission_artifact_preserved": statement.get(
            "basis_operation_permission_artifact_preserved"
        )
        is True,
        "selected_command": operation_execution.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved") is True,
        "selected_command_is_state": statement.get("selected_command_is_state") is True,
        "selected_operation_permission_recorded": statement.get(
            "selected_operation_permission_recorded"
        )
        is True,
        "operation_permission_created": statement.get("operation_permission_created") is True,
        "operation_permission_local_only": statement.get("operation_permission_local_only")
        is True,
        "operation_permission_read_only": statement.get("operation_permission_read_only")
        is True,
        "operation_execution_created": statement.get("operation_execution_created") is True,
        "operation_execution_performed": statement.get("operation_execution_performed")
        is True,
        "operation_execution_local_only": statement.get("operation_execution_local_only")
        is True,
        "operation_execution_read_only": statement.get("operation_execution_read_only")
        is True,
        "operation_execution_object_summary": {
            "operation_execution_type": operation_execution.get("operation_execution_type"),
            "operation_execution_scope": operation_execution.get("operation_execution_scope"),
            "operation_execution_version": operation_execution.get(
                "operation_execution_version"
            ),
            "selected_command": operation_execution.get("selected_command"),
            "operation_execution_created": operation_execution.get(
                "operation_execution_created"
            ),
            "operation_execution_performed": operation_execution.get(
                "operation_execution_performed"
            ),
            "operation_execution_local_only": operation_execution.get(
                "operation_execution_local_only"
            ),
            "operation_execution_read_only": operation_execution.get(
                "operation_execution_read_only"
            ),
        },
        "runtime_permission_not_created": operation_execution.get(
            "runtime_permission_created"
        )
        is False,
        "public_api_not_created": operation_execution.get("public_api_created") is False,
        "participant_facing_interface_not_created": operation_execution.get(
            "participant_facing_interface_created"
        )
        is False,
        "distributed_network_behavior_not_created": operation_execution.get(
            "distributed_network_behavior_created"
        )
        is False,
        "general_operation_permission_not_created": operation_execution.get(
            "general_operation_permission_created"
        )
        is False,
        "general_lookup_permission_not_created": operation_execution.get(
            "general_lookup_permission_created"
        )
        is False,
        "arbitrary_lookup_permission_not_created": operation_execution.get(
            "arbitrary_lookup_permission_created"
        )
        is False,
        "unsupported_commands_not_permitted": operation_execution.get(
            "unsupported_commands_permitted"
        )
        is False,
        "unsupported_lookup_keys_not_permitted": operation_execution.get(
            "unsupported_lookup_keys_permitted"
        )
        is False,
        "no_new_lookup_entry_created_beyond_bounded_lookup_result_object": (
            operation_execution.get("new_lookup_entry_created") is False
        ),
        "no_new_signal_entry_relevance_object_or_index_entry_created": all(
            operation_execution.get(field) is False
            for field in (
                "new_signal_accepted",
                "new_entry_accepted",
                "new_relevance_object_created",
                "new_index_entry_created",
            )
        ),
        "filesystem_discovery_not_performed": operation_execution.get(
            "filesystem_discovery_performed"
        )
        is False,
        "registry_search_query_surface_and_ranking_not_created": all(
            operation_execution.get(field) is False
            for field in (
                "registry_created",
                "search_surface_created",
                "query_surface_created",
                "ranking_surface_created",
            )
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": all(
            operation_execution.get(field) is False
            for field in (
                "scoring_surface_created",
                "priority_surface_created",
                "validity_judgment_created",
                "truth_judgment_created",
                "authority_judgment_created",
                "currentness_judgment_created",
            )
        ),
        "repeated_reception_permission_arbitrary_reception_and_feed_not_created": all(
            operation_execution.get(field) is False
            for field in (
                "repeated_reception_permission_created",
                "arbitrary_reception_created",
                "feed_created",
            )
        ),
        "source_authority_currentness_truth_synchronization_participation_not_created": all(
            operation_execution.get(field) is False
            for field in (
                "source_transfer_occurred",
                "source_receipt_occurred",
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
        "authorization_token_reuse_blocked": statement.get(
            "authorization_token_reuse_blocked"
        )
        is True,
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved"
        )
        is True,
        "follow_on_not_created": operation_execution.get("follow_on_work_authorized") is False,
        "key_non_claims": {
            "runtime_permission_created": non_claims.get("runtime_permission_created"),
            "public_api_created": non_claims.get("public_api_created"),
            "distributed_network_behavior_created": non_claims.get(
                "distributed_network_behavior_created"
            ),
            "follow_on_work_authorized": non_claims.get("follow_on_work_authorized"),
            "consumed_request_reopened": non_claims.get("consumed_request_reopened"),
            "authorization_token_reused": non_claims.get("authorization_token_reused"),
        },
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _safe_filename_stem(value: Any) -> str:
    safe = str(value or DEFAULT_OPERATION_EXECUTION_ID)
    safe = safe.replace("/", "_").replace("\\", "_").replace(" ", "_")
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe.strip("._-") or DEFAULT_OPERATION_EXECUTION_ID


def write_local_relevance_medium_read_only_operation_execution_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one operation-execution result artifact without overwrite."""

    operation_execution = _mapping(
        result.get("local_relevance_medium_read_only_operation_execution")
    )
    operation_execution_id = _safe_filename_stem(
        operation_execution.get("operation_execution_id", DEFAULT_OPERATION_EXECUTION_ID)
    )
    if output_path is None:
        target = OUTPUT_ROOT / (
            f"{operation_execution_id}__"
            "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
        )
    else:
        target = Path(output_path)

    target.parent.mkdir(parents=True, exist_ok=True)
    final_target = target
    if final_target.exists():
        stem = target.stem
        suffix = target.suffix
        counter = 1
        while final_target.exists():
            final_target = target.with_name(f"{stem}_{counter:03d}{suffix}")
            counter += 1

    with final_target.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return final_target


def build_declared_local_relevance_medium_read_only_operation_execution_v0_min_request(
    *,
    local_relevance_medium_read_only_operation_execution_id: str = (
        DEFAULT_OPERATION_EXECUTION_ID
    ),
    selected_operation_execution_boundary_artifact: Path | str = (
        DEFAULT_OPERATION_EXECUTION_BOUNDARY_ARTIFACT
    ),
    selected_operation_permission_artifact: Path | str = DEFAULT_OPERATION_PERMISSION_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    operation_execution_type: str = OPERATION_EXECUTION_TYPE,
    operation_execution_scope: str = OPERATION_EXECUTION_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared request for one selected-state operation execution."""

    if selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyOperationExecutionV0MinError(
            "selected_command must be exactly state"
        )
    non_claims = _canonical_false_non_claims()
    if declared_non_claims is not None:
        non_claims.update(dict(declared_non_claims))

    request: dict[str, Any] = {
        "local_relevance_medium_read_only_operation_execution_id": (
            local_relevance_medium_read_only_operation_execution_id
        ),
        "local_relevance_medium_read_only_operation_execution_question": CORE_QUESTION,
        "local_relevance_medium_read_only_operation_execution_intent": intent,
        "selected_operation_execution_boundary_artifact": str(
            selected_operation_execution_boundary_artifact
        ),
        "selected_operation_permission_artifact": str(
            selected_operation_permission_artifact
        ),
        "selected_command": selected_command,
        "operation_execution_type": operation_execution_type,
        "operation_execution_scope": operation_execution_scope,
        "selected_operation_permission_recorded": True,
        "operation_permission_created": True,
        "operation_permission_local_only": True,
        "operation_permission_read_only": True,
        "local_relevance_medium_read_only_operation_execution_recorded": True,
        "operation_execution_created": True,
        "operation_execution_performed": True,
        "operation_execution_local_only": True,
        "operation_execution_read_only": True,
        "declared_non_claims": non_claims,
    }
    request.update(overrides)
    return _sanitize(request)
