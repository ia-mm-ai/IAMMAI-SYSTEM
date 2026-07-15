"""Tests for the local read-only selected-state runtime permission resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION object. It verifies that the
resolver reads one clean runtime-permission boundary artifact and one clean
selected-state operation execution artifact, then records one local read-only
selected-state runtime-permission object only.

The suite does not create runtime behavior, runtime hosting behavior, runtime
loop behavior, daemon behavior, continuation behavior, runtime-held state,
runtime-held re-entry, second operation behavior, public API behavior,
participant-facing interface behavior, distributed network behavior, general
operation permission, general lookup permission, arbitrary lookup permission,
unsupported-command permission, unsupported-key permission, a new lookup entry
beyond the already bounded selected-state lookup result object, registry,
search, query surface, ranking, scoring, priority, validity judgment, truth
judgment, authority judgment, currentness judgment, repeated reception
permission, arbitrary reception, feed, new signal, new entry, new relevance
object beyond the already bounded selected-state lookup result object, new
index entry, filesystem discovery, source transfer, source receipt,
participation, older-runtime authority import, or follow-on work.
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

import resolve_local_relevance_medium_read_only_runtime_permission_v0_min as resolver  # noqa: E402


DEFAULT_RUNTIME_PERMISSION_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_permission_boundary_v0_min/"
    "local_relevance_medium_read_only_runtime_permission_boundary_reference_review_001__"
    "local_relevance_medium_read_only_runtime_permission_boundary_v0_min_result.json"
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
    "runtime_permission_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2"),
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
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_behavior_v0_min"),
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_runtime_permission_metadata",
    "declared_local_relevance_medium_read_only_runtime_permission_question",
    "selected_runtime_permission_boundary_artifact_basis",
    "selected_operation_execution_artifact_basis",
    "local_relevance_medium_read_only_runtime_permission",
    "local_relevance_medium_read_only_runtime_permission_checks",
    "local_relevance_medium_read_only_runtime_permission_statement",
    "local_relevance_medium_read_only_runtime_permission_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_permission_summary",
)

FORBIDDEN_RUNTIME_PERMISSION_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_permission_checks",
    "non_claims",
    "local_relevance_medium_read_only_runtime_permission_summary",
    "local_relevance_medium_read_only_runtime_permission_metadata",
)

RUNTIME_PERMISSION_OBJECT_FALSE_FIELDS = (
    "runtime_created",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "continuation_created",
    "runtime_held_state_created",
    "runtime_held_reentry_created",
    "second_operation_created",
    "metabolic_loop_created",
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

HOSTILE_SENTINELS = (
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_STATE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

OFFICIAL_STRINGS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
    "SELECTED_RUNTIME_PERMISSION_ONLY",
    "state",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED",
)


class LocalRelevanceMediumReadOnlyRuntimePermissionV0MinTests(unittest.TestCase):
    """Bounded executable tests for the runtime-permission resolver."""

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

    def write_json(self, path: Path, data: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")

    def synthetic_runtime_permission_boundary_artifact(self) -> dict[str, Any]:
        boundary = {
            "boundary_id": "local_relevance_medium_read_only_runtime_permission_boundary_001",
            "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY",
            "boundary_version": "0.1.0",
            "boundary_scope": "SELECTED_RUNTIME_PERMISSION_CONSIDERATION_ONLY",
            "selected_command": "state",
            "selected_command_is_state": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "future_runtime_permission_may_be_considered": True,
            "runtime_permission_created": False,
            "runtime_created": False,
            "runtime_hosting_created": False,
            "runtime_loop_created": False,
            "daemon_behavior_created": False,
            "continuation_created": False,
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
        statement = {
            "selected_command_is_state": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "future_runtime_permission_may_be_considered": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        summary = {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 89,
            **boundary,
            **statement,
        }
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 89,
            "local_relevance_medium_read_only_runtime_permission_boundary": boundary,
            "local_relevance_medium_read_only_runtime_permission_boundary_statement": statement,
            "local_relevance_medium_read_only_runtime_permission_boundary_summary": summary,
            "local_relevance_medium_read_only_runtime_permission_boundary_checks": [
                {
                    "check_name": "synthetic_clean_runtime_permission_boundary",
                    "passed": True,
                    "expected_posture": "clean boundary",
                    "actual_posture": "clean boundary",
                    "block_code": None,
                    "failure_code": None,
                }
            ],
        }

    def synthetic_operation_execution_artifact(self) -> dict[str, Any]:
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
            "runtime_permission_created": False,
            "runtime_created": False,
            "runtime_hosting_created": False,
            "runtime_loop_created": False,
            "daemon_behavior_created": False,
            "continuation_created": False,
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
        statement = {
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "selected_operation_execution_recorded": True,
            "selected_command_is_state": True,
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
            "passed_check_count": 93,
            **operation_execution,
            **statement,
        }
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 93,
            "local_relevance_medium_read_only_operation_execution": operation_execution,
            "local_relevance_medium_read_only_operation_execution_statement": statement,
            "local_relevance_medium_read_only_operation_execution_summary": summary,
            "local_relevance_medium_read_only_operation_execution_checks": [
                {
                    "check_name": "synthetic_clean_operation_execution",
                    "passed": True,
                    "expected_posture": "clean operation execution",
                    "actual_posture": "clean operation execution",
                    "block_code": None,
                    "failure_code": None,
                }
            ],
        }

    def write_synthetic_artifacts(
        self,
        directory: Path,
        *,
        case_name: str = "clean",
        boundary_mutator: Callable[[dict[str, Any]], None] | None = None,
        operation_mutator: Callable[[dict[str, Any]], None] | None = None,
    ) -> tuple[Path, Path, dict[str, Any], dict[str, Any]]:
        boundary = self.synthetic_runtime_permission_boundary_artifact()
        operation = self.synthetic_operation_execution_artifact()
        if boundary_mutator is not None:
            boundary_mutator(boundary)
        if operation_mutator is not None:
            operation_mutator(operation)
        boundary_path = directory / self.safe_json_filename(
            f"{case_name}_runtime_permission_boundary"
        )
        operation_path = directory / self.safe_json_filename(
            f"{case_name}_operation_execution"
        )
        self.write_json(boundary_path, boundary)
        self.write_json(operation_path, operation)
        return boundary_path, operation_path, boundary, operation

    def clean_request(
        self,
        boundary_path: Path,
        operation_path: Path,
        **extra_fields: Any,
    ) -> dict[str, Any]:
        request = (
            resolver.build_declared_local_relevance_medium_read_only_runtime_permission_v0_min_request(
                selected_runtime_permission_boundary_artifact=boundary_path,
                selected_operation_execution_artifact=operation_path,
            )
        )
        request.update(extra_fields)
        return request

    def result_summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_runtime_permission_summary"]

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return int(self.result_summary(result)["failed_check_count"])

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return int(self.result_summary(result)["passed_check_count"])

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        return list(result["local_relevance_medium_read_only_runtime_permission_checks"])

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

    def runtime_permission(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_runtime_permission"]

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_runtime_permission_statement"]

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
        non_claims = result["non_claims"]
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)
        self.assertNotIn("runtime_permission_created", non_claims)
        self.assertNotIn("runtime_permission_local_only", non_claims)
        self.assertNotIn("runtime_permission_read_only", non_claims)

    def assert_runtime_permission_non_claims(self, result: Mapping[str, Any]) -> None:
        runtime_permission = self.runtime_permission(result)
        for key in RUNTIME_PERMISSION_OBJECT_FALSE_FIELDS:
            self.assertIn(key, runtime_permission)
            self.assertIs(runtime_permission[key], False)
        self.assert_canonical_false_non_claims(result)

    def assert_runtime_permission_wrapper_separated(
        self,
        runtime_permission: Mapping[str, Any],
    ) -> None:
        for field in FORBIDDEN_RUNTIME_PERMISSION_WRAPPER_FIELDS:
            self.assertNotIn(field, runtime_permission)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_runtime_permission_non_claims(result)

    def assert_recorded_runtime_permission_core(
        self,
        result: Mapping[str, Any],
        boundary_path: Path,
        operation_path: Path,
    ) -> None:
        runtime_permission = self.runtime_permission(result)
        self.assertEqual(
            runtime_permission["runtime_permission_id"],
            "local_relevance_medium_read_only_runtime_permission_001",
        )
        self.assertEqual(
            runtime_permission["runtime_permission_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
        )
        self.assertEqual(runtime_permission["runtime_permission_version"], "0.1.0")
        self.assertEqual(
            runtime_permission["runtime_permission_scope"],
            "SELECTED_RUNTIME_PERMISSION_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            runtime_permission["basis_runtime_permission_boundary_artifact"],
            boundary_path,
        )
        self.assertEqual(
            runtime_permission["basis_runtime_permission_boundary_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            runtime_permission["basis_runtime_permission_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            runtime_permission["basis_runtime_permission_boundary_failed_check_count"],
            0,
        )
        self.assert_same_or_stable_artifact_path(
            runtime_permission["basis_operation_execution_artifact"],
            operation_path,
        )
        self.assertEqual(
            runtime_permission["basis_operation_execution_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
        )
        self.assertEqual(
            runtime_permission["basis_operation_execution_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            runtime_permission["basis_operation_execution_failed_check_count"],
            0,
        )
        self.assertEqual(runtime_permission["selected_command"], "state")
        self.assertIs(runtime_permission["selected_command_is_state"], True)
        self.assertIs(runtime_permission["selected_operation_execution_recorded"], True)
        self.assertIs(runtime_permission["operation_execution_created"], True)
        self.assertIs(runtime_permission["operation_execution_performed"], True)
        self.assertIs(runtime_permission["operation_execution_local_only"], True)
        self.assertIs(runtime_permission["operation_execution_read_only"], True)
        self.assertIs(
            runtime_permission[
                "local_relevance_medium_read_only_runtime_permission_recorded"
            ],
            True,
        )
        self.assertIs(runtime_permission["runtime_permission_created"], True)
        self.assertIs(runtime_permission["runtime_permission_local_only"], True)
        self.assertIs(runtime_permission["runtime_permission_read_only"], True)
        self.assert_runtime_permission_non_claims(result)
        self.assert_runtime_permission_wrapper_separated(runtime_permission)

    def assert_statement_true_fields(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        true_fields = (
            "local_relevance_medium_read_only_runtime_permission_recorded",
            "basis_runtime_permission_boundary_artifact_preserved",
            "basis_operation_execution_artifact_preserved",
            "selected_command_preserved",
            "selected_command_is_state",
            "selected_operation_execution_recorded",
            "operation_execution_created",
            "operation_execution_performed",
            "operation_execution_local_only",
            "operation_execution_read_only",
            "runtime_permission_created",
            "runtime_permission_local_only",
            "runtime_permission_read_only",
            "consumed_request_token_remains_closed",
            "authorization_token_reuse_blocked",
            "predecessor_failure_evidence_preserved",
            "result_level_non_claims_canonical_false",
        )
        for field in true_fields:
            self.assertIs(statement[field], True)

    def assert_not_under_forbidden_roots(self, output_path: Path) -> None:
        path = output_path
        try:
            stable = path.relative_to(REPO_ROOT)
        except ValueError:
            parts = path.parts
            if "artifacts" in parts:
                stable = Path(*parts[parts.index("artifacts") :])
            else:
                stable = path
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            self.assertNotEqual(stable, forbidden)
            self.assertFalse(stable.is_relative_to(forbidden))

    def assert_no_hostile_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def test_public_api_constants_and_builder_defaults(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_runtime_permission_v0_min",
            "resolve_local_relevance_medium_read_only_runtime_permission_v0_min_from_path",
            "write_local_relevance_medium_read_only_runtime_permission_v0_min_result",
            "build_local_relevance_medium_read_only_runtime_permission_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_runtime_permission_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_RUNTIME_PERMISSION_TYPE_VALUES",
            "SUPPORTED_RUNTIME_PERMISSION_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_runtime_permission_v0_min",
        )
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
            resolver.SUPPORTED_RUNTIME_PERMISSION_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_RUNTIME_PERMISSION_ONLY",
            resolver.SUPPORTED_RUNTIME_PERMISSION_SCOPE_VALUES,
        )
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
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in (
            "runtime_permission_created",
            "runtime_permission_local_only",
            "runtime_permission_read_only",
        ):
            self.assertNotIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)

        for code in (
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "RUNTIME_AUTHORITY_IMPORTED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        request = (
            resolver.build_declared_local_relevance_medium_read_only_runtime_permission_v0_min_request()
        )
        self.assertTrue(
            request["selected_runtime_permission_boundary_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_permission_boundary_reference_review_001__"
                "local_relevance_medium_read_only_runtime_permission_boundary_v0_min_result.json"
            )
        )
        self.assertTrue(
            request["selected_operation_execution_artifact"].endswith(
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

        self.assert_not_under_forbidden_roots(Path(resolver.OUTPUT_ROOT))

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            boundary_path, operation_path, _, _ = self.write_synthetic_artifacts(
                directory
            )
            request = self.clean_request(boundary_path, operation_path)
            result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min(
                    request
                )
            )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertEqual(self.result_summary(result)["result_version"], "0.1.0")
        self.assertEqual(
            self.result_summary(result)["resolver_module"],
            "resolve_local_relevance_medium_read_only_runtime_permission_v0_min",
        )
        self.assertEqual(
            result["local_relevance_medium_read_only_runtime_permission_metadata"][
                "local_relevance_medium_read_only_runtime_permission_id"
            ],
            "local_relevance_medium_read_only_runtime_permission_001",
        )
        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)
        self.assert_recorded_runtime_permission_core(result, boundary_path, operation_path)
        self.assert_statement_true_fields(result)
        self.assert_canonical_false_non_claims(result)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_RUNTIME_PERMISSION_BOUNDARY_ARTIFACT.exists():
            self.skipTest("default runtime permission boundary artifact is absent")
        if not DEFAULT_OPERATION_EXECUTION_ARTIFACT.exists():
            self.skipTest("default operation execution artifact is absent")

        request = (
            resolver.build_declared_local_relevance_medium_read_only_runtime_permission_v0_min_request()
        )
        result = (
            resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min(
                request
            )
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        runtime_permission = self.runtime_permission(result)
        self.assertEqual(runtime_permission["selected_command"], "state")
        self.assertEqual(
            runtime_permission["runtime_permission_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
        )
        self.assertEqual(
            runtime_permission["runtime_permission_scope"],
            "SELECTED_RUNTIME_PERMISSION_ONLY",
        )
        self.assertIs(runtime_permission["selected_operation_execution_recorded"], True)
        self.assertIs(runtime_permission["operation_execution_created"], True)
        self.assertIs(runtime_permission["operation_execution_performed"], True)
        self.assertIs(runtime_permission["operation_execution_local_only"], True)
        self.assertIs(runtime_permission["operation_execution_read_only"], True)
        self.assertIs(
            runtime_permission[
                "local_relevance_medium_read_only_runtime_permission_recorded"
            ],
            True,
        )
        self.assertIs(runtime_permission["runtime_permission_created"], True)
        self.assertIs(runtime_permission["runtime_permission_local_only"], True)
        self.assertIs(runtime_permission["runtime_permission_read_only"], True)
        self.assert_runtime_permission_non_claims(result)
        self.assert_statement_true_fields(result)
        self.assert_same_or_stable_artifact_path(
            runtime_permission["basis_runtime_permission_boundary_artifact"],
            DEFAULT_RUNTIME_PERMISSION_BOUNDARY_ARTIFACT,
        )
        self.assert_same_or_stable_artifact_path(
            runtime_permission["basis_operation_execution_artifact"],
            DEFAULT_OPERATION_EXECUTION_ARTIFACT,
        )

    def test_closure_token_and_older_runtime_import_blocking_behavior(self) -> None:
        cases: list[tuple[str, str, str | None, Any]] = [
            (
                "top_consumed_request_reopened",
                "top",
                "CONSUMED_REQUEST_REOPENED",
                ("consumed_request_reopened", True),
            ),
            (
                "top_authorization_token_reused",
                "top",
                "AUTHORIZATION_TOKEN_REUSED",
                ("authorization_token_reused", True),
            ),
            (
                "top_older_runtime_lineage_imported_as_authority",
                "top",
                "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
                ("older_runtime_lineage_imported_as_authority", True),
            ),
            (
                "top_older_runtime_permission_treated_as_current",
                "top",
                "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
                ("older_runtime_permission_treated_as_current", True),
            ),
            (
                "top_runtime_authority_imported",
                "top",
                "RUNTIME_AUTHORITY_IMPORTED",
                ("runtime_authority_imported", True),
            ),
        ]
        for key in (
            "consumed_request_reopened",
            "authorization_token_reused",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
        ):
            cases.append((f"declared_{key}_true", "non_claim", None, (key, True)))
            cases.append((f"declared_{key}_missing", "remove_non_claim", None, key))
            cases.append((f"declared_{key}_string_false", "non_claim", None, (key, "false")))
            cases.append((f"declared_{key}_none", "non_claim", None, (key, None)))

        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            boundary_path, operation_path, _, _ = self.write_synthetic_artifacts(
                directory,
                case_name="closure",
            )
            for name, mode, expected_code, payload in cases:
                with self.subTest(name=name):
                    request = self.clean_request(boundary_path, operation_path)
                    if mode == "top":
                        key, value = payload
                        request[key] = value
                    elif mode == "non_claim":
                        key, value = payload
                        request["declared_non_claims"][key] = value
                    elif mode == "remove_non_claim":
                        request["declared_non_claims"].pop(payload)
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    if expected_code is not None:
                        self.assertEqual(self.block_code(result), expected_code)
                    else:
                        self.assertEqual(
                            self.block_code(result),
                            "NON_CLAIM_MISSING_OR_FLIPPED",
                        )
                    for key in (
                        "consumed_request_reopened",
                        "authorization_token_reused",
                        "older_runtime_lineage_imported_as_authority",
                        "older_runtime_permission_treated_as_current",
                        "runtime_authority_imported",
                    ):
                        self.assertIs(result["non_claims"][key], False)

    def test_required_false_non_claims_are_canonicalized_after_illegal_true_input(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            boundary_path, operation_path, _, _ = self.write_synthetic_artifacts(
                directory,
                case_name="canonical",
            )
            clean_request = self.clean_request(boundary_path, operation_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertGreater(self.failed_check_count(result), 0)
                    self.assert_all_emitted_codes_public(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_runtime_permission_non_claims(result)

    def test_representative_blocking_behavior(self) -> None:
        def set_boundary_result_version(value: str) -> Callable[[dict[str, Any]], None]:
            def mutator(artifact: dict[str, Any]) -> None:
                artifact["result_version"] = value
                artifact["local_relevance_medium_read_only_runtime_permission_boundary"][
                    "boundary_version"
                ] = value
                artifact["local_relevance_medium_read_only_runtime_permission_boundary_summary"][
                    "result_version"
                ] = value

            return mutator

        def set_operation_result_version(value: str) -> Callable[[dict[str, Any]], None]:
            def mutator(artifact: dict[str, Any]) -> None:
                artifact["result_version"] = value
                artifact["local_relevance_medium_read_only_operation_execution"][
                    "operation_execution_version"
                ] = value
                artifact["local_relevance_medium_read_only_operation_execution_summary"][
                    "result_version"
                ] = value

            return mutator

        def flip_boundary_field(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            def mutator(artifact: dict[str, Any]) -> None:
                artifact["local_relevance_medium_read_only_runtime_permission_boundary"][
                    field
                ] = value
                artifact["local_relevance_medium_read_only_runtime_permission_boundary_summary"][
                    field
                ] = value

            return mutator

        def flip_operation_field(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            def mutator(artifact: dict[str, Any]) -> None:
                artifact["local_relevance_medium_read_only_operation_execution"][
                    field
                ] = value
                artifact["local_relevance_medium_read_only_operation_execution_summary"][
                    field
                ] = value

            return mutator

        def set_request(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            return lambda request: request.__setitem__(field, value)

        def pop_request(field: str) -> Callable[[dict[str, Any]], None]:
            return lambda request: request.pop(field, None)

        false_field_cases = [
            ("runtime created", "runtime_created"),
            ("runtime hosting created", "runtime_hosting_created"),
            ("runtime loop created", "runtime_loop_created"),
            ("daemon behavior created", "daemon_behavior_created"),
            ("continuation created", "continuation_created"),
            ("runtime-held state created", "runtime_held_state_created"),
            ("runtime-held re-entry created", "runtime_held_reentry_created"),
            ("second operation created", "second_operation_created"),
            ("public API created", "public_api_created"),
            ("participant-facing interface created", "participant_facing_interface_created"),
            ("distributed network behavior created", "distributed_network_behavior_created"),
            ("general operation permission created", "general_operation_permission_created"),
            ("general lookup permission created", "general_lookup_permission_created"),
            ("arbitrary lookup permission created", "arbitrary_lookup_permission_created"),
            ("unsupported commands permitted", "unsupported_commands_permitted"),
            ("unsupported lookup keys permitted", "unsupported_lookup_keys_permitted"),
            ("new lookup entry created", "new_lookup_entry_created"),
            ("new signal accepted", "new_signal_accepted"),
            ("new entry accepted", "new_entry_accepted"),
            ("new relevance object created", "new_relevance_object_created"),
            ("new index entry created", "new_index_entry_created"),
            ("filesystem discovery performed", "filesystem_discovery_performed"),
            ("registry created", "registry_created"),
            ("search surface created", "search_surface_created"),
            ("query surface created", "query_surface_created"),
            ("ranking surface created", "ranking_surface_created"),
            ("scoring surface created", "scoring_surface_created"),
            ("priority surface created", "priority_surface_created"),
            ("validity judgment created", "validity_judgment_created"),
            ("truth judgment created", "truth_judgment_created"),
            ("authority judgment created", "authority_judgment_created"),
            ("currentness judgment created", "currentness_judgment_created"),
            (
                "older runtime lineage imported as authority",
                "older_runtime_lineage_imported_as_authority",
            ),
            (
                "older runtime permission treated as current",
                "older_runtime_permission_treated_as_current",
            ),
            ("runtime authority imported", "runtime_authority_imported"),
            ("repeated reception permission created", "repeated_reception_permission_created"),
            ("arbitrary reception created", "arbitrary_reception_created"),
            ("feed created", "feed_created"),
            ("source transfer occurred", "source_transfer_occurred"),
            ("source receipt occurred", "source_receipt_occurred"),
            ("source created", "source_created"),
            ("authority created", "authority_created"),
            ("currentness created", "currentness_created"),
            ("truth created", "truth_created"),
            ("synchronization created", "synchronization_created"),
            ("participation authorized", "participation_authorized"),
            ("participant role created", "participant_role_created"),
            ("deployment created", "deployment_created"),
            ("public release created", "public_release_created"),
            ("broader reusable permission created", "broader_reusable_permission_created"),
            ("follow-on work authorized", "follow_on_work_authorized"),
            (
                "artifact existence treated as runtime-permission authority",
                "artifact_existence_treated_as_runtime_permission_authority",
            ),
            (
                "latest file posture treated as runtime-permission authority",
                "latest_file_posture_treated_as_runtime_permission_authority",
            ),
            (
                "repo-local availability treated as runtime-permission authority",
                "repo_local_availability_treated_as_runtime_permission_authority",
            ),
            (
                "hidden repo state used as runtime-permission content",
                "hidden_repo_state_used_as_runtime_permission_content",
            ),
            (
                "hidden repo state used as runtime-permission authority",
                "hidden_repo_state_used_as_runtime_permission_authority",
            ),
            ("consumed request reopened", "consumed_request_reopened"),
            ("authorization token reused", "authorization_token_reused"),
        ]

        cases: list[dict[str, Any]] = [
            {
                "name": "explicit block intent",
                "request_mutator": set_request(
                    "local_relevance_medium_read_only_runtime_permission_intent",
                    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
                ),
            },
            {
                "name": "missing request question",
                "request_mutator": set_request(
                    "local_relevance_medium_read_only_runtime_permission_question",
                    "",
                ),
            },
            {"name": "non-mapping request", "non_mapping": True},
            {
                "name": "unsupported intent",
                "request_mutator": set_request(
                    "local_relevance_medium_read_only_runtime_permission_intent",
                    "UNSUPPORTED_INTENT",
                ),
            },
            {
                "name": "runtime permission boundary artifact path missing",
                "request_mutator": set_request(
                    "selected_runtime_permission_boundary_artifact",
                    "",
                ),
            },
            {
                "name": "runtime permission boundary artifact unreadable",
                "request_mutator": lambda request: request.__setitem__(
                    "selected_runtime_permission_boundary_artifact",
                    str(Path(request["selected_runtime_permission_boundary_artifact"]).parent / "missing_boundary.json"),
                ),
            },
            {"name": "runtime permission boundary artifact JSON array", "boundary_array": True},
            {
                "name": "runtime permission boundary artifact not recorded",
                "boundary_mutator": lambda artifact: (
                    artifact.__setitem__("outcome", "NOT_RECORDED"),
                    artifact[
                        "local_relevance_medium_read_only_runtime_permission_boundary_summary"
                    ].__setitem__("outcome", "NOT_RECORDED"),
                ),
            },
            {
                "name": "runtime permission boundary artifact failed checks present",
                "boundary_mutator": lambda artifact: (
                    artifact.__setitem__("failed_check_count", 1),
                    artifact[
                        "local_relevance_medium_read_only_runtime_permission_boundary_summary"
                    ].__setitem__("failed_check_count", 1),
                ),
            },
            {
                "name": "runtime permission boundary artifact version not 0.1.0",
                "boundary_mutator": set_boundary_result_version("9.9.9"),
            },
            {
                "name": "operation execution artifact path missing",
                "request_mutator": set_request("selected_operation_execution_artifact", ""),
            },
            {
                "name": "operation execution artifact unreadable",
                "request_mutator": lambda request: request.__setitem__(
                    "selected_operation_execution_artifact",
                    str(Path(request["selected_operation_execution_artifact"]).parent / "missing_operation.json"),
                ),
            },
            {"name": "operation execution artifact JSON array", "operation_array": True},
            {
                "name": "operation execution artifact not recorded",
                "operation_mutator": lambda artifact: (
                    artifact.__setitem__("outcome", "NOT_RECORDED"),
                    artifact[
                        "local_relevance_medium_read_only_operation_execution_summary"
                    ].__setitem__("outcome", "NOT_RECORDED"),
                ),
            },
            {
                "name": "operation execution artifact failed checks present",
                "operation_mutator": lambda artifact: (
                    artifact.__setitem__("failed_check_count", 1),
                    artifact[
                        "local_relevance_medium_read_only_operation_execution_summary"
                    ].__setitem__("failed_check_count", 1),
                ),
            },
            {
                "name": "operation execution artifact version not 0.1.0",
                "operation_mutator": set_operation_result_version("9.9.9"),
            },
            {"name": "selected command missing", "request_mutator": pop_request("selected_command")},
            {
                "name": "selected command not state",
                "request_mutator": set_request("selected_command", "lookup first_orientation_locator"),
            },
            {
                "name": "selected operation execution not recorded",
                "operation_mutator": flip_operation_field(
                    "selected_operation_execution_recorded",
                    False,
                ),
            },
            {
                "name": "operation execution not created",
                "operation_mutator": flip_operation_field(
                    "operation_execution_created",
                    False,
                ),
            },
            {
                "name": "operation execution not performed",
                "operation_mutator": flip_operation_field(
                    "operation_execution_performed",
                    False,
                ),
            },
            {
                "name": "operation execution local only not true",
                "operation_mutator": flip_operation_field(
                    "operation_execution_local_only",
                    False,
                ),
            },
            {
                "name": "operation execution read only not true",
                "operation_mutator": flip_operation_field(
                    "operation_execution_read_only",
                    False,
                ),
            },
            {"name": "runtime permission type missing", "request_mutator": pop_request("runtime_permission_type")},
            {
                "name": "runtime permission type wrong",
                "request_mutator": set_request("runtime_permission_type", "LOCAL_RELEVANCE_MEDIUM_RUNTIME"),
            },
            {"name": "runtime permission scope missing", "request_mutator": pop_request("runtime_permission_scope")},
            {
                "name": "runtime permission scope wrong",
                "request_mutator": set_request("runtime_permission_scope", "RUNTIME"),
            },
            {
                "name": "local relevance medium read-only runtime permission not recorded",
                "request_mutator": set_request(
                    "local_relevance_medium_read_only_runtime_permission_recorded",
                    False,
                ),
            },
            {
                "name": "runtime permission not created",
                "request_mutator": set_request("runtime_permission_created", False),
            },
            {
                "name": "runtime permission local only not true",
                "request_mutator": set_request("runtime_permission_local_only", False),
            },
            {
                "name": "runtime permission read only not true",
                "request_mutator": set_request("runtime_permission_read_only", False),
            },
            {
                "name": "boundary future runtime permission not considered",
                "boundary_mutator": flip_boundary_field(
                    "future_runtime_permission_may_be_considered",
                    False,
                ),
            },
            {
                "name": "boundary already created runtime permission",
                "boundary_mutator": flip_boundary_field(
                    "runtime_permission_created",
                    True,
                ),
            },
            {
                "name": "predecessor failure repaired",
                "request_mutator": set_request("predecessor_failure_repaired", True),
            },
            {
                "name": "predecessor failure hidden",
                "request_mutator": set_request("predecessor_failure_hidden", True),
            },
            {
                "name": "predecessor failure claimed passed",
                "request_mutator": set_request("predecessor_failure_claimed_passed", True),
            },
            {
                "name": "required non-claim missing or flipped",
                "request_mutator": lambda request: request["declared_non_claims"].pop(
                    "runtime_created"
                ),
            },
        ]
        for case_name, field in false_field_cases:
            cases.append({"name": case_name, "request_mutator": set_request(field, True)})

        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            for index, case in enumerate(cases, start=1):
                with self.subTest(case=case["name"]):
                    if case.get("non_mapping"):
                        result = (
                            resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min(
                                ["not", "a", "mapping"]
                            )
                        )
                    else:
                        case_filename = self.safe_json_filename(case["name"], index)
                        case_dir = directory / case_filename.removesuffix(".json")
                        boundary_path, operation_path, _, _ = self.write_synthetic_artifacts(
                            case_dir,
                            case_name=case_filename,
                            boundary_mutator=case.get("boundary_mutator"),
                            operation_mutator=case.get("operation_mutator"),
                        )
                        if case.get("boundary_array"):
                            self.write_json(boundary_path, [])
                        if case.get("operation_array"):
                            self.write_json(operation_path, [])
                        request = self.clean_request(boundary_path, operation_path)
                        request_mutator = case.get("request_mutator")
                        if request_mutator is not None:
                            request_mutator(request)
                        result = (
                            resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min(
                                request
                            )
                        )
                    self.assert_blocked_with_public_code(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            boundary_path, operation_path, _, _ = self.write_synthetic_artifacts(
                directory,
                case_name="official",
            )
            request = self.clean_request(boundary_path, operation_path)
            result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min(
                    request
                )
            )
        runtime_permission = self.runtime_permission(result)
        self.assertEqual(
            runtime_permission["runtime_permission_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
        )
        self.assertEqual(
            runtime_permission["runtime_permission_scope"],
            "SELECTED_RUNTIME_PERMISSION_ONLY",
        )
        self.assertEqual(runtime_permission["selected_command"], "state")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        for outcome in (
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_NOT_RECORDED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_BLOCKED,
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for official in OFFICIAL_STRINGS[:3]:
            self.assertIn(official, serialized)
        self.assertIn(result["outcome"], serialized)
        self.assertNotIn("[REDACTED_SENSITIVE_CONTENT]", json.dumps(runtime_permission))

    def test_raw_hidden_and_older_runtime_hostile_content_is_contained(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)

            def boundary_mutator(artifact: dict[str, Any]) -> None:
                artifact["raw_runtime_permission_boundary_body"] = HOSTILE_SENTINELS[1]
                artifact["local_relevance_medium_read_only_runtime_permission_boundary"][
                    "raw_runtime_body"
                ] = HOSTILE_SENTINELS[2]

            def operation_mutator(artifact: dict[str, Any]) -> None:
                artifact["raw_operation_execution_body"] = "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN"
                artifact["local_relevance_medium_read_only_operation_execution"][
                    "raw_second_operation_body"
                ] = HOSTILE_SENTINELS[8]

            boundary_path, operation_path, boundary, operation = self.write_synthetic_artifacts(
                directory,
                case_name="hostile",
                boundary_mutator=boundary_mutator,
                operation_mutator=operation_mutator,
            )
            request = self.clean_request(boundary_path, operation_path)
            request["raw_runtime_body"] = HOSTILE_SENTINELS[2]
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            request["extra_context"] = {
                "raw_runtime_held_state_body": HOSTILE_SENTINELS[6],
                "older_runtime_authority": HOSTILE_SENTINELS[-2],
            }
            request_before = copy.deepcopy(request)
            boundary_before = copy.deepcopy(boundary)
            operation_before = copy.deepcopy(operation)

            result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min(
                    request
                )
            )

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        if result["outcome"] == resolver.OUTCOME_BLOCKED:
            self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        self.assert_no_hostile_sentinels(result)
        serialized = json.dumps(result, sort_keys=True)
        for official in OFFICIAL_STRINGS[:3]:
            self.assertIn(official, serialized)
        self.assertIn(result["outcome"], serialized)
        self.assert_runtime_permission_non_claims(result)
        self.assertEqual(request, request_before)
        self.assertEqual(boundary, boundary_before)
        self.assertEqual(operation, operation_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            boundary_path, operation_path, _, _ = self.write_synthetic_artifacts(
                directory,
                case_name="path",
            )
            request = self.clean_request(boundary_path, operation_path)
            request_path = directory / "request.json"
            self.write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.result_summary(result)["result_version"], "0.1.0")
            self.assertEqual(
                self.result_summary(result)["resolver_module"],
                "resolve_local_relevance_medium_read_only_runtime_permission_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = directory / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min_from_path(
                malformed_path
            )
            self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)

            array_path = directory / "array.json"
            self.write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)

            missing_result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min_from_path(
                directory / "missing.json"
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)

            patched_root = (
                directory
                / "artifacts"
                / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_root):
                first_path = resolver.write_local_relevance_medium_read_only_runtime_permission_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_runtime_permission_v0_min_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(second_path.parent.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(first_path.name.endswith("_result.json"))
            self.assertIn(
                "local_relevance_medium_read_only_runtime_permission_v0_min",
                str(first_path),
            )
            with first_path.open("r", encoding="utf-8") as handle:
                written = json.load(handle)
            self.assertEqual(written["outcome"], resolver.OUTCOME_RECORDED)
            self.assert_not_under_forbidden_roots(first_path)
            self.assert_not_under_forbidden_roots(second_path)

    def test_resolver_does_not_mutate_inputs_or_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            boundary = self.synthetic_runtime_permission_boundary_artifact()
            operation = self.synthetic_operation_execution_artifact()
            boundary["raw_runtime_permission_boundary_body"] = HOSTILE_SENTINELS[1]
            operation["raw_operation_execution_body"] = (
                "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN"
            )
            boundary_before = copy.deepcopy(boundary)
            operation_before = copy.deepcopy(operation)
            boundary_path = directory / "boundary.json"
            operation_path = directory / "operation.json"
            self.write_json(boundary_path, boundary)
            self.write_json(operation_path, operation)
            request = self.clean_request(boundary_path, operation_path)
            request["nested_payload"] = {
                "raw_runtime_body": HOSTILE_SENTINELS[2],
                "hidden_repo_state": HOSTILE_SENTINELS[-1],
            }
            request_before = copy.deepcopy(request)

            resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min(
                request
            )

        self.assertEqual(request, request_before)
        self.assertEqual(request["declared_non_claims"], request_before["declared_non_claims"])
        self.assertEqual(
            request["selected_runtime_permission_boundary_artifact"],
            request_before["selected_runtime_permission_boundary_artifact"],
        )
        self.assertEqual(
            request["selected_operation_execution_artifact"],
            request_before["selected_operation_execution_artifact"],
        )
        self.assertEqual(request["selected_command"], "state")
        self.assertEqual(
            request["runtime_permission_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
        )
        self.assertEqual(
            request["runtime_permission_scope"],
            "SELECTED_RUNTIME_PERMISSION_ONLY",
        )
        self.assertEqual(boundary, boundary_before)
        self.assertEqual(operation, operation_before)

    def test_predecessor_failure_preservation_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            boundary_path, operation_path, _, _ = self.write_synthetic_artifacts(
                directory,
                case_name="predecessor",
            )
            request = self.clean_request(boundary_path, operation_path)
            result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_permission_v0_min(
                    request
                )
            )

        summary = (
            resolver.build_local_relevance_medium_read_only_runtime_permission_v0_min_summary(
                result
            )
        )
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
        for key in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
        ):
            self.assertIs(result["non_claims"][key], False)


if __name__ == "__main__":
    unittest.main()
