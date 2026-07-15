"""Tests for the local read-only runtime-held-state boundary resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY object. It
verifies that the resolver reads one clean selected runtime v3 artifact, one
clean selected runtime boundary v2 artifact, one clean selected runtime
permission artifact, and one clean selected operation execution artifact, then
records one local read-only selected-state runtime-held-state boundary object
only.

The boundary remains selected-state-runtime-held-state-consideration-only. It
does not create runtime-held state, runtime hosting, runtime loop, daemon
behavior, continuation, runtime-held re-entry, second operation, prior-result
re-entry cycle, public API, participant-facing interface, distributed behavior,
general permission, arbitrary permission, registry, search, ranking, older
runtime authority import, or follow-on work.
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

import resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min as resolver  # noqa: E402


BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_RUNTIME_HELD_STATE_CONSIDERATION_ONLY"
SELECTED_COMMAND = "state"
RUNTIME_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED"
RUNTIME_BOUNDARY_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED"
)
RUNTIME_PERMISSION_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED"
)
OPERATION_EXECUTION_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED"
)

DEFAULT_RUNTIME_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_v0_min_v3/"
    "local_relevance_medium_read_only_runtime_reference_review_001__"
    "local_relevance_medium_read_only_runtime_v0_min_v3_result.json"
)
DEFAULT_RUNTIME_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_boundary_v0_min_v2/"
    "local_relevance_medium_read_only_runtime_boundary_reference_review_001__"
    "local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
)
DEFAULT_RUNTIME_PERMISSION_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "runtime_permission_v0_min/"
    "local_relevance_medium_read_only_runtime_permission_reference_review_001__"
    "local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
)
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
    "runtime_held_state_boundary_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_v0_min_v3"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_v0_min_v2"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_boundary_v0_min_v2"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_permission_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "operation_execution_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"
    ),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_runtime_held_state_boundary_metadata",
    "declared_local_relevance_medium_read_only_runtime_held_state_boundary_question",
    "selected_runtime_artifact_basis",
    "selected_runtime_boundary_artifact_basis",
    "selected_runtime_permission_artifact_basis",
    "selected_operation_execution_artifact_basis",
    "local_relevance_medium_read_only_runtime_held_state_boundary",
    "local_relevance_medium_read_only_runtime_held_state_boundary_checks",
    "local_relevance_medium_read_only_runtime_held_state_boundary_statement",
    "local_relevance_medium_read_only_runtime_held_state_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_held_state_boundary_summary",
)

FORBIDDEN_BOUNDARY_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_runtime_held_state_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_runtime_held_state_boundary_summary",
    "local_relevance_medium_read_only_runtime_held_state_boundary_metadata",
)

BOUNDARY_FALSE_FIELDS = (
    "runtime_held_state_created",
    "runtime_hosting_created",
    "runtime_loop_created",
    "daemon_behavior_created",
    "continuation_created",
    "runtime_held_reentry_created",
    "second_operation_created",
    "prior_result_reentry_cycle_created",
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
    "artifact_existence_treated_as_runtime_held_state_boundary_authority",
    "latest_file_posture_treated_as_runtime_held_state_boundary_authority",
    "repo_local_availability_treated_as_runtime_held_state_boundary_authority",
    "hidden_repo_state_used_as_runtime_held_state_boundary_content",
    "hidden_repo_state_used_as_runtime_held_state_boundary_authority",
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
)

STATEMENT_TRUE_FIELDS = (
    "local_relevance_medium_read_only_runtime_held_state_boundary_recorded",
    "basis_runtime_artifact_preserved",
    "basis_runtime_boundary_artifact_preserved",
    "basis_runtime_permission_artifact_preserved",
    "basis_operation_execution_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
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
    "future_runtime_held_state_may_be_considered",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_RUNTIME_HELD_STATE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_STATE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_OPERATION_EXECUTION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HELD_REENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "RAW_PRIOR_RESULT_REENTRY_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

LINEAGE_TOP_LEVEL_CODES = (
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
    (
        "older_runtime_lineage_imported_as_authority",
        "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
    ),
    (
        "older_runtime_permission_treated_as_current",
        "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
    ),
    ("runtime_authority_imported", "RUNTIME_AUTHORITY_IMPORTED"),
    ("runtime_v0_failure_repaired", "RUNTIME_V0_FAILURE_REPAIRED"),
    ("runtime_v0_failure_hidden", "RUNTIME_V0_FAILURE_HIDDEN"),
    ("runtime_v0_failure_claimed_passed", "RUNTIME_V0_FAILURE_CLAIMED_PASSED"),
    ("runtime_v2_failure_repaired", "RUNTIME_V2_FAILURE_REPAIRED"),
    ("runtime_v2_failure_hidden", "RUNTIME_V2_FAILURE_HIDDEN"),
    ("runtime_v2_failure_claimed_passed", "RUNTIME_V2_FAILURE_CLAIMED_PASSED"),
    ("runtime_boundary_v0_failure_repaired", "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED"),
    ("runtime_boundary_v0_failure_hidden", "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN"),
    (
        "runtime_boundary_v0_failure_claimed_passed",
        "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
    ),
)


class LocalRelevanceMediumReadOnlyRuntimeHeldStateBoundaryTests(unittest.TestCase):
    """Executable membrane for the runtime-held-state boundary resolver."""

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

    def write_json(self, path: Path, value: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get(
            "local_relevance_medium_read_only_runtime_held_state_boundary_checks", []
        )
        self.assertIsInstance(checks, list)
        return checks

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        boundary = result.get("local_relevance_medium_read_only_runtime_held_state_boundary")
        self.assertIsInstance(boundary, Mapping)
        return boundary

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get(
            "local_relevance_medium_read_only_runtime_held_state_boundary_statement"
        )
        self.assertIsInstance(statement, Mapping)
        return statement

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get(
            "local_relevance_medium_read_only_runtime_held_state_boundary_summary"
        )
        self.assertIsInstance(summary, Mapping)
        return summary

    def non_claims(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        return non_claims

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if isinstance(block, Mapping):
            return block.get("code") or block.get("block_code")
        return None

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

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

    def assert_boundary_object_not_wrapper(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for field in FORBIDDEN_BOUNDARY_WRAPPER_FIELDS:
            self.assertNotIn(field, boundary)

    def assert_runtime_held_state_boundary_non_claims(
        self, result: Mapping[str, Any]
    ) -> None:
        boundary = self.boundary(result)
        for field in BOUNDARY_FALSE_FIELDS:
            self.assertIn(field, boundary)
            self.assertIs(boundary[field], False)
        non_claims = self.non_claims(result)
        for field in BOUNDARY_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS:
            self.assertIn(field, non_claims)
            self.assertIs(non_claims[field], False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_runtime_held_state_boundary_non_claims(result)

    def assert_lineage_preserved(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        statement = self.statement(result)
        summary = self.summary(result)
        non_claims = self.non_claims(result)

        self.assertIs(boundary["runtime_v0_failure_evidence_preserved"], True)
        self.assertIs(boundary["runtime_v2_failure_evidence_preserved"], True)
        self.assertIs(boundary["runtime_boundary_v0_failure_evidence_preserved"], True)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)
        for key in (
            "runtime_v0_failure_repaired",
            "runtime_v0_failure_hidden",
            "runtime_v0_failure_claimed_passed",
            "runtime_v2_failure_repaired",
            "runtime_v2_failure_hidden",
            "runtime_v2_failure_claimed_passed",
            "runtime_boundary_v0_failure_repaired",
            "runtime_boundary_v0_failure_hidden",
            "runtime_boundary_v0_failure_claimed_passed",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertIs(non_claims[key], False)

    def assert_no_sentinels(self, value: Any) -> None:
        serialized = json.dumps(value, ensure_ascii=False, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_recorded_boundary(
        self, result: Mapping[str, Any], expected_paths: Mapping[str, Path] | None = None
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertEqual(self.summary(result)["result_version"], "0.1.0")
        self.assertEqual(
            self.summary(result)["resolver_module"],
            "resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min",
        )
        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        boundary = self.boundary(result)
        self.assertEqual(
            boundary["boundary_id"],
            "local_relevance_medium_read_only_runtime_held_state_boundary_001",
        )
        self.assertEqual(boundary["boundary_type"], BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], "0.1.0")
        self.assertEqual(boundary["boundary_scope"], BOUNDARY_SCOPE)
        self.assertEqual(boundary["basis_runtime_outcome"], RUNTIME_OUTCOME)
        self.assertEqual(boundary["basis_runtime_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_runtime_failed_check_count"], 0)
        self.assertEqual(
            boundary["basis_runtime_boundary_outcome"], RUNTIME_BOUNDARY_OUTCOME
        )
        self.assertEqual(boundary["basis_runtime_boundary_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_runtime_boundary_failed_check_count"], 0)
        self.assertEqual(
            boundary["basis_runtime_permission_outcome"], RUNTIME_PERMISSION_OUTCOME
        )
        self.assertEqual(boundary["basis_runtime_permission_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_runtime_permission_failed_check_count"], 0)
        self.assertEqual(
            boundary["basis_operation_execution_outcome"], OPERATION_EXECUTION_OUTCOME
        )
        self.assertEqual(boundary["basis_operation_execution_result_version"], "0.1.0")
        self.assertEqual(boundary["basis_operation_execution_failed_check_count"], 0)

        if expected_paths is not None:
            self.assert_same_or_stable_artifact_path(
                boundary["basis_runtime_artifact"], expected_paths["runtime"]
            )
            self.assert_same_or_stable_artifact_path(
                boundary["basis_runtime_boundary_artifact"],
                expected_paths["runtime_boundary"],
            )
            self.assert_same_or_stable_artifact_path(
                boundary["basis_runtime_permission_artifact"],
                expected_paths["runtime_permission"],
            )
            self.assert_same_or_stable_artifact_path(
                boundary["basis_operation_execution_artifact"],
                expected_paths["operation_execution"],
            )

        self.assertEqual(boundary["selected_command"], SELECTED_COMMAND)
        self.assertIs(boundary["selected_command_is_state"], True)
        for field in (
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
            "future_runtime_held_state_may_be_considered",
        ):
            self.assertIs(boundary[field], True)

        self.assert_runtime_held_state_boundary_non_claims(result)
        self.assert_boundary_object_not_wrapper(result)

        statement = self.statement(result)
        for field in STATEMENT_TRUE_FIELDS:
            self.assertIn(field, statement)
            self.assertIs(statement[field], True)

        self.assert_canonical_false_non_claims(result)
        self.assert_lineage_preserved(result)

    def synthetic_runtime_artifact(self) -> dict[str, Any]:
        runtime = {
            "runtime_id": "local_relevance_medium_read_only_runtime_001",
            "runtime_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME",
            "runtime_scope": "SELECTED_RUNTIME_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_runtime_recorded": True,
            "selected_runtime_recorded": True,
            "runtime_created": True,
            "runtime_local_only": True,
            "runtime_read_only": True,
            "selected_runtime_boundary_recorded": True,
            "future_runtime_may_be_considered": True,
            "selected_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "runtime_v0_failure_evidence_preserved": True,
            "runtime_v2_failure_evidence_preserved": True,
            "runtime_boundary_v0_failure_evidence_preserved": True,
        }
        for field in BOUNDARY_FALSE_FIELDS:
            runtime[field] = False
        return self.layered_artifact(
            outcome=RUNTIME_OUTCOME,
            metadata_key="local_relevance_medium_read_only_runtime_metadata",
            object_key="local_relevance_medium_read_only_runtime",
            statement_key="local_relevance_medium_read_only_runtime_statement",
            summary_key="local_relevance_medium_read_only_runtime_summary",
            object_value=runtime,
        )

    def synthetic_runtime_boundary_artifact(self) -> dict[str, Any]:
        boundary = {
            "boundary_id": "local_relevance_medium_read_only_runtime_boundary_001",
            "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
            "boundary_scope": "SELECTED_RUNTIME_CONSIDERATION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_runtime_boundary_recorded": True,
            "selected_runtime_boundary_recorded": True,
            "future_runtime_may_be_considered": True,
            "selected_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "runtime_created": False,
            "runtime_boundary_v0_failure_evidence_preserved": True,
        }
        for field in BOUNDARY_FALSE_FIELDS:
            boundary[field] = False
        return self.layered_artifact(
            outcome=RUNTIME_BOUNDARY_OUTCOME,
            metadata_key="local_relevance_medium_read_only_runtime_boundary_metadata",
            object_key="local_relevance_medium_read_only_runtime_boundary",
            statement_key="local_relevance_medium_read_only_runtime_boundary_statement",
            summary_key="local_relevance_medium_read_only_runtime_boundary_summary",
            object_value=boundary,
        )

    def synthetic_runtime_permission_artifact(self) -> dict[str, Any]:
        permission = {
            "runtime_permission_id": "local_relevance_medium_read_only_runtime_permission_001",
            "runtime_permission_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
            "runtime_permission_scope": "SELECTED_RUNTIME_PERMISSION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_runtime_permission_recorded": True,
            "selected_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "runtime_created": False,
        }
        for field in BOUNDARY_FALSE_FIELDS:
            permission[field] = False
        return self.layered_artifact(
            outcome=RUNTIME_PERMISSION_OUTCOME,
            metadata_key="local_relevance_medium_read_only_runtime_permission_metadata",
            object_key="local_relevance_medium_read_only_runtime_permission",
            statement_key="local_relevance_medium_read_only_runtime_permission_statement",
            summary_key="local_relevance_medium_read_only_runtime_permission_summary",
            object_value=permission,
        )

    def synthetic_operation_execution_artifact(self) -> dict[str, Any]:
        execution = {
            "operation_execution_id": "local_relevance_medium_read_only_operation_execution_001",
            "operation_execution_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
            "operation_execution_scope": "SELECTED_OPERATION_EXECUTION_ONLY",
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "selected_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
            "runtime_created": False,
        }
        for field in BOUNDARY_FALSE_FIELDS:
            execution[field] = False
        return self.layered_artifact(
            outcome=OPERATION_EXECUTION_OUTCOME,
            metadata_key="local_relevance_medium_read_only_operation_execution_metadata",
            object_key="local_relevance_medium_read_only_operation_execution",
            statement_key="local_relevance_medium_read_only_operation_execution_statement",
            summary_key="local_relevance_medium_read_only_operation_execution_summary",
            object_value=execution,
        )

    def layered_artifact(
        self,
        *,
        outcome: str,
        metadata_key: str,
        object_key: str,
        statement_key: str,
        summary_key: str,
        object_value: Mapping[str, Any],
    ) -> dict[str, Any]:
        statement = copy.deepcopy(dict(object_value))
        summary = copy.deepcopy(dict(object_value))
        summary["result_version"] = "0.1.0"
        summary["failed_check_count"] = 0
        return {
            "outcome": outcome,
            "result_version": "0.1.0",
            "failed_check_count": 0,
            metadata_key: {
                "result_version": "0.1.0",
                "resolver_module": "synthetic_clean_basis",
            },
            object_key: copy.deepcopy(dict(object_value)),
            statement_key: statement,
            summary_key: summary,
        }

    def synthetic_artifacts(self) -> dict[str, dict[str, Any]]:
        return {
            "runtime": self.synthetic_runtime_artifact(),
            "runtime_boundary": self.synthetic_runtime_boundary_artifact(),
            "runtime_permission": self.synthetic_runtime_permission_artifact(),
            "operation_execution": self.synthetic_operation_execution_artifact(),
        }

    def write_synthetic_basis(
        self, root: Path, artifacts: Mapping[str, Any] | None = None, name: str = "case"
    ) -> dict[str, Path]:
        root.mkdir(parents=True, exist_ok=True)
        artifacts = dict(artifacts or self.synthetic_artifacts())
        paths = {
            "runtime": root / f"{name}_runtime.json",
            "runtime_boundary": root / f"{name}_runtime_boundary.json",
            "runtime_permission": root / f"{name}_runtime_permission.json",
            "operation_execution": root / f"{name}_operation_execution.json",
        }
        for key, path in paths.items():
            self.write_json(path, artifacts[key])
        return paths

    def clean_request(self, paths: Mapping[str, Path]) -> dict[str, Any]:
        return (
            resolver.build_declared_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_request(
                selected_runtime_artifact=paths["runtime"],
                selected_runtime_boundary_artifact=paths["runtime_boundary"],
                selected_runtime_permission_artifact=paths["runtime_permission"],
                selected_operation_execution_artifact=paths["operation_execution"],
            )
        )

    def clean_request_with_artifacts(
        self, root: Path, name: str = "clean"
    ) -> tuple[dict[str, Any], dict[str, Path], dict[str, dict[str, Any]]]:
        artifacts = self.synthetic_artifacts()
        paths = self.write_synthetic_basis(root, artifacts, name)
        return self.clean_request(paths), paths, artifacts

    def set_layer_field(
        self, artifact: dict[str, Any], layer_names: tuple[str, ...], field: str, value: Any
    ) -> None:
        for layer_name in layer_names:
            layer = artifact.get(layer_name)
            if isinstance(layer, dict):
                layer[field] = value

    def artifact_layers(self, artifact_key: str) -> tuple[str, ...]:
        return {
            "runtime": (
                "local_relevance_medium_read_only_runtime",
                "local_relevance_medium_read_only_runtime_statement",
                "local_relevance_medium_read_only_runtime_summary",
            ),
            "runtime_boundary": (
                "local_relevance_medium_read_only_runtime_boundary",
                "local_relevance_medium_read_only_runtime_boundary_statement",
                "local_relevance_medium_read_only_runtime_boundary_summary",
            ),
            "runtime_permission": (
                "local_relevance_medium_read_only_runtime_permission",
                "local_relevance_medium_read_only_runtime_permission_statement",
                "local_relevance_medium_read_only_runtime_permission_summary",
            ),
            "operation_execution": (
                "local_relevance_medium_read_only_operation_execution",
                "local_relevance_medium_read_only_operation_execution_statement",
                "local_relevance_medium_read_only_operation_execution_summary",
            ),
        }[artifact_key]

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_request",
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
            "resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min",
        )
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(BOUNDARY_TYPE, resolver.SUPPORTED_BOUNDARY_TYPE_VALUES)
        self.assertIn(BOUNDARY_SCOPE, resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, SELECTED_COMMAND)

        for key in (
            "runtime_held_state_created",
            "runtime_hosting_created",
            "runtime_loop_created",
            "daemon_behavior_created",
            "continuation_created",
            "runtime_held_reentry_created",
            "second_operation_created",
            "prior_result_reentry_cycle_created",
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
            "RUNTIME_HELD_STATE_CREATED",
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

        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        request = (
            resolver.build_declared_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_request()
        )
        self.assertTrue(
            request["selected_runtime_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_reference_review_001__"
                "local_relevance_medium_read_only_runtime_v0_min_v3_result.json"
            )
        )
        self.assertTrue(
            request["selected_runtime_boundary_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_boundary_reference_review_001__"
                "local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
            )
        )
        self.assertTrue(
            request["selected_runtime_permission_artifact"].endswith(
                "local_relevance_medium_read_only_runtime_permission_reference_review_001__"
                "local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
            )
        )
        self.assertTrue(
            request["selected_operation_execution_artifact"].endswith(
                "local_relevance_medium_read_only_operation_execution_reference_review_001__"
                "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
            )
        )
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        self.assertEqual(request["boundary_type"], BOUNDARY_TYPE)
        self.assertEqual(request["boundary_scope"], BOUNDARY_SCOPE)
        declared_non_claims = request["declared_non_claims"]
        for key in (
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
            self.assertIs(declared_non_claims[key], False)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, paths, _artifacts = self.clean_request_with_artifacts(Path(tmp))
            result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                    request
                )
            )
            self.assert_recorded_boundary(result, paths)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        default_paths = {
            "runtime": DEFAULT_RUNTIME_ARTIFACT,
            "runtime_boundary": DEFAULT_RUNTIME_BOUNDARY_ARTIFACT,
            "runtime_permission": DEFAULT_RUNTIME_PERMISSION_ARTIFACT,
            "operation_execution": DEFAULT_OPERATION_EXECUTION_ARTIFACT,
        }
        missing = [str(path) for path in default_paths.values() if not path.exists()]
        if missing:
            self.skipTest("default live basis artifact missing: " + ", ".join(missing))

        request = (
            resolver.build_declared_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_request()
        )
        result = (
            resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                request
            )
        )
        self.assert_recorded_boundary(result, default_paths)

    def test_closure_older_runtime_and_failure_lineage_top_level_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base_request, _paths, _artifacts = self.clean_request_with_artifacts(Path(tmp))
            for key, expected_code in LINEAGE_TOP_LEVEL_CODES:
                with self.subTest(key=key):
                    request = copy.deepcopy(base_request)
                    request[key] = True
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assertIs(self.non_claims(result)[key], False)

            for key, _expected_code in LINEAGE_TOP_LEVEL_CODES:
                with self.subTest(declared_non_claim=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(self.non_claims(result)[key], False)

                with self.subTest(declared_non_claim_missing=key):
                    request = copy.deepcopy(base_request)
                    del request["declared_non_claims"][key]
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

                with self.subTest(declared_non_claim_non_bool=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = "false"
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_required_non_claims_canonicalize_false_when_flipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base_request, _paths, _artifacts = self.clean_request_with_artifacts(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(self.non_claims(result)[key], False)
                    self.assert_runtime_held_state_boundary_non_claims(result)

    def representative_cases(
        self, root: Path
    ) -> list[tuple[str, str, Callable[[dict[str, Any], dict[str, Any], dict[str, Path]], Any]]]:
        def request_set(key: str, value: Any) -> Callable[[dict[str, Any], dict[str, Any], dict[str, Path]], None]:
            def mutate(request: dict[str, Any], artifacts: dict[str, Any], paths: dict[str, Path]) -> None:
                request[key] = value

            return mutate

        def request_pop(key: str) -> Callable[[dict[str, Any], dict[str, Any], dict[str, Path]], None]:
            def mutate(request: dict[str, Any], artifacts: dict[str, Any], paths: dict[str, Path]) -> None:
                request.pop(key, None)

            return mutate

        def artifact_outcome(
            artifact_key: str, value: str
        ) -> Callable[[dict[str, Any], dict[str, Any], dict[str, Path]], None]:
            def mutate(request: dict[str, Any], artifacts: dict[str, Any], paths: dict[str, Path]) -> None:
                artifacts[artifact_key]["outcome"] = value
                self.write_json(paths[artifact_key], artifacts[artifact_key])

            return mutate

        def artifact_version(
            artifact_key: str, value: str
        ) -> Callable[[dict[str, Any], dict[str, Any], dict[str, Path]], None]:
            def mutate(request: dict[str, Any], artifacts: dict[str, Any], paths: dict[str, Path]) -> None:
                artifacts[artifact_key]["result_version"] = value
                self.write_json(paths[artifact_key], artifacts[artifact_key])

            return mutate

        def artifact_failed_checks(
            artifact_key: str, value: int
        ) -> Callable[[dict[str, Any], dict[str, Any], dict[str, Path]], None]:
            def mutate(request: dict[str, Any], artifacts: dict[str, Any], paths: dict[str, Path]) -> None:
                artifacts[artifact_key]["failed_check_count"] = value
                self.write_json(paths[artifact_key], artifacts[artifact_key])

            return mutate

        def artifact_array(
            artifact_key: str,
        ) -> Callable[[dict[str, Any], dict[str, Any], dict[str, Path]], None]:
            def mutate(request: dict[str, Any], artifacts: dict[str, Any], paths: dict[str, Path]) -> None:
                self.write_json(paths[artifact_key], ["not", "object"])

            return mutate

        def artifact_unreadable(
            artifact_key: str,
        ) -> Callable[[dict[str, Any], dict[str, Any], dict[str, Path]], None]:
            request_key = {
                "runtime": "selected_runtime_artifact",
                "runtime_boundary": "selected_runtime_boundary_artifact",
                "runtime_permission": "selected_runtime_permission_artifact",
                "operation_execution": "selected_operation_execution_artifact",
            }[artifact_key]

            def mutate(request: dict[str, Any], artifacts: dict[str, Any], paths: dict[str, Path]) -> None:
                request[request_key] = str(root / f"missing_{artifact_key}.json")

            return mutate

        def artifact_path_missing(
            request_key: str,
        ) -> Callable[[dict[str, Any], dict[str, Any], dict[str, Path]], None]:
            return request_set(request_key, "")

        def layer_false(
            artifact_key: str, field: str
        ) -> Callable[[dict[str, Any], dict[str, Any], dict[str, Path]], None]:
            def mutate(request: dict[str, Any], artifacts: dict[str, Any], paths: dict[str, Path]) -> None:
                self.set_layer_field(
                    artifacts[artifact_key],
                    self.artifact_layers(artifact_key),
                    field,
                    False,
                )
                self.write_json(paths[artifact_key], artifacts[artifact_key])

            return mutate

        cases: list[
            tuple[str, str, Callable[[dict[str, Any], dict[str, Any], dict[str, Path]], Any]]
        ] = [
            (
                "explicit block intent",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_BLOCK_REQUESTED",
                request_set(
                    "local_relevance_medium_read_only_runtime_held_state_boundary_intent",
                    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY",
                ),
            ),
            (
                "missing question",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_QUESTION_UNDECLARED",
                request_pop(
                    "local_relevance_medium_read_only_runtime_held_state_boundary_question"
                ),
            ),
            (
                "unsupported intent",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_INTENT_UNSUPPORTED",
                request_set(
                    "local_relevance_medium_read_only_runtime_held_state_boundary_intent",
                    "UNSUPPORTED",
                ),
            ),
            ("runtime artifact path missing", "RUNTIME_ARTIFACT_PATH_MISSING", artifact_path_missing("selected_runtime_artifact")),
            ("runtime artifact unreadable", "RUNTIME_ARTIFACT_UNREADABLE", artifact_unreadable("runtime")),
            ("runtime artifact JSON array", "RUNTIME_ARTIFACT_NOT_JSON_OBJECT", artifact_array("runtime")),
            ("runtime artifact not recorded", "RUNTIME_ARTIFACT_NOT_RECORDED", artifact_outcome("runtime", "WRONG")),
            ("runtime artifact failed checks", "RUNTIME_ARTIFACT_FAILED_CHECKS_PRESENT", artifact_failed_checks("runtime", 1)),
            ("runtime artifact version mismatch", "RUNTIME_ARTIFACT_VERSION_NOT_0_1_0", artifact_version("runtime", "9.9.9")),
            ("runtime boundary artifact path missing", "RUNTIME_BOUNDARY_ARTIFACT_PATH_MISSING", artifact_path_missing("selected_runtime_boundary_artifact")),
            ("runtime boundary artifact unreadable", "RUNTIME_BOUNDARY_ARTIFACT_UNREADABLE", artifact_unreadable("runtime_boundary")),
            ("runtime boundary artifact JSON array", "RUNTIME_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT", artifact_array("runtime_boundary")),
            ("runtime boundary artifact not recorded", "RUNTIME_BOUNDARY_ARTIFACT_NOT_RECORDED", artifact_outcome("runtime_boundary", "WRONG")),
            ("runtime boundary artifact failed checks", "RUNTIME_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT", artifact_failed_checks("runtime_boundary", 1)),
            ("runtime boundary artifact version mismatch", "RUNTIME_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0", artifact_version("runtime_boundary", "9.9.9")),
            ("runtime permission artifact path missing", "RUNTIME_PERMISSION_ARTIFACT_PATH_MISSING", artifact_path_missing("selected_runtime_permission_artifact")),
            ("runtime permission artifact unreadable", "RUNTIME_PERMISSION_ARTIFACT_UNREADABLE", artifact_unreadable("runtime_permission")),
            ("runtime permission artifact JSON array", "RUNTIME_PERMISSION_ARTIFACT_NOT_JSON_OBJECT", artifact_array("runtime_permission")),
            ("runtime permission artifact not recorded", "RUNTIME_PERMISSION_ARTIFACT_NOT_RECORDED", artifact_outcome("runtime_permission", "WRONG")),
            ("runtime permission artifact failed checks", "RUNTIME_PERMISSION_ARTIFACT_FAILED_CHECKS_PRESENT", artifact_failed_checks("runtime_permission", 1)),
            ("runtime permission artifact version mismatch", "RUNTIME_PERMISSION_ARTIFACT_VERSION_NOT_0_1_0", artifact_version("runtime_permission", "9.9.9")),
            ("operation execution artifact path missing", "OPERATION_EXECUTION_ARTIFACT_PATH_MISSING", artifact_path_missing("selected_operation_execution_artifact")),
            ("operation execution artifact unreadable", "OPERATION_EXECUTION_ARTIFACT_UNREADABLE", artifact_unreadable("operation_execution")),
            ("operation execution artifact JSON array", "OPERATION_EXECUTION_ARTIFACT_NOT_JSON_OBJECT", artifact_array("operation_execution")),
            ("operation execution artifact not recorded", "OPERATION_EXECUTION_ARTIFACT_NOT_RECORDED", artifact_outcome("operation_execution", "WRONG")),
            ("operation execution artifact failed checks", "OPERATION_EXECUTION_ARTIFACT_FAILED_CHECKS_PRESENT", artifact_failed_checks("operation_execution", 1)),
            ("operation execution artifact version mismatch", "OPERATION_EXECUTION_ARTIFACT_VERSION_NOT_0_1_0", artifact_version("operation_execution", "9.9.9")),
            ("selected command missing", "SELECTED_COMMAND_MISSING", request_set("selected_command", "")),
            ("selected command not state", "SELECTED_COMMAND_NOT_STATE", request_set("selected_command", "lookup")),
            ("selected runtime not recorded", "SELECTED_RUNTIME_NOT_RECORDED", layer_false("runtime", "selected_runtime_recorded")),
            ("runtime not created", "RUNTIME_NOT_CREATED", layer_false("runtime", "runtime_created")),
            ("runtime local only not true", "RUNTIME_LOCAL_ONLY_NOT_TRUE", layer_false("runtime", "runtime_local_only")),
            ("runtime read only not true", "RUNTIME_READ_ONLY_NOT_TRUE", layer_false("runtime", "runtime_read_only")),
            ("selected runtime boundary not recorded", "SELECTED_RUNTIME_BOUNDARY_NOT_RECORDED", layer_false("runtime_boundary", "selected_runtime_boundary_recorded")),
            ("future runtime may not be considered", "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED", layer_false("runtime_boundary", "future_runtime_may_be_considered")),
            ("selected runtime permission not recorded", "SELECTED_RUNTIME_PERMISSION_NOT_RECORDED", layer_false("runtime_permission", "selected_runtime_permission_recorded")),
            ("runtime permission not created", "RUNTIME_PERMISSION_NOT_CREATED", layer_false("runtime_permission", "runtime_permission_created")),
            ("runtime permission local only not true", "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE", layer_false("runtime_permission", "runtime_permission_local_only")),
            ("runtime permission read only not true", "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE", layer_false("runtime_permission", "runtime_permission_read_only")),
            ("selected operation execution not recorded", "SELECTED_OPERATION_EXECUTION_NOT_RECORDED", layer_false("operation_execution", "selected_operation_execution_recorded")),
            ("operation execution not created", "OPERATION_EXECUTION_NOT_CREATED", layer_false("operation_execution", "operation_execution_created")),
            ("operation execution not performed", "OPERATION_EXECUTION_NOT_PERFORMED", layer_false("operation_execution", "operation_execution_performed")),
            ("operation execution local only not true", "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE", layer_false("operation_execution", "operation_execution_local_only")),
            ("operation execution read only not true", "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE", layer_false("operation_execution", "operation_execution_read_only")),
            ("future runtime held state may not be considered", "FUTURE_RUNTIME_HELD_STATE_MAY_NOT_BE_CONSIDERED", request_set("future_runtime_held_state_may_not_be_considered", True)),
            ("boundary type missing", "BOUNDARY_TYPE_MISSING", request_set("boundary_type", "")),
            ("boundary type wrong", "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY", request_set("boundary_type", "REGISTRY")),
            ("boundary scope missing", "BOUNDARY_SCOPE_MISSING", request_set("boundary_scope", "")),
            ("boundary scope wrong", "BOUNDARY_SCOPE_NOT_SELECTED_RUNTIME_HELD_STATE_CONSIDERATION_ONLY", request_set("boundary_scope", "SEARCH_VIEW")),
            ("required non-claim missing", "NON_CLAIM_MISSING_OR_FLIPPED", lambda request, artifacts, paths: request["declared_non_claims"].pop("runtime_held_state_created", None)),
        ]

        top_level_flag_codes = (
            ("runtime_held_state_created", "RUNTIME_HELD_STATE_CREATED"),
            ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
            ("runtime_loop_created", "RUNTIME_LOOP_CREATED"),
            ("daemon_behavior_created", "DAEMON_BEHAVIOR_CREATED"),
            ("continuation_created", "CONTINUATION_CREATED"),
            ("runtime_held_reentry_created", "RUNTIME_HELD_REENTRY_CREATED"),
            ("second_operation_created", "SECOND_OPERATION_CREATED"),
            ("prior_result_reentry_cycle_created", "PRIOR_RESULT_REENTRY_CYCLE_CREATED"),
            ("public_api_created", "PUBLIC_API_CREATED"),
            ("participant_facing_interface_created", "PARTICIPANT_FACING_INTERFACE_CREATED"),
            ("distributed_network_behavior_created", "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
            ("general_operation_permission_created", "GENERAL_OPERATION_PERMISSION_CREATED"),
            ("general_lookup_permission_created", "GENERAL_LOOKUP_PERMISSION_CREATED"),
            ("arbitrary_lookup_permission_created", "ARBITRARY_LOOKUP_PERMISSION_CREATED"),
            ("unsupported_commands_permitted", "UNSUPPORTED_COMMANDS_PERMITTED"),
            ("unsupported_lookup_keys_permitted", "UNSUPPORTED_LOOKUP_KEYS_PERMITTED"),
            ("new_lookup_entry_created", "NEW_LOOKUP_ENTRY_CREATED"),
            ("new_signal_accepted", "NEW_SIGNAL_ACCEPTED"),
            ("new_entry_accepted", "NEW_ENTRY_ACCEPTED"),
            ("new_relevance_object_created", "NEW_RELEVANCE_OBJECT_CREATED"),
            ("new_index_entry_created", "NEW_INDEX_ENTRY_CREATED"),
            ("filesystem_discovery_performed", "FILESYSTEM_DISCOVERY_PERFORMED"),
            ("registry_created", "REGISTRY_CREATED"),
            ("search_surface_created", "SEARCH_SURFACE_CREATED"),
            ("query_surface_created", "QUERY_SURFACE_CREATED"),
            ("ranking_surface_created", "RANKING_SURFACE_CREATED"),
            ("scoring_surface_created", "SCORING_SURFACE_CREATED"),
            ("priority_surface_created", "PRIORITY_SURFACE_CREATED"),
            ("validity_judgment_created", "VALIDITY_JUDGMENT_CREATED"),
            ("truth_judgment_created", "TRUTH_JUDGMENT_CREATED"),
            ("authority_judgment_created", "AUTHORITY_JUDGMENT_CREATED"),
            ("currentness_judgment_created", "CURRENTNESS_JUDGMENT_CREATED"),
            (
                "older_runtime_lineage_imported_as_authority",
                "OLDER_RUNTIME_LINEAGE_IMPORTED_AS_AUTHORITY",
            ),
            (
                "older_runtime_permission_treated_as_current",
                "OLDER_RUNTIME_PERMISSION_TREATED_AS_CURRENT",
            ),
            ("runtime_authority_imported", "RUNTIME_AUTHORITY_IMPORTED"),
            ("runtime_v0_failure_repaired", "RUNTIME_V0_FAILURE_REPAIRED"),
            ("runtime_v0_failure_hidden", "RUNTIME_V0_FAILURE_HIDDEN"),
            ("runtime_v0_failure_claimed_passed", "RUNTIME_V0_FAILURE_CLAIMED_PASSED"),
            ("runtime_v2_failure_repaired", "RUNTIME_V2_FAILURE_REPAIRED"),
            ("runtime_v2_failure_hidden", "RUNTIME_V2_FAILURE_HIDDEN"),
            ("runtime_v2_failure_claimed_passed", "RUNTIME_V2_FAILURE_CLAIMED_PASSED"),
            (
                "runtime_boundary_v0_failure_repaired",
                "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
            ),
            ("runtime_boundary_v0_failure_hidden", "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN"),
            (
                "runtime_boundary_v0_failure_claimed_passed",
                "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
            ),
            ("repeated_reception_permission_created", "REPEATED_RECEPTION_PERMISSION_CREATED"),
            ("arbitrary_reception_created", "ARBITRARY_RECEPTION_CREATED"),
            ("feed_created", "FEED_CREATED"),
            ("source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
            ("source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
            ("source_created", "SOURCE_CREATED"),
            ("authority_created", "AUTHORITY_CREATED"),
            ("currentness_created", "CURRENTNESS_CREATED"),
            ("truth_created", "TRUTH_CREATED"),
            ("synchronization_created", "SYNCHRONIZATION_CREATED"),
            ("participation_authorized", "PARTICIPATION_AUTHORIZED"),
            ("participant_role_created", "PARTICIPANT_ROLE_CREATED"),
            ("deployment_created", "DEPLOYMENT_CREATED"),
            ("public_release_created", "PUBLIC_RELEASE_CREATED"),
            ("broader_reusable_permission_created", "BROADER_REUSABLE_PERMISSION_CREATED"),
            ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
            ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
            ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
            (
                "artifact_existence_treated_as_runtime_held_state_boundary_authority",
                "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HELD_STATE_BOUNDARY_AUTHORITY",
            ),
            (
                "latest_file_posture_treated_as_runtime_held_state_boundary_authority",
                "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HELD_STATE_BOUNDARY_AUTHORITY",
            ),
            (
                "repo_local_availability_treated_as_runtime_held_state_boundary_authority",
                "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HELD_STATE_BOUNDARY_AUTHORITY",
            ),
            (
                "hidden_repo_state_used_as_runtime_held_state_boundary_content",
                "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HELD_STATE_BOUNDARY_CONTENT",
            ),
            (
                "hidden_repo_state_used_as_runtime_held_state_boundary_authority",
                "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HELD_STATE_BOUNDARY_AUTHORITY",
            ),
            (
                "predecessor_failure_repaired",
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
            (
                "predecessor_failure_hidden",
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
            (
                "predecessor_failure_claimed_passed",
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
        )
        for key, code in top_level_flag_codes:
            cases.append((key, code, request_set(key, True)))
        return cases

    def test_representative_blocking_behavior(self) -> None:
        malformed_result = (
            resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                ["not", "a", "mapping"]  # type: ignore[arg-type]
            )
        )
        self.assert_blocked_with_public_code(malformed_result)
        self.assertEqual(
            self.block_code(malformed_result),
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_REQUEST_MALFORMED",
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = self.representative_cases(root)
            for index, (name, expected_code, mutate) in enumerate(cases, start=1):
                with self.subTest(name=name):
                    case_name = Path(self.safe_json_filename(name, index)).stem
                    artifacts = self.synthetic_artifacts()
                    paths = self.write_synthetic_basis(root / case_name, artifacts, case_name)
                    request = self.clean_request(paths)
                    mutate(request, artifacts, paths)
                    result = (
                        resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths, _artifacts = self.clean_request_with_artifacts(Path(tmp))
            result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                    request
                )
            )
            self.assert_recorded_boundary(result)
            serialized = json.dumps(result, ensure_ascii=False, sort_keys=True)
            for official in (
                BOUNDARY_TYPE,
                BOUNDARY_SCOPE,
                SELECTED_COMMAND,
                resolver.OUTCOME_RECORDED,
                resolver.RESOLVER_MODULE,
            ):
                self.assertIn(official, serialized)
            self.assertNotIn("[REDACTED]", serialized)
            self.assertNotIn("[REDACTED_OFFICIAL_VALUE]", serialized)
            for outcome in (
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_BLOCKED,
            ):
                self.assertIn(outcome, resolver.OUTCOME_FAMILY)

    def test_raw_hidden_and_older_runtime_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, paths, artifacts = self.clean_request_with_artifacts(Path(tmp))
            request["raw_runtime_held_state_boundary_body"] = HOSTILE_SENTINELS[0]
            request["hidden_repo_state"] = {"body": HOSTILE_SENTINELS[-1]}
            request["older_runtime_context"] = HOSTILE_SENTINELS[-2]
            for index, artifact in enumerate(artifacts.values()):
                artifact["raw_runtime_body"] = HOSTILE_SENTINELS[index % len(HOSTILE_SENTINELS)]
                artifact["hidden_repo_state"] = {
                    "full_body": HOSTILE_SENTINELS[(index + 1) % len(HOSTILE_SENTINELS)]
                }
            for key, path in paths.items():
                self.write_json(path, artifacts[key])
            original_request = copy.deepcopy(request)

            result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                    request
                )
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assert_no_sentinels(result)
            serialized = json.dumps(result, ensure_ascii=False, sort_keys=True)
            self.assertIn(BOUNDARY_TYPE, serialized)
            self.assertIn(BOUNDARY_SCOPE, serialized)
            self.assertIn(SELECTED_COMMAND, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assert_runtime_held_state_boundary_non_claims(result)
            self.assert_lineage_preserved(result)
            self.assertEqual(request, original_request)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request, _paths, _artifacts = self.clean_request_with_artifacts(root)
            request_path = self.write_json(root / "request.json", request)
            result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_from_path(
                    request_path
                )
            )
            self.assert_recorded_boundary(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed_result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_from_path(
                    malformed_path
                )
            )
            self.assert_blocked_with_public_code(malformed_result)

            array_path = self.write_json(root / "array.json", ["not", "object"])
            array_result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_from_path(
                    array_path
                )
            )
            self.assert_blocked_with_public_code(array_result)

            missing_result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_from_path(
                    root / "missing_request.json"
                )
            )
            self.assert_blocked_with_public_code(missing_result)

            output_root = root / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result(
                    result
                )

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(first_path.parent, output_root)
            self.assertIn(EXPECTED_OUTPUT_ROOT.name, first_path.parts)
            with first_path.open("r", encoding="utf-8") as handle:
                loaded = json.load(handle)
            self.assertEqual(loaded["outcome"], resolver.OUTCOME_RECORDED)
            for forbidden_root in FORBIDDEN_OUTPUT_ROOTS:
                self.assertFalse(
                    self.path_contains_part_sequence(first_path, forbidden_root),
                    f"output path unexpectedly under preserved root {forbidden_root}",
                )

    def path_contains_part_sequence(self, path: Path, sequence: Path) -> bool:
        parts = path.parts
        sequence_parts = sequence.parts
        if not sequence_parts:
            return False
        end = len(parts) - len(sequence_parts) + 1
        return any(parts[index : index + len(sequence_parts)] == sequence_parts for index in range(end))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths, artifacts = self.clean_request_with_artifacts(Path(tmp))
            request["raw_runtime_loop_body"] = HOSTILE_SENTINELS[6]
            request_before = copy.deepcopy(request)
            artifacts_before = copy.deepcopy(artifacts)
            result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                    request
                )
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assertEqual(request, request_before)
            self.assertEqual(artifacts, artifacts_before)

    def test_failure_lineage_and_predecessor_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths, _artifacts = self.clean_request_with_artifacts(Path(tmp))
            result = (
                resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                    request
                )
            )
            self.assert_recorded_boundary(result)
            summary = resolver.build_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_summary(
                result
            )
            self.assertIs(
                summary["runtime_v0_v2_boundary_v0_failure_evidence_preserved"], True
            )
            self.assertIs(
                summary[
                    "runtime_v0_v2_boundary_v0_failure_not_repaired_hidden_claimed_passed"
                ],
                True,
            )
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(summary["consumed_request_token_remains_closed"], True)
            self.assertIs(summary["authorization_token_reuse_blocked"], True)
            self.assertIs(summary["older_runtime_lineage_not_imported_as_authority"], True)
            self.assertIs(summary["older_runtime_permission_not_treated_as_current"], True)
            self.assertIs(summary["runtime_authority_not_imported"], True)

            for key, expected_code in LINEAGE_TOP_LEVEL_CODES[5:]:
                with self.subTest(key=key):
                    mutated = copy.deepcopy(request)
                    mutated[key] = True
                    blocked = (
                        resolver.resolve_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min(
                            mutated
                        )
                    )
                    self.assert_blocked_with_public_code(blocked)
                    self.assertEqual(self.block_code(blocked), expected_code)


if __name__ == "__main__":
    unittest.main()
