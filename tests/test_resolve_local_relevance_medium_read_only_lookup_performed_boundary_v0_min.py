"""Tests for the local read-only lookup performed boundary resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY object. It verifies
that the resolver reads one clean selected lookup command execution artifact and
records one local read-only selected-state lookup-performed-consideration
boundary.

The suite does not create lookup performed behavior, lookup result behavior,
operation permission, runtime permission, public API, participant-facing
interface, distributed behavior, general lookup permission, arbitrary lookup
permission, unsupported-command permission, unsupported-key permission, new
lookup entry, registry, search, query surface, ranking, scoring, priority,
validity judgment, truth judgment, authority judgment, currentness judgment,
repeated reception permission, arbitrary reception, feed, new signal, new entry,
new relevance object, new index entry, filesystem discovery, source transfer,
source receipt, participation, or follow-on work.
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

import resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min as resolver  # noqa: E402


DEFAULT_LOOKUP_COMMAND_EXECUTION_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_command_execution_v0_min/"
    "local_relevance_medium_read_only_lookup_command_execution_reference_review_"
    "001__local_relevance_medium_read_only_lookup_command_execution_v0_min_"
    "result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_performed_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_lookup_performed_boundary_metadata",
    "declared_local_relevance_medium_read_only_lookup_performed_boundary_question",
    "selected_lookup_command_execution_artifact_basis",
    "local_relevance_medium_read_only_lookup_performed_boundary",
    "local_relevance_medium_read_only_lookup_performed_boundary_checks",
    "local_relevance_medium_read_only_lookup_performed_boundary_statement",
    "local_relevance_medium_read_only_lookup_performed_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_lookup_performed_boundary_summary",
)

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_lookup_performed_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_lookup_performed_boundary_summary",
    "local_relevance_medium_read_only_lookup_performed_boundary_metadata",
)

BOUNDARY_FALSE_FIELDS = (
    "lookup_performed",
    "lookup_result_created",
    "operation_permission_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
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

COMMAND_EXECUTION_FALSE_FIELDS = (
    "lookup_performed",
    "lookup_result_created",
    "operation_permission_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
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

OFFICIAL_VALUES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY",
    "SELECTED_LOOKUP_PERFORMED_CONSIDERATION_ONLY",
    "state",
)


def path_has_root_parts(path: Path, root: Path) -> bool:
    path_parts = path.parts
    root_parts = root.parts
    if len(path_parts) < len(root_parts):
        return False
    return any(
        path_parts[index : index + len(root_parts)] == root_parts
        for index in range(len(path_parts) - len(root_parts) + 1)
    )


class LookupPerformedBoundaryResolverTests(unittest.TestCase):
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
        filename = f"{safe}.json"
        self.assertNotIn("/", filename)
        self.assertNotIn("\\", filename)
        return filename

    def synthetic_lookup_command_execution_artifact(self) -> dict[str, Any]:
        execution: dict[str, Any] = {
            "lookup_command_execution_id": (
                "local_relevance_medium_read_only_lookup_command_execution_001"
            ),
            "lookup_command_execution_type": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION"
            ),
            "lookup_command_execution_version": "0.1.0",
            "lookup_command_execution_scope": "SELECTED_LOOKUP_COMMAND_EXECUTION_ONLY",
            "basis_lookup_command_execution_boundary_artifact": (
                "synthetic_lookup_command_execution_boundary.json"
            ),
            "basis_lookup_command_execution_boundary_outcome": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BOUNDARY_RECORDED"
            ),
            "basis_lookup_command_execution_boundary_result_version": "0.1.0",
            "basis_lookup_command_execution_boundary_failed_check_count": 0,
            "basis_raw_full_state_packet_body_exposure_artifact": (
                "synthetic_raw_full_state_packet_body_exposure.json"
            ),
            "basis_raw_full_state_packet_body_exposure_outcome": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_RECORDED"
            ),
            "basis_raw_full_state_packet_body_exposure_result_version": "0.1.0",
            "basis_raw_full_state_packet_body_exposure_failed_check_count": 0,
            "selected_command": "state",
            "selected_command_is_state": True,
            "selected_raw_full_state_packet_body_exposure_recorded": True,
            "raw_full_state_packet_body_exposed": True,
            "raw_full_state_packet_body_exposure_local_only": True,
            "raw_full_state_packet_body_exposure_read_only": True,
            "local_relevance_medium_read_only_lookup_command_execution_recorded": True,
            "selected_lookup_command_execution_recorded": True,
            "lookup_command_executed": True,
            "lookup_command_execution_local_only": True,
            "lookup_command_execution_read_only": True,
        }
        for key in COMMAND_EXECUTION_FALSE_FIELDS:
            execution[key] = False
        statement = {
            "local_relevance_medium_read_only_lookup_command_execution_recorded": True,
            "basis_lookup_command_execution_boundary_artifact_preserved": True,
            "basis_raw_full_state_packet_body_exposure_artifact_preserved": True,
            "selected_command_preserved": True,
            "selected_command_is_state": True,
            "selected_raw_full_state_packet_body_exposure_recorded": True,
            "raw_full_state_packet_body_exposed": True,
            "raw_full_state_packet_body_exposure_local_only": True,
            "raw_full_state_packet_body_exposure_read_only": True,
            "selected_lookup_command_execution_recorded": True,
            "lookup_command_executed": True,
            "lookup_command_execution_local_only": True,
            "lookup_command_execution_read_only": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        summary = {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_RECORDED",
            "failed_check_count": 0,
            "passed_check_count": 89,
            "result_version": "0.1.0",
            "resolver_module": (
                "resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min"
            ),
            "selected_command": "state",
            "selected_command_is_state": True,
            "lookup_command_execution_recorded": True,
            "local_relevance_medium_read_only_lookup_command_execution_recorded": True,
            "selected_lookup_command_execution_recorded": True,
            "lookup_command_executed": True,
            "lookup_command_execution_local_only": True,
            "lookup_command_execution_read_only": True,
        }
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_RECORDED",
            "result_version": "0.1.0",
            "local_relevance_medium_read_only_lookup_command_execution_metadata": {
                "local_relevance_medium_read_only_lookup_command_execution_id": (
                    "local_relevance_medium_read_only_lookup_command_execution_001"
                ),
                "local_relevance_medium_read_only_lookup_command_execution_type": (
                    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION"
                ),
                "local_relevance_medium_read_only_lookup_command_execution_version": (
                    "0.1.0"
                ),
                "result_version": "0.1.0",
                "resolver_module": (
                    "resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min"
                ),
            },
            "local_relevance_medium_read_only_lookup_command_execution": execution,
            "local_relevance_medium_read_only_lookup_command_execution_statement": statement,
            "local_relevance_medium_read_only_lookup_command_execution_checks": [
                {
                    "check_name": "synthetic lookup command execution clean",
                    "passed": True,
                    "expected_posture": "clean",
                    "actual_posture": "clean",
                    "block_code": None,
                    "failure_code": None,
                }
            ],
            "local_relevance_medium_read_only_lookup_command_execution_summary": summary,
            "non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
        }

    def write_json(self, path: Path, value: Any) -> Path:
        path.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")
        return path

    def write_synthetic_lookup_command_execution_artifact(
        self,
        directory: Path,
        artifact: Mapping[str, Any] | None = None,
        stem: str = "synthetic",
    ) -> Path:
        path = directory / f"lookup_command_execution_{stem}.json"
        self.assertNotIn("/", path.name)
        self.assertNotIn("\\", path.name)
        value = (
            dict(artifact)
            if artifact is not None
            else self.synthetic_lookup_command_execution_artifact()
        )
        return self.write_json(path, copy.deepcopy(value))

    def build_request(self, artifact_path: Path | str) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_lookup_performed_boundary_v0_min_request(
            selected_lookup_command_execution_artifact=str(artifact_path)
        )

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result[
            "local_relevance_medium_read_only_lookup_performed_boundary_summary"
        ]

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        return result["local_relevance_medium_read_only_lookup_performed_boundary_checks"]

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_lookup_performed_boundary"]

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result[
            "local_relevance_medium_read_only_lookup_performed_boundary_statement"
        ]

    def non_claims(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["non_claims"]

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        summary = result.get(
            "local_relevance_medium_read_only_lookup_performed_boundary_summary"
        )
        if isinstance(summary, Mapping) and isinstance(summary.get("failed_check_count"), int):
            return summary["failed_check_count"]
        return sum(1 for check in self.checks(result) if check.get("passed") is not True)

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
        repo_actual_path = REPO_ROOT / actual_path
        if not actual_path.is_absolute() and repo_actual_path.exists():
            self.assertEqual(repo_actual_path.resolve(), expected_path.resolve())
            return
        if actual_path.exists() or expected_path.exists():
            self.assertEqual(actual_path.resolve(), expected_path.resolve())
            return
        self.assertTrue(str(actual).endswith(expected_path.name))

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = self.non_claims(result)
        self.assertIsInstance(non_claims, Mapping)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIs(type(non_claims[key]), bool)

    def assert_lookup_performed_boundary_non_claims(
        self, result: Mapping[str, Any]
    ) -> None:
        boundary = self.boundary(result)
        for key in BOUNDARY_FALSE_FIELDS:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False, key)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, self.non_claims(result))
            self.assertIs(self.non_claims(result)[key], False, key)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_lookup_performed_boundary_non_claims(result)

    def assert_not_under_forbidden_roots(self, path: Path) -> None:
        for root in FORBIDDEN_OUTPUT_ROOTS:
            self.assertNotEqual(path, root)
            self.assertFalse(path_has_root_parts(path, root), root)

    def assert_boundary_object_separate_from_wrapper(
        self, result: Mapping[str, Any]
    ) -> None:
        boundary = self.boundary(result)
        for key in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(key, boundary)

    def assert_serialized_result_excludes_sentinels(
        self, result: Mapping[str, Any]
    ) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_generated_booleans_are_booleans(
        self, result: Mapping[str, Any]
    ) -> None:
        for section in (self.boundary(result), self.statement(result), self.non_claims(result)):
            for value in section.values():
                if isinstance(value, bool):
                    self.assertIs(type(value), bool)

    def assert_clean_recorded_boundary(
        self, result: Mapping[str, Any], artifact_path: Path | str
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        summary = self.summary(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        for key in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(key, result)
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["boundary_id"],
            "local_relevance_medium_read_only_lookup_performed_boundary_001",
        )
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY",
        )
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_LOOKUP_PERFORMED_CONSIDERATION_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            boundary["basis_lookup_command_execution_artifact"],
            artifact_path,
        )
        self.assertEqual(
            boundary["basis_lookup_command_execution_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_RECORDED",
        )
        self.assertEqual(
            boundary["basis_lookup_command_execution_result_version"], "0.1.0"
        )
        self.assertEqual(
            boundary["basis_lookup_command_execution_failed_check_count"], 0
        )
        self.assertEqual(boundary["selected_command"], "state")
        self.assertIs(boundary["selected_command_is_state"], True)
        self.assertIs(boundary["selected_lookup_command_execution_recorded"], True)
        self.assertIs(boundary["lookup_command_executed"], True)
        self.assertIs(boundary["lookup_command_execution_local_only"], True)
        self.assertIs(boundary["lookup_command_execution_read_only"], True)
        self.assertIs(boundary["future_lookup_performed_may_be_considered"], True)
        self.assert_lookup_performed_boundary_non_claims(result)
        self.assert_boundary_object_separate_from_wrapper(result)
        statement = self.statement(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
        self.assert_canonical_false_non_claims(result)
        self.assert_generated_booleans_are_booleans(result)

    def assert_path_blocks_or_raises(self, path: Path) -> None:
        try:
            result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min_from_path(
                path
            )
        except resolver.LocalRelevanceMediumReadOnlyLookupPerformedBoundaryV0MinError:
            return
        self.assert_blocked_with_public_code(result)

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_lookup_performed_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_lookup_performed_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_lookup_performed_boundary_v0_min_request",
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
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min",
        )
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY",
            resolver.SUPPORTED_BOUNDARY_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_LOOKUP_PERFORMED_CONSIDERATION_ONLY",
            resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        for key in (
            "lookup_performed",
            "lookup_result_created",
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
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        request = resolver.build_declared_local_relevance_medium_read_only_lookup_performed_boundary_v0_min_request()
        self.assertTrue(
            request["selected_lookup_command_execution_artifact"].endswith(
                "local_relevance_medium_read_only_lookup_command_execution_reference_review_001__"
                "local_relevance_medium_read_only_lookup_command_execution_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], "state")
        self.assertIs(request["declared_non_claims"]["consumed_request_reopened"], False)
        self.assertIs(request["declared_non_claims"]["authorization_token_reused"], False)
        self.assert_not_under_forbidden_roots(Path(resolver.OUTPUT_ROOT))

    def test_successful_recorded_result_from_synthetic_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path = self.write_synthetic_lookup_command_execution_artifact(
                Path(tmp)
            )
            result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min(
                self.build_request(artifact_path)
            )
        self.assert_clean_recorded_boundary(result, artifact_path)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_LOOKUP_COMMAND_EXECUTION_ARTIFACT.exists():
            self.skipTest("default lookup command execution artifact not present")
        request = resolver.build_declared_local_relevance_medium_read_only_lookup_performed_boundary_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min(
            request
        )
        self.assert_clean_recorded_boundary(result, DEFAULT_LOOKUP_COMMAND_EXECUTION_ARTIFACT)
        boundary = self.boundary(result)
        self.assert_same_or_stable_artifact_path(
            boundary["basis_lookup_command_execution_artifact"],
            DEFAULT_LOOKUP_COMMAND_EXECUTION_ARTIFACT,
        )
        self.assertIs(boundary["future_lookup_performed_may_be_considered"], True)
        self.assertIs(boundary["lookup_performed"], False)
        self.assertIs(boundary["lookup_result_created"], False)
        self.assertIs(boundary["operation_permission_created"], False)
        self.assertIs(boundary["runtime_permission_created"], False)
        self.assertIs(boundary["public_api_created"], False)
        self.assertIs(boundary["distributed_network_behavior_created"], False)
        self.assertIs(boundary["general_lookup_permission_created"], False)
        self.assertIs(boundary["follow_on_work_authorized"], False)
        self.assertIs(self.statement(result)["predecessor_failure_evidence_preserved"], True)

    def test_closure_token_blocking_behavior(self) -> None:
        cases = (
            (
                "top-level consumed request reopened",
                lambda request: request.__setitem__("consumed_request_reopened", True),
                "CONSUMED_REQUEST_REOPENED",
            ),
            (
                "top-level authorization token reused",
                lambda request: request.__setitem__("authorization_token_reused", True),
                "AUTHORIZATION_TOKEN_REUSED",
            ),
            (
                "declared consumed request reopened true",
                lambda request: request["declared_non_claims"].__setitem__(
                    "consumed_request_reopened", True
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared authorization token reused true",
                lambda request: request["declared_non_claims"].__setitem__(
                    "authorization_token_reused", True
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared consumed request reopened missing",
                lambda request: request["declared_non_claims"].pop(
                    "consumed_request_reopened"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared authorization token reused missing",
                lambda request: request["declared_non_claims"].pop(
                    "authorization_token_reused"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared consumed request reopened string false",
                lambda request: request["declared_non_claims"].__setitem__(
                    "consumed_request_reopened", "false"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared authorization token reused string false",
                lambda request: request["declared_non_claims"].__setitem__(
                    "authorization_token_reused", "false"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared consumed request reopened none",
                lambda request: request["declared_non_claims"].__setitem__(
                    "consumed_request_reopened", None
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared authorization token reused none",
                lambda request: request["declared_non_claims"].__setitem__(
                    "authorization_token_reused", None
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path = self.write_synthetic_lookup_command_execution_artifact(
                Path(tmp)
            )
            for name, mutate, expected_code in cases:
                with self.subTest(name=name):
                    request = self.build_request(artifact_path)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_critical_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path = self.write_synthetic_lookup_command_execution_artifact(
                Path(tmp)
            )
            clean_request = self.build_request(artifact_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(self.non_claims(result)[key], False)
                    self.assert_canonical_false_non_claims(result)
                    self.assert_lookup_performed_boundary_non_claims(result)

    def test_representative_blocking_behavior_uses_safe_filenames(self) -> None:
        def set_summary(artifact: dict[str, Any], key: str, value: Any) -> None:
            artifact[
                "local_relevance_medium_read_only_lookup_command_execution_summary"
            ][key] = value

        def set_execution(artifact: dict[str, Any], key: str, value: Any) -> None:
            artifact["local_relevance_medium_read_only_lookup_command_execution"][key] = value
            artifact[
                "local_relevance_medium_read_only_lookup_command_execution_statement"
            ][key] = value
            set_summary(artifact, key, value)

        cases: list[
            tuple[
                str,
                Callable[[dict[str, Any]], None] | None,
                Callable[[dict[str, Any]], None] | None,
                str | None,
            ]
        ] = [
            ("explicit block intent", None, lambda r: r.__setitem__("local_relevance_medium_read_only_lookup_performed_boundary_intent", "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY"), None),
            ("missing request", None, None, "missing_request"),
            ("non-mapping request", None, None, "non_mapping"),
            ("unsupported intent", None, lambda r: r.__setitem__("local_relevance_medium_read_only_lookup_performed_boundary_intent", "UNSUPPORTED_INTENT"), None),
            ("lookup command execution artifact path missing", None, lambda r: r.pop("selected_lookup_command_execution_artifact"), None),
            ("lookup command execution artifact unreadable", None, lambda r: r.__setitem__("selected_lookup_command_execution_artifact", str(Path(r["_tmpdir"]) / "missing_lookup_command_execution.json")), None),
            ("lookup command execution artifact JSON array instead of object", None, None, "artifact_array"),
            ("lookup command execution artifact not recorded", lambda a: (a.__setitem__("outcome", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_NOT_RECORDED"), set_summary(a, "outcome", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_NOT_RECORDED")), None, None),
            ("lookup command execution artifact failed checks present", lambda a: set_summary(a, "failed_check_count", 1), None, None),
            ("lookup command execution artifact version not 0.1.0", lambda a: (a.__setitem__("result_version", "9.9.9"), set_summary(a, "result_version", "9.9.9")), None, None),
            ("selected command missing", None, lambda r: r.pop("selected_command"), None),
            ("selected command not state", None, lambda r: r.__setitem__("selected_command", "lookup first_orientation_locator"), None),
            ("selected lookup command execution not recorded", lambda a: set_execution(a, "local_relevance_medium_read_only_lookup_command_execution_recorded", False), None, None),
            ("lookup command not executed", lambda a: set_execution(a, "lookup_command_executed", False), None, None),
            ("lookup command execution local only not true", lambda a: set_execution(a, "lookup_command_execution_local_only", False), None, None),
            ("lookup command execution read only not true", lambda a: set_execution(a, "lookup_command_execution_read_only", False), None, None),
            ("future lookup performed may not be considered", None, lambda r: r.__setitem__("future_lookup_performed_may_be_considered", False), None),
            ("boundary type missing", None, lambda r: r.pop("boundary_type"), None),
            ("boundary type not LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY", None, lambda r: r.__setitem__("boundary_type", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED"), None),
            ("boundary scope missing", None, lambda r: r.pop("boundary_scope"), None),
            ("boundary scope not SELECTED_LOOKUP_PERFORMED_CONSIDERATION_ONLY", None, lambda r: r.__setitem__("boundary_scope", "SELECTED_LOOKUP_PERFORMED_ONLY"), None),
            ("predecessor failure evidence hidden/repaired/claimed passed", None, lambda r: r.__setitem__("predecessor_failure_hidden", True), None),
            ("required non-claim missing or flipped", None, lambda r: r["declared_non_claims"].__setitem__("lookup_performed", True), None),
        ]
        for field in (
            "lookup_performed",
            "lookup_result_created",
            "operation_permission_created",
            "runtime_permission_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
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
            "consumed_request_reopened",
            "authorization_token_reused",
            "artifact_existence_treated_as_lookup_performed_boundary_authority",
            "latest_file_posture_treated_as_lookup_performed_boundary_authority",
            "repo_local_availability_treated_as_lookup_performed_boundary_authority",
            "hidden_repo_state_used_as_lookup_performed_boundary_content",
            "hidden_repo_state_used_as_lookup_performed_boundary_authority",
        ):
            cases.append(
                (
                    field.replace("_", " "),
                    None,
                    lambda request, name=field: request.__setitem__(name, True),
                    None,
                )
            )
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            for index, (name, artifact_mutator, request_mutator, direct) in enumerate(cases):
                with self.subTest(name=name):
                    filename = self.safe_json_filename(name, index=index)
                    if direct == "missing_request":
                        result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min(
                            {}
                        )
                    elif direct == "non_mapping":
                        result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min(
                            ["not", "a", "mapping"]  # type: ignore[arg-type]
                        )
                    else:
                        artifact = self.synthetic_lookup_command_execution_artifact()
                        if artifact_mutator is not None:
                            artifact_mutator(artifact)
                        artifact_path = tmp_path / f"lookup_command_execution_{filename}"
                        if direct == "artifact_array":
                            artifact_path.write_text("[]", encoding="utf-8")
                        else:
                            self.write_json(artifact_path, artifact)
                        request = self.build_request(artifact_path)
                        request["_tmpdir"] = str(tmp_path)
                        if request_mutator is not None:
                            request_mutator(request)
                        request.pop("_tmpdir", None)
                        result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min(
                            request
                        )
                    self.assert_blocked_with_public_code(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path = self.write_synthetic_lookup_command_execution_artifact(
                Path(tmp)
            )
            result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min(
                self.build_request(artifact_path)
            )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY",
        )
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_LOOKUP_PERFORMED_CONSIDERATION_ONLY",
        )
        self.assertEqual(boundary["selected_command"], "state")
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_BOUNDARY_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for value in OFFICIAL_VALUES:
            self.assertIn(value, serialized)
        self.assertNotIn("[REDACTED_SENSITIVE_BODY]", boundary.values())
        self.assertNotIn("[REDACTED_HOSTILE_SENTINEL]", serialized)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact = self.synthetic_lookup_command_execution_artifact()
            artifact["raw_lookup_command_execution_body"] = (
                "RAW_LOOKUP_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN"
            )
            artifact["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
            artifact_path = self.write_synthetic_lookup_command_execution_artifact(
                Path(tmp),
                artifact,
                stem="hostile",
            )
            request = self.build_request(artifact_path)
            request["raw_lookup_performed_boundary_body"] = (
                "RAW_LOOKUP_PERFORMED_BOUNDARY_BODY_MUST_NOT_RETURN"
            )
            request["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
            original_request = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min(
                request
            )
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_serialized_result_excludes_sentinels(result)
        serialized = json.dumps(result, sort_keys=True)
        for value in OFFICIAL_VALUES:
            self.assertIn(value, serialized)
        self.assert_canonical_false_non_claims(result)
        self.assert_lookup_performed_boundary_non_claims(result)
        self.assertEqual(request, original_request)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact_path = self.write_synthetic_lookup_command_execution_artifact(
                tmp_path
            )
            request_path = tmp_path / "request.json"
            self.write_json(request_path, self.build_request(artifact_path))
            result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.summary(result)["result_version"], "0.1.0")
            self.assertEqual(
                self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE
            )
            self.assert_not_blocked(result)
            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            self.assert_path_blocks_or_raises(malformed_path)
            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_path_blocks_or_raises(array_path)
            self.assert_path_blocks_or_raises(tmp_path / "missing_request.json")
            output_root = tmp_path / "artifacts" / EXPECTED_OUTPUT_ROOT.name
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_local_relevance_medium_read_only_lookup_performed_boundary_v0_min_result(
                    result
                )
                second = resolver.write_local_relevance_medium_read_only_lookup_performed_boundary_v0_min_result(
                    result
                )
            self.assertTrue(first.parent.exists())
            self.assertTrue(second.parent.exists())
            self.assertNotEqual(first, second)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertIsInstance(json.loads(first.read_text(encoding="utf-8")), dict)
            self.assertIsInstance(json.loads(second.read_text(encoding="utf-8")), dict)
            self.assertIn(
                "local_relevance_medium_read_only_lookup_performed_boundary_v0_min",
                str(first),
            )
            self.assert_not_under_forbidden_roots(first)
            self.assert_not_under_forbidden_roots(second)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact = self.synthetic_lookup_command_execution_artifact()
            artifact["nested_raw_payload"] = {
                "raw_lookup_command_execution_body": (
                    "RAW_LOOKUP_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN"
                )
            }
            artifact_before = copy.deepcopy(artifact)
            artifact_path = self.write_synthetic_lookup_command_execution_artifact(
                Path(tmp), artifact
            )
            request = self.build_request(artifact_path)
            request["posture_mapping"] = {"lookup_performed": False}
            request["closure_token_fields"] = {
                "consumed_request_reopened": False,
                "authorization_token_reused": False,
            }
            request_before = copy.deepcopy(request)
            declared_non_claims_before = copy.deepcopy(request["declared_non_claims"])
            selected_path_before = request["selected_lookup_command_execution_artifact"]
            selected_command_before = request["selected_command"]
            boundary_type_before = request["boundary_type"]
            boundary_scope_before = request["boundary_scope"]
            result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min(
                request
            )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, request_before)
        self.assertEqual(request["declared_non_claims"], declared_non_claims_before)
        self.assertEqual(
            request["selected_lookup_command_execution_artifact"], selected_path_before
        )
        self.assertEqual(request["selected_command"], selected_command_before)
        self.assertEqual(request["boundary_type"], boundary_type_before)
        self.assertEqual(request["boundary_scope"], boundary_scope_before)
        self.assertEqual(artifact, artifact_before)

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path = self.write_synthetic_lookup_command_execution_artifact(
                Path(tmp)
            )
            result = resolver.resolve_local_relevance_medium_read_only_lookup_performed_boundary_v0_min(
                self.build_request(artifact_path)
            )
        statement = self.statement(result)
        summary = self.summary(result)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(statement["result_level_non_claims_canonical_false"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)
        non_claims = self.non_claims(result)
        self.assertIs(non_claims["predecessor_failure_repaired"], False)
        self.assertIs(non_claims["predecessor_failure_hidden"], False)
        self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
