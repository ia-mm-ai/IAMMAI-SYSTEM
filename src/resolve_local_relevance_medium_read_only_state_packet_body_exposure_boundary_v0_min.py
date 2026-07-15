"""Resolve one selected-state packet-body-exposure boundary.

This resolver records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY object. It
reads one clean selected-state result object artifact as result-object basis and
may record that future state packet body exposure can be considered later as a
separately bounded step.

The boundary object is boundary-shaped, local, read-only,
selected-state-packet-body-exposure-consideration-only, and non-packet-body-
exposure-shaped. It does not expose state packet body or raw/full state packet
body, perform lookup, execute lookup commands, create permissions, create public
or distributed surfaces, discover files, accept entries or signals, create
registry/search/query/ranking surfaces, or authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class LocalRelevanceMediumReadOnlyStatePacketBodyExposureBoundaryV0MinError(
    RuntimeError
):
    """Bounded resolver error for state packet body exposure boundary handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min"
)

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BLOCKED"
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
    "state_packet_body_exposure_boundary_v0_min"
)
DEFAULT_STATE_RESULT_OBJECT_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_result_object_v0_min/"
    "local_relevance_medium_read_only_state_result_object_reference_review_001__"
    "local_relevance_medium_read_only_state_result_object_v0_min_result.json"
)

DEFAULT_BOUNDARY_ID = (
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_001"
)
BOUNDARY_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY"
)
BOUNDARY_SCOPE = "SELECTED_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY"
SELECTED_COMMAND = "state"

STATE_RESULT_OBJECT_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_RECORDED"
)
STATE_RESULT_OBJECT_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT"
STATE_RESULT_OBJECT_SCOPE = "SELECTED_STATE_RESULT_OBJECT_ONLY"

SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)

INTENT_RECORD = (
    "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT for "
    "selected command state, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY be "
    "recorded that permits a future state packet body exposure for that "
    "selected-state result object to be considered as a separately bounded step, "
    "without exposing state packet body, exposing raw/full state packet body, "
    "performing lookup, executing lookup command, creating operation permission, "
    "creating runtime permission, creating public API, creating participant-facing "
    "interface, creating distributed network behavior, creating general lookup "
    "permission, creating arbitrary lookup permission, permitting unsupported "
    "commands, permitting unsupported lookup keys, creating new lookup result, "
    "creating new lookup entry, accepting new entries, accepting new signals, "
    "performing filesystem discovery, creating query surface, registry, search, "
    "ranking, scoring, priority, validity judgment, truth judgment, authority, "
    "currentness, synchronization, participation authorization, participant role, "
    "repeated reception permission, arbitrary reception, feed, source transfer, "
    "source receipt, or follow-on work?"
)

BOUNDARY_OBJECT_FALSE_FIELDS = (
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
    "artifact_existence_treated_as_state_packet_body_exposure_boundary_authority",
    "latest_file_posture_treated_as_state_packet_body_exposure_boundary_authority",
    "repo_local_availability_treated_as_state_packet_body_exposure_boundary_authority",
    "hidden_repo_state_used_as_state_packet_body_exposure_boundary_content",
    "hidden_repo_state_used_as_state_packet_body_exposure_boundary_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

REQUIRED_FALSE_NON_CLAIMS = BOUNDARY_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_recorded",
    "basis_state_result_object_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_state_result_object_recorded",
    "state_result_object_created",
    "state_result_object_local_only",
    "state_result_object_read_only",
    "future_state_packet_body_exposure_may_be_considered",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BLOCK_REQUESTED",
    "STATE_RESULT_OBJECT_ARTIFACT_PATH_MISSING",
    "STATE_RESULT_OBJECT_ARTIFACT_UNREADABLE",
    "STATE_RESULT_OBJECT_ARTIFACT_NOT_JSON_OBJECT",
    "STATE_RESULT_OBJECT_ARTIFACT_NOT_RECORDED",
    "STATE_RESULT_OBJECT_ARTIFACT_FAILED_CHECKS_PRESENT",
    "STATE_RESULT_OBJECT_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_STATE_RESULT_OBJECT_NOT_RECORDED",
    "STATE_RESULT_OBJECT_NOT_CREATED",
    "STATE_RESULT_OBJECT_LOCAL_ONLY_NOT_TRUE",
    "STATE_RESULT_OBJECT_READ_ONLY_NOT_TRUE",
    "FUTURE_STATE_PACKET_BODY_EXPOSURE_MAY_NOT_BE_CONSIDERED",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_SELECTED_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_REQUEST_UNREADABLE",
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
    "artifact_existence_treated_as_state_packet_body_exposure_boundary_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_AUTHORITY"
    ),
    "latest_file_posture_treated_as_state_packet_body_exposure_boundary_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_AUTHORITY"
    ),
    "repo_local_availability_treated_as_state_packet_body_exposure_boundary_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_AUTHORITY"
    ),
    "hidden_repo_state_used_as_state_packet_body_exposure_boundary_content": (
        "HIDDEN_REPO_STATE_USED_AS_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_CONTENT"
    ),
    "hidden_repo_state_used_as_state_packet_body_exposure_boundary_authority": (
        "HIDDEN_REPO_STATE_USED_AS_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_AUTHORITY"
    ),
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
}

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_state_packet_body_exposure_boundary_body",
    "raw_state_packet_body",
    "raw_full_state_packet_body",
    "raw_state_result_object_body",
    "raw_state_result_body",
    "raw_lookup_result_body",
    "raw_lookup_performed_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "state_packet_body_exposure_boundary_body",
    "state_packet_body",
    "full_state_packet_body",
    "state_result_object_body",
    "state_result_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_OBJECT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
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

OFFICIAL_VALUES = {
    BOUNDARY_TYPE,
    BOUNDARY_SCOPE,
    SELECTED_COMMAND,
    STATE_RESULT_OBJECT_RECORDED_OUTCOME,
    STATE_RESULT_OBJECT_TYPE,
    STATE_RESULT_OBJECT_SCOPE,
    *OUTCOME_FAMILY,
    *BLOCK_CODES,
    *REQUIRED_FALSE_NON_CLAIMS,
    *ALLOWED_TRUE_RECORDED_FIELDS,
}

WHAT_REMAINS_OPEN = (
    "local relevance medium read-only state packet body exposure boundary resolver",
    "local relevance medium read-only state packet body exposure boundary test",
    "local relevance medium read-only state packet body exposure boundary live artifact",
    "local relevance medium read-only state packet body exposure boundary terminal summary, if needed",
    "state packet body exposure",
    "raw/full state packet body exposure",
    "raw/full state packet body exposure boundary",
    "lookup command execution",
    "lookup performed",
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
    "derivative reception",
    "vessel relation",
    "adoption",
    "authority creation",
    "currentness creation",
    "truth creation",
    "synchronization",
    "participation authorization",
    "participant role",
    "receiving-context governance",
    "deployment",
    "public release",
    "publication flow",
    "broader reusable permission",
    "repeated reception permission",
    "arbitrary reception",
    "feed",
    "follow-on work",
)


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


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
        return "[REDACTED_SENSITIVE_BODY]"
    if isinstance(value, str):
        if value in OFFICIAL_VALUES:
            return value
        sanitized = value
        for sentinel in HOSTILE_SENTINELS:
            sanitized = sanitized.replace(sentinel, "[REDACTED_HOSTILE_SENTINEL]")
        return sanitized
    if isinstance(value, Mapping):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, tuple):
        return tuple(_sanitize(item, key) for item in value)
    return value


def _read_json_object(path_value: Any) -> tuple[dict[str, Any] | None, str | None]:
    try:
        path = Path(path_value)
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None, "STATE_RESULT_OBJECT_ARTIFACT_UNREADABLE"
    if not isinstance(value, dict):
        return None, "STATE_RESULT_OBJECT_ARTIFACT_NOT_JSON_OBJECT"
    return value, None


def _get_nested(mapping: Mapping[str, Any], *path: str) -> Any:
    value: Any = mapping
    for key in path:
        if not isinstance(value, Mapping):
            return None
        value = value.get(key)
    return value


def _artifact_result_version(artifact: Mapping[str, Any] | None) -> Any:
    if not artifact:
        return None
    return (
        _get_nested(
            artifact,
            "local_relevance_medium_read_only_state_result_object_summary",
            "result_version",
        )
        or _get_nested(
            artifact,
            "local_relevance_medium_read_only_state_result_object_metadata",
            "local_relevance_medium_read_only_state_result_object_version",
        )
        or artifact.get("result_version")
    )


def _artifact_failed_check_count(artifact: Mapping[str, Any] | None) -> Any:
    if not artifact:
        return None
    summary_count = _get_nested(
        artifact,
        "local_relevance_medium_read_only_state_result_object_summary",
        "failed_check_count",
    )
    if summary_count is not None:
        return summary_count
    checks = artifact.get("local_relevance_medium_read_only_state_result_object_checks")
    if isinstance(checks, list):
        return sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))
    return artifact.get("failed_check_count")


def _state_result_object(artifact: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not artifact:
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_result_object")
    if isinstance(value, Mapping):
        return value
    return {}


def _declared_non_claims(
    request: Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    if not isinstance(request, Mapping):
        return None
    value = request.get("declared_non_claims")
    return value if isinstance(value, Mapping) else None


def _top_or_non_claim(
    request: Mapping[str, Any] | None,
    key: str,
    non_claims: Mapping[str, Any] | None,
) -> Any:
    if isinstance(request, Mapping) and key in request:
        return request[key]
    if non_claims is not None and key in non_claims:
        return non_claims[key]
    return None


def _check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str | None = None,
) -> None:
    record = {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected),
        "actual_posture": _sanitize(actual),
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }
    checks.append(record)


def _first_failure_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _has_failed_checks(checks: list[Mapping[str, Any]]) -> bool:
    return any(not check.get("passed") for check in checks)


def _basis_field(
    state_result_object: Mapping[str, Any],
    field: str,
    default: Any = None,
) -> Any:
    return state_result_object.get(field, default)


def _basis_bool_true(state_result_object: Mapping[str, Any], field: str) -> bool:
    return _basis_field(state_result_object, field) is True


def _false_field_actual(
    request: Mapping[str, Any],
    non_claims: Mapping[str, Any] | None,
    state_result_object: Mapping[str, Any],
    field: str,
) -> Any:
    declared = _top_or_non_claim(request, field, non_claims)
    if declared is not None:
        return declared
    if field in state_result_object:
        return state_result_object.get(field)
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


def _build_boundary_object(
    *,
    boundary_id: str,
    basis_state_result_object_artifact: str | None,
    basis_state_result_object_outcome: Any,
    basis_state_result_object_result_version: Any,
    basis_state_result_object_failed_check_count: Any,
    selected_command: Any,
    selected_state_result_object_recorded: bool,
    state_result_object_created: bool,
    state_result_object_local_only: bool,
    state_result_object_read_only: bool,
    future_state_packet_body_exposure_may_be_considered: bool,
) -> dict[str, Any]:
    boundary = {
        "boundary_id": boundary_id,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "basis_state_result_object_artifact": basis_state_result_object_artifact,
        "basis_state_result_object_outcome": basis_state_result_object_outcome,
        "basis_state_result_object_result_version": basis_state_result_object_result_version,
        "basis_state_result_object_failed_check_count": (
            basis_state_result_object_failed_check_count
        ),
        "selected_command": selected_command,
        "selected_command_is_state": selected_command == SELECTED_COMMAND,
        "selected_state_result_object_recorded": selected_state_result_object_recorded,
        "state_result_object_created": state_result_object_created,
        "state_result_object_local_only": state_result_object_local_only,
        "state_result_object_read_only": state_result_object_read_only,
        "future_state_packet_body_exposure_may_be_considered": (
            future_state_packet_body_exposure_may_be_considered
        ),
    }
    for key in BOUNDARY_OBJECT_FALSE_FIELDS:
        boundary[key] = False
    return boundary


def _build_statement(boundary: Mapping[str, Any], recorded: bool) -> dict[str, bool]:
    return {
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_recorded": recorded,
        "basis_state_result_object_artifact_preserved": recorded,
        "selected_command_preserved": boundary.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": boundary.get("selected_command_is_state") is True,
        "selected_state_result_object_recorded": (
            boundary.get("selected_state_result_object_recorded") is True
        ),
        "state_result_object_created": boundary.get("state_result_object_created") is True,
        "state_result_object_local_only": (
            boundary.get("state_result_object_local_only") is True
        ),
        "state_result_object_read_only": (
            boundary.get("state_result_object_read_only") is True
        ),
        "future_state_packet_body_exposure_may_be_considered": (
            boundary.get("future_state_packet_body_exposure_may_be_considered") is True
        ),
        "result_level_non_claims_canonical_false": True,
    }


def _block_record(code: str | None, reason: Any = None) -> dict[str, Any]:
    if code is None:
        return {"blocked": False, "code": None, "block_code": None, "reason": None}
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": _sanitize(reason or code),
    }


def _minimal_blocked_result(code: str, reason: str) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _check(checks, "declared request readable", False, "mapping request", reason, code)
    boundary = _build_boundary_object(
        boundary_id=DEFAULT_BOUNDARY_ID,
        basis_state_result_object_artifact=None,
        basis_state_result_object_outcome=None,
        basis_state_result_object_result_version=None,
        basis_state_result_object_failed_check_count=None,
        selected_command=None,
        selected_state_result_object_recorded=False,
        state_result_object_created=False,
        state_result_object_local_only=False,
        state_result_object_read_only=False,
        future_state_packet_body_exposure_may_be_considered=False,
    )
    result = _assemble_result(
        boundary_id=DEFAULT_BOUNDARY_ID,
        question=None,
        intent=None,
        selected_state_result_object_artifact_basis={},
        boundary=boundary,
        checks=checks,
        outcome=OUTCOME_BLOCKED,
        block=_block_record(code, reason),
        additional_basis_required=[],
        not_recorded_basis=[],
    )
    return result


def _assemble_result(
    *,
    boundary_id: str,
    question: Any,
    intent: Any,
    selected_state_result_object_artifact_basis: Mapping[str, Any],
    boundary: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block: Mapping[str, Any],
    additional_basis_required: Any,
    not_recorded_basis: Any,
) -> dict[str, Any]:
    metadata = {
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_id": boundary_id,
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_type": BOUNDARY_TYPE,
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "declared_intent": _sanitize(intent),
    }
    recorded = outcome == OUTCOME_RECORDED
    statement = _build_statement(boundary, recorded)
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_metadata": metadata,
        "declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary_question": _sanitize(
            question
        ),
        "selected_state_result_object_artifact_basis": _sanitize(
            dict(selected_state_result_object_artifact_basis)
        ),
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary": _sanitize(
            dict(boundary)
        ),
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_checks": _sanitize(
            checks
        ),
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_statement": statement,
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_non_meaning": {
            "state_packet_body_exposure_created": False,
            "raw_full_state_packet_body_exposure_created": False,
            "lookup_performed": False,
            "operation_permission_created": False,
            "runtime_permission_created": False,
            "public_api_created": False,
            "participant_facing_interface_created": False,
            "distributed_network_behavior_created": False,
            "follow_on_work_authorized": False,
        },
        "additional_basis_required": _sanitize(additional_basis_required),
        "not_recorded_basis": _sanitize(not_recorded_basis),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": dict(block),
    }
    result[
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_summary"
    ] = build_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_summary(
        result
    )
    return result


def resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min(
    declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary: Mapping[
        str, Any
    ]
    | None = None,
) -> dict:
    """Resolve one state packet body exposure boundary request."""

    if declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary is None:
        return _minimal_blocked_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_REQUEST_MALFORMED",
            "request missing",
        )
    if not isinstance(
        declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary,
        Mapping,
    ):
        return _minimal_blocked_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_REQUEST_MALFORMED",
            "request is not a mapping",
        )

    request = copy.deepcopy(
        dict(declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary)
    )
    non_claims = _declared_non_claims(request)
    checks: list[dict[str, Any]] = []

    boundary_id = str(
        request.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_id",
            DEFAULT_BOUNDARY_ID,
        )
        or DEFAULT_BOUNDARY_ID
    )
    question = request.get(
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_question"
    )
    intent = request.get(
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_intent"
    )

    _check(
        checks,
        "state packet body exposure boundary question declared",
        isinstance(question, str) and bool(question.strip()),
        "declared boundary question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "boundary intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "boundary block not requested",
        intent != INTENT_BLOCK,
        "intent is not block request",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BLOCK_REQUESTED",
    )

    artifact_path_value = request.get("selected_state_result_object_artifact")
    artifact_missing = request.get("state_result_object_artifact_missing") is True
    _check(
        checks,
        "state result object artifact path declared",
        bool(artifact_path_value) and not artifact_missing,
        "selected state result object artifact path",
        artifact_path_value,
        "STATE_RESULT_OBJECT_ARTIFACT_PATH_MISSING",
    )

    artifact: dict[str, Any] | None = None
    artifact_read_error: str | None = None
    if artifact_path_value and not artifact_missing:
        artifact, artifact_read_error = _read_json_object(artifact_path_value)
    _check(
        checks,
        "state result object artifact readable JSON",
        artifact_read_error is None and artifact is not None,
        "readable JSON object",
        artifact_read_error or "readable JSON object",
        artifact_read_error or "STATE_RESULT_OBJECT_ARTIFACT_UNREADABLE",
    )

    state_result_object = _state_result_object(artifact)
    artifact_outcome = artifact.get("outcome") if artifact else None
    artifact_version = _artifact_result_version(artifact)
    artifact_failed_count = _artifact_failed_check_count(artifact)

    _check(
        checks,
        "state result object artifact outcome recorded",
        artifact_outcome == STATE_RESULT_OBJECT_RECORDED_OUTCOME
        and request.get("state_result_object_artifact_not_recorded") is not True,
        STATE_RESULT_OBJECT_RECORDED_OUTCOME,
        artifact_outcome,
        "STATE_RESULT_OBJECT_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "state result object artifact result version 0.1.0",
        artifact_version == RESULT_VERSION
        and request.get("state_result_object_artifact_version_not_0_1_0") is not True,
        RESULT_VERSION,
        artifact_version,
        "STATE_RESULT_OBJECT_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "state result object artifact failed check count zero",
        artifact_failed_count == 0
        and request.get("state_result_object_artifact_failed_checks_present") is not True,
        0,
        artifact_failed_count,
        "STATE_RESULT_OBJECT_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    selected_command = request.get("selected_command")
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
        selected_command == SELECTED_COMMAND,
        True,
        selected_command == SELECTED_COMMAND,
        "SELECTED_COMMAND_NOT_STATE",
    )

    selected_state_result_object_recorded = (
        state_result_object.get(
            "local_relevance_medium_read_only_state_result_object_recorded"
        )
        is True
    )
    state_result_object_created = (
        state_result_object.get("state_result_object_created") is True
    )
    state_result_object_local_only = (
        state_result_object.get("state_result_object_local_only") is True
    )
    state_result_object_read_only = (
        state_result_object.get("state_result_object_read_only") is True
    )

    _check(
        checks,
        "selected-state result object recorded",
        selected_state_result_object_recorded
        and request.get("selected_state_result_object_not_recorded") is not True,
        True,
        selected_state_result_object_recorded,
        "SELECTED_STATE_RESULT_OBJECT_NOT_RECORDED",
    )
    _check(
        checks,
        "state result object created",
        state_result_object_created
        and request.get("state_result_object_not_created") is not True,
        True,
        state_result_object_created,
        "STATE_RESULT_OBJECT_NOT_CREATED",
    )
    _check(
        checks,
        "state result object local only",
        state_result_object_local_only
        and request.get("state_result_object_local_only_not_true") is not True,
        True,
        state_result_object_local_only,
        "STATE_RESULT_OBJECT_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "state result object read only",
        state_result_object_read_only
        and request.get("state_result_object_read_only_not_true") is not True,
        True,
        state_result_object_read_only,
        "STATE_RESULT_OBJECT_READ_ONLY_NOT_TRUE",
    )

    future_may_be_considered = (
        request.get("future_state_packet_body_exposure_may_not_be_considered") is not True
        and request.get("future_state_packet_body_exposure_may_be_considered", True)
        is not False
    )
    _check(
        checks,
        "future state packet body exposure may be considered",
        future_may_be_considered,
        True,
        future_may_be_considered,
        "FUTURE_STATE_PACKET_BODY_EXPOSURE_MAY_NOT_BE_CONSIDERED",
    )

    boundary_type = request.get("boundary_type")
    boundary_scope = request.get("boundary_scope")
    _check(
        checks,
        "boundary type exact",
        boundary_type == BOUNDARY_TYPE,
        BOUNDARY_TYPE,
        boundary_type,
        "BOUNDARY_TYPE_MISSING"
        if boundary_type is None
        else "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY",
    )
    _check(
        checks,
        "boundary scope exact",
        boundary_scope == BOUNDARY_SCOPE,
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_MISSING"
        if boundary_scope is None
        else "BOUNDARY_SCOPE_NOT_SELECTED_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY",
    )

    false_field_names = {
        "state_packet_body_exposed": "state packet body not exposed",
        "raw_full_state_packet_body_exposed": "raw full state packet body not exposed",
        "lookup_performed": "lookup not performed",
        "lookup_command_executed": "lookup command not executed",
        "operation_permission_created": "operation permission not created",
        "runtime_permission_created": "runtime permission not created",
        "public_api_created": "public API not created",
        "participant_facing_interface_created": "participant-facing interface not created",
        "distributed_network_behavior_created": "distributed network behavior not created",
        "general_lookup_permission_created": "general lookup permission not created",
        "arbitrary_lookup_permission_created": "arbitrary lookup permission not created",
        "unsupported_commands_permitted": "unsupported commands not permitted",
        "unsupported_lookup_keys_permitted": "unsupported lookup keys not permitted",
        "new_lookup_result_created": "no new lookup result created",
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
        "repeated_reception_permission_created": "repeated reception permission not created",
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
        "follow_on_work_authorized": "follow-on work not authorized",
        "artifact_existence_treated_as_state_packet_body_exposure_boundary_authority": (
            "artifact existence not state-packet-body-exposure-boundary authority"
        ),
        "latest_file_posture_treated_as_state_packet_body_exposure_boundary_authority": (
            "latest file posture not state-packet-body-exposure-boundary authority"
        ),
        "repo_local_availability_treated_as_state_packet_body_exposure_boundary_authority": (
            "repo-local availability not state-packet-body-exposure-boundary authority"
        ),
        "hidden_repo_state_used_as_state_packet_body_exposure_boundary_content": (
            "hidden repo state not state-packet-body-exposure-boundary content"
        ),
        "hidden_repo_state_used_as_state_packet_body_exposure_boundary_authority": (
            "hidden repo state not state-packet-body-exposure-boundary authority"
        ),
    }

    for field, check_name in false_field_names.items():
        actual = _false_field_actual(request, non_claims, state_result_object, field)
        code = FALSE_FIELD_BLOCK_CODES.get(field, "NON_CLAIM_MISSING_OR_FLIPPED")
        _check(checks, check_name, actual is False, False, actual, code)

    deployment_actual = _top_or_non_claim(request, "deployment_created", non_claims)
    _check(
        checks,
        "deployment not created",
        deployment_actual in (False, None),
        False,
        deployment_actual if deployment_actual is not None else False,
        "DEPLOYMENT_CREATED",
    )
    public_release_actual = _top_or_non_claim(request, "public_release_created", non_claims)
    _check(
        checks,
        "public release not created",
        public_release_actual in (False, None),
        False,
        public_release_actual if public_release_actual is not None else False,
        "PUBLIC_RELEASE_CREATED",
    )
    broader_permission_actual = _top_or_non_claim(
        request, "broader_reusable_permission_created", non_claims
    )
    _check(
        checks,
        "broader reusable permission not created",
        broader_permission_actual in (False, None),
        False,
        broader_permission_actual if broader_permission_actual is not None else False,
        "BROADER_REUSABLE_PERMISSION_CREATED",
    )

    predecessor_failure_tampered = any(
        _top_or_non_claim(request, key, non_claims) is True
        or request.get(key) is True
        for key in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
    )
    _check(
        checks,
        "predecessor failure evidence preserved",
        not predecessor_failure_tampered,
        "preserved failed-lineage evidence",
        "tampered" if predecessor_failure_tampered else "preserved",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )

    required_non_claims_passed, required_non_claims_actual = _required_non_claims_false(
        non_claims
    )
    _check(
        checks,
        "required non-claims false",
        required_non_claims_passed,
        "all required non-claims present as false bool",
        required_non_claims_actual,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _check(
        checks,
        "result-level required false non-claims canonical false",
        True,
        "canonical false result-level non-claims",
        "canonical false result-level non-claims",
        None,
    )

    boundary = _build_boundary_object(
        boundary_id=boundary_id,
        basis_state_result_object_artifact=(
            str(artifact_path_value) if artifact_path_value else None
        ),
        basis_state_result_object_outcome=artifact_outcome,
        basis_state_result_object_result_version=artifact_version,
        basis_state_result_object_failed_check_count=artifact_failed_count,
        selected_command=selected_command,
        selected_state_result_object_recorded=selected_state_result_object_recorded,
        state_result_object_created=state_result_object_created,
        state_result_object_local_only=state_result_object_local_only,
        state_result_object_read_only=state_result_object_read_only,
        future_state_packet_body_exposure_may_be_considered=future_may_be_considered,
    )

    failed = _has_failed_checks(checks)
    additional_basis = request.get("additional_basis_context", [])
    not_recorded_basis = request.get("not_recorded_basis", [])

    if failed:
        outcome = OUTCOME_BLOCKED
        block_code = _first_failure_code(checks) or OUTCOME_BLOCKED
        block = _block_record(block_code, request.get("block_reason") or block_code)
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
        block = _block_record(None)
        not_recorded_basis = not_recorded_basis or [
            "declared request chose not to record boundary"
        ]
    elif (
        request.get("requested_local_relevance_medium_read_only_state_packet_body_exposure_boundary_outcome")
        == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        or additional_basis
    ):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        block = _block_record(None)
        additional_basis = additional_basis or [
            "additional boundary basis requested by declaration"
        ]
    else:
        outcome = OUTCOME_RECORDED
        block = _block_record(None)

    basis = {
        "selected_state_result_object_artifact": (
            str(artifact_path_value) if artifact_path_value else None
        ),
        "basis_state_result_object_artifact_preserved": outcome == OUTCOME_RECORDED,
        "basis_state_result_object_outcome": artifact_outcome,
        "basis_state_result_object_result_version": artifact_version,
        "basis_state_result_object_failed_check_count": artifact_failed_count,
        "raw_full_state_result_object_artifact_body_returned": False,
    }

    return _assemble_result(
        boundary_id=boundary_id,
        question=question,
        intent=intent,
        selected_state_result_object_artifact_basis=basis,
        boundary=boundary,
        checks=checks,
        outcome=outcome,
        block=block,
        additional_basis_required=additional_basis,
        not_recorded_basis=not_recorded_basis,
    )


def resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_from_path(
    declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary_path: Path
    | str,
) -> dict:
    """Read a declared request JSON object from a path and resolve it."""

    try:
        path = Path(
            declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary_path
        )
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return _minimal_blocked_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_REQUEST_UNREADABLE",
            f"request unreadable: {exc}",
        )
    if not isinstance(value, dict):
        return _minimal_blocked_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_REQUEST_MALFORMED",
            "request JSON is not an object",
        )
    return resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min(
        value
    )


def build_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact summary for a resolver result artifact."""

    checks = result.get(
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_checks",
        [],
    )
    if not isinstance(checks, list):
        checks = []
    passed_check_count = sum(
        1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True
    )
    failed_check_count = sum(
        1 for check in checks if isinstance(check, Mapping) and check.get("passed") is False
    )
    boundary = result.get(
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary", {}
    )
    if not isinstance(boundary, Mapping):
        boundary = {}
    statement = result.get(
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_statement",
        {},
    )
    if not isinstance(statement, Mapping):
        statement = {}
    metadata = result.get(
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_metadata",
        {},
    )
    if not isinstance(metadata, Mapping):
        metadata = {}
    block = result.get("block")
    if not isinstance(block, Mapping):
        block = {}
    non_claims = result.get("non_claims")
    if not isinstance(non_claims, Mapping):
        non_claims = {}

    def false_claim_is_preserved(key: str) -> bool:
        return boundary.get(key) is False and non_claims.get(key) is False

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("reason"),
        "boundary_id": boundary.get("boundary_id")
        or metadata.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_id"
        ),
        "question": result.get(
            "declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary_question"
        ),
        "intent": metadata.get("declared_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "boundary_recorded": statement.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_recorded"
        )
        is True,
        "basis_state_result_object_artifact_preserved": statement.get(
            "basis_state_result_object_artifact_preserved"
        )
        is True,
        "selected_command": boundary.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved")
        is True,
        "selected_command_is_state": statement.get("selected_command_is_state") is True,
        "selected_state_result_object_recorded": statement.get(
            "selected_state_result_object_recorded"
        )
        is True,
        "state_result_object_created": statement.get("state_result_object_created")
        is True,
        "state_result_object_local_only": statement.get("state_result_object_local_only")
        is True,
        "state_result_object_read_only": statement.get("state_result_object_read_only")
        is True,
        "future_state_packet_body_exposure_may_be_considered": statement.get(
            "future_state_packet_body_exposure_may_be_considered"
        )
        is True,
        "boundary_object_summary": {
            "boundary_type": boundary.get("boundary_type"),
            "boundary_scope": boundary.get("boundary_scope"),
            "basis_state_result_object_outcome": boundary.get(
                "basis_state_result_object_outcome"
            ),
            "basis_state_result_object_result_version": boundary.get(
                "basis_state_result_object_result_version"
            ),
            "basis_state_result_object_failed_check_count": boundary.get(
                "basis_state_result_object_failed_check_count"
            ),
        },
        "state_packet_body_not_exposed": false_claim_is_preserved(
            "state_packet_body_exposed"
        ),
        "raw_full_state_packet_body_not_exposed": false_claim_is_preserved(
            "raw_full_state_packet_body_exposed"
        ),
        "lookup_not_performed": false_claim_is_preserved("lookup_performed"),
        "lookup_command_not_executed": false_claim_is_preserved(
            "lookup_command_executed"
        ),
        "operation_permission_not_created": false_claim_is_preserved(
            "operation_permission_created"
        ),
        "runtime_permission_not_created": false_claim_is_preserved(
            "runtime_permission_created"
        ),
        "public_api_not_created": false_claim_is_preserved("public_api_created"),
        "participant_facing_interface_not_created": false_claim_is_preserved(
            "participant_facing_interface_created"
        ),
        "distributed_network_behavior_not_created": false_claim_is_preserved(
            "distributed_network_behavior_created"
        ),
        "general_lookup_permission_not_created": false_claim_is_preserved(
            "general_lookup_permission_created"
        ),
        "arbitrary_lookup_permission_not_created": false_claim_is_preserved(
            "arbitrary_lookup_permission_created"
        ),
        "unsupported_commands_not_permitted": false_claim_is_preserved(
            "unsupported_commands_permitted"
        ),
        "unsupported_lookup_keys_not_permitted": false_claim_is_preserved(
            "unsupported_lookup_keys_permitted"
        ),
        "no_new_lookup_result_or_entry_created": false_claim_is_preserved(
            "new_lookup_result_created"
        )
        and false_claim_is_preserved("new_lookup_entry_created"),
        "no_new_signal_entry_relevance_object_or_index_entry_created": (
            false_claim_is_preserved("new_signal_accepted")
            and false_claim_is_preserved("new_entry_accepted")
            and false_claim_is_preserved("new_relevance_object_created")
            and false_claim_is_preserved("new_index_entry_created")
        ),
        "filesystem_discovery_not_performed": false_claim_is_preserved(
            "filesystem_discovery_performed"
        ),
        "registry_search_query_surface_ranking_not_created": (
            false_claim_is_preserved("registry_created")
            and false_claim_is_preserved("search_surface_created")
            and false_claim_is_preserved("query_surface_created")
            and false_claim_is_preserved("ranking_surface_created")
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": (
            false_claim_is_preserved("scoring_surface_created")
            and false_claim_is_preserved("priority_surface_created")
            and false_claim_is_preserved("validity_judgment_created")
            and false_claim_is_preserved("truth_judgment_created")
            and false_claim_is_preserved("authority_judgment_created")
            and false_claim_is_preserved("currentness_judgment_created")
        ),
        "repeated_reception_arbitrary_reception_feed_not_created": (
            false_claim_is_preserved("repeated_reception_permission_created")
            and false_claim_is_preserved("arbitrary_reception_created")
            and false_claim_is_preserved("feed_created")
        ),
        "source_authority_currentness_truth_synchronization_participation_participant_role_not_created": (
            false_claim_is_preserved("source_transfer_occurred")
            and false_claim_is_preserved("source_receipt_occurred")
            and false_claim_is_preserved("source_created")
            and false_claim_is_preserved("authority_created")
            and false_claim_is_preserved("currentness_created")
            and false_claim_is_preserved("truth_created")
            and false_claim_is_preserved("synchronization_created")
            and false_claim_is_preserved("participation_authorized")
            and false_claim_is_preserved("participant_role_created")
        ),
        "follow_on_not_created": false_claim_is_preserved("follow_on_work_authorized"),
        "key_non_claims": {
            key: non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        },
        "predecessor_failure_evidence_preserved": (
            non_claims.get("predecessor_failure_repaired") is False
            and non_claims.get("predecessor_failure_hidden") is False
            and non_claims.get("predecessor_failure_claimed_passed") is False
        ),
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def write_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result artifact without silently overwriting files."""

    if not isinstance(result, Mapping):
        raise LocalRelevanceMediumReadOnlyStatePacketBodyExposureBoundaryV0MinError(
            "result must be a mapping"
        )
    metadata = result.get(
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_metadata",
        {},
    )
    boundary = result.get(
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary",
        {},
    )
    boundary_id = None
    if isinstance(metadata, Mapping):
        boundary_id = metadata.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_id"
        )
    if not boundary_id and isinstance(boundary, Mapping):
        boundary_id = boundary.get("boundary_id")
    boundary_id = str(boundary_id or DEFAULT_BOUNDARY_ID)
    filename = (
        f"{boundary_id}__"
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_result.json"
    )

    if output_path is None:
        candidate = OUTPUT_ROOT / filename
    else:
        output = Path(output_path)
        candidate = output if output.suffix == ".json" else output / filename
    candidate.parent.mkdir(parents=True, exist_ok=True)

    if candidate.exists():
        stem = candidate.stem
        suffix = candidate.suffix
        parent = candidate.parent
        index = 1
        while True:
            replacement = parent / f"{stem}_{index:03d}{suffix}"
            if not replacement.exists():
                candidate = replacement
                break
            index += 1

    candidate.write_text(
        json.dumps(_sanitize(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return candidate


def build_declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_request(
    *,
    local_relevance_medium_read_only_state_packet_body_exposure_boundary_id: str = DEFAULT_BOUNDARY_ID,
    selected_state_result_object_artifact: Path | str | None = None,
    selected_command: str = SELECTED_COMMAND,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared request with canonical false non-claims."""

    if selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyStatePacketBodyExposureBoundaryV0MinError(
            "selected_command must be state"
        )
    non_claims = _canonical_false_non_claims()
    if declared_non_claims is not None:
        non_claims.update(copy.deepcopy(dict(declared_non_claims)))
    request: dict[str, Any] = {
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_id": (
            local_relevance_medium_read_only_state_packet_body_exposure_boundary_id
        ),
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_question": CORE_QUESTION,
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_intent": intent,
        "selected_state_result_object_artifact": str(
            selected_state_result_object_artifact
            if selected_state_result_object_artifact is not None
            else DEFAULT_STATE_RESULT_OBJECT_ARTIFACT
        ),
        "selected_command": selected_command,
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "future_state_packet_body_exposure_may_be_considered": True,
        "declared_non_claims": non_claims,
    }
    request.update(copy.deepcopy(overrides))
    return request
