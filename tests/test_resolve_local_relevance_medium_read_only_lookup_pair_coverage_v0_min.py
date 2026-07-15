"""Tests for the local relevance medium read-only lookup-pair coverage resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE object. It verifies that
the resolver reads one clean first lookup result artifact, one clean second
lookup result artifact, and one clean read-only orientation index artifact as
lookup-basis evidence only. The coverage object records that both supported
lookup keys have clean individual lookup result artifacts, while remaining
read-only, local, coverage-shaped, and non-permission-shaped.

The suite does not create reusable lookup permission, general lookup
permission, a new lookup result, a new lookup entry, registry, search, query
surface, ranking, scoring, priority, validity judgment, truth judgment,
authority judgment, currentness judgment, repeated reception permission,
arbitrary reception, feed, new signal, new entry, new relevance object, new
index entry, filesystem discovery, source transfer, source receipt, runtime
permission, API, distributed behavior, operation permission, or follow-on work.
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

import resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min as resolver  # noqa: E402


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
DEFAULT_SECOND_LOOKUP_RESULT_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min/"
    "local_relevance_medium_read_only_second_orientation_lookup_result_reference_review_001__"
    "local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_result.json"
)
DEFAULT_ORIENTATION_INDEX_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_index_system_v0_min/"
    "local_relevance_medium_read_only_orientation_index_reference_review_001__"
    "local_relevance_medium_read_only_orientation_index_system_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_pair_coverage_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    "local_relevance_medium_read_only_lookup_pair_coverage_metadata",
    "declared_local_relevance_medium_read_only_lookup_pair_coverage_question",
    "selected_first_lookup_result_artifact_basis",
    "selected_second_lookup_result_artifact_basis",
    "selected_read_only_orientation_index_artifact_basis",
    "local_relevance_medium_read_only_lookup_pair_coverage",
    "local_relevance_medium_read_only_lookup_pair_coverage_checks",
    "local_relevance_medium_read_only_lookup_pair_coverage_statement",
    "local_relevance_medium_read_only_lookup_pair_coverage_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_lookup_pair_coverage_summary",
)

FORBIDDEN_OBJECT_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_lookup_pair_coverage_checks",
    "non_claims",
    "local_relevance_medium_read_only_lookup_pair_coverage_summary",
    "local_relevance_medium_read_only_lookup_pair_coverage_metadata",
)

COVERAGE_OBJECT_FALSE_FIELDS = (
    "reusable_lookup_permission_created",
    "general_lookup_permission_created",
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
    "local_relevance_medium_read_only_lookup_pair_coverage_recorded",
    "basis_first_lookup_result_artifact_preserved",
    "basis_second_lookup_result_artifact_preserved",
    "basis_read_only_orientation_index_artifact_preserved",
    "supported_lookup_keys_preserved",
    "covered_lookup_keys_preserved",
    "supported_lookup_key_count_is_two",
    "covered_lookup_key_count_is_two",
    "both_supported_lookup_keys_covered",
    "first_declared_lookup_key_preserved",
    "second_declared_lookup_key_preserved",
    "first_selected_received_signal_id_preserved",
    "second_selected_received_signal_id_preserved",
    "first_and_second_selected_received_signal_ids_distinct",
    "first_selected_locator_entry_artifact_preserved",
    "second_selected_locator_entry_artifact_preserved",
    "first_selected_orientation_view_artifact_preserved",
    "second_selected_orientation_view_artifact_preserved",
    "lookup_order_is_deterministic",
    "accepted_new_entries_count_is_zero",
    "deterministic_local_lookup_preserved",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PAIR_COVERAGE_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
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
            "passed_check_count": 100,
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


def _second_lookup_artifact() -> dict[str, Any]:
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_RECORDED",
        "local_relevance_medium_read_only_second_orientation_lookup_result_metadata": {
            "result_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min",
        },
        "local_relevance_medium_read_only_second_orientation_lookup_result_summary": {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 100,
        },
        "local_relevance_medium_read_only_second_orientation_lookup_result": {
            "second_lookup_result_id": "local_relevance_medium_read_only_second_orientation_lookup_result_001",
            "second_lookup_result_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT",
            "second_lookup_result_version": "0.1.0",
            "second_lookup_result_scope": "ONE_DECLARED_SECOND_ORIENTATION_LOOKUP_KEY_ONLY",
            "declared_lookup_key": "second_orientation_locator",
            "selected_received_signal_id": "bounded_relevance_signal_002",
            "selected_locator_entry_artifact": SECOND_LOCATOR_ARTIFACT,
            "selected_orientation_view_artifact": SECOND_ORIENTATION_VIEW_ARTIFACT,
        },
        "local_relevance_medium_read_only_second_orientation_lookup_result_checks": [
            {
                "check_name": "synthetic second lookup result artifact clean",
                "passed": True,
                "expected_posture": "recorded second lookup result",
                "actual_posture": "recorded second lookup result",
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
    second_mutator: Callable[[dict[str, Any]], None] | None = None,
    index_mutator: Callable[[dict[str, Any]], None] | None = None,
) -> tuple[Path, Path, Path, dict[str, Any], dict[str, Any], dict[str, Any]]:
    first = _first_lookup_artifact()
    second = _second_lookup_artifact()
    index = _orientation_index_artifact()
    if first_mutator is not None:
        first_mutator(first)
    if second_mutator is not None:
        second_mutator(second)
    if index_mutator is not None:
        index_mutator(index)
    first_path = root / "first_lookup_result.json"
    second_path = root / "second_lookup_result.json"
    index_path = root / "read_only_orientation_index.json"
    _write_json(first_path, first)
    _write_json(second_path, second)
    _write_json(index_path, index)
    return first_path, second_path, index_path, first, second, index


def _build_valid_request(
    first_path: Path,
    second_path: Path,
    index_path: Path,
    **overrides: Any,
) -> dict[str, Any]:
    request = resolver.build_declared_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_request(
        selected_first_lookup_result_artifact=first_path,
        selected_second_lookup_result_artifact=second_path,
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


class LocalRelevanceMediumReadOnlyLookupPairCoverageTests(unittest.TestCase):
    def assert_not_blocked(self, result):
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def _coverage(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        value = result.get("local_relevance_medium_read_only_lookup_pair_coverage")
        self.assertIsInstance(value, dict)
        return value

    def _statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        value = result.get("local_relevance_medium_read_only_lookup_pair_coverage_statement")
        self.assertIsInstance(value, dict)
        return value

    def _checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        value = result.get("local_relevance_medium_read_only_lookup_pair_coverage_checks")
        self.assertIsInstance(value, list)
        return value

    def _summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        value = result.get("local_relevance_medium_read_only_lookup_pair_coverage_summary")
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
        self._assert_non_claims_canonical_false(result)
        non_claims = result["non_claims"]
        for key in (
            "reusable_lookup_permission_created",
            "general_lookup_permission_created",
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

    def _assert_coverage_separate_from_wrapper(self, result: Mapping[str, Any]) -> None:
        coverage = self._coverage(result)
        for key in FORBIDDEN_OBJECT_WRAPPER_FIELDS:
            self.assertNotIn(key, coverage)

    def _assert_coverage_preserves_supported_keys(self, coverage: Mapping[str, Any]) -> None:
        self.assertEqual(coverage["supported_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(coverage["covered_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(coverage["supported_lookup_key_count"], 2)
        self.assertEqual(coverage["covered_lookup_key_count"], 2)
        self.assertEqual(coverage["first_declared_lookup_key"], "first_orientation_locator")
        self.assertEqual(coverage["second_declared_lookup_key"], "second_orientation_locator")
        self.assertEqual(coverage["first_selected_received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(coverage["second_selected_received_signal_id"], "bounded_relevance_signal_002")
        self.assertNotEqual(
            coverage["first_selected_received_signal_id"],
            coverage["second_selected_received_signal_id"],
        )
        self.assertEqual(coverage["first_selected_locator_entry_artifact"], FIRST_LOCATOR_ARTIFACT)
        self.assertEqual(coverage["second_selected_locator_entry_artifact"], SECOND_LOCATOR_ARTIFACT)
        self.assertEqual(coverage["first_selected_orientation_view_artifact"], FIRST_ORIENTATION_VIEW_ARTIFACT)
        self.assertEqual(coverage["second_selected_orientation_view_artifact"], SECOND_ORIENTATION_VIEW_ARTIFACT)
        self.assertEqual(coverage["lookup_order"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(coverage["accepted_new_entries_count"], 0)
        self.assertIs(coverage["deterministic_local_lookup_preserved"], True)

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
        self._assert_no_creation_posture_false(result)

    def _resolve_with(
        self,
        root: Path,
        request_mutator: Callable[[dict[str, Any], Path], None] | None = None,
        first_mutator: Callable[[dict[str, Any]], None] | None = None,
        second_mutator: Callable[[dict[str, Any]], None] | None = None,
        index_mutator: Callable[[dict[str, Any]], None] | None = None,
    ) -> dict[str, Any]:
        first_path, second_path, index_path, _, _, _ = _write_synthetic_basis(
            root,
            first_mutator,
            second_mutator,
            index_mutator,
        )
        request = _build_valid_request(first_path, second_path, index_path)
        if request_mutator is not None:
            request_mutator(request, root)
        return resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(request)

    def test_public_api_constants_and_output_root(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min",
            "resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_from_path",
            "write_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_result",
            "build_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_request",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_LOOKUP_PAIR_COVERAGE_TYPE_VALUES",
            "SUPPORTED_LOOKUP_PAIR_COVERAGE_SCOPE_VALUES",
            "SUPPORTED_LOOKUP_KEYS",
            "LOOKUP_ORDER",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min",
        )
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE",
            resolver.SUPPORTED_LOOKUP_PAIR_COVERAGE_TYPE_VALUES,
        )
        self.assertIn(
            "BOTH_SUPPORTED_ORIENTATION_LOOKUP_KEYS_COVERED_ONLY",
            resolver.SUPPORTED_LOOKUP_PAIR_COVERAGE_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SUPPORTED_LOOKUP_KEYS, ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(resolver.LOOKUP_ORDER, ["first_orientation_locator", "second_orientation_locator"])

        output_root = Path(resolver.OUTPUT_ROOT)
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            self.assertFalse(
                output_root == forbidden or _is_same_or_under(output_root, forbidden),
                f"{output_root} unexpectedly writes under {forbidden}",
            )

    def test_records_from_synthetic_artifacts_for_lookup_pair_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, second_path, index_path, _, _, _ = _write_synthetic_basis(Path(tmp))
            request = _build_valid_request(first_path, second_path, index_path)
            result = resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(request)
            summary = resolver.build_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min",
        )
        self.assertGreater(summary["passed_check_count"], 0)

        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        coverage = self._coverage(result)
        self.assertEqual(coverage["lookup_pair_coverage_id"], "local_relevance_medium_read_only_lookup_pair_coverage_001")
        self.assertEqual(coverage["lookup_pair_coverage_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE")
        self.assertEqual(coverage["lookup_pair_coverage_version"], "0.1.0")
        self.assertEqual(coverage["lookup_pair_coverage_scope"], "BOTH_SUPPORTED_ORIENTATION_LOOKUP_KEYS_COVERED_ONLY")
        self.assertEqual(coverage["basis_first_lookup_result_artifact"], str(first_path))
        self.assertEqual(
            coverage["basis_first_lookup_result_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_RECORDED",
        )
        self.assertEqual(coverage["basis_first_lookup_result_result_version"], "0.1.0")
        self.assertEqual(coverage["basis_first_lookup_result_failed_check_count"], 0)
        self.assertEqual(coverage["basis_second_lookup_result_artifact"], str(second_path))
        self.assertEqual(
            coverage["basis_second_lookup_result_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_RECORDED",
        )
        self.assertEqual(coverage["basis_second_lookup_result_result_version"], "0.1.0")
        self.assertEqual(coverage["basis_second_lookup_result_failed_check_count"], 0)
        self.assertEqual(coverage["basis_read_only_orientation_index_artifact"], str(index_path))
        self.assertEqual(coverage["lookup_table_key_count"], 2)
        self.assertEqual(coverage["lookup_table_target_count"], 2)
        self._assert_coverage_preserves_supported_keys(coverage)
        self.assertIs(coverage["lookup_pair_coverage_recorded"], True)
        for key in COVERAGE_OBJECT_FALSE_FIELDS:
            self.assertIn(key, coverage)
            self.assertIs(coverage[key], False)

        self._assert_coverage_separate_from_wrapper(result)
        self._assert_success_statement(result)
        self._assert_non_claims_canonical_false(result)

    def test_records_from_default_artifacts_when_present(self) -> None:
        if (
            not DEFAULT_FIRST_LOOKUP_RESULT_ARTIFACT.exists()
            or not DEFAULT_SECOND_LOOKUP_RESULT_ARTIFACT.exists()
            or not DEFAULT_ORIENTATION_INDEX_ARTIFACT.exists()
        ):
            self.skipTest("default lookup-pair coverage basis artifacts are not present")

        request = resolver.build_declared_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(request)
        summary = resolver.build_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_summary(result)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        coverage = self._coverage(result)
        self.assertEqual(coverage["lookup_pair_coverage_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE")
        self.assertEqual(coverage["lookup_pair_coverage_scope"], "BOTH_SUPPORTED_ORIENTATION_LOOKUP_KEYS_COVERED_ONLY")
        self.assertEqual(coverage["supported_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(coverage["covered_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(coverage["supported_lookup_key_count"], 2)
        self.assertEqual(coverage["covered_lookup_key_count"], 2)
        self.assertEqual(coverage["first_selected_received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(coverage["second_selected_received_signal_id"], "bounded_relevance_signal_002")
        self.assertNotEqual(coverage["first_selected_received_signal_id"], coverage["second_selected_received_signal_id"])
        self.assertTrue(coverage["first_selected_locator_entry_artifact"])
        self.assertTrue(coverage["second_selected_locator_entry_artifact"])
        self.assertTrue(coverage["first_selected_orientation_view_artifact"])
        self.assertTrue(coverage["second_selected_orientation_view_artifact"])
        self.assertEqual(coverage["lookup_order"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(coverage["accepted_new_entries_count"], 0)
        self.assertTrue(coverage["deterministic_local_lookup_preserved"])
        for key in COVERAGE_OBJECT_FALSE_FIELDS:
            self.assertIs(coverage[key], False)
        self._assert_no_creation_posture_false(result)

    def test_required_false_non_claims_canonicalize_and_block_when_flipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, second_path, index_path, _, _, _ = _write_synthetic_basis(Path(tmp))
            clean_request = _build_valid_request(first_path, second_path, index_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(request)
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

        def first_object(first: dict[str, Any]) -> dict[str, Any]:
            return first["local_relevance_medium_read_only_orientation_lookup_result"]

        def second_object(second: dict[str, Any]) -> dict[str, Any]:
            return second["local_relevance_medium_read_only_second_orientation_lookup_result"]

        def index_object(index: dict[str, Any]) -> dict[str, Any]:
            return index["local_relevance_medium_read_only_orientation_index"]

        def first_version_bad(first: dict[str, Any]) -> None:
            first["local_relevance_medium_read_only_orientation_lookup_result_metadata"]["result_version"] = "9.9.9"
            first["local_relevance_medium_read_only_orientation_lookup_result_summary"]["result_version"] = "9.9.9"
            first_object(first)["lookup_result_version"] = "9.9.9"

        def second_version_bad(second: dict[str, Any]) -> None:
            second["local_relevance_medium_read_only_second_orientation_lookup_result_metadata"]["result_version"] = "9.9.9"
            second["local_relevance_medium_read_only_second_orientation_lookup_result_summary"]["result_version"] = "9.9.9"
            second_object(second)["second_lookup_result_version"] = "9.9.9"

        def index_version_bad(index: dict[str, Any]) -> None:
            index["local_relevance_medium_read_only_orientation_index_system_metadata"]["result_version"] = "9.9.9"
            index["local_relevance_medium_read_only_orientation_index_system_summary"]["result_version"] = "9.9.9"
            index_object(index)["orientation_index_version"] = "9.9.9"

        direct_cases: list[tuple[str, Callable[[Path], dict[str, Any]]]] = [
            ("missing request mapping", lambda _root: resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min({})),
            (
                "non-mapping request",
                lambda _root: resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(
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
                Callable[[dict[str, Any]], None] | None,
            ]
        ] = [
            ("explicit block intent", set_request("local_relevance_medium_read_only_lookup_pair_coverage_intent", resolver.INTENT_BLOCK), None, None, None),
            ("unsupported intent", set_request("local_relevance_medium_read_only_lookup_pair_coverage_intent", "UNSUPPORTED_INTENT"), None, None, None),
            ("first lookup result artifact path missing", set_request("selected_first_lookup_result_artifact", ""), None, None, None),
            ("first lookup result artifact unreadable", lambda request, root: request.__setitem__("selected_first_lookup_result_artifact", str(root / "missing-first.json")), None, None, None),
            (
                "first lookup result artifact JSON array",
                lambda request, root: (_write_json(root / "first-array.json", []), request.__setitem__("selected_first_lookup_result_artifact", str(root / "first-array.json"))),
                None,
                None,
                None,
            ),
            ("first lookup result artifact not recorded", None, lambda first: first.__setitem__("outcome", "NOT_RECORDED"), None, None),
            ("first lookup result artifact failed checks present", None, lambda first: first["local_relevance_medium_read_only_orientation_lookup_result_summary"].__setitem__("failed_check_count", 1), None, None),
            ("first lookup result artifact version not 0.1.0", None, first_version_bad, None, None),
            ("second lookup result artifact path missing", set_request("selected_second_lookup_result_artifact", ""), None, None, None),
            ("second lookup result artifact unreadable", lambda request, root: request.__setitem__("selected_second_lookup_result_artifact", str(root / "missing-second.json")), None, None, None),
            (
                "second lookup result artifact JSON array",
                lambda request, root: (_write_json(root / "second-array.json", []), request.__setitem__("selected_second_lookup_result_artifact", str(root / "second-array.json"))),
                None,
                None,
                None,
            ),
            ("second lookup result artifact not recorded", None, None, lambda second: second.__setitem__("outcome", "NOT_RECORDED"), None),
            ("second lookup result artifact failed checks present", None, None, lambda second: second["local_relevance_medium_read_only_second_orientation_lookup_result_summary"].__setitem__("failed_check_count", 1), None),
            ("second lookup result artifact version not 0.1.0", None, None, second_version_bad, None),
            ("read-only orientation index artifact path missing", set_request("selected_read_only_orientation_index_artifact", ""), None, None, None),
            ("supported lookup keys not exact", None, None, None, lambda index: index_object(index)["lookup_table"].__setitem__("third_orientation_locator", {"lookup_key": "third_orientation_locator"})),
            ("covered lookup keys not exact", set_flag("covered_lookup_keys_not_exact"), None, None, None),
            ("supported lookup key count not two", None, None, None, lambda index: index_object(index).__setitem__("lookup_key_count", 3)),
            ("covered lookup key count not two", set_flag("covered_lookup_key_count_not_two"), None, None, None),
            ("lookup table key count not two", set_flag("lookup_table_key_count_not_two"), None, None, None),
            ("lookup table target count not two", None, None, None, lambda index: index_object(index).__setitem__("lookup_target_count", 3)),
            ("first declared lookup key not first_orientation_locator", None, lambda first: first_object(first).__setitem__("declared_lookup_key", "wrong_locator"), None, None),
            ("second declared lookup key not second_orientation_locator", None, None, lambda second: second_object(second).__setitem__("declared_lookup_key", "wrong_locator"), None),
            ("first selected received signal id not bounded_relevance_signal_001", None, lambda first: first_object(first).__setitem__("selected_received_signal_id", "bounded_relevance_signal_999"), None, None),
            ("second selected received signal id not bounded_relevance_signal_002", None, None, lambda second: second_object(second).__setitem__("selected_received_signal_id", "bounded_relevance_signal_999"), None),
            ("first and second selected received signal ids not distinct", set_flag("first_and_second_selected_received_signal_ids_not_distinct"), None, None, None),
            ("first selected locator entry artifact missing", None, lambda first: first_object(first).pop("selected_locator_entry_artifact", None), None, None),
            ("second selected locator entry artifact missing", None, None, lambda second: second_object(second).pop("selected_locator_entry_artifact", None), None),
            ("first selected orientation view artifact missing", None, lambda first: first_object(first).pop("selected_orientation_view_artifact", None), None, None),
            ("second selected orientation view artifact missing", None, None, lambda second: second_object(second).pop("selected_orientation_view_artifact", None), None),
            ("lookup order not deterministic", None, None, None, lambda index: index_object(index).__setitem__("lookup_order", ["second_orientation_locator", "first_orientation_locator"])),
            ("accepted new entries count not zero", None, None, None, lambda index: index_object(index).__setitem__("accepted_new_entries_count", 1)),
            ("deterministic local lookup not preserved", None, None, None, lambda index: index_object(index).__setitem__("deterministic_local_lookup_enabled", False)),
            ("lookup-pair coverage type missing", pop_request("lookup_pair_coverage_type"), None, None, None),
            ("lookup-pair coverage type unsupported", set_request("lookup_pair_coverage_type", "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT"), None, None, None),
            ("lookup-pair coverage scope missing", pop_request("lookup_pair_coverage_scope"), None, None, None),
            ("lookup-pair coverage scope unsupported", set_request("lookup_pair_coverage_scope", "ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY"), None, None, None),
            ("lookup-pair coverage not recorded", set_flag("lookup_pair_coverage_not_recorded"), None, None, None),
            ("reusable lookup permission created", set_flag("reusable_lookup_permission_created"), None, None, None),
            ("general lookup permission created", set_flag("general_lookup_permission_created"), None, None, None),
            ("new lookup result created", set_flag("new_lookup_result_created"), None, None, None),
            ("new lookup entry created", set_flag("new_lookup_entry_created"), None, None, None),
            ("new signal accepted", set_flag("new_signal_accepted"), None, None, None),
            ("new entry accepted", set_flag("new_entry_accepted"), None, None, None),
            ("new relevance object created", set_flag("new_relevance_object_created"), None, None, None),
            ("new index entry created", set_flag("new_index_entry_created"), None, None, None),
            ("filesystem discovery performed", set_flag("filesystem_discovery_performed"), None, None, None),
            ("registry created", set_flag("registry_created"), None, None, None),
            ("search surface created", set_flag("search_surface_created"), None, None, None),
            ("query surface created", set_flag("query_surface_created"), None, None, None),
            ("ranking surface created", set_flag("ranking_surface_created"), None, None, None),
            ("scoring surface created", set_flag("scoring_surface_created"), None, None, None),
            ("priority surface created", set_flag("priority_surface_created"), None, None, None),
            ("validity judgment created", set_flag("validity_judgment_created"), None, None, None),
            ("truth judgment created", set_flag("truth_judgment_created"), None, None, None),
            ("authority judgment created", set_flag("authority_judgment_created"), None, None, None),
            ("currentness judgment created", set_flag("currentness_judgment_created"), None, None, None),
            ("repeated reception permission created", set_flag("repeated_reception_permission_created"), None, None, None),
            ("arbitrary reception created", set_flag("arbitrary_reception_created"), None, None, None),
            ("feed created", set_flag("feed_created"), None, None, None),
            ("source transfer occurred", set_flag("source_transfer_occurred"), None, None, None),
            ("source receipt occurred", set_flag("source_receipt_occurred"), None, None, None),
            ("source created", set_flag("source_created"), None, None, None),
            ("authority created", set_flag("authority_created"), None, None, None),
            ("currentness created", set_flag("currentness_created"), None, None, None),
            ("truth created", set_flag("truth_created"), None, None, None),
            ("action created", set_flag("action_created"), None, None, None),
            ("synchronization created", set_flag("synchronization_created"), None, None, None),
            ("participation authorized", set_flag("participation_authorized"), None, None, None),
            ("participant role created", set_flag("participant_role_created"), None, None, None),
            ("runtime permission created", set_flag("runtime_permission_created"), None, None, None),
            ("public API created", set_flag("public_api_created"), None, None, None),
            ("participant-facing interface created", set_flag("participant_facing_interface_created"), None, None, None),
            ("distributed network behavior created", set_flag("distributed_network_behavior_created"), None, None, None),
            ("deployment created", set_flag("deployment_created"), None, None, None),
            ("public release created", set_flag("public_release_created"), None, None, None),
            ("operation permission created", set_flag("operation_permission_created"), None, None, None),
            ("broader reusable permission created", set_flag("broader_reusable_permission_created"), None, None, None),
            ("follow-on work authorized", set_flag("follow_on_work_authorized"), None, None, None),
            ("artifact existence treated as lookup-pair coverage authority", set_flag("artifact_existence_treated_as_lookup_pair_coverage_authority"), None, None, None),
            ("latest file posture treated as lookup-pair coverage authority", set_flag("latest_file_posture_treated_as_lookup_pair_coverage_authority"), None, None, None),
            ("repo-local availability treated as lookup-pair coverage authority", set_flag("repo_local_availability_treated_as_lookup_pair_coverage_authority"), None, None, None),
            ("hidden repo state used as lookup-pair coverage content", set_flag("hidden_repo_state_used_as_lookup_pair_coverage_content"), None, None, None),
            ("hidden repo state used as lookup-pair coverage authority", set_flag("hidden_repo_state_used_as_lookup_pair_coverage_authority"), None, None, None),
            ("predecessor failure repaired", set_flag("predecessor_failure_repaired"), None, None, None),
            ("predecessor failure hidden", set_flag("predecessor_failure_hidden"), None, None, None),
            ("predecessor failure claimed passed", set_flag("predecessor_failure_claimed_passed"), None, None, None),
            ("consumed request reopened", set_flag("consumed_request_reopened"), None, None, None),
            ("authorization token reused", set_flag("authorization_token_reused"), None, None, None),
            ("required non-claim missing", lambda request, _root: request["declared_non_claims"].pop("feed_created", None), None, None, None),
            ("required non-claim flipped", lambda request, _root: request["declared_non_claims"].__setitem__("feed_created", True), None, None, None),
            ("read-only orientation index artifact not recorded", None, None, None, lambda index: index.__setitem__("outcome", "NOT_RECORDED")),
            ("read-only orientation index artifact failed checks present", None, None, None, lambda index: index["local_relevance_medium_read_only_orientation_index_system_summary"].__setitem__("failed_check_count", 1)),
            ("read-only orientation index artifact version not 0.1.0", None, None, None, index_version_bad),
            (
                "read-only orientation index artifact JSON array",
                lambda request, root: (_write_json(root / "index-array.json", []), request.__setitem__("selected_read_only_orientation_index_artifact", str(root / "index-array.json"))),
                None,
                None,
                None,
            ),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, direct in direct_cases:
                with self.subTest(name=name):
                    self._assert_blocked_common(direct(root))
            for name, request_mutator, first_mutator, second_mutator, index_mutator in cases:
                with self.subTest(name=name):
                    result = self._resolve_with(root, request_mutator, first_mutator, second_mutator, index_mutator)
                    self._assert_blocked_common(result)

    def test_missing_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, second_path, index_path, _, _, _ = _write_synthetic_basis(Path(tmp))
            clean_request = _build_valid_request(first_path, second_path, index_path)
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
                    result = resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(request)
                    self.assertIn(result["outcome"], {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS})
                    self._assert_public_codes(result)
                    self._assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, second_path, index_path, _, _, _ = _write_synthetic_basis(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(
                _build_valid_request(first_path, second_path, index_path)
            )

        coverage = self._coverage(result)
        self.assertEqual(coverage["lookup_pair_coverage_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE")
        self.assertEqual(coverage["lookup_pair_coverage_scope"], "BOTH_SUPPORTED_ORIENTATION_LOOKUP_KEYS_COVERED_ONLY")
        self.assertEqual(coverage["supported_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(coverage["covered_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(coverage["first_selected_received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(coverage["second_selected_received_signal_id"], "bounded_relevance_signal_002")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_BLOCKED",
            },
        )
        serialized = json.dumps(result, sort_keys=True)
        self.assertNotIn("[REDACTED_RAW_CONTENT]", serialized)
        for official in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE",
            "BOTH_SUPPORTED_ORIENTATION_LOOKUP_KEYS_COVERED_ONLY",
            "first_orientation_locator",
            "second_orientation_locator",
            "bounded_relevance_signal_001",
            "bounded_relevance_signal_002",
        ):
            self.assertIn(official, serialized)

    def test_raw_hidden_hostile_content_containment_and_input_not_mutated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def mutate_first(first: dict[str, Any]) -> None:
                first["raw_first_lookup_result_body"] = HOSTILE_SENTINELS[2]
                first["local_relevance_medium_read_only_orientation_lookup_result"]["raw_full_body"] = (
                    HOSTILE_SENTINELS[6]
                )

            def mutate_second(second: dict[str, Any]) -> None:
                second["raw_second_lookup_result_body"] = HOSTILE_SENTINELS[3]
                second["local_relevance_medium_read_only_second_orientation_lookup_result"][
                    "second_lookup_result_body"
                ] = HOSTILE_SENTINELS[1]

            def mutate_index(index: dict[str, Any]) -> None:
                index["raw_orientation_index_system_body"] = HOSTILE_SENTINELS[4]
                index["local_relevance_medium_read_only_orientation_index"]["raw_orientation_index_body"] = (
                    HOSTILE_SENTINELS[5]
                )

            first_path, second_path, index_path, _, _, _ = _write_synthetic_basis(
                root,
                mutate_first,
                mutate_second,
                mutate_index,
            )
            request = _build_valid_request(first_path, second_path, index_path)
            request["raw_lookup_pair_coverage_body"] = HOSTILE_SENTINELS[0]
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            request["nested_raw"] = {"lookup_pair_coverage_body": HOSTILE_SENTINELS[1]}
            request_before = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(request)

        self.assertEqual(request, request_before)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self._assert_public_codes(result)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        for official in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE",
            "BOTH_SUPPORTED_ORIENTATION_LOOKUP_KEYS_COVERED_ONLY",
            "first_orientation_locator",
            "second_orientation_locator",
            "bounded_relevance_signal_001",
            "bounded_relevance_signal_002",
        ):
            self.assertIn(official, serialized)
        self._assert_no_creation_posture_false(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first_path, second_path, index_path, _, _, _ = _write_synthetic_basis(root)
            request = _build_valid_request(first_path, second_path, index_path)
            request_path = root / "request.json"
            _write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_from_path(
                request_path
            )
            summary = resolver.build_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            array_path = root / "array-request.json"
            _write_json(array_path, [])
            for path in (malformed_path, array_path, root / "missing-request.json"):
                with self.subTest(path=path.name):
                    malformed_result = (
                        resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_from_path(path)
                    )
                    self._assert_blocked_common(malformed_result)

            patched_output_root = root / EXPECTED_OUTPUT_ROOT.name
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_output_root):
                written = resolver.write_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_result(result)
                written_again = resolver.write_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_result(
                    result
                )

            self.assertTrue(written.parent.exists())
            self.assertTrue(written.exists())
            self.assertTrue(written_again.exists())
            self.assertNotEqual(written, written_again)
            with written.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn("local_relevance_medium_read_only_lookup_pair_coverage_v0_min", str(written))
            for forbidden in FORBIDDEN_OUTPUT_ROOTS:
                forbidden_abs = REPO_ROOT / forbidden
                self.assertFalse(_is_same_or_under(written.resolve(), forbidden_abs.resolve()))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first_artifact = _first_lookup_artifact()
            second_artifact = _second_lookup_artifact()
            index_artifact = _orientation_index_artifact()
            first_before = copy.deepcopy(first_artifact)
            second_before = copy.deepcopy(second_artifact)
            index_before = copy.deepcopy(index_artifact)
            first_path = root / "first.json"
            second_path = root / "second.json"
            index_path = root / "index.json"
            _write_json(first_path, first_artifact)
            _write_json(second_path, second_artifact)
            _write_json(index_path, index_artifact)

            request = _build_valid_request(first_path, second_path, index_path)
            request["posture"] = {
                "raw_full_body": "RAW_LOOKUP_PAIR_COVERAGE_BODY_MUST_NOT_RETURN",
                "nested": {"hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN"},
            }
            request_before = copy.deepcopy(request)
            non_claims_before = copy.deepcopy(request["declared_non_claims"])
            first_path_before = request["selected_first_lookup_result_artifact"]
            second_path_before = request["selected_second_lookup_result_artifact"]
            index_path_before = request["selected_read_only_orientation_index_artifact"]
            type_before = request["lookup_pair_coverage_type"]
            scope_before = request["lookup_pair_coverage_scope"]

            resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(request)

        self.assertEqual(request, request_before)
        self.assertEqual(request["declared_non_claims"], non_claims_before)
        self.assertEqual(request["selected_first_lookup_result_artifact"], first_path_before)
        self.assertEqual(request["selected_second_lookup_result_artifact"], second_path_before)
        self.assertEqual(request["selected_read_only_orientation_index_artifact"], index_path_before)
        self.assertEqual(request["lookup_pair_coverage_type"], type_before)
        self.assertEqual(request["lookup_pair_coverage_scope"], scope_before)
        self.assertEqual(first_artifact, first_before)
        self.assertEqual(second_artifact, second_before)
        self.assertEqual(index_artifact, index_before)
        self.assertEqual(request["posture"], request_before["posture"])

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, second_path, index_path, _, _, _ = _write_synthetic_basis(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(
                _build_valid_request(first_path, second_path, index_path)
            )
            summary = resolver.build_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_summary(result)

        statement = self._statement(result)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["predecessor_failure_not_repaired"], True)
        self.assertIs(statement["predecessor_failure_not_hidden"], True)
        self.assertIs(statement["predecessor_failure_not_claimed_passed"], True)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["key_non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(summary["key_non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(summary["key_non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(summary["key_non_claims"]["consumed_request_reopened"], False)
        self.assertIs(summary["key_non_claims"]["authorization_token_reused"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
