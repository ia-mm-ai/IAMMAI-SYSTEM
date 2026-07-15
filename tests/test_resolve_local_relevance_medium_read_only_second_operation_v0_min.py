"""Tests for the local relevance medium read-only second-operation resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION object. It verifies that the
resolver reads one clean selected second-operation boundary artifact, one clean
prior-result re-entry cycle artifact, one clean prior-result re-entry boundary
artifact, one clean runtime-held-re-entry artifact, one clean
runtime-held-re-entry boundary artifact, one clean runtime-held-state artifact,
one clean runtime-held-state boundary artifact, one clean runtime v3 artifact,
one clean runtime boundary v2 artifact, one clean runtime permission artifact,
and one clean selected operation execution artifact, then records one local
read-only selected-second-operation-only basis-reference-only operation object.

The operation object records second-operation-created true only in the bounded
local/read-only/basis-reference-only selected-state posture. It creates no
continuation, hosting, loop, daemon behavior, public API, participant-facing
interface, distributed behavior, raw state body, state mutation, state update,
older runtime authority import, authority/currentness/truth judgment, or
follow-on work.
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

import resolve_local_relevance_medium_read_only_second_operation_v0_min as resolver  # noqa: E402


OPERATION_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION"
OPERATION_SCOPE = "SELECTED_SECOND_OPERATION_ONLY"
SELECTED_COMMAND = "state"
REQ_FALSE = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
FIELD_CODES = getattr(resolver, "FIELD_BLOCK_CODES", {})

EXPECTED_OUTCOME_FAMILY = {
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_NOT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_REQUIRES_ADDITIONAL_BASIS",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BLOCKED",
}

EXPECTED_WRAPPER_SECTIONS = {
    "local_relevance_medium_read_only_second_operation_metadata",
    "declared_local_relevance_medium_read_only_second_operation_question",
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
    "local_relevance_medium_read_only_second_operation",
    "local_relevance_medium_read_only_second_operation_checks",
    "local_relevance_medium_read_only_second_operation_statement",
    "local_relevance_medium_read_only_second_operation_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_second_operation_summary",
}

FORBIDDEN_WRAPPER_FIELDS_IN_OPERATION = {
    "outcome",
    "block",
    "local_relevance_medium_read_only_second_operation_checks",
    "non_claims",
    "local_relevance_medium_read_only_second_operation_summary",
    "local_relevance_medium_read_only_second_operation_metadata",
}

DEFAULT_SUFFIXES = {
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

LINEAGE_TRUE_FIELDS = {
    "second_operation_boundary_v1_failure_evidence_preserved": True,
    "second_operation_boundary_v2_successor_evidence_preserved": True,
    "prior_result_cycle_v1_failure_evidence_preserved": True,
    "prior_result_cycle_v2_successor_evidence_preserved": True,
    "prior_result_boundary_v1_failure_evidence_preserved": True,
    "prior_result_boundary_v2_successor_evidence_preserved": True,
    "runtime_v0_failure_evidence_preserved": True,
    "runtime_v2_failure_evidence_preserved": True,
    "runtime_boundary_v0_failure_evidence_preserved": True,
    "lookup_command_execution_boundary_v1_filename_path_failure_evidence_preserved": True,
    "state_packet_body_exposure_boundary_v0_failure_evidence_preserved": True,
    "state_packet_body_exposure_v1_over_strict_test_evidence_preserved": True,
    "local_carrier_command_execution_boundary_v1_over_strict_failure_evidence_preserved": True,
    "predecessor_failure_evidence_preserved": True,
}
OPERATION_LINEAGE_TRUE_FIELDS = tuple(
    key for key in LINEAGE_TRUE_FIELDS if key != "predecessor_failure_evidence_preserved"
)

BASIS = (
    {
        "name": "second_operation_boundary",
        "request_key": "selected_second_operation_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_second_operation_boundary",
        "basis_prefix": "basis_second_operation_boundary",
        "block_prefix": "SECOND_OPERATION_BOUNDARY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_RECORDED",
        "type_key": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY",
        "scope_key": "boundary_scope",
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
        "block_prefix": "PRIOR_RESULT_REENTRY_CYCLE_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_RECORDED",
        "type_key": "cycle_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE",
        "scope_key": "cycle_scope",
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
        "block_prefix": "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_RECORDED",
        "type_key": "boundary_type",
        "type_value": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY",
        "scope_key": "boundary_scope",
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

BASIS_BY_NAME = {item["name"]: item for item in BASIS}

SUCCESS_TRUE_FIELDS = (
    "selected_command_is_state",
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
    "local_relevance_medium_read_only_second_operation_recorded",
    "second_operation_created",
    "second_operation_local_only",
    "second_operation_read_only",
    "second_operation_basis_reference_only",
    "second_operation_sequence_index_is_2",
) + OPERATION_LINEAGE_TRUE_FIELDS

FORBIDDEN_FINAL_FALSE_FIELDS = (
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

EXACT_FORBIDDEN_BLOCK_FIELDS = (
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

REQUEST_BLOCK_FIELDS = (
    "consumed_request_reopened",
    "authorization_token_reused",
    "older_runtime_lineage_imported_as_authority",
    "older_runtime_permission_treated_as_current",
    "runtime_authority_imported",
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
    "continuation_created",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "follow_on_work_authorized",
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

HOSTILE_SENTINELS = (
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
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


class LocalRelevanceMediumReadOnlySecondOperationV0MinTests(unittest.TestCase):
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

    def write_json(self, path: Path, value: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get("local_relevance_medium_read_only_second_operation_checks")
        return checks if isinstance(checks, list) else []

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        summary = result.get("local_relevance_medium_read_only_second_operation_summary")
        if isinstance(summary, Mapping) and isinstance(summary.get("failed_check_count"), int):
            return int(summary["failed_check_count"])
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        summary = result.get("local_relevance_medium_read_only_second_operation_summary")
        if isinstance(summary, Mapping) and isinstance(summary.get("passed_check_count"), int):
            return int(summary["passed_check_count"])
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def operation(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        operation = result.get("local_relevance_medium_read_only_second_operation")
        self.assertIsInstance(operation, Mapping)
        return operation

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get("local_relevance_medium_read_only_second_operation_statement")
        self.assertIsInstance(statement, Mapping)
        return statement

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get("local_relevance_medium_read_only_second_operation_summary")
        self.assertIsInstance(summary, Mapping)
        return summary

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

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
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)

    def assert_second_operation_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for key in (
            "second_operation_created",
            "second_operation_local_only",
            "second_operation_read_only",
            "second_operation_basis_reference_only",
            "second_operation_sequence_index_is_2",
        ):
            self.assertNotIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
            self.assertNotIn(key, non_claims)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_second_operation_non_claims(result)

    def assert_same_or_stable_artifact_path(self, actual: Any, expected: Any) -> None:
        actual_path = Path(str(actual))
        expected_path = Path(str(expected))
        try:
            self.assertEqual(actual_path.resolve(), expected_path.resolve())
            return
        except (AssertionError, OSError):
            pass
        self.assertEqual(actual_path.name, expected_path.name)

    def assert_code_present(self, result: Mapping[str, Any], code: str) -> None:
        emitted = {
            check.get("block_code") or check.get("failure_code")
            for check in self.checks(result)
            if check.get("passed") is False
        }
        if self.block_code(result):
            emitted.add(self.block_code(result))
        self.assertIn(code, emitted)

    def assert_wrapper_separated(self, result: Mapping[str, Any]) -> None:
        operation = self.operation(result)
        for key in FORBIDDEN_WRAPPER_FIELDS_IN_OPERATION:
            self.assertNotIn(key, operation)

    def assert_no_forbidden_runtime_posture(self, result: Mapping[str, Any]) -> None:
        operation = self.operation(result)
        for key in FORBIDDEN_FINAL_FALSE_FIELDS:
            self.assertIn(key, operation)
            self.assertIs(operation[key], False, key)
        summary = self.summary(result)
        self.assertIs(summary.get("continuation_not_created"), True)
        self.assertIs(summary.get("runtime_hosting_not_created"), True)
        self.assertIs(summary.get("runtime_loop_not_created"), True)
        self.assertIs(summary.get("daemon_behavior_not_created"), True)
        self.assertIs(summary.get("raw_state_body_not_embedded"), True)
        self.assertIs(summary.get("state_mutation_not_performed"), True)
        self.assertIs(summary.get("state_update_not_performed"), True)
        self.assertIs(summary.get("older_runtime_lineage_not_imported_as_authority"), True)
        self.assertIs(summary.get("older_runtime_permission_not_treated_as_current"), True)
        self.assertIs(summary.get("runtime_authority_not_imported"), True)

    def assert_success_posture(self, result: Mapping[str, Any]) -> None:
        operation = self.operation(result)
        self.assertEqual(operation["operation_id"], "local_relevance_medium_read_only_second_operation_001")
        self.assertEqual(operation["operation_type"], OPERATION_TYPE)
        self.assertEqual(operation["operation_version"], resolver.RESULT_VERSION)
        self.assertEqual(operation["operation_scope"], OPERATION_SCOPE)
        self.assertEqual(operation["operation_sequence_index"], 2)
        self.assertEqual(operation["selected_command"], SELECTED_COMMAND)
        for spec in BASIS:
            prefix = spec["basis_prefix"]
            self.assertEqual(operation[f"{prefix}_outcome"], spec["outcome"])
            self.assertEqual(operation[f"{prefix}_result_version"], resolver.RESULT_VERSION)
            self.assertEqual(operation[f"{prefix}_failed_check_count"], 0)
        for key in SUCCESS_TRUE_FIELDS:
            self.assertIn(key, operation)
            self.assertIs(operation[key], True, key)
        self.assert_no_forbidden_runtime_posture(result)
        self.assert_wrapper_separated(result)

    def assert_statement_success_posture(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        self.assertIs(statement["local_relevance_medium_read_only_second_operation_recorded"], True)
        for spec in BASIS:
            self.assertIs(statement[f"{spec['basis_prefix']}_artifact_preserved"], True)
        self.assertIs(statement["selected_command_preserved"], True)
        self.assertIs(statement["selected_command_is_state"], True)
        for key in (
            "second_operation_created",
            "second_operation_local_only",
            "second_operation_read_only",
            "second_operation_basis_reference_only",
            "second_operation_sequence_index_is_2",
            "consumed_request_token_remains_closed",
            "authorization_token_reuse_blocked",
            "predecessor_failure_evidence_preserved",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(statement[key], True, key)
        self.assertIs(statement["continuation_created"], False)
        for key in LINEAGE_TRUE_FIELDS:
            self.assertIs(statement[key], True, key)

    def assert_failure_lineage_preserved(self, result: Mapping[str, Any]) -> None:
        operation = self.operation(result)
        statement = self.statement(result)
        summary = self.summary(result)
        for key in (
            "second_operation_boundary_v1_failure_evidence_preserved",
            "second_operation_boundary_v2_successor_evidence_preserved",
            "prior_result_cycle_v1_failure_evidence_preserved",
            "prior_result_cycle_v2_successor_evidence_preserved",
            "prior_result_boundary_v1_failure_evidence_preserved",
            "prior_result_boundary_v2_successor_evidence_preserved",
            "runtime_v0_failure_evidence_preserved",
            "runtime_v2_failure_evidence_preserved",
            "runtime_boundary_v0_failure_evidence_preserved",
        ):
            self.assertIs(operation[key], True, key)
            self.assertIs(statement[key], True, key)
            self.assertIs(summary[key], True, key)
        for key in (
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
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertIs(operation[key], False, key)
        self.assertIs(summary["failure_not_repaired"], True)
        self.assertIs(summary["failure_not_hidden"], True)
        self.assertIs(summary["failure_not_claimed_passed"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)

    def synthetic_artifact(self, spec: Mapping[str, Any]) -> dict[str, Any]:
        true_fields = dict(LINEAGE_TRUE_FIELDS)
        true_fields.update(spec["true_fields"])
        selected = {
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "local_only": True,
            "read_only": True,
            "basis_reference_only": True,
        }
        selected[str(spec["type_key"])] = spec["type_value"]
        selected[str(spec["scope_key"])] = spec["scope_value"]
        selected.update(true_fields)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            selected[key] = False
        selected.update(
            {
                "second_operation_created": False,
                "prior_result_reentry_cycle_created": selected.get(
                    "prior_result_reentry_cycle_created",
                    False,
                ),
                "runtime_held_reentry_created": selected.get(
                    "runtime_held_reentry_created",
                    False,
                ),
                "runtime_held_state_created": selected.get(
                    "runtime_held_state_created",
                    False,
                ),
                "runtime_created": selected.get("runtime_created", False),
            }
        )
        if spec["name"] == "second_operation_boundary":
            selected["second_operation_created"] = False
        if spec["name"].endswith("_boundary"):
            selected["prior_result_reentry_cycle_created"] = False
            selected["runtime_held_reentry_created"] = False
            selected["runtime_held_state_created"] = False
            selected["runtime_created"] = False

        statement = dict(true_fields)
        summary = dict(true_fields)
        non_meaning = {
            key: value
            for key, value in true_fields.items()
            if "evidence_preserved" in key or "successor_evidence_preserved" in key
        }
        non_meaning.update(
            {
                "result_level_non_claims_canonical_false": True,
                "continuation_not_created": True,
                "raw_state_body_not_embedded": True,
                "state_mutation_not_performed": True,
                "state_update_not_performed": True,
            }
        )
        artifact = {
            "outcome": spec["outcome"],
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
            "passed_check_count": 5,
            spec["object_key"]: selected,
            f"{spec['object_key']}_statement": statement,
            f"{spec['object_key']}_summary": summary,
            f"{spec['object_key']}_non_meaning": non_meaning,
            f"{spec['object_key']}_checks": [
                {
                    "check_name": "synthetic_clean_recorded_basis",
                    "passed": True,
                    "expected_posture": "recorded clean basis",
                    "actual_posture": True,
                    "block_code": None,
                    "failure_code": None,
                }
            ],
            "non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
        }
        return artifact

    def build_synthetic_environment(
        self,
        root: Path,
        mutate_artifact: Callable[[Mapping[str, Any], dict[str, Any]], None] | None = None,
    ) -> tuple[dict[str, Any], dict[str, dict[str, Any]], dict[str, Path]]:
        artifacts: dict[str, dict[str, Any]] = {}
        paths: dict[str, Path] = {}
        request_paths: dict[str, str] = {}
        for index, spec in enumerate(BASIS, start=1):
            artifact = self.synthetic_artifact(spec)
            if mutate_artifact is not None:
                mutate_artifact(spec, artifact)
            filename = self.safe_json_filename(f"{spec['name']}_artifact", index)
            path = self.write_json(root / filename, artifact)
            artifacts[str(spec["name"])] = artifact
            paths[str(spec["request_key"])] = path
            request_paths[str(spec["request_key"])] = str(path)

        request = resolver.build_declared_local_relevance_medium_read_only_second_operation_v0_min_request(
            **request_paths
        )
        return request, artifacts, paths

    def resolve_synthetic(
        self,
        root: Path,
        mutate_artifact: Callable[[Mapping[str, Any], dict[str, Any]], None] | None = None,
    ) -> tuple[dict[str, Any], dict[str, Any], dict[str, dict[str, Any]], dict[str, Path]]:
        request, artifacts, paths = self.build_synthetic_environment(root, mutate_artifact)
        result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
            request
        )
        return request, result, artifacts, paths

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_second_operation_v0_min",
            "resolve_local_relevance_medium_read_only_second_operation_v0_min_from_path",
            "write_local_relevance_medium_read_only_second_operation_v0_min_result",
            "build_local_relevance_medium_read_only_second_operation_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_second_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_OPERATION_TYPE_VALUES",
            "SUPPORTED_OPERATION_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_second_operation_v0_min",
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_v0_min"
            )
        )
        self.assertIn(OPERATION_TYPE, resolver.SUPPORTED_OPERATION_TYPE_VALUES)
        self.assertIn(OPERATION_SCOPE, resolver.SUPPORTED_OPERATION_SCOPE_VALUES)
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
        for key in (
            "second_operation_created",
            "second_operation_local_only",
            "second_operation_read_only",
            "second_operation_basis_reference_only",
            "second_operation_sequence_index_is_2",
        ):
            self.assertNotIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
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
        self.assertTrue(EXPECTED_OUTCOME_FAMILY.issubset(set(resolver.OUTCOME_FAMILY)))

        request = resolver.build_declared_local_relevance_medium_read_only_second_operation_v0_min_request()
        for key, suffix in DEFAULT_SUFFIXES.items():
            self.assertTrue(str(request[key]).endswith(suffix), key)
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        self.assertEqual(request["operation_type"], OPERATION_TYPE)
        self.assertEqual(request["operation_scope"], OPERATION_SCOPE)
        self.assertEqual(request["operation_sequence_index"], 2)
        self.assertIsInstance(request["declared_non_claims"], Mapping)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, request["declared_non_claims"])
            self.assertIs(request["declared_non_claims"][key], False)

    def test_records_one_second_operation_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, result, _artifacts, paths = self.resolve_synthetic(Path(tmp))

            self.assertIsInstance(result, dict)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.failed_check_count(result), 0)
            self.assertGreater(self.passed_check_count(result), 0)
            self.assert_not_blocked(result)
            self.assertEqual(self.summary(result)["result_version"], "0.1.0")
            self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(
                self.operation(result)["operation_id"],
                request["local_relevance_medium_read_only_second_operation_id"],
            )
            self.assertTrue(EXPECTED_WRAPPER_SECTIONS.issubset(set(result)))
            self.assert_success_posture(result)
            self.assert_statement_success_posture(result)
            self.assert_canonical_false_non_claims(result)
            self.assert_second_operation_non_claims(result)
            self.assert_failure_lineage_preserved(result)
            for spec in BASIS:
                prefix = spec["basis_prefix"]
                self.assert_same_or_stable_artifact_path(
                    self.operation(result)[f"{prefix}_artifact"],
                    paths[str(spec["request_key"])],
                )

    def test_records_from_default_live_artifacts_when_present(self) -> None:
        request = resolver.build_declared_local_relevance_medium_read_only_second_operation_v0_min_request()
        missing = [
            key
            for key in DEFAULT_SUFFIXES
            if not (REPO_ROOT / str(request[key])).exists() and not Path(str(request[key])).exists()
        ]
        if missing:
            self.skipTest(f"default live artifacts missing: {', '.join(missing)}")

        result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
            request
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        operation = self.operation(result)
        self.assertEqual(operation["operation_type"], OPERATION_TYPE)
        self.assertEqual(operation["operation_scope"], OPERATION_SCOPE)
        self.assertEqual(operation["operation_sequence_index"], 2)
        self.assertEqual(operation["selected_command"], SELECTED_COMMAND)
        self.assertIs(operation["future_second_operation_may_be_considered"], True)
        self.assertIs(operation["second_operation_created"], True)
        self.assertIs(operation["second_operation_local_only"], True)
        self.assertIs(operation["second_operation_read_only"], True)
        self.assertIs(operation["second_operation_basis_reference_only"], True)
        self.assert_no_forbidden_runtime_posture(result)
        self.assert_failure_lineage_preserved(result)
        for spec in BASIS:
            section = result[str(spec["request_key"]).replace("artifact", "artifact_basis")]
            self.assert_same_or_stable_artifact_path(
                section["artifact_path"],
                request[str(spec["request_key"])],
            )

    def test_positive_basis_derivation_from_bounded_evidence(self) -> None:
        representative = {
            "selected_second_operation_boundary_recorded": "second_operation_boundary",
            "future_second_operation_may_be_considered": "second_operation_boundary",
            "selected_prior_result_reentry_cycle_recorded": "prior_result_reentry_cycle",
            "selected_prior_result_reentry_boundary_recorded": "prior_result_reentry_boundary",
            "selected_runtime_held_reentry_boundary_recorded": "runtime_held_reentry_boundary",
            "selected_runtime_held_state_boundary_recorded": "runtime_held_state_boundary",
            "selected_runtime_boundary_recorded": "runtime_boundary",
            "second_operation_boundary_v1_failure_evidence_preserved": "second_operation_boundary",
            "second_operation_boundary_v2_successor_evidence_preserved": "second_operation_boundary",
            "prior_result_cycle_v1_failure_evidence_preserved": "second_operation_boundary",
            "prior_result_cycle_v2_successor_evidence_preserved": "second_operation_boundary",
        }

        def mutate(spec: Mapping[str, Any], artifact: dict[str, Any]) -> None:
            object_value = artifact[str(spec["object_key"])]
            for field, basis_name in representative.items():
                if spec["name"] == basis_name:
                    object_value.pop(field, None)
                    artifact[f"{spec['object_key']}_statement"][field] = True
                    artifact[f"{spec['object_key']}_summary"][field] = True
                    artifact[f"{spec['object_key']}_non_meaning"][field] = True

        with tempfile.TemporaryDirectory() as tmp:
            _request, result, _artifacts, _paths = self.resolve_synthetic(
                Path(tmp),
                mutate,
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.failed_check_count(result), 0)
            self.assert_not_blocked(result)
            operation = self.operation(result)
            for field in representative:
                self.assertIs(operation[field], True, field)
            self.assertIs(operation["second_operation_created"], True)
            self.assertIs(operation["second_operation_local_only"], True)
            self.assertIs(operation["second_operation_read_only"], True)
            self.assertIs(operation["second_operation_basis_reference_only"], True)
            self.assertIs(operation["second_operation_sequence_index_is_2"], True)
            self.assert_no_forbidden_runtime_posture(result)

    def test_explanatory_true_values_do_not_trigger_forbidden_posture(self) -> None:
        explanatory_true = {
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
            "second_operation_created": True,
        }

        def mutate(_spec: Mapping[str, Any], artifact: dict[str, Any]) -> None:
            for section_name in (
                "statement",
                "summary",
                "non_meaning",
                "metadata",
                "explanatory_posture",
                "basis_commentary",
                "false_posture_preserved",
                "non_claim_preservation",
                "lineage_evidence",
            ):
                artifact[section_name] = dict(explanatory_true)
            artifact["checks"] = [
                {
                    "check_name": "continuation_not_created_false_posture_preserved",
                    "passed": True,
                    "expected_posture": "false posture preserved",
                    "actual_posture": True,
                    "block_code": None,
                    "failure_code": None,
                }
            ]

        with tempfile.TemporaryDirectory() as tmp:
            _request, result, _artifacts, _paths = self.resolve_synthetic(Path(tmp), mutate)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.failed_check_count(result), 0)
            self.assert_not_blocked(result)
            self.assert_success_posture(result)
            self.assert_canonical_false_non_claims(result)

    def test_exact_forbidden_selected_object_and_non_claim_true_blocks(self) -> None:
        for field in EXACT_FORBIDDEN_BLOCK_FIELDS:
            expected_code = FIELD_CODES.get(field, field.upper())
            with self.subTest(selected_object_field=field):
                def mutate_object(spec: Mapping[str, Any], artifact: dict[str, Any]) -> None:
                    if spec["name"] == "second_operation_boundary":
                        artifact[str(spec["object_key"])][field] = True

                with tempfile.TemporaryDirectory() as tmp:
                    _request, result, _artifacts, _paths = self.resolve_synthetic(
                        Path(tmp),
                        mutate_object,
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, expected_code)
                    self.assert_no_forbidden_runtime_posture(result)

            with self.subTest(top_level_non_claim=field):
                def mutate_non_claim(spec: Mapping[str, Any], artifact: dict[str, Any]) -> None:
                    if spec["name"] == "second_operation_boundary":
                        artifact[str(spec["object_key"])].pop(field, None)
                        artifact["non_claims"][field] = True

                with tempfile.TemporaryDirectory() as tmp:
                    _request, result, _artifacts, _paths = self.resolve_synthetic(
                        Path(tmp),
                        mutate_non_claim,
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, expected_code)
                    self.assert_no_forbidden_runtime_posture(result)

    def test_top_level_request_flips_and_declared_non_claim_malformed_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            clean_request, _artifacts, _paths = self.build_synthetic_environment(Path(tmp))
            for field in REQUEST_BLOCK_FIELDS:
                with self.subTest(top_level=field):
                    request = copy.deepcopy(clean_request)
                    request[field] = True
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, FIELD_CODES.get(field, field.upper()))
                    self.assert_no_forbidden_runtime_posture(result)

            for field in (
                "continuation_created",
                "raw_state_body_embedded",
                "state_mutation_performed",
                "state_update_performed",
                "older_runtime_lineage_imported_as_authority",
                "second_operation_boundary_v1_failure_repaired",
                "consumed_request_reopened",
                "authorization_token_reused",
            ):
                with self.subTest(declared_non_claim_true=field):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][field] = True
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assert_no_forbidden_runtime_posture(result)

                with self.subTest(declared_non_claim_missing=field):
                    request = copy.deepcopy(clean_request)
                    del request["declared_non_claims"][field]
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, "NON_CLAIM_MISSING_OR_FLIPPED")

                with self.subTest(declared_non_claim_non_bool=field):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][field] = "false"
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_required_false_non_claims_canonicalize_false_when_flipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            clean_request, _artifacts, _paths = self.build_synthetic_environment(Path(tmp))
            for index, key in enumerate(resolver.REQUIRED_FALSE_NON_CLAIMS):
                with self.subTest(key=key, index=index):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_no_forbidden_runtime_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            clean_request, clean_artifacts, paths = self.build_synthetic_environment(root)

            base_cases: list[tuple[str, Callable[[dict[str, Any]], dict[str, Any]], str | tuple[str, ...]]] = [
                (
                    "explicit_block_intent",
                    lambda request: {**request, "local_relevance_medium_read_only_second_operation_intent": resolver.INTENT_BLOCK},
                    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BLOCK_REQUESTED",
                ),
                (
                    "unsupported_intent",
                    lambda request: {**request, "local_relevance_medium_read_only_second_operation_intent": "UNSUPPORTED"},
                    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_INTENT_UNSUPPORTED",
                ),
                (
                    "selected_command_missing",
                    lambda request: {k: v for k, v in request.items() if k != "selected_command"},
                    "SELECTED_COMMAND_MISSING",
                ),
                (
                    "selected_command_not_state",
                    lambda request: {**request, "selected_command": "status"},
                    "SELECTED_COMMAND_NOT_STATE",
                ),
                (
                    "operation_type_missing",
                    lambda request: {k: v for k, v in request.items() if k != "operation_type"},
                    "OPERATION_TYPE_MISSING",
                ),
                (
                    "operation_type_wrong",
                    lambda request: {**request, "operation_type": "LOCAL_RELEVANCE_MEDIUM_CONTINUATION"},
                    "OPERATION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION",
                ),
                (
                    "operation_scope_missing",
                    lambda request: {k: v for k, v in request.items() if k != "operation_scope"},
                    "OPERATION_SCOPE_MISSING",
                ),
                (
                    "operation_scope_wrong",
                    lambda request: {**request, "operation_scope": "GENERAL_OPERATION"},
                    "OPERATION_SCOPE_NOT_SELECTED_SECOND_OPERATION_ONLY",
                ),
                (
                    "operation_sequence_missing",
                    lambda request: {k: v for k, v in request.items() if k != "operation_sequence_index"},
                    "OPERATION_SEQUENCE_INDEX_MISSING",
                ),
                (
                    "operation_sequence_wrong",
                    lambda request: {**request, "operation_sequence_index": 3},
                    "OPERATION_SEQUENCE_INDEX_NOT_2",
                ),
                (
                    "required_non_claim_missing",
                    lambda request: {
                        **request,
                        "declared_non_claims": {
                            k: v
                            for k, v in request["declared_non_claims"].items()
                            if k != "continuation_created"
                        },
                    },
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "second_operation_not_created",
                    lambda request: {**request, "second_operation_created": False},
                    "SECOND_OPERATION_NOT_CREATED",
                ),
                (
                    "second_operation_local_only_not_true",
                    lambda request: {**request, "second_operation_local_only": False},
                    "SECOND_OPERATION_LOCAL_ONLY_NOT_TRUE",
                ),
                (
                    "second_operation_read_only_not_true",
                    lambda request: {**request, "second_operation_read_only": False},
                    "SECOND_OPERATION_READ_ONLY_NOT_TRUE",
                ),
                (
                    "second_operation_basis_reference_only_not_true",
                    lambda request: {**request, "second_operation_basis_reference_only": False},
                    "SECOND_OPERATION_BASIS_REFERENCE_ONLY_NOT_TRUE",
                ),
                (
                    "second_operation_sequence_index_is_2_not_true",
                    lambda request: {**request, "second_operation_sequence_index_is_2": False},
                    "SECOND_OPERATION_SEQUENCE_INDEX_IS_2_NOT_TRUE",
                ),
            ]
            for name, mutator, expected in base_cases:
                with self.subTest(name=name):
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        mutator(copy.deepcopy(clean_request))
                    )
                    self.assert_blocked_with_public_code(result)
                    expected_values = (expected,) if isinstance(expected, str) else expected
                    for code in expected_values:
                        self.assert_code_present(result, code)
                    self.assert_no_forbidden_runtime_posture(result)

            malformed_results = (
                resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(None),
                resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min([]),
            )
            for result in malformed_results:
                self.assert_blocked_with_public_code(result)

            positive_cases = (
                ("second_operation_boundary", "selected_second_operation_boundary_recorded", "SELECTED_SECOND_OPERATION_BOUNDARY_NOT_RECORDED"),
                ("second_operation_boundary", "future_second_operation_may_be_considered", "FUTURE_SECOND_OPERATION_MAY_NOT_BE_CONSIDERED"),
                ("prior_result_reentry_cycle", "prior_result_reentry_cycle_created", "PRIOR_RESULT_REENTRY_CYCLE_NOT_CREATED"),
                ("prior_result_reentry_cycle", "prior_result_reentry_cycle_local_only", "PRIOR_RESULT_REENTRY_CYCLE_NOT_LOCAL_ONLY"),
                ("prior_result_reentry_cycle", "prior_result_reentry_cycle_read_only", "PRIOR_RESULT_REENTRY_CYCLE_NOT_READ_ONLY"),
                ("prior_result_reentry_cycle", "cycle_basis_reference_only", "CYCLE_BASIS_NOT_REFERENCE_ONLY"),
                ("prior_result_reentry_boundary", "future_prior_result_reentry_cycle_may_be_considered", "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED"),
                ("runtime_held_reentry", "runtime_held_reentry_created", "RUNTIME_HELD_REENTRY_NOT_CREATED"),
                ("runtime_held_state", "runtime_held_state_created", "RUNTIME_HELD_STATE_NOT_CREATED"),
                ("runtime", "runtime_created", "RUNTIME_NOT_CREATED"),
                ("runtime_permission", "runtime_permission_created", "RUNTIME_PERMISSION_NOT_CREATED"),
                ("operation_execution", "operation_execution_performed", "OPERATION_EXECUTION_NOT_PERFORMED"),
            )
            for basis_name, field, expected_code in positive_cases:
                with self.subTest(positive=basis_name, field=field):
                    def mutate(spec: Mapping[str, Any], artifact: dict[str, Any]) -> None:
                        if spec["name"] == basis_name:
                            artifact[str(spec["object_key"])][field] = False

                    _request, result, _artifacts, _paths = self.resolve_synthetic(root, mutate)
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, expected_code)

            for spec in BASIS:
                request_key = str(spec["request_key"])
                prefix = str(spec["block_prefix"])
                with self.subTest(artifact_missing=request_key):
                    request = copy.deepcopy(clean_request)
                    request.pop(request_key)
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, f"{prefix}_PATH_MISSING")

                with self.subTest(artifact_unreadable=request_key):
                    request = copy.deepcopy(clean_request)
                    request[request_key] = str(root / self.safe_json_filename(f"missing_{request_key}"))
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, f"{prefix}_UNREADABLE")

                with self.subTest(artifact_array=request_key):
                    path = self.write_json(root / self.safe_json_filename(f"array_{request_key}"), [])
                    request = copy.deepcopy(clean_request)
                    request[request_key] = str(path)
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, f"{prefix}_UNREADABLE")

                with self.subTest(artifact_not_recorded=request_key):
                    artifact = copy.deepcopy(clean_artifacts[str(spec["name"])])
                    artifact["outcome"] = "WRONG_OUTCOME"
                    path = self.write_json(root / self.safe_json_filename(f"wrong_outcome_{request_key}"), artifact)
                    request = copy.deepcopy(clean_request)
                    request[request_key] = str(path)
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, f"{prefix}_NOT_RECORDED")

                with self.subTest(artifact_failed_checks=request_key):
                    artifact = copy.deepcopy(clean_artifacts[str(spec["name"])])
                    artifact["failed_check_count"] = 1
                    path = self.write_json(root / self.safe_json_filename(f"failed_checks_{request_key}"), artifact)
                    request = copy.deepcopy(clean_request)
                    request[request_key] = str(path)
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, f"{prefix}_FAILED_CHECKS_PRESENT")

                with self.subTest(artifact_version=request_key):
                    artifact = copy.deepcopy(clean_artifacts[str(spec["name"])])
                    artifact["result_version"] = "0.2.0"
                    path = self.write_json(root / self.safe_json_filename(f"bad_version_{request_key}"), artifact)
                    request = copy.deepcopy(clean_request)
                    request[request_key] = str(path)
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, f"{prefix}_VERSION_NOT_0_1_0")

            representative_false = (
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
                "artifact_existence_treated_as_second_operation_authority",
                "latest_file_posture_treated_as_second_operation_authority",
                "repo_local_availability_treated_as_second_operation_authority",
                "hidden_repo_state_used_as_second_operation_content",
                "hidden_repo_state_used_as_second_operation_authority",
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
            )
            for field in representative_false:
                with self.subTest(top_level_false_posture=field):
                    request = copy.deepcopy(clean_request)
                    request[field] = True
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, FIELD_CODES.get(field, field.upper()))
                    self.assert_no_forbidden_runtime_posture(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _request, result, _artifacts, _paths = self.resolve_synthetic(Path(tmp))
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            operation = self.operation(result)
            self.assertEqual(operation["operation_type"], OPERATION_TYPE)
            self.assertEqual(operation["operation_scope"], OPERATION_SCOPE)
            self.assertEqual(operation["operation_sequence_index"], 2)
            self.assertEqual(operation["selected_command"], SELECTED_COMMAND)
            self.assertTrue(EXPECTED_OUTCOME_FAMILY.issubset(set(resolver.OUTCOME_FAMILY)))
            serialized = json.dumps(result, sort_keys=True)
            for official in (
                resolver.OUTCOME_RECORDED,
                OPERATION_TYPE,
                OPERATION_SCOPE,
                SELECTED_COMMAND,
                resolver.RESOLVER_MODULE,
            ):
                self.assertIn(official, serialized)
            self.assertIn('"operation_sequence_index": 2', serialized)
            self.assertNotIn("[REDACTED", operation["operation_type"])
            self.assertNotIn("[REDACTED", operation["operation_scope"])
            self.assertNotIn("[REDACTED", operation["selected_command"])

    def test_raw_hidden_older_runtime_hostile_content_containment_and_non_mutation(self) -> None:
        def mutate(_spec: Mapping[str, Any], artifact: dict[str, Any]) -> None:
            for index, sentinel in enumerate(HOSTILE_SENTINELS):
                artifact[f"extra_section_{index}"] = {
                    "raw_state_body": sentinel,
                    "hidden_repo_state": sentinel,
                    "raw_full_prior_artifact_body": sentinel,
                    "local_cache": sentinel,
                }
            artifact["basis_commentary"] = {
                "official_operation_type": OPERATION_TYPE,
                "official_scope": OPERATION_SCOPE,
                "official_selected_command": SELECTED_COMMAND,
            }

        with tempfile.TemporaryDirectory() as tmp:
            request, artifacts, _paths = self.build_synthetic_environment(Path(tmp), mutate)
            request["raw_second_operation_body"] = HOSTILE_SENTINELS[0]
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            request_before = copy.deepcopy(request)
            artifacts_before = copy.deepcopy(artifacts)

            result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assertEqual(request, request_before)
            self.assertEqual(artifacts, artifacts_before)
            serialized = json.dumps(result, sort_keys=True)
            for sentinel in HOSTILE_SENTINELS:
                self.assertNotIn(sentinel, serialized)
            for official in (OPERATION_TYPE, OPERATION_SCOPE, SELECTED_COMMAND):
                self.assertIn(official, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assert_no_forbidden_runtime_posture(result)
            self.assert_failure_lineage_preserved(result)

    def test_path_and_write_behavior(self) -> None:
        forbidden_root_parts = {
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
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request, _artifacts, _paths = self.build_synthetic_environment(root)
            request_path = self.write_json(root / "request.json", request)
            result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.summary(result)["result_version"], resolver.RESULT_VERSION)
            self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_with_public_code(malformed)

            array_path = self.write_json(root / "array_request.json", [])
            array_result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min_from_path(
                array_path
            )
            self.assert_blocked_with_public_code(array_result)

            missing_result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min_from_path(
                root / "missing_request.json"
            )
            self.assert_blocked_with_public_code(missing_result)

            output_root = root / (
                "artifacts/"
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_v0_min"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_local_relevance_medium_read_only_second_operation_v0_min_result(
                    result
                )
                second = resolver.write_local_relevance_medium_read_only_second_operation_v0_min_result(
                    result
                )
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(first.parent, output_root)
            self.assertIn(
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_v0_min",
                first.parts,
            )
            self.assertTrue(json.loads(first.read_text(encoding="utf-8")))
            self.assertTrue(json.loads(second.read_text(encoding="utf-8")))
            self.assertTrue(forbidden_root_parts.isdisjoint(set(first.parts)))
            self.assertTrue(forbidden_root_parts.isdisjoint(set(second.parts)))

    def test_non_mutation_of_request_and_synthetic_artifacts(self) -> None:
        def mutate(spec: Mapping[str, Any], artifact: dict[str, Any]) -> None:
            artifact[str(spec["object_key"])]["positive_basis_derivation_marker"] = True
            artifact["explanatory_posture"] = {
                "continuation_not_created": True,
                "older_runtime_authority_import_refusal_preserved": True,
            }

        with tempfile.TemporaryDirectory() as tmp:
            request, artifacts, paths = self.build_synthetic_environment(Path(tmp), mutate)
            request_before = copy.deepcopy(request)
            artifacts_before = copy.deepcopy(artifacts)
            paths_before = copy.deepcopy(paths)
            result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assertEqual(request, request_before)
            self.assertEqual(artifacts, artifacts_before)
            self.assertEqual(paths, paths_before)
            self.assertEqual(request["selected_command"], SELECTED_COMMAND)
            self.assertEqual(request["operation_type"], OPERATION_TYPE)
            self.assertEqual(request["operation_scope"], OPERATION_SCOPE)
            self.assertEqual(request["operation_sequence_index"], 2)

    def test_failure_lineage_and_predecessor_summary_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _request, result, _artifacts, _paths = self.resolve_synthetic(Path(tmp))
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assert_failure_lineage_preserved(result)
            summary = self.summary(result)
            self.assertIs(summary["result_level_non_claims_canonical_false"], True)
            self.assertIs(summary["raw_state_body_not_embedded"], True)
            self.assertIs(summary["state_mutation_not_performed"], True)
            self.assertIs(summary["state_update_not_performed"], True)
            self.assertIs(summary["second_operation_created"], True)
            self.assertIs(summary["second_operation_local_only"], True)
            self.assertIs(summary["second_operation_read_only"], True)
            self.assertIs(summary["second_operation_basis_reference_only"], True)
            self.assertIs(summary["second_operation_sequence_index_is_2"], True)
            self.assertIs(summary["continuation_not_created"], True)

        with tempfile.TemporaryDirectory() as tmp:
            clean_request, _artifacts, _paths = self.build_synthetic_environment(Path(tmp))
            for field in (
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
            ):
                with self.subTest(field=field):
                    request = copy.deepcopy(clean_request)
                    request[field] = True
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_code_present(result, FIELD_CODES.get(field, field.upper()))
                    self.assert_no_forbidden_runtime_posture(result)


if __name__ == "__main__":
    unittest.main()
