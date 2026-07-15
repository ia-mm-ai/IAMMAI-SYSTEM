"""V2 tests for the local read-only prior-result re-entry cycle resolver.

This suite is additive successor evidence for
resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2.
It preserves the v1 prior-result re-entry cycle resolver/test as failed-lineage
evidence: synthetic v1 tests passed, while the default live-artifact v1 test
blocked because v1 over-read explanatory true fields in statements, summaries,
non-meaning sections, checks, and preservation sections.

The v2 target records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE object only. These
tests prove that v2 uses exact selected-object false-posture keys, with fallback
only to exact top-level non_claims, and does not treat explanatory true values
as forbidden creation.
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

import resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2 as resolver  # noqa: E402


CYCLE_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE"
CYCLE_SCOPE = "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY"
SELECTED_COMMAND = "state"

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_prior_result_reentry_cycle_metadata",
    "declared_local_relevance_medium_read_only_prior_result_reentry_cycle_question",
    "selected_prior_result_reentry_boundary_artifact_basis",
    "selected_runtime_held_reentry_artifact_basis",
    "selected_runtime_held_reentry_boundary_artifact_basis",
    "selected_runtime_held_state_artifact_basis",
    "selected_runtime_held_state_boundary_artifact_basis",
    "selected_runtime_artifact_basis",
    "selected_runtime_boundary_artifact_basis",
    "selected_runtime_permission_artifact_basis",
    "selected_operation_execution_artifact_basis",
    "local_relevance_medium_read_only_prior_result_reentry_cycle",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_checks",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_statement",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_summary",
)

FORBIDDEN_CYCLE_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_checks",
    "non_claims",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_summary",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_metadata",
)

EXPECTED_OUTCOME_FAMILY = {
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUIRES_ADDITIONAL_BASIS",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_BLOCKED",
}

DEFAULT_ARTIFACT_SUFFIXES = {
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

DEFAULT_ARTIFACT_PATHS = {
    "selected_prior_result_reentry_boundary_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min"
    / DEFAULT_ARTIFACT_SUFFIXES["selected_prior_result_reentry_boundary_artifact"],
    "selected_runtime_held_reentry_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_v0_min"
    / DEFAULT_ARTIFACT_SUFFIXES["selected_runtime_held_reentry_artifact"],
    "selected_runtime_held_reentry_boundary_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min"
    / DEFAULT_ARTIFACT_SUFFIXES["selected_runtime_held_reentry_boundary_artifact"],
    "selected_runtime_held_state_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_v0_min"
    / DEFAULT_ARTIFACT_SUFFIXES["selected_runtime_held_state_artifact"],
    "selected_runtime_held_state_boundary_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min"
    / DEFAULT_ARTIFACT_SUFFIXES["selected_runtime_held_state_boundary_artifact"],
    "selected_runtime_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v3"
    / DEFAULT_ARTIFACT_SUFFIXES["selected_runtime_artifact"],
    "selected_runtime_boundary_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min_v2"
    / DEFAULT_ARTIFACT_SUFFIXES["selected_runtime_boundary_artifact"],
    "selected_runtime_permission_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min"
    / DEFAULT_ARTIFACT_SUFFIXES["selected_runtime_permission_artifact"],
    "selected_operation_execution_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min"
    / DEFAULT_ARTIFACT_SUFFIXES["selected_operation_execution_artifact"],
}

ARTIFACT_DEFINITIONS = (
    {
        "name": "prior_result_reentry_boundary",
        "request_key": "selected_prior_result_reentry_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_prior_result_reentry_boundary",
        "basis_prefix": "basis_prior_result_reentry_boundary",
        "block_prefix": "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_RECORDED",
        "type_key": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY",
        "scope_key": "boundary_scope",
        "scope_value": "SELECTED_PRIOR_RESULT_REENTRY_CONSIDERATION_ONLY",
        "true_fields": {
            "selected_prior_result_reentry_boundary_recorded": True,
            "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded": True,
            "future_prior_result_reentry_cycle_may_be_considered": True,
            "selected_runtime_held_reentry_recorded": True,
            "runtime_held_reentry_created": True,
            "runtime_held_reentry_local_only": True,
            "runtime_held_reentry_read_only": True,
            "held_reentry_basis_reference_only": True,
        },
    },
    {
        "name": "runtime_held_reentry",
        "request_key": "selected_runtime_held_reentry_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry",
        "basis_prefix": "basis_runtime_held_reentry",
        "block_prefix": "RUNTIME_HELD_REENTRY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_RECORDED",
        "type_key": "held_reentry_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY",
        "scope_key": "held_reentry_scope",
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
        "block_prefix": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY_RECORDED",
        "type_key": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY",
        "scope_key": "boundary_scope",
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
        "block_prefix": "RUNTIME_HELD_STATE_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_RECORDED",
        "type_key": "held_state_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE",
        "scope_key": "held_state_scope",
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
        "block_prefix": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_RECORDED",
        "type_key": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY",
        "scope_key": "boundary_scope",
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
        "block_prefix": "RUNTIME_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED",
        "type_key": "runtime_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME",
        "scope_key": "runtime_scope",
        "scope_value": "SELECTED_RUNTIME_ONLY",
        "true_fields": {
            "selected_runtime_recorded": True,
            "runtime_recorded": True,
            "local_relevance_medium_read_only_runtime_recorded": True,
            "runtime_created": True,
            "runtime_local_only": True,
            "runtime_read_only": True,
            "runtime_permission_basis_recorded": True,
            "operation_execution_basis_recorded": True,
        },
    },
    {
        "name": "runtime_boundary",
        "request_key": "selected_runtime_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_boundary",
        "basis_prefix": "basis_runtime_boundary",
        "block_prefix": "RUNTIME_BOUNDARY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED",
        "type_key": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
        "scope_key": "boundary_scope",
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
        "block_prefix": "RUNTIME_PERMISSION_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED",
        "type_key": "runtime_permission_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
        "scope_key": "runtime_permission_scope",
        "scope_value": "SELECTED_RUNTIME_PERMISSION_ONLY",
        "true_fields": {
            "selected_runtime_permission_recorded": True,
            "runtime_permission_recorded": True,
            "local_relevance_medium_read_only_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
            "selected_operation_execution_basis_recorded": True,
        },
    },
    {
        "name": "operation_execution",
        "request_key": "selected_operation_execution_artifact",
        "object_key": "local_relevance_medium_read_only_operation_execution",
        "basis_prefix": "basis_operation_execution",
        "block_prefix": "OPERATION_EXECUTION_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
        "type_key": "operation_execution_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
        "scope_key": "operation_execution_scope",
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

CYCLE_TRUE_FIELDS = (
    "selected_command_is_state",
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
    "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded",
    "prior_result_reentry_cycle_created",
    "prior_result_reentry_cycle_local_only",
    "prior_result_reentry_cycle_read_only",
    "cycle_basis_reference_only",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "prior_result_boundary_v1_failure_evidence_preserved",
    "prior_result_boundary_v2_successor_evidence_preserved",
)

CYCLE_FALSE_FIELDS = (
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
    "follow_on_work_authorized",
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

EXACT_FALSE_KEYS = (
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
    "second_operation_created",
    "continuation_created",
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
    ("second_operation_created", "SECOND_OPERATION_CREATED"),
    ("continuation_created", "CONTINUATION_CREATED"),
    ("runtime_v0_failure_repaired", "RUNTIME_V0_FAILURE_REPAIRED"),
    ("runtime_v0_failure_hidden", "RUNTIME_V0_FAILURE_HIDDEN"),
    ("runtime_v0_failure_claimed_passed", "RUNTIME_V0_FAILURE_CLAIMED_PASSED"),
    ("runtime_v2_failure_repaired", "RUNTIME_V2_FAILURE_REPAIRED"),
    ("runtime_v2_failure_hidden", "RUNTIME_V2_FAILURE_HIDDEN"),
    ("runtime_v2_failure_claimed_passed", "RUNTIME_V2_FAILURE_CLAIMED_PASSED"),
    ("runtime_boundary_v0_failure_repaired", "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED"),
    ("runtime_boundary_v0_failure_hidden", "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN"),
    ("runtime_boundary_v0_failure_claimed_passed", "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED"),
    ("prior_result_boundary_v1_failure_repaired", "PRIOR_RESULT_BOUNDARY_V1_FAILURE_REPAIRED"),
    ("prior_result_boundary_v1_failure_hidden", "PRIOR_RESULT_BOUNDARY_V1_FAILURE_HIDDEN"),
    ("prior_result_boundary_v1_failure_claimed_passed", "PRIOR_RESULT_BOUNDARY_V1_FAILURE_CLAIMED_PASSED"),
)

HOSTILE_SENTINELS = (
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
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

FORBIDDEN_OUTPUT_ROOTS = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_v0_min",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_v0_min",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v3",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v2",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min_v2",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min",
    REPO_ROOT / "artifacts" / "integrity_host_v0_min_coexistence_source_transfer_v0_min",
    REPO_ROOT / "artifacts" / "integrity_host_v0_min_coexistence_source_receipt_v0_min",
    REPO_ROOT / "artifacts" / "integrity_host_v0_min_coexistence_public_api_v0_min",
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_participant_facing_interface_v0_min",
    REPO_ROOT / "artifacts" / "integrity_host_v0_min_coexistence_distributed_network_v0_min",
)


class LocalRelevanceMediumReadOnlyPriorResultReentryCycleV0MinV2Test(unittest.TestCase):
    """Bounded tests for one selected-state prior-result re-entry cycle v2 object."""

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
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

    def write_json(self, path: Path, payload: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get(
            "local_relevance_medium_read_only_prior_result_reentry_cycle_summary"
        )
        if isinstance(summary, Mapping):
            return summary
        return resolver.build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_summary(
            result
        )

    def cycle(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        cycle = result.get("local_relevance_medium_read_only_prior_result_reentry_cycle")
        self.assertIsInstance(cycle, dict)
        return cycle

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get(
            "local_relevance_medium_read_only_prior_result_reentry_cycle_statement"
        )
        self.assertIsInstance(statement, dict)
        return statement

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get(
            "local_relevance_medium_read_only_prior_result_reentry_cycle_checks", []
        )
        self.assertIsInstance(checks, list)
        return [check for check in checks if isinstance(check, Mapping)]

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if isinstance(block, Mapping):
            return block.get("code") or block.get("block_code")
        return None

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        summary = self.summary(result)
        if isinstance(summary.get("failed_check_count"), int):
            return int(summary["failed_check_count"])
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        summary = self.summary(result)
        if isinstance(summary.get("passed_check_count"), int):
            return int(summary["passed_check_count"])
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def emitted_codes(self, result: Mapping[str, Any]) -> set[str]:
        emitted: set[str] = set()
        code = self.block_code(result)
        if code:
            emitted.add(code)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                value = check.get(key)
                if value:
                    emitted.add(str(value))
        return emitted

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
        try:
            if actual_path.resolve() == expected_path.resolve():
                return
        except OSError:
            pass
        self.assertTrue(
            str(actual).endswith(expected_path.name)
            or str(expected).endswith(actual_path.name),
            f"{actual!r} did not match or stably end with {expected!r}",
        )

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        for code in self.emitted_codes(result):
            self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(type(non_claims[key]), bool)
            self.assertIs(non_claims[key], False, key)
        for key in (
            "prior_result_reentry_cycle_created",
            "prior_result_reentry_cycle_local_only",
            "prior_result_reentry_cycle_read_only",
            "cycle_basis_reference_only",
        ):
            self.assertNotIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
            self.assertNotIn(key, non_claims)

    def assert_prior_result_reentry_cycle_non_claims(
        self, result: Mapping[str, Any]
    ) -> None:
        cycle = self.cycle(result)
        for key in CYCLE_FALSE_FIELDS:
            self.assertIs(cycle.get(key), False, key)
        self.assertIs(cycle.get("raw_state_body_embedded"), False)
        self.assertIs(cycle.get("state_mutation_performed"), False)
        self.assertIs(cycle.get("state_update_performed"), False)
        self.assertIs(cycle.get("second_operation_created"), False)
        self.assertIs(cycle.get("continuation_created"), False)
        self.assertIs(cycle.get("runtime_hosting_created"), False)
        self.assertIs(cycle.get("runtime_loop_created"), False)
        self.assertIs(cycle.get("daemon_behavior_created"), False)
        self.assertIs(cycle.get("public_api_created"), False)
        self.assertIs(cycle.get("participant_facing_interface_created"), False)
        self.assertIs(cycle.get("distributed_network_behavior_created"), False)
        self.assertIs(cycle.get("older_runtime_lineage_imported_as_authority"), False)
        self.assertIs(cycle.get("older_runtime_permission_treated_as_current"), False)
        self.assertIs(cycle.get("runtime_authority_imported"), False)
        self.assertIs(cycle.get("follow_on_work_authorized"), False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_prior_result_reentry_cycle_non_claims(result)

    def assert_cycle_not_wrapper(self, cycle: Mapping[str, Any]) -> None:
        for key in FORBIDDEN_CYCLE_WRAPPER_FIELDS:
            self.assertNotIn(key, cycle)

    def assert_lineage_preserved(self, result: Mapping[str, Any]) -> None:
        cycle = self.cycle(result)
        summary = self.summary(result)
        statement = self.statement(result)
        for key in (
            "runtime_v0_failure_evidence_preserved",
            "runtime_v2_failure_evidence_preserved",
            "runtime_boundary_v0_failure_evidence_preserved",
            "prior_result_boundary_v1_failure_evidence_preserved",
            "prior_result_boundary_v2_successor_evidence_preserved",
        ):
            self.assertIs(cycle.get(key), True)
            self.assertIs(summary.get(key), True)
        self.assertIs(statement.get("prior_result_cycle_v1_failure_evidence_preserved"), True)
        self.assertIn("v1_live_basis_extraction_mismatch_not_repaired_or_claimed_passed", json.dumps(result, sort_keys=True))
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
            "prior_result_boundary_v1_failure_repaired",
            "prior_result_boundary_v1_failure_hidden",
            "prior_result_boundary_v1_failure_claimed_passed",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertIs(result["non_claims"][key], False, key)
        for optional_key in (
            "prior_result_cycle_v1_failure_repaired",
            "prior_result_cycle_v1_failure_hidden",
            "prior_result_cycle_v1_failure_claimed_passed",
        ):
            if optional_key in result["non_claims"]:
                self.assertIs(result["non_claims"][optional_key], False)
        self.assertIs(summary.get("predecessor_failure_evidence_preserved"), True)
        self.assertIs(summary.get("result_level_non_claims_canonical_false"), True)
        self.assertIs(summary.get("consumed_request_token_remains_closed"), True)
        self.assertIs(summary.get("authorization_token_reuse_blocked"), True)

    def assert_explanatory_true_values_did_not_become_posture(
        self, result: Mapping[str, Any]
    ) -> None:
        cycle = self.cycle(result)
        for key in EXACT_FALSE_KEYS:
            self.assertIs(cycle.get(key), False, key)
            self.assertIs(result["non_claims"].get(key), False, key)
        self.assert_prior_result_reentry_cycle_non_claims(result)

    def assert_serialized_result_excludes_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def artifact_payload(
        self,
        definition: Mapping[str, Any],
        object_overrides: Mapping[str, Any] | None = None,
        top_overrides: Mapping[str, Any] | None = None,
        include_explanatory_true_fields: bool = False,
        include_sensitive_payload: bool = False,
    ) -> dict[str, Any]:
        false_fields = {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS}
        false_fields.update(
            {
                "prior_result_reentry_cycle_created": False,
                "prior_result_reentry_cycle_local_only": False,
                "prior_result_reentry_cycle_read_only": False,
                "cycle_basis_reference_only": False,
            }
        )
        object_payload: dict[str, Any] = {
            definition["type_key"]: definition["type_value"],
            definition["scope_key"]: definition["scope_value"],
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
            **false_fields,
            "runtime_v0_failure_evidence_preserved": True,
            "runtime_v2_failure_evidence_preserved": True,
            "runtime_boundary_v0_failure_evidence_preserved": True,
            "prior_result_boundary_v1_failure_evidence_preserved": True,
            "prior_result_boundary_v2_successor_evidence_preserved": True,
            **definition["true_fields"],
        }
        if object_overrides:
            object_payload.update(dict(object_overrides))
        payload: dict[str, Any] = {
            "outcome": definition["outcome"],
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
            "non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
            definition["object_key"]: object_payload,
            f"{definition['object_key']}_statement": {
                "basis_artifact_preserved": True,
                **definition["true_fields"],
            },
            f"{definition['object_key']}_summary": {
                "outcome": definition["outcome"],
                "result_version": resolver.RESULT_VERSION,
                "failed_check_count": 0,
                **definition["true_fields"],
            },
        }
        if include_explanatory_true_fields:
            self.add_misleading_explanatory_true_fields(payload)
        if include_sensitive_payload:
            payload["raw_body"] = HOSTILE_SENTINELS[0]
            payload["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            payload["raw_prior_result_reentry_cycle_body"] = HOSTILE_SENTINELS[0]
            payload["raw_runtime_body"] = HOSTILE_SENTINELS[6]
            payload["raw_runtime_permission_body"] = HOSTILE_SENTINELS[8]
            payload["raw_operation_execution_body"] = HOSTILE_SENTINELS[9]
            object_payload["raw_state_body"] = HOSTILE_SENTINELS[10]
            object_payload["raw_runtime_hosting_body"] = HOSTILE_SENTINELS[11]
            object_payload["raw_runtime_loop_body"] = HOSTILE_SENTINELS[12]
            object_payload["raw_daemon_body"] = HOSTILE_SENTINELS[13]
            object_payload["raw_continuation_body"] = HOSTILE_SENTINELS[14]
            object_payload["raw_second_operation_body"] = HOSTILE_SENTINELS[15]
            object_payload["older_runtime_authority_body"] = HOSTILE_SENTINELS[16]
        if top_overrides:
            payload.update(dict(top_overrides))
        return payload

    def add_misleading_explanatory_true_fields(self, payload: dict[str, Any]) -> None:
        misleading = {
            "raw_state_body_embedded_false_posture": True,
            "state_mutation_performed_false_posture": True,
            "state_update_performed_false_posture": True,
            "second_operation_created_false_posture": True,
            "continuation_created_false_posture": True,
            "older_runtime_authority_import_refusal_preserved": True,
            "result_level_non_claims_canonical_false": True,
            "raw_state_body_not_embedded": True,
            "state_mutation_not_performed": True,
            "state_update_not_performed": True,
            "second_operation_not_created": True,
            "continuation_not_created": True,
            "follow_on_not_authorized": True,
            "priority_surface_created_false_posture": True,
            "truth_judgment_created_false_posture": True,
            "authority_created_false_posture": True,
            "currentness_created_false_posture": True,
            "source_transfer_occurred_false_posture": True,
            "consumed_request_reopened_false_posture": True,
            "authorization_token_reused_false_posture": True,
        }
        for section in (
            "local_relevance_medium_read_only_prior_result_reentry_cycle_statement",
            "local_relevance_medium_read_only_prior_result_reentry_cycle_summary",
            "local_relevance_medium_read_only_prior_result_reentry_cycle_non_meaning",
            "metadata",
            "explanatory_posture",
            "basis_commentary",
            "false_posture_preserved",
            "non_claim_preservation",
            "lineage_evidence",
        ):
            payload[section] = copy.deepcopy(misleading)
        payload["checks"] = [
            {
                "check_name": "raw state body embedded false posture preserved",
                "passed": True,
                "actual_posture": True,
                "expected_posture": True,
                "failure_code": None,
            },
            {
                "check_name": "older runtime authority import refusal preserved",
                "passed": True,
                "actual_posture": True,
                "expected_posture": True,
                "failure_code": None,
            },
        ]

    def write_synthetic_artifacts(
        self,
        root: Path,
        object_overrides: Mapping[str, Mapping[str, Any]] | None = None,
        top_overrides: Mapping[str, Mapping[str, Any]] | None = None,
        include_explanatory_true_fields: bool = False,
        include_sensitive_payload: bool = False,
    ) -> tuple[dict[str, Path], dict[str, dict[str, Any]]]:
        paths: dict[str, Path] = {}
        payloads: dict[str, dict[str, Any]] = {}
        object_overrides = object_overrides or {}
        top_overrides = top_overrides or {}
        for index, definition in enumerate(ARTIFACT_DEFINITIONS, start=1):
            path = root / self.safe_json_filename(definition["name"], index)
            payload = self.artifact_payload(
                definition,
                object_overrides=object_overrides.get(definition["name"]),
                top_overrides=top_overrides.get(definition["name"]),
                include_explanatory_true_fields=include_explanatory_true_fields,
                include_sensitive_payload=include_sensitive_payload,
            )
            self.write_json(path, payload)
            paths[definition["request_key"]] = path
            payloads[definition["request_key"]] = payload
        return paths, payloads

    def build_request(self, paths: Mapping[str, Path], **extra: Any) -> dict[str, Any]:
        request = resolver.build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_request(
            selected_prior_result_reentry_boundary_artifact=paths[
                "selected_prior_result_reentry_boundary_artifact"
            ],
            selected_runtime_held_reentry_artifact=paths[
                "selected_runtime_held_reentry_artifact"
            ],
            selected_runtime_held_reentry_boundary_artifact=paths[
                "selected_runtime_held_reentry_boundary_artifact"
            ],
            selected_runtime_held_state_artifact=paths[
                "selected_runtime_held_state_artifact"
            ],
            selected_runtime_held_state_boundary_artifact=paths[
                "selected_runtime_held_state_boundary_artifact"
            ],
            selected_runtime_artifact=paths["selected_runtime_artifact"],
            selected_runtime_boundary_artifact=paths["selected_runtime_boundary_artifact"],
            selected_runtime_permission_artifact=paths[
                "selected_runtime_permission_artifact"
            ],
            selected_operation_execution_artifact=paths[
                "selected_operation_execution_artifact"
            ],
        )
        request.update(extra)
        return request

    def synthetic_request(
        self,
        root: Path,
        object_overrides: Mapping[str, Mapping[str, Any]] | None = None,
        top_overrides: Mapping[str, Mapping[str, Any]] | None = None,
        include_explanatory_true_fields: bool = False,
        include_sensitive_payload: bool = False,
        **extra: Any,
    ) -> tuple[dict[str, Any], dict[str, Path], dict[str, dict[str, Any]]]:
        paths, payloads = self.write_synthetic_artifacts(
            root,
            object_overrides=object_overrides,
            top_overrides=top_overrides,
            include_explanatory_true_fields=include_explanatory_true_fields,
            include_sensitive_payload=include_sensitive_payload,
        )
        return self.build_request(paths, **extra), paths, payloads

    def rewrite_payload(
        self,
        paths: Mapping[str, Path],
        payloads: Mapping[str, dict[str, Any]],
        request_key: str,
    ) -> None:
        self.write_json(paths[request_key], payloads[request_key])

    def assert_recorded_result(
        self,
        result: Mapping[str, Any],
        paths: Mapping[str, Path] | None = None,
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertEqual(self.summary(result)["result_version"], "0.1.0")
        self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(self.passed_check_count(result), 0)
        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)
        cycle = self.cycle(result)
        self.assertEqual(
            cycle["cycle_id"],
            "local_relevance_medium_read_only_prior_result_reentry_cycle_001",
        )
        self.assertEqual(cycle["cycle_type"], CYCLE_TYPE)
        self.assertEqual(cycle["cycle_version"], "0.1.0")
        self.assertEqual(cycle["cycle_scope"], CYCLE_SCOPE)
        self.assertEqual(cycle["selected_command"], SELECTED_COMMAND)
        self.assert_cycle_not_wrapper(cycle)
        for definition in ARTIFACT_DEFINITIONS:
            prefix = definition["basis_prefix"]
            self.assertEqual(cycle[f"{prefix}_outcome"], definition["outcome"])
            self.assertEqual(cycle[f"{prefix}_result_version"], "0.1.0")
            self.assertEqual(cycle[f"{prefix}_failed_check_count"], 0)
            if paths is not None:
                self.assert_same_or_stable_artifact_path(
                    cycle[f"{prefix}_artifact_path"], paths[definition["request_key"]]
                )
        for key in CYCLE_TRUE_FIELDS:
            self.assertIs(cycle.get(key), True, key)
        for key in CYCLE_FALSE_FIELDS:
            self.assertIs(cycle.get(key), False, key)
        self.assert_canonical_false_non_claims(result)
        self.assert_prior_result_reentry_cycle_non_claims(result)
        self.assert_lineage_preserved(result)
        statement = self.statement(result)
        for key in (
            "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded",
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
            "prior_result_reentry_cycle_created",
            "prior_result_reentry_cycle_local_only",
            "prior_result_reentry_cycle_read_only",
            "cycle_basis_reference_only",
            "runtime_v0_failure_evidence_preserved",
            "runtime_v2_failure_evidence_preserved",
            "runtime_boundary_v0_failure_evidence_preserved",
            "prior_result_boundary_v1_failure_evidence_preserved",
            "prior_result_boundary_v2_successor_evidence_preserved",
            "consumed_request_token_remains_closed",
            "authorization_token_reuse_blocked",
            "predecessor_failure_evidence_preserved",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(statement.get(key), True, key)
        self.assertIs(statement.get("second_operation_created"), False)
        self.assertIs(statement.get("continuation_created"), False)

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2",
            "resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_from_path",
            "write_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_result",
            "build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_summary",
            "build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_request",
            "resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min",
            "resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_from_path",
            "write_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_result",
            "build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)), name)
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_CYCLE_TYPE_VALUES",
            "SUPPORTED_CYCLE_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2",
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2"
            )
        )
        self.assertIn(CYCLE_TYPE, resolver.SUPPORTED_CYCLE_TYPE_VALUES)
        self.assertIn(CYCLE_SCOPE, resolver.SUPPORTED_CYCLE_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, SELECTED_COMMAND)
        for key in (
            "second_operation_created",
            "continuation_created",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "runtime_v0_failure_repaired",
            "runtime_v2_failure_repaired",
            "runtime_boundary_v0_failure_repaired",
            "prior_result_boundary_v1_failure_repaired",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in (
            "prior_result_reentry_cycle_created",
            "prior_result_reentry_cycle_local_only",
            "prior_result_reentry_cycle_read_only",
            "cycle_basis_reference_only",
        ):
            self.assertNotIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for code in (
            "SECOND_OPERATION_CREATED",
            "CONTINUATION_CREATED",
            "RAW_STATE_BODY_EMBEDDED",
            "STATE_MUTATION_PERFORMED",
            "STATE_UPDATE_PERFORMED",
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "RUNTIME_AUTHORITY_IMPORTED",
            "RUNTIME_V0_FAILURE_REPAIRED",
            "RUNTIME_V2_FAILURE_REPAIRED",
            "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
            "PRIOR_RESULT_BOUNDARY_V1_FAILURE_REPAIRED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        self.assertEqual(set(resolver.OUTCOME_FAMILY), EXPECTED_OUTCOME_FAMILY)
        request = resolver.build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_request()
        for key, suffix in DEFAULT_ARTIFACT_SUFFIXES.items():
            self.assertTrue(str(request[key]).endswith(suffix), key)
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        for key in (
            "second_operation_created",
            "continuation_created",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "consumed_request_reopened",
            "authorization_token_reused",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "runtime_v0_failure_repaired",
            "runtime_v0_failure_hidden",
            "runtime_v0_failure_claimed_passed",
            "runtime_v2_failure_repaired",
            "runtime_v2_failure_hidden",
            "runtime_v2_failure_claimed_passed",
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
            "prior_result_boundary_v1_failure_repaired",
            "prior_result_boundary_v1_failure_hidden",
            "prior_result_boundary_v1_failure_claimed_passed",
        ):
            self.assertIs(request["declared_non_claims"][key], False)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, paths, _payloads = self.synthetic_request(Path(directory))
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                request
            )
            self.assert_recorded_result(result, paths)
            cycle = self.cycle(result)
            for key in (
                "prior_result_reentry_cycle_created",
                "prior_result_reentry_cycle_local_only",
                "prior_result_reentry_cycle_read_only",
                "cycle_basis_reference_only",
            ):
                self.assertIs(cycle[key], True)
                self.assertNotIn(key, result["non_claims"])

    def test_successful_recorded_result_from_default_live_artifacts_if_present(self) -> None:
        request = resolver.build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_request()
        missing = [
            str(path)
            for key, path in DEFAULT_ARTIFACT_PATHS.items()
            if not Path(str(request[key])).exists() and not path.exists()
        ]
        if missing:
            self.skipTest("default live artifacts not present: " + ", ".join(missing))
        result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
            request
        )
        self.assert_recorded_result(result)
        cycle = self.cycle(result)
        for definition in ARTIFACT_DEFINITIONS:
            self.assert_same_or_stable_artifact_path(
                cycle[f"{definition['basis_prefix']}_artifact_path"],
                request[definition["request_key"]],
            )
        if "prior_result_cycle_v1_failure_evidence_preserved" in self.summary(result):
            self.assertIs(
                self.summary(result)["prior_result_cycle_v1_failure_evidence_preserved"],
                True,
            )

    def test_v2_exact_extraction_ignores_explanatory_true_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _paths, _payloads = self.synthetic_request(
                Path(directory), include_explanatory_true_fields=True
            )
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                request
            )
            self.assert_recorded_result(result)
            self.assert_explanatory_true_values_did_not_become_posture(result)
            cycle = self.cycle(result)
            self.assertIs(cycle["prior_result_reentry_cycle_created"], True)
            self.assertIs(cycle["prior_result_reentry_cycle_local_only"], True)
            self.assertIs(cycle["prior_result_reentry_cycle_read_only"], True)
            self.assertIs(cycle["cycle_basis_reference_only"], True)

    def test_exact_selected_object_and_top_level_non_claim_true_still_block(self) -> None:
        expected_codes = {
            "raw_state_body_embedded": "RAW_STATE_BODY_EMBEDDED",
            "state_mutation_performed": "STATE_MUTATION_PERFORMED",
            "state_update_performed": "STATE_UPDATE_PERFORMED",
            "second_operation_created": "SECOND_OPERATION_CREATED",
            "continuation_created": "CONTINUATION_CREATED",
            "older_runtime_lineage_imported_as_authority": "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "older_runtime_permission_treated_as_current": "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "runtime_authority_imported": "RUNTIME_AUTHORITY_IMPORTED",
            "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
            "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
            "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
        }
        with tempfile.TemporaryDirectory() as directory:
            for key in EXACT_FALSE_KEYS:
                with self.subTest(selected_object_key=key):
                    request, _paths, _payloads = self.synthetic_request(
                        Path(directory),
                        object_overrides={"prior_result_reentry_boundary": {key: True}},
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIn(expected_codes[key], self.emitted_codes(result))
                    self.assert_explanatory_true_values_did_not_become_posture(result)
                with self.subTest(top_level_non_claim_key=key):
                    request, paths, payloads = self.synthetic_request(Path(directory))
                    definition = ARTIFACT_DEFINITIONS[0]
                    payload = payloads[definition["request_key"]]
                    payload[definition["object_key"]].pop(key, None)
                    payload["non_claims"][key] = True
                    self.rewrite_payload(paths, payloads, definition["request_key"])
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIn(expected_codes[key], self.emitted_codes(result))
                    self.assert_explanatory_true_values_did_not_become_posture(result)

    def test_top_level_and_declared_non_claim_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for key, expected_code in TOP_LEVEL_BLOCK_CASES:
                with self.subTest(top_level=key):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request[key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assertIs(result["non_claims"][key], False)
                with self.subTest(declared_non_claim_true=key):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][key], False)
                with self.subTest(declared_non_claim_missing=key):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request["declared_non_claims"].pop(key)
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                with self.subTest(declared_non_claim_non_bool=key):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request["declared_non_claims"][key] = "false"
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_required_non_claim_canonicalization_blocks_flipped_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            clean_request, _paths, _payloads = self.synthetic_request(Path(directory))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_explanatory_true_values_did_not_become_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        scalar_cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", lambda request: request.update({"local_relevance_medium_read_only_prior_result_reentry_cycle_intent": resolver.INTENT_BLOCK})),
            ("unsupported intent", lambda request: request.update({"local_relevance_medium_read_only_prior_result_reentry_cycle_intent": "UNSUPPORTED"})),
            ("selected command missing", lambda request: request.pop("selected_command")),
            ("selected command not state", lambda request: request.update({"selected_command": "status"})),
            ("cycle type missing", lambda request: request.pop("cycle_type")),
            ("cycle type wrong", lambda request: request.update({"cycle_type": "LOCAL_RELEVANCE_MEDIUM_SECOND_OPERATION"})),
            ("cycle scope missing", lambda request: request.pop("cycle_scope")),
            ("cycle scope wrong", lambda request: request.update({"cycle_scope": "SECOND_OPERATION"})),
            ("cycle not recorded shortcut", lambda request: request.update({"local_relevance_medium_read_only_prior_result_reentry_cycle_not_recorded": True})),
            ("cycle not created shortcut", lambda request: request.update({"prior_result_reentry_cycle_not_created": True})),
            ("cycle not local shortcut", lambda request: request.update({"prior_result_reentry_cycle_local_only_not_true": True})),
            ("cycle not read only shortcut", lambda request: request.update({"prior_result_reentry_cycle_read_only_not_true": True})),
            ("cycle basis not reference only shortcut", lambda request: request.update({"cycle_basis_reference_only_not_true": True})),
            ("required non-claim missing", lambda request: request["declared_non_claims"].pop("second_operation_created")),
            ("predecessor failure repaired", lambda request: request.update({"predecessor_failure_repaired": True})),
            ("predecessor failure hidden", lambda request: request.update({"predecessor_failure_hidden": True})),
            ("predecessor failure claimed passed", lambda request: request.update({"predecessor_failure_claimed_passed": True})),
        )
        false_request_fields = (
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
            "follow_on_work_authorized",
            "artifact_existence_treated_as_prior_result_reentry_cycle_authority",
            "latest_file_posture_treated_as_prior_result_reentry_cycle_authority",
            "repo_local_availability_treated_as_prior_result_reentry_cycle_authority",
            "hidden_repo_state_used_as_prior_result_reentry_cycle_content",
            "hidden_repo_state_used_as_prior_result_reentry_cycle_authority",
        )
        true_field_cases = (
            ("prior_result_reentry_boundary", "selected_prior_result_reentry_boundary_recorded"),
            ("prior_result_reentry_boundary", "future_prior_result_reentry_cycle_may_be_considered"),
            ("runtime_held_reentry", "selected_runtime_held_reentry_recorded"),
            ("runtime_held_reentry", "runtime_held_reentry_created"),
            ("runtime_held_reentry", "runtime_held_reentry_local_only"),
            ("runtime_held_reentry", "runtime_held_reentry_read_only"),
            ("runtime_held_reentry", "held_reentry_basis_reference_only"),
            ("runtime_held_reentry_boundary", "selected_runtime_held_reentry_boundary_recorded"),
            ("runtime_held_reentry_boundary", "future_runtime_held_reentry_may_be_considered"),
            ("runtime_held_state", "selected_runtime_held_state_recorded"),
            ("runtime_held_state", "runtime_held_state_created"),
            ("runtime_held_state", "runtime_held_state_local_only"),
            ("runtime_held_state", "runtime_held_state_read_only"),
            ("runtime_held_state", "held_state_basis_reference_only"),
            ("runtime_held_state_boundary", "selected_runtime_held_state_boundary_recorded"),
            ("runtime_held_state_boundary", "future_runtime_held_state_may_be_considered"),
            ("runtime", "selected_runtime_recorded"),
            ("runtime", "runtime_created"),
            ("runtime", "runtime_local_only"),
            ("runtime", "runtime_read_only"),
            ("runtime_boundary", "selected_runtime_boundary_recorded"),
            ("runtime_boundary", "future_runtime_may_be_considered"),
            ("runtime_permission", "selected_runtime_permission_recorded"),
            ("runtime_permission", "runtime_permission_created"),
            ("runtime_permission", "runtime_permission_local_only"),
            ("runtime_permission", "runtime_permission_read_only"),
            ("operation_execution", "selected_operation_execution_recorded"),
            ("operation_execution", "operation_execution_created"),
            ("operation_execution", "operation_execution_performed"),
            ("operation_execution", "operation_execution_local_only"),
            ("operation_execution", "operation_execution_read_only"),
        )
        with tempfile.TemporaryDirectory() as directory:
            for name, mutate in scalar_cases:
                with self.subTest(name=name):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                ["not", "a", "mapping"]  # type: ignore[arg-type]
            )
            self.assert_blocked_with_public_code(result)
            for definition in ARTIFACT_DEFINITIONS:
                with self.subTest(artifact_missing=definition["name"]):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request.pop(definition["request_key"])
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                with self.subTest(artifact_unreadable=definition["name"]):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request[definition["request_key"]] = str(
                        Path(directory) / self.safe_json_filename(definition["name"] + " missing")
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                with self.subTest(artifact_array=definition["name"]):
                    request, paths, _payloads = self.synthetic_request(Path(directory))
                    self.write_json(paths[definition["request_key"]], ["not", "object"])
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                for name, top_override in (
                    ("not recorded", {"outcome": "NOT_RECORDED"}),
                    ("failed checks", {"failed_check_count": 1}),
                    ("wrong version", {"result_version": "0.2.0"}),
                ):
                    with self.subTest(artifact=definition["name"], case=name):
                        request, paths, _payloads = self.synthetic_request(Path(directory))
                        payload = self.artifact_payload(definition, top_overrides=top_override)
                        self.write_json(paths[definition["request_key"]], payload)
                        result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                            request
                        )
                        self.assert_blocked_with_public_code(result)
            for artifact_name, field in true_field_cases:
                with self.subTest(artifact=artifact_name, field=field):
                    request, _paths, _payloads = self.synthetic_request(
                        Path(directory), object_overrides={artifact_name: {field: False}}
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
            for field in false_request_fields:
                with self.subTest(false_request_field=field):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request[field] = True
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _paths, _payloads = self.synthetic_request(Path(directory))
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                request
            )
            self.assert_recorded_result(result)
            serialized = json.dumps(result, sort_keys=True)
            for official in (
                CYCLE_TYPE,
                CYCLE_SCOPE,
                SELECTED_COMMAND,
                resolver.OUTCOME_RECORDED,
                resolver.RESOLVER_MODULE,
            ):
                self.assertIn(official, serialized)
            self.assertNotIn("[REDACTED_RAW_CONTENT]", serialized)
            self.assertEqual(set(resolver.OUTCOME_FAMILY), EXPECTED_OUTCOME_FAMILY)

    def test_raw_hidden_and_older_runtime_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _paths, _payloads = self.synthetic_request(
                Path(directory),
                include_explanatory_true_fields=True,
                include_sensitive_payload=True,
            )
            request_before = copy.deepcopy(request)
            request["raw_prior_result_reentry_cycle_body"] = HOSTILE_SENTINELS[0]
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            request["older_runtime_authority_body"] = HOSTILE_SENTINELS[-2]
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assert_blocked_with_public_code(result)
            else:
                self.assert_recorded_result(result)
            self.assert_serialized_result_excludes_sentinels(result)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn(CYCLE_TYPE, serialized)
            self.assertIn(CYCLE_SCOPE, serialized)
            self.assertIn(SELECTED_COMMAND, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assert_explanatory_true_values_did_not_become_posture(result)
            for key, value in request_before.items():
                if key not in (
                    "raw_prior_result_reentry_cycle_body",
                    "hidden_repo_state",
                    "older_runtime_authority_body",
                ):
                    self.assertEqual(request[key], value)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request, _paths, _payloads = self.synthetic_request(root)
            request_path = root / "request.json"
            self.write_json(request_path, request)
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_from_path(
                request_path
            )
            self.assert_recorded_result(result)
            self.assertEqual(self.summary(result)["result_version"], "0.1.0")
            self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_from_path(
                malformed_path
            )
            self.assert_blocked_with_public_code(malformed)
            array_path = root / "array.json"
            self.write_json(array_path, ["not", "mapping"])
            array_result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_from_path(
                array_path
            )
            self.assert_blocked_with_public_code(array_result)
            missing_result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_from_path(
                root / "missing.json"
            )
            self.assert_blocked_with_public_code(missing_result)
            output_root = (
                root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_result(
                    result
                )
                second = resolver.write_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_result(
                    result
                )
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(first.parent, output_root)
            self.assertIn(
                "local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2",
                str(first.parent),
            )
            with first.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            for forbidden_root in FORBIDDEN_OUTPUT_ROOTS:
                self.assertNotEqual(first.parent.resolve(), forbidden_root.resolve())
                self.assertNotEqual(second.parent.resolve(), forbidden_root.resolve())

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _paths, payloads = self.synthetic_request(
                Path(directory),
                include_explanatory_true_fields=True,
                include_sensitive_payload=True,
            )
            request_before = copy.deepcopy(request)
            payloads_before = copy.deepcopy(payloads)
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                request
            )
            self.assert_recorded_result(result)
            self.assertEqual(request, request_before)
            self.assertEqual(payloads, payloads_before)
            self.assertEqual(request["selected_command"], SELECTED_COMMAND)
            self.assertEqual(request["cycle_type"], CYCLE_TYPE)
            self.assertEqual(request["cycle_scope"], CYCLE_SCOPE)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                self.assertIs(request["declared_non_claims"][key], False)

    def test_failure_lineage_and_predecessor_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _paths, _payloads = self.synthetic_request(Path(directory))
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                request
            )
            self.assert_recorded_result(result)
            self.assert_lineage_preserved(result)
            summary = self.summary(result)
            self.assertIs(summary.get("older_runtime_lineage_not_imported_as_authority"), True)
            self.assertIs(summary.get("older_runtime_permission_not_treated_as_current"), True)
            self.assertIs(summary.get("runtime_authority_not_imported"), True)
            self.assertIs(summary.get("second_operation_not_created"), True)
            self.assertIs(summary.get("continuation_not_created"), True)
            for key, expected_code in TOP_LEVEL_BLOCK_CASES:
                if not key.endswith(("_repaired", "_hidden", "_claimed_passed")):
                    continue
                with self.subTest(failure_flip=key):
                    flipped, _paths, _payloads = self.synthetic_request(Path(directory))
                    flipped[key] = True
                    blocked = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
                        flipped
                    )
                    self.assert_blocked_with_public_code(blocked)
                    self.assertEqual(self.block_code(blocked), expected_code)


if __name__ == "__main__":
    unittest.main()
