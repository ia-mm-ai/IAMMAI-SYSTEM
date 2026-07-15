"""Tests for the local relevance medium read-only reusable lookup permission boundary.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY object.
It verifies that the resolver reads one clean lookup-pair coverage artifact as
coverage basis, records that future reusable read-only lookup permission may be
considered later, and preserves the upstream lookup-pair coverage as coverage
only.

The suite does not grant reusable lookup permission, create reusable lookup
permission, create general lookup permission, create implicit permission,
create repeatability, create a new lookup result, create a new lookup entry,
accept new signal or entry, create new relevance object or index entry,
perform filesystem discovery, create registry, search, query surface, ranking,
scoring, priority, validity judgment, truth judgment, authority judgment,
currentness judgment, repeated reception permission, arbitrary reception, feed,
source transfer, source receipt, source, authority, currentness, truth, action,
synchronization, participation authorization, participant role, runtime
permission, public API, participant-facing interface, distributed behavior,
operation permission, or follow-on work.
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

import resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min as resolver  # noqa: E402


DEFAULT_LOOKUP_PAIR_COVERAGE_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_pair_coverage_v0_min/"
    "local_relevance_medium_read_only_lookup_pair_coverage_reference_review_001__"
    "local_relevance_medium_read_only_lookup_pair_coverage_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
    "declared_local_relevance_medium_read_only_reusable_lookup_permission_boundary_question",
    "selected_lookup_pair_coverage_artifact_basis",
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary",
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_checks",
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_statement",
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
)

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
)

BOUNDARY_FALSE_FIELDS = (
    "reusable_lookup_permission_granted",
    "reusable_lookup_permission_created",
    "general_lookup_permission_created",
    "implicit_permission_created",
    "repeatability_created",
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
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_recorded",
    "basis_lookup_pair_coverage_artifact_preserved",
    "supported_lookup_keys_preserved",
    "covered_lookup_keys_preserved",
    "supported_lookup_key_count_is_two",
    "covered_lookup_key_count_is_two",
    "both_supported_lookup_keys_covered",
    "lookup_pair_coverage_recorded",
    "coverage_only_preserved",
    "future_reusable_read_only_lookup_permission_may_be_considered",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PAIR_COVERAGE_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _lookup_pair_coverage_artifact() -> dict[str, Any]:
    coverage = {
        "lookup_pair_coverage_id": "local_relevance_medium_read_only_lookup_pair_coverage_001",
        "lookup_pair_coverage_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE",
        "lookup_pair_coverage_version": "0.1.0",
        "lookup_pair_coverage_scope": "BOTH_SUPPORTED_ORIENTATION_LOOKUP_KEYS_COVERED_ONLY",
        "supported_lookup_keys": ["first_orientation_locator", "second_orientation_locator"],
        "covered_lookup_keys": ["first_orientation_locator", "second_orientation_locator"],
        "supported_lookup_key_count": 2,
        "covered_lookup_key_count": 2,
        "lookup_table_key_count": 2,
        "lookup_table_target_count": 2,
        "both_supported_lookup_keys_covered": True,
        "lookup_pair_coverage_recorded": True,
        "coverage_only_preserved": True,
        "accepted_new_entries_count": 0,
        "deterministic_local_lookup_preserved": True,
        "reusable_lookup_permission_created": False,
        "general_lookup_permission_created": False,
        "new_lookup_result_created": False,
        "new_lookup_entry_created": False,
        "new_signal_accepted": False,
        "new_entry_accepted": False,
        "new_relevance_object_created": False,
        "new_index_entry_created": False,
        "filesystem_discovery_performed": False,
        "registry_created": False,
        "search_surface_created": False,
        "query_surface_created": False,
        "ranking_surface_created": False,
    }
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_RECORDED",
        "result_version": "0.1.0",
        "failed_check_count": 0,
        "local_relevance_medium_read_only_lookup_pair_coverage_metadata": {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "resolver_module": "resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min",
        },
        "local_relevance_medium_read_only_lookup_pair_coverage_summary": {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 226,
        },
        "local_relevance_medium_read_only_lookup_pair_coverage": coverage,
        "local_relevance_medium_read_only_lookup_pair_coverage_checks": [
            {
                "check_name": "synthetic lookup-pair coverage artifact clean",
                "passed": True,
                "expected_posture": "recorded lookup-pair coverage",
                "actual_posture": "recorded lookup-pair coverage",
            }
        ],
    }


def _write_synthetic_lookup_pair_coverage(
    root: Path,
    mutator: Callable[[dict[str, Any]], None] | None = None,
) -> tuple[Path, dict[str, Any]]:
    artifact = _lookup_pair_coverage_artifact()
    if mutator is not None:
        mutator(artifact)
    path = root / "lookup_pair_coverage.json"
    _write_json(path, artifact)
    return path, artifact


def _build_valid_request(path: Path, **overrides: Any) -> dict[str, Any]:
    request = resolver.build_declared_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_request(
        selected_lookup_pair_coverage_artifact=path,
    )
    request.update(copy.deepcopy(overrides))
    return request


def _is_same_or_under(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


class LocalRelevanceMediumReadOnlyReusableLookupPermissionBoundaryTests(unittest.TestCase):
    def assert_not_blocked(self, result):
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def _boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        value = result.get("local_relevance_medium_read_only_reusable_lookup_permission_boundary")
        self.assertIsInstance(value, dict)
        return value

    def _statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        value = result.get("local_relevance_medium_read_only_reusable_lookup_permission_boundary_statement")
        self.assertIsInstance(value, dict)
        return value

    def _checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        value = result.get("local_relevance_medium_read_only_reusable_lookup_permission_boundary_checks")
        self.assertIsInstance(value, list)
        return value

    def _summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        value = result.get("local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary")
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

    def _assert_no_permission_or_broader_creation(self, result: Mapping[str, Any]) -> None:
        self._assert_non_claims_canonical_false(result)
        non_claims = result["non_claims"]
        for key in (
            "reusable_lookup_permission_granted",
            "reusable_lookup_permission_created",
            "general_lookup_permission_created",
            "implicit_permission_created",
            "repeatability_created",
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
        boundary = result.get("local_relevance_medium_read_only_reusable_lookup_permission_boundary")
        if isinstance(boundary, dict):
            for key in BOUNDARY_FALSE_FIELDS:
                if key in boundary:
                    self.assertIs(boundary[key], False)

    def _assert_boundary_separate_from_wrapper(self, result: Mapping[str, Any]) -> None:
        boundary = self._boundary(result)
        for key in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(key, boundary)

    def _assert_boundary_preserves_coverage_only_posture(
        self,
        boundary: Mapping[str, Any],
        artifact_path: Path,
    ) -> None:
        self.assertEqual(boundary["boundary_id"], "local_relevance_medium_read_only_reusable_lookup_permission_boundary_001")
        self.assertEqual(boundary["boundary_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY")
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(boundary["boundary_scope"], "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_CONSIDERATION_ONLY")
        self.assertEqual(boundary["basis_lookup_pair_coverage_artifact"], str(artifact_path))
        self.assertEqual(
            boundary["basis_lookup_pair_coverage_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_RECORDED",
        )
        self.assertEqual(boundary["basis_lookup_pair_coverage_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_lookup_pair_coverage_failed_check_count"], 0)
        self.assertEqual(boundary["supported_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(boundary["covered_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(boundary["supported_lookup_key_count"], 2)
        self.assertEqual(boundary["covered_lookup_key_count"], 2)
        self.assertIs(boundary["both_supported_lookup_keys_covered"], True)
        self.assertIs(boundary["lookup_pair_coverage_recorded"], True)
        self.assertIs(boundary["coverage_only_preserved"], True)
        self.assertIs(boundary["future_reusable_read_only_lookup_permission_may_be_considered"], True)
        for key in BOUNDARY_FALSE_FIELDS:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False)

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
        self._assert_no_permission_or_broader_creation(result)

    def test_public_api_constants_and_output_root(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_request",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_BOUNDARY_TYPE_VALUES",
            "SUPPORTED_BOUNDARY_SCOPE_VALUES",
            "SUPPORTED_LOOKUP_KEYS",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min",
        )
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY",
            resolver.SUPPORTED_BOUNDARY_TYPE_VALUES,
        )
        self.assertIn(
            "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_CONSIDERATION_ONLY",
            resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SUPPORTED_LOOKUP_KEYS, ["first_orientation_locator", "second_orientation_locator"])

        output_root = Path(resolver.OUTPUT_ROOT)
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            self.assertFalse(
                output_root == forbidden or _is_same_or_under(output_root, forbidden),
                f"{output_root} unexpectedly writes under {forbidden}",
            )

    def test_records_from_synthetic_lookup_pair_coverage_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _ = _write_synthetic_lookup_pair_coverage(Path(tmp))
            request = _build_valid_request(artifact_path)
            result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min(request)
            summary = resolver.build_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["boundary_id"], "local_relevance_medium_read_only_reusable_lookup_permission_boundary_001")

        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        boundary = self._boundary(result)
        self._assert_boundary_preserves_coverage_only_posture(boundary, artifact_path)
        self._assert_boundary_separate_from_wrapper(result)
        self._assert_success_statement(result)
        self._assert_no_permission_or_broader_creation(result)

    def test_records_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_LOOKUP_PAIR_COVERAGE_ARTIFACT.exists():
            self.skipTest("default lookup-pair coverage artifact is not present")
        request = resolver.build_declared_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min(request)
        summary = resolver.build_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_summary(result)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        boundary = self._boundary(result)
        self.assertEqual(boundary["boundary_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY")
        self.assertEqual(boundary["boundary_scope"], "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_CONSIDERATION_ONLY")
        self.assertEqual(boundary["supported_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(boundary["covered_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(boundary["supported_lookup_key_count"], 2)
        self.assertEqual(boundary["covered_lookup_key_count"], 2)
        self.assertIs(boundary["both_supported_lookup_keys_covered"], True)
        self.assertIs(boundary["lookup_pair_coverage_recorded"], True)
        self.assertIs(boundary["coverage_only_preserved"], True)
        self.assertIs(boundary["future_reusable_read_only_lookup_permission_may_be_considered"], True)
        self._assert_no_permission_or_broader_creation(result)

    def test_canonicalizes_flipped_declared_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _ = _write_synthetic_lookup_pair_coverage(Path(tmp))
            clean_request = _build_valid_request(artifact_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min(request)
                    self._assert_blocked_common(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertNotEqual(result["non_claims"][key], True)

    def test_representative_blocking_behavior(self) -> None:
        shortcut_fields = (
            "both_supported_lookup_keys_covered_not_true",
            "future_reusable_read_only_lookup_permission_may_not_be_considered",
            "reusable_lookup_permission_granted",
            "reusable_lookup_permission_created",
            "general_lookup_permission_created",
            "implicit_permission_created",
            "repeatability_created",
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
            "deployment_created",
            "public_release_created",
            "operation_permission_created",
            "broader_reusable_permission_created",
            "follow_on_work_authorized",
            "artifact_existence_treated_as_reusable_lookup_boundary_authority",
            "latest_file_posture_treated_as_reusable_lookup_boundary_authority",
            "repo_local_availability_treated_as_reusable_lookup_boundary_authority",
            "hidden_repo_state_used_as_reusable_lookup_boundary_content",
            "hidden_repo_state_used_as_reusable_lookup_boundary_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        )

        def result_for_case(
            root: Path,
            request_mutator: Callable[[dict[str, Any], Path], None] | None = None,
            artifact_mutator: Callable[[dict[str, Any]], None] | None = None,
        ) -> dict[str, Any]:
            artifact_path, _ = _write_synthetic_lookup_pair_coverage(root, artifact_mutator)
            request = _build_valid_request(artifact_path)
            if request_mutator is not None:
                request_mutator(request, root)
            return resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min(request)

        cases: list[tuple[str, Callable[[Path], dict[str, Any]]]] = [
            (
                "explicit block intent",
                lambda root: result_for_case(
                    root,
                    lambda request, _: request.update(
                        {
                            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_intent": (
                                "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY"
                            )
                        }
                    ),
                ),
            ),
            ("missing request", lambda root: resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min({})),
            ("non-mapping request", lambda root: resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min(["not", "a", "mapping"])),
            (
                "unsupported intent",
                lambda root: result_for_case(
                    root,
                    lambda request, _: request.update(
                        {
                            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_intent": (
                                "UNSUPPORTED_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_INTENT"
                            )
                        }
                    ),
                ),
            ),
            (
                "lookup-pair coverage artifact path missing",
                lambda root: result_for_case(
                    root,
                    lambda request, _: request.update({"selected_lookup_pair_coverage_artifact": ""}),
                ),
            ),
            (
                "lookup-pair coverage artifact unreadable",
                lambda root: result_for_case(
                    root,
                    lambda request, case_root: request.update(
                        {"selected_lookup_pair_coverage_artifact": str(case_root / "missing.json")}
                    ),
                ),
            ),
            (
                "lookup-pair coverage artifact JSON array instead of object",
                lambda root: result_for_case(
                    root,
                    lambda request, case_root: (
                        _write_json(case_root / "array.json", []),
                        request.update({"selected_lookup_pair_coverage_artifact": str(case_root / "array.json")}),
                    ),
                ),
            ),
            (
                "lookup-pair coverage artifact not recorded",
                lambda root: result_for_case(root, artifact_mutator=lambda artifact: artifact.update({"outcome": "NOT_RECORDED"})),
            ),
            (
                "lookup-pair coverage artifact failed checks present",
                lambda root: result_for_case(root, artifact_mutator=lambda artifact: artifact.update({"failed_check_count": 1})),
            ),
            (
                "lookup-pair coverage artifact version not 0.1.0",
                lambda root: result_for_case(root, artifact_mutator=lambda artifact: artifact.update({"result_version": "9.9.9"})),
            ),
            (
                "supported lookup keys not exact",
                lambda root: result_for_case(
                    root,
                    artifact_mutator=lambda artifact: artifact["local_relevance_medium_read_only_lookup_pair_coverage"].update(
                        {"supported_lookup_keys": ["first_orientation_locator"]}
                    ),
                ),
            ),
            (
                "covered lookup keys not exact",
                lambda root: result_for_case(
                    root,
                    artifact_mutator=lambda artifact: artifact["local_relevance_medium_read_only_lookup_pair_coverage"].update(
                        {"covered_lookup_keys": ["second_orientation_locator"]}
                    ),
                ),
            ),
            (
                "supported lookup key count not two",
                lambda root: result_for_case(
                    root,
                    artifact_mutator=lambda artifact: artifact["local_relevance_medium_read_only_lookup_pair_coverage"].update(
                        {"supported_lookup_key_count": 1}
                    ),
                ),
            ),
            (
                "covered lookup key count not two",
                lambda root: result_for_case(
                    root,
                    artifact_mutator=lambda artifact: artifact["local_relevance_medium_read_only_lookup_pair_coverage"].update(
                        {"covered_lookup_key_count": 3}
                    ),
                ),
            ),
            (
                "lookup-pair coverage not recorded",
                lambda root: result_for_case(
                    root,
                    artifact_mutator=lambda artifact: artifact["local_relevance_medium_read_only_lookup_pair_coverage"].update(
                        {"lookup_pair_coverage_recorded": False}
                    ),
                ),
            ),
            (
                "coverage-only posture not preserved",
                lambda root: result_for_case(
                    root,
                    artifact_mutator=lambda artifact: artifact["local_relevance_medium_read_only_lookup_pair_coverage"].update(
                        {"reusable_lookup_permission_created": True}
                    ),
                ),
            ),
            (
                "boundary type missing",
                lambda root: result_for_case(root, lambda request, _: request.pop("boundary_type")),
            ),
            (
                "boundary type not exact",
                lambda root: result_for_case(root, lambda request, _: request.update({"boundary_type": "REGISTRY"})),
            ),
            (
                "boundary scope missing",
                lambda root: result_for_case(root, lambda request, _: request.pop("boundary_scope")),
            ),
            (
                "boundary scope not exact",
                lambda root: result_for_case(root, lambda request, _: request.update({"boundary_scope": "GENERAL_LOOKUP_PERMISSION"})),
            ),
            (
                "required non-claim missing or flipped",
                lambda root: result_for_case(
                    root,
                    lambda request, _: request["declared_non_claims"].pop("reusable_lookup_permission_created"),
                ),
            ),
        ]
        for field_name in shortcut_fields:
            cases.append(
                (
                    field_name.replace("_", " "),
                    lambda root, shortcut=field_name: result_for_case(
                        root,
                        lambda request, _: request.update({shortcut: True}),
                    ),
                )
            )

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            for index, (label, case_builder) in enumerate(cases):
                with self.subTest(case=label):
                    case_root = tmp_path / f"case_{index:03d}"
                    case_root.mkdir(parents=True, exist_ok=True)
                    result = case_builder(case_root)
                    self._assert_blocked_common(result)

    def test_missing_or_incomplete_declared_non_claims(self) -> None:
        def variants(clean_request: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
            missing = copy.deepcopy(clean_request)
            missing.pop("declared_non_claims")
            empty = copy.deepcopy(clean_request)
            empty["declared_non_claims"] = {}
            removed = copy.deepcopy(clean_request)
            removed["declared_non_claims"].pop("reusable_lookup_permission_created")
            string_value = copy.deepcopy(clean_request)
            string_value["declared_non_claims"]["reusable_lookup_permission_created"] = "false"
            none_value = copy.deepcopy(clean_request)
            none_value["declared_non_claims"]["reusable_lookup_permission_created"] = None
            return [
                ("declared_non_claims removed", missing),
                ("declared_non_claims empty", empty),
                ("one required non-claim removed", removed),
                ("one required non-claim string", string_value),
                ("one required non-claim none", none_value),
            ]

        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _ = _write_synthetic_lookup_pair_coverage(Path(tmp))
            clean_request = _build_valid_request(artifact_path)
            for label, request in variants(clean_request):
                with self.subTest(case=label):
                    result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min(request)
                    self.assertIn(result["outcome"], (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))
                    self._assert_public_codes(result)
                    self._assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _ = _write_synthetic_lookup_pair_coverage(Path(tmp))
            request = _build_valid_request(artifact_path)
            result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min(request)

        boundary = self._boundary(result)
        self.assertEqual(boundary["boundary_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY")
        self.assertEqual(boundary["boundary_scope"], "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_CONSIDERATION_ONLY")
        self.assertEqual(boundary["supported_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(boundary["covered_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_BLOCKED",
            },
        )
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY", serialized)
        self.assertIn("REUSABLE_READ_ONLY_LOOKUP_PERMISSION_CONSIDERATION_ONLY", serialized)
        self.assertIn("first_orientation_locator", serialized)
        self.assertIn("second_orientation_locator", serialized)
        self.assertNotEqual(boundary["boundary_type"], "[REDACTED_RAW_CONTENT]")
        self.assertNotEqual(boundary["boundary_scope"], "[REDACTED_RAW_CONTENT]")

    def test_raw_hidden_hostile_content_containment(self) -> None:
        def hostile_artifact(artifact: dict[str, Any]) -> None:
            artifact["raw_lookup_pair_coverage_body"] = HOSTILE_SENTINELS[2]
            artifact["hidden_repo_state"] = {"payload": HOSTILE_SENTINELS[-1]}
            artifact["local_relevance_medium_read_only_lookup_pair_coverage"]["artifact_body"] = (
                HOSTILE_SENTINELS[3]
            )

        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _ = _write_synthetic_lookup_pair_coverage(Path(tmp), hostile_artifact)
            request = _build_valid_request(
                artifact_path,
                raw_reusable_lookup_permission_boundary_body=HOSTILE_SENTINELS[0],
                hidden_repo_state={"payload": HOSTILE_SENTINELS[-1]},
            )
            request_before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min(request)

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY", serialized)
        self.assertIn("first_orientation_locator", serialized)
        self._assert_no_permission_or_broader_creation(result)
        self.assertEqual(request, request_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact_path, _ = _write_synthetic_lookup_pair_coverage(tmp_path)
            request = _build_valid_request(artifact_path)
            request_path = tmp_path / "request.json"
            _write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_from_path(
                request_path
            )
            summary = resolver.build_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_summary(result)

            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_from_path(
                malformed_path
            )
            self._assert_blocked_common(malformed)

            array_path = tmp_path / "array_request.json"
            _write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_from_path(
                array_path
            )
            self._assert_blocked_common(array_result)

            missing_result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_from_path(
                tmp_path / "missing_request.json"
            )
            self._assert_blocked_common(missing_result)

            output_root = tmp_path / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_result(result)
                second_path = resolver.write_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_result(result)

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(second_path.parent.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(second_path.name.endswith("_001.json"))
            with first_path.open("r", encoding="utf-8") as handle:
                self.assertIsInstance(json.load(handle), dict)
            with second_path.open("r", encoding="utf-8") as handle:
                self.assertIsInstance(json.load(handle), dict)

            self.assertIn(
                "local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min",
                str(first_path),
            )
            relative_parent = first_path.parent.relative_to(tmp_path)
            for forbidden in FORBIDDEN_OUTPUT_ROOTS:
                self.assertFalse(
                    relative_parent == forbidden or _is_same_or_under(relative_parent, forbidden),
                    f"{relative_parent} unexpectedly writes under {forbidden}",
                )

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact = _lookup_pair_coverage_artifact()
            artifact_before = copy.deepcopy(artifact)
            artifact_path = Path(tmp) / "lookup_pair_coverage.json"
            _write_json(artifact_path, artifact)
            request = _build_valid_request(
                artifact_path,
                raw_full_body={"payload": HOSTILE_SENTINELS[3]},
            )
            request_before = copy.deepcopy(request)
            declared_non_claims_before = copy.deepcopy(request["declared_non_claims"])
            selected_path_before = request["selected_lookup_pair_coverage_artifact"]

            resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min(request)

            self.assertEqual(request, request_before)
            self.assertEqual(request["declared_non_claims"], declared_non_claims_before)
            self.assertEqual(request["selected_lookup_pair_coverage_artifact"], selected_path_before)
            self.assertEqual(artifact, artifact_before)
            self.assertEqual(request["boundary_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY")
            self.assertEqual(request["boundary_scope"], "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_CONSIDERATION_ONLY")

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _ = _write_synthetic_lookup_pair_coverage(Path(tmp))
            request = _build_valid_request(artifact_path)
            result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min(request)
            summary = resolver.build_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_summary(result)

        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["predecessor_failure_not_repaired"], True)
        self.assertIs(summary["predecessor_failure_not_hidden"], True)
        self.assertIs(summary["predecessor_failure_not_claimed_passed"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        non_claims = result["non_claims"]
        self.assertIs(non_claims["predecessor_failure_repaired"], False)
        self.assertIs(non_claims["predecessor_failure_hidden"], False)
        self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
