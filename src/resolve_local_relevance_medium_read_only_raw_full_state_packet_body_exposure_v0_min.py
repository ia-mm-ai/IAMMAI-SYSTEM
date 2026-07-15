"""Resolve one local read-only raw/full state packet body exposure.

This resolver reads one clean raw/full state packet body exposure boundary
artifact and one clean selected-state packet body exposure artifact. It records
one bounded LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE
object for selected command ``state`` only.

The object is raw/full-state-packet-body-exposure-shaped, local, read-only,
selected-state-only, non-operation-shaped, closure-token-aware, and
non-runtime-shaped. It records ``raw_full_state_packet_body_exposed`` only in
the narrow sense that one bounded local read-only raw/full packet-body exposure
event exists. It does not perform lookup, execute lookup commands, create
permissions, create public or distributed surfaces, discover files, accept
entries or signals, create registry/search/query/ranking surfaces, or
authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class LocalRelevanceMediumReadOnlyRawFullStatePacketBodyExposureV0MinError(
    RuntimeError
):
    """Bounded resolver error for raw/full state packet body exposure."""


RESULT_VERSION = "0.1.0"
BASIS_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RESULT_VERSION = "0.1.0"
BASIS_STATE_PACKET_BODY_EXPOSURE_RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min"
)

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BLOCKED"
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
    "raw_full_state_packet_body_exposure_v0_min"
)
DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "raw_full_state_packet_body_exposure_boundary_v0_min/"
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_"
    "reference_review_001__local_relevance_medium_read_only_raw_full_state_packet_"
    "body_exposure_boundary_v0_min_result.json"
)
DEFAULT_STATE_PACKET_BODY_EXPOSURE_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_packet_body_exposure_v0_min/"
    "local_relevance_medium_read_only_state_packet_body_exposure_"
    "reference_review_001__local_relevance_medium_read_only_state_packet_body_"
    "exposure_v0_min_result.json"
)

DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ID = (
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_001"
)
RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE"
)
RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE = (
    "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY"
)
SELECTED_COMMAND = "state"

RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED"
)
RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY"
)
RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_SCOPE = (
    "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY"
)
STATE_PACKET_BODY_EXPOSURE_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_RECORDED"
)
STATE_PACKET_BODY_EXPOSURE_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE"
)
STATE_PACKET_BODY_EXPOSURE_SCOPE = "SELECTED_STATE_PACKET_BODY_EXPOSURE_ONLY"

SUPPORTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE_VALUES = (
    RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE,
)
SUPPORTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE_VALUES = (
    RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE,
)

INTENT_RECORD = (
    "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE"
)
INTENT_BLOCK = (
    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_"
    "EXPOSURE_BOUNDARY for selected command state, and one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE be "
    "recorded for the selected-state packet body exposure, without performing "
    "lookup, executing lookup command, creating operation permission, creating "
    "runtime permission, creating public API, creating participant-facing "
    "interface, creating distributed network behavior, creating general lookup "
    "permission, creating arbitrary lookup permission, permitting unsupported "
    "commands, permitting unsupported lookup keys, creating new lookup result, "
    "creating new lookup entry, accepting new entries, accepting new signals, "
    "performing filesystem discovery, creating query surface, registry, search, "
    "ranking, scoring, priority, validity judgment, truth judgment, authority, "
    "currentness, synchronization, participation authorization, participant "
    "role, repeated reception permission, arbitrary reception, feed, source "
    "transfer, source receipt, or follow-on work?"
)

RAW_FULL_STATE_PACKET_BODY_EXPOSURE_OBJECT_FALSE_FIELDS = (
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
    "artifact_existence_treated_as_raw_full_state_packet_body_exposure_authority",
    "latest_file_posture_treated_as_raw_full_state_packet_body_exposure_authority",
    "repo_local_availability_treated_as_raw_full_state_packet_body_exposure_authority",
    "hidden_repo_state_used_as_raw_full_state_packet_body_exposure_content",
    "hidden_repo_state_used_as_raw_full_state_packet_body_exposure_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

REQUIRED_FALSE_NON_CLAIMS = (
    RAW_FULL_STATE_PACKET_BODY_EXPOSURE_OBJECT_FALSE_FIELDS
    + REQUEST_ONLY_FALSE_FIELDS
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded",
    "basis_raw_full_state_packet_body_exposure_boundary_artifact_preserved",
    "basis_state_packet_body_exposure_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_state_packet_body_exposure_recorded",
    "state_packet_body_exposed",
    "state_packet_body_exposure_local_only",
    "state_packet_body_exposure_read_only",
    "raw_full_state_packet_body_exposed",
    "raw_full_state_packet_body_exposure_local_only",
    "raw_full_state_packet_body_exposure_read_only",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

_BASE_BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BLOCK_REQUESTED",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_PATH_MISSING",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_UNREADABLE",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_PATH_MISSING",
    "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_UNREADABLE",
    "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_NOT_JSON_OBJECT",
    "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_NOT_RECORDED",
    "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_FAILED_CHECKS_PRESENT",
    "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED",
    "STATE_PACKET_BODY_NOT_EXPOSED",
    "STATE_PACKET_BODY_EXPOSURE_LOCAL_ONLY_NOT_TRUE",
    "STATE_PACKET_BODY_EXPOSURE_READ_ONLY_NOT_TRUE",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE_MISSING",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE_MISSING",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE_NOT_SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED",
    "RAW_FULL_STATE_PACKET_BODY_NOT_EXPOSED",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_LOCAL_ONLY_NOT_TRUE",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_READ_ONLY_NOT_TRUE",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_REQUEST_UNREADABLE",
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
        "lookup_command_executed": "lookup command not executed",
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
        "consumed_request_reopened": "consumed request not reopened",
        "authorization_token_reused": "authorization token not reused",
        "follow_on_work_authorized": "follow-on work not authorized",
        "artifact_existence_treated_as_raw_full_state_packet_body_exposure_authority": (
            "artifact existence not raw/full state packet body exposure authority"
        ),
        "latest_file_posture_treated_as_raw_full_state_packet_body_exposure_authority": (
            "latest file posture not raw/full state packet body exposure authority"
        ),
        "repo_local_availability_treated_as_raw_full_state_packet_body_exposure_authority": (
            "repo-local availability not raw/full state packet body exposure authority"
        ),
        "hidden_repo_state_used_as_raw_full_state_packet_body_exposure_content": (
            "hidden repo state not raw/full state packet body exposure content"
        ),
        "hidden_repo_state_used_as_raw_full_state_packet_body_exposure_authority": (
            "hidden repo state not raw/full state packet body exposure authority"
        ),
        "prior_artifacts_mutated": "prior artifacts not mutated",
        "predecessor_failure_repaired": "predecessor failure not repaired",
        "predecessor_failure_hidden": "predecessor failure not hidden",
        "predecessor_failure_claimed_passed": (
            "predecessor failure not claimed passed"
        ),
    }
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_full_state_packet_body_exposure_body",
    "raw_full_state_packet_body",
    "full_state_packet_body",
    "raw_full_state_packet_body_exposure_boundary_body",
    "raw_state_packet_body_exposure_body",
    "raw_state_packet_body",
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
    "state_packet_body_exposure_body",
    "state_packet_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
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
    RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE,
    RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE,
    RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED_OUTCOME,
    RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_TYPE,
    RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_SCOPE,
    STATE_PACKET_BODY_EXPOSURE_RECORDED_OUTCOME,
    STATE_PACKET_BODY_EXPOSURE_TYPE,
    STATE_PACKET_BODY_EXPOSURE_SCOPE,
    SELECTED_COMMAND,
    RESULT_VERSION,
    BASIS_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RESULT_VERSION,
    BASIS_STATE_PACKET_BODY_EXPOSURE_RESULT_VERSION,
    RESOLVER_MODULE,
    *OUTCOME_FAMILY,
    *SUPPORTED_INTENTS,
    *BLOCK_CODES,
    *REQUIRED_FALSE_NON_CLAIMS,
    *ALLOWED_TRUE_RECORDED_FIELDS,
}

WHAT_REMAINS_OPEN = (
    "local relevance medium read-only raw/full state packet body exposure test",
    "local relevance medium read-only raw/full state packet body exposure live artifact",
    "local relevance medium read-only raw/full state packet body exposure terminal summary, if needed",
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
    if isinstance(value, Mapping):
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
    value = artifact.get(key) if isinstance(artifact, Mapping) else None
    return dict(value) if isinstance(value, Mapping) else {}


def _count_failed_checks(artifact: Mapping[str, Any] | None, key: str) -> int | None:
    if not isinstance(artifact, Mapping):
        return None
    checks = artifact.get(key)
    if isinstance(checks, list):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    return None


def _artifact_failed_count(
    artifact: Mapping[str, Any] | None,
    summary: Mapping[str, Any],
    checks_key: str,
) -> Any:
    if not isinstance(artifact, Mapping):
        return None
    value = _first_present(summary.get("failed_check_count"), artifact.get("failed_check_count"))
    if value is not None:
        return value
    return _count_failed_checks(artifact, checks_key)


def _artifact_bool(*values: Any) -> bool | None:
    for value in values:
        if isinstance(value, bool):
            return value
    return None


def _raw_full_boundary(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary",
    )


def _raw_full_boundary_summary(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_summary",
    )


def _raw_full_boundary_metadata(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_metadata",
    )


def _raw_full_boundary_statement(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_statement",
    )


def _state_packet_body_exposure(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_state_packet_body_exposure",
    )


def _state_packet_body_exposure_summary(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_state_packet_body_exposure_summary",
    )


def _state_packet_body_exposure_metadata(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_state_packet_body_exposure_metadata",
    )


def _state_packet_body_exposure_statement(
    artifact: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_state_packet_body_exposure_statement",
    )


def _declared_non_claims(
    request: Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    if not isinstance(request, Mapping):
        return None
    value = request.get("declared_non_claims")
    return value if isinstance(value, Mapping) else None


def _false_field_actual(
    request: Mapping[str, Any],
    field: str,
    *basis_maps: Mapping[str, Any],
) -> Any:
    if field in request:
        return request[field]
    for basis in basis_maps:
        if isinstance(basis, Mapping) and basis.get(field) is True:
            return True
    return False


def _positive_field_actual(
    request: Mapping[str, Any],
    positive_key: str,
    negative_shortcut_key: str,
) -> Any:
    if request.get(negative_shortcut_key) is True:
        return False
    if positive_key in request:
        return request.get(positive_key)
    return True


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


def _build_raw_full_state_packet_body_exposure_object(
    *,
    exposure_id: str,
    recorded: bool,
    raw_full_boundary_artifact_path: Path | None,
    raw_full_boundary_outcome: Any,
    raw_full_boundary_version: Any,
    raw_full_boundary_failed_count: Any,
    state_packet_body_exposure_artifact_path: Path | None,
    state_packet_body_exposure_outcome: Any,
    state_packet_body_exposure_version: Any,
    state_packet_body_exposure_failed_count: Any,
    selected_command: Any,
    selected_state_packet_body_exposure_recorded: bool,
    state_packet_body_exposed: bool,
    state_packet_body_exposure_local_only: bool,
    state_packet_body_exposure_read_only: bool,
) -> dict[str, Any]:
    object_selected_command = (
        SELECTED_COMMAND if selected_command == SELECTED_COMMAND else None
    )
    exposure: dict[str, Any] = {
        "raw_full_state_packet_body_exposure_id": exposure_id,
        "raw_full_state_packet_body_exposure_type": (
            RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE
        ),
        "raw_full_state_packet_body_exposure_version": RESULT_VERSION,
        "raw_full_state_packet_body_exposure_scope": (
            RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE
        ),
        "basis_raw_full_state_packet_body_exposure_boundary_artifact": (
            str(raw_full_boundary_artifact_path)
            if raw_full_boundary_artifact_path
            else None
        ),
        "basis_raw_full_state_packet_body_exposure_boundary_outcome": (
            raw_full_boundary_outcome
        ),
        "basis_raw_full_state_packet_body_exposure_boundary_result_version": (
            raw_full_boundary_version
        ),
        "basis_raw_full_state_packet_body_exposure_boundary_failed_check_count": (
            raw_full_boundary_failed_count
        ),
        "basis_state_packet_body_exposure_artifact": (
            str(state_packet_body_exposure_artifact_path)
            if state_packet_body_exposure_artifact_path
            else None
        ),
        "basis_state_packet_body_exposure_outcome": state_packet_body_exposure_outcome,
        "basis_state_packet_body_exposure_result_version": (
            state_packet_body_exposure_version
        ),
        "basis_state_packet_body_exposure_failed_check_count": (
            state_packet_body_exposure_failed_count
        ),
        "selected_command": object_selected_command,
        "selected_command_is_state": object_selected_command == SELECTED_COMMAND,
        "selected_state_packet_body_exposure_recorded": (
            selected_state_packet_body_exposure_recorded and recorded
        ),
        "state_packet_body_exposed": state_packet_body_exposed and recorded,
        "state_packet_body_exposure_local_only": (
            state_packet_body_exposure_local_only and recorded
        ),
        "state_packet_body_exposure_read_only": (
            state_packet_body_exposure_read_only and recorded
        ),
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded": (
            recorded
        ),
        "raw_full_state_packet_body_exposed": recorded,
        "raw_full_state_packet_body_exposure_local_only": recorded,
        "raw_full_state_packet_body_exposure_read_only": recorded,
    }
    for key in RAW_FULL_STATE_PACKET_BODY_EXPOSURE_OBJECT_FALSE_FIELDS:
        exposure[key] = False
    return exposure


def _build_statement(
    exposure: Mapping[str, Any],
    recorded: bool,
) -> dict[str, bool]:
    return {
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded": (
            exposure.get(
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded"
            )
            is True
        ),
        "basis_raw_full_state_packet_body_exposure_boundary_artifact_preserved": (
            recorded
            and exposure.get(
                "basis_raw_full_state_packet_body_exposure_boundary_artifact"
            )
            is not None
        ),
        "basis_state_packet_body_exposure_artifact_preserved": (
            recorded
            and exposure.get("basis_state_packet_body_exposure_artifact") is not None
        ),
        "selected_command_preserved": exposure.get("selected_command")
        == SELECTED_COMMAND,
        "selected_command_is_state": exposure.get("selected_command_is_state") is True,
        "selected_state_packet_body_exposure_recorded": exposure.get(
            "selected_state_packet_body_exposure_recorded"
        )
        is True,
        "state_packet_body_exposed": exposure.get("state_packet_body_exposed")
        is True,
        "state_packet_body_exposure_local_only": exposure.get(
            "state_packet_body_exposure_local_only"
        )
        is True,
        "state_packet_body_exposure_read_only": exposure.get(
            "state_packet_body_exposure_read_only"
        )
        is True,
        "raw_full_state_packet_body_exposed": exposure.get(
            "raw_full_state_packet_body_exposed"
        )
        is True,
        "raw_full_state_packet_body_exposure_local_only": exposure.get(
            "raw_full_state_packet_body_exposure_local_only"
        )
        is True,
        "raw_full_state_packet_body_exposure_read_only": exposure.get(
            "raw_full_state_packet_body_exposure_read_only"
        )
        is True,
        "consumed_request_token_remains_closed": recorded,
        "authorization_token_reuse_blocked": recorded,
        "predecessor_failure_evidence_preserved": recorded,
        "result_level_non_claims_canonical_false": recorded,
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "raw_full_state_packet_body_exposure_only": True,
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


def _build_declared_question_section(request: Mapping[str, Any] | None) -> dict[str, Any]:
    if request is None:
        return {
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_id": None,
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_question": None,
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_intent": None,
            "selected_raw_full_state_packet_body_exposure_boundary_artifact": None,
            "selected_state_packet_body_exposure_artifact": None,
            "selected_command": None,
            "raw_full_state_packet_body_exposure_type": None,
            "raw_full_state_packet_body_exposure_scope": None,
        }
    return {
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_id": (
            request.get(
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_id"
            )
        ),
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_question": (
            request.get(
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_question"
            )
        ),
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_intent": (
            request.get(
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_intent"
            )
        ),
        "selected_raw_full_state_packet_body_exposure_boundary_artifact": (
            str(request.get("selected_raw_full_state_packet_body_exposure_boundary_artifact"))
            if request.get("selected_raw_full_state_packet_body_exposure_boundary_artifact")
            is not None
            else None
        ),
        "selected_state_packet_body_exposure_artifact": (
            str(request.get("selected_state_packet_body_exposure_artifact"))
            if request.get("selected_state_packet_body_exposure_artifact") is not None
            else None
        ),
        "selected_command": request.get("selected_command"),
        "raw_full_state_packet_body_exposure_type": request.get(
            "raw_full_state_packet_body_exposure_type"
        ),
        "raw_full_state_packet_body_exposure_scope": request.get(
            "raw_full_state_packet_body_exposure_scope"
        ),
    }


def _build_raw_full_boundary_basis(
    artifact: Mapping[str, Any] | None,
    path: Path | None,
) -> dict[str, Any]:
    boundary = _raw_full_boundary(artifact)
    summary = _raw_full_boundary_summary(artifact)
    metadata = _raw_full_boundary_metadata(artifact)
    if not isinstance(artifact, Mapping):
        return {
            "selected_raw_full_state_packet_body_exposure_boundary_artifact": (
                str(path) if path else None
            ),
            "basis_artifact_read": False,
            "raw_full_state_packet_body_exposure_boundary_artifact_body_returned": False,
        }
    return {
        "selected_raw_full_state_packet_body_exposure_boundary_artifact": (
            str(path) if path else None
        ),
        "basis_artifact_read": True,
        "basis_raw_full_state_packet_body_exposure_boundary_artifact_preserved": True,
        "basis_raw_full_state_packet_body_exposure_boundary_outcome": _first_present(
            artifact.get("outcome"),
            summary.get("outcome"),
        ),
        "basis_raw_full_state_packet_body_exposure_boundary_result_version": (
            _first_present(
                summary.get("result_version"),
                artifact.get("result_version"),
                metadata.get(
                    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_version"
                ),
                metadata.get("result_version"),
                boundary.get("boundary_version"),
            )
        ),
        "basis_raw_full_state_packet_body_exposure_boundary_failed_check_count": (
            _artifact_failed_count(
                artifact,
                summary,
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_checks",
            )
        ),
        "selected_command": boundary.get("selected_command"),
        "selected_command_is_state": boundary.get("selected_command_is_state"),
        "future_raw_full_state_packet_body_exposure_may_be_considered": (
            boundary.get("future_raw_full_state_packet_body_exposure_may_be_considered")
        ),
        "raw_full_state_packet_body_exposure_boundary_artifact_body_returned": False,
    }


def _build_state_packet_body_exposure_basis(
    artifact: Mapping[str, Any] | None,
    path: Path | None,
) -> dict[str, Any]:
    packet_exposure = _state_packet_body_exposure(artifact)
    summary = _state_packet_body_exposure_summary(artifact)
    metadata = _state_packet_body_exposure_metadata(artifact)
    if not isinstance(artifact, Mapping):
        return {
            "selected_state_packet_body_exposure_artifact": (
                str(path) if path else None
            ),
            "basis_artifact_read": False,
            "raw_full_state_packet_body_exposure_artifact_body_returned": False,
        }
    return {
        "selected_state_packet_body_exposure_artifact": str(path) if path else None,
        "basis_artifact_read": True,
        "basis_state_packet_body_exposure_artifact_preserved": True,
        "basis_state_packet_body_exposure_outcome": _first_present(
            artifact.get("outcome"),
            summary.get("outcome"),
        ),
        "basis_state_packet_body_exposure_result_version": _first_present(
            summary.get("result_version"),
            artifact.get("result_version"),
            metadata.get(
                "local_relevance_medium_read_only_state_packet_body_exposure_version"
            ),
            metadata.get("result_version"),
            packet_exposure.get("state_packet_body_exposure_version"),
        ),
        "basis_state_packet_body_exposure_failed_check_count": _artifact_failed_count(
            artifact,
            summary,
            "local_relevance_medium_read_only_state_packet_body_exposure_checks",
        ),
        "selected_command": packet_exposure.get("selected_command"),
        "selected_command_is_state": packet_exposure.get("selected_command_is_state"),
        "selected_state_packet_body_exposure_recorded": _first_present(
            packet_exposure.get(
                "local_relevance_medium_read_only_state_packet_body_exposure_recorded"
            ),
            packet_exposure.get("selected_state_packet_body_exposure_recorded"),
            summary.get("state_packet_body_exposure_recorded"),
        ),
        "state_packet_body_exposed": packet_exposure.get("state_packet_body_exposed"),
        "state_packet_body_exposure_local_only": packet_exposure.get(
            "state_packet_body_exposure_local_only"
        ),
        "state_packet_body_exposure_read_only": packet_exposure.get(
            "state_packet_body_exposure_read_only"
        ),
        "raw_full_state_packet_body_exposure_artifact_body_returned": False,
    }


def build_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact summary for a raw/full state packet body exposure."""

    checks = result.get(
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_checks"
    )
    checks_list = checks if isinstance(checks, list) else []
    exposure = result.get(
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure"
    )
    exposure_map = exposure if isinstance(exposure, Mapping) else {}
    statement = result.get(
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_statement"
    )
    statement_map = statement if isinstance(statement, Mapping) else {}
    metadata = result.get(
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_metadata"
    )
    metadata_map = metadata if isinstance(metadata, Mapping) else {}
    declared = result.get(
        "declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_question"
    )
    declared_map = declared if isinstance(declared, Mapping) else {}
    block = result.get("block")
    block_map = block if isinstance(block, Mapping) else {}
    non_claims = result.get("non_claims")
    non_claims_map = non_claims if isinstance(non_claims, Mapping) else {}

    def non_claim_false(key: str) -> bool:
        return non_claims_map.get(key) is False

    return {
        "outcome": result.get("outcome"),
        "block_code": block_map.get("block_code") or block_map.get("code"),
        "block_reason": block_map.get("reason"),
        "raw_full_state_packet_body_exposure_id": exposure_map.get(
            "raw_full_state_packet_body_exposure_id"
        )
        or metadata_map.get(
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_id"
        ),
        "question": declared_map.get(
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_question"
        ),
        "intent": declared_map.get(
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_intent"
        ),
        "passed_check_count": _passed_check_count(checks_list),
        "failed_check_count": _failed_check_count(checks_list),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "raw_full_state_packet_body_exposure_recorded": statement_map.get(
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded"
        )
        is True,
        "basis_raw_full_state_packet_body_exposure_boundary_artifact_preserved": (
            statement_map.get(
                "basis_raw_full_state_packet_body_exposure_boundary_artifact_preserved"
            )
            is True
        ),
        "basis_state_packet_body_exposure_artifact_preserved": statement_map.get(
            "basis_state_packet_body_exposure_artifact_preserved"
        )
        is True,
        "selected_command": exposure_map.get("selected_command")
        or declared_map.get("selected_command"),
        "selected_command_preserved": statement_map.get("selected_command_preserved")
        is True,
        "selected_command_is_state": statement_map.get("selected_command_is_state")
        is True,
        "selected_state_packet_body_exposure_recorded": statement_map.get(
            "selected_state_packet_body_exposure_recorded"
        )
        is True,
        "state_packet_body_exposed": statement_map.get("state_packet_body_exposed")
        is True,
        "state_packet_body_exposure_local_only": statement_map.get(
            "state_packet_body_exposure_local_only"
        )
        is True,
        "state_packet_body_exposure_read_only": statement_map.get(
            "state_packet_body_exposure_read_only"
        )
        is True,
        "raw_full_state_packet_body_exposed": statement_map.get(
            "raw_full_state_packet_body_exposed"
        )
        is True,
        "raw_full_state_packet_body_exposure_local_only": statement_map.get(
            "raw_full_state_packet_body_exposure_local_only"
        )
        is True,
        "raw_full_state_packet_body_exposure_read_only": statement_map.get(
            "raw_full_state_packet_body_exposure_read_only"
        )
        is True,
        "raw_full_state_packet_body_exposure_object_summary": {
            "raw_full_state_packet_body_exposure_type": exposure_map.get(
                "raw_full_state_packet_body_exposure_type"
            ),
            "raw_full_state_packet_body_exposure_scope": exposure_map.get(
                "raw_full_state_packet_body_exposure_scope"
            ),
            "raw_full_state_packet_body_exposure_version": exposure_map.get(
                "raw_full_state_packet_body_exposure_version"
            ),
            "basis_raw_full_state_packet_body_exposure_boundary_outcome": (
                exposure_map.get(
                    "basis_raw_full_state_packet_body_exposure_boundary_outcome"
                )
            ),
            "basis_state_packet_body_exposure_outcome": exposure_map.get(
                "basis_state_packet_body_exposure_outcome"
            ),
        },
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
        "no_new_lookup_result_or_entry_created": (
            non_claim_false("new_lookup_result_created")
            and non_claim_false("new_lookup_entry_created")
        ),
        "no_new_signal_entry_relevance_object_or_index_entry_created": (
            non_claim_false("new_signal_accepted")
            and non_claim_false("new_entry_accepted")
            and non_claim_false("new_relevance_object_created")
            and non_claim_false("new_index_entry_created")
        ),
        "filesystem_discovery_not_performed": non_claim_false(
            "filesystem_discovery_performed"
        ),
        "registry_search_query_surface_ranking_not_created": (
            non_claim_false("registry_created")
            and non_claim_false("search_surface_created")
            and non_claim_false("query_surface_created")
            and non_claim_false("ranking_surface_created")
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": (
            non_claim_false("scoring_surface_created")
            and non_claim_false("priority_surface_created")
            and non_claim_false("validity_judgment_created")
            and non_claim_false("truth_judgment_created")
            and non_claim_false("authority_judgment_created")
            and non_claim_false("currentness_judgment_created")
        ),
        "repeated_reception_arbitrary_reception_feed_not_created": (
            non_claim_false("repeated_reception_permission_created")
            and non_claim_false("arbitrary_reception_created")
            and non_claim_false("feed_created")
        ),
        "source_authority_currentness_truth_synchronization_participation_participant_role_not_created": (
            non_claim_false("source_created")
            and non_claim_false("authority_created")
            and non_claim_false("currentness_created")
            and non_claim_false("truth_created")
            and non_claim_false("synchronization_created")
            and non_claim_false("participation_authorized")
            and non_claim_false("participant_role_created")
        ),
        "consumed_request_token_remains_closed": non_claim_false(
            "consumed_request_reopened"
        ),
        "authorization_token_reuse_blocked": non_claim_false(
            "authorization_token_reused"
        ),
        "predecessor_failure_evidence_preserved": (
            non_claim_false("predecessor_failure_repaired")
            and non_claim_false("predecessor_failure_hidden")
            and non_claim_false("predecessor_failure_claimed_passed")
        ),
        "follow_on_not_created": non_claim_false("follow_on_work_authorized"),
        "key_non_claims": {
            key: non_claims_map.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        },
        "result_level_non_claims_canonical_false": all(
            non_claims_map.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _assemble_result(
    *,
    request: Mapping[str, Any] | None,
    outcome: str,
    checks: list[dict[str, Any]],
    exposure: Mapping[str, Any],
    raw_full_boundary_artifact: Mapping[str, Any] | None,
    raw_full_boundary_path: Path | None,
    state_packet_body_exposure_artifact: Mapping[str, Any] | None,
    state_packet_body_exposure_path: Path | None,
    additional_basis_required: list[str] | None = None,
    not_recorded_basis: list[str] | None = None,
) -> dict[str, Any]:
    exposure_id = str(
        exposure.get("raw_full_state_packet_body_exposure_id")
        or DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ID
    )
    recorded = outcome == OUTCOME_RECORDED
    block_code = _first_failure_code(checks) if outcome == OUTCOME_BLOCKED else None
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_metadata": {
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_id": (
                exposure_id
            ),
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_type": (
                RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE
            ),
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_version": (
                RESULT_VERSION
            ),
            "generated_at": _now(),
            "resolver_module": RESOLVER_MODULE,
            "predecessor_boundary_resolver_module": (
                "resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_v0_min"
            ),
            "predecessor_packet_body_exposure_resolver_module": (
                "resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min"
            ),
            "predecessor_failure_preserved_as_lineage_evidence": True,
        },
        "declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_question": (
            _build_declared_question_section(request)
        ),
        "selected_raw_full_state_packet_body_exposure_boundary_artifact_basis": (
            _build_raw_full_boundary_basis(
                raw_full_boundary_artifact,
                raw_full_boundary_path,
            )
        ),
        "selected_state_packet_body_exposure_artifact_basis": (
            _build_state_packet_body_exposure_basis(
                state_packet_body_exposure_artifact,
                state_packet_body_exposure_path,
            )
        ),
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure": dict(
            exposure
        ),
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_checks": checks,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_statement": (
            _build_statement(exposure, recorded)
        ),
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": additional_basis_required or [],
        "not_recorded_basis": not_recorded_basis or [],
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": _block_record(block_code),
    }
    result[
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_summary"
    ] = build_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_summary(
        result
    )
    return _sanitize(result)


def _empty_exposure(recorded: bool = False) -> dict[str, Any]:
    return _build_raw_full_state_packet_body_exposure_object(
        exposure_id=DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ID,
        recorded=recorded,
        raw_full_boundary_artifact_path=None,
        raw_full_boundary_outcome=None,
        raw_full_boundary_version=None,
        raw_full_boundary_failed_count=None,
        state_packet_body_exposure_artifact_path=None,
        state_packet_body_exposure_outcome=None,
        state_packet_body_exposure_version=None,
        state_packet_body_exposure_failed_count=None,
        selected_command=None,
        selected_state_packet_body_exposure_recorded=False,
        state_packet_body_exposed=False,
        state_packet_body_exposure_local_only=False,
        state_packet_body_exposure_read_only=False,
    )


def _malformed_result(code: str, reason: str) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _check(
        checks,
        "declared local relevance medium read only raw full state packet body exposure request is mapping",
        False,
        "mapping request",
        reason,
        code,
    )
    return _assemble_result(
        request=None,
        outcome=OUTCOME_BLOCKED,
        checks=checks,
        exposure=_empty_exposure(),
        raw_full_boundary_artifact=None,
        raw_full_boundary_path=None,
        state_packet_body_exposure_artifact=None,
        state_packet_body_exposure_path=None,
    )


def resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min(
    declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure: Mapping[
        str, Any
    ]
    | None = None,
) -> dict:
    """Resolve one raw/full state packet body exposure request."""

    if declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure is None:
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_REQUEST_MALFORMED",
            "request missing",
        )
    if not isinstance(
        declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure,
        Mapping,
    ):
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_REQUEST_MALFORMED",
            "request is not a mapping",
        )

    request = copy.deepcopy(
        dict(declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure)
    )
    non_claims = _declared_non_claims(request)
    checks: list[dict[str, Any]] = []

    exposure_id = str(
        request.get("local_relevance_medium_read_only_raw_full_state_packet_body_exposure_id")
        or DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ID
    )
    question = request.get(
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_question"
    )
    intent = request.get(
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_intent"
    )

    _check(
        checks,
        "raw full state packet body exposure question declared",
        isinstance(question, str) and bool(question.strip()),
        "declared raw/full state packet body exposure question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "raw full state packet body exposure intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "raw full state packet body exposure block intent not requested",
        intent != INTENT_BLOCK,
        f"not {INTENT_BLOCK}",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BLOCK_REQUESTED",
    )

    raw_full_boundary_path = _as_path(
        request.get("selected_raw_full_state_packet_body_exposure_boundary_artifact")
    )
    raw_full_boundary_missing_requested = (
        request.get("raw_full_state_packet_body_exposure_boundary_artifact_missing")
        is True
    )
    _check(
        checks,
        "raw full state packet body exposure boundary artifact path declared",
        raw_full_boundary_path is not None and not raw_full_boundary_missing_requested,
        "declared raw/full state packet body exposure boundary artifact path",
        str(raw_full_boundary_path) if raw_full_boundary_path else None,
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_PATH_MISSING",
    )

    raw_full_boundary_artifact: dict[str, Any] | None = None
    raw_full_boundary_read_code: str | None = (
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_UNREADABLE"
    )
    if raw_full_boundary_path is not None and not raw_full_boundary_missing_requested:
        raw_full_boundary_artifact, raw_full_boundary_read_code = _read_json_object(
            raw_full_boundary_path,
            "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_UNREADABLE",
            "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
        )
    _check(
        checks,
        "raw full state packet body exposure boundary artifact readable JSON",
        raw_full_boundary_read_code is None,
        "readable JSON object",
        raw_full_boundary_read_code or "readable JSON object",
        raw_full_boundary_read_code,
    )

    state_packet_body_exposure_path = _as_path(
        request.get("selected_state_packet_body_exposure_artifact")
    )
    state_packet_body_exposure_missing_requested = (
        request.get("state_packet_body_exposure_artifact_missing") is True
    )
    _check(
        checks,
        "state packet body exposure artifact path declared",
        state_packet_body_exposure_path is not None
        and not state_packet_body_exposure_missing_requested,
        "declared selected-state packet body exposure artifact path",
        str(state_packet_body_exposure_path) if state_packet_body_exposure_path else None,
        "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_PATH_MISSING",
    )

    state_packet_body_exposure_artifact: dict[str, Any] | None = None
    state_packet_body_exposure_read_code: str | None = (
        "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_UNREADABLE"
    )
    if (
        state_packet_body_exposure_path is not None
        and not state_packet_body_exposure_missing_requested
    ):
        (
            state_packet_body_exposure_artifact,
            state_packet_body_exposure_read_code,
        ) = _read_json_object(
            state_packet_body_exposure_path,
            "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_UNREADABLE",
            "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_NOT_JSON_OBJECT",
        )
    _check(
        checks,
        "state packet body exposure artifact readable JSON",
        state_packet_body_exposure_read_code is None,
        "readable JSON object",
        state_packet_body_exposure_read_code or "readable JSON object",
        state_packet_body_exposure_read_code,
    )

    boundary = _raw_full_boundary(raw_full_boundary_artifact)
    boundary_summary = _raw_full_boundary_summary(raw_full_boundary_artifact)
    boundary_metadata = _raw_full_boundary_metadata(raw_full_boundary_artifact)
    boundary_statement = _raw_full_boundary_statement(raw_full_boundary_artifact)

    boundary_outcome = _first_present(
        raw_full_boundary_artifact.get("outcome") if raw_full_boundary_artifact else None,
        boundary_summary.get("outcome"),
    )
    boundary_version = _first_present(
        boundary_summary.get("result_version"),
        raw_full_boundary_artifact.get("result_version")
        if raw_full_boundary_artifact
        else None,
        boundary_metadata.get(
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_version"
        ),
        boundary_metadata.get("result_version"),
        boundary.get("boundary_version"),
    )
    boundary_failed_count = _artifact_failed_count(
        raw_full_boundary_artifact,
        boundary_summary,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_checks",
    )

    _check(
        checks,
        "raw full state packet body exposure boundary artifact outcome recorded",
        boundary_outcome == RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED_OUTCOME
        and request.get("raw_full_state_packet_body_exposure_boundary_artifact_not_recorded")
        is not True,
        RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED_OUTCOME,
        boundary_outcome,
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "raw full state packet body exposure boundary artifact result version 0.1.0",
        boundary_version
        == BASIS_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RESULT_VERSION
        and request.get(
            "raw_full_state_packet_body_exposure_boundary_artifact_version_not_0_1_0"
        )
        is not True,
        BASIS_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RESULT_VERSION,
        boundary_version,
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "raw full state packet body exposure boundary artifact failed check count zero",
        boundary_failed_count == 0
        and request.get(
            "raw_full_state_packet_body_exposure_boundary_artifact_failed_checks_present"
        )
        is not True,
        0,
        boundary_failed_count,
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    packet_exposure = _state_packet_body_exposure(state_packet_body_exposure_artifact)
    packet_summary = _state_packet_body_exposure_summary(
        state_packet_body_exposure_artifact
    )
    packet_metadata = _state_packet_body_exposure_metadata(
        state_packet_body_exposure_artifact
    )
    packet_statement = _state_packet_body_exposure_statement(
        state_packet_body_exposure_artifact
    )

    packet_outcome = _first_present(
        state_packet_body_exposure_artifact.get("outcome")
        if state_packet_body_exposure_artifact
        else None,
        packet_summary.get("outcome"),
    )
    packet_version = _first_present(
        packet_summary.get("result_version"),
        state_packet_body_exposure_artifact.get("result_version")
        if state_packet_body_exposure_artifact
        else None,
        packet_metadata.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_version"
        ),
        packet_metadata.get("result_version"),
        packet_exposure.get("state_packet_body_exposure_version"),
    )
    packet_failed_count = _artifact_failed_count(
        state_packet_body_exposure_artifact,
        packet_summary,
        "local_relevance_medium_read_only_state_packet_body_exposure_checks",
    )

    _check(
        checks,
        "state packet body exposure artifact outcome recorded",
        packet_outcome == STATE_PACKET_BODY_EXPOSURE_RECORDED_OUTCOME
        and request.get("state_packet_body_exposure_artifact_not_recorded") is not True,
        STATE_PACKET_BODY_EXPOSURE_RECORDED_OUTCOME,
        packet_outcome,
        "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "state packet body exposure artifact result version 0.1.0",
        packet_version == BASIS_STATE_PACKET_BODY_EXPOSURE_RESULT_VERSION
        and request.get("state_packet_body_exposure_artifact_version_not_0_1_0")
        is not True,
        BASIS_STATE_PACKET_BODY_EXPOSURE_RESULT_VERSION,
        packet_version,
        "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "state packet body exposure artifact failed check count zero",
        packet_failed_count == 0
        and request.get("state_packet_body_exposure_artifact_failed_checks_present")
        is not True,
        0,
        packet_failed_count,
        "STATE_PACKET_BODY_EXPOSURE_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    selected_command = request.get("selected_command")
    boundary_command_is_state = boundary.get("selected_command") in (None, SELECTED_COMMAND)
    packet_command_is_state = packet_exposure.get("selected_command") in (
        None,
        SELECTED_COMMAND,
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
        and boundary_command_is_state
        and packet_command_is_state
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
        and packet_exposure.get("selected_command_is_state") is not False,
        True,
        selected_command == SELECTED_COMMAND,
        "SELECTED_COMMAND_NOT_STATE",
    )

    selected_state_packet_body_exposure_recorded = _artifact_bool(
        packet_exposure.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_recorded"
        ),
        packet_exposure.get("selected_state_packet_body_exposure_recorded"),
        packet_statement.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_recorded"
        ),
        packet_summary.get("state_packet_body_exposure_recorded"),
    )
    state_packet_body_exposed = _artifact_bool(
        packet_exposure.get("state_packet_body_exposed"),
        packet_statement.get("state_packet_body_exposed"),
        packet_summary.get("state_packet_body_exposed"),
    )
    state_packet_body_exposure_local_only = _artifact_bool(
        packet_exposure.get("state_packet_body_exposure_local_only"),
        packet_statement.get("state_packet_body_exposure_local_only"),
        packet_summary.get("state_packet_body_exposure_local_only"),
    )
    state_packet_body_exposure_read_only = _artifact_bool(
        packet_exposure.get("state_packet_body_exposure_read_only"),
        packet_statement.get("state_packet_body_exposure_read_only"),
        packet_summary.get("state_packet_body_exposure_read_only"),
    )

    _check(
        checks,
        "selected-state packet body exposure recorded",
        selected_state_packet_body_exposure_recorded is True
        and request.get("selected_state_packet_body_exposure_not_recorded") is not True,
        True,
        selected_state_packet_body_exposure_recorded,
        "SELECTED_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED",
    )
    _check(
        checks,
        "state packet body exposed",
        state_packet_body_exposed is True
        and request.get("state_packet_body_not_exposed") is not True,
        True,
        state_packet_body_exposed,
        "STATE_PACKET_BODY_NOT_EXPOSED",
    )
    _check(
        checks,
        "state packet body exposure local only",
        state_packet_body_exposure_local_only is True
        and request.get("state_packet_body_exposure_local_only_not_true") is not True,
        True,
        state_packet_body_exposure_local_only,
        "STATE_PACKET_BODY_EXPOSURE_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "state packet body exposure read only",
        state_packet_body_exposure_read_only is True
        and request.get("state_packet_body_exposure_read_only_not_true") is not True,
        True,
        state_packet_body_exposure_read_only,
        "STATE_PACKET_BODY_EXPOSURE_READ_ONLY_NOT_TRUE",
    )

    exposure_type = request.get("raw_full_state_packet_body_exposure_type")
    exposure_scope = request.get("raw_full_state_packet_body_exposure_scope")
    _check(
        checks,
        "raw full state packet body exposure type exact",
        exposure_type == RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE
        and request.get(
            "raw_full_state_packet_body_exposure_type_not_local_relevance_medium_read_only_raw_full_state_packet_body_exposure"
        )
        is not True,
        RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE,
        exposure_type,
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE_MISSING"
        if exposure_type is None
        else "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE",
    )
    _check(
        checks,
        "raw full state packet body exposure scope exact",
        exposure_scope == RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE
        and request.get(
            "raw_full_state_packet_body_exposure_scope_not_selected_raw_full_state_packet_body_exposure_only"
        )
        is not True,
        RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE,
        exposure_scope,
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE_MISSING"
        if exposure_scope is None
        else "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE_NOT_SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY",
    )

    exposure_recorded = _positive_field_actual(
        request,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded",
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_not_recorded",
    )
    raw_full_exposed = _positive_field_actual(
        request,
        "raw_full_state_packet_body_exposed",
        "raw_full_state_packet_body_not_exposed",
    )
    raw_full_local_only = _positive_field_actual(
        request,
        "raw_full_state_packet_body_exposure_local_only",
        "raw_full_state_packet_body_exposure_local_only_not_true",
    )
    raw_full_read_only = _positive_field_actual(
        request,
        "raw_full_state_packet_body_exposure_read_only",
        "raw_full_state_packet_body_exposure_read_only_not_true",
    )
    _check(
        checks,
        "local relevance medium read-only raw full state packet body exposure recorded",
        exposure_recorded is True,
        True,
        exposure_recorded,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED",
    )
    _check(
        checks,
        "raw full state packet body exposed",
        raw_full_exposed is True,
        True,
        raw_full_exposed,
        "RAW_FULL_STATE_PACKET_BODY_NOT_EXPOSED",
    )
    _check(
        checks,
        "raw full state packet body exposure local only",
        raw_full_local_only is True,
        True,
        raw_full_local_only,
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "raw full state packet body exposure read only",
        raw_full_read_only is True,
        True,
        raw_full_read_only,
        "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_READ_ONLY_NOT_TRUE",
    )

    for field in REQUIRED_FALSE_NON_CLAIMS:
        actual = _false_field_actual(request, field, boundary, packet_exposure)
        code = FALSE_FIELD_BLOCK_CODES.get(field, "NON_CLAIM_MISSING_OR_FLIPPED")
        _check(
            checks,
            FALSE_CHECK_NAMES.get(field, field.replace("_", " ") + " false"),
            actual is False,
            False,
            actual,
            code,
        )

    predecessor_failure_evidence_preserved = all(
        _false_field_actual(request, field, boundary, packet_exposure) is False
        for field in (
            "prior_artifacts_mutated",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
    )
    _check(
        checks,
        "predecessor failure evidence preserved",
        predecessor_failure_evidence_preserved,
        True,
        predecessor_failure_evidence_preserved,
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

    failed = _failed_check_count(checks) > 0
    additional_basis = request.get("additional_basis_context", [])
    if not isinstance(additional_basis, list):
        additional_basis = [str(_sanitize(additional_basis))]
    not_recorded_basis = request.get("not_recorded_basis", [])
    if not isinstance(not_recorded_basis, list):
        not_recorded_basis = [str(_sanitize(not_recorded_basis))]

    if failed:
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
        not_recorded_basis = not_recorded_basis or [
            "declared request chose not to record raw/full state packet body exposure"
        ]
    elif (
        request.get(
            "requested_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_outcome"
        )
        == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        or additional_basis
    ):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        additional_basis = additional_basis or [
            "additional raw/full state packet body exposure basis requested by declaration"
        ]
    else:
        outcome = OUTCOME_RECORDED

    recorded = outcome == OUTCOME_RECORDED
    exposure = _build_raw_full_state_packet_body_exposure_object(
        exposure_id=exposure_id,
        recorded=recorded,
        raw_full_boundary_artifact_path=raw_full_boundary_path,
        raw_full_boundary_outcome=boundary_outcome,
        raw_full_boundary_version=boundary_version,
        raw_full_boundary_failed_count=boundary_failed_count,
        state_packet_body_exposure_artifact_path=state_packet_body_exposure_path,
        state_packet_body_exposure_outcome=packet_outcome,
        state_packet_body_exposure_version=packet_version,
        state_packet_body_exposure_failed_count=packet_failed_count,
        selected_command=selected_command,
        selected_state_packet_body_exposure_recorded=(
            selected_state_packet_body_exposure_recorded is True
        ),
        state_packet_body_exposed=state_packet_body_exposed is True,
        state_packet_body_exposure_local_only=(
            state_packet_body_exposure_local_only is True
        ),
        state_packet_body_exposure_read_only=(
            state_packet_body_exposure_read_only is True
        ),
    )

    return _assemble_result(
        request=request,
        outcome=outcome,
        checks=checks,
        exposure=exposure,
        raw_full_boundary_artifact=raw_full_boundary_artifact,
        raw_full_boundary_path=raw_full_boundary_path,
        state_packet_body_exposure_artifact=state_packet_body_exposure_artifact,
        state_packet_body_exposure_path=state_packet_body_exposure_path,
        additional_basis_required=additional_basis,
        not_recorded_basis=not_recorded_basis,
    )


def resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_from_path(
    declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_path: Path
    | str,
) -> dict:
    """Read a declared request JSON object from a path and resolve it."""

    try:
        path = Path(
            declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_path
        )
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_REQUEST_UNREADABLE",
            f"request unreadable: {exc}",
        )
    if not isinstance(value, dict):
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_REQUEST_MALFORMED",
            "request JSON is not an object",
        )
    return resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min(
        value
    )


def write_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result artifact without silently overwriting files."""

    if not isinstance(result, Mapping):
        raise LocalRelevanceMediumReadOnlyRawFullStatePacketBodyExposureV0MinError(
            "result must be a mapping"
        )
    metadata = result.get(
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_metadata",
        {},
    )
    exposure = result.get(
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure",
        {},
    )
    exposure_id = None
    if isinstance(metadata, Mapping):
        exposure_id = metadata.get(
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_id"
        )
    if not exposure_id and isinstance(exposure, Mapping):
        exposure_id = exposure.get("raw_full_state_packet_body_exposure_id")
    exposure_id = str(exposure_id or DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ID)
    filename = (
        f"{exposure_id}__"
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_result.json"
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
            next_candidate = parent / f"{stem}_{index:03d}{suffix}"
            if not next_candidate.exists():
                candidate = next_candidate
                break
            index += 1

    candidate.write_text(
        json.dumps(_sanitize(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return candidate


def build_declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_request(
    *,
    local_relevance_medium_read_only_raw_full_state_packet_body_exposure_id: str = (
        DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ID
    ),
    selected_raw_full_state_packet_body_exposure_boundary_artifact: Path | str = (
        DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT
    ),
    selected_state_packet_body_exposure_artifact: Path | str = (
        DEFAULT_STATE_PACKET_BODY_EXPOSURE_ARTIFACT
    ),
    selected_command: str = SELECTED_COMMAND,
    raw_full_state_packet_body_exposure_type: str = (
        RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE
    ),
    raw_full_state_packet_body_exposure_scope: str = (
        RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE
    ),
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a declared request for one raw/full state packet body exposure."""

    if selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyRawFullStatePacketBodyExposureV0MinError(
            "selected_command must be exactly state"
        )
    non_claims = (
        _canonical_false_non_claims()
        if declared_non_claims is None
        else {key: declared_non_claims.get(key, False) for key in REQUIRED_FALSE_NON_CLAIMS}
    )
    return {
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_id": (
            local_relevance_medium_read_only_raw_full_state_packet_body_exposure_id
        ),
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_question": (
            CORE_QUESTION
        ),
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_intent": (
            intent
        ),
        "selected_raw_full_state_packet_body_exposure_boundary_artifact": str(
            selected_raw_full_state_packet_body_exposure_boundary_artifact
        ),
        "selected_state_packet_body_exposure_artifact": str(
            selected_state_packet_body_exposure_artifact
        ),
        "selected_command": SELECTED_COMMAND,
        "raw_full_state_packet_body_exposure_type": (
            raw_full_state_packet_body_exposure_type
        ),
        "raw_full_state_packet_body_exposure_scope": (
            raw_full_state_packet_body_exposure_scope
        ),
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded": True,
        "raw_full_state_packet_body_exposed": True,
        "raw_full_state_packet_body_exposure_local_only": True,
        "raw_full_state_packet_body_exposure_read_only": True,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
        "declared_non_claims": non_claims,
    }
