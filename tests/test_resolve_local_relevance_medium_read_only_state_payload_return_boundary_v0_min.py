"""Tests for the selected-state state payload return boundary resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY object. It
verifies that the resolver reads one clean selected-state command execution
result artifact, records one local read-only payload-return-consideration
boundary, and keeps state payload return, state result object creation, state
packet body exposure, lookup, permissions, public/distributed surfaces,
registry/search/query/ranking, filesystem discovery, source transfer,
participation, and follow-on work out of the boundary object and result-level
posture.
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

import resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min as resolver  # noqa: E402


DEFAULT_COMMAND_EXECUTION_RESULT_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_execution_result_v0_min/"
    "local_relevance_medium_read_only_local_carrier_command_execution_result_"
    "reference_review_001__local_relevance_medium_read_only_local_carrier_"
    "command_execution_result_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_payload_return_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min"),
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
    "local_relevance_medium_read_only_state_payload_return_boundary_metadata",
    "declared_local_relevance_medium_read_only_state_payload_return_boundary_question",
    "selected_command_execution_result_artifact_basis",
    "local_relevance_medium_read_only_state_payload_return_boundary",
    "local_relevance_medium_read_only_state_payload_return_boundary_checks",
    "local_relevance_medium_read_only_state_payload_return_boundary_statement",
    "local_relevance_medium_read_only_state_payload_return_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_state_payload_return_boundary_summary",
)

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_state_payload_return_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_state_payload_return_boundary_summary",
    "local_relevance_medium_read_only_state_payload_return_boundary_metadata",
)

BOUNDARY_FALSE_FIELDS = (
    "state_payload_returned",
    "state_result_object_created",
    "state_packet_body_exposed",
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
    "local_relevance_medium_read_only_state_payload_return_boundary_recorded",
    "basis_command_execution_result_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_state_command_execution_result_recorded",
    "command_execution_result_created",
    "command_execution_result_local_only",
    "command_execution_result_read_only",
    "future_state_payload_return_may_be_considered",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_RETURN_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
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


def _set(mapping: dict[str, Any], key: str, value: Any) -> None:
    mapping[key] = value


def _pop(mapping: dict[str, Any], key: str) -> None:
    mapping.pop(key, None)


def _command_execution_result_object(**overrides: Any) -> dict[str, Any]:
    result_object = {
        "command_execution_result_id": "local_relevance_medium_read_only_local_carrier_command_execution_result_001",
        "command_execution_result_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT",
        "command_execution_result_version": "0.1.0",
        "command_execution_result_scope": "SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY",
        "basis_command_execution_result_boundary_artifact": "synthetic-boundary.json",
        "basis_command_execution_result_boundary_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED",
        "basis_command_execution_result_boundary_result_version": "0.1.0",
        "basis_command_execution_result_boundary_failed_check_count": 0,
        "basis_command_execution_artifact": "synthetic-command-execution.json",
        "basis_command_execution_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RECORDED",
        "basis_command_execution_result_version": "0.1.0",
        "basis_command_execution_failed_check_count": 0,
        "selected_command": "state",
        "selected_command_is_state": True,
        "selected_command_execution_recorded": True,
        "command_execution_performed": True,
        "command_execution_local_only": True,
        "command_execution_read_only": True,
        "local_carrier_command_execution_result_recorded": True,
        "command_execution_result_created": True,
        "command_execution_result_local_only": True,
        "command_execution_result_read_only": True,
    }
    for field in BOUNDARY_FALSE_FIELDS:
        result_object[field] = False
    result_object.update(overrides)
    return result_object


def _command_execution_result_artifact(**object_overrides: Any) -> dict[str, Any]:
    result_object = _command_execution_result_object(**object_overrides)
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_RECORDED",
        "result_version": "0.1.0",
        "failed_check_count": 0,
        "local_relevance_medium_read_only_local_carrier_command_execution_result_metadata": {
            "result_version": "0.1.0",
            "failed_check_count": 0,
        },
        "local_relevance_medium_read_only_local_carrier_command_execution_result_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "local_relevance_medium_read_only_local_carrier_command_execution_result_recorded": True,
            "command_execution_result_created": True,
            "command_execution_result_local_only": True,
            "command_execution_result_read_only": True,
        },
        "local_relevance_medium_read_only_local_carrier_command_execution_result_checks": [
            {"check_name": "synthetic clean command execution result", "passed": True}
        ],
        "local_relevance_medium_read_only_local_carrier_command_execution_result_statement": {
            "local_relevance_medium_read_only_local_carrier_command_execution_result_recorded": True,
            "selected_command_is_state": True,
            "command_execution_result_created": True,
            "command_execution_result_local_only": True,
            "command_execution_result_read_only": True,
            "result_level_non_claims_canonical_false": True,
        },
        "local_relevance_medium_read_only_local_carrier_command_execution_result": result_object,
    }


def _write_synthetic_artifact(
    directory: Path,
    *,
    object_overrides: Mapping[str, Any] | None = None,
    artifact_overrides: Mapping[str, Any] | None = None,
) -> tuple[Path, dict[str, Any]]:
    artifact_path = directory / "synthetic_command_execution_result.json"
    artifact = _command_execution_result_artifact(**dict(object_overrides or {}))
    if artifact_overrides:
        artifact.update(dict(artifact_overrides))
    _write_json(artifact_path, artifact)
    return artifact_path, artifact


def _build_request(artifact_path: Path, **overrides: Any) -> dict[str, Any]:
    request = (
        resolver.build_declared_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_request(
            selected_command_execution_result_artifact=str(artifact_path)
        )
    )
    request.update(overrides)
    return request


def _boundary(result: Mapping[str, Any]) -> dict[str, Any]:
    value = result.get("local_relevance_medium_read_only_state_payload_return_boundary")
    return dict(value) if isinstance(value, Mapping) else {}


def _statement(result: Mapping[str, Any]) -> dict[str, Any]:
    value = result.get(
        "local_relevance_medium_read_only_state_payload_return_boundary_statement"
    )
    return dict(value) if isinstance(value, Mapping) else {}


def _checks(result: Mapping[str, Any]) -> list[dict[str, Any]]:
    value = result.get("local_relevance_medium_read_only_state_payload_return_boundary_checks")
    if not isinstance(value, list):
        return []
    return [dict(item) for item in value if isinstance(item, Mapping)]


def _summary(result: Mapping[str, Any]) -> dict[str, Any]:
    value = result.get("local_relevance_medium_read_only_state_payload_return_boundary_summary")
    return dict(value) if isinstance(value, Mapping) else {}


class StatePayloadReturnBoundaryResolverTests(unittest.TestCase):
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

    def assert_all_block_codes_public(self, result: Mapping[str, Any]) -> None:
        for check in _checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIs(type(non_claims[key]), bool)

    def assert_boundary_not_wrapper(self, boundary: Mapping[str, Any]) -> None:
        for key in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(key, boundary)

    def assert_no_payload_lookup_permission_or_follow_on(
        self, result: Mapping[str, Any]
    ) -> None:
        boundary = _boundary(result)
        for field in BOUNDARY_FALSE_FIELDS:
            self.assertIn(field, boundary)
            self.assertIs(boundary[field], False)
        self.assert_non_claims_canonical_false(result)

    def assert_blocked_result(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        code = block.get("block_code") or block.get("code")
        self.assertIsInstance(code, str)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(_summary(result).get("failed_check_count", 0), 0)
        self.assert_all_block_codes_public(result)
        self.assert_no_payload_lookup_permission_or_follow_on(result)

    def assert_recorded_boundary(
        self, result: Mapping[str, Any], artifact_path: Path
    ) -> None:
        boundary = _boundary(result)
        self.assertEqual(
            boundary["boundary_id"],
            "local_relevance_medium_read_only_state_payload_return_boundary_001",
        )
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY",
        )
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_STATE_PAYLOAD_RETURN_CONSIDERATION_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            boundary["basis_command_execution_result_artifact"],
            artifact_path,
        )
        self.assertEqual(
            boundary["basis_command_execution_result_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_RECORDED",
        )
        self.assertEqual(
            boundary["basis_command_execution_result_result_version"],
            "0.1.0",
        )
        self.assertEqual(boundary["basis_command_execution_result_failed_check_count"], 0)
        self.assertEqual(boundary["selected_command"], "state")
        for key in (
            "selected_command_is_state",
            "selected_state_command_execution_result_recorded",
            "command_execution_result_created",
            "command_execution_result_local_only",
            "command_execution_result_read_only",
            "future_state_payload_return_may_be_considered",
        ):
            self.assertIs(boundary[key], True)
        self.assert_no_payload_lookup_permission_or_follow_on(result)
        self.assert_boundary_not_wrapper(boundary)

    def resolve_with_synthetic(
        self,
        mutation: Callable[[dict[str, Any], Path, dict[str, Any]], None] | None = None,
    ) -> dict[str, Any]:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact_path, artifact = _write_synthetic_artifact(tmp_path)
            request = _build_request(artifact_path)
            if mutation is not None:
                mutation(request, artifact_path, artifact)
            return resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min(
                request
            )

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_request",
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
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min",
        )
        self.assertTrue(Path(resolver.OUTPUT_ROOT).as_posix().endswith(EXPECTED_OUTPUT_ROOT.as_posix()))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY",
            resolver.SUPPORTED_BOUNDARY_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_STATE_PAYLOAD_RETURN_CONSIDERATION_ONLY",
            resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        request = (
            resolver.build_declared_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_request()
        )
        self.assertEqual(
            Path(request["selected_command_execution_result_artifact"]).name,
            DEFAULT_COMMAND_EXECUTION_RESULT_ARTIFACT.name,
        )
        self.assertEqual(request["selected_command"], "state")

        output_root = Path(resolver.OUTPUT_ROOT)
        for root in FORBIDDEN_OUTPUT_ROOTS:
            self.assertNotEqual(output_root, root)
            self.assertFalse(_path_has_component_prefix(output_root, root))

    def test_successful_recorded_result_from_synthetic_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = _write_synthetic_artifact(Path(tmp))
            request = _build_request(artifact_path)
            result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min(
                request
            )
            self.assertIsInstance(result, dict)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(_summary(result)["failed_check_count"], 0)
            self.assertGreater(_summary(result)["passed_check_count"], 0)
            self.assertEqual(_summary(result)["result_version"], "0.1.0")
            self.assertEqual(_summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            for section in EXPECTED_WRAPPER_SECTIONS:
                self.assertIn(section, result)

            self.assert_recorded_boundary(result, artifact_path)
            self.assertEqual(
                _boundary(result)["boundary_id"],
                request["local_relevance_medium_read_only_state_payload_return_boundary_id"],
            )
            for field in EXPECTED_TRUE_STATEMENT_FIELDS:
                self.assertIs(_statement(result)[field], True)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_COMMAND_EXECUTION_RESULT_ARTIFACT.exists():
            self.skipTest("default live command execution result artifact is absent")

        request = (
            resolver.build_declared_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_request()
        )
        result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min(
            request
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(_summary(result)["failed_check_count"], 0)
        self.assert_not_blocked(result)
        boundary = _boundary(result)
        self.assertEqual(boundary["selected_command"], "state")
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY",
        )
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_STATE_PAYLOAD_RETURN_CONSIDERATION_ONLY",
        )
        for key in (
            "selected_state_command_execution_result_recorded",
            "command_execution_result_created",
            "command_execution_result_local_only",
            "command_execution_result_read_only",
            "future_state_payload_return_may_be_considered",
        ):
            self.assertIs(boundary[key], True)
        self.assert_same_or_stable_artifact_path(
            boundary["basis_command_execution_result_artifact"],
            DEFAULT_COMMAND_EXECUTION_RESULT_ARTIFACT,
        )
        self.assert_no_payload_lookup_permission_or_follow_on(result)

    def test_required_false_non_claims_are_canonicalized_when_flipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = _write_synthetic_artifact(Path(tmp))
            clean_request = _build_request(artifact_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_result(result)
                    self.assertIs(result["non_claims"][key], False)

    def test_representative_blocking_behavior(self) -> None:
        intent_key = "local_relevance_medium_read_only_state_payload_return_boundary_intent"

        def mutate_artifact_top_level(
            key: str, value: Any
        ) -> Callable[[dict[str, Any], Path, dict[str, Any]], None]:
            def mutate(
                _request: dict[str, Any],
                artifact_path: Path,
                artifact: dict[str, Any],
            ) -> None:
                artifact[key] = value
                _write_json(artifact_path, artifact)

            return mutate

        cases: list[
            tuple[str, Callable[[dict[str, Any], Path, dict[str, Any]], None]]
        ] = [
            ("explicit block intent", lambda r, *_: _set(r, intent_key, "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY")),
            ("unsupported intent", lambda r, *_: _set(r, intent_key, "UNSUPPORTED_STATE_PAYLOAD_RETURN_BOUNDARY_INTENT")),
            ("command execution result artifact path missing", lambda r, *_: _pop(r, "selected_command_execution_result_artifact")),
            ("command execution result artifact unreadable", lambda r, p, *_: _set(r, "selected_command_execution_result_artifact", str(p.parent / "missing-result.json"))),
            ("command execution result artifact JSON array instead of object", lambda _r, p, *_: _write_json(p, [])),
            ("command execution result artifact not recorded", mutate_artifact_top_level("outcome", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_NOT_RECORDED")),
            ("command execution result artifact failed checks present", mutate_artifact_top_level("failed_check_count", 1)),
            ("command execution result artifact version not 0.1.0", mutate_artifact_top_level("result_version", "0.2.0")),
            ("selected command missing", lambda r, *_: _pop(r, "selected_command")),
            ("selected command not state", lambda r, *_: _set(r, "selected_command", "lookup first_orientation_locator")),
            ("selected-state command execution result not recorded", lambda r, *_: _set(r, "selected_state_command_execution_result_not_recorded", True)),
            ("command execution result not created", lambda r, *_: _set(r, "command_execution_result_not_created", True)),
            ("command execution result local only not true", lambda r, *_: _set(r, "command_execution_result_local_only_not_true", True)),
            ("command execution result read only not true", lambda r, *_: _set(r, "command_execution_result_read_only_not_true", True)),
            ("future state payload return may not be considered", lambda r, *_: _set(r, "future_state_payload_return_may_not_be_considered", True)),
            ("boundary type missing", lambda r, *_: _pop(r, "boundary_type")),
            ("boundary type not supported", lambda r, *_: _set(r, "boundary_type", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN")),
            ("boundary scope missing", lambda r, *_: _pop(r, "boundary_scope")),
            ("boundary scope not supported", lambda r, *_: _set(r, "boundary_scope", "STATE_PAYLOAD_RETURN_ONLY")),
            ("required non-claim missing", lambda r, *_: r["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])),
        ]

        for field in (
            "state_payload_returned",
            "state_result_object_created",
            "state_packet_body_exposed",
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
            "artifact_existence_treated_as_state_payload_return_boundary_authority",
            "latest_file_posture_treated_as_state_payload_return_boundary_authority",
            "repo_local_availability_treated_as_state_payload_return_boundary_authority",
            "hidden_repo_state_used_as_state_payload_return_boundary_content",
            "hidden_repo_state_used_as_state_payload_return_boundary_authority",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            cases.append((f"{field} asserted", lambda r, *_, field=field: _set(r, field, True)))

        cases.append(("predecessor failure evidence hidden/repaired/claimed passed", lambda r, *_: r.update({"predecessor_failure_repaired": True, "predecessor_failure_hidden": True, "predecessor_failure_claimed_passed": True})))
        cases.append(("required non-claim flipped", lambda r, *_: _set(r["declared_non_claims"], resolver.REQUIRED_FALSE_NON_CLAIMS[-1], True)))

        for name, mutation in cases:
            with self.subTest(case=name):
                self.assert_blocked_result(self.resolve_with_synthetic(mutation))

        for name, value in (("missing request", {}), ("non-mapping request", ["not", "a", "mapping"])):
            with self.subTest(case=name):
                result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min(
                    value
                )
                self.assert_blocked_result(result)

    def test_missing_or_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = _write_synthetic_artifact(Path(tmp))
            base_request = _build_request(artifact_path)
            variants: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
                ("remove declared_non_claims", lambda r: _pop(r, "declared_non_claims")),
                ("declared_non_claims empty", lambda r: _set(r, "declared_non_claims", {})),
                ("one required non-claim removed", lambda r: r["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])),
                ("one required non-claim string", lambda r: _set(r["declared_non_claims"], resolver.REQUIRED_FALSE_NON_CLAIMS[0], "false")),
                ("one required non-claim none", lambda r: _set(r["declared_non_claims"], resolver.REQUIRED_FALSE_NON_CLAIMS[0], None)),
            ]
            for name, mutate in variants:
                with self.subTest(case=name):
                    request = copy.deepcopy(base_request)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min(
                        request
                    )
                    self.assertIn(
                        result["outcome"],
                        (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS),
                    )
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        block = result.get("block") or {}
                        self.assertIn(block.get("block_code") or block.get("code"), resolver.BLOCK_CODES)
                    self.assert_all_block_codes_public(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = _write_synthetic_artifact(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min(
                _build_request(artifact_path)
            )
        boundary = _boundary(result)
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY",
        )
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_STATE_PAYLOAD_RETURN_CONSIDERATION_ONLY",
        )
        self.assertEqual(boundary["selected_command"], "state")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn(resolver.OUTCOME_RECORDED, serialized)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY",
            serialized,
        )
        self.assertIn("SELECTED_STATE_PAYLOAD_RETURN_CONSIDERATION_ONLY", serialized)
        self.assertIn('"state"', serialized)
        self.assertNotIn("[REDACTED_RAW_CONTENT]", serialized)

    def test_raw_and_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, artifact = _write_synthetic_artifact(Path(tmp))
            artifact["raw_command_execution_result_body"] = HOSTILE_SENTINELS[5]
            artifact["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            _write_json(artifact_path, artifact)
            request = _build_request(artifact_path)
            request["raw_full_body"] = {"payload": HOSTILE_SENTINELS[0]}
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            request["additional_basis_context"] = HOSTILE_SENTINELS[1]
            original_request = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min(
                request
            )
        self.assertEqual(request, original_request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_BOUNDARY",
            serialized,
        )
        self.assertIn("SELECTED_STATE_PAYLOAD_RETURN_CONSIDERATION_ONLY", serialized)
        self.assertIn('"state"', serialized)
        self.assert_no_payload_lookup_permission_or_follow_on(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact_path, _artifact = _write_synthetic_artifact(tmp_path)
            request = _build_request(artifact_path)
            request_path = tmp_path / "request.json"
            _write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(_summary(result)["result_version"], "0.1.0")
            self.assertEqual(_summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_result(malformed_result)

            array_path = tmp_path / "array.json"
            _write_json(array_path, [])
            self.assert_blocked_result(
                resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_from_path(
                    array_path
                )
            )
            self.assert_blocked_result(
                resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_from_path(
                    tmp_path / "missing.json"
                )
            )

            output_root = tmp_path / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_state_payload_return_boundary_v0_min_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIsInstance(json.loads(first_path.read_text(encoding="utf-8")), dict)
            self.assertIn(
                "local_relevance_medium_read_only_state_payload_return_boundary_v0_min",
                first_path.as_posix(),
            )
            for root in FORBIDDEN_OUTPUT_ROOTS:
                self.assertFalse(_path_has_component_prefix(first_path, root))
                self.assertFalse(_path_has_component_prefix(second_path, root))

    def test_resolver_does_not_mutate_inputs_or_synthetic_basis_material(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, artifact = _write_synthetic_artifact(Path(tmp))
            request = _build_request(artifact_path)
            request["raw_full_body"] = {"nested": HOSTILE_SENTINELS[2]}
            request["posture_mappings"] = {
                "state_payload_returned": False,
                "lookup_performed": False,
            }
            original_request = copy.deepcopy(request)
            original_non_claims = copy.deepcopy(request["declared_non_claims"])
            original_artifact_path = request["selected_command_execution_result_artifact"]
            original_selected_command = request["selected_command"]
            original_boundary_type = request["boundary_type"]
            original_boundary_scope = request["boundary_scope"]
            original_artifact = copy.deepcopy(artifact)

            result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min(
                request
            )

            self.assertEqual(request, original_request)
            self.assertEqual(request["declared_non_claims"], original_non_claims)
            self.assertEqual(request["selected_command_execution_result_artifact"], original_artifact_path)
            self.assertEqual(request["selected_command"], original_selected_command)
            self.assertEqual(request["boundary_type"], original_boundary_type)
            self.assertEqual(request["boundary_scope"], original_boundary_scope)
            self.assertEqual(artifact, original_artifact)
            self.assertEqual(request["posture_mappings"], original_request["posture_mappings"])
            self.assertEqual(request["raw_full_body"], original_request["raw_full_body"])
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)

    def test_predecessor_failure_and_token_reuse_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = _write_synthetic_artifact(Path(tmp))
            clean_request = _build_request(artifact_path)
            clean_result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min(
                clean_request
            )
            non_claims = clean_result["non_claims"]
            self.assertIs(non_claims["predecessor_failure_repaired"], False)
            self.assertIs(non_claims["predecessor_failure_hidden"], False)
            self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
            self.assertIs(non_claims["consumed_request_reopened"], False)
            self.assertIs(non_claims["authorization_token_reused"], False)
            self.assertIs(_summary(clean_result)["predecessor_failure_evidence_preserved"], True)

            for field in (
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
                "consumed_request_reopened",
                "authorization_token_reused",
            ):
                with self.subTest(field=field):
                    request = copy.deepcopy(clean_request)
                    request[field] = True
                    result = resolver.resolve_local_relevance_medium_read_only_state_payload_return_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_result(result)


if __name__ == "__main__":
    unittest.main()
