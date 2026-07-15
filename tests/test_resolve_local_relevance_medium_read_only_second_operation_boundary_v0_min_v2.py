"""V2 tests for the local read-only second-operation boundary resolver.

This suite treats the v1 second-operation boundary resolver/test as preserved
failed-lineage evidence: v1 mostly passed synthetic tests, but blocked default
live artifacts because positive basis posture was too narrowly extracted from
exact selected-object fields. The v2 target is additive successor evidence. It
does not repair, patch, edit, hide, rename, delete, or claim passed v1.

The v2 resolver records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY object only. These
tests verify that positive basis facts can be derived from bounded equivalent
evidence while forbidden false posture remains strict exact-key posture:
selected-object exact field first, then exact top-level non_claims only when
the selected-object field is absent, with no recursive artifact scan.
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

import resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2 as resolver  # noqa: E402


BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY"
BOUNDARY_SCOPE = "SELECTED_SECOND_OPERATION_CONSIDERATION_ONLY"
SELECTED_COMMAND = "state"
REQ_FALSE = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
FIELD_CODES = getattr(resolver, "FIELD_BLOCK_CODES", {})

EXPECTED_OUTCOME_FAMILY = {
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_NOT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_BLOCKED",
}

EXPECTED_WRAPPER_SECTIONS = {
    "local_relevance_medium_read_only_second_operation_boundary_metadata",
    "declared_local_relevance_medium_read_only_second_operation_boundary_question",
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
    "local_relevance_medium_read_only_second_operation_boundary",
    "local_relevance_medium_read_only_second_operation_boundary_checks",
    "local_relevance_medium_read_only_second_operation_boundary_statement",
    "local_relevance_medium_read_only_second_operation_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_second_operation_boundary_summary",
}

FORBIDDEN_WRAPPER_FIELDS_IN_BOUNDARY = {
    "outcome",
    "block",
    "local_relevance_medium_read_only_second_operation_boundary_checks",
    "non_claims",
    "local_relevance_medium_read_only_second_operation_boundary_summary",
    "local_relevance_medium_read_only_second_operation_boundary_metadata",
}

DEFAULT_SUFFIXES = {
    "selected_prior_result_reentry_cycle_artifact": (
        "local_relevance_medium_read_only_prior_result_reentry_cycle_reference_review_001__"
        "local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2_result.json"
    ),
    "selected_prior_result_reentry_boundary_artifact": (
        "local_relevance_medium_read_only_prior_result_reentry_boundary_reference_review_001__"
        "local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min_result.json"
    ),
    "selected_runtime_held_reentry_artifact": (
        "local_relevance_medium_read_only_runtime_held_reentry_reference_review_001__"
        "local_relevance_medium_read_only_runtime_held_reentry_v0_min_result.json"
    ),
    "selected_runtime_held_reentry_boundary_artifact": (
        "local_relevance_medium_read_only_runtime_held_reentry_boundary_reference_review_001__"
        "local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min_result.json"
    ),
    "selected_runtime_held_state_artifact": (
        "local_relevance_medium_read_only_runtime_held_state_reference_review_001__"
        "local_relevance_medium_read_only_runtime_held_state_v0_min_result.json"
    ),
    "selected_runtime_held_state_boundary_artifact": (
        "local_relevance_medium_read_only_runtime_held_state_boundary_reference_review_001__"
        "local_relevance_medium_read_only_runtime_held_state_boundary_v0_min_result.json"
    ),
    "selected_runtime_artifact": (
        "local_relevance_medium_read_only_runtime_reference_review_001__"
        "local_relevance_medium_read_only_runtime_v0_min_v3_result.json"
    ),
    "selected_runtime_boundary_artifact": (
        "local_relevance_medium_read_only_runtime_boundary_reference_review_001__"
        "local_relevance_medium_read_only_runtime_boundary_v0_min_v2_result.json"
    ),
    "selected_runtime_permission_artifact": (
        "local_relevance_medium_read_only_runtime_permission_reference_review_001__"
        "local_relevance_medium_read_only_runtime_permission_v0_min_result.json"
    ),
    "selected_operation_execution_artifact": (
        "local_relevance_medium_read_only_operation_execution_reference_review_001__"
        "local_relevance_medium_read_only_operation_execution_v0_min_result.json"
    ),
}

BASIS = (
    (
        "prior_result_reentry_cycle",
        "selected_prior_result_reentry_cycle_artifact",
        "local_relevance_medium_read_only_prior_result_reentry_cycle",
        "basis_prior_result_reentry_cycle",
        "PRIOR_RESULT_REENTRY_CYCLE_ARTIFACT",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_RECORDED",
        "cycle_type",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE",
        "cycle_scope",
        "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY",
        {
            "selected_prior_result_reentry_cycle_recorded": True,
            "prior_result_reentry_cycle_recorded": True,
            "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded": True,
            "prior_result_reentry_cycle_created": True,
            "prior_result_reentry_cycle_local_only": True,
            "prior_result_reentry_cycle_read_only": True,
            "cycle_basis_reference_only": True,
            "runtime_v0_failure_evidence_preserved": True,
            "runtime_v2_failure_evidence_preserved": True,
            "runtime_boundary_v0_failure_evidence_preserved": True,
            "prior_result_boundary_v1_failure_evidence_preserved": True,
            "prior_result_boundary_v2_successor_evidence_preserved": True,
            "prior_result_cycle_v1_failure_evidence_preserved": True,
            "prior_result_cycle_v2_successor_evidence_preserved": True,
        },
    ),
    (
        "prior_result_reentry_boundary",
        "selected_prior_result_reentry_boundary_artifact",
        "local_relevance_medium_read_only_prior_result_reentry_boundary",
        "basis_prior_result_reentry_boundary",
        "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_RECORDED",
        "boundary_type",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY",
        "boundary_scope",
        "SELECTED_PRIOR_RESULT_REENTRY_CONSIDERATION_ONLY",
        {
            "selected_prior_result_reentry_boundary_recorded": True,
            "prior_result_reentry_boundary_recorded": True,
            "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded": True,
            "future_prior_result_reentry_cycle_may_be_considered": True,
        },
    ),
    (
        "runtime_held_reentry",
        "selected_runtime_held_reentry_artifact",
        "local_relevance_medium_read_only_runtime_held_reentry",
        "basis_runtime_held_reentry",
        "RUNTIME_HELD_REENTRY_ARTIFACT",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_RECORDED",
        "held_reentry_type",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY",
        "held_reentry_scope",
        "SELECTED_RUNTIME_HELD_REENTRY_ONLY",
        {
            "selected_runtime_held_reentry_recorded": True,
            "runtime_held_reentry_recorded": True,
            "local_relevance_medium_read_only_runtime_held_reentry_recorded": True,
            "runtime_held_reentry_created": True,
            "runtime_held_reentry_local_only": True,
            "runtime_held_reentry_read_only": True,
            "held_reentry_basis_reference_only": True,
        },
    ),
    (
        "runtime_held_reentry_boundary",
        "selected_runtime_held_reentry_boundary_artifact",
        "local_relevance_medium_read_only_runtime_held_reentry_boundary",
        "basis_runtime_held_reentry_boundary",
        "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY_RECORDED",
        "boundary_type",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY",
        "boundary_scope",
        "SELECTED_RUNTIME_HELD_REENTRY_CONSIDERATION_ONLY",
        {
            "selected_runtime_held_reentry_boundary_recorded": True,
            "runtime_held_reentry_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_held_reentry_boundary_recorded": True,
            "future_runtime_held_reentry_may_be_considered": True,
        },
    ),
    (
        "runtime_held_state",
        "selected_runtime_held_state_artifact",
        "local_relevance_medium_read_only_runtime_held_state",
        "basis_runtime_held_state",
        "RUNTIME_HELD_STATE_ARTIFACT",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_RECORDED",
        "held_state_type",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE",
        "held_state_scope",
        "SELECTED_RUNTIME_HELD_STATE_ONLY",
        {
            "selected_runtime_held_state_recorded": True,
            "runtime_held_state_recorded": True,
            "local_relevance_medium_read_only_runtime_held_state_recorded": True,
            "runtime_held_state_created": True,
            "runtime_held_state_local_only": True,
            "runtime_held_state_read_only": True,
            "held_state_basis_reference_only": True,
        },
    ),
    (
        "runtime_held_state_boundary",
        "selected_runtime_held_state_boundary_artifact",
        "local_relevance_medium_read_only_runtime_held_state_boundary",
        "basis_runtime_held_state_boundary",
        "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_RECORDED",
        "boundary_type",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY",
        "boundary_scope",
        "SELECTED_RUNTIME_HELD_STATE_CONSIDERATION_ONLY",
        {
            "selected_runtime_held_state_boundary_recorded": True,
            "runtime_held_state_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_held_state_boundary_recorded": True,
            "future_runtime_held_state_may_be_considered": True,
        },
    ),
    (
        "runtime",
        "selected_runtime_artifact",
        "local_relevance_medium_read_only_runtime",
        "basis_runtime",
        "RUNTIME_ARTIFACT",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED",
        "runtime_type",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME",
        "runtime_scope",
        "SELECTED_RUNTIME_ONLY",
        {
            "selected_runtime_recorded": True,
            "runtime_recorded": True,
            "local_relevance_medium_read_only_runtime_recorded": True,
            "runtime_created": True,
            "runtime_local_only": True,
            "runtime_read_only": True,
        },
    ),
    (
        "runtime_boundary",
        "selected_runtime_boundary_artifact",
        "local_relevance_medium_read_only_runtime_boundary",
        "basis_runtime_boundary",
        "RUNTIME_BOUNDARY_ARTIFACT",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED",
        "boundary_type",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY",
        "boundary_scope",
        "SELECTED_RUNTIME_CONSIDERATION_ONLY",
        {
            "selected_runtime_boundary_recorded": True,
            "runtime_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_boundary_recorded": True,
            "future_runtime_may_be_considered": True,
        },
    ),
    (
        "runtime_permission",
        "selected_runtime_permission_artifact",
        "local_relevance_medium_read_only_runtime_permission",
        "basis_runtime_permission",
        "RUNTIME_PERMISSION_ARTIFACT",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED",
        "runtime_permission_type",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION",
        "runtime_permission_scope",
        "SELECTED_RUNTIME_PERMISSION_ONLY",
        {
            "selected_runtime_permission_recorded": True,
            "runtime_permission_recorded": True,
            "local_relevance_medium_read_only_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
        },
    ),
    (
        "operation_execution",
        "selected_operation_execution_artifact",
        "local_relevance_medium_read_only_operation_execution",
        "basis_operation_execution",
        "OPERATION_EXECUTION_ARTIFACT",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
        "operation_execution_type",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION",
        "operation_execution_scope",
        "SELECTED_OPERATION_EXECUTION_ONLY",
        {
            "selected_operation_execution_recorded": True,
            "operation_execution_recorded": True,
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
        },
    ),
)

TRUE_BOUNDARY_FIELDS = tuple(getattr(resolver, "POSITIVE_BOUNDARY_FIELDS", ()))

EXACT_FORBIDDEN = (
    "second_operation_created",
    "continuation_created",
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

LINEAGE_FALSE = (
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

LINEAGE_TRUE = (
    "second_operation_boundary_v1_failure_evidence_preserved",
    "second_operation_boundary_v2_successor_evidence_preserved",
    "prior_result_cycle_v1_failure_evidence_preserved",
    "prior_result_cycle_v2_successor_evidence_preserved",
    "prior_result_boundary_v1_failure_evidence_preserved",
    "prior_result_boundary_v2_successor_evidence_preserved",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
)

HOSTILE_SENTINELS = (
    "RAW_SECOND_OPERATION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
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
    "RAW_STATE_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


class TestLocalRelevanceMediumReadOnlySecondOperationBoundaryV0MinV2(unittest.TestCase):
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

    def basis_by_name(self, name: str) -> tuple[Any, ...]:
        for basis in BASIS:
            if basis[0] == name:
                return basis
        raise AssertionError(f"unknown basis {name}")

    def write_json(self, path: Path, value: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            json.dump(value, file, indent=2, sort_keys=True)
            file.write("\n")

    def make_artifact(self, basis: tuple[Any, ...]) -> dict[str, Any]:
        (
            _name,
            _request_key,
            object_key,
            _basis_prefix,
            _block_prefix,
            outcome,
            type_key,
            type_value,
            scope_key,
            scope_value,
            true_fields,
        ) = basis
        selected = {
            type_key: type_value,
            scope_key: scope_value,
            "selected_command": SELECTED_COMMAND,
            "selected_command_is_state": True,
            **{key: False for key in REQ_FALSE},
            **copy.deepcopy(true_fields),
        }
        statement = copy.deepcopy(true_fields)
        statement.update({key: False for key in EXACT_FORBIDDEN})
        summary = copy.deepcopy(statement)
        non_meaning = {
            key: True
            for key in true_fields
            if "evidence_preserved" in key or "successor_evidence_preserved" in key
        }
        return {
            "outcome": outcome,
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
            object_key: selected,
            "statement": statement,
            "summary": summary,
            "non_meaning": non_meaning,
            "non_claims": {key: False for key in REQ_FALSE},
            "local_relevance_medium_read_only_second_operation_boundary_checks": [
                {"check_name": "synthetic_clean", "passed": True}
            ],
        }

    def make_artifacts(self) -> dict[str, dict[str, Any]]:
        return {basis[0]: self.make_artifact(basis) for basis in BASIS}

    def selected_object(
        self,
        artifacts: Mapping[str, dict[str, Any]],
        name: str,
    ) -> dict[str, Any]:
        object_key = self.basis_by_name(name)[2]
        selected = artifacts[name][object_key]
        self.assertIsInstance(selected, dict)
        return selected

    def write_artifacts(
        self,
        root: Path,
        artifacts: Mapping[str, Any],
        prefix: str = "basis",
    ) -> dict[str, Path]:
        paths = {}
        for index, basis in enumerate(BASIS, start=1):
            name = basis[0]
            path = root / self.safe_json_filename(f"{prefix}_{name}", index)
            self.write_json(path, artifacts[name])
            paths[name] = path
        return paths

    def request_for(self, paths: Mapping[str, Path], **overrides: Any) -> dict[str, Any]:
        kwargs = {
            "selected_prior_result_reentry_cycle_artifact": paths["prior_result_reentry_cycle"],
            "selected_prior_result_reentry_boundary_artifact": paths["prior_result_reentry_boundary"],
            "selected_runtime_held_reentry_artifact": paths["runtime_held_reentry"],
            "selected_runtime_held_reentry_boundary_artifact": paths["runtime_held_reentry_boundary"],
            "selected_runtime_held_state_artifact": paths["runtime_held_state"],
            "selected_runtime_held_state_boundary_artifact": paths["runtime_held_state_boundary"],
            "selected_runtime_artifact": paths["runtime"],
            "selected_runtime_boundary_artifact": paths["runtime_boundary"],
            "selected_runtime_permission_artifact": paths["runtime_permission"],
            "selected_operation_execution_artifact": paths["operation_execution"],
            "boundary_type": BOUNDARY_TYPE,
            "boundary_scope": BOUNDARY_SCOPE,
            "selected_command": SELECTED_COMMAND,
        }
        kwargs.update(overrides)
        return (
            resolver.build_declared_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_request(
                **kwargs
            )
        )

    def clean_context(
        self,
        root: Path,
        artifact_mutator: Callable[[dict[str, dict[str, Any]]], None] | None = None,
        request_mutator: Callable[[dict[str, Any]], None] | None = None,
        prefix: str = "clean",
    ) -> tuple[dict[str, Any], dict[str, dict[str, Any]], dict[str, Path]]:
        artifacts = self.make_artifacts()
        if artifact_mutator:
            artifact_mutator(artifacts)
        paths = self.write_artifacts(root, artifacts, prefix=prefix)
        request = self.request_for(paths)
        if request_mutator:
            request_mutator(request)
        return request, artifacts, paths

    def resolve_clean(
        self,
        root: Path,
    ) -> tuple[dict[str, Any], dict[str, Any], dict[str, dict[str, Any]], dict[str, Path]]:
        request, artifacts, paths = self.clean_context(root)
        result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
            request
        )
        return result, request, artifacts, paths

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get("local_relevance_medium_read_only_second_operation_boundary_checks")
        self.assertIsInstance(checks, list)
        return [check for check in checks if isinstance(check, Mapping)]

    def check_by_name(self, result: Mapping[str, Any], name: str) -> Mapping[str, Any]:
        for check in self.checks(result):
            if check.get("check_name") == name:
                return check
        raise AssertionError(f"missing check {name}")

    def block_code(self, result: Mapping[str, Any]) -> Any:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

    def emitted_codes(self, result: Mapping[str, Any]) -> set[str]:
        codes = set()
        code = self.block_code(result)
        if isinstance(code, str):
            codes.add(code)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                value = check.get(key)
                if isinstance(value, str):
                    codes.add(value)
        return codes

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is not True)

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        boundary = result.get("local_relevance_medium_read_only_second_operation_boundary")
        self.assertIsInstance(boundary, Mapping)
        return boundary

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get("local_relevance_medium_read_only_second_operation_boundary_statement")
        self.assertIsInstance(statement, Mapping)
        return statement

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get("local_relevance_medium_read_only_second_operation_boundary_summary")
        self.assertIsInstance(summary, Mapping)
        return summary

    def non_claims(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        return non_claims

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        for code in self.emitted_codes(result):
            self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = self.non_claims(result)
        for key in REQ_FALSE:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIsInstance(non_claims[key], bool, key)
        self.assertNotIn("future_second_operation_may_be_considered", non_claims)

    def assert_second_operation_boundary_non_claims(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in REQ_FALSE:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False, key)
        for key in (
            "second_operation_created",
            "continuation_created",
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
            "follow_on_work_authorized",
        ):
            self.assertIs(boundary[key], False, key)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_second_operation_boundary_non_claims(result)

    def assert_same_or_stable_artifact_path(self, actual: Any, expected: Any) -> None:
        actual_path = Path(str(actual))
        expected_path = Path(str(expected))
        try:
            if actual_path.resolve() == expected_path.resolve():
                return
        except OSError:
            pass
        actual_stable = str(actual).replace("\\", "/")
        expected_stable = str(expected).replace("\\", "/")
        self.assertTrue(
            actual_stable.endswith(expected_path.name) or actual_stable.endswith(expected_stable),
            f"{actual!r} did not match {expected!r}",
        )

    def assert_recorded_boundary(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertEqual(boundary["boundary_id"], "local_relevance_medium_read_only_second_operation_boundary_001")
        self.assertEqual(boundary["boundary_type"], BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.RESULT_VERSION)
        self.assertEqual(boundary["boundary_scope"], BOUNDARY_SCOPE)
        self.assertEqual(boundary["selected_command"], SELECTED_COMMAND)
        for key in TRUE_BOUNDARY_FIELDS:
            self.assertIs(boundary[key], True, key)
        for key in FORBIDDEN_WRAPPER_FIELDS_IN_BOUNDARY:
            self.assertNotIn(key, boundary)
        self.assert_second_operation_boundary_non_claims(result)
        self.assert_canonical_false_non_claims(result)

    def assert_lineage_and_closure(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        statement = self.statement(result)
        summary = self.summary(result)
        for key in LINEAGE_TRUE:
            self.assertIs(boundary[key], True, key)
            self.assertIs(statement[key], True, key)
            self.assertIs(summary[key], True, key)
        for key in LINEAGE_FALSE:
            self.assertIs(boundary[key], False, key)
            self.assertIs(self.non_claims(result)[key], False, key)
        self.assertIs(boundary["consumed_request_reopened"], False)
        self.assertIs(boundary["authorization_token_reused"], False)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["result_level_non_claims_canonical_false"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)
        self.assertIs(summary["failure_not_repaired"], True)
        self.assertIs(summary["failure_not_hidden"], True)
        self.assertIs(summary["failure_not_claimed_passed"], True)

    def add_explanatory_true_values(self, artifacts: dict[str, dict[str, Any]]) -> None:
        explanatory = {
            "second_operation_created_false_posture": True,
            "second_operation_not_created": True,
            "continuation_created_false_posture": True,
            "continuation_not_created": True,
            "runtime_hosting_not_created": True,
            "runtime_loop_not_created": True,
            "daemon_behavior_not_created": True,
            "raw_state_body_embedded_false_posture": True,
            "state_mutation_performed_false_posture": True,
            "state_update_performed_false_posture": True,
            "older_runtime_authority_import_refusal_preserved": True,
            "result_level_non_claims_canonical_false": True,
            "follow_on_not_authorized": True,
            "future_second_operation_may_be_considered": True,
        }
        for artifact in artifacts.values():
            artifact["statement"].update(explanatory)
            artifact["summary"].update(explanatory)
            artifact["non_meaning"].update(explanatory)
            artifact["metadata"] = copy.deepcopy(explanatory)
            artifact["explanatory_posture"] = copy.deepcopy(explanatory)
            artifact["basis_commentary"] = {"lineage_evidence": copy.deepcopy(explanatory)}
            artifact["false_posture_preserved"] = copy.deepcopy(explanatory)
            artifact["non_claim_preservation"] = copy.deepcopy(explanatory)
            artifact["local_relevance_medium_read_only_second_operation_boundary_checks"] = [
                {
                    "check_name": "preserves_false_posture",
                    "passed": True,
                    "expected_posture": False,
                    "actual_posture": True,
                }
            ]

    def remove_positive_selected_object_fields(
        self,
        artifacts: dict[str, dict[str, Any]],
    ) -> None:
        removals = (
            ("prior_result_reentry_boundary", "selected_prior_result_reentry_boundary_recorded", "statement"),
            ("runtime_held_reentry_boundary", "selected_runtime_held_reentry_boundary_recorded", "summary"),
            ("runtime_held_state_boundary", "selected_runtime_held_state_boundary_recorded", None),
            ("runtime_boundary", "selected_runtime_boundary_recorded", None),
            ("prior_result_reentry_cycle", "prior_result_cycle_v1_failure_evidence_preserved", "non_meaning"),
            ("prior_result_reentry_cycle", "prior_result_cycle_v2_successor_evidence_preserved", "summary"),
            ("prior_result_reentry_cycle", "second_operation_boundary_v1_failure_evidence_preserved", "non_meaning"),
            ("prior_result_reentry_cycle", "second_operation_boundary_v2_successor_evidence_preserved", "summary"),
        )
        for artifact_name, field, section in removals:
            self.selected_object(artifacts, artifact_name).pop(field, None)
            if section is not None:
                artifacts[artifact_name].setdefault(section, {})[field] = True
        self.selected_object(artifacts, "prior_result_reentry_boundary").pop(
            "prior_result_reentry_boundary_recorded",
            None,
        )
        artifacts["prior_result_reentry_boundary"]["statement"][
            "prior_result_reentry_boundary_recorded"
        ] = True
        self.selected_object(artifacts, "runtime_boundary").pop("runtime_boundary_recorded", None)

    def inject_hostile_content(
        self,
        artifacts: dict[str, dict[str, Any]],
        request: dict[str, Any],
    ) -> None:
        for index, artifact in enumerate(artifacts.values()):
            sentinel = HOSTILE_SENTINELS[index % len(HOSTILE_SENTINELS)]
            artifact["raw_body"] = sentinel
            artifact["raw_full_body"] = sentinel
            artifact["artifact_body"] = "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN"
            artifact["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
            artifact["commentary"] = {"raw_runtime_body": "RAW_RUNTIME_BODY_MUST_NOT_RETURN"}
        request["raw_second_operation_boundary_body"] = "RAW_SECOND_OPERATION_BOUNDARY_BODY_MUST_NOT_RETURN"
        request["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2",
            "resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_from_path",
            "write_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_result",
            "build_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_summary",
            "build_declared_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)), name)
        for name in (
            "resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min",
            "resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_from_path",
            "write_local_relevance_medium_read_only_second_operation_boundary_v0_min_result",
            "build_local_relevance_medium_read_only_second_operation_boundary_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_second_operation_boundary_v0_min_request",
        ):
            if hasattr(resolver, name):
                self.assertTrue(callable(getattr(resolver, name)), name)
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
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2",
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2"
            )
        )
        self.assertIn(BOUNDARY_TYPE, resolver.SUPPORTED_BOUNDARY_TYPE_VALUES)
        self.assertIn(BOUNDARY_SCOPE, resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, SELECTED_COMMAND)
        self.assertEqual(set(resolver.OUTCOME_FAMILY), EXPECTED_OUTCOME_FAMILY)
        for key in (
            "second_operation_created",
            "continuation_created",
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
        self.assertNotIn(
            "future_second_operation_may_be_considered",
            resolver.REQUIRED_FALSE_NON_CLAIMS,
        )
        for code in (
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
            resolver.build_declared_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_request()
        )
        for key, suffix in DEFAULT_SUFFIXES.items():
            self.assertTrue(str(request[key]).endswith(suffix), key)
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        self.assertEqual(request["boundary_type"], BOUNDARY_TYPE)
        self.assertEqual(request["boundary_scope"], BOUNDARY_SCOPE)
        for key in REQ_FALSE:
            self.assertIn(key, request["declared_non_claims"])
            self.assertIs(request["declared_non_claims"][key], False)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result, _request, _artifacts, paths = self.resolve_clean(Path(temp_dir))
            self.assertIsInstance(result, dict)
            self.assertTrue(EXPECTED_WRAPPER_SECTIONS.issubset(result))
            self.assert_recorded_boundary(result)
            self.assert_lineage_and_closure(result)
            boundary = self.boundary(result)
            for basis in BASIS:
                name, _request_key, _object_key, basis_prefix, _block_prefix, outcome, *_rest = basis
                self.assert_same_or_stable_artifact_path(
                    boundary[f"{basis_prefix}_artifact_path"],
                    paths[name],
                )
                self.assertEqual(boundary[f"{basis_prefix}_outcome"], outcome)
                self.assertEqual(boundary[f"{basis_prefix}_result_version"], "0.1.0")
                self.assertEqual(boundary[f"{basis_prefix}_failed_check_count"], 0)
            statement = self.statement(result)
            self.assertIs(
                statement["local_relevance_medium_read_only_second_operation_boundary_recorded"],
                True,
            )
            for basis in BASIS:
                preserved_key = f"{basis[3]}_artifact_preserved"
                self.assertIs(statement[preserved_key], True, preserved_key)
            self.assertIs(statement["selected_command_preserved"], True)
            self.assertIs(statement["future_second_operation_may_be_considered"], True)
            self.assertIs(statement["second_operation_created"], False)
            self.assertIs(statement["continuation_created"], False)
            self.assertNotIn("future_second_operation_may_be_considered", self.non_claims(result))

    def test_successful_recorded_result_from_default_live_artifacts_if_present(self) -> None:
        request = (
            resolver.build_declared_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_request()
        )
        if not all(Path(request[key]).exists() for key in DEFAULT_SUFFIXES):
            self.skipTest("default live artifacts are not all present from current cwd")
        result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
            request
        )
        self.assert_recorded_boundary(result)
        self.assert_lineage_and_closure(result)
        boundary = self.boundary(result)
        for basis in BASIS:
            name, request_key, _object_key, basis_prefix, *_rest = basis
            self.assert_same_or_stable_artifact_path(
                boundary[f"{basis_prefix}_artifact_path"],
                request[request_key],
            )
            self.assertEqual(name, basis[0])
        for key in (
            "selected_prior_result_reentry_boundary_recorded",
            "selected_runtime_held_reentry_boundary_recorded",
            "selected_runtime_held_state_boundary_recorded",
            "selected_runtime_boundary_recorded",
            "second_operation_boundary_v1_failure_evidence_preserved",
        ):
            self.assertIs(boundary[key], True, key)

    def test_positive_basis_derivation_regression(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _artifacts, _paths = self.clean_context(
                Path(temp_dir),
                artifact_mutator=self.remove_positive_selected_object_fields,
                prefix="positive_derivation",
            )
            result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                request
            )
        self.assert_recorded_boundary(result)
        self.assert_lineage_and_closure(result)
        boundary = self.boundary(result)
        for key in (
            "selected_prior_result_reentry_boundary_recorded",
            "selected_runtime_held_reentry_boundary_recorded",
            "selected_runtime_held_state_boundary_recorded",
            "selected_runtime_boundary_recorded",
            "prior_result_cycle_v1_failure_evidence_preserved",
            "prior_result_cycle_v2_successor_evidence_preserved",
            "second_operation_boundary_v1_failure_evidence_preserved",
            "second_operation_boundary_v2_successor_evidence_preserved",
        ):
            self.assertIs(boundary[key], True, key)
        self.assertIs(self.check_by_name(result, "selected_prior_result_reentry_boundary_recorded")["actual_posture"], True)
        self.assertIs(self.check_by_name(result, "selected_runtime_held_reentry_boundary_recorded")["actual_posture"], True)
        self.assertIs(self.check_by_name(result, "selected_runtime_held_state_boundary_recorded")["actual_posture"], True)
        self.assertIs(self.check_by_name(result, "selected_runtime_boundary_recorded")["actual_posture"], True)

    def test_exact_extraction_ignores_explanatory_true_values(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, artifacts, _paths = self.clean_context(
                Path(temp_dir),
                artifact_mutator=self.add_explanatory_true_values,
                prefix="explanatory",
            )
            result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                request
            )
        self.assert_recorded_boundary(result)
        for artifact in artifacts.values():
            for key in EXACT_FORBIDDEN:
                self.assertIs(artifact["non_claims"][key], False)
        boundary = self.boundary(result)
        self.assertIs(boundary["future_second_operation_may_be_considered"], True)
        for key in EXACT_FORBIDDEN:
            self.assertIs(boundary[key], False, key)

    def test_exact_selected_object_and_exact_non_claim_true_values_block(self) -> None:
        for index, key in enumerate(EXACT_FORBIDDEN, start=1):
            with self.subTest(selected_object_key=key), tempfile.TemporaryDirectory() as temp_dir:
                def flip_object(
                    artifacts: dict[str, dict[str, Any]],
                    field: str = key,
                ) -> None:
                    self.selected_object(artifacts, "prior_result_reentry_cycle")[field] = True

                request, _artifacts, _paths = self.clean_context(
                    Path(temp_dir),
                    artifact_mutator=flip_object,
                    prefix=self.safe_json_filename(f"object_{key}", index).removesuffix(".json"),
                )
                result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                    request
                )
                self.assert_blocked_with_public_code(result)
                self.assertIn(FIELD_CODES.get(key, key.upper()), self.emitted_codes(result))

            with self.subTest(top_level_non_claim_key=key), tempfile.TemporaryDirectory() as temp_dir:
                def flip_non_claim(
                    artifacts: dict[str, dict[str, Any]],
                    field: str = key,
                ) -> None:
                    self.selected_object(artifacts, "prior_result_reentry_cycle").pop(field, None)
                    artifacts["prior_result_reentry_cycle"]["non_claims"][field] = True

                request, _artifacts, _paths = self.clean_context(
                    Path(temp_dir),
                    artifact_mutator=flip_non_claim,
                    prefix=self.safe_json_filename(f"non_claim_{key}", index).removesuffix(".json"),
                )
                result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                    request
                )
                self.assert_blocked_with_public_code(result)
                self.assertIn(FIELD_CODES.get(key, key.upper()), self.emitted_codes(result))

    def test_declared_request_blocking_and_non_claim_canonicalization(self) -> None:
        top_level_keys = (*EXACT_FORBIDDEN, *LINEAGE_FALSE)
        for key in top_level_keys:
            with self.subTest(top_level_key=key), tempfile.TemporaryDirectory() as temp_dir:
                request, _artifacts, _paths = self.clean_context(Path(temp_dir))
                request[key] = True
                result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                    request
                )
                self.assert_blocked_with_public_code(result)
                self.assertIn(FIELD_CODES.get(key, key.upper()), self.emitted_codes(result))

        with tempfile.TemporaryDirectory() as temp_dir:
            request, _artifacts, _paths = self.clean_context(Path(temp_dir))
            for key in REQ_FALSE:
                with self.subTest(declared_non_claim=key):
                    mutated = copy.deepcopy(request)
                    mutated["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                        mutated
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", self.emitted_codes(result))
                    self.assertIs(self.non_claims(result)[key], False)
            for key, value in (("second_operation_created", "false"), ("continuation_created", None)):
                with self.subTest(malformed_non_claim=key):
                    mutated = copy.deepcopy(request)
                    if value is None:
                        mutated["declared_non_claims"].pop(key)
                    else:
                        mutated["declared_non_claims"][key] = value
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                        mutated
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", self.emitted_codes(result))

    def test_representative_blocking_behavior(self) -> None:
        for request in (None, "not a mapping", {}):
            with self.subTest(request=request):
                result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(  # type: ignore[arg-type]
                    request
                )
                self.assert_blocked_with_public_code(result)

        request_cases = (
            (
                "explicit_block_intent",
                lambda request: request.update(
                    {
                        "local_relevance_medium_read_only_second_operation_boundary_intent": (
                            "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY"
                        )
                    }
                ),
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_BLOCK_REQUESTED",
            ),
            (
                "unsupported_intent",
                lambda request: request.update(
                    {"local_relevance_medium_read_only_second_operation_boundary_intent": "UNSUPPORTED"}
                ),
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY_INTENT_UNSUPPORTED",
            ),
            ("selected_command_missing", lambda request: request.pop("selected_command"), "SELECTED_COMMAND_MISSING"),
            ("selected_command_wrong", lambda request: request.update({"selected_command": "lookup"}), "SELECTED_COMMAND_NOT_STATE"),
            ("boundary_type_missing", lambda request: request.pop("boundary_type"), "BOUNDARY_TYPE_MISSING"),
            (
                "boundary_type_wrong",
                lambda request: request.update({"boundary_type": "LOCAL_RELEVANCE_MEDIUM_SECOND_OPERATION"}),
                "BOUNDARY_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_OPERATION_BOUNDARY",
            ),
            ("boundary_scope_missing", lambda request: request.pop("boundary_scope"), "BOUNDARY_SCOPE_MISSING"),
            (
                "boundary_scope_wrong",
                lambda request: request.update({"boundary_scope": "GENERAL"}),
                "BOUNDARY_SCOPE_NOT_SELECTED_SECOND_OPERATION_CONSIDERATION_ONLY",
            ),
            (
                "future_second_operation_not_considered",
                lambda request: request.update({"future_second_operation_may_be_considered": False}),
                "FUTURE_SECOND_OPERATION_MAY_NOT_BE_CONSIDERED",
            ),
        )
        for case_name, mutator, code in request_cases:
            with self.subTest(case=case_name), tempfile.TemporaryDirectory() as temp_dir:
                request, _artifacts, _paths = self.clean_context(
                    Path(temp_dir),
                    request_mutator=mutator,
                    prefix=self.safe_json_filename(case_name).removesuffix(".json"),
                )
                result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                    request
                )
                self.assert_blocked_with_public_code(result)
                self.assertIn(code, self.emitted_codes(result))

        true_posture_cases = (
            ("prior_result_reentry_cycle", "selected_prior_result_reentry_cycle_recorded", "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED"),
            ("prior_result_reentry_cycle", "prior_result_reentry_cycle_created", "PRIOR_RESULT_REENTRY_CYCLE_NOT_CREATED"),
            ("prior_result_reentry_cycle", "prior_result_reentry_cycle_local_only", "PRIOR_RESULT_REENTRY_CYCLE_NOT_LOCAL_ONLY"),
            ("prior_result_reentry_cycle", "prior_result_reentry_cycle_read_only", "PRIOR_RESULT_REENTRY_CYCLE_NOT_READ_ONLY"),
            ("prior_result_reentry_cycle", "cycle_basis_reference_only", "CYCLE_BASIS_NOT_REFERENCE_ONLY"),
            ("prior_result_reentry_boundary", "selected_prior_result_reentry_boundary_recorded", "SELECTED_PRIOR_RESULT_REENTRY_BOUNDARY_NOT_RECORDED"),
            ("prior_result_reentry_boundary", "future_prior_result_reentry_cycle_may_be_considered", "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED"),
            ("runtime_held_reentry", "runtime_held_reentry_created", "RUNTIME_HELD_REENTRY_NOT_CREATED"),
            ("runtime_held_state", "runtime_held_state_created", "RUNTIME_HELD_STATE_NOT_CREATED"),
            ("runtime", "runtime_created", "RUNTIME_NOT_CREATED"),
            ("runtime_permission", "runtime_permission_created", "RUNTIME_PERMISSION_NOT_CREATED"),
            ("operation_execution", "operation_execution_performed", "OPERATION_EXECUTION_NOT_PERFORMED"),
            ("prior_result_reentry_cycle", "runtime_v0_failure_evidence_preserved", "RUNTIME_V0_FAILURE_EVIDENCE_NOT_PRESERVED"),
        )
        for artifact_name, field, code in true_posture_cases:
            with self.subTest(artifact=artifact_name, field=field), tempfile.TemporaryDirectory() as temp_dir:
                def mutate(
                    artifacts: dict[str, dict[str, Any]],
                    name: str = artifact_name,
                    key: str = field,
                ) -> None:
                    self.selected_object(artifacts, name)[key] = False

                request, _artifacts, _paths = self.clean_context(
                    Path(temp_dir),
                    artifact_mutator=mutate,
                    prefix=self.safe_json_filename(f"{artifact_name}_{field}").removesuffix(".json"),
                )
                result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                    request
                )
                self.assert_blocked_with_public_code(result)
                self.assertIn(code, self.emitted_codes(result))

        for basis in BASIS:
            name, request_key, _object_key, _basis_prefix, block_prefix, _outcome, *_rest = basis
            cases = (
                ("path_missing", f"{block_prefix}_PATH_MISSING"),
                ("unreadable", f"{block_prefix}_UNREADABLE"),
                ("array", f"{block_prefix}_NOT_JSON_OBJECT"),
                ("not_recorded", f"{block_prefix}_NOT_RECORDED"),
                ("failed_checks", f"{block_prefix}_FAILED_CHECKS_PRESENT"),
                ("bad_version", f"{block_prefix}_VERSION_NOT_0_1_0"),
            )
            for suffix, code in cases:
                with self.subTest(artifact=name, case=suffix), tempfile.TemporaryDirectory() as temp_dir:
                    root = Path(temp_dir)
                    artifacts = self.make_artifacts()
                    paths = self.write_artifacts(
                        root,
                        artifacts,
                        prefix=self.safe_json_filename(f"{name}_{suffix}").removesuffix(".json"),
                    )
                    request = self.request_for(paths)
                    if suffix == "path_missing":
                        request.pop(request_key)
                    elif suffix == "unreadable":
                        request[request_key] = str(root / self.safe_json_filename(f"missing_{name}"))
                    elif suffix == "array":
                        array_path = root / self.safe_json_filename(f"{name}_array")
                        self.write_json(array_path, [])
                        request[request_key] = str(array_path)
                    elif suffix == "not_recorded":
                        artifacts[name]["outcome"] = "NOT_RECORDED"
                        self.write_json(paths[name], artifacts[name])
                    elif suffix == "failed_checks":
                        artifacts[name]["failed_check_count"] = 1
                        self.write_json(paths[name], artifacts[name])
                    elif suffix == "bad_version":
                        artifacts[name]["result_version"] = "9.9.9"
                        self.write_json(paths[name], artifacts[name])
                    result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIn(code, self.emitted_codes(result))

        representative_false_fields = (
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
            "artifact_existence_treated_as_second_operation_boundary_authority",
            "latest_file_posture_treated_as_second_operation_boundary_authority",
            "repo_local_availability_treated_as_second_operation_boundary_authority",
            "hidden_repo_state_used_as_second_operation_boundary_content",
            "hidden_repo_state_used_as_second_operation_boundary_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
        for field in representative_false_fields:
            with self.subTest(representative_false=field), tempfile.TemporaryDirectory() as temp_dir:
                request, _artifacts, _paths = self.clean_context(Path(temp_dir))
                request[field] = True
                result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                    request
                )
                self.assert_blocked_with_public_code(result)
                self.assertIn(FIELD_CODES.get(field, field.upper()), self.emitted_codes(result))

    def test_official_values_and_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result, _request, _artifacts, _paths = self.resolve_clean(Path(temp_dir))
            serialized = json.dumps(result, sort_keys=True)
            for official in (
                resolver.OUTCOME_RECORDED,
                BOUNDARY_TYPE,
                BOUNDARY_SCOPE,
                SELECTED_COMMAND,
                resolver.RESOLVER_MODULE,
            ):
                self.assertIn(official, serialized)
            self.assertNotIn("[REDACTED", self.boundary(result)["boundary_type"])
            self.assertNotIn("[REDACTED", self.boundary(result)["boundary_scope"])
            self.assertEqual(set(resolver.OUTCOME_FAMILY), EXPECTED_OUTCOME_FAMILY)

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request, artifacts, _paths = self.clean_context(root)
            self.inject_hostile_content(artifacts, request)
            original_artifacts = copy.deepcopy(artifacts)
            hostile_paths = self.write_artifacts(root / "hostile", artifacts, prefix="hostile")
            for basis in BASIS:
                request[basis[1]] = str(hostile_paths[basis[0]])
            original_request = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assert_blocked_with_public_code(result)
            else:
                self.assert_recorded_boundary(result)
                self.assert_lineage_and_closure(result)
            serialized = json.dumps(result, sort_keys=True)
            for sentinel in HOSTILE_SENTINELS:
                self.assertNotIn(sentinel, serialized)
            for official in (BOUNDARY_TYPE, BOUNDARY_SCOPE, SELECTED_COMMAND):
                self.assertIn(official, serialized)
            self.assertEqual(request, original_request)
            self.assertEqual(artifacts, original_artifacts)

    def test_path_write_non_mutation_and_lineage_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            result, request, artifacts, paths = self.resolve_clean(root)
            request_path = root / "request.json"
            self.write_json(request_path, request)
            from_path = (
                resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_from_path(
                    request_path
                )
            )
            self.assert_recorded_boundary(from_path)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            self.assert_blocked_with_public_code(
                resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_from_path(
                    malformed_path
                )
            )
            array_path = root / "array.json"
            self.write_json(array_path, [])
            self.assert_blocked_with_public_code(
                resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_from_path(
                    array_path
                )
            )
            self.assert_blocked_with_public_code(
                resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_from_path(
                    root / "missing.json"
                )
            )

            output_root = (
                root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                written = resolver.write_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_result(
                    result
                )
                written_again = resolver.write_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2_result(
                    result
                )
            self.assertTrue(written.exists())
            self.assertTrue(written_again.exists())
            self.assertNotEqual(written, written_again)
            self.assertIn(
                "local_relevance_medium_read_only_second_operation_boundary_v0_min_v2",
                str(written.parent),
            )
            with written.open("r", encoding="utf-8") as file:
                self.assertEqual(json.load(file)["outcome"], resolver.OUTCOME_RECORDED)
            forbidden_root_parts = {
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_operation_boundary_v0_min",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_v2",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_prior_result_reentry_boundary_v0_min",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_v0_min",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_reentry_boundary_v0_min",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_v0_min",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_held_state_boundary_v0_min",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v3",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min_v2",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_v0_min",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min_v2",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_boundary_v0_min",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_runtime_permission_v0_min",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_operation_execution_v0_min",
                "source_transfer",
                "source_receipt",
                "public_api",
                "participant_facing_interface",
                "distributed_network",
            }
            self.assertFalse(forbidden_root_parts.intersection(written.parts))

            request_before = copy.deepcopy(request)
            artifacts_before = copy.deepcopy(artifacts)
            paths_before = copy.deepcopy(paths)
            resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                request
            )
            self.assertEqual(request, request_before)
            self.assertEqual(artifacts, artifacts_before)
            self.assertEqual(paths, paths_before)

            self.assert_recorded_boundary(result)
            self.assert_lineage_and_closure(result)
            summary = self.summary(result)
            self.assertIs(summary["older_runtime_lineage_not_imported_as_authority"], True)
            self.assertIs(summary["older_runtime_permission_not_treated_as_current"], True)
            self.assertIs(summary["runtime_authority_not_imported"], True)
            self.assertIs(summary["raw_state_body_not_embedded"], True)
            self.assertIs(summary["state_mutation_not_performed"], True)
            self.assertIs(summary["state_update_not_performed"], True)
            self.assertIs(summary["future_second_operation_may_be_considered"], True)
            self.assertIs(summary["second_operation_not_created"], True)
            self.assertIs(summary["continuation_not_created"], True)

            for key in LINEAGE_FALSE:
                with self.subTest(lineage_flip=key):
                    mutated = copy.deepcopy(request)
                    mutated[key] = True
                    blocked = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                        mutated
                    )
                    self.assert_blocked_with_public_code(blocked)
                    self.assertIn(FIELD_CODES.get(key, key.upper()), self.emitted_codes(blocked))

    def test_non_mutation_for_positive_derivation_and_explanatory_payloads(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, artifacts, paths = self.clean_context(
                Path(temp_dir),
                artifact_mutator=lambda data: (
                    self.remove_positive_selected_object_fields(data),
                    self.add_explanatory_true_values(data),
                ),
                prefix="non_mutation",
            )
            original_request = copy.deepcopy(request)
            original_artifacts = copy.deepcopy(artifacts)
            original_paths = copy.deepcopy(paths)
            result = resolver.resolve_local_relevance_medium_read_only_second_operation_boundary_v0_min_v2(
                request
            )
            self.assert_recorded_boundary(result)
            self.assertEqual(request, original_request)
            self.assertEqual(artifacts, original_artifacts)
            self.assertEqual(paths, original_paths)


if __name__ == "__main__":
    unittest.main()
