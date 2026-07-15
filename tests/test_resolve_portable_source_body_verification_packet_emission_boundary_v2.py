"""Tests for the packet-emission-boundary v2 resolver.

This suite is bounded to packet-emission-boundary posture only. It preserves
v1 as visible predecessor conformance-failure evidence and verifies that v2
keeps generated posture, non-claim, summary, check, and metadata booleans as
booleans while still containing hostile raw-body and hidden-state payloads in
selected basis material.
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

import resolve_portable_source_body_verification_packet_emission_boundary_v2 as resolver


RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_RECORDED"
BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = {
    RECORDED,
    BLOCKED,
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_NOT_RECORDED",
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
}
REDACTION = "[bounded-redacted-raw-or-hidden-state]"
RAW_SENTINEL = "RAW_PACKET_EMISSION_BOUNDARY_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_PACKET_EMISSION_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN"
CORE_QUESTION = getattr(resolver, "EXPECTED_QUESTION", resolver.CORE_QUESTION)

TOP_LEVEL_SECTIONS = [
    "portable_source_body_verification_packet_emission_boundary_metadata",
    "declared_packet_emission_boundary_question",
    "selected_packet_artifact_basis",
    "selected_packet_artifact_terminal_summary_basis",
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
    "packet_emission_boundary_only_posture",
    "one_future_packet_emission_step_posture",
    "packet_artifact_basis_preserved_posture",
    "local_packet_artifact_recorded_posture",
    "packet_artifact_not_emission_posture",
    "packet_not_emitted_posture",
    "emitted_packet_not_created_posture",
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
    "packet_emission_boundary_scope",
    "packet_emission_boundary_checks",
    "packet_emission_boundary_statement",
    "packet_emission_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_packet_emission_boundary_summary",
]

TRUE_RECORDED_FIELDS = [
    "packet_emission_boundary_recorded",
    "one_future_packet_emission_step_declared",
    "packet_artifact_basis_preserved",
    "local_packet_artifact_recorded",
    "packet_artifact_not_emission",
    "packet_not_emitted",
    "emitted_packet_not_created",
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
]

FALSE_NON_CLAIM_FIELDS = list(resolver.REQUIRED_FALSE_NON_CLAIMS)

REPRESENTATIVE_BLOCK_CODES = [
    "PACKET_EMISSION_BOUNDARY_QUESTION_UNDECLARED",
    "PACKET_EMISSION_BOUNDARY_INTENT_UNSUPPORTED",
    "PACKET_ARTIFACT_BASIS_MISSING",
    "PACKET_ARTIFACT_NOT_RECORDED",
    "PACKET_ARTIFACT_FAILED_CHECKS_PRESENT",
    "PACKET_ARTIFACT_VERSION_NOT_0_1_0",
    "PACKET_ARTIFACT_DID_NOT_RECORD_LOCAL_PACKET_ARTIFACT",
    "PACKET_ARTIFACT_ALREADY_EMITTED_PACKET",
    "PACKET_ARTIFACT_ALREADY_TRANSFERRED_PACKET",
    "PACKET_ARTIFACT_COPIED_PACKET_TO_ANOTHER_DEVICE",
    "PACKET_ARTIFACT_AUTHORIZED_SOURCE_TRANSFER",
    "PACKET_ARTIFACT_AUTHORIZED_SOURCE_RECEIPT",
    "PACKET_ARTIFACT_AUTHORIZED_RECEPTION",
    "PACKET_ARTIFACT_AUTHORIZED_SECOND_CARRIER_EXECUTION",
    "PACKET_ARTIFACT_CREATED_EXTERNAL_RESULT",
    "PACKET_ARTIFACT_CREATED_CROSS_CARRIER_EVIDENCE",
    "PACKET_ARTIFACT_USED_HIDDEN_REPO_STATE_AS_EMISSION_AUTHORITY",
    "PACKET_ARTIFACT_TREATED_REPO_LOCAL_AVAILABILITY_AS_EMISSION_AUTHORITY",
    "PACKET_ARTIFACT_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
    "PACKET_ARTIFACT_TREATED_ARTIFACT_EXISTENCE_AS_EMISSION_AUTHORITY",
    "PACKET_ARTIFACT_TREATED_ARTIFACT_PATH_AS_CURRENTNESS",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_EMISSION",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_TRANSFER",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_COPY_AUTHORIZATION",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_SECOND_CARRIER_RECEIPT",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_SECOND_CARRIER_EXECUTION",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_SOURCE",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_AUTHORITY",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_CURRENTNESS",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_RUNTIME",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_CONTINUATION",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "PACKET_EMISSION_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "PACKET_EMITTED",
    "EMITTED_PACKET_CREATED",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_PACKET_EMISSION_BOUNDARY_SCOPE",
    "V1_SANITIZER_POSTURE_BOOL_CONFORMANCE_FAILURE_PRESERVED",
    "GENERATED_BOOLEAN_POSTURE_REDACTED",
    "GENERATED_NON_CLAIM_BOOLEAN_REDACTED",
    "GENERATED_SUMMARY_BOOLEAN_REDACTED",
]

SHORTCUT_FIELDS = [
    "selected_packet_artifact_result_outcome",
    "selected_packet_artifact_result_version",
    "selected_packet_artifact_failed_check_count",
    "selected_packet_artifact_recorded_local_packet_artifact",
    "selected_packet_artifact_packet_emitted",
    "selected_packet_artifact_packet_transferred",
    "selected_packet_artifact_copied_packet_to_another_device",
    "selected_packet_artifact_authorized_source_transfer",
    "selected_packet_artifact_authorized_source_receipt",
    "selected_packet_artifact_authorized_reception",
    "selected_packet_artifact_authorized_second_carrier_execution",
    "selected_packet_artifact_created_external_result",
    "selected_packet_artifact_created_cross_carrier_evidence",
    "selected_packet_artifact_used_hidden_repo_state_as_emission_authority",
    "selected_packet_artifact_treated_repo_local_availability_as_emission_authority",
    "selected_packet_artifact_raw_full_prior_artifact_body_returned",
    "selected_packet_artifact_treated_artifact_existence_as_emission_authority",
    "selected_packet_artifact_treated_artifact_path_as_currentness",
]


def _basis(label: str, outcome: str | None = None) -> dict[str, Any]:
    basis: dict[str, Any] = {
        "basis_label": label,
        "basis_id": f"{label}_basis_001",
        "declared": True,
        "basis_only": True,
        "reference_shaped": True,
        "selected_basis_reference_shape_preserved": True,
        "hidden_repo_state_excluded": True,
        "hidden_repo_state_not_used_as_emission_authority": True,
        "hidden_repo_state_used_as_emission_content": False,
        "hidden_repo_state_used_as_emission_authority": False,
        "repo_local_availability_not_emission_authority": True,
        "repo_local_availability_treated_as_emission_authority": False,
        "raw_full_prior_artifact_body_not_returned": True,
        "raw_full_prior_artifact_body_returned": False,
        "artifact_existence_treated_as_emission_authority": False,
        "artifact_path_treated_as_currentness": False,
        "packet_emitted": False,
        "packet_transferred": False,
        "packet_copied_to_another_device": False,
        "source_transfer_authorized": False,
        "source_receipt_authorized": False,
        "reception_authorization_created": False,
        "second_carrier_receipt_created": False,
        "second_carrier_execution_created": False,
        "external_result_created": False,
        "cross_carrier_evidence_created": False,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_claimed": False,
        "runtime_hosting_created": False,
        "follow_on_work_authorized": False,
    }
    if outcome is not None:
        basis["outcome"] = outcome
    return basis


def _clean_packet_artifact_basis() -> dict[str, Any]:
    basis = _basis(
        "packet_artifact",
        "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED",
    )
    basis.update(
        {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "packet_artifact_recorded": True,
            "one_local_packet_artifact_recorded": True,
            "local_packet_artifact_recorded": True,
            "packet_artifact_not_emission": True,
            "packet_not_emitted": True,
            "packet_not_transferred": True,
            "packet_transfer_not_authorized": True,
            "copy_to_another_device_not_authorized": True,
            "source_transfer_not_authorized": True,
            "source_receipt_not_created": True,
            "reception_authorization_not_created": True,
            "second_carrier_receipt_not_created": True,
            "second_carrier_execution_not_authorized": True,
            "external_result_not_created": True,
            "cross_carrier_evidence_not_created": True,
            "source_not_created": True,
            "authority_not_created": True,
            "currentness_not_created": True,
            "final_completion_not_created": True,
            "runtime_not_created": True,
            "follow_on_work_not_authorized": True,
            "emitted_packet_created": False,
            "packet_emitted": False,
            "packet_transferred": False,
            "packet_copied_to_another_device": False,
            "source_transfer_authorized": False,
            "source_receipt_authorized": False,
            "reception_authorization_created": False,
            "second_carrier_execution_authorized": False,
            "second_carrier_execution_created": False,
            "external_result_created": False,
            "cross_carrier_evidence_created": False,
        }
    )
    return basis


def _valid_request() -> dict[str, Any]:
    request = resolver.build_declared_portable_source_body_verification_packet_emission_boundary_v2_request(
        packet_emission_boundary_request_id="packet_emission_boundary_v2_reference_review_001",
        selected_packet_artifact_result_path="artifacts/synthetic/packet_artifact_result.json",
    )
    for field in SHORTCUT_FIELDS:
        request.pop(field, None)
    request.update(
        {
            "packet_emission_boundary_request_id": "packet_emission_boundary_v2_reference_review_001",
            "packet_emission_boundary_question": CORE_QUESTION,
            "packet_emission_boundary_intent": "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY",
            "selected_packet_artifact_basis": _clean_packet_artifact_basis(),
            "selected_packet_artifact_terminal_summary_basis": _basis("packet_artifact_terminal_summary"),
            "selected_packet_boundary_basis": _basis(
                "packet_boundary",
                "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED",
            ),
            "selected_command_success_basis": _basis(
                "command_success",
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED",
            ),
            "selected_command_result_v2_basis": _basis(
                "command_result_v2",
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED",
            ),
            "selected_output_capture_v2_basis": _basis(
                "output_capture_v2",
                "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED",
            ),
            "selected_command_output_report_artifact_basis": _basis(
                "command_output_report_artifact",
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED",
            ),
            "selected_command_execution_basis": _basis(
                "command_execution",
                "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED",
            ),
            "selected_command_report_lineage_basis": _basis("command_report_lineage"),
            "selected_predecessor_failure_basis": _basis("predecessor_failure"),
            "selected_evidence_manifest_basis": _basis("evidence_manifest"),
            "selected_artifact_containment_basis": _basis("artifact_containment"),
            "selected_portable_verification_basis": _basis("portable_verification"),
            "packet_emission_boundary_scope": list(resolver.SUPPORTED_PACKET_EMISSION_BOUNDARY_SCOPE),
            "declared_non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
        }
    )
    request["selected_command_execution_basis"].update(
        {"execution_trace_audit_only": True, "audit_only": True}
    )
    request["selected_command_report_lineage_basis"].update(
        {
            "lineage_only": True,
            "command_report_lineage_treated_as_current_report_artifact": False,
            "command_report_lineage_treated_as_source": False,
            "command_report_lineage_treated_as_authority": False,
            "command_report_lineage_treated_as_currentness": False,
            "treated_as_current_report_artifact": False,
            "treated_as_source": False,
            "treated_as_authority": False,
            "treated_as_currentness": False,
        }
    )
    request["selected_predecessor_failure_basis"].update(
        {
            "predecessor_failures_visible": True,
            "predecessor_failure_evidence_visible": True,
            "predecessor_failure_evidence_hidden_or_repaired": False,
            "predecessor_failures_repaired": False,
            "predecessor_failures_hidden": False,
            "predecessor_failures_claimed_passed": False,
            "predecessor_failure_evidence_repaired": False,
            "predecessor_failure_evidence_hidden": False,
            "predecessor_failure_evidence_claimed_passed": False,
            "hidden": False,
            "repaired": False,
            "claimed_passed": False,
        }
    )
    for posture_key in resolver.POSTURE_KEYS:
        posture = request.setdefault(posture_key, {})
        posture.update(
            {
                "declared": True,
                "posture_declared": True,
                "posture_only": True,
                "hidden_repo_state_excluded": True,
                "hidden_repo_state_not_used_as_emission_authority": True,
                "hidden_repo_state_used_as_emission_content": False,
                "hidden_repo_state_used_as_emission_authority": False,
                "repo_local_availability_not_emission_authority": True,
                "raw_full_prior_artifact_body_not_returned": True,
            }
        )
    return request


def _set_path(mapping: dict[str, Any], path: list[str], value: Any) -> None:
    target = mapping
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def _delete_path(mapping: dict[str, Any], path: list[str]) -> None:
    target = mapping
    for key in path[:-1]:
        target = target[key]
    del target[path[-1]]


class PortableSourceBodyVerificationPacketEmissionBoundaryV2Tests(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in result.get("packet_emission_boundary_checks", []):
            self.assertIsInstance(check.get("passed"), bool)
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_bool_field(
        self,
        mapping: Mapping[str, Any],
        key: str,
        expected: bool,
        *,
        required: bool = True,
    ) -> None:
        if key not in mapping:
            if required:
                self.fail(f"{key} missing from mapping")
            return
        value = mapping[key]
        self.assertIsInstance(value, bool, key)
        self.assertIs(value, expected, key)
        self.assertNotEqual(value, REDACTION)

    def assert_no_overreach_created(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims", {})
        for key in [
            "packet_emitted",
            "emitted_packet_created",
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
        ]:
            self.assert_bool_field(non_claims, key, False)

    def assert_generated_booleans_are_preserved(self, result: Mapping[str, Any]) -> None:
        metadata = result["portable_source_body_verification_packet_emission_boundary_metadata"]
        self.assert_bool_field(metadata, "v1_predecessor_failure_preserved", True)
        self.assert_bool_field(metadata, "v1_repaired", False)
        self.assert_bool_field(metadata, "v1_hidden", False)
        self.assert_bool_field(metadata, "v1_claimed_passed", False)
        self.assert_bool_field(metadata, "v2_successor_does_not_erase_v1", True)

        statement = result["packet_emission_boundary_statement"]
        recorded = result["outcome"] == RECORDED
        if recorded:
            for key in TRUE_RECORDED_FIELDS:
                self.assert_bool_field(statement, key, True)
        self.assert_bool_field(
            statement,
            "hidden_repo_state_used_as_emission_content",
            False,
            required=False,
        )
        self.assert_bool_field(
            statement,
            "hidden_repo_state_used_as_emission_authority",
            False,
            required=False,
        )
        self.assert_bool_field(statement, "hidden_repo_state_excluded", recorded, required=False)
        self.assert_bool_field(
            statement,
            "repo_local_availability_not_emission_authority",
            recorded,
            required=False,
        )

        non_claims = result["non_claims"]
        for key in FALSE_NON_CLAIM_FIELDS:
            self.assert_bool_field(non_claims, key, False)

        summary = result["portable_source_body_verification_packet_emission_boundary_summary"]
        for key in TRUE_RECORDED_FIELDS:
            self.assert_bool_field(summary, key, result["outcome"] == RECORDED, required=False)
        self.assert_bool_field(summary, "hidden_repo_state_excluded", result["outcome"] == RECORDED)
        self.assert_bool_field(
            summary,
            "repo_local_availability_not_emission_authority",
            result["outcome"] == RECORDED,
        )
        self.assert_bool_field(summary, "v1_predecessor_failure_preserved", True)
        self.assert_bool_field(summary, "v1_repaired", False)
        self.assert_bool_field(summary, "v1_hidden", False)
        self.assert_bool_field(summary, "v1_claimed_passed", False)
        self.assert_bool_field(summary, "v2_successor_does_not_erase_v1", True)
        for key, value in summary.get("key_non_claims", {}).items():
            self.assertIsInstance(value, bool, key)
            self.assertIs(value, False, key)

        for posture_key in resolver.POSTURE_KEYS:
            posture = result[posture_key]
            self.assert_bool_field(posture, "hidden_repo_state_excluded", True, required=False)
            self.assert_bool_field(
                posture,
                "hidden_repo_state_not_used_as_emission_authority",
                True,
                required=False,
            )
            self.assert_bool_field(
                posture,
                "hidden_repo_state_used_as_emission_content",
                False,
                required=False,
            )
            self.assert_bool_field(
                posture,
                "hidden_repo_state_used_as_emission_authority",
                False,
                required=False,
            )
            self.assert_bool_field(
                posture,
                "repo_local_availability_not_emission_authority",
                True,
                required=False,
            )

        for check in result["packet_emission_boundary_checks"]:
            self.assertIsInstance(check.get("passed"), bool)
            for field in ("expected_posture", "actual_posture"):
                value = check.get(field)
                if isinstance(value, bool):
                    self.assertNotEqual(value, REDACTION)
                self.assertNotEqual(value, REDACTION)

    def assert_no_raw_payload(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)

    def test_public_api_and_constants(self) -> None:
        for name in [
            "resolve_portable_source_body_verification_packet_emission_boundary_v2",
            "resolve_portable_source_body_verification_packet_emission_boundary_v2_from_path",
            "write_portable_source_body_verification_packet_emission_boundary_v2_result",
            "build_portable_source_body_verification_packet_emission_boundary_v2_summary",
            "build_declared_portable_source_body_verification_packet_emission_boundary_v2_request",
            "resolve_portable_source_body_verification_packet_emission_boundary",
            "resolve_portable_source_body_verification_packet_emission_boundary_from_path",
            "write_portable_source_body_verification_packet_emission_boundary_result",
            "build_portable_source_body_verification_packet_emission_boundary_summary",
            "build_declared_portable_source_body_verification_packet_emission_boundary_request",
        ]:
            self.assertTrue(callable(getattr(resolver, name)))

        for name in [
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_PACKET_EMISSION_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ]:
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.2.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission_boundary_v2"
            )
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_v2_packet_emission_boundary_recorded_result(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        result = resolver.resolve_portable_source_body_verification_packet_emission_boundary_v2(
            declared_packet_emission_boundary_request=request
        )

        self.assertEqual(request, original)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        metadata = result["portable_source_body_verification_packet_emission_boundary_metadata"]
        self.assertEqual(metadata["failed_check_count"], 0)
        self.assertIsNone(result["block"]["block_code"])
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        self.assertEqual(
            metadata["portable_source_body_verification_packet_emission_boundary_result_version"],
            "0.2.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_packet_emission_boundary_v2",
        )
        self.assertEqual(
            metadata["packet_emission_boundary_request_id"],
            request["packet_emission_boundary_request_id"],
        )
        self.assertEqual(
            metadata["successor_of"],
            "resolve_portable_source_body_verification_packet_emission_boundary",
        )
        self.assert_bool_field(metadata, "v1_predecessor_failure_preserved", True)
        self.assert_bool_field(metadata, "v1_repaired", False)
        self.assert_bool_field(metadata, "v1_hidden", False)
        self.assert_bool_field(metadata, "v1_claimed_passed", False)
        self.assert_bool_field(metadata, "v2_successor_does_not_erase_v1", True)

        statement = result["packet_emission_boundary_statement"]
        for key in TRUE_RECORDED_FIELDS:
            self.assert_bool_field(statement, key, True)
        self.assert_bool_field(
            statement,
            "hidden_repo_state_used_as_emission_content",
            False,
            required=False,
        )
        self.assert_bool_field(
            statement,
            "hidden_repo_state_used_as_emission_authority",
            False,
            required=False,
        )

        non_claims = result["non_claims"]
        for key in FALSE_NON_CLAIM_FIELDS:
            self.assert_bool_field(non_claims, key, False)

        non_meaning = result["packet_emission_boundary_non_meaning"]
        for key in [
            "packet_was_emitted",
            "emitted_packet_exists",
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
            "follow_on_work_authorized",
            "artifact_existence_became_emission_authority",
            "artifact_path_became_currentness",
            "repo_local_availability_became_emission_authority",
            "hidden_repo_state_became_emission_authority",
        ]:
            self.assert_bool_field(non_meaning, key, False)

        self.assert_public_block_codes(result)
        self.assert_no_overreach_created(result)
        self.assert_generated_booleans_are_preserved(result)

    def test_summary_helper_preserves_v2_successor_and_boolean_posture(self) -> None:
        result = resolver.resolve_portable_source_body_verification_packet_emission_boundary_v2(
            declared_packet_emission_boundary_request=_valid_request()
        )
        summary = resolver.build_portable_source_body_verification_packet_emission_boundary_v2_summary(
            result
        )

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(
            summary["request_id"],
            result["portable_source_body_verification_packet_emission_boundary_metadata"][
                "packet_emission_boundary_request_id"
            ],
        )
        self.assertEqual(summary["question"], CORE_QUESTION)
        self.assertEqual(
            summary["intent"],
            "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY",
        )
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        for key in TRUE_RECORDED_FIELDS:
            self.assert_bool_field(summary, key, True)
        for key, value in summary["key_non_claims"].items():
            self.assertIsInstance(value, bool, key)
            self.assertIs(value, False, key)
        self.assertEqual(
            summary["selected_packet_artifact_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED",
        )
        self.assertEqual(summary["selected_packet_artifact_version"], "0.1.0")
        self.assertEqual(summary["selected_packet_artifact_failed_check_count"], 0)
        self.assert_bool_field(summary, "no_emission_transfer_copy_receipt_cross_carrier_evidence", True)
        self.assert_bool_field(summary, "no_source_authority_currentness_final_completion_runtime", True)
        self.assert_bool_field(summary, "no_deployment_public_release_follow_on", True)
        self.assert_bool_field(summary, "v1_predecessor_failure_preserved", True)
        self.assert_bool_field(summary, "v1_repaired", False)
        self.assert_bool_field(summary, "v1_hidden", False)
        self.assert_bool_field(summary, "v1_claimed_passed", False)
        self.assert_bool_field(summary, "v2_successor_does_not_erase_v1", True)

    def test_representative_blocking_behavior(self) -> None:
        def case(
            label: str,
            mutate: Callable[[dict[str, Any]], None],
            expected_code: str | None = None,
        ) -> tuple[str, Callable[[dict[str, Any]], None], str | None]:
            return (label, mutate, expected_code)

        def flip_non_claim(name: str) -> Callable[[dict[str, Any]], None]:
            def mutate(request: dict[str, Any]) -> None:
                request["declared_non_claims"][name] = True

            return mutate

        def emit_full_prior_artifact_body(request: dict[str, Any]) -> None:
            request["declared_non_claims"]["full_prior_artifact_body_emitted"] = True
            request["raw_full_prior_artifact_body_returned"] = True

        cases = [
            case(
                "explicit block intent",
                lambda r: _set_path(
                    r,
                    ["packet_emission_boundary_intent"],
                    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY",
                ),
                "PACKET_EMISSION_BOUNDARY_EXPLICIT_BLOCK_INTENT",
            ),
            case(
                "unsupported intent",
                lambda r: _set_path(r, ["packet_emission_boundary_intent"], "UNSUPPORTED"),
                "PACKET_EMISSION_BOUNDARY_INTENT_UNSUPPORTED",
            ),
            case(
                "unsupported scope",
                lambda r: r["packet_emission_boundary_scope"].append("UNSUPPORTED_SCOPE"),
                "UNSUPPORTED_PACKET_EMISSION_BOUNDARY_SCOPE",
            ),
            case(
                "missing packet artifact basis",
                lambda r: _delete_path(r, ["selected_packet_artifact_basis"]),
                "PACKET_ARTIFACT_BASIS_MISSING",
            ),
            case(
                "packet artifact not recorded",
                lambda r: _set_path(r, ["selected_packet_artifact_basis", "outcome"], "NOT_RECORDED"),
                "PACKET_ARTIFACT_NOT_RECORDED",
            ),
            case(
                "packet artifact failed checks",
                lambda r: _set_path(r, ["selected_packet_artifact_basis", "failed_check_count"], 1),
                "PACKET_ARTIFACT_FAILED_CHECKS_PRESENT",
            ),
            case(
                "packet artifact version mismatch",
                lambda r: _set_path(r, ["selected_packet_artifact_basis", "result_version"], "9.9.9"),
                "PACKET_ARTIFACT_VERSION_NOT_0_1_0",
            ),
            case(
                "packet artifact did not record local packet artifact",
                lambda r: _set_path(
                    r,
                    ["selected_packet_artifact_basis", "one_local_packet_artifact_recorded"],
                    False,
                ),
                "PACKET_ARTIFACT_DID_NOT_RECORD_LOCAL_PACKET_ARTIFACT",
            ),
            case(
                "packet artifact already emitted packet",
                lambda r: _set_path(r, ["selected_packet_artifact_basis", "packet_emitted"], True),
                "PACKET_ARTIFACT_ALREADY_EMITTED_PACKET",
            ),
            case(
                "packet artifact already transferred packet",
                lambda r: _set_path(r, ["selected_packet_artifact_basis", "packet_transferred"], True),
                "PACKET_ARTIFACT_ALREADY_TRANSFERRED_PACKET",
            ),
            case(
                "packet artifact copied packet to another device",
                lambda r: _set_path(
                    r,
                    ["selected_packet_artifact_basis", "packet_copied_to_another_device"],
                    True,
                ),
                "PACKET_ARTIFACT_COPIED_PACKET_TO_ANOTHER_DEVICE",
            ),
            case(
                "packet artifact authorized source transfer",
                lambda r: _set_path(
                    r,
                    ["selected_packet_artifact_basis", "source_transfer_authorized"],
                    True,
                ),
                "PACKET_ARTIFACT_AUTHORIZED_SOURCE_TRANSFER",
            ),
            case(
                "packet artifact authorized source receipt",
                lambda r: _set_path(
                    r,
                    ["selected_packet_artifact_basis", "source_receipt_authorized"],
                    True,
                ),
                "PACKET_ARTIFACT_AUTHORIZED_SOURCE_RECEIPT",
            ),
            case(
                "packet artifact authorized reception",
                lambda r: _set_path(
                    r,
                    ["selected_packet_artifact_basis", "reception_authorization_created"],
                    True,
                ),
                "PACKET_ARTIFACT_AUTHORIZED_RECEPTION",
            ),
            case(
                "packet artifact authorized second-carrier execution",
                lambda r: _set_path(
                    r,
                    ["selected_packet_artifact_basis", "second_carrier_execution_authorized"],
                    True,
                ),
                "PACKET_ARTIFACT_AUTHORIZED_SECOND_CARRIER_EXECUTION",
            ),
            case(
                "packet artifact created external result",
                lambda r: _set_path(
                    r,
                    ["selected_packet_artifact_basis", "external_result_created"],
                    True,
                ),
                "PACKET_ARTIFACT_CREATED_EXTERNAL_RESULT",
            ),
            case(
                "packet artifact created cross-carrier evidence",
                lambda r: _set_path(
                    r,
                    ["selected_packet_artifact_basis", "cross_carrier_evidence_created"],
                    True,
                ),
                "PACKET_ARTIFACT_CREATED_CROSS_CARRIER_EVIDENCE",
            ),
            case(
                "packet artifact used hidden repo state as emission authority",
                lambda r: _set_path(
                    r,
                    ["selected_packet_artifact_basis", "hidden_repo_state_used_as_emission_authority"],
                    True,
                ),
                "PACKET_ARTIFACT_USED_HIDDEN_REPO_STATE_AS_EMISSION_AUTHORITY",
            ),
            case(
                "packet artifact treated repo-local availability as emission authority",
                lambda r: _set_path(
                    r,
                    [
                        "selected_packet_artifact_basis",
                        "repo_local_availability_treated_as_emission_authority",
                    ],
                    True,
                ),
                "PACKET_ARTIFACT_TREATED_REPO_LOCAL_AVAILABILITY_AS_EMISSION_AUTHORITY",
            ),
            case(
                "packet artifact returned raw full prior artifact body",
                lambda r: _set_path(
                    r,
                    ["selected_packet_artifact_basis", "raw_full_prior_artifact_body_returned"],
                    True,
                ),
                "PACKET_ARTIFACT_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
            ),
            case(
                "packet artifact treated artifact existence as emission authority",
                lambda r: _set_path(
                    r,
                    [
                        "selected_packet_artifact_basis",
                        "artifact_existence_treated_as_emission_authority",
                    ],
                    True,
                ),
                "PACKET_ARTIFACT_TREATED_ARTIFACT_EXISTENCE_AS_EMISSION_AUTHORITY",
            ),
            case(
                "packet artifact treated artifact path as currentness",
                lambda r: _set_path(
                    r,
                    ["selected_packet_artifact_basis", "artifact_path_treated_as_currentness"],
                    True,
                ),
                "PACKET_ARTIFACT_TREATED_ARTIFACT_PATH_AS_CURRENTNESS",
            ),
            case("boundary treated as emission", flip_non_claim("packet_emission_boundary_treated_as_emission")),
            case("boundary treated as transfer", flip_non_claim("packet_emission_boundary_treated_as_transfer")),
            case(
                "boundary treated as copy authorization",
                flip_non_claim("packet_emission_boundary_treated_as_copy_authorization"),
            ),
            case(
                "boundary treated as source transfer",
                flip_non_claim("packet_emission_boundary_treated_as_source_transfer"),
            ),
            case(
                "boundary treated as source receipt",
                flip_non_claim("packet_emission_boundary_treated_as_source_receipt"),
            ),
            case(
                "boundary treated as reception",
                flip_non_claim("packet_emission_boundary_treated_as_reception_authorization"),
            ),
            case(
                "boundary treated as second-carrier receipt",
                flip_non_claim("packet_emission_boundary_treated_as_second_carrier_receipt"),
            ),
            case(
                "boundary treated as second-carrier execution",
                flip_non_claim("packet_emission_boundary_treated_as_second_carrier_execution"),
            ),
            case(
                "boundary treated as cross-carrier evidence",
                flip_non_claim("packet_emission_boundary_treated_as_cross_carrier_evidence"),
            ),
            case("boundary treated as source", flip_non_claim("packet_emission_boundary_treated_as_source")),
            case("boundary treated as authority", flip_non_claim("packet_emission_boundary_treated_as_authority")),
            case(
                "boundary treated as currentness",
                flip_non_claim("packet_emission_boundary_treated_as_currentness"),
            ),
            case(
                "boundary treated as final completion",
                flip_non_claim("packet_emission_boundary_treated_as_final_completion"),
            ),
            case("boundary treated as runtime", flip_non_claim("packet_emission_boundary_treated_as_runtime")),
            case(
                "boundary treated as continuation",
                flip_non_claim("packet_emission_boundary_treated_as_continuation"),
            ),
            case(
                "boundary treated as reusable permission",
                flip_non_claim("packet_emission_boundary_treated_as_reusable_permission"),
            ),
            case(
                "boundary treated as follow-on work",
                flip_non_claim("packet_emission_boundary_treated_as_follow_on_work"),
            ),
            case("packet emitted", flip_non_claim("packet_emitted")),
            case("emitted packet created", flip_non_claim("emitted_packet_created")),
            case("packet transferred", flip_non_claim("packet_transferred")),
            case("packet copied to another device", flip_non_claim("packet_copied_to_another_device")),
            case("source transfer occurred", flip_non_claim("source_transfer_occurred")),
            case("source receipt occurred", flip_non_claim("source_receipt_occurred")),
            case("reception authorization created", flip_non_claim("reception_authorization_created")),
            case("second-carrier receipt created", flip_non_claim("second_carrier_receipt_created")),
            case("second-carrier execution created", flip_non_claim("second_carrier_execution_created")),
            case("external result created", flip_non_claim("external_result_created")),
            case("cross-carrier evidence created", flip_non_claim("cross_carrier_evidence_created")),
            case("source created", flip_non_claim("source_created")),
            case("authority created", flip_non_claim("authority_created")),
            case("currentness created", flip_non_claim("currentness_created")),
            case("final completion claimed", flip_non_claim("final_completion_claimed")),
            case("runtime hosting created", flip_non_claim("runtime_hosting_created")),
            case("deployment created", flip_non_claim("deployment_created")),
            case("public release created", flip_non_claim("public_release_created")),
            case("operation permission created", flip_non_claim("operation_permission_created")),
            case("continuation authorized", flip_non_claim("continuation_authorized")),
            case("reusable permission created", flip_non_claim("reusable_permission_created")),
            case("follow-on authorized", flip_non_claim("follow_on_work_authorized")),
            case(
                "artifact existence treated as emission authority",
                flip_non_claim("artifact_existence_treated_as_emission_authority"),
            ),
            case("artifact path treated as currentness", flip_non_claim("artifact_path_treated_as_currentness")),
            case(
                "repo-local availability treated as emission authority",
                flip_non_claim("repo_local_availability_treated_as_emission_authority"),
            ),
            case("hidden repo state used as emission content", flip_non_claim("hidden_repo_state_used_as_emission_content")),
            case(
                "hidden repo state used as emission authority",
                flip_non_claim("hidden_repo_state_used_as_emission_authority"),
            ),
            case(
                "selected basis not reference shaped",
                lambda r: _set_path(r, ["reference_shaped_input_posture"], False),
                "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
            ),
            case("raw full prior artifact body returned", flip_non_claim("raw_full_prior_artifact_body_returned")),
            case(
                "predecessor failure hidden",
                lambda r: _set_path(
                    r,
                    ["selected_predecessor_failure_basis", "predecessor_failures_hidden"],
                    True,
                ),
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
            case(
                "predecessor failure repaired",
                lambda r: _set_path(
                    r,
                    ["selected_predecessor_failure_basis", "predecessor_failures_repaired"],
                    True,
                ),
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
            case(
                "predecessor failure claimed passed",
                lambda r: _set_path(
                    r,
                    ["selected_predecessor_failure_basis", "predecessor_failures_claimed_passed"],
                    True,
                ),
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
            case(
                "lineage treated as current report artifact",
                lambda r: _set_path(
                    r,
                    [
                        "selected_command_report_lineage_basis",
                        "command_report_lineage_treated_as_current_report_artifact",
                    ],
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
            ),
            case(
                "lineage treated as source",
                lambda r: _set_path(
                    r,
                    ["selected_command_report_lineage_basis", "command_report_lineage_treated_as_source"],
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
            ),
            case(
                "lineage treated as authority",
                lambda r: _set_path(
                    r,
                    ["selected_command_report_lineage_basis", "command_report_lineage_treated_as_authority"],
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
            ),
            case(
                "lineage treated as currentness",
                lambda r: _set_path(
                    r,
                    ["selected_command_report_lineage_basis", "command_report_lineage_treated_as_currentness"],
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
            ),
            case("consumed request reopened", flip_non_claim("consumed_request_reopened")),
            case("authorization token reused", flip_non_claim("authorization_token_reused")),
            case("full prior artifact body emitted", emit_full_prior_artifact_body),
            case("artifacts mutated", flip_non_claim("prior_artifacts_mutated")),
            case(
                "required non-claim missing",
                lambda r: _delete_path(r, ["declared_non_claims", "packet_emitted"]),
            ),
        ]

        for label, mutate, expected_code in cases:
            with self.subTest(label=label):
                request = _valid_request()
                mutate(request)
                result = resolver.resolve_portable_source_body_verification_packet_emission_boundary_v2(
                    declared_packet_emission_boundary_request=request
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIsNotNone(result["block"]["block_code"])
                if expected_code is not None:
                    self.assertEqual(result["block"]["block_code"], expected_code)
                self.assert_public_block_codes(result)
                self.assert_no_overreach_created(result)
                self.assert_generated_booleans_are_preserved(result)

        for label, request in [
            ("missing request", None),
            ("non-mapping request", ["not", "a", "mapping"]),
        ]:
            with self.subTest(label=label):
                result = resolver.resolve_portable_source_body_verification_packet_emission_boundary_v2(
                    declared_packet_emission_boundary_request=request
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
                self.assert_public_block_codes(result)
                self.assert_no_overreach_created(result)
                self.assert_generated_booleans_are_preserved(result)

    def test_path_and_write_behavior(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_packet_emission_boundary_v2_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result["portable_source_body_verification_packet_emission_boundary_metadata"]
            self.assertEqual(
                metadata["portable_source_body_verification_packet_emission_boundary_result_version"],
                "0.2.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_packet_emission_boundary_v2",
            )

            alias_result = resolver.resolve_portable_source_body_verification_packet_emission_boundary_from_path(
                request_path
            )
            alias_metadata = alias_result[
                "portable_source_body_verification_packet_emission_boundary_metadata"
            ]
            self.assertEqual(alias_metadata["resolver_module"], metadata["resolver_module"])
            self.assertEqual(
                alias_metadata["portable_source_body_verification_packet_emission_boundary_result_version"],
                "0.2.0",
            )

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketEmissionBoundaryV2Error):
                resolver.resolve_portable_source_body_verification_packet_emission_boundary_v2_from_path(
                    malformed_path
                )

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            try:
                array_result = (
                    resolver.resolve_portable_source_body_verification_packet_emission_boundary_v2_from_path(
                        array_path
                    )
                )
            except resolver.PortableSourceBodyVerificationPacketEmissionBoundaryV2Error:
                array_result = None
            if array_result is not None:
                self.assertEqual(array_result["outcome"], BLOCKED)
                self.assertEqual(
                    array_result["block"]["block_code"],
                    "DECLARED_PACKET_EMISSION_BOUNDARY_REQUEST_MALFORMED",
                )

            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketEmissionBoundaryV2Error):
                resolver.resolve_portable_source_body_verification_packet_emission_boundary_v2_from_path(
                    temp_root / "missing.json"
                )

            output_root = (
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission_boundary_v2"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_packet_emission_boundary_v2_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_packet_emission_boundary_v2_result(
                    result
                )

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(first_path.parent, output_root)
            self.assertEqual(
                first_path.parent.name,
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission_boundary_v2",
            )
            self.assertNotEqual(
                first_path.parent.name,
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission_boundary",
            )
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            forbidden = [
                "packet_artifact",
                "emitted_packet",
                "packet_transfer",
                "second_carrier",
                "cross_carrier",
                "runtime",
                "deployment",
                "public_release",
            ]
            self.assertFalse(any(part in first_path.parent.name for part in forbidden))

    def test_non_mutation(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        result = resolver.resolve_portable_source_body_verification_packet_emission_boundary_v2(
            declared_packet_emission_boundary_request=request
        )
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, original)
        for key in [
            "selected_packet_artifact_basis",
            "selected_packet_artifact_terminal_summary_basis",
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
            "packet_emission_boundary_scope",
            "declared_non_claims",
        ]:
            self.assertEqual(request[key], original[key])
        for posture_key in resolver.POSTURE_KEYS:
            self.assertEqual(request[posture_key], original[posture_key])

    def test_raw_full_body_and_hidden_repo_state_containment(self) -> None:
        request = _valid_request()
        hostile = {
            "raw_body": HOSTILE_RAW_VALUE,
            "raw_full_body": HOSTILE_RAW_VALUE,
            "full_body": HOSTILE_RAW_VALUE,
            "artifact_body": HOSTILE_RAW_VALUE,
            "raw_result_body": HOSTILE_RAW_VALUE,
            "raw_output_body": HOSTILE_RAW_VALUE,
            "emitted_packet_body": HOSTILE_RAW_VALUE,
            "packet_body": HOSTILE_RAW_VALUE,
            "source_body": HOSTILE_RAW_VALUE,
            "authority_body": HOSTILE_RAW_VALUE,
            "hidden_repo_state": HOSTILE_RAW_VALUE,
            "current_working_tree": HOSTILE_RAW_VALUE,
            "local_cache": HOSTILE_RAW_VALUE,
            "repo_local_only_dependency": HOSTILE_RAW_VALUE,
            "unlisted_file_dependency": HOSTILE_RAW_VALUE,
            "nested": [{"payload": RAW_SENTINEL}],
            "lawful_generated_hidden_repo_state_boolean": False,
        }
        for section in [
            "selected_packet_artifact_basis",
            "selected_packet_boundary_basis",
            "selected_command_success_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        ]:
            request[section].update(copy.deepcopy(hostile))

        original = copy.deepcopy(request)
        result = resolver.resolve_portable_source_body_verification_packet_emission_boundary_v2(
            declared_packet_emission_boundary_request=request
        )

        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_no_raw_payload(result)
        self.assert_public_block_codes(result)
        self.assert_no_overreach_created(result)
        self.assert_generated_booleans_are_preserved(result)
        self.assertEqual(request, original)
        self.assert_bool_field(result["non_claims"], "hidden_repo_state_used_as_emission_content", False)
        self.assert_bool_field(result["non_claims"], "hidden_repo_state_used_as_emission_authority", False)
        self.assert_bool_field(
            result["non_claims"],
            "repo_local_availability_treated_as_emission_authority",
            False,
        )


if __name__ == "__main__":
    unittest.main()
