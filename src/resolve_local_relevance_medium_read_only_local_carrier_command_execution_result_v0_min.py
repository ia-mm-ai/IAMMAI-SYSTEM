"""Resolve one selected-state local carrier command execution result.

This resolver records one local read-only selected-state command execution
result object. It reads one clean command execution result boundary artifact as
result-consideration basis and one clean selected-state command execution
artifact as execution basis.

The object is command-execution-result-shaped, local, read-only,
selected-state-only, non-payload, and non-operation-shaped. It records
``command_execution_result_created`` only in the narrow sense that one bounded
local read-only result object exists. It does not return state payload, create a
state result object, expose state packet body, perform lookup, execute lookup
commands, create permissions, create public or distributed surfaces, discover
files, or authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyLocalCarrierCommandExecutionResultV0MinError(
    RuntimeError
):
    """Raised for bounded write/path errors in this resolver."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min"
)

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BLOCKED"
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
    "local_carrier_command_execution_result_v0_min"
)
DEFAULT_COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_execution_result_boundary_v0_min/"
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_"
    "reference_review_001__local_relevance_medium_read_only_local_carrier_"
    "command_execution_result_boundary_v0_min_result.json"
)
DEFAULT_COMMAND_EXECUTION_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_execution_v0_min/"
    "local_relevance_medium_read_only_local_carrier_command_execution_reference_review_001__"
    "local_relevance_medium_read_only_local_carrier_command_execution_v0_min_result.json"
)

DEFAULT_COMMAND_EXECUTION_RESULT_ID = (
    "local_relevance_medium_read_only_local_carrier_command_execution_result_001"
)
COMMAND_EXECUTION_RESULT_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT"
)
COMMAND_EXECUTION_RESULT_SCOPE = "SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY"
SELECTED_COMMAND = "state"

COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED"
)
COMMAND_EXECUTION_RESULT_BOUNDARY_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY"
)
COMMAND_EXECUTION_RESULT_BOUNDARY_SCOPE = (
    "SELECTED_STATE_COMMAND_EXECUTION_RESULT_CONSIDERATION_ONLY"
)
COMMAND_EXECUTION_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RECORDED"
)
COMMAND_EXECUTION_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION"
)
COMMAND_EXECUTION_SCOPE = "SINGLE_LOCAL_READ_ONLY_STATE_COMMAND_EXECUTION_ONLY"

SUPPORTED_COMMAND_EXECUTION_RESULT_TYPE_VALUES = (COMMAND_EXECUTION_RESULT_TYPE,)
SUPPORTED_COMMAND_EXECUTION_RESULT_SCOPE_VALUES = (COMMAND_EXECUTION_RESULT_SCOPE,)

INTENT_RECORD = (
    "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT"
)
INTENT_BLOCK = (
    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY "
    "for selected command state, and one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT be "
    "recorded for the selected-state command execution, without returning state "
    "payload, creating state result object, exposing state packet body, "
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

COMMAND_EXECUTION_RESULT_OBJECT_FALSE_FIELDS = (
    "state_payload_returned",
    "state_result_object_created",
    "state_packet_body_exposed",
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
    "state_payload_returned",
    "state_result_object_created",
    "state_packet_body_exposed",
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
    "artifact_existence_treated_as_command_execution_result_authority",
    "latest_file_posture_treated_as_command_execution_result_authority",
    "repo_local_availability_treated_as_command_execution_result_authority",
    "hidden_repo_state_used_as_command_execution_result_content",
    "hidden_repo_state_used_as_command_execution_result_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_local_carrier_command_execution_result_recorded",
    "basis_command_execution_result_boundary_artifact_preserved",
    "basis_command_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_command_execution_recorded",
    "command_execution_performed",
    "command_execution_local_only",
    "command_execution_read_only",
    "command_execution_result_created",
    "command_execution_result_local_only",
    "command_execution_result_read_only",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BLOCK_REQUESTED",
    "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_PATH_MISSING",
    "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_UNREADABLE",
    "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "COMMAND_EXECUTION_ARTIFACT_PATH_MISSING",
    "COMMAND_EXECUTION_ARTIFACT_UNREADABLE",
    "COMMAND_EXECUTION_ARTIFACT_NOT_JSON_OBJECT",
    "COMMAND_EXECUTION_ARTIFACT_NOT_RECORDED",
    "COMMAND_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "COMMAND_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_COMMAND_EXECUTION_NOT_RECORDED",
    "COMMAND_EXECUTION_NOT_PERFORMED",
    "COMMAND_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    "COMMAND_EXECUTION_READ_ONLY_NOT_TRUE",
    "COMMAND_EXECUTION_RESULT_TYPE_MISSING",
    "COMMAND_EXECUTION_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT",
    "COMMAND_EXECUTION_RESULT_SCOPE_MISSING",
    "COMMAND_EXECUTION_RESULT_SCOPE_NOT_SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY",
    "LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_NOT_RECORDED",
    "COMMAND_EXECUTION_RESULT_NOT_CREATED",
    "COMMAND_EXECUTION_RESULT_LOCAL_ONLY_NOT_TRUE",
    "COMMAND_EXECUTION_RESULT_READ_ONLY_NOT_TRUE",
    "STATE_PAYLOAD_RETURNED",
    "STATE_RESULT_OBJECT_CREATED",
    "STATE_PACKET_BODY_EXPOSED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_RESULT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PRIOR_ARTIFACTS_MUTATED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_REQUEST_UNREADABLE",
)

FALSE_FIELD_BLOCK_CODES = {
    "state_payload_returned": "STATE_PAYLOAD_RETURNED",
    "state_result_object_created": "STATE_RESULT_OBJECT_CREATED",
    "state_packet_body_exposed": "STATE_PACKET_BODY_EXPOSED",
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
    "derivative_reception_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "vessel_relation_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "adoption_created": "FOLLOW_ON_WORK_AUTHORIZED",
    "receiving_context_governance_created": "FOLLOW_ON_WORK_AUTHORIZED",
    "publication_flow_created": "FOLLOW_ON_WORK_AUTHORIZED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "artifact_existence_treated_as_command_execution_result_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY"
    ),
    "latest_file_posture_treated_as_command_execution_result_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY"
    ),
    "repo_local_availability_treated_as_command_execution_result_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY"
    ),
    "hidden_repo_state_used_as_command_execution_result_content": (
        "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_RESULT_CONTENT"
    ),
    "hidden_repo_state_used_as_command_execution_result_authority": (
        "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY"
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

TRUE_FIELD_BLOCK_CODES = {
    "selected_command_execution_recorded": "SELECTED_COMMAND_EXECUTION_NOT_RECORDED",
    "command_execution_performed": "COMMAND_EXECUTION_NOT_PERFORMED",
    "command_execution_local_only": "COMMAND_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    "command_execution_read_only": "COMMAND_EXECUTION_READ_ONLY_NOT_TRUE",
    "local_carrier_command_execution_result_recorded": (
        "LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_NOT_RECORDED"
    ),
    "command_execution_result_created": "COMMAND_EXECUTION_RESULT_NOT_CREATED",
    "command_execution_result_local_only": (
        "COMMAND_EXECUTION_RESULT_LOCAL_ONLY_NOT_TRUE"
    ),
    "command_execution_result_read_only": (
        "COMMAND_EXECUTION_RESULT_READ_ONLY_NOT_TRUE"
    ),
}

SHORTCUT_FAILURES = {
    "command_execution_result_boundary_artifact_missing": (
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_PATH_MISSING"
    ),
    "command_execution_result_boundary_artifact_not_recorded": (
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_NOT_RECORDED"
    ),
    "command_execution_result_boundary_artifact_failed_checks_present": (
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "command_execution_result_boundary_artifact_version_not_0_1_0": (
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "command_execution_artifact_missing": "COMMAND_EXECUTION_ARTIFACT_PATH_MISSING",
    "command_execution_artifact_not_recorded": "COMMAND_EXECUTION_ARTIFACT_NOT_RECORDED",
    "command_execution_artifact_failed_checks_present": (
        "COMMAND_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "command_execution_artifact_version_not_0_1_0": (
        "COMMAND_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "selected_command_missing": "SELECTED_COMMAND_MISSING",
    "selected_command_not_state": "SELECTED_COMMAND_NOT_STATE",
    "selected_command_execution_not_recorded": "SELECTED_COMMAND_EXECUTION_NOT_RECORDED",
    "command_execution_not_performed": "COMMAND_EXECUTION_NOT_PERFORMED",
    "command_execution_local_only_not_true": "COMMAND_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    "command_execution_read_only_not_true": "COMMAND_EXECUTION_READ_ONLY_NOT_TRUE",
    "command_execution_result_type_not_local_relevance_medium_read_only_local_carrier_command_execution_result": (
        "COMMAND_EXECUTION_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT"
    ),
    "command_execution_result_scope_not_selected_state_command_execution_result_only": (
        "COMMAND_EXECUTION_RESULT_SCOPE_NOT_SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY"
    ),
    "local_carrier_command_execution_result_not_recorded": (
        "LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_NOT_RECORDED"
    ),
    "command_execution_result_not_created": "COMMAND_EXECUTION_RESULT_NOT_CREATED",
    "command_execution_result_local_only_not_true": (
        "COMMAND_EXECUTION_RESULT_LOCAL_ONLY_NOT_TRUE"
    ),
    "command_execution_result_read_only_not_true": (
        "COMMAND_EXECUTION_RESULT_READ_ONLY_NOT_TRUE"
    ),
    **FALSE_FIELD_BLOCK_CODES,
}

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_command_execution_result_body",
    "raw_state_payload_body",
    "raw_state_result_body",
    "raw_state_packet_body",
    "raw_lookup_result_body",
    "raw_lookup_performed_body",
    "raw_command_execution_result_boundary_body",
    "raw_command_execution_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "command_execution_result_body",
    "state_payload_body",
    "state_result_body",
    "state_packet_body",
    "lookup_result_body",
    "lookup_performed_body",
    "command_execution_result_boundary_body",
    "command_execution_body",
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

RAW_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
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

OFFICIAL_STRINGS = {
    RESULT_VERSION,
    RESOLVER_MODULE,
    DEFAULT_COMMAND_EXECUTION_RESULT_ID,
    COMMAND_EXECUTION_RESULT_TYPE,
    COMMAND_EXECUTION_RESULT_SCOPE,
    SELECTED_COMMAND,
    COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED_OUTCOME,
    COMMAND_EXECUTION_RECORDED_OUTCOME,
    CORE_QUESTION,
    *OUTCOME_FAMILY,
    *SUPPORTED_INTENTS,
    *SUPPORTED_COMMAND_EXECUTION_RESULT_TYPE_VALUES,
    *SUPPORTED_COMMAND_EXECUTION_RESULT_SCOPE_VALUES,
    *REQUIRED_FALSE_NON_CLAIMS,
    *ALLOWED_TRUE_RECORDED_FIELDS,
    *BLOCK_CODES,
}

FORBIDDEN_OUTPUT_ROOTS = (
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_surface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_reusable_lookup_permission_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_pair_coverage_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_lookup_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_index_system_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_comparison_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_relation_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_multiplicity_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_reception_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_successor_candidate_admission_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_successor_reception_request_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_layer_closure_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_loop_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_reception_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_deployment_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_release_v0_min"),
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _is_mapping(value: Any) -> bool:
    return isinstance(value, MappingABC)


def _mapping_at(mapping: Mapping[str, Any], key: str) -> dict[str, Any]:
    value = mapping.get(key)
    if _is_mapping(value):
        return dict(value)
    return {}


def _sanitize(value: Any, parent_key: str | None = None) -> Any:
    key = parent_key or ""
    key_lower = key.lower()
    sensitive = key_lower in SENSITIVE_CONTENT_KEYS or key_lower.endswith("_body")
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if sensitive or any(sentinel in value for sentinel in RAW_SENTINELS):
            return "[REDACTED_RAW_CONTENT]"
        return value
    if _is_mapping(value):
        if sensitive:
            return "[REDACTED_RAW_CONTENT]"
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        if sensitive:
            return "[REDACTED_RAW_CONTENT]"
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, tuple):
        if sensitive:
            return "[REDACTED_RAW_CONTENT]"
        return [_sanitize(item, parent_key) for item in value]
    return value


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


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
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
    }
    if not passed:
        public_code = (
            code
            if code in BLOCK_CODES
            else "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_REQUEST_MALFORMED"
        )
        record["block_code"] = public_code
        record["failure_code"] = public_code
    checks.append(record)


def _failed_codes(checks: list[dict[str, Any]]) -> list[str]:
    codes: list[str] = []
    for check in checks:
        if check.get("passed") is True:
            continue
        code = check.get("block_code") or check.get("failure_code")
        if isinstance(code, str) and code:
            codes.append(code)
    return codes


def _first_failed_code(checks: list[dict[str, Any]]) -> str | None:
    codes = _failed_codes(checks)
    return codes[0] if codes else None


def _check_counts(checks: list[dict[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = len(checks) - passed
    return passed, failed


def _summary_mapping(artifact: Mapping[str, Any], summary_key: str) -> dict[str, Any]:
    summary = artifact.get(summary_key)
    return dict(summary) if _is_mapping(summary) else {}


def _metadata_mapping(artifact: Mapping[str, Any], metadata_key: str) -> dict[str, Any]:
    metadata = artifact.get(metadata_key)
    return dict(metadata) if _is_mapping(metadata) else {}


def _artifact_outcome(
    artifact: Mapping[str, Any],
    metadata_key: str,
    summary_key: str,
) -> Any:
    summary = _summary_mapping(artifact, summary_key)
    metadata = _metadata_mapping(artifact, metadata_key)
    for candidate in (
        artifact.get("outcome"),
        summary.get("outcome"),
        metadata.get("outcome"),
    ):
        if candidate is not None:
            return candidate
    return None


def _artifact_result_version(
    artifact: Mapping[str, Any],
    metadata_key: str,
    summary_key: str,
    object_mapping: Mapping[str, Any] | None = None,
) -> Any:
    summary = _summary_mapping(artifact, summary_key)
    metadata = _metadata_mapping(artifact, metadata_key)
    object_mapping = object_mapping or {}
    for candidate in (
        artifact.get("result_version"),
        summary.get("result_version"),
        metadata.get("result_version"),
        metadata.get(
            "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_version"
        ),
        metadata.get(
            "local_relevance_medium_read_only_local_carrier_command_execution_version"
        ),
        object_mapping.get("command_execution_result_version"),
        object_mapping.get("boundary_version"),
        object_mapping.get("command_execution_version"),
    ):
        if candidate is not None:
            return candidate
    return None


def _artifact_failed_check_count(
    artifact: Mapping[str, Any],
    metadata_key: str,
    summary_key: str,
    checks_key: str,
) -> Any:
    summary = _summary_mapping(artifact, summary_key)
    metadata = _metadata_mapping(artifact, metadata_key)
    checks = artifact.get(checks_key)
    if isinstance(artifact.get("failed_check_count"), int):
        return artifact.get("failed_check_count")
    if isinstance(summary.get("failed_check_count"), int):
        return summary.get("failed_check_count")
    if isinstance(metadata.get("failed_check_count"), int):
        return metadata.get("failed_check_count")
    if isinstance(checks, list):
        return sum(1 for check in checks if _is_mapping(check) and not check.get("passed"))
    return None


def _read_json_artifact(
    path_value: Any,
    unreadable_code: str,
    not_object_code: str,
) -> tuple[dict[str, Any] | None, str | None]:
    try:
        path = Path(path_value)
    except TypeError:
        return None, unreadable_code
    try:
        with path.open("r", encoding="utf-8") as handle:
            artifact = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return None, unreadable_code
    if not _is_mapping(artifact):
        return None, not_object_code
    return dict(artifact), None


def _append_declared_request_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    question = declared.get(
        "local_relevance_medium_read_only_local_carrier_command_execution_result_question"
    )
    _check(
        checks,
        "command execution result question declared",
        isinstance(question, str) and bool(question.strip()),
        "declared non-empty question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_QUESTION_UNDECLARED",
    )

    intent = declared.get(
        "local_relevance_medium_read_only_local_carrier_command_execution_result_intent"
    )
    _check(
        checks,
        "command execution result intent supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _check(
            checks,
            "explicit block intent not requested",
            False,
            "no explicit block request",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BLOCK_REQUESTED",
        )

    result_type = declared.get("command_execution_result_type")
    _check(
        checks,
        "command execution result type declared",
        result_type is not None,
        COMMAND_EXECUTION_RESULT_TYPE,
        result_type,
        "COMMAND_EXECUTION_RESULT_TYPE_MISSING",
    )
    _check(
        checks,
        "command execution result type exact",
        result_type == COMMAND_EXECUTION_RESULT_TYPE,
        COMMAND_EXECUTION_RESULT_TYPE,
        result_type,
        "COMMAND_EXECUTION_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT",
    )

    result_scope = declared.get("command_execution_result_scope")
    _check(
        checks,
        "command execution result scope declared",
        result_scope is not None,
        COMMAND_EXECUTION_RESULT_SCOPE,
        result_scope,
        "COMMAND_EXECUTION_RESULT_SCOPE_MISSING",
    )
    _check(
        checks,
        "command execution result scope exact",
        result_scope == COMMAND_EXECUTION_RESULT_SCOPE,
        COMMAND_EXECUTION_RESULT_SCOPE,
        result_scope,
        "COMMAND_EXECUTION_RESULT_SCOPE_NOT_SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY",
    )


def _append_selected_command_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    selected_command = declared.get("selected_command")
    _check(
        checks,
        "selected command declared",
        selected_command is not None,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_MISSING",
    )
    _check(
        checks,
        "selected command exactly state",
        selected_command == SELECTED_COMMAND,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )


def _append_shortcut_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    for field, code in SHORTCUT_FAILURES.items():
        if declared.get(field) is True:
            _check(
                checks,
                f"{field} shortcut not asserted",
                False,
                False,
                True,
                code,
            )


def _append_declared_non_claim_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    declared_non_claims = declared.get("declared_non_claims")
    if not _is_mapping(declared_non_claims):
        _check(
            checks,
            "declared non-claims mapping present",
            False,
            "mapping with every required non-claim set to false",
            declared_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return
    for key in REQUIRED_FALSE_NON_CLAIMS:
        value = declared_non_claims.get(key)
        _check(
            checks,
            f"declared non-claim {key} false",
            value is False,
            False,
            value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _append_false_posture_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    for field, code in FALSE_FIELD_BLOCK_CODES.items():
        if field in declared:
            _check(
                checks,
                f"{field} not created or authorized",
                declared.get(field) is False,
                False,
                declared.get(field),
                code,
            )


def _append_true_posture_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    for field, code in TRUE_FIELD_BLOCK_CODES.items():
        if field in declared:
            _check(
                checks,
                f"{field} true when declared",
                declared.get(field) is True,
                True,
                declared.get(field),
                code,
            )


def _validate_command_execution_result_boundary_artifact(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    artifact_path = declared.get("selected_command_execution_result_boundary_artifact")
    basis = {
        "artifact": _sanitize(artifact_path),
        "outcome": None,
        "result_version": None,
        "failed_check_count": None,
    }
    _check(
        checks,
        "command execution result boundary artifact path declared",
        isinstance(artifact_path, (str, Path)) and bool(str(artifact_path)),
        "path to one command execution result boundary artifact",
        artifact_path,
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_PATH_MISSING",
    )
    if not isinstance(artifact_path, (str, Path)) or not str(artifact_path):
        return basis, {}

    artifact, read_code = _read_json_artifact(
        artifact_path,
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_UNREADABLE",
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    )
    _check(
        checks,
        "command execution result boundary artifact readable JSON object",
        read_code is None,
        "readable JSON object",
        read_code or "readable JSON object",
        read_code or "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_UNREADABLE",
    )
    if artifact is None:
        return basis, {}

    boundary = _mapping_at(
        artifact,
        "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary",
    )
    metadata_key = (
        "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_metadata"
    )
    summary_key = (
        "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_summary"
    )
    checks_key = (
        "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_checks"
    )
    outcome = _artifact_outcome(artifact, metadata_key, summary_key)
    result_version = _artifact_result_version(
        artifact, metadata_key, summary_key, boundary
    )
    failed_check_count = _artifact_failed_check_count(
        artifact, metadata_key, summary_key, checks_key
    )
    basis.update(
        {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
        }
    )

    _check(
        checks,
        "command execution result boundary artifact outcome recorded",
        outcome == COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED_OUTCOME,
        COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED_OUTCOME,
        outcome,
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "command execution result boundary artifact result version 0.1.0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version,
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "command execution result boundary artifact failed check count zero",
        failed_check_count == 0,
        0,
        failed_check_count,
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "command execution result boundary type exact in artifact",
        boundary.get("boundary_type") == COMMAND_EXECUTION_RESULT_BOUNDARY_TYPE,
        COMMAND_EXECUTION_RESULT_BOUNDARY_TYPE,
        boundary.get("boundary_type"),
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "command execution result boundary scope exact in artifact",
        boundary.get("boundary_scope") == COMMAND_EXECUTION_RESULT_BOUNDARY_SCOPE,
        COMMAND_EXECUTION_RESULT_BOUNDARY_SCOPE,
        boundary.get("boundary_scope"),
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "selected command preserved by command execution result boundary artifact",
        boundary.get("selected_command") == SELECTED_COMMAND,
        SELECTED_COMMAND,
        boundary.get("selected_command"),
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected command is state in command execution result boundary artifact",
        boundary.get("selected_command_is_state") is True,
        True,
        boundary.get("selected_command_is_state"),
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected command execution recorded in command execution result boundary artifact",
        boundary.get("selected_command_execution_recorded") is True,
        True,
        boundary.get("selected_command_execution_recorded"),
        "SELECTED_COMMAND_EXECUTION_NOT_RECORDED",
    )
    _check(
        checks,
        "command execution performed in command execution result boundary artifact",
        boundary.get("command_execution_performed") is True,
        True,
        boundary.get("command_execution_performed"),
        "COMMAND_EXECUTION_NOT_PERFORMED",
    )
    _check(
        checks,
        "command execution local only in command execution result boundary artifact",
        boundary.get("command_execution_local_only") is True,
        True,
        boundary.get("command_execution_local_only"),
        "COMMAND_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "command execution read only in command execution result boundary artifact",
        boundary.get("command_execution_read_only") is True,
        True,
        boundary.get("command_execution_read_only"),
        "COMMAND_EXECUTION_READ_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "future command execution result considered by boundary artifact",
        boundary.get("future_command_execution_result_may_be_considered") is True,
        True,
        boundary.get("future_command_execution_result_may_be_considered"),
        "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    for field in COMMAND_EXECUTION_RESULT_OBJECT_FALSE_FIELDS:
        if field in boundary:
            _check(
                checks,
                f"{field} false in command execution result boundary artifact",
                boundary.get(field) is False,
                False,
                boundary.get(field),
                FALSE_FIELD_BLOCK_CODES.get(field, "FOLLOW_ON_WORK_AUTHORIZED"),
            )
    if "command_execution_result_created" in boundary:
        _check(
            checks,
            "command execution result not already created by boundary artifact",
            boundary.get("command_execution_result_created") is False,
            False,
            boundary.get("command_execution_result_created"),
            "COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT_NOT_RECORDED",
        )
    return basis, boundary


def _validate_command_execution_artifact(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    artifact_path = declared.get("selected_command_execution_artifact")
    basis = {
        "artifact": _sanitize(artifact_path),
        "outcome": None,
        "result_version": None,
        "failed_check_count": None,
    }
    _check(
        checks,
        "command execution artifact path declared",
        isinstance(artifact_path, (str, Path)) and bool(str(artifact_path)),
        "path to one selected-state command execution artifact",
        artifact_path,
        "COMMAND_EXECUTION_ARTIFACT_PATH_MISSING",
    )
    if not isinstance(artifact_path, (str, Path)) or not str(artifact_path):
        return basis, {}

    artifact, read_code = _read_json_artifact(
        artifact_path,
        "COMMAND_EXECUTION_ARTIFACT_UNREADABLE",
        "COMMAND_EXECUTION_ARTIFACT_NOT_JSON_OBJECT",
    )
    _check(
        checks,
        "command execution artifact readable JSON object",
        read_code is None,
        "readable JSON object",
        read_code or "readable JSON object",
        read_code or "COMMAND_EXECUTION_ARTIFACT_UNREADABLE",
    )
    if artifact is None:
        return basis, {}

    command_execution = _mapping_at(
        artifact,
        "local_relevance_medium_read_only_local_carrier_command_execution",
    )
    metadata_key = (
        "local_relevance_medium_read_only_local_carrier_command_execution_metadata"
    )
    summary_key = (
        "local_relevance_medium_read_only_local_carrier_command_execution_summary"
    )
    checks_key = "local_relevance_medium_read_only_local_carrier_command_execution_checks"
    outcome = _artifact_outcome(artifact, metadata_key, summary_key)
    result_version = _artifact_result_version(
        artifact, metadata_key, summary_key, command_execution
    )
    failed_check_count = _artifact_failed_check_count(
        artifact, metadata_key, summary_key, checks_key
    )
    basis.update(
        {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
        }
    )

    _check(
        checks,
        "command execution artifact outcome recorded",
        outcome == COMMAND_EXECUTION_RECORDED_OUTCOME,
        COMMAND_EXECUTION_RECORDED_OUTCOME,
        outcome,
        "COMMAND_EXECUTION_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "command execution artifact result version 0.1.0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version,
        "COMMAND_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "command execution artifact failed check count zero",
        failed_check_count == 0,
        0,
        failed_check_count,
        "COMMAND_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "command execution type in artifact",
        command_execution.get("command_execution_type") == COMMAND_EXECUTION_TYPE,
        COMMAND_EXECUTION_TYPE,
        command_execution.get("command_execution_type"),
        "COMMAND_EXECUTION_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "command execution scope in artifact",
        command_execution.get("command_execution_scope") == COMMAND_EXECUTION_SCOPE,
        COMMAND_EXECUTION_SCOPE,
        command_execution.get("command_execution_scope"),
        "COMMAND_EXECUTION_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "selected command preserved by command execution artifact",
        command_execution.get("selected_command") == SELECTED_COMMAND,
        SELECTED_COMMAND,
        command_execution.get("selected_command"),
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected command is state in command execution artifact",
        command_execution.get("selected_command_is_state") is True,
        True,
        command_execution.get("selected_command_is_state"),
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected command execution recorded in command execution artifact",
        command_execution.get("local_carrier_command_execution_recorded") is True,
        True,
        command_execution.get("local_carrier_command_execution_recorded"),
        "SELECTED_COMMAND_EXECUTION_NOT_RECORDED",
    )
    _check(
        checks,
        "command execution performed in command execution artifact",
        command_execution.get("command_execution_performed") is True,
        True,
        command_execution.get("command_execution_performed"),
        "COMMAND_EXECUTION_NOT_PERFORMED",
    )
    _check(
        checks,
        "command execution local only in command execution artifact",
        command_execution.get("command_execution_local_only") is True,
        True,
        command_execution.get("command_execution_local_only"),
        "COMMAND_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "command execution read only in command execution artifact",
        command_execution.get("command_execution_read_only") is True,
        True,
        command_execution.get("command_execution_read_only"),
        "COMMAND_EXECUTION_READ_ONLY_NOT_TRUE",
    )
    for field in COMMAND_EXECUTION_RESULT_OBJECT_FALSE_FIELDS:
        if field in command_execution:
            _check(
                checks,
                f"{field} false in command execution artifact",
                command_execution.get(field) is False,
                False,
                command_execution.get(field),
                FALSE_FIELD_BLOCK_CODES.get(field, "FOLLOW_ON_WORK_AUTHORIZED"),
            )
    return basis, command_execution


def _append_command_execution_result_membrane_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    _append_false_posture_checks(checks, declared)
    _append_true_posture_checks(checks, declared)
    _append_shortcut_checks(checks, declared)
    _append_declared_non_claim_checks(checks, declared)
    _check(
        checks,
        "artifact existence not command execution result authority",
        declared.get("artifact_existence_treated_as_command_execution_result_authority")
        is not True,
        False,
        declared.get("artifact_existence_treated_as_command_execution_result_authority"),
        "ARTIFACT_EXISTENCE_TREATED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY",
    )
    _check(
        checks,
        "latest file posture not command execution result authority",
        declared.get("latest_file_posture_treated_as_command_execution_result_authority")
        is not True,
        False,
        declared.get("latest_file_posture_treated_as_command_execution_result_authority"),
        "LATEST_FILE_POSTURE_TREATED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY",
    )
    _check(
        checks,
        "repo local availability not command execution result authority",
        declared.get("repo_local_availability_treated_as_command_execution_result_authority")
        is not True,
        False,
        declared.get("repo_local_availability_treated_as_command_execution_result_authority"),
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY",
    )
    _check(
        checks,
        "hidden repo state not command execution result content",
        declared.get("hidden_repo_state_used_as_command_execution_result_content")
        is not True,
        False,
        declared.get("hidden_repo_state_used_as_command_execution_result_content"),
        "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_RESULT_CONTENT",
    )
    _check(
        checks,
        "hidden repo state not command execution result authority",
        declared.get("hidden_repo_state_used_as_command_execution_result_authority")
        is not True,
        False,
        declared.get("hidden_repo_state_used_as_command_execution_result_authority"),
        "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_RESULT_AUTHORITY",
    )
    predecessor_clean = not any(
        declared.get(key) is True
        for key in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
    )
    _check(
        checks,
        "predecessor failure evidence preserved",
        predecessor_clean,
        "preserved predecessor failure evidence",
        "repaired/hidden/claimed passed" if not predecessor_clean else "preserved",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _check(
        checks,
        "consumed request remains closed",
        declared.get("consumed_request_reopened") is not True,
        False,
        declared.get("consumed_request_reopened"),
        "CONSUMED_REQUEST_REOPENED",
    )
    _check(
        checks,
        "authorization token not reused",
        declared.get("authorization_token_reused") is not True,
        False,
        declared.get("authorization_token_reused"),
        "AUTHORIZATION_TOKEN_REUSED",
    )


def _build_command_execution_result_object(
    declared: Mapping[str, Any],
    boundary_basis: Mapping[str, Any],
    command_execution_basis: Mapping[str, Any],
    recorded: bool,
) -> dict[str, Any]:
    selected_command = declared.get("selected_command")
    if not isinstance(selected_command, str):
        selected_command = ""
    execution_result = {
        "command_execution_result_id": str(
            declared.get(
                "local_relevance_medium_read_only_local_carrier_command_execution_result_id",
                DEFAULT_COMMAND_EXECUTION_RESULT_ID,
            )
        ),
        "command_execution_result_type": COMMAND_EXECUTION_RESULT_TYPE,
        "command_execution_result_version": RESULT_VERSION,
        "command_execution_result_scope": COMMAND_EXECUTION_RESULT_SCOPE,
        "basis_command_execution_result_boundary_artifact": _sanitize(
            boundary_basis.get("artifact")
        ),
        "basis_command_execution_result_boundary_outcome": boundary_basis.get(
            "outcome"
        ),
        "basis_command_execution_result_boundary_result_version": boundary_basis.get(
            "result_version"
        ),
        "basis_command_execution_result_boundary_failed_check_count": boundary_basis.get(
            "failed_check_count"
        ),
        "basis_command_execution_artifact": _sanitize(
            command_execution_basis.get("artifact")
        ),
        "basis_command_execution_outcome": command_execution_basis.get("outcome"),
        "basis_command_execution_result_version": command_execution_basis.get(
            "result_version"
        ),
        "basis_command_execution_failed_check_count": command_execution_basis.get(
            "failed_check_count"
        ),
        "selected_command": selected_command,
        "selected_command_is_state": recorded and selected_command == SELECTED_COMMAND,
        "selected_command_execution_recorded": recorded,
        "command_execution_performed": recorded,
        "command_execution_local_only": recorded,
        "command_execution_read_only": recorded,
        "local_carrier_command_execution_result_recorded": recorded,
        "command_execution_result_created": recorded,
        "command_execution_result_local_only": recorded,
        "command_execution_result_read_only": recorded,
    }
    for field in COMMAND_EXECUTION_RESULT_OBJECT_FALSE_FIELDS:
        execution_result[field] = False
    return execution_result


def _build_statement(
    outcome: str,
    execution_result: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    boundary_preserved = (
        recorded
        and execution_result.get("basis_command_execution_result_boundary_outcome")
        == COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED_OUTCOME
        and execution_result.get("basis_command_execution_result_boundary_result_version")
        == RESULT_VERSION
        and execution_result.get(
            "basis_command_execution_result_boundary_failed_check_count"
        )
        == 0
    )
    execution_preserved = (
        recorded
        and execution_result.get("basis_command_execution_outcome")
        == COMMAND_EXECUTION_RECORDED_OUTCOME
        and execution_result.get("basis_command_execution_result_version")
        == RESULT_VERSION
        and execution_result.get("basis_command_execution_failed_check_count") == 0
    )
    return {
        "local_relevance_medium_read_only_local_carrier_command_execution_result_recorded": recorded,
        "basis_command_execution_result_boundary_artifact_preserved": boundary_preserved,
        "basis_command_execution_artifact_preserved": execution_preserved,
        "selected_command_preserved": recorded
        and execution_result.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": execution_result.get("selected_command_is_state")
        is True,
        "selected_command_execution_recorded": execution_result.get(
            "selected_command_execution_recorded"
        )
        is True,
        "command_execution_performed": execution_result.get("command_execution_performed")
        is True,
        "command_execution_local_only": execution_result.get(
            "command_execution_local_only"
        )
        is True,
        "command_execution_read_only": execution_result.get("command_execution_read_only")
        is True,
        "command_execution_result_created": execution_result.get(
            "command_execution_result_created"
        )
        is True,
        "command_execution_result_local_only": execution_result.get(
            "command_execution_result_local_only"
        )
        is True,
        "command_execution_result_read_only": execution_result.get(
            "command_execution_result_read_only"
        )
        is True,
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _build_non_meaning(non_claims: Mapping[str, bool]) -> dict[str, Any]:
    return {
        "command_execution_result_is_not_state_payload_return": True,
        "command_execution_result_is_not_state_result_object": True,
        "command_execution_result_exposes_no_state_packet_body": True,
        "command_execution_result_performs_no_lookup": True,
        "command_execution_result_executes_no_lookup_command": True,
        "command_execution_result_creates_no_operation_permission": True,
        "command_execution_result_creates_no_runtime_permission": True,
        "command_execution_result_creates_no_public_api": True,
        "command_execution_result_creates_no_participant_facing_interface": True,
        "command_execution_result_creates_no_distributed_network_behavior": True,
        "command_execution_result_creates_no_general_lookup_permission": True,
        "command_execution_result_creates_no_arbitrary_lookup_permission": True,
        "command_execution_result_creates_no_registry_search_query_or_ranking": True,
        "command_execution_result_authorizes_no_follow_on_work": True,
        "result_level_non_claims": dict(non_claims),
    }


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium read-only local carrier command execution result test",
        "local relevance medium read-only local carrier command execution result live artifact",
        "local relevance medium read-only local carrier command execution result terminal summary, if needed",
        "state payload return",
        "state result object",
        "state packet body exposure",
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
        "follow-on work",
    ]


def _determine_outcome(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> str:
    if _first_failed_code(checks):
        return OUTCOME_BLOCKED
    requested = declared.get(
        "requested_local_relevance_medium_read_only_local_carrier_command_execution_result_outcome"
    )
    if requested in OUTCOME_FAMILY:
        return requested
    intent = declared.get(
        "local_relevance_medium_read_only_local_carrier_command_execution_result_intent"
    )
    if intent == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    if declared.get("additional_basis_context"):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if declared.get("not_recorded_basis"):
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _build_block(
    outcome: str,
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> dict[str, Any] | None:
    if outcome != OUTCOME_BLOCKED:
        return None
    code = _first_failed_code(checks) or (
        "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_REQUEST_MALFORMED"
    )
    reason = declared.get("block_reason")
    if not isinstance(reason, str) or not reason.strip():
        reason = "local relevance medium read-only local carrier command execution result blocked"
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": _sanitize(reason),
    }


def _finalize_result(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
    boundary_basis: Mapping[str, Any],
    command_execution_basis: Mapping[str, Any],
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    outcome = _determine_outcome(declared, checks)
    recorded = outcome == OUTCOME_RECORDED
    execution_result = _build_command_execution_result_object(
        declared, boundary_basis, command_execution_basis, recorded
    )
    statement = _build_statement(outcome, execution_result, non_claims)
    passed_check_count, failed_check_count = _check_counts(checks)

    metadata = {
        "local_relevance_medium_read_only_local_carrier_command_execution_result_id": execution_result[
            "command_execution_result_id"
        ],
        "local_relevance_medium_read_only_local_carrier_command_execution_result_type": COMMAND_EXECUTION_RESULT_TYPE,
        "local_relevance_medium_read_only_local_carrier_command_execution_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
    }
    declared_question = {
        "question": _sanitize(
            declared.get(
                "local_relevance_medium_read_only_local_carrier_command_execution_result_question"
            )
        ),
        "intent": _sanitize(
            declared.get(
                "local_relevance_medium_read_only_local_carrier_command_execution_result_intent"
            )
        ),
        "selected_command_execution_result_boundary_artifact": _sanitize(
            declared.get("selected_command_execution_result_boundary_artifact")
        ),
        "selected_command_execution_artifact": _sanitize(
            declared.get("selected_command_execution_artifact")
        ),
        "selected_command": _sanitize(declared.get("selected_command")),
        "command_execution_result_type": _sanitize(
            declared.get("command_execution_result_type")
        ),
        "command_execution_result_scope": _sanitize(
            declared.get("command_execution_result_scope")
        ),
    }
    boundary_artifact_basis = {
        "selected_command_execution_result_boundary_artifact": _sanitize(
            boundary_basis.get("artifact")
        ),
        "basis_command_execution_result_boundary_outcome": boundary_basis.get(
            "outcome"
        ),
        "basis_command_execution_result_boundary_result_version": boundary_basis.get(
            "result_version"
        ),
        "basis_command_execution_result_boundary_failed_check_count": boundary_basis.get(
            "failed_check_count"
        ),
        "basis_role": "command execution result consideration basis only",
    }
    command_execution_artifact_basis = {
        "selected_command_execution_artifact": _sanitize(
            command_execution_basis.get("artifact")
        ),
        "basis_command_execution_outcome": command_execution_basis.get("outcome"),
        "basis_command_execution_result_version": command_execution_basis.get(
            "result_version"
        ),
        "basis_command_execution_failed_check_count": command_execution_basis.get(
            "failed_check_count"
        ),
        "basis_role": "selected-state command execution basis only",
    }
    additional_basis_required = []
    if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        additional_basis_required.append(
            _sanitize(declared.get("additional_basis_context") or "additional basis required")
        )
    not_recorded_basis = []
    if outcome == OUTCOME_NOT_RECORDED:
        not_recorded_basis.append(
            _sanitize(declared.get("not_recorded_basis") or "command execution result not recorded")
        )

    result: dict[str, Any] = {
        "local_relevance_medium_read_only_local_carrier_command_execution_result_metadata": metadata,
        "declared_local_relevance_medium_read_only_local_carrier_command_execution_result_question": declared_question,
        "selected_command_execution_result_boundary_artifact_basis": boundary_artifact_basis,
        "selected_command_execution_artifact_basis": command_execution_artifact_basis,
        "local_relevance_medium_read_only_local_carrier_command_execution_result": execution_result,
        "local_relevance_medium_read_only_local_carrier_command_execution_result_checks": checks,
        "local_relevance_medium_read_only_local_carrier_command_execution_result_statement": statement,
        "local_relevance_medium_read_only_local_carrier_command_execution_result_non_meaning": _build_non_meaning(
            non_claims
        ),
        "additional_basis_required": additional_basis_required,
        "not_recorded_basis": not_recorded_basis,
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": _build_block(outcome, checks, declared),
    }
    result[
        "local_relevance_medium_read_only_local_carrier_command_execution_result_summary"
    ] = build_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_summary(
        result
    )
    return _sanitize(result)


def resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
    declared_local_relevance_medium_read_only_local_carrier_command_execution_result: Mapping[
        str, Any
    ]
    | None = None,
) -> dict[str, Any]:
    """Resolve one selected-state command execution result request."""

    if declared_local_relevance_medium_read_only_local_carrier_command_execution_result is None:
        declared = (
            build_declared_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_request()
        )
    elif not _is_mapping(
        declared_local_relevance_medium_read_only_local_carrier_command_execution_result
    ):
        checks: list[dict[str, Any]] = []
        _check(
            checks,
            "declared request mapping",
            False,
            "mapping",
            type(
                declared_local_relevance_medium_read_only_local_carrier_command_execution_result
            ).__name__,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_REQUEST_MALFORMED",
        )
        declared = {
            "local_relevance_medium_read_only_local_carrier_command_execution_result_id": DEFAULT_COMMAND_EXECUTION_RESULT_ID,
            "local_relevance_medium_read_only_local_carrier_command_execution_result_question": None,
            "local_relevance_medium_read_only_local_carrier_command_execution_result_intent": None,
            "selected_command_execution_result_boundary_artifact": None,
            "selected_command_execution_artifact": None,
            "selected_command": None,
            "command_execution_result_type": None,
            "command_execution_result_scope": None,
            "declared_non_claims": {},
        }
        empty_basis = {
            "artifact": None,
            "outcome": None,
            "result_version": None,
            "failed_check_count": None,
        }
        return _finalize_result(declared, checks, empty_basis, empty_basis)
    else:
        declared = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_local_carrier_command_execution_result)
        )

    checks = []
    _append_declared_request_checks(checks, declared)
    _append_selected_command_checks(checks, declared)
    boundary_basis, _boundary = _validate_command_execution_result_boundary_artifact(
        checks, declared
    )
    command_execution_basis, _command_execution = _validate_command_execution_artifact(
        checks, declared
    )
    _append_command_execution_result_membrane_checks(checks, declared)
    _check(
        checks,
        "result-level required false non-claims canonical false",
        all(_canonical_non_claims().get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS),
        "all emitted result-level non-claims false",
        "all emitted result-level non-claims false",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return _finalize_result(declared, checks, boundary_basis, command_execution_basis)


def resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_from_path(
    declared_local_relevance_medium_read_only_local_carrier_command_execution_result_path: Path
    | str,
) -> dict[str, Any]:
    """Read a declared request JSON file and resolve it."""

    try:
        path = Path(
            declared_local_relevance_medium_read_only_local_carrier_command_execution_result_path
        )
        with path.open("r", encoding="utf-8") as handle:
            declared = json.load(handle)
    except (OSError, TypeError, json.JSONDecodeError):
        checks: list[dict[str, Any]] = []
        _check(
            checks,
            "declared request path readable JSON",
            False,
            "readable request JSON object",
            str(
                declared_local_relevance_medium_read_only_local_carrier_command_execution_result_path
            ),
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_REQUEST_UNREADABLE",
        )
        empty_basis = {
            "artifact": None,
            "outcome": None,
            "result_version": None,
            "failed_check_count": None,
        }
        declared_fallback = {
            "local_relevance_medium_read_only_local_carrier_command_execution_result_id": DEFAULT_COMMAND_EXECUTION_RESULT_ID,
            "local_relevance_medium_read_only_local_carrier_command_execution_result_question": None,
            "local_relevance_medium_read_only_local_carrier_command_execution_result_intent": None,
            "selected_command_execution_result_boundary_artifact": None,
            "selected_command_execution_artifact": None,
            "selected_command": None,
            "command_execution_result_type": None,
            "command_execution_result_scope": None,
            "declared_non_claims": {},
        }
        return _finalize_result(declared_fallback, checks, empty_basis, empty_basis)
    if not _is_mapping(declared):
        return resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
            declared
        )
    return resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
        declared
    )


def build_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact deterministic summary for the resolver result."""

    execution_result = _mapping_at(
        result,
        "local_relevance_medium_read_only_local_carrier_command_execution_result",
    )
    checks = result.get(
        "local_relevance_medium_read_only_local_carrier_command_execution_result_checks",
        [],
    )
    checks_list = checks if isinstance(checks, list) else []
    passed_check_count, failed_check_count = _check_counts(checks_list)
    block = result.get("block") if _is_mapping(result.get("block")) else {}
    non_claims = result.get("non_claims")
    if not _is_mapping(non_claims):
        non_claims = {}

    def false_summary(field: str) -> bool:
        return execution_result.get(field) is False and non_claims.get(field) is False

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("reason"),
        "command_execution_result_id": execution_result.get(
            "command_execution_result_id"
        ),
        "question": _mapping_at(
            result,
            "declared_local_relevance_medium_read_only_local_carrier_command_execution_result_question",
        ).get("question"),
        "intent": _mapping_at(
            result,
            "declared_local_relevance_medium_read_only_local_carrier_command_execution_result_question",
        ).get("intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "command_execution_result_recorded": result.get("outcome") == OUTCOME_RECORDED,
        "local_relevance_medium_read_only_local_carrier_command_execution_result_recorded": result.get(
            "outcome"
        )
        == OUTCOME_RECORDED,
        "basis_command_execution_result_boundary_artifact_preserved": execution_result.get(
            "basis_command_execution_result_boundary_outcome"
        )
        == COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED_OUTCOME
        and execution_result.get("basis_command_execution_result_boundary_result_version")
        == RESULT_VERSION
        and execution_result.get(
            "basis_command_execution_result_boundary_failed_check_count"
        )
        == 0
        and result.get("outcome") == OUTCOME_RECORDED,
        "basis_command_execution_artifact_preserved": execution_result.get(
            "basis_command_execution_outcome"
        )
        == COMMAND_EXECUTION_RECORDED_OUTCOME
        and execution_result.get("basis_command_execution_result_version")
        == RESULT_VERSION
        and execution_result.get("basis_command_execution_failed_check_count") == 0
        and result.get("outcome") == OUTCOME_RECORDED,
        "selected_command": execution_result.get("selected_command"),
        "selected_command_preserved": execution_result.get("selected_command")
        == SELECTED_COMMAND
        and result.get("outcome") == OUTCOME_RECORDED,
        "selected_command_is_state": execution_result.get("selected_command_is_state")
        is True,
        "selected_command_execution_recorded": execution_result.get(
            "selected_command_execution_recorded"
        )
        is True,
        "command_execution_performed": execution_result.get("command_execution_performed")
        is True,
        "command_execution_local_only": execution_result.get(
            "command_execution_local_only"
        )
        is True,
        "command_execution_read_only": execution_result.get("command_execution_read_only")
        is True,
        "command_execution_result_created": execution_result.get(
            "command_execution_result_created"
        )
        is True,
        "command_execution_result_local_only": execution_result.get(
            "command_execution_result_local_only"
        )
        is True,
        "command_execution_result_read_only": execution_result.get(
            "command_execution_result_read_only"
        )
        is True,
        "command_execution_result_object_summary": {
            "command_execution_result_type": execution_result.get(
                "command_execution_result_type"
            ),
            "command_execution_result_scope": execution_result.get(
                "command_execution_result_scope"
            ),
            "basis_command_execution_result_boundary_outcome": execution_result.get(
                "basis_command_execution_result_boundary_outcome"
            ),
            "basis_command_execution_outcome": execution_result.get(
                "basis_command_execution_outcome"
            ),
            "basis_command_execution_result_boundary_failed_check_count": execution_result.get(
                "basis_command_execution_result_boundary_failed_check_count"
            ),
            "basis_command_execution_failed_check_count": execution_result.get(
                "basis_command_execution_failed_check_count"
            ),
        },
        "state_payload_not_returned": false_summary("state_payload_returned"),
        "state_result_object_not_created": false_summary(
            "state_result_object_created"
        ),
        "state_packet_body_not_exposed": false_summary("state_packet_body_exposed"),
        "lookup_not_performed": false_summary("lookup_performed"),
        "lookup_command_not_executed": false_summary("lookup_command_executed"),
        "operation_permission_not_created": false_summary("operation_permission_created"),
        "runtime_permission_not_created": false_summary("runtime_permission_created"),
        "public_api_not_created": false_summary("public_api_created"),
        "participant_facing_interface_not_created": false_summary(
            "participant_facing_interface_created"
        ),
        "distributed_network_behavior_not_created": false_summary(
            "distributed_network_behavior_created"
        ),
        "general_lookup_permission_not_created": false_summary(
            "general_lookup_permission_created"
        ),
        "arbitrary_lookup_permission_not_created": false_summary(
            "arbitrary_lookup_permission_created"
        ),
        "unsupported_commands_not_permitted": false_summary(
            "unsupported_commands_permitted"
        ),
        "unsupported_lookup_keys_not_permitted": false_summary(
            "unsupported_lookup_keys_permitted"
        ),
        "no_new_lookup_result_or_entry_created": false_summary(
            "new_lookup_result_created"
        )
        and false_summary("new_lookup_entry_created"),
        "no_new_signal_entry_relevance_object_or_index_entry_created": false_summary(
            "new_signal_accepted"
        )
        and false_summary("new_entry_accepted")
        and false_summary("new_relevance_object_created")
        and false_summary("new_index_entry_created"),
        "filesystem_discovery_not_performed": false_summary(
            "filesystem_discovery_performed"
        ),
        "registry_search_query_surface_or_ranking_not_created": false_summary(
            "registry_created"
        )
        and false_summary("search_surface_created")
        and false_summary("query_surface_created")
        and false_summary("ranking_surface_created"),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": false_summary(
            "scoring_surface_created"
        )
        and false_summary("priority_surface_created")
        and false_summary("validity_judgment_created")
        and false_summary("truth_judgment_created")
        and false_summary("authority_judgment_created")
        and false_summary("currentness_judgment_created"),
        "repeated_reception_arbitrary_reception_or_feed_not_created": false_summary(
            "repeated_reception_permission_created"
        )
        and false_summary("arbitrary_reception_created")
        and false_summary("feed_created"),
        "source_authority_currentness_truth_synchronization_participation_participant_role_not_created": false_summary(
            "source_transfer_occurred"
        )
        and false_summary("source_receipt_occurred")
        and false_summary("authority_created")
        and false_summary("currentness_created")
        and false_summary("truth_created")
        and false_summary("synchronization_created")
        and false_summary("participation_authorized")
        and false_summary("participant_role_created"),
        "follow_on_not_created": false_summary("follow_on_work_authorized"),
        "key_non_claims": {key: non_claims.get(key) for key in REQUIRED_FALSE_NON_CLAIMS},
        "predecessor_failure_evidence_preserved": non_claims.get(
            "predecessor_failure_repaired"
        )
        is False
        and non_claims.get("predecessor_failure_hidden") is False
        and non_claims.get("predecessor_failure_claimed_passed") is False,
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _is_forbidden_output_path(path: Path) -> bool:
    try:
        normalized = path.resolve()
    except OSError:
        normalized = path.absolute()
    for root in FORBIDDEN_OUTPUT_ROOTS:
        try:
            root_resolved = root.resolve()
        except OSError:
            root_resolved = root.absolute()
        if normalized == root_resolved or root_resolved in normalized.parents:
            return True
    return False


def _next_available_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter:03d}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def write_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result JSON artifact without silently overwriting."""

    execution_result = _mapping_at(
        result,
        "local_relevance_medium_read_only_local_carrier_command_execution_result",
    )
    result_id = execution_result.get(
        "command_execution_result_id", DEFAULT_COMMAND_EXECUTION_RESULT_ID
    )
    filename = (
        f"{result_id}__local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_result.json"
    )
    if output_path is None:
        path = OUTPUT_ROOT / filename
    else:
        candidate = Path(output_path)
        path = candidate if candidate.suffix == ".json" else candidate / filename
    if _is_forbidden_output_path(path):
        raise LocalRelevanceMediumReadOnlyLocalCarrierCommandExecutionResultV0MinError(
            f"refusing to write command execution result into forbidden root: {path}"
        )
    path = _next_available_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return path


def build_declared_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_request(
    *,
    local_relevance_medium_read_only_local_carrier_command_execution_result_id: str = DEFAULT_COMMAND_EXECUTION_RESULT_ID,
    selected_command_execution_result_boundary_artifact: Path | str | None = None,
    selected_command_execution_artifact: Path | str | None = None,
    selected_command: str = SELECTED_COMMAND,
    command_execution_result_type: str = COMMAND_EXECUTION_RESULT_TYPE,
    command_execution_result_scope: str = COMMAND_EXECUTION_RESULT_SCOPE,
    intent: str = INTENT_RECORD,
    question: str = CORE_QUESTION,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared request for the selected-state command execution result."""

    if selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyLocalCarrierCommandExecutionResultV0MinError(
            "selected command must be exactly state"
        )
    non_claims = _canonical_non_claims()
    if declared_non_claims is not None:
        non_claims.update(dict(declared_non_claims))
    request: dict[str, Any] = {
        "local_relevance_medium_read_only_local_carrier_command_execution_result_id": (
            local_relevance_medium_read_only_local_carrier_command_execution_result_id
        ),
        "local_relevance_medium_read_only_local_carrier_command_execution_result_question": question,
        "local_relevance_medium_read_only_local_carrier_command_execution_result_intent": intent,
        "selected_command_execution_result_boundary_artifact": str(
            selected_command_execution_result_boundary_artifact
            or DEFAULT_COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT
        ),
        "selected_command_execution_artifact": str(
            selected_command_execution_artifact or DEFAULT_COMMAND_EXECUTION_ARTIFACT
        ),
        "selected_command": selected_command,
        "command_execution_result_type": command_execution_result_type,
        "command_execution_result_scope": command_execution_result_scope,
        "selected_command_execution_recorded": True,
        "command_execution_performed": True,
        "command_execution_local_only": True,
        "command_execution_read_only": True,
        "local_carrier_command_execution_result_recorded": True,
        "command_execution_result_created": True,
        "command_execution_result_local_only": True,
        "command_execution_result_read_only": True,
        "declared_non_claims": non_claims,
    }
    for key in REQUIRED_FALSE_NON_CLAIMS:
        request[key] = False
    request.update(overrides)
    return request
