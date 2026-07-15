"""Resolve one v2 local relevance medium read-only derivative participant role admission.

This v2 resolver records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION object
only. It reads one clean selected continuation artifact as role-admission basis
and references the selected continuation terminal summary as declared basis.

It preserves the v1 role-admission membrane as predecessor evidence and fixes
the sanitizer/canonicalization defect that could redact official boolean false
posture fields whose keys mention hidden repo state. Official boolean posture
fields and required false non-claims remain booleans wherever emitted.

The role admission is local, read-only, selected-state-only, basis-reference-
only, downstream of continuation, closure-token-aware, and preserved-ancestor-
authority-import-blocking. It creates no participation motion, participant
output authorization, action authorization, participant re-entry, derivative
reception, vessel relation, runtime hosting, runtime loop, daemon behavior,
public API, participant-facing interface, distributed network behavior, source
transfer, source receipt, source, authority, currentness, truth,
synchronization, deployment, public release, broader reusable permission,
adoption, receiving-context governance, publication flow, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping


class LocalRelevanceMediumReadOnlyDerivativeParticipantRoleAdmissionV0MinV2Error(
    RuntimeError
):
    """Bounded resolver error for role-admission request/path handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2"
)

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "derivative_participant_role_admission_v0_min_v2"
)

SELECTED_COMMAND = "state"

ROLE_ADMISSION_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION"
)
ROLE_ADMISSION_SCOPE = "SELECTED_ROLE_ADMISSION_ONLY"
SUPPORTED_ROLE_ADMISSION_TYPE_VALUES = (ROLE_ADMISSION_TYPE,)
SUPPORTED_ROLE_ADMISSION_SCOPE_VALUES = (ROLE_ADMISSION_SCOPE,)

CONTINUATION_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION"
CONTINUATION_SCOPE = "SELECTED_CONTINUATION_ONLY"
CONTINUATION_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_RECORDED"

INTENT_RECORD = (
    "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION"
)
INTENT_BLOCK = (
    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_ROLE_ADMISSION_ID = (
    "local_relevance_medium_read_only_derivative_participant_role_admission_001"
)
DEFAULT_CONTINUATION_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "continuation_v0_min/"
    "local_relevance_medium_read_only_continuation_reference_review_001"
    "__local_relevance_medium_read_only_continuation_v0_min_result.json"
)
DEFAULT_CONTINUATION_TERMINAL_SUMMARY = (
    "spec/LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION terminal "
    "summary, one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION artifact "
    "for selected command state, and the preserved local relevance medium "
    "read-only continuation basis chain, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION be "
    "recorded for one bounded derivative participant role inside the "
    "already-standing local relevance medium read-only continuation body, "
    "without creating participation motion, authorizing output, authorizing "
    "action, creating participant re-entry, creating derivative reception, "
    "creating vessel relation, creating runtime hosting, creating runtime loop, "
    "creating daemon behavior, creating public API, creating participant-facing "
    "interface, creating distributed network behavior, creating source, "
    "authority, currentness, truth, synchronization, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "participation_motion_created",
    "participant_output_authorized",
    "action_authorization_created",
    "participant_reentry_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "third_operation_created",
    "unbounded_operation_sequence_created",
    "reusable_operation_permission_created",
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
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
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
    "received_derivative_participation_authority_imported",
    "received_derivative_action_authority_imported",
    "bounded_derivative_vessel_authority_imported",
    "derivative_vessel_relation_authority_imported",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "source_created",
    "authority_created",
    "currentness_created",
    "truth_created",
    "synchronization_created",
    "deployment_created",
    "public_release_created",
    "broader_reusable_permission_created",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "follow_on_work_authorized",
    "artifact_existence_treated_as_role_admission_authority",
    "latest_file_posture_treated_as_role_admission_authority",
    "repo_local_availability_treated_as_role_admission_authority",
    "hidden_repo_state_used_as_role_admission_content",
    "hidden_repo_state_used_as_role_admission_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "continuation_v1_failure_repaired",
    "continuation_v1_failure_hidden",
    "continuation_v1_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_derivative_participant_role_admission_recorded",
    "derivative_participant_role_admission_created",
    "bounded_derivative_participant_role_admitted",
    "role_admission_local_only",
    "role_admission_read_only",
    "role_admission_selected_state_only",
    "role_admission_basis_reference_only",
    "role_admission_inside_continuation_body",
    "role_admission_from_continuation_only",
    "basis_continuation_terminal_summary_preserved",
    "basis_continuation_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_continuation_recorded",
    "continuation_created",
    "continuation_local_only",
    "continuation_read_only",
    "continuation_basis_reference_only",
    "continuation_selected_state_only",
    "continuation_from_second_operation",
    "continuation_sequence_count_is_2",
    "continuation_v1_failure_evidence_preserved",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_BLOCK_REQUESTED",
    "CONTINUATION_TERMINAL_SUMMARY_PATH_MISSING",
    "CONTINUATION_ARTIFACT_PATH_MISSING",
    "CONTINUATION_ARTIFACT_UNREADABLE",
    "CONTINUATION_ARTIFACT_NOT_JSON_OBJECT",
    "CONTINUATION_ARTIFACT_NOT_RECORDED",
    "CONTINUATION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "CONTINUATION_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_CONTINUATION_NOT_RECORDED",
    "CONTINUATION_NOT_CREATED",
    "CONTINUATION_LOCAL_ONLY_NOT_TRUE",
    "CONTINUATION_READ_ONLY_NOT_TRUE",
    "CONTINUATION_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "CONTINUATION_SELECTED_STATE_ONLY_NOT_TRUE",
    "CONTINUATION_FROM_SECOND_OPERATION_NOT_TRUE",
    "CONTINUATION_OPERATION_SEQUENCE_COUNT_NOT_2",
    "CONTINUATION_SEQUENCE_COUNT_NOT_2",
    "CONTINUATION_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
    "ROLE_ADMISSION_TYPE_MISSING",
    "ROLE_ADMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION",
    "ROLE_ADMISSION_SCOPE_MISSING",
    "ROLE_ADMISSION_SCOPE_NOT_SELECTED_ROLE_ADMISSION_ONLY",
    "BOUNDED_DERIVATIVE_PARTICIPANT_ROLE_NOT_ADMITTED",
    "ROLE_ADMISSION_LOCAL_ONLY_NOT_TRUE",
    "ROLE_ADMISSION_READ_ONLY_NOT_TRUE",
    "ROLE_ADMISSION_SELECTED_STATE_ONLY_NOT_TRUE",
    "ROLE_ADMISSION_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "ROLE_ADMISSION_NOT_INSIDE_CONTINUATION_BODY",
    "ROLE_ADMISSION_NOT_FROM_CONTINUATION_ONLY",
    "PARTICIPATION_MOTION_CREATED",
    "PARTICIPANT_OUTPUT_AUTHORIZED",
    "ACTION_AUTHORIZATION_CREATED",
    "PARTICIPANT_REENTRY_CREATED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "RUNTIME_HOSTING_CREATED",
    "RUNTIME_LOOP_CREATED",
    "DAEMON_BEHAVIOR_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "THIRD_OPERATION_CREATED",
    "UNBOUNDED_OPERATION_SEQUENCE_CREATED",
    "REUSABLE_OPERATION_PERMISSION_CREATED",
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
    "RAW_STATE_BODY_EMBEDDED",
    "STATE_MUTATION_PERFORMED",
    "STATE_UPDATE_PERFORMED",
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
    "RECEIVED_DERIVATIVE_PARTICIPATION_AUTHORITY_IMPORTED",
    "RECEIVED_DERIVATIVE_ACTION_AUTHORITY_IMPORTED",
    "BOUNDED_DERIVATIVE_VESSEL_AUTHORITY_IMPORTED",
    "DERIVATIVE_VESSEL_RELATION_AUTHORITY_IMPORTED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "TRUTH_CREATED",
    "SYNCHRONIZATION_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_ROLE_ADMISSION_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_ROLE_ADMISSION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_ROLE_ADMISSION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_ROLE_ADMISSION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_ROLE_ADMISSION_AUTHORITY",
    "CONTINUATION_V1_FAILURE_REPAIRED",
    "CONTINUATION_V1_FAILURE_HIDDEN",
    "CONTINUATION_V1_FAILURE_CLAIMED_PASSED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_REQUEST_UNREADABLE",
)

FALSE_FIELD_BLOCK_CODES = {
    "participation_motion_created": "PARTICIPATION_MOTION_CREATED",
    "participant_output_authorized": "PARTICIPANT_OUTPUT_AUTHORIZED",
    "action_authorization_created": "ACTION_AUTHORIZATION_CREATED",
    "participant_reentry_created": "PARTICIPANT_REENTRY_CREATED",
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
    "runtime_hosting_created": "RUNTIME_HOSTING_CREATED",
    "runtime_loop_created": "RUNTIME_LOOP_CREATED",
    "daemon_behavior_created": "DAEMON_BEHAVIOR_CREATED",
    "public_api_created": "PUBLIC_API_CREATED",
    "participant_facing_interface_created": "PARTICIPANT_FACING_INTERFACE_CREATED",
    "distributed_network_behavior_created": "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "third_operation_created": "THIRD_OPERATION_CREATED",
    "unbounded_operation_sequence_created": "UNBOUNDED_OPERATION_SEQUENCE_CREATED",
    "reusable_operation_permission_created": "REUSABLE_OPERATION_PERMISSION_CREATED",
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
    "raw_state_body_embedded": "RAW_STATE_BODY_EMBEDDED",
    "state_mutation_performed": "STATE_MUTATION_PERFORMED",
    "state_update_performed": "STATE_UPDATE_PERFORMED",
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
    "received_derivative_participation_authority_imported": (
        "RECEIVED_DERIVATIVE_PARTICIPATION_AUTHORITY_IMPORTED"
    ),
    "received_derivative_action_authority_imported": (
        "RECEIVED_DERIVATIVE_ACTION_AUTHORITY_IMPORTED"
    ),
    "bounded_derivative_vessel_authority_imported": (
        "BOUNDED_DERIVATIVE_VESSEL_AUTHORITY_IMPORTED"
    ),
    "derivative_vessel_relation_authority_imported": (
        "DERIVATIVE_VESSEL_RELATION_AUTHORITY_IMPORTED"
    ),
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "source_created": "SOURCE_CREATED",
    "authority_created": "AUTHORITY_CREATED",
    "currentness_created": "CURRENTNESS_CREATED",
    "truth_created": "TRUTH_CREATED",
    "synchronization_created": "SYNCHRONIZATION_CREATED",
    "deployment_created": "DEPLOYMENT_CREATED",
    "public_release_created": "PUBLIC_RELEASE_CREATED",
    "broader_reusable_permission_created": "BROADER_REUSABLE_PERMISSION_CREATED",
    "adoption_created": "ADOPTION_CREATED",
    "receiving_context_governance_created": "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "publication_flow_created": "PUBLICATION_FLOW_CREATED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "artifact_existence_treated_as_role_admission_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_ROLE_ADMISSION_AUTHORITY"
    ),
    "latest_file_posture_treated_as_role_admission_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_ROLE_ADMISSION_AUTHORITY"
    ),
    "repo_local_availability_treated_as_role_admission_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_ROLE_ADMISSION_AUTHORITY"
    ),
    "hidden_repo_state_used_as_role_admission_content": (
        "HIDDEN_REPO_STATE_USED_AS_ROLE_ADMISSION_CONTENT"
    ),
    "hidden_repo_state_used_as_role_admission_authority": (
        "HIDDEN_REPO_STATE_USED_AS_ROLE_ADMISSION_AUTHORITY"
    ),
    "prior_artifacts_mutated": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
    "continuation_v1_failure_repaired": "CONTINUATION_V1_FAILURE_REPAIRED",
    "continuation_v1_failure_hidden": "CONTINUATION_V1_FAILURE_HIDDEN",
    "continuation_v1_failure_claimed_passed": (
        "CONTINUATION_V1_FAILURE_CLAIMED_PASSED"
    ),
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
}

ROLE_POSITIVE_FIELDS = (
    "local_relevance_medium_read_only_derivative_participant_role_admission_recorded",
    "derivative_participant_role_admission_created",
    "bounded_derivative_participant_role_admitted",
    "role_admission_local_only",
    "role_admission_read_only",
    "role_admission_selected_state_only",
    "role_admission_basis_reference_only",
    "role_admission_inside_continuation_body",
    "role_admission_from_continuation_only",
)

CONTINUATION_POSITIVE_FIELDS = (
    "selected_continuation_recorded",
    "continuation_created",
    "continuation_local_only",
    "continuation_read_only",
    "continuation_basis_reference_only",
    "continuation_selected_state_only",
    "continuation_from_second_operation",
    "continuation_sequence_count_is_2",
    "predecessor_failure_evidence_preserved",
)

RAW_SENTINELS = (
    "RAW_ROLE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPATION_MOTION_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_OUTPUT_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_AUTHORIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_DERIVATIVE_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_VESSEL_RELATION_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_BODY_MUST_NOT_RETURN",
    "PRESERVED_DERIVATIVE_ANCESTOR_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

OFFICIAL_STRING_VALUES = frozenset(
    OUTCOME_FAMILY
    + BLOCK_CODES
    + SUPPORTED_ROLE_ADMISSION_TYPE_VALUES
    + SUPPORTED_ROLE_ADMISSION_SCOPE_VALUES
    + SUPPORTED_INTENTS
    + (
        SELECTED_COMMAND,
        CONTINUATION_TYPE,
        CONTINUATION_SCOPE,
        CONTINUATION_OUTCOME,
        RESULT_VERSION,
        RESOLVER_MODULE,
    )
)

_MISSING = object()


def _is_mapping(value: Any) -> bool:
    return isinstance(value, dict)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00",
        "Z",
    )


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return REPO_ROOT / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    return str(path)


def _sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return (
        lowered.endswith("_body")
        or "hidden_repo_state" in lowered
        or "current_working_tree" in lowered
        or "local_cache" in lowered
        or lowered in {"raw_body", "raw_artifact_body", "raw_prior_artifact_body"}
    )


def _sanitize_value(value: Any, key: str = "") -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, bool):
        return value
    if value is None:
        return None
    if isinstance(value, str):
        if any(sentinel in value for sentinel in RAW_SENTINELS):
            return "[REDACTED]"
        if key and _sensitive_key(key):
            return "[REDACTED]"
        if value in OFFICIAL_STRING_VALUES:
            return value
        return value
    if key and _sensitive_key(key):
        return "[REDACTED]"
    if isinstance(value, list):
        return [_sanitize_value(item, key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize_value(item, key) for item in value]
    if _is_mapping(value):
        return {
            str(item_key): _sanitize_value(item_value, str(item_key))
            for item_key, item_value in value.items()
        }
    return value


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _add_check(
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
            "expected_posture": _sanitize_value(expected_posture, check_name),
            "actual_posture": _sanitize_value(actual_posture, check_name),
            "block_code": None if passed else code,
            "failure_code": None if passed else code,
        }
    )


def _failed_checks(checks: Iterable[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [check for check in checks if check.get("passed") is False]


def _first_failure_code(checks: Iterable[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code in BLOCK_CODES:
                return code
    return None


def _read_json_object(path_value: Path | str) -> tuple[dict[str, Any] | None, str | None]:
    try:
        with _repo_path(path_value).open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return None, "CONTINUATION_ARTIFACT_UNREADABLE"
    if not _is_mapping(data):
        return None, "CONTINUATION_ARTIFACT_NOT_JSON_OBJECT"
    return data, None


def _selected_continuation_object(artifact: Mapping[str, Any]) -> dict[str, Any]:
    selected = artifact.get("local_relevance_medium_read_only_continuation")
    return copy.deepcopy(selected) if _is_mapping(selected) else {}


def _statement_section(artifact: Mapping[str, Any]) -> dict[str, Any]:
    section = artifact.get("local_relevance_medium_read_only_continuation_statement")
    return copy.deepcopy(section) if _is_mapping(section) else {}


def _summary_section(artifact: Mapping[str, Any]) -> dict[str, Any]:
    section = artifact.get("local_relevance_medium_read_only_continuation_summary")
    return copy.deepcopy(section) if _is_mapping(section) else {}


def _non_meaning_section(artifact: Mapping[str, Any]) -> dict[str, Any]:
    section = artifact.get("local_relevance_medium_read_only_continuation_non_meaning")
    return copy.deepcopy(section) if _is_mapping(section) else {}


def _top_level_non_claims(artifact: Mapping[str, Any]) -> dict[str, Any]:
    section = artifact.get("non_claims")
    return copy.deepcopy(section) if _is_mapping(section) else {}


def _artifact_outcome(artifact: Mapping[str, Any]) -> Any:
    return artifact.get("outcome")


def _artifact_result_version(
    artifact: Mapping[str, Any],
    selected: Mapping[str, Any],
    summary: Mapping[str, Any],
) -> Any:
    metadata = artifact.get("local_relevance_medium_read_only_continuation_metadata")
    if artifact.get("result_version") is not None:
        return artifact.get("result_version")
    if _is_mapping(metadata) and metadata.get(
        "local_relevance_medium_read_only_continuation_version"
    ) is not None:
        return metadata.get("local_relevance_medium_read_only_continuation_version")
    if summary.get("result_version") is not None:
        return summary.get("result_version")
    return selected.get("continuation_version")


def _artifact_failed_check_count(
    artifact: Mapping[str, Any],
    selected: Mapping[str, Any],
    summary: Mapping[str, Any],
) -> Any:
    if artifact.get("failed_check_count") is not None:
        return artifact.get("failed_check_count")
    if summary.get("failed_check_count") is not None:
        return summary.get("failed_check_count")
    if selected.get("failed_check_count") is not None:
        return selected.get("failed_check_count")
    checks = artifact.get("local_relevance_medium_read_only_continuation_checks")
    if isinstance(checks, list):
        return len([check for check in checks if _is_mapping(check) and check.get("passed") is False])
    return None


def _extract_positive(
    field: str,
    artifact: Mapping[str, Any],
    selected: Mapping[str, Any],
    statement: Mapping[str, Any],
    summary: Mapping[str, Any],
    terminal_summary_declared: bool,
) -> Any:
    aliases = {
        "selected_continuation_recorded": (
            "selected_continuation_recorded",
            "local_relevance_medium_read_only_continuation_recorded",
            "continuation_recorded",
        ),
        "continuation_sequence_count_is_2": (
            "continuation_sequence_count_is_2",
            "continuation_operation_sequence_count_is_2",
        ),
    }
    for key in aliases.get(field, (field,)):
        if key in selected:
            return selected[key]
    for section in (statement, summary):
        for key in aliases.get(field, (field,)):
            if key in section:
                return section[key]
    if field == "selected_continuation_recorded":
        return (
            _artifact_outcome(artifact) == CONTINUATION_OUTCOME
            and selected.get("continuation_type") == CONTINUATION_TYPE
            and selected.get("continuation_scope") == CONTINUATION_SCOPE
        )
    if field == "continuation_v1_failure_evidence_preserved":
        for section in (selected, statement, summary, _non_meaning_section(artifact)):
            if "continuation_v1_failure_evidence_preserved" in section:
                return section["continuation_v1_failure_evidence_preserved"]
        return (
            terminal_summary_declared
            and _artifact_outcome(artifact) == CONTINUATION_OUTCOME
            and selected.get("predecessor_failure_evidence_preserved") is True
        )
    return _MISSING


def _extract_sequence_count(
    selected: Mapping[str, Any],
    statement: Mapping[str, Any],
    summary: Mapping[str, Any],
) -> Any:
    for section in (selected, statement, summary):
        if section.get("continuation_operation_sequence_count") is not None:
            return section.get("continuation_operation_sequence_count")
    return _MISSING


def _extract_false_posture(
    field: str,
    artifact: Mapping[str, Any],
    selected: Mapping[str, Any],
    clean_basis: bool,
) -> Any:
    if field in selected:
        return selected[field]
    non_claims = _top_level_non_claims(artifact)
    if field in non_claims:
        return non_claims[field]
    if clean_basis:
        return False
    return _MISSING


def _basis_info(
    request: Mapping[str, Any],
    artifact: Mapping[str, Any] | None,
    selected: Mapping[str, Any],
    summary: Mapping[str, Any],
    read_error: str | None,
) -> dict[str, Any]:
    artifact_path = request.get("selected_continuation_artifact")
    outcome = _artifact_outcome(artifact) if artifact is not None else None
    result_version = (
        _artifact_result_version(artifact, selected, summary)
        if artifact is not None
        else None
    )
    failed_check_count = (
        _artifact_failed_check_count(artifact, selected, summary)
        if artifact is not None
        else None
    )
    return {
        "artifact_path": _display_path(artifact_path),
        "artifact_readable": artifact is not None and read_error is None,
        "artifact_json_object": artifact is not None,
        "artifact_preserved": artifact is not None and read_error is None,
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "selected_object_present": bool(selected),
        "object_type": selected.get("continuation_type"),
        "object_scope": selected.get("continuation_scope"),
        "object_type_matches": selected.get("continuation_type") == CONTINUATION_TYPE,
        "object_scope_matches": selected.get("continuation_scope") == CONTINUATION_SCOPE,
    }


def _validate_header(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    question = request.get(
        "local_relevance_medium_read_only_derivative_participant_role_admission_question"
    )
    _add_check(
        checks,
        "role_admission_question_declared",
        isinstance(question, str) and bool(question.strip()),
        "declared role-admission question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_QUESTION_UNDECLARED",
    )

    intent = request.get(
        "local_relevance_medium_read_only_derivative_participant_role_admission_intent"
    )
    _add_check(
        checks,
        "role_admission_intent_supported",
        intent in SUPPORTED_INTENTS and intent != INTENT_BLOCK,
        f"one of {(INTENT_RECORD, INTENT_DO_NOT_RECORD)}",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_BLOCK_REQUESTED"
        if intent == INTENT_BLOCK
        else "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_INTENT_UNSUPPORTED",
    )

    terminal_summary = request.get("selected_continuation_terminal_summary_path")
    _add_check(
        checks,
        "selected_continuation_terminal_summary_path_declared",
        isinstance(terminal_summary, (str, Path)) and bool(str(terminal_summary)),
        "declared terminal summary path",
        terminal_summary,
        "CONTINUATION_TERMINAL_SUMMARY_PATH_MISSING",
    )

    artifact_path = request.get("selected_continuation_artifact")
    _add_check(
        checks,
        "selected_continuation_artifact_path_declared",
        isinstance(artifact_path, (str, Path)) and bool(str(artifact_path)),
        "declared continuation artifact path",
        artifact_path,
        "CONTINUATION_ARTIFACT_PATH_MISSING",
    )

    selected_command = request.get("selected_command")
    _add_check(
        checks,
        "selected_command_declared",
        selected_command is not None,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_MISSING",
    )
    _add_check(
        checks,
        "selected_command_exactly_state",
        selected_command == SELECTED_COMMAND,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _add_check(
        checks,
        "selected_command_is_state",
        selected_command == SELECTED_COMMAND,
        True,
        selected_command == SELECTED_COMMAND,
        "SELECTED_COMMAND_NOT_STATE",
    )

    role_admission_type = request.get("role_admission_type")
    _add_check(
        checks,
        "role_admission_type_declared",
        role_admission_type is not None,
        ROLE_ADMISSION_TYPE,
        role_admission_type,
        "ROLE_ADMISSION_TYPE_MISSING",
    )
    _add_check(
        checks,
        "role_admission_type_exact",
        role_admission_type == ROLE_ADMISSION_TYPE,
        ROLE_ADMISSION_TYPE,
        role_admission_type,
        "ROLE_ADMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION",
    )

    role_admission_scope = request.get("role_admission_scope")
    _add_check(
        checks,
        "role_admission_scope_declared",
        role_admission_scope is not None,
        ROLE_ADMISSION_SCOPE,
        role_admission_scope,
        "ROLE_ADMISSION_SCOPE_MISSING",
    )
    _add_check(
        checks,
        "role_admission_scope_exact",
        role_admission_scope == ROLE_ADMISSION_SCOPE,
        ROLE_ADMISSION_SCOPE,
        role_admission_scope,
        "ROLE_ADMISSION_SCOPE_NOT_SELECTED_ROLE_ADMISSION_ONLY",
    )


def _validate_declared_non_claims(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    declared = request.get("declared_non_claims")
    mapping_ok = _is_mapping(declared)
    _add_check(
        checks,
        "declared_non_claims_mapping",
        mapping_ok,
        "mapping with all required false non-claims",
        type(declared).__name__,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    declared_map = declared if _is_mapping(declared) else {}
    for key in REQUIRED_FALSE_NON_CLAIMS:
        value = declared_map.get(key, _MISSING)
        _add_check(
            checks,
            f"declared_non_claim_{key}_false",
            value is False,
            False,
            None if value is _MISSING else value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _validate_artifact_basis(
    basis: Mapping[str, Any],
    read_error: str | None,
    checks: list[dict[str, Any]],
) -> bool:
    _add_check(
        checks,
        "selected_continuation_artifact_readable",
        read_error is None,
        "readable JSON object",
        read_error or "readable",
        read_error or "CONTINUATION_ARTIFACT_UNREADABLE",
    )
    _add_check(
        checks,
        "selected_continuation_artifact_object_shaped",
        bool(basis.get("artifact_json_object")),
        "JSON object",
        basis.get("artifact_json_object"),
        "CONTINUATION_ARTIFACT_NOT_JSON_OBJECT",
    )
    _add_check(
        checks,
        "selected_continuation_artifact_outcome_recorded",
        basis.get("outcome") == CONTINUATION_OUTCOME,
        CONTINUATION_OUTCOME,
        basis.get("outcome"),
        "CONTINUATION_ARTIFACT_NOT_RECORDED",
    )
    _add_check(
        checks,
        "selected_continuation_artifact_result_version_0_1_0",
        basis.get("result_version") == RESULT_VERSION,
        RESULT_VERSION,
        basis.get("result_version"),
        "CONTINUATION_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _add_check(
        checks,
        "selected_continuation_artifact_failed_check_count_zero",
        basis.get("failed_check_count") == 0,
        0,
        basis.get("failed_check_count"),
        "CONTINUATION_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    return (
        read_error is None
        and basis.get("artifact_json_object") is True
        and basis.get("outcome") == CONTINUATION_OUTCOME
        and basis.get("result_version") == RESULT_VERSION
        and basis.get("failed_check_count") == 0
        and basis.get("selected_object_present") is True
    )


def _validate_continuation_basis(
    artifact: Mapping[str, Any],
    selected: Mapping[str, Any],
    statement: Mapping[str, Any],
    summary: Mapping[str, Any],
    clean_basis: bool,
    terminal_summary_declared: bool,
    checks: list[dict[str, Any]],
) -> dict[str, Any]:
    values: dict[str, Any] = {}
    for field in CONTINUATION_POSITIVE_FIELDS:
        values[field] = _extract_positive(
            field,
            artifact,
            selected,
            statement,
            summary,
            terminal_summary_declared,
        )
    sequence_count = _extract_sequence_count(selected, statement, summary)
    values["continuation_operation_sequence_count"] = (
        sequence_count if sequence_count is not _MISSING else None
    )
    values["continuation_v1_failure_evidence_preserved"] = _extract_positive(
        "continuation_v1_failure_evidence_preserved",
        artifact,
        selected,
        statement,
        summary,
        terminal_summary_declared,
    )

    check_specs = (
        (
            "selected_continuation_recorded",
            values.get("selected_continuation_recorded") is True,
            True,
            values.get("selected_continuation_recorded"),
            "SELECTED_CONTINUATION_NOT_RECORDED",
        ),
        (
            "continuation_created",
            values.get("continuation_created") is True,
            True,
            values.get("continuation_created"),
            "CONTINUATION_NOT_CREATED",
        ),
        (
            "continuation_local_only",
            values.get("continuation_local_only") is True,
            True,
            values.get("continuation_local_only"),
            "CONTINUATION_LOCAL_ONLY_NOT_TRUE",
        ),
        (
            "continuation_read_only",
            values.get("continuation_read_only") is True,
            True,
            values.get("continuation_read_only"),
            "CONTINUATION_READ_ONLY_NOT_TRUE",
        ),
        (
            "continuation_basis_reference_only",
            values.get("continuation_basis_reference_only") is True,
            True,
            values.get("continuation_basis_reference_only"),
            "CONTINUATION_BASIS_REFERENCE_ONLY_NOT_TRUE",
        ),
        (
            "continuation_selected_state_only",
            values.get("continuation_selected_state_only") is True,
            True,
            values.get("continuation_selected_state_only"),
            "CONTINUATION_SELECTED_STATE_ONLY_NOT_TRUE",
        ),
        (
            "continuation_from_second_operation",
            values.get("continuation_from_second_operation") is True,
            True,
            values.get("continuation_from_second_operation"),
            "CONTINUATION_FROM_SECOND_OPERATION_NOT_TRUE",
        ),
        (
            "continuation_operation_sequence_count_is_2",
            values.get("continuation_operation_sequence_count") == 2,
            2,
            values.get("continuation_operation_sequence_count"),
            "CONTINUATION_OPERATION_SEQUENCE_COUNT_NOT_2",
        ),
        (
            "continuation_sequence_count_is_2",
            values.get("continuation_sequence_count_is_2") is True,
            True,
            values.get("continuation_sequence_count_is_2"),
            "CONTINUATION_SEQUENCE_COUNT_NOT_2",
        ),
        (
            "continuation_v1_failure_evidence_preserved",
            values.get("continuation_v1_failure_evidence_preserved") is True,
            True,
            values.get("continuation_v1_failure_evidence_preserved"),
            "CONTINUATION_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
        ),
        (
            "predecessor_failure_evidence_preserved",
            values.get("predecessor_failure_evidence_preserved") is True,
            True,
            values.get("predecessor_failure_evidence_preserved"),
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
    )
    for check_name, passed, expected, actual, code in check_specs:
        _add_check(checks, check_name, passed, expected, actual, code)

    for key in REQUIRED_FALSE_NON_CLAIMS:
        value = _extract_false_posture(key, artifact, selected, clean_basis)
        if value is _MISSING:
            continue
        _add_check(
            checks,
            f"continuation_basis_{key}_false_posture",
            value is not True,
            False,
            value,
            FALSE_FIELD_BLOCK_CODES[key],
        )
    return values


def _build_role_admission_object(
    request: Mapping[str, Any],
    basis: Mapping[str, Any],
    continuation_values: Mapping[str, Any],
    recorded: bool,
) -> dict[str, Any]:
    role_id = request.get(
        "local_relevance_medium_read_only_derivative_participant_role_admission_id",
        DEFAULT_ROLE_ADMISSION_ID,
    )
    role: dict[str, Any] = {
        "role_admission_id": _sanitize_value(role_id, "role_admission_id"),
        "role_admission_type": ROLE_ADMISSION_TYPE,
        "role_admission_version": RESULT_VERSION,
        "role_admission_scope": ROLE_ADMISSION_SCOPE,
        "basis_continuation_terminal_summary_path": _sanitize_value(
            request.get("selected_continuation_terminal_summary_path"),
            "selected_continuation_terminal_summary_path",
        ),
        "basis_continuation_artifact": _sanitize_value(
            request.get("selected_continuation_artifact"),
            "selected_continuation_artifact",
        ),
        "basis_continuation_outcome": _sanitize_value(
            basis.get("outcome"),
            "basis_continuation_outcome",
        ),
        "basis_continuation_result_version": basis.get("result_version"),
        "basis_continuation_failed_check_count": basis.get("failed_check_count"),
        "basis_continuation_terminal_summary_preserved": bool(
            request.get("selected_continuation_terminal_summary_path")
        ),
        "basis_continuation_artifact_preserved": bool(basis.get("artifact_preserved")),
        "selected_command": _sanitize_value(
            request.get("selected_command"),
            "selected_command",
        ),
        "selected_command_preserved": request.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": request.get("selected_command") == SELECTED_COMMAND,
        "selected_continuation_recorded": continuation_values.get(
            "selected_continuation_recorded"
        )
        is True,
        "continuation_created": continuation_values.get("continuation_created") is True,
        "continuation_local_only": continuation_values.get("continuation_local_only")
        is True,
        "continuation_read_only": continuation_values.get("continuation_read_only")
        is True,
        "continuation_basis_reference_only": continuation_values.get(
            "continuation_basis_reference_only"
        )
        is True,
        "continuation_selected_state_only": continuation_values.get(
            "continuation_selected_state_only"
        )
        is True,
        "continuation_from_second_operation": continuation_values.get(
            "continuation_from_second_operation"
        )
        is True,
        "continuation_operation_sequence_count": 2
        if continuation_values.get("continuation_operation_sequence_count") == 2
        else continuation_values.get("continuation_operation_sequence_count"),
        "continuation_sequence_count_is_2": continuation_values.get(
            "continuation_sequence_count_is_2"
        )
        is True,
    }
    for field in ROLE_POSITIVE_FIELDS:
        role[field] = bool(recorded)
    role.update(_canonical_non_claims())
    role.update(
        {
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "continuation_v1_failure_evidence_preserved": continuation_values.get(
                "continuation_v1_failure_evidence_preserved"
            )
            is True,
            "predecessor_failure_evidence_preserved": continuation_values.get(
                "predecessor_failure_evidence_preserved"
            )
            is True,
            "result_level_non_claims_canonical_false": True,
        }
    )
    return role


def _validate_role_object(
    role: Mapping[str, Any],
    checks: list[dict[str, Any]],
    require_recorded: bool,
) -> None:
    positive_checks = (
        (
            "local_relevance_medium_read_only_derivative_participant_role_admission_recorded",
            "local_relevance_medium_read_only_derivative_participant_role_admission_recorded",
            "BOUNDED_DERIVATIVE_PARTICIPANT_ROLE_NOT_ADMITTED",
        ),
        (
            "derivative_participant_role_admission_created",
            "derivative_participant_role_admission_created",
            "BOUNDED_DERIVATIVE_PARTICIPANT_ROLE_NOT_ADMITTED",
        ),
        (
            "bounded_derivative_participant_role_admitted",
            "bounded_derivative_participant_role_admitted",
            "BOUNDED_DERIVATIVE_PARTICIPANT_ROLE_NOT_ADMITTED",
        ),
        (
            "role_admission_local_only",
            "role_admission_local_only",
            "ROLE_ADMISSION_LOCAL_ONLY_NOT_TRUE",
        ),
        (
            "role_admission_read_only",
            "role_admission_read_only",
            "ROLE_ADMISSION_READ_ONLY_NOT_TRUE",
        ),
        (
            "role_admission_selected_state_only",
            "role_admission_selected_state_only",
            "ROLE_ADMISSION_SELECTED_STATE_ONLY_NOT_TRUE",
        ),
        (
            "role_admission_basis_reference_only",
            "role_admission_basis_reference_only",
            "ROLE_ADMISSION_BASIS_REFERENCE_ONLY_NOT_TRUE",
        ),
        (
            "role_admission_inside_continuation_body",
            "role_admission_inside_continuation_body",
            "ROLE_ADMISSION_NOT_INSIDE_CONTINUATION_BODY",
        ),
        (
            "role_admission_from_continuation_only",
            "role_admission_from_continuation_only",
            "ROLE_ADMISSION_NOT_FROM_CONTINUATION_ONLY",
        ),
    )
    if require_recorded:
        for check_name, field, code in positive_checks:
            _add_check(
                checks,
                check_name,
                role.get(field) is True,
                True,
                role.get(field),
                code,
            )

    for key in REQUIRED_FALSE_NON_CLAIMS:
        _add_check(
            checks,
            f"role_admission_{key}_false",
            role.get(key) is False,
            False,
            role.get(key),
            FALSE_FIELD_BLOCK_CODES[key],
        )
    _add_check(
        checks,
        "result_level_required_false_non_claims_canonical_false",
        role.get("result_level_non_claims_canonical_false") is True,
        True,
        role.get("result_level_non_claims_canonical_false"),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _build_statement(role: Mapping[str, Any]) -> dict[str, Any]:
    statement = {
        "local_relevance_medium_read_only_derivative_participant_role_admission_recorded": role.get(
            "local_relevance_medium_read_only_derivative_participant_role_admission_recorded"
        )
        is True,
        "derivative_participant_role_admission_created": role.get(
            "derivative_participant_role_admission_created"
        )
        is True,
        "bounded_derivative_participant_role_admitted": role.get(
            "bounded_derivative_participant_role_admitted"
        )
        is True,
        "role_admission_local_only": role.get("role_admission_local_only") is True,
        "role_admission_read_only": role.get("role_admission_read_only") is True,
        "role_admission_selected_state_only": role.get(
            "role_admission_selected_state_only"
        )
        is True,
        "role_admission_basis_reference_only": role.get(
            "role_admission_basis_reference_only"
        )
        is True,
        "role_admission_inside_continuation_body": role.get(
            "role_admission_inside_continuation_body"
        )
        is True,
        "role_admission_from_continuation_only": role.get(
            "role_admission_from_continuation_only"
        )
        is True,
        "selected_command_preserved": role.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": role.get("selected_command_is_state") is True,
        "selected_continuation_recorded": role.get("selected_continuation_recorded")
        is True,
        "continuation_created": role.get("continuation_created") is True,
        "continuation_local_only": role.get("continuation_local_only") is True,
        "continuation_read_only": role.get("continuation_read_only") is True,
        "continuation_basis_reference_only": role.get(
            "continuation_basis_reference_only"
        )
        is True,
        "continuation_selected_state_only": role.get("continuation_selected_state_only")
        is True,
        "continuation_from_second_operation": role.get(
            "continuation_from_second_operation"
        )
        is True,
        "continuation_operation_sequence_count": role.get(
            "continuation_operation_sequence_count"
        ),
        "continuation_sequence_count_is_2": role.get("continuation_sequence_count_is_2")
        is True,
        "continuation_v1_failure_evidence_preserved": role.get(
            "continuation_v1_failure_evidence_preserved"
        )
        is True,
        "predecessor_failure_evidence_preserved": role.get(
            "predecessor_failure_evidence_preserved"
        )
        is True,
        "consumed_request_token_remains_closed": role.get(
            "consumed_request_token_remains_closed"
        )
        is True,
        "authorization_token_reuse_blocked": role.get("authorization_token_reuse_blocked")
        is True,
        "result_level_non_claims_canonical_false": role.get(
            "result_level_non_claims_canonical_false"
        )
        is True,
    }
    for key in REQUIRED_FALSE_NON_CLAIMS:
        statement[key] = False
    return statement


def _build_non_meaning() -> dict[str, Any]:
    return {
        "this_is_role_admission_only": True,
        "this_is_not_participation_motion": True,
        "this_is_not_output_authorization": True,
        "this_is_not_action_authorization": True,
        "this_is_not_participant_reentry": True,
        "this_is_not_derivative_reception": True,
        "this_is_not_vessel_relation": True,
        "this_is_not_runtime_hosting": True,
        "this_is_not_runtime_loop": True,
        "this_is_not_daemon_behavior": True,
        "this_is_not_public_api": True,
        "this_is_not_participant_facing_interface": True,
        "this_is_not_distributed_network_behavior": True,
        "this_is_not_source": True,
        "this_is_not_authority": True,
        "this_is_not_currentness": True,
        "this_is_not_truth": True,
        "this_imports_no_preserved_ancestor_derivative_authority": True,
        "role_admission_requires_separate_participation_motion_to_participate": True,
        "output_still_requires_separate_authorization": True,
        "action_still_requires_separate_authorization": True,
    }


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    role_id = request.get(
        "local_relevance_medium_read_only_derivative_participant_role_admission_id",
        DEFAULT_ROLE_ADMISSION_ID,
    )
    return {
        "local_relevance_medium_read_only_derivative_participant_role_admission_id": (
            _sanitize_value(role_id, "role_admission_id")
        ),
        "local_relevance_medium_read_only_derivative_participant_role_admission_type": (
            ROLE_ADMISSION_TYPE
        ),
        "local_relevance_medium_read_only_derivative_participant_role_admission_version": (
            RESULT_VERSION
        ),
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "intent": _sanitize_value(
            request.get(
                "local_relevance_medium_read_only_derivative_participant_role_admission_intent"
            ),
            "intent",
        ),
    }


def _selected_terminal_summary_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "selected_continuation_terminal_summary_path": _sanitize_value(
            request.get("selected_continuation_terminal_summary_path"),
            "selected_continuation_terminal_summary_path",
        ),
        "terminal_summary_path_declared": bool(
            request.get("selected_continuation_terminal_summary_path")
        ),
        "terminal_summary_parsed": False,
        "terminal_summary_required_for_clean_artifact": False,
    }


def _selected_artifact_basis(basis: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "selected_continuation_artifact": _sanitize_value(
            basis.get("artifact_path"),
            "selected_continuation_artifact",
        ),
        "artifact_preserved": bool(basis.get("artifact_preserved")),
        "artifact_readable": bool(basis.get("artifact_readable")),
        "artifact_json_object": bool(basis.get("artifact_json_object")),
        "outcome": _sanitize_value(basis.get("outcome"), "outcome"),
        "result_version": basis.get("result_version"),
        "failed_check_count": basis.get("failed_check_count"),
        "selected_object_present": bool(basis.get("selected_object_present")),
        "object_type": _sanitize_value(basis.get("object_type"), "object_type"),
        "object_scope": _sanitize_value(basis.get("object_scope"), "object_scope"),
        "object_type_matches": bool(basis.get("object_type_matches")),
        "object_scope_matches": bool(basis.get("object_scope_matches")),
    }


def _what_remains_open() -> list[str]:
    return [
        "local_relevance_medium_read_only_derivative_participant_role_admission_test",
        "local_relevance_medium_read_only_derivative_participant_role_admission_live_artifact",
        "local_relevance_medium_read_only_derivative_participant_role_admission_terminal_summary",
        "participation_motion",
        "participant_output_authorization",
        "action_authorization",
        "participant_reentry",
        "derivative_reception",
        "vessel_relation",
        "runtime_hosting",
        "runtime_loop",
        "daemon_behavior",
        "public_api",
        "participant_facing_interface",
        "distributed_network_behavior",
        "source_transfer",
        "source_receipt",
        "source_authority_currentness_truth_synchronization",
        "deployment_public_release",
        "receiving_context_governance",
        "publication_flow",
        "follow_on_work",
    ]


def _summary_from_parts(
    result: Mapping[str, Any],
    checks: Iterable[Mapping[str, Any]],
) -> dict[str, Any]:
    check_list = list(checks)
    failed_count = len(_failed_checks(check_list))
    passed_count = len(check_list) - failed_count
    role = result.get("local_relevance_medium_read_only_derivative_participant_role_admission")
    if not _is_mapping(role):
        role = {}
    block = result.get("block")
    if not _is_mapping(block):
        block = {}
    non_claims = result.get("non_claims")
    if not _is_mapping(non_claims):
        non_claims = {}
    result_level_non_claims_false = all(
        non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
    )
    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "role_admission_id": role.get("role_admission_id"),
        "question": result.get(
            "declared_local_relevance_medium_read_only_derivative_participant_role_admission_question"
        ),
        "intent": (
            result.get(
                "local_relevance_medium_read_only_derivative_participant_role_admission_metadata",
                {},
            ).get("intent")
            if _is_mapping(
                result.get(
                    "local_relevance_medium_read_only_derivative_participant_role_admission_metadata"
                )
            )
            else None
        ),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "selected_command": role.get("selected_command"),
        "selected_command_preserved": role.get("selected_command_preserved") is True,
        "selected_command_is_state": role.get("selected_command_is_state") is True,
        "selected_continuation_recorded": role.get("selected_continuation_recorded")
        is True,
        "continuation_created": role.get("continuation_created") is True,
        "continuation_local_only": role.get("continuation_local_only") is True,
        "continuation_read_only": role.get("continuation_read_only") is True,
        "continuation_basis_reference_only": role.get(
            "continuation_basis_reference_only"
        )
        is True,
        "continuation_selected_state_only": role.get("continuation_selected_state_only")
        is True,
        "continuation_from_second_operation": role.get(
            "continuation_from_second_operation"
        )
        is True,
        "continuation_operation_sequence_count": role.get(
            "continuation_operation_sequence_count"
        ),
        "continuation_sequence_count_is_2": role.get("continuation_sequence_count_is_2")
        is True,
        "role_admission_recorded": role.get(
            "local_relevance_medium_read_only_derivative_participant_role_admission_recorded"
        )
        is True,
        "derivative_participant_role_admission_created": role.get(
            "derivative_participant_role_admission_created"
        )
        is True,
        "bounded_derivative_participant_role_admitted": role.get(
            "bounded_derivative_participant_role_admitted"
        )
        is True,
        "role_admission_local_only": role.get("role_admission_local_only") is True,
        "role_admission_read_only": role.get("role_admission_read_only") is True,
        "role_admission_selected_state_only": role.get(
            "role_admission_selected_state_only"
        )
        is True,
        "role_admission_basis_reference_only": role.get(
            "role_admission_basis_reference_only"
        )
        is True,
        "role_admission_inside_continuation_body": role.get(
            "role_admission_inside_continuation_body"
        )
        is True,
        "role_admission_from_continuation_only": role.get(
            "role_admission_from_continuation_only"
        )
        is True,
        "participation_motion_not_created": role.get("participation_motion_created")
        is False,
        "participant_output_not_authorized": role.get("participant_output_authorized")
        is False,
        "action_authorization_not_created": role.get("action_authorization_created")
        is False,
        "participant_reentry_not_created": role.get("participant_reentry_created")
        is False,
        "derivative_reception_not_authorized": role.get("derivative_reception_authorized")
        is False,
        "vessel_relation_not_authorized": role.get("vessel_relation_authorized")
        is False,
        "runtime_hosting_not_created": role.get("runtime_hosting_created") is False,
        "runtime_loop_not_created": role.get("runtime_loop_created") is False,
        "daemon_behavior_not_created": role.get("daemon_behavior_created") is False,
        "public_api_not_created": role.get("public_api_created") is False,
        "participant_facing_interface_not_created": role.get(
            "participant_facing_interface_created"
        )
        is False,
        "distributed_network_behavior_not_created": role.get(
            "distributed_network_behavior_created"
        )
        is False,
        "source_authority_currentness_truth_synchronization_follow_on_not_created": (
            role.get("source_created") is False
            and role.get("authority_created") is False
            and role.get("currentness_created") is False
            and role.get("truth_created") is False
            and role.get("synchronization_created") is False
            and role.get("follow_on_work_authorized") is False
        ),
        "preserved_ancestor_derivative_surfaces_not_imported_as_authority": (
            role.get("received_derivative_participation_authority_imported") is False
            and role.get("received_derivative_action_authority_imported") is False
            and role.get("bounded_derivative_vessel_authority_imported") is False
            and role.get("derivative_vessel_relation_authority_imported") is False
        ),
        "raw_state_body_not_embedded": role.get("raw_state_body_embedded") is False,
        "state_mutation_not_performed": role.get("state_mutation_performed") is False,
        "state_update_not_performed": role.get("state_update_performed") is False,
        "closure_token_remains_closed": role.get("consumed_request_reopened") is False,
        "authorization_token_reuse_blocked": role.get("authorization_token_reused")
        is False,
        "continuation_v1_failure_evidence_preserved": role.get(
            "continuation_v1_failure_evidence_preserved"
        )
        is True,
        "predecessor_failure_evidence_preserved": role.get(
            "predecessor_failure_evidence_preserved"
        )
        is True,
        "result_level_non_claims_canonical_false": (
            result_level_non_claims_false
            and role.get("result_level_non_claims_canonical_false") is True
        ),
        "hidden_repo_state_role_admission_content_non_claim_is_false": (
            non_claims.get("hidden_repo_state_used_as_role_admission_content")
            is False
        ),
        "hidden_repo_state_role_admission_authority_non_claim_is_false": (
            non_claims.get("hidden_repo_state_used_as_role_admission_authority")
            is False
        ),
    }
    return summary


def build_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_summary(
    result: Mapping[str, Any],
) -> dict:
    checks = result.get(
        "local_relevance_medium_read_only_derivative_participant_role_admission_checks"
    )
    if not isinstance(checks, list):
        checks = []
    return _summary_from_parts(result, checks)


def _finalize_result(
    request: Mapping[str, Any],
    basis: Mapping[str, Any],
    continuation_values: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    role = _build_role_admission_object(request, basis, continuation_values, recorded)
    _validate_role_object(role, checks, recorded)
    statement = _build_statement(role)
    failed = _failed_checks(checks)
    code = _first_failure_code(checks)
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": code if outcome == OUTCOME_BLOCKED else None,
        "block_code": code if outcome == OUTCOME_BLOCKED else None,
        "reason": code if outcome == OUTCOME_BLOCKED else None,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_derivative_participant_role_admission_metadata": (
            _metadata(request)
        ),
        "declared_local_relevance_medium_read_only_derivative_participant_role_admission_question": (
            _sanitize_value(
                request.get(
                    "local_relevance_medium_read_only_derivative_participant_role_admission_question",
                    DEFAULT_QUESTION,
                ),
                "local_relevance_medium_read_only_derivative_participant_role_admission_question",
            )
        ),
        "selected_continuation_terminal_summary_basis": (
            _selected_terminal_summary_basis(request)
        ),
        "selected_continuation_artifact_basis": _selected_artifact_basis(basis),
        "local_relevance_medium_read_only_derivative_participant_role_admission": role,
        "local_relevance_medium_read_only_derivative_participant_role_admission_checks": (
            checks
        ),
        "local_relevance_medium_read_only_derivative_participant_role_admission_statement": (
            statement
        ),
        "local_relevance_medium_read_only_derivative_participant_role_admission_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": []
        if not failed
        else [check["check_name"] for check in failed],
        "not_recorded_basis": []
        if outcome == OUTCOME_RECORDED
        else [check["check_name"] for check in failed],
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result[
        "local_relevance_medium_read_only_derivative_participant_role_admission_summary"
    ] = build_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_summary(
        result
    )
    return _sanitize_value(result)


def _resolve_request(request: Mapping[str, Any]) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _validate_header(request, checks)
    _validate_declared_non_claims(request, checks)

    artifact_path = request.get("selected_continuation_artifact")
    artifact: dict[str, Any] | None = None
    read_error: str | None = "CONTINUATION_ARTIFACT_PATH_MISSING"
    if isinstance(artifact_path, (str, Path)) and bool(str(artifact_path)):
        artifact, read_error = _read_json_object(artifact_path)

    selected = _selected_continuation_object(artifact or {})
    statement = _statement_section(artifact or {})
    summary = _summary_section(artifact or {})
    basis = _basis_info(request, artifact, selected, summary, read_error)
    terminal_summary_declared = bool(request.get("selected_continuation_terminal_summary_path"))
    clean_basis = _validate_artifact_basis(basis, read_error, checks)
    continuation_values = _validate_continuation_basis(
        artifact or {},
        selected,
        statement,
        summary,
        clean_basis,
        terminal_summary_declared,
        checks,
    )

    intent = request.get(
        "local_relevance_medium_read_only_derivative_participant_role_admission_intent"
    )
    failed_before_role = _failed_checks(checks)
    if intent == INTENT_DO_NOT_RECORD and not failed_before_role:
        outcome = OUTCOME_NOT_RECORDED
    elif intent != INTENT_RECORD or failed_before_role:
        outcome = OUTCOME_BLOCKED
    else:
        outcome = OUTCOME_RECORDED
    return _finalize_result(request, basis, continuation_values, checks, outcome)


def resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2(
    declared_local_relevance_medium_read_only_derivative_participant_role_admission: Mapping[str, Any] | None = None,
) -> dict:
    if declared_local_relevance_medium_read_only_derivative_participant_role_admission is None:
        request = build_declared_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_request()
    elif _is_mapping(
        declared_local_relevance_medium_read_only_derivative_participant_role_admission
    ):
        request = copy.deepcopy(
            declared_local_relevance_medium_read_only_derivative_participant_role_admission
        )
    else:
        request = build_declared_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_request()
        request[
            "local_relevance_medium_read_only_derivative_participant_role_admission_intent"
        ] = INTENT_BLOCK
        request["_request_error_code"] = (
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_REQUEST_MALFORMED"
        )
    result = _resolve_request(request)
    error_code = request.get("_request_error_code")
    if isinstance(error_code, str) and error_code in BLOCK_CODES:
        checks = result[
            "local_relevance_medium_read_only_derivative_participant_role_admission_checks"
        ]
        _add_check(
            checks,
            "declared_role_admission_request_valid",
            False,
            "mapping request",
            error_code,
            error_code,
        )
        result["outcome"] = OUTCOME_BLOCKED
        result["block"] = {
            "blocked": True,
            "code": error_code,
            "block_code": error_code,
            "reason": error_code,
        }
        result[
            "local_relevance_medium_read_only_derivative_participant_role_admission_summary"
        ] = build_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_summary(
            result
        )
    return result


def resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_from_path(
    declared_local_relevance_medium_read_only_derivative_participant_role_admission_path: Path | str,
) -> dict:
    try:
        with _repo_path(
            declared_local_relevance_medium_read_only_derivative_participant_role_admission_path
        ).open("r", encoding="utf-8") as handle:
            request = json.load(handle)
    except (OSError, json.JSONDecodeError):
        request = build_declared_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_request()
        request[
            "local_relevance_medium_read_only_derivative_participant_role_admission_intent"
        ] = INTENT_BLOCK
        request["_request_error_code"] = (
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_REQUEST_UNREADABLE"
        )
        return resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2(
            request
        )
    if not _is_mapping(request):
        request = build_declared_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_request()
        request[
            "local_relevance_medium_read_only_derivative_participant_role_admission_intent"
        ] = INTENT_BLOCK
        request["_request_error_code"] = (
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_DERIVATIVE_PARTICIPANT_ROLE_ADMISSION_REQUEST_MALFORMED"
        )
    return resolve_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2(
        request
    )


def _result_filename(result: Mapping[str, Any]) -> str:
    role = result.get("local_relevance_medium_read_only_derivative_participant_role_admission")
    role_id = DEFAULT_ROLE_ADMISSION_ID
    if _is_mapping(role) and isinstance(role.get("role_admission_id"), str):
        role_id = role["role_admission_id"]
    return f"{role_id}__local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_result.json"


def _non_overwriting_path(path: Path) -> Path:
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


def write_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if output_path is None:
        path = REPO_ROOT / OUTPUT_ROOT / _result_filename(result)
    else:
        candidate = _repo_path(output_path)
        if candidate.suffix:
            path = candidate
        else:
            path = candidate / _result_filename(result)
    path = _non_overwriting_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize_value(result), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return path


def build_declared_local_relevance_medium_read_only_derivative_participant_role_admission_v0_min_v2_request(
    local_relevance_medium_read_only_derivative_participant_role_admission_id: str = DEFAULT_ROLE_ADMISSION_ID,
    local_relevance_medium_read_only_derivative_participant_role_admission_question: str = DEFAULT_QUESTION,
    local_relevance_medium_read_only_derivative_participant_role_admission_intent: str = INTENT_RECORD,
    selected_continuation_terminal_summary_path: Path | str = DEFAULT_CONTINUATION_TERMINAL_SUMMARY,
    selected_continuation_artifact: Path | str = DEFAULT_CONTINUATION_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    role_admission_type: str = ROLE_ADMISSION_TYPE,
    role_admission_scope: str = ROLE_ADMISSION_SCOPE,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    if declared_non_claims is not None:
        non_claims.update(copy.deepcopy(dict(declared_non_claims)))
    request = {
        "local_relevance_medium_read_only_derivative_participant_role_admission_id": (
            local_relevance_medium_read_only_derivative_participant_role_admission_id
        ),
        "local_relevance_medium_read_only_derivative_participant_role_admission_question": (
            local_relevance_medium_read_only_derivative_participant_role_admission_question
        ),
        "local_relevance_medium_read_only_derivative_participant_role_admission_intent": (
            local_relevance_medium_read_only_derivative_participant_role_admission_intent
        ),
        "selected_continuation_terminal_summary_path": str(
            selected_continuation_terminal_summary_path
        ),
        "selected_continuation_artifact": str(selected_continuation_artifact),
        "selected_command": selected_command,
        "role_admission_type": role_admission_type,
        "role_admission_scope": role_admission_scope,
        "declared_non_claims": non_claims,
    }
    request.update(copy.deepcopy(overrides))
    return request
