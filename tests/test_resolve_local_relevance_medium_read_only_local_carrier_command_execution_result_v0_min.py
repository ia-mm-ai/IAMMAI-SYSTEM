"""Tests for the selected-state local carrier command execution result resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT object.
It verifies that the resolver reads one clean command execution result boundary
artifact and one clean selected-state command execution artifact, records one
local read-only selected-state command execution result object, and keeps state
payload return, state result object creation, state packet body exposure,
lookup, permissions, public/distributed surfaces, registry/search/query/ranking,
filesystem discovery, source transfer, participation, and follow-on work out of
the result object and result-level posture.
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

import resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min as resolver  # noqa: E402


DEFAULT_COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_execution_result_boundary_v0_min/"
    "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_"
    "reference_review_001__local_relevance_medium_read_only_local_carrier_"
    "command_execution_result_boundary_v0_min_result.json"
)
DEFAULT_COMMAND_EXECUTION_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_execution_v0_min/"
    "local_relevance_medium_read_only_local_carrier_command_execution_reference_review_001__"
    "local_relevance_medium_read_only_local_carrier_command_execution_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_execution_result_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    "local_relevance_medium_read_only_local_carrier_command_execution_result_metadata",
    "declared_local_relevance_medium_read_only_local_carrier_command_execution_result_question",
    "selected_command_execution_result_boundary_artifact_basis",
    "selected_command_execution_artifact_basis",
    "local_relevance_medium_read_only_local_carrier_command_execution_result",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_checks",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_statement",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_summary",
)

FORBIDDEN_RESULT_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_checks",
    "non_claims",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_summary",
    "local_relevance_medium_read_only_local_carrier_command_execution_result_metadata",
)

RESULT_OBJECT_FALSE_FIELDS = (
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
    "local_relevance_medium_read_only_local_carrier_command_execution_result_recorded",
    "basis_command_execution_result_boundary_artifact_preserved",
    "basis_command_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_command_execution_recorded",
    "command_execution_performed",
    "command_execution_local_only",
    "command_execution_read_only",
    "command_execution_result_created",
    "command_execution_result_local_only",
    "command_execution_result_read_only",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
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


def _set(mapping: dict[str, Any], key: str, value: Any) -> None:
    mapping[key] = value


def _pop(mapping: dict[str, Any], key: str) -> None:
    mapping.pop(key, None)


def _result_boundary_object(**overrides: Any) -> dict[str, Any]:
    boundary = {
        "boundary_id": "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_001",
        "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY",
        "boundary_version": "0.1.0",
        "boundary_scope": "SELECTED_STATE_COMMAND_EXECUTION_RESULT_CONSIDERATION_ONLY",
        "basis_command_execution_artifact": str(DEFAULT_COMMAND_EXECUTION_ARTIFACT),
        "basis_command_execution_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RECORDED",
        "basis_command_execution_result_version": "0.1.0",
        "basis_command_execution_failed_check_count": 0,
        "selected_command": "state",
        "selected_command_is_state": True,
        "selected_command_execution_recorded": True,
        "command_execution_performed": True,
        "command_execution_local_only": True,
        "command_execution_read_only": True,
        "future_command_execution_result_may_be_considered": True,
        "command_execution_result_created": False,
    }
    for field in RESULT_OBJECT_FALSE_FIELDS:
        boundary[field] = False
    boundary.update(overrides)
    return boundary


def _command_execution_object(**overrides: Any) -> dict[str, Any]:
    execution = {
        "command_execution_id": "local_relevance_medium_read_only_local_carrier_command_execution_001",
        "command_execution_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION",
        "command_execution_version": "0.1.0",
        "command_execution_scope": "SINGLE_LOCAL_READ_ONLY_STATE_COMMAND_EXECUTION_ONLY",
        "selected_command": "state",
        "selected_command_is_state": True,
        "selected_command_is_from_closed_command_set": True,
        "single_command_selected": True,
        "local_carrier_command_execution_recorded": True,
        "command_execution_performed": True,
        "command_execution_local_only": True,
        "command_execution_read_only": True,
        "command_execution_result_created": False,
    }
    for field in RESULT_OBJECT_FALSE_FIELDS:
        execution[field] = False
    execution.update(overrides)
    return execution


def _command_execution_result_boundary_artifact(**object_overrides: Any) -> dict[str, Any]:
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED",
        "result_version": "0.1.0",
        "failed_check_count": 0,
        "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_metadata": {
            "result_version": "0.1.0",
            "failed_check_count": 0,
        },
        "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
        },
        "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_checks": [
            {"check_name": "synthetic clean boundary", "passed": True}
        ],
        "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary": _result_boundary_object(
            **object_overrides
        ),
    }


def _command_execution_artifact(**object_overrides: Any) -> dict[str, Any]:
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RECORDED",
        "result_version": "0.1.0",
        "failed_check_count": 0,
        "local_relevance_medium_read_only_local_carrier_command_execution_metadata": {
            "result_version": "0.1.0",
            "failed_check_count": 0,
        },
        "local_relevance_medium_read_only_local_carrier_command_execution_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
        },
        "local_relevance_medium_read_only_local_carrier_command_execution_checks": [
            {"check_name": "synthetic clean execution", "passed": True}
        ],
        "local_relevance_medium_read_only_local_carrier_command_execution": _command_execution_object(
            **object_overrides
        ),
    }


def _write_synthetic_artifacts(
    directory: Path,
    *,
    boundary_object_overrides: Mapping[str, Any] | None = None,
    execution_object_overrides: Mapping[str, Any] | None = None,
    boundary_artifact_overrides: Mapping[str, Any] | None = None,
    execution_artifact_overrides: Mapping[str, Any] | None = None,
) -> tuple[Path, Path, dict[str, Any], dict[str, Any]]:
    boundary_path = directory / "synthetic_command_execution_result_boundary.json"
    execution_path = directory / "synthetic_command_execution.json"
    boundary = _command_execution_result_boundary_artifact(
        **dict(boundary_object_overrides or {})
    )
    execution = _command_execution_artifact(**dict(execution_object_overrides or {}))
    if boundary_artifact_overrides:
        boundary.update(dict(boundary_artifact_overrides))
    if execution_artifact_overrides:
        execution.update(dict(execution_artifact_overrides))
    boundary[
        "local_relevance_medium_read_only_local_carrier_command_execution_result_boundary"
    ]["basis_command_execution_artifact"] = str(execution_path)
    _write_json(boundary_path, boundary)
    _write_json(execution_path, execution)
    return boundary_path, execution_path, boundary, execution


def _build_request(boundary_path: Path, execution_path: Path, **overrides: Any) -> dict[str, Any]:
    request = (
        resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_request(
            selected_command_execution_result_boundary_artifact=str(boundary_path),
            selected_command_execution_artifact=str(execution_path),
        )
    )
    request.update(overrides)
    return request


def _execution_result(result: Mapping[str, Any]) -> dict[str, Any]:
    value = result.get("local_relevance_medium_read_only_local_carrier_command_execution_result")
    return dict(value) if isinstance(value, Mapping) else {}


def _statement(result: Mapping[str, Any]) -> dict[str, Any]:
    value = result.get("local_relevance_medium_read_only_local_carrier_command_execution_result_statement")
    return dict(value) if isinstance(value, Mapping) else {}


def _checks(result: Mapping[str, Any]) -> list[dict[str, Any]]:
    value = result.get("local_relevance_medium_read_only_local_carrier_command_execution_result_checks")
    if not isinstance(value, list):
        return []
    return [dict(item) for item in value if isinstance(item, Mapping)]


def _summary(result: Mapping[str, Any]) -> dict[str, Any]:
    value = result.get("local_relevance_medium_read_only_local_carrier_command_execution_result_summary")
    return dict(value) if isinstance(value, Mapping) else {}


class LocalCarrierCommandExecutionResultResolverTests(unittest.TestCase):
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

    def assert_result_object_not_wrapper(self, result_object: Mapping[str, Any]) -> None:
        for key in FORBIDDEN_RESULT_WRAPPER_FIELDS:
            self.assertNotIn(key, result_object)

    def assert_no_payload_lookup_permission_or_follow_on(
        self, result: Mapping[str, Any]
    ) -> None:
        result_object = _execution_result(result)
        for field in RESULT_OBJECT_FALSE_FIELDS:
            self.assertIn(field, result_object)
            self.assertIs(result_object[field], False)
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

    def assert_recorded_result_object(
        self, result: Mapping[str, Any], boundary_path: Path, execution_path: Path
    ) -> None:
        result_object = _execution_result(result)
        self.assertEqual(
            result_object["command_execution_result_id"],
            "local_relevance_medium_read_only_local_carrier_command_execution_result_001",
        )
        self.assertEqual(
            result_object["command_execution_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT",
        )
        self.assertEqual(result_object["command_execution_result_version"], "0.1.0")
        self.assertEqual(
            result_object["command_execution_result_scope"],
            "SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            result_object["basis_command_execution_result_boundary_artifact"],
            boundary_path,
        )
        self.assertEqual(
            result_object["basis_command_execution_result_boundary_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            result_object["basis_command_execution_result_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            result_object["basis_command_execution_result_boundary_failed_check_count"],
            0,
        )
        self.assert_same_or_stable_artifact_path(
            result_object["basis_command_execution_artifact"], execution_path
        )
        self.assertEqual(
            result_object["basis_command_execution_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RECORDED",
        )
        self.assertEqual(result_object["basis_command_execution_result_version"], "0.1.0")
        self.assertEqual(result_object["basis_command_execution_failed_check_count"], 0)
        for key in (
            "selected_command_is_state",
            "selected_command_execution_recorded",
            "command_execution_performed",
            "command_execution_local_only",
            "command_execution_read_only",
            "local_carrier_command_execution_result_recorded",
            "command_execution_result_created",
            "command_execution_result_local_only",
            "command_execution_result_read_only",
        ):
            self.assertIs(result_object[key], True)
        self.assertEqual(result_object["selected_command"], "state")
        self.assert_no_payload_lookup_permission_or_follow_on(result)
        self.assert_result_object_not_wrapper(result_object)

    def resolve_with_synthetic(
        self,
        mutation: Callable[[dict[str, Any], Path, Path, dict[str, Any], dict[str, Any]], None]
        | None = None,
    ) -> dict[str, Any]:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary_path, execution_path, boundary, execution = _write_synthetic_artifacts(
                tmp_path
            )
            request = _build_request(boundary_path, execution_path)
            if mutation is not None:
                mutation(request, boundary_path, execution_path, boundary, execution)
            return resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
                request
            )

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min",
            "resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_from_path",
            "write_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_result",
            "build_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_COMMAND_EXECUTION_RESULT_TYPE_VALUES",
            "SUPPORTED_COMMAND_EXECUTION_RESULT_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min",
        )
        self.assertTrue(Path(resolver.OUTPUT_ROOT).as_posix().endswith(EXPECTED_OUTPUT_ROOT.as_posix()))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT",
            resolver.SUPPORTED_COMMAND_EXECUTION_RESULT_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY",
            resolver.SUPPORTED_COMMAND_EXECUTION_RESULT_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        request = (
            resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_request()
        )
        self.assertEqual(Path(request["selected_command_execution_result_boundary_artifact"]).name, DEFAULT_COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT.name)
        self.assertEqual(Path(request["selected_command_execution_artifact"]).name, DEFAULT_COMMAND_EXECUTION_ARTIFACT.name)
        self.assertEqual(request["selected_command"], "state")

        output_root = Path(resolver.OUTPUT_ROOT)
        for root in FORBIDDEN_OUTPUT_ROOTS:
            self.assertNotEqual(output_root, root)
            self.assertFalse(_path_has_component_prefix(output_root, root))

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, execution_path, _boundary, _execution = _write_synthetic_artifacts(
                Path(tmp)
            )
            request = _build_request(boundary_path, execution_path)
            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
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

            self.assert_recorded_result_object(result, boundary_path, execution_path)
            self.assertEqual(
                _execution_result(result)["command_execution_result_id"],
                request["local_relevance_medium_read_only_local_carrier_command_execution_result_id"],
            )
            for field in EXPECTED_TRUE_STATEMENT_FIELDS:
                self.assertIs(_statement(result)[field], True)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not (
            DEFAULT_COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT.exists()
            and DEFAULT_COMMAND_EXECUTION_ARTIFACT.exists()
        ):
            self.skipTest("default live command execution result basis artifacts are absent")

        request = (
            resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_request()
        )
        result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
            request
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(_summary(result)["failed_check_count"], 0)
        self.assert_not_blocked(result)
        result_object = _execution_result(result)
        self.assertEqual(result_object["selected_command"], "state")
        self.assertEqual(
            result_object["command_execution_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT",
        )
        self.assertEqual(
            result_object["command_execution_result_scope"],
            "SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY",
        )
        self.assertIs(result_object["selected_command_execution_recorded"], True)
        self.assertIs(result_object["command_execution_performed"], True)
        self.assertIs(result_object["command_execution_local_only"], True)
        self.assertIs(result_object["command_execution_read_only"], True)
        self.assertIs(result_object["local_carrier_command_execution_result_recorded"], True)
        self.assertIs(result_object["command_execution_result_created"], True)
        self.assertIs(result_object["command_execution_result_local_only"], True)
        self.assertIs(result_object["command_execution_result_read_only"], True)
        self.assert_same_or_stable_artifact_path(
            result_object["basis_command_execution_result_boundary_artifact"],
            DEFAULT_COMMAND_EXECUTION_RESULT_BOUNDARY_ARTIFACT,
        )
        self.assert_same_or_stable_artifact_path(
            result_object["basis_command_execution_artifact"],
            DEFAULT_COMMAND_EXECUTION_ARTIFACT,
        )
        self.assert_no_payload_lookup_permission_or_follow_on(result)

    def test_required_false_non_claims_are_canonicalized_when_flipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, execution_path, _boundary, _execution = _write_synthetic_artifacts(
                Path(tmp)
            )
            clean_request = _build_request(boundary_path, execution_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
                        request
                    )
                    self.assert_blocked_result(result)
                    self.assertIs(result["non_claims"][key], False)

    def test_representative_blocking_behavior(self) -> None:
        intent_key = "local_relevance_medium_read_only_local_carrier_command_execution_result_intent"

        def mutate_boundary_artifact(
            key: str, value: Any
        ) -> Callable[[dict[str, Any], Path, Path, dict[str, Any], dict[str, Any]], None]:
            def mutate(
                _request: dict[str, Any],
                boundary_path: Path,
                _execution_path: Path,
                boundary: dict[str, Any],
                _execution: dict[str, Any],
            ) -> None:
                boundary[key] = value
                _write_json(boundary_path, boundary)

            return mutate

        def mutate_execution_artifact(
            key: str, value: Any
        ) -> Callable[[dict[str, Any], Path, Path, dict[str, Any], dict[str, Any]], None]:
            def mutate(
                _request: dict[str, Any],
                _boundary_path: Path,
                execution_path: Path,
                _boundary: dict[str, Any],
                execution: dict[str, Any],
            ) -> None:
                execution[key] = value
                _write_json(execution_path, execution)

            return mutate

        cases: list[
            tuple[
                str,
                Callable[[dict[str, Any], Path, Path, dict[str, Any], dict[str, Any]], None],
            ]
        ] = [
            ("explicit block intent", lambda r, *_: _set(r, intent_key, "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT")),
            ("unsupported intent", lambda r, *_: _set(r, intent_key, "UNSUPPORTED_COMMAND_EXECUTION_RESULT_INTENT")),
            ("command execution result boundary artifact path missing", lambda r, *_: _pop(r, "selected_command_execution_result_boundary_artifact")),
            ("command execution result boundary artifact unreadable", lambda r, b, *_: _set(r, "selected_command_execution_result_boundary_artifact", str(b.parent / "missing-boundary.json"))),
            ("command execution result boundary artifact JSON array instead of object", lambda _r, b, *_: _write_json(b, [])),
            ("command execution result boundary artifact not recorded", mutate_boundary_artifact("outcome", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BOUNDARY_NOT_RECORDED")),
            ("command execution result boundary artifact failed checks present", mutate_boundary_artifact("failed_check_count", 1)),
            ("command execution result boundary artifact version not 0.1.0", mutate_boundary_artifact("result_version", "0.2.0")),
            ("command execution artifact path missing", lambda r, *_: _pop(r, "selected_command_execution_artifact")),
            ("command execution artifact unreadable", lambda r, _b, e, *_: _set(r, "selected_command_execution_artifact", str(e.parent / "missing-execution.json"))),
            ("command execution artifact JSON array instead of object", lambda _r, _b, e, *_: _write_json(e, [])),
            ("command execution artifact not recorded", mutate_execution_artifact("outcome", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_NOT_RECORDED")),
            ("command execution artifact failed checks present", mutate_execution_artifact("failed_check_count", 1)),
            ("command execution artifact version not 0.1.0", mutate_execution_artifact("result_version", "0.2.0")),
            ("selected command missing", lambda r, *_: _pop(r, "selected_command")),
            ("selected command not state", lambda r, *_: _set(r, "selected_command", "lookup first_orientation_locator")),
            ("command execution result type missing", lambda r, *_: _pop(r, "command_execution_result_type")),
            ("command execution result type not supported", lambda r, *_: _set(r, "command_execution_result_type", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN")),
            ("command execution result scope missing", lambda r, *_: _pop(r, "command_execution_result_scope")),
            ("command execution result scope not supported", lambda r, *_: _set(r, "command_execution_result_scope", "STATE_PAYLOAD_RETURN_ONLY")),
            ("required non-claim missing", lambda r, *_: r["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])),
        ]

        for field in (
            "selected_command_execution_recorded",
            "command_execution_performed",
            "command_execution_local_only",
            "command_execution_read_only",
            "local_carrier_command_execution_result_recorded",
            "command_execution_result_created",
            "command_execution_result_local_only",
            "command_execution_result_read_only",
        ):
            cases.append((f"{field} not true", lambda r, *_, field=field: _set(r, field, False)))

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
            "artifact_existence_treated_as_command_execution_result_authority",
            "latest_file_posture_treated_as_command_execution_result_authority",
            "repo_local_availability_treated_as_command_execution_result_authority",
            "hidden_repo_state_used_as_command_execution_result_content",
            "hidden_repo_state_used_as_command_execution_result_authority",
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
                result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
                    value
                )
                self.assert_blocked_result(result)

    def test_missing_or_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, execution_path, _boundary, _execution = _write_synthetic_artifacts(
                Path(tmp)
            )
            base_request = _build_request(boundary_path, execution_path)
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
                    result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
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
            boundary_path, execution_path, _boundary, _execution = _write_synthetic_artifacts(
                Path(tmp)
            )
            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
                _build_request(boundary_path, execution_path)
            )
        result_object = _execution_result(result)
        self.assertEqual(
            result_object["command_execution_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT",
        )
        self.assertEqual(
            result_object["command_execution_result_scope"],
            "SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY",
        )
        self.assertEqual(result_object["selected_command"], "state")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn(resolver.OUTCOME_RECORDED, serialized)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT",
            serialized,
        )
        self.assertIn("SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY", serialized)
        self.assertIn('"state"', serialized)
        self.assertNotIn("[REDACTED_RAW_CONTENT]", serialized)

    def test_raw_and_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, execution_path, boundary, execution = _write_synthetic_artifacts(
                Path(tmp)
            )
            boundary["raw_command_execution_result_boundary_body"] = HOSTILE_SENTINELS[7]
            execution["raw_command_execution_body"] = HOSTILE_SENTINELS[8]
            _write_json(boundary_path, boundary)
            _write_json(execution_path, execution)
            request = _build_request(boundary_path, execution_path)
            request["raw_full_body"] = {"payload": HOSTILE_SENTINELS[0]}
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            request["additional_basis_context"] = HOSTILE_SENTINELS[1]
            original_request = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
                request
            )
        self.assertEqual(request, original_request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_EXECUTION_RESULT",
            serialized,
        )
        self.assertIn("SELECTED_STATE_COMMAND_EXECUTION_RESULT_ONLY", serialized)
        self.assertIn('"state"', serialized)
        self.assert_no_payload_lookup_permission_or_follow_on(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary_path, execution_path, _boundary, _execution = _write_synthetic_artifacts(
                tmp_path
            )
            request = _build_request(boundary_path, execution_path)
            request_path = tmp_path / "request.json"
            _write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(_summary(result)["result_version"], "0.1.0")
            self.assertEqual(_summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_result(malformed_result)

            array_path = tmp_path / "array.json"
            _write_json(array_path, [])
            self.assert_blocked_result(
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_from_path(
                    array_path
                )
            )
            self.assert_blocked_result(
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_from_path(
                    tmp_path / "missing.json"
                )
            )

            output_root = tmp_path / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIsInstance(json.loads(first_path.read_text(encoding="utf-8")), dict)
            self.assertIn(
                "local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min",
                first_path.as_posix(),
            )
            for root in FORBIDDEN_OUTPUT_ROOTS:
                self.assertFalse(_path_has_component_prefix(first_path, root))
                self.assertFalse(_path_has_component_prefix(second_path, root))

    def test_resolver_does_not_mutate_inputs_or_synthetic_basis_material(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, execution_path, boundary, execution = _write_synthetic_artifacts(
                Path(tmp)
            )
            request = _build_request(boundary_path, execution_path)
            request["raw_full_body"] = {"nested": HOSTILE_SENTINELS[2]}
            request["posture_mappings"] = {
                "state_payload_returned": False,
                "lookup_performed": False,
            }
            original_request = copy.deepcopy(request)
            original_non_claims = copy.deepcopy(request["declared_non_claims"])
            original_boundary_path = request["selected_command_execution_result_boundary_artifact"]
            original_execution_path = request["selected_command_execution_artifact"]
            original_selected_command = request["selected_command"]
            original_result_type = request["command_execution_result_type"]
            original_result_scope = request["command_execution_result_scope"]
            original_boundary = copy.deepcopy(boundary)
            original_execution = copy.deepcopy(execution)

            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
                request
            )

            self.assertEqual(request, original_request)
            self.assertEqual(request["declared_non_claims"], original_non_claims)
            self.assertEqual(request["selected_command_execution_result_boundary_artifact"], original_boundary_path)
            self.assertEqual(request["selected_command_execution_artifact"], original_execution_path)
            self.assertEqual(request["selected_command"], original_selected_command)
            self.assertEqual(request["command_execution_result_type"], original_result_type)
            self.assertEqual(request["command_execution_result_scope"], original_result_scope)
            self.assertEqual(boundary, original_boundary)
            self.assertEqual(execution, original_execution)
            self.assertEqual(request["posture_mappings"], original_request["posture_mappings"])
            self.assertEqual(request["raw_full_body"], original_request["raw_full_body"])
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)

    def test_predecessor_failure_and_token_reuse_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, execution_path, _boundary, _execution = _write_synthetic_artifacts(
                Path(tmp)
            )
            clean_request = _build_request(boundary_path, execution_path)
            clean_result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
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
                    result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min(
                        request
                    )
                    self.assert_blocked_result(result)


if __name__ == "__main__":
    unittest.main()
