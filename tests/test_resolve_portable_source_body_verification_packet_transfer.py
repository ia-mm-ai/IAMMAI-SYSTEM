"""Executable checks for bounded packet-transfer posture only.

This suite is downstream of recorded packet-transfer-boundary posture. It
verifies one bounded transfer/copy posture without creating second-carrier
receipt, second-carrier execution, external result, cross-carrier proof, source
transfer, source receipt, reception authorization, source, authority,
currentness, runtime, final completion, continuation, reusable permission, or
follow-on work. Carrier possession and copy presence remain non-receipt
authority, hidden repo state remains excluded, selected basis stays
reference-shaped, the consumed request token remains closed, and authorization
token reuse remains blocked.
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

import resolve_portable_source_body_verification_packet_transfer as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_PACKET_TRANSFER_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
POSTURE_SECTIONS = tuple(getattr(resolver, "POSTURE_KEYS", ()))

RAW_SENTINEL = "RAW_PACKET_TRANSFER_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_PACKET_TRANSFER_FULL_BODY_VALUE_MUST_NOT_RETURN"
REDACTION_STRINGS = (
    "[bounded-redacted-raw-or-hidden-state]",
    "[bounded-reference-omitted-raw-or-hidden-state]",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_packet_transfer_metadata",
    "declared_packet_transfer_question",
    "selected_packet_transfer_boundary_basis",
    "selected_packet_transfer_boundary_terminal_summary_basis",
    "selected_packet_emission_basis",
    "selected_packet_emission_terminal_summary_basis",
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
    "packet_transfer_spec_only_posture",
    "one_bounded_transfer_posture",
    "packet_transfer_boundary_basis_preserved_posture",
    "packet_emission_basis_preserved_posture",
    "emitted_packet_basis_preserved_posture",
    "transfer_performed_bounded_posture",
    "copy_to_another_device_bounded_posture",
    "transfer_not_receipt_posture",
    "transfer_not_execution_posture",
    "second_carrier_receipt_not_created_posture",
    "second_carrier_execution_not_authorized_posture",
    "source_transfer_not_authorized_posture",
    "source_receipt_not_created_posture",
    "reception_authorization_not_created_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "final_completion_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_transfer_authority_posture",
    "carrier_possession_not_receipt_authority_posture",
    "copy_presence_not_receipt_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "packet_transfer_scope",
    "packet_transfer_checks",
    "packet_transfer_statement",
    "packet_transfer_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_packet_transfer_summary",
)

SELECTED_BASIS_SECTIONS = tuple(resolver.SELECTED_BASIS_KEYS)

TRUE_RECORDED_FIELDS = (
    "packet_transfer_recorded",
    "bounded_packet_transfer_recorded",
    "packet_transfer_boundary_basis_preserved",
    "packet_emission_basis_preserved",
    "emitted_packet_basis_preserved",
    "transfer_performed_bounded",
    "copy_to_another_device_bounded",
    "transfer_not_receipt",
    "transfer_not_execution",
    "second_carrier_receipt_not_created",
    "second_carrier_execution_not_authorized",
    "source_transfer_not_authorized",
    "source_receipt_not_created",
    "reception_authorization_not_created",
    "external_result_not_created",
    "cross_carrier_evidence_not_created",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "final_completion_not_created",
    "runtime_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_transfer_authority",
    "repo_local_availability_not_transfer_authority",
    "carrier_possession_not_receipt_authority",
    "copy_presence_not_receipt_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

FALSE_NON_CLAIMS_TO_CHECK = (
    "second_carrier_receipt_created",
    "second_carrier_execution_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "packet_transfer_treated_as_second_carrier_receipt",
    "packet_transfer_treated_as_second_carrier_execution",
    "packet_transfer_treated_as_source_transfer",
    "packet_transfer_treated_as_source_receipt",
    "packet_transfer_treated_as_reception_authorization",
    "packet_transfer_treated_as_cross_carrier_evidence",
    "packet_transfer_treated_as_source",
    "packet_transfer_treated_as_authority",
    "packet_transfer_treated_as_currentness",
    "packet_transfer_treated_as_final_completion",
    "packet_transfer_treated_as_runtime",
    "packet_transfer_treated_as_continuation",
    "packet_transfer_treated_as_reusable_permission",
    "packet_transfer_treated_as_follow_on_work",
    "transferred_packet_treated_as_source",
    "transferred_packet_treated_as_authority",
    "transferred_packet_treated_as_currentness",
    "artifact_existence_treated_as_transfer_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_transfer_authority",
    "carrier_possession_treated_as_receipt_authority",
    "copy_presence_treated_as_receipt_authority",
    "hidden_repo_state_used_as_transfer_content",
    "hidden_repo_state_used_as_transfer_authority",
    "v1_repaired",
    "v1_hidden",
    "v1_claimed_passed",
)

NON_MEANING_FALSE_FIELDS = (
    "second_carrier_received_anything",
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
    "follow_on_work_authorized",
    "transfer_became_source_transfer",
    "transfer_became_source_receipt",
    "transfer_became_reception_authorization",
    "transfer_became_cross_carrier_proof",
    "copy_presence_became_receipt",
    "carrier_possession_became_receipt",
    "transferred_packet_became_source",
    "transferred_packet_became_authority",
    "transferred_packet_became_currentness",
    "artifact_existence_became_transfer_authority",
    "artifact_path_became_currentness",
    "repo_local_availability_became_transfer_authority",
    "hidden_repo_state_became_transfer_authority",
    "v1_packet_emission_boundary_repaired",
    "v1_packet_emission_boundary_hidden",
    "v1_packet_emission_boundary_erased",
    "v1_packet_emission_boundary_claimed_passed",
)

REPRESENTATIVE_BLOCK_CODES = (
    "PACKET_TRANSFER_QUESTION_UNDECLARED",
    "PACKET_TRANSFER_INTENT_UNSUPPORTED",
    "PACKET_TRANSFER_BOUNDARY_BASIS_MISSING",
    "PACKET_TRANSFER_BOUNDARY_NOT_RECORDED",
    "PACKET_TRANSFER_BOUNDARY_FAILED_CHECKS_PRESENT",
    "PACKET_TRANSFER_BOUNDARY_VERSION_NOT_0_1_0",
    "PACKET_TRANSFER_BOUNDARY_DID_NOT_DECLARE_FUTURE_TRANSFER_STEP",
    "PACKET_TRANSFER_BOUNDARY_ALREADY_PERFORMED_TRANSFER",
    "PACKET_TRANSFER_BOUNDARY_ALREADY_PERFORMED_COPY",
    "PACKET_TRANSFER_BOUNDARY_CREATED_SECOND_CARRIER_RECEIPT",
    "PACKET_TRANSFER_BOUNDARY_AUTHORIZED_SECOND_CARRIER_EXECUTION",
    "PACKET_TRANSFER_BOUNDARY_CREATED_EXTERNAL_RESULT",
    "PACKET_TRANSFER_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
    "PACKET_TRANSFER_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_TRANSFER_AUTHORITY",
    "PACKET_TRANSFER_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_TRANSFER_AUTHORITY",
    "PACKET_TRANSFER_BOUNDARY_TREATED_CARRIER_POSSESSION_AS_RECEIPT_AUTHORITY",
    "PACKET_TRANSFER_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
    "PACKET_EMISSION_BASIS_MISSING",
    "PACKET_EMISSION_NOT_RECORDED",
    "PACKET_EMISSION_FAILED_CHECKS_PRESENT",
    "PACKET_EMISSION_DID_NOT_PRESERVE_V1_FAILURE",
    "PACKET_TRANSFER_TREATED_AS_SECOND_CARRIER_RECEIPT",
    "PACKET_TRANSFER_TREATED_AS_SECOND_CARRIER_EXECUTION",
    "PACKET_TRANSFER_TREATED_AS_SOURCE_TRANSFER",
    "PACKET_TRANSFER_TREATED_AS_SOURCE_RECEIPT",
    "PACKET_TRANSFER_TREATED_AS_RECEPTION_AUTHORIZATION",
    "PACKET_TRANSFER_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "PACKET_TRANSFER_TREATED_AS_SOURCE",
    "PACKET_TRANSFER_TREATED_AS_AUTHORITY",
    "PACKET_TRANSFER_TREATED_AS_CURRENTNESS",
    "PACKET_TRANSFER_TREATED_AS_FINAL_COMPLETION",
    "PACKET_TRANSFER_TREATED_AS_RUNTIME",
    "PACKET_TRANSFER_TREATED_AS_CONTINUATION",
    "PACKET_TRANSFER_TREATED_AS_REUSABLE_PERMISSION",
    "PACKET_TRANSFER_TREATED_AS_FOLLOW_ON_WORK",
    "TRANSFERRED_PACKET_TREATED_AS_SOURCE",
    "TRANSFERRED_PACKET_TREATED_AS_AUTHORITY",
    "TRANSFERRED_PACKET_TREATED_AS_CURRENTNESS",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SECOND_CARRIER_RECEIPT_CREATED",
    "SECOND_CARRIER_EXECUTION_CREATED",
    "EXTERNAL_RESULT_CREATED",
    "CROSS_CARRIER_EVIDENCE_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_TRANSFER_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_TRANSFER_AUTHORITY",
    "CARRIER_POSSESSION_TREATED_AS_RECEIPT_AUTHORITY",
    "COPY_PRESENCE_TREATED_AS_RECEIPT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_TRANSFER_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_TRANSFER_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_TRANSFER",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_PACKET_TRANSFER_SCOPE",
)


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _make_request(**overrides: Any) -> dict[str, Any]:
    request = resolver.build_declared_portable_source_body_verification_packet_transfer_request(
        packet_transfer_request_id="packet_transfer_test_request_001"
    )
    request["packet_transfer_scope"] = sorted(SUPPORTED_SCOPE)
    request["declared_non_claims"] = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    for key, value in overrides.items():
        request[key] = value
    return request


def _mutated_request(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = _make_request()
    mutator(request)
    return request


class PacketTransferResolverTests(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping):
            block_code = block.get("block_code")
            if block_code is not None:
                self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in result.get("packet_transfer_checks", []):
            if not isinstance(check, Mapping):
                continue
            for field in ("block_code", "failure_code"):
                code = check.get(field)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_booleans(self, result: Mapping[str, Any]) -> None:
        for section_name in (
            "packet_transfer_statement",
            "packet_transfer_non_meaning",
            "non_claims",
        ):
            section = result.get(section_name, {})
            self.assertIsInstance(section, Mapping)
            for key, value in section.items():
                self.assertIs(type(value), bool, f"{section_name}.{key}")
                self.assertNotIn(value, REDACTION_STRINGS)
        summary = result.get("portable_source_body_verification_packet_transfer_summary", {})
        self.assertIsInstance(summary, Mapping)
        for key, value in summary.items():
            if isinstance(value, bool):
                self.assertIs(type(value), bool, f"summary.{key}")
                self.assertNotIn(value, REDACTION_STRINGS)

    def assert_no_raw_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _json_text(result)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)

    def assert_no_later_authority_created(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims", {})
        self.assertIsInstance(non_claims, Mapping)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
        statement = result.get("packet_transfer_statement", {})
        self.assertIsInstance(statement, Mapping)
        for key in (
            "second_carrier_receipt_not_created",
            "second_carrier_execution_not_authorized",
            "source_transfer_not_authorized",
            "source_receipt_not_created",
            "reception_authorization_not_created",
            "external_result_not_created",
            "cross_carrier_evidence_not_created",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "final_completion_not_created",
            "runtime_not_created",
            "follow_on_work_not_authorized",
            "hidden_repo_state_excluded",
            "hidden_repo_state_not_used_as_transfer_authority",
            "repo_local_availability_not_transfer_authority",
            "carrier_possession_not_receipt_authority",
            "copy_presence_not_receipt_authority",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
        ):
            self.assertIs(statement.get(key), True, key)

    def assert_blocked_safely(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), BLOCKED)
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIn(block.get("block_code"), resolver.BLOCK_CODES)
        self.assert_public_block_codes(result)
        self.assert_no_later_authority_created(result)
        non_claims = result["non_claims"]
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)
        self.assertIs(non_claims["v1_repaired"], False)
        self.assertIs(non_claims["v1_hidden"], False)
        self.assertIs(non_claims["v1_claimed_passed"], False)
        self.assert_generated_booleans_are_booleans(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_packet_transfer",
            "resolve_portable_source_body_verification_packet_transfer_from_path",
            "write_portable_source_body_verification_packet_transfer_result",
            "build_portable_source_body_verification_packet_transfer_summary",
            "build_declared_portable_source_body_verification_packet_transfer_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_PACKET_TRANSFER_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_transfer"
            )
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_packet_transfer_recorded_result(self) -> None:
        request = _make_request()
        original = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_packet_transfer(
            declared_packet_transfer_request=request
        )

        self.assertEqual(request, original)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        summary = result["portable_source_body_verification_packet_transfer_summary"]
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result["block"])
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        metadata = result["portable_source_body_verification_packet_transfer_metadata"]
        self.assertEqual(
            metadata["portable_source_body_verification_packet_transfer_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_packet_transfer",
        )
        self.assertEqual(
            metadata["portable_source_body_verification_packet_transfer_request_id"],
            "packet_transfer_test_request_001",
        )

        statement = result["packet_transfer_statement"]
        for key in TRUE_RECORDED_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)

        non_claims = result["non_claims"]
        for key in FALSE_NON_CLAIMS_TO_CHECK:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

        non_meaning = result["packet_transfer_non_meaning"]
        for key in NON_MEANING_FALSE_FIELDS:
            self.assertIn(key, non_meaning)
            self.assertIs(non_meaning[key], False, key)

        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_booleans(result)
        self.assert_no_raw_sentinels(result)

    def test_summary_helper_preserves_packet_transfer_posture(self) -> None:
        result = resolver.resolve_portable_source_body_verification_packet_transfer(
            declared_packet_transfer_request=_make_request()
        )
        summary = resolver.build_portable_source_body_verification_packet_transfer_summary(result)

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["request_id"], "packet_transfer_test_request_001")
        self.assertEqual(summary["question"], resolver.CORE_QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)

        for key in (
            "packet_transfer_recorded",
            "bounded_packet_transfer_recorded",
            "packet_transfer_boundary_basis_preserved",
            "packet_emission_basis_preserved",
            "emitted_packet_basis_preserved",
            "transfer_performed_bounded",
            "copy_to_another_device_bounded",
            "transfer_not_receipt",
            "transfer_not_execution",
            "second_carrier_receipt_not_created",
            "second_carrier_execution_not_authorized",
            "source_transfer_not_authorized",
            "source_receipt_not_created",
            "reception_authorization_not_created",
            "external_result_not_created",
            "cross_carrier_evidence_not_created",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "final_completion_not_created",
            "runtime_not_created",
            "follow_on_work_not_authorized",
            "hidden_repo_state_excluded",
            "hidden_repo_state_not_used_as_transfer_authority",
            "repo_local_availability_not_transfer_authority",
            "carrier_possession_not_receipt_authority",
            "copy_presence_not_receipt_authority",
            "selected_basis_reference_shape_preserved",
            "raw_full_prior_artifact_body_not_returned",
            "no_receipt_execution_cross_carrier_evidence",
            "no_source_authority_currentness_final_completion_runtime",
            "no_deployment_public_release_follow_on",
            "v1_predecessor_failure_preserved",
            "v1_not_repaired_hidden_or_claimed_passed",
        ):
            self.assertIs(summary[key], True, key)

        self.assertEqual(
            summary["selected_packet_transfer_boundary_outcome"],
            resolver.PACKET_TRANSFER_BOUNDARY_RECORDED,
        )
        self.assertEqual(summary["selected_packet_transfer_boundary_version"], "0.1.0")
        self.assertEqual(summary["selected_packet_transfer_boundary_failed_check_count"], 0)
        key_non_claims = summary["key_non_claims"]
        for key, value in key_non_claims.items():
            self.assertIs(value, False, key)

    def test_representative_blocking_behavior(self) -> None:
        block_cases: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
            ("explicit block intent", lambda r: r.update(packet_transfer_intent=resolver.INTENT_BLOCK)),
            ("unsupported intent", lambda r: r.update(packet_transfer_intent="UNSUPPORTED")),
            ("unsupported scope", lambda r: r.update(packet_transfer_scope=["UNSUPPORTED_SCOPE"])),
            ("missing boundary basis", lambda r: r.pop("selected_packet_transfer_boundary_basis")),
            ("boundary not recorded", lambda r: r.update(selected_packet_transfer_boundary_result_outcome="NOT_RECORDED")),
            ("boundary failed checks", lambda r: r.update(selected_packet_transfer_boundary_failed_check_count=1)),
            ("boundary version wrong", lambda r: r.update(selected_packet_transfer_boundary_result_version="9.9.9")),
            ("boundary no future step", lambda r: r.update(selected_packet_transfer_boundary_declared_future_transfer_step=False)),
            ("boundary already transferred", lambda r: r.update(selected_packet_transfer_boundary_already_performed_transfer=True)),
            ("boundary already copied", lambda r: r.update(selected_packet_transfer_boundary_already_performed_copy=True)),
            ("boundary created receipt", lambda r: r.update(selected_packet_transfer_boundary_created_second_carrier_receipt=True)),
            ("boundary authorized execution", lambda r: r.update(selected_packet_transfer_boundary_authorized_second_carrier_execution=True)),
            ("boundary created external result", lambda r: r.update(selected_packet_transfer_boundary_created_external_result=True)),
            ("boundary created cross evidence", lambda r: r.update(selected_packet_transfer_boundary_created_cross_carrier_evidence=True)),
            ("boundary used hidden authority", lambda r: r.update(selected_packet_transfer_boundary_used_hidden_repo_state_as_transfer_authority=True)),
            ("boundary repo local authority", lambda r: r.update(selected_packet_transfer_boundary_treated_repo_local_availability_as_transfer_authority=True)),
            ("boundary carrier receipt authority", lambda r: r.update(selected_packet_transfer_boundary_treated_carrier_possession_as_receipt_authority=True)),
            ("boundary raw body returned", lambda r: r.update(selected_packet_transfer_boundary_raw_full_prior_artifact_body_returned=True)),
            ("emission basis missing", lambda r: r.pop("selected_packet_emission_basis")),
            ("emission not recorded", lambda r: r.update(selected_packet_emission_result_outcome="NOT_RECORDED")),
            ("emission failed checks", lambda r: r.update(selected_packet_emission_failed_check_count=1)),
            ("emission v1 failure missing", lambda r: r.update(selected_packet_emission_v1_failure_preserved=False)),
            ("selected basis not reference", lambda r: r.update(reference_shaped_input_posture=False)),
            ("command lineage current report", lambda r: r.update(command_report_lineage_treated_as_current_report_artifact=True)),
            ("command lineage source", lambda r: r.update(command_report_lineage_treated_as_source=True)),
            ("command lineage authority", lambda r: r.update(command_report_lineage_treated_as_authority=True)),
            ("command lineage currentness", lambda r: r.update(command_report_lineage_treated_as_currentness=True)),
            ("forced full prior body outside transfer", lambda r: r.update(_forced_block_code="FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_TRANSFER")),
            ("missing required non-claim", lambda r: r["declared_non_claims"].pop("source_created")),
        ]

        non_claim_block_cases = (
            "second_carrier_receipt_created",
            "second_carrier_execution_created",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "external_result_created",
            "cross_carrier_evidence_created",
            "packet_transfer_treated_as_second_carrier_receipt",
            "packet_transfer_treated_as_second_carrier_execution",
            "packet_transfer_treated_as_source_transfer",
            "packet_transfer_treated_as_source_receipt",
            "packet_transfer_treated_as_reception_authorization",
            "packet_transfer_treated_as_cross_carrier_evidence",
            "packet_transfer_treated_as_source",
            "packet_transfer_treated_as_authority",
            "packet_transfer_treated_as_currentness",
            "packet_transfer_treated_as_final_completion",
            "packet_transfer_treated_as_runtime",
            "packet_transfer_treated_as_continuation",
            "packet_transfer_treated_as_reusable_permission",
            "packet_transfer_treated_as_follow_on_work",
            "transferred_packet_treated_as_source",
            "transferred_packet_treated_as_authority",
            "transferred_packet_treated_as_currentness",
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
            "artifact_existence_treated_as_transfer_authority",
            "artifact_path_treated_as_currentness",
            "repo_local_availability_treated_as_transfer_authority",
            "carrier_possession_treated_as_receipt_authority",
            "copy_presence_treated_as_receipt_authority",
            "hidden_repo_state_used_as_transfer_content",
            "hidden_repo_state_used_as_transfer_authority",
            "raw_full_prior_artifact_body_returned",
            "prior_artifacts_mutated",
            "consumed_request_reopened",
            "authorization_token_reused",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
        )
        for key in non_claim_block_cases:
            block_cases.append(
                (
                    f"non-claim flipped {key}",
                    lambda r, non_claim_key=key: r["declared_non_claims"].__setitem__(
                        non_claim_key, True
                    ),
                )
            )

        for label, mutator in block_cases:
            with self.subTest(label=label):
                result = resolver.resolve_portable_source_body_verification_packet_transfer(
                    declared_packet_transfer_request=_mutated_request(mutator)
                )
                self.assert_blocked_safely(result)

        for malformed in (None, ["not", "a", "mapping"]):
            with self.subTest(label=f"malformed {malformed!r}"):
                result = resolver.resolve_portable_source_body_verification_packet_transfer(
                    declared_packet_transfer_request=malformed  # type: ignore[arg-type]
                )
                self.assert_blocked_safely(result)

    def test_path_and_write_behavior(self) -> None:
        request = _make_request()
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            request_path = temp_dir / "packet_transfer_request.json"
            request_path.write_text(_json_text(request), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_packet_transfer_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result["portable_source_body_verification_packet_transfer_metadata"]
            self.assertEqual(
                metadata["portable_source_body_verification_packet_transfer_result_version"],
                "0.1.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_packet_transfer",
            )

            malformed_path = temp_dir / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketTransferError):
                resolver.resolve_portable_source_body_verification_packet_transfer_from_path(
                    malformed_path
                )

            array_path = temp_dir / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_portable_source_body_verification_packet_transfer_from_path(
                array_path
            )
            self.assert_blocked_safely(array_result)

            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketTransferError):
                resolver.resolve_portable_source_body_verification_packet_transfer_from_path(
                    temp_dir / "missing.json"
                )

            redirected_root = (
                temp_dir
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_transfer"
            )
            with patch.object(resolver, "OUTPUT_ROOT", redirected_root):
                first_path = resolver.write_portable_source_body_verification_packet_transfer_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_packet_transfer_result(
                    result
                )

            self.assertEqual(first_path.parent, redirected_root)
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(second_path.stem.endswith("_001"))
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            self.assertIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_transfer",
                str(first_path),
            )
            for forbidden_root in (
                "packet_transfer_boundary",
                "packet_emission/",
                "second_carrier",
                "cross_carrier",
                "runtime",
                "deployment",
                "public_release",
            ):
                self.assertNotIn(forbidden_root, str(first_path))

    def test_non_mutation(self) -> None:
        request = _make_request()
        original = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_packet_transfer(
            declared_packet_transfer_request=request
        )

        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, original)
        for section in SELECTED_BASIS_SECTIONS + POSTURE_SECTIONS:
            self.assertEqual(request[section], original[section], section)
        self.assertEqual(request["packet_transfer_scope"], original["packet_transfer_scope"])
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
            "transfer_body": HOSTILE_RAW_VALUE,
            "copy_body": HOSTILE_RAW_VALUE,
            "packet_body": HOSTILE_RAW_VALUE,
            "source_body": HOSTILE_RAW_VALUE,
            "authority_body": HOSTILE_RAW_VALUE,
            "hidden_repo_state": HOSTILE_RAW_VALUE,
            "current_working_tree": HOSTILE_RAW_VALUE,
            "local_cache": HOSTILE_RAW_VALUE,
            "repo_local_only_dependency": HOSTILE_RAW_VALUE,
            "carrier_possession": HOSTILE_RAW_VALUE,
            "copy_presence": HOSTILE_RAW_VALUE,
            "unlisted_file_dependency": HOSTILE_RAW_VALUE,
            "nested": [{"sentinel": RAW_SENTINEL, "value": HOSTILE_RAW_VALUE}],
        }
        for section in (
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
            request[section]["hostile_payload"] = copy.deepcopy(hostile_payload)
        request["_forced_block_code"] = "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"

        original = copy.deepcopy(request)
        result = resolver.resolve_portable_source_body_verification_packet_transfer(
            declared_packet_transfer_request=request
        )

        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertEqual(request, original)
        self.assert_public_block_codes(result)
        self.assert_no_raw_sentinels(result)
        self.assert_no_later_authority_created(result)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_transfer_content"], False)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_transfer_authority"], False)
        self.assertIs(
            result["non_claims"]["repo_local_availability_treated_as_transfer_authority"],
            False,
        )
        self.assertIs(
            result["non_claims"]["carrier_possession_treated_as_receipt_authority"],
            False,
        )
        self.assertIs(
            result["non_claims"]["copy_presence_treated_as_receipt_authority"],
            False,
        )
        self.assert_generated_booleans_are_booleans(result)


if __name__ == "__main__":
    unittest.main()
