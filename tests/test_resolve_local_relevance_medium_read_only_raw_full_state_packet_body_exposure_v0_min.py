"""Tests for the local read-only raw/full state packet body exposure resolver.

This suite is bounded to one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE object. It
verifies that the resolver reads one clean raw/full state packet body exposure
boundary artifact and one clean selected-state packet body exposure artifact,
records one local read-only selected-state raw/full packet-body exposure event,
and keeps lookup, lookup command execution, operation permission, runtime
permission, public/distributed surfaces, registry/search/query/ranking,
filesystem discovery, source transfer, participation, and follow-on work out of
the object and result-level posture.
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

import resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min as resolver  # noqa: E402


DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "raw_full_state_packet_body_exposure_boundary_v0_min/"
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_"
    "reference_review_001__local_relevance_medium_read_only_raw_full_state_packet_"
    "body_exposure_boundary_v0_min_result.json"
)
DEFAULT_STATE_PACKET_BODY_EXPOSURE_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_packet_body_exposure_v0_min/"
    "local_relevance_medium_read_only_state_packet_body_exposure_reference_review_001__"
    "local_relevance_medium_read_only_state_packet_body_exposure_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "raw_full_state_packet_body_exposure_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_packet_body_exposure_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min_v2"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_result_object_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_result_object_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_payload_return_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_payload_return_boundary_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_transfer_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_source_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_public_api_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_participant_facing_interface_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_distributed_network_behavior_v0_min"),
)

EXPECTED_WRAPPER_SECTIONS = (
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_metadata",
    "declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_question",
    "selected_raw_full_state_packet_body_exposure_boundary_artifact_basis",
    "selected_state_packet_body_exposure_artifact_basis",
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure",
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_checks",
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_statement",
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_summary",
)

FORBIDDEN_EXPOSURE_WRAPPER_FIELDS = (
    "outcome",
    "block",
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_checks",
    "non_claims",
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_summary",
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_metadata",
)

RAW_FULL_EXPOSURE_OBJECT_FALSE_FIELDS = (
    "lookup_performed",
    "lookup_command_executed",
    "operation_permission_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_commands_permitted",
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
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "consumed_request_reopened",
    "authorization_token_reused",
    "follow_on_work_authorized",
)

BOUNDARY_FALSE_FIELDS = (
    "raw_full_state_packet_body_exposed",
    "lookup_performed",
    "lookup_command_executed",
    "operation_permission_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_commands_permitted",
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
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "consumed_request_reopened",
    "authorization_token_reused",
    "follow_on_work_authorized",
)

STATE_PACKET_EXPOSURE_FALSE_FIELDS = (
    "raw_full_state_packet_body_exposed",
    "lookup_performed",
    "lookup_command_executed",
    "operation_permission_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_commands_permitted",
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
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "consumed_request_reopened",
    "authorization_token_reused",
    "follow_on_work_authorized",
)

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded",
    "basis_raw_full_state_packet_body_exposure_boundary_artifact_preserved",
    "basis_state_packet_body_exposure_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_state_packet_body_exposure_recorded",
    "state_packet_body_exposed",
    "state_packet_body_exposure_local_only",
    "state_packet_body_exposure_read_only",
    "raw_full_state_packet_body_exposed",
    "raw_full_state_packet_body_exposure_local_only",
    "raw_full_state_packet_body_exposure_read_only",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_OBJECT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _path_has_component_prefix(candidate: Path | str, root: Path | str) -> bool:
    candidate_parts = Path(candidate).parts
    root_parts = Path(root).parts
    if not root_parts or len(root_parts) > len(candidate_parts):
        return False
    return any(
        candidate_parts[index : index + len(root_parts)] == root_parts
        for index in range(0, len(candidate_parts) - len(root_parts) + 1)
    )


def _set(mapping: dict[str, Any], key: str, value: Any) -> None:
    mapping[key] = value


def _pop(mapping: dict[str, Any], key: str) -> None:
    mapping.pop(key, None)


def _clean_raw_full_boundary_artifact(
    *,
    boundary_overrides: Mapping[str, Any] | None = None,
    summary_overrides: Mapping[str, Any] | None = None,
    metadata_overrides: Mapping[str, Any] | None = None,
    statement_overrides: Mapping[str, Any] | None = None,
    artifact_overrides: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    boundary = {
        "boundary_id": "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_001",
        "boundary_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY",
        "boundary_version": "0.1.0",
        "boundary_scope": "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY",
        "basis_state_packet_body_exposure_artifact": "synthetic_state_packet_body_exposure.json",
        "basis_state_packet_body_exposure_outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_RECORDED",
        "basis_state_packet_body_exposure_result_version": "0.1.0",
        "basis_state_packet_body_exposure_failed_check_count": 0,
        "selected_command": "state",
        "selected_command_is_state": True,
        "selected_state_packet_body_exposure_recorded": True,
        "state_packet_body_exposed": True,
        "state_packet_body_exposure_local_only": True,
        "state_packet_body_exposure_read_only": True,
        "future_raw_full_state_packet_body_exposure_may_be_considered": True,
    }
    for field in BOUNDARY_FALSE_FIELDS:
        boundary[field] = False
    if boundary_overrides:
        boundary.update(dict(boundary_overrides))

    summary = {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED",
        "failed_check_count": 0,
        "passed_check_count": 82,
        "result_version": "0.1.0",
        "resolver_module": "resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_v0_min",
        "selected_command": "state",
        "selected_command_is_state": True,
        "selected_state_packet_body_exposure_recorded": True,
        "state_packet_body_exposed": True,
        "state_packet_body_exposure_local_only": True,
        "state_packet_body_exposure_read_only": True,
        "future_raw_full_state_packet_body_exposure_may_be_considered": True,
        "raw_full_state_packet_body_exposed": False,
        "lookup_performed": False,
        "lookup_command_executed": False,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
        "predecessor_failure_evidence_preserved": True,
    }
    if summary_overrides:
        summary.update(dict(summary_overrides))

    metadata = {
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_id": boundary[
            "boundary_id"
        ],
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_version": "0.1.0",
        "resolver_module": "resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_v0_min",
    }
    if metadata_overrides:
        metadata.update(dict(metadata_overrides))

    statement = {
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_recorded": True,
        "basis_state_packet_body_exposure_artifact_preserved": True,
        "selected_command_preserved": True,
        "selected_command_is_state": True,
        "selected_state_packet_body_exposure_recorded": True,
        "state_packet_body_exposed": True,
        "state_packet_body_exposure_local_only": True,
        "state_packet_body_exposure_read_only": True,
        "future_raw_full_state_packet_body_exposure_may_be_considered": True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": True,
    }
    if statement_overrides:
        statement.update(dict(statement_overrides))

    artifact = {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED",
        "result_version": "0.1.0",
        "failed_check_count": 0,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_metadata": metadata,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary": boundary,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_checks": [
            {
                "check_name": "synthetic raw full boundary clean",
                "passed": True,
                "expected_posture": "clean raw/full boundary",
                "actual_posture": "clean raw/full boundary",
                "block_code": None,
                "failure_code": None,
            }
        ],
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_statement": statement,
        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_summary": summary,
        "non_claims": {key: False for key in BOUNDARY_FALSE_FIELDS},
        "block": {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        },
    }
    if artifact_overrides:
        artifact.update(dict(artifact_overrides))
    return artifact


def _clean_state_packet_body_exposure_artifact(
    *,
    exposure_overrides: Mapping[str, Any] | None = None,
    summary_overrides: Mapping[str, Any] | None = None,
    metadata_overrides: Mapping[str, Any] | None = None,
    statement_overrides: Mapping[str, Any] | None = None,
    artifact_overrides: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    exposure = {
        "state_packet_body_exposure_id": "local_relevance_medium_read_only_state_packet_body_exposure_001",
        "state_packet_body_exposure_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE",
        "state_packet_body_exposure_version": "0.1.0",
        "state_packet_body_exposure_scope": "SELECTED_STATE_PACKET_BODY_EXPOSURE_ONLY",
        "selected_command": "state",
        "selected_command_is_state": True,
        "local_relevance_medium_read_only_state_packet_body_exposure_recorded": True,
        "selected_state_packet_body_exposure_recorded": True,
        "state_packet_body_exposed": True,
        "state_packet_body_exposure_local_only": True,
        "state_packet_body_exposure_read_only": True,
    }
    for field in STATE_PACKET_EXPOSURE_FALSE_FIELDS:
        exposure[field] = False
    if exposure_overrides:
        exposure.update(dict(exposure_overrides))

    summary = {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_RECORDED",
        "failed_check_count": 0,
        "passed_check_count": 90,
        "result_version": "0.1.0",
        "resolver_module": "resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min",
        "selected_command": "state",
        "selected_command_is_state": True,
        "selected_state_packet_body_exposure_recorded": True,
        "state_packet_body_exposure_recorded": True,
        "state_packet_body_exposed": True,
        "state_packet_body_exposure_local_only": True,
        "state_packet_body_exposure_read_only": True,
    }
    if summary_overrides:
        summary.update(dict(summary_overrides))

    metadata = {
        "local_relevance_medium_read_only_state_packet_body_exposure_id": "local_relevance_medium_read_only_state_packet_body_exposure_001",
        "local_relevance_medium_read_only_state_packet_body_exposure_type": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE",
        "local_relevance_medium_read_only_state_packet_body_exposure_version": "0.1.0",
        "resolver_module": "resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min",
    }
    if metadata_overrides:
        metadata.update(dict(metadata_overrides))

    statement = {
        "local_relevance_medium_read_only_state_packet_body_exposure_recorded": True,
        "selected_command_preserved": True,
        "selected_command_is_state": True,
        "selected_state_packet_body_exposure_recorded": True,
        "state_packet_body_exposed": True,
        "state_packet_body_exposure_local_only": True,
        "state_packet_body_exposure_read_only": True,
        "result_level_non_claims_canonical_false": True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
    }
    if statement_overrides:
        statement.update(dict(statement_overrides))

    artifact = {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_RECORDED",
        "result_version": "0.1.0",
        "failed_check_count": 0,
        "local_relevance_medium_read_only_state_packet_body_exposure_metadata": metadata,
        "local_relevance_medium_read_only_state_packet_body_exposure": exposure,
        "local_relevance_medium_read_only_state_packet_body_exposure_checks": [
            {
                "check_name": "synthetic selected-state packet body exposure clean",
                "passed": True,
                "expected_posture": "clean selected-state packet body exposure",
                "actual_posture": "clean selected-state packet body exposure",
                "block_code": None,
                "failure_code": None,
            }
        ],
        "local_relevance_medium_read_only_state_packet_body_exposure_statement": statement,
        "local_relevance_medium_read_only_state_packet_body_exposure_summary": summary,
        "non_claims": {key: False for key in STATE_PACKET_EXPOSURE_FALSE_FIELDS},
        "block": {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        },
    }
    if artifact_overrides:
        artifact.update(dict(artifact_overrides))
    return artifact


class LocalRelevanceMediumReadOnlyRawFullStatePacketBodyExposureV0MinTests(
    unittest.TestCase
):
    maxDiff = None

    def write_synthetic_raw_full_boundary_artifact(
        self,
        directory: Path,
        *,
        name: str = "synthetic_raw_full_boundary.json",
        artifact: Mapping[str, Any] | None = None,
        **artifact_kwargs: Any,
    ) -> tuple[Path, dict[str, Any]]:
        material = (
            copy.deepcopy(dict(artifact))
            if artifact is not None
            else _clean_raw_full_boundary_artifact(**artifact_kwargs)
        )
        path = directory / name
        _write_json(path, material)
        return path, material

    def write_synthetic_state_packet_body_exposure_artifact(
        self,
        directory: Path,
        *,
        name: str = "synthetic_state_packet_body_exposure.json",
        artifact: Mapping[str, Any] | None = None,
        **artifact_kwargs: Any,
    ) -> tuple[Path, dict[str, Any]]:
        material = (
            copy.deepcopy(dict(artifact))
            if artifact is not None
            else _clean_state_packet_body_exposure_artifact(**artifact_kwargs)
        )
        path = directory / name
        _write_json(path, material)
        return path, material

    def build_request_for_artifacts(
        self,
        raw_full_boundary_artifact: Path | str,
        state_packet_body_exposure_artifact: Path | str,
    ) -> dict[str, Any]:
        return resolver.build_declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_request(
            selected_raw_full_state_packet_body_exposure_boundary_artifact=raw_full_boundary_artifact,
            selected_state_packet_body_exposure_artifact=state_packet_body_exposure_artifact,
        )

    def build_synthetic_request(
        self,
        directory: Path,
    ) -> tuple[Path, Path, dict[str, Any], dict[str, Any], dict[str, Any]]:
        boundary_path, boundary_artifact = self.write_synthetic_raw_full_boundary_artifact(
            directory
        )
        packet_path, packet_artifact = self.write_synthetic_state_packet_body_exposure_artifact(
            directory
        )
        request = self.build_request_for_artifacts(boundary_path, packet_path)
        return boundary_path, packet_path, boundary_artifact, packet_artifact, request

    def exposure(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        exposure = result.get(
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure"
        )
        self.assertIsInstance(exposure, Mapping)
        return exposure

    def statement(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        statement = result.get(
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_statement"
        )
        self.assertIsInstance(statement, Mapping)
        return statement

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get(
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_checks"
        )
        self.assertIsInstance(checks, list)
        return checks

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = resolver.build_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_summary(
            result
        )
        self.assertIsInstance(summary, Mapping)
        return summary

    def non_claims(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        return non_claims

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is not True)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

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

    def assert_generated_booleans_are_booleans(
        self,
        mapping: Mapping[str, Any],
        keys: tuple[str, ...],
    ) -> None:
        for key in keys:
            self.assertIn(key, mapping)
            self.assertIsInstance(mapping[key], bool)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = self.non_claims(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)

    def assert_raw_full_exposure_non_claims(self, result: Mapping[str, Any]) -> None:
        self.assert_canonical_false_non_claims(result)
        exposure = self.exposure(result)
        for key in RAW_FULL_EXPOSURE_OBJECT_FALSE_FIELDS:
            self.assertIn(key, exposure)
            self.assertIs(exposure[key], False)
            self.assertIsInstance(exposure[key], bool)
        if result.get("outcome") != resolver.OUTCOME_RECORDED:
            self.assertIs(
                exposure[
                    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded"
                ],
                False,
            )
            self.assertIs(exposure["raw_full_state_packet_body_exposed"], False)
            self.assertIs(exposure["raw_full_state_packet_body_exposure_local_only"], False)
            self.assertIs(exposure["raw_full_state_packet_body_exposure_read_only"], False)

    def assert_closure_tokens_false(self, result: Mapping[str, Any]) -> None:
        non_claims = self.non_claims(result)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)
        exposure = self.exposure(result)
        self.assertIs(exposure["consumed_request_reopened"], False)
        self.assertIs(exposure["authorization_token_reused"], False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_raw_full_exposure_non_claims(result)

    def assert_exposure_object_not_wrapper(self, result: Mapping[str, Any]) -> None:
        exposure = self.exposure(result)
        for key in FORBIDDEN_EXPOSURE_WRAPPER_FIELDS:
            self.assertNotIn(key, exposure)

    def assert_exposure_preserves_raw_full_posture(
        self,
        result: Mapping[str, Any],
        boundary_path: Path | str,
        packet_path: Path | str,
    ) -> None:
        exposure = self.exposure(result)
        self.assertEqual(
            exposure["raw_full_state_packet_body_exposure_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE",
        )
        self.assertEqual(
            exposure["raw_full_state_packet_body_exposure_scope"],
            "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY",
        )
        self.assertEqual(exposure["raw_full_state_packet_body_exposure_version"], "0.1.0")
        self.assert_same_or_stable_artifact_path(
            exposure["basis_raw_full_state_packet_body_exposure_boundary_artifact"],
            boundary_path,
        )
        self.assertEqual(
            exposure["basis_raw_full_state_packet_body_exposure_boundary_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            exposure["basis_raw_full_state_packet_body_exposure_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            exposure["basis_raw_full_state_packet_body_exposure_boundary_failed_check_count"],
            0,
        )
        self.assert_same_or_stable_artifact_path(
            exposure["basis_state_packet_body_exposure_artifact"],
            packet_path,
        )
        self.assertEqual(
            exposure["basis_state_packet_body_exposure_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_RECORDED",
        )
        self.assertEqual(exposure["basis_state_packet_body_exposure_result_version"], "0.1.0")
        self.assertEqual(exposure["basis_state_packet_body_exposure_failed_check_count"], 0)
        self.assertEqual(exposure["selected_command"], "state")
        self.assertIs(exposure["selected_command_is_state"], True)
        self.assertIs(exposure["selected_state_packet_body_exposure_recorded"], True)
        self.assertIs(exposure["state_packet_body_exposed"], True)
        self.assertIs(exposure["state_packet_body_exposure_local_only"], True)
        self.assertIs(exposure["state_packet_body_exposure_read_only"], True)
        self.assertIs(
            exposure[
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded"
            ],
            True,
        )
        self.assertIs(exposure["raw_full_state_packet_body_exposed"], True)
        self.assertIs(exposure["raw_full_state_packet_body_exposure_local_only"], True)
        self.assertIs(exposure["raw_full_state_packet_body_exposure_read_only"], True)
        for key in RAW_FULL_EXPOSURE_OBJECT_FALSE_FIELDS:
            self.assertIn(key, exposure)
            self.assertIs(exposure[key], False)
            self.assertIsInstance(exposure[key], bool)
        self.assert_exposure_object_not_wrapper(result)

    def assert_no_hostile_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_output_path_not_prior_root(self, path: Path) -> None:
        for forbidden in FORBIDDEN_OUTPUT_ROOTS:
            self.assertFalse(
                _path_has_component_prefix(path, forbidden),
                f"{path} unexpectedly wrote under {forbidden}",
            )

    def test_public_api_constants_and_default_builder(self) -> None:
        for name in (
            "resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min",
            "resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_from_path",
            "write_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_result",
            "build_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_summary",
            "build_declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE_VALUES",
            "SUPPORTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE_VALUES",
            "SELECTED_COMMAND",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min",
        )
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE",
            resolver.SUPPORTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_TYPE_VALUES,
        )
        self.assertIn(
            "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY",
            resolver.SUPPORTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_SCOPE_VALUES,
        )
        self.assertEqual(resolver.SELECTED_COMMAND, "state")
        self.assertIn("lookup_performed", resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("consumed_request_reopened", resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("authorization_token_reused", resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("CONSUMED_REQUEST_REOPENED", resolver.BLOCK_CODES)
        self.assertIn("AUTHORIZATION_TOKEN_REUSED", resolver.BLOCK_CODES)
        self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", resolver.BLOCK_CODES)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BLOCKED",
            },
        )

        request = resolver.build_declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_request()
        self.assertTrue(
            str(
                request["selected_raw_full_state_packet_body_exposure_boundary_artifact"]
            ).endswith(
                DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT.name
            )
        )
        self.assertTrue(
            str(request["selected_state_packet_body_exposure_artifact"]).endswith(
                DEFAULT_STATE_PACKET_BODY_EXPOSURE_ARTIFACT.name
            )
        )
        self.assertEqual(request["selected_command"], "state")
        self.assertIs(request["declared_non_claims"]["consumed_request_reopened"], False)
        self.assertIs(request["declared_non_claims"]["authorization_token_reused"], False)

        output_root = Path(resolver.OUTPUT_ROOT)
        self.assertFalse(output_root.is_absolute())
        self.assert_output_path_not_prior_root(output_root / "probe.json")

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            (
                boundary_path,
                packet_path,
                _boundary_artifact,
                _packet_artifact,
                request,
            ) = self.build_synthetic_request(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min(
                request
            )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        summary = self.summary(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assertEqual(
            summary["raw_full_state_packet_body_exposure_id"],
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_001",
        )

        for section in EXPECTED_WRAPPER_SECTIONS:
            self.assertIn(section, result)

        exposure = self.exposure(result)
        self.assertEqual(
            exposure["raw_full_state_packet_body_exposure_id"],
            "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_001",
        )
        self.assert_exposure_preserves_raw_full_posture(
            result,
            boundary_path,
            packet_path,
        )

        statement = self.statement(result)
        for key in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True)
        self.assert_generated_booleans_are_booleans(statement, EXPECTED_TRUE_STATEMENT_FIELDS)
        self.assert_canonical_false_non_claims(result)
        self.assert_closure_tokens_false(result)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT.exists():
            self.skipTest("default raw/full boundary artifact is absent")
        if not DEFAULT_STATE_PACKET_BODY_EXPOSURE_ARTIFACT.exists():
            self.skipTest("default selected-state packet body exposure artifact is absent")

        request = resolver.build_declared_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_request()
        result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min(
            request
        )

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        exposure = self.exposure(result)
        self.assertEqual(exposure["selected_command"], "state")
        self.assertEqual(
            exposure["raw_full_state_packet_body_exposure_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE",
        )
        self.assertEqual(
            exposure["raw_full_state_packet_body_exposure_scope"],
            "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY",
        )
        self.assertIs(exposure["selected_state_packet_body_exposure_recorded"], True)
        self.assertIs(exposure["state_packet_body_exposed"], True)
        self.assertIs(exposure["state_packet_body_exposure_local_only"], True)
        self.assertIs(exposure["state_packet_body_exposure_read_only"], True)
        self.assertIs(
            exposure[
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_recorded"
            ],
            True,
        )
        self.assertIs(exposure["raw_full_state_packet_body_exposed"], True)
        self.assertIs(exposure["raw_full_state_packet_body_exposure_local_only"], True)
        self.assertIs(exposure["raw_full_state_packet_body_exposure_read_only"], True)
        for key in (
            "lookup_performed",
            "lookup_command_executed",
            "operation_permission_created",
            "runtime_permission_created",
            "public_api_created",
            "distributed_network_behavior_created",
            "general_lookup_permission_created",
            "follow_on_work_authorized",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(exposure[key], False)
        self.assertIs(self.statement(result)["predecessor_failure_evidence_preserved"], True)
        self.assert_same_or_stable_artifact_path(
            exposure["basis_raw_full_state_packet_body_exposure_boundary_artifact"],
            DEFAULT_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT,
        )
        self.assert_same_or_stable_artifact_path(
            exposure["basis_state_packet_body_exposure_artifact"],
            DEFAULT_STATE_PACKET_BODY_EXPOSURE_ARTIFACT,
        )
        self.assert_canonical_false_non_claims(result)

    def test_closure_token_blocking_behavior(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str], ...] = (
            (
                "top level consumed request reopened",
                lambda request: request.__setitem__("consumed_request_reopened", True),
                "CONSUMED_REQUEST_REOPENED",
            ),
            (
                "top level authorization token reused",
                lambda request: request.__setitem__("authorization_token_reused", True),
                "AUTHORIZATION_TOKEN_REUSED",
            ),
            (
                "declared consumed request reopened true",
                lambda request: request["declared_non_claims"].__setitem__(
                    "consumed_request_reopened", True
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared authorization token reused true",
                lambda request: request["declared_non_claims"].__setitem__(
                    "authorization_token_reused", True
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared consumed request reopened missing",
                lambda request: request["declared_non_claims"].pop(
                    "consumed_request_reopened"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared authorization token reused missing",
                lambda request: request["declared_non_claims"].pop(
                    "authorization_token_reused"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared consumed request reopened string",
                lambda request: request["declared_non_claims"].__setitem__(
                    "consumed_request_reopened", "false"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared authorization token reused string",
                lambda request: request["declared_non_claims"].__setitem__(
                    "authorization_token_reused", "false"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared consumed request reopened none",
                lambda request: request["declared_non_claims"].__setitem__(
                    "consumed_request_reopened", None
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "declared authorization token reused none",
                lambda request: request["declared_non_claims"].__setitem__(
                    "authorization_token_reused", None
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            _boundary_path, _packet_path, _boundary, _packet, base_request = (
                self.build_synthetic_request(Path(tmp))
            )
            for name, mutate, expected_code in cases:
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutate(request)
                    result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assert_closure_tokens_false(result)

    def test_required_non_claim_canonicalization_for_flipped_declared_non_claims(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _boundary_path, _packet_path, _boundary, _packet, base_request = (
                self.build_synthetic_request(Path(tmp))
            )
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(self.non_claims(result)[key], False)
                    self.assert_canonical_false_non_claims(result)
                    self.assert_closure_tokens_false(result)

    def test_representative_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (
                boundary_path,
                packet_path,
                _boundary,
                _packet,
                base_request,
            ) = self.build_synthetic_request(tmp_path)
            array_artifact = tmp_path / "array_artifact.json"
            _write_json(array_artifact, [])
            not_recorded_boundary_path, _ = self.write_synthetic_raw_full_boundary_artifact(
                tmp_path,
                name="not_recorded_boundary.json",
                artifact_overrides={
                    "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_NOT_RECORDED"
                },
                summary_overrides={
                    "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_NOT_RECORDED"
                },
            )
            failed_boundary_path, failed_boundary = self.write_synthetic_raw_full_boundary_artifact(
                tmp_path,
                name="failed_boundary.json",
                artifact_overrides={"failed_check_count": 1},
                summary_overrides={"failed_check_count": 1},
            )
            failed_boundary[
                "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_checks"
            ] = [{"check_name": "synthetic failed boundary check", "passed": False}]
            _write_json(failed_boundary_path, failed_boundary)
            wrong_version_boundary_path, _ = self.write_synthetic_raw_full_boundary_artifact(
                tmp_path,
                name="wrong_version_boundary.json",
                artifact_overrides={"result_version": "9.9.9"},
                summary_overrides={"result_version": "9.9.9"},
                metadata_overrides={
                    "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_boundary_version": "9.9.9"
                },
                boundary_overrides={"boundary_version": "9.9.9"},
            )

            not_recorded_packet_path, _ = self.write_synthetic_state_packet_body_exposure_artifact(
                tmp_path,
                name="not_recorded_packet.json",
                artifact_overrides={
                    "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED"
                },
                summary_overrides={
                    "outcome": "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED"
                },
            )
            failed_packet_path, failed_packet = self.write_synthetic_state_packet_body_exposure_artifact(
                tmp_path,
                name="failed_packet.json",
                artifact_overrides={"failed_check_count": 1},
                summary_overrides={"failed_check_count": 1},
            )
            failed_packet[
                "local_relevance_medium_read_only_state_packet_body_exposure_checks"
            ] = [{"check_name": "synthetic failed packet check", "passed": False}]
            _write_json(failed_packet_path, failed_packet)
            wrong_version_packet_path, _ = self.write_synthetic_state_packet_body_exposure_artifact(
                tmp_path,
                name="wrong_version_packet.json",
                artifact_overrides={"result_version": "9.9.9"},
                summary_overrides={"result_version": "9.9.9"},
                metadata_overrides={
                    "local_relevance_medium_read_only_state_packet_body_exposure_version": "9.9.9"
                },
                exposure_overrides={"state_packet_body_exposure_version": "9.9.9"},
            )

            cases: list[tuple[str, Callable[[dict[str, Any]], None] | None, Any]] = [
                ("missing request", None, None),
                ("non-mapping request", None, ["not", "a", "mapping"]),
                (
                    "explicit block intent",
                    lambda request: request.__setitem__(
                        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_intent",
                        resolver.INTENT_BLOCK,
                    ),
                    None,
                ),
                (
                    "unsupported intent",
                    lambda request: request.__setitem__(
                        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_intent",
                        "UNSUPPORTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_INTENT",
                    ),
                    None,
                ),
                (
                    "raw/full boundary artifact path missing",
                    lambda request: request.pop(
                        "selected_raw_full_state_packet_body_exposure_boundary_artifact"
                    ),
                    None,
                ),
                (
                    "raw/full boundary artifact unreadable",
                    lambda request: request.__setitem__(
                        "selected_raw_full_state_packet_body_exposure_boundary_artifact",
                        str(tmp_path / "missing_raw_full_boundary.json"),
                    ),
                    None,
                ),
                (
                    "raw/full boundary artifact JSON array",
                    lambda request: request.__setitem__(
                        "selected_raw_full_state_packet_body_exposure_boundary_artifact",
                        str(array_artifact),
                    ),
                    None,
                ),
                (
                    "raw/full boundary artifact not recorded",
                    lambda request: request.__setitem__(
                        "selected_raw_full_state_packet_body_exposure_boundary_artifact",
                        str(not_recorded_boundary_path),
                    ),
                    None,
                ),
                (
                    "raw/full boundary artifact failed checks present",
                    lambda request: request.__setitem__(
                        "selected_raw_full_state_packet_body_exposure_boundary_artifact",
                        str(failed_boundary_path),
                    ),
                    None,
                ),
                (
                    "raw/full boundary artifact version not 0.1.0",
                    lambda request: request.__setitem__(
                        "selected_raw_full_state_packet_body_exposure_boundary_artifact",
                        str(wrong_version_boundary_path),
                    ),
                    None,
                ),
                (
                    "state packet body exposure artifact path missing",
                    lambda request: request.pop("selected_state_packet_body_exposure_artifact"),
                    None,
                ),
                (
                    "state packet body exposure artifact unreadable",
                    lambda request: request.__setitem__(
                        "selected_state_packet_body_exposure_artifact",
                        str(tmp_path / "missing_state_packet_body_exposure.json"),
                    ),
                    None,
                ),
                (
                    "state packet body exposure artifact JSON array",
                    lambda request: request.__setitem__(
                        "selected_state_packet_body_exposure_artifact",
                        str(array_artifact),
                    ),
                    None,
                ),
                (
                    "state packet body exposure artifact not recorded",
                    lambda request: request.__setitem__(
                        "selected_state_packet_body_exposure_artifact",
                        str(not_recorded_packet_path),
                    ),
                    None,
                ),
                (
                    "state packet body exposure artifact failed checks present",
                    lambda request: request.__setitem__(
                        "selected_state_packet_body_exposure_artifact",
                        str(failed_packet_path),
                    ),
                    None,
                ),
                (
                    "state packet body exposure artifact version not 0.1.0",
                    lambda request: request.__setitem__(
                        "selected_state_packet_body_exposure_artifact",
                        str(wrong_version_packet_path),
                    ),
                    None,
                ),
                ("selected command missing", lambda request: request.pop("selected_command"), None),
                ("selected command not state", lambda request: request.__setitem__("selected_command", "lookup"), None),
                (
                    "selected-state packet body exposure not recorded",
                    lambda request: request.__setitem__(
                        "selected_state_packet_body_exposure_not_recorded", True
                    ),
                    None,
                ),
                (
                    "state packet body not exposed",
                    lambda request: request.__setitem__("state_packet_body_not_exposed", True),
                    None,
                ),
                (
                    "state packet body exposure local only not true",
                    lambda request: request.__setitem__(
                        "state_packet_body_exposure_local_only_not_true", True
                    ),
                    None,
                ),
                (
                    "state packet body exposure read only not true",
                    lambda request: request.__setitem__(
                        "state_packet_body_exposure_read_only_not_true", True
                    ),
                    None,
                ),
                (
                    "raw/full state packet body exposure type missing",
                    lambda request: request.pop("raw_full_state_packet_body_exposure_type"),
                    None,
                ),
                (
                    "raw/full state packet body exposure type unsupported",
                    lambda request: request.__setitem__(
                        "raw_full_state_packet_body_exposure_type",
                        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_OPERATION_PERMISSION",
                    ),
                    None,
                ),
                (
                    "raw/full state packet body exposure scope missing",
                    lambda request: request.pop("raw_full_state_packet_body_exposure_scope"),
                    None,
                ),
                (
                    "raw/full state packet body exposure scope unsupported",
                    lambda request: request.__setitem__(
                        "raw_full_state_packet_body_exposure_scope",
                        "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY",
                    ),
                    None,
                ),
                (
                    "local raw/full state packet body exposure not recorded",
                    lambda request: request.__setitem__(
                        "local_relevance_medium_read_only_raw_full_state_packet_body_exposure_not_recorded",
                        True,
                    ),
                    None,
                ),
                (
                    "raw/full state packet body not exposed",
                    lambda request: request.__setitem__(
                        "raw_full_state_packet_body_not_exposed", True
                    ),
                    None,
                ),
                (
                    "raw/full state packet body exposure local only not true",
                    lambda request: request.__setitem__(
                        "raw_full_state_packet_body_exposure_local_only_not_true", True
                    ),
                    None,
                ),
                (
                    "raw/full state packet body exposure read only not true",
                    lambda request: request.__setitem__(
                        "raw_full_state_packet_body_exposure_read_only_not_true", True
                    ),
                    None,
                ),
                (
                    "required non-claim missing",
                    lambda request: request["declared_non_claims"].pop("lookup_performed"),
                    None,
                ),
                (
                    "required non-claim flipped",
                    lambda request: request["declared_non_claims"].__setitem__(
                        "lookup_performed", True
                    ),
                    None,
                ),
            ]

            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                cases.append(
                    (
                        f"{field} top-level true",
                        lambda request, field=field: request.__setitem__(field, True),
                        None,
                    )
                )

            self.assertTrue(boundary_path.exists())
            self.assertTrue(packet_path.exists())
            for name, mutate, direct_value in cases:
                with self.subTest(name=name):
                    if mutate is None:
                        request_value = direct_value
                    else:
                        request_value = copy.deepcopy(base_request)
                        mutate(request_value)
                    result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min(
                        request_value
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assert_closure_tokens_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            (
                _boundary_path,
                _packet_path,
                _boundary,
                _packet,
                request,
            ) = self.build_synthetic_request(Path(tmp))
            result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min(
                request
            )

        exposure = self.exposure(result)
        self.assertEqual(
            exposure["raw_full_state_packet_body_exposure_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE",
        )
        self.assertEqual(
            exposure["raw_full_state_packet_body_exposure_scope"],
            "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY",
        )
        self.assertEqual(exposure["selected_command"], "state")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIn(resolver.OUTCOME_RECORDED, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OUTCOME_NOT_RECORDED, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OUTCOME_BLOCKED, resolver.OUTCOME_FAMILY)

        serialized = json.dumps(result, sort_keys=True)
        self.assertIn(resolver.OUTCOME_RECORDED, serialized)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE",
            serialized,
        )
        self.assertIn("SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY", serialized)
        self.assertIn('"state"', serialized)
        self.assertNotIn("[REDACTED", serialized)

    def test_raw_hidden_hostile_content_containment_and_no_request_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary_artifact = _clean_raw_full_boundary_artifact(
                boundary_overrides={
                    "raw_full_state_packet_body_exposure_boundary_body": HOSTILE_SENTINELS[3],
                    "raw_full_state_packet_body": HOSTILE_SENTINELS[2],
                },
                artifact_overrides={"hidden_repo_state": {"payload": HOSTILE_SENTINELS[-1]}},
            )
            packet_artifact = _clean_state_packet_body_exposure_artifact(
                exposure_overrides={
                    "state_packet_body": HOSTILE_SENTINELS[5],
                    "state_packet_body_exposure_body": HOSTILE_SENTINELS[4],
                },
                artifact_overrides={
                    "raw_full_state_packet_body": HOSTILE_SENTINELS[2],
                    "hidden_repo_state": {"payload": HOSTILE_SENTINELS[-1]},
                },
            )
            boundary_original = copy.deepcopy(boundary_artifact)
            packet_original = copy.deepcopy(packet_artifact)
            boundary_path, _ = self.write_synthetic_raw_full_boundary_artifact(
                tmp_path,
                artifact=boundary_artifact,
            )
            packet_path, _ = self.write_synthetic_state_packet_body_exposure_artifact(
                tmp_path,
                artifact=packet_artifact,
            )
            request = self.build_request_for_artifacts(boundary_path, packet_path)
            request["raw_full_state_packet_body_exposure_body"] = HOSTILE_SENTINELS[0]
            request["raw_full_state_packet_body"] = HOSTILE_SENTINELS[2]
            request["hidden_repo_state"] = {"payload": HOSTILE_SENTINELS[-1]}
            request["current_working_tree"] = {"raw_body": HOSTILE_SENTINELS[-2]}
            request_original = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min(
                request
            )

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        if result["outcome"] == resolver.OUTCOME_BLOCKED:
            self.assert_blocked_with_public_code(result)
        self.assert_no_hostile_sentinels(result)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE",
            serialized,
        )
        self.assertIn("SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY", serialized)
        self.assertIn('"state"', serialized)
        self.assert_canonical_false_non_claims(result)
        self.assert_closure_tokens_false(result)
        self.assertEqual(request, request_original)
        self.assertEqual(boundary_artifact, boundary_original)
        self.assertEqual(packet_artifact, packet_original)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (
                _boundary_path,
                _packet_path,
                _boundary,
                _packet,
                request,
            ) = self.build_synthetic_request(tmp_path)
            request_path = tmp_path / "declared_raw_full_state_packet_body_exposure_request.json"
            _write_json(request_path, request)
            result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(self.summary(result)["result_version"], "0.1.0")
            self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            bad_json_path = tmp_path / "bad_request.json"
            bad_json_path.write_text("{", encoding="utf-8")
            bad_result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_from_path(
                bad_json_path
            )
            self.assert_blocked_with_public_code(bad_result)

            array_request_path = tmp_path / "array_request.json"
            _write_json(array_request_path, [])
            array_result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_from_path(
                array_request_path
            )
            self.assert_blocked_with_public_code(array_result)

            missing_result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_from_path(
                tmp_path / "missing_request.json"
            )
            self.assert_blocked_with_public_code(missing_result)

            patched_output_root = tmp_path / "artifacts" / EXPECTED_OUTPUT_ROOT.name
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_output_root):
                first_path = resolver.write_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(second_path.stem.endswith("_001"))
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn(EXPECTED_OUTPUT_ROOT.name, str(first_path))
            self.assert_output_path_not_prior_root(first_path)
            self.assert_output_path_not_prior_root(second_path)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            boundary_artifact = _clean_raw_full_boundary_artifact(
                artifact_overrides={"hidden_repo_state": {"payload": HOSTILE_SENTINELS[-1]}},
                boundary_overrides={"raw_full_state_packet_body": HOSTILE_SENTINELS[2]},
            )
            packet_artifact = _clean_state_packet_body_exposure_artifact(
                artifact_overrides={"hidden_repo_state": {"payload": HOSTILE_SENTINELS[-1]}},
                exposure_overrides={"state_packet_body": HOSTILE_SENTINELS[5]},
            )
            boundary_original = copy.deepcopy(boundary_artifact)
            packet_original = copy.deepcopy(packet_artifact)
            boundary_path, _ = self.write_synthetic_raw_full_boundary_artifact(
                tmp_path,
                artifact=boundary_artifact,
            )
            packet_path, _ = self.write_synthetic_state_packet_body_exposure_artifact(
                tmp_path,
                artifact=packet_artifact,
            )
            request = self.build_request_for_artifacts(boundary_path, packet_path)
            request["nested_raw_payload"] = {
                "raw_full_state_packet_body": HOSTILE_SENTINELS[2],
                "items": [{"hidden_repo_state": HOSTILE_SENTINELS[-1]}],
            }
            request_original = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min(
                request
            )

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertEqual(request, request_original)
        self.assertEqual(request["declared_non_claims"], request_original["declared_non_claims"])
        self.assertEqual(
            request["selected_raw_full_state_packet_body_exposure_boundary_artifact"],
            request_original["selected_raw_full_state_packet_body_exposure_boundary_artifact"],
        )
        self.assertEqual(
            request["selected_state_packet_body_exposure_artifact"],
            request_original["selected_state_packet_body_exposure_artifact"],
        )
        self.assertEqual(request["selected_command"], "state")
        self.assertEqual(
            request["raw_full_state_packet_body_exposure_type"],
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_RAW_FULL_STATE_PACKET_BODY_EXPOSURE",
        )
        self.assertEqual(
            request["raw_full_state_packet_body_exposure_scope"],
            "SELECTED_RAW_FULL_STATE_PACKET_BODY_EXPOSURE_ONLY",
        )
        self.assertIs(request["consumed_request_reopened"], False)
        self.assertIs(request["authorization_token_reused"], False)
        self.assertEqual(boundary_artifact, boundary_original)
        self.assertEqual(packet_artifact, packet_original)
        self.assert_canonical_false_non_claims(result)

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _boundary_path, _packet_path, _boundary, _packet, request = (
                self.build_synthetic_request(Path(tmp))
            )
            result = resolver.resolve_local_relevance_medium_read_only_raw_full_state_packet_body_exposure_v0_min(
                request
            )

        statement = self.statement(result)
        non_claims = self.non_claims(result)
        summary = self.summary(result)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(non_claims["predecessor_failure_repaired"], False)
        self.assertIs(non_claims["predecessor_failure_hidden"], False)
        self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)


if __name__ == "__main__":
    unittest.main()
