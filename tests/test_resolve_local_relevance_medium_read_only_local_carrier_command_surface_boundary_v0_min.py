"""Tests for the local relevance medium read-only local carrier command surface boundary.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY object.
It verifies that the resolver reads one clean reusable lookup permission
artifact and one clean read-only state reader / state packet artifact using the
standing state packet path, then records one boundary allowing a future local
read-only carrier command surface to be considered only for state,
lookup first_orientation_locator, and lookup second_orientation_locator.

The suite does not create local carrier command surface behavior, command
execution behavior, command execution result behavior, operation permission,
runtime permission, API behavior, distributed behavior, general lookup
permission, arbitrary lookup permission, unsupported-command permission,
unsupported-key permission, new lookup result, new lookup entry, registry,
search, query surface, ranking, scoring, priority, validity judgment, truth
judgment, authority judgment, currentness judgment, repeated reception
permission, arbitrary reception, feed, new signal, new entry, new relevance
object, new index entry, filesystem discovery, source transfer, source receipt,
action, synchronization, participation, or follow-on work.
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

import resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min as resolver  # noqa: E402


DEFAULT_REUSABLE_LOOKUP_PERMISSION_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_reusable_lookup_permission_v0_min/"
    "local_relevance_medium_read_only_reusable_lookup_permission_reference_review_001__"
    "local_relevance_medium_read_only_reusable_lookup_permission_v0_min_result.json"
)
DEFAULT_READ_ONLY_STATE_READER_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min/"
    "local_relevance_medium_read_only_state_packet_reference_review_001__"
    "local_relevance_medium_read_only_state_reader_v0_min_result.json"
)
NON_STANDING_STATE_READER_FILENAME = (
    "local_relevance_medium_read_only_state_reader_reference_review_001__"
    "local_relevance_medium_read_only_state_reader_v0_min_result.json"
)
STANDING_STATE_PACKET_FILENAME = (
    "local_relevance_medium_read_only_state_packet_reference_review_001__"
    "local_relevance_medium_read_only_state_reader_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_surface_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata",
    "declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary_question",
    "selected_reusable_lookup_permission_artifact_basis",
    "selected_read_only_state_reader_artifact_basis",
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary",
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_checks",
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_statement",
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_summary",
)

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_summary",
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata",
)

BOUNDARY_OBJECT_FALSE_FIELDS = (
    "local_carrier_command_surface_created",
    "command_execution_performed",
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
    "action_created",
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "follow_on_work_authorized",
)

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_recorded",
    "basis_reusable_lookup_permission_artifact_preserved",
    "basis_read_only_state_reader_artifact_preserved",
    "basis_state_packet_object_preserved",
    "basis_state_reader_type_preserved",
    "basis_state_reader_scope_preserved",
    "allowed_commands_preserved",
    "allowed_command_count_is_three",
    "state_command_may_be_considered",
    "lookup_first_orientation_locator_command_may_be_considered",
    "lookup_second_orientation_locator_command_may_be_considered",
    "future_local_read_only_carrier_command_surface_may_be_considered",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_SURFACE_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_REUSABLE_LOOKUP_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_READ_ONLY_STATE_READER_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _path_is_under(candidate: Path, root: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def _reusable_lookup_permission_artifact(
    *,
    outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_RECORDED",
    result_version: str = "0.1.0",
    failed_check_count: int = 0,
    permission_overrides: Mapping[str, Any] | None = None,
    extra_fields: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    permission = {
        "permission_id": "local_relevance_medium_read_only_reusable_lookup_permission_001",
        "permission_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION",
        "permission_version": "0.1.0",
        "permission_scope": "REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY",
        "supported_lookup_keys": ["first_orientation_locator", "second_orientation_locator"],
        "covered_lookup_keys": ["first_orientation_locator", "second_orientation_locator"],
        "permitted_lookup_keys": ["first_orientation_locator", "second_orientation_locator"],
        "reusable_read_only_lookup_permission_created": True,
        "reusable_read_only_lookup_permission_scope_bounded": True,
        "repeated_read_only_deterministic_lookup_permitted": True,
        "general_lookup_permission_created": False,
        "arbitrary_lookup_permission_created": False,
        "unsupported_lookup_keys_permitted": False,
    }
    if permission_overrides:
        permission.update(permission_overrides)
    artifact = {
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "local_relevance_medium_read_only_reusable_lookup_permission_metadata": {
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "resolver_module": "resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min",
        },
        "local_relevance_medium_read_only_reusable_lookup_permission": permission,
        "local_relevance_medium_read_only_reusable_lookup_permission_checks": [
            {
                "check_name": "synthetic reusable lookup permission clean",
                "passed": failed_check_count == 0,
                "expected_posture": "clean reusable lookup permission artifact",
                "actual_posture": "clean reusable lookup permission artifact",
            }
        ],
        "local_relevance_medium_read_only_reusable_lookup_permission_summary": {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "passed_check_count": 216,
        },
    }
    if extra_fields:
        artifact.update(extra_fields)
    return artifact


def _read_only_state_reader_artifact(
    *,
    outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED",
    result_version: str = "0.1.0",
    failed_check_count: int = 0,
    include_packet: bool = True,
    packet_overrides: Mapping[str, Any] | None = None,
    extra_fields: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    packet = {
        "state_packet_id": "local_relevance_medium_read_only_state_packet_001",
        "state_packet_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
        "state_packet_version": "0.1.0",
        "state_reader_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
        "state_reader_version": "0.1.0",
        "state_reader_scope": "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
    }
    if packet_overrides:
        packet.update(packet_overrides)
    artifact = {
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "local_relevance_medium_read_only_state_reader_metadata": {
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "resolver_module": "resolve_local_relevance_medium_read_only_state_reader_v0_min",
        },
        "local_relevance_medium_read_only_state_reader_checks": [
            {
                "check_name": "synthetic read-only state reader clean",
                "passed": failed_check_count == 0,
                "expected_posture": "clean read-only state reader artifact",
                "actual_posture": "clean read-only state reader artifact",
            }
        ],
        "local_relevance_medium_read_only_state_reader_summary": {
            "outcome": outcome,
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            "passed_check_count": 220,
        },
    }
    if include_packet:
        artifact["local_relevance_medium_read_only_state_packet"] = packet
    if extra_fields:
        artifact.update(extra_fields)
    return artifact


class LocalCarrierCommandSurfaceBoundaryResolverTests(unittest.TestCase):
    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def _clean_request(
        self,
        tmp_path: Path,
        *,
        reusable_artifact: Mapping[str, Any] | None = None,
        state_reader_artifact: Mapping[str, Any] | None = None,
    ) -> tuple[dict[str, Any], Path, Path, dict[str, Any], dict[str, Any]]:
        reusable = dict(copy.deepcopy(reusable_artifact or _reusable_lookup_permission_artifact()))
        state_reader = dict(copy.deepcopy(state_reader_artifact or _read_only_state_reader_artifact()))
        reusable_path = tmp_path / "synthetic_reusable_lookup_permission.json"
        state_reader_path = tmp_path / "synthetic_state_packet_reader.json"
        _write_json(reusable_path, reusable)
        _write_json(state_reader_path, state_reader)
        request = (
            resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_request(
                selected_reusable_lookup_permission_artifact=reusable_path,
                selected_read_only_state_reader_artifact=state_reader_path,
            )
        )
        return request, reusable_path, state_reader_path, reusable, state_reader

    def _resolve_clean(self, tmp_path: Path) -> dict[str, Any]:
        request, _, _, _, _ = self._clean_request(tmp_path)
        return resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
            request
        )

    def _boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        boundary = result.get(
            "local_relevance_medium_read_only_local_carrier_command_surface_boundary"
        )
        self.assertIsInstance(boundary, dict)
        return boundary

    def _statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get(
            "local_relevance_medium_read_only_local_carrier_command_surface_boundary_statement"
        )
        self.assertIsInstance(statement, dict)
        return statement

    def _checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get(
            "local_relevance_medium_read_only_local_carrier_command_surface_boundary_checks"
        )
        self.assertIsInstance(checks, list)
        return [check for check in checks if isinstance(check, Mapping)]

    def _block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        code = block.get("block_code") or block.get("code")
        return code if isinstance(code, str) else None

    def assert_all_public_codes(self, result: Mapping[str, Any]) -> None:
        block_code = self._block_code(result)
        if block_code is not None:
            self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in self._checks(result):
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
            self.assertIsInstance(non_claims[key], bool)

    def assert_no_forbidden_result_posture(self, result: Mapping[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        non_claims = result["non_claims"]
        for key in (
            "local_carrier_command_surface_created",
            "command_execution_performed",
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
            "action_created",
            "synchronization_created",
            "participation_authorized",
            "participant_role_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(non_claims[key], False)

    def assert_boundary_not_wrapper(self, boundary: Mapping[str, Any]) -> None:
        for key in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(key, boundary)

    def assert_allowed_command_set(self, boundary: Mapping[str, Any]) -> None:
        self.assertEqual(
            boundary.get("allowed_commands"),
            ["state", "lookup first_orientation_locator", "lookup second_orientation_locator"],
        )
        self.assertEqual(boundary.get("allowed_command_count"), 3)

    def assert_default_state_reader_path_uses_state_packet_filename(
        self,
        request: Mapping[str, Any],
    ) -> None:
        path = request.get("selected_read_only_state_reader_artifact")
        self.assertIsInstance(path, str)
        self.assertTrue(path.endswith(STANDING_STATE_PACKET_FILENAME))
        self.assertNotIn(NON_STANDING_STATE_READER_FILENAME, path)

    def assert_blocked_common(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertIsNotNone(self._block_code(result))
        self.assertIn(self._block_code(result), resolver.BLOCK_CODES)
        self.assertGreater(
            sum(1 for check in self._checks(result) if check.get("passed") is not True),
            0,
        )
        self.assert_all_public_codes(result)
        self.assert_no_forbidden_result_posture(result)

    def test_public_api_constants_and_default_builder_paths(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_request",
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
            "ALLOWED_COMMANDS",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min",
        )
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY",
            resolver.SUPPORTED_BOUNDARY_TYPE_VALUES,
        )
        self.assertIn(
            "LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY",
            resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES,
        )
        self.assertEqual(
            list(resolver.ALLOWED_COMMANDS),
            ["state", "lookup first_orientation_locator", "lookup second_orientation_locator"],
        )

        request = (
            resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_request()
        )
        reusable_path = request["selected_reusable_lookup_permission_artifact"]
        self.assertTrue(
            reusable_path.endswith(
                "local_relevance_medium_read_only_reusable_lookup_permission_reference_review_001__"
                "local_relevance_medium_read_only_reusable_lookup_permission_v0_min_result.json"
            )
        )
        self.assert_default_state_reader_path_uses_state_packet_filename(request)

        root = Path(resolver.OUTPUT_ROOT)
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            self.assertNotEqual(root, forbidden)
            self.assertFalse(_path_is_under(root, forbidden), f"{root} is under {forbidden}")

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request, reusable_path, state_reader_path, _, _ = self._clean_request(tmp_path)
            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
                request
            )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        metadata = result["local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata"]
        self.assertEqual(metadata["failed_check_count"], 0)
        self.assertEqual(metadata["result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(metadata["passed_check_count"], 0)

        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        boundary = self._boundary(result)
        self.assertEqual(
            boundary["boundary_id"],
            "local_relevance_medium_read_only_local_carrier_command_surface_boundary_001",
        )
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY",
        )
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(
            boundary["boundary_scope"],
            "LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY",
        )
        self.assertEqual(boundary["basis_reusable_lookup_permission_artifact"], str(reusable_path))
        self.assertEqual(
            boundary["basis_reusable_lookup_permission_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_RECORDED",
        )
        self.assertEqual(boundary["basis_reusable_lookup_permission_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_reusable_lookup_permission_failed_check_count"], 0)
        self.assertEqual(boundary["basis_read_only_state_reader_artifact"], str(state_reader_path))
        self.assertEqual(
            boundary["basis_read_only_state_reader_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED",
        )
        self.assertEqual(boundary["basis_read_only_state_reader_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_read_only_state_reader_failed_check_count"], 0)
        self.assertEqual(
            boundary["basis_state_packet_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
        )
        self.assertEqual(
            boundary["basis_state_reader_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
        )
        self.assertEqual(
            boundary["basis_state_reader_scope"],
            "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
        )
        self.assert_allowed_command_set(boundary)
        self.assertIs(boundary["state_command_may_be_considered"], True)
        self.assertIs(boundary["lookup_first_orientation_locator_command_may_be_considered"], True)
        self.assertIs(boundary["lookup_second_orientation_locator_command_may_be_considered"], True)
        self.assertIs(boundary["future_local_read_only_carrier_command_surface_may_be_considered"], True)
        for key in BOUNDARY_OBJECT_FALSE_FIELDS:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False)
        self.assert_boundary_not_wrapper(boundary)

        statement = self._statement(result)
        for key in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True)
        self.assert_non_claims_canonical_false(result)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_REUSABLE_LOOKUP_PERMISSION_ARTIFACT.exists():
            self.skipTest("default reusable lookup permission artifact is not present")
        if not DEFAULT_READ_ONLY_STATE_READER_ARTIFACT.exists():
            self.skipTest("default read-only state packet artifact is not present")

        request = (
            resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_request()
        )
        self.assert_default_state_reader_path_uses_state_packet_filename(request)
        result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
            request
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            result["local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata"][
                "failed_check_count"
            ],
            0,
        )
        self.assert_not_blocked(result)
        boundary = self._boundary(result)
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY",
        )
        self.assertEqual(
            boundary["boundary_scope"],
            "LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY",
        )
        self.assertTrue(boundary["basis_read_only_state_reader_artifact"].endswith(STANDING_STATE_PACKET_FILENAME))
        self.assertNotIn(NON_STANDING_STATE_READER_FILENAME, boundary["basis_read_only_state_reader_artifact"])
        self.assertEqual(boundary["basis_state_packet_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET")
        self.assertEqual(boundary["basis_state_reader_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER")
        self.assertEqual(boundary["basis_state_reader_scope"], "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY")
        self.assert_allowed_command_set(boundary)
        self.assertIs(boundary["future_local_read_only_carrier_command_surface_may_be_considered"], True)
        for key in BOUNDARY_OBJECT_FALSE_FIELDS:
            self.assertIs(boundary[key], False)
        self.assert_no_forbidden_result_posture(result)

    def test_required_false_non_claim_flips_block_and_canonicalize_result(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base_request, _, _, _, _ = self._clean_request(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_common(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_no_forbidden_result_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        def set_field(field: str, value: Any) -> Callable[[dict[str, Any], Path], None]:
            def mutate(request: dict[str, Any], tmp_path: Path) -> None:
                request[field] = value

            return mutate

        def pop_field(field: str) -> Callable[[dict[str, Any], Path], None]:
            def mutate(request: dict[str, Any], tmp_path: Path) -> None:
                request.pop(field, None)

            return mutate

        def set_missing_temp_path(field: str, filename: str) -> Callable[[dict[str, Any], Path], None]:
            def mutate(request: dict[str, Any], tmp_path: Path) -> None:
                request[field] = str(tmp_path / filename)

            return mutate

        def write_reusable(value: Any) -> Callable[[dict[str, Any], Path], None]:
            def mutate(request: dict[str, Any], tmp_path: Path) -> None:
                _write_json(Path(request["selected_reusable_lookup_permission_artifact"]), value)

            return mutate

        def write_state_reader(value: Any) -> Callable[[dict[str, Any], Path], None]:
            def mutate(request: dict[str, Any], tmp_path: Path) -> None:
                _write_json(Path(request["selected_read_only_state_reader_artifact"]), value)

            return mutate

        cases: list[tuple[str, Callable[[dict[str, Any], Path], None] | str]] = [
            ("explicit block intent", set_field("local_relevance_medium_read_only_local_carrier_command_surface_boundary_intent", "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY")),
            ("missing request", "EMPTY_REQUEST"),
            ("non-mapping request", "NON_MAPPING_REQUEST"),
            ("unsupported intent", set_field("local_relevance_medium_read_only_local_carrier_command_surface_boundary_intent", "UNSUPPORTED_INTENT")),
            ("reusable lookup permission artifact path missing", set_field("selected_reusable_lookup_permission_artifact", "")),
            ("reusable lookup permission artifact unreadable", set_missing_temp_path("selected_reusable_lookup_permission_artifact", "missing_reusable_artifact.json")),
            ("reusable lookup permission artifact JSON array instead of object", write_reusable([])),
            ("reusable lookup permission artifact not recorded", write_reusable(_reusable_lookup_permission_artifact(outcome="LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_NOT_RECORDED"))),
            ("reusable lookup permission artifact failed checks present", write_reusable(_reusable_lookup_permission_artifact(failed_check_count=1))),
            ("reusable lookup permission artifact version not 0.1.0", write_reusable(_reusable_lookup_permission_artifact(result_version="9.9.9"))),
            ("read-only state reader artifact path missing", set_field("selected_read_only_state_reader_artifact", "")),
            ("read-only state reader artifact unreadable", set_missing_temp_path("selected_read_only_state_reader_artifact", "missing_state_reader_artifact.json")),
            ("read-only state reader artifact JSON array instead of object", write_state_reader([])),
            ("read-only state reader artifact not recorded", write_state_reader(_read_only_state_reader_artifact(outcome="LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_NOT_RECORDED"))),
            ("read-only state reader artifact failed checks present", write_state_reader(_read_only_state_reader_artifact(failed_check_count=1))),
            ("read-only state reader artifact version not 0.1.0", write_state_reader(_read_only_state_reader_artifact(result_version="9.9.9"))),
            ("read-only state packet object missing", write_state_reader(_read_only_state_reader_artifact(include_packet=False))),
            ("state packet type not exact", write_state_reader(_read_only_state_reader_artifact(packet_overrides={"state_packet_type": "WRONG"}))),
            ("state reader type not exact", write_state_reader(_read_only_state_reader_artifact(packet_overrides={"state_reader_type": "WRONG"}))),
            ("state reader scope not exact", write_state_reader(_read_only_state_reader_artifact(packet_overrides={"state_reader_scope": "WRONG"}))),
            ("allowed commands not exact", set_field("allowed_commands", ["state"])),
            ("allowed command count not three", set_field("allowed_command_count", 2)),
            ("state command may not be considered", set_field("state_command_may_be_considered", False)),
            ("lookup first orientation locator command may not be considered", set_field("lookup_first_orientation_locator_command_may_be_considered", False)),
            ("lookup second orientation locator command may not be considered", set_field("lookup_second_orientation_locator_command_may_be_considered", False)),
            ("future local read-only carrier command surface may not be considered", set_field("future_local_read_only_carrier_command_surface_may_be_considered", False)),
            ("boundary type missing", pop_field("boundary_type")),
            ("boundary type not exact", set_field("boundary_type", "WRONG")),
            ("boundary scope missing", pop_field("boundary_scope")),
            ("boundary scope not exact", set_field("boundary_scope", "WRONG")),
            ("local carrier command surface created", set_field("local_carrier_command_surface_created", True)),
            ("command execution performed", set_field("command_execution_performed", True)),
            ("operation permission created", set_field("operation_permission_created", True)),
            ("runtime permission created", set_field("runtime_permission_created", True)),
            ("public API created", set_field("public_api_created", True)),
            ("participant-facing interface created", set_field("participant_facing_interface_created", True)),
            ("distributed network behavior created", set_field("distributed_network_behavior_created", True)),
            ("general lookup permission created", set_field("general_lookup_permission_created", True)),
            ("arbitrary lookup permission created", set_field("arbitrary_lookup_permission_created", True)),
            ("unsupported commands permitted", set_field("unsupported_commands_permitted", True)),
            ("unsupported lookup keys permitted", set_field("unsupported_lookup_keys_permitted", True)),
            ("new lookup result created", set_field("new_lookup_result_created", True)),
            ("new lookup entry created", set_field("new_lookup_entry_created", True)),
            ("new signal accepted", set_field("new_signal_accepted", True)),
            ("new entry accepted", set_field("new_entry_accepted", True)),
            ("new relevance object created", set_field("new_relevance_object_created", True)),
            ("new index entry created", set_field("new_index_entry_created", True)),
            ("filesystem discovery performed", set_field("filesystem_discovery_performed", True)),
            ("registry created", set_field("registry_created", True)),
            ("search surface created", set_field("search_surface_created", True)),
            ("query surface created", set_field("query_surface_created", True)),
            ("ranking surface created", set_field("ranking_surface_created", True)),
            ("scoring surface created", set_field("scoring_surface_created", True)),
            ("priority surface created", set_field("priority_surface_created", True)),
            ("validity judgment created", set_field("validity_judgment_created", True)),
            ("truth judgment created", set_field("truth_judgment_created", True)),
            ("authority judgment created", set_field("authority_judgment_created", True)),
            ("currentness judgment created", set_field("currentness_judgment_created", True)),
            ("repeated reception permission created", set_field("repeated_reception_permission_created", True)),
            ("arbitrary reception created", set_field("arbitrary_reception_created", True)),
            ("feed created", set_field("feed_created", True)),
            ("source transfer occurred", set_field("source_transfer_occurred", True)),
            ("source receipt occurred", set_field("source_receipt_occurred", True)),
            ("source created", set_field("source_created", True)),
            ("authority created", set_field("authority_created", True)),
            ("currentness created", set_field("currentness_created", True)),
            ("truth created", set_field("truth_created", True)),
            ("action created", set_field("action_created", True)),
            ("synchronization created", set_field("synchronization_created", True)),
            ("participation authorized", set_field("participation_authorized", True)),
            ("participant role created", set_field("participant_role_created", True)),
            ("deployment created", set_field("deployment_created", True)),
            ("public release created", set_field("public_release_created", True)),
            ("broader reusable permission created", set_field("broader_reusable_permission_created", True)),
            ("follow-on work authorized", set_field("follow_on_work_authorized", True)),
            ("artifact existence treated as authority", set_field("artifact_existence_treated_as_carrier_command_boundary_authority", True)),
            ("latest file posture treated as authority", set_field("latest_file_posture_treated_as_carrier_command_boundary_authority", True)),
            ("repo local availability treated as authority", set_field("repo_local_availability_treated_as_carrier_command_boundary_authority", True)),
            ("hidden repo state used as content", set_field("hidden_repo_state_used_as_carrier_command_boundary_content", True)),
            ("hidden repo state used as authority", set_field("hidden_repo_state_used_as_carrier_command_boundary_authority", True)),
            ("predecessor failure repaired", set_field("predecessor_failure_repaired", True)),
            ("predecessor failure hidden", set_field("predecessor_failure_hidden", True)),
            ("predecessor failure claimed passed", set_field("predecessor_failure_claimed_passed", True)),
            ("consumed request reopened", set_field("consumed_request_reopened", True)),
            ("authorization token reused", set_field("authorization_token_reused", True)),
            ("required non-claim flipped", lambda request, tmp_path: request["declared_non_claims"].__setitem__("local_carrier_command_surface_created", True)),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            for name, mutate in cases:
                with self.subTest(name=name):
                    if mutate == "NON_MAPPING_REQUEST":
                        result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
                            "not a mapping"
                        )
                    elif mutate == "EMPTY_REQUEST":
                        result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
                            {}
                        )
                    else:
                        request, _, _, _, _ = self._clean_request(tmp_path)
                        mutate(request, tmp_path)
                        result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
                            request
                        )
                    self.assert_blocked_common(result)

    def test_missing_or_incomplete_declared_non_claims_canonicalize_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base_request, _, _, _, _ = self._clean_request(Path(tmp))
            first_key = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            variants: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
                ("remove declared_non_claims", lambda request: request.pop("declared_non_claims", None)),
                ("empty declared_non_claims", lambda request: request.__setitem__("declared_non_claims", {})),
                ("remove one required non-claim", lambda request: request["declared_non_claims"].pop(first_key)),
                ("non-bool string", lambda request: request["declared_non_claims"].__setitem__(first_key, "false")),
                ("none value", lambda request: request["declared_non_claims"].__setitem__(first_key, None)),
            ]
            for name, mutate in variants:
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
                        request
                    )
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS},
                    )
                    self.assert_all_public_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = self._resolve_clean(Path(tmp))
        boundary = self._boundary(result)
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY",
        )
        self.assertEqual(
            boundary["boundary_scope"],
            "LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY",
        )
        self.assert_allowed_command_set(boundary)
        self.assertEqual(boundary["basis_state_packet_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET")
        self.assertEqual(boundary["basis_state_reader_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER")
        self.assertEqual(boundary["basis_state_reader_scope"], "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_BLOCKED",
            },
        )
        serialized_boundary = json.dumps(boundary, sort_keys=True)
        self.assertNotIn("[REDACTED", serialized_boundary)

    def test_raw_hidden_hostile_content_is_contained(self) -> None:
        sentinel = HOSTILE_SENTINELS[0]
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            reusable = _reusable_lookup_permission_artifact(
                extra_fields={"raw_reusable_lookup_permission_body": sentinel}
            )
            state_reader = _read_only_state_reader_artifact(
                extra_fields={"raw_state_packet_body": HOSTILE_SENTINELS[6]}
            )
            request, _, _, _, _ = self._clean_request(
                tmp_path,
                reusable_artifact=reusable,
                state_reader_artifact=state_reader,
            )
            request["raw_full_body"] = HOSTILE_SENTINELS[7]
            request["hidden_repo_state"] = {"payload": HOSTILE_SENTINELS[-1]}
            original_request = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
                request
            )
        self.assertEqual(request, original_request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for raw in HOSTILE_SENTINELS:
            self.assertNotIn(raw, serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY", serialized)
        self.assertIn("LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY", serialized)
        self.assertIn("state", serialized)
        self.assertIn("lookup first_orientation_locator", serialized)
        self.assertIn("lookup second_orientation_locator", serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET", serialized)
        self.assert_no_forbidden_result_posture(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request, _, _, _, _ = self._clean_request(tmp_path)
            request_path = tmp_path / "request.json"
            _write_json(request_path, request)
            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(
                result["local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata"][
                    "result_version"
                ],
                "0.1.0",
            )
            self.assertEqual(
                result["local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata"][
                    "resolver_module"
                ],
                resolver.RESOLVER_MODULE,
            )
            self.assert_not_blocked(result)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_common(malformed)

            array_path = tmp_path / "array.json"
            _write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_from_path(
                array_path
            )
            self.assert_blocked_common(array_result)

            missing_result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_from_path(
                tmp_path / "missing-request.json"
            )
            self.assert_blocked_common(missing_result)

            output_root = tmp_path / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_result(
                    result
                )
            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(second_path.name.endswith("_001.json"))
            with first_path.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn(
                "local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min",
                str(first_path),
            )
            for forbidden in FORBIDDEN_OUTPUT_ROOTS:
                self.assertFalse(_path_is_under(first_path, forbidden))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, reusable_path, state_reader_path, reusable, state_reader = self._clean_request(
                Path(tmp)
            )
            request["nested_payload"] = {
                "raw_local_carrier_command_surface_boundary_body": HOSTILE_SENTINELS[1]
            }
            original_request = copy.deepcopy(request)
            original_declared_non_claims = copy.deepcopy(request["declared_non_claims"])
            original_reusable = copy.deepcopy(reusable)
            original_state_reader = copy.deepcopy(state_reader)
            selected_reusable_path = request["selected_reusable_lookup_permission_artifact"]
            selected_state_reader_path = request["selected_read_only_state_reader_artifact"]

            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
                request
            )

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertEqual(request, original_request)
        self.assertEqual(request["declared_non_claims"], original_declared_non_claims)
        self.assertEqual(request["selected_reusable_lookup_permission_artifact"], selected_reusable_path)
        self.assertEqual(request["selected_read_only_state_reader_artifact"], selected_state_reader_path)
        self.assertEqual(request["boundary_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY")
        self.assertEqual(request["boundary_scope"], "LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY")
        self.assertEqual(
            request["allowed_commands"],
            ["state", "lookup first_orientation_locator", "lookup second_orientation_locator"],
        )
        self.assertEqual(reusable, original_reusable)
        self.assertEqual(state_reader, original_state_reader)
        self.assertTrue(str(reusable_path).endswith("synthetic_reusable_lookup_permission.json"))
        self.assertTrue(str(state_reader_path).endswith("synthetic_state_packet_reader.json"))

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _, _, _ = self._clean_request(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
                request
            )
            summary = resolver.build_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min_summary(
                result
            )
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
            self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
            self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
            self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
            self.assertIs(result["non_claims"]["authorization_token_reused"], False)

            for field in (
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
                "consumed_request_reopened",
                "authorization_token_reused",
            ):
                blocked_request = copy.deepcopy(request)
                blocked_request[field] = True
                blocked = resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_boundary_v0_min(
                    blocked_request
                )
                self.assert_blocked_common(blocked)


if __name__ == "__main__":
    unittest.main()
