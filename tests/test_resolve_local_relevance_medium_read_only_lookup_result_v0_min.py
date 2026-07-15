"""Tests for the local read-only selected-state lookup result resolver.

This suite is bounded to one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT
object. It verifies that the resolver reads one clean lookup result boundary
artifact and one clean selected-state lookup performed artifact, then records
one local read-only selected-state lookup-result object only.

The suite does not create operation permission, runtime permission, public API,
participant-facing interface, distributed behavior, general lookup permission,
arbitrary lookup permission, unsupported-command permission, unsupported-key
permission, a new lookup entry beyond the bounded selected-state lookup result
object, registry, search, query surface, ranking, scoring, priority, validity
judgment, truth judgment, authority judgment, currentness judgment, repeated
reception permission, arbitrary reception, feed, new signal, new entry, new
relevance object beyond the bounded selected-state lookup result object, new
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

import resolve_local_relevance_medium_read_only_lookup_result_v0_min as resolver  # noqa: E402


DEFAULT_LOOKUP_RESULT_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_result_boundary_v0_min/"
    "local_relevance_medium_read_only_lookup_result_boundary_reference_review_001__"
    "local_relevance_medium_read_only_lookup_result_boundary_v0_min_result.json"
)
DEFAULT_LOOKUP_PERFORMED_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "lookup_performed_v0_min/"
    "local_relevance_medium_read_only_lookup_performed_reference_review_001__"
    "local_relevance_medium_read_only_lookup_performed_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_result_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_lookup_result_metadata",
    "declared_local_relevance_medium_read_only_lookup_result_question",
    "selected_lookup_result_boundary_artifact_basis",
    "selected_lookup_performed_artifact_basis",
    "local_relevance_medium_read_only_lookup_result",
    "local_relevance_medium_read_only_lookup_result_checks",
    "local_relevance_medium_read_only_lookup_result_statement",
    "local_relevance_medium_read_only_lookup_result_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_lookup_result_summary",
)

FORBIDDEN_LOOKUP_RESULT_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_lookup_result_checks",
    "non_claims",
    "local_relevance_medium_read_only_lookup_result_summary",
    "local_relevance_medium_read_only_lookup_result_metadata",
)

LOOKUP_RESULT_OBJECT_FALSE_FIELDS = (
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
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

OFFICIAL_VALUES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT",
    "SELECTED_LOOKUP_RESULT_ONLY",
    "state",
)


class LocalRelevanceMediumReadOnlyLookupResultV0MinTests(unittest.TestCase):
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
        checks = result.get("local_relevance_medium_read_only_lookup_result_checks")
        self.assertIsInstance(checks, list)
        return checks

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def lookup_result(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        lookup_result = result.get("local_relevance_medium_read_only_lookup_result")
        self.assertIsInstance(lookup_result, dict)
        return lookup_result

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get("local_relevance_medium_read_only_lookup_result_statement")
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

    def assert_lookup_result_non_claims(self, result: Mapping[str, Any]) -> None:
        self.assert_canonical_false_non_claims(result)
        lookup_result = self.lookup_result(result)
        for key in LOOKUP_RESULT_OBJECT_FALSE_FIELDS:
            self.assertIn(key, lookup_result)
            self.assertIs(lookup_result[key], False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_lookup_result_non_claims(result)

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

    def assert_no_wrapper_confusion(self, lookup_result: Mapping[str, Any]) -> None:
        for field in FORBIDDEN_LOOKUP_RESULT_WRAPPER_FIELDS:
            self.assertNotIn(field, lookup_result)

    def assert_boolean_values(self, mapping: Mapping[str, Any], keys: tuple[str, ...]) -> None:
        for key in keys:
            self.assertIn(key, mapping)
            self.assertIsInstance(mapping[key], bool)

    def assert_closure_tokens_false(self, result: Mapping[str, Any]) -> None:
        non_claims = self.non_claims(result)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)
        lookup_result = self.lookup_result(result)
        self.assertIs(lookup_result["consumed_request_reopened"], False)
        self.assertIs(lookup_result["authorization_token_reused"], False)

    def assert_blocked_non_creation_posture(self, result: Mapping[str, Any]) -> None:
        lookup_result = self.lookup_result(result)
        self.assertIs(lookup_result["lookup_result_created"], False)
        self.assertIs(lookup_result["lookup_result_local_only"], False)
        self.assertIs(lookup_result["lookup_result_read_only"], False)
        for key in LOOKUP_RESULT_OBJECT_FALSE_FIELDS:
            self.assertIs(lookup_result[key], False)
        self.assert_canonical_false_non_claims(result)

    def assert_recorded_lookup_result_posture(
        self,
        result: Mapping[str, Any],
        boundary_path: Path,
        performed_path: Path,
    ) -> None:
        lookup_result = self.lookup_result(result)
        self.assertEqual(
            lookup_result["lookup_result_id"],
            "local_relevance_medium_read_only_lookup_result_001",
        )
        self.assertEqual(
            lookup_result["lookup_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT",
        )
        self.assertEqual(lookup_result["lookup_result_version"], "0.1.0")
        self.assertEqual(lookup_result["lookup_result_scope"], "SELECTED_LOOKUP_RESULT_ONLY")
        self.assert_same_or_stable_artifact_path(
            lookup_result["basis_lookup_result_boundary_artifact"], boundary_path
        )
        self.assertEqual(
            lookup_result["basis_lookup_result_boundary_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_RECORDED",
        )
        self.assertEqual(lookup_result["basis_lookup_result_boundary_result_version"], "0.1.0")
        self.assertEqual(lookup_result["basis_lookup_result_boundary_failed_check_count"], 0)
        self.assert_same_or_stable_artifact_path(
            lookup_result["basis_lookup_performed_artifact"], performed_path
        )
        self.assertEqual(
            lookup_result["basis_lookup_performed_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_RECORDED",
        )
        self.assertEqual(lookup_result["basis_lookup_performed_result_version"], "0.1.0")
        self.assertEqual(lookup_result["basis_lookup_performed_failed_check_count"], 0)
        self.assertEqual(lookup_result["selected_command"], "state")
        for key in (
            "selected_command_is_state",
            "selected_lookup_performed_recorded",
            "lookup_performed",
            "lookup_performed_local_only",
            "lookup_performed_read_only",
            "local_relevance_medium_read_only_lookup_result_recorded",
            "lookup_result_created",
            "lookup_result_local_only",
            "lookup_result_read_only",
        ):
            self.assertIs(lookup_result[key], True)
        for key in LOOKUP_RESULT_OBJECT_FALSE_FIELDS:
            self.assertIs(lookup_result[key], False)
        self.assert_no_wrapper_confusion(lookup_result)
        self.assert_boolean_values(
            lookup_result,
            (
                "selected_command_is_state",
                "selected_lookup_performed_recorded",
                "lookup_performed",
                "lookup_performed_local_only",
                "lookup_performed_read_only",
                "local_relevance_medium_read_only_lookup_result_recorded",
                "lookup_result_created",
                "lookup_result_local_only",
                "lookup_result_read_only",
                *LOOKUP_RESULT_OBJECT_FALSE_FIELDS,
            ),
        )

    def assert_recorded_statement(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        for key in (
            "local_relevance_medium_read_only_lookup_result_recorded",
            "basis_lookup_result_boundary_artifact_preserved",
            "basis_lookup_performed_artifact_preserved",
            "selected_command_preserved",
            "selected_command_is_state",
            "selected_lookup_performed_recorded",
            "lookup_performed",
            "lookup_performed_local_only",
            "lookup_performed_read_only",
            "lookup_result_created",
            "lookup_result_local_only",
            "lookup_result_read_only",
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

    def synthetic_lookup_result_boundary_artifact(self) -> dict[str, Any]:
        boundary = {
            "boundary_id": "local_relevance_medium_read_only_lookup_result_boundary_001",
            "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY",
            "boundary_version": "0.1.0",
            "boundary_scope": "SELECTED_LOOKUP_RESULT_CONSIDERATION_ONLY",
            "basis_lookup_performed_artifact": "synthetic_lookup_performed.json",
            "basis_lookup_performed_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_RECORDED",
            "basis_lookup_performed_result_version": "0.1.0",
            "basis_lookup_performed_failed_check_count": 0,
            "selected_command": "state",
            "selected_command_is_state": True,
            "selected_lookup_performed_recorded": True,
            "lookup_performed": True,
            "lookup_performed_local_only": True,
            "lookup_performed_read_only": True,
            "future_lookup_result_may_be_considered": True,
            "lookup_result_created": False,
        }
        for key in LOOKUP_RESULT_OBJECT_FALSE_FIELDS:
            boundary[key] = False
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "local_relevance_medium_read_only_lookup_result_boundary": boundary,
            "local_relevance_medium_read_only_lookup_result_boundary_statement": {
                "local_relevance_medium_read_only_lookup_result_boundary_recorded": True,
                "basis_lookup_performed_artifact_preserved": True,
                "selected_command_preserved": True,
                "selected_command_is_state": True,
                "selected_lookup_performed_recorded": True,
                "lookup_performed": True,
                "lookup_performed_local_only": True,
                "lookup_performed_read_only": True,
                "future_lookup_result_may_be_considered": True,
                "consumed_request_token_remains_closed": True,
                "authorization_token_reuse_blocked": True,
                "predecessor_failure_evidence_preserved": True,
                "result_level_non_claims_canonical_false": True,
            },
            "local_relevance_medium_read_only_lookup_result_boundary_summary": {
                "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_RECORDED",
                "result_version": "0.1.0",
                "failed_check_count": 0,
                "selected_command": "state",
                "selected_command_is_state": True,
                "future_lookup_result_may_be_considered": True,
            },
        }

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
            "lookup_result_created": False,
        }
        for key in LOOKUP_RESULT_OBJECT_FALSE_FIELDS:
            performed[key] = False
        return {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "local_relevance_medium_read_only_lookup_performed": performed,
            "local_relevance_medium_read_only_lookup_performed_statement": {
                "local_relevance_medium_read_only_lookup_performed_recorded": True,
                "selected_lookup_performed_recorded": True,
                "selected_command_preserved": True,
                "selected_command_is_state": True,
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
                "selected_lookup_performed_recorded": True,
                "local_relevance_medium_read_only_lookup_performed_recorded": True,
                "lookup_performed": True,
                "lookup_performed_local_only": True,
                "lookup_performed_read_only": True,
                "lookup_result_created": False,
            },
        }

    def write_basis_artifacts(
        self,
        directory: Path,
        *,
        name: str = "basis",
    ) -> tuple[Path, Path, dict[str, Any], dict[str, Any]]:
        boundary = self.synthetic_lookup_result_boundary_artifact()
        performed = self.synthetic_lookup_performed_artifact()
        boundary_path = directory / self.safe_json_filename(f"{name}_lookup_result_boundary")
        performed_path = directory / self.safe_json_filename(f"{name}_lookup_performed")
        self.write_json(boundary_path, boundary)
        self.write_json(performed_path, performed)
        return boundary_path, performed_path, boundary, performed

    def valid_request_for_paths(self, boundary_path: Path, performed_path: Path) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_lookup_result_v0_min_request(
            selected_lookup_result_boundary_artifact=boundary_path,
            selected_lookup_performed_artifact=performed_path,
        )

    def clean_recorded_result(
        self,
    ) -> tuple[dict[str, Any], tempfile.TemporaryDirectory[str], Path, Path]:
        temp = tempfile.TemporaryDirectory()
        directory = Path(temp.name)
        boundary_path, performed_path, _boundary, _performed = self.write_basis_artifacts(directory)
        result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min(
            self.valid_request_for_paths(boundary_path, performed_path)
        )
        return result, temp, boundary_path, performed_path

    def set_performed_basis_bool(self, artifact: dict[str, Any], key: str, value: bool) -> None:
        performed = artifact["local_relevance_medium_read_only_lookup_performed"]
        summary = artifact["local_relevance_medium_read_only_lookup_performed_summary"]
        statement = artifact["local_relevance_medium_read_only_lookup_performed_statement"]
        performed[key] = value
        summary[key] = value
        statement[key] = value
        if key == "selected_lookup_performed_recorded":
            performed["local_relevance_medium_read_only_lookup_performed_recorded"] = value
            summary["local_relevance_medium_read_only_lookup_performed_recorded"] = value
            statement["local_relevance_medium_read_only_lookup_performed_recorded"] = value

    def test_public_api_constants_and_builder_paths(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_lookup_result_v0_min",
            "resolve_local_relevance_medium_read_only_lookup_result_v0_min_from_path",
            "write_local_relevance_medium_read_only_lookup_result_v0_min_result",
            "build_local_relevance_medium_read_only_lookup_result_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_lookup_result_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_LOOKUP_RESULT_TYPE_VALUES",
            "SUPPORTED_LOOKUP_RESULT_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_lookup_result_v0_min",
        )
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT",
            resolver.SUPPORTED_LOOKUP_RESULT_TYPE_VALUES,
        )
        self.assertIn("SELECTED_LOOKUP_RESULT_ONLY", resolver.SUPPORTED_LOOKUP_RESULT_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        for key in (
            "operation_permission_created",
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
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        request = resolver.build_declared_local_relevance_medium_read_only_lookup_result_v0_min_request()
        self.assertTrue(
            request["selected_lookup_result_boundary_artifact"].endswith(
                "local_relevance_medium_read_only_lookup_result_boundary_reference_review_001__"
                "local_relevance_medium_read_only_lookup_result_boundary_v0_min_result.json"
            )
        )
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

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, performed_path, _boundary, _performed = self.write_basis_artifacts(Path(tmp))
            request = self.valid_request_for_paths(boundary_path, performed_path)
            result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min(request)
            summary = resolver.build_local_relevance_medium_read_only_lookup_result_v0_min_summary(result)

            self.assertIsInstance(result, dict)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.failed_check_count(result), 0)
            self.assert_not_blocked(result)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertGreater(self.passed_check_count(result), 0)
            self.assertEqual(
                self.lookup_result(result)["lookup_result_id"],
                "local_relevance_medium_read_only_lookup_result_001",
            )
            for section in EXPECTED_WRAPPER_SECTIONS:
                self.assertIn(section, result)
            self.assert_recorded_lookup_result_posture(result, boundary_path, performed_path)
            self.assert_recorded_statement(result)
            self.assert_canonical_false_non_claims(result)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_LOOKUP_RESULT_BOUNDARY_ARTIFACT.exists() or not DEFAULT_LOOKUP_PERFORMED_ARTIFACT.exists():
            self.skipTest("default lookup result boundary and lookup performed artifacts are not both present")

        request = resolver.build_declared_local_relevance_medium_read_only_lookup_result_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min(request)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        lookup_result = self.lookup_result(result)
        self.assertEqual(lookup_result["selected_command"], "state")
        self.assertEqual(lookup_result["lookup_result_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT")
        self.assertEqual(lookup_result["lookup_result_scope"], "SELECTED_LOOKUP_RESULT_ONLY")
        for key in (
            "selected_lookup_performed_recorded",
            "lookup_performed",
            "lookup_performed_local_only",
            "lookup_performed_read_only",
            "local_relevance_medium_read_only_lookup_result_recorded",
            "lookup_result_created",
            "lookup_result_local_only",
            "lookup_result_read_only",
        ):
            self.assertIs(lookup_result[key], True)
        for key in (
            "operation_permission_created",
            "runtime_permission_created",
            "public_api_created",
            "distributed_network_behavior_created",
            "general_lookup_permission_created",
            "follow_on_work_authorized",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(lookup_result[key], False)
        self.assertIs(self.statement(result)["predecessor_failure_evidence_preserved"], True)
        self.assert_same_or_stable_artifact_path(
            lookup_result["basis_lookup_result_boundary_artifact"],
            DEFAULT_LOOKUP_RESULT_BOUNDARY_ARTIFACT,
        )
        self.assert_same_or_stable_artifact_path(
            lookup_result["basis_lookup_performed_artifact"],
            DEFAULT_LOOKUP_PERFORMED_ARTIFACT,
        )

    def test_closure_token_blocking_behavior(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str | None], ...] = (
            ("top-level consumed_request_reopened", lambda request: request.__setitem__("consumed_request_reopened", True), "CONSUMED_REQUEST_REOPENED"),
            ("top-level authorization_token_reused", lambda request: request.__setitem__("authorization_token_reused", True), "AUTHORIZATION_TOKEN_REUSED"),
            ("declared consumed_request_reopened true", lambda request: request["declared_non_claims"].__setitem__("consumed_request_reopened", True), "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("declared authorization_token_reused true", lambda request: request["declared_non_claims"].__setitem__("authorization_token_reused", True), "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("declared consumed_request_reopened removed", lambda request: request["declared_non_claims"].pop("consumed_request_reopened"), "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("declared authorization_token_reused removed", lambda request: request["declared_non_claims"].pop("authorization_token_reused"), "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("declared consumed_request_reopened string false", lambda request: request["declared_non_claims"].__setitem__("consumed_request_reopened", "false"), "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("declared authorization_token_reused string false", lambda request: request["declared_non_claims"].__setitem__("authorization_token_reused", "false"), "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("declared consumed_request_reopened none", lambda request: request["declared_non_claims"].__setitem__("consumed_request_reopened", None), "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("declared authorization_token_reused none", lambda request: request["declared_non_claims"].__setitem__("authorization_token_reused", None), "NON_CLAIM_MISSING_OR_FLIPPED"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, performed_path, _boundary, _performed = self.write_basis_artifacts(Path(tmp))
            base_request = self.valid_request_for_paths(boundary_path, performed_path)
            for name, mutate, expected_code in cases:
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    if expected_code is not None:
                        self.assertEqual(self.block_code(result), expected_code)
                    self.assert_closure_tokens_false(result)
                    self.assert_blocked_non_creation_posture(result)

    def test_critical_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, performed_path, _boundary, _performed = self.write_basis_artifacts(Path(tmp))
            base_request = self.valid_request_for_paths(boundary_path, performed_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(self.non_claims(result)[key], False)
                    self.assertNotEqual(self.non_claims(result)[key], request["declared_non_claims"][key])
                    self.assert_blocked_non_creation_posture(result)

    def representative_block_cases(
        self,
    ) -> tuple[tuple[str, Callable[[dict[str, Any], dict[str, Any], dict[str, Any], Path, Path, Path], Any]], ...]:
        def set_boundary_top(key: str, value: Any) -> Callable[..., None]:
            def mutate(_request: dict[str, Any], boundary: dict[str, Any], _performed: dict[str, Any], _bp: Path, _pp: Path, _directory: Path) -> None:
                boundary[key] = value
            return mutate

        def set_performed_top(key: str, value: Any) -> Callable[..., None]:
            def mutate(_request: dict[str, Any], _boundary: dict[str, Any], performed: dict[str, Any], _bp: Path, _pp: Path, _directory: Path) -> None:
                performed[key] = value
            return mutate

        def set_request(key: str, value: Any) -> Callable[..., None]:
            def mutate(request: dict[str, Any], _boundary: dict[str, Any], _performed: dict[str, Any], _bp: Path, _pp: Path, _directory: Path) -> None:
                request[key] = value
            return mutate

        def remove_request(key: str) -> Callable[..., None]:
            def mutate(request: dict[str, Any], _boundary: dict[str, Any], _performed: dict[str, Any], _bp: Path, _pp: Path, _directory: Path) -> None:
                request.pop(key, None)
            return mutate

        def set_performed_bool(key: str, value: bool) -> Callable[..., None]:
            def mutate(_request: dict[str, Any], _boundary: dict[str, Any], performed: dict[str, Any], _bp: Path, _pp: Path, _directory: Path) -> None:
                self.set_performed_basis_bool(performed, key, value)
            return mutate

        def boundary_json_array(request: dict[str, Any], _boundary: dict[str, Any], _performed: dict[str, Any], boundary_path: Path, _pp: Path, _directory: Path) -> None:
            self.write_json(boundary_path, [])
            request["selected_lookup_result_boundary_artifact"] = str(boundary_path)

        def performed_json_array(request: dict[str, Any], _boundary: dict[str, Any], _performed: dict[str, Any], _bp: Path, performed_path: Path, _directory: Path) -> None:
            self.write_json(performed_path, [])
            request["selected_lookup_performed_artifact"] = str(performed_path)

        def missing_non_claim(request: dict[str, Any], _boundary: dict[str, Any], _performed: dict[str, Any], _bp: Path, _pp: Path, _directory: Path) -> None:
            request["declared_non_claims"].pop("operation_permission_created")

        return (
            ("explicit block intent", set_request("local_relevance_medium_read_only_lookup_result_intent", "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT")),
            ("unsupported intent", set_request("local_relevance_medium_read_only_lookup_result_intent", "UNSUPPORTED_INTENT")),
            ("lookup result boundary artifact path missing", set_request("selected_lookup_result_boundary_artifact", "")),
            ("lookup result boundary artifact unreadable", set_request("selected_lookup_result_boundary_artifact", "missing_lookup_result_boundary.json")),
            ("lookup result boundary artifact JSON array instead of object", boundary_json_array),
            ("lookup result boundary artifact not recorded", set_boundary_top("outcome", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BOUNDARY_NOT_RECORDED")),
            ("lookup result boundary artifact failed checks present", set_boundary_top("failed_check_count", 1)),
            ("lookup result boundary artifact version not 0.1.0", set_boundary_top("result_version", "9.9.9")),
            ("lookup performed artifact path missing", set_request("selected_lookup_performed_artifact", "")),
            ("lookup performed artifact unreadable", set_request("selected_lookup_performed_artifact", "missing_lookup_performed.json")),
            ("lookup performed artifact JSON array instead of object", performed_json_array),
            ("lookup performed artifact not recorded", set_performed_top("outcome", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PERFORMED_NOT_RECORDED")),
            ("lookup performed artifact failed checks present", set_performed_top("failed_check_count", 1)),
            ("lookup performed artifact version not 0.1.0", set_performed_top("result_version", "9.9.9")),
            ("selected command missing", remove_request("selected_command")),
            ("selected command not state", set_request("selected_command", "lookup")),
            ("selected lookup performed not recorded", set_performed_bool("selected_lookup_performed_recorded", False)),
            ("lookup not performed", set_performed_bool("lookup_performed", False)),
            ("lookup performed local only not true", set_performed_bool("lookup_performed_local_only", False)),
            ("lookup performed read only not true", set_performed_bool("lookup_performed_read_only", False)),
            ("lookup result type missing", remove_request("lookup_result_type")),
            ("lookup result type not exact", set_request("lookup_result_type", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION")),
            ("lookup result scope missing", remove_request("lookup_result_scope")),
            ("lookup result scope not selected only", set_request("lookup_result_scope", "REGISTRY")),
            ("local relevance medium read-only lookup result not recorded", set_request("local_relevance_medium_read_only_lookup_result_not_recorded", True)),
            ("lookup result not created", set_request("lookup_result_not_created", True)),
            ("lookup result local only not true", set_request("lookup_result_local_only_not_true", True)),
            ("lookup result read only not true", set_request("lookup_result_read_only_not_true", True)),
            ("operation permission created", set_request("operation_permission_created", True)),
            ("runtime permission created", set_request("runtime_permission_created", True)),
            ("public API created", set_request("public_api_created", True)),
            ("participant-facing interface created", set_request("participant_facing_interface_created", True)),
            ("distributed network behavior created", set_request("distributed_network_behavior_created", True)),
            ("general lookup permission created", set_request("general_lookup_permission_created", True)),
            ("arbitrary lookup permission created", set_request("arbitrary_lookup_permission_created", True)),
            ("unsupported commands permitted", set_request("unsupported_commands_permitted", True)),
            ("unsupported lookup keys permitted", set_request("unsupported_lookup_keys_permitted", True)),
            ("new lookup entry created", set_request("new_lookup_entry_created", True)),
            ("new signal accepted", set_request("new_signal_accepted", True)),
            ("new entry accepted", set_request("new_entry_accepted", True)),
            ("new relevance object created", set_request("new_relevance_object_created", True)),
            ("new index entry created", set_request("new_index_entry_created", True)),
            ("filesystem discovery performed", set_request("filesystem_discovery_performed", True)),
            ("registry created", set_request("registry_created", True)),
            ("search surface created", set_request("search_surface_created", True)),
            ("query surface created", set_request("query_surface_created", True)),
            ("ranking surface created", set_request("ranking_surface_created", True)),
            ("scoring surface created", set_request("scoring_surface_created", True)),
            ("priority surface created", set_request("priority_surface_created", True)),
            ("validity judgment created", set_request("validity_judgment_created", True)),
            ("truth judgment created", set_request("truth_judgment_created", True)),
            ("authority judgment created", set_request("authority_judgment_created", True)),
            ("currentness judgment created", set_request("currentness_judgment_created", True)),
            ("repeated reception permission created", set_request("repeated_reception_permission_created", True)),
            ("arbitrary reception created", set_request("arbitrary_reception_created", True)),
            ("feed created", set_request("feed_created", True)),
            ("source transfer occurred", set_request("source_transfer_occurred", True)),
            ("source receipt occurred", set_request("source_receipt_occurred", True)),
            ("source created", set_request("source_created", True)),
            ("authority created", set_request("authority_created", True)),
            ("currentness created", set_request("currentness_created", True)),
            ("truth created", set_request("truth_created", True)),
            ("synchronization created", set_request("synchronization_created", True)),
            ("participation authorized", set_request("participation_authorized", True)),
            ("participant role created", set_request("participant_role_created", True)),
            ("deployment created", set_request("deployment_created", True)),
            ("public release created", set_request("public_release_created", True)),
            ("broader reusable permission created", set_request("broader_reusable_permission_created", True)),
            ("follow-on work authorized", set_request("follow_on_work_authorized", True)),
            ("consumed request reopened", set_request("consumed_request_reopened", True)),
            ("authorization token reused", set_request("authorization_token_reused", True)),
            ("artifact existence treated as lookup-result authority", set_request("artifact_existence_treated_as_lookup_result_authority", True)),
            ("latest file posture treated as lookup-result authority", set_request("latest_file_posture_treated_as_lookup_result_authority", True)),
            ("repo-local availability treated as lookup-result authority", set_request("repo_local_availability_treated_as_lookup_result_authority", True)),
            ("hidden repo state used as lookup-result content", set_request("hidden_repo_state_used_as_lookup_result_content", True)),
            ("hidden repo state used as lookup-result authority", set_request("hidden_repo_state_used_as_lookup_result_authority", True)),
            ("predecessor failure evidence hidden repaired claimed passed", set_request("predecessor_failure_repaired", True)),
            ("required non-claim missing or flipped", missing_non_claim),
        )

    def test_representative_blocking_behavior(self) -> None:
        malformed_results = (
            resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min(None),
            resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min(["not", "mapping"]),  # type: ignore[arg-type]
        )
        for result in malformed_results:
            self.assert_blocked_with_public_code(result)
            self.assert_blocked_non_creation_posture(result)

        for index, (name, mutate) in enumerate(self.representative_block_cases(), start=1):
            with self.subTest(name=name):
                with tempfile.TemporaryDirectory() as tmp:
                    directory = Path(tmp)
                    boundary_path, performed_path, boundary, performed = self.write_basis_artifacts(
                        directory,
                        name=self.safe_json_filename(name, index=index).removesuffix(".json"),
                    )
                    request = self.valid_request_for_paths(boundary_path, performed_path)
                    mutate(request, boundary, performed, boundary_path, performed_path, directory)
                    if boundary_path.exists():
                        try:
                            current = json.loads(boundary_path.read_text(encoding="utf-8"))
                        except json.JSONDecodeError:
                            current = None
                        if isinstance(current, dict):
                            self.write_json(boundary_path, boundary)
                    if performed_path.exists():
                        try:
                            current = json.loads(performed_path.read_text(encoding="utf-8"))
                        except json.JSONDecodeError:
                            current = None
                        if isinstance(current, dict):
                            self.write_json(performed_path, performed)
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    self.assert_blocked_non_creation_posture(result)

    def test_official_values_are_preserved(self) -> None:
        result, temp, _boundary_path, _performed_path = self.clean_recorded_result()
        try:
            lookup_result = self.lookup_result(result)
            self.assertEqual(lookup_result["lookup_result_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT")
            self.assertEqual(lookup_result["lookup_result_scope"], "SELECTED_LOOKUP_RESULT_ONLY")
            self.assertEqual(lookup_result["selected_command"], "state")
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            for outcome in (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT_BLOCKED",
            ):
                self.assertIn(outcome, resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            for official in OFFICIAL_VALUES:
                self.assertIn(official, serialized)
            self.assertNotIn("[REDACTED_RAW_BODY]", lookup_result.values())
        finally:
            temp.cleanup()

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            boundary_path, performed_path, boundary, performed = self.write_basis_artifacts(directory)
            boundary["raw_lookup_result_boundary_body"] = HOSTILE_SENTINELS[2]
            performed["raw_lookup_performed_body"] = HOSTILE_SENTINELS[3]
            self.write_json(boundary_path, boundary)
            self.write_json(performed_path, performed)
            request = self.valid_request_for_paths(boundary_path, performed_path)
            request["additional_basis_context"] = {
                "raw_lookup_result_body": HOSTILE_SENTINELS[0],
                "hidden_repo_state": HOSTILE_SENTINELS[-1],
            }
            request["not_recorded_basis"] = [{"raw_body": HOSTILE_SENTINELS[1]}]
            request_before = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min(request)

            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assert_blocked_with_public_code(result)
            self.assert_no_hostile_sentinels(result)
            serialized = json.dumps(result, sort_keys=True)
            for official in OFFICIAL_VALUES:
                self.assertIn(official, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assert_closure_tokens_false(result)
            for key in (
                "operation_permission_created",
                "runtime_permission_created",
                "public_api_created",
                "participant_facing_interface_created",
                "distributed_network_behavior_created",
                "follow_on_work_authorized",
            ):
                self.assertIs(self.non_claims(result)[key], False)
            self.assertEqual(request, request_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            boundary_path, performed_path, _boundary, _performed = self.write_basis_artifacts(directory)
            request = self.valid_request_for_paths(boundary_path, performed_path)
            request_path = directory / "request.json"
            self.write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min_from_path(request_path)
            summary = resolver.build_local_relevance_medium_read_only_lookup_result_v0_min_summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            malformed_path = directory / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min_from_path(
                malformed_path
            )
            self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)
            array_path = directory / "array.json"
            self.write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min_from_path(array_path)
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            missing_result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min_from_path(
                directory / "missing.json"
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)

            output_root = directory / "local_relevance_medium_read_only_lookup_result_v0_min"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_lookup_result_v0_min_result(result)
                second_path = resolver.write_local_relevance_medium_read_only_lookup_result_v0_min_result(result)
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(first_path.parent.exists())
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn("local_relevance_medium_read_only_lookup_result_v0_min", str(first_path))
            self.assert_not_under_forbidden_roots(first_path)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            boundary_path, performed_path, boundary, performed = self.write_basis_artifacts(directory)
            boundary_before = copy.deepcopy(boundary)
            performed_before = copy.deepcopy(performed)
            request = self.valid_request_for_paths(boundary_path, performed_path)
            request["additional_basis_context"] = {
                "nested": {
                    "raw_lookup_result_body": HOSTILE_SENTINELS[0],
                    "hidden_repo_state": HOSTILE_SENTINELS[-1],
                }
            }
            request_before = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_lookup_result_v0_min(request)

            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(request, request_before)
            self.assertEqual(boundary, boundary_before)
            self.assertEqual(performed, performed_before)
            self.assertEqual(request["selected_lookup_result_boundary_artifact"], request_before["selected_lookup_result_boundary_artifact"])
            self.assertEqual(request["selected_lookup_performed_artifact"], request_before["selected_lookup_performed_artifact"])
            self.assertEqual(request["selected_command"], "state")
            self.assertEqual(request["lookup_result_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_RESULT")
            self.assertEqual(request["lookup_result_scope"], "SELECTED_LOOKUP_RESULT_ONLY")
            self.assertIs(request["declared_non_claims"]["consumed_request_reopened"], False)
            self.assertIs(request["declared_non_claims"]["authorization_token_reused"], False)

    def test_predecessor_failure_preservation(self) -> None:
        result, temp, _boundary_path, _performed_path = self.clean_recorded_result()
        try:
            statement = self.statement(result)
            summary = result["local_relevance_medium_read_only_lookup_result_summary"]
            self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
            self.assertIs(statement["consumed_request_token_remains_closed"], True)
            self.assertIs(statement["authorization_token_reuse_blocked"], True)
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(summary["result_level_non_claims_canonical_false"], True)
            self.assertIs(summary["consumed_request_token_remains_closed"], True)
            self.assertIs(summary["authorization_token_reuse_blocked"], True)
            for key in (
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
                "consumed_request_reopened",
                "authorization_token_reused",
            ):
                self.assertIs(self.non_claims(result)[key], False)
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main()
