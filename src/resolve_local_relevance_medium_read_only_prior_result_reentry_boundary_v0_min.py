"""Resolve one local read-only prior-result re-entry boundary.

This resolver records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY object only. It
reads one clean runtime-held-re-entry artifact, one clean runtime-held-re-entry
boundary artifact, one clean runtime-held-state artifact, one clean
runtime-held-state boundary artifact, one clean runtime v3 artifact, one clean
runtime boundary v2 artifact, one clean runtime permission artifact, and one
clean operation execution artifact as basis references.

The boundary is local, read-only, selected-prior-result-reentry-consideration-
only, raw-state-body-excluding, state-mutation-refusing, state-update-refusing,
closure-token-aware, non-cycle-shaped, non-second-operation-shaped,
non-continuation-shaped, non-hosting-shaped, non-loop-shaped, non-daemon-shaped,
and older-runtime-authority-import-blocking.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyPriorResultReentryBoundaryV0MinError(
    RuntimeError
):
    """Bounded resolver error for prior-result re-entry boundary handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min"
)

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_BLOCKED"
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
    "prior_result_reentry_boundary_v0_min"
)

DEFAULT_BOUNDARY_ID = "local_relevance_medium_read_only_prior_result_reentry_boundary_001"
BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_PRIOR_RESULT_REENTRY_CONSIDERATION_ONLY"
SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)
SELECTED_COMMAND = "state"

INTENT_RECORD = (
    "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_RUNTIME_HELD_REENTRY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_held_reentry_v0_min/"
    "local_relevance_medium_read_only_runtime_held_reentry_reference_review_001__"
    "local_relevance_medium_read_only_runtime_held_reentry_v0_min_result.json"
)
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

EXPECTED_RUNTIME_HELD_REENTRY_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_RECORDED"
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

BOUNDARY_OBJECT_FALSE_FIELDS = (
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
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
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
    "artifact_existence_treated_as_prior_result_reentry_boundary_authority",
    "latest_file_posture_treated_as_prior_result_reentry_boundary_authority",
    "repo_local_availability_treated_as_prior_result_reentry_boundary_authority",
    "hidden_repo_state_used_as_prior_result_reentry_boundary_content",
    "hidden_repo_state_used_as_prior_result_reentry_boundary_authority",
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
)
REQUIRED_FALSE_NON_CLAIMS = BOUNDARY_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded",
    "basis_runtime_held_reentry_artifact_preserved",
    "basis_runtime_held_reentry_boundary_artifact_preserved",
    "basis_runtime_held_state_artifact_preserved",
    "basis_runtime_held_state_boundary_artifact_preserved",
    "basis_runtime_artifact_preserved",
    "basis_runtime_boundary_artifact_preserved",
    "basis_runtime_permission_artifact_preserved",
    "basis_operation_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_runtime_held_reentry_recorded",
    "runtime_held_reentry_created",
    "runtime_held_reentry_local_only",
    "runtime_held_reentry_read_only",
    "held_reentry_basis_reference_only",
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
    "future_prior_result_reentry_cycle_may_be_considered",
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
    "runtime_held_reentry_artifact_missing": "RUNTIME_HELD_REENTRY_ARTIFACT_PATH_MISSING",
    "runtime_held_reentry_artifact_not_recorded": "RUNTIME_HELD_REENTRY_ARTIFACT_NOT_RECORDED",
    "runtime_held_reentry_artifact_failed_checks_present": "RUNTIME_HELD_REENTRY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_held_reentry_artifact_version_not_0_1_0": "RUNTIME_HELD_REENTRY_ARTIFACT_VERSION_NOT_0_1_0",
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
    "selected_runtime_held_reentry_not_recorded": "SELECTED_RUNTIME_HELD_REENTRY_NOT_RECORDED",
    "runtime_held_reentry_not_created": "RUNTIME_HELD_REENTRY_NOT_CREATED",
    "runtime_held_reentry_local_only_not_true": "RUNTIME_HELD_REENTRY_LOCAL_ONLY_NOT_TRUE",
    "runtime_held_reentry_read_only_not_true": "RUNTIME_HELD_REENTRY_READ_ONLY_NOT_TRUE",
    "held_reentry_basis_reference_only_not_true": "HELD_REENTRY_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "selected_runtime_held_reentry_boundary_not_recorded": "SELECTED_RUNTIME_HELD_REENTRY_BOUNDARY_NOT_RECORDED",
    "future_runtime_held_reentry_may_not_be_considered": "FUTURE_RUNTIME_HELD_REENTRY_MAY_NOT_BE_CONSIDERED",
    "selected_runtime_held_state_not_recorded": "SELECTED_RUNTIME_HELD_STATE_NOT_RECORDED",
    "runtime_held_state_not_created": "RUNTIME_HELD_STATE_NOT_CREATED",
    "runtime_held_state_local_only_not_true": "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE",
    "runtime_held_state_read_only_not_true": "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE",
    "held_state_basis_reference_only_not_true": "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE",
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
    "future_prior_result_reentry_cycle_may_not_be_considered": "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED",
    "boundary_type_not_local_relevance_medium_read_only_prior_result_reentry_boundary": "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY",
    "boundary_scope_not_selected_prior_result_reentry_consideration_only": "BOUNDARY_SCOPE_NOT_SELECTED_PRIOR_RESULT_REENTRY_CONSIDERATION_ONLY",
    "raw_state_body_embedded": "RAW_STATE_BODY_EMBEDDED",
    "state_mutation_performed": "STATE_MUTATION_PERFORMED",
    "state_update_performed": "STATE_UPDATE_PERFORMED",
}

BASE_BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_BLOCK_REQUESTED",
    "RUNTIME_HELD_REENTRY_ARTIFACT_PATH_MISSING",
    "RUNTIME_HELD_REENTRY_ARTIFACT_UNREADABLE",
    "RUNTIME_HELD_REENTRY_ARTIFACT_NOT_JSON_OBJECT",
    "RUNTIME_HELD_REENTRY_ARTIFACT_NOT_RECORDED",
    "RUNTIME_HELD_REENTRY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "RUNTIME_HELD_REENTRY_ARTIFACT_VERSION_NOT_0_1_0",
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
    "SELECTED_RUNTIME_HELD_REENTRY_NOT_RECORDED",
    "RUNTIME_HELD_REENTRY_NOT_CREATED",
    "RUNTIME_HELD_REENTRY_LOCAL_ONLY_NOT_TRUE",
    "RUNTIME_HELD_REENTRY_READ_ONLY_NOT_TRUE",
    "HELD_REENTRY_BASIS_REFERENCE_ONLY_NOT_TRUE",
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
    "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_SELECTED_PRIOR_RESULT_REENTRY_CONSIDERATION_ONLY",
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
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "ARTIFACT_EXISTENCE_TREATED_AS_PRIOR_RESULT_REENTRY_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_PRIOR_RESULT_REENTRY_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_PRIOR_RESULT_REENTRY_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_PRIOR_RESULT_REENTRY_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_PRIOR_RESULT_REENTRY_BOUNDARY_AUTHORITY",
    "PRIOR_ARTIFACTS_MUTATED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_REQUEST_UNREADABLE",
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
    "raw_prior_result_reentry_boundary_body",
    "raw_prior_result_reentry_body",
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
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "prior_result_reentry_boundary_body",
    "prior_result_reentry_body",
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
    "RAW_PRIOR_RESULT_REENTRY_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_PRIOR_RESULT_REENTRY_BODY_MUST_NOT_RETURN",
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
        "name": "runtime_held_reentry",
        "path_key": "selected_runtime_held_reentry_artifact",
        "basis_key": "selected_runtime_held_reentry_artifact_basis",
        "label": "runtime-held-re-entry artifact",
        "prefix": "RUNTIME_HELD_REENTRY_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_HELD_REENTRY_OUTCOME,
        "default_path": DEFAULT_RUNTIME_HELD_REENTRY_ARTIFACT,
        "object_prefix": "basis_runtime_held_reentry",
    },
    {
        "name": "runtime_held_reentry_boundary",
        "path_key": "selected_runtime_held_reentry_boundary_artifact",
        "basis_key": "selected_runtime_held_reentry_boundary_artifact_basis",
        "label": "runtime-held-re-entry boundary artifact",
        "prefix": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME,
        "default_path": DEFAULT_RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT,
        "object_prefix": "basis_runtime_held_reentry_boundary",
    },
    {
        "name": "runtime_held_state",
        "path_key": "selected_runtime_held_state_artifact",
        "basis_key": "selected_runtime_held_state_artifact_basis",
        "label": "runtime-held-state artifact",
        "prefix": "RUNTIME_HELD_STATE_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_HELD_STATE_OUTCOME,
        "default_path": DEFAULT_RUNTIME_HELD_STATE_ARTIFACT,
        "object_prefix": "basis_runtime_held_state",
    },
    {
        "name": "runtime_held_state_boundary",
        "path_key": "selected_runtime_held_state_boundary_artifact",
        "basis_key": "selected_runtime_held_state_boundary_artifact_basis",
        "label": "runtime-held-state boundary artifact",
        "prefix": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_HELD_STATE_BOUNDARY_OUTCOME,
        "default_path": DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT,
        "object_prefix": "basis_runtime_held_state_boundary",
    },
    {
        "name": "runtime",
        "path_key": "selected_runtime_artifact",
        "basis_key": "selected_runtime_artifact_basis",
        "label": "runtime artifact",
        "prefix": "RUNTIME_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_OUTCOME,
        "default_path": DEFAULT_RUNTIME_ARTIFACT,
        "object_prefix": "basis_runtime",
    },
    {
        "name": "runtime_boundary",
        "path_key": "selected_runtime_boundary_artifact",
        "basis_key": "selected_runtime_boundary_artifact_basis",
        "label": "runtime boundary artifact",
        "prefix": "RUNTIME_BOUNDARY_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        "default_path": DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
        "object_prefix": "basis_runtime_boundary",
    },
    {
        "name": "runtime_permission",
        "path_key": "selected_runtime_permission_artifact",
        "basis_key": "selected_runtime_permission_artifact_basis",
        "label": "runtime permission artifact",
        "prefix": "RUNTIME_PERMISSION_ARTIFACT",
        "expected_outcome": EXPECTED_RUNTIME_PERMISSION_OUTCOME,
        "default_path": DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
        "object_prefix": "basis_runtime_permission",
    },
    {
        "name": "operation_execution",
        "path_key": "selected_operation_execution_artifact",
        "basis_key": "selected_operation_execution_artifact_basis",
        "label": "operation execution artifact",
        "prefix": "OPERATION_EXECUTION_ARTIFACT",
        "expected_outcome": EXPECTED_OPERATION_EXECUTION_OUTCOME,
        "default_path": DEFAULT_OPERATION_EXECUTION_ARTIFACT,
        "object_prefix": "basis_operation_execution",
    },
)

FIELD_ALIASES = {
    "selected_runtime_held_reentry_recorded": (
        "selected_runtime_held_reentry_recorded",
        "local_relevance_medium_read_only_runtime_held_reentry_recorded",
    ),
    "selected_runtime_held_reentry_boundary_recorded": (
        "selected_runtime_held_reentry_boundary_recorded",
        "local_relevance_medium_read_only_runtime_held_reentry_boundary_recorded",
    ),
    "selected_runtime_held_state_recorded": (
        "selected_runtime_held_state_recorded",
        "local_relevance_medium_read_only_runtime_held_state_recorded",
    ),
    "selected_runtime_held_state_boundary_recorded": (
        "selected_runtime_held_state_boundary_recorded",
        "local_relevance_medium_read_only_runtime_held_state_boundary_recorded",
    ),
    "selected_runtime_recorded": (
        "selected_runtime_recorded",
        "local_relevance_medium_read_only_runtime_recorded",
    ),
    "selected_runtime_boundary_recorded": (
        "selected_runtime_boundary_recorded",
        "local_relevance_medium_read_only_runtime_boundary_recorded",
    ),
    "selected_runtime_permission_recorded": (
        "selected_runtime_permission_recorded",
        "local_relevance_medium_read_only_runtime_permission_recorded",
    ),
    "selected_operation_execution_recorded": (
        "selected_operation_execution_recorded",
        "local_relevance_medium_read_only_operation_execution_recorded",
    ),
}

TRUE_FIELD_DEFAULT_BASIS = {
    "selected_runtime_held_reentry_recorded": "runtime_held_reentry",
    "runtime_held_reentry_created": "runtime_held_reentry",
    "runtime_held_reentry_local_only": "runtime_held_reentry",
    "runtime_held_reentry_read_only": "runtime_held_reentry",
    "held_reentry_basis_reference_only": "runtime_held_reentry",
    "selected_runtime_held_reentry_boundary_recorded": "runtime_held_reentry_boundary",
    "future_runtime_held_reentry_may_be_considered": "runtime_held_reentry_boundary",
    "selected_runtime_held_state_recorded": "runtime_held_state",
    "runtime_held_state_created": "runtime_held_state",
    "runtime_held_state_local_only": "runtime_held_state",
    "runtime_held_state_read_only": "runtime_held_state",
    "held_state_basis_reference_only": "runtime_held_state",
    "selected_runtime_held_state_boundary_recorded": "runtime_held_state_boundary",
    "future_runtime_held_state_may_be_considered": "runtime_held_state_boundary",
    "selected_runtime_recorded": "runtime",
    "runtime_created": "runtime",
    "runtime_local_only": "runtime",
    "runtime_read_only": "runtime",
    "selected_runtime_boundary_recorded": "runtime_boundary",
    "future_runtime_may_be_considered": "runtime_boundary",
    "selected_runtime_permission_recorded": "runtime_permission",
    "runtime_permission_created": "runtime_permission",
    "runtime_permission_local_only": "runtime_permission",
    "runtime_permission_read_only": "runtime_permission",
    "selected_operation_execution_recorded": "operation_execution",
    "operation_execution_created": "operation_execution",
    "operation_execution_performed": "operation_execution",
    "operation_execution_local_only": "operation_execution",
    "operation_execution_read_only": "operation_execution",
}

BOUNDARY_TRUE_FIELDS = (
    "selected_runtime_held_reentry_recorded",
    "runtime_held_reentry_created",
    "runtime_held_reentry_local_only",
    "runtime_held_reentry_read_only",
    "held_reentry_basis_reference_only",
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
    "future_prior_result_reentry_cycle_may_be_considered",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY for selected command state, "
    "one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME, one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY, "
    "one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION, existing reusable read-only lookup permission, "
    "prior lookup-pair coverage, and prior local carrier command surface, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY be recorded that permits a future "
    "local read-only prior-result re-entry cycle to be considered as a separately bounded step, without "
    "creating prior-result re-entry cycle, creating second operation, creating continuation, creating "
    "runtime hosting, creating runtime loop, creating daemon behavior, creating public API, creating "
    "participant-facing interface, creating distributed network behavior, creating general operation "
    "permission, creating general lookup permission, creating arbitrary lookup permission, permitting "
    "unsupported commands, permitting unsupported lookup keys, creating new lookup entry beyond the "
    "already bounded selected-state lookup result object, embedding raw state body, mutating state, "
    "updating state, accepting new entries, accepting new signals, performing filesystem discovery, "
    "importing older runtime/post-runtime authority, creating query surface, registry, search, ranking, "
    "scoring, priority, validity judgment, truth judgment, authority, currentness, synchronization, "
    "participation authorization, participant role, repeated reception permission, arbitrary reception, "
    "feed, source transfer, source receipt, or follow-on work?"
)

WHAT_REMAINS_OPEN = (
    "local relevance medium read-only prior-result re-entry boundary test",
    "local relevance medium read-only prior-result re-entry boundary live artifact",
    "local relevance medium read-only prior-result re-entry boundary terminal summary",
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
            else "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_REQUEST_MALFORMED"
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


def _basis_clean_by_name(
    artifact_bases: Mapping[str, Mapping[str, Any]], name: str
) -> bool:
    for spec in ARTIFACT_SPECS:
        if spec["name"] == name:
            basis = artifact_bases.get(str(spec["basis_key"]), {})
            return basis.get("artifact_preserved") is True
    return False


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


def _value_from_sources(
    field: str,
    request: Mapping[str, Any],
    artifacts: Mapping[str, Mapping[str, Any] | None],
    artifact_bases: Mapping[str, Mapping[str, Any]],
    default: Any = None,
) -> Any:
    key_names = FIELD_ALIASES.get(field, (field,))
    for key in key_names:
        if key in request:
            return request[key]
    for artifact in artifacts.values():
        found = _find_first_key(artifact, key_names)
        if found is not None:
            return found
    if field == "future_prior_result_reentry_cycle_may_be_considered":
        if request.get("future_prior_result_reentry_cycle_may_not_be_considered") is True:
            return False
        return True
    if field in (
        "runtime_v0_failure_evidence_preserved",
        "runtime_v2_failure_evidence_preserved",
        "runtime_boundary_v0_failure_evidence_preserved",
    ):
        return True
    basis_name = TRUE_FIELD_DEFAULT_BASIS.get(field)
    if basis_name is not None and _basis_clean_by_name(artifact_bases, basis_name):
        return True
    return default


def _check_bool_true(
    checks: list[dict[str, Any]],
    name: str,
    field: str,
    code: str,
    request: Mapping[str, Any],
    artifacts: Mapping[str, Mapping[str, Any] | None],
    artifact_bases: Mapping[str, Mapping[str, Any]],
) -> bool:
    actual = _value_from_sources(field, request, artifacts, artifact_bases, default=None)
    passed = actual is True
    checks.append(_new_check(name, passed, True, actual, code))
    return passed


def _check_bool_false(
    checks: list[dict[str, Any]],
    name: str,
    field: str,
    code: str,
    request: Mapping[str, Any],
    artifacts: Mapping[str, Mapping[str, Any] | None],
) -> bool:
    actual = _value_from_sources(field, request, artifacts, {}, default=False)
    passed = actual is False
    checks.append(_new_check(name, passed, False, actual, code))
    return passed


def _validate_declared_non_claims(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    declared = request.get("declared_non_claims")
    is_mapping = isinstance(declared, MappingABC)
    checks.append(
        _new_check(
            "declared non-claims mapping present",
            is_mapping,
            "mapping with required false non-claims",
            type(declared).__name__ if declared is not None else None,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    if not is_mapping:
        return
    for key in REQUIRED_FALSE_NON_CLAIMS:
        value = declared.get(key)
        checks.append(
            _new_check(
                f"declared non-claim {key} is false bool",
                value is False,
                False,
                value,
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )
        )


def _validate_top_level_false_posture(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    for field, code in TOP_LEVEL_BLOCK_FIELD_CODES.items():
        if request.get(field) is True:
            checks.append(
                _new_check(
                    f"top-level {field} remains false",
                    False,
                    False,
                    True,
                    code,
                )
            )
    for field, code in SHORTCUT_BLOCK_FIELD_CODES.items():
        if request.get(field) is True:
            checks.append(
                _new_check(
                    f"shortcut {field} remains false",
                    False,
                    False,
                    True,
                    code,
                )
            )


def _validate_declared_request(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    question = request.get(
        "local_relevance_medium_read_only_prior_result_reentry_boundary_question"
    )
    checks.append(
        _new_check(
            "prior-result re-entry boundary question declared",
            isinstance(question, str) and bool(question.strip()),
            "declared prior-result re-entry boundary question",
            question,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_QUESTION_UNDECLARED",
        )
    )

    intent = request.get(
        "local_relevance_medium_read_only_prior_result_reentry_boundary_intent",
        INTENT_RECORD,
    )
    checks.append(
        _new_check(
            "boundary intent supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_INTENT_UNSUPPORTED",
        )
    )
    if intent == INTENT_BLOCK:
        checks.append(
            _new_check(
                "explicit prior-result re-entry boundary block request absent",
                False,
                "no block request",
                intent,
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_BLOCK_REQUESTED",
            )
        )

    selected_command = request.get("selected_command")
    checks.append(
        _new_check(
            "selected command declared",
            selected_command not in (None, ""),
            "declared selected command",
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

    boundary_type = request.get("boundary_type")
    checks.append(
        _new_check(
            "boundary type declared",
            boundary_type not in (None, ""),
            BOUNDARY_TYPE,
            boundary_type,
            "BOUNDARY_TYPE_MISSING",
        )
    )
    checks.append(
        _new_check(
            "boundary type exact",
            boundary_type == BOUNDARY_TYPE,
            BOUNDARY_TYPE,
            boundary_type,
            "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY",
        )
    )

    boundary_scope = request.get("boundary_scope")
    checks.append(
        _new_check(
            "boundary scope declared",
            boundary_scope not in (None, ""),
            BOUNDARY_SCOPE,
            boundary_scope,
            "BOUNDARY_SCOPE_MISSING",
        )
    )
    checks.append(
        _new_check(
            "boundary scope exact",
            boundary_scope == BOUNDARY_SCOPE,
            BOUNDARY_SCOPE,
            boundary_scope,
            "BOUNDARY_SCOPE_NOT_SELECTED_PRIOR_RESULT_REENTRY_CONSIDERATION_ONLY",
        )
    )

    _validate_top_level_false_posture(request, checks)
    _validate_declared_non_claims(request, checks)


def _build_boundary_object(
    request: Mapping[str, Any],
    artifact_bases: Mapping[str, Mapping[str, Any]],
    artifacts: Mapping[str, Mapping[str, Any] | None],
) -> dict[str, Any]:
    boundary_id = request.get(
        "local_relevance_medium_read_only_prior_result_reentry_boundary_id",
        DEFAULT_BOUNDARY_ID,
    )
    boundary: dict[str, Any] = {
        "boundary_id": str(boundary_id or DEFAULT_BOUNDARY_ID),
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
    }
    for spec in ARTIFACT_SPECS:
        basis = artifact_bases.get(str(spec["basis_key"]), {})
        prefix = str(spec["object_prefix"])
        boundary[f"{prefix}_artifact"] = basis.get("artifact_path")
        boundary[f"{prefix}_outcome"] = basis.get("outcome")
        boundary[f"{prefix}_result_version"] = basis.get("result_version")
        boundary[f"{prefix}_failed_check_count"] = basis.get("failed_check_count")

    boundary["selected_command"] = request.get("selected_command", SELECTED_COMMAND)
    boundary["selected_command_is_state"] = boundary["selected_command"] == SELECTED_COMMAND
    for field in BOUNDARY_TRUE_FIELDS:
        if field == "selected_command_is_state":
            continue
        boundary[field] = bool(
            _value_from_sources(field, request, artifacts, artifact_bases, default=False)
        )
    for field in BOUNDARY_OBJECT_FALSE_FIELDS:
        boundary[field] = False
    return _sanitize(boundary)


def _build_statement(
    outcome: str,
    boundary: Mapping[str, Any],
    artifact_bases: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement: dict[str, Any] = {
        "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded": recorded,
        "basis_runtime_held_reentry_artifact_preserved": artifact_bases[
            "selected_runtime_held_reentry_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_runtime_held_reentry_boundary_artifact_preserved": artifact_bases[
            "selected_runtime_held_reentry_boundary_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_runtime_held_state_artifact_preserved": artifact_bases[
            "selected_runtime_held_state_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_runtime_held_state_boundary_artifact_preserved": artifact_bases[
            "selected_runtime_held_state_boundary_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_runtime_artifact_preserved": artifact_bases[
            "selected_runtime_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_runtime_boundary_artifact_preserved": artifact_bases[
            "selected_runtime_boundary_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_runtime_permission_artifact_preserved": artifact_bases[
            "selected_runtime_permission_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "basis_operation_execution_artifact_preserved": artifact_bases[
            "selected_operation_execution_artifact_basis"
        ].get("artifact_preserved")
        is True,
        "selected_command_preserved": boundary.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": boundary.get("selected_command_is_state") is True,
        "consumed_request_token_remains_closed": boundary.get("consumed_request_reopened")
        is False,
        "authorization_token_reuse_blocked": boundary.get("authorization_token_reused")
        is False,
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }
    for field in BOUNDARY_TRUE_FIELDS:
        statement[field] = boundary.get(field) is True
    for field in BOUNDARY_OBJECT_FALSE_FIELDS:
        statement[field] = boundary.get(field) is False
    statement["runtime_v0_failure_not_repaired"] = True
    statement["runtime_v0_failure_not_hidden"] = True
    statement["runtime_v0_failure_not_claimed_passed"] = True
    statement["runtime_v2_failure_not_repaired"] = True
    statement["runtime_v2_failure_not_hidden"] = True
    statement["runtime_v2_failure_not_claimed_passed"] = True
    statement["runtime_boundary_v0_failure_not_repaired"] = True
    statement["runtime_boundary_v0_failure_not_hidden"] = True
    statement["runtime_boundary_v0_failure_not_claimed_passed"] = True
    return statement


def _build_non_meaning() -> dict[str, bool]:
    return {
        "prior_result_reentry_cycle_created": False,
        "second_operation_created": False,
        "continuation_created": False,
        "runtime_hosting_created": False,
        "runtime_loop_created": False,
        "daemon_behavior_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "general_operation_permission_created": False,
        "general_lookup_permission_created": False,
        "arbitrary_lookup_permission_created": False,
        "unsupported_commands_permitted": False,
        "unsupported_lookup_keys_permitted": False,
        "query_surface_created": False,
        "registry_created": False,
        "search_surface_created": False,
        "ranking_surface_created": False,
        "older_runtime_lineage_imported_as_authority": False,
        "runtime_authority_imported": False,
        "follow_on_work_authorized": False,
    }


def _validate_boundary_posture(
    request: Mapping[str, Any],
    artifacts: Mapping[str, Mapping[str, Any] | None],
    artifact_bases: Mapping[str, Mapping[str, Any]],
    checks: list[dict[str, Any]],
) -> None:
    true_checks = {
        "selected_runtime_held_reentry_recorded": "SELECTED_RUNTIME_HELD_REENTRY_NOT_RECORDED",
        "runtime_held_reentry_created": "RUNTIME_HELD_REENTRY_NOT_CREATED",
        "runtime_held_reentry_local_only": "RUNTIME_HELD_REENTRY_LOCAL_ONLY_NOT_TRUE",
        "runtime_held_reentry_read_only": "RUNTIME_HELD_REENTRY_READ_ONLY_NOT_TRUE",
        "held_reentry_basis_reference_only": "HELD_REENTRY_BASIS_REFERENCE_ONLY_NOT_TRUE",
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
        "future_prior_result_reentry_cycle_may_be_considered": "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED",
        "runtime_v0_failure_evidence_preserved": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "runtime_v2_failure_evidence_preserved": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "runtime_boundary_v0_failure_evidence_preserved": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    }
    for field, code in true_checks.items():
        _check_bool_true(
            checks,
            field.replace("_", " "),
            field,
            code,
            request,
            artifacts,
            artifact_bases,
        )

    false_codes = {
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
    for field in REQUIRED_FALSE_NON_CLAIMS:
        code = false_codes.get(field, TOP_LEVEL_BLOCK_FIELD_CODES.get(field, field.upper()))
        _check_bool_false(
            checks,
            f"{field} remains false",
            field,
            code,
            request,
            artifacts,
        )

    canonical = _canonical_non_claims()
    checks.append(
        _new_check(
            "result-level required false non-claims canonical false",
            all(value is False for value in canonical.values()),
            "all required result-level non-claims false bool",
            canonical,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )


def _minimal_request_mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, MappingABC) else {}


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    artifact_bases: Mapping[str, Mapping[str, Any]] | None = None,
    artifacts: Mapping[str, Mapping[str, Any] | None] | None = None,
) -> dict[str, Any]:
    request_map = _minimal_request_mapping(request)
    basis_map = dict(artifact_bases or _basis_map_with_defaults())
    artifact_map = dict(artifacts or {})
    failed_check_count = sum(1 for check in checks if check.get("passed") is not True)
    first_code = _first_failed_code(checks)
    intent = request_map.get(
        "local_relevance_medium_read_only_prior_result_reentry_boundary_intent",
        INTENT_RECORD,
    )
    if failed_check_count:
        outcome = OUTCOME_BLOCKED
    elif request_map.get("additional_basis_context"):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif intent == INTENT_DO_NOT_RECORD or request_map.get("not_recorded_basis"):
        outcome = OUTCOME_NOT_RECORDED
    else:
        outcome = OUTCOME_RECORDED

    boundary = _build_boundary_object(request_map, basis_map, artifact_map)
    statement = _build_statement(outcome, boundary, basis_map)
    metadata = {
        "local_relevance_medium_read_only_prior_result_reentry_boundary_id": boundary[
            "boundary_id"
        ],
        "local_relevance_medium_read_only_prior_result_reentry_boundary_type": BOUNDARY_TYPE,
        "local_relevance_medium_read_only_prior_result_reentry_boundary_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_prior_result_reentry_boundary_metadata": metadata,
        "declared_local_relevance_medium_read_only_prior_result_reentry_boundary_question": {
            "question": _sanitize(
                request_map.get(
                    "local_relevance_medium_read_only_prior_result_reentry_boundary_question"
                )
            ),
            "intent": _sanitize(intent),
            "boundary_type": _sanitize(request_map.get("boundary_type")),
            "boundary_scope": _sanitize(request_map.get("boundary_scope")),
            "selected_command": _sanitize(request_map.get("selected_command")),
        },
        **basis_map,
        "local_relevance_medium_read_only_prior_result_reentry_boundary": boundary,
        "local_relevance_medium_read_only_prior_result_reentry_boundary_checks": checks,
        "local_relevance_medium_read_only_prior_result_reentry_boundary_statement": statement,
        "local_relevance_medium_read_only_prior_result_reentry_boundary_non_meaning": _build_non_meaning(),
        "additional_basis_required": _sanitize(
            request_map.get("additional_basis_context", [])
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else []
        ),
        "not_recorded_basis": _sanitize(
            request_map.get("not_recorded_basis", [])
            if outcome == OUTCOME_NOT_RECORDED
            else []
        ),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": _block_dict(first_code, first_code),
    }
    result["local_relevance_medium_read_only_prior_result_reentry_boundary_summary"] = (
        build_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_summary(
            result
        )
    )
    return _sanitize(result)


def _bad_request_result(code: str, reason: Any) -> dict[str, Any]:
    checks = [
        _new_check(
            "declared prior-result re-entry boundary request readable mapping",
            False,
            "readable JSON mapping request",
            reason,
            code,
        )
    ]
    return _build_result({}, checks)


def resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(
    declared_local_relevance_medium_read_only_prior_result_reentry_boundary: Mapping[str, Any]
    | None = None,
) -> dict[str, Any]:
    """Resolve one local read-only prior-result re-entry boundary request."""

    if declared_local_relevance_medium_read_only_prior_result_reentry_boundary is None:
        request = (
            build_declared_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_request()
        )
    elif not isinstance(
        declared_local_relevance_medium_read_only_prior_result_reentry_boundary,
        MappingABC,
    ):
        return _bad_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_REQUEST_MALFORMED",
            type(
                declared_local_relevance_medium_read_only_prior_result_reentry_boundary
            ).__name__,
        )
    else:
        request = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_prior_result_reentry_boundary)
        )

    checks: list[dict[str, Any]] = []
    _validate_declared_request(request, checks)

    artifact_bases: dict[str, dict[str, Any]] = {}
    artifacts: dict[str, dict[str, Any] | None] = {}
    for spec in ARTIFACT_SPECS:
        basis, artifact = _validate_basis_artifact(request, spec, checks)
        artifact_bases[str(spec["basis_key"])] = basis
        artifacts[str(spec["name"])] = artifact

    _validate_boundary_posture(request, artifacts, artifact_bases, checks)
    return _build_result(request, checks, artifact_bases, artifacts)


def resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_from_path(
    declared_local_relevance_medium_read_only_prior_result_reentry_boundary_path: Path | str,
) -> dict[str, Any]:
    """Read a declared request JSON object from path and resolve it."""

    try:
        loaded = json.loads(
            Path(
                declared_local_relevance_medium_read_only_prior_result_reentry_boundary_path
            ).read_text(encoding="utf-8")
        )
    except Exception as exc:  # noqa: BLE001 - converted to bounded public result.
        return _bad_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_REQUEST_UNREADABLE",
            f"{exc.__class__.__name__}: {exc}",
        )
    if not isinstance(loaded, MappingABC):
        return _bad_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_REQUEST_MALFORMED",
            type(loaded).__name__,
        )
    return resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(
        loaded
    )


def build_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary for a resolver result."""

    checks = result.get("local_relevance_medium_read_only_prior_result_reentry_boundary_checks")
    if not isinstance(checks, list):
        checks = []
    failed_check_count = sum(
        1 for check in checks if isinstance(check, MappingABC) and check.get("passed") is not True
    )
    passed_check_count = sum(
        1 for check in checks if isinstance(check, MappingABC) and check.get("passed") is True
    )
    boundary = result.get("local_relevance_medium_read_only_prior_result_reentry_boundary")
    if not isinstance(boundary, MappingABC):
        boundary = {}
    statement = result.get(
        "local_relevance_medium_read_only_prior_result_reentry_boundary_statement"
    )
    if not isinstance(statement, MappingABC):
        statement = {}
    metadata = result.get(
        "local_relevance_medium_read_only_prior_result_reentry_boundary_metadata"
    )
    if not isinstance(metadata, MappingABC):
        metadata = {}
    block = result.get("block")
    if not isinstance(block, MappingABC):
        block = {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "boundary_id": boundary.get("boundary_id")
        or metadata.get("local_relevance_medium_read_only_prior_result_reentry_boundary_id"),
        "question": result.get(
            "declared_local_relevance_medium_read_only_prior_result_reentry_boundary_question",
            {},
        ).get("question")
        if isinstance(
            result.get(
                "declared_local_relevance_medium_read_only_prior_result_reentry_boundary_question"
            ),
            MappingABC,
        )
        else None,
        "intent": result.get(
            "declared_local_relevance_medium_read_only_prior_result_reentry_boundary_question",
            {},
        ).get("intent")
        if isinstance(
            result.get(
                "declared_local_relevance_medium_read_only_prior_result_reentry_boundary_question"
            ),
            MappingABC,
        )
        else None,
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": metadata.get("result_version") or RESULT_VERSION,
        "resolver_module": metadata.get("resolver_module") or RESOLVER_MODULE,
        "boundary_recorded": result.get("outcome") == OUTCOME_RECORDED,
        "boundary_object_summary": {
            "boundary_type": boundary.get("boundary_type"),
            "boundary_scope": boundary.get("boundary_scope"),
            "boundary_version": boundary.get("boundary_version"),
        },
        "key_non_claims": result.get("non_claims", {}),
    }
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[field] = statement.get(field)
    for field in BOUNDARY_OBJECT_FALSE_FIELDS:
        if field in boundary:
            summary[field] = boundary.get(field)
    summary["prior_result_reentry_cycle_not_created"] = (
        boundary.get("prior_result_reentry_cycle_created") is False
    )
    summary["second_operation_not_created"] = (
        boundary.get("second_operation_created") is False
    )
    summary["continuation_not_created"] = boundary.get("continuation_created") is False
    summary["runtime_hosting_not_created"] = (
        boundary.get("runtime_hosting_created") is False
    )
    summary["runtime_loop_not_created"] = boundary.get("runtime_loop_created") is False
    summary["daemon_behavior_not_created"] = (
        boundary.get("daemon_behavior_created") is False
    )
    summary["public_api_not_created"] = boundary.get("public_api_created") is False
    summary["participant_facing_interface_not_created"] = (
        boundary.get("participant_facing_interface_created") is False
    )
    summary["distributed_network_behavior_not_created"] = (
        boundary.get("distributed_network_behavior_created") is False
    )
    summary["older_runtime_lineage_not_imported_as_authority"] = (
        boundary.get("older_runtime_lineage_imported_as_authority") is False
    )
    summary["older_runtime_permission_not_treated_as_current"] = (
        boundary.get("older_runtime_permission_treated_as_current") is False
    )
    summary["runtime_authority_not_imported"] = (
        boundary.get("runtime_authority_imported") is False
    )
    summary["raw_state_body_not_embedded"] = (
        boundary.get("raw_state_body_embedded") is False
    )
    summary["state_mutation_not_performed"] = (
        boundary.get("state_mutation_performed") is False
    )
    summary["state_update_not_performed"] = (
        boundary.get("state_update_performed") is False
    )
    summary["follow_on_not_created"] = (
        boundary.get("follow_on_work_authorized") is False
    )
    summary["result_level_non_claims_canonical_false"] = all(
        value is False
        for value in (result.get("non_claims") or {}).values()
    )
    return _sanitize(summary)


def write_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result as stable UTF-8 JSON without overwriting."""

    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyPriorResultReentryBoundaryV0MinError(
            "result must be a mapping"
        )
    result_copy = _sanitize(copy.deepcopy(dict(result)))
    if output_path is None:
        metadata = result_copy.get(
            "local_relevance_medium_read_only_prior_result_reentry_boundary_metadata",
            {},
        )
        if not isinstance(metadata, MappingABC):
            metadata = {}
        boundary_id = (
            metadata.get("local_relevance_medium_read_only_prior_result_reentry_boundary_id")
            or DEFAULT_BOUNDARY_ID
        )
        filename = (
            f"{boundary_id}__local_relevance_medium_read_only_"
            "prior_result_reentry_boundary_v0_min_result.json"
        )
        candidate = OUTPUT_ROOT / filename
    else:
        candidate = Path(output_path)

    candidate.parent.mkdir(parents=True, exist_ok=True)
    final_path = candidate
    if final_path.exists():
        stem = candidate.stem
        suffix = candidate.suffix
        index = 1
        while final_path.exists():
            final_path = candidate.with_name(f"{stem}_{index:03d}{suffix}")
            index += 1
    final_path.write_text(
        json.dumps(result_copy, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_request(
    *,
    local_relevance_medium_read_only_prior_result_reentry_boundary_id: str = DEFAULT_BOUNDARY_ID,
    local_relevance_medium_read_only_prior_result_reentry_boundary_question: str = CORE_QUESTION,
    local_relevance_medium_read_only_prior_result_reentry_boundary_intent: str = INTENT_RECORD,
    selected_runtime_held_reentry_artifact: Path | str = DEFAULT_RUNTIME_HELD_REENTRY_ARTIFACT,
    selected_runtime_held_reentry_boundary_artifact: Path | str = DEFAULT_RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT,
    selected_runtime_held_state_artifact: Path | str = DEFAULT_RUNTIME_HELD_STATE_ARTIFACT,
    selected_runtime_held_state_boundary_artifact: Path | str = DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT,
    selected_runtime_artifact: Path | str = DEFAULT_RUNTIME_ARTIFACT,
    selected_runtime_boundary_artifact: Path | str = DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
    selected_runtime_permission_artifact: Path | str = DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
    selected_operation_execution_artifact: Path | str = DEFAULT_OPERATION_EXECUTION_ARTIFACT,
    selected_command: str = SELECTED_COMMAND,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    declared_non_claims: Mapping[str, Any] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    """Build a declared request with bounded defaults and false non-claims."""

    request = {
        "local_relevance_medium_read_only_prior_result_reentry_boundary_id": (
            local_relevance_medium_read_only_prior_result_reentry_boundary_id
        ),
        "local_relevance_medium_read_only_prior_result_reentry_boundary_question": (
            local_relevance_medium_read_only_prior_result_reentry_boundary_question
        ),
        "local_relevance_medium_read_only_prior_result_reentry_boundary_intent": (
            local_relevance_medium_read_only_prior_result_reentry_boundary_intent
        ),
        "selected_runtime_held_reentry_artifact": str(
            selected_runtime_held_reentry_artifact
        ),
        "selected_runtime_held_reentry_boundary_artifact": str(
            selected_runtime_held_reentry_boundary_artifact
        ),
        "selected_runtime_held_state_artifact": str(
            selected_runtime_held_state_artifact
        ),
        "selected_runtime_held_state_boundary_artifact": str(
            selected_runtime_held_state_boundary_artifact
        ),
        "selected_runtime_artifact": str(selected_runtime_artifact),
        "selected_runtime_boundary_artifact": str(selected_runtime_boundary_artifact),
        "selected_runtime_permission_artifact": str(
            selected_runtime_permission_artifact
        ),
        "selected_operation_execution_artifact": str(
            selected_operation_execution_artifact
        ),
        "selected_command": selected_command,
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "declared_non_claims": _canonical_non_claims(),
    }
    if declared_non_claims is not None:
        request["declared_non_claims"] = copy.deepcopy(dict(declared_non_claims))
    request.update(copy.deepcopy(extra_fields))
    return _sanitize(request)
