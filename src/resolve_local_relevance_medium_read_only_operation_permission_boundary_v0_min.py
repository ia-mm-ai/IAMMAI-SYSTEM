"""Resolve one local read-only operation-permission boundary.

This resolver reads one clean
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT artifact as selected-state
lookup-result basis. It records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY object only.

The object is boundary-shaped, local, read-only,
selected-state-operation-permission-consideration-only, closure-token-aware,
non-operation-permission-shaped, non-operation-execution-shaped, and
non-runtime-shaped. It may record that one future local read-only operation
permission may be considered as a separately bounded step. It does not create
operation permission, operation execution, runtime permission, public or
distributed surfaces, unsupported commands or keys, registry/search/query/
ranking surfaces, filesystem discovery, source movement, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyOperationPermissionBoundaryV0MinError(RuntimeError):
    """Bounded resolver error for operation permission boundary handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_operation_permission_boundary_v0_min"
)

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_BLOCKED"
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
    "operation_permission_boundary_v0_min"
)
DEFAULT_LOOKUP_RESULT_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_result_v0_min/"
    "local_relevance_medium_read_only_lookup_result_reference_review_001__"
    "local_relevance_medium_read_only_lookup_result_v0_min_result.json"
)

DEFAULT_BOUNDARY_ID = "local_relevance_medium_read_only_operation_permission_boundary_001"
BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_OPERATION_PERMISSION_CONSIDERATION_ONLY"
SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)
SELECTED_COMMAND = "state"

LOOKUP_RESULT_RECORDED_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_RECORDED"

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT for selected "
    "command state, existing reusable read-only lookup permission, prior "
    "lookup-pair coverage, and prior local carrier command surface, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY be recorded "
    "that permits a future local read-only operation permission to be considered "
    "as a separately bounded step, without creating operation permission, "
    "creating operation execution, creating runtime permission, creating public "
    "API, creating participant-facing interface, creating distributed network "
    "behavior, creating general operation permission, creating general lookup "
    "permission, creating arbitrary lookup permission, permitting unsupported "
    "commands, permitting unsupported lookup keys, creating new lookup entry "
    "beyond the already bounded selected-state lookup result object, accepting "
    "new entries, accepting new signals, performing filesystem discovery, "
    "creating query surface, registry, search, ranking, scoring, priority, "
    "validity judgment, truth judgment, authority, currentness, synchronization, "
    "participation authorization, participant role, repeated reception "
    "permission, arbitrary reception, feed, source transfer, source receipt, "
    "or follow-on work?"
)

BOUNDARY_OBJECT_FALSE_FIELDS = (
    "operation_permission_created",
    "operation_execution_created",
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
    "artifact_existence_treated_as_operation_permission_boundary_authority",
    "latest_file_posture_treated_as_operation_permission_boundary_authority",
    "repo_local_availability_treated_as_operation_permission_boundary_authority",
    "hidden_repo_state_used_as_operation_permission_boundary_content",
    "hidden_repo_state_used_as_operation_permission_boundary_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

REQUIRED_FALSE_NON_CLAIMS = BOUNDARY_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_operation_permission_boundary_recorded",
    "basis_lookup_result_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_lookup_result_recorded",
    "lookup_result_created",
    "lookup_result_local_only",
    "lookup_result_read_only",
    "future_operation_permission_may_be_considered",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_BLOCK_REQUESTED",
    "LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
    "LOOKUP_RESULT_ARTIFACT_UNREADABLE",
    "LOOKUP_RESULT_ARTIFACT_NOT_JSON_OBJECT",
    "LOOKUP_RESULT_ARTIFACT_NOT_RECORDED",
    "LOOKUP_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOOKUP_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_LOOKUP_RESULT_NOT_RECORDED",
    "LOOKUP_RESULT_NOT_CREATED",
    "LOOKUP_RESULT_LOCAL_ONLY_NOT_TRUE",
    "LOOKUP_RESULT_READ_ONLY_NOT_TRUE",
    "FUTURE_OPERATION_PERMISSION_MAY_NOT_BE_CONSIDERED",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_SELECTED_OPERATION_PERMISSION_CONSIDERATION_ONLY",
    "OPERATION_PERMISSION_CREATED",
    "OPERATION_EXECUTION_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_OPERATION_PERMISSION_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_OPERATION_PERMISSION_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_OPERATION_PERMISSION_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_OPERATION_PERMISSION_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_OPERATION_PERMISSION_BOUNDARY_AUTHORITY",
    "PRIOR_ARTIFACTS_MUTATED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_REQUEST_UNREADABLE",
)

_FALSE_FIELD_BLOCK_CODES = {
    "operation_permission_created": "OPERATION_PERMISSION_CREATED",
    "operation_execution_created": "OPERATION_EXECUTION_CREATED",
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
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "artifact_existence_treated_as_operation_permission_boundary_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_OPERATION_PERMISSION_BOUNDARY_AUTHORITY"
    ),
    "latest_file_posture_treated_as_operation_permission_boundary_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_OPERATION_PERMISSION_BOUNDARY_AUTHORITY"
    ),
    "repo_local_availability_treated_as_operation_permission_boundary_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_OPERATION_PERMISSION_BOUNDARY_AUTHORITY"
    ),
    "hidden_repo_state_used_as_operation_permission_boundary_content": (
        "HIDDEN_REPO_STATE_USED_AS_OPERATION_PERMISSION_BOUNDARY_CONTENT"
    ),
    "hidden_repo_state_used_as_operation_permission_boundary_authority": (
        "HIDDEN_REPO_STATE_USED_AS_OPERATION_PERMISSION_BOUNDARY_AUTHORITY"
    ),
    "prior_artifacts_mutated": "PRIOR_ARTIFACTS_MUTATED",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
}

_SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_operation_permission_boundary_body",
    "raw_operation_permission_body",
    "raw_operation_execution_body",
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
    "operation_permission_boundary_body",
    "operation_permission_body",
    "operation_execution_body",
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

_HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN",
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


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _is_mapping(value: Any) -> bool:
    return isinstance(value, MappingABC)


def _sanitize(value: Any, key: str | None = None) -> Any:
    if key is not None and (key in _SENSITIVE_CONTENT_KEYS or key.endswith("_body")):
        return "[REDACTED_RAW_BODY]"
    if _is_mapping(value):
        return {str(item_key): _sanitize(item_value, str(item_key)) for item_key, item_value in value.items()}
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    if isinstance(value, str) and any(sentinel in value for sentinel in _HOSTILE_SENTINELS):
        return "[REDACTED_RAW_BODY]"
    return value


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _path_to_string(path_value: Path | str | None) -> str | None:
    if path_value is None:
        return None
    return str(Path(path_value))


def _read_json_object(path_value: Path | str | None) -> tuple[dict[str, Any] | None, str | None, str | None]:
    if path_value is None or str(path_value) == "":
        return None, "PATH_MISSING", "artifact path is missing"
    path = Path(path_value)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception as exc:
        return None, "UNREADABLE", f"artifact could not be read as JSON: {exc}"
    if not _is_mapping(loaded):
        return None, "NOT_JSON_OBJECT", "artifact JSON is not an object"
    return dict(loaded), None, None


def _nested_get(mapping: Mapping[str, Any], path: tuple[str, ...]) -> Any:
    current: Any = mapping
    for part in path:
        if not _is_mapping(current) or part not in current:
            return None
        current = current[part]
    return current


def _first_present(mapping: Mapping[str, Any], paths: tuple[tuple[str, ...], ...]) -> Any:
    for path in paths:
        value = _nested_get(mapping, path)
        if value is not None:
            return value
    return None


def _as_int_or_none(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    return None


def _artifact_common(data: Mapping[str, Any], object_key: str, version_key: str) -> dict[str, Any]:
    return {
        "outcome": _first_present(
            data,
            (
                ("outcome",),
                (f"{object_key}_summary", "outcome"),
                (f"{object_key}_metadata", "outcome"),
            ),
        ),
        "result_version": _first_present(
            data,
            (
                ("result_version",),
                (f"{object_key}_summary", "result_version"),
                (f"{object_key}_metadata", "result_version"),
                (object_key, version_key),
            ),
        ),
        "failed_check_count": _as_int_or_none(
            _first_present(
                data,
                (
                    ("failed_check_count",),
                    (f"{object_key}_summary", "failed_check_count"),
                    (f"{object_key}_metadata", "failed_check_count"),
                ),
            )
        ),
    }


def _extract_lookup_result_basis(
    artifact_path: Path | str | None,
    artifact_data: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if artifact_data is None:
        return {
            "artifact_path": _path_to_string(artifact_path),
            "artifact_readable_json": False,
            "artifact_json_object": False,
            "artifact_outcome": None,
            "artifact_result_version": None,
            "artifact_failed_check_count": None,
            "basis_kind": "selected_state_lookup_result_basis_only",
        }
    common = _artifact_common(
        artifact_data,
        "local_relevance_medium_read_only_lookup_result",
        "lookup_result_version",
    )
    lookup_result_object = artifact_data.get("local_relevance_medium_read_only_lookup_result", {})
    statement = artifact_data.get("local_relevance_medium_read_only_lookup_result_statement", {})
    summary = artifact_data.get("local_relevance_medium_read_only_lookup_result_summary", {})
    if not _is_mapping(lookup_result_object):
        lookup_result_object = {}
    if not _is_mapping(statement):
        statement = {}
    if not _is_mapping(summary):
        summary = {}
    layers = {
        "object": lookup_result_object,
        "statement": statement,
        "summary": summary,
    }
    return {
        "artifact_path": _path_to_string(artifact_path),
        "artifact_readable_json": True,
        "artifact_json_object": True,
        "artifact_outcome": common["outcome"],
        "artifact_result_version": common["result_version"],
        "artifact_failed_check_count": common["failed_check_count"],
        "basis_kind": "selected_state_lookup_result_basis_only",
        "selected_command": _first_present(
            layers,
            (
                ("object", "selected_command"),
                ("summary", "selected_command"),
            ),
        ),
        "selected_command_is_state": _first_present(
            layers,
            (
                ("object", "selected_command_is_state"),
                ("statement", "selected_command_is_state"),
                ("summary", "selected_command_is_state"),
            ),
        ),
        "selected_lookup_result_recorded": _first_present(
            layers,
            (
                ("object", "local_relevance_medium_read_only_lookup_result_recorded"),
                ("statement", "local_relevance_medium_read_only_lookup_result_recorded"),
                ("summary", "lookup_result_recorded"),
                ("summary", "local_relevance_medium_read_only_lookup_result_recorded"),
            ),
        ),
        "lookup_result_created": _first_present(
            layers,
            (
                ("object", "lookup_result_created"),
                ("statement", "lookup_result_created"),
                ("summary", "lookup_result_created"),
            ),
        ),
        "lookup_result_local_only": _first_present(
            layers,
            (
                ("object", "lookup_result_local_only"),
                ("statement", "lookup_result_local_only"),
                ("summary", "lookup_result_local_only"),
            ),
        ),
        "lookup_result_read_only": _first_present(
            layers,
            (
                ("object", "lookup_result_read_only"),
                ("statement", "lookup_result_read_only"),
                ("summary", "lookup_result_read_only"),
            ),
        ),
    }


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> None:
    code = None if passed else block_code
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _sanitize(expected_posture),
            "actual_posture": _sanitize(actual_posture),
            "block_code": code,
            "failure_code": code,
        }
    )


def _failed_codes(checks: list[dict[str, Any]]) -> list[str]:
    codes: list[str] = []
    for check in checks:
        if check.get("passed") is True:
            continue
        code = check.get("block_code") or check.get("failure_code")
        if isinstance(code, str) and code:
            codes.append(code)
    return codes


def _first_failed_code(checks: list[dict[str, Any]], default: str) -> str:
    codes = _failed_codes(checks)
    if codes:
        return codes[0]
    return default


def _has_false_shortcut(declared: Mapping[str, Any], key: str) -> bool:
    return declared.get(key) is True


def _declared_false_field_passed(declared: Mapping[str, Any], field: str) -> bool:
    if field not in declared:
        return True
    return declared[field] is False


def _declared_non_claims_passed(declared_non_claims: Any) -> tuple[bool, dict[str, Any]]:
    details: dict[str, Any] = {}
    if not _is_mapping(declared_non_claims):
        return False, {"declared_non_claims": "missing_or_not_mapping"}
    for key in REQUIRED_FALSE_NON_CLAIMS:
        value = declared_non_claims.get(key)
        if value is not False:
            details[key] = _sanitize(value)
    return not details, details


def _build_boundary_object(
    *,
    recorded: bool,
    boundary_id: str,
    lookup_result_basis: Mapping[str, Any],
    selected_command: Any,
) -> dict[str, Any]:
    return {
        "boundary_id": boundary_id,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "basis_lookup_result_artifact": lookup_result_basis.get("artifact_path"),
        "basis_lookup_result_outcome": lookup_result_basis.get("artifact_outcome"),
        "basis_lookup_result_result_version": lookup_result_basis.get("artifact_result_version"),
        "basis_lookup_result_failed_check_count": lookup_result_basis.get("artifact_failed_check_count"),
        "selected_command": (
            selected_command
            if selected_command == SELECTED_COMMAND
            else lookup_result_basis.get("selected_command")
        ),
        "selected_command_is_state": bool(recorded),
        "selected_lookup_result_recorded": bool(recorded),
        "lookup_result_created": bool(recorded),
        "lookup_result_local_only": bool(recorded),
        "lookup_result_read_only": bool(recorded),
        "future_operation_permission_may_be_considered": bool(recorded),
        "operation_permission_created": False,
        "operation_execution_created": False,
        "runtime_permission_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "general_operation_permission_created": False,
        "general_lookup_permission_created": False,
        "arbitrary_lookup_permission_created": False,
        "unsupported_commands_permitted": False,
        "unsupported_lookup_keys_permitted": False,
        "new_lookup_entry_created": False,
        "new_signal_accepted": False,
        "new_entry_accepted": False,
        "new_relevance_object_created": False,
        "new_index_entry_created": False,
        "filesystem_discovery_performed": False,
        "registry_created": False,
        "search_surface_created": False,
        "query_surface_created": False,
        "ranking_surface_created": False,
        "scoring_surface_created": False,
        "priority_surface_created": False,
        "validity_judgment_created": False,
        "truth_judgment_created": False,
        "authority_judgment_created": False,
        "currentness_judgment_created": False,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "authority_created": False,
        "currentness_created": False,
        "truth_created": False,
        "synchronization_created": False,
        "participation_authorized": False,
        "participant_role_created": False,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
        "follow_on_work_authorized": False,
    }


def _build_statement(
    *,
    recorded: bool,
    lookup_result_basis: Mapping[str, Any],
) -> dict[str, bool]:
    return {
        "local_relevance_medium_read_only_operation_permission_boundary_recorded": bool(recorded),
        "basis_lookup_result_artifact_preserved": bool(
            lookup_result_basis.get("artifact_readable_json")
        ),
        "selected_command_preserved": bool(recorded),
        "selected_command_is_state": bool(recorded),
        "selected_lookup_result_recorded": bool(recorded),
        "lookup_result_created": bool(recorded),
        "lookup_result_local_only": bool(recorded),
        "lookup_result_read_only": bool(recorded),
        "future_operation_permission_may_be_considered": bool(recorded),
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "operation_permission_created": False,
        "operation_execution_created": False,
        "runtime_permission_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "general_operation_permission_created": False,
        "general_lookup_permission_created": False,
        "arbitrary_lookup_permission_created": False,
        "unsupported_commands_permitted": False,
        "unsupported_lookup_keys_permitted": False,
        "new_lookup_entry_created_beyond_bounded_lookup_result_object": False,
        "registry_created": False,
        "search_surface_created": False,
        "query_surface_created": False,
        "ranking_surface_created": False,
        "operation_permission_inferred_from_lookup_result": False,
        "operation_execution_inferred_from_boundary": False,
        "runtime_permission_inferred_from_boundary": False,
        "follow_on_work_authorized": False,
    }


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium read-only operation permission boundary test",
        "local relevance medium read-only operation permission boundary live artifact",
        "local relevance medium read-only operation permission boundary terminal summary, if separately selected",
        "operation permission",
        "operation execution",
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
        "follow-on work",
    ]


def _build_result_artifact(
    *,
    declared: Mapping[str, Any] | None,
    outcome: str,
    checks: list[dict[str, Any]],
    lookup_result_basis: Mapping[str, Any],
    recorded: bool,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    boundary_id = DEFAULT_BOUNDARY_ID
    selected_command = SELECTED_COMMAND
    question = None
    intent = None
    additional_basis_required: Any = []
    not_recorded_basis: Any = []
    if declared is not None:
        boundary_id = str(
            declared.get("local_relevance_medium_read_only_operation_permission_boundary_id")
            or DEFAULT_BOUNDARY_ID
        )
        question = declared.get("local_relevance_medium_read_only_operation_permission_boundary_question")
        intent = declared.get("local_relevance_medium_read_only_operation_permission_boundary_intent")
        selected_command = declared.get("selected_command", SELECTED_COMMAND)
        additional_basis_required = declared.get("additional_basis_context", [])
        not_recorded_basis = declared.get("not_recorded_basis", [])

    metadata = {
        "local_relevance_medium_read_only_operation_permission_boundary_id": boundary_id,
        "local_relevance_medium_read_only_operation_permission_boundary_type": BOUNDARY_TYPE,
        "local_relevance_medium_read_only_operation_permission_boundary_version": RESULT_VERSION,
        "result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }
    boundary = _build_boundary_object(
        recorded=recorded,
        boundary_id=boundary_id,
        lookup_result_basis=lookup_result_basis,
        selected_command=selected_command,
    )
    statement = _build_statement(recorded=recorded, lookup_result_basis=lookup_result_basis)

    effective_block_code = block_code
    if outcome == OUTCOME_BLOCKED and effective_block_code is None:
        effective_block_code = _first_failed_code(
            checks,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_REQUEST_MALFORMED",
        )
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": effective_block_code if outcome == OUTCOME_BLOCKED else None,
        "block_code": effective_block_code if outcome == OUTCOME_BLOCKED else None,
        "reason": _sanitize(block_reason) if outcome == OUTCOME_BLOCKED else None,
    }

    result: dict[str, Any] = {
        "local_relevance_medium_read_only_operation_permission_boundary_metadata": metadata,
        "declared_local_relevance_medium_read_only_operation_permission_boundary_question": {
            "question": _sanitize(question),
            "intent": _sanitize(intent),
            "selected_command": _sanitize(selected_command),
            "boundary_type": BOUNDARY_TYPE,
            "boundary_scope": BOUNDARY_SCOPE,
        },
        "selected_lookup_result_artifact_basis": _sanitize(dict(lookup_result_basis)),
        "local_relevance_medium_read_only_operation_permission_boundary": _sanitize(boundary),
        "local_relevance_medium_read_only_operation_permission_boundary_checks": _sanitize(checks),
        "local_relevance_medium_read_only_operation_permission_boundary_statement": _sanitize(statement),
        "local_relevance_medium_read_only_operation_permission_boundary_non_meaning": _sanitize(_build_non_meaning()),
        "additional_basis_required": _sanitize(additional_basis_required),
        "not_recorded_basis": _sanitize(not_recorded_basis),
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["local_relevance_medium_read_only_operation_permission_boundary_summary"] = (
        build_local_relevance_medium_read_only_operation_permission_boundary_v0_min_summary(result)
    )
    return result


def _blocked_malformed_result(code: str, reason: str) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _add_check(
        checks,
        "declared local relevance medium read-only operation permission boundary request is mapping",
        False,
        "mapping request",
        reason,
        code,
    )
    return _build_result_artifact(
        declared=None,
        outcome=OUTCOME_BLOCKED,
        checks=checks,
        lookup_result_basis=_extract_lookup_result_basis(None, None),
        recorded=False,
        block_code=code,
        block_reason=reason,
    )


def resolve_local_relevance_medium_read_only_operation_permission_boundary_v0_min(
    declared_local_relevance_medium_read_only_operation_permission_boundary: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded local read-only operation permission boundary request."""

    if declared_local_relevance_medium_read_only_operation_permission_boundary is None:
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_REQUEST_MALFORMED",
            "declared operation permission boundary request is missing",
        )
    if not _is_mapping(declared_local_relevance_medium_read_only_operation_permission_boundary):
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_REQUEST_MALFORMED",
            "declared operation permission boundary request is not a mapping",
        )

    declared: dict[str, Any] = copy.deepcopy(
        dict(declared_local_relevance_medium_read_only_operation_permission_boundary)
    )
    checks: list[dict[str, Any]] = []

    question = declared.get("local_relevance_medium_read_only_operation_permission_boundary_question")
    intent = declared.get("local_relevance_medium_read_only_operation_permission_boundary_intent")
    selected_command = declared.get("selected_command")
    boundary_type = declared.get("boundary_type")
    boundary_scope = declared.get("boundary_scope")

    _add_check(
        checks,
        "operation permission boundary question declared",
        isinstance(question, str) and bool(question.strip()),
        "declared operation permission boundary question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_QUESTION_UNDECLARED",
    )
    _add_check(
        checks,
        "operation permission boundary intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _add_check(
        checks,
        "operation permission boundary block intent not requested",
        intent != INTENT_BLOCK,
        "intent is not BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_BLOCK_REQUESTED",
    )

    lookup_result_artifact_path = declared.get("selected_lookup_result_artifact")
    lookup_result_path_declared = bool(lookup_result_artifact_path) and not _has_false_shortcut(
        declared,
        "lookup_result_artifact_missing",
    )
    _add_check(
        checks,
        "lookup result artifact path declared",
        lookup_result_path_declared,
        "selected lookup result artifact path",
        lookup_result_artifact_path,
        "LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
    )

    lookup_result_data, read_error, read_reason = _read_json_object(lookup_result_artifact_path)
    _add_check(
        checks,
        "lookup result artifact readable JSON",
        read_error in (None, "NOT_JSON_OBJECT"),
        "readable JSON",
        read_reason if read_error else "readable JSON",
        "LOOKUP_RESULT_ARTIFACT_UNREADABLE",
    )
    _add_check(
        checks,
        "lookup result artifact JSON object",
        read_error is None,
        "JSON object",
        read_reason if read_error else "JSON object",
        "LOOKUP_RESULT_ARTIFACT_NOT_JSON_OBJECT",
    )

    lookup_result_basis = _extract_lookup_result_basis(
        lookup_result_artifact_path,
        lookup_result_data,
    )

    _add_check(
        checks,
        "lookup result artifact outcome recorded",
        lookup_result_basis.get("artifact_outcome") == LOOKUP_RESULT_RECORDED_OUTCOME
        and not _has_false_shortcut(declared, "lookup_result_artifact_not_recorded"),
        LOOKUP_RESULT_RECORDED_OUTCOME,
        lookup_result_basis.get("artifact_outcome"),
        "LOOKUP_RESULT_ARTIFACT_NOT_RECORDED",
    )
    _add_check(
        checks,
        "lookup result artifact result version 0.1.0",
        lookup_result_basis.get("artifact_result_version") == RESULT_VERSION
        and not _has_false_shortcut(declared, "lookup_result_artifact_version_not_0_1_0"),
        RESULT_VERSION,
        lookup_result_basis.get("artifact_result_version"),
        "LOOKUP_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _add_check(
        checks,
        "lookup result artifact failed check count zero",
        lookup_result_basis.get("artifact_failed_check_count") == 0
        and not _has_false_shortcut(declared, "lookup_result_artifact_failed_checks_present"),
        0,
        lookup_result_basis.get("artifact_failed_check_count"),
        "LOOKUP_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    _add_check(
        checks,
        "selected command declared",
        selected_command is not None and not _has_false_shortcut(declared, "selected_command_missing"),
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_MISSING",
    )
    _add_check(
        checks,
        "selected command exactly state",
        selected_command == SELECTED_COMMAND and not _has_false_shortcut(declared, "selected_command_not_state"),
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _add_check(
        checks,
        "selected command is state",
        lookup_result_basis.get("selected_command_is_state") is True
        and lookup_result_basis.get("selected_command") == SELECTED_COMMAND,
        True,
        {
            "selected_command": lookup_result_basis.get("selected_command"),
            "selected_command_is_state": lookup_result_basis.get("selected_command_is_state"),
        },
        "SELECTED_COMMAND_NOT_STATE",
    )
    _add_check(
        checks,
        "selected lookup result recorded",
        lookup_result_basis.get("selected_lookup_result_recorded") is True
        and not _has_false_shortcut(declared, "selected_lookup_result_not_recorded"),
        True,
        lookup_result_basis.get("selected_lookup_result_recorded"),
        "SELECTED_LOOKUP_RESULT_NOT_RECORDED",
    )
    _add_check(
        checks,
        "lookup result created",
        lookup_result_basis.get("lookup_result_created") is True
        and declared.get("lookup_result_created", True) is True
        and not _has_false_shortcut(declared, "lookup_result_not_created"),
        True,
        {
            "artifact": lookup_result_basis.get("lookup_result_created"),
            "declared": declared.get("lookup_result_created", True),
        },
        "LOOKUP_RESULT_NOT_CREATED",
    )
    _add_check(
        checks,
        "lookup result local only",
        lookup_result_basis.get("lookup_result_local_only") is True
        and declared.get("lookup_result_local_only", True) is True
        and not _has_false_shortcut(declared, "lookup_result_local_only_not_true"),
        True,
        {
            "artifact": lookup_result_basis.get("lookup_result_local_only"),
            "declared": declared.get("lookup_result_local_only", True),
        },
        "LOOKUP_RESULT_LOCAL_ONLY_NOT_TRUE",
    )
    _add_check(
        checks,
        "lookup result read only",
        lookup_result_basis.get("lookup_result_read_only") is True
        and declared.get("lookup_result_read_only", True) is True
        and not _has_false_shortcut(declared, "lookup_result_read_only_not_true"),
        True,
        {
            "artifact": lookup_result_basis.get("lookup_result_read_only"),
            "declared": declared.get("lookup_result_read_only", True),
        },
        "LOOKUP_RESULT_READ_ONLY_NOT_TRUE",
    )
    _add_check(
        checks,
        "future operation permission may be considered",
        declared.get("future_operation_permission_may_be_considered", True) is True
        and not _has_false_shortcut(declared, "future_operation_permission_may_not_be_considered"),
        True,
        declared.get("future_operation_permission_may_be_considered", True),
        "FUTURE_OPERATION_PERMISSION_MAY_NOT_BE_CONSIDERED",
    )

    _add_check(
        checks,
        "boundary type declared",
        boundary_type is not None,
        BOUNDARY_TYPE,
        boundary_type,
        "BOUNDARY_TYPE_MISSING",
    )
    _add_check(
        checks,
        "boundary type local relevance medium read-only operation permission boundary",
        boundary_type == BOUNDARY_TYPE
        and not _has_false_shortcut(
            declared,
            "boundary_type_not_local_relevance_medium_read_only_operation_permission_boundary",
        ),
        BOUNDARY_TYPE,
        boundary_type,
        "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY",
    )
    _add_check(
        checks,
        "boundary scope declared",
        boundary_scope is not None,
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_MISSING",
    )
    _add_check(
        checks,
        "boundary scope selected operation permission consideration only",
        boundary_scope == BOUNDARY_SCOPE
        and not _has_false_shortcut(
            declared,
            "boundary_scope_not_selected_operation_permission_consideration_only",
        ),
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_NOT_SELECTED_OPERATION_PERMISSION_CONSIDERATION_ONLY",
    )

    for field in REQUIRED_FALSE_NON_CLAIMS:
        code = _FALSE_FIELD_BLOCK_CODES.get(field, "NON_CLAIM_MISSING_OR_FLIPPED")
        _add_check(
            checks,
            f"{field} remains false",
            _declared_false_field_passed(declared, field),
            False,
            declared.get(field, False),
            code,
        )

    declared_non_claims_passed, declared_non_claims_details = _declared_non_claims_passed(
        declared.get("declared_non_claims")
    )
    _add_check(
        checks,
        "required non-claims false",
        declared_non_claims_passed,
        "every required declared non-claim present as false bool",
        declared_non_claims_details if declared_non_claims_details else "all required non-claims false",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _add_check(
        checks,
        "predecessor failure evidence preserved",
        declared.get("predecessor_failure_repaired") is not True
        and declared.get("predecessor_failure_hidden") is not True
        and declared.get("predecessor_failure_claimed_passed") is not True,
        "predecessor failure remains preserved evidence only",
        {
            "predecessor_failure_repaired": declared.get("predecessor_failure_repaired", False),
            "predecessor_failure_hidden": declared.get("predecessor_failure_hidden", False),
            "predecessor_failure_claimed_passed": declared.get("predecessor_failure_claimed_passed", False),
        },
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _add_check(
        checks,
        "result-level required false non-claims canonical false",
        True,
        "final result-level non_claims canonical false",
        "canonical false",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    failed_codes = _failed_codes(checks)
    if failed_codes:
        outcome = OUTCOME_BLOCKED
        recorded = False
        block_code = failed_codes[0]
        block_reason = declared.get("block_reason") or block_code
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
        recorded = False
        block_code = None
        block_reason = None
    elif (
        declared.get("requested_local_relevance_medium_read_only_operation_permission_boundary_outcome")
        == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    ):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        recorded = False
        block_code = None
        block_reason = None
    else:
        outcome = OUTCOME_RECORDED
        recorded = True
        block_code = None
        block_reason = None

    return _build_result_artifact(
        declared=declared,
        outcome=outcome,
        checks=checks,
        lookup_result_basis=lookup_result_basis,
        recorded=recorded,
        block_code=block_code,
        block_reason=block_reason,
    )


def resolve_local_relevance_medium_read_only_operation_permission_boundary_v0_min_from_path(
    declared_local_relevance_medium_read_only_operation_permission_boundary_path: Path | str,
) -> dict[str, Any]:
    """Read a declared request JSON object from a path and resolve it."""

    path = Path(declared_local_relevance_medium_read_only_operation_permission_boundary_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception as exc:
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_REQUEST_UNREADABLE",
            f"declared operation permission boundary request could not be read: {exc}",
        )
    if not _is_mapping(loaded):
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_REQUEST_MALFORMED",
            "declared operation permission boundary request JSON is not an object",
        )
    return resolve_local_relevance_medium_read_only_operation_permission_boundary_v0_min(dict(loaded))


def build_local_relevance_medium_read_only_operation_permission_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact JSON-safe summary for a resolver result artifact."""

    checks = result.get("local_relevance_medium_read_only_operation_permission_boundary_checks", [])
    if not isinstance(checks, list):
        checks = []
    passed_check_count = sum(1 for check in checks if _is_mapping(check) and check.get("passed") is True)
    failed_check_count = sum(1 for check in checks if _is_mapping(check) and check.get("passed") is not True)
    metadata = result.get("local_relevance_medium_read_only_operation_permission_boundary_metadata", {})
    if not _is_mapping(metadata):
        metadata = {}
    question = result.get("declared_local_relevance_medium_read_only_operation_permission_boundary_question", {})
    if not _is_mapping(question):
        question = {}
    boundary = result.get("local_relevance_medium_read_only_operation_permission_boundary", {})
    if not _is_mapping(boundary):
        boundary = {}
    statement = result.get("local_relevance_medium_read_only_operation_permission_boundary_statement", {})
    if not _is_mapping(statement):
        statement = {}
    block = result.get("block", {})
    if not _is_mapping(block):
        block = {}
    non_claims = result.get("non_claims", {})
    if not _is_mapping(non_claims):
        non_claims = {}
    key_non_claims = {
        "operation_permission_created": non_claims.get("operation_permission_created", False),
        "operation_execution_created": non_claims.get("operation_execution_created", False),
        "runtime_permission_created": non_claims.get("runtime_permission_created", False),
        "public_api_created": non_claims.get("public_api_created", False),
        "participant_facing_interface_created": non_claims.get("participant_facing_interface_created", False),
        "distributed_network_behavior_created": non_claims.get("distributed_network_behavior_created", False),
        "general_operation_permission_created": non_claims.get("general_operation_permission_created", False),
        "general_lookup_permission_created": non_claims.get("general_lookup_permission_created", False),
        "arbitrary_lookup_permission_created": non_claims.get("arbitrary_lookup_permission_created", False),
        "unsupported_commands_permitted": non_claims.get("unsupported_commands_permitted", False),
        "unsupported_lookup_keys_permitted": non_claims.get("unsupported_lookup_keys_permitted", False),
        "new_lookup_entry_created": non_claims.get("new_lookup_entry_created", False),
        "filesystem_discovery_performed": non_claims.get("filesystem_discovery_performed", False),
        "registry_created": non_claims.get("registry_created", False),
        "search_surface_created": non_claims.get("search_surface_created", False),
        "query_surface_created": non_claims.get("query_surface_created", False),
        "ranking_surface_created": non_claims.get("ranking_surface_created", False),
        "follow_on_work_authorized": non_claims.get("follow_on_work_authorized", False),
        "consumed_request_reopened": non_claims.get("consumed_request_reopened", False),
        "authorization_token_reused": non_claims.get("authorization_token_reused", False),
    }
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "boundary_id": boundary.get("boundary_id")
        or metadata.get("local_relevance_medium_read_only_operation_permission_boundary_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": metadata.get("result_version") or RESULT_VERSION,
        "resolver_module": metadata.get("resolver_module") or RESOLVER_MODULE,
        "boundary_recorded": statement.get(
            "local_relevance_medium_read_only_operation_permission_boundary_recorded",
            False,
        ),
        "basis_lookup_result_artifact_preserved": statement.get(
            "basis_lookup_result_artifact_preserved",
            False,
        ),
        "selected_command": boundary.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved", False),
        "selected_command_is_state": statement.get("selected_command_is_state", False),
        "selected_lookup_result_recorded": statement.get("selected_lookup_result_recorded", False),
        "lookup_result_created": statement.get("lookup_result_created", False),
        "lookup_result_local_only": statement.get("lookup_result_local_only", False),
        "lookup_result_read_only": statement.get("lookup_result_read_only", False),
        "future_operation_permission_may_be_considered": statement.get(
            "future_operation_permission_may_be_considered",
            False,
        ),
        "boundary_object_summary": {
            "boundary_type": boundary.get("boundary_type"),
            "boundary_scope": boundary.get("boundary_scope"),
            "basis_lookup_result_outcome": boundary.get("basis_lookup_result_outcome"),
            "basis_lookup_result_result_version": boundary.get("basis_lookup_result_result_version"),
            "basis_lookup_result_failed_check_count": boundary.get("basis_lookup_result_failed_check_count"),
        },
        "operation_permission_not_created": non_claims.get("operation_permission_created") is False,
        "operation_execution_not_created": non_claims.get("operation_execution_created") is False,
        "runtime_permission_not_created": non_claims.get("runtime_permission_created") is False,
        "public_api_not_created": non_claims.get("public_api_created") is False,
        "participant_facing_interface_not_created": non_claims.get("participant_facing_interface_created") is False,
        "distributed_network_behavior_not_created": non_claims.get("distributed_network_behavior_created") is False,
        "general_operation_permission_not_created": non_claims.get("general_operation_permission_created") is False,
        "general_lookup_permission_not_created": non_claims.get("general_lookup_permission_created") is False,
        "arbitrary_lookup_permission_not_created": non_claims.get("arbitrary_lookup_permission_created") is False,
        "unsupported_commands_not_permitted": non_claims.get("unsupported_commands_permitted") is False,
        "unsupported_lookup_keys_not_permitted": non_claims.get("unsupported_lookup_keys_permitted") is False,
        "no_new_lookup_entry_created_beyond_bounded_lookup_result_object": (
            non_claims.get("new_lookup_entry_created") is False
        ),
        "no_new_signal_entry_relevance_object_index_entry_created": (
            non_claims.get("new_signal_accepted") is False
            and non_claims.get("new_entry_accepted") is False
            and non_claims.get("new_relevance_object_created") is False
            and non_claims.get("new_index_entry_created") is False
        ),
        "filesystem_discovery_not_performed": non_claims.get("filesystem_discovery_performed") is False,
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
        "source_authority_currentness_truth_synchronization_participation_participant_role_not_created": (
            non_claims.get("source_transfer_occurred") is False
            and non_claims.get("source_receipt_occurred") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("truth_created") is False
            and non_claims.get("synchronization_created") is False
            and non_claims.get("participation_authorized") is False
            and non_claims.get("participant_role_created") is False
        ),
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed", False),
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked", False),
        "predecessor_failure_evidence_preserved": statement.get("predecessor_failure_evidence_preserved", False),
        "follow_on_not_created": non_claims.get("follow_on_work_authorized") is False,
        "key_non_claims": key_non_claims,
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def write_local_relevance_medium_read_only_operation_permission_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result artifact as deterministic UTF-8 JSON."""

    if not _is_mapping(result):
        raise LocalRelevanceMediumReadOnlyOperationPermissionBoundaryV0MinError(
            "result must be a mapping"
        )
    if output_path is None:
        metadata = result.get("local_relevance_medium_read_only_operation_permission_boundary_metadata", {})
        boundary = result.get("local_relevance_medium_read_only_operation_permission_boundary", {})
        boundary_id = DEFAULT_BOUNDARY_ID
        if _is_mapping(metadata):
            boundary_id = str(
                metadata.get("local_relevance_medium_read_only_operation_permission_boundary_id")
                or boundary_id
            )
        if _is_mapping(boundary):
            boundary_id = str(boundary.get("boundary_id") or boundary_id)
        candidate = OUTPUT_ROOT / (
            f"{boundary_id}__local_relevance_medium_read_only_operation_permission_boundary_v0_min_result.json"
        )
    else:
        candidate = Path(output_path)
    candidate.parent.mkdir(parents=True, exist_ok=True)
    final_path = candidate
    if final_path.exists():
        stem = candidate.stem
        suffix = candidate.suffix
        index = 1
        while True:
            next_path = candidate.with_name(f"{stem}_{index:03d}{suffix}")
            if not next_path.exists():
                final_path = next_path
                break
            index += 1
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path


def build_declared_local_relevance_medium_read_only_operation_permission_boundary_v0_min_request(
    *,
    local_relevance_medium_read_only_operation_permission_boundary_id: str = DEFAULT_BOUNDARY_ID,
    selected_lookup_result_artifact: Path | str = DEFAULT_LOOKUP_RESULT_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    local_relevance_medium_read_only_operation_permission_boundary_intent: str = INTENT_RECORD,
    local_relevance_medium_read_only_operation_permission_boundary_question: str = CORE_QUESTION,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared request for one selected-state operation permission boundary."""

    if selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyOperationPermissionBoundaryV0MinError(
            "selected command must be exactly state"
        )
    non_claims = _canonical_false_non_claims()
    if declared_non_claims is not None:
        for key, value in declared_non_claims.items():
            non_claims[str(key)] = value
    request: dict[str, Any] = {
        "local_relevance_medium_read_only_operation_permission_boundary_id": (
            local_relevance_medium_read_only_operation_permission_boundary_id
        ),
        "local_relevance_medium_read_only_operation_permission_boundary_question": (
            local_relevance_medium_read_only_operation_permission_boundary_question
        ),
        "local_relevance_medium_read_only_operation_permission_boundary_intent": (
            local_relevance_medium_read_only_operation_permission_boundary_intent
        ),
        "selected_lookup_result_artifact": str(Path(selected_lookup_result_artifact)),
        "selected_command": selected_command,
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "future_operation_permission_may_be_considered": True,
        "declared_non_claims": non_claims,
    }
    request.update(overrides)
    return request
