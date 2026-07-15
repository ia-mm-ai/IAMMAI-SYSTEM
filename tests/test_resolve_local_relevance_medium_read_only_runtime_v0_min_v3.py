"""Tests for the local read-only selected-state runtime v3 successor.

This suite treats v3 as additive successor evidence. It preserves the runtime
v0 default-live-artifact extraction mismatch, the runtime v2 write-helper
missing-file-handle failure, and the runtime-boundary v0 selected-operation-
execution recorded-alias ambiguity as failed lineage.

The suite verifies that v3 records one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME
object only. It does not create runtime hosting, runtime loop, daemon behavior,
continuation, runtime-held state, runtime-held re-entry, second operation,
prior-result re-entry, public API, participant-facing interface, distributed
network behavior, older-runtime authority import, or follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_read_only_runtime_v0_min_v3 as resolver  # noqa: E402


RUNTIME_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME"
RUNTIME_SCOPE = "SELECTED_RUNTIME_ONLY"
SELECTED_COMMAND = "state"
RUNTIME_BOUNDARY_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED"
RUNTIME_PERMISSION_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED"
)
OPERATION_EXECUTION_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED"
)

DEFAULT_RUNTIME_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_boundary_v0_min_v2/"
    "local_relevance_medium_read_only_runtime_boundary_reference_review_001__"
    "local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
)
DEFAULT_RUNTIME_PERMISSION_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_permission_v0_min/"
    "local_relevance_medium_read_only_runtime_permission_reference_review_001__"
    "local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
)
DEFAULT_OPERATION_EXECUTION_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_execution_v0_min/"
    "local_relevance_medium_read_only_operation_execution_reference_review_001__"
    "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_runtime_metadata",
    "declared_local_relevance_medium_read_only_runtime_question",
    "selected_runtime_boundary_artifact_basis",
    "selected_runtime_permission_artifact_basis",
    "selected_operation_execution_artifact_basis",
    "local_relevance_medium_read_only_runtime",
    "local_relevance_medium_read_only_runtime_checks",
    "local_relevance_medium_read_only_runtime_statement",
    "local_relevance_medium_read_only_runtime_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_summary",
)

FORBIDDEN_RUNTIME_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_checks",
    "non_claims",
    "local_relevance_medium_read_only_runtime_summary",
    "local_relevance_medium_read_only_runtime_metadata",
)

RUNTIME_FALSE_FIELDS = (
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "continuation_created",
    "runtime_held_state_created",
    "runtime_held_reentry_created",
    "second_operation_created",
    "prior_result_reentry_cycle_created",
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

STATEMENT_TRUE_FIELDS = (
    "local_relevance_medium_read_only_runtime_recorded",
    "basis_runtime_boundary_artifact_preserved",
    "basis_runtime_permission_artifact_preserved",
    "basis_operation_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
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
    "runtime_created",
    "runtime_local_only",
    "runtime_read_only",
    "runtime_v0_runtime_permission_created_default_artifact_extraction_mismatch_preserved",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_write_helper_missing_file_handle_failure_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

RUNTIME_PERMISSION_LAYERS = (
    "local_relevance_medium_read_only_runtime_permission",
    "local_relevance_medium_read_only_runtime_permission_statement",
    "local_relevance_medium_read_only_runtime_permission_summary",
)

HOSTILE_SENTINELS = (
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_STATE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "RAW_PRIOR_RESULT_REENTRY_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_v0_min_v2"
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
        "runtime_permission_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "operation_execution_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
)


class LocalRelevanceMediumReadOnlyRuntimeV3Tests(unittest.TestCase):
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
        with path.open("w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get("local_relevance_medium_read_only_runtime_checks")
        self.assertIsInstance(checks, list)
        return checks

    def runtime(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        runtime = result.get("local_relevance_medium_read_only_runtime")
        self.assertIsInstance(runtime, dict)
        return runtime

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get("local_relevance_medium_read_only_runtime_statement")
        self.assertIsInstance(statement, dict)
        return statement

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get("local_relevance_medium_read_only_runtime_summary")
        self.assertIsInstance(summary, dict)
        return summary

    def non_claims(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        return non_claims

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
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
        non_claims = self.non_claims(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)
        self.assertNotIn("runtime_created", non_claims)
        self.assertNotIn("runtime_local_only", non_claims)
        self.assertNotIn("runtime_read_only", non_claims)

    def assert_runtime_non_claims(self, result: Mapping[str, Any]) -> None:
        runtime = self.runtime(result)
        for field in RUNTIME_FALSE_FIELDS:
            self.assertIn(field, runtime)
            self.assertIs(runtime[field], False, field)
        non_claims = self.non_claims(result)
        for key in (
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertIs(non_claims[key], False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_runtime_non_claims(result)

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

    def assert_runtime_object_not_wrapper(self, result: Mapping[str, Any]) -> None:
        runtime = self.runtime(result)
        for field in FORBIDDEN_RUNTIME_WRAPPER_FIELDS:
            self.assertNotIn(field, runtime)

    def assert_lineage_preserved(self, result: Mapping[str, Any]) -> None:
        runtime = self.runtime(result)
        statement = self.statement(result)
        summary = self.summary(result)
        non_meaning = result.get("local_relevance_medium_read_only_runtime_non_meaning")
        self.assertIsInstance(non_meaning, dict)
        self.assertIs(
            statement[
                "runtime_v0_runtime_permission_created_default_artifact_extraction_mismatch_preserved"
            ],
            True,
        )
        self.assertIs(statement["runtime_v0_failure_evidence_preserved"], True)
        self.assertIs(
            statement["runtime_v2_write_helper_missing_file_handle_failure_preserved"],
            True,
        )
        self.assertIs(statement["runtime_v2_failure_evidence_preserved"], True)
        self.assertEqual(
            statement["successor_of_resolver_module"],
            "resolve_local_relevance_medium_read_only_runtime_v0_min_v2",
        )
        self.assertIs(
            runtime[
                "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved"
            ],
            True,
        )
        self.assertIs(runtime["runtime_boundary_v0_failure_evidence_preserved"], True)
        self.assertIs(statement["runtime_boundary_v0_failure_evidence_preserved"], True)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(non_meaning["not_runtime_v0_repair"], True)
        self.assertIs(non_meaning["not_runtime_v0_hide"], True)
        self.assertIs(non_meaning["not_runtime_v0_pass_claim"], True)
        self.assertIs(non_meaning["not_runtime_v2_repair"], True)
        self.assertIs(non_meaning["not_runtime_v2_hide"], True)
        self.assertIs(non_meaning["not_runtime_v2_pass_claim"], True)
        self.assertIs(non_meaning["not_runtime_boundary_v0_repair"], True)
        self.assertIs(non_meaning["not_runtime_boundary_v0_hide"], True)
        self.assertIs(non_meaning["not_runtime_boundary_v0_pass_claim"], True)
        self.assertIs(
            summary[
                "runtime_v0_runtime_permission_created_default_artifact_extraction_mismatch_preserved"
            ],
            True,
        )
        self.assertIs(summary["runtime_v0_failure_evidence_preserved"], True)
        self.assertIs(
            summary[
                "runtime_v2_write_helper_missing_file_handle_failure_preserved"
            ],
            True,
        )
        self.assertIs(summary["runtime_v2_failure_evidence_preserved"], True)
        self.assertIs(summary["runtime_boundary_v0_failure_evidence_preserved"], True)
        self.assertEqual(
            summary["successor_of_resolver_module"],
            "resolve_local_relevance_medium_read_only_runtime_v0_min_v2",
        )

    def assert_recorded_runtime(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)
        metadata = result["local_relevance_medium_read_only_runtime_metadata"]
        self.assertEqual(metadata["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        runtime = self.runtime(result)
        self.assertEqual(runtime["runtime_id"], "local_relevance_medium_read_only_runtime_001")
        self.assertEqual(runtime["runtime_type"], RUNTIME_TYPE)
        self.assertEqual(runtime["runtime_version"], resolver.RESULT_VERSION)
        self.assertEqual(runtime["runtime_scope"], RUNTIME_SCOPE)
        self.assertEqual(runtime["basis_runtime_boundary_outcome"], RUNTIME_BOUNDARY_OUTCOME)
        self.assertEqual(runtime["basis_runtime_boundary_result_version"], "0.1.0")
        self.assertEqual(runtime["basis_runtime_boundary_failed_check_count"], 0)
        self.assertEqual(runtime["basis_runtime_permission_outcome"], RUNTIME_PERMISSION_OUTCOME)
        self.assertEqual(runtime["basis_runtime_permission_result_version"], "0.1.0")
        self.assertEqual(runtime["basis_runtime_permission_failed_check_count"], 0)
        self.assertEqual(runtime["basis_operation_execution_outcome"], OPERATION_EXECUTION_OUTCOME)
        self.assertEqual(runtime["basis_operation_execution_result_version"], "0.1.0")
        self.assertEqual(runtime["basis_operation_execution_failed_check_count"], 0)
        for key in (
            "selected_command_is_state",
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
            "local_relevance_medium_read_only_runtime_recorded",
            "runtime_created",
            "runtime_local_only",
            "runtime_read_only",
        ):
            self.assertIs(runtime[key], True, key)
        self.assertEqual(runtime["selected_command"], SELECTED_COMMAND)
        self.assert_runtime_non_claims(result)
        self.assert_runtime_object_not_wrapper(result)
        statement = self.statement(result)
        for key in STATEMENT_TRUE_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
        self.assert_canonical_false_non_claims(result)
        self.assert_lineage_preserved(result)

    def base_runtime_boundary_artifact(self) -> dict[str, Any]:
        boundary = {
            "boundary_id": "local_relevance_medium_read_only_runtime_boundary_001",
            "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
            "boundary_version": "0.1.0",
            "boundary_scope": "SELECTED_RUNTIME_CONSIDERATION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "selected_runtime_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_boundary_recorded": True,
            "selected_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "future_runtime_may_be_considered": True,
            "runtime_created": False,
            "runtime_hosting_created": False,
            "runtime_loop_created": False,
            "daemon_behavior_created": False,
            "continuation_created": False,
            "runtime_held_state_created": False,
            "runtime_held_reentry_created": False,
            "second_operation_created": False,
            "prior_result_reentry_cycle_created": False,
            "older_runtime_lineage_imported_as_authority": False,
            "older_runtime_permission_treated_as_current": False,
            "runtime_authority_imported": False,
            "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved": True,
            "runtime_boundary_v0_failure_evidence_preserved": True,
            "consumed_request_reopened": False,
            "authorization_token_reused": False,
            "follow_on_work_authorized": False,
        }
        return {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "outcome": RUNTIME_BOUNDARY_OUTCOME,
            "local_relevance_medium_read_only_runtime_boundary": copy.deepcopy(boundary),
            "local_relevance_medium_read_only_runtime_boundary_statement": copy.deepcopy(boundary),
            "local_relevance_medium_read_only_runtime_boundary_summary": copy.deepcopy(boundary),
        }

    def runtime_permission_layer(self, include_permission_posture: bool = True) -> dict[str, Any]:
        layer = {
            "runtime_permission_id": "local_relevance_medium_read_only_runtime_permission_001",
            "runtime_permission_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
            "runtime_permission_version": "0.1.0",
            "runtime_permission_scope": "SELECTED_RUNTIME_PERMISSION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "runtime_created": False,
            "runtime_hosting_created": False,
            "runtime_loop_created": False,
            "daemon_behavior_created": False,
            "continuation_created": False,
            "runtime_held_state_created": False,
            "runtime_held_reentry_created": False,
            "second_operation_created": False,
            "prior_result_reentry_cycle_created": False,
            "public_api_created": False,
            "participant_facing_interface_created": False,
            "distributed_network_behavior_created": False,
            "older_runtime_lineage_imported_as_authority": False,
            "older_runtime_permission_treated_as_current": False,
            "runtime_authority_imported": False,
            "consumed_request_reopened": False,
            "authorization_token_reused": False,
            "follow_on_work_authorized": False,
        }
        if include_permission_posture:
            layer.update(
                {
                    "local_relevance_medium_read_only_runtime_permission_recorded": True,
                    "selected_runtime_permission_recorded": True,
                    "runtime_permission_created": True,
                    "runtime_permission_local_only": True,
                    "runtime_permission_read_only": True,
                }
            )
        return layer

    def base_runtime_permission_artifact(self) -> dict[str, Any]:
        layer = self.runtime_permission_layer(include_permission_posture=True)
        return {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "outcome": RUNTIME_PERMISSION_OUTCOME,
            "local_relevance_medium_read_only_runtime_permission": copy.deepcopy(layer),
            "local_relevance_medium_read_only_runtime_permission_statement": copy.deepcopy(layer),
            "local_relevance_medium_read_only_runtime_permission_summary": copy.deepcopy(layer),
        }

    def base_operation_execution_artifact(self) -> dict[str, Any]:
        execution = {
            "operation_execution_id": "local_relevance_medium_read_only_operation_execution_001",
            "operation_execution_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
            "operation_execution_version": "0.1.0",
            "operation_execution_scope": "SELECTED_OPERATION_EXECUTION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "runtime_hosting_created": False,
            "runtime_loop_created": False,
            "daemon_behavior_created": False,
            "continuation_created": False,
            "runtime_held_state_created": False,
            "runtime_held_reentry_created": False,
            "second_operation_created": False,
            "prior_result_reentry_cycle_created": False,
            "public_api_created": False,
            "participant_facing_interface_created": False,
            "distributed_network_behavior_created": False,
            "older_runtime_lineage_imported_as_authority": False,
            "older_runtime_permission_treated_as_current": False,
            "runtime_authority_imported": False,
            "consumed_request_reopened": False,
            "authorization_token_reused": False,
            "follow_on_work_authorized": False,
        }
        return {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "outcome": OPERATION_EXECUTION_OUTCOME,
            "local_relevance_medium_read_only_operation_execution": copy.deepcopy(execution),
            "local_relevance_medium_read_only_operation_execution_statement": copy.deepcopy(execution),
            "local_relevance_medium_read_only_operation_execution_summary": copy.deepcopy(execution),
        }

    def write_synthetic_artifacts(
        self,
        root: Path,
        runtime_boundary: Mapping[str, Any] | None = None,
        runtime_permission: Mapping[str, Any] | None = None,
        operation_execution: Mapping[str, Any] | None = None,
        prefix: str = "clean",
    ) -> tuple[Path, Path, Path]:
        boundary_path = self.write_json(
            root / self.safe_json_filename(f"{prefix}_runtime_boundary"),
            runtime_boundary or self.base_runtime_boundary_artifact(),
        )
        permission_path = self.write_json(
            root / self.safe_json_filename(f"{prefix}_runtime_permission"),
            runtime_permission or self.base_runtime_permission_artifact(),
        )
        execution_path = self.write_json(
            root / self.safe_json_filename(f"{prefix}_operation_execution"),
            operation_execution or self.base_operation_execution_artifact(),
        )
        return boundary_path, permission_path, execution_path

    def clean_request(
        self,
        root: Path,
        runtime_boundary: Mapping[str, Any] | None = None,
        runtime_permission: Mapping[str, Any] | None = None,
        operation_execution: Mapping[str, Any] | None = None,
        prefix: str = "clean",
    ) -> dict[str, Any]:
        boundary_path, permission_path, execution_path = self.write_synthetic_artifacts(
            root,
            runtime_boundary=runtime_boundary,
            runtime_permission=runtime_permission,
            operation_execution=operation_execution,
            prefix=prefix,
        )
        return resolver.build_declared_local_relevance_medium_read_only_runtime_v0_min_v3_request(
            selected_runtime_boundary_artifact=boundary_path,
            selected_runtime_permission_artifact=permission_path,
            selected_operation_execution_artifact=execution_path,
        )

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_runtime_v0_min_v3",
            "resolve_local_relevance_medium_read_only_runtime_v0_min_v3_from_path",
            "write_local_relevance_medium_read_only_runtime_v0_min_v3_result",
            "build_local_relevance_medium_read_only_runtime_v0_min_v3_summary",
            "build_declared_local_relevance_medium_read_only_runtime_v0_min_v3_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_RUNTIME_TYPE_VALUES",
            "SUPPORTED_RUNTIME_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_runtime_v0_min_v3",
        )
        self.assertTrue(
            resolver.OUTPUT_ROOT.as_posix().endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
                "runtime_v0_min_v3"
            )
        )
        self.assertIn(RUNTIME_TYPE, resolver.SUPPORTED_RUNTIME_TYPE_VALUES)
        self.assertIn(RUNTIME_SCOPE, resolver.SUPPORTED_RUNTIME_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, SELECTED_COMMAND)
        for key in (
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "continuation_created",
            "runtime_held_state_created",
            "runtime_held_reentry_created",
            "second_operation_created",
            "prior_result_reentry_cycle_created",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
            "follow_on_work_authorized",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in ("runtime_created", "runtime_local_only", "runtime_read_only"):
            self.assertNotIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for code in (
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "RUNTIME_AUTHORITY_IMPORTED",
            "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
            "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN",
            "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
            "RUNTIME_PERMISSION_NOT_CREATED",
            "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE",
            "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        for key in (
            "runtime_v0_runtime_permission_created_default_artifact_extraction_mismatch_preserved",
            "runtime_v0_failure_evidence_preserved",
            "runtime_v2_write_helper_missing_file_handle_failure_preserved",
            "runtime_v2_failure_evidence_preserved",
            "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved",
            "runtime_boundary_v0_failure_evidence_preserved",
            "predecessor_failure_evidence_preserved",
        ):
            self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS)
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        request = resolver.build_declared_local_relevance_medium_read_only_runtime_v0_min_v3_request()
        self.assertTrue(
            request["selected_runtime_boundary_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_boundary_reference_review_001__"
                "local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
            )
        )
        self.assertTrue(
            request["selected_runtime_permission_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_permission_reference_review_001__"
                "local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
            )
        )
        self.assertTrue(
            request["selected_operation_execution_artifact"].endswith(
                "local_relevance_medium_read_only_operation_execution_reference_review_001__"
                "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        for key in (
            "consumed_request_reopened",
            "authorization_token_reused",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
        ):
            self.assertIs(request["declared_non_claims"][key], False)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.clean_request(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                request
            )
        self.assert_recorded_runtime(result)
        runtime = self.runtime(result)
        self.assert_same_or_stable_artifact_path(
            runtime["basis_runtime_boundary_artifact"],
            request["selected_runtime_boundary_artifact"],
        )
        self.assert_same_or_stable_artifact_path(
            runtime["basis_runtime_permission_artifact"],
            request["selected_runtime_permission_artifact"],
        )
        self.assert_same_or_stable_artifact_path(
            runtime["basis_operation_execution_artifact"],
            request["selected_operation_execution_artifact"],
        )

    def test_runtime_permission_relevant_layer_extraction(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            for layer_name in RUNTIME_PERMISSION_LAYERS:
                with self.subTest(source_layer=layer_name):
                    artifact = {
                        "result_version": "0.1.0",
                        "failed_check_count": 0,
                        "outcome": RUNTIME_PERMISSION_OUTCOME,
                    }
                    for candidate_layer in RUNTIME_PERMISSION_LAYERS:
                        include = candidate_layer == layer_name
                        artifact[candidate_layer] = self.runtime_permission_layer(
                            include_permission_posture=include
                        )
                    request = self.clean_request(
                        tmp_path,
                        runtime_permission=artifact,
                        prefix=f"layer_{layer_name}",
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                        request
                    )
                    self.assert_recorded_runtime(result)
                    runtime = self.runtime(result)
                    self.assertIs(runtime["runtime_permission_created"], True)
                    self.assertIs(runtime["runtime_permission_local_only"], True)
                    self.assertIs(runtime["runtime_permission_read_only"], True)
            for field, expected_code in (
                ("runtime_permission_created", "RUNTIME_PERMISSION_NOT_CREATED"),
                ("runtime_permission_local_only", "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE"),
                ("runtime_permission_read_only", "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE"),
            ):
                with self.subTest(false_contradiction=field):
                    artifact = self.base_runtime_permission_artifact()
                    artifact[
                        "local_relevance_medium_read_only_runtime_permission"
                    ][field] = True
                    artifact[
                        "local_relevance_medium_read_only_runtime_permission_statement"
                    ][field] = False
                    request = self.clean_request(
                        tmp_path,
                        runtime_permission=artifact,
                        prefix=f"false_{field}",
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assert_lineage_preserved(result)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        defaults = (
            DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
            DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
            DEFAULT_OPERATION_EXECUTION_ARTIFACT,
        )
        if not all(path.exists() for path in defaults):
            self.skipTest("default live runtime v3 basis artifacts are not present")
        request = resolver.build_declared_local_relevance_medium_read_only_runtime_v0_min_v3_request()
        result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
            request
        )
        self.assert_recorded_runtime(result)
        runtime = self.runtime(result)
        self.assert_same_or_stable_artifact_path(
            runtime["basis_runtime_boundary_artifact"],
            DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
        )
        self.assert_same_or_stable_artifact_path(
            runtime["basis_runtime_permission_artifact"],
            DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
        )
        self.assert_same_or_stable_artifact_path(
            runtime["basis_operation_execution_artifact"],
            DEFAULT_OPERATION_EXECUTION_ARTIFACT,
        )

    def test_closure_runtime_import_and_lineage_blocking(self) -> None:
        exact_cases = (
            ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
            ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
            (
                "older_runtime_lineage_imported_as_authority",
                "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            ),
            (
                "older_runtime_permission_treated_as_current",
                "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            ),
            ("runtime_authority_imported", "RUNTIME_AUTHORITY_IMPORTED"),
            (
                "runtime_boundary_v0_failure_repaired",
                "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
            ),
            (
                "runtime_boundary_v0_failure_hidden",
                "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN",
            ),
            (
                "runtime_boundary_v0_failure_claimed_passed",
                "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
            ),
        )
        predecessor_cases = (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
        declared_non_claim_cases = (
            "consumed_request_reopened",
            "authorization_token_reused",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
        )
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            for key, expected_code in exact_cases:
                with self.subTest(top_level=key):
                    request = self.clean_request(tmp_path, prefix=f"top_{key}")
                    request[key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
            for key in predecessor_cases:
                with self.subTest(top_level=key):
                    request = self.clean_request(tmp_path, prefix=f"top_{key}")
                    request[key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(
                        self.block_code(result),
                        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
                    )
            for key in declared_non_claim_cases:
                for value in (True, "false", None, "__MISSING__"):
                    with self.subTest(declared_non_claim=key, value=value):
                        request = self.clean_request(tmp_path, prefix=f"nonclaim_{key}_{value}")
                        if value == "__MISSING__":
                            request["declared_non_claims"].pop(key)
                        else:
                            request["declared_non_claims"][key] = value
                        result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                            request
                        )
                        self.assert_blocked_with_public_code(result)
                        self.assertEqual(
                            self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED"
                        )

    def test_required_false_non_claims_canonicalize_after_flipped_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base_request = self.clean_request(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.non_claims(result)[key], False)
                    self.assert_lineage_preserved(result)

    def test_representative_blocking_behavior(self) -> None:
        top_level_flags = (
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
            "local_relevance_medium_read_only_runtime_not_recorded",
            "runtime_not_created",
            "runtime_local_only_not_true",
            "runtime_read_only_not_true",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "continuation_created",
            "runtime_held_state_created",
            "runtime_held_reentry_created",
            "second_operation_created",
            "prior_result_reentry_cycle_created",
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
            "artifact_existence_treated_as_runtime_authority",
            "latest_file_posture_treated_as_runtime_authority",
            "repo_local_availability_treated_as_runtime_authority",
            "hidden_repo_state_used_as_runtime_content",
            "hidden_repo_state_used_as_runtime_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            malformed_cases: list[tuple[str, Any]] = [
                ("missing request fields", {}),
                ("non-mapping request", ["not", "a", "mapping"]),
            ]
            for name, payload in malformed_cases:
                with self.subTest(case=name):
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                        payload
                    )
                    self.assert_blocked_with_public_code(result)
            request_cases: list[tuple[str, dict[str, Any]]] = [
                (
                    "explicit block intent",
                    {
                        "local_relevance_medium_read_only_runtime_intent": (
                            "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME"
                        )
                    },
                ),
                ("unsupported intent", {"local_relevance_medium_read_only_runtime_intent": "NOPE"}),
                ("selected command missing", {"selected_command": ""}),
                ("selected command not state", {"selected_command": "status"}),
                ("runtime type missing", {"runtime_type": ""}),
                ("runtime type wrong", {"runtime_type": "LOCAL_RELEVANCE_MEDIUM_RUNTIME_HOSTING"}),
                ("runtime scope missing", {"runtime_scope": ""}),
                ("runtime scope wrong", {"runtime_scope": "RUNTIME_HOSTING"}),
            ]
            for name, mutation in request_cases:
                with self.subTest(case=name):
                    request = self.clean_request(tmp_path, prefix=self.safe_json_filename(name))
                    request.update(mutation)
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
            artifact_cases = (
                ("runtime boundary artifact path missing", "selected_runtime_boundary_artifact", ""),
                ("runtime boundary artifact unreadable", "selected_runtime_boundary_artifact", tmp_path / "missing_boundary.json"),
                ("runtime permission artifact path missing", "selected_runtime_permission_artifact", ""),
                ("runtime permission artifact unreadable", "selected_runtime_permission_artifact", tmp_path / "missing_permission.json"),
                ("operation execution artifact path missing", "selected_operation_execution_artifact", ""),
                ("operation execution artifact unreadable", "selected_operation_execution_artifact", tmp_path / "missing_execution.json"),
            )
            for name, field, value in artifact_cases:
                with self.subTest(case=name):
                    request = self.clean_request(tmp_path, prefix=self.safe_json_filename(name))
                    request[field] = str(value)
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
            artifact_mutations = (
                ("runtime boundary artifact JSON array", "selected_runtime_boundary_artifact", []),
                ("runtime permission artifact JSON array", "selected_runtime_permission_artifact", []),
                ("operation execution artifact JSON array", "selected_operation_execution_artifact", []),
                (
                    "runtime boundary artifact not recorded",
                    "selected_runtime_boundary_artifact",
                    {"outcome": "NOPE", "result_version": "0.1.0", "failed_check_count": 0},
                ),
                (
                    "runtime permission artifact not recorded",
                    "selected_runtime_permission_artifact",
                    {"outcome": "NOPE", "result_version": "0.1.0", "failed_check_count": 0},
                ),
                (
                    "operation execution artifact not recorded",
                    "selected_operation_execution_artifact",
                    {"outcome": "NOPE", "result_version": "0.1.0", "failed_check_count": 0},
                ),
                (
                    "runtime boundary artifact failed checks present",
                    "selected_runtime_boundary_artifact",
                    {**self.base_runtime_boundary_artifact(), "failed_check_count": 1},
                ),
                (
                    "runtime permission artifact failed checks present",
                    "selected_runtime_permission_artifact",
                    {**self.base_runtime_permission_artifact(), "failed_check_count": 1},
                ),
                (
                    "operation execution artifact failed checks present",
                    "selected_operation_execution_artifact",
                    {**self.base_operation_execution_artifact(), "failed_check_count": 1},
                ),
                (
                    "runtime boundary artifact version not 0.1.0",
                    "selected_runtime_boundary_artifact",
                    {**self.base_runtime_boundary_artifact(), "result_version": "9.9.9"},
                ),
                (
                    "runtime permission artifact version not 0.1.0",
                    "selected_runtime_permission_artifact",
                    {**self.base_runtime_permission_artifact(), "result_version": "9.9.9"},
                ),
                (
                    "operation execution artifact version not 0.1.0",
                    "selected_operation_execution_artifact",
                    {**self.base_operation_execution_artifact(), "result_version": "9.9.9"},
                ),
            )
            for index, (name, field, artifact) in enumerate(artifact_mutations):
                with self.subTest(case=name):
                    request = self.clean_request(tmp_path, prefix=self.safe_json_filename(name, index))
                    path = self.write_json(
                        tmp_path / self.safe_json_filename(f"mutated_{name}", index),
                        artifact,
                    )
                    request[field] = str(path)
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
            for flag in top_level_flags:
                with self.subTest(top_level_flag=flag):
                    request = self.clean_request(tmp_path, prefix=self.safe_json_filename(flag))
                    request[flag] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
            with self.subTest(case="required non-claim missing"):
                request = self.clean_request(tmp_path, prefix="missing_non_claim")
                request["declared_non_claims"].pop("runtime_hosting_created")
                result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                    request
                )
                self.assert_blocked_with_public_code(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.clean_request(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                request
            )
        self.assert_recorded_runtime(result)
        serialized = json.dumps(result, sort_keys=True)
        for official in (
            RUNTIME_TYPE,
            RUNTIME_SCOPE,
            SELECTED_COMMAND,
            resolver.OUTCOME_RECORDED,
            resolver.RESOLVER_MODULE,
        ):
            self.assertIn(official, serialized)
        self.assertNotIn("[REDACTED_SENSITIVE_RUNTIME_CONTENT]", serialized)

    def test_raw_hidden_and_older_runtime_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary = self.base_runtime_boundary_artifact()
            permission = self.base_runtime_permission_artifact()
            execution = self.base_operation_execution_artifact()
            boundary["raw_runtime_boundary_body"] = HOSTILE_SENTINELS[1]
            permission["raw_runtime_permission_body"] = HOSTILE_SENTINELS[2]
            execution["raw_runtime_body"] = HOSTILE_SENTINELS[0]
            request = self.clean_request(
                tmp_path,
                runtime_boundary=boundary,
                runtime_permission=permission,
                operation_execution=execution,
                prefix="hostile",
            )
            request["raw_runtime_body"] = HOSTILE_SENTINELS[0]
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            original_request = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                request
            )
        self.assertEqual(request, original_request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        for official in (RUNTIME_TYPE, RUNTIME_SCOPE, SELECTED_COMMAND, resolver.RESOLVER_MODULE):
            self.assertIn(official, serialized)
        self.assert_canonical_false_non_claims(result)
        self.assert_runtime_non_claims(result)
        self.assert_lineage_preserved(result)

    def test_write_helper_regression(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request = self.clean_request(tmp_path)
            result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                request
            )
            self.assert_recorded_runtime(result)
            output_root = tmp_path / "local_relevance_medium_read_only_runtime_v0_min_v3"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                written = resolver.write_local_relevance_medium_read_only_runtime_v0_min_v3_result(
                    result
                )
                written_again = resolver.write_local_relevance_medium_read_only_runtime_v0_min_v3_result(
                    result
                )
            self.assertIsInstance(written, Path)
            self.assertTrue(written.exists())
            self.assertTrue(written_again.exists())
            self.assertNotEqual(written, written_again)
            self.assertIn("local_relevance_medium_read_only_runtime_v0_min_v3", written.as_posix())
            with written.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            with written_again.open("r", encoding="utf-8") as handle:
                parsed_again = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(parsed_again["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(
                parsed["local_relevance_medium_read_only_runtime_metadata"][
                    "resolver_module"
                ],
                "resolve_local_relevance_medium_read_only_runtime_v0_min_v3",
            )
            for forbidden in FORBIDDEN_OUTPUT_ROOTS:
                forbidden_abs = (REPO_ROOT / forbidden).resolve()
                self.assertFalse(
                    written.resolve().is_relative_to(forbidden_abs),
                    forbidden.as_posix(),
                )
            explicit_path = (
                tmp_path
                / "explicit"
                / "local_relevance_medium_read_only_runtime_v0_min_v3"
                / "explicit_result.json"
            )
            explicit_written = (
                resolver.write_local_relevance_medium_read_only_runtime_v0_min_v3_result(
                    result, explicit_path
                )
            )
            explicit_written_again = (
                resolver.write_local_relevance_medium_read_only_runtime_v0_min_v3_result(
                    result, explicit_path
                )
            )
            self.assertEqual(explicit_written, explicit_path)
            self.assertTrue(explicit_written.exists())
            self.assertTrue(explicit_written_again.exists())
            self.assertNotEqual(explicit_written, explicit_written_again)
            with explicit_written.open("r", encoding="utf-8") as handle:
                explicit_parsed = json.load(handle)
            self.assertEqual(explicit_parsed["outcome"], resolver.OUTCOME_RECORDED)

    def test_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request = self.clean_request(tmp_path)
            request_path = self.write_json(tmp_path / "request.json", request)
            result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3_from_path(
                request_path
            )
            self.assert_recorded_runtime(result)
            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3_from_path(
                malformed_path
            )
            self.assert_blocked_with_public_code(malformed)
            array_path = self.write_json(tmp_path / "array.json", [])
            array_result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3_from_path(
                array_path
            )
            self.assert_blocked_with_public_code(array_result)
            missing_result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3_from_path(
                tmp_path / "missing.json"
            )
            self.assert_blocked_with_public_code(missing_result)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary = self.base_runtime_boundary_artifact()
            permission = self.base_runtime_permission_artifact()
            execution = self.base_operation_execution_artifact()
            boundary_before = copy.deepcopy(boundary)
            permission_before = copy.deepcopy(permission)
            execution_before = copy.deepcopy(execution)
            request = self.clean_request(
                tmp_path,
                runtime_boundary=boundary,
                runtime_permission=permission,
                operation_execution=execution,
                prefix="non_mutation",
            )
            request["raw_runtime_body"] = HOSTILE_SENTINELS[0]
            request_before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                request
            )
        self.assert_recorded_runtime(result)
        self.assertEqual(request, request_before)
        self.assertEqual(boundary, boundary_before)
        self.assertEqual(permission, permission_before)
        self.assertEqual(execution, execution_before)

    def test_runtime_v0_v2_and_runtime_boundary_v0_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.clean_request(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                request
            )
            self.assert_recorded_runtime(result)
            self.assert_lineage_preserved(result)
            for key, expected_code in (
                ("runtime_boundary_v0_failure_repaired", "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED"),
                ("runtime_boundary_v0_failure_hidden", "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN"),
                (
                    "runtime_boundary_v0_failure_claimed_passed",
                    "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
                ),
            ):
                with self.subTest(flip=key):
                    blocked_request = copy.deepcopy(request)
                    blocked_request[key] = True
                    blocked = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                        blocked_request
                    )
                    self.assert_blocked_with_public_code(blocked)
                    self.assertEqual(self.block_code(blocked), expected_code)

    def test_predecessor_failure_preservation_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.clean_request(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_v3(
                request
            )
        self.assert_recorded_runtime(result)
        summary = self.summary(result)
        non_claims = self.non_claims(result)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["older_runtime_lineage_not_imported_as_authority"], True)
        self.assertIs(summary["older_runtime_permission_not_treated_as_current"], True)
        self.assertIs(summary["runtime_authority_not_imported"], True)
        self.assertIs(summary["runtime_v0_failure_evidence_preserved"], True)
        self.assertIs(
            summary[
                "runtime_v2_write_helper_missing_file_handle_failure_preserved"
            ],
            True,
        )
        self.assertIs(summary["runtime_v2_failure_evidence_preserved"], True)
        self.assertIs(
            summary["runtime_boundary_v0_failure_evidence_preserved"], True
        )
        for key in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertIs(non_claims[key], False)


if __name__ == "__main__":
    unittest.main()
