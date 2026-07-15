"""Local read-only prior-result re-entry cycle resolver, v2.

This successor preserves the v1 prior-result re-entry cycle resolver as
failed-lineage evidence. The v1 live default-artifact failure was a basis
extraction mismatch: it treated explanatory true values in statements,
summaries, non-meaning sections, and checks as actual forbidden creation.

The v2 resolver reads one declared set of nine selected-state basis artifacts
and records one local, read-only, selected-prior-result-reentry-cycle-only
object. It validates false posture only by exact selected-object keys, with a
fallback to exact top-level non_claims. It does not recursively search basis
artifacts and does not import older runtime authority.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping


class LocalRelevanceMediumReadOnlyPriorResultReentryCycleV0MinV2Error(Exception):
    """Bounded resolver error for malformed path-based inputs."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2"
)
SELECTED_COMMAND = "state"

CYCLE_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE"
CYCLE_SCOPE = "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY"

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

SUPPORTED_CYCLE_TYPE_VALUES = (CYCLE_TYPE,)
SUPPORTED_CYCLE_SCOPE_VALUES = (CYCLE_SCOPE,)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2"
)

DEFAULT_PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min"
    / "local_relevance_medium_read_only_prior_result_reentry_boundary_reference_review_001__local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_result.json"
)
DEFAULT_RUNTIME_HELD_REENTRY_ARTIFACT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_v0_min"
    / "local_relevance_medium_read_only_runtime_held_reentry_reference_review_001__local_relevance_medium_read_only_runtime_held_reentry_v0_min_result.json"
)
DEFAULT_RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min"
    / "local_relevance_medium_read_only_runtime_held_reentry_boundary_reference_review_001__local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min_result.json"
)
DEFAULT_RUNTIME_HELD_STATE_ARTIFACT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_v0_min"
    / "local_relevance_medium_read_only_runtime_held_state_reference_review_001__local_relevance_medium_read_only_runtime_held_state_v0_min_result.json"
)
DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min"
    / "local_relevance_medium_read_only_runtime_held_state_boundary_reference_review_001__local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result.json"
)
DEFAULT_RUNTIME_ARTIFACT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v3"
    / "local_relevance_medium_read_only_runtime_reference_review_001__local_relevance_medium_read_only_runtime_v0_min_v3_result.json"
)
DEFAULT_RUNTIME_BOUNDARY_ARTIFACT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min_v2"
    / "local_relevance_medium_read_only_runtime_boundary_reference_review_001__local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
)
DEFAULT_RUNTIME_PERMISSION_ARTIFACT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min"
    / "local_relevance_medium_read_only_runtime_permission_reference_review_001__local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
)
DEFAULT_OPERATION_EXECUTION_ARTIFACT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min"
    / "local_relevance_medium_read_only_operation_execution_reference_review_001__local_relevance_medium_read_only_operation_execution_v0_min_result.json"
)

ARTIFACT_SPECS: tuple[dict[str, Any], ...] = (
    {
        "name": "prior_result_reentry_boundary",
        "path_key": "selected_prior_result_reentry_boundary_artifact",
        "basis_key": "selected_prior_result_reentry_boundary_artifact_basis",
        "object_key": "local_relevance_medium_read_only_prior_result_reentry_boundary",
        "cycle_prefix": "basis_prior_result_reentry_boundary",
        "check_prefix": "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_RECORDED",
        "default_path": DEFAULT_PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT,
    },
    {
        "name": "runtime_held_reentry",
        "path_key": "selected_runtime_held_reentry_artifact",
        "basis_key": "selected_runtime_held_reentry_artifact_basis",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry",
        "cycle_prefix": "basis_runtime_held_reentry",
        "check_prefix": "RUNTIME_HELD_REENTRY_ARTIFACT",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_RECORDED",
        "default_path": DEFAULT_RUNTIME_HELD_REENTRY_ARTIFACT,
    },
    {
        "name": "runtime_held_reentry_boundary",
        "path_key": "selected_runtime_held_reentry_boundary_artifact",
        "basis_key": "selected_runtime_held_reentry_boundary_artifact_basis",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry_boundary",
        "cycle_prefix": "basis_runtime_held_reentry_boundary",
        "check_prefix": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY_RECORDED",
        "default_path": DEFAULT_RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT,
    },
    {
        "name": "runtime_held_state",
        "path_key": "selected_runtime_held_state_artifact",
        "basis_key": "selected_runtime_held_state_artifact_basis",
        "object_key": "local_relevance_medium_read_only_runtime_held_state",
        "cycle_prefix": "basis_runtime_held_state",
        "check_prefix": "RUNTIME_HELD_STATE_ARTIFACT",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_RECORDED",
        "default_path": DEFAULT_RUNTIME_HELD_STATE_ARTIFACT,
    },
    {
        "name": "runtime_held_state_boundary",
        "path_key": "selected_runtime_held_state_boundary_artifact",
        "basis_key": "selected_runtime_held_state_boundary_artifact_basis",
        "object_key": "local_relevance_medium_read_only_runtime_held_state_boundary",
        "cycle_prefix": "basis_runtime_held_state_boundary",
        "check_prefix": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_RECORDED",
        "default_path": DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT,
    },
    {
        "name": "runtime",
        "path_key": "selected_runtime_artifact",
        "basis_key": "selected_runtime_artifact_basis",
        "object_key": "local_relevance_medium_read_only_runtime",
        "cycle_prefix": "basis_runtime",
        "check_prefix": "RUNTIME_ARTIFACT",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED",
        "default_path": DEFAULT_RUNTIME_ARTIFACT,
    },
    {
        "name": "runtime_boundary",
        "path_key": "selected_runtime_boundary_artifact",
        "basis_key": "selected_runtime_boundary_artifact_basis",
        "object_key": "local_relevance_medium_read_only_runtime_boundary",
        "cycle_prefix": "basis_runtime_boundary",
        "check_prefix": "RUNTIME_BOUNDARY_ARTIFACT",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED",
        "default_path": DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
    },
    {
        "name": "runtime_permission",
        "path_key": "selected_runtime_permission_artifact",
        "basis_key": "selected_runtime_permission_artifact_basis",
        "object_key": "local_relevance_medium_read_only_runtime_permission",
        "cycle_prefix": "basis_runtime_permission",
        "check_prefix": "RUNTIME_PERMISSION_ARTIFACT",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED",
        "default_path": DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
    },
    {
        "name": "operation_execution",
        "path_key": "selected_operation_execution_artifact",
        "basis_key": "selected_operation_execution_artifact_basis",
        "object_key": "local_relevance_medium_read_only_operation_execution",
        "cycle_prefix": "basis_operation_execution",
        "check_prefix": "OPERATION_EXECUTION_ARTIFACT",
        "expected_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
        "default_path": DEFAULT_OPERATION_EXECUTION_ARTIFACT,
    },
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
    "artifact_existence_treated_as_prior_result_reentry_cycle_authority",
    "latest_file_posture_treated_as_prior_result_reentry_cycle_authority",
    "repo_local_availability_treated_as_prior_result_reentry_cycle_authority",
    "hidden_repo_state_used_as_prior_result_reentry_cycle_content",
    "hidden_repo_state_used_as_prior_result_reentry_cycle_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "prior_result_cycle_v1_failure_repaired",
    "prior_result_cycle_v1_failure_hidden",
    "prior_result_cycle_v1_failure_claimed_passed",
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
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

CYCLE_OBJECT_FALSE_FIELDS = tuple(dict.fromkeys(REQUIRED_FALSE_NON_CLAIMS))

REQUEST_ONLY_FALSE_FIELDS = tuple(
    key for key in REQUIRED_FALSE_NON_CLAIMS if key not in CYCLE_OBJECT_FALSE_FIELDS
)

ALLOWED_TRUE_RECORDED_FIELDS = (
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
)

TRUE_FIELD_ALIASES = {
    "selected_prior_result_reentry_boundary_recorded": (
        "selected_prior_result_reentry_boundary_recorded",
        "prior_result_reentry_boundary_recorded",
        "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded",
    ),
    "selected_runtime_held_reentry_recorded": (
        "selected_runtime_held_reentry_recorded",
        "runtime_held_reentry_recorded",
        "local_relevance_medium_read_only_runtime_held_reentry_recorded",
    ),
    "runtime_held_reentry_created": (
        "runtime_held_reentry_created",
        "local_relevance_medium_read_only_runtime_held_reentry_created",
    ),
    "runtime_held_reentry_local_only": (
        "runtime_held_reentry_local_only",
        "local_relevance_medium_read_only_runtime_held_reentry_local_only",
    ),
    "runtime_held_reentry_read_only": (
        "runtime_held_reentry_read_only",
        "local_relevance_medium_read_only_runtime_held_reentry_read_only",
    ),
    "held_reentry_basis_reference_only": (
        "held_reentry_basis_reference_only",
        "runtime_held_reentry_basis_reference_only",
        "local_relevance_medium_read_only_runtime_held_reentry_basis_reference_only",
    ),
    "selected_runtime_held_reentry_boundary_recorded": (
        "selected_runtime_held_reentry_boundary_recorded",
        "runtime_held_reentry_boundary_recorded",
        "local_relevance_medium_read_only_runtime_held_reentry_boundary_recorded",
    ),
    "selected_runtime_held_state_recorded": (
        "selected_runtime_held_state_recorded",
        "runtime_held_state_recorded",
        "local_relevance_medium_read_only_runtime_held_state_recorded",
    ),
    "runtime_held_state_created": (
        "runtime_held_state_created",
        "local_relevance_medium_read_only_runtime_held_state_created",
    ),
    "runtime_held_state_local_only": (
        "runtime_held_state_local_only",
        "local_relevance_medium_read_only_runtime_held_state_local_only",
    ),
    "runtime_held_state_read_only": (
        "runtime_held_state_read_only",
        "local_relevance_medium_read_only_runtime_held_state_read_only",
    ),
    "held_state_basis_reference_only": (
        "held_state_basis_reference_only",
        "runtime_held_state_basis_reference_only",
        "local_relevance_medium_read_only_runtime_held_state_basis_reference_only",
    ),
    "selected_runtime_held_state_boundary_recorded": (
        "selected_runtime_held_state_boundary_recorded",
        "runtime_held_state_boundary_recorded",
        "local_relevance_medium_read_only_runtime_held_state_boundary_recorded",
    ),
    "selected_runtime_recorded": (
        "selected_runtime_recorded",
        "runtime_recorded",
        "local_relevance_medium_read_only_runtime_recorded",
    ),
    "runtime_created": (
        "runtime_created",
        "local_relevance_medium_read_only_runtime_created",
    ),
    "runtime_local_only": (
        "runtime_local_only",
        "local_relevance_medium_read_only_runtime_local_only",
    ),
    "runtime_read_only": (
        "runtime_read_only",
        "local_relevance_medium_read_only_runtime_read_only",
    ),
    "selected_runtime_boundary_recorded": (
        "selected_runtime_boundary_recorded",
        "runtime_boundary_recorded",
        "local_relevance_medium_read_only_runtime_boundary_recorded",
    ),
    "selected_runtime_permission_recorded": (
        "selected_runtime_permission_recorded",
        "runtime_permission_recorded",
        "local_relevance_medium_read_only_runtime_permission_recorded",
    ),
    "runtime_permission_created": (
        "runtime_permission_created",
        "local_relevance_medium_read_only_runtime_permission_created",
    ),
    "runtime_permission_local_only": (
        "runtime_permission_local_only",
        "local_relevance_medium_read_only_runtime_permission_local_only",
    ),
    "runtime_permission_read_only": (
        "runtime_permission_read_only",
        "local_relevance_medium_read_only_runtime_permission_read_only",
    ),
    "selected_operation_execution_recorded": (
        "selected_operation_execution_recorded",
        "operation_execution_recorded",
        "local_relevance_medium_read_only_operation_execution_recorded",
    ),
    "operation_execution_created": (
        "operation_execution_created",
        "local_relevance_medium_read_only_operation_execution_created",
    ),
    "operation_execution_performed": (
        "operation_execution_performed",
        "local_relevance_medium_read_only_operation_execution_performed",
    ),
    "operation_execution_local_only": (
        "operation_execution_local_only",
        "local_relevance_medium_read_only_operation_execution_local_only",
    ),
    "operation_execution_read_only": (
        "operation_execution_read_only",
        "local_relevance_medium_read_only_operation_execution_read_only",
    ),
}

TRUE_FIELD_BASIS = {
    "selected_prior_result_reentry_boundary_recorded": "prior_result_reentry_boundary",
    "future_prior_result_reentry_cycle_may_be_considered": "prior_result_reentry_boundary",
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

TOP_LEVEL_BLOCK_OVERRIDES = {
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "older_runtime_lineage_imported_as_authority": "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
    "older_runtime_permission_treated_as_current": "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
    "runtime_authority_imported": "RUNTIME_AUTHORITY_IMPORTED",
    "raw_state_body_embedded": "RAW_STATE_BODY_EMBEDDED",
    "state_mutation_performed": "STATE_MUTATION_PERFORMED",
    "state_update_performed": "STATE_UPDATE_PERFORMED",
    "second_operation_created": "SECOND_OPERATION_CREATED",
    "continuation_created": "CONTINUATION_CREATED",
    "runtime_v0_failure_repaired": "RUNTIME_V0_FAILURE_REPAIRED",
    "runtime_v0_failure_hidden": "RUNTIME_V0_FAILURE_HIDDEN",
    "runtime_v0_failure_claimed_passed": "RUNTIME_V0_FAILURE_CLAIMED_PASSED",
    "runtime_v2_failure_repaired": "RUNTIME_V2_FAILURE_REPAIRED",
    "runtime_v2_failure_hidden": "RUNTIME_V2_FAILURE_HIDDEN",
    "runtime_v2_failure_claimed_passed": "RUNTIME_V2_FAILURE_CLAIMED_PASSED",
    "runtime_boundary_v0_failure_repaired": "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
    "runtime_boundary_v0_failure_hidden": "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN",
    "runtime_boundary_v0_failure_claimed_passed": "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
    "prior_result_boundary_v1_failure_repaired": "PRIOR_RESULT_BOUNDARY_V1_FAILURE_REPAIRED",
    "prior_result_boundary_v1_failure_hidden": "PRIOR_RESULT_BOUNDARY_V1_FAILURE_HIDDEN",
    "prior_result_boundary_v1_failure_claimed_passed": "PRIOR_RESULT_BOUNDARY_V1_FAILURE_CLAIMED_PASSED",
    "prior_result_cycle_v1_failure_repaired": "PRIOR_RESULT_CYCLE_V1_FAILURE_REPAIRED",
    "prior_result_cycle_v1_failure_hidden": "PRIOR_RESULT_CYCLE_V1_FAILURE_HIDDEN",
    "prior_result_cycle_v1_failure_claimed_passed": "PRIOR_RESULT_CYCLE_V1_FAILURE_CLAIMED_PASSED",
}

SHORTCUT_BLOCK_FIELD_CODES = {
    "prior_result_reentry_boundary_artifact_missing": "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT_MISSING",
    "prior_result_reentry_boundary_artifact_not_recorded": "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "prior_result_reentry_boundary_artifact_failed_checks_present": "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "prior_result_reentry_boundary_artifact_version_not_0_1_0": "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_held_reentry_artifact_missing": "RUNTIME_HELD_REENTRY_ARTIFACT_MISSING",
    "runtime_held_reentry_artifact_not_recorded": "RUNTIME_HELD_REENTRY_ARTIFACT_NOT_RECORDED",
    "runtime_held_reentry_artifact_failed_checks_present": "RUNTIME_HELD_REENTRY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_held_reentry_artifact_version_not_0_1_0": "RUNTIME_HELD_REENTRY_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_held_reentry_boundary_artifact_missing": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_MISSING",
    "runtime_held_reentry_boundary_artifact_not_recorded": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "runtime_held_reentry_boundary_artifact_failed_checks_present": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_held_reentry_boundary_artifact_version_not_0_1_0": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_held_state_artifact_missing": "RUNTIME_HELD_STATE_ARTIFACT_MISSING",
    "runtime_held_state_artifact_not_recorded": "RUNTIME_HELD_STATE_ARTIFACT_NOT_RECORDED",
    "runtime_held_state_artifact_failed_checks_present": "RUNTIME_HELD_STATE_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_held_state_artifact_version_not_0_1_0": "RUNTIME_HELD_STATE_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_held_state_boundary_artifact_missing": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_MISSING",
    "runtime_held_state_boundary_artifact_not_recorded": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "runtime_held_state_boundary_artifact_failed_checks_present": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_held_state_boundary_artifact_version_not_0_1_0": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_artifact_missing": "RUNTIME_ARTIFACT_MISSING",
    "runtime_artifact_not_recorded": "RUNTIME_ARTIFACT_NOT_RECORDED",
    "runtime_artifact_failed_checks_present": "RUNTIME_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_artifact_version_not_0_1_0": "RUNTIME_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_boundary_artifact_missing": "RUNTIME_BOUNDARY_ARTIFACT_MISSING",
    "runtime_boundary_artifact_not_recorded": "RUNTIME_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "runtime_boundary_artifact_failed_checks_present": "RUNTIME_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_boundary_artifact_version_not_0_1_0": "RUNTIME_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "runtime_permission_artifact_missing": "RUNTIME_PERMISSION_ARTIFACT_MISSING",
    "runtime_permission_artifact_not_recorded": "RUNTIME_PERMISSION_ARTIFACT_NOT_RECORDED",
    "runtime_permission_artifact_failed_checks_present": "RUNTIME_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "runtime_permission_artifact_version_not_0_1_0": "RUNTIME_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0",
    "operation_execution_artifact_missing": "OPERATION_EXECUTION_ARTIFACT_MISSING",
    "operation_execution_artifact_not_recorded": "OPERATION_EXECUTION_ARTIFACT_NOT_RECORDED",
    "operation_execution_artifact_failed_checks_present": "OPERATION_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "operation_execution_artifact_version_not_0_1_0": "OPERATION_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0",
    "selected_command_missing": "SELECTED_COMMAND_MISSING",
    "selected_command_not_state": "SELECTED_COMMAND_NOT_STATE",
    "cycle_type_not_local_relevance_medium_read_only_prior_result_reentry_cycle": "CYCLE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE",
    "cycle_scope_not_selected_prior_result_reentry_cycle_only": "CYCLE_SCOPE_NOT_SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY",
}

for _field in TRUE_FIELD_BASIS:
    SHORTCUT_BLOCK_FIELD_CODES[f"{_field}_not_true"] = _field.upper() + "_NOT_TRUE"
for _field in CYCLE_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS:
    SHORTCUT_BLOCK_FIELD_CODES.setdefault(_field, _field.upper())
SHORTCUT_BLOCK_FIELD_CODES.update(TOP_LEVEL_BLOCK_OVERRIDES)
SHORTCUT_BLOCK_FIELD_CODES.update(
    {
        "local_relevance_medium_read_only_prior_result_reentry_cycle_not_recorded": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED",
        "prior_result_reentry_cycle_not_created": "PRIOR_RESULT_REENTRY_CYCLE_NOT_CREATED",
        "prior_result_reentry_cycle_local_only_not_true": "PRIOR_RESULT_REENTRY_CYCLE_LOCAL_ONLY_NOT_TRUE",
        "prior_result_reentry_cycle_read_only_not_true": "PRIOR_RESULT_REENTRY_CYCLE_READ_ONLY_NOT_TRUE",
        "cycle_basis_reference_only_not_true": "CYCLE_BASIS_REFERENCE_ONLY_NOT_TRUE",
        "future_prior_result_reentry_cycle_may_not_be_considered": "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED",
        "future_runtime_held_reentry_may_not_be_considered": "FUTURE_RUNTIME_HELD_REENTRY_MAY_NOT_BE_CONSIDERED",
        "future_runtime_held_state_may_not_be_considered": "FUTURE_RUNTIME_HELD_STATE_MAY_NOT_BE_CONSIDERED",
        "future_runtime_may_not_be_considered": "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED",
        "selected_prior_result_reentry_boundary_not_recorded": "SELECTED_PRIOR_RESULT_REENTRY_BOUNDARY_NOT_RECORDED",
        "selected_runtime_held_reentry_not_recorded": "SELECTED_RUNTIME_HELD_REENTRY_NOT_RECORDED",
        "runtime_held_reentry_not_created": "RUNTIME_HELD_REENTRY_NOT_CREATED",
        "runtime_held_reentry_local_only_not_true": "RUNTIME_HELD_REENTRY_LOCAL_ONLY_NOT_TRUE",
        "runtime_held_reentry_read_only_not_true": "RUNTIME_HELD_REENTRY_READ_ONLY_NOT_TRUE",
        "held_reentry_basis_reference_only_not_true": "HELD_REENTRY_BASIS_REFERENCE_ONLY_NOT_TRUE",
        "selected_runtime_held_reentry_boundary_not_recorded": "SELECTED_RUNTIME_HELD_REENTRY_BOUNDARY_NOT_RECORDED",
        "selected_runtime_held_state_not_recorded": "SELECTED_RUNTIME_HELD_STATE_NOT_RECORDED",
        "runtime_held_state_not_created": "RUNTIME_HELD_STATE_NOT_CREATED",
        "runtime_held_state_local_only_not_true": "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE",
        "runtime_held_state_read_only_not_true": "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE",
        "held_state_basis_reference_only_not_true": "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE",
        "selected_runtime_held_state_boundary_not_recorded": "SELECTED_RUNTIME_HELD_STATE_BOUNDARY_NOT_RECORDED",
        "selected_runtime_not_recorded": "SELECTED_RUNTIME_NOT_RECORDED",
        "runtime_not_created": "RUNTIME_NOT_CREATED",
        "runtime_local_only_not_true": "RUNTIME_LOCAL_ONLY_NOT_TRUE",
        "runtime_read_only_not_true": "RUNTIME_READ_ONLY_NOT_TRUE",
        "selected_runtime_boundary_not_recorded": "SELECTED_RUNTIME_BOUNDARY_NOT_RECORDED",
        "selected_runtime_permission_not_recorded": "SELECTED_RUNTIME_PERMISSION_NOT_RECORDED",
        "runtime_permission_not_created": "RUNTIME_PERMISSION_NOT_CREATED",
        "runtime_permission_local_only_not_true": "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE",
        "runtime_permission_read_only_not_true": "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE",
        "selected_operation_execution_not_recorded": "SELECTED_OPERATION_EXECUTION_NOT_RECORDED",
        "operation_execution_not_created": "OPERATION_EXECUTION_NOT_CREATED",
        "operation_execution_not_performed": "OPERATION_EXECUTION_NOT_PERFORMED",
        "operation_execution_local_only_not_true": "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE",
        "operation_execution_read_only_not_true": "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE",
    }
)

BLOCK_CODES = tuple(
    dict.fromkeys(
        tuple(SHORTCUT_BLOCK_FIELD_CODES.values())
        + tuple(TOP_LEVEL_BLOCK_OVERRIDES.values())
        + tuple(
            f"{spec['check_prefix']}_{suffix}"
            for spec in ARTIFACT_SPECS
            for suffix in (
                "PATH_MISSING",
                "UNREADABLE",
                "JSON_NOT_OBJECT",
                "NOT_RECORDED",
                "VERSION_NOT_0_1_0",
                "FAILED_CHECKS_PRESENT",
            )
        )
        + (
            "REQUEST_MISSING",
            "REQUEST_NOT_MAPPING",
            "QUESTION_MISSING",
            "INTENT_UNSUPPORTED",
            "EXPLICIT_BLOCK_REQUESTED",
            "EXPLICIT_NOT_RECORDED_REQUESTED",
            "CYCLE_TYPE_MISSING",
            "CYCLE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE",
            "CYCLE_SCOPE_MISSING",
            "CYCLE_SCOPE_NOT_SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY",
            "SELECTED_COMMAND_MISSING",
            "SELECTED_COMMAND_NOT_STATE",
            "NON_CLAIMS_NOT_MAPPING",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED",
            "PRIOR_RESULT_REENTRY_CYCLE_V1_LIVE_BASIS_EXTRACTION_MISMATCH_PRESERVED",
            "ARTIFACT_JSON_NOT_OBJECT",
            "ARTIFACT_PATH_MISSING",
            "ARTIFACT_UNREADABLE",
            "ARTIFACT_OUTCOME_NOT_RECORDED",
            "ARTIFACT_RESULT_VERSION_NOT_0_1_0",
            "ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
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

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
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
    "raw_continuation_body",
    "raw_second_operation_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "prior_result_reentry_cycle_body",
    "prior_result_reentry_boundary_body",
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

OFFICIAL_STRINGS = frozenset(
    {
        CYCLE_TYPE,
        CYCLE_SCOPE,
        SELECTED_COMMAND,
        RESULT_VERSION,
        RESOLVER_MODULE,
        OUTCOME_RECORDED,
        OUTCOME_NOT_RECORDED,
        OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        OUTCOME_BLOCKED,
    }
    | set(BLOCK_CODES)
    | set(OUTCOME_FAMILY)
    | set(REQUIRED_FALSE_NON_CLAIMS)
    | set(ALLOWED_TRUE_RECORDED_FIELDS)
)


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_sensitive_key(key: str) -> bool:
    normalized = str(key)
    return normalized in SENSITIVE_CONTENT_KEYS or normalized.endswith("_body")


def _sanitize(value: Any, parent_key: str | None = None) -> Any:
    if _is_sensitive_key(parent_key or ""):
        return "[REDACTED_RAW_CONTENT]"
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        sanitized = value
        for sentinel in HOSTILE_SENTINELS:
            sanitized = sanitized.replace(sentinel, "[REDACTED_RAW_CONTENT]")
        return sanitized
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, int | float):
        return value
    if isinstance(value, list):
        return [_sanitize(item, parent_key=parent_key) for item in value]
    if _is_mapping(value):
        return {str(key): _sanitize(item, parent_key=str(key)) for key, item in value.items()}
    return str(value)


def _safe_path_string(value: Any) -> str:
    return _sanitize(str(Path(value))) if value is not None else ""


def _failed_check_count(artifact: Mapping[str, Any]) -> int | None:
    for key in ("failed_check_count", "failure_count"):
        value = artifact.get(key)
        if isinstance(value, bool):
            continue
        if isinstance(value, int):
            return value
    summary = artifact.get("local_relevance_medium_read_only_prior_result_reentry_cycle_summary")
    if _is_mapping(summary):
        value = summary.get("failed_check_count")
        if isinstance(value, int) and not isinstance(value, bool):
            return value
    for value in artifact.values():
        if _is_mapping(value) and "failed_check_count" in value:
            count = value.get("failed_check_count")
            if isinstance(count, int) and not isinstance(count, bool):
                return count
    checks = artifact.get("local_relevance_medium_read_only_prior_result_reentry_cycle_checks")
    if isinstance(checks, list):
        return sum(1 for check in checks if _is_mapping(check) and check.get("passed") is False)
    return None


def _artifact_result_version(artifact: Mapping[str, Any]) -> str | None:
    value = artifact.get("result_version")
    if isinstance(value, str):
        return value
    for key in (
        "local_relevance_medium_read_only_prior_result_reentry_cycle_summary",
        "local_relevance_medium_read_only_prior_result_reentry_cycle_metadata",
    ):
        section = artifact.get(key)
        if _is_mapping(section) and isinstance(section.get("result_version"), str):
            return section["result_version"]
    for value in artifact.values():
        if _is_mapping(value) and isinstance(value.get("result_version"), str):
            return value["result_version"]
    return None


def _selected_object(artifact: Mapping[str, Any], object_key: str) -> Mapping[str, Any]:
    selected = artifact.get(object_key)
    return selected if _is_mapping(selected) else {}


def _exact_selected_value(
    artifact: Mapping[str, Any],
    object_key: str,
    field: str,
    aliases: Iterable[str] | None = None,
) -> tuple[bool, Any]:
    selected = _selected_object(artifact, object_key)
    for key in aliases or (field,):
        if key in selected:
            return True, selected[key]
    return False, None


def _basis_clean(basis: Mapping[str, Any]) -> bool:
    return (
        basis.get("outcome_matches") is True
        and basis.get("result_version_matches") is True
        and basis.get("failed_check_count_matches") is True
    )


def _artifact_true_posture(
    artifact: Mapping[str, Any],
    object_key: str,
    basis: Mapping[str, Any],
    field: str,
) -> bool:
    aliases = TRUE_FIELD_ALIASES.get(field, (field,))
    present, value = _exact_selected_value(artifact, object_key, field, aliases)
    if present:
        return value is True
    return _basis_clean(basis)


def _artifact_false_posture(
    artifact: Mapping[str, Any],
    object_key: str,
    field: str,
) -> bool:
    present, value = _exact_selected_value(artifact, object_key, field)
    if present:
        return value is False
    non_claims = artifact.get("non_claims")
    if _is_mapping(non_claims) and field in non_claims:
        return non_claims[field] is False
    return True


def _read_json_file(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except Exception as exc:
        raise LocalRelevanceMediumReadOnlyPriorResultReentryCycleV0MinV2Error(str(exc)) from exc


def _read_basis_artifact(
    request: Mapping[str, Any],
    spec: Mapping[str, Any],
) -> tuple[dict[str, Any], Mapping[str, Any] | None]:
    raw_path = request.get(spec["path_key"])
    if raw_path in (None, ""):
        return (
            {
                "artifact_path": "",
                "path_declared": False,
                "readable": False,
                "json_object": False,
                "selected_object_key": spec["object_key"],
                "selected_object_present": False,
                "outcome": None,
                "expected_outcome": spec["expected_outcome"],
                "outcome_matches": False,
                "result_version": None,
                "result_version_matches": False,
                "failed_check_count": None,
                "failed_check_count_matches": False,
            },
            None,
        )
    path = Path(str(raw_path))
    basis: dict[str, Any] = {
        "artifact_path": _safe_path_string(path),
        "path_declared": True,
        "readable": False,
        "json_object": False,
        "selected_object_key": spec["object_key"],
        "selected_object_present": False,
        "outcome": None,
        "expected_outcome": spec["expected_outcome"],
        "outcome_matches": False,
        "result_version": None,
        "result_version_matches": False,
        "failed_check_count": None,
        "failed_check_count_matches": False,
    }
    try:
        artifact = _read_json_file(path)
    except LocalRelevanceMediumReadOnlyPriorResultReentryCycleV0MinV2Error as exc:
        basis["read_error"] = _sanitize(str(exc))
        return basis, None
    basis["readable"] = True
    if not _is_mapping(artifact):
        return basis, None
    basis["json_object"] = True
    basis["selected_object_present"] = _is_mapping(artifact.get(spec["object_key"]))
    outcome = artifact.get("outcome")
    result_version = _artifact_result_version(artifact)
    failed_count = _failed_check_count(artifact)
    basis["outcome"] = _sanitize(outcome)
    basis["outcome_matches"] = outcome == spec["expected_outcome"]
    basis["result_version"] = result_version
    basis["result_version_matches"] = result_version == RESULT_VERSION
    basis["failed_check_count"] = failed_count
    basis["failed_check_count_matches"] = failed_count == 0
    return basis, artifact


def _check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str,
) -> None:
    record: dict[str, Any] = {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected),
        "actual_posture": _sanitize(actual),
    }
    if passed:
        record["failure_code"] = None
    else:
        record["block_code"] = code
        record["failure_code"] = code
    checks.append(record)


def _first_failed_code(checks: Iterable[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code:
                return code
    return None


def _validate_declared_non_claims(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    declared = request.get("declared_non_claims")
    if not _is_mapping(declared):
        _check(
            checks,
            "declared non-claims mapping",
            False,
            "mapping with required false values",
            type(declared).__name__,
            "NON_CLAIMS_NOT_MAPPING",
        )
        return
    for key in REQUIRED_FALSE_NON_CLAIMS:
        _check(
            checks,
            f"declared non-claim {key} false",
            key in declared and declared.get(key) is False,
            False,
            declared.get(key, "[missing]"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _validate_request_shape(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    question = request.get(
        "local_relevance_medium_read_only_prior_result_reentry_cycle_question"
    )
    _check(
        checks,
        "prior-result re-entry cycle question declared",
        isinstance(question, str) and bool(question.strip()),
        "non-empty question",
        question,
        "QUESTION_MISSING",
    )
    intent = request.get("local_relevance_medium_read_only_prior_result_reentry_cycle_intent")
    _check(
        checks,
        "prior-result re-entry cycle intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "selected command declared",
        "selected_command" in request,
        SELECTED_COMMAND,
        request.get("selected_command", "[missing]"),
        "SELECTED_COMMAND_MISSING",
    )
    _check(
        checks,
        "selected command exactly state",
        request.get("selected_command") == SELECTED_COMMAND,
        SELECTED_COMMAND,
        request.get("selected_command"),
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "cycle type declared",
        "cycle_type" in request,
        CYCLE_TYPE,
        request.get("cycle_type", "[missing]"),
        "CYCLE_TYPE_MISSING",
    )
    _check(
        checks,
        "cycle type exact",
        request.get("cycle_type") == CYCLE_TYPE,
        CYCLE_TYPE,
        request.get("cycle_type"),
        "CYCLE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE",
    )
    _check(
        checks,
        "cycle scope declared",
        "cycle_scope" in request,
        CYCLE_SCOPE,
        request.get("cycle_scope", "[missing]"),
        "CYCLE_SCOPE_MISSING",
    )
    _check(
        checks,
        "cycle scope exact",
        request.get("cycle_scope") == CYCLE_SCOPE,
        CYCLE_SCOPE,
        request.get("cycle_scope"),
        "CYCLE_SCOPE_NOT_SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY",
    )
    for key, code in TOP_LEVEL_BLOCK_OVERRIDES.items():
        _check(
            checks,
            f"request {key} false",
            request.get(key) is not True,
            False,
            request.get(key, False),
            code,
        )
    for key, code in SHORTCUT_BLOCK_FIELD_CODES.items():
        if key in TOP_LEVEL_BLOCK_OVERRIDES:
            continue
        if request.get(key) is True:
            _check(checks, f"shortcut {key} not requested", False, False, True, code)
    _validate_declared_non_claims(request, checks)


def _validate_basis(
    checks: list[dict[str, Any]],
    basis_by_name: Mapping[str, Mapping[str, Any]],
    artifacts_by_name: Mapping[str, Mapping[str, Any] | None],
) -> None:
    spec_by_name = {str(spec["name"]): spec for spec in ARTIFACT_SPECS}
    for name, spec in spec_by_name.items():
        basis = basis_by_name[name]
        prefix = str(spec["check_prefix"])
        _check(
            checks,
            f"{name} artifact path declared",
            basis.get("path_declared") is True,
            "declared path",
            basis.get("artifact_path"),
            f"{prefix}_PATH_MISSING",
        )
        _check(
            checks,
            f"{name} artifact readable",
            basis.get("readable") is True,
            "readable JSON file",
            basis.get("readable"),
            f"{prefix}_UNREADABLE",
        )
        _check(
            checks,
            f"{name} artifact JSON object",
            basis.get("json_object") is True,
            "JSON object",
            basis.get("json_object"),
            f"{prefix}_JSON_NOT_OBJECT",
        )
        _check(
            checks,
            f"{name} artifact outcome recorded",
            basis.get("outcome_matches") is True,
            spec["expected_outcome"],
            basis.get("outcome"),
            f"{prefix}_NOT_RECORDED",
        )
        _check(
            checks,
            f"{name} artifact result version 0.1.0",
            basis.get("result_version_matches") is True,
            RESULT_VERSION,
            basis.get("result_version"),
            f"{prefix}_VERSION_NOT_0_1_0",
        )
        _check(
            checks,
            f"{name} artifact failed check count zero",
            basis.get("failed_check_count_matches") is True,
            0,
            basis.get("failed_check_count"),
            f"{prefix}_FAILED_CHECKS_PRESENT",
        )

    for field, basis_name in TRUE_FIELD_BASIS.items():
        artifact = artifacts_by_name.get(basis_name)
        spec = spec_by_name[basis_name]
        basis = basis_by_name[basis_name]
        passed = (
            _is_mapping(artifact)
            and _artifact_true_posture(artifact, spec["object_key"], basis, field)
        )
        _check(
            checks,
            f"{field} true",
            passed,
            True,
            passed,
            SHORTCUT_BLOCK_FIELD_CODES.get(f"{field}_not_true", field.upper() + "_NOT_TRUE"),
        )

    for field in CYCLE_OBJECT_FALSE_FIELDS:
        passed = True
        actuals: dict[str, bool] = {}
        for basis_name, spec in spec_by_name.items():
            artifact = artifacts_by_name.get(basis_name)
            if not _is_mapping(artifact):
                continue
            basis_passed = _artifact_false_posture(artifact, spec["object_key"], field)
            actuals[basis_name] = basis_passed
            if not basis_passed:
                passed = False
        _check(
            checks,
            f"basis exact false posture {field}",
            passed,
            "selected-object exact false or top-level non_claim false",
            actuals,
            SHORTCUT_BLOCK_FIELD_CODES.get(field, field.upper()),
        )


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    cycle_id = str(
        request.get(
            "local_relevance_medium_read_only_prior_result_reentry_cycle_id",
            "local_relevance_medium_read_only_prior_result_reentry_cycle_001",
        )
    )
    return {
        "local_relevance_medium_read_only_prior_result_reentry_cycle_id": _sanitize(
            cycle_id
        ),
        "local_relevance_medium_read_only_prior_result_reentry_cycle_type": CYCLE_TYPE,
        "local_relevance_medium_read_only_prior_result_reentry_cycle_version": RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
        "prior_result_cycle_v1_failure_evidence_preserved": True,
        "prior_result_cycle_v1_failure_repaired": False,
        "prior_result_cycle_v1_failure_hidden": False,
        "prior_result_cycle_v1_failure_claimed_passed": False,
        "v2_live_basis_extraction_mismatch_correction_applied": True,
    }


def _build_cycle_object(
    request: Mapping[str, Any],
    basis_by_name: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    cycle: dict[str, Any] = {
        "cycle_id": _sanitize(
            request.get(
                "local_relevance_medium_read_only_prior_result_reentry_cycle_id",
                "local_relevance_medium_read_only_prior_result_reentry_cycle_001",
            )
        ),
        "cycle_type": CYCLE_TYPE,
        "cycle_version": RESULT_VERSION,
        "cycle_scope": CYCLE_SCOPE,
    }
    for spec in ARTIFACT_SPECS:
        basis = basis_by_name[str(spec["name"])]
        prefix = str(spec["cycle_prefix"])
        cycle[f"{prefix}_artifact_path"] = basis.get("artifact_path")
        cycle[f"{prefix}_outcome"] = basis.get("outcome")
        cycle[f"{prefix}_result_version"] = basis.get("result_version")
        cycle[f"{prefix}_failed_check_count"] = basis.get("failed_check_count")

    cycle.update(
        {
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "selected_prior_result_reentry_boundary_recorded": True,
            "future_prior_result_reentry_cycle_may_be_considered": True,
            "selected_runtime_held_reentry_recorded": True,
            "runtime_held_reentry_created": True,
            "runtime_held_reentry_local_only": True,
            "runtime_held_reentry_read_only": True,
            "held_reentry_basis_reference_only": True,
            "selected_runtime_held_reentry_boundary_recorded": True,
            "future_runtime_held_reentry_may_be_considered": True,
            "selected_runtime_held_state_recorded": True,
            "runtime_held_state_created": True,
            "runtime_held_state_local_only": True,
            "runtime_held_state_read_only": True,
            "held_state_basis_reference_only": True,
            "selected_runtime_held_state_boundary_recorded": True,
            "future_runtime_held_state_may_be_considered": True,
            "selected_runtime_recorded": True,
            "runtime_created": True,
            "runtime_local_only": True,
            "runtime_read_only": True,
            "selected_runtime_boundary_recorded": True,
            "future_runtime_may_be_considered": True,
            "selected_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded": True,
            "prior_result_reentry_cycle_created": True,
            "prior_result_reentry_cycle_local_only": True,
            "prior_result_reentry_cycle_read_only": True,
            "cycle_basis_reference_only": True,
            "runtime_v0_failure_evidence_preserved": True,
            "runtime_v2_failure_evidence_preserved": True,
            "runtime_boundary_v0_failure_evidence_preserved": True,
            "prior_result_boundary_v1_failure_evidence_preserved": True,
            "prior_result_boundary_v2_successor_evidence_preserved": True,
        }
    )
    for field in CYCLE_OBJECT_FALSE_FIELDS:
        cycle[field] = False
    return cycle


def _empty_cycle_object(request: Mapping[str, Any] | None) -> dict[str, Any]:
    request = request or {}
    return {
        "cycle_id": _sanitize(
            request.get(
                "local_relevance_medium_read_only_prior_result_reentry_cycle_id",
                "local_relevance_medium_read_only_prior_result_reentry_cycle_001",
            )
        ),
        "cycle_type": CYCLE_TYPE,
        "cycle_version": RESULT_VERSION,
        "cycle_scope": CYCLE_SCOPE,
        "selected_command": SELECTED_COMMAND,
        "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded": False,
        "prior_result_reentry_cycle_created": False,
        "prior_result_reentry_cycle_local_only": False,
        "prior_result_reentry_cycle_read_only": False,
        "cycle_basis_reference_only": False,
        **{field: False for field in CYCLE_OBJECT_FALSE_FIELDS},
        "runtime_v0_failure_evidence_preserved": True,
        "runtime_v2_failure_evidence_preserved": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
        "prior_result_boundary_v1_failure_evidence_preserved": True,
        "prior_result_boundary_v2_successor_evidence_preserved": True,
    }


def _build_statement(recorded: bool) -> dict[str, Any]:
    statement: dict[str, Any] = {
        "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded": recorded,
        "basis_prior_result_reentry_boundary_artifact_preserved": recorded,
        "basis_runtime_held_reentry_artifact_preserved": recorded,
        "basis_runtime_held_reentry_boundary_artifact_preserved": recorded,
        "basis_runtime_held_state_artifact_preserved": recorded,
        "basis_runtime_held_state_boundary_artifact_preserved": recorded,
        "basis_runtime_artifact_preserved": recorded,
        "basis_runtime_boundary_artifact_preserved": recorded,
        "basis_runtime_permission_artifact_preserved": recorded,
        "basis_operation_execution_artifact_preserved": recorded,
        "selected_command_preserved": recorded,
        "selected_command_is_state": recorded,
        "selected_prior_result_reentry_boundary_recorded": recorded,
        "future_prior_result_reentry_cycle_may_be_considered": recorded,
        "selected_runtime_held_reentry_recorded": recorded,
        "runtime_held_reentry_created": recorded,
        "runtime_held_reentry_local_only": recorded,
        "runtime_held_reentry_read_only": recorded,
        "held_reentry_basis_reference_only": recorded,
        "selected_runtime_held_reentry_boundary_recorded": recorded,
        "future_runtime_held_reentry_may_be_considered": recorded,
        "selected_runtime_held_state_recorded": recorded,
        "runtime_held_state_created": recorded,
        "runtime_held_state_local_only": recorded,
        "runtime_held_state_read_only": recorded,
        "held_state_basis_reference_only": recorded,
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
        "prior_result_reentry_cycle_created": recorded,
        "prior_result_reentry_cycle_local_only": recorded,
        "prior_result_reentry_cycle_read_only": recorded,
        "cycle_basis_reference_only": recorded,
        "second_operation_created": False,
        "continuation_created": False,
        "runtime_v0_failure_evidence_preserved": True,
        "runtime_v2_failure_evidence_preserved": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
        "prior_result_boundary_v1_failure_evidence_preserved": True,
        "prior_result_boundary_v2_successor_evidence_preserved": True,
        "prior_result_cycle_v1_failure_evidence_preserved": True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }
    return statement


def _non_meaning() -> dict[str, bool]:
    return {
        "not_second_operation": True,
        "not_continuation": True,
        "not_runtime_hosting": True,
        "not_runtime_loop": True,
        "not_daemon": True,
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
        "not_scoring": True,
        "not_priority": True,
        "not_validity_judgment": True,
        "not_truth_judgment": True,
        "not_authority": True,
        "not_currentness": True,
        "not_feed": True,
        "not_follow_on_work": True,
        "not_terminal_summary": True,
        "v1_live_basis_extraction_mismatch_not_repaired_or_claimed_passed": True,
    }


def _build_summary_values(result: Mapping[str, Any]) -> dict[str, Any]:
    checks = result.get("local_relevance_medium_read_only_prior_result_reentry_cycle_checks")
    check_list = checks if isinstance(checks, list) else []
    passed_count = sum(1 for check in check_list if _is_mapping(check) and check.get("passed") is True)
    failed_count = sum(1 for check in check_list if _is_mapping(check) and check.get("passed") is False)
    cycle = result.get("local_relevance_medium_read_only_prior_result_reentry_cycle")
    cycle_map = cycle if _is_mapping(cycle) else {}
    statement = result.get("local_relevance_medium_read_only_prior_result_reentry_cycle_statement")
    statement_map = statement if _is_mapping(statement) else {}
    block = result.get("block")
    block_map = block if _is_mapping(block) else {}
    return {
        "outcome": result.get("outcome"),
        "block_code": block_map.get("code") or block_map.get("block_code"),
        "block_reason": block_map.get("reason"),
        "cycle_id": cycle_map.get("cycle_id"),
        "question": result.get("declared_local_relevance_medium_read_only_prior_result_reentry_cycle_question"),
        "intent": result.get("declared_local_relevance_medium_read_only_prior_result_reentry_cycle_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "cycle_recorded": cycle_map.get(
            "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded", False
        )
        is True,
        "basis_prior_result_reentry_boundary_artifact_preserved": statement_map.get(
            "basis_prior_result_reentry_boundary_artifact_preserved", False
        ),
        "basis_runtime_held_reentry_artifact_preserved": statement_map.get(
            "basis_runtime_held_reentry_artifact_preserved", False
        ),
        "basis_runtime_held_reentry_boundary_artifact_preserved": statement_map.get(
            "basis_runtime_held_reentry_boundary_artifact_preserved", False
        ),
        "basis_runtime_held_state_artifact_preserved": statement_map.get(
            "basis_runtime_held_state_artifact_preserved", False
        ),
        "basis_runtime_held_state_boundary_artifact_preserved": statement_map.get(
            "basis_runtime_held_state_boundary_artifact_preserved", False
        ),
        "basis_runtime_artifact_preserved": statement_map.get("basis_runtime_artifact_preserved", False),
        "basis_runtime_boundary_artifact_preserved": statement_map.get(
            "basis_runtime_boundary_artifact_preserved", False
        ),
        "basis_runtime_permission_artifact_preserved": statement_map.get(
            "basis_runtime_permission_artifact_preserved", False
        ),
        "basis_operation_execution_artifact_preserved": statement_map.get(
            "basis_operation_execution_artifact_preserved", False
        ),
        "selected_command": cycle_map.get("selected_command", SELECTED_COMMAND),
        "selected_command_preserved": statement_map.get("selected_command_preserved", False),
        "selected_command_is_state": cycle_map.get("selected_command_is_state", False),
        "selected_prior_result_reentry_boundary_recorded": cycle_map.get(
            "selected_prior_result_reentry_boundary_recorded", False
        ),
        "future_prior_result_reentry_cycle_may_be_considered": cycle_map.get(
            "future_prior_result_reentry_cycle_may_be_considered", False
        ),
        "selected_runtime_held_reentry_recorded": cycle_map.get(
            "selected_runtime_held_reentry_recorded", False
        ),
        "runtime_held_reentry_created": cycle_map.get("runtime_held_reentry_created", False),
        "runtime_held_reentry_local_only": cycle_map.get("runtime_held_reentry_local_only", False),
        "runtime_held_reentry_read_only": cycle_map.get("runtime_held_reentry_read_only", False),
        "held_reentry_basis_reference_only": cycle_map.get("held_reentry_basis_reference_only", False),
        "selected_runtime_held_reentry_boundary_recorded": cycle_map.get(
            "selected_runtime_held_reentry_boundary_recorded", False
        ),
        "selected_runtime_held_state_recorded": cycle_map.get(
            "selected_runtime_held_state_recorded", False
        ),
        "runtime_held_state_created": cycle_map.get("runtime_held_state_created", False),
        "runtime_held_state_local_only": cycle_map.get("runtime_held_state_local_only", False),
        "runtime_held_state_read_only": cycle_map.get("runtime_held_state_read_only", False),
        "held_state_basis_reference_only": cycle_map.get("held_state_basis_reference_only", False),
        "raw_state_body_embedded": cycle_map.get("raw_state_body_embedded", False),
        "state_mutation_performed": cycle_map.get("state_mutation_performed", False),
        "state_update_performed": cycle_map.get("state_update_performed", False),
        "selected_runtime_recorded": cycle_map.get("selected_runtime_recorded", False),
        "selected_runtime_boundary_recorded": cycle_map.get("selected_runtime_boundary_recorded", False),
        "selected_runtime_permission_recorded": cycle_map.get("selected_runtime_permission_recorded", False),
        "selected_operation_execution_recorded": cycle_map.get("selected_operation_execution_recorded", False),
        "prior_result_reentry_cycle_created": cycle_map.get("prior_result_reentry_cycle_created", False),
        "prior_result_reentry_cycle_local_only": cycle_map.get(
            "prior_result_reentry_cycle_local_only", False
        ),
        "prior_result_reentry_cycle_read_only": cycle_map.get(
            "prior_result_reentry_cycle_read_only", False
        ),
        "cycle_basis_reference_only": cycle_map.get("cycle_basis_reference_only", False),
        "cycle_object_summary": {
            "cycle_type": cycle_map.get("cycle_type"),
            "cycle_scope": cycle_map.get("cycle_scope"),
            "cycle_version": cycle_map.get("cycle_version"),
        },
        "second_operation_not_created": cycle_map.get("second_operation_created") is False,
        "continuation_not_created": cycle_map.get("continuation_created") is False,
        "runtime_hosting_not_created": cycle_map.get("runtime_hosting_created") is False,
        "runtime_loop_not_created": cycle_map.get("runtime_loop_created") is False,
        "daemon_behavior_not_created": cycle_map.get("daemon_behavior_created") is False,
        "public_api_not_created": cycle_map.get("public_api_created") is False,
        "participant_facing_interface_not_created": cycle_map.get(
            "participant_facing_interface_created"
        )
        is False,
        "distributed_network_behavior_not_created": cycle_map.get(
            "distributed_network_behavior_created"
        )
        is False,
        "older_runtime_lineage_not_imported_as_authority": cycle_map.get(
            "older_runtime_lineage_imported_as_authority"
        )
        is False,
        "older_runtime_permission_not_treated_as_current": cycle_map.get(
            "older_runtime_permission_treated_as_current"
        )
        is False,
        "runtime_authority_not_imported": cycle_map.get("runtime_authority_imported") is False,
        "runtime_v0_failure_evidence_preserved": cycle_map.get(
            "runtime_v0_failure_evidence_preserved", False
        ),
        "runtime_v2_failure_evidence_preserved": cycle_map.get(
            "runtime_v2_failure_evidence_preserved", False
        ),
        "runtime_boundary_v0_failure_evidence_preserved": cycle_map.get(
            "runtime_boundary_v0_failure_evidence_preserved", False
        ),
        "prior_result_boundary_v1_failure_evidence_preserved": cycle_map.get(
            "prior_result_boundary_v1_failure_evidence_preserved", False
        ),
        "prior_result_boundary_v2_successor_evidence_preserved": cycle_map.get(
            "prior_result_boundary_v2_successor_evidence_preserved", False
        ),
        "prior_result_cycle_v1_failure_evidence_preserved": statement_map.get(
            "prior_result_cycle_v1_failure_evidence_preserved", False
        ),
        "failure_not_repaired_hidden_or_claimed_passed": all(
            result.get("non_claims", {}).get(key) is False
            for key in (
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
                "prior_result_boundary_v1_failure_repaired",
                "prior_result_boundary_v1_failure_hidden",
                "prior_result_boundary_v1_failure_claimed_passed",
                "prior_result_cycle_v1_failure_repaired",
                "prior_result_cycle_v1_failure_hidden",
                "prior_result_cycle_v1_failure_claimed_passed",
            )
        ),
        "consumed_request_token_remains_closed": statement_map.get(
            "consumed_request_token_remains_closed", False
        ),
        "authorization_token_reuse_blocked": statement_map.get(
            "authorization_token_reuse_blocked", False
        ),
        "predecessor_failure_evidence_preserved": statement_map.get(
            "predecessor_failure_evidence_preserved", False
        ),
        "result_level_non_claims_canonical_false": statement_map.get(
            "result_level_non_claims_canonical_false", False
        ),
    }


def build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a deterministic summary from a resolver result artifact."""

    return _sanitize(_build_summary_values(result))


def _result_artifact(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    basis_by_name: Mapping[str, Mapping[str, Any]],
    recorded: bool,
    outcome: str,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    cycle = _build_cycle_object(request, basis_by_name) if recorded else _empty_cycle_object(request)
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": block_code,
        "block_code": block_code,
        "reason": _sanitize(block_reason) if block_reason is not None else None,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_prior_result_reentry_cycle_metadata": _metadata(request),
        "declared_local_relevance_medium_read_only_prior_result_reentry_cycle_question": _sanitize(
            request.get("local_relevance_medium_read_only_prior_result_reentry_cycle_question")
        ),
        "declared_local_relevance_medium_read_only_prior_result_reentry_cycle_intent": _sanitize(
            request.get("local_relevance_medium_read_only_prior_result_reentry_cycle_intent")
        ),
        "local_relevance_medium_read_only_prior_result_reentry_cycle": cycle,
        "local_relevance_medium_read_only_prior_result_reentry_cycle_checks": _sanitize(checks),
        "local_relevance_medium_read_only_prior_result_reentry_cycle_statement": _build_statement(
            recorded
        ),
        "local_relevance_medium_read_only_prior_result_reentry_cycle_non_meaning": _non_meaning(),
        "additional_basis_required": [],
        "not_recorded_basis": [] if recorded else [_sanitize(block_reason or "not recorded")],
        "what_remains_open": [
            "terminal summary, if separately admitted",
            "future local read-only cycle consideration, if separately admitted",
        ],
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    for spec in ARTIFACT_SPECS:
        result[str(spec["basis_key"])] = _sanitize(dict(basis_by_name.get(str(spec["name"]), {})))
    result["local_relevance_medium_read_only_prior_result_reentry_cycle_summary"] = (
        build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_summary(result)
    )
    return _sanitize(result)


def resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(
    declared_local_relevance_medium_read_only_prior_result_reentry_cycle: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve whether one selected-state prior-result re-entry cycle may be recorded."""

    if declared_local_relevance_medium_read_only_prior_result_reentry_cycle is None:
        request = build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_request()
    elif not _is_mapping(declared_local_relevance_medium_read_only_prior_result_reentry_cycle):
        checks: list[dict[str, Any]] = []
        _check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_local_relevance_medium_read_only_prior_result_reentry_cycle).__name__,
            "REQUEST_NOT_MAPPING",
        )
        empty_basis = {str(spec["name"]): {} for spec in ARTIFACT_SPECS}
        return _result_artifact(
            {},
            checks,
            empty_basis,
            False,
            OUTCOME_BLOCKED,
            "REQUEST_NOT_MAPPING",
            "Declared request is not a mapping.",
        )
    else:
        request = copy.deepcopy(dict(declared_local_relevance_medium_read_only_prior_result_reentry_cycle))

    checks: list[dict[str, Any]] = []
    _validate_request_shape(request, checks)

    basis_by_name: dict[str, Mapping[str, Any]] = {}
    artifacts_by_name: dict[str, Mapping[str, Any] | None] = {}
    for spec in ARTIFACT_SPECS:
        basis, artifact = _read_basis_artifact(request, spec)
        basis_by_name[str(spec["name"])] = basis
        artifacts_by_name[str(spec["name"])] = artifact

    _validate_basis(checks, basis_by_name, artifacts_by_name)

    intent = request.get("local_relevance_medium_read_only_prior_result_reentry_cycle_intent")
    if intent == INTENT_BLOCK:
        _check(
            checks,
            "explicit block intent absent",
            False,
            "record intent",
            intent,
            "EXPLICIT_BLOCK_REQUESTED",
        )
    elif intent == INTENT_DO_NOT_RECORD:
        _check(
            checks,
            "explicit not-recorded intent absent",
            False,
            "record intent",
            intent,
            "EXPLICIT_NOT_RECORDED_REQUESTED",
        )

    failed_code = _first_failed_code(checks)
    if failed_code is not None:
        return _result_artifact(
            request,
            checks,
            basis_by_name,
            False,
            OUTCOME_BLOCKED,
            failed_code,
            "Prior-result re-entry cycle blocked by declared request or selected basis.",
        )

    _check(
        checks,
        "local relevance medium read-only prior-result re-entry cycle recorded",
        True,
        True,
        True,
        "PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED",
    )
    _check(checks, "prior-result re-entry cycle created", True, True, True, "PRIOR_RESULT_REENTRY_CYCLE_NOT_CREATED")
    _check(
        checks,
        "prior-result re-entry cycle local only",
        True,
        True,
        True,
        "PRIOR_RESULT_REENTRY_CYCLE_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "prior-result re-entry cycle read only",
        True,
        True,
        True,
        "PRIOR_RESULT_REENTRY_CYCLE_READ_ONLY_NOT_TRUE",
    )
    _check(checks, "cycle basis reference only", True, True, True, "CYCLE_BASIS_REFERENCE_ONLY_NOT_TRUE")
    _check(
        checks,
        "result-level required false non-claims canonical false",
        True,
        "all required non-claims false",
        "all required non-claims false",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    return _result_artifact(
        request,
        checks,
        basis_by_name,
        True,
        OUTCOME_RECORDED,
        None,
        None,
    )


def resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_from_path(
    declared_local_relevance_medium_read_only_prior_result_reentry_cycle_path: Path | str,
) -> dict[str, Any]:
    """Resolve a declared request loaded from a JSON file path."""

    path = Path(declared_local_relevance_medium_read_only_prior_result_reentry_cycle_path)
    try:
        request = _read_json_file(path)
    except LocalRelevanceMediumReadOnlyPriorResultReentryCycleV0MinV2Error as exc:
        checks: list[dict[str, Any]] = []
        _check(
            checks,
            "request path readable",
            False,
            "readable JSON mapping",
            str(exc),
            "ARTIFACT_UNREADABLE",
        )
        return _result_artifact(
            {},
            checks,
            {str(spec["name"]): {} for spec in ARTIFACT_SPECS},
            False,
            OUTCOME_BLOCKED,
            "ARTIFACT_UNREADABLE",
            "Declared request path was unreadable.",
        )
    if not _is_mapping(request):
        checks = []
        _check(
            checks,
            "request JSON object",
            False,
            "JSON object",
            type(request).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _result_artifact(
            {},
            checks,
            {str(spec["name"]): {} for spec in ARTIFACT_SPECS},
            False,
            OUTCOME_BLOCKED,
            "REQUEST_NOT_MAPPING",
            "Declared request JSON was not an object.",
        )
    return resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2(request)


def _unique_output_path(path: Path) -> Path:
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


def write_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a result artifact without silently overwriting an existing file."""

    if output_path is None:
        cycle = result.get("local_relevance_medium_read_only_prior_result_reentry_cycle")
        cycle_id = "local_relevance_medium_read_only_prior_result_reentry_cycle_001"
        if _is_mapping(cycle) and cycle.get("cycle_id"):
            cycle_id = str(cycle["cycle_id"])
        output_path = (
            OUTPUT_ROOT
            / f"{cycle_id}__local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_result.json"
        )
    path = _unique_output_path(Path(output_path))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, ensure_ascii=True, indent=2, sort_keys=True)
        handle.write("\n")
    return path


def build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_request(
    *,
    local_relevance_medium_read_only_prior_result_reentry_cycle_id: str = "local_relevance_medium_read_only_prior_result_reentry_cycle_001",
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
    cycle_type: str = CYCLE_TYPE,
    cycle_scope: str = CYCLE_SCOPE,
    intent: str = INTENT_RECORD,
) -> dict[str, Any]:
    """Build a declared request for one local read-only prior-result re-entry cycle."""

    return {
        "local_relevance_medium_read_only_prior_result_reentry_cycle_id": local_relevance_medium_read_only_prior_result_reentry_cycle_id,
        "local_relevance_medium_read_only_prior_result_reentry_cycle_question": (
            "May one local relevance medium read-only prior-result re-entry cycle be "
            "recorded for selected command state from bounded selected-state bases?"
        ),
        "local_relevance_medium_read_only_prior_result_reentry_cycle_intent": intent,
        "selected_prior_result_reentry_boundary_artifact": str(
            selected_prior_result_reentry_boundary_artifact
        ),
        "selected_runtime_held_reentry_artifact": str(selected_runtime_held_reentry_artifact),
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
        "cycle_type": cycle_type,
        "cycle_scope": cycle_scope,
        "declared_non_claims": _canonical_non_claims(),
    }


resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min = (
    resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2
)
resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_from_path = (
    resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_from_path
)
write_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_result = (
    write_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_result
)
build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_summary = (
    build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_summary
)
build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_request = (
    build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_request
)
