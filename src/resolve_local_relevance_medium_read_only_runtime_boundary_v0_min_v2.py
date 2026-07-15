"""Resolve one local read-only selected-state runtime boundary, v2.

This additive successor preserves the v0 runtime-boundary resolver as failed
lineage evidence. The v2 correction is narrow: selected-operation-execution
recorded aliases are inspected across the operation-execution object,
statement, and summary, and any present false or non-boolean alias blocks the
boundary with SELECTED_OPERATION_EXECUTION_NOT_RECORDED.

The resolver records one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY
object only. It remains local, read-only, selected-state-runtime-consideration
only, closure-token-aware, non-runtime-shaped, non-runtime-hosting-shaped, and
older-runtime-authority-import-blocking.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyRuntimeBoundaryV0MinV2Error(RuntimeError):
    """Bounded resolver error for v2 runtime-boundary request/path handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_boundary_v0_min_v2"
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

DEFAULT_BOUNDARY_ID = "local_relevance_medium_read_only_runtime_boundary_001"
BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_RUNTIME_CONSIDERATION_ONLY"
SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)
SELECTED_COMMAND = "state"

RUNTIME_PERMISSION_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED"
)
OPERATION_EXECUTION_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED"
)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION for "
    "selected command state, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION, existing reusable "
    "read-only lookup permission, prior lookup-pair coverage, and prior local "
    "carrier command surface, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY be recorded that permits a "
    "future local read-only runtime to be considered as a separately bounded "
    "step, without creating runtime, creating runtime hosting, creating runtime "
    "loop, creating daemon behavior, creating continuation, creating "
    "runtime-held state, creating runtime-held re-entry, creating second "
    "operation, creating prior-result re-entry cycle, creating public API, "
    "creating participant-facing interface, creating distributed network "
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

SELECTED_OPERATION_EXECUTION_RECORDED_ALIAS_KEYS = (
    "selected_operation_execution_recorded",
    "local_relevance_medium_read_only_operation_execution_recorded",
)

BOUNDARY_OBJECT_FALSE_FIELDS = (
    "runtime_created",
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
    "artifact_existence_treated_as_runtime_boundary_authority",
    "latest_file_posture_treated_as_runtime_boundary_authority",
    "repo_local_availability_treated_as_runtime_boundary_authority",
    "hidden_repo_state_used_as_runtime_boundary_content",
    "hidden_repo_state_used_as_runtime_boundary_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

REQUIRED_FALSE_NON_CLAIMS = BOUNDARY_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_runtime_boundary_recorded",
    "basis_runtime_permission_artifact_preserved",
    "basis_operation_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_runtime_permission_recorded",
    "runtime_permission_created",
    "runtime_permission_local_only",
    "runtime_permission_read_only",
    "selected_operation_execution_recorded",
    "operation_execution_created",
    "operation_execution_performed",
    "operation_execution_local_only",
    "operation_execution_read_only",
    "future_runtime_may_be_considered",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_BLOCK_REQUESTED",
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
    "SELECTED_RUNTIME_PERMISSION_NOT_RECORDED",
    "RUNTIME_PERMISSION_NOT_CREATED",
    "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE",
    "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE",
    "SELECTED_OPERATION_EXECUTION_NOT_RECORDED",
    "OPERATION_EXECUTION_NOT_CREATED",
    "OPERATION_EXECUTION_NOT_PERFORMED",
    "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE",
    "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_SELECTED_RUNTIME_CONSIDERATION_ONLY",
    "RUNTIME_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_AUTHORITY",
    "PRIOR_ARTIFACTS_MUTATED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_REQUEST_UNREADABLE",
)

_FALSE_FIELD_BLOCK_CODES = {
    "runtime_created": "RUNTIME_CREATED",
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
    "older_runtime_lineage_imported_as_authority": (
        "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY"
    ),
    "older_runtime_permission_treated_as_current": (
        "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT"
    ),
    "runtime_authority_imported": "RUNTIME_AUTHORITY_IMPORTED",
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
    "artifact_existence_treated_as_runtime_boundary_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY"
    ),
    "latest_file_posture_treated_as_runtime_boundary_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY"
    ),
    "repo_local_availability_treated_as_runtime_boundary_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY"
    ),
    "hidden_repo_state_used_as_runtime_boundary_content": (
        "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_CONTENT"
    ),
    "hidden_repo_state_used_as_runtime_boundary_authority": (
        "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_AUTHORITY"
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

_SHORTCUT_BLOCK_CODES = {
    "runtime_permission_artifact_missing": "RUNTIME_PERMISSION_ARTIFACT_PATH_MISSING",
    "runtime_permission_artifact_not_recorded": "RUNTIME_PERMISSION_ARTIFACT_NOT_RECORDED",
    "runtime_permission_artifact_failed_checks_present": (
        "RUNTIME_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "runtime_permission_artifact_version_not_0_1_0": (
        "RUNTIME_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "operation_execution_artifact_missing": "OPERATION_EXECUTION_ARTIFACT_PATH_MISSING",
    "operation_execution_artifact_not_recorded": (
        "OPERATION_EXECUTION_ARTIFACT_NOT_RECORDED"
    ),
    "operation_execution_artifact_failed_checks_present": (
        "OPERATION_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "operation_execution_artifact_version_not_0_1_0": (
        "OPERATION_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "selected_command_missing": "SELECTED_COMMAND_MISSING",
    "selected_command_not_state": "SELECTED_COMMAND_NOT_STATE",
    "selected_runtime_permission_not_recorded": "SELECTED_RUNTIME_PERMISSION_NOT_RECORDED",
    "runtime_permission_not_created": "RUNTIME_PERMISSION_NOT_CREATED",
    "runtime_permission_local_only_not_true": "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE",
    "runtime_permission_read_only_not_true": "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE",
    "selected_operation_execution_not_recorded": (
        "SELECTED_OPERATION_EXECUTION_NOT_RECORDED"
    ),
    "operation_execution_not_created": "OPERATION_EXECUTION_NOT_CREATED",
    "operation_execution_not_performed": "OPERATION_EXECUTION_NOT_PERFORMED",
    "operation_execution_local_only_not_true": "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    "operation_execution_read_only_not_true": "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE",
    "future_runtime_may_not_be_considered": "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED",
    "boundary_type_not_local_relevance_medium_read_only_runtime_boundary": (
        "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY"
    ),
    "boundary_scope_not_selected_runtime_consideration_only": (
        "BOUNDARY_SCOPE_NOT_SELECTED_RUNTIME_CONSIDERATION_ONLY"
    ),
}

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_runtime_boundary_body",
    "raw_runtime_permission_body",
    "raw_runtime_permission_boundary_body",
    "raw_runtime_body",
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
    "runtime_boundary_body",
    "runtime_permission_body",
    "runtime_permission_boundary_body",
    "runtime_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
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

HIDDEN_REQUEST_CONTENT_KEYS = (
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _sanitize(value: Any, key: str | None = None) -> Any:
    key_name = str(key or "").lower()
    if key_name in SENSITIVE_CONTENT_KEYS or key_name.endswith("_body"):
        return "[REDACTED_RUNTIME_BOUNDARY_CONTENT]"
    if isinstance(value, str):
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return "[REDACTED_RUNTIME_BOUNDARY_CONTENT]"
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, MappingABC):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, key) for item in value]
    return copy.deepcopy(value)


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _as_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        stripped = value.strip()
        if stripped.isdigit():
            return int(stripped)
    return None


def _mapping(value: Any) -> Mapping[str, Any]:
    if isinstance(value, MappingABC):
        return value
    return {}


def _find_first_mapping_value(artifact: Mapping[str, Any], suffix: str) -> Mapping[str, Any]:
    for key, value in artifact.items():
        if str(key).endswith(suffix) and isinstance(value, MappingABC):
            return value
    return {}


def _find_first_checks(artifact: Mapping[str, Any]) -> list[Any]:
    for key, value in artifact.items():
        if str(key).endswith("_checks") and isinstance(value, list):
            return value
    return []


def _failed_count_from_checks(checks: list[Any]) -> int:
    return sum(
        1
        for check in checks
        if isinstance(check, MappingABC) and check.get("passed") is False
    )


def _passed_count_from_checks(checks: list[Any]) -> int:
    return sum(
        1 for check in checks if isinstance(check, MappingABC) and check.get("passed") is True
    )


def _artifact_common(
    artifact: Mapping[str, Any],
    object_key: str,
    object_version_key: str,
) -> dict[str, Any]:
    obj = _mapping(artifact.get(object_key))
    summary = _find_first_mapping_value(artifact, "_summary")
    metadata = _find_first_mapping_value(artifact, "_metadata")
    checks = _find_first_checks(artifact)
    failed_count = _first_present(
        artifact.get("failed_check_count"),
        summary.get("failed_check_count"),
        metadata.get("failed_check_count"),
    )
    passed_count = _first_present(
        artifact.get("passed_check_count"),
        summary.get("passed_check_count"),
        metadata.get("passed_check_count"),
    )
    return {
        "object": obj,
        "summary": summary,
        "metadata": metadata,
        "checks": checks,
        "outcome": _first_present(
            artifact.get("outcome"),
            summary.get("outcome"),
            metadata.get("outcome"),
        ),
        "result_version": _first_present(
            artifact.get("result_version"),
            summary.get("result_version"),
            metadata.get("result_version"),
            obj.get(object_version_key),
        ),
        "failed_check_count": _first_present(
            _as_int(failed_count),
            _failed_count_from_checks(checks) if checks else None,
        ),
        "passed_check_count": _first_present(
            _as_int(passed_count),
            _passed_count_from_checks(checks) if checks else None,
        ),
    }


def _read_json_object(path_value: Any, not_object_code: str) -> tuple[dict[str, Any] | None, str | None]:
    try:
        with Path(path_value).open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return None, not_object_code.replace("_NOT_JSON_OBJECT", "_UNREADABLE")
    if not isinstance(data, MappingABC):
        return None, not_object_code
    return dict(copy.deepcopy(data)), None


def _empty_runtime_permission_basis(path_value: Any) -> dict[str, Any]:
    return {
        "artifact_path": str(path_value) if path_value is not None else None,
        "artifact_outcome": None,
        "artifact_result_version": None,
        "artifact_failed_check_count": None,
        "artifact_passed_check_count": None,
        "runtime_permission_type": None,
        "runtime_permission_scope": None,
        "selected_command": None,
        "selected_command_is_state": None,
        "selected_runtime_permission_recorded": None,
        "runtime_permission_created": None,
        "runtime_permission_local_only": None,
        "runtime_permission_read_only": None,
        "operation_execution_created": None,
        "operation_execution_performed": None,
        "operation_execution_local_only": None,
        "operation_execution_read_only": None,
        "runtime_created": None,
        "runtime_hosting_created": None,
        "runtime_loop_created": None,
        "daemon_behavior_created": None,
        "continuation_created": None,
        "older_runtime_lineage_imported_as_authority": None,
        "older_runtime_permission_treated_as_current": None,
        "runtime_authority_imported": None,
    }


def _extract_runtime_permission_basis(
    artifact: Mapping[str, Any],
    path_value: Any,
) -> dict[str, Any]:
    common = _artifact_common(
        artifact,
        "local_relevance_medium_read_only_runtime_permission",
        "runtime_permission_version",
    )
    obj = common["object"]
    summary = common["summary"]
    statement = _mapping(
        artifact.get("local_relevance_medium_read_only_runtime_permission_statement")
    )
    return {
        "artifact_path": str(path_value),
        "artifact_outcome": common["outcome"],
        "artifact_result_version": common["result_version"],
        "artifact_failed_check_count": common["failed_check_count"],
        "artifact_passed_check_count": common["passed_check_count"],
        "runtime_permission_type": _first_present(
            obj.get("runtime_permission_type"),
            summary.get("runtime_permission_type"),
        ),
        "runtime_permission_scope": _first_present(
            obj.get("runtime_permission_scope"),
            summary.get("runtime_permission_scope"),
        ),
        "selected_command": _first_present(
            obj.get("selected_command"),
            summary.get("selected_command"),
        ),
        "selected_command_is_state": _first_present(
            obj.get("selected_command_is_state"),
            statement.get("selected_command_is_state"),
            summary.get("selected_command_is_state"),
        ),
        "selected_runtime_permission_recorded": _first_present(
            obj.get("local_relevance_medium_read_only_runtime_permission_recorded"),
            obj.get("selected_runtime_permission_recorded"),
            statement.get("local_relevance_medium_read_only_runtime_permission_recorded"),
            statement.get("selected_runtime_permission_recorded"),
            summary.get("local_relevance_medium_read_only_runtime_permission_recorded"),
            summary.get("selected_runtime_permission_recorded"),
            common["outcome"] == RUNTIME_PERMISSION_RECORDED_OUTCOME,
        ),
        "runtime_permission_created": _first_present(
            obj.get("runtime_permission_created"),
            statement.get("runtime_permission_created"),
            summary.get("runtime_permission_created"),
        ),
        "runtime_permission_local_only": _first_present(
            obj.get("runtime_permission_local_only"),
            statement.get("runtime_permission_local_only"),
            summary.get("runtime_permission_local_only"),
        ),
        "runtime_permission_read_only": _first_present(
            obj.get("runtime_permission_read_only"),
            statement.get("runtime_permission_read_only"),
            summary.get("runtime_permission_read_only"),
        ),
        "operation_execution_created": _first_present(
            obj.get("operation_execution_created"),
            statement.get("operation_execution_created"),
            summary.get("operation_execution_created"),
        ),
        "operation_execution_performed": _first_present(
            obj.get("operation_execution_performed"),
            statement.get("operation_execution_performed"),
            summary.get("operation_execution_performed"),
        ),
        "operation_execution_local_only": _first_present(
            obj.get("operation_execution_local_only"),
            statement.get("operation_execution_local_only"),
            summary.get("operation_execution_local_only"),
        ),
        "operation_execution_read_only": _first_present(
            obj.get("operation_execution_read_only"),
            statement.get("operation_execution_read_only"),
            summary.get("operation_execution_read_only"),
        ),
        "runtime_created": _first_present(obj.get("runtime_created"), summary.get("runtime_created")),
        "runtime_hosting_created": _first_present(
            obj.get("runtime_hosting_created"),
            summary.get("runtime_hosting_created"),
        ),
        "runtime_loop_created": _first_present(
            obj.get("runtime_loop_created"),
            summary.get("runtime_loop_created"),
        ),
        "daemon_behavior_created": _first_present(
            obj.get("daemon_behavior_created"),
            summary.get("daemon_behavior_created"),
        ),
        "continuation_created": _first_present(
            obj.get("continuation_created"),
            summary.get("continuation_created"),
        ),
        "older_runtime_lineage_imported_as_authority": _first_present(
            obj.get("older_runtime_lineage_imported_as_authority"),
            summary.get("older_runtime_lineage_imported_as_authority"),
        ),
        "older_runtime_permission_treated_as_current": _first_present(
            obj.get("older_runtime_permission_treated_as_current"),
            summary.get("older_runtime_permission_treated_as_current"),
        ),
        "runtime_authority_imported": _first_present(
            obj.get("runtime_authority_imported"),
            summary.get("runtime_authority_imported"),
        ),
    }


def _empty_operation_execution_basis(path_value: Any) -> dict[str, Any]:
    return {
        "artifact_path": str(path_value) if path_value is not None else None,
        "artifact_outcome": None,
        "artifact_result_version": None,
        "artifact_failed_check_count": None,
        "artifact_passed_check_count": None,
        "selected_command": None,
        "selected_command_is_state": None,
        "selected_operation_execution_recorded": None,
        "selected_operation_execution_recorded_aliases_clean": None,
        "selected_operation_execution_recorded_alias_postures": [],
        "selected_operation_execution_recorded_alias_conflict_detected": None,
        "operation_execution_created": None,
        "operation_execution_performed": None,
        "operation_execution_local_only": None,
        "operation_execution_read_only": None,
    }


def _collect_operation_execution_recorded_aliases(
    obj: Mapping[str, Any],
    statement: Mapping[str, Any],
    summary: Mapping[str, Any],
) -> list[dict[str, Any]]:
    postures: list[dict[str, Any]] = []
    for section_name, section in (
        ("local_relevance_medium_read_only_operation_execution", obj),
        ("local_relevance_medium_read_only_operation_execution_statement", statement),
        ("local_relevance_medium_read_only_operation_execution_summary", summary),
    ):
        for alias_key in SELECTED_OPERATION_EXECUTION_RECORDED_ALIAS_KEYS:
            if alias_key in section:
                postures.append(
                    {
                        "section": section_name,
                        "field": alias_key,
                        "value": section.get(alias_key),
                    }
                )
    return postures


def _clean_selected_operation_execution_recorded(
    postures: list[Mapping[str, Any]],
    outcome_recorded: bool,
) -> tuple[bool, bool]:
    if any(posture.get("value") is False for posture in postures):
        return False, True
    if any(
        posture.get("value") not in (True, False)
        for posture in postures
    ):
        return False, True
    if any(posture.get("value") is True for posture in postures):
        return True, False
    return outcome_recorded, False


def _extract_operation_execution_basis(
    artifact: Mapping[str, Any],
    path_value: Any,
) -> dict[str, Any]:
    common = _artifact_common(
        artifact,
        "local_relevance_medium_read_only_operation_execution",
        "operation_execution_version",
    )
    obj = common["object"]
    summary = common["summary"]
    statement = _mapping(
        artifact.get("local_relevance_medium_read_only_operation_execution_statement")
    )
    alias_postures = _collect_operation_execution_recorded_aliases(
        obj,
        statement,
        summary,
    )
    selected_recorded, alias_conflict_detected = (
        _clean_selected_operation_execution_recorded(
            alias_postures,
            common["outcome"] == OPERATION_EXECUTION_RECORDED_OUTCOME,
        )
    )
    return {
        "artifact_path": str(path_value),
        "artifact_outcome": common["outcome"],
        "artifact_result_version": common["result_version"],
        "artifact_failed_check_count": common["failed_check_count"],
        "artifact_passed_check_count": common["passed_check_count"],
        "selected_command": _first_present(obj.get("selected_command"), summary.get("selected_command")),
        "selected_command_is_state": _first_present(
            obj.get("selected_command_is_state"),
            statement.get("selected_command_is_state"),
            summary.get("selected_command_is_state"),
        ),
        "selected_operation_execution_recorded": selected_recorded,
        "selected_operation_execution_recorded_aliases_clean": (
            not alias_conflict_detected
        ),
        "selected_operation_execution_recorded_alias_postures": alias_postures,
        "selected_operation_execution_recorded_alias_conflict_detected": (
            alias_conflict_detected
        ),
        "operation_execution_created": _first_present(
            obj.get("operation_execution_created"),
            statement.get("operation_execution_created"),
            summary.get("operation_execution_created"),
        ),
        "operation_execution_performed": _first_present(
            obj.get("operation_execution_performed"),
            statement.get("operation_execution_performed"),
            summary.get("operation_execution_performed"),
        ),
        "operation_execution_local_only": _first_present(
            obj.get("operation_execution_local_only"),
            statement.get("operation_execution_local_only"),
            summary.get("operation_execution_local_only"),
        ),
        "operation_execution_read_only": _first_present(
            obj.get("operation_execution_read_only"),
            statement.get("operation_execution_read_only"),
            summary.get("operation_execution_read_only"),
        ),
    }


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    public_code = code if code in BLOCK_CODES else "NON_CLAIM_MISSING_OR_FLIPPED"
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _sanitize(expected_posture),
            "actual_posture": _sanitize(actual_posture),
            "block_code": None if passed else public_code,
            "failure_code": None if passed else public_code,
        }
    )


def _failed_checks(checks: list[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [check for check in checks if check.get("passed") is False]


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if code in BLOCK_CODES:
                return str(code)
    return None


def _check_requested_false_fields(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    for field in REQUIRED_FALSE_NON_CLAIMS:
        value = declared.get(field, False)
        passed = value is False
        _add_check(
            checks,
            f"{field}_not_created_or_authorized",
            passed,
            False,
            value,
            _FALSE_FIELD_BLOCK_CODES.get(field, "NON_CLAIM_MISSING_OR_FLIPPED"),
        )


def _declared_non_claims_passed(declared_non_claims: Any) -> bool:
    if not isinstance(declared_non_claims, MappingABC):
        return False
    return all(declared_non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _raw_or_hidden_content_present(declared: Mapping[str, Any]) -> bool:
    def contains_hidden(value: Any, key: str | None = None) -> bool:
        key_name = str(key or "").lower()
        if key_name in HIDDEN_REQUEST_CONTENT_KEYS:
            return True
        if key_name in SENSITIVE_CONTENT_KEYS or key_name.endswith("_body"):
            return True
        if isinstance(value, str):
            return any(sentinel in value for sentinel in HOSTILE_SENTINELS)
        if isinstance(value, MappingABC):
            return any(contains_hidden(v, str(k)) for k, v in value.items())
        if isinstance(value, (list, tuple)):
            return any(contains_hidden(item, key) for item in value)
        return False

    return contains_hidden(declared)


def _build_boundary_object(
    declared: Mapping[str, Any],
    runtime_permission_basis: Mapping[str, Any],
    operation_execution_basis: Mapping[str, Any],
    recorded: bool,
) -> dict[str, Any]:
    requested_command = declared.get("selected_command")
    selected_command = SELECTED_COMMAND if requested_command == SELECTED_COMMAND else None
    selected_command_is_state = selected_command == SELECTED_COMMAND

    boundary: dict[str, Any] = {
        "boundary_id": str(declared.get("local_relevance_medium_read_only_runtime_boundary_id") or DEFAULT_BOUNDARY_ID),
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "basis_runtime_permission_artifact": runtime_permission_basis.get("artifact_path"),
        "basis_runtime_permission_outcome": runtime_permission_basis.get("artifact_outcome"),
        "basis_runtime_permission_result_version": runtime_permission_basis.get("artifact_result_version"),
        "basis_runtime_permission_failed_check_count": runtime_permission_basis.get("artifact_failed_check_count"),
        "basis_operation_execution_artifact": operation_execution_basis.get("artifact_path"),
        "basis_operation_execution_outcome": operation_execution_basis.get("artifact_outcome"),
        "basis_operation_execution_result_version": operation_execution_basis.get("artifact_result_version"),
        "basis_operation_execution_failed_check_count": operation_execution_basis.get("artifact_failed_check_count"),
        "selected_command": selected_command,
        "selected_command_is_state": selected_command_is_state,
        "selected_runtime_permission_recorded": runtime_permission_basis.get("selected_runtime_permission_recorded") is True,
        "runtime_permission_created": runtime_permission_basis.get("runtime_permission_created") is True,
        "runtime_permission_local_only": runtime_permission_basis.get("runtime_permission_local_only") is True,
        "runtime_permission_read_only": runtime_permission_basis.get("runtime_permission_read_only") is True,
        "selected_operation_execution_recorded": operation_execution_basis.get("selected_operation_execution_recorded") is True,
        "operation_execution_created": operation_execution_basis.get("operation_execution_created") is True,
        "operation_execution_performed": operation_execution_basis.get("operation_execution_performed") is True,
        "operation_execution_local_only": operation_execution_basis.get("operation_execution_local_only") is True,
        "operation_execution_read_only": operation_execution_basis.get("operation_execution_read_only") is True,
        "future_runtime_may_be_considered": bool(recorded),
    }
    for field in BOUNDARY_OBJECT_FALSE_FIELDS:
        boundary[field] = False
    return _sanitize(boundary)


def _build_statement(boundary: Mapping[str, Any], recorded: bool) -> dict[str, bool]:
    return {
        "local_relevance_medium_read_only_runtime_boundary_recorded": bool(recorded),
        "basis_runtime_permission_artifact_preserved": (
            boundary.get("basis_runtime_permission_outcome")
            == RUNTIME_PERMISSION_RECORDED_OUTCOME
        ),
        "basis_operation_execution_artifact_preserved": (
            boundary.get("basis_operation_execution_outcome")
            == OPERATION_EXECUTION_RECORDED_OUTCOME
        ),
        "selected_command_preserved": boundary.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": boundary.get("selected_command_is_state") is True,
        "selected_runtime_permission_recorded": boundary.get(
            "selected_runtime_permission_recorded"
        )
        is True,
        "runtime_permission_created": boundary.get("runtime_permission_created") is True,
        "runtime_permission_local_only": boundary.get("runtime_permission_local_only")
        is True,
        "runtime_permission_read_only": boundary.get("runtime_permission_read_only")
        is True,
        "selected_operation_execution_recorded": boundary.get(
            "selected_operation_execution_recorded"
        )
        is True,
        "operation_execution_created": boundary.get("operation_execution_created") is True,
        "operation_execution_performed": boundary.get("operation_execution_performed")
        is True,
        "operation_execution_local_only": boundary.get("operation_execution_local_only")
        is True,
        "operation_execution_read_only": boundary.get("operation_execution_read_only")
        is True,
        "future_runtime_may_be_considered": boundary.get(
            "future_runtime_may_be_considered"
        )
        is True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    non_meaning = {
        "runtime_boundary_is_runtime": False,
        "runtime_boundary_is_runtime_hosting": False,
        "runtime_boundary_is_runtime_loop": False,
        "runtime_boundary_is_daemon_behavior": False,
        "runtime_boundary_is_continuation": False,
        "runtime_boundary_is_runtime_held_state": False,
        "runtime_boundary_is_runtime_held_reentry": False,
        "runtime_boundary_is_second_operation": False,
        "runtime_boundary_is_prior_result_reentry_cycle": False,
        "runtime_boundary_is_public_api": False,
        "runtime_boundary_is_participant_facing_interface": False,
        "runtime_boundary_is_distributed_network_behavior": False,
        "runtime_boundary_imports_older_runtime_authority": False,
        "runtime_boundary_creates_registry_search_query_or_ranking": False,
        "runtime_boundary_authorizes_follow_on_work": False,
        "runtime_boundary_v2_mutates_v0": False,
        "runtime_boundary_v2_repairs_v0": False,
        "runtime_boundary_v2_hides_v0_failure": False,
        "runtime_boundary_v2_claims_v0_passed": False,
        "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
    }
    for field in REQUIRED_FALSE_NON_CLAIMS:
        non_meaning[field] = False
    return non_meaning


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium read-only runtime boundary v2 test",
        "local relevance medium read-only runtime boundary v2 live artifact",
        "local relevance medium read-only runtime boundary v2 terminal summary",
        "runtime",
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
        "publication flow",
        "repeated reception permission",
        "arbitrary reception",
        "feed",
        "follow-on work",
    ]


def _build_result_artifact(
    declared: Mapping[str, Any],
    runtime_permission_basis: Mapping[str, Any],
    operation_execution_basis: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block_reason: Any = None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    boundary = _build_boundary_object(
        declared,
        runtime_permission_basis,
        operation_execution_basis,
        recorded,
    )
    statement = _build_statement(boundary, recorded)
    block_code = _first_failed_code(checks)
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": block_code if outcome == OUTCOME_BLOCKED else None,
        "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
        "reason": _sanitize(block_reason or block_code) if outcome == OUTCOME_BLOCKED else None,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_runtime_boundary_metadata": {
            "local_relevance_medium_read_only_runtime_boundary_id": boundary[
                "boundary_id"
            ],
            "local_relevance_medium_read_only_runtime_boundary_type": BOUNDARY_TYPE,
            "local_relevance_medium_read_only_runtime_boundary_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
            "result_version": RESULT_VERSION,
            "successor_of_resolver_module": (
                "resolve_local_relevance_medium_read_only_runtime_boundary_v0_min"
            ),
            "runtime_boundary_v0_failure_evidence_preserved": True,
        },
        "declared_local_relevance_medium_read_only_runtime_boundary_question": {
            "question": _sanitize(
                declared.get("local_relevance_medium_read_only_runtime_boundary_question")
            ),
            "intent": _sanitize(
                declared.get("local_relevance_medium_read_only_runtime_boundary_intent")
            ),
            "selected_command": _sanitize(declared.get("selected_command")),
            "boundary_type": _sanitize(declared.get("boundary_type")),
            "boundary_scope": _sanitize(declared.get("boundary_scope")),
        },
        "selected_runtime_permission_artifact_basis": _sanitize(
            dict(runtime_permission_basis)
        ),
        "selected_operation_execution_artifact_basis": _sanitize(
            dict(operation_execution_basis)
        ),
        "local_relevance_medium_read_only_runtime_boundary": boundary,
        "local_relevance_medium_read_only_runtime_boundary_checks": _sanitize(checks),
        "local_relevance_medium_read_only_runtime_boundary_statement": statement,
        "local_relevance_medium_read_only_runtime_boundary_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": _sanitize(
            declared.get("additional_basis_context", [])
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else []
        ),
        "not_recorded_basis": _sanitize(
            declared.get("not_recorded_basis", [])
            if outcome in (OUTCOME_NOT_RECORDED, OUTCOME_BLOCKED)
            else []
        ),
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["local_relevance_medium_read_only_runtime_boundary_summary"] = (
        build_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_summary(result)
    )
    return _sanitize(result)


def _blocked_malformed_result(code: str, reason: Any) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _add_check(
        checks,
        "declared_local_relevance_medium_read_only_runtime_boundary_request_readable",
        False,
        "mapping JSON object",
        reason,
        code,
    )
    return _build_result_artifact(
        {},
        _empty_runtime_permission_basis(None),
        _empty_operation_execution_basis(None),
        checks,
        OUTCOME_BLOCKED,
        reason,
    )


def resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(
    declared_local_relevance_medium_read_only_runtime_boundary: Mapping[str, Any]
    | None = None,
) -> dict:
    """Resolve one bounded local read-only selected-state runtime boundary, v2."""

    if declared_local_relevance_medium_read_only_runtime_boundary is None:
        declared = (
            build_declared_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_request()
        )
    elif isinstance(declared_local_relevance_medium_read_only_runtime_boundary, MappingABC):
        declared = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_runtime_boundary)
        )
    else:
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_REQUEST_MALFORMED",
            "declared request is not a mapping",
        )

    checks: list[dict[str, Any]] = []
    question = declared.get("local_relevance_medium_read_only_runtime_boundary_question")
    intent = declared.get("local_relevance_medium_read_only_runtime_boundary_intent")

    _add_check(
        checks,
        "runtime_boundary_question_declared",
        isinstance(question, str) and bool(question.strip()),
        "declared runtime boundary question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_QUESTION_UNDECLARED",
    )
    _add_check(
        checks,
        "runtime_boundary_intent_supported",
        intent in SUPPORTED_INTENTS and intent != INTENT_BLOCK,
        f"one of {SUPPORTED_INTENTS[:-1]}",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_BLOCK_REQUESTED"
        if intent == INTENT_BLOCK
        else "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_INTENT_UNSUPPORTED",
    )

    runtime_permission_path = declared.get("selected_runtime_permission_artifact")
    runtime_permission_path_declared = (
        runtime_permission_path is not None
        and runtime_permission_path != ""
        and declared.get("runtime_permission_artifact_missing") is not True
    )
    _add_check(
        checks,
        "runtime_permission_artifact_path_declared",
        runtime_permission_path_declared,
        "declared runtime permission artifact path",
        runtime_permission_path,
        "RUNTIME_PERMISSION_ARTIFACT_PATH_MISSING",
    )
    runtime_permission_basis = _empty_runtime_permission_basis(runtime_permission_path)
    if runtime_permission_path_declared:
        runtime_permission_artifact, runtime_permission_read_code = _read_json_object(
            runtime_permission_path,
            "RUNTIME_PERMISSION_ARTIFACT_NOT_JSON_OBJECT",
        )
        _add_check(
            checks,
            "runtime_permission_artifact_readable_json_object",
            runtime_permission_read_code is None,
            "readable JSON object",
            runtime_permission_read_code or "readable JSON object",
            runtime_permission_read_code or "RUNTIME_PERMISSION_ARTIFACT_UNREADABLE",
        )
        if runtime_permission_artifact is not None:
            runtime_permission_basis = _extract_runtime_permission_basis(
                runtime_permission_artifact,
                runtime_permission_path,
            )

    runtime_permission_outcome_ok = (
        runtime_permission_basis.get("artifact_outcome")
        == RUNTIME_PERMISSION_RECORDED_OUTCOME
        and declared.get("runtime_permission_artifact_not_recorded") is not True
    )
    _add_check(
        checks,
        "runtime_permission_artifact_outcome_recorded",
        runtime_permission_outcome_ok,
        RUNTIME_PERMISSION_RECORDED_OUTCOME,
        runtime_permission_basis.get("artifact_outcome"),
        "RUNTIME_PERMISSION_ARTIFACT_NOT_RECORDED",
    )
    runtime_permission_version_ok = (
        runtime_permission_basis.get("artifact_result_version") == RESULT_VERSION
        and declared.get("runtime_permission_artifact_version_not_0_1_0") is not True
    )
    _add_check(
        checks,
        "runtime_permission_artifact_result_version_0_1_0",
        runtime_permission_version_ok,
        RESULT_VERSION,
        runtime_permission_basis.get("artifact_result_version"),
        "RUNTIME_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0",
    )
    runtime_permission_failed_count = runtime_permission_basis.get(
        "artifact_failed_check_count"
    )
    runtime_permission_failed_count_ok = (
        runtime_permission_failed_count == 0
        and declared.get("runtime_permission_artifact_failed_checks_present") is not True
    )
    _add_check(
        checks,
        "runtime_permission_artifact_failed_check_count_zero",
        runtime_permission_failed_count_ok,
        0,
        runtime_permission_failed_count,
        "RUNTIME_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    operation_execution_path = declared.get("selected_operation_execution_artifact")
    operation_execution_path_declared = (
        operation_execution_path is not None
        and operation_execution_path != ""
        and declared.get("operation_execution_artifact_missing") is not True
    )
    _add_check(
        checks,
        "operation_execution_artifact_path_declared",
        operation_execution_path_declared,
        "declared operation execution artifact path",
        operation_execution_path,
        "OPERATION_EXECUTION_ARTIFACT_PATH_MISSING",
    )
    operation_execution_basis = _empty_operation_execution_basis(operation_execution_path)
    if operation_execution_path_declared:
        operation_execution_artifact, operation_execution_read_code = _read_json_object(
            operation_execution_path,
            "OPERATION_EXECUTION_ARTIFACT_NOT_JSON_OBJECT",
        )
        _add_check(
            checks,
            "operation_execution_artifact_readable_json_object",
            operation_execution_read_code is None,
            "readable JSON object",
            operation_execution_read_code or "readable JSON object",
            operation_execution_read_code or "OPERATION_EXECUTION_ARTIFACT_UNREADABLE",
        )
        if operation_execution_artifact is not None:
            operation_execution_basis = _extract_operation_execution_basis(
                operation_execution_artifact,
                operation_execution_path,
            )

    operation_execution_outcome_ok = (
        operation_execution_basis.get("artifact_outcome")
        == OPERATION_EXECUTION_RECORDED_OUTCOME
        and declared.get("operation_execution_artifact_not_recorded") is not True
    )
    _add_check(
        checks,
        "operation_execution_artifact_outcome_recorded",
        operation_execution_outcome_ok,
        OPERATION_EXECUTION_RECORDED_OUTCOME,
        operation_execution_basis.get("artifact_outcome"),
        "OPERATION_EXECUTION_ARTIFACT_NOT_RECORDED",
    )
    operation_execution_version_ok = (
        operation_execution_basis.get("artifact_result_version") == RESULT_VERSION
        and declared.get("operation_execution_artifact_version_not_0_1_0") is not True
    )
    _add_check(
        checks,
        "operation_execution_artifact_result_version_0_1_0",
        operation_execution_version_ok,
        RESULT_VERSION,
        operation_execution_basis.get("artifact_result_version"),
        "OPERATION_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0",
    )
    operation_execution_failed_count = operation_execution_basis.get(
        "artifact_failed_check_count"
    )
    operation_execution_failed_count_ok = (
        operation_execution_failed_count == 0
        and declared.get("operation_execution_artifact_failed_checks_present") is not True
    )
    _add_check(
        checks,
        "operation_execution_artifact_failed_check_count_zero",
        operation_execution_failed_count_ok,
        0,
        operation_execution_failed_count,
        "OPERATION_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    selected_command = declared.get("selected_command")
    selected_command_declared = (
        selected_command is not None and declared.get("selected_command_missing") is not True
    )
    _add_check(
        checks,
        "selected_command_declared",
        selected_command_declared,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_MISSING",
    )
    selected_command_is_state = (
        selected_command == SELECTED_COMMAND
        and declared.get("selected_command_not_state") is not True
    )
    _add_check(
        checks,
        "selected_command_exactly_state",
        selected_command_is_state,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _add_check(
        checks,
        "selected_command_is_state",
        selected_command_is_state,
        True,
        selected_command_is_state,
        "SELECTED_COMMAND_NOT_STATE",
    )

    _add_check(
        checks,
        "selected_runtime_permission_recorded",
        runtime_permission_basis.get("selected_runtime_permission_recorded") is True
        and declared.get("selected_runtime_permission_not_recorded") is not True,
        True,
        runtime_permission_basis.get("selected_runtime_permission_recorded"),
        "SELECTED_RUNTIME_PERMISSION_NOT_RECORDED",
    )
    _add_check(
        checks,
        "runtime_permission_created",
        runtime_permission_basis.get("runtime_permission_created") is True
        and declared.get("runtime_permission_not_created") is not True,
        True,
        runtime_permission_basis.get("runtime_permission_created"),
        "RUNTIME_PERMISSION_NOT_CREATED",
    )
    _add_check(
        checks,
        "runtime_permission_local_only",
        runtime_permission_basis.get("runtime_permission_local_only") is True
        and declared.get("runtime_permission_local_only_not_true") is not True,
        True,
        runtime_permission_basis.get("runtime_permission_local_only"),
        "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE",
    )
    _add_check(
        checks,
        "runtime_permission_read_only",
        runtime_permission_basis.get("runtime_permission_read_only") is True
        and declared.get("runtime_permission_read_only_not_true") is not True,
        True,
        runtime_permission_basis.get("runtime_permission_read_only"),
        "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE",
    )

    operation_execution_recorded_actual = {
        "selected_operation_execution_recorded": operation_execution_basis.get(
            "selected_operation_execution_recorded"
        ),
        "selected_operation_execution_recorded_aliases_clean": (
            operation_execution_basis.get(
                "selected_operation_execution_recorded_aliases_clean"
            )
        ),
        "selected_operation_execution_recorded_alias_postures": (
            operation_execution_basis.get(
                "selected_operation_execution_recorded_alias_postures"
            )
        ),
    }
    _add_check(
        checks,
        "selected_operation_execution_recorded",
        operation_execution_basis.get("selected_operation_execution_recorded") is True
        and operation_execution_basis.get(
            "selected_operation_execution_recorded_aliases_clean"
        )
        is True
        and declared.get("selected_operation_execution_not_recorded") is not True,
        True,
        operation_execution_recorded_actual,
        "SELECTED_OPERATION_EXECUTION_NOT_RECORDED",
    )
    _add_check(
        checks,
        "operation_execution_created",
        operation_execution_basis.get("operation_execution_created") is True
        and declared.get("operation_execution_not_created") is not True,
        True,
        operation_execution_basis.get("operation_execution_created"),
        "OPERATION_EXECUTION_NOT_CREATED",
    )
    _add_check(
        checks,
        "operation_execution_performed",
        operation_execution_basis.get("operation_execution_performed") is True
        and declared.get("operation_execution_not_performed") is not True,
        True,
        operation_execution_basis.get("operation_execution_performed"),
        "OPERATION_EXECUTION_NOT_PERFORMED",
    )
    _add_check(
        checks,
        "operation_execution_local_only",
        operation_execution_basis.get("operation_execution_local_only") is True
        and declared.get("operation_execution_local_only_not_true") is not True,
        True,
        operation_execution_basis.get("operation_execution_local_only"),
        "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    )
    _add_check(
        checks,
        "operation_execution_read_only",
        operation_execution_basis.get("operation_execution_read_only") is True
        and declared.get("operation_execution_read_only_not_true") is not True,
        True,
        operation_execution_basis.get("operation_execution_read_only"),
        "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE",
    )

    future_runtime = declared.get("future_runtime_may_be_considered", True)
    _add_check(
        checks,
        "future_runtime_may_be_considered",
        future_runtime is True
        and declared.get("future_runtime_may_not_be_considered") is not True,
        True,
        future_runtime,
        "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED",
    )

    boundary_type = declared.get("boundary_type")
    _add_check(
        checks,
        "boundary_type_declared",
        boundary_type is not None,
        BOUNDARY_TYPE,
        boundary_type,
        "BOUNDARY_TYPE_MISSING",
    )
    _add_check(
        checks,
        "boundary_type_exact",
        boundary_type == BOUNDARY_TYPE
        and declared.get("boundary_type_not_local_relevance_medium_read_only_runtime_boundary")
        is not True,
        BOUNDARY_TYPE,
        boundary_type,
        "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
    )

    boundary_scope = declared.get("boundary_scope")
    _add_check(
        checks,
        "boundary_scope_declared",
        boundary_scope is not None,
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_MISSING",
    )
    _add_check(
        checks,
        "boundary_scope_exact",
        boundary_scope == BOUNDARY_SCOPE
        and declared.get("boundary_scope_not_selected_runtime_consideration_only")
        is not True,
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_NOT_SELECTED_RUNTIME_CONSIDERATION_ONLY",
    )

    for field, code in _SHORTCUT_BLOCK_CODES.items():
        if field in declared:
            _add_check(
                checks,
                f"{field}_shortcut_not_asserted",
                declared.get(field) is not True,
                False,
                declared.get(field),
                code,
            )

    _check_requested_false_fields(declared, checks)

    declared_non_claims = declared.get("declared_non_claims")
    _add_check(
        checks,
        "required_declared_non_claims_false",
        _declared_non_claims_passed(declared_non_claims),
        "all required non-claims present as false bool",
        declared_non_claims,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _add_check(
        checks,
        "raw_or_hidden_request_content_not_used",
        not _raw_or_hidden_content_present(declared),
        False,
        _raw_or_hidden_content_present(declared),
        "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_CONTENT",
    )
    predecessor_failure_preserved = not (
        declared.get("predecessor_failure_repaired") is True
        or declared.get("predecessor_failure_hidden") is True
        or declared.get("predecessor_failure_claimed_passed") is True
    )
    _add_check(
        checks,
        "predecessor_failure_evidence_preserved",
        predecessor_failure_preserved,
        True,
        predecessor_failure_preserved,
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _add_check(
        checks,
        "runtime_boundary_v0_failure_evidence_preserved",
        True,
        True,
        True,
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _add_check(
        checks,
        "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved",
        True,
        True,
        True,
        "SELECTED_OPERATION_EXECUTION_NOT_RECORDED",
    )
    _add_check(
        checks,
        "result_level_required_false_non_claims_canonical_false",
        all(value is False for value in _canonical_false_non_claims().values()),
        "canonical false result-level non-claims",
        _canonical_false_non_claims(),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    if _failed_checks(checks):
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif (
        declared.get("requested_local_relevance_medium_read_only_runtime_boundary_outcome")
        == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    ):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    else:
        outcome = OUTCOME_RECORDED

    return _build_result_artifact(
        declared,
        runtime_permission_basis,
        operation_execution_basis,
        checks,
        outcome,
        declared.get("block_reason"),
    )


def resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_from_path(
    declared_local_relevance_medium_read_only_runtime_boundary_path: Path | str,
) -> dict:
    """Resolve a declared v2 runtime-boundary request from one JSON object path."""

    try:
        with Path(declared_local_relevance_medium_read_only_runtime_boundary_path).open(
            "r",
            encoding="utf-8",
        ) as handle:
            data = json.load(handle)
    except Exception as exc:
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_REQUEST_UNREADABLE",
            str(exc),
        )
    if not isinstance(data, MappingABC):
        return _blocked_malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_REQUEST_MALFORMED",
            "declared request JSON is not an object",
        )
    return resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(data)


def build_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build the bounded v2 runtime-boundary summary view."""

    checks = list(
        result.get("local_relevance_medium_read_only_runtime_boundary_checks", [])
        if isinstance(
            result.get("local_relevance_medium_read_only_runtime_boundary_checks"),
            list,
        )
        else []
    )
    boundary = _mapping(result.get("local_relevance_medium_read_only_runtime_boundary"))
    statement = _mapping(
        result.get("local_relevance_medium_read_only_runtime_boundary_statement")
    )
    declared_question = _mapping(
        result.get("declared_local_relevance_medium_read_only_runtime_boundary_question")
    )
    block = _mapping(result.get("block"))
    non_claims = _mapping(result.get("non_claims"))
    failed_check_count = len(_failed_checks(checks))
    passed_check_count = _passed_count_from_checks(checks)

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "boundary_id": boundary.get("boundary_id"),
        "question": declared_question.get("question"),
        "intent": declared_question.get("intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "successor_of_resolver_module": (
            "resolve_local_relevance_medium_read_only_runtime_boundary_v0_min"
        ),
        "local_relevance_medium_read_only_runtime_boundary_recorded": statement.get(
            "local_relevance_medium_read_only_runtime_boundary_recorded"
        )
        is True,
        "basis_runtime_permission_artifact_preserved": statement.get(
            "basis_runtime_permission_artifact_preserved"
        )
        is True,
        "basis_operation_execution_artifact_preserved": statement.get(
            "basis_operation_execution_artifact_preserved"
        )
        is True,
        "selected_command": boundary.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved") is True,
        "selected_command_is_state": statement.get("selected_command_is_state") is True,
        "selected_runtime_permission_recorded": statement.get(
            "selected_runtime_permission_recorded"
        )
        is True,
        "runtime_permission_created": statement.get("runtime_permission_created") is True,
        "runtime_permission_local_only": statement.get("runtime_permission_local_only")
        is True,
        "runtime_permission_read_only": statement.get("runtime_permission_read_only")
        is True,
        "selected_operation_execution_recorded": statement.get(
            "selected_operation_execution_recorded"
        )
        is True,
        "operation_execution_created": statement.get("operation_execution_created") is True,
        "operation_execution_performed": statement.get("operation_execution_performed")
        is True,
        "operation_execution_local_only": statement.get("operation_execution_local_only")
        is True,
        "operation_execution_read_only": statement.get("operation_execution_read_only")
        is True,
        "future_runtime_may_be_considered": statement.get(
            "future_runtime_may_be_considered"
        )
        is True,
        "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved": statement.get(
            "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved"
        )
        is True,
        "runtime_boundary_v0_failure_evidence_preserved": statement.get(
            "runtime_boundary_v0_failure_evidence_preserved"
        )
        is True,
        "boundary_object_summary": {
            "boundary_type": boundary.get("boundary_type"),
            "boundary_scope": boundary.get("boundary_scope"),
            "boundary_version": boundary.get("boundary_version"),
            "selected_command": boundary.get("selected_command"),
            "runtime_permission_created": boundary.get("runtime_permission_created"),
            "runtime_permission_local_only": boundary.get("runtime_permission_local_only"),
            "runtime_permission_read_only": boundary.get("runtime_permission_read_only"),
            "operation_execution_created": boundary.get("operation_execution_created"),
            "operation_execution_performed": boundary.get("operation_execution_performed"),
            "operation_execution_local_only": boundary.get("operation_execution_local_only"),
            "operation_execution_read_only": boundary.get("operation_execution_read_only"),
            "future_runtime_may_be_considered": boundary.get(
                "future_runtime_may_be_considered"
            ),
        },
        "runtime_not_created": boundary.get("runtime_created") is False,
        "runtime_hosting_not_created": boundary.get("runtime_hosting_created") is False,
        "runtime_loop_not_created": boundary.get("runtime_loop_created") is False,
        "daemon_behavior_not_created": boundary.get("daemon_behavior_created") is False,
        "continuation_not_created": boundary.get("continuation_created") is False,
        "runtime_held_state_not_created": boundary.get("runtime_held_state_created")
        is False,
        "runtime_held_reentry_not_created": boundary.get("runtime_held_reentry_created")
        is False,
        "second_operation_not_created": boundary.get("second_operation_created") is False,
        "prior_result_reentry_cycle_not_created": boundary.get(
            "prior_result_reentry_cycle_created"
        )
        is False,
        "public_api_not_created": boundary.get("public_api_created") is False,
        "participant_facing_interface_not_created": boundary.get(
            "participant_facing_interface_created"
        )
        is False,
        "distributed_network_behavior_not_created": boundary.get(
            "distributed_network_behavior_created"
        )
        is False,
        "general_operation_permission_not_created": boundary.get(
            "general_operation_permission_created"
        )
        is False,
        "general_lookup_permission_not_created": boundary.get(
            "general_lookup_permission_created"
        )
        is False,
        "arbitrary_lookup_permission_not_created": boundary.get(
            "arbitrary_lookup_permission_created"
        )
        is False,
        "unsupported_commands_not_permitted": boundary.get(
            "unsupported_commands_permitted"
        )
        is False,
        "unsupported_lookup_keys_not_permitted": boundary.get(
            "unsupported_lookup_keys_permitted"
        )
        is False,
        "no_new_lookup_entry_created_beyond_bounded_lookup_result_object": (
            boundary.get("new_lookup_entry_created") is False
        ),
        "no_new_signal_entry_relevance_object_or_index_entry_created": all(
            boundary.get(field) is False
            for field in (
                "new_signal_accepted",
                "new_entry_accepted",
                "new_relevance_object_created",
                "new_index_entry_created",
            )
        ),
        "filesystem_discovery_not_performed": boundary.get(
            "filesystem_discovery_performed"
        )
        is False,
        "registry_search_query_surface_or_ranking_not_created": all(
            boundary.get(field) is False
            for field in (
                "registry_created",
                "search_surface_created",
                "query_surface_created",
                "ranking_surface_created",
            )
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": (
            all(
                boundary.get(field) is False
                for field in (
                    "scoring_surface_created",
                    "priority_surface_created",
                    "validity_judgment_created",
                    "truth_judgment_created",
                    "authority_judgment_created",
                    "currentness_judgment_created",
                )
            )
        ),
        "older_runtime_lineage_not_imported_as_authority": boundary.get(
            "older_runtime_lineage_imported_as_authority"
        )
        is False,
        "older_runtime_permission_not_treated_as_current": boundary.get(
            "older_runtime_permission_treated_as_current"
        )
        is False,
        "runtime_authority_not_imported": boundary.get("runtime_authority_imported")
        is False,
        "repeated_reception_permission_arbitrary_reception_feed_not_created": all(
            boundary.get(field) is False
            for field in (
                "repeated_reception_permission_created",
                "arbitrary_reception_created",
                "feed_created",
            )
        ),
        "source_authority_currentness_truth_synchronization_participation_not_created": (
            all(
                boundary.get(field) is False
                for field in (
                    "source_transfer_occurred",
                    "source_receipt_occurred",
                    "authority_created",
                    "currentness_created",
                    "truth_created",
                    "synchronization_created",
                    "participation_authorized",
                    "participant_role_created",
                )
            )
        ),
        "consumed_request_token_remains_closed": statement.get(
            "consumed_request_token_remains_closed"
        )
        is True,
        "authorization_token_reuse_blocked": statement.get(
            "authorization_token_reuse_blocked"
        )
        is True,
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved"
        )
        is True,
        "follow_on_not_created": boundary.get("follow_on_work_authorized") is False,
        "key_non_claims": {
            "runtime_created": non_claims.get("runtime_created"),
            "runtime_hosting_created": non_claims.get("runtime_hosting_created"),
            "runtime_loop_created": non_claims.get("runtime_loop_created"),
            "daemon_behavior_created": non_claims.get("daemon_behavior_created"),
            "continuation_created": non_claims.get("continuation_created"),
            "runtime_held_state_created": non_claims.get("runtime_held_state_created"),
            "runtime_held_reentry_created": non_claims.get(
                "runtime_held_reentry_created"
            ),
            "prior_result_reentry_cycle_created": non_claims.get(
                "prior_result_reentry_cycle_created"
            ),
            "older_runtime_lineage_imported_as_authority": non_claims.get(
                "older_runtime_lineage_imported_as_authority"
            ),
            "older_runtime_permission_treated_as_current": non_claims.get(
                "older_runtime_permission_treated_as_current"
            ),
            "runtime_authority_imported": non_claims.get("runtime_authority_imported"),
            "consumed_request_reopened": non_claims.get("consumed_request_reopened"),
            "authorization_token_reused": non_claims.get("authorization_token_reused"),
            "follow_on_work_authorized": non_claims.get("follow_on_work_authorized"),
        },
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _safe_filename_stem(value: Any) -> str:
    text = str(value or DEFAULT_BOUNDARY_ID)
    safe = "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in text)
    return safe.strip("_") or DEFAULT_BOUNDARY_ID


def write_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded v2 runtime-boundary result without overwriting JSON."""

    boundary = _mapping(result.get("local_relevance_medium_read_only_runtime_boundary"))
    boundary_id = boundary.get("boundary_id", DEFAULT_BOUNDARY_ID)
    if output_path is None:
        output_path = OUTPUT_ROOT / (
            f"{_safe_filename_stem(boundary_id)}__"
            "local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
        )
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = path
    if final_path.exists():
        stem = path.stem
        suffix = path.suffix
        counter = 1
        while True:
            candidate = path.with_name(f"{stem}_{counter:03d}{suffix}")
            if not candidate.exists():
                final_path = candidate
                break
            counter += 1
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path


def build_declared_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_request(
    *,
    local_relevance_medium_read_only_runtime_boundary_id: str = DEFAULT_BOUNDARY_ID,
    selected_runtime_permission_artifact: Path | str = DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
    selected_operation_execution_artifact: Path | str = DEFAULT_OPERATION_EXECUTION_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    runtime_boundary_intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, bool] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    """Build a bounded declared request for the selected-state runtime boundary."""

    request = {
        "local_relevance_medium_read_only_runtime_boundary_id": (
            local_relevance_medium_read_only_runtime_boundary_id
        ),
        "local_relevance_medium_read_only_runtime_boundary_question": CORE_QUESTION,
        "local_relevance_medium_read_only_runtime_boundary_intent": (
            runtime_boundary_intent
        ),
        "selected_runtime_permission_artifact": str(selected_runtime_permission_artifact),
        "selected_operation_execution_artifact": str(selected_operation_execution_artifact),
        "selected_command": selected_command,
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "future_runtime_may_be_considered": True,
        "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
        "declared_non_claims": (
            dict(declared_non_claims)
            if declared_non_claims is not None
            else _canonical_false_non_claims()
        ),
    }
    request.update(_sanitize(extra_fields))
    return request
