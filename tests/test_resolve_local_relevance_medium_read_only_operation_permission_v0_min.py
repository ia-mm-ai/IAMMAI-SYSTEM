"""Tests for the local read-only selected-state operation permission resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION object. It verifies that
the resolver reads one clean operation-permission boundary artifact and one
clean selected-state lookup result artifact, then records one local read-only
selected-state operation-permission object only.

The suite does not create operation execution behavior, runtime permission,
public API, participant-facing interface, distributed behavior, general
operation permission, general lookup permission, arbitrary lookup permission,
unsupported-command permission, unsupported-key permission, a new lookup entry
beyond the already bounded selected-state lookup result object, registry,
search, query surface, ranking, scoring, priority, validity judgment, truth
judgment, authority judgment, currentness judgment, repeated reception
permission, arbitrary reception, feed, new signal, new entry, new relevance
object beyond the already bounded selected-state lookup result object, new
index entry, filesystem discovery, source transfer, source receipt,
participation, operation execution, runtime permission, or follow-on work.
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

import resolve_local_relevance_medium_read_only_operation_permission_v0_min as resolver  # noqa: E402


DEFAULT_OPERATION_PERMISSION_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_permission_boundary_v0_min/"
    "local_relevance_medium_read_only_operation_permission_boundary_reference_review_001__"
    "local_relevance_medium_read_only_operation_permission_boundary_v0_min_result.json"
)
DEFAULT_LOOKUP_RESULT_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_result_v0_min/"
    "local_relevance_medium_read_only_lookup_result_reference_review_001__"
    "local_relevance_medium_read_only_lookup_result_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_permission_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_behavior_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_loop_v0_min"),
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_operation_permission_metadata",
    "declared_local_relevance_medium_read_only_operation_permission_question",
    "selected_operation_permission_boundary_artifact_basis",
    "selected_lookup_result_artifact_basis",
    "local_relevance_medium_read_only_operation_permission",
    "local_relevance_medium_read_only_operation_permission_checks",
    "local_relevance_medium_read_only_operation_permission_statement",
    "local_relevance_medium_read_only_operation_permission_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_operation_permission_summary",
)

FORBIDDEN_OPERATION_PERMISSION_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_operation_permission_checks",
    "non_claims",
    "local_relevance_medium_read_only_operation_permission_summary",
    "local_relevance_medium_read_only_operation_permission_metadata",
)

OPERATION_PERMISSION_OBJECT_FALSE_FIELDS = (
    "operation_execution_created",
    "runtime_permission_created",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_COMMAND_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_OBJECT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

OFFICIAL_STRINGS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION",
    "SELECTED_OPERATION_PERMISSION_ONLY",
    "state",
)


class LocalRelevanceMediumReadOnlyOperationPermissionResolverTests(unittest.TestCase):
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

    def write_json(self, path: Path, data: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def synthetic_operation_permission_boundary_artifact(self) -> dict[str, Any]:
        boundary = {
            "boundary_id": "local_relevance_medium_read_only_operation_permission_boundary_001",
            "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY",
            "boundary_version": "0.1.0",
            "boundary_scope": "SELECTED_OPERATION_PERMISSION_CONSIDERATION_ONLY",
            "basis_lookup_result_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_RECORDED",
            "basis_lookup_result_result_version": "0.1.0",
            "basis_lookup_result_failed_check_count": 0,
            "selected_command": "state",
            "selected_command_is_state": True,
            "selected_lookup_result_recorded": True,
            "lookup_result_created": True,
            "lookup_result_local_only": True,
            "lookup_result_read_only": True,
            "future_operation_permission_may_be_considered": True,
        }
        for key in ("operation_permission_created",) + OPERATION_PERMISSION_OBJECT_FALSE_FIELDS:
            boundary[key] = False
        statement = {
            "local_relevance_medium_read_only_operation_permission_boundary_recorded": True,
            "basis_lookup_result_artifact_preserved": True,
            "selected_command_preserved": True,
            "selected_command_is_state": True,
            "selected_lookup_result_recorded": True,
            "lookup_result_created": True,
            "lookup_result_local_only": True,
            "lookup_result_read_only": True,
            "future_operation_permission_may_be_considered": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 83,
            "local_relevance_medium_read_only_operation_permission_boundary_metadata": {
                "result_version": "0.1.0",
                "resolver_module": "resolve_local_relevance_medium_read_only_operation_permission_boundary_v0_min",
            },
            "local_relevance_medium_read_only_operation_permission_boundary": boundary,
            "local_relevance_medium_read_only_operation_permission_boundary_statement": statement,
            "local_relevance_medium_read_only_operation_permission_boundary_checks": [],
            "local_relevance_medium_read_only_operation_permission_boundary_summary": {
                "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_RECORDED",
                "result_version": "0.1.0",
                "failed_check_count": 0,
                "passed_check_count": 83,
                "selected_command": "state",
                **statement,
            },
        }

    def synthetic_lookup_result_artifact(self) -> dict[str, Any]:
        lookup_result = {
            "lookup_result_id": "local_relevance_medium_read_only_lookup_result_001",
            "lookup_result_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT",
            "lookup_result_version": "0.1.0",
            "lookup_result_scope": "SELECTED_LOOKUP_RESULT_ONLY",
            "selected_command": "state",
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_lookup_result_recorded": True,
            "selected_lookup_result_recorded": True,
            "lookup_result_created": True,
            "lookup_result_local_only": True,
            "lookup_result_read_only": True,
        }
        for key in ("operation_permission_created",) + OPERATION_PERMISSION_OBJECT_FALSE_FIELDS:
            lookup_result[key] = False
        statement = {
            "local_relevance_medium_read_only_lookup_result_recorded": True,
            "selected_lookup_result_recorded": True,
            "selected_command_preserved": True,
            "selected_command_is_state": True,
            "lookup_result_created": True,
            "lookup_result_local_only": True,
            "lookup_result_read_only": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 92,
            "local_relevance_medium_read_only_lookup_result_metadata": {
                "result_version": "0.1.0",
                "resolver_module": "resolve_local_relevance_medium_read_only_lookup_result_v0_min",
            },
            "local_relevance_medium_read_only_lookup_result": lookup_result,
            "local_relevance_medium_read_only_lookup_result_statement": statement,
            "local_relevance_medium_read_only_lookup_result_checks": [],
            "local_relevance_medium_read_only_lookup_result_summary": {
                "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_RECORDED",
                "result_version": "0.1.0",
                "failed_check_count": 0,
                "passed_check_count": 92,
                "selected_command": "state",
                **statement,
            },
        }

    def write_synthetic_artifacts(
        self,
        directory: Path,
        name: str = "clean",
        boundary_mutator: Callable[[dict[str, Any]], None] | None = None,
        lookup_mutator: Callable[[dict[str, Any]], None] | None = None,
        boundary_payload: Any | None = None,
        lookup_payload: Any | None = None,
    ) -> tuple[Path, Path, dict[str, Any], dict[str, Any]]:
        boundary_artifact = self.synthetic_operation_permission_boundary_artifact()
        lookup_artifact = self.synthetic_lookup_result_artifact()
        if boundary_mutator is not None:
            boundary_mutator(boundary_artifact)
        if lookup_mutator is not None:
            lookup_mutator(lookup_artifact)
        boundary_path = directory / self.safe_json_filename(f"{name}_boundary")
        lookup_path = directory / self.safe_json_filename(f"{name}_lookup")
        self.write_json(
            boundary_path,
            boundary_artifact if boundary_payload is None else boundary_payload,
        )
        self.write_json(
            lookup_path,
            lookup_artifact if lookup_payload is None else lookup_payload,
        )
        return boundary_path, lookup_path, boundary_artifact, lookup_artifact

    def valid_request(self, boundary_path: Path, lookup_path: Path) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_operation_permission_v0_min_request(
            selected_operation_permission_boundary_artifact=boundary_path,
            selected_lookup_result_artifact=lookup_path,
        )

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get("local_relevance_medium_read_only_operation_permission_checks")
        self.assertIsInstance(checks, list)
        return checks

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def operation_permission(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        operation_permission = result.get("local_relevance_medium_read_only_operation_permission")
        self.assertIsInstance(operation_permission, Mapping)
        return operation_permission

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get("local_relevance_medium_read_only_operation_permission_statement")
        self.assertIsInstance(statement, Mapping)
        return statement

    def non_claims(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        return non_claims

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
        non_claims = self.non_claims(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)

    def assert_operation_permission_non_claims(self, result: Mapping[str, Any]) -> None:
        operation_permission = self.operation_permission(result)
        for key in OPERATION_PERMISSION_OBJECT_FALSE_FIELDS:
            self.assertIn(key, operation_permission)
            self.assertIs(operation_permission[key], False)
        self.assertIs(self.non_claims(result)["follow_on_work_authorized"], False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_operation_permission_non_claims(result)

    def assert_operation_permission_not_wrapper_confused(
        self,
        operation_permission: Mapping[str, Any],
    ) -> None:
        for field in FORBIDDEN_OPERATION_PERMISSION_WRAPPER_FIELDS:
            self.assertNotIn(field, operation_permission)

    def assert_operation_permission_recorded_posture(
        self,
        result: Mapping[str, Any],
        boundary_path: Path,
        lookup_path: Path,
    ) -> None:
        operation_permission = self.operation_permission(result)
        self.assertEqual(
            operation_permission["operation_permission_id"],
            "local_relevance_medium_read_only_operation_permission_001",
        )
        self.assertEqual(
            operation_permission["operation_permission_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION",
        )
        self.assertEqual(operation_permission["operation_permission_version"], "0.1.0")
        self.assertEqual(
            operation_permission["operation_permission_scope"],
            "SELECTED_OPERATION_PERMISSION_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            operation_permission["basis_operation_permission_boundary_artifact"],
            boundary_path,
        )
        self.assertEqual(
            operation_permission["basis_operation_permission_boundary_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            operation_permission["basis_operation_permission_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            operation_permission["basis_operation_permission_boundary_failed_check_count"],
            0,
        )
        self.assert_same_or_stable_artifact_path(
            operation_permission["basis_lookup_result_artifact"],
            lookup_path,
        )
        self.assertEqual(
            operation_permission["basis_lookup_result_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_RECORDED",
        )
        self.assertEqual(operation_permission["basis_lookup_result_result_version"], "0.1.0")
        self.assertEqual(operation_permission["basis_lookup_result_failed_check_count"], 0)
        expected_true = (
            "selected_command_is_state",
            "selected_lookup_result_recorded",
            "lookup_result_created",
            "lookup_result_local_only",
            "lookup_result_read_only",
            "local_relevance_medium_read_only_operation_permission_recorded",
            "operation_permission_created",
            "operation_permission_local_only",
            "operation_permission_read_only",
        )
        self.assertEqual(operation_permission["selected_command"], "state")
        for key in expected_true:
            self.assertIn(key, operation_permission)
            self.assertIs(operation_permission[key], True)
            self.assertIsInstance(operation_permission[key], bool)
        self.assert_operation_permission_non_claims(result)
        self.assert_operation_permission_not_wrapper_confused(operation_permission)

    def assert_statement_recorded_posture(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        for key in (
            "local_relevance_medium_read_only_operation_permission_recorded",
            "basis_operation_permission_boundary_artifact_preserved",
            "basis_lookup_result_artifact_preserved",
            "selected_command_preserved",
            "selected_command_is_state",
            "selected_lookup_result_recorded",
            "lookup_result_created",
            "lookup_result_local_only",
            "lookup_result_read_only",
            "operation_permission_created",
            "operation_permission_local_only",
            "operation_permission_read_only",
            "consumed_request_token_remains_closed",
            "authorization_token_reuse_blocked",
            "predecessor_failure_evidence_preserved",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIn(key, statement)
            self.assertIs(statement[key], True)
            self.assertIsInstance(statement[key], bool)

    def assert_blocked_non_creation_posture(self, result: Mapping[str, Any]) -> None:
        operation_permission = self.operation_permission(result)
        for key in (
            "operation_execution_created",
            "runtime_permission_created",
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
            "authority_created",
            "currentness_created",
            "truth_created",
            "synchronization_created",
            "participation_authorized",
            "participant_role_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(operation_permission.get(key), False)
        self.assertIs(self.non_claims(result)["source_created"], False)
        self.assertIs(self.non_claims(result)["deployment_created"], False)
        self.assertIs(self.non_claims(result)["public_release_created"], False)
        self.assertIs(self.non_claims(result)["broader_reusable_permission_created"], False)

    def assert_not_under_forbidden_roots(self, output_path: Path) -> None:
        output_resolved = Path(output_path).resolve()
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            forbidden_resolved = (REPO_ROOT / forbidden).resolve()
            self.assertFalse(
                output_resolved == forbidden_resolved
                or forbidden_resolved in output_resolved.parents,
                f"{output_path} wrote under forbidden root {forbidden}",
            )

    def assert_no_hostile_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_operation_permission_v0_min",
            "resolve_local_relevance_medium_read_only_operation_permission_v0_min_from_path",
            "write_local_relevance_medium_read_only_operation_permission_v0_min_result",
            "build_local_relevance_medium_read_only_operation_permission_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_operation_permission_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_OPERATION_PERMISSION_TYPE_VALUES",
            "SUPPORTED_OPERATION_PERMISSION_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_operation_permission_v0_min",
        )
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION",
            resolver.SUPPORTED_OPERATION_PERMISSION_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_OPERATION_PERMISSION_ONLY",
            resolver.SUPPORTED_OPERATION_PERMISSION_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        for key in (
            "operation_execution_created",
            "runtime_permission_created",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for code in (
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        request = (
            resolver.build_declared_local_relevance_medium_read_only_operation_permission_v0_min_request()
        )
        self.assertTrue(
            request["selected_operation_permission_boundary_artifact"].endswith(
                "local_relevance_medium_read_only_operation_permission_boundary_reference_review_001__"
                "local_relevance_medium_read_only_operation_permission_boundary_v0_min_result.json"
            )
        )
        self.assertTrue(
            request["selected_lookup_result_artifact"].endswith(
                "local_relevance_medium_read_only_lookup_result_reference_review_001__"
                "local_relevance_medium_read_only_lookup_result_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], "state")
        self.assertIs(request["declared_non_claims"]["consumed_request_reopened"], False)
        self.assertIs(request["declared_non_claims"]["authorization_token_reused"], False)
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            self.assertNotEqual(Path(resolver.OUTPUT_ROOT), forbidden)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(root)
            request = self.valid_request(boundary_path, lookup_path)

            result = resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min(
                request
            )

            self.assertIsInstance(result, dict)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.failed_check_count(result), 0)
            self.assert_not_blocked(result)
            summary = result["local_relevance_medium_read_only_operation_permission_summary"]
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_read_only_operation_permission_v0_min",
            )
            self.assertGreater(self.passed_check_count(result), 0)
            self.assertEqual(
                self.operation_permission(result)["operation_permission_id"],
                "local_relevance_medium_read_only_operation_permission_001",
            )
            for section in EXPECTED_WRAPPER_SECTIONS:
                self.assertIn(section, result)
            self.assert_operation_permission_recorded_posture(result, boundary_path, lookup_path)
            self.assert_statement_recorded_posture(result)
            self.assert_canonical_false_non_claims(result)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_OPERATION_PERMISSION_BOUNDARY_ARTIFACT.exists():
            self.skipTest("default operation permission boundary artifact is not present")
        if not DEFAULT_LOOKUP_RESULT_ARTIFACT.exists():
            self.skipTest("default lookup result artifact is not present")

        request = resolver.build_declared_local_relevance_medium_read_only_operation_permission_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min(
            request
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        operation_permission = self.operation_permission(result)
        self.assertEqual(operation_permission["selected_command"], "state")
        self.assertEqual(
            operation_permission["operation_permission_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION",
        )
        self.assertEqual(
            operation_permission["operation_permission_scope"],
            "SELECTED_OPERATION_PERMISSION_ONLY",
        )
        for key in (
            "selected_lookup_result_recorded",
            "lookup_result_created",
            "lookup_result_local_only",
            "lookup_result_read_only",
            "local_relevance_medium_read_only_operation_permission_recorded",
            "operation_permission_created",
            "operation_permission_local_only",
            "operation_permission_read_only",
        ):
            self.assertIs(operation_permission[key], True)
        for key in (
            "operation_execution_created",
            "runtime_permission_created",
            "public_api_created",
            "distributed_network_behavior_created",
            "general_operation_permission_created",
            "general_lookup_permission_created",
            "follow_on_work_authorized",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(operation_permission[key], False)
        self.assertIs(self.statement(result)["predecessor_failure_evidence_preserved"], True)
        self.assert_same_or_stable_artifact_path(
            operation_permission["basis_operation_permission_boundary_artifact"],
            DEFAULT_OPERATION_PERMISSION_BOUNDARY_ARTIFACT,
        )
        self.assert_same_or_stable_artifact_path(
            operation_permission["basis_lookup_result_artifact"],
            DEFAULT_LOOKUP_RESULT_ARTIFACT,
        )

    def test_closure_token_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(root)
            base_request = self.valid_request(boundary_path, lookup_path)
            cases: list[tuple[str, Callable[[dict[str, Any]], None], str]] = [
                (
                    "top-level consumed_request_reopened true",
                    lambda request: request.__setitem__("consumed_request_reopened", True),
                    "CONSUMED_REQUEST_REOPENED",
                ),
                (
                    "top-level authorization_token_reused true",
                    lambda request: request.__setitem__("authorization_token_reused", True),
                    "AUTHORIZATION_TOKEN_REUSED",
                ),
                (
                    "declared consumed_request_reopened true",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "consumed_request_reopened", True
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "declared authorization_token_reused true",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "authorization_token_reused", True
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "remove declared consumed_request_reopened",
                    lambda request: request["declared_non_claims"].pop(
                        "consumed_request_reopened"
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "remove declared authorization_token_reused",
                    lambda request: request["declared_non_claims"].pop(
                        "authorization_token_reused"
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "declared consumed_request_reopened string false",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "consumed_request_reopened", "false"
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "declared authorization_token_reused string false",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "authorization_token_reused", "false"
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "declared consumed_request_reopened none",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "consumed_request_reopened", None
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "declared authorization_token_reused none",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "authorization_token_reused", None
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
            ]
            for name, mutator, expected_code in cases:
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutator(request)
                    result = resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assertIs(self.non_claims(result)["consumed_request_reopened"], False)
                    self.assertIs(self.non_claims(result)["authorization_token_reused"], False)
                    self.assert_blocked_non_creation_posture(result)

    def test_required_false_non_claim_canonicalization_blocks_flipped_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(root)
            base_request = self.valid_request(boundary_path, lookup_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(self.non_claims(result)[key], False)
                    self.assert_canonical_false_non_claims(result)
                    self.assertIsNot(self.non_claims(result)[key], True)
                    self.assert_blocked_non_creation_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        def set_key(key: str, value: Any = True) -> Callable[[dict[str, Any]], None]:
            return lambda request: request.__setitem__(key, value)

        def remove_key(key: str) -> Callable[[dict[str, Any]], None]:
            return lambda request: request.pop(key, None)

        def set_declared_non_claim(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
            return lambda request: request["declared_non_claims"].__setitem__(key, value)

        cases: list[tuple[str, Callable[[dict[str, Any]], None] | str, str | None]] = [
            ("explicit block intent", set_key("local_relevance_medium_read_only_operation_permission_intent", "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION"), None),
            ("missing request", "empty_request", None),
            ("non-mapping request", "non_mapping", None),
            ("unsupported intent", set_key("local_relevance_medium_read_only_operation_permission_intent", "UNSUPPORTED"), None),
            ("operation permission boundary artifact path missing", set_key("selected_operation_permission_boundary_artifact", ""), None),
            ("operation permission boundary artifact unreadable", set_key("selected_operation_permission_boundary_artifact", "missing-boundary.json"), None),
            ("operation permission boundary artifact JSON array instead of object", "boundary_array", None),
            ("operation permission boundary artifact not recorded", "boundary_not_recorded", None),
            ("operation permission boundary artifact failed checks present", "boundary_failed_checks", None),
            ("operation permission boundary artifact version not 0.1.0", "boundary_bad_version", None),
            ("lookup result artifact path missing", set_key("selected_lookup_result_artifact", ""), None),
            ("lookup result artifact unreadable", set_key("selected_lookup_result_artifact", "missing-lookup.json"), None),
            ("lookup result artifact JSON array instead of object", "lookup_array", None),
            ("lookup result artifact not recorded", "lookup_not_recorded", None),
            ("lookup result artifact failed checks present", "lookup_failed_checks", None),
            ("lookup result artifact version not 0.1.0", "lookup_bad_version", None),
            ("selected command missing", remove_key("selected_command"), None),
            ("selected command not state", set_key("selected_command", "status"), None),
            ("selected lookup result not recorded", set_key("selected_lookup_result_not_recorded", True), None),
            ("lookup result not created", set_key("lookup_result_not_created", True), None),
            ("lookup result local only not true", set_key("lookup_result_local_only_not_true", True), None),
            ("lookup result read only not true", set_key("lookup_result_read_only_not_true", True), None),
            ("operation permission type missing", remove_key("operation_permission_type"), None),
            ("operation permission type not supported", set_key("operation_permission_type", "PUBLIC_API"), None),
            ("operation permission scope missing", remove_key("operation_permission_scope"), None),
            ("operation permission scope not selected only", set_key("operation_permission_scope", "GENERAL"), None),
            ("local relevance medium read only operation permission not recorded", set_key("local_relevance_medium_read_only_operation_permission_not_recorded", True), None),
            ("operation permission not created", set_key("operation_permission_created", False), None),
            ("operation permission local only not true", set_key("operation_permission_local_only", False), None),
            ("operation permission read only not true", set_key("operation_permission_read_only", False), None),
            ("operation execution created", set_key("operation_execution_created", True), None),
            ("runtime permission created", set_key("runtime_permission_created", True), None),
            ("public API created", set_key("public_api_created", True), None),
            ("participant-facing interface created", set_key("participant_facing_interface_created", True), None),
            ("distributed network behavior created", set_key("distributed_network_behavior_created", True), None),
            ("general operation permission created", set_key("general_operation_permission_created", True), None),
            ("general lookup permission created", set_key("general_lookup_permission_created", True), None),
            ("arbitrary lookup permission created", set_key("arbitrary_lookup_permission_created", True), None),
            ("unsupported commands permitted", set_key("unsupported_commands_permitted", True), None),
            ("unsupported lookup keys permitted", set_key("unsupported_lookup_keys_permitted", True), None),
            ("new lookup entry created", set_key("new_lookup_entry_created", True), None),
            ("new signal accepted", set_key("new_signal_accepted", True), None),
            ("new entry accepted", set_key("new_entry_accepted", True), None),
            ("new relevance object created", set_key("new_relevance_object_created", True), None),
            ("new index entry created", set_key("new_index_entry_created", True), None),
            ("filesystem discovery performed", set_key("filesystem_discovery_performed", True), None),
            ("registry created", set_key("registry_created", True), None),
            ("search surface created", set_key("search_surface_created", True), None),
            ("query surface created", set_key("query_surface_created", True), None),
            ("ranking surface created", set_key("ranking_surface_created", True), None),
            ("scoring surface created", set_key("scoring_surface_created", True), None),
            ("priority surface created", set_key("priority_surface_created", True), None),
            ("validity judgment created", set_key("validity_judgment_created", True), None),
            ("truth judgment created", set_key("truth_judgment_created", True), None),
            ("authority judgment created", set_key("authority_judgment_created", True), None),
            ("currentness judgment created", set_key("currentness_judgment_created", True), None),
            ("repeated reception permission created", set_key("repeated_reception_permission_created", True), None),
            ("arbitrary reception created", set_key("arbitrary_reception_created", True), None),
            ("feed created", set_key("feed_created", True), None),
            ("source transfer occurred", set_key("source_transfer_occurred", True), None),
            ("source receipt occurred", set_key("source_receipt_occurred", True), None),
            ("source created", set_key("source_created", True), None),
            ("authority created", set_key("authority_created", True), None),
            ("currentness created", set_key("currentness_created", True), None),
            ("truth created", set_key("truth_created", True), None),
            ("synchronization created", set_key("synchronization_created", True), None),
            ("participation authorized", set_key("participation_authorized", True), None),
            ("participant role created", set_key("participant_role_created", True), None),
            ("deployment created", set_key("deployment_created", True), None),
            ("public release created", set_key("public_release_created", True), None),
            ("broader reusable permission created", set_key("broader_reusable_permission_created", True), None),
            ("follow-on work authorized", set_key("follow_on_work_authorized", True), None),
            ("consumed request reopened", set_key("consumed_request_reopened", True), None),
            ("authorization token reused", set_key("authorization_token_reused", True), None),
            ("artifact existence treated as operation-permission authority", set_key("artifact_existence_treated_as_operation_permission_authority", True), None),
            ("latest file posture treated as operation-permission authority", set_key("latest_file_posture_treated_as_operation_permission_authority", True), None),
            ("repo-local availability treated as operation-permission authority", set_key("repo_local_availability_treated_as_operation_permission_authority", True), None),
            ("hidden repo state used as operation-permission content", set_key("hidden_repo_state_used_as_operation_permission_content", True), None),
            ("hidden repo state used as operation-permission authority", set_key("hidden_repo_state_used_as_operation_permission_authority", True), None),
            ("predecessor failure evidence repaired", set_key("predecessor_failure_repaired", True), None),
            ("predecessor failure evidence hidden", set_key("predecessor_failure_hidden", True), None),
            ("predecessor failure evidence claimed passed", set_key("predecessor_failure_claimed_passed", True), None),
            ("required non-claim missing or flipped", set_declared_non_claim("runtime_permission_created", True), None),
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for index, (name, mutation, _) in enumerate(cases):
                with self.subTest(name=name):
                    boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(
                        root,
                        self.safe_json_filename(name, index),
                    )
                    if mutation == "boundary_array":
                        boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(
                            root,
                            self.safe_json_filename(name, index),
                            boundary_payload=[],
                        )
                    elif mutation == "lookup_array":
                        boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(
                            root,
                            self.safe_json_filename(name, index),
                            lookup_payload=[],
                        )
                    elif mutation == "boundary_not_recorded":
                        boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(
                            root,
                            self.safe_json_filename(name, index),
                            boundary_mutator=lambda artifact: artifact.__setitem__(
                                "outcome",
                                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BOUNDARY_NOT_RECORDED",
                            ),
                        )
                    elif mutation == "boundary_failed_checks":
                        boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(
                            root,
                            self.safe_json_filename(name, index),
                            boundary_mutator=lambda artifact: artifact.__setitem__(
                                "failed_check_count",
                                1,
                            ),
                        )
                    elif mutation == "boundary_bad_version":
                        boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(
                            root,
                            self.safe_json_filename(name, index),
                            boundary_mutator=lambda artifact: artifact.__setitem__(
                                "result_version",
                                "0.2.0",
                            ),
                        )
                    elif mutation == "lookup_not_recorded":
                        boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(
                            root,
                            self.safe_json_filename(name, index),
                            lookup_mutator=lambda artifact: artifact.__setitem__(
                                "outcome",
                                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_NOT_RECORDED",
                            ),
                        )
                    elif mutation == "lookup_failed_checks":
                        boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(
                            root,
                            self.safe_json_filename(name, index),
                            lookup_mutator=lambda artifact: artifact.__setitem__(
                                "failed_check_count",
                                1,
                            ),
                        )
                    elif mutation == "lookup_bad_version":
                        boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(
                            root,
                            self.safe_json_filename(name, index),
                            lookup_mutator=lambda artifact: artifact.__setitem__(
                                "result_version",
                                "0.2.0",
                            ),
                        )

                    if mutation == "non_mapping":
                        result = resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min(
                            ["not", "a", "mapping"]  # type: ignore[arg-type]
                        )
                    elif mutation == "empty_request":
                        result = resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min(
                            {}
                        )
                    else:
                        request = self.valid_request(boundary_path, lookup_path)
                        if callable(mutation):
                            mutation(request)
                        result = resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min(
                            request
                        )

                    self.assert_blocked_with_public_code(result)
                    self.assert_blocked_non_creation_posture(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(root)
            result = resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min(
                self.valid_request(boundary_path, lookup_path)
            )
            operation_permission = self.operation_permission(result)
            self.assertEqual(
                operation_permission["operation_permission_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION",
            )
            self.assertEqual(
                operation_permission["operation_permission_scope"],
                "SELECTED_OPERATION_PERMISSION_ONLY",
            )
            self.assertEqual(operation_permission["selected_command"], "state")
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            for outcome in (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BLOCKED",
            ):
                self.assertIn(outcome, resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn(
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_RECORDED",
                serialized,
            )
            for official in OFFICIAL_STRINGS:
                self.assertIn(official, serialized)
            self.assertNotIn("[REDACTED_SENSITIVE_CONTENT]", serialized)

    def test_raw_hidden_hostile_content_containment_and_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)

            def poison_boundary(artifact: dict[str, Any]) -> None:
                artifact["raw_operation_permission_boundary_body"] = (
                    "RAW_OPERATION_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN"
                )
                artifact["local_relevance_medium_read_only_operation_permission_boundary"][
                    "raw_body"
                ] = "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN"

            def poison_lookup(artifact: dict[str, Any]) -> None:
                artifact["raw_lookup_result_body"] = "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN"
                artifact["local_relevance_medium_read_only_lookup_result"][
                    "hidden_repo_state"
                ] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"

            boundary_path, lookup_path, boundary_artifact, lookup_artifact = (
                self.write_synthetic_artifacts(
                    root,
                    "hostile",
                    boundary_mutator=poison_boundary,
                    lookup_mutator=poison_lookup,
                )
            )
            request = self.valid_request(boundary_path, lookup_path)
            request["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
            request["raw_operation_permission_body"] = (
                "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_BODY_MUST_NOT_RETURN"
            )
            request["extra_section"] = {
                "raw_body": "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN"
            }
            request_before = copy.deepcopy(request)
            boundary_before = copy.deepcopy(boundary_artifact)
            lookup_before = copy.deepcopy(lookup_artifact)

            result = resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min(
                request
            )

            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assert_blocked_with_public_code(result)
            self.assert_no_hostile_sentinels(result)
            serialized = json.dumps(result, sort_keys=True)
            for official in OFFICIAL_STRINGS:
                self.assertIn(official, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assertIs(self.non_claims(result)["consumed_request_reopened"], False)
            self.assertIs(self.non_claims(result)["authorization_token_reused"], False)
            self.assert_blocked_non_creation_posture(result)
            self.assertEqual(request, request_before)
            self.assertEqual(boundary_artifact, boundary_before)
            self.assertEqual(lookup_artifact, lookup_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(root)
            request = self.valid_request(boundary_path, lookup_path)
            request_path = self.write_json(root / "request.json", request)

            result = resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            summary = result["local_relevance_medium_read_only_operation_permission_summary"]
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_read_only_operation_permission_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = (
                resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min_from_path(
                    malformed_path
                )
            )
            self.assert_blocked_with_public_code(malformed_result)
            array_path = self.write_json(root / "array.json", [])
            array_result = (
                resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min_from_path(
                    array_path
                )
            )
            self.assert_blocked_with_public_code(array_result)
            missing_result = (
                resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min_from_path(
                    root / "missing.json"
                )
            )
            self.assert_blocked_with_public_code(missing_result)

            patched_root = root / (
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
                "operation_permission_v0_min"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_root):
                first_path = (
                    resolver.write_local_relevance_medium_read_only_operation_permission_v0_min_result(
                        result
                    )
                )
                second_path = (
                    resolver.write_local_relevance_medium_read_only_operation_permission_v0_min_result(
                        result
                    )
                )
            self.assertTrue(first_path.parent.exists())
            self.assertTrue(second_path.parent.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIn(
                "local_relevance_medium_read_only_operation_permission_v0_min",
                str(first_path),
            )
            with first_path.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assert_not_under_forbidden_roots(first_path)
            self.assert_not_under_forbidden_roots(second_path)

    def test_resolver_does_not_mutate_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            boundary_path, lookup_path, boundary_artifact, lookup_artifact = (
                self.write_synthetic_artifacts(root)
            )
            request = self.valid_request(boundary_path, lookup_path)
            request["posture_mapping"] = {
                "operation_permission_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION",
                "operation_permission_scope": "SELECTED_OPERATION_PERMISSION_ONLY",
            }
            request["closure_tokens"] = {
                "consumed_request_reopened": False,
                "authorization_token_reused": False,
            }
            request["nested_raw_payload"] = {
                "raw_body": "RAW_OPERATION_PERMISSION_BODY_MUST_NOT_RETURN"
            }
            request_before = copy.deepcopy(request)
            declared_non_claims_before = copy.deepcopy(request["declared_non_claims"])
            boundary_path_before = request["selected_operation_permission_boundary_artifact"]
            lookup_path_before = request["selected_lookup_result_artifact"]
            selected_command_before = request["selected_command"]
            operation_permission_type_before = request["operation_permission_type"]
            operation_permission_scope_before = request["operation_permission_scope"]
            boundary_artifact_before = copy.deepcopy(boundary_artifact)
            lookup_artifact_before = copy.deepcopy(lookup_artifact)

            resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min(request)

            self.assertEqual(request, request_before)
            self.assertEqual(request["declared_non_claims"], declared_non_claims_before)
            self.assertEqual(
                request["selected_operation_permission_boundary_artifact"],
                boundary_path_before,
            )
            self.assertEqual(request["selected_lookup_result_artifact"], lookup_path_before)
            self.assertEqual(request["selected_command"], selected_command_before)
            self.assertEqual(request["operation_permission_type"], operation_permission_type_before)
            self.assertEqual(
                request["operation_permission_scope"],
                operation_permission_scope_before,
            )
            self.assertEqual(boundary_artifact, boundary_artifact_before)
            self.assertEqual(lookup_artifact, lookup_artifact_before)

    def test_predecessor_failure_and_closure_repair_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            boundary_path, lookup_path, _, _ = self.write_synthetic_artifacts(root)
            result = resolver.resolve_local_relevance_medium_read_only_operation_permission_v0_min(
                self.valid_request(boundary_path, lookup_path)
            )
            statement = self.statement(result)
            summary = result["local_relevance_medium_read_only_operation_permission_summary"]
            non_claims = self.non_claims(result)
            self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
            self.assertIs(non_claims["predecessor_failure_repaired"], False)
            self.assertIs(non_claims["predecessor_failure_hidden"], False)
            self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
            self.assertIs(statement["consumed_request_token_remains_closed"], True)
            self.assertIs(statement["authorization_token_reuse_blocked"], True)
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(summary["result_level_non_claims_canonical_false"], True)
            self.assertIs(summary["consumed_request_token_remains_closed"], True)
            self.assertIs(summary["authorization_token_reuse_blocked"], True)
            self.assertIs(non_claims["consumed_request_reopened"], False)
            self.assertIs(non_claims["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
