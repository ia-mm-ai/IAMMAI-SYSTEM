"""Tests for the selected-state local read-only state result object resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT object. It verifies that
the resolver reads one clean state-result-object boundary artifact and one clean
selected-state payload return artifact, records one local read-only
selected-state result object, and keeps packet body exposure, raw/full packet
body exposure, lookup, command lookup execution, permissions, public/distributed
surfaces, registry/search/query/ranking, filesystem discovery, source transfer,
participation, and follow-on work out of the object and result-level posture.
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

import resolve_local_relevance_medium_read_only_state_result_object_v0_min as resolver  # noqa: E402


DEFAULT_STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_result_object_boundary_v0_min/"
    "local_relevance_medium_read_only_state_result_object_boundary_reference_review_001__"
    "local_relevance_medium_read_only_state_result_object_boundary_v0_min_result.json"
)
DEFAULT_STATE_PAYLOAD_RETURN_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_payload_return_v0_min/"
    "local_relevance_medium_read_only_state_payload_return_reference_review_001__"
    "local_relevance_medium_read_only_state_payload_return_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_result_object_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_result_object_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_payload_return_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_payload_return_boundary_v0_min"),
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
    "local_relevance_medium_read_only_state_result_object_metadata",
    "declared_local_relevance_medium_read_only_state_result_object_question",
    "selected_state_result_object_boundary_artifact_basis",
    "selected_state_payload_return_artifact_basis",
    "local_relevance_medium_read_only_state_result_object",
    "local_relevance_medium_read_only_state_result_object_checks",
    "local_relevance_medium_read_only_state_result_object_statement",
    "local_relevance_medium_read_only_state_result_object_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_state_result_object_summary",
)

FORBIDDEN_STATE_RESULT_OBJECT_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_state_result_object_checks",
    "non_claims",
    "local_relevance_medium_read_only_state_result_object_summary",
    "local_relevance_medium_read_only_state_result_object_metadata",
)

STATE_RESULT_OBJECT_FALSE_FIELDS = (
    "state_packet_body_exposed",
    "raw_full_state_packet_body_exposed",
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

REQUEST_ONLY_FALSE_FIELDS = (
    "source_created",
    "deployment_created",
    "public_release_created",
    "broader_reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "artifact_existence_treated_as_state_result_object_authority",
    "latest_file_posture_treated_as_state_result_object_authority",
    "repo_local_availability_treated_as_state_result_object_authority",
    "hidden_repo_state_used_as_state_result_object_content",
    "hidden_repo_state_used_as_state_result_object_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "local_relevance_medium_read_only_state_result_object_recorded",
    "basis_state_result_object_boundary_artifact_preserved",
    "basis_state_payload_return_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_state_payload_return_recorded",
    "state_payload_returned",
    "state_payload_return_local_only",
    "state_payload_return_read_only",
    "state_result_object_created",
    "state_result_object_local_only",
    "state_result_object_read_only",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_OBJECT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_OBJECT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_RETURN_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PAYLOAD_BODY_MUST_NOT_RETURN",
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


def _clean_state_result_object_boundary_artifact(**overrides: Any) -> dict[str, Any]:
    boundary = {
        "boundary_id": "local_relevance_medium_read_only_state_result_object_boundary_001",
        "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY",
        "boundary_version": "0.1.0",
        "boundary_scope": "SELECTED_STATE_RESULT_OBJECT_CONSIDERATION_ONLY",
        "basis_state_payload_return_artifact": str(DEFAULT_STATE_PAYLOAD_RETURN_ARTIFACT),
        "basis_state_payload_return_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_RECORDED",
        "basis_state_payload_return_result_version": "0.1.0",
        "basis_state_payload_return_failed_check_count": 0,
        "selected_command": "state",
        "selected_command_is_state": True,
        "selected_state_payload_return_recorded": True,
        "state_payload_returned": True,
        "state_payload_return_local_only": True,
        "state_payload_return_read_only": True,
        "future_state_result_object_may_be_considered": True,
        "state_result_object_created": False,
        "state_packet_body_exposed": False,
        "raw_full_state_packet_body_exposed": False,
        "lookup_performed": False,
        "lookup_command_executed": False,
    }
    for field in STATE_RESULT_OBJECT_FALSE_FIELDS:
        boundary.setdefault(field, False)
    boundary.update(overrides)
    statement = {
        "local_relevance_medium_read_only_state_result_object_boundary_recorded": True,
        "basis_state_payload_return_artifact_preserved": True,
        "selected_command_preserved": True,
        "selected_command_is_state": True,
        "selected_state_payload_return_recorded": True,
        "state_payload_returned": True,
        "state_payload_return_local_only": True,
        "state_payload_return_read_only": True,
        "future_state_result_object_may_be_considered": True,
        "result_level_non_claims_canonical_false": True,
    }
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_RECORDED",
        "result_version": "0.1.0",
        "failed_check_count": 0,
        "local_relevance_medium_read_only_state_result_object_boundary_metadata": {
            "local_relevance_medium_read_only_state_result_object_boundary_id": boundary[
                "boundary_id"
            ],
            "local_relevance_medium_read_only_state_result_object_boundary_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_read_only_state_result_object_boundary_v0_min",
        },
        "local_relevance_medium_read_only_state_result_object_boundary": boundary,
        "local_relevance_medium_read_only_state_result_object_boundary_checks": [],
        "local_relevance_medium_read_only_state_result_object_boundary_statement": statement,
        "local_relevance_medium_read_only_state_result_object_boundary_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 75,
        },
    }


def _clean_state_payload_return_artifact(**overrides: Any) -> dict[str, Any]:
    payload_return = {
        "state_payload_return_id": "local_relevance_medium_read_only_state_payload_return_001",
        "state_payload_return_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN",
        "state_payload_return_version": "0.1.0",
        "state_payload_return_scope": "SELECTED_STATE_PAYLOAD_RETURN_ONLY",
        "selected_command": "state",
        "selected_command_is_state": True,
        "selected_state_payload_return_recorded": True,
        "state_payload_returned": True,
        "state_payload_return_local_only": True,
        "state_payload_return_read_only": True,
        "state_result_object_created": False,
        "state_packet_body_exposed": False,
        "raw_full_state_packet_body_exposed": False,
        "lookup_performed": False,
        "lookup_command_executed": False,
    }
    for field in STATE_RESULT_OBJECT_FALSE_FIELDS:
        payload_return.setdefault(field, False)
    payload_return.update(overrides)
    statement = {
        "local_relevance_medium_read_only_state_payload_return_recorded": True,
        "selected_command_preserved": True,
        "selected_command_is_state": True,
        "selected_state_payload_return_recorded": True,
        "state_payload_returned": True,
        "state_payload_return_local_only": True,
        "state_payload_return_read_only": True,
        "result_level_non_claims_canonical_false": True,
    }
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_RECORDED",
        "result_version": "0.1.0",
        "failed_check_count": 0,
        "local_relevance_medium_read_only_state_payload_return_metadata": {
            "local_relevance_medium_read_only_state_payload_return_id": payload_return[
                "state_payload_return_id"
            ],
            "local_relevance_medium_read_only_state_payload_return_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_read_only_state_payload_return_v0_min",
        },
        "local_relevance_medium_read_only_state_payload_return": payload_return,
        "local_relevance_medium_read_only_state_payload_return_checks": [],
        "local_relevance_medium_read_only_state_payload_return_statement": statement,
        "local_relevance_medium_read_only_state_payload_return_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 347,
        },
    }


class LocalRelevanceMediumReadOnlyStateResultObjectTests(unittest.TestCase):
    def make_bundle(self, temp_dir: str) -> dict[str, Any]:
        root = Path(temp_dir)
        boundary_path = root / "state_result_object_boundary.json"
        payload_path = root / "state_payload_return.json"
        boundary_artifact = _clean_state_result_object_boundary_artifact()
        payload_artifact = _clean_state_payload_return_artifact()
        request = resolver.build_declared_local_relevance_medium_read_only_state_result_object_v0_min_request(
            selected_state_result_object_boundary_artifact=boundary_path,
            selected_state_payload_return_artifact=payload_path,
        )
        return {
            "boundary_path": boundary_path,
            "payload_path": payload_path,
            "boundary_artifact": boundary_artifact,
            "payload_artifact": payload_artifact,
            "request": request,
            "write_boundary": True,
            "write_payload": True,
        }

    def resolve_bundle(
        self,
        temp_dir: str,
        mutator: Callable[[dict[str, Any]], None] | None = None,
    ) -> dict[str, Any]:
        bundle = self.make_bundle(temp_dir)
        if mutator is not None:
            mutator(bundle)
        if bundle.get("write_boundary", True):
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
        if bundle.get("write_payload", True):
            _write_json(bundle["payload_path"], bundle["payload_artifact"])
        return resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min(
            bundle["request"]
        )

    def recorded_result(self) -> tuple[dict[str, Any], Path, Path]:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        bundle = self.make_bundle(temp.name)
        _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
        _write_json(bundle["payload_path"], bundle["payload_artifact"])
        result = resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min(
            bundle["request"]
        )
        return result, bundle["boundary_path"], bundle["payload_path"]

    def summary(self, result: Mapping[str, Any]) -> dict[str, Any]:
        return resolver.build_local_relevance_medium_read_only_state_result_object_v0_min_summary(
            result
        )

    def state_result_object(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result["local_relevance_medium_read_only_state_result_object"]
        self.assertIsInstance(value, dict)
        return value

    def statement(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result["local_relevance_medium_read_only_state_result_object_statement"]
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: Mapping[str, Any]) -> list[dict[str, Any]]:
        value = result["local_relevance_medium_read_only_state_result_object_checks"]
        self.assertIsInstance(value, list)
        return value

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        code = block.get("block_code") or block.get("code")
        return code if isinstance(code, str) else None

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_same_or_stable_artifact_path(self, actual: Any, expected: Path | str) -> None:
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
        block_code = self.block_code(result)
        if block_code is not None:
            self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            self.assertIsInstance(check, dict)
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)

    def assert_no_forbidden_result_posture(self, result: Mapping[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        object_value = result.get("local_relevance_medium_read_only_state_result_object")
        if isinstance(object_value, Mapping):
            for field in STATE_RESULT_OBJECT_FALSE_FIELDS:
                self.assertIs(object_value[field], False)
        non_claims = result["non_claims"]
        for field in STATE_RESULT_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS:
            self.assertIs(non_claims[field], False)

    def assert_result_object_not_wrapper(self, state_result_object: Mapping[str, Any]) -> None:
        for key in FORBIDDEN_STATE_RESULT_OBJECT_WRAPPER_FIELDS:
            self.assertNotIn(key, state_result_object)

    def assert_state_result_object_posture(
        self,
        result: Mapping[str, Any],
        boundary_path: Path,
        payload_path: Path,
    ) -> None:
        state_result_object = self.state_result_object(result)
        self.assertEqual(
            state_result_object["state_result_object_id"],
            "local_relevance_medium_read_only_state_result_object_001",
        )
        self.assertEqual(
            state_result_object["state_result_object_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT",
        )
        self.assertEqual(state_result_object["state_result_object_version"], "0.1.0")
        self.assertEqual(
            state_result_object["state_result_object_scope"],
            "SELECTED_STATE_RESULT_OBJECT_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            state_result_object["basis_state_result_object_boundary_artifact"],
            boundary_path,
        )
        self.assertEqual(
            state_result_object["basis_state_result_object_boundary_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            state_result_object["basis_state_result_object_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            state_result_object["basis_state_result_object_boundary_failed_check_count"],
            0,
        )
        self.assert_same_or_stable_artifact_path(
            state_result_object["basis_state_payload_return_artifact"],
            payload_path,
        )
        self.assertEqual(
            state_result_object["basis_state_payload_return_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_RECORDED",
        )
        self.assertEqual(
            state_result_object["basis_state_payload_return_result_version"],
            "0.1.0",
        )
        self.assertEqual(state_result_object["basis_state_payload_return_failed_check_count"], 0)
        self.assertEqual(state_result_object["selected_command"], "state")
        self.assertIs(state_result_object["selected_command_is_state"], True)
        self.assertIs(state_result_object["selected_state_payload_return_recorded"], True)
        self.assertIs(state_result_object["state_payload_returned"], True)
        self.assertIs(state_result_object["state_payload_return_local_only"], True)
        self.assertIs(state_result_object["state_payload_return_read_only"], True)
        self.assertIs(
            state_result_object["local_relevance_medium_read_only_state_result_object_recorded"],
            True,
        )
        self.assertIs(state_result_object["state_result_object_created"], True)
        self.assertIs(state_result_object["state_result_object_local_only"], True)
        self.assertIs(state_result_object["state_result_object_read_only"], True)
        for field in STATE_RESULT_OBJECT_FALSE_FIELDS:
            self.assertIn(field, state_result_object)
            self.assertIs(state_result_object[field], False)
            self.assertIsInstance(state_result_object[field], bool)
        self.assert_result_object_not_wrapper(state_result_object)

    def assert_statement_true_fields(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        for key in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True)

    def assert_blocked_common(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.summary(result)["failed_check_count"], 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_no_forbidden_result_posture(result)

    def assert_path_not_under_forbidden_roots(self, path: Path | str) -> None:
        for root in FORBIDDEN_OUTPUT_ROOTS:
            self.assertFalse(_path_has_component_prefix(path, root), root)

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_state_result_object_v0_min",
            "resolve_local_relevance_medium_read_only_state_result_object_v0_min_from_path",
            "write_local_relevance_medium_read_only_state_result_object_v0_min_result",
            "build_local_relevance_medium_read_only_state_result_object_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_state_result_object_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_STATE_RESULT_OBJECT_TYPE_VALUES",
            "SUPPORTED_STATE_RESULT_OBJECT_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_state_result_object_v0_min",
        )
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT",
            resolver.SUPPORTED_STATE_RESULT_OBJECT_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_STATE_RESULT_OBJECT_ONLY",
            resolver.SUPPORTED_STATE_RESULT_OBJECT_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BLOCKED",
            },
        )

        request = resolver.build_declared_local_relevance_medium_read_only_state_result_object_v0_min_request()
        self.assertTrue(
            request["selected_state_result_object_boundary_artifact"].endswith(
                "local_relevance_medium_read_only_state_result_object_boundary_reference_review_001__"
                "local_relevance_medium_read_only_state_result_object_boundary_v0_min_result.json"
            )
        )
        self.assertTrue(
            request["selected_state_payload_return_artifact"].endswith(
                "local_relevance_medium_read_only_state_payload_return_reference_review_001__"
                "local_relevance_medium_read_only_state_payload_return_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], "state")
        self.assert_path_not_under_forbidden_roots(resolver.OUTPUT_ROOT)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        result, boundary_path, payload_path = self.recorded_result()
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        summary = self.summary(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            summary["state_result_object_id"],
            "local_relevance_medium_read_only_state_result_object_001",
        )

        for key in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(key, result)

        self.assert_state_result_object_posture(result, boundary_path, payload_path)
        self.assert_statement_true_fields(result)
        self.assert_non_claims_canonical_false(result)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT.exists():
            self.skipTest("default state result object boundary artifact is not present")
        if not DEFAULT_STATE_PAYLOAD_RETURN_ARTIFACT.exists():
            self.skipTest("default state payload return artifact is not present")

        request = resolver.build_declared_local_relevance_medium_read_only_state_result_object_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.summary(result)["failed_check_count"], 0)
        self.assert_not_blocked(result)
        state_result_object = self.state_result_object(result)
        self.assertEqual(state_result_object["selected_command"], "state")
        self.assertEqual(
            state_result_object["state_result_object_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT",
        )
        self.assertEqual(
            state_result_object["state_result_object_scope"],
            "SELECTED_STATE_RESULT_OBJECT_ONLY",
        )
        self.assertIs(state_result_object["selected_state_payload_return_recorded"], True)
        self.assertIs(state_result_object["state_payload_returned"], True)
        self.assertIs(state_result_object["state_payload_return_local_only"], True)
        self.assertIs(state_result_object["state_payload_return_read_only"], True)
        self.assertIs(
            state_result_object["local_relevance_medium_read_only_state_result_object_recorded"],
            True,
        )
        self.assertIs(state_result_object["state_result_object_created"], True)
        self.assertIs(state_result_object["state_result_object_local_only"], True)
        self.assertIs(state_result_object["state_result_object_read_only"], True)
        self.assertIs(state_result_object["state_packet_body_exposed"], False)
        self.assertIs(state_result_object["raw_full_state_packet_body_exposed"], False)
        self.assertIs(state_result_object["lookup_performed"], False)
        self.assertIs(state_result_object["lookup_command_executed"], False)
        for key in (
            "operation_permission_created",
            "runtime_permission_created",
            "public_api_created",
            "distributed_network_behavior_created",
            "general_lookup_permission_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(state_result_object[key], False)
        self.assert_same_or_stable_artifact_path(
            state_result_object["basis_state_result_object_boundary_artifact"],
            DEFAULT_STATE_RESULT_OBJECT_BOUNDARY_ARTIFACT,
        )
        self.assert_same_or_stable_artifact_path(
            state_result_object["basis_state_payload_return_artifact"],
            DEFAULT_STATE_PAYLOAD_RETURN_ARTIFACT,
        )

    def test_critical_non_claim_canonicalization_blocks_flipped_declared_values(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
            _write_json(bundle["payload_path"], bundle["payload_artifact"])
            clean_request = bundle["request"]

            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min(
                        request
                    )
                    self.assert_blocked_common(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertNotEqual(result["non_claims"][key], True)

    def test_representative_blocking_behavior(self) -> None:
        def boundary_json_array(bundle: dict[str, Any]) -> None:
            bundle["boundary_artifact"] = []

        def payload_json_array(bundle: dict[str, Any]) -> None:
            bundle["payload_artifact"] = []

        def boundary_unreadable(bundle: dict[str, Any]) -> None:
            bundle["request"]["selected_state_result_object_boundary_artifact"] = str(
                Path(bundle["boundary_path"]).with_name("missing-boundary.json")
            )
            bundle["write_boundary"] = False

        def payload_unreadable(bundle: dict[str, Any]) -> None:
            bundle["request"]["selected_state_payload_return_artifact"] = str(
                Path(bundle["payload_path"]).with_name("missing-payload.json")
            )
            bundle["write_payload"] = False

        def boundary_not_recorded(bundle: dict[str, Any]) -> None:
            bundle["boundary_artifact"]["outcome"] = (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_NOT_RECORDED"
            )
            bundle["boundary_artifact"][
                "local_relevance_medium_read_only_state_result_object_boundary_summary"
            ]["outcome"] = (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_NOT_RECORDED"
            )

        def boundary_failed(bundle: dict[str, Any]) -> None:
            bundle["boundary_artifact"]["failed_check_count"] = 1
            bundle["boundary_artifact"][
                "local_relevance_medium_read_only_state_result_object_boundary_summary"
            ]["failed_check_count"] = 1

        def boundary_version(bundle: dict[str, Any]) -> None:
            bundle["boundary_artifact"]["result_version"] = "9.9.9"
            bundle["boundary_artifact"][
                "local_relevance_medium_read_only_state_result_object_boundary_summary"
            ]["result_version"] = "9.9.9"

        def payload_not_recorded(bundle: dict[str, Any]) -> None:
            bundle["payload_artifact"]["outcome"] = (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_NOT_RECORDED"
            )
            bundle["payload_artifact"][
                "local_relevance_medium_read_only_state_payload_return_summary"
            ]["outcome"] = (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_NOT_RECORDED"
            )

        def payload_failed(bundle: dict[str, Any]) -> None:
            bundle["payload_artifact"]["failed_check_count"] = 1
            bundle["payload_artifact"][
                "local_relevance_medium_read_only_state_payload_return_summary"
            ]["failed_check_count"] = 1

        def payload_version(bundle: dict[str, Any]) -> None:
            bundle["payload_artifact"]["result_version"] = "9.9.9"
            bundle["payload_artifact"][
                "local_relevance_medium_read_only_state_payload_return_summary"
            ]["result_version"] = "9.9.9"

        object_field_cases: tuple[tuple[str, str, Any], ...] = (
            ("selected command not state", "selected_command", "lookup first_orientation_locator"),
            ("state result object type not supported", "state_result_object_type", "WRONG_TYPE"),
            ("state result object scope not supported", "state_result_object_scope", "WRONG_SCOPE"),
            ("state result object created false", "state_result_object_created", False),
            ("state result object local only false", "state_result_object_local_only", False),
            ("state result object read only false", "state_result_object_read_only", False),
        )
        shortcut_true_cases = (
            "state_result_object_boundary_artifact_missing",
            "state_payload_return_artifact_missing",
            "selected_command_missing",
            "selected_command_not_state",
            "selected_state_payload_return_not_recorded",
            "state_payload_not_returned",
            "state_payload_return_local_only_not_true",
            "state_payload_return_read_only_not_true",
            "state_result_object_type_not_local_relevance_medium_read_only_state_result_object",
            "state_result_object_scope_not_selected_state_result_object_only",
            "local_relevance_medium_read_only_state_result_object_not_recorded",
            "state_result_object_not_created",
            "state_result_object_local_only_not_true",
            "state_result_object_read_only_not_true",
        )
        false_field_cases = STATE_RESULT_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS
        direct_request_cases: list[tuple[str, Any]] = [
            ("missing request", None),
            ("non-mapping request", ["not", "mapping"]),
        ]
        mutation_cases: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
            (
                "explicit block intent",
                lambda bundle: _set(
                    bundle["request"],
                    "local_relevance_medium_read_only_state_result_object_intent",
                    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT",
                ),
            ),
            (
                "unsupported intent",
                lambda bundle: _set(
                    bundle["request"],
                    "local_relevance_medium_read_only_state_result_object_intent",
                    "UNSUPPORTED_INTENT",
                ),
            ),
            (
                "state result object boundary artifact path missing",
                lambda bundle: _set(
                    bundle["request"],
                    "selected_state_result_object_boundary_artifact",
                    "",
                ),
            ),
            ("state result object boundary artifact unreadable", boundary_unreadable),
            ("state result object boundary artifact JSON array instead of object", boundary_json_array),
            ("state result object boundary artifact not recorded", boundary_not_recorded),
            ("state result object boundary artifact failed checks present", boundary_failed),
            ("state result object boundary artifact version not 0.1.0", boundary_version),
            (
                "state payload return artifact path missing",
                lambda bundle: _set(bundle["request"], "selected_state_payload_return_artifact", ""),
            ),
            ("state payload return artifact unreadable", payload_unreadable),
            ("state payload return artifact JSON array instead of object", payload_json_array),
            ("state payload return artifact not recorded", payload_not_recorded),
            ("state payload return artifact failed checks present", payload_failed),
            ("state payload return artifact version not 0.1.0", payload_version),
            ("selected command missing", lambda bundle: _pop(bundle["request"], "selected_command")),
            (
                "state result object type missing",
                lambda bundle: _pop(bundle["request"], "state_result_object_type"),
            ),
            (
                "state result object scope missing",
                lambda bundle: _pop(bundle["request"], "state_result_object_scope"),
            ),
            (
                "required non-claim missing",
                lambda bundle: _pop(
                    bundle["request"]["declared_non_claims"],
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0],
                ),
            ),
            (
                "required non-claim flipped",
                lambda bundle: _set(
                    bundle["request"]["declared_non_claims"],
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0],
                    True,
                ),
            ),
        ]
        for label, key, value in object_field_cases:
            mutation_cases.append((label, lambda bundle, key=key, value=value: _set(bundle["request"], key, value)))
        for key in shortcut_true_cases + false_field_cases:
            mutation_cases.append(
                (key, lambda bundle, key=key: _set(bundle["request"], key, True))
            )

        for label, request in direct_request_cases:
            with self.subTest(case=label):
                result = resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min(
                    request
                )
                self.assert_blocked_common(result)

        with tempfile.TemporaryDirectory() as temp_dir:
            for label, mutator in mutation_cases:
                with self.subTest(case=label):
                    result = self.resolve_bundle(temp_dir, mutator)
                    self.assert_blocked_common(result)

    def test_missing_or_incomplete_declared_non_claims_behavior(self) -> None:
        variants: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("remove declared_non_claims", lambda request: _pop(request, "declared_non_claims")),
            ("empty declared_non_claims", lambda request: _set(request, "declared_non_claims", {})),
            (
                "remove one required non-claim",
                lambda request: _pop(request["declared_non_claims"], resolver.REQUIRED_FALSE_NON_CLAIMS[0]),
            ),
            (
                "non-bool declared non-claim",
                lambda request: _set(
                    request["declared_non_claims"],
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0],
                    "false",
                ),
            ),
            (
                "none declared non-claim",
                lambda request: _set(
                    request["declared_non_claims"],
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0],
                    None,
                ),
            ),
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
            _write_json(bundle["payload_path"], bundle["payload_artifact"])
            for label, mutate_request in variants:
                with self.subTest(case=label):
                    request = copy.deepcopy(bundle["request"])
                    mutate_request(request)
                    result = resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min(
                        request
                    )
                    self.assertIn(
                        result["outcome"],
                        (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS),
                    )
                    self.assert_all_emitted_codes_public(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        result, _, _ = self.recorded_result()
        state_result_object = self.state_result_object(result)
        self.assertEqual(
            state_result_object["state_result_object_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT",
        )
        self.assertEqual(
            state_result_object["state_result_object_scope"],
            "SELECTED_STATE_RESULT_OBJECT_ONLY",
        )
        self.assertEqual(state_result_object["selected_command"], "state")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BLOCKED",
            },
        )
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_RECORDED", serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT", serialized)
        self.assertIn("SELECTED_STATE_RESULT_OBJECT_ONLY", serialized)
        self.assertIn('"state"', serialized)
        self.assertNotIn("[REDACTED_SENSITIVE_CONTENT]", state_result_object.values())

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            request_before = copy.deepcopy(bundle["request"])
            boundary_before = copy.deepcopy(bundle["boundary_artifact"])
            payload_before = copy.deepcopy(bundle["payload_artifact"])
            bundle["request"]["raw_full_state_packet_body"] = HOSTILE_SENTINELS[3]
            bundle["request"]["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            bundle["request"]["extra_section"] = {"state_packet_body": HOSTILE_SENTINELS[4]}
            bundle["boundary_artifact"]["raw_state_result_object_boundary_body"] = (
                HOSTILE_SENTINELS[5]
            )
            bundle["payload_artifact"]["raw_state_payload_return_body"] = HOSTILE_SENTINELS[6]
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
            _write_json(bundle["payload_path"], bundle["payload_artifact"])
            request_for_resolve = copy.deepcopy(bundle["request"])
            result = resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min(
                request_for_resolve
            )

            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            for sentinel in HOSTILE_SENTINELS:
                self.assertNotIn(sentinel, serialized)
            self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT", serialized)
            self.assertIn("SELECTED_STATE_RESULT_OBJECT_ONLY", serialized)
            self.assertIn("state", serialized)
            self.assert_no_forbidden_result_posture(result)
            self.assertEqual(request_for_resolve, bundle["request"])
            clean_subset = self.make_bundle(temp_dir)
            self.assertEqual(request_before, clean_subset["request"])
            self.assertEqual(boundary_before, clean_subset["boundary_artifact"])
            self.assertEqual(payload_before, clean_subset["payload_artifact"])

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
            _write_json(bundle["payload_path"], bundle["payload_artifact"])
            request_path = Path(temp_dir) / "request.json"
            _write_json(request_path, bundle["request"])

            result = resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.summary(result)["result_version"], "0.1.0")
            self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            malformed_path = Path(temp_dir) / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = (
                resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min_from_path(
                    malformed_path
                )
            )
            self.assert_blocked_common(malformed_result)

            array_path = Path(temp_dir) / "array.json"
            _write_json(array_path, [])
            array_result = (
                resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min_from_path(
                    array_path
                )
            )
            self.assert_blocked_common(array_result)

            missing_result = (
                resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min_from_path(
                    Path(temp_dir) / "missing.json"
                )
            )
            self.assert_blocked_common(missing_result)

            output_root = Path(temp_dir) / (
                "artifacts/"
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
                "state_result_object_v0_min"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_state_result_object_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_state_result_object_v0_min_result(
                    result
                )
            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIsInstance(json.loads(first_path.read_text(encoding="utf-8")), dict)
            self.assertIn("state_result_object_v0_min", str(first_path))
            self.assert_path_not_under_forbidden_roots(first_path)
            self.assert_path_not_under_forbidden_roots(second_path)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            request = bundle["request"]
            request["nested_raw"] = {"raw_state_result_object_body": HOSTILE_SENTINELS[0]}
            request_before = copy.deepcopy(request)
            declared_before = copy.deepcopy(request["declared_non_claims"])
            boundary_path_before = request["selected_state_result_object_boundary_artifact"]
            payload_path_before = request["selected_state_payload_return_artifact"]
            selected_command_before = request["selected_command"]
            state_type_before = request["state_result_object_type"]
            state_scope_before = request["state_result_object_scope"]
            boundary_before = copy.deepcopy(bundle["boundary_artifact"])
            payload_before = copy.deepcopy(bundle["payload_artifact"])
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
            _write_json(bundle["payload_path"], bundle["payload_artifact"])

            resolver.resolve_local_relevance_medium_read_only_state_result_object_v0_min(request)

            self.assertEqual(request, request_before)
            self.assertEqual(request["declared_non_claims"], declared_before)
            self.assertEqual(request["selected_state_result_object_boundary_artifact"], boundary_path_before)
            self.assertEqual(request["selected_state_payload_return_artifact"], payload_path_before)
            self.assertEqual(request["selected_command"], selected_command_before)
            self.assertEqual(request["state_result_object_type"], state_type_before)
            self.assertEqual(request["state_result_object_scope"], state_scope_before)
            self.assertEqual(bundle["boundary_artifact"], boundary_before)
            self.assertEqual(bundle["payload_artifact"], payload_before)
            self.assertEqual(request["nested_raw"], request_before["nested_raw"])

    def test_predecessor_failure_preservation(self) -> None:
        result, _, _ = self.recorded_result()
        statement = self.statement(result)
        summary = self.summary(result)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["predecessor_failure_repaired"], False)
        self.assertIs(statement["predecessor_failure_hidden"], False)
        self.assertIs(statement["predecessor_failure_claimed_passed"], False)
        self.assertIs(statement["consumed_request_reopened"], False)
        self.assertIs(statement["authorization_token_reused"], False)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)


if __name__ == "__main__":
    unittest.main()
