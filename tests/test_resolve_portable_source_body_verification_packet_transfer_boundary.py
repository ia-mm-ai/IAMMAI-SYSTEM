"""Executable checks for bounded packet-transfer-boundary posture only.

These tests keep the packet-transfer-boundary line downstream of recorded
packet emission. They verify one future transfer/copy boundary without
performing transfer, copy, receipt, execution, cross-carrier proof, source,
authority, currentness, runtime, final completion, continuation, reusable
permission, or follow-on work.
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

import resolve_portable_source_body_verification_packet_transfer_boundary as resolver


RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_RECORDED"
NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_NOT_RECORDED"
REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
EXTRA_FALSE_NON_CLAIMS = tuple(getattr(resolver, "EXTRA_FALSE_NON_CLAIMS", ()))
POSTURE_SECTIONS = tuple(getattr(resolver, "POSTURE_KEYS", ()))

RAW_SENTINEL = "RAW_PACKET_TRANSFER_BOUNDARY_BODY_MUST_NOT_RETURN"
RAW_TRANSFER_SENTINEL = "RAW_PACKET_TRANSFER_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_PACKET_TRANSFER_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN"
REDACTION_STRINGS = (
    "[bounded-redacted-raw-or-hidden-state]",
    "[bounded-reference-omitted-raw-or-hidden-state]",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_packet_transfer_boundary_metadata",
    "declared_packet_transfer_boundary_question",
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
    "packet_transfer_boundary_only_posture",
    "one_future_transfer_step_posture",
    "packet_emission_basis_preserved_posture",
    "emitted_packet_basis_preserved_posture",
    "packet_emission_not_transfer_posture",
    "transfer_not_performed_posture",
    "copy_to_another_device_not_performed_posture",
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
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "packet_transfer_boundary_scope",
    "packet_transfer_boundary_checks",
    "packet_transfer_boundary_statement",
    "packet_transfer_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_packet_transfer_boundary_summary",
)

SELECTED_BASIS_SECTIONS = (
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
)

TRUE_RECORDED_FIELDS = (
    "packet_transfer_boundary_recorded",
    "one_future_transfer_step_declared",
    "packet_emission_basis_preserved",
    "emitted_packet_basis_preserved",
    "packet_emission_not_transfer",
    "transfer_not_performed",
    "copy_to_another_device_not_performed",
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
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

FALSE_NON_CLAIMS_TO_CHECK = (
    "packet_transferred",
    "packet_copied_to_another_device",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_receipt_created",
    "second_carrier_execution_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "packet_transfer_boundary_treated_as_transfer",
    "packet_transfer_boundary_treated_as_copy_authorization",
    "packet_transfer_boundary_treated_as_source_transfer",
    "packet_transfer_boundary_treated_as_source_receipt",
    "packet_transfer_boundary_treated_as_reception_authorization",
    "packet_transfer_boundary_treated_as_second_carrier_receipt",
    "packet_transfer_boundary_treated_as_second_carrier_execution",
    "packet_transfer_boundary_treated_as_cross_carrier_evidence",
    "packet_transfer_boundary_treated_as_source",
    "packet_transfer_boundary_treated_as_authority",
    "packet_transfer_boundary_treated_as_currentness",
    "packet_transfer_boundary_treated_as_final_completion",
    "packet_transfer_boundary_treated_as_runtime",
    "packet_transfer_boundary_treated_as_continuation",
    "packet_transfer_boundary_treated_as_reusable_permission",
    "packet_transfer_boundary_treated_as_follow_on_work",
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
    "artifact_existence_treated_as_transfer_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_transfer_authority",
    "carrier_possession_treated_as_receipt_authority",
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
    "transfer_boundary_became_transfer",
    "transfer_boundary_became_copy_authorization",
    "transfer_boundary_became_second_carrier_receipt",
    "transfer_boundary_became_second_carrier_execution",
    "transfer_boundary_became_cross_carrier_proof",
    "transfer_boundary_became_source_authority_currentness",
    "carrier_possession_became_receipt",
    "artifact_existence_became_transfer_authority",
    "artifact_path_became_currentness",
    "repo_local_availability_became_transfer_authority",
    "hidden_repo_state_became_transfer_authority",
    "v1_packet_emission_boundary_resolver_was_repaired_hidden_erased_or_claimed_passed",
)

REPRESENTATIVE_BLOCK_CODES = {
    "PACKET_TRANSFER_BOUNDARY_QUESTION_UNDECLARED",
    "PACKET_TRANSFER_BOUNDARY_INTENT_UNSUPPORTED",
    "PACKET_EMISSION_BASIS_MISSING",
    "PACKET_EMISSION_NOT_RECORDED",
    "PACKET_EMISSION_FAILED_CHECKS_PRESENT",
    "PACKET_EMISSION_VERSION_NOT_0_1_0",
    "PACKET_EMISSION_DID_NOT_RECORD_BOUNDED_PACKET_EMISSION",
    "PACKET_EMISSION_DID_NOT_PRESERVE_V1_FAILURE",
    "PACKET_EMISSION_AUTHORIZED_TRANSFER",
    "PACKET_EMISSION_AUTHORIZED_COPY_TO_ANOTHER_DEVICE",
    "PACKET_EMISSION_AUTHORIZED_SOURCE_TRANSFER",
    "PACKET_EMISSION_CREATED_SOURCE_RECEIPT",
    "PACKET_EMISSION_CREATED_RECEPTION_AUTHORIZATION",
    "PACKET_EMISSION_CREATED_SECOND_CARRIER_RECEIPT",
    "PACKET_EMISSION_AUTHORIZED_SECOND_CARRIER_EXECUTION",
    "PACKET_EMISSION_CREATED_EXTERNAL_RESULT",
    "PACKET_EMISSION_CREATED_CROSS_CARRIER_EVIDENCE",
    "PACKET_EMISSION_USED_HIDDEN_REPO_STATE_AS_TRANSFER_AUTHORITY",
    "PACKET_EMISSION_TREATED_REPO_LOCAL_AVAILABILITY_AS_TRANSFER_AUTHORITY",
    "PACKET_EMISSION_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_EMISSION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_TRANSFER",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_COPY_AUTHORIZATION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SECOND_CARRIER_RECEIPT",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SECOND_CARRIER_EXECUTION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_AUTHORITY",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CURRENTNESS",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_RUNTIME",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CONTINUATION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_TRANSFER_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_TRANSFER_AUTHORITY",
    "CARRIER_POSSESSION_TREATED_AS_RECEIPT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_TRANSFER_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_TRANSFER_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_TRANSFER",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE",
}


def _fresh_request() -> dict[str, Any]:
    request = resolver.build_declared_portable_source_body_verification_packet_transfer_boundary_request(
        packet_transfer_boundary_request_id=(
            "portable_source_body_verification_packet_transfer_boundary_unit_request_001"
        )
    )
    request["packet_transfer_boundary_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    request["declared_non_claims"].update({key: False for key in EXTRA_FALSE_NON_CLAIMS})
    request["selected_command_execution_basis"][
        "outcome"
    ] = "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED"
    return request


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _set_emission(
    request: dict[str, Any],
    shortcut_key: str,
    basis_key: str,
    value: Any,
) -> None:
    request[shortcut_key] = value
    request.setdefault("selected_packet_emission_basis", {})[basis_key] = value


def _flip_non_claim(non_claim_key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.setdefault("declared_non_claims", {})[non_claim_key] = True

    return mutate


def _missing_non_claim(non_claim_key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.setdefault("declared_non_claims", {}).pop(non_claim_key, None)

    return mutate


class PacketTransferBoundaryResolverTests(unittest.TestCase):
    def assert_block_codes_are_public(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping):
            block_code = block.get("block_code")
            if block_code is not None:
                self.assertIn(block_code, resolver.BLOCK_CODES)

        for check in result.get("packet_transfer_boundary_checks", []):
            if not isinstance(check, Mapping):
                continue
            for code_key in ("block_code", "failure_code"):
                code = check.get(code_key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_bools(self, result: Mapping[str, Any]) -> None:
        metadata = result.get(
            "portable_source_body_verification_packet_transfer_boundary_metadata", {}
        )
        for key in (
            "v1_packet_emission_boundary_failure_preserved",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
            "packet_transfer_boundary_does_not_repair_hide_or_claim_v1_passed",
        ):
            if key in metadata:
                self.assertIs(type(metadata[key]), bool)

        boolean_sections = (
            *POSTURE_SECTIONS,
            "packet_transfer_boundary_statement",
            "non_claims",
        )
        boolean_keys = set(TRUE_RECORDED_FIELDS)
        boolean_keys.update(REQUIRED_FALSE_NON_CLAIMS)
        boolean_keys.update(EXTRA_FALSE_NON_CLAIMS)
        for section_name in boolean_sections:
            section = result.get(section_name, {})
            if not isinstance(section, Mapping):
                continue
            for key, value in section.items():
                if key in boolean_keys or isinstance(value, bool):
                    self.assertIs(type(value), bool, f"{section_name}.{key}")
                    self.assertNotIn(value, REDACTION_STRINGS)

        summary = result.get(
            "portable_source_body_verification_packet_transfer_boundary_summary", {}
        )
        summary_bool_keys = {
            *TRUE_RECORDED_FIELDS,
            "v1_predecessor_failure_preserved",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
            "no_transfer_copy_receipt_execution_cross_carrier_evidence",
            "no_source_authority_currentness_final_completion_runtime",
            "no_deployment_public_release_follow_on",
        }
        for key in summary_bool_keys:
            if key in summary:
                self.assertIs(type(summary[key]), bool, f"summary.{key}")
        for key, value in summary.get("key_non_claims", {}).items():
            self.assertIs(type(value), bool, f"summary.key_non_claims.{key}")

        for check in result.get("packet_transfer_boundary_checks", []):
            if isinstance(check, Mapping) and "passed" in check:
                self.assertIs(type(check["passed"]), bool)

    def assert_no_raw_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _json_text(result)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(RAW_TRANSFER_SENTINEL, serialized)
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
            "artifact_existence_treated_as_transfer_authority",
            "artifact_path_treated_as_currentness",
            "repo_local_availability_treated_as_transfer_authority",
            "carrier_possession_treated_as_receipt_authority",
            "hidden_repo_state_used_as_transfer_content",
            "hidden_repo_state_used_as_transfer_authority",
            "consumed_request_reopened",
            "authorization_token_reused",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
        ):
            if key in non_claims:
                self.assertIs(non_claims[key], False, key)

        block = result.get("block")
        if isinstance(block, Mapping):
            for key in (
                "packet_transferred",
                "packet_copied_to_another_device",
                "source_created",
                "authority_created",
                "currentness_created",
                "runtime_hosting_created",
                "follow_on_work_authorized",
                "consumed_request_reopened",
                "authorization_token_reused",
                "v1_repaired",
                "v1_hidden",
                "v1_claimed_passed",
            ):
                if key in block:
                    self.assertIs(block[key], False, key)

    def _resolve_block_case(
        self,
        mutate: Callable[[dict[str, Any]], None],
    ) -> dict[str, Any]:
        request = _fresh_request()
        mutate(request)
        return resolver.resolve_portable_source_body_verification_packet_transfer_boundary(
            declared_packet_transfer_boundary_request=request
        )

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_packet_transfer_boundary",
            "resolve_portable_source_body_verification_packet_transfer_boundary_from_path",
            "write_portable_source_body_verification_packet_transfer_boundary_result",
            "build_portable_source_body_verification_packet_transfer_boundary_summary",
            "build_declared_portable_source_body_verification_packet_transfer_boundary_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "packet_transfer_boundary"
            )
        )
        self.assertTrue(REPRESENTATIVE_BLOCK_CODES.issubset(set(resolver.BLOCK_CODES)))
        self.assertIn("PACKET_TRANSFER_BOUNDARY_ONLY", SUPPORTED_SCOPE)
        self.assertIn("ONE_FUTURE_TRANSFER_STEP_ONLY", SUPPORTED_SCOPE)
        self.assertIn("CARRIER_POSSESSION_NOT_RECEIPT_AUTHORITY", SUPPORTED_SCOPE)
        for key in (
            "packet_transferred",
            "packet_transfer_boundary_treated_as_transfer",
            "carrier_possession_treated_as_receipt_authority",
            "hidden_repo_state_used_as_transfer_authority",
        ):
            self.assertIn(key, REQUIRED_FALSE_NON_CLAIMS)

    def test_successful_packet_transfer_boundary_recorded_result(self) -> None:
        request = _fresh_request()
        original_request = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_packet_transfer_boundary(
            declared_packet_transfer_boundary_request=request
        )

        self.assertEqual(request, original_request)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        metadata = result["portable_source_body_verification_packet_transfer_boundary_metadata"]
        self.assertEqual(metadata["failed_check_count"], 0)
        self.assertGreater(metadata["passed_check_count"], 0)
        self.assertIsNone(result["block"]["block_code"])

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        self.assertEqual(
            metadata["portable_source_body_verification_packet_transfer_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_packet_transfer_boundary",
        )
        self.assertEqual(
            metadata["packet_transfer_boundary_request_id"],
            "portable_source_body_verification_packet_transfer_boundary_unit_request_001",
        )
        self.assertIs(metadata["v1_packet_emission_boundary_failure_preserved"], True)
        self.assertIs(metadata["v1_repaired"], False)
        self.assertIs(metadata["v1_hidden"], False)
        self.assertIs(metadata["v1_claimed_passed"], False)

        statement = result["packet_transfer_boundary_statement"]
        for key in TRUE_RECORDED_FIELDS:
            self.assertIn(key, statement)
            self.assertIs(statement[key], True, key)

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
        for key in FALSE_NON_CLAIMS_TO_CHECK:
            if key in non_claims:
                self.assertIs(non_claims[key], False, key)

        non_meaning = result["packet_transfer_boundary_non_meaning"]
        for key in NON_MEANING_FALSE_FIELDS:
            self.assertIn(key, non_meaning)
            self.assertIs(non_meaning[key], False, key)

        emission_basis = result["selected_packet_emission_basis"]
        self.assertEqual(
            emission_basis["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_RECORDED",
        )
        self.assertEqual(emission_basis["result_version"], "0.1.0")
        self.assertEqual(emission_basis["failed_check_count"], 0)
        self.assertIs(emission_basis["bounded_packet_emission_recorded"], True)
        self.assertIs(emission_basis["packet_emission_boundary_v1_failure_preserved"], True)
        self.assertIs(emission_basis["packet_transfer_not_authorized"], True)
        self.assertIs(emission_basis["copy_to_another_device_not_authorized"], True)
        self.assertIs(emission_basis["source_transfer_not_authorized"], True)
        self.assertIs(emission_basis["source_receipt_not_created"], True)
        self.assertIs(emission_basis["reception_authorization_not_created"], True)
        self.assertIs(emission_basis["second_carrier_receipt_not_created"], True)
        self.assertIs(emission_basis["second_carrier_execution_not_authorized"], True)
        self.assertIs(emission_basis["external_result_not_created"], True)
        self.assertIs(emission_basis["cross_carrier_evidence_not_created"], True)
        self.assertIs(emission_basis["hidden_repo_state_not_used_as_transfer_authority"], True)
        self.assertIs(emission_basis["repo_local_availability_not_transfer_authority"], True)
        self.assertIs(
            emission_basis["raw_full_prior_artifact_body_not_returned"],
            True,
        )

        self.assertEqual(
            result["selected_packet_emission_boundary_v2_basis"]["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_RECORDED",
        )
        self.assertIs(
            result["selected_packet_emission_boundary_v1_predecessor_failure_basis"][
                "v1_predecessor_failure_preserved"
            ],
            True,
        )
        self.assertIs(
            result["selected_packet_emission_boundary_v1_predecessor_failure_basis"][
                "v1_repaired"
            ],
            False,
        )
        self.assertEqual(
            result["selected_packet_artifact_basis"]["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED",
        )
        self.assertEqual(
            result["selected_packet_boundary_basis"]["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            result["selected_command_success_basis"]["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED",
        )
        self.assertEqual(
            result["selected_command_result_v2_basis"]["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED",
        )
        self.assertEqual(
            result["selected_output_capture_v2_basis"]["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED",
        )
        self.assertEqual(
            result["selected_command_output_report_artifact_basis"]["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED",
        )
        self.assertEqual(
            result["selected_command_execution_basis"]["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED",
        )
        self.assertIs(result["selected_command_execution_basis"]["audit_only"], True)
        self.assertIs(result["selected_command_report_lineage_basis"]["lineage_only"], True)

        self.assert_block_codes_are_public(result)
        self.assert_generated_booleans_are_bools(result)
        self.assert_no_raw_sentinels(result)
        self.assert_no_later_work_created(result)

    def test_summary_helper_preserves_packet_transfer_boundary_posture(self) -> None:
        result = resolver.resolve_portable_source_body_verification_packet_transfer_boundary(
            declared_packet_transfer_boundary_request=_fresh_request()
        )
        summary = resolver.build_portable_source_body_verification_packet_transfer_boundary_summary(
            result
        )

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["request_id"],
            "portable_source_body_verification_packet_transfer_boundary_unit_request_001",
        )
        self.assertEqual(summary["question"], resolver.CORE_QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)

        for key in TRUE_RECORDED_FIELDS:
            self.assertIn(key, summary)
            self.assertIs(summary[key], True, key)

        self.assertEqual(
            summary["selected_packet_emission_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_RECORDED",
        )
        self.assertEqual(summary["selected_packet_emission_version"], "0.1.0")
        self.assertEqual(summary["selected_packet_emission_failed_check_count"], 0)
        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_repaired"], False)
        self.assertIs(summary["v1_hidden"], False)
        self.assertIs(summary["v1_claimed_passed"], False)
        self.assertIs(
            summary["no_transfer_copy_receipt_execution_cross_carrier_evidence"], True
        )
        self.assertIs(
            summary["no_source_authority_currentness_final_completion_runtime"], True
        )
        self.assertIs(summary["no_deployment_public_release_follow_on"], True)

        for key, value in summary["key_non_claims"].items():
            self.assertIs(type(value), bool, key)
            self.assertIs(value, False, key)

        statement = result["packet_transfer_boundary_statement"]
        for key in (
            "transfer_not_performed",
            "copy_to_another_device_not_performed",
            "second_carrier_receipt_not_created",
            "second_carrier_execution_not_authorized",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "runtime_not_created",
            "follow_on_work_not_authorized",
        ):
            self.assertIs(statement[key], True, key)

    def test_representative_blocking_behavior(self) -> None:
        malformed_results = (
            resolver.resolve_portable_source_body_verification_packet_transfer_boundary(
                declared_packet_transfer_boundary_request=None
            ),
            resolver.resolve_portable_source_body_verification_packet_transfer_boundary(
                declared_packet_transfer_boundary_request=["not", "a", "mapping"]
            ),
        )
        for result in malformed_results:
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertIsNotNone(result["block"]["block_code"])
            self.assert_block_codes_are_public(result)
            self.assert_generated_booleans_are_bools(result)
            self.assert_no_later_work_created(result)

        block_cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", lambda r: r.update({"packet_transfer_boundary_intent": resolver.INTENT_BLOCK})),
            ("undeclared question", lambda r: r.update({"packet_transfer_boundary_question": ""})),
            ("unsupported intent", lambda r: r.update({"packet_transfer_boundary_intent": "UNSUPPORTED_INTENT"})),
            (
                "unsupported scope",
                lambda r: r["packet_transfer_boundary_scope"].append(
                    "UNSUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE_VALUE"
                ),
            ),
            ("missing packet emission basis", lambda r: r.pop("selected_packet_emission_basis")),
            (
                "missing packet emission terminal summary",
                lambda r: r.pop("selected_packet_emission_terminal_summary_basis"),
            ),
            (
                "missing packet emission boundary v2",
                lambda r: r.pop("selected_packet_emission_boundary_v2_basis"),
            ),
            (
                "missing v1 predecessor failure",
                lambda r: r.pop("selected_packet_emission_boundary_v1_predecessor_failure_basis"),
            ),
            ("missing packet artifact basis", lambda r: r.pop("selected_packet_artifact_basis")),
            (
                "packet emission not recorded",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_result_outcome",
                    "outcome",
                    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_NOT_RECORDED",
                ),
            ),
            (
                "packet emission failed checks",
                lambda r: _set_emission(
                    r, "selected_packet_emission_failed_check_count", "failed_check_count", 1
                ),
            ),
            (
                "packet emission wrong version",
                lambda r: _set_emission(
                    r, "selected_packet_emission_result_version", "result_version", "0.2.0"
                ),
            ),
            (
                "packet emission did not record bounded emission",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_bounded_packet_emission_recorded",
                    "bounded_packet_emission_recorded",
                    False,
                ),
            ),
            (
                "packet emission did not preserve v1 failure",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_v1_failure_preserved",
                    "packet_emission_boundary_v1_failure_preserved",
                    False,
                ),
            ),
            (
                "packet emission authorized transfer",
                lambda r: _set_emission(
                    r, "selected_packet_emission_authorized_transfer", "packet_transfer_authorized", True
                ),
            ),
            (
                "packet emission authorized copy",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_authorized_copy_to_another_device",
                    "copy_to_another_device_authorized",
                    True,
                ),
            ),
            (
                "packet emission authorized source transfer",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_authorized_source_transfer",
                    "source_transfer_authorized",
                    True,
                ),
            ),
            (
                "packet emission created source receipt",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_created_source_receipt",
                    "source_receipt_created",
                    True,
                ),
            ),
            (
                "packet emission created reception authorization",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_created_reception_authorization",
                    "reception_authorization_created",
                    True,
                ),
            ),
            (
                "packet emission created second carrier receipt",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_created_second_carrier_receipt",
                    "second_carrier_receipt_created",
                    True,
                ),
            ),
            (
                "packet emission authorized second carrier execution",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_authorized_second_carrier_execution",
                    "second_carrier_execution_authorized",
                    True,
                ),
            ),
            (
                "packet emission created external result",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_created_external_result",
                    "external_result_created",
                    True,
                ),
            ),
            (
                "packet emission created cross carrier evidence",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_created_cross_carrier_evidence",
                    "cross_carrier_evidence_created",
                    True,
                ),
            ),
            (
                "packet emission used hidden repo state as transfer authority",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_used_hidden_repo_state_as_transfer_authority",
                    "hidden_repo_state_used_as_transfer_authority",
                    True,
                ),
            ),
            (
                "packet emission treated repo local availability as transfer authority",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_treated_repo_local_availability_as_transfer_authority",
                    "repo_local_availability_treated_as_transfer_authority",
                    True,
                ),
            ),
            (
                "packet emission returned raw prior body outside bounded emission",
                lambda r: _set_emission(
                    r,
                    "selected_packet_emission_raw_full_prior_artifact_body_returned_outside_bounded_emission",
                    "raw_full_prior_artifact_body_returned_outside_bounded_emission",
                    True,
                ),
            ),
            (
                "execution trace not audit only",
                lambda r: r["selected_command_execution_basis"].update(
                    {"execution_trace_audit_only": False, "audit_only": False}
                ),
            ),
            (
                "command report lineage not lineage only",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    {"command_report_lineage_only": False, "lineage_only": False}
                ),
            ),
            (
                "command report lineage treated as current report artifact",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    {"command_report_lineage_treated_as_current_report_artifact": True}
                ),
            ),
            (
                "command report lineage treated as source",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    {"command_report_lineage_treated_as_source": True}
                ),
            ),
            (
                "command report lineage treated as authority",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    {"command_report_lineage_treated_as_authority": True}
                ),
            ),
            (
                "command report lineage treated as currentness",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    {"command_report_lineage_treated_as_currentness": True}
                ),
            ),
            (
                "predecessor failure hidden or repaired",
                lambda r: r["selected_predecessor_failure_basis"].update(
                    {"predecessor_failure_evidence_hidden_or_repaired": True}
                ),
            ),
            ("selected basis not reference shaped", lambda r: r.update({"reference_shaped_input_posture": False})),
            ("raw full prior artifact body returned", _flip_non_claim("raw_full_prior_artifact_body_returned")),
            ("consumed request reopened", _flip_non_claim("consumed_request_reopened")),
            ("authorization token reused", _flip_non_claim("authorization_token_reused")),
            (
                "full prior body emitted outside bounded transfer",
                lambda r: r.update({"full_prior_artifact_body_emitted_outside_bounded_transfer": True}),
            ),
            ("artifacts mutated", _flip_non_claim("prior_artifacts_mutated")),
            ("required non claim missing", _missing_non_claim("packet_transferred")),
            (
                "required non claim flipped",
                _flip_non_claim("packet_transfer_boundary_treated_as_transfer"),
            ),
        )

        non_claim_block_cases = tuple(
            (f"non claim flipped {key}", _flip_non_claim(key))
            for key in FALSE_NON_CLAIMS_TO_CHECK
            if key
            not in {
                "packet_transfer_boundary_treated_as_transfer",
                "raw_full_prior_artifact_body_returned",
                "prior_artifacts_mutated",
                "consumed_request_reopened",
                "authorization_token_reused",
            }
        )

        for label, mutate in (*block_cases, *non_claim_block_cases):
            with self.subTest(label=label):
                result = self._resolve_block_case(mutate)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIsNotNone(result["block"]["block_code"])
                self.assert_block_codes_are_public(result)
                self.assert_generated_booleans_are_bools(result)
                self.assert_no_later_work_created(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            request_path = temp_dir / "declared_packet_transfer_boundary_request.json"
            request_path.write_text(_json_text(_fresh_request()), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_packet_transfer_boundary_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result[
                "portable_source_body_verification_packet_transfer_boundary_metadata"
            ]
            self.assertEqual(
                metadata["portable_source_body_verification_packet_transfer_boundary_result_version"],
                "0.1.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_packet_transfer_boundary",
            )

            malformed_path = temp_dir / "malformed.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationPacketTransferBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_packet_transfer_boundary_from_path(
                    malformed_path
                )

            array_path = temp_dir / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationPacketTransferBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_packet_transfer_boundary_from_path(
                    array_path
                )

            with self.assertRaises(
                resolver.PortableSourceBodyVerificationPacketTransferBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_packet_transfer_boundary_from_path(
                    temp_dir / "missing.json"
                )

            output_root = (
                temp_dir
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_transfer_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_packet_transfer_boundary_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_packet_transfer_boundary_result(
                    result
                )

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(second_path.stem.rsplit("_", 1)[-1], "001")
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], RECORDED)
            self.assertEqual(json.loads(second_path.read_text(encoding="utf-8"))["outcome"], RECORDED)
            self.assertIn(
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_packet_transfer_boundary",
                first_path.as_posix(),
            )
            forbidden_fragments = (
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission/",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_transfer/",
                "second_carrier",
                "cross_carrier",
                "runtime",
                "deployment",
                "public_release",
            )
            for fragment in forbidden_fragments:
                self.assertNotIn(fragment, first_path.as_posix())
                self.assertNotIn(fragment, second_path.as_posix())

    def test_non_mutation(self) -> None:
        request = _fresh_request()
        selected_before = {
            key: copy.deepcopy(request[key])
            for key in SELECTED_BASIS_SECTIONS
        }
        posture_before = {
            key: copy.deepcopy(request[key])
            for key in POSTURE_SECTIONS
        }
        scope_before = copy.deepcopy(request["packet_transfer_boundary_scope"])
        non_claims_before = copy.deepcopy(request["declared_non_claims"])
        request_before = copy.deepcopy(request)

        resolver.resolve_portable_source_body_verification_packet_transfer_boundary(
            declared_packet_transfer_boundary_request=request
        )

        self.assertEqual(request, request_before)
        for key in SELECTED_BASIS_SECTIONS:
            self.assertEqual(request[key], selected_before[key], key)
        for key in POSTURE_SECTIONS:
            self.assertEqual(request[key], posture_before[key], key)
        self.assertEqual(request["packet_transfer_boundary_scope"], scope_before)
        self.assertEqual(request["declared_non_claims"], non_claims_before)

    def test_raw_full_body_and_hidden_state_containment(self) -> None:
        request = _fresh_request()
        hostile_payload = {
            "raw_body": HOSTILE_RAW_VALUE,
            "raw_full_body": {"nested": [RAW_SENTINEL]},
            "full_body": HOSTILE_RAW_VALUE,
            "artifact_body": HOSTILE_RAW_VALUE,
            "raw_result_body": HOSTILE_RAW_VALUE,
            "raw_output_body": HOSTILE_RAW_VALUE,
            "transfer_body": HOSTILE_RAW_VALUE,
            "copy_body": HOSTILE_RAW_VALUE,
            "packet_body": HOSTILE_RAW_VALUE,
            "source_body": HOSTILE_RAW_VALUE,
            "authority_body": HOSTILE_RAW_VALUE,
            "hidden_repo_state": {"sentinel": RAW_SENTINEL},
            "current_working_tree": HOSTILE_RAW_VALUE,
            "local_cache": HOSTILE_RAW_VALUE,
            "repo_local_only_dependency": HOSTILE_RAW_VALUE,
            "carrier_possession": {
                "reference_only": True,
                "carrier_possession_treated_as_receipt_authority": False,
            },
            "unlisted_file_dependency": HOSTILE_RAW_VALUE,
            "nested_payload": [
                {"raw_body": RAW_SENTINEL},
                {"transfer_body": HOSTILE_RAW_VALUE},
            ],
        }
        for section in (
            "selected_packet_emission_basis",
            "selected_packet_emission_boundary_v2_basis",
            "selected_packet_artifact_basis",
            "selected_packet_boundary_basis",
            "selected_command_success_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        ):
            request[section].update(copy.deepcopy(hostile_payload))

        request_before = copy.deepcopy(request)
        result = resolver.resolve_portable_source_body_verification_packet_transfer_boundary(
            declared_packet_transfer_boundary_request=request
        )

        self.assertEqual(request, request_before)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_block_codes_are_public(result)
        self.assert_generated_booleans_are_bools(result)
        self.assert_no_raw_sentinels(result)
        self.assert_no_later_work_created(result)

        non_claims = result["non_claims"]
        self.assertIs(non_claims["hidden_repo_state_used_as_transfer_content"], False)
        self.assertIs(non_claims["hidden_repo_state_used_as_transfer_authority"], False)
        self.assertIs(non_claims["repo_local_availability_treated_as_transfer_authority"], False)
        self.assertIs(non_claims["carrier_possession_treated_as_receipt_authority"], False)

        statement = result["packet_transfer_boundary_statement"]
        for key in (
            "hidden_repo_state_excluded",
            "hidden_repo_state_not_used_as_transfer_authority",
            "repo_local_availability_not_transfer_authority",
            "carrier_possession_not_receipt_authority",
            "selected_basis_reference_shape_preserved",
            "raw_full_prior_artifact_body_not_returned",
        ):
            self.assertIs(type(statement[key]), bool, key)
            self.assertNotIn(statement[key], REDACTION_STRINGS)


if __name__ == "__main__":
    unittest.main()
