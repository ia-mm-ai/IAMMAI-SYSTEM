"""Tests for the selected-state local read-only state packet body exposure.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE object. It verifies
that the resolver reads one clean state packet body exposure boundary v2
artifact and one clean selected-state result object artifact, records one local
read-only selected-state packet body exposure event, and keeps raw/full packet
body exposure, lookup, lookup command execution, permissions,
public/distributed surfaces, registry/search/query/ranking, filesystem
discovery, source transfer, participation, and follow-on work out of the object
and result-level posture.
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

import resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min as resolver  # noqa: E402


DEFAULT_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_packet_body_exposure_boundary_v0_min_v2/"
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_"
    "reference_review_001__local_relevance_medium_read_only_state_packet_body_"
    "exposure_boundary_v0_min_v2_result.json"
)
DEFAULT_STATE_RESULT_OBJECT_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_result_object_v0_min/"
    "local_relevance_medium_read_only_state_result_object_reference_review_001__"
    "local_relevance_medium_read_only_state_result_object_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_packet_body_exposure_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_result_object_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_result_object_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_payload_return_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_payload_return_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_result_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_execution_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_local_carrier_command_surface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_state_packet_body_exposure_metadata",
    "declared_local_relevance_medium_read_only_state_packet_body_exposure_question",
    "selected_state_packet_body_exposure_boundary_artifact_basis",
    "selected_state_result_object_artifact_basis",
    "local_relevance_medium_read_only_state_packet_body_exposure",
    "local_relevance_medium_read_only_state_packet_body_exposure_checks",
    "local_relevance_medium_read_only_state_packet_body_exposure_statement",
    "local_relevance_medium_read_only_state_packet_body_exposure_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_state_packet_body_exposure_summary",
)

FORBIDDEN_EXPOSURE_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_state_packet_body_exposure_checks",
    "non_claims",
    "local_relevance_medium_read_only_state_packet_body_exposure_summary",
    "local_relevance_medium_read_only_state_packet_body_exposure_metadata",
)

EXPOSURE_FALSE_FIELDS = (
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
    "consumed_request_reopened",
    "authorization_token_reused",
    "follow_on_work_authorized",
)

BASIS_FALSE_FIELDS = ("state_packet_body_exposed",) + EXPOSURE_FALSE_FIELDS

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "local_relevance_medium_read_only_state_packet_body_exposure_recorded",
    "basis_state_packet_body_exposure_boundary_artifact_preserved",
    "basis_state_result_object_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_state_result_object_recorded",
    "state_result_object_created",
    "state_result_object_local_only",
    "state_result_object_read_only",
    "state_packet_body_exposed",
    "state_packet_body_exposure_local_only",
    "state_packet_body_exposure_read_only",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_OBJECT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
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
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


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


def _clean_boundary_artifact(**overrides: Any) -> dict[str, Any]:
    boundary = {
        "boundary_id": "local_relevance_medium_read_only_state_packet_body_exposure_boundary_001",
        "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY",
        "boundary_version": "0.1.1",
        "boundary_scope": "SELECTED_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY",
        "basis_state_result_object_artifact": "synthetic_selected_state_result_object.json",
        "basis_state_result_object_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_RECORDED",
        "basis_state_result_object_result_version": "0.1.0",
        "basis_state_result_object_failed_check_count": 0,
        "selected_command": "state",
        "selected_command_is_state": True,
        "selected_state_result_object_recorded": True,
        "state_result_object_created": True,
        "state_result_object_local_only": True,
        "state_result_object_read_only": True,
        "future_state_packet_body_exposure_may_be_considered": True,
    }
    for field in BASIS_FALSE_FIELDS:
        boundary[field] = False
    boundary.update(overrides.pop("boundary_overrides", {}))

    artifact = {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED",
        "result_version": "0.1.1",
        "failed_check_count": 0,
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_metadata": {
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_id": boundary[
                "boundary_id"
            ],
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_version": "0.1.1",
            "resolver_module": "resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2",
            "predecessor_resolver_module": "resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min",
            "predecessor_failure_preserved_as_lineage_evidence": True,
        },
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary": boundary,
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_checks": [
            {
                "check_name": "synthetic state packet body exposure boundary clean",
                "passed": True,
            }
        ],
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_statement": {
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_recorded": True,
            "basis_state_result_object_artifact_preserved": True,
            "selected_command_preserved": True,
            "selected_command_is_state": True,
            "selected_state_result_object_recorded": True,
            "state_result_object_created": True,
            "state_result_object_local_only": True,
            "state_result_object_read_only": True,
            "future_state_packet_body_exposure_may_be_considered": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "predecessor_failure_not_repaired": True,
            "predecessor_failure_not_hidden": True,
            "predecessor_failure_not_claimed_passed": True,
            "result_level_non_claims_canonical_false": True,
        },
        "non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
        "block": {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        },
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED",
            "failed_check_count": 0,
            "passed_check_count": 82,
            "result_version": "0.1.1",
            "resolver_module": "resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2",
            "predecessor_resolver_module": "resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min",
            "selected_command": "state",
            "selected_command_is_state": True,
            "selected_state_result_object_recorded": True,
            "state_result_object_created": True,
            "state_result_object_local_only": True,
            "state_result_object_read_only": True,
            "future_state_packet_body_exposure_may_be_considered": True,
            "consumed_request_reopened": False,
            "authorization_token_reused": False,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "predecessor_failure_not_repaired": True,
            "predecessor_failure_not_hidden": True,
            "predecessor_failure_not_claimed_passed": True,
            "result_level_non_claims_canonical_false": True,
        },
    }
    artifact.update(overrides)
    return artifact


def _clean_state_result_object_artifact(**overrides: Any) -> dict[str, Any]:
    state_result_object = {
        "state_result_object_id": "local_relevance_medium_read_only_state_result_object_001",
        "state_result_object_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT",
        "state_result_object_version": "0.1.0",
        "state_result_object_scope": "SELECTED_STATE_RESULT_OBJECT_ONLY",
        "basis_state_result_object_boundary_artifact": "synthetic_state_result_object_boundary.json",
        "basis_state_result_object_boundary_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_BOUNDARY_RECORDED",
        "basis_state_result_object_boundary_result_version": "0.1.0",
        "basis_state_result_object_boundary_failed_check_count": 0,
        "basis_state_payload_return_artifact": "synthetic_state_payload_return.json",
        "basis_state_payload_return_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PAYLOAD_RETURN_RECORDED",
        "basis_state_payload_return_result_version": "0.1.0",
        "basis_state_payload_return_failed_check_count": 0,
        "selected_command": "state",
        "selected_command_is_state": True,
        "local_relevance_medium_read_only_state_result_object_recorded": True,
        "selected_state_result_object_recorded": True,
        "state_result_object_created": True,
        "state_result_object_local_only": True,
        "state_result_object_read_only": True,
    }
    for field in BASIS_FALSE_FIELDS:
        state_result_object[field] = False
    state_result_object.update(overrides.pop("state_result_object_overrides", {}))

    artifact = {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_RECORDED",
        "result_version": "0.1.0",
        "failed_check_count": 0,
        "local_relevance_medium_read_only_state_result_object_metadata": {
            "local_relevance_medium_read_only_state_result_object_id": state_result_object[
                "state_result_object_id"
            ],
            "local_relevance_medium_read_only_state_result_object_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_read_only_state_result_object_v0_min",
        },
        "local_relevance_medium_read_only_state_result_object": state_result_object,
        "local_relevance_medium_read_only_state_result_object_checks": [
            {
                "check_name": "synthetic selected-state result object clean",
                "passed": True,
            }
        ],
        "local_relevance_medium_read_only_state_result_object_statement": {
            "local_relevance_medium_read_only_state_result_object_recorded": True,
            "basis_state_result_object_boundary_artifact_preserved": True,
            "basis_state_payload_return_artifact_preserved": True,
            "selected_command_preserved": True,
            "selected_command_is_state": True,
            "selected_state_result_object_recorded": True,
            "state_result_object_created": True,
            "state_result_object_local_only": True,
            "state_result_object_read_only": True,
            "result_level_non_claims_canonical_false": True,
        },
        "non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
        "block": {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        },
        "local_relevance_medium_read_only_state_result_object_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_RECORDED",
            "failed_check_count": 0,
            "passed_check_count": 95,
            "result_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_read_only_state_result_object_v0_min",
            "selected_command": "state",
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_state_result_object_recorded": True,
            "selected_state_result_object_recorded": True,
            "state_result_object_created": True,
            "state_result_object_local_only": True,
            "state_result_object_read_only": True,
            "result_level_non_claims_canonical_false": True,
        },
    }
    artifact.update(overrides)
    return artifact


class LocalRelevanceMediumReadOnlyStatePacketBodyExposureTests(unittest.TestCase):
    def make_bundle(self, temp_dir: str) -> dict[str, Any]:
        root = Path(temp_dir)
        boundary_path = root / "state_packet_body_exposure_boundary_v2.json"
        result_object_path = root / "selected_state_result_object.json"
        boundary_artifact = _clean_boundary_artifact()
        result_object_artifact = _clean_state_result_object_artifact()
        request = (
            resolver.build_declared_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_request(
                selected_state_packet_body_exposure_boundary_artifact=boundary_path,
                selected_state_result_object_artifact=result_object_path,
            )
        )
        return {
            "boundary_path": boundary_path,
            "result_object_path": result_object_path,
            "boundary_artifact": boundary_artifact,
            "result_object_artifact": result_object_artifact,
            "request": request,
            "write_boundary_artifact": True,
            "write_result_object_artifact": True,
        }

    def resolve_bundle(
        self,
        temp_dir: str,
        mutator: Callable[[dict[str, Any]], None] | None = None,
    ) -> dict[str, Any]:
        bundle = self.make_bundle(temp_dir)
        if mutator is not None:
            mutator(bundle)
        if bundle.get("write_boundary_artifact", True):
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
        if bundle.get("write_result_object_artifact", True):
            _write_json(bundle["result_object_path"], bundle["result_object_artifact"])
        return resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min(
            bundle["request"]
        )

    def recorded_result(self) -> tuple[dict[str, Any], Path, Path]:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        bundle = self.make_bundle(temp.name)
        _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
        _write_json(bundle["result_object_path"], bundle["result_object_artifact"])
        result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min(
            bundle["request"]
        )
        return result, bundle["boundary_path"], bundle["result_object_path"]

    def summary(self, result: Mapping[str, Any]) -> dict[str, Any]:
        return resolver.build_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_summary(
            result
        )

    def packet_exposure(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result["local_relevance_medium_read_only_state_packet_body_exposure"]
        self.assertIsInstance(value, dict)
        return value

    def statement(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result[
            "local_relevance_medium_read_only_state_packet_body_exposure_statement"
        ]
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: Mapping[str, Any]) -> list[dict[str, Any]]:
        value = result[
            "local_relevance_medium_read_only_state_packet_body_exposure_checks"
        ]
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

    def assert_closure_token_final_posture_false(
        self,
        result: Mapping[str, Any],
    ) -> None:
        non_claims = result["non_claims"]
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)
        summary = self.summary(result)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)

    def assert_no_forbidden_result_posture(self, result: Mapping[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        self.assert_closure_token_final_posture_false(result)
        packet_exposure = result.get(
            "local_relevance_medium_read_only_state_packet_body_exposure"
        )
        if isinstance(packet_exposure, Mapping):
            for field in EXPOSURE_FALSE_FIELDS:
                self.assertIn(field, packet_exposure)
                self.assertIs(packet_exposure[field], False)
                self.assertIsInstance(packet_exposure[field], bool)
            if result.get("outcome") != resolver.OUTCOME_RECORDED:
                self.assertIs(packet_exposure["state_packet_body_exposed"], False)
                self.assertIs(packet_exposure["state_packet_body_exposure_local_only"], False)
                self.assertIs(packet_exposure["state_packet_body_exposure_read_only"], False)

    def assert_packet_exposure_not_wrapper(self, packet_exposure: Mapping[str, Any]) -> None:
        for key in FORBIDDEN_EXPOSURE_WRAPPER_FIELDS:
            self.assertNotIn(key, packet_exposure)

    def assert_packet_exposure_posture(
        self,
        result: Mapping[str, Any],
        boundary_path: Path | str,
        result_object_path: Path | str,
    ) -> None:
        packet_exposure = self.packet_exposure(result)
        self.assertEqual(
            packet_exposure["state_packet_body_exposure_id"],
            "local_relevance_medium_read_only_state_packet_body_exposure_001",
        )
        self.assertEqual(
            packet_exposure["state_packet_body_exposure_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE",
        )
        self.assertEqual(packet_exposure["state_packet_body_exposure_version"], "0.1.0")
        self.assertEqual(
            packet_exposure["state_packet_body_exposure_scope"],
            "SELECTED_STATE_PACKET_BODY_EXPOSURE_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            packet_exposure["basis_state_packet_body_exposure_boundary_artifact"],
            boundary_path,
        )
        self.assertEqual(
            packet_exposure["basis_state_packet_body_exposure_boundary_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            packet_exposure["basis_state_packet_body_exposure_boundary_result_version"],
            "0.1.1",
        )
        self.assertEqual(
            packet_exposure["basis_state_packet_body_exposure_boundary_failed_check_count"],
            0,
        )
        self.assert_same_or_stable_artifact_path(
            packet_exposure["basis_state_result_object_artifact"],
            result_object_path,
        )
        self.assertEqual(
            packet_exposure["basis_state_result_object_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_RECORDED",
        )
        self.assertEqual(packet_exposure["basis_state_result_object_result_version"], "0.1.0")
        self.assertEqual(packet_exposure["basis_state_result_object_failed_check_count"], 0)
        self.assertEqual(packet_exposure["selected_command"], "state")
        self.assertIs(packet_exposure["selected_command_is_state"], True)
        self.assertIs(packet_exposure["selected_state_result_object_recorded"], True)
        self.assertIs(packet_exposure["state_result_object_created"], True)
        self.assertIs(packet_exposure["state_result_object_local_only"], True)
        self.assertIs(packet_exposure["state_result_object_read_only"], True)
        self.assertIs(
            packet_exposure[
                "local_relevance_medium_read_only_state_packet_body_exposure_recorded"
            ],
            True,
        )
        self.assertIs(packet_exposure["state_packet_body_exposed"], True)
        self.assertIs(packet_exposure["state_packet_body_exposure_local_only"], True)
        self.assertIs(packet_exposure["state_packet_body_exposure_read_only"], True)
        for field in EXPOSURE_FALSE_FIELDS:
            self.assertIn(field, packet_exposure)
            self.assertIs(packet_exposure[field], False)
            self.assertIsInstance(packet_exposure[field], bool)
        self.assert_packet_exposure_not_wrapper(packet_exposure)

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
            "resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min",
            "resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_from_path",
            "write_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_result",
            "build_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_STATE_PACKET_BODY_EXPOSURE_TYPE_VALUES",
            "SUPPORTED_STATE_PACKET_BODY_EXPOSURE_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min",
        )
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE",
            resolver.SUPPORTED_STATE_PACKET_BODY_EXPOSURE_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_STATE_PACKET_BODY_EXPOSURE_ONLY",
            resolver.SUPPORTED_STATE_PACKET_BODY_EXPOSURE_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        self.assertIn("raw_full_state_packet_body_exposed", resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("consumed_request_reopened", resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("authorization_token_reused", resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("CONSUMED_REQUEST_REOPENED", resolver.BLOCK_CODES)
        self.assertIn("AUTHORIZATION_TOKEN_REUSED", resolver.BLOCK_CODES)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BLOCKED",
            },
        )

        request = (
            resolver.build_declared_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_request()
        )
        self.assertEqual(request["selected_command"], "state")
        self.assertTrue(
            str(request["selected_state_packet_body_exposure_boundary_artifact"]).endswith(
                "local_relevance_medium_read_only_state_packet_body_exposure_boundary_"
                "reference_review_001__local_relevance_medium_read_only_state_packet_body_"
                "exposure_boundary_v0_min_v2_result.json"
            )
        )
        self.assertTrue(
            str(request["selected_state_result_object_artifact"]).endswith(
                "local_relevance_medium_read_only_state_result_object_reference_review_001__"
                "local_relevance_medium_read_only_state_result_object_v0_min_result.json"
            )
        )
        self.assertIs(request["declared_non_claims"]["consumed_request_reopened"], False)
        self.assertIs(request["declared_non_claims"]["authorization_token_reused"], False)
        self.assertFalse(
            any(
                _path_has_component_prefix(resolver.OUTPUT_ROOT, root)
                for root in FORBIDDEN_OUTPUT_ROOTS
            )
        )

    def test_records_state_packet_body_exposure_from_synthetic_artifacts(self) -> None:
        result, boundary_path, result_object_path = self.recorded_result()
        summary = self.summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            summary["state_packet_body_exposure_id"],
            "local_relevance_medium_read_only_state_packet_body_exposure_001",
        )
        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        self.assert_packet_exposure_posture(result, boundary_path, result_object_path)
        self.assert_statement_true_fields(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_closure_token_final_posture_false(result)
        self.assert_all_emitted_codes_public(result)

    def test_records_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT.exists():
            self.skipTest("default state packet body exposure boundary artifact not present")
        if not DEFAULT_STATE_RESULT_OBJECT_ARTIFACT.exists():
            self.skipTest("default selected-state result object artifact not present")
        request = (
            resolver.build_declared_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_request()
        )
        result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min(
            request
        )
        summary = self.summary(result)
        packet_exposure = self.packet_exposure(result)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(packet_exposure["selected_command"], "state")
        self.assertEqual(
            packet_exposure["state_packet_body_exposure_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE",
        )
        self.assertEqual(
            packet_exposure["state_packet_body_exposure_scope"],
            "SELECTED_STATE_PACKET_BODY_EXPOSURE_ONLY",
        )
        self.assertIs(packet_exposure["selected_state_result_object_recorded"], True)
        self.assertIs(packet_exposure["state_result_object_created"], True)
        self.assertIs(packet_exposure["state_result_object_local_only"], True)
        self.assertIs(packet_exposure["state_result_object_read_only"], True)
        self.assertIs(
            packet_exposure[
                "local_relevance_medium_read_only_state_packet_body_exposure_recorded"
            ],
            True,
        )
        self.assertIs(packet_exposure["state_packet_body_exposed"], True)
        self.assertIs(packet_exposure["state_packet_body_exposure_local_only"], True)
        self.assertIs(packet_exposure["state_packet_body_exposure_read_only"], True)
        self.assert_no_forbidden_result_posture(result)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assert_same_or_stable_artifact_path(
            packet_exposure["basis_state_packet_body_exposure_boundary_artifact"],
            DEFAULT_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT,
        )
        self.assert_same_or_stable_artifact_path(
            packet_exposure["basis_state_result_object_artifact"],
            DEFAULT_STATE_RESULT_OBJECT_ARTIFACT,
        )

    def test_closure_token_blocking_behavior(self) -> None:
        cases: list[tuple[str, str | None, Callable[[dict[str, Any]], None]]] = [
            (
                "top-level consumed request reopened",
                "CONSUMED_REQUEST_REOPENED",
                lambda request: _set(request, "consumed_request_reopened", True),
            ),
            (
                "top-level authorization token reused",
                "AUTHORIZATION_TOKEN_REUSED",
                lambda request: _set(request, "authorization_token_reused", True),
            ),
            (
                "non-claim consumed request reopened",
                "CONSUMED_REQUEST_REOPENED",
                lambda request: _set(
                    request["declared_non_claims"],
                    "consumed_request_reopened",
                    True,
                ),
            ),
            (
                "non-claim authorization token reused",
                "AUTHORIZATION_TOKEN_REUSED",
                lambda request: _set(
                    request["declared_non_claims"],
                    "authorization_token_reused",
                    True,
                ),
            ),
            (
                "missing consumed request non-claim",
                "NON_CLAIM_MISSING_OR_FLIPPED",
                lambda request: _pop(
                    request["declared_non_claims"],
                    "consumed_request_reopened",
                ),
            ),
            (
                "missing authorization token non-claim",
                "NON_CLAIM_MISSING_OR_FLIPPED",
                lambda request: _pop(
                    request["declared_non_claims"],
                    "authorization_token_reused",
                ),
            ),
            (
                "string consumed request non-claim",
                "CONSUMED_REQUEST_REOPENED",
                lambda request: _set(
                    request["declared_non_claims"],
                    "consumed_request_reopened",
                    "false",
                ),
            ),
            (
                "string authorization token non-claim",
                "AUTHORIZATION_TOKEN_REUSED",
                lambda request: _set(
                    request["declared_non_claims"],
                    "authorization_token_reused",
                    "false",
                ),
            ),
            (
                "none consumed request non-claim",
                "NON_CLAIM_MISSING_OR_FLIPPED",
                lambda request: _set(
                    request["declared_non_claims"],
                    "consumed_request_reopened",
                    None,
                ),
            ),
            (
                "none authorization token non-claim",
                "NON_CLAIM_MISSING_OR_FLIPPED",
                lambda request: _set(
                    request["declared_non_claims"],
                    "authorization_token_reused",
                    None,
                ),
            ),
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
            _write_json(bundle["result_object_path"], bundle["result_object_artifact"])
            for name, expected_code, mutator in cases:
                with self.subTest(case=name):
                    request = copy.deepcopy(bundle["request"])
                    mutator(request)
                    result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min(
                        request
                    )
                    self.assert_blocked_common(result)
                    if expected_code is not None:
                        self.assertEqual(self.block_code(result), expected_code)
                    self.assert_closure_token_final_posture_false(result)

    def test_canonicalizes_flipped_required_non_claims_to_false(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
            _write_json(bundle["result_object_path"], bundle["result_object_artifact"])

            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(bundle["request"])
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min(
                        request
                    )
                    self.assert_blocked_common(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_no_forbidden_result_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        def boundary_override(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            def mutate(bundle: dict[str, Any]) -> None:
                bundle["boundary_artifact"][
                    "local_relevance_medium_read_only_state_packet_body_exposure_boundary"
                ][field] = value

            return mutate

        def result_object_override(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            def mutate(bundle: dict[str, Any]) -> None:
                bundle["result_object_artifact"][
                    "local_relevance_medium_read_only_state_result_object"
                ][field] = value

            return mutate

        def boundary_summary_override(
            field: str,
            value: Any,
        ) -> Callable[[dict[str, Any]], None]:
            def mutate(bundle: dict[str, Any]) -> None:
                bundle["boundary_artifact"][
                    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_summary"
                ][field] = value

            return mutate

        def result_object_summary_override(
            field: str,
            value: Any,
        ) -> Callable[[dict[str, Any]], None]:
            def mutate(bundle: dict[str, Any]) -> None:
                bundle["result_object_artifact"][
                    "local_relevance_medium_read_only_state_result_object_summary"
                ][field] = value

            return mutate

        cases: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
            (
                "explicit block intent",
                lambda bundle: _set(
                    bundle["request"],
                    "local_relevance_medium_read_only_state_packet_body_exposure_intent",
                    resolver.INTENT_BLOCK,
                ),
            ),
            (
                "unsupported intent",
                lambda bundle: _set(
                    bundle["request"],
                    "local_relevance_medium_read_only_state_packet_body_exposure_intent",
                    "UNSUPPORTED_INTENT",
                ),
            ),
            (
                "state packet body exposure boundary artifact path missing",
                lambda bundle: _pop(
                    bundle["request"],
                    "selected_state_packet_body_exposure_boundary_artifact",
                ),
            ),
            (
                "state packet body exposure boundary artifact unreadable",
                lambda bundle: _set(
                    bundle["request"],
                    "selected_state_packet_body_exposure_boundary_artifact",
                    str(Path(bundle["boundary_path"]).with_name("missing_boundary.json")),
                ),
            ),
            (
                "state packet body exposure boundary artifact not recorded",
                lambda bundle: _set(bundle["boundary_artifact"], "outcome", "NOT_RECORDED"),
            ),
            (
                "state packet body exposure boundary artifact failed checks present",
                boundary_summary_override("failed_check_count", 1),
            ),
            (
                "state packet body exposure boundary artifact version not 0.1.1",
                boundary_summary_override("result_version", "9.9.9"),
            ),
            (
                "state result object artifact path missing",
                lambda bundle: _pop(
                    bundle["request"],
                    "selected_state_result_object_artifact",
                ),
            ),
            (
                "state result object artifact unreadable",
                lambda bundle: _set(
                    bundle["request"],
                    "selected_state_result_object_artifact",
                    str(Path(bundle["result_object_path"]).with_name("missing_result_object.json")),
                ),
            ),
            (
                "state result object artifact not recorded",
                lambda bundle: _set(
                    bundle["result_object_artifact"],
                    "outcome",
                    "NOT_RECORDED",
                ),
            ),
            (
                "state result object artifact failed checks present",
                result_object_summary_override("failed_check_count", 1),
            ),
            (
                "state result object artifact version not 0.1.0",
                result_object_summary_override("result_version", "9.9.9"),
            ),
            ("selected command missing", lambda bundle: _pop(bundle["request"], "selected_command")),
            (
                "selected command not state",
                lambda bundle: _set(bundle["request"], "selected_command", "lookup first_orientation_locator"),
            ),
            (
                "selected-state result object not recorded",
                result_object_override("selected_state_result_object_recorded", False),
            ),
            ("state result object not created", result_object_override("state_result_object_created", False)),
            ("state result object local only not true", result_object_override("state_result_object_local_only", False)),
            ("state result object read only not true", result_object_override("state_result_object_read_only", False)),
            (
                "state packet body exposure boundary did not allow consideration",
                boundary_override("future_state_packet_body_exposure_may_be_considered", False),
            ),
            (
                "state packet body exposure type missing",
                lambda bundle: _pop(bundle["request"], "state_packet_body_exposure_type"),
            ),
            (
                "state packet body exposure type wrong",
                lambda bundle: _set(
                    bundle["request"],
                    "state_packet_body_exposure_type",
                    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE",
                ),
            ),
            (
                "state packet body exposure scope missing",
                lambda bundle: _pop(bundle["request"], "state_packet_body_exposure_scope"),
            ),
            (
                "state packet body exposure scope wrong",
                lambda bundle: _set(
                    bundle["request"],
                    "state_packet_body_exposure_scope",
                    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY",
                ),
            ),
            (
                "local relevance medium read-only state packet body exposure not recorded",
                lambda bundle: _set(
                    bundle["request"],
                    "local_relevance_medium_read_only_state_packet_body_exposure_not_recorded",
                    True,
                ),
            ),
            (
                "state packet body not exposed",
                lambda bundle: _set(bundle["request"], "state_packet_body_not_exposed", True),
            ),
            (
                "state packet body exposure local only not true",
                lambda bundle: _set(
                    bundle["request"],
                    "state_packet_body_exposure_local_only_not_true",
                    True,
                ),
            ),
            (
                "state packet body exposure read only not true",
                lambda bundle: _set(
                    bundle["request"],
                    "state_packet_body_exposure_read_only_not_true",
                    True,
                ),
            ),
            ("consumed request reopened", lambda bundle: _set(bundle["request"], "consumed_request_reopened", True)),
            ("authorization token reused", lambda bundle: _set(bundle["request"], "authorization_token_reused", True)),
            (
                "required non-claim missing",
                lambda bundle: _pop(
                    bundle["request"]["declared_non_claims"],
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0],
                ),
            ),
        ]
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            cases.append(
                (
                    f"{field} flipped",
                    lambda bundle, field=field: _set(
                        bundle["request"],
                        field,
                        True,
                    ),
                )
            )

        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            boundary_array_path = Path(temp_dir) / "boundary_array.json"
            _write_json(boundary_array_path, [])
            result_object_array_path = Path(temp_dir) / "result_object_array.json"
            _write_json(result_object_array_path, [])

            boundary_array_result = self.resolve_bundle(
                temp_dir,
                lambda changed: _set(
                    changed["request"],
                    "selected_state_packet_body_exposure_boundary_artifact",
                    str(boundary_array_path),
                ),
            )
            self.assert_blocked_common(boundary_array_result)

            result_object_array_result = self.resolve_bundle(
                temp_dir,
                lambda changed: _set(
                    changed["request"],
                    "selected_state_result_object_artifact",
                    str(result_object_array_path),
                ),
            )
            self.assert_blocked_common(result_object_array_result)

        missing_result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min(
            None
        )
        self.assert_blocked_common(missing_result)
        non_mapping_result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min(
            ["not", "a", "mapping"]  # type: ignore[arg-type]
        )
        self.assert_blocked_common(non_mapping_result)

        for name, mutator in cases:
            with self.subTest(case=name):
                with tempfile.TemporaryDirectory() as temp_dir:
                    result = self.resolve_bundle(temp_dir, mutator)
                    self.assert_blocked_common(result)

    def test_official_values_are_preserved(self) -> None:
        result, _boundary_path, _result_object_path = self.recorded_result()
        serialized = json.dumps(result, sort_keys=True)
        packet_exposure = self.packet_exposure(result)

        self.assertEqual(
            packet_exposure["state_packet_body_exposure_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE",
        )
        self.assertEqual(
            packet_exposure["state_packet_body_exposure_scope"],
            "SELECTED_STATE_PACKET_BODY_EXPOSURE_ONLY",
        )
        self.assertEqual(packet_exposure["selected_command"], "state")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        for value in (
            resolver.OUTCOME_RECORDED,
            packet_exposure["state_packet_body_exposure_type"],
            packet_exposure["state_packet_body_exposure_scope"],
            "state",
        ):
            self.assertIn(value, serialized)
        for value in resolver.OUTCOME_FAMILY:
            self.assertIn(value, resolver.OUTCOME_FAMILY)
        self.assertNotIn("[REDACTED", packet_exposure["state_packet_body_exposure_type"])
        self.assertNotIn("[REDACTED", packet_exposure["state_packet_body_exposure_scope"])
        self.assertNotIn("[REDACTED", packet_exposure["selected_command"])

    def test_raw_hidden_hostile_content_containment_and_no_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            bundle["request"]["raw_body"] = HOSTILE_SENTINELS[0]
            bundle["request"]["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            bundle["request"]["nested_payload"] = {
                "raw_state_packet_body": HOSTILE_SENTINELS[2],
                "ordinary_official": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE",
            }
            bundle["boundary_artifact"]["raw_state_packet_body_exposure_boundary_body"] = HOSTILE_SENTINELS[4]
            bundle["boundary_artifact"]["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            bundle["result_object_artifact"]["raw_state_result_object_body"] = HOSTILE_SENTINELS[5]
            bundle["result_object_artifact"]["hidden_repo_state"] = HOSTILE_SENTINELS[-1]

            request_before = copy.deepcopy(bundle["request"])
            boundary_before = copy.deepcopy(bundle["boundary_artifact"])
            result_object_before = copy.deepcopy(bundle["result_object_artifact"])
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
            _write_json(bundle["result_object_path"], bundle["result_object_artifact"])
            result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min(
                bundle["request"]
            )

            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            for sentinel in HOSTILE_SENTINELS:
                self.assertNotIn(sentinel, serialized)
            self.assertIn(
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE",
                serialized,
            )
            self.assertIn("SELECTED_STATE_PACKET_BODY_EXPOSURE_ONLY", serialized)
            self.assertIn("state", serialized)
            self.assert_no_forbidden_result_posture(result)
            self.assertEqual(bundle["request"], request_before)
            self.assertEqual(bundle["boundary_artifact"], boundary_before)
            self.assertEqual(bundle["result_object_artifact"], result_object_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            bundle = self.make_bundle(temp_dir)
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
            _write_json(bundle["result_object_path"], bundle["result_object_artifact"])
            request_path = root / "request.json"
            _write_json(request_path, bundle["request"])

            result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_from_path(
                request_path
            )
            summary = self.summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], resolver.OUTCOME_BLOCKED)

            array_path = root / "request_array.json"
            _write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)

            missing_result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_from_path(
                root / "missing_request.json"
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)

            output_root = root / "local_relevance_medium_read_only_state_packet_body_exposure_v0_min"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                output_path = resolver.write_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_result(
                    result
                )
                second_output_path = resolver.write_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_result(
                    result
                )

            self.assertTrue(output_path.parent.exists())
            self.assertTrue(output_path.exists())
            self.assertTrue(second_output_path.exists())
            self.assertNotEqual(output_path, second_output_path)
            self.assertTrue(second_output_path.stem.endswith("_001"))
            self.assertEqual(
                json.loads(output_path.read_text(encoding="utf-8"))["outcome"],
                resolver.OUTCOME_RECORDED,
            )
            self.assertIn(
                "local_relevance_medium_read_only_state_packet_body_exposure_v0_min",
                str(output_path),
            )
            self.assert_path_not_under_forbidden_roots(output_path)
            self.assert_path_not_under_forbidden_roots(second_output_path)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            bundle["request"]["nested_payload"] = {
                "hidden_repo_state": HOSTILE_SENTINELS[-1],
                "raw_state_packet_body": HOSTILE_SENTINELS[2],
            }
            request_before = copy.deepcopy(bundle["request"])
            non_claims_before = copy.deepcopy(bundle["request"]["declared_non_claims"])
            boundary_path_before = bundle["request"][
                "selected_state_packet_body_exposure_boundary_artifact"
            ]
            result_object_path_before = bundle["request"]["selected_state_result_object_artifact"]
            selected_command_before = bundle["request"]["selected_command"]
            exposure_type_before = bundle["request"]["state_packet_body_exposure_type"]
            exposure_scope_before = bundle["request"]["state_packet_body_exposure_scope"]
            closure_token_before = (
                bundle["request"]["declared_non_claims"]["consumed_request_reopened"],
                bundle["request"]["declared_non_claims"]["authorization_token_reused"],
            )
            boundary_before = copy.deepcopy(bundle["boundary_artifact"])
            result_object_before = copy.deepcopy(bundle["result_object_artifact"])
            _write_json(bundle["boundary_path"], bundle["boundary_artifact"])
            _write_json(bundle["result_object_path"], bundle["result_object_artifact"])

            result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min(
                bundle["request"]
            )

            self.assertEqual(bundle["request"], request_before)
            self.assertEqual(bundle["request"]["declared_non_claims"], non_claims_before)
            self.assertEqual(
                bundle["request"]["selected_state_packet_body_exposure_boundary_artifact"],
                boundary_path_before,
            )
            self.assertEqual(
                bundle["request"]["selected_state_result_object_artifact"],
                result_object_path_before,
            )
            self.assertEqual(bundle["request"]["selected_command"], selected_command_before)
            self.assertEqual(
                bundle["request"]["state_packet_body_exposure_type"],
                exposure_type_before,
            )
            self.assertEqual(
                bundle["request"]["state_packet_body_exposure_scope"],
                exposure_scope_before,
            )
            self.assertEqual(
                (
                    bundle["request"]["declared_non_claims"]["consumed_request_reopened"],
                    bundle["request"]["declared_non_claims"]["authorization_token_reused"],
                ),
                closure_token_before,
            )
            self.assertEqual(bundle["boundary_artifact"], boundary_before)
            self.assertEqual(bundle["result_object_artifact"], result_object_before)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)

    def test_predecessor_failure_preservation(self) -> None:
        result, _boundary_path, _result_object_path = self.recorded_result()
        summary = self.summary(result)
        statement = self.statement(result)
        non_claims = result["non_claims"]

        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["predecessor_failure_not_repaired"], True)
        self.assertIs(statement["predecessor_failure_not_hidden"], True)
        self.assertIs(statement["predecessor_failure_not_claimed_passed"], True)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        self.assertIs(non_claims["predecessor_failure_repaired"], False)
        self.assertIs(non_claims["predecessor_failure_hidden"], False)
        self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)

        with tempfile.TemporaryDirectory() as temp_dir:
            consumed = self.resolve_bundle(
                temp_dir,
                lambda bundle: _set(bundle["request"], "consumed_request_reopened", True),
            )
            self.assert_blocked_common(consumed)
            self.assertEqual(self.block_code(consumed), "CONSUMED_REQUEST_REOPENED")
        with tempfile.TemporaryDirectory() as temp_dir:
            reused = self.resolve_bundle(
                temp_dir,
                lambda bundle: _set(bundle["request"], "authorization_token_reused", True),
            )
            self.assert_blocked_common(reused)
            self.assertEqual(self.block_code(reused), "AUTHORIZATION_TOKEN_REUSED")


if __name__ == "__main__":
    unittest.main()
