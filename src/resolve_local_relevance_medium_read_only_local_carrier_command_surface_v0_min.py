"""Resolve one local relevance medium read-only local carrier command surface.

This resolver reads one selected
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY artifact
as command-surface consideration basis, one selected
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION artifact as bounded
lookup-permission basis, and one selected
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER /
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET artifact as read-only state basis.

It records one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE
object only. The object is local, read-only, carrier-facing, and
closed-command-set-only. It records availability for exactly ``state``,
``lookup first_orientation_locator``, and
``lookup second_orientation_locator``. It does not execute commands, return
state, perform lookup, create command execution result, operation permission,
runtime permission, API, participant-facing interface, distributed behavior,
general lookup permission, arbitrary lookup permission, unsupported-command
permission, unsupported-key permission, new lookup result, new lookup entry,
registry, search, query surface, ranking, scoring, priority, validity
judgment, truth judgment, authority judgment, currentness judgment, repeated
reception permission, arbitrary reception, feed, source transfer, source
receipt, action, synchronization, participation, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyLocalCarrierCommandSurfaceV0MinError(Exception):
    """Bounded error for local carrier command surface handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min"
)

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_RECORDED"
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_surface_v0_min"
)
DEFAULT_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_surface_boundary_v0_min/"
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_"
    "reference_review_001__local_relevance_medium_read_only_local_carrier_"
    "command_surface_boundary_v0_min_result.json"
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

DEFAULT_COMMAND_SURFACE_ID = (
    "local_relevance_medium_read_only_local_carrier_command_surface_001"
)

COMMAND_SURFACE_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE"
COMMAND_SURFACE_SCOPE = "LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY"
SUPPORTED_COMMAND_SURFACE_TYPE_VALUES = (COMMAND_SURFACE_TYPE,)
SUPPORTED_COMMAND_SURFACE_SCOPE_VALUES = (COMMAND_SURFACE_SCOPE,)

LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_RECORDED"
)
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

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY, "
    "one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION, and one "
    "clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER / "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET basis, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE be recorded that "
    "exposes only the local read-only commands state, lookup first_orientation_locator, "
    "and lookup second_orientation_locator, without executing commands, creating "
    "command execution result, creating operation permission, creating runtime "
    "permission, creating public API, creating participant-facing interface, creating "
    "distributed network behavior, creating general lookup permission, creating "
    "arbitrary lookup permission, permitting unsupported commands, permitting "
    "unsupported lookup keys, creating new lookup result, creating new lookup entry, "
    "accepting new entries, accepting new signals, performing filesystem discovery, "
    "creating query surface, registry, search, ranking, scoring, priority, validity "
    "judgment, truth judgment, authority, currentness, action, synchronization, "
    "participation authorization, participant role, repeated reception permission, "
    "arbitrary reception, feed, source transfer, source receipt, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "command_execution_performed",
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
    "artifact_existence_treated_as_carrier_command_surface_authority",
    "latest_file_posture_treated_as_carrier_command_surface_authority",
    "repo_local_availability_treated_as_carrier_command_surface_authority",
    "hidden_repo_state_used_as_carrier_command_surface_content",
    "hidden_repo_state_used_as_carrier_command_surface_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

COMMAND_SURFACE_OBJECT_FALSE_FIELDS = (
    "command_execution_performed",
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
    "local_relevance_medium_read_only_local_carrier_command_surface_recorded",
    "basis_local_carrier_command_surface_boundary_artifact_preserved",
    "basis_reusable_lookup_permission_artifact_preserved",
    "basis_read_only_state_reader_artifact_preserved",
    "basis_state_packet_object_preserved",
    "basis_state_reader_type_preserved",
    "basis_state_reader_scope_preserved",
    "allowed_commands_preserved",
    "allowed_command_count_is_three",
    "state_command_available",
    "lookup_first_orientation_locator_command_available",
    "lookup_second_orientation_locator_command_available",
    "command_surface_local_only",
    "command_surface_read_only",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BLOCK_REQUESTED",
    "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_PATH_MISSING",
    "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_UNREADABLE",
    "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
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
    "STATE_COMMAND_NOT_AVAILABLE",
    "LOOKUP_FIRST_ORIENTATION_LOCATOR_COMMAND_NOT_AVAILABLE",
    "LOOKUP_SECOND_ORIENTATION_LOCATOR_COMMAND_NOT_AVAILABLE",
    "COMMAND_SURFACE_TYPE_MISSING",
    "COMMAND_SURFACE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE",
    "COMMAND_SURFACE_SCOPE_MISSING",
    "COMMAND_SURFACE_SCOPE_NOT_LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY",
    "LOCAL_CARRIER_COMMAND_SURFACE_NOT_RECORDED",
    "COMMAND_SURFACE_LOCAL_ONLY_NOT_TRUE",
    "COMMAND_SURFACE_READ_ONLY_NOT_TRUE",
    "COMMAND_EXECUTION_PERFORMED",
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
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_CARRIER_COMMAND_SURFACE_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_CARRIER_COMMAND_SURFACE_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_CARRIER_COMMAND_SURFACE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_CARRIER_COMMAND_SURFACE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_CARRIER_COMMAND_SURFACE_AUTHORITY",
    "PRIOR_ARTIFACTS_MUTATED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_REQUEST_UNREADABLE",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_local_carrier_command_surface_body",
    "raw_local_carrier_command_surface_boundary_body",
    "raw_command_execution_body",
    "raw_command_execution_result_body",
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
    "local_carrier_command_surface_body",
    "local_carrier_command_surface_boundary_body",
    "command_execution_body",
    "command_execution_result_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_SURFACE_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BODY_MUST_NOT_RETURN",
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

FALSE_FIELD_BLOCK_CODES = {
    "command_execution_performed": "COMMAND_EXECUTION_PERFORMED",
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
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
    "adoption_created": "ADOPTION_CREATED",
    "receiving_context_governance_created": "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "publication_flow_created": "PUBLICATION_FLOW_CREATED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "artifact_existence_treated_as_carrier_command_surface_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_CARRIER_COMMAND_SURFACE_AUTHORITY"
    ),
    "latest_file_posture_treated_as_carrier_command_surface_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_CARRIER_COMMAND_SURFACE_AUTHORITY"
    ),
    "repo_local_availability_treated_as_carrier_command_surface_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_CARRIER_COMMAND_SURFACE_AUTHORITY"
    ),
    "hidden_repo_state_used_as_carrier_command_surface_content": (
        "HIDDEN_REPO_STATE_USED_AS_CARRIER_COMMAND_SURFACE_CONTENT"
    ),
    "hidden_repo_state_used_as_carrier_command_surface_authority": (
        "HIDDEN_REPO_STATE_USED_AS_CARRIER_COMMAND_SURFACE_AUTHORITY"
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

SHORTCUT_FAILURES = {
    "local_carrier_command_surface_boundary_artifact_missing": (
        "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_PATH_MISSING"
    ),
    "local_carrier_command_surface_boundary_artifact_not_recorded": (
        "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_NOT_RECORDED"
    ),
    "local_carrier_command_surface_boundary_artifact_failed_checks_present": (
        "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "local_carrier_command_surface_boundary_artifact_version_not_0_1_0": (
        "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "reusable_lookup_permission_artifact_missing": (
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_PATH_MISSING"
    ),
    "reusable_lookup_permission_artifact_not_recorded": (
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_NOT_RECORDED"
    ),
    "reusable_lookup_permission_artifact_failed_checks_present": (
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "reusable_lookup_permission_artifact_version_not_0_1_0": (
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "read_only_state_reader_artifact_missing": "READ_ONLY_STATE_READER_ARTIFACT_PATH_MISSING",
    "read_only_state_reader_artifact_not_recorded": (
        "READ_ONLY_STATE_READER_ARTIFACT_NOT_RECORDED"
    ),
    "read_only_state_reader_artifact_failed_checks_present": (
        "READ_ONLY_STATE_READER_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "read_only_state_reader_artifact_version_not_0_1_0": (
        "READ_ONLY_STATE_READER_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "state_packet_object_missing": "READ_ONLY_STATE_PACKET_OBJECT_MISSING",
    "state_packet_type_not_local_relevance_medium_read_only_state_packet": (
        "STATE_PACKET_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET"
    ),
    "state_reader_type_not_local_relevance_medium_read_only_state_reader": (
        "STATE_READER_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER"
    ),
    "state_reader_scope_not_read_existing_local_relevance_medium_state_only": (
        "STATE_READER_SCOPE_NOT_READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY"
    ),
    "allowed_commands_not_exact": "ALLOWED_COMMANDS_NOT_EXACT",
    "allowed_command_count_not_three": "ALLOWED_COMMAND_COUNT_NOT_THREE",
    "state_command_not_available": "STATE_COMMAND_NOT_AVAILABLE",
    "lookup_first_orientation_locator_command_not_available": (
        "LOOKUP_FIRST_ORIENTATION_LOCATOR_COMMAND_NOT_AVAILABLE"
    ),
    "lookup_second_orientation_locator_command_not_available": (
        "LOOKUP_SECOND_ORIENTATION_LOCATOR_COMMAND_NOT_AVAILABLE"
    ),
    "command_surface_type_not_local_relevance_medium_read_only_local_carrier_command_surface": (
        "COMMAND_SURFACE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE"
    ),
    "command_surface_scope_not_local_read_only_state_and_two_lookup_commands_only": (
        "COMMAND_SURFACE_SCOPE_NOT_LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY"
    ),
    "local_carrier_command_surface_not_recorded": "LOCAL_CARRIER_COMMAND_SURFACE_NOT_RECORDED",
    "command_surface_local_only_not_true": "COMMAND_SURFACE_LOCAL_ONLY_NOT_TRUE",
    "command_surface_read_only_not_true": "COMMAND_SURFACE_READ_ONLY_NOT_TRUE",
}
SHORTCUT_FAILURES.update(FALSE_FIELD_BLOCK_CODES)

FORBIDDEN_OUTPUT_ROOTS = (
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
OFFICIAL_STRINGS.update(SUPPORTED_COMMAND_SURFACE_TYPE_VALUES)
OFFICIAL_STRINGS.update(SUPPORTED_COMMAND_SURFACE_SCOPE_VALUES)
OFFICIAL_STRINGS.update(ALLOWED_COMMANDS)
OFFICIAL_STRINGS.update(REQUIRED_FALSE_NON_CLAIMS)
OFFICIAL_STRINGS.update(ALLOWED_TRUE_RECORDED_FIELDS)
OFFICIAL_STRINGS.update(
    {
        RESULT_VERSION,
        RESOLVER_MODULE,
        DEFAULT_COMMAND_SURFACE_ID,
        LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_RECORDED_OUTCOME,
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
            else "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_REQUEST_MALFORMED"
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


def _mapping_at(artifact: Mapping[str, Any] | None, key: str) -> Mapping[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {}
    value = artifact.get(key)
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
        "local_relevance_medium_read_only_local_carrier_command_surface_question"
    )
    intent = declared.get(
        "local_relevance_medium_read_only_local_carrier_command_surface_intent"
    )
    command_surface_type = declared.get("command_surface_type")
    command_surface_scope = declared.get("command_surface_scope")

    _append_check(
        checks,
        "local carrier command surface question declared",
        _present(question),
        "declared local carrier command surface question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_QUESTION_UNDECLARED",
    )
    _append_check(
        checks,
        "command surface intent supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _append_check(
            checks,
            "local carrier command surface block intent not requested",
            False,
            f"not {INTENT_BLOCK}",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BLOCK_REQUESTED",
        )
    _append_check(
        checks,
        "command surface type declared",
        _present(command_surface_type),
        COMMAND_SURFACE_TYPE,
        command_surface_type,
        "COMMAND_SURFACE_TYPE_MISSING",
    )
    _append_check(
        checks,
        "command surface type exact",
        command_surface_type == COMMAND_SURFACE_TYPE,
        COMMAND_SURFACE_TYPE,
        command_surface_type,
        "COMMAND_SURFACE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE",
    )
    _append_check(
        checks,
        "command surface scope declared",
        _present(command_surface_scope),
        COMMAND_SURFACE_SCOPE,
        command_surface_scope,
        "COMMAND_SURFACE_SCOPE_MISSING",
    )
    _append_check(
        checks,
        "command surface scope local read-only state and two lookup commands only",
        command_surface_scope == COMMAND_SURFACE_SCOPE,
        COMMAND_SURFACE_SCOPE,
        command_surface_scope,
        "COMMAND_SURFACE_SCOPE_NOT_LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY",
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


def _append_allowed_command_checks(
    declared: Mapping[str, Any],
    boundary_object: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    declared_allowed_commands = declared.get("allowed_commands", list(ALLOWED_COMMANDS))
    boundary_allowed_commands = boundary_object.get("allowed_commands")
    allowed_commands_basis = (
        boundary_allowed_commands
        if isinstance(boundary_allowed_commands, list)
        else declared_allowed_commands
    )
    declared_command_count = declared.get(
        "allowed_command_count",
        len(declared_allowed_commands)
        if isinstance(declared_allowed_commands, list)
        else None,
    )
    boundary_command_count = boundary_object.get("allowed_command_count")
    command_count_basis = (
        boundary_command_count
        if isinstance(boundary_command_count, int) and not isinstance(boundary_command_count, bool)
        else declared_command_count
    )

    _append_check(
        checks,
        "allowed commands exact",
        declared_allowed_commands == list(ALLOWED_COMMANDS)
        and allowed_commands_basis == list(ALLOWED_COMMANDS),
        list(ALLOWED_COMMANDS),
        {
            "declared_allowed_commands": declared_allowed_commands,
            "basis_allowed_commands": allowed_commands_basis,
        },
        "ALLOWED_COMMANDS_NOT_EXACT",
    )
    _append_check(
        checks,
        "allowed command count exactly three",
        declared_command_count == 3 and command_count_basis == 3,
        3,
        {
            "declared_allowed_command_count": declared_command_count,
            "basis_allowed_command_count": command_count_basis,
        },
        "ALLOWED_COMMAND_COUNT_NOT_THREE",
    )

    state_available = declared.get("state_command_available", True) is True
    first_available = (
        declared.get("lookup_first_orientation_locator_command_available", True) is True
    )
    second_available = (
        declared.get("lookup_second_orientation_locator_command_available", True) is True
    )
    boundary_state_considered = boundary_object.get("state_command_may_be_considered", True) is True
    boundary_first_considered = (
        boundary_object.get("lookup_first_orientation_locator_command_may_be_considered", True)
        is True
    )
    boundary_second_considered = (
        boundary_object.get("lookup_second_orientation_locator_command_may_be_considered", True)
        is True
    )

    _append_check(
        checks,
        "state command available",
        state_available and boundary_state_considered,
        True,
        {
            "declared_state_command_available": declared.get(
                "state_command_available", True
            ),
            "basis_state_command_may_be_considered": boundary_object.get(
                "state_command_may_be_considered", True
            ),
        },
        "STATE_COMMAND_NOT_AVAILABLE",
    )
    _append_check(
        checks,
        "lookup first orientation locator command available",
        first_available and boundary_first_considered,
        True,
        {
            "declared_lookup_first_orientation_locator_command_available": declared.get(
                "lookup_first_orientation_locator_command_available", True
            ),
            "basis_lookup_first_orientation_locator_command_may_be_considered": (
                boundary_object.get(
                    "lookup_first_orientation_locator_command_may_be_considered",
                    True,
                )
            ),
        },
        "LOOKUP_FIRST_ORIENTATION_LOCATOR_COMMAND_NOT_AVAILABLE",
    )
    _append_check(
        checks,
        "lookup second orientation locator command available",
        second_available and boundary_second_considered,
        True,
        {
            "declared_lookup_second_orientation_locator_command_available": declared.get(
                "lookup_second_orientation_locator_command_available", True
            ),
            "basis_lookup_second_orientation_locator_command_may_be_considered": (
                boundary_object.get(
                    "lookup_second_orientation_locator_command_may_be_considered",
                    True,
                )
            ),
        },
        "LOOKUP_SECOND_ORIENTATION_LOCATOR_COMMAND_NOT_AVAILABLE",
    )


def _append_command_surface_posture_checks(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    _append_check(
        checks,
        "local carrier command surface recorded",
        declared.get("local_carrier_command_surface_recorded", True) is True,
        True,
        declared.get("local_carrier_command_surface_recorded", True),
        "LOCAL_CARRIER_COMMAND_SURFACE_NOT_RECORDED",
    )
    _append_check(
        checks,
        "command surface local only",
        declared.get("command_surface_local_only", True) is True,
        True,
        declared.get("command_surface_local_only", True),
        "COMMAND_SURFACE_LOCAL_ONLY_NOT_TRUE",
    )
    _append_check(
        checks,
        "command surface read only",
        declared.get("command_surface_read_only", True) is True,
        True,
        declared.get("command_surface_read_only", True),
        "COMMAND_SURFACE_READ_ONLY_NOT_TRUE",
    )


def _append_authority_exclusion_checks(checks: list[dict[str, Any]]) -> None:
    _append_check(
        checks,
        "artifact existence not carrier-command-surface authority",
        True,
        "artifact existence not treated as carrier-command-surface authority",
        False,
    )
    _append_check(
        checks,
        "latest file posture not carrier-command-surface authority",
        True,
        "latest file posture not treated as carrier-command-surface authority",
        False,
    )
    _append_check(
        checks,
        "repo-local availability not carrier-command-surface authority",
        True,
        "repo-local availability not treated as carrier-command-surface authority",
        False,
    )
    _append_check(
        checks,
        "hidden repo state not carrier-command-surface content or authority",
        True,
        "hidden repo state excluded from carrier-command-surface content and authority",
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


def _validate_local_carrier_command_surface_boundary_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, dict[str, Any], Mapping[str, Any]]:
    artifact_value = declared.get("selected_local_carrier_command_surface_boundary_artifact")
    path_text = _string_or_empty(artifact_value)
    _append_check(
        checks,
        "local carrier command surface boundary artifact path declared",
        _present(path_text),
        "selected local carrier command surface boundary artifact path",
        path_text,
        "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_PATH_MISSING",
    )
    artifact, read_code, path_text = _read_json_artifact(
        artifact_value,
        "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_PATH_MISSING",
        "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_UNREADABLE",
        "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    )
    if read_code:
        _append_check(
            checks,
            "local carrier command surface boundary artifact readable JSON object",
            False,
            "readable JSON object",
            path_text or artifact_value,
            read_code,
        )
        return None, _basis(path_text), {}

    assert artifact is not None
    boundary_object = _mapping_at(
        artifact, "local_relevance_medium_read_only_local_carrier_command_surface_boundary"
    )
    outcome = _artifact_outcome(
        artifact,
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata",
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_summary",
    )
    result_version = _artifact_result_version(
        artifact,
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata",
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_summary",
        boundary_object,
    )
    failed_check_count = _artifact_failed_check_count(
        artifact,
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata",
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_summary",
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_checks",
    )

    _append_check(
        checks,
        "local carrier command surface boundary artifact readable JSON object",
        True,
        "readable JSON object",
        path_text,
    )
    _append_check(
        checks,
        "local carrier command surface boundary artifact outcome recorded",
        outcome == LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_RECORDED_OUTCOME,
        LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_RECORDED_OUTCOME,
        outcome,
        "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "local carrier command surface boundary artifact result version 0.1.0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version,
        "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "local carrier command surface boundary artifact failed check count zero",
        failed_check_count == 0,
        0,
        failed_check_count,
        "LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    return (
        artifact,
        _basis(path_text, outcome, result_version, failed_check_count),
        boundary_object,
    )


def _validate_reusable_lookup_permission_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, dict[str, Any]]:
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
        return None, _basis(path_text)

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
    )
    failed_check_count = _artifact_failed_check_count(
        artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_summary",
        "local_relevance_medium_read_only_reusable_lookup_permission_checks",
    )

    _append_check(
        checks,
        "reusable lookup permission artifact readable JSON object",
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
        failed_check_count == 0,
        0,
        failed_check_count,
        "REUSABLE_LOOKUP_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    return artifact, _basis(path_text, outcome, result_version, failed_check_count)


def _validate_read_only_state_reader_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, dict[str, Any], dict[str, Any]]:
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
        return None, _basis(path_text), {}

    assert artifact is not None
    state_packet = _mapping_at(artifact, "local_relevance_medium_read_only_state_packet")
    state_reader = _mapping_at(artifact, "local_relevance_medium_read_only_state_reader")
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
    failed_check_count = _artifact_failed_check_count(
        artifact,
        "local_relevance_medium_read_only_state_reader_metadata",
        "local_relevance_medium_read_only_state_reader_summary",
        "local_relevance_medium_read_only_state_reader_checks",
    )
    state_packet_type = _first_string(
        state_packet,
        artifact,
        keys=("state_packet_type", "basis_state_packet_type"),
    )
    state_reader_type = _first_string(
        state_packet,
        state_reader,
        artifact,
        keys=("state_reader_type", "basis_state_reader_type"),
    )
    state_reader_scope = _first_string(
        state_packet,
        state_reader,
        artifact,
        keys=("state_reader_scope", "basis_state_reader_scope"),
    )

    _append_check(
        checks,
        "read-only state reader artifact readable JSON object",
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
        failed_check_count == 0,
        0,
        failed_check_count,
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
        "state packet type is LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
        state_packet_type == STATE_PACKET_TYPE,
        STATE_PACKET_TYPE,
        state_packet_type,
        "STATE_PACKET_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
    )
    _append_check(
        checks,
        "state reader type is LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
        state_reader_type == STATE_READER_TYPE,
        STATE_READER_TYPE,
        state_reader_type,
        "STATE_READER_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
    )
    _append_check(
        checks,
        "state reader scope is READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
        state_reader_scope == STATE_READER_SCOPE,
        STATE_READER_SCOPE,
        state_reader_scope,
        "STATE_READER_SCOPE_NOT_READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
    )
    state_values = {
        "basis_state_packet_type": state_packet_type,
        "basis_state_reader_type": state_reader_type,
        "basis_state_reader_scope": state_reader_scope,
    }
    return (
        artifact,
        _basis(path_text, outcome, result_version, failed_check_count),
        state_values,
    )


def _first_string(*sources: Mapping[str, Any], keys: tuple[str, ...]) -> str | None:
    for source in sources:
        if not isinstance(source, MappingABC):
            continue
        for key in keys:
            value = source.get(key)
            if isinstance(value, str):
                return value
    return None


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


def _build_command_surface_object(
    declared: Mapping[str, Any],
    boundary_basis: Mapping[str, Any],
    reusable_basis: Mapping[str, Any],
    state_basis: Mapping[str, Any],
    state_values: Mapping[str, Any],
    recorded: bool,
) -> dict[str, Any]:
    command_surface = {
        "command_surface_id": _string_or_empty(
            declared.get(
                "local_relevance_medium_read_only_local_carrier_command_surface_id",
                DEFAULT_COMMAND_SURFACE_ID,
            )
        )
        or DEFAULT_COMMAND_SURFACE_ID,
        "command_surface_type": COMMAND_SURFACE_TYPE,
        "command_surface_version": RESULT_VERSION,
        "command_surface_scope": COMMAND_SURFACE_SCOPE,
        "basis_local_carrier_command_surface_boundary_artifact": boundary_basis.get(
            "artifact_path", ""
        ),
        "basis_local_carrier_command_surface_boundary_outcome": boundary_basis.get(
            "outcome"
        ),
        "basis_local_carrier_command_surface_boundary_result_version": boundary_basis.get(
            "result_version"
        ),
        "basis_local_carrier_command_surface_boundary_failed_check_count": (
            boundary_basis.get("failed_check_count")
        ),
        "basis_reusable_lookup_permission_artifact": reusable_basis.get("artifact_path", ""),
        "basis_reusable_lookup_permission_outcome": reusable_basis.get("outcome"),
        "basis_reusable_lookup_permission_result_version": reusable_basis.get(
            "result_version"
        ),
        "basis_reusable_lookup_permission_failed_check_count": reusable_basis.get(
            "failed_check_count"
        ),
        "basis_read_only_state_reader_artifact": state_basis.get("artifact_path", ""),
        "basis_read_only_state_reader_outcome": state_basis.get("outcome"),
        "basis_read_only_state_reader_result_version": state_basis.get("result_version"),
        "basis_read_only_state_reader_failed_check_count": state_basis.get(
            "failed_check_count"
        ),
        "basis_state_packet_type": state_values.get("basis_state_packet_type"),
        "basis_state_reader_type": state_values.get("basis_state_reader_type"),
        "basis_state_reader_scope": state_values.get("basis_state_reader_scope"),
        "allowed_commands": list(ALLOWED_COMMANDS),
        "allowed_command_count": len(ALLOWED_COMMANDS),
        "state_command_available": bool(recorded),
        "lookup_first_orientation_locator_command_available": bool(recorded),
        "lookup_second_orientation_locator_command_available": bool(recorded),
        "local_carrier_command_surface_recorded": bool(recorded),
        "command_surface_local_only": bool(recorded),
        "command_surface_read_only": bool(recorded),
    }
    for field_name in COMMAND_SURFACE_OBJECT_FALSE_FIELDS:
        command_surface[field_name] = False
    return command_surface


def _build_statement(
    outcome: str,
    command_surface: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {
        "local_relevance_medium_read_only_local_carrier_command_surface_recorded": recorded,
        "basis_local_carrier_command_surface_boundary_artifact_preserved": recorded
        and command_surface.get("basis_local_carrier_command_surface_boundary_outcome")
        == LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_RECORDED_OUTCOME
        and command_surface.get(
            "basis_local_carrier_command_surface_boundary_result_version"
        )
        == RESULT_VERSION
        and command_surface.get(
            "basis_local_carrier_command_surface_boundary_failed_check_count"
        )
        == 0,
        "basis_reusable_lookup_permission_artifact_preserved": recorded
        and command_surface.get("basis_reusable_lookup_permission_outcome")
        == REUSABLE_LOOKUP_PERMISSION_RECORDED_OUTCOME
        and command_surface.get("basis_reusable_lookup_permission_result_version")
        == RESULT_VERSION
        and command_surface.get("basis_reusable_lookup_permission_failed_check_count") == 0,
        "basis_read_only_state_reader_artifact_preserved": recorded
        and command_surface.get("basis_read_only_state_reader_outcome")
        == READ_ONLY_STATE_READER_RECORDED_OUTCOME
        and command_surface.get("basis_read_only_state_reader_result_version")
        == RESULT_VERSION
        and command_surface.get("basis_read_only_state_reader_failed_check_count") == 0,
        "basis_state_packet_object_preserved": recorded
        and command_surface.get("basis_state_packet_type") == STATE_PACKET_TYPE,
        "basis_state_reader_type_preserved": recorded
        and command_surface.get("basis_state_reader_type") == STATE_READER_TYPE,
        "basis_state_reader_scope_preserved": recorded
        and command_surface.get("basis_state_reader_scope") == STATE_READER_SCOPE,
        "allowed_commands_preserved": recorded
        and command_surface.get("allowed_commands") == list(ALLOWED_COMMANDS),
        "allowed_command_count_is_three": recorded
        and command_surface.get("allowed_command_count") == 3,
        "state_command_available": recorded
        and command_surface.get("state_command_available") is True,
        "lookup_first_orientation_locator_command_available": recorded
        and command_surface.get("lookup_first_orientation_locator_command_available")
        is True,
        "lookup_second_orientation_locator_command_available": recorded
        and command_surface.get("lookup_second_orientation_locator_command_available")
        is True,
        "command_surface_local_only": recorded
        and command_surface.get("command_surface_local_only") is True,
        "command_surface_read_only": recorded
        and command_surface.get("command_surface_read_only") is True,
        "result_level_non_claims_canonical_false": all(
            key in non_claims and non_claims[key] is False
            for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }
    return statement


def _build_non_meaning(non_claims: Mapping[str, bool]) -> dict[str, Any]:
    return {
        "command_surface_executes_commands": False,
        "command_surface_returns_state": False,
        "command_surface_performs_lookup": False,
        "command_surface_creates_command_execution_result": False,
        "command_surface_creates_operation_permission": False,
        "command_surface_creates_runtime_permission": False,
        "command_surface_creates_public_api": False,
        "command_surface_creates_participant_facing_interface": False,
        "command_surface_creates_distributed_network_behavior": False,
        "command_surface_creates_general_lookup_permission": False,
        "command_surface_creates_arbitrary_lookup_permission": False,
        "command_surface_permits_unsupported_commands": False,
        "command_surface_permits_unsupported_lookup_keys": False,
        "command_surface_creates_new_lookup_result": False,
        "command_surface_creates_new_lookup_entry": False,
        "command_surface_performs_filesystem_discovery": False,
        "command_surface_authorizes_follow_on_work": False,
        "result_level_non_claims": dict(non_claims),
    }


def _determine_outcome(
    declared: Mapping[str, Any],
    checks: list[Mapping[str, Any]],
) -> str:
    if _first_failed_code(checks):
        return OUTCOME_BLOCKED
    requested = declared.get(
        "requested_local_relevance_medium_read_only_local_carrier_command_surface_outcome"
    )
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or declared.get(
        "additional_basis_context"
    ):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if requested == OUTCOME_NOT_RECORDED or declared.get("not_recorded_basis"):
        return OUTCOME_NOT_RECORDED
    if (
        declared.get(
            "local_relevance_medium_read_only_local_carrier_command_surface_intent"
        )
        == INTENT_DO_NOT_RECORD
    ):
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _finalize_result(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
    boundary_basis: Mapping[str, Any] | None = None,
    reusable_basis: Mapping[str, Any] | None = None,
    state_basis: Mapping[str, Any] | None = None,
    state_values: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    boundary_basis = dict(boundary_basis or _basis(""))
    reusable_basis = dict(reusable_basis or _basis(""))
    state_basis = dict(state_basis or _basis(""))
    state_values = dict(state_values or {})

    outcome = _determine_outcome(declared, checks)
    recorded = outcome == OUTCOME_RECORDED
    command_surface = _build_command_surface_object(
        declared,
        boundary_basis,
        reusable_basis,
        state_basis,
        state_values,
        recorded,
    )
    statement = _build_statement(outcome, command_surface, non_claims)
    passed_count, failed_count = _check_counts(checks)
    block_code = _first_failed_code(checks)
    block = None
    if outcome == OUTCOME_BLOCKED:
        block = {
            "blocked": True,
            "block_code": block_code
            or "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_REQUEST_MALFORMED",
            "reason": _sanitize(declared.get("block_reason", "blocked by bounded check")),
        }

    metadata = {
        "local_relevance_medium_read_only_local_carrier_command_surface_id": (
            command_surface["command_surface_id"]
        ),
        "local_relevance_medium_read_only_local_carrier_command_surface_type": (
            COMMAND_SURFACE_TYPE
        ),
        "local_relevance_medium_read_only_local_carrier_command_surface_version": (
            RESULT_VERSION
        ),
        "generated_at": _utc_timestamp(),
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
    }

    result: dict[str, Any] = {
        "local_relevance_medium_read_only_local_carrier_command_surface_metadata": metadata,
        "declared_local_relevance_medium_read_only_local_carrier_command_surface_question": {
            "question": _sanitize(
                declared.get(
                    "local_relevance_medium_read_only_local_carrier_command_surface_question"
                )
            ),
            "intent": _sanitize(
                declared.get(
                    "local_relevance_medium_read_only_local_carrier_command_surface_intent"
                )
            ),
            "command_surface_type": COMMAND_SURFACE_TYPE,
            "command_surface_scope": COMMAND_SURFACE_SCOPE,
        },
        "selected_local_carrier_command_surface_boundary_artifact_basis": dict(
            boundary_basis
        ),
        "selected_reusable_lookup_permission_artifact_basis": dict(reusable_basis),
        "selected_read_only_state_reader_artifact_basis": dict(state_basis),
        "local_relevance_medium_read_only_local_carrier_command_surface": command_surface,
        "local_relevance_medium_read_only_local_carrier_command_surface_checks": checks,
        "local_relevance_medium_read_only_local_carrier_command_surface_statement": statement,
        "local_relevance_medium_read_only_local_carrier_command_surface_non_meaning": (
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
    result["local_relevance_medium_read_only_local_carrier_command_surface_summary"] = (
        build_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_summary(
            result
        )
    )
    return result


def resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min(
    declared_local_relevance_medium_read_only_local_carrier_command_surface: Mapping[
        str, Any
    ]
    | None = None,
) -> dict:
    """Resolve one local read-only carrier command surface request."""

    if declared_local_relevance_medium_read_only_local_carrier_command_surface is None:
        declared = (
            build_declared_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_request()
        )
    elif isinstance(
        declared_local_relevance_medium_read_only_local_carrier_command_surface,
        MappingABC,
    ):
        declared = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_local_carrier_command_surface)
        )
    else:
        checks = [
            _make_check(
                "declared local carrier command surface request is mapping",
                False,
                "mapping",
                type(
                    declared_local_relevance_medium_read_only_local_carrier_command_surface
                ).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result({}, checks)

    checks: list[dict[str, Any]] = []
    _append_declared_request_checks(declared, checks)
    _append_shortcut_checks(declared, checks)
    _append_non_claim_checks(declared, checks)
    _append_false_posture_checks(declared, checks)

    _, boundary_basis, boundary_object = (
        _validate_local_carrier_command_surface_boundary_artifact(declared, checks)
    )
    _, reusable_basis = _validate_reusable_lookup_permission_artifact(declared, checks)
    _, state_basis, state_values = _validate_read_only_state_reader_artifact(
        declared, checks
    )

    _append_allowed_command_checks(declared, boundary_object, checks)
    _append_command_surface_posture_checks(declared, checks)
    _append_authority_exclusion_checks(checks)

    return _finalize_result(
        declared,
        checks,
        boundary_basis=boundary_basis,
        reusable_basis=reusable_basis,
        state_basis=state_basis,
        state_values=state_values,
    )


def resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_from_path(
    declared_local_relevance_medium_read_only_local_carrier_command_surface_path: Path | str,
) -> dict:
    """Read a declared request JSON object from a path and resolve it."""

    path = Path(declared_local_relevance_medium_read_only_local_carrier_command_surface_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            declared = json.load(handle)
    except Exception:
        checks = [
            _make_check(
                "declared local carrier command surface request readable",
                False,
                "readable JSON object",
                str(path),
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_REQUEST_UNREADABLE",
            )
        ]
        return _finalize_result({}, checks)
    if not isinstance(declared, MappingABC):
        checks = [
            _make_check(
                "declared local carrier command surface request is JSON object",
                False,
                "JSON object",
                type(declared).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result({}, checks)
    return resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min(
        declared
    )


def build_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact public summary from a resolver result."""

    metadata = _mapping_at(
        result, "local_relevance_medium_read_only_local_carrier_command_surface_metadata"
    )
    command_surface = _mapping_at(
        result, "local_relevance_medium_read_only_local_carrier_command_surface"
    )
    statement = _mapping_at(
        result, "local_relevance_medium_read_only_local_carrier_command_surface_statement"
    )
    checks = result.get("local_relevance_medium_read_only_local_carrier_command_surface_checks")
    check_list = checks if isinstance(checks, list) else []
    passed_count, failed_count = _check_counts(check_list)
    block = result.get("block")
    block_mapping = block if isinstance(block, MappingABC) else {}
    non_claims = _mapping_at(result, "non_claims")

    return {
        "outcome": result.get("outcome"),
        "block_code": block_mapping.get("block_code"),
        "block_reason": block_mapping.get("reason"),
        "command_surface_id": command_surface.get("command_surface_id")
        or metadata.get("local_relevance_medium_read_only_local_carrier_command_surface_id"),
        "question": _mapping_at(
            result,
            "declared_local_relevance_medium_read_only_local_carrier_command_surface_question",
        ).get("question"),
        "intent": _mapping_at(
            result,
            "declared_local_relevance_medium_read_only_local_carrier_command_surface_question",
        ).get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get("result_version", RESULT_VERSION),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "command_surface_recorded": command_surface.get(
            "local_carrier_command_surface_recorded"
        )
        is True,
        "basis_local_carrier_command_surface_boundary_artifact_preserved": (
            statement.get("basis_local_carrier_command_surface_boundary_artifact_preserved")
            is True
        ),
        "basis_reusable_lookup_permission_artifact_preserved": (
            statement.get("basis_reusable_lookup_permission_artifact_preserved") is True
        ),
        "basis_read_only_state_reader_artifact_preserved": (
            statement.get("basis_read_only_state_reader_artifact_preserved") is True
        ),
        "basis_state_packet_object_preserved": (
            statement.get("basis_state_packet_object_preserved") is True
        ),
        "basis_state_reader_type_preserved": (
            statement.get("basis_state_reader_type_preserved") is True
        ),
        "basis_state_reader_scope_preserved": (
            statement.get("basis_state_reader_scope_preserved") is True
        ),
        "allowed_commands_preserved": statement.get("allowed_commands_preserved") is True,
        "allowed_command_count_is_three": (
            statement.get("allowed_command_count_is_three") is True
        ),
        "state_command_available": statement.get("state_command_available") is True,
        "lookup_first_orientation_locator_command_available": (
            statement.get("lookup_first_orientation_locator_command_available") is True
        ),
        "lookup_second_orientation_locator_command_available": (
            statement.get("lookup_second_orientation_locator_command_available") is True
        ),
        "command_surface_local_only": statement.get("command_surface_local_only") is True,
        "command_surface_read_only": statement.get("command_surface_read_only") is True,
        "command_surface_object_summary": {
            "command_surface_type": command_surface.get("command_surface_type"),
            "command_surface_scope": command_surface.get("command_surface_scope"),
            "allowed_commands": command_surface.get("allowed_commands"),
            "allowed_command_count": command_surface.get("allowed_command_count"),
        },
        "command_execution_not_performed": non_claims.get("command_execution_performed")
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
                "follow_on_work_authorized",
            )
        },
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": statement.get(
            "result_level_non_claims_canonical_false"
        )
        is True,
    }


def write_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result as stable JSON without silently overwriting."""

    metadata = _mapping_at(
        result, "local_relevance_medium_read_only_local_carrier_command_surface_metadata"
    )
    command_surface_id = _string_or_empty(
        metadata.get("local_relevance_medium_read_only_local_carrier_command_surface_id")
    ) or DEFAULT_COMMAND_SURFACE_ID
    filename = (
        f"{command_surface_id}__"
        "local_relevance_medium_read_only_local_carrier_command_surface_v0_min_result.json"
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


def _ensure_not_forbidden_output_path(path: Path) -> Path:
    normalized = Path(path)
    parts = normalized.parts
    for forbidden in FORBIDDEN_OUTPUT_ROOTS:
        forbidden_parts = forbidden.parts
        if len(parts) >= len(forbidden_parts) and parts[: len(forbidden_parts)] == forbidden_parts:
            raise LocalRelevanceMediumReadOnlyLocalCarrierCommandSurfaceV0MinError(
                f"refusing to write local carrier command surface result under {forbidden}"
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


def build_declared_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_request(
    local_relevance_medium_read_only_local_carrier_command_surface_id: str = DEFAULT_COMMAND_SURFACE_ID,
    selected_local_carrier_command_surface_boundary_artifact: Path | str = DEFAULT_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT,
    selected_reusable_lookup_permission_artifact: Path | str = DEFAULT_REUSABLE_LOOKUP_PERMISSION_ARTIFACT,
    selected_read_only_state_reader_artifact: Path | str = DEFAULT_READ_ONLY_STATE_READER_ARTIFACT,
    command_surface_type: str = COMMAND_SURFACE_TYPE,
    command_surface_scope: str = COMMAND_SURFACE_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a bounded declared request for the local carrier command surface."""

    request: dict[str, Any] = {
        "local_relevance_medium_read_only_local_carrier_command_surface_id": (
            local_relevance_medium_read_only_local_carrier_command_surface_id
        ),
        "local_relevance_medium_read_only_local_carrier_command_surface_question": (
            CORE_QUESTION
        ),
        "local_relevance_medium_read_only_local_carrier_command_surface_intent": intent,
        "selected_local_carrier_command_surface_boundary_artifact": str(
            selected_local_carrier_command_surface_boundary_artifact
        ),
        "selected_reusable_lookup_permission_artifact": str(
            selected_reusable_lookup_permission_artifact
        ),
        "selected_read_only_state_reader_artifact": str(
            selected_read_only_state_reader_artifact
        ),
        "command_surface_type": command_surface_type,
        "command_surface_scope": command_surface_scope,
        "allowed_commands": list(ALLOWED_COMMANDS),
        "allowed_command_count": len(ALLOWED_COMMANDS),
        "state_command_available": True,
        "lookup_first_orientation_locator_command_available": True,
        "lookup_second_orientation_locator_command_available": True,
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
