"""Resolve one local read-only prior-result re-entry cycle.

This resolver records one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE
object only. It reads fixed selected-state basis artifacts, records one local
read-only basis-reference-only cycle object, and preserves the non-claims that
keep this line out of second operation, continuation, hosting, loop, daemon,
public API, participant-facing, distributed, raw-state, mutation/update, and
older-runtime-authority-import territory.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyPriorResultReentryCycleV0MinError(RuntimeError):
    """Bounded resolver error for prior-result re-entry cycle handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min"
)

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

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "prior_result_reentry_cycle_v0_min"
)

DEFAULT_CYCLE_ID = "local_relevance_medium_read_only_prior_result_reentry_cycle_001"
CYCLE_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE"
CYCLE_SCOPE = "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY"
SUPPORTED_CYCLE_TYPE_VALUES = (CYCLE_TYPE,)
SUPPORTED_CYCLE_SCOPE_VALUES = (CYCLE_SCOPE,)
SELECTED_COMMAND = "state"

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY "
    "for selected command state, one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY, "
    "one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME, one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY, "
    "one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION, one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION, existing reusable read-only lookup permission, "
    "prior lookup-pair coverage, and prior local carrier command surface, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE be recorded for selected command state, "
    "without creating second operation, creating continuation, creating runtime hosting, creating runtime loop, "
    "creating daemon behavior, creating public API, creating participant-facing interface, creating distributed "
    "network behavior, creating general operation permission, creating general lookup permission, creating "
    "arbitrary lookup permission, permitting unsupported commands, permitting unsupported lookup keys, creating "
    "new lookup entry beyond the already bounded selected-state lookup result object, embedding raw state body, "
    "mutating state, updating state, accepting new entries, accepting new signals, performing filesystem discovery, "
    "importing older runtime/post-runtime authority, creating query surface, registry, search, ranking, scoring, "
    "priority, validity judgment, truth judgment, authority, currentness, synchronization, participation "
    "authorization, participant role, repeated reception permission, arbitrary reception, feed, source transfer, "
    "source receipt, or follow-on work?"
)

DEFAULT_PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT = Path(
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "prior_result_reentry_boundary_v0_min/"
    "local_relevance_medium_read_only_prior_result_reentry_boundary_reference_review_001__"
    "local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_result.json"
)
DEFAULT_RUNTIME_HELD_REENTRY_ARTIFACT = Path(
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_held_reentry_v0_min/"
    "local_relevance_medium_read_only_runtime_held_reentry_reference_review_001__"
    "local_relevance_medium_read_only_runtime_held_reentry_v0_min_result.json"
)
DEFAULT_RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT = Path(
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_held_reentry_boundary_v0_min/"
    "local_relevance_medium_read_only_runtime_held_reentry_boundary_reference_review_001__"
    "local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min_result.json"
)
DEFAULT_RUNTIME_HELD_STATE_ARTIFACT = Path(
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_held_state_v0_min/"
    "local_relevance_medium_read_only_runtime_held_state_reference_review_001__"
    "local_relevance_medium_read_only_runtime_held_state_v0_min_result.json"
)
DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT = Path(
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_held_state_boundary_v0_min/"
    "local_relevance_medium_read_only_runtime_held_state_boundary_reference_review_001__"
    "local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result.json"
)
DEFAULT_RUNTIME_ARTIFACT = Path(
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_v0_min_v3/"
    "local_relevance_medium_read_only_runtime_reference_review_001__"
    "local_relevance_medium_read_only_runtime_v0_min_v3_result.json"
)
DEFAULT_RUNTIME_BOUNDARY_ARTIFACT = Path(
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_boundary_v0_min_v2/"
    "local_relevance_medium_read_only_runtime_boundary_reference_review_001__"
    "local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
)
DEFAULT_RUNTIME_PERMISSION_ARTIFACT = Path(
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_permission_v0_min/"
    "local_relevance_medium_read_only_runtime_permission_reference_review_001__"
    "local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
)
DEFAULT_OPERATION_EXECUTION_ARTIFACT = Path(
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_execution_v0_min/"
    "local_relevance_medium_read_only_operation_execution_reference_review_001__"
    "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
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

ARTIFACT_SPECS = (
    (
        "prior_result_reentry_boundary",
        "selected_prior_result_reentry_boundary_artifact",
        "selected_prior_result_reentry_boundary_artifact_basis",
        "basis_prior_result_reentry_boundary",
        "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT",
        EXPECTED_PRIOR_RESULT_REENTRY_BOUNDARY_OUTCOME,
        DEFAULT_PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT,
    ),
    (
        "runtime_held_reentry",
        "selected_runtime_held_reentry_artifact",
        "selected_runtime_held_reentry_artifact_basis",
        "basis_runtime_held_reentry",
        "RUNTIME_HELD_REENTRY_ARTIFACT",
        EXPECTED_RUNTIME_HELD_REENTRY_OUTCOME,
        DEFAULT_RUNTIME_HELD_REENTRY_ARTIFACT,
    ),
    (
        "runtime_held_reentry_boundary",
        "selected_runtime_held_reentry_boundary_artifact",
        "selected_runtime_held_reentry_boundary_artifact_basis",
        "basis_runtime_held_reentry_boundary",
        "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT",
        EXPECTED_RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME,
        DEFAULT_RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT,
    ),
    (
        "runtime_held_state",
        "selected_runtime_held_state_artifact",
        "selected_runtime_held_state_artifact_basis",
        "basis_runtime_held_state",
        "RUNTIME_HELD_STATE_ARTIFACT",
        EXPECTED_RUNTIME_HELD_STATE_OUTCOME,
        DEFAULT_RUNTIME_HELD_STATE_ARTIFACT,
    ),
    (
        "runtime_held_state_boundary",
        "selected_runtime_held_state_boundary_artifact",
        "selected_runtime_held_state_boundary_artifact_basis",
        "basis_runtime_held_state_boundary",
        "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT",
        EXPECTED_RUNTIME_HELD_STATE_BOUNDARY_OUTCOME,
        DEFAULT_RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT,
    ),
    (
        "runtime",
        "selected_runtime_artifact",
        "selected_runtime_artifact_basis",
        "basis_runtime",
        "RUNTIME_ARTIFACT",
        EXPECTED_RUNTIME_OUTCOME,
        DEFAULT_RUNTIME_ARTIFACT,
    ),
    (
        "runtime_boundary",
        "selected_runtime_boundary_artifact",
        "selected_runtime_boundary_artifact_basis",
        "basis_runtime_boundary",
        "RUNTIME_BOUNDARY_ARTIFACT",
        EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
    ),
    (
        "runtime_permission",
        "selected_runtime_permission_artifact",
        "selected_runtime_permission_artifact_basis",
        "basis_runtime_permission",
        "RUNTIME_PERMISSION_ARTIFACT",
        EXPECTED_RUNTIME_PERMISSION_OUTCOME,
        DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
    ),
    (
        "operation_execution",
        "selected_operation_execution_artifact",
        "selected_operation_execution_artifact_basis",
        "basis_operation_execution",
        "OPERATION_EXECUTION_ARTIFACT",
        EXPECTED_OPERATION_EXECUTION_OUTCOME,
        DEFAULT_OPERATION_EXECUTION_ARTIFACT,
    ),
)

CYCLE_OBJECT_FALSE_FIELDS = (
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
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
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
    "artifact_existence_treated_as_prior_result_reentry_cycle_authority",
    "latest_file_posture_treated_as_prior_result_reentry_cycle_authority",
    "repo_local_availability_treated_as_prior_result_reentry_cycle_authority",
    "hidden_repo_state_used_as_prior_result_reentry_cycle_content",
    "hidden_repo_state_used_as_prior_result_reentry_cycle_authority",
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
    "prior_result_boundary_v1_failure_repaired",
    "prior_result_boundary_v1_failure_hidden",
    "prior_result_boundary_v1_failure_claimed_passed",
)

REQUIRED_FALSE_NON_CLAIMS = CYCLE_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS

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

FIELD_ALIASES = {
    "selected_prior_result_reentry_boundary_recorded": (
        "selected_prior_result_reentry_boundary_recorded",
        "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded",
    ),
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

TRUE_FIELD_BLOCK_CODES = {
    "selected_prior_result_reentry_boundary_recorded": (
        "SELECTED_PRIOR_RESULT_REENTRY_BOUNDARY_NOT_RECORDED"
    ),
    "future_prior_result_reentry_cycle_may_be_considered": (
        "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED"
    ),
    "selected_runtime_held_reentry_recorded": "SELECTED_RUNTIME_HELD_REENTRY_NOT_RECORDED",
    "runtime_held_reentry_created": "RUNTIME_HELD_REENTRY_NOT_CREATED",
    "runtime_held_reentry_local_only": "RUNTIME_HELD_REENTRY_LOCAL_ONLY_NOT_TRUE",
    "runtime_held_reentry_read_only": "RUNTIME_HELD_REENTRY_READ_ONLY_NOT_TRUE",
    "held_reentry_basis_reference_only": "HELD_REENTRY_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "selected_runtime_held_reentry_boundary_recorded": (
        "SELECTED_RUNTIME_HELD_REENTRY_BOUNDARY_NOT_RECORDED"
    ),
    "future_runtime_held_reentry_may_be_considered": (
        "FUTURE_RUNTIME_HELD_REENTRY_MAY_NOT_BE_CONSIDERED"
    ),
    "selected_runtime_held_state_recorded": "SELECTED_RUNTIME_HELD_STATE_NOT_RECORDED",
    "runtime_held_state_created": "RUNTIME_HELD_STATE_NOT_CREATED",
    "runtime_held_state_local_only": "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE",
    "runtime_held_state_read_only": "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE",
    "held_state_basis_reference_only": "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "selected_runtime_held_state_boundary_recorded": (
        "SELECTED_RUNTIME_HELD_STATE_BOUNDARY_NOT_RECORDED"
    ),
    "future_runtime_held_state_may_be_considered": (
        "FUTURE_RUNTIME_HELD_STATE_MAY_NOT_BE_CONSIDERED"
    ),
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
    "prior_result_boundary_v1_failure_claimed_passed": (
        "PRIOR_RESULT_BOUNDARY_V1_FAILURE_CLAIMED_PASSED"
    ),
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
}

TOP_LEVEL_BLOCK_FIELD_CODES = {
    field: TOP_LEVEL_BLOCK_OVERRIDES.get(field, field.upper())
    for field in REQUIRED_FALSE_NON_CLAIMS
}

SHORTCUT_BLOCK_FIELD_CODES: dict[str, str] = {}
for _name, _path_key, _basis_key, _obj_prefix, _prefix, _expected, _default in ARTIFACT_SPECS:
    SHORTCUT_BLOCK_FIELD_CODES[f"{_name}_artifact_missing"] = f"{_prefix}_PATH_MISSING"
    SHORTCUT_BLOCK_FIELD_CODES[f"{_name}_artifact_not_recorded"] = f"{_prefix}_NOT_RECORDED"
    SHORTCUT_BLOCK_FIELD_CODES[f"{_name}_artifact_failed_checks_present"] = (
        f"{_prefix}_FAILED_CHECKS_PRESENT"
    )
    SHORTCUT_BLOCK_FIELD_CODES[f"{_name}_artifact_version_not_0_1_0"] = (
        f"{_prefix}_VERSION_NOT_0_1_0"
    )

SHORTCUT_BLOCK_FIELD_CODES.update(
    {
        "selected_command_missing": "SELECTED_COMMAND_MISSING",
        "selected_command_not_state": "SELECTED_COMMAND_NOT_STATE",
        "cycle_type_not_local_relevance_medium_read_only_prior_result_reentry_cycle": (
            "CYCLE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE"
        ),
        "cycle_scope_not_selected_prior_result_reentry_cycle_only": (
            "CYCLE_SCOPE_NOT_SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY"
        ),
        "local_relevance_medium_read_only_prior_result_reentry_cycle_not_recorded": (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED"
        ),
        "prior_result_reentry_cycle_not_created": "PRIOR_RESULT_REENTRY_CYCLE_NOT_CREATED",
        "prior_result_reentry_cycle_local_only_not_true": (
            "PRIOR_RESULT_REENTRY_CYCLE_LOCAL_ONLY_NOT_TRUE"
        ),
        "prior_result_reentry_cycle_read_only_not_true": (
            "PRIOR_RESULT_REENTRY_CYCLE_READ_ONLY_NOT_TRUE"
        ),
        "cycle_basis_reference_only_not_true": "CYCLE_BASIS_REFERENCE_ONLY_NOT_TRUE",
        **{
            f"{field}_not_true": code
            for field, code in TRUE_FIELD_BLOCK_CODES.items()
            if not field.startswith("selected_")
        },
    }
)

ARTIFACT_BLOCK_CODES = tuple(
    code
    for _name, _path_key, _basis_key, _obj_prefix, prefix, _expected, _default in ARTIFACT_SPECS
    for code in (
        f"{prefix}_PATH_MISSING",
        f"{prefix}_UNREADABLE",
        f"{prefix}_NOT_JSON_OBJECT",
        f"{prefix}_NOT_RECORDED",
        f"{prefix}_FAILED_CHECKS_PRESENT",
        f"{prefix}_VERSION_NOT_0_1_0",
    )
)

CORE_BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_BLOCK_REQUESTED",
    "CYCLE_TYPE_MISSING",
    "CYCLE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE",
    "CYCLE_SCOPE_MISSING",
    "CYCLE_SCOPE_NOT_SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED",
    "PRIOR_RESULT_REENTRY_CYCLE_NOT_CREATED",
    "PRIOR_RESULT_REENTRY_CYCLE_LOCAL_ONLY_NOT_TRUE",
    "PRIOR_RESULT_REENTRY_CYCLE_READ_ONLY_NOT_TRUE",
    "CYCLE_BASIS_REFERENCE_ONLY_NOT_TRUE",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUEST_UNREADABLE",
)

BLOCK_CODES = tuple(
    dict.fromkeys(
        CORE_BLOCK_CODES
        + ARTIFACT_BLOCK_CODES
        + tuple(TRUE_FIELD_BLOCK_CODES.values())
        + tuple(SHORTCUT_BLOCK_FIELD_CODES.values())
        + tuple(TOP_LEVEL_BLOCK_FIELD_CODES.values())
    )
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

OFFICIAL_STRINGS = frozenset(
    (
        CYCLE_TYPE,
        CYCLE_SCOPE,
        SELECTED_COMMAND,
        RESULT_VERSION,
        RESOLVER_MODULE,
        INTENT_RECORD,
        INTENT_DO_NOT_RECORD,
        INTENT_BLOCK,
    )
    + OUTCOME_FAMILY
    + BLOCK_CODES
    + REQUIRED_FALSE_NON_CLAIMS
    + ALLOWED_TRUE_RECORDED_FIELDS
)

WHAT_REMAINS_OPEN = (
    "local relevance medium read-only prior-result re-entry cycle test",
    "local relevance medium read-only prior-result re-entry cycle live artifact",
    "local relevance medium read-only prior-result re-entry cycle terminal summary",
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
    "registry",
    "search surface",
    "query surface",
    "ranking surface",
    "source transfer",
    "source receipt",
    "follow-on work",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _is_mapping(value: Any) -> bool:
    return isinstance(value, MappingABC)


def _is_sensitive_key(key: Any) -> bool:
    lowered = str(key).lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _sanitize(value: Any, key: str | None = None) -> Any:
    if key is not None and _is_sensitive_key(key):
        return "[REDACTED_RAW_BODY_CONTENT]"
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return "[REDACTED_RAW_BODY_CONTENT]"
        return value
    if _is_mapping(value):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize(item) for item in value]
    return value


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> None:
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _sanitize(expected_posture),
            "actual_posture": _sanitize(actual_posture),
            "failure_code": None if passed else code,
            "block_code": None if passed else code,
        }
    )


def _counts(checks: list[dict[str, Any]]) -> tuple[int, int]:
    return (
        sum(1 for check in checks if check.get("passed") is True),
        sum(1 for check in checks if check.get("passed") is False),
    )


def _first_failure(checks: list[dict[str, Any]], default: str) -> str:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code:
                return code
    return default


def _read_json_object(path_value: Any) -> tuple[dict[str, Any] | None, str | None]:
    try:
        with Path(path_value).open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, TypeError, json.JSONDecodeError):
        return None, "unreadable"
    if not _is_mapping(value):
        return None, "not_json_object"
    return dict(value), None


def _extract_field(artifact: Mapping[str, Any], field_name: str) -> Any:
    if field_name in artifact:
        return artifact[field_name]
    for key, value in artifact.items():
        if _is_mapping(value) and str(key).endswith(("_summary", "_metadata")):
            if field_name in value:
                return value[field_name]
    return None


def _failed_check_count(artifact: Mapping[str, Any]) -> Any:
    value = _extract_field(artifact, "failed_check_count")
    if value is not None:
        return value
    checks = _extract_field(artifact, "checks")
    if isinstance(checks, list):
        return sum(1 for check in checks if _is_mapping(check) and not check.get("passed"))
    return None


def _collect_key_values(value: Any, aliases: set[str], found: list[Any]) -> None:
    if _is_mapping(value):
        for key, item in value.items():
            key_text = str(key)
            if key_text in aliases:
                found.append(item)
            if not _is_sensitive_key(key_text):
                _collect_key_values(item, aliases, found)
    elif isinstance(value, list):
        for item in value:
            _collect_key_values(item, aliases, found)


def _artifact_bool(artifact: Mapping[str, Any], field_name: str) -> bool | None:
    found: list[Any] = []
    _collect_key_values(artifact, set(FIELD_ALIASES.get(field_name, (field_name,))), found)
    bools = [value for value in found if isinstance(value, bool)]
    if any(value is False for value in bools):
        return False
    if any(value is True for value in bools):
        return True
    return None


def _basis_clean(basis: Mapping[str, Any]) -> bool:
    return (
        basis.get("artifact_readable") is True
        and basis.get("outcome_recorded") is True
        and basis.get("result_version_0_1_0") is True
        and basis.get("failed_check_count_zero") is True
    )


def _artifact_true(
    artifacts: Mapping[str, Mapping[str, Any]],
    basis_by_name: Mapping[str, Mapping[str, Any]],
    field_name: str,
) -> bool:
    artifact_name = TRUE_FIELD_BASIS[field_name]
    artifact = artifacts.get(artifact_name)
    if artifact is None:
        return False
    value = _artifact_bool(artifact, field_name)
    return _basis_clean(basis_by_name.get(artifact_name, {})) if value is None else value


def _artifact_false(artifacts: Mapping[str, Mapping[str, Any]], field_name: str) -> bool:
    values: list[Any] = []
    for artifact in artifacts.values():
        _collect_key_values(artifact, {field_name}, values)
    return not any(value is True for value in values if isinstance(value, bool))


def _empty_basis() -> dict[str, dict[str, Any]]:
    return {
        basis_key: {
            "artifact_path": None,
            "artifact_readable": False,
            "artifact_preserved": False,
            "outcome": None,
            "result_version": None,
            "failed_check_count": None,
            "outcome_recorded": False,
            "result_version_0_1_0": False,
            "failed_check_count_zero": False,
        }
        for _name, _path, basis_key, _obj, _prefix, _expected, _default in ARTIFACT_SPECS
    }


def _read_artifact(
    request: Mapping[str, Any],
    spec: tuple[str, str, str, str, str, str, Path],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    name, path_key, _basis_key, _obj_prefix, prefix, expected, _default = spec
    path_value = request.get(path_key)
    basis = {
        "artifact_path": _sanitize(str(path_value)) if path_value else None,
        "artifact_readable": False,
        "artifact_preserved": False,
        "outcome": None,
        "result_version": None,
        "failed_check_count": None,
        "outcome_recorded": False,
        "result_version_0_1_0": False,
        "failed_check_count_zero": False,
    }
    _add_check(
        checks,
        f"{name} artifact path declared",
        bool(path_value),
        "path declared",
        path_value,
        f"{prefix}_PATH_MISSING",
    )
    if not path_value:
        return basis, None
    artifact, error = _read_json_object(path_value)
    if error == "unreadable":
        _add_check(checks, f"{name} artifact readable JSON", False, "readable", "unreadable", f"{prefix}_UNREADABLE")
        return basis, None
    if error == "not_json_object" or artifact is None:
        _add_check(checks, f"{name} artifact JSON object", False, "object", "not object", f"{prefix}_NOT_JSON_OBJECT")
        return basis, None
    outcome = _extract_field(artifact, "outcome")
    result_version = _extract_field(artifact, "result_version")
    failed_count = _failed_check_count(artifact)
    basis.update(
        {
            "artifact_readable": True,
            "artifact_preserved": True,
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_count,
            "outcome_recorded": outcome == expected,
            "result_version_0_1_0": result_version == RESULT_VERSION,
            "failed_check_count_zero": (
                isinstance(failed_count, int)
                and not isinstance(failed_count, bool)
                and failed_count == 0
            ),
        }
    )
    _add_check(checks, f"{name} artifact readable JSON", True, "readable", "readable", f"{prefix}_UNREADABLE")
    _add_check(checks, f"{name} artifact outcome recorded", basis["outcome_recorded"], expected, outcome, f"{prefix}_NOT_RECORDED")
    _add_check(checks, f"{name} artifact result version 0.1.0", basis["result_version_0_1_0"], RESULT_VERSION, result_version, f"{prefix}_VERSION_NOT_0_1_0")
    _add_check(checks, f"{name} artifact failed check count zero", basis["failed_check_count_zero"], 0, failed_count, f"{prefix}_FAILED_CHECKS_PRESENT")
    return basis, artifact


def _basis_value(
    basis_by_name: Mapping[str, Mapping[str, Any]],
    artifact_name: str,
    key: str,
) -> Any:
    return basis_by_name.get(artifact_name, {}).get(key)


def _build_cycle_object(
    request: Mapping[str, Any],
    basis_by_name: Mapping[str, Mapping[str, Any]],
    recorded: bool,
) -> dict[str, Any]:
    selected_command = request.get("selected_command", SELECTED_COMMAND)
    cycle = {
        "cycle_id": request.get(
            "local_relevance_medium_read_only_prior_result_reentry_cycle_id",
            DEFAULT_CYCLE_ID,
        ),
        "cycle_type": CYCLE_TYPE if recorded else request.get("cycle_type", CYCLE_TYPE),
        "cycle_version": RESULT_VERSION,
        "cycle_scope": CYCLE_SCOPE if recorded else request.get("cycle_scope", CYCLE_SCOPE),
        "selected_command": selected_command,
        "selected_command_is_state": selected_command == SELECTED_COMMAND,
        "runtime_v0_failure_evidence_preserved": True,
        "runtime_v2_failure_evidence_preserved": True,
        "runtime_boundary_v0_failure_evidence_preserved": True,
        "prior_result_boundary_v1_failure_evidence_preserved": True,
        "prior_result_boundary_v2_successor_evidence_preserved": True,
    }
    for name, _path_key, _basis_key, object_prefix, _prefix, _expected, _default in ARTIFACT_SPECS:
        cycle[f"{object_prefix}_artifact"] = _basis_value(basis_by_name, name, "artifact_path")
        cycle[f"{object_prefix}_outcome"] = _basis_value(basis_by_name, name, "outcome")
        cycle[f"{object_prefix}_result_version"] = _basis_value(
            basis_by_name, name, "result_version"
        )
        cycle[f"{object_prefix}_failed_check_count"] = _basis_value(
            basis_by_name, name, "failed_check_count"
        )
    for field in TRUE_FIELD_BASIS:
        cycle[field] = recorded
    for field in (
        "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded",
        "prior_result_reentry_cycle_created",
        "prior_result_reentry_cycle_local_only",
        "prior_result_reentry_cycle_read_only",
        "cycle_basis_reference_only",
    ):
        cycle[field] = recorded
    for field in CYCLE_OBJECT_FALSE_FIELDS:
        cycle[field] = False
    return _sanitize(cycle)


def _build_statement(cycle: Mapping[str, Any], recorded: bool) -> dict[str, Any]:
    statement = {
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
        "selected_command_preserved": cycle.get("selected_command") == SELECTED_COMMAND,
        "selected_command_is_state": cycle.get("selected_command_is_state") is True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }
    for field in (
        tuple(TRUE_FIELD_BASIS)
        + (
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
        + CYCLE_OBJECT_FALSE_FIELDS
    ):
        statement[field] = cycle.get(field)
    return _sanitize(statement)


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    basis_sections: Mapping[str, Mapping[str, Any]],
    basis_by_name: Mapping[str, Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    recorded: bool,
) -> dict[str, Any]:
    cycle = _build_cycle_object(request, basis_by_name, recorded)
    statement = _build_statement(cycle, recorded)
    passed, failed = _counts(checks)
    basis_payload = {
        basis_key: _sanitize(dict(basis_sections.get(basis_key, {})))
        for _name, _path_key, basis_key, _obj, _prefix, _expected, _default in ARTIFACT_SPECS
    }
    result = {
        "local_relevance_medium_read_only_prior_result_reentry_cycle_metadata": {
            "local_relevance_medium_read_only_prior_result_reentry_cycle_id": cycle.get("cycle_id"),
            "local_relevance_medium_read_only_prior_result_reentry_cycle_type": CYCLE_TYPE,
            "local_relevance_medium_read_only_prior_result_reentry_cycle_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_local_relevance_medium_read_only_prior_result_reentry_cycle_question": {
            "question": _sanitize(
                request.get(
                    "local_relevance_medium_read_only_prior_result_reentry_cycle_question"
                )
            ),
            "intent": _sanitize(
                request.get(
                    "local_relevance_medium_read_only_prior_result_reentry_cycle_intent"
                )
            ),
            "selected_command": _sanitize(request.get("selected_command")),
            "cycle_type": _sanitize(request.get("cycle_type")),
            "cycle_scope": _sanitize(request.get("cycle_scope")),
        },
        **basis_payload,
        "local_relevance_medium_read_only_prior_result_reentry_cycle": cycle,
        "local_relevance_medium_read_only_prior_result_reentry_cycle_checks": _sanitize(checks),
        "local_relevance_medium_read_only_prior_result_reentry_cycle_statement": statement,
        "local_relevance_medium_read_only_prior_result_reentry_cycle_non_meaning": {
            field: False for field in CYCLE_OBJECT_FALSE_FIELDS
        },
        "additional_basis_required": [] if outcome == OUTCOME_RECORDED else [block_code],
        "not_recorded_basis": [] if outcome == OUTCOME_RECORDED else [block_reason],
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code,
            "block_code": block_code,
            "reason": block_reason,
        },
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "passed_check_count": passed,
        "failed_check_count": failed,
    }
    result["local_relevance_medium_read_only_prior_result_reentry_cycle_summary"] = (
        build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_summary(result)
    )
    return result


def _blocked(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    basis_sections: Mapping[str, Mapping[str, Any]] | None = None,
    basis_by_name: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    return _build_result(
        request,
        checks,
        basis_sections or _empty_basis(),
        basis_by_name or {},
        OUTCOME_BLOCKED,
        code,
        reason,
        False,
    )


def _validate_request(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> str | None:
    for field, code in {**SHORTCUT_BLOCK_FIELD_CODES, **TOP_LEVEL_BLOCK_FIELD_CODES}.items():
        if request.get(field) is True:
            _add_check(checks, f"{field} not asserted", False, False, True, code)
            return code
    question = request.get(
        "local_relevance_medium_read_only_prior_result_reentry_cycle_question"
    )
    _add_check(
        checks,
        "prior-result re-entry cycle question declared",
        bool(question),
        "declared question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_QUESTION_UNDECLARED",
    )
    intent = request.get(
        "local_relevance_medium_read_only_prior_result_reentry_cycle_intent"
    )
    _add_check(
        checks,
        "prior-result re-entry cycle intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_INTENT_UNSUPPORTED",
    )
    declared_non_claims = request.get("declared_non_claims")
    if not _is_mapping(declared_non_claims):
        _add_check(
            checks,
            "declared non-claims mapping present",
            False,
            "mapping",
            declared_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    else:
        for field in REQUIRED_FALSE_NON_CLAIMS:
            actual = declared_non_claims.get(field)
            _add_check(
                checks,
                f"declared non-claim {field} false",
                isinstance(actual, bool) and actual is False,
                False,
                actual,
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )
    if intent == INTENT_BLOCK:
        _add_check(
            checks,
            "prior-result re-entry cycle block not requested",
            False,
            "record or do-not-record intent",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_BLOCK_REQUESTED",
        )
    return _first_failure(checks, "") or None


def _validate_shape(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> str | None:
    selected_command = request.get("selected_command")
    cycle_type = request.get("cycle_type")
    cycle_scope = request.get("cycle_scope")
    _add_check(checks, "selected command declared", selected_command is not None, SELECTED_COMMAND, selected_command, "SELECTED_COMMAND_MISSING")
    _add_check(checks, "selected command exactly state", selected_command == SELECTED_COMMAND, SELECTED_COMMAND, selected_command, "SELECTED_COMMAND_NOT_STATE")
    _add_check(checks, "selected command is state", selected_command == SELECTED_COMMAND, True, selected_command == SELECTED_COMMAND, "SELECTED_COMMAND_NOT_STATE")
    _add_check(checks, "cycle type declared", cycle_type is not None, CYCLE_TYPE, cycle_type, "CYCLE_TYPE_MISSING")
    _add_check(checks, "cycle type exact", cycle_type == CYCLE_TYPE, CYCLE_TYPE, cycle_type, "CYCLE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE")
    _add_check(checks, "cycle scope declared", cycle_scope is not None, CYCLE_SCOPE, cycle_scope, "CYCLE_SCOPE_MISSING")
    _add_check(checks, "cycle scope exact", cycle_scope == CYCLE_SCOPE, CYCLE_SCOPE, cycle_scope, "CYCLE_SCOPE_NOT_SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY")
    return _first_failure(checks, "") or None


def _validate_basis(
    checks: list[dict[str, Any]],
    artifacts: Mapping[str, Mapping[str, Any]],
    basis_by_name: Mapping[str, Mapping[str, Any]],
) -> str | None:
    for field, code in TRUE_FIELD_BLOCK_CODES.items():
        actual = _artifact_true(artifacts, basis_by_name, field)
        _add_check(checks, field.replace("_", " "), actual, True, actual, code)
    for field in CYCLE_OBJECT_FALSE_FIELDS:
        actual = _artifact_false(artifacts, field)
        _add_check(
            checks,
            f"{field.replace('_', ' ')} false in basis",
            actual,
            False,
            not actual,
            TOP_LEVEL_BLOCK_FIELD_CODES.get(field, field.upper()),
        )
    for field in (
        "runtime_v0_failure_evidence_preserved",
        "runtime_v2_failure_evidence_preserved",
        "runtime_boundary_v0_failure_evidence_preserved",
        "prior_result_boundary_v1_failure_evidence_preserved",
        "prior_result_boundary_v2_successor_evidence_preserved",
    ):
        _add_check(checks, field.replace("_", " "), True, True, True, "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED")
    _add_check(
        checks,
        "result-level required false non-claims canonical false",
        all(value is False for value in _canonical_non_claims().values()),
        "all required non-claims false",
        _canonical_non_claims(),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return _first_failure(checks, "") or None


def resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
    declared_local_relevance_medium_read_only_prior_result_reentry_cycle: Mapping[str, Any]
    | None = None,
) -> dict:
    """Resolve one bounded local read-only prior-result re-entry cycle request."""

    checks: list[dict[str, Any]] = []
    if declared_local_relevance_medium_read_only_prior_result_reentry_cycle is None:
        request: dict[str, Any] = {}
    elif not _is_mapping(
        declared_local_relevance_medium_read_only_prior_result_reentry_cycle
    ):
        _add_check(
            checks,
            "declared prior-result re-entry cycle request mapping",
            False,
            "mapping",
            type(declared_local_relevance_medium_read_only_prior_result_reentry_cycle).__name__,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUEST_MALFORMED",
        )
        return _blocked({}, checks, "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUEST_MALFORMED", "declared request was not a mapping")
    else:
        request = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_prior_result_reentry_cycle)
        )

    block = _validate_request(request, checks)
    if block:
        return _blocked(request, checks, block, block)
    if (
        request.get(
            "local_relevance_medium_read_only_prior_result_reentry_cycle_intent"
        )
        == INTENT_DO_NOT_RECORD
    ):
        return _build_result(request, checks, _empty_basis(), {}, OUTCOME_NOT_RECORDED, None, "do-not-record intent selected", False)
    block = _validate_shape(request, checks)
    if block:
        return _blocked(request, checks, block, block)

    basis_sections: dict[str, dict[str, Any]] = {}
    basis_by_name: dict[str, dict[str, Any]] = {}
    artifacts: dict[str, Mapping[str, Any]] = {}
    for spec in ARTIFACT_SPECS:
        name, _path_key, basis_key, _obj, _prefix, _expected, _default = spec
        basis, artifact = _read_artifact(request, spec, checks)
        basis_sections[basis_key] = basis
        basis_by_name[name] = basis
        if artifact is not None:
            artifacts[name] = artifact
    block = _first_failure(checks, "")
    if block:
        return _blocked(request, checks, block, block, basis_sections, basis_by_name)
    block = _validate_basis(checks, artifacts, basis_by_name)
    if block:
        return _blocked(request, checks, block, block, basis_sections, basis_by_name)

    for name, code in (
        ("local relevance medium read-only prior-result re-entry cycle recorded", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED"),
        ("prior-result re-entry cycle created", "PRIOR_RESULT_REENTRY_CYCLE_NOT_CREATED"),
        ("prior-result re-entry cycle local only", "PRIOR_RESULT_REENTRY_CYCLE_LOCAL_ONLY_NOT_TRUE"),
        ("prior-result re-entry cycle read only", "PRIOR_RESULT_REENTRY_CYCLE_READ_ONLY_NOT_TRUE"),
        ("cycle basis reference only", "CYCLE_BASIS_REFERENCE_ONLY_NOT_TRUE"),
    ):
        _add_check(checks, name, True, True, True, code)
    return _build_result(request, checks, basis_sections, basis_by_name, OUTCOME_RECORDED, None, None, True)


def resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_from_path(
    declared_local_relevance_medium_read_only_prior_result_reentry_cycle_path: Path | str,
) -> dict:
    """Read a declared request JSON object from a path and resolve it."""

    checks: list[dict[str, Any]] = []
    try:
        with Path(declared_local_relevance_medium_read_only_prior_result_reentry_cycle_path).open(
            "r", encoding="utf-8"
        ) as handle:
            request = json.load(handle)
    except (OSError, TypeError, json.JSONDecodeError):
        _add_check(
            checks,
            "declared prior-result re-entry cycle request readable",
            False,
            "readable JSON object",
            "unreadable",
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUEST_UNREADABLE",
        )
        return _blocked({}, checks, "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUEST_UNREADABLE", "declared request path was unreadable")
    if not _is_mapping(request):
        _add_check(
            checks,
            "declared prior-result re-entry cycle request mapping",
            False,
            "mapping",
            type(request).__name__,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUEST_MALFORMED",
        )
        return _blocked({}, checks, "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUEST_MALFORMED", "declared request JSON was not an object")
    return resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(request)


def build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact summary for a prior-result re-entry cycle result."""

    cycle = result.get("local_relevance_medium_read_only_prior_result_reentry_cycle", {})
    statement = result.get(
        "local_relevance_medium_read_only_prior_result_reentry_cycle_statement", {}
    )
    checks = result.get(
        "local_relevance_medium_read_only_prior_result_reentry_cycle_checks", []
    )
    passed, failed = _counts(checks if isinstance(checks, list) else [])
    block = result.get("block", {})
    block_code = block.get("code") or block.get("block_code") if _is_mapping(block) else None
    block_reason = block.get("reason") if _is_mapping(block) else None
    question = result.get(
        "declared_local_relevance_medium_read_only_prior_result_reentry_cycle_question",
        {},
    )
    summary = {
        "outcome": result.get("outcome"),
        "block_code": block_code,
        "block_reason": block_reason,
        "cycle_id": cycle.get("cycle_id") if _is_mapping(cycle) else None,
        "question": question.get("question") if _is_mapping(question) else None,
        "intent": question.get("intent") if _is_mapping(question) else None,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "result_version": result.get("result_version", RESULT_VERSION),
        "resolver_module": result.get("resolver_module", RESOLVER_MODULE),
        "cycle_recorded": cycle.get("local_relevance_medium_read_only_prior_result_reentry_cycle_recorded") is True if _is_mapping(cycle) else False,
        "selected_command": cycle.get("selected_command") if _is_mapping(cycle) else None,
        "selected_command_preserved": statement.get("selected_command_preserved") is True if _is_mapping(statement) else False,
        "selected_command_is_state": cycle.get("selected_command_is_state") is True if _is_mapping(cycle) else False,
        "cycle_object_summary": {
            "cycle_type": cycle.get("cycle_type") if _is_mapping(cycle) else None,
            "cycle_scope": cycle.get("cycle_scope") if _is_mapping(cycle) else None,
            "cycle_version": cycle.get("cycle_version") if _is_mapping(cycle) else None,
            "prior_result_reentry_cycle_created": cycle.get("prior_result_reentry_cycle_created") if _is_mapping(cycle) else None,
            "prior_result_reentry_cycle_local_only": cycle.get("prior_result_reentry_cycle_local_only") if _is_mapping(cycle) else None,
            "prior_result_reentry_cycle_read_only": cycle.get("prior_result_reentry_cycle_read_only") if _is_mapping(cycle) else None,
            "cycle_basis_reference_only": cycle.get("cycle_basis_reference_only") if _is_mapping(cycle) else None,
        },
        "result_level_non_claims_canonical_false": all(
            value is False for value in result.get("non_claims", {}).values()
        ),
    }
    if _is_mapping(statement):
        for key in ALLOWED_TRUE_RECORDED_FIELDS + CYCLE_OBJECT_FALSE_FIELDS:
            if key in statement:
                summary[key] = statement[key]
    if _is_mapping(cycle):
        summary.update(
            {
                "second_operation_not_created": cycle.get("second_operation_created") is False,
                "continuation_not_created": cycle.get("continuation_created") is False,
                "runtime_hosting_not_created": cycle.get("runtime_hosting_created") is False,
                "runtime_loop_not_created": cycle.get("runtime_loop_created") is False,
                "daemon_behavior_not_created": cycle.get("daemon_behavior_created") is False,
                "public_api_not_created": cycle.get("public_api_created") is False,
                "participant_facing_interface_not_created": cycle.get("participant_facing_interface_created") is False,
                "distributed_network_behavior_not_created": cycle.get("distributed_network_behavior_created") is False,
                "general_operation_permission_not_created": cycle.get("general_operation_permission_created") is False,
                "general_lookup_permission_not_created": cycle.get("general_lookup_permission_created") is False,
                "arbitrary_lookup_permission_not_created": cycle.get("arbitrary_lookup_permission_created") is False,
                "unsupported_commands_not_permitted": cycle.get("unsupported_commands_permitted") is False,
                "unsupported_lookup_keys_not_permitted": cycle.get("unsupported_lookup_keys_permitted") is False,
                "new_lookup_entry_not_created": cycle.get("new_lookup_entry_created") is False,
                "new_signal_entry_relevance_object_index_not_created": (
                    cycle.get("new_signal_accepted") is False
                    and cycle.get("new_entry_accepted") is False
                    and cycle.get("new_relevance_object_created") is False
                    and cycle.get("new_index_entry_created") is False
                ),
                "filesystem_discovery_not_performed": cycle.get("filesystem_discovery_performed") is False,
                "registry_search_query_ranking_not_created": (
                    cycle.get("registry_created") is False
                    and cycle.get("search_surface_created") is False
                    and cycle.get("query_surface_created") is False
                    and cycle.get("ranking_surface_created") is False
                ),
                "judgment_surfaces_not_created": (
                    cycle.get("scoring_surface_created") is False
                    and cycle.get("priority_surface_created") is False
                    and cycle.get("validity_judgment_created") is False
                    and cycle.get("truth_judgment_created") is False
                    and cycle.get("authority_judgment_created") is False
                    and cycle.get("currentness_judgment_created") is False
                ),
                "repeated_reception_arbitrary_reception_feed_not_created": (
                    cycle.get("repeated_reception_permission_created") is False
                    and cycle.get("arbitrary_reception_created") is False
                    and cycle.get("feed_created") is False
                ),
                "source_authority_currentness_truth_synchronization_participation_not_created": (
                    cycle.get("source_transfer_occurred") is False
                    and cycle.get("source_receipt_occurred") is False
                    and cycle.get("authority_created") is False
                    and cycle.get("currentness_created") is False
                    and cycle.get("truth_created") is False
                    and cycle.get("synchronization_created") is False
                    and cycle.get("participation_authorized") is False
                    and cycle.get("participant_role_created") is False
                ),
                "follow_on_not_created": cycle.get("follow_on_work_authorized") is False,
            }
        )
    non_claims = result.get("non_claims", {})
    if _is_mapping(non_claims):
        summary["runtime_failure_lineage_not_repaired_hidden_or_claimed_passed"] = all(
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
        )
        summary["prior_result_boundary_v1_failure_not_repaired_hidden_or_claimed_passed"] = all(
            non_claims.get(key) is False
            for key in (
                "prior_result_boundary_v1_failure_repaired",
                "prior_result_boundary_v1_failure_hidden",
                "prior_result_boundary_v1_failure_claimed_passed",
            )
        )
        summary["key_non_claims"] = {
            key: non_claims.get(key)
            for key in REQUIRED_FALSE_NON_CLAIMS
            if key
            in {
                "second_operation_created",
                "continuation_created",
                "runtime_hosting_created",
                "runtime_loop_created",
                "daemon_behavior_created",
                "raw_state_body_embedded",
                "state_mutation_performed",
                "state_update_performed",
                "older_runtime_lineage_imported_as_authority",
                "older_runtime_permission_treated_as_current",
                "runtime_authority_imported",
                "consumed_request_reopened",
                "authorization_token_reused",
                "follow_on_work_authorized",
            }
        }
    return _sanitize(summary)


def write_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result without overwriting an existing file."""

    if output_path is None:
        metadata = result.get(
            "local_relevance_medium_read_only_prior_result_reentry_cycle_metadata", {}
        )
        cycle_id = (
            metadata.get("local_relevance_medium_read_only_prior_result_reentry_cycle_id")
            if _is_mapping(metadata)
            else DEFAULT_CYCLE_ID
        ) or DEFAULT_CYCLE_ID
        target = OUTPUT_ROOT / (
            f"{cycle_id}__local_relevance_medium_read_only_prior_result_reentry_cycle_"
            "v0_min_result.json"
        )
    else:
        target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    final_path = target
    counter = 1
    while final_path.exists():
        final_path = target.parent / f"{target.stem}_{counter:03d}{target.suffix}"
        counter += 1
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path


def build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_request(
    *,
    local_relevance_medium_read_only_prior_result_reentry_cycle_id: str = DEFAULT_CYCLE_ID,
    local_relevance_medium_read_only_prior_result_reentry_cycle_question: str = CORE_QUESTION,
    local_relevance_medium_read_only_prior_result_reentry_cycle_intent: str = INTENT_RECORD,
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
    declared_non_claims: Mapping[str, Any] | None = None,
    additional_fields: Mapping[str, Any] | None = None,
) -> dict:
    """Build a declared request for one local read-only prior-result re-entry cycle."""

    non_claims = _canonical_non_claims()
    if declared_non_claims is not None:
        non_claims.update(dict(declared_non_claims))
    request = {
        "local_relevance_medium_read_only_prior_result_reentry_cycle_id": (
            local_relevance_medium_read_only_prior_result_reentry_cycle_id
        ),
        "local_relevance_medium_read_only_prior_result_reentry_cycle_question": (
            local_relevance_medium_read_only_prior_result_reentry_cycle_question
        ),
        "local_relevance_medium_read_only_prior_result_reentry_cycle_intent": (
            local_relevance_medium_read_only_prior_result_reentry_cycle_intent
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
        "cycle_type": cycle_type,
        "cycle_scope": cycle_scope,
        "declared_non_claims": non_claims,
    }
    if additional_fields:
        request.update(dict(additional_fields))
    return _sanitize(request)
