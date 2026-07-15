"""Tests for the local read-only runtime-boundary v2 successor resolver.

This test surface treats v2 as additive successor evidence. It preserves the
v0 selected-operation-execution recorded-alias ambiguity as failed lineage and
verifies that v2 blocks explicit false recorded aliases without creating
runtime, runtime hosting, loops, daemon behavior, continuation, APIs,
distributed behavior, older-runtime authority import, or follow-on work.
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

import resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2 as resolver


BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_RUNTIME_CONSIDERATION_ONLY"
SELECTED_COMMAND = "state"
RUNTIME_PERMISSION_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED"
OPERATION_EXECUTION_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED"

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

EXPECTED_WRAPPER_SECTIONS = {
    "local_relevance_medium_read_only_runtime_boundary_metadata",
    "declared_local_relevance_medium_read_only_runtime_boundary_question",
    "selected_runtime_permission_artifact_basis",
    "selected_operation_execution_artifact_basis",
    "local_relevance_medium_read_only_runtime_boundary",
    "local_relevance_medium_read_only_runtime_boundary_checks",
    "local_relevance_medium_read_only_runtime_boundary_statement",
    "local_relevance_medium_read_only_runtime_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_boundary_summary",
}

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = {
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_runtime_boundary_summary",
    "local_relevance_medium_read_only_runtime_boundary_metadata",
}

BOUNDARY_FALSE_FIELDS = (
    "runtime_created",
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

REQUEST_ONLY_FALSE_FIELDS = (
    "artifact_existence_treated_as_runtime_boundary_authority",
    "latest_file_posture_treated_as_runtime_boundary_authority",
    "repo_local_availability_treated_as_runtime_boundary_authority",
    "hidden_repo_state_used_as_runtime_boundary_content",
    "hidden_repo_state_used_as_runtime_boundary_authority",
    "deployment_created",
    "public_release_created",
    "broader_reusable_permission_created",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

STATEMENT_TRUE_FIELDS = (
    "local_relevance_medium_read_only_runtime_boundary_recorded",
    "basis_runtime_permission_artifact_preserved",
    "basis_operation_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_runtime_permission_recorded",
    "runtime_permission_created",
    "runtime_permission_local_only",
    "runtime_permission_read_only",
    "selected_operation_execution_recorded",
    "operation_execution_created",
    "operation_execution_performed",
    "operation_execution_local_only",
    "operation_execution_read_only",
    "future_runtime_may_be_considered",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
    "runtime_boundary_v0_failure_evidence_preserved",
    "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved",
)

OPERATION_EXECUTION_SECTIONS = (
    "local_relevance_medium_read_only_operation_execution",
    "local_relevance_medium_read_only_operation_execution_statement",
    "local_relevance_medium_read_only_operation_execution_summary",
)

OPERATION_EXECUTION_RECORDED_ALIASES = (
    "selected_operation_execution_recorded",
    "local_relevance_medium_read_only_operation_execution_recorded",
)

HOSTILE_SENTINELS = (
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
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
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min",
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min",
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_boundary_v0_min",
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min",
    "artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min",
    "artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min",
    "artifacts/integrity_host_v0_min_coexistence_public_api_v0_min",
    "artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min",
    "artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min",
)


class LocalRelevanceMediumReadOnlyRuntimeBoundaryV2Tests(unittest.TestCase):
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

    def runtime_permission_artifact(self) -> dict[str, Any]:
        boundary_false = {key: False for key in BOUNDARY_FALSE_FIELDS}
        runtime_permission = {
            "runtime_permission_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
            "runtime_permission_scope": "SELECTED_RUNTIME_PERMISSION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_runtime_permission_recorded": True,
            "selected_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            **boundary_false,
        }
        statement = {
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_runtime_permission_recorded": True,
            "selected_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            **boundary_false,
        }
        return {
            "result_version": resolver.RESULT_VERSION,
            "resolver_module": "resolve_local_relevance_medium_read_only_runtime_permission_v0_min",
            "outcome": RUNTIME_PERMISSION_OUTCOME,
            "failed_check_count": 0,
            "local_relevance_medium_read_only_runtime_permission": runtime_permission,
            "local_relevance_medium_read_only_runtime_permission_statement": statement,
            "local_relevance_medium_read_only_runtime_permission_summary": copy.deepcopy(statement),
            "local_relevance_medium_read_only_runtime_permission_checks": [
                {"check_name": "synthetic clean runtime permission", "passed": True}
            ],
        }

    def operation_execution_artifact(self) -> dict[str, Any]:
        boundary_false = {key: False for key in BOUNDARY_FALSE_FIELDS}
        operation_execution = {
            "operation_execution_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
            "operation_execution_scope": "SELECTED_OPERATION_EXECUTION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "selected_operation_execution_recorded": True,
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            **boundary_false,
        }
        statement = {
            "selected_command_is_state": True,
            "selected_operation_execution_recorded": True,
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            **boundary_false,
        }
        return {
            "result_version": resolver.RESULT_VERSION,
            "resolver_module": "resolve_local_relevance_medium_read_only_operation_execution_v0_min",
            "outcome": OPERATION_EXECUTION_OUTCOME,
            "failed_check_count": 0,
            "local_relevance_medium_read_only_operation_execution": operation_execution,
            "local_relevance_medium_read_only_operation_execution_statement": copy.deepcopy(statement),
            "local_relevance_medium_read_only_operation_execution_summary": copy.deepcopy(statement),
            "local_relevance_medium_read_only_operation_execution_checks": [
                {"check_name": "synthetic clean operation execution", "passed": True}
            ],
        }

    def write_synthetic_artifacts(
        self,
        root: Path,
        case_name: str = "clean",
        runtime_permission_mutator: Callable[[dict[str, Any]], None] | None = None,
        operation_execution_mutator: Callable[[dict[str, Any]], None] | None = None,
    ) -> tuple[Path, Path, dict[str, Any], dict[str, Any]]:
        runtime_permission = self.runtime_permission_artifact()
        operation_execution = self.operation_execution_artifact()
        if runtime_permission_mutator is not None:
            runtime_permission_mutator(runtime_permission)
        if operation_execution_mutator is not None:
            operation_execution_mutator(operation_execution)
        runtime_path = root / f"runtime_permission_{self.safe_json_filename(case_name)}"
        operation_path = root / f"operation_execution_{self.safe_json_filename(case_name)}"
        self.write_json(runtime_path, runtime_permission)
        self.write_json(operation_path, operation_execution)
        return runtime_path, operation_path, runtime_permission, operation_execution

    def clean_request(self, runtime_path: Path, operation_path: Path) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_request(
            selected_runtime_permission_artifact=runtime_path,
            selected_operation_execution_artifact=operation_path,
            local_relevance_medium_read_only_runtime_boundary_id=(
                "local_relevance_medium_read_only_runtime_boundary_001"
            ),
        )

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_runtime_boundary"]

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_runtime_boundary_statement"]

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return resolver.build_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_summary(result)

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        return list(result.get("local_relevance_medium_read_only_runtime_boundary_checks", []))

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
            self.assertIs(type(non_claims[key]), bool)

    def assert_runtime_boundary_non_claims(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in BOUNDARY_FALSE_FIELDS:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False)
            self.assertIs(type(boundary[key]), bool)
        for key in REQUEST_ONLY_FALSE_FIELDS:
            if key in result["non_claims"]:
                self.assertIs(result["non_claims"][key], False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_runtime_boundary_non_claims(result)

    def assert_boundary_wrapper_separated(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(key, boundary)

    def assert_statement_true_fields(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        for key in STATEMENT_TRUE_FIELDS:
            self.assertIs(statement.get(key), True, key)

    def assert_v0_failure_evidence_preserved(self, result: Mapping[str, Any]) -> None:
        locations = [
            result.get("local_relevance_medium_read_only_runtime_boundary_metadata", {}),
            result.get("local_relevance_medium_read_only_runtime_boundary_statement", {}),
            result.get("local_relevance_medium_read_only_runtime_boundary_non_meaning", {}),
            result.get("local_relevance_medium_read_only_runtime_boundary_summary", {}),
            self.summary(result),
        ]
        for key in (
            "runtime_boundary_v0_selected_operation_execution_recorded_alias_ambiguity_preserved",
            "runtime_boundary_v0_failure_evidence_preserved",
            "predecessor_failure_evidence_preserved",
        ):
            self.assertTrue(any(isinstance(location, Mapping) and location.get(key) is True for location in locations), key)
        non_meaning = result.get("local_relevance_medium_read_only_runtime_boundary_non_meaning", {})
        self.assertIs(non_meaning.get("runtime_boundary_v2_mutates_v0"), False)
        self.assertIs(non_meaning.get("runtime_boundary_v2_repairs_v0"), False)
        self.assertIs(non_meaning.get("runtime_boundary_v2_hides_v0_failure"), False)
        self.assertIs(non_meaning.get("runtime_boundary_v2_claims_v0_passed"), False)
        non_claims = result.get("non_claims", {})
        self.assertIs(non_claims.get("predecessor_failure_repaired"), False)
        self.assertIs(non_claims.get("predecessor_failure_hidden"), False)
        self.assertIs(non_claims.get("predecessor_failure_claimed_passed"), False)

    def assert_recorded_boundary_core(self, result: Mapping[str, Any], runtime_path: Path, operation_path: Path) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertEqual(self.summary(result)["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assertTrue(EXPECTED_WRAPPER_SECTIONS.issubset(result.keys()))
        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_id"], "local_relevance_medium_read_only_runtime_boundary_001")
        self.assertEqual(boundary["boundary_type"], BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.RESULT_VERSION)
        self.assertEqual(boundary["boundary_scope"], BOUNDARY_SCOPE)
        self.assert_same_or_stable_artifact_path(boundary["basis_runtime_permission_artifact"], runtime_path)
        self.assertEqual(boundary["basis_runtime_permission_outcome"], RUNTIME_PERMISSION_OUTCOME)
        self.assertEqual(boundary["basis_runtime_permission_result_version"], resolver.RESULT_VERSION)
        self.assertEqual(boundary["basis_runtime_permission_failed_check_count"], 0)
        self.assert_same_or_stable_artifact_path(boundary["basis_operation_execution_artifact"], operation_path)
        self.assertEqual(boundary["basis_operation_execution_outcome"], OPERATION_EXECUTION_OUTCOME)
        self.assertEqual(boundary["basis_operation_execution_result_version"], resolver.RESULT_VERSION)
        self.assertEqual(boundary["basis_operation_execution_failed_check_count"], 0)
        self.assertEqual(boundary["selected_command"], SELECTED_COMMAND)
        self.assertIs(boundary["selected_command_is_state"], True)
        self.assertIs(boundary["selected_runtime_permission_recorded"], True)
        self.assertIs(boundary["runtime_permission_created"], True)
        self.assertIs(boundary["runtime_permission_local_only"], True)
        self.assertIs(boundary["runtime_permission_read_only"], True)
        self.assertIs(boundary["selected_operation_execution_recorded"], True)
        self.assertIs(boundary["operation_execution_created"], True)
        self.assertIs(boundary["operation_execution_performed"], True)
        self.assertIs(boundary["operation_execution_local_only"], True)
        self.assertIs(boundary["operation_execution_read_only"], True)
        self.assertIs(boundary["future_runtime_may_be_considered"], True)
        self.assert_runtime_boundary_non_claims(result)
        self.assert_boundary_wrapper_separated(result)
        self.assert_statement_true_fields(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_v0_failure_evidence_preserved(result)

    def assert_output_path_not_under_prior_roots(self, path: Path) -> None:
        resolved = path.resolve()
        for root in FORBIDDEN_OUTPUT_ROOTS:
            forbidden = (REPO_ROOT / root).resolve()
            self.assertFalse(resolved == forbidden or forbidden in resolved.parents, root)

    def assert_no_hostile_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def resolve_clean_synthetic(self, temp_root: Path) -> tuple[dict[str, Any], Path, Path]:
        runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(temp_root)
        request = self.clean_request(runtime_path, operation_path)
        result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(request)
        return result, runtime_path, operation_path

    def test_public_api_constants_and_builder_defaults(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2",
            "resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_from_path",
            "write_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result",
            "build_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_summary",
            "build_declared_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
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
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min_v2"
            )
        )
        self.assertIn(BOUNDARY_TYPE, resolver.SUPPORTED_BOUNDARY_TYPE_VALUES)
        self.assertIn(BOUNDARY_SCOPE, resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, SELECTED_COMMAND)
        for code in (
            "SELECTED_OPERATION_EXECUTION_NOT_RECORDED",
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "RUNTIME_AUTHORITY_IMPORTED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        for key in (
            "runtime_created",
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
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_BLOCKED",
            },
        )

        request = resolver.build_declared_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_request()
        self.assertTrue(
            str(request["selected_runtime_permission_artifact"]).endswith(
                "local_relevance_medium_read_only_runtime_permission_reference_review_001__local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
            )
        )
        self.assertTrue(
            str(request["selected_operation_execution_artifact"]).endswith(
                "local_relevance_medium_read_only_operation_execution_reference_review_001__local_relevance_medium_read_only_operation_execution_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        for key in (
            "consumed_request_reopened",
            "authorization_token_reused",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
        ):
            self.assertIs(request["declared_non_claims"][key], False)

        with tempfile.TemporaryDirectory() as temp_dir:
            result, _, _ = self.resolve_clean_synthetic(Path(temp_dir))
            self.assert_v0_failure_evidence_preserved(result)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result, runtime_path, operation_path = self.resolve_clean_synthetic(Path(temp_dir))
            self.assertIsInstance(result, dict)
            self.assert_recorded_boundary_core(result, runtime_path, operation_path)

    def test_v2_blocks_selected_operation_execution_recorded_alias_ambiguity(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            cases: list[tuple[str, str, str]] = []
            for section in OPERATION_EXECUTION_SECTIONS:
                for alias in OPERATION_EXECUTION_RECORDED_ALIASES:
                    cases.append((section, alias, f"{section} {alias} false"))
            cases.append(
                (
                    "local_relevance_medium_read_only_operation_execution",
                    "local_relevance_medium_read_only_operation_execution_recorded",
                    "same section conflicting aliases",
                )
            )

            for index, (section, alias, label) in enumerate(cases):
                with self.subTest(label=label):
                    def mutate_operation(artifact: dict[str, Any], section: str = section, alias: str = alias) -> None:
                        artifact[section][alias] = False
                        other_alias = next(key for key in OPERATION_EXECUTION_RECORDED_ALIASES if key != alias)
                        artifact[section][other_alias] = True

                    runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(
                        temp_root,
                        self.safe_json_filename(label, index),
                        operation_execution_mutator=mutate_operation,
                    )
                    request = self.clean_request(runtime_path, operation_path)
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "SELECTED_OPERATION_EXECUTION_NOT_RECORDED")
                    self.assert_v0_failure_evidence_preserved(result)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_RUNTIME_PERMISSION_ARTIFACT.exists() or not DEFAULT_OPERATION_EXECUTION_ARTIFACT.exists():
            self.skipTest("default live runtime permission and operation execution artifacts are not both present")
        request = resolver.build_declared_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_request()
        result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(request)
        self.assert_recorded_boundary_core(result, DEFAULT_RUNTIME_PERMISSION_ARTIFACT, DEFAULT_OPERATION_EXECUTION_ARTIFACT)

    def test_closure_token_and_older_runtime_import_blocking(self) -> None:
        top_level_cases = (
            ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
            ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
            ("older_runtime_lineage_imported_as_authority", "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY"),
            ("older_runtime_permission_treated_as_current", "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT"),
            ("runtime_authority_imported", "RUNTIME_AUTHORITY_IMPORTED"),
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(Path(temp_dir))
            for key, expected_code in top_level_cases:
                with self.subTest(top_level=key):
                    request = self.clean_request(runtime_path, operation_path)
                    request[key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
            for key, _ in top_level_cases:
                for value in (True, "false", None):
                    with self.subTest(declared_non_claim=key, value=value):
                        request = self.clean_request(runtime_path, operation_path)
                        request["declared_non_claims"][key] = value
                        result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(request)
                        self.assert_blocked_with_public_code(result)
                        self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                with self.subTest(declared_non_claim_missing=key):
                    request = self.clean_request(runtime_path, operation_path)
                    del request["declared_non_claims"][key]
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_required_false_non_claims_canonicalize_after_flipped_input(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(Path(temp_dir))
            clean_request = self.clean_request(runtime_path, operation_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_runtime_boundary_non_claims(result)

    def test_representative_blocking_behavior(self) -> None:
        def no_change(_: dict[str, Any]) -> None:
            return None

        def runtime_mutator(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            def mutate(artifact: dict[str, Any]) -> None:
                artifact["local_relevance_medium_read_only_runtime_permission"][field] = value
                artifact["local_relevance_medium_read_only_runtime_permission_statement"][field] = value
                artifact["local_relevance_medium_read_only_runtime_permission_summary"][field] = value
            return mutate

        def operation_mutator(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            def mutate(artifact: dict[str, Any]) -> None:
                for section in OPERATION_EXECUTION_SECTIONS:
                    artifact[section][field] = value
            return mutate

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            cases: list[tuple[str, str | None, Callable[[dict[str, Any]], None] | None, Callable[[dict[str, Any]], None] | None, Callable[[dict[str, Any]], None] | None, bool, Any]] = [
                ("explicit block intent", None, None, None, lambda request: request.__setitem__("local_relevance_medium_read_only_runtime_boundary_intent", "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY"), False, None),
                ("unsupported intent", None, None, None, lambda request: request.__setitem__("local_relevance_medium_read_only_runtime_boundary_intent", "UNSUPPORTED"), False, None),
                ("runtime permission artifact not recorded", None, lambda artifact: artifact.__setitem__("outcome", "NOPE"), None, None, False, None),
                ("runtime permission artifact failed checks present", None, lambda artifact: artifact.__setitem__("failed_check_count", 1), None, None, False, None),
                ("runtime permission artifact version not 0.1.0", None, lambda artifact: artifact.__setitem__("result_version", "9.9.9"), None, None, False, None),
                ("operation execution artifact not recorded", None, None, lambda artifact: artifact.__setitem__("outcome", "NOPE"), None, False, None),
                ("operation execution artifact failed checks present", None, None, lambda artifact: artifact.__setitem__("failed_check_count", 1), None, False, None),
                ("operation execution artifact version not 0.1.0", None, None, lambda artifact: artifact.__setitem__("result_version", "9.9.9"), None, False, None),
                ("selected operation execution alias false", "SELECTED_OPERATION_EXECUTION_NOT_RECORDED", None, operation_mutator("selected_operation_execution_recorded", False), None, False, None),
                ("selected command missing", None, None, None, lambda request: request.pop("selected_command", None), False, None),
                ("selected command not state", None, None, None, lambda request: request.__setitem__("selected_command", "status"), False, None),
                ("boundary type missing", None, None, None, lambda request: request.pop("boundary_type", None), False, None),
                ("boundary type wrong", None, None, None, lambda request: request.__setitem__("boundary_type", "LOCAL_RELEVANCE_MEDIUM_RUNTIME"), False, None),
                ("boundary scope missing", None, None, None, lambda request: request.pop("boundary_scope", None), False, None),
                ("boundary scope wrong", None, None, None, lambda request: request.__setitem__("boundary_scope", "RUNTIME"), False, None),
                ("runtime permission not created", None, runtime_mutator("runtime_permission_created", False), None, None, False, None),
                ("runtime permission local only not true", None, runtime_mutator("runtime_permission_local_only", False), None, None, False, None),
                ("runtime permission read only not true", None, runtime_mutator("runtime_permission_read_only", False), None, None, False, None),
                ("operation execution not created", None, None, operation_mutator("operation_execution_created", False), None, False, None),
                ("operation execution not performed", None, None, operation_mutator("operation_execution_performed", False), None, False, None),
                ("operation execution local only not true", None, None, operation_mutator("operation_execution_local_only", False), None, False, None),
                ("operation execution read only not true", None, None, operation_mutator("operation_execution_read_only", False), None, False, None),
            ]
            for field in BOUNDARY_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS:
                cases.append((field, None, None, None, lambda request, field=field: request.__setitem__(field, True), False, None))
            cases.extend(
                [
                    ("runtime permission artifact path missing", None, None, None, lambda request: request.pop("selected_runtime_permission_artifact", None), False, None),
                    ("operation execution artifact path missing", None, None, None, lambda request: request.pop("selected_operation_execution_artifact", None), False, None),
                    ("runtime permission artifact unreadable", None, None, None, lambda request: request.__setitem__("selected_runtime_permission_artifact", root / "missing_runtime.json"), False, None),
                    ("operation execution artifact unreadable", None, None, None, lambda request: request.__setitem__("selected_operation_execution_artifact", root / "missing_operation.json"), False, None),
                    ("runtime permission artifact array", None, None, None, None, True, "runtime"),
                    ("operation execution artifact array", None, None, None, None, True, "operation"),
                    ("required non-claim missing", "NON_CLAIM_MISSING_OR_FLIPPED", None, None, lambda request: request["declared_non_claims"].pop("runtime_created", None), False, None),
                ]
            )
            for index, (label, exact_code, runtime_edit, operation_edit, request_edit, artifact_array, array_kind) in enumerate(cases):
                with self.subTest(label=label):
                    runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(
                        root,
                        self.safe_json_filename(label, index),
                        runtime_permission_mutator=runtime_edit,
                        operation_execution_mutator=operation_edit,
                    )
                    if artifact_array and array_kind == "runtime":
                        self.write_json(runtime_path, [])
                    if artifact_array and array_kind == "operation":
                        self.write_json(operation_path, [])
                    request = self.clean_request(runtime_path, operation_path)
                    if request_edit is not None:
                        request_edit(request)
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(request)
                    self.assert_blocked_with_public_code(result)
                    if exact_code is not None:
                        self.assertEqual(self.block_code(result), exact_code)
                    self.assert_v0_failure_evidence_preserved(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result, _, _ = self.resolve_clean_synthetic(Path(temp_dir))
            boundary = self.boundary(result)
            self.assertEqual(boundary["boundary_type"], BOUNDARY_TYPE)
            self.assertEqual(boundary["boundary_scope"], BOUNDARY_SCOPE)
            self.assertEqual(boundary["selected_command"], SELECTED_COMMAND)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            for outcome in (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_BLOCKED",
            ):
                self.assertIn(outcome, resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn(resolver.OUTCOME_RECORDED, serialized)
            self.assertIn(BOUNDARY_TYPE, serialized)
            self.assertIn(BOUNDARY_SCOPE, serialized)
            self.assertIn('"state"', serialized)
            self.assertIn(resolver.RESOLVER_MODULE, serialized)
            self.assertNotIn("[REDACTED_RUNTIME_BOUNDARY_CONTENT]", serialized)

    def test_raw_hidden_and_older_runtime_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            original_request: dict[str, Any] | None = None

            def mutate_runtime(artifact: dict[str, Any]) -> None:
                artifact["raw_runtime_permission_body"] = HOSTILE_SENTINELS[1]
                artifact["local_relevance_medium_read_only_runtime_permission"]["raw_runtime_body"] = HOSTILE_SENTINELS[2]

            def mutate_operation(artifact: dict[str, Any]) -> None:
                artifact["raw_operation_execution_body"] = HOSTILE_SENTINELS[3]
                artifact["local_relevance_medium_read_only_operation_execution"]["hidden_repo_state"] = HOSTILE_SENTINELS[-1]

            runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(
                root,
                "hostile",
                runtime_permission_mutator=mutate_runtime,
                operation_execution_mutator=mutate_operation,
            )
            request = self.clean_request(runtime_path, operation_path)
            request["raw_runtime_boundary_body"] = HOSTILE_SENTINELS[0]
            request["runtime_held_state_body"] = HOSTILE_SENTINELS[7]
            request["older_runtime_authority_body"] = HOSTILE_SENTINELS[-2]
            original_request = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(request)
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
            self.assert_no_hostile_sentinels(result)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn(BOUNDARY_TYPE, serialized)
            self.assertIn(BOUNDARY_SCOPE, serialized)
            self.assertIn(SELECTED_COMMAND, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assert_runtime_boundary_non_claims(result)
            self.assertEqual(request, original_request)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(root)
            request = self.clean_request(runtime_path, operation_path)
            request_path = self.write_json(root / "request.json", request)
            result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_from_path(request_path)
            self.assert_recorded_boundary_core(result, runtime_path, operation_path)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            try:
                malformed_result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_from_path(
                    malformed_path
                )
            except resolver.LocalRelevanceMediumReadOnlyRuntimeBoundaryV0MinV2Error:
                malformed_result = None
            if malformed_result is not None:
                self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)

            array_path = self.write_json(root / "array.json", [])
            array_result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_from_path(array_path)
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)

            try:
                missing_result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_from_path(
                    root / "missing_request.json"
                )
            except resolver.LocalRelevanceMediumReadOnlyRuntimeBoundaryV0MinV2Error:
                missing_result = None
            if missing_result is not None:
                self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)

            output_root = root / "artifacts" / (
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min_v2"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result(result)
                second_path = resolver.write_local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result(result)
            self.assertTrue(first_path.parent.exists())
            self.assertTrue(second_path.parent.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn("local_relevance_medium_read_only_runtime_boundary_v0_min_v2", str(first_path))
            self.assert_output_path_not_under_prior_roots(first_path)
            self.assert_output_path_not_under_prior_roots(second_path)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            runtime_path, operation_path, runtime_artifact, operation_artifact = self.write_synthetic_artifacts(root)
            request = self.clean_request(runtime_path, operation_path)
            request["nested_payload"] = {"raw_runtime_body": HOSTILE_SENTINELS[2]}
            request_before = copy.deepcopy(request)
            runtime_before = copy.deepcopy(runtime_artifact)
            operation_before = copy.deepcopy(operation_artifact)
            result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_v2(request)
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assertEqual(request, request_before)
            self.assertEqual(runtime_artifact, runtime_before)
            self.assertEqual(operation_artifact, operation_before)
            self.assertEqual(request["selected_runtime_permission_artifact"], request_before["selected_runtime_permission_artifact"])
            self.assertEqual(request["selected_operation_execution_artifact"], request_before["selected_operation_execution_artifact"])
            self.assertEqual(request["selected_command"], SELECTED_COMMAND)
            self.assertEqual(request["boundary_type"], BOUNDARY_TYPE)
            self.assertEqual(request["boundary_scope"], BOUNDARY_SCOPE)

    def test_predecessor_and_v0_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result, _, _ = self.resolve_clean_synthetic(Path(temp_dir))
            summary = self.summary(result)
            self.assert_v0_failure_evidence_preserved(result)
            self.assertIs(self.statement(result).get("predecessor_failure_evidence_preserved"), True)
            self.assertIs(summary.get("predecessor_failure_evidence_preserved"), True)
            self.assertIs(summary.get("result_level_non_claims_canonical_false"), True)
            self.assertIs(summary.get("consumed_request_token_remains_closed"), True)
            self.assertIs(summary.get("authorization_token_reuse_blocked"), True)
            self.assertIs(summary.get("older_runtime_lineage_not_imported_as_authority"), True)
            self.assertIs(summary.get("older_runtime_permission_not_treated_as_current"), True)
            self.assertIs(summary.get("runtime_authority_not_imported"), True)
            self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
            self.assertIs(result["non_claims"]["authorization_token_reused"], False)
            self.assertIs(result["non_claims"]["older_runtime_lineage_imported_as_authority"], False)
            self.assertIs(result["non_claims"]["older_runtime_permission_treated_as_current"], False)
            self.assertIs(result["non_claims"]["runtime_authority_imported"], False)


if __name__ == "__main__":
    unittest.main()
