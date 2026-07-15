"""Tests for the local read-only operation execution boundary resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY object. It
verifies that the resolver reads one clean selected-state operation permission
artifact and records one local read-only selected-state
operation-execution-consideration boundary only.

The suite does not create or perform operation execution behavior, runtime
permission, public API, participant-facing interface, distributed behavior,
general operation permission, general lookup permission, arbitrary lookup
permission, unsupported-command permission, unsupported-key permission, a new
lookup entry beyond the already bounded selected-state lookup result object,
registry, search, query surface, ranking, scoring, priority, validity judgment,
truth judgment, authority judgment, currentness judgment, repeated reception
permission, arbitrary reception, feed, new signal, new entry, new relevance
object beyond the already bounded selected-state lookup result object, new
index entry, filesystem discovery, source transfer, source receipt,
participation, runtime permission, or follow-on work.
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

import resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min as resolver  # noqa: E402


DEFAULT_OPERATION_PERMISSION_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_permission_v0_min/"
    "local_relevance_medium_read_only_operation_permission_reference_review_001__"
    "local_relevance_medium_read_only_operation_permission_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_execution_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_permission_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_permission_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_result_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_performed_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_performed_boundary_v0_min"),
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
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_loop_v0_min"),
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_operation_execution_boundary_metadata",
    "declared_local_relevance_medium_read_only_operation_execution_boundary_question",
    "selected_operation_permission_artifact_basis",
    "local_relevance_medium_read_only_operation_execution_boundary",
    "local_relevance_medium_read_only_operation_execution_boundary_checks",
    "local_relevance_medium_read_only_operation_execution_boundary_statement",
    "local_relevance_medium_read_only_operation_execution_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_operation_execution_boundary_summary",
)

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_operation_execution_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_operation_execution_boundary_summary",
    "local_relevance_medium_read_only_operation_execution_boundary_metadata",
)

BOUNDARY_FALSE_FIELDS = (
    "operation_execution_created",
    "operation_execution_performed",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "general_operation_permission_created",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BOUNDARY_BODY_MUST_NOT_RETURN",
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

OFFICIAL_STRINGS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY",
    "SELECTED_OPERATION_EXECUTION_CONSIDERATION_ONLY",
    "state",
)


class LocalRelevanceMediumReadOnlyOperationExecutionBoundaryResolverTests(
    unittest.TestCase
):
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
        return f"{safe}.json"

    def write_json(self, path: Path, data: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def synthetic_operation_permission_artifact(self) -> dict[str, Any]:
        operation_permission = {
            "operation_permission_id": "local_relevance_medium_read_only_operation_permission_001",
            "operation_permission_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION",
            "operation_permission_version": "0.1.0",
            "operation_permission_scope": "SELECTED_OPERATION_PERMISSION_ONLY",
            "selected_command": "state",
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_operation_permission_recorded": True,
            "selected_operation_permission_recorded": True,
            "operation_permission_created": True,
            "operation_permission_local_only": True,
            "operation_permission_read_only": True,
        }
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            operation_permission[key] = False
        statement = {
            "local_relevance_medium_read_only_operation_permission_recorded": True,
            "selected_command_preserved": True,
            "selected_command_is_state": True,
            "selected_operation_permission_recorded": True,
            "operation_permission_created": True,
            "operation_permission_local_only": True,
            "operation_permission_read_only": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        summary = {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 90,
            "selected_command": "state",
            **statement,
        }
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            summary[key] = False
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 90,
            "local_relevance_medium_read_only_operation_permission_metadata": {
                "result_version": "0.1.0",
                "resolver_module": "resolve_local_relevance_medium_read_only_operation_permission_v0_min",
            },
            "local_relevance_medium_read_only_operation_permission": operation_permission,
            "local_relevance_medium_read_only_operation_permission_statement": statement,
            "local_relevance_medium_read_only_operation_permission_checks": [],
            "local_relevance_medium_read_only_operation_permission_summary": summary,
            "non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
        }

    def write_synthetic_operation_permission_artifact(
        self,
        directory: Path,
        name: str = "clean",
        mutator: Callable[[dict[str, Any]], None] | None = None,
        payload: Any | None = None,
    ) -> tuple[Path, dict[str, Any]]:
        artifact = self.synthetic_operation_permission_artifact()
        if mutator is not None:
            mutator(artifact)
        path = directory / self.safe_json_filename(f"{name}_operation_permission")
        self.write_json(path, artifact if payload is None else payload)
        return path, artifact

    def valid_request(self, operation_permission_path: Path) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_operation_execution_boundary_v0_min_request(
            selected_operation_permission_artifact=operation_permission_path
        )

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get(
            "local_relevance_medium_read_only_operation_execution_boundary_checks"
        )
        self.assertIsInstance(checks, list)
        return checks

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        boundary = result.get(
            "local_relevance_medium_read_only_operation_execution_boundary"
        )
        self.assertIsInstance(boundary, Mapping)
        return boundary

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get(
            "local_relevance_medium_read_only_operation_execution_boundary_statement"
        )
        self.assertIsInstance(statement, Mapping)
        return statement

    def non_claims(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        return non_claims

    def block_code(self, result: Mapping[str, Any]) -> Any:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

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
        if actual_path.exists() or expected_path.exists():
            self.assertEqual(actual_path.resolve(), expected_path.resolve())
            return
        self.assertTrue(str(actual).endswith(expected_path.name))

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                emitted = check.get(key)
                if emitted is not None:
                    self.assertIn(emitted, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = self.non_claims(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)

    def assert_operation_execution_boundary_non_claims(
        self,
        result: Mapping[str, Any],
    ) -> None:
        boundary = self.boundary(result)
        for key in BOUNDARY_FALSE_FIELDS:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False)
        self.assertIs(self.non_claims(result)["source_created"], False)
        self.assertIs(self.non_claims(result)["deployment_created"], False)
        self.assertIs(self.non_claims(result)["public_release_created"], False)
        self.assertIs(self.non_claims(result)["broader_reusable_permission_created"], False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_operation_execution_boundary_non_claims(result)

    def assert_boundary_not_wrapper_confused(
        self,
        boundary: Mapping[str, Any],
    ) -> None:
        for field in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(field, boundary)

    def assert_boundary_recorded_posture(
        self,
        result: Mapping[str, Any],
        operation_permission_path: Path,
    ) -> None:
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["boundary_id"],
            "local_relevance_medium_read_only_operation_execution_boundary_001",
        )
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY",
        )
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_OPERATION_EXECUTION_CONSIDERATION_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            boundary["basis_operation_permission_artifact"],
            operation_permission_path,
        )
        self.assertEqual(
            boundary["basis_operation_permission_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_RECORDED",
        )
        self.assertEqual(boundary["basis_operation_permission_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_operation_permission_failed_check_count"], 0)
        expected_true = (
            "selected_command_is_state",
            "selected_operation_permission_recorded",
            "operation_permission_created",
            "operation_permission_local_only",
            "operation_permission_read_only",
            "future_operation_execution_may_be_considered",
        )
        self.assertEqual(boundary["selected_command"], "state")
        for key in expected_true:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], True)
            self.assertIsInstance(boundary[key], bool)
        self.assert_operation_execution_boundary_non_claims(result)
        self.assert_boundary_not_wrapper_confused(boundary)

    def assert_statement_recorded_posture(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        for key in (
            "local_relevance_medium_read_only_operation_execution_boundary_recorded",
            "basis_operation_permission_artifact_preserved",
            "selected_command_preserved",
            "selected_command_is_state",
            "selected_operation_permission_recorded",
            "operation_permission_created",
            "operation_permission_local_only",
            "operation_permission_read_only",
            "future_operation_execution_may_be_considered",
            "consumed_request_token_remains_closed",
            "authorization_token_reuse_blocked",
            "predecessor_failure_evidence_preserved",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIn(key, statement)
            self.assertIs(statement[key], True)
            self.assertIsInstance(statement[key], bool)

    def assert_blocked_non_creation_posture(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in BOUNDARY_FALSE_FIELDS:
            self.assertIs(boundary.get(key), False)
        for key in (
            "source_created",
            "deployment_created",
            "public_release_created",
            "broader_reusable_permission_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "adoption_created",
            "receiving_context_governance_created",
            "publication_flow_created",
        ):
            self.assertIs(self.non_claims(result)[key], False)

    def assert_not_under_forbidden_roots(self, output_path: Path) -> None:
        output_resolved = Path(output_path).resolve()
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            forbidden_resolved = (REPO_ROOT / forbidden).resolve()
            self.assertFalse(
                output_resolved == forbidden_resolved
                or forbidden_resolved in output_resolved.parents,
                f"{output_path} wrote under forbidden root {forbidden}",
            )

    def assert_no_hostile_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_operation_execution_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_operation_execution_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_operation_execution_boundary_v0_min_request",
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
            "resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min",
        )
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY",
            resolver.SUPPORTED_BOUNDARY_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_OPERATION_EXECUTION_CONSIDERATION_ONLY",
            resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        for key in (
            "operation_execution_created",
            "operation_execution_performed",
            "runtime_permission_created",
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
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        request = (
            resolver.build_declared_local_relevance_medium_read_only_operation_execution_boundary_v0_min_request()
        )
        self.assertTrue(
            request["selected_operation_permission_artifact"].endswith(
                "local_relevance_medium_read_only_operation_permission_reference_review_001__"
                "local_relevance_medium_read_only_operation_permission_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], "state")
        self.assertIs(request["declared_non_claims"]["consumed_request_reopened"], False)
        self.assertIs(request["declared_non_claims"]["authorization_token_reused"], False)
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            self.assertNotEqual(Path(resolver.OUTPUT_ROOT), forbidden)

    def test_successful_recorded_result_from_synthetic_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_permission_path, _ = self.write_synthetic_operation_permission_artifact(
                root
            )
            request = self.valid_request(operation_permission_path)

            result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min(
                request
            )

            self.assertIsInstance(result, dict)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.failed_check_count(result), 0)
            self.assert_not_blocked(result)
            summary = result[
                "local_relevance_medium_read_only_operation_execution_boundary_summary"
            ]
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min",
            )
            self.assertGreater(self.passed_check_count(result), 0)
            self.assertEqual(
                self.boundary(result)["boundary_id"],
                "local_relevance_medium_read_only_operation_execution_boundary_001",
            )
            for section in EXPECTED_WRAPPER_SECTIONS:
                self.assertIn(section, result)
            self.assert_boundary_recorded_posture(result, operation_permission_path)
            self.assert_statement_recorded_posture(result)
            self.assert_canonical_false_non_claims(result)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_OPERATION_PERMISSION_ARTIFACT.exists():
            self.skipTest("default operation permission artifact is not present")

        request = resolver.build_declared_local_relevance_medium_read_only_operation_execution_boundary_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min(
            request
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        boundary = self.boundary(result)
        self.assertEqual(boundary["selected_command"], "state")
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY",
        )
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_OPERATION_EXECUTION_CONSIDERATION_ONLY",
        )
        for key in (
            "selected_operation_permission_recorded",
            "operation_permission_created",
            "operation_permission_local_only",
            "operation_permission_read_only",
            "future_operation_execution_may_be_considered",
        ):
            self.assertIs(boundary[key], True)
        for key in (
            "operation_execution_created",
            "operation_execution_performed",
            "runtime_permission_created",
            "public_api_created",
            "distributed_network_behavior_created",
            "general_operation_permission_created",
            "general_lookup_permission_created",
            "follow_on_work_authorized",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(boundary[key], False)
        self.assertIs(self.statement(result)["predecessor_failure_evidence_preserved"], True)
        self.assert_same_or_stable_artifact_path(
            boundary["basis_operation_permission_artifact"],
            DEFAULT_OPERATION_PERMISSION_ARTIFACT,
        )

    def test_closure_token_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_permission_path, _ = self.write_synthetic_operation_permission_artifact(
                root
            )
            base_request = self.valid_request(operation_permission_path)
            cases: list[tuple[str, Callable[[dict[str, Any]], None], str]] = [
                (
                    "top-level consumed_request_reopened true",
                    lambda request: request.__setitem__("consumed_request_reopened", True),
                    "CONSUMED_REQUEST_REOPENED",
                ),
                (
                    "top-level authorization_token_reused true",
                    lambda request: request.__setitem__("authorization_token_reused", True),
                    "AUTHORIZATION_TOKEN_REUSED",
                ),
                (
                    "declared consumed_request_reopened true",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "consumed_request_reopened", True
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "declared authorization_token_reused true",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "authorization_token_reused", True
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "remove declared consumed_request_reopened",
                    lambda request: request["declared_non_claims"].pop(
                        "consumed_request_reopened"
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "remove declared authorization_token_reused",
                    lambda request: request["declared_non_claims"].pop(
                        "authorization_token_reused"
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "declared consumed_request_reopened string false",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "consumed_request_reopened", "false"
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "declared authorization_token_reused string false",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "authorization_token_reused", "false"
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "declared consumed_request_reopened none",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "consumed_request_reopened", None
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "declared authorization_token_reused none",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "authorization_token_reused", None
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
            ]
            for name, mutator, expected_code in cases:
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutator(request)
                    result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assertIs(self.non_claims(result)["consumed_request_reopened"], False)
                    self.assertIs(self.non_claims(result)["authorization_token_reused"], False)
                    self.assert_blocked_non_creation_posture(result)

    def test_required_false_non_claim_canonicalization_blocks_flipped_inputs(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_permission_path, _ = self.write_synthetic_operation_permission_artifact(
                root
            )
            base_request = self.valid_request(operation_permission_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(self.non_claims(result)[key], False)
                    self.assert_canonical_false_non_claims(result)
                    self.assertIsNot(self.non_claims(result)[key], True)
                    self.assert_blocked_non_creation_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        def set_key(key: str, value: Any = True) -> Callable[[dict[str, Any]], None]:
            return lambda request: request.__setitem__(key, value)

        def remove_key(key: str) -> Callable[[dict[str, Any]], None]:
            return lambda request: request.pop(key, None)

        def set_declared_non_claim(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
            return lambda request: request["declared_non_claims"].__setitem__(key, value)

        cases: list[tuple[str, Callable[[dict[str, Any]], None] | str]] = [
            ("explicit block intent", set_key("local_relevance_medium_read_only_operation_execution_boundary_intent", "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY")),
            ("missing request", "empty_request"),
            ("non-mapping request", "non_mapping"),
            ("unsupported intent", set_key("local_relevance_medium_read_only_operation_execution_boundary_intent", "UNSUPPORTED")),
            ("operation permission artifact path missing", set_key("selected_operation_permission_artifact", "")),
            ("operation permission artifact unreadable", "missing_artifact"),
            ("operation permission artifact JSON array instead of object", "artifact_array"),
            ("operation permission artifact not recorded", "artifact_not_recorded"),
            ("operation permission artifact failed checks present", "artifact_failed_checks"),
            ("operation permission artifact version not 0.1.0", "artifact_bad_version"),
            ("selected command missing", remove_key("selected_command")),
            ("selected command not state", set_key("selected_command", "status")),
            ("selected operation permission not recorded", set_key("selected_operation_permission_not_recorded", True)),
            ("operation permission not created", set_key("operation_permission_not_created", True)),
            ("operation permission local only not true", set_key("operation_permission_local_only_not_true", True)),
            ("operation permission read only not true", set_key("operation_permission_read_only_not_true", True)),
            ("future operation execution may not be considered", set_key("future_operation_execution_may_be_considered", False)),
            ("boundary type missing", remove_key("boundary_type")),
            ("boundary type not supported", set_key("boundary_type", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION")),
            ("boundary scope missing", remove_key("boundary_scope")),
            ("boundary scope not selected only", set_key("boundary_scope", "GENERAL_OPERATION_EXECUTION")),
            ("operation execution created", set_key("operation_execution_created", True)),
            ("operation execution performed", set_key("operation_execution_performed", True)),
            ("runtime permission created", set_key("runtime_permission_created", True)),
            ("public API created", set_key("public_api_created", True)),
            ("participant-facing interface created", set_key("participant_facing_interface_created", True)),
            ("distributed network behavior created", set_key("distributed_network_behavior_created", True)),
            ("general operation permission created", set_key("general_operation_permission_created", True)),
            ("general lookup permission created", set_key("general_lookup_permission_created", True)),
            ("arbitrary lookup permission created", set_key("arbitrary_lookup_permission_created", True)),
            ("unsupported commands permitted", set_key("unsupported_commands_permitted", True)),
            ("unsupported lookup keys permitted", set_key("unsupported_lookup_keys_permitted", True)),
            ("new lookup entry created", set_key("new_lookup_entry_created", True)),
            ("new signal accepted", set_key("new_signal_accepted", True)),
            ("new entry accepted", set_key("new_entry_accepted", True)),
            ("new relevance object created", set_key("new_relevance_object_created", True)),
            ("new index entry created", set_key("new_index_entry_created", True)),
            ("filesystem discovery performed", set_key("filesystem_discovery_performed", True)),
            ("registry created", set_key("registry_created", True)),
            ("search surface created", set_key("search_surface_created", True)),
            ("query surface created", set_key("query_surface_created", True)),
            ("ranking surface created", set_key("ranking_surface_created", True)),
            ("scoring surface created", set_key("scoring_surface_created", True)),
            ("priority surface created", set_key("priority_surface_created", True)),
            ("validity judgment created", set_key("validity_judgment_created", True)),
            ("truth judgment created", set_key("truth_judgment_created", True)),
            ("authority judgment created", set_key("authority_judgment_created", True)),
            ("currentness judgment created", set_key("currentness_judgment_created", True)),
            ("repeated reception permission created", set_key("repeated_reception_permission_created", True)),
            ("arbitrary reception created", set_key("arbitrary_reception_created", True)),
            ("feed created", set_key("feed_created", True)),
            ("source transfer occurred", set_key("source_transfer_occurred", True)),
            ("source receipt occurred", set_key("source_receipt_occurred", True)),
            ("source created", set_key("source_created", True)),
            ("authority created", set_key("authority_created", True)),
            ("currentness created", set_key("currentness_created", True)),
            ("truth created", set_key("truth_created", True)),
            ("synchronization created", set_key("synchronization_created", True)),
            ("participation authorized", set_key("participation_authorized", True)),
            ("participant role created", set_key("participant_role_created", True)),
            ("deployment created", set_key("deployment_created", True)),
            ("public release created", set_key("public_release_created", True)),
            ("broader reusable permission created", set_key("broader_reusable_permission_created", True)),
            ("follow-on work authorized", set_key("follow_on_work_authorized", True)),
            ("consumed request reopened", set_key("consumed_request_reopened", True)),
            ("authorization token reused", set_key("authorization_token_reused", True)),
            ("artifact existence treated as operation-execution-boundary authority", set_key("artifact_existence_treated_as_operation_execution_boundary_authority", True)),
            ("latest file posture treated as operation-execution-boundary authority", set_key("latest_file_posture_treated_as_operation_execution_boundary_authority", True)),
            ("repo-local availability treated as operation-execution-boundary authority", set_key("repo_local_availability_treated_as_operation_execution_boundary_authority", True)),
            ("hidden repo state used as operation-execution-boundary content", set_key("hidden_repo_state_used_as_operation_execution_boundary_content", True)),
            ("hidden repo state used as operation-execution-boundary authority", set_key("hidden_repo_state_used_as_operation_execution_boundary_authority", True)),
            ("predecessor failure evidence repaired", set_key("predecessor_failure_repaired", True)),
            ("predecessor failure evidence hidden", set_key("predecessor_failure_hidden", True)),
            ("predecessor failure evidence claimed passed", set_key("predecessor_failure_claimed_passed", True)),
            ("required non-claim missing or flipped", set_declared_non_claim("runtime_permission_created", True)),
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for index, (name, mutation) in enumerate(cases):
                with self.subTest(name=name):
                    operation_permission_path, _ = (
                        self.write_synthetic_operation_permission_artifact(
                            root,
                            self.safe_json_filename(name, index),
                        )
                    )
                    if mutation == "artifact_array":
                        operation_permission_path, _ = (
                            self.write_synthetic_operation_permission_artifact(
                                root,
                                self.safe_json_filename(name, index),
                                payload=[],
                            )
                        )
                    elif mutation == "artifact_not_recorded":
                        operation_permission_path, _ = (
                            self.write_synthetic_operation_permission_artifact(
                                root,
                                self.safe_json_filename(name, index),
                                mutator=lambda artifact: artifact.__setitem__(
                                    "outcome",
                                    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_NOT_RECORDED",
                                ),
                            )
                        )
                    elif mutation == "artifact_failed_checks":
                        operation_permission_path, _ = (
                            self.write_synthetic_operation_permission_artifact(
                                root,
                                self.safe_json_filename(name, index),
                                mutator=lambda artifact: artifact.__setitem__(
                                    "failed_check_count",
                                    1,
                                ),
                            )
                        )
                    elif mutation == "artifact_bad_version":
                        operation_permission_path, _ = (
                            self.write_synthetic_operation_permission_artifact(
                                root,
                                self.safe_json_filename(name, index),
                                mutator=lambda artifact: artifact.__setitem__(
                                    "result_version",
                                    "0.2.0",
                                ),
                            )
                        )

                    if mutation == "non_mapping":
                        result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min(
                            ["not", "a", "mapping"]  # type: ignore[arg-type]
                        )
                    elif mutation == "empty_request":
                        result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min(
                            {}
                        )
                    else:
                        request = self.valid_request(operation_permission_path)
                        if mutation == "missing_artifact":
                            request["selected_operation_permission_artifact"] = str(
                                root / "missing-operation-permission.json"
                            )
                        elif callable(mutation):
                            mutation(request)
                        result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min(
                            request
                        )

                    self.assert_blocked_with_public_code(result)
                    self.assert_blocked_non_creation_posture(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_permission_path, _ = self.write_synthetic_operation_permission_artifact(
                root
            )
            result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min(
                self.valid_request(operation_permission_path)
            )
            boundary = self.boundary(result)
            self.assertEqual(
                boundary["boundary_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY",
            )
            self.assertEqual(
                boundary["boundary_scope"],
                "SELECTED_OPERATION_EXECUTION_CONSIDERATION_ONLY",
            )
            self.assertEqual(boundary["selected_command"], "state")
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            for outcome in (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_BLOCKED",
            ):
                self.assertIn(outcome, resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn(
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_RECORDED",
                serialized,
            )
            for official in OFFICIAL_STRINGS:
                self.assertIn(official, serialized)
            self.assertNotIn("[REDACTED_SENSITIVE_CONTENT]", serialized)

    def test_raw_hidden_hostile_content_containment_and_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)

            def poison_artifact(artifact: dict[str, Any]) -> None:
                artifact["raw_operation_permission_body"] = (
                    "RAW_OPERATION_PERMISSION_BODY_MUST_NOT_RETURN"
                )
                artifact["local_relevance_medium_read_only_operation_permission"][
                    "raw_body"
                ] = "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN"
                artifact["local_relevance_medium_read_only_operation_permission"][
                    "hidden_repo_state"
                ] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"

            operation_permission_path, operation_permission_artifact = (
                self.write_synthetic_operation_permission_artifact(
                    root,
                    "hostile",
                    mutator=poison_artifact,
                )
            )
            request = self.valid_request(operation_permission_path)
            request["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
            request["raw_operation_execution_boundary_body"] = (
                "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN"
            )
            request["extra_section"] = {
                "raw_body": "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN"
            }
            request_before = copy.deepcopy(request)
            operation_permission_before = copy.deepcopy(operation_permission_artifact)

            result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min(
                request
            )

            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assert_blocked_with_public_code(result)
            self.assert_no_hostile_sentinels(result)
            serialized = json.dumps(result, sort_keys=True)
            for official in OFFICIAL_STRINGS:
                self.assertIn(official, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assertIs(self.non_claims(result)["consumed_request_reopened"], False)
            self.assertIs(self.non_claims(result)["authorization_token_reused"], False)
            self.assert_blocked_non_creation_posture(result)
            self.assertEqual(request, request_before)
            self.assertEqual(operation_permission_artifact, operation_permission_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_permission_path, _ = self.write_synthetic_operation_permission_artifact(
                root
            )
            request = self.valid_request(operation_permission_path)
            request_path = self.write_json(root / "request.json", request)

            result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            summary = result[
                "local_relevance_medium_read_only_operation_execution_boundary_summary"
            ]
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_with_public_code(malformed_result)
            array_path = self.write_json(root / "array.json", [])
            array_result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min_from_path(
                array_path
            )
            self.assert_blocked_with_public_code(array_result)
            missing_result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min_from_path(
                root / "missing.json"
            )
            self.assert_blocked_with_public_code(missing_result)

            patched_root = root / (
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
                "operation_execution_boundary_v0_min"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_root):
                first_path = resolver.write_local_relevance_medium_read_only_operation_execution_boundary_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_operation_execution_boundary_v0_min_result(
                    result
                )
            self.assertTrue(first_path.parent.exists())
            self.assertTrue(second_path.parent.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIn(
                "local_relevance_medium_read_only_operation_execution_boundary_v0_min",
                str(first_path),
            )
            with first_path.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assert_not_under_forbidden_roots(first_path)
            self.assert_not_under_forbidden_roots(second_path)

    def test_resolver_does_not_mutate_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_permission_path, operation_permission_artifact = (
                self.write_synthetic_operation_permission_artifact(root)
            )
            request = self.valid_request(operation_permission_path)
            request["posture_mapping"] = {
                "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY",
                "boundary_scope": "SELECTED_OPERATION_EXECUTION_CONSIDERATION_ONLY",
            }
            request["closure_tokens"] = {
                "consumed_request_reopened": False,
                "authorization_token_reused": False,
            }
            request["nested_raw_payload"] = {
                "raw_body": "RAW_OPERATION_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN"
            }
            request_before = copy.deepcopy(request)
            declared_non_claims_before = copy.deepcopy(request["declared_non_claims"])
            operation_permission_path_before = request["selected_operation_permission_artifact"]
            selected_command_before = request["selected_command"]
            boundary_type_before = request["boundary_type"]
            boundary_scope_before = request["boundary_scope"]
            operation_permission_before = copy.deepcopy(operation_permission_artifact)

            resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min(
                request
            )

            self.assertEqual(request, request_before)
            self.assertEqual(request["declared_non_claims"], declared_non_claims_before)
            self.assertEqual(
                request["selected_operation_permission_artifact"],
                operation_permission_path_before,
            )
            self.assertEqual(request["selected_command"], selected_command_before)
            self.assertEqual(request["boundary_type"], boundary_type_before)
            self.assertEqual(request["boundary_scope"], boundary_scope_before)
            self.assertEqual(operation_permission_artifact, operation_permission_before)

    def test_predecessor_failure_and_closure_repair_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_permission_path, _ = self.write_synthetic_operation_permission_artifact(
                root
            )
            result = resolver.resolve_local_relevance_medium_read_only_operation_execution_boundary_v0_min(
                self.valid_request(operation_permission_path)
            )
            statement = self.statement(result)
            summary = result[
                "local_relevance_medium_read_only_operation_execution_boundary_summary"
            ]
            non_claims = self.non_claims(result)
            self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
            self.assertIs(non_claims["predecessor_failure_repaired"], False)
            self.assertIs(non_claims["predecessor_failure_hidden"], False)
            self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
            self.assertIs(statement["consumed_request_token_remains_closed"], True)
            self.assertIs(statement["authorization_token_reuse_blocked"], True)
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(summary["result_level_non_claims_canonical_false"], True)
            self.assertIs(summary["consumed_request_token_remains_closed"], True)
            self.assertIs(summary["authorization_token_reuse_blocked"], True)
            self.assertIs(non_claims["consumed_request_reopened"], False)
            self.assertIs(non_claims["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
