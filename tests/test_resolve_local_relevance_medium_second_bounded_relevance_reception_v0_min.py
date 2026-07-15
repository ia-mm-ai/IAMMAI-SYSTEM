"""Tests for the local relevance medium second bounded relevance reception resolver.

This suite is bounded to one second reception object. It verifies that the
resolver reads one clean local relevance medium successor candidate admission
artifact, preserves the basis admission, request, index-entry, orientation-view,
receipt, reception, and existing received identifier basis, receives one
admitted successor candidate as bounded relevance material, declares second
received identifiers, and does not create repeated reception permission,
arbitrary reception, feed, second receipt, second orientation view, second index
entry, local medium multiplicity result, relation view, comparison view, index
system, registry, search, ranking, source transfer, source receipt, source,
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

import resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min as resolver  # noqa: E402


DEFAULT_SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT = (
    REPO_ROOT
    / "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_successor_candidate_admission_v0_min/"
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
    "local_relevance_medium_second_bounded_relevance_reception_metadata",
    "declared_local_relevance_medium_second_bounded_relevance_reception_question",
    "selected_successor_candidate_admission_artifact_basis",
    "second_bounded_relevance_reception_object",
    "local_relevance_medium_second_bounded_relevance_reception_checks",
    "local_relevance_medium_second_bounded_relevance_reception_statement",
    "local_relevance_medium_second_bounded_relevance_reception_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_medium_second_bounded_relevance_reception_summary",
}

SECOND_RECEPTION_OBJECT_FIELDS = {
    "second_reception_id",
    "second_reception_type",
    "second_reception_version",
    "second_reception_scope",
    "basis_successor_candidate_admission_artifact",
    "basis_successor_candidate_admission_outcome",
    "basis_successor_candidate_admission_result_version",
    "basis_successor_candidate_admission_failed_check_count",
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
    "admitted_successor_candidate_scope",
    "candidate_admission_status",
    "second_received_signal_id",
    "second_relevance_basis_id",
    "second_relevance_scope_id",
    "second_carrier_context_id",
    "second_reception_envelope_id",
    "multiplicity_purpose",
    "max_local_orientation_objects_after_second_reception",
    "second_bounded_relevance_reception_recorded",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "second_receipt_created",
    "second_orientation_view_created",
    "second_index_entry_created",
    "local_medium_multiplicity_result_created",
    "relation_view_created",
    "comparison_view_created",
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

WRAPPER_KEYS_FORBIDDEN_IN_SECOND_RECEPTION_OBJECT = {
    "outcome",
    "block",
    "local_relevance_medium_second_bounded_relevance_reception_checks",
    "non_claims",
    "local_relevance_medium_second_bounded_relevance_reception_summary",
    "local_relevance_medium_second_bounded_relevance_reception_metadata",
}

NO_CREATION_NON_CLAIMS = {
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "second_receipt_created",
    "second_orientation_view_created",
    "second_index_entry_created",
    "local_medium_multiplicity_result_created",
    "relation_view_created",
    "comparison_view_created",
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

HOSTILE_KEYS = [
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_second_reception_body",
    "raw_second_bounded_relevance_reception_body",
    "raw_successor_candidate_admission_body",
    "raw_successor_reception_request_body",
    "raw_successor_candidate_body",
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
    "second_reception_body",
    "second_bounded_relevance_reception_body",
    "successor_candidate_admission_body",
    "successor_reception_request_body",
    "successor_candidate_body",
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
]

HOSTILE_SENTINELS = [
    "RAW_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_CANDIDATE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RECEPTION_REQUEST_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_CANDIDATE_BODY_MUST_NOT_RETURN",
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
]


def _write_json(path: Path, value: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")
    return path


def _synthetic_successor_candidate_admission_artifact() -> dict[str, Any]:
    return {
        "outcome": "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_RECORDED",
        "local_relevance_medium_successor_candidate_admission_metadata": {
            "local_relevance_medium_successor_candidate_admission_id": (
                "local_relevance_medium_successor_candidate_admission_reference_review_001"
            ),
            "local_relevance_medium_successor_candidate_admission_type": (
                "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION"
            ),
            "local_relevance_medium_successor_candidate_admission_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 77,
            "resolver_module": "resolve_local_relevance_medium_successor_candidate_admission_v0_min",
        },
        "successor_candidate_admission_object": {
            "admission_id": "local_relevance_medium_successor_candidate_admission_001",
            "admission_type": "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION",
            "admission_version": "0.1.0",
            "admission_scope": "ONE_SUCCESSOR_CANDIDATE_ADMISSION_ONLY",
            "basis_successor_reception_request_artifact": (
                BASIS_SUCCESSOR_RECEPTION_REQUEST_ARTIFACT
            ),
            "basis_successor_reception_request_outcome": (
                "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_RECORDED"
            ),
            "basis_successor_reception_request_result_version": "0.1.0",
            "basis_successor_reception_request_failed_check_count": 0,
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
            "successor_candidate_id": "bounded_relevance_signal_candidate_002",
            "successor_candidate_scope": "BOUNDED_RELEVANCE_RECEPTION_CANDIDATE_ONLY",
            "candidate_admission_status": "ADMITTED_AS_SUCCESSOR_RECEPTION_CANDIDATE_ONLY",
            "future_second_reception_scope": "FUTURE_SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY",
            "multiplicity_purpose": "LOCAL_MEDIUM_MULTIPLICITY_TEST_ONLY",
            "max_local_orientation_objects_after_future_reception": 2,
            "successor_candidate_admitted_as_candidate": True,
            "second_reception_created": False,
            "candidate_received": False,
            "reception_authorization_created": False,
            "repeated_reception_permission_created": False,
            "arbitrary_reception_created": False,
            "feed_created": False,
            "relation_view_created": False,
            "comparison_view_created": False,
            "index_system_created": False,
            "registry_created": False,
            "search_surface_created": False,
            "ranking_surface_created": False,
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
        "local_relevance_medium_successor_candidate_admission_summary": {
            "outcome": "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "passed_check_count": 77,
            "resolver_module": "resolve_local_relevance_medium_successor_candidate_admission_v0_min",
        },
    }


def _clean_request(admission_artifact_path: Path) -> dict[str, Any]:
    return resolver.build_declared_local_relevance_medium_second_bounded_relevance_reception_v0_min_request(
        selected_successor_candidate_admission_artifact=admission_artifact_path,
    )


def _block_code(result: dict[str, Any]) -> str | None:
    block = result.get("block")
    if not isinstance(block, dict):
        return None
    return block.get("code") or block.get("block_code")


def _failed_checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        check
        for check in result.get(
            "local_relevance_medium_second_bounded_relevance_reception_checks", []
        )
        if isinstance(check, dict) and check.get("passed") is not True
    ]


def _set_admission_object_field(
    artifact: dict[str, Any],
    field: str,
    value: Any = None,
) -> dict[str, Any]:
    updated = copy.deepcopy(artifact)
    updated["successor_candidate_admission_object"][field] = value
    return updated


class LocalRelevanceMediumSecondBoundedRelevanceReceptionTests(unittest.TestCase):
    def write_synthetic_artifact(
        self,
        tmp_path: Path,
        artifact: dict[str, Any] | None = None,
        name: str = "successor_candidate_admission",
    ) -> tuple[dict[str, Any], Path, dict[str, Any]]:
        synthetic = copy.deepcopy(artifact or _synthetic_successor_candidate_admission_artifact())
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

    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        code = _block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in result.get(
            "local_relevance_medium_second_bounded_relevance_reception_checks", []
        ):
            if not isinstance(check, dict):
                continue
            for key in ("block_code", "failure_code"):
                value = check.get(key)
                if value is not None:
                    self.assertIn(value, resolver.BLOCK_CODES)

    def assert_blocked(
        self,
        result: dict[str, Any],
        expected_code: str | None = None,
    ) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        code = block.get("code") or block.get("block_code")
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        if expected_code is not None:
            failed_codes = {
                check.get("block_code") or check.get("failure_code")
                for check in _failed_checks(result)
            }
            self.assertIn(expected_code, failed_codes | {code})
        self.assertTrue(_failed_checks(result))
        self.assert_public_block_codes(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_created_posture(result)
        self.assert_second_reception_object_is_small(result)

    def assert_non_claims_canonical_false(self, result: dict[str, Any]) -> None:
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False)
            self.assertIsInstance(result["non_claims"][key], bool)

    def assert_second_reception_object_is_small(self, result: dict[str, Any]) -> None:
        second_reception_object = result.get("second_bounded_relevance_reception_object")
        if second_reception_object is None:
            return
        self.assertIsInstance(second_reception_object, dict)
        self.assertLessEqual(set(second_reception_object), SECOND_RECEPTION_OBJECT_FIELDS)
        for key in WRAPPER_KEYS_FORBIDDEN_IN_SECOND_RECEPTION_OBJECT:
            self.assertNotIn(key, second_reception_object)

    def assert_no_created_posture(self, result: dict[str, Any]) -> None:
        for key in NO_CREATION_NON_CLAIMS:
            self.assertIs(result["non_claims"][key], False)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)

        second_reception_object = result.get("second_bounded_relevance_reception_object")
        if isinstance(second_reception_object, dict) and second_reception_object:
            self.assertIs(
                second_reception_object["second_bounded_relevance_reception_recorded"],
                True,
            )
            for key in (
                "repeated_reception_permission_created",
                "arbitrary_reception_created",
                "feed_created",
                "second_receipt_created",
                "second_orientation_view_created",
                "second_index_entry_created",
                "local_medium_multiplicity_result_created",
                "relation_view_created",
                "comparison_view_created",
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
            ):
                self.assertIs(second_reception_object[key], False)

    def assert_official_values_preserved(self, result: dict[str, Any]) -> None:
        second_reception_object = result["second_bounded_relevance_reception_object"]
        self.assertEqual(
            second_reception_object["second_reception_type"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION",
        )
        self.assertEqual(
            second_reception_object["second_reception_scope"],
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY",
        )
        self.assertEqual(
            second_reception_object["admitted_successor_candidate_scope"],
            "BOUNDED_RELEVANCE_RECEPTION_CANDIDATE_ONLY",
        )
        self.assertEqual(
            second_reception_object["candidate_admission_status"],
            "ADMITTED_AS_SUCCESSOR_RECEPTION_CANDIDATE_ONLY",
        )
        self.assertEqual(
            second_reception_object["multiplicity_purpose"],
            "LOCAL_MEDIUM_MULTIPLICITY_TEST_ONLY",
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        for value in (
            second_reception_object["second_reception_type"],
            second_reception_object["second_reception_scope"],
            second_reception_object["admitted_successor_candidate_scope"],
            second_reception_object["candidate_admission_status"],
            second_reception_object["multiplicity_purpose"],
            result["outcome"],
        ):
            self.assertNotEqual(value, "[REDACTED_RAW_BODY]")

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
            "resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min",
            "resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min_from_path",
            "write_local_relevance_medium_second_bounded_relevance_reception_v0_min_result",
            "build_local_relevance_medium_second_bounded_relevance_reception_v0_min_summary",
            "build_declared_local_relevance_medium_second_bounded_relevance_reception_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_RECEPTION_SCOPE_VALUES",
            "SUPPORTED_SECOND_RECEPTION_TYPE_VALUES",
            "SUPPORTED_SUCCESSOR_CANDIDATE_SCOPE_VALUES",
            "SUPPORTED_CANDIDATE_ADMISSION_STATUS_VALUES",
            "SUPPORTED_MULTIPLICITY_PURPOSE_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min",
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_"
                "local_relevance_medium_second_bounded_relevance_reception_v0_min"
            )
        )
        self.assertIn(
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION",
            resolver.SUPPORTED_SECOND_RECEPTION_TYPE_VALUES,
        )
        self.assertIn(
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY",
            resolver.SUPPORTED_SECOND_RECEPTION_SCOPE_VALUES,
        )
        self.assertIn(
            "BOUNDED_RELEVANCE_RECEPTION_CANDIDATE_ONLY",
            resolver.SUPPORTED_SUCCESSOR_CANDIDATE_SCOPE_VALUES,
        )
        self.assertIn(
            "ADMITTED_AS_SUCCESSOR_RECEPTION_CANDIDATE_ONLY",
            resolver.SUPPORTED_CANDIDATE_ADMISSION_STATUS_VALUES,
        )
        self.assertIn(
            "LOCAL_MEDIUM_MULTIPLICITY_TEST_ONLY",
            resolver.SUPPORTED_MULTIPLICITY_PURPOSE_VALUES,
        )

        output_root = str(resolver.OUTPUT_ROOT)
        forbidden_substrings = (
            "local_relevance_medium_successor_candidate_admission_v0_min",
            "local_relevance_medium_successor_reception_request_v0_min",
            "local_relevance_orientation_index_entry_v0_min",
            "relevance_orientation_view_v0_min",
            "bounded_relevance_receipt_v0_min_v2",
            "bounded_relevance_reception_v0_min",
        )
        for forbidden in forbidden_substrings:
            self.assertNotIn(forbidden, output_root)
        for forbidden_part in (
            "source-transfer",
            "source-receipt",
            "reception",
            "public-api",
            "participant-facing-interface",
            "distributed-network",
        ):
            self.assertNotIn(forbidden_part, Path(output_root).parts)

    def test_successful_recorded_result_from_synthetic_candidate_admission_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            result = (
                resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
                    request
                )
            )
            summary = (
                resolver.build_local_relevance_medium_second_bounded_relevance_reception_v0_min_summary(
                    result
                )
            )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min",
        )
        metadata = result["local_relevance_medium_second_bounded_relevance_reception_metadata"]
        self.assertEqual(
            metadata["local_relevance_medium_second_bounded_relevance_reception_id"],
            request["local_relevance_medium_second_bounded_relevance_reception_id"],
        )
        self.assertTrue(EXPECTED_TOP_LEVEL_SECTIONS.issubset(set(result)))

        second_reception_object = result["second_bounded_relevance_reception_object"]
        self.assertEqual(
            second_reception_object["second_reception_id"],
            "local_relevance_medium_second_bounded_relevance_reception_001",
        )
        self.assertEqual(
            second_reception_object["second_reception_type"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION",
        )
        self.assertEqual(second_reception_object["second_reception_version"], "0.1.0")
        self.assertEqual(
            second_reception_object["second_reception_scope"],
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY",
        )
        self.assertEqual(
            second_reception_object["basis_successor_candidate_admission_artifact"],
            str(artifact_path),
        )
        self.assertEqual(
            second_reception_object["basis_successor_candidate_admission_outcome"],
            "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_RECORDED",
        )
        self.assertEqual(
            second_reception_object["basis_successor_candidate_admission_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            second_reception_object["basis_successor_candidate_admission_failed_check_count"],
            0,
        )
        self.assertEqual(
            second_reception_object["basis_successor_reception_request_artifact"],
            BASIS_SUCCESSOR_RECEPTION_REQUEST_ARTIFACT,
        )
        self.assertEqual(
            second_reception_object["basis_index_entry_artifact"],
            BASIS_INDEX_ENTRY_ARTIFACT,
        )
        self.assertEqual(
            second_reception_object["existing_orientation_view_artifact"],
            ORIENTATION_VIEW_ARTIFACT,
        )
        self.assertEqual(
            second_reception_object["existing_source_receipt_artifact"],
            SOURCE_RECEIPT_ARTIFACT,
        )
        self.assertEqual(
            second_reception_object["existing_referenced_reception_artifact"],
            REFERENCED_RECEPTION_ARTIFACT,
        )
        self.assertEqual(
            second_reception_object["existing_received_signal_id"],
            "bounded_relevance_signal_001",
        )
        self.assertEqual(
            second_reception_object["existing_received_relevance_basis_id"],
            "bounded_relevance_basis_001",
        )
        self.assertEqual(
            second_reception_object["existing_received_relevance_scope_id"],
            "bounded_relevance_scope_001",
        )
        self.assertEqual(
            second_reception_object["existing_received_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_001",
        )
        self.assertEqual(
            second_reception_object["existing_received_reception_envelope_id"],
            "bounded_relevance_reception_envelope_001",
        )
        self.assertEqual(
            second_reception_object["admitted_successor_candidate_id"],
            "bounded_relevance_signal_candidate_002",
        )
        self.assertEqual(
            second_reception_object["admitted_successor_candidate_scope"],
            "BOUNDED_RELEVANCE_RECEPTION_CANDIDATE_ONLY",
        )
        self.assertEqual(
            second_reception_object["candidate_admission_status"],
            "ADMITTED_AS_SUCCESSOR_RECEPTION_CANDIDATE_ONLY",
        )
        self.assertEqual(
            second_reception_object["second_received_signal_id"],
            "bounded_relevance_signal_002",
        )
        self.assertNotEqual(
            second_reception_object["second_received_signal_id"],
            second_reception_object["existing_received_signal_id"],
        )
        self.assertEqual(
            second_reception_object["second_relevance_basis_id"],
            "bounded_relevance_basis_002",
        )
        self.assertEqual(
            second_reception_object["second_relevance_scope_id"],
            "bounded_relevance_scope_002",
        )
        self.assertEqual(
            second_reception_object["second_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_002",
        )
        self.assertEqual(
            second_reception_object["second_reception_envelope_id"],
            "bounded_relevance_reception_envelope_002",
        )
        self.assertEqual(
            second_reception_object["multiplicity_purpose"],
            "LOCAL_MEDIUM_MULTIPLICITY_TEST_ONLY",
        )
        self.assertEqual(
            second_reception_object["max_local_orientation_objects_after_second_reception"],
            2,
        )
        self.assertIs(
            second_reception_object["second_bounded_relevance_reception_recorded"],
            True,
        )
        self.assert_no_created_posture(result)
        self.assert_second_reception_object_is_small(result)

        statement = result["local_relevance_medium_second_bounded_relevance_reception_statement"]
        for key in (
            "local_relevance_medium_second_bounded_relevance_reception_recorded",
            "basis_successor_candidate_admission_artifact_preserved",
            "basis_successor_reception_request_artifact_preserved",
            "basis_index_entry_artifact_preserved",
            "existing_orientation_view_artifact_preserved",
            "existing_source_receipt_artifact_preserved",
            "existing_referenced_reception_artifact_preserved",
            "existing_received_signal_id_preserved",
            "existing_received_relevance_basis_id_preserved",
            "existing_received_relevance_scope_id_preserved",
            "existing_received_carrier_context_id_preserved",
            "existing_received_reception_envelope_id_preserved",
            "admitted_successor_candidate_id_preserved",
            "second_received_signal_id_declared",
            "second_received_signal_differs_from_existing_signal",
            "second_relevance_basis_id_declared",
            "second_relevance_scope_id_declared",
            "second_carrier_context_id_declared",
            "second_reception_envelope_id_declared",
            "second_reception_scope_second_only",
            "multiplicity_purpose_local_only",
            "max_local_orientation_objects_after_second_reception_is_two",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(statement[key], True)
        self.assert_non_claims_canonical_false(result)
        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_bool(result)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT.exists():
            self.skipTest("default local relevance medium successor candidate admission artifact absent")

        request = (
            resolver.build_declared_local_relevance_medium_second_bounded_relevance_reception_v0_min_request()
        )
        result = (
            resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
                request
            )
        )
        summary = (
            resolver.build_local_relevance_medium_second_bounded_relevance_reception_v0_min_summary(
                result
            )
        )
        second_reception_object = result["second_bounded_relevance_reception_object"]

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        self.assertEqual(
            second_reception_object["second_reception_type"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION",
        )
        self.assertEqual(
            second_reception_object["second_reception_scope"],
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY",
        )
        self.assertEqual(
            second_reception_object["admitted_successor_candidate_id"],
            "bounded_relevance_signal_candidate_002",
        )
        self.assertNotEqual(
            second_reception_object["second_received_signal_id"],
            second_reception_object["existing_received_signal_id"],
        )
        self.assertEqual(
            second_reception_object["second_received_signal_id"],
            "bounded_relevance_signal_002",
        )
        self.assertEqual(
            second_reception_object["second_relevance_basis_id"],
            "bounded_relevance_basis_002",
        )
        self.assertEqual(
            second_reception_object["second_relevance_scope_id"],
            "bounded_relevance_scope_002",
        )
        self.assertEqual(
            second_reception_object["second_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_002",
        )
        self.assertEqual(
            second_reception_object["second_reception_envelope_id"],
            "bounded_relevance_reception_envelope_002",
        )
        self.assert_no_created_posture(result)

    def test_critical_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            clean_request, _artifact_path, _artifact = self.write_synthetic_artifact(
                Path(tmp)
            )
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = (
                        resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
                            request
                        )
                    )
                    self.assert_blocked(result, expected_code="NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][key], False)

    def test_representative_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            clean_request, _artifact_path, artifact = self.write_synthetic_artifact(
                tmp_path
            )
            unreadable_path = tmp_path / "missing_successor_candidate_admission_result.json"
            array_path = _write_json(tmp_path / "array_successor_candidate_admission_result.json", [])

            cases: list[tuple[str, Any, str]] = [
                (
                    "explicit block intent",
                    {"local_relevance_medium_second_bounded_relevance_reception_intent": (
                        "BLOCK_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION"
                    )},
                    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_BLOCK_REQUESTED",
                ),
                (
                    "missing request fields",
                    {"__raw_request__": {}},
                    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_QUESTION_UNDECLARED",
                ),
                (
                    "non-mapping request",
                    ["not", "a", "mapping"],
                    "DECLARED_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_REQUEST_MALFORMED",
                ),
                (
                    "unsupported intent",
                    {"local_relevance_medium_second_bounded_relevance_reception_intent": "UNSUPPORTED"},
                    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_INTENT_UNSUPPORTED",
                ),
                (
                    "selected successor candidate admission artifact path missing",
                    {"selected_successor_candidate_admission_artifact": ""},
                    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_PATH_MISSING",
                ),
                (
                    "selected successor candidate admission artifact unreadable",
                    {"selected_successor_candidate_admission_artifact": str(unreadable_path)},
                    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_UNREADABLE",
                ),
                (
                    "selected successor candidate admission artifact JSON array instead of object",
                    {"selected_successor_candidate_admission_artifact": str(array_path)},
                    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_NOT_JSON_OBJECT",
                ),
                (
                    "selected successor candidate admission artifact not recorded",
                    {"artifact": {**artifact, "outcome": "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_NOT_RECORDED"}},
                    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_NOT_RECORDED",
                ),
                (
                    "selected successor candidate admission artifact failed checks present",
                    {"artifact": {**artifact, "local_relevance_medium_successor_candidate_admission_metadata": {
                        **artifact["local_relevance_medium_successor_candidate_admission_metadata"],
                        "failed_check_count": 1,
                    }}},
                    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
                ),
                (
                    "selected successor candidate admission artifact version not 0.1.0",
                    {"artifact": {**artifact, "local_relevance_medium_successor_candidate_admission_metadata": {
                        **artifact["local_relevance_medium_successor_candidate_admission_metadata"],
                        "local_relevance_medium_successor_candidate_admission_version": "9.9.9",
                    }}},
                    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_VERSION_NOT_0_1_0",
                ),
                ("successor candidate admission object missing", {"artifact": {key: value for key, value in artifact.items() if key != "successor_candidate_admission_object"}}, "SUCCESSOR_CANDIDATE_ADMISSION_OBJECT_MISSING"),
                ("admission type not successor candidate admission", {"artifact": _set_admission_object_field(artifact, "admission_type", "WRONG_TYPE")}, "ADMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION"),
                ("admission scope not one candidate only", {"artifact": _set_admission_object_field(artifact, "admission_scope", "WRONG_SCOPE")}, "ADMISSION_SCOPE_NOT_ONE_CANDIDATE_ONLY"),
                ("successor candidate id missing", {"artifact": _set_admission_object_field(artifact, "successor_candidate_id", "")}, "SUCCESSOR_CANDIDATE_ID_MISSING"),
                ("successor candidate id equals existing signal", {"artifact": _set_admission_object_field(artifact, "successor_candidate_id", "bounded_relevance_signal_001")}, "SUCCESSOR_CANDIDATE_ID_EQUALS_EXISTING_SIGNAL"),
                ("successor candidate scope not bounded only", {"artifact": _set_admission_object_field(artifact, "successor_candidate_scope", "UNSUPPORTED_SCOPE")}, "SUCCESSOR_CANDIDATE_SCOPE_NOT_BOUNDED_ONLY"),
                ("candidate admission status not candidate only", {"artifact": _set_admission_object_field(artifact, "candidate_admission_status", "UNSUPPORTED_STATUS")}, "CANDIDATE_ADMISSION_STATUS_NOT_CANDIDATE_ONLY"),
                ("future second reception scope not bounded only", {"artifact": _set_admission_object_field(artifact, "future_second_reception_scope", "UNSUPPORTED_SCOPE")}, "FUTURE_SECOND_RECEPTION_SCOPE_NOT_BOUNDED_ONLY"),
                ("multiplicity purpose not local only", {"multiplicity_purpose": "UNSUPPORTED_PURPOSE"}, "MULTIPLICITY_PURPOSE_NOT_LOCAL_ONLY"),
                ("max local orientation objects after future reception not two", {"artifact": _set_admission_object_field(artifact, "max_local_orientation_objects_after_future_reception", 3)}, "MAX_LOCAL_ORIENTATION_OBJECTS_AFTER_FUTURE_RECEPTION_NOT_TWO"),
                ("second reception scope missing", {"second_reception_scope": ""}, "SECOND_RECEPTION_SCOPE_MISSING"),
                ("second reception scope not second only", {"second_reception_scope": "UNSUPPORTED_SCOPE"}, "SECOND_RECEPTION_SCOPE_NOT_SECOND_ONLY"),
                ("second reception type missing", {"second_reception_type": ""}, "SECOND_RECEPTION_TYPE_MISSING"),
                ("second reception type wrong", {"second_reception_type": "UNSUPPORTED_TYPE"}, "SECOND_RECEPTION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION"),
                ("admitted successor candidate id missing", {"admitted_successor_candidate_id": ""}, "ADMITTED_SUCCESSOR_CANDIDATE_ID_MISSING"),
                ("admitted successor candidate id differs", {"admitted_successor_candidate_id": "bounded_relevance_signal_candidate_999"}, "ADMITTED_SUCCESSOR_CANDIDATE_ID_DIFFERS_FROM_SUCCESSOR_CANDIDATE_ID"),
                ("second received signal id missing", {"second_received_signal_id": ""}, "SECOND_RECEIVED_SIGNAL_ID_MISSING"),
                ("second received signal id equals existing signal", {"second_received_signal_id": "bounded_relevance_signal_001"}, "SECOND_RECEIVED_SIGNAL_ID_EQUALS_EXISTING_SIGNAL"),
                ("second relevance basis id missing", {"second_relevance_basis_id": ""}, "SECOND_RELEVANCE_BASIS_ID_MISSING"),
                ("second relevance scope id missing", {"second_relevance_scope_id": ""}, "SECOND_RELEVANCE_SCOPE_ID_MISSING"),
                ("second carrier context id missing", {"second_carrier_context_id": ""}, "SECOND_CARRIER_CONTEXT_ID_MISSING"),
                ("second reception envelope id missing", {"second_reception_envelope_id": ""}, "SECOND_RECEPTION_ENVELOPE_ID_MISSING"),
                ("second bounded relevance reception not recorded", {"second_bounded_relevance_reception_not_recorded": True}, "SECOND_BOUNDED_RELEVANCE_RECEPTION_NOT_RECORDED"),
                ("repeated reception permission created", {"repeated_reception_permission_created": True}, "REPEATED_RECEPTION_PERMISSION_CREATED"),
                ("arbitrary reception created", {"arbitrary_reception_created": True}, "ARBITRARY_RECEPTION_CREATED"),
                ("feed created", {"feed_created": True}, "FEED_CREATED"),
                ("second receipt created", {"second_receipt_created": True}, "SECOND_RECEIPT_CREATED"),
                ("second orientation view created", {"second_orientation_view_created": True}, "SECOND_ORIENTATION_VIEW_CREATED"),
                ("second index entry created", {"second_index_entry_created": True}, "SECOND_INDEX_ENTRY_CREATED"),
                ("local medium multiplicity result created", {"local_medium_multiplicity_result_created": True}, "LOCAL_MEDIUM_MULTIPLICITY_RESULT_CREATED"),
                ("relation view created", {"relation_view_created": True}, "RELATION_VIEW_CREATED"),
                ("comparison view created", {"comparison_view_created": True}, "COMPARISON_VIEW_CREATED"),
                ("index system created", {"index_system_created": True}, "INDEX_SYSTEM_CREATED"),
                ("registry created", {"registry_created": True}, "REGISTRY_CREATED"),
                ("search surface created", {"search_surface_created": True}, "SEARCH_SURFACE_CREATED"),
                ("ranking surface created", {"ranking_surface_created": True}, "RANKING_SURFACE_CREATED"),
                ("source transfer occurred", {"source_transfer_occurred": True}, "SOURCE_TRANSFER_OCCURRED"),
                ("source receipt occurred", {"source_receipt_occurred": True}, "SOURCE_RECEIPT_OCCURRED"),
                ("source created", {"source_created": True}, "SOURCE_CREATED"),
                ("authority created", {"authority_created": True}, "AUTHORITY_CREATED"),
                ("currentness created", {"currentness_created": True}, "CURRENTNESS_CREATED"),
                ("truth created", {"truth_created": True}, "TRUTH_CREATED"),
                ("action created", {"action_created": True}, "ACTION_CREATED"),
                ("synchronization created", {"synchronization_created": True}, "SYNCHRONIZATION_CREATED"),
                ("participation authorized", {"participation_authorized": True}, "PARTICIPATION_AUTHORIZED"),
                ("participant role created", {"participant_role_created": True}, "PARTICIPANT_ROLE_CREATED"),
                ("runtime permission created", {"runtime_permission_created": True}, "RUNTIME_PERMISSION_CREATED"),
                ("public API created", {"public_api_created": True}, "PUBLIC_API_CREATED"),
                ("participant-facing interface created", {"participant_facing_interface_created": True}, "PARTICIPANT_FACING_INTERFACE_CREATED"),
                ("distributed network behavior created", {"distributed_network_behavior_created": True}, "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
                ("deployment created", {"deployment_created": True}, "DEPLOYMENT_CREATED"),
                ("public release created", {"public_release_created": True}, "PUBLIC_RELEASE_CREATED"),
                ("operation permission created", {"operation_permission_created": True}, "OPERATION_PERMISSION_CREATED"),
                ("broader reusable permission created", {"broader_reusable_permission_created": True}, "BROADER_REUSABLE_PERMISSION_CREATED"),
                ("follow-on work authorized", {"follow_on_work_authorized": True}, "FOLLOW_ON_WORK_AUTHORIZED"),
                ("artifact existence treated as second-reception authority", {"artifact_existence_treated_as_second_reception_authority": True}, "ARTIFACT_EXISTENCE_TREATED_AS_SECOND_RECEPTION_AUTHORITY"),
                ("latest file posture treated as second-reception authority", {"latest_file_posture_treated_as_second_reception_authority": True}, "LATEST_FILE_POSTURE_TREATED_AS_SECOND_RECEPTION_AUTHORITY"),
                ("repo-local availability treated as second-reception authority", {"repo_local_availability_treated_as_second_reception_authority": True}, "REPO_LOCAL_AVAILABILITY_TREATED_AS_SECOND_RECEPTION_AUTHORITY"),
                ("hidden repo state used as second-reception content", {"hidden_repo_state_used_as_second_reception_content": True}, "HIDDEN_REPO_STATE_USED_AS_SECOND_RECEPTION_CONTENT"),
                ("hidden repo state used as second-reception authority", {"hidden_repo_state_used_as_second_reception_authority": True}, "HIDDEN_REPO_STATE_USED_AS_SECOND_RECEPTION_AUTHORITY"),
                ("predecessor failure repaired", {"predecessor_failure_repaired": True}, "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
                ("predecessor failure hidden", {"predecessor_failure_hidden": True}, "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
                ("predecessor failure claimed passed", {"predecessor_failure_claimed_passed": True}, "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
                ("consumed request reopened", {"consumed_request_reopened": True}, "CONSUMED_REQUEST_REOPENED"),
                ("authorization token reused", {"authorization_token_reused": True}, "AUTHORIZATION_TOKEN_REUSED"),
                ("required non-claim missing", {"remove_non_claim": "authority_created"}, "NON_CLAIM_MISSING_OR_FLIPPED"),
                ("required non-claim flipped", {"flip_non_claim": "authority_created"}, "NON_CLAIM_MISSING_OR_FLIPPED"),
            ]

            for name, mutation, expected_code in cases:
                with self.subTest(name=name):
                    if isinstance(mutation, list):
                        result = (
                            resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
                                mutation
                            )
                        )
                    else:
                        raw_request = mutation.get("__raw_request__")
                        if raw_request is not None:
                            result = (
                                resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
                                    raw_request
                                )
                            )
                            self.assert_blocked(result, expected_code=expected_code)
                            continue
                        request = copy.deepcopy(clean_request)
                        artifact_for_case = mutation.get("artifact")
                        if artifact_for_case is not None:
                            artifact_path = _write_json(
                                tmp_path / f"{name.replace(' ', '_')}.json",
                                artifact_for_case,
                            )
                            request["selected_successor_candidate_admission_artifact"] = str(
                                artifact_path
                            )
                        remove_non_claim = mutation.get("remove_non_claim")
                        flip_non_claim = mutation.get("flip_non_claim")
                        for key, value in mutation.items():
                            if key not in {"artifact", "remove_non_claim", "flip_non_claim"}:
                                request[key] = value
                        if remove_non_claim is not None:
                            request["declared_non_claims"].pop(remove_non_claim)
                        if flip_non_claim is not None:
                            request["declared_non_claims"][flip_non_claim] = True
                        result = (
                            resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
                                request
                            )
                        )
                    self.assert_blocked(result, expected_code=expected_code)

    def test_missing_or_incomplete_declared_non_claims_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            clean_request, _artifact_path, _artifact = self.write_synthetic_artifact(
                Path(tmp)
            )
            variants = []
            missing_mapping = copy.deepcopy(clean_request)
            missing_mapping.pop("declared_non_claims")
            variants.append(missing_mapping)

            empty_mapping = copy.deepcopy(clean_request)
            empty_mapping["declared_non_claims"] = {}
            variants.append(empty_mapping)

            missing_one = copy.deepcopy(clean_request)
            missing_one["declared_non_claims"].pop("authority_created")
            variants.append(missing_one)

            string_value = copy.deepcopy(clean_request)
            string_value["declared_non_claims"]["authority_created"] = "false"
            variants.append(string_value)

            none_value = copy.deepcopy(clean_request)
            none_value["declared_non_claims"]["authority_created"] = None
            variants.append(none_value)

            for request in variants:
                with self.subTest(variant=request.get("declared_non_claims")):
                    result = (
                        resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
                            request
                        )
                    )
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS},
                    )
                    self.assert_public_block_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            result = (
                resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
                    request
                )
            )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertTrue(
            {
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_BLOCKED,
            }.issubset(set(resolver.OUTCOME_FAMILY))
        )
        self.assert_official_values_preserved(result)

    def test_raw_and_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact = _synthetic_successor_candidate_admission_artifact()
            for key, sentinel in zip(HOSTILE_KEYS, HOSTILE_SENTINELS * 4):
                artifact[key] = sentinel
            request, _artifact_path, _synthetic = self.write_synthetic_artifact(
                tmp_path,
                artifact=artifact,
                name="hostile_successor_candidate_admission",
            )
            original_request = copy.deepcopy(request)
            request["raw_second_reception_body"] = HOSTILE_SENTINELS[0]
            request["hidden_repo_state"] = {"payload": HOSTILE_SENTINELS[-1]}

            result = (
                resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
                    request
                )
            )

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_hostile_sentinels(result)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION", serialized)
        self.assertIn("SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY", serialized)
        self.assertIn("BOUNDED_RELEVANCE_RECEPTION_CANDIDATE_ONLY", serialized)
        self.assertIn("ADMITTED_AS_SUCCESSOR_RECEPTION_CANDIDATE_ONLY", serialized)
        self.assertIn("LOCAL_MEDIUM_MULTIPLICITY_TEST_ONLY", serialized)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_created_posture(result)
        self.assertEqual(original_request["declared_non_claims"], request["declared_non_claims"])

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request, _artifact_path, _artifact = self.write_synthetic_artifact(tmp_path)
            request_path = _write_json(tmp_path / "second_reception_request.json", request)

            result = (
                resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min_from_path(
                    request_path
                )
            )
            summary = (
                resolver.build_local_relevance_medium_second_bounded_relevance_reception_v0_min_summary(
                    result
                )
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min",
            )
            self.assert_not_blocked(result)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{bad", encoding="utf-8")
            with self.assertRaises(
                resolver.LocalRelevanceMediumSecondBoundedRelevanceReceptionV0MinError
            ):
                resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min_from_path(
                    malformed_path
                )

            array_request_path = _write_json(tmp_path / "array_request.json", [])
            array_result = (
                resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min_from_path(
                    array_request_path
                )
            )
            self.assert_blocked(
                array_result,
                expected_code=(
                    "DECLARED_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_REQUEST_MALFORMED"
                ),
            )

            with self.assertRaises(
                resolver.LocalRelevanceMediumSecondBoundedRelevanceReceptionV0MinError
            ):
                resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min_from_path(
                    tmp_path / "missing_request.json"
                )

            patched_root = (
                tmp_path
                / "artifacts/"
                "integrity_host_v0_min_coexistence_"
                "local_relevance_medium_second_bounded_relevance_reception_v0_min"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_root):
                first_path = (
                    resolver.write_local_relevance_medium_second_bounded_relevance_reception_v0_min_result(
                        result
                    )
                )
                second_path = (
                    resolver.write_local_relevance_medium_second_bounded_relevance_reception_v0_min_result(
                        result
                    )
                )

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIsInstance(json.loads(first_path.read_text(encoding="utf-8")), dict)
            self.assertIsInstance(json.loads(second_path.read_text(encoding="utf-8")), dict)
            self.assertIn(
                "local_relevance_medium_second_bounded_relevance_reception_v0_min",
                str(first_path),
            )
            forbidden_parts = {
                "local_relevance_medium_successor_candidate_admission_v0_min",
                "local_relevance_medium_successor_reception_request_v0_min",
                "local_relevance_orientation_index_entry_v0_min",
                "relevance_orientation_view_v0_min",
                "bounded_relevance_receipt_v0_min_v2",
                "bounded_relevance_reception_v0_min",
                "post_runtime_daemon_runtime_loop",
                "source-transfer",
                "source-receipt",
                "public-api",
                "participant-facing-interface",
                "distributed-network",
            }
            self.assertFalse(forbidden_parts.intersection(first_path.parts))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact = _synthetic_successor_candidate_admission_artifact()
            artifact["raw_body"] = HOSTILE_SENTINELS[0]
            artifact_before = copy.deepcopy(artifact)
            request, _artifact_path, _artifact = self.write_synthetic_artifact(
                tmp_path,
                artifact=artifact,
            )
            request["nested_payload"] = {"hidden_repo_state": HOSTILE_SENTINELS[-1]}
            request_before = copy.deepcopy(request)
            declared_non_claims_before = copy.deepcopy(request["declared_non_claims"])

            resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
                request
            )

        self.assertEqual(request, request_before)
        self.assertEqual(request["declared_non_claims"], declared_non_claims_before)
        self.assertEqual(artifact, artifact_before)
        self.assertEqual(
            request["second_reception_scope"],
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY",
        )
        self.assertEqual(
            request["second_reception_type"],
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION",
        )
        self.assertEqual(request["second_received_signal_id"], "bounded_relevance_signal_002")
        self.assertEqual(request["second_relevance_basis_id"], "bounded_relevance_basis_002")
        self.assertEqual(request["second_relevance_scope_id"], "bounded_relevance_scope_002")
        self.assertEqual(
            request["second_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_002",
        )
        self.assertEqual(
            request["second_reception_envelope_id"],
            "bounded_relevance_reception_envelope_002",
        )
        self.assertEqual(
            request["multiplicity_purpose"],
            "LOCAL_MEDIUM_MULTIPLICITY_TEST_ONLY",
        )

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            result = (
                resolver.resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
                    request
                )
            )
            summary = (
                resolver.build_local_relevance_medium_second_bounded_relevance_reception_v0_min_summary(
                    result
                )
            )

        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
