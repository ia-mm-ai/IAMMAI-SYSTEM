"""Tests for the local relevance medium multiplicity result resolver.

This suite is bounded to one LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT object.
It verifies that the resolver reads one clean first local relevance orientation
index entry artifact and one clean second local relevance orientation index
entry artifact, preserves first and second locator, orientation, receipt,
reception, request/admission lineage, records exactly two locally discoverable
orientation objects, and keeps the multiplicity result object separate from
the resolver wrapper.

The suite does not create relation view, comparison view, index system,
registry, search, ranking, repeated reception permission, arbitrary reception,
feed, source transfer, source receipt, authority, currentness, truth, action,
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
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_local_relevance_medium_multiplicity_result_v0_min as resolver  # noqa: E402


DEFAULT_FIRST_LOCATOR_ARTIFACT = (
    REPO_ROOT
    / "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min/"
    "local_relevance_orientation_index_entry_reference_review_001__"
    "local_relevance_orientation_index_entry_v0_min_result.json"
)
DEFAULT_SECOND_LOCATOR_ARTIFACT = (
    REPO_ROOT
    / "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min/"
    "local_relevance_medium_second_local_relevance_orientation_index_entry_reference_review_001__"
    "local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_multiplicity_result_v0_min"
)
FORBIDDEN_EXACT_OUTPUT_ROOTS = (
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
    Path("artifacts/integrity_host_v0_min_coexistence_post_runtime_daemon_runtime_loop"),
    Path("artifacts/source-transfer"),
    Path("artifacts/source-receipt"),
    Path("artifacts/public-api"),
    Path("artifacts/participant-facing-interface"),
    Path("artifacts/distributed-network"),
)

FIRST_ORIENTATION_VIEW_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min/"
    "relevance_orientation_view_reference_review_001__relevance_orientation_view_v0_min_result.json"
)
SECOND_ORIENTATION_VIEW_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min/"
    "local_relevance_medium_second_relevance_orientation_view_reference_review_001__"
    "local_relevance_medium_second_relevance_orientation_view_v0_min_result.json"
)
FIRST_RECEIPT_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2/"
    "bounded_relevance_receipt_reference_review_001__bounded_relevance_receipt_v0_min_v2_result.json"
)
SECOND_RECEIPT_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_receipt_v0_min/"
    "local_relevance_medium_second_bounded_relevance_receipt_reference_review_001__"
    "local_relevance_medium_second_bounded_relevance_receipt_v0_min_result.json"
)
FIRST_RECEPTION_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min/"
    "bounded_relevance_reception_reference_review_001__bounded_relevance_reception_v0_min_result.json"
)
SECOND_RECEPTION_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_reception_v0_min/"
    "local_relevance_medium_second_bounded_relevance_reception_reference_review_001__"
    "local_relevance_medium_second_bounded_relevance_reception_v0_min_result.json"
)
SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_successor_candidate_admission_v0_min/"
    "local_relevance_medium_successor_candidate_admission_reference_review_001__"
    "local_relevance_medium_successor_candidate_admission_v0_min_result.json"
)
SUCCESSOR_RECEPTION_REQUEST_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_successor_reception_request_v0_min/"
    "local_relevance_medium_successor_reception_request_reference_review_001__"
    "local_relevance_medium_successor_reception_request_v0_min_result.json"
)

EXPECTED_TOP_LEVEL_SECTIONS = {
    "local_relevance_medium_multiplicity_result_metadata",
    "declared_local_relevance_medium_multiplicity_result_question",
    "selected_local_relevance_orientation_index_entry_artifact_basis",
    "local_relevance_medium_multiplicity_result",
    "local_relevance_medium_multiplicity_result_checks",
    "local_relevance_medium_multiplicity_result_statement",
    "local_relevance_medium_multiplicity_result_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_multiplicity_result_summary",
}

MULTIPLICITY_RESULT_FIELDS = {
    "multiplicity_result_id",
    "multiplicity_result_type",
    "multiplicity_result_version",
    "multiplicity_result_scope",
    "basis_first_local_relevance_orientation_index_entry_artifact",
    "basis_first_local_relevance_orientation_index_entry_outcome",
    "basis_first_local_relevance_orientation_index_entry_result_version",
    "basis_first_local_relevance_orientation_index_entry_failed_check_count",
    "basis_second_local_relevance_orientation_index_entry_artifact",
    "basis_second_local_relevance_orientation_index_entry_outcome",
    "basis_second_local_relevance_orientation_index_entry_result_version",
    "basis_second_local_relevance_orientation_index_entry_failed_check_count",
    "first_orientation_view_artifact",
    "second_orientation_view_artifact",
    "first_receipt_artifact",
    "second_receipt_artifact",
    "first_reception_artifact",
    "second_reception_artifact",
    "successor_candidate_admission_artifact",
    "successor_reception_request_artifact",
    "first_received_signal_id",
    "second_received_signal_id",
    "first_relevance_basis_id",
    "second_relevance_basis_id",
    "first_relevance_scope_id",
    "second_relevance_scope_id",
    "first_carrier_context_id",
    "second_carrier_context_id",
    "first_reception_envelope_id",
    "second_reception_envelope_id",
    "multiplicity_count",
    "two_local_orientation_locators_present",
    "first_locator_preserved",
    "second_locator_preserved",
    "first_and_second_signals_distinct",
    "basis_lineage_preserved",
    "multiplicity_result_recorded",
    "relation_view_created",
    "comparison_view_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
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
}

WRAPPER_KEYS_FORBIDDEN_IN_MULTIPLICITY_RESULT = {
    "outcome",
    "block",
    "local_relevance_medium_multiplicity_result_checks",
    "non_claims",
    "local_relevance_medium_multiplicity_result_summary",
    "local_relevance_medium_multiplicity_result_metadata",
}

MULTIPLICITY_RESULT_FALSE_FIELDS = {
    "relation_view_created",
    "comparison_view_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
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
}

EXPECTED_IDENTIFIERS = {
    "first_received_signal_id": "bounded_relevance_signal_001",
    "second_received_signal_id": "bounded_relevance_signal_002",
    "first_relevance_basis_id": "bounded_relevance_basis_001",
    "second_relevance_basis_id": "bounded_relevance_basis_002",
    "first_relevance_scope_id": "bounded_relevance_scope_001",
    "second_relevance_scope_id": "bounded_relevance_scope_002",
    "first_carrier_context_id": "bounded_relevance_signal_carrier_context_001",
    "second_carrier_context_id": "bounded_relevance_signal_carrier_context_002",
    "first_reception_envelope_id": "bounded_relevance_reception_envelope_001",
    "second_reception_envelope_id": "bounded_relevance_reception_envelope_002",
}

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_BODY_MUST_NOT_RETURN",
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


def _write_json(path: Path, payload: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _first_index_entry(**overrides: Any) -> dict[str, Any]:
    entry = {
        "index_entry_id": "local_relevance_orientation_index_entry_001",
        "index_entry_type": "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
        "index_entry_version": "0.1.0",
        "index_entry_scope": "LOCAL_INDEX_ENTRY_ONLY",
        "orientation_view_artifact": FIRST_ORIENTATION_VIEW_ARTIFACT,
        "orientation_view_outcome": "RELEVANCE_ORIENTATION_VIEW_RECORDED",
        "orientation_view_result_version": "0.1.0",
        "orientation_view_failed_check_count": 0,
        "orientation_scope": "LOCAL_ORIENTATION_ONLY",
        "source_receipt_artifact": FIRST_RECEIPT_ARTIFACT,
        "referenced_reception_artifact": FIRST_RECEPTION_ARTIFACT,
        "received_signal_id": "bounded_relevance_signal_001",
        "received_relevance_basis_id": "bounded_relevance_basis_001",
        "received_relevance_scope_id": "bounded_relevance_scope_001",
        "received_carrier_context_id": "bounded_relevance_signal_carrier_context_001",
        "received_reception_envelope_id": "bounded_relevance_reception_envelope_001",
        "local_discoverability": True,
    }
    entry.update(overrides)
    return entry


def _second_index_entry(**overrides: Any) -> dict[str, Any]:
    entry = {
        "second_index_entry_id": (
            "local_relevance_medium_second_local_relevance_orientation_index_entry_001"
        ),
        "second_index_entry_type": (
            "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY"
        ),
        "second_index_entry_version": "0.1.0",
        "second_index_entry_scope": "SECOND_LOCAL_INDEX_ENTRY_ONLY",
        "basis_second_relevance_orientation_view_artifact": SECOND_ORIENTATION_VIEW_ARTIFACT,
        "basis_second_relevance_orientation_view_outcome": (
            "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW_RECORDED"
        ),
        "basis_second_relevance_orientation_view_result_version": "0.1.0",
        "basis_second_relevance_orientation_view_failed_check_count": 0,
        "basis_second_bounded_relevance_receipt_artifact": SECOND_RECEIPT_ARTIFACT,
        "basis_second_bounded_relevance_reception_artifact": SECOND_RECEPTION_ARTIFACT,
        "basis_successor_candidate_admission_artifact": (
            SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT
        ),
        "basis_successor_reception_request_artifact": SUCCESSOR_RECEPTION_REQUEST_ARTIFACT,
        "basis_first_local_relevance_orientation_index_entry_artifact": (
            "artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min/"
            "local_relevance_orientation_index_entry_reference_review_001__"
            "local_relevance_orientation_index_entry_v0_min_result.json"
        ),
        "existing_orientation_view_artifact": FIRST_ORIENTATION_VIEW_ARTIFACT,
        "existing_source_receipt_artifact": FIRST_RECEIPT_ARTIFACT,
        "existing_referenced_reception_artifact": FIRST_RECEPTION_ARTIFACT,
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
        "local_discoverability": True,
    }
    entry.update(overrides)
    return entry


def _synthetic_first_locator_artifact(
    artifact_overrides: dict[str, Any] | None = None,
    entry_overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    artifact = {
        "outcome": "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED",
        "local_relevance_orientation_index_entry_metadata": {
            "local_relevance_orientation_index_entry_id": (
                "local_relevance_orientation_index_entry_001"
            ),
            "local_relevance_orientation_index_entry_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_orientation_index_entry_v0_min",
            "passed_check_count": 58,
            "failed_check_count": 0,
        },
        "local_relevance_orientation_index_entry_summary": {
            "outcome": "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED",
            "result_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_orientation_index_entry_v0_min",
            "passed_check_count": 58,
            "failed_check_count": 0,
        },
        "index_entry": _first_index_entry(**(entry_overrides or {})),
        "local_relevance_orientation_index_entry_checks": [
            {
                "check_name": "synthetic_clean_first_locator_basis",
                "passed": True,
                "expected_posture": "clean first local locator",
                "actual_posture": "clean first local locator",
                "block_code": None,
                "failure_code": None,
            }
        ],
    }
    if artifact_overrides:
        artifact.update(artifact_overrides)
    return artifact


def _synthetic_second_locator_artifact(
    artifact_overrides: dict[str, Any] | None = None,
    entry_overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    artifact = {
        "outcome": (
            "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED"
        ),
        "local_relevance_medium_second_local_relevance_orientation_index_entry_metadata": {
            "local_relevance_medium_second_local_relevance_orientation_index_entry_id": (
                "local_relevance_medium_second_local_relevance_orientation_index_entry_001"
            ),
            "local_relevance_medium_second_local_relevance_orientation_index_entry_version": (
                "0.1.0"
            ),
            "resolver_module": (
                "resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min"
            ),
            "passed_check_count": 84,
            "failed_check_count": 0,
        },
        "local_relevance_medium_second_local_relevance_orientation_index_entry_summary": {
            "outcome": (
                "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED"
            ),
            "result_version": "0.1.0",
            "resolver_module": (
                "resolve_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min"
            ),
            "passed_check_count": 84,
            "failed_check_count": 0,
        },
        "second_local_relevance_orientation_index_entry": _second_index_entry(
            **(entry_overrides or {})
        ),
        "local_relevance_medium_second_local_relevance_orientation_index_entry_checks": [
            {
                "check_name": "synthetic_clean_second_locator_basis",
                "passed": True,
                "expected_posture": "clean second local locator",
                "actual_posture": "clean second local locator",
                "block_code": None,
                "failure_code": None,
            }
        ],
    }
    if artifact_overrides:
        artifact.update(artifact_overrides)
    return artifact


def _request_for(first_path: Path | str, second_path: Path | str, **overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_local_relevance_medium_multiplicity_result_v0_min_request(
        selected_first_local_relevance_orientation_index_entry_artifact=first_path,
        selected_second_local_relevance_orientation_index_entry_artifact=second_path,
        **overrides,
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


class LocalRelevanceMediumMultiplicityResultTests(unittest.TestCase):
    def assert_not_blocked(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def multiplicity_result(self, result: dict[str, Any]) -> dict[str, Any]:
        multiplicity_result = result.get("local_relevance_medium_multiplicity_result")
        self.assertIsInstance(multiplicity_result, dict)
        return multiplicity_result

    def statement(self, result: dict[str, Any]) -> dict[str, Any]:
        statement = result.get("local_relevance_medium_multiplicity_result_statement")
        self.assertIsInstance(statement, dict)
        return statement

    def summary(self, result: dict[str, Any]) -> dict[str, Any]:
        summary = result.get("local_relevance_medium_multiplicity_result_summary")
        self.assertIsInstance(summary, dict)
        return summary

    def checks(self, result: dict[str, Any]) -> list[dict[str, Any]]:
        checks = result.get("local_relevance_medium_multiplicity_result_checks")
        self.assertIsInstance(checks, list)
        return checks

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
        multiplicity_result = self.multiplicity_result(result)
        for key in MULTIPLICITY_RESULT_FALSE_FIELDS:
            if key in multiplicity_result:
                self.assertIs(multiplicity_result[key], False, key)
        non_meaning = result.get("local_relevance_medium_multiplicity_result_non_meaning")
        self.assertIsInstance(non_meaning, dict)
        for key, value in non_meaning.items():
            self.assertIs(value, False, key)

    def assert_multiplicity_result_not_wrapper(
        self, multiplicity_result: dict[str, Any]
    ) -> None:
        for key in WRAPPER_KEYS_FORBIDDEN_IN_MULTIPLICITY_RESULT:
            self.assertNotIn(key, multiplicity_result)

    def assert_successful_recorded_result(
        self,
        result: dict[str, Any],
        first_path: Path | str,
        second_path: Path | str,
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        summary = self.summary(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_local_relevance_medium_multiplicity_result_v0_min",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            summary["multiplicity_result_id"],
            "local_relevance_medium_multiplicity_result_001",
        )
        self.assertTrue(EXPECTED_TOP_LEVEL_SECTIONS.issubset(result))

        multiplicity_result = self.multiplicity_result(result)
        self.assertTrue(MULTIPLICITY_RESULT_FIELDS.issubset(multiplicity_result))
        self.assertEqual(
            multiplicity_result["multiplicity_result_id"],
            "local_relevance_medium_multiplicity_result_001",
        )
        self.assertEqual(
            multiplicity_result["multiplicity_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT",
        )
        self.assertEqual(multiplicity_result["multiplicity_result_version"], "0.1.0")
        self.assertEqual(
            multiplicity_result["multiplicity_result_scope"],
            "TWO_LOCAL_ORIENTATION_LOCATORS_ONLY",
        )
        self.assertEqual(
            multiplicity_result[
                "basis_first_local_relevance_orientation_index_entry_outcome"
            ],
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED",
        )
        self.assertEqual(
            multiplicity_result[
                "basis_first_local_relevance_orientation_index_entry_result_version"
            ],
            "0.1.0",
        )
        self.assertEqual(
            multiplicity_result[
                "basis_first_local_relevance_orientation_index_entry_failed_check_count"
            ],
            0,
        )
        self.assertEqual(
            multiplicity_result[
                "basis_second_local_relevance_orientation_index_entry_outcome"
            ],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED",
        )
        self.assertEqual(
            multiplicity_result[
                "basis_second_local_relevance_orientation_index_entry_result_version"
            ],
            "0.1.0",
        )
        self.assertEqual(
            multiplicity_result[
                "basis_second_local_relevance_orientation_index_entry_failed_check_count"
            ],
            0,
        )
        self.assertEqual(
            multiplicity_result["basis_first_local_relevance_orientation_index_entry_artifact"],
            str(first_path),
        )
        self.assertEqual(
            multiplicity_result["basis_second_local_relevance_orientation_index_entry_artifact"],
            str(second_path),
        )
        self.assertEqual(
            multiplicity_result["first_orientation_view_artifact"],
            FIRST_ORIENTATION_VIEW_ARTIFACT,
        )
        self.assertEqual(
            multiplicity_result["second_orientation_view_artifact"],
            SECOND_ORIENTATION_VIEW_ARTIFACT,
        )
        self.assertEqual(multiplicity_result["first_receipt_artifact"], FIRST_RECEIPT_ARTIFACT)
        self.assertEqual(
            multiplicity_result["second_receipt_artifact"], SECOND_RECEIPT_ARTIFACT
        )
        self.assertEqual(
            multiplicity_result["first_reception_artifact"], FIRST_RECEPTION_ARTIFACT
        )
        self.assertEqual(
            multiplicity_result["second_reception_artifact"], SECOND_RECEPTION_ARTIFACT
        )
        self.assertEqual(
            multiplicity_result["successor_candidate_admission_artifact"],
            SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT,
        )
        self.assertEqual(
            multiplicity_result["successor_reception_request_artifact"],
            SUCCESSOR_RECEPTION_REQUEST_ARTIFACT,
        )
        for key, expected in EXPECTED_IDENTIFIERS.items():
            self.assertEqual(multiplicity_result[key], expected)
        self.assertNotEqual(
            multiplicity_result["first_received_signal_id"],
            multiplicity_result["second_received_signal_id"],
        )
        self.assertEqual(multiplicity_result["multiplicity_count"], 2)
        self.assertIs(multiplicity_result["two_local_orientation_locators_present"], True)
        self.assertIs(multiplicity_result["first_locator_preserved"], True)
        self.assertIs(multiplicity_result["second_locator_preserved"], True)
        self.assertIs(multiplicity_result["first_and_second_signals_distinct"], True)
        self.assertIs(multiplicity_result["basis_lineage_preserved"], True)
        self.assertIs(multiplicity_result["multiplicity_result_recorded"], True)
        for key in MULTIPLICITY_RESULT_FALSE_FIELDS:
            self.assertIs(multiplicity_result[key], False, key)
        self.assert_multiplicity_result_not_wrapper(multiplicity_result)

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

    def write_synthetic_artifacts(
        self,
        directory: Path,
        first_name: str = "synthetic_first_locator.json",
        second_name: str = "synthetic_second_locator.json",
        first_artifact_overrides: dict[str, Any] | None = None,
        second_artifact_overrides: dict[str, Any] | None = None,
        first_entry_overrides: dict[str, Any] | None = None,
        second_entry_overrides: dict[str, Any] | None = None,
        first_payload: Any | None = None,
        second_payload: Any | None = None,
    ) -> tuple[Path, Path, dict[str, Any], dict[str, Any]]:
        first_artifact = (
            first_payload
            if first_payload is not None
            else _synthetic_first_locator_artifact(
                artifact_overrides=first_artifact_overrides,
                entry_overrides=first_entry_overrides,
            )
        )
        second_artifact = (
            second_payload
            if second_payload is not None
            else _synthetic_second_locator_artifact(
                artifact_overrides=second_artifact_overrides,
                entry_overrides=second_entry_overrides,
            )
        )
        first_path = _write_json(directory / first_name, first_artifact)
        second_path = _write_json(directory / second_name, second_artifact)
        return first_path, second_path, first_artifact, second_artifact

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_local_relevance_medium_multiplicity_result_v0_min",
            "resolve_local_relevance_medium_multiplicity_result_v0_min_from_path",
            "write_local_relevance_medium_multiplicity_result_v0_min_result",
            "build_local_relevance_medium_multiplicity_result_v0_min_summary",
            "build_declared_local_relevance_medium_multiplicity_result_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_MULTIPLICITY_RESULT_SCOPE_VALUES",
            "SUPPORTED_MULTIPLICITY_RESULT_TYPE_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_multiplicity_result_v0_min",
        )
        self.assertTrue(str(Path(resolver.OUTPUT_ROOT)).endswith(str(EXPECTED_OUTPUT_ROOT)))
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT",
            resolver.SUPPORTED_MULTIPLICITY_RESULT_TYPE_VALUES,
        )
        self.assertIn(
            "TWO_LOCAL_ORIENTATION_LOCATORS_ONLY",
            resolver.SUPPORTED_MULTIPLICITY_RESULT_SCOPE_VALUES,
        )
        for forbidden_root in FORBIDDEN_EXACT_OUTPUT_ROOTS:
            self.assertFalse(_same_or_child(Path(resolver.OUTPUT_ROOT), forbidden_root))

    def test_successful_recorded_result_from_synthetic_locator_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, second_path, _first_artifact, _second_artifact = (
                self.write_synthetic_artifacts(Path(tmp))
            )
            request = _request_for(first_path, second_path)
            result = resolver.resolve_local_relevance_medium_multiplicity_result_v0_min(
                request
            )
        self.assert_successful_recorded_result(result, first_path, second_path)

    def test_successful_recorded_result_from_default_artifacts_if_present(self) -> None:
        if not DEFAULT_FIRST_LOCATOR_ARTIFACT.exists():
            self.skipTest("default first local relevance orientation index entry artifact absent")
        if not DEFAULT_SECOND_LOCATOR_ARTIFACT.exists():
            self.skipTest(
                "default second local relevance orientation index entry artifact absent"
            )
        request = resolver.build_declared_local_relevance_medium_multiplicity_result_v0_min_request()
        result = resolver.resolve_local_relevance_medium_multiplicity_result_v0_min(request)
        self.assert_successful_recorded_result(
            result,
            "artifacts/"
            "integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min/"
            "local_relevance_orientation_index_entry_reference_review_001__"
            "local_relevance_orientation_index_entry_v0_min_result.json",
            "artifacts/"
            "integrity_host_v0_min_coexistence_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min/"
            "local_relevance_medium_second_local_relevance_orientation_index_entry_reference_review_001__"
            "local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_result.json",
        )

    def test_required_false_non_claims_canonicalize_flipped_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, second_path, _first_artifact, _second_artifact = (
                self.write_synthetic_artifacts(Path(tmp))
            )
            clean_request = _request_for(first_path, second_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_multiplicity_result_v0_min(
                        request
                    )
                    self.assert_blocked_public(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertNotIn(": true", json.dumps(result["non_claims"], sort_keys=True))

    def test_representative_blocking_behavior(self) -> None:
        false_flag_cases = [
            "relation_view_created",
            "comparison_view_created",
            "index_system_created",
            "registry_created",
            "search_surface_created",
            "ranking_surface_created",
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
            "artifact_existence_treated_as_multiplicity_result_authority",
            "latest_file_posture_treated_as_multiplicity_result_authority",
            "repo_local_availability_treated_as_multiplicity_result_authority",
            "hidden_repo_state_used_as_multiplicity_result_content",
            "hidden_repo_state_used_as_multiplicity_result_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ]

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            base_first, base_second, _first_artifact, _second_artifact = (
                self.write_synthetic_artifacts(tmp_path, "base_first.json", "base_second.json")
            )

            def resolve_with(
                name: str,
                request_updates: dict[str, Any] | None = None,
                first_entry_updates: dict[str, Any] | None = None,
                second_entry_updates: dict[str, Any] | None = None,
                first_artifact_updates: dict[str, Any] | None = None,
                second_artifact_updates: dict[str, Any] | None = None,
                direct_request: Any = None,
                first_array_artifact: bool = False,
                second_array_artifact: bool = False,
                first_missing: bool = False,
                second_missing: bool = False,
                request_mutator: Any = None,
            ) -> dict[str, Any]:
                if direct_request is not None:
                    return resolver.resolve_local_relevance_medium_multiplicity_result_v0_min(
                        direct_request
                    )
                first_path = tmp_path / f"{name}_first.json"
                second_path = tmp_path / f"{name}_second.json"
                if first_missing:
                    first_path = tmp_path / f"{name}_first_absent.json"
                elif first_array_artifact:
                    _write_json(first_path, [])
                else:
                    first_artifact = _synthetic_first_locator_artifact(
                        artifact_overrides=first_artifact_updates,
                        entry_overrides=first_entry_updates,
                    )
                    _write_json(first_path, first_artifact)
                if second_missing:
                    second_path = tmp_path / f"{name}_second_absent.json"
                elif second_array_artifact:
                    _write_json(second_path, [])
                else:
                    second_artifact = _synthetic_second_locator_artifact(
                        artifact_overrides=second_artifact_updates,
                        entry_overrides=second_entry_updates,
                    )
                    _write_json(second_path, second_artifact)
                request = _request_for(first_path, second_path)
                if request_updates:
                    request.update(request_updates)
                if request_mutator:
                    request_mutator(request)
                return resolver.resolve_local_relevance_medium_multiplicity_result_v0_min(
                    request
                )

            cases: list[tuple[str, dict[str, Any]]] = [
                (
                    "explicit_block_intent",
                    {
                        "request_updates": {
                            "local_relevance_medium_multiplicity_result_intent": (
                                "BLOCK_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT"
                            )
                        }
                    },
                ),
                ("missing_request", {"direct_request": {}}),
                ("non_mapping_request", {"direct_request": "not a mapping"}),
                (
                    "unsupported_intent",
                    {
                        "request_updates": {
                            "local_relevance_medium_multiplicity_result_intent": (
                                "UNSUPPORTED_INTENT"
                            )
                        }
                    },
                ),
                (
                    "first_path_missing",
                    {
                        "request_updates": {
                            "selected_first_local_relevance_orientation_index_entry_artifact": ""
                        }
                    },
                ),
                (
                    "second_path_missing",
                    {
                        "request_updates": {
                            "selected_second_local_relevance_orientation_index_entry_artifact": ""
                        }
                    },
                ),
                ("first_path_unreadable", {"first_missing": True}),
                ("second_path_unreadable", {"second_missing": True}),
                ("first_json_array", {"first_array_artifact": True}),
                ("second_json_array", {"second_array_artifact": True}),
                (
                    "first_artifact_not_recorded",
                    {
                        "first_artifact_updates": {
                            "outcome": "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_NOT_RECORDED"
                        }
                    },
                ),
                (
                    "second_artifact_not_recorded",
                    {
                        "second_artifact_updates": {
                            "outcome": (
                                "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_NOT_RECORDED"
                            )
                        }
                    },
                ),
                (
                    "first_artifact_failed_checks",
                    {
                        "first_artifact_updates": {
                            "local_relevance_orientation_index_entry_metadata": {
                                "local_relevance_orientation_index_entry_version": "0.1.0",
                                "failed_check_count": 1,
                            }
                        }
                    },
                ),
                (
                    "second_artifact_failed_checks",
                    {
                        "second_artifact_updates": {
                            "local_relevance_medium_second_local_relevance_orientation_index_entry_metadata": {
                                "local_relevance_medium_second_local_relevance_orientation_index_entry_version": "0.1.0",
                                "failed_check_count": 1,
                            }
                        }
                    },
                ),
                (
                    "first_artifact_version_wrong",
                    {
                        "first_artifact_updates": {
                            "local_relevance_orientation_index_entry_metadata": {
                                "local_relevance_orientation_index_entry_version": "9.9.9",
                                "failed_check_count": 0,
                            }
                        }
                    },
                ),
                (
                    "second_artifact_version_wrong",
                    {
                        "second_artifact_updates": {
                            "local_relevance_medium_second_local_relevance_orientation_index_entry_metadata": {
                                "local_relevance_medium_second_local_relevance_orientation_index_entry_version": "9.9.9",
                                "failed_check_count": 0,
                            }
                        }
                    },
                ),
                ("first_object_missing", {"first_artifact_updates": {"index_entry": {}}}),
                (
                    "second_object_missing",
                    {
                        "second_artifact_updates": {
                            "second_local_relevance_orientation_index_entry": {}
                        }
                    },
                ),
                ("first_locator_artifact_missing", {"request_updates": {"first_locator_artifact_missing": True}}),
                ("second_locator_artifact_missing", {"request_updates": {"second_locator_artifact_missing": True}}),
                ("first_orientation_missing", {"first_entry_updates": {"orientation_view_artifact": ""}}),
                (
                    "second_orientation_missing",
                    {
                        "second_entry_updates": {
                            "basis_second_relevance_orientation_view_artifact": ""
                        }
                    },
                ),
                ("first_receipt_missing", {"first_entry_updates": {"source_receipt_artifact": ""}}),
                (
                    "second_receipt_missing",
                    {
                        "second_entry_updates": {
                            "basis_second_bounded_relevance_receipt_artifact": ""
                        }
                    },
                ),
                (
                    "first_reception_missing",
                    {"first_entry_updates": {"referenced_reception_artifact": ""}},
                ),
                (
                    "second_reception_missing",
                    {
                        "second_entry_updates": {
                            "basis_second_bounded_relevance_reception_artifact": ""
                        }
                    },
                ),
                ("first_signal_missing", {"first_entry_updates": {"received_signal_id": ""}}),
                (
                    "second_signal_missing",
                    {"second_entry_updates": {"second_received_signal_id": ""}},
                ),
                (
                    "signals_not_distinct",
                    {
                        "second_entry_updates": {
                            "second_received_signal_id": "bounded_relevance_signal_001"
                        }
                    },
                ),
                (
                    "first_basis_missing",
                    {"first_entry_updates": {"received_relevance_basis_id": ""}},
                ),
                (
                    "second_basis_missing",
                    {"second_entry_updates": {"second_relevance_basis_id": ""}},
                ),
                (
                    "first_scope_missing",
                    {"first_entry_updates": {"received_relevance_scope_id": ""}},
                ),
                (
                    "second_scope_missing",
                    {"second_entry_updates": {"second_relevance_scope_id": ""}},
                ),
                (
                    "first_context_missing",
                    {"first_entry_updates": {"received_carrier_context_id": ""}},
                ),
                (
                    "second_context_missing",
                    {"second_entry_updates": {"second_carrier_context_id": ""}},
                ),
                (
                    "first_envelope_missing",
                    {"first_entry_updates": {"received_reception_envelope_id": ""}},
                ),
                (
                    "second_envelope_missing",
                    {"second_entry_updates": {"second_reception_envelope_id": ""}},
                ),
                (
                    "multiplicity_type_missing",
                    {"request_mutator": lambda req: req.pop("multiplicity_result_type", None)},
                ),
                (
                    "multiplicity_type_wrong",
                    {"request_updates": {"multiplicity_result_type": "RELEVANCE_RELATION_VIEW"}},
                ),
                (
                    "multiplicity_scope_missing",
                    {"request_mutator": lambda req: req.pop("multiplicity_result_scope", None)},
                ),
                (
                    "multiplicity_scope_wrong",
                    {"request_updates": {"multiplicity_result_scope": "RELATION_SCOPE"}},
                ),
                ("multiplicity_count_not_two", {"request_updates": {"multiplicity_count": 3}}),
                (
                    "two_locators_not_present",
                    {"request_updates": {"two_local_orientation_locators_not_present": True}},
                ),
                ("basis_lineage_not_preserved", {"request_updates": {"basis_lineage_not_preserved": True}}),
                ("multiplicity_result_not_recorded", {"request_updates": {"multiplicity_result_not_recorded": True}}),
                (
                    "required_non_claim_missing",
                    {"request_mutator": lambda req: req["declared_non_claims"].pop("feed_created", None)},
                ),
            ]
            cases.extend((flag, {"request_updates": {flag: True}}) for flag in false_flag_cases)

            self.assertTrue(base_first.exists())
            self.assertTrue(base_second.exists())
            for name, kwargs in cases:
                with self.subTest(case=name):
                    result = resolve_with(name, **kwargs)
                    self.assert_blocked_public(result)

    def test_missing_or_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, second_path, _first_artifact, _second_artifact = (
                self.write_synthetic_artifacts(Path(tmp))
            )
            variants = []
            request = _request_for(first_path, second_path)
            request.pop("declared_non_claims")
            variants.append(("declared_non_claims_removed", request))
            request = _request_for(first_path, second_path)
            request["declared_non_claims"] = {}
            variants.append(("declared_non_claims_empty", request))
            request = _request_for(first_path, second_path)
            request["declared_non_claims"].pop("feed_created")
            variants.append(("one_required_non_claim_removed", request))
            request = _request_for(first_path, second_path)
            request["declared_non_claims"]["feed_created"] = "false"
            variants.append(("one_required_non_claim_string", request))
            request = _request_for(first_path, second_path)
            request["declared_non_claims"]["feed_created"] = None
            variants.append(("one_required_non_claim_none", request))

            for name, variant in variants:
                with self.subTest(variant=name):
                    result = resolver.resolve_local_relevance_medium_multiplicity_result_v0_min(
                        variant
                    )
                    self.assertIn(
                        result["outcome"],
                        {
                            resolver.OUTCOME_BLOCKED,
                            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                        },
                    )
                    self.assert_public_block_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, second_path, _first_artifact, _second_artifact = (
                self.write_synthetic_artifacts(Path(tmp))
            )
            result = resolver.resolve_local_relevance_medium_multiplicity_result_v0_min(
                _request_for(first_path, second_path)
            )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        multiplicity_result = self.multiplicity_result(result)
        self.assertEqual(
            multiplicity_result["multiplicity_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT",
        )
        self.assertEqual(
            multiplicity_result["multiplicity_result_scope"],
            "TWO_LOCAL_ORIENTATION_LOCATORS_ONLY",
        )
        for expected in (
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_NOT_RECORDED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_BLOCKED,
        ):
            self.assertIn(expected, resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT", serialized)
        self.assertIn("TWO_LOCAL_ORIENTATION_LOCATORS_ONLY", serialized)
        self.assertNotIn("[REDACTED_HOSTILE_SENTINEL]", serialized)
        self.assertNotIn("[REDACTED_RAW_BODY_CONTENT]", serialized)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            first_artifact = _synthetic_first_locator_artifact()
            second_artifact = _synthetic_second_locator_artifact()
            first_artifact["raw_full_body"] = HOSTILE_SENTINELS[2]
            first_artifact["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            first_artifact["index_entry"]["raw_first_orientation_body"] = HOSTILE_SENTINELS[4]
            second_artifact["raw_full_body"] = HOSTILE_SENTINELS[3]
            second_artifact["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            second_artifact["second_local_relevance_orientation_index_entry"][
                "raw_second_orientation_body"
            ] = HOSTILE_SENTINELS[5]
            first_path = _write_json(tmp_path / "hostile_first_locator.json", first_artifact)
            second_path = _write_json(tmp_path / "hostile_second_locator.json", second_artifact)
            request = _request_for(
                first_path,
                second_path,
                raw_full_body=HOSTILE_SENTINELS[0],
                hidden_repo_state=HOSTILE_SENTINELS[-1],
                nested_payload={"raw_source_body": HOSTILE_SENTINELS[12]},
            )
            request_before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_multiplicity_result_v0_min(
                request
            )

        self.assertEqual(request, request_before)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT", serialized)
        self.assertIn("TWO_LOCAL_ORIENTATION_LOCATORS_ONLY", serialized)
        self.assert_no_forbidden_creation(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            first_path, second_path, _first_artifact, _second_artifact = (
                self.write_synthetic_artifacts(tmp_path)
            )
            request_path = _write_json(tmp_path / "request.json", _request_for(first_path, second_path))
            result = resolver.resolve_local_relevance_medium_multiplicity_result_v0_min_from_path(
                request_path
            )
            self.assert_successful_recorded_result(result, first_path, second_path)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(resolver.LocalRelevanceMediumMultiplicityResultV0MinError):
                resolver.resolve_local_relevance_medium_multiplicity_result_v0_min_from_path(
                    malformed_path
                )

            array_request_path = _write_json(tmp_path / "array_request.json", [])
            array_result = (
                resolver.resolve_local_relevance_medium_multiplicity_result_v0_min_from_path(
                    array_request_path
                )
            )
            self.assert_blocked_public(array_result)

            with self.assertRaises(resolver.LocalRelevanceMediumMultiplicityResultV0MinError):
                resolver.resolve_local_relevance_medium_multiplicity_result_v0_min_from_path(
                    tmp_path / "missing_request.json"
                )

            output_root = tmp_path / "local_relevance_medium_multiplicity_result_v0_min"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_written = resolver.write_local_relevance_medium_multiplicity_result_v0_min_result(
                    result
                )
                second_written = resolver.write_local_relevance_medium_multiplicity_result_v0_min_result(
                    result
                )
            self.assertTrue(first_written.parent.exists())
            self.assertNotEqual(first_written, second_written)
            self.assertTrue(second_written.name.endswith("_001.json"))
            self.assertIn("local_relevance_medium_multiplicity_result_v0_min", str(first_written))
            for written_path in (first_written, second_written):
                parsed = json.loads(written_path.read_text(encoding="utf-8"))
                self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
                for forbidden_root in FORBIDDEN_EXACT_OUTPUT_ROOTS:
                    self.assertFalse(_same_or_child(written_path, forbidden_root))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_artifact = _synthetic_first_locator_artifact()
            second_artifact = _synthetic_second_locator_artifact()
            first_artifact_before = copy.deepcopy(first_artifact)
            second_artifact_before = copy.deepcopy(second_artifact)
            first_path = _write_json(Path(tmp) / "non_mutation_first.json", first_artifact)
            second_path = _write_json(Path(tmp) / "non_mutation_second.json", second_artifact)
            request = _request_for(
                first_path,
                second_path,
                posture_mapping={"raw_source_body": HOSTILE_SENTINELS[12]},
            )
            request["declared_non_claims_mapping_alias"] = request["declared_non_claims"]
            request_before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_multiplicity_result_v0_min(
                request
            )
        self.assertEqual(first_artifact, first_artifact_before)
        self.assertEqual(second_artifact, second_artifact_before)
        self.assertEqual(request, request_before)
        self.assertEqual(
            request["selected_first_local_relevance_orientation_index_entry_artifact"],
            str(first_path),
        )
        self.assertEqual(
            request["selected_second_local_relevance_orientation_index_entry_artifact"],
            str(second_path),
        )
        self.assertEqual(
            request["multiplicity_result_scope"],
            "TWO_LOCAL_ORIENTATION_LOCATORS_ONLY",
        )
        self.assertEqual(
            request["multiplicity_result_type"],
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT",
        )
        self.assertEqual(request["declared_non_claims"], request_before["declared_non_claims"])
        self.assert_successful_recorded_result(result, first_path, second_path)

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first_path, second_path, _first_artifact, _second_artifact = (
                self.write_synthetic_artifacts(Path(tmp))
            )
            result = resolver.resolve_local_relevance_medium_multiplicity_result_v0_min(
                _request_for(first_path, second_path)
            )
            for flag in (
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
                "consumed_request_reopened",
                "authorization_token_reused",
            ):
                request = _request_for(first_path, second_path, **{flag: True})
                blocked = resolver.resolve_local_relevance_medium_multiplicity_result_v0_min(
                    request
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
