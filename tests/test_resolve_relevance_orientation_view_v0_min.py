"""Executable tests for the relevance orientation view resolver.

This suite is bounded to one local relevance orientation view. The view is an
instrument-shaped output from a clean bounded relevance receipt v2 artifact and
its referenced bounded relevance reception artifact. These tests do not create
a boundary, next-layer selection, source transfer, source receipt, reception
authorization, source, authority, currentness, truth, action, synchronization,
participation authorization, participant role, runtime permission, public API,
participant-facing interface, distributed network behavior, deployment, public
release, operation permission, broader reusable permission, adoption,
receiving-context governance, publication flow, or follow-on work.
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

import resolve_relevance_orientation_view_v0_min as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
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
    "deployment/",
    "public-release",
)

TOP_LEVEL_SECTIONS = (
    "relevance_orientation_view_metadata",
    "declared_relevance_orientation_view_question",
    "selected_bounded_relevance_receipt_v2_artifact_basis",
    "referenced_bounded_relevance_reception_artifact_basis",
    "orientation_view",
    "relevance_orientation_view_checks",
    "relevance_orientation_view_statement",
    "relevance_orientation_view_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "relevance_orientation_view_summary",
)

ORIENTATION_VIEW_FIELDS = (
    "orientation_view_id",
    "orientation_view_type",
    "orientation_view_version",
    "orientation_scope",
    "source_receipt_artifact",
    "referenced_reception_artifact",
    "receipt_outcome",
    "receipt_result_version",
    "receipt_failed_check_count",
    "receipt_scope",
    "receipt_does_not_expand_reception",
    "received_signal_id",
    "received_relevance_basis_id",
    "received_relevance_scope_id",
    "received_carrier_context_id",
    "received_reception_envelope_id",
    "inspectably_present",
    "standing_identifiers",
    "non_inference",
    "unavailable",
    "orientation_statement",
)

WRAPPER_KEYS_FORBIDDEN_IN_ORIENTATION_VIEW = (
    "outcome",
    "block",
    "relevance_orientation_view_checks",
    "non_claims",
    "relevance_orientation_view_summary",
    "relevance_orientation_view_metadata",
)

EXPECTED_BLOCK_CODES = (
    "RELEVANCE_ORIENTATION_VIEW_QUESTION_UNDECLARED",
    "RELEVANCE_ORIENTATION_VIEW_INTENT_UNSUPPORTED",
    "RELEVANCE_ORIENTATION_VIEW_BLOCK_REQUESTED",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_PATH_MISSING",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_UNREADABLE",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_NOT_JSON_OBJECT",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_NOT_RECORDED",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_FAILED_CHECKS_PRESENT",
    "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_VERSION_NOT_0_2_0",
    "RECEIPT_OBJECT_MISSING",
    "REFERENCED_RECEPTION_ARTIFACT_MISSING",
    "RECEIPT_SCOPE_NOT_INSPECTABLE_ONLY",
    "RECEIPT_EXPANDS_RECEPTION",
    "RECEIVED_SIGNAL_ID_MISSING",
    "RECEIVED_RELEVANCE_BASIS_ID_MISSING",
    "RECEIVED_RELEVANCE_SCOPE_ID_MISSING",
    "RECEIVED_CARRIER_CONTEXT_ID_MISSING",
    "RECEIVED_RECEPTION_ENVELOPE_ID_MISSING",
    "ORIENTATION_SCOPE_MISSING",
    "ORIENTATION_SCOPE_NOT_LOCAL_ONLY",
    "ORIENTATION_ADDED_NEW_SIGNAL",
    "ORIENTATION_ADDED_NEW_RELEVANCE_BASIS",
    "ORIENTATION_ADDED_NEW_RELEVANCE_SCOPE",
    "ORIENTATION_ADDED_NEW_CARRIER_CONTEXT",
    "ORIENTATION_ADDED_NEW_ENVELOPE",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_ORIENTATION_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_ORIENTATION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_ORIENTATION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_ORIENTATION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_ORIENTATION_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_RELEVANCE_ORIENTATION_VIEW_REQUEST_MALFORMED",
    "DECLARED_RELEVANCE_ORIENTATION_VIEW_REQUEST_UNREADABLE",
)

HOSTILE_SENTINELS = (
    "RAW_RELEVANCE_ORIENTATION_VIEW_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RELEVANCE_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RELEVANCE_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_RECEIPT_BODY_MUST_NOT_RETURN",
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

HOSTILE_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_orientation_body",
    "raw_relevance_orientation_view_body",
    "raw_bounded_relevance_receipt_body",
    "raw_bounded_relevance_reception_body",
    "raw_receipt_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "orientation_body",
    "relevance_orientation_view_body",
    "bounded_relevance_receipt_body",
    "bounded_relevance_reception_body",
    "receipt_body",
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


def write_json(path: Path, value: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def synthetic_reception_artifact(**overrides: Any) -> dict[str, Any]:
    artifact: dict[str, Any] = {
        "outcome": "BOUNDED_RELEVANCE_RECEPTION_RECORDED",
        "bounded_relevance_reception_metadata": {
            "bounded_relevance_reception_version": "0.1.0",
            "failed_check_count": 0,
        },
        "bounded_relevance_signal": {"signal_id": "bounded_relevance_signal_001"},
        "relevance_basis": {"basis_id": "bounded_relevance_basis_001"},
        "relevance_scope": {"scope_id": "bounded_relevance_scope_001"},
        "relevance_signal_carrier_context": {
            "context_id": "bounded_relevance_signal_carrier_context_001"
        },
        "bounded_relevance_reception_envelope": {
            "envelope_id": "bounded_relevance_reception_envelope_001"
        },
    }
    artifact.update(copy.deepcopy(overrides))
    return artifact


def synthetic_receipt_artifact(
    referenced_reception_artifact: Path | str,
    **overrides: Any,
) -> dict[str, Any]:
    artifact: dict[str, Any] = {
        "outcome": "BOUNDED_RELEVANCE_RECEIPT_RECORDED",
        "bounded_relevance_receipt_metadata": {
            "bounded_relevance_receipt_version": "0.2.0",
            "failed_check_count": 0,
        },
        "bounded_relevance_receipt_summary": {
            "outcome": "BOUNDED_RELEVANCE_RECEIPT_RECORDED",
            "result_version": "0.2.0",
            "failed_check_count": 0,
        },
        "receipt_object": {
            "receipt_id": "bounded_relevance_receipt_001",
            "receipt_type": "bounded_relevance_receipt",
            "receipt_version": "0.2.0",
            "received_relevance_artifact": str(referenced_reception_artifact),
            "received_relevance_artifact_outcome": "BOUNDED_RELEVANCE_RECEPTION_RECORDED",
            "received_relevance_artifact_result_version": "0.1.0",
            "received_relevance_artifact_failed_check_count": 0,
            "received_signal_id": "bounded_relevance_signal_001",
            "received_relevance_basis_id": "bounded_relevance_basis_001",
            "received_relevance_scope_id": "bounded_relevance_scope_001",
            "received_carrier_context_id": "bounded_relevance_signal_carrier_context_001",
            "received_reception_envelope_id": "bounded_relevance_reception_envelope_001",
            "receipt_scope": "INSPECTABLE_RECEIPT_ONLY",
            "does_not_expand_reception": True,
        },
    }
    artifact.update(copy.deepcopy(overrides))
    return artifact


def clean_request(receipt_artifact_path: Path | str) -> dict[str, Any]:
    return resolver.build_declared_relevance_orientation_view_v0_min_request(
        selected_bounded_relevance_receipt_v2_artifact=str(receipt_artifact_path)
    )


def block_code(result: dict[str, Any]) -> str | None:
    block = result.get("block") or {}
    return block.get("code") or block.get("block_code")


class RelevanceOrientationViewResolverTests(unittest.TestCase):
    def write_synthetic_pair(
        self,
        tmpdir: Path,
        receipt_overrides: dict[str, Any] | None = None,
        reception_overrides: dict[str, Any] | None = None,
    ) -> tuple[dict[str, Any], Path, Path, dict[str, Any], dict[str, Any]]:
        reception_artifact = synthetic_reception_artifact(**(reception_overrides or {}))
        reception_path = write_json(tmpdir / "synthetic_reception_result.json", reception_artifact)
        receipt_artifact = synthetic_receipt_artifact(reception_path, **(receipt_overrides or {}))
        receipt_path = write_json(tmpdir / "synthetic_receipt_v2_result.json", receipt_artifact)
        return clean_request(receipt_path), receipt_path, reception_path, receipt_artifact, reception_artifact

    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        block = result.get("block") or {}
        for key in ("code", "block_code"):
            code = block.get(key)
            if code:
                self.assertIn(code, resolver.BLOCK_CODES)
        for code in block.get("failed_block_codes", []):
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in result.get("relevance_orientation_view_checks", []):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_failed_code_present(self, result: dict[str, Any], expected_code: str) -> None:
        block = result.get("block") or {}
        check_codes = {
            check.get("block_code") or check.get("failure_code")
            for check in result.get("relevance_orientation_view_checks", [])
        }
        emitted_codes = set(block.get("failed_block_codes", [])) | check_codes | {block_code(result)}
        self.assertIn(expected_code, emitted_codes)

    def assert_non_claims_canonical_false(self, result: dict[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIsInstance(non_claims[key], bool, key)

    def assert_bool_fields_are_bool(self, result: dict[str, Any]) -> None:
        for section_name in ("relevance_orientation_view_statement", "non_claims"):
            for key, value in result[section_name].items():
                self.assertIsInstance(value, bool, f"{section_name}.{key}")
        orientation_view = result.get("orientation_view") or {}
        for value in (orientation_view.get("non_inference") or {}).values():
            self.assertIsInstance(value, bool)
        for check in result.get("relevance_orientation_view_checks", []):
            self.assertIsInstance(check.get("passed"), bool)

    def assert_orientation_view_is_small(self, result: dict[str, Any]) -> None:
        orientation_view = result.get("orientation_view")
        self.assertIsInstance(orientation_view, dict)
        if not orientation_view:
            return
        self.assertLessEqual(set(orientation_view), set(ORIENTATION_VIEW_FIELDS))
        for key in WRAPPER_KEYS_FORBIDDEN_IN_ORIENTATION_VIEW:
            self.assertNotIn(key, orientation_view)
        serialized = json.dumps(orientation_view, sort_keys=True)
        self.assertNotIn("raw_full_body", serialized)
        self.assertNotIn("artifact_body", serialized)
        self.assertNotIn("bounded_relevance_receipt_body", serialized)
        self.assertNotIn("bounded_relevance_reception_body", serialized)

    def assert_no_created_posture(self, result: dict[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in (
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
        ):
            self.assertIs(non_claims[key], False, key)
        orientation_view = result.get("orientation_view") or {}
        for key, value in (orientation_view.get("non_inference") or {}).items():
            self.assertIs(value, False, key)

    def assert_no_hostile_sentinels(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_values_preserved(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("LOCAL_ORIENTATION_ONLY", serialized)
        self.assertIn("INSPECTABLE_RECEIPT_ONLY", serialized)
        self.assertIn(str(result["outcome"]), serialized)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", serialized)

    def assert_blocked_public_and_safe(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIsNotNone(block_code(result))
        self.assertIn(block_code(result), resolver.BLOCK_CODES)
        self.assert_public_block_codes(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_created_posture(result)
        self.assert_orientation_view_is_small(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_relevance_orientation_view_v0_min",
            "resolve_relevance_orientation_view_v0_min_from_path",
            "write_relevance_orientation_view_v0_min_result",
            "build_relevance_orientation_view_v0_min_summary",
            "build_declared_relevance_orientation_view_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_ORIENTATION_SCOPE_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_relevance_orientation_view_v0_min")
        output_root = str(resolver.OUTPUT_ROOT)
        self.assertTrue(output_root.endswith(EXPECTED_OUTPUT_ROOT_SUFFIX))
        self.assertIn("LOCAL_ORIENTATION_ONLY", resolver.SUPPORTED_ORIENTATION_SCOPE_VALUES)
        for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
            self.assertNotIn(fragment, output_root)
        for code in EXPECTED_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_synthetic_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, receipt_path, reception_path, _, _ = self.write_synthetic_pair(Path(tmp))
            result = resolver.resolve_relevance_orientation_view_v0_min(request)
            summary = resolver.build_relevance_orientation_view_v0_min_summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertFalse(result["block"]["blocked"])
        self.assertIsNone(result["block"]["code"])
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], "resolve_relevance_orientation_view_v0_min")
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["request_id"], request["relevance_orientation_view_request_id"])
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        orientation_view = result["orientation_view"]
        self.assert_orientation_view_is_small(result)
        self.assertEqual(orientation_view["orientation_view_id"], "relevance_orientation_view_001")
        self.assertEqual(orientation_view["orientation_view_type"], "relevance_orientation_view")
        self.assertEqual(orientation_view["orientation_view_version"], "0.1.0")
        self.assertEqual(orientation_view["orientation_scope"], "LOCAL_ORIENTATION_ONLY")
        self.assertEqual(orientation_view["source_receipt_artifact"], str(receipt_path))
        self.assertEqual(orientation_view["referenced_reception_artifact"], str(reception_path))
        self.assertEqual(orientation_view["receipt_outcome"], "BOUNDED_RELEVANCE_RECEIPT_RECORDED")
        self.assertEqual(orientation_view["receipt_result_version"], "0.2.0")
        self.assertEqual(orientation_view["receipt_failed_check_count"], 0)
        self.assertEqual(orientation_view["receipt_scope"], "INSPECTABLE_RECEIPT_ONLY")
        self.assertIs(orientation_view["receipt_does_not_expand_reception"], True)
        self.assertEqual(orientation_view["received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(orientation_view["received_relevance_basis_id"], "bounded_relevance_basis_001")
        self.assertEqual(orientation_view["received_relevance_scope_id"], "bounded_relevance_scope_001")
        self.assertEqual(
            orientation_view["received_carrier_context_id"],
            "bounded_relevance_signal_carrier_context_001",
        )
        self.assertEqual(
            orientation_view["received_reception_envelope_id"],
            "bounded_relevance_reception_envelope_001",
        )

        for key in ("inspectably_present", "standing_identifiers", "non_inference", "unavailable", "orientation_statement"):
            self.assertIn(key, orientation_view)
        for value in (
            "bounded relevance receipt v2 artifact",
            "referenced bounded relevance reception artifact",
            "received signal id",
            "received relevance basis id",
            "received relevance scope id",
            "received carrier context id",
            "received reception envelope id",
        ):
            self.assertIn(value, orientation_view["inspectably_present"])
        self.assertEqual(
            orientation_view["standing_identifiers"],
            {
                "received_signal_id": "bounded_relevance_signal_001",
                "received_relevance_basis_id": "bounded_relevance_basis_001",
                "received_relevance_scope_id": "bounded_relevance_scope_001",
                "received_carrier_context_id": "bounded_relevance_signal_carrier_context_001",
                "received_reception_envelope_id": "bounded_relevance_reception_envelope_001",
            },
        )
        for key in (
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
        ):
            self.assertIn(key, orientation_view["non_inference"])
            self.assertIs(orientation_view["non_inference"][key], False)
        for value in (
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
        ):
            self.assertIn(value, orientation_view["unavailable"])

        statement = result["relevance_orientation_view_statement"]
        for key in (
            "relevance_orientation_view_recorded",
            "source_receipt_artifact_preserved",
            "referenced_reception_artifact_preserved",
            "received_signal_id_preserved",
            "received_relevance_basis_id_preserved",
            "received_relevance_scope_id_preserved",
            "received_carrier_context_id_preserved",
            "received_reception_envelope_id_preserved",
            "orientation_scope_local_only",
            "orientation_does_not_expand_receipt",
            "orientation_does_not_expand_reception",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(statement[key], True, key)
        self.assert_non_claims_canonical_false(result)
        self.assert_bool_fields_are_bool(result)
        self.assert_official_values_preserved(result)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        default_artifact = REPO_ROOT / resolver.DEFAULT_RECEIPT_V2_ARTIFACT
        if not default_artifact.exists():
            self.skipTest("default bounded relevance receipt v2 live artifact is not present")
        request = resolver.build_declared_relevance_orientation_view_v0_min_request()
        result = resolver.resolve_relevance_orientation_view_v0_min(request)
        summary = resolver.build_relevance_orientation_view_v0_min_summary(result)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        orientation_view = result["orientation_view"]
        self.assertEqual(orientation_view["orientation_scope"], "LOCAL_ORIENTATION_ONLY")
        self.assertEqual(orientation_view["receipt_scope"], "INSPECTABLE_RECEIPT_ONLY")
        self.assertEqual(
            orientation_view["received_reception_envelope_id"],
            "bounded_relevance_reception_envelope_001",
        )
        for key in (
            "authority_created",
            "currentness_created",
            "truth_created",
            "action_created",
            "synchronization_created",
            "participation_authorized",
            "runtime_permission_created",
            "public_api_created",
            "distributed_network_behavior_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(orientation_view["non_inference"][key], False)

    def test_critical_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            clean, _, _, _, _ = self.write_synthetic_pair(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(clean)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_relevance_orientation_view_v0_min(request)
                    self.assert_blocked_public_and_safe(result)
                    self.assertGreater(
                        len([check for check in result["relevance_orientation_view_checks"] if not check["passed"]]),
                        0,
                    )
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_non_claims_canonical_false(result)
                    self.assert_no_created_posture(result)
                    self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
                    self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
                    self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)

    def test_representative_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base_tmp = Path(tmp)

            def clean() -> dict[str, Any]:
                request, _, _, _, _ = self.write_synthetic_pair(base_tmp / "case_clean")
                return request

            def with_receipt_override(**override: Any) -> dict[str, Any]:
                request, _, _, _, _ = self.write_synthetic_pair(
                    base_tmp / f"case_{len(list(base_tmp.iterdir()))}",
                    receipt_overrides=override,
                )
                return request

            def with_receipt_object_updates(**updates: Any) -> dict[str, Any]:
                request, receipt_path, reception_path, receipt_artifact, _ = self.write_synthetic_pair(
                    base_tmp / f"case_{len(list(base_tmp.iterdir()))}"
                )
                receipt_artifact["receipt_object"].update(updates)
                write_json(receipt_path, receipt_artifact)
                return request

            unreadable_request = clean()
            unreadable_request["selected_bounded_relevance_receipt_v2_artifact"] = str(
                base_tmp / "missing_receipt.json"
            )
            array_receipt = base_tmp / "array_receipt.json"
            write_json(array_receipt, [])
            array_request = clean_request(array_receipt)
            array_request["relevance_orientation_view_request_id"] = "array_request"

            non_json_reception_request, receipt_path, _, receipt_artifact, _ = self.write_synthetic_pair(
                base_tmp / "non_json_reception"
            )
            bad_reception = base_tmp / "non_json_reception" / "bad_reception.json"
            write_json(bad_reception, [])
            receipt_artifact["receipt_object"]["received_relevance_artifact"] = str(bad_reception)
            write_json(receipt_path, receipt_artifact)

            missing_reception_request = with_receipt_object_updates(
                received_relevance_artifact=str(base_tmp / "missing_reception.json")
            )

            block_cases: list[tuple[str, Any, str | None]] = [
                ("explicit block intent", {**clean(), "relevance_orientation_view_intent": "BLOCK_RELEVANCE_ORIENTATION_VIEW"}, "RELEVANCE_ORIENTATION_VIEW_BLOCK_REQUESTED"),
                ("missing request mapping", {}, None),
                ("non-mapping request", ["not", "a", "mapping"], "DECLARED_RELEVANCE_ORIENTATION_VIEW_REQUEST_MALFORMED"),
                ("unsupported intent", {**clean(), "relevance_orientation_view_intent": "UNSUPPORTED"}, "RELEVANCE_ORIENTATION_VIEW_INTENT_UNSUPPORTED"),
                ("receipt path missing", {**clean(), "selected_bounded_relevance_receipt_v2_artifact": ""}, "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_PATH_MISSING"),
                ("receipt unreadable", unreadable_request, "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_UNREADABLE"),
                ("receipt JSON array", array_request, "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_NOT_JSON_OBJECT"),
                ("receipt not recorded", with_receipt_override(outcome="BOUNDED_RELEVANCE_RECEIPT_NOT_RECORDED"), "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_NOT_RECORDED"),
                ("receipt failed checks", with_receipt_override(bounded_relevance_receipt_metadata={"bounded_relevance_receipt_version": "0.2.0", "failed_check_count": 1}), "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_FAILED_CHECKS_PRESENT"),
                ("receipt version wrong", with_receipt_override(bounded_relevance_receipt_metadata={"bounded_relevance_receipt_version": "0.3.0", "failed_check_count": 0}), "BOUNDED_RELEVANCE_RECEIPT_V2_ARTIFACT_VERSION_NOT_0_2_0"),
                ("receipt object missing", with_receipt_override(receipt_object=None), "RECEIPT_OBJECT_MISSING"),
                ("referenced reception missing", missing_reception_request, "REFERENCED_RECEPTION_ARTIFACT_MISSING"),
                ("referenced reception not JSON object", non_json_reception_request, "REFERENCED_RECEPTION_ARTIFACT_MISSING"),
                ("receipt scope wrong", with_receipt_object_updates(receipt_scope="NOT_INSPECTABLE"), "RECEIPT_SCOPE_NOT_INSPECTABLE_ONLY"),
                ("receipt expands", with_receipt_object_updates(does_not_expand_reception=False), "RECEIPT_EXPANDS_RECEPTION"),
                ("missing signal id", with_receipt_object_updates(received_signal_id=""), "RECEIVED_SIGNAL_ID_MISSING"),
                ("missing basis id", with_receipt_object_updates(received_relevance_basis_id=""), "RECEIVED_RELEVANCE_BASIS_ID_MISSING"),
                ("missing scope id", with_receipt_object_updates(received_relevance_scope_id=""), "RECEIVED_RELEVANCE_SCOPE_ID_MISSING"),
                ("missing carrier id", with_receipt_object_updates(received_carrier_context_id=""), "RECEIVED_CARRIER_CONTEXT_ID_MISSING"),
                ("missing envelope id", with_receipt_object_updates(received_reception_envelope_id=""), "RECEIVED_RECEPTION_ENVELOPE_ID_MISSING"),
                ("missing orientation scope", {key: value for key, value in clean().items() if key != "orientation_scope"}, "ORIENTATION_SCOPE_MISSING"),
                ("orientation scope wrong", {**clean(), "orientation_scope": "NOT_LOCAL"}, "ORIENTATION_SCOPE_NOT_LOCAL_ONLY"),
                ("orientation adds signal", {**clean(), "orientation_adds_new_signal": True}, "ORIENTATION_ADDED_NEW_SIGNAL"),
                ("orientation adds basis", {**clean(), "orientation_adds_new_relevance_basis": True}, "ORIENTATION_ADDED_NEW_RELEVANCE_BASIS"),
                ("orientation adds scope", {**clean(), "orientation_adds_new_relevance_scope": True}, "ORIENTATION_ADDED_NEW_RELEVANCE_SCOPE"),
                ("orientation adds carrier", {**clean(), "orientation_adds_new_carrier_context": True}, "ORIENTATION_ADDED_NEW_CARRIER_CONTEXT"),
                ("orientation adds envelope", {**clean(), "orientation_adds_new_envelope": True}, "ORIENTATION_ADDED_NEW_ENVELOPE"),
                ("source transfer occurred", {**clean(), "source_transfer_occurred": True}, "SOURCE_TRANSFER_OCCURRED"),
                ("source receipt occurred", {**clean(), "source_receipt_occurred": True}, "SOURCE_RECEIPT_OCCURRED"),
                ("reception authorization", {**clean(), "reception_authorization_created": True}, "RECEPTION_AUTHORIZATION_CREATED"),
                ("source created", {**clean(), "source_created": True}, "SOURCE_CREATED"),
                ("authority created", {**clean(), "authority_created": True}, "AUTHORITY_CREATED"),
                ("currentness created", {**clean(), "currentness_created": True}, "CURRENTNESS_CREATED"),
                ("truth created", {**clean(), "truth_created": True}, "TRUTH_CREATED"),
                ("action created", {**clean(), "action_created": True}, "ACTION_CREATED"),
                ("synchronization created", {**clean(), "synchronization_created": True}, "SYNCHRONIZATION_CREATED"),
                ("participation authorized", {**clean(), "participation_authorized": True}, "PARTICIPATION_AUTHORIZED"),
                ("participant role", {**clean(), "participant_role_created": True}, "PARTICIPANT_ROLE_CREATED"),
                ("runtime permission", {**clean(), "runtime_permission_created": True}, "RUNTIME_PERMISSION_CREATED"),
                ("public API", {**clean(), "public_api_created": True}, "PUBLIC_API_CREATED"),
                ("participant-facing interface", {**clean(), "participant_facing_interface_created": True}, "PARTICIPANT_FACING_INTERFACE_CREATED"),
                ("distributed behavior", {**clean(), "distributed_network_behavior_created": True}, "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
                ("deployment", {**clean(), "deployment_created": True}, "DEPLOYMENT_CREATED"),
                ("public release", {**clean(), "public_release_created": True}, "PUBLIC_RELEASE_CREATED"),
                ("operation permission", {**clean(), "operation_permission_created": True}, "OPERATION_PERMISSION_CREATED"),
                ("broader reusable permission", {**clean(), "broader_reusable_permission_created": True}, "BROADER_REUSABLE_PERMISSION_CREATED"),
                ("follow-on", {**clean(), "follow_on_work_authorized": True}, "FOLLOW_ON_WORK_AUTHORIZED"),
                ("artifact existence authority", {**clean(), "artifact_existence_treated_as_orientation_authority": True}, "ARTIFACT_EXISTENCE_TREATED_AS_ORIENTATION_AUTHORITY"),
                ("latest posture authority", {**clean(), "latest_file_posture_treated_as_orientation_authority": True}, "LATEST_FILE_POSTURE_TREATED_AS_ORIENTATION_AUTHORITY"),
                ("repo local authority", {**clean(), "repo_local_availability_treated_as_orientation_authority": True}, "REPO_LOCAL_AVAILABILITY_TREATED_AS_ORIENTATION_AUTHORITY"),
                ("hidden content", {**clean(), "hidden_repo_state_used_as_orientation_content": True}, "HIDDEN_REPO_STATE_USED_AS_ORIENTATION_CONTENT"),
                ("hidden authority", {**clean(), "hidden_repo_state_used_as_orientation_authority": True}, "HIDDEN_REPO_STATE_USED_AS_ORIENTATION_AUTHORITY"),
                ("predecessor repaired", {**clean(), "predecessor_failure_repaired": True}, "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
                ("predecessor hidden", {**clean(), "predecessor_failure_hidden": True}, "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
                ("predecessor claimed", {**clean(), "predecessor_failure_claimed_passed": True}, "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
                ("consumed reopened", {**clean(), "consumed_request_reopened": True}, "CONSUMED_REQUEST_REOPENED"),
                ("authorization reused", {**clean(), "authorization_token_reused": True}, "AUTHORIZATION_TOKEN_REUSED"),
            ]

            required_non_claim_missing = clean()
            required_non_claim_missing["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])
            block_cases.append(("required non-claim missing", required_non_claim_missing, "NON_CLAIM_MISSING_OR_FLIPPED"))

            for name, request, expected_code in block_cases:
                with self.subTest(name=name):
                    result = resolver.resolve_relevance_orientation_view_v0_min(request)
                    self.assert_blocked_public_and_safe(result)
                    if expected_code is not None:
                        self.assert_failed_code_present(result, expected_code)

    def test_missing_or_incomplete_declared_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            clean, _, _, _, _ = self.write_synthetic_pair(Path(tmp))
            variants: list[tuple[str, dict[str, Any]]] = []
            removed = copy.deepcopy(clean)
            removed.pop("declared_non_claims")
            variants.append(("removed declared_non_claims", removed))
            empty = copy.deepcopy(clean)
            empty["declared_non_claims"] = {}
            variants.append(("empty declared_non_claims", empty))
            missing_one = copy.deepcopy(clean)
            missing_one["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])
            variants.append(("missing one required non-claim", missing_one))
            string_one = copy.deepcopy(clean)
            string_one["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = "false"
            variants.append(("string non-claim", string_one))
            none_one = copy.deepcopy(clean)
            none_one["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = None
            variants.append(("none non-claim", none_one))

            for name, request in variants:
                with self.subTest(name=name):
                    result = resolver.resolve_relevance_orientation_view_v0_min(request)
                    self.assertIn(
                        result["outcome"],
                        (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS),
                    )
                    self.assert_public_block_codes(result)
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _, _, _ = self.write_synthetic_pair(Path(tmp))
            result = resolver.resolve_relevance_orientation_view_v0_min(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(result["orientation_view"]["orientation_scope"], "LOCAL_ORIENTATION_ONLY")
        self.assertEqual(result["orientation_view"]["receipt_scope"], "INSPECTABLE_RECEIPT_ONLY")
        for expected in (
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_NOT_RECORDED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_BLOCKED,
        ):
            self.assertIn(expected, resolver.OUTCOME_FAMILY)
        self.assert_official_values_preserved(result)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            hostile_payload = {
                key: HOSTILE_SENTINELS[index % len(HOSTILE_SENTINELS)]
                for index, key in enumerate(HOSTILE_KEYS)
            }
            request, receipt_path, reception_path, receipt_artifact, reception_artifact = self.write_synthetic_pair(tmpdir)
            request_before = copy.deepcopy(request)
            request["hostile_extra"] = copy.deepcopy(hostile_payload)
            request_before_resolve = copy.deepcopy(request)
            receipt_artifact["hostile_raw"] = copy.deepcopy(hostile_payload)
            reception_artifact["hostile_raw"] = copy.deepcopy(hostile_payload)
            write_json(receipt_path, receipt_artifact)
            write_json(reception_path, reception_artifact)
            result = resolver.resolve_relevance_orientation_view_v0_min(request)

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_hostile_sentinels(result)
        self.assert_official_values_preserved(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_created_posture(result)
        self.assert_orientation_view_is_small(result)
        self.assertEqual(request, request_before_resolve)
        self.assertEqual(request_before["declared_non_claims"], request["declared_non_claims"])
        self.assertEqual(
            request_before["selected_bounded_relevance_receipt_v2_artifact"],
            request["selected_bounded_relevance_receipt_v2_artifact"],
        )

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            request, _, _, _, _ = self.write_synthetic_pair(tmpdir / "basis")
            request_path = write_json(tmpdir / "request.json", request)
            result = resolver.resolve_relevance_orientation_view_v0_min_from_path(request_path)
            summary = resolver.build_relevance_orientation_view_v0_min_summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], "resolve_relevance_orientation_view_v0_min")

            malformed_path = tmpdir / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(resolver.RelevanceOrientationViewV0MinError):
                resolver.resolve_relevance_orientation_view_v0_min_from_path(malformed_path)

            array_path = write_json(tmpdir / "array_request.json", [])
            array_result = resolver.resolve_relevance_orientation_view_v0_min_from_path(array_path)
            self.assert_blocked_public_and_safe(array_result)

            with self.assertRaises(resolver.RelevanceOrientationViewV0MinError):
                resolver.resolve_relevance_orientation_view_v0_min_from_path(tmpdir / "missing_request.json")

            output_root = tmpdir / "relevance_orientation_view_v0_min_output"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_relevance_orientation_view_v0_min_result(result)
                second_path = resolver.write_relevance_orientation_view_v0_min_result(result)
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(first_path.parent.exists())
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn("relevance_orientation_view_v0_min", str(first_path))
            for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
                self.assertNotIn(fragment, str(first_path))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _, receipt_artifact, reception_artifact = self.write_synthetic_pair(Path(tmp))
            request["nested_payload"] = {"raw_body": "RAW_ORIENTATION_BODY_MUST_NOT_RETURN"}
            request_before = copy.deepcopy(request)
            receipt_before = copy.deepcopy(receipt_artifact)
            reception_before = copy.deepcopy(reception_artifact)
            result = resolver.resolve_relevance_orientation_view_v0_min(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, request_before)
        self.assertEqual(request["declared_non_claims"], request_before["declared_non_claims"])
        self.assertEqual(receipt_artifact, receipt_before)
        self.assertEqual(reception_artifact, reception_before)
        self.assertEqual(request["orientation_scope"], "LOCAL_ORIENTATION_ONLY")

    def test_predecessor_failure_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _, _, _ = self.write_synthetic_pair(Path(tmp))
            result = resolver.resolve_relevance_orientation_view_v0_min(request)
            summary = resolver.build_relevance_orientation_view_v0_min_summary(result)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
