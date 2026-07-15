"""Tests for the local relevance medium relation view resolver.

This suite is bounded to one LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW object. It
verifies that the resolver reads one clean local relevance medium multiplicity
result artifact, preserves multiplicity, locator, orientation, receipt,
reception, request/admission lineage, records bounded relation-readable
co-presence only, and keeps the relation view object separate from the resolver
wrapper.

The suite does not create comparison view, index system, registry, search,
ranking, repeated reception permission, arbitrary reception, feed, source
transfer, source receipt, authority, currentness, truth, action,
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

import resolve_local_relevance_medium_relation_view_v0_min as resolver  # noqa: E402


DEFAULT_MULTIPLICITY_RESULT_ARTIFACT = (
    REPO_ROOT
    / "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_multiplicity_result_v0_min/"
    "local_relevance_medium_multiplicity_result_reference_review_001__"
    "local_relevance_medium_multiplicity_result_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_relation_view_v0_min"
)
FORBIDDEN_EXACT_OUTPUT_ROOTS = (
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
    Path("artifacts/integrity_host_v0_min_coexistence_post_runtime_daemon_runtime_loop"),
    Path("artifacts/source-transfer"),
    Path("artifacts/source-receipt"),
    Path("artifacts/public-api"),
    Path("artifacts/participant-facing-interface"),
    Path("artifacts/distributed-network"),
)

FIRST_LOCATOR_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min/"
    "local_relevance_orientation_index_entry_reference_review_001__"
    "local_relevance_orientation_index_entry_v0_min_result.json"
)
SECOND_LOCATOR_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min/"
    "local_relevance_medium_second_local_relevance_orientation_index_entry_reference_review_001__"
    "local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_result.json"
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
    "local_relevance_medium_relation_view_metadata",
    "declared_local_relevance_medium_relation_view_question",
    "selected_local_relevance_medium_multiplicity_result_artifact_basis",
    "local_relevance_medium_relation_view",
    "local_relevance_medium_relation_view_checks",
    "local_relevance_medium_relation_view_statement",
    "local_relevance_medium_relation_view_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_relation_view_summary",
}

WRAPPER_FIELDS_FORBIDDEN_IN_RELATION_VIEW = {
    "outcome",
    "block",
    "local_relevance_medium_relation_view_checks",
    "non_claims",
    "local_relevance_medium_relation_view_summary",
    "local_relevance_medium_relation_view_metadata",
}

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_BODY_MUST_NOT_RETURN",
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


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _relation_view(result: dict[str, Any]) -> dict[str, Any]:
    relation_view = result.get("local_relevance_medium_relation_view")
    if not isinstance(relation_view, dict):
        raise AssertionError("local_relevance_medium_relation_view is not a dict")
    return relation_view


def _statement(result: dict[str, Any]) -> dict[str, Any]:
    statement = result.get("local_relevance_medium_relation_view_statement")
    if not isinstance(statement, dict):
        raise AssertionError("local_relevance_medium_relation_view_statement is not a dict")
    return statement


def _non_claims(result: dict[str, Any]) -> dict[str, Any]:
    non_claims = result.get("non_claims")
    if not isinstance(non_claims, dict):
        raise AssertionError("non_claims is not a dict")
    return non_claims


def _checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    checks = result.get("local_relevance_medium_relation_view_checks")
    if not isinstance(checks, list):
        raise AssertionError("local_relevance_medium_relation_view_checks is not a list")
    return checks


def _summary(result: dict[str, Any]) -> dict[str, Any]:
    summary = result.get("local_relevance_medium_relation_view_summary")
    if not isinstance(summary, dict):
        raise AssertionError("local_relevance_medium_relation_view_summary is not a dict")
    return summary


def _block_code(result: dict[str, Any]) -> str | None:
    block = result.get("block")
    if isinstance(block, dict):
        code = block.get("block_code") or block.get("code")
        return code if isinstance(code, str) else None
    return None


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _clean_multiplicity_result_object() -> dict[str, Any]:
    return {
        "multiplicity_result_id": "local_relevance_medium_multiplicity_result_001",
        "multiplicity_result_type": "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT",
        "multiplicity_result_version": "0.1.0",
        "multiplicity_result_scope": "TWO_LOCAL_ORIENTATION_LOCATORS_ONLY",
        "basis_first_local_relevance_orientation_index_entry_artifact": FIRST_LOCATOR_ARTIFACT,
        "basis_first_local_relevance_orientation_index_entry_outcome": (
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED"
        ),
        "basis_first_local_relevance_orientation_index_entry_result_version": "0.1.0",
        "basis_first_local_relevance_orientation_index_entry_failed_check_count": 0,
        "basis_second_local_relevance_orientation_index_entry_artifact": SECOND_LOCATOR_ARTIFACT,
        "basis_second_local_relevance_orientation_index_entry_outcome": (
            "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED"
        ),
        "basis_second_local_relevance_orientation_index_entry_result_version": "0.1.0",
        "basis_second_local_relevance_orientation_index_entry_failed_check_count": 0,
        "first_orientation_view_artifact": FIRST_ORIENTATION_VIEW_ARTIFACT,
        "second_orientation_view_artifact": SECOND_ORIENTATION_VIEW_ARTIFACT,
        "first_receipt_artifact": FIRST_RECEIPT_ARTIFACT,
        "second_receipt_artifact": SECOND_RECEIPT_ARTIFACT,
        "first_reception_artifact": FIRST_RECEPTION_ARTIFACT,
        "second_reception_artifact": SECOND_RECEPTION_ARTIFACT,
        "successor_candidate_admission_artifact": SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT,
        "successor_reception_request_artifact": SUCCESSOR_RECEPTION_REQUEST_ARTIFACT,
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
        "multiplicity_count": 2,
        "two_local_orientation_locators_present": True,
        "first_locator_preserved": True,
        "second_locator_preserved": True,
        "first_and_second_signals_distinct": True,
        "basis_lineage_preserved": True,
        "multiplicity_result_recorded": True,
        "relation_view_created": False,
        "comparison_view_created": False,
        "index_system_created": False,
        "registry_created": False,
        "search_surface_created": False,
        "ranking_surface_created": False,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "authority_created": False,
        "currentness_created": False,
        "truth_created": False,
        "action_created": False,
        "synchronization_created": False,
        "participation_authorized": False,
        "participant_role_created": False,
        "runtime_permission_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "follow_on_work_authorized": False,
    }


def _clean_multiplicity_result_artifact() -> dict[str, Any]:
    return {
        "local_relevance_medium_multiplicity_result_metadata": {
            "local_relevance_medium_multiplicity_result_id": (
                "local_relevance_medium_multiplicity_result_001"
            ),
            "local_relevance_medium_multiplicity_result_type": (
                "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT"
            ),
            "local_relevance_medium_multiplicity_result_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_multiplicity_result_v0_min",
        },
        "local_relevance_medium_multiplicity_result_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_RECORDED",
            "failed_check_count": 0,
            "passed_check_count": 91,
            "result_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_multiplicity_result_v0_min",
        },
        "local_relevance_medium_multiplicity_result_checks": [
            {
                "check_name": "synthetic clean multiplicity result",
                "passed": True,
                "expected_posture": "clean multiplicity result",
                "actual_posture": "clean multiplicity result",
            }
        ],
        "local_relevance_medium_multiplicity_result": _clean_multiplicity_result_object(),
        "outcome": "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_RECORDED",
    }


def _write_synthetic_multiplicity_result_artifact(
    directory: Path,
    artifact: dict[str, Any] | None = None,
) -> tuple[Path, dict[str, Any]]:
    artifact_body = copy.deepcopy(artifact or _clean_multiplicity_result_artifact())
    path = directory / "synthetic_multiplicity_result.json"
    _write_json(path, artifact_body)
    return path, artifact_body


def _clean_request(artifact_path: Path | str) -> dict[str, Any]:
    return resolver.build_declared_local_relevance_medium_relation_view_v0_min_request(
        selected_local_relevance_medium_multiplicity_result_artifact=artifact_path
    )


def _resolve_with_artifact(
    directory: Path,
    artifact: dict[str, Any] | None = None,
    request_updates: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], Path, dict[str, Any], dict[str, Any]]:
    path, artifact_body = _write_synthetic_multiplicity_result_artifact(directory, artifact)
    request = _clean_request(path)
    if request_updates:
        request.update(copy.deepcopy(request_updates))
    request_before = copy.deepcopy(request)
    result = resolver.resolve_local_relevance_medium_relation_view_v0_min(request)
    return result, path, artifact_body, request_before


class LocalRelevanceMediumRelationViewTests(unittest.TestCase):
    def assert_not_blocked(self, result):
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_output_not_under_prior_roots(self, output_path: Path) -> None:
        path = Path(output_path)
        for forbidden in FORBIDDEN_EXACT_OUTPUT_ROOTS:
            self.assertFalse(path == forbidden)
            self.assertFalse(_is_relative_to(path, forbidden))

    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        block_code = _block_code(result)
        if block_code is not None:
            self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in _checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: dict[str, Any]) -> None:
        non_claims = _non_claims(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)

    def assert_no_overreach_created(self, result: dict[str, Any]) -> None:
        non_claims = _non_claims(result)
        for key in (
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
            "operation_permission_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(non_claims[key], False)

    def assert_relation_view_not_wrapper(self, relation_view: dict[str, Any]) -> None:
        for key in WRAPPER_FIELDS_FORBIDDEN_IN_RELATION_VIEW:
            self.assertNotIn(key, relation_view)

    def assert_recorded_relation_view_shape(
        self, result: dict[str, Any], artifact_path: Path
    ) -> None:
        relation_view = _relation_view(result)
        self.assertEqual(
            relation_view["relation_view_id"], "local_relevance_medium_relation_view_001"
        )
        self.assertEqual(
            relation_view["relation_view_type"], "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW"
        )
        self.assertEqual(relation_view["relation_view_version"], "0.1.0")
        self.assertEqual(
            relation_view["relation_view_scope"],
            "TWO_LOCAL_ORIENTATION_OBJECTS_RELATION_VIEW_ONLY",
        )
        self.assertEqual(
            relation_view["relation_frame"],
            "BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY",
        )
        self.assertEqual(
            relation_view["basis_local_relevance_medium_multiplicity_result_artifact"],
            str(artifact_path),
        )
        self.assertEqual(
            relation_view["basis_local_relevance_medium_multiplicity_result_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_RECORDED",
        )
        self.assertEqual(
            relation_view["basis_local_relevance_medium_multiplicity_result_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            relation_view["basis_local_relevance_medium_multiplicity_result_failed_check_count"],
            0,
        )
        self.assertEqual(
            relation_view["basis_first_local_relevance_orientation_index_entry_artifact"],
            FIRST_LOCATOR_ARTIFACT,
        )
        self.assertEqual(
            relation_view["basis_second_local_relevance_orientation_index_entry_artifact"],
            SECOND_LOCATOR_ARTIFACT,
        )
        self.assertEqual(
            relation_view["first_orientation_view_artifact"],
            FIRST_ORIENTATION_VIEW_ARTIFACT,
        )
        self.assertEqual(
            relation_view["second_orientation_view_artifact"],
            SECOND_ORIENTATION_VIEW_ARTIFACT,
        )
        self.assertEqual(relation_view["first_receipt_artifact"], FIRST_RECEIPT_ARTIFACT)
        self.assertEqual(
            relation_view["second_receipt_artifact"], SECOND_RECEIPT_ARTIFACT
        )
        self.assertEqual(
            relation_view["first_reception_artifact"], FIRST_RECEPTION_ARTIFACT
        )
        self.assertEqual(
            relation_view["second_reception_artifact"], SECOND_RECEPTION_ARTIFACT
        )
        self.assertEqual(
            relation_view["successor_candidate_admission_artifact"],
            SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT,
        )
        self.assertEqual(
            relation_view["successor_reception_request_artifact"],
            SUCCESSOR_RECEPTION_REQUEST_ARTIFACT,
        )
        self.assertEqual(
            relation_view["first_received_signal_id"], "bounded_relevance_signal_001"
        )
        self.assertEqual(
            relation_view["second_received_signal_id"], "bounded_relevance_signal_002"
        )
        self.assertNotEqual(
            relation_view["first_received_signal_id"],
            relation_view["second_received_signal_id"],
        )
        self.assertEqual(
            relation_view["first_relevance_basis_id"], "bounded_relevance_basis_001"
        )
        self.assertEqual(
            relation_view["second_relevance_basis_id"], "bounded_relevance_basis_002"
        )
        self.assertEqual(
            relation_view["first_relevance_scope_id"], "bounded_relevance_scope_001"
        )
        self.assertEqual(
            relation_view["second_relevance_scope_id"], "bounded_relevance_scope_002"
        )
        self.assertEqual(
            relation_view["first_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_001",
        )
        self.assertEqual(
            relation_view["second_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_002",
        )
        self.assertEqual(
            relation_view["first_reception_envelope_id"],
            "bounded_relevance_reception_envelope_001",
        )
        self.assertEqual(
            relation_view["second_reception_envelope_id"],
            "bounded_relevance_reception_envelope_002",
        )
        self.assertEqual(relation_view["multiplicity_count"], 2)
        self.assertEqual(relation_view["relation_pair_count"], 1)
        self.assertIs(relation_view["two_local_orientation_objects_preserved"], True)
        self.assertIs(relation_view["first_and_second_signals_distinct"], True)
        self.assertIs(relation_view["relation_readable_co_presence_recorded"], True)
        self.assertIs(relation_view["relation_view_recorded"], True)
        for key in (
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
        ):
            self.assertIs(relation_view[key], False)
        self.assert_relation_view_not_wrapper(relation_view)

    def assert_recorded_statement_shape(self, result: dict[str, Any]) -> None:
        statement = _statement(result)
        for key in (
            "local_relevance_medium_relation_view_recorded",
            "basis_local_relevance_medium_multiplicity_result_artifact_preserved",
            "basis_first_local_relevance_orientation_index_entry_artifact_preserved",
            "basis_second_local_relevance_orientation_index_entry_artifact_preserved",
            "first_orientation_view_artifact_preserved",
            "second_orientation_view_artifact_preserved",
            "first_receipt_artifact_preserved",
            "second_receipt_artifact_preserved",
            "first_reception_artifact_preserved",
            "second_reception_artifact_preserved",
            "successor_candidate_admission_artifact_preserved",
            "successor_reception_request_artifact_preserved",
            "first_received_signal_id_preserved",
            "second_received_signal_id_preserved",
            "first_and_second_signals_distinct",
            "first_relevance_basis_id_preserved",
            "second_relevance_basis_id_preserved",
            "first_relevance_scope_id_preserved",
            "second_relevance_scope_id_preserved",
            "first_carrier_context_id_preserved",
            "second_carrier_context_id_preserved",
            "first_reception_envelope_id_preserved",
            "second_reception_envelope_id_preserved",
            "relation_view_scope_local_only",
            "relation_frame_bounded_co_presence_only",
            "relation_pair_count_is_one",
            "relation_readable_co_presence_recorded",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(statement[key], True)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_local_relevance_medium_relation_view_v0_min",
            "resolve_local_relevance_medium_relation_view_v0_min_from_path",
            "write_local_relevance_medium_relation_view_v0_min_result",
            "build_local_relevance_medium_relation_view_v0_min_summary",
            "build_declared_local_relevance_medium_relation_view_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_RELATION_VIEW_SCOPE_VALUES",
            "SUPPORTED_RELATION_VIEW_TYPE_VALUES",
            "SUPPORTED_RELATION_FRAME_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_relation_view_v0_min",
        )
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW",
            resolver.SUPPORTED_RELATION_VIEW_TYPE_VALUES,
        )
        self.assertIn(
            "TWO_LOCAL_ORIENTATION_OBJECTS_RELATION_VIEW_ONLY",
            resolver.SUPPORTED_RELATION_VIEW_SCOPE_VALUES,
        )
        self.assertIn(
            "BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY",
            resolver.SUPPORTED_RELATION_FRAME_VALUES,
        )
        self.assert_output_not_under_prior_roots(Path(resolver.OUTPUT_ROOT))

    def test_successful_recorded_result_from_synthetic_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result, artifact_path, _artifact, _request = _resolve_with_artifact(Path(tmp))

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(_summary(result)["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(_summary(result)["result_version"], "0.1.0")
        self.assertEqual(
            _summary(result)["resolver_module"],
            "resolve_local_relevance_medium_relation_view_v0_min",
        )
        self.assertGreater(_summary(result)["passed_check_count"], 0)
        self.assertEqual(_summary(result)["relation_view_id"], "local_relevance_medium_relation_view_001")
        self.assertTrue(EXPECTED_TOP_LEVEL_SECTIONS.issubset(result.keys()))
        self.assert_recorded_relation_view_shape(result, artifact_path)
        self.assert_recorded_statement_shape(result)
        self.assert_non_claims_canonical_false(result)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_MULTIPLICITY_RESULT_ARTIFACT.exists():
            self.skipTest("default local relevance medium multiplicity result artifact is absent")
        request = resolver.build_declared_local_relevance_medium_relation_view_v0_min_request()
        result = resolver.resolve_local_relevance_medium_relation_view_v0_min(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(_summary(result)["failed_check_count"], 0)
        self.assert_not_blocked(result)
        relation_view = _relation_view(result)
        self.assertEqual(
            relation_view["relation_view_type"], "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW"
        )
        self.assertEqual(
            relation_view["relation_view_scope"],
            "TWO_LOCAL_ORIENTATION_OBJECTS_RELATION_VIEW_ONLY",
        )
        self.assertEqual(
            relation_view["relation_frame"],
            "BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY",
        )
        self.assertEqual(relation_view["first_received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(relation_view["second_received_signal_id"], "bounded_relevance_signal_002")
        self.assertNotEqual(
            relation_view["first_received_signal_id"],
            relation_view["second_received_signal_id"],
        )
        self.assertEqual(relation_view["multiplicity_count"], 2)
        self.assertEqual(relation_view["relation_pair_count"], 1)
        self.assertIs(relation_view["relation_readable_co_presence_recorded"], True)
        self.assert_no_overreach_created(result)

    def test_critical_non_claim_canonicalization_blocks_flipped_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = _write_synthetic_multiplicity_result_artifact(Path(tmp))
            clean_request = _clean_request(artifact_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_relation_view_v0_min(request)
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assertIsNotNone(_block_code(result))
                    self.assert_public_block_codes(result)
                    self.assertGreater(_summary(result)["failed_check_count"], 0)
                    self.assert_non_claims_canonical_false(result)
                    self.assertIs(_non_claims(result)[key], False)
                    self.assert_no_overreach_created(result)

    def test_representative_blocking_behavior(self) -> None:
        def mutate_artifact(field: str, value: Any = None, remove: bool = False):
            def inner(artifact: dict[str, Any]) -> None:
                obj = artifact["local_relevance_medium_multiplicity_result"]
                if remove:
                    obj.pop(field, None)
                else:
                    obj[field] = value

            return inner

        def mutate_summary(field: str, value: Any):
            def inner(artifact: dict[str, Any]) -> None:
                artifact["local_relevance_medium_multiplicity_result_summary"][field] = value

            return inner

        def mutate_metadata(field: str, value: Any):
            def inner(artifact: dict[str, Any]) -> None:
                artifact["local_relevance_medium_multiplicity_result_metadata"][field] = value

            return inner

        def mutate_top_level(field: str, value: Any):
            def inner(artifact: dict[str, Any]) -> None:
                artifact[field] = value

            return inner

        cases: list[tuple[str, dict[str, Any], Any | None, str | None]] = [
            ("explicit block intent", {"local_relevance_medium_relation_view_intent": resolver.INTENT_BLOCK}, None, None),
            ("unsupported intent", {"local_relevance_medium_relation_view_intent": "UNSUPPORTED"}, None, None),
            ("path missing", {"selected_local_relevance_medium_multiplicity_result_artifact": ""}, None, None),
            ("artifact not recorded", {}, mutate_top_level("outcome", "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_NOT_RECORDED"), None),
            ("artifact failed checks present", {}, mutate_summary("failed_check_count", 1), None),
            ("artifact version not 0.1.0", {}, mutate_metadata("local_relevance_medium_multiplicity_result_version", "9.9.9"), None),
            ("object missing", {}, lambda artifact: artifact.pop("local_relevance_medium_multiplicity_result", None), None),
            ("multiplicity type wrong", {}, mutate_artifact("multiplicity_result_type", "WRONG"), None),
            ("multiplicity scope wrong", {}, mutate_artifact("multiplicity_result_scope", "WRONG"), None),
            ("multiplicity count wrong", {}, mutate_artifact("multiplicity_count", 3), None),
            ("first locator missing", {}, mutate_artifact("basis_first_local_relevance_orientation_index_entry_artifact", remove=True), None),
            ("second locator missing", {}, mutate_artifact("basis_second_local_relevance_orientation_index_entry_artifact", remove=True), None),
            ("first orientation missing", {}, mutate_artifact("first_orientation_view_artifact", remove=True), None),
            ("second orientation missing", {}, mutate_artifact("second_orientation_view_artifact", remove=True), None),
            ("first receipt missing", {}, mutate_artifact("first_receipt_artifact", remove=True), None),
            ("second receipt missing", {}, mutate_artifact("second_receipt_artifact", remove=True), None),
            ("first reception missing", {}, mutate_artifact("first_reception_artifact", remove=True), None),
            ("second reception missing", {}, mutate_artifact("second_reception_artifact", remove=True), None),
            ("first signal missing", {}, mutate_artifact("first_received_signal_id", remove=True), None),
            ("second signal missing", {}, mutate_artifact("second_received_signal_id", remove=True), None),
            ("signals not distinct", {}, mutate_artifact("second_received_signal_id", "bounded_relevance_signal_001"), None),
            ("first basis missing", {}, mutate_artifact("first_relevance_basis_id", remove=True), None),
            ("second basis missing", {}, mutate_artifact("second_relevance_basis_id", remove=True), None),
            ("first scope missing", {}, mutate_artifact("first_relevance_scope_id", remove=True), None),
            ("second scope missing", {}, mutate_artifact("second_relevance_scope_id", remove=True), None),
            ("first context missing", {}, mutate_artifact("first_carrier_context_id", remove=True), None),
            ("second context missing", {}, mutate_artifact("second_carrier_context_id", remove=True), None),
            ("first envelope missing", {}, mutate_artifact("first_reception_envelope_id", remove=True), None),
            ("second envelope missing", {}, mutate_artifact("second_reception_envelope_id", remove=True), None),
            ("relation type missing", {"relation_view_type": ""}, None, None),
            ("relation type wrong", {"relation_view_type": "WRONG"}, None, None),
            ("relation scope missing", {"relation_view_scope": ""}, None, None),
            ("relation scope wrong", {"relation_view_scope": "WRONG"}, None, None),
            ("relation frame missing", {"relation_frame": ""}, None, None),
            ("relation frame wrong", {"relation_frame": "WRONG"}, None, None),
            ("relation pair count not one", {"relation_pair_count": 2}, None, None),
            ("co-presence not recorded", {"relation_readable_co_presence_recorded": False}, None, None),
            ("relation view not recorded", {"relation_view_recorded": False}, None, None),
            ("comparison view created", {"comparison_view_created": True}, None, None),
            ("index system created", {"index_system_created": True}, None, None),
            ("registry created", {"registry_created": True}, None, None),
            ("search created", {"search_surface_created": True}, None, None),
            ("ranking created", {"ranking_surface_created": True}, None, None),
            ("repeated permission created", {"repeated_reception_permission_created": True}, None, None),
            ("arbitrary reception created", {"arbitrary_reception_created": True}, None, None),
            ("feed created", {"feed_created": True}, None, None),
            ("source transfer occurred", {"source_transfer_occurred": True}, None, None),
            ("source receipt occurred", {"source_receipt_occurred": True}, None, None),
            ("source created", {"source_created": True}, None, None),
            ("authority created", {"authority_created": True}, None, None),
            ("currentness created", {"currentness_created": True}, None, None),
            ("truth created", {"truth_created": True}, None, None),
            ("action created", {"action_created": True}, None, None),
            ("synchronization created", {"synchronization_created": True}, None, None),
            ("participation authorized", {"participation_authorized": True}, None, None),
            ("participant role created", {"participant_role_created": True}, None, None),
            ("runtime permission created", {"runtime_permission_created": True}, None, None),
            ("public API created", {"public_api_created": True}, None, None),
            ("participant-facing interface created", {"participant_facing_interface_created": True}, None, None),
            ("distributed behavior created", {"distributed_network_behavior_created": True}, None, None),
            ("deployment created", {"deployment_created": True}, None, None),
            ("public release created", {"public_release_created": True}, None, None),
            ("operation permission created", {"operation_permission_created": True}, None, None),
            ("broader reusable permission created", {"broader_reusable_permission_created": True}, None, None),
            ("follow-on work authorized", {"follow_on_work_authorized": True}, None, None),
            ("artifact existence as authority", {"artifact_existence_treated_as_relation_view_authority": True}, None, None),
            ("latest posture as authority", {"latest_file_posture_treated_as_relation_view_authority": True}, None, None),
            ("repo local as authority", {"repo_local_availability_treated_as_relation_view_authority": True}, None, None),
            ("hidden content used", {"hidden_repo_state_used_as_relation_view_content": True}, None, None),
            ("hidden authority used", {"hidden_repo_state_used_as_relation_view_authority": True}, None, None),
            ("predecessor repaired", {"predecessor_failure_repaired": True}, None, None),
            ("predecessor hidden", {"predecessor_failure_hidden": True}, None, None),
            ("predecessor claimed passed", {"predecessor_failure_claimed_passed": True}, None, None),
            ("consumed request reopened", {"consumed_request_reopened": True}, None, None),
            ("authorization token reused", {"authorization_token_reused": True}, None, None),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            for name, request_updates, artifact_mutator, _expected_code in cases:
                with self.subTest(name=name):
                    artifact = _clean_multiplicity_result_artifact()
                    if artifact_mutator is not None:
                        artifact_mutator(artifact)
                    result, _path, _artifact, _request = _resolve_with_artifact(
                        tmp_path, artifact=artifact, request_updates=request_updates
                    )
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assertIsNotNone(_block_code(result))
                    self.assert_public_block_codes(result)
                    self.assert_no_overreach_created(result)
                    self.assert_non_claims_canonical_false(result)

            with self.subTest(name="missing request"):
                result = resolver.resolve_local_relevance_medium_relation_view_v0_min()
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assert_public_block_codes(result)
                self.assert_non_claims_canonical_false(result)

            with self.subTest(name="non-mapping request"):
                result = resolver.resolve_local_relevance_medium_relation_view_v0_min(["bad"])
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assert_public_block_codes(result)
                self.assert_non_claims_canonical_false(result)

            with self.subTest(name="artifact unreadable"):
                request = _clean_request(tmp_path / "missing.json")
                result = resolver.resolve_local_relevance_medium_relation_view_v0_min(request)
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assert_public_block_codes(result)
                self.assert_non_claims_canonical_false(result)

            with self.subTest(name="artifact JSON array"):
                array_path = tmp_path / "array.json"
                _write_json(array_path, [])
                request = _clean_request(array_path)
                result = resolver.resolve_local_relevance_medium_relation_view_v0_min(request)
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assert_public_block_codes(result)
                self.assert_non_claims_canonical_false(result)

            with self.subTest(name="required non-claim flipped"):
                artifact_path, _artifact = _write_synthetic_multiplicity_result_artifact(tmp_path)
                request = _clean_request(artifact_path)
                request["declared_non_claims"]["comparison_view_created"] = True
                result = resolver.resolve_local_relevance_medium_relation_view_v0_min(request)
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assert_public_block_codes(result)
                self.assert_non_claims_canonical_false(result)

    def test_missing_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact = _write_synthetic_multiplicity_result_artifact(Path(tmp))
            variants = []
            request = _clean_request(artifact_path)
            request.pop("declared_non_claims")
            variants.append(request)
            request = _clean_request(artifact_path)
            request["declared_non_claims"] = {}
            variants.append(request)
            request = _clean_request(artifact_path)
            request["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])
            variants.append(request)
            request = _clean_request(artifact_path)
            request["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = "false"
            variants.append(request)
            request = _clean_request(artifact_path)
            request["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = None
            variants.append(request)

            for request in variants:
                with self.subTest(request=request):
                    result = resolver.resolve_local_relevance_medium_relation_view_v0_min(request)
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS},
                    )
                    self.assert_public_block_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result, _path, _artifact, _request = _resolve_with_artifact(Path(tmp))
        relation_view = _relation_view(result)
        self.assertEqual(
            relation_view["relation_view_type"], "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW"
        )
        self.assertEqual(
            relation_view["relation_view_scope"],
            "TWO_LOCAL_ORIENTATION_OBJECTS_RELATION_VIEW_ONLY",
        )
        self.assertEqual(
            relation_view["relation_frame"],
            "BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY",
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_RECORDED", resolver.OUTCOME_FAMILY)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_NOT_RECORDED", resolver.OUTCOME_FAMILY)
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_REQUIRES_ADDITIONAL_BASIS",
            resolver.OUTCOME_FAMILY,
        )
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_BLOCKED", resolver.OUTCOME_FAMILY)
        self.assertNotEqual(relation_view["relation_view_type"], "[REDACTED_RAW_CONTENT]")
        self.assertNotEqual(relation_view["relation_view_scope"], "[REDACTED_RAW_CONTENT]")
        self.assertNotEqual(relation_view["relation_frame"], "[REDACTED_RAW_CONTENT]")

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact = _clean_multiplicity_result_artifact()
            artifact["raw_multiplicity_result_body"] = HOSTILE_SENTINELS[2]
            artifact["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            artifact["local_relevance_medium_multiplicity_result"][
                "raw_first_local_index_entry_body"
            ] = HOSTILE_SENTINELS[3]
            artifact_path, _artifact_body = _write_synthetic_multiplicity_result_artifact(
                tmp_path, artifact
            )
            request = _clean_request(artifact_path)
            request["raw_relation_view_body"] = HOSTILE_SENTINELS[1]
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            request_before = copy.deepcopy(request)
            result = resolver.resolve_local_relevance_medium_relation_view_v0_min(request)

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW", serialized)
        self.assertIn("TWO_LOCAL_ORIENTATION_OBJECTS_RELATION_VIEW_ONLY", serialized)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_overreach_created(result)
        self.assertEqual(request, request_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact_path, _artifact = _write_synthetic_multiplicity_result_artifact(tmp_path)
            request = _clean_request(artifact_path)
            request_path = tmp_path / "request.json"
            _write_json(request_path, request)
            result = resolver.resolve_local_relevance_medium_relation_view_v0_min_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(_summary(result)["result_version"], "0.1.0")
            self.assertEqual(
                _summary(result)["resolver_module"],
                "resolve_local_relevance_medium_relation_view_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_relation_view_v0_min_from_path(
                malformed_path
            )
            self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(malformed_result)

            array_path = tmp_path / "array_request.json"
            _write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_relation_view_v0_min_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(array_result)

            missing_result = resolver.resolve_local_relevance_medium_relation_view_v0_min_from_path(
                tmp_path / "missing_request.json"
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(missing_result)

            output_root = tmp_path / "local_relevance_medium_relation_view_v0_min"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                written = resolver.write_local_relevance_medium_relation_view_v0_min_result(
                    result
                )
                written_again = resolver.write_local_relevance_medium_relation_view_v0_min_result(
                    result
                )

            self.assertTrue(written.parent.exists())
            self.assertNotEqual(written, written_again)
            self.assertTrue(written_again.name.endswith("_001.json"))
            json.loads(written.read_text(encoding="utf-8"))
            json.loads(written_again.read_text(encoding="utf-8"))
            self.assertIn("local_relevance_medium_relation_view_v0_min", str(written))
            self.assert_output_not_under_prior_roots(written)
            self.assert_output_not_under_prior_roots(written_again)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact_path, artifact = _write_synthetic_multiplicity_result_artifact(tmp_path)
            artifact_before = copy.deepcopy(artifact)
            request = _clean_request(artifact_path)
            request["raw_relation_view_body"] = {
                "sentinel": "RAW_RELATION_VIEW_BODY_MUST_NOT_RETURN"
            }
            request_before = copy.deepcopy(request)
            declared_non_claims_before = copy.deepcopy(request["declared_non_claims"])

            result = resolver.resolve_local_relevance_medium_relation_view_v0_min(request)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, request_before)
        self.assertEqual(request["declared_non_claims"], declared_non_claims_before)
        self.assertEqual(artifact, artifact_before)
        self.assertEqual(
            request["selected_local_relevance_medium_multiplicity_result_artifact"],
            str(artifact_path),
        )
        self.assertEqual(
            request["relation_view_scope"],
            "TWO_LOCAL_ORIENTATION_OBJECTS_RELATION_VIEW_ONLY",
        )
        self.assertEqual(
            request["relation_view_type"], "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW"
        )
        self.assertEqual(
            request["relation_frame"], "BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY"
        )

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result, _path, _artifact, _request = _resolve_with_artifact(Path(tmp))

        summary = _summary(result)
        non_claims = _non_claims(result)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(non_claims["predecessor_failure_repaired"], False)
        self.assertIs(non_claims["predecessor_failure_hidden"], False)
        self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)


if __name__ == "__main__":
    unittest.main()
