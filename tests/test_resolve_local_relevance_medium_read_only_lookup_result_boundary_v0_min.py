"""Tests for the local read-only selected-state lookup result boundary resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY object. It verifies that
the resolver reads one clean selected-state lookup performed artifact and
records one local read-only selected-state lookup-result-consideration boundary
only.

The suite does not create lookup result behavior, operation permission, runtime
permission, public API, participant-facing interface, distributed behavior,
general lookup permission, arbitrary lookup permission, unsupported-command
permission, unsupported-key permission, new lookup entry, registry, search,
query surface, ranking, scoring, priority, validity judgment, truth judgment,
authority judgment, currentness judgment, repeated reception permission,
arbitrary reception, feed, new signal, new entry, new relevance object, new
index entry, filesystem discovery, source transfer, source receipt,
participation, or follow-on work.
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

import resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min as resolver  # noqa: E402


DEFAULT_LOOKUP_PERFORMED_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_performed_v0_min/"
    "local_relevance_medium_read_only_lookup_performed_reference_review_001__"
    "local_relevance_medium_read_only_lookup_performed_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_result_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_lookup_result_boundary_metadata",
    "declared_local_relevance_medium_read_only_lookup_result_boundary_question",
    "selected_lookup_performed_artifact_basis",
    "local_relevance_medium_read_only_lookup_result_boundary",
    "local_relevance_medium_read_only_lookup_result_boundary_checks",
    "local_relevance_medium_read_only_lookup_result_boundary_statement",
    "local_relevance_medium_read_only_lookup_result_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_lookup_result_boundary_summary",
)

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_lookup_result_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_lookup_result_boundary_summary",
    "local_relevance_medium_read_only_lookup_result_boundary_metadata",
)

BOUNDARY_FALSE_FIELDS = (
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
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

OFFICIAL_VALUES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY",
    "SELECTED_LOOKUP_RESULT_CONSIDERATION_ONLY",
    "state",
)


class LocalRelevanceMediumReadOnlyLookupResultBoundaryV0MinTests(unittest.TestCase):
    maxDiff = None

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
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

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get("local_relevance_medium_read_only_lookup_result_boundary_checks")
        self.assertIsInstance(checks, list)
        return checks

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        boundary = result.get("local_relevance_medium_read_only_lookup_result_boundary")
        self.assertIsInstance(boundary, dict)
        return boundary

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get(
            "local_relevance_medium_read_only_lookup_result_boundary_statement"
        )
        self.assertIsInstance(statement, dict)
        return statement

    def non_claims(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        return non_claims

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
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)

    def assert_lookup_result_boundary_non_claims(self, result: Mapping[str, Any]) -> None:
        self.assert_canonical_false_non_claims(result)
        boundary = self.boundary(result)
        for key in BOUNDARY_FALSE_FIELDS:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_lookup_result_boundary_non_claims(result)

    def assert_same_or_stable_artifact_path(self, actual: Any, expected: Path) -> None:
        self.assertIsNotNone(actual)
        actual_path = Path(str(actual))
        expected_path = Path(expected)
        if actual_path.is_absolute() and expected_path.is_absolute():
            self.assertEqual(actual_path, expected_path)
            return
        if actual_path.exists() or expected_path.exists():
            self.assertEqual(actual_path.resolve(), expected_path.resolve())
            return
        self.assertTrue(str(actual).endswith(expected_path.name))

    def assert_no_wrapper_confusion(self, boundary: Mapping[str, Any]) -> None:
        for field in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(field, boundary)

    def assert_boolean_values(self, mapping: Mapping[str, Any], keys: tuple[str, ...]) -> None:
        for key in keys:
            self.assertIn(key, mapping)
            self.assertIsInstance(mapping[key], bool)

    def assert_closure_tokens_false(self, result: Mapping[str, Any]) -> None:
        non_claims = self.non_claims(result)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)
        boundary = self.boundary(result)
        self.assertIs(boundary["consumed_request_reopened"], False)
        self.assertIs(boundary["authorization_token_reused"], False)

    def assert_blocked_non_creation_posture(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in BOUNDARY_FALSE_FIELDS:
            self.assertIs(boundary[key], False)
        non_claims = self.non_claims(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[key], False)

    def assert_recorded_lookup_result_boundary_posture(
        self,
        result: Mapping[str, Any],
        performed_path: Path,
    ) -> None:
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["boundary_id"],
            "local_relevance_medium_read_only_lookup_result_boundary_001",
        )
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY",
        )
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(boundary["boundary_scope"], "SELECTED_LOOKUP_RESULT_CONSIDERATION_ONLY")
        self.assert_same_or_stable_artifact_path(
            boundary["basis_lookup_performed_artifact"], performed_path
        )
        self.assertEqual(
            boundary["basis_lookup_performed_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_RECORDED",
        )
        self.assertEqual(boundary["basis_lookup_performed_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_lookup_performed_failed_check_count"], 0)
        self.assertEqual(boundary["selected_command"], "state")
        for key in (
            "selected_command_is_state",
            "selected_lookup_performed_recorded",
            "lookup_performed",
            "lookup_performed_local_only",
            "lookup_performed_read_only",
            "future_lookup_result_may_be_considered",
        ):
            self.assertIs(boundary[key], True)
        for key in BOUNDARY_FALSE_FIELDS:
            self.assertIs(boundary[key], False)
        self.assert_no_wrapper_confusion(boundary)
        self.assert_boolean_values(
            boundary,
            (
                "selected_command_is_state",
                "selected_lookup_performed_recorded",
                "lookup_performed",
                "lookup_performed_local_only",
                "lookup_performed_read_only",
                "future_lookup_result_may_be_considered",
                *BOUNDARY_FALSE_FIELDS,
            ),
        )

    def assert_recorded_statement(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        for key in (
            "local_relevance_medium_read_only_lookup_result_boundary_recorded",
            "basis_lookup_performed_artifact_preserved",
            "selected_command_preserved",
            "selected_command_is_state",
            "selected_lookup_performed_recorded",
            "lookup_performed",
            "lookup_performed_local_only",
            "lookup_performed_read_only",
            "future_lookup_result_may_be_considered",
            "consumed_request_token_remains_closed",
            "authorization_token_reuse_blocked",
            "predecessor_failure_evidence_preserved",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIn(key, statement)
            self.assertIs(statement[key], True)

    def assert_no_hostile_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def path_is_or_under(self, path: Path, root: Path) -> bool:
        path = Path(path)
        root = Path(root)
        if path == root:
            return True
        try:
            path.relative_to(root)
            return True
        except ValueError:
            return False

    def assert_not_under_forbidden_roots(self, path: Path) -> None:
        path = Path(path)
        candidate_paths = (path, path.parent)
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            forbidden_candidates = (forbidden, REPO_ROOT / forbidden)
            for candidate in candidate_paths:
                for forbidden_candidate in forbidden_candidates:
                    self.assertFalse(
                        self.path_is_or_under(candidate, forbidden_candidate),
                        f"{candidate} must not write under prior root {forbidden_candidate}",
                    )

    def write_json(self, path: Path, data: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def synthetic_lookup_performed_artifact(self) -> dict[str, Any]:
        performed = {
            "lookup_performed_id": "local_relevance_medium_read_only_lookup_performed_001",
            "lookup_performed_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED",
            "lookup_performed_version": "0.1.0",
            "lookup_performed_scope": "SELECTED_LOOKUP_PERFORMED_ONLY",
            "selected_command": "state",
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_lookup_performed_recorded": True,
            "selected_lookup_performed_recorded": True,
            "lookup_performed": True,
            "lookup_performed_local_only": True,
            "lookup_performed_read_only": True,
            "lookup_command_executed": True,
            "lookup_command_execution_local_only": True,
            "lookup_command_execution_read_only": True,
        }
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            performed[key] = False
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "local_relevance_medium_read_only_lookup_performed": performed,
            "local_relevance_medium_read_only_lookup_performed_checks": [],
            "local_relevance_medium_read_only_lookup_performed_statement": {
                "local_relevance_medium_read_only_lookup_performed_recorded": True,
                "selected_command_preserved": True,
                "selected_command_is_state": True,
                "selected_lookup_performed_recorded": True,
                "lookup_performed": True,
                "lookup_performed_local_only": True,
                "lookup_performed_read_only": True,
                "consumed_request_token_remains_closed": True,
                "authorization_token_reuse_blocked": True,
                "predecessor_failure_evidence_preserved": True,
                "result_level_non_claims_canonical_false": True,
            },
            "local_relevance_medium_read_only_lookup_performed_summary": {
                "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_RECORDED",
                "result_version": "0.1.0",
                "failed_check_count": 0,
                "selected_command": "state",
                "selected_command_is_state": True,
                "lookup_performed_recorded": True,
                "local_relevance_medium_read_only_lookup_performed_recorded": True,
                "lookup_performed": True,
                "lookup_performed_local_only": True,
                "lookup_performed_read_only": True,
                "lookup_result_created": False,
            },
        }

    def write_basis_artifact(self, directory: Path) -> tuple[Path, dict[str, Any]]:
        artifact = self.synthetic_lookup_performed_artifact()
        path = directory / "lookup_performed.json"
        self.write_json(path, artifact)
        return path, artifact

    def valid_request_for_path(self, performed_path: Path) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_lookup_result_boundary_v0_min_request(
            selected_lookup_performed_artifact=performed_path,
        )

    def clean_recorded_result(self) -> tuple[dict[str, Any], tempfile.TemporaryDirectory[str], Path]:
        temp = tempfile.TemporaryDirectory()
        directory = Path(temp.name)
        performed_path, _artifact = self.write_basis_artifact(directory)
        result = resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min(
            self.valid_request_for_path(performed_path)
        )
        return result, temp, performed_path

    def set_performed_basis_bool(self, artifact: dict[str, Any], key: str, value: bool) -> None:
        performed = artifact["local_relevance_medium_read_only_lookup_performed"]
        summary = artifact["local_relevance_medium_read_only_lookup_performed_summary"]
        statement = artifact["local_relevance_medium_read_only_lookup_performed_statement"]
        performed[key] = value
        summary[key] = value
        statement[key] = value
        if key == "selected_lookup_performed_recorded":
            performed["local_relevance_medium_read_only_lookup_performed_recorded"] = value
            summary["lookup_performed_recorded"] = value
            summary["local_relevance_medium_read_only_lookup_performed_recorded"] = value
            statement["local_relevance_medium_read_only_lookup_performed_recorded"] = value

    def test_public_api_constants_and_builder_paths(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_lookup_result_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_lookup_result_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_lookup_result_boundary_v0_min_request",
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
            "resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min",
        )
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY",
            resolver.SUPPORTED_BOUNDARY_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_LOOKUP_RESULT_CONSIDERATION_ONLY",
            resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        for key in (
            "lookup_result_created",
            "operation_permission_created",
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
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        request = resolver.build_declared_local_relevance_medium_read_only_lookup_result_boundary_v0_min_request()
        self.assertTrue(
            request["selected_lookup_performed_artifact"].endswith(
                "local_relevance_medium_read_only_lookup_performed_reference_review_001__"
                "local_relevance_medium_read_only_lookup_performed_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], "state")
        self.assertIs(request["declared_non_claims"]["consumed_request_reopened"], False)
        self.assertIs(request["declared_non_claims"]["authorization_token_reused"], False)
        self.assert_not_under_forbidden_roots(Path(resolver.OUTPUT_ROOT))

    def test_successful_recorded_result_from_synthetic_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            performed_path, _artifact = self.write_basis_artifact(Path(tmp))
            request = self.valid_request_for_path(performed_path)
            result = resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min(
                request
            )
            summary = resolver.build_local_relevance_medium_read_only_lookup_result_boundary_v0_min_summary(
                result
            )

            self.assertIsInstance(result, dict)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.failed_check_count(result), 0)
            self.assert_not_blocked(result)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min",
            )
            self.assertGreater(self.passed_check_count(result), 0)
            self.assertEqual(
                self.boundary(result)["boundary_id"],
                "local_relevance_medium_read_only_lookup_result_boundary_001",
            )
            for section in EXPECTED_WRAPPER_SECTIONS:
                self.assertIn(section, result)
            self.assert_recorded_lookup_result_boundary_posture(result, performed_path)
            self.assert_recorded_statement(result)
            self.assert_canonical_false_non_claims(result)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_LOOKUP_PERFORMED_ARTIFACT.exists():
            self.skipTest("default lookup performed artifact is not present")

        request = resolver.build_declared_local_relevance_medium_read_only_lookup_result_boundary_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min(
            request
        )

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        boundary = self.boundary(result)
        self.assertEqual(boundary["selected_command"], "state")
        self.assertEqual(
            boundary["boundary_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY",
        )
        self.assertEqual(boundary["boundary_scope"], "SELECTED_LOOKUP_RESULT_CONSIDERATION_ONLY")
        for key in (
            "selected_lookup_performed_recorded",
            "lookup_performed",
            "lookup_performed_local_only",
            "lookup_performed_read_only",
            "future_lookup_result_may_be_considered",
        ):
            self.assertIs(boundary[key], True)
        for key in (
            "lookup_result_created",
            "operation_permission_created",
            "runtime_permission_created",
            "public_api_created",
            "distributed_network_behavior_created",
            "general_lookup_permission_created",
            "follow_on_work_authorized",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(boundary[key], False)
        self.assert_recorded_statement(result)
        self.assert_same_or_stable_artifact_path(
            boundary["basis_lookup_performed_artifact"],
            DEFAULT_LOOKUP_PERFORMED_ARTIFACT,
        )

    def test_closure_token_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            performed_path, _artifact = self.write_basis_artifact(Path(tmp))
            base_request = self.valid_request_for_path(performed_path)

            cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str], ...] = (
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
                    "declared consumed_request_reopened missing",
                    lambda request: request["declared_non_claims"].pop(
                        "consumed_request_reopened"
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                ),
                (
                    "declared authorization_token_reused missing",
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
            )
            for name, mutate, expected_code in cases:
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assert_closure_tokens_false(result)
                    self.assert_blocked_non_creation_posture(result)

    def test_required_non_claim_canonicalization_blocks_flipped_true(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            performed_path, _artifact = self.write_basis_artifact(Path(tmp))
            base_request = self.valid_request_for_path(performed_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(self.non_claims(result)[key], False)
                    self.assert_blocked_non_creation_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        def mutate_performed(
            request: dict[str, Any],
            directory: Path,
            case_name: str,
            mutator: Callable[[dict[str, Any]], None] | Any,
        ) -> None:
            artifact = self.synthetic_lookup_performed_artifact()
            if callable(mutator):
                mutator(artifact)
                payload: Any = artifact
            else:
                payload = mutator
            path = directory / self.safe_json_filename(case_name)
            self.write_json(path, payload)
            request["selected_lookup_performed_artifact"] = str(path)

        def set_artifact_outcome(artifact: dict[str, Any], outcome: str) -> None:
            artifact["outcome"] = outcome
            artifact["local_relevance_medium_read_only_lookup_performed_summary"][
                "outcome"
            ] = outcome

        def set_artifact_version(artifact: dict[str, Any], version: str) -> None:
            artifact["result_version"] = version
            artifact["local_relevance_medium_read_only_lookup_performed"][
                "lookup_performed_version"
            ] = version
            artifact["local_relevance_medium_read_only_lookup_performed_summary"][
                "result_version"
            ] = version

        def set_artifact_failed(artifact: dict[str, Any]) -> None:
            artifact["failed_check_count"] = 1
            artifact["local_relevance_medium_read_only_lookup_performed_checks"] = [
                {
                    "check_name": "synthetic failed lookup performed basis check",
                    "passed": False,
                    "failure_code": "SYNTHETIC_BASIS_FAILURE",
                }
            ]
            artifact["local_relevance_medium_read_only_lookup_performed_summary"][
                "failed_check_count"
            ] = 1

        cases: list[tuple[str, Callable[[dict[str, Any], Path, int], Any]]] = [
            (
                "explicit block intent",
                lambda request, _directory, _index: request.__setitem__(
                    "local_relevance_medium_read_only_lookup_result_boundary_intent",
                    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY",
                ),
            ),
            ("missing request", lambda request, _directory, _index: request.clear()),
            (
                "non-mapping request",
                lambda _request, _directory, _index: ["not", "a", "mapping"],
            ),
            (
                "unsupported intent",
                lambda request, _directory, _index: request.__setitem__(
                    "local_relevance_medium_read_only_lookup_result_boundary_intent",
                    "UNSUPPORTED_LOOKUP_RESULT_BOUNDARY_INTENT",
                ),
            ),
            (
                "lookup performed artifact path missing",
                lambda request, _directory, _index: request.__setitem__(
                    "lookup_performed_artifact_missing", True
                ),
            ),
            (
                "lookup performed artifact unreadable",
                lambda request, directory, index: request.__setitem__(
                    "selected_lookup_performed_artifact",
                    str(directory / self.safe_json_filename("missing performed", index)),
                ),
            ),
            (
                "lookup performed artifact JSON array instead of object",
                lambda request, directory, _index: mutate_performed(
                    request, directory, "performed array", []
                ),
            ),
            (
                "lookup performed artifact not recorded",
                lambda request, directory, _index: mutate_performed(
                    request,
                    directory,
                    "performed not recorded",
                    lambda artifact: set_artifact_outcome(
                        artifact,
                        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_NOT_RECORDED",
                    ),
                ),
            ),
            (
                "lookup performed artifact failed checks present",
                lambda request, directory, _index: mutate_performed(
                    request,
                    directory,
                    "performed failed checks",
                    set_artifact_failed,
                ),
            ),
            (
                "lookup performed artifact version not 0.1.0",
                lambda request, directory, _index: mutate_performed(
                    request,
                    directory,
                    "performed bad version",
                    lambda artifact: set_artifact_version(artifact, "9.9.9"),
                ),
            ),
            (
                "selected command missing",
                lambda request, _directory, _index: (
                    request.pop("selected_command", None),
                    None,
                )[1],
            ),
            (
                "selected command not state",
                lambda request, _directory, _index: request.__setitem__(
                    "selected_command", "lookup"
                ),
            ),
            (
                "selected lookup performed not recorded",
                lambda request, directory, _index: mutate_performed(
                    request,
                    directory,
                    "performed selected not recorded",
                    lambda artifact: self.set_performed_basis_bool(
                        artifact, "selected_lookup_performed_recorded", False
                    ),
                ),
            ),
            (
                "lookup not performed",
                lambda request, directory, _index: mutate_performed(
                    request,
                    directory,
                    "lookup not performed",
                    lambda artifact: self.set_performed_basis_bool(
                        artifact, "lookup_performed", False
                    ),
                ),
            ),
            (
                "lookup performed local only not true",
                lambda request, directory, _index: mutate_performed(
                    request,
                    directory,
                    "lookup performed local not true",
                    lambda artifact: self.set_performed_basis_bool(
                        artifact, "lookup_performed_local_only", False
                    ),
                ),
            ),
            (
                "lookup performed read only not true",
                lambda request, directory, _index: mutate_performed(
                    request,
                    directory,
                    "lookup performed read not true",
                    lambda artifact: self.set_performed_basis_bool(
                        artifact, "lookup_performed_read_only", False
                    ),
                ),
            ),
            (
                "future lookup result may not be considered",
                lambda request, _directory, _index: request.__setitem__(
                    "future_lookup_result_may_not_be_considered", True
                ),
            ),
            (
                "boundary type missing",
                lambda request, _directory, _index: (
                    request.pop("boundary_type", None),
                    None,
                )[1],
            ),
            (
                "boundary type wrong",
                lambda request, _directory, _index: request.__setitem__(
                    "boundary_type",
                    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT",
                ),
            ),
            (
                "boundary scope missing",
                lambda request, _directory, _index: (
                    request.pop("boundary_scope", None),
                    None,
                )[1],
            ),
            (
                "boundary scope wrong",
                lambda request, _directory, _index: request.__setitem__(
                    "boundary_scope", "SELECTED_LOOKUP_RESULT_ONLY"
                ),
            ),
            ("lookup result created", lambda request, _directory, _index: request.__setitem__("lookup_result_created", True)),
            ("operation permission created", lambda request, _directory, _index: request.__setitem__("operation_permission_created", True)),
            ("runtime permission created", lambda request, _directory, _index: request.__setitem__("runtime_permission_created", True)),
            ("public API created", lambda request, _directory, _index: request.__setitem__("public_api_created", True)),
            ("participant-facing interface created", lambda request, _directory, _index: request.__setitem__("participant_facing_interface_created", True)),
            ("distributed network behavior created", lambda request, _directory, _index: request.__setitem__("distributed_network_behavior_created", True)),
            ("general lookup permission created", lambda request, _directory, _index: request.__setitem__("general_lookup_permission_created", True)),
            ("arbitrary lookup permission created", lambda request, _directory, _index: request.__setitem__("arbitrary_lookup_permission_created", True)),
            ("unsupported commands permitted", lambda request, _directory, _index: request.__setitem__("unsupported_commands_permitted", True)),
            ("unsupported lookup keys permitted", lambda request, _directory, _index: request.__setitem__("unsupported_lookup_keys_permitted", True)),
            ("new lookup entry created", lambda request, _directory, _index: request.__setitem__("new_lookup_entry_created", True)),
            ("new signal accepted", lambda request, _directory, _index: request.__setitem__("new_signal_accepted", True)),
            ("new entry accepted", lambda request, _directory, _index: request.__setitem__("new_entry_accepted", True)),
            ("new relevance object created", lambda request, _directory, _index: request.__setitem__("new_relevance_object_created", True)),
            ("new index entry created", lambda request, _directory, _index: request.__setitem__("new_index_entry_created", True)),
            ("filesystem discovery performed", lambda request, _directory, _index: request.__setitem__("filesystem_discovery_performed", True)),
            ("registry created", lambda request, _directory, _index: request.__setitem__("registry_created", True)),
            ("search surface created", lambda request, _directory, _index: request.__setitem__("search_surface_created", True)),
            ("query surface created", lambda request, _directory, _index: request.__setitem__("query_surface_created", True)),
            ("ranking surface created", lambda request, _directory, _index: request.__setitem__("ranking_surface_created", True)),
            ("scoring surface created", lambda request, _directory, _index: request.__setitem__("scoring_surface_created", True)),
            ("priority surface created", lambda request, _directory, _index: request.__setitem__("priority_surface_created", True)),
            ("validity judgment created", lambda request, _directory, _index: request.__setitem__("validity_judgment_created", True)),
            ("truth judgment created", lambda request, _directory, _index: request.__setitem__("truth_judgment_created", True)),
            ("authority judgment created", lambda request, _directory, _index: request.__setitem__("authority_judgment_created", True)),
            ("currentness judgment created", lambda request, _directory, _index: request.__setitem__("currentness_judgment_created", True)),
            ("repeated reception permission created", lambda request, _directory, _index: request.__setitem__("repeated_reception_permission_created", True)),
            ("arbitrary reception created", lambda request, _directory, _index: request.__setitem__("arbitrary_reception_created", True)),
            ("feed created", lambda request, _directory, _index: request.__setitem__("feed_created", True)),
            ("source transfer occurred", lambda request, _directory, _index: request.__setitem__("source_transfer_occurred", True)),
            ("source receipt occurred", lambda request, _directory, _index: request.__setitem__("source_receipt_occurred", True)),
            ("source created", lambda request, _directory, _index: request.__setitem__("source_created", True)),
            ("authority created", lambda request, _directory, _index: request.__setitem__("authority_created", True)),
            ("currentness created", lambda request, _directory, _index: request.__setitem__("currentness_created", True)),
            ("truth created", lambda request, _directory, _index: request.__setitem__("truth_created", True)),
            ("synchronization created", lambda request, _directory, _index: request.__setitem__("synchronization_created", True)),
            ("participation authorized", lambda request, _directory, _index: request.__setitem__("participation_authorized", True)),
            ("participant role created", lambda request, _directory, _index: request.__setitem__("participant_role_created", True)),
            ("deployment created", lambda request, _directory, _index: request.__setitem__("deployment_created", True)),
            ("public release created", lambda request, _directory, _index: request.__setitem__("public_release_created", True)),
            ("broader reusable permission created", lambda request, _directory, _index: request.__setitem__("broader_reusable_permission_created", True)),
            ("follow-on work authorized", lambda request, _directory, _index: request.__setitem__("follow_on_work_authorized", True)),
            ("consumed request reopened", lambda request, _directory, _index: request.__setitem__("consumed_request_reopened", True)),
            ("authorization token reused", lambda request, _directory, _index: request.__setitem__("authorization_token_reused", True)),
            ("artifact existence treated as lookup-result-boundary authority", lambda request, _directory, _index: request.__setitem__("artifact_existence_treated_as_lookup_result_boundary_authority", True)),
            ("latest file posture treated as lookup-result-boundary authority", lambda request, _directory, _index: request.__setitem__("latest_file_posture_treated_as_lookup_result_boundary_authority", True)),
            ("repo-local availability treated as lookup-result-boundary authority", lambda request, _directory, _index: request.__setitem__("repo_local_availability_treated_as_lookup_result_boundary_authority", True)),
            ("hidden repo state used as lookup-result-boundary content", lambda request, _directory, _index: request.__setitem__("hidden_repo_state_used_as_lookup_result_boundary_content", True)),
            ("hidden repo state used as lookup-result-boundary authority", lambda request, _directory, _index: request.__setitem__("hidden_repo_state_used_as_lookup_result_boundary_authority", True)),
            ("predecessor failure evidence hidden repaired claimed passed", lambda request, _directory, _index: request.__setitem__("predecessor_failure_hidden", True)),
            (
                "required non-claim missing or flipped",
                lambda request, _directory, _index: (
                    request["declared_non_claims"].pop("lookup_result_created", None),
                    None,
                )[1],
            ),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            performed_path, _artifact = self.write_basis_artifact(directory)
            for index, (name, mutate) in enumerate(cases):
                with self.subTest(name=name):
                    request = self.valid_request_for_path(performed_path)
                    maybe_direct = mutate(request, directory, index)
                    declared = maybe_direct if maybe_direct is not None else request
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min(
                        declared
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_blocked_non_creation_posture(result)

    def test_official_values_are_preserved(self) -> None:
        result, temp, _performed_path = self.clean_recorded_result()
        try:
            boundary = self.boundary(result)
            self.assertEqual(
                boundary["boundary_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY",
            )
            self.assertEqual(
                boundary["boundary_scope"],
                "SELECTED_LOOKUP_RESULT_CONSIDERATION_ONLY",
            )
            self.assertEqual(boundary["selected_command"], "state")
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            for outcome in (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_BLOCKED",
            ):
                self.assertIn(outcome, resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            for official in OFFICIAL_VALUES:
                self.assertIn(official, serialized)
            self.assertNotIn("[REDACTED", serialized)
        finally:
            temp.cleanup()

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            artifact = self.synthetic_lookup_performed_artifact()
            artifact["raw_lookup_performed_body"] = HOSTILE_SENTINELS[3]
            artifact["local_relevance_medium_read_only_lookup_performed"][
                "raw_full_body"
            ] = HOSTILE_SENTINELS[0]
            artifact["local_relevance_medium_read_only_lookup_performed"][
                "hidden_repo_state"
            ] = HOSTILE_SENTINELS[-1]
            performed_path = directory / "hostile_lookup_performed.json"
            self.write_json(performed_path, artifact)
            request = self.valid_request_for_path(performed_path)
            request["raw_lookup_result_boundary_body"] = HOSTILE_SENTINELS[1]
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            original = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min(
                request
            )

            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assert_blocked_with_public_code(result)
            self.assert_no_hostile_sentinels(result)
            serialized = json.dumps(result, sort_keys=True)
            for official in OFFICIAL_VALUES:
                self.assertIn(official, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assert_closure_tokens_false(result)
            self.assert_blocked_non_creation_posture(result)
            self.assertEqual(request, original)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            performed_path, _artifact = self.write_basis_artifact(directory)
            request = self.valid_request_for_path(performed_path)
            request_path = directory / "request.json"
            self.write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            summary = resolver.build_local_relevance_medium_read_only_lookup_result_boundary_v0_min_summary(
                result
            )
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = directory / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(
                resolver.LocalRelevanceMediumReadOnlyLookupResultBoundaryV0MinError
            ):
                resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min_from_path(
                    malformed_path
                )

            array_path = directory / "array.json"
            self.write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min_from_path(
                array_path
            )
            self.assert_blocked_with_public_code(array_result)

            missing_path = directory / "missing_request.json"
            with self.assertRaises(
                resolver.LocalRelevanceMediumReadOnlyLookupResultBoundaryV0MinError
            ):
                resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min_from_path(
                    missing_path
                )

            output_root = directory / "local_relevance_medium_read_only_lookup_result_boundary_v0_min"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_lookup_result_boundary_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_lookup_result_boundary_v0_min_result(
                    result
                )
            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIsInstance(json.loads(first_path.read_text(encoding="utf-8")), dict)
            self.assertIsInstance(json.loads(second_path.read_text(encoding="utf-8")), dict)
            self.assertIn(
                "local_relevance_medium_read_only_lookup_result_boundary_v0_min",
                str(first_path.parent),
            )
            self.assert_not_under_forbidden_roots(first_path)
            self.assert_not_under_forbidden_roots(second_path)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            artifact = self.synthetic_lookup_performed_artifact()
            artifact_original = copy.deepcopy(artifact)
            performed_path = directory / "performed_non_mutation.json"
            self.write_json(performed_path, artifact)
            request = self.valid_request_for_path(performed_path)
            request["raw_lookup_result_boundary_body"] = {
                "sentinel": HOSTILE_SENTINELS[0],
                "nested": {"hidden_repo_state": HOSTILE_SENTINELS[-1]},
            }
            original_request = copy.deepcopy(request)
            original_declared_non_claims = copy.deepcopy(request["declared_non_claims"])
            original_performed_path = request["selected_lookup_performed_artifact"]
            original_selected_command = request["selected_command"]
            original_type = request["boundary_type"]
            original_scope = request["boundary_scope"]

            resolver.resolve_local_relevance_medium_read_only_lookup_result_boundary_v0_min(
                request
            )

            self.assertEqual(request, original_request)
            self.assertEqual(request["declared_non_claims"], original_declared_non_claims)
            self.assertEqual(request["selected_lookup_performed_artifact"], original_performed_path)
            self.assertEqual(request["selected_command"], original_selected_command)
            self.assertEqual(request["boundary_type"], original_type)
            self.assertEqual(request["boundary_scope"], original_scope)
            self.assertIs(request["declared_non_claims"]["consumed_request_reopened"], False)
            self.assertIs(request["declared_non_claims"]["authorization_token_reused"], False)
            self.assertEqual(artifact, artifact_original)

    def test_predecessor_failure_preservation(self) -> None:
        result, temp, _performed_path = self.clean_recorded_result()
        try:
            statement = self.statement(result)
            summary = resolver.build_local_relevance_medium_read_only_lookup_result_boundary_v0_min_summary(
                result
            )
            non_claims = self.non_claims(result)
            self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
            self.assertIs(non_claims["predecessor_failure_repaired"], False)
            self.assertIs(non_claims["predecessor_failure_hidden"], False)
            self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
            self.assertIs(statement["consumed_request_token_remains_closed"], True)
            self.assertIs(statement["authorization_token_reuse_blocked"], True)
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(summary["result_level_non_claims_canonical_false"], True)
            self.assertIs(summary["key_non_claims"]["consumed_request_reopened"], True)
            self.assertIs(summary["key_non_claims"]["authorization_token_reused"], True)
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main()
