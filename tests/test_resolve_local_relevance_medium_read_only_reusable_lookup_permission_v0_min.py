"""Tests for the local relevance medium read-only reusable lookup permission.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION object. It verifies
that the resolver reads one clean reusable lookup permission boundary artifact
and one clean lookup-pair coverage artifact, then records one bounded reusable
read-only lookup permission over exactly first_orientation_locator and
second_orientation_locator.

The suite does not create general lookup permission, arbitrary lookup
permission, unsupported-key permission, query surface, registry, search,
ranking, scoring, priority, validity judgment, truth judgment, authority
judgment, currentness judgment, repeated reception permission, arbitrary
reception, feed, new lookup result, new lookup entry, new signal, new entry,
new relevance object, new index entry, filesystem discovery, source transfer,
source receipt, runtime permission, API, distributed behavior, operation
permission, or follow-on work.
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

import resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min as resolver  # noqa: E402


DEFAULT_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min/"
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_reference_review_001__"
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_result.json"
)
DEFAULT_LOOKUP_PAIR_COVERAGE_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_pair_coverage_v0_min/"
    "local_relevance_medium_read_only_lookup_pair_coverage_reference_review_001__"
    "local_relevance_medium_read_only_lookup_pair_coverage_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_reusable_lookup_permission_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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
    "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
    "declared_local_relevance_medium_read_only_reusable_lookup_permission_question",
    "selected_reusable_lookup_permission_boundary_artifact_basis",
    "selected_lookup_pair_coverage_artifact_basis",
    "local_relevance_medium_read_only_reusable_lookup_permission",
    "local_relevance_medium_read_only_reusable_lookup_permission_checks",
    "local_relevance_medium_read_only_reusable_lookup_permission_statement",
    "local_relevance_medium_read_only_reusable_lookup_permission_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_reusable_lookup_permission_summary",
)

FORBIDDEN_PERMISSION_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_reusable_lookup_permission_checks",
    "non_claims",
    "local_relevance_medium_read_only_reusable_lookup_permission_summary",
    "local_relevance_medium_read_only_reusable_lookup_permission_metadata",
)

PERMISSION_OBJECT_FALSE_FIELDS = (
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
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
    "local_relevance_medium_read_only_reusable_lookup_permission_recorded",
    "basis_reusable_lookup_permission_boundary_artifact_preserved",
    "basis_lookup_pair_coverage_artifact_preserved",
    "supported_lookup_keys_preserved",
    "covered_lookup_keys_preserved",
    "permitted_lookup_keys_preserved",
    "supported_lookup_key_count_is_two",
    "covered_lookup_key_count_is_two",
    "permitted_lookup_key_count_is_two",
    "both_supported_lookup_keys_covered",
    "lookup_pair_coverage_recorded",
    "coverage_only_preserved",
    "boundary_recorded",
    "future_reusable_read_only_lookup_permission_was_considered",
    "reusable_read_only_lookup_permission_created",
    "reusable_read_only_lookup_permission_scope_bounded",
    "repeated_read_only_deterministic_lookup_permitted",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_REUSABLE_LOOKUP_PERMISSION_BODY_MUST_NOT_RETURN",
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


def _boundary_artifact() -> dict[str, Any]:
    boundary = {
        "boundary_id": "local_relevance_medium_read_only_reusable_lookup_permission_boundary_001",
        "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY",
        "boundary_version": "0.1.0",
        "boundary_scope": "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_CONSIDERATION_ONLY",
        "supported_lookup_keys": ["first_orientation_locator", "second_orientation_locator"],
        "covered_lookup_keys": ["first_orientation_locator", "second_orientation_locator"],
        "supported_lookup_key_count": 2,
        "covered_lookup_key_count": 2,
        "both_supported_lookup_keys_covered": True,
        "lookup_pair_coverage_recorded": True,
        "coverage_only_preserved": True,
        "future_reusable_read_only_lookup_permission_may_be_considered": True,
    }
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_RECORDED",
        "result_version": "0.1.0",
        "failed_check_count": 0,
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata": {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "resolver_module": "resolve_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min",
        },
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 199,
        },
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary": boundary,
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_statement": {
            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_recorded": True,
            "future_reusable_read_only_lookup_permission_may_be_considered": True,
            "coverage_only_preserved": True,
            "result_level_non_claims_canonical_false": True,
        },
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_checks": [
            {
                "check_name": "synthetic reusable lookup permission boundary artifact clean",
                "passed": True,
                "expected_posture": "recorded reusable lookup permission boundary",
                "actual_posture": "recorded reusable lookup permission boundary",
            }
        ],
    }


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
        "both_supported_lookup_keys_covered": True,
        "lookup_pair_coverage_recorded": True,
        "coverage_only_preserved": True,
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
            "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_RECORDED",
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


def _write_synthetic_artifacts(
    root: Path,
    boundary_mutator: Callable[[dict[str, Any]], None] | None = None,
    coverage_mutator: Callable[[dict[str, Any]], None] | None = None,
) -> tuple[Path, Path, dict[str, Any], dict[str, Any]]:
    boundary = _boundary_artifact()
    coverage = _lookup_pair_coverage_artifact()
    if boundary_mutator is not None:
        boundary_mutator(boundary)
    if coverage_mutator is not None:
        coverage_mutator(coverage)
    boundary_path = root / "reusable_lookup_permission_boundary.json"
    coverage_path = root / "lookup_pair_coverage.json"
    _write_json(boundary_path, boundary)
    _write_json(coverage_path, coverage)
    return boundary_path, coverage_path, boundary, coverage


def _build_valid_request(boundary_path: Path, coverage_path: Path, **overrides: Any) -> dict[str, Any]:
    request = resolver.build_declared_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_request(
        selected_reusable_lookup_permission_boundary_artifact=boundary_path,
        selected_lookup_pair_coverage_artifact=coverage_path,
    )
    request.update(copy.deepcopy(overrides))
    return request


def _is_same_or_under(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


class LocalRelevanceMediumReadOnlyReusableLookupPermissionTests(unittest.TestCase):
    def assert_not_blocked(self, result):
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def permission(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        permission = result.get("local_relevance_medium_read_only_reusable_lookup_permission")
        self.assertIsInstance(permission, Mapping)
        return permission

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get("local_relevance_medium_read_only_reusable_lookup_permission_statement")
        self.assertIsInstance(statement, Mapping)
        return statement

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get("local_relevance_medium_read_only_reusable_lookup_permission_checks")
        self.assertIsInstance(checks, list)
        return checks

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        code = block.get("block_code") or block.get("code")
        return code if isinstance(code, str) else None

    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        code = self.block_code(result)
        if result.get("outcome") == resolver.OUTCOME_BLOCKED:
            self.assertIsNotNone(code)
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            check_code = check.get("block_code") or check.get("failure_code")
            if check_code is not None:
                self.assertIn(check_code, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIs(type(non_claims[key]), bool)

    def assert_permission_object_not_wrapper(self, permission: Mapping[str, Any]) -> None:
        for key in FORBIDDEN_PERMISSION_WRAPPER_FIELDS:
            self.assertNotIn(key, permission)

    def assert_no_overreach(self, result: Mapping[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        permission = self.permission(result)
        for key in PERMISSION_OBJECT_FALSE_FIELDS:
            if key in permission:
                self.assertIs(permission[key], False, key)
        for key in (
            "general_lookup_permission_created",
            "arbitrary_lookup_permission_created",
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
            self.assertIs(result["non_claims"][key], False, key)

    def assert_permission_bounded_to_two_keys(self, permission: Mapping[str, Any]) -> None:
        expected_keys = ["first_orientation_locator", "second_orientation_locator"]
        self.assertEqual(permission["supported_lookup_keys"], expected_keys)
        self.assertEqual(permission["covered_lookup_keys"], expected_keys)
        self.assertEqual(permission["permitted_lookup_keys"], expected_keys)
        self.assertEqual(permission["supported_lookup_key_count"], 2)
        self.assertEqual(permission["covered_lookup_key_count"], 2)
        self.assertEqual(permission["permitted_lookup_key_count"], 2)
        self.assertIs(permission["both_supported_lookup_keys_covered"], True)
        self.assertIs(permission["lookup_pair_coverage_recorded"], True)
        self.assertIs(permission["coverage_only_preserved"], True)
        self.assertIs(permission["boundary_recorded"], True)
        self.assertIs(permission["future_reusable_read_only_lookup_permission_was_considered"], True)
        self.assertIs(permission["reusable_read_only_lookup_permission_created"], True)
        self.assertIs(permission["reusable_read_only_lookup_permission_scope_bounded"], True)
        self.assertIs(permission["repeated_read_only_deterministic_lookup_permitted"], True)
        self.assertIs(permission["unsupported_lookup_keys_permitted"], False)

    def assert_serialized_has_no_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def recorded_synthetic_result(self) -> dict[str, Any]:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, coverage_path, _, _ = _write_synthetic_artifacts(Path(tmp))
            request = _build_valid_request(boundary_path, coverage_path)
            return resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min(
                request
            )

    def test_public_api_constants_and_output_root(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min",
            "resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_from_path",
            "write_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_result",
            "build_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_PERMISSION_TYPE_VALUES",
            "SUPPORTED_PERMISSION_SCOPE_VALUES",
            "SUPPORTED_LOOKUP_KEYS",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min",
        )
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION",
            resolver.SUPPORTED_PERMISSION_TYPE_VALUES,
        )
        self.assertIn(
            "REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY",
            resolver.SUPPORTED_PERMISSION_SCOPE_VALUES,
        )
        self.assertEqual(
            resolver.SUPPORTED_LOOKUP_KEYS,
            ["first_orientation_locator", "second_orientation_locator"],
        )

        output_root = REPO_ROOT / Path(resolver.OUTPUT_ROOT)
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            forbidden_root = REPO_ROOT / forbidden
            self.assertFalse(_is_same_or_under(output_root, forbidden_root), forbidden)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, coverage_path, _, _ = _write_synthetic_artifacts(Path(tmp))
            request = _build_valid_request(boundary_path, coverage_path)
            result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min(
                request
            )
            summary = resolver.build_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_summary(
                result
            )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["permission_id"], "local_relevance_medium_read_only_reusable_lookup_permission_001")

        for key in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(key, result)

        permission = self.permission(result)
        self.assertEqual(permission["permission_id"], "local_relevance_medium_read_only_reusable_lookup_permission_001")
        self.assertEqual(permission["permission_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION")
        self.assertEqual(permission["permission_version"], "0.1.0")
        self.assertEqual(permission["permission_scope"], "REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY")
        self.assertEqual(permission["basis_reusable_lookup_permission_boundary_artifact"], str(boundary_path))
        self.assertEqual(
            permission["basis_reusable_lookup_permission_boundary_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_RECORDED",
        )
        self.assertEqual(permission["basis_reusable_lookup_permission_boundary_result_version"], "0.1.0")
        self.assertEqual(permission["basis_reusable_lookup_permission_boundary_failed_check_count"], 0)
        self.assertEqual(permission["basis_lookup_pair_coverage_artifact"], str(coverage_path))
        self.assertEqual(
            permission["basis_lookup_pair_coverage_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_RECORDED",
        )
        self.assertEqual(permission["basis_lookup_pair_coverage_result_version"], "0.1.0")
        self.assertEqual(permission["basis_lookup_pair_coverage_failed_check_count"], 0)
        self.assert_permission_bounded_to_two_keys(permission)
        for key in PERMISSION_OBJECT_FALSE_FIELDS:
            self.assertIs(permission[key], False, key)
        self.assert_permission_object_not_wrapper(permission)

        statement = self.statement(result)
        for key in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIs(statement[key], True, key)
        self.assert_non_claims_canonical_false(result)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_BOUNDARY_ARTIFACT.exists() or not DEFAULT_LOOKUP_PAIR_COVERAGE_ARTIFACT.exists():
            self.skipTest("default reusable lookup permission boundary or lookup-pair coverage artifact absent")

        request = resolver.build_declared_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min(
            request
        )
        summary = resolver.build_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_summary(
            result
        )

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        permission = self.permission(result)
        self.assertEqual(permission["permission_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION")
        self.assertEqual(permission["permission_scope"], "REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY")
        self.assert_permission_bounded_to_two_keys(permission)
        self.assert_no_overreach(result)

    def test_required_non_claim_flips_block_and_canonicalize(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, coverage_path, _, _ = _write_synthetic_artifacts(Path(tmp))
            clean_request = _build_valid_request(boundary_path, coverage_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min(
                        request
                    )
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assert_public_codes(result)
                    self.assertGreater(
                        sum(1 for check in self.checks(result) if check.get("passed") is not True),
                        0,
                    )
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_non_claims_canonical_false(result)
                    self.assert_no_overreach(result)

    def test_representative_blocking_behavior(self) -> None:
        def boundary_object(artifact: dict[str, Any]) -> dict[str, Any]:
            return artifact["local_relevance_medium_read_only_reusable_lookup_permission_boundary"]

        def coverage_object(artifact: dict[str, Any]) -> dict[str, Any]:
            return artifact["local_relevance_medium_read_only_lookup_pair_coverage"]

        cases: list[tuple[str, dict[str, Any]]] = [
            (
                "explicit block intent",
                {
                    "request": {
                        "local_relevance_medium_read_only_reusable_lookup_permission_intent": (
                            resolver.INTENT_BLOCK
                        )
                    }
                },
            ),
            ("missing request", {"direct": {}}),
            ("non-mapping request", {"direct": "not a mapping"}),
            (
                "unsupported intent",
                {
                    "request": {
                        "local_relevance_medium_read_only_reusable_lookup_permission_intent": (
                            "UNSUPPORTED_INTENT"
                        )
                    }
                },
            ),
            ("boundary artifact path missing", {"request": {"selected_reusable_lookup_permission_boundary_artifact": ""}}),
            ("boundary artifact unreadable", {"missing_boundary": True}),
            ("boundary artifact JSON array", {"boundary_raw": []}),
            ("boundary artifact not recorded", {"boundary": lambda artifact: artifact.update({"outcome": "NOT_RECORDED"})}),
            ("boundary artifact failed checks present", {"boundary": lambda artifact: artifact.update({"failed_check_count": 1})}),
            ("boundary artifact version not 0.1.0", {"boundary": lambda artifact: artifact.update({"result_version": "9.9.9"})}),
            ("coverage artifact path missing", {"request": {"selected_lookup_pair_coverage_artifact": ""}}),
            ("coverage artifact unreadable", {"missing_coverage": True}),
            ("coverage artifact JSON array", {"coverage_raw": []}),
            ("coverage artifact not recorded", {"coverage": lambda artifact: artifact.update({"outcome": "NOT_RECORDED"})}),
            ("coverage artifact failed checks present", {"coverage": lambda artifact: artifact.update({"failed_check_count": 1})}),
            ("coverage artifact version not 0.1.0", {"coverage": lambda artifact: artifact.update({"result_version": "9.9.9"})}),
            ("supported lookup keys not exact", {"coverage": lambda artifact: coverage_object(artifact).update({"supported_lookup_keys": ["first_orientation_locator"]})}),
            ("covered lookup keys not exact", {"coverage": lambda artifact: coverage_object(artifact).update({"covered_lookup_keys": ["first_orientation_locator"]})}),
            ("permitted lookup keys not exact", {"request": {"permitted_lookup_keys": ["first_orientation_locator"], "permitted_lookup_key_count": 1}}),
            ("supported lookup key count not two", {"coverage": lambda artifact: coverage_object(artifact).update({"supported_lookup_key_count": 1})}),
            ("covered lookup key count not two", {"coverage": lambda artifact: coverage_object(artifact).update({"covered_lookup_key_count": 1})}),
            ("permitted lookup key count not two", {"request": {"permitted_lookup_key_count": 1}}),
            ("both supported lookup keys covered not true", {"request": {"both_supported_lookup_keys_covered_not_true": True}}),
            ("lookup-pair coverage not recorded", {"coverage": lambda artifact: coverage_object(artifact).update({"lookup_pair_coverage_recorded": False})}),
            ("coverage-only posture not preserved", {"coverage": lambda artifact: coverage_object(artifact).update({"reusable_lookup_permission_created": True})}),
            ("boundary not recorded", {"boundary": lambda artifact: boundary_object(artifact).update({"boundary_type": "WRONG"})}),
            ("future reusable read-only lookup permission not considered", {"request": {"future_reusable_read_only_lookup_permission_not_considered": True}}),
            ("permission type missing", {"request_delete": ["permission_type"]}),
            ("permission type wrong", {"request": {"permission_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_GENERAL_LOOKUP_PERMISSION"}}),
            ("permission scope missing", {"request_delete": ["permission_scope"]}),
            ("permission scope wrong", {"request": {"permission_scope": "GENERAL_SCOPE"}}),
            ("reusable permission not created", {"request": {"reusable_read_only_lookup_permission_not_created": True}}),
            ("reusable permission scope not bounded", {"request": {"reusable_read_only_lookup_permission_scope_not_bounded": True}}),
            ("repeated deterministic lookup not permitted", {"request": {"repeated_read_only_deterministic_lookup_not_permitted": True}}),
            ("general lookup permission created", {"request": {"general_lookup_permission_created": True}}),
            ("arbitrary lookup permission created", {"request": {"arbitrary_lookup_permission_created": True}}),
            ("unsupported lookup keys permitted", {"request": {"unsupported_lookup_keys_permitted": True}}),
            ("new lookup result created", {"request": {"new_lookup_result_created": True}}),
            ("new lookup entry created", {"request": {"new_lookup_entry_created": True}}),
            ("new signal accepted", {"request": {"new_signal_accepted": True}}),
            ("new entry accepted", {"request": {"new_entry_accepted": True}}),
            ("new relevance object created", {"request": {"new_relevance_object_created": True}}),
            ("new index entry created", {"request": {"new_index_entry_created": True}}),
            ("filesystem discovery performed", {"request": {"filesystem_discovery_performed": True}}),
            ("registry created", {"request": {"registry_created": True}}),
            ("search surface created", {"request": {"search_surface_created": True}}),
            ("query surface created", {"request": {"query_surface_created": True}}),
            ("ranking surface created", {"request": {"ranking_surface_created": True}}),
            ("scoring surface created", {"request": {"scoring_surface_created": True}}),
            ("priority surface created", {"request": {"priority_surface_created": True}}),
            ("validity judgment created", {"request": {"validity_judgment_created": True}}),
            ("truth judgment created", {"request": {"truth_judgment_created": True}}),
            ("authority judgment created", {"request": {"authority_judgment_created": True}}),
            ("currentness judgment created", {"request": {"currentness_judgment_created": True}}),
            ("repeated reception permission created", {"request": {"repeated_reception_permission_created": True}}),
            ("arbitrary reception created", {"request": {"arbitrary_reception_created": True}}),
            ("feed created", {"request": {"feed_created": True}}),
            ("source transfer occurred", {"request": {"source_transfer_occurred": True}}),
            ("source receipt occurred", {"request": {"source_receipt_occurred": True}}),
            ("source created", {"request": {"source_created": True}}),
            ("authority created", {"request": {"authority_created": True}}),
            ("currentness created", {"request": {"currentness_created": True}}),
            ("truth created", {"request": {"truth_created": True}}),
            ("action created", {"request": {"action_created": True}}),
            ("synchronization created", {"request": {"synchronization_created": True}}),
            ("participation authorized", {"request": {"participation_authorized": True}}),
            ("participant role created", {"request": {"participant_role_created": True}}),
            ("runtime permission created", {"request": {"runtime_permission_created": True}}),
            ("public API created", {"request": {"public_api_created": True}}),
            ("participant-facing interface created", {"request": {"participant_facing_interface_created": True}}),
            ("distributed network behavior created", {"request": {"distributed_network_behavior_created": True}}),
            ("deployment created", {"request": {"deployment_created": True}}),
            ("public release created", {"request": {"public_release_created": True}}),
            ("operation permission created", {"request": {"operation_permission_created": True}}),
            ("broader reusable permission created", {"request": {"broader_reusable_permission_created": True}}),
            ("follow-on work authorized", {"request": {"follow_on_work_authorized": True}}),
            ("artifact existence treated as authority", {"request": {"artifact_existence_treated_as_reusable_lookup_permission_authority": True}}),
            ("latest file posture treated as authority", {"request": {"latest_file_posture_treated_as_reusable_lookup_permission_authority": True}}),
            ("repo local availability treated as authority", {"request": {"repo_local_availability_treated_as_reusable_lookup_permission_authority": True}}),
            ("hidden repo state used as content", {"request": {"hidden_repo_state_used_as_reusable_lookup_permission_content": True}}),
            ("hidden repo state used as authority", {"request": {"hidden_repo_state_used_as_reusable_lookup_permission_authority": True}}),
            ("predecessor failure repaired", {"request": {"predecessor_failure_repaired": True}}),
            ("predecessor failure hidden", {"request": {"predecessor_failure_hidden": True}}),
            ("predecessor failure claimed passed", {"request": {"predecessor_failure_claimed_passed": True}}),
            ("consumed request reopened", {"request": {"consumed_request_reopened": True}}),
            ("authorization token reused", {"request": {"authorization_token_reused": True}}),
            ("required non-claim flipped", {"non_claim": resolver.REQUIRED_FALSE_NON_CLAIMS[0]}),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            for name, setup in cases:
                with self.subTest(name=name):
                    case_root = tmp_path / name.replace(" ", "_").replace("/", "_")
                    boundary_path, coverage_path, boundary, coverage = _write_synthetic_artifacts(case_root)
                    if "boundary" in setup:
                        setup["boundary"](boundary)
                        _write_json(boundary_path, boundary)
                    if "coverage" in setup:
                        setup["coverage"](coverage)
                        _write_json(coverage_path, coverage)
                    if "boundary_raw" in setup:
                        _write_json(boundary_path, setup["boundary_raw"])
                    if "coverage_raw" in setup:
                        _write_json(coverage_path, setup["coverage_raw"])

                    if "direct" in setup:
                        request_or_direct = setup["direct"]
                    else:
                        request = _build_valid_request(boundary_path, coverage_path)
                        request.update(copy.deepcopy(setup.get("request", {})))
                        if setup.get("missing_boundary"):
                            request["selected_reusable_lookup_permission_boundary_artifact"] = str(
                                case_root / "missing_boundary.json"
                            )
                        if setup.get("missing_coverage"):
                            request["selected_lookup_pair_coverage_artifact"] = str(
                                case_root / "missing_coverage.json"
                            )
                        for key in setup.get("request_delete", []):
                            request.pop(key, None)
                        if "non_claim" in setup:
                            request["declared_non_claims"][setup["non_claim"]] = True
                        request_or_direct = request

                    result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min(
                        request_or_direct
                    )
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assert_public_codes(result)
                    self.assert_no_overreach(result)

    def test_missing_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, coverage_path, _, _ = _write_synthetic_artifacts(Path(tmp))
            clean_request = _build_valid_request(boundary_path, coverage_path)
            variants: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
                ("remove declared_non_claims", lambda request: request.pop("declared_non_claims", None)),
                ("empty declared_non_claims", lambda request: request.update({"declared_non_claims": {}})),
                (
                    "remove one required non-claim",
                    lambda request: request["declared_non_claims"].pop(
                        resolver.REQUIRED_FALSE_NON_CLAIMS[0],
                        None,
                    ),
                ),
                (
                    "one required non-claim string",
                    lambda request: request["declared_non_claims"].update(
                        {resolver.REQUIRED_FALSE_NON_CLAIMS[0]: "false"}
                    ),
                ),
                (
                    "one required non-claim none",
                    lambda request: request["declared_non_claims"].update(
                        {resolver.REQUIRED_FALSE_NON_CLAIMS[0]: None}
                    ),
                ),
            ]
            for name, mutate in variants:
                with self.subTest(name=name):
                    request = copy.deepcopy(clean_request)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min(
                        request
                    )
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS},
                    )
                    self.assert_public_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        result = self.recorded_synthetic_result()
        permission = self.permission(result)
        self.assertEqual(permission["permission_type"], "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION")
        self.assertEqual(permission["permission_scope"], "REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY")
        self.assertEqual(permission["supported_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(permission["covered_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(permission["permitted_lookup_keys"], ["first_orientation_locator", "second_orientation_locator"])
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BLOCKED",
            },
        )
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION", serialized)
        self.assertIn("REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY", serialized)
        self.assertIn("first_orientation_locator", serialized)
        self.assertNotEqual(permission["permission_type"], "[REDACTED_RAW_CONTENT]")
        self.assertNotEqual(permission["permission_scope"], "[REDACTED_RAW_CONTENT]")

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)

            def poison_boundary(artifact: dict[str, Any]) -> None:
                artifact["raw_reusable_lookup_permission_boundary_body"] = HOSTILE_SENTINELS[2]
                artifact["hidden_repo_state"] = HOSTILE_SENTINELS[-1]

            def poison_coverage(artifact: dict[str, Any]) -> None:
                artifact["raw_lookup_pair_coverage_body"] = HOSTILE_SENTINELS[3]

            boundary_path, coverage_path, _, _ = _write_synthetic_artifacts(
                tmp_path,
                poison_boundary,
                poison_coverage,
            )
            request = _build_valid_request(
                boundary_path,
                coverage_path,
                raw_reusable_lookup_permission_body=HOSTILE_SENTINELS[1],
                hidden_repo_state={"payload": HOSTILE_SENTINELS[-1]},
            )
            before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min(
                request
            )

        self.assertEqual(request, before)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_serialized_has_no_sentinels(result)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION", serialized)
        self.assertIn("first_orientation_locator", serialized)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_overreach(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary_path, coverage_path, _, _ = _write_synthetic_artifacts(tmp_path)
            request = _build_valid_request(boundary_path, coverage_path)
            request_path = tmp_path / "request.json"
            _write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_from_path(
                request_path
            )
            summary = resolver.build_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_summary(
                result
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_from_path(
                malformed_path
            )
            self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(malformed_result)

            array_path = tmp_path / "array.json"
            _write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(array_result)

            missing_result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_from_path(
                tmp_path / "missing.json"
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(missing_result)

            output_root = tmp_path / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_output = resolver.write_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_result(
                    result
                )
                second_output = resolver.write_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_result(
                    result
                )

            self.assertTrue(first_output.parent.exists())
            self.assertTrue(second_output.parent.exists())
            self.assertNotEqual(first_output, second_output)
            with first_output.open("r", encoding="utf-8") as handle:
                self.assertIsInstance(json.load(handle), dict)
            with second_output.open("r", encoding="utf-8") as handle:
                self.assertIsInstance(json.load(handle), dict)
            self.assertIn(
                "local_relevance_medium_read_only_reusable_lookup_permission_v0_min",
                str(first_output),
            )
            for forbidden in FORBIDDEN_OUTPUT_ROOTS:
                self.assertFalse(_is_same_or_under(first_output, REPO_ROOT / forbidden), forbidden)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            boundary_path, coverage_path, boundary_artifact, coverage_artifact = _write_synthetic_artifacts(
                Path(tmp)
            )
            request = _build_valid_request(
                boundary_path,
                coverage_path,
                raw_full_body={"payload": HOSTILE_SENTINELS[0]},
            )
            request_before = copy.deepcopy(request)
            declared_non_claims_before = copy.deepcopy(request["declared_non_claims"])
            boundary_path_before = request["selected_reusable_lookup_permission_boundary_artifact"]
            coverage_path_before = request["selected_lookup_pair_coverage_artifact"]
            boundary_artifact_before = copy.deepcopy(boundary_artifact)
            coverage_artifact_before = copy.deepcopy(coverage_artifact)
            permission_type_before = request["permission_type"]
            permission_scope_before = request["permission_scope"]

            result = resolver.resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min(
                request
            )

            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(request, request_before)
            self.assertEqual(request["declared_non_claims"], declared_non_claims_before)
            self.assertEqual(request["selected_reusable_lookup_permission_boundary_artifact"], boundary_path_before)
            self.assertEqual(request["selected_lookup_pair_coverage_artifact"], coverage_path_before)
            self.assertEqual(request["permission_type"], permission_type_before)
            self.assertEqual(request["permission_scope"], permission_scope_before)
            self.assertEqual(boundary_artifact, boundary_artifact_before)
            self.assertEqual(coverage_artifact, coverage_artifact_before)
            with boundary_path.open("r", encoding="utf-8") as handle:
                self.assertEqual(json.load(handle), boundary_artifact_before)
            with coverage_path.open("r", encoding="utf-8") as handle:
                self.assertEqual(json.load(handle), coverage_artifact_before)

    def test_predecessor_failure_preservation(self) -> None:
        result = self.recorded_synthetic_result()
        summary = resolver.build_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_summary(
            result
        )
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["predecessor_failure_not_repaired"], True)
        self.assertIs(summary["predecessor_failure_not_hidden"], True)
        self.assertIs(summary["predecessor_failure_not_claimed_passed"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
