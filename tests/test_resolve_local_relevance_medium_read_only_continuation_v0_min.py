"""Tests for the local relevance medium read-only continuation resolver.

This suite treats the target as one continuation resolver only. It verifies
that a LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION is recorded as a local,
read-only, selected-continuation-only, selected-state-only, basis-reference-only
object anchored to the selected first-operation / second-operation line. The
tests also preserve predecessor failed-lineage evidence and keep result-level
non-claims canonical false.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_read_only_continuation_v0_min as resolver  # noqa: E402


CONTINUATION_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION"
CONTINUATION_SCOPE = "SELECTED_CONTINUATION_ONLY"
SELECTED_COMMAND = "state"
REQ_FALSE = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
FIELD_CODES = getattr(
    resolver,
    "FIELD_BLOCK_CODES",
    {key: key.upper() for key in REQ_FALSE},
)
BASIS_SPECS = tuple(resolver.BASIS_ARTIFACT_SPECS)

EXPECTED_OUTCOME_FAMILY = {
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_NOT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_REQUIRES_ADDITIONAL_BASIS",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BLOCKED",
}

EXPECTED_WRAPPER_SECTIONS = {
    "local_relevance_medium_read_only_continuation_metadata",
    "declared_local_relevance_medium_read_only_continuation_question",
    "selected_continuation_boundary_artifact_basis",
    "selected_second_operation_artifact_basis",
    "selected_second_operation_boundary_artifact_basis",
    "selected_prior_result_reentry_cycle_artifact_basis",
    "selected_prior_result_reentry_boundary_artifact_basis",
    "selected_runtime_held_reentry_artifact_basis",
    "selected_runtime_held_reentry_boundary_artifact_basis",
    "selected_runtime_held_state_artifact_basis",
    "selected_runtime_held_state_boundary_artifact_basis",
    "selected_runtime_artifact_basis",
    "selected_runtime_boundary_artifact_basis",
    "selected_runtime_permission_artifact_basis",
    "selected_operation_execution_artifact_basis",
    "local_relevance_medium_read_only_continuation",
    "local_relevance_medium_read_only_continuation_checks",
    "local_relevance_medium_read_only_continuation_statement",
    "local_relevance_medium_read_only_continuation_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_continuation_summary",
}

FORBIDDEN_WRAPPER_FIELDS_IN_CONTINUATION = {
    "outcome",
    "block",
    "local_relevance_medium_read_only_continuation_checks",
    "non_claims",
    "local_relevance_medium_read_only_continuation_summary",
    "local_relevance_medium_read_only_continuation_metadata",
}

DEFAULT_SUFFIXES = {
    "selected_continuation_boundary_artifact": (
        "local_relevance_medium_read_only_continuation_boundary_reference_review_001"
        "__local_relevance_medium_read_only_continuation_boundary_v0_min_result.json"
    ),
    "selected_second_operation_artifact": (
        "local_relevance_medium_read_only_second_operation_reference_review_001"
        "__local_relevance_medium_read_only_second_operation_v0_min_result.json"
    ),
    "selected_second_operation_boundary_artifact": (
        "local_relevance_medium_read_only_second_operation_boundary_reference_review_001"
        "__local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_result.json"
    ),
    "selected_prior_result_reentry_cycle_artifact": (
        "local_relevance_medium_read_only_prior_result_reentry_cycle_reference_review_001"
        "__local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_result.json"
    ),
    "selected_prior_result_reentry_boundary_artifact": (
        "local_relevance_medium_read_only_prior_result_reentry_boundary_reference_review_001"
        "__local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_result.json"
    ),
    "selected_runtime_held_reentry_artifact": (
        "local_relevance_medium_read_only_runtime_held_reentry_reference_review_001"
        "__local_relevance_medium_read_only_runtime_held_reentry_v0_min_result.json"
    ),
    "selected_runtime_held_reentry_boundary_artifact": (
        "local_relevance_medium_read_only_runtime_held_reentry_boundary_reference_review_001"
        "__local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min_result.json"
    ),
    "selected_runtime_held_state_artifact": (
        "local_relevance_medium_read_only_runtime_held_state_reference_review_001"
        "__local_relevance_medium_read_only_runtime_held_state_v0_min_result.json"
    ),
    "selected_runtime_held_state_boundary_artifact": (
        "local_relevance_medium_read_only_runtime_held_state_boundary_reference_review_001"
        "__local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result.json"
    ),
    "selected_runtime_artifact": (
        "local_relevance_medium_read_only_runtime_reference_review_001"
        "__local_relevance_medium_read_only_runtime_v0_min_v3_result.json"
    ),
    "selected_runtime_boundary_artifact": (
        "local_relevance_medium_read_only_runtime_boundary_reference_review_001"
        "__local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
    ),
    "selected_runtime_permission_artifact": (
        "local_relevance_medium_read_only_runtime_permission_reference_review_001"
        "__local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
    ),
    "selected_operation_execution_artifact": (
        "local_relevance_medium_read_only_operation_execution_reference_review_001"
        "__local_relevance_medium_read_only_operation_execution_v0_min_result.json"
    ),
}

LINEAGE_TRUE_FIELDS = (
    "second_operation_boundary_v1_failure_evidence_preserved",
    "second_operation_boundary_v2_successor_evidence_preserved",
    "prior_result_cycle_v1_failure_evidence_preserved",
    "prior_result_cycle_v2_successor_evidence_preserved",
    "prior_result_boundary_v1_failure_evidence_preserved",
    "prior_result_boundary_v2_successor_evidence_preserved",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "lookup_command_execution_boundary_v1_filename_path_failure_evidence_preserved",
    "state_packet_body_exposure_boundary_v0_failure_evidence_preserved",
    "state_packet_body_exposure_v1_over_strict_test_evidence_preserved",
    "local_carrier_command_execution_boundary_v1_over_strict_failure_evidence_preserved",
)

FALSE_POSTURE_FIELDS = REQ_FALSE + ("continuation_created",)

HOSTILE_SENTINELS = (
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_PRIOR_RESULT_REENTRY_CYCLE_BODY_MUST_NOT_RETURN",
    "RAW_PRIOR_RESULT_REENTRY_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_STATE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_STATE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def _basis_spec_by_name(name: str) -> Mapping[str, Any]:
    for spec in BASIS_SPECS:
        if spec["name"] == name:
            return spec
    raise AssertionError(f"unknown basis spec {name!r}")


def _true_fields_for_basis(name: str) -> dict[str, Any]:
    common = {
        "selected_command": SELECTED_COMMAND,
        "selected_command_is_state": True,
        "selected_command_preserved": True,
    }
    common.update({key: True for key in LINEAGE_TRUE_FIELDS})

    by_name: dict[str, dict[str, Any]] = {
        "continuation_boundary": {
            "selected_continuation_boundary_recorded": True,
            "continuation_boundary_recorded": True,
            "local_relevance_medium_read_only_continuation_boundary_recorded": True,
            "future_continuation_may_be_considered": True,
        },
        "second_operation": {
            "selected_second_operation_recorded": True,
            "second_operation_recorded": True,
            "local_relevance_medium_read_only_second_operation_recorded": True,
            "second_operation_created": True,
            "local_relevance_medium_read_only_second_operation_created": True,
            "second_operation_local_only": True,
            "local_relevance_medium_read_only_second_operation_local_only": True,
            "local_only": True,
            "second_operation_read_only": True,
            "local_relevance_medium_read_only_second_operation_read_only": True,
            "read_only": True,
            "second_operation_basis_reference_only": True,
            "basis_reference_only": True,
            "second_operation_sequence_index_is_2": True,
            "operation_sequence_index": 2,
            "sequence_index": 2,
        },
        "second_operation_boundary": {
            "selected_second_operation_boundary_recorded": True,
            "second_operation_boundary_recorded": True,
            "local_relevance_medium_read_only_second_operation_boundary_recorded": True,
            "future_second_operation_may_be_considered": True,
        },
        "prior_result_reentry_cycle": {
            "selected_prior_result_reentry_cycle_recorded": True,
            "prior_result_reentry_cycle_recorded": True,
            "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded": True,
            "prior_result_reentry_cycle_created": True,
            "local_relevance_medium_read_only_prior_result_reentry_cycle_created": True,
            "prior_result_reentry_cycle_local_only": True,
            "local_relevance_medium_read_only_prior_result_reentry_cycle_local_only": True,
            "prior_result_reentry_cycle_read_only": True,
            "local_relevance_medium_read_only_prior_result_reentry_cycle_read_only": True,
            "cycle_basis_reference_only": True,
            "basis_reference_only": True,
            "local_only": True,
            "read_only": True,
        },
        "prior_result_reentry_boundary": {
            "selected_prior_result_reentry_boundary_recorded": True,
            "prior_result_reentry_boundary_recorded": True,
            "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded": True,
            "future_prior_result_reentry_cycle_may_be_considered": True,
        },
        "runtime_held_reentry": {
            "selected_runtime_held_reentry_recorded": True,
            "runtime_held_reentry_recorded": True,
            "local_relevance_medium_read_only_runtime_held_reentry_recorded": True,
            "runtime_held_reentry_created": True,
            "local_relevance_medium_read_only_runtime_held_reentry_created": True,
            "runtime_held_reentry_local_only": True,
            "local_relevance_medium_read_only_runtime_held_reentry_local_only": True,
            "runtime_held_reentry_read_only": True,
            "local_relevance_medium_read_only_runtime_held_reentry_read_only": True,
            "held_reentry_basis_reference_only": True,
            "runtime_held_reentry_basis_reference_only": True,
            "basis_reference_only": True,
            "local_only": True,
            "read_only": True,
        },
        "runtime_held_reentry_boundary": {
            "selected_runtime_held_reentry_boundary_recorded": True,
            "runtime_held_reentry_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_held_reentry_boundary_recorded": True,
            "future_runtime_held_reentry_may_be_considered": True,
        },
        "runtime_held_state": {
            "selected_runtime_held_state_recorded": True,
            "runtime_held_state_recorded": True,
            "local_relevance_medium_read_only_runtime_held_state_recorded": True,
            "runtime_held_state_created": True,
            "local_relevance_medium_read_only_runtime_held_state_created": True,
            "runtime_held_state_local_only": True,
            "local_relevance_medium_read_only_runtime_held_state_local_only": True,
            "runtime_held_state_read_only": True,
            "local_relevance_medium_read_only_runtime_held_state_read_only": True,
            "held_state_basis_reference_only": True,
            "runtime_held_state_basis_reference_only": True,
            "basis_reference_only": True,
            "local_only": True,
            "read_only": True,
        },
        "runtime_held_state_boundary": {
            "selected_runtime_held_state_boundary_recorded": True,
            "runtime_held_state_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_held_state_boundary_recorded": True,
            "future_runtime_held_state_may_be_considered": True,
        },
        "runtime": {
            "selected_runtime_recorded": True,
            "runtime_recorded": True,
            "local_relevance_medium_read_only_runtime_recorded": True,
            "runtime_created": True,
            "local_relevance_medium_read_only_runtime_created": True,
            "runtime_local_only": True,
            "local_relevance_medium_read_only_runtime_local_only": True,
            "runtime_read_only": True,
            "local_relevance_medium_read_only_runtime_read_only": True,
            "local_only": True,
            "read_only": True,
        },
        "runtime_boundary": {
            "selected_runtime_boundary_recorded": True,
            "runtime_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_boundary_recorded": True,
            "future_runtime_may_be_considered": True,
        },
        "runtime_permission": {
            "selected_runtime_permission_recorded": True,
            "runtime_permission_recorded": True,
            "local_relevance_medium_read_only_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "local_relevance_medium_read_only_runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "local_relevance_medium_read_only_runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
            "local_relevance_medium_read_only_runtime_permission_read_only": True,
            "local_only": True,
            "read_only": True,
        },
        "operation_execution": {
            "selected_operation_execution_recorded": True,
            "operation_execution_recorded": True,
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "operation_execution_created": True,
            "local_relevance_medium_read_only_operation_execution_created": True,
            "operation_execution_performed": True,
            "local_relevance_medium_read_only_operation_execution_performed": True,
            "operation_execution_local_only": True,
            "local_relevance_medium_read_only_operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "local_relevance_medium_read_only_operation_execution_read_only": True,
            "local_only": True,
            "read_only": True,
        },
    }
    result = dict(common)
    result.update(by_name[name])
    return result


class LocalRelevanceMediumReadOnlyContinuationV0MinTests(unittest.TestCase):
    def assert_not_blocked(self, result):
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def block_code(self, result: Mapping[str, Any]) -> Any:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

    def safe_json_filename(self, name, index=None):
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

    def assert_blocked_with_public_code(self, result):
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_continuation_non_claims(result)

    def assert_same_or_stable_artifact_path(self, actual, expected):
        actual_path = Path(str(actual))
        expected_path = Path(str(expected))
        try:
            self.assertEqual(actual_path.resolve(), expected_path.resolve())
            return
        except (AssertionError, OSError):
            pass
        self.assertTrue(
            str(actual).endswith(expected_path.name),
            f"{actual!r} does not resolve to or end with {expected_path.name!r}",
        )

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        checks = result.get("local_relevance_medium_read_only_continuation_checks", [])
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is False
        )

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        checks = result.get("local_relevance_medium_read_only_continuation_checks", [])
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is True
        )

    def continuation(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        continuation = result["local_relevance_medium_read_only_continuation"]
        self.assertIsInstance(continuation, Mapping)
        return continuation

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result["local_relevance_medium_read_only_continuation_statement"]
        self.assertIsInstance(statement, Mapping)
        return statement

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = resolver.build_local_relevance_medium_read_only_continuation_v0_min_summary(
            result
        )
        self.assertIsInstance(summary, Mapping)
        return summary

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in result.get("local_relevance_medium_read_only_continuation_checks", []):
            if not isinstance(check, Mapping):
                continue
            for key in ("block_code", "failure_code"):
                emitted = check.get(key)
                if emitted is not None:
                    self.assertIn(emitted, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, Mapping)
        for key in REQ_FALSE:
            self.assertIn(key, non_claims)
            self.assertIs(type(non_claims[key]), bool)
            self.assertIs(non_claims[key], False)

    def assert_continuation_non_claims(self, result: Mapping[str, Any]) -> None:
        continuation = self.continuation(result)
        for key in REQ_FALSE:
            self.assertIs(continuation.get(key), False, key)
        for key in (
            "continuation_created",
            "continuation_local_only",
            "continuation_read_only",
            "continuation_basis_reference_only",
            "continuation_selected_state_only",
            "continuation_from_second_operation",
            "continuation_sequence_count_is_2",
        ):
            self.assertNotIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)

    def assert_wrapper_separate_from_continuation(self, result: Mapping[str, Any]) -> None:
        continuation = self.continuation(result)
        for key in FORBIDDEN_WRAPPER_FIELDS_IN_CONTINUATION:
            self.assertNotIn(key, continuation)

    def assert_clean_basis_sections(self, result: Mapping[str, Any]) -> None:
        continuation = self.continuation(result)
        for spec in BASIS_SPECS:
            basis_section = result[str(spec["basis_section"])]
            self.assertIsInstance(basis_section, Mapping)
            self.assertEqual(basis_section["outcome"], spec["expected_outcome"])
            self.assertEqual(basis_section["result_version"], resolver.RESULT_VERSION)
            self.assertEqual(basis_section["failed_check_count"], 0)
            self.assertIs(basis_section["artifact_preserved"], True)
            prefix = str(spec["basis_prefix"])
            self.assertEqual(
                continuation[f"{prefix}_outcome"],
                spec["expected_outcome"],
            )
            self.assertEqual(
                continuation[f"{prefix}_result_version"],
                resolver.RESULT_VERSION,
            )
            self.assertEqual(continuation[f"{prefix}_failed_check_count"], 0)

    def assert_clean_continuation_object(self, result: Mapping[str, Any]) -> None:
        continuation = self.continuation(result)
        self.assertEqual(
            continuation["continuation_id"],
            "local_relevance_medium_read_only_continuation_001",
        )
        self.assertEqual(continuation["continuation_type"], CONTINUATION_TYPE)
        self.assertEqual(continuation["continuation_version"], resolver.RESULT_VERSION)
        self.assertEqual(continuation["continuation_scope"], CONTINUATION_SCOPE)
        self.assertEqual(continuation["selected_command"], SELECTED_COMMAND)
        self.assertIs(continuation["selected_command_is_state"], True)
        for key in resolver.POSITIVE_BASIS_FIELDS:
            self.assertIs(continuation[key], True, key)
        self.assertIs(
            continuation["local_relevance_medium_read_only_continuation_recorded"],
            True,
        )
        for key in (
            "continuation_created",
            "continuation_local_only",
            "continuation_read_only",
            "continuation_basis_reference_only",
            "continuation_selected_state_only",
            "continuation_from_second_operation",
            "continuation_sequence_count_is_2",
        ):
            self.assertIs(continuation[key], True, key)
        self.assertEqual(continuation["continuation_operation_sequence_count"], 2)
        self.assertEqual(continuation["operation_sequence_index"], 2)
        self.assert_continuation_non_claims(result)
        self.assert_failure_lineage_preserved(result)
        self.assert_wrapper_separate_from_continuation(result)

    def assert_statement_posture(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        for key in (
            "local_relevance_medium_read_only_continuation_recorded",
            "selected_command_preserved",
            "continuation_created",
            "continuation_local_only",
            "continuation_read_only",
            "continuation_basis_reference_only",
            "continuation_selected_state_only",
            "continuation_from_second_operation",
            "continuation_sequence_count_is_2",
            "consumed_request_token_remains_closed",
            "authorization_token_reuse_blocked",
            "predecessor_failure_evidence_preserved",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(statement[key], True, key)
        self.assertEqual(statement["continuation_operation_sequence_count"], 2)
        for spec in BASIS_SPECS:
            self.assertIs(statement[str(spec["preserved_key"])], True)
        for key in LINEAGE_TRUE_FIELDS:
            self.assertIs(statement[key], True, key)
        for key in REQ_FALSE:
            self.assertIs(statement[key], False, key)

    def assert_failure_lineage_preserved(self, result: Mapping[str, Any]) -> None:
        continuation = self.continuation(result)
        summary = self.summary(result)
        for key in LINEAGE_TRUE_FIELDS:
            self.assertIs(continuation.get(key), True, key)
            self.assertIs(summary.get(key), True, key)
        for stem in (
            "second_operation_boundary_v1_failure",
            "prior_result_cycle_v1_failure",
            "prior_result_boundary_v1_failure",
            "runtime_v0_failure",
            "runtime_v2_failure",
            "runtime_boundary_v0_failure",
        ):
            for suffix in ("repaired", "hidden", "claimed_passed"):
                key = f"{stem}_{suffix}"
                self.assertIs(continuation.get(key), False, key)
        for key in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertIs(continuation.get(key), False, key)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["failure_not_repaired"], True)
        self.assertIs(summary["failure_not_hidden"], True)
        self.assertIs(summary["failure_not_claimed_passed"], True)

    def assert_result_recorded_clean(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assertEqual(
            result["local_relevance_medium_read_only_continuation_metadata"][
                "resolver_module"
            ],
            resolver.RESOLVER_MODULE,
        )
        self.assertEqual(
            result["local_relevance_medium_read_only_continuation_metadata"][
                "local_relevance_medium_read_only_continuation_version"
            ],
            resolver.RESULT_VERSION,
        )
        self.assertTrue(EXPECTED_WRAPPER_SECTIONS.issubset(result.keys()))
        self.assert_clean_basis_sections(result)
        self.assert_clean_continuation_object(result)
        self.assert_statement_posture(result)

    def assert_serialized_without_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def _write_json(self, path: Path, value: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def _artifact_for(
        self,
        spec: Mapping[str, Any],
        *,
        omit_object_fields: tuple[str, ...] = (),
        selected_overrides: Mapping[str, Any] | None = None,
        statement_overrides: Mapping[str, Any] | None = None,
        summary_overrides: Mapping[str, Any] | None = None,
        non_meaning_overrides: Mapping[str, Any] | None = None,
        top_level_non_claim_overrides: Mapping[str, Any] | None = None,
        extra_sections: Mapping[str, Any] | None = None,
        outcome: str | None = None,
        result_version: str = "0.1.0",
        failed_check_count: int = 0,
    ) -> dict[str, Any]:
        name = str(spec["name"])
        prefix = f"local_relevance_medium_read_only_{name}"
        true_fields = _true_fields_for_basis(name)
        false_fields = {key: False for key in FALSE_POSTURE_FIELDS}
        selected = {
            str(spec["type_field"]): spec["type_value"],
            str(spec["scope_field"]): spec["scope_value"],
            **true_fields,
            **false_fields,
        }
        for key in omit_object_fields:
            selected.pop(key, None)
        if selected_overrides:
            selected.update(dict(selected_overrides))

        statement = {**true_fields, **false_fields}
        summary = {**true_fields, **false_fields}
        non_meaning = {
            **{key: True for key in LINEAGE_TRUE_FIELDS},
            **false_fields,
            "predecessor_failure_evidence_preserved": True,
            "result_level_non_claims_canonical_false": True,
        }
        if statement_overrides:
            statement.update(dict(statement_overrides))
        if summary_overrides:
            summary.update(dict(summary_overrides))
        if non_meaning_overrides:
            non_meaning.update(dict(non_meaning_overrides))

        non_claims = {key: False for key in REQ_FALSE}
        non_claims["continuation_created"] = False
        if top_level_non_claim_overrides:
            non_claims.update(dict(top_level_non_claim_overrides))

        artifact = {
            "outcome": outcome or spec["expected_outcome"],
            "result_version": result_version,
            "failed_check_count": failed_check_count,
            f"{prefix}_metadata": {
                "result_version": result_version,
                "selected_command": SELECTED_COMMAND,
            },
            spec["object_key"]: selected,
            f"{prefix}_statement": statement,
            f"{prefix}_summary": summary,
            f"{prefix}_non_meaning": non_meaning,
            "non_claims": non_claims,
            f"{prefix}_checks": [
                {
                    "check_name": "synthetic_clean_basis",
                    "passed": True,
                    "expected_posture": True,
                    "actual_posture": True,
                }
            ],
        }
        if extra_sections:
            artifact.update(copy.deepcopy(dict(extra_sections)))
        return artifact

    def _write_synthetic_artifacts(
        self,
        root: Path,
        *,
        mutations: Mapping[str, Mapping[str, Any]] | None = None,
        name_suffix: str = "clean",
    ) -> tuple[dict[str, str], dict[str, dict[str, Any]]]:
        paths: dict[str, str] = {}
        artifacts: dict[str, dict[str, Any]] = {}
        mutations = mutations or {}
        for index, spec in enumerate(BASIS_SPECS, start=1):
            name = str(spec["name"])
            kwargs = dict(mutations.get(name, {}))
            artifact = self._artifact_for(spec, **kwargs)
            filename = self.safe_json_filename(f"{name}_{name_suffix}", index)
            path = root / filename
            self._write_json(path, artifact)
            paths[str(spec["request_key"])] = str(path)
            artifacts[name] = artifact
        return paths, artifacts

    def _valid_request(
        self,
        root: Path,
        *,
        mutations: Mapping[str, Mapping[str, Any]] | None = None,
        request_overrides: Mapping[str, Any] | None = None,
        name_suffix: str = "clean",
    ) -> tuple[dict[str, Any], dict[str, dict[str, Any]], dict[str, str]]:
        paths, artifacts = self._write_synthetic_artifacts(
            root,
            mutations=mutations,
            name_suffix=name_suffix,
        )
        request = resolver.build_declared_local_relevance_medium_read_only_continuation_v0_min_request(
            local_relevance_medium_read_only_continuation_id=(
                "local_relevance_medium_read_only_continuation_001"
            ),
            selected_continuation_boundary_artifact=paths[
                "selected_continuation_boundary_artifact"
            ],
            selected_second_operation_artifact=paths[
                "selected_second_operation_artifact"
            ],
            selected_second_operation_boundary_artifact=paths[
                "selected_second_operation_boundary_artifact"
            ],
            selected_prior_result_reentry_cycle_artifact=paths[
                "selected_prior_result_reentry_cycle_artifact"
            ],
            selected_prior_result_reentry_boundary_artifact=paths[
                "selected_prior_result_reentry_boundary_artifact"
            ],
            selected_runtime_held_reentry_artifact=paths[
                "selected_runtime_held_reentry_artifact"
            ],
            selected_runtime_held_reentry_boundary_artifact=paths[
                "selected_runtime_held_reentry_boundary_artifact"
            ],
            selected_runtime_held_state_artifact=paths[
                "selected_runtime_held_state_artifact"
            ],
            selected_runtime_held_state_boundary_artifact=paths[
                "selected_runtime_held_state_boundary_artifact"
            ],
            selected_runtime_artifact=paths["selected_runtime_artifact"],
            selected_runtime_boundary_artifact=paths[
                "selected_runtime_boundary_artifact"
            ],
            selected_runtime_permission_artifact=paths[
                "selected_runtime_permission_artifact"
            ],
            selected_operation_execution_artifact=paths[
                "selected_operation_execution_artifact"
            ],
        )
        if request_overrides:
            request.update(copy.deepcopy(dict(request_overrides)))
        return request, artifacts, paths

    def _resolve_clean(self, tmp: Path) -> dict[str, Any]:
        request, _, _ = self._valid_request(tmp)
        return resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
            request
        )

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_continuation_v0_min",
            "resolve_local_relevance_medium_read_only_continuation_v0_min_from_path",
            "write_local_relevance_medium_read_only_continuation_v0_min_result",
            "build_local_relevance_medium_read_only_continuation_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_continuation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_CONTINUATION_TYPE_VALUES",
            "SUPPORTED_CONTINUATION_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_continuation_v0_min",
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_continuation_v0_min"
            )
        )
        self.assertIn(CONTINUATION_TYPE, resolver.SUPPORTED_CONTINUATION_TYPE_VALUES)
        self.assertIn(CONTINUATION_SCOPE, resolver.SUPPORTED_CONTINUATION_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, SELECTED_COMMAND)
        self.assertEqual(set(resolver.OUTCOME_FAMILY), EXPECTED_OUTCOME_FAMILY)

        for key in (
            "third_operation_created",
            "unbounded_operation_sequence_created",
            "reusable_operation_permission_created",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "second_operation_boundary_v1_failure_repaired",
            "prior_result_cycle_v1_failure_repaired",
            "prior_result_boundary_v1_failure_repaired",
            "runtime_v0_failure_repaired",
            "runtime_v2_failure_repaired",
            "runtime_boundary_v0_failure_repaired",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in (
            "continuation_created",
            "continuation_local_only",
            "continuation_read_only",
            "continuation_basis_reference_only",
            "continuation_selected_state_only",
            "continuation_from_second_operation",
            "continuation_sequence_count_is_2",
        ):
            self.assertNotIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for code in (
            "THIRD_OPERATION_CREATED",
            "UNBOUNDED_OPERATION_SEQUENCE_CREATED",
            "REUSABLE_OPERATION_PERMISSION_CREATED",
            "RUNTIME_HOSTING_CREATED",
            "RUNTIME_LOOP_CREATED",
            "DAEMON_BEHAVIOR_CREATED",
            "RAW_STATE_BODY_EMBEDDED",
            "STATE_MUTATION_PERFORMED",
            "STATE_UPDATE_PERFORMED",
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "RUNTIME_AUTHORITY_IMPORTED",
            "SECOND_OPERATION_BOUNDARY_V1_FAILURE_REPAIRED",
            "PRIOR_RESULT_CYCLE_V1_FAILURE_REPAIRED",
            "PRIOR_RESULT_BOUNDARY_V1_FAILURE_REPAIRED",
            "RUNTIME_V0_FAILURE_REPAIRED",
            "RUNTIME_V2_FAILURE_REPAIRED",
            "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

        request = (
            resolver.build_declared_local_relevance_medium_read_only_continuation_v0_min_request()
        )
        for key, suffix in DEFAULT_SUFFIXES.items():
            self.assertTrue(str(request[key]).endswith(suffix), key)
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        self.assertEqual(request["continuation_type"], CONTINUATION_TYPE)
        self.assertEqual(request["continuation_scope"], CONTINUATION_SCOPE)
        self.assertIsInstance(request["declared_non_claims"], Mapping)
        for key in REQ_FALSE:
            self.assertIs(request["declared_non_claims"][key], False)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            result = self._resolve_clean(Path(td))
            self.assert_result_recorded_clean(result)

    def test_successful_recorded_result_from_default_live_artifacts_if_present(self) -> None:
        request = (
            resolver.build_declared_local_relevance_medium_read_only_continuation_v0_min_request()
        )
        missing = [
            path
            for path in (REPO_ROOT / request[key] for key in DEFAULT_SUFFIXES)
            if not path.exists()
        ]
        if missing:
            self.skipTest(f"default live continuation basis artifact missing: {missing[0]}")

        result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
            request
        )
        self.assert_result_recorded_clean(result)
        continuation = self.continuation(result)
        for spec in BASIS_SPECS:
            prefix = str(spec["basis_prefix"])
            self.assert_same_or_stable_artifact_path(
                continuation[f"{prefix}_artifact"],
                request[str(spec["request_key"])],
            )

    def test_positive_basis_derivation_from_bounded_sections_and_identity(self) -> None:
        omitted_fields = {
            "continuation_boundary": (
                "selected_continuation_boundary_recorded",
                "future_continuation_may_be_considered",
                "second_operation_boundary_v1_failure_evidence_preserved",
                "second_operation_boundary_v2_successor_evidence_preserved",
                "prior_result_cycle_v1_failure_evidence_preserved",
                "prior_result_cycle_v2_successor_evidence_preserved",
            ),
            "second_operation": (
                "selected_second_operation_recorded",
                "second_operation_created",
                "second_operation_local_only",
                "second_operation_read_only",
                "second_operation_basis_reference_only",
                "second_operation_sequence_index_is_2",
            ),
            "second_operation_boundary": (
                "selected_second_operation_boundary_recorded",
                "future_second_operation_may_be_considered",
            ),
            "prior_result_reentry_cycle": (
                "selected_prior_result_reentry_cycle_recorded",
            ),
            "prior_result_reentry_boundary": (
                "selected_prior_result_reentry_boundary_recorded",
            ),
            "runtime_held_reentry_boundary": (
                "selected_runtime_held_reentry_boundary_recorded",
            ),
            "runtime_held_state_boundary": (
                "selected_runtime_held_state_boundary_recorded",
            ),
            "runtime_boundary": ("selected_runtime_boundary_recorded",),
        }
        mutations = {
            name: {"omit_object_fields": tuple(fields)}
            for name, fields in omitted_fields.items()
        }
        with tempfile.TemporaryDirectory() as td:
            request, _, _ = self._valid_request(
                Path(td),
                mutations=mutations,
                name_suffix="positive_derivation",
            )
            result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                request
            )
            self.assert_result_recorded_clean(result)

    def test_forbidden_false_posture_ignores_explanatory_true_values(self) -> None:
        explanatory = {
            "statement_overrides": {
                "runtime_hosting_created_false_posture": True,
                "runtime_hosting_not_created": True,
                "runtime_loop_not_created": True,
                "daemon_behavior_not_created": True,
                "third_operation_not_created": True,
                "unbounded_operation_sequence_not_created": True,
                "reusable_operation_permission_not_created": True,
                "raw_state_body_embedded_false_posture": True,
                "state_mutation_performed_false_posture": True,
                "state_update_performed_false_posture": True,
                "older_runtime_authority_import_refusal_preserved": True,
                "result_level_non_claims_canonical_false": True,
                "follow_on_not_authorized": True,
                "continuation_created": True,
            },
            "summary_overrides": {
                "runtime_hosting_not_created": True,
                "runtime_loop_not_created": True,
                "daemon_behavior_not_created": True,
                "third_operation_not_created": True,
                "unbounded_operation_sequence_not_created": True,
                "reusable_operation_permission_not_created": True,
            },
            "non_meaning_overrides": {
                "false_posture_preserved": True,
                "non_claim_preservation": True,
                "lineage_evidence": True,
            },
            "extra_sections": {
                "metadata": {"runtime_hosting_not_created": True},
                "explanatory_posture": {"runtime_hosting_created_false_posture": True},
                "basis_commentary": {"actual_posture": True},
                "false_posture_preserved": {"runtime_loop_not_created": True},
                "non_claim_preservation": {"daemon_behavior_not_created": True},
                "lineage_evidence": {"continuation_created": True},
            },
        }
        mutations = {str(spec["name"]): explanatory for spec in BASIS_SPECS}
        with tempfile.TemporaryDirectory() as td:
            request, _, _ = self._valid_request(
                Path(td),
                mutations=mutations,
                name_suffix="explanatory_true",
            )
            result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                request
            )
            self.assert_result_recorded_clean(result)

    def test_exact_selected_object_and_top_level_non_claim_true_blocks(self) -> None:
        forbidden_cases = (
            "third_operation_created",
            "unbounded_operation_sequence_created",
            "reusable_operation_permission_created",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "consumed_request_reopened",
            "authorization_token_reused",
            "follow_on_work_authorized",
        )
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for index, key in enumerate(forbidden_cases, start=1):
                with self.subTest(selected_object_key=key):
                    mutations = {
                        "continuation_boundary": {
                            "selected_overrides": {key: True},
                        }
                    }
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"selected_{key}", index),
                        mutations=mutations,
                        name_suffix=f"selected_{key}",
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), FIELD_CODES[key])

                with self.subTest(top_level_non_claim=key):
                    mutations = {
                        "continuation_boundary": {
                            "omit_object_fields": (key,),
                            "top_level_non_claim_overrides": {key: True},
                        }
                    }
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"non_claim_{key}", index),
                        mutations=mutations,
                        name_suffix=f"non_claim_{key}",
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), FIELD_CODES[key])

    def test_declared_request_blocking_and_canonicalization(self) -> None:
        top_level_cases = (
            "consumed_request_reopened",
            "authorization_token_reused",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "third_operation_created",
            "unbounded_operation_sequence_created",
            "reusable_operation_permission_created",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "follow_on_work_authorized",
            "second_operation_boundary_v1_failure_repaired",
            "second_operation_boundary_v1_failure_hidden",
            "second_operation_boundary_v1_failure_claimed_passed",
            "prior_result_cycle_v1_failure_repaired",
            "prior_result_cycle_v1_failure_hidden",
            "prior_result_cycle_v1_failure_claimed_passed",
            "prior_result_boundary_v1_failure_repaired",
            "prior_result_boundary_v1_failure_hidden",
            "prior_result_boundary_v1_failure_claimed_passed",
            "runtime_v0_failure_repaired",
            "runtime_v0_failure_hidden",
            "runtime_v0_failure_claimed_passed",
            "runtime_v2_failure_repaired",
            "runtime_v2_failure_hidden",
            "runtime_v2_failure_claimed_passed",
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
        )
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for index, key in enumerate(top_level_cases, start=1):
                with self.subTest(top_level=key):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(key, index),
                        request_overrides={key: True},
                        name_suffix=key,
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), FIELD_CODES[key])
            for index, key in enumerate(REQ_FALSE, start=1):
                with self.subTest(declared_non_claim_flipped=key):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"flip_{key}", index),
                        name_suffix=f"flip_{key}",
                    )
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][key], False)
                with self.subTest(declared_non_claim_missing=key):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"missing_{key}", index),
                        name_suffix=f"missing_{key}",
                    )
                    del request["declared_non_claims"][key]
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                with self.subTest(declared_non_claim_non_bool=key):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"non_bool_{key}", index),
                        name_suffix=f"non_bool_{key}",
                    )
                    request["declared_non_claims"][key] = "false"
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_representative_basis_and_header_blocking(self) -> None:
        cases: list[tuple[str, str | None, Any]] = [
            (
                "explicit block intent",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_BLOCK_REQUESTED",
                lambda request, root: request.update(
                    {
                        "local_relevance_medium_read_only_continuation_intent": (
                            "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION"
                        )
                    }
                ),
            ),
            (
                "unsupported intent",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION_INTENT_UNSUPPORTED",
                lambda request, root: request.update(
                    {"local_relevance_medium_read_only_continuation_intent": "UNSUPPORTED"}
                ),
            ),
            (
                "selected command missing",
                "SELECTED_COMMAND_MISSING",
                lambda request, root: request.pop("selected_command", None),
            ),
            (
                "selected command not state",
                "SELECTED_COMMAND_NOT_STATE",
                lambda request, root: request.update({"selected_command": "status"}),
            ),
            (
                "continuation type missing",
                "CONTINUATION_TYPE_MISSING",
                lambda request, root: request.pop("continuation_type", None),
            ),
            (
                "continuation type unsupported",
                "CONTINUATION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_CONTINUATION",
                lambda request, root: request.update({"continuation_type": "PUBLIC_API"}),
            ),
            (
                "continuation scope missing",
                "CONTINUATION_SCOPE_MISSING",
                lambda request, root: request.pop("continuation_scope", None),
            ),
            (
                "continuation scope unsupported",
                "CONTINUATION_SCOPE_NOT_SELECTED_CONTINUATION_ONLY",
                lambda request, root: request.update({"continuation_scope": "GENERAL"}),
            ),
            (
                "required non claim missing",
                "NON_CLAIM_MISSING_OR_FLIPPED",
                lambda request, root: request["declared_non_claims"].pop(
                    "runtime_hosting_created",
                    None,
                ),
            ),
        ]

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for index, (name, expected_code, mutate) in enumerate(cases, start=1):
                with self.subTest(name=name):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(name, index),
                        name_suffix=name,
                    )
                    mutate(request, root)
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

            for spec in BASIS_SPECS:
                request_key = str(spec["request_key"])
                prefix = str(spec["block_prefix"])
                with self.subTest(artifact_path_missing=request_key):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"missing_{request_key}"),
                        name_suffix=f"missing_{request_key}",
                    )
                    request[request_key] = ""
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), f"{prefix}_PATH_MISSING")

                with self.subTest(artifact_unreadable=request_key):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"unreadable_{request_key}"),
                        name_suffix=f"unreadable_{request_key}",
                    )
                    request[request_key] = str(root / "does_not_exist.json")
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), f"{prefix}_UNREADABLE")

                with self.subTest(artifact_json_array=request_key):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"array_{request_key}"),
                        name_suffix=f"array_{request_key}",
                    )
                    array_path = root / self.safe_json_filename(f"array_{request_key}")
                    self._write_json(array_path, [])
                    request[request_key] = str(array_path)
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIn(
                        self.block_code(result),
                        {f"{prefix}_UNREADABLE", f"{prefix}_NOT_JSON_OBJECT"},
                    )

                with self.subTest(artifact_not_recorded=request_key):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"not_recorded_{request_key}"),
                        mutations={
                            str(spec["name"]): {
                                "outcome": f"{spec['expected_outcome']}_WRONG"
                            }
                        },
                        name_suffix=f"not_recorded_{request_key}",
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), f"{prefix}_NOT_RECORDED")

                with self.subTest(artifact_failed_checks=request_key):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"failed_{request_key}"),
                        mutations={
                            str(spec["name"]): {"failed_check_count": 1}
                        },
                        name_suffix=f"failed_{request_key}",
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(
                        self.block_code(result),
                        f"{prefix}_FAILED_CHECKS_PRESENT",
                    )

                with self.subTest(artifact_bad_version=request_key):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"version_{request_key}"),
                        mutations={
                            str(spec["name"]): {"result_version": "9.9.9"}
                        },
                        name_suffix=f"version_{request_key}",
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(
                        self.block_code(result),
                        f"{prefix}_VERSION_NOT_0_1_0",
                    )

            representative_positive = (
                ("continuation_boundary", "future_continuation_may_be_considered"),
                ("second_operation", "second_operation_created"),
                ("second_operation", "second_operation_local_only"),
                ("second_operation", "second_operation_read_only"),
                ("second_operation", "second_operation_basis_reference_only"),
                ("second_operation_boundary", "future_second_operation_may_be_considered"),
                ("prior_result_reentry_cycle", "prior_result_reentry_cycle_created"),
                ("prior_result_reentry_cycle", "prior_result_reentry_cycle_local_only"),
                ("prior_result_reentry_cycle", "prior_result_reentry_cycle_read_only"),
                ("prior_result_reentry_boundary", "future_prior_result_reentry_cycle_may_be_considered"),
                ("runtime_held_reentry", "runtime_held_reentry_created"),
                ("runtime_held_state", "runtime_held_state_created"),
                ("runtime", "runtime_created"),
                ("runtime_permission", "runtime_permission_created"),
                ("operation_execution", "operation_execution_performed"),
            )
            for name, field in representative_positive:
                with self.subTest(positive_basis_false=f"{name}:{field}"):
                    mutations = {name: {"selected_overrides": {field: False}}}
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(f"{name}_{field}_false"),
                        mutations=mutations,
                        name_suffix=f"{name}_{field}_false",
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)

            with self.subTest(second_operation_sequence_index_not_two=True):
                mutations = {
                    "second_operation": {
                        "selected_overrides": {
                            "operation_sequence_index": 3,
                            "sequence_index": 3,
                            "second_operation_sequence_index_is_2": False,
                        }
                    }
                }
                request, _, _ = self._valid_request(
                    root / "operation_sequence_index_not_2",
                    mutations=mutations,
                    name_suffix="operation_sequence_index_not_2",
                )
                result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                    request
                )
                self.assert_blocked_with_public_code(result)
                self.assertEqual(self.block_code(result), "OPERATION_SEQUENCE_INDEX_NOT_2")

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            result = self._resolve_clean(Path(td))
            self.assert_result_recorded_clean(result)
            continuation = self.continuation(result)
            self.assertEqual(continuation["continuation_type"], CONTINUATION_TYPE)
            self.assertEqual(continuation["continuation_scope"], CONTINUATION_SCOPE)
            self.assertEqual(continuation["selected_command"], SELECTED_COMMAND)
            serialized = json.dumps(result, sort_keys=True)
            for value in (
                resolver.OUTCOME_RECORDED,
                CONTINUATION_TYPE,
                CONTINUATION_SCOPE,
                SELECTED_COMMAND,
                resolver.RESOLVER_MODULE,
            ):
                self.assertIn(value, serialized)
            self.assertNotIn("[REDACTED", serialized)

    def test_raw_hidden_and_older_runtime_sentinels_are_sanitized(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            request, artifacts, paths = self._valid_request(
                root,
                request_overrides={
                    "raw_continuation_body": "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
                    "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
                    "older_runtime_authority_import_body": (
                        "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN"
                    ),
                },
                name_suffix="sentinel",
            )
            request_before = copy.deepcopy(request)
            for index, spec in enumerate(BASIS_SPECS):
                path = Path(paths[str(spec["request_key"])])
                artifact = copy.deepcopy(artifacts[str(spec["name"])])
                sentinel = HOSTILE_SENTINELS[index % len(HOSTILE_SENTINELS)]
                artifact["raw_full_prior_artifact_body"] = sentinel
                artifact["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
                artifact["raw_state_body"] = "RAW_STATE_BODY_MUST_NOT_RETURN"
                self._write_json(path, artifact)

            result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assert_blocked_with_public_code(result)
            else:
                self.assert_result_recorded_clean(result)
            self.assert_serialized_without_sentinels(result)
            self.assert_canonical_false_non_claims(result)
            self.assert_continuation_non_claims(result)
            continuation = self.continuation(result)
            self.assertEqual(continuation["continuation_type"], CONTINUATION_TYPE)
            self.assertEqual(continuation["continuation_scope"], CONTINUATION_SCOPE)
            self.assertEqual(continuation["selected_command"], SELECTED_COMMAND)
            self.assertEqual(request, request_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            request, _, _ = self._valid_request(root, name_suffix="path")
            request_path = root / "request.json"
            self._write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min_from_path(
                request_path
            )
            self.assert_result_recorded_clean(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = (
                resolver.resolve_local_relevance_medium_read_only_continuation_v0_min_from_path(
                    malformed_path
                )
            )
            self.assert_blocked_with_public_code(malformed)

            array_request_path = root / "array_request.json"
            self._write_json(array_request_path, [])
            array_result = (
                resolver.resolve_local_relevance_medium_read_only_continuation_v0_min_from_path(
                    array_request_path
                )
            )
            self.assert_blocked_with_public_code(array_result)

            missing_result = (
                resolver.resolve_local_relevance_medium_read_only_continuation_v0_min_from_path(
                    root / "missing_request.json"
                )
            )
            self.assert_blocked_with_public_code(missing_result)

            output_root = (
                root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_continuation_v0_min"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_local_relevance_medium_read_only_continuation_v0_min_result(
                    result
                )
                second = resolver.write_local_relevance_medium_read_only_continuation_v0_min_result(
                    result
                )
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn(
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_continuation_v0_min",
                first.parts,
            )
            with first.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            forbidden_parts = set(resolver.FORBIDDEN_OUTPUT_ROOT_PARTS)
            forbidden_parts.discard(
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_continuation_v0_min"
            )
            self.assertFalse(forbidden_parts.intersection(first.parts))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            explanatory = {
                "continuation_boundary": {
                    "statement_overrides": {
                        "runtime_hosting_not_created": True,
                        "continuation_created": True,
                    },
                    "extra_sections": {
                        "raw_state_body": "RAW_STATE_BODY_MUST_NOT_RETURN",
                    },
                }
            }
            request, artifacts, paths = self._valid_request(
                root,
                mutations=explanatory,
                name_suffix="non_mutation",
            )
            before_request = copy.deepcopy(request)
            before_artifacts = copy.deepcopy(artifacts)
            before_paths = copy.deepcopy(paths)
            result = resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                request
            )
            self.assert_result_recorded_clean(result)
            self.assertEqual(request, before_request)
            self.assertEqual(artifacts, before_artifacts)
            self.assertEqual(paths, before_paths)

    def test_failure_lineage_and_predecessor_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            result = self._resolve_clean(Path(td))
            self.assert_result_recorded_clean(result)
            self.assert_failure_lineage_preserved(result)
            summary = self.summary(result)
            for key in (
                "predecessor_failure_evidence_preserved",
                "result_level_non_claims_canonical_false",
                "consumed_request_token_remains_closed",
                "authorization_token_reuse_blocked",
                "older_runtime_lineage_not_imported_as_authority",
                "older_runtime_permission_not_treated_as_current",
                "runtime_authority_not_imported",
                "third_operation_not_created",
                "unbounded_operation_sequence_not_created",
                "reusable_operation_permission_not_created",
                "runtime_hosting_not_created",
                "runtime_loop_not_created",
                "daemon_behavior_not_created",
            ):
                self.assertIs(summary[key], True, key)
            for key in (
                "raw_state_body_embedded",
                "state_mutation_performed",
                "state_update_performed",
            ):
                self.assertIs(summary[key], False, key)

            flip_fields = (
                "second_operation_boundary_v1_failure_repaired",
                "second_operation_boundary_v1_failure_hidden",
                "second_operation_boundary_v1_failure_claimed_passed",
                "prior_result_cycle_v1_failure_repaired",
                "prior_result_cycle_v1_failure_hidden",
                "prior_result_cycle_v1_failure_claimed_passed",
                "prior_result_boundary_v1_failure_repaired",
                "prior_result_boundary_v1_failure_hidden",
                "prior_result_boundary_v1_failure_claimed_passed",
                "runtime_v0_failure_repaired",
                "runtime_v0_failure_hidden",
                "runtime_v0_failure_claimed_passed",
                "runtime_v2_failure_repaired",
                "runtime_v2_failure_hidden",
                "runtime_v2_failure_claimed_passed",
                "runtime_boundary_v0_failure_repaired",
                "runtime_boundary_v0_failure_hidden",
                "runtime_boundary_v0_failure_claimed_passed",
            )
            root = Path(td)
            for index, key in enumerate(flip_fields, start=1):
                with self.subTest(failure_lineage_flip=key):
                    request, _, _ = self._valid_request(
                        root / self.safe_json_filename(key, index),
                        request_overrides={key: True},
                        name_suffix=key,
                    )
                    blocked = (
                        resolver.resolve_local_relevance_medium_read_only_continuation_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(blocked)
                    self.assertEqual(self.block_code(blocked), FIELD_CODES[key])


if __name__ == "__main__":
    unittest.main()
