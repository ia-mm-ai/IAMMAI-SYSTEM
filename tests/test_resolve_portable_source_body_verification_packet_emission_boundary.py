"""Tests for portable source-body verification packet emission boundary only.

This suite is downstream of the recorded local packet artifact. It verifies
that the packet emission boundary resolver records one future packet-emission
step boundary only: packet has not been emitted, emitted packet has not been
created, packet has not been transferred or copied, source transfer and source
receipt have not occurred, reception authorization does not exist,
second-carrier receipt/execution has not occurred, external result and
cross-carrier evidence have not been created, and source/authority/currentness/
runtime/final-completion/follow-on remain unauthorized.
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

import resolve_portable_source_body_verification_packet_emission_boundary as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_PACKET_EMISSION_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)

RAW_SENTINEL = "RAW_PACKET_EMISSION_BOUNDARY_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_PACKET_EMISSION_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN"

TOP_LEVEL_SECTIONS = (
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
)

TRUE_RECORDED_FIELDS = (
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
    "repo_local_availability_not_emission_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

REPRESENTATIVE_BLOCK_CODES = (
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
)


def _basis(label: str, outcome: str | None = None) -> dict[str, Any]:
    value: dict[str, Any] = {
        "basis_label": label,
        "declared": True,
        "basis_only": True,
        "reference_shaped": True,
        "selected_basis_reference_shape_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
        "hidden_repo_state_excluded": True,
        "hidden_repo_state_used_as_emission_content": False,
        "hidden_repo_state_used_as_emission_authority": False,
        "repo_local_availability_treated_as_emission_authority": False,
        "artifact_existence_treated_as_emission_authority": False,
        "artifact_path_treated_as_currentness": False,
    }
    if outcome is not None:
        value["outcome"] = outcome
    return value


def _request() -> dict[str, Any]:
    request = resolver.build_declared_portable_source_body_verification_packet_emission_boundary_request()
    request["packet_emission_boundary_question"] = resolver.CORE_QUESTION
    request["packet_emission_boundary_intent"] = resolver.INTENT_RECORD
    request["packet_emission_boundary_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    request["reference_shaped_input_posture"] = True
    for shortcut in (
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
    ):
        request.pop(shortcut, None)

    request["selected_packet_artifact_basis"] = _basis(
        "selected_packet_artifact_basis",
        "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED",
    )
    request["selected_packet_artifact_basis"].update(
        {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "packet_artifact_recorded": True,
            "one_local_packet_artifact_recorded": True,
            "local_packet_artifact_recorded": True,
            "packet_artifact_not_emission": True,
            "packet_not_emitted": True,
            "packet_emitted": False,
            "emitted_packet_created": False,
            "packet_not_transferred": True,
            "packet_transferred": False,
            "packet_copied_to_another_device": False,
            "source_transfer_authorized": False,
            "source_receipt_authorized": False,
            "reception_authorization_created": False,
            "second_carrier_execution_authorized": False,
            "second_carrier_execution_created": False,
            "external_result_created": False,
            "cross_carrier_evidence_created": False,
            "repo_local_availability_not_emission_authority": True,
            "raw_full_prior_artifact_body_not_returned": True,
        }
    )
    request["selected_packet_artifact_terminal_summary_basis"] = _basis(
        "selected_packet_artifact_terminal_summary_basis"
    )
    request["selected_packet_boundary_basis"] = _basis(
        "selected_packet_boundary_basis",
        "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED",
    )
    request["selected_command_success_basis"] = _basis(
        "selected_command_success_basis",
        "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED",
    )
    request["selected_command_result_v2_basis"] = _basis(
        "selected_command_result_v2_basis",
        "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED",
    )
    request["selected_output_capture_v2_basis"] = _basis(
        "selected_output_capture_v2_basis",
        "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED",
    )
    request["selected_command_output_report_artifact_basis"] = _basis(
        "selected_command_output_report_artifact_basis",
        "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED",
    )
    request["selected_command_execution_basis"] = _basis("selected_command_execution_basis")
    request["selected_command_execution_basis"].update(
        {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED",
            "execution_trace_audit_only": True,
            "audit_only": True,
        }
    )
    request["selected_command_report_lineage_basis"] = _basis(
        "selected_command_report_lineage_basis"
    )
    request["selected_command_report_lineage_basis"].update(
        {
            "command_report_lineage_only": True,
            "lineage_only": True,
            "command_report_lineage_treated_as_current_report_artifact": False,
            "command_report_lineage_treated_as_source": False,
            "command_report_lineage_treated_as_authority": False,
            "command_report_lineage_treated_as_currentness": False,
        }
    )
    request["selected_predecessor_failure_basis"] = _basis(
        "selected_predecessor_failure_basis"
    )
    request["selected_predecessor_failure_basis"].update(
        {
            "predecessor_failure_evidence_visible": True,
            "predecessor_failures_visible": True,
            "predecessor_failure_evidence_hidden_or_repaired": False,
            "predecessor_failures_repaired": False,
            "predecessor_failures_hidden": False,
            "predecessor_failures_claimed_passed": False,
        }
    )
    request["selected_evidence_manifest_basis"] = _basis("selected_evidence_manifest_basis")
    request["selected_artifact_containment_basis"] = _basis(
        "selected_artifact_containment_basis"
    )
    request["selected_portable_verification_basis"] = _basis(
        "selected_portable_verification_basis"
    )

    for key in resolver.POSTURE_KEYS:
        request.setdefault(key, {"declared": True})
        request[key].update({"declared": True, "packet_emission_boundary_posture_only": True})
    return request


def _resolve(request: Mapping[str, Any] | None = None) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_packet_emission_boundary(
        declared_packet_emission_boundary_request=request
    )


def _set_nested(mapping: dict[str, Any], section: str, key: str, value: Any) -> None:
    mapping[section][key] = value


def _delete(mapping: dict[str, Any], key: str) -> None:
    del mapping[key]


class PortableSourceBodyVerificationPacketEmissionBoundaryTests(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block", {})
        if isinstance(block, Mapping):
            block_code = block.get("block_code")
            if block_code is not None:
                self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in result.get("packet_emission_boundary_checks", []):
            self.assertIsInstance(check, Mapping)
            for code_key in ("block_code", "failure_code"):
                code = check.get(code_key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_no_overreach_created(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in (
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
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "another_reception_request_authorized",
            "follow_on_work_authorized",
            "hidden_repo_state_used_as_emission_content",
            "hidden_repo_state_used_as_emission_authority",
            "repo_local_availability_treated_as_emission_authority",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(non_claims[key], False, key)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_packet_emission_boundary",
            "resolve_portable_source_body_verification_packet_emission_boundary_from_path",
            "write_portable_source_body_verification_packet_emission_boundary_result",
            "build_portable_source_body_verification_packet_emission_boundary_summary",
            "build_declared_portable_source_body_verification_packet_emission_boundary_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_PACKET_EMISSION_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission_boundary"
            )
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_packet_emission_boundary_recorded_result(self) -> None:
        request = _request()
        result = _resolve(request)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        metadata = result["portable_source_body_verification_packet_emission_boundary_metadata"]
        self.assertEqual(metadata["failed_check_count"], 0)
        self.assertFalse(result["block"]["blocked"])
        self.assertIsNone(result["block"]["block_code"])
        self.assert_public_block_codes(result)

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        self.assertEqual(
            metadata["portable_source_body_verification_packet_emission_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_packet_emission_boundary",
        )
        self.assertEqual(
            metadata["packet_emission_boundary_request_id"],
            request["packet_emission_boundary_request_id"],
        )

        statement = result["packet_emission_boundary_statement"]
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(statement[key], True, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(result["non_claims"][key], False, key)

        non_meaning = result["packet_emission_boundary_non_meaning"]
        for key in (
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
        ):
            self.assertIs(non_meaning[key], False, key)

    def test_summary_helper(self) -> None:
        request = _request()
        result = _resolve(request)
        summary = resolver.build_portable_source_body_verification_packet_emission_boundary_summary(
            result
        )
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["request_id"], request["packet_emission_boundary_request_id"])
        self.assertEqual(summary["question"], resolver.CORE_QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(summary[key], True, key)
        self.assertEqual(
            summary["selected_packet_artifact_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED",
        )
        self.assertEqual(summary["selected_packet_artifact_version"], "0.1.0")
        self.assertEqual(summary["selected_packet_artifact_failed_check_count"], 0)
        self.assertIs(summary["no_emission_transfer_copy_receipt_cross_carrier_evidence"], True)
        self.assertIs(summary["no_source_authority_currentness_final_completion_runtime"], True)
        self.assertIs(summary["no_deployment_public_release_follow_on"], True)
        for key, value in summary["key_non_claims"].items():
            self.assertIs(value, False, key)

    def test_representative_blocking_behavior(self) -> None:
        def flip_non_claim(name: str) -> Callable[[dict[str, Any]], None]:
            return lambda request: request["declared_non_claims"].__setitem__(name, True)

        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", lambda r: r.__setitem__("packet_emission_boundary_intent", resolver.INTENT_BLOCK)),
            ("unsupported intent", lambda r: r.__setitem__("packet_emission_boundary_intent", "UNSUPPORTED")),
            ("unsupported scope", lambda r: r["packet_emission_boundary_scope"].append("UNSUPPORTED_PACKET_EMISSION_BOUNDARY_SCOPE_VALUE")),
            ("missing packet artifact basis", lambda r: _delete(r, "selected_packet_artifact_basis")),
            ("packet artifact not recorded", lambda r: _set_nested(r, "selected_packet_artifact_basis", "outcome", "BAD")),
            ("packet artifact failed checks", lambda r: _set_nested(r, "selected_packet_artifact_basis", "failed_check_count", 1)),
            ("packet artifact bad version", lambda r: _set_nested(r, "selected_packet_artifact_basis", "result_version", "9.9.9")),
            ("packet artifact did not record local artifact", lambda r: _set_nested(r, "selected_packet_artifact_basis", "one_local_packet_artifact_recorded", False)),
            ("packet artifact emitted", lambda r: _set_nested(r, "selected_packet_artifact_basis", "packet_emitted", True)),
            ("packet artifact transferred", lambda r: _set_nested(r, "selected_packet_artifact_basis", "packet_transferred", True)),
            ("packet artifact copied", lambda r: _set_nested(r, "selected_packet_artifact_basis", "packet_copied_to_another_device", True)),
            ("packet artifact source transfer", lambda r: _set_nested(r, "selected_packet_artifact_basis", "source_transfer_authorized", True)),
            ("packet artifact source receipt", lambda r: _set_nested(r, "selected_packet_artifact_basis", "source_receipt_authorized", True)),
            ("packet artifact reception", lambda r: _set_nested(r, "selected_packet_artifact_basis", "reception_authorization_created", True)),
            ("packet artifact second carrier", lambda r: _set_nested(r, "selected_packet_artifact_basis", "second_carrier_execution_authorized", True)),
            ("packet artifact external result", lambda r: _set_nested(r, "selected_packet_artifact_basis", "external_result_created", True)),
            ("packet artifact cross carrier", lambda r: _set_nested(r, "selected_packet_artifact_basis", "cross_carrier_evidence_created", True)),
            ("packet artifact hidden authority", lambda r: _set_nested(r, "selected_packet_artifact_basis", "hidden_repo_state_used_as_emission_authority", True)),
            ("packet artifact repo-local authority", lambda r: _set_nested(r, "selected_packet_artifact_basis", "repo_local_availability_treated_as_emission_authority", True)),
            ("packet artifact raw body returned", lambda r: _set_nested(r, "selected_packet_artifact_basis", "raw_full_prior_artifact_body_returned", True)),
            ("packet artifact existence authority", lambda r: _set_nested(r, "selected_packet_artifact_basis", "artifact_existence_treated_as_emission_authority", True)),
            ("packet artifact path currentness", lambda r: _set_nested(r, "selected_packet_artifact_basis", "artifact_path_treated_as_currentness", True)),
            ("boundary treated as emission", flip_non_claim("packet_emission_boundary_treated_as_emission")),
            ("boundary treated as transfer", flip_non_claim("packet_emission_boundary_treated_as_transfer")),
            ("boundary treated as copy", flip_non_claim("packet_emission_boundary_treated_as_copy_authorization")),
            ("boundary treated as source transfer", flip_non_claim("packet_emission_boundary_treated_as_source_transfer")),
            ("boundary treated as source receipt", flip_non_claim("packet_emission_boundary_treated_as_source_receipt")),
            ("boundary treated as reception", flip_non_claim("packet_emission_boundary_treated_as_reception_authorization")),
            ("boundary treated as second carrier receipt", flip_non_claim("packet_emission_boundary_treated_as_second_carrier_receipt")),
            ("boundary treated as second carrier execution", flip_non_claim("packet_emission_boundary_treated_as_second_carrier_execution")),
            ("boundary treated as cross carrier", flip_non_claim("packet_emission_boundary_treated_as_cross_carrier_evidence")),
            ("boundary treated as source", flip_non_claim("packet_emission_boundary_treated_as_source")),
            ("boundary treated as authority", flip_non_claim("packet_emission_boundary_treated_as_authority")),
            ("boundary treated as currentness", flip_non_claim("packet_emission_boundary_treated_as_currentness")),
            ("boundary treated as final completion", flip_non_claim("packet_emission_boundary_treated_as_final_completion")),
            ("boundary treated as runtime", flip_non_claim("packet_emission_boundary_treated_as_runtime")),
            ("boundary treated as continuation", flip_non_claim("packet_emission_boundary_treated_as_continuation")),
            ("boundary treated as reusable", flip_non_claim("packet_emission_boundary_treated_as_reusable_permission")),
            ("boundary treated as follow on", flip_non_claim("packet_emission_boundary_treated_as_follow_on_work")),
            ("packet emitted", flip_non_claim("packet_emitted")),
            ("emitted packet created", flip_non_claim("emitted_packet_created")),
            ("packet transferred", flip_non_claim("packet_transferred")),
            ("packet copied", flip_non_claim("packet_copied_to_another_device")),
            ("source transfer", flip_non_claim("source_transfer_occurred")),
            ("source receipt", flip_non_claim("source_receipt_occurred")),
            ("reception authorization", flip_non_claim("reception_authorization_created")),
            ("second carrier receipt", flip_non_claim("second_carrier_receipt_created")),
            ("second carrier execution", flip_non_claim("second_carrier_execution_created")),
            ("external result", flip_non_claim("external_result_created")),
            ("cross carrier evidence", flip_non_claim("cross_carrier_evidence_created")),
            ("source created", flip_non_claim("source_created")),
            ("authority created", flip_non_claim("authority_created")),
            ("currentness created", flip_non_claim("currentness_created")),
            ("final completion claimed", flip_non_claim("final_completion_claimed")),
            ("runtime created", flip_non_claim("runtime_hosting_created")),
            ("deployment created", flip_non_claim("deployment_created")),
            ("public release created", flip_non_claim("public_release_created")),
            ("operation permission", flip_non_claim("operation_permission_created")),
            ("continuation", flip_non_claim("continuation_authorized")),
            ("reusable", flip_non_claim("reusable_permission_created")),
            ("follow on", flip_non_claim("follow_on_work_authorized")),
            ("artifact existence authority", flip_non_claim("artifact_existence_treated_as_emission_authority")),
            ("artifact path currentness", flip_non_claim("artifact_path_treated_as_currentness")),
            ("repo local authority", flip_non_claim("repo_local_availability_treated_as_emission_authority")),
            ("hidden content", flip_non_claim("hidden_repo_state_used_as_emission_content")),
            ("hidden authority", flip_non_claim("hidden_repo_state_used_as_emission_authority")),
            ("selected basis not reference", lambda r: _set_nested(r, "selected_command_success_basis", "reference_shaped", False)),
            ("raw full body returned", lambda r: _set_nested(r, "selected_command_success_basis", "raw_full_prior_artifact_body_returned", True)),
            ("predecessor repaired", lambda r: _set_nested(r, "selected_predecessor_failure_basis", "predecessor_failures_repaired", True)),
            ("predecessor hidden", lambda r: _set_nested(r, "selected_predecessor_failure_basis", "predecessor_failures_hidden", True)),
            ("predecessor claimed passed", lambda r: _set_nested(r, "selected_predecessor_failure_basis", "predecessor_failures_claimed_passed", True)),
            ("lineage current artifact", lambda r: _set_nested(r, "selected_command_report_lineage_basis", "command_report_lineage_treated_as_current_report_artifact", True)),
            ("lineage source", lambda r: _set_nested(r, "selected_command_report_lineage_basis", "command_report_lineage_treated_as_source", True)),
            ("lineage authority", lambda r: _set_nested(r, "selected_command_report_lineage_basis", "command_report_lineage_treated_as_authority", True)),
            ("lineage currentness", lambda r: _set_nested(r, "selected_command_report_lineage_basis", "command_report_lineage_treated_as_currentness", True)),
            ("consumed reopened", flip_non_claim("consumed_request_reopened")),
            ("authorization reused", flip_non_claim("authorization_token_reused")),
            ("full prior body emitted", lambda r: r.__setitem__("full_prior_artifact_body_emitted", True)),
            ("artifacts mutated", flip_non_claim("prior_artifacts_mutated")),
            ("required non-claim missing", lambda r: r["declared_non_claims"].pop("packet_emitted")),
        )

        special_cases = (
            ("missing request", lambda: _resolve(None)),
            ("non-mapping request", lambda: _resolve(["not", "mapping"])),  # type: ignore[arg-type]
        )
        for label, get_result in special_cases:
            with self.subTest(label=label):
                result = get_result()
                self.assertEqual(result["outcome"], BLOCKED)
                self.assert_public_block_codes(result)
                self.assert_no_overreach_created(result)

        for label, mutate in cases:
            with self.subTest(label=label):
                request = _request()
                mutate(request)
                result = _resolve(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertTrue(result["block"]["blocked"])
                self.assertIsNotNone(result["block"]["block_code"])
                self.assert_public_block_codes(result)
                self.assert_no_overreach_created(result)

    def test_path_and_write_behavior(self) -> None:
        request = _request()
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            request_path = temp_dir / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            result = resolver.resolve_portable_source_body_verification_packet_emission_boundary_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result["portable_source_body_verification_packet_emission_boundary_metadata"]
            self.assertEqual(
                metadata["portable_source_body_verification_packet_emission_boundary_result_version"],
                "0.1.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_packet_emission_boundary",
            )

            malformed_path = temp_dir / "malformed.json"
            malformed_path.write_text("{ malformed", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketEmissionBoundaryError):
                resolver.resolve_portable_source_body_verification_packet_emission_boundary_from_path(
                    malformed_path
                )

            array_path = temp_dir / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketEmissionBoundaryError):
                resolver.resolve_portable_source_body_verification_packet_emission_boundary_from_path(
                    array_path
                )

            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketEmissionBoundaryError):
                resolver.resolve_portable_source_body_verification_packet_emission_boundary_from_path(
                    temp_dir / "missing.json"
                )

            output_root = (
                temp_dir
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                written = resolver.write_portable_source_body_verification_packet_emission_boundary_result(
                    result
                )
                written_again = resolver.write_portable_source_body_verification_packet_emission_boundary_result(
                    result
                )

            self.assertEqual(written.parent, output_root)
            self.assertTrue(written.exists())
            self.assertTrue(written_again.exists())
            self.assertNotEqual(written, written_again)
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            self.assertTrue(
                str(written.parent).endswith(
                    "artifacts/"
                    "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission_boundary"
                )
            )
            for forbidden in (
                "portable_source_body_verification_packet_artifact",
                "emitted_packet",
                "packet_transfer",
                "second_carrier",
                "cross_carrier",
                "runtime",
                "deployment",
                "public_release",
            ):
                self.assertNotIn(forbidden, written.parent.name)

    def test_non_mutation(self) -> None:
        request = _request()
        original = copy.deepcopy(request)
        result = _resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, original)

    def test_raw_full_body_and_hidden_repo_state_containment(self) -> None:
        request = _request()
        for section in (
            "selected_packet_artifact_basis",
            "selected_packet_boundary_basis",
            "selected_command_success_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        ):
            request[section]["raw_body"] = HOSTILE_RAW_VALUE
            request[section]["raw_full_body"] = HOSTILE_RAW_VALUE
            request[section]["full_body"] = HOSTILE_RAW_VALUE
            request[section]["artifact_body"] = HOSTILE_RAW_VALUE
            request[section]["raw_result_body"] = HOSTILE_RAW_VALUE
            request[section]["raw_output_body"] = HOSTILE_RAW_VALUE
            request[section]["emitted_packet_body"] = HOSTILE_RAW_VALUE
            request[section]["packet_body"] = HOSTILE_RAW_VALUE
            request[section]["source_body"] = HOSTILE_RAW_VALUE
            request[section]["authority_body"] = HOSTILE_RAW_VALUE
            request[section]["hidden_repo_state"] = {"value": HOSTILE_RAW_VALUE}
            request[section]["current_working_tree"] = HOSTILE_RAW_VALUE
            request[section]["local_cache"] = HOSTILE_RAW_VALUE
            request[section]["repo_local_only_dependency"] = HOSTILE_RAW_VALUE
            request[section]["unlisted_file_dependency"] = HOSTILE_RAW_VALUE
            request[section]["nested"] = [{"raw_full_body": HOSTILE_RAW_VALUE}, RAW_SENTINEL]

        original = copy.deepcopy(request)
        result = _resolve(request)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        serialized = json.dumps(result, sort_keys=True)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)
        self.assert_public_block_codes(result)
        self.assert_no_overreach_created(result)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
