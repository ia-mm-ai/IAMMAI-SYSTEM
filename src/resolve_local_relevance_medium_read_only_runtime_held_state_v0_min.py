"""Resolve one local read-only runtime-held-state object for selected command state.

This resolver is intentionally narrow: it reads one selected runtime-held-state
boundary artifact, one selected runtime v3 artifact, one selected runtime
boundary v2 artifact, one selected runtime permission artifact, and one selected
operation execution artifact. It records one basis-reference-only held-state
object and does not create hosting, loop, daemon, continuation, re-entry, second
operation, public API, distributed behavior, registry, search, ranking, authority,
currentness, truth, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyRuntimeHeldStateV0MinError(Exception):
    """Bounded resolver error for runtime-held-state result writing and reading."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_runtime_held_state_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_v0_min"
)

SELECTED_COMMAND = "state"
HELD_STATE_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE"
HELD_STATE_SCOPE = "SELECTED_RUNTIME_HELD_STATE_ONLY"
HELD_STATE_ID = "local_relevance_medium_read_only_runtime_held_state_001"

SUPPORTED_HELD_STATE_TYPE_VALUES = (HELD_STATE_TYPE,)
SUPPORTED_HELD_STATE_SCOPE_VALUES = (HELD_STATE_SCOPE,)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min/"
    "local_relevance_medium_read_only_runtime_held_state_boundary_reference_review_001__"
    "local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result.json"
)
DEFAULT_RUNTIME_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v3/"
    "local_relevance_medium_read_only_runtime_reference_review_001__"
    "local_relevance_medium_read_only_runtime_v0_min_v3_result.json"
)
DEFAULT_RUNTIME_BOUNDARY_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min_v2/"
    "local_relevance_medium_read_only_runtime_boundary_reference_review_001__"
    "local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
)
DEFAULT_RUNTIME_PERMISSION_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min/"
    "local_relevance_medium_read_only_runtime_permission_reference_review_001__"
    "local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
)
DEFAULT_OPERATION_EXECUTION_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min/"
    "local_relevance_medium_read_only_operation_execution_reference_review_001__"
    "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
)

EXPECTED_RUNTIME_HELD_STATE_BOUNDARY_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_RECORDED"
)
EXPECTED_RUNTIME_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED"
EXPECTED_RUNTIME_BOUNDARY_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED"
EXPECTED_RUNTIME_PERMISSION_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED"
)
EXPECTED_OPERATION_EXECUTION_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "continuation_created",
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
    "artifact_existence_treated_as_runtime_held_state_authority",
    "latest_file_posture_treated_as_runtime_held_state_authority",
    "repo_local_availability_treated_as_runtime_held_state_authority",
    "hidden_repo_state_used_as_runtime_held_state_content",
    "hidden_repo_state_used_as_runtime_held_state_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "runtime_v0_failure_repaired",
    "runtime_v0_failure_hidden",
    "runtime_v0_failure_claimed_passed",
    "runtime_v2_failure_repaired",
    "runtime_v2_failure_hidden",
    "runtime_v2_failure_claimed_passed",
    "runtime_boundary_v0_failure_repaired",
    "runtime_boundary_v0_failure_hidden",
    "runtime_boundary_v0_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_runtime_held_state_recorded",
    "basis_runtime_held_state_boundary_artifact_preserved",
    "basis_runtime_artifact_preserved",
    "basis_runtime_boundary_artifact_preserved",
    "basis_runtime_permission_artifact_preserved",
    "basis_operation_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_runtime_held_state_boundary_recorded",
    "future_runtime_held_state_may_be_considered",
    "selected_runtime_recorded",
    "runtime_created",
    "runtime_local_only",
    "runtime_read_only",
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
    "runtime_held_state_created",
    "runtime_held_state_local_only",
    "runtime_held_state_read_only",
    "held_state_basis_reference_only",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BLOCK_REQUESTED",
    "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_PATH_MISSING",
    "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_UNREADABLE",
    "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "RUNTIME_ARTIFACT_PATH_MISSING",
    "RUNTIME_ARTIFACT_UNREADABLE",
    "RUNTIME_ARTIFACT_NOT_JSON_OBJECT",
    "RUNTIME_ARTIFACT_NOT_RECORDED",
    "RUNTIME_ARTIFACT_FAILED_CHECKS_PRESENT",
    "RUNTIME_ARTIFACT_VERSION_NOT_0_1_0",
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
    "SELECTED_RUNTIME_HELD_STATE_BOUNDARY_NOT_RECORDED",
    "FUTURE_RUNTIME_HELD_STATE_MAY_NOT_BE_CONSIDERED",
    "SELECTED_RUNTIME_NOT_RECORDED",
    "RUNTIME_NOT_CREATED",
    "RUNTIME_LOCAL_ONLY_NOT_TRUE",
    "RUNTIME_READ_ONLY_NOT_TRUE",
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
    "HELD_STATE_TYPE_MISSING",
    "HELD_STATE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE",
    "HELD_STATE_SCOPE_MISSING",
    "HELD_STATE_SCOPE_NOT_SELECTED_RUNTIME_HELD_STATE_ONLY",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_NOT_RECORDED",
    "RUNTIME_HELD_STATE_NOT_CREATED",
    "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE",
    "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE",
    "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "RAW_STATE_BODY_EMBEDDED",
    "STATE_MUTATION_PERFORMED",
    "STATE_UPDATE_PERFORMED",
    "RUNTIME_HOSTING_CREATED",
    "RUNTIME_LOOP_CREATED",
    "DAEMON_BEHAVIOR_CREATED",
    "CONTINUATION_CREATED",
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
    "RUNTIME_V0_FAILURE_REPAIRED",
    "RUNTIME_V0_FAILURE_HIDDEN",
    "RUNTIME_V0_FAILURE_CLAIMED_PASSED",
    "RUNTIME_V2_FAILURE_REPAIRED",
    "RUNTIME_V2_FAILURE_HIDDEN",
    "RUNTIME_V2_FAILURE_CLAIMED_PASSED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HELD_STATE_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HELD_STATE_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HELD_STATE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HELD_STATE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HELD_STATE_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_REQUEST_UNREADABLE",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_runtime_held_state_body",
    "raw_runtime_held_state_boundary_body",
    "raw_runtime_body",
    "raw_runtime_boundary_body",
    "raw_runtime_permission_body",
    "raw_operation_execution_body",
    "raw_runtime_hosting_body",
    "raw_runtime_loop_body",
    "raw_daemon_body",
    "raw_continuation_body",
    "raw_runtime_held_reentry_body",
    "raw_second_operation_body",
    "raw_prior_result_reentry_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "runtime_held_state_body",
    "runtime_held_state_boundary_body",
    "runtime_body",
    "runtime_boundary_body",
    "runtime_permission_body",
    "operation_execution_body",
    "runtime_hosting_body",
    "runtime_loop_body",
    "daemon_body",
    "continuation_body",
    "runtime_held_reentry_body",
    "second_operation_body",
    "prior_result_reentry_body",
    "source_body",
    "authority_body",
    "currentness_body",
    "public_api_body",
    "participant_facing_interface_body",
    "distributed_network_behavior_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

HOSTILE_SENTINELS = (
    "RAW_RUNTIME_HELD_STATE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_STATE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "RAW_PRIOR_RESULT_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

TOP_LEVEL_BLOCK_FIELD_CODES = {
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "older_runtime_lineage_imported_as_authority": "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
    "older_runtime_permission_treated_as_current": "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
    "runtime_authority_imported": "RUNTIME_AUTHORITY_IMPORTED",
    "raw_state_body_embedded": "RAW_STATE_BODY_EMBEDDED",
    "state_mutation_performed": "STATE_MUTATION_PERFORMED",
    "state_update_performed": "STATE_UPDATE_PERFORMED",
    "runtime_v0_failure_repaired": "RUNTIME_V0_FAILURE_REPAIRED",
    "runtime_v0_failure_hidden": "RUNTIME_V0_FAILURE_HIDDEN",
    "runtime_v0_failure_claimed_passed": "RUNTIME_V0_FAILURE_CLAIMED_PASSED",
    "runtime_v2_failure_repaired": "RUNTIME_V2_FAILURE_REPAIRED",
    "runtime_v2_failure_hidden": "RUNTIME_V2_FAILURE_HIDDEN",
    "runtime_v2_failure_claimed_passed": "RUNTIME_V2_FAILURE_CLAIMED_PASSED",
    "runtime_boundary_v0_failure_repaired": "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
    "runtime_boundary_v0_failure_hidden": "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN",
    "runtime_boundary_v0_failure_claimed_passed": "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
    "runtime_hosting_created": "RUNTIME_HOSTING_CREATED",
    "runtime_loop_created": "RUNTIME_LOOP_CREATED",
    "daemon_behavior_created": "DAEMON_BEHAVIOR_CREATED",
    "continuation_created": "CONTINUATION_CREATED",
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
    "artifact_existence_treated_as_runtime_held_state_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HELD_STATE_AUTHORITY"
    ),
    "latest_file_posture_treated_as_runtime_held_state_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HELD_STATE_AUTHORITY"
    ),
    "repo_local_availability_treated_as_runtime_held_state_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HELD_STATE_AUTHORITY"
    ),
    "hidden_repo_state_used_as_runtime_held_state_content": (
        "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HELD_STATE_CONTENT"
    ),
    "hidden_repo_state_used_as_runtime_held_state_authority": (
        "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HELD_STATE_AUTHORITY"
    ),
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
}

SHORTCUT_BLOCK_FIELD_CODES = {
    "runtime_held_state_boundary_artifact_missing": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_PATH_MISSING",
    "runtime_held_state_boundary_artifact_not_recorded": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "runtime_held_state_boundary_artifact_failed_checks_present": (
        "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "runtime_held_state_boundary_artifact_version_not_0_1_0": (
        "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "runtime_artifact_missing": "RUNTIME_ARTIFACT_PATH_MISSING",
    "runtime_artifact_not_recorded": "RUNTIME_ARTIFACT_NOT_RECORDED",
    "runtime_artifact_failed_checks_present": "RUNTIME_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_artifact_version_not_0_1_0": "RUNTIME_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_boundary_artifact_missing": "RUNTIME_BOUNDARY_ARTIFACT_PATH_MISSING",
    "runtime_boundary_artifact_not_recorded": "RUNTIME_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "runtime_boundary_artifact_failed_checks_present": (
        "RUNTIME_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "runtime_boundary_artifact_version_not_0_1_0": "RUNTIME_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_permission_artifact_missing": "RUNTIME_PERMISSION_ARTIFACT_PATH_MISSING",
    "runtime_permission_artifact_not_recorded": "RUNTIME_PERMISSION_ARTIFACT_NOT_RECORDED",
    "runtime_permission_artifact_failed_checks_present": (
        "RUNTIME_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "runtime_permission_artifact_version_not_0_1_0": (
        "RUNTIME_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "operation_execution_artifact_missing": "OPERATION_EXECUTION_ARTIFACT_PATH_MISSING",
    "operation_execution_artifact_not_recorded": "OPERATION_EXECUTION_ARTIFACT_NOT_RECORDED",
    "operation_execution_artifact_failed_checks_present": (
        "OPERATION_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "operation_execution_artifact_version_not_0_1_0": (
        "OPERATION_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "selected_command_missing": "SELECTED_COMMAND_MISSING",
    "selected_command_not_state": "SELECTED_COMMAND_NOT_STATE",
    "selected_runtime_held_state_boundary_not_recorded": (
        "SELECTED_RUNTIME_HELD_STATE_BOUNDARY_NOT_RECORDED"
    ),
    "future_runtime_held_state_may_not_be_considered": (
        "FUTURE_RUNTIME_HELD_STATE_MAY_NOT_BE_CONSIDERED"
    ),
    "selected_runtime_not_recorded": "SELECTED_RUNTIME_NOT_RECORDED",
    "runtime_not_created": "RUNTIME_NOT_CREATED",
    "runtime_local_only_not_true": "RUNTIME_LOCAL_ONLY_NOT_TRUE",
    "runtime_read_only_not_true": "RUNTIME_READ_ONLY_NOT_TRUE",
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
    "held_state_type_not_local_relevance_medium_read_only_runtime_held_state": (
        "HELD_STATE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE"
    ),
    "held_state_scope_not_selected_runtime_held_state_only": (
        "HELD_STATE_SCOPE_NOT_SELECTED_RUNTIME_HELD_STATE_ONLY"
    ),
    "local_relevance_medium_read_only_runtime_held_state_not_recorded": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_NOT_RECORDED"
    ),
    "runtime_held_state_not_created": "RUNTIME_HELD_STATE_NOT_CREATED",
    "runtime_held_state_local_only_not_true": "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE",
    "runtime_held_state_read_only_not_true": "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE",
    "held_state_basis_reference_only_not_true": "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE",
}

ARTIFACT_SPECS = (
    {
        "path_key": "selected_runtime_held_state_boundary_artifact",
        "basis_name": "selected_runtime_held_state_boundary_artifact_basis",
        "label": "runtime-held-state boundary artifact",
        "prefix": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_HELD_STATE_BOUNDARY_OUTCOME,
    },
    {
        "path_key": "selected_runtime_artifact",
        "basis_name": "selected_runtime_artifact_basis",
        "label": "runtime artifact",
        "prefix": "RUNTIME_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_OUTCOME,
    },
    {
        "path_key": "selected_runtime_boundary_artifact",
        "basis_name": "selected_runtime_boundary_artifact_basis",
        "label": "runtime boundary artifact",
        "prefix": "RUNTIME_BOUNDARY_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
    },
    {
        "path_key": "selected_runtime_permission_artifact",
        "basis_name": "selected_runtime_permission_artifact_basis",
        "label": "runtime permission artifact",
        "prefix": "RUNTIME_PERMISSION_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_PERMISSION_OUTCOME,
    },
    {
        "path_key": "selected_operation_execution_artifact",
        "basis_name": "selected_operation_execution_artifact_basis",
        "label": "operation execution artifact",
        "prefix": "OPERATION_EXECUTION_ARTIFACT",
        "expected_outcome": EXPECTED_OPERATION_EXECUTION_OUTCOME,
    },
)

WHAT_REMAINS_OPEN = (
    "local relevance medium read-only runtime-held state test",
    "local relevance medium read-only runtime-held state live artifact",
    "local relevance medium read-only runtime-held state terminal summary, if needed",
    "runtime hosting",
    "runtime loop",
    "daemon behavior",
    "continuation",
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
)


def _is_mapping(value: Any) -> bool:
    return isinstance(value, MappingABC)


def _is_sensitive_key(key: str | None) -> bool:
    if not key:
        return False
    return key in SENSITIVE_CONTENT_KEYS or key.endswith("_body")


def _sanitize(value: Any, key: str | None = None) -> Any:
    if _is_sensitive_key(key):
        return "[REDACTED]"
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        sanitized = value
        for sentinel in HOSTILE_SENTINELS:
            sanitized = sanitized.replace(sentinel, "[REDACTED]")
        return sanitized
    if _is_mapping(value):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, key) for item in value]
    return value


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


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
    if not passed:
        check["block_code"] = code or "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_REQUEST_MALFORMED"
        check["failure_code"] = check["block_code"]
    return check


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    checks.append(_make_check(check_name, passed, expected_posture, actual_posture, code))


def _first_failed_code(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code:
                return code
    return None


def _find_first_key(value: Any, key_names: tuple[str, ...]) -> Any:
    if _is_mapping(value):
        for key in key_names:
            if key in value:
                return value[key]
        for nested_key, nested_value in value.items():
            if _is_sensitive_key(str(nested_key)):
                continue
            found = _find_first_key(nested_value, key_names)
            if found is not None:
                return found
    elif isinstance(value, list):
        for item in value:
            found = _find_first_key(item, key_names)
            if found is not None:
                return found
    return None


def _find_checks(value: Any) -> list[dict[str, Any]]:
    if _is_mapping(value):
        collected: list[dict[str, Any]] = []
        for key, nested_value in value.items():
            if _is_sensitive_key(str(key)):
                continue
            if str(key).endswith("_checks") or str(key) == "checks":
                if isinstance(nested_value, list):
                    collected.extend([item for item in nested_value if _is_mapping(item)])
            else:
                collected.extend(_find_checks(nested_value))
        return collected
    if isinstance(value, list):
        collected = []
        for item in value:
            collected.extend(_find_checks(item))
        return collected
    return []


def _extract_failed_check_count(artifact: Mapping[str, Any]) -> Any:
    direct = _find_first_key(artifact, ("failed_check_count",))
    if isinstance(direct, int) and not isinstance(direct, bool):
        return direct
    checks = _find_checks(artifact)
    if checks:
        return sum(1 for check in checks if check.get("passed") is not True)
    return None


def _read_json_object(path_value: Any) -> tuple[dict[str, Any] | None, str | None]:
    try:
        path = Path(path_value)
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - bounded into resolver result.
        return None, f"{exc.__class__.__name__}: {exc}"
    if not _is_mapping(data):
        return None, "JSON value is not an object"
    return dict(data), None


def _read_basis_artifact(
    request: Mapping[str, Any],
    spec: Mapping[str, str],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    path_key = spec["path_key"]
    prefix = spec["prefix"]
    label = spec["label"]
    expected_outcome = spec["expected_outcome"]
    path_value = request.get(path_key)
    path_declared = isinstance(path_value, (str, Path)) and str(path_value) != ""

    basis: dict[str, Any] = {
        "artifact_path": _sanitize(path_value),
        "artifact_readable_json": False,
        "artifact_json_object": False,
        "outcome": None,
        "result_version": None,
        "failed_check_count": None,
        "artifact_preserved": False,
    }

    _add_check(
        checks,
        f"{label} path declared",
        path_declared,
        "declared path",
        path_value,
        f"{prefix}_PATH_MISSING",
    )
    if not path_declared:
        return basis, None

    artifact, read_error = _read_json_object(path_value)
    not_json_object = read_error == "JSON value is not an object"
    readable = (artifact is not None and read_error is None) or not_json_object
    _add_check(
        checks,
        f"{label} readable JSON",
        readable,
        "readable JSON object",
        read_error or "readable",
        f"{prefix}_UNREADABLE",
    )
    if not readable:
        return basis, None
    if not_json_object:
        basis["artifact_readable_json"] = True
        _add_check(
            checks,
            f"{label} JSON object",
            False,
            "JSON object",
            "JSON value is not an object",
            f"{prefix}_NOT_JSON_OBJECT",
        )
        return basis, None

    basis["artifact_readable_json"] = True
    basis["artifact_json_object"] = True
    _add_check(
        checks,
        f"{label} JSON object",
        True,
        "JSON object",
        "JSON object",
        f"{prefix}_NOT_JSON_OBJECT",
    )

    outcome = _find_first_key(artifact, ("outcome",))
    result_version = _find_first_key(artifact, ("result_version",))
    failed_check_count = _extract_failed_check_count(artifact)

    basis["outcome"] = _sanitize(outcome)
    basis["result_version"] = _sanitize(result_version)
    basis["failed_check_count"] = failed_check_count

    _add_check(
        checks,
        f"{label} outcome recorded",
        outcome == expected_outcome,
        expected_outcome,
        outcome,
        f"{prefix}_NOT_RECORDED",
    )
    _add_check(
        checks,
        f"{label} result version 0.1.0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version,
        f"{prefix}_VERSION_NOT_0_1_0",
    )
    _add_check(
        checks,
        f"{label} failed check count zero",
        failed_check_count == 0,
        0,
        failed_check_count,
        f"{prefix}_FAILED_CHECKS_PRESENT",
    )

    basis["artifact_preserved"] = (
        outcome == expected_outcome and result_version == RESULT_VERSION and failed_check_count == 0
    )
    return basis, artifact


def _request_value(request: Mapping[str, Any], key: str, default: Any = None) -> Any:
    return request.get(key, default)


def _validate_request_shape(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    question = request.get("local_relevance_medium_read_only_runtime_held_state_question")
    question_declared = isinstance(question, str) and question.strip() != ""
    _add_check(
        checks,
        "runtime-held state question declared",
        question_declared,
        "declared runtime-held state question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_QUESTION_UNDECLARED",
    )

    intent = request.get("local_relevance_medium_read_only_runtime_held_state_intent")
    _add_check(
        checks,
        "runtime-held state intent supported",
        intent in SUPPORTED_INTENTS and intent != INTENT_BLOCK,
        f"one of {SUPPORTED_INTENTS[:-1]}",
        intent,
        (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BLOCK_REQUESTED"
            if intent == INTENT_BLOCK
            else "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_INTENT_UNSUPPORTED"
        ),
    )

    selected_command = request.get("selected_command")
    _add_check(
        checks,
        "selected command declared",
        selected_command is not None and selected_command != "",
        "selected command declared",
        selected_command,
        "SELECTED_COMMAND_MISSING",
    )
    _add_check(
        checks,
        "selected command exactly state",
        selected_command == SELECTED_COMMAND,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _add_check(
        checks,
        "selected command is state",
        selected_command == SELECTED_COMMAND,
        True,
        selected_command == SELECTED_COMMAND,
        "SELECTED_COMMAND_NOT_STATE",
    )

    held_state_type = request.get("held_state_type")
    _add_check(
        checks,
        "held state type declared",
        held_state_type is not None and held_state_type != "",
        HELD_STATE_TYPE,
        held_state_type,
        "HELD_STATE_TYPE_MISSING",
    )
    _add_check(
        checks,
        "held state type exact",
        held_state_type == HELD_STATE_TYPE,
        HELD_STATE_TYPE,
        held_state_type,
        "HELD_STATE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE",
    )

    held_state_scope = request.get("held_state_scope")
    _add_check(
        checks,
        "held state scope declared",
        held_state_scope is not None and held_state_scope != "",
        HELD_STATE_SCOPE,
        held_state_scope,
        "HELD_STATE_SCOPE_MISSING",
    )
    _add_check(
        checks,
        "held state scope exact",
        held_state_scope == HELD_STATE_SCOPE,
        HELD_STATE_SCOPE,
        held_state_scope,
        "HELD_STATE_SCOPE_NOT_SELECTED_RUNTIME_HELD_STATE_ONLY",
    )


def _validate_shortcuts(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for key, code in {**SHORTCUT_BLOCK_FIELD_CODES, **TOP_LEVEL_BLOCK_FIELD_CODES}.items():
        if request.get(key) is True:
            _add_check(
                checks,
                f"{key} not asserted",
                False,
                False,
                True,
                code,
            )


def _validate_declared_non_claims(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    declared = request.get("declared_non_claims")
    if not _is_mapping(declared):
        _add_check(
            checks,
            "declared non-claims mapping present",
            False,
            "mapping with required false non-claims",
            declared,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return

    _add_check(
        checks,
        "declared non-claims mapping present",
        True,
        "mapping with required false non-claims",
        "mapping",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    for key in REQUIRED_FALSE_NON_CLAIMS:
        value = declared.get(key)
        _add_check(
            checks,
            f"required non-claim {key} false",
            isinstance(value, bool) and value is False,
            False,
            value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _build_held_state_object(
    request: Mapping[str, Any],
    bases: Mapping[str, Mapping[str, Any]],
    recorded: bool,
) -> dict[str, Any]:
    selected_command = _request_value(request, "selected_command", SELECTED_COMMAND)
    return {
        "held_state_id": _request_value(
            request,
            "local_relevance_medium_read_only_runtime_held_state_id",
            HELD_STATE_ID,
        ),
        "held_state_type": _request_value(request, "held_state_type", HELD_STATE_TYPE),
        "held_state_version": RESULT_VERSION,
        "held_state_scope": _request_value(request, "held_state_scope", HELD_STATE_SCOPE),
        "basis_runtime_held_state_boundary_artifact": _request_value(
            request,
            "selected_runtime_held_state_boundary_artifact",
            DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT,
        ),
        "basis_runtime_held_state_boundary_outcome": bases[
            "selected_runtime_held_state_boundary_artifact_basis"
        ].get("outcome"),
        "basis_runtime_held_state_boundary_result_version": bases[
            "selected_runtime_held_state_boundary_artifact_basis"
        ].get("result_version"),
        "basis_runtime_held_state_boundary_failed_check_count": bases[
            "selected_runtime_held_state_boundary_artifact_basis"
        ].get("failed_check_count"),
        "basis_runtime_artifact": _request_value(
            request,
            "selected_runtime_artifact",
            DEFAULT_RUNTIME_ARTIFACT,
        ),
        "basis_runtime_outcome": bases["selected_runtime_artifact_basis"].get("outcome"),
        "basis_runtime_result_version": bases["selected_runtime_artifact_basis"].get("result_version"),
        "basis_runtime_failed_check_count": bases["selected_runtime_artifact_basis"].get(
            "failed_check_count"
        ),
        "basis_runtime_boundary_artifact": _request_value(
            request,
            "selected_runtime_boundary_artifact",
            DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
        ),
        "basis_runtime_boundary_outcome": bases["selected_runtime_boundary_artifact_basis"].get(
            "outcome"
        ),
        "basis_runtime_boundary_result_version": bases[
            "selected_runtime_boundary_artifact_basis"
        ].get("result_version"),
        "basis_runtime_boundary_failed_check_count": bases[
            "selected_runtime_boundary_artifact_basis"
        ].get("failed_check_count"),
        "basis_runtime_permission_artifact": _request_value(
            request,
            "selected_runtime_permission_artifact",
            DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
        ),
        "basis_runtime_permission_outcome": bases["selected_runtime_permission_artifact_basis"].get(
            "outcome"
        ),
        "basis_runtime_permission_result_version": bases[
            "selected_runtime_permission_artifact_basis"
        ].get("result_version"),
        "basis_runtime_permission_failed_check_count": bases[
            "selected_runtime_permission_artifact_basis"
        ].get("failed_check_count"),
        "basis_operation_execution_artifact": _request_value(
            request,
            "selected_operation_execution_artifact",
            DEFAULT_OPERATION_EXECUTION_ARTIFACT,
        ),
        "basis_operation_execution_outcome": bases["selected_operation_execution_artifact_basis"].get(
            "outcome"
        ),
        "basis_operation_execution_result_version": bases[
            "selected_operation_execution_artifact_basis"
        ].get("result_version"),
        "basis_operation_execution_failed_check_count": bases[
            "selected_operation_execution_artifact_basis"
        ].get("failed_check_count"),
        "selected_command": selected_command,
        "selected_command_is_state": selected_command == SELECTED_COMMAND,
        "selected_runtime_held_state_boundary_recorded": recorded,
        "future_runtime_held_state_may_be_considered": recorded,
        "selected_runtime_recorded": recorded,
        "runtime_created": recorded,
        "runtime_local_only": recorded,
        "runtime_read_only": recorded,
        "selected_runtime_boundary_recorded": recorded,
        "future_runtime_may_be_considered": recorded,
        "selected_runtime_permission_recorded": recorded,
        "runtime_permission_created": recorded,
        "runtime_permission_local_only": recorded,
        "runtime_permission_read_only": recorded,
        "selected_operation_execution_recorded": recorded,
        "operation_execution_created": recorded,
        "operation_execution_performed": recorded,
        "operation_execution_local_only": recorded,
        "operation_execution_read_only": recorded,
        "local_relevance_medium_read_only_runtime_held_state_recorded": recorded,
        "runtime_held_state_created": recorded,
        "runtime_held_state_local_only": recorded,
        "runtime_held_state_read_only": recorded,
        "held_state_basis_reference_only": recorded,
        "raw_state_body_embedded": False,
        "state_mutation_performed": False,
        "state_update_performed": False,
        "runtime_hosting_created": False,
        "runtime_loop_created": False,
        "daemon_behavior_created": False,
        "continuation_created": False,
        "runtime_held_reentry_created": False,
        "second_operation_created": False,
        "prior_result_reentry_cycle_created": False,
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
        "older_runtime_lineage_imported_as_authority": False,
        "older_runtime_permission_treated_as_current": False,
        "runtime_authority_imported": False,
        "runtime_v0_failure_evidence_preserved": True,
        "runtime_v2_failure_evidence_preserved": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
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


def _build_statement(held_state: Mapping[str, Any], recorded: bool) -> dict[str, Any]:
    return {
        "local_relevance_medium_read_only_runtime_held_state_recorded": recorded,
        "basis_runtime_held_state_boundary_artifact_preserved": recorded,
        "basis_runtime_artifact_preserved": recorded,
        "basis_runtime_boundary_artifact_preserved": recorded,
        "basis_runtime_permission_artifact_preserved": recorded,
        "basis_operation_execution_artifact_preserved": recorded,
        "selected_command_preserved": held_state.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": held_state.get("selected_command_is_state") is True,
        "selected_runtime_held_state_boundary_recorded": held_state.get(
            "selected_runtime_held_state_boundary_recorded"
        )
        is True,
        "future_runtime_held_state_may_be_considered": held_state.get(
            "future_runtime_held_state_may_be_considered"
        )
        is True,
        "selected_runtime_recorded": held_state.get("selected_runtime_recorded") is True,
        "runtime_created": held_state.get("runtime_created") is True,
        "runtime_local_only": held_state.get("runtime_local_only") is True,
        "runtime_read_only": held_state.get("runtime_read_only") is True,
        "selected_runtime_boundary_recorded": held_state.get("selected_runtime_boundary_recorded")
        is True,
        "future_runtime_may_be_considered": held_state.get("future_runtime_may_be_considered")
        is True,
        "selected_runtime_permission_recorded": held_state.get(
            "selected_runtime_permission_recorded"
        )
        is True,
        "runtime_permission_created": held_state.get("runtime_permission_created") is True,
        "runtime_permission_local_only": held_state.get("runtime_permission_local_only") is True,
        "runtime_permission_read_only": held_state.get("runtime_permission_read_only") is True,
        "selected_operation_execution_recorded": held_state.get(
            "selected_operation_execution_recorded"
        )
        is True,
        "operation_execution_created": held_state.get("operation_execution_created") is True,
        "operation_execution_performed": held_state.get("operation_execution_performed") is True,
        "operation_execution_local_only": held_state.get("operation_execution_local_only") is True,
        "operation_execution_read_only": held_state.get("operation_execution_read_only") is True,
        "runtime_held_state_created": held_state.get("runtime_held_state_created") is True,
        "runtime_held_state_local_only": held_state.get("runtime_held_state_local_only") is True,
        "runtime_held_state_read_only": held_state.get("runtime_held_state_read_only") is True,
        "held_state_basis_reference_only": held_state.get("held_state_basis_reference_only") is True,
        "raw_state_body_embedded": False,
        "state_mutation_performed": False,
        "state_update_performed": False,
        "runtime_v0_failure_evidence_preserved": True,
        "runtime_v2_failure_evidence_preserved": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }


def _add_generated_object_checks(
    checks: list[dict[str, Any]],
    held_state: Mapping[str, Any],
    recorded: bool,
) -> None:
    true_checks = {
        "selected runtime-held-state boundary recorded": "selected_runtime_held_state_boundary_recorded",
        "future runtime-held state may be considered": "future_runtime_held_state_may_be_considered",
        "selected runtime recorded": "selected_runtime_recorded",
        "runtime created": "runtime_created",
        "runtime local only": "runtime_local_only",
        "runtime read only": "runtime_read_only",
        "selected runtime boundary recorded": "selected_runtime_boundary_recorded",
        "future runtime may be considered": "future_runtime_may_be_considered",
        "selected runtime permission recorded": "selected_runtime_permission_recorded",
        "runtime permission created": "runtime_permission_created",
        "runtime permission local only": "runtime_permission_local_only",
        "runtime permission read only": "runtime_permission_read_only",
        "selected operation execution recorded": "selected_operation_execution_recorded",
        "operation execution created": "operation_execution_created",
        "operation execution performed": "operation_execution_performed",
        "operation execution local only": "operation_execution_local_only",
        "operation execution read only": "operation_execution_read_only",
        "local relevance medium read-only runtime-held state recorded": (
            "local_relevance_medium_read_only_runtime_held_state_recorded"
        ),
        "runtime-held state created": "runtime_held_state_created",
        "runtime-held state local only": "runtime_held_state_local_only",
        "runtime-held state read only": "runtime_held_state_read_only",
        "held state basis reference only": "held_state_basis_reference_only",
        "runtime v0 failure evidence preserved": "runtime_v0_failure_evidence_preserved",
        "runtime v2 failure evidence preserved": "runtime_v2_failure_evidence_preserved",
        "runtime boundary v0 failure evidence preserved": (
            "runtime_boundary_v0_failure_evidence_preserved"
        ),
    }
    true_failure_codes = {
        "local_relevance_medium_read_only_runtime_held_state_recorded": (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_NOT_RECORDED"
        ),
        "runtime_held_state_created": "RUNTIME_HELD_STATE_NOT_CREATED",
        "runtime_held_state_local_only": "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE",
        "runtime_held_state_read_only": "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE",
        "held_state_basis_reference_only": "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE",
    }
    for check_name, key in true_checks.items():
        expected = True if recorded else False
        value = held_state.get(key)
        _add_check(
            checks,
            check_name,
            value is expected,
            expected,
            value,
            true_failure_codes.get(key, "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_REQUEST_MALFORMED"),
        )

    false_checks = {
        "raw state body not embedded": "raw_state_body_embedded",
        "state mutation not performed": "state_mutation_performed",
        "state update not performed": "state_update_performed",
        "runtime hosting not created": "runtime_hosting_created",
        "runtime loop not created": "runtime_loop_created",
        "daemon behavior not created": "daemon_behavior_created",
        "continuation not created": "continuation_created",
        "runtime-held re-entry not created": "runtime_held_reentry_created",
        "second operation not created": "second_operation_created",
        "prior-result re-entry cycle not created": "prior_result_reentry_cycle_created",
        "public API not created": "public_api_created",
        "participant-facing interface not created": "participant_facing_interface_created",
        "distributed network behavior not created": "distributed_network_behavior_created",
        "general operation permission not created": "general_operation_permission_created",
        "general lookup permission not created": "general_lookup_permission_created",
        "arbitrary lookup permission not created": "arbitrary_lookup_permission_created",
        "unsupported commands not permitted": "unsupported_commands_permitted",
        "unsupported lookup keys not permitted": "unsupported_lookup_keys_permitted",
        "no new lookup entry created beyond bounded lookup result object": "new_lookup_entry_created",
        "no new signal accepted": "new_signal_accepted",
        "no new entry accepted": "new_entry_accepted",
        "no new relevance object created beyond bounded lookup result object": "new_relevance_object_created",
        "no new index entry created": "new_index_entry_created",
        "filesystem discovery not performed": "filesystem_discovery_performed",
        "registry not created": "registry_created",
        "search not created": "search_surface_created",
        "query surface not created": "query_surface_created",
        "ranking not created": "ranking_surface_created",
        "scoring not created": "scoring_surface_created",
        "priority not created": "priority_surface_created",
        "validity judgment not created": "validity_judgment_created",
        "truth judgment not created": "truth_judgment_created",
        "authority judgment not created": "authority_judgment_created",
        "currentness judgment not created": "currentness_judgment_created",
        "older runtime lineage not imported as authority": "older_runtime_lineage_imported_as_authority",
        "older runtime permission not treated as current": "older_runtime_permission_treated_as_current",
        "runtime authority not imported": "runtime_authority_imported",
        "repeated reception permission not created": "repeated_reception_permission_created",
        "arbitrary reception not created": "arbitrary_reception_created",
        "feed not created": "feed_created",
        "source transfer not created": "source_transfer_occurred",
        "source receipt not created": "source_receipt_occurred",
        "authority not created": "authority_created",
        "currentness not created": "currentness_created",
        "truth not created": "truth_created",
        "synchronization not created": "synchronization_created",
        "participation not authorized": "participation_authorized",
        "participant role not created": "participant_role_created",
        "consumed request not reopened": "consumed_request_reopened",
        "authorization token not reused": "authorization_token_reused",
        "follow-on work not authorized": "follow_on_work_authorized",
    }
    for check_name, key in false_checks.items():
        _add_check(
            checks,
            check_name,
            held_state.get(key) is False,
            False,
            held_state.get(key),
            TOP_LEVEL_BLOCK_FIELD_CODES.get(key, "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_REQUEST_MALFORMED"),
        )


def _basis_map_with_defaults() -> dict[str, dict[str, Any]]:
    return {
        str(spec["basis_name"]): {
            "artifact_path": None,
            "artifact_readable_json": False,
            "artifact_json_object": False,
            "outcome": None,
            "result_version": None,
            "failed_check_count": None,
            "artifact_preserved": False,
        }
        for spec in ARTIFACT_SPECS
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "runtime_hosting_created": False,
        "runtime_loop_created": False,
        "daemon_behavior_created": False,
        "continuation_created": False,
        "runtime_held_reentry_created": False,
        "second_operation_created": False,
        "prior_result_reentry_cycle_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "general_operation_permission_created": False,
        "general_lookup_permission_created": False,
        "arbitrary_lookup_permission_created": False,
        "registry_created": False,
        "search_surface_created": False,
        "query_surface_created": False,
        "ranking_surface_created": False,
        "older_runtime_lineage_imported_as_authority": False,
        "older_runtime_permission_treated_as_current": False,
        "runtime_authority_imported": False,
        "follow_on_work_authorized": False,
    }


def _block_dict(code: str | None, reason: str | None = None) -> dict[str, Any]:
    if code:
        return {
            "blocked": True,
            "code": code,
            "block_code": code,
            "reason": _sanitize(reason or code),
        }
    return {"blocked": False, "code": None, "block_code": None, "reason": None}


def _build_metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "local_relevance_medium_read_only_runtime_held_state_id": request.get(
            "local_relevance_medium_read_only_runtime_held_state_id",
            HELD_STATE_ID,
        ),
        "local_relevance_medium_read_only_runtime_held_state_type": HELD_STATE_TYPE,
        "local_relevance_medium_read_only_runtime_held_state_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "intent": request.get("local_relevance_medium_read_only_runtime_held_state_intent"),
    }


def _result_level_non_claims_canonical_false(non_claims: Mapping[str, Any]) -> bool:
    return all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def resolve_local_relevance_medium_read_only_runtime_held_state_v0_min(
    declared_local_relevance_medium_read_only_runtime_held_state: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve a single local read-only runtime-held-state object."""

    checks: list[dict[str, Any]] = []
    non_claims = _canonical_non_claims()

    if not _is_mapping(declared_local_relevance_medium_read_only_runtime_held_state):
        request: dict[str, Any] = {}
        _add_check(
            checks,
            "declared runtime-held-state request mapping",
            False,
            "mapping",
            type(declared_local_relevance_medium_read_only_runtime_held_state).__name__,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_REQUEST_MALFORMED",
        )
    else:
        request = copy.deepcopy(dict(declared_local_relevance_medium_read_only_runtime_held_state))
        _add_check(
            checks,
            "declared runtime-held-state request mapping",
            True,
            "mapping",
            "mapping",
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_REQUEST_MALFORMED",
        )
        _validate_request_shape(request, checks)
        _validate_shortcuts(request, checks)
        _validate_declared_non_claims(request, checks)

    bases = _basis_map_with_defaults()
    if request:
        for spec in ARTIFACT_SPECS:
            basis, _artifact = _read_basis_artifact(request, spec, checks)
            bases[str(spec["basis_name"])] = basis

    preliminary_block_code = _first_failed_code(checks)
    requested_intent = request.get("local_relevance_medium_read_only_runtime_held_state_intent")
    if requested_intent == INTENT_DO_NOT_RECORD and preliminary_block_code is None:
        outcome = OUTCOME_NOT_RECORDED
        recorded = False
        block_code = None
    else:
        recorded = preliminary_block_code is None
        outcome = OUTCOME_RECORDED if recorded else OUTCOME_BLOCKED
        block_code = None if recorded else preliminary_block_code

    held_state = _build_held_state_object(request, bases, recorded)
    if recorded:
        _add_generated_object_checks(checks, held_state, True)
        block_code = _first_failed_code(checks)
        if block_code:
            recorded = False
            outcome = OUTCOME_BLOCKED
            held_state = _build_held_state_object(request, bases, False)

    _add_check(
        checks,
        "artifact existence not runtime-held-state authority",
        request.get("artifact_existence_treated_as_runtime_held_state_authority") is not True,
        False,
        request.get("artifact_existence_treated_as_runtime_held_state_authority", False),
        "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HELD_STATE_AUTHORITY",
    )
    _add_check(
        checks,
        "latest file posture not runtime-held-state authority",
        request.get("latest_file_posture_treated_as_runtime_held_state_authority") is not True,
        False,
        request.get("latest_file_posture_treated_as_runtime_held_state_authority", False),
        "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HELD_STATE_AUTHORITY",
    )
    _add_check(
        checks,
        "repo-local availability not runtime-held-state authority",
        request.get("repo_local_availability_treated_as_runtime_held_state_authority") is not True,
        False,
        request.get("repo_local_availability_treated_as_runtime_held_state_authority", False),
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HELD_STATE_AUTHORITY",
    )
    _add_check(
        checks,
        "hidden repo state not runtime-held-state content or authority",
        request.get("hidden_repo_state_used_as_runtime_held_state_content") is not True
        and request.get("hidden_repo_state_used_as_runtime_held_state_authority") is not True,
        False,
        {
            "content": request.get("hidden_repo_state_used_as_runtime_held_state_content", False),
            "authority": request.get("hidden_repo_state_used_as_runtime_held_state_authority", False),
        },
        "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HELD_STATE_CONTENT",
    )
    _add_check(
        checks,
        "predecessor failure evidence preserved",
        not any(
            request.get(key) is True
            for key in (
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
            )
        ),
        True,
        "preserved",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _add_check(
        checks,
        "result-level required false non-claims canonical false",
        _result_level_non_claims_canonical_false(non_claims),
        True,
        _result_level_non_claims_canonical_false(non_claims),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    final_block_code = _first_failed_code(checks)
    if final_block_code and outcome == OUTCOME_RECORDED:
        outcome = OUTCOME_BLOCKED
        block_code = final_block_code
        recorded = False
        held_state = _build_held_state_object(request, bases, False)
    elif final_block_code and outcome != OUTCOME_NOT_RECORDED:
        outcome = OUTCOME_BLOCKED
        block_code = final_block_code

    statement = _build_statement(held_state, recorded and outcome == OUTCOME_RECORDED)
    result = {
        "local_relevance_medium_read_only_runtime_held_state_metadata": _build_metadata(request),
        "declared_local_relevance_medium_read_only_runtime_held_state_question": _sanitize(
            request.get("local_relevance_medium_read_only_runtime_held_state_question")
        ),
        "selected_runtime_held_state_boundary_artifact_basis": bases[
            "selected_runtime_held_state_boundary_artifact_basis"
        ],
        "selected_runtime_artifact_basis": bases["selected_runtime_artifact_basis"],
        "selected_runtime_boundary_artifact_basis": bases["selected_runtime_boundary_artifact_basis"],
        "selected_runtime_permission_artifact_basis": bases[
            "selected_runtime_permission_artifact_basis"
        ],
        "selected_operation_execution_artifact_basis": bases[
            "selected_operation_execution_artifact_basis"
        ],
        "local_relevance_medium_read_only_runtime_held_state": _sanitize(held_state),
        "local_relevance_medium_read_only_runtime_held_state_checks": checks,
        "local_relevance_medium_read_only_runtime_held_state_statement": statement,
        "local_relevance_medium_read_only_runtime_held_state_non_meaning": _build_non_meaning(),
        "additional_basis_required": _sanitize(request.get("additional_basis_context", [])),
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis", [])),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": _block_dict(block_code, request.get("block_reason")),
    }
    result["local_relevance_medium_read_only_runtime_held_state_summary"] = (
        build_local_relevance_medium_read_only_runtime_held_state_v0_min_summary(result)
    )
    return result


def resolve_local_relevance_medium_read_only_runtime_held_state_v0_min_from_path(
    declared_local_relevance_medium_read_only_runtime_held_state_path: Path | str,
) -> dict[str, Any]:
    """Read a declared runtime-held-state request from JSON and resolve it."""

    try:
        data = json.loads(Path(declared_local_relevance_medium_read_only_runtime_held_state_path).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - returned as bounded blocked result.
        request = build_declared_local_relevance_medium_read_only_runtime_held_state_v0_min_request()
        request["local_relevance_medium_read_only_runtime_held_state_question"] = ""
        request["block_reason"] = f"request unreadable: {exc.__class__.__name__}"
        result = resolve_local_relevance_medium_read_only_runtime_held_state_v0_min(request)
        result["outcome"] = OUTCOME_BLOCKED
        result["block"] = _block_dict(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_REQUEST_UNREADABLE",
            f"request unreadable: {exc.__class__.__name__}",
        )
        result["local_relevance_medium_read_only_runtime_held_state_summary"] = (
            build_local_relevance_medium_read_only_runtime_held_state_v0_min_summary(result)
        )
        return result
    if not _is_mapping(data):
        request = build_declared_local_relevance_medium_read_only_runtime_held_state_v0_min_request()
        request["local_relevance_medium_read_only_runtime_held_state_question"] = ""
        result = resolve_local_relevance_medium_read_only_runtime_held_state_v0_min(request)
        result["outcome"] = OUTCOME_BLOCKED
        result["block"] = _block_dict(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_REQUEST_MALFORMED",
            "request JSON is not an object",
        )
        result["local_relevance_medium_read_only_runtime_held_state_summary"] = (
            build_local_relevance_medium_read_only_runtime_held_state_v0_min_summary(result)
        )
        return result
    return resolve_local_relevance_medium_read_only_runtime_held_state_v0_min(data)


def build_local_relevance_medium_read_only_runtime_held_state_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact JSON-safe summary from a resolver result."""

    checks = result.get("local_relevance_medium_read_only_runtime_held_state_checks", [])
    if not isinstance(checks, list):
        checks = []
    failed_check_count = sum(1 for check in checks if _is_mapping(check) and check.get("passed") is not True)
    passed_check_count = sum(1 for check in checks if _is_mapping(check) and check.get("passed") is True)
    held_state = result.get("local_relevance_medium_read_only_runtime_held_state", {})
    if not _is_mapping(held_state):
        held_state = {}
    statement = result.get("local_relevance_medium_read_only_runtime_held_state_statement", {})
    if not _is_mapping(statement):
        statement = {}
    metadata = result.get("local_relevance_medium_read_only_runtime_held_state_metadata", {})
    if not _is_mapping(metadata):
        metadata = {}
    block = result.get("block", {})
    if not _is_mapping(block):
        block = {}
    non_claims = result.get("non_claims", {})
    if not _is_mapping(non_claims):
        non_claims = {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "held_state_id": held_state.get("held_state_id")
        or metadata.get("local_relevance_medium_read_only_runtime_held_state_id"),
        "question": result.get("declared_local_relevance_medium_read_only_runtime_held_state_question"),
        "intent": None,
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "held_state_recorded": held_state.get(
            "local_relevance_medium_read_only_runtime_held_state_recorded"
        )
        is True,
        "basis_runtime_held_state_boundary_artifact_preserved": statement.get(
            "basis_runtime_held_state_boundary_artifact_preserved"
        )
        is True,
        "basis_runtime_artifact_preserved": statement.get("basis_runtime_artifact_preserved")
        is True,
        "basis_runtime_boundary_artifact_preserved": statement.get(
            "basis_runtime_boundary_artifact_preserved"
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
        "selected_command": held_state.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved") is True,
        "selected_command_is_state": held_state.get("selected_command_is_state") is True,
        "selected_runtime_held_state_boundary_recorded": held_state.get(
            "selected_runtime_held_state_boundary_recorded"
        )
        is True,
        "future_runtime_held_state_may_be_considered": held_state.get(
            "future_runtime_held_state_may_be_considered"
        )
        is True,
        "selected_runtime_recorded": held_state.get("selected_runtime_recorded") is True,
        "runtime_created": held_state.get("runtime_created") is True,
        "runtime_local_only": held_state.get("runtime_local_only") is True,
        "runtime_read_only": held_state.get("runtime_read_only") is True,
        "selected_runtime_boundary_recorded": held_state.get("selected_runtime_boundary_recorded")
        is True,
        "future_runtime_may_be_considered": held_state.get("future_runtime_may_be_considered")
        is True,
        "selected_runtime_permission_recorded": held_state.get(
            "selected_runtime_permission_recorded"
        )
        is True,
        "runtime_permission_created": held_state.get("runtime_permission_created") is True,
        "runtime_permission_local_only": held_state.get("runtime_permission_local_only") is True,
        "runtime_permission_read_only": held_state.get("runtime_permission_read_only") is True,
        "selected_operation_execution_recorded": held_state.get(
            "selected_operation_execution_recorded"
        )
        is True,
        "operation_execution_created": held_state.get("operation_execution_created") is True,
        "operation_execution_performed": held_state.get("operation_execution_performed") is True,
        "operation_execution_local_only": held_state.get("operation_execution_local_only") is True,
        "operation_execution_read_only": held_state.get("operation_execution_read_only") is True,
        "runtime_held_state_created": held_state.get("runtime_held_state_created") is True,
        "runtime_held_state_local_only": held_state.get("runtime_held_state_local_only") is True,
        "runtime_held_state_read_only": held_state.get("runtime_held_state_read_only") is True,
        "held_state_basis_reference_only": held_state.get("held_state_basis_reference_only") is True,
        "raw_state_body_embedded_false_posture": held_state.get("raw_state_body_embedded") is False,
        "state_mutation_performed_false_posture": held_state.get("state_mutation_performed") is False,
        "state_update_performed_false_posture": held_state.get("state_update_performed") is False,
        "held_state_object_summary": {
            "held_state_type": held_state.get("held_state_type"),
            "held_state_scope": held_state.get("held_state_scope"),
            "held_state_version": held_state.get("held_state_version"),
            "basis_reference_only": held_state.get("held_state_basis_reference_only") is True,
        },
        "runtime_hosting_not_created": held_state.get("runtime_hosting_created") is False,
        "runtime_loop_not_created": held_state.get("runtime_loop_created") is False,
        "daemon_behavior_not_created": held_state.get("daemon_behavior_created") is False,
        "continuation_not_created": held_state.get("continuation_created") is False,
        "runtime_held_reentry_not_created": held_state.get("runtime_held_reentry_created") is False,
        "second_operation_not_created": held_state.get("second_operation_created") is False,
        "prior_result_reentry_cycle_not_created": held_state.get("prior_result_reentry_cycle_created")
        is False,
        "public_api_not_created": held_state.get("public_api_created") is False,
        "participant_facing_interface_not_created": held_state.get(
            "participant_facing_interface_created"
        )
        is False,
        "distributed_network_behavior_not_created": held_state.get(
            "distributed_network_behavior_created"
        )
        is False,
        "general_operation_permission_not_created": held_state.get(
            "general_operation_permission_created"
        )
        is False,
        "general_lookup_permission_not_created": held_state.get("general_lookup_permission_created")
        is False,
        "arbitrary_lookup_permission_not_created": held_state.get(
            "arbitrary_lookup_permission_created"
        )
        is False,
        "unsupported_commands_not_permitted": held_state.get("unsupported_commands_permitted")
        is False,
        "unsupported_lookup_keys_not_permitted": held_state.get("unsupported_lookup_keys_permitted")
        is False,
        "no_new_lookup_entry_created_beyond_bounded_lookup_result_object": held_state.get(
            "new_lookup_entry_created"
        )
        is False,
        "no_new_signal_entry_relevance_object_index_entry_created": (
            held_state.get("new_signal_accepted") is False
            and held_state.get("new_entry_accepted") is False
            and held_state.get("new_relevance_object_created") is False
            and held_state.get("new_index_entry_created") is False
        ),
        "filesystem_discovery_not_performed": held_state.get("filesystem_discovery_performed")
        is False,
        "registry_search_query_surface_ranking_not_created": (
            held_state.get("registry_created") is False
            and held_state.get("search_surface_created") is False
            and held_state.get("query_surface_created") is False
            and held_state.get("ranking_surface_created") is False
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": (
            held_state.get("scoring_surface_created") is False
            and held_state.get("priority_surface_created") is False
            and held_state.get("validity_judgment_created") is False
            and held_state.get("truth_judgment_created") is False
            and held_state.get("authority_judgment_created") is False
            and held_state.get("currentness_judgment_created") is False
        ),
        "older_runtime_lineage_not_imported_as_authority": held_state.get(
            "older_runtime_lineage_imported_as_authority"
        )
        is False,
        "older_runtime_permission_not_treated_as_current": held_state.get(
            "older_runtime_permission_treated_as_current"
        )
        is False,
        "runtime_authority_not_imported": held_state.get("runtime_authority_imported") is False,
        "runtime_v0_failure_evidence_preserved": held_state.get(
            "runtime_v0_failure_evidence_preserved"
        )
        is True,
        "runtime_v2_failure_evidence_preserved": held_state.get(
            "runtime_v2_failure_evidence_preserved"
        )
        is True,
        "runtime_boundary_v0_failure_evidence_preserved": held_state.get(
            "runtime_boundary_v0_failure_evidence_preserved"
        )
        is True,
        "runtime_v0_v2_boundary_v0_failure_not_repaired_hidden_claimed_passed": (
            non_claims.get("runtime_v0_failure_repaired") is False
            and non_claims.get("runtime_v0_failure_hidden") is False
            and non_claims.get("runtime_v0_failure_claimed_passed") is False
            and non_claims.get("runtime_v2_failure_repaired") is False
            and non_claims.get("runtime_v2_failure_hidden") is False
            and non_claims.get("runtime_v2_failure_claimed_passed") is False
            and non_claims.get("runtime_boundary_v0_failure_repaired") is False
            and non_claims.get("runtime_boundary_v0_failure_hidden") is False
            and non_claims.get("runtime_boundary_v0_failure_claimed_passed") is False
        ),
        "repeated_reception_permission_arbitrary_reception_feed_not_created": (
            held_state.get("repeated_reception_permission_created") is False
            and held_state.get("arbitrary_reception_created") is False
            and held_state.get("feed_created") is False
        ),
        "source_authority_currentness_truth_synchronization_participation_participant_role_not_created": (
            held_state.get("source_transfer_occurred") is False
            and held_state.get("source_receipt_occurred") is False
            and held_state.get("authority_created") is False
            and held_state.get("currentness_created") is False
            and held_state.get("truth_created") is False
            and held_state.get("synchronization_created") is False
            and held_state.get("participation_authorized") is False
            and held_state.get("participant_role_created") is False
        ),
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed")
        is True,
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked")
        is True,
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved"
        )
        is True,
        "follow_on_not_created": held_state.get("follow_on_work_authorized") is False,
        "key_non_claims": {
            "raw_state_body_embedded": non_claims.get("raw_state_body_embedded"),
            "state_mutation_performed": non_claims.get("state_mutation_performed"),
            "state_update_performed": non_claims.get("state_update_performed"),
            "continuation_created": non_claims.get("continuation_created"),
            "runtime_held_reentry_created": non_claims.get("runtime_held_reentry_created"),
            "second_operation_created": non_claims.get("second_operation_created"),
            "follow_on_work_authorized": non_claims.get("follow_on_work_authorized"),
        },
        "result_level_non_claims_canonical_false": _result_level_non_claims_canonical_false(
            non_claims
        ),
    }

    metadata = result.get("local_relevance_medium_read_only_runtime_held_state_metadata", {})
    if _is_mapping(metadata):
        summary["intent"] = metadata.get("intent")
    return _sanitize(summary)


def write_local_relevance_medium_read_only_runtime_held_state_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result under the runtime-held-state output root."""

    if not _is_mapping(result):
        raise LocalRelevanceMediumReadOnlyRuntimeHeldStateV0MinError("result must be a mapping")

    held_state = result.get("local_relevance_medium_read_only_runtime_held_state", {})
    if not _is_mapping(held_state):
        held_state_id = HELD_STATE_ID
    else:
        held_state_id = str(held_state.get("held_state_id") or HELD_STATE_ID)

    if output_path is None:
        candidate = OUTPUT_ROOT / f"{held_state_id}__local_relevance_medium_read_only_runtime_held_state_v0_min_result.json"
    else:
        candidate = Path(output_path)

    output_root_resolved = OUTPUT_ROOT.resolve()
    parent_resolved = candidate.parent.resolve()
    try:
        parent_resolved.relative_to(output_root_resolved)
    except ValueError as exc:
        raise LocalRelevanceMediumReadOnlyRuntimeHeldStateV0MinError(
            "output path must remain under the runtime-held-state output root"
        ) from exc

    candidate.parent.mkdir(parents=True, exist_ok=True)
    final_path = candidate
    if final_path.exists():
        stem = candidate.stem
        suffix = candidate.suffix
        for index in range(1, 10000):
            numbered = candidate.with_name(f"{stem}_{index:03d}{suffix}")
            if not numbered.exists():
                final_path = numbered
                break
        else:
            raise LocalRelevanceMediumReadOnlyRuntimeHeldStateV0MinError(
                "could not allocate non-overwriting output filename"
            )

    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path


def build_declared_local_relevance_medium_read_only_runtime_held_state_v0_min_request(
    *,
    local_relevance_medium_read_only_runtime_held_state_id: str = HELD_STATE_ID,
    selected_runtime_held_state_boundary_artifact: Path | str = DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT,
    selected_runtime_artifact: Path | str = DEFAULT_RUNTIME_ARTIFACT,
    selected_runtime_boundary_artifact: Path | str = DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
    selected_runtime_permission_artifact: Path | str = DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
    selected_operation_execution_artifact: Path | str = DEFAULT_OPERATION_EXECUTION_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    held_state_type: str = HELD_STATE_TYPE,
    held_state_scope: str = HELD_STATE_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    """Build a declared request that records cleanly when default artifacts exist."""

    non_claims = _canonical_non_claims()
    if declared_non_claims is not None:
        for key, value in declared_non_claims.items():
            non_claims[str(key)] = bool(value)

    question = (
        "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY "
        "for selected command state, one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME, "
        "one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY, one clean "
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION, one clean "
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION, existing reusable "
        "read-only lookup permission, prior lookup-pair coverage, and prior local "
        "carrier command surface, may one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE "
        "be recorded for selected command state without creating hosting, loop, daemon "
        "behavior, continuation, runtime-held re-entry, second operation, prior-result "
        "re-entry cycle, public API, participant-facing interface, distributed network "
        "behavior, general operation permission, general lookup permission, arbitrary "
        "lookup permission, unsupported commands, unsupported lookup keys, new lookup "
        "entry, new entries, new signals, filesystem discovery, older runtime authority "
        "import, query surface, registry, search, ranking, authority, currentness, truth, "
        "source transfer, source receipt, or follow-on work?"
    )

    return {
        "local_relevance_medium_read_only_runtime_held_state_id": (
            local_relevance_medium_read_only_runtime_held_state_id
        ),
        "local_relevance_medium_read_only_runtime_held_state_question": question,
        "local_relevance_medium_read_only_runtime_held_state_intent": intent,
        "selected_runtime_held_state_boundary_artifact": str(
            selected_runtime_held_state_boundary_artifact
        ),
        "selected_runtime_artifact": str(selected_runtime_artifact),
        "selected_runtime_boundary_artifact": str(selected_runtime_boundary_artifact),
        "selected_runtime_permission_artifact": str(selected_runtime_permission_artifact),
        "selected_operation_execution_artifact": str(selected_operation_execution_artifact),
        "selected_command": selected_command,
        "held_state_type": held_state_type,
        "held_state_scope": held_state_scope,
        "declared_non_claims": non_claims,
    }
