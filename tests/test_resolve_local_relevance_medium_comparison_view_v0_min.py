"""Bounded tests for the local relevance medium comparison view resolver.

The suite exercises one comparison-view object only. It verifies that the
resolver reads one clean relation-view artifact, preserves the upstream
lineage, records bounded comparison-readability, and keeps every broader
ranking, authority, runtime, interface, and follow-on posture false.
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

import resolve_local_relevance_medium_comparison_view_v0_min as resolver  # noqa: E402


DEFAULT_RELATION_VIEW_ARTIFACT = REPO_ROOT / (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_relation_view_v0_min/"
    "local_relevance_medium_relation_view_reference_review_001__"
    "local_relevance_medium_relation_view_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_comparison_view_v0_min"
)

FORBIDDEN_OUTPUT_ROOTS = (
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

BASIS_MULTIPLICITY_RESULT_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_multiplicity_result_v0_min/"
    "local_relevance_medium_multiplicity_result_reference_review_001__"
    "local_relevance_medium_multiplicity_result_v0_min_result.json"
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
    "relevance_orientation_view_reference_review_001__relevance_orientation_view_v0_min_result.json"
)
SECOND_ORIENTATION_VIEW_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min/"
    "local_relevance_medium_second_relevance_orientation_view_reference_review_001__"
    "local_relevance_medium_second_relevance_orientation_view_v0_min_result.json"
)
FIRST_RECEIPT_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2/"
    "bounded_relevance_receipt_reference_review_001__bounded_relevance_receipt_v0_min_v2_result.json"
)
SECOND_RECEIPT_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_receipt_v0_min/"
    "local_relevance_medium_second_bounded_relevance_receipt_reference_review_001__"
    "local_relevance_medium_second_bounded_relevance_receipt_v0_min_result.json"
)
FIRST_RECEPTION_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min/"
    "bounded_relevance_reception_reference_review_001__bounded_relevance_reception_v0_min_result.json"
)
SECOND_RECEPTION_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_reception_v0_min/"
    "local_relevance_medium_second_bounded_relevance_reception_reference_review_001__"
    "local_relevance_medium_second_bounded_relevance_reception_v0_min_result.json"
)
SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_successor_candidate_admission_v0_min/"
    "local_relevance_medium_successor_candidate_admission_reference_review_001__"
    "local_relevance_medium_successor_candidate_admission_v0_min_result.json"
)
SUCCESSOR_RECEPTION_REQUEST_ARTIFACT = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_successor_reception_request_v0_min/"
    "local_relevance_medium_successor_reception_request_reference_review_001__"
    "local_relevance_medium_successor_reception_request_v0_min_result.json"
)

EXPECTED_TOP_LEVEL_SECTIONS = {
    "local_relevance_medium_comparison_view_metadata",
    "declared_local_relevance_medium_comparison_view_question",
    "selected_local_relevance_medium_relation_view_artifact_basis",
    "local_relevance_medium_comparison_view",
    "local_relevance_medium_comparison_view_checks",
    "local_relevance_medium_comparison_view_statement",
    "local_relevance_medium_comparison_view_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_comparison_view_summary",
}

WRAPPER_FIELDS_FORBIDDEN_IN_COMPARISON_VIEW = {
    "outcome",
    "block",
    "local_relevance_medium_comparison_view_checks",
    "non_claims",
    "local_relevance_medium_comparison_view_summary",
    "local_relevance_medium_comparison_view_metadata",
}

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_BODY_MUST_NOT_RETURN",
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

NO_OVERREACH_NON_CLAIMS = (
    "ranking_surface_created",
    "scoring_surface_created",
    "priority_surface_created",
    "validity_judgment_created",
    "truth_judgment_created",
    "authority_judgment_created",
    "currentness_judgment_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_created",
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
    "broader_reusable_permission_created",
    "follow_on_work_authorized",
)


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _comparison_view(result: Mapping[str, Any]) -> Mapping[str, Any]:
    comparison_view = result.get("local_relevance_medium_comparison_view")
    if not isinstance(comparison_view, Mapping):
        raise AssertionError("local_relevance_medium_comparison_view is not a mapping")
    return comparison_view


def _statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    statement = result.get("local_relevance_medium_comparison_view_statement")
    if not isinstance(statement, Mapping):
        raise AssertionError("local_relevance_medium_comparison_view_statement is not a mapping")
    return statement


def _summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = result.get("local_relevance_medium_comparison_view_summary")
    if not isinstance(summary, Mapping):
        raise AssertionError("local_relevance_medium_comparison_view_summary is not a mapping")
    return summary


def _checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    checks = result.get("local_relevance_medium_comparison_view_checks")
    if not isinstance(checks, list):
        raise AssertionError("local_relevance_medium_comparison_view_checks is not a list")
    return checks


def _block_code(result: Mapping[str, Any]) -> str | None:
    block = result.get("block")
    if not isinstance(block, Mapping):
        return None
    code = block.get("code") or block.get("block_code")
    return code if isinstance(code, str) else None


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")


def _clean_relation_view_object() -> dict[str, Any]:
    return {
        "relation_view_id": "local_relevance_medium_relation_view_001",
        "relation_view_type": "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW",
        "relation_view_version": "0.1.0",
        "relation_view_scope": "TWO_LOCAL_ORIENTATION_OBJECTS_RELATION_VIEW_ONLY",
        "relation_frame": "BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY",
        "basis_local_relevance_medium_multiplicity_result_artifact": BASIS_MULTIPLICITY_RESULT_ARTIFACT,
        "basis_local_relevance_medium_multiplicity_result_outcome": (
            "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_RECORDED"
        ),
        "basis_local_relevance_medium_multiplicity_result_result_version": "0.1.0",
        "basis_local_relevance_medium_multiplicity_result_failed_check_count": 0,
        "basis_first_local_relevance_orientation_index_entry_artifact": FIRST_LOCATOR_ARTIFACT,
        "basis_second_local_relevance_orientation_index_entry_artifact": SECOND_LOCATOR_ARTIFACT,
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
        "relation_pair_count": 1,
        "two_local_orientation_objects_preserved": True,
        "first_and_second_signals_distinct": True,
        "relation_readable_co_presence_recorded": True,
        "relation_view_recorded": True,
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


def _clean_relation_view_artifact() -> dict[str, Any]:
    return {
        "local_relevance_medium_relation_view_metadata": {
            "local_relevance_medium_relation_view_id": "local_relevance_medium_relation_view_001",
            "local_relevance_medium_relation_view_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_relation_view_v0_min",
        },
        "local_relevance_medium_relation_view_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_RECORDED",
            "failed_check_count": 0,
            "passed_check_count": 87,
            "result_version": "0.1.0",
            "resolver_module": "resolve_local_relevance_medium_relation_view_v0_min",
            "local_relevance_medium_relation_view_recorded": True,
        },
        "local_relevance_medium_relation_view_checks": [
            {
                "check_name": "synthetic_relation_view_artifact_clean",
                "passed": True,
                "expected_posture": "clean local relevance medium relation view artifact",
                "actual_posture": "clean local relevance medium relation view artifact",
            }
        ],
        "local_relevance_medium_relation_view": _clean_relation_view_object(),
        "outcome": "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_RECORDED",
        "failed_check_count": 0,
        "result_version": "0.1.0",
    }


def _write_synthetic_relation_view_artifact(
    directory: Path,
    artifact: Mapping[str, Any] | None = None,
) -> tuple[Path, dict[str, Any]]:
    artifact_body = copy.deepcopy(dict(artifact or _clean_relation_view_artifact()))
    artifact_path = directory / "synthetic_relation_view_artifact.json"
    _write_json(artifact_path, artifact_body)
    return artifact_path, artifact_body


def _clean_request(artifact_path: Path | str) -> dict[str, Any]:
    return resolver.build_declared_local_relevance_medium_comparison_view_v0_min_request(
        selected_local_relevance_medium_relation_view_artifact=str(artifact_path)
    )


def _mutate_relation_view(
    artifact: dict[str, Any],
    key: str,
    value: Any,
) -> None:
    relation_view = artifact["local_relevance_medium_relation_view"]
    relation_view[key] = value


class LocalRelevanceMediumComparisonViewResolverTests(unittest.TestCase):
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
        if output_path.is_absolute():
            candidate = output_path.resolve()
            forbidden_roots = [(REPO_ROOT / root).resolve() for root in FORBIDDEN_OUTPUT_ROOTS]
        else:
            candidate = output_path
            forbidden_roots = list(FORBIDDEN_OUTPUT_ROOTS)
        for root in forbidden_roots:
            self.assertFalse(candidate == root or _is_relative_to(candidate, root), root)

    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block_code = _block_code(result)
        if block_code is not None:
            self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in _checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIs(type(non_claims[key]), bool)

    def assert_no_overreach_created(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in NO_OVERREACH_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)

    def assert_comparison_view_not_wrapper(self, comparison_view: Mapping[str, Any]) -> None:
        for key in WRAPPER_FIELDS_FORBIDDEN_IN_COMPARISON_VIEW:
            self.assertNotIn(key, comparison_view)

    def assert_recorded_statement_shape(self, result: Mapping[str, Any]) -> None:
        statement = _statement(result)
        true_fields = (
            "local_relevance_medium_comparison_view_recorded",
            "basis_local_relevance_medium_relation_view_artifact_preserved",
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
            "comparison_view_scope_local_only",
            "comparison_frame_bounded_non_ranking_only",
            "comparison_pair_count_is_one",
            "relation_readable_co_presence_preserved",
            "comparison_readable_distinctions_recorded",
            "result_level_non_claims_canonical_false",
        )
        for key in true_fields:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
            self.assertIs(type(statement[key]), bool, key)

    def assert_recorded_comparison_view_shape(
        self,
        result: Mapping[str, Any],
        relation_artifact_path: Path | str,
    ) -> None:
        comparison_view = _comparison_view(result)
        self.assertEqual(comparison_view["comparison_view_id"], "local_relevance_medium_comparison_view_001")
        self.assertEqual(comparison_view["comparison_view_type"], "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW")
        self.assertEqual(comparison_view["comparison_view_version"], "0.1.0")
        self.assertEqual(
            comparison_view["comparison_view_scope"],
            "TWO_LOCAL_ORIENTATION_OBJECTS_COMPARISON_VIEW_ONLY",
        )
        self.assertEqual(comparison_view["comparison_frame"], "BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY")
        self.assertEqual(
            comparison_view["basis_local_relevance_medium_relation_view_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_RECORDED",
        )
        self.assertEqual(comparison_view["basis_local_relevance_medium_relation_view_result_version"], "0.1.0")
        self.assertEqual(comparison_view["basis_local_relevance_medium_relation_view_failed_check_count"], 0)
        self.assertEqual(
            comparison_view["basis_local_relevance_medium_relation_view_artifact"],
            str(relation_artifact_path),
        )
        self.assertEqual(
            comparison_view["basis_local_relevance_medium_multiplicity_result_artifact"],
            BASIS_MULTIPLICITY_RESULT_ARTIFACT,
        )
        self.assertEqual(
            comparison_view["basis_first_local_relevance_orientation_index_entry_artifact"],
            FIRST_LOCATOR_ARTIFACT,
        )
        self.assertEqual(
            comparison_view["basis_second_local_relevance_orientation_index_entry_artifact"],
            SECOND_LOCATOR_ARTIFACT,
        )
        self.assertEqual(comparison_view["first_orientation_view_artifact"], FIRST_ORIENTATION_VIEW_ARTIFACT)
        self.assertEqual(comparison_view["second_orientation_view_artifact"], SECOND_ORIENTATION_VIEW_ARTIFACT)
        self.assertEqual(comparison_view["first_receipt_artifact"], FIRST_RECEIPT_ARTIFACT)
        self.assertEqual(comparison_view["second_receipt_artifact"], SECOND_RECEIPT_ARTIFACT)
        self.assertEqual(comparison_view["first_reception_artifact"], FIRST_RECEPTION_ARTIFACT)
        self.assertEqual(comparison_view["second_reception_artifact"], SECOND_RECEPTION_ARTIFACT)
        self.assertEqual(
            comparison_view["successor_candidate_admission_artifact"],
            SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT,
        )
        self.assertEqual(
            comparison_view["successor_reception_request_artifact"],
            SUCCESSOR_RECEPTION_REQUEST_ARTIFACT,
        )
        self.assertEqual(comparison_view["first_received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(comparison_view["second_received_signal_id"], "bounded_relevance_signal_002")
        self.assertNotEqual(
            comparison_view["first_received_signal_id"],
            comparison_view["second_received_signal_id"],
        )
        self.assertEqual(comparison_view["first_relevance_basis_id"], "bounded_relevance_basis_001")
        self.assertEqual(comparison_view["second_relevance_basis_id"], "bounded_relevance_basis_002")
        self.assertEqual(comparison_view["first_relevance_scope_id"], "bounded_relevance_scope_001")
        self.assertEqual(comparison_view["second_relevance_scope_id"], "bounded_relevance_scope_002")
        self.assertEqual(
            comparison_view["first_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_001",
        )
        self.assertEqual(
            comparison_view["second_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_002",
        )
        self.assertEqual(
            comparison_view["first_reception_envelope_id"],
            "bounded_relevance_reception_envelope_001",
        )
        self.assertEqual(
            comparison_view["second_reception_envelope_id"],
            "bounded_relevance_reception_envelope_002",
        )
        self.assertEqual(comparison_view["multiplicity_count"], 2)
        self.assertEqual(comparison_view["relation_pair_count"], 1)
        self.assertEqual(comparison_view["comparison_pair_count"], 1)
        for key in (
            "first_and_second_signals_distinct",
            "two_local_orientation_objects_preserved",
            "relation_readable_co_presence_preserved",
            "comparison_readable_distinctions_recorded",
            "comparison_view_recorded",
        ):
            self.assertIs(comparison_view[key], True, key)
        for key in (
            "ranking_surface_created",
            "scoring_surface_created",
            "priority_surface_created",
            "validity_judgment_created",
            "truth_judgment_created",
            "authority_judgment_created",
            "currentness_judgment_created",
            "index_system_created",
            "registry_created",
            "search_surface_created",
            "ranking_created",
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
            self.assertIn(key, comparison_view)
            self.assertIs(comparison_view[key], False, key)
        self.assert_comparison_view_not_wrapper(comparison_view)

    def resolve_from_synthetic_artifact(
        self,
        directory: Path,
        artifact: Mapping[str, Any] | None = None,
        request_updates: Mapping[str, Any] | None = None,
    ) -> tuple[dict[str, Any], Path, dict[str, Any], dict[str, Any]]:
        artifact_path, artifact_body = _write_synthetic_relation_view_artifact(directory, artifact)
        request = _clean_request(artifact_path)
        if request_updates:
            request.update(copy.deepcopy(dict(request_updates)))
        request_before = copy.deepcopy(request)
        result = resolver.resolve_local_relevance_medium_comparison_view_v0_min(request)
        return result, artifact_path, artifact_body, request_before

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_local_relevance_medium_comparison_view_v0_min",
            "resolve_local_relevance_medium_comparison_view_v0_min_from_path",
            "write_local_relevance_medium_comparison_view_v0_min_result",
            "build_local_relevance_medium_comparison_view_v0_min_summary",
            "build_declared_local_relevance_medium_comparison_view_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_COMPARISON_VIEW_SCOPE_VALUES",
            "SUPPORTED_COMPARISON_VIEW_TYPE_VALUES",
            "SUPPORTED_COMPARISON_FRAME_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_local_relevance_medium_comparison_view_v0_min")
        self.assertEqual(Path(resolver.OUTPUT_ROOT), EXPECTED_OUTPUT_ROOT)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW", resolver.SUPPORTED_COMPARISON_VIEW_TYPE_VALUES)
        self.assertIn(
            "TWO_LOCAL_ORIENTATION_OBJECTS_COMPARISON_VIEW_ONLY",
            resolver.SUPPORTED_COMPARISON_VIEW_SCOPE_VALUES,
        )
        self.assertIn(
            "BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY",
            resolver.SUPPORTED_COMPARISON_FRAME_VALUES,
        )
        self.assert_output_not_under_prior_roots(Path(resolver.OUTPUT_ROOT))

    def test_successful_recorded_result_from_synthetic_relation_view_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result, artifact_path, _artifact_body, _request_before = self.resolve_from_synthetic_artifact(Path(tmp))

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        summary = _summary(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], "resolve_local_relevance_medium_comparison_view_v0_min")
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(_comparison_view(result)["comparison_view_id"], "local_relevance_medium_comparison_view_001")
        self.assertTrue(EXPECTED_TOP_LEVEL_SECTIONS.issubset(result.keys()))
        self.assert_recorded_comparison_view_shape(result, artifact_path)
        self.assert_recorded_statement_shape(result)
        self.assert_non_claims_canonical_false(result)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_RELATION_VIEW_ARTIFACT.exists():
            self.skipTest("default local relevance medium relation view artifact is not present")

        request = resolver.build_declared_local_relevance_medium_comparison_view_v0_min_request()
        result = resolver.resolve_local_relevance_medium_comparison_view_v0_min(request)
        comparison_view = _comparison_view(result)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(_summary(result)["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(comparison_view["comparison_view_type"], "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW")
        self.assertEqual(
            comparison_view["comparison_view_scope"],
            "TWO_LOCAL_ORIENTATION_OBJECTS_COMPARISON_VIEW_ONLY",
        )
        self.assertEqual(comparison_view["comparison_frame"], "BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY")
        self.assertEqual(comparison_view["first_received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(comparison_view["second_received_signal_id"], "bounded_relevance_signal_002")
        self.assertNotEqual(comparison_view["first_received_signal_id"], comparison_view["second_received_signal_id"])
        self.assertEqual(comparison_view["multiplicity_count"], 2)
        self.assertEqual(comparison_view["relation_pair_count"], 1)
        self.assertEqual(comparison_view["comparison_pair_count"], 1)
        self.assertIs(comparison_view["relation_readable_co_presence_preserved"], True)
        self.assertIs(comparison_view["comparison_readable_distinctions_recorded"], True)
        for key in (
            "ranking_surface_created",
            "scoring_surface_created",
            "priority_surface_created",
            "validity_judgment_created",
            "truth_judgment_created",
            "authority_judgment_created",
            "currentness_judgment_created",
            "index_system_created",
            "registry_created",
            "search_surface_created",
            "ranking_created",
            "repeated_reception_permission_created",
            "arbitrary_reception_created",
            "feed_created",
            "authority_created",
            "currentness_created",
            "action_created",
            "synchronization_created",
            "participation_authorized",
            "runtime_permission_created",
            "public_api_created",
            "distributed_network_behavior_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(comparison_view[key], False, key)

    def test_declared_non_claim_flips_block_and_are_canonicalized(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact_body = _write_synthetic_relation_view_artifact(Path(tmp))
            clean_request = _clean_request(artifact_path)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_comparison_view_v0_min(request)
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assertIsNotNone(_block_code(result))
                    self.assertIn(_block_code(result), resolver.BLOCK_CODES)
                    self.assertGreater(_summary(result)["failed_check_count"], 0)
                    self.assert_public_block_codes(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_non_claims_canonical_false(result)
                    self.assert_no_overreach_created(result)

    def _artifact_mutation_case(
        self,
        directory: Path,
        mutate: Callable[[dict[str, Any]], None],
        request_updates: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        artifact = _clean_relation_view_artifact()
        mutate(artifact)
        result, _artifact_path, _artifact_body, _request_before = self.resolve_from_synthetic_artifact(
            directory,
            artifact,
            request_updates,
        )
        return result

    def _request_update_case(
        self,
        directory: Path,
        request_updates: Mapping[str, Any],
    ) -> dict[str, Any]:
        result, _artifact_path, _artifact_body, _request_before = self.resolve_from_synthetic_artifact(
            directory,
            request_updates=request_updates,
        )
        return result

    def test_representative_blocking_behavior(self) -> None:
        false_posture_flags = (
            "ranking_surface_created",
            "scoring_surface_created",
            "priority_surface_created",
            "validity_judgment_created",
            "truth_judgment_created",
            "authority_judgment_created",
            "currentness_judgment_created",
            "index_system_created",
            "registry_created",
            "search_surface_created",
            "ranking_created",
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
            "artifact_existence_treated_as_comparison_view_authority",
            "latest_file_posture_treated_as_comparison_view_authority",
            "repo_local_availability_treated_as_comparison_view_authority",
            "hidden_repo_state_used_as_comparison_view_content",
            "hidden_repo_state_used_as_comparison_view_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        )
        artifact_field_missing = {
            "basis local relevance medium multiplicity result artifact missing": (
                "basis_local_relevance_medium_multiplicity_result_artifact"
            ),
            "first locator artifact missing": "basis_first_local_relevance_orientation_index_entry_artifact",
            "second locator artifact missing": "basis_second_local_relevance_orientation_index_entry_artifact",
            "first orientation view artifact missing": "first_orientation_view_artifact",
            "second orientation view artifact missing": "second_orientation_view_artifact",
            "first receipt artifact missing": "first_receipt_artifact",
            "second receipt artifact missing": "second_receipt_artifact",
            "first reception artifact missing": "first_reception_artifact",
            "second reception artifact missing": "second_reception_artifact",
            "first received signal id missing": "first_received_signal_id",
            "second received signal id missing": "second_received_signal_id",
            "first relevance basis id missing": "first_relevance_basis_id",
            "second relevance basis id missing": "second_relevance_basis_id",
            "first relevance scope id missing": "first_relevance_scope_id",
            "second relevance scope id missing": "second_relevance_scope_id",
            "first carrier context id missing": "first_carrier_context_id",
            "second carrier context id missing": "second_carrier_context_id",
            "first reception envelope id missing": "first_reception_envelope_id",
            "second reception envelope id missing": "second_reception_envelope_id",
        }

        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            array_artifact_path = directory / "array_relation_view_artifact.json"
            _write_json(array_artifact_path, [{"not": "object"}])

            cases: list[tuple[str, Callable[[], dict[str, Any]]]] = [
                (
                    "explicit block intent",
                    lambda: self._request_update_case(
                        directory,
                        {"local_relevance_medium_comparison_view_intent": "BLOCK_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW"},
                    ),
                ),
                ("missing request", lambda: resolver.resolve_local_relevance_medium_comparison_view_v0_min()),
                ("non-mapping request", lambda: resolver.resolve_local_relevance_medium_comparison_view_v0_min([])),
                (
                    "unsupported intent",
                    lambda: self._request_update_case(
                        directory,
                        {"local_relevance_medium_comparison_view_intent": "RANK_THE_LOCAL_ORIENTATION_OBJECTS"},
                    ),
                ),
                (
                    "selected relation view artifact path missing",
                    lambda: self._request_update_case(
                        directory,
                        {"selected_local_relevance_medium_relation_view_artifact": ""},
                    ),
                ),
                (
                    "selected relation view artifact unreadable",
                    lambda: self._request_update_case(
                        directory,
                        {"selected_local_relevance_medium_relation_view_artifact": str(directory / "missing.json")},
                    ),
                ),
                (
                    "selected relation view artifact JSON array",
                    lambda: self._request_update_case(
                        directory,
                        {"selected_local_relevance_medium_relation_view_artifact": str(array_artifact_path)},
                    ),
                ),
                (
                    "relation view artifact not recorded",
                    lambda: self._artifact_mutation_case(
                        directory,
                        lambda artifact: (
                            artifact.update({"outcome": "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_NOT_RECORDED"}),
                            artifact["local_relevance_medium_relation_view_summary"].update(
                                {"outcome": "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_NOT_RECORDED"}
                            ),
                        ),
                    ),
                ),
                (
                    "relation view artifact failed checks present",
                    lambda: self._artifact_mutation_case(
                        directory,
                        lambda artifact: (
                            artifact.update({"failed_check_count": 1}),
                            artifact["local_relevance_medium_relation_view_summary"].update(
                                {"failed_check_count": 1}
                            ),
                        ),
                    ),
                ),
                (
                    "relation view artifact version not 0.1.0",
                    lambda: self._artifact_mutation_case(
                        directory,
                        lambda artifact: (
                            artifact.update({"result_version": "9.9.9"}),
                            artifact["local_relevance_medium_relation_view_summary"].update(
                                {"result_version": "9.9.9"}
                            ),
                        ),
                    ),
                ),
                (
                    "relation view object missing",
                    lambda: self._artifact_mutation_case(
                        directory,
                        lambda artifact: artifact.pop("local_relevance_medium_relation_view", None),
                    ),
                ),
                (
                    "relation view type invalid",
                    lambda: self._artifact_mutation_case(
                        directory,
                        lambda artifact: _mutate_relation_view(artifact, "relation_view_type", "LOCAL_RELEVANCE_INDEX"),
                    ),
                ),
                (
                    "relation view scope invalid",
                    lambda: self._artifact_mutation_case(
                        directory,
                        lambda artifact: _mutate_relation_view(artifact, "relation_view_scope", "GENERAL_RELATION_VIEW"),
                    ),
                ),
                (
                    "relation frame invalid",
                    lambda: self._artifact_mutation_case(
                        directory,
                        lambda artifact: _mutate_relation_view(artifact, "relation_frame", "UNBOUNDED_RELATION_FRAME"),
                    ),
                ),
                (
                    "multiplicity count not two",
                    lambda: self._artifact_mutation_case(
                        directory,
                        lambda artifact: _mutate_relation_view(artifact, "multiplicity_count", 3),
                    ),
                ),
                (
                    "relation pair count not one",
                    lambda: self._artifact_mutation_case(
                        directory,
                        lambda artifact: _mutate_relation_view(artifact, "relation_pair_count", 2),
                    ),
                ),
                (
                    "relation view artifact missing shortcut",
                    lambda: self._request_update_case(directory, {"relation_view_artifact_missing": True}),
                ),
                (
                    "first and second received signal ids not distinct",
                    lambda: self._artifact_mutation_case(
                        directory,
                        lambda artifact: (
                            _mutate_relation_view(
                                artifact,
                                "second_received_signal_id",
                                "bounded_relevance_signal_001",
                            ),
                            _mutate_relation_view(artifact, "first_and_second_signals_distinct", False),
                        ),
                    ),
                ),
                (
                    "comparison view type missing",
                    lambda: self._request_update_case(directory, {"comparison_view_type": ""}),
                ),
                (
                    "comparison view type invalid",
                    lambda: self._request_update_case(
                        directory,
                        {"comparison_view_type": "LOCAL_RELEVANCE_INDEX"},
                    ),
                ),
                (
                    "comparison view scope missing",
                    lambda: self._request_update_case(directory, {"comparison_view_scope": ""}),
                ),
                (
                    "comparison view scope invalid",
                    lambda: self._request_update_case(
                        directory,
                        {"comparison_view_scope": "SEARCH_VIEW_SCOPE"},
                    ),
                ),
                (
                    "comparison frame missing",
                    lambda: self._request_update_case(directory, {"comparison_frame": ""}),
                ),
                (
                    "comparison frame invalid",
                    lambda: self._request_update_case(
                        directory,
                        {"comparison_frame": "RANKING_COMPARISON_FRAME"},
                    ),
                ),
                (
                    "comparison pair count not one",
                    lambda: self._request_update_case(directory, {"comparison_pair_count": 2}),
                ),
                (
                    "relation-readable co-presence not preserved",
                    lambda: self._artifact_mutation_case(
                        directory,
                        lambda artifact: _mutate_relation_view(
                            artifact,
                            "relation_readable_co_presence_recorded",
                            False,
                        ),
                    ),
                ),
                (
                    "comparison-readable distinctions not recorded",
                    lambda: self._request_update_case(
                        directory,
                        {"comparison_readable_distinctions_recorded": False},
                    ),
                ),
                (
                    "comparison view not recorded",
                    lambda: self._request_update_case(directory, {"comparison_view_recorded": False}),
                ),
            ]

            for label, field in artifact_field_missing.items():
                cases.append(
                    (
                        label,
                        lambda field=field: self._artifact_mutation_case(
                            directory,
                            lambda artifact, field=field: _mutate_relation_view(artifact, field, ""),
                        ),
                    )
                )
            for flag in false_posture_flags:
                cases.append(
                    (
                        flag,
                        lambda flag=flag: self._request_update_case(directory, {flag: True}),
                    )
                )
            cases.append(
                (
                    "required non-claim missing or flipped",
                    lambda: self._request_update_case(
                        directory,
                        {
                            "declared_non_claims": {
                                key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]
                            }
                        },
                    ),
                )
            )

            for label, make_result in cases:
                with self.subTest(label=label):
                    result = make_result()
                    self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                    self.assertIsNotNone(_block_code(result), label)
                    self.assertIn(_block_code(result), resolver.BLOCK_CODES)
                    self.assert_public_block_codes(result)
                    self.assert_no_overreach_created(result)
                    self.assert_non_claims_canonical_false(result)

    def test_missing_or_incomplete_declared_non_claims_still_emit_false_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact_path, _artifact_body = _write_synthetic_relation_view_artifact(Path(tmp))
            clean_request = _clean_request(artifact_path)
            first_key = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            variants = []

            missing_mapping = copy.deepcopy(clean_request)
            missing_mapping.pop("declared_non_claims", None)
            variants.append(("missing declared_non_claims", missing_mapping))

            empty_mapping = copy.deepcopy(clean_request)
            empty_mapping["declared_non_claims"] = {}
            variants.append(("empty declared_non_claims", empty_mapping))

            missing_one = copy.deepcopy(clean_request)
            missing_one["declared_non_claims"].pop(first_key, None)
            variants.append(("one non-claim removed", missing_one))

            string_value = copy.deepcopy(clean_request)
            string_value["declared_non_claims"][first_key] = "false"
            variants.append(("one non-claim string", string_value))

            none_value = copy.deepcopy(clean_request)
            none_value["declared_non_claims"][first_key] = None
            variants.append(("one non-claim None", none_value))

            for label, request in variants:
                with self.subTest(label=label):
                    result = resolver.resolve_local_relevance_medium_comparison_view_v0_min(request)
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS},
                    )
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assertIsNotNone(_block_code(result))
                        self.assertIn(_block_code(result), resolver.BLOCK_CODES)
                    self.assert_public_block_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result, _artifact_path, _artifact_body, _request_before = self.resolve_from_synthetic_artifact(Path(tmp))
        comparison_view = _comparison_view(result)
        self.assertEqual(comparison_view["comparison_view_type"], "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW")
        self.assertEqual(
            comparison_view["comparison_view_scope"],
            "TWO_LOCAL_ORIENTATION_OBJECTS_COMPARISON_VIEW_ONLY",
        )
        self.assertEqual(comparison_view["comparison_frame"], "BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        for outcome in (
            "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_NOT_RECORDED",
            "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_REQUIRES_ADDITIONAL_BASIS",
            "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW", serialized)
        self.assertIn("TWO_LOCAL_ORIENTATION_OBJECTS_COMPARISON_VIEW_ONLY", serialized)
        self.assertIn("BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY", serialized)
        self.assertNotIn("[REDACTED_RAW_CONTENT]", serialized)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            artifact = _clean_relation_view_artifact()
            artifact["raw_relation_view_body"] = HOSTILE_SENTINELS[2]
            artifact["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            artifact["local_relevance_medium_relation_view"]["raw_full_body"] = HOSTILE_SENTINELS[-2]
            artifact_path, _artifact_body = _write_synthetic_relation_view_artifact(directory, artifact)
            request = _clean_request(artifact_path)
            request["raw_full_body"] = HOSTILE_SENTINELS[0]
            request["hidden_repo_state"] = {"payload": HOSTILE_SENTINELS[-1]}
            request["extra_context"] = {"raw_comparison_view_body": HOSTILE_SENTINELS[1]}
            request_before = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_medium_comparison_view_v0_min(request)

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW", serialized)
        self.assertIn("TWO_LOCAL_ORIENTATION_OBJECTS_COMPARISON_VIEW_ONLY", serialized)
        self.assertIn("BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY", serialized)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_overreach_created(result)
        self.assertEqual(request, request_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            artifact_path, _artifact_body = _write_synthetic_relation_view_artifact(directory)
            request = _clean_request(artifact_path)
            request_path = directory / "declared_comparison_view_request.json"
            _write_json(request_path, request)

            result = resolver.resolve_local_relevance_medium_comparison_view_v0_min_from_path(request_path)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(_summary(result)["result_version"], "0.1.0")
            self.assertEqual(_summary(result)["resolver_module"], "resolve_local_relevance_medium_comparison_view_v0_min")
            self.assert_not_blocked(result)

            malformed_path = directory / "malformed_request.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            malformed_result = resolver.resolve_local_relevance_medium_comparison_view_v0_min_from_path(
                malformed_path
            )
            self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(malformed_result)

            array_path = directory / "array_request.json"
            _write_json(array_path, [])
            array_result = resolver.resolve_local_relevance_medium_comparison_view_v0_min_from_path(array_path)
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(array_result)

            missing_result = resolver.resolve_local_relevance_medium_comparison_view_v0_min_from_path(
                directory / "missing_request.json"
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(missing_result)

            output_root = directory / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_output = resolver.write_local_relevance_medium_comparison_view_v0_min_result(result)
                second_output = resolver.write_local_relevance_medium_comparison_view_v0_min_result(result)

            self.assertTrue(first_output.exists())
            self.assertTrue(first_output.parent.exists())
            parsed = json.loads(first_output.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertTrue(second_output.exists())
            self.assertNotEqual(first_output, second_output)
            self.assertIn("local_relevance_medium_comparison_view_v0_min", str(first_output))
            self.assert_output_not_under_prior_roots(first_output)
            self.assert_output_not_under_prior_roots(second_output)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            artifact = _clean_relation_view_artifact()
            artifact["local_relevance_medium_relation_view"]["raw_full_body"] = HOSTILE_SENTINELS[-2]
            artifact_before = copy.deepcopy(artifact)
            artifact_path, artifact_body = _write_synthetic_relation_view_artifact(directory, artifact)
            request = _clean_request(artifact_path)
            request["posture_mappings"] = {"ranking_surface_created": False}
            request["nested_raw_payload"] = {"raw_body": HOSTILE_SENTINELS[0]}
            request_before = copy.deepcopy(request)
            non_claims_before = copy.deepcopy(request["declared_non_claims"])
            scope_before = request["comparison_view_scope"]
            type_before = request["comparison_view_type"]
            frame_before = request["comparison_frame"]

            resolver.resolve_local_relevance_medium_comparison_view_v0_min(request)

        self.assertEqual(request, request_before)
        self.assertEqual(request["declared_non_claims"], non_claims_before)
        self.assertEqual(artifact, artifact_before)
        self.assertEqual(artifact_body, artifact_before)
        self.assertEqual(request["comparison_view_scope"], scope_before)
        self.assertEqual(request["comparison_view_type"], type_before)
        self.assertEqual(request["comparison_frame"], frame_before)
        self.assertEqual(request["posture_mappings"], request_before["posture_mappings"])
        self.assertEqual(request["nested_raw_payload"], request_before["nested_raw_payload"])

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result, _artifact_path, _artifact_body, _request_before = self.resolve_from_synthetic_artifact(Path(tmp))
        summary = resolver.build_local_relevance_medium_comparison_view_v0_min_summary(result)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["result_level_non_claims_canonical_false"], True)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)
        self.assert_non_claims_canonical_false(result)


if __name__ == "__main__":
    unittest.main()
