"""Tests for the local relevance medium read-only orientation lookup result.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT from one clean
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX. It verifies one declared
lookup key, one already-standing target, deterministic local lookup, and
canonical false non-claims.

The suite does not create registry, search, query surface, ranking, scoring,
priority, validity judgment, truth judgment, authority judgment, currentness
judgment, repeated reception permission, arbitrary reception, feed, new signal,
new entry, new relevance object, new index entry, filesystem discovery, source
transfer, source receipt, runtime permission, API, distributed behavior,
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

import resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min as resolver  # noqa: E402


DEFAULT_ORIENTATION_INDEX_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_index_system_v0_min/"
    "local_relevance_medium_read_only_orientation_index_reference_review_001__"
    "local_relevance_medium_read_only_orientation_index_system_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_lookup_result_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_index_system_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_comparison_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_relation_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_multiplicity_result_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_receipt_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_reception_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_successor_candidate_admission_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_successor_reception_request_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_runtime_loop_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_behavior_v0_min"),
)

FIRST_LOCATOR_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min/"
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
    "artifacts/"
    "integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min/"
    "relevance_orientation_view_reference_review_001__"
    "relevance_orientation_view_v0_min_result.json"
)
SECOND_ORIENTATION_VIEW_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min/"
    "local_relevance_medium_second_relevance_orientation_view_reference_review_001__"
    "local_relevance_medium_second_relevance_orientation_view_v0_min_result.json"
)

EXPECTED_TARGETS = {
    "first_orientation_locator": {
        "received_signal_id": "bounded_relevance_signal_001",
        "locator_entry_artifact": FIRST_LOCATOR_ARTIFACT,
        "orientation_view_artifact": FIRST_ORIENTATION_VIEW_ARTIFACT,
    },
    "second_orientation_locator": {
        "received_signal_id": "bounded_relevance_signal_002",
        "locator_entry_artifact": SECOND_LOCATOR_ARTIFACT,
        "orientation_view_artifact": SECOND_ORIENTATION_VIEW_ARTIFACT,
    },
}

EXPECTED_TOP_LEVEL_SECTIONS = {
    "local_relevance_medium_read_only_orientation_lookup_result_metadata",
    "declared_local_relevance_medium_read_only_orientation_lookup_result_question",
    "selected_local_relevance_medium_read_only_orientation_index_artifact_basis",
    "local_relevance_medium_read_only_orientation_lookup_result",
    "local_relevance_medium_read_only_orientation_lookup_result_checks",
    "local_relevance_medium_read_only_orientation_lookup_result_statement",
    "local_relevance_medium_read_only_orientation_lookup_result_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_orientation_lookup_result_summary",
}

WRAPPER_FIELDS_FORBIDDEN_IN_LOOKUP_RESULT = {
    "outcome",
    "block",
    "local_relevance_medium_read_only_orientation_lookup_result_checks",
    "non_claims",
    "local_relevance_medium_read_only_orientation_lookup_result_summary",
    "local_relevance_medium_read_only_orientation_lookup_result_metadata",
}

LOOKUP_RESULT_FALSE_FIELDS = (
    "new_signal_accepted",
    "new_entry_accepted",
    "new_relevance_object_created",
    "new_index_entry_created",
    "filesystem_discovery_performed",
    "registry_created",
    "search_surface_created",
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

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_INDEX_SYSTEM_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_INDEX_BODY_MUST_NOT_RETURN",
    "RAW_STATE_READER_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_COMPARISON_VIEW_BODY_MUST_NOT_RETURN",
    "RAW_RELATION_VIEW_BODY_MUST_NOT_RETURN",
    "RAW_MULTIPLICITY_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_LOCAL_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_LOCAL_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_CANDIDATE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RECEPTION_REQUEST_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def _write_json(path: Path, value: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return path


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _artifact_relative(path: Path | str) -> Path:
    candidate = Path(path)
    parts = candidate.parts
    if "artifacts" not in parts:
        return candidate
    return Path(*parts[parts.index("artifacts") :])


def _synthetic_orientation_index_artifact(
    *,
    include_index: bool = True,
    outcome: str = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_RECORDED",
    result_version: str = "0.1.0",
    failed_check_count: int = 0,
    index_mutator: Callable[[dict[str, Any]], None] | None = None,
    artifact_mutator: Callable[[dict[str, Any], dict[str, Any]], None] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    orientation_index: dict[str, Any] = {
        "orientation_index_id": "local_relevance_medium_read_only_orientation_index_001",
        "orientation_index_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
        "orientation_index_version": "0.1.0",
        "orientation_index_system_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
        "orientation_index_system_version": "0.1.0",
        "orientation_index_scope": "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
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
    }
    if index_mutator is not None:
        index_mutator(orientation_index)

    artifact: dict[str, Any] = {
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "local_relevance_medium_read_only_orientation_index_system_metadata": {
            "result_version": result_version,
            "resolver_module": "resolve_local_relevance_medium_read_only_orientation_index_system_v0_min",
            "failed_check_count": failed_check_count,
        },
        "local_relevance_medium_read_only_orientation_index_system_summary": {
            "result_version": result_version,
            "failed_check_count": failed_check_count,
        },
        "local_relevance_medium_read_only_orientation_index_system_checks": [
            {
                "check_name": "synthetic clean read-only orientation index system basis",
                "passed": failed_check_count == 0,
            }
        ],
    }
    if include_index:
        artifact["local_relevance_medium_read_only_orientation_index"] = orientation_index
    if artifact_mutator is not None:
        artifact_mutator(artifact, orientation_index)
    return artifact, orientation_index


def _write_valid_orientation_index_artifact(
    temp_root: Path,
    **kwargs: Any,
) -> tuple[Path, dict[str, Any], dict[str, Any]]:
    artifact, orientation_index = _synthetic_orientation_index_artifact(**kwargs)
    path = _write_json(temp_root / "synthetic_read_only_orientation_index_artifact.json", artifact)
    return path, artifact, orientation_index


def _build_request(
    artifact_path: Path | str,
    *,
    declared_lookup_key: str = "first_orientation_locator",
    **overrides: Any,
) -> dict[str, Any]:
    return resolver.build_declared_local_relevance_medium_read_only_orientation_lookup_result_v0_min_request(
        selected_local_relevance_medium_read_only_orientation_index_artifact=artifact_path,
        declared_lookup_key=declared_lookup_key,
        **overrides,
    )


def _lookup_result(result: Mapping[str, Any]) -> Mapping[str, Any]:
    lookup_result = result.get("local_relevance_medium_read_only_orientation_lookup_result")
    if not isinstance(lookup_result, Mapping):
        raise AssertionError("local_relevance_medium_read_only_orientation_lookup_result is not a mapping")
    return lookup_result


def _statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    statement = result.get("local_relevance_medium_read_only_orientation_lookup_result_statement")
    if not isinstance(statement, Mapping):
        raise AssertionError("lookup result statement is not a mapping")
    return statement


def _summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = result.get("local_relevance_medium_read_only_orientation_lookup_result_summary")
    if not isinstance(summary, Mapping):
        raise AssertionError("lookup result summary is not a mapping")
    return summary


def _checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    checks = result.get("local_relevance_medium_read_only_orientation_lookup_result_checks")
    if not isinstance(checks, list):
        raise AssertionError("lookup result checks is not a list")
    return checks


def _block_code(result: Mapping[str, Any]) -> str | None:
    block = result.get("block")
    if not isinstance(block, Mapping):
        return None
    code = block.get("block_code") or block.get("code")
    return code if isinstance(code, str) else None


class LocalRelevanceMediumReadOnlyOrientationLookupResultTests(unittest.TestCase):
    def assert_not_blocked(self, result):
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        code = _block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in _checks(result):
            for key in ("block_code", "failure_code"):
                emitted_code = check.get(key)
                if emitted_code is not None:
                    self.assertIn(emitted_code, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIs(type(non_claims[key]), bool)

    def assert_no_new_or_broader_behavior(self, result: Mapping[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        lookup_result = _lookup_result(result)
        for key in LOOKUP_RESULT_FALSE_FIELDS:
            if key in lookup_result:
                self.assertIs(lookup_result[key], False, key)

    def assert_lookup_result_not_wrapper_confused(self, result: Mapping[str, Any]) -> None:
        lookup_result = _lookup_result(result)
        for key in WRAPPER_FIELDS_FORBIDDEN_IN_LOOKUP_RESULT:
            self.assertNotIn(key, lookup_result)

    def assert_target_matches_declared_key(
        self,
        lookup_result: Mapping[str, Any],
        declared_lookup_key: str,
    ) -> None:
        expected = EXPECTED_TARGETS[declared_lookup_key]
        self.assertEqual(lookup_result["declared_lookup_key"], declared_lookup_key)
        self.assertEqual(
            lookup_result["selected_received_signal_id"],
            expected["received_signal_id"],
        )
        self.assertEqual(
            lookup_result["selected_locator_entry_artifact"],
            expected["locator_entry_artifact"],
        )
        self.assertEqual(
            lookup_result["selected_orientation_view_artifact"],
            expected["orientation_view_artifact"],
        )

    def assert_not_under_forbidden_roots(self, path: Path | str) -> None:
        relative_path = _artifact_relative(path)
        for forbidden_root in FORBIDDEN_OUTPUT_ROOTS:
            self.assertFalse(
                relative_path == forbidden_root
                or _is_relative_to(relative_path, forbidden_root),
                f"{relative_path} wrote under forbidden root {forbidden_root}",
            )

    def assert_recorded_lookup_result(
        self,
        result: Mapping[str, Any],
        artifact_path: Path | str,
        declared_lookup_key: str,
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        self.assertTrue(EXPECTED_TOP_LEVEL_SECTIONS.issubset(result.keys()))

        summary = _summary(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

        lookup_result = _lookup_result(result)
        self.assertEqual(
            lookup_result["lookup_result_id"],
            "local_relevance_medium_read_only_orientation_lookup_result_001",
        )
        self.assertEqual(
            lookup_result["lookup_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT",
        )
        self.assertEqual(lookup_result["lookup_result_version"], "0.1.0")
        self.assertEqual(
            lookup_result["lookup_result_scope"],
            "ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY",
        )
        self.assertEqual(
            lookup_result["basis_read_only_orientation_index_artifact"],
            str(artifact_path),
        )
        self.assertEqual(
            lookup_result["basis_read_only_orientation_index_system_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_RECORDED",
        )
        self.assertEqual(
            lookup_result["basis_read_only_orientation_index_system_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            lookup_result["basis_read_only_orientation_index_system_failed_check_count"],
            0,
        )
        self.assertEqual(
            lookup_result["basis_orientation_index_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
        )
        self.assertEqual(
            lookup_result["basis_orientation_index_system_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
        )
        self.assertEqual(
            lookup_result["basis_orientation_index_scope"],
            "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
        )
        self.assertIs(lookup_result["lookup_key_supported"], True)
        self.assertIs(lookup_result["lookup_target_found"], True)
        self.assert_target_matches_declared_key(lookup_result, declared_lookup_key)
        self.assertEqual(lookup_result["lookup_table_key_count"], 2)
        self.assertEqual(lookup_result["lookup_table_target_count"], 2)
        self.assertEqual(
            lookup_result["lookup_order"],
            ["first_orientation_locator", "second_orientation_locator"],
        )
        self.assertEqual(lookup_result["accepted_new_entries_count"], 0)
        self.assertIs(lookup_result["deterministic_local_lookup_preserved"], True)
        self.assertIs(lookup_result["read_only_lookup_result_recorded"], True)
        for key in LOOKUP_RESULT_FALSE_FIELDS:
            self.assertIs(lookup_result[key], False, key)

        self.assert_lookup_result_not_wrapper_confused(result)
        statement = _statement(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
        self.assert_non_claims_canonical_false(result)

    def assert_blocked_result(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        block_code = _block_code(result)
        self.assertIsNotNone(block_code)
        self.assertIn(block_code, resolver.BLOCK_CODES)
        self.assertGreater(_summary(result)["failed_check_count"], 0)
        self.assert_public_block_codes(result)
        self.assert_no_new_or_broader_behavior(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min",
            "resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min_from_path",
            "write_local_relevance_medium_read_only_orientation_lookup_result_v0_min_result",
            "build_local_relevance_medium_read_only_orientation_lookup_result_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_orientation_lookup_result_v0_min_request",
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
            "resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min",
        )
        self.assertTrue(Path(resolver.OUTPUT_ROOT).as_posix().endswith(EXPECTED_OUTPUT_ROOT.as_posix()))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT",
            resolver.SUPPORTED_LOOKUP_RESULT_TYPE_VALUES,
        )
        self.assertIn(
            "ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY",
            resolver.SUPPORTED_LOOKUP_RESULT_SCOPE_VALUES,
        )
        self.assertEqual(
            set(resolver.SUPPORTED_LOOKUP_KEYS),
            {"first_orientation_locator", "second_orientation_locator"},
        )
        self.assertEqual(
            resolver.LOOKUP_ORDER,
            ["first_orientation_locator", "second_orientation_locator"],
        )
        self.assert_not_under_forbidden_roots(resolver.OUTPUT_ROOT)

    def test_recorded_first_locator_from_synthetic_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _index = _write_valid_orientation_index_artifact(
                temp_root
            )
            request = _build_request(
                artifact_path,
                declared_lookup_key="first_orientation_locator",
            )
            result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
                request
            )
            self.assert_recorded_lookup_result(
                result,
                artifact_path,
                "first_orientation_locator",
            )

    def test_recorded_second_locator_from_synthetic_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _index = _write_valid_orientation_index_artifact(
                temp_root
            )
            request = _build_request(
                artifact_path,
                declared_lookup_key="second_orientation_locator",
            )
            result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
                request
            )
            self.assert_recorded_lookup_result(
                result,
                artifact_path,
                "second_orientation_locator",
            )
            lookup_result = _lookup_result(result)
            self.assertEqual(
                lookup_result["selected_received_signal_id"],
                "bounded_relevance_signal_002",
            )
            self.assertTrue(
                lookup_result["selected_locator_entry_artifact"].endswith(
                    "local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_result.json"
                )
            )
            self.assertTrue(
                lookup_result["selected_orientation_view_artifact"].endswith(
                    "local_relevance_medium_second_relevance_orientation_view_v0_min_result.json"
                )
            )

    def test_recorded_default_artifact_if_present(self) -> None:
        if not DEFAULT_ORIENTATION_INDEX_ARTIFACT.exists():
            self.skipTest("default local relevance medium read-only orientation index artifact is absent")

        request = resolver.build_declared_local_relevance_medium_read_only_orientation_lookup_result_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
            request
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(_summary(result)["failed_check_count"], 0)
        self.assert_not_blocked(result)
        lookup_result = _lookup_result(result)
        self.assertEqual(
            lookup_result["lookup_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT",
        )
        self.assertEqual(
            lookup_result["lookup_result_scope"],
            "ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY",
        )
        self.assert_target_matches_declared_key(
            lookup_result,
            "first_orientation_locator",
        )
        self.assertEqual(lookup_result["lookup_table_key_count"], 2)
        self.assertEqual(lookup_result["lookup_table_target_count"], 2)
        self.assertEqual(lookup_result["lookup_order"], resolver.LOOKUP_ORDER)
        self.assertEqual(lookup_result["accepted_new_entries_count"], 0)
        self.assertIs(lookup_result["deterministic_local_lookup_preserved"], True)
        for key in LOOKUP_RESULT_FALSE_FIELDS:
            self.assertIs(lookup_result[key], False, key)
        self.assert_no_new_or_broader_behavior(result)

    def test_required_false_non_claims_canonicalize_flipped_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _index = _write_valid_orientation_index_artifact(
                temp_root
            )
            clean_request = _build_request(artifact_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
                        request
                    )
                    self.assert_blocked_result(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertNotEqual(result["non_claims"][key], True)

    def test_representative_blocking_behavior(self) -> None:
        def req_set(key: str, value: Any) -> Callable[[dict[str, Any], Path], None]:
            def mutate(request: dict[str, Any], _temp_root: Path) -> None:
                request[key] = value

            return mutate

        def req_pop(key: str) -> Callable[[dict[str, Any], Path], None]:
            def mutate(request: dict[str, Any], _temp_root: Path) -> None:
                request.pop(key, None)

            return mutate

        def missing_path(request: dict[str, Any], temp_root: Path) -> None:
            request["selected_local_relevance_medium_read_only_orientation_index_artifact"] = str(
                temp_root / "missing_artifact.json"
            )

        def array_artifact(request: dict[str, Any], temp_root: Path) -> None:
            array_path = _write_json(temp_root / "array_artifact.json", [])
            request["selected_local_relevance_medium_read_only_orientation_index_artifact"] = str(
                array_path
            )

        def non_claim_missing(request: dict[str, Any], _temp_root: Path) -> None:
            request["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])

        def non_claim_flipped(request: dict[str, Any], _temp_root: Path) -> None:
            request["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = True

        def remove_lookup_key(index: dict[str, Any]) -> None:
            index["lookup_table"].pop("first_orientation_locator", None)

        def remove_target_field(key: str) -> Callable[[dict[str, Any]], None]:
            def mutate(index: dict[str, Any]) -> None:
                index["lookup_table"]["first_orientation_locator"].pop(key, None)

            return mutate

        request_cases: list[tuple[str, Callable[[dict[str, Any], Path], None]]] = [
            (
                "explicit block intent",
                req_set(
                    "local_relevance_medium_read_only_orientation_lookup_result_intent",
                    resolver.BLOCK_INTENT,
                ),
            ),
            (
                "unsupported intent",
                req_set(
                    "local_relevance_medium_read_only_orientation_lookup_result_intent",
                    "UNSUPPORTED_INTENT",
                ),
            ),
            (
                "selected orientation index artifact path missing",
                req_pop("selected_local_relevance_medium_read_only_orientation_index_artifact"),
            ),
            ("selected orientation index artifact unreadable", missing_path),
            ("selected orientation index artifact JSON array", array_artifact),
            ("declared lookup key missing", req_pop("declared_lookup_key")),
            ("declared lookup key unsupported", req_set("declared_lookup_key", "third_orientation_locator")),
            ("lookup result type missing", req_pop("lookup_result_type")),
            ("lookup result type wrong", req_set("lookup_result_type", "UNSUPPORTED_LOOKUP_RESULT_TYPE")),
            ("lookup result scope missing", req_pop("lookup_result_scope")),
            ("lookup result scope wrong", req_set("lookup_result_scope", "MANY_KEYS")),
            ("read-only lookup result not recorded", req_set("read_only_lookup_result_not_recorded", True)),
            ("new signal accepted", req_set("new_signal_accepted", True)),
            ("new entry accepted", req_set("new_entry_accepted", True)),
            ("new relevance object created", req_set("new_relevance_object_created", True)),
            ("new index entry created", req_set("new_index_entry_created", True)),
            ("filesystem discovery performed", req_set("filesystem_discovery_performed", True)),
            ("query surface created", req_set("query_surface_created", True)),
            ("registry created", req_set("registry_created", True)),
            ("search surface created", req_set("search_surface_created", True)),
            ("ranking surface created", req_set("ranking_surface_created", True)),
            ("scoring surface created", req_set("scoring_surface_created", True)),
            ("priority surface created", req_set("priority_surface_created", True)),
            ("validity judgment created", req_set("validity_judgment_created", True)),
            ("truth judgment created", req_set("truth_judgment_created", True)),
            ("authority judgment created", req_set("authority_judgment_created", True)),
            ("currentness judgment created", req_set("currentness_judgment_created", True)),
            ("repeated reception permission created", req_set("repeated_reception_permission_created", True)),
            ("arbitrary reception created", req_set("arbitrary_reception_created", True)),
            ("feed created", req_set("feed_created", True)),
            ("source transfer occurred", req_set("source_transfer_occurred", True)),
            ("source receipt occurred", req_set("source_receipt_occurred", True)),
            ("source created", req_set("source_created", True)),
            ("authority created", req_set("authority_created", True)),
            ("currentness created", req_set("currentness_created", True)),
            ("truth created", req_set("truth_created", True)),
            ("action created", req_set("action_created", True)),
            ("synchronization created", req_set("synchronization_created", True)),
            ("participation authorized", req_set("participation_authorized", True)),
            ("participant role created", req_set("participant_role_created", True)),
            ("runtime permission created", req_set("runtime_permission_created", True)),
            ("public API created", req_set("public_api_created", True)),
            ("participant-facing interface created", req_set("participant_facing_interface_created", True)),
            ("distributed network behavior created", req_set("distributed_network_behavior_created", True)),
            ("deployment created", req_set("deployment_created", True)),
            ("public release created", req_set("public_release_created", True)),
            ("operation permission created", req_set("operation_permission_created", True)),
            ("broader reusable permission created", req_set("broader_reusable_permission_created", True)),
            ("follow-on work authorized", req_set("follow_on_work_authorized", True)),
            (
                "artifact existence treated as read-only lookup result authority",
                req_set("artifact_existence_treated_as_read_only_lookup_result_authority", True),
            ),
            (
                "latest file posture treated as read-only lookup result authority",
                req_set("latest_file_posture_treated_as_read_only_lookup_result_authority", True),
            ),
            (
                "repo-local availability treated as read-only lookup result authority",
                req_set("repo_local_availability_treated_as_read_only_lookup_result_authority", True),
            ),
            (
                "hidden repo state used as read-only lookup result content",
                req_set("hidden_repo_state_used_as_read_only_lookup_result_content", True),
            ),
            (
                "hidden repo state used as read-only lookup result authority",
                req_set("hidden_repo_state_used_as_read_only_lookup_result_authority", True),
            ),
            ("predecessor failure repaired", req_set("predecessor_failure_repaired", True)),
            ("predecessor failure hidden", req_set("predecessor_failure_hidden", True)),
            ("predecessor failure claimed passed", req_set("predecessor_failure_claimed_passed", True)),
            ("consumed request reopened", req_set("consumed_request_reopened", True)),
            ("authorization token reused", req_set("authorization_token_reused", True)),
            ("required non-claim missing", non_claim_missing),
            ("required non-claim flipped", non_claim_flipped),
        ]

        artifact_cases: list[tuple[str, dict[str, Any]]] = [
            (
                "selected orientation index artifact not recorded",
                {"outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_NOT_RECORDED"},
            ),
            ("selected orientation index artifact failed checks present", {"failed_check_count": 1}),
            ("selected orientation index artifact version not 0.1.0", {"result_version": "9.9.9"}),
            ("local relevance medium read-only orientation index object missing", {"include_index": False}),
            (
                "orientation index type wrong",
                {
                    "index_mutator": lambda index: index.__setitem__(
                        "orientation_index_type",
                        "UNSUPPORTED_ORIENTATION_INDEX_TYPE",
                    )
                },
            ),
            (
                "orientation index system type wrong",
                {
                    "index_mutator": lambda index: index.__setitem__(
                        "orientation_index_system_type",
                        "UNSUPPORTED_ORIENTATION_INDEX_SYSTEM_TYPE",
                    )
                },
            ),
            (
                "orientation index scope wrong",
                {
                    "index_mutator": lambda index: index.__setitem__(
                        "orientation_index_scope",
                        "UNSUPPORTED_ORIENTATION_INDEX_SCOPE",
                    )
                },
            ),
            ("lookup target not found", {"index_mutator": remove_lookup_key}),
            (
                "selected received signal id missing",
                {"index_mutator": remove_target_field("received_signal_id")},
            ),
            (
                "selected locator entry artifact missing",
                {"index_mutator": remove_target_field("locator_entry_artifact")},
            ),
            (
                "selected orientation view artifact missing",
                {"index_mutator": remove_target_field("orientation_view_artifact")},
            ),
            (
                "lookup table not two entries",
                {
                    "index_mutator": lambda index: index["lookup_table"].pop(
                        "second_orientation_locator",
                        None,
                    )
                },
            ),
            (
                "lookup table target count not two",
                {"index_mutator": lambda index: index.__setitem__("lookup_target_count", 1)},
            ),
            (
                "lookup order not deterministic",
                {
                    "index_mutator": lambda index: index.__setitem__(
                        "lookup_order",
                        ["second_orientation_locator", "first_orientation_locator"],
                    )
                },
            ),
            (
                "accepted new entries count not zero",
                {"index_mutator": lambda index: index.__setitem__("accepted_new_entries_count", 1)},
            ),
            (
                "deterministic local lookup not preserved",
                {"index_mutator": lambda index: index.__setitem__("deterministic_local_lookup_enabled", False)},
            ),
        ]

        special_cases: list[tuple[str, Any]] = [
            ("missing request mapping fields", {}),
            ("non-mapping request", ["not", "mapping"]),
        ]

        for name, request_value in special_cases:
            with self.subTest(case=name):
                result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
                    request_value
                )
                self.assert_blocked_result(result)

        for name, request_mutator in request_cases:
            with self.subTest(case=name):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir)
                    artifact_path, _artifact, _index = _write_valid_orientation_index_artifact(
                        temp_root
                    )
                    request = _build_request(artifact_path)
                    request_mutator(request, temp_root)
                    result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
                        request
                    )
                    self.assert_blocked_result(result)

        for name, kwargs in artifact_cases:
            with self.subTest(case=name):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir)
                    artifact_path, _artifact, _index = _write_valid_orientation_index_artifact(
                        temp_root,
                        **kwargs,
                    )
                    request = _build_request(artifact_path)
                    result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
                        request
                    )
                    self.assert_blocked_result(result)

    def test_missing_or_incomplete_declared_non_claims_block_with_public_code(self) -> None:
        variants: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
            ("remove declared_non_claims", lambda request: request.pop("declared_non_claims", None)),
            ("empty declared_non_claims", lambda request: request.__setitem__("declared_non_claims", {})),
            (
                "remove one required non-claim",
                lambda request: request["declared_non_claims"].pop(
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0],
                    None,
                ),
            ),
            (
                "required non-claim as string",
                lambda request: request["declared_non_claims"].__setitem__(
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0],
                    "false",
                ),
            ),
            (
                "required non-claim as None",
                lambda request: request["declared_non_claims"].__setitem__(
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0],
                    None,
                ),
            ),
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _index = _write_valid_orientation_index_artifact(
                temp_root
            )
            clean_request = _build_request(artifact_path)
            for name, mutate in variants:
                with self.subTest(case=name):
                    request = copy.deepcopy(clean_request)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
                        request
                    )
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS},
                    )
                    self.assert_public_block_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _index = _write_valid_orientation_index_artifact(
                temp_root
            )
            result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
                _build_request(artifact_path)
            )
            lookup_result = _lookup_result(result)
            serialized = json.dumps(result, sort_keys=True)
            self.assertEqual(
                lookup_result["lookup_result_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT",
            )
            self.assertEqual(
                lookup_result["lookup_result_scope"],
                "ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY",
            )
            self.assertEqual(lookup_result["declared_lookup_key"], "first_orientation_locator")
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            for expected_outcome in (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_BLOCKED",
            ):
                self.assertIn(expected_outcome, resolver.OUTCOME_FAMILY)
            self.assertEqual(
                set(resolver.SUPPORTED_LOOKUP_KEYS),
                {"first_orientation_locator", "second_orientation_locator"},
            )
            for official_value in (
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT",
                "ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY",
                "first_orientation_locator",
                "second_orientation_locator",
            ):
                self.assertIn(official_value, serialized)
            self.assertNotIn("[REDACTED_RAW_CONTENT]", serialized)

    def test_raw_hidden_hostile_content_containment_and_non_mutation(self) -> None:
        sentinel_map = {
            "raw_full_body": HOSTILE_SENTINELS[0],
            "hidden_repo_state": HOSTILE_SENTINELS[-1],
            "extra_body": HOSTILE_SENTINELS[1],
        }

        def inject_artifact_sentinels(
            artifact: dict[str, Any],
            index: dict[str, Any],
        ) -> None:
            artifact["raw_orientation_index_system_body"] = HOSTILE_SENTINELS[2]
            artifact["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            index["raw_orientation_index_body"] = HOSTILE_SENTINELS[3]
            index["lookup_table"]["first_orientation_locator"]["raw_body"] = HOSTILE_SENTINELS[9]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _index = _write_valid_orientation_index_artifact(
                temp_root,
                artifact_mutator=inject_artifact_sentinels,
            )
            request = _build_request(artifact_path)
            request.update(copy.deepcopy(sentinel_map))
            request_before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            for sentinel in HOSTILE_SENTINELS:
                self.assertNotIn(sentinel, serialized)
            self.assertIn("LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT", serialized)
            self.assertIn("first_orientation_locator", serialized)
            self.assert_non_claims_canonical_false(result)
            self.assert_no_new_or_broader_behavior(result)
            self.assertEqual(request, request_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _index = _write_valid_orientation_index_artifact(
                temp_root
            )
            request = _build_request(artifact_path)
            request_path = _write_json(temp_root / "request.json", request)
            result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(_summary(result)["result_version"], "0.1.0")
            self.assertEqual(_summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min_from_path(
                malformed_path
            )
            self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(malformed_result)

            array_request_path = _write_json(temp_root / "array_request.json", [])
            array_result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min_from_path(
                array_request_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(array_result)

            missing_result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min_from_path(
                temp_root / "missing_request.json"
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(missing_result)

            patched_root = (
                temp_root
                / "artifacts/"
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_lookup_result_v0_min"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_root):
                first_path = resolver.write_local_relevance_medium_read_only_orientation_lookup_result_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_orientation_lookup_result_v0_min_result(
                    result
                )
            self.assertTrue(first_path.parent.exists())
            self.assertNotEqual(first_path, second_path)
            for path in (first_path, second_path):
                with path.open("r", encoding="utf-8") as handle:
                    parsed = json.load(handle)
                self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
                self.assertIn(
                    "local_relevance_medium_read_only_orientation_lookup_result_v0_min",
                    path.as_posix(),
                )
                self.assert_not_under_forbidden_roots(path)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact, orientation_index = _synthetic_orientation_index_artifact()
            artifact_before = copy.deepcopy(artifact)
            artifact_path = _write_json(
                temp_root / "synthetic_read_only_orientation_index_artifact.json",
                artifact,
            )
            request = _build_request(artifact_path)
            request["nested_raw_payload"] = {"raw_body": HOSTILE_SENTINELS[0]}
            request_before = copy.deepcopy(request)
            declared_non_claims_before = copy.deepcopy(request["declared_non_claims"])
            result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
                request
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(request, request_before)
            self.assertEqual(request["declared_non_claims"], declared_non_claims_before)
            self.assertEqual(artifact, artifact_before)
            self.assertEqual(
                orientation_index["orientation_index_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
            )
            self.assertEqual(
                orientation_index["orientation_index_system_type"],
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
            )
            self.assertEqual(
                orientation_index["orientation_index_scope"],
                "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
            )

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, _artifact, _index = _write_valid_orientation_index_artifact(
                temp_root
            )
            result = resolver.resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
                _build_request(artifact_path)
            )
            statement = _statement(result)
            summary = _summary(result)
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
