"""Tests for the local read-only prior-result re-entry cycle resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE object. It verifies
that the resolver reads one clean prior-result re-entry boundary artifact, one
clean runtime-held-re-entry artifact, one clean runtime-held-re-entry boundary
artifact, one clean runtime-held-state artifact, one clean runtime-held-state
boundary artifact, one clean runtime v3 artifact, one clean runtime boundary v2
artifact, one clean runtime permission artifact, and one clean operation
execution artifact, then records one local read-only selected-state
prior-result re-entry cycle object only.

The cycle object remains selected-prior-result-reentry-cycle-only,
basis-reference-only, raw-state-body-excluding, state-mutation-refusing,
state-update-refusing, closure-token-aware, non-second-operation-shaped,
non-continuation-shaped, non-hosting-shaped, non-loop-shaped,
non-daemon-shaped, and older-runtime-authority-import-blocking.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min as resolver  # noqa: E402


CYCLE_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE"
CYCLE_SCOPE = "SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY"
SELECTED_COMMAND = "state"

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_prior_result_reentry_cycle_metadata",
    "declared_local_relevance_medium_read_only_prior_result_reentry_cycle_question",
    "selected_prior_result_reentry_boundary_artifact_basis",
    "selected_runtime_held_reentry_artifact_basis",
    "selected_runtime_held_reentry_boundary_artifact_basis",
    "selected_runtime_held_state_artifact_basis",
    "selected_runtime_held_state_boundary_artifact_basis",
    "selected_runtime_artifact_basis",
    "selected_runtime_boundary_artifact_basis",
    "selected_runtime_permission_artifact_basis",
    "selected_operation_execution_artifact_basis",
    "local_relevance_medium_read_only_prior_result_reentry_cycle",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_checks",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_statement",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_summary",
)

FORBIDDEN_CYCLE_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_checks",
    "non_claims",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_summary",
    "local_relevance_medium_read_only_prior_result_reentry_cycle_metadata",
)

CYCLE_TRUE_FIELDS = (
    "selected_command_is_state",
    "selected_prior_result_reentry_boundary_recorded",
    "future_prior_result_reentry_cycle_may_be_considered",
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
    "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded",
    "prior_result_reentry_cycle_created",
    "prior_result_reentry_cycle_local_only",
    "prior_result_reentry_cycle_read_only",
    "cycle_basis_reference_only",
    "runtime_v0_failure_evidence_preserved",
    "runtime_v2_failure_evidence_preserved",
    "runtime_boundary_v0_failure_evidence_preserved",
    "prior_result_boundary_v1_failure_evidence_preserved",
    "prior_result_boundary_v2_successor_evidence_preserved",
)

CYCLE_FALSE_FIELDS = (
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
    "raw_state_body_embedded",
    "state_mutation_performed",
    "state_update_performed",
    "consumed_request_reopened",
    "authorization_token_reused",
    "follow_on_work_authorized",
)

ARTIFACT_DEFINITIONS = (
    {
        "name": "prior_result_reentry_boundary",
        "request_key": "selected_prior_result_reentry_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_prior_result_reentry_boundary",
        "basis_prefix": "basis_prior_result_reentry_boundary",
        "block_prefix": "PRIOR_RESULT_REENTRY_BOUNDARY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_BOUNDARY_RECORDED",
        "true_fields": {
            "selected_prior_result_reentry_boundary_recorded": True,
            "local_relevance_medium_read_only_prior_result_reentry_boundary_recorded": True,
            "future_prior_result_reentry_cycle_may_be_considered": True,
        },
    },
    {
        "name": "runtime_held_reentry",
        "request_key": "selected_runtime_held_reentry_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry",
        "basis_prefix": "basis_runtime_held_reentry",
        "block_prefix": "RUNTIME_HELD_REENTRY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_RECORDED",
        "true_fields": {
            "selected_runtime_held_reentry_recorded": True,
            "local_relevance_medium_read_only_runtime_held_reentry_recorded": True,
            "runtime_held_reentry_created": True,
            "runtime_held_reentry_local_only": True,
            "runtime_held_reentry_read_only": True,
            "held_reentry_basis_reference_only": True,
        },
    },
    {
        "name": "runtime_held_reentry_boundary",
        "request_key": "selected_runtime_held_reentry_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_reentry_boundary",
        "basis_prefix": "basis_runtime_held_reentry_boundary",
        "block_prefix": "RUNTIME_HELD_REENTRY_BOUNDARY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_REENTRY_BOUNDARY_RECORDED",
        "true_fields": {
            "selected_runtime_held_reentry_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_held_reentry_boundary_recorded": True,
            "future_runtime_held_reentry_may_be_considered": True,
        },
    },
    {
        "name": "runtime_held_state",
        "request_key": "selected_runtime_held_state_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_state",
        "basis_prefix": "basis_runtime_held_state",
        "block_prefix": "RUNTIME_HELD_STATE_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_RECORDED",
        "true_fields": {
            "selected_runtime_held_state_recorded": True,
            "local_relevance_medium_read_only_runtime_held_state_recorded": True,
            "runtime_held_state_created": True,
            "runtime_held_state_local_only": True,
            "runtime_held_state_read_only": True,
            "held_state_basis_reference_only": True,
        },
    },
    {
        "name": "runtime_held_state_boundary",
        "request_key": "selected_runtime_held_state_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_held_state_boundary",
        "basis_prefix": "basis_runtime_held_state_boundary",
        "block_prefix": "RUNTIME_HELD_STATE_BOUNDARY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_HELD_STATE_BOUNDARY_RECORDED",
        "true_fields": {
            "selected_runtime_held_state_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_held_state_boundary_recorded": True,
            "future_runtime_held_state_may_be_considered": True,
        },
    },
    {
        "name": "runtime",
        "request_key": "selected_runtime_artifact",
        "object_key": "local_relevance_medium_read_only_runtime",
        "basis_prefix": "basis_runtime",
        "block_prefix": "RUNTIME_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_RECORDED",
        "true_fields": {
            "selected_runtime_recorded": True,
            "local_relevance_medium_read_only_runtime_recorded": True,
            "runtime_created": True,
            "runtime_local_only": True,
            "runtime_read_only": True,
        },
    },
    {
        "name": "runtime_boundary",
        "request_key": "selected_runtime_boundary_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_boundary",
        "basis_prefix": "basis_runtime_boundary",
        "block_prefix": "RUNTIME_BOUNDARY_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_BOUNDARY_RECORDED",
        "true_fields": {
            "selected_runtime_boundary_recorded": True,
            "local_relevance_medium_read_only_runtime_boundary_recorded": True,
            "future_runtime_may_be_considered": True,
        },
    },
    {
        "name": "runtime_permission",
        "request_key": "selected_runtime_permission_artifact",
        "object_key": "local_relevance_medium_read_only_runtime_permission",
        "basis_prefix": "basis_runtime_permission",
        "block_prefix": "RUNTIME_PERMISSION_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RUNTIME_PERMISSION_RECORDED",
        "true_fields": {
            "selected_runtime_permission_recorded": True,
            "local_relevance_medium_read_only_runtime_permission_recorded": True,
            "runtime_permission_created": True,
            "runtime_permission_local_only": True,
            "runtime_permission_read_only": True,
        },
    },
    {
        "name": "operation_execution",
        "request_key": "selected_operation_execution_artifact",
        "object_key": "local_relevance_medium_read_only_operation_execution",
        "basis_prefix": "basis_operation_execution",
        "block_prefix": "OPERATION_EXECUTION_ARTIFACT",
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_EXECUTION_RECORDED",
        "true_fields": {
            "selected_operation_execution_recorded": True,
            "local_relevance_medium_read_only_operation_execution_recorded": True,
            "operation_execution_created": True,
            "operation_execution_performed": True,
            "operation_execution_local_only": True,
            "operation_execution_read_only": True,
        },
    },
)

DEFAULT_ARTIFACT_SUFFIXES = {
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

FORBIDDEN_OUTPUT_ROOTS = (
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "prior_result_reentry_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_reentry_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_reentry_boundary_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_state_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
        "runtime_held_state_boundary_v0_min"
    ),
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

HOSTILE_SENTINELS = (
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
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_OPERATION_BODY_MUST_NOT_RETURN",
    "OLDER_RUNTIME_AUTHORITY_IMPORT_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


class LocalRelevanceMediumReadOnlyPriorResultReentryCycleV0MinTest(unittest.TestCase):
    """Bounded tests for one selected-state prior-result re-entry cycle object."""

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

    def write_json(self, path: Path, payload: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")

    def artifact_payload(
        self,
        definition: Mapping[str, Any],
        object_overrides: Mapping[str, Any] | None = None,
        top_overrides: Mapping[str, Any] | None = None,
        include_sensitive_payload: bool = False,
    ) -> dict[str, Any]:
        false_fields = {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS}
        false_fields.update({key: False for key in CYCLE_FALSE_FIELDS})
        false_fields.update(
            {
                "prior_result_reentry_cycle_created": False,
                "prior_result_reentry_cycle_local_only": False,
                "prior_result_reentry_cycle_read_only": False,
                "cycle_basis_reference_only": False,
                "source_created": False,
                "deployment_created": False,
                "public_release_created": False,
                "broader_reusable_permission_created": False,
            }
        )
        object_payload = {
            "selected_command": SELECTED_COMMAND,
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
            **false_fields,
            "runtime_v0_failure_evidence_preserved": True,
            "runtime_v2_failure_evidence_preserved": True,
            "runtime_boundary_v0_failure_evidence_preserved": True,
            "prior_result_boundary_v1_failure_evidence_preserved": True,
            "prior_result_boundary_v2_successor_evidence_preserved": True,
            **definition["true_fields"],
        }
        if object_overrides:
            object_payload.update(dict(object_overrides))
        payload = {
            "outcome": definition["outcome"],
            "result_version": resolver.RESULT_VERSION,
            "failed_check_count": 0,
            definition["object_key"]: object_payload,
            f"{definition['object_key']}_statement": copy.deepcopy(object_payload),
            f"{definition['object_key']}_summary": {
                "outcome": definition["outcome"],
                "result_version": resolver.RESULT_VERSION,
                "failed_check_count": 0,
                **definition["true_fields"],
            },
        }
        if include_sensitive_payload:
            payload["raw_body"] = HOSTILE_SENTINELS[0]
            payload["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            object_payload["raw_state_body"] = HOSTILE_SENTINELS[10]
            object_payload["raw_runtime_hosting_body"] = HOSTILE_SENTINELS[11]
            object_payload["older_runtime_authority_body"] = HOSTILE_SENTINELS[-2]
        if top_overrides:
            payload.update(dict(top_overrides))
        return payload

    def write_synthetic_artifacts(
        self,
        root: Path,
        object_overrides: Mapping[str, Mapping[str, Any]] | None = None,
        top_overrides: Mapping[str, Mapping[str, Any]] | None = None,
        include_sensitive_payload: bool = False,
    ) -> tuple[dict[str, Path], dict[str, dict[str, Any]]]:
        paths: dict[str, Path] = {}
        payloads: dict[str, dict[str, Any]] = {}
        object_overrides = object_overrides or {}
        top_overrides = top_overrides or {}
        for index, definition in enumerate(ARTIFACT_DEFINITIONS, start=1):
            path = root / self.safe_json_filename(definition["name"], index)
            payload = self.artifact_payload(
                definition,
                object_overrides=object_overrides.get(definition["name"]),
                top_overrides=top_overrides.get(definition["name"]),
                include_sensitive_payload=include_sensitive_payload,
            )
            self.write_json(path, payload)
            paths[definition["request_key"]] = path
            payloads[definition["request_key"]] = payload
        return paths, payloads

    def build_request(self, paths: Mapping[str, Path], **extra: Any) -> dict[str, Any]:
        request = resolver.build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_request(
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
        request.update(extra)
        return request

    def synthetic_request(
        self,
        root: Path,
        object_overrides: Mapping[str, Mapping[str, Any]] | None = None,
        top_overrides: Mapping[str, Mapping[str, Any]] | None = None,
        include_sensitive_payload: bool = False,
        **extra: Any,
    ) -> tuple[dict[str, Any], dict[str, Path], dict[str, dict[str, Any]]]:
        paths, payloads = self.write_synthetic_artifacts(
            root,
            object_overrides=object_overrides,
            top_overrides=top_overrides,
            include_sensitive_payload=include_sensitive_payload,
        )
        return self.build_request(paths, **extra), paths, payloads

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if isinstance(block, Mapping):
            return block.get("code") or block.get("block_code")
        return None

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        if isinstance(result.get("failed_check_count"), int):
            return int(result["failed_check_count"])
        summary = result.get(
            "local_relevance_medium_read_only_prior_result_reentry_cycle_summary",
            {},
        )
        if isinstance(summary, Mapping) and isinstance(
            summary.get("failed_check_count"), int
        ):
            return int(summary["failed_check_count"])
        checks = result.get(
            "local_relevance_medium_read_only_prior_result_reentry_cycle_checks",
            [],
        )
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is False
        )

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
        actual_path = Path(str(actual))
        expected_path = Path(str(expected))
        try:
            if actual_path.resolve() == expected_path.resolve():
                return
        except OSError:
            pass
        self.assertTrue(
            str(actual).endswith(expected_path.name)
            or str(expected).endswith(actual_path.name),
            f"{actual!r} did not match or stably end with {expected!r}",
        )

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        code = self.block_code(result)
        if code:
            self.assertIn(code, resolver.BLOCK_CODES)
        checks = result.get(
            "local_relevance_medium_read_only_prior_result_reentry_cycle_checks",
            [],
        )
        for check in checks:
            if not isinstance(check, Mapping):
                continue
            for key in ("block_code", "failure_code"):
                emitted = check.get(key)
                if emitted:
                    self.assertIn(emitted, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(type(non_claims[key]), bool)
            self.assertIs(non_claims[key], False)
        for key in (
            "prior_result_reentry_cycle_created",
            "prior_result_reentry_cycle_local_only",
            "prior_result_reentry_cycle_read_only",
            "cycle_basis_reference_only",
        ):
            self.assertNotIn(key, non_claims)

    def assert_prior_result_reentry_cycle_non_claims(
        self, result: Mapping[str, Any]
    ) -> None:
        cycle = result.get("local_relevance_medium_read_only_prior_result_reentry_cycle")
        self.assertIsInstance(cycle, dict)
        for key in CYCLE_FALSE_FIELDS:
            self.assertIs(cycle.get(key), False, key)
        self.assertIs(cycle.get("raw_state_body_embedded"), False)
        self.assertIs(cycle.get("state_mutation_performed"), False)
        self.assertIs(cycle.get("state_update_performed"), False)
        self.assertIs(cycle.get("second_operation_created"), False)
        self.assertIs(cycle.get("continuation_created"), False)
        self.assertIs(cycle.get("runtime_hosting_created"), False)
        self.assertIs(cycle.get("runtime_loop_created"), False)
        self.assertIs(cycle.get("daemon_behavior_created"), False)
        self.assertIs(cycle.get("older_runtime_lineage_imported_as_authority"), False)
        self.assertIs(cycle.get("older_runtime_permission_treated_as_current"), False)
        self.assertIs(cycle.get("runtime_authority_imported"), False)
        self.assertIs(cycle.get("follow_on_work_authorized"), False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_prior_result_reentry_cycle_non_claims(result)

    def assert_cycle_not_wrapper(self, cycle: Mapping[str, Any]) -> None:
        for key in FORBIDDEN_CYCLE_WRAPPER_FIELDS:
            self.assertNotIn(key, cycle)

    def assert_failure_lineage_preserved(self, result: Mapping[str, Any]) -> None:
        cycle = result["local_relevance_medium_read_only_prior_result_reentry_cycle"]
        summary = resolver.build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_summary(
            result
        )
        for key in (
            "runtime_v0_failure_evidence_preserved",
            "runtime_v2_failure_evidence_preserved",
            "runtime_boundary_v0_failure_evidence_preserved",
            "prior_result_boundary_v1_failure_evidence_preserved",
            "prior_result_boundary_v2_successor_evidence_preserved",
        ):
            self.assertIs(cycle.get(key), True)
            self.assertIs(summary.get(key), True)
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
            "prior_result_boundary_v1_failure_repaired",
            "prior_result_boundary_v1_failure_hidden",
            "prior_result_boundary_v1_failure_claimed_passed",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertIs(result["non_claims"][key], False)
        self.assertIs(summary.get("predecessor_failure_evidence_preserved"), True)
        self.assertIs(summary.get("result_level_non_claims_canonical_false"), True)

    def assert_recorded_result(
        self,
        result: Mapping[str, Any],
        paths: Mapping[str, Path] | None = None,
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertEqual(result["result_version"], "0.1.0")
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(result.get("passed_check_count", 0), 0)
        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        cycle = result["local_relevance_medium_read_only_prior_result_reentry_cycle"]
        self.assertEqual(
            cycle["cycle_id"],
            "local_relevance_medium_read_only_prior_result_reentry_cycle_001",
        )
        self.assertEqual(cycle["cycle_type"], CYCLE_TYPE)
        self.assertEqual(cycle["cycle_version"], "0.1.0")
        self.assertEqual(cycle["cycle_scope"], CYCLE_SCOPE)
        self.assertEqual(cycle["selected_command"], SELECTED_COMMAND)
        self.assert_cycle_not_wrapper(cycle)
        for definition in ARTIFACT_DEFINITIONS:
            prefix = definition["basis_prefix"]
            self.assertEqual(cycle[f"{prefix}_outcome"], definition["outcome"])
            self.assertEqual(cycle[f"{prefix}_result_version"], "0.1.0")
            self.assertEqual(cycle[f"{prefix}_failed_check_count"], 0)
            if paths is not None:
                self.assert_same_or_stable_artifact_path(
                    cycle[f"{prefix}_artifact"],
                    paths[definition["request_key"]],
                )
        for key in CYCLE_TRUE_FIELDS:
            self.assertIs(cycle.get(key), True, key)
        for key in CYCLE_FALSE_FIELDS:
            self.assertIs(cycle.get(key), False, key)
        self.assert_canonical_false_non_claims(result)
        self.assert_prior_result_reentry_cycle_non_claims(result)
        self.assert_failure_lineage_preserved(result)

        statement = result["local_relevance_medium_read_only_prior_result_reentry_cycle_statement"]
        for key in (
            "local_relevance_medium_read_only_prior_result_reentry_cycle_recorded",
            "basis_prior_result_reentry_boundary_artifact_preserved",
            "basis_runtime_held_reentry_artifact_preserved",
            "basis_runtime_held_reentry_boundary_artifact_preserved",
            "basis_runtime_held_state_artifact_preserved",
            "basis_runtime_held_state_boundary_artifact_preserved",
            "basis_runtime_artifact_preserved",
            "basis_runtime_boundary_artifact_preserved",
            "basis_runtime_permission_artifact_preserved",
            "basis_operation_execution_artifact_preserved",
            "selected_command_preserved",
            "selected_command_is_state",
            "prior_result_reentry_cycle_created",
            "prior_result_reentry_cycle_local_only",
            "prior_result_reentry_cycle_read_only",
            "cycle_basis_reference_only",
            "runtime_v0_failure_evidence_preserved",
            "runtime_v2_failure_evidence_preserved",
            "runtime_boundary_v0_failure_evidence_preserved",
            "prior_result_boundary_v1_failure_evidence_preserved",
            "prior_result_boundary_v2_successor_evidence_preserved",
            "consumed_request_token_remains_closed",
            "authorization_token_reuse_blocked",
            "predecessor_failure_evidence_preserved",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(statement.get(key), True, key)
        self.assertIs(statement.get("second_operation_created"), False)
        self.assertIs(statement.get("continuation_created"), False)

    def default_path(self, path_value: str) -> Path:
        path = Path(path_value)
        return path if path.is_absolute() else REPO_ROOT / path

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min",
            "resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_from_path",
            "write_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_result",
            "build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_CYCLE_TYPE_VALUES",
            "SUPPORTED_CYCLE_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min",
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
                "prior_result_reentry_cycle_v0_min"
            )
        )
        self.assertIn(CYCLE_TYPE, resolver.SUPPORTED_CYCLE_TYPE_VALUES)
        self.assertIn(CYCLE_SCOPE, resolver.SUPPORTED_CYCLE_SCOPE_VALUES)
        self.assertEqual(resolver.SELECTED_COMMAND, SELECTED_COMMAND)
        for key in (
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
            "prior_result_boundary_v1_failure_repaired",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in (
            "prior_result_reentry_cycle_created",
            "prior_result_reentry_cycle_local_only",
            "prior_result_reentry_cycle_read_only",
            "cycle_basis_reference_only",
        ):
            self.assertNotIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
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
            "RUNTIME_V0_FAILURE_REPAIRED",
            "RUNTIME_V2_FAILURE_REPAIRED",
            "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
            "PRIOR_RESULT_BOUNDARY_V1_FAILURE_REPAIRED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_BLOCKED",
            },
        )

        request = resolver.build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_request()
        for key, suffix in DEFAULT_ARTIFACT_SUFFIXES.items():
            self.assertTrue(str(request[key]).endswith(suffix), key)
        self.assertEqual(request["selected_command"], SELECTED_COMMAND)
        for key in (
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
            "prior_result_boundary_v1_failure_repaired",
            "prior_result_boundary_v1_failure_hidden",
            "prior_result_boundary_v1_failure_claimed_passed",
        ):
            self.assertIs(request["declared_non_claims"][key], False)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, paths, _payloads = self.synthetic_request(Path(directory))
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                request
            )
            self.assert_recorded_result(result, paths)
            cycle = result["local_relevance_medium_read_only_prior_result_reentry_cycle"]
            for key in (
                "prior_result_reentry_cycle_created",
                "prior_result_reentry_cycle_local_only",
                "prior_result_reentry_cycle_read_only",
                "cycle_basis_reference_only",
            ):
                self.assertIs(cycle[key], True)
                self.assertNotIn(key, result["non_claims"])

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        request = resolver.build_declared_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_request()
        missing = [
            str(self.default_path(request[key]))
            for key in DEFAULT_ARTIFACT_SUFFIXES
            if not self.default_path(request[key]).exists()
        ]
        if missing:
            self.skipTest("default live artifacts not present: " + ", ".join(missing))
        result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
            request
        )
        self.assert_recorded_result(result)
        cycle = result["local_relevance_medium_read_only_prior_result_reentry_cycle"]
        for key in DEFAULT_ARTIFACT_SUFFIXES:
            definition = next(
                item for item in ARTIFACT_DEFINITIONS if item["request_key"] == key
            )
            self.assert_same_or_stable_artifact_path(
                cycle[f"{definition['basis_prefix']}_artifact"],
                request[key],
            )

    def test_top_level_blocking_exact_public_codes(self) -> None:
        cases = (
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
            ("raw_state_body_embedded", "RAW_STATE_BODY_EMBEDDED"),
            ("state_mutation_performed", "STATE_MUTATION_PERFORMED"),
            ("state_update_performed", "STATE_UPDATE_PERFORMED"),
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
            (
                "runtime_boundary_v0_failure_claimed_passed",
                "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
            ),
            (
                "prior_result_boundary_v1_failure_repaired",
                "PRIOR_RESULT_BOUNDARY_V1_FAILURE_REPAIRED",
            ),
            (
                "prior_result_boundary_v1_failure_hidden",
                "PRIOR_RESULT_BOUNDARY_V1_FAILURE_HIDDEN",
            ),
            (
                "prior_result_boundary_v1_failure_claimed_passed",
                "PRIOR_RESULT_BOUNDARY_V1_FAILURE_CLAIMED_PASSED",
            ),
        )
        with tempfile.TemporaryDirectory() as directory:
            for key, expected_code in cases:
                with self.subTest(key=key):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request[key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assertIs(result["non_claims"][key], False)

                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][key], False)

                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request["declared_non_claims"].pop(key)
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request["declared_non_claims"][key] = "false"
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_required_non_claim_canonicalization_blocks_flipped_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            clean_request, _paths, _payloads = self.synthetic_request(Path(directory))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_prior_result_reentry_cycle_non_claims(result)

    def test_representative_blocking_behavior(self) -> None:
        scalar_cases = (
            (
                "explicit block intent",
                lambda request: request.update(
                    {
                        "local_relevance_medium_read_only_prior_result_reentry_cycle_intent": resolver.INTENT_BLOCK
                    }
                ),
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_BLOCK_REQUESTED",
            ),
            (
                "unsupported intent",
                lambda request: request.update(
                    {
                        "local_relevance_medium_read_only_prior_result_reentry_cycle_intent": "UNSUPPORTED"
                    }
                ),
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_INTENT_UNSUPPORTED",
            ),
            ("selected command missing", lambda request: request.pop("selected_command"), "SELECTED_COMMAND_MISSING"),
            (
                "selected command not state",
                lambda request: request.update({"selected_command": "status"}),
                "SELECTED_COMMAND_NOT_STATE",
            ),
            ("cycle type missing", lambda request: request.pop("cycle_type"), "CYCLE_TYPE_MISSING"),
            (
                "cycle type wrong",
                lambda request: request.update({"cycle_type": "LOCAL_RELEVANCE_MEDIUM_SECOND_OPERATION"}),
                "CYCLE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE",
            ),
            ("cycle scope missing", lambda request: request.pop("cycle_scope"), "CYCLE_SCOPE_MISSING"),
            (
                "cycle scope wrong",
                lambda request: request.update({"cycle_scope": "SECOND_OPERATION"}),
                "CYCLE_SCOPE_NOT_SELECTED_PRIOR_RESULT_REENTRY_CYCLE_ONLY",
            ),
            (
                "cycle not recorded shortcut",
                lambda request: request.update(
                    {
                        "local_relevance_medium_read_only_prior_result_reentry_cycle_not_recorded": True
                    }
                ),
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_NOT_RECORDED",
            ),
            (
                "cycle not created shortcut",
                lambda request: request.update({"prior_result_reentry_cycle_not_created": True}),
                "PRIOR_RESULT_REENTRY_CYCLE_NOT_CREATED",
            ),
            (
                "cycle not local shortcut",
                lambda request: request.update(
                    {"prior_result_reentry_cycle_local_only_not_true": True}
                ),
                "PRIOR_RESULT_REENTRY_CYCLE_LOCAL_ONLY_NOT_TRUE",
            ),
            (
                "cycle not read only shortcut",
                lambda request: request.update(
                    {"prior_result_reentry_cycle_read_only_not_true": True}
                ),
                "PRIOR_RESULT_REENTRY_CYCLE_READ_ONLY_NOT_TRUE",
            ),
            (
                "cycle basis not reference only shortcut",
                lambda request: request.update({"cycle_basis_reference_only_not_true": True}),
                "CYCLE_BASIS_REFERENCE_ONLY_NOT_TRUE",
            ),
            (
                "required non-claim missing",
                lambda request: request["declared_non_claims"].pop(
                    "second_operation_created"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "predecessor failure repaired",
                lambda request: request.update({"predecessor_failure_repaired": True}),
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
        )
        with tempfile.TemporaryDirectory() as directory:
            for name, mutate, expected_code in scalar_cases:
                with self.subTest(name=name):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min()
            self.assert_blocked_with_public_code(result)
            self.assertEqual(
                self.block_code(result),
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_QUESTION_UNDECLARED",
            )
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                ["not", "a", "mapping"]  # type: ignore[arg-type]
            )
            self.assert_blocked_with_public_code(result)
            self.assertEqual(
                self.block_code(result),
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_PRIOR_RESULT_REENTRY_CYCLE_REQUEST_MALFORMED",
            )

            for definition in ARTIFACT_DEFINITIONS:
                request, _paths, _payloads = self.synthetic_request(Path(directory))
                request.pop(definition["request_key"])
                result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                    request
                )
                self.assert_blocked_with_public_code(result)
                self.assertEqual(
                    self.block_code(result), f"{definition['block_prefix']}_PATH_MISSING"
                )

                request, _paths, _payloads = self.synthetic_request(Path(directory))
                request[definition["request_key"]] = str(
                    Path(directory) / self.safe_json_filename(definition["name"] + " missing")
                )
                result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                    request
                )
                self.assert_blocked_with_public_code(result)
                self.assertEqual(
                    self.block_code(result), f"{definition['block_prefix']}_UNREADABLE"
                )

                request, paths, _payloads = self.synthetic_request(Path(directory))
                self.write_json(paths[definition["request_key"]], ["not", "object"])
                result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                    request
                )
                self.assert_blocked_with_public_code(result)
                self.assertEqual(
                    self.block_code(result), f"{definition['block_prefix']}_NOT_JSON_OBJECT"
                )

                for suffix, top_override in (
                    ("not recorded", {"outcome": "NOT_RECORDED"}),
                    ("failed checks", {"failed_check_count": 1}),
                    ("wrong version", {"result_version": "0.2.0"}),
                ):
                    request, paths, _payloads = self.synthetic_request(Path(directory))
                    payload = self.artifact_payload(
                        definition,
                        top_overrides=top_override,
                    )
                    self.write_json(
                        paths[definition["request_key"]],
                        payload,
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    expected = {
                        "not recorded": f"{definition['block_prefix']}_NOT_RECORDED",
                        "failed checks": f"{definition['block_prefix']}_FAILED_CHECKS_PRESENT",
                        "wrong version": f"{definition['block_prefix']}_VERSION_NOT_0_1_0",
                    }[suffix]
                    self.assertEqual(self.block_code(result), expected)

            true_field_cases = (
                ("prior_result_reentry_boundary", "selected_prior_result_reentry_boundary_recorded", "SELECTED_PRIOR_RESULT_REENTRY_BOUNDARY_NOT_RECORDED"),
                ("prior_result_reentry_boundary", "future_prior_result_reentry_cycle_may_be_considered", "FUTURE_PRIOR_RESULT_REENTRY_CYCLE_MAY_NOT_BE_CONSIDERED"),
                ("runtime_held_reentry", "runtime_held_reentry_created", "RUNTIME_HELD_REENTRY_NOT_CREATED"),
                ("runtime_held_reentry", "runtime_held_reentry_local_only", "RUNTIME_HELD_REENTRY_LOCAL_ONLY_NOT_TRUE"),
                ("runtime_held_reentry", "runtime_held_reentry_read_only", "RUNTIME_HELD_REENTRY_READ_ONLY_NOT_TRUE"),
                ("runtime_held_reentry", "held_reentry_basis_reference_only", "HELD_REENTRY_BASIS_REFERENCE_ONLY_NOT_TRUE"),
                ("runtime_held_reentry_boundary", "future_runtime_held_reentry_may_be_considered", "FUTURE_RUNTIME_HELD_REENTRY_MAY_NOT_BE_CONSIDERED"),
                ("runtime_held_state", "runtime_held_state_created", "RUNTIME_HELD_STATE_NOT_CREATED"),
                ("runtime_held_state", "runtime_held_state_local_only", "RUNTIME_HELD_STATE_LOCAL_ONLY_NOT_TRUE"),
                ("runtime_held_state", "runtime_held_state_read_only", "RUNTIME_HELD_STATE_READ_ONLY_NOT_TRUE"),
                ("runtime_held_state", "held_state_basis_reference_only", "HELD_STATE_BASIS_REFERENCE_ONLY_NOT_TRUE"),
                ("runtime_held_state_boundary", "future_runtime_held_state_may_be_considered", "FUTURE_RUNTIME_HELD_STATE_MAY_NOT_BE_CONSIDERED"),
                ("runtime", "runtime_created", "RUNTIME_NOT_CREATED"),
                ("runtime", "runtime_local_only", "RUNTIME_LOCAL_ONLY_NOT_TRUE"),
                ("runtime", "runtime_read_only", "RUNTIME_READ_ONLY_NOT_TRUE"),
                ("runtime_boundary", "future_runtime_may_be_considered", "FUTURE_RUNTIME_MAY_NOT_BE_CONSIDERED"),
                ("runtime_permission", "runtime_permission_created", "RUNTIME_PERMISSION_NOT_CREATED"),
                ("runtime_permission", "runtime_permission_local_only", "RUNTIME_PERMISSION_LOCAL_ONLY_NOT_TRUE"),
                ("runtime_permission", "runtime_permission_read_only", "RUNTIME_PERMISSION_READ_ONLY_NOT_TRUE"),
                ("operation_execution", "operation_execution_created", "OPERATION_EXECUTION_NOT_CREATED"),
                ("operation_execution", "operation_execution_performed", "OPERATION_EXECUTION_NOT_PERFORMED"),
                ("operation_execution", "operation_execution_local_only", "OPERATION_EXECUTION_LOCAL_ONLY_NOT_TRUE"),
                ("operation_execution", "operation_execution_read_only", "OPERATION_EXECUTION_READ_ONLY_NOT_TRUE"),
            )
            for artifact_name, field, expected_code in true_field_cases:
                with self.subTest(artifact=artifact_name, field=field):
                    request, _paths, _payloads = self.synthetic_request(
                        Path(directory),
                        object_overrides={artifact_name: {field: False}},
                    )
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

            for field in (
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
                "artifact_existence_treated_as_prior_result_reentry_cycle_authority",
                "latest_file_posture_treated_as_prior_result_reentry_cycle_authority",
                "repo_local_availability_treated_as_prior_result_reentry_cycle_authority",
                "hidden_repo_state_used_as_prior_result_reentry_cycle_content",
                "hidden_repo_state_used_as_prior_result_reentry_cycle_authority",
            ):
                with self.subTest(top_level_false_field=field):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request[field] = True
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _paths, _payloads = self.synthetic_request(Path(directory))
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                request
            )
            self.assert_recorded_result(result)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn(CYCLE_TYPE, serialized)
            self.assertIn(CYCLE_SCOPE, serialized)
            self.assertIn(SELECTED_COMMAND, serialized)
            self.assertIn(resolver.OUTCOME_RECORDED, serialized)
            self.assertIn(resolver.RESOLVER_MODULE, serialized)
            self.assertIn(CYCLE_TYPE, result["local_relevance_medium_read_only_prior_result_reentry_cycle"]["cycle_type"])
            self.assertIn(CYCLE_SCOPE, result["local_relevance_medium_read_only_prior_result_reentry_cycle"]["cycle_scope"])
            self.assertEqual(
                set(resolver.OUTCOME_FAMILY),
                {
                    resolver.OUTCOME_RECORDED,
                    resolver.OUTCOME_NOT_RECORDED,
                    resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                    resolver.OUTCOME_BLOCKED,
                },
            )
            self.assertNotIn("[REDACTED_RAW_BODY_CONTENT]", result["outcome"])
            self.assertNotIn("[REDACTED_RAW_BODY_CONTENT]", serialized.split(CYCLE_TYPE)[0])

    def test_raw_hidden_and_older_runtime_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _paths, _payloads = self.synthetic_request(
                Path(directory),
                include_sensitive_payload=True,
                additional_fields={
                    "raw_prior_result_reentry_cycle_body": HOSTILE_SENTINELS[0],
                    "hidden_repo_state": HOSTILE_SENTINELS[-1],
                    "raw_second_operation_body": HOSTILE_SENTINELS[15],
                },
            )
            original_request = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            serialized = json.dumps(result, sort_keys=True)
            for sentinel in HOSTILE_SENTINELS:
                self.assertNotIn(sentinel, serialized)
            self.assertIn(CYCLE_TYPE, serialized)
            self.assertIn(CYCLE_SCOPE, serialized)
            self.assertIn(SELECTED_COMMAND, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assert_prior_result_reentry_cycle_non_claims(result)
            self.assertEqual(request, original_request)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request, _paths, _payloads = self.synthetic_request(root)
            request_path = root / "request.json"
            self.write_json(request_path, request)
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_from_path(
                request_path
            )
            self.assert_recorded_result(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_with_public_code(malformed_result)

            array_path = root / "array.json"
            self.write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_from_path(
                array_path
            )
            self.assert_blocked_with_public_code(array_result)

            missing_result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_from_path(
                root / "missing.json"
            )
            self.assert_blocked_with_public_code(missing_result)

            output_root = root / resolver.OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_result(
                    result
                )
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            with first_path.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn(
                "local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min",
                str(first_path),
            )
            actual_parent = first_path.parent.resolve()
            for forbidden in FORBIDDEN_OUTPUT_ROOTS:
                self.assertNotEqual(actual_parent, (root / forbidden).resolve())

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, paths, payloads = self.synthetic_request(
                Path(directory),
                include_sensitive_payload=True,
                additional_fields={"raw_runtime_body": HOSTILE_SENTINELS[6]},
            )
            request_before = copy.deepcopy(request)
            paths_before = copy.deepcopy(paths)
            payloads_before = copy.deepcopy(payloads)
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                request
            )
            self.assertEqual(request, request_before)
            self.assertEqual(paths, paths_before)
            self.assertEqual(payloads, payloads_before)
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)

    def test_failure_lineage_and_predecessor_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _paths, _payloads = self.synthetic_request(Path(directory))
            result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                request
            )
            self.assert_recorded_result(result)
            summary = resolver.build_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min_summary(
                result
            )
            self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
            self.assertIs(summary["result_level_non_claims_canonical_false"], True)
            self.assertIs(summary["consumed_request_reopened"], False)
            self.assertIs(summary["authorization_token_reused"], False)
            self.assertIs(summary["raw_state_body_embedded"], False)
            self.assertIs(summary["state_mutation_performed"], False)
            self.assertIs(summary["state_update_performed"], False)
            self.assertIs(summary["second_operation_created"], False)
            self.assertIs(summary["continuation_created"], False)
            self.assertIs(
                summary["cycle_object_summary"]["prior_result_reentry_cycle_created"],
                True,
            )
            self.assertIs(
                summary["cycle_object_summary"]["prior_result_reentry_cycle_local_only"],
                True,
            )
            self.assertIs(
                summary["cycle_object_summary"]["prior_result_reentry_cycle_read_only"],
                True,
            )
            self.assertIs(
                summary["cycle_object_summary"]["cycle_basis_reference_only"],
                True,
            )

            flip_cases = {
                "runtime_v0_failure_repaired": "RUNTIME_V0_FAILURE_REPAIRED",
                "runtime_v0_failure_hidden": "RUNTIME_V0_FAILURE_HIDDEN",
                "runtime_v0_failure_claimed_passed": "RUNTIME_V0_FAILURE_CLAIMED_PASSED",
                "runtime_v2_failure_repaired": "RUNTIME_V2_FAILURE_REPAIRED",
                "runtime_v2_failure_hidden": "RUNTIME_V2_FAILURE_HIDDEN",
                "runtime_v2_failure_claimed_passed": "RUNTIME_V2_FAILURE_CLAIMED_PASSED",
                "runtime_boundary_v0_failure_repaired": "RUNTIME_BOUNDARY_V0_FAILURE_REPAIRED",
                "runtime_boundary_v0_failure_hidden": "RUNTIME_BOUNDARY_V0_FAILURE_HIDDEN",
                "runtime_boundary_v0_failure_claimed_passed": "RUNTIME_BOUNDARY_V0_FAILURE_CLAIMED_PASSED",
                "prior_result_boundary_v1_failure_repaired": "PRIOR_RESULT_BOUNDARY_V1_FAILURE_REPAIRED",
                "prior_result_boundary_v1_failure_hidden": "PRIOR_RESULT_BOUNDARY_V1_FAILURE_HIDDEN",
                "prior_result_boundary_v1_failure_claimed_passed": "PRIOR_RESULT_BOUNDARY_V1_FAILURE_CLAIMED_PASSED",
            }
            for key, expected_code in flip_cases.items():
                with self.subTest(key=key):
                    request, _paths, _payloads = self.synthetic_request(Path(directory))
                    request[key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_prior_result_reentry_cycle_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)


if __name__ == "__main__":
    unittest.main()
