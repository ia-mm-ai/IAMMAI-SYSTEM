"""Resolve one local relevance medium read-only local carrier command surface boundary.

This resolver reads one selected
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION artifact as bounded
lookup-permission basis and one selected
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER /
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET artifact as read-only state basis.
It records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY object
only.

The boundary is read-only, local, carrier-facing, and non-command-surface-shaped.
It may record that a future local read-only carrier command surface may be
considered for exactly ``state``, ``lookup first_orientation_locator``, and
``lookup second_orientation_locator``. It does not create the command surface,
execute commands, create operation permission, runtime permission, API,
distributed behavior, general lookup permission, arbitrary lookup permission,
unsupported command permission, unsupported-key permission, new lookup result,
new lookup entry, registry, search, query surface, ranking, scoring, priority,
validity judgment, truth judgment, authority judgment, currentness judgment,
repeated reception permission, arbitrary reception, feed, source transfer,
source receipt, action, synchronization, participation, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyLocalCarrierCommandSurfaceBoundaryV0MinError(Exception):
    """Bounded error for local carrier command surface boundary handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min"
)

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_BLOCKED"
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
    "local_carrier_command_surface_boundary_v0_min"
)
DEFAULT_REUSABLE_LOOKUP_PERMISSION_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "reusable_lookup_permission_v0_min/"
    "local_relevance_medium_read_only_reusable_lookup_permission_reference_review_001__"
    "local_relevance_medium_read_only_reusable_lookup_permission_v0_min_result.json"
)
DEFAULT_READ_ONLY_STATE_READER_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min/"
    "local_relevance_medium_read_only_state_packet_reference_review_001__"
    "local_relevance_medium_read_only_state_reader_v0_min_result.json"
)

DEFAULT_BOUNDARY_ID = (
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_001"
)

BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY"
BOUNDARY_SCOPE = "LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY"
SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)

REUSABLE_LOOKUP_PERMISSION_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_RECORDED"
)
READ_ONLY_STATE_READER_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED"
)
STATE_PACKET_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET"
STATE_READER_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER"
STATE_READER_SCOPE = "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY"

ALLOWED_COMMANDS = (
    "state",
    "lookup first_orientation_locator",
    "lookup second_orientation_locator",
)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION "
    "and one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER / "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET basis, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY be "
    "recorded that permits a future local read-only carrier command surface to be "
    "considered for only the commands state, lookup first_orientation_locator, and "
    "lookup second_orientation_locator, without creating the command surface, "
    "executing commands, creating operation permission, creating runtime permission, "
    "creating public API, creating participant-facing interface, creating distributed "
    "network behavior, creating general lookup permission, creating arbitrary lookup "
    "permission, permitting unsupported lookup keys, creating new lookup result, "
    "creating new lookup entry, accepting new entries, accepting new signals, "
    "performing filesystem discovery, creating query surface, registry, search, "
    "ranking, scoring, priority, validity judgment, truth judgment, authority, "
    "currentness, action, synchronization, participation authorization, participant "
    "role, repeated reception permission, arbitrary reception, feed, source transfer, "
    "source receipt, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "local_carrier_command_surface_created",
    "command_execution_performed",
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
    "artifact_existence_treated_as_carrier_command_boundary_authority",
    "latest_file_posture_treated_as_carrier_command_boundary_authority",
    "repo_local_availability_treated_as_carrier_command_boundary_authority",
    "hidden_repo_state_used_as_carrier_command_boundary_content",
    "hidden_repo_state_used_as_carrier_command_boundary_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

BOUNDARY_OBJECT_FALSE_FIELDS = (
    "local_carrier_command_surface_created",
    "command_execution_performed",
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
    "action_created",
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "follow_on_work_authorized",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_recorded",
    "basis_reusable_lookup_permission_artifact_preserved",
    "basis_read_only_state_reader_artifact_preserved",
    "basis_state_packet_object_preserved",
    "basis_state_reader_type_preserved",
    "basis_state_reader_scope_preserved",
    "allowed_commands_preserved",
    "allowed_command_count_is_three",
    "state_command_may_be_considered",
    "lookup_first_orientation_locator_command_may_be_considered",
    "lookup_second_orientation_locator_command_may_be_considered",
    "future_local_read_only_carrier_command_surface_may_be_considered",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_BLOCK_REQUESTED",
    "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_PATH_MISSING",
    "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_UNREADABLE",
    "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_NOT_JSON_OBJECT",
    "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_NOT_RECORDED",
    "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0",
    "READ_ONLY_STATE_READER_ARTIFACT_PATH_MISSING",
    "READ_ONLY_STATE_READER_ARTIFACT_UNREADABLE",
    "READ_ONLY_STATE_READER_ARTIFACT_NOT_JSON_OBJECT",
    "READ_ONLY_STATE_READER_ARTIFACT_NOT_RECORDED",
    "READ_ONLY_STATE_READER_ARTIFACT_FAILED_CHECKS_PRESENT",
    "READ_ONLY_STATE_READER_ARTIFACT_VERSION_NOT_0_1_0",
    "READ_ONLY_STATE_PACKET_OBJECT_MISSING",
    "STATE_PACKET_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
    "STATE_READER_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
    "STATE_READER_SCOPE_NOT_READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
    "ALLOWED_COMMANDS_NOT_EXACT",
    "ALLOWED_COMMAND_COUNT_NOT_THREE",
    "STATE_COMMAND_MAY_NOT_BE_CONSIDERED",
    "LOOKUP_FIRST_ORIENTATION_LOCATOR_COMMAND_MAY_NOT_BE_CONSIDERED",
    "LOOKUP_SECOND_ORIENTATION_LOCATOR_COMMAND_MAY_NOT_BE_CONSIDERED",
    "FUTURE_LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_MAY_NOT_BE_CONSIDERED",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY",
    "LOCAL_CARRIER_COMMAND_SURFACE_CREATED",
    "COMMAND_EXECUTION_PERFORMED",
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
    "ACTION_CREATED",
    "SYNCHRONIZATION_CREATED",
    "PARTICIPATION_AUTHORIZED",
    "PARTICIPANT_ROLE_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_CARRIER_COMMAND_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_CARRIER_COMMAND_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_CARRIER_COMMAND_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_CARRIER_COMMAND_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_CARRIER_COMMAND_BOUNDARY_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_REQUEST_UNREADABLE",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_local_carrier_command_surface_boundary_body",
    "raw_local_carrier_command_surface_body",
    "raw_command_execution_body",
    "raw_reusable_lookup_permission_body",
    "raw_read_only_state_reader_body",
    "raw_state_reader_body",
    "raw_state_packet_body",
    "raw_lookup_pair_coverage_body",
    "raw_lookup_result_body",
    "raw_orientation_index_system_body",
    "raw_orientation_index_body",
    "raw_comparison_view_body",
    "raw_relation_view_body",
    "raw_multiplicity_result_body",
    "raw_first_local_index_entry_body",
    "raw_second_local_index_entry_body",
    "raw_first_orientation_body",
    "raw_second_orientation_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "local_carrier_command_surface_boundary_body",
    "local_carrier_command_surface_body",
    "command_execution_body",
    "reusable_lookup_permission_body",
    "read_only_state_reader_body",
    "state_reader_body",
    "state_packet_body",
    "lookup_pair_coverage_body",
    "lookup_result_body",
    "orientation_index_system_body",
    "orientation_index_body",
    "comparison_view_body",
    "relation_view_body",
    "multiplicity_result_body",
    "first_local_index_entry_body",
    "second_local_index_entry_body",
    "first_orientation_body",
    "second_orientation_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_SURFACE_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_REUSABLE_LOOKUP_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_READ_ONLY_STATE_READER_BODY_MUST_NOT_RETURN",
    "RAW_STATE_READER_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PAIR_COVERAGE_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_INDEX_SYSTEM_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_INDEX_BODY_MUST_NOT_RETURN",
    "RAW_COMPARISON_VIEW_BODY_MUST_NOT_RETURN",
    "RAW_RELATION_VIEW_BODY_MUST_NOT_RETURN",
    "RAW_MULTIPLICITY_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_LOCAL_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_LOCAL_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_ORIENTATION_BODY_MUST_NOT_RETURN",
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

SHORTCUT_FAILURES = {
    "reusable_lookup_permission_artifact_missing": "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_PATH_MISSING",
    "reusable_lookup_permission_artifact_not_recorded": "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_NOT_RECORDED",
    "reusable_lookup_permission_artifact_failed_checks_present": "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "reusable_lookup_permission_artifact_version_not_0_1_0": "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0",
    "read_only_state_reader_artifact_missing": "READ_ONLY_STATE_READER_ARTIFACT_PATH_MISSING",
    "read_only_state_reader_artifact_not_recorded": "READ_ONLY_STATE_READER_ARTIFACT_NOT_RECORDED",
    "read_only_state_reader_artifact_failed_checks_present": "READ_ONLY_STATE_READER_ARTIFACT_FAILED_CHECKS_PRESENT",
    "read_only_state_reader_artifact_version_not_0_1_0": "READ_ONLY_STATE_READER_ARTIFACT_VERSION_NOT_0_1_0",
    "state_packet_object_missing": "READ_ONLY_STATE_PACKET_OBJECT_MISSING",
    "state_packet_type_not_local_relevance_medium_read_only_state_packet": "STATE_PACKET_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
    "state_reader_type_not_local_relevance_medium_read_only_state_reader": "STATE_READER_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
    "state_reader_scope_not_read_existing_local_relevance_medium_state_only": "STATE_READER_SCOPE_NOT_READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
    "allowed_commands_not_exact": "ALLOWED_COMMANDS_NOT_EXACT",
    "allowed_command_count_not_three": "ALLOWED_COMMAND_COUNT_NOT_THREE",
    "state_command_may_not_be_considered": "STATE_COMMAND_MAY_NOT_BE_CONSIDERED",
    "lookup_first_orientation_locator_command_may_not_be_considered": "LOOKUP_FIRST_ORIENTATION_LOCATOR_COMMAND_MAY_NOT_BE_CONSIDERED",
    "lookup_second_orientation_locator_command_may_not_be_considered": "LOOKUP_SECOND_ORIENTATION_LOCATOR_COMMAND_MAY_NOT_BE_CONSIDERED",
    "future_local_read_only_carrier_command_surface_may_not_be_considered": "FUTURE_LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_MAY_NOT_BE_CONSIDERED",
    "boundary_type_not_local_relevance_medium_read_only_local_carrier_command_surface_boundary": "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY",
    "boundary_scope_not_local_read_only_carrier_command_surface_consideration_only": "BOUNDARY_SCOPE_NOT_LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY",
    "local_carrier_command_surface_created": "LOCAL_CARRIER_COMMAND_SURFACE_CREATED",
    "command_execution_performed": "COMMAND_EXECUTION_PERFORMED",
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
    "action_created": "ACTION_CREATED",
    "synchronization_created": "SYNCHRONIZATION_CREATED",
    "participation_authorized": "PARTICIPATION_AUTHORIZED",
    "participant_role_created": "PARTICIPANT_ROLE_CREATED",
    "deployment_created": "DEPLOYMENT_CREATED",
    "public_release_created": "PUBLIC_RELEASE_CREATED",
    "broader_reusable_permission_created": "BROADER_REUSABLE_PERMISSION_CREATED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "artifact_existence_treated_as_carrier_command_boundary_authority": "ARTIFACT_EXISTENCE_TREATED_AS_CARRIER_COMMAND_BOUNDARY_AUTHORITY",
    "latest_file_posture_treated_as_carrier_command_boundary_authority": "LATEST_FILE_POSTURE_TREATED_AS_CARRIER_COMMAND_BOUNDARY_AUTHORITY",
    "repo_local_availability_treated_as_carrier_command_boundary_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_CARRIER_COMMAND_BOUNDARY_AUTHORITY",
    "hidden_repo_state_used_as_carrier_command_boundary_content": "HIDDEN_REPO_STATE_USED_AS_CARRIER_COMMAND_BOUNDARY_CONTENT",
    "hidden_repo_state_used_as_carrier_command_boundary_authority": "HIDDEN_REPO_STATE_USED_AS_CARRIER_COMMAND_BOUNDARY_AUTHORITY",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
}

FORBIDDEN_OUTPUT_ROOTS = (
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

OFFICIAL_STRINGS = set(OUTCOME_FAMILY)
OFFICIAL_STRINGS.update(BLOCK_CODES)
OFFICIAL_STRINGS.update(SUPPORTED_INTENTS)
OFFICIAL_STRINGS.update(SUPPORTED_BOUNDARY_TYPE_VALUES)
OFFICIAL_STRINGS.update(SUPPORTED_BOUNDARY_SCOPE_VALUES)
OFFICIAL_STRINGS.update(ALLOWED_COMMANDS)
OFFICIAL_STRINGS.update(REQUIRED_FALSE_NON_CLAIMS)
OFFICIAL_STRINGS.update(ALLOWED_TRUE_RECORDED_FIELDS)
OFFICIAL_STRINGS.update(
    {
        RESULT_VERSION,
        RESOLVER_MODULE,
        DEFAULT_BOUNDARY_ID,
        REUSABLE_LOOKUP_PERMISSION_RECORDED_OUTCOME,
        READ_ONLY_STATE_READER_RECORDED_OUTCOME,
        STATE_PACKET_TYPE,
        STATE_READER_TYPE,
        STATE_READER_SCOPE,
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
            else "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_REQUEST_MALFORMED"
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
        "boundary_version",
        "permission_version",
        "state_packet_version",
        "state_reader_version",
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


def _state_packet_object_from_artifact(artifact: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {}
    value = artifact.get("local_relevance_medium_read_only_state_packet")
    return value if isinstance(value, MappingABC) else {}


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


def _append_declared_request_checks(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    question = declared.get(
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_question"
    )
    intent = declared.get(
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_intent"
    )
    boundary_type = declared.get("boundary_type")
    boundary_scope = declared.get("boundary_scope")

    _append_check(
        checks,
        "local carrier command surface boundary question declared",
        _present(question),
        "declared local carrier command surface boundary question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_QUESTION_UNDECLARED",
    )
    _append_check(
        checks,
        "boundary intent supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _append_check(
            checks,
            "local carrier command surface boundary block intent not requested",
            False,
            f"not {INTENT_BLOCK}",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_BLOCK_REQUESTED",
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
        "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY",
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
        "boundary scope local read-only carrier command surface consideration only",
        boundary_scope == BOUNDARY_SCOPE,
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_NOT_LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY",
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


def _append_allowed_command_checks(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    allowed_commands = declared.get("allowed_commands", list(ALLOWED_COMMANDS))
    allowed_command_count = declared.get(
        "allowed_command_count",
        len(allowed_commands) if isinstance(allowed_commands, list) else None,
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
        allowed_command_count == 3,
        3,
        allowed_command_count,
        "ALLOWED_COMMAND_COUNT_NOT_THREE",
    )
    _append_check(
        checks,
        "state command may be considered",
        declared.get("state_command_may_be_considered", True) is True,
        True,
        declared.get("state_command_may_be_considered", True),
        "STATE_COMMAND_MAY_NOT_BE_CONSIDERED",
    )
    _append_check(
        checks,
        "lookup first orientation locator command may be considered",
        declared.get("lookup_first_orientation_locator_command_may_be_considered", True)
        is True,
        True,
        declared.get("lookup_first_orientation_locator_command_may_be_considered", True),
        "LOOKUP_FIRST_ORIENTATION_LOCATOR_COMMAND_MAY_NOT_BE_CONSIDERED",
    )
    _append_check(
        checks,
        "lookup second orientation locator command may be considered",
        declared.get("lookup_second_orientation_locator_command_may_be_considered", True)
        is True,
        True,
        declared.get("lookup_second_orientation_locator_command_may_be_considered", True),
        "LOOKUP_SECOND_ORIENTATION_LOCATOR_COMMAND_MAY_NOT_BE_CONSIDERED",
    )
    _append_check(
        checks,
        "future local read-only carrier command surface may be considered",
        declared.get("future_local_read_only_carrier_command_surface_may_be_considered", True)
        is True,
        True,
        declared.get("future_local_read_only_carrier_command_surface_may_be_considered", True),
        "FUTURE_LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_MAY_NOT_BE_CONSIDERED",
    )


def _append_authority_exclusion_checks(checks: list[dict[str, Any]]) -> None:
    _append_check(
        checks,
        "artifact existence not carrier-command-boundary authority",
        True,
        "artifact existence not treated as carrier-command-boundary authority",
        False,
    )
    _append_check(
        checks,
        "latest file posture not carrier-command-boundary authority",
        True,
        "latest file posture not treated as carrier-command-boundary authority",
        False,
    )
    _append_check(
        checks,
        "repo-local availability not carrier-command-boundary authority",
        True,
        "repo-local availability not treated as carrier-command-boundary authority",
        False,
    )
    _append_check(
        checks,
        "hidden repo state not carrier-command-boundary content or authority",
        True,
        "hidden repo state excluded from carrier-command-boundary content and authority",
        False,
    )
    _append_check(
        checks,
        "predecessor failure evidence preserved",
        True,
        "predecessor failed-lineage evidence preserved",
        "predecessor failed-lineage evidence preserved",
    )
    _append_check(
        checks,
        "result-level required false non-claims canonical false",
        True,
        "all result-level required false non-claims canonical false",
        _canonical_non_claims(),
    )


def _validate_reusable_lookup_permission_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, str]:
    artifact_value = declared.get("selected_reusable_lookup_permission_artifact")
    path_text = _string_or_empty(artifact_value)
    _append_check(
        checks,
        "reusable lookup permission artifact path declared",
        _present(path_text),
        "selected reusable lookup permission artifact path",
        path_text,
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_PATH_MISSING",
    )
    artifact, read_code, path_text = _read_json_artifact(
        artifact_value,
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_PATH_MISSING",
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_UNREADABLE",
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_NOT_JSON_OBJECT",
    )
    if read_code:
        _append_check(
            checks,
            "reusable lookup permission artifact readable JSON object",
            False,
            "readable JSON object",
            path_text or artifact_value,
            read_code,
        )
        return None, path_text

    assert artifact is not None
    outcome = _artifact_outcome(
        artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_summary",
    )
    result_version = _artifact_result_version(
        artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_summary",
        artifact.get("local_relevance_medium_read_only_reusable_lookup_permission")
        if isinstance(
            artifact.get("local_relevance_medium_read_only_reusable_lookup_permission"),
            MappingABC,
        )
        else None,
    )
    failed_count = _artifact_failed_check_count(
        artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_summary",
        "local_relevance_medium_read_only_reusable_lookup_permission_checks",
    )
    _append_check(
        checks,
        "reusable lookup permission artifact readable JSON",
        True,
        "readable JSON object",
        path_text,
    )
    _append_check(
        checks,
        "reusable lookup permission artifact outcome recorded",
        outcome == REUSABLE_LOOKUP_PERMISSION_RECORDED_OUTCOME,
        REUSABLE_LOOKUP_PERMISSION_RECORDED_OUTCOME,
        outcome,
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "reusable lookup permission artifact result version 0.1.0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version,
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "reusable lookup permission artifact failed check count zero",
        failed_count == 0,
        0,
        failed_count,
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    return artifact, path_text


def _validate_read_only_state_reader_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, str]:
    artifact_value = declared.get("selected_read_only_state_reader_artifact")
    path_text = _string_or_empty(artifact_value)
    _append_check(
        checks,
        "read-only state reader artifact path declared",
        _present(path_text),
        "selected read-only state reader artifact path",
        path_text,
        "READ_ONLY_STATE_READER_ARTIFACT_PATH_MISSING",
    )
    artifact, read_code, path_text = _read_json_artifact(
        artifact_value,
        "READ_ONLY_STATE_READER_ARTIFACT_PATH_MISSING",
        "READ_ONLY_STATE_READER_ARTIFACT_UNREADABLE",
        "READ_ONLY_STATE_READER_ARTIFACT_NOT_JSON_OBJECT",
    )
    if read_code:
        _append_check(
            checks,
            "read-only state reader artifact readable JSON object",
            False,
            "readable JSON object",
            path_text or artifact_value,
            read_code,
        )
        return None, path_text

    assert artifact is not None
    state_packet = _state_packet_object_from_artifact(artifact)
    outcome = _artifact_outcome(
        artifact,
        "local_relevance_medium_read_only_state_reader_metadata",
        "local_relevance_medium_read_only_state_reader_summary",
    )
    result_version = _artifact_result_version(
        artifact,
        "local_relevance_medium_read_only_state_reader_metadata",
        "local_relevance_medium_read_only_state_reader_summary",
        state_packet,
    )
    failed_count = _artifact_failed_check_count(
        artifact,
        "local_relevance_medium_read_only_state_reader_metadata",
        "local_relevance_medium_read_only_state_reader_summary",
        "local_relevance_medium_read_only_state_reader_checks",
    )
    _append_check(
        checks,
        "read-only state reader artifact readable JSON",
        True,
        "readable JSON object",
        path_text,
    )
    _append_check(
        checks,
        "read-only state reader artifact outcome recorded",
        outcome == READ_ONLY_STATE_READER_RECORDED_OUTCOME,
        READ_ONLY_STATE_READER_RECORDED_OUTCOME,
        outcome,
        "READ_ONLY_STATE_READER_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "read-only state reader artifact result version 0.1.0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version,
        "READ_ONLY_STATE_READER_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "read-only state reader artifact failed check count zero",
        failed_count == 0,
        0,
        failed_count,
        "READ_ONLY_STATE_READER_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _append_check(
        checks,
        "read-only state packet object present",
        bool(state_packet),
        "local_relevance_medium_read_only_state_packet object",
        bool(state_packet),
        "READ_ONLY_STATE_PACKET_OBJECT_MISSING",
    )
    _append_check(
        checks,
        "state packet type exact",
        state_packet.get("state_packet_type") == STATE_PACKET_TYPE,
        STATE_PACKET_TYPE,
        state_packet.get("state_packet_type"),
        "STATE_PACKET_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
    )
    _append_check(
        checks,
        "state reader type exact",
        state_packet.get("state_reader_type") == STATE_READER_TYPE,
        STATE_READER_TYPE,
        state_packet.get("state_reader_type"),
        "STATE_READER_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
    )
    _append_check(
        checks,
        "state reader scope exact",
        state_packet.get("state_reader_scope") == STATE_READER_SCOPE,
        STATE_READER_SCOPE,
        state_packet.get("state_reader_scope"),
        "STATE_READER_SCOPE_NOT_READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
    )
    return artifact, path_text


def _build_boundary_object(
    declared: Mapping[str, Any],
    reusable_lookup_permission_artifact: Mapping[str, Any],
    reusable_lookup_permission_path: str,
    read_only_state_reader_artifact: Mapping[str, Any],
    read_only_state_reader_path: str,
) -> dict[str, Any]:
    state_packet = _state_packet_object_from_artifact(read_only_state_reader_artifact)
    reusable_outcome = _artifact_outcome(
        reusable_lookup_permission_artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_summary",
    )
    reusable_version = _artifact_result_version(
        reusable_lookup_permission_artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_summary",
        reusable_lookup_permission_artifact.get(
            "local_relevance_medium_read_only_reusable_lookup_permission"
        )
        if isinstance(
            reusable_lookup_permission_artifact.get(
                "local_relevance_medium_read_only_reusable_lookup_permission"
            ),
            MappingABC,
        )
        else None,
    )
    reusable_failed_count = _artifact_failed_check_count(
        reusable_lookup_permission_artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_summary",
        "local_relevance_medium_read_only_reusable_lookup_permission_checks",
    )
    state_reader_outcome = _artifact_outcome(
        read_only_state_reader_artifact,
        "local_relevance_medium_read_only_state_reader_metadata",
        "local_relevance_medium_read_only_state_reader_summary",
    )
    state_reader_version = _artifact_result_version(
        read_only_state_reader_artifact,
        "local_relevance_medium_read_only_state_reader_metadata",
        "local_relevance_medium_read_only_state_reader_summary",
        state_packet,
    )
    state_reader_failed_count = _artifact_failed_check_count(
        read_only_state_reader_artifact,
        "local_relevance_medium_read_only_state_reader_metadata",
        "local_relevance_medium_read_only_state_reader_summary",
        "local_relevance_medium_read_only_state_reader_checks",
    )

    boundary = {
        "boundary_id": _string_or_empty(
            declared.get("local_relevance_medium_read_only_local_carrier_command_surface_boundary_id")
        )
        or DEFAULT_BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "basis_reusable_lookup_permission_artifact": reusable_lookup_permission_path,
        "basis_reusable_lookup_permission_outcome": reusable_outcome,
        "basis_reusable_lookup_permission_result_version": reusable_version,
        "basis_reusable_lookup_permission_failed_check_count": reusable_failed_count,
        "basis_read_only_state_reader_artifact": read_only_state_reader_path,
        "basis_read_only_state_reader_outcome": state_reader_outcome,
        "basis_read_only_state_reader_result_version": state_reader_version,
        "basis_read_only_state_reader_failed_check_count": state_reader_failed_count,
        "basis_state_packet_type": state_packet.get("state_packet_type"),
        "basis_state_reader_type": state_packet.get("state_reader_type"),
        "basis_state_reader_scope": state_packet.get("state_reader_scope"),
        "allowed_commands": list(ALLOWED_COMMANDS),
        "allowed_command_count": 3,
        "state_command_may_be_considered": True,
        "lookup_first_orientation_locator_command_may_be_considered": True,
        "lookup_second_orientation_locator_command_may_be_considered": True,
        "future_local_read_only_carrier_command_surface_may_be_considered": True,
    }
    boundary.update({key: False for key in BOUNDARY_OBJECT_FALSE_FIELDS})
    return boundary


def _append_boundary_object_checks(
    boundary: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    _append_check(
        checks,
        "boundary object type local carrier command surface boundary",
        boundary.get("boundary_type") == BOUNDARY_TYPE,
        BOUNDARY_TYPE,
        boundary.get("boundary_type"),
        "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY",
    )
    _append_check(
        checks,
        "boundary object scope consideration only",
        boundary.get("boundary_scope") == BOUNDARY_SCOPE,
        BOUNDARY_SCOPE,
        boundary.get("boundary_scope"),
        "BOUNDARY_SCOPE_NOT_LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY",
    )
    _append_check(
        checks,
        "basis reusable lookup permission artifact preserved",
        _present(boundary.get("basis_reusable_lookup_permission_artifact")),
        "selected reusable lookup permission artifact path preserved",
        boundary.get("basis_reusable_lookup_permission_artifact"),
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_PATH_MISSING",
    )
    _append_check(
        checks,
        "basis read-only state reader artifact preserved",
        _present(boundary.get("basis_read_only_state_reader_artifact")),
        "selected read-only state reader artifact path preserved",
        boundary.get("basis_read_only_state_reader_artifact"),
        "READ_ONLY_STATE_READER_ARTIFACT_PATH_MISSING",
    )
    _append_check(
        checks,
        "basis state packet object preserved",
        boundary.get("basis_state_packet_type") == STATE_PACKET_TYPE,
        STATE_PACKET_TYPE,
        boundary.get("basis_state_packet_type"),
        "STATE_PACKET_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
    )
    _append_check(
        checks,
        "basis state reader type preserved",
        boundary.get("basis_state_reader_type") == STATE_READER_TYPE,
        STATE_READER_TYPE,
        boundary.get("basis_state_reader_type"),
        "STATE_READER_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
    )
    _append_check(
        checks,
        "basis state reader scope preserved",
        boundary.get("basis_state_reader_scope") == STATE_READER_SCOPE,
        STATE_READER_SCOPE,
        boundary.get("basis_state_reader_scope"),
        "STATE_READER_SCOPE_NOT_READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
    )
    _append_check(
        checks,
        "allowed commands preserved",
        boundary.get("allowed_commands") == list(ALLOWED_COMMANDS),
        list(ALLOWED_COMMANDS),
        boundary.get("allowed_commands"),
        "ALLOWED_COMMANDS_NOT_EXACT",
    )
    _append_check(
        checks,
        "allowed command count is three",
        boundary.get("allowed_command_count") == 3,
        3,
        boundary.get("allowed_command_count"),
        "ALLOWED_COMMAND_COUNT_NOT_THREE",
    )
    for field_name in (
        "state_command_may_be_considered",
        "lookup_first_orientation_locator_command_may_be_considered",
        "lookup_second_orientation_locator_command_may_be_considered",
        "future_local_read_only_carrier_command_surface_may_be_considered",
    ):
        _append_check(
            checks,
            f"{field_name} true",
            boundary.get(field_name) is True,
            True,
            boundary.get(field_name),
            SHORTCUT_FAILURES.get(
                field_name.replace("_may_be_considered", "_may_not_be_considered"),
                "FUTURE_LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_MAY_NOT_BE_CONSIDERED",
            ),
        )
    for field_name in BOUNDARY_OBJECT_FALSE_FIELDS:
        _append_check(
            checks,
            f"{field_name} false",
            boundary.get(field_name) is False,
            False,
            boundary.get(field_name),
            SHORTCUT_FAILURES.get(field_name),
        )


def _build_statement(boundary: Mapping[str, Any], non_claims: Mapping[str, bool]) -> dict[str, bool]:
    return {
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_recorded": (
            boundary.get("boundary_type") == BOUNDARY_TYPE
            and boundary.get("boundary_scope") == BOUNDARY_SCOPE
            and boundary.get("future_local_read_only_carrier_command_surface_may_be_considered")
            is True
        ),
        "basis_reusable_lookup_permission_artifact_preserved": _present(
            boundary.get("basis_reusable_lookup_permission_artifact")
        ),
        "basis_read_only_state_reader_artifact_preserved": _present(
            boundary.get("basis_read_only_state_reader_artifact")
        ),
        "basis_state_packet_object_preserved": (
            boundary.get("basis_state_packet_type") == STATE_PACKET_TYPE
        ),
        "basis_state_reader_type_preserved": (
            boundary.get("basis_state_reader_type") == STATE_READER_TYPE
        ),
        "basis_state_reader_scope_preserved": (
            boundary.get("basis_state_reader_scope") == STATE_READER_SCOPE
        ),
        "allowed_commands_preserved": boundary.get("allowed_commands") == list(ALLOWED_COMMANDS),
        "allowed_command_count_is_three": boundary.get("allowed_command_count") == 3,
        "state_command_may_be_considered": (
            boundary.get("state_command_may_be_considered") is True
        ),
        "lookup_first_orientation_locator_command_may_be_considered": (
            boundary.get("lookup_first_orientation_locator_command_may_be_considered") is True
        ),
        "lookup_second_orientation_locator_command_may_be_considered": (
            boundary.get("lookup_second_orientation_locator_command_may_be_considered") is True
        ),
        "future_local_read_only_carrier_command_surface_may_be_considered": (
            boundary.get("future_local_read_only_carrier_command_surface_may_be_considered")
            is True
        ),
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "not_local_carrier_command_surface": True,
        "not_command_execution": True,
        "not_operation_permission": True,
        "not_runtime_permission": True,
        "not_public_api": True,
        "not_participant_facing_interface": True,
        "not_distributed_network_behavior": True,
        "not_general_lookup_permission": True,
        "not_arbitrary_lookup_permission": True,
        "not_unsupported_command_permission": True,
        "not_unsupported_key_permission": True,
        "not_new_lookup_result": True,
        "not_new_lookup_entry": True,
        "not_registry": True,
        "not_search": True,
        "not_query_surface": True,
        "not_ranking": True,
        "not_authority": True,
        "not_currentness": True,
        "not_truth": True,
        "not_action": True,
        "not_follow_on_work": True,
    }


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium read-only local carrier command surface boundary test",
        "local relevance medium read-only local carrier command surface boundary live artifact",
        "local relevance medium read-only local carrier command surface boundary terminal summary, if needed",
        "local relevance medium read-only local carrier command surface",
        "local carrier command execution",
        "operation permission",
        "runtime permission",
        "public API",
        "participant-facing interface",
        "distributed network behavior",
        "general lookup permission",
        "arbitrary lookup permission",
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
        "action",
        "synchronization",
        "participation authorization",
        "participant role",
        "repeated reception permission",
        "arbitrary reception",
        "feed",
        "follow-on work",
    ]


def _reusable_lookup_permission_artifact_basis(
    artifact: Mapping[str, Any] | None,
    path_text: str,
) -> dict[str, Any]:
    artifact_map = artifact if isinstance(artifact, MappingABC) else {}
    return {
        "basis_role": "bounded_lookup_permission_basis_only",
        "basis_reusable_lookup_permission_artifact": path_text,
        "basis_reusable_lookup_permission_outcome": _artifact_outcome(
            artifact_map,
            "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
            "local_relevance_medium_read_only_reusable_lookup_permission_summary",
        )
        if artifact_map
        else None,
        "basis_reusable_lookup_permission_result_version": _artifact_result_version(
            artifact_map,
            "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
            "local_relevance_medium_read_only_reusable_lookup_permission_summary",
            artifact_map.get("local_relevance_medium_read_only_reusable_lookup_permission")
            if isinstance(
                artifact_map.get("local_relevance_medium_read_only_reusable_lookup_permission"),
                MappingABC,
            )
            else None,
        )
        if artifact_map
        else None,
        "basis_reusable_lookup_permission_failed_check_count": _artifact_failed_check_count(
            artifact_map,
            "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
            "local_relevance_medium_read_only_reusable_lookup_permission_summary",
            "local_relevance_medium_read_only_reusable_lookup_permission_checks",
        )
        if artifact_map
        else None,
        "raw_artifact_body_returned": False,
    }


def _read_only_state_reader_artifact_basis(
    artifact: Mapping[str, Any] | None,
    path_text: str,
) -> dict[str, Any]:
    artifact_map = artifact if isinstance(artifact, MappingABC) else {}
    state_packet = _state_packet_object_from_artifact(artifact_map)
    return {
        "basis_role": "read_only_state_basis_only",
        "basis_read_only_state_reader_artifact": path_text,
        "basis_read_only_state_reader_outcome": _artifact_outcome(
            artifact_map,
            "local_relevance_medium_read_only_state_reader_metadata",
            "local_relevance_medium_read_only_state_reader_summary",
        )
        if artifact_map
        else None,
        "basis_read_only_state_reader_result_version": _artifact_result_version(
            artifact_map,
            "local_relevance_medium_read_only_state_reader_metadata",
            "local_relevance_medium_read_only_state_reader_summary",
            state_packet,
        )
        if artifact_map
        else None,
        "basis_read_only_state_reader_failed_check_count": _artifact_failed_check_count(
            artifact_map,
            "local_relevance_medium_read_only_state_reader_metadata",
            "local_relevance_medium_read_only_state_reader_summary",
            "local_relevance_medium_read_only_state_reader_checks",
        )
        if artifact_map
        else None,
        "basis_state_packet_type": state_packet.get("state_packet_type"),
        "basis_state_reader_type": state_packet.get("state_reader_type"),
        "basis_state_reader_scope": state_packet.get("state_reader_scope"),
        "raw_artifact_body_returned": False,
    }


def _finalize_result(
    declared: Mapping[str, Any],
    reusable_lookup_permission_artifact: Mapping[str, Any] | None,
    reusable_lookup_permission_path: str,
    read_only_state_reader_artifact: Mapping[str, Any] | None,
    read_only_state_reader_path: str,
    boundary: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block_code: str | None,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    statement = _build_statement(boundary, non_claims)
    passed_count, failed_count = _check_counts(checks)
    declared_id = _string_or_empty(
        declared.get("local_relevance_medium_read_only_local_carrier_command_surface_boundary_id")
    )
    boundary_id = _string_or_empty(boundary.get("boundary_id")) or declared_id or DEFAULT_BOUNDARY_ID
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": block_code if outcome == OUTCOME_BLOCKED else None,
        "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
        "reason": _sanitize(declared.get("block_reason"))
        if outcome == OUTCOME_BLOCKED and declared.get("block_reason") is not None
        else (block_code if outcome == OUTCOME_BLOCKED else None),
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata": {
            "local_relevance_medium_read_only_local_carrier_command_surface_boundary_id": boundary_id,
            "local_relevance_medium_read_only_local_carrier_command_surface_boundary_type": BOUNDARY_TYPE,
            "local_relevance_medium_read_only_local_carrier_command_surface_boundary_version": RESULT_VERSION,
            "generated_at": _utc_timestamp(),
            "resolver_module": RESOLVER_MODULE,
            "result_version": RESULT_VERSION,
            "passed_check_count": passed_count,
            "failed_check_count": failed_count,
        },
        "declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary_question": {
            "question": _sanitize(
                declared.get(
                    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_question"
                )
            ),
            "intent": _sanitize(
                declared.get(
                    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_intent"
                )
            ),
        },
        "selected_reusable_lookup_permission_artifact_basis": (
            _reusable_lookup_permission_artifact_basis(
                reusable_lookup_permission_artifact,
                reusable_lookup_permission_path,
            )
        ),
        "selected_read_only_state_reader_artifact_basis": (
            _read_only_state_reader_artifact_basis(
                read_only_state_reader_artifact,
                read_only_state_reader_path,
            )
        ),
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary": (
            copy.deepcopy(dict(boundary))
        ),
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_checks": (
            copy.deepcopy(checks)
        ),
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_statement": (
            statement
        ),
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": copy.deepcopy(declared.get("additional_basis_context", []))
        if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        else [],
        "not_recorded_basis": copy.deepcopy(declared.get("not_recorded_basis", []))
        if outcome == OUTCOME_NOT_RECORDED
        else [],
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    result[
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_summary"
    ] = build_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_summary(
        result
    )
    return _sanitize(result)


def resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
    declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary: Mapping[
        str, Any
    ]
    | None = None,
) -> dict[str, Any]:
    if declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary is None:
        declared = (
            build_declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_request()
        )
    elif isinstance(
        declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary,
        MappingABC,
    ):
        declared = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary)
        )
    else:
        checks = [
            _make_check(
                "declared local carrier command surface boundary request mapping",
                False,
                "mapping request",
                type(
                    declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary
                ).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result(
            {},
            None,
            "",
            None,
            "",
            {},
            checks,
            OUTCOME_BLOCKED,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_REQUEST_MALFORMED",
        )

    checks: list[dict[str, Any]] = []
    _append_declared_request_checks(declared, checks)
    _append_shortcut_checks(declared, checks)
    _append_non_claim_checks(declared, checks)
    _append_allowed_command_checks(declared, checks)
    _append_authority_exclusion_checks(checks)

    reusable_lookup_permission_artifact, reusable_lookup_permission_path = (
        _validate_reusable_lookup_permission_artifact(declared, checks)
    )
    read_only_state_reader_artifact, read_only_state_reader_path = (
        _validate_read_only_state_reader_artifact(declared, checks)
    )

    failed_before_object = _first_failed_code(checks)
    boundary: dict[str, Any] = {}
    if (
        failed_before_object is None
        and declared.get(
            "local_relevance_medium_read_only_local_carrier_command_surface_boundary_intent"
        )
        == INTENT_RECORD
        and reusable_lookup_permission_artifact is not None
        and read_only_state_reader_artifact is not None
    ):
        boundary = _build_boundary_object(
            declared,
            reusable_lookup_permission_artifact,
            reusable_lookup_permission_path,
            read_only_state_reader_artifact,
            read_only_state_reader_path,
        )
        _append_boundary_object_checks(boundary, checks)
    elif failed_before_object is None:
        _append_check(
            checks,
            "local carrier command surface boundary not recorded by non-record intent",
            True,
            "not recorded",
            declared.get(
                "local_relevance_medium_read_only_local_carrier_command_surface_boundary_intent"
            ),
        )

    failed_code = _first_failed_code(checks)
    if failed_code:
        return _finalize_result(
            declared,
            reusable_lookup_permission_artifact,
            reusable_lookup_permission_path,
            read_only_state_reader_artifact,
            read_only_state_reader_path,
            boundary,
            checks,
            OUTCOME_BLOCKED,
            failed_code,
        )

    requested_outcome = declared.get(
        "requested_local_relevance_medium_read_only_local_carrier_command_surface_boundary_outcome"
    )
    if requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return _finalize_result(
            declared,
            reusable_lookup_permission_artifact,
            reusable_lookup_permission_path,
            read_only_state_reader_artifact,
            read_only_state_reader_path,
            boundary,
            checks,
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            None,
        )
    if requested_outcome == OUTCOME_NOT_RECORDED or declared.get(
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_intent"
    ) == INTENT_DO_NOT_RECORD:
        return _finalize_result(
            declared,
            reusable_lookup_permission_artifact,
            reusable_lookup_permission_path,
            read_only_state_reader_artifact,
            read_only_state_reader_path,
            {},
            checks,
            OUTCOME_NOT_RECORDED,
            None,
        )

    return _finalize_result(
        declared,
        reusable_lookup_permission_artifact,
        reusable_lookup_permission_path,
        read_only_state_reader_artifact,
        read_only_state_reader_path,
        boundary,
        checks,
        OUTCOME_RECORDED,
        None,
    )


def resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_from_path(
    declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary_path: Path
    | str,
) -> dict[str, Any]:
    path = Path(declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception:
        checks = [
            _make_check(
                "declared local carrier command surface boundary request path readable JSON",
                False,
                "readable JSON object",
                str(path),
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_REQUEST_UNREADABLE",
            )
        ]
        return _finalize_result(
            {},
            None,
            "",
            None,
            "",
            {},
            checks,
            OUTCOME_BLOCKED,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_REQUEST_UNREADABLE",
        )
    if not isinstance(loaded, MappingABC):
        checks = [
            _make_check(
                "declared local carrier command surface boundary request JSON object",
                False,
                "JSON object",
                type(loaded).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result(
            {},
            None,
            "",
            None,
            "",
            {},
            checks,
            OUTCOME_BLOCKED,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_REQUEST_MALFORMED",
        )
    return resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
        loaded
    )


def _path_is_under(candidate: Path, root: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def _guard_output_path(path: Path) -> None:
    for forbidden_root in FORBIDDEN_OUTPUT_ROOTS:
        if path == forbidden_root or _path_is_under(path, forbidden_root):
            raise LocalRelevanceMediumReadOnlyLocalCarrierCommandSurfaceBoundaryV0MinError(
                f"refusing to write under prior artifact root: {forbidden_root}"
            )


def write_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyLocalCarrierCommandSurfaceBoundaryV0MinError(
            "result must be a mapping"
        )

    metadata = result.get(
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata"
    )
    metadata_map = metadata if isinstance(metadata, MappingABC) else {}
    boundary = result.get("local_relevance_medium_read_only_local_carrier_command_surface_boundary")
    boundary_map = boundary if isinstance(boundary, MappingABC) else {}
    result_id = (
        _string_or_empty(
            metadata_map.get(
                "local_relevance_medium_read_only_local_carrier_command_surface_boundary_id"
            )
        )
        or _string_or_empty(boundary_map.get("boundary_id"))
        or DEFAULT_BOUNDARY_ID
    )
    filename = (
        f"{result_id}__"
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_result.json"
    )
    if output_path is None:
        path = OUTPUT_ROOT / filename
    else:
        candidate = Path(output_path)
        path = candidate / filename if candidate.suffix == "" else candidate
    _guard_output_path(path)
    if path.exists():
        base = path.with_suffix("")
        suffix = path.suffix
        counter = 1
        next_path = Path(f"{base}_{counter:03d}{suffix}")
        while next_path.exists():
            counter += 1
            next_path = Path(f"{base}_{counter:03d}{suffix}")
        path = next_path
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(copy.deepcopy(dict(result))), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return path


def build_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyLocalCarrierCommandSurfaceBoundaryV0MinError(
            "result must be a mapping"
        )
    metadata = result.get(
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata"
    )
    metadata_map = metadata if isinstance(metadata, MappingABC) else {}
    declared_question = result.get(
        "declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary_question"
    )
    declared_map = declared_question if isinstance(declared_question, MappingABC) else {}
    boundary = result.get("local_relevance_medium_read_only_local_carrier_command_surface_boundary")
    boundary_map = boundary if isinstance(boundary, MappingABC) else {}
    checks = result.get(
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_checks"
    )
    checks_list = checks if isinstance(checks, list) else []
    passed_count, failed_count = _check_counts(
        [check for check in checks_list if isinstance(check, MappingABC)]
    )
    statement = result.get(
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_statement"
    )
    statement_map = statement if isinstance(statement, MappingABC) else {}
    non_claims = result.get("non_claims")
    non_claims_map = non_claims if isinstance(non_claims, MappingABC) else {}
    block = result.get("block")
    block_map = block if isinstance(block, MappingABC) else {}

    return _sanitize(
        {
            "outcome": result.get("outcome"),
            "block_code": block_map.get("block_code") or block_map.get("code"),
            "block_reason": block_map.get("reason"),
            "boundary_id": _string_or_empty(boundary_map.get("boundary_id"))
            or _string_or_empty(
                metadata_map.get(
                    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_id"
                )
            ),
            "question": declared_map.get("question"),
            "intent": declared_map.get("intent"),
            "passed_check_count": passed_count,
            "failed_check_count": failed_count,
            "result_version": metadata_map.get("result_version") or RESULT_VERSION,
            "resolver_module": metadata_map.get("resolver_module") or RESOLVER_MODULE,
            "boundary_recorded": bool(
                statement_map.get(
                    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_recorded"
                )
            ),
            "basis_reusable_lookup_permission_artifact_preserved": bool(
                statement_map.get("basis_reusable_lookup_permission_artifact_preserved")
            ),
            "basis_read_only_state_reader_artifact_preserved": bool(
                statement_map.get("basis_read_only_state_reader_artifact_preserved")
            ),
            "basis_state_packet_object_preserved": bool(
                statement_map.get("basis_state_packet_object_preserved")
            ),
            "basis_state_reader_type_preserved": bool(
                statement_map.get("basis_state_reader_type_preserved")
            ),
            "basis_state_reader_scope_preserved": bool(
                statement_map.get("basis_state_reader_scope_preserved")
            ),
            "allowed_commands_preserved": bool(
                statement_map.get("allowed_commands_preserved")
            ),
            "allowed_command_count_is_three": bool(
                statement_map.get("allowed_command_count_is_three")
            ),
            "state_command_may_be_considered": bool(
                statement_map.get("state_command_may_be_considered")
            ),
            "lookup_first_orientation_locator_command_may_be_considered": bool(
                statement_map.get("lookup_first_orientation_locator_command_may_be_considered")
            ),
            "lookup_second_orientation_locator_command_may_be_considered": bool(
                statement_map.get("lookup_second_orientation_locator_command_may_be_considered")
            ),
            "future_local_read_only_carrier_command_surface_may_be_considered": bool(
                statement_map.get("future_local_read_only_carrier_command_surface_may_be_considered")
            ),
            "boundary_object_summary": {
                "boundary_type": boundary_map.get("boundary_type"),
                "boundary_scope": boundary_map.get("boundary_scope"),
                "basis_reusable_lookup_permission_outcome": boundary_map.get(
                    "basis_reusable_lookup_permission_outcome"
                ),
                "basis_read_only_state_reader_outcome": boundary_map.get(
                    "basis_read_only_state_reader_outcome"
                ),
                "basis_state_packet_type": boundary_map.get("basis_state_packet_type"),
                "basis_state_reader_type": boundary_map.get("basis_state_reader_type"),
                "basis_state_reader_scope": boundary_map.get("basis_state_reader_scope"),
                "allowed_commands": boundary_map.get("allowed_commands"),
                "allowed_command_count": boundary_map.get("allowed_command_count"),
            },
            "local_carrier_command_surface_not_created": (
                non_claims_map.get("local_carrier_command_surface_created") is False
            ),
            "command_execution_not_performed": (
                non_claims_map.get("command_execution_performed") is False
            ),
            "operation_permission_not_created": (
                non_claims_map.get("operation_permission_created") is False
            ),
            "runtime_permission_not_created": (
                non_claims_map.get("runtime_permission_created") is False
            ),
            "public_api_not_created": non_claims_map.get("public_api_created") is False,
            "participant_facing_interface_not_created": (
                non_claims_map.get("participant_facing_interface_created") is False
            ),
            "distributed_network_behavior_not_created": (
                non_claims_map.get("distributed_network_behavior_created") is False
            ),
            "general_lookup_permission_not_created": (
                non_claims_map.get("general_lookup_permission_created") is False
            ),
            "arbitrary_lookup_permission_not_created": (
                non_claims_map.get("arbitrary_lookup_permission_created") is False
            ),
            "unsupported_commands_not_permitted": (
                non_claims_map.get("unsupported_commands_permitted") is False
            ),
            "unsupported_lookup_keys_not_permitted": (
                non_claims_map.get("unsupported_lookup_keys_permitted") is False
            ),
            "no_new_lookup_result_or_entry_created": (
                non_claims_map.get("new_lookup_result_created") is False
                and non_claims_map.get("new_lookup_entry_created") is False
            ),
            "no_new_signal_entry_relevance_object_or_index_entry_created": (
                non_claims_map.get("new_signal_accepted") is False
                and non_claims_map.get("new_entry_accepted") is False
                and non_claims_map.get("new_relevance_object_created") is False
                and non_claims_map.get("new_index_entry_created") is False
            ),
            "filesystem_discovery_not_performed": (
                non_claims_map.get("filesystem_discovery_performed") is False
            ),
            "registry_search_query_surface_ranking_not_created": (
                non_claims_map.get("registry_created") is False
                and non_claims_map.get("search_surface_created") is False
                and non_claims_map.get("query_surface_created") is False
                and non_claims_map.get("ranking_surface_created") is False
            ),
            "scoring_priority_validity_truth_authority_currentness_judgment_not_created": (
                non_claims_map.get("scoring_surface_created") is False
                and non_claims_map.get("priority_surface_created") is False
                and non_claims_map.get("validity_judgment_created") is False
                and non_claims_map.get("truth_judgment_created") is False
                and non_claims_map.get("authority_judgment_created") is False
                and non_claims_map.get("currentness_judgment_created") is False
            ),
            "repeated_reception_permission_arbitrary_reception_feed_not_created": (
                non_claims_map.get("repeated_reception_permission_created") is False
                and non_claims_map.get("arbitrary_reception_created") is False
                and non_claims_map.get("feed_created") is False
            ),
            "source_authority_currentness_truth_action_synchronization_participation_participant_role_not_created": (
                non_claims_map.get("source_created") is False
                and non_claims_map.get("authority_created") is False
                and non_claims_map.get("currentness_created") is False
                and non_claims_map.get("truth_created") is False
                and non_claims_map.get("action_created") is False
                and non_claims_map.get("synchronization_created") is False
                and non_claims_map.get("participation_authorized") is False
                and non_claims_map.get("participant_role_created") is False
            ),
            "follow_on_not_created": non_claims_map.get("follow_on_work_authorized")
            is False,
            "key_non_claims": {
                key: non_claims_map.get(key)
                for key in (
                    "local_carrier_command_surface_created",
                    "command_execution_performed",
                    "operation_permission_created",
                    "runtime_permission_created",
                    "public_api_created",
                    "general_lookup_permission_created",
                    "arbitrary_lookup_permission_created",
                    "unsupported_commands_permitted",
                    "unsupported_lookup_keys_permitted",
                    "new_lookup_result_created",
                    "new_lookup_entry_created",
                    "filesystem_discovery_performed",
                    "follow_on_work_authorized",
                )
            },
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": all(
                non_claims_map.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
            ),
        }
    )


def build_declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_request(
    *,
    local_relevance_medium_read_only_local_carrier_command_surface_boundary_id: str = DEFAULT_BOUNDARY_ID,
    local_relevance_medium_read_only_local_carrier_command_surface_boundary_question: str | None = None,
    local_relevance_medium_read_only_local_carrier_command_surface_boundary_intent: str = INTENT_RECORD,
    selected_reusable_lookup_permission_artifact: Path | str = DEFAULT_REUSABLE_LOOKUP_PERMISSION_ARTIFACT,
    selected_read_only_state_reader_artifact: Path | str = DEFAULT_READ_ONLY_STATE_READER_ARTIFACT,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    allowed_commands: list[str] | None = None,
    allowed_command_count: int = 3,
    declared_non_claims: Mapping[str, bool] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    question = (
        local_relevance_medium_read_only_local_carrier_command_surface_boundary_question
        or CORE_QUESTION
    )
    request = {
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_id": (
            local_relevance_medium_read_only_local_carrier_command_surface_boundary_id
        ),
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_question": (
            question
        ),
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_intent": (
            local_relevance_medium_read_only_local_carrier_command_surface_boundary_intent
        ),
        "selected_reusable_lookup_permission_artifact": _string_or_empty(
            selected_reusable_lookup_permission_artifact
        ),
        "selected_read_only_state_reader_artifact": _string_or_empty(
            selected_read_only_state_reader_artifact
        ),
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "allowed_commands": copy.deepcopy(
            list(ALLOWED_COMMANDS) if allowed_commands is None else allowed_commands
        ),
        "allowed_command_count": allowed_command_count,
        "state_command_may_be_considered": True,
        "lookup_first_orientation_locator_command_may_be_considered": True,
        "lookup_second_orientation_locator_command_may_be_considered": True,
        "future_local_read_only_carrier_command_surface_may_be_considered": True,
        "declared_non_claims": dict(
            _canonical_non_claims() if declared_non_claims is None else declared_non_claims
        ),
    }
    request.update(extra_fields)
    return _sanitize(request)
