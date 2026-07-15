"""V2 tests for the local read-only local carrier command execution boundary.

This successor conformance suite preserves the v1 test as over-strict
failed-lineage evidence. V2 keeps the boundary object local, read-only,
single-command, and non-execution-shaped while correcting two v1 assertions:
recorded results need only serialize recorded-outcome official values, and
repo-default artifact paths may compare by resolution or stable filename suffix.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min as resolver


DEFAULT_SURFACE_ARTIFACT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_surface_v0_min"
    / "local_relevance_medium_read_only_local_carrier_command_surface_reference_review_001__local_relevance_medium_read_only_local_carrier_command_surface_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_metadata",
    "declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_question",
    "selected_local_carrier_command_surface_artifact_basis",
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary",
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_checks",
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_statement",
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_summary",
)

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_summary",
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_metadata",
)

BOUNDARY_FALSE_FIELDS = (
    "command_execution_performed",
    "command_execution_created",
    "command_execution_result_created",
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
    "state_returned",
    "lookup_performed",
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
    "action_created",
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "follow_on_work_authorized",
)

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_recorded",
    "basis_local_carrier_command_surface_artifact_preserved",
    "allowed_commands_preserved",
    "allowed_command_count_is_three",
    "selected_command_preserved",
    "selected_command_is_from_closed_command_set",
    "single_command_selected",
    "future_single_local_read_only_command_execution_may_be_considered",
    "local_carrier_command_surface_recorded",
    "command_surface_local_only",
    "command_surface_read_only",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_SURFACE_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RETURN_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def _json_safe(value: Any) -> str:
    return json.dumps(value, sort_keys=True)


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


def _surface_object(**overrides: Any) -> dict[str, Any]:
    surface = {
        "command_surface_id": "local_relevance_medium_read_only_local_carrier_command_surface_001",
        "command_surface_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE",
        "command_surface_version": "0.1.0",
        "command_surface_scope": "LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY",
        "allowed_commands": list(resolver.ALLOWED_COMMANDS),
        "allowed_command_count": 3,
        "state_command_available": True,
        "lookup_first_orientation_locator_command_available": True,
        "lookup_second_orientation_locator_command_available": True,
        "local_carrier_command_surface_recorded": True,
        "command_surface_local_only": True,
        "command_surface_read_only": True,
        "command_execution_performed": False,
        "command_execution_result_created": False,
        "operation_permission_created": False,
        "runtime_permission_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "general_lookup_permission_created": False,
        "arbitrary_lookup_permission_created": False,
        "unsupported_commands_permitted": False,
        "unsupported_lookup_keys_permitted": False,
    }
    surface.update(overrides)
    return surface


def _surface_artifact(
    *,
    outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_RECORDED",
    result_version: str = "0.1.0",
    failed_check_count: int = 0,
    surface_overrides: dict[str, Any] | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    artifact = {
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "local_relevance_medium_read_only_local_carrier_command_surface_metadata": {
            "result_version": result_version,
            "failed_check_count": failed_check_count,
        },
        "local_relevance_medium_read_only_local_carrier_command_surface": _surface_object(
            **(surface_overrides or {})
        ),
    }
    if extra:
        artifact.update(extra)
    return artifact


def _write_synthetic_surface_artifact(
    directory: Path,
    artifact: dict[str, Any] | None = None,
) -> Path:
    path = directory / "synthetic_local_carrier_command_surface_result.json"
    _write_json(path, artifact or _surface_artifact())
    return path


def _valid_request(surface_path: Path | str, **overrides: Any) -> dict[str, Any]:
    request = resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_request(
        selected_local_carrier_command_surface_artifact=surface_path
    )
    request.update(overrides)
    return request


class LocalCarrierCommandExecutionBoundaryV0MinV2Tests(unittest.TestCase):
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

    def boundary(self, result: dict[str, Any]) -> dict[str, Any]:
        boundary = result["local_relevance_medium_read_only_local_carrier_command_execution_boundary"]
        self.assertIsInstance(boundary, dict)
        return boundary

    def statement(self, result: dict[str, Any]) -> dict[str, Any]:
        statement = result[
            "local_relevance_medium_read_only_local_carrier_command_execution_boundary_statement"
        ]
        self.assertIsInstance(statement, dict)
        return statement

    def checks(self, result: dict[str, Any]) -> list[dict[str, Any]]:
        checks = result[
            "local_relevance_medium_read_only_local_carrier_command_execution_boundary_checks"
        ]
        self.assertIsInstance(checks, list)
        return checks

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        return block.get("block_code") or block.get("code")

    def assert_public_codes(self, result: dict[str, Any]) -> None:
        block_code = self.block_code(result)
        if block_code is not None:
            self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            code = check.get("block_code") or check.get("failure_code")
            if code is not None:
                self.assertIn(code, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: dict[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(type(non_claims[key]), bool)
            self.assertIs(non_claims[key], False)

    def assert_no_overreach_posture(self, result: dict[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        boundary = self.boundary(result)
        for field in BOUNDARY_FALSE_FIELDS:
            if field in boundary:
                self.assertIs(boundary[field], False, field)

    def assert_boundary_is_not_wrapper(self, result: dict[str, Any]) -> None:
        boundary = self.boundary(result)
        for field in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(field, boundary)

    def assert_allowed_commands_preserved(
        self,
        boundary: dict[str, Any],
        selected_command: str = "state",
    ) -> None:
        self.assertEqual(boundary["allowed_commands"], list(resolver.ALLOWED_COMMANDS))
        self.assertEqual(boundary["allowed_command_count"], 3)
        self.assertEqual(boundary["selected_command"], selected_command)
        self.assertIs(boundary["selected_command_is_from_closed_command_set"], True)
        self.assertIs(boundary["single_command_selected"], True)

    def assert_path_not_under_forbidden_roots(self, output_path: Path | str) -> None:
        for forbidden_root in FORBIDDEN_OUTPUT_ROOTS:
            self.assertFalse(
                _path_has_component_prefix(output_path, forbidden_root),
                f"{output_path} must not be under {forbidden_root}",
            )

    def assert_recorded_result_core(
        self,
        result: dict[str, Any],
        surface_path: Path,
        selected_command: str = "state",
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        summary = resolver.build_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_summary(
            result
        )
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        metadata = result[
            "local_relevance_medium_read_only_local_carrier_command_execution_boundary_metadata"
        ]
        self.assertEqual(
            metadata["local_relevance_medium_read_only_local_carrier_command_execution_boundary_id"],
            "local_relevance_medium_read_only_local_carrier_command_execution_boundary_001",
        )
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)

        boundary = self.boundary(result)
        self.assertEqual(
            boundary["boundary_id"],
            "local_relevance_medium_read_only_local_carrier_command_execution_boundary_001",
        )
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY",
        )
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(
            boundary["boundary_scope"],
            "SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_CONSIDERATION_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            boundary["basis_local_carrier_command_surface_artifact"],
            surface_path,
        )
        self.assertEqual(
            boundary["basis_local_carrier_command_surface_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_RECORDED",
        )
        self.assertEqual(boundary["basis_local_carrier_command_surface_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_local_carrier_command_surface_failed_check_count"], 0)
        self.assert_allowed_commands_preserved(boundary, selected_command=selected_command)
        self.assertIs(
            boundary["future_single_local_read_only_command_execution_may_be_considered"],
            True,
        )
        self.assertIs(boundary["local_carrier_command_surface_recorded"], True)
        self.assertIs(boundary["command_surface_local_only"], True)
        self.assertIs(boundary["command_surface_read_only"], True)
        self.assert_no_overreach_posture(result)
        self.assert_boundary_is_not_wrapper(result)

        statement = self.statement(result)
        for field in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIs(statement[field], True, field)

    def test_public_api_constants_and_default_builder(self) -> None:
        for public_name in (
            "resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_request",
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
            "ALLOWED_COMMANDS",
            "DEFAULT_SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, constant_name), constant_name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min",
        )
        self.assertTrue(Path(resolver.OUTPUT_ROOT).as_posix().endswith(EXPECTED_OUTPUT_ROOT.as_posix()))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY",
            resolver.SUPPORTED_BOUNDARY_TYPE_VALUES,
        )
        self.assertIn(
            "SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_CONSIDERATION_ONLY",
            resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES,
        )
        self.assertEqual(list(resolver.ALLOWED_COMMANDS), [
            "state",
            "lookup first_orientation_locator",
            "lookup second_orientation_locator",
        ])
        self.assertEqual(resolver.DEFAULT_SELECTED_COMMAND, "state")
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_BLOCKED",
        })

        request = resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_request()
        self.assertTrue(
            str(request["selected_local_carrier_command_surface_artifact"]).endswith(
                "local_relevance_medium_read_only_local_carrier_command_surface_reference_review_001__local_relevance_medium_read_only_local_carrier_command_surface_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], "state")
        self.assert_path_not_under_forbidden_roots(Path(resolver.OUTPUT_ROOT))

    def test_successful_recorded_result_from_synthetic_artifact_default_selected_command(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            surface_path = _write_synthetic_surface_artifact(temp_dir)
            request = _valid_request(surface_path)
            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
                request
            )
            self.assert_recorded_result_core(result, surface_path)

    def test_successful_recorded_result_for_each_allowed_selected_command(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            surface_path = _write_synthetic_surface_artifact(temp_dir)
            for selected_command in resolver.ALLOWED_COMMANDS:
                with self.subTest(selected_command=selected_command):
                    request = _valid_request(surface_path, selected_command=selected_command)
                    result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
                        request
                    )
                    self.assert_recorded_result_core(
                        result,
                        surface_path,
                        selected_command=selected_command,
                    )

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_SURFACE_ARTIFACT.exists():
            self.skipTest("Default local carrier command surface artifact is not present.")
        request = resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
            request
        )
        self.assert_recorded_result_core(result, DEFAULT_SURFACE_ARTIFACT)

    def test_required_non_claims_are_canonical_false_when_incoming_flipped(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            surface_path = _write_synthetic_surface_artifact(temp_dir)
            base_request = _valid_request(surface_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
                        request
                    )
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
                    self.assertGreater(
                        resolver.build_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_summary(
                            result
                        )["failed_check_count"],
                        0,
                    )
                    self.assert_public_codes(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_no_overreach_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        def rewrite_artifact(
            path: Path,
            *,
            outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_RECORDED",
            result_version: str = "0.1.0",
            failed_check_count: int = 0,
            surface_overrides: dict[str, Any] | None = None,
        ) -> None:
            _write_json(
                path,
                _surface_artifact(
                    outcome=outcome,
                    result_version=result_version,
                    failed_check_count=failed_check_count,
                    surface_overrides=surface_overrides,
                ),
            )

        def set_true(field: str) -> Callable[[dict[str, Any], Path], Any]:
            return lambda request, _path: request.__setitem__(field, True)

        cases: list[tuple[str, Callable[[dict[str, Any], Path], Any]]] = [
            (
                "explicit block intent",
                lambda request, _path: request.__setitem__(
                    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_intent",
                    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY",
                ),
            ),
            ("missing request", lambda _request, _path: {}),
            ("non-mapping request", lambda _request, _path: "not a mapping"),
            (
                "unsupported intent",
                lambda request, _path: request.__setitem__(
                    "local_relevance_medium_read_only_local_carrier_command_execution_boundary_intent",
                    "UNSUPPORTED_INTENT",
                ),
            ),
            (
                "local carrier command surface artifact path missing",
                lambda request, _path: request.__setitem__(
                    "selected_local_carrier_command_surface_artifact",
                    "",
                ),
            ),
            (
                "local carrier command surface artifact unreadable",
                lambda request, path: request.__setitem__(
                    "selected_local_carrier_command_surface_artifact",
                    str(path.parent / "missing_surface_artifact.json"),
                ),
            ),
            ("local carrier command surface artifact JSON array", lambda _request, path: _write_json(path, [])),
            (
                "local carrier command surface artifact not recorded",
                lambda _request, path: rewrite_artifact(
                    path,
                    outcome="LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_NOT_RECORDED",
                ),
            ),
            (
                "local carrier command surface artifact failed checks present",
                lambda _request, path: rewrite_artifact(path, failed_check_count=1),
            ),
            (
                "local carrier command surface artifact version not 0.1.0",
                lambda _request, path: rewrite_artifact(path, result_version="9.9.9"),
            ),
            (
                "allowed commands not exact",
                lambda _request, path: rewrite_artifact(
                    path,
                    surface_overrides={"allowed_commands": ["state"]},
                ),
            ),
            (
                "allowed command count not three",
                lambda _request, path: rewrite_artifact(
                    path,
                    surface_overrides={"allowed_command_count": 2},
                ),
            ),
            ("selected command missing", lambda request, _path: request.pop("selected_command", None)),
            (
                "selected command not in closed command set",
                lambda request, _path: request.__setitem__("selected_command", "lookup unsupported"),
            ),
            (
                "more than one selected command supplied",
                lambda request, _path: request.__setitem__(
                    "selected_command",
                    ["state", "lookup first_orientation_locator"],
                ),
            ),
            (
                "future single local read only command execution may not be considered",
                lambda request, _path: request.__setitem__(
                    "future_single_local_read_only_command_execution_may_be_considered",
                    False,
                ),
            ),
            (
                "local carrier command surface not recorded",
                lambda _request, path: rewrite_artifact(
                    path,
                    surface_overrides={"local_carrier_command_surface_recorded": False},
                ),
            ),
            (
                "command surface local only not true",
                lambda _request, path: rewrite_artifact(
                    path,
                    surface_overrides={"command_surface_local_only": False},
                ),
            ),
            (
                "command surface read only not true",
                lambda _request, path: rewrite_artifact(
                    path,
                    surface_overrides={"command_surface_read_only": False},
                ),
            ),
            ("boundary type missing", lambda request, _path: request.pop("boundary_type", None)),
            (
                "boundary type wrong",
                lambda request, _path: request.__setitem__("boundary_type", "WRONG_BOUNDARY"),
            ),
            ("boundary scope missing", lambda request, _path: request.pop("boundary_scope", None)),
            (
                "boundary scope wrong",
                lambda request, _path: request.__setitem__("boundary_scope", "WRONG_SCOPE"),
            ),
        ]

        for field in (
            "command_execution_performed",
            "command_execution_created",
            "command_execution_result_created",
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
            "state_returned",
            "lookup_performed",
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
            "source_created",
            "authority_created",
            "currentness_created",
            "truth_created",
            "action_created",
            "synchronization_created",
            "participation_authorized",
            "participant_role_created",
            "deployment_created",
            "public_release_created",
            "broader_reusable_permission_created",
            "follow_on_work_authorized",
            "artifact_existence_treated_as_command_execution_boundary_authority",
            "latest_file_posture_treated_as_command_execution_boundary_authority",
            "repo_local_availability_treated_as_command_execution_boundary_authority",
            "hidden_repo_state_used_as_command_execution_boundary_content",
            "hidden_repo_state_used_as_command_execution_boundary_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            cases.append((field, set_true(field)))

        cases.extend(
            [
                (
                    "required non-claim missing",
                    lambda request, _path: request["declared_non_claims"].pop(
                        "command_execution_performed",
                        None,
                    ),
                ),
                (
                    "required non-claim flipped",
                    lambda request, _path: request["declared_non_claims"].__setitem__(
                        "command_execution_performed",
                        True,
                    ),
                ),
            ]
        )

        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            for label, mutate in cases:
                with self.subTest(label=label):
                    surface_path = _write_synthetic_surface_artifact(temp_dir)
                    request = _valid_request(surface_path)
                    candidate = mutate(request, surface_path)
                    if candidate is None:
                        candidate = request
                    result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
                        candidate
                    )
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
                    self.assert_public_codes(result)
                    self.assertGreater(
                        resolver.build_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_summary(
                            result
                        )["failed_check_count"],
                        0,
                    )
                    self.assert_no_overreach_posture(result)

    def test_missing_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            surface_path = _write_synthetic_surface_artifact(temp_dir)
            base_request = _valid_request(surface_path)
            variants: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
                ("remove declared_non_claims", lambda request: request.pop("declared_non_claims", None)),
                ("empty declared_non_claims", lambda request: request.__setitem__("declared_non_claims", {})),
                (
                    "remove one required non-claim",
                    lambda request: request["declared_non_claims"].pop(
                        "command_execution_performed",
                        None,
                    ),
                ),
                (
                    "required non-claim string",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "command_execution_performed",
                        "false",
                    ),
                ),
                (
                    "required non-claim none",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "command_execution_performed",
                        None,
                    ),
                ),
            ]
            for label, mutate in variants:
                with self.subTest(label=label):
                    request = copy.deepcopy(base_request)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
                        request
                    )
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS},
                    )
                    self.assert_public_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved_without_overbroad_outcome_serialization(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            surface_path = _write_synthetic_surface_artifact(temp_dir)
            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
                _valid_request(surface_path)
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(set(resolver.OUTCOME_FAMILY), {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY_BLOCKED",
            })

            boundary = self.boundary(result)
            self.assertEqual(
                boundary["boundary_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY",
            )
            self.assertEqual(
                boundary["boundary_scope"],
                "SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_CONSIDERATION_ONLY",
            )
            self.assertEqual(boundary["allowed_commands"], list(resolver.ALLOWED_COMMANDS))
            self.assertIn(boundary["selected_command"], resolver.ALLOWED_COMMANDS)

            serialized = _json_safe(result)
            for value in (
                resolver.OUTCOME_RECORDED,
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY",
                "SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_CONSIDERATION_ONLY",
                "state",
                "lookup first_orientation_locator",
                "lookup second_orientation_locator",
            ):
                self.assertIn(value, serialized)
            self.assertNotIn("[REDACTED_OFFICIAL_VALUE]", serialized)
            self.assertNotIn("[REDACTED_RAW_CONTENT]", boundary["boundary_type"])

            blocked_result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
                _valid_request(surface_path, selected_command="unsupported command")
            )
            self.assertEqual(blocked_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assertIn(blocked_result["outcome"], resolver.OUTCOME_FAMILY)
            self.assertIn(blocked_result["outcome"], _json_safe(blocked_result))

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            artifact = _surface_artifact(
                extra={
                    "raw_local_carrier_command_surface_body": HOSTILE_SENTINELS[5],
                    "hidden_repo_state": HOSTILE_SENTINELS[-1],
                },
                surface_overrides={"raw_body": HOSTILE_SENTINELS[0]},
            )
            surface_path = _write_synthetic_surface_artifact(temp_dir, artifact)
            request = _valid_request(surface_path)
            request["raw_full_body"] = HOSTILE_SENTINELS[-2]
            request["hidden_repo_state"] = {"payload": HOSTILE_SENTINELS[-1]}
            original_request = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            serialized = _json_safe(result)
            for sentinel in HOSTILE_SENTINELS:
                self.assertNotIn(sentinel, serialized)
            self.assertIn(
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY",
                serialized,
            )
            self.assertIn("SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_CONSIDERATION_ONLY", serialized)
            self.assert_no_overreach_posture(result)
            self.assertEqual(request, original_request)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            surface_path = _write_synthetic_surface_artifact(temp_dir)
            request_path = temp_dir / "request.json"
            _write_json(request_path, _valid_request(surface_path))

            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_from_path(
                request_path
            )
            self.assert_recorded_result_core(result, surface_path)

            malformed_path = temp_dir / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            try:
                malformed_result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_from_path(
                    malformed_path
                )
            except resolver.LocalRelevanceMediumReadOnlyLocalCarrierCommandExecutionBoundaryV0MinError:
                malformed_result = None
            if malformed_result is not None:
                self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assert_public_codes(malformed_result)

            array_request_path = temp_dir / "array_request.json"
            _write_json(array_request_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_from_path(
                array_request_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(array_result)

            missing_path = temp_dir / "missing_request.json"
            try:
                missing_result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_from_path(
                    missing_path
                )
            except resolver.LocalRelevanceMediumReadOnlyLocalCarrierCommandExecutionBoundaryV0MinError:
                missing_result = None
            if missing_result is not None:
                self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assert_public_codes(missing_result)

            patched_root = temp_dir / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_root):
                output_path = resolver.write_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_result(
                    result
                )
                second_output_path = resolver.write_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_result(
                    result
                )

            self.assertTrue(output_path.exists())
            self.assertTrue(second_output_path.exists())
            self.assertNotEqual(output_path, second_output_path)
            self.assertEqual(json.loads(output_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn(
                "local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min",
                output_path.as_posix(),
            )
            self.assert_path_not_under_forbidden_roots(output_path)
            self.assert_path_not_under_forbidden_roots(second_output_path)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            artifact = _surface_artifact(
                extra={"raw_full_body": {"sentinel": HOSTILE_SENTINELS[-2]}},
                surface_overrides={"raw_body": {"nested": HOSTILE_SENTINELS[0]}},
            )
            original_artifact = copy.deepcopy(artifact)
            surface_path = _write_synthetic_surface_artifact(temp_dir, artifact)
            request = _valid_request(
                surface_path,
                selected_command="lookup first_orientation_locator",
            )
            request["local_cache"] = {"sentinel": HOSTILE_SENTINELS[-1]}
            original_request = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
                request
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(request, original_request)
            self.assertEqual(artifact, original_artifact)
            self.assertEqual(
                request["selected_local_carrier_command_surface_artifact"],
                original_request["selected_local_carrier_command_surface_artifact"],
            )
            self.assertEqual(request["selected_command"], "lookup first_orientation_locator")
            self.assertEqual(
                request["boundary_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_BOUNDARY",
            )
            self.assertEqual(
                request["boundary_scope"],
                "SINGLE_LOCAL_READ_ONLY_COMMAND_EXECUTION_CONSIDERATION_ONLY",
            )
            self.assertEqual(request["allowed_commands"], list(resolver.ALLOWED_COMMANDS))
            self.assert_no_overreach_posture(result)

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            surface_path = _write_synthetic_surface_artifact(temp_dir)
            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min(
                _valid_request(surface_path)
            )
            summary = resolver.build_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min_summary(
                result
            )
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
            self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
            self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
            self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
            self.assertIs(result["non_claims"]["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
