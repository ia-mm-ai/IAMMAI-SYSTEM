"""Tests for the local relevance medium second relevance orientation view resolver.

This suite is bounded to one second orientation view object. It verifies that
the resolver reads one clean local relevance medium second bounded relevance
receipt artifact, preserves the basis second receipt, second reception,
candidate-admission, request, index-entry, orientation-view, source-receipt,
referenced reception, existing received identifier basis, and second received
identifiers, and records one local orientation instrument only.

The suite does not create second index entry, local medium multiplicity result,
relation view, comparison view, repeated reception permission, arbitrary
reception, feed, index system, registry, search, ranking, source transfer,
source receipt, authority, currentness, truth, action, synchronization,
participation authorization, participant role, runtime permission, public API,
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

import resolve_local_relevance_medium_second_relevance_orientation_view_v0_min as resolver  # noqa: E402


DEFAULT_SECOND_RECEIPT_ARTIFACT = (
    REPO_ROOT
    / "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_receipt_v0_min/"
    "local_relevance_medium_second_bounded_relevance_receipt_reference_review_001__"
    "local_relevance_medium_second_bounded_relevance_receipt_v0_min_result.json"
)

EXPECTED_OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min"
)
FORBIDDEN_EXACT_OUTPUT_ROOTS = (
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
BASIS_INDEX_ENTRY_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min/"
    "local_relevance_orientation_index_entry_reference_review_001__"
    "local_relevance_orientation_index_entry_v0_min_result.json"
)
ORIENTATION_VIEW_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min/"
    "relevance_orientation_view_reference_review_001__relevance_orientation_view_v0_min_result.json"
)
SOURCE_RECEIPT_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2/"
    "bounded_relevance_receipt_reference_review_001__bounded_relevance_receipt_v0_min_v2_result.json"
)
REFERENCED_RECEPTION_ARTIFACT = (
    "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min/"
    "bounded_relevance_reception_reference_review_001__bounded_relevance_reception_v0_min_result.json"
)

EXPECTED_TOP_LEVEL_SECTIONS = {
    "local_relevance_medium_second_relevance_orientation_view_metadata",
    "declared_local_relevance_medium_second_relevance_orientation_view_question",
    "selected_second_bounded_relevance_receipt_artifact_basis",
    "second_relevance_orientation_view",
    "local_relevance_medium_second_relevance_orientation_view_checks",
    "local_relevance_medium_second_relevance_orientation_view_statement",
    "local_relevance_medium_second_relevance_orientation_view_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_second_relevance_orientation_view_summary",
}

SECOND_ORIENTATION_VIEW_FIELDS = {
    "second_orientation_view_id",
    "second_orientation_view_type",
    "second_orientation_view_version",
    "second_orientation_scope",
    "basis_second_bounded_relevance_receipt_artifact",
    "basis_second_bounded_relevance_receipt_outcome",
    "basis_second_bounded_relevance_receipt_result_version",
    "basis_second_bounded_relevance_receipt_failed_check_count",
    "basis_second_bounded_relevance_reception_artifact",
    "basis_successor_candidate_admission_artifact",
    "basis_successor_reception_request_artifact",
    "basis_index_entry_artifact",
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
    "inspectably_present",
    "standing_identifiers",
    "non_inference",
    "unavailable",
    "orientation_statement",
    "second_receipt_expanded",
    "second_reception_expanded",
    "second_index_entry_created",
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

WRAPPER_KEYS_FORBIDDEN_IN_SECOND_ORIENTATION_VIEW = {
    "outcome",
    "block",
    "local_relevance_medium_second_relevance_orientation_view_checks",
    "non_claims",
    "local_relevance_medium_second_relevance_orientation_view_summary",
    "local_relevance_medium_second_relevance_orientation_view_metadata",
}

EXPECTED_INSPECTABLY_PRESENT = {
    "second bounded relevance receipt artifact",
    "referenced second bounded relevance reception artifact",
    "second received signal id",
    "second relevance basis id",
    "second relevance scope id",
    "second carrier context id",
    "second reception envelope id",
}

EXPECTED_STANDING_IDENTIFIERS = {
    "second_received_signal_id": "bounded_relevance_signal_002",
    "second_relevance_basis_id": "bounded_relevance_basis_002",
    "second_relevance_scope_id": "bounded_relevance_scope_002",
    "second_carrier_context_id": "bounded_relevance_signal_carrier_context_002",
    "second_reception_envelope_id": "bounded_relevance_reception_envelope_002",
}

EXPECTED_NON_INFERENCE_FALSE_FIELDS = {
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
    "follow_on_work_authorized",
}

EXPECTED_UNAVAILABLE = {
    "second local relevance orientation index entry",
    "local medium multiplicity result",
    "relation view",
    "comparison view",
    "source standing",
    "authority standing",
    "operative currentness",
    "truth claim",
    "action authorization",
    "synchronization authorization",
    "participation authorization",
    "participant role",
    "runtime permission",
    "public interface",
    "distributed network behavior",
    "follow-on work authorization",
}

ORIENTATION_OBJECT_FALSE_FIELDS = {
    "second_receipt_expanded",
    "second_reception_expanded",
    "second_index_entry_created",
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

NO_CREATION_NON_CLAIMS = {
    "second_receipt_expanded",
    "second_reception_expanded",
    "second_index_entry_created",
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
    "operation_permission_created",
    "follow_on_work_authorized",
}

HOSTILE_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_second_orientation_body",
    "raw_second_relevance_orientation_view_body",
    "raw_second_receipt_body",
    "raw_second_reception_body",
    "raw_successor_candidate_admission_body",
    "raw_successor_reception_request_body",
    "raw_index_entry_body",
    "raw_orientation_body",
    "raw_bounded_relevance_receipt_body",
    "raw_bounded_relevance_reception_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "second_orientation_body",
    "second_relevance_orientation_view_body",
    "second_receipt_body",
    "second_reception_body",
    "successor_candidate_admission_body",
    "successor_reception_request_body",
    "index_entry_body",
    "orientation_body",
    "bounded_relevance_receipt_body",
    "bounded_relevance_reception_body",
    "source_body",
    "authority_body",
    "currentness_body",
    "action_body",
    "synchronization_body",
    "public_api_body",
    "participant_facing_interface_body",
    "distributed_network_behavior_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_CANDIDATE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RECEPTION_REQUEST_BODY_MUST_NOT_RETURN",
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


def _write_json(path: Path, value: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")
    return path


def _synthetic_second_receipt_artifact() -> dict[str, Any]:
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_RECORDED",
        "local_relevance_medium_second_bounded_relevance_receipt_metadata": {
            "local_relevance_medium_second_bounded_relevance_receipt_id": (
                "local_relevance_medium_second_bounded_relevance_receipt_001"
            ),
            "local_relevance_medium_second_bounded_relevance_receipt_type": (
                "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT"
            ),
            "local_relevance_medium_second_bounded_relevance_receipt_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 75,
            "resolver_module": (
                "resolve_local_relevance_medium_second_bounded_relevance_receipt_v0_min"
            ),
        },
        "second_bounded_relevance_receipt_object": {
            "second_receipt_id": "local_relevance_medium_second_bounded_relevance_receipt_001",
            "second_receipt_type": "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT",
            "second_receipt_version": "0.1.0",
            "second_receipt_scope": "SECOND_INSPECTABLE_RECEIPT_ONLY",
            "basis_second_bounded_relevance_reception_artifact": (
                BASIS_SECOND_RECEPTION_ARTIFACT
            ),
            "basis_second_bounded_relevance_reception_outcome": (
                "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_RECORDED"
            ),
            "basis_second_bounded_relevance_reception_result_version": "0.1.0",
            "basis_second_bounded_relevance_reception_failed_check_count": 0,
            "basis_successor_candidate_admission_artifact": (
                BASIS_SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT
            ),
            "basis_successor_reception_request_artifact": (
                BASIS_SUCCESSOR_RECEPTION_REQUEST_ARTIFACT
            ),
            "basis_index_entry_artifact": BASIS_INDEX_ENTRY_ARTIFACT,
            "existing_orientation_view_artifact": ORIENTATION_VIEW_ARTIFACT,
            "existing_source_receipt_artifact": SOURCE_RECEIPT_ARTIFACT,
            "existing_referenced_reception_artifact": REFERENCED_RECEPTION_ARTIFACT,
            "existing_received_signal_id": "bounded_relevance_signal_001",
            "existing_received_relevance_basis_id": "bounded_relevance_basis_001",
            "existing_received_relevance_scope_id": "bounded_relevance_scope_001",
            "existing_received_carrier_context_id": (
                "bounded_relevance_signal_carrier_context_001"
            ),
            "existing_received_reception_envelope_id": (
                "bounded_relevance_reception_envelope_001"
            ),
            "admitted_successor_candidate_id": "bounded_relevance_signal_candidate_002",
            "second_received_signal_id": "bounded_relevance_signal_002",
            "second_relevance_basis_id": "bounded_relevance_basis_002",
            "second_relevance_scope_id": "bounded_relevance_scope_002",
            "second_carrier_context_id": "bounded_relevance_signal_carrier_context_002",
            "second_reception_envelope_id": "bounded_relevance_reception_envelope_002",
            "second_reception_artifact_preserved": True,
            "second_received_identifiers_preserved": True,
            "second_receipt_does_not_expand_reception": True,
            "second_orientation_view_created": False,
            "second_index_entry_created": False,
            "local_medium_multiplicity_result_created": False,
            "relation_view_created": False,
            "comparison_view_created": False,
            "repeated_reception_permission_created": False,
            "arbitrary_reception_created": False,
            "feed_created": False,
            "index_system_created": False,
            "registry_created": False,
            "search_surface_created": False,
            "ranking_surface_created": False,
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
        },
        "local_relevance_medium_second_bounded_relevance_receipt_checks": [
            {"check_name": "synthetic_clean_check", "passed": True}
        ],
        "local_relevance_medium_second_bounded_relevance_receipt_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 75,
            "resolver_module": (
                "resolve_local_relevance_medium_second_bounded_relevance_receipt_v0_min"
            ),
        },
    }


def _clean_request(second_receipt_artifact_path: Path) -> dict[str, Any]:
    return resolver.build_declared_local_relevance_medium_second_relevance_orientation_view_v0_min_request(
        selected_second_bounded_relevance_receipt_artifact=second_receipt_artifact_path,
    )


def _block_code(result: dict[str, Any]) -> str | None:
    block = result.get("block")
    if not isinstance(block, dict):
        return None
    return block.get("code") or block.get("block_code")


def _checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        check
        for check in result.get("local_relevance_medium_second_relevance_orientation_view_checks", [])
        if isinstance(check, dict)
    ]


def _failed_checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return [check for check in _checks(result) if check.get("passed") is not True]


def _set_second_receipt_object_field(
    artifact: dict[str, Any],
    field: str,
    value: Any = None,
) -> dict[str, Any]:
    updated = copy.deepcopy(artifact)
    updated["second_bounded_relevance_receipt_object"][field] = value
    return updated


def _set_metadata(artifact: dict[str, Any], field: str, value: Any) -> dict[str, Any]:
    updated = copy.deepcopy(artifact)
    updated["local_relevance_medium_second_bounded_relevance_receipt_metadata"][field] = value
    return updated


def _without_key(artifact: dict[str, Any], field: str) -> dict[str, Any]:
    updated = copy.deepcopy(artifact)
    updated.pop(field, None)
    return updated


def _flip_non_claim(request: dict[str, Any], field: str) -> dict[str, Any]:
    updated = copy.deepcopy(request)
    updated["declared_non_claims"][field] = True
    return updated


def _path_text(path: Path | str) -> str:
    return Path(path).as_posix().rstrip("/")


def _path_has_suffix(path: Path | str, suffix: Path | str) -> bool:
    path_parts = Path(path).parts
    suffix_parts = Path(suffix).parts
    return len(path_parts) >= len(suffix_parts) and path_parts[-len(suffix_parts) :] == suffix_parts


def _same_or_under(path: Path | str, root: Path | str) -> bool:
    path_text = _path_text(path)
    root_text = _path_text(root)
    return path_text == root_text or path_text.startswith(f"{root_text}/")


class LocalRelevanceMediumSecondRelevanceOrientationViewTests(unittest.TestCase):
    def write_synthetic_artifact(
        self,
        tmp_path: Path,
        artifact: dict[str, Any] | None = None,
        name: str = "second_bounded_relevance_receipt",
    ) -> tuple[dict[str, Any], Path, dict[str, Any]]:
        synthetic = copy.deepcopy(artifact or _synthetic_second_receipt_artifact())
        artifact_path = _write_json(tmp_path / f"{name}.json", synthetic)
        return _clean_request(artifact_path), artifact_path, synthetic

    def assert_not_blocked(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_output_root_is_second_orientation_only(self) -> None:
        output_root = resolver.OUTPUT_ROOT
        self.assertTrue(_path_has_suffix(output_root, EXPECTED_OUTPUT_ROOT), output_root)
        normalized = _path_text(output_root)
        forbidden_text = {_path_text(root) for root in FORBIDDEN_EXACT_OUTPUT_ROOTS}
        self.assertNotIn(normalized, forbidden_text)

    def assert_path_under_second_orientation_output_root_only(
        self,
        output_path: Path,
        output_root: Path,
    ) -> None:
        self.assertTrue(_same_or_under(output_path, output_root), output_path)
        self.assertTrue(_path_has_suffix(output_root, EXPECTED_OUTPUT_ROOT), output_root)
        for forbidden_root in FORBIDDEN_EXACT_OUTPUT_ROOTS:
            self.assertFalse(_same_or_under(output_path, forbidden_root))
        artifacts_root = output_root.parent
        for forbidden_root in FORBIDDEN_EXACT_OUTPUT_ROOTS:
            forbidden_sibling = artifacts_root / forbidden_root.name
            self.assertFalse(_same_or_under(output_path, forbidden_sibling))

    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        code = _block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in _checks(result):
            for key in ("block_code", "failure_code"):
                value = check.get(key)
                if value is not None:
                    self.assertIn(value, resolver.BLOCK_CODES)

    def assert_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        self.assertIsNotNone(block.get("code") or block.get("block_code"))
        self.assertTrue(_failed_checks(result))
        self.assert_public_block_codes(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_created_posture(result)
        self.assert_second_orientation_view_is_small(result)

    def assert_non_claims_canonical_false(self, result: dict[str, Any]) -> None:
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False)
            self.assertIsInstance(result["non_claims"][key], bool)

    def assert_second_orientation_view_is_small(self, result: dict[str, Any]) -> None:
        orientation_view = result.get("second_relevance_orientation_view")
        if orientation_view is None:
            return
        self.assertIsInstance(orientation_view, dict)
        self.assertLessEqual(set(orientation_view), SECOND_ORIENTATION_VIEW_FIELDS)
        for key in WRAPPER_KEYS_FORBIDDEN_IN_SECOND_ORIENTATION_VIEW:
            self.assertNotIn(key, orientation_view)

    def assert_no_created_posture(self, result: dict[str, Any]) -> None:
        for key in NO_CREATION_NON_CLAIMS:
            self.assertIs(result["non_claims"][key], False)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)

        orientation_view = result.get("second_relevance_orientation_view")
        if isinstance(orientation_view, dict) and orientation_view:
            for key in ORIENTATION_OBJECT_FALSE_FIELDS:
                self.assertIs(orientation_view[key], False, key)
            for key in EXPECTED_NON_INFERENCE_FALSE_FIELDS:
                self.assertIs(orientation_view["non_inference"][key], False, key)

    def assert_second_orientation_view_content(
        self,
        result: dict[str, Any],
        artifact_path: Path,
    ) -> None:
        orientation_view = result["second_relevance_orientation_view"]
        self.assertEqual(
            orientation_view["second_orientation_view_id"],
            "local_relevance_medium_second_relevance_orientation_view_001",
        )
        self.assertEqual(
            orientation_view["second_orientation_view_type"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW",
        )
        self.assertEqual(orientation_view["second_orientation_view_version"], "0.1.0")
        self.assertEqual(orientation_view["second_orientation_scope"], "SECOND_LOCAL_ORIENTATION_ONLY")
        self.assertEqual(
            orientation_view["basis_second_bounded_relevance_receipt_artifact"],
            str(artifact_path),
        )
        self.assertEqual(
            orientation_view["basis_second_bounded_relevance_receipt_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_RECORDED",
        )
        self.assertEqual(
            orientation_view["basis_second_bounded_relevance_receipt_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            orientation_view["basis_second_bounded_relevance_receipt_failed_check_count"],
            0,
        )
        self.assertEqual(
            orientation_view["basis_second_bounded_relevance_reception_artifact"],
            BASIS_SECOND_RECEPTION_ARTIFACT,
        )
        self.assertEqual(
            orientation_view["basis_successor_candidate_admission_artifact"],
            BASIS_SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT,
        )
        self.assertEqual(
            orientation_view["basis_successor_reception_request_artifact"],
            BASIS_SUCCESSOR_RECEPTION_REQUEST_ARTIFACT,
        )
        self.assertEqual(orientation_view["basis_index_entry_artifact"], BASIS_INDEX_ENTRY_ARTIFACT)
        self.assertEqual(orientation_view["existing_orientation_view_artifact"], ORIENTATION_VIEW_ARTIFACT)
        self.assertEqual(orientation_view["existing_source_receipt_artifact"], SOURCE_RECEIPT_ARTIFACT)
        self.assertEqual(
            orientation_view["existing_referenced_reception_artifact"],
            REFERENCED_RECEPTION_ARTIFACT,
        )
        self.assertEqual(orientation_view["existing_received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(
            orientation_view["existing_received_relevance_basis_id"],
            "bounded_relevance_basis_001",
        )
        self.assertEqual(
            orientation_view["existing_received_relevance_scope_id"],
            "bounded_relevance_scope_001",
        )
        self.assertEqual(
            orientation_view["existing_received_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_001",
        )
        self.assertEqual(
            orientation_view["existing_received_reception_envelope_id"],
            "bounded_relevance_reception_envelope_001",
        )
        self.assertEqual(
            orientation_view["admitted_successor_candidate_id"],
            "bounded_relevance_signal_candidate_002",
        )
        self.assertEqual(orientation_view["second_received_signal_id"], "bounded_relevance_signal_002")
        self.assertNotEqual(
            orientation_view["second_received_signal_id"],
            orientation_view["existing_received_signal_id"],
        )
        self.assertEqual(orientation_view["second_relevance_basis_id"], "bounded_relevance_basis_002")
        self.assertEqual(orientation_view["second_relevance_scope_id"], "bounded_relevance_scope_002")
        self.assertEqual(
            orientation_view["second_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_002",
        )
        self.assertEqual(
            orientation_view["second_reception_envelope_id"],
            "bounded_relevance_reception_envelope_002",
        )

        self.assertTrue(EXPECTED_INSPECTABLY_PRESENT.issubset(orientation_view["inspectably_present"]))
        self.assertEqual(orientation_view["standing_identifiers"], EXPECTED_STANDING_IDENTIFIERS)
        for key in EXPECTED_NON_INFERENCE_FALSE_FIELDS:
            self.assertIn(key, orientation_view["non_inference"])
            self.assertIs(orientation_view["non_inference"][key], False)
            self.assertIsInstance(orientation_view["non_inference"][key], bool)
        self.assertTrue(EXPECTED_UNAVAILABLE.issubset(orientation_view["unavailable"]))
        self.assert_no_created_posture(result)
        self.assert_second_orientation_view_is_small(result)

    def assert_official_values_preserved(self, result: dict[str, Any]) -> None:
        orientation_view = result["second_relevance_orientation_view"]
        self.assertEqual(
            orientation_view["second_orientation_view_type"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW",
        )
        self.assertEqual(orientation_view["second_orientation_scope"], "SECOND_LOCAL_ORIENTATION_ONLY")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        for value in (
            "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW",
            "SECOND_LOCAL_ORIENTATION_ONLY",
            resolver.OUTCOME_RECORDED,
        ):
            self.assertIn(value, serialized)
        self.assertNotEqual(
            orientation_view["second_orientation_view_type"],
            "[REDACTED_RAW_BODY_CONTENT]",
        )
        self.assertNotEqual(orientation_view["second_orientation_scope"], "[REDACTED_RAW_BODY_CONTENT]")

    def assert_no_hostile_sentinels(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_generated_booleans_are_bool(self, value: Any) -> None:
        if isinstance(value, dict):
            for item in value.values():
                self.assert_generated_booleans_are_bool(item)
        elif isinstance(value, list):
            for item in value:
                self.assert_generated_booleans_are_bool(item)
        elif isinstance(value, bool):
            self.assertIsInstance(value, bool)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_local_relevance_medium_second_relevance_orientation_view_v0_min",
            "resolve_local_relevance_medium_second_relevance_orientation_view_v0_min_from_path",
            "write_local_relevance_medium_second_relevance_orientation_view_v0_min_result",
            "build_local_relevance_medium_second_relevance_orientation_view_v0_min_summary",
            "build_declared_local_relevance_medium_second_relevance_orientation_view_v0_min_request",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_ORIENTATION_SCOPE_VALUES",
            "SUPPORTED_SECOND_ORIENTATION_TYPE_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_second_relevance_orientation_view_v0_min",
        )
        self.assert_output_root_is_second_orientation_only()
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW",
            resolver.SUPPORTED_SECOND_ORIENTATION_TYPE_VALUES,
        )
        self.assertIn(
            "SECOND_LOCAL_ORIENTATION_ONLY",
            resolver.SUPPORTED_SECOND_ORIENTATION_SCOPE_VALUES,
        )

    def test_successful_recorded_result_from_synthetic_second_receipt_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, artifact_path, _ = self.write_synthetic_artifact(Path(tmp))
            result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min(
                request
            )
            summary = resolver.build_local_relevance_medium_second_relevance_orientation_view_v0_min_summary(
                result
            )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            summary["second_orientation_id"],
            "local_relevance_medium_second_relevance_orientation_view_001",
        )
        self.assertTrue(EXPECTED_TOP_LEVEL_SECTIONS.issubset(result))

        self.assert_second_orientation_view_content(result, artifact_path)
        statement = result["local_relevance_medium_second_relevance_orientation_view_statement"]
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
        self.assert_non_claims_canonical_false(result)
        self.assert_generated_booleans_are_bool(result)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_SECOND_RECEIPT_ARTIFACT.exists():
            self.skipTest("default local relevance medium second bounded relevance receipt artifact absent")
        request = resolver.build_declared_local_relevance_medium_second_relevance_orientation_view_v0_min_request()
        result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min(request)
        summary = resolver.build_local_relevance_medium_second_relevance_orientation_view_v0_min_summary(
            result
        )

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        orientation_view = result["second_relevance_orientation_view"]
        self.assertEqual(
            orientation_view["second_orientation_view_type"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW",
        )
        self.assertEqual(orientation_view["second_orientation_scope"], "SECOND_LOCAL_ORIENTATION_ONLY")
        self.assertEqual(orientation_view["standing_identifiers"], EXPECTED_STANDING_IDENTIFIERS)
        self.assertTrue(EXPECTED_INSPECTABLY_PRESENT.issubset(orientation_view["inspectably_present"]))
        self.assertTrue(EXPECTED_UNAVAILABLE.issubset(orientation_view["unavailable"]))
        for key in EXPECTED_NON_INFERENCE_FALSE_FIELDS:
            self.assertIs(orientation_view["non_inference"][key], False)
        self.assert_no_created_posture(result)

    def test_declared_non_claims_flipped_true_block_and_final_non_claims_false(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            clean_request, _, _ = self.write_synthetic_artifact(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min(
                        request
                    )
                    self.assert_blocked(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_non_claims_canonical_false(result)

    def test_representative_blocking_behavior(self) -> None:
        def mutate_artifact(field: str, value: Any) -> Any:
            return lambda artifact, request, tmp: (
                _set_second_receipt_object_field(artifact, field, value),
                request,
            )

        def request_flag(field: str) -> Any:
            return lambda artifact, request, tmp: (artifact, {**request, field: True})

        cases: list[tuple[str, Any]] = [
            (
                "explicit block intent",
                lambda a, r, t: (
                    a,
                    {
                        **r,
                        "local_relevance_medium_second_relevance_orientation_view_intent": (
                            "BLOCK_LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW"
                        ),
                    },
                ),
            ),
            ("missing request", lambda a, r, t: (a, {})),
            (
                "unsupported intent",
                lambda a, r, t: (
                    a,
                    {
                        **r,
                        "local_relevance_medium_second_relevance_orientation_view_intent": "UNSUPPORTED",
                    },
                ),
            ),
            (
                "artifact path missing",
                lambda a, r, t: (a, {**r, "selected_second_bounded_relevance_receipt_artifact": ""}),
            ),
            (
                "artifact unreadable",
                lambda a, r, t: (
                    a,
                    {
                        **r,
                        "selected_second_bounded_relevance_receipt_artifact": str(t / "missing.json"),
                        "__skip_artifact_write": True,
                    },
                ),
            ),
            ("artifact JSON array", lambda a, r, t: (["not", "object"], r)),
            ("artifact not recorded", lambda a, r, t: ({**a, "outcome": "NOT_RECORDED"}, r)),
            ("artifact failed checks", lambda a, r, t: (_set_metadata(a, "failed_check_count", 1), r)),
            (
                "artifact wrong version",
                lambda a, r, t: (
                    _set_metadata(
                        a,
                        "local_relevance_medium_second_bounded_relevance_receipt_version",
                        "9.9.9",
                    ),
                    r,
                ),
            ),
            ("object missing", lambda a, r, t: (_without_key(a, "second_bounded_relevance_receipt_object"), r)),
            ("second receipt type invalid", mutate_artifact("second_receipt_type", "WRONG")),
            ("second receipt scope invalid", mutate_artifact("second_receipt_scope", "WRONG")),
            ("second received signal missing", mutate_artifact("second_received_signal_id", None)),
            (
                "second received signal equals existing",
                mutate_artifact("second_received_signal_id", "bounded_relevance_signal_001"),
            ),
            ("second relevance basis missing", mutate_artifact("second_relevance_basis_id", None)),
            ("second relevance scope missing", mutate_artifact("second_relevance_scope_id", None)),
            ("second carrier context missing", mutate_artifact("second_carrier_context_id", None)),
            ("second reception envelope missing", mutate_artifact("second_reception_envelope_id", None)),
            ("second orientation view type missing", lambda a, r, t: (a, {**r, "second_orientation_view_type": None})),
            (
                "second orientation view type invalid",
                lambda a, r, t: (a, {**r, "second_orientation_view_type": "WRONG"}),
            ),
            ("second orientation scope missing", lambda a, r, t: (a, {**r, "second_orientation_scope": None})),
            (
                "second orientation scope invalid",
                lambda a, r, t: (a, {**r, "second_orientation_scope": "WRONG"}),
            ),
            ("inspectably present incomplete", request_flag("inspectably_present_missing_or_incomplete")),
            ("standing identifiers not preserved", request_flag("standing_identifiers_missing_or_not_preserved")),
            ("non-inference flipped", request_flag("non_inference_missing_or_flipped")),
            ("unavailable claims missing", request_flag("unavailable_missing_required_claims")),
            ("second receipt expanded", request_flag("second_receipt_expanded")),
            ("second reception expanded", request_flag("second_reception_expanded")),
            ("second index entry created", request_flag("second_index_entry_created")),
            ("local medium multiplicity result created", request_flag("local_medium_multiplicity_result_created")),
            ("relation view created", request_flag("relation_view_created")),
            ("comparison view created", request_flag("comparison_view_created")),
            ("repeated reception permission created", request_flag("repeated_reception_permission_created")),
            ("arbitrary reception created", request_flag("arbitrary_reception_created")),
            ("feed created", request_flag("feed_created")),
            ("index system created", request_flag("index_system_created")),
            ("registry created", request_flag("registry_created")),
            ("search surface created", request_flag("search_surface_created")),
            ("ranking surface created", request_flag("ranking_surface_created")),
            ("source transfer occurred", request_flag("source_transfer_occurred")),
            ("source receipt occurred", request_flag("source_receipt_occurred")),
            ("source created", request_flag("source_created")),
            ("authority created", request_flag("authority_created")),
            ("currentness created", request_flag("currentness_created")),
            ("truth created", request_flag("truth_created")),
            ("action created", request_flag("action_created")),
            ("synchronization created", request_flag("synchronization_created")),
            ("participation authorized", request_flag("participation_authorized")),
            ("participant role created", request_flag("participant_role_created")),
            ("runtime permission created", request_flag("runtime_permission_created")),
            ("public API created", request_flag("public_api_created")),
            ("participant-facing interface created", request_flag("participant_facing_interface_created")),
            ("distributed network behavior created", request_flag("distributed_network_behavior_created")),
            ("deployment created", request_flag("deployment_created")),
            ("public release created", request_flag("public_release_created")),
            ("operation permission created", request_flag("operation_permission_created")),
            ("broader reusable permission created", request_flag("broader_reusable_permission_created")),
            ("follow-on work authorized", request_flag("follow_on_work_authorized")),
            (
                "artifact existence authority",
                request_flag("artifact_existence_treated_as_second_orientation_authority"),
            ),
            (
                "latest file posture authority",
                request_flag("latest_file_posture_treated_as_second_orientation_authority"),
            ),
            (
                "repo local availability authority",
                request_flag("repo_local_availability_treated_as_second_orientation_authority"),
            ),
            (
                "hidden repo state content",
                request_flag("hidden_repo_state_used_as_second_orientation_content"),
            ),
            (
                "hidden repo state authority",
                request_flag("hidden_repo_state_used_as_second_orientation_authority"),
            ),
            ("predecessor failure repaired", request_flag("predecessor_failure_repaired")),
            ("predecessor failure hidden", request_flag("predecessor_failure_hidden")),
            ("predecessor failure claimed passed", request_flag("predecessor_failure_claimed_passed")),
            ("consumed request reopened", request_flag("consumed_request_reopened")),
            ("authorization token reused", request_flag("authorization_token_reused")),
            ("required non-claim flipped", lambda a, r, t: (a, _flip_non_claim(r, "feed_created"))),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            base_artifact = _synthetic_second_receipt_artifact()
            for name, mutator in cases:
                with self.subTest(name=name):
                    request = _clean_request(tmp_path / f"{name.replace(' ', '_')}.json")
                    artifact, request = mutator(copy.deepcopy(base_artifact), request, tmp_path)
                    if isinstance(artifact, list):
                        _write_json(Path(request["selected_second_bounded_relevance_receipt_artifact"]), artifact)
                    elif request.get("selected_second_bounded_relevance_receipt_artifact") and not request.get(
                        "__skip_artifact_write"
                    ):
                        artifact_path = _write_json(
                            Path(request["selected_second_bounded_relevance_receipt_artifact"]),
                            artifact,
                        )
                        request["selected_second_bounded_relevance_receipt_artifact"] = str(artifact_path)
                    result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min(
                        request
                    )
                    self.assert_blocked(result)

        non_mapping_result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min(
            ["not", "mapping"]
        )
        self.assert_blocked(non_mapping_result)

    def test_missing_or_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            clean_request, _, _ = self.write_synthetic_artifact(Path(tmp))
            variants = []
            removed = copy.deepcopy(clean_request)
            removed.pop("declared_non_claims")
            variants.append(removed)
            empty = copy.deepcopy(clean_request)
            empty["declared_non_claims"] = {}
            variants.append(empty)
            missing_one = copy.deepcopy(clean_request)
            missing_one["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])
            variants.append(missing_one)
            string_one = copy.deepcopy(clean_request)
            string_one["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = "false"
            variants.append(string_one)
            none_one = copy.deepcopy(clean_request)
            none_one["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = None
            variants.append(none_one)

            for request in variants:
                with self.subTest(variant=request.get("declared_non_claims")):
                    result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min(
                        request
                    )
                    self.assertIn(
                        result["outcome"],
                        (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS),
                    )
                    self.assert_public_block_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _ = self.write_synthetic_artifact(Path(tmp))
            result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min(
                request
            )

        self.assert_official_values_preserved(result)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW_NOT_RECORDED",
                "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW_BLOCKED",
            },
        )

    def test_raw_hidden_hostile_content_containment_and_input_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, artifact_path, artifact = self.write_synthetic_artifact(Path(tmp))
            for key, sentinel in zip(HOSTILE_KEYS, HOSTILE_SENTINELS * 3):
                request[key] = sentinel
                artifact[key] = sentinel
                artifact["second_bounded_relevance_receipt_object"][key] = sentinel
            request["not_recorded_basis"] = [
                {"raw_second_orientation_body": HOSTILE_SENTINELS[0]},
                {"raw_second_receipt_body": HOSTILE_SENTINELS[2]},
                {"hidden_repo_state": HOSTILE_SENTINELS[-1]},
            ]
            request_before = copy.deepcopy(request)
            artifact_before = copy.deepcopy(artifact)
            _write_json(artifact_path, artifact)

            result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min(
                request
            )

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        if result["outcome"] == resolver.OUTCOME_BLOCKED:
            self.assert_public_block_codes(result)
        self.assert_no_hostile_sentinels(result)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW", serialized)
        self.assertIn("SECOND_LOCAL_ORIENTATION_ONLY", serialized)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_created_posture(result)
        self.assertEqual(request, request_before)
        self.assertEqual(artifact, artifact_before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request, _, _ = self.write_synthetic_artifact(tmp_path)
            request_path = _write_json(tmp_path / "request.json", request)

            result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min_from_path(
                request_path
            )
            summary = resolver.build_local_relevance_medium_second_relevance_orientation_view_v0_min_summary(
                result
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_not_blocked(result)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            with self.assertRaises(
                resolver.LocalRelevanceMediumSecondRelevanceOrientationViewV0MinError
            ):
                resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min_from_path(
                    malformed_path
                )

            array_path = _write_json(tmp_path / "array.json", [])
            array_result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min_from_path(
                array_path
            )
            self.assert_blocked(array_result)

            with self.assertRaises(
                resolver.LocalRelevanceMediumSecondRelevanceOrientationViewV0MinError
            ):
                resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min_from_path(
                    tmp_path / "missing_request.json"
                )

            output_root = tmp_path / EXPECTED_OUTPUT_ROOT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_medium_second_relevance_orientation_view_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_medium_second_relevance_orientation_view_v0_min_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(second_path.stem.endswith("_001"))
            json.loads(first_path.read_text(encoding="utf-8"))
            json.loads(second_path.read_text(encoding="utf-8"))
            self.assertIn("local_relevance_medium_second_relevance_orientation_view_v0_min", str(first_path))
            self.assert_path_under_second_orientation_output_root_only(first_path, output_root)
            self.assert_path_under_second_orientation_output_root_only(second_path, output_root)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, artifact = self.write_synthetic_artifact(Path(tmp))
            request["posture"] = {"nested": {"raw_body": HOSTILE_SENTINELS[0]}}
            before_request = copy.deepcopy(request)
            before_non_claims = copy.deepcopy(request["declared_non_claims"])
            before_artifact = copy.deepcopy(artifact)

            result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min(
                request
            )

        self.assertEqual(request, before_request)
        self.assertEqual(request["declared_non_claims"], before_non_claims)
        self.assertEqual(artifact, before_artifact)
        self.assertEqual(
            request["selected_second_bounded_relevance_receipt_artifact"],
            before_request["selected_second_bounded_relevance_receipt_artifact"],
        )
        self.assertEqual(request["second_orientation_scope"], "SECOND_LOCAL_ORIENTATION_ONLY")
        self.assertEqual(
            request["second_orientation_view_type"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW",
        )
        self.assertEqual(request["posture"], before_request["posture"])
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _ = self.write_synthetic_artifact(Path(tmp))
            result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min(
                request
            )
            summary = resolver.build_local_relevance_medium_second_relevance_orientation_view_v0_min_summary(
                result
            )

        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)

        for field in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            with self.subTest(field=field):
                blocked_request = copy.deepcopy(request)
                blocked_request[field] = True
                blocked_result = resolver.resolve_local_relevance_medium_second_relevance_orientation_view_v0_min(
                    blocked_request
                )
                self.assert_blocked(blocked_result)


if __name__ == "__main__":
    unittest.main()
