"""Resolve one local read-only lookup command execution.

This resolver reads one selected
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BOUNDARY artifact and
one selected LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE
artifact. It records one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION
object only.

The object is lookup-command-execution-shaped, local, read-only, selected-state
only, closure-token-aware, non-lookup-performed-shaped, non-lookup-result-shaped,
non-operation-shaped, and non-runtime-shaped. It records one bounded local
read-only lookup command execution for selected command state. It does not
perform lookup, create lookup result, create operation permission, create runtime
permission, create public or distributed surfaces, permit unsupported commands or
keys, discover files, accept entries or signals, create registry/search/query/
ranking surfaces, or authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyLookupCommandExecutionV0MinError(RuntimeError):
    """Bounded resolver error for lookup command execution handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min"
)

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_RECORDED"
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_command_execution_v0_min"
)
DEFAULT_LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_command_execution_boundary_v0_min/"
    "local_relevance_medium_read_only_lookup_command_execution_boundary_"
    "reference_review_001__local_relevance_medium_read_only_lookup_command_"
    "execution_boundary_v0_min_result.json"
)
DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "raw_full_state_packet_body_exposure_v0_min/"
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_"
    "reference_review_001__local_relevance_medium_read_only_raw_full_state_packet_"
    "body_exposure_v0_min_result.json"
)

DEFAULT_LOOKUP_COMMAND_EXECUTION_ID = (
    "local_relevance_medium_read_only_lookup_command_execution_001"
)
LOOKUP_COMMAND_EXECUTION_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION"
)
LOOKUP_COMMAND_EXECUTION_SCOPE = "SELECTED_LOOKUP_COMMAND_EXECUTION_ONLY"
SUPPORTED_LOOKUP_COMMAND_EXECUTION_TYPE_VALUES = (LOOKUP_COMMAND_EXECUTION_TYPE,)
SUPPORTED_LOOKUP_COMMAND_EXECUTION_SCOPE_VALUES = (LOOKUP_COMMAND_EXECUTION_SCOPE,)
SELECTED_COMMAND = "state"

LOOKUP_COMMAND_EXECUTION_BOUNDARY_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BOUNDARY_RECORDED"
)
RAW_FULL_STATE_PACKET_BODY_EXPOSURE_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_RECORDED"
)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_"
    "BOUNDARY for selected command state, one clean LOCAL_RELEVANCE_MEDIUM_READ_"
    "ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE, existing reusable read-only lookup "
    "permission, and prior local carrier command surface, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION be recorded for "
    "selected command state, without performing lookup, creating lookup result, "
    "creating operation permission, creating runtime permission, creating public "
    "API, creating participant-facing interface, creating distributed network "
    "behavior, creating general lookup permission, creating arbitrary lookup "
    "permission, permitting unsupported commands, permitting unsupported lookup "
    "keys, creating new lookup entry, accepting new entries, accepting new "
    "signals, performing filesystem discovery, creating query surface, registry, "
    "search, ranking, scoring, priority, validity judgment, truth judgment, "
    "authority, currentness, synchronization, participation authorization, "
    "participant role, repeated reception permission, arbitrary reception, feed, "
    "source transfer, source receipt, or follow-on work?"
)

LOOKUP_COMMAND_EXECUTION_OBJECT_FALSE_FIELDS = (
    "lookup_performed",
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
    "artifact_existence_treated_as_lookup_command_execution_authority",
    "latest_file_posture_treated_as_lookup_command_execution_authority",
    "repo_local_availability_treated_as_lookup_command_execution_authority",
    "hidden_repo_state_used_as_lookup_command_execution_content",
    "hidden_repo_state_used_as_lookup_command_execution_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

REQUIRED_FALSE_NON_CLAIMS = (
    LOOKUP_COMMAND_EXECUTION_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_lookup_command_execution_recorded",
    "basis_lookup_command_execution_boundary_artifact_preserved",
    "basis_raw_full_state_packet_body_exposure_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_raw_full_state_packet_body_exposure_recorded",
    "raw_full_state_packet_body_exposed",
    "raw_full_state_packet_body_exposure_local_only",
    "raw_full_state_packet_body_exposure_read_only",
    "lookup_command_executed",
    "lookup_command_execution_local_only",
    "lookup_command_execution_read_only",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

_BASE_BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BLOCK_REQUESTED",
    "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_PATH_MISSING",
    "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_UNREADABLE",
    "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_PATH_MISSING",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_UNREADABLE",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_NOT_JSON_OBJECT",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_NOT_RECORDED",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_FAILED_CHECKS_PRESENT",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED",
    "RAW_FULL_STATE_PACKET_BODY_NOT_EXPOSED",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_LOCAL_ONLY_NOT_TRUE",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_READ_ONLY_NOT_TRUE",
    "LOOKUP_COMMAND_EXECUTION_TYPE_MISSING",
    "LOOKUP_COMMAND_EXECUTION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION",
    "LOOKUP_COMMAND_EXECUTION_SCOPE_MISSING",
    "LOOKUP_COMMAND_EXECUTION_SCOPE_NOT_SELECTED_LOOKUP_COMMAND_EXECUTION_ONLY",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_NOT_RECORDED",
    "LOOKUP_COMMAND_NOT_EXECUTED",
    "LOOKUP_COMMAND_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    "LOOKUP_COMMAND_EXECUTION_READ_ONLY_NOT_TRUE",
    "LOOKUP_PERFORMED",
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
    "FOLLOW_ON_WORK_AUTHORIZED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "ARTIFACT_EXISTENCE_TREATED_AS_LOOKUP_COMMAND_EXECUTION_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_LOOKUP_COMMAND_EXECUTION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_LOOKUP_COMMAND_EXECUTION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_LOOKUP_COMMAND_EXECUTION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_LOOKUP_COMMAND_EXECUTION_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_REQUEST_UNREADABLE",
)

FALSE_FIELD_BLOCK_CODES = {field: field.upper() for field in REQUIRED_FALSE_NON_CLAIMS}
FALSE_FIELD_BLOCK_CODES.update(
    {
        "prior_artifacts_mutated": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "predecessor_failure_repaired": (
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
        ),
        "predecessor_failure_hidden": (
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
        ),
        "predecessor_failure_claimed_passed": (
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
        ),
    }
)
BLOCK_CODES = tuple(
    dict.fromkeys(
        _BASE_BLOCK_CODES
        + tuple(FALSE_FIELD_BLOCK_CODES.values())
        + (
            "DERIVATIVE_RECEPTION_AUTHORIZED",
            "VESSEL_RELATION_AUTHORIZED",
            "ADOPTION_CREATED",
            "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
            "PUBLICATION_FLOW_CREATED",
        )
    )
)

FALSE_CHECK_NAMES = {
    field: field.replace("_", " ") + " false" for field in REQUIRED_FALSE_NON_CLAIMS
}
FALSE_CHECK_NAMES.update(
    {
        "lookup_performed": "lookup not performed",
        "lookup_result_created": "lookup result not created",
        "operation_permission_created": "operation permission not created",
        "runtime_permission_created": "runtime permission not created",
        "public_api_created": "public API not created",
        "participant_facing_interface_created": (
            "participant-facing interface not created"
        ),
        "distributed_network_behavior_created": (
            "distributed network behavior not created"
        ),
        "general_lookup_permission_created": "general lookup permission not created",
        "arbitrary_lookup_permission_created": (
            "arbitrary lookup permission not created"
        ),
        "unsupported_commands_permitted": "unsupported commands not permitted",
        "unsupported_lookup_keys_permitted": "unsupported lookup keys not permitted",
        "new_lookup_entry_created": "no new lookup entry created",
        "new_signal_accepted": "no new signal accepted",
        "new_entry_accepted": "no new entry accepted",
        "new_relevance_object_created": "no new relevance object created",
        "new_index_entry_created": "no new index entry created",
        "filesystem_discovery_performed": "filesystem discovery not performed",
        "registry_created": "registry not created",
        "search_surface_created": "search not created",
        "query_surface_created": "query surface not created",
        "ranking_surface_created": "ranking not created",
        "scoring_surface_created": "scoring not created",
        "priority_surface_created": "priority not created",
        "validity_judgment_created": "validity judgment not created",
        "truth_judgment_created": "truth judgment not created",
        "authority_judgment_created": "authority judgment not created",
        "currentness_judgment_created": "currentness judgment not created",
        "repeated_reception_permission_created": (
            "repeated reception permission not created"
        ),
        "arbitrary_reception_created": "arbitrary reception not created",
        "feed_created": "feed not created",
        "source_transfer_occurred": "source transfer not created",
        "source_receipt_occurred": "source receipt not created",
        "source_created": "source not created",
        "authority_created": "authority not created",
        "currentness_created": "currentness not created",
        "truth_created": "truth not created",
        "synchronization_created": "synchronization not created",
        "participation_authorized": "participation not authorized",
        "participant_role_created": "participant role not created",
        "deployment_created": "deployment not created",
        "public_release_created": "public release not created",
        "broader_reusable_permission_created": (
            "broader reusable permission not created"
        ),
        "follow_on_work_authorized": "follow-on work not authorized",
        "artifact_existence_treated_as_lookup_command_execution_authority": (
            "artifact existence not lookup command execution authority"
        ),
        "latest_file_posture_treated_as_lookup_command_execution_authority": (
            "latest file posture not lookup command execution authority"
        ),
        "repo_local_availability_treated_as_lookup_command_execution_authority": (
            "repo-local availability not lookup command execution authority"
        ),
        "hidden_repo_state_used_as_lookup_command_execution_content": (
            "hidden repo state not lookup command execution content"
        ),
        "hidden_repo_state_used_as_lookup_command_execution_authority": (
            "hidden repo state not lookup command execution authority"
        ),
        "prior_artifacts_mutated": "prior artifacts not mutated",
        "predecessor_failure_repaired": "predecessor failure not repaired",
        "predecessor_failure_hidden": "predecessor failure not hidden",
        "predecessor_failure_claimed_passed": (
            "predecessor failure not claimed passed"
        ),
        "consumed_request_reopened": "consumed request not reopened",
        "authorization_token_reused": "authorization token not reused",
    }
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_lookup_command_execution_body",
    "raw_lookup_performed_body",
    "raw_lookup_result_body",
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
    "lookup_command_execution_body",
    "lookup_performed_body",
    "lookup_result_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
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
    LOOKUP_COMMAND_EXECUTION_TYPE,
    LOOKUP_COMMAND_EXECUTION_SCOPE,
    SELECTED_COMMAND,
    LOOKUP_COMMAND_EXECUTION_BOUNDARY_RECORDED_OUTCOME,
    RAW_FULL_STATE_PACKET_BODY_EXPOSURE_RECORDED_OUTCOME,
    *OUTCOME_FAMILY,
    *SUPPORTED_INTENTS,
    *BLOCK_CODES,
    *REQUIRED_FALSE_NON_CLAIMS,
    *ALLOWED_TRUE_RECORDED_FIELDS,
}

WHAT_REMAINS_OPEN = (
    "local relevance medium read-only lookup command execution test",
    "local relevance medium read-only lookup command execution live artifact",
    "local relevance medium read-only lookup command execution terminal summary, if needed",
    "lookup performed",
    "lookup result",
    "operation permission",
    "runtime permission",
    "public API",
    "participant-facing interface",
    "distributed network behavior",
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
    "broader reusable permission",
    "repeated reception permission",
    "arbitrary reception",
    "feed",
    "follow-on work",
)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    return key in SENSITIVE_CONTENT_KEYS or key.endswith("_body")


def _sanitize(value: Any, key: str | None = None) -> Any:
    if _is_sensitive_key(key):
        if isinstance(value, str) and value in OFFICIAL_VALUES:
            return value
        return "[REDACTED_SENSITIVE_BODY]"
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if value in OFFICIAL_VALUES:
            return value
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
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None, unreadable_code
    if not isinstance(value, dict):
        return None, not_object_code
    return _sanitize(value), None


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _mapping_section(artifact: Mapping[str, Any] | None, key: str) -> dict[str, Any]:
    value = artifact.get(key) if isinstance(artifact, MappingABC) else None
    return dict(value) if isinstance(value, MappingABC) else {}


def _count_failed_checks(artifact: Mapping[str, Any] | None, key: str) -> int | None:
    if not isinstance(artifact, MappingABC):
        return None
    checks = artifact.get(key)
    if isinstance(checks, list):
        return sum(
            1
            for check in checks
            if isinstance(check, MappingABC) and check.get("passed") is not True
        )
    return None


def _artifact_failed_count(
    artifact: Mapping[str, Any] | None,
    summary: Mapping[str, Any],
    checks_key: str,
) -> Any:
    if not isinstance(artifact, MappingABC):
        return None
    value = _first_present(
        summary.get("failed_check_count"), artifact.get("failed_check_count")
    )
    if value is not None:
        return value
    return _count_failed_checks(artifact, checks_key)


def _artifact_bool(*values: Any) -> bool | None:
    for value in values:
        if isinstance(value, bool):
            return value
    return None


def _lookup_command_execution_boundary(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_lookup_command_execution_boundary",
    )


def _lookup_command_execution_boundary_summary(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_lookup_command_execution_boundary_summary",
    )


def _lookup_command_execution_boundary_metadata(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_lookup_command_execution_boundary_metadata",
    )


def _lookup_command_execution_boundary_statement(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_lookup_command_execution_boundary_statement",
    )


def _raw_full_state_packet_body_exposure(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure",
    )


def _raw_full_state_packet_body_exposure_summary(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_summary",
    )


def _raw_full_state_packet_body_exposure_metadata(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_metadata",
    )


def _raw_full_state_packet_body_exposure_statement(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_statement",
    )


def _declared_non_claims(
    request: Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    if not isinstance(request, MappingABC):
        return None
    value = request.get("declared_non_claims")
    return value if isinstance(value, MappingABC) else None


def _false_field_actual(
    request: Mapping[str, Any],
    field: str,
    *basis_maps: Mapping[str, Any],
) -> Any:
    if field in request:
        return request[field]
    for basis in basis_maps:
        if isinstance(basis, MappingABC) and basis.get(field) is True:
            return True
    return False


def _required_non_claims_false(
    non_claims: Mapping[str, Any] | None,
) -> tuple[bool, str]:
    if non_claims is None:
        return False, "declared_non_claims missing or not object"
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in non_claims:
            return False, f"{key} missing"
        if non_claims.get(key) is not False:
            return False, f"{key} is not false"
    return True, "all required non-claims false"


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _sanitize(expected_posture),
            "actual_posture": _sanitize(actual_posture),
            "block_code": None if passed else code,
            "failure_code": None if passed else code,
        }
    )


def _first_failure_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _failed_check_count(checks: list[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is not True)


def _passed_check_count(checks: list[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is True)


def _block_record(code: str | None, reason: Any = None) -> dict[str, Any]:
    if code is None:
        return {"blocked": False, "code": None, "block_code": None, "reason": None}
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": _sanitize(reason or code),
    }


def _extract_lookup_command_execution_boundary_basis(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    boundary = _lookup_command_execution_boundary(artifact)
    summary = _lookup_command_execution_boundary_summary(artifact)
    metadata = _lookup_command_execution_boundary_metadata(artifact)
    statement = _lookup_command_execution_boundary_statement(artifact)
    return {
        "outcome": _first_present(
            artifact.get("outcome") if isinstance(artifact, MappingABC) else None,
            summary.get("outcome"),
        ),
        "result_version": _first_present(
            summary.get("result_version"),
            metadata.get(
                "local_relevance_medium_read_only_lookup_command_execution_boundary_version"
            ),
            metadata.get("result_version"),
            boundary.get("boundary_version"),
            artifact.get("result_version") if isinstance(artifact, MappingABC) else None,
        ),
        "failed_check_count": _artifact_failed_count(
            artifact,
            summary,
            "local_relevance_medium_read_only_lookup_command_execution_boundary_checks",
        ),
        "selected_command": _first_present(
            boundary.get("selected_command"),
            summary.get("selected_command"),
            statement.get("selected_command"),
        ),
        "future_lookup_command_execution_may_be_considered": _artifact_bool(
            boundary.get("future_lookup_command_execution_may_be_considered"),
            summary.get("future_lookup_command_execution_may_be_considered"),
            statement.get("future_lookup_command_execution_may_be_considered"),
        ),
        "selected_raw_full_recorded": _artifact_bool(
            boundary.get("selected_raw_full_state_packet_body_exposure_recorded"),
            summary.get("selected_raw_full_state_packet_body_exposure_recorded"),
            statement.get("selected_raw_full_state_packet_body_exposure_recorded"),
        ),
        "raw_full_exposed": _artifact_bool(
            boundary.get("raw_full_state_packet_body_exposed"),
            summary.get("raw_full_state_packet_body_exposed"),
            statement.get("raw_full_state_packet_body_exposed"),
        ),
        "raw_full_local_only": _artifact_bool(
            boundary.get("raw_full_state_packet_body_exposure_local_only"),
            summary.get("raw_full_state_packet_body_exposure_local_only"),
            statement.get("raw_full_state_packet_body_exposure_local_only"),
        ),
        "raw_full_read_only": _artifact_bool(
            boundary.get("raw_full_state_packet_body_exposure_read_only"),
            summary.get("raw_full_state_packet_body_exposure_read_only"),
            statement.get("raw_full_state_packet_body_exposure_read_only"),
        ),
        "boundary_object": boundary,
    }


def _extract_raw_full_state_packet_body_exposure_basis(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    exposure = _raw_full_state_packet_body_exposure(artifact)
    summary = _raw_full_state_packet_body_exposure_summary(artifact)
    metadata = _raw_full_state_packet_body_exposure_metadata(artifact)
    statement = _raw_full_state_packet_body_exposure_statement(artifact)
    return {
        "outcome": _first_present(
            artifact.get("outcome") if isinstance(artifact, MappingABC) else None,
            summary.get("outcome"),
        ),
        "result_version": _first_present(
            summary.get("result_version"),
            metadata.get(
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_version"
            ),
            metadata.get("result_version"),
            exposure.get("raw_full_state_packet_body_exposure_version"),
            artifact.get("result_version") if isinstance(artifact, MappingABC) else None,
        ),
        "failed_check_count": _artifact_failed_count(
            artifact,
            summary,
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_checks",
        ),
        "selected_command": _first_present(
            exposure.get("selected_command"),
            summary.get("selected_command"),
            statement.get("selected_command"),
        ),
        "selected_raw_full_recorded": _artifact_bool(
            exposure.get(
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded"
            ),
            exposure.get("selected_raw_full_state_packet_body_exposure_recorded"),
            summary.get(
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded"
            ),
            summary.get("selected_raw_full_state_packet_body_exposure_recorded"),
            statement.get(
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded"
            ),
            statement.get("selected_raw_full_state_packet_body_exposure_recorded"),
        ),
        "raw_full_exposed": _artifact_bool(
            exposure.get("raw_full_state_packet_body_exposed"),
            summary.get("raw_full_state_packet_body_exposed"),
            statement.get("raw_full_state_packet_body_exposed"),
        ),
        "raw_full_local_only": _artifact_bool(
            exposure.get("raw_full_state_packet_body_exposure_local_only"),
            summary.get("raw_full_state_packet_body_exposure_local_only"),
            statement.get("raw_full_state_packet_body_exposure_local_only"),
        ),
        "raw_full_read_only": _artifact_bool(
            exposure.get("raw_full_state_packet_body_exposure_read_only"),
            summary.get("raw_full_state_packet_body_exposure_read_only"),
            statement.get("raw_full_state_packet_body_exposure_read_only"),
        ),
        "exposure_object": exposure,
    }


def _build_lookup_command_execution_object(
    *,
    lookup_command_execution_id: str,
    recorded: bool,
    boundary_artifact_path: Path | None,
    boundary_basis: Mapping[str, Any],
    raw_full_artifact_path: Path | None,
    raw_full_basis: Mapping[str, Any],
    selected_command: Any,
) -> dict[str, Any]:
    object_selected_command = (
        SELECTED_COMMAND if selected_command == SELECTED_COMMAND else None
    )
    execution: dict[str, Any] = {
        "lookup_command_execution_id": lookup_command_execution_id,
        "lookup_command_execution_type": LOOKUP_COMMAND_EXECUTION_TYPE,
        "lookup_command_execution_version": RESULT_VERSION,
        "lookup_command_execution_scope": LOOKUP_COMMAND_EXECUTION_SCOPE,
        "basis_lookup_command_execution_boundary_artifact": (
            str(boundary_artifact_path) if boundary_artifact_path else None
        ),
        "basis_lookup_command_execution_boundary_outcome": boundary_basis.get(
            "outcome"
        ),
        "basis_lookup_command_execution_boundary_result_version": boundary_basis.get(
            "result_version"
        ),
        "basis_lookup_command_execution_boundary_failed_check_count": boundary_basis.get(
            "failed_check_count"
        ),
        "basis_raw_full_state_packet_body_exposure_artifact": (
            str(raw_full_artifact_path) if raw_full_artifact_path else None
        ),
        "basis_raw_full_state_packet_body_exposure_outcome": raw_full_basis.get(
            "outcome"
        ),
        "basis_raw_full_state_packet_body_exposure_result_version": raw_full_basis.get(
            "result_version"
        ),
        "basis_raw_full_state_packet_body_exposure_failed_check_count": (
            raw_full_basis.get("failed_check_count")
        ),
        "selected_command": object_selected_command,
        "selected_command_is_state": object_selected_command == SELECTED_COMMAND,
        "selected_raw_full_state_packet_body_exposure_recorded": (
            raw_full_basis.get("selected_raw_full_recorded") is True and recorded
        ),
        "raw_full_state_packet_body_exposed": (
            raw_full_basis.get("raw_full_exposed") is True and recorded
        ),
        "raw_full_state_packet_body_exposure_local_only": (
            raw_full_basis.get("raw_full_local_only") is True and recorded
        ),
        "raw_full_state_packet_body_exposure_read_only": (
            raw_full_basis.get("raw_full_read_only") is True and recorded
        ),
        "local_relevance_medium_read_only_lookup_command_execution_recorded": (
            recorded
        ),
        "lookup_command_executed": recorded,
        "lookup_command_execution_local_only": recorded,
        "lookup_command_execution_read_only": recorded,
    }
    for key in LOOKUP_COMMAND_EXECUTION_OBJECT_FALSE_FIELDS:
        execution[key] = False
    return execution


def _build_statement(
    execution: Mapping[str, Any],
    recorded: bool,
) -> dict[str, bool]:
    if not recorded:
        return {key: False for key in ALLOWED_TRUE_RECORDED_FIELDS}
    return {
        "local_relevance_medium_read_only_lookup_command_execution_recorded": (
            True
        ),
        "basis_lookup_command_execution_boundary_artifact_preserved": (
            execution.get("basis_lookup_command_execution_boundary_artifact")
            is not None
        ),
        "basis_raw_full_state_packet_body_exposure_artifact_preserved": (
            execution.get("basis_raw_full_state_packet_body_exposure_artifact")
            is not None
        ),
        "selected_command_preserved": execution.get("selected_command")
        == SELECTED_COMMAND,
        "selected_command_is_state": execution.get("selected_command_is_state")
        is True,
        "selected_raw_full_state_packet_body_exposure_recorded": execution.get(
            "selected_raw_full_state_packet_body_exposure_recorded"
        )
        is True,
        "raw_full_state_packet_body_exposed": execution.get(
            "raw_full_state_packet_body_exposed"
        )
        is True,
        "raw_full_state_packet_body_exposure_local_only": execution.get(
            "raw_full_state_packet_body_exposure_local_only"
        )
        is True,
        "raw_full_state_packet_body_exposure_read_only": execution.get(
            "raw_full_state_packet_body_exposure_read_only"
        )
        is True,
        "lookup_command_executed": execution.get("lookup_command_executed")
        is True,
        "lookup_command_execution_local_only": execution.get(
            "lookup_command_execution_local_only"
        )
        is True,
        "lookup_command_execution_read_only": execution.get(
            "lookup_command_execution_read_only"
        )
        is True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "lookup_command_execution_only": True,
        "not_lookup_performed": True,
        "not_lookup_result": True,
        "not_operation_permission": True,
        "not_runtime_permission": True,
        "not_public_api": True,
        "not_participant_facing_interface": True,
        "not_distributed_network_behavior": True,
        "not_general_lookup_permission": True,
        "not_arbitrary_lookup_permission": True,
        "not_unsupported_command_permission": True,
        "not_unsupported_key_permission": True,
        "not_registry": True,
        "not_search": True,
        "not_query_surface": True,
        "not_ranking": True,
        "not_follow_on_work": True,
    }


def _build_declared_question_section(request: Mapping[str, Any] | None) -> dict[str, Any]:
    if request is None:
        return {
            "local_relevance_medium_read_only_lookup_command_execution_id": None,
            "local_relevance_medium_read_only_lookup_command_execution_question": None,
            "local_relevance_medium_read_only_lookup_command_execution_intent": None,
            "selected_lookup_command_execution_boundary_artifact": None,
            "selected_raw_full_state_packet_body_exposure_artifact": None,
            "selected_command": None,
            "lookup_command_execution_type": None,
            "lookup_command_execution_scope": None,
        }
    return {
        "local_relevance_medium_read_only_lookup_command_execution_id": request.get(
            "local_relevance_medium_read_only_lookup_command_execution_id"
        ),
        "local_relevance_medium_read_only_lookup_command_execution_question": request.get(
            "local_relevance_medium_read_only_lookup_command_execution_question"
        ),
        "local_relevance_medium_read_only_lookup_command_execution_intent": request.get(
            "local_relevance_medium_read_only_lookup_command_execution_intent"
        ),
        "selected_lookup_command_execution_boundary_artifact": (
            str(request.get("selected_lookup_command_execution_boundary_artifact"))
            if request.get("selected_lookup_command_execution_boundary_artifact")
            is not None
            else None
        ),
        "selected_raw_full_state_packet_body_exposure_artifact": (
            str(request.get("selected_raw_full_state_packet_body_exposure_artifact"))
            if request.get("selected_raw_full_state_packet_body_exposure_artifact")
            is not None
            else None
        ),
        "selected_command": request.get("selected_command"),
        "lookup_command_execution_type": request.get("lookup_command_execution_type"),
        "lookup_command_execution_scope": request.get("lookup_command_execution_scope"),
    }


def _build_boundary_artifact_basis(
    *,
    path: Path | None,
    basis: Mapping[str, Any],
    preserved: bool,
) -> dict[str, Any]:
    return {
        "selected_lookup_command_execution_boundary_artifact": (
            str(path) if path else None
        ),
        "basis_lookup_command_execution_boundary_artifact_preserved": preserved,
        "basis_lookup_command_execution_boundary_outcome": basis.get("outcome"),
        "basis_lookup_command_execution_boundary_result_version": basis.get(
            "result_version"
        ),
        "basis_lookup_command_execution_boundary_failed_check_count": basis.get(
            "failed_check_count"
        ),
        "basis_lookup_command_execution_boundary_selected_command": basis.get(
            "selected_command"
        ),
        "basis_future_lookup_command_execution_may_be_considered": basis.get(
            "future_lookup_command_execution_may_be_considered"
        ),
    }


def _build_raw_full_artifact_basis(
    *,
    path: Path | None,
    basis: Mapping[str, Any],
    preserved: bool,
) -> dict[str, Any]:
    return {
        "selected_raw_full_state_packet_body_exposure_artifact": (
            str(path) if path else None
        ),
        "basis_raw_full_state_packet_body_exposure_artifact_preserved": preserved,
        "basis_raw_full_state_packet_body_exposure_outcome": basis.get("outcome"),
        "basis_raw_full_state_packet_body_exposure_result_version": basis.get(
            "result_version"
        ),
        "basis_raw_full_state_packet_body_exposure_failed_check_count": basis.get(
            "failed_check_count"
        ),
        "basis_raw_full_state_packet_body_exposure_selected_command": basis.get(
            "selected_command"
        ),
    }


def _build_summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    execution = result.get("local_relevance_medium_read_only_lookup_command_execution")
    if not isinstance(execution, MappingABC):
        execution = {}
    checks = result.get("local_relevance_medium_read_only_lookup_command_execution_checks")
    if not isinstance(checks, list):
        checks = []
    statement = result.get(
        "local_relevance_medium_read_only_lookup_command_execution_statement"
    )
    if not isinstance(statement, MappingABC):
        statement = {}
    non_claims = result.get("non_claims")
    if not isinstance(non_claims, MappingABC):
        non_claims = {}
    block = result.get("block")
    if not isinstance(block, MappingABC):
        block = {}
    question_section = result.get(
        "declared_local_relevance_medium_read_only_lookup_command_execution_question"
    )
    if not isinstance(question_section, MappingABC):
        question_section = {}
    execution_id = execution.get("lookup_command_execution_id")
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "lookup_command_execution_id": execution_id,
        "question": question_section.get(
            "local_relevance_medium_read_only_lookup_command_execution_question"
        ),
        "intent": question_section.get(
            "local_relevance_medium_read_only_lookup_command_execution_intent"
        ),
        "passed_check_count": _passed_check_count(checks),
        "failed_check_count": _failed_check_count(checks),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "lookup_command_execution_recorded": statement.get(
            "local_relevance_medium_read_only_lookup_command_execution_recorded"
        )
        is True,
        "basis_lookup_command_execution_boundary_artifact_preserved": statement.get(
            "basis_lookup_command_execution_boundary_artifact_preserved"
        )
        is True,
        "basis_raw_full_state_packet_body_exposure_artifact_preserved": statement.get(
            "basis_raw_full_state_packet_body_exposure_artifact_preserved"
        )
        is True,
        "selected_command": execution.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved")
        is True,
        "selected_command_is_state": statement.get("selected_command_is_state")
        is True,
        "selected_raw_full_state_packet_body_exposure_recorded": statement.get(
            "selected_raw_full_state_packet_body_exposure_recorded"
        )
        is True,
        "raw_full_state_packet_body_exposed": statement.get(
            "raw_full_state_packet_body_exposed"
        )
        is True,
        "raw_full_state_packet_body_exposure_local_only": statement.get(
            "raw_full_state_packet_body_exposure_local_only"
        )
        is True,
        "raw_full_state_packet_body_exposure_read_only": statement.get(
            "raw_full_state_packet_body_exposure_read_only"
        )
        is True,
        "lookup_command_executed": statement.get("lookup_command_executed")
        is True,
        "lookup_command_execution_local_only": statement.get(
            "lookup_command_execution_local_only"
        )
        is True,
        "lookup_command_execution_read_only": statement.get(
            "lookup_command_execution_read_only"
        )
        is True,
        "lookup_command_execution_object_summary": {
            "lookup_command_execution_id": execution_id,
            "lookup_command_execution_type": execution.get(
                "lookup_command_execution_type"
            ),
            "lookup_command_execution_scope": execution.get(
                "lookup_command_execution_scope"
            ),
            "selected_command": execution.get("selected_command"),
            "lookup_command_executed": execution.get("lookup_command_executed"),
        },
        "lookup_not_performed": non_claims.get("lookup_performed") is False,
        "lookup_result_not_created": non_claims.get("lookup_result_created")
        is False,
        "operation_permission_not_created": non_claims.get(
            "operation_permission_created"
        )
        is False,
        "runtime_permission_not_created": non_claims.get("runtime_permission_created")
        is False,
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
        "unsupported_commands_not_permitted": non_claims.get(
            "unsupported_commands_permitted"
        )
        is False,
        "unsupported_lookup_keys_not_permitted": non_claims.get(
            "unsupported_lookup_keys_permitted"
        )
        is False,
        "no_new_lookup_entry_created": non_claims.get("new_lookup_entry_created")
        is False,
        "no_new_signal_entry_relevance_object_or_index_entry_created": (
            non_claims.get("new_signal_accepted") is False
            and non_claims.get("new_entry_accepted") is False
            and non_claims.get("new_relevance_object_created") is False
            and non_claims.get("new_index_entry_created") is False
        ),
        "filesystem_discovery_not_performed": non_claims.get(
            "filesystem_discovery_performed"
        )
        is False,
        "registry_search_query_surface_ranking_not_created": (
            non_claims.get("registry_created") is False
            and non_claims.get("search_surface_created") is False
            and non_claims.get("query_surface_created") is False
            and non_claims.get("ranking_surface_created") is False
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": (
            non_claims.get("scoring_surface_created") is False
            and non_claims.get("priority_surface_created") is False
            and non_claims.get("validity_judgment_created") is False
            and non_claims.get("truth_judgment_created") is False
            and non_claims.get("authority_judgment_created") is False
            and non_claims.get("currentness_judgment_created") is False
        ),
        "repeated_reception_arbitrary_reception_feed_not_created": (
            non_claims.get("repeated_reception_permission_created") is False
            and non_claims.get("arbitrary_reception_created") is False
            and non_claims.get("feed_created") is False
        ),
        "source_authority_currentness_truth_synchronization_participation_not_created": (
            non_claims.get("source_created") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("truth_created") is False
            and non_claims.get("synchronization_created") is False
            and non_claims.get("participation_authorized") is False
            and non_claims.get("participant_role_created") is False
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
        "follow_on_not_created": non_claims.get("follow_on_work_authorized")
        is False,
        "key_non_claims": {
            "lookup_performed": non_claims.get("lookup_performed"),
            "lookup_result_created": non_claims.get("lookup_result_created"),
            "operation_permission_created": non_claims.get(
                "operation_permission_created"
            ),
            "runtime_permission_created": non_claims.get("runtime_permission_created"),
            "consumed_request_reopened": non_claims.get("consumed_request_reopened"),
            "authorization_token_reused": non_claims.get(
                "authorization_token_reused"
            ),
            "follow_on_work_authorized": non_claims.get("follow_on_work_authorized"),
        },
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _build_result(
    *,
    request: Mapping[str, Any] | None,
    checks: list[dict[str, Any]],
    outcome: str,
    block_code: str | None,
    execution: Mapping[str, Any],
    boundary_artifact_basis: Mapping[str, Any],
    raw_full_artifact_basis: Mapping[str, Any],
    additional_basis_required: Any = None,
    not_recorded_basis: Any = None,
) -> dict[str, Any]:
    execution_id = (
        execution.get("lookup_command_execution_id")
        or DEFAULT_LOOKUP_COMMAND_EXECUTION_ID
    )
    recorded = outcome == OUTCOME_RECORDED and block_code is None
    statement = _build_statement(execution, recorded)
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_lookup_command_execution_metadata": {
            "local_relevance_medium_read_only_lookup_command_execution_id": (
                execution_id
            ),
            "local_relevance_medium_read_only_lookup_command_execution_type": (
                LOOKUP_COMMAND_EXECUTION_TYPE
            ),
            "local_relevance_medium_read_only_lookup_command_execution_version": (
                RESULT_VERSION
            ),
            "generated_at": _now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_local_relevance_medium_read_only_lookup_command_execution_question": (
            _sanitize(_build_declared_question_section(request))
        ),
        "selected_lookup_command_execution_boundary_artifact_basis": _sanitize(
            boundary_artifact_basis
        ),
        "selected_raw_full_state_packet_body_exposure_artifact_basis": _sanitize(
            raw_full_artifact_basis
        ),
        "local_relevance_medium_read_only_lookup_command_execution": _sanitize(
            dict(execution)
        ),
        "local_relevance_medium_read_only_lookup_command_execution_checks": (
            _sanitize(checks)
        ),
        "local_relevance_medium_read_only_lookup_command_execution_statement": (
            statement
        ),
        "local_relevance_medium_read_only_lookup_command_execution_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": _sanitize(additional_basis_required),
        "not_recorded_basis": _sanitize(not_recorded_basis),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": _block_record(block_code),
    }
    result["local_relevance_medium_read_only_lookup_command_execution_summary"] = (
        build_local_relevance_medium_read_only_lookup_command_execution_v0_min_summary(
            result
        )
    )
    return result


def _empty_execution_for_malformed() -> dict[str, Any]:
    return _build_lookup_command_execution_object(
        lookup_command_execution_id=DEFAULT_LOOKUP_COMMAND_EXECUTION_ID,
        recorded=False,
        boundary_artifact_path=None,
        boundary_basis={},
        raw_full_artifact_path=None,
        raw_full_basis={},
        selected_command=None,
    )


def _malformed_result(code: str, reason: Any) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _check(
        checks,
        "declared lookup command execution request readable mapping",
        False,
        "mapping request",
        reason,
        code,
    )
    return _build_result(
        request=None,
        checks=checks,
        outcome=OUTCOME_BLOCKED,
        block_code=code,
        execution=_empty_execution_for_malformed(),
        boundary_artifact_basis={},
        raw_full_artifact_basis={},
    )


def _candidate_output_path(output_path: Path) -> Path:
    if not output_path.exists():
        return output_path
    stem = output_path.stem
    suffix = output_path.suffix
    parent = output_path.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def build_local_relevance_medium_read_only_lookup_command_execution_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary for a lookup command execution result."""

    return _sanitize(_build_summary_from_result(result))


def build_declared_local_relevance_medium_read_only_lookup_command_execution_v0_min_request(
    *,
    local_relevance_medium_read_only_lookup_command_execution_id: str = DEFAULT_LOOKUP_COMMAND_EXECUTION_ID,
    selected_lookup_command_execution_boundary_artifact: Path | str = DEFAULT_LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT,
    selected_raw_full_state_packet_body_exposure_artifact: Path | str = DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    lookup_command_execution_type: str = LOOKUP_COMMAND_EXECUTION_TYPE,
    lookup_command_execution_scope: str = LOOKUP_COMMAND_EXECUTION_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a valid declared lookup command execution request."""

    if selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyLookupCommandExecutionV0MinError(
            "selected_command must be state"
        )
    request: dict[str, Any] = {
        "local_relevance_medium_read_only_lookup_command_execution_id": (
            local_relevance_medium_read_only_lookup_command_execution_id
        ),
        "local_relevance_medium_read_only_lookup_command_execution_question": (
            CORE_QUESTION
        ),
        "local_relevance_medium_read_only_lookup_command_execution_intent": intent,
        "selected_lookup_command_execution_boundary_artifact": str(
            selected_lookup_command_execution_boundary_artifact
        ),
        "selected_raw_full_state_packet_body_exposure_artifact": str(
            selected_raw_full_state_packet_body_exposure_artifact
        ),
        "selected_command": selected_command,
        "lookup_command_execution_type": lookup_command_execution_type,
        "lookup_command_execution_scope": lookup_command_execution_scope,
        "declared_non_claims": (
            dict(declared_non_claims)
            if declared_non_claims is not None
            else _canonical_false_non_claims()
        ),
    }
    request.update(overrides)
    return request


def resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
    declared_local_relevance_medium_read_only_lookup_command_execution: Mapping[
        str, Any
    ]
    | None = None,
) -> dict[str, Any]:
    """Resolve one local read-only lookup command execution request."""

    if declared_local_relevance_medium_read_only_lookup_command_execution is None:
        request = (
            build_declared_local_relevance_medium_read_only_lookup_command_execution_v0_min_request()
        )
    elif not isinstance(
        declared_local_relevance_medium_read_only_lookup_command_execution,
        MappingABC,
    ):
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_REQUEST_MALFORMED",
            "request is not a mapping",
        )
    else:
        request = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_lookup_command_execution)
        )

    checks: list[dict[str, Any]] = []
    lookup_command_execution_id = str(
        request.get(
            "local_relevance_medium_read_only_lookup_command_execution_id",
            DEFAULT_LOOKUP_COMMAND_EXECUTION_ID,
        )
        or DEFAULT_LOOKUP_COMMAND_EXECUTION_ID
    )
    question = request.get(
        "local_relevance_medium_read_only_lookup_command_execution_question"
    )
    intent = request.get(
        "local_relevance_medium_read_only_lookup_command_execution_intent"
    )
    boundary_artifact_path = _as_path(
        request.get("selected_lookup_command_execution_boundary_artifact")
    )
    raw_full_artifact_path = _as_path(
        request.get("selected_raw_full_state_packet_body_exposure_artifact")
    )
    selected_command = request.get("selected_command")
    lookup_command_execution_type = request.get("lookup_command_execution_type")
    lookup_command_execution_scope = request.get("lookup_command_execution_scope")
    declared_non_claims = _declared_non_claims(request)

    _check(
        checks,
        "lookup command execution question declared",
        isinstance(question, str) and bool(question.strip()),
        "declared lookup command execution question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "lookup command execution intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _check(
            checks,
            "lookup command execution block not requested",
            False,
            "not block requested",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BLOCK_REQUESTED",
        )

    _check(
        checks,
        "lookup command execution boundary artifact path declared",
        boundary_artifact_path is not None
        and request.get("lookup_command_execution_boundary_artifact_missing")
        is not True,
        "declared lookup command execution boundary artifact path",
        request.get("selected_lookup_command_execution_boundary_artifact"),
        "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_PATH_MISSING",
    )
    boundary_artifact: dict[str, Any] | None = None
    boundary_read_code: str | None = None
    if boundary_artifact_path is not None:
        boundary_artifact, boundary_read_code = _read_json_object(
            boundary_artifact_path,
            "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_UNREADABLE",
            "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
        )
        _check(
            checks,
            "lookup command execution boundary artifact readable JSON",
            boundary_read_code is None,
            "readable JSON object",
            boundary_read_code or "readable JSON object",
            boundary_read_code,
        )

    _check(
        checks,
        "raw/full state packet body exposure artifact path declared",
        raw_full_artifact_path is not None
        and request.get("raw_full_state_packet_body_exposure_artifact_missing")
        is not True,
        "declared raw/full state packet body exposure artifact path",
        request.get("selected_raw_full_state_packet_body_exposure_artifact"),
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_PATH_MISSING",
    )
    raw_full_artifact: dict[str, Any] | None = None
    raw_full_read_code: str | None = None
    if raw_full_artifact_path is not None:
        raw_full_artifact, raw_full_read_code = _read_json_object(
            raw_full_artifact_path,
            "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_UNREADABLE",
            "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_NOT_JSON_OBJECT",
        )
        _check(
            checks,
            "raw/full state packet body exposure artifact readable JSON",
            raw_full_read_code is None,
            "readable JSON object",
            raw_full_read_code or "readable JSON object",
            raw_full_read_code,
        )

    boundary_basis = _extract_lookup_command_execution_boundary_basis(
        boundary_artifact
    )
    raw_full_basis = _extract_raw_full_state_packet_body_exposure_basis(
        raw_full_artifact
    )
    boundary_object = boundary_basis.get("boundary_object")
    if not isinstance(boundary_object, MappingABC):
        boundary_object = {}
    raw_full_object = raw_full_basis.get("exposure_object")
    if not isinstance(raw_full_object, MappingABC):
        raw_full_object = {}

    _check(
        checks,
        "lookup command execution boundary artifact outcome recorded",
        boundary_basis.get("outcome")
        == LOOKUP_COMMAND_EXECUTION_BOUNDARY_RECORDED_OUTCOME
        and request.get("lookup_command_execution_boundary_artifact_not_recorded")
        is not True,
        LOOKUP_COMMAND_EXECUTION_BOUNDARY_RECORDED_OUTCOME,
        boundary_basis.get("outcome"),
        "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "lookup command execution boundary artifact result version 0.1.0",
        boundary_basis.get("result_version") == RESULT_VERSION
        and request.get(
            "lookup_command_execution_boundary_artifact_version_not_0_1_0"
        )
        is not True,
        RESULT_VERSION,
        boundary_basis.get("result_version"),
        "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "lookup command execution boundary artifact failed check count zero",
        boundary_basis.get("failed_check_count") == 0
        and request.get(
            "lookup_command_execution_boundary_artifact_failed_checks_present"
        )
        is not True,
        0,
        boundary_basis.get("failed_check_count"),
        "LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "raw/full state packet body exposure artifact outcome recorded",
        raw_full_basis.get("outcome")
        == RAW_FULL_STATE_PACKET_BODY_EXPOSURE_RECORDED_OUTCOME
        and request.get("raw_full_state_packet_body_exposure_artifact_not_recorded")
        is not True,
        RAW_FULL_STATE_PACKET_BODY_EXPOSURE_RECORDED_OUTCOME,
        raw_full_basis.get("outcome"),
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "raw/full state packet body exposure artifact result version 0.1.0",
        raw_full_basis.get("result_version") == RESULT_VERSION
        and request.get(
            "raw_full_state_packet_body_exposure_artifact_version_not_0_1_0"
        )
        is not True,
        RESULT_VERSION,
        raw_full_basis.get("result_version"),
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "raw/full state packet body exposure artifact failed check count zero",
        raw_full_basis.get("failed_check_count") == 0
        and request.get(
            "raw_full_state_packet_body_exposure_artifact_failed_checks_present"
        )
        is not True,
        0,
        raw_full_basis.get("failed_check_count"),
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "selected command declared",
        selected_command is not None and request.get("selected_command_missing") is not True,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_MISSING",
    )
    _check(
        checks,
        "selected command exactly state",
        selected_command == SELECTED_COMMAND
        and request.get("selected_command_not_state") is not True,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected command is state",
        selected_command == SELECTED_COMMAND
        and boundary_basis.get("selected_command") == SELECTED_COMMAND
        and raw_full_basis.get("selected_command") == SELECTED_COMMAND,
        "selected command state",
        {
            "request": selected_command,
            "boundary": boundary_basis.get("selected_command"),
            "raw_full": raw_full_basis.get("selected_command"),
        },
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected raw/full state packet body exposure recorded",
        raw_full_basis.get("selected_raw_full_recorded") is True
        and boundary_basis.get("selected_raw_full_recorded") is True
        and request.get("selected_raw_full_state_packet_body_exposure_not_recorded")
        is not True,
        True,
        {
            "boundary": boundary_basis.get("selected_raw_full_recorded"),
            "raw_full": raw_full_basis.get("selected_raw_full_recorded"),
        },
        "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED",
    )
    _check(
        checks,
        "raw/full state packet body exposed",
        raw_full_basis.get("raw_full_exposed") is True
        and boundary_basis.get("raw_full_exposed") is True
        and request.get("raw_full_state_packet_body_not_exposed") is not True,
        True,
        {
            "boundary": boundary_basis.get("raw_full_exposed"),
            "raw_full": raw_full_basis.get("raw_full_exposed"),
        },
        "RAW_FULL_STATE_PACKET_BODY_NOT_EXPOSED",
    )
    _check(
        checks,
        "raw/full state packet body exposure local only",
        raw_full_basis.get("raw_full_local_only") is True
        and boundary_basis.get("raw_full_local_only") is True
        and request.get("raw_full_state_packet_body_exposure_local_only_not_true")
        is not True,
        True,
        {
            "boundary": boundary_basis.get("raw_full_local_only"),
            "raw_full": raw_full_basis.get("raw_full_local_only"),
        },
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "raw/full state packet body exposure read only",
        raw_full_basis.get("raw_full_read_only") is True
        and boundary_basis.get("raw_full_read_only") is True
        and request.get("raw_full_state_packet_body_exposure_read_only_not_true")
        is not True,
        True,
        {
            "boundary": boundary_basis.get("raw_full_read_only"),
            "raw_full": raw_full_basis.get("raw_full_read_only"),
        },
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_READ_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "lookup command execution type declared",
        lookup_command_execution_type is not None,
        LOOKUP_COMMAND_EXECUTION_TYPE,
        lookup_command_execution_type,
        "LOOKUP_COMMAND_EXECUTION_TYPE_MISSING",
    )
    _check(
        checks,
        "lookup command execution type exact",
        lookup_command_execution_type == LOOKUP_COMMAND_EXECUTION_TYPE
        and request.get(
            "lookup_command_execution_type_not_local_relevance_medium_read_only_lookup_command_execution"
        )
        is not True,
        LOOKUP_COMMAND_EXECUTION_TYPE,
        lookup_command_execution_type,
        "LOOKUP_COMMAND_EXECUTION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION",
    )
    _check(
        checks,
        "lookup command execution scope declared",
        lookup_command_execution_scope is not None,
        LOOKUP_COMMAND_EXECUTION_SCOPE,
        lookup_command_execution_scope,
        "LOOKUP_COMMAND_EXECUTION_SCOPE_MISSING",
    )
    _check(
        checks,
        "lookup command execution scope exact",
        lookup_command_execution_scope == LOOKUP_COMMAND_EXECUTION_SCOPE
        and request.get(
            "lookup_command_execution_scope_not_selected_lookup_command_execution_only"
        )
        is not True,
        LOOKUP_COMMAND_EXECUTION_SCOPE,
        lookup_command_execution_scope,
        "LOOKUP_COMMAND_EXECUTION_SCOPE_NOT_SELECTED_LOOKUP_COMMAND_EXECUTION_ONLY",
    )
    _check(
        checks,
        "local relevance medium read-only lookup command execution recorded",
        request.get(
            "local_relevance_medium_read_only_lookup_command_execution_not_recorded"
        )
        is not True,
        True,
        request.get(
            "local_relevance_medium_read_only_lookup_command_execution_not_recorded",
            False,
        )
        is not True,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_NOT_RECORDED",
    )
    _check(
        checks,
        "lookup command executed",
        request.get("lookup_command_not_executed") is not True
        and request.get("lookup_command_executed", True) is True,
        True,
        request.get("lookup_command_executed", True),
        "LOOKUP_COMMAND_NOT_EXECUTED",
    )
    _check(
        checks,
        "lookup command execution local only",
        request.get("lookup_command_execution_local_only_not_true") is not True
        and request.get("lookup_command_execution_local_only", True) is True,
        True,
        request.get("lookup_command_execution_local_only", True),
        "LOOKUP_COMMAND_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "lookup command execution read only",
        request.get("lookup_command_execution_read_only_not_true") is not True
        and request.get("lookup_command_execution_read_only", True) is True,
        True,
        request.get("lookup_command_execution_read_only", True),
        "LOOKUP_COMMAND_EXECUTION_READ_ONLY_NOT_TRUE",
    )

    for field in REQUIRED_FALSE_NON_CLAIMS:
        actual = _false_field_actual(request, field, boundary_object, raw_full_object)
        code = FALSE_FIELD_BLOCK_CODES.get(field, field.upper())
        _check(
            checks,
            FALSE_CHECK_NAMES.get(field, field.replace("_", " ") + " false"),
            actual is False,
            False,
            actual,
            code,
        )

    required_non_claims_passed, required_non_claims_actual = _required_non_claims_false(
        declared_non_claims
    )
    _check(
        checks,
        "required non-claims false",
        required_non_claims_passed,
        "all required declared non-claims exactly false",
        required_non_claims_actual,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _check(
        checks,
        "predecessor failure evidence preserved",
        request.get("predecessor_failure_repaired") is not True
        and request.get("predecessor_failure_hidden") is not True
        and request.get("predecessor_failure_claimed_passed") is not True,
        "preserved failed-lineage evidence",
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
    canonical_non_claims = _canonical_false_non_claims()
    _check(
        checks,
        "result-level required false non-claims canonical false",
        all(value is False for value in canonical_non_claims.values()),
        "all result-level non-claims false",
        canonical_non_claims,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    block_code = _first_failure_code(checks)
    if block_code is not None:
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif request.get("additional_basis_context"):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    else:
        outcome = OUTCOME_RECORDED

    recorded = outcome == OUTCOME_RECORDED and block_code is None
    execution = _build_lookup_command_execution_object(
        lookup_command_execution_id=lookup_command_execution_id,
        recorded=recorded,
        boundary_artifact_path=boundary_artifact_path,
        boundary_basis=boundary_basis,
        raw_full_artifact_path=raw_full_artifact_path,
        raw_full_basis=raw_full_basis,
        selected_command=selected_command,
    )
    boundary_artifact_basis = _build_boundary_artifact_basis(
        path=boundary_artifact_path,
        basis=boundary_basis,
        preserved=recorded and boundary_artifact_path is not None,
    )
    raw_full_artifact_basis = _build_raw_full_artifact_basis(
        path=raw_full_artifact_path,
        basis=raw_full_basis,
        preserved=recorded and raw_full_artifact_path is not None,
    )
    return _build_result(
        request=request,
        checks=checks,
        outcome=outcome,
        block_code=block_code,
        execution=execution,
        boundary_artifact_basis=boundary_artifact_basis,
        raw_full_artifact_basis=raw_full_artifact_basis,
        additional_basis_required=(
            request.get("additional_basis_context")
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else None
        ),
        not_recorded_basis=(
            request.get("not_recorded_basis")
            if outcome == OUTCOME_NOT_RECORDED
            else None
        ),
    )


def resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min_from_path(
    declared_local_relevance_medium_read_only_lookup_command_execution_path: Path | str,
) -> dict[str, Any]:
    """Resolve one lookup command execution request from a JSON path."""

    path = _as_path(
        declared_local_relevance_medium_read_only_lookup_command_execution_path
    )
    if path is None:
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_REQUEST_UNREADABLE",
            "request path missing",
        )
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_REQUEST_UNREADABLE",
            str(exc),
        )
    if not isinstance(value, dict):
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_REQUEST_MALFORMED",
            "request JSON is not an object",
        )
    return resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
        value
    )


def write_local_relevance_medium_read_only_lookup_command_execution_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a lookup command execution result as stable UTF-8 JSON."""

    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyLookupCommandExecutionV0MinError(
            "result must be a mapping"
        )
    metadata = result.get(
        "local_relevance_medium_read_only_lookup_command_execution_metadata",
        {},
    )
    if not isinstance(metadata, MappingABC):
        metadata = {}
    execution_id = (
        metadata.get("local_relevance_medium_read_only_lookup_command_execution_id")
        or DEFAULT_LOOKUP_COMMAND_EXECUTION_ID
    )
    filename = (
        f"{execution_id}__local_relevance_medium_read_only_lookup_command_"
        "execution_v0_min_result.json"
    )
    if output_path is None:
        target = OUTPUT_ROOT / filename
    else:
        provided = Path(output_path)
        target = provided / filename if provided.suffix == "" else provided
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _candidate_output_path(target)
    target.write_text(
        json.dumps(_sanitize(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
