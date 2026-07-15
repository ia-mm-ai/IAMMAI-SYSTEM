"""Tests for the local read-only runtime permission boundary resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY object. It verifies
that the resolver reads one clean selected-state operation execution artifact
and records one local read-only selected-state runtime-permission-consideration
boundary only.

The suite does not create runtime permission, runtime, runtime hosting, runtime
loop, daemon behavior, continuation, public API, participant-facing interface,
distributed behavior, general operation permission, general lookup permission,
arbitrary lookup permission, unsupported-command permission, unsupported-key
permission, a new lookup entry beyond the already bounded selected-state lookup
result object, registry, search, query surface, ranking, scoring, priority,
validity judgment, truth judgment, authority judgment, currentness judgment,
older runtime authority import, repeated reception permission, arbitrary
reception, feed, new signal, new entry, new relevance object beyond the already
bounded selected-state lookup result object, new index entry, filesystem
discovery, source transfer, source receipt, participation, or follow-on work.
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

import resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min as resolver  # noqa: E402


DEFAULT_OPERATION_EXECUTION_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "operation_execution_v0_min/"
    "local_relevance_medium_read_only_operation_execution_reference_review_001__"
    "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_permission_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_boundary_v0_min"),
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
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_layer_closure_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_loop_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_permission_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_hosting_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_ongoing_runtime_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_reusable_runtime_permission_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_post_runtime_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_daemon_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_continuation_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_behavior_v0_min"),
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_runtime_permission_boundary_metadata",
    "declared_local_relevance_medium_read_only_runtime_permission_boundary_question",
    "selected_operation_execution_artifact_basis",
    "local_relevance_medium_read_only_runtime_permission_boundary",
    "local_relevance_medium_read_only_runtime_permission_boundary_checks",
    "local_relevance_medium_read_only_runtime_permission_boundary_statement",
    "local_relevance_medium_read_only_runtime_permission_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_permission_boundary_summary",
)

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_permission_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_runtime_permission_boundary_summary",
    "local_relevance_medium_read_only_runtime_permission_boundary_metadata",
)

BOUNDARY_FALSE_FIELDS = (
    "runtime_permission_created",
    "runtime_created",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "continuation_created",
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
    "older_runtime_lineage_imported_as_authority",
    "older_runtime_permission_treated_as_current",
    "runtime_authority_imported",
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
    "artifact_existence_treated_as_runtime_permission_boundary_authority",
    "latest_file_posture_treated_as_runtime_permission_boundary_authority",
    "repo_local_availability_treated_as_runtime_permission_boundary_authority",
    "hidden_repo_state_used_as_runtime_permission_boundary_content",
    "hidden_repo_state_used_as_runtime_permission_boundary_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

HOSTILE_SENTINELS = (
    "RAW_RUNTIME_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

OFFICIAL_STRINGS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY",
    "SELECTED_RUNTIME_PERMISSION_CONSIDERATION_ONLY",
    "state",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
)


class LocalRelevanceMediumReadOnlyRuntimePermissionBoundaryResolverTests(
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

    def synthetic_operation_execution_artifact(self) -> dict[str, Any]:
        operation_execution = {
            "operation_execution_id": "local_relevance_medium_read_only_operation_execution_001",
            "operation_execution_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
            "operation_execution_version": "0.1.0",
            "operation_execution_scope": "SELECTED_OPERATION_EXECUTION_ONLY",
            "basis_operation_execution_boundary_outcome": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_BOUNDARY_RECORDED"
            ),
            "basis_operation_execution_boundary_result_version": "0.1.0",
            "basis_operation_execution_boundary_failed_check_count": 0,
            "basis_operation_permission_outcome": (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION_RECORDED"
            ),
            "basis_operation_permission_result_version": "0.1.0",
            "basis_operation_permission_failed_check_count": 0,
            "selected_command": "state",
            "selected_command_is_state": True,
            "selected_operation_permission_recorded": True,
            "operation_permission_created": True,
            "operation_permission_local_only": True,
            "operation_permission_read_only": True,
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
        }
        for key in BOUNDARY_FALSE_FIELDS:
            operation_execution[key] = False
        statement = {
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "selected_operation_execution_recorded": True,
            "selected_command_preserved": True,
            "selected_command_is_state": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        summary = {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 89,
            "selected_command": "state",
            **statement,
        }
        for key in BOUNDARY_FALSE_FIELDS:
            summary[key] = False
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 89,
            "local_relevance_medium_read_only_operation_execution_metadata": {
                "result_version": "0.1.0",
                "resolver_module": (
                    "resolve_local_relevance_medium_read_only_operation_execution_v0_min"
                ),
            },
            "local_relevance_medium_read_only_operation_execution": (
                operation_execution
            ),
            "local_relevance_medium_read_only_operation_execution_statement": statement,
            "local_relevance_medium_read_only_operation_execution_checks": [],
            "local_relevance_medium_read_only_operation_execution_summary": summary,
            "non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
        }

    def write_synthetic_operation_execution_artifact(
        self,
        directory: Path,
        name: str = "clean",
        mutator: Callable[[dict[str, Any]], None] | None = None,
        payload: Any | None = None,
    ) -> tuple[Path, dict[str, Any]]:
        artifact = self.synthetic_operation_execution_artifact()
        if mutator is not None:
            mutator(artifact)
        path = directory / self.safe_json_filename(f"{name}_operation_execution")
        self.write_json(path, artifact if payload is None else payload)
        return path, artifact

    def valid_request(self, operation_execution_path: Path) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_request(
            selected_operation_execution_artifact=operation_execution_path
        )

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get(
            "local_relevance_medium_read_only_runtime_permission_boundary_checks"
        )
        self.assertIsInstance(checks, list)
        return checks

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        boundary = result.get("local_relevance_medium_read_only_runtime_permission_boundary")
        self.assertIsInstance(boundary, Mapping)
        return boundary

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get(
            "local_relevance_medium_read_only_runtime_permission_boundary_statement"
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

    def assert_runtime_permission_boundary_non_claims(
        self,
        result: Mapping[str, Any],
    ) -> None:
        boundary = self.boundary(result)
        for key in BOUNDARY_FALSE_FIELDS:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False)
            self.assertIsInstance(boundary[key], bool)
        for key in REQUEST_ONLY_FALSE_FIELDS:
            self.assertIn(key, self.non_claims(result))
            self.assertIs(self.non_claims(result)[key], False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_runtime_permission_boundary_non_claims(result)

    def assert_boundary_not_wrapper_confused(self, boundary: Mapping[str, Any]) -> None:
        for field in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(field, boundary)

    def assert_recorded_boundary_posture(
        self,
        result: Mapping[str, Any],
        operation_execution_path: Path,
    ) -> None:
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["boundary_id"],
            "local_relevance_medium_read_only_runtime_permission_boundary_001",
        )
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY",
        )
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_RUNTIME_PERMISSION_CONSIDERATION_ONLY",
        )
        self.assert_same_or_stable_artifact_path(
            boundary["basis_operation_execution_artifact"],
            operation_execution_path,
        )
        self.assertEqual(
            boundary["basis_operation_execution_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
        )
        self.assertEqual(boundary["basis_operation_execution_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_operation_execution_failed_check_count"], 0)
        self.assertEqual(boundary["selected_command"], "state")
        for key in (
            "selected_command_is_state",
            "selected_operation_execution_recorded",
            "operation_execution_created",
            "operation_execution_performed",
            "operation_execution_local_only",
            "operation_execution_read_only",
            "future_runtime_permission_may_be_considered",
        ):
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], True)
            self.assertIsInstance(boundary[key], bool)
        self.assert_runtime_permission_boundary_non_claims(result)
        self.assert_boundary_not_wrapper_confused(boundary)

    def assert_statement_recorded_posture(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True)
            self.assertIsInstance(statement[key], bool)

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

    def mutate_operation_execution_flag(
        self,
        field: str,
        value: Any,
    ) -> Callable[[dict[str, Any]], None]:
        def mutate(artifact: dict[str, Any]) -> None:
            artifact[field] = value
            artifact["local_relevance_medium_read_only_operation_execution"][field] = (
                value
            )
            artifact[
                "local_relevance_medium_read_only_operation_execution_statement"
            ][field] = value
            artifact["local_relevance_medium_read_only_operation_execution_summary"][
                field
            ] = value

        return mutate

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_request",
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
            "resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min",
        )
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY",
            resolver.SUPPORTED_BOUNDARY_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_RUNTIME_PERMISSION_CONSIDERATION_ONLY",
            resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        for key in (
            "runtime_permission_created",
            "runtime_created",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "continuation_created",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for code in (
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "RUNTIME_AUTHORITY_IMPORTED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        request = (
            resolver.build_declared_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_request()
        )
        self.assertTrue(
            request["selected_operation_execution_artifact"].endswith(
                "local_relevance_medium_read_only_operation_execution_reference_review_001__"
                "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], "state")
        self.assertIs(request["declared_non_claims"]["consumed_request_reopened"], False)
        self.assertIs(request["declared_non_claims"]["authorization_token_reused"], False)
        self.assertIs(
            request["declared_non_claims"][
                "older_runtime_lineage_imported_as_authority"
            ],
            False,
        )
        self.assertIs(
            request["declared_non_claims"][
                "older_runtime_permission_treated_as_current"
            ],
            False,
        )
        self.assertIs(request["declared_non_claims"]["runtime_authority_imported"], False)
        self.assert_not_under_forbidden_roots(REPO_ROOT / resolver.OUTPUT_ROOT)

    def test_successful_recorded_result_from_synthetic_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_execution_path, _ = (
                self.write_synthetic_operation_execution_artifact(root)
            )
            request = self.valid_request(operation_execution_path)

            result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min(
                request
            )

            self.assertIsInstance(result, dict)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.failed_check_count(result), 0)
            self.assert_not_blocked(result)
            summary = result[
                "local_relevance_medium_read_only_runtime_permission_boundary_summary"
            ]
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min",
            )
            self.assertGreater(self.passed_check_count(result), 0)
            self.assertEqual(
                self.boundary(result)["boundary_id"],
                "local_relevance_medium_read_only_runtime_permission_boundary_001",
            )
            for section in EXPECTED_WRAPPER_SECTIONS:
                self.assertIn(section, result)
            self.assert_recorded_boundary_posture(result, operation_execution_path)
            self.assert_statement_recorded_posture(result)
            self.assert_canonical_false_non_claims(result)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_OPERATION_EXECUTION_ARTIFACT.exists():
            self.skipTest("default operation execution artifact is not present")

        request = (
            resolver.build_declared_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_request()
        )
        result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min(
            request
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        boundary = self.boundary(result)
        self.assertEqual(boundary["selected_command"], "state")
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY",
        )
        self.assertEqual(
            boundary["boundary_scope"],
            "SELECTED_RUNTIME_PERMISSION_CONSIDERATION_ONLY",
        )
        for key in (
            "selected_operation_execution_recorded",
            "operation_execution_created",
            "operation_execution_performed",
            "operation_execution_local_only",
            "operation_execution_read_only",
            "future_runtime_permission_may_be_considered",
        ):
            self.assertIs(boundary[key], True)
        for key in (
            "runtime_permission_created",
            "runtime_created",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "continuation_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "consumed_request_reopened",
            "authorization_token_reused",
            "follow_on_work_authorized",
        ):
            self.assertIs(boundary[key], False)
        self.assertIs(self.statement(result)["predecessor_failure_evidence_preserved"], True)
        self.assert_same_or_stable_artifact_path(
            boundary["basis_operation_execution_artifact"],
            DEFAULT_OPERATION_EXECUTION_ARTIFACT,
        )

    def test_closure_token_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_execution_path, _ = (
                self.write_synthetic_operation_execution_artifact(root)
            )
            base_request = self.valid_request(operation_execution_path)
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
                    "string declared consumed_request_reopened",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "consumed_request_reopened", "false"
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "string declared authorization_token_reused",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "authorization_token_reused", "false"
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "none declared consumed_request_reopened",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "consumed_request_reopened", None
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "none declared authorization_token_reused",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "authorization_token_reused", None
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
            ]
            for name, mutate, expected_code in cases:
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assertIs(
                        result["non_claims"]["consumed_request_reopened"],
                        False,
                    )
                    self.assertIs(
                        result["non_claims"]["authorization_token_reused"],
                        False,
                    )

    def test_required_false_non_claims_canonicalize_when_flipped(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_execution_path, _ = (
                self.write_synthetic_operation_execution_artifact(root)
            )
            base_request = self.valid_request(operation_execution_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_runtime_permission_boundary_non_claims(result)
                    self.assertIs(
                        self.boundary(result)[
                            "older_runtime_lineage_imported_as_authority"
                        ],
                        False,
                    )
                    self.assertIs(
                        self.boundary(result)[
                            "older_runtime_permission_treated_as_current"
                        ],
                        False,
                    )
                    self.assertIs(
                        self.boundary(result)["runtime_authority_imported"],
                        False,
                    )

    def test_representative_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)

            def request_case(
                name: str,
                mutate_request: Callable[[dict[str, Any]], None] | None = None,
                mutate_artifact: Callable[[dict[str, Any]], None] | None = None,
                payload: Any | None = None,
                non_mapping_request: Any | None = None,
            ) -> tuple[str, dict[str, Any] | Any]:
                if non_mapping_request is not None:
                    return name, non_mapping_request
                path, _ = self.write_synthetic_operation_execution_artifact(
                    root,
                    self.safe_json_filename(name),
                    mutate_artifact,
                    payload,
                )
                request = self.valid_request(path)
                if mutate_request is not None:
                    mutate_request(request)
                return name, request

            cases: list[tuple[str, dict[str, Any] | Any]] = [
                request_case(
                    "explicit block intent",
                    lambda request: request.__setitem__(
                        "local_relevance_medium_read_only_runtime_permission_boundary_intent",
                        "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY",
                    ),
                ),
                ("missing request", {}),
                request_case("non-mapping request", non_mapping_request=["not", "mapping"]),
                request_case(
                    "unsupported intent",
                    lambda request: request.__setitem__(
                        "local_relevance_medium_read_only_runtime_permission_boundary_intent",
                        "UNSUPPORTED",
                    ),
                ),
                request_case(
                    "operation execution artifact path missing",
                    lambda request: request.pop("selected_operation_execution_artifact"),
                ),
                request_case(
                    "operation execution artifact unreadable",
                    lambda request: request.__setitem__(
                        "selected_operation_execution_artifact",
                        str(root / "missing_operation_execution.json"),
                    ),
                ),
                request_case(
                    "operation execution artifact JSON array instead of object",
                    payload=[],
                ),
                request_case(
                    "operation execution artifact not recorded",
                    mutate_artifact=lambda artifact: artifact.__setitem__(
                        "outcome", "NOT_RECORDED"
                    ),
                ),
                request_case(
                    "operation execution artifact failed checks present",
                    mutate_artifact=lambda artifact: artifact.__setitem__(
                        "failed_check_count", 1
                    ),
                ),
                request_case(
                    "operation execution artifact version not 0.1.0",
                    mutate_artifact=lambda artifact: artifact.__setitem__(
                        "result_version", "9.9.9"
                    ),
                ),
                request_case(
                    "selected command missing",
                    lambda request: request.pop("selected_command"),
                ),
                request_case(
                    "selected command not state",
                    lambda request: request.__setitem__("selected_command", "lookup"),
                ),
                request_case(
                    "selected operation execution not recorded",
                    lambda request: request.__setitem__(
                        "selected_operation_execution_not_recorded", True
                    ),
                ),
                request_case(
                    "operation execution not created",
                    lambda request: request.__setitem__(
                        "operation_execution_not_created", True
                    ),
                ),
                request_case(
                    "operation execution not performed",
                    lambda request: request.__setitem__(
                        "operation_execution_not_performed", True
                    ),
                ),
                request_case(
                    "operation execution local only not true",
                    lambda request: request.__setitem__(
                        "operation_execution_local_only_not_true", True
                    ),
                ),
                request_case(
                    "operation execution read only not true",
                    lambda request: request.__setitem__(
                        "operation_execution_read_only_not_true", True
                    ),
                ),
                request_case(
                    "future runtime permission may not be considered",
                    lambda request: request.__setitem__(
                        "future_runtime_permission_may_not_be_considered",
                        True,
                    ),
                ),
                request_case("boundary type missing", lambda request: request.pop("boundary_type")),
                request_case(
                    "boundary type not local relevance medium read only runtime permission boundary",
                    lambda request: request.__setitem__("boundary_type", "WRONG"),
                ),
                request_case("boundary scope missing", lambda request: request.pop("boundary_scope")),
                request_case(
                    "boundary scope not selected runtime permission consideration only",
                    lambda request: request.__setitem__("boundary_scope", "WRONG"),
                ),
            ]
            for field in (
                "runtime_permission_created",
                "runtime_created",
                "runtime_hosting_created",
                "runtime_loop_created",
                "daemon_behavior_created",
                "continuation_created",
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
                "older_runtime_lineage_imported_as_authority",
                "older_runtime_permission_treated_as_current",
                "runtime_authority_imported",
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
                "artifact_existence_treated_as_runtime_permission_boundary_authority",
                "latest_file_posture_treated_as_runtime_permission_boundary_authority",
                "repo_local_availability_treated_as_runtime_permission_boundary_authority",
                "hidden_repo_state_used_as_runtime_permission_boundary_content",
                "hidden_repo_state_used_as_runtime_permission_boundary_authority",
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
            ):
                cases.append(
                    request_case(
                        f"{field} true",
                        lambda request, field=field: request.__setitem__(
                            field, True
                        ),
                    )
                )
            cases.append(
                request_case(
                    "required non-claim missing",
                    lambda request: request["declared_non_claims"].pop(
                        "runtime_created"
                    ),
                )
            )
            cases.append(
                request_case(
                    "required non-claim flipped",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "runtime_created", True
                    ),
                )
            )

            for name, request in cases:
                with self.subTest(name=name):
                    result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_execution_path, _ = (
                self.write_synthetic_operation_execution_artifact(root)
            )
            result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min(
                self.valid_request(operation_execution_path)
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            boundary = self.boundary(result)
            self.assertEqual(
                boundary["boundary_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY",
            )
            self.assertEqual(
                boundary["boundary_scope"],
                "SELECTED_RUNTIME_PERMISSION_CONSIDERATION_ONLY",
            )
            self.assertEqual(boundary["selected_command"], "state")
            for outcome in (
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_BLOCKED,
            ):
                self.assertIn(outcome, resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            for official in OFFICIAL_STRINGS:
                self.assertIn(official, serialized)
            self.assertNotIn("[REDACTED", serialized)

    def test_raw_hidden_and_older_runtime_hostile_content_is_contained(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)

            def mutate(artifact: dict[str, Any]) -> None:
                artifact["raw_runtime_body"] = "RAW_RUNTIME_BODY_MUST_NOT_RETURN"
                artifact[
                    "local_relevance_medium_read_only_operation_execution"
                ]["raw_runtime_permission_body"] = (
                    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN"
                )

            operation_execution_path, _ = (
                self.write_synthetic_operation_execution_artifact(
                    root,
                    "hostile",
                    mutate,
                )
            )
            request = self.valid_request(operation_execution_path)
            request["raw_runtime_permission_boundary_body"] = (
                "RAW_RUNTIME_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN"
            )
            request["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
            request["older_runtime_lineage"] = {
                "raw_runtime_body": "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN"
            }
            before = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min(
                request
            )

            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assert_no_hostile_sentinels(result)
            serialized = json.dumps(result, sort_keys=True)
            for official in OFFICIAL_STRINGS[:3]:
                self.assertIn(official, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assert_runtime_permission_boundary_non_claims(result)
            self.assertEqual(request, before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_execution_path, _ = (
                self.write_synthetic_operation_execution_artifact(root)
            )
            request = self.valid_request(operation_execution_path)
            request_path = self.write_json(root / "request.json", request)

            result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(
                result[
                    "local_relevance_medium_read_only_runtime_permission_boundary_summary"
                ]["result_version"],
                "0.1.0",
            )
            self.assertEqual(
                result[
                    "local_relevance_medium_read_only_runtime_permission_boundary_summary"
                ]["resolver_module"],
                "resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_with_public_code(malformed_result)

            array_path = self.write_json(root / "array.json", [])
            array_result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_from_path(
                array_path
            )
            self.assert_blocked_with_public_code(array_result)

            missing_result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_from_path(
                root / "missing_request.json"
            )
            self.assert_blocked_with_public_code(missing_result)

            output_root = (
                root
                / "local_relevance_medium_read_only_runtime_permission_boundary_v0_min"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_result(
                    result
                )
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(first_path.parent.exists())
            self.assertIn(
                "local_relevance_medium_read_only_runtime_permission_boundary_v0_min",
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
            artifact = self.synthetic_operation_execution_artifact()
            artifact_before = copy.deepcopy(artifact)
            operation_execution_path = self.write_json(
                root / "operation_execution.json",
                artifact,
            )
            request = self.valid_request(operation_execution_path)
            request["nested_payload"] = {
                "raw_runtime_body": "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
                "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            }
            request_before = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min(
                request
            )

            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assertEqual(request, request_before)
            self.assertEqual(artifact, artifact_before)
            self.assertEqual(
                request["selected_operation_execution_artifact"],
                request_before["selected_operation_execution_artifact"],
            )
            self.assertEqual(request["selected_command"], "state")
            self.assertEqual(
                request["boundary_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_BOUNDARY",
            )
            self.assertEqual(
                request["boundary_scope"],
                "SELECTED_RUNTIME_PERMISSION_CONSIDERATION_ONLY",
            )
            self.assertIs(
                request["declared_non_claims"]["consumed_request_reopened"],
                False,
            )
            self.assertIs(
                request["declared_non_claims"]["authorization_token_reused"],
                False,
            )
            self.assertIs(
                request["declared_non_claims"][
                    "older_runtime_lineage_imported_as_authority"
                ],
                False,
            )

    def test_predecessor_failure_and_closure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            operation_execution_path, _ = (
                self.write_synthetic_operation_execution_artifact(root)
            )
            result = resolver.resolve_local_relevance_medium_read_only_runtime_permission_boundary_v0_min(
                self.valid_request(operation_execution_path)
            )
            summary = resolver.build_local_relevance_medium_read_only_runtime_permission_boundary_v0_min_summary(
                result
            )
            statement = self.statement(result)
            self.assertIs(
                statement["predecessor_failure_evidence_preserved"],
                True,
            )
            self.assertIs(
                statement["result_level_non_claims_canonical_false"],
                True,
            )
            self.assertIs(statement["consumed_request_token_remains_closed"], True)
            self.assertIs(statement["authorization_token_reuse_blocked"], True)
            self.assertIs(
                result["non_claims"]["predecessor_failure_repaired"],
                False,
            )
            self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
            self.assertIs(
                result["non_claims"]["predecessor_failure_claimed_passed"],
                False,
            )
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(summary["result_level_non_claims_canonical_false"], True)
            self.assertIs(summary["consumed_request_token_remains_closed"], True)
            self.assertIs(summary["authorization_token_reuse_blocked"], True)
            self.assertIs(
                summary["older_runtime_lineage_not_imported_as_authority"],
                True,
            )
            self.assertIs(
                summary["older_runtime_permission_not_treated_as_current"],
                True,
            )
            self.assertIs(summary["runtime_authority_not_imported"], True)


if __name__ == "__main__":
    unittest.main()
