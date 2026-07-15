"""Tests for the local read-only lookup command execution resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION object. It verifies
that the resolver reads one clean lookup command execution boundary artifact and
one clean selected raw/full state packet body exposure artifact, then records
one local read-only selected-state lookup-command-execution event.

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

import resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min as resolver  # noqa: E402


DEFAULT_LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_command_execution_boundary_v0_min/"
    "local_relevance_medium_read_only_lookup_command_execution_boundary_"
    "reference_review_001__local_relevance_medium_read_only_lookup_command_"
    "execution_boundary_v0_min_result.json"
)
DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "raw_full_state_packet_body_exposure_v0_min/"
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_"
    "reference_review_001__local_relevance_medium_read_only_raw_full_state_packet_"
    "body_exposure_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_command_execution_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    "local_relevance_medium_read_only_lookup_command_execution_metadata",
    "declared_local_relevance_medium_read_only_lookup_command_execution_question",
    "selected_lookup_command_execution_boundary_artifact_basis",
    "selected_raw_full_state_packet_body_exposure_artifact_basis",
    "local_relevance_medium_read_only_lookup_command_execution",
    "local_relevance_medium_read_only_lookup_command_execution_checks",
    "local_relevance_medium_read_only_lookup_command_execution_statement",
    "local_relevance_medium_read_only_lookup_command_execution_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_lookup_command_execution_summary",
)

FORBIDDEN_EXECUTION_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_lookup_command_execution_checks",
    "non_claims",
    "local_relevance_medium_read_only_lookup_command_execution_summary",
    "local_relevance_medium_read_only_lookup_command_execution_metadata",
)

EXECUTION_FALSE_FIELDS = (
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

BOUNDARY_ARTIFACT_FALSE_FIELDS = (
    "lookup_command_executed",
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

RAW_FULL_ARTIFACT_FALSE_FIELDS = (
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
    "consumed_request_reopened",
    "authorization_token_reused",
    "follow_on_work_authorized",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_COMMAND_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
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


def path_has_root_parts(path: Path, root: Path) -> bool:
    path_parts = path.parts
    root_parts = root.parts
    if len(path_parts) < len(root_parts):
        return False
    return any(
        path_parts[index : index + len(root_parts)] == root_parts
        for index in range(len(path_parts) - len(root_parts) + 1)
    )


class LookupCommandExecutionResolverTests(unittest.TestCase):
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

    def synthetic_lookup_command_execution_boundary_artifact(self) -> dict[str, Any]:
        boundary: dict[str, Any] = {
            "boundary_id": (
                "local_relevance_medium_read_only_lookup_command_execution_boundary_001"
            ),
            "boundary_type": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BOUNDARY"
            ),
            "boundary_version": "0.1.0",
            "boundary_scope": "SELECTED_LOOKUP_COMMAND_EXECUTION_CONSIDERATION_ONLY",
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
            "future_lookup_command_execution_may_be_considered": True,
        }
        for key in BOUNDARY_ARTIFACT_FALSE_FIELDS:
            boundary[key] = False
        statement = {
            "local_relevance_medium_read_only_lookup_command_execution_boundary_recorded": True,
            "basis_raw_full_state_packet_body_exposure_artifact_preserved": True,
            "selected_command": "state",
            "selected_command_preserved": True,
            "selected_command_is_state": True,
            "selected_raw_full_state_packet_body_exposure_recorded": True,
            "raw_full_state_packet_body_exposed": True,
            "raw_full_state_packet_body_exposure_local_only": True,
            "raw_full_state_packet_body_exposure_read_only": True,
            "future_lookup_command_execution_may_be_considered": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        summary = {
            "outcome": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BOUNDARY_RECORDED"
            ),
            "failed_check_count": 0,
            "passed_check_count": 82,
            "result_version": "0.1.0",
            "resolver_module": (
                "resolve_local_relevance_medium_read_only_lookup_command_execution_boundary_v0_min"
            ),
            "selected_command": "state",
            "selected_command_is_state": True,
            "selected_raw_full_state_packet_body_exposure_recorded": True,
            "raw_full_state_packet_body_exposed": True,
            "raw_full_state_packet_body_exposure_local_only": True,
            "raw_full_state_packet_body_exposure_read_only": True,
            "future_lookup_command_execution_may_be_considered": True,
        }
        return {
            "outcome": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BOUNDARY_RECORDED"
            ),
            "result_version": "0.1.0",
            "local_relevance_medium_read_only_lookup_command_execution_boundary_metadata": {
                "local_relevance_medium_read_only_lookup_command_execution_boundary_version": "0.1.0",
                "result_version": "0.1.0",
                "resolver_module": (
                    "resolve_local_relevance_medium_read_only_lookup_command_execution_boundary_v0_min"
                ),
            },
            "local_relevance_medium_read_only_lookup_command_execution_boundary": boundary,
            "local_relevance_medium_read_only_lookup_command_execution_boundary_statement": statement,
            "local_relevance_medium_read_only_lookup_command_execution_boundary_checks": [
                {
                    "check_name": "synthetic lookup command execution boundary clean",
                    "passed": True,
                    "expected_posture": "clean",
                    "actual_posture": "clean",
                    "block_code": None,
                    "failure_code": None,
                }
            ],
            "local_relevance_medium_read_only_lookup_command_execution_boundary_summary": summary,
            "non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
        }

    def synthetic_raw_full_state_packet_body_exposure_artifact(self) -> dict[str, Any]:
        exposure: dict[str, Any] = {
            "raw_full_state_packet_body_exposure_id": (
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_001"
            ),
            "raw_full_state_packet_body_exposure_type": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE"
            ),
            "raw_full_state_packet_body_exposure_version": "0.1.0",
            "raw_full_state_packet_body_exposure_scope": (
                "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY"
            ),
            "basis_raw_full_state_packet_body_exposure_boundary_artifact": (
                "synthetic_raw_full_state_packet_body_exposure_boundary.json"
            ),
            "basis_raw_full_state_packet_body_exposure_boundary_outcome": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED"
            ),
            "basis_raw_full_state_packet_body_exposure_boundary_result_version": "0.1.0",
            "basis_raw_full_state_packet_body_exposure_boundary_failed_check_count": 0,
            "basis_state_packet_body_exposure_artifact": (
                "synthetic_state_packet_body_exposure.json"
            ),
            "basis_state_packet_body_exposure_outcome": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_RECORDED"
            ),
            "basis_state_packet_body_exposure_result_version": "0.1.0",
            "basis_state_packet_body_exposure_failed_check_count": 0,
            "selected_command": "state",
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded": True,
            "selected_raw_full_state_packet_body_exposure_recorded": True,
            "selected_state_packet_body_exposure_recorded": True,
            "raw_full_state_packet_body_exposed": True,
            "raw_full_state_packet_body_exposure_local_only": True,
            "raw_full_state_packet_body_exposure_read_only": True,
            "state_packet_body_exposed": True,
            "state_packet_body_exposure_local_only": True,
            "state_packet_body_exposure_read_only": True,
        }
        for key in RAW_FULL_ARTIFACT_FALSE_FIELDS:
            exposure[key] = False
        statement = {
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded": True,
            "selected_raw_full_state_packet_body_exposure_recorded": True,
            "selected_command": "state",
            "selected_command_preserved": True,
            "selected_command_is_state": True,
            "raw_full_state_packet_body_exposed": True,
            "raw_full_state_packet_body_exposure_local_only": True,
            "raw_full_state_packet_body_exposure_read_only": True,
            "state_packet_body_exposed": True,
            "state_packet_body_exposure_local_only": True,
            "state_packet_body_exposure_read_only": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        summary = {
            "outcome": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_RECORDED"
            ),
            "failed_check_count": 0,
            "passed_check_count": 89,
            "result_version": "0.1.0",
            "resolver_module": (
                "resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min"
            ),
            "selected_command": "state",
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded": True,
            "selected_raw_full_state_packet_body_exposure_recorded": True,
            "raw_full_state_packet_body_exposed": True,
            "raw_full_state_packet_body_exposure_local_only": True,
            "raw_full_state_packet_body_exposure_read_only": True,
            "state_packet_body_exposed": True,
            "state_packet_body_exposure_local_only": True,
            "state_packet_body_exposure_read_only": True,
        }
        return {
            "outcome": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_RECORDED"
            ),
            "result_version": "0.1.0",
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_metadata": {
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_version": "0.1.0",
                "result_version": "0.1.0",
                "resolver_module": (
                    "resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min"
                ),
            },
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure": exposure,
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_statement": statement,
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_checks": [
                {
                    "check_name": "synthetic raw/full exposure clean",
                    "passed": True,
                    "expected_posture": "clean",
                    "actual_posture": "clean",
                    "block_code": None,
                    "failure_code": None,
                }
            ],
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_summary": summary,
            "non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
        }

    def write_json(self, path: Path, value: Any) -> Path:
        path.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")
        return path

    def write_synthetic_basis_artifacts(
        self,
        directory: Path,
        boundary: Mapping[str, Any] | None = None,
        raw_full: Mapping[str, Any] | None = None,
        stem: str = "synthetic",
    ) -> tuple[Path, Path]:
        boundary_path = directory / f"boundary_{stem}.json"
        raw_full_path = directory / f"raw_full_{stem}.json"
        self.assertNotIn("/", boundary_path.name)
        self.assertNotIn("\\", boundary_path.name)
        self.assertNotIn("/", raw_full_path.name)
        self.assertNotIn("\\", raw_full_path.name)
        self.write_json(
            boundary_path,
            copy.deepcopy(
                dict(boundary)
                if boundary is not None
                else self.synthetic_lookup_command_execution_boundary_artifact()
            ),
        )
        self.write_json(
            raw_full_path,
            copy.deepcopy(
                dict(raw_full)
                if raw_full is not None
                else self.synthetic_raw_full_state_packet_body_exposure_artifact()
            ),
        )
        return boundary_path, raw_full_path

    def build_request(
        self, boundary_path: Path | str, raw_full_path: Path | str
    ) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_lookup_command_execution_v0_min_request(
            selected_lookup_command_execution_boundary_artifact=str(boundary_path),
            selected_raw_full_state_packet_body_exposure_artifact=str(raw_full_path),
        )

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_lookup_command_execution_summary"]

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        return result["local_relevance_medium_read_only_lookup_command_execution_checks"]

    def execution(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_lookup_command_execution"]

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["local_relevance_medium_read_only_lookup_command_execution_statement"]

    def non_claims(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        return result["non_claims"]

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        summary = result.get("local_relevance_medium_read_only_lookup_command_execution_summary")
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

    def assert_lookup_command_execution_non_claims(
        self, result: Mapping[str, Any]
    ) -> None:
        execution = self.execution(result)
        for key in EXECUTION_FALSE_FIELDS:
            self.assertIn(key, execution)
            self.assertIs(execution[key], False, key)
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
        self.assert_lookup_command_execution_non_claims(result)

    def assert_not_under_forbidden_roots(self, path: Path) -> None:
        for root in FORBIDDEN_OUTPUT_ROOTS:
            self.assertNotEqual(path, root)
            self.assertFalse(path_has_root_parts(path, root), root)

    def assert_execution_object_separate_from_wrapper(
        self, result: Mapping[str, Any]
    ) -> None:
        execution = self.execution(result)
        for key in FORBIDDEN_EXECUTION_WRAPPER_FIELDS:
            self.assertNotIn(key, execution)

    def assert_serialized_result_excludes_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_clean_recorded_execution(
        self, result: Mapping[str, Any], boundary_path: Path | str, raw_full_path: Path | str
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
        execution = self.execution(result)
        self.assertEqual(
            execution["lookup_command_execution_id"],
            "local_relevance_medium_read_only_lookup_command_execution_001",
        )
        self.assertEqual(
            execution["lookup_command_execution_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION",
        )
        self.assertEqual(execution["lookup_command_execution_version"], "0.1.0")
        self.assertEqual(
            execution["lookup_command_execution_scope"],
            "SELECTED_LOOKUP_COMMAND_EXECUTION_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            execution["basis_lookup_command_execution_boundary_artifact"],
            boundary_path,
        )
        self.assertEqual(
            execution["basis_lookup_command_execution_boundary_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            execution["basis_lookup_command_execution_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            execution["basis_lookup_command_execution_boundary_failed_check_count"],
            0,
        )
        self.assert_same_or_stable_artifact_path(
            execution["basis_raw_full_state_packet_body_exposure_artifact"],
            raw_full_path,
        )
        self.assertEqual(
            execution["basis_raw_full_state_packet_body_exposure_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_RECORDED",
        )
        self.assertEqual(
            execution["basis_raw_full_state_packet_body_exposure_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            execution["basis_raw_full_state_packet_body_exposure_failed_check_count"],
            0,
        )
        self.assertEqual(execution["selected_command"], "state")
        self.assertIs(execution["selected_command_is_state"], True)
        self.assertIs(
            execution["selected_raw_full_state_packet_body_exposure_recorded"], True
        )
        self.assertIs(execution["raw_full_state_packet_body_exposed"], True)
        self.assertIs(execution["raw_full_state_packet_body_exposure_local_only"], True)
        self.assertIs(execution["raw_full_state_packet_body_exposure_read_only"], True)
        self.assertIs(
            execution["local_relevance_medium_read_only_lookup_command_execution_recorded"],
            True,
        )
        self.assertIs(execution["lookup_command_executed"], True)
        self.assertIs(execution["lookup_command_execution_local_only"], True)
        self.assertIs(execution["lookup_command_execution_read_only"], True)
        self.assert_lookup_command_execution_non_claims(result)
        self.assert_execution_object_separate_from_wrapper(result)
        statement = self.statement(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
        self.assert_canonical_false_non_claims(result)

    def assert_path_blocks_or_raises(self, path: Path) -> None:
        try:
            result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min_from_path(
                path
            )
        except resolver.LocalRelevanceMediumReadOnlyLookupCommandExecutionV0MinError:
            return
        self.assert_blocked_with_public_code(result)

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min",
            "resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min_from_path",
            "write_local_relevance_medium_read_only_lookup_command_execution_v0_min_result",
            "build_local_relevance_medium_read_only_lookup_command_execution_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_lookup_command_execution_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_LOOKUP_COMMAND_EXECUTION_TYPE_VALUES",
            "SUPPORTED_LOOKUP_COMMAND_EXECUTION_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min",
        )
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION",
            resolver.SUPPORTED_LOOKUP_COMMAND_EXECUTION_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_LOOKUP_COMMAND_EXECUTION_ONLY",
            resolver.SUPPORTED_LOOKUP_COMMAND_EXECUTION_SCOPE_VALUES,
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
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        request = resolver.build_declared_local_relevance_medium_read_only_lookup_command_execution_v0_min_request()
        self.assertTrue(
            request["selected_lookup_command_execution_boundary_artifact"].endswith(
                "local_relevance_medium_read_only_lookup_command_execution_boundary_reference_review_001__"
                "local_relevance_medium_read_only_lookup_command_execution_boundary_v0_min_result.json"
            )
        )
        self.assertTrue(
            request["selected_raw_full_state_packet_body_exposure_artifact"].endswith(
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_reference_review_001__"
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], "state")
        self.assertIs(request["declared_non_claims"]["consumed_request_reopened"], False)
        self.assertIs(request["declared_non_claims"]["authorization_token_reused"], False)
        self.assert_not_under_forbidden_roots(Path(resolver.OUTPUT_ROOT))

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, raw_full_path = self.write_synthetic_basis_artifacts(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
                self.build_request(boundary_path, raw_full_path)
            )
        self.assert_clean_recorded_execution(result, boundary_path, raw_full_path)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT.exists():
            self.skipTest("default lookup command execution boundary artifact not present")
        if not DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT.exists():
            self.skipTest("default raw/full state packet body exposure artifact not present")
        request = resolver.build_declared_local_relevance_medium_read_only_lookup_command_execution_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
            request
        )
        self.assert_clean_recorded_execution(
            result,
            DEFAULT_LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT,
            DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT,
        )
        execution = self.execution(result)
        self.assert_same_or_stable_artifact_path(
            execution["basis_lookup_command_execution_boundary_artifact"],
            DEFAULT_LOOKUP_COMMAND_EXECUTION_BOUNDARY_ARTIFACT,
        )
        self.assert_same_or_stable_artifact_path(
            execution["basis_raw_full_state_packet_body_exposure_artifact"],
            DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ARTIFACT,
        )
        self.assertIs(execution["lookup_command_executed"], True)
        self.assertIs(execution["lookup_performed"], False)
        self.assertIs(execution["lookup_result_created"], False)
        self.assertIs(execution["operation_permission_created"], False)
        self.assertIs(execution["runtime_permission_created"], False)
        self.assertIs(execution["public_api_created"], False)
        self.assertIs(execution["distributed_network_behavior_created"], False)
        self.assertIs(execution["general_lookup_permission_created"], False)
        self.assertIs(execution["follow_on_work_authorized"], False)

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
            boundary_path, raw_full_path = self.write_synthetic_basis_artifacts(Path(tmp))
            for name, mutate, expected_code in cases:
                with self.subTest(name=name):
                    request = self.build_request(boundary_path, raw_full_path)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_critical_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, raw_full_path = self.write_synthetic_basis_artifacts(Path(tmp))
            clean_request = self.build_request(boundary_path, raw_full_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(self.non_claims(result)[key], False)
                    self.assert_canonical_false_non_claims(result)
                    self.assert_lookup_command_execution_non_claims(result)

    def test_representative_blocking_behavior_uses_safe_filenames(self) -> None:
        def set_boundary_summary(artifact: dict[str, Any], key: str, value: Any) -> None:
            artifact[
                "local_relevance_medium_read_only_lookup_command_execution_boundary_summary"
            ][key] = value

        def set_boundary_object(artifact: dict[str, Any], key: str, value: Any) -> None:
            artifact[
                "local_relevance_medium_read_only_lookup_command_execution_boundary"
            ][key] = value
            artifact[
                "local_relevance_medium_read_only_lookup_command_execution_boundary_statement"
            ][key] = value
            set_boundary_summary(artifact, key, value)

        def set_raw_summary(artifact: dict[str, Any], key: str, value: Any) -> None:
            artifact[
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_summary"
            ][key] = value

        def set_raw_exposure(artifact: dict[str, Any], key: str, value: Any) -> None:
            artifact[
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure"
            ][key] = value
            artifact[
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_statement"
            ][key] = value
            set_raw_summary(artifact, key, value)

        cases: tuple[
            tuple[
                str,
                Callable[[dict[str, Any]], None] | None,
                Callable[[dict[str, Any]], None] | None,
                Callable[[dict[str, Any]], None] | None,
                str | None,
            ],
            ...,
        ] = (
            ("explicit block intent", None, None, lambda r: r.__setitem__("local_relevance_medium_read_only_lookup_command_execution_intent", "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION"), None),
            ("missing request", None, None, None, "missing_request"),
            ("non-mapping request", None, None, None, "non_mapping"),
            ("unsupported intent", None, None, lambda r: r.__setitem__("local_relevance_medium_read_only_lookup_command_execution_intent", "UNSUPPORTED_INTENT"), None),
            ("lookup command execution boundary artifact path missing", None, None, lambda r: r.pop("selected_lookup_command_execution_boundary_artifact"), None),
            ("lookup command execution boundary artifact unreadable", None, None, lambda r: r.__setitem__("selected_lookup_command_execution_boundary_artifact", str(Path(r["_tmpdir"]) / "missing_boundary.json")), None),
            ("lookup command execution boundary artifact JSON array", None, None, None, "boundary_array"),
            ("lookup command execution boundary artifact not recorded", lambda a: (a.__setitem__("outcome", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED"), set_boundary_summary(a, "outcome", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED")), None, None, None),
            ("lookup command execution boundary artifact failed checks present", lambda a: set_boundary_summary(a, "failed_check_count", 1), None, None, None),
            ("lookup command execution boundary artifact version not 0.1.0", lambda a: set_boundary_summary(a, "result_version", "9.9.9"), None, None, None),
            ("raw/full state packet body exposure artifact path missing", None, None, lambda r: r.pop("selected_raw_full_state_packet_body_exposure_artifact"), None),
            ("raw/full state packet body exposure artifact unreadable", None, None, lambda r: r.__setitem__("selected_raw_full_state_packet_body_exposure_artifact", str(Path(r["_tmpdir"]) / "missing_raw_full.json")), None),
            ("raw/full state packet body exposure artifact JSON array", None, None, None, "raw_array"),
            ("raw/full state packet body exposure artifact not recorded", None, lambda a: (a.__setitem__("outcome", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED"), set_raw_summary(a, "outcome", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED")), None, None),
            ("raw/full state packet body exposure artifact failed checks present", None, lambda a: set_raw_summary(a, "failed_check_count", 1), None, None),
            ("raw/full state packet body exposure artifact version not 0.1.0", None, lambda a: set_raw_summary(a, "result_version", "9.9.9"), None, None),
            ("selected command missing", None, None, lambda r: r.pop("selected_command"), None),
            ("selected command not state", None, None, lambda r: r.__setitem__("selected_command", "lookup first_orientation_locator"), None),
            ("selected raw/full state packet body exposure not recorded", lambda a: set_boundary_object(a, "selected_raw_full_state_packet_body_exposure_recorded", False), lambda a: set_raw_exposure(a, "selected_raw_full_state_packet_body_exposure_recorded", False), None, None),
            ("raw/full state packet body not exposed", lambda a: set_boundary_object(a, "raw_full_state_packet_body_exposed", False), lambda a: set_raw_exposure(a, "raw_full_state_packet_body_exposed", False), None, None),
            ("raw/full state packet body exposure local only not true", lambda a: set_boundary_object(a, "raw_full_state_packet_body_exposure_local_only", False), lambda a: set_raw_exposure(a, "raw_full_state_packet_body_exposure_local_only", False), None, None),
            ("raw/full state packet body exposure read only not true", lambda a: set_boundary_object(a, "raw_full_state_packet_body_exposure_read_only", False), lambda a: set_raw_exposure(a, "raw_full_state_packet_body_exposure_read_only", False), None, None),
            ("lookup command execution type missing", None, None, lambda r: r.pop("lookup_command_execution_type"), None),
            ("lookup command execution type unsupported", None, None, lambda r: r.__setitem__("lookup_command_execution_type", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED"), None),
            ("lookup command execution scope missing", None, None, lambda r: r.pop("lookup_command_execution_scope"), None),
            ("lookup command execution scope unsupported", None, None, lambda r: r.__setitem__("lookup_command_execution_scope", "SELECTED_LOOKUP_PERFORMED_ONLY"), None),
            ("local relevance medium read-only lookup command execution not recorded", None, None, lambda r: r.__setitem__("local_relevance_medium_read_only_lookup_command_execution_not_recorded", True), None),
            ("lookup command not executed", None, None, lambda r: r.__setitem__("lookup_command_not_executed", True), None),
            ("lookup command execution local only not true", None, None, lambda r: r.__setitem__("lookup_command_execution_local_only_not_true", True), None),
            ("lookup command execution read only not true", None, None, lambda r: r.__setitem__("lookup_command_execution_read_only_not_true", True), None),
            ("lookup performed", None, None, lambda r: r.__setitem__("lookup_performed", True), None),
            ("lookup result created", None, None, lambda r: r.__setitem__("lookup_result_created", True), None),
            ("operation permission created", None, None, lambda r: r.__setitem__("operation_permission_created", True), None),
            ("runtime permission created", None, None, lambda r: r.__setitem__("runtime_permission_created", True), None),
            ("public API created", None, None, lambda r: r.__setitem__("public_api_created", True), None),
            ("participant-facing interface created", None, None, lambda r: r.__setitem__("participant_facing_interface_created", True), None),
            ("distributed network behavior created", None, None, lambda r: r.__setitem__("distributed_network_behavior_created", True), None),
            ("general lookup permission created", None, None, lambda r: r.__setitem__("general_lookup_permission_created", True), None),
            ("arbitrary lookup permission created", None, None, lambda r: r.__setitem__("arbitrary_lookup_permission_created", True), None),
            ("unsupported commands permitted", None, None, lambda r: r.__setitem__("unsupported_commands_permitted", True), None),
            ("unsupported lookup keys permitted", None, None, lambda r: r.__setitem__("unsupported_lookup_keys_permitted", True), None),
            ("new lookup entry created", None, None, lambda r: r.__setitem__("new_lookup_entry_created", True), None),
            ("new signal accepted", None, None, lambda r: r.__setitem__("new_signal_accepted", True), None),
            ("new entry accepted", None, None, lambda r: r.__setitem__("new_entry_accepted", True), None),
            ("new relevance object created", None, None, lambda r: r.__setitem__("new_relevance_object_created", True), None),
            ("new index entry created", None, None, lambda r: r.__setitem__("new_index_entry_created", True), None),
            ("filesystem discovery performed", None, None, lambda r: r.__setitem__("filesystem_discovery_performed", True), None),
            ("registry created", None, None, lambda r: r.__setitem__("registry_created", True), None),
            ("search surface created", None, None, lambda r: r.__setitem__("search_surface_created", True), None),
            ("query surface created", None, None, lambda r: r.__setitem__("query_surface_created", True), None),
            ("ranking surface created", None, None, lambda r: r.__setitem__("ranking_surface_created", True), None),
            ("scoring surface created", None, None, lambda r: r.__setitem__("scoring_surface_created", True), None),
            ("priority surface created", None, None, lambda r: r.__setitem__("priority_surface_created", True), None),
            ("validity judgment created", None, None, lambda r: r.__setitem__("validity_judgment_created", True), None),
            ("truth judgment created", None, None, lambda r: r.__setitem__("truth_judgment_created", True), None),
            ("authority judgment created", None, None, lambda r: r.__setitem__("authority_judgment_created", True), None),
            ("currentness judgment created", None, None, lambda r: r.__setitem__("currentness_judgment_created", True), None),
            ("repeated reception permission created", None, None, lambda r: r.__setitem__("repeated_reception_permission_created", True), None),
            ("arbitrary reception created", None, None, lambda r: r.__setitem__("arbitrary_reception_created", True), None),
            ("feed created", None, None, lambda r: r.__setitem__("feed_created", True), None),
            ("source transfer occurred", None, None, lambda r: r.__setitem__("source_transfer_occurred", True), None),
            ("source receipt occurred", None, None, lambda r: r.__setitem__("source_receipt_occurred", True), None),
            ("source created", None, None, lambda r: r.__setitem__("source_created", True), None),
            ("authority created", None, None, lambda r: r.__setitem__("authority_created", True), None),
            ("currentness created", None, None, lambda r: r.__setitem__("currentness_created", True), None),
            ("truth created", None, None, lambda r: r.__setitem__("truth_created", True), None),
            ("synchronization created", None, None, lambda r: r.__setitem__("synchronization_created", True), None),
            ("participation authorized", None, None, lambda r: r.__setitem__("participation_authorized", True), None),
            ("participant role created", None, None, lambda r: r.__setitem__("participant_role_created", True), None),
            ("deployment created", None, None, lambda r: r.__setitem__("deployment_created", True), None),
            ("public release created", None, None, lambda r: r.__setitem__("public_release_created", True), None),
            ("broader reusable permission created", None, None, lambda r: r.__setitem__("broader_reusable_permission_created", True), None),
            ("follow-on work authorized", None, None, lambda r: r.__setitem__("follow_on_work_authorized", True), None),
            ("consumed request reopened", None, None, lambda r: r.__setitem__("consumed_request_reopened", True), None),
            ("authorization token reused", None, None, lambda r: r.__setitem__("authorization_token_reused", True), None),
            ("artifact existence treated as authority", None, None, lambda r: r.__setitem__("artifact_existence_treated_as_lookup_command_execution_authority", True), None),
            ("latest file posture treated as authority", None, None, lambda r: r.__setitem__("latest_file_posture_treated_as_lookup_command_execution_authority", True), None),
            ("repo-local availability treated as authority", None, None, lambda r: r.__setitem__("repo_local_availability_treated_as_lookup_command_execution_authority", True), None),
            ("hidden repo state used as content", None, None, lambda r: r.__setitem__("hidden_repo_state_used_as_lookup_command_execution_content", True), None),
            ("hidden repo state used as authority", None, None, lambda r: r.__setitem__("hidden_repo_state_used_as_lookup_command_execution_authority", True), None),
            ("predecessor failure repaired", None, None, lambda r: r.__setitem__("predecessor_failure_repaired", True), None),
            ("predecessor failure hidden", None, None, lambda r: r.__setitem__("predecessor_failure_hidden", True), None),
            ("predecessor failure claimed passed", None, None, lambda r: r.__setitem__("predecessor_failure_claimed_passed", True), None),
            ("required non-claim flipped", None, None, lambda r: r["declared_non_claims"].__setitem__("lookup_performed", True), None),
        )
        slash_cases = {
            "raw/full state packet body exposure artifact not recorded",
            "raw/full state packet body exposure artifact failed checks present",
            "raw/full state packet body exposure artifact version not 0.1.0",
            "selected raw/full state packet body exposure not recorded",
            "raw/full state packet body not exposed",
            "raw/full state packet body exposure local only not true",
            "raw/full state packet body exposure read only not true",
        }
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            for index, (
                name,
                boundary_mutator,
                raw_mutator,
                request_mutator,
                direct,
            ) in enumerate(cases):
                with self.subTest(name=name):
                    filename = self.safe_json_filename(name, index=index)
                    if name in slash_cases:
                        self.assertIn("raw_full", filename)
                    if direct == "missing_request":
                        result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
                            {}
                        )
                    elif direct == "non_mapping":
                        result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
                            ["not", "a", "mapping"]  # type: ignore[arg-type]
                        )
                    else:
                        boundary = self.synthetic_lookup_command_execution_boundary_artifact()
                        raw_full = self.synthetic_raw_full_state_packet_body_exposure_artifact()
                        if boundary_mutator is not None:
                            boundary_mutator(boundary)
                        if raw_mutator is not None:
                            raw_mutator(raw_full)
                        boundary_path = tmp_path / f"boundary_{filename}"
                        raw_full_path = tmp_path / f"raw_full_{filename}"
                        if direct == "boundary_array":
                            boundary_path.write_text("[]", encoding="utf-8")
                        else:
                            self.write_json(boundary_path, boundary)
                        if direct == "raw_array":
                            raw_full_path.write_text("[]", encoding="utf-8")
                        else:
                            self.write_json(raw_full_path, raw_full)
                        request = self.build_request(boundary_path, raw_full_path)
                        request["_tmpdir"] = str(tmp_path)
                        if request_mutator is not None:
                            request_mutator(request)
                        request.pop("_tmpdir", None)
                        result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
                            request
                        )
                    self.assert_blocked_with_public_code(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, raw_full_path = self.write_synthetic_basis_artifacts(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
                self.build_request(boundary_path, raw_full_path)
            )
        execution = self.execution(result)
        self.assertEqual(
            execution["lookup_command_execution_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION",
        )
        self.assertEqual(
            execution["lookup_command_execution_scope"],
            "SELECTED_LOOKUP_COMMAND_EXECUTION_ONLY",
        )
        self.assertEqual(execution["selected_command"], "state")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn(resolver.OUTCOME_RECORDED, serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION", serialized)
        self.assertIn("SELECTED_LOOKUP_COMMAND_EXECUTION_ONLY", serialized)
        self.assertIn('"state"', serialized)
        self.assertNotIn("[REDACTED", serialized)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary = self.synthetic_lookup_command_execution_boundary_artifact()
            raw_full = self.synthetic_raw_full_state_packet_body_exposure_artifact()
            boundary["raw_lookup_command_execution_boundary_body"] = HOSTILE_SENTINELS[4]
            boundary["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            raw_full["raw_full_state_packet_body_exposure_body"] = HOSTILE_SENTINELS[5]
            raw_full["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            boundary_path, raw_full_path = self.write_synthetic_basis_artifacts(
                Path(tmp), boundary, raw_full
            )
            request = self.build_request(boundary_path, raw_full_path)
            request["raw_lookup_command_execution_body"] = HOSTILE_SENTINELS[0]
            request["hidden_repo_state"] = {"body": HOSTILE_SENTINELS[-1]}
            before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
                request
            )
        self.assertEqual(request, before)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_serialized_result_excludes_sentinels(result)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_COMMAND_EXECUTION", serialized)
        self.assertIn("SELECTED_LOOKUP_COMMAND_EXECUTION_ONLY", serialized)
        self.assert_canonical_false_non_claims(result)
        self.assert_lookup_command_execution_non_claims(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary_path, raw_full_path = self.write_synthetic_basis_artifacts(tmp_path)
            request_path = tmp_path / "request.json"
            request_path.write_text(
                json.dumps(
                    self.build_request(boundary_path, raw_full_path),
                    indent=2,
                    sort_keys=True,
                ),
                encoding="utf-8",
            )
            result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min_from_path(
                request_path
            )
            self.assert_clean_recorded_execution(result, boundary_path, raw_full_path)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            self.assert_path_blocks_or_raises(malformed_path)
            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_path_blocks_or_raises(array_path)
            self.assert_path_blocks_or_raises(tmp_path / "missing_request.json")

            output_root = tmp_path / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                written = resolver.write_local_relevance_medium_read_only_lookup_command_execution_v0_min_result(
                    result
                )
                written_again = resolver.write_local_relevance_medium_read_only_lookup_command_execution_v0_min_result(
                    result
                )
            self.assertTrue(written.parent.exists())
            self.assertTrue(written.exists())
            self.assertTrue(written_again.exists())
            self.assertNotEqual(written, written_again)
            self.assertTrue(written_again.stem.endswith("_001"))
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn(
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_command_execution_v0_min",
                written.parts,
            )
            self.assert_not_under_forbidden_roots(written)
            self.assert_not_under_forbidden_roots(written_again)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary = self.synthetic_lookup_command_execution_boundary_artifact()
            raw_full = self.synthetic_raw_full_state_packet_body_exposure_artifact()
            boundary["nested_raw"] = {
                "raw_lookup_command_execution_boundary_body": HOSTILE_SENTINELS[4]
            }
            raw_full["nested_raw"] = {
                "raw_full_state_packet_body_exposure_body": HOSTILE_SENTINELS[5]
            }
            boundary_before = copy.deepcopy(boundary)
            raw_full_before = copy.deepcopy(raw_full)
            boundary_path, raw_full_path = self.write_synthetic_basis_artifacts(
                Path(tmp), boundary, raw_full
            )
            self.assertEqual(boundary, boundary_before)
            self.assertEqual(raw_full, raw_full_before)
            request = self.build_request(boundary_path, raw_full_path)
            request["posture_mappings"] = {
                "lookup_command_executed": True,
                "lookup_performed": False,
            }
            request["closure_tokens"] = {
                "consumed_request_reopened": False,
                "authorization_token_reused": False,
            }
            request["nested_raw_payload"] = {
                "raw_lookup_result_body": HOSTILE_SENTINELS[3]
            }
            before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
                request
            )
        self.assertEqual(request, before)
        self.assertEqual(request["declared_non_claims"], before["declared_non_claims"])
        self.assertEqual(
            request["selected_lookup_command_execution_boundary_artifact"],
            before["selected_lookup_command_execution_boundary_artifact"],
        )
        self.assertEqual(
            request["selected_raw_full_state_packet_body_exposure_artifact"],
            before["selected_raw_full_state_packet_body_exposure_artifact"],
        )
        self.assertEqual(request["selected_command"], before["selected_command"])
        self.assertEqual(
            request["lookup_command_execution_type"],
            before["lookup_command_execution_type"],
        )
        self.assertEqual(
            request["lookup_command_execution_scope"],
            before["lookup_command_execution_scope"],
        )
        self.assertEqual(request["posture_mappings"], before["posture_mappings"])
        self.assertEqual(request["closure_tokens"], before["closure_tokens"])
        self.assertEqual(request["nested_raw_payload"], before["nested_raw_payload"])
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, raw_full_path = self.write_synthetic_basis_artifacts(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_lookup_command_execution_v0_min(
                self.build_request(boundary_path, raw_full_path)
            )
        statement = self.statement(result)
        summary = self.summary(result)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        non_claims = self.non_claims(result)
        self.assertIs(non_claims["predecessor_failure_repaired"], False)
        self.assertIs(non_claims["predecessor_failure_hidden"], False)
        self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
