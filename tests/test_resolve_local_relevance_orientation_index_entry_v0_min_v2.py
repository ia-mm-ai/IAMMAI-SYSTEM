"""V2 executable tests for the local relevance orientation index entry resolver.

This suite preserves the substantive v1 test intent while correcting one
over-strict clean-result assertion. V1 remains predecessor failed test evidence:
it required ``result["block"] is None`` for a clean recorded result, while the
resolver lawfully emits either ``None`` or an explicit unblocked block object.

These tests remain bounded to one local locator object. They do not create an
index system, registry, search surface, ranking surface, boundary, source
transfer, source receipt, reception authorization, authority, currentness,
truth, action, synchronization, participation authorization, participant role,
runtime permission, public API, participant-facing interface, distributed
network behavior, deployment, public release, operation permission, broader
permission, adoption, receiving-context governance, publication flow, or
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

import resolve_local_relevance_orientation_index_entry_v0_min as resolver  # noqa: E402


V1_TEST_PATH = REPO_ROOT / "tests/test_resolve_local_relevance_orientation_index_entry_v0_min.py"
DEFAULT_ORIENTATION_ARTIFACT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min/"
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

TOP_LEVEL_SECTIONS = {
    "local_relevance_orientation_index_entry_metadata",
    "declared_local_relevance_orientation_index_entry_question",
    "selected_relevance_orientation_view_artifact_basis",
    "index_entry",
    "local_relevance_orientation_index_entry_checks",
    "local_relevance_orientation_index_entry_statement",
    "local_relevance_orientation_index_entry_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "local_relevance_orientation_index_entry_summary",
}

INDEX_ENTRY_FIELDS = {
    "index_entry_id",
    "index_entry_type",
    "index_entry_version",
    "index_entry_scope",
    "orientation_view_artifact",
    "orientation_view_outcome",
    "orientation_view_result_version",
    "orientation_view_failed_check_count",
    "orientation_scope",
    "source_receipt_artifact",
    "referenced_reception_artifact",
    "received_signal_id",
    "received_relevance_basis_id",
    "received_relevance_scope_id",
    "received_carrier_context_id",
    "received_reception_envelope_id",
    "local_discoverability",
    "does_not_create_index_system",
    "does_not_create_registry",
    "does_not_create_search",
    "does_not_create_ranking",
    "authority_created",
    "currentness_created",
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

WRAPPER_KEYS_FORBIDDEN_IN_INDEX_ENTRY = {
    "outcome",
    "block",
    "local_relevance_orientation_index_entry_checks",
    "non_claims",
    "local_relevance_orientation_index_entry_summary",
    "local_relevance_orientation_index_entry_metadata",
}

EXPECTED_BLOCK_CODES = {
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_BLOCK_REQUESTED",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_PATH_MISSING",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_UNREADABLE",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_NOT_JSON_OBJECT",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_NOT_RECORDED",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_FAILED_CHECKS_PRESENT",
    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_VERSION_NOT_0_1_0",
    "ORIENTATION_VIEW_MISSING",
    "ORIENTATION_SCOPE_NOT_LOCAL_ONLY",
    "ORIENTATION_VIEW_SOURCE_RECEIPT_ARTIFACT_MISSING",
    "ORIENTATION_VIEW_REFERENCED_RECEPTION_ARTIFACT_MISSING",
    "RECEIVED_SIGNAL_ID_MISSING",
    "RECEIVED_RELEVANCE_BASIS_ID_MISSING",
    "RECEIVED_RELEVANCE_SCOPE_ID_MISSING",
    "RECEIVED_CARRIER_CONTEXT_ID_MISSING",
    "RECEIVED_RECEPTION_ENVELOPE_ID_MISSING",
    "INDEX_ENTRY_SCOPE_MISSING",
    "INDEX_ENTRY_SCOPE_NOT_LOCAL_ONLY",
    "INDEX_ENTRY_TYPE_MISSING",
    "INDEX_ENTRY_TYPE_NOT_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
    "INDEX_ENTRY_CREATED_INDEX_SYSTEM",
    "INDEX_ENTRY_CREATED_REGISTRY",
    "INDEX_ENTRY_CREATED_SEARCH",
    "INDEX_ENTRY_CREATED_RANKING",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "TRUTH_CREATED",
    "ACTION_CREATED",
    "SYNCHRONIZATION_CREATED",
    "PARTICIPATION_AUTHORIZED",
    "PARTICIPANT_ROLE_CREATED",
    "RUNTIME_PERMISSION_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_INDEX_ENTRY_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_INDEX_ENTRY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_INDEX_ENTRY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_INDEX_ENTRY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_INDEX_ENTRY_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_REQUEST_UNREADABLE",
}

NO_CREATION_NON_CLAIMS = {
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
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
    "raw_index_entry_body",
    "raw_local_relevance_orientation_index_entry_body",
    "raw_orientation_body",
    "raw_relevance_orientation_view_body",
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
    "index_entry_body",
    "local_relevance_orientation_index_entry_body",
    "orientation_body",
    "relevance_orientation_view_body",
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
    "RAW_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_RELEVANCE_ORIENTATION_VIEW_BODY_MUST_NOT_RETURN",
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


def _synthetic_orientation_artifact() -> dict[str, Any]:
    return {
        "outcome": "RELEVANCE_ORIENTATION_VIEW_RECORDED",
        "relevance_orientation_view_metadata": {
            "relevance_orientation_view_id": "relevance_orientation_view_reference_review_001",
            "relevance_orientation_view_type": "relevance_orientation_view_result",
            "relevance_orientation_view_version": "0.1.0",
            "failed_check_count": 0,
            "resolver_module": "resolve_relevance_orientation_view_v0_min",
        },
        "orientation_view": {
            "orientation_view_id": "relevance_orientation_view_001",
            "orientation_view_type": "relevance_orientation_view",
            "orientation_view_version": "0.1.0",
            "orientation_scope": "LOCAL_ORIENTATION_ONLY",
            "source_receipt_artifact": SOURCE_RECEIPT_ARTIFACT,
            "referenced_reception_artifact": REFERENCED_RECEPTION_ARTIFACT,
            "receipt_outcome": "BOUNDED_RELEVANCE_RECEIPT_RECORDED",
            "receipt_result_version": "0.2.0",
            "receipt_failed_check_count": 0,
            "receipt_scope": "INSPECTABLE_RECEIPT_ONLY",
            "receipt_does_not_expand_reception": True,
            "received_signal_id": "bounded_relevance_signal_001",
            "received_relevance_basis_id": "bounded_relevance_basis_001",
            "received_relevance_scope_id": "bounded_relevance_scope_001",
            "received_carrier_context_id": "bounded_relevance_signal_carrier_context_001",
            "received_reception_envelope_id": "bounded_relevance_reception_envelope_001",
        },
        "relevance_orientation_view_summary": {
            "outcome": "RELEVANCE_ORIENTATION_VIEW_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "resolver_module": "resolve_relevance_orientation_view_v0_min",
        },
    }


def _clean_request(orientation_artifact_path: Path) -> dict[str, Any]:
    return resolver.build_declared_local_relevance_orientation_index_entry_v0_min_request(
        selected_relevance_orientation_view_artifact=orientation_artifact_path,
    )


def _block_code(result: dict[str, Any]) -> str | None:
    block = result.get("block")
    if not isinstance(block, dict):
        return None
    return block.get("code") or block.get("block_code")


def _failed_checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        check
        for check in result.get("local_relevance_orientation_index_entry_checks", [])
        if isinstance(check, dict) and check.get("passed") is not True
    ]


def _mutate_orientation_view(
    artifact: dict[str, Any], field: str, value: Any = None
) -> dict[str, Any]:
    updated = copy.deepcopy(artifact)
    updated["orientation_view"][field] = value
    return updated


class LocalRelevanceOrientationIndexEntryV2Tests(unittest.TestCase):
    def write_synthetic_artifact(
        self, tmp_path: Path, artifact: dict[str, Any] | None = None, name: str = "orientation"
    ) -> tuple[dict[str, Any], Path, dict[str, Any]]:
        synthetic = copy.deepcopy(artifact or _synthetic_orientation_artifact())
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
        for check in result.get("local_relevance_orientation_index_entry_checks", []):
            if not isinstance(check, dict):
                continue
            for key in ("block_code", "failure_code"):
                value = check.get(key)
                if value is not None:
                    self.assertIn(value, resolver.BLOCK_CODES)

    def assert_blocked(self, result: dict[str, Any], expected_code: str | None = None) -> None:
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
        self.assert_index_entry_is_small(result)

    def assert_non_claims_canonical_false(self, result: dict[str, Any]) -> None:
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False)
            self.assertIsInstance(result["non_claims"][key], bool)

    def assert_index_entry_is_small(self, result: dict[str, Any]) -> None:
        index_entry = result.get("index_entry")
        if index_entry is None:
            return
        self.assertIsInstance(index_entry, dict)
        self.assertLessEqual(set(index_entry), INDEX_ENTRY_FIELDS)
        for key in WRAPPER_KEYS_FORBIDDEN_IN_INDEX_ENTRY:
            self.assertNotIn(key, index_entry)
        self.assertNotEqual(index_entry.get("index_entry_type"), "RELEVANCE_INDEX")
        self.assertNotEqual(index_entry.get("index_entry_type"), "LOCAL_RELEVANCE_INDEX")

    def assert_no_created_posture(self, result: dict[str, Any]) -> None:
        for key in NO_CREATION_NON_CLAIMS:
            self.assertIs(result["non_claims"][key], False)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        index_entry = result.get("index_entry")
        if isinstance(index_entry, dict) and index_entry:
            for key in (
                "authority_created",
                "currentness_created",
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
                self.assertIs(index_entry[key], False)
            self.assertIs(index_entry["does_not_create_index_system"], True)
            self.assertIs(index_entry["does_not_create_registry"], True)
            self.assertIs(index_entry["does_not_create_search"], True)
            self.assertIs(index_entry["does_not_create_ranking"], True)

    def assert_official_values_preserved(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY", serialized)
        self.assertIn("LOCAL_INDEX_ENTRY_ONLY", serialized)
        self.assertIn("LOCAL_ORIENTATION_ONLY", serialized)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertNotIn("__REDACTED__", serialized)

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
            "resolve_local_relevance_orientation_index_entry_v0_min",
            "resolve_local_relevance_orientation_index_entry_v0_min_from_path",
            "write_local_relevance_orientation_index_entry_v0_min_result",
            "build_local_relevance_orientation_index_entry_v0_min_summary",
            "build_declared_local_relevance_orientation_index_entry_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_INDEX_ENTRY_SCOPE_VALUES",
            "SUPPORTED_INDEX_ENTRY_TYPE_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_local_relevance_orientation_index_entry_v0_min",
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min"
            )
        )
        self.assertIn("LOCAL_INDEX_ENTRY_ONLY", resolver.SUPPORTED_INDEX_ENTRY_SCOPE_VALUES)
        self.assertIn(
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
            resolver.SUPPORTED_INDEX_ENTRY_TYPE_VALUES,
        )
        self.assertNotIn("RELEVANCE_INDEX", resolver.SUPPORTED_INDEX_ENTRY_TYPE_VALUES)
        self.assertNotIn("LOCAL_RELEVANCE_INDEX", resolver.SUPPORTED_INDEX_ENTRY_TYPE_VALUES)
        self.assertTrue(EXPECTED_BLOCK_CODES.issubset(set(resolver.BLOCK_CODES)))

        output_root = str(resolver.OUTPUT_ROOT)
        for forbidden in (
            "relevance_orientation_view_v0_min",
            "bounded_relevance_receipt_v0_min_v2",
            "bounded_relevance_receipt_v0_min",
            "bounded_relevance_reception_v0_min",
            "post_runtime_loop_internal_runtime_layer_closure",
            "post_runtime_daemon_runtime_loop",
            "source-transfer",
            "source-receipt",
            "reception/",
            "public-api",
            "participant-facing-interface",
            "distributed-network",
            "deployment",
            "public-release",
        ):
            self.assertNotIn(forbidden, output_root)

    def test_successful_recorded_result_from_synthetic_orientation_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(request)
            summary = resolver.build_local_relevance_orientation_index_entry_v0_min_summary(result)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"], "resolve_local_relevance_orientation_index_entry_v0_min"
        )
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(set(result)))

        index_entry = result["index_entry"]
        self.assertEqual(index_entry["index_entry_id"], "local_relevance_orientation_index_entry_001")
        self.assertEqual(index_entry["index_entry_type"], "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY")
        self.assertNotEqual(index_entry["index_entry_type"], "RELEVANCE_INDEX")
        self.assertNotEqual(index_entry["index_entry_type"], "LOCAL_RELEVANCE_INDEX")
        self.assertEqual(index_entry["index_entry_version"], "0.1.0")
        self.assertEqual(index_entry["index_entry_scope"], "LOCAL_INDEX_ENTRY_ONLY")
        self.assertEqual(index_entry["orientation_view_artifact"], str(artifact_path))
        self.assertEqual(index_entry["orientation_view_outcome"], "RELEVANCE_ORIENTATION_VIEW_RECORDED")
        self.assertEqual(index_entry["orientation_view_result_version"], "0.1.0")
        self.assertEqual(index_entry["orientation_view_failed_check_count"], 0)
        self.assertEqual(index_entry["orientation_scope"], "LOCAL_ORIENTATION_ONLY")
        self.assertEqual(index_entry["source_receipt_artifact"], SOURCE_RECEIPT_ARTIFACT)
        self.assertEqual(index_entry["referenced_reception_artifact"], REFERENCED_RECEPTION_ARTIFACT)
        self.assertEqual(index_entry["received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(index_entry["received_relevance_basis_id"], "bounded_relevance_basis_001")
        self.assertEqual(index_entry["received_relevance_scope_id"], "bounded_relevance_scope_001")
        self.assertEqual(
            index_entry["received_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_001",
        )
        self.assertEqual(
            index_entry["received_reception_envelope_id"],
            "bounded_relevance_reception_envelope_001",
        )
        self.assertIs(index_entry["local_discoverability"], True)
        self.assert_no_created_posture(result)
        self.assert_index_entry_is_small(result)

        statement = result["local_relevance_orientation_index_entry_statement"]
        for key in (
            "local_relevance_orientation_index_entry_recorded",
            "orientation_view_artifact_preserved",
            "source_receipt_artifact_preserved",
            "referenced_reception_artifact_preserved",
            "received_signal_id_preserved",
            "received_relevance_basis_id_preserved",
            "received_relevance_scope_id_preserved",
            "received_carrier_context_id_preserved",
            "received_reception_envelope_id_preserved",
            "index_entry_scope_local_only",
            "local_discoverability_preserved",
            "index_entry_does_not_create_index_system",
            "index_entry_does_not_create_registry",
            "index_entry_does_not_create_search",
            "index_entry_does_not_create_ranking",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(statement[key], True)
        self.assert_non_claims_canonical_false(result)
        self.assert_public_block_codes(result)
        self.assert_official_values_preserved(result)
        self.assert_generated_booleans_are_bool(result)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        if not DEFAULT_ORIENTATION_ARTIFACT.exists():
            self.skipTest("default relevance orientation view artifact is not present")

        request = resolver.build_declared_local_relevance_orientation_index_entry_v0_min_request()
        result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(request)
        summary = resolver.build_local_relevance_orientation_index_entry_v0_min_summary(result)
        index_entry = result["index_entry"]

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(index_entry["index_entry_type"], "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY")
        self.assertEqual(index_entry["index_entry_scope"], "LOCAL_INDEX_ENTRY_ONLY")
        self.assertEqual(index_entry["orientation_scope"], "LOCAL_ORIENTATION_ONLY")
        self.assertEqual(
            index_entry["received_reception_envelope_id"],
            "bounded_relevance_reception_envelope_001",
        )
        self.assert_no_created_posture(result)

    def test_critical_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            clean_request, _artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(request)
                    self.assert_blocked(result, expected_code="NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][key], False)

    def test_representative_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            clean_request, _artifact_path, artifact = self.write_synthetic_artifact(tmp_path)
            unreadable_path = tmp_path / "missing_orientation_result.json"
            array_path = _write_json(tmp_path / "array_orientation_result.json", [])

            cases: list[tuple[str, Any, str]] = [
                (
                    "explicit block intent",
                    lambda: self._request_with(
                        clean_request,
                        local_relevance_orientation_index_entry_intent=(
                            "BLOCK_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY"
                        ),
                    ),
                    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_BLOCK_REQUESTED",
                ),
                ("missing request mapping", lambda: {}, "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_QUESTION_UNDECLARED"),
                (
                    "non-mapping request",
                    lambda: ["not", "a", "mapping"],
                    "DECLARED_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_REQUEST_MALFORMED",
                ),
                (
                    "unsupported intent",
                    lambda: self._request_with(
                        clean_request,
                        local_relevance_orientation_index_entry_intent="UNSUPPORTED",
                    ),
                    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_INTENT_UNSUPPORTED",
                ),
                (
                    "artifact path missing",
                    lambda: self._request_with(clean_request, selected_relevance_orientation_view_artifact=""),
                    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_PATH_MISSING",
                ),
                (
                    "artifact unreadable",
                    lambda: self._request_with(
                        clean_request,
                        selected_relevance_orientation_view_artifact=str(unreadable_path),
                    ),
                    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_UNREADABLE",
                ),
                (
                    "artifact not JSON object",
                    lambda: self._request_with(
                        clean_request,
                        selected_relevance_orientation_view_artifact=str(array_path),
                    ),
                    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_NOT_JSON_OBJECT",
                ),
                (
                    "artifact not recorded",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        artifact,
                        "not_recorded",
                        top_updates={"outcome": "RELEVANCE_ORIENTATION_VIEW_NOT_RECORDED"},
                        summary_updates={"outcome": "RELEVANCE_ORIENTATION_VIEW_NOT_RECORDED"},
                    ),
                    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_NOT_RECORDED",
                ),
                (
                    "artifact failed checks present",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        artifact,
                        "failed_checks",
                        metadata_updates={"failed_check_count": 1},
                        summary_updates={"failed_check_count": 1},
                    ),
                    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_FAILED_CHECKS_PRESENT",
                ),
                (
                    "artifact version not 0.1.0",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        artifact,
                        "wrong_version",
                        metadata_updates={"relevance_orientation_view_version": "0.2.0"},
                        summary_updates={"result_version": "0.2.0"},
                    ),
                    "RELEVANCE_ORIENTATION_VIEW_ARTIFACT_VERSION_NOT_0_1_0",
                ),
                (
                    "orientation view missing",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        artifact,
                        "orientation_missing",
                        top_updates={"orientation_view": None},
                    ),
                    "ORIENTATION_VIEW_MISSING",
                ),
                (
                    "orientation scope not local",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        _mutate_orientation_view(artifact, "orientation_scope", "NOT_LOCAL"),
                        "scope_not_local",
                    ),
                    "ORIENTATION_SCOPE_NOT_LOCAL_ONLY",
                ),
                (
                    "source receipt missing",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        _mutate_orientation_view(artifact, "source_receipt_artifact", ""),
                        "source_receipt_missing",
                    ),
                    "ORIENTATION_VIEW_SOURCE_RECEIPT_ARTIFACT_MISSING",
                ),
                (
                    "referenced reception missing",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        _mutate_orientation_view(artifact, "referenced_reception_artifact", ""),
                        "referenced_reception_missing",
                    ),
                    "ORIENTATION_VIEW_REFERENCED_RECEPTION_ARTIFACT_MISSING",
                ),
                (
                    "received signal id missing",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        _mutate_orientation_view(artifact, "received_signal_id", ""),
                        "signal_missing",
                    ),
                    "RECEIVED_SIGNAL_ID_MISSING",
                ),
                (
                    "received relevance basis id missing",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        _mutate_orientation_view(artifact, "received_relevance_basis_id", ""),
                        "basis_missing",
                    ),
                    "RECEIVED_RELEVANCE_BASIS_ID_MISSING",
                ),
                (
                    "received relevance scope id missing",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        _mutate_orientation_view(artifact, "received_relevance_scope_id", ""),
                        "scope_missing",
                    ),
                    "RECEIVED_RELEVANCE_SCOPE_ID_MISSING",
                ),
                (
                    "received carrier context id missing",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        _mutate_orientation_view(artifact, "received_carrier_context_id", ""),
                        "carrier_missing",
                    ),
                    "RECEIVED_CARRIER_CONTEXT_ID_MISSING",
                ),
                (
                    "received reception envelope id missing",
                    lambda: self._request_for_artifact(
                        tmp_path,
                        _mutate_orientation_view(artifact, "received_reception_envelope_id", ""),
                        "envelope_missing",
                    ),
                    "RECEIVED_RECEPTION_ENVELOPE_ID_MISSING",
                ),
                (
                    "index entry scope missing",
                    lambda: self._request_without(clean_request, "index_entry_scope"),
                    "INDEX_ENTRY_SCOPE_MISSING",
                ),
                (
                    "index entry scope not local",
                    lambda: self._request_with(clean_request, index_entry_scope="GLOBAL_INDEX"),
                    "INDEX_ENTRY_SCOPE_NOT_LOCAL_ONLY",
                ),
                (
                    "index entry type missing",
                    lambda: self._request_without(clean_request, "index_entry_type"),
                    "INDEX_ENTRY_TYPE_MISSING",
                ),
                (
                    "index entry type not exact",
                    lambda: self._request_with(clean_request, index_entry_type="OTHER"),
                    "INDEX_ENTRY_TYPE_NOT_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
                ),
                (
                    "index entry type attempted as RELEVANCE_INDEX",
                    lambda: self._request_with(clean_request, index_entry_type="RELEVANCE_INDEX"),
                    "INDEX_ENTRY_TYPE_NOT_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
                ),
                (
                    "index entry type attempted as LOCAL_RELEVANCE_INDEX",
                    lambda: self._request_with(clean_request, index_entry_type="LOCAL_RELEVANCE_INDEX"),
                    "INDEX_ENTRY_TYPE_NOT_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
                ),
            ]

            flag_codes = {
                "index_entry_creates_index_system": "INDEX_ENTRY_CREATED_INDEX_SYSTEM",
                "index_entry_creates_registry": "INDEX_ENTRY_CREATED_REGISTRY",
                "index_entry_creates_search": "INDEX_ENTRY_CREATED_SEARCH",
                "index_entry_creates_ranking": "INDEX_ENTRY_CREATED_RANKING",
                "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
                "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
                "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
                "source_created": "SOURCE_CREATED",
                "authority_created": "AUTHORITY_CREATED",
                "currentness_created": "CURRENTNESS_CREATED",
                "truth_created": "TRUTH_CREATED",
                "action_created": "ACTION_CREATED",
                "synchronization_created": "SYNCHRONIZATION_CREATED",
                "participation_authorized": "PARTICIPATION_AUTHORIZED",
                "participant_role_created": "PARTICIPANT_ROLE_CREATED",
                "runtime_permission_created": "RUNTIME_PERMISSION_CREATED",
                "public_api_created": "PUBLIC_API_CREATED",
                "participant_facing_interface_created": "PARTICIPANT_FACING_INTERFACE_CREATED",
                "distributed_network_behavior_created": "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
                "deployment_created": "DEPLOYMENT_CREATED",
                "public_release_created": "PUBLIC_RELEASE_CREATED",
                "operation_permission_created": "OPERATION_PERMISSION_CREATED",
                "broader_reusable_permission_created": "BROADER_REUSABLE_PERMISSION_CREATED",
                "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
                "artifact_existence_treated_as_index_entry_authority": (
                    "ARTIFACT_EXISTENCE_TREATED_AS_INDEX_ENTRY_AUTHORITY"
                ),
                "latest_file_posture_treated_as_index_entry_authority": (
                    "LATEST_FILE_POSTURE_TREATED_AS_INDEX_ENTRY_AUTHORITY"
                ),
                "repo_local_availability_treated_as_index_entry_authority": (
                    "REPO_LOCAL_AVAILABILITY_TREATED_AS_INDEX_ENTRY_AUTHORITY"
                ),
                "hidden_repo_state_used_as_index_entry_content": (
                    "HIDDEN_REPO_STATE_USED_AS_INDEX_ENTRY_CONTENT"
                ),
                "hidden_repo_state_used_as_index_entry_authority": (
                    "HIDDEN_REPO_STATE_USED_AS_INDEX_ENTRY_AUTHORITY"
                ),
                "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
                "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
                "predecessor_failure_claimed_passed": (
                    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
                ),
                "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
                "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
            }
            for flag, code in flag_codes.items():
                cases.append((flag, lambda flag=flag: self._request_with(clean_request, **{flag: True}), code))
            cases.append(
                (
                    "required non-claim missing",
                    lambda: self._request_with_missing_non_claim(
                        clean_request, resolver.REQUIRED_FALSE_NON_CLAIMS[0]
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )
            )

            for name, request_factory, expected_code in cases:
                with self.subTest(case=name):
                    result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(
                        request_factory()
                    )
                    self.assert_blocked(result, expected_code=expected_code)

    def _request_with(self, clean_request: dict[str, Any], **updates: Any) -> dict[str, Any]:
        request = copy.deepcopy(clean_request)
        request.update(updates)
        return request

    def _request_without(self, clean_request: dict[str, Any], key: str) -> dict[str, Any]:
        request = copy.deepcopy(clean_request)
        request.pop(key, None)
        return request

    def _request_with_missing_non_claim(
        self, clean_request: dict[str, Any], key: str
    ) -> dict[str, Any]:
        request = copy.deepcopy(clean_request)
        request["declared_non_claims"].pop(key, None)
        return request

    def _request_for_artifact(
        self,
        tmp_path: Path,
        base_artifact: dict[str, Any],
        name: str,
        *,
        top_updates: dict[str, Any] | None = None,
        metadata_updates: dict[str, Any] | None = None,
        summary_updates: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        artifact = copy.deepcopy(base_artifact)
        if top_updates:
            artifact.update(top_updates)
        if metadata_updates:
            artifact["relevance_orientation_view_metadata"].update(metadata_updates)
        if summary_updates:
            artifact["relevance_orientation_view_summary"].update(summary_updates)
        artifact_path = _write_json(tmp_path / f"{name}.json", artifact)
        return _clean_request(artifact_path)

    def test_missing_or_incomplete_declared_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            clean_request, _artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            variants = [
                self._request_without(clean_request, "declared_non_claims"),
                self._request_with(clean_request, declared_non_claims={}),
                self._request_with_missing_non_claim(
                    clean_request, resolver.REQUIRED_FALSE_NON_CLAIMS[0]
                ),
                self._request_with_non_claim_value(
                    clean_request, resolver.REQUIRED_FALSE_NON_CLAIMS[0], "false"
                ),
                self._request_with_non_claim_value(
                    clean_request, resolver.REQUIRED_FALSE_NON_CLAIMS[0], None
                ),
            ]
            for request in variants:
                with self.subTest(shape=request.get("declared_non_claims", "missing")):
                    result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(request)
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS},
                    )
                    self.assert_public_block_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def _request_with_non_claim_value(
        self, clean_request: dict[str, Any], key: str, value: Any
    ) -> dict[str, Any]:
        request = copy.deepcopy(clean_request)
        request["declared_non_claims"][key] = value
        return request

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(request)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        index_entry = result["index_entry"]
        self.assertEqual(index_entry["index_entry_type"], "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY")
        self.assertEqual(index_entry["index_entry_scope"], "LOCAL_INDEX_ENTRY_ONLY")
        self.assertEqual(index_entry["orientation_scope"], "LOCAL_ORIENTATION_ONLY")
        self.assertTrue(
            {
                "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED",
                "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_NOT_RECORDED",
                "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_REQUIRES_ADDITIONAL_BASIS",
                "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_BLOCKED",
            }.issubset(set(resolver.OUTCOME_FAMILY))
        )
        self.assert_official_values_preserved(result)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            artifact = _synthetic_orientation_artifact()
            hostile_payload = {
                key: HOSTILE_SENTINELS[index % len(HOSTILE_SENTINELS)]
                for index, key in enumerate(HOSTILE_KEYS)
            }
            artifact["raw_body"] = hostile_payload
            artifact["orientation_view"]["raw_index_entry_body"] = HOSTILE_SENTINELS[0]
            artifact["orientation_view"]["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            artifact_path = _write_json(tmp_path / "hostile_orientation_result.json", artifact)
            request = _clean_request(artifact_path)
            request["raw_full_body"] = hostile_payload
            request["hidden_repo_state"] = HOSTILE_SENTINELS[-1]
            request_before = copy.deepcopy(request)

            result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(request)

        self.assertEqual(request, request_before)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_public_block_codes(result)
        self.assert_no_hostile_sentinels(result)
        self.assert_official_values_preserved(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_created_posture(result)
        self.assert_index_entry_is_small(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request, _artifact_path, _artifact = self.write_synthetic_artifact(tmp_path)
            request_path = _write_json(tmp_path / "request.json", request)

            result = resolver.resolve_local_relevance_orientation_index_entry_v0_min_from_path(
                request_path
            )
            summary = resolver.build_local_relevance_orientation_index_entry_v0_min_summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assert_not_blocked(result)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_local_relevance_orientation_index_entry_v0_min",
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(resolver.LocalRelevanceOrientationIndexEntryV0MinError):
                resolver.resolve_local_relevance_orientation_index_entry_v0_min_from_path(
                    malformed_path
                )
            with self.assertRaises(resolver.LocalRelevanceOrientationIndexEntryV0MinError):
                resolver.resolve_local_relevance_orientation_index_entry_v0_min_from_path(
                    tmp_path / "missing_request.json"
                )

            array_request_path = _write_json(tmp_path / "array_request.json", [])
            array_result = resolver.resolve_local_relevance_orientation_index_entry_v0_min_from_path(
                array_request_path
            )
            self.assert_blocked(
                array_result,
                expected_code="DECLARED_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_REQUEST_MALFORMED",
            )

            output_root = tmp_path / "local_relevance_orientation_index_entry_v0_min_output"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_local_relevance_orientation_index_entry_v0_min_result(
                    result
                )
                second_path = resolver.write_local_relevance_orientation_index_entry_v0_min_result(
                    result
                )

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIsInstance(json.loads(first_path.read_text(encoding="utf-8")), dict)
            self.assertIn("local_relevance_orientation_index_entry_v0_min", str(first_path))
            for forbidden in (
                "relevance_orientation_view_v0_min",
                "bounded_relevance_receipt_v0_min",
                "bounded_relevance_reception_v0_min",
                "post_runtime_daemon_runtime_loop",
                "source-transfer",
                "source-receipt",
                "reception/",
                "public-api",
                "participant-facing-interface",
                "distributed-network",
                "deployment",
                "public-release",
            ):
                self.assertNotIn(forbidden, str(first_path))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            artifact = _synthetic_orientation_artifact()
            artifact_before = copy.deepcopy(artifact)
            artifact_path = _write_json(Path(tmp) / "orientation.json", artifact)
            request = _clean_request(artifact_path)
            request["posture_mappings"] = {"official": "LOCAL_INDEX_ENTRY_ONLY"}
            request["raw_body"] = {"sentinel": HOSTILE_SENTINELS[0]}
            request_before = copy.deepcopy(request)
            declared_non_claims_before = copy.deepcopy(request["declared_non_claims"])

            result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(request)

        self.assertEqual(request, request_before)
        self.assertEqual(request["declared_non_claims"], declared_non_claims_before)
        self.assertEqual(artifact, artifact_before)
        self.assertEqual(request["index_entry_scope"], "LOCAL_INDEX_ENTRY_ONLY")
        self.assertEqual(request["index_entry_type"], "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY")
        self.assertEqual(request["posture_mappings"], {"official": "LOCAL_INDEX_ENTRY_ONLY"})
        self.assertEqual(request["raw_body"], {"sentinel": HOSTILE_SENTINELS[0]})
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)

    def test_predecessor_failure_preservation(self) -> None:
        self.assertTrue(V1_TEST_PATH.exists())
        v1_text = V1_TEST_PATH.read_text(encoding="utf-8")
        self.assertIn('self.assertIsNone(result["block"])', v1_text)

        with tempfile.TemporaryDirectory() as tmp:
            request, _artifact_path, _artifact = self.write_synthetic_artifact(Path(tmp))
            result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(request)
            summary = resolver.build_local_relevance_orientation_index_entry_v0_min_summary(result)

            repaired_result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(
                self._request_with(request, predecessor_failure_repaired=True)
            )
            reopened_result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(
                self._request_with(request, consumed_request_reopened=True)
            )
            reused_result = resolver.resolve_local_relevance_orientation_index_entry_v0_min(
                self._request_with(request, authorization_token_reused=True)
            )

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_not_blocked(result)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)
        self.assert_blocked(
            repaired_result,
            expected_code="PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
        self.assert_blocked(reopened_result, expected_code="CONSUMED_REQUEST_REOPENED")
        self.assert_blocked(reused_result, expected_code="AUTHORIZATION_TOKEN_REUSED")


if __name__ == "__main__":
    unittest.main()
