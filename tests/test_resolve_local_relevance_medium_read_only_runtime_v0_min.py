"""Tests for the local relevance medium read-only selected-state runtime.

This suite is bounded to one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME object.
It verifies that the resolver reads one clean runtime boundary v2 artifact, one
clean selected-state runtime permission artifact, and one clean selected-state
operation execution artifact, then records one local read-only selected-state
runtime object only.

The suite does not create runtime hosting behavior, runtime loop behavior,
daemon behavior, continuation behavior, runtime-held state, runtime-held
re-entry, second operation behavior, prior-result re-entry behavior, public API
behavior, participant-facing interface behavior, distributed-network behavior,
general operation permission, general lookup permission, arbitrary lookup
permission, unsupported-command permission, unsupported-key permission, new
lookup entry behavior beyond the already bounded selected-state lookup result
object, registry, search, query surface, ranking, scoring, priority,
validity/truth/authority/currentness judgment, older-runtime authority import,
repeated reception permission, arbitrary reception, feed, source transfer,
source receipt, authority/currentness/truth/synchronization/participation
behavior, or follow-on work.
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

import resolve_local_relevance_medium_read_only_runtime_v0_min as resolver  # noqa: E402


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

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "operation_execution_boundary_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_distributed_network_behavior_v0_min"
    ),
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
    "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
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


class LocalRelevanceMediumReadOnlyRuntimeV0MinTest(unittest.TestCase):
    def safe_json_filename(self, name: object, index: int | None = None) -> str:
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

    def synthetic_runtime_boundary_artifact(self) -> dict[str, Any]:
        boundary = {
            "boundary_id": "local_relevance_medium_read_only_runtime_boundary_001",
            "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
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
            "outcome": RUNTIME_BOUNDARY_OUTCOME,
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
            "local_relevance_medium_read_only_runtime_boundary_metadata": {
                "result_version": resolver.RESULT_VERSION,
                "failed_check_count": 0,
                "resolver_module": "resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2",
            },
            "local_relevance_medium_read_only_runtime_boundary": dict(boundary),
            "local_relevance_medium_read_only_runtime_boundary_statement": dict(
                boundary
            ),
            "local_relevance_medium_read_only_runtime_boundary_summary": dict(
                boundary,
                result_version=resolver.RESULT_VERSION,
                failed_check_count=0,
            ),
            "local_relevance_medium_read_only_runtime_boundary_checks": [
                {"check_name": "synthetic clean", "passed": True}
            ],
        }

    def synthetic_runtime_permission_artifact(self) -> dict[str, Any]:
        permission = {
            "runtime_permission_id": (
                "local_relevance_medium_read_only_runtime_permission_001"
            ),
            "runtime_permission_type": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION"
            ),
            "runtime_permission_scope": "SELECTED_RUNTIME_PERMISSION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
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
        return {
            "outcome": RUNTIME_PERMISSION_OUTCOME,
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
            "local_relevance_medium_read_only_runtime_permission_metadata": {
                "result_version": resolver.RESULT_VERSION,
                "failed_check_count": 0,
                "resolver_module": (
                    "resolve_local_relevance_medium_read_only_runtime_permission_v0_min"
                ),
            },
            "local_relevance_medium_read_only_runtime_permission": dict(permission),
            "local_relevance_medium_read_only_runtime_permission_statement": dict(
                permission
            ),
            "local_relevance_medium_read_only_runtime_permission_summary": dict(
                permission,
                result_version=resolver.RESULT_VERSION,
                failed_check_count=0,
            ),
            "local_relevance_medium_read_only_runtime_permission_checks": [
                {"check_name": "synthetic clean", "passed": True}
            ],
        }

    def synthetic_operation_execution_artifact(self) -> dict[str, Any]:
        execution = {
            "operation_execution_id": (
                "local_relevance_medium_read_only_operation_execution_001"
            ),
            "operation_execution_type": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION"
            ),
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
            "outcome": OPERATION_EXECUTION_OUTCOME,
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
            "local_relevance_medium_read_only_operation_execution_metadata": {
                "result_version": resolver.RESULT_VERSION,
                "failed_check_count": 0,
                "resolver_module": (
                    "resolve_local_relevance_medium_read_only_operation_execution_v0_min"
                ),
            },
            "local_relevance_medium_read_only_operation_execution": dict(execution),
            "local_relevance_medium_read_only_operation_execution_statement": dict(
                execution
            ),
            "local_relevance_medium_read_only_operation_execution_summary": dict(
                execution,
                result_version=resolver.RESULT_VERSION,
                failed_check_count=0,
            ),
            "local_relevance_medium_read_only_operation_execution_checks": [
                {"check_name": "synthetic clean", "passed": True}
            ],
        }

    def build_synthetic_request(
        self,
        root: Path,
        name: str = "clean",
        index: int | None = None,
        runtime_boundary_mutator: Callable[[dict[str, Any]], None] | None = None,
        runtime_permission_mutator: Callable[[dict[str, Any]], None] | None = None,
        operation_execution_mutator: Callable[[dict[str, Any]], None] | None = None,
    ) -> tuple[dict[str, Any], dict[str, Path], dict[str, dict[str, Any]]]:
        runtime_boundary = self.synthetic_runtime_boundary_artifact()
        runtime_permission = self.synthetic_runtime_permission_artifact()
        operation_execution = self.synthetic_operation_execution_artifact()
        if runtime_boundary_mutator is not None:
            runtime_boundary_mutator(runtime_boundary)
        if runtime_permission_mutator is not None:
            runtime_permission_mutator(runtime_permission)
        if operation_execution_mutator is not None:
            operation_execution_mutator(operation_execution)

        paths = {
            "runtime_boundary": root
            / self.safe_json_filename(f"{name}_runtime_boundary", index),
            "runtime_permission": root
            / self.safe_json_filename(f"{name}_runtime_permission", index),
            "operation_execution": root
            / self.safe_json_filename(f"{name}_operation_execution", index),
        }
        self.write_json(paths["runtime_boundary"], runtime_boundary)
        self.write_json(paths["runtime_permission"], runtime_permission)
        self.write_json(paths["operation_execution"], operation_execution)
        request = resolver.build_declared_local_relevance_medium_read_only_runtime_v0_min_request(
            selected_runtime_boundary_artifact=paths["runtime_boundary"],
            selected_runtime_permission_artifact=paths["runtime_permission"],
            selected_operation_execution_artifact=paths["operation_execution"],
        )
        artifacts = {
            "runtime_boundary": runtime_boundary,
            "runtime_permission": runtime_permission,
            "operation_execution": operation_execution,
        }
        return request, paths, artifacts

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get("local_relevance_medium_read_only_runtime_checks", [])
        self.assertIsInstance(checks, list)
        return checks

    def runtime(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        runtime = result.get("local_relevance_medium_read_only_runtime")
        self.assertIsInstance(runtime, Mapping)
        return runtime

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get("local_relevance_medium_read_only_runtime_statement")
        self.assertIsInstance(statement, Mapping)
        return statement

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get("local_relevance_medium_read_only_runtime_summary")
        self.assertIsInstance(summary, Mapping)
        return summary

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_same_or_stable_artifact_path(
        self, actual: str | Path, expected: str | Path
    ) -> None:
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
        block_code = self.block_code(result)
        if block_code is not None:
            self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIsInstance(non_claims[key], bool)
            self.assertIs(non_claims[key], False)
        self.assertNotIn("runtime_created", non_claims)
        self.assertNotIn("runtime_local_only", non_claims)
        self.assertNotIn("runtime_read_only", non_claims)

    def assert_runtime_non_claims(self, result: Mapping[str, Any]) -> None:
        runtime = self.runtime(result)
        for key in RUNTIME_FALSE_FIELDS:
            self.assertIn(key, runtime)
            self.assertIs(runtime[key], False, key)
        non_claims = result["non_claims"]
        for key in (
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "source_created",
            "deployment_created",
            "public_release_created",
            "broader_reusable_permission_created",
        ):
            self.assertIn(key, non_claims)
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

    def assert_runtime_object_not_wrapper(self, result: Mapping[str, Any]) -> None:
        runtime = self.runtime(result)
        for key in FORBIDDEN_RUNTIME_WRAPPER_FIELDS:
            self.assertNotIn(key, runtime)

    def assert_runtime_recorded_posture(
        self, result: Mapping[str, Any], paths: Mapping[str, Path] | None = None
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertEqual(self.summary(result)["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(self.passed_check_count(result), 0)
        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        runtime = self.runtime(result)
        self.assertEqual(runtime["runtime_id"], "local_relevance_medium_read_only_runtime_001")
        self.assertEqual(runtime["runtime_type"], RUNTIME_TYPE)
        self.assertEqual(runtime["runtime_version"], resolver.RESULT_VERSION)
        self.assertEqual(runtime["runtime_scope"], RUNTIME_SCOPE)
        if paths is not None:
            self.assert_same_or_stable_artifact_path(
                runtime["basis_runtime_boundary_artifact"],
                paths["runtime_boundary"],
            )
            self.assert_same_or_stable_artifact_path(
                runtime["basis_runtime_permission_artifact"],
                paths["runtime_permission"],
            )
            self.assert_same_or_stable_artifact_path(
                runtime["basis_operation_execution_artifact"],
                paths["operation_execution"],
            )
        self.assertEqual(runtime["basis_runtime_boundary_outcome"], RUNTIME_BOUNDARY_OUTCOME)
        self.assertEqual(runtime["basis_runtime_boundary_result_version"], resolver.RESULT_VERSION)
        self.assertEqual(runtime["basis_runtime_boundary_failed_check_count"], 0)
        self.assertEqual(runtime["basis_runtime_permission_outcome"], RUNTIME_PERMISSION_OUTCOME)
        self.assertEqual(runtime["basis_runtime_permission_result_version"], resolver.RESULT_VERSION)
        self.assertEqual(runtime["basis_runtime_permission_failed_check_count"], 0)
        self.assertEqual(runtime["basis_operation_execution_outcome"], OPERATION_EXECUTION_OUTCOME)
        self.assertEqual(runtime["basis_operation_execution_result_version"], resolver.RESULT_VERSION)
        self.assertEqual(runtime["basis_operation_execution_failed_check_count"], 0)
        self.assertEqual(runtime["selected_command"], SELECTED_COMMAND)
        self.assertIs(runtime["selected_command_is_state"], True)
        for key in (
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
            "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved",
            "runtime_boundary_v0_failure_evidence_preserved",
        ):
            self.assertIs(runtime[key], True, key)
        self.assert_runtime_non_claims(result)
        self.assert_runtime_object_not_wrapper(result)

        statement = self.statement(result)
        for key in STATEMENT_TRUE_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
        self.assert_canonical_false_non_claims(result)
        self.assert_all_emitted_codes_public(result)

    def assert_v0_failure_preserved(self, result: Mapping[str, Any]) -> None:
        runtime = self.runtime(result)
        statement = self.statement(result)
        summary = self.summary(result)
        self.assertIs(
            runtime[
                "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved"
            ],
            True,
        )
        self.assertIs(runtime["runtime_boundary_v0_failure_evidence_preserved"], True)
        self.assertIs(statement["runtime_boundary_v0_failure_evidence_preserved"], True)
        self.assertIs(summary["runtime_boundary_v0_failure_evidence_preserved"], True)
        self.assertIs(
            summary["runtime_boundary_v0_failure_not_repaired_hidden_claimed_passed"],
            True,
        )
        for key in (
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
        ):
            self.assertIs(result["non_claims"][key], False)

    def assert_path_not_under_forbidden_roots(self, path: Path) -> None:
        resolved = path.resolve()
        for root in FORBIDDEN_OUTPUT_ROOTS:
            forbidden = (REPO_ROOT / root).resolve()
            try:
                resolved.relative_to(forbidden)
            except ValueError:
                continue
            self.fail(f"{resolved} unexpectedly writes under {forbidden}")

    def assert_serialized_no_sentinels(
        self, result: Mapping[str, Any], sentinels: tuple[str, ...] = HOSTILE_SENTINELS
    ) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in sentinels:
            self.assertNotIn(sentinel, serialized)

    def mutate_nested_key(
        self, artifact: dict[str, Any], key: str, value: Any
    ) -> None:
        artifact[key] = value
        for section in artifact.values():
            if isinstance(section, dict) and key in section:
                section[key] = value

    def resolve_case(self, request: Any) -> dict[str, Any]:
        return resolver.resolve_local_relevance_medium_read_only_runtime_v0_min(request)

    def test_public_api_constants_and_builder_defaults(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_runtime_v0_min",
            "resolve_local_relevance_medium_read_only_runtime_v0_min_from_path",
            "write_local_relevance_medium_read_only_runtime_v0_min_result",
            "build_local_relevance_medium_read_only_runtime_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_runtime_v0_min_request",
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
            "resolve_local_relevance_medium_read_only_runtime_v0_min",
        )
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
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
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertNotIn("runtime_created", resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertNotIn("runtime_local_only", resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertNotIn("runtime_read_only", resolver.REQUIRED_FALSE_NON_CLAIMS)
        for code in (
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "RUNTIME_AUTHORITY_IMPORTED",
            "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
            "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN",
            "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        request = resolver.build_declared_local_relevance_medium_read_only_runtime_v0_min_request()
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

        self.assert_path_not_under_forbidden_roots(REPO_ROOT / resolver.OUTPUT_ROOT)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, paths, _artifacts = self.build_synthetic_request(Path(tmp))
            result = self.resolve_case(request)

        self.assert_runtime_recorded_posture(result, paths)
        runtime = self.runtime(result)
        self.assertIs(runtime["runtime_created"], True)
        self.assertIs(runtime["runtime_local_only"], True)
        self.assertIs(runtime["runtime_read_only"], True)
        self.assertNotIn("runtime_created", result["non_claims"])
        self.assertNotIn("runtime_local_only", result["non_claims"])
        self.assertNotIn("runtime_read_only", result["non_claims"])

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        default_paths = {
            "runtime_boundary": DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
            "runtime_permission": DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
            "operation_execution": DEFAULT_OPERATION_EXECUTION_ARTIFACT,
        }
        missing = [path for path in default_paths.values() if not path.exists()]
        if missing:
            self.skipTest(f"default live artifacts absent: {missing!r}")
        request = resolver.build_declared_local_relevance_medium_read_only_runtime_v0_min_request()
        result = self.resolve_case(request)
        self.assert_runtime_recorded_posture(result)
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
        self.assert_v0_failure_preserved(result)

    def test_closure_older_runtime_and_v0_failure_blocking(self) -> None:
        top_level_cases = (
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
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for index, (key, expected_code) in enumerate(top_level_cases):
                with self.subTest(top_level=key):
                    request, _paths, _artifacts = self.build_synthetic_request(
                        root, key, index
                    )
                    request[key] = True
                    result = self.resolve_case(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
            for index, (key, _expected_code) in enumerate(top_level_cases, start=100):
                for value in (True, "false", None):
                    with self.subTest(declared_non_claim=key, value=value):
                        request, _paths, _artifacts = self.build_synthetic_request(
                            root, f"{key}_{value!r}", index
                        )
                        request["declared_non_claims"][key] = value
                        result = self.resolve_case(request)
                        self.assert_blocked_with_public_code(result)
                        self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                with self.subTest(declared_non_claim_missing=key):
                    request, _paths, _artifacts = self.build_synthetic_request(
                        root, f"{key}_missing", index + 500
                    )
                    del request["declared_non_claims"][key]
                    result = self.resolve_case(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_required_false_non_claims_canonicalize_false_when_flipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request, _paths, _artifacts = self.build_synthetic_request(root)
            for index, key in enumerate(resolver.REQUIRED_FALSE_NON_CLAIMS):
                with self.subTest(key=key):
                    mutated = copy.deepcopy(request)
                    mutated["declared_non_claims"][key] = True
                    result = self.resolve_case(mutated)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)

    def test_representative_blocking_behavior(self) -> None:
        def set_request_flag(key: str) -> Callable[[dict[str, Any]], None]:
            def mutate(request: dict[str, Any]) -> None:
                request[key] = True

            return mutate

        direct_cases: list[tuple[str, Any]] = [
            ("missing request", {}),
            ("non-mapping request", ["not", "a", "mapping"]),
        ]
        top_level_flags = (
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

        request_cases: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
            (
                "explicit block intent",
                lambda req: req.__setitem__(
                    "local_relevance_medium_read_only_runtime_intent",
                    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME",
                ),
            ),
            (
                "unsupported intent",
                lambda req: req.__setitem__(
                    "local_relevance_medium_read_only_runtime_intent", "UNSUPPORTED"
                ),
            ),
            ("runtime boundary artifact path missing", lambda req: req.__setitem__("selected_runtime_boundary_artifact", "")),
            ("runtime permission artifact path missing", lambda req: req.__setitem__("selected_runtime_permission_artifact", "")),
            ("operation execution artifact path missing", lambda req: req.__setitem__("selected_operation_execution_artifact", "")),
            ("runtime boundary artifact unreadable", lambda req: req.__setitem__("selected_runtime_boundary_artifact", "missing_runtime_boundary.json")),
            ("runtime permission artifact unreadable", lambda req: req.__setitem__("selected_runtime_permission_artifact", "missing_runtime_permission.json")),
            ("operation execution artifact unreadable", lambda req: req.__setitem__("selected_operation_execution_artifact", "missing_operation_execution.json")),
            ("selected command missing", lambda req: req.pop("selected_command", None)),
            ("selected command not state", lambda req: req.__setitem__("selected_command", "lookup")),
            ("runtime type missing", lambda req: req.pop("runtime_type", None)),
            ("runtime type not exact", lambda req: req.__setitem__("runtime_type", "PUBLIC_API")),
            ("runtime scope missing", lambda req: req.pop("runtime_scope", None)),
            ("runtime scope not exact", lambda req: req.__setitem__("runtime_scope", "RUNTIME_HOSTING")),
            (
                "required non-claim missing",
                lambda req: req["declared_non_claims"].pop("runtime_hosting_created"),
            ),
            (
                "required non-claim flipped",
                lambda req: req["declared_non_claims"].__setitem__(
                    "runtime_loop_created", True
                ),
            ),
        ]
        request_cases.extend(
            (flag.replace("_", " "), set_request_flag(flag)) for flag in top_level_flags
        )

        artifact_cases: list[
            tuple[
                str,
                Callable[[dict[str, Any]], None] | None,
                Callable[[dict[str, Any]], None] | None,
                Callable[[dict[str, Any]], None] | None,
            ]
        ] = [
            (
                "runtime boundary artifact not recorded",
                lambda art: art.__setitem__("outcome", "BLOCKED"),
                None,
                None,
            ),
            (
                "runtime boundary artifact failed checks present",
                lambda art: art.__setitem__("failed_check_count", 1),
                None,
                None,
            ),
            (
                "runtime boundary artifact version not 0.1.0",
                lambda art: art.__setitem__("result_version", "9.9.9"),
                None,
                None,
            ),
            (
                "runtime permission artifact not recorded",
                None,
                lambda art: art.__setitem__("outcome", "BLOCKED"),
                None,
            ),
            (
                "runtime permission artifact failed checks present",
                None,
                lambda art: art.__setitem__("failed_check_count", 1),
                None,
            ),
            (
                "runtime permission artifact version not 0.1.0",
                None,
                lambda art: art.__setitem__("result_version", "9.9.9"),
                None,
            ),
            (
                "operation execution artifact not recorded",
                None,
                None,
                lambda art: art.__setitem__("outcome", "BLOCKED"),
            ),
            (
                "operation execution artifact failed checks present",
                None,
                None,
                lambda art: art.__setitem__("failed_check_count", 1),
            ),
            (
                "operation execution artifact version not 0.1.0",
                None,
                None,
                lambda art: art.__setitem__("result_version", "9.9.9"),
            ),
            (
                "selected runtime boundary not recorded",
                lambda art: self.mutate_nested_key(art, "selected_runtime_boundary_recorded", False),
                None,
                None,
            ),
            (
                "future runtime may not be considered",
                lambda art: self.mutate_nested_key(art, "future_runtime_may_be_considered", False),
                None,
                None,
            ),
            (
                "selected runtime permission not recorded",
                None,
                lambda art: self.mutate_nested_key(art, "selected_runtime_permission_recorded", False),
                None,
            ),
            (
                "runtime permission not created",
                None,
                lambda art: self.mutate_nested_key(art, "runtime_permission_created", False),
                None,
            ),
            (
                "runtime permission local only not true",
                None,
                lambda art: self.mutate_nested_key(art, "runtime_permission_local_only", False),
                None,
            ),
            (
                "runtime permission read only not true",
                None,
                lambda art: self.mutate_nested_key(art, "runtime_permission_read_only", False),
                None,
            ),
            (
                "selected operation execution not recorded",
                None,
                None,
                lambda art: self.mutate_nested_key(art, "selected_operation_execution_recorded", False),
            ),
            (
                "operation execution not created",
                None,
                None,
                lambda art: self.mutate_nested_key(art, "operation_execution_created", False),
            ),
            (
                "operation execution not performed",
                None,
                None,
                lambda art: self.mutate_nested_key(art, "operation_execution_performed", False),
            ),
            (
                "operation execution local only not true",
                None,
                None,
                lambda art: self.mutate_nested_key(art, "operation_execution_local_only", False),
            ),
            (
                "operation execution read only not true",
                None,
                None,
                lambda art: self.mutate_nested_key(art, "operation_execution_read_only", False),
            ),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for index, (name, direct_request) in enumerate(direct_cases):
                with self.subTest(case=name):
                    result = self.resolve_case(direct_request)
                    self.assert_blocked_with_public_code(result)
            for index, (name, mutator) in enumerate(request_cases, start=20):
                with self.subTest(case=name):
                    request, _paths, _artifacts = self.build_synthetic_request(
                        root, self.safe_json_filename(name), index
                    )
                    mutator(request)
                    result = self.resolve_case(request)
                    self.assert_blocked_with_public_code(result)
            for index, (name, rb_mut, rp_mut, oe_mut) in enumerate(artifact_cases, start=200):
                with self.subTest(case=name):
                    request, _paths, _artifacts = self.build_synthetic_request(
                        root,
                        self.safe_json_filename(name),
                        index,
                        runtime_boundary_mutator=rb_mut,
                        runtime_permission_mutator=rp_mut,
                        operation_execution_mutator=oe_mut,
                    )
                    result = self.resolve_case(request)
                    self.assert_blocked_with_public_code(result)

            for index, artifact_key in enumerate(
                (
                    "selected_runtime_boundary_artifact",
                    "selected_runtime_permission_artifact",
                    "selected_operation_execution_artifact",
                ),
                start=500,
            ):
                with self.subTest(json_array_artifact=artifact_key):
                    request, _paths, _artifacts = self.build_synthetic_request(
                        root, f"{artifact_key}_array", index
                    )
                    array_path = root / self.safe_json_filename(artifact_key, index)
                    self.write_json(array_path, ["not", "object"])
                    request[artifact_key] = str(array_path)
                    result = self.resolve_case(request)
                    self.assert_blocked_with_public_code(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths, _artifacts = self.build_synthetic_request(Path(tmp))
            result = self.resolve_case(request)
        self.assert_runtime_recorded_posture(result)
        serialized = json.dumps(result, sort_keys=True)
        for official in (
            RUNTIME_TYPE,
            RUNTIME_SCOPE,
            SELECTED_COMMAND,
            resolver.OUTCOME_RECORDED,
            resolver.RESOLVER_MODULE,
        ):
            self.assertIn(official, serialized)
        self.assertNotIn("[REDACTED", self.runtime(result)["runtime_type"])
        self.assertNotIn("[REDACTED", self.runtime(result)["runtime_scope"])
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_NOT_RECORDED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_BLOCKED,
        })

    def test_raw_hidden_older_runtime_hostile_content_containment(self) -> None:
        def add_hostile_content(artifact: dict[str, Any]) -> None:
            artifact["raw_runtime_body"] = "RAW_RUNTIME_BODY_MUST_NOT_RETURN"
            artifact["raw_runtime_boundary_body"] = (
                "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN"
            )
            artifact["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
            artifact["older_runtime_authority_import"] = (
                "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN"
            )

        with tempfile.TemporaryDirectory() as tmp:
            request, _paths, _artifacts = self.build_synthetic_request(
                Path(tmp),
                "hostile",
                runtime_boundary_mutator=add_hostile_content,
                runtime_permission_mutator=add_hostile_content,
                operation_execution_mutator=add_hostile_content,
            )
            request_before = copy.deepcopy(request)
            request["raw_runtime_body"] = "RAW_RUNTIME_BODY_MUST_NOT_RETURN"
            request["raw_runtime_hosting_body"] = "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN"
            request["runtime_loop_body"] = "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN"
            request["daemon_body"] = "RAW_DAEMON_BODY_MUST_NOT_RETURN"
            request["continuation_body"] = "RAW_CONTINUATION_BODY_MUST_NOT_RETURN"
            request["runtime_held_state_body"] = (
                "RAW_RUNTIME_HELD_STATE_BODY_MUST_NOT_RETURN"
            )
            request["runtime_held_reentry_body"] = (
                "RAW_RUNTIME_HELD_REENTRY_BODY_MUST_NOT_RETURN"
            )
            request["second_operation_body"] = "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN"
            request["prior_result_reentry_body"] = (
                "RAW_PRIOR_RESULT_REENTRY_BODY_MUST_NOT_RETURN"
            )
            request["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
            request["older_runtime_authority_import"] = (
                "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN"
            )
            mutated_request_before_resolve = copy.deepcopy(request)
            result = self.resolve_case(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_serialized_no_sentinels(result)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn(RUNTIME_TYPE, serialized)
        self.assertIn(RUNTIME_SCOPE, serialized)
        self.assertIn(SELECTED_COMMAND, serialized)
        self.assert_canonical_false_non_claims(result)
        self.assert_runtime_non_claims(result)
        self.assertEqual(request, mutated_request_before_resolve)
        self.assertNotEqual(request, request_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request, _paths, _artifacts = self.build_synthetic_request(root, "path")
            request_path = root / "request.json"
            self.write_json(request_path, request)
            result = resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_from_path(
                request_path
            )
            self.assert_runtime_recorded_posture(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_from_path(
                    malformed_path
                )
            )
            self.assert_blocked_with_public_code(malformed_result)

            array_path = root / "array.json"
            self.write_json(array_path, ["not", "mapping"])
            array_result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_from_path(
                    array_path
                )
            )
            self.assert_blocked_with_public_code(array_result)

            missing_result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_v0_min_from_path(
                    root / "missing.json"
                )
            )
            self.assert_blocked_with_public_code(missing_result)

            output_root = root / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_runtime_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_runtime_v0_min_result(
                    result
                )
            self.assertNotEqual(first_path, second_path)
            for output_path in (first_path, second_path):
                self.assertTrue(output_path.exists())
                self.assertIn("local_relevance_medium_read_only_runtime_v0_min", str(output_path))
                self.assert_path_not_under_forbidden_roots(output_path)
                with output_path.open("r", encoding="utf-8") as handle:
                    parsed = json.load(handle)
                self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, paths, artifacts = self.build_synthetic_request(Path(tmp), "immut")
            request["raw_runtime_body"] = "RAW_RUNTIME_BODY_MUST_NOT_RETURN"
            request["nested"] = {
                "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
                "runtime_hosting_body": "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
            }
            request_before = copy.deepcopy(request)
            paths_before = copy.deepcopy(paths)
            artifacts_before = copy.deepcopy(artifacts)
            result = self.resolve_case(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertEqual(request, request_before)
        self.assertEqual(paths, paths_before)
        self.assertEqual(artifacts, artifacts_before)
        self.assert_serialized_no_sentinels(result)

    def test_runtime_boundary_v0_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths, _artifacts = self.build_synthetic_request(Path(tmp))
            result = self.resolve_case(request)
            self.assert_runtime_recorded_posture(result)
            self.assert_v0_failure_preserved(result)
            for key, expected_code in (
                ("runtime_boundary_v0_failure_repaired", "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED"),
                ("runtime_boundary_v0_failure_hidden", "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN"),
                (
                    "runtime_boundary_v0_failure_claimed_passed",
                    "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
                ),
            ):
                with self.subTest(key=key):
                    blocked_request = copy.deepcopy(request)
                    blocked_request[key] = True
                    blocked = self.resolve_case(blocked_request)
                    self.assert_blocked_with_public_code(blocked)
                    self.assertEqual(self.block_code(blocked), expected_code)

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths, _artifacts = self.build_synthetic_request(Path(tmp))
            result = self.resolve_case(request)
        self.assert_runtime_recorded_posture(result)
        statement = self.statement(result)
        summary = self.summary(result)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["older_runtime_lineage_not_imported_as_authority"], True)
        self.assertIs(summary["older_runtime_permission_not_treated_as_current"], True)
        self.assertIs(summary["runtime_authority_not_imported"], True)
        for key in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(result["non_claims"][key], False)


if __name__ == "__main__":
    unittest.main()
