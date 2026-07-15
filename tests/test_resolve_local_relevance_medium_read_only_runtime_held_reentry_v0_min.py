"""Tests for the local read-only runtime-held-re-entry resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY object. It verifies that
the resolver reads one clean runtime-held-re-entry boundary artifact, one clean
runtime-held-state artifact, one clean runtime-held-state boundary artifact,
one clean runtime v3 artifact, one clean runtime boundary v2 artifact, one
clean runtime permission artifact, and one clean operation execution artifact,
then records one local read-only selected-state runtime-held re-entry object
only.

The held re-entry remains selected-state-only, basis-reference-only,
raw-state-body-excluding, state-mutation-refusing, state-update-refusing,
non-prior-result-cycle-shaped, non-second-operation-shaped,
non-continuation-shaped, non-hosting-shaped, non-loop-shaped,
non-daemon-shaped, and older-runtime-authority-import-blocking.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min as resolver  # noqa: E402


HELD_REENTRY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY"
HELD_REENTRY_SCOPE = "SELECTED_RUNTIME_HELD_REENTRY_ONLY"
SELECTED_COMMAND = "state"

RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY_RECORDED"
)
RUNTIME_HELD_STATE_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_RECORDED"
)
RUNTIME_HELD_STATE_BOUNDARY_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_RECORDED"
)
RUNTIME_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED"
RUNTIME_BOUNDARY_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED"
RUNTIME_PERMISSION_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED"
)
OPERATION_EXECUTION_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED"
)

ARTIFACT_OBJECT_KEYS = {
    "held_reentry_boundary": "local_relevance_medium_read_only_runtime_held_reentry_boundary",
    "held_state": "local_relevance_medium_read_only_runtime_held_state",
    "held_state_boundary": "local_relevance_medium_read_only_runtime_held_state_boundary",
    "runtime": "local_relevance_medium_read_only_runtime",
    "runtime_boundary": "local_relevance_medium_read_only_runtime_boundary",
    "runtime_permission": "local_relevance_medium_read_only_runtime_permission",
    "operation_execution": "local_relevance_medium_read_only_operation_execution",
}

ARTIFACT_REQUEST_KEYS = {
    "held_reentry_boundary": "selected_runtime_held_reentry_boundary_artifact",
    "held_state": "selected_runtime_held_state_artifact",
    "held_state_boundary": "selected_runtime_held_state_boundary_artifact",
    "runtime": "selected_runtime_artifact",
    "runtime_boundary": "selected_runtime_boundary_artifact",
    "runtime_permission": "selected_runtime_permission_artifact",
    "operation_execution": "selected_operation_execution_artifact",
}

ARTIFACT_OUTCOMES = {
    "held_reentry_boundary": RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME,
    "held_state": RUNTIME_HELD_STATE_OUTCOME,
    "held_state_boundary": RUNTIME_HELD_STATE_BOUNDARY_OUTCOME,
    "runtime": RUNTIME_OUTCOME,
    "runtime_boundary": RUNTIME_BOUNDARY_OUTCOME,
    "runtime_permission": RUNTIME_PERMISSION_OUTCOME,
    "operation_execution": OPERATION_EXECUTION_OUTCOME,
}

DEFAULT_ARTIFACT_PATHS = {
    "selected_runtime_held_reentry_boundary_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min"
    / "local_relevance_medium_read_only_runtime_held_reentry_boundary_reference_review_001__local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min_result.json",
    "selected_runtime_held_state_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_v0_min"
    / "local_relevance_medium_read_only_runtime_held_state_reference_review_001__local_relevance_medium_read_only_runtime_held_state_v0_min_result.json",
    "selected_runtime_held_state_boundary_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min"
    / "local_relevance_medium_read_only_runtime_held_state_boundary_reference_review_001__local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result.json",
    "selected_runtime_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v3"
    / "local_relevance_medium_read_only_runtime_reference_review_001__local_relevance_medium_read_only_runtime_v0_min_v3_result.json",
    "selected_runtime_boundary_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min_v2"
    / "local_relevance_medium_read_only_runtime_boundary_reference_review_001__local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json",
    "selected_runtime_permission_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min"
    / "local_relevance_medium_read_only_runtime_permission_reference_review_001__local_relevance_medium_read_only_runtime_permission_v0_min_result.json",
    "selected_operation_execution_artifact": REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min"
    / "local_relevance_medium_read_only_operation_execution_reference_review_001__local_relevance_medium_read_only_operation_execution_v0_min_result.json",
}

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_runtime_held_reentry_metadata",
    "declared_local_relevance_medium_read_only_runtime_held_reentry_question",
    "selected_runtime_held_reentry_boundary_artifact_basis",
    "selected_runtime_held_state_artifact_basis",
    "selected_runtime_held_state_boundary_artifact_basis",
    "selected_runtime_artifact_basis",
    "selected_runtime_boundary_artifact_basis",
    "selected_runtime_permission_artifact_basis",
    "selected_operation_execution_artifact_basis",
    "local_relevance_medium_read_only_runtime_held_reentry",
    "local_relevance_medium_read_only_runtime_held_reentry_checks",
    "local_relevance_medium_read_only_runtime_held_reentry_statement",
    "local_relevance_medium_read_only_runtime_held_reentry_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_held_reentry_summary",
)

FORBIDDEN_HELD_REENTRY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_held_reentry_checks",
    "non_claims",
    "local_relevance_medium_read_only_runtime_held_reentry_summary",
    "local_relevance_medium_read_only_runtime_held_reentry_metadata",
)

HELD_REENTRY_TRUE_FIELDS = (
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
    "local_relevance_medium_read_only_runtime_held_reentry_recorded",
    "runtime_held_reentry_created",
    "runtime_held_reentry_local_only",
    "runtime_held_reentry_read_only",
    "held_reentry_basis_reference_only",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
)

HELD_REENTRY_FALSE_FIELDS = (
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
    "consumed_request_reopened",
    "authorization_token_reused",
    "follow_on_work_authorized",
)

STATEMENT_TRUE_FIELDS = (
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

STATEMENT_FALSE_FIELDS = (
    "prior_result_reentry_cycle_created",
    "second_operation_created",
    "continuation_created",
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
)

EXACT_TOP_LEVEL_BLOCKS = {
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "older_runtime_lineage_imported_as_authority": (
        "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY"
    ),
    "older_runtime_permission_treated_as_current": (
        "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT"
    ),
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
    "runtime_boundary_v0_failure_claimed_passed": (
        "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED"
    ),
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
    "RAW_STATE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "RAW_PRIOR_RESULT_REENTRY_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

FORBIDDEN_OUTPUT_ROOT_NAMES = {
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


class LocalRelevanceMediumReadOnlyRuntimeHeldReentryV0MinTests(unittest.TestCase):
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

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if isinstance(block, Mapping):
            code = block.get("code") or block.get("block_code")
            return str(code) if code is not None else None
        return None

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get(
            "local_relevance_medium_read_only_runtime_held_reentry_checks", []
        )
        if not isinstance(checks, list):
            return []
        return [check for check in checks if isinstance(check, Mapping)]

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is not True)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def held_reentry(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        held_reentry = result.get("local_relevance_medium_read_only_runtime_held_reentry", {})
        self.assertIsInstance(held_reentry, Mapping)
        return held_reentry

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get(
            "local_relevance_medium_read_only_runtime_held_reentry_statement", {}
        )
        self.assertIsInstance(statement, Mapping)
        return statement

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = resolver.build_local_relevance_medium_read_only_runtime_held_reentry_v0_min_summary(
            result
        )
        self.assertIsInstance(summary, Mapping)
        return summary

    def assert_same_or_stable_artifact_path(self, actual: Any, expected: Any) -> None:
        actual_path = Path(actual)
        expected_path = Path(expected)
        if actual_path.is_absolute() and expected_path.is_absolute():
            self.assertEqual(actual_path, expected_path)
            return
        if actual_path.exists() or expected_path.exists():
            self.assertEqual(actual_path.resolve(), expected_path.resolve())
            return
        self.assertTrue(str(actual).endswith(expected_path.name))

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(type(non_claims[key]), bool)
            self.assertIs(non_claims[key], False)
        for key in (
            "runtime_held_reentry_created",
            "runtime_held_reentry_local_only",
            "runtime_held_reentry_read_only",
            "held_reentry_basis_reference_only",
        ):
            self.assertNotIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
            self.assertNotIn(key, non_claims)

    def assert_runtime_held_reentry_non_claims(self, result: Mapping[str, Any]) -> None:
        held_reentry = self.held_reentry(result)
        for key in HELD_REENTRY_FALSE_FIELDS:
            self.assertIn(key, held_reentry)
            self.assertIs(held_reentry[key], False, key)
        for key in (
            "prior_result_reentry_cycle_created",
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
            "runtime_v0_failure_repaired",
            "runtime_v0_failure_hidden",
            "runtime_v0_failure_claimed_passed",
            "runtime_v2_failure_repaired",
            "runtime_v2_failure_hidden",
            "runtime_v2_failure_claimed_passed",
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
            "follow_on_work_authorized",
        ):
            self.assertIs(result["non_claims"][key], False, key)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_runtime_held_reentry_non_claims(result)

    def assert_held_reentry_separate_from_wrapper(
        self, result: Mapping[str, Any]
    ) -> None:
        held_reentry = self.held_reentry(result)
        for key in FORBIDDEN_HELD_REENTRY_WRAPPER_FIELDS:
            self.assertNotIn(key, held_reentry)

    def assert_recorded_held_reentry_posture(
        self, result: Mapping[str, Any], paths: Mapping[str, Path] | None = None
    ) -> None:
        held_reentry = self.held_reentry(result)
        self.assertEqual(
            held_reentry["held_reentry_id"],
            "local_relevance_medium_read_only_runtime_held_reentry_001",
        )
        self.assertEqual(held_reentry["held_reentry_type"], HELD_REENTRY_TYPE)
        self.assertEqual(held_reentry["held_reentry_version"], resolver.RESULT_VERSION)
        self.assertEqual(held_reentry["held_reentry_scope"], HELD_REENTRY_SCOPE)
        self.assertEqual(
            held_reentry["basis_runtime_held_reentry_boundary_outcome"],
            RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME,
        )
        self.assertEqual(
            held_reentry["basis_runtime_held_reentry_boundary_result_version"], "0.1.0"
        )
        self.assertEqual(
            held_reentry["basis_runtime_held_reentry_boundary_failed_check_count"], 0
        )
        self.assertEqual(
            held_reentry["basis_runtime_held_state_outcome"],
            RUNTIME_HELD_STATE_OUTCOME,
        )
        self.assertEqual(
            held_reentry["basis_runtime_held_state_result_version"], "0.1.0"
        )
        self.assertEqual(held_reentry["basis_runtime_held_state_failed_check_count"], 0)
        self.assertEqual(
            held_reentry["basis_runtime_held_state_boundary_outcome"],
            RUNTIME_HELD_STATE_BOUNDARY_OUTCOME,
        )
        self.assertEqual(
            held_reentry["basis_runtime_held_state_boundary_result_version"], "0.1.0"
        )
        self.assertEqual(
            held_reentry["basis_runtime_held_state_boundary_failed_check_count"], 0
        )
        self.assertEqual(held_reentry["basis_runtime_outcome"], RUNTIME_OUTCOME)
        self.assertEqual(held_reentry["basis_runtime_result_version"], "0.1.0")
        self.assertEqual(held_reentry["basis_runtime_failed_check_count"], 0)
        self.assertEqual(
            held_reentry["basis_runtime_boundary_outcome"], RUNTIME_BOUNDARY_OUTCOME
        )
        self.assertEqual(
            held_reentry["basis_runtime_boundary_result_version"], "0.1.0"
        )
        self.assertEqual(held_reentry["basis_runtime_boundary_failed_check_count"], 0)
        self.assertEqual(
            held_reentry["basis_runtime_permission_outcome"],
            RUNTIME_PERMISSION_OUTCOME,
        )
        self.assertEqual(
            held_reentry["basis_runtime_permission_result_version"], "0.1.0"
        )
        self.assertEqual(held_reentry["basis_runtime_permission_failed_check_count"], 0)
        self.assertEqual(
            held_reentry["basis_operation_execution_outcome"],
            OPERATION_EXECUTION_OUTCOME,
        )
        self.assertEqual(
            held_reentry["basis_operation_execution_result_version"], "0.1.0"
        )
        self.assertEqual(held_reentry["basis_operation_execution_failed_check_count"], 0)
        self.assertEqual(held_reentry["selected_command"], SELECTED_COMMAND)
        for key in HELD_REENTRY_TRUE_FIELDS:
            self.assertIn(key, held_reentry)
            self.assertIs(type(held_reentry[key]), bool)
            self.assertIs(held_reentry[key], True, key)
        for key in HELD_REENTRY_FALSE_FIELDS:
            self.assertIn(key, held_reentry)
            self.assertIs(type(held_reentry[key]), bool)
            self.assertIs(held_reentry[key], False, key)
        if paths is not None:
            self.assert_same_or_stable_artifact_path(
                held_reentry["basis_runtime_held_reentry_boundary_artifact"],
                paths["held_reentry_boundary"],
            )
            self.assert_same_or_stable_artifact_path(
                held_reentry["basis_runtime_held_state_artifact"], paths["held_state"]
            )
            self.assert_same_or_stable_artifact_path(
                held_reentry["basis_runtime_held_state_boundary_artifact"],
                paths["held_state_boundary"],
            )
            self.assert_same_or_stable_artifact_path(
                held_reentry["basis_runtime_artifact"], paths["runtime"]
            )
            self.assert_same_or_stable_artifact_path(
                held_reentry["basis_runtime_boundary_artifact"],
                paths["runtime_boundary"],
            )
            self.assert_same_or_stable_artifact_path(
                held_reentry["basis_runtime_permission_artifact"],
                paths["runtime_permission"],
            )
            self.assert_same_or_stable_artifact_path(
                held_reentry["basis_operation_execution_artifact"],
                paths["operation_execution"],
            )
        self.assert_held_reentry_separate_from_wrapper(result)

    def assert_statement_fields(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        for key in STATEMENT_TRUE_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
        for key in STATEMENT_FALSE_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], False, key)

    def assert_failure_lineage_preserved(self, result: Mapping[str, Any]) -> None:
        held_reentry = self.held_reentry(result)
        summary = self.summary(result)
        self.assertIs(held_reentry["runtime_v0_failure_evidence_preserved"], True)
        self.assertIs(held_reentry["runtime_v2_failure_evidence_preserved"], True)
        self.assertIs(held_reentry["runtime_boundary_v0_failure_evidence_preserved"], True)
        self.assertIs(summary["runtime_v0_failure_evidence_preserved"], True)
        self.assertIs(summary["runtime_v2_failure_evidence_preserved"], True)
        self.assertIs(summary["runtime_boundary_v0_failure_evidence_preserved"], True)
        self.assertIs(
            summary["runtime_v0_v2_boundary_v0_failure_not_repaired_hidden_claimed_passed"],
            True,
        )
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
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertIs(result["non_claims"][key], False, key)

    def assert_serialized_result_omits_sentinels(
        self, result: Mapping[str, Any]
    ) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_strings_preserved(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for official in (
            HELD_REENTRY_TYPE,
            HELD_REENTRY_SCOPE,
            SELECTED_COMMAND,
            result["outcome"],
            resolver.RESOLVER_MODULE,
        ):
            self.assertIn(official, serialized)
            self.assertNotIn(f"[REDACTED]{official}", serialized)

    def write_json(self, path: Path, value: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(value, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return path

    def wrap_artifact(
        self, outcome: str, object_key: str, object_value: Mapping[str, Any]
    ) -> dict[str, Any]:
        obj = copy.deepcopy(dict(object_value))
        return {
            "outcome": outcome,
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
            object_key: obj,
            f"{object_key}_statement": copy.deepcopy(obj),
            f"{object_key}_summary": copy.deepcopy(obj),
            f"{object_key}_checks": [{"check_name": "synthetic clean", "passed": True}],
        }

    def base_false_fields(self) -> dict[str, bool]:
        return {
            "raw_state_body_embedded": False,
            "state_mutation_performed": False,
            "state_update_performed": False,
            "runtime_held_reentry_created": False,
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
            "repeated_reception_permission_created": False,
            "arbitrary_reception_created": False,
            "feed_created": False,
            "source_transfer_occurred": False,
            "source_receipt_occurred": False,
            "source_created": False,
            "authority_created": False,
            "currentness_created": False,
            "truth_created": False,
            "synchronization_created": False,
            "participation_authorized": False,
            "participant_role_created": False,
            "deployment_created": False,
            "public_release_created": False,
            "broader_reusable_permission_created": False,
            "derivative_reception_authorized": False,
            "vessel_relation_authorized": False,
            "adoption_created": False,
            "receiving_context_governance_created": False,
            "publication_flow_created": False,
            "consumed_request_reopened": False,
            "authorization_token_reused": False,
            "follow_on_work_authorized": False,
        }

    def synthetic_artifact_payloads(self) -> dict[str, dict[str, Any]]:
        false_fields = self.base_false_fields()
        held_reentry_boundary = {
            **false_fields,
            "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY",
            "boundary_scope": "SELECTED_RUNTIME_HELD_REENTRY_CONSIDERATION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_runtime_held_reentry_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_held_reentry_boundary_recorded": True,
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
            "runtime_v0_failure_evidence_preserved": True,
            "runtime_v2_failure_evidence_preserved": True,
            "runtime_boundary_v0_failure_evidence_preserved": True,
        }
        held_state = {
            **held_reentry_boundary,
            "held_state_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE",
            "held_state_scope": "SELECTED_RUNTIME_HELD_STATE_ONLY",
            "local_relevance_medium_read_only_runtime_held_state_recorded": True,
            "runtime_held_reentry_created": False,
        }
        held_state_boundary = {
            **false_fields,
            "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY",
            "boundary_scope": "SELECTED_RUNTIME_HELD_STATE_CONSIDERATION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_runtime_held_state_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_held_state_boundary_recorded": True,
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
            "runtime_v0_failure_evidence_preserved": True,
            "runtime_v2_failure_evidence_preserved": True,
            "runtime_boundary_v0_failure_evidence_preserved": True,
        }
        runtime = {
            **false_fields,
            "runtime_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME",
            "runtime_scope": "SELECTED_RUNTIME_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_runtime_recorded": True,
            "local_relevance_medium_read_only_runtime_recorded": True,
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
            "runtime_v0_failure_evidence_preserved": True,
            "runtime_v2_failure_evidence_preserved": True,
            "runtime_boundary_v0_failure_evidence_preserved": True,
        }
        runtime_boundary = {
            **false_fields,
            "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
            "boundary_scope": "SELECTED_RUNTIME_CONSIDERATION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_runtime_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_boundary_recorded": True,
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
            "runtime_boundary_v0_failure_evidence_preserved": True,
        }
        runtime_permission = {
            **false_fields,
            "runtime_permission_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
            "runtime_permission_scope": "SELECTED_RUNTIME_PERMISSION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_runtime_permission_recorded": True,
            "local_relevance_medium_read_only_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
        }
        operation_execution = {
            **false_fields,
            "operation_execution_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
            "operation_execution_scope": "SELECTED_OPERATION_EXECUTION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_operation_execution_recorded": True,
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
        }
        return {
            "held_reentry_boundary": self.wrap_artifact(
                RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME,
                ARTIFACT_OBJECT_KEYS["held_reentry_boundary"],
                held_reentry_boundary,
            ),
            "held_state": self.wrap_artifact(
                RUNTIME_HELD_STATE_OUTCOME,
                ARTIFACT_OBJECT_KEYS["held_state"],
                held_state,
            ),
            "held_state_boundary": self.wrap_artifact(
                RUNTIME_HELD_STATE_BOUNDARY_OUTCOME,
                ARTIFACT_OBJECT_KEYS["held_state_boundary"],
                held_state_boundary,
            ),
            "runtime": self.wrap_artifact(
                RUNTIME_OUTCOME,
                ARTIFACT_OBJECT_KEYS["runtime"],
                runtime,
            ),
            "runtime_boundary": self.wrap_artifact(
                RUNTIME_BOUNDARY_OUTCOME,
                ARTIFACT_OBJECT_KEYS["runtime_boundary"],
                runtime_boundary,
            ),
            "runtime_permission": self.wrap_artifact(
                RUNTIME_PERMISSION_OUTCOME,
                ARTIFACT_OBJECT_KEYS["runtime_permission"],
                runtime_permission,
            ),
            "operation_execution": self.wrap_artifact(
                OPERATION_EXECUTION_OUTCOME,
                ARTIFACT_OBJECT_KEYS["operation_execution"],
                operation_execution,
            ),
        }

    def set_wrapped_field(
        self, artifact: dict[str, Any], object_key: str, field: str, value: Any
    ) -> None:
        for key in (object_key, f"{object_key}_statement", f"{object_key}_summary"):
            if isinstance(artifact.get(key), dict):
                artifact[key][field] = value

    def write_synthetic_artifacts(
        self,
        root: Path,
        mutator: Callable[[dict[str, dict[str, Any]]], None] | None = None,
    ) -> tuple[dict[str, Path], dict[str, dict[str, Any]]]:
        artifacts = self.synthetic_artifact_payloads()
        if mutator is not None:
            mutator(artifacts)
        paths = {
            "held_reentry_boundary": root / "runtime_held_reentry_boundary.json",
            "held_state": root / "runtime_held_state.json",
            "held_state_boundary": root / "runtime_held_state_boundary.json",
            "runtime": root / "runtime_v3.json",
            "runtime_boundary": root / "runtime_boundary_v2.json",
            "runtime_permission": root / "runtime_permission.json",
            "operation_execution": root / "operation_execution.json",
        }
        for key, path in paths.items():
            self.write_json(path, artifacts[key])
        return paths, artifacts

    def build_request_for_paths(self, paths: Mapping[str, Path]) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_runtime_held_reentry_v0_min_request(
            local_relevance_medium_read_only_runtime_held_reentry_id=(
                "local_relevance_medium_read_only_runtime_held_reentry_001"
            ),
            selected_runtime_held_reentry_boundary_artifact=paths[
                "held_reentry_boundary"
            ],
            selected_runtime_held_state_artifact=paths["held_state"],
            selected_runtime_held_state_boundary_artifact=paths["held_state_boundary"],
            selected_runtime_artifact=paths["runtime"],
            selected_runtime_boundary_artifact=paths["runtime_boundary"],
            selected_runtime_permission_artifact=paths["runtime_permission"],
            selected_operation_execution_artifact=paths["operation_execution"],
            selected_command=SELECTED_COMMAND,
            held_reentry_type=HELD_REENTRY_TYPE,
            held_reentry_scope=HELD_REENTRY_SCOPE,
        )

    def build_valid_synthetic_request(
        self,
        root: Path,
        mutator: Callable[[dict[str, dict[str, Any]]], None] | None = None,
    ) -> tuple[dict[str, Any], dict[str, Path], dict[str, dict[str, Any]]]:
        paths, artifacts = self.write_synthetic_artifacts(root, mutator)
        return self.build_request_for_paths(paths), paths, artifacts

    def resolve_valid_synthetic(self, root: Path) -> dict[str, Any]:
        request, _, _ = self.build_valid_synthetic_request(root)
        return resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
            request
        )

    def make_request_with_artifact_mutation(
        self,
        root: Path,
        artifact_key: str,
        mutator: Callable[[dict[str, Any]], None],
    ) -> dict[str, Any]:
        def all_artifacts_mutator(artifacts: dict[str, dict[str, Any]]) -> None:
            mutator(artifacts[artifact_key])

        request, _, _ = self.build_valid_synthetic_request(root, all_artifacts_mutator)
        return request

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min",
            "resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min_from_path",
            "write_local_relevance_medium_read_only_runtime_held_reentry_v0_min_result",
            "build_local_relevance_medium_read_only_runtime_held_reentry_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_runtime_held_reentry_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_HELD_REENTRY_TYPE_VALUES",
            "SUPPORTED_HELD_REENTRY_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min",
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_v0_min"
            )
        )
        self.assertIn(HELD_REENTRY_TYPE, resolver.SUPPORTED_HELD_REENTRY_TYPE_VALUES)
        self.assertIn(HELD_REENTRY_SCOPE, resolver.SUPPORTED_HELD_REENTRY_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, SELECTED_COMMAND)
        for key in (
            "prior_result_reentry_cycle_created",
            "second_operation_created",
            "continuation_created",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "runtime_v0_failure_repaired",
            "runtime_v2_failure_repaired",
            "runtime_boundary_v0_failure_repaired",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in (
            "runtime_held_reentry_created",
            "runtime_held_reentry_local_only",
            "runtime_held_reentry_read_only",
            "held_reentry_basis_reference_only",
        ):
            self.assertNotIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for code in (
            "PRIOR_RESULT_REENTRY_CYCLE_CREATED",
            "SECOND_OPERATION_CREATED",
            "CONTINUATION_CREATED",
            "RAW_STATE_BODY_EMBEDDED",
            "STATE_MUTATION_PERFORMED",
            "STATE_UPDATE_PERFORMED",
            "RUNTIME_HOSTING_CREATED",
            "RUNTIME_LOOP_CREATED",
            "DAEMON_BEHAVIOR_CREATED",
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "RUNTIME_AUTHORITY_IMPORTED",
            "RUNTIME_V0_FAILURE_REPAIRED",
            "RUNTIME_V2_FAILURE_REPAIRED",
            "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        request = resolver.build_declared_local_relevance_medium_read_only_runtime_held_reentry_v0_min_request()
        self.assertTrue(
            request["selected_runtime_held_reentry_boundary_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_held_reentry_boundary_reference_review_001__local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min_result.json"
            )
        )
        self.assertTrue(
            request["selected_runtime_held_state_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_held_state_reference_review_001__local_relevance_medium_read_only_runtime_held_state_v0_min_result.json"
            )
        )
        self.assertTrue(
            request["selected_runtime_held_state_boundary_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_held_state_boundary_reference_review_001__local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result.json"
            )
        )
        self.assertTrue(
            request["selected_runtime_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_reference_review_001__local_relevance_medium_read_only_runtime_v0_min_v3_result.json"
            )
        )
        self.assertTrue(
            request["selected_runtime_boundary_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_boundary_reference_review_001__local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
            )
        )
        self.assertTrue(
            request["selected_runtime_permission_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_permission_reference_review_001__local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
            )
        )
        self.assertTrue(
            request["selected_operation_execution_artifact"].endswith(
                "local_relevance_medium_read_only_operation_execution_reference_review_001__local_relevance_medium_read_only_operation_execution_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        for key in (
            "prior_result_reentry_cycle_created",
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
        ):
            self.assertIs(request["declared_non_claims"][key], False)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            request, paths, _ = self.build_valid_synthetic_request(Path(tmp_dir))
            result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                request
            )
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        summary = self.summary(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            summary["held_reentry_id"],
            "local_relevance_medium_read_only_runtime_held_reentry_001",
        )
        for key in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(key, result)
        self.assert_recorded_held_reentry_posture(result, paths)
        self.assert_statement_fields(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_failure_lineage_preserved(result)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        missing = [path for path in DEFAULT_ARTIFACT_PATHS.values() if not path.exists()]
        if missing:
            self.skipTest(f"default live artifacts absent: {missing[0]}")
        request = resolver.build_declared_local_relevance_medium_read_only_runtime_held_reentry_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
            request
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        held_reentry = self.held_reentry(result)
        self.assertEqual(held_reentry["selected_command"], SELECTED_COMMAND)
        self.assertEqual(held_reentry["held_reentry_type"], HELD_REENTRY_TYPE)
        self.assertEqual(held_reentry["held_reentry_scope"], HELD_REENTRY_SCOPE)
        for key in HELD_REENTRY_TRUE_FIELDS:
            self.assertIs(held_reentry[key], True, key)
        for key in HELD_REENTRY_FALSE_FIELDS:
            self.assertIs(held_reentry[key], False, key)
        self.assert_statement_fields(result)
        self.assert_failure_lineage_preserved(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_same_or_stable_artifact_path(
            held_reentry["basis_runtime_held_reentry_boundary_artifact"],
            DEFAULT_ARTIFACT_PATHS["selected_runtime_held_reentry_boundary_artifact"],
        )
        self.assert_same_or_stable_artifact_path(
            held_reentry["basis_runtime_held_state_artifact"],
            DEFAULT_ARTIFACT_PATHS["selected_runtime_held_state_artifact"],
        )
        self.assert_same_or_stable_artifact_path(
            held_reentry["basis_runtime_held_state_boundary_artifact"],
            DEFAULT_ARTIFACT_PATHS["selected_runtime_held_state_boundary_artifact"],
        )
        self.assert_same_or_stable_artifact_path(
            held_reentry["basis_runtime_artifact"],
            DEFAULT_ARTIFACT_PATHS["selected_runtime_artifact"],
        )
        self.assert_same_or_stable_artifact_path(
            held_reentry["basis_runtime_boundary_artifact"],
            DEFAULT_ARTIFACT_PATHS["selected_runtime_boundary_artifact"],
        )
        self.assert_same_or_stable_artifact_path(
            held_reentry["basis_runtime_permission_artifact"],
            DEFAULT_ARTIFACT_PATHS["selected_runtime_permission_artifact"],
        )
        self.assert_same_or_stable_artifact_path(
            held_reentry["basis_operation_execution_artifact"],
            DEFAULT_ARTIFACT_PATHS["selected_operation_execution_artifact"],
        )

    def test_top_level_and_declared_non_claim_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            base_root = Path(tmp_dir)
            for index, (key, expected_code) in enumerate(EXACT_TOP_LEVEL_BLOCKS.items()):
                with self.subTest(top_level=key):
                    request, _, _ = self.build_valid_synthetic_request(
                        base_root / f"top_{index}"
                    )
                    request[key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assertIs(result["non_claims"][key], False)
            for index, key in enumerate(EXACT_TOP_LEVEL_BLOCKS):
                with self.subTest(declared_flipped=key):
                    request, _, _ = self.build_valid_synthetic_request(
                        base_root / f"declared_flipped_{index}"
                    )
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                with self.subTest(declared_missing=key):
                    request, _, _ = self.build_valid_synthetic_request(
                        base_root / f"declared_missing_{index}"
                    )
                    request["declared_non_claims"].pop(key)
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                with self.subTest(declared_non_bool=key):
                    request, _, _ = self.build_valid_synthetic_request(
                        base_root / f"declared_non_bool_{index}"
                    )
                    request["declared_non_claims"][key] = "false"
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            for index, key in enumerate(resolver.REQUIRED_FALSE_NON_CLAIMS):
                with self.subTest(key=key):
                    request, _, _ = self.build_valid_synthetic_request(root / f"case_{index}")
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_runtime_held_reentry_non_claims(result)

    def test_representative_blocking_behavior(self) -> None:
        cases: list[tuple[str, Callable[[dict[str, Any], Path], dict[str, Any]]]] = [
            (
                "explicit block intent",
                lambda request, _root: {
                    **request,
                    "local_relevance_medium_read_only_runtime_held_reentry_intent": (
                        "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY"
                    ),
                },
            ),
            (
                "unsupported intent",
                lambda request, _root: {
                    **request,
                    "local_relevance_medium_read_only_runtime_held_reentry_intent": "UNSUPPORTED",
                },
            ),
            (
                "runtime-held-re-entry boundary artifact path missing",
                lambda request, _root: {
                    **request,
                    "selected_runtime_held_reentry_boundary_artifact": "",
                },
            ),
            (
                "runtime-held-state artifact path missing",
                lambda request, _root: {**request, "selected_runtime_held_state_artifact": ""},
            ),
            (
                "runtime-held-state boundary artifact path missing",
                lambda request, _root: {
                    **request,
                    "selected_runtime_held_state_boundary_artifact": "",
                },
            ),
            (
                "runtime artifact path missing",
                lambda request, _root: {**request, "selected_runtime_artifact": ""},
            ),
            (
                "runtime boundary artifact path missing",
                lambda request, _root: {**request, "selected_runtime_boundary_artifact": ""},
            ),
            (
                "runtime permission artifact path missing",
                lambda request, _root: {**request, "selected_runtime_permission_artifact": ""},
            ),
            (
                "operation execution artifact path missing",
                lambda request, _root: {**request, "selected_operation_execution_artifact": ""},
            ),
            ("selected command missing", lambda request, _root: {**request, "selected_command": ""}),
            (
                "selected command not state",
                lambda request, _root: {**request, "selected_command": "lookup"},
            ),
            (
                "held re-entry type missing",
                lambda request, _root: {
                    key: value for key, value in request.items() if key != "held_reentry_type"
                },
            ),
            (
                "held re-entry type wrong",
                lambda request, _root: {
                    **request,
                    "held_reentry_type": "LOCAL_RELEVANCE_MEDIUM_RUNTIME_HOSTING",
                },
            ),
            (
                "held re-entry scope missing",
                lambda request, _root: {
                    key: value for key, value in request.items() if key != "held_reentry_scope"
                },
            ),
            (
                "held re-entry scope wrong",
                lambda request, _root: {
                    **request,
                    "held_reentry_scope": "SELECTED_RUNTIME_LOOP_ONLY",
                },
            ),
        ]
        shortcut_cases = (
            "runtime_held_reentry_boundary_artifact_missing",
            "runtime_held_reentry_boundary_artifact_not_recorded",
            "runtime_held_reentry_boundary_artifact_failed_checks_present",
            "runtime_held_reentry_boundary_artifact_version_not_0_1_0",
            "runtime_held_state_artifact_missing",
            "runtime_held_state_artifact_not_recorded",
            "runtime_held_state_artifact_failed_checks_present",
            "runtime_held_state_artifact_version_not_0_1_0",
            "runtime_held_state_boundary_artifact_missing",
            "runtime_held_state_boundary_artifact_not_recorded",
            "runtime_held_state_boundary_artifact_failed_checks_present",
            "runtime_held_state_boundary_artifact_version_not_0_1_0",
            "runtime_artifact_missing",
            "runtime_artifact_not_recorded",
            "runtime_artifact_failed_checks_present",
            "runtime_artifact_version_not_0_1_0",
            "runtime_boundary_artifact_missing",
            "runtime_boundary_artifact_not_recorded",
            "runtime_boundary_artifact_failed_checks_present",
            "runtime_boundary_artifact_version_not_0_1_0",
            "runtime_permission_artifact_missing",
            "runtime_permission_artifact_not_recorded",
            "runtime_permission_artifact_failed_checks_present",
            "runtime_permission_artifact_version_not_0_1_0",
            "operation_execution_artifact_missing",
            "operation_execution_artifact_not_recorded",
            "operation_execution_artifact_failed_checks_present",
            "operation_execution_artifact_version_not_0_1_0",
            "selected_runtime_held_reentry_boundary_not_recorded",
            "future_runtime_held_reentry_may_not_be_considered",
            "selected_runtime_held_state_not_recorded",
            "runtime_held_state_not_created",
            "runtime_held_state_local_only_not_true",
            "runtime_held_state_read_only_not_true",
            "held_state_basis_reference_only_not_true",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "selected_runtime_held_state_boundary_not_recorded",
            "future_runtime_held_state_may_not_be_considered",
            "selected_runtime_not_recorded",
            "runtime_not_created",
            "runtime_local_only_not_true",
            "runtime_read_only_not_true",
            "selected_runtime_boundary_not_recorded",
            "future_runtime_may_not_be_considered",
            "selected_runtime_permission_not_recorded",
            "runtime_permission_not_created",
            "runtime_permission_local_only_not_true",
            "runtime_permission_read_only_not_true",
            "selected_operation_execution_not_recorded",
            "operation_execution_not_created",
            "operation_execution_not_performed",
            "operation_execution_local_only_not_true",
            "operation_execution_read_only_not_true",
            "local_relevance_medium_read_only_runtime_held_reentry_not_recorded",
            "runtime_held_reentry_not_created",
            "runtime_held_reentry_local_only_not_true",
            "runtime_held_reentry_read_only_not_true",
            "held_reentry_basis_reference_only_not_true",
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
            "runtime_v0_failure_repaired",
            "runtime_v0_failure_hidden",
            "runtime_v0_failure_claimed_passed",
            "runtime_v2_failure_repaired",
            "runtime_v2_failure_hidden",
            "runtime_v2_failure_claimed_passed",
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
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
            "consumed_request_reopened",
            "authorization_token_reused",
            "artifact_existence_treated_as_runtime_held_reentry_authority",
            "latest_file_posture_treated_as_runtime_held_reentry_authority",
            "repo_local_availability_treated_as_runtime_held_reentry_authority",
            "hidden_repo_state_used_as_runtime_held_reentry_content",
            "hidden_repo_state_used_as_runtime_held_reentry_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
        for field in shortcut_cases:
            cases.append((field, lambda request, _root, field=field: {**request, field: True}))
        cases.extend(
            [
                (
                    "required non-claim missing",
                    lambda request, _root: {
                        **request,
                        "declared_non_claims": {
                            key: value
                            for key, value in request["declared_non_claims"].items()
                            if key != "prior_result_reentry_cycle_created"
                        },
                    },
                ),
                (
                    "required non-claim flipped",
                    lambda request, _root: {
                        **request,
                        "declared_non_claims": {
                            **request["declared_non_claims"],
                            "prior_result_reentry_cycle_created": True,
                        },
                    },
                ),
            ]
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            for malformed_request in (None, ["not", "mapping"]):
                result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                    malformed_request  # type: ignore[arg-type]
                )
                self.assert_blocked_with_public_code(result)
            for index, (name, mutate_request) in enumerate(cases):
                with self.subTest(name=name):
                    case_root = root / self.safe_json_filename(name, index).removesuffix(
                        ".json"
                    )
                    request, _, _ = self.build_valid_synthetic_request(case_root)
                    mutated_request = mutate_request(copy.deepcopy(request), case_root)
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                        mutated_request
                    )
                    self.assert_blocked_with_public_code(result)

            artifact_cases = []
            for artifact_key in ARTIFACT_OBJECT_KEYS:
                artifact_cases.extend(
                    (
                        (artifact_key, "outcome", f"{ARTIFACT_OUTCOMES[artifact_key]}_BAD"),
                        (artifact_key, "failed_check_count", 1),
                        (artifact_key, "result_version", "9.9.9"),
                    )
                )
            for index, (artifact_key, key, value) in enumerate(artifact_cases):
                with self.subTest(artifact=artifact_key, key=key):
                    request = self.make_request_with_artifact_mutation(
                        root / f"artifact_{index}",
                        artifact_key,
                        lambda artifact, key=key, value=value: artifact.__setitem__(
                            key, value
                        ),
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)

            posture_cases = (
                ("held_reentry_boundary", "selected_runtime_held_reentry_boundary_recorded", False),
                ("held_reentry_boundary", "future_runtime_held_reentry_may_be_considered", False),
                ("held_state", "runtime_held_state_created", False),
                ("held_state", "held_state_basis_reference_only", False),
                ("held_state", "raw_state_body_embedded", True),
                ("held_state_boundary", "future_runtime_held_state_may_be_considered", False),
                ("runtime", "runtime_created", False),
                ("runtime", "runtime_read_only", False),
                ("runtime_boundary", "future_runtime_may_be_considered", False),
                ("runtime_permission", "runtime_permission_created", False),
                ("operation_execution", "operation_execution_performed", False),
            )
            for index, (artifact_key, field, value) in enumerate(posture_cases):
                with self.subTest(artifact=artifact_key, posture=field):
                    object_key = ARTIFACT_OBJECT_KEYS[artifact_key]
                    request = self.make_request_with_artifact_mutation(
                        root / f"posture_{index}",
                        artifact_key,
                        lambda artifact, object_key=object_key, field=field, value=value: (
                            self.set_wrapped_field(artifact, object_key, field, value)
                        ),
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)

            for index, request_key in enumerate(ARTIFACT_REQUEST_KEYS.values()):
                with self.subTest(unreadable_artifact=request_key):
                    request, _, _ = self.build_valid_synthetic_request(
                        root / f"unreadable_{index}"
                    )
                    request[request_key] = str(
                        root / self.safe_json_filename(f"absent_{request_key}", index)
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)

            for index, request_key in enumerate(ARTIFACT_REQUEST_KEYS.values()):
                with self.subTest(json_array_artifact=request_key):
                    request, _, _ = self.build_valid_synthetic_request(
                        root / f"array_{index}"
                    )
                    array_path = root / self.safe_json_filename(request_key, index)
                    self.write_json(array_path, [])
                    request[request_key] = str(array_path)
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            result = self.resolve_valid_synthetic(Path(tmp_dir))
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        held_reentry = self.held_reentry(result)
        self.assertEqual(held_reentry["held_reentry_type"], HELD_REENTRY_TYPE)
        self.assertEqual(held_reentry["held_reentry_scope"], HELD_REENTRY_SCOPE)
        self.assertEqual(held_reentry["selected_command"], SELECTED_COMMAND)
        for outcome in (
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_NOT_RECORDED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_BLOCKED,
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        self.assert_official_strings_preserved(result)

    def test_raw_hidden_older_runtime_hostile_content_containment(self) -> None:
        def inject_sentinels(artifacts: dict[str, dict[str, Any]]) -> None:
            sensitive_keys = {
                "held_reentry_boundary": "raw_runtime_held_reentry_boundary_body",
                "held_state": "raw_runtime_held_state_body",
                "held_state_boundary": "raw_runtime_held_state_boundary_body",
                "runtime": "raw_runtime_body",
                "runtime_boundary": "raw_runtime_boundary_body",
                "runtime_permission": "raw_runtime_permission_body",
                "operation_execution": "raw_operation_execution_body",
            }
            for index, (artifact_key, sensitive_key) in enumerate(sensitive_keys.items()):
                artifacts[artifact_key][sensitive_key] = HOSTILE_SENTINELS[index]
                object_key = ARTIFACT_OBJECT_KEYS[artifact_key]
                artifacts[artifact_key][object_key][sensitive_key] = HOSTILE_SENTINELS[
                    index + 1
                ]

        with tempfile.TemporaryDirectory() as tmp_dir:
            request, _, artifacts = self.build_valid_synthetic_request(
                Path(tmp_dir), inject_sentinels
            )
            original_request = copy.deepcopy(request)
            original_artifacts = copy.deepcopy(artifacts)
            injected = {
                "raw_runtime_held_reentry_body": HOSTILE_SENTINELS[0],
                "raw_runtime_held_reentry_boundary_body": HOSTILE_SENTINELS[1],
                "raw_runtime_held_state_body": HOSTILE_SENTINELS[2],
                "raw_prior_result_reentry_body": HOSTILE_SENTINELS[14],
                "raw_second_operation_body": HOSTILE_SENTINELS[13],
                "raw_runtime_hosting_body": HOSTILE_SENTINELS[9],
                "hidden_repo_state": HOSTILE_SENTINELS[-1],
                "older_runtime_authority_probe": HOSTILE_SENTINELS[-2],
            }
            request.update(injected)
            result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                request
            )
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        if result["outcome"] == resolver.OUTCOME_BLOCKED:
            self.assert_blocked_with_public_code(result)
        else:
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.failed_check_count(result), 0)
        self.assert_serialized_result_omits_sentinels(result)
        self.assert_official_strings_preserved(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_runtime_held_reentry_non_claims(result)
        self.assertEqual(request, {**original_request, **injected})
        self.assertEqual(artifacts, original_artifacts)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            request, _, _ = self.build_valid_synthetic_request(root / "basis")
            request_path = self.write_json(root / "request.json", request)
            result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.summary(result)["result_version"], "0.1.0")
            self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_with_public_code(malformed)
            array_path = self.write_json(root / "array_request.json", [])
            array_result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min_from_path(
                array_path
            )
            self.assert_blocked_with_public_code(array_result)
            missing_result = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min_from_path(
                root / "missing_request.json"
            )
            self.assert_blocked_with_public_code(missing_result)

            output_root = (
                root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_v0_min"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                output_path = resolver.write_local_relevance_medium_read_only_runtime_held_reentry_v0_min_result(
                    result
                )
                output_path_second = resolver.write_local_relevance_medium_read_only_runtime_held_reentry_v0_min_result(
                    result
                )
            self.assertTrue(output_path.exists())
            self.assertTrue(output_path_second.exists())
            self.assertNotEqual(output_path, output_path_second)
            self.assertTrue(output_path.parent.exists())
            self.assertEqual(
                json.loads(output_path.read_text(encoding="utf-8"))["outcome"],
                resolver.OUTCOME_RECORDED,
            )
            self.assertIn(
                "local_relevance_medium_read_only_runtime_held_reentry_v0_min",
                output_path.as_posix(),
            )
            for forbidden_root_name in FORBIDDEN_OUTPUT_ROOT_NAMES:
                self.assertNotIn(forbidden_root_name, output_path.parts)
                self.assertNotIn(forbidden_root_name, output_path_second.parts)

    def test_non_mutation(self) -> None:
        def inject_nested_payloads(artifacts: dict[str, dict[str, Any]]) -> None:
            artifacts["held_reentry_boundary"]["raw_runtime_held_reentry_boundary_body"] = (
                HOSTILE_SENTINELS[1]
            )
            artifacts["held_state"]["raw_runtime_held_state_body"] = HOSTILE_SENTINELS[2]
            artifacts["runtime"]["raw_runtime_body"] = HOSTILE_SENTINELS[4]

        with tempfile.TemporaryDirectory() as tmp_dir:
            request, paths, artifacts = self.build_valid_synthetic_request(
                Path(tmp_dir), inject_nested_payloads
            )
            request["raw_runtime_loop_body"] = HOSTILE_SENTINELS[10]
            original_request = copy.deepcopy(request)
            original_declared_non_claims = copy.deepcopy(request["declared_non_claims"])
            original_paths = copy.deepcopy(paths)
            original_artifacts = copy.deepcopy(artifacts)
            resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                request
            )
        self.assertEqual(request, original_request)
        self.assertEqual(request["declared_non_claims"], original_declared_non_claims)
        self.assertEqual(paths, original_paths)
        self.assertEqual(artifacts, original_artifacts)
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        self.assertEqual(request["held_reentry_type"], HELD_REENTRY_TYPE)
        self.assertEqual(request["held_reentry_scope"], HELD_REENTRY_SCOPE)
        for key in EXACT_TOP_LEVEL_BLOCKS:
            self.assertIn(key, request)

    def test_failure_lineage_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            result = self.resolve_valid_synthetic(Path(tmp_dir))
        self.assert_failure_lineage_preserved(result)
        for key, expected_code in (
            ("runtime_v0_failure_repaired", "RUNTIME_V0_FAILURE_REPAIRED"),
            ("runtime_v0_failure_hidden", "RUNTIME_V0_FAILURE_HIDDEN"),
            ("runtime_v0_failure_claimed_passed", "RUNTIME_V0_FAILURE_CLAIMED_PASSED"),
            ("runtime_v2_failure_repaired", "RUNTIME_V2_FAILURE_REPAIRED"),
            ("runtime_v2_failure_hidden", "RUNTIME_V2_FAILURE_HIDDEN"),
            ("runtime_v2_failure_claimed_passed", "RUNTIME_V2_FAILURE_CLAIMED_PASSED"),
            ("runtime_boundary_v0_failure_repaired", "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED"),
            ("runtime_boundary_v0_failure_hidden", "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN"),
            (
                "runtime_boundary_v0_failure_claimed_passed",
                "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
            ),
        ):
            with self.subTest(key=key):
                with tempfile.TemporaryDirectory() as tmp_dir:
                    request, _, _ = self.build_valid_synthetic_request(Path(tmp_dir))
                    request[key] = True
                    blocked = resolver.resolve_local_relevance_medium_read_only_runtime_held_reentry_v0_min(
                        request
                    )
                self.assert_blocked_with_public_code(blocked)
                self.assertEqual(self.block_code(blocked), expected_code)
                self.assertIs(blocked["non_claims"][key], False)

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            result = self.resolve_valid_synthetic(Path(tmp_dir))
        summary = self.summary(result)
        statement = self.statement(result)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(statement["result_level_non_claims_canonical_false"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["older_runtime_lineage_not_imported_as_authority"], True)
        self.assertIs(summary["older_runtime_permission_not_treated_as_current"], True)
        self.assertIs(summary["runtime_authority_not_imported"], True)
        self.assertIs(summary["raw_state_body_embedded_false_posture"], True)
        self.assertIs(summary["state_mutation_performed_false_posture"], True)
        self.assertIs(summary["state_update_performed_false_posture"], True)
        self.assertIs(summary["prior_result_reentry_cycle_not_created"], True)
        self.assertIs(summary["second_operation_not_created"], True)
        self.assertIs(summary["continuation_not_created"], True)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)


if __name__ == "__main__":
    unittest.main()
