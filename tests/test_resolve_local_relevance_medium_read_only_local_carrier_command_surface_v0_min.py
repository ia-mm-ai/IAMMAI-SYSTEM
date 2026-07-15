"""Tests for the local relevance medium read-only local carrier command surface.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE object. It
verifies that the resolver reads one clean local carrier command surface
boundary artifact, one clean reusable lookup permission artifact, and one clean
read-only state reader / state packet artifact using the standing state packet
path, then records one local read-only carrier-facing command surface with a
closed command set.

The suite does not create command execution behavior, command execution result
behavior, operation permission, runtime permission, API behavior, distributed
behavior, general lookup permission, arbitrary lookup permission, unsupported
command permission, unsupported-key permission, new lookup result, new lookup
entry, registry, search, query surface, ranking, scoring, priority, validity
judgment, truth judgment, authority judgment, currentness judgment, repeated
reception permission, arbitrary reception, feed, new signal, new entry, new
relevance object, new index entry, filesystem discovery, source transfer,
source receipt, action, synchronization, participation, or follow-on work.
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

import resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min as resolver  # noqa: E402


DEFAULT_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "local_carrier_command_surface_boundary_v0_min/"
    "local_relevance_medium_read_only_local_carrier_command_surface_boundary_"
    "reference_review_001__local_relevance_medium_read_only_local_carrier_"
    "command_surface_boundary_v0_min_result.json"
)
DEFAULT_REUSABLE_LOOKUP_PERMISSION_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "reusable_lookup_permission_v0_min/"
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
    "local_carrier_command_surface_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "local_carrier_command_surface_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "reusable_lookup_permission_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "reusable_lookup_permission_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "lookup_pair_coverage_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "second_orientation_lookup_result_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "orientation_lookup_result_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "orientation_index_system_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "state_reader_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_comparison_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_relation_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_multiplicity_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_local_"
        "relevance_orientation_index_entry_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_"
        "orientation_view_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_"
        "relevance_receipt_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_"
        "relevance_reception_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_successor_"
        "candidate_admission_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_successor_"
        "reception_request_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_loop_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_local_carrier_command_surface_metadata",
    "declared_local_relevance_medium_read_only_local_carrier_command_surface_question",
    "selected_local_carrier_command_surface_boundary_artifact_basis",
    "selected_reusable_lookup_permission_artifact_basis",
    "selected_read_only_state_reader_artifact_basis",
    "local_relevance_medium_read_only_local_carrier_command_surface",
    "local_relevance_medium_read_only_local_carrier_command_surface_checks",
    "local_relevance_medium_read_only_local_carrier_command_surface_statement",
    "local_relevance_medium_read_only_local_carrier_command_surface_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_local_carrier_command_surface_summary",
)

FORBIDDEN_SURFACE_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_local_carrier_command_surface_checks",
    "non_claims",
    "local_relevance_medium_read_only_local_carrier_command_surface_summary",
    "local_relevance_medium_read_only_local_carrier_command_surface_metadata",
)

SURFACE_OBJECT_FALSE_FIELDS = (
    "command_execution_performed",
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
    "local_relevance_medium_read_only_local_carrier_command_surface_recorded",
    "basis_local_carrier_command_surface_boundary_artifact_preserved",
    "basis_reusable_lookup_permission_artifact_preserved",
    "basis_read_only_state_reader_artifact_preserved",
    "basis_state_packet_object_preserved",
    "basis_state_reader_type_preserved",
    "basis_state_reader_scope_preserved",
    "allowed_commands_preserved",
    "allowed_command_count_is_three",
    "state_command_available",
    "lookup_first_orientation_locator_command_available",
    "lookup_second_orientation_locator_command_available",
    "command_surface_local_only",
    "command_surface_read_only",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_SURFACE_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_EXECUTION_RESULT_BODY_MUST_NOT_RETURN",
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


def _path_is_same_or_under(candidate: Path, root: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def _local_carrier_command_surface_boundary_artifact(
    *,
    outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_RECORDED",
    result_version: str = "0.1.0",
    failed_check_count: int = 0,
    boundary_overrides: Mapping[str, Any] | None = None,
    extra: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    boundary = {
        "boundary_id": "local_relevance_medium_read_only_local_carrier_command_surface_boundary_001",
        "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY",
        "boundary_scope": "LOCAL_READ_ONLY_CARRIER_COMMAND_SURFACE_CONSIDERATION_ONLY",
        "allowed_commands": [
            "state",
            "lookup first_orientation_locator",
            "lookup second_orientation_locator",
        ],
        "allowed_command_count": 3,
        "state_command_may_be_considered": True,
        "lookup_first_orientation_locator_command_may_be_considered": True,
        "lookup_second_orientation_locator_command_may_be_considered": True,
        "future_local_read_only_carrier_command_surface_may_be_considered": True,
    }
    if boundary_overrides:
        boundary.update(copy.deepcopy(dict(boundary_overrides)))
    artifact = {
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary_metadata": {
            "result_version": result_version,
            "failed_check_count": failed_check_count,
        },
        "local_relevance_medium_read_only_local_carrier_command_surface_boundary": boundary,
    }
    if extra:
        artifact.update(copy.deepcopy(dict(extra)))
    return artifact


def _reusable_lookup_permission_artifact(
    *,
    outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_RECORDED",
    result_version: str = "0.1.0",
    failed_check_count: int = 0,
    permission_overrides: Mapping[str, Any] | None = None,
    extra: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    permission = {
        "permission_id": "local_relevance_medium_read_only_reusable_lookup_permission_001",
        "permission_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION",
        "permission_scope": "REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY",
        "supported_lookup_keys": [
            "first_orientation_locator",
            "second_orientation_locator",
        ],
        "covered_lookup_keys": [
            "first_orientation_locator",
            "second_orientation_locator",
        ],
        "permitted_lookup_keys": [
            "first_orientation_locator",
            "second_orientation_locator",
        ],
        "reusable_read_only_lookup_permission_created": True,
        "reusable_read_only_lookup_permission_scope_bounded": True,
        "repeated_read_only_deterministic_lookup_permitted": True,
        "general_lookup_permission_created": False,
        "arbitrary_lookup_permission_created": False,
        "unsupported_lookup_keys_permitted": False,
    }
    if permission_overrides:
        permission.update(copy.deepcopy(dict(permission_overrides)))
    artifact = {
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "local_relevance_medium_read_only_reusable_lookup_permission_metadata": {
            "result_version": result_version,
            "failed_check_count": failed_check_count,
        },
        "local_relevance_medium_read_only_reusable_lookup_permission": permission,
    }
    if extra:
        artifact.update(copy.deepcopy(dict(extra)))
    return artifact


def _read_only_state_reader_artifact(
    *,
    outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED",
    result_version: str = "0.1.0",
    failed_check_count: int = 0,
    packet_overrides: Mapping[str, Any] | None = None,
    include_packet: bool = True,
    extra: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    packet = {
        "state_packet_id": "local_relevance_medium_read_only_state_packet_001",
        "state_packet_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
        "state_reader_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
        "state_reader_scope": "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
    }
    if packet_overrides:
        packet.update(copy.deepcopy(dict(packet_overrides)))
    artifact = {
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "local_relevance_medium_read_only_state_reader_metadata": {
            "result_version": result_version,
            "failed_check_count": failed_check_count,
        },
        "local_relevance_medium_read_only_state_reader": {
            "state_reader_type": packet.get("state_reader_type"),
            "state_reader_scope": packet.get("state_reader_scope"),
        },
    }
    if include_packet:
        artifact["local_relevance_medium_read_only_state_packet"] = packet
    if extra:
        artifact.update(copy.deepcopy(dict(extra)))
    return artifact


def _write_synthetic_artifacts(
    directory: Path,
    *,
    boundary_artifact: Mapping[str, Any] | None = None,
    reusable_artifact: Mapping[str, Any] | None = None,
    state_artifact: Mapping[str, Any] | None = None,
) -> tuple[Path, Path, Path]:
    boundary_path = directory / "boundary.json"
    reusable_path = directory / "reusable_lookup_permission.json"
    state_path = directory / "state_packet.json"
    _write_json(
        boundary_path,
        boundary_artifact or _local_carrier_command_surface_boundary_artifact(),
    )
    _write_json(reusable_path, reusable_artifact or _reusable_lookup_permission_artifact())
    _write_json(state_path, state_artifact or _read_only_state_reader_artifact())
    return boundary_path, reusable_path, state_path


def _valid_request(
    boundary_path: Path,
    reusable_path: Path,
    state_path: Path,
    **overrides: Any,
) -> dict[str, Any]:
    request = (
        resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_request(
            selected_local_carrier_command_surface_boundary_artifact=str(boundary_path),
            selected_reusable_lookup_permission_artifact=str(reusable_path),
            selected_read_only_state_reader_artifact=str(state_path),
        )
    )
    request.update(copy.deepcopy(overrides))
    return request


def _serialized(value: Any) -> str:
    return json.dumps(value, sort_keys=True)


class LocalCarrierCommandSurfaceResolverTests(unittest.TestCase):
    def assert_not_blocked(self, result):
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def surface(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        surface = result["local_relevance_medium_read_only_local_carrier_command_surface"]
        self.assertIsInstance(surface, dict)
        return surface

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result[
            "local_relevance_medium_read_only_local_carrier_command_surface_statement"
        ]
        self.assertIsInstance(statement, dict)
        return statement

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result[
            "local_relevance_medium_read_only_local_carrier_command_surface_checks"
        ]
        self.assertIsInstance(checks, list)
        return checks

    def block_code(self, result: Mapping[str, Any]) -> str:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        code = block.get("block_code") or block.get("code")
        self.assertIsInstance(code, str)
        return code

    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        public_codes = set(resolver.BLOCK_CODES)
        self.assertIn(self.block_code(result), public_codes)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                if key in check:
                    self.assertIn(check[key], public_codes)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIs(type(non_claims[key]), bool)

    def assert_surface_not_wrapper(self, surface: Mapping[str, Any]) -> None:
        for key in FORBIDDEN_SURFACE_WRAPPER_FIELDS:
            self.assertNotIn(key, surface)

    def assert_allowed_commands_preserved(self, surface: Mapping[str, Any]) -> None:
        self.assertEqual(surface["allowed_commands"], list(resolver.ALLOWED_COMMANDS))
        self.assertEqual(surface["allowed_command_count"], 3)

    def assert_no_overreach_posture(self, result: Mapping[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        surface = self.surface(result)
        for key in SURFACE_OBJECT_FALSE_FIELDS:
            if key in surface:
                self.assertIs(surface[key], False, key)
        non_claims = result["non_claims"]
        for key in (
            "command_execution_performed",
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
            "follow_on_work_authorized",
        ):
            self.assertIs(non_claims[key], False, key)

    def assert_no_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _serialized(result)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_default_state_reader_uses_state_packet_filename(
        self, request: Mapping[str, Any]
    ) -> None:
        state_path = request["selected_read_only_state_reader_artifact"]
        self.assertTrue(state_path.endswith(STANDING_STATE_PACKET_FILENAME))
        self.assertNotIn(NON_STANDING_STATE_READER_FILENAME, state_path)

    def assert_recorded_result_shape(
        self,
        result: Mapping[str, Any],
        *,
        boundary_path: Path,
        reusable_path: Path,
        state_path: Path,
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        metadata = result[
            "local_relevance_medium_read_only_local_carrier_command_surface_metadata"
        ]
        self.assertEqual(metadata["failed_check_count"], 0)
        self.assertGreater(metadata["passed_check_count"], 0)
        self.assertEqual(metadata["result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        for key in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(key, result)

        surface = self.surface(result)
        self.assertEqual(
            surface["command_surface_id"],
            "local_relevance_medium_read_only_local_carrier_command_surface_001",
        )
        self.assertEqual(
            surface["command_surface_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE",
        )
        self.assertEqual(surface["command_surface_version"], "0.1.0")
        self.assertEqual(
            surface["command_surface_scope"],
            "LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY",
        )
        self.assertEqual(
            surface["basis_local_carrier_command_surface_boundary_artifact"],
            str(boundary_path),
        )
        self.assertEqual(
            surface["basis_local_carrier_command_surface_boundary_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            surface["basis_local_carrier_command_surface_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            surface["basis_local_carrier_command_surface_boundary_failed_check_count"],
            0,
        )
        self.assertEqual(surface["basis_reusable_lookup_permission_artifact"], str(reusable_path))
        self.assertEqual(
            surface["basis_reusable_lookup_permission_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_RECORDED",
        )
        self.assertEqual(
            surface["basis_reusable_lookup_permission_result_version"], "0.1.0"
        )
        self.assertEqual(
            surface["basis_reusable_lookup_permission_failed_check_count"], 0
        )
        self.assertEqual(surface["basis_read_only_state_reader_artifact"], str(state_path))
        self.assertEqual(
            surface["basis_read_only_state_reader_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED",
        )
        self.assertEqual(surface["basis_read_only_state_reader_result_version"], "0.1.0")
        self.assertEqual(surface["basis_read_only_state_reader_failed_check_count"], 0)
        self.assertEqual(
            surface["basis_state_packet_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
        )
        self.assertEqual(
            surface["basis_state_reader_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
        )
        self.assertEqual(
            surface["basis_state_reader_scope"],
            "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
        )
        self.assert_allowed_commands_preserved(surface)
        self.assertIs(surface["state_command_available"], True)
        self.assertIs(surface["lookup_first_orientation_locator_command_available"], True)
        self.assertIs(surface["lookup_second_orientation_locator_command_available"], True)
        self.assertIs(surface["local_carrier_command_surface_recorded"], True)
        self.assertIs(surface["command_surface_local_only"], True)
        self.assertIs(surface["command_surface_read_only"], True)
        self.assert_surface_not_wrapper(surface)

        for key in SURFACE_OBJECT_FALSE_FIELDS:
            self.assertIn(key, surface)
            self.assertIs(surface[key], False, key)

        statement = self.statement(result)
        for key in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
        self.assert_non_claims_canonical_false(result)

    def test_public_api_constants_and_default_builder_paths(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min",
            "resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_from_path",
            "write_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_result",
            "build_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_COMMAND_SURFACE_TYPE_VALUES",
            "SUPPORTED_COMMAND_SURFACE_SCOPE_VALUES",
            "ALLOWED_COMMANDS",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min",
        )
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE",
            resolver.SUPPORTED_COMMAND_SURFACE_TYPE_VALUES,
        )
        self.assertIn(
            "LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY",
            resolver.SUPPORTED_COMMAND_SURFACE_SCOPE_VALUES,
        )
        self.assertEqual(
            list(resolver.ALLOWED_COMMANDS),
            ["state", "lookup first_orientation_locator", "lookup second_orientation_locator"],
        )

        request = (
            resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_request()
        )
        self.assertTrue(
            request["selected_local_carrier_command_surface_boundary_artifact"].endswith(
                "local_relevance_medium_read_only_local_carrier_command_surface_boundary_"
                "reference_review_001__local_relevance_medium_read_only_local_carrier_"
                "command_surface_boundary_v0_min_result.json"
            )
        )
        self.assertTrue(
            request["selected_reusable_lookup_permission_artifact"].endswith(
                "local_relevance_medium_read_only_reusable_lookup_permission_reference_review_001__"
                "local_relevance_medium_read_only_reusable_lookup_permission_v0_min_result.json"
            )
        )
        self.assert_default_state_reader_uses_state_packet_filename(request)

        output_root = Path(resolver.OUTPUT_ROOT)
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            self.assertFalse(_path_is_same_or_under(output_root, forbidden), forbidden)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary_path, reusable_path, state_path = _write_synthetic_artifacts(tmp_path)
            request = _valid_request(boundary_path, reusable_path, state_path)
            result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min(
                    request
                )
            )
            self.assert_recorded_result_shape(
                result,
                boundary_path=boundary_path,
                reusable_path=reusable_path,
                state_path=state_path,
            )

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        default_paths = (
            DEFAULT_LOCAL_CARRIER_COMMAND_SURFACE_BOUNDARY_ARTIFACT,
            DEFAULT_REUSABLE_LOOKUP_PERMISSION_ARTIFACT,
            DEFAULT_READ_ONLY_STATE_READER_ARTIFACT,
        )
        if not all(path.exists() for path in default_paths):
            self.skipTest("default live artifacts are not all present")

        request = (
            resolver.build_declared_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_request()
        )
        self.assert_default_state_reader_uses_state_packet_filename(request)
        result = (
            resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min(
                request
            )
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            result[
                "local_relevance_medium_read_only_local_carrier_command_surface_metadata"
            ]["failed_check_count"],
            0,
        )
        self.assert_not_blocked(result)
        surface = self.surface(result)
        self.assertEqual(
            surface["command_surface_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE",
        )
        self.assertEqual(
            surface["command_surface_scope"],
            "LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY",
        )
        self.assertTrue(
            surface["basis_read_only_state_reader_artifact"].endswith(
                STANDING_STATE_PACKET_FILENAME
            )
        )
        self.assertNotIn(
            NON_STANDING_STATE_READER_FILENAME,
            surface["basis_read_only_state_reader_artifact"],
        )
        self.assertEqual(
            surface["basis_state_packet_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
        )
        self.assertEqual(
            surface["basis_state_reader_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
        )
        self.assertEqual(
            surface["basis_state_reader_scope"],
            "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
        )
        self.assert_allowed_commands_preserved(surface)
        self.assertIs(surface["state_command_available"], True)
        self.assertIs(surface["lookup_first_orientation_locator_command_available"], True)
        self.assertIs(surface["lookup_second_orientation_locator_command_available"], True)
        self.assertIs(surface["local_carrier_command_surface_recorded"], True)
        self.assertIs(surface["command_surface_local_only"], True)
        self.assertIs(surface["command_surface_read_only"], True)
        self.assert_no_overreach_posture(result)

    def test_declared_non_claim_flips_block_and_output_remains_false(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, reusable_path, state_path = _write_synthetic_artifacts(Path(tmp))
            clean_request = _valid_request(boundary_path, reusable_path, state_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min(
                            request
                        )
                    )
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assert_public_codes(result)
                    self.assertTrue(
                        any(check.get("passed") is not True for check in self.checks(result))
                    )
                    self.assert_non_claims_canonical_false(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_no_overreach_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        def with_artifacts(
            mutation: Callable[[dict[str, Any], Path], Any] | None = None,
            *,
            boundary_artifact: Mapping[str, Any] | None = None,
            reusable_artifact: Mapping[str, Any] | None = None,
            state_artifact: Mapping[str, Any] | None = None,
        ) -> Callable[[Path], Any]:
            def build(tmp_path: Path) -> Any:
                boundary_path, reusable_path, state_path = _write_synthetic_artifacts(
                    tmp_path,
                    boundary_artifact=boundary_artifact,
                    reusable_artifact=reusable_artifact,
                    state_artifact=state_artifact,
                )
                request = _valid_request(boundary_path, reusable_path, state_path)
                if mutation is not None:
                    return mutation(request, tmp_path)
                return request

            return build

        def set_field(name: str, value: Any) -> Callable[[dict[str, Any], Path], dict[str, Any]]:
            def mutate(request: dict[str, Any], _: Path) -> dict[str, Any]:
                request[name] = value
                return request

            return mutate

        def del_field(name: str) -> Callable[[dict[str, Any], Path], dict[str, Any]]:
            def mutate(request: dict[str, Any], _: Path) -> dict[str, Any]:
                request.pop(name, None)
                return request

            return mutate

        def artifact_array(field: str) -> Callable[[dict[str, Any], Path], dict[str, Any]]:
            def mutate(request: dict[str, Any], tmp_path: Path) -> dict[str, Any]:
                path = tmp_path / f"{field}_array.json"
                _write_json(path, [])
                request[field] = str(path)
                return request

            return mutate

        block_cases: list[tuple[str, Any]] = [
            (
                "explicit block intent",
                with_artifacts(set_field("local_relevance_medium_read_only_local_carrier_command_surface_intent", resolver.INTENT_BLOCK)),
            ),
            ("missing request", lambda _tmp: {}),
            ("non-mapping request", lambda _tmp: "not a mapping"),
            (
                "unsupported intent",
                with_artifacts(set_field("local_relevance_medium_read_only_local_carrier_command_surface_intent", "UNSUPPORTED")),
            ),
            (
                "boundary artifact path missing",
                with_artifacts(set_field("selected_local_carrier_command_surface_boundary_artifact", "")),
            ),
            (
                "boundary artifact unreadable",
                with_artifacts(set_field("selected_local_carrier_command_surface_boundary_artifact", "missing-boundary.json")),
            ),
            (
                "boundary artifact JSON array",
                with_artifacts(artifact_array("selected_local_carrier_command_surface_boundary_artifact")),
            ),
            (
                "boundary artifact not recorded",
                with_artifacts(boundary_artifact=_local_carrier_command_surface_boundary_artifact(outcome="NOT_RECORDED")),
            ),
            (
                "boundary artifact failed checks present",
                with_artifacts(boundary_artifact=_local_carrier_command_surface_boundary_artifact(failed_check_count=1)),
            ),
            (
                "boundary artifact version stale",
                with_artifacts(boundary_artifact=_local_carrier_command_surface_boundary_artifact(result_version="0.0.9")),
            ),
            (
                "reusable artifact path missing",
                with_artifacts(set_field("selected_reusable_lookup_permission_artifact", "")),
            ),
            (
                "reusable artifact unreadable",
                with_artifacts(set_field("selected_reusable_lookup_permission_artifact", "missing-reusable.json")),
            ),
            (
                "reusable artifact JSON array",
                with_artifacts(artifact_array("selected_reusable_lookup_permission_artifact")),
            ),
            (
                "reusable artifact not recorded",
                with_artifacts(reusable_artifact=_reusable_lookup_permission_artifact(outcome="NOT_RECORDED")),
            ),
            (
                "reusable artifact failed checks present",
                with_artifacts(reusable_artifact=_reusable_lookup_permission_artifact(failed_check_count=1)),
            ),
            (
                "reusable artifact version stale",
                with_artifacts(reusable_artifact=_reusable_lookup_permission_artifact(result_version="0.0.9")),
            ),
            (
                "state artifact path missing",
                with_artifacts(set_field("selected_read_only_state_reader_artifact", "")),
            ),
            (
                "state artifact unreadable",
                with_artifacts(set_field("selected_read_only_state_reader_artifact", "missing-state.json")),
            ),
            (
                "state artifact JSON array",
                with_artifacts(artifact_array("selected_read_only_state_reader_artifact")),
            ),
            (
                "state artifact not recorded",
                with_artifacts(state_artifact=_read_only_state_reader_artifact(outcome="NOT_RECORDED")),
            ),
            (
                "state artifact failed checks present",
                with_artifacts(state_artifact=_read_only_state_reader_artifact(failed_check_count=1)),
            ),
            (
                "state artifact version stale",
                with_artifacts(state_artifact=_read_only_state_reader_artifact(result_version="0.0.9")),
            ),
            (
                "state packet object missing",
                with_artifacts(state_artifact=_read_only_state_reader_artifact(include_packet=False)),
            ),
            (
                "state packet type wrong",
                with_artifacts(state_artifact=_read_only_state_reader_artifact(packet_overrides={"state_packet_type": "WRONG"})),
            ),
            (
                "state reader type wrong",
                with_artifacts(state_artifact=_read_only_state_reader_artifact(packet_overrides={"state_reader_type": "WRONG"})),
            ),
            (
                "state reader scope wrong",
                with_artifacts(state_artifact=_read_only_state_reader_artifact(packet_overrides={"state_reader_scope": "WRONG"})),
            ),
            ("allowed commands not exact", with_artifacts(set_field("allowed_commands", ["state"]))),
            ("allowed command count not three", with_artifacts(set_field("allowed_command_count", 2))),
            ("state command not available", with_artifacts(set_field("state_command_available", False))),
            (
                "lookup first command not available",
                with_artifacts(set_field("lookup_first_orientation_locator_command_available", False)),
            ),
            (
                "lookup second command not available",
                with_artifacts(set_field("lookup_second_orientation_locator_command_available", False)),
            ),
            ("command surface type missing", with_artifacts(del_field("command_surface_type"))),
            (
                "command surface type wrong",
                with_artifacts(set_field("command_surface_type", "WRONG")),
            ),
            ("command surface scope missing", with_artifacts(del_field("command_surface_scope"))),
            (
                "command surface scope wrong",
                with_artifacts(set_field("command_surface_scope", "WRONG")),
            ),
            (
                "local carrier command surface not recorded",
                with_artifacts(set_field("local_carrier_command_surface_recorded", False)),
            ),
            (
                "command surface local only not true",
                with_artifacts(set_field("command_surface_local_only", False)),
            ),
            (
                "command surface read only not true",
                with_artifacts(set_field("command_surface_read_only", False)),
            ),
            (
                "predecessor repaired",
                with_artifacts(set_field("predecessor_failure_repaired", True)),
            ),
            (
                "predecessor hidden",
                with_artifacts(set_field("predecessor_failure_hidden", True)),
            ),
            (
                "predecessor claimed passed",
                with_artifacts(set_field("predecessor_failure_claimed_passed", True)),
            ),
            (
                "required non-claim missing",
                with_artifacts(lambda request, _tmp: (request["declared_non_claims"].pop("runtime_permission_created"), request)[1]),
            ),
        ]
        for field_name in (
            "command_execution_performed",
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
            "artifact_existence_treated_as_carrier_command_surface_authority",
            "latest_file_posture_treated_as_carrier_command_surface_authority",
            "repo_local_availability_treated_as_carrier_command_surface_authority",
            "hidden_repo_state_used_as_carrier_command_surface_content",
            "hidden_repo_state_used_as_carrier_command_surface_authority",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            block_cases.append((field_name, with_artifacts(set_field(field_name, True))))

        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            for index, (name, builder) in enumerate(block_cases):
                with self.subTest(name=name):
                    case_dir = tmp_root / f"case_{index:03d}"
                    case_dir.mkdir()
                    request_or_value = builder(case_dir)
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min(
                            request_or_value
                        )
                    )
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assert_public_codes(result)
                    self.assert_no_overreach_posture(result)

    def test_missing_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, reusable_path, state_path = _write_synthetic_artifacts(Path(tmp))
            clean_request = _valid_request(boundary_path, reusable_path, state_path)
            variants = []
            missing_mapping = copy.deepcopy(clean_request)
            missing_mapping.pop("declared_non_claims")
            variants.append(("remove declared_non_claims", missing_mapping))
            empty_mapping = copy.deepcopy(clean_request)
            empty_mapping["declared_non_claims"] = {}
            variants.append(("empty declared_non_claims", empty_mapping))
            missing_one = copy.deepcopy(clean_request)
            missing_one["declared_non_claims"].pop("runtime_permission_created")
            variants.append(("remove one non-claim", missing_one))
            string_one = copy.deepcopy(clean_request)
            string_one["declared_non_claims"]["runtime_permission_created"] = "false"
            variants.append(("non-bool string", string_one))
            none_one = copy.deepcopy(clean_request)
            none_one["declared_non_claims"]["runtime_permission_created"] = None
            variants.append(("none value", none_one))

            for name, request in variants:
                with self.subTest(name=name):
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min(
                            request
                        )
                    )
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS},
                    )
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assert_public_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, reusable_path, state_path = _write_synthetic_artifacts(Path(tmp))
            result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min(
                    _valid_request(boundary_path, reusable_path, state_path)
                )
            )
            surface = self.surface(result)
            official_values = (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE",
                "LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
                "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
                "state",
                "lookup first_orientation_locator",
                "lookup second_orientation_locator",
            )
            self.assertEqual(
                surface["command_surface_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE",
            )
            self.assertEqual(
                surface["command_surface_scope"],
                "LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY",
            )
            self.assert_allowed_commands_preserved(surface)
            self.assertEqual(
                surface["basis_state_packet_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
            )
            self.assertEqual(
                surface["basis_state_reader_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
            )
            self.assertEqual(
                surface["basis_state_reader_scope"],
                "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(
                set(resolver.OUTCOME_FAMILY),
                {
                    resolver.OUTCOME_RECORDED,
                    resolver.OUTCOME_NOT_RECORDED,
                    resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                    resolver.OUTCOME_BLOCKED,
                },
            )
            serialized = _serialized(result)
            for value in official_values:
                self.assertIn(value, serialized)
            self.assertNotEqual(surface["command_surface_type"], "[REDACTED_RAW_CONTENT]")
            self.assertNotEqual(surface["command_surface_scope"], "[REDACTED_RAW_CONTENT]")

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary_artifact = _local_carrier_command_surface_boundary_artifact(
                extra={"raw_local_carrier_command_surface_boundary_body": HOSTILE_SENTINELS[2]}
            )
            reusable_artifact = _reusable_lookup_permission_artifact(
                extra={"raw_reusable_lookup_permission_body": HOSTILE_SENTINELS[5]}
            )
            state_artifact = _read_only_state_reader_artifact(
                extra={"hidden_repo_state": HOSTILE_SENTINELS[-1]}
            )
            boundary_path, reusable_path, state_path = _write_synthetic_artifacts(
                tmp_path,
                boundary_artifact=boundary_artifact,
                reusable_artifact=reusable_artifact,
                state_artifact=state_artifact,
            )
            request = _valid_request(
                boundary_path,
                reusable_path,
                state_path,
                raw_full_body=HOSTILE_SENTINELS[0],
                hidden_repo_state=HOSTILE_SENTINELS[-1],
            )
            original_request = copy.deepcopy(request)
            result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min(
                    request
                )
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assert_public_codes(result)
            self.assert_no_sentinels(result)
            serialized = _serialized(result)
            self.assertIn(
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE",
                serialized,
            )
            self.assertIn("LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY", serialized)
            self.assert_non_claims_canonical_false(result)
            self.assert_no_overreach_posture(result)
            self.assertEqual(request, original_request)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary_path, reusable_path, state_path = _write_synthetic_artifacts(tmp_path)
            request = _valid_request(boundary_path, reusable_path, state_path)
            request_path = tmp_path / "request.json"
            _write_json(request_path, request)

            result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_from_path(
                    request_path
                )
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(
                result[
                    "local_relevance_medium_read_only_local_carrier_command_surface_metadata"
                ]["result_version"],
                "0.1.0",
            )
            self.assertEqual(
                result[
                    "local_relevance_medium_read_only_local_carrier_command_surface_metadata"
                ]["resolver_module"],
                resolver.RESOLVER_MODULE,
            )
            self.assert_not_blocked(result)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_from_path(
                    malformed_path
                )
            )
            self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(malformed_result)

            array_path = tmp_path / "array.json"
            _write_json(array_path, [])
            array_result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_from_path(
                    array_path
                )
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(array_result)

            missing_result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_from_path(
                    tmp_path / "missing.json"
                )
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(missing_result)

            output_root = tmp_path / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = (
                    resolver.write_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_result(
                        result
                    )
                )
                second_path = (
                    resolver.write_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_result(
                        result
                    )
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
                "local_relevance_medium_read_only_local_carrier_command_surface_v0_min",
                str(first_path),
            )
            for forbidden in FORBIDDEN_OUTPUT_ROOTS:
                self.assertFalse(_path_is_same_or_under(first_path, tmp_path / forbidden))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary_artifact = _local_carrier_command_surface_boundary_artifact(
                extra={"raw_full_body": HOSTILE_SENTINELS[0]}
            )
            reusable_artifact = _reusable_lookup_permission_artifact(
                extra={"raw_full_body": HOSTILE_SENTINELS[5]}
            )
            state_artifact = _read_only_state_reader_artifact(
                extra={"raw_full_body": HOSTILE_SENTINELS[7]}
            )
            boundary_artifact_before = copy.deepcopy(boundary_artifact)
            reusable_artifact_before = copy.deepcopy(reusable_artifact)
            state_artifact_before = copy.deepcopy(state_artifact)
            boundary_path, reusable_path, state_path = _write_synthetic_artifacts(
                tmp_path,
                boundary_artifact=boundary_artifact,
                reusable_artifact=reusable_artifact,
                state_artifact=state_artifact,
            )
            request = _valid_request(
                boundary_path,
                reusable_path,
                state_path,
                posture_mappings={"nested": {"raw_full_body": HOSTILE_SENTINELS[0]}},
            )
            request_before = copy.deepcopy(request)
            declared_non_claims_before = copy.deepcopy(request["declared_non_claims"])
            result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min(
                    request
                )
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(request, request_before)
            self.assertEqual(request["declared_non_claims"], declared_non_claims_before)
            self.assertEqual(str(boundary_path), request["selected_local_carrier_command_surface_boundary_artifact"])
            self.assertEqual(str(reusable_path), request["selected_reusable_lookup_permission_artifact"])
            self.assertEqual(str(state_path), request["selected_read_only_state_reader_artifact"])
            self.assertEqual(boundary_artifact, boundary_artifact_before)
            self.assertEqual(reusable_artifact, reusable_artifact_before)
            self.assertEqual(state_artifact, state_artifact_before)
            self.assertEqual(
                request["command_surface_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOCAL_CARRIER_COMMAND_SURFACE",
            )
            self.assertEqual(
                request["command_surface_scope"],
                "LOCAL_READ_ONLY_STATE_AND_TWO_LOOKUP_COMMANDS_ONLY",
            )
            self.assertEqual(request["allowed_commands"], list(resolver.ALLOWED_COMMANDS))

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, reusable_path, state_path = _write_synthetic_artifacts(Path(tmp))
            result = (
                resolver.resolve_local_relevance_medium_read_only_local_carrier_command_surface_v0_min(
                    _valid_request(boundary_path, reusable_path, state_path)
                )
            )
            summary = resolver.build_local_relevance_medium_read_only_local_carrier_command_surface_v0_min_summary(
                result
            )
            non_claims = result["non_claims"]
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(non_claims["predecessor_failure_repaired"], False)
            self.assertIs(non_claims["predecessor_failure_hidden"], False)
            self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
            self.assertIs(non_claims["consumed_request_reopened"], False)
            self.assertIs(non_claims["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
