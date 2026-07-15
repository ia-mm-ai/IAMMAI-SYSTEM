"""Resolve one local read-only selected-state payload return.

This resolver records one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN
object. It reads one clean state payload return boundary artifact as
payload-return-consideration basis and one clean selected-state command
execution result artifact as result basis.

The object is state-payload-return-shaped, local, read-only,
selected-state-only, non-result-object, non-packet-body-exposure, and
non-operation-shaped. It records ``state_payload_returned`` only in the narrow
sense that one bounded local read-only payload return event exists. It does not
create a state result object, expose state packet body or raw/full state packet
body, perform lookup, execute lookup commands, create permissions, create
public or distributed surfaces, discover files, accept new entries or signals,
create registry/search/query/ranking surfaces, or authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyStatePayloadReturnV0MinError(RuntimeError):
    """Raised for bounded path/write errors in this resolver."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_state_payload_return_v0_min"
)

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_RECORDED"
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_payload_return_v0_min"
)
DEFAULT_STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_payload_return_boundary_v0_min/"
    "local_relevance_medium_read_only_state_payload_return_boundary_"
    "reference_review_001__local_relevance_medium_read_only_state_payload_"
    "return_boundary_v0_min_result.json"
)
DEFAULT_COMMAND_EXECUTION_RESULT_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_execution_result_v0_min/"
    "local_relevance_medium_read_only_local_carrier_command_execution_result_"
    "reference_review_001__local_relevance_medium_read_only_local_carrier_"
    "command_execution_result_v0_min_result.json"
)

DEFAULT_STATE_PAYLOAD_RETURN_ID = (
    "local_relevance_medium_read_only_state_payload_return_001"
)
STATE_PAYLOAD_RETURN_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN"
STATE_PAYLOAD_RETURN_SCOPE = "SELECTED_STATE_PAYLOAD_RETURN_ONLY"
SELECTED_COMMAND = "state"

STATE_PAYLOAD_RETURN_BOUNDARY_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY_RECORDED"
)
STATE_PAYLOAD_RETURN_BOUNDARY_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY"
)
STATE_PAYLOAD_RETURN_BOUNDARY_SCOPE = (
    "SELECTED_STATE_PAYLOAD_RETURN_CONSIDERATION_ONLY"
)
COMMAND_EXECUTION_RESULT_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_RECORDED"
)
COMMAND_EXECUTION_RESULT_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT"
)
COMMAND_EXECUTION_RESULT_SCOPE = "SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY"

SUPPORTED_STATE_PAYLOAD_RETURN_TYPE_VALUES = (STATE_PAYLOAD_RETURN_TYPE,)
SUPPORTED_STATE_PAYLOAD_RETURN_SCOPE_VALUES = (STATE_PAYLOAD_RETURN_SCOPE,)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY "
    "for selected command state, and one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT, "
    "may one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN be recorded "
    "for the selected-state command execution result, without creating state "
    "result object, exposing raw/full state packet body, performing lookup, "
    "executing lookup command, creating operation permission, creating runtime "
    "permission, creating public API, creating participant-facing interface, "
    "creating distributed network behavior, creating general lookup permission, "
    "creating arbitrary lookup permission, permitting unsupported commands, "
    "permitting unsupported lookup keys, creating new lookup result, creating "
    "new lookup entry, accepting new entries, accepting new signals, performing "
    "filesystem discovery, creating query surface, registry, search, ranking, "
    "scoring, priority, validity judgment, truth judgment, authority, "
    "currentness, synchronization, participation authorization, participant "
    "role, repeated reception permission, arbitrary reception, feed, source "
    "transfer, source receipt, or follow-on work?"
)

STATE_PAYLOAD_RETURN_OBJECT_FALSE_FIELDS = (
    "state_result_object_created",
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

REQUIRED_FALSE_NON_CLAIMS = (
    "state_result_object_created",
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
    "artifact_existence_treated_as_state_payload_return_authority",
    "latest_file_posture_treated_as_state_payload_return_authority",
    "repo_local_availability_treated_as_state_payload_return_authority",
    "hidden_repo_state_used_as_state_payload_return_content",
    "hidden_repo_state_used_as_state_payload_return_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_state_payload_return_recorded",
    "basis_state_payload_return_boundary_artifact_preserved",
    "basis_command_execution_result_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_state_command_execution_result_recorded",
    "command_execution_result_created",
    "command_execution_result_local_only",
    "command_execution_result_read_only",
    "state_payload_returned",
    "state_payload_return_local_only",
    "state_payload_return_read_only",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BLOCK_REQUESTED",
    "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_PATH_MISSING",
    "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_UNREADABLE",
    "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "COMMAND_EXECUTION_RESULT_ARTIFACT_PATH_MISSING",
    "COMMAND_EXECUTION_RESULT_ARTIFACT_UNREADABLE",
    "COMMAND_EXECUTION_RESULT_ARTIFACT_NOT_JSON_OBJECT",
    "COMMAND_EXECUTION_RESULT_ARTIFACT_NOT_RECORDED",
    "COMMAND_EXECUTION_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
    "COMMAND_EXECUTION_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_STATE_COMMAND_EXECUTION_RESULT_NOT_RECORDED",
    "COMMAND_EXECUTION_RESULT_NOT_CREATED",
    "COMMAND_EXECUTION_RESULT_LOCAL_ONLY_NOT_TRUE",
    "COMMAND_EXECUTION_RESULT_READ_ONLY_NOT_TRUE",
    "STATE_PAYLOAD_RETURN_TYPE_MISSING",
    "STATE_PAYLOAD_RETURN_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN",
    "STATE_PAYLOAD_RETURN_SCOPE_MISSING",
    "STATE_PAYLOAD_RETURN_SCOPE_NOT_SELECTED_STATE_PAYLOAD_RETURN_ONLY",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_NOT_RECORDED",
    "STATE_PAYLOAD_NOT_RETURNED",
    "STATE_PAYLOAD_RETURN_LOCAL_ONLY_NOT_TRUE",
    "STATE_PAYLOAD_RETURN_READ_ONLY_NOT_TRUE",
    "STATE_RESULT_OBJECT_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_STATE_PAYLOAD_RETURN_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_STATE_PAYLOAD_RETURN_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_STATE_PAYLOAD_RETURN_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_STATE_PAYLOAD_RETURN_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_STATE_PAYLOAD_RETURN_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PRIOR_ARTIFACTS_MUTATED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_REQUEST_UNREADABLE",
)

FALSE_FIELD_BLOCK_CODES = {
    "state_result_object_created": "STATE_RESULT_OBJECT_CREATED",
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
    "derivative_reception_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "vessel_relation_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "adoption_created": "FOLLOW_ON_WORK_AUTHORIZED",
    "receiving_context_governance_created": "FOLLOW_ON_WORK_AUTHORIZED",
    "publication_flow_created": "FOLLOW_ON_WORK_AUTHORIZED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "artifact_existence_treated_as_state_payload_return_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_STATE_PAYLOAD_RETURN_AUTHORITY"
    ),
    "latest_file_posture_treated_as_state_payload_return_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_STATE_PAYLOAD_RETURN_AUTHORITY"
    ),
    "repo_local_availability_treated_as_state_payload_return_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_STATE_PAYLOAD_RETURN_AUTHORITY"
    ),
    "hidden_repo_state_used_as_state_payload_return_content": (
        "HIDDEN_REPO_STATE_USED_AS_STATE_PAYLOAD_RETURN_CONTENT"
    ),
    "hidden_repo_state_used_as_state_payload_return_authority": (
        "HIDDEN_REPO_STATE_USED_AS_STATE_PAYLOAD_RETURN_AUTHORITY"
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
    "local_relevance_medium_read_only_state_payload_return_recorded": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_NOT_RECORDED"
    ),
    "state_payload_returned": "STATE_PAYLOAD_NOT_RETURNED",
    "state_payload_return_local_only": "STATE_PAYLOAD_RETURN_LOCAL_ONLY_NOT_TRUE",
    "state_payload_return_read_only": "STATE_PAYLOAD_RETURN_READ_ONLY_NOT_TRUE",
}

SHORTCUT_FAILURES = {
    "state_payload_return_boundary_artifact_missing": (
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_PATH_MISSING"
    ),
    "state_payload_return_boundary_artifact_not_recorded": (
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_RECORDED"
    ),
    "state_payload_return_boundary_artifact_failed_checks_present": (
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "state_payload_return_boundary_artifact_version_not_0_1_0": (
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "command_execution_result_artifact_missing": (
        "COMMAND_EXECUTION_RESULT_ARTIFACT_PATH_MISSING"
    ),
    "command_execution_result_artifact_not_recorded": (
        "COMMAND_EXECUTION_RESULT_ARTIFACT_NOT_RECORDED"
    ),
    "command_execution_result_artifact_failed_checks_present": (
        "COMMAND_EXECUTION_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "command_execution_result_artifact_version_not_0_1_0": (
        "COMMAND_EXECUTION_RESULT_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "selected_command_missing": "SELECTED_COMMAND_MISSING",
    "selected_command_not_state": "SELECTED_COMMAND_NOT_STATE",
    "selected_state_command_execution_result_not_recorded": (
        "SELECTED_STATE_COMMAND_EXECUTION_RESULT_NOT_RECORDED"
    ),
    "command_execution_result_not_created": "COMMAND_EXECUTION_RESULT_NOT_CREATED",
    "command_execution_result_local_only_not_true": (
        "COMMAND_EXECUTION_RESULT_LOCAL_ONLY_NOT_TRUE"
    ),
    "command_execution_result_read_only_not_true": (
        "COMMAND_EXECUTION_RESULT_READ_ONLY_NOT_TRUE"
    ),
    "state_payload_return_type_not_local_relevance_medium_read_only_state_payload_return": (
        "STATE_PAYLOAD_RETURN_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN"
    ),
    "state_payload_return_scope_not_selected_state_payload_return_only": (
        "STATE_PAYLOAD_RETURN_SCOPE_NOT_SELECTED_STATE_PAYLOAD_RETURN_ONLY"
    ),
    "local_relevance_medium_read_only_state_payload_return_not_recorded": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_NOT_RECORDED"
    ),
    "state_payload_not_returned": "STATE_PAYLOAD_NOT_RETURNED",
    "state_payload_return_local_only_not_true": (
        "STATE_PAYLOAD_RETURN_LOCAL_ONLY_NOT_TRUE"
    ),
    "state_payload_return_read_only_not_true": (
        "STATE_PAYLOAD_RETURN_READ_ONLY_NOT_TRUE"
    ),
    **FALSE_FIELD_BLOCK_CODES,
}

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_state_payload_return_body",
    "raw_state_payload_body",
    "raw_state_result_body",
    "raw_state_packet_body",
    "raw_full_state_packet_body",
    "raw_state_payload_return_boundary_body",
    "raw_command_execution_result_body",
    "raw_lookup_result_body",
    "raw_lookup_performed_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "state_payload_return_body",
    "state_payload_body",
    "state_result_body",
    "state_packet_body",
    "full_state_packet_body",
    "command_execution_result_body",
    "state_payload_return_boundary_body",
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

RAW_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_RETURN_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_RETURN_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BODY_MUST_NOT_RETURN",
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

OFFICIAL_STRINGS = {
    RESULT_VERSION,
    RESOLVER_MODULE,
    DEFAULT_STATE_PAYLOAD_RETURN_ID,
    STATE_PAYLOAD_RETURN_TYPE,
    STATE_PAYLOAD_RETURN_SCOPE,
    STATE_PAYLOAD_RETURN_BOUNDARY_RECORDED_OUTCOME,
    STATE_PAYLOAD_RETURN_BOUNDARY_TYPE,
    STATE_PAYLOAD_RETURN_BOUNDARY_SCOPE,
    COMMAND_EXECUTION_RESULT_RECORDED_OUTCOME,
    COMMAND_EXECUTION_RESULT_TYPE,
    COMMAND_EXECUTION_RESULT_SCOPE,
    SELECTED_COMMAND,
    CORE_QUESTION,
    *OUTCOME_FAMILY,
    *SUPPORTED_INTENTS,
    *SUPPORTED_STATE_PAYLOAD_RETURN_TYPE_VALUES,
    *SUPPORTED_STATE_PAYLOAD_RETURN_SCOPE_VALUES,
    *REQUIRED_FALSE_NON_CLAIMS,
    *ALLOWED_TRUE_RECORDED_FIELDS,
    *BLOCK_CODES,
}

FORBIDDEN_OUTPUT_ROOTS = (
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "state_payload_return_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "local_carrier_command_execution_result_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "local_carrier_command_execution_result_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "local_carrier_command_execution_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "local_carrier_command_execution_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "local_carrier_command_surface_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "local_carrier_command_surface_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "reusable_lookup_permission_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "reusable_lookup_permission_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "lookup_pair_coverage_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "second_orientation_lookup_result_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "orientation_lookup_result_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "orientation_index_system_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "state_reader_v0_min"
    ),
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
    return isinstance(value, dict)


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
    public_code = (
        code
        if code in BLOCK_CODES
        else "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_REQUEST_MALFORMED"
    )
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
    }
    if not passed:
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
        metadata.get("local_relevance_medium_read_only_state_payload_return_boundary_version"),
        metadata.get(
            "local_relevance_medium_read_only_local_carrier_command_execution_result_version"
        ),
        object_mapping.get("state_payload_return_version"),
        object_mapping.get("boundary_version"),
        object_mapping.get("command_execution_result_version"),
        object_mapping.get("result_version"),
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


def _truth_from_mappings(
    mappings: tuple[Mapping[str, Any], ...],
    keys: tuple[str, ...],
) -> bool:
    for mapping in mappings:
        for key in keys:
            if mapping.get(key) is True:
                return True
    return False


def _append_declared_request_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    question = declared.get("local_relevance_medium_read_only_state_payload_return_question")
    _check(
        checks,
        "state payload return question declared",
        isinstance(question, str) and bool(question.strip()),
        "declared non-empty question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_QUESTION_UNDECLARED",
    )

    intent = declared.get("local_relevance_medium_read_only_state_payload_return_intent")
    _check(
        checks,
        "state payload return intent supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _check(
            checks,
            "explicit block intent not requested",
            False,
            "no explicit block request",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BLOCK_REQUESTED",
        )

    state_payload_return_type = declared.get("state_payload_return_type")
    _check(
        checks,
        "state payload return type declared",
        state_payload_return_type is not None,
        STATE_PAYLOAD_RETURN_TYPE,
        state_payload_return_type,
        "STATE_PAYLOAD_RETURN_TYPE_MISSING",
    )
    _check(
        checks,
        "state payload return type exact",
        state_payload_return_type == STATE_PAYLOAD_RETURN_TYPE,
        STATE_PAYLOAD_RETURN_TYPE,
        state_payload_return_type,
        "STATE_PAYLOAD_RETURN_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN",
    )

    state_payload_return_scope = declared.get("state_payload_return_scope")
    _check(
        checks,
        "state payload return scope declared",
        state_payload_return_scope is not None,
        STATE_PAYLOAD_RETURN_SCOPE,
        state_payload_return_scope,
        "STATE_PAYLOAD_RETURN_SCOPE_MISSING",
    )
    _check(
        checks,
        "state payload return scope exact",
        state_payload_return_scope == STATE_PAYLOAD_RETURN_SCOPE,
        STATE_PAYLOAD_RETURN_SCOPE,
        state_payload_return_scope,
        "STATE_PAYLOAD_RETURN_SCOPE_NOT_SELECTED_STATE_PAYLOAD_RETURN_ONLY",
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
    _check(
        checks,
        "selected command is state",
        selected_command == SELECTED_COMMAND,
        "selected command is state",
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )


def _append_shortcut_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    for shortcut, code in SHORTCUT_FAILURES.items():
        _check(
            checks,
            f"shortcut {shortcut} not asserted",
            declared.get(shortcut) is not True,
            False,
            declared.get(shortcut, False),
            code,
        )


def _append_declared_non_claim_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    non_claims = declared.get("declared_non_claims")
    _check(
        checks,
        "declared non-claims mapping present",
        _is_mapping(non_claims),
        "mapping with every required non-claim false",
        type(non_claims).__name__,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    if not _is_mapping(non_claims):
        return
    for key in REQUIRED_FALSE_NON_CLAIMS:
        _check(
            checks,
            f"declared non-claim {key} false",
            non_claims.get(key) is False,
            False,
            non_claims.get(key),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _append_false_posture_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    for field, code in FALSE_FIELD_BLOCK_CODES.items():
        actual = declared.get(field, False)
        _check(
            checks,
            f"{field} false",
            actual is False,
            False,
            actual,
            code,
        )


def _append_declared_true_posture_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> None:
    for field, code in TRUE_FIELD_BLOCK_CODES.items():
        actual = declared.get(field, True)
        _check(
            checks,
            f"{field} true when declared",
            actual is True,
            True,
            actual,
            code,
        )


def _validate_state_payload_return_boundary_artifact(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    path_value = declared.get("selected_state_payload_return_boundary_artifact")
    path_declared = isinstance(path_value, (str, Path)) and bool(str(path_value))
    _check(
        checks,
        "state payload return boundary artifact path declared",
        path_declared,
        "declared state payload return boundary artifact path",
        path_value,
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_PATH_MISSING",
    )

    basis: dict[str, Any] = {
        "artifact": path_value if path_declared else None,
        "outcome": None,
        "result_version": None,
        "failed_check_count": None,
        "selected_command": None,
        "selected_command_is_state": None,
        "future_state_payload_return_may_be_considered": None,
    }
    if not path_declared:
        return basis, {}

    artifact, error = _read_json_artifact(
        path_value,
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_UNREADABLE",
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    )
    _check(
        checks,
        "state payload return boundary artifact readable JSON",
        error is None or error == "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
        "readable JSON",
        error or "readable JSON",
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_UNREADABLE",
    )
    _check(
        checks,
        "state payload return boundary artifact JSON object",
        error is None,
        "JSON object",
        error or "JSON object",
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    )
    if error is not None or artifact is None:
        return basis, {}

    metadata_key = "local_relevance_medium_read_only_state_payload_return_boundary_metadata"
    summary_key = "local_relevance_medium_read_only_state_payload_return_boundary_summary"
    checks_key = "local_relevance_medium_read_only_state_payload_return_boundary_checks"
    object_key = "local_relevance_medium_read_only_state_payload_return_boundary"
    boundary = _mapping_at(artifact, object_key)
    statement = _mapping_at(
        artifact,
        "local_relevance_medium_read_only_state_payload_return_boundary_statement",
    )
    summary = _summary_mapping(artifact, summary_key)

    outcome = _artifact_outcome(artifact, metadata_key, summary_key)
    result_version = _artifact_result_version(
        artifact,
        metadata_key,
        summary_key,
        boundary,
    )
    failed_check_count = _artifact_failed_check_count(
        artifact,
        metadata_key,
        summary_key,
        checks_key,
    )
    selected_command = boundary.get("selected_command")
    selected_command_is_state = boundary.get("selected_command_is_state") is True
    future_may_be_considered = _truth_from_mappings(
        (boundary, statement, summary),
        ("future_state_payload_return_may_be_considered",),
    )

    basis.update(
        {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "selected_command": selected_command,
            "selected_command_is_state": selected_command_is_state,
            "future_state_payload_return_may_be_considered": future_may_be_considered,
        }
    )

    _check(
        checks,
        "state payload return boundary artifact outcome recorded",
        outcome == STATE_PAYLOAD_RETURN_BOUNDARY_RECORDED_OUTCOME,
        STATE_PAYLOAD_RETURN_BOUNDARY_RECORDED_OUTCOME,
        outcome,
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "state payload return boundary artifact result version 0.1.0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version,
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "state payload return boundary artifact failed check count zero",
        failed_check_count == 0,
        0,
        failed_check_count,
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "state payload return boundary type exact in artifact",
        boundary.get("boundary_type") == STATE_PAYLOAD_RETURN_BOUNDARY_TYPE,
        STATE_PAYLOAD_RETURN_BOUNDARY_TYPE,
        boundary.get("boundary_type"),
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "state payload return boundary scope exact in artifact",
        boundary.get("boundary_scope") == STATE_PAYLOAD_RETURN_BOUNDARY_SCOPE,
        STATE_PAYLOAD_RETURN_BOUNDARY_SCOPE,
        boundary.get("boundary_scope"),
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "selected command preserved by state payload return boundary artifact",
        selected_command == SELECTED_COMMAND,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected command is state in state payload return boundary artifact",
        selected_command_is_state,
        True,
        selected_command_is_state,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "future state payload return considered by boundary artifact",
        future_may_be_considered,
        True,
        future_may_be_considered,
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    if "state_payload_returned" in boundary:
        _check(
            checks,
            "state payload not already returned by boundary artifact",
            boundary.get("state_payload_returned") is False,
            False,
            boundary.get("state_payload_returned"),
            "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_RECORDED",
        )
    for field in STATE_PAYLOAD_RETURN_OBJECT_FALSE_FIELDS:
        if field in boundary:
            _check(
                checks,
                f"{field} false in state payload return boundary artifact",
                boundary.get(field) is False,
                False,
                boundary.get(field),
                FALSE_FIELD_BLOCK_CODES.get(field, "FOLLOW_ON_WORK_AUTHORIZED"),
            )
    return basis, boundary


def _validate_command_execution_result_artifact(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    path_value = declared.get("selected_command_execution_result_artifact")
    path_declared = isinstance(path_value, (str, Path)) and bool(str(path_value))
    _check(
        checks,
        "command execution result artifact path declared",
        path_declared,
        "declared command execution result artifact path",
        path_value,
        "COMMAND_EXECUTION_RESULT_ARTIFACT_PATH_MISSING",
    )

    basis: dict[str, Any] = {
        "artifact": path_value if path_declared else None,
        "outcome": None,
        "result_version": None,
        "failed_check_count": None,
        "selected_command": None,
        "selected_command_is_state": None,
        "selected_state_command_execution_result_recorded": None,
        "command_execution_result_created": None,
        "command_execution_result_local_only": None,
        "command_execution_result_read_only": None,
    }
    if not path_declared:
        return basis, {}

    artifact, error = _read_json_artifact(
        path_value,
        "COMMAND_EXECUTION_RESULT_ARTIFACT_UNREADABLE",
        "COMMAND_EXECUTION_RESULT_ARTIFACT_NOT_JSON_OBJECT",
    )
    _check(
        checks,
        "command execution result artifact readable JSON",
        error is None or error == "COMMAND_EXECUTION_RESULT_ARTIFACT_NOT_JSON_OBJECT",
        "readable JSON",
        error or "readable JSON",
        "COMMAND_EXECUTION_RESULT_ARTIFACT_UNREADABLE",
    )
    _check(
        checks,
        "command execution result artifact JSON object",
        error is None,
        "JSON object",
        error or "JSON object",
        "COMMAND_EXECUTION_RESULT_ARTIFACT_NOT_JSON_OBJECT",
    )
    if error is not None or artifact is None:
        return basis, {}

    metadata_key = (
        "local_relevance_medium_read_only_local_carrier_command_execution_result_metadata"
    )
    summary_key = (
        "local_relevance_medium_read_only_local_carrier_command_execution_result_summary"
    )
    checks_key = (
        "local_relevance_medium_read_only_local_carrier_command_execution_result_checks"
    )
    object_key = "local_relevance_medium_read_only_local_carrier_command_execution_result"
    result_object = _mapping_at(artifact, object_key)
    statement = _mapping_at(
        artifact,
        "local_relevance_medium_read_only_local_carrier_command_execution_result_statement",
    )
    summary = _summary_mapping(artifact, summary_key)

    outcome = _artifact_outcome(artifact, metadata_key, summary_key)
    result_version = _artifact_result_version(
        artifact,
        metadata_key,
        summary_key,
        result_object,
    )
    failed_check_count = _artifact_failed_check_count(
        artifact,
        metadata_key,
        summary_key,
        checks_key,
    )
    selected_command = result_object.get("selected_command")
    selected_command_is_state = result_object.get("selected_command_is_state") is True
    selected_result_recorded = _truth_from_mappings(
        (result_object, statement, summary),
        (
            "selected_state_command_execution_result_recorded",
            "local_carrier_command_execution_result_recorded",
            "local_relevance_medium_read_only_local_carrier_command_execution_result_recorded",
            "command_execution_result_recorded",
        ),
    )
    command_execution_result_created = _truth_from_mappings(
        (result_object, statement, summary),
        ("command_execution_result_created",),
    )
    command_execution_result_local_only = _truth_from_mappings(
        (result_object, statement, summary),
        ("command_execution_result_local_only",),
    )
    command_execution_result_read_only = _truth_from_mappings(
        (result_object, statement, summary),
        ("command_execution_result_read_only",),
    )

    basis.update(
        {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "selected_command": selected_command,
            "selected_command_is_state": selected_command_is_state,
            "selected_state_command_execution_result_recorded": selected_result_recorded,
            "command_execution_result_created": command_execution_result_created,
            "command_execution_result_local_only": command_execution_result_local_only,
            "command_execution_result_read_only": command_execution_result_read_only,
        }
    )

    _check(
        checks,
        "command execution result artifact outcome recorded",
        outcome == COMMAND_EXECUTION_RESULT_RECORDED_OUTCOME,
        COMMAND_EXECUTION_RESULT_RECORDED_OUTCOME,
        outcome,
        "COMMAND_EXECUTION_RESULT_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "command execution result artifact result version 0.1.0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version,
        "COMMAND_EXECUTION_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "command execution result artifact failed check count zero",
        failed_check_count == 0,
        0,
        failed_check_count,
        "COMMAND_EXECUTION_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "selected command exactly state in command execution result artifact",
        selected_command == SELECTED_COMMAND,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected command is state in command execution result artifact",
        selected_command_is_state,
        True,
        selected_command_is_state,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected-state command execution result recorded",
        selected_result_recorded,
        True,
        selected_result_recorded,
        "SELECTED_STATE_COMMAND_EXECUTION_RESULT_NOT_RECORDED",
    )
    _check(
        checks,
        "command execution result created",
        command_execution_result_created,
        True,
        command_execution_result_created,
        "COMMAND_EXECUTION_RESULT_NOT_CREATED",
    )
    _check(
        checks,
        "command execution result local only",
        command_execution_result_local_only,
        True,
        command_execution_result_local_only,
        "COMMAND_EXECUTION_RESULT_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "command execution result read only",
        command_execution_result_read_only,
        True,
        command_execution_result_read_only,
        "COMMAND_EXECUTION_RESULT_READ_ONLY_NOT_TRUE",
    )
    if "state_payload_returned" in result_object:
        _check(
            checks,
            "state payload not already returned by command execution result artifact",
            result_object.get("state_payload_returned") is False,
            False,
            result_object.get("state_payload_returned"),
            "COMMAND_EXECUTION_RESULT_ARTIFACT_NOT_RECORDED",
        )
    for field in STATE_PAYLOAD_RETURN_OBJECT_FALSE_FIELDS:
        if field in result_object:
            _check(
                checks,
                f"{field} false in command execution result artifact",
                result_object.get(field) is False,
                False,
                result_object.get(field),
                FALSE_FIELD_BLOCK_CODES.get(field, "FOLLOW_ON_WORK_AUTHORIZED"),
            )
    return basis, result_object


def _append_state_payload_return_membrane_checks(
    checks: list[dict[str, Any]],
    declared: Mapping[str, Any],
    boundary_basis: Mapping[str, Any],
    command_execution_result_basis: Mapping[str, Any],
) -> None:
    _append_shortcut_checks(checks, declared)
    _append_declared_true_posture_checks(checks, declared)

    _check(
        checks,
        "state payload return boundary may be considered",
        boundary_basis.get("future_state_payload_return_may_be_considered") is True,
        True,
        boundary_basis.get("future_state_payload_return_may_be_considered"),
        "STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    for field, code in (
        (
            "selected_state_command_execution_result_recorded",
            "SELECTED_STATE_COMMAND_EXECUTION_RESULT_NOT_RECORDED",
        ),
        ("command_execution_result_created", "COMMAND_EXECUTION_RESULT_NOT_CREATED"),
        (
            "command_execution_result_local_only",
            "COMMAND_EXECUTION_RESULT_LOCAL_ONLY_NOT_TRUE",
        ),
        (
            "command_execution_result_read_only",
            "COMMAND_EXECUTION_RESULT_READ_ONLY_NOT_TRUE",
        ),
    ):
        _check(
            checks,
            field.replace("_", " "),
            command_execution_result_basis.get(field) is True,
            True,
            command_execution_result_basis.get(field),
            code,
        )

    _append_false_posture_checks(checks, declared)
    _append_declared_non_claim_checks(checks, declared)
    _check(
        checks,
        "artifact existence not state payload return authority",
        declared.get("artifact_existence_treated_as_state_payload_return_authority")
        is not True,
        False,
        declared.get("artifact_existence_treated_as_state_payload_return_authority"),
        "ARTIFACT_EXISTENCE_TREATED_AS_STATE_PAYLOAD_RETURN_AUTHORITY",
    )
    _check(
        checks,
        "latest file posture not state payload return authority",
        declared.get("latest_file_posture_treated_as_state_payload_return_authority")
        is not True,
        False,
        declared.get("latest_file_posture_treated_as_state_payload_return_authority"),
        "LATEST_FILE_POSTURE_TREATED_AS_STATE_PAYLOAD_RETURN_AUTHORITY",
    )
    _check(
        checks,
        "repo local availability not state payload return authority",
        declared.get("repo_local_availability_treated_as_state_payload_return_authority")
        is not True,
        False,
        declared.get("repo_local_availability_treated_as_state_payload_return_authority"),
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_STATE_PAYLOAD_RETURN_AUTHORITY",
    )
    _check(
        checks,
        "hidden repo state not state payload return content",
        declared.get("hidden_repo_state_used_as_state_payload_return_content") is not True,
        False,
        declared.get("hidden_repo_state_used_as_state_payload_return_content"),
        "HIDDEN_REPO_STATE_USED_AS_STATE_PAYLOAD_RETURN_CONTENT",
    )
    _check(
        checks,
        "hidden repo state not state payload return authority",
        declared.get("hidden_repo_state_used_as_state_payload_return_authority")
        is not True,
        False,
        declared.get("hidden_repo_state_used_as_state_payload_return_authority"),
        "HIDDEN_REPO_STATE_USED_AS_STATE_PAYLOAD_RETURN_AUTHORITY",
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
    _check(
        checks,
        "result-level required false non-claims canonical false",
        all(_canonical_non_claims().get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS),
        "all emitted result-level non-claims false",
        "all emitted result-level non-claims false",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _check(
        checks,
        "required non-claims false",
        all(_canonical_non_claims().get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS),
        "required non-claims false",
        "required non-claims false",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _build_state_payload_return_object(
    declared: Mapping[str, Any],
    boundary_basis: Mapping[str, Any],
    command_execution_result_basis: Mapping[str, Any],
    recorded: bool,
) -> dict[str, Any]:
    selected_command = declared.get("selected_command")
    if not isinstance(selected_command, str):
        selected_command = ""
    payload_return = {
        "state_payload_return_id": str(
            declared.get(
                "local_relevance_medium_read_only_state_payload_return_id",
                DEFAULT_STATE_PAYLOAD_RETURN_ID,
            )
        ),
        "state_payload_return_type": STATE_PAYLOAD_RETURN_TYPE,
        "state_payload_return_version": RESULT_VERSION,
        "state_payload_return_scope": STATE_PAYLOAD_RETURN_SCOPE,
        "basis_state_payload_return_boundary_artifact": _sanitize(
            boundary_basis.get("artifact")
        ),
        "basis_state_payload_return_boundary_outcome": boundary_basis.get("outcome"),
        "basis_state_payload_return_boundary_result_version": boundary_basis.get(
            "result_version"
        ),
        "basis_state_payload_return_boundary_failed_check_count": boundary_basis.get(
            "failed_check_count"
        ),
        "basis_command_execution_result_artifact": _sanitize(
            command_execution_result_basis.get("artifact")
        ),
        "basis_command_execution_result_outcome": command_execution_result_basis.get(
            "outcome"
        ),
        "basis_command_execution_result_result_version": command_execution_result_basis.get(
            "result_version"
        ),
        "basis_command_execution_result_failed_check_count": (
            command_execution_result_basis.get("failed_check_count")
        ),
        "selected_command": selected_command,
        "selected_command_is_state": recorded and selected_command == SELECTED_COMMAND,
        "selected_state_command_execution_result_recorded": recorded,
        "command_execution_result_created": recorded,
        "command_execution_result_local_only": recorded,
        "command_execution_result_read_only": recorded,
        "local_relevance_medium_read_only_state_payload_return_recorded": recorded,
        "state_payload_returned": recorded,
        "state_payload_return_local_only": recorded,
        "state_payload_return_read_only": recorded,
    }
    for field in STATE_PAYLOAD_RETURN_OBJECT_FALSE_FIELDS:
        payload_return[field] = False
    return payload_return


def _build_statement(
    outcome: str,
    payload_return: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    boundary_preserved = (
        recorded
        and payload_return.get("basis_state_payload_return_boundary_outcome")
        == STATE_PAYLOAD_RETURN_BOUNDARY_RECORDED_OUTCOME
        and payload_return.get("basis_state_payload_return_boundary_result_version")
        == RESULT_VERSION
        and payload_return.get("basis_state_payload_return_boundary_failed_check_count")
        == 0
    )
    command_execution_result_preserved = (
        recorded
        and payload_return.get("basis_command_execution_result_outcome")
        == COMMAND_EXECUTION_RESULT_RECORDED_OUTCOME
        and payload_return.get("basis_command_execution_result_result_version")
        == RESULT_VERSION
        and payload_return.get("basis_command_execution_result_failed_check_count") == 0
    )
    return {
        "local_relevance_medium_read_only_state_payload_return_recorded": recorded,
        "basis_state_payload_return_boundary_artifact_preserved": boundary_preserved,
        "basis_command_execution_result_artifact_preserved": (
            command_execution_result_preserved
        ),
        "selected_command_preserved": recorded
        and payload_return.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": payload_return.get("selected_command_is_state")
        is True,
        "selected_state_command_execution_result_recorded": payload_return.get(
            "selected_state_command_execution_result_recorded"
        )
        is True,
        "command_execution_result_created": payload_return.get(
            "command_execution_result_created"
        )
        is True,
        "command_execution_result_local_only": payload_return.get(
            "command_execution_result_local_only"
        )
        is True,
        "command_execution_result_read_only": payload_return.get(
            "command_execution_result_read_only"
        )
        is True,
        "state_payload_returned": payload_return.get("state_payload_returned") is True,
        "state_payload_return_local_only": payload_return.get(
            "state_payload_return_local_only"
        )
        is True,
        "state_payload_return_read_only": payload_return.get(
            "state_payload_return_read_only"
        )
        is True,
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _build_non_meaning(non_claims: Mapping[str, bool]) -> dict[str, Any]:
    return {
        "state_payload_return_is_not_state_result_object": True,
        "state_payload_return_exposes_no_state_packet_body": True,
        "state_payload_return_exposes_no_raw_full_state_packet_body": True,
        "state_payload_return_performs_no_lookup": True,
        "state_payload_return_executes_no_lookup_command": True,
        "state_payload_return_creates_no_operation_permission": True,
        "state_payload_return_creates_no_runtime_permission": True,
        "state_payload_return_creates_no_public_api": True,
        "state_payload_return_creates_no_participant_facing_interface": True,
        "state_payload_return_creates_no_distributed_network_behavior": True,
        "state_payload_return_creates_no_general_lookup_permission": True,
        "state_payload_return_creates_no_arbitrary_lookup_permission": True,
        "state_payload_return_creates_no_registry_search_query_or_ranking": True,
        "state_payload_return_authorizes_no_follow_on_work": True,
        "result_level_non_claims": dict(non_claims),
    }


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium read-only state payload return test",
        "local relevance medium read-only state payload return live artifact",
        "local relevance medium read-only state payload return terminal summary, if needed",
        "state result object",
        "state packet body exposure",
        "raw/full state packet body exposure",
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
        "requested_local_relevance_medium_read_only_state_payload_return_outcome"
    )
    if requested in OUTCOME_FAMILY:
        return requested
    intent = declared.get("local_relevance_medium_read_only_state_payload_return_intent")
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
        "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_REQUEST_MALFORMED"
    )
    reason = declared.get("block_reason")
    if not isinstance(reason, str) or not reason.strip():
        reason = "local relevance medium read-only state payload return blocked"
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": _sanitize(reason),
    }


def _empty_basis() -> dict[str, Any]:
    return {
        "artifact": None,
        "outcome": None,
        "result_version": None,
        "failed_check_count": None,
        "selected_command": None,
        "selected_command_is_state": None,
        "selected_state_command_execution_result_recorded": None,
        "command_execution_result_created": None,
        "command_execution_result_local_only": None,
        "command_execution_result_read_only": None,
        "future_state_payload_return_may_be_considered": None,
    }


def _fallback_declared_request() -> dict[str, Any]:
    return {
        "local_relevance_medium_read_only_state_payload_return_id": (
            DEFAULT_STATE_PAYLOAD_RETURN_ID
        ),
        "local_relevance_medium_read_only_state_payload_return_question": None,
        "local_relevance_medium_read_only_state_payload_return_intent": None,
        "selected_state_payload_return_boundary_artifact": None,
        "selected_command_execution_result_artifact": None,
        "selected_command": None,
        "state_payload_return_type": None,
        "state_payload_return_scope": None,
        "declared_non_claims": {},
    }


def _finalize_result(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
    boundary_basis: Mapping[str, Any],
    command_execution_result_basis: Mapping[str, Any],
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    outcome = _determine_outcome(declared, checks)
    recorded = outcome == OUTCOME_RECORDED
    payload_return = _build_state_payload_return_object(
        declared,
        boundary_basis,
        command_execution_result_basis,
        recorded,
    )
    statement = _build_statement(outcome, payload_return, non_claims)
    passed_check_count, failed_check_count = _check_counts(checks)

    metadata = {
        "local_relevance_medium_read_only_state_payload_return_id": payload_return[
            "state_payload_return_id"
        ],
        "local_relevance_medium_read_only_state_payload_return_type": (
            STATE_PAYLOAD_RETURN_TYPE
        ),
        "local_relevance_medium_read_only_state_payload_return_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
    }
    declared_question = {
        "question": _sanitize(
            declared.get("local_relevance_medium_read_only_state_payload_return_question")
        ),
        "intent": _sanitize(
            declared.get("local_relevance_medium_read_only_state_payload_return_intent")
        ),
        "selected_state_payload_return_boundary_artifact": _sanitize(
            declared.get("selected_state_payload_return_boundary_artifact")
        ),
        "selected_command_execution_result_artifact": _sanitize(
            declared.get("selected_command_execution_result_artifact")
        ),
        "selected_command": _sanitize(declared.get("selected_command")),
        "state_payload_return_type": _sanitize(
            declared.get("state_payload_return_type")
        ),
        "state_payload_return_scope": _sanitize(
            declared.get("state_payload_return_scope")
        ),
    }
    boundary_artifact_basis = {
        "selected_state_payload_return_boundary_artifact": _sanitize(
            boundary_basis.get("artifact")
        ),
        "basis_state_payload_return_boundary_outcome": boundary_basis.get("outcome"),
        "basis_state_payload_return_boundary_result_version": boundary_basis.get(
            "result_version"
        ),
        "basis_state_payload_return_boundary_failed_check_count": boundary_basis.get(
            "failed_check_count"
        ),
        "basis_role": "state payload return boundary as payload-return-consideration basis only",
    }
    command_execution_result_artifact_basis = {
        "selected_command_execution_result_artifact": _sanitize(
            command_execution_result_basis.get("artifact")
        ),
        "basis_command_execution_result_outcome": command_execution_result_basis.get(
            "outcome"
        ),
        "basis_command_execution_result_result_version": (
            command_execution_result_basis.get("result_version")
        ),
        "basis_command_execution_result_failed_check_count": (
            command_execution_result_basis.get("failed_check_count")
        ),
        "basis_role": "selected-state command execution result basis only",
    }
    additional_basis_required = []
    if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        additional_basis_required.append(
            _sanitize(
                declared.get("additional_basis_context")
                or "additional state payload return basis required"
            )
        )
    not_recorded_basis = []
    if outcome == OUTCOME_NOT_RECORDED:
        not_recorded_basis.append(
            _sanitize(
                declared.get("not_recorded_basis")
                or "state payload return not recorded"
            )
        )

    result: dict[str, Any] = {
        "local_relevance_medium_read_only_state_payload_return_metadata": metadata,
        "declared_local_relevance_medium_read_only_state_payload_return_question": (
            declared_question
        ),
        "selected_state_payload_return_boundary_artifact_basis": boundary_artifact_basis,
        "selected_command_execution_result_artifact_basis": (
            command_execution_result_artifact_basis
        ),
        "local_relevance_medium_read_only_state_payload_return": payload_return,
        "local_relevance_medium_read_only_state_payload_return_checks": checks,
        "local_relevance_medium_read_only_state_payload_return_statement": statement,
        "local_relevance_medium_read_only_state_payload_return_non_meaning": (
            _build_non_meaning(non_claims)
        ),
        "additional_basis_required": additional_basis_required,
        "not_recorded_basis": not_recorded_basis,
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": _build_block(outcome, checks, declared),
    }
    result[
        "local_relevance_medium_read_only_state_payload_return_summary"
    ] = build_local_relevance_medium_read_only_state_payload_return_v0_min_summary(
        result
    )
    return _sanitize(result)


def resolve_local_relevance_medium_read_only_state_payload_return_v0_min(
    declared_local_relevance_medium_read_only_state_payload_return: Mapping[str, Any]
    | None = None,
) -> dict[str, Any]:
    """Resolve one local read-only selected-state payload return request."""

    if declared_local_relevance_medium_read_only_state_payload_return is None:
        declared = (
            build_declared_local_relevance_medium_read_only_state_payload_return_v0_min_request()
        )
    elif not _is_mapping(declared_local_relevance_medium_read_only_state_payload_return):
        checks: list[dict[str, Any]] = []
        _check(
            checks,
            "declared request mapping",
            False,
            "mapping",
            type(declared_local_relevance_medium_read_only_state_payload_return).__name__,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_REQUEST_MALFORMED",
        )
        return _finalize_result(
            _fallback_declared_request(),
            checks,
            _empty_basis(),
            _empty_basis(),
        )
    else:
        declared = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_state_payload_return)
        )

    checks: list[dict[str, Any]] = []
    _append_declared_request_checks(checks, declared)
    _append_selected_command_checks(checks, declared)
    boundary_basis, _boundary = _validate_state_payload_return_boundary_artifact(
        checks,
        declared,
    )
    command_execution_result_basis, _command_execution_result = (
        _validate_command_execution_result_artifact(checks, declared)
    )
    _append_state_payload_return_membrane_checks(
        checks,
        declared,
        boundary_basis,
        command_execution_result_basis,
    )
    return _finalize_result(declared, checks, boundary_basis, command_execution_result_basis)


def resolve_local_relevance_medium_read_only_state_payload_return_v0_min_from_path(
    declared_local_relevance_medium_read_only_state_payload_return_path: Path | str,
) -> dict[str, Any]:
    """Read a declared request JSON file and resolve it."""

    try:
        path = Path(declared_local_relevance_medium_read_only_state_payload_return_path)
        with path.open("r", encoding="utf-8") as handle:
            declared = json.load(handle)
    except (OSError, TypeError, json.JSONDecodeError):
        checks: list[dict[str, Any]] = []
        _check(
            checks,
            "declared request path readable JSON",
            False,
            "readable request JSON object",
            str(declared_local_relevance_medium_read_only_state_payload_return_path),
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_REQUEST_UNREADABLE",
        )
        return _finalize_result(
            _fallback_declared_request(),
            checks,
            _empty_basis(),
            _empty_basis(),
        )
    return resolve_local_relevance_medium_read_only_state_payload_return_v0_min(declared)


def build_local_relevance_medium_read_only_state_payload_return_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact deterministic summary for the resolver result."""

    payload_return = _mapping_at(
        result,
        "local_relevance_medium_read_only_state_payload_return",
    )
    checks = result.get(
        "local_relevance_medium_read_only_state_payload_return_checks",
        [],
    )
    checks_list = checks if isinstance(checks, list) else []
    passed_check_count, failed_check_count = _check_counts(checks_list)
    block = result.get("block") if _is_mapping(result.get("block")) else {}
    non_claims = result.get("non_claims")
    if not _is_mapping(non_claims):
        non_claims = {}

    def false_summary(field: str) -> bool:
        object_ok = (
            payload_return.get(field) is False
            if field in STATE_PAYLOAD_RETURN_OBJECT_FALSE_FIELDS
            else True
        )
        return object_ok and non_claims.get(field) is False

    boundary_preserved = (
        payload_return.get("basis_state_payload_return_boundary_outcome")
        == STATE_PAYLOAD_RETURN_BOUNDARY_RECORDED_OUTCOME
        and payload_return.get("basis_state_payload_return_boundary_result_version")
        == RESULT_VERSION
        and payload_return.get("basis_state_payload_return_boundary_failed_check_count")
        == 0
        and result.get("outcome") == OUTCOME_RECORDED
    )
    command_execution_result_preserved = (
        payload_return.get("basis_command_execution_result_outcome")
        == COMMAND_EXECUTION_RESULT_RECORDED_OUTCOME
        and payload_return.get("basis_command_execution_result_result_version")
        == RESULT_VERSION
        and payload_return.get("basis_command_execution_result_failed_check_count") == 0
        and result.get("outcome") == OUTCOME_RECORDED
    )
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("reason"),
        "state_payload_return_id": payload_return.get("state_payload_return_id"),
        "question": _mapping_at(
            result,
            "declared_local_relevance_medium_read_only_state_payload_return_question",
        ).get("question"),
        "intent": _mapping_at(
            result,
            "declared_local_relevance_medium_read_only_state_payload_return_question",
        ).get("intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "state_payload_return_recorded": result.get("outcome") == OUTCOME_RECORDED,
        "local_relevance_medium_read_only_state_payload_return_recorded": result.get(
            "outcome"
        )
        == OUTCOME_RECORDED,
        "basis_state_payload_return_boundary_artifact_preserved": boundary_preserved,
        "basis_command_execution_result_artifact_preserved": (
            command_execution_result_preserved
        ),
        "selected_command": payload_return.get("selected_command"),
        "selected_command_preserved": payload_return.get("selected_command")
        == SELECTED_COMMAND
        and result.get("outcome") == OUTCOME_RECORDED,
        "selected_command_is_state": payload_return.get("selected_command_is_state")
        is True,
        "selected_state_command_execution_result_recorded": payload_return.get(
            "selected_state_command_execution_result_recorded"
        )
        is True,
        "command_execution_result_created": payload_return.get(
            "command_execution_result_created"
        )
        is True,
        "command_execution_result_local_only": payload_return.get(
            "command_execution_result_local_only"
        )
        is True,
        "command_execution_result_read_only": payload_return.get(
            "command_execution_result_read_only"
        )
        is True,
        "state_payload_returned": payload_return.get("state_payload_returned") is True,
        "state_payload_return_local_only": payload_return.get(
            "state_payload_return_local_only"
        )
        is True,
        "state_payload_return_read_only": payload_return.get(
            "state_payload_return_read_only"
        )
        is True,
        "state_payload_return_object_summary": {
            "state_payload_return_type": payload_return.get("state_payload_return_type"),
            "state_payload_return_scope": payload_return.get("state_payload_return_scope"),
            "basis_state_payload_return_boundary_outcome": payload_return.get(
                "basis_state_payload_return_boundary_outcome"
            ),
            "basis_command_execution_result_outcome": payload_return.get(
                "basis_command_execution_result_outcome"
            ),
        },
        "state_result_object_not_created": false_summary("state_result_object_created"),
        "state_packet_body_not_exposed": false_summary("state_packet_body_exposed"),
        "raw_full_state_packet_body_not_exposed": false_summary(
            "raw_full_state_packet_body_exposed"
        ),
        "lookup_not_performed": false_summary("lookup_performed"),
        "lookup_command_not_executed": false_summary("lookup_command_executed"),
        "operation_permission_not_created": false_summary(
            "operation_permission_created"
        ),
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
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": (
            false_summary("scoring_surface_created")
            and false_summary("priority_surface_created")
            and false_summary("validity_judgment_created")
            and false_summary("truth_judgment_created")
            and false_summary("authority_judgment_created")
            and false_summary("currentness_judgment_created")
        ),
        "repeated_reception_arbitrary_reception_or_feed_not_created": false_summary(
            "repeated_reception_permission_created"
        )
        and false_summary("arbitrary_reception_created")
        and false_summary("feed_created"),
        "source_authority_currentness_truth_synchronization_participation_participant_role_not_created": (
            false_summary("source_created")
            and false_summary("authority_created")
            and false_summary("currentness_created")
            and false_summary("truth_created")
            and false_summary("synchronization_created")
            and false_summary("participation_authorized")
            and false_summary("participant_role_created")
        ),
        "follow_on_not_created": false_summary("follow_on_work_authorized"),
        "key_non_claims": {
            key: non_claims.get(key) for key in REQUIRED_FALSE_NON_CLAIMS
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


def _path_has_component_prefix(candidate: Path, root: Path) -> bool:
    candidate_parts = candidate.parts
    root_parts = root.parts
    if not root_parts or len(root_parts) > len(candidate_parts):
        return False
    return any(
        candidate_parts[index : index + len(root_parts)] == root_parts
        for index in range(0, len(candidate_parts) - len(root_parts) + 1)
    )


def _guard_output_path(candidate: Path) -> None:
    for forbidden_root in FORBIDDEN_OUTPUT_ROOTS:
        if candidate == forbidden_root or _path_has_component_prefix(
            candidate,
            forbidden_root,
        ):
            raise LocalRelevanceMediumReadOnlyStatePayloadReturnV0MinError(
                f"refusing to write state payload return result under {forbidden_root}"
            )


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


def write_local_relevance_medium_read_only_state_payload_return_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result as deterministic JSON without overwriting."""

    payload_return = _mapping_at(
        result,
        "local_relevance_medium_read_only_state_payload_return",
    )
    payload_return_id = payload_return.get(
        "state_payload_return_id",
        DEFAULT_STATE_PAYLOAD_RETURN_ID,
    )
    filename = f"{payload_return_id}__local_relevance_medium_read_only_state_payload_return_v0_min_result.json"
    if output_path is None:
        target = OUTPUT_ROOT / filename
    else:
        requested = Path(output_path)
        target = requested if requested.suffix else requested / filename
    _guard_output_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _next_available_path(target)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def build_declared_local_relevance_medium_read_only_state_payload_return_v0_min_request(
    *,
    local_relevance_medium_read_only_state_payload_return_id: str = DEFAULT_STATE_PAYLOAD_RETURN_ID,
    selected_state_payload_return_boundary_artifact: Path | str = DEFAULT_STATE_PAYLOAD_RETURN_BOUNDARY_ARTIFACT,
    selected_command_execution_result_artifact: Path | str = DEFAULT_COMMAND_EXECUTION_RESULT_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    state_payload_return_type: str = STATE_PAYLOAD_RETURN_TYPE,
    state_payload_return_scope: str = STATE_PAYLOAD_RETURN_SCOPE,
    intent: str = INTENT_RECORD,
) -> dict[str, Any]:
    """Build a valid declared request with required non-claims set to false."""

    if selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyStatePayloadReturnV0MinError(
            "selected command must be exactly state"
        )
    return {
        "local_relevance_medium_read_only_state_payload_return_id": (
            local_relevance_medium_read_only_state_payload_return_id
        ),
        "local_relevance_medium_read_only_state_payload_return_question": CORE_QUESTION,
        "local_relevance_medium_read_only_state_payload_return_intent": intent,
        "selected_state_payload_return_boundary_artifact": str(
            selected_state_payload_return_boundary_artifact
        ),
        "selected_command_execution_result_artifact": str(
            selected_command_execution_result_artifact
        ),
        "selected_command": selected_command,
        "state_payload_return_type": state_payload_return_type,
        "state_payload_return_scope": state_payload_return_scope,
        "local_relevance_medium_read_only_state_payload_return_recorded": True,
        "state_payload_returned": True,
        "state_payload_return_local_only": True,
        "state_payload_return_read_only": True,
        "declared_non_claims": _canonical_non_claims(),
    }
