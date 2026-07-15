"""Resolve one local relevance medium read-only local carrier command execution boundary.

This resolver reads one selected
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE artifact as
command-availability basis. It records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY object
only.

The boundary is local, read-only, single-command, and non-execution-shaped. It
may record that one future local read-only command execution may be considered
for exactly one selected command from the closed command set: ``state``,
``lookup first_orientation_locator``, or
``lookup second_orientation_locator``. It does not execute commands, create
command execution, create command execution result, return state, perform
lookup, create operation permission, runtime permission, API,
participant-facing interface, distributed behavior, general lookup permission,
arbitrary lookup permission, unsupported-command permission, unsupported-key
permission, new lookup result, new lookup entry, registry, search, query
surface, ranking, scoring, priority, validity judgment, truth judgment,
authority judgment, currentness judgment, repeated reception permission,
arbitrary reception, feed, source transfer, source receipt, action,
synchronization, participation, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyLocalCarrierCommandExecutionBoundaryV0MinError(
    Exception
):
    """Bounded error for local carrier command execution boundary handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min"
)

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_BLOCKED"
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
    "local_carrier_command_execution_boundary_v0_min"
)
DEFAULT_LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_surface_v0_min/"
    "local_relevance_medium_read_only_local_carrier_command_surface_reference_review_001__"
    "local_relevance_medium_read_only_local_carrier_command_surface_v0_min_result.json"
)

DEFAULT_BOUNDARY_ID = (
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_001"
)

BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY"
BOUNDARY_SCOPE = "SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_CONSIDERATION_ONLY"
SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)

LOCAL_CARRIER_COMMAND_SURFACE_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_RECORDED"
)
COMMAND_SURFACE_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE"
COMMAND_SURFACE_SCOPE = "LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY"

ALLOWED_COMMANDS = (
    "state",
    "lookup first_orientation_locator",
    "lookup second_orientation_locator",
)
DEFAULT_SELECTED_COMMAND = "state"

INTENT_RECORD = (
    "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE, "
    "may one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY "
    "be recorded that permits a future single local read-only command execution to be "
    "considered for one selected command from the closed command set, state, lookup "
    "first_orientation_locator, or lookup second_orientation_locator, without executing "
    "the command, creating command execution, creating command execution result, "
    "creating operation permission, creating runtime permission, creating public API, "
    "creating participant-facing interface, creating distributed network behavior, "
    "creating general lookup permission, creating arbitrary lookup permission, "
    "permitting unsupported commands, permitting unsupported lookup keys, creating new "
    "lookup result, creating new lookup entry, returning state, performing lookup, "
    "accepting new entries, accepting new signals, performing filesystem discovery, "
    "creating query surface, registry, search, ranking, scoring, priority, validity "
    "judgment, truth judgment, authority, currentness, action, synchronization, "
    "participation authorization, participant role, repeated reception permission, "
    "arbitrary reception, feed, source transfer, source receipt, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "command_execution_performed",
    "command_execution_created",
    "command_execution_result_created",
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
    "state_returned",
    "lookup_performed",
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
    "action_created",
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
    "artifact_existence_treated_as_command_execution_boundary_authority",
    "latest_file_posture_treated_as_command_execution_boundary_authority",
    "repo_local_availability_treated_as_command_execution_boundary_authority",
    "hidden_repo_state_used_as_command_execution_boundary_content",
    "hidden_repo_state_used_as_command_execution_boundary_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

BOUNDARY_OBJECT_FALSE_FIELDS = (
    "command_execution_performed",
    "command_execution_created",
    "command_execution_result_created",
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
    "state_returned",
    "lookup_performed",
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
    "action_created",
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "follow_on_work_authorized",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_recorded",
    "basis_local_carrier_command_surface_artifact_preserved",
    "allowed_commands_preserved",
    "allowed_command_count_is_three",
    "selected_command_preserved",
    "selected_command_is_from_closed_command_set",
    "single_command_selected",
    "future_single_local_read_only_command_execution_may_be_considered",
    "local_carrier_command_surface_recorded",
    "command_surface_local_only",
    "command_surface_read_only",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_BLOCK_REQUESTED",
    "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_PATH_MISSING",
    "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_UNREADABLE",
    "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_NOT_JSON_OBJECT",
    "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_NOT_RECORDED",
    "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_VERSION_NOT_0_1_0",
    "ALLOWED_COMMANDS_NOT_EXACT",
    "ALLOWED_COMMAND_COUNT_NOT_THREE",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_IN_CLOSED_COMMAND_SET",
    "MORE_THAN_ONE_SELECTED_COMMAND_SUPPLIED",
    "FUTURE_SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_MAY_NOT_BE_CONSIDERED",
    "LOCAL_CARRIER_COMMAND_SURFACE_NOT_RECORDED",
    "COMMAND_SURFACE_LOCAL_ONLY_NOT_TRUE",
    "COMMAND_SURFACE_READ_ONLY_NOT_TRUE",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_CONSIDERATION_ONLY",
    "COMMAND_EXECUTION_PERFORMED",
    "COMMAND_EXECUTION_CREATED",
    "COMMAND_EXECUTION_RESULT_CREATED",
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
    "STATE_RETURNED",
    "LOOKUP_PERFORMED",
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
    "ACTION_CREATED",
    "SYNCHRONIZATION_CREATED",
    "PARTICIPATION_AUTHORIZED",
    "PARTICIPANT_ROLE_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_REQUEST_UNREADABLE",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_local_carrier_command_execution_boundary_body",
    "raw_local_carrier_command_execution_body",
    "raw_command_execution_body",
    "raw_command_execution_result_body",
    "raw_local_carrier_command_surface_body",
    "raw_state_return_body",
    "raw_lookup_result_body",
    "raw_lookup_performed_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "local_carrier_command_execution_boundary_body",
    "local_carrier_command_execution_body",
    "command_execution_body",
    "command_execution_result_body",
    "local_carrier_command_surface_body",
    "state_return_body",
    "lookup_result_body",
    "lookup_performed_body",
    "source_body",
    "authority_body",
    "currentness_body",
    "action_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_SURFACE_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RETURN_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

FALSE_FIELD_BLOCK_CODES = {
    "command_execution_performed": "COMMAND_EXECUTION_PERFORMED",
    "command_execution_created": "COMMAND_EXECUTION_CREATED",
    "command_execution_result_created": "COMMAND_EXECUTION_RESULT_CREATED",
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
    "state_returned": "STATE_RETURNED",
    "lookup_performed": "LOOKUP_PERFORMED",
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
    "action_created": "ACTION_CREATED",
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
    "artifact_existence_treated_as_command_execution_boundary_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY"
    ),
    "latest_file_posture_treated_as_command_execution_boundary_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY"
    ),
    "repo_local_availability_treated_as_command_execution_boundary_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY"
    ),
    "hidden_repo_state_used_as_command_execution_boundary_content": (
        "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_BOUNDARY_CONTENT"
    ),
    "hidden_repo_state_used_as_command_execution_boundary_authority": (
        "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY"
    ),
    "prior_artifacts_mutated": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
}

SHORTCUT_FAILURES = {
    "local_carrier_command_surface_artifact_missing": (
        "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_PATH_MISSING"
    ),
    "local_carrier_command_surface_artifact_not_recorded": (
        "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_NOT_RECORDED"
    ),
    "local_carrier_command_surface_artifact_failed_checks_present": (
        "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "local_carrier_command_surface_artifact_version_not_0_1_0": (
        "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "allowed_commands_not_exact": "ALLOWED_COMMANDS_NOT_EXACT",
    "allowed_command_count_not_three": "ALLOWED_COMMAND_COUNT_NOT_THREE",
    "selected_command_missing": "SELECTED_COMMAND_MISSING",
    "selected_command_not_in_closed_command_set": (
        "SELECTED_COMMAND_NOT_IN_CLOSED_COMMAND_SET"
    ),
    "more_than_one_selected_command_supplied": "MORE_THAN_ONE_SELECTED_COMMAND_SUPPLIED",
    "future_single_local_read_only_command_execution_may_not_be_considered": (
        "FUTURE_SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_MAY_NOT_BE_CONSIDERED"
    ),
    "local_carrier_command_surface_not_recorded": "LOCAL_CARRIER_COMMAND_SURFACE_NOT_RECORDED",
    "command_surface_local_only_not_true": "COMMAND_SURFACE_LOCAL_ONLY_NOT_TRUE",
    "command_surface_read_only_not_true": "COMMAND_SURFACE_READ_ONLY_NOT_TRUE",
    "boundary_type_not_local_relevance_medium_read_only_local_carrier_command_execution_boundary": (
        "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY"
    ),
    "boundary_scope_not_single_local_read_only_command_execution_consideration_only": (
        "BOUNDARY_SCOPE_NOT_SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_CONSIDERATION_ONLY"
    ),
}
SHORTCUT_FAILURES.update(FALSE_FIELD_BLOCK_CODES)

FORBIDDEN_OUTPUT_ROOTS = (
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
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_local_"
        "relevance_orientation_index_entry_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_"
        "orientation_view_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_"
        "relevance_receipt_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_"
        "relevance_reception_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_successor_"
        "candidate_admission_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_successor_"
        "reception_request_v0_min"
    ),
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

OFFICIAL_STRINGS = set(OUTCOME_FAMILY)
OFFICIAL_STRINGS.update(BLOCK_CODES)
OFFICIAL_STRINGS.update(SUPPORTED_INTENTS)
OFFICIAL_STRINGS.update(SUPPORTED_BOUNDARY_TYPE_VALUES)
OFFICIAL_STRINGS.update(SUPPORTED_BOUNDARY_SCOPE_VALUES)
OFFICIAL_STRINGS.update(ALLOWED_COMMANDS)
OFFICIAL_STRINGS.update(REQUIRED_FALSE_NON_CLAIMS)
OFFICIAL_STRINGS.update(ALLOWED_TRUE_RECORDED_FIELDS)
OFFICIAL_STRINGS.update(BOUNDARY_OBJECT_FALSE_FIELDS)
OFFICIAL_STRINGS.update(
    {
        RESULT_VERSION,
        RESOLVER_MODULE,
        DEFAULT_BOUNDARY_ID,
        BOUNDARY_TYPE,
        BOUNDARY_SCOPE,
        COMMAND_SURFACE_TYPE,
        COMMAND_SURFACE_SCOPE,
        LOCAL_CARRIER_COMMAND_SURFACE_RECORDED_OUTCOME,
    }
)


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _string_or_empty(value: Any) -> str:
    if isinstance(value, Path):
        return str(value)
    return value if isinstance(value, str) else ""


def _present(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _safe_int(value: Any) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _is_sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    key_lower = key.lower()
    return key_lower in SENSITIVE_CONTENT_KEYS or key_lower.endswith("_body")


def _sanitize(value: Any, parent_key: str | None = None) -> Any:
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if parent_key and _is_sensitive_key(parent_key):
            return "[REDACTED_RAW_CONTENT]"
        if any(sentinel in value for sentinel in RAW_SENTINELS):
            return "[REDACTED_RAW_CONTENT]"
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, MappingABC):
        if parent_key and _is_sensitive_key(parent_key):
            return "[REDACTED_RAW_CONTENT]"
        return {str(key): _sanitize(item, str(key)) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, parent_key) for item in value]
    return value


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> dict[str, Any]:
    check = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
    }
    if not passed and code:
        public_code = (
            code
            if code in BLOCK_CODES
            else "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED"
        )
        check["block_code"] = public_code
        check["failure_code"] = public_code
    return check


def _append_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    checks.append(_make_check(check_name, passed, expected_posture, actual_posture, code))


def _check_counts(checks: list[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is True:
            continue
        code = check.get("block_code") or check.get("failure_code")
        if isinstance(code, str) and code in BLOCK_CODES:
            return code
    return None


def _first_mapping_for_key_suffix(artifact: Mapping[str, Any], suffix: str) -> Mapping[str, Any]:
    for key, value in artifact.items():
        if isinstance(key, str) and key.endswith(suffix) and isinstance(value, MappingABC):
            return value
    return {}


def _metadata(artifact: Mapping[str, Any], preferred_key: str) -> Mapping[str, Any]:
    preferred = artifact.get(preferred_key)
    if isinstance(preferred, MappingABC):
        return preferred
    return _first_mapping_for_key_suffix(artifact, "_metadata")


def _summary_mapping(artifact: Mapping[str, Any], preferred_key: str) -> Mapping[str, Any]:
    preferred = artifact.get(preferred_key)
    if isinstance(preferred, MappingABC):
        return preferred
    return _first_mapping_for_key_suffix(artifact, "_summary")


def _artifact_outcome(
    artifact: Mapping[str, Any],
    metadata_key: str,
    summary_key: str,
) -> str | None:
    metadata = _metadata(artifact, metadata_key)
    summary = _summary_mapping(artifact, summary_key)
    for source in (artifact, metadata, summary):
        value = source.get("outcome")
        if isinstance(value, str):
            return value
    return None


def _artifact_result_version(
    artifact: Mapping[str, Any],
    metadata_key: str,
    summary_key: str,
    object_value: Mapping[str, Any] | None = None,
) -> str | None:
    metadata = _metadata(artifact, metadata_key)
    summary = _summary_mapping(artifact, summary_key)
    sources: list[Mapping[str, Any]] = [artifact, metadata, summary]
    if isinstance(object_value, MappingABC):
        sources.append(object_value)
    version_keys = (
        "result_version",
        "command_surface_version",
        "boundary_version",
        "version",
    )
    for source in sources:
        for key in version_keys:
            value = source.get(key)
            if isinstance(value, str):
                return value
    return None


def _artifact_failed_check_count(
    artifact: Mapping[str, Any],
    metadata_key: str,
    summary_key: str,
    checks_key: str,
) -> int | None:
    metadata = _metadata(artifact, metadata_key)
    summary = _summary_mapping(artifact, summary_key)
    for source in (artifact, metadata, summary):
        count = _safe_int(source.get("failed_check_count"))
        if count is not None:
            return count
    checks = artifact.get(checks_key)
    if isinstance(checks, list):
        return sum(
            1
            for check in checks
            if isinstance(check, MappingABC) and check.get("passed") is not True
        )
    return None


def _mapping_at(artifact: Mapping[str, Any] | None, key: str) -> Mapping[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {}
    value = artifact.get(key)
    return value if isinstance(value, MappingABC) else {}


def _basis(
    path_text: str,
    outcome: str | None = None,
    result_version: str | None = None,
    failed_check_count: int | None = None,
) -> dict[str, Any]:
    return {
        "artifact_path": path_text,
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "artifact_body_preserved": True,
        "raw_artifact_body_returned": False,
    }


def _read_json_artifact(
    path_value: Any,
    missing_code: str,
    unreadable_code: str,
    not_object_code: str,
) -> tuple[dict[str, Any] | None, str | None, str]:
    path_text = _string_or_empty(path_value)
    if not _present(path_text):
        return None, missing_code, ""
    path = Path(path_text)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception:
        return None, unreadable_code, path_text
    if not isinstance(loaded, MappingABC):
        return None, not_object_code, path_text
    return dict(loaded), None, path_text


def _selected_command_values(value: Any) -> tuple[str | None, bool, bool]:
    if isinstance(value, str):
        return value, _present(value), False
    if isinstance(value, (list, tuple, set)):
        values = list(value)
        if len(values) == 1 and isinstance(values[0], str):
            return values[0], _present(values[0]), False
        return None, len(values) > 0, len(values) != 1
    return None, value is not None, False


def _append_declared_request_checks(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    question = declared.get(
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_question"
    )
    intent = declared.get(
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_intent"
    )
    boundary_type = declared.get("boundary_type")
    boundary_scope = declared.get("boundary_scope")

    _append_check(
        checks,
        "local carrier command execution boundary question declared",
        _present(question),
        "declared local carrier command execution boundary question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_QUESTION_UNDECLARED",
    )
    _append_check(
        checks,
        "command execution boundary intent supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _append_check(
            checks,
            "local carrier command execution boundary block intent not requested",
            False,
            f"not {INTENT_BLOCK}",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_BLOCK_REQUESTED",
        )
    _append_check(
        checks,
        "boundary type declared",
        _present(boundary_type),
        BOUNDARY_TYPE,
        boundary_type,
        "BOUNDARY_TYPE_MISSING",
    )
    _append_check(
        checks,
        "boundary type exact",
        boundary_type == BOUNDARY_TYPE,
        BOUNDARY_TYPE,
        boundary_type,
        "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY",
    )
    _append_check(
        checks,
        "boundary scope declared",
        _present(boundary_scope),
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_MISSING",
    )
    _append_check(
        checks,
        "boundary scope single local read-only command execution consideration only",
        boundary_scope == BOUNDARY_SCOPE,
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_NOT_SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_CONSIDERATION_ONLY",
    )


def _append_shortcut_checks(declared: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for field_name, block_code in SHORTCUT_FAILURES.items():
        asserted = declared.get(field_name) is True
        _append_check(
            checks,
            f"shortcut {field_name} not asserted",
            not asserted,
            False,
            asserted,
            block_code,
        )


def _append_non_claim_checks(declared: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    declared_non_claims = declared.get("declared_non_claims")
    if not isinstance(declared_non_claims, MappingABC):
        _append_check(
            checks,
            "declared non-claims mapping present",
            False,
            "mapping with every required non-claim false",
            declared_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return
    for key in REQUIRED_FALSE_NON_CLAIMS:
        actual = declared_non_claims.get(key)
        _append_check(
            checks,
            f"required non-claim {key} declared false",
            actual is False,
            False,
            actual,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _append_false_posture_checks(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    for field_name, block_code in FALSE_FIELD_BLOCK_CODES.items():
        if field_name in declared:
            actual = declared.get(field_name)
            passed = actual is False
        else:
            actual = False
            passed = True
        _append_check(
            checks,
            f"{field_name} remains false",
            passed,
            False,
            actual,
            block_code,
        )


def _append_declared_command_surface_posture_checks(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    declared_allowed_commands = declared.get("allowed_commands", list(ALLOWED_COMMANDS))
    declared_allowed_command_count = declared.get(
        "allowed_command_count", len(ALLOWED_COMMANDS)
    )
    _append_check(
        checks,
        "declared allowed commands exact",
        declared_allowed_commands == list(ALLOWED_COMMANDS),
        list(ALLOWED_COMMANDS),
        declared_allowed_commands,
        "ALLOWED_COMMANDS_NOT_EXACT",
    )
    _append_check(
        checks,
        "declared allowed command count exactly three",
        declared_allowed_command_count == len(ALLOWED_COMMANDS),
        len(ALLOWED_COMMANDS),
        declared_allowed_command_count,
        "ALLOWED_COMMAND_COUNT_NOT_THREE",
    )
    _append_check(
        checks,
        "declared local carrier command surface recorded",
        declared.get("local_carrier_command_surface_recorded", True) is True,
        True,
        declared.get("local_carrier_command_surface_recorded", True),
        "LOCAL_CARRIER_COMMAND_SURFACE_NOT_RECORDED",
    )
    _append_check(
        checks,
        "declared command surface local only",
        declared.get("command_surface_local_only", True) is True,
        True,
        declared.get("command_surface_local_only", True),
        "COMMAND_SURFACE_LOCAL_ONLY_NOT_TRUE",
    )
    _append_check(
        checks,
        "declared command surface read only",
        declared.get("command_surface_read_only", True) is True,
        True,
        declared.get("command_surface_read_only", True),
        "COMMAND_SURFACE_READ_ONLY_NOT_TRUE",
    )


def _validate_local_carrier_command_surface_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, dict[str, Any], Mapping[str, Any]]:
    artifact_value = declared.get("selected_local_carrier_command_surface_artifact")
    path_text = _string_or_empty(artifact_value)
    _append_check(
        checks,
        "local carrier command surface artifact path declared",
        _present(path_text),
        "selected local carrier command surface artifact path",
        path_text,
        "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_PATH_MISSING",
    )
    artifact, read_code, path_text = _read_json_artifact(
        artifact_value,
        "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_PATH_MISSING",
        "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_UNREADABLE",
        "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_NOT_JSON_OBJECT",
    )
    if read_code:
        _append_check(
            checks,
            "local carrier command surface artifact readable JSON object",
            False,
            "readable JSON object",
            path_text or artifact_value,
            read_code,
        )
        return None, _basis(path_text), {}

    assert artifact is not None
    command_surface = _mapping_at(
        artifact, "local_relevance_medium_read_only_local_carrier_command_surface"
    )
    outcome = _artifact_outcome(
        artifact,
        "local_relevance_medium_read_only_local_carrier_command_surface_metadata",
        "local_relevance_medium_read_only_local_carrier_command_surface_summary",
    )
    result_version = _artifact_result_version(
        artifact,
        "local_relevance_medium_read_only_local_carrier_command_surface_metadata",
        "local_relevance_medium_read_only_local_carrier_command_surface_summary",
        command_surface,
    )
    failed_check_count = _artifact_failed_check_count(
        artifact,
        "local_relevance_medium_read_only_local_carrier_command_surface_metadata",
        "local_relevance_medium_read_only_local_carrier_command_surface_summary",
        "local_relevance_medium_read_only_local_carrier_command_surface_checks",
    )

    allowed_commands = command_surface.get("allowed_commands")
    allowed_command_count = command_surface.get("allowed_command_count")

    _append_check(
        checks,
        "local carrier command surface artifact readable JSON object",
        True,
        "readable JSON object",
        path_text,
    )
    _append_check(
        checks,
        "local carrier command surface artifact outcome recorded",
        outcome == LOCAL_CARRIER_COMMAND_SURFACE_RECORDED_OUTCOME,
        LOCAL_CARRIER_COMMAND_SURFACE_RECORDED_OUTCOME,
        outcome,
        "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "local carrier command surface artifact result version 0.1.0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version,
        "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "local carrier command surface artifact failed check count zero",
        failed_check_count == 0,
        0,
        failed_check_count,
        "LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _append_check(
        checks,
        "allowed commands exact",
        allowed_commands == list(ALLOWED_COMMANDS),
        list(ALLOWED_COMMANDS),
        allowed_commands,
        "ALLOWED_COMMANDS_NOT_EXACT",
    )
    _append_check(
        checks,
        "allowed command count exactly three",
        allowed_command_count == len(ALLOWED_COMMANDS),
        len(ALLOWED_COMMANDS),
        allowed_command_count,
        "ALLOWED_COMMAND_COUNT_NOT_THREE",
    )
    _append_check(
        checks,
        "local carrier command surface recorded",
        command_surface.get("local_carrier_command_surface_recorded") is True,
        True,
        command_surface.get("local_carrier_command_surface_recorded"),
        "LOCAL_CARRIER_COMMAND_SURFACE_NOT_RECORDED",
    )
    _append_check(
        checks,
        "command surface local only",
        command_surface.get("command_surface_local_only") is True,
        True,
        command_surface.get("command_surface_local_only"),
        "COMMAND_SURFACE_LOCAL_ONLY_NOT_TRUE",
    )
    _append_check(
        checks,
        "command surface read only",
        command_surface.get("command_surface_read_only") is True,
        True,
        command_surface.get("command_surface_read_only"),
        "COMMAND_SURFACE_READ_ONLY_NOT_TRUE",
    )
    return (
        artifact,
        _basis(path_text, outcome, result_version, failed_check_count),
        command_surface,
    )


def _append_selected_command_checks(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str | None, bool, bool]:
    selected_raw = declared.get("selected_command")
    selected_command, selected_declared, selected_multi = _selected_command_values(
        selected_raw
    )
    selected_commands_raw = declared.get("selected_commands")
    if isinstance(selected_commands_raw, (list, tuple, set)):
        selected_multi = selected_multi or len(selected_commands_raw) != 1
    elif selected_commands_raw is not None:
        selected_multi = True
    selected_multi = (
        selected_multi
        or declared.get("more_than_one_selected_command_supplied") is True
    )
    selected_in_closed_set = selected_command in ALLOWED_COMMANDS
    single_command_selected = (
        selected_declared and selected_in_closed_set and not selected_multi
    )
    future_may_be_considered = (
        declared.get(
            "future_single_local_read_only_command_execution_may_be_considered",
            True,
        )
        is True
    )

    _append_check(
        checks,
        "selected command declared",
        selected_declared,
        "one selected command from closed command set",
        selected_raw,
        "SELECTED_COMMAND_MISSING",
    )
    _append_check(
        checks,
        "selected command in closed command set",
        selected_in_closed_set,
        list(ALLOWED_COMMANDS),
        selected_command if selected_command is not None else selected_raw,
        "SELECTED_COMMAND_NOT_IN_CLOSED_COMMAND_SET",
    )
    _append_check(
        checks,
        "exactly one command selected",
        single_command_selected,
        "exactly one selected command",
        {
            "selected_command": selected_raw,
            "selected_commands": selected_commands_raw,
            "more_than_one_selected_command_supplied": selected_multi,
        },
        "MORE_THAN_ONE_SELECTED_COMMAND_SUPPLIED",
    )
    _append_check(
        checks,
        "future single local read-only command execution may be considered",
        future_may_be_considered,
        True,
        declared.get(
            "future_single_local_read_only_command_execution_may_be_considered",
            True,
        ),
        "FUTURE_SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_MAY_NOT_BE_CONSIDERED",
    )
    return selected_command, single_command_selected, future_may_be_considered


def _append_authority_exclusion_checks(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    _append_check(
        checks,
        "artifact existence not command-execution-boundary authority",
        declared.get("artifact_existence_treated_as_command_execution_boundary_authority", False)
        is False,
        False,
        declared.get(
            "artifact_existence_treated_as_command_execution_boundary_authority", False
        ),
        "ARTIFACT_EXISTENCE_TREATED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY",
    )
    _append_check(
        checks,
        "latest file posture not command-execution-boundary authority",
        declared.get("latest_file_posture_treated_as_command_execution_boundary_authority", False)
        is False,
        False,
        declared.get(
            "latest_file_posture_treated_as_command_execution_boundary_authority", False
        ),
        "LATEST_FILE_POSTURE_TREATED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY",
    )
    _append_check(
        checks,
        "repo-local availability not command-execution-boundary authority",
        declared.get("repo_local_availability_treated_as_command_execution_boundary_authority", False)
        is False,
        False,
        declared.get(
            "repo_local_availability_treated_as_command_execution_boundary_authority",
            False,
        ),
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY",
    )
    hidden_content_used = (
        declared.get("hidden_repo_state_used_as_command_execution_boundary_content", False)
        is True
    )
    hidden_authority_used = (
        declared.get("hidden_repo_state_used_as_command_execution_boundary_authority", False)
        is True
    )
    _append_check(
        checks,
        "hidden repo state not command-execution-boundary content or authority",
        not hidden_content_used and not hidden_authority_used,
        "hidden repo state excluded from command-execution-boundary content and authority",
        {
            "hidden_repo_state_used_as_command_execution_boundary_content": (
                hidden_content_used
            ),
            "hidden_repo_state_used_as_command_execution_boundary_authority": (
                hidden_authority_used
            ),
        },
        (
            "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_BOUNDARY_CONTENT"
            if hidden_content_used
            else "HIDDEN_REPO_STATE_USED_AS_COMMAND_EXECUTION_BOUNDARY_AUTHORITY"
        ),
    )
    predecessor_bad = (
        declared.get("predecessor_failure_repaired") is True
        or declared.get("predecessor_failure_hidden") is True
        or declared.get("predecessor_failure_claimed_passed") is True
    )
    _append_check(
        checks,
        "predecessor failure evidence preserved",
        not predecessor_bad,
        "predecessor failed-lineage evidence preserved",
        "predecessor failed-lineage evidence preserved"
        if not predecessor_bad
        else "predecessor failure evidence hidden or repaired",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _append_check(
        checks,
        "result-level required false non-claims canonical false",
        True,
        "all result-level required false non-claims canonical false",
        _canonical_non_claims(),
    )


def _build_boundary_object(
    declared: Mapping[str, Any],
    surface_basis: Mapping[str, Any],
    selected_command: str | None,
    single_command_selected: bool,
    future_may_be_considered: bool,
    command_surface: Mapping[str, Any],
    recorded: bool,
) -> dict[str, Any]:
    selected = selected_command if isinstance(selected_command, str) else ""
    boundary = {
        "boundary_id": _string_or_empty(
            declared.get(
                "local_relevance_medium_read_only_local_carrier_command_execution_boundary_id",
                DEFAULT_BOUNDARY_ID,
            )
        )
        or DEFAULT_BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "basis_local_carrier_command_surface_artifact": surface_basis.get(
            "artifact_path", ""
        ),
        "basis_local_carrier_command_surface_outcome": surface_basis.get("outcome"),
        "basis_local_carrier_command_surface_result_version": surface_basis.get(
            "result_version"
        ),
        "basis_local_carrier_command_surface_failed_check_count": surface_basis.get(
            "failed_check_count"
        ),
        "allowed_commands": list(ALLOWED_COMMANDS),
        "allowed_command_count": len(ALLOWED_COMMANDS),
        "selected_command": selected,
        "selected_command_is_from_closed_command_set": (
            recorded and selected in ALLOWED_COMMANDS
        ),
        "single_command_selected": recorded and single_command_selected,
        "future_single_local_read_only_command_execution_may_be_considered": (
            recorded and future_may_be_considered
        ),
        "local_carrier_command_surface_recorded": (
            recorded
            and command_surface.get("local_carrier_command_surface_recorded") is True
        ),
        "command_surface_local_only": (
            recorded and command_surface.get("command_surface_local_only") is True
        ),
        "command_surface_read_only": (
            recorded and command_surface.get("command_surface_read_only") is True
        ),
    }
    for field_name in BOUNDARY_OBJECT_FALSE_FIELDS:
        boundary[field_name] = False
    return boundary


def _build_statement(
    outcome: str,
    boundary: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_recorded": recorded,
        "basis_local_carrier_command_surface_artifact_preserved": recorded
        and boundary.get("basis_local_carrier_command_surface_outcome")
        == LOCAL_CARRIER_COMMAND_SURFACE_RECORDED_OUTCOME
        and boundary.get("basis_local_carrier_command_surface_result_version")
        == RESULT_VERSION
        and boundary.get("basis_local_carrier_command_surface_failed_check_count") == 0,
        "allowed_commands_preserved": recorded
        and boundary.get("allowed_commands") == list(ALLOWED_COMMANDS),
        "allowed_command_count_is_three": recorded
        and boundary.get("allowed_command_count") == len(ALLOWED_COMMANDS),
        "selected_command_preserved": recorded
        and boundary.get("selected_command") in ALLOWED_COMMANDS,
        "selected_command_is_from_closed_command_set": recorded
        and boundary.get("selected_command_is_from_closed_command_set") is True,
        "single_command_selected": recorded
        and boundary.get("single_command_selected") is True,
        "future_single_local_read_only_command_execution_may_be_considered": recorded
        and boundary.get(
            "future_single_local_read_only_command_execution_may_be_considered"
        )
        is True,
        "local_carrier_command_surface_recorded": recorded
        and boundary.get("local_carrier_command_surface_recorded") is True,
        "command_surface_local_only": recorded
        and boundary.get("command_surface_local_only") is True,
        "command_surface_read_only": recorded
        and boundary.get("command_surface_read_only") is True,
        "result_level_non_claims_canonical_false": all(
            key in non_claims and non_claims[key] is False
            for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }
    return statement


def _build_non_meaning(non_claims: Mapping[str, bool]) -> dict[str, Any]:
    return {
        "command_execution_boundary_executes_selected_command": False,
        "command_execution_boundary_creates_command_execution": False,
        "command_execution_boundary_creates_command_execution_result": False,
        "command_execution_boundary_returns_state": False,
        "command_execution_boundary_performs_lookup": False,
        "command_execution_boundary_creates_operation_permission": False,
        "command_execution_boundary_creates_runtime_permission": False,
        "command_execution_boundary_creates_public_api": False,
        "command_execution_boundary_creates_participant_facing_interface": False,
        "command_execution_boundary_creates_distributed_network_behavior": False,
        "command_execution_boundary_creates_general_lookup_permission": False,
        "command_execution_boundary_creates_arbitrary_lookup_permission": False,
        "command_execution_boundary_permits_unsupported_commands": False,
        "command_execution_boundary_permits_unsupported_lookup_keys": False,
        "command_execution_boundary_creates_new_lookup_result": False,
        "command_execution_boundary_creates_new_lookup_entry": False,
        "command_execution_boundary_performs_filesystem_discovery": False,
        "command_execution_boundary_authorizes_follow_on_work": False,
        "result_level_non_claims": dict(non_claims),
    }


def _determine_outcome(
    declared: Mapping[str, Any],
    checks: list[Mapping[str, Any]],
) -> str:
    if _first_failed_code(checks):
        return OUTCOME_BLOCKED
    requested = declared.get(
        "requested_local_relevance_medium_read_only_local_carrier_command_execution_boundary_outcome"
    )
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or declared.get(
        "additional_basis_context"
    ):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if requested == OUTCOME_NOT_RECORDED or declared.get("not_recorded_basis"):
        return OUTCOME_NOT_RECORDED
    if (
        declared.get(
            "local_relevance_medium_read_only_local_carrier_command_execution_boundary_intent"
        )
        == INTENT_DO_NOT_RECORD
    ):
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _finalize_result(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
    surface_basis: Mapping[str, Any] | None = None,
    command_surface: Mapping[str, Any] | None = None,
    selected_command: str | None = None,
    single_command_selected: bool = False,
    future_may_be_considered: bool = False,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    surface_basis = dict(surface_basis or _basis(""))
    command_surface = dict(command_surface or {})

    outcome = _determine_outcome(declared, checks)
    recorded = outcome == OUTCOME_RECORDED
    boundary = _build_boundary_object(
        declared,
        surface_basis,
        selected_command,
        single_command_selected,
        future_may_be_considered,
        command_surface,
        recorded,
    )
    statement = _build_statement(outcome, boundary, non_claims)
    passed_count, failed_count = _check_counts(checks)
    block_code = _first_failed_code(checks)
    block = None
    if outcome == OUTCOME_BLOCKED:
        public_code = (
            block_code
            or "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED"
        )
        block = {
            "blocked": True,
            "code": public_code,
            "block_code": public_code,
            "reason": _sanitize(declared.get("block_reason", "blocked by bounded check")),
        }

    metadata = {
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_id": (
            boundary["boundary_id"]
        ),
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_type": (
            BOUNDARY_TYPE
        ),
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_version": (
            RESULT_VERSION
        ),
        "generated_at": _utc_timestamp(),
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
    }

    result: dict[str, Any] = {
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_metadata": (
            metadata
        ),
        "declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_question": {
            "question": _sanitize(
                declared.get(
                    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_question"
                )
            ),
            "intent": _sanitize(
                declared.get(
                    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_intent"
                )
            ),
            "boundary_type": BOUNDARY_TYPE,
            "boundary_scope": BOUNDARY_SCOPE,
            "selected_command": _sanitize(boundary.get("selected_command")),
        },
        "selected_local_carrier_command_surface_artifact_basis": dict(surface_basis),
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary": (
            boundary
        ),
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_checks": (
            checks
        ),
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_statement": (
            statement
        ),
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_non_meaning": (
            _build_non_meaning(non_claims)
        ),
        "additional_basis_required": _sanitize(declared.get("additional_basis_context")),
        "not_recorded_basis": _sanitize(declared.get("not_recorded_basis")),
        "what_remains_open": [
            "local carrier command execution",
            "local carrier command execution result",
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
            "authority",
            "currentness",
            "truth",
            "action",
            "synchronization",
            "participation authorization",
            "participant role",
            "follow-on work",
        ],
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    result[
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_summary"
    ] = build_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_summary(
        result
    )
    return result


def resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
    declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary: Mapping[
        str, Any
    ]
    | None = None,
) -> dict:
    """Resolve one local read-only carrier command execution boundary request."""

    if (
        declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary
        is None
    ):
        declared = (
            build_declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_request()
        )
    elif isinstance(
        declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary,
        MappingABC,
    ):
        declared = copy.deepcopy(
            dict(
                declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary
            )
        )
    else:
        checks = [
            _make_check(
                "declared local carrier command execution boundary request is mapping",
                False,
                "mapping",
                type(
                    declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary
                ).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result({}, checks)

    checks: list[dict[str, Any]] = []
    _append_declared_request_checks(declared, checks)
    _append_shortcut_checks(declared, checks)
    _append_non_claim_checks(declared, checks)
    _append_false_posture_checks(declared, checks)
    _append_declared_command_surface_posture_checks(declared, checks)

    _, surface_basis, command_surface = _validate_local_carrier_command_surface_artifact(
        declared, checks
    )
    selected_command, single_command_selected, future_may_be_considered = (
        _append_selected_command_checks(declared, checks)
    )
    _append_authority_exclusion_checks(declared, checks)

    return _finalize_result(
        declared,
        checks,
        surface_basis=surface_basis,
        command_surface=command_surface,
        selected_command=selected_command,
        single_command_selected=single_command_selected,
        future_may_be_considered=future_may_be_considered,
    )


def resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_from_path(
    declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_path: Path
    | str,
) -> dict:
    """Read a declared request JSON object from a path and resolve it."""

    path = Path(
        declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_path
    )
    try:
        with path.open("r", encoding="utf-8") as handle:
            declared = json.load(handle)
    except Exception:
        checks = [
            _make_check(
                "declared local carrier command execution boundary request readable",
                False,
                "readable JSON object",
                str(path),
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_REQUEST_UNREADABLE",
            )
        ]
        return _finalize_result({}, checks)
    if not isinstance(declared, MappingABC):
        checks = [
            _make_check(
                "declared local carrier command execution boundary request is JSON object",
                False,
                "JSON object",
                type(declared).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result({}, checks)
    return resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
        declared
    )


def build_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact public summary from a resolver result."""

    metadata = _mapping_at(
        result,
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_metadata",
    )
    boundary = _mapping_at(
        result, "local_relevance_medium_read_only_local_carrier_command_execution_boundary"
    )
    statement = _mapping_at(
        result,
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_statement",
    )
    checks = result.get(
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_checks"
    )
    check_list = checks if isinstance(checks, list) else []
    passed_count, failed_count = _check_counts(check_list)
    block = result.get("block")
    block_mapping = block if isinstance(block, MappingABC) else {}
    non_claims = _mapping_at(result, "non_claims")

    return {
        "outcome": result.get("outcome"),
        "block_code": block_mapping.get("block_code") or block_mapping.get("code"),
        "block_reason": block_mapping.get("reason"),
        "boundary_id": boundary.get("boundary_id")
        or metadata.get(
            "local_relevance_medium_read_only_local_carrier_command_execution_boundary_id"
        ),
        "question": _mapping_at(
            result,
            "declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_question",
        ).get("question"),
        "intent": _mapping_at(
            result,
            "declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_question",
        ).get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get("result_version", RESULT_VERSION),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "boundary_recorded": boundary.get(
            "future_single_local_read_only_command_execution_may_be_considered"
        )
        is True,
        "basis_local_carrier_command_surface_artifact_preserved": statement.get(
            "basis_local_carrier_command_surface_artifact_preserved"
        )
        is True,
        "allowed_commands_preserved": statement.get("allowed_commands_preserved")
        is True,
        "allowed_command_count_is_three": statement.get("allowed_command_count_is_three")
        is True,
        "selected_command": boundary.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved")
        is True,
        "selected_command_is_from_closed_command_set": statement.get(
            "selected_command_is_from_closed_command_set"
        )
        is True,
        "single_command_selected": statement.get("single_command_selected") is True,
        "future_single_local_read_only_command_execution_may_be_considered": statement.get(
            "future_single_local_read_only_command_execution_may_be_considered"
        )
        is True,
        "local_carrier_command_surface_recorded": statement.get(
            "local_carrier_command_surface_recorded"
        )
        is True,
        "command_surface_local_only": statement.get("command_surface_local_only") is True,
        "command_surface_read_only": statement.get("command_surface_read_only") is True,
        "boundary_object_summary": {
            "boundary_type": boundary.get("boundary_type"),
            "boundary_scope": boundary.get("boundary_scope"),
            "allowed_commands": boundary.get("allowed_commands"),
            "allowed_command_count": boundary.get("allowed_command_count"),
            "selected_command": boundary.get("selected_command"),
        },
        "command_execution_not_performed": non_claims.get("command_execution_performed")
        is False,
        "command_execution_not_created": non_claims.get("command_execution_created")
        is False,
        "command_execution_result_not_created": non_claims.get(
            "command_execution_result_created"
        )
        is False,
        "operation_permission_not_created": non_claims.get("operation_permission_created")
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
        "no_new_lookup_result_or_entry_created": (
            non_claims.get("new_lookup_result_created") is False
            and non_claims.get("new_lookup_entry_created") is False
        ),
        "state_not_returned": non_claims.get("state_returned") is False,
        "lookup_not_performed": non_claims.get("lookup_performed") is False,
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
        "repeated_reception_permission_arbitrary_reception_feed_not_created": (
            non_claims.get("repeated_reception_permission_created") is False
            and non_claims.get("arbitrary_reception_created") is False
            and non_claims.get("feed_created") is False
        ),
        "source_authority_currentness_truth_action_synchronization_participation_participant_role_not_created": (
            non_claims.get("source_created") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("truth_created") is False
            and non_claims.get("action_created") is False
            and non_claims.get("synchronization_created") is False
            and non_claims.get("participation_authorized") is False
            and non_claims.get("participant_role_created") is False
        ),
        "follow_on_not_created": non_claims.get("follow_on_work_authorized") is False,
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "command_execution_performed",
                "command_execution_created",
                "command_execution_result_created",
                "operation_permission_created",
                "runtime_permission_created",
                "public_api_created",
                "participant_facing_interface_created",
                "distributed_network_behavior_created",
                "general_lookup_permission_created",
                "arbitrary_lookup_permission_created",
                "unsupported_commands_permitted",
                "unsupported_lookup_keys_permitted",
                "state_returned",
                "lookup_performed",
                "follow_on_work_authorized",
            )
        },
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": statement.get(
            "result_level_non_claims_canonical_false"
        )
        is True,
    }


def write_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result as stable JSON without silently overwriting."""

    metadata = _mapping_at(
        result,
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_metadata",
    )
    boundary_id = _safe_filename_part(
        _string_or_empty(
            metadata.get(
                "local_relevance_medium_read_only_local_carrier_command_execution_boundary_id"
            )
        )
        or DEFAULT_BOUNDARY_ID
    )
    filename = (
        f"{boundary_id}__"
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_result.json"
    )
    if output_path is None:
        candidate = OUTPUT_ROOT / filename
    else:
        supplied = Path(output_path)
        candidate = supplied / filename if supplied.suffix == "" else supplied

    candidate = _ensure_not_forbidden_output_path(candidate)
    candidate.parent.mkdir(parents=True, exist_ok=True)
    final_path = _with_numeric_suffix_if_exists(candidate)
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(dict(result), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path


def _safe_filename_part(value: str) -> str:
    safe = "".join(
        character
        if character.isalnum() or character in {"_", "-", "."}
        else "_"
        for character in value
    )
    return safe or DEFAULT_BOUNDARY_ID


def _ensure_not_forbidden_output_path(path: Path) -> Path:
    normalized = Path(path)
    parts = normalized.parts
    for forbidden in FORBIDDEN_OUTPUT_ROOTS:
        forbidden_parts = forbidden.parts
        for index in range(0, len(parts) - len(forbidden_parts) + 1):
            if parts[index : index + len(forbidden_parts)] == forbidden_parts:
                raise LocalRelevanceMediumReadOnlyLocalCarrierCommandExecutionBoundaryV0MinError(
                    "refusing to write local carrier command execution boundary result "
                    f"under {forbidden}"
                )
    return normalized


def _with_numeric_suffix_if_exists(path: Path) -> Path:
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


def build_declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_request(
    local_relevance_medium_read_only_local_carrier_command_execution_boundary_id: str = DEFAULT_BOUNDARY_ID,
    selected_local_carrier_command_surface_artifact: Path | str = DEFAULT_LOCAL_CARRIER_COMMAND_SURFACE_ARTIFACT,
    selected_command: str = DEFAULT_SELECTED_COMMAND,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a bounded declared request for the command execution boundary."""

    request: dict[str, Any] = {
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_id": (
            local_relevance_medium_read_only_local_carrier_command_execution_boundary_id
        ),
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_question": (
            CORE_QUESTION
        ),
        "local_relevance_medium_read_only_local_carrier_command_execution_boundary_intent": (
            intent
        ),
        "selected_local_carrier_command_surface_artifact": str(
            selected_local_carrier_command_surface_artifact
        ),
        "selected_command": selected_command,
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "allowed_commands": list(ALLOWED_COMMANDS),
        "allowed_command_count": len(ALLOWED_COMMANDS),
        "future_single_local_read_only_command_execution_may_be_considered": True,
        "local_carrier_command_surface_recorded": True,
        "command_surface_local_only": True,
        "command_surface_read_only": True,
        "declared_non_claims": (
            copy.deepcopy(dict(declared_non_claims))
            if isinstance(declared_non_claims, MappingABC)
            else _canonical_non_claims()
        ),
    }
    for field_name in REQUIRED_FALSE_NON_CLAIMS:
        request[field_name] = False
    request.update(copy.deepcopy(overrides))
    return request
