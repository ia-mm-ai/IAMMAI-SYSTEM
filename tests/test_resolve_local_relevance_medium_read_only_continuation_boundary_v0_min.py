"""Tests for the local read-only continuation-boundary resolver.

This suite verifies one selected-state
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY object only. The
boundary records that a future local read-only continuation may be considered
as a separately bounded step, while preserving non-continuation, non-hosting,
non-loop, non-daemon, raw-state-body-excluding, state-mutation-refusing,
state-update-refusing, closure-token-aware, and older-runtime-authority-
import-blocking posture.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_read_only_continuation_boundary_v0_min as resolver  # noqa: E402


BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_CONTINUATION_CONSIDERATION_ONLY"
SELECTED_COMMAND = "state"

EXPECTED_OUTCOME_FAMILY = {
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_NOT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_BLOCKED",
}

EXPECTED_WRAPPER_SECTIONS = {
    "local_relevance_medium_read_only_continuation_boundary_metadata",
    "declared_local_relevance_medium_read_only_continuation_boundary_question",
    "selected_second_operation_artifact_basis",
    "selected_second_operation_boundary_artifact_basis",
    "selected_prior_result_reentry_cycle_artifact_basis",
    "selected_prior_result_reentry_boundary_artifact_basis",
    "selected_runtime_held_reentry_artifact_basis",
    "selected_runtime_held_reentry_boundary_artifact_basis",
    "selected_runtime_held_state_artifact_basis",
    "selected_runtime_held_state_boundary_artifact_basis",
    "selected_runtime_artifact_basis",
    "selected_runtime_boundary_artifact_basis",
    "selected_runtime_permission_artifact_basis",
    "selected_operation_execution_artifact_basis",
    "local_relevance_medium_read_only_continuation_boundary",
    "local_relevance_medium_read_only_continuation_boundary_checks",
    "local_relevance_medium_read_only_continuation_boundary_statement",
    "local_relevance_medium_read_only_continuation_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_continuation_boundary_summary",
}

FORBIDDEN_WRAPPER_FIELDS_IN_BOUNDARY = {
    "outcome",
    "block",
    "local_relevance_medium_read_only_continuation_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_continuation_boundary_summary",
    "local_relevance_medium_read_only_continuation_boundary_metadata",
}

DEFAULT_SUFFIXES = {
    "selected_second_operation_artifact": (
        "local_relevance_medium_read_only_second_operation_reference_review_001__"
        "local_relevance_medium_read_only_second_operation_v0_min_result.json"
    ),
    "selected_second_operation_boundary_artifact": (
        "local_relevance_medium_read_only_second_operation_boundary_reference_review_001__"
        "local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_result.json"
    ),
    "selected_prior_result_reentry_cycle_artifact": (
        "local_relevance_medium_read_only_prior_result_reentry_cycle_reference_review_001__"
        "local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_result.json"
    ),
    "selected_prior_result_reentry_boundary_artifact": (
        "local_relevance_medium_read_only_prior_result_reentry_boundary_reference_review_001__"
        "local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_result.json"
    ),
    "selected_runtime_held_reentry_artifact": (
        "local_relevance_medium_read_only_runtime_held_reentry_reference_review_001__"
        "local_relevance_medium_read_only_runtime_held_reentry_v0_min_result.json"
    ),
    "selected_runtime_held_reentry_boundary_artifact": (
        "local_relevance_medium_read_only_runtime_held_reentry_boundary_reference_review_001__"
        "local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min_result.json"
    ),
    "selected_runtime_held_state_artifact": (
        "local_relevance_medium_read_only_runtime_held_state_reference_review_001__"
        "local_relevance_medium_read_only_runtime_held_state_v0_min_result.json"
    ),
    "selected_runtime_held_state_boundary_artifact": (
        "local_relevance_medium_read_only_runtime_held_state_boundary_reference_review_001__"
        "local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result.json"
    ),
    "selected_runtime_artifact": (
        "local_relevance_medium_read_only_runtime_reference_review_001__"
        "local_relevance_medium_read_only_runtime_v0_min_v3_result.json"
    ),
    "selected_runtime_boundary_artifact": (
        "local_relevance_medium_read_only_runtime_boundary_reference_review_001__"
        "local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
    ),
    "selected_runtime_permission_artifact": (
        "local_relevance_medium_read_only_runtime_permission_reference_review_001__"
        "local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
    ),
    "selected_operation_execution_artifact": (
        "local_relevance_medium_read_only_operation_execution_reference_review_001__"
        "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
    ),
}

BASIS = (
    {
        "name": "second_operation",
        "request_key": "selected_second_operation_artifact",
        "object_key": "local_relevance_medium_read_only_second_operation",
        "basis_prefix": "basis_second_operation",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_RECORDED",
        "type_field": "operation_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION",
        "scope_field": "operation_scope",
        "scope_value": "SELECTED_SECOND_OPERATION_ONLY",
        "true_fields": {
            "selected_second_operation_recorded": True,
            "second_operation_recorded": True,
            "local_relevance_medium_read_only_second_operation_recorded": True,
            "second_operation_created": True,
            "second_operation_local_only": True,
            "second_operation_read_only": True,
            "second_operation_basis_reference_only": True,
            "second_operation_sequence_index_is_2": True,
            "operation_sequence_index": 2,
        },
    },
    {
        "name": "second_operation_boundary",
        "request_key": "selected_second_operation_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_second_operation_boundary",
        "basis_prefix": "basis_second_operation_boundary",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_RECORDED",
        "type_field": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY",
        "scope_field": "boundary_scope",
        "scope_value": "SELECTED_SECOND_OPERATION_CONSIDERATION_ONLY",
        "true_fields": {
            "selected_second_operation_boundary_recorded": True,
            "second_operation_boundary_recorded": True,
            "local_relevance_medium_read_only_second_operation_boundary_recorded": True,
            "future_second_operation_may_be_considered": True,
        },
    },
    {
        "name": "prior_result_reentry_cycle",
        "request_key": "selected_prior_result_reentry_cycle_artifact",
        "object_key": "local_relevance_medium_read_only_prior_result_reentry_cycle",
        "basis_prefix": "basis_prior_result_reentry_cycle",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_RECORDED",
        "type_field": "cycle_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE",
        "scope_field": "cycle_scope",
        "scope_value": "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY",
        "true_fields": {
            "selected_prior_result_reentry_cycle_recorded": True,
            "prior_result_reentry_cycle_recorded": True,
            "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded": True,
            "prior_result_reentry_cycle_created": True,
            "prior_result_reentry_cycle_local_only": True,
            "prior_result_reentry_cycle_read_only": True,
            "cycle_basis_reference_only": True,
        },
    },
    {
        "name": "prior_result_reentry_boundary",
        "request_key": "selected_prior_result_reentry_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_prior_result_reentry_boundary",
        "basis_prefix": "basis_prior_result_reentry_boundary",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_RECORDED",
        "type_field": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY",
        "scope_field": "boundary_scope",
        "scope_value": "SELECTED_PRIOR_RESULT_REENTRY_CONSIDERATION_ONLY",
        "true_fields": {
            "selected_prior_result_reentry_boundary_recorded": True,
            "prior_result_reentry_boundary_recorded": True,
            "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded": True,
            "future_prior_result_reentry_cycle_may_be_considered": True,
        },
    },
    {
        "name": "runtime_held_reentry",
        "request_key": "selected_runtime_held_reentry_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry",
        "basis_prefix": "basis_runtime_held_reentry",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_RECORDED",
        "type_field": "held_reentry_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY",
        "scope_field": "held_reentry_scope",
        "scope_value": "SELECTED_RUNTIME_HELD_REENTRY_ONLY",
        "true_fields": {
            "selected_runtime_held_reentry_recorded": True,
            "runtime_held_reentry_recorded": True,
            "local_relevance_medium_read_only_runtime_held_reentry_recorded": True,
            "runtime_held_reentry_created": True,
            "runtime_held_reentry_local_only": True,
            "runtime_held_reentry_read_only": True,
            "held_reentry_basis_reference_only": True,
        },
    },
    {
        "name": "runtime_held_reentry_boundary",
        "request_key": "selected_runtime_held_reentry_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry_boundary",
        "basis_prefix": "basis_runtime_held_reentry_boundary",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY_RECORDED",
        "type_field": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY",
        "scope_field": "boundary_scope",
        "scope_value": "SELECTED_RUNTIME_HELD_REENTRY_CONSIDERATION_ONLY",
        "true_fields": {
            "selected_runtime_held_reentry_boundary_recorded": True,
            "runtime_held_reentry_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_held_reentry_boundary_recorded": True,
            "future_runtime_held_reentry_may_be_considered": True,
        },
    },
    {
        "name": "runtime_held_state",
        "request_key": "selected_runtime_held_state_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_state",
        "basis_prefix": "basis_runtime_held_state",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_RECORDED",
        "type_field": "held_state_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE",
        "scope_field": "held_state_scope",
        "scope_value": "SELECTED_RUNTIME_HELD_STATE_ONLY",
        "true_fields": {
            "selected_runtime_held_state_recorded": True,
            "runtime_held_state_recorded": True,
            "local_relevance_medium_read_only_runtime_held_state_recorded": True,
            "runtime_held_state_created": True,
            "runtime_held_state_local_only": True,
            "runtime_held_state_read_only": True,
            "held_state_basis_reference_only": True,
        },
    },
    {
        "name": "runtime_held_state_boundary",
        "request_key": "selected_runtime_held_state_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_state_boundary",
        "basis_prefix": "basis_runtime_held_state_boundary",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_RECORDED",
        "type_field": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY",
        "scope_field": "boundary_scope",
        "scope_value": "SELECTED_RUNTIME_HELD_STATE_CONSIDERATION_ONLY",
        "true_fields": {
            "selected_runtime_held_state_boundary_recorded": True,
            "runtime_held_state_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_held_state_boundary_recorded": True,
            "future_runtime_held_state_may_be_considered": True,
        },
    },
    {
        "name": "runtime",
        "request_key": "selected_runtime_artifact",
        "object_key": "local_relevance_medium_read_only_runtime",
        "basis_prefix": "basis_runtime",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED",
        "type_field": "runtime_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME",
        "scope_field": "runtime_scope",
        "scope_value": "SELECTED_RUNTIME_ONLY",
        "true_fields": {
            "selected_runtime_recorded": True,
            "runtime_recorded": True,
            "local_relevance_medium_read_only_runtime_recorded": True,
            "runtime_created": True,
            "runtime_local_only": True,
            "runtime_read_only": True,
        },
    },
    {
        "name": "runtime_boundary",
        "request_key": "selected_runtime_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_boundary",
        "basis_prefix": "basis_runtime_boundary",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED",
        "type_field": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
        "scope_field": "boundary_scope",
        "scope_value": "SELECTED_RUNTIME_CONSIDERATION_ONLY",
        "true_fields": {
            "selected_runtime_boundary_recorded": True,
            "runtime_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_boundary_recorded": True,
            "future_runtime_may_be_considered": True,
        },
    },
    {
        "name": "runtime_permission",
        "request_key": "selected_runtime_permission_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_permission",
        "basis_prefix": "basis_runtime_permission",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED",
        "type_field": "runtime_permission_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
        "scope_field": "runtime_permission_scope",
        "scope_value": "SELECTED_RUNTIME_PERMISSION_ONLY",
        "true_fields": {
            "selected_runtime_permission_recorded": True,
            "runtime_permission_recorded": True,
            "local_relevance_medium_read_only_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
        },
    },
    {
        "name": "operation_execution",
        "request_key": "selected_operation_execution_artifact",
        "object_key": "local_relevance_medium_read_only_operation_execution",
        "basis_prefix": "basis_operation_execution",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
        "type_field": "operation_execution_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
        "scope_field": "operation_execution_scope",
        "scope_value": "SELECTED_OPERATION_EXECUTION_ONLY",
        "true_fields": {
            "selected_operation_execution_recorded": True,
            "operation_execution_recorded": True,
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
        },
    },
)

BASIS_BY_NAME = {spec["name"]: spec for spec in BASIS}

POSITIVE_FIELDS = (
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
)

LINEAGE_TRUE_FIELDS = (
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

NAMED_FAILURE_FALSE_FIELDS = (
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
)

EXACT_FORBIDDEN_FIELDS = (
    "continuation_created",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
    "older_runtime_lineage_imported_as_authority",
    "older_runtime_permission_treated_as_current",
    "runtime_authority_imported",
    "consumed_request_reopened",
    "authorization_token_reused",
    "follow_on_work_authorized",
)

TOP_LEVEL_BLOCK_CASES = (
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
    ("older_runtime_lineage_imported_as_authority", "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY"),
    ("older_runtime_permission_treated_as_current", "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT"),
    ("runtime_authority_imported", "RUNTIME_AUTHORITY_IMPORTED"),
    ("raw_state_body_embedded", "RAW_STATE_BODY_EMBEDDED"),
    ("state_mutation_performed", "STATE_MUTATION_PERFORMED"),
    ("state_update_performed", "STATE_UPDATE_PERFORMED"),
    ("continuation_created", "CONTINUATION_CREATED"),
    ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
    ("runtime_loop_created", "RUNTIME_LOOP_CREATED"),
    ("daemon_behavior_created", "DAEMON_BEHAVIOR_CREATED"),
    ("public_api_created", "PUBLIC_API_CREATED"),
    ("participant_facing_interface_created", "PARTICIPANT_FACING_INTERFACE_CREATED"),
    ("distributed_network_behavior_created", "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
    ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    ("second_operation_boundary_v1_failure_repaired", "SECOND_OPERATION_BOUNDARY_V1_FAILURE_REPAIRED"),
    ("second_operation_boundary_v1_failure_hidden", "SECOND_OPERATION_BOUNDARY_V1_FAILURE_HIDDEN"),
    ("second_operation_boundary_v1_failure_claimed_passed", "SECOND_OPERATION_BOUNDARY_V1_FAILURE_CLAIMED_PASSED"),
    ("prior_result_cycle_v1_failure_repaired", "PRIOR_RESULT_CYCLE_V1_FAILURE_REPAIRED"),
    ("prior_result_cycle_v1_failure_hidden", "PRIOR_RESULT_CYCLE_V1_FAILURE_HIDDEN"),
    ("prior_result_cycle_v1_failure_claimed_passed", "PRIOR_RESULT_CYCLE_V1_FAILURE_CLAIMED_PASSED"),
    ("prior_result_boundary_v1_failure_repaired", "PRIOR_RESULT_BOUNDARY_V1_FAILURE_REPAIRED"),
    ("prior_result_boundary_v1_failure_hidden", "PRIOR_RESULT_BOUNDARY_V1_FAILURE_HIDDEN"),
    ("prior_result_boundary_v1_failure_claimed_passed", "PRIOR_RESULT_BOUNDARY_V1_FAILURE_CLAIMED_PASSED"),
    ("runtime_v0_failure_repaired", "RUNTIME_V0_FAILURE_REPAIRED"),
    ("runtime_v0_failure_hidden", "RUNTIME_V0_FAILURE_HIDDEN"),
    ("runtime_v0_failure_claimed_passed", "RUNTIME_V0_FAILURE_CLAIMED_PASSED"),
    ("runtime_v2_failure_repaired", "RUNTIME_V2_FAILURE_REPAIRED"),
    ("runtime_v2_failure_hidden", "RUNTIME_V2_FAILURE_HIDDEN"),
    ("runtime_v2_failure_claimed_passed", "RUNTIME_V2_FAILURE_CLAIMED_PASSED"),
    ("runtime_boundary_v0_failure_repaired", "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED"),
    ("runtime_boundary_v0_failure_hidden", "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN"),
    ("runtime_boundary_v0_failure_claimed_passed", "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED"),
)

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
    "RAW_STATE_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

FORBIDDEN_OUTPUT_ROOT_NAMES = {
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_boundary_v0_min",
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2",
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
    "integrity_host_v0_min_coexistence_source_transfer_v0_min",
    "integrity_host_v0_min_coexistence_source_receipt_v0_min",
    "integrity_host_v0_min_coexistence_public_api_v0_min",
    "integrity_host_v0_min_coexistence_participant_facing_interface_v0_min",
    "integrity_host_v0_min_coexistence_distributed_network_v0_min",
}


class LocalRelevanceMediumReadOnlyContinuationBoundaryTests(unittest.TestCase):
    def safe_json_filename(self, name: Any, index: int | None = None) -> str:
        safe = str(name)
        safe = safe.replace("/", "_").replace("\\", "_")
        safe = safe.replace(" ", "_")
        safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_json(self, path: Path, value: Mapping[str, Any] | list[Any]) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")
        return path

    def false_non_claims(self) -> dict[str, bool]:
        return {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS}

    def lineage_true(self) -> dict[str, bool]:
        return {key: True for key in LINEAGE_TRUE_FIELDS}

    def artifact(
        self,
        spec: Mapping[str, Any],
        omit_object_fields: set[str] | None = None,
        explanatory_true: bool = False,
        hostile_sentinels: bool = False,
    ) -> dict[str, Any]:
        false_fields = self.false_non_claims()
        true_fields = dict(spec["true_fields"])
        true_fields.update(self.lineage_true())
        selected_object = {
            spec["type_field"]: spec["type_value"],
            spec["scope_field"]: spec["scope_value"],
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            **true_fields,
            **false_fields,
        }
        for field in omit_object_fields or set():
            selected_object.pop(field, None)

        statement = {
            "selected_command_is_state": True,
            **true_fields,
            **false_fields,
        }
        summary = copy.deepcopy(statement)
        non_meaning = {
            **self.lineage_true(),
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        if explanatory_true:
            for section in (statement, summary, non_meaning):
                section.update(
                    {
                        "continuation_created_false_posture": True,
                        "continuation_not_created": True,
                        "runtime_hosting_not_created": True,
                        "runtime_loop_not_created": True,
                        "daemon_behavior_not_created": True,
                        "raw_state_body_embedded_false_posture": True,
                        "state_mutation_performed_false_posture": True,
                        "state_update_performed_false_posture": True,
                        "older_runtime_authority_import_refusal_preserved": True,
                        "result_level_non_claims_canonical_false": True,
                        "follow_on_not_authorized": True,
                        "future_continuation_may_be_considered": True,
                    }
                )

        artifact = {
            "result_version": resolver.RESULT_VERSION,
            "resolver_module": f"synthetic_{spec['name']}_resolver",
            "outcome": spec["outcome"],
            "failed_check_count": 0,
            spec["object_key"]: selected_object,
            f"{spec['object_key']}_statement": statement,
            f"{spec['object_key']}_summary": summary,
            f"{spec['object_key']}_non_meaning": non_meaning,
            "non_claims": false_fields,
            f"{spec['object_key']}_checks": [
                {
                    "check_name": "synthetic false posture preservation",
                    "passed": True,
                    "actual_posture": False,
                }
            ],
        }
        if explanatory_true:
            artifact.update(
                {
                    "metadata": {"continuation_not_created": True},
                    "explanatory_posture": {"runtime_loop_not_created": True},
                    "basis_commentary": {"daemon_behavior_not_created": True},
                    "false_posture_preserved": {"raw_state_body_embedded_false_posture": True},
                    "non_claim_preservation": {"result_level_non_claims_canonical_false": True},
                    "lineage_evidence": {"future_continuation_may_be_considered": True},
                    "checks": [
                        {
                            "check_name": "continuation_created false posture remains false",
                            "passed": True,
                            "actual_posture": True,
                        }
                    ],
                }
            )
        if hostile_sentinels:
            artifact["raw_full_prior_artifact_body"] = HOSTILE_SENTINELS[0]
            artifact["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            selected_object["raw_state_body"] = HOSTILE_SENTINELS[-3]
            selected_object["older_runtime_authority_body"] = HOSTILE_SENTINELS[-2]
        return artifact

    def write_synthetic_artifacts(
        self,
        root: Path,
        case_name: str = "clean",
        omit_object_fields: Mapping[str, set[str]] | None = None,
        mutators: Mapping[str, Callable[[dict[str, Any]], None]] | None = None,
        explanatory_true: bool = False,
        hostile_sentinels: bool = False,
    ) -> tuple[dict[str, Path], dict[str, dict[str, Any]]]:
        paths: dict[str, Path] = {}
        artifacts: dict[str, dict[str, Any]] = {}
        for index, spec in enumerate(BASIS):
            artifact = self.artifact(
                spec,
                omit_object_fields=set((omit_object_fields or {}).get(spec["name"], set())),
                explanatory_true=explanatory_true,
                hostile_sentinels=hostile_sentinels,
            )
            if mutators and spec["name"] in mutators:
                mutators[spec["name"]](artifact)
            path = root / f"{index:02d}_{spec['name']}_{self.safe_json_filename(case_name)}"
            self.write_json(path, artifact)
            paths[spec["request_key"]] = path
            artifacts[spec["name"]] = artifact
        return paths, artifacts

    def clean_request(self, paths: Mapping[str, Path]) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_continuation_boundary_v0_min_request(
            local_relevance_medium_read_only_continuation_boundary_id=(
                "local_relevance_medium_read_only_continuation_boundary_001"
            ),
            **paths,
        )

    def resolve_clean_synthetic(
        self,
        root: Path,
        **kwargs: Any,
    ) -> tuple[dict[str, Any], dict[str, Path], dict[str, dict[str, Any]], dict[str, Any]]:
        paths, artifacts = self.write_synthetic_artifacts(root, **kwargs)
        request = self.clean_request(paths)
        result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
            request
        )
        return result, paths, artifacts, request

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_continuation_boundary"]

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_continuation_boundary_statement"]

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return resolver.build_local_relevance_medium_read_only_continuation_boundary_v0_min_summary(
            result
        )

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        return list(result.get("local_relevance_medium_read_only_continuation_boundary_checks", []))

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def block_code(self, result: Mapping[str, Any]) -> Any:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_same_or_stable_artifact_path(self, actual: Any, expected: Any) -> None:
        actual_path = Path(str(actual))
        expected_path = Path(str(expected))
        if actual_path.exists() and expected_path.exists():
            self.assertEqual(actual_path.resolve(), expected_path.resolve())
            return
        if actual_path.is_absolute() and expected_path.is_absolute():
            self.assertEqual(actual_path, expected_path)
            return
        self.assertEqual(actual_path.name, expected_path.name)

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                emitted = check.get(key)
                if emitted is not None:
                    self.assertIn(emitted, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIs(type(non_claims[key]), bool, key)
        self.assertNotIn("future_continuation_may_be_considered", resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertNotIn("future_continuation_may_be_considered", non_claims)

    def assert_continuation_boundary_non_claims(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False, key)
            self.assertIs(type(boundary[key]), bool, key)
        self.assertIs(boundary["future_continuation_may_be_considered"], result["outcome"] == resolver.OUTCOME_RECORDED)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_continuation_boundary_non_claims(result)

    def assert_boundary_wrapper_separated(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in FORBIDDEN_WRAPPER_FIELDS_IN_BOUNDARY:
            self.assertNotIn(key, boundary)

    def assert_failure_lineage_preserved(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        statement = self.statement(result)
        summary = self.summary(result)
        non_meaning = result["local_relevance_medium_read_only_continuation_boundary_non_meaning"]
        for key in LINEAGE_TRUE_FIELDS:
            self.assertIs(boundary.get(key), True, key)
            self.assertIs(statement.get(key), True, key)
            self.assertIs(summary.get(key), True, key)
        for key in NAMED_FAILURE_FALSE_FIELDS:
            self.assertIs(boundary.get(key), False, key)
            self.assertIs(result["non_claims"].get(key), False, key)
        for prefix in (
            "second_operation_boundary_v1_failure",
            "prior_result_cycle_v1_failure",
            "prior_result_boundary_v1_failure",
            "runtime_v0_failure",
            "runtime_v2_failure",
            "runtime_boundary_v0_failure",
        ):
            self.assertIs(non_meaning.get(f"{prefix}_not_repaired"), True)
            self.assertIs(non_meaning.get(f"{prefix}_not_hidden"), True)
            self.assertIs(non_meaning.get(f"{prefix}_not_claimed_passed"), True)

    def assert_boundary_core(
        self,
        result: Mapping[str, Any],
        paths: Mapping[str, Path],
    ) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assertTrue(EXPECTED_WRAPPER_SECTIONS.issubset(result.keys()))
        summary = self.summary(result)
        self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_id"], "local_relevance_medium_read_only_continuation_boundary_001")
        self.assertEqual(boundary["boundary_type"], BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.RESULT_VERSION)
        self.assertEqual(boundary["boundary_scope"], BOUNDARY_SCOPE)
        for spec in BASIS:
            prefix = spec["basis_prefix"]
            self.assert_same_or_stable_artifact_path(
                boundary[f"{prefix}_artifact"],
                paths[spec["request_key"]],
            )
            self.assertEqual(boundary[f"{prefix}_outcome"], spec["outcome"])
            self.assertEqual(boundary[f"{prefix}_result_version"], resolver.RESULT_VERSION)
            self.assertEqual(boundary[f"{prefix}_failed_check_count"], 0)

        self.assertEqual(boundary["selected_command"], SELECTED_COMMAND)
        self.assertIs(boundary["selected_command_is_state"], True)
        for field in POSITIVE_FIELDS:
            self.assertIs(boundary[field], True, field)
        self.assertEqual(boundary["operation_sequence_index"], 2)
        self.assertIs(boundary["future_continuation_may_be_considered"], True)
        self.assert_continuation_boundary_non_claims(result)
        self.assert_boundary_wrapper_separated(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_failure_lineage_preserved(result)

        statement = self.statement(result)
        self.assertIs(statement["local_relevance_medium_read_only_continuation_boundary_recorded"], True)
        self.assertIs(statement["future_continuation_may_be_considered"], True)
        self.assertIs(statement["continuation_created"], False)
        self.assertIs(statement["runtime_hosting_created"], False)
        self.assertIs(statement["runtime_loop_created"], False)
        self.assertIs(statement["daemon_behavior_created"], False)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["result_level_non_claims_canonical_false"], True)
        for spec in BASIS:
            preserved_key = f"{spec['basis_prefix']}_artifact_preserved"
            self.assertIs(statement[preserved_key], True)

    def assert_no_hostile_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_output_path_not_under_prior_roots(self, path: Path) -> None:
        self.assertIn(
            "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_continuation_boundary_v0_min",
            path.parts,
        )
        for name in FORBIDDEN_OUTPUT_ROOT_NAMES:
            self.assertNotIn(name, path.parts)

    def test_public_api_constants_and_builder_defaults(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_continuation_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_continuation_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_continuation_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_continuation_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_continuation_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)), name)
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_BOUNDARY_TYPE_VALUES",
            "SUPPORTED_BOUNDARY_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_continuation_boundary_v0_min",
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_continuation_boundary_v0_min"
            )
        )
        self.assertIn(BOUNDARY_TYPE, resolver.SUPPORTED_BOUNDARY_TYPE_VALUES)
        self.assertIn(BOUNDARY_SCOPE, resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, SELECTED_COMMAND)
        for key in (
            "continuation_created",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "second_operation_boundary_v1_failure_repaired",
            "prior_result_cycle_v1_failure_repaired",
            "prior_result_boundary_v1_failure_repaired",
            "runtime_v0_failure_repaired",
            "runtime_v2_failure_repaired",
            "runtime_boundary_v0_failure_repaired",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertNotIn("future_continuation_may_be_considered", resolver.REQUIRED_FALSE_NON_CLAIMS)
        for code in (
            "CONTINUATION_CREATED",
            "RAW_STATE_BODY_EMBEDDED",
            "STATE_MUTATION_PERFORMED",
            "STATE_UPDATE_PERFORMED",
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "RUNTIME_AUTHORITY_IMPORTED",
            "SECOND_OPERATION_BOUNDARY_V1_FAILURE_REPAIRED",
            "PRIOR_RESULT_CYCLE_V1_FAILURE_REPAIRED",
            "PRIOR_RESULT_BOUNDARY_V1_FAILURE_REPAIRED",
            "RUNTIME_V0_FAILURE_REPAIRED",
            "RUNTIME_V2_FAILURE_REPAIRED",
            "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        self.assertEqual(set(resolver.OUTCOME_FAMILY), EXPECTED_OUTCOME_FAMILY)

        request = resolver.build_declared_local_relevance_medium_read_only_continuation_boundary_v0_min_request()
        for key, suffix in DEFAULT_SUFFIXES.items():
            self.assertTrue(str(request[key]).endswith(suffix), key)
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        self.assertEqual(request["boundary_type"], BOUNDARY_TYPE)
        self.assertEqual(request["boundary_scope"], BOUNDARY_SCOPE)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, request["declared_non_claims"])
            self.assertIs(request["declared_non_claims"][key], False)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result, paths, _, _ = self.resolve_clean_synthetic(Path(temp_dir))
            self.assertIsInstance(result, dict)
            self.assert_boundary_core(result, paths)

    def test_successful_recorded_result_from_default_live_artifacts_if_present(self) -> None:
        request = resolver.build_declared_local_relevance_medium_read_only_continuation_boundary_v0_min_request()
        missing = []
        for key in DEFAULT_SUFFIXES:
            path = Path(request[key])
            read_path = path if path.is_absolute() else REPO_ROOT / path
            if not read_path.exists():
                missing.append(key)
        if missing:
            self.skipTest(f"default live artifacts missing: {', '.join(missing)}")

        result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
            request
        )
        default_paths = {key: (REPO_ROOT / Path(request[key])) for key in DEFAULT_SUFFIXES}
        self.assert_boundary_core(result, default_paths)
        boundary = self.boundary(result)
        for spec in BASIS:
            self.assert_same_or_stable_artifact_path(
                boundary[f"{spec['basis_prefix']}_artifact"],
                default_paths[spec["request_key"]],
            )

    def test_positive_basis_derivation_regression(self) -> None:
        omit_fields = {
            "second_operation": {
                "selected_second_operation_recorded",
                "second_operation_created",
                "second_operation_local_only",
                "second_operation_read_only",
                "second_operation_basis_reference_only",
                "second_operation_sequence_index_is_2",
                "second_operation_boundary_v1_failure_evidence_preserved",
                "second_operation_boundary_v2_successor_evidence_preserved",
                "prior_result_cycle_v1_failure_evidence_preserved",
                "prior_result_cycle_v2_successor_evidence_preserved",
            },
            "second_operation_boundary": {
                "selected_second_operation_boundary_recorded",
                "future_second_operation_may_be_considered",
            },
            "prior_result_reentry_cycle": {"selected_prior_result_reentry_cycle_recorded"},
            "prior_result_reentry_boundary": {"selected_prior_result_reentry_boundary_recorded"},
            "runtime_held_reentry_boundary": {"selected_runtime_held_reentry_boundary_recorded"},
            "runtime_held_state_boundary": {"selected_runtime_held_state_boundary_recorded"},
            "runtime_boundary": {"selected_runtime_boundary_recorded"},
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            result, paths, _, _ = self.resolve_clean_synthetic(
                Path(temp_dir),
                omit_object_fields=omit_fields,
            )
            self.assert_boundary_core(result, paths)
            boundary = self.boundary(result)
            for fields in omit_fields.values():
                for field in fields:
                    self.assertIs(boundary[field], True, field)
            self.assertIs(boundary["continuation_created"], False)
            self.assertIs(boundary["raw_state_body_embedded"], False)
            self.assertIs(boundary["state_mutation_performed"], False)
            self.assertIs(boundary["state_update_performed"], False)
            self.assertIs(boundary["older_runtime_lineage_imported_as_authority"], False)
            self.assertIs(boundary["follow_on_work_authorized"], False)

    def test_forbidden_false_posture_uses_exact_extraction_only(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result, paths, _, _ = self.resolve_clean_synthetic(
                Path(temp_dir),
                explanatory_true=True,
            )
            self.assert_boundary_core(result, paths)
            boundary = self.boundary(result)
            for field in EXACT_FORBIDDEN_FIELDS:
                self.assertIs(boundary[field], False, field)
                self.assertIs(result["non_claims"][field], False, field)

    def test_exact_selected_object_forbidden_true_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for index, field in enumerate(EXACT_FORBIDDEN_FIELDS):
                with self.subTest(field=field):
                    def mutate(artifact: dict[str, Any], field: str = field) -> None:
                        artifact["local_relevance_medium_read_only_second_operation"][field] = True

                    paths, _ = self.write_synthetic_artifacts(
                        root,
                        self.safe_json_filename(field, index),
                        mutators={"second_operation": mutate},
                    )
                    request = self.clean_request(paths)
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), field.upper())
                    self.assert_continuation_boundary_non_claims(result)

    def test_exact_top_level_non_claim_true_blocks_when_object_key_absent(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for index, field in enumerate(EXACT_FORBIDDEN_FIELDS):
                with self.subTest(field=field):
                    def mutate(artifact: dict[str, Any], field: str = field) -> None:
                        artifact["local_relevance_medium_read_only_second_operation"].pop(field, None)
                        artifact["non_claims"][field] = True

                    paths, _ = self.write_synthetic_artifacts(
                        root,
                        self.safe_json_filename(f"non_claim_{field}", index),
                        mutators={"second_operation": mutate},
                    )
                    request = self.clean_request(paths)
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), field.upper())
                    self.assert_continuation_boundary_non_claims(result)

    def test_declared_top_level_blocking_cases(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths, _ = self.write_synthetic_artifacts(Path(temp_dir))
            for field, expected_code in TOP_LEVEL_BLOCK_CASES:
                with self.subTest(field=field):
                    request = self.clean_request(paths)
                    request[field] = True
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_declared_non_claim_canonicalization_for_each_required_false_key(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths, _ = self.write_synthetic_artifacts(Path(temp_dir))
            clean_request = self.clean_request(paths)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_continuation_boundary_non_claims(result)

    def test_declared_non_claim_missing_and_non_bool_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths, _ = self.write_synthetic_artifacts(Path(temp_dir))
            clean_request = self.clean_request(paths)
            for key in ("continuation_created", "raw_state_body_embedded", "authorization_token_reused"):
                with self.subTest(missing=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"].pop(key)
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                with self.subTest(non_bool=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = "false"
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_representative_blocking_behavior(self) -> None:
        def artifact_mutator(name: str, field: str, value: Any) -> dict[str, Callable[[dict[str, Any]], None]]:
            object_key = BASIS_BY_NAME[name]["object_key"]

            def mutate(artifact: dict[str, Any]) -> None:
                artifact[object_key][field] = value
                artifact[f"{object_key}_statement"][field] = value
                artifact[f"{object_key}_summary"][field] = value

            return {name: mutate}

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            cases: list[tuple[str, Callable[[dict[str, Path]], None] | None, Mapping[str, Callable[[dict[str, Any]], None]] | None, Callable[[dict[str, Any]], None] | None, str | None]] = [
                ("missing request", None, None, lambda request: request.clear(), None),
                ("explicit block intent", None, None, lambda request: request.__setitem__("local_relevance_medium_read_only_continuation_boundary_intent", "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY"), "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_BLOCK_REQUESTED"),
                ("unsupported intent", None, None, lambda request: request.__setitem__("local_relevance_medium_read_only_continuation_boundary_intent", "UNSUPPORTED"), "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_INTENT_UNSUPPORTED"),
                ("selected command missing", None, None, lambda request: request.pop("selected_command", None), "SELECTED_COMMAND_MISSING"),
                ("selected command not state", None, None, lambda request: request.__setitem__("selected_command", "status"), "SELECTED_COMMAND_NOT_STATE"),
                ("boundary type missing", None, None, lambda request: request.pop("boundary_type", None), "BOUNDARY_TYPE_MISSING"),
                ("boundary type wrong", None, None, lambda request: request.__setitem__("boundary_type", "LOCAL_RELEVANCE_MEDIUM_CONTINUATION"), "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY"),
                ("boundary scope missing", None, None, lambda request: request.pop("boundary_scope", None), "BOUNDARY_SCOPE_MISSING"),
                ("boundary scope wrong", None, None, lambda request: request.__setitem__("boundary_scope", "GENERAL_CONTINUATION"), "BOUNDARY_SCOPE_NOT_SELECTED_CONTINUATION_CONSIDERATION_ONLY"),
                ("second operation not created", None, artifact_mutator("second_operation", "second_operation_created", False), None, "SECOND_OPERATION_NOT_CREATED"),
                ("second operation not local only", None, artifact_mutator("second_operation", "second_operation_local_only", False), None, "SECOND_OPERATION_LOCAL_ONLY_NOT_TRUE"),
                ("second operation not read only", None, artifact_mutator("second_operation", "second_operation_read_only", False), None, "SECOND_OPERATION_READ_ONLY_NOT_TRUE"),
                ("second operation not basis reference only", None, artifact_mutator("second_operation", "second_operation_basis_reference_only", False), None, "SECOND_OPERATION_BASIS_REFERENCE_ONLY_NOT_TRUE"),
                ("second operation sequence not 2", None, artifact_mutator("second_operation", "operation_sequence_index", 3), None, "OPERATION_SEQUENCE_INDEX_NOT_2"),
                ("second operation boundary future false", None, artifact_mutator("second_operation_boundary", "future_second_operation_may_be_considered", False), None, "FUTURE_SECOND_OPERATION_MAY_NOT_BE_CONSIDERED"),
                ("prior result cycle not recorded", None, artifact_mutator("prior_result_reentry_cycle", "selected_prior_result_reentry_cycle_recorded", False), None, "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED"),
                ("prior result boundary future false", None, artifact_mutator("prior_result_reentry_boundary", "future_prior_result_reentry_cycle_may_be_considered", False), None, "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED"),
                ("runtime held reentry not created", None, artifact_mutator("runtime_held_reentry", "runtime_held_reentry_created", False), None, "RUNTIME_HELD_REENTRY_NOT_CREATED"),
                ("runtime held state not created", None, artifact_mutator("runtime_held_state", "runtime_held_state_created", False), None, "RUNTIME_HELD_STATE_NOT_CREATED"),
                ("runtime not created", None, artifact_mutator("runtime", "runtime_created", False), None, "RUNTIME_NOT_CREATED"),
                ("runtime permission not created", None, artifact_mutator("runtime_permission", "runtime_permission_created", False), None, "RUNTIME_PERMISSION_NOT_CREATED"),
                ("operation execution not performed", None, artifact_mutator("operation_execution", "operation_execution_performed", False), None, "OPERATION_EXECUTION_NOT_PERFORMED"),
                ("required non-claim missing", None, None, lambda request: request["declared_non_claims"].pop("continuation_created"), "NON_CLAIM_MISSING_OR_FLIPPED"),
            ]
            for field in (
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
            ):
                cases.append(
                    (
                        field,
                        None,
                        None,
                        lambda request, field=field: request.__setitem__(field, True),
                        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
                        if field.startswith("predecessor_failure_")
                        else field.upper(),
                    )
                )

            for index, spec in enumerate(BASIS):
                cases.extend(
                    [
                        (
                            f"{spec['name']} artifact path missing",
                            None,
                            None,
                            lambda request, key=spec["request_key"]: request.pop(key, None),
                            f"{spec['name'].upper()}_ARTIFACT_PATH_MISSING",
                        ),
                        (
                            f"{spec['name']} artifact unreadable",
                            lambda paths, key=spec["request_key"]: paths.__setitem__(key, root / f"missing_{key}.json"),
                            None,
                            None,
                            f"{spec['name'].upper()}_ARTIFACT_UNREADABLE",
                        ),
                        (
                            f"{spec['name']} artifact not recorded",
                            None,
                            {spec["name"]: lambda artifact: artifact.__setitem__("outcome", "NOPE")},
                            None,
                            f"{spec['name'].upper()}_ARTIFACT_NOT_RECORDED",
                        ),
                        (
                            f"{spec['name']} artifact failed checks present",
                            None,
                            {spec["name"]: lambda artifact: artifact.__setitem__("failed_check_count", 1)},
                            None,
                            f"{spec['name'].upper()}_ARTIFACT_FAILED_CHECKS_PRESENT",
                        ),
                        (
                            f"{spec['name']} artifact version wrong",
                            None,
                            {spec["name"]: lambda artifact: artifact.__setitem__("result_version", "9.9.9")},
                            None,
                            f"{spec['name'].upper()}_ARTIFACT_VERSION_NOT_0_1_0",
                        ),
                    ]
                )
                cases.append(
                    (
                        f"{spec['name']} artifact array",
                        None,
                        {spec["name"]: lambda artifact, name=spec["name"]: artifact.clear()},
                        None,
                        f"{spec['name'].upper()}_ARTIFACT_UNREADABLE",
                    )
                )

            for index, (label, path_edit, mutators, request_edit, expected_code) in enumerate(cases):
                with self.subTest(label=label):
                    paths, _ = self.write_synthetic_artifacts(
                        root,
                        self.safe_json_filename(label, index),
                        mutators=mutators,
                    )
                    if "artifact array" in label:
                        affected = label.split(" artifact array", 1)[0]
                        self.write_json(paths[BASIS_BY_NAME[affected]["request_key"]], [])
                    if path_edit is not None:
                        path_edit(paths)
                    request = self.clean_request(paths)
                    if request_edit is not None:
                        request_edit(request)
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    if expected_code is not None:
                        self.assertEqual(self.block_code(result), expected_code)

    def test_missing_and_non_mapping_requests_block(self) -> None:
        missing_result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
            "not a mapping"
        )
        self.assert_blocked_with_public_code(missing_result)
        self.assertEqual(
            self.block_code(missing_result),
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BOUNDARY_REQUEST_MALFORMED",
        )

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result, paths, _, _ = self.resolve_clean_synthetic(Path(temp_dir))
            self.assert_boundary_core(result, paths)
            boundary = self.boundary(result)
            self.assertEqual(boundary["boundary_type"], BOUNDARY_TYPE)
            self.assertEqual(boundary["boundary_scope"], BOUNDARY_SCOPE)
            self.assertEqual(boundary["selected_command"], SELECTED_COMMAND)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            for outcome in EXPECTED_OUTCOME_FAMILY:
                self.assertIn(outcome, resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn(resolver.OUTCOME_RECORDED, serialized)
            self.assertIn(BOUNDARY_TYPE, serialized)
            self.assertIn(BOUNDARY_SCOPE, serialized)
            self.assertIn('"state"', serialized)
            self.assertIn(resolver.RESOLVER_MODULE, serialized)
            self.assertNotIn("[REDACTED", boundary["boundary_type"])
            self.assertNotIn("[REDACTED", boundary["boundary_scope"])

    def test_raw_hidden_older_runtime_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths, artifacts = self.write_synthetic_artifacts(
                Path(temp_dir),
                "hostile",
                hostile_sentinels=True,
            )
            request = self.clean_request(paths)
            request["raw_continuation_boundary_body"] = HOSTILE_SENTINELS[0]
            request["raw_continuation_body"] = HOSTILE_SENTINELS[1]
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            original_request = copy.deepcopy(request)
            original_artifacts = copy.deepcopy(artifacts)
            result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
            self.assert_no_hostile_sentinels(result)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn(BOUNDARY_TYPE, serialized)
            self.assertIn(BOUNDARY_SCOPE, serialized)
            self.assertIn(SELECTED_COMMAND, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assert_continuation_boundary_non_claims(result)
            self.assertEqual(request, original_request)
            self.assertEqual(artifacts, original_artifacts)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            paths, _ = self.write_synthetic_artifacts(root)
            request = self.clean_request(paths)
            request_path = self.write_json(root / "request.json", request)
            result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min_from_path(
                request_path
            )
            self.assert_boundary_core(result, paths)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_with_public_code(malformed_result)

            array_path = self.write_json(root / "array.json", [])
            array_result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min_from_path(
                array_path
            )
            self.assert_blocked_with_public_code(array_result)

            missing_result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min_from_path(
                root / "missing_request.json"
            )
            self.assert_blocked_with_public_code(missing_result)

            output_root = root / "artifacts" / (
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_continuation_boundary_v0_min"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_continuation_boundary_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_continuation_boundary_v0_min_result(
                    result
                )
            self.assertTrue(first_path.parent.exists())
            self.assertTrue(second_path.parent.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn("local_relevance_medium_read_only_continuation_boundary_v0_min", str(first_path))
            self.assert_output_path_not_under_prior_roots(first_path)
            self.assert_output_path_not_under_prior_roots(second_path)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths, artifacts = self.write_synthetic_artifacts(
                Path(temp_dir),
                "non_mutation",
                explanatory_true=True,
                hostile_sentinels=True,
            )
            request = self.clean_request(paths)
            request["nested_payload"] = {"raw_state_body": HOSTILE_SENTINELS[-3]}
            request_before = copy.deepcopy(request)
            artifacts_before = copy.deepcopy(artifacts)
            result = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assertEqual(request, request_before)
            self.assertEqual(artifacts, artifacts_before)
            self.assertEqual(request["selected_command"], SELECTED_COMMAND)
            self.assertEqual(request["boundary_type"], BOUNDARY_TYPE)
            self.assertEqual(request["boundary_scope"], BOUNDARY_SCOPE)
            for key in DEFAULT_SUFFIXES:
                self.assertEqual(request[key], request_before[key])

    def test_failure_lineage_and_predecessor_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result, paths, _, _ = self.resolve_clean_synthetic(Path(temp_dir))
            self.assert_boundary_core(result, paths)
            summary = self.summary(result)
            self.assertIs(summary.get("predecessor_failure_evidence_preserved"), True)
            self.assertIs(summary.get("result_level_non_claims_canonical_false"), True)
            self.assertIs(summary.get("consumed_request_token_remains_closed"), True)
            self.assertIs(summary.get("authorization_token_reuse_blocked"), True)
            self.assertIs(summary.get("older_runtime_lineage_not_imported_as_authority"), True)
            self.assertIs(summary.get("older_runtime_permission_not_treated_as_current"), True)
            self.assertIs(summary.get("runtime_authority_not_imported"), True)
            self.assertIs(summary.get("raw_state_body_embedded"), False)
            self.assertIs(summary.get("state_mutation_performed"), False)
            self.assertIs(summary.get("state_update_performed"), False)
            self.assertIs(summary.get("future_continuation_may_be_considered"), True)
            self.assertIs(summary.get("continuation_not_created"), True)
            self.assertIs(summary.get("runtime_hosting_not_created"), True)
            self.assertIs(summary.get("runtime_loop_not_created"), True)
            self.assertIs(summary.get("daemon_behavior_not_created"), True)

            for field, expected_code in TOP_LEVEL_BLOCK_CASES:
                if "failure" not in field:
                    continue
                with self.subTest(failure_flip=field):
                    request = self.clean_request(paths)
                    request[field] = True
                    blocked = resolver.resolve_local_relevance_medium_read_only_continuation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(blocked)
                    self.assertEqual(self.block_code(blocked), expected_code)


if __name__ == "__main__":
    unittest.main()
