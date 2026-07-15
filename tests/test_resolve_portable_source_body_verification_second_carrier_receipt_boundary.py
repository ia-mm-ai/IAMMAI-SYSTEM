"""Executable checks for second-carrier receipt-boundary posture only.

This suite is downstream of recorded packet transfer. It verifies that the
resolver can record one future second-carrier receipt step boundary without
creating receipt, receipt artifact, second-carrier execution, external result,
cross-carrier evidence, source transfer, source receipt, reception
authorization, source, authority, currentness, runtime, final completion,
continuation, reusable permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable, Mapping
from unittest.mock import patch


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_portable_source_body_verification_second_carrier_receipt_boundary as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_RECEIPT_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
SELECTED_BASIS_SECTIONS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_SECTIONS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINEL = "RAW_SECOND_CARRIER_RECEIPT_BOUNDARY_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = (
    "HOSTILE_SECOND_CARRIER_RECEIPT_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN"
)
REDACTION_STRINGS = (
    "[bounded-redacted-raw-or-hidden-state]",
    "[bounded-reference-omitted-raw-or-hidden-state]",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_receipt_boundary_metadata",
    "declared_second_carrier_receipt_boundary_question",
    "selected_packet_transfer_basis",
    "selected_packet_transfer_terminal_summary_basis",
    "selected_packet_transfer_boundary_basis",
    "selected_packet_emission_basis",
    "selected_packet_emission_boundary_v2_basis",
    "selected_packet_emission_boundary_v1_predecessor_failure_basis",
    "selected_packet_artifact_basis",
    "selected_packet_boundary_basis",
    "selected_command_success_basis",
    "selected_command_result_v2_basis",
    "selected_output_capture_v2_basis",
    "selected_command_output_report_artifact_basis",
    "selected_command_execution_basis",
    "selected_command_report_lineage_basis",
    "selected_predecessor_failure_basis",
    "selected_evidence_manifest_basis",
    "selected_artifact_containment_basis",
    "selected_portable_verification_basis",
    "second_carrier_receipt_boundary_only_posture",
    "one_future_second_carrier_receipt_step_posture",
    "packet_transfer_basis_preserved_posture",
    "transferred_packet_basis_preserved_posture",
    "packet_transfer_not_receipt_posture",
    "receipt_not_created_posture",
    "receipt_artifact_not_created_posture",
    "receiving_carrier_not_authority_posture",
    "carrier_possession_not_receipt_authority_posture",
    "copy_presence_not_receipt_authority_posture",
    "second_carrier_execution_not_authorized_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "source_transfer_not_authorized_posture",
    "source_receipt_not_created_posture",
    "reception_authorization_not_created_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "final_completion_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_receipt_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "second_carrier_receipt_boundary_scope",
    "second_carrier_receipt_boundary_checks",
    "second_carrier_receipt_boundary_statement",
    "second_carrier_receipt_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_receipt_boundary_summary",
)

TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)

FALSE_NON_CLAIMS_TO_CHECK = (
    "second_carrier_receipt_created",
    "receipt_artifact_created",
    "second_carrier_execution_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_receipt_boundary_treated_as_receipt",
    "second_carrier_receipt_boundary_treated_as_execution",
    "second_carrier_receipt_boundary_treated_as_external_result",
    "second_carrier_receipt_boundary_treated_as_cross_carrier_evidence",
    "second_carrier_receipt_boundary_treated_as_source_transfer",
    "second_carrier_receipt_boundary_treated_as_source_receipt",
    "second_carrier_receipt_boundary_treated_as_reception_authorization",
    "second_carrier_receipt_boundary_treated_as_source",
    "second_carrier_receipt_boundary_treated_as_authority",
    "second_carrier_receipt_boundary_treated_as_currentness",
    "second_carrier_receipt_boundary_treated_as_final_completion",
    "second_carrier_receipt_boundary_treated_as_runtime",
    "second_carrier_receipt_boundary_treated_as_continuation",
    "second_carrier_receipt_boundary_treated_as_reusable_permission",
    "second_carrier_receipt_boundary_treated_as_follow_on_work",
    "receiving_carrier_treated_as_authority",
    "carrier_possession_treated_as_receipt_authority",
    "copy_presence_treated_as_receipt_authority",
    "artifact_existence_treated_as_receipt_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_receipt_authority",
    "hidden_repo_state_used_as_receipt_content",
    "hidden_repo_state_used_as_receipt_authority",
    "source_created",
    "authority_created",
    "currentness_created",
    "final_completion_claimed",
    "runtime_hosting_created",
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "continuation_authorized",
    "reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "another_reception_request_authorized",
    "follow_on_work_authorized",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "consumed_request_reopened",
    "authorization_token_reused",
    "v1_repaired",
    "v1_hidden",
    "v1_claimed_passed",
)

NON_MEANING_FALSE_FIELDS = (
    "second_carrier_received_anything",
    "receipt_artifact_exists",
    "second_carrier_executed_anything",
    "external_result_exists",
    "cross_carrier_evidence_exists",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_exists",
    "source_exists",
    "authority_exists",
    "currentness_exists",
    "final_completion_exists",
    "runtime_exists",
    "deployment_exists",
    "public_release_exists",
    "continuation_authorized",
    "reusable_permission_exists",
    "follow_on_work_authorized",
    "receipt_boundary_became_receipt",
    "receipt_boundary_became_execution",
    "receipt_boundary_became_external_result",
    "receipt_boundary_became_cross_carrier_proof",
    "receipt_boundary_became_source_transfer",
    "receipt_boundary_became_source_receipt",
    "receipt_boundary_became_reception_authorization",
    "receipt_boundary_became_source",
    "receipt_boundary_became_authority",
    "receipt_boundary_became_currentness",
    "transfer_became_receipt",
    "copy_presence_became_receipt",
    "carrier_possession_became_receipt",
    "receiving_carrier_became_authority",
    "transferred_packet_became_source",
    "transferred_packet_became_authority",
    "transferred_packet_became_currentness",
    "artifact_existence_became_receipt_authority",
    "artifact_path_became_currentness",
    "repo_local_availability_became_receipt_authority",
    "hidden_repo_state_became_receipt_authority",
    "v1_packet_emission_boundary_repaired",
    "v1_packet_emission_boundary_hidden",
    "v1_packet_emission_boundary_erased",
    "v1_packet_emission_boundary_claimed_passed",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_RECEIPT_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_INTENT_UNSUPPORTED",
    "PACKET_TRANSFER_BASIS_MISSING",
    "PACKET_TRANSFER_NOT_RECORDED",
    "PACKET_TRANSFER_FAILED_CHECKS_PRESENT",
    "PACKET_TRANSFER_VERSION_NOT_0_1_0",
    "PACKET_TRANSFER_DID_NOT_RECORD_BOUNDED_PACKET_TRANSFER",
    "PACKET_TRANSFER_TREATED_TRANSFER_AS_RECEIPT",
    "PACKET_TRANSFER_TREATED_TRANSFER_AS_EXECUTION",
    "PACKET_TRANSFER_CREATED_SECOND_CARRIER_RECEIPT",
    "PACKET_TRANSFER_AUTHORIZED_SECOND_CARRIER_EXECUTION",
    "PACKET_TRANSFER_CREATED_EXTERNAL_RESULT",
    "PACKET_TRANSFER_CREATED_CROSS_CARRIER_EVIDENCE",
    "PACKET_TRANSFER_USED_HIDDEN_REPO_STATE_AS_RECEIPT_AUTHORITY",
    "PACKET_TRANSFER_TREATED_REPO_LOCAL_AVAILABILITY_AS_RECEIPT_AUTHORITY",
    "PACKET_TRANSFER_TREATED_CARRIER_POSSESSION_AS_RECEIPT_AUTHORITY",
    "PACKET_TRANSFER_TREATED_COPY_PRESENCE_AS_RECEIPT_AUTHORITY",
    "PACKET_TRANSFER_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_TRANSFER",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_RECEIPT",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_EXECUTION",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_SOURCE",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "SECOND_CARRIER_RECEIPT_CREATED",
    "RECEIPT_ARTIFACT_CREATED",
    "SECOND_CARRIER_EXECUTION_CREATED",
    "EXTERNAL_RESULT_CREATED",
    "CROSS_CARRIER_EVIDENCE_CREATED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "FINAL_COMPLETION_CLAIMED",
    "RUNTIME_HOSTING_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "CONTINUATION_AUTHORIZED",
    "REUSABLE_PERMISSION_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "CARRIER_POSSESSION_TREATED_AS_RECEIPT_AUTHORITY",
    "COPY_PRESENCE_TREATED_AS_RECEIPT_AUTHORITY",
    "ARTIFACT_EXISTENCE_TREATED_AS_RECEIPT_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RECEIPT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RECEIPT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RECEIPT_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_RECEIPT_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_RECEIPT_BOUNDARY_SCOPE",
)


def _json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2)


def _make_request(**overrides: Any) -> dict[str, Any]:
    request = (
        resolver.build_declared_portable_source_body_verification_second_carrier_receipt_boundary_request(
            second_carrier_receipt_boundary_request_id=(
                "second_carrier_receipt_boundary_test_request_001"
            )
        )
    )
    request["second_carrier_receipt_boundary_scope"] = sorted(SUPPORTED_SCOPE)
    request["declared_non_claims"] = {
        key: False for key in REQUIRED_FALSE_NON_CLAIMS
    }
    request.update(copy.deepcopy(overrides))
    return request


def _resolve(request: Mapping[str, Any] | None) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_second_carrier_receipt_boundary(
        declared_second_carrier_receipt_boundary_request=request
    )


class SecondCarrierReceiptBoundaryAssertions:
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping):
            code = block.get("block_code")
            if code is not None:
                self.assertIn(code, resolver.BLOCK_CODES)
        checks = result.get("second_carrier_receipt_boundary_checks", [])
        self.assertIsInstance(checks, list)
        for check in checks:
            self.assertIsInstance(check, Mapping)
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES, check)

    def assert_generated_booleans_are_booleans(self, result: Mapping[str, Any]) -> None:
        for section_name in (
            "second_carrier_receipt_boundary_statement",
            "second_carrier_receipt_boundary_non_meaning",
            "non_claims",
        ):
            section = result.get(section_name)
            self.assertIsInstance(section, Mapping)
            for key, value in section.items():
                self.assertIs(type(value), bool, f"{section_name}.{key}")
                self.assertNotIn(value, REDACTION_STRINGS)

        summary = result.get(
            "portable_source_body_verification_second_carrier_receipt_boundary_summary"
        )
        self.assertIsInstance(summary, Mapping)
        for key, value in summary.items():
            if isinstance(value, Mapping):
                for nested_key, nested_value in value.items():
                    if isinstance(nested_value, bool):
                        self.assertIs(type(nested_value), bool, f"{key}.{nested_key}")
                        self.assertNotIn(nested_value, REDACTION_STRINGS)
            elif isinstance(value, bool):
                self.assertIs(type(value), bool, key)
                self.assertNotIn(value, REDACTION_STRINGS)

    def assert_no_raw_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _json_text(result)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)

    def assert_no_later_authority_created(self, result: Mapping[str, Any]) -> None:
        statement = result["second_carrier_receipt_boundary_statement"]
        for key in (
            "receipt_not_created",
            "receipt_artifact_not_created",
            "receiving_carrier_not_authority",
            "carrier_possession_not_receipt_authority",
            "copy_presence_not_receipt_authority",
            "second_carrier_execution_not_authorized",
            "external_result_not_created",
            "cross_carrier_evidence_not_created",
            "source_transfer_not_authorized",
            "source_receipt_not_created",
            "reception_authorization_not_created",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "final_completion_not_created",
            "runtime_not_created",
            "follow_on_work_not_authorized",
            "hidden_repo_state_excluded",
            "hidden_repo_state_not_used_as_receipt_authority",
            "repo_local_availability_not_receipt_authority",
            "raw_full_prior_artifact_body_not_returned",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
        ):
            self.assertIs(statement.get(key), True, key)

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_blocked_safely(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), BLOCKED)
        self.assertIsInstance(result.get("block"), Mapping)
        self.assertIsNotNone(result["block"].get("block_code"))
        self.assert_public_block_codes(result)
        self.assert_no_later_authority_created(result)
        self.assert_generated_booleans_are_booleans(result)


class TestPortableSourceBodyVerificationSecondCarrierReceiptBoundary(
    SecondCarrierReceiptBoundaryAssertions,
    unittest.TestCase,
):
    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_receipt_boundary",
            "resolve_portable_source_body_verification_second_carrier_receipt_boundary_from_path",
            "write_portable_source_body_verification_second_carrier_receipt_boundary_result",
            "build_portable_source_body_verification_second_carrier_receipt_boundary_summary",
            "build_declared_portable_source_body_verification_second_carrier_receipt_boundary_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_CARRIER_RECEIPT_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_receipt_boundary"
            )
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_second_carrier_receipt_boundary_recorded_result(self) -> None:
        request = _make_request()
        original = copy.deepcopy(request)

        result = _resolve(request)

        self.assertEqual(request, original)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"])
        self.assertEqual(
            result["portable_source_body_verification_second_carrier_receipt_boundary_summary"][
                "failed_check_count"
            ],
            0,
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)

        metadata = result[
            "portable_source_body_verification_second_carrier_receipt_boundary_metadata"
        ]
        self.assertEqual(
            metadata[
                "portable_source_body_verification_second_carrier_receipt_boundary_result_version"
            ],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_second_carrier_receipt_boundary",
        )
        self.assertEqual(
            metadata[
                "portable_source_body_verification_second_carrier_receipt_boundary_request_id"
            ],
            request["second_carrier_receipt_boundary_request_id"],
        )

        statement = result["second_carrier_receipt_boundary_statement"]
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(statement.get(key), True, key)

        non_claims = result["non_claims"]
        for key in FALSE_NON_CLAIMS_TO_CHECK:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)

        non_meaning = result["second_carrier_receipt_boundary_non_meaning"]
        for key in NON_MEANING_FALSE_FIELDS:
            self.assertIn(key, non_meaning)
            self.assertIs(non_meaning[key], False, key)

        packet_transfer_basis = result["selected_packet_transfer_basis"]
        self.assertEqual(
            packet_transfer_basis["selected_packet_transfer_result_outcome"],
            resolver.PACKET_TRANSFER_RECORDED,
        )
        self.assertEqual(
            packet_transfer_basis["selected_packet_transfer_result_version"], "0.1.0"
        )
        self.assertEqual(
            packet_transfer_basis["selected_packet_transfer_failed_check_count"], 0
        )

        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_booleans(result)
        self.assert_no_raw_sentinels(result)

    def test_summary_helper_preserves_receipt_boundary_posture(self) -> None:
        request = _make_request()
        result = _resolve(request)
        summary = (
            resolver.build_portable_source_body_verification_second_carrier_receipt_boundary_summary(
                result
            )
        )

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["request_id"], request["second_carrier_receipt_boundary_request_id"]
        )
        self.assertEqual(summary["question"], resolver.CORE_QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)

        for key in (
            "second_carrier_receipt_boundary_recorded",
            "one_future_second_carrier_receipt_step_declared",
            "packet_transfer_basis_preserved",
            "transferred_packet_basis_preserved",
            "packet_transfer_not_receipt",
            "receipt_not_created",
            "receipt_artifact_not_created",
            "receiving_carrier_not_authority",
            "carrier_possession_not_receipt_authority",
            "copy_presence_not_receipt_authority",
            "second_carrier_execution_not_authorized",
            "external_result_not_created",
            "cross_carrier_evidence_not_created",
            "source_transfer_not_authorized",
            "source_receipt_not_created",
            "reception_authorization_not_created",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "final_completion_not_created",
            "runtime_not_created",
            "follow_on_work_not_authorized",
            "hidden_repo_state_excluded",
            "hidden_repo_state_not_used_as_receipt_authority",
            "repo_local_availability_not_receipt_authority",
            "selected_basis_reference_shape_preserved",
            "raw_full_prior_artifact_body_not_returned",
            "no_receipt_execution_external_result_cross_carrier_evidence",
            "no_source_authority_currentness_final_completion_runtime",
            "no_deployment_public_release_follow_on",
            "v1_predecessor_failure_preserved",
            "v1_not_repaired_hidden_or_claimed_passed",
        ):
            self.assertIs(summary[key], True, key)

        self.assertEqual(
            summary["selected_packet_transfer_outcome"], resolver.PACKET_TRANSFER_RECORDED
        )
        self.assertEqual(summary["selected_packet_transfer_version"], "0.1.0")
        self.assertEqual(summary["selected_packet_transfer_failed_check_count"], 0)

        key_non_claims = summary["key_non_claims"]
        for key, value in key_non_claims.items():
            self.assertIs(value, False, key)

    def test_representative_blocking_behavior(self) -> None:
        block_cases: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
            (
                "explicit block intent",
                lambda request: request.update(
                    {"second_carrier_receipt_boundary_intent": resolver.INTENT_BLOCK}
                ),
            ),
            (
                "unsupported intent",
                lambda request: request.update(
                    {"second_carrier_receipt_boundary_intent": "UNSUPPORTED_INTENT"}
                ),
            ),
            (
                "unsupported scope",
                lambda request: request.update(
                    {
                        "second_carrier_receipt_boundary_scope": [
                            "UNSUPPORTED_SCOPE"
                        ]
                    }
                ),
            ),
            (
                "missing packet transfer basis",
                lambda request: request.pop("selected_packet_transfer_basis"),
            ),
            (
                "missing packet transfer terminal summary",
                lambda request: request.pop(
                    "selected_packet_transfer_terminal_summary_basis"
                ),
            ),
            (
                "packet transfer not recorded",
                lambda request: request.update(
                    {"selected_packet_transfer_result_outcome": "NOT_RECORDED"}
                ),
            ),
            (
                "packet transfer failed checks",
                lambda request: request.update(
                    {"selected_packet_transfer_failed_check_count": 1}
                ),
            ),
            (
                "packet transfer version mismatch",
                lambda request: request.update(
                    {"selected_packet_transfer_result_version": "9.9.9"}
                ),
            ),
            (
                "packet transfer did not record bounded packet transfer",
                lambda request: request.update(
                    {
                        "selected_packet_transfer_bounded_packet_transfer_recorded": False
                    }
                ),
            ),
            (
                "packet transfer treated transfer as receipt",
                lambda request: request.update(
                    {"selected_packet_transfer_transfer_not_receipt": False}
                ),
            ),
            (
                "packet transfer treated transfer as execution",
                lambda request: request.update(
                    {"selected_packet_transfer_transfer_not_execution": False}
                ),
            ),
            (
                "packet transfer created second-carrier receipt",
                lambda request: request.update(
                    {"selected_packet_transfer_created_second_carrier_receipt": True}
                ),
            ),
            (
                "packet transfer authorized second-carrier execution",
                lambda request: request.update(
                    {
                        "selected_packet_transfer_authorized_second_carrier_execution": True
                    }
                ),
            ),
            (
                "packet transfer created external result",
                lambda request: request.update(
                    {"selected_packet_transfer_created_external_result": True}
                ),
            ),
            (
                "packet transfer created cross-carrier evidence",
                lambda request: request.update(
                    {"selected_packet_transfer_created_cross_carrier_evidence": True}
                ),
            ),
            (
                "packet transfer used hidden repo state as receipt authority",
                lambda request: request.update(
                    {
                        "selected_packet_transfer_used_hidden_repo_state_as_receipt_authority": True
                    }
                ),
            ),
            (
                "packet transfer treated repo-local availability as receipt authority",
                lambda request: request.update(
                    {
                        "selected_packet_transfer_treated_repo_local_availability_as_receipt_authority": True
                    }
                ),
            ),
            (
                "packet transfer treated carrier possession as receipt authority",
                lambda request: request.update(
                    {
                        "selected_packet_transfer_treated_carrier_possession_as_receipt_authority": True
                    }
                ),
            ),
            (
                "packet transfer treated copy presence as receipt authority",
                lambda request: request.update(
                    {
                        "selected_packet_transfer_treated_copy_presence_as_receipt_authority": True
                    }
                ),
            ),
            (
                "packet transfer returned raw prior body",
                lambda request: request.update(
                    {
                        "selected_packet_transfer_raw_full_prior_artifact_body_returned_outside_bounded_transfer": True
                    }
                ),
            ),
            (
                "selected basis not reference-shaped",
                lambda request: request.update({"reference_shaped_input_posture": False}),
            ),
            (
                "predecessor failure repaired",
                lambda request: request["selected_predecessor_failure_basis"].update(
                    {"v1_repaired": True}
                ),
            ),
            (
                "command report lineage treated as current report artifact",
                lambda request: request["selected_command_report_lineage_basis"].update(
                    {"command_report_lineage_treated_as_current_report_artifact": True}
                ),
            ),
            (
                "command report lineage treated as source",
                lambda request: request["selected_command_report_lineage_basis"].update(
                    {"command_report_lineage_treated_as_source": True}
                ),
            ),
            (
                "command report lineage treated as authority",
                lambda request: request["selected_command_report_lineage_basis"].update(
                    {"command_report_lineage_treated_as_authority": True}
                ),
            ),
            (
                "command report lineage treated as currentness",
                lambda request: request["selected_command_report_lineage_basis"].update(
                    {"command_report_lineage_treated_as_currentness": True}
                ),
            ),
            (
                "full prior body emitted outside bounded receipt-boundary posture",
                lambda request: request.update(
                    {
                        "_forced_block_code": (
                            "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_RECEIPT_BOUNDARY"
                        )
                    }
                ),
            ),
            (
                "artifacts mutated",
                lambda request: request["declared_non_claims"].update(
                    {"prior_artifacts_mutated": True}
                ),
            ),
            (
                "required non-claim missing",
                lambda request: request["declared_non_claims"].pop("source_created"),
            ),
        ]

        for non_claim in REQUIRED_FALSE_NON_CLAIMS:
            block_cases.append(
                (
                    f"required non-claim flipped: {non_claim}",
                    lambda request, key=non_claim: request[
                        "declared_non_claims"
                    ].update({key: True}),
                )
            )

        malformed_results = [
            _resolve(None),
            resolver.resolve_portable_source_body_verification_second_carrier_receipt_boundary(
                declared_second_carrier_receipt_boundary_request=["not", "mapping"]
            ),
        ]
        for result in malformed_results:
            self.assert_blocked_safely(result)

        for label, mutate in block_cases:
            with self.subTest(label=label):
                request = _make_request()
                mutate(request)
                result = _resolve(request)
                self.assert_blocked_safely(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request = _make_request(
                second_carrier_receipt_boundary_request_id="path_write_receipt_boundary"
            )
            request_path = tmp_path / "request.json"
            request_path.write_text(_json_text(request), encoding="utf-8")

            result = (
                resolver.resolve_portable_source_body_verification_second_carrier_receipt_boundary_from_path(
                    request_path
                )
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result[
                "portable_source_body_verification_second_carrier_receipt_boundary_metadata"
            ]
            self.assertEqual(
                metadata[
                    "portable_source_body_verification_second_carrier_receipt_boundary_result_version"
                ],
                "0.1.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_second_carrier_receipt_boundary",
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierReceiptBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_receipt_boundary_from_path(
                    malformed_path
                )

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_portable_source_body_verification_second_carrier_receipt_boundary_from_path(
                    array_path
                )
            )
            self.assert_blocked_safely(array_result)

            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierReceiptBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_receipt_boundary_from_path(
                    tmp_path / "missing.json"
                )

            redirected_root = (
                tmp_path
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_receipt_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", redirected_root):
                first_path = (
                    resolver.write_portable_source_body_verification_second_carrier_receipt_boundary_result(
                        result
                    )
                )
                second_path = (
                    resolver.write_portable_source_body_verification_second_carrier_receipt_boundary_result(
                        result
                    )
                )

            self.assertEqual(first_path.parent, redirected_root)
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(second_path.stem.endswith("_001"))
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)

            output_text = str(first_path)
            self.assertIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_receipt_boundary",
                output_text,
            )
            for forbidden in (
                "packet_transfer/",
                "packet_transfer_boundary/",
                "second_carrier_receipt/",
                "second_carrier_execution/",
                "cross_carrier/",
                "runtime/",
                "deployment/",
                "public_release/",
            ):
                self.assertNotIn(forbidden, output_text)

    def test_non_mutation(self) -> None:
        request = _make_request()
        original = copy.deepcopy(request)

        result = _resolve(request)

        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, original)
        for section in SELECTED_BASIS_SECTIONS + POSTURE_SECTIONS:
            self.assertEqual(request[section], original[section], section)
        self.assertEqual(
            request["second_carrier_receipt_boundary_scope"],
            original["second_carrier_receipt_boundary_scope"],
        )
        self.assertEqual(request["declared_non_claims"], original["declared_non_claims"])

    def test_raw_full_body_hidden_repo_state_containment(self) -> None:
        request = _make_request()
        hostile_payload = {
            "raw_body": HOSTILE_RAW_VALUE,
            "raw_full_body": HOSTILE_RAW_VALUE,
            "full_body": HOSTILE_RAW_VALUE,
            "artifact_body": HOSTILE_RAW_VALUE,
            "raw_result_body": HOSTILE_RAW_VALUE,
            "raw_output_body": HOSTILE_RAW_VALUE,
            "receipt_body": HOSTILE_RAW_VALUE,
            "receipt_artifact_body": HOSTILE_RAW_VALUE,
            "execution_body": HOSTILE_RAW_VALUE,
            "external_result_body": HOSTILE_RAW_VALUE,
            "cross_carrier_evidence_body": HOSTILE_RAW_VALUE,
            "packet_body": HOSTILE_RAW_VALUE,
            "source_body": HOSTILE_RAW_VALUE,
            "authority_body": HOSTILE_RAW_VALUE,
            "hidden_repo_state": HOSTILE_RAW_VALUE,
            "current_working_tree": HOSTILE_RAW_VALUE,
            "local_cache": HOSTILE_RAW_VALUE,
            "repo_local_only_dependency": HOSTILE_RAW_VALUE,
            "carrier_possession": HOSTILE_RAW_VALUE,
            "copy_presence": HOSTILE_RAW_VALUE,
            "receiving_carrier": HOSTILE_RAW_VALUE,
            "unlisted_file_dependency": HOSTILE_RAW_VALUE,
            "nested": [{"sentinel": RAW_SENTINEL, "value": HOSTILE_RAW_VALUE}],
        }
        for section in (
            "selected_packet_transfer_basis",
            "selected_packet_transfer_boundary_basis",
            "selected_packet_emission_basis",
            "selected_packet_emission_boundary_v2_basis",
            "selected_packet_artifact_basis",
            "selected_packet_boundary_basis",
            "selected_command_success_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        ):
            request[section]["hostile_reference_payload"] = copy.deepcopy(
                hostile_payload
            )
        original = copy.deepcopy(request)

        result = _resolve(request)

        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertEqual(request, original)
        self.assert_public_block_codes(result)
        self.assert_no_raw_sentinels(result)
        self.assert_no_later_authority_created(result)
        self.assert_generated_booleans_are_booleans(result)


if __name__ == "__main__":
    unittest.main()
