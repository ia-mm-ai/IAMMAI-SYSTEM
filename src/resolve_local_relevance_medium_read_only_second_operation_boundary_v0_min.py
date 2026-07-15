"""Resolve one local read-only second-operation boundary.

This resolver records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY object only. It reads
one clean prior-result re-entry cycle artifact, one clean prior-result re-entry
boundary artifact, one clean runtime-held-re-entry artifact, one clean
runtime-held-re-entry boundary artifact, one clean runtime-held-state artifact,
one clean runtime-held-state boundary artifact, one clean runtime v3 artifact,
one clean runtime boundary v2 artifact, one clean runtime permission artifact,
and one clean operation execution artifact as explicit basis references.

The boundary is local, read-only, selected-second-operation-consideration-only,
raw-state-body-excluding, state-mutation-refusing, state-update-refusing,
closure-token-aware, non-second-operation-shaped, non-continuation-shaped,
non-hosting-shaped, non-loop-shaped, non-daemon-shaped, and
older-runtime-authority-import-blocking.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlySecondOperationBoundaryV0MinError(RuntimeError):
    """Bounded resolver error for second-operation-boundary handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "second_operation_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "prior_result_reentry_cycle_v0_min_v2"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "prior_result_reentry_cycle_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "prior_result_reentry_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_reentry_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_reentry_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_state_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_state_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_v0_min_v3"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_v0_min_v2"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_boundary_v0_min_v2"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_permission_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "operation_execution_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_reception_feed_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_deployment_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_release_v0_min"),
)

DEFAULT_BOUNDARY_ID = "local_relevance_medium_read_only_second_operation_boundary_001"
BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_SECOND_OPERATION_CONSIDERATION_ONLY"
SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)
SELECTED_COMMAND = "state"

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_PRIOR_RESULT_REENTRY_CYCLE_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "prior_result_reentry_cycle_v0_min_v2/"
    "local_relevance_medium_read_only_prior_result_reentry_cycle_reference_review_001__"
    "local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_result.json"
)
DEFAULT_PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "prior_result_reentry_boundary_v0_min/"
    "local_relevance_medium_read_only_prior_result_reentry_boundary_reference_review_001__"
    "local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_result.json"
)
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

EXPECTED_PRIOR_RESULT_REENTRY_CYCLE_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_RECORDED"
)
EXPECTED_PRIOR_RESULT_REENTRY_BOUNDARY_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_RECORDED"
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

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE "
    "for selected command state, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION, existing reusable "
    "read-only lookup permission, prior lookup-pair coverage, and prior local "
    "carrier command surface, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY be recorded that "
    "permits a future local read-only second operation to be considered as a "
    "separately bounded step, without creating second operation, creating "
    "continuation, creating runtime hosting, creating runtime loop, creating "
    "daemon behavior, creating public API, creating participant-facing "
    "interface, creating distributed network behavior, creating general "
    "operation permission, creating general lookup permission, creating "
    "arbitrary lookup permission, permitting unsupported commands, permitting "
    "unsupported lookup keys, creating new lookup entry beyond the already "
    "bounded selected-state lookup result object, embedding raw state body, "
    "mutating state, updating state, accepting new entries, accepting new "
    "signals, performing filesystem discovery, importing older runtime/"
    "post-runtime authority, creating query surface, registry, search, ranking, "
    "scoring, priority, validity judgment, truth judgment, authority, "
    "currentness, synchronization, participation authorization, participant "
    "role, repeated reception permission, arbitrary reception, feed, source "
    "transfer, source receipt, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
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
    "artifact_existence_treated_as_second_operation_boundary_authority",
    "latest_file_posture_treated_as_second_operation_boundary_authority",
    "repo_local_availability_treated_as_second_operation_boundary_authority",
    "hidden_repo_state_used_as_second_operation_boundary_content",
    "hidden_repo_state_used_as_second_operation_boundary_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "prior_result_cycle_v1_failure_repaired",
    "prior_result_cycle_v1_failure_hidden",
    "prior_result_cycle_v1_failure_claimed_passed",
    "prior_result_boundary_v1_failure_repaired",
    "prior_result_boundary_v1_failure_hidden",
    "prior_result_boundary_v1_failure_claimed_passed",
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
    "local_relevance_medium_read_only_second_operation_boundary_recorded",
    "basis_prior_result_reentry_cycle_artifact_preserved",
    "basis_prior_result_reentry_boundary_artifact_preserved",
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
    "selected_prior_result_reentry_cycle_recorded",
    "prior_result_reentry_cycle_created",
    "prior_result_reentry_cycle_local_only",
    "prior_result_reentry_cycle_read_only",
    "cycle_basis_reference_only",
    "selected_prior_result_reentry_boundary_recorded",
    "future_prior_result_reentry_cycle_may_be_considered",
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
    "future_second_operation_may_be_considered",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "prior_result_boundary_v1_failure_evidence_preserved",
    "prior_result_boundary_v2_successor_evidence_preserved",
    "prior_result_cycle_v1_failure_evidence_preserved",
    "prior_result_cycle_v2_successor_evidence_preserved",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

_ARTIFACT_ERROR_SUFFIXES = (
    "PATH_MISSING",
    "UNREADABLE",
    "NOT_JSON_OBJECT",
    "NOT_RECORDED",
    "FAILED_CHECKS_PRESENT",
    "VERSION_NOT_0_1_0",
)
_ARTIFACT_BLOCK_PREFIXES = (
    "PRIOR_RESULT_REENTRY_CYCLE_ARTIFACT",
    "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT",
    "RUNTIME_HELD_REENTRY_ARTIFACT",
    "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT",
    "RUNTIME_HELD_STATE_ARTIFACT",
    "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT",
    "RUNTIME_ARTIFACT",
    "RUNTIME_BOUNDARY_ARTIFACT",
    "RUNTIME_PERMISSION_ARTIFACT",
    "OPERATION_EXECUTION_ARTIFACT",
)

_EXTRA_BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_BLOCK_REQUESTED",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_SELECTED_SECOND_OPERATION_CONSIDERATION_ONLY",
    "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED",
    "PRIOR_RESULT_REENTRY_CYCLE_NOT_CREATED",
    "PRIOR_RESULT_REENTRY_CYCLE_LOCAL_ONLY_NOT_TRUE",
    "PRIOR_RESULT_REENTRY_CYCLE_READ_ONLY_NOT_TRUE",
    "CYCLE_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "SELECTED_PRIOR_RESULT_REENTRY_BOUNDARY_NOT_RECORDED",
    "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED",
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
    "FUTURE_SECOND_OPERATION_MAY_NOT_BE_CONSIDERED",
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
    "PRIOR_RESULT_CYCLE_V1_FAILURE_REPAIRED",
    "PRIOR_RESULT_CYCLE_V1_FAILURE_HIDDEN",
    "PRIOR_RESULT_CYCLE_V1_FAILURE_CLAIMED_PASSED",
    "PRIOR_RESULT_BOUNDARY_V1_FAILURE_REPAIRED",
    "PRIOR_RESULT_BOUNDARY_V1_FAILURE_HIDDEN",
    "PRIOR_RESULT_BOUNDARY_V1_FAILURE_CLAIMED_PASSED",
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
    "RAW_STATE_BODY_EMBEDDED",
    "STATE_MUTATION_PERFORMED",
    "STATE_UPDATE_PERFORMED",
    "ARTIFACT_EXISTENCE_TREATED_AS_SECOND_OPERATION_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_SECOND_OPERATION_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SECOND_OPERATION_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SECOND_OPERATION_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SECOND_OPERATION_BOUNDARY_AUTHORITY",
    "PRIOR_ARTIFACTS_MUTATED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_REQUEST_UNREADABLE",
)

BLOCK_CODES = tuple(
    code
    for code in (
        *(
            f"{prefix}_{suffix}"
            for prefix in _ARTIFACT_BLOCK_PREFIXES
            for suffix in _ARTIFACT_ERROR_SUFFIXES
        ),
        *_EXTRA_BLOCK_CODES,
    )
)

FIELD_BLOCK_CODES = {
    "second_operation_created": "SECOND_OPERATION_CREATED",
    "continuation_created": "CONTINUATION_CREATED",
    "runtime_hosting_created": "RUNTIME_HOSTING_CREATED",
    "runtime_loop_created": "RUNTIME_LOOP_CREATED",
    "daemon_behavior_created": "DAEMON_BEHAVIOR_CREATED",
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
    "artifact_existence_treated_as_second_operation_boundary_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_SECOND_OPERATION_BOUNDARY_AUTHORITY"
    ),
    "latest_file_posture_treated_as_second_operation_boundary_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_SECOND_OPERATION_BOUNDARY_AUTHORITY"
    ),
    "repo_local_availability_treated_as_second_operation_boundary_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_SECOND_OPERATION_BOUNDARY_AUTHORITY"
    ),
    "hidden_repo_state_used_as_second_operation_boundary_content": (
        "HIDDEN_REPO_STATE_USED_AS_SECOND_OPERATION_BOUNDARY_CONTENT"
    ),
    "hidden_repo_state_used_as_second_operation_boundary_authority": (
        "HIDDEN_REPO_STATE_USED_AS_SECOND_OPERATION_BOUNDARY_AUTHORITY"
    ),
    "prior_artifacts_mutated": "PRIOR_ARTIFACTS_MUTATED",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
    "prior_result_cycle_v1_failure_repaired": "PRIOR_RESULT_CYCLE_V1_FAILURE_REPAIRED",
    "prior_result_cycle_v1_failure_hidden": "PRIOR_RESULT_CYCLE_V1_FAILURE_HIDDEN",
    "prior_result_cycle_v1_failure_claimed_passed": (
        "PRIOR_RESULT_CYCLE_V1_FAILURE_CLAIMED_PASSED"
    ),
    "prior_result_boundary_v1_failure_repaired": (
        "PRIOR_RESULT_BOUNDARY_V1_FAILURE_REPAIRED"
    ),
    "prior_result_boundary_v1_failure_hidden": (
        "PRIOR_RESULT_BOUNDARY_V1_FAILURE_HIDDEN"
    ),
    "prior_result_boundary_v1_failure_claimed_passed": (
        "PRIOR_RESULT_BOUNDARY_V1_FAILURE_CLAIMED_PASSED"
    ),
    "runtime_v0_failure_repaired": "RUNTIME_V0_FAILURE_REPAIRED",
    "runtime_v0_failure_hidden": "RUNTIME_V0_FAILURE_HIDDEN",
    "runtime_v0_failure_claimed_passed": "RUNTIME_V0_FAILURE_CLAIMED_PASSED",
    "runtime_v2_failure_repaired": "RUNTIME_V2_FAILURE_REPAIRED",
    "runtime_v2_failure_hidden": "RUNTIME_V2_FAILURE_HIDDEN",
    "runtime_v2_failure_claimed_passed": "RUNTIME_V2_FAILURE_CLAIMED_PASSED",
    "runtime_boundary_v0_failure_repaired": "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
    "runtime_boundary_v0_failure_hidden": "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN",
    "runtime_boundary_v0_failure_claimed_passed": (
        "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED"
    ),
    "raw_state_body_embedded": "RAW_STATE_BODY_EMBEDDED",
    "state_mutation_performed": "STATE_MUTATION_PERFORMED",
    "state_update_performed": "STATE_UPDATE_PERFORMED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
}

HOSTILE_SENTINELS = (
    "RAW_SECOND_OPERATION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_PRIOR_RESULT_REENTRY_CYCLE_BODY_MUST_NOT_RETURN",
    "RAW_PRIOR_RESULT_REENTRY_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_STATE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_STATE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_second_operation_boundary_body",
    "raw_second_operation_body",
    "raw_continuation_body",
    "raw_prior_result_reentry_cycle_body",
    "raw_prior_result_reentry_boundary_body",
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
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}
REDACTED_RAW_CONTENT = "[redacted_raw_content]"

_MISSING = object()


BASIS_ARTIFACT_SPECS = (
    {
        "name": "prior_result_reentry_cycle",
        "request_key": "selected_prior_result_reentry_cycle_artifact",
        "basis_key": "selected_prior_result_reentry_cycle_artifact_basis",
        "basis_prefix": "basis_prior_result_reentry_cycle",
        "object_key": "local_relevance_medium_read_only_prior_result_reentry_cycle",
        "expected_outcome": EXPECTED_PRIOR_RESULT_REENTRY_CYCLE_OUTCOME,
        "block_prefix": "PRIOR_RESULT_REENTRY_CYCLE_ARTIFACT",
        "default_path": DEFAULT_PRIOR_RESULT_REENTRY_CYCLE_ARTIFACT,
    },
    {
        "name": "prior_result_reentry_boundary",
        "request_key": "selected_prior_result_reentry_boundary_artifact",
        "basis_key": "selected_prior_result_reentry_boundary_artifact_basis",
        "basis_prefix": "basis_prior_result_reentry_boundary",
        "object_key": "local_relevance_medium_read_only_prior_result_reentry_boundary",
        "expected_outcome": EXPECTED_PRIOR_RESULT_REENTRY_BOUNDARY_OUTCOME,
        "block_prefix": "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT",
        "default_path": DEFAULT_PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT,
    },
    {
        "name": "runtime_held_reentry",
        "request_key": "selected_runtime_held_reentry_artifact",
        "basis_key": "selected_runtime_held_reentry_artifact_basis",
        "basis_prefix": "basis_runtime_held_reentry",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry",
        "expected_outcome": EXPECTED_RUNTIME_HELD_REENTRY_OUTCOME,
        "block_prefix": "RUNTIME_HELD_REENTRY_ARTIFACT",
        "default_path": DEFAULT_RUNTIME_HELD_REENTRY_ARTIFACT,
    },
    {
        "name": "runtime_held_reentry_boundary",
        "request_key": "selected_runtime_held_reentry_boundary_artifact",
        "basis_key": "selected_runtime_held_reentry_boundary_artifact_basis",
        "basis_prefix": "basis_runtime_held_reentry_boundary",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry_boundary",
        "expected_outcome": EXPECTED_RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME,
        "block_prefix": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT",
        "default_path": DEFAULT_RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT,
    },
    {
        "name": "runtime_held_state",
        "request_key": "selected_runtime_held_state_artifact",
        "basis_key": "selected_runtime_held_state_artifact_basis",
        "basis_prefix": "basis_runtime_held_state",
        "object_key": "local_relevance_medium_read_only_runtime_held_state",
        "expected_outcome": EXPECTED_RUNTIME_HELD_STATE_OUTCOME,
        "block_prefix": "RUNTIME_HELD_STATE_ARTIFACT",
        "default_path": DEFAULT_RUNTIME_HELD_STATE_ARTIFACT,
    },
    {
        "name": "runtime_held_state_boundary",
        "request_key": "selected_runtime_held_state_boundary_artifact",
        "basis_key": "selected_runtime_held_state_boundary_artifact_basis",
        "basis_prefix": "basis_runtime_held_state_boundary",
        "object_key": "local_relevance_medium_read_only_runtime_held_state_boundary",
        "expected_outcome": EXPECTED_RUNTIME_HELD_STATE_BOUNDARY_OUTCOME,
        "block_prefix": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT",
        "default_path": DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT,
    },
    {
        "name": "runtime",
        "request_key": "selected_runtime_artifact",
        "basis_key": "selected_runtime_artifact_basis",
        "basis_prefix": "basis_runtime",
        "object_key": "local_relevance_medium_read_only_runtime",
        "expected_outcome": EXPECTED_RUNTIME_OUTCOME,
        "block_prefix": "RUNTIME_ARTIFACT",
        "default_path": DEFAULT_RUNTIME_ARTIFACT,
    },
    {
        "name": "runtime_boundary",
        "request_key": "selected_runtime_boundary_artifact",
        "basis_key": "selected_runtime_boundary_artifact_basis",
        "basis_prefix": "basis_runtime_boundary",
        "object_key": "local_relevance_medium_read_only_runtime_boundary",
        "expected_outcome": EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        "block_prefix": "RUNTIME_BOUNDARY_ARTIFACT",
        "default_path": DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
    },
    {
        "name": "runtime_permission",
        "request_key": "selected_runtime_permission_artifact",
        "basis_key": "selected_runtime_permission_artifact_basis",
        "basis_prefix": "basis_runtime_permission",
        "object_key": "local_relevance_medium_read_only_runtime_permission",
        "expected_outcome": EXPECTED_RUNTIME_PERMISSION_OUTCOME,
        "block_prefix": "RUNTIME_PERMISSION_ARTIFACT",
        "default_path": DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
    },
    {
        "name": "operation_execution",
        "request_key": "selected_operation_execution_artifact",
        "basis_key": "selected_operation_execution_artifact_basis",
        "basis_prefix": "basis_operation_execution",
        "object_key": "local_relevance_medium_read_only_operation_execution",
        "expected_outcome": EXPECTED_OPERATION_EXECUTION_OUTCOME,
        "block_prefix": "OPERATION_EXECUTION_ARTIFACT",
        "default_path": DEFAULT_OPERATION_EXECUTION_ARTIFACT,
    },
)

TRUE_POSTURE_REQUIREMENTS = (
    (
        "selected_prior_result_reentry_cycle_recorded",
        "prior_result_reentry_cycle",
        (
            "selected_prior_result_reentry_cycle_recorded",
            "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded",
        ),
        "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED",
    ),
    (
        "prior_result_reentry_cycle_created",
        "prior_result_reentry_cycle",
        ("prior_result_reentry_cycle_created",),
        "PRIOR_RESULT_REENTRY_CYCLE_NOT_CREATED",
    ),
    (
        "prior_result_reentry_cycle_local_only",
        "prior_result_reentry_cycle",
        ("prior_result_reentry_cycle_local_only",),
        "PRIOR_RESULT_REENTRY_CYCLE_LOCAL_ONLY_NOT_TRUE",
    ),
    (
        "prior_result_reentry_cycle_read_only",
        "prior_result_reentry_cycle",
        ("prior_result_reentry_cycle_read_only",),
        "PRIOR_RESULT_REENTRY_CYCLE_READ_ONLY_NOT_TRUE",
    ),
    (
        "cycle_basis_reference_only",
        "prior_result_reentry_cycle",
        ("cycle_basis_reference_only",),
        "CYCLE_BASIS_REFERENCE_ONLY_NOT_TRUE",
    ),
    (
        "selected_prior_result_reentry_boundary_recorded",
        "prior_result_reentry_boundary",
        (
            "selected_prior_result_reentry_boundary_recorded",
            "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded",
        ),
        "SELECTED_PRIOR_RESULT_REENTRY_BOUNDARY_NOT_RECORDED",
    ),
    (
        "future_prior_result_reentry_cycle_may_be_considered",
        "prior_result_reentry_boundary",
        ("future_prior_result_reentry_cycle_may_be_considered",),
        "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED",
    ),
    (
        "selected_runtime_held_reentry_recorded",
        "runtime_held_reentry",
        (
            "selected_runtime_held_reentry_recorded",
            "local_relevance_medium_read_only_runtime_held_reentry_recorded",
        ),
        "SELECTED_RUNTIME_HELD_REENTRY_NOT_RECORDED",
    ),
    (
        "runtime_held_reentry_created",
        "runtime_held_reentry",
        ("runtime_held_reentry_created",),
        "RUNTIME_HELD_REENTRY_NOT_CREATED",
    ),
    (
        "runtime_held_reentry_local_only",
        "runtime_held_reentry",
        ("runtime_held_reentry_local_only",),
        "RUNTIME_HELD_REENTRY_LOCAL_ONLY_NOT_TRUE",
    ),
    (
        "runtime_held_reentry_read_only",
        "runtime_held_reentry",
        ("runtime_held_reentry_read_only",),
        "RUNTIME_HELD_REENTRY_READ_ONLY_NOT_TRUE",
    ),
    (
        "held_reentry_basis_reference_only",
        "runtime_held_reentry",
        ("held_reentry_basis_reference_only",),
        "HELD_REENTRY_BASIS_REFERENCE_ONLY_NOT_TRUE",
    ),
    (
        "selected_runtime_held_reentry_boundary_recorded",
        "runtime_held_reentry_boundary",
        (
            "selected_runtime_held_reentry_boundary_recorded",
            "local_relevance_medium_read_only_runtime_held_reentry_boundary_recorded",
        ),
        "SELECTED_RUNTIME_HELD_REENTRY_BOUNDARY_NOT_RECORDED",
    ),
    (
        "future_runtime_held_reentry_may_be_considered",
        "runtime_held_reentry_boundary",
        ("future_runtime_held_reentry_may_be_considered",),
        "FUTURE_RUNTIME_HELD_REENTRY_MAY_NOT_BE_CONSIDERED",
    ),
    (
        "selected_runtime_held_state_recorded",
        "runtime_held_state",
        (
            "selected_runtime_held_state_recorded",
            "local_relevance_medium_read_only_runtime_held_state_recorded",
        ),
        "SELECTED_RUNTIME_HELD_STATE_NOT_RECORDED",
    ),
    (
        "runtime_held_state_created",
        "runtime_held_state",
        ("runtime_held_state_created",),
        "RUNTIME_HELD_STATE_NOT_CREATED",
    ),
    (
        "runtime_held_state_local_only",
        "runtime_held_state",
        ("runtime_held_state_local_only",),
        "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE",
    ),
    (
        "runtime_held_state_read_only",
        "runtime_held_state",
        ("runtime_held_state_read_only",),
        "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE",
    ),
    (
        "held_state_basis_reference_only",
        "runtime_held_state",
        ("held_state_basis_reference_only",),
        "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE",
    ),
    (
        "selected_runtime_held_state_boundary_recorded",
        "runtime_held_state_boundary",
        (
            "selected_runtime_held_state_boundary_recorded",
            "local_relevance_medium_read_only_runtime_held_state_boundary_recorded",
        ),
        "SELECTED_RUNTIME_HELD_STATE_BOUNDARY_NOT_RECORDED",
    ),
    (
        "future_runtime_held_state_may_be_considered",
        "runtime_held_state_boundary",
        ("future_runtime_held_state_may_be_considered",),
        "FUTURE_RUNTIME_HELD_STATE_MAY_NOT_BE_CONSIDERED",
    ),
    (
        "selected_runtime_recorded",
        "runtime",
        ("selected_runtime_recorded", "local_relevance_medium_read_only_runtime_recorded"),
        "SELECTED_RUNTIME_NOT_RECORDED",
    ),
    ("runtime_created", "runtime", ("runtime_created",), "RUNTIME_NOT_CREATED"),
    (
        "runtime_local_only",
        "runtime",
        ("runtime_local_only",),
        "RUNTIME_LOCAL_ONLY_NOT_TRUE",
    ),
    (
        "runtime_read_only",
        "runtime",
        ("runtime_read_only",),
        "RUNTIME_READ_ONLY_NOT_TRUE",
    ),
    (
        "selected_runtime_boundary_recorded",
        "runtime_boundary",
        (
            "selected_runtime_boundary_recorded",
            "local_relevance_medium_read_only_runtime_boundary_recorded",
        ),
        "SELECTED_RUNTIME_BOUNDARY_NOT_RECORDED",
    ),
    (
        "future_runtime_may_be_considered",
        "runtime_boundary",
        ("future_runtime_may_be_considered",),
        "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED",
    ),
    (
        "selected_runtime_permission_recorded",
        "runtime_permission",
        (
            "selected_runtime_permission_recorded",
            "local_relevance_medium_read_only_runtime_permission_recorded",
        ),
        "SELECTED_RUNTIME_PERMISSION_NOT_RECORDED",
    ),
    (
        "runtime_permission_created",
        "runtime_permission",
        ("runtime_permission_created",),
        "RUNTIME_PERMISSION_NOT_CREATED",
    ),
    (
        "runtime_permission_local_only",
        "runtime_permission",
        ("runtime_permission_local_only",),
        "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE",
    ),
    (
        "runtime_permission_read_only",
        "runtime_permission",
        ("runtime_permission_read_only",),
        "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE",
    ),
    (
        "selected_operation_execution_recorded",
        "operation_execution",
        (
            "selected_operation_execution_recorded",
            "local_relevance_medium_read_only_operation_execution_recorded",
        ),
        "SELECTED_OPERATION_EXECUTION_NOT_RECORDED",
    ),
    (
        "operation_execution_created",
        "operation_execution",
        ("operation_execution_created",),
        "OPERATION_EXECUTION_NOT_CREATED",
    ),
    (
        "operation_execution_performed",
        "operation_execution",
        ("operation_execution_performed",),
        "OPERATION_EXECUTION_NOT_PERFORMED",
    ),
    (
        "operation_execution_local_only",
        "operation_execution",
        ("operation_execution_local_only",),
        "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE",
    ),
    (
        "operation_execution_read_only",
        "operation_execution",
        ("operation_execution_read_only",),
        "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE",
    ),
    (
        "runtime_v0_failure_evidence_preserved",
        "prior_result_reentry_cycle",
        ("runtime_v0_failure_evidence_preserved",),
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    ),
    (
        "runtime_v2_failure_evidence_preserved",
        "prior_result_reentry_cycle",
        ("runtime_v2_failure_evidence_preserved",),
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    ),
    (
        "runtime_boundary_v0_failure_evidence_preserved",
        "prior_result_reentry_cycle",
        ("runtime_boundary_v0_failure_evidence_preserved",),
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    ),
    (
        "prior_result_boundary_v1_failure_evidence_preserved",
        "prior_result_reentry_cycle",
        ("prior_result_boundary_v1_failure_evidence_preserved",),
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    ),
    (
        "prior_result_boundary_v2_successor_evidence_preserved",
        "prior_result_reentry_cycle",
        ("prior_result_boundary_v2_successor_evidence_preserved",),
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    ),
    (
        "prior_result_cycle_v1_failure_evidence_preserved",
        "prior_result_reentry_cycle",
        ("prior_result_cycle_v1_failure_evidence_preserved",),
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    ),
    (
        "prior_result_cycle_v2_successor_evidence_preserved",
        "prior_result_reentry_cycle",
        ("prior_result_cycle_v2_successor_evidence_preserved",),
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    ),
)

BOUNDARY_FALSE_FIELDS = (
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
    "artifact_existence_treated_as_second_operation_boundary_authority",
    "latest_file_posture_treated_as_second_operation_boundary_authority",
    "repo_local_availability_treated_as_second_operation_boundary_authority",
    "hidden_repo_state_used_as_second_operation_boundary_content",
    "hidden_repo_state_used_as_second_operation_boundary_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "prior_result_cycle_v1_failure_repaired",
    "prior_result_cycle_v1_failure_hidden",
    "prior_result_cycle_v1_failure_claimed_passed",
    "prior_result_boundary_v1_failure_repaired",
    "prior_result_boundary_v1_failure_hidden",
    "prior_result_boundary_v1_failure_claimed_passed",
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

WHAT_REMAINS_OPEN = (
    "local relevance medium read-only second-operation boundary tests",
    "local relevance medium read-only second-operation boundary live artifact",
    "local relevance medium read-only second-operation boundary terminal summary",
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
    "authority/currentness/truth/synchronization",
    "participation authorization",
    "deployment",
    "public release",
    "follow-on work",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _is_mapping(value: Any) -> bool:
    return isinstance(value, MappingABC)


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_sensitive_key(key: Any) -> bool:
    text = str(key)
    return text in SENSITIVE_CONTENT_KEYS or text.endswith("_body")


def _sanitize_value(value: Any, key: Any | None = None) -> Any:
    if key is not None and _is_sensitive_key(key):
        return REDACTED_RAW_CONTENT
    if isinstance(value, str):
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return REDACTED_RAW_CONTENT
        return value
    if _is_mapping(value):
        return {str(k): _sanitize_value(v, k) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize_value(item) for item in value]
    if isinstance(value, tuple):
        return tuple(_sanitize_value(item) for item in value)
    return copy.deepcopy(value)


def _selected_object(artifact: Mapping[str, Any] | None, object_key: str) -> Mapping[str, Any]:
    if not _is_mapping(artifact):
        return {}
    selected = artifact.get(object_key)
    if _is_mapping(selected):
        return selected
    return {}


def _top_level_non_claims(artifact: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not _is_mapping(artifact):
        return {}
    non_claims = artifact.get("non_claims")
    if _is_mapping(non_claims):
        return non_claims
    return {}


def _extract_exact_posture(
    artifact: Mapping[str, Any] | None,
    object_key: str,
    key: str,
) -> Any:
    selected = _selected_object(artifact, object_key)
    if key in selected:
        return selected[key]
    non_claims = _top_level_non_claims(artifact)
    if key in non_claims:
        return non_claims[key]
    return _MISSING


def _extract_exact_true_posture(
    artifact: Mapping[str, Any] | None,
    object_key: str,
    keys: tuple[str, ...],
) -> Any:
    selected = _selected_object(artifact, object_key)
    for key in keys:
        if key in selected:
            return selected[key]
    return _MISSING


def _extract_result_version(artifact: Mapping[str, Any]) -> Any:
    for key in ("result_version", "boundary_version", "cycle_version", "runtime_version"):
        if key in artifact:
            return artifact[key]
    for section_name, section in artifact.items():
        if _is_mapping(section) and (
            section_name.endswith("_metadata") or section_name.endswith("_summary")
        ):
            for key in (
                "result_version",
                "boundary_version",
                "cycle_version",
                "held_reentry_version",
                "held_state_version",
                "runtime_version",
                "runtime_permission_version",
                "operation_execution_version",
            ):
                if key in section:
                    return section[key]
    return _MISSING


def _check_records_from_artifact(artifact: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    checks: list[Mapping[str, Any]] = []
    for key, value in artifact.items():
        if key.endswith("_checks") and isinstance(value, list):
            checks.extend(item for item in value if _is_mapping(item))
    return checks


def _extract_failed_check_count(artifact: Mapping[str, Any]) -> Any:
    for key in ("failed_check_count", "failed_checks"):
        value = artifact.get(key)
        if isinstance(value, int) and not isinstance(value, bool):
            return value
    for section_name, section in artifact.items():
        if _is_mapping(section) and (
            section_name.endswith("_metadata") or section_name.endswith("_summary")
        ):
            value = section.get("failed_check_count")
            if isinstance(value, int) and not isinstance(value, bool):
                return value
    checks = _check_records_from_artifact(artifact)
    if checks:
        return sum(1 for check in checks if check.get("passed") is not True)
    return _MISSING


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> None:
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize_value(expected_posture),
        "actual_posture": _sanitize_value(actual_posture),
    }
    if not passed:
        record["block_code"] = code
        record["failure_code"] = code
    checks.append(record)


def _failed_checks(checks: list[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [check for check in checks if check.get("passed") is not True]


def _first_block_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code in BLOCK_CODES:
                return code
    return None


def _read_artifact(
    spec: Mapping[str, Any],
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[Mapping[str, Any] | None, dict[str, Any]]:
    request_key = str(spec["request_key"])
    block_prefix = str(spec["block_prefix"])
    path_value = request.get(request_key)
    path_declared = path_value not in (None, "")
    _add_check(
        checks,
        f"{request_key}_path_declared",
        path_declared,
        "declared artifact path",
        path_value if path_declared else None,
        f"{block_prefix}_PATH_MISSING",
    )
    basis: dict[str, Any] = {
        "artifact_path": _sanitize_value(str(path_value)) if path_declared else None,
        "artifact_readable": False,
        "artifact_json_object": False,
        "artifact_preserved": False,
        "outcome": None,
        "result_version": None,
        "failed_check_count": None,
    }
    if not path_declared:
        return None, basis

    path = Path(path_value)
    try:
        with path.open("r", encoding="utf-8") as artifact_file:
            artifact = json.load(artifact_file)
    except Exception as exc:  # noqa: BLE001 - bounded public block result, not escape.
        _add_check(
            checks,
            f"{request_key}_readable",
            False,
            "readable JSON artifact",
            f"{type(exc).__name__}: {exc}",
            f"{block_prefix}_UNREADABLE",
        )
        return None, basis

    _add_check(
        checks,
        f"{request_key}_readable",
        True,
        "readable JSON artifact",
        "readable",
        f"{block_prefix}_UNREADABLE",
    )

    is_object = _is_mapping(artifact)
    _add_check(
        checks,
        f"{request_key}_json_object",
        is_object,
        "JSON object",
        type(artifact).__name__,
        f"{block_prefix}_NOT_JSON_OBJECT",
    )
    if not is_object:
        return None, basis

    artifact_mapping = artifact
    outcome = artifact_mapping.get("outcome")
    result_version = _extract_result_version(artifact_mapping)
    failed_check_count = _extract_failed_check_count(artifact_mapping)
    expected_outcome = spec["expected_outcome"]
    basis.update(
        {
            "artifact_readable": True,
            "artifact_json_object": True,
            "outcome": _sanitize_value(outcome),
            "result_version": _sanitize_value(result_version)
            if result_version is not _MISSING
            else None,
            "failed_check_count": failed_check_count
            if failed_check_count is not _MISSING
            else None,
        }
    )

    _add_check(
        checks,
        f"{request_key}_outcome_recorded",
        outcome == expected_outcome,
        expected_outcome,
        outcome,
        f"{block_prefix}_NOT_RECORDED",
    )
    _add_check(
        checks,
        f"{request_key}_result_version_0_1_0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version if result_version is not _MISSING else None,
        f"{block_prefix}_VERSION_NOT_0_1_0",
    )
    _add_check(
        checks,
        f"{request_key}_failed_check_count_zero",
        failed_check_count == 0,
        0,
        failed_check_count if failed_check_count is not _MISSING else None,
        f"{block_prefix}_FAILED_CHECKS_PRESENT",
    )
    if (
        outcome == expected_outcome
        and result_version == RESULT_VERSION
        and failed_check_count == 0
    ):
        basis["artifact_preserved"] = True
    return artifact_mapping, basis


def _validate_request_header(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    question = request.get(
        "local_relevance_medium_read_only_second_operation_boundary_question"
    )
    _add_check(
        checks,
        "second_operation_boundary_question_declared",
        bool(question),
        "declared second-operation boundary question",
        question if question else None,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_QUESTION_UNDECLARED",
    )

    intent = request.get(
        "local_relevance_medium_read_only_second_operation_boundary_intent",
        INTENT_RECORD,
    )
    _add_check(
        checks,
        "second_operation_boundary_intent_supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _add_check(
        checks,
        "second_operation_boundary_not_explicitly_blocked",
        intent != INTENT_BLOCK,
        f"not {INTENT_BLOCK}",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_BLOCK_REQUESTED",
    )

    selected_command = request.get("selected_command")
    _add_check(
        checks,
        "selected_command_declared",
        selected_command is not None,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_MISSING",
    )
    _add_check(
        checks,
        "selected_command_exactly_state",
        selected_command == SELECTED_COMMAND,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )

    boundary_type = request.get("boundary_type")
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
        boundary_type == BOUNDARY_TYPE,
        BOUNDARY_TYPE,
        boundary_type,
        "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY",
    )

    boundary_scope = request.get("boundary_scope")
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
        boundary_scope == BOUNDARY_SCOPE,
        BOUNDARY_SCOPE,
        boundary_scope,
        "BOUNDARY_SCOPE_NOT_SELECTED_SECOND_OPERATION_CONSIDERATION_ONLY",
    )

    future_consideration = request.get("future_second_operation_may_be_considered", True)
    _add_check(
        checks,
        "future_second_operation_may_be_considered",
        future_consideration is True,
        True,
        future_consideration,
        "FUTURE_SECOND_OPERATION_MAY_NOT_BE_CONSIDERED",
    )


def _validate_declared_non_claims(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    declared_non_claims = request.get("declared_non_claims")
    is_mapping = _is_mapping(declared_non_claims)
    _add_check(
        checks,
        "declared_non_claims_mapping",
        is_mapping,
        "mapping with every required false non-claim set to false",
        type(declared_non_claims).__name__ if declared_non_claims is not None else None,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    if not is_mapping:
        return
    for key in REQUIRED_FALSE_NON_CLAIMS:
        actual = declared_non_claims.get(key, _MISSING)
        _add_check(
            checks,
            f"declared_non_claim_{key}_false",
            actual is False,
            False,
            actual if actual is not _MISSING else None,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _validate_top_level_false_fields(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in request:
            continue
        actual = request.get(key)
        code = FIELD_BLOCK_CODES.get(key, "NON_CLAIM_MISSING_OR_FLIPPED")
        _add_check(
            checks,
            f"top_level_{key}_not_true",
            actual is not True,
            "not true",
            actual,
            code,
        )


def _validate_true_postures(
    artifacts: Mapping[str, Mapping[str, Any]],
    checks: list[dict[str, Any]],
) -> dict[str, bool]:
    postures: dict[str, bool] = {}
    specs_by_name = {str(spec["name"]): spec for spec in BASIS_ARTIFACT_SPECS}
    for output_key, artifact_name, aliases, code in TRUE_POSTURE_REQUIREMENTS:
        artifact = artifacts.get(artifact_name)
        spec = specs_by_name[artifact_name]
        actual = _extract_exact_true_posture(
            artifact,
            str(spec["object_key"]),
            aliases,
        )
        passed = actual is True
        _add_check(
            checks,
            output_key,
            passed,
            True,
            actual if actual is not _MISSING else None,
            code,
        )
        postures[output_key] = bool(passed)
    return postures


def _validate_basis_false_postures(
    artifacts: Mapping[str, Mapping[str, Any]],
    checks: list[dict[str, Any]],
) -> None:
    specs_by_name = {str(spec["name"]): spec for spec in BASIS_ARTIFACT_SPECS}
    for artifact_name, artifact in artifacts.items():
        spec = specs_by_name[artifact_name]
        object_key = str(spec["object_key"])
        for field in BOUNDARY_FALSE_FIELDS:
            actual = _extract_exact_posture(artifact, object_key, field)
            code = FIELD_BLOCK_CODES.get(field, "NON_CLAIM_MISSING_OR_FLIPPED")
            if actual is _MISSING:
                passed = True
                reported_actual: Any = "absent"
            else:
                passed = actual is False
                reported_actual = actual
            _add_check(
                checks,
                f"{artifact_name}_{field}_not_true",
                passed,
                False,
                reported_actual,
                code,
            )


def _basis_sections_from_infos(
    basis_infos: Mapping[str, Mapping[str, Any]]
) -> dict[str, dict[str, Any]]:
    sections: dict[str, dict[str, Any]] = {}
    for spec in BASIS_ARTIFACT_SPECS:
        name = str(spec["name"])
        basis_key = str(spec["basis_key"])
        info = dict(basis_infos.get(name, {}))
        sections[basis_key] = {
            "artifact_path": info.get("artifact_path"),
            "artifact_readable": bool(info.get("artifact_readable")),
            "artifact_json_object": bool(info.get("artifact_json_object")),
            "artifact_preserved": bool(info.get("artifact_preserved")),
            "outcome": info.get("outcome"),
            "result_version": info.get("result_version"),
            "failed_check_count": info.get("failed_check_count"),
            "basis_role": name,
        }
    return sections


def _basis_path_value(
    basis_infos: Mapping[str, Mapping[str, Any]],
    name: str,
) -> Any:
    return basis_infos.get(name, {}).get("artifact_path")


def _basis_value(
    basis_infos: Mapping[str, Mapping[str, Any]],
    name: str,
    key: str,
) -> Any:
    return basis_infos.get(name, {}).get(key)


def _build_boundary_object(
    request: Mapping[str, Any],
    basis_infos: Mapping[str, Mapping[str, Any]],
    true_postures: Mapping[str, bool],
    recorded: bool,
) -> dict[str, Any]:
    boundary_id = request.get(
        "local_relevance_medium_read_only_second_operation_boundary_id",
        DEFAULT_BOUNDARY_ID,
    )
    boundary: dict[str, Any] = {
        "boundary_id": _sanitize_value(boundary_id),
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "basis_prior_result_reentry_cycle_artifact": _basis_path_value(
            basis_infos, "prior_result_reentry_cycle"
        ),
        "basis_prior_result_reentry_cycle_outcome": _basis_value(
            basis_infos, "prior_result_reentry_cycle", "outcome"
        ),
        "basis_prior_result_reentry_cycle_result_version": _basis_value(
            basis_infos, "prior_result_reentry_cycle", "result_version"
        ),
        "basis_prior_result_reentry_cycle_failed_check_count": _basis_value(
            basis_infos, "prior_result_reentry_cycle", "failed_check_count"
        ),
        "basis_prior_result_reentry_boundary_artifact": _basis_path_value(
            basis_infos, "prior_result_reentry_boundary"
        ),
        "basis_prior_result_reentry_boundary_outcome": _basis_value(
            basis_infos, "prior_result_reentry_boundary", "outcome"
        ),
        "basis_prior_result_reentry_boundary_result_version": _basis_value(
            basis_infos, "prior_result_reentry_boundary", "result_version"
        ),
        "basis_prior_result_reentry_boundary_failed_check_count": _basis_value(
            basis_infos, "prior_result_reentry_boundary", "failed_check_count"
        ),
        "basis_runtime_held_reentry_artifact": _basis_path_value(
            basis_infos, "runtime_held_reentry"
        ),
        "basis_runtime_held_reentry_outcome": _basis_value(
            basis_infos, "runtime_held_reentry", "outcome"
        ),
        "basis_runtime_held_reentry_result_version": _basis_value(
            basis_infos, "runtime_held_reentry", "result_version"
        ),
        "basis_runtime_held_reentry_failed_check_count": _basis_value(
            basis_infos, "runtime_held_reentry", "failed_check_count"
        ),
        "basis_runtime_held_reentry_boundary_artifact": _basis_path_value(
            basis_infos, "runtime_held_reentry_boundary"
        ),
        "basis_runtime_held_reentry_boundary_outcome": _basis_value(
            basis_infos, "runtime_held_reentry_boundary", "outcome"
        ),
        "basis_runtime_held_reentry_boundary_result_version": _basis_value(
            basis_infos, "runtime_held_reentry_boundary", "result_version"
        ),
        "basis_runtime_held_reentry_boundary_failed_check_count": _basis_value(
            basis_infos, "runtime_held_reentry_boundary", "failed_check_count"
        ),
        "basis_runtime_held_state_artifact": _basis_path_value(
            basis_infos, "runtime_held_state"
        ),
        "basis_runtime_held_state_outcome": _basis_value(
            basis_infos, "runtime_held_state", "outcome"
        ),
        "basis_runtime_held_state_result_version": _basis_value(
            basis_infos, "runtime_held_state", "result_version"
        ),
        "basis_runtime_held_state_failed_check_count": _basis_value(
            basis_infos, "runtime_held_state", "failed_check_count"
        ),
        "basis_runtime_held_state_boundary_artifact": _basis_path_value(
            basis_infos, "runtime_held_state_boundary"
        ),
        "basis_runtime_held_state_boundary_outcome": _basis_value(
            basis_infos, "runtime_held_state_boundary", "outcome"
        ),
        "basis_runtime_held_state_boundary_result_version": _basis_value(
            basis_infos, "runtime_held_state_boundary", "result_version"
        ),
        "basis_runtime_held_state_boundary_failed_check_count": _basis_value(
            basis_infos, "runtime_held_state_boundary", "failed_check_count"
        ),
        "basis_runtime_artifact": _basis_path_value(basis_infos, "runtime"),
        "basis_runtime_outcome": _basis_value(basis_infos, "runtime", "outcome"),
        "basis_runtime_result_version": _basis_value(
            basis_infos, "runtime", "result_version"
        ),
        "basis_runtime_failed_check_count": _basis_value(
            basis_infos, "runtime", "failed_check_count"
        ),
        "basis_runtime_boundary_artifact": _basis_path_value(
            basis_infos, "runtime_boundary"
        ),
        "basis_runtime_boundary_outcome": _basis_value(
            basis_infos, "runtime_boundary", "outcome"
        ),
        "basis_runtime_boundary_result_version": _basis_value(
            basis_infos, "runtime_boundary", "result_version"
        ),
        "basis_runtime_boundary_failed_check_count": _basis_value(
            basis_infos, "runtime_boundary", "failed_check_count"
        ),
        "basis_runtime_permission_artifact": _basis_path_value(
            basis_infos, "runtime_permission"
        ),
        "basis_runtime_permission_outcome": _basis_value(
            basis_infos, "runtime_permission", "outcome"
        ),
        "basis_runtime_permission_result_version": _basis_value(
            basis_infos, "runtime_permission", "result_version"
        ),
        "basis_runtime_permission_failed_check_count": _basis_value(
            basis_infos, "runtime_permission", "failed_check_count"
        ),
        "basis_operation_execution_artifact": _basis_path_value(
            basis_infos, "operation_execution"
        ),
        "basis_operation_execution_outcome": _basis_value(
            basis_infos, "operation_execution", "outcome"
        ),
        "basis_operation_execution_result_version": _basis_value(
            basis_infos, "operation_execution", "result_version"
        ),
        "basis_operation_execution_failed_check_count": _basis_value(
            basis_infos, "operation_execution", "failed_check_count"
        ),
        "selected_command": SELECTED_COMMAND,
        "selected_command_is_state": recorded,
        "future_second_operation_may_be_considered": recorded,
    }
    for key, value in true_postures.items():
        boundary[key] = bool(recorded and value)
    for field in BOUNDARY_FALSE_FIELDS:
        boundary[field] = False
    return boundary


def _build_statement(
    basis_infos: Mapping[str, Mapping[str, Any]],
    boundary: Mapping[str, Any],
    recorded: bool,
) -> dict[str, Any]:
    statement: dict[str, Any] = {
        "local_relevance_medium_read_only_second_operation_boundary_recorded": recorded,
        "basis_prior_result_reentry_cycle_artifact_preserved": bool(
            basis_infos.get("prior_result_reentry_cycle", {}).get("artifact_preserved")
        ),
        "basis_prior_result_reentry_boundary_artifact_preserved": bool(
            basis_infos.get("prior_result_reentry_boundary", {}).get("artifact_preserved")
        ),
        "basis_runtime_held_reentry_artifact_preserved": bool(
            basis_infos.get("runtime_held_reentry", {}).get("artifact_preserved")
        ),
        "basis_runtime_held_reentry_boundary_artifact_preserved": bool(
            basis_infos.get("runtime_held_reentry_boundary", {}).get("artifact_preserved")
        ),
        "basis_runtime_held_state_artifact_preserved": bool(
            basis_infos.get("runtime_held_state", {}).get("artifact_preserved")
        ),
        "basis_runtime_held_state_boundary_artifact_preserved": bool(
            basis_infos.get("runtime_held_state_boundary", {}).get("artifact_preserved")
        ),
        "basis_runtime_artifact_preserved": bool(
            basis_infos.get("runtime", {}).get("artifact_preserved")
        ),
        "basis_runtime_boundary_artifact_preserved": bool(
            basis_infos.get("runtime_boundary", {}).get("artifact_preserved")
        ),
        "basis_runtime_permission_artifact_preserved": bool(
            basis_infos.get("runtime_permission", {}).get("artifact_preserved")
        ),
        "basis_operation_execution_artifact_preserved": bool(
            basis_infos.get("operation_execution", {}).get("artifact_preserved")
        ),
        "selected_command_preserved": boundary.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": boundary.get("selected_command_is_state") is True,
        "consumed_request_token_remains_closed": (
            boundary.get("consumed_request_reopened") is False
        ),
        "authorization_token_reuse_blocked": (
            boundary.get("authorization_token_reused") is False
        ),
        "predecessor_failure_evidence_preserved": (
            boundary.get("prior_result_cycle_v1_failure_evidence_preserved") is True
            and boundary.get("prior_result_boundary_v1_failure_evidence_preserved") is True
            and boundary.get("runtime_v0_failure_evidence_preserved") is True
            and boundary.get("runtime_v2_failure_evidence_preserved") is True
            and boundary.get("runtime_boundary_v0_failure_evidence_preserved") is True
        ),
        "result_level_non_claims_canonical_false": True,
    }
    for key in (
        "selected_prior_result_reentry_cycle_recorded",
        "prior_result_reentry_cycle_created",
        "prior_result_reentry_cycle_local_only",
        "prior_result_reentry_cycle_read_only",
        "cycle_basis_reference_only",
        "selected_prior_result_reentry_boundary_recorded",
        "future_prior_result_reentry_cycle_may_be_considered",
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
        "future_second_operation_may_be_considered",
        "runtime_v0_failure_evidence_preserved",
        "runtime_v2_failure_evidence_preserved",
        "runtime_boundary_v0_failure_evidence_preserved",
        "prior_result_boundary_v1_failure_evidence_preserved",
        "prior_result_boundary_v2_successor_evidence_preserved",
        "prior_result_cycle_v1_failure_evidence_preserved",
        "prior_result_cycle_v2_successor_evidence_preserved",
    ):
        statement[key] = boundary.get(key) is True
    for field in BOUNDARY_FALSE_FIELDS:
        statement[field] = False
        statement[f"{field}_not_created_or_not_performed"] = True
    return statement


def _build_non_meaning() -> dict[str, bool]:
    return {
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
        "raw_state_body_embedded": False,
        "state_mutation_performed": False,
        "state_update_performed": False,
        "older_runtime_lineage_imported_as_authority": False,
        "older_runtime_permission_treated_as_current": False,
        "runtime_authority_imported": False,
        "follow_on_work_authorized": False,
    }


def _empty_basis_infos() -> dict[str, dict[str, Any]]:
    infos: dict[str, dict[str, Any]] = {}
    for spec in BASIS_ARTIFACT_SPECS:
        infos[str(spec["name"])] = {
            "artifact_path": None,
            "artifact_readable": False,
            "artifact_json_object": False,
            "artifact_preserved": False,
            "outcome": None,
            "result_version": None,
            "failed_check_count": None,
        }
    return infos


def _build_result(
    request: Mapping[str, Any],
    basis_infos: Mapping[str, Mapping[str, Any]],
    checks: list[dict[str, Any]],
    true_postures: Mapping[str, bool] | None = None,
    forced_outcome: str | None = None,
) -> dict[str, Any]:
    true_postures = true_postures or {}
    failed = _failed_checks(checks)
    intent = request.get(
        "local_relevance_medium_read_only_second_operation_boundary_intent",
        INTENT_RECORD,
    )
    if forced_outcome is not None:
        outcome = forced_outcome
    elif failed:
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    else:
        outcome = OUTCOME_RECORDED
    recorded = outcome == OUTCOME_RECORDED
    boundary = _build_boundary_object(request, basis_infos, true_postures, recorded)
    block_code = _first_block_code(checks) if outcome == OUTCOME_BLOCKED else None
    block = (
        {
            "blocked": True,
            "code": block_code,
            "block_code": block_code,
            "reason": block_code,
        }
        if block_code
        else {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        }
    )
    statement = _build_statement(basis_infos, boundary, recorded)
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_second_operation_boundary_metadata": {
            "local_relevance_medium_read_only_second_operation_boundary_id": boundary[
                "boundary_id"
            ],
            "local_relevance_medium_read_only_second_operation_boundary_type": BOUNDARY_TYPE,
            "local_relevance_medium_read_only_second_operation_boundary_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_local_relevance_medium_read_only_second_operation_boundary_question": {
            "local_relevance_medium_read_only_second_operation_boundary_id": _sanitize_value(
                request.get(
                    "local_relevance_medium_read_only_second_operation_boundary_id",
                    DEFAULT_BOUNDARY_ID,
                )
            ),
            "question": _sanitize_value(
                request.get(
                    "local_relevance_medium_read_only_second_operation_boundary_question"
                )
            ),
            "intent": _sanitize_value(
                request.get(
                    "local_relevance_medium_read_only_second_operation_boundary_intent",
                    INTENT_RECORD,
                )
            ),
            "selected_command": _sanitize_value(request.get("selected_command")),
            "boundary_type": _sanitize_value(request.get("boundary_type")),
            "boundary_scope": _sanitize_value(request.get("boundary_scope")),
        },
        **_basis_sections_from_infos(basis_infos),
        "local_relevance_medium_read_only_second_operation_boundary": boundary,
        "local_relevance_medium_read_only_second_operation_boundary_checks": checks,
        "local_relevance_medium_read_only_second_operation_boundary_statement": statement,
        "local_relevance_medium_read_only_second_operation_boundary_non_meaning": _build_non_meaning(),
        "additional_basis_required": []
        if outcome != OUTCOME_REQUIRES_ADDITIONAL_BASIS
        else ["additional explicit basis required"],
        "not_recorded_basis": []
        if outcome != OUTCOME_NOT_RECORDED
        else ["declared intent did not record this boundary"],
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": len(failed),
    }
    result[
        "local_relevance_medium_read_only_second_operation_boundary_summary"
    ] = build_local_relevance_medium_read_only_second_operation_boundary_v0_min_summary(
        result
    )
    return _sanitize_value(result)


def _resolve_mapping(request: Mapping[str, Any]) -> dict[str, Any]:
    working_request = copy.deepcopy(dict(request))
    checks: list[dict[str, Any]] = []
    _validate_request_header(working_request, checks)
    _validate_top_level_false_fields(working_request, checks)
    _validate_declared_non_claims(working_request, checks)

    artifacts: dict[str, Mapping[str, Any]] = {}
    basis_infos = _empty_basis_infos()
    for spec in BASIS_ARTIFACT_SPECS:
        artifact, basis_info = _read_artifact(spec, working_request, checks)
        basis_infos[str(spec["name"])] = basis_info
        if artifact is not None:
            artifacts[str(spec["name"])] = artifact

    true_postures = _validate_true_postures(artifacts, checks)
    _validate_basis_false_postures(artifacts, checks)

    return _build_result(working_request, basis_infos, checks, true_postures)


def resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min(
    declared_local_relevance_medium_read_only_second_operation_boundary: Mapping[str, Any]
    | None = None,
) -> dict:
    """Resolve one bounded local read-only second-operation boundary."""

    if declared_local_relevance_medium_read_only_second_operation_boundary is None:
        request = build_declared_local_relevance_medium_read_only_second_operation_boundary_v0_min_request()
    else:
        request = declared_local_relevance_medium_read_only_second_operation_boundary
    if not _is_mapping(request):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_request_mapping",
            False,
            "mapping",
            type(request).__name__,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_REQUEST_MALFORMED",
        )
        return _build_result({}, _empty_basis_infos(), checks)
    return _resolve_mapping(request)


def resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_from_path(
    declared_local_relevance_medium_read_only_second_operation_boundary_path: Path | str,
) -> dict:
    """Read a declared second-operation-boundary request and resolve it."""

    try:
        with Path(declared_local_relevance_medium_read_only_second_operation_boundary_path).open(
            "r",
            encoding="utf-8",
        ) as request_file:
            request = json.load(request_file)
    except Exception as exc:  # noqa: BLE001 - converted into bounded block result.
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "declared_request_readable",
            False,
            "readable JSON request",
            f"{type(exc).__name__}: {exc}",
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_REQUEST_UNREADABLE",
        )
        return _build_result({}, _empty_basis_infos(), checks)
    if not _is_mapping(request):
        checks = []
        _add_check(
            checks,
            "declared_request_mapping",
            False,
            "JSON object request",
            type(request).__name__,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_REQUEST_MALFORMED",
        )
        return _build_result({}, _empty_basis_infos(), checks)
    return resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min(
        request
    )


def _path_is_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def _guard_output_path(path: Path) -> None:
    for forbidden_root in FORBIDDEN_OUTPUT_ROOTS:
        if _path_is_under(path, forbidden_root):
            raise LocalRelevanceMediumReadOnlySecondOperationBoundaryV0MinError(
                f"refusing to write second-operation-boundary result under {forbidden_root}"
            )


def _dedupe_output_path(path: Path) -> Path:
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


def write_local_relevance_medium_read_only_second_operation_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result as stable UTF-8 JSON without overwriting."""

    if not _is_mapping(result):
        raise LocalRelevanceMediumReadOnlySecondOperationBoundaryV0MinError(
            "result must be a mapping"
        )
    boundary = result.get("local_relevance_medium_read_only_second_operation_boundary")
    boundary_id = DEFAULT_BOUNDARY_ID
    if _is_mapping(boundary) and boundary.get("boundary_id"):
        boundary_id = str(boundary["boundary_id"])
    if output_path is None:
        path = OUTPUT_ROOT / (
            f"{boundary_id}__"
            "local_relevance_medium_read_only_second_operation_boundary_v0_min_result.json"
        )
    else:
        path = Path(output_path)
    _guard_output_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    target = _dedupe_output_path(path)
    with target.open("w", encoding="utf-8") as result_file:
        json.dump(_sanitize_value(dict(result)), result_file, indent=2, sort_keys=True)
        result_file.write("\n")
    return target


def build_local_relevance_medium_read_only_second_operation_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact summary for a second-operation-boundary result."""

    boundary = result.get("local_relevance_medium_read_only_second_operation_boundary")
    if not _is_mapping(boundary):
        boundary = {}
    checks = result.get("local_relevance_medium_read_only_second_operation_boundary_checks")
    if not isinstance(checks, list):
        checks = []
    failed_count = sum(1 for check in checks if _is_mapping(check) and check.get("passed") is not True)
    passed_count = sum(1 for check in checks if _is_mapping(check) and check.get("passed") is True)
    block = result.get("block")
    block_code = None
    block_reason = None
    if _is_mapping(block):
        block_code = block.get("code") or block.get("block_code")
        block_reason = block.get("reason")
    non_claims = result.get("non_claims")
    non_claims_canonical = (
        _is_mapping(non_claims)
        and all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)
    )
    summary = {
        "outcome": result.get("outcome"),
        "block_code": block_code,
        "block_reason": block_reason,
        "boundary_id": boundary.get("boundary_id"),
        "question": result.get(
            "declared_local_relevance_medium_read_only_second_operation_boundary_question",
            {},
        ).get("question")
        if _is_mapping(
            result.get(
                "declared_local_relevance_medium_read_only_second_operation_boundary_question"
            )
        )
        else None,
        "intent": result.get(
            "declared_local_relevance_medium_read_only_second_operation_boundary_question",
            {},
        ).get("intent")
        if _is_mapping(
            result.get(
                "declared_local_relevance_medium_read_only_second_operation_boundary_question"
            )
        )
        else None,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": result.get("result_version", RESULT_VERSION),
        "resolver_module": result.get("resolver_module", RESOLVER_MODULE),
        "boundary_recorded": result.get("outcome") == OUTCOME_RECORDED,
        "selected_command": boundary.get("selected_command"),
        "selected_command_preserved": boundary.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": boundary.get("selected_command_is_state") is True,
        "second_operation_not_created": boundary.get("second_operation_created") is False,
        "continuation_not_created": boundary.get("continuation_created") is False,
        "runtime_hosting_not_created": boundary.get("runtime_hosting_created") is False,
        "runtime_loop_not_created": boundary.get("runtime_loop_created") is False,
        "daemon_behavior_not_created": boundary.get("daemon_behavior_created") is False,
        "public_api_not_created": boundary.get("public_api_created") is False,
        "participant_facing_interface_not_created": (
            boundary.get("participant_facing_interface_created") is False
        ),
        "distributed_network_behavior_not_created": (
            boundary.get("distributed_network_behavior_created") is False
        ),
        "older_runtime_lineage_not_imported_as_authority": (
            boundary.get("older_runtime_lineage_imported_as_authority") is False
        ),
        "older_runtime_permission_not_treated_as_current": (
            boundary.get("older_runtime_permission_treated_as_current") is False
        ),
        "runtime_authority_not_imported": (
            boundary.get("runtime_authority_imported") is False
        ),
        "consumed_request_token_remains_closed": (
            boundary.get("consumed_request_reopened") is False
        ),
        "authorization_token_reuse_blocked": (
            boundary.get("authorization_token_reused") is False
        ),
        "predecessor_failure_evidence_preserved": (
            boundary.get("prior_result_cycle_v1_failure_evidence_preserved") is True
            and boundary.get("prior_result_boundary_v1_failure_evidence_preserved") is True
            and boundary.get("runtime_v0_failure_evidence_preserved") is True
            and boundary.get("runtime_v2_failure_evidence_preserved") is True
            and boundary.get("runtime_boundary_v0_failure_evidence_preserved") is True
        ),
        "result_level_non_claims_canonical_false": non_claims_canonical,
    }
    for key in (
        "selected_prior_result_reentry_cycle_recorded",
        "prior_result_reentry_cycle_created",
        "prior_result_reentry_cycle_local_only",
        "prior_result_reentry_cycle_read_only",
        "cycle_basis_reference_only",
        "selected_prior_result_reentry_boundary_recorded",
        "future_prior_result_reentry_cycle_may_be_considered",
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
        "raw_state_body_embedded",
        "state_mutation_performed",
        "state_update_performed",
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
        "future_second_operation_may_be_considered",
        "runtime_v0_failure_evidence_preserved",
        "runtime_v2_failure_evidence_preserved",
        "runtime_boundary_v0_failure_evidence_preserved",
        "prior_result_boundary_v1_failure_evidence_preserved",
        "prior_result_boundary_v2_successor_evidence_preserved",
        "prior_result_cycle_v1_failure_evidence_preserved",
        "prior_result_cycle_v2_successor_evidence_preserved",
    ):
        summary[key] = boundary.get(key)
    summary["failure_not_repaired_hidden_or_claimed_passed"] = (
        boundary.get("prior_result_cycle_v1_failure_repaired") is False
        and boundary.get("prior_result_cycle_v1_failure_hidden") is False
        and boundary.get("prior_result_cycle_v1_failure_claimed_passed") is False
        and boundary.get("prior_result_boundary_v1_failure_repaired") is False
        and boundary.get("prior_result_boundary_v1_failure_hidden") is False
        and boundary.get("prior_result_boundary_v1_failure_claimed_passed") is False
        and boundary.get("runtime_v0_failure_repaired") is False
        and boundary.get("runtime_v0_failure_hidden") is False
        and boundary.get("runtime_v0_failure_claimed_passed") is False
        and boundary.get("runtime_v2_failure_repaired") is False
        and boundary.get("runtime_v2_failure_hidden") is False
        and boundary.get("runtime_v2_failure_claimed_passed") is False
        and boundary.get("runtime_boundary_v0_failure_repaired") is False
        and boundary.get("runtime_boundary_v0_failure_hidden") is False
        and boundary.get("runtime_boundary_v0_failure_claimed_passed") is False
    )
    return _sanitize_value(summary)


def build_declared_local_relevance_medium_read_only_second_operation_boundary_v0_min_request(
    *,
    local_relevance_medium_read_only_second_operation_boundary_id: str = DEFAULT_BOUNDARY_ID,
    local_relevance_medium_read_only_second_operation_boundary_question: str = CORE_QUESTION,
    local_relevance_medium_read_only_second_operation_boundary_intent: str = INTENT_RECORD,
    selected_prior_result_reentry_cycle_artifact: Path | str = DEFAULT_PRIOR_RESULT_REENTRY_CYCLE_ARTIFACT,
    selected_prior_result_reentry_boundary_artifact: Path | str = DEFAULT_PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT,
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
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared request for the bounded second-operation boundary."""

    non_claims = _canonical_non_claims()
    if declared_non_claims is not None:
        non_claims.update(dict(declared_non_claims))
    request: dict[str, Any] = {
        "local_relevance_medium_read_only_second_operation_boundary_id": (
            local_relevance_medium_read_only_second_operation_boundary_id
        ),
        "local_relevance_medium_read_only_second_operation_boundary_question": (
            local_relevance_medium_read_only_second_operation_boundary_question
        ),
        "local_relevance_medium_read_only_second_operation_boundary_intent": (
            local_relevance_medium_read_only_second_operation_boundary_intent
        ),
        "selected_prior_result_reentry_cycle_artifact": str(
            selected_prior_result_reentry_cycle_artifact
        ),
        "selected_prior_result_reentry_boundary_artifact": str(
            selected_prior_result_reentry_boundary_artifact
        ),
        "selected_runtime_held_reentry_artifact": str(
            selected_runtime_held_reentry_artifact
        ),
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
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "future_second_operation_may_be_considered": True,
        "declared_non_claims": non_claims,
    }
    request.update(overrides)
    return _sanitize_value(request)
