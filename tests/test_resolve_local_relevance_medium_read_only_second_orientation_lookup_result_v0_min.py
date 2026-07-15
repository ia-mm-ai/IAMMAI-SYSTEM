"""Tests for the local relevance medium read-only second orientation lookup result resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT object. It
verifies that the resolver reads one clean first read-only orientation lookup
result artifact as predecessor evidence, reads one clean read-only orientation
index artifact as deterministic lookup basis, resolves declared key
second_orientation_locator only, returns one already-standing second target,
and keeps every reusable-permission, lookup-pair coverage, discovery, registry,
search, ranking, authority, runtime, interface, distributed, and follow-on
posture false.
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

import resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min as resolver  # noqa: E402


FIRST_LOCATOR_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min/"
    "local_relevance_orientation_index_entry_reference_review_001__"
    "local_relevance_orientation_index_entry_v0_min_result.json"
)
SECOND_LOCATOR_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min/"
    "local_relevance_medium_second_local_relevance_orientation_index_entry_reference_review_001__"
    "local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_result.json"
)
FIRST_ORIENTATION_VIEW_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min/"
    "relevance_orientation_view_reference_review_001__relevance_orientation_view_v0_min_result.json"
)
SECOND_ORIENTATION_VIEW_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min/"
    "local_relevance_medium_second_relevance_orientation_view_reference_review_001__"
    "local_relevance_medium_second_relevance_orientation_view_v0_min_result.json"
)

DEFAULT_FIRST_LOOKUP_RESULT_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_lookup_result_v0_min/"
    "local_relevance_medium_read_only_orientation_lookup_result_reference_review_001__"
    "local_relevance_medium_read_only_orientation_lookup_result_v0_min_result.json"
)
DEFAULT_ORIENTATION_INDEX_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_index_system_v0_min/"
    "local_relevance_medium_read_only_orientation_index_reference_review_001__"
    "local_relevance_medium_read_only_orientation_index_system_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    "local_relevance_medium_read_only_second_orientation_lookup_result_metadata",
    "declared_local_relevance_medium_read_only_second_orientation_lookup_result_question",
    "selected_first_lookup_result_artifact_basis",
    "selected_read_only_orientation_index_artifact_basis",
    "local_relevance_medium_read_only_second_orientation_lookup_result",
    "local_relevance_medium_read_only_second_orientation_lookup_result_checks",
    "local_relevance_medium_read_only_second_orientation_lookup_result_statement",
    "local_relevance_medium_read_only_second_orientation_lookup_result_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_second_orientation_lookup_result_summary",
)

FORBIDDEN_OBJECT_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_second_orientation_lookup_result_checks",
    "non_claims",
    "local_relevance_medium_read_only_second_orientation_lookup_result_summary",
    "local_relevance_medium_read_only_second_orientation_lookup_result_metadata",
)

SECOND_LOOKUP_RESULT_OBJECT_FALSE_FIELDS = (
    "lookup_pair_coverage_created",
    "reusable_lookup_permission_created",
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
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "follow_on_work_authorized",
)

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "local_relevance_medium_read_only_second_orientation_lookup_result_recorded",
    "basis_first_lookup_result_artifact_preserved",
    "basis_read_only_orientation_index_artifact_preserved",
    "declared_lookup_key_preserved",
    "declared_lookup_key_is_second_orientation_locator",
    "lookup_key_supported",
    "lookup_target_found",
    "selected_received_signal_id_preserved",
    "selected_locator_entry_artifact_preserved",
    "selected_orientation_view_artifact_preserved",
    "lookup_table_has_two_entries",
    "lookup_order_is_deterministic",
    "lookup_key_count_is_two",
    "lookup_target_count_is_two",
    "accepted_new_entries_count_is_zero",
    "deterministic_local_lookup_preserved",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_INDEX_SYSTEM_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_INDEX_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _first_lookup_artifact() -> dict[str, Any]:
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_RECORDED",
        "local_relevance_medium_read_only_orientation_lookup_result_metadata": {
            "result_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min",
        },
        "local_relevance_medium_read_only_orientation_lookup_result_summary": {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 155,
        },
        "local_relevance_medium_read_only_orientation_lookup_result": {
            "lookup_result_id": "local_relevance_medium_read_only_orientation_lookup_result_001",
            "lookup_result_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT",
            "lookup_result_version": "0.1.0",
            "lookup_result_scope": "ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY",
            "declared_lookup_key": "first_orientation_locator",
            "selected_received_signal_id": "bounded_relevance_signal_001",
            "selected_locator_entry_artifact": FIRST_LOCATOR_ARTIFACT,
            "selected_orientation_view_artifact": FIRST_ORIENTATION_VIEW_ARTIFACT,
        },
        "local_relevance_medium_read_only_orientation_lookup_result_checks": [
            {
                "check_name": "synthetic first lookup result artifact clean",
                "passed": True,
                "expected_posture": "recorded first lookup result",
                "actual_posture": "recorded first lookup result",
            }
        ],
    }


def _orientation_index_artifact() -> dict[str, Any]:
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_RECORDED",
        "local_relevance_medium_read_only_orientation_index_system_metadata": {
            "result_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_read_only_orientation_index_system_v0_min",
        },
        "local_relevance_medium_read_only_orientation_index_system_summary": {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 100,
        },
        "local_relevance_medium_read_only_orientation_index": {
            "orientation_index_id": "local_relevance_medium_read_only_orientation_index_001",
            "orientation_index_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
            "orientation_index_system_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
            "orientation_index_scope": "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
            "orientation_index_version": "0.1.0",
            "orientation_index_system_version": "0.1.0",
            "lookup_table": {
                "first_orientation_locator": {
                    "lookup_key": "first_orientation_locator",
                    "received_signal_id": "bounded_relevance_signal_001",
                    "locator_entry_artifact": FIRST_LOCATOR_ARTIFACT,
                    "orientation_view_artifact": FIRST_ORIENTATION_VIEW_ARTIFACT,
                },
                "second_orientation_locator": {
                    "lookup_key": "second_orientation_locator",
                    "received_signal_id": "bounded_relevance_signal_002",
                    "locator_entry_artifact": SECOND_LOCATOR_ARTIFACT,
                    "orientation_view_artifact": SECOND_ORIENTATION_VIEW_ARTIFACT,
                },
            },
            "lookup_order": ["first_orientation_locator", "second_orientation_locator"],
            "lookup_key_count": 2,
            "lookup_target_count": 2,
            "accepted_new_entries_count": 0,
            "deterministic_local_lookup_enabled": True,
        },
        "local_relevance_medium_read_only_orientation_index_system_checks": [
            {
                "check_name": "synthetic read-only orientation index artifact clean",
                "passed": True,
                "expected_posture": "recorded read-only orientation index",
                "actual_posture": "recorded read-only orientation index",
            }
        ],
    }


def _write_synthetic_basis(
    root: Path,
    first_mutator: Callable[[dict[str, Any]], None] | None = None,
    index_mutator: Callable[[dict[str, Any]], None] | None = None,
) -> tuple[Path, Path, dict[str, Any], dict[str, Any]]:
    first = _first_lookup_artifact()
    index = _orientation_index_artifact()
    if first_mutator is not None:
        first_mutator(first)
    if index_mutator is not None:
        index_mutator(index)
    first_path = root / "first_lookup_result.json"
    index_path = root / "read_only_orientation_index.json"
    _write_json(first_path, first)
    _write_json(index_path, index)
    return first_path, index_path, first, index


def _build_valid_request(first_path: Path, index_path: Path, **overrides: Any) -> dict[str, Any]:
    request = resolver.build_declared_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_request(
        selected_first_lookup_result_artifact=first_path,
        selected_read_only_orientation_index_artifact=index_path,
    )
    request.update(copy.deepcopy(overrides))
    return request


def _is_same_or_under(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


class LocalRelevanceMediumReadOnlySecondOrientationLookupResultTests(unittest.TestCase):
    def assert_not_blocked(self, result):
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def _second_lookup_result(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        value = result.get("local_relevance_medium_read_only_second_orientation_lookup_result")
        self.assertIsInstance(value, dict)
        return value

    def _statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        value = result.get("local_relevance_medium_read_only_second_orientation_lookup_result_statement")
        self.assertIsInstance(value, dict)
        return value

    def _checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        value = result.get("local_relevance_medium_read_only_second_orientation_lookup_result_checks")
        self.assertIsInstance(value, list)
        return value

    def _summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        value = result.get("local_relevance_medium_read_only_second_orientation_lookup_result_summary")
        self.assertIsInstance(value, dict)
        return value

    def _block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        code = block.get("block_code") or block.get("code")
        return code if isinstance(code, str) else None

    def _assert_public_codes(self, result: Mapping[str, Any]) -> None:
        for check in self._checks(result):
            for field in ("block_code", "failure_code"):
                code = check.get(field)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)
        code = self._block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)

    def _assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)

    def _assert_no_creation_posture_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in (
            "lookup_pair_coverage_created",
            "reusable_lookup_permission_created",
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
            "runtime_permission_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "operation_permission_created",
            "follow_on_work_authorized",
        ):
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)

    def _assert_second_lookup_result_separate_from_wrapper(self, result: Mapping[str, Any]) -> None:
        second_lookup_result = self._second_lookup_result(result)
        for key in FORBIDDEN_OBJECT_WRAPPER_FIELDS:
            self.assertNotIn(key, second_lookup_result)

    def _assert_second_lookup_target(self, second_lookup_result: Mapping[str, Any]) -> None:
        self.assertEqual(second_lookup_result["declared_lookup_key"], "second_orientation_locator")
        self.assertTrue(second_lookup_result["lookup_key_supported"])
        self.assertTrue(second_lookup_result["lookup_target_found"])
        self.assertEqual(second_lookup_result["selected_received_signal_id"], "bounded_relevance_signal_002")
        self.assertEqual(second_lookup_result["selected_locator_entry_artifact"], SECOND_LOCATOR_ARTIFACT)
        self.assertEqual(second_lookup_result["selected_orientation_view_artifact"], SECOND_ORIENTATION_VIEW_ARTIFACT)

    def _assert_success_statement(self, result: Mapping[str, Any]) -> None:
        statement = self._statement(result)
        for key in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True)

    def _assert_blocked_common(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        code = self._block_code(result)
        self.assertIsInstance(code, str)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreaterEqual(self._summary(result)["failed_check_count"], 1)
        self._assert_public_codes(result)
        self._assert_non_claims_canonical_false(result)
        self._assert_no_creation_posture_false(result)

    def _resolve_with(
        self,
        root: Path,
        request_mutator: Callable[[dict[str, Any], Path], None] | None = None,
        first_mutator: Callable[[dict[str, Any]], None] | None = None,
        index_mutator: Callable[[dict[str, Any]], None] | None = None,
    ) -> dict[str, Any]:
        first_path, index_path, _, _ = _write_synthetic_basis(root, first_mutator, index_mutator)
        request = _build_valid_request(first_path, index_path)
        if request_mutator is not None:
            request_mutator(request, root)
        return resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(request)

    def test_public_api_constants_and_output_root(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min",
            "resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_from_path",
            "write_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_result",
            "build_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_request",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_LOOKUP_RESULT_TYPE_VALUES",
            "SUPPORTED_SECOND_LOOKUP_RESULT_SCOPE_VALUES",
            "REQUIRED_SECOND_LOOKUP_KEY",
            "LOOKUP_ORDER",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min",
        )
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT",
            resolver.SUPPORTED_SECOND_LOOKUP_RESULT_TYPE_VALUES,
        )
        self.assertIn(
            "ONE_DECLARED_SECOND_ORIENTATION_LOOKUP_KEY_ONLY",
            resolver.SUPPORTED_SECOND_LOOKUP_RESULT_SCOPE_VALUES,
        )
        self.assertEqual(resolver.REQUIRED_SECOND_LOOKUP_KEY, "second_orientation_locator")
        self.assertEqual(resolver.LOOKUP_ORDER, ["first_orientation_locator", "second_orientation_locator"])

        output_root = Path(resolver.OUTPUT_ROOT)
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            self.assertFalse(
                output_root == forbidden or _is_same_or_under(output_root, forbidden),
                f"{output_root} unexpectedly writes under {forbidden}",
            )

    def test_records_from_synthetic_artifacts_for_second_locator(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, index_path, _, _ = _write_synthetic_basis(Path(tmp))
            request = _build_valid_request(first_path, index_path)
            result = resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(request)
            summary = resolver.build_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_summary(
                result
            )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min",
        )
        self.assertGreater(summary["passed_check_count"], 0)

        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        second_lookup_result = self._second_lookup_result(result)
        self.assertEqual(
            second_lookup_result["second_lookup_result_id"],
            "local_relevance_medium_read_only_second_orientation_lookup_result_001",
        )
        self.assertEqual(
            second_lookup_result["second_lookup_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT",
        )
        self.assertEqual(second_lookup_result["second_lookup_result_version"], "0.1.0")
        self.assertEqual(
            second_lookup_result["second_lookup_result_scope"],
            "ONE_DECLARED_SECOND_ORIENTATION_LOOKUP_KEY_ONLY",
        )
        self.assertEqual(second_lookup_result["basis_first_lookup_result_artifact"], str(first_path))
        self.assertEqual(
            second_lookup_result["basis_first_lookup_result_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_RECORDED",
        )
        self.assertEqual(second_lookup_result["basis_first_lookup_result_result_version"], "0.1.0")
        self.assertEqual(second_lookup_result["basis_first_lookup_result_failed_check_count"], 0)
        self.assertEqual(second_lookup_result["basis_read_only_orientation_index_artifact"], str(index_path))
        self.assertEqual(
            second_lookup_result["basis_read_only_orientation_index_system_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_RECORDED",
        )
        self.assertEqual(second_lookup_result["basis_read_only_orientation_index_system_result_version"], "0.1.0")
        self.assertEqual(second_lookup_result["basis_read_only_orientation_index_system_failed_check_count"], 0)
        self.assertEqual(
            second_lookup_result["basis_orientation_index_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
        )
        self.assertEqual(
            second_lookup_result["basis_orientation_index_system_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
        )
        self.assertEqual(
            second_lookup_result["basis_orientation_index_scope"],
            "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
        )
        self._assert_second_lookup_target(second_lookup_result)
        self.assertEqual(second_lookup_result["lookup_table_key_count"], 2)
        self.assertEqual(second_lookup_result["lookup_table_target_count"], 2)
        self.assertEqual(second_lookup_result["lookup_order"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(second_lookup_result["accepted_new_entries_count"], 0)
        self.assertTrue(second_lookup_result["deterministic_local_lookup_preserved"])
        self.assertTrue(second_lookup_result["second_lookup_result_recorded"])
        for key in SECOND_LOOKUP_RESULT_OBJECT_FALSE_FIELDS:
            self.assertIn(key, second_lookup_result)
            self.assertIs(second_lookup_result[key], False)

        self._assert_second_lookup_result_separate_from_wrapper(result)
        self._assert_success_statement(result)
        self._assert_non_claims_canonical_false(result)

    def test_records_from_default_artifacts_when_present(self) -> None:
        if not DEFAULT_FIRST_LOOKUP_RESULT_ARTIFACT.exists() or not DEFAULT_ORIENTATION_INDEX_ARTIFACT.exists():
            self.skipTest("default first lookup or read-only orientation index artifact is not present")

        with (
            mock.patch.object(resolver, "DEFAULT_FIRST_LOOKUP_RESULT_ARTIFACT", DEFAULT_FIRST_LOOKUP_RESULT_ARTIFACT),
            mock.patch.object(
                resolver,
                "DEFAULT_READ_ONLY_ORIENTATION_INDEX_ARTIFACT",
                DEFAULT_ORIENTATION_INDEX_ARTIFACT,
            ),
        ):
            request = resolver.build_declared_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(request)
        summary = resolver.build_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_summary(result)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        second_lookup_result = self._second_lookup_result(result)
        self.assertEqual(
            second_lookup_result["second_lookup_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT",
        )
        self.assertEqual(
            second_lookup_result["second_lookup_result_scope"],
            "ONE_DECLARED_SECOND_ORIENTATION_LOOKUP_KEY_ONLY",
        )
        self.assertEqual(second_lookup_result["declared_lookup_key"], "second_orientation_locator")
        self.assertEqual(second_lookup_result["selected_received_signal_id"], "bounded_relevance_signal_002")
        self.assertTrue(second_lookup_result["selected_locator_entry_artifact"])
        self.assertTrue(second_lookup_result["selected_orientation_view_artifact"])
        self.assertEqual(second_lookup_result["lookup_table_key_count"], 2)
        self.assertEqual(second_lookup_result["lookup_order"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(second_lookup_result["accepted_new_entries_count"], 0)
        self.assertTrue(second_lookup_result["deterministic_local_lookup_preserved"])
        for key in SECOND_LOOKUP_RESULT_OBJECT_FALSE_FIELDS:
            self.assertIs(second_lookup_result[key], False)
        self._assert_no_creation_posture_false(result)

    def test_required_false_non_claims_canonicalize_and_block_when_flipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, index_path, _, _ = _write_synthetic_basis(Path(tmp))
            clean_request = _build_valid_request(first_path, index_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(
                        request
                    )
                    self._assert_blocked_common(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertNotEqual(result["non_claims"][key], True)

    def test_representative_blocking_behavior(self) -> None:
        def set_request(field: str, value: Any) -> Callable[[dict[str, Any], Path], None]:
            return lambda request, _root: request.__setitem__(field, value)

        def pop_request(field: str) -> Callable[[dict[str, Any], Path], None]:
            return lambda request, _root: request.pop(field, None)

        def set_flag(field: str) -> Callable[[dict[str, Any], Path], None]:
            return set_request(field, True)

        def first_version_bad(first: dict[str, Any]) -> None:
            first["local_relevance_medium_read_only_orientation_lookup_result_metadata"]["result_version"] = "9.9.9"
            first["local_relevance_medium_read_only_orientation_lookup_result_summary"]["result_version"] = "9.9.9"
            first["local_relevance_medium_read_only_orientation_lookup_result"]["lookup_result_version"] = "9.9.9"

        def first_failed(first: dict[str, Any]) -> None:
            first["local_relevance_medium_read_only_orientation_lookup_result_summary"]["failed_check_count"] = 1

        def index_version_bad(index: dict[str, Any]) -> None:
            index["local_relevance_medium_read_only_orientation_index_system_metadata"]["result_version"] = "9.9.9"
            index["local_relevance_medium_read_only_orientation_index_system_summary"]["result_version"] = "9.9.9"
            index["local_relevance_medium_read_only_orientation_index"]["orientation_index_version"] = "9.9.9"

        def index_failed(index: dict[str, Any]) -> None:
            index["local_relevance_medium_read_only_orientation_index_system_summary"]["failed_check_count"] = 1

        def second_target(index: dict[str, Any]) -> dict[str, Any]:
            return index["local_relevance_medium_read_only_orientation_index"]["lookup_table"][
                "second_orientation_locator"
            ]

        direct_cases: list[tuple[str, Callable[[Path], dict[str, Any]]]] = [
            ("missing request mapping", lambda _root: resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min({})),
            (
                "non-mapping request",
                lambda _root: resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(
                    ["not", "a", "mapping"]
                ),
            ),
        ]

        cases: list[
            tuple[
                str,
                Callable[[dict[str, Any], Path], None] | None,
                Callable[[dict[str, Any]], None] | None,
                Callable[[dict[str, Any]], None] | None,
            ]
        ] = [
            ("explicit block intent", set_request("local_relevance_medium_read_only_second_orientation_lookup_result_intent", resolver.INTENT_BLOCK), None, None),
            ("unsupported intent", set_request("local_relevance_medium_read_only_second_orientation_lookup_result_intent", "UNSUPPORTED_INTENT"), None, None),
            ("first lookup result artifact path missing", set_request("selected_first_lookup_result_artifact", ""), None, None),
            ("first lookup result artifact unreadable", lambda request, root: request.__setitem__("selected_first_lookup_result_artifact", str(root / "missing-first.json")), None, None),
            (
                "first lookup result artifact JSON array",
                lambda request, root: (_write_json(root / "first-array.json", []), request.__setitem__("selected_first_lookup_result_artifact", str(root / "first-array.json"))),
                None,
                None,
            ),
            ("first lookup result artifact not recorded", None, lambda first: first.__setitem__("outcome", "NOT_RECORDED"), None),
            ("first lookup result artifact failed checks present", None, first_failed, None),
            ("first lookup result artifact version not 0.1.0", None, first_version_bad, None),
            ("read-only orientation index artifact path missing", set_request("selected_read_only_orientation_index_artifact", ""), None, None),
            ("read-only orientation index artifact unreadable", lambda request, root: request.__setitem__("selected_read_only_orientation_index_artifact", str(root / "missing-index.json")), None, None),
            (
                "read-only orientation index artifact JSON array",
                lambda request, root: (_write_json(root / "index-array.json", []), request.__setitem__("selected_read_only_orientation_index_artifact", str(root / "index-array.json"))),
                None,
                None,
            ),
            ("read-only orientation index artifact not recorded", None, None, lambda index: index.__setitem__("outcome", "NOT_RECORDED")),
            ("read-only orientation index artifact failed checks present", None, None, index_failed),
            ("read-only orientation index artifact version not 0.1.0", None, None, index_version_bad),
            ("read-only orientation index object missing", None, None, lambda index: index.pop("local_relevance_medium_read_only_orientation_index", None)),
            ("declared lookup key missing", pop_request("declared_lookup_key"), None, None),
            ("declared lookup key not second_orientation_locator", set_request("declared_lookup_key", "first_orientation_locator"), None, None),
            ("lookup target not found", None, None, lambda index: index["local_relevance_medium_read_only_orientation_index"]["lookup_table"].pop("second_orientation_locator", None)),
            ("selected received signal id not bounded_relevance_signal_002", None, None, lambda index: second_target(index).__setitem__("received_signal_id", "bounded_relevance_signal_999")),
            ("selected second locator entry artifact missing", None, None, lambda index: second_target(index).pop("locator_entry_artifact", None)),
            ("selected second orientation view artifact missing", None, None, lambda index: second_target(index).pop("orientation_view_artifact", None)),
            (
                "lookup table not two entries",
                None,
                None,
                lambda index: (
                    index["local_relevance_medium_read_only_orientation_index"]["lookup_table"].__setitem__(
                        "third_orientation_locator",
                        {"lookup_key": "third_orientation_locator", "received_signal_id": "bounded_relevance_signal_003"},
                    ),
                    index["local_relevance_medium_read_only_orientation_index"].__setitem__("lookup_key_count", 3),
                    index["local_relevance_medium_read_only_orientation_index"].__setitem__("lookup_target_count", 3),
                ),
            ),
            ("lookup table target count not two", None, None, lambda index: index["local_relevance_medium_read_only_orientation_index"].__setitem__("lookup_target_count", 3)),
            ("lookup order not deterministic", None, None, lambda index: index["local_relevance_medium_read_only_orientation_index"].__setitem__("lookup_order", ["second_orientation_locator", "first_orientation_locator"])),
            ("accepted new entries count not zero", None, None, lambda index: index["local_relevance_medium_read_only_orientation_index"].__setitem__("accepted_new_entries_count", 1)),
            ("deterministic local lookup not preserved", None, None, lambda index: index["local_relevance_medium_read_only_orientation_index"].__setitem__("deterministic_local_lookup_enabled", False)),
            ("second lookup result type missing", pop_request("second_lookup_result_type"), None, None),
            ("second lookup result type unsupported", set_request("second_lookup_result_type", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT"), None, None),
            ("second lookup result scope missing", pop_request("second_lookup_result_scope"), None, None),
            ("second lookup result scope unsupported", set_request("second_lookup_result_scope", "ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY"), None, None),
            ("second lookup result not recorded", set_flag("second_lookup_result_not_recorded"), None, None),
            ("lookup-pair coverage created", set_flag("lookup_pair_coverage_created"), None, None),
            ("reusable lookup permission created", set_flag("reusable_lookup_permission_created"), None, None),
            ("new signal accepted", set_flag("new_signal_accepted"), None, None),
            ("new entry accepted", set_flag("new_entry_accepted"), None, None),
            ("new relevance object created", set_flag("new_relevance_object_created"), None, None),
            ("new index entry created", set_flag("new_index_entry_created"), None, None),
            ("filesystem discovery performed", set_flag("filesystem_discovery_performed"), None, None),
            ("registry created", set_flag("registry_created"), None, None),
            ("search surface created", set_flag("search_surface_created"), None, None),
            ("query surface created", set_flag("query_surface_created"), None, None),
            ("ranking surface created", set_flag("ranking_surface_created"), None, None),
            ("scoring surface created", set_flag("scoring_surface_created"), None, None),
            ("priority surface created", set_flag("priority_surface_created"), None, None),
            ("validity judgment created", set_flag("validity_judgment_created"), None, None),
            ("truth judgment created", set_flag("truth_judgment_created"), None, None),
            ("authority judgment created", set_flag("authority_judgment_created"), None, None),
            ("currentness judgment created", set_flag("currentness_judgment_created"), None, None),
            ("repeated reception permission created", set_flag("repeated_reception_permission_created"), None, None),
            ("arbitrary reception created", set_flag("arbitrary_reception_created"), None, None),
            ("feed created", set_flag("feed_created"), None, None),
            ("source transfer occurred", set_flag("source_transfer_occurred"), None, None),
            ("source receipt occurred", set_flag("source_receipt_occurred"), None, None),
            ("source created", set_flag("source_created"), None, None),
            ("authority created", set_flag("authority_created"), None, None),
            ("currentness created", set_flag("currentness_created"), None, None),
            ("truth created", set_flag("truth_created"), None, None),
            ("action created", set_flag("action_created"), None, None),
            ("synchronization created", set_flag("synchronization_created"), None, None),
            ("participation authorized", set_flag("participation_authorized"), None, None),
            ("participant role created", set_flag("participant_role_created"), None, None),
            ("runtime permission created", set_flag("runtime_permission_created"), None, None),
            ("public API created", set_flag("public_api_created"), None, None),
            ("participant-facing interface created", set_flag("participant_facing_interface_created"), None, None),
            ("distributed network behavior created", set_flag("distributed_network_behavior_created"), None, None),
            ("deployment created", set_flag("deployment_created"), None, None),
            ("public release created", set_flag("public_release_created"), None, None),
            ("operation permission created", set_flag("operation_permission_created"), None, None),
            ("broader reusable permission created", set_flag("broader_reusable_permission_created"), None, None),
            ("follow-on work authorized", set_flag("follow_on_work_authorized"), None, None),
            ("artifact existence treated as second lookup result authority", set_flag("artifact_existence_treated_as_second_lookup_result_authority"), None, None),
            ("latest file posture treated as second lookup result authority", set_flag("latest_file_posture_treated_as_second_lookup_result_authority"), None, None),
            ("repo-local availability treated as second lookup result authority", set_flag("repo_local_availability_treated_as_second_lookup_result_authority"), None, None),
            ("hidden repo state used as second lookup result content", set_flag("hidden_repo_state_used_as_second_lookup_result_content"), None, None),
            ("hidden repo state used as second lookup result authority", set_flag("hidden_repo_state_used_as_second_lookup_result_authority"), None, None),
            ("predecessor failure repaired", set_flag("predecessor_failure_repaired"), None, None),
            ("predecessor failure hidden", set_flag("predecessor_failure_hidden"), None, None),
            ("predecessor failure claimed passed", set_flag("predecessor_failure_claimed_passed"), None, None),
            ("consumed request reopened", set_flag("consumed_request_reopened"), None, None),
            ("authorization token reused", set_flag("authorization_token_reused"), None, None),
            ("required non-claim missing", lambda request, _root: request["declared_non_claims"].pop("feed_created", None), None, None),
            ("required non-claim flipped", lambda request, _root: request["declared_non_claims"].__setitem__("feed_created", True), None, None),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, direct in direct_cases:
                with self.subTest(name=name):
                    self._assert_blocked_common(direct(root))
            for name, request_mutator, first_mutator, index_mutator in cases:
                with self.subTest(name=name):
                    result = self._resolve_with(root, request_mutator, first_mutator, index_mutator)
                    self._assert_blocked_common(result)

    def test_missing_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, index_path, _, _ = _write_synthetic_basis(Path(tmp))
            clean_request = _build_valid_request(first_path, index_path)
            variants = {
                "removed mapping": lambda request: request.pop("declared_non_claims", None),
                "empty mapping": lambda request: request.__setitem__("declared_non_claims", {}),
                "one missing": lambda request: request["declared_non_claims"].pop("feed_created", None),
                "string": lambda request: request["declared_non_claims"].__setitem__("feed_created", "false"),
                "none": lambda request: request["declared_non_claims"].__setitem__("feed_created", None),
            }
            for name, mutate in variants.items():
                with self.subTest(name=name):
                    request = copy.deepcopy(clean_request)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(
                        request
                    )
                    self.assertIn(result["outcome"], {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS})
                    self._assert_public_codes(result)
                    self._assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, index_path, _, _ = _write_synthetic_basis(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(
                _build_valid_request(first_path, index_path)
            )

        second_lookup_result = self._second_lookup_result(result)
        self.assertEqual(
            second_lookup_result["second_lookup_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT",
        )
        self.assertEqual(
            second_lookup_result["second_lookup_result_scope"],
            "ONE_DECLARED_SECOND_ORIENTATION_LOOKUP_KEY_ONLY",
        )
        self.assertEqual(second_lookup_result["declared_lookup_key"], "second_orientation_locator")
        self.assertEqual(second_lookup_result["selected_received_signal_id"], "bounded_relevance_signal_002")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_BLOCKED",
            },
        )
        self.assertEqual(resolver.REQUIRED_SECOND_LOOKUP_KEY, "second_orientation_locator")
        serialized = json.dumps(result, sort_keys=True)
        self.assertNotIn("[REDACTED_RAW_CONTENT]", serialized)
        for official in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT",
            "ONE_DECLARED_SECOND_ORIENTATION_LOOKUP_KEY_ONLY",
            "second_orientation_locator",
            "bounded_relevance_signal_002",
        ):
            self.assertIn(official, serialized)

    def test_raw_hidden_hostile_content_containment_and_input_not_mutated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def mutate_first(first: dict[str, Any]) -> None:
                first["raw_lookup_result_body"] = HOSTILE_SENTINELS[2]
                first["local_relevance_medium_read_only_orientation_lookup_result"]["raw_full_body"] = (
                    HOSTILE_SENTINELS[5]
                )

            def mutate_index(index: dict[str, Any]) -> None:
                index["raw_orientation_index_body"] = HOSTILE_SENTINELS[4]
                second = index["local_relevance_medium_read_only_orientation_index"]["lookup_table"][
                    "second_orientation_locator"
                ]
                second["second_local_index_entry_body"] = HOSTILE_SENTINELS[1]

            first_path, index_path, _, _ = _write_synthetic_basis(root, mutate_first, mutate_index)
            request = _build_valid_request(first_path, index_path)
            request["raw_full_body"] = HOSTILE_SENTINELS[0]
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            request["nested_raw"] = {"raw_orientation_index_system_body": HOSTILE_SENTINELS[3]}
            request_before = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(request)

        self.assertEqual(request, request_before)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self._assert_public_codes(result)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        for official in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT",
            "ONE_DECLARED_SECOND_ORIENTATION_LOOKUP_KEY_ONLY",
            "second_orientation_locator",
            "bounded_relevance_signal_002",
        ):
            self.assertIn(official, serialized)
        self._assert_non_claims_canonical_false(result)
        self._assert_no_creation_posture_false(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first_path, index_path, _, _ = _write_synthetic_basis(root)
            request = _build_valid_request(first_path, index_path)
            request_path = root / "request.json"
            _write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_from_path(
                request_path
            )
            summary = resolver.build_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_summary(
                result
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            array_path = root / "array-request.json"
            _write_json(array_path, [])
            for path in (malformed_path, array_path, root / "missing-request.json"):
                with self.subTest(path=path.name):
                    malformed_result = (
                        resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_from_path(
                            path
                        )
                    )
                    self._assert_blocked_common(malformed_result)

            patched_output_root = root / EXPECTED_OUTPUT_ROOT.name
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_output_root):
                written = resolver.write_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_result(
                    result
                )
                written_again = (
                    resolver.write_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_result(
                        result
                    )
                )

            self.assertTrue(written.parent.exists())
            self.assertTrue(written.exists())
            self.assertTrue(written_again.exists())
            self.assertNotEqual(written, written_again)
            with written.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn("local_relevance_medium_read_only_second_orientation_lookup_result_v0_min", str(written))
            for forbidden in FORBIDDEN_OUTPUT_ROOTS:
                forbidden_abs = REPO_ROOT / forbidden
                self.assertFalse(_is_same_or_under(written.resolve(), forbidden_abs.resolve()))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first_artifact = _first_lookup_artifact()
            index_artifact = _orientation_index_artifact()
            first_before = copy.deepcopy(first_artifact)
            index_before = copy.deepcopy(index_artifact)
            first_path = root / "first.json"
            index_path = root / "index.json"
            _write_json(first_path, first_artifact)
            _write_json(index_path, index_artifact)

            request = _build_valid_request(first_path, index_path)
            request["posture"] = {
                "raw_full_body": "RAW_SECOND_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
                "nested": {"hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN"},
            }
            request_before = copy.deepcopy(request)
            non_claims_before = copy.deepcopy(request["declared_non_claims"])
            first_path_before = request["selected_first_lookup_result_artifact"]
            index_path_before = request["selected_read_only_orientation_index_artifact"]
            declared_key_before = request["declared_lookup_key"]
            type_before = request["second_lookup_result_type"]
            scope_before = request["second_lookup_result_scope"]

            resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(request)

        self.assertEqual(request, request_before)
        self.assertEqual(request["declared_non_claims"], non_claims_before)
        self.assertEqual(request["selected_first_lookup_result_artifact"], first_path_before)
        self.assertEqual(request["selected_read_only_orientation_index_artifact"], index_path_before)
        self.assertEqual(request["declared_lookup_key"], declared_key_before)
        self.assertEqual(request["second_lookup_result_type"], type_before)
        self.assertEqual(request["second_lookup_result_scope"], scope_before)
        self.assertEqual(first_artifact, first_before)
        self.assertEqual(index_artifact, index_before)
        self.assertEqual(request["posture"], request_before["posture"])

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, index_path, _, _ = _write_synthetic_basis(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(
                _build_valid_request(first_path, index_path)
            )
            summary = resolver.build_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_summary(
                result
            )

        statement = self._statement(result)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["predecessor_failure_not_repaired"], True)
        self.assertIs(statement["predecessor_failure_not_hidden"], True)
        self.assertIs(statement["predecessor_failure_not_claimed_passed"], True)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
