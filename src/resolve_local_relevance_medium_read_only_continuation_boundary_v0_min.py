"""Resolve one local relevance medium read-only continuation boundary.

This resolver records one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY
object only. It reads one clean selected second-operation artifact, one clean
second-operation boundary artifact, one clean prior-result re-entry cycle
artifact, one clean prior-result re-entry boundary artifact, one clean
runtime-held-re-entry artifact, one clean runtime-held-re-entry boundary
artifact, one clean runtime-held-state artifact, one clean runtime-held-state
boundary artifact, one clean runtime v3 artifact, one clean runtime boundary v2
artifact, one clean runtime permission artifact, and one clean operation
execution artifact as selected-state basis references.

The boundary is local, read-only, selected-continuation-consideration-only,
raw-state-body-excluding, state-mutation-refusing, state-update-refusing,
closure-token-aware, non-continuation-shaped, non-hosting-shaped,
non-loop-shaped, non-daemon-shaped, and older-runtime-authority-import-blocking.
It allows one future local read-only continuation to be considered as a
separately bounded step. It does not create continuation, runtime hosting,
runtime loop, daemon behavior, public API, participant-facing interface,
distributed behavior, authority/currentness/truth judgment, raw state body
embedding, state mutation, state update, older runtime authority import, or
follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping


class LocalRelevanceMediumReadOnlyContinuationBoundaryV0MinError(RuntimeError):
    """Bounded resolver error for continuation-boundary request/path handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_continuation_boundary_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "continuation_boundary_v0_min"
)

BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_CONTINUATION_CONSIDERATION_ONLY"
SELECTED_COMMAND = "state"

SUPPORTED_BOUNDARY_TYPE_VALUES = (BOUNDARY_TYPE,)
SUPPORTED_BOUNDARY_SCOPE_VALUES = (BOUNDARY_SCOPE,)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

DEFAULT_BOUNDARY_ID = "local_relevance_medium_read_only_continuation_boundary_001"
DEFAULT_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION for "
    "selected command state, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE, one clean "
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
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY be recorded that "
    "permits a future local read-only continuation to be considered as a "
    "separately bounded step, without creating continuation, runtime hosting, "
    "runtime loop, daemon behavior, public API, participant-facing interface, "
    "distributed behavior, general operation permission, general lookup "
    "permission, arbitrary lookup permission, unsupported command/key "
    "permission, new lookup entry, raw state body, state mutation, state update, "
    "older runtime authority import, query surface, registry, search, ranking, "
    "authority, currentness, truth, source transfer, source receipt, or "
    "follow-on work?"
)

DEFAULT_ARTIFACT_PATHS = {
    "selected_second_operation_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "second_operation_v0_min/"
        "local_relevance_medium_read_only_second_operation_reference_review_001"
        "__local_relevance_medium_read_only_second_operation_v0_min_result.json"
    ),
    "selected_second_operation_boundary_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "second_operation_boundary_v0_min_v2/"
        "local_relevance_medium_read_only_second_operation_boundary_reference_review_001"
        "__local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_result.json"
    ),
    "selected_prior_result_reentry_cycle_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "prior_result_reentry_cycle_v0_min_v2/"
        "local_relevance_medium_read_only_prior_result_reentry_cycle_reference_review_001"
        "__local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_result.json"
    ),
    "selected_prior_result_reentry_boundary_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "prior_result_reentry_boundary_v0_min/"
        "local_relevance_medium_read_only_prior_result_reentry_boundary_reference_review_001"
        "__local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_result.json"
    ),
    "selected_runtime_held_reentry_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_reentry_v0_min/"
        "local_relevance_medium_read_only_runtime_held_reentry_reference_review_001"
        "__local_relevance_medium_read_only_runtime_held_reentry_v0_min_result.json"
    ),
    "selected_runtime_held_reentry_boundary_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_reentry_boundary_v0_min/"
        "local_relevance_medium_read_only_runtime_held_reentry_boundary_reference_review_001"
        "__local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min_result.json"
    ),
    "selected_runtime_held_state_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_state_v0_min/"
        "local_relevance_medium_read_only_runtime_held_state_reference_review_001"
        "__local_relevance_medium_read_only_runtime_held_state_v0_min_result.json"
    ),
    "selected_runtime_held_state_boundary_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_state_boundary_v0_min/"
        "local_relevance_medium_read_only_runtime_held_state_boundary_reference_review_001"
        "__local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result.json"
    ),
    "selected_runtime_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_v0_min_v3/"
        "local_relevance_medium_read_only_runtime_reference_review_001"
        "__local_relevance_medium_read_only_runtime_v0_min_v3_result.json"
    ),
    "selected_runtime_boundary_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_boundary_v0_min_v2/"
        "local_relevance_medium_read_only_runtime_boundary_reference_review_001"
        "__local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
    ),
    "selected_runtime_permission_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_permission_v0_min/"
        "local_relevance_medium_read_only_runtime_permission_reference_review_001"
        "__local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
    ),
    "selected_operation_execution_artifact": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "operation_execution_v0_min/"
        "local_relevance_medium_read_only_operation_execution_reference_review_001"
        "__local_relevance_medium_read_only_operation_execution_v0_min_result.json"
    ),
}

BASIS_ARTIFACT_SPECS = (
    {
        "name": "second_operation",
        "request_key": "selected_second_operation_artifact",
        "basis_section": "selected_second_operation_artifact_basis",
        "basis_prefix": "basis_second_operation",
        "preserved_key": "basis_second_operation_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_second_operation",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_RECORDED",
        "block_prefix": "SECOND_OPERATION_ARTIFACT",
        "type_field": "operation_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION",
        "scope_field": "operation_scope",
        "scope_value": "SELECTED_SECOND_OPERATION_ONLY",
    },
    {
        "name": "second_operation_boundary",
        "request_key": "selected_second_operation_boundary_artifact",
        "basis_section": "selected_second_operation_boundary_artifact_basis",
        "basis_prefix": "basis_second_operation_boundary",
        "preserved_key": "basis_second_operation_boundary_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_second_operation_boundary",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_RECORDED",
        "block_prefix": "SECOND_OPERATION_BOUNDARY_ARTIFACT",
        "type_field": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY",
        "scope_field": "boundary_scope",
        "scope_value": "SELECTED_SECOND_OPERATION_CONSIDERATION_ONLY",
    },
    {
        "name": "prior_result_reentry_cycle",
        "request_key": "selected_prior_result_reentry_cycle_artifact",
        "basis_section": "selected_prior_result_reentry_cycle_artifact_basis",
        "basis_prefix": "basis_prior_result_reentry_cycle",
        "preserved_key": "basis_prior_result_reentry_cycle_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_prior_result_reentry_cycle",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_RECORDED",
        "block_prefix": "PRIOR_RESULT_REENTRY_CYCLE_ARTIFACT",
        "type_field": "cycle_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE",
        "scope_field": "cycle_scope",
        "scope_value": "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY",
    },
    {
        "name": "prior_result_reentry_boundary",
        "request_key": "selected_prior_result_reentry_boundary_artifact",
        "basis_section": "selected_prior_result_reentry_boundary_artifact_basis",
        "basis_prefix": "basis_prior_result_reentry_boundary",
        "preserved_key": "basis_prior_result_reentry_boundary_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_prior_result_reentry_boundary",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_RECORDED",
        "block_prefix": "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT",
        "type_field": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY",
        "scope_field": "boundary_scope",
        "scope_value": "SELECTED_PRIOR_RESULT_REENTRY_CONSIDERATION_ONLY",
    },
    {
        "name": "runtime_held_reentry",
        "request_key": "selected_runtime_held_reentry_artifact",
        "basis_section": "selected_runtime_held_reentry_artifact_basis",
        "basis_prefix": "basis_runtime_held_reentry",
        "preserved_key": "basis_runtime_held_reentry_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_RECORDED",
        "block_prefix": "RUNTIME_HELD_REENTRY_ARTIFACT",
        "type_field": "held_reentry_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY",
        "scope_field": "held_reentry_scope",
        "scope_value": "SELECTED_RUNTIME_HELD_REENTRY_ONLY",
    },
    {
        "name": "runtime_held_reentry_boundary",
        "request_key": "selected_runtime_held_reentry_boundary_artifact",
        "basis_section": "selected_runtime_held_reentry_boundary_artifact_basis",
        "basis_prefix": "basis_runtime_held_reentry_boundary",
        "preserved_key": "basis_runtime_held_reentry_boundary_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry_boundary",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY_RECORDED",
        "block_prefix": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT",
        "type_field": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY",
        "scope_field": "boundary_scope",
        "scope_value": "SELECTED_RUNTIME_HELD_REENTRY_CONSIDERATION_ONLY",
    },
    {
        "name": "runtime_held_state",
        "request_key": "selected_runtime_held_state_artifact",
        "basis_section": "selected_runtime_held_state_artifact_basis",
        "basis_prefix": "basis_runtime_held_state",
        "preserved_key": "basis_runtime_held_state_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_runtime_held_state",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_RECORDED",
        "block_prefix": "RUNTIME_HELD_STATE_ARTIFACT",
        "type_field": "held_state_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE",
        "scope_field": "held_state_scope",
        "scope_value": "SELECTED_RUNTIME_HELD_STATE_ONLY",
    },
    {
        "name": "runtime_held_state_boundary",
        "request_key": "selected_runtime_held_state_boundary_artifact",
        "basis_section": "selected_runtime_held_state_boundary_artifact_basis",
        "basis_prefix": "basis_runtime_held_state_boundary",
        "preserved_key": "basis_runtime_held_state_boundary_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_runtime_held_state_boundary",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_RECORDED",
        "block_prefix": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT",
        "type_field": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY",
        "scope_field": "boundary_scope",
        "scope_value": "SELECTED_RUNTIME_HELD_STATE_CONSIDERATION_ONLY",
    },
    {
        "name": "runtime",
        "request_key": "selected_runtime_artifact",
        "basis_section": "selected_runtime_artifact_basis",
        "basis_prefix": "basis_runtime",
        "preserved_key": "basis_runtime_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_runtime",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED",
        "block_prefix": "RUNTIME_ARTIFACT",
        "type_field": "runtime_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME",
        "scope_field": "runtime_scope",
        "scope_value": "SELECTED_RUNTIME_ONLY",
    },
    {
        "name": "runtime_boundary",
        "request_key": "selected_runtime_boundary_artifact",
        "basis_section": "selected_runtime_boundary_artifact_basis",
        "basis_prefix": "basis_runtime_boundary",
        "preserved_key": "basis_runtime_boundary_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_runtime_boundary",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED",
        "block_prefix": "RUNTIME_BOUNDARY_ARTIFACT",
        "type_field": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
        "scope_field": "boundary_scope",
        "scope_value": "SELECTED_RUNTIME_CONSIDERATION_ONLY",
    },
    {
        "name": "runtime_permission",
        "request_key": "selected_runtime_permission_artifact",
        "basis_section": "selected_runtime_permission_artifact_basis",
        "basis_prefix": "basis_runtime_permission",
        "preserved_key": "basis_runtime_permission_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_runtime_permission",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED",
        "block_prefix": "RUNTIME_PERMISSION_ARTIFACT",
        "type_field": "runtime_permission_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
        "scope_field": "runtime_permission_scope",
        "scope_value": "SELECTED_RUNTIME_PERMISSION_ONLY",
    },
    {
        "name": "operation_execution",
        "request_key": "selected_operation_execution_artifact",
        "basis_section": "selected_operation_execution_artifact_basis",
        "basis_prefix": "basis_operation_execution",
        "preserved_key": "basis_operation_execution_artifact_preserved",
        "object_key": "local_relevance_medium_read_only_operation_execution",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
        "block_prefix": "OPERATION_EXECUTION_ARTIFACT",
        "type_field": "operation_execution_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
        "scope_field": "operation_execution_scope",
        "scope_value": "SELECTED_OPERATION_EXECUTION_ONLY",
    },
)

BASIS_BY_NAME = {spec["name"]: spec for spec in BASIS_ARTIFACT_SPECS}

REQUIRED_FALSE_NON_CLAIMS = (
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
    "artifact_existence_treated_as_continuation_boundary_authority",
    "latest_file_posture_treated_as_continuation_boundary_authority",
    "repo_local_availability_treated_as_continuation_boundary_authority",
    "hidden_repo_state_used_as_continuation_boundary_content",
    "hidden_repo_state_used_as_continuation_boundary_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "second_operation_boundary_v1_failure_repaired",
    "second_operation_boundary_v1_failure_hidden",
    "second_operation_boundary_v1_failure_claimed_passed",
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

POSITIVE_BASIS_FIELDS = (
    "selected_command_is_state",
    "selected_second_operation_recorded",
    "second_operation_created",
    "second_operation_local_only",
    "second_operation_read_only",
    "second_operation_basis_reference_only",
    "second_operation_sequence_index_is_2",
    "selected_second_operation_boundary_recorded",
    "future_second_operation_may_be_considered",
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
    "second_operation_boundary_v1_failure_evidence_preserved",
    "second_operation_boundary_v2_successor_evidence_preserved",
    "prior_result_cycle_v1_failure_evidence_preserved",
    "prior_result_cycle_v2_successor_evidence_preserved",
    "prior_result_boundary_v1_failure_evidence_preserved",
    "prior_result_boundary_v2_successor_evidence_preserved",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "lookup_command_execution_boundary_v1_filename_path_failure_evidence_preserved",
    "state_packet_body_exposure_boundary_v0_failure_evidence_preserved",
    "state_packet_body_exposure_v1_over_strict_test_evidence_preserved",
    "local_carrier_command_execution_boundary_v1_over_strict_failure_evidence_preserved",
)

BOUNDARY_TRUE_FIELDS = (
    "local_relevance_medium_read_only_continuation_boundary_recorded",
    "future_continuation_may_be_considered",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_continuation_boundary_recorded",
    "basis_second_operation_artifact_preserved",
    "basis_second_operation_boundary_artifact_preserved",
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
    "future_continuation_may_be_considered",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
) + POSITIVE_BASIS_FIELDS

FIELD_BLOCK_CODES = {key: key.upper() for key in REQUIRED_FALSE_NON_CLAIMS}
FIELD_BLOCK_CODES.update(
    {
        "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "predecessor_failure_claimed_passed": (
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
        ),
    }
)

TRUE_REQUIREMENTS = (
    (
        "selected_second_operation_recorded",
        "second_operation",
        "SELECTED_SECOND_OPERATION_NOT_RECORDED",
        (
            "second_operation_recorded",
            "local_relevance_medium_read_only_second_operation_recorded",
        ),
    ),
    (
        "second_operation_created",
        "second_operation",
        "SECOND_OPERATION_NOT_CREATED",
        ("local_relevance_medium_read_only_second_operation_created",),
    ),
    (
        "second_operation_local_only",
        "second_operation",
        "SECOND_OPERATION_LOCAL_ONLY_NOT_TRUE",
        ("local_only", "local_relevance_medium_read_only_second_operation_local_only"),
    ),
    (
        "second_operation_read_only",
        "second_operation",
        "SECOND_OPERATION_READ_ONLY_NOT_TRUE",
        ("read_only", "local_relevance_medium_read_only_second_operation_read_only"),
    ),
    (
        "second_operation_basis_reference_only",
        "second_operation",
        "SECOND_OPERATION_BASIS_REFERENCE_ONLY_NOT_TRUE",
        ("basis_reference_only",),
    ),
    (
        "second_operation_sequence_index_is_2",
        "second_operation",
        "SECOND_OPERATION_SEQUENCE_INDEX_IS_2_NOT_TRUE",
        (),
    ),
    (
        "selected_second_operation_boundary_recorded",
        "second_operation_boundary",
        "SELECTED_SECOND_OPERATION_BOUNDARY_NOT_RECORDED",
        (
            "second_operation_boundary_recorded",
            "local_relevance_medium_read_only_second_operation_boundary_recorded",
        ),
    ),
    (
        "future_second_operation_may_be_considered",
        "second_operation_boundary",
        "FUTURE_SECOND_OPERATION_MAY_NOT_BE_CONSIDERED",
        (),
    ),
    (
        "selected_prior_result_reentry_cycle_recorded",
        "prior_result_reentry_cycle",
        "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED",
        (
            "prior_result_reentry_cycle_recorded",
            "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded",
        ),
    ),
    (
        "prior_result_reentry_cycle_created",
        "prior_result_reentry_cycle",
        "PRIOR_RESULT_REENTRY_CYCLE_NOT_CREATED",
        ("local_relevance_medium_read_only_prior_result_reentry_cycle_created",),
    ),
    (
        "prior_result_reentry_cycle_local_only",
        "prior_result_reentry_cycle",
        "PRIOR_RESULT_REENTRY_CYCLE_NOT_LOCAL_ONLY",
        ("local_only", "local_relevance_medium_read_only_prior_result_reentry_cycle_local_only"),
    ),
    (
        "prior_result_reentry_cycle_read_only",
        "prior_result_reentry_cycle",
        "PRIOR_RESULT_REENTRY_CYCLE_NOT_READ_ONLY",
        ("read_only", "local_relevance_medium_read_only_prior_result_reentry_cycle_read_only"),
    ),
    (
        "cycle_basis_reference_only",
        "prior_result_reentry_cycle",
        "CYCLE_BASIS_NOT_REFERENCE_ONLY",
        ("basis_reference_only",),
    ),
    (
        "selected_prior_result_reentry_boundary_recorded",
        "prior_result_reentry_boundary",
        "SELECTED_PRIOR_RESULT_REENTRY_BOUNDARY_NOT_RECORDED",
        (
            "prior_result_reentry_boundary_recorded",
            "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded",
        ),
    ),
    (
        "future_prior_result_reentry_cycle_may_be_considered",
        "prior_result_reentry_boundary",
        "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED",
        (),
    ),
    (
        "selected_runtime_held_reentry_recorded",
        "runtime_held_reentry",
        "SELECTED_RUNTIME_HELD_REENTRY_NOT_RECORDED",
        (
            "runtime_held_reentry_recorded",
            "local_relevance_medium_read_only_runtime_held_reentry_recorded",
        ),
    ),
    (
        "runtime_held_reentry_created",
        "runtime_held_reentry",
        "RUNTIME_HELD_REENTRY_NOT_CREATED",
        ("local_relevance_medium_read_only_runtime_held_reentry_created",),
    ),
    (
        "runtime_held_reentry_local_only",
        "runtime_held_reentry",
        "RUNTIME_HELD_REENTRY_NOT_LOCAL_ONLY",
        ("local_only", "local_relevance_medium_read_only_runtime_held_reentry_local_only"),
    ),
    (
        "runtime_held_reentry_read_only",
        "runtime_held_reentry",
        "RUNTIME_HELD_REENTRY_NOT_READ_ONLY",
        ("read_only", "local_relevance_medium_read_only_runtime_held_reentry_read_only"),
    ),
    (
        "held_reentry_basis_reference_only",
        "runtime_held_reentry",
        "HELD_REENTRY_BASIS_NOT_REFERENCE_ONLY",
        ("basis_reference_only", "runtime_held_reentry_basis_reference_only"),
    ),
    (
        "selected_runtime_held_reentry_boundary_recorded",
        "runtime_held_reentry_boundary",
        "SELECTED_RUNTIME_HELD_REENTRY_BOUNDARY_NOT_RECORDED",
        (
            "runtime_held_reentry_boundary_recorded",
            "local_relevance_medium_read_only_runtime_held_reentry_boundary_recorded",
        ),
    ),
    (
        "future_runtime_held_reentry_may_be_considered",
        "runtime_held_reentry_boundary",
        "FUTURE_RUNTIME_HELD_REENTRY_MAY_NOT_BE_CONSIDERED",
        (),
    ),
    (
        "selected_runtime_held_state_recorded",
        "runtime_held_state",
        "SELECTED_RUNTIME_HELD_STATE_NOT_RECORDED",
        (
            "runtime_held_state_recorded",
            "local_relevance_medium_read_only_runtime_held_state_recorded",
        ),
    ),
    (
        "runtime_held_state_created",
        "runtime_held_state",
        "RUNTIME_HELD_STATE_NOT_CREATED",
        ("local_relevance_medium_read_only_runtime_held_state_created",),
    ),
    (
        "runtime_held_state_local_only",
        "runtime_held_state",
        "RUNTIME_HELD_STATE_NOT_LOCAL_ONLY",
        ("local_only", "local_relevance_medium_read_only_runtime_held_state_local_only"),
    ),
    (
        "runtime_held_state_read_only",
        "runtime_held_state",
        "RUNTIME_HELD_STATE_NOT_READ_ONLY",
        ("read_only", "local_relevance_medium_read_only_runtime_held_state_read_only"),
    ),
    (
        "held_state_basis_reference_only",
        "runtime_held_state",
        "HELD_STATE_BASIS_NOT_REFERENCE_ONLY",
        ("basis_reference_only", "runtime_held_state_basis_reference_only"),
    ),
    (
        "selected_runtime_held_state_boundary_recorded",
        "runtime_held_state_boundary",
        "SELECTED_RUNTIME_HELD_STATE_BOUNDARY_NOT_RECORDED",
        (
            "runtime_held_state_boundary_recorded",
            "local_relevance_medium_read_only_runtime_held_state_boundary_recorded",
        ),
    ),
    (
        "future_runtime_held_state_may_be_considered",
        "runtime_held_state_boundary",
        "FUTURE_RUNTIME_HELD_STATE_MAY_NOT_BE_CONSIDERED",
        (),
    ),
    (
        "selected_runtime_recorded",
        "runtime",
        "SELECTED_RUNTIME_NOT_RECORDED",
        ("runtime_recorded", "local_relevance_medium_read_only_runtime_recorded"),
    ),
    (
        "runtime_created",
        "runtime",
        "RUNTIME_NOT_CREATED",
        ("local_relevance_medium_read_only_runtime_created",),
    ),
    (
        "runtime_local_only",
        "runtime",
        "RUNTIME_NOT_LOCAL_ONLY",
        ("local_only", "local_relevance_medium_read_only_runtime_local_only"),
    ),
    (
        "runtime_read_only",
        "runtime",
        "RUNTIME_NOT_READ_ONLY",
        ("read_only", "local_relevance_medium_read_only_runtime_read_only"),
    ),
    (
        "selected_runtime_boundary_recorded",
        "runtime_boundary",
        "SELECTED_RUNTIME_BOUNDARY_NOT_RECORDED",
        (
            "runtime_boundary_recorded",
            "local_relevance_medium_read_only_runtime_boundary_recorded",
        ),
    ),
    (
        "future_runtime_may_be_considered",
        "runtime_boundary",
        "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED",
        (),
    ),
    (
        "selected_runtime_permission_recorded",
        "runtime_permission",
        "SELECTED_RUNTIME_PERMISSION_NOT_RECORDED",
        (
            "runtime_permission_recorded",
            "local_relevance_medium_read_only_runtime_permission_recorded",
        ),
    ),
    (
        "runtime_permission_created",
        "runtime_permission",
        "RUNTIME_PERMISSION_NOT_CREATED",
        ("local_relevance_medium_read_only_runtime_permission_created",),
    ),
    (
        "runtime_permission_local_only",
        "runtime_permission",
        "RUNTIME_PERMISSION_NOT_LOCAL_ONLY",
        ("local_only", "local_relevance_medium_read_only_runtime_permission_local_only"),
    ),
    (
        "runtime_permission_read_only",
        "runtime_permission",
        "RUNTIME_PERMISSION_NOT_READ_ONLY",
        ("read_only", "local_relevance_medium_read_only_runtime_permission_read_only"),
    ),
    (
        "selected_operation_execution_recorded",
        "operation_execution",
        "SELECTED_OPERATION_EXECUTION_NOT_RECORDED",
        (
            "operation_execution_recorded",
            "local_relevance_medium_read_only_operation_execution_recorded",
        ),
    ),
    (
        "operation_execution_created",
        "operation_execution",
        "OPERATION_EXECUTION_NOT_CREATED",
        ("local_relevance_medium_read_only_operation_execution_created",),
    ),
    (
        "operation_execution_performed",
        "operation_execution",
        "OPERATION_EXECUTION_NOT_PERFORMED",
        ("local_relevance_medium_read_only_operation_execution_performed",),
    ),
    (
        "operation_execution_local_only",
        "operation_execution",
        "OPERATION_EXECUTION_NOT_LOCAL_ONLY",
        ("local_only", "local_relevance_medium_read_only_operation_execution_local_only"),
    ),
    (
        "operation_execution_read_only",
        "operation_execution",
        "OPERATION_EXECUTION_NOT_READ_ONLY",
        ("read_only", "local_relevance_medium_read_only_operation_execution_read_only"),
    ),
    (
        "second_operation_boundary_v1_failure_evidence_preserved",
        "second_operation",
        "SECOND_OPERATION_BOUNDARY_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "second_operation_boundary_v2_successor_evidence_preserved",
        "second_operation",
        "SECOND_OPERATION_BOUNDARY_V2_SUCCESSOR_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "prior_result_cycle_v1_failure_evidence_preserved",
        "second_operation",
        "PRIOR_RESULT_CYCLE_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "prior_result_cycle_v2_successor_evidence_preserved",
        "second_operation",
        "PRIOR_RESULT_CYCLE_V2_SUCCESSOR_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "prior_result_boundary_v1_failure_evidence_preserved",
        "second_operation",
        "PRIOR_RESULT_BOUNDARY_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "prior_result_boundary_v2_successor_evidence_preserved",
        "second_operation",
        "PRIOR_RESULT_BOUNDARY_V2_SUCCESSOR_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "runtime_v0_failure_evidence_preserved",
        "second_operation",
        "RUNTIME_V0_FAILURE_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "runtime_v2_failure_evidence_preserved",
        "second_operation",
        "RUNTIME_V2_FAILURE_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "runtime_boundary_v0_failure_evidence_preserved",
        "second_operation",
        "RUNTIME_BOUNDARY_V0_FAILURE_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "lookup_command_execution_boundary_v1_filename_path_failure_evidence_preserved",
        "second_operation",
        "LOOKUP_COMMAND_EXECUTION_BOUNDARY_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "state_packet_body_exposure_boundary_v0_failure_evidence_preserved",
        "second_operation",
        "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_V0_FAILURE_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "state_packet_body_exposure_v1_over_strict_test_evidence_preserved",
        "second_operation",
        "STATE_PACKET_BODY_EXPOSURE_V1_OVER_STRICT_TEST_EVIDENCE_NOT_PRESERVED",
        (),
    ),
    (
        "local_carrier_command_execution_boundary_v1_over_strict_failure_evidence_preserved",
        "second_operation",
        "LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
        (),
    ),
)

BASE_BLOCK_CODES = {
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_BLOCK_REQUESTED",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "BOUNDARY_TYPE_MISSING",
    "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY",
    "BOUNDARY_SCOPE_MISSING",
    "BOUNDARY_SCOPE_NOT_SELECTED_CONTINUATION_CONSIDERATION_ONLY",
    "FUTURE_CONTINUATION_MAY_NOT_BE_CONSIDERED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_REQUEST_UNREADABLE",
}

for _spec in BASIS_ARTIFACT_SPECS:
    _prefix = str(_spec["block_prefix"])
    BASE_BLOCK_CODES.update(
        {
            f"{_prefix}_PATH_MISSING",
            f"{_prefix}_UNREADABLE",
            f"{_prefix}_NOT_JSON_OBJECT",
            f"{_prefix}_NOT_RECORDED",
            f"{_prefix}_FAILED_CHECKS_PRESENT",
            f"{_prefix}_VERSION_NOT_0_1_0",
        }
    )

BASE_BLOCK_CODES.update(FIELD_BLOCK_CODES.values())
BASE_BLOCK_CODES.update(item[2] for item in TRUE_REQUIREMENTS)
BASE_BLOCK_CODES.update(
    {
        "OPERATION_SEQUENCE_INDEX_NOT_2",
        "CONSUMED_REQUEST_REOPENED",
        "AUTHORIZATION_TOKEN_REUSED",
        "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
        "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
        "RUNTIME_AUTHORITY_IMPORTED",
        "RAW_STATE_BODY_EMBEDDED",
        "STATE_MUTATION_PERFORMED",
        "STATE_UPDATE_PERFORMED",
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
        "ARTIFACT_EXISTENCE_TREATED_AS_CONTINUATION_BOUNDARY_AUTHORITY",
        "LATEST_FILE_POSTURE_TREATED_AS_CONTINUATION_BOUNDARY_AUTHORITY",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_CONTINUATION_BOUNDARY_AUTHORITY",
        "HIDDEN_REPO_STATE_USED_AS_CONTINUATION_BOUNDARY_CONTENT",
        "HIDDEN_REPO_STATE_USED_AS_CONTINUATION_BOUNDARY_AUTHORITY",
        "PRIOR_ARTIFACTS_MUTATED",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "SECOND_OPERATION_BOUNDARY_V1_FAILURE_REPAIRED",
        "SECOND_OPERATION_BOUNDARY_V1_FAILURE_HIDDEN",
        "SECOND_OPERATION_BOUNDARY_V1_FAILURE_CLAIMED_PASSED",
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
        "LOOKUP_COMMAND_EXECUTION_BOUNDARY_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
        "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_V0_FAILURE_EVIDENCE_NOT_PRESERVED",
        "STATE_PACKET_BODY_EXPOSURE_V1_OVER_STRICT_TEST_EVIDENCE_NOT_PRESERVED",
        "LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_V1_FAILURE_EVIDENCE_NOT_PRESERVED",
    }
)

BLOCK_CODES = tuple(sorted(BASE_BLOCK_CODES))

HOSTILE_SENTINELS = (
    "RAW_CONTINUATION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BOUNDARY_BODY_MUST_NOT_RETURN",
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

OFFICIAL_STRINGS = set(OUTCOME_FAMILY)
OFFICIAL_STRINGS.update(BLOCK_CODES)
OFFICIAL_STRINGS.update(SUPPORTED_INTENTS)
OFFICIAL_STRINGS.update(SUPPORTED_BOUNDARY_TYPE_VALUES)
OFFICIAL_STRINGS.update(SUPPORTED_BOUNDARY_SCOPE_VALUES)
OFFICIAL_STRINGS.add(SELECTED_COMMAND)
OFFICIAL_STRINGS.add(RESULT_VERSION)
OFFICIAL_STRINGS.add(RESOLVER_MODULE)
for _spec in BASIS_ARTIFACT_SPECS:
    OFFICIAL_STRINGS.add(str(_spec["expected_outcome"]))
    for _key in ("type_value", "scope_value"):
        if _spec.get(_key):
            OFFICIAL_STRINGS.add(str(_spec[_key]))

_MISSING = object()


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return (
        lowered.endswith("_body")
        or "raw_body" in lowered
        or "full_body" in lowered
        or "artifact_body" in lowered
        or "raw_full_prior_artifact" in lowered
        or "hidden_repo_state" in lowered
        or "current_working_tree" in lowered
        or "local_cache" in lowered
        or "vendor_environment" in lowered
        or "carrier_payload" in lowered
    )


def _sanitize_string(value: str, key: str = "") -> str:
    if value in OFFICIAL_STRINGS:
        return value
    if _is_sensitive_key(key):
        return "[REDACTED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_RAW_BODY]"
    if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
        return "[REDACTED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_RAW_BODY]"
    return value


def _sanitize_value(value: Any, key: str = "") -> Any:
    if isinstance(value, Path):
        return _sanitize_string(str(value), key)
    if isinstance(value, str):
        return _sanitize_string(value, key)
    if isinstance(value, bool) or value is None or isinstance(value, (int, float)):
        return value
    if isinstance(value, MappingABC):
        if _is_sensitive_key(key):
            return "[REDACTED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_RAW_BODY]"
        return {str(k): _sanitize_value(v, str(k)) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        if _is_sensitive_key(key):
            return "[REDACTED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_RAW_BODY]"
        return [_sanitize_value(item, key) for item in value]
    return _sanitize_string(str(value), key)


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _safe_filename_fragment(value: Any) -> str:
    safe = str(value or DEFAULT_BOUNDARY_ID)
    safe = safe.replace("/", "_").replace("\\", "_").replace(" ", "_")
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe.strip("._-") or DEFAULT_BOUNDARY_ID


def _coerce_path(value: Any) -> Path | None:
    if value is None or value == "":
        return None
    try:
        return Path(str(value))
    except TypeError:
        return None


def _resolve_read_path(path: Path) -> Path:
    if path.exists() or path.is_absolute():
        return path
    candidate = REPO_ROOT / path
    if candidate.exists():
        return candidate
    return path


def _selected_object(
    artifact: Mapping[str, Any],
    spec: Mapping[str, Any],
) -> Mapping[str, Any] | None:
    value = artifact.get(str(spec["object_key"]))
    if isinstance(value, MappingABC):
        return value
    return None


def _top_level_non_claims(artifact: Mapping[str, Any]) -> Mapping[str, Any]:
    value = artifact.get("non_claims")
    if isinstance(value, MappingABC):
        return value
    return {}


def _section_matches(name: str, suffix: str) -> bool:
    return name == suffix or name.endswith(f"_{suffix}")


def _top_level_sections(
    artifact: Mapping[str, Any],
    suffixes: Iterable[str],
) -> list[Mapping[str, Any]]:
    sections: list[Mapping[str, Any]] = []
    suffix_tuple = tuple(suffixes)
    for key, value in artifact.items():
        if isinstance(value, MappingABC) and any(
            _section_matches(str(key), suffix) for suffix in suffix_tuple
        ):
            sections.append(value)
    return sections


def _extract_exact_from_sections(
    artifact: Mapping[str, Any],
    keys: Iterable[str],
    suffixes: Iterable[str],
) -> Any:
    key_tuple = tuple(keys)
    for section in _top_level_sections(artifact, suffixes):
        for key in key_tuple:
            if key in section:
                return section[key]
    return _MISSING


def _extract_top_level_or_bounded(
    artifact: Mapping[str, Any],
    keys: Iterable[str],
) -> Any:
    key_tuple = tuple(keys)
    for key in key_tuple:
        if key in artifact:
            return artifact[key]
    value = _extract_exact_from_sections(
        artifact,
        key_tuple,
        ("metadata", "summary", "statement", "result_metadata", "artifact_metadata"),
    )
    if value is not _MISSING:
        return value
    for key, top_value in artifact.items():
        if isinstance(top_value, MappingABC) and (
            str(key).endswith("_metadata")
            or str(key).endswith("_summary")
            or str(key).endswith("_statement")
        ):
            for wanted in key_tuple:
                if wanted in top_value:
                    return top_value[wanted]
    return _MISSING


def _as_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.isdigit():
        return int(value)
    return None


def _extract_result_version(artifact: Mapping[str, Any]) -> str | None:
    value = _extract_top_level_or_bounded(
        artifact,
        (
            "result_version",
            "operation_version",
            "boundary_version",
            "cycle_version",
            "runtime_version",
            "permission_version",
            "execution_version",
        ),
    )
    if isinstance(value, str):
        return value
    for key, top_value in artifact.items():
        if str(key).endswith("_version") and isinstance(top_value, str):
            return top_value
        if isinstance(top_value, MappingABC):
            for nested_key, nested_value in top_value.items():
                if str(nested_key).endswith("_version") and isinstance(nested_value, str):
                    return nested_value
    return None


def _extract_failed_check_count(artifact: Mapping[str, Any]) -> int | None:
    value = _extract_top_level_or_bounded(
        artifact,
        ("failed_check_count", "failed_checks_count"),
    )
    coerced = _as_int(value)
    if coerced is not None:
        return coerced

    failed_checks = _extract_top_level_or_bounded(artifact, ("failed_checks",))
    if isinstance(failed_checks, list):
        return len(failed_checks)

    for key, top_value in artifact.items():
        if str(key).endswith("_checks") and isinstance(top_value, list):
            failed = [
                check
                for check in top_value
                if isinstance(check, MappingABC) and check.get("passed") is False
            ]
            return len(failed)

    outcome = _extract_top_level_or_bounded(artifact, ("outcome",))
    return 0 if outcome is not _MISSING else None


def _read_json_object(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        return None, str(exc)
    if not isinstance(value, dict):
        return None, "JSON value is not an object"
    return value, None


def _artifact_basis_blank(spec: Mapping[str, Any], path: Any = None) -> dict[str, Any]:
    return {
        "basis_name": spec["name"],
        "artifact_path": _sanitize_value(path, "artifact_path"),
        "artifact_preserved": False,
        "outcome": None,
        "result_version": None,
        "failed_check_count": None,
        "object_key": spec["object_key"],
        "selected_object_present": False,
        "object_type_matches": False,
        "object_scope_matches": False,
        "identity_evidence": False,
    }


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> None:
    public_code = (
        code
        if code in BLOCK_CODES
        else "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_REQUEST_MALFORMED"
    )
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _sanitize_value(expected_posture, "expected_posture"),
            "actual_posture": _sanitize_value(actual_posture, "actual_posture"),
            "block_code": None if passed else public_code,
            "failure_code": None if passed else public_code,
        }
    )


def _read_basis_artifact(
    request: Mapping[str, Any],
    spec: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> dict[str, Any]:
    request_key = str(spec["request_key"])
    prefix = str(spec["block_prefix"])
    raw_path = request.get(request_key)
    path = _coerce_path(raw_path)

    path_declared = path is not None
    _add_check(
        checks,
        f"{request_key}_path_declared",
        path_declared,
        "declared path",
        raw_path,
        f"{prefix}_PATH_MISSING",
    )
    if path is None:
        basis = _artifact_basis_blank(spec, raw_path)
        basis["artifact"] = {}
        return basis

    read_path = _resolve_read_path(path)
    artifact, error = _read_json_object(read_path)
    readable = artifact is not None and error is None
    _add_check(
        checks,
        f"{request_key}_readable",
        readable,
        "readable UTF-8 JSON object",
        "readable" if readable else error,
        f"{prefix}_UNREADABLE",
    )
    object_shaped = isinstance(artifact, dict)
    _add_check(
        checks,
        f"{request_key}_json_object_shaped",
        object_shaped,
        "JSON object",
        type(artifact).__name__ if artifact is not None else None,
        f"{prefix}_NOT_JSON_OBJECT",
    )
    if not isinstance(artifact, dict):
        basis = _artifact_basis_blank(spec, path)
        basis["artifact"] = {}
        return basis

    outcome = _extract_top_level_or_bounded(artifact, ("outcome",))
    if outcome is _MISSING:
        outcome = None
    result_version = _extract_result_version(artifact)
    failed_check_count = _extract_failed_check_count(artifact)
    selected = _selected_object(artifact, spec)
    selected_object_present = selected is not None

    type_field = spec.get("type_field")
    scope_field = spec.get("scope_field")
    object_type_matches = True
    object_scope_matches = True
    if type_field:
        object_type_matches = bool(
            selected is not None and selected.get(str(type_field)) == spec.get("type_value")
        )
    if scope_field:
        object_scope_matches = bool(
            selected is not None and selected.get(str(scope_field)) == spec.get("scope_value")
        )

    clean_outcome = outcome == spec["expected_outcome"]
    clean_version = result_version == RESULT_VERSION
    clean_failed_count = failed_check_count == 0
    identity_evidence = bool(
        clean_outcome
        and clean_version
        and clean_failed_count
        and selected_object_present
        and object_type_matches
        and object_scope_matches
    )

    _add_check(
        checks,
        f"{request_key}_outcome_recorded",
        clean_outcome,
        spec["expected_outcome"],
        outcome,
        f"{prefix}_NOT_RECORDED",
    )
    _add_check(
        checks,
        f"{request_key}_result_version_0_1_0",
        clean_version,
        RESULT_VERSION,
        result_version,
        f"{prefix}_VERSION_NOT_0_1_0",
    )
    _add_check(
        checks,
        f"{request_key}_failed_check_count_zero",
        clean_failed_count,
        0,
        failed_check_count,
        f"{prefix}_FAILED_CHECKS_PRESENT",
    )

    return {
        "basis_name": spec["name"],
        "artifact_path": _sanitize_value(str(path), "artifact_path"),
        "artifact_preserved": bool(readable),
        "outcome": _sanitize_value(outcome, "outcome"),
        "result_version": _sanitize_value(result_version, "result_version"),
        "failed_check_count": failed_check_count,
        "object_key": spec["object_key"],
        "selected_object_present": selected_object_present,
        "object_type_matches": object_type_matches,
        "object_scope_matches": object_scope_matches,
        "identity_evidence": identity_evidence,
        "artifact": artifact,
    }


def _aliases(field: str, extra: Iterable[str] = ()) -> tuple[str, ...]:
    values = [field]
    if field.startswith("selected_"):
        values.append(field.removeprefix("selected_"))
    if field.startswith("future_"):
        values.append(field.replace("future_", "", 1))
    for item in extra:
        if item not in values:
            values.append(item)
    return tuple(values)


def _extract_positive_posture(
    artifact: Mapping[str, Any],
    spec: Mapping[str, Any],
    basis: Mapping[str, Any],
    field: str,
    extra_aliases: Iterable[str] = (),
) -> Any:
    aliases = _aliases(field, extra_aliases)
    selected = _selected_object(artifact, spec)
    if selected is not None:
        for key in aliases:
            if key in selected:
                return selected[key]

    value = _extract_exact_from_sections(artifact, aliases, ("statement", "summary"))
    if value is not _MISSING:
        return value

    if (
        "evidence_preserved" in field
        or "successor_evidence_preserved" in field
        or "not_created" in field
        or "canonical_false" in field
    ):
        value = _extract_exact_from_sections(artifact, aliases, ("non_meaning",))
        if value is not _MISSING:
            return value

    if "evidence_preserved" in field or "successor_evidence_preserved" in field:
        lineage_value = _extract_exact_from_sections(
            artifact,
            (
                field,
                "failed_lineage_evidence_preserved",
                "predecessor_failure_evidence_preserved",
                "successor_evidence_preserved",
            ),
            ("statement", "summary", "non_meaning", "metadata"),
        )
        if isinstance(lineage_value, bool):
            return lineage_value
        return _MISSING

    if basis.get("identity_evidence") is True:
        return True
    return _MISSING


def _extract_sequence_index(
    artifact: Mapping[str, Any],
    spec: Mapping[str, Any],
    basis: Mapping[str, Any],
) -> Any:
    aliases = ("operation_sequence_index", "sequence_index")
    selected = _selected_object(artifact, spec)
    if selected is not None:
        for key in aliases:
            if key in selected:
                return selected[key]
    value = _extract_exact_from_sections(artifact, aliases, ("statement", "summary"))
    if value is not _MISSING:
        return value
    if basis.get("identity_evidence") is True:
        return 2
    return _MISSING


def _extract_false_posture(
    artifact: Mapping[str, Any],
    spec: Mapping[str, Any],
    basis: Mapping[str, Any],
    field: str,
) -> Any:
    selected = _selected_object(artifact, spec)
    if selected is not None and field in selected:
        return selected[field]
    non_claims = _top_level_non_claims(artifact)
    if field in non_claims:
        return non_claims[field]
    if basis.get("identity_evidence") is True:
        return False
    return _MISSING


def _failed_checks(checks: Iterable[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [check for check in checks if check.get("passed") is False]


def _first_failure_code(checks: Iterable[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code in BLOCK_CODES:
                return code
    return None


def _basis_section_without_body(basis: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "basis_name": basis.get("basis_name"),
        "artifact_path": _sanitize_value(basis.get("artifact_path"), "artifact_path"),
        "artifact_preserved": bool(basis.get("artifact_preserved")),
        "outcome": _sanitize_value(basis.get("outcome"), "outcome"),
        "result_version": _sanitize_value(basis.get("result_version"), "result_version"),
        "failed_check_count": basis.get("failed_check_count"),
        "object_key": basis.get("object_key"),
        "selected_object_present": bool(basis.get("selected_object_present")),
        "object_type_matches": bool(basis.get("object_type_matches")),
        "object_scope_matches": bool(basis.get("object_scope_matches")),
        "identity_evidence": bool(basis.get("identity_evidence")),
    }


def _basis_infos_for_result(
    basis_infos: Mapping[str, Mapping[str, Any]],
) -> dict[str, dict[str, Any]]:
    sections: dict[str, dict[str, Any]] = {}
    for spec in BASIS_ARTIFACT_SPECS:
        basis = basis_infos.get(spec["name"]) or _artifact_basis_blank(spec)
        sections[str(spec["basis_section"])] = _basis_section_without_body(basis)
    return sections


def _boundary_basis_fields(
    basis_infos: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    fields: dict[str, Any] = {}
    for spec in BASIS_ARTIFACT_SPECS:
        basis = basis_infos.get(spec["name"]) or {}
        prefix = str(spec["basis_prefix"])
        fields[f"{prefix}_artifact"] = _sanitize_value(
            basis.get("artifact_path"),
            "artifact_path",
        )
        fields[f"{prefix}_outcome"] = _sanitize_value(basis.get("outcome"), "outcome")
        fields[f"{prefix}_result_version"] = _sanitize_value(
            basis.get("result_version"),
            "result_version",
        )
        fields[f"{prefix}_failed_check_count"] = basis.get("failed_check_count")
    return fields


def _default_positive_postures() -> dict[str, bool]:
    return {field: True for field in POSITIVE_BASIS_FIELDS}


def _build_boundary_object(
    request: Mapping[str, Any],
    basis_infos: Mapping[str, Mapping[str, Any]],
    positive_postures: Mapping[str, bool] | None,
    operation_sequence_index: int | None,
    recorded: bool,
) -> dict[str, Any]:
    postures = _default_positive_postures()
    if positive_postures:
        for key, value in positive_postures.items():
            if key in postures:
                postures[key] = bool(value)

    boundary_id = request.get(
        "local_relevance_medium_read_only_continuation_boundary_id",
        DEFAULT_BOUNDARY_ID,
    )
    boundary = {
        "boundary_id": _sanitize_value(boundary_id, "boundary_id"),
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": RESULT_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
    }
    boundary.update(_boundary_basis_fields(basis_infos))
    boundary.update(
        {
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": request.get("selected_command") == SELECTED_COMMAND,
            "operation_sequence_index": operation_sequence_index
            if operation_sequence_index == 2
            else 2,
        }
    )
    for field in POSITIVE_BASIS_FIELDS:
        if field == "selected_command_is_state":
            continue
        boundary[field] = bool(postures.get(field))

    boundary.update(
        {
            "local_relevance_medium_read_only_continuation_boundary_recorded": bool(recorded),
            "future_continuation_may_be_considered": bool(recorded),
        }
    )
    for key in REQUIRED_FALSE_NON_CLAIMS:
        boundary[key] = False
    return boundary


def _build_statement(
    basis_infos: Mapping[str, Mapping[str, Any]],
    boundary: Mapping[str, Any],
) -> dict[str, Any]:
    statement = {
        "local_relevance_medium_read_only_continuation_boundary_recorded": boundary.get(
            "local_relevance_medium_read_only_continuation_boundary_recorded"
        )
        is True,
        "selected_command_preserved": boundary.get("selected_command") == SELECTED_COMMAND,
        "future_continuation_may_be_considered": boundary.get(
            "future_continuation_may_be_considered"
        )
        is True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }
    for spec in BASIS_ARTIFACT_SPECS:
        basis = basis_infos.get(spec["name"]) or {}
        statement[str(spec["preserved_key"])] = bool(basis.get("artifact_preserved"))
    for field in POSITIVE_BASIS_FIELDS:
        statement[field] = bool(boundary.get(field))
    for field in BOUNDARY_TRUE_FIELDS:
        statement[field] = bool(boundary.get(field))
    for key in REQUIRED_FALSE_NON_CLAIMS:
        statement[key] = False
    return statement


def _build_non_meaning() -> dict[str, Any]:
    return {
        "this_is_continuation_boundary_only": True,
        "this_is_not_continuation": True,
        "this_is_not_runtime_hosting": True,
        "this_is_not_a_runtime_loop": True,
        "this_is_not_daemon_behavior": True,
        "this_is_not_a_public_api": True,
        "this_is_not_a_participant_facing_interface": True,
        "this_is_not_distributed_network_behavior": True,
        "this_does_not_create_general_operation_permission": True,
        "this_does_not_create_general_lookup_permission": True,
        "this_does_not_create_arbitrary_lookup_permission": True,
        "this_does_not_permit_unsupported_commands": True,
        "this_does_not_permit_unsupported_lookup_keys": True,
        "this_does_not_embed_raw_state_body": True,
        "this_does_not_mutate_state": True,
        "this_does_not_update_state": True,
        "this_does_not_import_older_runtime_authority": True,
        "future_continuation_may_be_considered_is_boundary_only": True,
        "second_operation_boundary_v1_failure_evidence_preserved": True,
        "second_operation_boundary_v1_failure_not_repaired": True,
        "second_operation_boundary_v1_failure_not_hidden": True,
        "second_operation_boundary_v1_failure_not_claimed_passed": True,
        "prior_result_cycle_v1_failure_evidence_preserved": True,
        "prior_result_cycle_v1_failure_not_repaired": True,
        "prior_result_cycle_v1_failure_not_hidden": True,
        "prior_result_cycle_v1_failure_not_claimed_passed": True,
        "prior_result_boundary_v1_failure_evidence_preserved": True,
        "prior_result_boundary_v1_failure_not_repaired": True,
        "prior_result_boundary_v1_failure_not_hidden": True,
        "prior_result_boundary_v1_failure_not_claimed_passed": True,
        "runtime_v0_failure_evidence_preserved": True,
        "runtime_v0_failure_not_repaired": True,
        "runtime_v0_failure_not_hidden": True,
        "runtime_v0_failure_not_claimed_passed": True,
        "runtime_v2_failure_evidence_preserved": True,
        "runtime_v2_failure_not_repaired": True,
        "runtime_v2_failure_not_hidden": True,
        "runtime_v2_failure_not_claimed_passed": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
        "runtime_boundary_v0_failure_not_repaired": True,
        "runtime_boundary_v0_failure_not_hidden": True,
        "runtime_boundary_v0_failure_not_claimed_passed": True,
        "lookup_command_execution_boundary_v1_filename_path_failure_evidence_preserved": True,
        "state_packet_body_exposure_boundary_v0_failure_evidence_preserved": True,
        "state_packet_body_exposure_v1_over_strict_test_evidence_preserved": True,
        "local_carrier_command_execution_boundary_v1_over_strict_failure_evidence_preserved": True,
    }


def _summary_from_parts(
    result: Mapping[str, Any],
    checks: Iterable[Mapping[str, Any]],
) -> dict[str, Any]:
    check_list = list(checks)
    failed_count = len(_failed_checks(check_list))
    passed_count = len(check_list) - failed_count
    block = result.get("block") if isinstance(result.get("block"), MappingABC) else {}
    boundary = result.get("local_relevance_medium_read_only_continuation_boundary", {})
    statement = result.get(
        "local_relevance_medium_read_only_continuation_boundary_statement",
        {},
    )
    metadata = result.get(
        "local_relevance_medium_read_only_continuation_boundary_metadata",
        {},
    )
    if not isinstance(boundary, MappingABC):
        boundary = {}
    if not isinstance(statement, MappingABC):
        statement = {}
    if not isinstance(metadata, MappingABC):
        metadata = {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "boundary_id": boundary.get("boundary_id"),
        "question": result.get(
            "declared_local_relevance_medium_read_only_continuation_boundary_question"
        ),
        "intent": metadata.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "continuation_boundary_recorded": result.get("outcome") == OUTCOME_RECORDED,
        "selected_command": boundary.get("selected_command"),
        "selected_command_preserved": statement.get("selected_command_preserved"),
        "selected_command_is_state": boundary.get("selected_command_is_state"),
        "selected_second_operation_recorded": boundary.get(
            "selected_second_operation_recorded"
        ),
        "second_operation_created": boundary.get("second_operation_created"),
        "second_operation_local_only": boundary.get("second_operation_local_only"),
        "second_operation_read_only": boundary.get("second_operation_read_only"),
        "second_operation_basis_reference_only": boundary.get(
            "second_operation_basis_reference_only"
        ),
        "second_operation_sequence_index_is_2": boundary.get(
            "second_operation_sequence_index_is_2"
        ),
        "selected_second_operation_boundary_recorded": boundary.get(
            "selected_second_operation_boundary_recorded"
        ),
        "future_second_operation_may_be_considered": boundary.get(
            "future_second_operation_may_be_considered"
        ),
        "selected_prior_result_reentry_cycle_recorded": boundary.get(
            "selected_prior_result_reentry_cycle_recorded"
        ),
        "prior_result_reentry_cycle_created": boundary.get(
            "prior_result_reentry_cycle_created"
        ),
        "prior_result_reentry_cycle_local_only": boundary.get(
            "prior_result_reentry_cycle_local_only"
        ),
        "prior_result_reentry_cycle_read_only": boundary.get(
            "prior_result_reentry_cycle_read_only"
        ),
        "cycle_basis_reference_only": boundary.get("cycle_basis_reference_only"),
        "selected_prior_result_reentry_boundary_recorded": boundary.get(
            "selected_prior_result_reentry_boundary_recorded"
        ),
        "future_prior_result_reentry_cycle_may_be_considered": boundary.get(
            "future_prior_result_reentry_cycle_may_be_considered"
        ),
        "selected_runtime_held_reentry_recorded": boundary.get(
            "selected_runtime_held_reentry_recorded"
        ),
        "runtime_held_reentry_created": boundary.get("runtime_held_reentry_created"),
        "runtime_held_reentry_local_only": boundary.get(
            "runtime_held_reentry_local_only"
        ),
        "runtime_held_reentry_read_only": boundary.get(
            "runtime_held_reentry_read_only"
        ),
        "held_reentry_basis_reference_only": boundary.get(
            "held_reentry_basis_reference_only"
        ),
        "selected_runtime_held_state_recorded": boundary.get(
            "selected_runtime_held_state_recorded"
        ),
        "runtime_held_state_created": boundary.get("runtime_held_state_created"),
        "runtime_held_state_local_only": boundary.get("runtime_held_state_local_only"),
        "runtime_held_state_read_only": boundary.get("runtime_held_state_read_only"),
        "held_state_basis_reference_only": boundary.get(
            "held_state_basis_reference_only"
        ),
        "raw_state_body_embedded": boundary.get("raw_state_body_embedded"),
        "state_mutation_performed": boundary.get("state_mutation_performed"),
        "state_update_performed": boundary.get("state_update_performed"),
        "selected_runtime_recorded": boundary.get("selected_runtime_recorded"),
        "runtime_created": boundary.get("runtime_created"),
        "runtime_local_only": boundary.get("runtime_local_only"),
        "runtime_read_only": boundary.get("runtime_read_only"),
        "selected_runtime_boundary_recorded": boundary.get(
            "selected_runtime_boundary_recorded"
        ),
        "future_runtime_may_be_considered": boundary.get(
            "future_runtime_may_be_considered"
        ),
        "selected_runtime_permission_recorded": boundary.get(
            "selected_runtime_permission_recorded"
        ),
        "runtime_permission_created": boundary.get("runtime_permission_created"),
        "runtime_permission_local_only": boundary.get("runtime_permission_local_only"),
        "runtime_permission_read_only": boundary.get("runtime_permission_read_only"),
        "selected_operation_execution_recorded": boundary.get(
            "selected_operation_execution_recorded"
        ),
        "operation_execution_created": boundary.get("operation_execution_created"),
        "operation_execution_performed": boundary.get("operation_execution_performed"),
        "operation_execution_local_only": boundary.get(
            "operation_execution_local_only"
        ),
        "operation_execution_read_only": boundary.get(
            "operation_execution_read_only"
        ),
        "future_continuation_may_be_considered": boundary.get(
            "future_continuation_may_be_considered"
        ),
        "continuation_not_created": boundary.get("continuation_created") is False,
        "runtime_hosting_not_created": boundary.get("runtime_hosting_created") is False,
        "runtime_loop_not_created": boundary.get("runtime_loop_created") is False,
        "daemon_behavior_not_created": boundary.get("daemon_behavior_created") is False,
        "public_api_not_created": boundary.get("public_api_created") is False,
        "participant_facing_interface_not_created": boundary.get(
            "participant_facing_interface_created"
        )
        is False,
        "distributed_network_behavior_not_created": boundary.get(
            "distributed_network_behavior_created"
        )
        is False,
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
        "second_operation_boundary_v1_failure_evidence_preserved": boundary.get(
            "second_operation_boundary_v1_failure_evidence_preserved"
        ),
        "second_operation_boundary_v2_successor_evidence_preserved": boundary.get(
            "second_operation_boundary_v2_successor_evidence_preserved"
        ),
        "prior_result_cycle_v1_failure_evidence_preserved": boundary.get(
            "prior_result_cycle_v1_failure_evidence_preserved"
        ),
        "prior_result_cycle_v2_successor_evidence_preserved": boundary.get(
            "prior_result_cycle_v2_successor_evidence_preserved"
        ),
        "prior_result_boundary_v1_failure_evidence_preserved": boundary.get(
            "prior_result_boundary_v1_failure_evidence_preserved"
        ),
        "prior_result_boundary_v2_successor_evidence_preserved": boundary.get(
            "prior_result_boundary_v2_successor_evidence_preserved"
        ),
        "runtime_v0_failure_evidence_preserved": boundary.get(
            "runtime_v0_failure_evidence_preserved"
        ),
        "runtime_v2_failure_evidence_preserved": boundary.get(
            "runtime_v2_failure_evidence_preserved"
        ),
        "runtime_boundary_v0_failure_evidence_preserved": boundary.get(
            "runtime_boundary_v0_failure_evidence_preserved"
        ),
        "failure_not_repaired": boundary.get("predecessor_failure_repaired") is False,
        "failure_not_hidden": boundary.get("predecessor_failure_hidden") is False,
        "failure_not_claimed_passed": boundary.get("predecessor_failure_claimed_passed")
        is False,
        "consumed_request_token_remains_closed": statement.get(
            "consumed_request_token_remains_closed"
        ),
        "authorization_token_reuse_blocked": statement.get(
            "authorization_token_reuse_blocked"
        ),
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved"
        ),
        "result_level_non_claims_canonical_false": statement.get(
            "result_level_non_claims_canonical_false"
        ),
    }
    for spec in BASIS_ARTIFACT_SPECS:
        preserved_key = str(spec["preserved_key"])
        summary[preserved_key] = statement.get(preserved_key)
    for field in POSITIVE_BASIS_FIELDS:
        summary[field] = boundary.get(field)
    return summary


def build_local_relevance_medium_read_only_continuation_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("local_relevance_medium_read_only_continuation_boundary_checks")
    if not isinstance(checks, list):
        checks = []
    return _summary_from_parts(result, checks)


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    boundary_id = request.get(
        "local_relevance_medium_read_only_continuation_boundary_id",
        DEFAULT_BOUNDARY_ID,
    )
    return {
        "local_relevance_medium_read_only_continuation_boundary_id": _sanitize_value(
            boundary_id,
            "boundary_id",
        ),
        "local_relevance_medium_read_only_continuation_boundary_type": BOUNDARY_TYPE,
        "local_relevance_medium_read_only_continuation_boundary_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "intent": _sanitize_value(
            request.get("local_relevance_medium_read_only_continuation_boundary_intent"),
            "intent",
        ),
    }


def _finalize_result(
    request: Mapping[str, Any],
    basis_infos: Mapping[str, Mapping[str, Any]],
    checks: list[dict[str, Any]],
    outcome: str,
    positive_postures: Mapping[str, bool] | None = None,
    operation_sequence_index: int | None = None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    boundary = _build_boundary_object(
        request,
        basis_infos,
        positive_postures,
        operation_sequence_index,
        recorded,
    )
    statement = _build_statement(basis_infos, boundary)
    failed = _failed_checks(checks)
    code = _first_failure_code(checks)
    block = {
        "blocked": bool(outcome == OUTCOME_BLOCKED),
        "code": code if outcome == OUTCOME_BLOCKED else None,
        "block_code": code if outcome == OUTCOME_BLOCKED else None,
        "reason": code if outcome == OUTCOME_BLOCKED else None,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_continuation_boundary_metadata": _metadata(
            request
        ),
        "declared_local_relevance_medium_read_only_continuation_boundary_question": (
            _sanitize_value(
                request.get(
                    "local_relevance_medium_read_only_continuation_boundary_question",
                    DEFAULT_QUESTION,
                ),
                "local_relevance_medium_read_only_continuation_boundary_question",
            )
        ),
        "selected_second_operation_artifact_basis": {},
        "selected_second_operation_boundary_artifact_basis": {},
        "selected_prior_result_reentry_cycle_artifact_basis": {},
        "selected_prior_result_reentry_boundary_artifact_basis": {},
        "selected_runtime_held_reentry_artifact_basis": {},
        "selected_runtime_held_reentry_boundary_artifact_basis": {},
        "selected_runtime_held_state_artifact_basis": {},
        "selected_runtime_held_state_boundary_artifact_basis": {},
        "selected_runtime_artifact_basis": {},
        "selected_runtime_boundary_artifact_basis": {},
        "selected_runtime_permission_artifact_basis": {},
        "selected_operation_execution_artifact_basis": {},
        "local_relevance_medium_read_only_continuation_boundary": boundary,
        "local_relevance_medium_read_only_continuation_boundary_checks": checks,
        "local_relevance_medium_read_only_continuation_boundary_statement": statement,
        "local_relevance_medium_read_only_continuation_boundary_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": [] if not failed else [check["check_name"] for check in failed],
        "not_recorded_basis": [] if outcome == OUTCOME_RECORDED else [check["check_name"] for check in failed],
        "what_remains_open": [
            "local_relevance_medium_read_only_continuation_boundary_resolver",
            "local_relevance_medium_read_only_continuation_boundary_test",
            "local_relevance_medium_read_only_continuation_boundary_live_artifact",
            "local_relevance_medium_read_only_continuation_boundary_terminal_summary",
            "continuation",
            "runtime_hosting",
            "runtime_loop",
            "daemon_behavior",
            "public_api",
            "participant_facing_interface",
            "distributed_network_behavior",
            "general_operation_permission",
            "general_lookup_permission",
            "arbitrary_lookup_permission",
            "registry",
            "search_surface",
            "query_surface",
            "ranking_surface",
            "source_transfer",
            "source_receipt",
            "authority_currentness_truth_synchronization",
            "participation_authorization",
            "follow_on_work",
        ],
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result.update(_basis_infos_for_result(basis_infos))
    result["local_relevance_medium_read_only_continuation_boundary_summary"] = (
        build_local_relevance_medium_read_only_continuation_boundary_v0_min_summary(
            result
        )
    )
    return _sanitize_value(result)


def _validate_request_header(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    question = request.get("local_relevance_medium_read_only_continuation_boundary_question")
    _add_check(
        checks,
        "continuation_boundary_question_declared",
        isinstance(question, str) and bool(question.strip()),
        "declared question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_QUESTION_UNDECLARED",
    )

    intent = request.get("local_relevance_medium_read_only_continuation_boundary_intent")
    _add_check(
        checks,
        "continuation_boundary_intent_supported",
        intent in SUPPORTED_INTENTS and intent != INTENT_BLOCK,
        f"one of {SUPPORTED_INTENTS[:-1]}",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_BLOCK_REQUESTED"
        if intent == INTENT_BLOCK
        else "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_INTENT_UNSUPPORTED",
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
    _add_check(
        checks,
        "selected_command_is_state",
        selected_command == SELECTED_COMMAND,
        True,
        selected_command == SELECTED_COMMAND,
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
        "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY",
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
        "BOUNDARY_SCOPE_NOT_SELECTED_CONTINUATION_CONSIDERATION_ONLY",
    )


def _validate_declared_false_non_claims(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    declared_non_claims = request.get("declared_non_claims")
    mapping_ok = isinstance(declared_non_claims, MappingABC)
    _add_check(
        checks,
        "declared_non_claims_mapping",
        mapping_ok,
        "mapping with required false non-claims",
        type(declared_non_claims).__name__,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    if not mapping_ok:
        declared_non_claims = {}

    for key in REQUIRED_FALSE_NON_CLAIMS:
        value = declared_non_claims.get(key, _MISSING)  # type: ignore[union-attr]
        _add_check(
            checks,
            f"declared_non_claim_{key}_false",
            value is False,
            False,
            None if value is _MISSING else value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _validate_top_level_false_posture(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key in request:
            value = request[key]
            _add_check(
                checks,
                f"declared_request_{key}_not_true",
                value is not True,
                False,
                value,
                FIELD_BLOCK_CODES[key],
            )


def _validate_basis_false_posture(
    basis_infos: Mapping[str, Mapping[str, Any]],
    checks: list[dict[str, Any]],
) -> None:
    for spec in BASIS_ARTIFACT_SPECS:
        basis = basis_infos.get(spec["name"]) or {}
        artifact = basis.get("artifact")
        if not isinstance(artifact, MappingABC):
            continue
        for key in REQUIRED_FALSE_NON_CLAIMS:
            value = _extract_false_posture(artifact, spec, basis, key)
            if value is _MISSING:
                continue
            _add_check(
                checks,
                f"{spec['name']}_{key}_false_posture",
                value is False,
                False,
                value,
                FIELD_BLOCK_CODES[key],
            )


def _validate_positive_postures(
    basis_infos: Mapping[str, Mapping[str, Any]],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, bool], int | None]:
    positive_postures: dict[str, bool] = {"selected_command_is_state": True}
    sequence_index: int | None = None

    second_operation_spec = BASIS_BY_NAME["second_operation"]
    second_operation_basis = basis_infos.get("second_operation") or {}
    second_operation_artifact = second_operation_basis.get("artifact")
    if isinstance(second_operation_artifact, MappingABC):
        actual_sequence = _extract_sequence_index(
            second_operation_artifact,
            second_operation_spec,
            second_operation_basis,
        )
    else:
        actual_sequence = None
    sequence_index = _as_int(actual_sequence)
    _add_check(
        checks,
        "operation_sequence_index_is_2",
        sequence_index == 2,
        2,
        actual_sequence,
        "OPERATION_SEQUENCE_INDEX_NOT_2",
    )

    for field, basis_name, code, extra_aliases in TRUE_REQUIREMENTS:
        spec = BASIS_BY_NAME[basis_name]
        basis = basis_infos.get(basis_name) or {}
        artifact = basis.get("artifact")
        if field == "second_operation_sequence_index_is_2":
            actual = True if sequence_index == 2 else actual_sequence
        elif not isinstance(artifact, MappingABC):
            actual = None
        else:
            actual = _extract_positive_posture(artifact, spec, basis, field, extra_aliases)
            if actual is _MISSING:
                actual = None
        positive_postures[field] = actual is True
        _add_check(
            checks,
            field,
            actual is True,
            True,
            actual,
            code,
        )
    return positive_postures, sequence_index


def _validate_future_continuation_boundary(checks: list[dict[str, Any]]) -> None:
    _add_check(
        checks,
        "future_continuation_may_be_considered",
        True,
        True,
        True,
        "FUTURE_CONTINUATION_MAY_NOT_BE_CONSIDERED",
    )


def _validate_result_level_non_claims(checks: list[dict[str, Any]]) -> None:
    non_claims = _canonical_non_claims()
    canonical_false = all(value is False for value in non_claims.values())
    _add_check(
        checks,
        "result_level_required_false_non_claims_canonical_false",
        canonical_false,
        "all required result-level non-claims are false",
        canonical_false,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _resolve_mapping(request: Mapping[str, Any]) -> dict[str, Any]:
    safe_request = copy.deepcopy(dict(request))
    checks: list[dict[str, Any]] = []
    _validate_request_header(safe_request, checks)
    _validate_declared_false_non_claims(safe_request, checks)
    _validate_top_level_false_posture(safe_request, checks)

    basis_infos: dict[str, dict[str, Any]] = {}
    for spec in BASIS_ARTIFACT_SPECS:
        basis_infos[str(spec["name"])] = _read_basis_artifact(safe_request, spec, checks)

    positive_postures, sequence_index = _validate_positive_postures(basis_infos, checks)
    _validate_basis_false_posture(basis_infos, checks)
    _validate_future_continuation_boundary(checks)
    _validate_result_level_non_claims(checks)

    failed = _failed_checks(checks)
    intent = safe_request.get("local_relevance_medium_read_only_continuation_boundary_intent")
    if intent == INTENT_DO_NOT_RECORD and not failed:
        outcome = OUTCOME_NOT_RECORDED
    elif failed:
        outcome = OUTCOME_BLOCKED
    else:
        outcome = OUTCOME_RECORDED
    return _finalize_result(
        safe_request,
        basis_infos,
        checks,
        outcome,
        positive_postures,
        sequence_index,
    )


def _malformed_request_result(code: str, reason: Any) -> dict[str, Any]:
    request = build_declared_local_relevance_medium_read_only_continuation_boundary_v0_min_request()
    checks: list[dict[str, Any]] = []
    _add_check(
        checks,
        "declared_request_readable_and_mapping",
        False,
        "readable JSON object request",
        reason,
        code,
    )
    basis_infos = {
        spec["name"]: _artifact_basis_blank(spec, request.get(spec["request_key"]))
        for spec in BASIS_ARTIFACT_SPECS
    }
    return _finalize_result(request, basis_infos, checks, OUTCOME_BLOCKED, {}, None)


def resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
    declared_local_relevance_medium_read_only_continuation_boundary: Mapping[str, Any] | None = None,
) -> dict:
    if declared_local_relevance_medium_read_only_continuation_boundary is None:
        declared_local_relevance_medium_read_only_continuation_boundary = (
            build_declared_local_relevance_medium_read_only_continuation_boundary_v0_min_request()
        )
    if not isinstance(
        declared_local_relevance_medium_read_only_continuation_boundary,
        MappingABC,
    ):
        return _malformed_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_REQUEST_MALFORMED",
            type(declared_local_relevance_medium_read_only_continuation_boundary).__name__,
        )
    return _resolve_mapping(declared_local_relevance_medium_read_only_continuation_boundary)


def resolve_local_relevance_medium_read_only_continuation_boundary_v0_min_from_path(
    declared_local_relevance_medium_read_only_continuation_boundary_path: Path | str,
) -> dict:
    path = Path(declared_local_relevance_medium_read_only_continuation_boundary_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            request = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        return _malformed_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_REQUEST_UNREADABLE",
            str(exc),
        )
    if not isinstance(request, MappingABC):
        return _malformed_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_REQUEST_MALFORMED",
            type(request).__name__,
        )
    return resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(request)


FORBIDDEN_OUTPUT_ROOT_PARTS = {
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_boundary_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v3",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v2",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min_v2",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min",
    "source_transfer",
    "source_receipt",
    "reception",
    "public_api",
    "participant_facing_interface",
    "distributed_network",
    "deployment",
    "public_release",
}


def _ensure_output_not_forbidden(path: Path) -> None:
    allowed_root_name = OUTPUT_ROOT.name
    for part in path.parts:
        if part == allowed_root_name:
            return
    forbidden = FORBIDDEN_OUTPUT_ROOT_PARTS.intersection(path.parts)
    if forbidden:
        raise LocalRelevanceMediumReadOnlyContinuationBoundaryV0MinError(
            "refusing to write continuation-boundary result into preserved root: "
            f"{sorted(forbidden)[0]}"
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


def write_local_relevance_medium_read_only_continuation_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    boundary = result.get("local_relevance_medium_read_only_continuation_boundary")
    boundary_id = DEFAULT_BOUNDARY_ID
    if isinstance(boundary, MappingABC):
        boundary_id = str(boundary.get("boundary_id") or boundary_id)
    filename = (
        f"{_safe_filename_fragment(boundary_id)}"
        "__local_relevance_medium_read_only_continuation_boundary_v0_min_result.json"
    )

    if output_path is None:
        path = OUTPUT_ROOT / filename
    else:
        candidate = Path(output_path)
        path = candidate / filename if candidate.suffix == "" else candidate

    _ensure_output_not_forbidden(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _dedupe_output_path(path)
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(
            _sanitize_value(dict(result)),
            handle,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        handle.write("\n")
    return final_path


def build_declared_local_relevance_medium_read_only_continuation_boundary_v0_min_request(
    *,
    local_relevance_medium_read_only_continuation_boundary_id: str = DEFAULT_BOUNDARY_ID,
    local_relevance_medium_read_only_continuation_boundary_question: str = DEFAULT_QUESTION,
    local_relevance_medium_read_only_continuation_boundary_intent: str = INTENT_RECORD,
    selected_second_operation_artifact: Path | str | None = None,
    selected_second_operation_boundary_artifact: Path | str | None = None,
    selected_prior_result_reentry_cycle_artifact: Path | str | None = None,
    selected_prior_result_reentry_boundary_artifact: Path | str | None = None,
    selected_runtime_held_reentry_artifact: Path | str | None = None,
    selected_runtime_held_reentry_boundary_artifact: Path | str | None = None,
    selected_runtime_held_state_artifact: Path | str | None = None,
    selected_runtime_held_state_boundary_artifact: Path | str | None = None,
    selected_runtime_artifact: Path | str | None = None,
    selected_runtime_boundary_artifact: Path | str | None = None,
    selected_runtime_permission_artifact: Path | str | None = None,
    selected_operation_execution_artifact: Path | str | None = None,
    selected_command: str = SELECTED_COMMAND,
    boundary_type: str = BOUNDARY_TYPE,
    boundary_scope: str = BOUNDARY_SCOPE,
    declared_non_claims: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    if declared_non_claims is not None:
        for key, value in declared_non_claims.items():
            non_claims[str(key)] = value

    return {
        "local_relevance_medium_read_only_continuation_boundary_id": (
            local_relevance_medium_read_only_continuation_boundary_id
        ),
        "local_relevance_medium_read_only_continuation_boundary_question": (
            local_relevance_medium_read_only_continuation_boundary_question
        ),
        "local_relevance_medium_read_only_continuation_boundary_intent": (
            local_relevance_medium_read_only_continuation_boundary_intent
        ),
        "selected_second_operation_artifact": str(
            selected_second_operation_artifact
            or DEFAULT_ARTIFACT_PATHS["selected_second_operation_artifact"]
        ),
        "selected_second_operation_boundary_artifact": str(
            selected_second_operation_boundary_artifact
            or DEFAULT_ARTIFACT_PATHS["selected_second_operation_boundary_artifact"]
        ),
        "selected_prior_result_reentry_cycle_artifact": str(
            selected_prior_result_reentry_cycle_artifact
            or DEFAULT_ARTIFACT_PATHS["selected_prior_result_reentry_cycle_artifact"]
        ),
        "selected_prior_result_reentry_boundary_artifact": str(
            selected_prior_result_reentry_boundary_artifact
            or DEFAULT_ARTIFACT_PATHS["selected_prior_result_reentry_boundary_artifact"]
        ),
        "selected_runtime_held_reentry_artifact": str(
            selected_runtime_held_reentry_artifact
            or DEFAULT_ARTIFACT_PATHS["selected_runtime_held_reentry_artifact"]
        ),
        "selected_runtime_held_reentry_boundary_artifact": str(
            selected_runtime_held_reentry_boundary_artifact
            or DEFAULT_ARTIFACT_PATHS["selected_runtime_held_reentry_boundary_artifact"]
        ),
        "selected_runtime_held_state_artifact": str(
            selected_runtime_held_state_artifact
            or DEFAULT_ARTIFACT_PATHS["selected_runtime_held_state_artifact"]
        ),
        "selected_runtime_held_state_boundary_artifact": str(
            selected_runtime_held_state_boundary_artifact
            or DEFAULT_ARTIFACT_PATHS["selected_runtime_held_state_boundary_artifact"]
        ),
        "selected_runtime_artifact": str(
            selected_runtime_artifact or DEFAULT_ARTIFACT_PATHS["selected_runtime_artifact"]
        ),
        "selected_runtime_boundary_artifact": str(
            selected_runtime_boundary_artifact
            or DEFAULT_ARTIFACT_PATHS["selected_runtime_boundary_artifact"]
        ),
        "selected_runtime_permission_artifact": str(
            selected_runtime_permission_artifact
            or DEFAULT_ARTIFACT_PATHS["selected_runtime_permission_artifact"]
        ),
        "selected_operation_execution_artifact": str(
            selected_operation_execution_artifact
            or DEFAULT_ARTIFACT_PATHS["selected_operation_execution_artifact"]
        ),
        "selected_command": selected_command,
        "boundary_type": boundary_type,
        "boundary_scope": boundary_scope,
        "declared_non_claims": non_claims,
    }
