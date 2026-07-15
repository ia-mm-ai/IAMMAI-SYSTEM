"""Tests for bounded portable source-body verification packet emission.

This suite is downstream of recorded packet-emission-boundary v2. It verifies
that the packet-emission resolver records one bounded local packet-emission
posture only: packet emission is not packet transfer, not copying to another
device, not source transfer, not source receipt, not reception authorization,
not second-carrier receipt/execution, not external result, not cross-carrier
proof, and not source/authority/currentness/runtime/final-completion/follow-on.
The preserved v1 packet-emission-boundary failure remains visible and
unrepaired, hidden repo state is excluded, repo-local availability is not
emission authority, consumed request remains closed, and authorization token
reuse remains blocked.
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

import resolve_portable_source_body_verification_packet_emission as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_PACKET_EMISSION_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
EXTRA_FALSE_NON_CLAIMS = tuple(getattr(resolver, "EXTRA_FALSE_NON_CLAIMS", ()))
REDACTION = "[bounded-redacted-raw-or-hidden-state]"

RAW_SENTINEL = "RAW_PACKET_EMISSION_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_PACKET_EMISSION_FULL_BODY_VALUE_MUST_NOT_RETURN"

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_packet_emission_metadata",
    "declared_packet_emission_question",
    "selected_packet_emission_boundary_v2_basis",
    "selected_packet_emission_boundary_v2_terminal_summary_basis",
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
    "packet_emission_spec_only_posture",
    "one_bounded_packet_emission_posture",
    "packet_emission_boundary_v2_basis_preserved_posture",
    "packet_emission_boundary_v1_failure_preserved_posture",
    "packet_artifact_basis_preserved_posture",
    "emitted_packet_recorded_or_bounded_posture",
    "packet_transfer_not_authorized_posture",
    "copy_to_another_device_not_authorized_posture",
    "source_transfer_not_authorized_posture",
    "source_receipt_not_created_posture",
    "reception_authorization_not_created_posture",
    "second_carrier_receipt_not_created_posture",
    "second_carrier_execution_not_authorized_posture",
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
    "repo_local_availability_not_emission_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "packet_emission_scope",
    "packet_emission_checks",
    "packet_emission_statement",
    "packet_emission_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_packet_emission_summary",
)

TRUE_RECORDED_FIELDS = (
    "packet_emission_recorded",
    "bounded_packet_emission_recorded",
    "packet_emission_boundary_v2_basis_preserved",
    "packet_emission_boundary_v1_failure_preserved",
    "packet_artifact_basis_preserved",
    "emitted_packet_recorded_or_bounded",
    "packet_transfer_not_authorized",
    "copy_to_another_device_not_authorized",
    "source_transfer_not_authorized",
    "source_receipt_not_created",
    "reception_authorization_not_created",
    "second_carrier_receipt_not_created",
    "second_carrier_execution_not_authorized",
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
    "hidden_repo_state_not_used_as_emission_authority",
    "repo_local_availability_not_emission_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

REPRESENTATIVE_BLOCK_CODES = (
    "PACKET_EMISSION_QUESTION_UNDECLARED",
    "PACKET_EMISSION_INTENT_UNSUPPORTED",
    "PACKET_EMISSION_BOUNDARY_V2_BASIS_MISSING",
    "PACKET_EMISSION_BOUNDARY_V2_NOT_RECORDED",
    "PACKET_EMISSION_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
    "PACKET_EMISSION_BOUNDARY_V2_VERSION_NOT_0_2_0",
    "PACKET_EMISSION_BOUNDARY_V2_V1_FAILURE_EVIDENCE_MISSING",
    "PACKET_EMISSION_BOUNDARY_V2_REPAIRED_V1",
    "PACKET_EMISSION_BOUNDARY_V2_HID_V1",
    "PACKET_EMISSION_BOUNDARY_V2_CLAIMED_V1_PASSED",
    "PACKET_EMISSION_BOUNDARY_V2_DID_NOT_DECLARE_FUTURE_PACKET_EMISSION_STEP",
    "PACKET_EMISSION_BOUNDARY_V2_ALREADY_EMITTED_PACKET",
    "PACKET_EMISSION_BOUNDARY_V2_ALREADY_CREATED_EMITTED_PACKET",
    "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_TRANSFER",
    "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_COPY_TO_ANOTHER_DEVICE",
    "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SOURCE_TRANSFER",
    "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SOURCE_RECEIPT",
    "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_RECEPTION",
    "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SECOND_CARRIER_RECEIPT",
    "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SECOND_CARRIER_EXECUTION",
    "PACKET_EMISSION_BOUNDARY_V2_CREATED_EXTERNAL_RESULT",
    "PACKET_EMISSION_BOUNDARY_V2_CREATED_CROSS_CARRIER_EVIDENCE",
    "PACKET_EMISSION_BOUNDARY_V2_USED_HIDDEN_REPO_STATE_AS_EMISSION_AUTHORITY",
    "PACKET_EMISSION_BOUNDARY_V2_TREATED_REPO_LOCAL_AVAILABILITY_AS_EMISSION_AUTHORITY",
    "PACKET_EMISSION_BOUNDARY_V2_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
    "PACKET_ARTIFACT_BASIS_MISSING",
    "PACKET_ARTIFACT_NOT_RECORDED",
    "PACKET_ARTIFACT_FAILED_CHECKS_PRESENT",
    "PACKET_EMISSION_TREATED_AS_TRANSFER",
    "PACKET_EMISSION_TREATED_AS_COPY_TO_ANOTHER_DEVICE",
    "PACKET_EMISSION_TREATED_AS_SOURCE_TRANSFER",
    "PACKET_EMISSION_TREATED_AS_SOURCE_RECEIPT",
    "PACKET_EMISSION_TREATED_AS_RECEPTION_AUTHORIZATION",
    "PACKET_EMISSION_TREATED_AS_SECOND_CARRIER_RECEIPT",
    "PACKET_EMISSION_TREATED_AS_SECOND_CARRIER_EXECUTION",
    "PACKET_EMISSION_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "PACKET_EMISSION_TREATED_AS_SOURCE",
    "PACKET_EMISSION_TREATED_AS_AUTHORITY",
    "PACKET_EMISSION_TREATED_AS_CURRENTNESS",
    "PACKET_EMISSION_TREATED_AS_FINAL_COMPLETION",
    "PACKET_EMISSION_TREATED_AS_RUNTIME",
    "PACKET_EMISSION_TREATED_AS_CONTINUATION",
    "PACKET_EMISSION_TREATED_AS_REUSABLE_PERMISSION",
    "PACKET_EMISSION_TREATED_AS_FOLLOW_ON_WORK",
    "EMITTED_PACKET_TREATED_AS_SOURCE",
    "EMITTED_PACKET_TREATED_AS_AUTHORITY",
    "EMITTED_PACKET_TREATED_AS_CURRENTNESS",
    "PACKET_TRANSFERRED",
    "PACKET_COPIED_TO_ANOTHER_DEVICE",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_EMISSION_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_EMISSION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_EMISSION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_EMISSION_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EMISSION",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_PACKET_EMISSION_SCOPE",
)

SELECTED_BASIS_SECTIONS = (
    "selected_packet_emission_boundary_v2_basis",
    "selected_packet_emission_boundary_v2_terminal_summary_basis",
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
)

NON_MEANING_FALSE_FIELDS = (
    "packet_was_transferred",
    "packet_was_copied_to_another_device",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_exists",
    "second_carrier_received_anything",
    "second_carrier_executed_anything",
    "external_result_exists",
    "cross_carrier_evidence_exists",
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
    "packet_emission_became_source_transfer",
    "packet_emission_became_source_receipt",
    "packet_emission_became_reception_authorization",
    "packet_emission_became_cross_carrier_proof",
    "emitted_packet_became_source",
    "emitted_packet_became_authority",
    "emitted_packet_became_currentness",
    "artifact_existence_became_emission_authority",
    "artifact_path_became_currentness",
    "repo_local_availability_became_emission_authority",
    "hidden_repo_state_became_emission_authority",
    "v1_packet_emission_boundary_resolver_was_repaired_hidden_erased_or_claimed_passed",
)


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _fresh_request() -> dict[str, Any]:
    request = resolver.build_declared_portable_source_body_verification_packet_emission_request(
        packet_emission_request_id="portable_source_body_verification_packet_emission_unit_request_001"
    )
    request["packet_emission_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    request["declared_non_claims"].update({key: False for key in EXTRA_FALSE_NON_CLAIMS})
    request["selected_command_execution_basis"]["outcome"] = (
        "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED"
    )
    return request


def _flip_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"][key] = True

    return mutate


def _missing_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"].pop(key, None)

    return mutate


def _set_boundary(shortcut: str, basis_key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[shortcut] = value
        request["selected_packet_emission_boundary_v2_basis"][basis_key] = value

    return mutate


def _set_artifact(shortcut: str, basis_key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[shortcut] = value
        request["selected_packet_artifact_basis"][basis_key] = value

    return mutate


class PacketEmissionResolverTests(unittest.TestCase):
    def assert_block_codes_are_public(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if _is_mapping(block):
            code = block.get("block_code")
            if code is not None:
                self.assertIn(code, resolver.BLOCK_CODES)
        for check in result.get("packet_emission_checks", []):
            if not _is_mapping(check):
                continue
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_bools(self, result: Mapping[str, Any]) -> None:
        metadata = result.get("portable_source_body_verification_packet_emission_metadata", {})
        for key in (
            "v1_packet_emission_boundary_failure_preserved",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
            "packet_emission_does_not_repair_hide_or_claim_v1_passed",
        ):
            if _is_mapping(metadata) and key in metadata:
                self.assertIs(type(metadata[key]), bool)
                self.assertNotEqual(metadata[key], REDACTION)

        for section_name in tuple(getattr(resolver, "POSTURE_KEYS", ())) + (
            "packet_emission_statement",
            "non_claims",
            "portable_source_body_verification_packet_emission_summary",
        ):
            section = result.get(section_name, {})
            if not _is_mapping(section):
                continue
            for key, value in section.items():
                self.assertNotEqual(value, REDACTION)
                if isinstance(value, bool):
                    self.assertIs(type(value), bool)
                if key in TRUE_RECORDED_FIELDS or key in REQUIRED_FALSE_NON_CLAIMS:
                    self.assertIs(type(value), bool, key)

        summary = result.get("portable_source_body_verification_packet_emission_summary", {})
        if _is_mapping(summary):
            for key in TRUE_RECORDED_FIELDS:
                if key in summary:
                    self.assertIs(type(summary[key]), bool, key)
            for key in (
                "v1_predecessor_failure_preserved",
                "v1_repaired",
                "v1_hidden",
                "v1_claimed_passed",
                "no_transfer_copy_receipt_cross_carrier_evidence",
                "no_source_authority_currentness_final_completion_runtime",
                "no_deployment_public_release_follow_on",
            ):
                if key in summary:
                    self.assertIs(type(summary[key]), bool, key)
            key_non_claims = summary.get("key_non_claims", {})
            if _is_mapping(key_non_claims):
                for value in key_non_claims.values():
                    self.assertIs(type(value), bool)
                    self.assertNotEqual(value, REDACTION)

        for check in result.get("packet_emission_checks", []):
            if _is_mapping(check):
                self.assertIs(type(check.get("passed")), bool)
                self.assertNotEqual(check.get("passed"), REDACTION)

    def assert_no_raw_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _json_text(result)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)

    def assert_no_later_work_created(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims", {})
        for key in (
            "packet_transferred",
            "packet_copied_to_another_device",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "second_carrier_receipt_created",
            "second_carrier_execution_created",
            "external_result_created",
            "cross_carrier_evidence_created",
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
            if _is_mapping(non_claims) and key in non_claims:
                self.assertIs(non_claims[key], False, key)
        block = result.get("block")
        if _is_mapping(block):
            for key in (
                "packet_transferred",
                "packet_copied_to_another_device",
                "source_transfer_occurred",
                "source_receipt_occurred",
                "reception_authorization_created",
                "second_carrier_receipt_created",
                "second_carrier_execution_created",
                "external_result_created",
                "cross_carrier_evidence_created",
                "source_created",
                "authority_created",
                "currentness_created",
                "final_completion_claimed",
                "runtime_hosting_created",
                "deployment_created",
                "public_release_created",
                "follow_on_work_authorized",
                "consumed_request_reopened",
                "authorization_token_reused",
                "v1_repaired",
                "v1_hidden",
                "v1_claimed_passed",
                "artifacts_mutated",
            ):
                if key in block:
                    self.assertIs(block[key], False, key)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_packet_emission",
            "resolve_portable_source_body_verification_packet_emission_from_path",
            "write_portable_source_body_verification_packet_emission_result",
            "build_portable_source_body_verification_packet_emission_summary",
            "build_declared_portable_source_body_verification_packet_emission_request",
        ):
            self.assertTrue(hasattr(resolver, name), name)
            self.assertTrue(callable(getattr(resolver, name)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_PACKET_EMISSION_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).replace("\\", "/").endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission"
            )
        )
        self.assertTrue(set(REPRESENTATIVE_BLOCK_CODES).issubset(set(resolver.BLOCK_CODES)))
        self.assertTrue(set(SUPPORTED_SCOPE).issubset(set(resolver.SUPPORTED_PACKET_EMISSION_SCOPE)))
        self.assertIn("packet_transferred", REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("hidden_repo_state_used_as_emission_authority", REQUIRED_FALSE_NON_CLAIMS)

    def test_successful_packet_emission_recorded_result(self) -> None:
        request = _fresh_request()
        before = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_packet_emission(request)

        self.assertEqual(request, before)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        block = result["block"]
        self.assertFalse(block["blocked"])
        self.assertIsNone(block["block_code"])
        self.assertEqual(
            result["portable_source_body_verification_packet_emission_metadata"][
                "failed_check_count"
            ],
            0,
        )
        self.assertGreater(
            result["portable_source_body_verification_packet_emission_metadata"][
                "passed_check_count"
            ],
            0,
        )

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)

        metadata = result["portable_source_body_verification_packet_emission_metadata"]
        self.assertEqual(
            metadata["portable_source_body_verification_packet_emission_result_version"],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], "resolve_portable_source_body_verification_packet_emission")
        self.assertEqual(
            metadata["packet_emission_request_id"],
            "portable_source_body_verification_packet_emission_unit_request_001",
        )
        self.assertIs(metadata["v1_packet_emission_boundary_failure_preserved"], True)
        self.assertIs(metadata["v1_repaired"], False)
        self.assertIs(metadata["v1_hidden"], False)
        self.assertIs(metadata["v1_claimed_passed"], False)

        statement = result["packet_emission_statement"]
        for key in TRUE_RECORDED_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)
            self.assertIs(type(statement[key]), bool, key)
            self.assertNotEqual(statement[key], REDACTION)

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIs(type(non_claims[key]), bool, key)
            self.assertNotEqual(non_claims[key], REDACTION)
        for key in EXTRA_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

        for key in (
            "packet_transferred",
            "packet_copied_to_another_device",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "second_carrier_receipt_created",
            "second_carrier_execution_created",
            "external_result_created",
            "cross_carrier_evidence_created",
            "packet_emission_treated_as_transfer",
            "packet_emission_treated_as_copy_to_another_device",
            "packet_emission_treated_as_source_transfer",
            "packet_emission_treated_as_source_receipt",
            "packet_emission_treated_as_reception_authorization",
            "packet_emission_treated_as_second_carrier_receipt",
            "packet_emission_treated_as_second_carrier_execution",
            "packet_emission_treated_as_cross_carrier_evidence",
            "packet_emission_treated_as_source",
            "packet_emission_treated_as_authority",
            "packet_emission_treated_as_currentness",
            "packet_emission_treated_as_final_completion",
            "packet_emission_treated_as_runtime",
            "packet_emission_treated_as_continuation",
            "packet_emission_treated_as_reusable_permission",
            "packet_emission_treated_as_follow_on_work",
            "emitted_packet_treated_as_source",
            "emitted_packet_treated_as_authority",
            "emitted_packet_treated_as_currentness",
            "artifact_existence_treated_as_emission_authority",
            "artifact_path_treated_as_currentness",
            "repo_local_availability_treated_as_emission_authority",
            "hidden_repo_state_used_as_emission_content",
            "hidden_repo_state_used_as_emission_authority",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
        ):
            self.assertIs(non_claims[key], False, key)

        non_meaning = result["packet_emission_non_meaning"]
        for key in NON_MEANING_FALSE_FIELDS:
            self.assertIn(key, non_meaning)
            self.assertIs(non_meaning[key], False, key)

        boundary_basis = result["selected_packet_emission_boundary_v2_basis"]
        self.assertEqual(
            boundary_basis["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_RECORDED",
        )
        self.assertEqual(boundary_basis["result_version"], "0.2.0")
        self.assertEqual(boundary_basis["failed_check_count"], 0)
        self.assertIs(boundary_basis["v1_predecessor_failure_preserved"], True)
        self.assertIs(boundary_basis["v1_repaired"], False)
        self.assertIs(boundary_basis["v1_hidden"], False)
        self.assertIs(boundary_basis["v1_claimed_passed"], False)

        self.assert_block_codes_are_public(result)
        self.assert_generated_booleans_are_bools(result)
        self.assert_no_raw_sentinels(result)

    def test_summary_helper_preserves_packet_emission_posture(self) -> None:
        request = _fresh_request()
        result = resolver.resolve_portable_source_body_verification_packet_emission(request)

        summary = resolver.build_portable_source_body_verification_packet_emission_summary(result)

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["request_id"],
            "portable_source_body_verification_packet_emission_unit_request_001",
        )
        self.assertEqual(summary["question"], resolver.CORE_QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            summary["selected_packet_emission_boundary_v2_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_RECORDED",
        )
        self.assertEqual(summary["selected_packet_emission_boundary_v2_version"], "0.2.0")
        self.assertEqual(summary["selected_packet_emission_boundary_v2_failed_check_count"], 0)
        for key in TRUE_RECORDED_FIELDS:
            self.assertIn(key, summary)
            self.assertIs(summary[key], True, key)
            self.assertIs(type(summary[key]), bool, key)
        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_repaired"], False)
        self.assertIs(summary["v1_hidden"], False)
        self.assertIs(summary["v1_claimed_passed"], False)
        self.assertIs(summary["no_transfer_copy_receipt_cross_carrier_evidence"], True)
        self.assertIs(summary["no_source_authority_currentness_final_completion_runtime"], True)
        self.assertIs(summary["no_deployment_public_release_follow_on"], True)
        for key, value in summary["key_non_claims"].items():
            self.assertIs(type(value), bool, key)
            self.assertIs(value, False, key)
        self.assertNotIn(REDACTION, {value for value in summary.values() if isinstance(value, str)})

    def test_representative_blocking_behavior(self) -> None:
        malformed_results = (
            ("missing request", None),
            ("non-mapping request", ["not", "a", "mapping"]),
        )
        for label, request in malformed_results:
            with self.subTest(label=label):
                result = resolver.resolve_portable_source_body_verification_packet_emission(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assert_block_codes_are_public(result)
                self.assert_no_later_work_created(result)
                self.assert_generated_booleans_are_bools(result)

        block_cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", lambda request: request.update({"packet_emission_intent": resolver.INTENT_BLOCK})),
            ("undeclared question", lambda request: request.update({"packet_emission_question": ""})),
            ("unsupported intent", lambda request: request.update({"packet_emission_intent": "UNSUPPORTED_PACKET_EMISSION_INTENT"})),
            ("unsupported scope", lambda request: request["packet_emission_scope"].append("UNSUPPORTED_PACKET_EMISSION_SCOPE_VALUE")),
            ("missing packet-emission-boundary-v2 basis", lambda request: request.pop("selected_packet_emission_boundary_v2_basis")),
            ("missing packet-emission-boundary-v2 terminal summary basis", lambda request: request.pop("selected_packet_emission_boundary_v2_terminal_summary_basis")),
            ("packet-emission-boundary-v2 not recorded", _set_boundary("selected_packet_emission_boundary_v2_result_outcome", "outcome", "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_NOT_RECORDED")),
            ("packet-emission-boundary-v2 failed checks", _set_boundary("selected_packet_emission_boundary_v2_failed_check_count", "failed_check_count", 1)),
            ("packet-emission-boundary-v2 wrong version", _set_boundary("selected_packet_emission_boundary_v2_result_version", "result_version", "0.1.0")),
            ("packet-emission-boundary-v2 v1 failure evidence missing", _set_boundary("selected_packet_emission_boundary_v2_v1_failure_preserved", "v1_predecessor_failure_preserved", False)),
            ("packet-emission-boundary-v2 repaired v1", _set_boundary("selected_packet_emission_boundary_v2_v1_repaired", "v1_repaired", True)),
            ("packet-emission-boundary-v2 hid v1", _set_boundary("selected_packet_emission_boundary_v2_v1_hidden", "v1_hidden", True)),
            ("packet-emission-boundary-v2 claimed v1 passed", _set_boundary("selected_packet_emission_boundary_v2_v1_claimed_passed", "v1_claimed_passed", True)),
            ("packet-emission-boundary-v2 did not declare future packet-emission step", _set_boundary("selected_packet_emission_boundary_v2_declared_future_packet_emission_step", "one_future_packet_emission_step_declared", False)),
            ("packet-emission-boundary-v2 already emitted packet", _set_boundary("selected_packet_emission_boundary_v2_packet_emitted", "packet_emitted", True)),
            ("packet-emission-boundary-v2 already created emitted packet", _set_boundary("selected_packet_emission_boundary_v2_emitted_packet_created", "emitted_packet_created", True)),
            ("packet-emission-boundary-v2 authorized transfer", _set_boundary("selected_packet_emission_boundary_v2_authorized_transfer", "packet_transfer_authorized", True)),
            ("packet-emission-boundary-v2 authorized copy", _set_boundary("selected_packet_emission_boundary_v2_authorized_copy_to_another_device", "copy_to_another_device_authorized", True)),
            ("packet-emission-boundary-v2 authorized source transfer", _set_boundary("selected_packet_emission_boundary_v2_authorized_source_transfer", "source_transfer_authorized", True)),
            ("packet-emission-boundary-v2 authorized source receipt", _set_boundary("selected_packet_emission_boundary_v2_authorized_source_receipt", "source_receipt_authorized", True)),
            ("packet-emission-boundary-v2 authorized reception", _set_boundary("selected_packet_emission_boundary_v2_authorized_reception", "reception_authorization_created", True)),
            ("packet-emission-boundary-v2 authorized second-carrier receipt", _set_boundary("selected_packet_emission_boundary_v2_authorized_second_carrier_receipt", "second_carrier_receipt_authorized", True)),
            ("packet-emission-boundary-v2 authorized second-carrier execution", _set_boundary("selected_packet_emission_boundary_v2_authorized_second_carrier_execution", "second_carrier_execution_authorized", True)),
            ("packet-emission-boundary-v2 created external result", _set_boundary("selected_packet_emission_boundary_v2_created_external_result", "external_result_created", True)),
            ("packet-emission-boundary-v2 created cross-carrier evidence", _set_boundary("selected_packet_emission_boundary_v2_created_cross_carrier_evidence", "cross_carrier_evidence_created", True)),
            ("packet-emission-boundary-v2 used hidden repo state as emission authority", _set_boundary("selected_packet_emission_boundary_v2_used_hidden_repo_state_as_emission_authority", "hidden_repo_state_used_as_emission_authority", True)),
            ("packet-emission-boundary-v2 treated repo-local availability as emission authority", _set_boundary("selected_packet_emission_boundary_v2_treated_repo_local_availability_as_emission_authority", "repo_local_availability_treated_as_emission_authority", True)),
            ("packet-emission-boundary-v2 returned raw full prior artifact body", _set_boundary("selected_packet_emission_boundary_v2_raw_full_prior_artifact_body_returned", "raw_full_prior_artifact_body_returned", True)),
            ("packet artifact basis missing", lambda request: request.pop("selected_packet_artifact_basis")),
            ("packet artifact not recorded", _set_artifact("selected_packet_artifact_result_outcome", "outcome", "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_NOT_RECORDED")),
            ("packet artifact failed checks", _set_artifact("selected_packet_artifact_failed_check_count", "failed_check_count", 1)),
            ("command report lineage not lineage-only", lambda request: request["selected_command_report_lineage_basis"].update({"lineage_only": False, "command_report_lineage_only": False})),
            ("command report lineage treated as current report artifact", lambda request: request["selected_command_report_lineage_basis"].update({"command_report_lineage_treated_as_current_report_artifact": True})),
            ("command report lineage treated as source", lambda request: request["selected_command_report_lineage_basis"].update({"command_report_lineage_treated_as_source": True})),
            ("command report lineage treated as authority", lambda request: request["selected_command_report_lineage_basis"].update({"command_report_lineage_treated_as_authority": True})),
            ("command report lineage treated as currentness", lambda request: request["selected_command_report_lineage_basis"].update({"command_report_lineage_treated_as_currentness": True})),
            ("predecessor failure evidence repaired", lambda request: request["selected_predecessor_failure_basis"].update({"predecessor_failures_repaired": True})),
            ("selected basis not reference-shaped", lambda request: request.update({"reference_shaped_input_posture": False})),
            ("raw full prior artifact body returned", _flip_non_claim("raw_full_prior_artifact_body_returned")),
            ("consumed request reopened", _flip_non_claim("consumed_request_reopened")),
            ("authorization token reused", _flip_non_claim("authorization_token_reused")),
            ("full prior body emitted outside bounded emission", lambda request: request.update({"full_prior_artifact_body_emitted_outside_bounded_emission": True})),
            ("artifacts mutated", lambda request: request.update({"artifacts_mutated": True})),
            ("required non-claim missing", _missing_non_claim("packet_transferred")),
            ("required non-claim flipped", _flip_non_claim("packet_emission_treated_as_transfer")),
        )

        non_claim_block_cases = (
            "packet_emission_treated_as_copy_to_another_device",
            "packet_emission_treated_as_source_transfer",
            "packet_emission_treated_as_source_receipt",
            "packet_emission_treated_as_reception_authorization",
            "packet_emission_treated_as_second_carrier_receipt",
            "packet_emission_treated_as_second_carrier_execution",
            "packet_emission_treated_as_cross_carrier_evidence",
            "packet_emission_treated_as_source",
            "packet_emission_treated_as_authority",
            "packet_emission_treated_as_currentness",
            "packet_emission_treated_as_final_completion",
            "packet_emission_treated_as_runtime",
            "packet_emission_treated_as_continuation",
            "packet_emission_treated_as_reusable_permission",
            "packet_emission_treated_as_follow_on_work",
            "emitted_packet_treated_as_source",
            "emitted_packet_treated_as_authority",
            "emitted_packet_treated_as_currentness",
            "packet_transferred",
            "packet_copied_to_another_device",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "second_carrier_receipt_created",
            "second_carrier_execution_created",
            "external_result_created",
            "cross_carrier_evidence_created",
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
            "artifact_existence_treated_as_emission_authority",
            "artifact_path_treated_as_currentness",
            "repo_local_availability_treated_as_emission_authority",
            "hidden_repo_state_used_as_emission_content",
            "hidden_repo_state_used_as_emission_authority",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
        )

        for label, mutate in block_cases + tuple((key, _flip_non_claim(key)) for key in non_claim_block_cases):
            with self.subTest(label=label):
                request = _fresh_request()
                mutate(request)
                result = resolver.resolve_portable_source_body_verification_packet_emission(request)
                self.assertEqual(result["outcome"], BLOCKED, label)
                self.assertTrue(result["block"]["block_code"], label)
                self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
                self.assert_block_codes_are_public(result)
                self.assert_no_later_work_created(result)
                self.assert_generated_booleans_are_bools(result)

    def test_path_and_write_behavior(self) -> None:
        request = _fresh_request()
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            request_path = tmp / "packet_emission_request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_packet_emission_from_path(
                request_path
            )

            self.assertEqual(result["outcome"], RECORDED)
            metadata = result["portable_source_body_verification_packet_emission_metadata"]
            self.assertEqual(
                metadata["portable_source_body_verification_packet_emission_result_version"],
                "0.1.0",
            )
            self.assertEqual(metadata["resolver_module"], "resolve_portable_source_body_verification_packet_emission")

            malformed_path = tmp / "malformed.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketEmissionError):
                resolver.resolve_portable_source_body_verification_packet_emission_from_path(
                    malformed_path
                )

            array_path = tmp / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketEmissionError):
                resolver.resolve_portable_source_body_verification_packet_emission_from_path(
                    array_path
                )

            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketEmissionError):
                resolver.resolve_portable_source_body_verification_packet_emission_from_path(
                    tmp / "missing.json"
                )

            output_root = (
                tmp
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_portable_source_body_verification_packet_emission_result(
                    result
                )
                second = resolver.write_portable_source_body_verification_packet_emission_result(
                    result
                )

            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertTrue(second.name.endswith("_001.json"))
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], RECORDED)
            normalized = str(first).replace("\\", "/")
            self.assertIn(
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission/",
                normalized,
            )
            for forbidden_root in (
                "packet_emission_boundary_v2",
                "packet_artifact",
                "packet_transfer",
                "second_carrier",
                "cross_carrier",
                "runtime",
                "deployment",
                "public_release",
            ):
                self.assertNotIn(forbidden_root, normalized)

    def test_non_mutation(self) -> None:
        request = _fresh_request()
        before = copy.deepcopy(request)

        resolver.resolve_portable_source_body_verification_packet_emission(request)

        self.assertEqual(request, before)
        for key in SELECTED_BASIS_SECTIONS:
            self.assertEqual(request[key], before[key], key)
        for key in getattr(resolver, "POSTURE_KEYS", ()):
            self.assertEqual(request[key], before[key], key)
        self.assertEqual(request["packet_emission_scope"], before["packet_emission_scope"])
        self.assertEqual(request["declared_non_claims"], before["declared_non_claims"])

    def test_raw_full_body_and_hidden_state_containment(self) -> None:
        request = _fresh_request()
        hostile_payload = {
            "raw_body": HOSTILE_RAW_VALUE,
            "raw_full_body": RAW_SENTINEL,
            "full_body": HOSTILE_RAW_VALUE,
            "artifact_body": HOSTILE_RAW_VALUE,
            "raw_result_body": HOSTILE_RAW_VALUE,
            "raw_output_body": HOSTILE_RAW_VALUE,
            "emitted_packet_body": HOSTILE_RAW_VALUE,
            "packet_body": HOSTILE_RAW_VALUE,
            "source_body": HOSTILE_RAW_VALUE,
            "authority_body": HOSTILE_RAW_VALUE,
            "hidden_repo_state": {"sentinel": RAW_SENTINEL},
            "current_working_tree": HOSTILE_RAW_VALUE,
            "local_cache": HOSTILE_RAW_VALUE,
            "repo_local_only_dependency": HOSTILE_RAW_VALUE,
            "unlisted_file_dependency": HOSTILE_RAW_VALUE,
            "nested_payload": [{"body": RAW_SENTINEL}],
        }
        for section in (
            "selected_packet_emission_boundary_v2_basis",
            "selected_packet_artifact_basis",
            "selected_packet_boundary_basis",
            "selected_command_success_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        ):
            request[section].update(copy.deepcopy(hostile_payload))
        before = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_packet_emission(request)

        self.assertEqual(request, before)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_no_raw_sentinels(result)
        self.assert_block_codes_are_public(result)
        self.assert_no_later_work_created(result)
        self.assert_generated_booleans_are_bools(result)

        non_claims = result["non_claims"]
        self.assertIs(non_claims["hidden_repo_state_used_as_emission_content"], False)
        self.assertIs(non_claims["hidden_repo_state_used_as_emission_authority"], False)
        self.assertIs(non_claims["repo_local_availability_treated_as_emission_authority"], False)
        statement = result["packet_emission_statement"]
        self.assertIs(type(statement["hidden_repo_state_excluded"]), bool)
        self.assertNotEqual(statement["hidden_repo_state_excluded"], REDACTION)
        self.assertIs(type(statement["repo_local_availability_not_emission_authority"]), bool)
        self.assertNotEqual(
            statement["repo_local_availability_not_emission_authority"],
            REDACTION,
        )


if __name__ == "__main__":
    unittest.main()
