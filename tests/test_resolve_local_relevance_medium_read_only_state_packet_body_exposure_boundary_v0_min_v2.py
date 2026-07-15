"""Tests for the selected-state packet body exposure boundary v2 resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY object.
The v2 resolver is a successor for the v0 closure-token gap: consumed request
reopening and authorization token reuse must block while result-level
non-claims remain canonical false. The v0 resolver/test remain preserved
failed-lineage evidence; this suite does not repair, hide, rename, or delete
them.
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

import resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2 as resolver  # noqa: E402


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
    "state_packet_body_exposure_boundary_v0_min_v2"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_metadata",
    "declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary_question",
    "selected_state_result_object_artifact_basis",
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary",
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_checks",
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_statement",
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_summary",
)

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_summary",
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_metadata",
)

BOUNDARY_OBJECT_FALSE_FIELDS = (
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

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_recorded",
    "basis_state_result_object_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_state_result_object_recorded",
    "state_result_object_created",
    "state_result_object_local_only",
    "state_result_object_read_only",
    "future_state_packet_body_exposure_may_be_considered",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
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
        "selected_state_payload_return_recorded": True,
        "state_payload_returned": True,
        "state_payload_return_local_only": True,
        "state_payload_return_read_only": True,
        "state_result_object_created": True,
        "state_result_object_local_only": True,
        "state_result_object_read_only": True,
    }
    for field in BOUNDARY_OBJECT_FALSE_FIELDS:
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
            "selected_state_payload_return_recorded": True,
            "state_payload_returned": True,
            "state_payload_return_local_only": True,
            "state_payload_return_read_only": True,
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


class LocalRelevanceMediumReadOnlyStatePacketBodyExposureBoundaryV2Tests(
    unittest.TestCase
):
    def make_bundle(self, temp_dir: str) -> dict[str, Any]:
        root = Path(temp_dir)
        artifact_path = root / "selected_state_result_object.json"
        artifact = _clean_state_result_object_artifact()
        request = (
            resolver.build_declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_request(
                selected_state_result_object_artifact=artifact_path,
            )
        )
        return {
            "artifact_path": artifact_path,
            "artifact": artifact,
            "request": request,
            "write_artifact": True,
        }

    def resolve_bundle(
        self,
        temp_dir: str,
        mutator: Callable[[dict[str, Any]], None] | None = None,
    ) -> dict[str, Any]:
        bundle = self.make_bundle(temp_dir)
        if mutator is not None:
            mutator(bundle)
        if bundle.get("write_artifact", True):
            _write_json(bundle["artifact_path"], bundle["artifact"])
        return resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2(
            bundle["request"]
        )

    def recorded_result(self) -> tuple[dict[str, Any], Path]:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        bundle = self.make_bundle(temp.name)
        _write_json(bundle["artifact_path"], bundle["artifact"])
        result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2(
            bundle["request"]
        )
        return result, bundle["artifact_path"]

    def summary(self, result: Mapping[str, Any]) -> dict[str, Any]:
        return resolver.build_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_summary(
            result
        )

    def boundary(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result["local_relevance_medium_read_only_state_packet_body_exposure_boundary"]
        self.assertIsInstance(value, dict)
        return value

    def statement(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result[
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_statement"
        ]
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: Mapping[str, Any]) -> list[dict[str, Any]]:
        value = result[
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_checks"
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
        self.assertIs(summary["consumed_request_reopened"], False)
        self.assertIs(summary["authorization_token_reused"], False)

    def assert_no_forbidden_result_posture(self, result: Mapping[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        self.assert_closure_token_final_posture_false(result)
        boundary = result.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary"
        )
        if isinstance(boundary, Mapping):
            for field in BOUNDARY_OBJECT_FALSE_FIELDS:
                self.assertIn(field, boundary)
                self.assertIs(boundary[field], False)
                self.assertIsInstance(boundary[field], bool)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(result["non_claims"][field], False)

    def assert_boundary_not_wrapper(self, boundary: Mapping[str, Any]) -> None:
        for key in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(key, boundary)

    def assert_boundary_posture(
        self,
        result: Mapping[str, Any],
        artifact_path: Path | str,
    ) -> None:
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["boundary_id"],
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_001",
        )
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY",
        )
        self.assertEqual(boundary["boundary_version"], "0.1.1")
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            boundary["basis_state_result_object_artifact"],
            artifact_path,
        )
        self.assertEqual(
            boundary["basis_state_result_object_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_RECORDED",
        )
        self.assertEqual(boundary["basis_state_result_object_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_state_result_object_failed_check_count"], 0)
        self.assertEqual(boundary["selected_command"], "state")
        self.assertIs(boundary["selected_command_is_state"], True)
        self.assertIs(boundary["selected_state_result_object_recorded"], True)
        self.assertIs(boundary["state_result_object_created"], True)
        self.assertIs(boundary["state_result_object_local_only"], True)
        self.assertIs(boundary["state_result_object_read_only"], True)
        self.assertIs(
            boundary["future_state_packet_body_exposure_may_be_considered"],
            True,
        )
        for field in BOUNDARY_OBJECT_FALSE_FIELDS:
            self.assertIn(field, boundary)
            self.assertIs(boundary[field], False)
            self.assertIsInstance(boundary[field], bool)
        self.assert_boundary_not_wrapper(boundary)

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
            "resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2",
            "resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_from_path",
            "write_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_result",
            "build_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_summary",
            "build_declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_request",
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

        self.assertEqual(resolver.RESULT_VERSION, "0.1.1")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2",
        )
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY",
            resolver.SUPPORTED_BOUNDARY_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY",
            resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        self.assertIn("consumed_request_reopened", resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("authorization_token_reused", resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("CONSUMED_REQUEST_REOPENED", resolver.BLOCK_CODES)
        self.assertIn("AUTHORIZATION_TOKEN_REUSED", resolver.BLOCK_CODES)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BLOCKED",
            },
        )

        request = (
            resolver.build_declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_request()
        )
        self.assertEqual(request["selected_command"], "state")
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

    def test_records_boundary_from_synthetic_state_result_object_artifact(self) -> None:
        result, artifact_path = self.recorded_result()
        summary = self.summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.1")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            summary["boundary_id"],
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_001",
        )
        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        self.assert_boundary_posture(result, artifact_path)
        self.assert_statement_true_fields(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_closure_token_final_posture_false(result)
        self.assert_all_emitted_codes_public(result)

    def test_records_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_STATE_RESULT_OBJECT_ARTIFACT.exists():
            self.skipTest("default selected-state result object artifact not present")
        request = (
            resolver.build_declared_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_request()
        )
        result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2(
            request
        )
        summary = self.summary(result)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assert_boundary_posture(result, DEFAULT_STATE_RESULT_OBJECT_ARTIFACT)
        boundary = self.boundary(result)
        self.assertEqual(boundary["selected_command"], "state")
        self.assertIs(boundary["future_state_packet_body_exposure_may_be_considered"], True)
        self.assert_no_forbidden_result_posture(result)

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
            _write_json(bundle["artifact_path"], bundle["artifact"])
            for name, expected_code, mutator in cases:
                with self.subTest(case=name):
                    request = copy.deepcopy(bundle["request"])
                    mutator(request)
                    result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2(
                        request
                    )
                    self.assert_blocked_common(result)
                    if expected_code is not None:
                        self.assertEqual(self.block_code(result), expected_code)
                    self.assert_closure_token_final_posture_false(result)

    def test_canonicalizes_flipped_required_non_claims_to_false(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            _write_json(bundle["artifact_path"], bundle["artifact"])

            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(bundle["request"])
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2(
                        request
                    )
                    self.assert_blocked_common(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_no_forbidden_result_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        def artifact_override(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            def mutate(bundle: dict[str, Any]) -> None:
                bundle["artifact"]["local_relevance_medium_read_only_state_result_object"][
                    field
                ] = value

            return mutate

        def top_level_artifact_override(
            field: str,
            value: Any,
        ) -> Callable[[dict[str, Any]], None]:
            def mutate(bundle: dict[str, Any]) -> None:
                bundle["artifact"][field] = value

            return mutate

        cases: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
            (
                "explicit block intent",
                lambda bundle: _set(
                    bundle["request"],
                    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_intent",
                    resolver.INTENT_BLOCK,
                ),
            ),
            (
                "unsupported intent",
                lambda bundle: _set(
                    bundle["request"],
                    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_intent",
                    "UNSUPPORTED_INTENT",
                ),
            ),
            (
                "artifact path missing",
                lambda bundle: _pop(bundle["request"], "selected_state_result_object_artifact"),
            ),
            (
                "artifact unreadable",
                lambda bundle: _set(
                    bundle["request"],
                    "selected_state_result_object_artifact",
                    str(Path(bundle["artifact_path"]).with_name("missing.json")),
                ),
            ),
            (
                "artifact not recorded",
                top_level_artifact_override("outcome", "NOT_RECORDED"),
            ),
            (
                "artifact failed checks present",
                lambda bundle: _set(
                    bundle["artifact"][
                        "local_relevance_medium_read_only_state_result_object_summary"
                    ],
                    "failed_check_count",
                    1,
                ),
            ),
            (
                "artifact version not 0.1.0",
                lambda bundle: _set(
                    bundle["artifact"][
                        "local_relevance_medium_read_only_state_result_object_summary"
                    ],
                    "result_version",
                    "9.9.9",
                ),
            ),
            ("selected command missing", lambda bundle: _pop(bundle["request"], "selected_command")),
            (
                "selected command not state",
                lambda bundle: _set(bundle["request"], "selected_command", "lookup first_orientation_locator"),
            ),
            (
                "selected-state result object not recorded",
                artifact_override(
                    "local_relevance_medium_read_only_state_result_object_recorded",
                    False,
                ),
            ),
            ("state result object not created", artifact_override("state_result_object_created", False)),
            ("state result object local only not true", artifact_override("state_result_object_local_only", False)),
            ("state result object read only not true", artifact_override("state_result_object_read_only", False)),
            (
                "future state packet body exposure may not be considered",
                lambda bundle: _set(
                    bundle["request"],
                    "future_state_packet_body_exposure_may_be_considered",
                    False,
                ),
            ),
            ("boundary type missing", lambda bundle: _pop(bundle["request"], "boundary_type")),
            (
                "boundary type wrong",
                lambda bundle: _set(
                    bundle["request"],
                    "boundary_type",
                    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE",
                ),
            ),
            ("boundary scope missing", lambda bundle: _pop(bundle["request"], "boundary_scope")),
            (
                "boundary scope wrong",
                lambda bundle: _set(bundle["request"], "boundary_scope", "STATE_PACKET_BODY_EXPOSURE_ONLY"),
            ),
            ("predecessor failure hidden", lambda bundle: _set(bundle["request"], "predecessor_failure_hidden", True)),
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
                        bundle["request"]["declared_non_claims"],
                        field,
                        True,
                    ),
                )
            )

        with tempfile.TemporaryDirectory() as temp_dir:
            array_artifact_path = Path(temp_dir) / "array_artifact.json"
            _write_json(array_artifact_path, [])
            array_result = self.resolve_bundle(
                temp_dir,
                lambda bundle: _set(
                    bundle["request"],
                    "selected_state_result_object_artifact",
                    str(array_artifact_path),
                ),
            )
            self.assert_blocked_common(array_result)

        missing_result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2(
            None
        )
        self.assert_blocked_common(missing_result)
        non_mapping_result = (
            resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2(
                ["not", "a", "mapping"]  # type: ignore[arg-type]
            )
        )
        self.assert_blocked_common(non_mapping_result)

        for name, mutator in cases:
            with self.subTest(case=name):
                with tempfile.TemporaryDirectory() as temp_dir:
                    result = self.resolve_bundle(temp_dir, mutator)
                    self.assert_blocked_common(result)

    def test_official_values_are_preserved(self) -> None:
        result, _artifact_path = self.recorded_result()
        serialized = json.dumps(result, sort_keys=True)
        boundary = self.boundary(result)

        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY",
        )
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY",
        )
        self.assertEqual(boundary["selected_command"], "state")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        for value in (
            resolver.OUTCOME_RECORDED,
            boundary["boundary_type"],
            boundary["boundary_scope"],
            "state",
        ):
            self.assertIn(value, serialized)
        for value in resolver.OUTCOME_FAMILY:
            self.assertIn(value, resolver.OUTCOME_FAMILY)
        self.assertNotIn("[REDACTED", boundary["boundary_type"])
        self.assertNotIn("[REDACTED", boundary["boundary_scope"])
        self.assertNotIn("[REDACTED", boundary["selected_command"])

    def test_raw_hidden_hostile_content_containment_and_no_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle = self.make_bundle(temp_dir)
            bundle["request"]["raw_body"] = HOSTILE_SENTINELS[0]
            bundle["request"]["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            bundle["request"]["nested_payload"] = {
                "raw_state_packet_body": HOSTILE_SENTINELS[2],
                "ordinary_official": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY",
            }
            bundle["artifact"]["raw_state_packet_body"] = HOSTILE_SENTINELS[2]
            bundle["artifact"]["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            bundle["artifact"]["local_relevance_medium_read_only_state_result_object"][
                "raw_state_result_object_body"
            ] = HOSTILE_SENTINELS[4]

            request_before = copy.deepcopy(bundle["request"])
            artifact_before = copy.deepcopy(bundle["artifact"])
            _write_json(bundle["artifact_path"], bundle["artifact"])
            result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2(
                bundle["request"]
            )

            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            for sentinel in HOSTILE_SENTINELS:
                self.assertNotIn(sentinel, serialized)
            self.assertIn(
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY",
                serialized,
            )
            self.assertIn("SELECTED_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY", serialized)
            self.assertIn("state", serialized)
            self.assert_no_forbidden_result_posture(result)
            self.assertEqual(bundle["request"], request_before)
            self.assertEqual(bundle["artifact"], artifact_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            bundle = self.make_bundle(temp_dir)
            _write_json(bundle["artifact_path"], bundle["artifact"])
            request_path = root / "request.json"
            _write_json(request_path, bundle["request"])

            result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_from_path(
                request_path
            )
            summary = self.summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.1")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], resolver.OUTCOME_BLOCKED)

            array_path = root / "request_array.json"
            _write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)

            missing_result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_from_path(
                root / "missing_request.json"
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)

            output_root = root / "local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                output_path = resolver.write_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_result(
                    result
                )
                second_output_path = resolver.write_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2_result(
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
                "local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2",
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
            artifact_path_before = bundle["request"]["selected_state_result_object_artifact"]
            selected_command_before = bundle["request"]["selected_command"]
            boundary_type_before = bundle["request"]["boundary_type"]
            boundary_scope_before = bundle["request"]["boundary_scope"]
            closure_token_before = (
                bundle["request"]["declared_non_claims"]["consumed_request_reopened"],
                bundle["request"]["declared_non_claims"]["authorization_token_reused"],
            )
            artifact_before = copy.deepcopy(bundle["artifact"])
            _write_json(bundle["artifact_path"], bundle["artifact"])

            result = resolver.resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2(
                bundle["request"]
            )

            self.assertEqual(bundle["request"], request_before)
            self.assertEqual(bundle["request"]["declared_non_claims"], non_claims_before)
            self.assertEqual(
                bundle["request"]["selected_state_result_object_artifact"],
                artifact_path_before,
            )
            self.assertEqual(bundle["request"]["selected_command"], selected_command_before)
            self.assertEqual(bundle["request"]["boundary_type"], boundary_type_before)
            self.assertEqual(bundle["request"]["boundary_scope"], boundary_scope_before)
            self.assertEqual(
                (
                    bundle["request"]["declared_non_claims"]["consumed_request_reopened"],
                    bundle["request"]["declared_non_claims"]["authorization_token_reused"],
                ),
                closure_token_before,
            )
            self.assertEqual(bundle["artifact"], artifact_before)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)

    def test_predecessor_failure_preservation(self) -> None:
        result, _artifact_path = self.recorded_result()
        summary = self.summary(result)
        non_claims = result["non_claims"]

        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["predecessor_failure_not_repaired"], True)
        self.assertIs(summary["predecessor_failure_not_hidden"], True)
        self.assertIs(summary["predecessor_failure_not_claimed_passed"], True)
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
