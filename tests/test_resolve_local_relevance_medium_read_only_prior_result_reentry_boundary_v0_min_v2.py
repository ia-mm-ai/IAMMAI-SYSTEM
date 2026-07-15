"""V2 tests for the local read-only prior-result re-entry boundary resolver.

This additive successor preserves
tests/test_resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min.py
as failed-lineage evidence. That v1 test failed in test_path_and_write_behavior
because it asserted paths written under tempfile.TemporaryDirectory() after the
temporary directory context had exited.

This v2 suite keeps the target boundary-shaped, selected-state-only, local,
read-only, raw-state-body-excluding, state-mutation-refusing,
state-update-refusing, closure-token-aware, non-cycle, non-second-operation,
non-continuation, non-hosting, non-loop, non-daemon, and
older-runtime-authority-import-blocking.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min as resolver


BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_PRIOR_RESULT_REENTRY_CONSIDERATION_ONLY"
SELECTED_COMMAND = "state"

RUNTIME_HELD_REENTRY_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_RECORDED"
RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY_RECORDED"
)
RUNTIME_HELD_STATE_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_RECORDED"
RUNTIME_HELD_STATE_BOUNDARY_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_RECORDED"
)
RUNTIME_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED"
RUNTIME_BOUNDARY_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED"
RUNTIME_PERMISSION_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED"
OPERATION_EXECUTION_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED"

EXPECTED_OUTCOME_FAMILY = {
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_NOT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_BLOCKED",
}

EXPECTED_WRAPPER_SECTIONS = {
    "local_relevance_medium_read_only_prior_result_reentry_boundary_metadata",
    "declared_local_relevance_medium_read_only_prior_result_reentry_boundary_question",
    "selected_runtime_held_reentry_artifact_basis",
    "selected_runtime_held_reentry_boundary_artifact_basis",
    "selected_runtime_held_state_artifact_basis",
    "selected_runtime_held_state_boundary_artifact_basis",
    "selected_runtime_artifact_basis",
    "selected_runtime_boundary_artifact_basis",
    "selected_runtime_permission_artifact_basis",
    "selected_operation_execution_artifact_basis",
    "local_relevance_medium_read_only_prior_result_reentry_boundary",
    "local_relevance_medium_read_only_prior_result_reentry_boundary_checks",
    "local_relevance_medium_read_only_prior_result_reentry_boundary_statement",
    "local_relevance_medium_read_only_prior_result_reentry_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_prior_result_reentry_boundary_summary",
}

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = {
    "outcome",
    "block",
    "local_relevance_medium_read_only_prior_result_reentry_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_prior_result_reentry_boundary_summary",
    "local_relevance_medium_read_only_prior_result_reentry_boundary_metadata",
}

BOUNDARY_TRUE_FIELDS = {
    "selected_command_is_state",
    "selected_runtime_held_reentry_recorded",
    "runtime_held_reentry_created",
    "runtime_held_reentry_local_only",
    "runtime_held_reentry_read_only",
    "held_reentry_basis_reference_only",
    "selected_runtime_held_reentry_boundary_recorded",
    "future_runtime_held_reentry_may_be_considered",
    "selected_runtime_held_state_recorded",
    "runtime_held_state_created",
    "runtime_held_state_local_only",
    "runtime_held_state_read_only",
    "held_state_basis_reference_only",
    "selected_runtime_held_state_boundary_recorded",
    "future_runtime_held_state_may_be_considered",
    "selected_runtime_recorded",
    "runtime_created",
    "runtime_local_only",
    "runtime_read_only",
    "selected_runtime_boundary_recorded",
    "future_runtime_may_be_considered",
    "selected_runtime_permission_recorded",
    "runtime_permission_created",
    "runtime_permission_local_only",
    "runtime_permission_read_only",
    "selected_operation_execution_recorded",
    "operation_execution_created",
    "operation_execution_performed",
    "operation_execution_local_only",
    "operation_execution_read_only",
    "future_prior_result_reentry_cycle_may_be_considered",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
}

BOUNDARY_FALSE_FIELDS = {
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
    "prior_result_reentry_cycle_created",
    "second_operation_created",
    "continuation_created",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
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
}

FAILURE_NON_CLAIM_FIELDS = {
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "runtime_v0_failure_repaired",
    "runtime_v0_failure_hidden",
    "runtime_v0_failure_claimed_passed",
    "runtime_v2_failure_repaired",
    "runtime_v2_failure_hidden",
    "runtime_v2_failure_claimed_passed",
    "runtime_boundary_v0_failure_repaired",
    "runtime_boundary_v0_failure_hidden",
    "runtime_boundary_v0_failure_claimed_passed",
}

TOP_LEVEL_EXACT_BLOCKS = [
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
    ("older_runtime_lineage_imported_as_authority", "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY"),
    ("older_runtime_permission_treated_as_current", "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT"),
    ("runtime_authority_imported", "RUNTIME_AUTHORITY_IMPORTED"),
    ("raw_state_body_embedded", "RAW_STATE_BODY_EMBEDDED"),
    ("state_mutation_performed", "STATE_MUTATION_PERFORMED"),
    ("state_update_performed", "STATE_UPDATE_PERFORMED"),
    ("prior_result_reentry_cycle_created", "PRIOR_RESULT_REENTRY_CYCLE_CREATED"),
    ("second_operation_created", "SECOND_OPERATION_CREATED"),
    ("continuation_created", "CONTINUATION_CREATED"),
    ("runtime_v0_failure_repaired", "RUNTIME_V0_FAILURE_REPAIRED"),
    ("runtime_v0_failure_hidden", "RUNTIME_V0_FAILURE_HIDDEN"),
    ("runtime_v0_failure_claimed_passed", "RUNTIME_V0_FAILURE_CLAIMED_PASSED"),
    ("runtime_v2_failure_repaired", "RUNTIME_V2_FAILURE_REPAIRED"),
    ("runtime_v2_failure_hidden", "RUNTIME_V2_FAILURE_HIDDEN"),
    ("runtime_v2_failure_claimed_passed", "RUNTIME_V2_FAILURE_CLAIMED_PASSED"),
    ("runtime_boundary_v0_failure_repaired", "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED"),
    ("runtime_boundary_v0_failure_hidden", "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN"),
    ("runtime_boundary_v0_failure_claimed_passed", "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED"),
]

HOSTILE_SENTINELS = [
    "RAW_PRIOR_RESULT_REENTRY_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_PRIOR_RESULT_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_STATE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_STATE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_STATE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
]

DEFAULT_ARTIFACT_PATHS = {
    "selected_runtime_held_reentry_artifact": REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_v0_min/local_relevance_medium_read_only_runtime_held_reentry_reference_review_001__local_relevance_medium_read_only_runtime_held_reentry_v0_min_result.json",
    "selected_runtime_held_reentry_boundary_artifact": REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min/local_relevance_medium_read_only_runtime_held_reentry_boundary_reference_review_001__local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min_result.json",
    "selected_runtime_held_state_artifact": REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_v0_min/local_relevance_medium_read_only_runtime_held_state_reference_review_001__local_relevance_medium_read_only_runtime_held_state_v0_min_result.json",
    "selected_runtime_held_state_boundary_artifact": REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min/local_relevance_medium_read_only_runtime_held_state_boundary_reference_review_001__local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result.json",
    "selected_runtime_artifact": REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v3/local_relevance_medium_read_only_runtime_reference_review_001__local_relevance_medium_read_only_runtime_v0_min_v3_result.json",
    "selected_runtime_boundary_artifact": REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min_v2/local_relevance_medium_read_only_runtime_boundary_reference_review_001__local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json",
    "selected_runtime_permission_artifact": REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min/local_relevance_medium_read_only_runtime_permission_reference_review_001__local_relevance_medium_read_only_runtime_permission_v0_min_result.json",
    "selected_operation_execution_artifact": REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min/local_relevance_medium_read_only_operation_execution_reference_review_001__local_relevance_medium_read_only_operation_execution_v0_min_result.json",
}

ARTIFACT_SPECS = [
    {
        "name": "runtime_held_reentry",
        "request_key": "selected_runtime_held_reentry_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry",
        "outcome": RUNTIME_HELD_REENTRY_OUTCOME,
        "filename": "runtime_held_reentry.json",
    },
    {
        "name": "runtime_held_reentry_boundary",
        "request_key": "selected_runtime_held_reentry_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry_boundary",
        "outcome": RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME,
        "filename": "runtime_held_reentry_boundary.json",
    },
    {
        "name": "runtime_held_state",
        "request_key": "selected_runtime_held_state_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_state",
        "outcome": RUNTIME_HELD_STATE_OUTCOME,
        "filename": "runtime_held_state.json",
    },
    {
        "name": "runtime_held_state_boundary",
        "request_key": "selected_runtime_held_state_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_state_boundary",
        "outcome": RUNTIME_HELD_STATE_BOUNDARY_OUTCOME,
        "filename": "runtime_held_state_boundary.json",
    },
    {
        "name": "runtime",
        "request_key": "selected_runtime_artifact",
        "object_key": "local_relevance_medium_read_only_runtime",
        "outcome": RUNTIME_OUTCOME,
        "filename": "runtime.json",
    },
    {
        "name": "runtime_boundary",
        "request_key": "selected_runtime_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_boundary",
        "outcome": RUNTIME_BOUNDARY_OUTCOME,
        "filename": "runtime_boundary.json",
    },
    {
        "name": "runtime_permission",
        "request_key": "selected_runtime_permission_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_permission",
        "outcome": RUNTIME_PERMISSION_OUTCOME,
        "filename": "runtime_permission.json",
    },
    {
        "name": "operation_execution",
        "request_key": "selected_operation_execution_artifact",
        "object_key": "local_relevance_medium_read_only_operation_execution",
        "outcome": OPERATION_EXECUTION_OUTCOME,
        "filename": "operation_execution.json",
    },
]


class LocalRelevanceMediumReadOnlyPriorResultReentryBoundaryV0MinV2Test(unittest.TestCase):
    """V2 executable membrane for one prior-result re-entry boundary object."""

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
        return f"{safe}.json"

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
        code = block.get("code") or block.get("block_code")
        return str(code) if code is not None else None

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get("local_relevance_medium_read_only_prior_result_reentry_boundary_checks")
        self.assertIsInstance(checks, list)
        return checks

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        summary = result.get("local_relevance_medium_read_only_prior_result_reentry_boundary_summary")
        if isinstance(summary, Mapping) and isinstance(summary.get("failed_check_count"), int):
            return int(summary["failed_check_count"])
        return sum(1 for check in self.checks(result) if not check.get("passed"))

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        summary = result.get("local_relevance_medium_read_only_prior_result_reentry_boundary_summary")
        if isinstance(summary, Mapping) and isinstance(summary.get("passed_check_count"), int):
            return int(summary["passed_check_count"])
        return sum(1 for check in self.checks(result) if check.get("passed"))

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        boundary = result.get("local_relevance_medium_read_only_prior_result_reentry_boundary")
        self.assertIsInstance(boundary, dict)
        return boundary

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get("local_relevance_medium_read_only_prior_result_reentry_boundary_statement")
        self.assertIsInstance(statement, dict)
        return statement

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get("local_relevance_medium_read_only_prior_result_reentry_boundary_summary")
        self.assertIsInstance(summary, dict)
        return summary

    def assert_same_or_stable_artifact_path(self, actual: Any, expected: Any) -> None:
        actual_path = Path(str(actual))
        expected_path = Path(str(expected))
        try:
            self.assertEqual(actual_path.resolve(), expected_path.resolve())
            return
        except (AssertionError, FileNotFoundError, OSError):
            pass
        self.assertTrue(
            str(actual_path).endswith(expected_path.name)
            or str(expected_path).endswith(actual_path.name),
            f"{actual_path!s} does not match stable artifact suffix {expected_path.name!s}",
        )

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        codes = set(resolver.BLOCK_CODES)
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, codes)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                emitted = check.get(key)
                if emitted is not None:
                    self.assertIn(emitted, codes)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(type(non_claims[key]), bool)
            self.assertIs(non_claims[key], False)

    def assert_prior_result_reentry_boundary_non_claims(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in BOUNDARY_FALSE_FIELDS:
            if key in boundary:
                self.assertIs(boundary[key], False, key)
        non_claims = result["non_claims"]
        for key in (
            "prior_result_reentry_cycle_created",
            "second_operation_created",
            "continuation_created",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "follow_on_work_authorized",
            *FAILURE_NON_CLAIM_FIELDS,
        ):
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_prior_result_reentry_boundary_non_claims(result)

    def assert_boundary_not_wrapper(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(key, boundary)

    def assert_boundary_posture(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_id"], "local_relevance_medium_read_only_prior_result_reentry_boundary_001")
        self.assertEqual(boundary["boundary_type"], BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.RESULT_VERSION)
        self.assertEqual(boundary["boundary_scope"], BOUNDARY_SCOPE)
        self.assertEqual(boundary["selected_command"], SELECTED_COMMAND)
        for key in BOUNDARY_TRUE_FIELDS:
            self.assertIs(boundary[key], True, key)
        for key in BOUNDARY_FALSE_FIELDS:
            self.assertIs(boundary[key], False, key)
        expected_basis = {
            "basis_runtime_held_reentry_outcome": RUNTIME_HELD_REENTRY_OUTCOME,
            "basis_runtime_held_reentry_boundary_outcome": RUNTIME_HELD_REENTRY_BOUNDARY_OUTCOME,
            "basis_runtime_held_state_outcome": RUNTIME_HELD_STATE_OUTCOME,
            "basis_runtime_held_state_boundary_outcome": RUNTIME_HELD_STATE_BOUNDARY_OUTCOME,
            "basis_runtime_outcome": RUNTIME_OUTCOME,
            "basis_runtime_boundary_outcome": RUNTIME_BOUNDARY_OUTCOME,
            "basis_runtime_permission_outcome": RUNTIME_PERMISSION_OUTCOME,
            "basis_operation_execution_outcome": OPERATION_EXECUTION_OUTCOME,
        }
        for key, value in expected_basis.items():
            self.assertEqual(boundary[key], value)
            stem = key.removesuffix("_outcome")
            self.assertEqual(boundary[f"{stem}_result_version"], resolver.RESULT_VERSION)
            self.assertEqual(boundary[f"{stem}_failed_check_count"], 0)

    def assert_recorded_statement(self, result: Mapping[str, Any]) -> None:
        statement = self.statement(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)

    def assert_failure_lineage_preserved(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        summary = self.summary(result)
        statement = self.statement(result)
        for key in (
            "runtime_v0_failure_evidence_preserved",
            "runtime_v2_failure_evidence_preserved",
            "runtime_boundary_v0_failure_evidence_preserved",
        ):
            self.assertIs(boundary[key], True, key)
            self.assertIs(statement[key], True, key)
            if key in summary:
                self.assertIs(summary[key], True, key)
        non_claims = result["non_claims"]
        for key in FAILURE_NON_CLAIM_FIELDS:
            self.assertIs(non_claims[key], False, key)

    def assert_no_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def clean_artifact_posture(self) -> dict[str, Any]:
        posture: dict[str, Any] = {
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
        }
        posture.update({key: True for key in BOUNDARY_TRUE_FIELDS})
        posture.update({key: False for key in BOUNDARY_FALSE_FIELDS})
        posture.update({key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS})
        posture.update(
            {
                "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded": False,
                "consumed_request_token_remains_closed": True,
                "authorization_token_reuse_blocked": True,
                "predecessor_failure_evidence_preserved": True,
                "result_level_non_claims_canonical_false": True,
            }
        )
        return posture

    def synthetic_artifact(self, spec: Mapping[str, Any]) -> dict[str, Any]:
        posture = self.clean_artifact_posture()
        name = str(spec["name"])
        object_key = str(spec["object_key"])
        if name.endswith("_boundary"):
            posture["boundary_type"] = f"LOCAL_RELEVANCE_MEDIUM_READ_ONLY_{name.upper()}"
            posture["boundary_scope"] = f"SELECTED_{name.upper()}_CONSIDERATION_ONLY"
        elif name == "runtime":
            posture["runtime_type"] = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME"
            posture["runtime_scope"] = "SELECTED_RUNTIME_ONLY"
        elif name == "runtime_permission":
            posture["runtime_permission_type"] = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION"
            posture["runtime_permission_scope"] = "SELECTED_RUNTIME_PERMISSION_ONLY"
        elif name == "operation_execution":
            posture["operation_execution_type"] = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION"
            posture["operation_execution_scope"] = "SELECTED_OPERATION_EXECUTION_ONLY"
        elif name == "runtime_held_state":
            posture["held_state_type"] = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE"
            posture["held_state_scope"] = "SELECTED_RUNTIME_HELD_STATE_ONLY"
        else:
            posture["held_reentry_type"] = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY"
            posture["held_reentry_scope"] = "SELECTED_RUNTIME_HELD_REENTRY_ONLY"
        return {
            "outcome": spec["outcome"],
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
            object_key: copy.deepcopy(posture),
            f"{object_key}_statement": copy.deepcopy(posture),
            f"{object_key}_summary": copy.deepcopy(posture),
            "non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
        }

    def write_json(self, path: Path, value: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")
        return path

    def write_synthetic_artifacts(
        self,
        root: Path,
        artifact_mutator: Callable[[str, dict[str, Any]], None] | None = None,
        include_sentinels: bool = False,
    ) -> tuple[dict[str, str], dict[str, dict[str, Any]]]:
        paths: dict[str, str] = {}
        artifacts: dict[str, dict[str, Any]] = {}
        for index, spec in enumerate(ARTIFACT_SPECS, 1):
            artifact = self.synthetic_artifact(spec)
            if include_sentinels:
                object_key = str(spec["object_key"])
                artifact[object_key]["raw_body"] = HOSTILE_SENTINELS[index % len(HOSTILE_SENTINELS)]
                artifact[object_key]["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
                artifact["raw_full_body"] = "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN"
            if artifact_mutator is not None:
                artifact_mutator(str(spec["name"]), artifact)
            filename = self.safe_json_filename(str(spec["filename"]), index=index)
            path = root / filename
            self.write_json(path, artifact)
            paths[str(spec["request_key"])] = str(path)
            artifacts[str(spec["name"])] = artifact
        return paths, artifacts

    def build_clean_request(self, paths: Mapping[str, Any]) -> dict[str, Any]:
        request = resolver.build_declared_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_request(
            selected_runtime_held_reentry_artifact=paths["selected_runtime_held_reentry_artifact"],
            selected_runtime_held_reentry_boundary_artifact=paths[
                "selected_runtime_held_reentry_boundary_artifact"
            ],
            selected_runtime_held_state_artifact=paths["selected_runtime_held_state_artifact"],
            selected_runtime_held_state_boundary_artifact=paths[
                "selected_runtime_held_state_boundary_artifact"
            ],
            selected_runtime_artifact=paths["selected_runtime_artifact"],
            selected_runtime_boundary_artifact=paths["selected_runtime_boundary_artifact"],
            selected_runtime_permission_artifact=paths["selected_runtime_permission_artifact"],
            selected_operation_execution_artifact=paths["selected_operation_execution_artifact"],
        )
        request.update({key: True for key in BOUNDARY_TRUE_FIELDS})
        request["boundary_type"] = BOUNDARY_TYPE
        request["boundary_scope"] = BOUNDARY_SCOPE
        request["selected_command"] = SELECTED_COMMAND
        return request

    def build_clean_synthetic_request(
        self, root: Path
    ) -> tuple[dict[str, Any], dict[str, dict[str, Any]], dict[str, str]]:
        paths, artifacts = self.write_synthetic_artifacts(root)
        request = self.build_clean_request(paths)
        return request, artifacts, paths

    def resolve_clean_synthetic(self, root: Path) -> dict[str, Any]:
        request, _, _ = self.build_clean_synthetic_request(root)
        return resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(request)

    def assert_clean_recorded_result(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        summary = self.summary(result)
        self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)
        self.assert_boundary_posture(result)
        self.assert_boundary_not_wrapper(result)
        self.assert_recorded_statement(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_failure_lineage_preserved(result)

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_request",
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
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min"
            )
        )
        self.assertIn(BOUNDARY_TYPE, resolver.SUPPORTED_BOUNDARY_TYPE_VALUES)
        self.assertIn(BOUNDARY_SCOPE, resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, SELECTED_COMMAND)
        for key in (
            "prior_result_reentry_cycle_created",
            "second_operation_created",
            "continuation_created",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "runtime_v0_failure_repaired",
            "runtime_v2_failure_repaired",
            "runtime_boundary_v0_failure_repaired",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for code in (
            "PRIOR_RESULT_REENTRY_CYCLE_CREATED",
            "SECOND_OPERATION_CREATED",
            "CONTINUATION_CREATED",
            "RAW_STATE_BODY_EMBEDDED",
            "STATE_MUTATION_PERFORMED",
            "STATE_UPDATE_PERFORMED",
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            "RUNTIME_AUTHORITY_IMPORTED",
            "RUNTIME_V0_FAILURE_REPAIRED",
            "RUNTIME_V2_FAILURE_REPAIRED",
            "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        self.assertTrue(EXPECTED_OUTCOME_FAMILY.issubset(set(resolver.OUTCOME_FAMILY)))

        request = resolver.build_declared_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_request()
        for key, path in DEFAULT_ARTIFACT_PATHS.items():
            self.assertTrue(str(request[key]).endswith(path.name), key)
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        self.assertEqual(request["boundary_type"], BOUNDARY_TYPE)
        self.assertEqual(request["boundary_scope"], BOUNDARY_SCOPE)
        for key in (
            "prior_result_reentry_cycle_created",
            "second_operation_created",
            "continuation_created",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "consumed_request_reopened",
            "authorization_token_reused",
            "older_runtime_lineage_imported_as_authority",
            "older_runtime_permission_treated_as_current",
            "runtime_authority_imported",
            "runtime_v0_failure_repaired",
            "runtime_v0_failure_hidden",
            "runtime_v0_failure_claimed_passed",
            "runtime_v2_failure_repaired",
            "runtime_v2_failure_hidden",
            "runtime_v2_failure_claimed_passed",
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
        ):
            self.assertIn(key, request["declared_non_claims"])
            self.assertIs(request["declared_non_claims"][key], False)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, paths = self.build_clean_synthetic_request(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(request)
        self.assert_clean_recorded_result(result)
        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_id"], request["local_relevance_medium_read_only_prior_result_reentry_boundary_id"])
        for spec in ARTIFACT_SPECS:
            basis_key = f"basis_{spec['name']}_artifact"
            if basis_key not in boundary and spec["name"] == "runtime_held_reentry_boundary":
                basis_key = "basis_runtime_held_reentry_boundary_artifact"
            self.assert_same_or_stable_artifact_path(boundary[basis_key], paths[str(spec["request_key"])])

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        missing = [path for path in DEFAULT_ARTIFACT_PATHS.values() if not Path(path).exists()]
        if missing:
            self.skipTest("default live artifacts are not all present")
        request = resolver.build_declared_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_request()
        request.update({key: True for key in BOUNDARY_TRUE_FIELDS})
        result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(request)
        if result["outcome"] != resolver.OUTCOME_RECORDED:
            self.skipTest("default live artifacts are present but not clean for this resolver")
        self.assert_clean_recorded_result(result)
        boundary = self.boundary(result)
        for spec in ARTIFACT_SPECS:
            key = str(spec["request_key"])
            boundary_key = f"basis_{spec['name']}_artifact"
            self.assert_same_or_stable_artifact_path(boundary[boundary_key], DEFAULT_ARTIFACT_PATHS[key])

    def test_closure_older_runtime_raw_state_cycle_and_lineage_top_level_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _ = self.build_clean_synthetic_request(Path(tmp))
            for key, expected_code in TOP_LEVEL_EXACT_BLOCKS:
                with self.subTest(key=key):
                    candidate = copy.deepcopy(request)
                    candidate[key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assertIs(result["non_claims"][key], False)

    def test_declared_non_claim_malformed_flipped_missing_cases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _ = self.build_clean_synthetic_request(Path(tmp))
            keys = [key for key, _ in TOP_LEVEL_EXACT_BLOCKS]
            for key in keys:
                for mode in ("flipped", "missing", "non_bool"):
                    with self.subTest(key=key, mode=mode):
                        candidate = copy.deepcopy(request)
                        if mode == "flipped":
                            candidate["declared_non_claims"][key] = True
                        elif mode == "missing":
                            candidate["declared_non_claims"].pop(key, None)
                        else:
                            candidate["declared_non_claims"][key] = "false"
                        result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(candidate)
                        self.assert_blocked_with_public_code(result)
                        self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_critical_canonicalization_for_all_required_false_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _ = self.build_clean_synthetic_request(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    candidate = copy.deepcopy(request)
                    candidate["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)

    def test_representative_blocking_behavior(self) -> None:
        block_cases: list[tuple[str, Callable[[dict[str, Any], Path], Any]]] = [
            ("explicit block intent", lambda req, root: req.update({"local_relevance_medium_read_only_prior_result_reentry_boundary_intent": "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY"})),
            ("missing request", lambda req, root: {}),
            ("non mapping request", lambda req, root: ["not", "mapping"]),
            ("unsupported intent", lambda req, root: req.update({"local_relevance_medium_read_only_prior_result_reentry_boundary_intent": "UNSUPPORTED"})),
            ("selected command missing", lambda req, root: req.pop("selected_command", None)),
            ("selected command not state", lambda req, root: req.update({"selected_command": "status"})),
            ("boundary type missing", lambda req, root: req.pop("boundary_type", None)),
            ("boundary type wrong", lambda req, root: req.update({"boundary_type": "REGISTRY"})),
            ("boundary scope missing", lambda req, root: req.pop("boundary_scope", None)),
            ("boundary scope wrong", lambda req, root: req.update({"boundary_scope": "SEARCH_VIEW"})),
            ("required non claim missing", lambda req, root: req["declared_non_claims"].pop("prior_result_reentry_cycle_created", None)),
        ]
        for spec in ARTIFACT_SPECS:
            request_key = str(spec["request_key"])
            name = str(spec["name"])
            block_cases.extend(
                [
                    (f"{name} path missing", lambda req, root, key=request_key: req.pop(key, None)),
                    (f"{name} unreadable", lambda req, root, key=request_key: req.update({key: str(root / "missing.json")})),
                    (
                        f"{name} array",
                        lambda req, root, key=request_key, n=name: req.update(
                            {key: str(self.write_json(root / self.safe_json_filename(f"{n} array"), []))}
                        ),
                    ),
                    (
                        f"{name} not recorded",
                        lambda req, root, key=request_key, n=name: self.replace_artifact_for_request(
                            req, root, key, n, {"outcome": "NOT_RECORDED"}
                        ),
                    ),
                    (
                        f"{name} failed checks",
                        lambda req, root, key=request_key, n=name: self.replace_artifact_for_request(
                            req, root, key, n, {"failed_check_count": 1}
                        ),
                    ),
                    (
                        f"{name} version wrong",
                        lambda req, root, key=request_key, n=name: self.replace_artifact_for_request(
                            req, root, key, n, {"result_version": "9.9.9"}
                        ),
                    ),
                ]
            )
        for field in (
            "selected_runtime_held_reentry_not_recorded",
            "runtime_held_reentry_not_created",
            "runtime_held_reentry_local_only_not_true",
            "runtime_held_reentry_read_only_not_true",
            "held_reentry_basis_reference_only_not_true",
            "selected_runtime_held_reentry_boundary_not_recorded",
            "future_runtime_held_reentry_may_not_be_considered",
            "selected_runtime_held_state_not_recorded",
            "runtime_held_state_not_created",
            "runtime_held_state_local_only_not_true",
            "runtime_held_state_read_only_not_true",
            "held_state_basis_reference_only_not_true",
            "raw_state_body_embedded",
            "state_mutation_performed",
            "state_update_performed",
            "selected_runtime_held_state_boundary_not_recorded",
            "future_runtime_held_state_may_not_be_considered",
            "selected_runtime_not_recorded",
            "runtime_not_created",
            "runtime_local_only_not_true",
            "runtime_read_only_not_true",
            "selected_runtime_boundary_not_recorded",
            "future_runtime_may_not_be_considered",
            "selected_runtime_permission_not_recorded",
            "runtime_permission_not_created",
            "runtime_permission_local_only_not_true",
            "runtime_permission_read_only_not_true",
            "selected_operation_execution_not_recorded",
            "operation_execution_not_created",
            "operation_execution_not_performed",
            "operation_execution_local_only_not_true",
            "operation_execution_read_only_not_true",
            "future_prior_result_reentry_cycle_may_not_be_considered",
            "prior_result_reentry_cycle_created",
            "second_operation_created",
            "continuation_created",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
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
            "runtime_v0_failure_repaired",
            "runtime_v0_failure_hidden",
            "runtime_v0_failure_claimed_passed",
            "runtime_v2_failure_repaired",
            "runtime_v2_failure_hidden",
            "runtime_v2_failure_claimed_passed",
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
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
            "artifact_existence_treated_as_prior_result_reentry_boundary_authority",
            "latest_file_posture_treated_as_prior_result_reentry_boundary_authority",
            "repo_local_availability_treated_as_prior_result_reentry_boundary_authority",
            "hidden_repo_state_used_as_prior_result_reentry_boundary_content",
            "hidden_repo_state_used_as_prior_result_reentry_boundary_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            block_cases.append((field, lambda req, root, f=field: req.update({f: True})))

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for index, (name, mutate) in enumerate(block_cases, 1):
                with self.subTest(name=name):
                    case_root = root / self.safe_json_filename(name, index=index).removesuffix(".json")
                    request, _, _ = self.build_clean_synthetic_request(case_root)
                    maybe_request = mutate(request, case_root)
                    candidate = maybe_request if maybe_request is not None else request
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)

    def replace_artifact_for_request(
        self, request: dict[str, Any], root: Path, request_key: str, artifact_name: str, updates: Mapping[str, Any]
    ) -> None:
        spec = next(item for item in ARTIFACT_SPECS if item["name"] == artifact_name)
        artifact = self.synthetic_artifact(spec)
        artifact.update(updates)
        path = root / self.safe_json_filename(f"{artifact_name}_{next(iter(updates))}")
        self.write_json(path, artifact)
        request[request_key] = str(path)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = self.resolve_clean_synthetic(Path(tmp))
        self.assert_clean_recorded_result(result)
        serialized = json.dumps(result, sort_keys=True)
        for value in (
            resolver.OUTCOME_RECORDED,
            BOUNDARY_TYPE,
            BOUNDARY_SCOPE,
            SELECTED_COMMAND,
            resolver.RESOLVER_MODULE,
        ):
            self.assertIn(value, serialized)
        self.assertNotIn("[REDACTED]", serialized)
        self.assertTrue(EXPECTED_OUTCOME_FAMILY.issubset(set(resolver.OUTCOME_FAMILY)))

    def test_raw_hidden_older_runtime_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths, artifacts = self.write_synthetic_artifacts(root, include_sentinels=True)
            request = self.build_clean_request(paths)
            original_request = copy.deepcopy(request)
            original_artifacts = copy.deepcopy(artifacts)
            request["raw_prior_result_reentry_boundary_body"] = "RAW_PRIOR_RESULT_REENTRY_BOUNDARY_BODY_MUST_NOT_RETURN"
            request["raw_runtime_hosting_body"] = "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN"
            request["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_sentinels(result)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn(BOUNDARY_TYPE, serialized)
        self.assertIn(BOUNDARY_SCOPE, serialized)
        self.assertIn(SELECTED_COMMAND, serialized)
        self.assert_canonical_false_non_claims(result)
        self.assert_prior_result_reentry_boundary_non_claims(result)
        self.assertEqual(original_request["selected_command"], SELECTED_COMMAND)
        self.assertEqual(original_artifacts, artifacts)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request, _, _ = self.build_clean_synthetic_request(root / "basis")
            request_path = self.write_json(root / "request.json", request)
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_from_path(request_path)
            self.assert_clean_recorded_result(result)

            malformed = root / "malformed.json"
            malformed.write_text("{not json", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_from_path(malformed)
            self.assert_blocked_with_public_code(malformed_result)

            array_path = self.write_json(root / "array.json", [])
            array_result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_from_path(array_path)
            self.assert_blocked_with_public_code(array_result)

            missing_result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_from_path(root / "missing.json")
            self.assert_blocked_with_public_code(missing_result)

            output_root = root / "artifacts" / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_result(result)
                second = resolver.write_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_result(result)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertTrue(first.parent.exists())
            self.assertEqual(first.parent, output_root)
            self.assertIn("local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min", str(first.parent))
            parsed_first = json.loads(first.read_text(encoding="utf-8"))
            parsed_second = json.loads(second.read_text(encoding="utf-8"))
            self.assertEqual(parsed_first["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(parsed_second["outcome"], resolver.OUTCOME_RECORDED)
            self.assertTrue(second.stem.startswith(first.stem))
            forbidden_exact_roots = {
                Path("integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_v0_min"),
                Path("integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min"),
                Path("integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_v0_min"),
                Path("integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min"),
                Path("integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v3"),
                Path("integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v2"),
                Path("integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min"),
                Path("integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min_v2"),
                Path("integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min"),
                Path("integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min"),
                Path("integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min"),
                Path("source-transfer"),
                Path("source-receipt"),
                Path("public-api"),
                Path("participant-facing-interface"),
                Path("distributed-network"),
            }
            self.assertNotIn(first.parent.name, {path.name for path in forbidden_exact_roots})

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, artifacts, paths = self.build_clean_synthetic_request(Path(tmp))
            request["raw_runtime_loop_body"] = "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN"
            original_request = copy.deepcopy(request)
            original_artifacts = copy.deepcopy(artifacts)
            original_paths = copy.deepcopy(paths)
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertEqual(request, original_request)
        self.assertEqual(artifacts, original_artifacts)
        self.assertEqual(paths, original_paths)

    def test_failure_lineage_and_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _ = self.build_clean_synthetic_request(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(request)
            self.assert_clean_recorded_result(result)
            summary = self.summary(result)
            self.assertIs(summary.get("predecessor_failure_evidence_preserved"), True)
            self.assertIs(summary.get("result_level_non_claims_canonical_false"), True)
            self.assertIs(summary.get("consumed_request_token_remains_closed"), True)
            self.assertIs(summary.get("authorization_token_reuse_blocked"), True)
            self.assertIs(summary.get("older_runtime_lineage_not_imported_as_authority"), True)
            self.assertIs(summary.get("older_runtime_permission_not_treated_as_current"), True)
            self.assertIs(summary.get("runtime_authority_not_imported"), True)
            self.assertIs(summary.get("raw_state_body_not_embedded"), True)
            self.assertIs(summary.get("state_mutation_not_performed"), True)
            self.assertIs(summary.get("state_update_not_performed"), True)
            self.assertIs(summary.get("prior_result_reentry_cycle_not_created"), True)
            self.assertIs(summary.get("second_operation_not_created"), True)
            self.assertIs(summary.get("continuation_not_created"), True)

            for key, expected_code in TOP_LEVEL_EXACT_BLOCKS:
                if not key.startswith("runtime_"):
                    continue
                with self.subTest(key=key):
                    candidate = copy.deepcopy(request)
                    candidate[key] = True
                    blocked = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(blocked)
                    self.assertEqual(self.block_code(blocked), expected_code)


if __name__ == "__main__":
    unittest.main()
