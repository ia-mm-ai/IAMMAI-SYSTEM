"""Tests for the selected-state command execution result boundary resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY
object. It verifies that the resolver reads one clean selected-state command
execution artifact, records one local read-only result-consideration boundary,
and keeps command execution result, state payload return, state result object,
lookup, permissions, public/distributed surfaces, registry/search/query/ranking,
filesystem discovery, source transfer, participation, and follow-on work out of
the boundary object and result-level posture.
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

import resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min as resolver  # noqa: E402


DEFAULT_COMMAND_EXECUTION_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_execution_v0_min/"
    "local_relevance_medium_read_only_local_carrier_command_execution_reference_"
    "review_001__local_relevance_medium_read_only_local_carrier_command_"
    "execution_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_execution_result_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_surface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_reusable_lookup_permission_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_pair_coverage_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_lookup_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_index_system_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_comparison_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_relation_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_multiplicity_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_reception_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_successor_candidate_admission_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_successor_reception_request_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_loop_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_metadata",
    "declared_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_question",
    "selected_command_execution_artifact_basis",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_checks",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_statement",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_summary",
)

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_summary",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_metadata",
)

BOUNDARY_FALSE_FIELDS = (
    "command_execution_result_created",
    "state_payload_returned",
    "state_result_object_created",
    "lookup_performed",
    "lookup_command_executed",
    "operation_permission_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_commands_permitted",
    "unsupported_lookup_keys_permitted",
    "new_lookup_result_created",
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
)

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_recorded",
    "basis_command_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_command_execution_recorded",
    "command_execution_performed",
    "command_execution_local_only",
    "command_execution_read_only",
    "future_command_execution_result_may_be_considered",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
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


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _path_has_component_prefix(candidate: Path | str, root: Path | str) -> bool:
    candidate_parts = Path(candidate).parts
    root_parts = Path(root).parts
    if not root_parts or len(root_parts) > len(candidate_parts):
        return False
    return any(
        candidate_parts[index : index + len(root_parts)] == root_parts
        for index in range(0, len(candidate_parts) - len(root_parts) + 1)
    )


def _command_execution_object(**overrides: Any) -> dict[str, Any]:
    execution = {
        "command_execution_id": "local_relevance_medium_read_only_local_carrier_command_execution_001",
        "command_execution_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION",
        "command_execution_version": "0.1.0",
        "command_execution_scope": "SINGLE_LOCAL_READ_ONLY_STATE_COMMAND_EXECUTION_ONLY",
        "basis_command_execution_boundary_outcome": (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_RECORDED"
        ),
        "basis_command_execution_boundary_result_version": "0.1.0",
        "basis_command_execution_boundary_failed_check_count": 0,
        "basis_local_carrier_command_surface_outcome": (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_RECORDED"
        ),
        "basis_local_carrier_command_surface_result_version": "0.1.0",
        "basis_local_carrier_command_surface_failed_check_count": 0,
        "allowed_commands": [
            "state",
            "lookup first_orientation_locator",
            "lookup second_orientation_locator",
        ],
        "allowed_command_count": 3,
        "selected_command": "state",
        "selected_command_is_state": True,
        "selected_command_is_from_closed_command_set": True,
        "single_command_selected": True,
        "local_carrier_command_execution_recorded": True,
        "command_execution_performed": True,
        "command_execution_local_only": True,
        "command_execution_read_only": True,
        "command_execution_result_created": False,
        "state_payload_returned": False,
        "state_result_object_created": False,
        "lookup_performed": False,
        "lookup_command_executed": False,
        "operation_permission_created": False,
        "runtime_permission_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "general_lookup_permission_created": False,
        "arbitrary_lookup_permission_created": False,
        "unsupported_commands_permitted": False,
        "unsupported_lookup_keys_permitted": False,
        "new_lookup_result_created": False,
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
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "authority_created": False,
        "currentness_created": False,
        "truth_created": False,
        "synchronization_created": False,
        "participation_authorized": False,
        "participant_role_created": False,
        "follow_on_work_authorized": False,
    }
    execution.update(overrides)
    return execution


def _command_execution_artifact(
    *,
    outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RECORDED",
    result_version: str = "0.1.0",
    failed_check_count: int = 0,
    execution_overrides: dict[str, Any] | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    artifact = {
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "local_relevance_medium_read_only_local_carrier_command_execution_metadata": {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "resolver_module": (
                "resolve_local_relevance_medium_read_only_local_carrier_"
                "command_execution_v0_min"
            ),
        },
        "local_relevance_medium_read_only_local_carrier_command_execution": (
            _command_execution_object(**(execution_overrides or {}))
        ),
        "local_relevance_medium_read_only_local_carrier_command_execution_checks": [
            {"check_name": "synthetic clean command execution", "passed": failed_check_count == 0}
        ],
        "local_relevance_medium_read_only_local_carrier_command_execution_summary": {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
        },
    }
    if extra:
        artifact.update(extra)
    return artifact


def _write_command_execution_artifact(
    directory: Path,
    artifact: dict[str, Any] | None = None,
    name: str = "synthetic_command_execution_result.json",
) -> Path:
    path = directory / name
    _write_json(path, artifact or _command_execution_artifact())
    return path


def _valid_request(command_execution_artifact: Path | str, **overrides: Any) -> dict[str, Any]:
    request = (
        resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_request(
            selected_command_execution_artifact=command_execution_artifact
        )
    )
    request.update(overrides)
    return request


def _synthetic_request(directory: Path) -> tuple[dict[str, Any], Path]:
    command_execution_path = _write_command_execution_artifact(directory)
    return _valid_request(command_execution_path), command_execution_path


class LocalCarrierCommandExecutionResultBoundaryV0MinTests(unittest.TestCase):
    def assert_not_blocked(self, result):
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_same_or_stable_artifact_path(self, actual, expected):
        actual_path = Path(actual)
        expected_path = Path(expected)
        if actual_path.is_absolute() and expected_path.is_absolute():
            self.assertEqual(actual_path, expected_path)
            return
        if actual_path.exists() or expected_path.exists():
            self.assertEqual(actual_path.resolve(), expected_path.resolve())
            return
        self.assertTrue(str(actual).endswith(expected_path.name))

    def boundary(self, result: Mapping[str, Any]) -> dict[str, Any]:
        boundary = result[
            "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary"
        ]
        self.assertIsInstance(boundary, dict)
        return boundary

    def statement(self, result: Mapping[str, Any]) -> dict[str, Any]:
        statement = result[
            "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_statement"
        ]
        self.assertIsInstance(statement, dict)
        return statement

    def checks(self, result: Mapping[str, Any]) -> list[dict[str, Any]]:
        checks = result[
            "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_checks"
        ]
        self.assertIsInstance(checks, list)
        return checks

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        return block.get("block_code") or block.get("code")

    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        block_code = self.block_code(result)
        if block_code is not None:
            self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            code = check.get("block_code") or check.get("failure_code")
            if code is not None:
                self.assertIn(code, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(type(non_claims[key]), bool)
            self.assertIs(non_claims[key], False)

    def assert_boundary_false_posture(self, boundary: Mapping[str, Any]) -> None:
        for field in BOUNDARY_FALSE_FIELDS:
            self.assertIn(field, boundary)
            self.assertIs(boundary[field], False, field)

    def assert_no_result_behaviors(self, result: Mapping[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        self.assert_boundary_false_posture(self.boundary(result))

    def assert_boundary_is_not_wrapper(self, boundary: Mapping[str, Any]) -> None:
        for field in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(field, boundary)

    def assert_selected_state_result_boundary_posture(
        self,
        boundary: Mapping[str, Any],
        command_execution_path: Path | str,
    ) -> None:
        self.assertEqual(
            boundary["boundary_id"],
            "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_001",
        )
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY",
        )
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_STATE_COMMAND_EXECUTION_RESULT_CONSIDERATION_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            boundary["basis_command_execution_artifact"],
            command_execution_path,
        )
        self.assertEqual(
            boundary["basis_command_execution_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RECORDED",
        )
        self.assertEqual(boundary["basis_command_execution_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_command_execution_failed_check_count"], 0)
        self.assertEqual(boundary["selected_command"], "state")
        self.assertIs(boundary["selected_command_is_state"], True)
        self.assertIs(boundary["selected_command_execution_recorded"], True)
        self.assertIs(boundary["command_execution_performed"], True)
        self.assertIs(boundary["command_execution_local_only"], True)
        self.assertIs(boundary["command_execution_read_only"], True)
        self.assertIs(boundary["future_command_execution_result_may_be_considered"], True)
        self.assert_boundary_false_posture(boundary)
        self.assert_boundary_is_not_wrapper(boundary)

    def assert_recorded_result_core(
        self,
        result: Mapping[str, Any],
        command_execution_path: Path | str,
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        summary = (
            resolver.build_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_summary(
                result
            )
        )
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(
            summary["boundary_id"],
            "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_001",
        )

        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        boundary = self.boundary(result)
        self.assert_selected_state_result_boundary_posture(boundary, command_execution_path)

        statement = self.statement(result)
        for field in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIn(field, statement)
            self.assertIs(statement[field], True, field)

        self.assert_non_claims_canonical_false(result)

    def assert_no_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_values_present(self, serialized: str) -> None:
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY",
            serialized,
        )
        self.assertIn("SELECTED_STATE_COMMAND_EXECUTION_RESULT_CONSIDERATION_ONLY", serialized)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED",
            serialized,
        )
        self.assertIn("state", serialized)

    def assert_path_not_under_forbidden_roots(self, output_path: Path | str) -> None:
        for forbidden_root in FORBIDDEN_OUTPUT_ROOTS:
            self.assertFalse(
                _path_has_component_prefix(output_path, forbidden_root),
                f"{output_path} must not be under {forbidden_root}",
            )

    def test_public_api_constants_and_default_builder(self) -> None:
        for public_name in (
            "resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, public_name)))

        for constant_name in (
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
            self.assertTrue(hasattr(resolver, constant_name), constant_name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min",
        )
        self.assertTrue(Path(resolver.OUTPUT_ROOT).as_posix().endswith(EXPECTED_OUTPUT_ROOT.as_posix()))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY",
            resolver.SUPPORTED_BOUNDARY_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_STATE_COMMAND_EXECUTION_RESULT_CONSIDERATION_ONLY",
            resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_BLOCKED",
            },
        )

        request = (
            resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_request()
        )
        self.assertTrue(
            str(request["selected_command_execution_artifact"]).endswith(
                "local_relevance_medium_read_only_local_carrier_command_execution_reference_review_001__local_relevance_medium_read_only_local_carrier_command_execution_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], "state")
        self.assert_path_not_under_forbidden_roots(Path(resolver.OUTPUT_ROOT))

    def test_successful_recorded_result_from_synthetic_command_execution_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            request, command_execution_path = _synthetic_request(Path(temp_dir_name))
            result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min(
                    request
                )
            )
            self.assert_recorded_result_core(result, command_execution_path)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_COMMAND_EXECUTION_ARTIFACT.exists():
            self.skipTest("default selected-state command execution artifact is not present")

        request = (
            resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_request()
        )
        result = (
            resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min(
                request
            )
        )
        self.assert_recorded_result_core(result, DEFAULT_COMMAND_EXECUTION_ARTIFACT)

    def test_required_false_non_claims_canonicalize_illegal_true(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            request, _ = _synthetic_request(Path(temp_dir_name))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    mutated = copy.deepcopy(request)
                    mutated["declared_non_claims"][key] = True
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min(
                            mutated
                        )
                    )
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
                    summary = (
                        resolver.build_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_summary(
                            result
                        )
                    )
                    self.assertGreater(summary["failed_check_count"], 0)
                    self.assert_public_codes(result)
                    self.assert_no_result_behaviors(result)
                    self.assertIs(result["non_claims"][key], False)

    def _block_cases(self, base_dir: Path) -> list[tuple[str, Callable[[], Any]]]:
        def valid() -> dict[str, Any]:
            request, _ = _synthetic_request(base_dir)
            return request

        def with_command_execution_artifact(artifact: dict[str, Any]) -> dict[str, Any]:
            request = valid()
            path = base_dir / f"command_execution_case_{len(list(base_dir.glob('command_execution_case_*')))}.json"
            _write_json(path, artifact)
            request["selected_command_execution_artifact"] = str(path)
            return request

        cases: list[tuple[str, Callable[[], Any]]] = [
            ("explicit block intent", lambda: dict(valid(), local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_intent=resolver.INTENT_BLOCK)),
            ("missing request", lambda: {}),
            ("non-mapping request", lambda: ["not", "a", "mapping"]),
            ("unsupported intent", lambda: dict(valid(), local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_intent="UNSUPPORTED_INTENT")),
            ("command execution artifact path missing", lambda: dict(valid(), selected_command_execution_artifact="")),
            ("command execution artifact unreadable", lambda: dict(valid(), selected_command_execution_artifact=str(base_dir / "missing_command_execution.json"))),
            ("command execution artifact JSON array", lambda: dict(valid(), selected_command_execution_artifact=str(_write_array_file(base_dir / "command_execution_array.json")))),
            (
                "command execution artifact not recorded",
                lambda: with_command_execution_artifact(
                    _command_execution_artifact(
                        outcome="LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_NOT_RECORDED"
                    )
                ),
            ),
            (
                "command execution artifact failed checks present",
                lambda: with_command_execution_artifact(
                    _command_execution_artifact(failed_check_count=1)
                ),
            ),
            (
                "command execution artifact version not 0.1.0",
                lambda: with_command_execution_artifact(
                    _command_execution_artifact(result_version="9.9.9")
                ),
            ),
            ("selected command missing", lambda: _without(valid(), "selected_command")),
            ("selected command not state", lambda: dict(valid(), selected_command="lookup first_orientation_locator")),
            (
                "selected command execution not recorded",
                lambda: with_command_execution_artifact(
                    _command_execution_artifact(
                        execution_overrides={"local_carrier_command_execution_recorded": False}
                    )
                ),
            ),
            (
                "command execution not performed",
                lambda: with_command_execution_artifact(
                    _command_execution_artifact(
                        execution_overrides={"command_execution_performed": False}
                    )
                ),
            ),
            (
                "command execution local only not true",
                lambda: with_command_execution_artifact(
                    _command_execution_artifact(
                        execution_overrides={"command_execution_local_only": False}
                    )
                ),
            ),
            (
                "command execution read only not true",
                lambda: with_command_execution_artifact(
                    _command_execution_artifact(
                        execution_overrides={"command_execution_read_only": False}
                    )
                ),
            ),
            ("future command execution result may not be considered", lambda: dict(valid(), future_command_execution_result_may_be_considered=False)),
            ("boundary type missing", lambda: _without(valid(), "boundary_type")),
            ("boundary type wrong", lambda: dict(valid(), boundary_type="LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT")),
            ("boundary scope missing", lambda: _without(valid(), "boundary_scope")),
            ("boundary scope wrong", lambda: dict(valid(), boundary_scope="COMMAND_EXECUTION_RESULT_SCOPE")),
            ("predecessor failure repaired", lambda: dict(valid(), predecessor_failure_repaired=True)),
            ("predecessor failure hidden", lambda: dict(valid(), predecessor_failure_hidden=True)),
            ("predecessor failure claimed passed", lambda: dict(valid(), predecessor_failure_claimed_passed=True)),
            ("consumed request reopened", lambda: dict(valid(), consumed_request_reopened=True)),
            ("authorization token reused", lambda: dict(valid(), authorization_token_reused=True)),
            ("required non-claim missing", lambda: _without_nested(valid(), "declared_non_claims", "command_execution_result_created")),
            ("required non-claim flipped", lambda: _flip_declared_non_claim(valid(), "command_execution_result_created")),
        ]
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            cases.append((f"{field} asserted", lambda field=field: dict(valid(), **{field: True})))
        return cases

    def test_representative_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            base_dir = Path(temp_dir_name)
            for name, request_factory in self._block_cases(base_dir):
                with self.subTest(name=name):
                    request = request_factory()
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min(
                            request
                        )
                    )
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
                    self.assert_public_codes(result)
                    self.assert_no_result_behaviors(result)

    def test_missing_or_incomplete_declared_non_claims_still_emit_canonical_false(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            request, _ = _synthetic_request(Path(temp_dir_name))
            required_key = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            variants = {
                "removed declared_non_claims": _without(copy.deepcopy(request), "declared_non_claims"),
                "empty declared_non_claims": dict(copy.deepcopy(request), declared_non_claims={}),
                "one non-claim removed": _without_nested(
                    copy.deepcopy(request), "declared_non_claims", required_key
                ),
                "one non-claim string": _with_nested(
                    copy.deepcopy(request), "declared_non_claims", required_key, "false"
                ),
                "one non-claim none": _with_nested(
                    copy.deepcopy(request), "declared_non_claims", required_key, None
                ),
            }
            for name, variant in variants.items():
                with self.subTest(name=name):
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min(
                            variant
                        )
                    )
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS},
                    )
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
                    self.assert_public_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            request, command_execution_path = _synthetic_request(Path(temp_dir_name))
            result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min(
                    request
                )
            )
            self.assert_recorded_result_core(result, command_execution_path)
            boundary = self.boundary(result)
            self.assertEqual(
                boundary["boundary_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY",
            )
            self.assertEqual(
                boundary["boundary_scope"],
                "SELECTED_STATE_COMMAND_EXECUTION_RESULT_CONSIDERATION_ONLY",
            )
            self.assertEqual(boundary["selected_command"], "state")
            serialized = json.dumps(result, sort_keys=True)
            self.assert_official_values_present(serialized)
            self.assertNotIn("[REDACTED_RAW_CONTENT]", serialized)
            for expected in (
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_BLOCKED,
            ):
                self.assertIn(expected, resolver.OUTCOME_FAMILY)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            command_execution_artifact = _command_execution_artifact(
                extra={
                    "raw_command_execution_body": HOSTILE_SENTINELS[7],
                    "hidden_repo_state": {"value": HOSTILE_SENTINELS[-1]},
                }
            )
            command_execution_path = _write_command_execution_artifact(
                temp_dir, command_execution_artifact
            )
            request = _valid_request(command_execution_path)
            request["raw_full_body"] = HOSTILE_SENTINELS[-2]
            request["hidden_repo_state"] = {"sentinel": HOSTILE_SENTINELS[-1]}
            request["extra"] = {"raw_state_payload_body": HOSTILE_SENTINELS[3]}
            original_request = copy.deepcopy(request)

            result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min(
                    request
                )
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assert_no_sentinels(result)
            self.assert_official_values_present(json.dumps(result, sort_keys=True))
            self.assert_no_result_behaviors(result)
            self.assertEqual(request, original_request)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            request, _ = _synthetic_request(temp_dir)
            request_path = temp_dir / "request.json"
            _write_json(request_path, request)

            result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_from_path(
                    request_path
                )
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assert_not_blocked(result)
            summary = (
                resolver.build_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_summary(
                    result
                )
            )
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = temp_dir / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_from_path(
                    malformed_path
                )
            )
            self.assertEqual(malformed["outcome"], resolver.OUTCOME_BLOCKED)
            self.assertIn(self.block_code(malformed), resolver.BLOCK_CODES)

            array_path = _write_array_file(temp_dir / "request_array.json")
            array_result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_from_path(
                    array_path
                )
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assertIn(self.block_code(array_result), resolver.BLOCK_CODES)

            missing_result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_from_path(
                    temp_dir / "missing_request.json"
                )
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assertIn(self.block_code(missing_result), resolver.BLOCK_CODES)

            output_root = temp_dir / EXPECTED_OUTPUT_ROOT.name
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = (
                    resolver.write_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_result(
                        result
                    )
                )
                second_path = (
                    resolver.write_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_result(
                        result
                    )
                )

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn(EXPECTED_OUTPUT_ROOT.name, first_path.parts)
            self.assert_path_not_under_forbidden_roots(first_path)
            self.assert_path_not_under_forbidden_roots(second_path)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            command_execution_artifact = _command_execution_artifact(
                extra={"raw_full_body": {"sentinel": HOSTILE_SENTINELS[-2]}}
            )
            original_command_execution_artifact = copy.deepcopy(command_execution_artifact)
            command_execution_path = _write_command_execution_artifact(
                temp_dir, command_execution_artifact
            )
            request = _valid_request(command_execution_path)
            request["raw_state_payload_body"] = HOSTILE_SENTINELS[3]
            original_request = copy.deepcopy(request)
            original_declared_non_claims = copy.deepcopy(request["declared_non_claims"])

            resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min(
                request
            )

            self.assertEqual(request, original_request)
            self.assertEqual(request["declared_non_claims"], original_declared_non_claims)
            self.assertEqual(request["selected_command_execution_artifact"], str(command_execution_path))
            self.assertEqual(request["selected_command"], "state")
            self.assertEqual(
                request["boundary_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY",
            )
            self.assertEqual(
                request["boundary_scope"],
                "SELECTED_STATE_COMMAND_EXECUTION_RESULT_CONSIDERATION_ONLY",
            )
            self.assertEqual(command_execution_artifact, original_command_execution_artifact)

    def test_predecessor_failure_and_token_posture_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            request, command_execution_path = _synthetic_request(Path(temp_dir_name))
            result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min(
                    request
                )
            )
            self.assert_recorded_result_core(result, command_execution_path)
            summary = (
                resolver.build_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min_summary(
                    result
                )
            )
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            non_claims = result["non_claims"]
            self.assertIs(non_claims["predecessor_failure_repaired"], False)
            self.assertIs(non_claims["predecessor_failure_hidden"], False)
            self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
            self.assertIs(non_claims["consumed_request_reopened"], False)
            self.assertIs(non_claims["authorization_token_reused"], False)
            check_names = {check["check_name"] for check in self.checks(result)}
            self.assertIn("predecessor failure evidence preserved", check_names)
            self.assertIn("consumed request remains closed", check_names)
            self.assertIn("authorization token not reused", check_names)


def _write_array_file(path: Path) -> Path:
    _write_json(path, [{"not": "an object"}])
    return path


def _without(mapping: dict[str, Any], key: str) -> dict[str, Any]:
    mapping.pop(key, None)
    return mapping


def _without_nested(mapping: dict[str, Any], parent: str, key: str) -> dict[str, Any]:
    nested = mapping.get(parent)
    if isinstance(nested, dict):
        nested.pop(key, None)
    return mapping


def _with_nested(
    mapping: dict[str, Any],
    parent: str,
    key: str,
    value: Any,
) -> dict[str, Any]:
    nested = mapping.setdefault(parent, {})
    if isinstance(nested, dict):
        nested[key] = value
    return mapping


def _flip_declared_non_claim(mapping: dict[str, Any], key: str) -> dict[str, Any]:
    nested = mapping.setdefault("declared_non_claims", {})
    if isinstance(nested, dict):
        nested[key] = True
    return mapping


if __name__ == "__main__":
    unittest.main()
