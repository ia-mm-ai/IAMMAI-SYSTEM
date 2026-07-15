"""Resolve one local read-only selected-state lookup result boundary.

This resolver reads one clean
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED artifact as selected-state
lookup-performed basis. It records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY object only.

The object is boundary-shaped, local, read-only,
selected-state-lookup-result-consideration-only, closure-token-aware,
non-lookup-result-shaped, and non-operation-shaped. It may record that one
future local read-only lookup result may be considered as a separately bounded
step. It does not create lookup result, operation permission, runtime
permission, public or distributed surfaces, unsupported commands or keys,
registry/search/query/ranking surfaces, filesystem discovery, source movement,
or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyLookupResultBoundaryV0MinError(RuntimeError):
    """Bounded resolver error for lookup result boundary handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_result_boundary_v0_min"
)
DEFAULT_LOOKUP_PERFORMED_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_performed_v0_min/"
    "local_relevance_medium_read_only_lookup_performed_reference_review_001__"
    "local_relevance_medium_read_only_lookup_performed_v0_min_result.json"
)

DEFAULT_BOUNDARY_ID = "local_relevance_medium_read_only_lookup_result_boundary_001"
BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_LOOKUP_RESULT_CONSIDERATION_ONLY"
SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)
SELECTED_COMMAND = "state"

LOOKUP_PERFORMED_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_RECORDED"
)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED for "
    "selected command state, existing reusable read-only lookup permission, and "
    "prior lookup-pair coverage, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY be recorded that "
    "permits a future local read-only lookup result to be considered as a "
    "separately bounded step, without creating lookup result, creating operation "
    "permission, creating runtime permission, creating public API, creating "
    "participant-facing interface, creating distributed network behavior, "
    "creating general lookup permission, creating arbitrary lookup permission, "
    "permitting unsupported commands, permitting unsupported lookup keys, "
    "creating new lookup entry, accepting new entries, accepting new signals, "
    "performing filesystem discovery, creating query surface, registry, search, "
    "ranking, scoring, priority, validity judgment, truth judgment, authority, "
    "currentness, synchronization, participation authorization, participant role, "
    "repeated reception permission, arbitrary reception, feed, source transfer, "
    "source receipt, or follow-on work?"
)

BOUNDARY_OBJECT_FALSE_FIELDS = (
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
    "artifact_existence_treated_as_lookup_result_boundary_authority",
    "latest_file_posture_treated_as_lookup_result_boundary_authority",
    "repo_local_availability_treated_as_lookup_result_boundary_authority",
    "hidden_repo_state_used_as_lookup_result_boundary_content",
    "hidden_repo_state_used_as_lookup_result_boundary_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

REQUIRED_FALSE_NON_CLAIMS = BOUNDARY_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_lookup_result_boundary_recorded",
    "basis_lookup_performed_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_lookup_performed_recorded",
    "lookup_performed",
    "lookup_performed_local_only",
    "lookup_performed_read_only",
    "future_lookup_result_may_be_considered",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_BLOCK_REQUESTED",
    "LOOKUP_PERFORMED_ARTIFACT_PATH_MISSING",
    "LOOKUP_PERFORMED_ARTIFACT_UNREADABLE",
    "LOOKUP_PERFORMED_ARTIFACT_NOT_JSON_OBJECT",
    "LOOKUP_PERFORMED_ARTIFACT_NOT_RECORDED",
    "LOOKUP_PERFORMED_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOOKUP_PERFORMED_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_LOOKUP_PERFORMED_NOT_RECORDED",
    "LOOKUP_NOT_PERFORMED",
    "LOOKUP_PERFORMED_LOCAL_ONLY_NOT_TRUE",
    "LOOKUP_PERFORMED_READ_ONLY_NOT_TRUE",
    "FUTURE_LOOKUP_RESULT_MAY_NOT_BE_CONSIDERED",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_SELECTED_LOOKUP_RESULT_CONSIDERATION_ONLY",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_LOOKUP_RESULT_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_LOOKUP_RESULT_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_LOOKUP_RESULT_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_LOOKUP_RESULT_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_LOOKUP_RESULT_BOUNDARY_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_REQUEST_UNREADABLE",
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
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "artifact_existence_treated_as_lookup_result_boundary_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_LOOKUP_RESULT_BOUNDARY_AUTHORITY"
    ),
    "latest_file_posture_treated_as_lookup_result_boundary_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_LOOKUP_RESULT_BOUNDARY_AUTHORITY"
    ),
    "repo_local_availability_treated_as_lookup_result_boundary_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_LOOKUP_RESULT_BOUNDARY_AUTHORITY"
    ),
    "hidden_repo_state_used_as_lookup_result_boundary_content": (
        "HIDDEN_REPO_STATE_USED_AS_LOOKUP_RESULT_BOUNDARY_CONTENT"
    ),
    "hidden_repo_state_used_as_lookup_result_boundary_authority": (
        "HIDDEN_REPO_STATE_USED_AS_LOOKUP_RESULT_BOUNDARY_AUTHORITY"
    ),
    "prior_artifacts_mutated": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
}

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_lookup_result_boundary_body",
    "raw_lookup_result_body",
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
    "lookup_result_boundary_body",
    "lookup_result_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
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

OFFICIAL_VALUES = {
    RESULT_VERSION,
    RESOLVER_MODULE,
    BOUNDARY_TYPE,
    BOUNDARY_SCOPE,
    SELECTED_COMMAND,
    LOOKUP_PERFORMED_RECORDED_OUTCOME,
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


def _extract_lookup_performed_basis(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    if artifact is None:
        return {}
    performed = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_performed"
    )
    statement = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_performed_statement"
    )
    summary = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_performed_summary"
    )
    metadata = _mapping_section(
        artifact, "local_relevance_medium_read_only_lookup_performed_metadata"
    )
    return {
        "outcome": _first_present(artifact.get("outcome"), summary.get("outcome")),
        "result_version": _first_present(
            summary.get("result_version"),
            metadata.get("result_version"),
            metadata.get("local_relevance_medium_read_only_lookup_performed_version"),
            performed.get("lookup_performed_version"),
            artifact.get("result_version"),
        ),
        "failed_check_count": _artifact_failed_check_count(
            artifact, "local_relevance_medium_read_only_lookup_performed_checks"
        ),
        "selected_command": _first_present(
            performed.get("selected_command"),
            summary.get("selected_command"),
            statement.get("selected_command"),
        ),
        "selected_command_is_state": _artifact_bool(
            performed.get("selected_command_is_state"),
            summary.get("selected_command_is_state"),
            statement.get("selected_command_is_state"),
        ),
        "selected_lookup_performed_recorded": _artifact_bool(
            performed.get("local_relevance_medium_read_only_lookup_performed_recorded"),
            summary.get("lookup_performed_recorded"),
            summary.get("local_relevance_medium_read_only_lookup_performed_recorded"),
            statement.get("local_relevance_medium_read_only_lookup_performed_recorded"),
        ),
        "lookup_performed": _artifact_bool(
            performed.get("lookup_performed"),
            summary.get("lookup_performed"),
            statement.get("lookup_performed"),
        ),
        "lookup_performed_local_only": _artifact_bool(
            performed.get("lookup_performed_local_only"),
            summary.get("lookup_performed_local_only"),
            statement.get("lookup_performed_local_only"),
        ),
        "lookup_performed_read_only": _artifact_bool(
            performed.get("lookup_performed_read_only"),
            summary.get("lookup_performed_read_only"),
            statement.get("lookup_performed_read_only"),
        ),
        "lookup_result_created": _artifact_bool(
            performed.get("lookup_result_created"),
            summary.get("lookup_result_created"),
        ),
        "performed_object": performed,
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
    if isinstance(result_or_checks, MappingABC):
        checks = result_or_checks.get(
            "local_relevance_medium_read_only_lookup_result_boundary_checks"
        )
    else:
        checks = result_or_checks
    if not isinstance(checks, list):
        return 0
    return sum(
        1 for check in checks if isinstance(check, MappingABC) and check.get("passed") is False
    )


def _passed_check_count(result_or_checks: Mapping[str, Any] | list[Any]) -> int:
    if isinstance(result_or_checks, MappingABC):
        checks = result_or_checks.get(
            "local_relevance_medium_read_only_lookup_result_boundary_checks"
        )
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


def _false_field_actual(
    request: Mapping[str, Any], field: str, *basis_maps: Mapping[str, Any]
) -> Any:
    if request.get(field) is True:
        return True
    for basis in basis_maps:
        if basis.get(field) is True:
            return True
    return False


def _build_boundary_object(
    *,
    boundary_id: str,
    recorded: bool,
    selected_lookup_performed_artifact: Path | None,
    lookup_performed_basis: Mapping[str, Any],
    selected_command: Any,
) -> dict[str, Any]:
    selected_command_value = SELECTED_COMMAND if selected_command == SELECTED_COMMAND else None
    boundary = {
        "boundary_id": boundary_id,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "basis_lookup_performed_artifact": (
            str(selected_lookup_performed_artifact)
            if selected_lookup_performed_artifact is not None
            else None
        ),
        "basis_lookup_performed_outcome": lookup_performed_basis.get("outcome"),
        "basis_lookup_performed_result_version": lookup_performed_basis.get(
            "result_version"
        ),
        "basis_lookup_performed_failed_check_count": lookup_performed_basis.get(
            "failed_check_count"
        ),
        "selected_command": selected_command_value,
        "selected_command_is_state": recorded and selected_command_value == SELECTED_COMMAND,
        "selected_lookup_performed_recorded": recorded
        and lookup_performed_basis.get("selected_lookup_performed_recorded") is True,
        "lookup_performed": recorded
        and lookup_performed_basis.get("lookup_performed") is True,
        "lookup_performed_local_only": recorded
        and lookup_performed_basis.get("lookup_performed_local_only") is True,
        "lookup_performed_read_only": recorded
        and lookup_performed_basis.get("lookup_performed_read_only") is True,
        "future_lookup_result_may_be_considered": recorded,
    }
    for field in BOUNDARY_OBJECT_FALSE_FIELDS:
        boundary[field] = False
    return boundary


def _build_statement(
    *,
    recorded: bool,
    lookup_performed_artifact_preserved: bool,
    selected_command: Any,
    lookup_performed_basis: Mapping[str, Any],
) -> dict[str, bool]:
    if not recorded:
        return {key: False for key in ALLOWED_TRUE_RECORDED_FIELDS}
    selected_command_is_state = selected_command == SELECTED_COMMAND
    return {
        "local_relevance_medium_read_only_lookup_result_boundary_recorded": True,
        "basis_lookup_performed_artifact_preserved": lookup_performed_artifact_preserved,
        "selected_command_preserved": selected_command_is_state,
        "selected_command_is_state": selected_command_is_state,
        "selected_lookup_performed_recorded": lookup_performed_basis.get(
            "selected_lookup_performed_recorded"
        )
        is True,
        "lookup_performed": lookup_performed_basis.get("lookup_performed") is True,
        "lookup_performed_local_only": lookup_performed_basis.get(
            "lookup_performed_local_only"
        )
        is True,
        "lookup_performed_read_only": lookup_performed_basis.get(
            "lookup_performed_read_only"
        )
        is True,
        "future_lookup_result_may_be_considered": True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "lookup_result_boundary_only": True,
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
            "local_relevance_medium_read_only_lookup_result_boundary_id": request.get(
                "local_relevance_medium_read_only_lookup_result_boundary_id"
            ),
            "local_relevance_medium_read_only_lookup_result_boundary_question": request.get(
                "local_relevance_medium_read_only_lookup_result_boundary_question"
            ),
            "local_relevance_medium_read_only_lookup_result_boundary_intent": request.get(
                "local_relevance_medium_read_only_lookup_result_boundary_intent"
            ),
            "selected_lookup_performed_artifact": request.get(
                "selected_lookup_performed_artifact"
            ),
            "selected_command": request.get("selected_command"),
            "boundary_type": request.get("boundary_type"),
            "boundary_scope": request.get("boundary_scope"),
        }
    )


def _build_lookup_performed_basis_section(
    path: Path | None,
    basis: Mapping[str, Any],
    artifact_preserved: bool,
) -> dict[str, Any]:
    return {
        "selected_lookup_performed_artifact": str(path) if path is not None else None,
        "basis_lookup_performed_artifact_preserved": artifact_preserved,
        "basis_lookup_performed_outcome": basis.get("outcome"),
        "basis_lookup_performed_result_version": basis.get("result_version"),
        "basis_lookup_performed_failed_check_count": basis.get("failed_check_count"),
        "basis_lookup_performed_selected_command": basis.get("selected_command"),
        "selected_lookup_performed_recorded": basis.get(
            "selected_lookup_performed_recorded"
        )
        is True,
        "lookup_performed": basis.get("lookup_performed") is True,
        "lookup_performed_local_only": basis.get("lookup_performed_local_only") is True,
        "lookup_performed_read_only": basis.get("lookup_performed_read_only") is True,
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
    boundary = _mapping_section(
        result, "local_relevance_medium_read_only_lookup_result_boundary"
    )
    statement = _mapping_section(
        result, "local_relevance_medium_read_only_lookup_result_boundary_statement"
    )
    question = _mapping_section(
        result, "declared_local_relevance_medium_read_only_lookup_result_boundary_question"
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
        "boundary_id": boundary.get("boundary_id"),
        "question": question.get(
            "local_relevance_medium_read_only_lookup_result_boundary_question"
        ),
        "intent": question.get(
            "local_relevance_medium_read_only_lookup_result_boundary_intent"
        ),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "boundary_recorded": statement.get(
            "local_relevance_medium_read_only_lookup_result_boundary_recorded"
        )
        is True,
        "basis_lookup_performed_artifact_preserved": statement.get(
            "basis_lookup_performed_artifact_preserved"
        )
        is True,
        "selected_command": boundary.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved") is True,
        "selected_command_is_state": statement.get("selected_command_is_state") is True,
        "selected_lookup_performed_recorded": statement.get(
            "selected_lookup_performed_recorded"
        )
        is True,
        "lookup_performed": statement.get("lookup_performed") is True,
        "lookup_performed_local_only": statement.get("lookup_performed_local_only") is True,
        "lookup_performed_read_only": statement.get("lookup_performed_read_only") is True,
        "future_lookup_result_may_be_considered": statement.get(
            "future_lookup_result_may_be_considered"
        )
        is True,
        "boundary_object_summary": {
            "boundary_type": boundary.get("boundary_type"),
            "boundary_scope": boundary.get("boundary_scope"),
            "basis_lookup_performed_artifact": boundary.get("basis_lookup_performed_artifact"),
            "selected_command": boundary.get("selected_command"),
            "future_lookup_result_may_be_considered": boundary.get(
                "future_lookup_result_may_be_considered"
            )
            is True,
            "lookup_result_created": boundary.get("lookup_result_created") is True,
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


def build_local_relevance_medium_read_only_lookup_result_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact deterministic summary for a lookup-result-boundary result."""

    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyLookupResultBoundaryV0MinError(
            "result must be a mapping"
        )
    return _build_summary_from_result(result)


def _add_checks(
    *,
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    selected_lookup_performed_artifact: Path | None,
    lookup_performed_read_code: str | None,
    lookup_performed_basis: Mapping[str, Any],
) -> None:
    question = request.get("local_relevance_medium_read_only_lookup_result_boundary_question")
    intent = request.get("local_relevance_medium_read_only_lookup_result_boundary_intent")
    selected_command = request.get("selected_command")
    boundary_type = request.get("boundary_type")
    boundary_scope = request.get("boundary_scope")
    performed_object = lookup_performed_basis.get("performed_object")
    if not isinstance(performed_object, MappingABC):
        performed_object = {}

    checks.append(
        _check(
            "lookup result boundary question declared",
            isinstance(question, str) and bool(question.strip()),
            "declared lookup result boundary question",
            question,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "boundary intent supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "lookup result boundary block not requested",
            intent != INTENT_BLOCK,
            "no explicit lookup result boundary block request",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_BLOCK_REQUESTED",
        )
    )
    checks.append(
        _check(
            "lookup performed artifact path declared",
            selected_lookup_performed_artifact is not None,
            "declared lookup performed artifact path",
            selected_lookup_performed_artifact,
            "LOOKUP_PERFORMED_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _check(
            "lookup performed artifact readable JSON object",
            lookup_performed_read_code is None,
            "readable JSON object",
            lookup_performed_read_code,
            lookup_performed_read_code or "LOOKUP_PERFORMED_ARTIFACT_UNREADABLE",
        )
    )
    lookup_performed_not_recorded = request.get("lookup_performed_artifact_not_recorded") is True
    checks.append(
        _check(
            "lookup performed artifact outcome recorded",
            (
                not lookup_performed_not_recorded
                and lookup_performed_basis.get("outcome") == LOOKUP_PERFORMED_RECORDED_OUTCOME
            ),
            LOOKUP_PERFORMED_RECORDED_OUTCOME,
            lookup_performed_basis.get("outcome"),
            "LOOKUP_PERFORMED_ARTIFACT_NOT_RECORDED",
        )
    )
    lookup_performed_version_bad = (
        request.get("lookup_performed_artifact_version_not_0_1_0") is True
    )
    checks.append(
        _check(
            "lookup performed artifact result version 0.1.0",
            (
                not lookup_performed_version_bad
                and lookup_performed_basis.get("result_version") == RESULT_VERSION
            ),
            RESULT_VERSION,
            lookup_performed_basis.get("result_version"),
            "LOOKUP_PERFORMED_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    lookup_performed_failed = (
        request.get("lookup_performed_artifact_failed_checks_present") is True
    )
    checks.append(
        _check(
            "lookup performed artifact failed check count zero",
            (
                not lookup_performed_failed
                and lookup_performed_basis.get("failed_check_count") == 0
            ),
            0,
            lookup_performed_basis.get("failed_check_count"),
            "LOOKUP_PERFORMED_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "selected command declared",
            request.get("selected_command_missing") is not True and selected_command is not None,
            SELECTED_COMMAND,
            selected_command,
            "SELECTED_COMMAND_MISSING",
        )
    )
    selected_command_is_state = (
        request.get("selected_command_not_state") is not True
        and selected_command == SELECTED_COMMAND
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
                and lookup_performed_basis.get("selected_command") == SELECTED_COMMAND
                and lookup_performed_basis.get("selected_command_is_state") is True
            ),
            "selected command state in request and lookup performed basis",
            {
                "request_selected_command": selected_command,
                "basis_selected_command": lookup_performed_basis.get("selected_command"),
                "basis_selected_command_is_state": lookup_performed_basis.get(
                    "selected_command_is_state"
                ),
            },
            "SELECTED_COMMAND_NOT_STATE",
        )
    )
    checks.append(
        _check(
            "selected lookup performed recorded",
            (
                request.get("selected_lookup_performed_not_recorded") is not True
                and lookup_performed_basis.get("selected_lookup_performed_recorded") is True
            ),
            True,
            lookup_performed_basis.get("selected_lookup_performed_recorded"),
            "SELECTED_LOOKUP_PERFORMED_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "lookup performed true",
            (
                request.get("lookup_not_performed") is not True
                and lookup_performed_basis.get("lookup_performed") is True
            ),
            True,
            lookup_performed_basis.get("lookup_performed"),
            "LOOKUP_NOT_PERFORMED",
        )
    )
    checks.append(
        _check(
            "lookup performed local only",
            (
                request.get("lookup_performed_local_only_not_true") is not True
                and lookup_performed_basis.get("lookup_performed_local_only") is True
            ),
            True,
            lookup_performed_basis.get("lookup_performed_local_only"),
            "LOOKUP_PERFORMED_LOCAL_ONLY_NOT_TRUE",
        )
    )
    checks.append(
        _check(
            "lookup performed read only",
            (
                request.get("lookup_performed_read_only_not_true") is not True
                and lookup_performed_basis.get("lookup_performed_read_only") is True
            ),
            True,
            lookup_performed_basis.get("lookup_performed_read_only"),
            "LOOKUP_PERFORMED_READ_ONLY_NOT_TRUE",
        )
    )
    checks.append(
        _check(
            "future lookup result may be considered",
            request.get("future_lookup_result_may_not_be_considered") is not True,
            True,
            request.get("future_lookup_result_may_not_be_considered") is not True,
            "FUTURE_LOOKUP_RESULT_MAY_NOT_BE_CONSIDERED",
        )
    )
    checks.append(
        _check(
            "boundary type declared",
            boundary_type is not None,
            BOUNDARY_TYPE,
            boundary_type,
            "BOUNDARY_TYPE_MISSING",
        )
    )
    checks.append(
        _check(
            "boundary type exact",
            (
                request.get(
                    "boundary_type_not_local_relevance_medium_read_only_lookup_result_boundary"
                )
                is not True
                and boundary_type == BOUNDARY_TYPE
            ),
            BOUNDARY_TYPE,
            boundary_type,
            "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY",
        )
    )
    checks.append(
        _check(
            "boundary scope declared",
            boundary_scope is not None,
            BOUNDARY_SCOPE,
            boundary_scope,
            "BOUNDARY_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "boundary scope selected lookup result consideration only",
            (
                request.get("boundary_scope_not_selected_lookup_result_consideration_only")
                is not True
                and boundary_scope == BOUNDARY_SCOPE
            ),
            BOUNDARY_SCOPE,
            boundary_scope,
            "BOUNDARY_SCOPE_NOT_SELECTED_LOOKUP_RESULT_CONSIDERATION_ONLY",
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
        actual = _false_field_actual(request, field, performed_object)
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
    boundary_id = str(
        request_copy.get(
            "local_relevance_medium_read_only_lookup_result_boundary_id",
            DEFAULT_BOUNDARY_ID,
        )
        or DEFAULT_BOUNDARY_ID
    )
    selected_lookup_performed_path = None
    if request_copy.get("lookup_performed_artifact_missing") is not True:
        selected_lookup_performed_path = _as_path(
            request_copy.get("selected_lookup_performed_artifact")
        )

    lookup_performed_artifact: dict[str, Any] | None = None
    lookup_performed_read_code: str | None = "LOOKUP_PERFORMED_ARTIFACT_PATH_MISSING"
    if selected_lookup_performed_path is not None:
        lookup_performed_artifact, lookup_performed_read_code = _read_json_object(
            selected_lookup_performed_path,
            "LOOKUP_PERFORMED_ARTIFACT_UNREADABLE",
            "LOOKUP_PERFORMED_ARTIFACT_NOT_JSON_OBJECT",
        )

    lookup_performed_basis = _extract_lookup_performed_basis(lookup_performed_artifact)
    checks: list[dict[str, Any]] = []
    _add_checks(
        request=request_copy,
        checks=checks,
        selected_lookup_performed_artifact=selected_lookup_performed_path,
        lookup_performed_read_code=lookup_performed_read_code,
        lookup_performed_basis=lookup_performed_basis,
    )

    failure_code = _first_failure_code(checks)
    if failure_code is not None:
        outcome = OUTCOME_BLOCKED
    elif request_copy.get(
        "requested_local_relevance_medium_read_only_lookup_result_boundary_outcome"
    ) == OUTCOME_REQUIRES_ADDITIONAL_BASIS or bool(
        request_copy.get("additional_basis_context")
    ):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif request_copy.get("local_relevance_medium_read_only_lookup_result_boundary_intent") == (
        INTENT_DO_NOT_RECORD
    ):
        outcome = OUTCOME_NOT_RECORDED
    else:
        outcome = OUTCOME_RECORDED

    recorded = outcome == OUTCOME_RECORDED
    selected_command = request_copy.get("selected_command")
    boundary = _build_boundary_object(
        boundary_id=boundary_id,
        recorded=recorded,
        selected_lookup_performed_artifact=selected_lookup_performed_path,
        lookup_performed_basis=lookup_performed_basis,
        selected_command=selected_command,
    )
    statement = _build_statement(
        recorded=recorded,
        lookup_performed_artifact_preserved=selected_lookup_performed_path is not None
        and lookup_performed_read_code is None,
        selected_command=selected_command,
        lookup_performed_basis=lookup_performed_basis,
    )
    block = _block_record(failure_code, request_copy.get("block_reason"))
    metadata = {
        "local_relevance_medium_read_only_lookup_result_boundary_id": boundary_id,
        "local_relevance_medium_read_only_lookup_result_boundary_type": BOUNDARY_TYPE,
        "local_relevance_medium_read_only_lookup_result_boundary_version": RESULT_VERSION,
        "generated_at": _utc_timestamp(),
        "resolver_module": RESOLVER_MODULE,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_lookup_result_boundary_metadata": metadata,
        "declared_local_relevance_medium_read_only_lookup_result_boundary_question": (
            _build_declared_question_section(request_copy)
        ),
        "selected_lookup_performed_artifact_basis": _build_lookup_performed_basis_section(
            selected_lookup_performed_path,
            lookup_performed_basis,
            selected_lookup_performed_path is not None and lookup_performed_read_code is None,
        ),
        "local_relevance_medium_read_only_lookup_result_boundary": boundary,
        "local_relevance_medium_read_only_lookup_result_boundary_checks": checks,
        "local_relevance_medium_read_only_lookup_result_boundary_statement": statement,
        "local_relevance_medium_read_only_lookup_result_boundary_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": (
            _sanitize(request_copy.get("additional_basis_context"))
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else None
        ),
        "not_recorded_basis": (
            _sanitize(
                request_copy.get(
                    "not_recorded_basis",
                    "lookup result boundary not recorded by request",
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
    result["local_relevance_medium_read_only_lookup_result_boundary_summary"] = (
        _build_summary_from_result(result)
    )
    return result


def _blocked_malformed_result(code: str, reason: str) -> dict[str, Any]:
    checks = [
        _check(
            "declared local relevance medium read-only lookup result boundary request mapping",
            False,
            "mapping request",
            reason,
            code,
        )
    ]
    boundary = _build_boundary_object(
        boundary_id=DEFAULT_BOUNDARY_ID,
        recorded=False,
        selected_lookup_performed_artifact=None,
        lookup_performed_basis={},
        selected_command=None,
    )
    statement = _build_statement(
        recorded=False,
        lookup_performed_artifact_preserved=False,
        selected_command=None,
        lookup_performed_basis={},
    )
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_lookup_result_boundary_metadata": {
            "local_relevance_medium_read_only_lookup_result_boundary_id": (
                DEFAULT_BOUNDARY_ID
            ),
            "local_relevance_medium_read_only_lookup_result_boundary_type": BOUNDARY_TYPE,
            "local_relevance_medium_read_only_lookup_result_boundary_version": RESULT_VERSION,
            "generated_at": _utc_timestamp(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_local_relevance_medium_read_only_lookup_result_boundary_question": {},
        "selected_lookup_performed_artifact_basis": _build_lookup_performed_basis_section(
            None, {}, False
        ),
        "local_relevance_medium_read_only_lookup_result_boundary": boundary,
        "local_relevance_medium_read_only_lookup_result_boundary_checks": checks,
        "local_relevance_medium_read_only_lookup_result_boundary_statement": statement,
        "local_relevance_medium_read_only_lookup_result_boundary_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": None,
        "not_recorded_basis": None,
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_false_non_claims(),
        "outcome": OUTCOME_BLOCKED,
        "block": _block_record(code, reason),
    }
    result["local_relevance_medium_read_only_lookup_result_boundary_summary"] = (
        _build_summary_from_result(result)
    )
    return result


def resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min(
    declared_local_relevance_medium_read_only_lookup_result_boundary: (
        Mapping[str, Any] | None
    ) = None,
) -> dict[str, Any]:
    """Resolve one selected-state local read-only lookup result boundary request."""

    if declared_local_relevance_medium_read_only_lookup_result_boundary is None:
        declared_local_relevance_medium_read_only_lookup_result_boundary = (
            build_declared_local_relevance_medium_read_only_lookup_result_boundary_v0_min_request()
        )
    if not isinstance(
        declared_local_relevance_medium_read_only_lookup_result_boundary, MappingABC
    ):
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_REQUEST_MALFORMED",
            "declared request is not a mapping",
        )
    return _resolve_from_mapping(
        declared_local_relevance_medium_read_only_lookup_result_boundary
    )


def resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min_from_path(
    declared_local_relevance_medium_read_only_lookup_result_boundary_path: Path | str,
) -> dict[str, Any]:
    """Read a declared lookup-result-boundary request JSON file and resolve it."""

    try:
        parsed = json.loads(
            Path(
                declared_local_relevance_medium_read_only_lookup_result_boundary_path
            ).read_text(encoding="utf-8")
        )
    except (OSError, json.JSONDecodeError) as exc:
        raise LocalRelevanceMediumReadOnlyLookupResultBoundaryV0MinError(
            "declared lookup result boundary request path is unreadable"
        ) from exc
    if not isinstance(parsed, MappingABC):
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_REQUEST_MALFORMED",
            "declared request JSON is not an object",
        )
    return resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min(parsed)


def _result_boundary_id(result: Mapping[str, Any]) -> str:
    boundary = _mapping_section(
        result, "local_relevance_medium_read_only_lookup_result_boundary"
    )
    metadata = _mapping_section(
        result, "local_relevance_medium_read_only_lookup_result_boundary_metadata"
    )
    value = _first_present(
        boundary.get("boundary_id"),
        metadata.get("local_relevance_medium_read_only_lookup_result_boundary_id"),
        DEFAULT_BOUNDARY_ID,
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


def write_local_relevance_medium_read_only_lookup_result_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a lookup-result-boundary resolver result without overwriting."""

    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyLookupResultBoundaryV0MinError(
            "result must be a mapping"
        )
    filename = (
        f"{_result_boundary_id(result)}__"
        "local_relevance_medium_read_only_lookup_result_boundary_v0_min_result.json"
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


def build_declared_local_relevance_medium_read_only_lookup_result_boundary_v0_min_request(
    *,
    local_relevance_medium_read_only_lookup_result_boundary_id: str = DEFAULT_BOUNDARY_ID,
    selected_lookup_performed_artifact: Path | str = DEFAULT_LOOKUP_PERFORMED_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared request for one selected-state lookup result boundary."""

    override_selected_command = overrides.get("selected_command", selected_command)
    if override_selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyLookupResultBoundaryV0MinError(
            "selected command must be exactly state"
        )
    non_claims = _canonical_false_non_claims()
    if declared_non_claims is not None:
        non_claims.update(dict(declared_non_claims))
    request: dict[str, Any] = {
        "local_relevance_medium_read_only_lookup_result_boundary_id": (
            local_relevance_medium_read_only_lookup_result_boundary_id
        ),
        "local_relevance_medium_read_only_lookup_result_boundary_question": CORE_QUESTION,
        "local_relevance_medium_read_only_lookup_result_boundary_intent": intent,
        "selected_lookup_performed_artifact": str(selected_lookup_performed_artifact),
        "selected_command": SELECTED_COMMAND,
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "declared_non_claims": non_claims,
    }
    request.update(overrides)
    request["selected_command"] = SELECTED_COMMAND
    return request
