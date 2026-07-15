"""Resolve one local read-only selected-state runtime.

This resolver reads one clean
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY artifact, one clean
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION artifact, and one clean
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION artifact. It records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME object only.

The object is runtime-shaped, local, read-only, selected-state-only,
closure-token-aware, non-hosting-shaped, non-loop-shaped, non-daemon-shaped,
and older-runtime-authority-import-refusing. It creates no runtime hosting,
runtime loop, daemon behavior, continuation, runtime-held state, runtime-held
re-entry, second operation, prior-result re-entry cycle, public API,
participant-facing interface, distributed behavior, registry/search/query/
ranking surface, source movement, older runtime authority import, or follow-on
work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyRuntimeV0MinError(RuntimeError):
    """Bounded resolver error for runtime request/path handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_runtime_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_v0_min"
)
DEFAULT_RUNTIME_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_boundary_v0_min_v2/"
    "local_relevance_medium_read_only_runtime_boundary_reference_review_001__"
    "local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
)
DEFAULT_RUNTIME_PERMISSION_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_permission_v0_min/"
    "local_relevance_medium_read_only_runtime_permission_reference_review_001__"
    "local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
)
DEFAULT_OPERATION_EXECUTION_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_execution_v0_min/"
    "local_relevance_medium_read_only_operation_execution_reference_review_001__"
    "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
)

DEFAULT_RUNTIME_ID = "local_relevance_medium_read_only_runtime_001"
RUNTIME_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME"
RUNTIME_SCOPE = "SELECTED_RUNTIME_ONLY"
SUPPORTED_RUNTIME_TYPE_VALUES = (RUNTIME_TYPE,)
SUPPORTED_RUNTIME_SCOPE_VALUES = (RUNTIME_SCOPE,)
SELECTED_COMMAND = "state"

RUNTIME_BOUNDARY_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED"
)
RUNTIME_PERMISSION_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED"
)
OPERATION_EXECUTION_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED"
)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY for "
    "selected command state, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION, existing reusable "
    "read-only lookup permission, prior lookup-pair coverage, and prior local "
    "carrier command surface, may one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME "
    "be recorded for selected command state, without creating runtime hosting, "
    "creating runtime loop, creating daemon behavior, creating continuation, "
    "creating runtime-held state, creating runtime-held re-entry, creating "
    "second operation, creating prior-result re-entry cycle, creating public "
    "API, creating participant-facing interface, creating distributed network "
    "behavior, creating general operation permission, creating general lookup "
    "permission, creating arbitrary lookup permission, permitting unsupported "
    "commands, permitting unsupported lookup keys, creating new lookup entry "
    "beyond the already bounded selected-state lookup result object, accepting "
    "new entries, accepting new signals, performing filesystem discovery, "
    "importing older runtime/post-runtime authority, creating query surface, "
    "registry, search, ranking, scoring, priority, validity judgment, truth "
    "judgment, authority, currentness, synchronization, participation "
    "authorization, participant role, repeated reception permission, arbitrary "
    "reception, feed, source transfer, source receipt, or follow-on work?"
)

RUNTIME_OBJECT_FALSE_FIELDS = (
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "continuation_created",
    "runtime_held_state_created",
    "runtime_held_reentry_created",
    "second_operation_created",
    "prior_result_reentry_cycle_created",
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
    "older_runtime_lineage_imported_as_authority",
    "older_runtime_permission_treated_as_current",
    "runtime_authority_imported",
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
    "artifact_existence_treated_as_runtime_authority",
    "latest_file_posture_treated_as_runtime_authority",
    "repo_local_availability_treated_as_runtime_authority",
    "hidden_repo_state_used_as_runtime_content",
    "hidden_repo_state_used_as_runtime_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "runtime_boundary_v0_failure_repaired",
    "runtime_boundary_v0_failure_hidden",
    "runtime_boundary_v0_failure_claimed_passed",
)

REQUIRED_FALSE_NON_CLAIMS = RUNTIME_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_runtime_recorded",
    "basis_runtime_boundary_artifact_preserved",
    "basis_runtime_permission_artifact_preserved",
    "basis_operation_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_runtime_boundary_recorded",
    "future_runtime_may_be_considered",
    "selected_runtime_permission_recorded",
    "runtime_permission_created",
    "runtime_permission_local_only",
    "runtime_permission_read_only",
    "selected_operation_execution_recorded",
    "operation_execution_created",
    "operation_execution_performed",
    "operation_execution_local_only",
    "operation_execution_read_only",
    "runtime_created",
    "runtime_local_only",
    "runtime_read_only",
    "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BLOCK_REQUESTED",
    "RUNTIME_BOUNDARY_ARTIFACT_PATH_MISSING",
    "RUNTIME_BOUNDARY_ARTIFACT_UNREADABLE",
    "RUNTIME_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "RUNTIME_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "RUNTIME_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "RUNTIME_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "RUNTIME_PERMISSION_ARTIFACT_PATH_MISSING",
    "RUNTIME_PERMISSION_ARTIFACT_UNREADABLE",
    "RUNTIME_PERMISSION_ARTIFACT_NOT_JSON_OBJECT",
    "RUNTIME_PERMISSION_ARTIFACT_NOT_RECORDED",
    "RUNTIME_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "RUNTIME_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0",
    "OPERATION_EXECUTION_ARTIFACT_PATH_MISSING",
    "OPERATION_EXECUTION_ARTIFACT_UNREADABLE",
    "OPERATION_EXECUTION_ARTIFACT_NOT_JSON_OBJECT",
    "OPERATION_EXECUTION_ARTIFACT_NOT_RECORDED",
    "OPERATION_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "OPERATION_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_RUNTIME_BOUNDARY_NOT_RECORDED",
    "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED",
    "SELECTED_RUNTIME_PERMISSION_NOT_RECORDED",
    "RUNTIME_PERMISSION_NOT_CREATED",
    "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE",
    "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE",
    "SELECTED_OPERATION_EXECUTION_NOT_RECORDED",
    "OPERATION_EXECUTION_NOT_CREATED",
    "OPERATION_EXECUTION_NOT_PERFORMED",
    "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE",
    "RUNTIME_TYPE_MISSING",
    "RUNTIME_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME",
    "RUNTIME_SCOPE_MISSING",
    "RUNTIME_SCOPE_NOT_SELECTED_RUNTIME_ONLY",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_NOT_RECORDED",
    "RUNTIME_NOT_CREATED",
    "RUNTIME_LOCAL_ONLY_NOT_TRUE",
    "RUNTIME_READ_ONLY_NOT_TRUE",
    "RUNTIME_HOSTING_CREATED",
    "RUNTIME_LOOP_CREATED",
    "DAEMON_BEHAVIOR_CREATED",
    "CONTINUATION_CREATED",
    "RUNTIME_HELD_STATE_CREATED",
    "RUNTIME_HELD_REENTRY_CREATED",
    "SECOND_OPERATION_CREATED",
    "PRIOR_RESULT_REENTRY_CYCLE_CREATED",
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
    "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
    "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
    "RUNTIME_AUTHORITY_IMPORTED",
    "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
    "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN",
    "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_REQUEST_UNREADABLE",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_runtime_body",
    "raw_runtime_boundary_body",
    "raw_runtime_permission_body",
    "raw_runtime_permission_boundary_body",
    "raw_runtime_hosting_body",
    "raw_runtime_loop_body",
    "raw_daemon_body",
    "raw_continuation_body",
    "raw_runtime_held_state_body",
    "raw_runtime_held_reentry_body",
    "raw_second_operation_body",
    "raw_prior_result_reentry_body",
    "raw_operation_execution_body",
    "raw_operation_execution_boundary_body",
    "raw_operation_permission_body",
    "raw_operation_permission_boundary_body",
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
    "runtime_body",
    "runtime_boundary_body",
    "runtime_permission_body",
    "runtime_permission_boundary_body",
    "runtime_hosting_body",
    "runtime_loop_body",
    "daemon_body",
    "continuation_body",
    "runtime_held_state_body",
    "runtime_held_reentry_body",
    "second_operation_body",
    "prior_result_reentry_body",
    "operation_execution_body",
    "operation_execution_boundary_body",
    "operation_permission_body",
    "operation_permission_boundary_body",
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

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_STATE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "RAW_PRIOR_RESULT_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
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
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

TOP_LEVEL_BLOCK_FLAG_CODES = {
    "runtime_boundary_artifact_missing": "RUNTIME_BOUNDARY_ARTIFACT_PATH_MISSING",
    "runtime_boundary_artifact_not_recorded": "RUNTIME_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "runtime_boundary_artifact_failed_checks_present": "RUNTIME_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_boundary_artifact_version_not_0_1_0": "RUNTIME_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_permission_artifact_missing": "RUNTIME_PERMISSION_ARTIFACT_PATH_MISSING",
    "runtime_permission_artifact_not_recorded": "RUNTIME_PERMISSION_ARTIFACT_NOT_RECORDED",
    "runtime_permission_artifact_failed_checks_present": "RUNTIME_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_permission_artifact_version_not_0_1_0": "RUNTIME_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0",
    "operation_execution_artifact_missing": "OPERATION_EXECUTION_ARTIFACT_PATH_MISSING",
    "operation_execution_artifact_not_recorded": "OPERATION_EXECUTION_ARTIFACT_NOT_RECORDED",
    "operation_execution_artifact_failed_checks_present": "OPERATION_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "operation_execution_artifact_version_not_0_1_0": "OPERATION_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0",
    "selected_command_missing": "SELECTED_COMMAND_MISSING",
    "selected_command_not_state": "SELECTED_COMMAND_NOT_STATE",
    "selected_runtime_boundary_not_recorded": "SELECTED_RUNTIME_BOUNDARY_NOT_RECORDED",
    "future_runtime_may_not_be_considered": "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED",
    "selected_runtime_permission_not_recorded": "SELECTED_RUNTIME_PERMISSION_NOT_RECORDED",
    "runtime_permission_not_created": "RUNTIME_PERMISSION_NOT_CREATED",
    "runtime_permission_local_only_not_true": "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE",
    "runtime_permission_read_only_not_true": "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE",
    "selected_operation_execution_not_recorded": "SELECTED_OPERATION_EXECUTION_NOT_RECORDED",
    "operation_execution_not_created": "OPERATION_EXECUTION_NOT_CREATED",
    "operation_execution_not_performed": "OPERATION_EXECUTION_NOT_PERFORMED",
    "operation_execution_local_only_not_true": "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    "operation_execution_read_only_not_true": "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE",
    "runtime_type_not_local_relevance_medium_read_only_runtime": "RUNTIME_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME",
    "runtime_scope_not_selected_runtime_only": "RUNTIME_SCOPE_NOT_SELECTED_RUNTIME_ONLY",
    "local_relevance_medium_read_only_runtime_not_recorded": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_NOT_RECORDED",
    "runtime_not_created": "RUNTIME_NOT_CREATED",
    "runtime_local_only_not_true": "RUNTIME_LOCAL_ONLY_NOT_TRUE",
    "runtime_read_only_not_true": "RUNTIME_READ_ONLY_NOT_TRUE",
    "runtime_hosting_created": "RUNTIME_HOSTING_CREATED",
    "runtime_loop_created": "RUNTIME_LOOP_CREATED",
    "daemon_behavior_created": "DAEMON_BEHAVIOR_CREATED",
    "continuation_created": "CONTINUATION_CREATED",
    "runtime_held_state_created": "RUNTIME_HELD_STATE_CREATED",
    "runtime_held_reentry_created": "RUNTIME_HELD_REENTRY_CREATED",
    "second_operation_created": "SECOND_OPERATION_CREATED",
    "prior_result_reentry_cycle_created": "PRIOR_RESULT_REENTRY_CYCLE_CREATED",
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
    "older_runtime_lineage_imported_as_authority": "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
    "older_runtime_permission_treated_as_current": "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
    "runtime_authority_imported": "RUNTIME_AUTHORITY_IMPORTED",
    "runtime_boundary_v0_failure_repaired": "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
    "runtime_boundary_v0_failure_hidden": "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN",
    "runtime_boundary_v0_failure_claimed_passed": "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
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
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "artifact_existence_treated_as_runtime_authority": "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_AUTHORITY",
    "latest_file_posture_treated_as_runtime_authority": "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_AUTHORITY",
    "repo_local_availability_treated_as_runtime_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_AUTHORITY",
    "hidden_repo_state_used_as_runtime_content": "HIDDEN_REPO_STATE_USED_AS_RUNTIME_CONTENT",
    "hidden_repo_state_used_as_runtime_authority": "HIDDEN_REPO_STATE_USED_AS_RUNTIME_AUTHORITY",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _contains_hostile_sentinel(value: str) -> bool:
    return any(sentinel in value for sentinel in HOSTILE_SENTINELS)


def _is_sensitive_key(key: Any) -> bool:
    lowered = str(key).lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _sanitize(value: Any, key: Any | None = None) -> Any:
    if key is not None and _is_sensitive_key(key):
        return "[REDACTED_SENSITIVE_RUNTIME_CONTENT]"
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if _contains_hostile_sentinel(value):
            return "[REDACTED_SENSITIVE_RUNTIME_CONTENT]"
        return value
    if isinstance(value, MappingABC):
        return {str(k): _sanitize(v, k) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    return value


def _as_mapping(value: Any) -> Mapping[str, Any] | None:
    if isinstance(value, MappingABC):
        return value
    return None


def _iter_key_values(value: Any):
    if isinstance(value, MappingABC):
        for key, item in value.items():
            yield str(key), item
            yield from _iter_key_values(item)
    elif isinstance(value, list):
        for item in value:
            yield from _iter_key_values(item)


def _first_recursive_value(value: Any, keys: tuple[str, ...]) -> Any:
    if isinstance(value, MappingABC):
        for key in keys:
            if key in value:
                return value[key]
        for section_key, section in value.items():
            if str(section_key).endswith("_metadata") and isinstance(section, MappingABC):
                for key in keys:
                    if key in section:
                        return section[key]
        for section_key, section in value.items():
            if str(section_key).endswith("_summary") and isinstance(section, MappingABC):
                for key in keys:
                    if key in section:
                        return section[key]
        for item in value.values():
            found = _first_recursive_value(item, keys)
            if found is not None:
                return found
    elif isinstance(value, list):
        for item in value:
            found = _first_recursive_value(item, keys)
            if found is not None:
                return found
    return None


def _artifact_outcome(artifact: Mapping[str, Any] | None) -> Any:
    if artifact is None:
        return None
    return artifact.get("outcome")


def _artifact_result_version(artifact: Mapping[str, Any] | None) -> Any:
    if artifact is None:
        return None
    if "result_version" in artifact:
        return artifact["result_version"]
    for section_key, section in artifact.items():
        if str(section_key).endswith("_metadata") and isinstance(section, MappingABC):
            if "result_version" in section:
                return section["result_version"]
    for section_key, section in artifact.items():
        if str(section_key).endswith("_summary") and isinstance(section, MappingABC):
            if "result_version" in section:
                return section["result_version"]
    return _first_recursive_value(artifact, ("result_version",))


def _artifact_failed_check_count(artifact: Mapping[str, Any] | None) -> Any:
    if artifact is None:
        return None
    direct = artifact.get("failed_check_count")
    if isinstance(direct, int) and not isinstance(direct, bool):
        return direct
    for section_key, section in artifact.items():
        if str(section_key).endswith("_metadata") and isinstance(section, MappingABC):
            found = section.get("failed_check_count")
            if isinstance(found, int) and not isinstance(found, bool):
                return found
    for section_key, section in artifact.items():
        if str(section_key).endswith("_summary") and isinstance(section, MappingABC):
            found = section.get("failed_check_count")
            if isinstance(found, int) and not isinstance(found, bool):
                return found
    for key, value in _iter_key_values(artifact):
        if key.endswith("_checks") and isinstance(value, list):
            return sum(
                1
                for check in value
                if isinstance(check, MappingABC) and check.get("passed") is False
            )
    found = _first_recursive_value(artifact, ("failed_check_count",))
    if isinstance(found, int) and not isinstance(found, bool):
        return found
    return found


def _present_true_without_false(
    artifact: Mapping[str, Any] | None, field_names: tuple[str, ...]
) -> bool:
    if artifact is None:
        return False
    found_true = False
    for key, value in _iter_key_values(artifact):
        if key in field_names:
            if value is False:
                return False
            if value is not True:
                return False
            found_true = True
    return found_true


def _read_json_object(path_value: Any) -> tuple[Mapping[str, Any] | None, str | None, Any]:
    if path_value in (None, ""):
        return None, "PATH_MISSING", path_value
    try:
        with Path(path_value).open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception as exc:  # noqa: BLE001 - bounded public resolver error surface
        return None, "UNREADABLE", f"{type(exc).__name__}: {exc}"
    if not isinstance(loaded, MappingABC):
        return None, "NOT_JSON_OBJECT", type(loaded).__name__
    return copy.deepcopy(dict(loaded)), None, "readable JSON object"


def _new_check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> dict[str, Any]:
    check = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
    }
    if not passed:
        check["block_code"] = code
        check["failure_code"] = code
    return check


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _basis_artifact_summary(
    path_value: Any,
    artifact: Mapping[str, Any] | None,
    expected_outcome: str,
) -> dict[str, Any]:
    return {
        "artifact": str(path_value) if path_value not in (None, "") else None,
        "artifact_read": artifact is not None,
        "artifact_body_embedded": False,
        "outcome": _artifact_outcome(artifact),
        "expected_outcome": expected_outcome,
        "result_version": _artifact_result_version(artifact),
        "failed_check_count": _artifact_failed_check_count(artifact),
        "result_version_expected": RESULT_VERSION,
        "failed_check_count_expected": 0,
    }


def build_declared_local_relevance_medium_read_only_runtime_v0_min_request(
    local_relevance_medium_read_only_runtime_id: str = DEFAULT_RUNTIME_ID,
    selected_runtime_boundary_artifact: Path | str | None = None,
    selected_runtime_permission_artifact: Path | str | None = None,
    selected_operation_execution_artifact: Path | str | None = None,
    selected_command: str = SELECTED_COMMAND,
    runtime_type: str = RUNTIME_TYPE,
    runtime_scope: str = RUNTIME_SCOPE,
    local_relevance_medium_read_only_runtime_intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    """Build a deterministic declared runtime request."""

    if selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyRuntimeV0MinError(
            "selected command must be exactly state"
        )
    request_non_claims = _canonical_false_non_claims()
    if declared_non_claims is not None:
        request_non_claims.update(copy.deepcopy(dict(declared_non_claims)))
    request = {
        "local_relevance_medium_read_only_runtime_id": (
            local_relevance_medium_read_only_runtime_id
        ),
        "local_relevance_medium_read_only_runtime_question": CORE_QUESTION,
        "local_relevance_medium_read_only_runtime_intent": (
            local_relevance_medium_read_only_runtime_intent
        ),
        "selected_runtime_boundary_artifact": str(
            selected_runtime_boundary_artifact or DEFAULT_RUNTIME_BOUNDARY_ARTIFACT
        ),
        "selected_runtime_permission_artifact": str(
            selected_runtime_permission_artifact or DEFAULT_RUNTIME_PERMISSION_ARTIFACT
        ),
        "selected_operation_execution_artifact": str(
            selected_operation_execution_artifact or DEFAULT_OPERATION_EXECUTION_ARTIFACT
        ),
        "selected_command": SELECTED_COMMAND,
        "runtime_type": runtime_type,
        "runtime_scope": runtime_scope,
        "declared_non_claims": request_non_claims,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
        "older_runtime_lineage_imported_as_authority": False,
        "older_runtime_permission_treated_as_current": False,
        "runtime_authority_imported": False,
        "runtime_boundary_v0_failure_repaired": False,
        "runtime_boundary_v0_failure_hidden": False,
        "runtime_boundary_v0_failure_claimed_passed": False,
        "predecessor_failure_repaired": False,
        "predecessor_failure_hidden": False,
        "predecessor_failure_claimed_passed": False,
        "artifact_existence_treated_as_runtime_authority": False,
        "latest_file_posture_treated_as_runtime_authority": False,
        "repo_local_availability_treated_as_runtime_authority": False,
        "hidden_repo_state_used_as_runtime_content": False,
        "hidden_repo_state_used_as_runtime_authority": False,
        "prior_artifacts_mutated": False,
        "follow_on_work_authorized": False,
    }
    request.update(copy.deepcopy(extra_fields))
    return request


def _validate_declared_non_claims(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    declared = request.get("declared_non_claims")
    bad_keys: list[str] = []
    if not isinstance(declared, MappingABC):
        bad_keys = list(REQUIRED_FALSE_NON_CLAIMS)
    else:
        for key in REQUIRED_FALSE_NON_CLAIMS:
            if key not in declared or declared.get(key) is not False:
                bad_keys.append(key)
    checks.append(
        _new_check(
            "required non-claims false",
            not bad_keys,
            "every required declared non-claim is present as bool false",
            {"bad_keys": bad_keys[:20], "bad_key_count": len(bad_keys)},
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )


def _validate_top_level_false_flags(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    for field, code in TOP_LEVEL_BLOCK_FLAG_CODES.items():
        checks.append(
            _new_check(
                f"{field} not asserted",
                request.get(field) is not True,
                False,
                request.get(field, False),
                code,
            )
        )


def _validate_basis_artifact(
    artifact_name: str,
    path_value: Any,
    path_missing_code: str,
    unreadable_code: str,
    not_object_code: str,
    not_recorded_code: str,
    failed_checks_code: str,
    version_code: str,
    expected_outcome: str,
    checks: list[dict[str, Any]],
) -> Mapping[str, Any] | None:
    missing = path_value in (None, "")
    checks.append(
        _new_check(
            f"{artifact_name} artifact path declared",
            not missing,
            "declared artifact path",
            path_value,
            path_missing_code,
        )
    )
    if missing:
        return None
    artifact, read_error, read_actual = _read_json_object(path_value)
    checks.append(
        _new_check(
            f"{artifact_name} artifact readable JSON",
            read_error is None,
            "readable JSON object",
            read_actual,
            unreadable_code if read_error == "UNREADABLE" else not_object_code,
        )
    )
    if read_error is not None:
        if read_error == "NOT_JSON_OBJECT":
            checks[-1]["block_code"] = not_object_code
            checks[-1]["failure_code"] = not_object_code
        return None
    outcome = _artifact_outcome(artifact)
    checks.append(
        _new_check(
            f"{artifact_name} artifact outcome recorded",
            outcome == expected_outcome,
            expected_outcome,
            outcome,
            not_recorded_code,
        )
    )
    result_version = _artifact_result_version(artifact)
    checks.append(
        _new_check(
            f"{artifact_name} artifact result version 0.1.0",
            result_version == RESULT_VERSION,
            RESULT_VERSION,
            result_version,
            version_code,
        )
    )
    failed_count = _artifact_failed_check_count(artifact)
    checks.append(
        _new_check(
            f"{artifact_name} artifact failed check count zero",
            failed_count == 0,
            0,
            failed_count,
            failed_checks_code,
        )
    )
    return artifact


def _build_runtime_object(
    request: Mapping[str, Any],
    recorded: bool,
    runtime_boundary_basis: Mapping[str, Any],
    runtime_permission_basis: Mapping[str, Any],
    operation_execution_basis: Mapping[str, Any],
    upstream: Mapping[str, bool],
) -> dict[str, Any]:
    runtime = {
        "runtime_id": str(
            request.get("local_relevance_medium_read_only_runtime_id")
            or DEFAULT_RUNTIME_ID
        ),
        "runtime_type": RUNTIME_TYPE,
        "runtime_version": RESULT_VERSION,
        "runtime_scope": RUNTIME_SCOPE,
        "basis_runtime_boundary_artifact": runtime_boundary_basis.get("artifact"),
        "basis_runtime_boundary_outcome": runtime_boundary_basis.get("outcome"),
        "basis_runtime_boundary_result_version": runtime_boundary_basis.get(
            "result_version"
        ),
        "basis_runtime_boundary_failed_check_count": runtime_boundary_basis.get(
            "failed_check_count"
        ),
        "basis_runtime_permission_artifact": runtime_permission_basis.get("artifact"),
        "basis_runtime_permission_outcome": runtime_permission_basis.get("outcome"),
        "basis_runtime_permission_result_version": runtime_permission_basis.get(
            "result_version"
        ),
        "basis_runtime_permission_failed_check_count": runtime_permission_basis.get(
            "failed_check_count"
        ),
        "basis_operation_execution_artifact": operation_execution_basis.get("artifact"),
        "basis_operation_execution_outcome": operation_execution_basis.get("outcome"),
        "basis_operation_execution_result_version": operation_execution_basis.get(
            "result_version"
        ),
        "basis_operation_execution_failed_check_count": operation_execution_basis.get(
            "failed_check_count"
        ),
        "selected_command": request.get("selected_command"),
        "selected_command_is_state": request.get("selected_command") == SELECTED_COMMAND,
        "selected_runtime_boundary_recorded": bool(
            upstream.get("selected_runtime_boundary_recorded")
        ),
        "future_runtime_may_be_considered": bool(
            upstream.get("future_runtime_may_be_considered")
        ),
        "selected_runtime_permission_recorded": bool(
            upstream.get("selected_runtime_permission_recorded")
        ),
        "runtime_permission_created": bool(upstream.get("runtime_permission_created")),
        "runtime_permission_local_only": bool(
            upstream.get("runtime_permission_local_only")
        ),
        "runtime_permission_read_only": bool(
            upstream.get("runtime_permission_read_only")
        ),
        "selected_operation_execution_recorded": bool(
            upstream.get("selected_operation_execution_recorded")
        ),
        "operation_execution_created": bool(
            upstream.get("operation_execution_created")
        ),
        "operation_execution_performed": bool(
            upstream.get("operation_execution_performed")
        ),
        "operation_execution_local_only": bool(
            upstream.get("operation_execution_local_only")
        ),
        "operation_execution_read_only": bool(
            upstream.get("operation_execution_read_only")
        ),
        "local_relevance_medium_read_only_runtime_recorded": bool(recorded),
        "runtime_created": bool(recorded),
        "runtime_local_only": bool(recorded),
        "runtime_read_only": bool(recorded),
        "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
    }
    for field in RUNTIME_OBJECT_FALSE_FIELDS:
        runtime[field] = False
    return runtime


def _runtime_statement(runtime: Mapping[str, Any], recorded: bool) -> dict[str, Any]:
    return {
        "local_relevance_medium_read_only_runtime_recorded": bool(recorded),
        "basis_runtime_boundary_artifact_preserved": bool(
            runtime.get("basis_runtime_boundary_artifact")
        ),
        "basis_runtime_permission_artifact_preserved": bool(
            runtime.get("basis_runtime_permission_artifact")
        ),
        "basis_operation_execution_artifact_preserved": bool(
            runtime.get("basis_operation_execution_artifact")
        ),
        "selected_command_preserved": runtime.get("selected_command")
        == SELECTED_COMMAND,
        "selected_command_is_state": runtime.get("selected_command_is_state") is True,
        "selected_runtime_boundary_recorded": runtime.get(
            "selected_runtime_boundary_recorded"
        )
        is True,
        "future_runtime_may_be_considered": runtime.get(
            "future_runtime_may_be_considered"
        )
        is True,
        "selected_runtime_permission_recorded": runtime.get(
            "selected_runtime_permission_recorded"
        )
        is True,
        "runtime_permission_created": runtime.get("runtime_permission_created")
        is True,
        "runtime_permission_local_only": runtime.get("runtime_permission_local_only")
        is True,
        "runtime_permission_read_only": runtime.get("runtime_permission_read_only")
        is True,
        "selected_operation_execution_recorded": runtime.get(
            "selected_operation_execution_recorded"
        )
        is True,
        "operation_execution_created": runtime.get("operation_execution_created")
        is True,
        "operation_execution_performed": runtime.get("operation_execution_performed")
        is True,
        "operation_execution_local_only": runtime.get(
            "operation_execution_local_only"
        )
        is True,
        "operation_execution_read_only": runtime.get("operation_execution_read_only")
        is True,
        "runtime_created": runtime.get("runtime_created") is True,
        "runtime_local_only": runtime.get("runtime_local_only") is True,
        "runtime_read_only": runtime.get("runtime_read_only") is True,
        "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
        "runtime_boundary_v0_failure_not_repaired": True,
        "runtime_boundary_v0_failure_not_hidden": True,
        "runtime_boundary_v0_failure_not_claimed_passed": True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "lookup_command_execution_boundary_v1_filename_path_failure_evidence_preserved": True,
        "state_packet_body_exposure_boundary_v0_failure_evidence_preserved": True,
        "state_packet_body_exposure_v1_over_strict_evidence_preserved": True,
        "local_carrier_command_execution_boundary_v1_over_strict_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }


def _runtime_non_meaning() -> dict[str, Any]:
    return {
        "not_runtime_hosting": True,
        "not_runtime_loop": True,
        "not_daemon_behavior": True,
        "not_continuation": True,
        "not_runtime_held_state": True,
        "not_runtime_held_reentry": True,
        "not_second_operation": True,
        "not_prior_result_reentry_cycle": True,
        "not_public_api": True,
        "not_participant_facing_interface": True,
        "not_distributed_network_behavior": True,
        "not_general_operation_permission": True,
        "not_general_lookup_permission": True,
        "not_registry": True,
        "not_search": True,
        "not_query_surface": True,
        "not_ranking": True,
        "not_older_runtime_authority_import": True,
        "not_follow_on_work": True,
    }


def _open_items() -> list[str]:
    return [
        "runtime hosting",
        "runtime loop",
        "daemon behavior",
        "continuation",
        "runtime-held state",
        "runtime-held re-entry",
        "second operation",
        "prior-result re-entry cycle",
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


def build_local_relevance_medium_read_only_runtime_v0_min_summary(
    result: Mapping[str, Any]
) -> dict[str, Any]:
    checks = result.get("local_relevance_medium_read_only_runtime_checks", [])
    if not isinstance(checks, list):
        checks = []
    runtime = result.get("local_relevance_medium_read_only_runtime", {})
    if not isinstance(runtime, MappingABC):
        runtime = {}
    statement = result.get("local_relevance_medium_read_only_runtime_statement", {})
    if not isinstance(statement, MappingABC):
        statement = {}
    block = result.get("block")
    if not isinstance(block, MappingABC):
        block = {}
    failed_count = sum(1 for check in checks if check.get("passed") is False)
    passed_count = sum(1 for check in checks if check.get("passed") is True)
    non_claims = result.get("non_claims", {})
    canonical_false = (
        isinstance(non_claims, MappingABC)
        and all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)
        and all(isinstance(non_claims.get(key), bool) for key in REQUIRED_FALSE_NON_CLAIMS)
    )
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "runtime_id": runtime.get("runtime_id"),
        "question": result.get(
            "declared_local_relevance_medium_read_only_runtime_question", {}
        ).get("question")
        if isinstance(
            result.get("declared_local_relevance_medium_read_only_runtime_question"),
            MappingABC,
        )
        else None,
        "intent": result.get(
            "declared_local_relevance_medium_read_only_runtime_question", {}
        ).get("intent")
        if isinstance(
            result.get("declared_local_relevance_medium_read_only_runtime_question"),
            MappingABC,
        )
        else None,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "runtime_recorded": runtime.get(
            "local_relevance_medium_read_only_runtime_recorded"
        ),
        "basis_runtime_boundary_artifact_preserved": statement.get(
            "basis_runtime_boundary_artifact_preserved"
        ),
        "basis_runtime_permission_artifact_preserved": statement.get(
            "basis_runtime_permission_artifact_preserved"
        ),
        "basis_operation_execution_artifact_preserved": statement.get(
            "basis_operation_execution_artifact_preserved"
        ),
        "selected_command": runtime.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved"),
        "selected_command_is_state": runtime.get("selected_command_is_state"),
        "selected_runtime_boundary_recorded": runtime.get(
            "selected_runtime_boundary_recorded"
        ),
        "future_runtime_may_be_considered": runtime.get(
            "future_runtime_may_be_considered"
        ),
        "selected_runtime_permission_recorded": runtime.get(
            "selected_runtime_permission_recorded"
        ),
        "runtime_permission_created": runtime.get("runtime_permission_created"),
        "runtime_permission_local_only": runtime.get("runtime_permission_local_only"),
        "runtime_permission_read_only": runtime.get("runtime_permission_read_only"),
        "selected_operation_execution_recorded": runtime.get(
            "selected_operation_execution_recorded"
        ),
        "operation_execution_created": runtime.get("operation_execution_created"),
        "operation_execution_performed": runtime.get("operation_execution_performed"),
        "operation_execution_local_only": runtime.get("operation_execution_local_only"),
        "operation_execution_read_only": runtime.get("operation_execution_read_only"),
        "runtime_created": runtime.get("runtime_created"),
        "runtime_local_only": runtime.get("runtime_local_only"),
        "runtime_read_only": runtime.get("runtime_read_only"),
        "runtime_object_summary": {
            "runtime_type": runtime.get("runtime_type"),
            "runtime_scope": runtime.get("runtime_scope"),
            "runtime_version": runtime.get("runtime_version"),
        },
        "runtime_hosting_not_created": runtime.get("runtime_hosting_created") is False,
        "runtime_loop_not_created": runtime.get("runtime_loop_created") is False,
        "daemon_behavior_not_created": runtime.get("daemon_behavior_created") is False,
        "continuation_not_created": runtime.get("continuation_created") is False,
        "runtime_held_state_not_created": runtime.get("runtime_held_state_created")
        is False,
        "runtime_held_reentry_not_created": runtime.get("runtime_held_reentry_created")
        is False,
        "second_operation_not_created": runtime.get("second_operation_created") is False,
        "prior_result_reentry_cycle_not_created": runtime.get(
            "prior_result_reentry_cycle_created"
        )
        is False,
        "public_api_not_created": runtime.get("public_api_created") is False,
        "participant_facing_interface_not_created": runtime.get(
            "participant_facing_interface_created"
        )
        is False,
        "distributed_network_behavior_not_created": runtime.get(
            "distributed_network_behavior_created"
        )
        is False,
        "general_operation_permission_not_created": runtime.get(
            "general_operation_permission_created"
        )
        is False,
        "general_lookup_permission_not_created": runtime.get(
            "general_lookup_permission_created"
        )
        is False,
        "arbitrary_lookup_permission_not_created": runtime.get(
            "arbitrary_lookup_permission_created"
        )
        is False,
        "unsupported_commands_not_permitted": runtime.get(
            "unsupported_commands_permitted"
        )
        is False,
        "unsupported_lookup_keys_not_permitted": runtime.get(
            "unsupported_lookup_keys_permitted"
        )
        is False,
        "no_new_lookup_entry_created_beyond_bounded_lookup_result_object": runtime.get(
            "new_lookup_entry_created"
        )
        is False,
        "no_new_signal_entry_relevance_object_index_entry_created": all(
            runtime.get(key) is False
            for key in (
                "new_signal_accepted",
                "new_entry_accepted",
                "new_relevance_object_created",
                "new_index_entry_created",
            )
        ),
        "filesystem_discovery_not_performed": runtime.get(
            "filesystem_discovery_performed"
        )
        is False,
        "registry_search_query_surface_ranking_not_created": all(
            runtime.get(key) is False
            for key in (
                "registry_created",
                "search_surface_created",
                "query_surface_created",
                "ranking_surface_created",
            )
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": all(
            runtime.get(key) is False
            for key in (
                "scoring_surface_created",
                "priority_surface_created",
                "validity_judgment_created",
                "truth_judgment_created",
                "authority_judgment_created",
                "currentness_judgment_created",
            )
        ),
        "older_runtime_lineage_not_imported_as_authority": runtime.get(
            "older_runtime_lineage_imported_as_authority"
        )
        is False,
        "older_runtime_permission_not_treated_as_current": runtime.get(
            "older_runtime_permission_treated_as_current"
        )
        is False,
        "runtime_authority_not_imported": runtime.get("runtime_authority_imported")
        is False,
        "runtime_boundary_v0_failure_evidence_preserved": runtime.get(
            "runtime_boundary_v0_failure_evidence_preserved"
        )
        is True,
        "runtime_boundary_v0_failure_not_repaired_hidden_claimed_passed": all(
            result.get("non_claims", {}).get(key) is False
            for key in (
                "runtime_boundary_v0_failure_repaired",
                "runtime_boundary_v0_failure_hidden",
                "runtime_boundary_v0_failure_claimed_passed",
            )
        )
        if isinstance(result.get("non_claims"), MappingABC)
        else False,
        "repeated_reception_permission_arbitrary_reception_feed_not_created": all(
            runtime.get(key) is False
            for key in (
                "repeated_reception_permission_created",
                "arbitrary_reception_created",
                "feed_created",
            )
        ),
        "source_authority_currentness_truth_synchronization_participation_participant_role_not_created": all(
            runtime.get(key) is False
            for key in (
                "source_transfer_occurred",
                "source_receipt_occurred",
                "authority_created",
                "currentness_created",
                "truth_created",
                "synchronization_created",
                "participation_authorized",
                "participant_role_created",
            )
        ),
        "consumed_request_token_remains_closed": statement.get(
            "consumed_request_token_remains_closed"
        ),
        "authorization_token_reuse_blocked": statement.get(
            "authorization_token_reuse_blocked"
        ),
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved"
        ),
        "follow_on_not_created": runtime.get("follow_on_work_authorized") is False,
        "key_non_claims": {
            key: result.get("non_claims", {}).get(key)
            for key in (
                "runtime_hosting_created",
                "runtime_loop_created",
                "daemon_behavior_created",
                "older_runtime_lineage_imported_as_authority",
                "runtime_authority_imported",
                "consumed_request_reopened",
                "authorization_token_reused",
            )
        }
        if isinstance(result.get("non_claims"), MappingABC)
        else {},
        "result_level_non_claims_canonical_false": canonical_false,
    }


def _compose_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    runtime_boundary_basis: Mapping[str, Any],
    runtime_permission_basis: Mapping[str, Any],
    operation_execution_basis: Mapping[str, Any],
    upstream: Mapping[str, bool],
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    runtime = _build_runtime_object(
        request,
        recorded,
        runtime_boundary_basis,
        runtime_permission_basis,
        operation_execution_basis,
        upstream,
    )
    first_code = _first_failed_code(checks)
    block = (
        {
            "blocked": True,
            "code": first_code,
            "block_code": first_code,
            "reason": "runtime blocked by bounded public check failure",
        }
        if outcome == OUTCOME_BLOCKED
        else {"blocked": False, "code": None, "block_code": None, "reason": None}
    )
    metadata = {
        "local_relevance_medium_read_only_runtime_id": runtime["runtime_id"],
        "local_relevance_medium_read_only_runtime_type": RUNTIME_TYPE,
        "local_relevance_medium_read_only_runtime_version": RESULT_VERSION,
        "result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_runtime_metadata": metadata,
        "declared_local_relevance_medium_read_only_runtime_question": {
            "question": _sanitize(
                request.get("local_relevance_medium_read_only_runtime_question")
            ),
            "intent": _sanitize(
                request.get("local_relevance_medium_read_only_runtime_intent")
            ),
            "request": _sanitize(copy.deepcopy(dict(request))),
        },
        "selected_runtime_boundary_artifact_basis": dict(runtime_boundary_basis),
        "selected_runtime_permission_artifact_basis": dict(runtime_permission_basis),
        "selected_operation_execution_artifact_basis": dict(operation_execution_basis),
        "local_relevance_medium_read_only_runtime": runtime,
        "local_relevance_medium_read_only_runtime_checks": checks,
        "local_relevance_medium_read_only_runtime_statement": _runtime_statement(
            runtime, recorded
        ),
        "local_relevance_medium_read_only_runtime_non_meaning": _runtime_non_meaning(),
        "additional_basis_required": []
        if outcome != OUTCOME_REQUIRES_ADDITIONAL_BASIS
        else ["additional clean runtime basis required"],
        "not_recorded_basis": []
        if outcome != OUTCOME_NOT_RECORDED
        else ["runtime was not recorded by declared request posture"],
        "what_remains_open": _open_items(),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["local_relevance_medium_read_only_runtime_summary"] = (
        build_local_relevance_medium_read_only_runtime_v0_min_summary(result)
    )
    return result


def _blocked_result_from_code(
    code: str,
    reason: Any,
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    bounded_request = dict(
        request
        or build_declared_local_relevance_medium_read_only_runtime_v0_min_request()
    )
    checks = [
        _new_check(
            "declared local relevance medium read-only runtime request readable",
            False,
            "readable declared request mapping",
            reason,
            code,
        )
    ]
    empty_basis = _basis_artifact_summary(None, None, "")
    upstream = {
        "selected_runtime_boundary_recorded": False,
        "future_runtime_may_be_considered": False,
        "selected_runtime_permission_recorded": False,
        "runtime_permission_created": False,
        "runtime_permission_local_only": False,
        "runtime_permission_read_only": False,
        "selected_operation_execution_recorded": False,
        "operation_execution_created": False,
        "operation_execution_performed": False,
        "operation_execution_local_only": False,
        "operation_execution_read_only": False,
    }
    return _compose_result(
        bounded_request,
        checks,
        OUTCOME_BLOCKED,
        empty_basis,
        empty_basis,
        empty_basis,
        upstream,
    )


def resolve_local_relevance_medium_read_only_runtime_v0_min(
    declared_local_relevance_medium_read_only_runtime: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded local read-only selected-state runtime."""

    if declared_local_relevance_medium_read_only_runtime is None:
        request = build_declared_local_relevance_medium_read_only_runtime_v0_min_request()
    elif not isinstance(declared_local_relevance_medium_read_only_runtime, MappingABC):
        return _blocked_result_from_code(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_REQUEST_MALFORMED",
            type(declared_local_relevance_medium_read_only_runtime).__name__,
        )
    else:
        request = copy.deepcopy(dict(declared_local_relevance_medium_read_only_runtime))

    checks: list[dict[str, Any]] = []
    forced_code = request.get("_forced_block_code")
    if isinstance(forced_code, str) and forced_code in BLOCK_CODES:
        checks.append(
            _new_check(
                "declared local relevance medium read-only runtime request readable",
                False,
                "readable declared request mapping",
                request.get("_forced_block_reason"),
                forced_code,
            )
        )

    question = request.get("local_relevance_medium_read_only_runtime_question")
    checks.append(
        _new_check(
            "runtime question declared",
            isinstance(question, str) and bool(question.strip()),
            "declared runtime question",
            question,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_QUESTION_UNDECLARED",
        )
    )
    intent = request.get("local_relevance_medium_read_only_runtime_intent")
    checks.append(
        _new_check(
            "runtime intent supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _new_check(
            "runtime block intent not requested",
            intent != INTENT_BLOCK,
            "not block intent",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BLOCK_REQUESTED",
        )
    )

    _validate_top_level_false_flags(request, checks)
    _validate_declared_non_claims(request, checks)

    runtime_boundary_path = request.get("selected_runtime_boundary_artifact")
    runtime_permission_path = request.get("selected_runtime_permission_artifact")
    operation_execution_path = request.get("selected_operation_execution_artifact")

    runtime_boundary_artifact = _validate_basis_artifact(
        "runtime boundary",
        runtime_boundary_path,
        "RUNTIME_BOUNDARY_ARTIFACT_PATH_MISSING",
        "RUNTIME_BOUNDARY_ARTIFACT_UNREADABLE",
        "RUNTIME_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
        "RUNTIME_BOUNDARY_ARTIFACT_NOT_RECORDED",
        "RUNTIME_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
        "RUNTIME_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
        RUNTIME_BOUNDARY_RECORDED_OUTCOME,
        checks,
    )
    runtime_permission_artifact = _validate_basis_artifact(
        "runtime permission",
        runtime_permission_path,
        "RUNTIME_PERMISSION_ARTIFACT_PATH_MISSING",
        "RUNTIME_PERMISSION_ARTIFACT_UNREADABLE",
        "RUNTIME_PERMISSION_ARTIFACT_NOT_JSON_OBJECT",
        "RUNTIME_PERMISSION_ARTIFACT_NOT_RECORDED",
        "RUNTIME_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
        "RUNTIME_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0",
        RUNTIME_PERMISSION_RECORDED_OUTCOME,
        checks,
    )
    operation_execution_artifact = _validate_basis_artifact(
        "operation execution",
        operation_execution_path,
        "OPERATION_EXECUTION_ARTIFACT_PATH_MISSING",
        "OPERATION_EXECUTION_ARTIFACT_UNREADABLE",
        "OPERATION_EXECUTION_ARTIFACT_NOT_JSON_OBJECT",
        "OPERATION_EXECUTION_ARTIFACT_NOT_RECORDED",
        "OPERATION_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT",
        "OPERATION_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0",
        OPERATION_EXECUTION_RECORDED_OUTCOME,
        checks,
    )

    selected_command = request.get("selected_command")
    checks.append(
        _new_check(
            "selected command declared",
            selected_command not in (None, ""),
            "selected command declared",
            selected_command,
            "SELECTED_COMMAND_MISSING",
        )
    )
    checks.append(
        _new_check(
            "selected command exactly state",
            selected_command == SELECTED_COMMAND,
            SELECTED_COMMAND,
            selected_command,
            "SELECTED_COMMAND_NOT_STATE",
        )
    )
    checks.append(
        _new_check(
            "selected command is state",
            selected_command == SELECTED_COMMAND,
            True,
            selected_command == SELECTED_COMMAND,
            "SELECTED_COMMAND_NOT_STATE",
        )
    )

    runtime_type = request.get("runtime_type")
    checks.append(
        _new_check(
            "runtime type declared",
            runtime_type not in (None, ""),
            RUNTIME_TYPE,
            runtime_type,
            "RUNTIME_TYPE_MISSING",
        )
    )
    checks.append(
        _new_check(
            "runtime type exact",
            runtime_type == RUNTIME_TYPE,
            RUNTIME_TYPE,
            runtime_type,
            "RUNTIME_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME",
        )
    )
    runtime_scope = request.get("runtime_scope")
    checks.append(
        _new_check(
            "runtime scope declared",
            runtime_scope not in (None, ""),
            RUNTIME_SCOPE,
            runtime_scope,
            "RUNTIME_SCOPE_MISSING",
        )
    )
    checks.append(
        _new_check(
            "runtime scope exact",
            runtime_scope == RUNTIME_SCOPE,
            RUNTIME_SCOPE,
            runtime_scope,
            "RUNTIME_SCOPE_NOT_SELECTED_RUNTIME_ONLY",
        )
    )

    upstream = {
        "selected_runtime_boundary_recorded": _present_true_without_false(
            runtime_boundary_artifact,
            (
                "selected_runtime_boundary_recorded",
                "local_relevance_medium_read_only_runtime_boundary_recorded",
            ),
        ),
        "future_runtime_may_be_considered": _present_true_without_false(
            runtime_boundary_artifact,
            ("future_runtime_may_be_considered",),
        ),
        "selected_runtime_permission_recorded": _present_true_without_false(
            runtime_permission_artifact,
            (
                "selected_runtime_permission_recorded",
                "local_relevance_medium_read_only_runtime_permission_recorded",
            ),
        ),
        "runtime_permission_created": _present_true_without_false(
            runtime_permission_artifact,
            ("runtime_permission_created",),
        ),
        "runtime_permission_local_only": _present_true_without_false(
            runtime_permission_artifact,
            ("runtime_permission_local_only",),
        ),
        "runtime_permission_read_only": _present_true_without_false(
            runtime_permission_artifact,
            ("runtime_permission_read_only",),
        ),
        "selected_operation_execution_recorded": _present_true_without_false(
            operation_execution_artifact,
            (
                "selected_operation_execution_recorded",
                "local_relevance_medium_read_only_operation_execution_recorded",
            ),
        ),
        "operation_execution_created": _present_true_without_false(
            operation_execution_artifact,
            ("operation_execution_created",),
        ),
        "operation_execution_performed": _present_true_without_false(
            operation_execution_artifact,
            ("operation_execution_performed",),
        ),
        "operation_execution_local_only": _present_true_without_false(
            operation_execution_artifact,
            ("operation_execution_local_only",),
        ),
        "operation_execution_read_only": _present_true_without_false(
            operation_execution_artifact,
            ("operation_execution_read_only",),
        ),
    }
    upstream_check_codes = {
        "selected_runtime_boundary_recorded": "SELECTED_RUNTIME_BOUNDARY_NOT_RECORDED",
        "future_runtime_may_be_considered": "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED",
        "selected_runtime_permission_recorded": "SELECTED_RUNTIME_PERMISSION_NOT_RECORDED",
        "runtime_permission_created": "RUNTIME_PERMISSION_NOT_CREATED",
        "runtime_permission_local_only": "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE",
        "runtime_permission_read_only": "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE",
        "selected_operation_execution_recorded": "SELECTED_OPERATION_EXECUTION_NOT_RECORDED",
        "operation_execution_created": "OPERATION_EXECUTION_NOT_CREATED",
        "operation_execution_performed": "OPERATION_EXECUTION_NOT_PERFORMED",
        "operation_execution_local_only": "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE",
        "operation_execution_read_only": "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE",
    }
    for field, code in upstream_check_codes.items():
        checks.append(
            _new_check(
                field.replace("_", " "),
                upstream[field] is True,
                True,
                upstream[field],
                code,
            )
        )

    predecessor_preservation = {
        "runtime_boundary_v0_failure_evidence_preserved": True,
        "runtime_boundary_v0_failure_not_repaired": request.get(
            "runtime_boundary_v0_failure_repaired"
        )
        is not True,
        "runtime_boundary_v0_failure_not_hidden": request.get(
            "runtime_boundary_v0_failure_hidden"
        )
        is not True,
        "runtime_boundary_v0_failure_not_claimed_passed": request.get(
            "runtime_boundary_v0_failure_claimed_passed"
        )
        is not True,
        "predecessor_failure_evidence_preserved": all(
            request.get(key) is not True
            for key in (
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
            )
        ),
    }
    checks.append(
        _new_check(
            "runtime boundary v0 failure evidence preserved",
            predecessor_preservation["runtime_boundary_v0_failure_evidence_preserved"],
            True,
            predecessor_preservation["runtime_boundary_v0_failure_evidence_preserved"],
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    )
    checks.append(
        _new_check(
            "runtime boundary v0 failure not repaired",
            predecessor_preservation["runtime_boundary_v0_failure_not_repaired"],
            True,
            predecessor_preservation["runtime_boundary_v0_failure_not_repaired"],
            "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
        )
    )
    checks.append(
        _new_check(
            "runtime boundary v0 failure not hidden",
            predecessor_preservation["runtime_boundary_v0_failure_not_hidden"],
            True,
            predecessor_preservation["runtime_boundary_v0_failure_not_hidden"],
            "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN",
        )
    )
    checks.append(
        _new_check(
            "runtime boundary v0 failure not claimed passed",
            predecessor_preservation["runtime_boundary_v0_failure_not_claimed_passed"],
            True,
            predecessor_preservation["runtime_boundary_v0_failure_not_claimed_passed"],
            "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
        )
    )
    checks.append(
        _new_check(
            "predecessor failure evidence preserved",
            predecessor_preservation["predecessor_failure_evidence_preserved"],
            True,
            predecessor_preservation["predecessor_failure_evidence_preserved"],
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    )

    candidate_recordable = (
        not any(check.get("passed") is False for check in checks)
        and intent == INTENT_RECORD
        and request.get("requested_local_relevance_medium_read_only_runtime_outcome")
        not in (OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS)
    )
    runtime_recorded_check_passes = (
        candidate_recordable
        or intent == INTENT_DO_NOT_RECORD
        or request.get("requested_local_relevance_medium_read_only_runtime_outcome")
        in (OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS)
    )
    for name, passed, code in (
        (
            "local relevance medium read-only runtime recorded",
            runtime_recorded_check_passes,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_NOT_RECORDED",
        ),
        ("runtime created", runtime_recorded_check_passes, "RUNTIME_NOT_CREATED"),
        ("runtime local only", runtime_recorded_check_passes, "RUNTIME_LOCAL_ONLY_NOT_TRUE"),
        ("runtime read only", runtime_recorded_check_passes, "RUNTIME_READ_ONLY_NOT_TRUE"),
    ):
        checks.append(_new_check(name, passed, True, passed, code))
    checks.append(
        _new_check(
            "result-level required false non-claims canonical false",
            True,
            "canonical false result-level non-claims",
            "canonical false result-level non-claims",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )

    runtime_boundary_basis = _basis_artifact_summary(
        runtime_boundary_path,
        runtime_boundary_artifact,
        RUNTIME_BOUNDARY_RECORDED_OUTCOME,
    )
    runtime_permission_basis = _basis_artifact_summary(
        runtime_permission_path,
        runtime_permission_artifact,
        RUNTIME_PERMISSION_RECORDED_OUTCOME,
    )
    operation_execution_basis = _basis_artifact_summary(
        operation_execution_path,
        operation_execution_artifact,
        OPERATION_EXECUTION_RECORDED_OUTCOME,
    )

    failed = any(check.get("passed") is False for check in checks)
    requested_outcome = request.get("requested_local_relevance_medium_read_only_runtime_outcome")
    if failed:
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD or requested_outcome == OUTCOME_NOT_RECORDED:
        outcome = OUTCOME_NOT_RECORDED
    elif (
        requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        or request.get("additional_basis_context")
    ):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    else:
        outcome = OUTCOME_RECORDED

    return _compose_result(
        request,
        checks,
        outcome,
        runtime_boundary_basis,
        runtime_permission_basis,
        operation_execution_basis,
        upstream,
    )


def resolve_local_relevance_medium_read_only_runtime_v0_min_from_path(
    declared_local_relevance_medium_read_only_runtime_path: Path | str,
) -> dict[str, Any]:
    """Resolve one declared runtime request from an explicit JSON file path."""

    try:
        with Path(declared_local_relevance_medium_read_only_runtime_path).open(
            "r", encoding="utf-8"
        ) as handle:
            loaded = json.load(handle)
    except Exception as exc:  # noqa: BLE001 - bounded public resolver error surface
        request = build_declared_local_relevance_medium_read_only_runtime_v0_min_request()
        request["_forced_block_code"] = (
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_REQUEST_UNREADABLE"
        )
        request["_forced_block_reason"] = f"{type(exc).__name__}: {exc}"
        return resolve_local_relevance_medium_read_only_runtime_v0_min(request)
    if not isinstance(loaded, MappingABC):
        return _blocked_result_from_code(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_REQUEST_MALFORMED",
            type(loaded).__name__,
        )
    return resolve_local_relevance_medium_read_only_runtime_v0_min(loaded)


def _result_output_path(result: Mapping[str, Any], output_path: Path | str | None) -> Path:
    if output_path is not None:
        candidate = Path(output_path)
        if candidate.suffix:
            return candidate
        runtime_id = _runtime_id_from_result(result)
        return candidate / f"{runtime_id}__local_relevance_medium_read_only_runtime_v0_min_result.json"
    runtime_id = _runtime_id_from_result(result)
    return OUTPUT_ROOT / f"{runtime_id}__local_relevance_medium_read_only_runtime_v0_min_result.json"


def _runtime_id_from_result(result: Mapping[str, Any]) -> str:
    runtime = result.get("local_relevance_medium_read_only_runtime")
    if isinstance(runtime, MappingABC) and runtime.get("runtime_id"):
        return str(runtime["runtime_id"])
    metadata = result.get("local_relevance_medium_read_only_runtime_metadata")
    if isinstance(metadata, MappingABC) and metadata.get(
        "local_relevance_medium_read_only_runtime_id"
    ):
        return str(metadata["local_relevance_medium_read_only_runtime_id"])
    return DEFAULT_RUNTIME_ID


def _with_non_overwriting_suffix(path: Path) -> Path:
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


def write_local_relevance_medium_read_only_runtime_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a runtime resolver result without silently overwriting."""

    candidate = _with_non_overwriting_suffix(_result_output_path(result, output_path))
    candidate.parent.mkdir(parents=True, exist_ok=True)
    with candidate.open("w", encoding="utf-8") as handle:
        json.dump(dict(result), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return candidate
