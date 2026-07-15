"""Executable tests for the bounded relevance receipt v2 resolver.

This suite is bounded to one inspectable bounded relevance receipt object. The
v2 resolver must read the selected bounded relevance reception artifact JSON,
extract the received signal, basis, scope, carrier-context, and envelope ids
from that artifact, and preserve the actual upstream envelope id without
expanding reception.

The v1 bounded relevance receipt resolver, test, and live artifact remain
preserved predecessor evidence only. These tests do not repair v1, hide v1,
claim v1 is v2, overwrite the v1 artifact, or create source transfer, source
receipt, reception authorization, source, authority, currentness, truth,
action, synchronization, participation authorization, participant role, runtime
permission, public API, participant-facing interface, distributed network
behavior, deployment, public release, operation permission, broader reusable
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

import resolve_bounded_relevance_receipt_v0_min_v2 as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2"
)
V1_OUTPUT_ROOT_SEGMENT = "integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min"
V2_OUTPUT_ROOT_SEGMENT = "integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2"

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
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
    "bounded_relevance_receipt_metadata",
    "declared_bounded_relevance_receipt_question",
    "selected_bounded_relevance_reception_artifact_basis",
    "extracted_bounded_relevance_reception_artifact_facts",
    "receipt_object",
    "bounded_relevance_receipt_checks",
    "bounded_relevance_receipt_statement",
    "bounded_relevance_receipt_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "bounded_relevance_receipt_summary",
)

RECEIPT_OBJECT_FIELDS = (
    "receipt_id",
    "receipt_type",
    "receipt_version",
    "received_relevance_artifact",
    "received_relevance_artifact_outcome",
    "received_relevance_artifact_result_version",
    "received_relevance_artifact_failed_check_count",
    "received_signal_id",
    "received_relevance_basis_id",
    "received_relevance_scope_id",
    "received_carrier_context_id",
    "received_reception_envelope_id",
    "receipt_scope",
    "does_not_expand_reception",
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
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "follow_on_work_authorized",
)

WRAPPER_KEYS_FORBIDDEN_IN_RECEIPT_OBJECT = (
    "outcome",
    "block",
    "bounded_relevance_receipt_checks",
    "non_claims",
    "bounded_relevance_receipt_summary",
    "bounded_relevance_receipt_metadata",
    "extracted_bounded_relevance_reception_artifact_facts",
)

EXTRACTED_FACT_KEYS = (
    "received_relevance_artifact_outcome",
    "received_relevance_artifact_result_version",
    "received_relevance_artifact_failed_check_count",
    "received_signal_id",
    "received_relevance_basis_id",
    "received_relevance_scope_id",
    "received_carrier_context_id",
    "received_reception_envelope_id",
)

EXPECTED_BLOCK_CODES = (
    "BOUNDED_RELEVANCE_RECEIPT_QUESTION_UNDECLARED",
    "BOUNDED_RELEVANCE_RECEIPT_INTENT_UNSUPPORTED",
    "BOUNDED_RELEVANCE_RECEIPT_BLOCK_REQUESTED",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_PATH_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_UNREADABLE",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_JSON_OBJECT",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_EXTRACTION_FAILED",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_RECORDED",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_VERSION_NOT_0_1_0",
    "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_AMBIGUOUS",
    "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_AMBIGUOUS",
    "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_AMBIGUOUS",
    "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_AMBIGUOUS",
    "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_AMBIGUOUS",
    "DECLARED_EXTRACTED_OUTCOME_MISMATCH",
    "DECLARED_EXTRACTED_RESULT_VERSION_MISMATCH",
    "DECLARED_EXTRACTED_FAILED_CHECK_COUNT_MISMATCH",
    "DECLARED_EXTRACTED_SIGNAL_ID_MISMATCH",
    "DECLARED_EXTRACTED_RELEVANCE_BASIS_ID_MISMATCH",
    "DECLARED_EXTRACTED_RELEVANCE_SCOPE_ID_MISMATCH",
    "DECLARED_EXTRACTED_CARRIER_CONTEXT_ID_MISMATCH",
    "DECLARED_EXTRACTED_RECEPTION_ENVELOPE_ID_MISMATCH",
    "RECEIPT_SCOPE_MISSING",
    "RECEIPT_SCOPE_NOT_INSPECTABLE_ONLY",
    "RECEIPT_EXPANDS_RECEPTION",
    "RECEIPT_CREATED_NEW_SIGNAL",
    "RECEIPT_CREATED_NEW_RELEVANCE_BASIS",
    "RECEIPT_CREATED_NEW_RELEVANCE_SCOPE",
    "RECEIPT_CREATED_NEW_CARRIER_CONTEXT",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RECEIPT_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_RECEIPT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RECEIPT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RECEIPT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RECEIPT_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "V1_RECEIPT_ARTIFACT_NOT_PRESERVED_AS_PREDECESSOR_EVIDENCE",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_BOUNDED_RELEVANCE_RECEIPT_REQUEST_MALFORMED",
    "DECLARED_BOUNDED_RELEVANCE_RECEIPT_REQUEST_UNREADABLE",
)

HOSTILE_SENTINELS = (
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


def synthetic_reception_artifact(**overrides: Any) -> dict[str, Any]:
    artifact: dict[str, Any] = {
        "outcome": "BOUNDED_RELEVANCE_RECEPTION_RECORDED",
        "bounded_relevance_reception_metadata": {
            "bounded_relevance_reception_version": "0.1.0",
            "failed_check_count": 0,
        },
        "bounded_relevance_signal": {
            "signal_id": "bounded_relevance_signal_001",
            "signal_kind": "medium_facing_reception_material",
        },
        "relevance_basis": {
            "basis_id": "bounded_relevance_basis_001",
            "basis_role": "declared_relevance_basis_only",
        },
        "relevance_scope": {
            "scope_id": "bounded_relevance_scope_001",
            "bounded": True,
            "one_signal_only": True,
        },
        "relevance_signal_carrier_context": {
            "context_id": "bounded_relevance_signal_carrier_context_001",
            "basis_role": "context_only",
        },
        "bounded_relevance_reception_envelope": {
            "envelope_id": "bounded_relevance_reception_envelope_001",
            "declared": True,
            "fresh_admission_required_outside_envelope": True,
        },
        "bounded_runtime_loop_envelope": {
            "envelope_id": "bounded_runtime_loop_envelope_v0",
        },
    }
    artifact.update(copy.deepcopy(overrides))
    return artifact


def write_json(path: Path, value: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def write_synthetic_artifact(directory: Path, artifact: dict[str, Any] | None = None) -> Path:
    return write_json(directory / "synthetic_bounded_relevance_reception_result.json", artifact or synthetic_reception_artifact())


def clean_request(artifact_path: Path) -> dict[str, Any]:
    return resolver.build_declared_bounded_relevance_receipt_v0_min_v2_request(
        selected_bounded_relevance_reception_artifact=str(artifact_path)
    )


def block_code(result: dict[str, Any]) -> str | None:
    block = result.get("block") or {}
    return block.get("code") or block.get("block_code")


class BoundedRelevanceReceiptV2ResolverTests(unittest.TestCase):
    def make_request_and_artifact(
        self,
        tmpdir: Path,
        artifact: dict[str, Any] | None = None,
    ) -> tuple[dict[str, Any], Path, dict[str, Any]]:
        artifact_dict = artifact or synthetic_reception_artifact()
        artifact_path = write_synthetic_artifact(tmpdir, artifact_dict)
        return clean_request(artifact_path), artifact_path, artifact_dict

    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        block = result.get("block") or {}
        for key in ("code", "block_code"):
            code = block.get(key)
            if code:
                self.assertIn(code, resolver.BLOCK_CODES)
        for code in block.get("failed_block_codes", []):
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in result.get("bounded_relevance_receipt_checks", []):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_failed_code_present(self, result: dict[str, Any], expected_code: str) -> None:
        block = result.get("block") or {}
        check_codes = {
            check.get("block_code") or check.get("failure_code")
            for check in result.get("bounded_relevance_receipt_checks", [])
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
        for section_name in ("bounded_relevance_receipt_statement", "non_claims"):
            for key, value in result[section_name].items():
                self.assertIsInstance(value, bool, f"{section_name}.{key}")
        receipt_object = result.get("receipt_object") or {}
        for key, value in receipt_object.items():
            if key in resolver.REQUIRED_FALSE_NON_CLAIMS or key == "does_not_expand_reception":
                self.assertIsInstance(value, bool, key)

    def assert_receipt_object_is_small(self, result: dict[str, Any]) -> None:
        receipt_object = result.get("receipt_object")
        self.assertIsInstance(receipt_object, dict)
        if not receipt_object:
            return
        self.assertLessEqual(set(receipt_object), set(RECEIPT_OBJECT_FIELDS))
        for key in WRAPPER_KEYS_FORBIDDEN_IN_RECEIPT_OBJECT:
            self.assertNotIn(key, receipt_object)

    def assert_extracted_facts_are_small(self, result: dict[str, Any]) -> None:
        facts = result.get("extracted_bounded_relevance_reception_artifact_facts")
        self.assertIsInstance(facts, dict)
        self.assertLessEqual(set(facts), set(EXTRACTED_FACT_KEYS))
        serialized = json.dumps(facts, sort_keys=True)
        self.assertNotIn("raw_body", serialized)
        self.assertNotIn("raw_full_body", serialized)
        self.assertNotIn("artifact_body", serialized)
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
            "deployment_created",
            "public_release_created",
            "operation_permission_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(non_claims[key], False, key)
        receipt_object = result.get("receipt_object") or {}
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
            "deployment_created",
            "public_release_created",
            "operation_permission_created",
            "follow_on_work_authorized",
        ):
            if key in receipt_object:
                self.assertIs(receipt_object[key], False, key)

    def assert_no_hostile_sentinels(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_values_preserved(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("INSPECTABLE_RECEIPT_ONLY", serialized)
        self.assertIn(str(result["outcome"]), serialized)
        self.assertNotIn("[bounded-relevance-receipt-redacted]", serialized)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", serialized)

    def assert_blocked_public_and_safe(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIsNotNone(block_code(result))
        self.assertIn(block_code(result), resolver.BLOCK_CODES)
        self.assert_public_block_codes(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_created_posture(result)
        self.assert_receipt_object_is_small(result)
        self.assert_extracted_facts_are_small(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_bounded_relevance_receipt_v0_min_v2",
            "resolve_bounded_relevance_receipt_v0_min_v2_from_path",
            "write_bounded_relevance_receipt_v0_min_v2_result",
            "build_bounded_relevance_receipt_v0_min_v2_summary",
            "build_declared_bounded_relevance_receipt_v0_min_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_RECEIPT_SCOPE_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.2.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_bounded_relevance_receipt_v0_min_v2")
        output_root = str(resolver.OUTPUT_ROOT)
        self.assertTrue(output_root.endswith(EXPECTED_OUTPUT_ROOT_SUFFIX))
        self.assertIn("INSPECTABLE_RECEIPT_ONLY", resolver.SUPPORTED_RECEIPT_SCOPE_VALUES)
        self.assertNotEqual(Path(output_root).name, V1_OUTPUT_ROOT_SEGMENT)
        self.assertEqual(Path(output_root).name, V2_OUTPUT_ROOT_SEGMENT)
        for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
            self.assertNotIn(fragment, output_root)
        for code in EXPECTED_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_synthetic_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, artifact_path, _ = self.make_request_and_artifact(Path(tmp))
            result = resolver.resolve_bounded_relevance_receipt_v0_min_v2(request)
            summary = resolver.build_bounded_relevance_receipt_v0_min_v2_summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertFalse(result["block"]["blocked"])
        self.assertIsNone(result["block"]["code"])
        self.assertEqual(summary["result_version"], "0.2.0")
        self.assertEqual(summary["resolver_module"], "resolve_bounded_relevance_receipt_v0_min_v2")
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["request_id"], request["bounded_relevance_receipt_request_id"])
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        facts = result["extracted_bounded_relevance_reception_artifact_facts"]
        self.assertEqual(facts["received_relevance_artifact_outcome"], "BOUNDED_RELEVANCE_RECEPTION_RECORDED")
        self.assertEqual(facts["received_relevance_artifact_result_version"], "0.1.0")
        self.assertEqual(facts["received_relevance_artifact_failed_check_count"], 0)
        self.assertEqual(facts["received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(facts["received_relevance_basis_id"], "bounded_relevance_basis_001")
        self.assertEqual(facts["received_relevance_scope_id"], "bounded_relevance_scope_001")
        self.assertEqual(facts["received_carrier_context_id"], "bounded_relevance_signal_carrier_context_001")
        self.assertEqual(facts["received_reception_envelope_id"], "bounded_relevance_reception_envelope_001")
        self.assert_extracted_facts_are_small(result)

        receipt_object = result["receipt_object"]
        self.assert_receipt_object_is_small(result)
        self.assertEqual(receipt_object["receipt_id"], "bounded_relevance_receipt_001")
        self.assertEqual(receipt_object["receipt_type"], "bounded_relevance_receipt")
        self.assertEqual(receipt_object["receipt_version"], "0.2.0")
        self.assertEqual(receipt_object["received_relevance_artifact"], str(artifact_path))
        self.assertEqual(receipt_object["received_relevance_artifact_outcome"], "BOUNDED_RELEVANCE_RECEPTION_RECORDED")
        self.assertEqual(receipt_object["received_relevance_artifact_result_version"], "0.1.0")
        self.assertEqual(receipt_object["received_relevance_artifact_failed_check_count"], 0)
        self.assertEqual(receipt_object["received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(receipt_object["received_relevance_basis_id"], "bounded_relevance_basis_001")
        self.assertEqual(receipt_object["received_relevance_scope_id"], "bounded_relevance_scope_001")
        self.assertEqual(receipt_object["received_carrier_context_id"], "bounded_relevance_signal_carrier_context_001")
        self.assertEqual(receipt_object["received_reception_envelope_id"], "bounded_relevance_reception_envelope_001")
        self.assertNotEqual(receipt_object["received_reception_envelope_id"], "bounded_relevance_reception_envelope_v0")
        self.assertNotEqual(receipt_object["received_reception_envelope_id"], "bounded_runtime_loop_envelope_v0")
        self.assertEqual(receipt_object["receipt_scope"], "INSPECTABLE_RECEIPT_ONLY")
        self.assertIs(receipt_object["does_not_expand_reception"], True)
        self.assert_no_created_posture(result)

        statement = result["bounded_relevance_receipt_statement"]
        for key in (
            "bounded_relevance_receipt_recorded",
            "artifact_values_extracted_from_reception_artifact",
            "declared_extracted_values_correspond",
            "received_relevance_artifact_preserved",
            "received_signal_id_preserved",
            "received_relevance_basis_id_preserved",
            "received_relevance_scope_id_preserved",
            "received_carrier_context_id_preserved",
            "received_reception_envelope_id_preserved",
            "receipt_scope_inspectable_only",
            "receipt_does_not_expand_reception",
            "v1_receipt_artifact_preserved_as_predecessor_evidence",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(statement[key], True, key)
        self.assert_non_claims_canonical_false(result)
        self.assert_bool_fields_are_bool(result)
        self.assert_official_values_preserved(result)

    def test_successful_recorded_result_from_default_artifact_if_present(self) -> None:
        default_artifact = REPO_ROOT / resolver.DEFAULT_RECEIVED_RELEVANCE_ARTIFACT
        if not default_artifact.exists():
            self.skipTest("default bounded relevance reception live artifact is not present")
        request = resolver.build_declared_bounded_relevance_receipt_v0_min_v2_request()
        result = resolver.resolve_bounded_relevance_receipt_v0_min_v2(request)
        summary = resolver.build_bounded_relevance_receipt_v0_min_v2_summary(result)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        facts = result["extracted_bounded_relevance_reception_artifact_facts"]
        self.assertEqual(facts["received_reception_envelope_id"], "bounded_relevance_reception_envelope_001")
        self.assertNotEqual(facts["received_reception_envelope_id"], "bounded_relevance_reception_envelope_v0")
        self.assertEqual(result["receipt_object"]["received_reception_envelope_id"], facts["received_reception_envelope_id"])

    def test_declared_extracted_mismatch_blocks(self) -> None:
        cases = (
            (
                "selected_bounded_relevance_reception_artifact_outcome",
                "BOUNDED_RELEVANCE_RECEPTION_NOT_RECORDED",
                "DECLARED_EXTRACTED_OUTCOME_MISMATCH",
            ),
            ("selected_bounded_relevance_reception_artifact_result_version", "9.9.9", "DECLARED_EXTRACTED_RESULT_VERSION_MISMATCH"),
            ("selected_bounded_relevance_reception_artifact_failed_check_count", 7, "DECLARED_EXTRACTED_FAILED_CHECK_COUNT_MISMATCH"),
            ("selected_bounded_relevance_reception_signal_id", "bounded_relevance_signal_999", "DECLARED_EXTRACTED_SIGNAL_ID_MISMATCH"),
            ("selected_bounded_relevance_reception_basis_id", "bounded_relevance_basis_999", "DECLARED_EXTRACTED_RELEVANCE_BASIS_ID_MISMATCH"),
            ("selected_bounded_relevance_reception_scope_id", "bounded_relevance_scope_999", "DECLARED_EXTRACTED_RELEVANCE_SCOPE_ID_MISMATCH"),
            (
                "selected_bounded_relevance_reception_carrier_context_id",
                "bounded_relevance_signal_carrier_context_999",
                "DECLARED_EXTRACTED_CARRIER_CONTEXT_ID_MISMATCH",
            ),
            (
                "selected_bounded_relevance_reception_envelope_id",
                "bounded_relevance_reception_envelope_v0",
                "DECLARED_EXTRACTED_RECEPTION_ENVELOPE_ID_MISMATCH",
            ),
        )
        for field, value, expected_code in cases:
            with self.subTest(field=field):
                with tempfile.TemporaryDirectory() as tmp:
                    request, _, _ = self.make_request_and_artifact(Path(tmp))
                    request[field] = value
                    result = resolver.resolve_bounded_relevance_receipt_v0_min_v2(request)
                self.assert_blocked_public_and_safe(result)
                self.assertEqual(block_code(result), expected_code)
                self.assertEqual(result["receipt_object"], {})

    def test_extraction_missing_and_ambiguous_blocks(self) -> None:
        cases = (
            ("missing signal", {"bounded_relevance_signal": {}}, "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_MISSING"),
            ("missing basis", {"relevance_basis": {}}, "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_MISSING"),
            ("missing scope", {"relevance_scope": {}}, "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_MISSING"),
            ("missing context", {"relevance_signal_carrier_context": {}}, "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_MISSING"),
            ("missing envelope", {"bounded_relevance_reception_envelope": {}}, "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_MISSING"),
            (
                "ambiguous signal",
                {"other_bounded_relevance_signal": {"signal_id": "bounded_relevance_signal_002"}},
                "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_AMBIGUOUS",
            ),
            (
                "ambiguous basis",
                {"other_relevance_basis": {"basis_id": "bounded_relevance_basis_002"}},
                "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_AMBIGUOUS",
            ),
            (
                "ambiguous scope",
                {"other_relevance_scope": {"scope_id": "bounded_relevance_scope_002"}},
                "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_AMBIGUOUS",
            ),
            (
                "ambiguous context",
                {"other_carrier_context": {"context_id": "bounded_relevance_signal_carrier_context_002"}},
                "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_AMBIGUOUS",
            ),
            (
                "ambiguous envelope",
                {"other_bounded_relevance_reception_envelope": {"envelope_id": "bounded_relevance_reception_envelope_002"}},
                "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_AMBIGUOUS",
            ),
        )
        for name, overrides, expected_code in cases:
            with self.subTest(name=name):
                with tempfile.TemporaryDirectory() as tmp:
                    request, _, _ = self.make_request_and_artifact(Path(tmp), synthetic_reception_artifact(**overrides))
                    result = resolver.resolve_bounded_relevance_receipt_v0_min_v2(request)
                self.assert_blocked_public_and_safe(result)
                self.assert_failed_code_present(result, expected_code)

    def test_critical_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base_request, _, _ = self.make_request_and_artifact(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_bounded_relevance_receipt_v0_min_v2(request)
                    self.assert_blocked_public_and_safe(result)
                    self.assert_failed_code_present(result, "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][key], False)
                    self.assertEqual(result["receipt_object"], {})
                    self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
                    self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
                    self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)

    def test_representative_blocking_behavior(self) -> None:
        def artifact_mutation(**overrides: Any) -> tuple[dict[str, Any], dict[str, Any]]:
            return {}, synthetic_reception_artifact(**overrides)

        cases: tuple[tuple[str, dict[str, Any], dict[str, Any] | list[Any] | str | None], ...] = (
            ("explicit block intent", {"bounded_relevance_receipt_intent": resolver.INTENT_BLOCK}, None),
            ("missing request", {"clear_request": True}, None),
            ("unsupported intent", {"bounded_relevance_receipt_intent": "UNSUPPORTED"}, None),
            ("artifact path missing", {"selected_bounded_relevance_reception_artifact": ""}, None),
            ("artifact unreadable", {"selected_bounded_relevance_reception_artifact": "missing.json"}, None),
            ("artifact JSON array", {}, []),
            ("artifact not recorded", *artifact_mutation(outcome="BOUNDED_RELEVANCE_RECEPTION_NOT_RECORDED")),
            (
                "artifact failed checks present",
                *artifact_mutation(bounded_relevance_reception_metadata={"bounded_relevance_reception_version": "0.1.0", "failed_check_count": 1}),
            ),
            (
                "artifact version not 0.1.0",
                *artifact_mutation(bounded_relevance_reception_metadata={"bounded_relevance_reception_version": "9.9.9", "failed_check_count": 0}),
            ),
            ("missing receipt scope", {"receipt_scope": ""}, None),
            ("receipt scope not inspectable only", {"receipt_scope": "UNBOUNDED"}, None),
            ("receipt expands reception", {"receipt_expands_reception": True}, None),
            ("receipt creates new signal", {"receipt_creates_new_signal": True}, None),
            ("receipt creates new basis", {"receipt_creates_new_relevance_basis": True}, None),
            ("receipt creates new scope", {"receipt_creates_new_relevance_scope": True}, None),
            ("receipt creates new carrier context", {"receipt_creates_new_carrier_context": True}, None),
            ("source transfer occurred", {"source_transfer_occurred": True}, None),
            ("source receipt occurred", {"source_receipt_occurred": True}, None),
            ("reception authorization created", {"reception_authorization_created": True}, None),
            ("source created", {"source_created": True}, None),
            ("authority created", {"authority_created": True}, None),
            ("currentness created", {"currentness_created": True}, None),
            ("truth created", {"truth_created": True}, None),
            ("action created", {"action_created": True}, None),
            ("synchronization created", {"synchronization_created": True}, None),
            ("participation authorized", {"participation_authorized": True}, None),
            ("participant role created", {"participant_role_created": True}, None),
            ("runtime permission created", {"runtime_permission_created": True}, None),
            ("public API created", {"public_api_created": True}, None),
            ("participant-facing interface created", {"participant_facing_interface_created": True}, None),
            ("distributed network behavior created", {"distributed_network_behavior_created": True}, None),
            ("deployment created", {"deployment_created": True}, None),
            ("public release created", {"public_release_created": True}, None),
            ("operation permission created", {"operation_permission_created": True}, None),
            ("broader reusable permission created", {"broader_reusable_permission_created": True}, None),
            ("follow-on work authorized", {"follow_on_work_authorized": True}, None),
            ("artifact existence treated as receipt authority", {"artifact_existence_treated_as_receipt_authority": True}, None),
            ("latest file posture treated as receipt authority", {"latest_file_posture_treated_as_receipt_authority": True}, None),
            ("repo-local availability treated as receipt authority", {"repo_local_availability_treated_as_receipt_authority": True}, None),
            ("hidden repo state used as content", {"hidden_repo_state_used_as_receipt_content": True}, None),
            ("hidden repo state used as authority", {"hidden_repo_state_used_as_receipt_authority": True}, None),
            ("predecessor repaired", {"predecessor_failure_repaired": True}, None),
            ("predecessor hidden", {"predecessor_failure_hidden": True}, None),
            ("predecessor claimed passed", {"predecessor_failure_claimed_passed": True}, None),
            ("v1 artifact not preserved", {"v1_receipt_artifact_preserved_as_predecessor_evidence": False}, None),
            ("consumed request reopened", {"consumed_request_reopened": True}, None),
            ("authorization token reused", {"authorization_token_reused": True}, None),
            ("required non-claim flipped", {"flip_non_claim": "source_created"}, None),
        )
        for name, request_overrides, artifact_value in cases:
            with self.subTest(name=name):
                with tempfile.TemporaryDirectory() as tmp:
                    tmpdir = Path(tmp)
                    if artifact_value is None:
                        request, _, _ = self.make_request_and_artifact(tmpdir)
                    else:
                        artifact_path = write_json(tmpdir / "synthetic_bounded_relevance_reception_result.json", artifact_value)
                        request = clean_request(artifact_path)
                    if request_overrides.pop("clear_request", False):
                        request.clear()
                    flip_key = request_overrides.pop("flip_non_claim", None)
                    request.update(request_overrides)
                    if flip_key:
                        request["declared_non_claims"].pop(flip_key, None)
                    result = resolver.resolve_bounded_relevance_receipt_v0_min_v2(request)
                self.assert_blocked_public_and_safe(result)

        result = resolver.resolve_bounded_relevance_receipt_v0_min_v2("not a mapping")  # type: ignore[arg-type]
        self.assert_blocked_public_and_safe(result)

    def test_missing_or_incomplete_declared_non_claims(self) -> None:
        variants = []
        with tempfile.TemporaryDirectory() as tmp:
            base_request, _, _ = self.make_request_and_artifact(Path(tmp))
            missing_section = copy.deepcopy(base_request)
            missing_section.pop("declared_non_claims")
            variants.append(("missing declared_non_claims", missing_section))
            empty = copy.deepcopy(base_request)
            empty["declared_non_claims"] = {}
            variants.append(("empty declared_non_claims", empty))
            missing_one = copy.deepcopy(base_request)
            missing_one["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])
            variants.append(("missing one non-claim", missing_one))
            string_value = copy.deepcopy(base_request)
            string_value["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[1]] = "false"
            variants.append(("string non-claim", string_value))
            none_value = copy.deepcopy(base_request)
            none_value["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[2]] = None
            variants.append(("none non-claim", none_value))
            for name, request in variants:
                with self.subTest(name=name):
                    result = resolver.resolve_bounded_relevance_receipt_v0_min_v2(request)
                    self.assertIn(result["outcome"], (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))
                    self.assert_public_block_codes(result)
                    self.assert_failed_code_present(result, "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _ = self.make_request_and_artifact(Path(tmp))
            result = resolver.resolve_bounded_relevance_receipt_v0_min_v2(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(result["receipt_object"]["receipt_scope"], "INSPECTABLE_RECEIPT_ONLY")
        for outcome in (
            "BOUNDED_RELEVANCE_RECEIPT_RECORDED",
            "BOUNDED_RELEVANCE_RECEIPT_NOT_RECORDED",
            "BOUNDED_RELEVANCE_RECEIPT_REQUIRES_ADDITIONAL_BASIS",
            "BOUNDED_RELEVANCE_RECEIPT_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        self.assert_official_values_preserved(result)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            artifact = synthetic_reception_artifact()
            for index, key in enumerate(HOSTILE_KEYS):
                artifact[key] = HOSTILE_SENTINELS[index % len(HOSTILE_SENTINELS)]
            artifact_path = write_synthetic_artifact(tmpdir, artifact)
            request = clean_request(artifact_path)
            for index, key in enumerate(HOSTILE_KEYS):
                request[key] = HOSTILE_SENTINELS[index % len(HOSTILE_SENTINELS)]
            before = copy.deepcopy(request)
            result = resolver.resolve_bounded_relevance_receipt_v0_min_v2(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_hostile_sentinels(result)
        self.assert_official_values_preserved(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_extracted_facts_are_small(result)
        self.assert_no_created_posture(result)
        self.assertEqual(request, before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            request, _, _ = self.make_request_and_artifact(tmpdir)
            request_path = write_json(tmpdir / "request.json", request)
            result = resolver.resolve_bounded_relevance_receipt_v0_min_v2_from_path(request_path)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(result["bounded_relevance_receipt_metadata"]["bounded_relevance_receipt_version"], "0.2.0")
            self.assertEqual(result["bounded_relevance_receipt_metadata"]["resolver_module"], "resolve_bounded_relevance_receipt_v0_min_v2")

            malformed_path = tmpdir / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = resolver.resolve_bounded_relevance_receipt_v0_min_v2_from_path(malformed_path)
            self.assert_blocked_public_and_safe(malformed_result)

            array_request_path = write_json(tmpdir / "array_request.json", [])
            array_result = resolver.resolve_bounded_relevance_receipt_v0_min_v2_from_path(array_request_path)
            self.assert_blocked_public_and_safe(array_result)

            missing_result = resolver.resolve_bounded_relevance_receipt_v0_min_v2_from_path(tmpdir / "missing_request.json")
            self.assert_blocked_public_and_safe(missing_result)

            output_root = tmpdir / V2_OUTPUT_ROOT_SEGMENT
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_bounded_relevance_receipt_v0_min_v2_result(result)
                second_path = resolver.write_bounded_relevance_receipt_v0_min_v2_result(result)
            self.assertTrue(first_path.parent.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn("bounded_relevance_receipt_v0_min_v2", str(first_path))
            self.assertNotEqual(first_path.parent.name, V1_OUTPUT_ROOT_SEGMENT)
            forbidden = (
                "bounded_relevance_reception_v0_min/",
                "post_runtime_daemon_runtime_loop/",
                "source-transfer/",
                "source-receipt/",
                "reception/",
                "public-api/",
                "participant-facing-interface/",
                "distributed-network/",
                "deployment/",
                "public-release/",
            )
            for fragment in forbidden:
                self.assertNotIn(fragment, str(first_path))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            artifact = synthetic_reception_artifact()
            artifact["nested_raw"] = {"raw_body": HOSTILE_SENTINELS[0]}
            artifact_before = copy.deepcopy(artifact)
            request, _, _ = self.make_request_and_artifact(tmpdir, artifact)
            request["extra_nested"] = {"hidden_repo_state": HOSTILE_SENTINELS[-1]}
            request_before = copy.deepcopy(request)
            result = resolver.resolve_bounded_relevance_receipt_v0_min_v2(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, request_before)
        self.assertEqual(artifact, artifact_before)
        self.assertEqual(request["declared_non_claims"], request_before["declared_non_claims"])
        self.assertEqual(request["selected_bounded_relevance_reception_artifact"], request_before["selected_bounded_relevance_reception_artifact"])
        self.assertEqual(request["receipt_scope"], request_before["receipt_scope"])

    def test_predecessor_failure_and_v1_preservation(self) -> None:
        v1_artifact = (
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min"
            / "bounded_relevance_receipt_reference_review_001__bounded_relevance_receipt_v0_min_result.json"
        )
        v1_before = None
        if v1_artifact.exists():
            v1_before = (v1_artifact.stat().st_size, v1_artifact.stat().st_mtime_ns)
        with tempfile.TemporaryDirectory() as tmp:
            request, _, _ = self.make_request_and_artifact(Path(tmp))
            result = resolver.resolve_bounded_relevance_receipt_v0_min_v2(request)
            summary = resolver.build_bounded_relevance_receipt_v0_min_v2_summary(result)
            with mock.patch.object(resolver, "OUTPUT_ROOT", Path(tmp) / V2_OUTPUT_ROOT_SEGMENT):
                written = resolver.write_bounded_relevance_receipt_v0_min_v2_result(result)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["v1_receipt_artifact_preserved_as_predecessor_evidence"], True)
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)
        self.assertIn("bounded_relevance_receipt_v0_min_v2", str(written))
        if v1_before is not None:
            self.assertEqual((v1_artifact.stat().st_size, v1_artifact.stat().st_mtime_ns), v1_before)


if __name__ == "__main__":
    unittest.main()
