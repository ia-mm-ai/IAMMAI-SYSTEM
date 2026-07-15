"""Tests for portable source-body verification second-carrier receipt only.

This suite is downstream of the recorded second-carrier receipt boundary. It
verifies that the resolver records one bounded receipt posture only: receipt is
not second-carrier execution, external result, cross-carrier proof, source
transfer, source receipt, reception authorization, source, authority,
currentness, runtime, final completion, continuation, reusable permission, or
follow-on work. Receiving carrier, carrier possession, and copy presence remain
non-authoritative, hidden repo state is excluded, repo-local availability is
not receipt authority, selected basis remains reference-shaped, the consumed
request token remains closed, and authorization token reuse remains blocked.
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

import resolve_portable_source_body_verification_second_carrier_receipt as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINEL = "RAW_SECOND_CARRIER_RECEIPT_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_SECOND_CARRIER_RECEIPT_FULL_BODY_VALUE_MUST_NOT_RETURN"
REDACTION_STRINGS = {
    "[bounded-redacted-raw-or-hidden-state]",
    "[bounded-reference-omitted-raw-or-hidden-state]",
}

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_receipt_metadata",
    "declared_second_carrier_receipt_question",
    "selected_second_carrier_receipt_boundary_basis",
    "selected_second_carrier_receipt_boundary_terminal_summary_basis",
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
    "second_carrier_receipt_spec_only_posture",
    "one_bounded_second_carrier_receipt_posture",
    "second_carrier_receipt_boundary_basis_preserved_posture",
    "packet_transfer_basis_preserved_posture",
    "transferred_packet_basis_preserved_posture",
    "receipt_recorded_bounded_posture",
    "receipt_artifact_recorded_or_bounded_posture",
    "receipt_not_execution_posture",
    "receipt_not_external_result_posture",
    "receipt_not_cross_carrier_evidence_posture",
    "receiving_carrier_not_authority_posture",
    "carrier_possession_not_authority_posture",
    "copy_presence_not_authority_posture",
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
    "second_carrier_receipt_scope",
    "second_carrier_receipt_checks",
    "second_carrier_receipt_statement",
    "second_carrier_receipt_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_receipt_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_RECEIPT_QUESTION_UNDECLARED",
    "SECOND_CARRIER_RECEIPT_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_NOT_RECORDED",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_DID_NOT_DECLARE_FUTURE_RECEIPT_STEP",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_ALREADY_CREATED_RECEIPT",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_ALREADY_CREATED_RECEIPT_ARTIFACT",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_AUTHORIZED_SECOND_CARRIER_EXECUTION",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_RECEIPT_AUTHORITY",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_RECEIPT_AUTHORITY",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_CARRIER_POSSESSION_AS_RECEIPT_AUTHORITY",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_COPY_PRESENCE_AS_RECEIPT_AUTHORITY",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
    "PACKET_TRANSFER_BASIS_MISSING",
    "PACKET_TRANSFER_NOT_RECORDED",
    "PACKET_TRANSFER_FAILED_CHECKS_PRESENT",
    "PACKET_TRANSFER_DID_NOT_RECORD_BOUNDED_PACKET_TRANSFER",
    "PACKET_TRANSFER_TREATED_TRANSFER_AS_RECEIPT",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_EXECUTION",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_RECEIPT_TREATED_AS_FOLLOW_ON_WORK",
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
    "CARRIER_POSSESSION_TREATED_AS_AUTHORITY",
    "COPY_PRESENCE_TREATED_AS_AUTHORITY",
    "ARTIFACT_EXISTENCE_TREATED_AS_RECEIPT_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RECEIPT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RECEIPT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RECEIPT_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_RECEIPT",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE",
)

NON_MEANING_FALSE_FIELDS = (
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
    "receipt_became_execution",
    "receipt_became_external_result",
    "receipt_became_cross_carrier_proof",
    "receipt_became_source_transfer",
    "receipt_became_source_receipt",
    "receipt_became_reception_authorization",
    "receipt_became_source",
    "receipt_became_authority",
    "receipt_became_currentness",
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


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = (
        resolver.build_declared_portable_source_body_verification_second_carrier_receipt_request(
            "second_carrier_receipt_test_request_001"
        )
    )
    request["second_carrier_receipt_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = _false_non_claims()
    request.update(copy.deepcopy(overrides))
    return request


def _with_non_claim(key: str, value: bool = True) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"][key] = value

    return mutate


def _with_top_level(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[key] = value

    return mutate


def _with_basis_flag(
    basis_key: str,
    key: str,
    value: Any,
) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[basis_key][key] = value

    return mutate


class SecondCarrierReceiptResolverTest(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping):
            block_code = block.get("block_code")
            if block_code is not None:
                self.assertIn(block_code, resolver.BLOCK_CODES)

        for check in result.get("second_carrier_receipt_checks", []):
            if not isinstance(check, Mapping):
                continue
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_boolean_fields(self, result: Mapping[str, Any]) -> None:
        for section_name in (
            "second_carrier_receipt_statement",
            "second_carrier_receipt_non_meaning",
            "non_claims",
        ):
            section = result.get(section_name)
            self.assertIsInstance(section, dict)
            for key, value in section.items():
                with self.subTest(section=section_name, key=key):
                    self.assertIsInstance(value, bool)
                    self.assertNotIn(value, REDACTION_STRINGS)

        summary = result.get("portable_source_body_verification_second_carrier_receipt_summary")
        self.assertIsInstance(summary, dict)
        for key, value in summary.items():
            if isinstance(value, bool):
                self.assertIsInstance(value, bool)
                self.assertNotIn(value, REDACTION_STRINGS)
        key_non_claims = summary.get("key_non_claims", {})
        self.assertIsInstance(key_non_claims, dict)
        for key, value in key_non_claims.items():
            with self.subTest(summary_non_claim=key):
                self.assertIsInstance(value, bool)
                self.assertNotIn(value, REDACTION_STRINGS)

    def assert_no_raw_or_hidden_sentinels(
        self,
        result: Mapping[str, Any],
        *extra_sentinels: str,
    ) -> None:
        serialized = _json_text(result)
        for sentinel in (RAW_SENTINEL, HOSTILE_RAW_VALUE, *extra_sentinels):
            self.assertNotIn(sentinel, serialized)

    def assert_no_later_authority_created(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims", {})
        self.assertIsInstance(non_claims, dict)
        for key in (
            "second_carrier_execution_created",
            "external_result_created",
            "cross_carrier_evidence_created",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
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
            "follow_on_work_authorized",
            "consumed_request_reopened",
            "authorization_token_reused",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
        ):
            with self.subTest(no_later_claim=key):
                self.assertIs(non_claims.get(key), False)

    def assert_recorded_receipt_result(
        self,
        result: Mapping[str, Any],
        request: Mapping[str, Any],
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get("outcome"), RECORDED)
        self.assertIsNone(result.get("block"))
        for section in TOP_LEVEL_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, result)

        metadata = result["portable_source_body_verification_second_carrier_receipt_metadata"]
        self.assertEqual(
            metadata["portable_source_body_verification_second_carrier_receipt_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_second_carrier_receipt",
        )
        self.assertEqual(
            metadata["portable_source_body_verification_second_carrier_receipt_request_id"],
            request["second_carrier_receipt_request_id"],
        )

        summary = result["portable_source_body_verification_second_carrier_receipt_summary"]
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)

        statement = result["second_carrier_receipt_statement"]
        for key in TRUE_RECORDED_FIELDS:
            with self.subTest(statement_true=key):
                self.assertIs(statement.get(key), True)

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim_false=key):
                self.assertIn(key, non_claims)
                self.assertIs(non_claims[key], False)

        non_meaning = result["second_carrier_receipt_non_meaning"]
        for key in NON_MEANING_FALSE_FIELDS:
            with self.subTest(non_meaning_false=key):
                self.assertIn(key, non_meaning)
                self.assertIs(non_meaning[key], False)

        boundary_basis = result["selected_second_carrier_receipt_boundary_basis"]
        self.assertEqual(
            boundary_basis["selected_second_carrier_receipt_boundary_result_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            boundary_basis["selected_second_carrier_receipt_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            boundary_basis["selected_second_carrier_receipt_boundary_failed_check_count"],
            0,
        )
        packet_transfer_basis = result["selected_packet_transfer_basis"]
        self.assertEqual(
            packet_transfer_basis["selected_packet_transfer_result_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_RECORDED",
        )
        self.assertEqual(packet_transfer_basis["selected_packet_transfer_failed_check_count"], 0)
        self.assertIs(
            packet_transfer_basis["selected_packet_transfer_bounded_packet_transfer_recorded"],
            True,
        )
        self.assertIs(packet_transfer_basis["selected_packet_transfer_transfer_not_receipt"], True)

        remains_open = result["what_remains_open"]
        self.assertIs(remains_open["open_means_not_scheduled"], True)
        self.assertIs(remains_open["open_means_not_authorized"], True)
        self.assertIs(remains_open["open_means_not_executed"], True)
        self.assertIn("second-device / second-carrier execution", remains_open["open_items"])

        self.assert_public_block_codes(result)
        self.assert_generated_boolean_fields(result)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_no_later_authority_created(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_receipt",
            "resolve_portable_source_body_verification_second_carrier_receipt_from_path",
            "write_portable_source_body_verification_second_carrier_receipt_result",
            "build_portable_source_body_verification_second_carrier_receipt_summary",
            "build_declared_portable_source_body_verification_second_carrier_receipt_request",
        ):
            with self.subTest(public_api=name):
                self.assertTrue(hasattr(resolver, name))
                self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            with self.subTest(constant=name):
                self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_receipt"
            )
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            with self.subTest(block_code=code):
                self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_second_carrier_receipt_recorded_result(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_second_carrier_receipt(
            declared_second_carrier_receipt_request=request
        )

        self.assertEqual(request, original)
        self.assert_recorded_receipt_result(result, request)

    def test_summary_helper_preserves_receipt_posture(self) -> None:
        request = _valid_request()
        result = resolver.resolve_portable_source_body_verification_second_carrier_receipt(
            declared_second_carrier_receipt_request=request
        )
        summary = resolver.build_portable_source_body_verification_second_carrier_receipt_summary(
            result
        )

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["request_id"], request["second_carrier_receipt_request_id"])
        self.assertEqual(summary["question"], request["second_carrier_receipt_question"])
        self.assertEqual(summary["intent"], request["second_carrier_receipt_intent"])
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)

        for key in TRUE_RECORDED_FIELDS:
            if key in summary:
                with self.subTest(summary_true=key):
                    self.assertIs(summary[key], True)

        self.assertIs(summary["no_execution_external_result_cross_carrier_evidence"], True)
        self.assertIs(summary["no_source_authority_currentness_final_completion_runtime"], True)
        self.assertIs(summary["no_deployment_public_release_follow_on"], True)
        self.assertEqual(
            summary["selected_second_carrier_receipt_boundary_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_BOUNDARY_RECORDED",
        )
        self.assertEqual(summary["selected_second_carrier_receipt_boundary_version"], "0.1.0")
        self.assertEqual(summary["selected_second_carrier_receipt_boundary_failed_check_count"], 0)
        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_not_repaired_hidden_or_claimed_passed"], True)

        key_non_claims = summary["key_non_claims"]
        for key, value in key_non_claims.items():
            with self.subTest(summary_non_claim=key):
                self.assertIs(value, False)

    def test_representative_blocking_behavior(self) -> None:
        malformed_results = (
            resolver.resolve_portable_source_body_verification_second_carrier_receipt(),
            resolver.resolve_portable_source_body_verification_second_carrier_receipt(
                declared_second_carrier_receipt_request=["not", "a", "mapping"]
            ),
        )
        for result in malformed_results:
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
            self.assert_public_block_codes(result)
            self.assert_no_later_authority_created(result)

        cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str], ...] = (
            (
                "explicit block intent",
                _with_top_level("second_carrier_receipt_intent", resolver.INTENT_BLOCK),
                "SECOND_CARRIER_RECEIPT_BLOCK_REQUESTED",
            ),
            (
                "unsupported intent",
                _with_top_level("second_carrier_receipt_intent", "UNSUPPORTED_RECEIPT_INTENT"),
                "SECOND_CARRIER_RECEIPT_INTENT_UNSUPPORTED",
            ),
            (
                "unsupported scope",
                _with_top_level(
                    "second_carrier_receipt_scope",
                    list(SUPPORTED_SCOPE) + ["UNSUPPORTED_SCOPE"],
                ),
                "UNSUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE",
            ),
            (
                "missing second-carrier receipt boundary basis",
                lambda request: request.pop("selected_second_carrier_receipt_boundary_basis"),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_BASIS_MISSING",
            ),
            (
                "second-carrier receipt boundary not recorded",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_result_outcome",
                    "NOT_RECORDED",
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_NOT_RECORDED",
            ),
            (
                "second-carrier receipt boundary failed checks",
                _with_top_level("selected_second_carrier_receipt_boundary_failed_check_count", 1),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_FAILED_CHECKS_PRESENT",
            ),
            (
                "second-carrier receipt boundary version mismatch",
                _with_top_level("selected_second_carrier_receipt_boundary_result_version", "9.9.9"),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_VERSION_NOT_0_1_0",
            ),
            (
                "second-carrier receipt boundary missing future step",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_declared_future_receipt_step",
                    False,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_DID_NOT_DECLARE_FUTURE_RECEIPT_STEP",
            ),
            (
                "second-carrier receipt boundary already created receipt",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_already_created_receipt",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_ALREADY_CREATED_RECEIPT",
            ),
            (
                "second-carrier receipt boundary already created receipt artifact",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_already_created_receipt_artifact",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_ALREADY_CREATED_RECEIPT_ARTIFACT",
            ),
            (
                "second-carrier receipt boundary authorized execution",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_authorized_second_carrier_execution",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_AUTHORIZED_SECOND_CARRIER_EXECUTION",
            ),
            (
                "second-carrier receipt boundary created external result",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_created_external_result",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_CREATED_EXTERNAL_RESULT",
            ),
            (
                "second-carrier receipt boundary created cross-carrier evidence",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_created_cross_carrier_evidence",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
            ),
            (
                "second-carrier receipt boundary used hidden repo state",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_used_hidden_repo_state_as_receipt_authority",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_RECEIPT_AUTHORITY",
            ),
            (
                "second-carrier receipt boundary treated repo-local availability as authority",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_treated_repo_local_availability_as_receipt_authority",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_RECEIPT_AUTHORITY",
            ),
            (
                "second-carrier receipt boundary treated carrier possession as authority",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_treated_carrier_possession_as_receipt_authority",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_CARRIER_POSSESSION_AS_RECEIPT_AUTHORITY",
            ),
            (
                "second-carrier receipt boundary treated copy presence as authority",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_treated_copy_presence_as_receipt_authority",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_COPY_PRESENCE_AS_RECEIPT_AUTHORITY",
            ),
            (
                "second-carrier receipt boundary treated receiving carrier as authority",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_treated_receiving_carrier_as_authority",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
            ),
            (
                "second-carrier receipt boundary returned raw full prior artifact body",
                _with_top_level(
                    "selected_second_carrier_receipt_boundary_raw_full_prior_artifact_body_returned",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
            ),
            (
                "packet transfer basis missing",
                lambda request: request.pop("selected_packet_transfer_basis"),
                "PACKET_TRANSFER_BASIS_MISSING",
            ),
            (
                "packet transfer not recorded",
                _with_top_level("selected_packet_transfer_result_outcome", "NOT_RECORDED"),
                "PACKET_TRANSFER_NOT_RECORDED",
            ),
            (
                "packet transfer failed checks",
                _with_top_level("selected_packet_transfer_failed_check_count", 1),
                "PACKET_TRANSFER_FAILED_CHECKS_PRESENT",
            ),
            (
                "packet transfer did not record bounded transfer",
                _with_top_level("selected_packet_transfer_bounded_packet_transfer_recorded", False),
                "PACKET_TRANSFER_DID_NOT_RECORD_BOUNDED_PACKET_TRANSFER",
            ),
            (
                "packet transfer treated transfer as receipt",
                _with_top_level("selected_packet_transfer_transfer_not_receipt", False),
                "PACKET_TRANSFER_TREATED_TRANSFER_AS_RECEIPT",
            ),
            (
                "receipt treated as execution",
                _with_non_claim("second_carrier_receipt_treated_as_execution"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_EXECUTION",
            ),
            (
                "receipt treated as external result",
                _with_non_claim("second_carrier_receipt_treated_as_external_result"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_EXTERNAL_RESULT",
            ),
            (
                "receipt treated as cross-carrier evidence",
                _with_non_claim("second_carrier_receipt_treated_as_cross_carrier_evidence"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
            ),
            (
                "receipt treated as source transfer",
                _with_non_claim("second_carrier_receipt_treated_as_source_transfer"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE_TRANSFER",
            ),
            (
                "receipt treated as source receipt",
                _with_non_claim("second_carrier_receipt_treated_as_source_receipt"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE_RECEIPT",
            ),
            (
                "receipt treated as reception authorization",
                _with_non_claim("second_carrier_receipt_treated_as_reception_authorization"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_RECEPTION_AUTHORIZATION",
            ),
            (
                "receipt treated as source",
                _with_non_claim("second_carrier_receipt_treated_as_source"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE",
            ),
            (
                "receipt treated as authority",
                _with_non_claim("second_carrier_receipt_treated_as_authority"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_AUTHORITY",
            ),
            (
                "receipt treated as currentness",
                _with_non_claim("second_carrier_receipt_treated_as_currentness"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_CURRENTNESS",
            ),
            (
                "receipt treated as final completion",
                _with_non_claim("second_carrier_receipt_treated_as_final_completion"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_FINAL_COMPLETION",
            ),
            (
                "receipt treated as runtime",
                _with_non_claim("second_carrier_receipt_treated_as_runtime"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_RUNTIME",
            ),
            (
                "receipt treated as continuation",
                _with_non_claim("second_carrier_receipt_treated_as_continuation"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_CONTINUATION",
            ),
            (
                "receipt treated as reusable permission",
                _with_non_claim("second_carrier_receipt_treated_as_reusable_permission"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_REUSABLE_PERMISSION",
            ),
            (
                "receipt treated as follow-on",
                _with_non_claim("second_carrier_receipt_treated_as_follow_on_work"),
                "SECOND_CARRIER_RECEIPT_TREATED_AS_FOLLOW_ON_WORK",
            ),
            (
                "second-carrier execution created",
                _with_non_claim("second_carrier_execution_created"),
                "SECOND_CARRIER_EXECUTION_CREATED",
            ),
            ("external result created", _with_non_claim("external_result_created"), "EXTERNAL_RESULT_CREATED"),
            (
                "cross-carrier evidence created",
                _with_non_claim("cross_carrier_evidence_created"),
                "CROSS_CARRIER_EVIDENCE_CREATED",
            ),
            (
                "source transfer occurred",
                _with_non_claim("source_transfer_occurred"),
                "SOURCE_TRANSFER_OCCURRED",
            ),
            (
                "source receipt occurred",
                _with_non_claim("source_receipt_occurred"),
                "SOURCE_RECEIPT_OCCURRED",
            ),
            (
                "reception authorization created",
                _with_non_claim("reception_authorization_created"),
                "RECEPTION_AUTHORIZATION_CREATED",
            ),
            ("source created", _with_non_claim("source_created"), "SOURCE_CREATED"),
            ("authority created", _with_non_claim("authority_created"), "AUTHORITY_CREATED"),
            ("currentness created", _with_non_claim("currentness_created"), "CURRENTNESS_CREATED"),
            (
                "final completion claimed",
                _with_non_claim("final_completion_claimed"),
                "FINAL_COMPLETION_CLAIMED",
            ),
            (
                "runtime hosting created",
                _with_non_claim("runtime_hosting_created"),
                "RUNTIME_HOSTING_CREATED",
            ),
            ("deployment created", _with_non_claim("deployment_created"), "DEPLOYMENT_CREATED"),
            (
                "public release created",
                _with_non_claim("public_release_created"),
                "PUBLIC_RELEASE_CREATED",
            ),
            (
                "operation permission created",
                _with_non_claim("operation_permission_created"),
                "OPERATION_PERMISSION_CREATED",
            ),
            (
                "continuation authorized",
                _with_non_claim("continuation_authorized"),
                "CONTINUATION_AUTHORIZED",
            ),
            (
                "reusable permission created",
                _with_non_claim("reusable_permission_created"),
                "REUSABLE_PERMISSION_CREATED",
            ),
            (
                "follow-on work authorized",
                _with_non_claim("follow_on_work_authorized"),
                "FOLLOW_ON_WORK_AUTHORIZED",
            ),
            (
                "receiving carrier treated as authority",
                _with_non_claim("receiving_carrier_treated_as_authority"),
                "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
            ),
            (
                "carrier possession treated as authority",
                _with_non_claim("carrier_possession_treated_as_authority"),
                "CARRIER_POSSESSION_TREATED_AS_AUTHORITY",
            ),
            (
                "copy presence treated as authority",
                _with_non_claim("copy_presence_treated_as_authority"),
                "COPY_PRESENCE_TREATED_AS_AUTHORITY",
            ),
            (
                "artifact existence treated as receipt authority",
                _with_non_claim("artifact_existence_treated_as_receipt_authority"),
                "ARTIFACT_EXISTENCE_TREATED_AS_RECEIPT_AUTHORITY",
            ),
            (
                "artifact path treated as currentness",
                _with_non_claim("artifact_path_treated_as_currentness"),
                "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
            ),
            (
                "repo-local availability treated as receipt authority",
                _with_non_claim("repo_local_availability_treated_as_receipt_authority"),
                "REPO_LOCAL_AVAILABILITY_TREATED_AS_RECEIPT_AUTHORITY",
            ),
            (
                "hidden repo state used as receipt content",
                _with_non_claim("hidden_repo_state_used_as_receipt_content"),
                "HIDDEN_REPO_STATE_USED_AS_RECEIPT_CONTENT",
            ),
            (
                "hidden repo state used as receipt authority",
                _with_non_claim("hidden_repo_state_used_as_receipt_authority"),
                "HIDDEN_REPO_STATE_USED_AS_RECEIPT_AUTHORITY",
            ),
            (
                "selected basis not reference-shaped",
                _with_top_level("reference_shaped_input_posture", False),
                "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
            ),
            (
                "raw full prior artifact body returned",
                _with_non_claim("raw_full_prior_artifact_body_returned"),
                "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
            ),
            (
                "predecessor failure repaired",
                _with_basis_flag("selected_predecessor_failure_basis", "v1_repaired", True),
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
            (
                "predecessor failure hidden",
                _with_basis_flag("selected_predecessor_failure_basis", "v1_hidden", True),
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
            (
                "predecessor failure claimed passed",
                _with_basis_flag("selected_predecessor_failure_basis", "v1_claimed_passed", True),
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
            (
                "command report lineage treated as current report artifact",
                _with_basis_flag(
                    "selected_command_report_lineage_basis",
                    "command_report_lineage_treated_as_current_report_artifact",
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
            ),
            (
                "command report lineage treated as source",
                _with_basis_flag(
                    "selected_command_report_lineage_basis",
                    "command_report_lineage_treated_as_source",
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
            ),
            (
                "command report lineage treated as authority",
                _with_basis_flag(
                    "selected_command_report_lineage_basis",
                    "command_report_lineage_treated_as_authority",
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
            ),
            (
                "command report lineage treated as currentness",
                _with_basis_flag(
                    "selected_command_report_lineage_basis",
                    "command_report_lineage_treated_as_currentness",
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
            ),
            (
                "consumed request reopened",
                _with_non_claim("consumed_request_reopened"),
                "CONSUMED_REQUEST_REOPENED",
            ),
            (
                "authorization token reused",
                _with_non_claim("authorization_token_reused"),
                "AUTHORIZATION_TOKEN_REUSED",
            ),
            (
                "full prior artifact body emitted outside bounded receipt",
                _with_top_level("full_prior_artifact_body_emitted_outside_bounded_receipt", True),
                "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_RECEIPT",
            ),
            (
                "artifacts mutated",
                _with_non_claim("prior_artifacts_mutated"),
                "ARTIFACTS_MUTATED",
            ),
            (
                "required non-claim missing",
                lambda request: request["declared_non_claims"].pop("source_created"),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        )

        for name, mutate, expected_code in cases:
            with self.subTest(block_case=name):
                request = _valid_request()
                mutate(request)
                result = resolver.resolve_portable_source_body_verification_second_carrier_receipt(
                    declared_second_carrier_receipt_request=request
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIsInstance(result["block"], dict)
                self.assertEqual(result["block"]["block_code"], expected_code)
                self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
                self.assert_public_block_codes(result)
                self.assert_generated_boolean_fields(result)
                self.assert_no_later_authority_created(result)

    def test_path_and_write_behavior(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            request_path = tmp / "declared_second_carrier_receipt_request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_second_carrier_receipt_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result["portable_source_body_verification_second_carrier_receipt_metadata"]
            self.assertEqual(
                metadata["portable_source_body_verification_second_carrier_receipt_result_version"],
                "0.1.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_second_carrier_receipt",
            )

            malformed_path = tmp / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationSecondCarrierReceiptError):
                resolver.resolve_portable_source_body_verification_second_carrier_receipt_from_path(
                    malformed_path
                )

            array_path = tmp / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_portable_source_body_verification_second_carrier_receipt_from_path(
                    array_path
                )
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assert_public_block_codes(array_result)

            with self.assertRaises(resolver.PortableSourceBodyVerificationSecondCarrierReceiptError):
                resolver.resolve_portable_source_body_verification_second_carrier_receipt_from_path(
                    tmp / "missing.json"
                )

            redirected_root = (
                tmp
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_receipt"
            )
            with patch.object(resolver, "OUTPUT_ROOT", redirected_root):
                written = resolver.write_portable_source_body_verification_second_carrier_receipt_result(
                    result
                )
                second_written = (
                    resolver.write_portable_source_body_verification_second_carrier_receipt_result(
                        result
                    )
                )

            self.assertEqual(written.parent, redirected_root)
            self.assertTrue(written.exists())
            self.assertTrue(second_written.exists())
            self.assertNotEqual(written, second_written)
            self.assertEqual(second_written.stem[-4:], "_001")
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            self.assertIn(
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_receipt",
                written.as_posix(),
            )
            forbidden_roots = (
                "second_carrier_receipt_boundary",
                "second_carrier_execution",
                "external_result",
                "cross_carrier",
                "runtime",
                "deployment",
                "public_release",
            )
            for forbidden in forbidden_roots:
                with self.subTest(forbidden_root=forbidden):
                    self.assertNotIn(forbidden, written.as_posix())

    def test_resolver_does_not_mutate_request_or_basis(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_second_carrier_receipt(
            declared_second_carrier_receipt_request=request
        )

        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, original)
        for key in SELECTED_BASIS_KEYS + POSTURE_KEYS:
            with self.subTest(unmutated_section=key):
                self.assertEqual(request[key], original[key])
        self.assertEqual(request["second_carrier_receipt_scope"], original["second_carrier_receipt_scope"])
        self.assertEqual(request["declared_non_claims"], original["declared_non_claims"])

    def test_raw_full_body_and_hidden_repo_state_containment(self) -> None:
        request = _valid_request()
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
            "receipt_artifact_presence": HOSTILE_RAW_VALUE,
            "unlisted_file_dependency": HOSTILE_RAW_VALUE,
            "nested": {"sentinel": RAW_SENTINEL, "values": [RAW_SENTINEL]},
        }
        for key in (
            "selected_second_carrier_receipt_boundary_basis",
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
            request[key]["hostile_containment_probe"] = copy.deepcopy(hostile_payload)

        original = copy.deepcopy(request)
        result = resolver.resolve_portable_source_body_verification_second_carrier_receipt(
            declared_second_carrier_receipt_request=request
        )

        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        if result["block"]:
            self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
        self.assert_public_block_codes(result)
        self.assert_no_raw_or_hidden_sentinels(result, RAW_SENTINEL, HOSTILE_RAW_VALUE)
        self.assert_no_later_authority_created(result)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_receipt_content"], False)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_receipt_authority"], False)
        self.assertIs(
            result["non_claims"]["repo_local_availability_treated_as_receipt_authority"],
            False,
        )
        self.assertIs(result["non_claims"]["carrier_possession_treated_as_authority"], False)
        self.assertIs(result["non_claims"]["copy_presence_treated_as_authority"], False)
        self.assertIs(result["non_claims"]["receiving_carrier_treated_as_authority"], False)
        self.assertEqual(request, original)
        self.assert_generated_boolean_fields(result)


if __name__ == "__main__":
    unittest.main()
