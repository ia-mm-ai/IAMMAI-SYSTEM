"""Executable tests for the local relevance medium read-only runtime boundary.

The target resolver records one selected-state, local, read-only runtime
boundary only. These tests keep the boundary object separate from the resolver
wrapper and verify that no runtime, runtime hosting, runtime loop, daemon,
continuation, re-entry, public API, distributed behavior, registry, search,
ranking, older-runtime authority import, or follow-on work is created.
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

import resolve_local_relevance_medium_read_only_runtime_boundary_v0_min as resolver


DEFAULT_RUNTIME_PERMISSION_ARTIFACT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_permission_v0_min/local_relevance_medium_read_only_runtime_permission_"
    "reference_review_001__local_relevance_medium_read_only_runtime_permission_"
    "v0_min_result.json"
)
DEFAULT_OPERATION_EXECUTION_ARTIFACT = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_execution_v0_min/local_relevance_medium_read_only_operation_execution_"
    "reference_review_001__local_relevance_medium_read_only_operation_execution_"
    "v0_min_result.json"
)
EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = [
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_permission_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_permission_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_result_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_performed_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_performed_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_command_execution_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_command_execution_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_packet_body_exposure_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v2_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_result_object_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_result_object_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_payload_return_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_payload_return_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_surface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_reusable_lookup_permission_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_layer_closure_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_loop_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_hosting_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_ongoing_runtime_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_reusable_runtime_permission_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_post_runtime_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_daemon_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_continuation_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
]

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

BOUNDARY_FALSE_FIELDS = [
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
]

STATEMENT_TRUE_FIELDS = [
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
]

HOSTILE_SENTINELS = [
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
]


class LocalRelevanceMediumReadOnlyRuntimeBoundaryV0MinTest(unittest.TestCase):
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

    def write_json(self, path: Path, data: object) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
        return path

    def runtime_permission_artifact(self) -> dict[str, Any]:
        runtime_permission = {
            "runtime_permission_id": "local_relevance_medium_read_only_runtime_permission_001",
            "runtime_permission_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
            "runtime_permission_version": "0.1.0",
            "runtime_permission_scope": "SELECTED_RUNTIME_PERMISSION_ONLY",
            "selected_command": "state",
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
        }
        for key in BOUNDARY_FALSE_FIELDS:
            runtime_permission[key] = False

        statement = {
            "local_relevance_medium_read_only_runtime_permission_recorded": True,
            "selected_command_preserved": True,
            "selected_command_is_state": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        summary = {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 12,
            **runtime_permission,
            **statement,
        }
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 12,
            "local_relevance_medium_read_only_runtime_permission": runtime_permission,
            "local_relevance_medium_read_only_runtime_permission_statement": statement,
            "local_relevance_medium_read_only_runtime_permission_summary": summary,
            "local_relevance_medium_read_only_runtime_permission_checks": [
                {"check_name": "synthetic_runtime_permission_clean", "passed": True}
            ],
        }

    def operation_execution_artifact(self) -> dict[str, Any]:
        operation_execution = {
            "operation_execution_id": "local_relevance_medium_read_only_operation_execution_001",
            "operation_execution_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
            "operation_execution_version": "0.1.0",
            "operation_execution_scope": "SELECTED_OPERATION_EXECUTION_ONLY",
            "selected_command": "state",
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
        }
        for key in BOUNDARY_FALSE_FIELDS:
            operation_execution[key] = False

        statement = {
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "selected_command_preserved": True,
            "selected_command_is_state": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        summary = {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 12,
            **operation_execution,
            **statement,
        }
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 12,
            "local_relevance_medium_read_only_operation_execution": operation_execution,
            "local_relevance_medium_read_only_operation_execution_statement": statement,
            "local_relevance_medium_read_only_operation_execution_summary": summary,
            "local_relevance_medium_read_only_operation_execution_checks": [
                {"check_name": "synthetic_operation_execution_clean", "passed": True}
            ],
        }

    def write_synthetic_artifacts(
        self,
        root: Path,
        case_name: str = "clean",
        runtime_permission_mutator: Callable[[dict[str, Any]], None] | None = None,
        operation_execution_mutator: Callable[[dict[str, Any]], None] | None = None,
    ) -> tuple[Path, Path, dict[str, Any], dict[str, Any]]:
        runtime_artifact = self.runtime_permission_artifact()
        operation_artifact = self.operation_execution_artifact()
        if runtime_permission_mutator is not None:
            runtime_permission_mutator(runtime_artifact)
        if operation_execution_mutator is not None:
            operation_execution_mutator(operation_artifact)
        runtime_path = root / self.safe_json_filename(f"{case_name}_runtime_permission")
        operation_path = root / self.safe_json_filename(f"{case_name}_operation_execution")
        self.write_json(runtime_path, runtime_artifact)
        self.write_json(operation_path, operation_artifact)
        return runtime_path, operation_path, runtime_artifact, operation_artifact

    def clean_request(self, runtime_permission_path: Path, operation_execution_path: Path) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_runtime_boundary_v0_min_request(
            selected_runtime_permission_artifact=runtime_permission_path,
            selected_operation_execution_artifact=operation_execution_path,
        )

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_runtime_boundary_summary"]

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        return list(result.get("local_relevance_medium_read_only_runtime_boundary_checks", []))

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        summary = self.summary(result)
        return int(summary.get("failed_check_count", 0))

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        summary = self.summary(result)
        return int(summary.get("passed_check_count", 0))

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_runtime_boundary"]

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_runtime_boundary_statement"]

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        code = block.get("code")
        if code is not None:
            return str(code)
        block_code = block.get("block_code")
        if block_code is not None:
            return str(block_code)
        return None

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_same_or_stable_artifact_path(self, actual: object, expected: object) -> None:
        actual_path = Path(str(actual))
        expected_path = Path(str(expected))
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
        non_claims = result["non_claims"]
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIsInstance(non_claims[key], bool)
            self.assertIs(non_claims[key], False)

    def assert_runtime_boundary_non_claims(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in BOUNDARY_FALSE_FIELDS:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False, key)

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
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)

    def assert_recorded_boundary_core(
        self,
        result: Mapping[str, Any],
        runtime_permission_path: Path,
        operation_execution_path: Path,
    ) -> None:
        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_id"], "local_relevance_medium_read_only_runtime_boundary_001")
        self.assertEqual(boundary["boundary_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY")
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(boundary["boundary_scope"], "SELECTED_RUNTIME_CONSIDERATION_ONLY")
        self.assert_same_or_stable_artifact_path(boundary["basis_runtime_permission_artifact"], runtime_permission_path)
        self.assertEqual(
            boundary["basis_runtime_permission_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED",
        )
        self.assertEqual(boundary["basis_runtime_permission_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_runtime_permission_failed_check_count"], 0)
        self.assert_same_or_stable_artifact_path(boundary["basis_operation_execution_artifact"], operation_execution_path)
        self.assertEqual(
            boundary["basis_operation_execution_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
        )
        self.assertEqual(boundary["basis_operation_execution_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_operation_execution_failed_check_count"], 0)
        self.assertEqual(boundary["selected_command"], "state")
        for key in (
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
        ):
            self.assertIs(boundary[key], True, key)
        self.assert_runtime_boundary_non_claims(result)
        self.assert_boundary_wrapper_separated(result)

    def assert_clean_recorded_result(
        self,
        result: Mapping[str, Any],
        runtime_permission_path: Path,
        operation_execution_path: Path,
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        summary = self.summary(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(
            result["local_relevance_medium_read_only_runtime_boundary_metadata"][
                "local_relevance_medium_read_only_runtime_boundary_id"
            ],
            "local_relevance_medium_read_only_runtime_boundary_001",
        )
        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)
        self.assert_recorded_boundary_core(result, runtime_permission_path, operation_execution_path)
        self.assert_statement_true_fields(result)
        self.assert_canonical_false_non_claims(result)

    def assert_output_path_not_under_prior_roots(self, path: Path) -> None:
        candidate = path
        for root in FORBIDDEN_OUTPUT_ROOTS:
            self.assertNotEqual(candidate, root)
            try:
                self.assertFalse(candidate.is_relative_to(root))
            except ValueError:
                pass

    def assert_no_hostile_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def test_public_api_constants_and_builder_defaults(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_runtime_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_runtime_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_runtime_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_runtime_boundary_v0_min_request",
        ):
            self.assertTrue(hasattr(resolver, name), name)

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
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_local_relevance_medium_read_only_runtime_boundary_v0_min")
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY", resolver.SUPPORTED_BOUNDARY_TYPE_VALUES)
        self.assertIn("SELECTED_RUNTIME_CONSIDERATION_ONLY", resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, "state")

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

        for code in (
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "RUNTIME_AUTHORITY_IMPORTED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_BLOCKED",
            },
        )

        request = resolver.build_declared_local_relevance_medium_read_only_runtime_boundary_v0_min_request()
        self.assertTrue(
            str(request["selected_runtime_permission_artifact"]).endswith(
                "local_relevance_medium_read_only_runtime_permission_reference_review_001__"
                "local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
            )
        )
        self.assertTrue(
            str(request["selected_operation_execution_artifact"]).endswith(
                "local_relevance_medium_read_only_operation_execution_reference_review_001__"
                "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], "state")
        for key in (
            "consumed_request_reopened",
            "authorization_token_reused",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
        ):
            self.assertIs(request["declared_non_claims"][key], False)

        self.assert_output_path_not_under_prior_roots(Path(resolver.OUTPUT_ROOT))

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(tmp_path)
            request = self.clean_request(runtime_path, operation_path)

            result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min(request)

            self.assert_clean_recorded_result(result, runtime_path, operation_path)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_RUNTIME_PERMISSION_ARTIFACT.exists() or not DEFAULT_OPERATION_EXECUTION_ARTIFACT.exists():
            self.skipTest("default runtime permission or operation execution live artifact is absent")

        request = resolver.build_declared_local_relevance_medium_read_only_runtime_boundary_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min(request)

        self.assert_clean_recorded_result(
            result,
            DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
            DEFAULT_OPERATION_EXECUTION_ARTIFACT,
        )
        boundary = self.boundary(result)
        self.assert_same_or_stable_artifact_path(
            boundary["basis_runtime_permission_artifact"],
            DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
        )
        self.assert_same_or_stable_artifact_path(
            boundary["basis_operation_execution_artifact"],
            DEFAULT_OPERATION_EXECUTION_ARTIFACT,
        )

    def test_closure_token_and_older_runtime_import_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(Path(tmp))
            top_level_cases = [
                ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
                ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
                ("older_runtime_lineage_imported_as_authority", "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY"),
                ("older_runtime_permission_treated_as_current", "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT"),
                ("runtime_authority_imported", "RUNTIME_AUTHORITY_IMPORTED"),
            ]
            for key, expected_code in top_level_cases:
                with self.subTest(top_level=key):
                    request = self.clean_request(runtime_path, operation_path)
                    request[key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

            for key in (
                "consumed_request_reopened",
                "authorization_token_reused",
                "older_runtime_lineage_imported_as_authority",
                "older_runtime_permission_treated_as_current",
                "runtime_authority_imported",
            ):
                for value in (True, "false", None):
                    with self.subTest(declared_non_claim=key, value=repr(value)):
                        request = self.clean_request(runtime_path, operation_path)
                        request["declared_non_claims"][key] = value
                        result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min(request)
                        self.assert_blocked_with_public_code(result)
                        self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                with self.subTest(declared_non_claim=key, value="missing"):
                    request = self.clean_request(runtime_path, operation_path)
                    request["declared_non_claims"].pop(key)
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_required_false_non_claims_canonicalize_after_flipped_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(Path(tmp))
            clean_request = self.clean_request(runtime_path, operation_path)

            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_canonical_false_non_claims(result)
                    self.assert_runtime_boundary_non_claims(result)

    def test_representative_blocking_behavior(self) -> None:
        def request_case(
            tmp_path: Path,
            name: str,
            request_mutator: Callable[[dict[str, Any]], None] | None = None,
            runtime_mutator: Callable[[dict[str, Any]], None] | None = None,
            operation_mutator: Callable[[dict[str, Any]], None] | None = None,
            runtime_json: object | None = None,
            operation_json: object | None = None,
        ) -> dict[str, Any]:
            runtime_path, operation_path, runtime_artifact, operation_artifact = self.write_synthetic_artifacts(
                tmp_path,
                self.safe_json_filename(name).removesuffix(".json"),
                runtime_mutator,
                operation_mutator,
            )
            if runtime_json is not None:
                self.write_json(runtime_path, runtime_json)
            if operation_json is not None:
                self.write_json(operation_path, operation_json)
            request = self.clean_request(runtime_path, operation_path)
            self.assertIsInstance(runtime_artifact, dict)
            self.assertIsInstance(operation_artifact, dict)
            if request_mutator is not None:
                request_mutator(request)
            return request

        false_field_cases = [
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
            "artifact_existence_treated_as_runtime_boundary_authority",
            "latest_file_posture_treated_as_runtime_boundary_authority",
            "repo_local_availability_treated_as_runtime_boundary_authority",
            "hidden_repo_state_used_as_runtime_boundary_content",
            "hidden_repo_state_used_as_runtime_boundary_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ]

        def set_runtime_permission_object(artifact: dict[str, Any], key: str, value: Any) -> None:
            artifact["local_relevance_medium_read_only_runtime_permission"][key] = value
            artifact["local_relevance_medium_read_only_runtime_permission_summary"][key] = value

        def set_operation_execution_object(artifact: dict[str, Any], key: str, value: Any) -> None:
            artifact["local_relevance_medium_read_only_operation_execution"][key] = value
            artifact["local_relevance_medium_read_only_operation_execution_summary"][key] = value

        cases: list[tuple[str, Callable[[Path], object]]] = [
            (
                "explicit block intent",
                lambda tmp: request_case(
                    tmp,
                    "explicit_block_intent",
                    lambda req: req.update(
                        {
                            "local_relevance_medium_read_only_runtime_boundary_intent":
                            "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY"
                        }
                    ),
                ),
            ),
            ("missing request", lambda tmp: {}),
            ("non-mapping request", lambda tmp: ["not", "a", "mapping"]),
            (
                "unsupported intent",
                lambda tmp: request_case(
                    tmp,
                    "unsupported_intent",
                    lambda req: req.update(
                        {"local_relevance_medium_read_only_runtime_boundary_intent": "UNSUPPORTED_INTENT"}
                    ),
                ),
            ),
            (
                "runtime permission artifact path missing",
                lambda tmp: request_case(tmp, "runtime_permission_path_missing", lambda req: req.pop("selected_runtime_permission_artifact")),
            ),
            (
                "runtime permission artifact unreadable",
                lambda tmp: request_case(
                    tmp,
                    "runtime_permission_unreadable",
                    lambda req: req.update({"selected_runtime_permission_artifact": str(tmp / "missing_runtime.json")}),
                ),
            ),
            (
                "runtime permission artifact JSON array instead of object",
                lambda tmp: request_case(tmp, "runtime_permission_array", runtime_json=[]),
            ),
            (
                "runtime permission artifact not recorded",
                lambda tmp: request_case(
                    tmp,
                    "runtime_permission_not_recorded",
                    runtime_mutator=lambda artifact: artifact.update({"outcome": "NOT_RECORDED"}),
                ),
            ),
            (
                "runtime permission artifact failed checks present",
                lambda tmp: request_case(
                    tmp,
                    "runtime_permission_failed_checks",
                    runtime_mutator=lambda artifact: artifact.update({"failed_check_count": 1}),
                ),
            ),
            (
                "runtime permission artifact version not 0.1.0",
                lambda tmp: request_case(
                    tmp,
                    "runtime_permission_wrong_version",
                    runtime_mutator=lambda artifact: artifact.update({"result_version": "9.9.9"}),
                ),
            ),
            (
                "operation execution artifact path missing",
                lambda tmp: request_case(tmp, "operation_execution_path_missing", lambda req: req.pop("selected_operation_execution_artifact")),
            ),
            (
                "operation execution artifact unreadable",
                lambda tmp: request_case(
                    tmp,
                    "operation_execution_unreadable",
                    lambda req: req.update({"selected_operation_execution_artifact": str(tmp / "missing_operation.json")}),
                ),
            ),
            (
                "operation execution artifact JSON array instead of object",
                lambda tmp: request_case(tmp, "operation_execution_array", operation_json=[]),
            ),
            (
                "operation execution artifact not recorded",
                lambda tmp: request_case(
                    tmp,
                    "operation_execution_not_recorded",
                    operation_mutator=lambda artifact: artifact.update({"outcome": "NOT_RECORDED"}),
                ),
            ),
            (
                "operation execution artifact failed checks present",
                lambda tmp: request_case(
                    tmp,
                    "operation_execution_failed_checks",
                    operation_mutator=lambda artifact: artifact.update({"failed_check_count": 1}),
                ),
            ),
            (
                "operation execution artifact version not 0.1.0",
                lambda tmp: request_case(
                    tmp,
                    "operation_execution_wrong_version",
                    operation_mutator=lambda artifact: artifact.update({"result_version": "9.9.9"}),
                ),
            ),
            ("selected command missing", lambda tmp: request_case(tmp, "selected_command_missing", lambda req: req.pop("selected_command"))),
            (
                "selected command not state",
                lambda tmp: request_case(tmp, "selected_command_not_state", lambda req: req.update({"selected_command": "lookup"})),
            ),
            (
                "selected runtime permission not recorded",
                lambda tmp: request_case(
                    tmp,
                    "selected_runtime_permission_not_recorded",
                    runtime_mutator=lambda artifact: set_runtime_permission_object(
                        artifact, "local_relevance_medium_read_only_runtime_permission_recorded", False
                    ),
                ),
            ),
            (
                "runtime permission not created",
                lambda tmp: request_case(
                    tmp,
                    "runtime_permission_not_created",
                    runtime_mutator=lambda artifact: set_runtime_permission_object(artifact, "runtime_permission_created", False),
                ),
            ),
            (
                "runtime permission local only not true",
                lambda tmp: request_case(
                    tmp,
                    "runtime_permission_local_only_not_true",
                    runtime_mutator=lambda artifact: set_runtime_permission_object(artifact, "runtime_permission_local_only", False),
                ),
            ),
            (
                "runtime permission read only not true",
                lambda tmp: request_case(
                    tmp,
                    "runtime_permission_read_only_not_true",
                    runtime_mutator=lambda artifact: set_runtime_permission_object(artifact, "runtime_permission_read_only", False),
                ),
            ),
            (
                "selected operation execution not recorded",
                lambda tmp: request_case(
                    tmp,
                    "selected_operation_execution_not_recorded",
                    operation_mutator=lambda artifact: set_operation_execution_object(
                        artifact, "local_relevance_medium_read_only_operation_execution_recorded", False
                    ),
                ),
            ),
            (
                "operation execution not created",
                lambda tmp: request_case(
                    tmp,
                    "operation_execution_not_created",
                    operation_mutator=lambda artifact: set_operation_execution_object(artifact, "operation_execution_created", False),
                ),
            ),
            (
                "operation execution not performed",
                lambda tmp: request_case(
                    tmp,
                    "operation_execution_not_performed",
                    operation_mutator=lambda artifact: set_operation_execution_object(artifact, "operation_execution_performed", False),
                ),
            ),
            (
                "operation execution local only not true",
                lambda tmp: request_case(
                    tmp,
                    "operation_execution_local_only_not_true",
                    operation_mutator=lambda artifact: set_operation_execution_object(artifact, "operation_execution_local_only", False),
                ),
            ),
            (
                "operation execution read only not true",
                lambda tmp: request_case(
                    tmp,
                    "operation_execution_read_only_not_true",
                    operation_mutator=lambda artifact: set_operation_execution_object(artifact, "operation_execution_read_only", False),
                ),
            ),
            (
                "future runtime may not be considered",
                lambda tmp: request_case(
                    tmp,
                    "future_runtime_may_not_be_considered",
                    lambda req: req.update({"future_runtime_may_not_be_considered": True}),
                ),
            ),
            ("boundary type missing", lambda tmp: request_case(tmp, "boundary_type_missing", lambda req: req.pop("boundary_type"))),
            (
                "boundary type wrong",
                lambda tmp: request_case(tmp, "boundary_type_wrong", lambda req: req.update({"boundary_type": "LOCAL_RELEVANCE_MEDIUM_RUNTIME"})),
            ),
            ("boundary scope missing", lambda tmp: request_case(tmp, "boundary_scope_missing", lambda req: req.pop("boundary_scope"))),
            (
                "boundary scope wrong",
                lambda tmp: request_case(tmp, "boundary_scope_wrong", lambda req: req.update({"boundary_scope": "GENERAL_RUNTIME"})),
            ),
            (
                "required non-claim missing",
                lambda tmp: request_case(tmp, "required_non_claim_missing", lambda req: req["declared_non_claims"].pop("runtime_created")),
            ),
            (
                "required non-claim flipped",
                lambda tmp: request_case(
                    tmp,
                    "required_non_claim_flipped",
                    lambda req: req["declared_non_claims"].update({"runtime_created": True}),
                ),
            ),
        ]
        for field in false_field_cases:
            cases.append(
                (
                    field.replace("_", " "),
                    lambda tmp, field=field: request_case(
                        tmp,
                        field,
                        lambda req, field=field: req.update({field: True}),
                    ),
                )
            )

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            for index, (name, factory) in enumerate(cases):
                with self.subTest(case=name):
                    case_dir = tmp_path / self.safe_json_filename(name, index).removesuffix(".json")
                    case_dir.mkdir()
                    request = factory(case_dir)
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min(request)  # type: ignore[arg-type]
                    self.assert_blocked_with_public_code(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min(
                self.clean_request(runtime_path, operation_path)
            )

            self.assertEqual(self.boundary(result)["boundary_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY")
            self.assertEqual(self.boundary(result)["boundary_scope"], "SELECTED_RUNTIME_CONSIDERATION_ONLY")
            self.assertEqual(self.boundary(result)["selected_command"], "state")
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(set(resolver.OUTCOME_FAMILY), set(resolver.OUTCOME_FAMILY))
            serialized = json.dumps(result, sort_keys=True)
            for official in (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
                "SELECTED_RUNTIME_CONSIDERATION_ONLY",
                '"state"',
            ):
                self.assertIn(official, serialized)
            self.assertNotIn("[REDACTED_RUNTIME_BOUNDARY_CONTENT]", serialized)

    def test_raw_hidden_and_older_runtime_hostile_content_containment(self) -> None:
        def add_artifact_sentinels(artifact: dict[str, Any]) -> None:
            artifact["raw_runtime_body"] = HOSTILE_SENTINELS[2]
            artifact["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            artifact["raw_prior_result_reentry_body"] = HOSTILE_SENTINELS[10]

        with tempfile.TemporaryDirectory() as tmp:
            runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(
                Path(tmp),
                "hostile",
                runtime_permission_mutator=add_artifact_sentinels,
                operation_execution_mutator=add_artifact_sentinels,
            )
            request = self.clean_request(runtime_path, operation_path)
            request["raw_runtime_boundary_body"] = HOSTILE_SENTINELS[0]
            request["runtime_held_state_body"] = HOSTILE_SENTINELS[7]
            request["older_runtime_authority_body"] = HOSTILE_SENTINELS[11]
            original_request = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min(request)

            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assert_no_hostile_sentinels(result)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY", serialized)
            self.assertIn("SELECTED_RUNTIME_CONSIDERATION_ONLY", serialized)
            self.assertIn('"state"', serialized)
            self.assert_canonical_false_non_claims(result)
            self.assert_runtime_boundary_non_claims(result)
            self.assertEqual(request, original_request)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(tmp_path)
            request = self.clean_request(runtime_path, operation_path)
            request_path = self.write_json(tmp_path / "request.json", request)

            result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_from_path(request_path)
            self.assert_clean_recorded_result(result, runtime_path, operation_path)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            try:
                malformed = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_from_path(malformed_path)
            except resolver.LocalRelevanceMediumReadOnlyRuntimeBoundaryV0MinError:
                malformed = None
            if malformed is not None:
                self.assert_blocked_with_public_code(malformed)

            array_path = self.write_json(tmp_path / "array.json", [])
            array_result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_from_path(array_path)
            self.assert_blocked_with_public_code(array_result)

            try:
                missing_result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min_from_path(
                    tmp_path / "missing.json"
                )
            except resolver.LocalRelevanceMediumReadOnlyRuntimeBoundaryV0MinError:
                missing_result = None
            if missing_result is not None:
                self.assert_blocked_with_public_code(missing_result)

            patched_output_root = tmp_path / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_output_root):
                first_path = resolver.write_local_relevance_medium_read_only_runtime_boundary_v0_min_result(result)
                second_path = resolver.write_local_relevance_medium_read_only_runtime_boundary_v0_min_result(result)

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(second_path.parent.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(json.loads(second_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn("local_relevance_medium_read_only_runtime_boundary_v0_min", str(first_path))
            self.assert_output_path_not_under_prior_roots(first_path)
            self.assert_output_path_not_under_prior_roots(second_path)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            runtime_path, operation_path, runtime_artifact, operation_artifact = self.write_synthetic_artifacts(tmp_path)
            runtime_artifact_before = copy.deepcopy(runtime_artifact)
            operation_artifact_before = copy.deepcopy(operation_artifact)
            request = self.clean_request(runtime_path, operation_path)
            request["additional_basis_context"] = {
                "raw_runtime_loop_body": HOSTILE_SENTINELS[4],
                "posture": {
                    "selected_command": "state",
                    "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
                },
            }
            request_before = copy.deepcopy(request)

            resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min(request)

            self.assertEqual(request, request_before)
            self.assertEqual(runtime_artifact, runtime_artifact_before)
            self.assertEqual(operation_artifact, operation_artifact_before)
            self.assertEqual(request["selected_command"], "state")
            self.assertEqual(request["boundary_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY")
            self.assertEqual(request["boundary_scope"], "SELECTED_RUNTIME_CONSIDERATION_ONLY")
            self.assertIs(request["declared_non_claims"]["consumed_request_reopened"], False)
            self.assertIs(request["declared_non_claims"]["authorization_token_reused"], False)
            self.assertIs(request["declared_non_claims"]["older_runtime_lineage_imported_as_authority"], False)
            self.assertIs(request["declared_non_claims"]["runtime_authority_imported"], False)

    def test_predecessor_failure_preservation_and_summary_posture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runtime_path, operation_path, _, _ = self.write_synthetic_artifacts(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_runtime_boundary_v0_min(
                self.clean_request(runtime_path, operation_path)
            )
            summary = resolver.build_local_relevance_medium_read_only_runtime_boundary_v0_min_summary(result)

            self.assertIs(self.statement(result)["predecessor_failure_evidence_preserved"], True)
            self.assertIs(self.statement(result)["consumed_request_token_remains_closed"], True)
            self.assertIs(self.statement(result)["authorization_token_reuse_blocked"], True)
            self.assertIs(self.statement(result)["result_level_non_claims_canonical_false"], True)
            self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
            self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
            self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(summary["result_level_non_claims_canonical_false"], True)
            self.assertIs(summary["consumed_request_token_remains_closed"], True)
            self.assertIs(summary["authorization_token_reuse_blocked"], True)
            self.assertIs(summary["older_runtime_lineage_not_imported_as_authority"], True)
            self.assertIs(summary["older_runtime_permission_not_treated_as_current"], True)
            self.assertIs(summary["runtime_authority_not_imported"], True)


if __name__ == "__main__":
    unittest.main()
