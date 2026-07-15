"""Tests for the local relevance medium second local relevance orientation index entry resolver.

This suite is bounded to one second local locator object. It verifies that the
resolver reads one clean local relevance medium second relevance orientation
view artifact, preserves the basis second orientation, second receipt, second
reception, candidate-admission, successor request, first local index entry,
first orientation-view, first receipt, first reception, existing received
identifier basis, and second received identifiers, and records one local
discoverability object only.

The suite does not create local medium multiplicity result, relation view,
comparison view, repeated reception permission, arbitrary reception, feed,
index system, registry, search, ranking, source transfer, source receipt,
authority, currentness, truth, action, synchronization, participation
authorization, participant role, runtime permission, public API,
participant-facing interface, distributed behavior, operation permission, or
follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min as resolver  # noqa: E402


DEFAULT_SECOND_ORIENTATION_ARTIFACT = (
    REPO_ROOT
    / "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min/"
    "local_relevance_medium_second_relevance_orientation_view_reference_review_001__"
    "local_relevance_medium_second_relevance_orientation_view_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min"
)
FORBIDDEN_EXACT_OUTPUT_ROOTS = (
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min"
    ),
    Path(
        "artifacts/"
        "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_receipt_v0_min"
    ),
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
    Path("artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2"),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min"),
    Path("artifacts/integrity_host_v0_min_coexistence_post_runtime_daemon_runtime_loop"),
    Path("artifacts/source-transfer"),
    Path("artifacts/source-receipt"),
    Path("artifacts/public-api"),
    Path("artifacts/participant-facing-interface"),
    Path("artifacts/distributed-network"),
)

BASIS_SECOND_RECEIPT_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_receipt_v0_min/"
    "local_relevance_medium_second_bounded_relevance_receipt_reference_review_001__"
    "local_relevance_medium_second_bounded_relevance_receipt_v0_min_result.json"
)
BASIS_SECOND_RECEPTION_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_reception_v0_min/"
    "local_relevance_medium_second_bounded_relevance_reception_reference_review_001__"
    "local_relevance_medium_second_bounded_relevance_reception_v0_min_result.json"
)
BASIS_SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_successor_candidate_admission_v0_min/"
    "local_relevance_medium_successor_candidate_admission_reference_review_001__"
    "local_relevance_medium_successor_candidate_admission_v0_min_result.json"
)
BASIS_SUCCESSOR_RECEPTION_REQUEST_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_successor_reception_request_v0_min/"
    "local_relevance_medium_successor_reception_request_reference_review_001__"
    "local_relevance_medium_successor_reception_request_v0_min_result.json"
)
BASIS_FIRST_INDEX_ENTRY_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min/"
    "local_relevance_orientation_index_entry_reference_review_001__"
    "local_relevance_orientation_index_entry_v0_min_result.json"
)
EXISTING_ORIENTATION_VIEW_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min/"
    "relevance_orientation_view_reference_review_001__relevance_orientation_view_v0_min_result.json"
)
EXISTING_SOURCE_RECEIPT_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2/"
    "bounded_relevance_receipt_reference_review_001__bounded_relevance_receipt_v0_min_v2_result.json"
)
EXISTING_REFERENCED_RECEPTION_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min/"
    "bounded_relevance_reception_reference_review_001__bounded_relevance_reception_v0_min_result.json"
)

EXPECTED_TOP_LEVEL_SECTIONS = {
    "local_relevance_medium_second_local_relevance_orientation_index_entry_metadata",
    "declared_local_relevance_medium_second_local_relevance_orientation_index_entry_question",
    "selected_second_relevance_orientation_view_artifact_basis",
    "second_local_relevance_orientation_index_entry",
    "local_relevance_medium_second_local_relevance_orientation_index_entry_checks",
    "local_relevance_medium_second_local_relevance_orientation_index_entry_statement",
    "local_relevance_medium_second_local_relevance_orientation_index_entry_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_second_local_relevance_orientation_index_entry_summary",
}

SECOND_INDEX_ENTRY_FIELDS = {
    "second_index_entry_id",
    "second_index_entry_type",
    "second_index_entry_version",
    "second_index_entry_scope",
    "basis_second_relevance_orientation_view_artifact",
    "basis_second_relevance_orientation_view_outcome",
    "basis_second_relevance_orientation_view_result_version",
    "basis_second_relevance_orientation_view_failed_check_count",
    "basis_second_bounded_relevance_receipt_artifact",
    "basis_second_bounded_relevance_reception_artifact",
    "basis_successor_candidate_admission_artifact",
    "basis_successor_reception_request_artifact",
    "basis_first_local_relevance_orientation_index_entry_artifact",
    "existing_orientation_view_artifact",
    "existing_source_receipt_artifact",
    "existing_referenced_reception_artifact",
    "existing_received_signal_id",
    "existing_received_relevance_basis_id",
    "existing_received_relevance_scope_id",
    "existing_received_carrier_context_id",
    "existing_received_reception_envelope_id",
    "admitted_successor_candidate_id",
    "second_received_signal_id",
    "second_relevance_basis_id",
    "second_relevance_scope_id",
    "second_carrier_context_id",
    "second_reception_envelope_id",
    "local_discoverability",
    "second_orientation_view_artifact_preserved",
    "second_received_identifiers_preserved",
    "basis_lineage_preserved",
    "index_entry_does_not_create_index_system",
    "index_entry_does_not_create_registry",
    "index_entry_does_not_create_search",
    "index_entry_does_not_create_ranking",
    "local_medium_multiplicity_result_created",
    "relation_view_created",
    "comparison_view_created",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
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
}

WRAPPER_KEYS_FORBIDDEN_IN_SECOND_INDEX_ENTRY = {
    "outcome",
    "block",
    "local_relevance_medium_second_local_relevance_orientation_index_entry_checks",
    "non_claims",
    "local_relevance_medium_second_local_relevance_orientation_index_entry_summary",
    "local_relevance_medium_second_local_relevance_orientation_index_entry_metadata",
}

EXPECTED_SECOND_IDENTIFIERS = {
    "second_received_signal_id": "bounded_relevance_signal_002",
    "second_relevance_basis_id": "bounded_relevance_basis_002",
    "second_relevance_scope_id": "bounded_relevance_scope_002",
    "second_carrier_context_id": "bounded_relevance_signal_carrier_context_002",
    "second_reception_envelope_id": "bounded_relevance_reception_envelope_002",
}

ENTRY_FALSE_FIELDS = {
    "local_medium_multiplicity_result_created",
    "relation_view_created",
    "comparison_view_created",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
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
}

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_CANDIDATE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RECEPTION_REQUEST_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_LOCAL_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RELEVANCE_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RELEVANCE_RECEPTION_BODY_MUST_NOT_RETURN",
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


def _write_json(path: Path, payload: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _second_orientation_view_object(**overrides: Any) -> dict[str, Any]:
    view = {
        "second_orientation_view_id": "local_relevance_medium_second_relevance_orientation_view_001",
        "second_orientation_view_type": "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW",
        "second_orientation_view_version": "0.1.0",
        "second_orientation_scope": "SECOND_LOCAL_ORIENTATION_ONLY",
        "basis_second_bounded_relevance_receipt_artifact": BASIS_SECOND_RECEIPT_ARTIFACT,
        "basis_second_bounded_relevance_reception_artifact": BASIS_SECOND_RECEPTION_ARTIFACT,
        "basis_successor_candidate_admission_artifact": (
            BASIS_SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT
        ),
        "basis_successor_reception_request_artifact": BASIS_SUCCESSOR_RECEPTION_REQUEST_ARTIFACT,
        "basis_index_entry_artifact": BASIS_FIRST_INDEX_ENTRY_ARTIFACT,
        "existing_orientation_view_artifact": EXISTING_ORIENTATION_VIEW_ARTIFACT,
        "existing_source_receipt_artifact": EXISTING_SOURCE_RECEIPT_ARTIFACT,
        "existing_referenced_reception_artifact": EXISTING_REFERENCED_RECEPTION_ARTIFACT,
        "existing_received_signal_id": "bounded_relevance_signal_001",
        "existing_received_relevance_basis_id": "bounded_relevance_basis_001",
        "existing_received_relevance_scope_id": "bounded_relevance_scope_001",
        "existing_received_carrier_context_id": "bounded_relevance_signal_carrier_context_001",
        "existing_received_reception_envelope_id": "bounded_relevance_reception_envelope_001",
        "admitted_successor_candidate_id": "bounded_relevance_signal_candidate_002",
        "second_received_signal_id": "bounded_relevance_signal_002",
        "second_relevance_basis_id": "bounded_relevance_basis_002",
        "second_relevance_scope_id": "bounded_relevance_scope_002",
        "second_carrier_context_id": "bounded_relevance_signal_carrier_context_002",
        "second_reception_envelope_id": "bounded_relevance_reception_envelope_002",
    }
    view.update(overrides)
    return view


def _synthetic_second_orientation_artifact(
    artifact_overrides: dict[str, Any] | None = None,
    view_overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    artifact = {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW_RECORDED",
        "local_relevance_medium_second_relevance_orientation_view_metadata": {
            "local_relevance_medium_second_relevance_orientation_view_id": (
                "local_relevance_medium_second_relevance_orientation_view_001"
            ),
            "local_relevance_medium_second_relevance_orientation_view_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_second_relevance_orientation_view_v0_min",
            "passed_check_count": 77,
            "failed_check_count": 0,
        },
        "local_relevance_medium_second_relevance_orientation_view_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW_RECORDED",
            "result_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_second_relevance_orientation_view_v0_min",
            "passed_check_count": 77,
            "failed_check_count": 0,
        },
        "second_relevance_orientation_view": _second_orientation_view_object(
            **(view_overrides or {})
        ),
        "local_relevance_medium_second_relevance_orientation_view_checks": [
            {
                "check_name": "synthetic_clean_second_orientation_basis",
                "passed": True,
                "expected_posture": "clean second orientation view",
                "actual_posture": "clean second orientation view",
                "block_code": None,
                "failure_code": None,
            }
        ],
    }
    if artifact_overrides:
        artifact.update(artifact_overrides)
    return artifact


def _request_for(artifact_path: Path | str, **overrides: Any) -> dict[str, Any]:
    return (
        resolver.build_declared_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_request(
            selected_second_relevance_orientation_view_artifact=artifact_path,
            **overrides,
        )
    )


def _same_or_child(path: Path, root: Path) -> bool:
    path = Path(path)
    root = Path(root)
    if path.is_absolute() != root.is_absolute():
        path = path if path.is_absolute() else REPO_ROOT / path
        root = root if root.is_absolute() else REPO_ROOT / root
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


class LocalRelevanceMediumSecondLocalRelevanceOrientationIndexEntryTests(unittest.TestCase):
    def assert_not_blocked(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def entry(self, result: dict[str, Any]) -> dict[str, Any]:
        entry = result.get("second_local_relevance_orientation_index_entry")
        self.assertIsInstance(entry, dict)
        return entry

    def statement(self, result: dict[str, Any]) -> dict[str, Any]:
        statement = result.get(
            "local_relevance_medium_second_local_relevance_orientation_index_entry_statement"
        )
        self.assertIsInstance(statement, dict)
        return statement

    def checks(self, result: dict[str, Any]) -> list[dict[str, Any]]:
        checks = result.get(
            "local_relevance_medium_second_local_relevance_orientation_index_entry_checks"
        )
        self.assertIsInstance(checks, list)
        return checks

    def summary(self, result: dict[str, Any]) -> dict[str, Any]:
        summary = result.get(
            "local_relevance_medium_second_local_relevance_orientation_index_entry_summary"
        )
        self.assertIsInstance(summary, dict)
        return summary

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        return block.get("block_code") or block.get("code")

    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                emitted = check.get(key)
                if emitted is not None:
                    self.assertIn(emitted, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIs(type(non_claims[key]), bool)

    def assert_no_forbidden_creation(self, result: dict[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        entry = self.entry(result)
        for key in ENTRY_FALSE_FIELDS:
            if key in entry:
                self.assertIs(entry[key], False, key)
        non_meaning = result.get(
            "local_relevance_medium_second_local_relevance_orientation_index_entry_non_meaning"
        )
        self.assertIsInstance(non_meaning, dict)
        for key, value in non_meaning.items():
            self.assertIs(value, False, key)

    def assert_second_index_entry_not_wrapper(self, entry: dict[str, Any]) -> None:
        for key in WRAPPER_KEYS_FORBIDDEN_IN_SECOND_INDEX_ENTRY:
            self.assertNotIn(key, entry)

    def assert_successful_recorded_result(
        self,
        result: dict[str, Any],
        artifact_path: Path | str,
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        summary = self.summary(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            summary["second_index_entry_id"],
            "local_relevance_medium_second_local_relevance_orientation_index_entry_001",
        )
        self.assertTrue(EXPECTED_TOP_LEVEL_SECTIONS.issubset(result))

        entry = self.entry(result)
        self.assertTrue(SECOND_INDEX_ENTRY_FIELDS.issubset(entry))
        self.assertEqual(
            entry["second_index_entry_id"],
            "local_relevance_medium_second_local_relevance_orientation_index_entry_001",
        )
        self.assertEqual(
            entry["second_index_entry_type"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
        )
        self.assertEqual(entry["second_index_entry_version"], "0.1.0")
        self.assertEqual(entry["second_index_entry_scope"], "SECOND_LOCAL_INDEX_ENTRY_ONLY")
        self.assertEqual(
            entry["basis_second_relevance_orientation_view_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW_RECORDED",
        )
        self.assertEqual(entry["basis_second_relevance_orientation_view_result_version"], "0.1.0")
        self.assertEqual(entry["basis_second_relevance_orientation_view_failed_check_count"], 0)
        self.assertEqual(entry["basis_second_relevance_orientation_view_artifact"], str(artifact_path))
        self.assertEqual(entry["basis_second_bounded_relevance_receipt_artifact"], BASIS_SECOND_RECEIPT_ARTIFACT)
        self.assertEqual(entry["basis_second_bounded_relevance_reception_artifact"], BASIS_SECOND_RECEPTION_ARTIFACT)
        self.assertEqual(
            entry["basis_successor_candidate_admission_artifact"],
            BASIS_SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT,
        )
        self.assertEqual(
            entry["basis_successor_reception_request_artifact"],
            BASIS_SUCCESSOR_RECEPTION_REQUEST_ARTIFACT,
        )
        self.assertEqual(
            entry["basis_first_local_relevance_orientation_index_entry_artifact"],
            BASIS_FIRST_INDEX_ENTRY_ARTIFACT,
        )
        self.assertEqual(entry["existing_orientation_view_artifact"], EXISTING_ORIENTATION_VIEW_ARTIFACT)
        self.assertEqual(entry["existing_source_receipt_artifact"], EXISTING_SOURCE_RECEIPT_ARTIFACT)
        self.assertEqual(
            entry["existing_referenced_reception_artifact"],
            EXISTING_REFERENCED_RECEPTION_ARTIFACT,
        )
        self.assertEqual(entry["existing_received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(entry["existing_received_relevance_basis_id"], "bounded_relevance_basis_001")
        self.assertEqual(entry["existing_received_relevance_scope_id"], "bounded_relevance_scope_001")
        self.assertEqual(
            entry["existing_received_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_001",
        )
        self.assertEqual(
            entry["existing_received_reception_envelope_id"],
            "bounded_relevance_reception_envelope_001",
        )
        self.assertEqual(entry["admitted_successor_candidate_id"], "bounded_relevance_signal_candidate_002")
        for key, expected in EXPECTED_SECOND_IDENTIFIERS.items():
            self.assertEqual(entry[key], expected)
        self.assertNotEqual(entry["second_received_signal_id"], entry["existing_received_signal_id"])
        self.assertIs(entry["local_discoverability"], True)
        self.assertIs(entry["second_orientation_view_artifact_preserved"], True)
        self.assertIs(entry["second_received_identifiers_preserved"], True)
        self.assertIs(entry["basis_lineage_preserved"], True)
        self.assertIs(entry["index_entry_does_not_create_index_system"], True)
        self.assertIs(entry["index_entry_does_not_create_registry"], True)
        self.assertIs(entry["index_entry_does_not_create_search"], True)
        self.assertIs(entry["index_entry_does_not_create_ranking"], True)
        for key in ENTRY_FALSE_FIELDS:
            self.assertIs(entry[key], False, key)
        self.assert_second_index_entry_not_wrapper(entry)

        statement = self.statement(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
        self.assert_no_forbidden_creation(result)

    def assert_blocked_public(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        self.assertGreater(self.summary(result)["failed_check_count"], 0)
        self.assert_public_block_codes(result)
        self.assert_no_forbidden_creation(result)

    def write_synthetic_artifact(
        self,
        directory: Path,
        name: str = "synthetic_second_orientation.json",
        artifact_overrides: dict[str, Any] | None = None,
        view_overrides: dict[str, Any] | None = None,
    ) -> tuple[Path, dict[str, Any]]:
        artifact = _synthetic_second_orientation_artifact(
            artifact_overrides=artifact_overrides,
            view_overrides=view_overrides,
        )
        path = directory / name
        _write_json(path, artifact)
        return path, artifact

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min",
            "resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_from_path",
            "write_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_result",
            "build_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_summary",
            "build_declared_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_INDEX_ENTRY_SCOPE_VALUES",
            "SUPPORTED_SECOND_INDEX_ENTRY_TYPE_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min",
        )
        self.assertTrue(str(Path(resolver.OUTPUT_ROOT)).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
            resolver.SUPPORTED_SECOND_INDEX_ENTRY_TYPE_VALUES,
        )
        self.assertIn(
            "SECOND_LOCAL_INDEX_ENTRY_ONLY",
            resolver.SUPPORTED_SECOND_INDEX_ENTRY_SCOPE_VALUES,
        )
        for forbidden_root in FORBIDDEN_EXACT_OUTPUT_ROOTS:
            self.assertFalse(_same_or_child(Path(resolver.OUTPUT_ROOT), forbidden_root))

    def test_successful_recorded_result_from_synthetic_second_orientation_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            request = _request_for(artifact_path)
            result = resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min(
                request
            )
        self.assert_successful_recorded_result(result, artifact_path)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_SECOND_ORIENTATION_ARTIFACT.exists():
            self.skipTest("default local relevance medium second relevance orientation view artifact absent")
        request = resolver.build_declared_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_request()
        result = resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min(
            request
        )
        self.assert_successful_recorded_result(
            result,
            "artifacts/"
            "integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min/"
            "local_relevance_medium_second_relevance_orientation_view_reference_review_001__"
            "local_relevance_medium_second_relevance_orientation_view_v0_min_result.json",
        )

    def test_required_false_non_claims_canonicalize_flipped_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            clean_request = _request_for(artifact_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = (
                        resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_public(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertNotIn(": true", json.dumps(result["non_claims"], sort_keys=True))

    def test_representative_blocking_behavior(self) -> None:
        false_flag_cases = [
            "local_medium_multiplicity_result_created",
            "relation_view_created",
            "comparison_view_created",
            "repeated_reception_permission_created",
            "arbitrary_reception_created",
            "feed_created",
            "index_system_created",
            "registry_created",
            "search_surface_created",
            "ranking_surface_created",
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
            "artifact_existence_treated_as_second_index_entry_authority",
            "latest_file_posture_treated_as_second_index_entry_authority",
            "repo_local_availability_treated_as_second_index_entry_authority",
            "hidden_repo_state_used_as_second_index_entry_content",
            "hidden_repo_state_used_as_second_index_entry_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ]

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact_path, _artifact = self.write_synthetic_artifact(tmp_path, "base.json")

            def resolve_with(
                name: str,
                request_updates: dict[str, Any] | None = None,
                view_updates: dict[str, Any] | None = None,
                artifact_updates: dict[str, Any] | None = None,
                direct_request: Any = None,
                array_artifact: bool = False,
                missing_selected_artifact: bool = False,
                request_mutator: Any = None,
            ) -> dict[str, Any]:
                if direct_request is not None:
                    return (
                        resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min(
                            direct_request
                        )
                    )
                selected_path = tmp_path / f"{name}.json"
                if missing_selected_artifact:
                    selected_path = tmp_path / f"{name}_absent.json"
                elif array_artifact:
                    _write_json(selected_path, [])
                else:
                    artifact = _synthetic_second_orientation_artifact(
                        artifact_overrides=artifact_updates,
                        view_overrides=view_updates,
                    )
                    _write_json(selected_path, artifact)
                request = _request_for(selected_path)
                if request_updates:
                    request.update(request_updates)
                if request_mutator:
                    request_mutator(request)
                return (
                    resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min(
                        request
                    )
                )

            cases: list[tuple[str, dict[str, Any]]] = [
                ("explicit_block_intent", {"request_updates": {"local_relevance_medium_second_local_relevance_orientation_index_entry_intent": "BLOCK_LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY"}}),
                ("missing_request", {"direct_request": {}}),
                ("non_mapping_request", {"direct_request": "not a mapping"}),
                ("unsupported_intent", {"request_updates": {"local_relevance_medium_second_local_relevance_orientation_index_entry_intent": "UNSUPPORTED_INTENT"}}),
                ("selected_path_missing", {"request_updates": {"selected_second_relevance_orientation_view_artifact": ""}}),
                ("selected_path_unreadable", {"missing_selected_artifact": True}),
                ("selected_json_array", {"array_artifact": True}),
                ("artifact_not_recorded", {"artifact_updates": {"outcome": "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW_NOT_RECORDED"}}),
                ("artifact_failed_checks", {"artifact_updates": {"local_relevance_medium_second_relevance_orientation_view_metadata": {"local_relevance_medium_second_relevance_orientation_view_version": "0.1.0", "failed_check_count": 1}}}),
                ("artifact_version_wrong", {"artifact_updates": {"local_relevance_medium_second_relevance_orientation_view_metadata": {"local_relevance_medium_second_relevance_orientation_view_version": "9.9.9", "failed_check_count": 0}}}),
                ("orientation_object_missing", {"artifact_updates": {"second_relevance_orientation_view": {}}}),
                ("orientation_type_wrong", {"view_updates": {"second_orientation_view_type": "WRONG_TYPE"}}),
                ("orientation_scope_wrong", {"view_updates": {"second_orientation_scope": "WRONG_SCOPE"}}),
                ("second_signal_missing", {"view_updates": {"second_received_signal_id": ""}}),
                ("second_basis_missing", {"view_updates": {"second_relevance_basis_id": ""}}),
                ("second_scope_missing", {"view_updates": {"second_relevance_scope_id": ""}}),
                ("second_context_missing", {"view_updates": {"second_carrier_context_id": ""}}),
                ("second_envelope_missing", {"view_updates": {"second_reception_envelope_id": ""}}),
                ("second_index_entry_type_missing", {"request_mutator": lambda req: req.pop("second_index_entry_type", None)}),
                ("second_index_entry_type_wrong", {"request_updates": {"second_index_entry_type": "WRONG_TYPE"}}),
                ("second_index_entry_scope_missing", {"request_mutator": lambda req: req.pop("second_index_entry_scope", None)}),
                ("second_index_entry_scope_wrong", {"request_updates": {"second_index_entry_scope": "WRONG_SCOPE"}}),
                ("basis_second_orientation_missing", {"request_updates": {"basis_second_relevance_orientation_view_artifact_missing": True}}),
                ("basis_second_receipt_missing", {"view_updates": {"basis_second_bounded_relevance_receipt_artifact": ""}}),
                ("basis_second_reception_missing", {"view_updates": {"basis_second_bounded_relevance_reception_artifact": ""}}),
                ("basis_successor_admission_missing", {"view_updates": {"basis_successor_candidate_admission_artifact": ""}}),
                ("basis_successor_request_missing", {"view_updates": {"basis_successor_reception_request_artifact": ""}}),
                ("basis_first_index_entry_missing", {"view_updates": {"basis_index_entry_artifact": ""}}),
                ("second_orientation_artifact_missing", {"request_updates": {"second_orientation_view_artifact_missing": True}}),
                ("second_identifiers_not_preserved", {"request_updates": {"second_received_identifiers_not_preserved": True}}),
                ("basis_lineage_not_preserved", {"request_updates": {"basis_lineage_not_preserved": True}}),
                ("local_discoverability_not_true", {"request_updates": {"local_discoverability_not_true": True}}),
                ("index_entry_creates_index_system", {"request_updates": {"index_entry_creates_index_system": True}}),
                ("index_entry_creates_registry", {"request_updates": {"index_entry_creates_registry": True}}),
                ("index_entry_creates_search", {"request_updates": {"index_entry_creates_search": True}}),
                ("index_entry_creates_ranking", {"request_updates": {"index_entry_creates_ranking": True}}),
                ("required_non_claim_missing", {"request_mutator": lambda req: req["declared_non_claims"].pop("feed_created", None)}),
            ]
            cases.extend((flag, {"request_updates": {flag: True}}) for flag in false_flag_cases)

            self.assertTrue(artifact_path.exists())
            for name, kwargs in cases:
                with self.subTest(case=name):
                    result = resolve_with(name, **kwargs)
                    self.assert_blocked_public(result)

    def test_missing_or_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            variants = []
            request = _request_for(artifact_path)
            request.pop("declared_non_claims")
            variants.append(("declared_non_claims_removed", request))
            request = _request_for(artifact_path)
            request["declared_non_claims"] = {}
            variants.append(("declared_non_claims_empty", request))
            request = _request_for(artifact_path)
            request["declared_non_claims"].pop("feed_created")
            variants.append(("one_required_non_claim_removed", request))
            request = _request_for(artifact_path)
            request["declared_non_claims"]["feed_created"] = "false"
            variants.append(("one_required_non_claim_string", request))
            request = _request_for(artifact_path)
            request["declared_non_claims"]["feed_created"] = None
            variants.append(("one_required_non_claim_none", request))

            for name, variant in variants:
                with self.subTest(variant=name):
                    result = (
                        resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min(
                            variant
                        )
                    )
                    self.assertIn(result["outcome"], {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS})
                    self.assert_public_block_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            result = resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min(
                _request_for(artifact_path)
            )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        entry = self.entry(result)
        self.assertEqual(
            entry["second_index_entry_type"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
        )
        self.assertEqual(entry["second_index_entry_scope"], "SECOND_LOCAL_INDEX_ENTRY_ONLY")
        for expected in (
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_NOT_RECORDED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_BLOCKED,
        ):
            self.assertIn(expected, resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY", serialized)
        self.assertIn("SECOND_LOCAL_INDEX_ENTRY_ONLY", serialized)
        self.assertNotIn("[REDACTED_HOSTILE_SENTINEL]", serialized)
        self.assertNotIn("[REDACTED_RAW_BODY_CONTENT]", serialized)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact = _synthetic_second_orientation_artifact()
            artifact["raw_full_body"] = HOSTILE_SENTINELS[0]
            artifact["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            artifact["second_relevance_orientation_view"]["raw_second_orientation_body"] = (
                HOSTILE_SENTINELS[2]
            )
            artifact_path = _write_json(tmp_path / "hostile_second_orientation.json", artifact)
            request = _request_for(
                artifact_path,
                raw_full_body=HOSTILE_SENTINELS[10],
                hidden_repo_state=HOSTILE_SENTINELS[-1],
                nested_payload={"raw_source_body": HOSTILE_SENTINELS[12]},
            )
            request_before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min(
                request
            )

        self.assertEqual(request, request_before)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY", serialized)
        self.assertIn("SECOND_LOCAL_INDEX_ENTRY_ONLY", serialized)
        self.assert_no_forbidden_creation(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact_path, _artifact = self.write_synthetic_artifact(tmp_path)
            request_path = _write_json(tmp_path / "request.json", _request_for(artifact_path))
            result = (
                resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_from_path(
                    request_path
                )
            )
            self.assert_successful_recorded_result(result, artifact_path)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(
                resolver.LocalRelevanceMediumSecondLocalRelevanceOrientationIndexEntryV0MinError
            ):
                resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_from_path(
                    malformed_path
                )

            array_request_path = _write_json(tmp_path / "array_request.json", [])
            array_result = (
                resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_from_path(
                    array_request_path
                )
            )
            self.assert_blocked_public(array_result)

            with self.assertRaises(
                resolver.LocalRelevanceMediumSecondLocalRelevanceOrientationIndexEntryV0MinError
            ):
                resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_from_path(
                    tmp_path / "missing_request.json"
                )

            output_root = tmp_path / "local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_result(
                    result
                )
            self.assertTrue(first_path.parent.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(second_path.name.endswith("_001.json"))
            self.assertIn(
                "local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min",
                str(first_path),
            )
            for written_path in (first_path, second_path):
                parsed = json.loads(written_path.read_text(encoding="utf-8"))
                self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
                for forbidden_root in FORBIDDEN_EXACT_OUTPUT_ROOTS:
                    self.assertFalse(_same_or_child(written_path, forbidden_root))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact = _synthetic_second_orientation_artifact()
            artifact_before = copy.deepcopy(artifact)
            artifact_path = _write_json(Path(tmp) / "non_mutation_artifact.json", artifact)
            request = _request_for(
                artifact_path,
                posture_mapping={"raw_source_body": HOSTILE_SENTINELS[12]},
            )
            request["declared_non_claims_mapping_alias"] = request["declared_non_claims"]
            request_before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min(
                request
            )
        self.assertEqual(artifact, artifact_before)
        self.assertEqual(request, request_before)
        self.assertEqual(request["selected_second_relevance_orientation_view_artifact"], str(artifact_path))
        self.assertEqual(request["second_index_entry_scope"], "SECOND_LOCAL_INDEX_ENTRY_ONLY")
        self.assertEqual(
            request["second_index_entry_type"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
        )
        self.assertEqual(request["declared_non_claims"], request_before["declared_non_claims"])
        self.assert_successful_recorded_result(result, artifact_path)

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            result = resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min(
                _request_for(artifact_path)
            )
            for flag in (
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
                "consumed_request_reopened",
                "authorization_token_reused",
            ):
                request = _request_for(artifact_path, **{flag: True})
                blocked = (
                    resolver.resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min(
                        request
                    )
                )
                with self.subTest(flag=flag):
                    self.assert_blocked_public(blocked)

        summary = self.summary(result)
        non_claims = result["non_claims"]
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(non_claims["predecessor_failure_repaired"], False)
        self.assertIs(non_claims["predecessor_failure_hidden"], False)
        self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
