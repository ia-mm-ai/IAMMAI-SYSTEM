"""Resolve one local read-only runtime-held re-entry.

This resolver records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY object only. It reads one
clean runtime-held-re-entry boundary artifact, one clean runtime-held-state
artifact, one clean runtime-held-state boundary artifact, one clean runtime v3
artifact, one clean runtime boundary v2 artifact, one clean runtime permission
artifact, and one clean operation execution artifact as basis references.

The held re-entry is local, read-only, selected-state-only,
basis-reference-only, raw-state-body-excluding, state-mutation-refusing,
state-update-refusing, non-prior-result-cycle-shaped, non-second-operation-
shaped, non-continuation-shaped, non-hosting-shaped, non-loop-shaped,
non-daemon-shaped, and older-runtime-authority-import-blocking.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyRuntimeHeldReentryV0MinError(RuntimeError):
    """Bounded resolver error for runtime-held-re-entry handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_held_reentry_v0_min"
)

DEFAULT_HELD_REENTRY_ID = "local_relevance_medium_read_only_runtime_held_reentry_001"
HELD_REENTRY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY"
HELD_REENTRY_SCOPE = "SELECTED_RUNTIME_HELD_REENTRY_ONLY"
SUPPORTED_HELD_REENTRY_TYPE_VALUES = (HELD_REENTRY_TYPE,)
SUPPORTED_HELD_REENTRY_SCOPE_VALUES = (HELD_REENTRY_SCOPE,)
SELECTED_COMMAND = "state"

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_held_reentry_boundary_v0_min/"
    "local_relevance_medium_read_only_runtime_held_reentry_boundary_reference_review_001__"
    "local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min_result.json"
)
DEFAULT_RUNTIME_HELD_STATE_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_held_state_v0_min/"
    "local_relevance_medium_read_only_runtime_held_state_reference_review_001__"
    "local_relevance_medium_read_only_runtime_held_state_v0_min_result.json"
)
DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_held_state_boundary_v0_min/"
    "local_relevance_medium_read_only_runtime_held_state_boundary_reference_review_001__"
    "local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result.json"
)
DEFAULT_RUNTIME_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_v0_min_v3/"
    "local_relevance_medium_read_only_runtime_reference_review_001__"
    "local_relevance_medium_read_only_runtime_v0_min_v3_result.json"
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

EXPECTED_RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY_RECORDED"
)
EXPECTED_RUNTIME_HELD_STATE_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_RECORDED"
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
    "prior_result_reentry_cycle_created",
    "second_operation_created",
    "continuation_created",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
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
    "artifact_existence_treated_as_runtime_held_reentry_authority",
    "latest_file_posture_treated_as_runtime_held_reentry_authority",
    "repo_local_availability_treated_as_runtime_held_reentry_authority",
    "hidden_repo_state_used_as_runtime_held_reentry_content",
    "hidden_repo_state_used_as_runtime_held_reentry_authority",
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
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_runtime_held_reentry_recorded",
    "basis_runtime_held_reentry_boundary_artifact_preserved",
    "basis_runtime_held_state_artifact_preserved",
    "basis_runtime_held_state_boundary_artifact_preserved",
    "basis_runtime_artifact_preserved",
    "basis_runtime_boundary_artifact_preserved",
    "basis_runtime_permission_artifact_preserved",
    "basis_operation_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_runtime_held_reentry_boundary_recorded",
    "future_runtime_held_reentry_may_be_considered",
    "selected_runtime_held_state_recorded",
    "runtime_held_state_created",
    "runtime_held_state_local_only",
    "runtime_held_state_read_only",
    "held_state_basis_reference_only",
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
    "runtime_held_reentry_created",
    "runtime_held_reentry_local_only",
    "runtime_held_reentry_read_only",
    "held_reentry_basis_reference_only",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

SPECIAL_FALSE_FIELD_BLOCK_CODES = {
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
}

EXACT_TOP_LEVEL_BLOCKS = {
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
}


def _auto_block_code(field_name: str) -> str:
    return SPECIAL_FALSE_FIELD_BLOCK_CODES.get(field_name, field_name.upper())


TOP_LEVEL_BLOCK_FIELD_CODES = {
    key: EXACT_TOP_LEVEL_BLOCKS.get(key, _auto_block_code(key))
    for key in REQUIRED_FALSE_NON_CLAIMS
}

SHORTCUT_BLOCK_FIELD_CODES = {
    "runtime_held_reentry_boundary_artifact_missing": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_PATH_MISSING",
    "runtime_held_reentry_boundary_artifact_not_recorded": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "runtime_held_reentry_boundary_artifact_failed_checks_present": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_held_reentry_boundary_artifact_version_not_0_1_0": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_held_state_artifact_missing": "RUNTIME_HELD_STATE_ARTIFACT_PATH_MISSING",
    "runtime_held_state_artifact_not_recorded": "RUNTIME_HELD_STATE_ARTIFACT_NOT_RECORDED",
    "runtime_held_state_artifact_failed_checks_present": "RUNTIME_HELD_STATE_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_held_state_artifact_version_not_0_1_0": "RUNTIME_HELD_STATE_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_held_state_boundary_artifact_missing": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_PATH_MISSING",
    "runtime_held_state_boundary_artifact_not_recorded": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "runtime_held_state_boundary_artifact_failed_checks_present": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_held_state_boundary_artifact_version_not_0_1_0": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_artifact_missing": "RUNTIME_ARTIFACT_PATH_MISSING",
    "runtime_artifact_not_recorded": "RUNTIME_ARTIFACT_NOT_RECORDED",
    "runtime_artifact_failed_checks_present": "RUNTIME_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_artifact_version_not_0_1_0": "RUNTIME_ARTIFACT_VERSION_NOT_0_1_0",
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
    "selected_runtime_held_reentry_boundary_not_recorded": "SELECTED_RUNTIME_HELD_REENTRY_BOUNDARY_NOT_RECORDED",
    "future_runtime_held_reentry_may_not_be_considered": "FUTURE_RUNTIME_HELD_REENTRY_MAY_NOT_BE_CONSIDERED",
    "selected_runtime_held_state_not_recorded": "SELECTED_RUNTIME_HELD_STATE_NOT_RECORDED",
    "runtime_held_state_not_created": "RUNTIME_HELD_STATE_NOT_CREATED",
    "runtime_held_state_local_only_not_true": "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE",
    "runtime_held_state_read_only_not_true": "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE",
    "held_state_basis_reference_only_not_true": "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "raw_state_body_embedded": "RAW_STATE_BODY_EMBEDDED",
    "state_mutation_performed": "STATE_MUTATION_PERFORMED",
    "state_update_performed": "STATE_UPDATE_PERFORMED",
    "selected_runtime_held_state_boundary_not_recorded": "SELECTED_RUNTIME_HELD_STATE_BOUNDARY_NOT_RECORDED",
    "future_runtime_held_state_may_not_be_considered": "FUTURE_RUNTIME_HELD_STATE_MAY_NOT_BE_CONSIDERED",
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
    "held_reentry_type_not_local_relevance_medium_read_only_runtime_held_reentry": "HELD_REENTRY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY",
    "held_reentry_scope_not_selected_runtime_held_reentry_only": "HELD_REENTRY_SCOPE_NOT_SELECTED_RUNTIME_HELD_REENTRY_ONLY",
    "local_relevance_medium_read_only_runtime_held_reentry_not_recorded": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_NOT_RECORDED",
    "runtime_held_reentry_not_created": "RUNTIME_HELD_REENTRY_NOT_CREATED",
    "runtime_held_reentry_local_only_not_true": "RUNTIME_HELD_REENTRY_LOCAL_ONLY_NOT_TRUE",
    "runtime_held_reentry_read_only_not_true": "RUNTIME_HELD_REENTRY_READ_ONLY_NOT_TRUE",
    "held_reentry_basis_reference_only_not_true": "HELD_REENTRY_BASIS_REFERENCE_ONLY_NOT_TRUE",
}

BASE_BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BLOCK_REQUESTED",
    "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_PATH_MISSING",
    "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_UNREADABLE",
    "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "RUNTIME_HELD_STATE_ARTIFACT_PATH_MISSING",
    "RUNTIME_HELD_STATE_ARTIFACT_UNREADABLE",
    "RUNTIME_HELD_STATE_ARTIFACT_NOT_JSON_OBJECT",
    "RUNTIME_HELD_STATE_ARTIFACT_NOT_RECORDED",
    "RUNTIME_HELD_STATE_ARTIFACT_FAILED_CHECKS_PRESENT",
    "RUNTIME_HELD_STATE_ARTIFACT_VERSION_NOT_0_1_0",
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
    "SELECTED_RUNTIME_HELD_REENTRY_BOUNDARY_NOT_RECORDED",
    "FUTURE_RUNTIME_HELD_REENTRY_MAY_NOT_BE_CONSIDERED",
    "SELECTED_RUNTIME_HELD_STATE_NOT_RECORDED",
    "RUNTIME_HELD_STATE_NOT_CREATED",
    "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE",
    "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE",
    "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "RAW_STATE_BODY_EMBEDDED",
    "STATE_MUTATION_PERFORMED",
    "STATE_UPDATE_PERFORMED",
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
    "HELD_REENTRY_TYPE_MISSING",
    "HELD_REENTRY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY",
    "HELD_REENTRY_SCOPE_MISSING",
    "HELD_REENTRY_SCOPE_NOT_SELECTED_RUNTIME_HELD_REENTRY_ONLY",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_NOT_RECORDED",
    "RUNTIME_HELD_REENTRY_NOT_CREATED",
    "RUNTIME_HELD_REENTRY_LOCAL_ONLY_NOT_TRUE",
    "RUNTIME_HELD_REENTRY_READ_ONLY_NOT_TRUE",
    "HELD_REENTRY_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "PRIOR_RESULT_REENTRY_CYCLE_CREATED",
    "SECOND_OPERATION_CREATED",
    "CONTINUATION_CREATED",
    "RUNTIME_HOSTING_CREATED",
    "RUNTIME_LOOP_CREATED",
    "DAEMON_BEHAVIOR_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HELD_REENTRY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HELD_REENTRY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HELD_REENTRY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HELD_REENTRY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HELD_REENTRY_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_REQUEST_UNREADABLE",
)

BLOCK_CODES = tuple(
    dict.fromkeys(
        BASE_BLOCK_CODES
        + tuple(SHORTCUT_BLOCK_FIELD_CODES.values())
        + tuple(TOP_LEVEL_BLOCK_FIELD_CODES.values())
    )
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_runtime_held_reentry_body",
    "raw_runtime_held_reentry_boundary_body",
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
    "raw_second_operation_body",
    "raw_prior_result_reentry_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "runtime_held_reentry_body",
    "runtime_held_reentry_boundary_body",
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
    "RAW_RUNTIME_HELD_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BOUNDARY_BODY_MUST_NOT_RETURN",
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

ARTIFACT_SPECS = (
    {
        "path_key": "selected_runtime_held_reentry_boundary_artifact",
        "basis_key": "selected_runtime_held_reentry_boundary_artifact_basis",
        "label": "runtime-held-re-entry boundary artifact",
        "prefix": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME,
        "default_path": DEFAULT_RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT,
    },
    {
        "path_key": "selected_runtime_held_state_artifact",
        "basis_key": "selected_runtime_held_state_artifact_basis",
        "label": "runtime-held-state artifact",
        "prefix": "RUNTIME_HELD_STATE_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_HELD_STATE_OUTCOME,
        "default_path": DEFAULT_RUNTIME_HELD_STATE_ARTIFACT,
    },
    {
        "path_key": "selected_runtime_held_state_boundary_artifact",
        "basis_key": "selected_runtime_held_state_boundary_artifact_basis",
        "label": "runtime-held-state boundary artifact",
        "prefix": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_HELD_STATE_BOUNDARY_OUTCOME,
        "default_path": DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT,
    },
    {
        "path_key": "selected_runtime_artifact",
        "basis_key": "selected_runtime_artifact_basis",
        "label": "runtime artifact",
        "prefix": "RUNTIME_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_OUTCOME,
        "default_path": DEFAULT_RUNTIME_ARTIFACT,
    },
    {
        "path_key": "selected_runtime_boundary_artifact",
        "basis_key": "selected_runtime_boundary_artifact_basis",
        "label": "runtime boundary artifact",
        "prefix": "RUNTIME_BOUNDARY_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        "default_path": DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
    },
    {
        "path_key": "selected_runtime_permission_artifact",
        "basis_key": "selected_runtime_permission_artifact_basis",
        "label": "runtime permission artifact",
        "prefix": "RUNTIME_PERMISSION_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_PERMISSION_OUTCOME,
        "default_path": DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
    },
    {
        "path_key": "selected_operation_execution_artifact",
        "basis_key": "selected_operation_execution_artifact_basis",
        "label": "operation execution artifact",
        "prefix": "OPERATION_EXECUTION_ARTIFACT",
        "expected_outcome": EXPECTED_OPERATION_EXECUTION_OUTCOME,
        "default_path": DEFAULT_OPERATION_EXECUTION_ARTIFACT,
    },
)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY "
    "for selected command state, one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE, "
    "one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME, one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY, "
    "one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION, existing reusable read-only lookup "
    "permission, prior lookup-pair coverage, and prior local carrier command surface, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY be recorded for selected command state, "
    "without creating prior-result re-entry cycle, creating second operation, creating continuation, "
    "creating runtime hosting, creating runtime loop, creating daemon behavior, creating public API, "
    "creating participant-facing interface, creating distributed network behavior, creating general "
    "operation permission, creating general lookup permission, creating arbitrary lookup permission, "
    "permitting unsupported commands, permitting unsupported lookup keys, creating new lookup entry "
    "beyond the already bounded selected-state lookup result object, embedding raw state body, "
    "mutating state, updating state, accepting new entries, accepting new signals, performing "
    "filesystem discovery, importing older runtime/post-runtime authority, creating query surface, "
    "registry, search, ranking, scoring, priority, validity judgment, truth judgment, authority, "
    "currentness, synchronization, participation authorization, participant role, repeated reception "
    "permission, arbitrary reception, feed, source transfer, source receipt, or follow-on work?"
)

WHAT_REMAINS_OPEN = (
    "local relevance medium read-only runtime-held re-entry test",
    "local relevance medium read-only runtime-held re-entry live artifact",
    "local relevance medium read-only runtime-held re-entry terminal summary",
    "prior-result re-entry cycle",
    "second operation",
    "continuation",
    "runtime hosting",
    "runtime loop",
    "daemon behavior",
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


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _is_sensitive_key(key: Any) -> bool:
    key_text = str(key)
    return key_text in SENSITIVE_CONTENT_KEYS or key_text.endswith("_body")


def _sanitize(value: Any, key: Any | None = None) -> Any:
    if key is not None and _is_sensitive_key(key):
        return "[REDACTED]"
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        sanitized = value
        for sentinel in HOSTILE_SENTINELS:
            sanitized = sanitized.replace(sentinel, "[REDACTED]")
        return sanitized
    if isinstance(value, MappingABC):
        return {str(k): _sanitize(v, k) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, key) for item in value]
    return value


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


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
        public_code = (
            code
            if code in BLOCK_CODES
            else "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_REQUEST_MALFORMED"
        )
        check["block_code"] = public_code
        check["failure_code"] = public_code
    return check


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code:
                return code
    return None


def _block_dict(code: str | None, reason: Any = None) -> dict[str, Any]:
    if code:
        return {
            "blocked": True,
            "code": code,
            "block_code": code,
            "reason": _sanitize(reason or code),
        }
    return {"blocked": False, "code": None, "block_code": None, "reason": None}


def _find_first_key(value: Any, key_names: tuple[str, ...]) -> Any:
    if isinstance(value, MappingABC):
        for key in key_names:
            if key in value:
                return value[key]
        for nested_key, nested_value in value.items():
            if _is_sensitive_key(nested_key):
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
    if isinstance(value, MappingABC):
        collected: list[dict[str, Any]] = []
        for key, nested_value in value.items():
            if _is_sensitive_key(key):
                continue
            if str(key).endswith("_checks") or key == "checks":
                if isinstance(nested_value, list):
                    collected.extend(
                        [dict(item) for item in nested_value if isinstance(item, MappingABC)]
                    )
            else:
                collected.extend(_find_checks(nested_value))
        return collected
    if isinstance(value, list):
        collected = []
        for item in value:
            collected.extend(_find_checks(item))
        return collected
    return []


def _artifact_failed_check_count(artifact: Mapping[str, Any] | None) -> Any:
    if artifact is None:
        return None
    direct = _find_first_key(artifact, ("failed_check_count",))
    if isinstance(direct, int) and not isinstance(direct, bool):
        return direct
    checks = _find_checks(artifact)
    if checks:
        return sum(1 for check in checks if check.get("passed") is not True)
    return direct


def _artifact_result_version(artifact: Mapping[str, Any] | None) -> Any:
    if artifact is None:
        return None
    return _find_first_key(artifact, ("result_version",))


def _artifact_outcome(artifact: Mapping[str, Any] | None) -> Any:
    if artifact is None:
        return None
    return _find_first_key(artifact, ("outcome",))


def _read_json_object(path_value: Any) -> tuple[dict[str, Any] | None, str | None, Any]:
    if path_value in (None, ""):
        return None, "PATH_MISSING", path_value
    try:
        loaded = json.loads(Path(path_value).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - converted to bounded public result.
        return None, "UNREADABLE", f"{exc.__class__.__name__}: {exc}"
    if not isinstance(loaded, MappingABC):
        return None, "NOT_JSON_OBJECT", type(loaded).__name__
    return copy.deepcopy(dict(loaded)), None, "readable JSON object"


def _basis_artifact_summary(
    path_value: Any,
    artifact: Mapping[str, Any] | None,
    expected_outcome: str,
) -> dict[str, Any]:
    outcome = _artifact_outcome(artifact)
    result_version = _artifact_result_version(artifact)
    failed_check_count = _artifact_failed_check_count(artifact)
    preserved = (
        artifact is not None
        and outcome == expected_outcome
        and result_version == RESULT_VERSION
        and failed_check_count == 0
    )
    return {
        "artifact": str(path_value) if path_value not in (None, "") else None,
        "artifact_path": str(path_value) if path_value not in (None, "") else None,
        "artifact_readable_json": artifact is not None,
        "artifact_json_object": artifact is not None,
        "artifact_body_embedded": False,
        "outcome": _sanitize(outcome),
        "expected_outcome": expected_outcome,
        "result_version": _sanitize(result_version),
        "failed_check_count": failed_check_count,
        "result_version_expected": RESULT_VERSION,
        "failed_check_count_expected": 0,
        "artifact_preserved": preserved,
    }


def _empty_basis(expected_outcome: str = "") -> dict[str, Any]:
    return _basis_artifact_summary(None, None, expected_outcome)


def _basis_map_with_defaults() -> dict[str, dict[str, Any]]:
    return {
        str(spec["basis_key"]): _empty_basis(str(spec["expected_outcome"]))
        for spec in ARTIFACT_SPECS
    }


def _request_artifact(request: Mapping[str, Any], key: str, default: Path) -> str:
    value = request.get(key)
    if value in (None, ""):
        return str(default)
    return str(value)


def _validate_basis_artifact(
    request: Mapping[str, Any],
    spec: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    path_key = str(spec["path_key"])
    label = str(spec["label"])
    prefix = str(spec["prefix"])
    expected_outcome = str(spec["expected_outcome"])
    path_value = request.get(path_key)

    missing = path_value in (None, "")
    checks.append(
        _new_check(
            f"{label} path declared",
            not missing,
            "declared artifact path",
            path_value,
            f"{prefix}_PATH_MISSING",
        )
    )
    if missing:
        return _empty_basis(expected_outcome), None

    artifact, read_status, actual = _read_json_object(path_value)
    if read_status == "UNREADABLE":
        checks.append(
            _new_check(
                f"{label} readable JSON",
                False,
                "readable JSON object",
                actual,
                f"{prefix}_UNREADABLE",
            )
        )
        return _basis_artifact_summary(path_value, None, expected_outcome), None
    checks.append(
        _new_check(
            f"{label} readable JSON",
            True,
            "readable JSON",
            "readable JSON",
            f"{prefix}_UNREADABLE",
        )
    )
    if read_status == "NOT_JSON_OBJECT":
        checks.append(
            _new_check(
                f"{label} JSON object",
                False,
                "JSON object",
                actual,
                f"{prefix}_NOT_JSON_OBJECT",
            )
        )
        return _basis_artifact_summary(path_value, None, expected_outcome), None
    checks.append(
        _new_check(
            f"{label} JSON object",
            True,
            "JSON object",
            "JSON object",
            f"{prefix}_NOT_JSON_OBJECT",
        )
    )

    outcome = _artifact_outcome(artifact)
    result_version = _artifact_result_version(artifact)
    failed_check_count = _artifact_failed_check_count(artifact)
    checks.append(
        _new_check(
            f"{label} outcome recorded",
            outcome == expected_outcome,
            expected_outcome,
            outcome,
            f"{prefix}_NOT_RECORDED",
        )
    )
    checks.append(
        _new_check(
            f"{label} result version 0.1.0",
            result_version == RESULT_VERSION,
            RESULT_VERSION,
            result_version,
            f"{prefix}_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _new_check(
            f"{label} failed check count zero",
            failed_check_count == 0,
            0,
            failed_check_count,
            f"{prefix}_FAILED_CHECKS_PRESENT",
        )
    )
    return _basis_artifact_summary(path_value, artifact, expected_outcome), artifact


def _boolean_posture(
    artifact: Mapping[str, Any] | None,
    field_names: tuple[str, ...],
) -> tuple[bool, dict[str, Any]]:
    values: list[dict[str, Any]] = []
    if artifact is not None:
        for field_name in field_names:
            value = _find_first_key(artifact, (field_name,))
            if value is not None:
                values.append({"field": field_name, "value": value})
    if not values:
        return False, {"reason": "missing_relevant_posture", "values": values}
    for item in values:
        if item["value"] is not True:
            return False, {"reason": "not_true", "values": values}
    return True, {"reason": "true", "values": values}


def _false_posture(
    artifact: Mapping[str, Any] | None,
    field_names: tuple[str, ...],
) -> tuple[bool, dict[str, Any]]:
    values: list[dict[str, Any]] = []
    if artifact is not None:
        for field_name in field_names:
            value = _find_first_key(artifact, (field_name,))
            if value is not None:
                values.append({"field": field_name, "value": value})
    if not values:
        return False, {"reason": "missing_relevant_posture", "values": values}
    for item in values:
        if item["value"] is not False:
            return False, {"reason": "not_false", "values": values}
    return True, {"reason": "false", "values": values}


def _selected_command_posture(artifact: Mapping[str, Any] | None) -> tuple[bool, dict[str, Any]]:
    value = _find_first_key(artifact, ("selected_command",)) if artifact is not None else None
    return value == SELECTED_COMMAND, {"selected_command": value}


def _add_bool_posture_check(
    checks: list[dict[str, Any]],
    check_name: str,
    artifact: Mapping[str, Any] | None,
    field_names: tuple[str, ...],
    code: str,
) -> bool:
    passed, detail = _boolean_posture(artifact, field_names)
    checks.append(_new_check(check_name, passed, True, detail, code))
    return passed


def _add_false_posture_check(
    checks: list[dict[str, Any]],
    check_name: str,
    artifact: Mapping[str, Any] | None,
    field_names: tuple[str, ...],
    code: str,
) -> bool:
    passed, detail = _false_posture(artifact, field_names)
    checks.append(_new_check(check_name, passed, False, detail, code))
    return passed


def _validate_declared_non_claims(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
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
            {"bad_keys": bad_keys[:30], "bad_key_count": len(bad_keys)},
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )


def _validate_top_level_block_fields(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    merged = {**SHORTCUT_BLOCK_FIELD_CODES, **TOP_LEVEL_BLOCK_FIELD_CODES}
    for field, code in merged.items():
        checks.append(
            _new_check(
                f"{field} not asserted",
                request.get(field) is not True,
                False,
                request.get(field, False),
                code,
            )
        )


def _empty_upstream() -> dict[str, bool]:
    return {
        "selected_runtime_held_reentry_boundary_recorded": False,
        "future_runtime_held_reentry_may_be_considered": False,
        "selected_runtime_held_state_recorded": False,
        "runtime_held_state_created": False,
        "runtime_held_state_local_only": False,
        "runtime_held_state_read_only": False,
        "held_state_basis_reference_only": False,
        "raw_state_body_embedded_false": False,
        "state_mutation_performed_false": False,
        "state_update_performed_false": False,
        "selected_runtime_held_state_boundary_recorded": False,
        "future_runtime_held_state_may_be_considered": False,
        "selected_runtime_recorded": False,
        "runtime_created": False,
        "runtime_local_only": False,
        "runtime_read_only": False,
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


def _validate_request_shape(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    question = request.get("local_relevance_medium_read_only_runtime_held_reentry_question")
    checks.append(
        _new_check(
            "runtime-held re-entry question declared",
            isinstance(question, str) and bool(question.strip()),
            "declared runtime-held re-entry question",
            question,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_QUESTION_UNDECLARED",
        )
    )

    intent = request.get("local_relevance_medium_read_only_runtime_held_reentry_intent")
    checks.append(
        _new_check(
            "runtime-held re-entry intent supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _new_check(
            "runtime-held re-entry block intent not requested",
            intent != INTENT_BLOCK,
            "not block intent",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BLOCK_REQUESTED",
        )
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

    held_reentry_type = request.get("held_reentry_type")
    checks.append(
        _new_check(
            "held re-entry type declared",
            held_reentry_type not in (None, ""),
            HELD_REENTRY_TYPE,
            held_reentry_type,
            "HELD_REENTRY_TYPE_MISSING",
        )
    )
    checks.append(
        _new_check(
            "held re-entry type exact",
            held_reentry_type == HELD_REENTRY_TYPE,
            HELD_REENTRY_TYPE,
            held_reentry_type,
            "HELD_REENTRY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY",
        )
    )

    held_reentry_scope = request.get("held_reentry_scope")
    checks.append(
        _new_check(
            "held re-entry scope declared",
            held_reentry_scope not in (None, ""),
            HELD_REENTRY_SCOPE,
            held_reentry_scope,
            "HELD_REENTRY_SCOPE_MISSING",
        )
    )
    checks.append(
        _new_check(
            "held re-entry scope exact",
            held_reentry_scope == HELD_REENTRY_SCOPE,
            HELD_REENTRY_SCOPE,
            held_reentry_scope,
            "HELD_REENTRY_SCOPE_NOT_SELECTED_RUNTIME_HELD_REENTRY_ONLY",
        )
    )


def _validate_artifact_selected_command(
    checks: list[dict[str, Any]],
    artifact_name: str,
    artifact: Mapping[str, Any] | None,
) -> None:
    passed, detail = _selected_command_posture(artifact)
    checks.append(
        _new_check(
            f"{artifact_name} selected command state",
            passed,
            SELECTED_COMMAND,
            detail,
            "SELECTED_COMMAND_NOT_STATE",
        )
    )


def _validate_upstream_postures(
    checks: list[dict[str, Any]],
    artifacts: Mapping[str, Mapping[str, Any] | None],
) -> dict[str, bool]:
    boundary = artifacts.get("selected_runtime_held_reentry_boundary_artifact")
    held_state = artifacts.get("selected_runtime_held_state_artifact")
    held_state_boundary = artifacts.get("selected_runtime_held_state_boundary_artifact")
    runtime = artifacts.get("selected_runtime_artifact")
    runtime_boundary = artifacts.get("selected_runtime_boundary_artifact")
    runtime_permission = artifacts.get("selected_runtime_permission_artifact")
    operation_execution = artifacts.get("selected_operation_execution_artifact")

    upstream = _empty_upstream()
    upstream["selected_runtime_held_reentry_boundary_recorded"] = _add_bool_posture_check(
        checks,
        "selected runtime-held-re-entry boundary recorded",
        boundary,
        (
            "selected_runtime_held_reentry_boundary_recorded",
            "local_relevance_medium_read_only_runtime_held_reentry_boundary_recorded",
            "boundary_recorded",
        ),
        "SELECTED_RUNTIME_HELD_REENTRY_BOUNDARY_NOT_RECORDED",
    )
    upstream["future_runtime_held_reentry_may_be_considered"] = _add_bool_posture_check(
        checks,
        "future runtime-held re-entry may be considered",
        boundary,
        ("future_runtime_held_reentry_may_be_considered",),
        "FUTURE_RUNTIME_HELD_REENTRY_MAY_NOT_BE_CONSIDERED",
    )
    _add_false_posture_check(
        checks,
        "boundary raw state body not embedded",
        boundary,
        ("raw_state_body_embedded",),
        "RAW_STATE_BODY_EMBEDDED",
    )
    _add_false_posture_check(
        checks,
        "boundary state mutation not performed",
        boundary,
        ("state_mutation_performed",),
        "STATE_MUTATION_PERFORMED",
    )
    _add_false_posture_check(
        checks,
        "boundary state update not performed",
        boundary,
        ("state_update_performed",),
        "STATE_UPDATE_PERFORMED",
    )

    upstream["selected_runtime_held_state_recorded"] = _add_bool_posture_check(
        checks,
        "selected runtime-held state recorded",
        held_state,
        (
            "selected_runtime_held_state_recorded",
            "local_relevance_medium_read_only_runtime_held_state_recorded",
            "held_state_recorded",
        ),
        "SELECTED_RUNTIME_HELD_STATE_NOT_RECORDED",
    )
    upstream["runtime_held_state_created"] = _add_bool_posture_check(
        checks,
        "runtime-held state created",
        held_state,
        ("runtime_held_state_created",),
        "RUNTIME_HELD_STATE_NOT_CREATED",
    )
    upstream["runtime_held_state_local_only"] = _add_bool_posture_check(
        checks,
        "runtime-held state local only",
        held_state,
        ("runtime_held_state_local_only",),
        "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE",
    )
    upstream["runtime_held_state_read_only"] = _add_bool_posture_check(
        checks,
        "runtime-held state read only",
        held_state,
        ("runtime_held_state_read_only",),
        "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE",
    )
    upstream["held_state_basis_reference_only"] = _add_bool_posture_check(
        checks,
        "held state basis reference only",
        held_state,
        ("held_state_basis_reference_only",),
        "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE",
    )
    upstream["raw_state_body_embedded_false"] = _add_false_posture_check(
        checks,
        "runtime-held state raw state body not embedded",
        held_state,
        ("raw_state_body_embedded",),
        "RAW_STATE_BODY_EMBEDDED",
    )
    upstream["state_mutation_performed_false"] = _add_false_posture_check(
        checks,
        "runtime-held state mutation not performed",
        held_state,
        ("state_mutation_performed",),
        "STATE_MUTATION_PERFORMED",
    )
    upstream["state_update_performed_false"] = _add_false_posture_check(
        checks,
        "runtime-held state update not performed",
        held_state,
        ("state_update_performed",),
        "STATE_UPDATE_PERFORMED",
    )

    upstream["selected_runtime_held_state_boundary_recorded"] = _add_bool_posture_check(
        checks,
        "selected runtime-held-state boundary recorded",
        held_state_boundary,
        (
            "selected_runtime_held_state_boundary_recorded",
            "local_relevance_medium_read_only_runtime_held_state_boundary_recorded",
            "boundary_recorded",
        ),
        "SELECTED_RUNTIME_HELD_STATE_BOUNDARY_NOT_RECORDED",
    )
    upstream["future_runtime_held_state_may_be_considered"] = _add_bool_posture_check(
        checks,
        "future runtime-held state may be considered",
        held_state_boundary,
        ("future_runtime_held_state_may_be_considered",),
        "FUTURE_RUNTIME_HELD_STATE_MAY_NOT_BE_CONSIDERED",
    )
    upstream["selected_runtime_recorded"] = _add_bool_posture_check(
        checks,
        "selected runtime recorded",
        runtime,
        ("selected_runtime_recorded", "local_relevance_medium_read_only_runtime_recorded"),
        "SELECTED_RUNTIME_NOT_RECORDED",
    )
    upstream["runtime_created"] = _add_bool_posture_check(
        checks,
        "runtime created",
        runtime,
        ("runtime_created",),
        "RUNTIME_NOT_CREATED",
    )
    upstream["runtime_local_only"] = _add_bool_posture_check(
        checks,
        "runtime local only",
        runtime,
        ("runtime_local_only",),
        "RUNTIME_LOCAL_ONLY_NOT_TRUE",
    )
    upstream["runtime_read_only"] = _add_bool_posture_check(
        checks,
        "runtime read only",
        runtime,
        ("runtime_read_only",),
        "RUNTIME_READ_ONLY_NOT_TRUE",
    )
    upstream["selected_runtime_boundary_recorded"] = _add_bool_posture_check(
        checks,
        "selected runtime boundary recorded",
        runtime_boundary,
        (
            "selected_runtime_boundary_recorded",
            "local_relevance_medium_read_only_runtime_boundary_recorded",
        ),
        "SELECTED_RUNTIME_BOUNDARY_NOT_RECORDED",
    )
    upstream["future_runtime_may_be_considered"] = _add_bool_posture_check(
        checks,
        "future runtime may be considered",
        runtime_boundary,
        ("future_runtime_may_be_considered",),
        "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED",
    )
    upstream["selected_runtime_permission_recorded"] = _add_bool_posture_check(
        checks,
        "selected runtime permission recorded",
        runtime_permission,
        (
            "selected_runtime_permission_recorded",
            "local_relevance_medium_read_only_runtime_permission_recorded",
        ),
        "SELECTED_RUNTIME_PERMISSION_NOT_RECORDED",
    )
    upstream["runtime_permission_created"] = _add_bool_posture_check(
        checks,
        "runtime permission created",
        runtime_permission,
        ("runtime_permission_created",),
        "RUNTIME_PERMISSION_NOT_CREATED",
    )
    upstream["runtime_permission_local_only"] = _add_bool_posture_check(
        checks,
        "runtime permission local only",
        runtime_permission,
        ("runtime_permission_local_only",),
        "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE",
    )
    upstream["runtime_permission_read_only"] = _add_bool_posture_check(
        checks,
        "runtime permission read only",
        runtime_permission,
        ("runtime_permission_read_only",),
        "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE",
    )
    upstream["selected_operation_execution_recorded"] = _add_bool_posture_check(
        checks,
        "selected operation execution recorded",
        operation_execution,
        (
            "selected_operation_execution_recorded",
            "local_relevance_medium_read_only_operation_execution_recorded",
        ),
        "SELECTED_OPERATION_EXECUTION_NOT_RECORDED",
    )
    upstream["operation_execution_created"] = _add_bool_posture_check(
        checks,
        "operation execution created",
        operation_execution,
        ("operation_execution_created",),
        "OPERATION_EXECUTION_NOT_CREATED",
    )
    upstream["operation_execution_performed"] = _add_bool_posture_check(
        checks,
        "operation execution performed",
        operation_execution,
        ("operation_execution_performed",),
        "OPERATION_EXECUTION_NOT_PERFORMED",
    )
    upstream["operation_execution_local_only"] = _add_bool_posture_check(
        checks,
        "operation execution local only",
        operation_execution,
        ("operation_execution_local_only",),
        "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    )
    upstream["operation_execution_read_only"] = _add_bool_posture_check(
        checks,
        "operation execution read only",
        operation_execution,
        ("operation_execution_read_only",),
        "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE",
    )
    return upstream


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "local_relevance_medium_read_only_runtime_held_reentry_id": str(
            request.get("local_relevance_medium_read_only_runtime_held_reentry_id")
            or DEFAULT_HELD_REENTRY_ID
        ),
        "local_relevance_medium_read_only_runtime_held_reentry_type": HELD_REENTRY_TYPE,
        "local_relevance_medium_read_only_runtime_held_reentry_version": RESULT_VERSION,
        "result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "intent": request.get("local_relevance_medium_read_only_runtime_held_reentry_intent"),
    }


def _result_level_non_claims_canonical_false(non_claims: Mapping[str, Any]) -> bool:
    return all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _build_held_reentry_object(
    request: Mapping[str, Any],
    bases: Mapping[str, Mapping[str, Any]],
    upstream: Mapping[str, bool],
    recorded: bool,
) -> dict[str, Any]:
    selected_command = request.get("selected_command", SELECTED_COMMAND)
    held_reentry: dict[str, Any] = {
        "held_reentry_id": str(
            request.get("local_relevance_medium_read_only_runtime_held_reentry_id")
            or DEFAULT_HELD_REENTRY_ID
        ),
        "held_reentry_type": HELD_REENTRY_TYPE,
        "held_reentry_version": RESULT_VERSION,
        "held_reentry_scope": HELD_REENTRY_SCOPE,
        "basis_runtime_held_reentry_boundary_artifact": _request_artifact(
            request,
            "selected_runtime_held_reentry_boundary_artifact",
            DEFAULT_RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT,
        ),
        "basis_runtime_held_reentry_boundary_outcome": bases[
            "selected_runtime_held_reentry_boundary_artifact_basis"
        ].get("outcome"),
        "basis_runtime_held_reentry_boundary_result_version": bases[
            "selected_runtime_held_reentry_boundary_artifact_basis"
        ].get("result_version"),
        "basis_runtime_held_reentry_boundary_failed_check_count": bases[
            "selected_runtime_held_reentry_boundary_artifact_basis"
        ].get("failed_check_count"),
        "basis_runtime_held_state_artifact": _request_artifact(
            request,
            "selected_runtime_held_state_artifact",
            DEFAULT_RUNTIME_HELD_STATE_ARTIFACT,
        ),
        "basis_runtime_held_state_outcome": bases[
            "selected_runtime_held_state_artifact_basis"
        ].get("outcome"),
        "basis_runtime_held_state_result_version": bases[
            "selected_runtime_held_state_artifact_basis"
        ].get("result_version"),
        "basis_runtime_held_state_failed_check_count": bases[
            "selected_runtime_held_state_artifact_basis"
        ].get("failed_check_count"),
        "basis_runtime_held_state_boundary_artifact": _request_artifact(
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
        "basis_runtime_artifact": _request_artifact(
            request, "selected_runtime_artifact", DEFAULT_RUNTIME_ARTIFACT
        ),
        "basis_runtime_outcome": bases["selected_runtime_artifact_basis"].get("outcome"),
        "basis_runtime_result_version": bases["selected_runtime_artifact_basis"].get(
            "result_version"
        ),
        "basis_runtime_failed_check_count": bases["selected_runtime_artifact_basis"].get(
            "failed_check_count"
        ),
        "basis_runtime_boundary_artifact": _request_artifact(
            request,
            "selected_runtime_boundary_artifact",
            DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
        ),
        "basis_runtime_boundary_outcome": bases[
            "selected_runtime_boundary_artifact_basis"
        ].get("outcome"),
        "basis_runtime_boundary_result_version": bases[
            "selected_runtime_boundary_artifact_basis"
        ].get("result_version"),
        "basis_runtime_boundary_failed_check_count": bases[
            "selected_runtime_boundary_artifact_basis"
        ].get("failed_check_count"),
        "basis_runtime_permission_artifact": _request_artifact(
            request,
            "selected_runtime_permission_artifact",
            DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
        ),
        "basis_runtime_permission_outcome": bases[
            "selected_runtime_permission_artifact_basis"
        ].get("outcome"),
        "basis_runtime_permission_result_version": bases[
            "selected_runtime_permission_artifact_basis"
        ].get("result_version"),
        "basis_runtime_permission_failed_check_count": bases[
            "selected_runtime_permission_artifact_basis"
        ].get("failed_check_count"),
        "basis_operation_execution_artifact": _request_artifact(
            request,
            "selected_operation_execution_artifact",
            DEFAULT_OPERATION_EXECUTION_ARTIFACT,
        ),
        "basis_operation_execution_outcome": bases[
            "selected_operation_execution_artifact_basis"
        ].get("outcome"),
        "basis_operation_execution_result_version": bases[
            "selected_operation_execution_artifact_basis"
        ].get("result_version"),
        "basis_operation_execution_failed_check_count": bases[
            "selected_operation_execution_artifact_basis"
        ].get("failed_check_count"),
        "selected_command": selected_command,
        "selected_command_is_state": selected_command == SELECTED_COMMAND,
        "selected_runtime_held_reentry_boundary_recorded": bool(
            recorded and upstream.get("selected_runtime_held_reentry_boundary_recorded")
        ),
        "future_runtime_held_reentry_may_be_considered": bool(
            recorded and upstream.get("future_runtime_held_reentry_may_be_considered")
        ),
        "selected_runtime_held_state_recorded": bool(
            recorded and upstream.get("selected_runtime_held_state_recorded")
        ),
        "runtime_held_state_created": bool(
            recorded and upstream.get("runtime_held_state_created")
        ),
        "runtime_held_state_local_only": bool(
            recorded and upstream.get("runtime_held_state_local_only")
        ),
        "runtime_held_state_read_only": bool(
            recorded and upstream.get("runtime_held_state_read_only")
        ),
        "held_state_basis_reference_only": bool(
            recorded and upstream.get("held_state_basis_reference_only")
        ),
        "raw_state_body_embedded": False,
        "state_mutation_performed": False,
        "state_update_performed": False,
        "selected_runtime_held_state_boundary_recorded": bool(
            recorded and upstream.get("selected_runtime_held_state_boundary_recorded")
        ),
        "future_runtime_held_state_may_be_considered": bool(
            recorded and upstream.get("future_runtime_held_state_may_be_considered")
        ),
        "selected_runtime_recorded": bool(
            recorded and upstream.get("selected_runtime_recorded")
        ),
        "runtime_created": bool(recorded and upstream.get("runtime_created")),
        "runtime_local_only": bool(recorded and upstream.get("runtime_local_only")),
        "runtime_read_only": bool(recorded and upstream.get("runtime_read_only")),
        "selected_runtime_boundary_recorded": bool(
            recorded and upstream.get("selected_runtime_boundary_recorded")
        ),
        "future_runtime_may_be_considered": bool(
            recorded and upstream.get("future_runtime_may_be_considered")
        ),
        "selected_runtime_permission_recorded": bool(
            recorded and upstream.get("selected_runtime_permission_recorded")
        ),
        "runtime_permission_created": bool(
            recorded and upstream.get("runtime_permission_created")
        ),
        "runtime_permission_local_only": bool(
            recorded and upstream.get("runtime_permission_local_only")
        ),
        "runtime_permission_read_only": bool(
            recorded and upstream.get("runtime_permission_read_only")
        ),
        "selected_operation_execution_recorded": bool(
            recorded and upstream.get("selected_operation_execution_recorded")
        ),
        "operation_execution_created": bool(
            recorded and upstream.get("operation_execution_created")
        ),
        "operation_execution_performed": bool(
            recorded and upstream.get("operation_execution_performed")
        ),
        "operation_execution_local_only": bool(
            recorded and upstream.get("operation_execution_local_only")
        ),
        "operation_execution_read_only": bool(
            recorded and upstream.get("operation_execution_read_only")
        ),
        "local_relevance_medium_read_only_runtime_held_reentry_recorded": bool(recorded),
        "runtime_held_reentry_created": bool(recorded),
        "runtime_held_reentry_local_only": bool(recorded),
        "runtime_held_reentry_read_only": bool(recorded),
        "held_reentry_basis_reference_only": bool(recorded),
        "runtime_v0_failure_evidence_preserved": True,
        "runtime_v2_failure_evidence_preserved": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
    }
    for field in REQUIRED_FALSE_NON_CLAIMS:
        if field.startswith("artifact_existence_treated"):
            continue
        if field.startswith("latest_file_posture"):
            continue
        if field.startswith("repo_local_availability"):
            continue
        if field.startswith("hidden_repo_state"):
            continue
        if field.startswith("prior_artifacts"):
            continue
        if field.startswith("predecessor_failure"):
            continue
        if field.startswith("runtime_v0_failure"):
            continue
        if field.startswith("runtime_v2_failure"):
            continue
        if field.startswith("runtime_boundary_v0_failure"):
            continue
        held_reentry[field] = False
    return held_reentry


def _build_statement(
    held_reentry: Mapping[str, Any],
    bases: Mapping[str, Mapping[str, Any]],
    recorded: bool,
) -> dict[str, Any]:
    return {
        "local_relevance_medium_read_only_runtime_held_reentry_recorded": recorded,
        "basis_runtime_held_reentry_boundary_artifact_preserved": bases[
            "selected_runtime_held_reentry_boundary_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_runtime_held_state_artifact_preserved": bases[
            "selected_runtime_held_state_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_runtime_held_state_boundary_artifact_preserved": bases[
            "selected_runtime_held_state_boundary_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_runtime_artifact_preserved": bases["selected_runtime_artifact_basis"].get(
            "artifact_preserved"
        )
        is True,
        "basis_runtime_boundary_artifact_preserved": bases[
            "selected_runtime_boundary_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_runtime_permission_artifact_preserved": bases[
            "selected_runtime_permission_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_operation_execution_artifact_preserved": bases[
            "selected_operation_execution_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "selected_command_preserved": held_reentry.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": held_reentry.get("selected_command_is_state") is True,
        "selected_runtime_held_reentry_boundary_recorded": held_reentry.get(
            "selected_runtime_held_reentry_boundary_recorded"
        )
        is True,
        "future_runtime_held_reentry_may_be_considered": held_reentry.get(
            "future_runtime_held_reentry_may_be_considered"
        )
        is True,
        "selected_runtime_held_state_recorded": held_reentry.get(
            "selected_runtime_held_state_recorded"
        )
        is True,
        "runtime_held_state_created": held_reentry.get("runtime_held_state_created")
        is True,
        "runtime_held_state_local_only": held_reentry.get("runtime_held_state_local_only")
        is True,
        "runtime_held_state_read_only": held_reentry.get("runtime_held_state_read_only")
        is True,
        "held_state_basis_reference_only": held_reentry.get("held_state_basis_reference_only")
        is True,
        "selected_runtime_held_state_boundary_recorded": held_reentry.get(
            "selected_runtime_held_state_boundary_recorded"
        )
        is True,
        "future_runtime_held_state_may_be_considered": held_reentry.get(
            "future_runtime_held_state_may_be_considered"
        )
        is True,
        "selected_runtime_recorded": held_reentry.get("selected_runtime_recorded") is True,
        "runtime_created": held_reentry.get("runtime_created") is True,
        "runtime_local_only": held_reentry.get("runtime_local_only") is True,
        "runtime_read_only": held_reentry.get("runtime_read_only") is True,
        "selected_runtime_boundary_recorded": held_reentry.get(
            "selected_runtime_boundary_recorded"
        )
        is True,
        "future_runtime_may_be_considered": held_reentry.get("future_runtime_may_be_considered")
        is True,
        "selected_runtime_permission_recorded": held_reentry.get(
            "selected_runtime_permission_recorded"
        )
        is True,
        "runtime_permission_created": held_reentry.get("runtime_permission_created") is True,
        "runtime_permission_local_only": held_reentry.get("runtime_permission_local_only")
        is True,
        "runtime_permission_read_only": held_reentry.get("runtime_permission_read_only")
        is True,
        "selected_operation_execution_recorded": held_reentry.get(
            "selected_operation_execution_recorded"
        )
        is True,
        "operation_execution_created": held_reentry.get("operation_execution_created")
        is True,
        "operation_execution_performed": held_reentry.get("operation_execution_performed")
        is True,
        "operation_execution_local_only": held_reentry.get("operation_execution_local_only")
        is True,
        "operation_execution_read_only": held_reentry.get("operation_execution_read_only")
        is True,
        "runtime_held_reentry_created": held_reentry.get("runtime_held_reentry_created")
        is True,
        "runtime_held_reentry_local_only": held_reentry.get("runtime_held_reentry_local_only")
        is True,
        "runtime_held_reentry_read_only": held_reentry.get("runtime_held_reentry_read_only")
        is True,
        "held_reentry_basis_reference_only": held_reentry.get(
            "held_reentry_basis_reference_only"
        )
        is True,
        "prior_result_reentry_cycle_created": False,
        "second_operation_created": False,
        "continuation_created": False,
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


def _build_non_meaning() -> dict[str, bool]:
    return {
        "not_prior_result_reentry_cycle": True,
        "not_second_operation": True,
        "not_continuation": True,
        "not_runtime_hosting": True,
        "not_runtime_loop": True,
        "not_daemon_behavior": True,
        "not_public_api": True,
        "not_participant_facing_interface": True,
        "not_distributed_network_behavior": True,
        "not_general_operation_permission": True,
        "not_general_lookup_permission": True,
        "not_arbitrary_lookup_permission": True,
        "not_registry": True,
        "not_search": True,
        "not_query_surface": True,
        "not_ranking": True,
        "not_authority_currentness_truth": True,
        "not_older_runtime_authority_import": True,
        "not_runtime_v0_repair": True,
        "not_runtime_v0_hide": True,
        "not_runtime_v0_pass_claim": True,
        "not_runtime_v2_repair": True,
        "not_runtime_v2_hide": True,
        "not_runtime_v2_pass_claim": True,
        "not_runtime_boundary_v0_repair": True,
        "not_runtime_boundary_v0_hide": True,
        "not_runtime_boundary_v0_pass_claim": True,
        "not_follow_on_work": True,
    }


def _add_generated_held_reentry_checks(
    checks: list[dict[str, Any]],
    held_reentry: Mapping[str, Any],
    recorded: bool,
) -> None:
    true_codes = {
        "selected_runtime_held_reentry_boundary_recorded": "SELECTED_RUNTIME_HELD_REENTRY_BOUNDARY_NOT_RECORDED",
        "future_runtime_held_reentry_may_be_considered": "FUTURE_RUNTIME_HELD_REENTRY_MAY_NOT_BE_CONSIDERED",
        "selected_runtime_held_state_recorded": "SELECTED_RUNTIME_HELD_STATE_NOT_RECORDED",
        "runtime_held_state_created": "RUNTIME_HELD_STATE_NOT_CREATED",
        "runtime_held_state_local_only": "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE",
        "runtime_held_state_read_only": "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE",
        "held_state_basis_reference_only": "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE",
        "selected_runtime_held_state_boundary_recorded": "SELECTED_RUNTIME_HELD_STATE_BOUNDARY_NOT_RECORDED",
        "future_runtime_held_state_may_be_considered": "FUTURE_RUNTIME_HELD_STATE_MAY_NOT_BE_CONSIDERED",
        "selected_runtime_recorded": "SELECTED_RUNTIME_NOT_RECORDED",
        "runtime_created": "RUNTIME_NOT_CREATED",
        "runtime_local_only": "RUNTIME_LOCAL_ONLY_NOT_TRUE",
        "runtime_read_only": "RUNTIME_READ_ONLY_NOT_TRUE",
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
        "local_relevance_medium_read_only_runtime_held_reentry_recorded": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_NOT_RECORDED",
        "runtime_held_reentry_created": "RUNTIME_HELD_REENTRY_NOT_CREATED",
        "runtime_held_reentry_local_only": "RUNTIME_HELD_REENTRY_LOCAL_ONLY_NOT_TRUE",
        "runtime_held_reentry_read_only": "RUNTIME_HELD_REENTRY_READ_ONLY_NOT_TRUE",
        "held_reentry_basis_reference_only": "HELD_REENTRY_BASIS_REFERENCE_ONLY_NOT_TRUE",
    }
    for field, code in true_codes.items():
        expected = True if recorded else False
        checks.append(
            _new_check(
                field.replace("_", " "),
                held_reentry.get(field) is expected,
                expected,
                held_reentry.get(field),
                code,
            )
        )
    false_checks = (
        "raw_state_body_embedded",
        "state_mutation_performed",
        "state_update_performed",
        "prior_result_reentry_cycle_created",
        "second_operation_created",
        "continuation_created",
        "runtime_hosting_created",
        "runtime_loop_created",
        "daemon_behavior_created",
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
    for field in false_checks:
        checks.append(
            _new_check(
                f"{field} false",
                held_reentry.get(field) is False,
                False,
                held_reentry.get(field),
                TOP_LEVEL_BLOCK_FIELD_CODES.get(
                    field,
                    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_REQUEST_MALFORMED",
                ),
            )
        )


def _compose_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    bases: Mapping[str, Mapping[str, Any]],
    upstream: Mapping[str, bool],
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    non_claims = _canonical_non_claims()
    held_reentry = _build_held_reentry_object(request, bases, upstream, recorded)
    block_code = _first_failed_code(checks) if outcome == OUTCOME_BLOCKED else None
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_runtime_held_reentry_metadata": _metadata(request),
        "declared_local_relevance_medium_read_only_runtime_held_reentry_question": {
            "question": _sanitize(
                request.get("local_relevance_medium_read_only_runtime_held_reentry_question")
            ),
            "intent": _sanitize(
                request.get("local_relevance_medium_read_only_runtime_held_reentry_intent")
            ),
            "request": _sanitize(copy.deepcopy(dict(request))),
        },
        "selected_runtime_held_reentry_boundary_artifact_basis": dict(
            bases["selected_runtime_held_reentry_boundary_artifact_basis"]
        ),
        "selected_runtime_held_state_artifact_basis": dict(
            bases["selected_runtime_held_state_artifact_basis"]
        ),
        "selected_runtime_held_state_boundary_artifact_basis": dict(
            bases["selected_runtime_held_state_boundary_artifact_basis"]
        ),
        "selected_runtime_artifact_basis": dict(bases["selected_runtime_artifact_basis"]),
        "selected_runtime_boundary_artifact_basis": dict(
            bases["selected_runtime_boundary_artifact_basis"]
        ),
        "selected_runtime_permission_artifact_basis": dict(
            bases["selected_runtime_permission_artifact_basis"]
        ),
        "selected_operation_execution_artifact_basis": dict(
            bases["selected_operation_execution_artifact_basis"]
        ),
        "local_relevance_medium_read_only_runtime_held_reentry": _sanitize(held_reentry),
        "local_relevance_medium_read_only_runtime_held_reentry_checks": checks,
        "local_relevance_medium_read_only_runtime_held_reentry_statement": _build_statement(
            held_reentry, bases, recorded
        ),
        "local_relevance_medium_read_only_runtime_held_reentry_non_meaning": _build_non_meaning(),
        "additional_basis_required": _sanitize(request.get("additional_basis_context", []))
        if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        else [],
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis", []))
        if outcome == OUTCOME_NOT_RECORDED
        else [],
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": _block_dict(block_code, request.get("block_reason")),
    }
    result["local_relevance_medium_read_only_runtime_held_reentry_summary"] = (
        build_local_relevance_medium_read_only_runtime_held_reentry_v0_min_summary(result)
    )
    return result


def _blocked_result_from_code(
    code: str,
    reason: Any,
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    bounded_request = dict(
        request
        or {
            "local_relevance_medium_read_only_runtime_held_reentry_id": DEFAULT_HELD_REENTRY_ID,
            "local_relevance_medium_read_only_runtime_held_reentry_question": "",
            "local_relevance_medium_read_only_runtime_held_reentry_intent": INTENT_RECORD,
            "selected_command": SELECTED_COMMAND,
            "held_reentry_type": HELD_REENTRY_TYPE,
            "held_reentry_scope": HELD_REENTRY_SCOPE,
            "declared_non_claims": _canonical_non_claims(),
        }
    )
    checks = [
        _new_check(
            "declared local relevance medium read-only runtime-held re-entry request readable",
            False,
            "readable declared request mapping",
            reason,
            code,
        )
    ]
    return _compose_result(
        bounded_request,
        checks,
        OUTCOME_BLOCKED,
        _basis_map_with_defaults(),
        _empty_upstream(),
    )


def build_declared_local_relevance_medium_read_only_runtime_held_reentry_v0_min_request(
    *,
    local_relevance_medium_read_only_runtime_held_reentry_id: str = DEFAULT_HELD_REENTRY_ID,
    selected_runtime_held_reentry_boundary_artifact: Path | str = DEFAULT_RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT,
    selected_runtime_held_state_artifact: Path | str = DEFAULT_RUNTIME_HELD_STATE_ARTIFACT,
    selected_runtime_held_state_boundary_artifact: Path | str = DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT,
    selected_runtime_artifact: Path | str = DEFAULT_RUNTIME_ARTIFACT,
    selected_runtime_boundary_artifact: Path | str = DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
    selected_runtime_permission_artifact: Path | str = DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
    selected_operation_execution_artifact: Path | str = DEFAULT_OPERATION_EXECUTION_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    held_reentry_type: str = HELD_REENTRY_TYPE,
    held_reentry_scope: str = HELD_REENTRY_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    """Build a declared request for this one runtime-held-re-entry resolver."""

    non_claims: dict[str, Any] = _canonical_non_claims()
    if declared_non_claims is not None:
        for key, value in declared_non_claims.items():
            non_claims[str(key)] = value

    request: dict[str, Any] = {
        "local_relevance_medium_read_only_runtime_held_reentry_id": (
            local_relevance_medium_read_only_runtime_held_reentry_id
        ),
        "local_relevance_medium_read_only_runtime_held_reentry_question": CORE_QUESTION,
        "local_relevance_medium_read_only_runtime_held_reentry_intent": intent,
        "selected_runtime_held_reentry_boundary_artifact": str(
            selected_runtime_held_reentry_boundary_artifact
        ),
        "selected_runtime_held_state_artifact": str(selected_runtime_held_state_artifact),
        "selected_runtime_held_state_boundary_artifact": str(
            selected_runtime_held_state_boundary_artifact
        ),
        "selected_runtime_artifact": str(selected_runtime_artifact),
        "selected_runtime_boundary_artifact": str(selected_runtime_boundary_artifact),
        "selected_runtime_permission_artifact": str(selected_runtime_permission_artifact),
        "selected_operation_execution_artifact": str(selected_operation_execution_artifact),
        "selected_command": selected_command,
        "held_reentry_type": held_reentry_type,
        "held_reentry_scope": held_reentry_scope,
        "declared_non_claims": non_claims,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
        "older_runtime_lineage_imported_as_authority": False,
        "older_runtime_permission_treated_as_current": False,
        "runtime_authority_imported": False,
        "raw_state_body_embedded": False,
        "state_mutation_performed": False,
        "state_update_performed": False,
        "runtime_v0_failure_repaired": False,
        "runtime_v0_failure_hidden": False,
        "runtime_v0_failure_claimed_passed": False,
        "runtime_v2_failure_repaired": False,
        "runtime_v2_failure_hidden": False,
        "runtime_v2_failure_claimed_passed": False,
        "runtime_boundary_v0_failure_repaired": False,
        "runtime_boundary_v0_failure_hidden": False,
        "runtime_boundary_v0_failure_claimed_passed": False,
        "predecessor_failure_repaired": False,
        "predecessor_failure_hidden": False,
        "predecessor_failure_claimed_passed": False,
        "follow_on_work_authorized": False,
    }
    request.update(copy.deepcopy(extra_fields))
    return request


def resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
    declared_local_relevance_medium_read_only_runtime_held_reentry: Mapping[str, Any]
    | None = None,
) -> dict[str, Any]:
    """Resolve one selected-state local read-only runtime-held re-entry object."""

    if not isinstance(
        declared_local_relevance_medium_read_only_runtime_held_reentry,
        MappingABC,
    ):
        return _blocked_result_from_code(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_REQUEST_MALFORMED",
            type(declared_local_relevance_medium_read_only_runtime_held_reentry).__name__,
        )

    request = copy.deepcopy(dict(declared_local_relevance_medium_read_only_runtime_held_reentry))
    checks: list[dict[str, Any]] = [
        _new_check(
            "declared runtime-held re-entry request mapping",
            True,
            "mapping",
            "mapping",
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_REQUEST_MALFORMED",
        )
    ]
    bases = _basis_map_with_defaults()
    upstream = _empty_upstream()

    _validate_request_shape(request, checks)
    _validate_top_level_block_fields(request, checks)
    _validate_declared_non_claims(request, checks)

    if _first_failed_code(checks):
        return _compose_result(request, checks, OUTCOME_BLOCKED, bases, upstream)

    intent = request.get("local_relevance_medium_read_only_runtime_held_reentry_intent")
    if intent == INTENT_DO_NOT_RECORD:
        return _compose_result(request, checks, OUTCOME_NOT_RECORDED, bases, upstream)

    artifacts: dict[str, Mapping[str, Any] | None] = {}
    for spec in ARTIFACT_SPECS:
        basis, artifact = _validate_basis_artifact(request, spec, checks)
        bases[str(spec["basis_key"])] = basis
        artifacts[str(spec["path_key"])] = artifact

    for spec in ARTIFACT_SPECS:
        _validate_artifact_selected_command(
            checks,
            str(spec["label"]),
            artifacts.get(str(spec["path_key"])),
        )

    upstream = _validate_upstream_postures(checks, artifacts)
    checks.append(
        _new_check(
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
    )
    checks.append(
        _new_check(
            "result-level required false non-claims canonical false",
            _result_level_non_claims_canonical_false(_canonical_non_claims()),
            True,
            _result_level_non_claims_canonical_false(_canonical_non_claims()),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )

    recorded = _first_failed_code(checks) is None
    held_reentry = _build_held_reentry_object(request, bases, upstream, recorded)
    _add_generated_held_reentry_checks(checks, held_reentry, recorded)

    outcome = OUTCOME_RECORDED if _first_failed_code(checks) is None else OUTCOME_BLOCKED
    return _compose_result(
        request,
        checks,
        outcome,
        bases,
        upstream if outcome == OUTCOME_RECORDED else _empty_upstream(),
    )


def resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min_from_path(
    declared_local_relevance_medium_read_only_runtime_held_reentry_path: Path | str,
) -> dict[str, Any]:
    """Read a declared runtime-held-re-entry request from JSON."""

    try:
        loaded = json.loads(
            Path(declared_local_relevance_medium_read_only_runtime_held_reentry_path).read_text(
                encoding="utf-8"
            )
        )
    except Exception as exc:  # noqa: BLE001 - converted into bounded result.
        return _blocked_result_from_code(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_REQUEST_UNREADABLE",
            f"{exc.__class__.__name__}: {exc}",
        )
    if not isinstance(loaded, MappingABC):
        return _blocked_result_from_code(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_REQUEST_MALFORMED",
            "request JSON is not an object",
        )
    return resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(loaded)


def build_local_relevance_medium_read_only_runtime_held_reentry_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact JSON-safe summary from a resolver result."""

    checks = result.get("local_relevance_medium_read_only_runtime_held_reentry_checks", [])
    checks = checks if isinstance(checks, list) else []
    held_reentry = result.get("local_relevance_medium_read_only_runtime_held_reentry", {})
    held_reentry = held_reentry if isinstance(held_reentry, MappingABC) else {}
    statement = result.get(
        "local_relevance_medium_read_only_runtime_held_reentry_statement", {}
    )
    statement = statement if isinstance(statement, MappingABC) else {}
    metadata = result.get(
        "local_relevance_medium_read_only_runtime_held_reentry_metadata", {}
    )
    metadata = metadata if isinstance(metadata, MappingABC) else {}
    block = result.get("block", {})
    block = block if isinstance(block, MappingABC) else {}
    non_claims = result.get("non_claims", {})
    non_claims = non_claims if isinstance(non_claims, MappingABC) else {}
    passed_count = sum(
        1
        for check in checks
        if isinstance(check, MappingABC) and check.get("passed") is True
    )
    failed_count = sum(
        1
        for check in checks
        if isinstance(check, MappingABC) and check.get("passed") is not True
    )
    canonical_false = _result_level_non_claims_canonical_false(non_claims)
    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "held_reentry_id": held_reentry.get("held_reentry_id")
        or metadata.get("local_relevance_medium_read_only_runtime_held_reentry_id"),
        "question": result.get(
            "declared_local_relevance_medium_read_only_runtime_held_reentry_question",
            {},
        ).get("question")
        if isinstance(
            result.get(
                "declared_local_relevance_medium_read_only_runtime_held_reentry_question"
            ),
            MappingABC,
        )
        else None,
        "intent": metadata.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "held_reentry_recorded": statement.get(
            "local_relevance_medium_read_only_runtime_held_reentry_recorded"
        )
        is True,
        "basis_runtime_held_reentry_boundary_artifact_preserved": statement.get(
            "basis_runtime_held_reentry_boundary_artifact_preserved"
        )
        is True,
        "basis_runtime_held_state_artifact_preserved": statement.get(
            "basis_runtime_held_state_artifact_preserved"
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
        "selected_command": held_reentry.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved") is True,
        "selected_command_is_state": held_reentry.get("selected_command_is_state") is True,
        "selected_runtime_held_reentry_boundary_recorded": held_reentry.get(
            "selected_runtime_held_reentry_boundary_recorded"
        )
        is True,
        "future_runtime_held_reentry_may_be_considered": held_reentry.get(
            "future_runtime_held_reentry_may_be_considered"
        )
        is True,
        "selected_runtime_held_state_recorded": held_reentry.get(
            "selected_runtime_held_state_recorded"
        )
        is True,
        "runtime_held_state_created": held_reentry.get("runtime_held_state_created")
        is True,
        "runtime_held_state_local_only": held_reentry.get("runtime_held_state_local_only")
        is True,
        "runtime_held_state_read_only": held_reentry.get("runtime_held_state_read_only")
        is True,
        "held_state_basis_reference_only": held_reentry.get("held_state_basis_reference_only")
        is True,
        "raw_state_body_embedded_false_posture": held_reentry.get("raw_state_body_embedded")
        is False,
        "state_mutation_performed_false_posture": held_reentry.get(
            "state_mutation_performed"
        )
        is False,
        "state_update_performed_false_posture": held_reentry.get("state_update_performed")
        is False,
        "selected_runtime_held_state_boundary_recorded": held_reentry.get(
            "selected_runtime_held_state_boundary_recorded"
        )
        is True,
        "future_runtime_held_state_may_be_considered": held_reentry.get(
            "future_runtime_held_state_may_be_considered"
        )
        is True,
        "selected_runtime_recorded": held_reentry.get("selected_runtime_recorded") is True,
        "runtime_created": held_reentry.get("runtime_created") is True,
        "runtime_local_only": held_reentry.get("runtime_local_only") is True,
        "runtime_read_only": held_reentry.get("runtime_read_only") is True,
        "selected_runtime_boundary_recorded": held_reentry.get(
            "selected_runtime_boundary_recorded"
        )
        is True,
        "future_runtime_may_be_considered": held_reentry.get(
            "future_runtime_may_be_considered"
        )
        is True,
        "selected_runtime_permission_recorded": held_reentry.get(
            "selected_runtime_permission_recorded"
        )
        is True,
        "runtime_permission_created": held_reentry.get("runtime_permission_created") is True,
        "runtime_permission_local_only": held_reentry.get("runtime_permission_local_only")
        is True,
        "runtime_permission_read_only": held_reentry.get("runtime_permission_read_only")
        is True,
        "selected_operation_execution_recorded": held_reentry.get(
            "selected_operation_execution_recorded"
        )
        is True,
        "operation_execution_created": held_reentry.get("operation_execution_created")
        is True,
        "operation_execution_performed": held_reentry.get("operation_execution_performed")
        is True,
        "operation_execution_local_only": held_reentry.get("operation_execution_local_only")
        is True,
        "operation_execution_read_only": held_reentry.get("operation_execution_read_only")
        is True,
        "runtime_held_reentry_created": held_reentry.get("runtime_held_reentry_created")
        is True,
        "runtime_held_reentry_local_only": held_reentry.get("runtime_held_reentry_local_only")
        is True,
        "runtime_held_reentry_read_only": held_reentry.get("runtime_held_reentry_read_only")
        is True,
        "held_reentry_basis_reference_only": held_reentry.get(
            "held_reentry_basis_reference_only"
        )
        is True,
        "held_reentry_object_summary": {
            "held_reentry_type": held_reentry.get("held_reentry_type"),
            "held_reentry_scope": held_reentry.get("held_reentry_scope"),
            "held_reentry_version": held_reentry.get("held_reentry_version"),
        },
        "prior_result_reentry_cycle_not_created": held_reentry.get(
            "prior_result_reentry_cycle_created"
        )
        is False,
        "second_operation_not_created": held_reentry.get("second_operation_created")
        is False,
        "continuation_not_created": held_reentry.get("continuation_created") is False,
        "runtime_hosting_not_created": held_reentry.get("runtime_hosting_created") is False,
        "runtime_loop_not_created": held_reentry.get("runtime_loop_created") is False,
        "daemon_behavior_not_created": held_reentry.get("daemon_behavior_created") is False,
        "public_api_not_created": held_reentry.get("public_api_created") is False,
        "participant_facing_interface_not_created": held_reentry.get(
            "participant_facing_interface_created"
        )
        is False,
        "distributed_network_behavior_not_created": held_reentry.get(
            "distributed_network_behavior_created"
        )
        is False,
        "general_operation_permission_not_created": held_reentry.get(
            "general_operation_permission_created"
        )
        is False,
        "general_lookup_permission_not_created": held_reentry.get(
            "general_lookup_permission_created"
        )
        is False,
        "arbitrary_lookup_permission_not_created": held_reentry.get(
            "arbitrary_lookup_permission_created"
        )
        is False,
        "unsupported_commands_not_permitted": held_reentry.get(
            "unsupported_commands_permitted"
        )
        is False,
        "unsupported_lookup_keys_not_permitted": held_reentry.get(
            "unsupported_lookup_keys_permitted"
        )
        is False,
        "new_lookup_entry_not_created": held_reentry.get("new_lookup_entry_created")
        is False,
        "new_signal_entry_relevance_object_index_entry_not_created": all(
            held_reentry.get(key) is False
            for key in (
                "new_signal_accepted",
                "new_entry_accepted",
                "new_relevance_object_created",
                "new_index_entry_created",
            )
        ),
        "filesystem_discovery_not_performed": held_reentry.get(
            "filesystem_discovery_performed"
        )
        is False,
        "registry_search_query_ranking_not_created": all(
            held_reentry.get(key) is False
            for key in (
                "registry_created",
                "search_surface_created",
                "query_surface_created",
                "ranking_surface_created",
            )
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": all(
            held_reentry.get(key) is False
            for key in (
                "scoring_surface_created",
                "priority_surface_created",
                "validity_judgment_created",
                "truth_judgment_created",
                "authority_judgment_created",
                "currentness_judgment_created",
            )
        ),
        "older_runtime_lineage_not_imported_as_authority": held_reentry.get(
            "older_runtime_lineage_imported_as_authority"
        )
        is False,
        "older_runtime_permission_not_treated_as_current": held_reentry.get(
            "older_runtime_permission_treated_as_current"
        )
        is False,
        "runtime_authority_not_imported": held_reentry.get("runtime_authority_imported")
        is False,
        "runtime_v0_failure_evidence_preserved": held_reentry.get(
            "runtime_v0_failure_evidence_preserved"
        )
        is True,
        "runtime_v2_failure_evidence_preserved": held_reentry.get(
            "runtime_v2_failure_evidence_preserved"
        )
        is True,
        "runtime_boundary_v0_failure_evidence_preserved": held_reentry.get(
            "runtime_boundary_v0_failure_evidence_preserved"
        )
        is True,
        "runtime_v0_v2_boundary_v0_failure_not_repaired_hidden_claimed_passed": all(
            non_claims.get(key) is False
            for key in (
                "runtime_v0_failure_repaired",
                "runtime_v0_failure_hidden",
                "runtime_v0_failure_claimed_passed",
                "runtime_v2_failure_repaired",
                "runtime_v2_failure_hidden",
                "runtime_v2_failure_claimed_passed",
                "runtime_boundary_v0_failure_repaired",
                "runtime_boundary_v0_failure_hidden",
                "runtime_boundary_v0_failure_claimed_passed",
            )
        ),
        "repeated_reception_arbitrary_reception_feed_not_created": all(
            held_reentry.get(key) is False
            for key in (
                "repeated_reception_permission_created",
                "arbitrary_reception_created",
                "feed_created",
            )
        ),
        "source_authority_currentness_truth_synchronization_participation_participant_role_not_created": all(
            held_reentry.get(key) is False
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
        )
        is True,
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked")
        is True,
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved"
        )
        is True,
        "follow_on_not_created": held_reentry.get("follow_on_work_authorized") is False,
        "key_non_claims": {
            "prior_result_reentry_cycle_created": non_claims.get(
                "prior_result_reentry_cycle_created"
            ),
            "second_operation_created": non_claims.get("second_operation_created"),
            "continuation_created": non_claims.get("continuation_created"),
            "raw_state_body_embedded": non_claims.get("raw_state_body_embedded"),
            "state_mutation_performed": non_claims.get("state_mutation_performed"),
            "state_update_performed": non_claims.get("state_update_performed"),
            "older_runtime_lineage_imported_as_authority": non_claims.get(
                "older_runtime_lineage_imported_as_authority"
            ),
            "runtime_authority_imported": non_claims.get("runtime_authority_imported"),
            "consumed_request_reopened": non_claims.get("consumed_request_reopened"),
            "authorization_token_reused": non_claims.get("authorization_token_reused"),
        },
        "result_level_non_claims_canonical_false": canonical_false,
    }
    return _sanitize(summary)


def write_local_relevance_medium_read_only_runtime_held_reentry_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result without overwriting an existing artifact."""

    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyRuntimeHeldReentryV0MinError(
            "result must be a mapping"
        )
    if output_path is None:
        metadata = result.get(
            "local_relevance_medium_read_only_runtime_held_reentry_metadata", {}
        )
        if not isinstance(metadata, MappingABC):
            metadata = {}
        held_reentry_id = str(
            metadata.get("local_relevance_medium_read_only_runtime_held_reentry_id")
            or DEFAULT_HELD_REENTRY_ID
        )
        target = OUTPUT_ROOT / (
            f"{held_reentry_id}__local_relevance_medium_read_only_runtime_held_reentry_v0_min_result.json"
        )
    else:
        target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    candidate = target
    if candidate.exists():
        stem = target.stem
        suffix = target.suffix
        for index in range(1, 1000):
            candidate = target.with_name(f"{stem}_{index:03d}{suffix}")
            if not candidate.exists():
                break
        else:
            raise LocalRelevanceMediumReadOnlyRuntimeHeldReentryV0MinError(
                "could not allocate non-overwriting output path"
            )
    candidate.write_text(
        json.dumps(_sanitize(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return candidate
