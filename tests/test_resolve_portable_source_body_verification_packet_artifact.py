"""Tests for portable source-body verification packet artifact posture only.

This suite is downstream of the recorded packet boundary. It verifies that the
packet artifact resolver records one local packet artifact only: packet artifact
is not packet emission, transfer, second-carrier execution, cross-carrier proof,
source, authority, currentness, runtime, final completion, or follow-on work.
Hidden repo state is excluded, repo-local availability is not packet authority,
selected basis remains reference-shaped, the consumed request token remains
closed, and authorization token reuse remains blocked.
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

import resolve_portable_source_body_verification_packet_artifact as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_PACKET_ARTIFACT_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
EXTRA_FALSE_NON_CLAIMS = tuple(getattr(resolver, "EXTRA_FALSE_NON_CLAIMS", ()))

RAW_SENTINEL = "RAW_PACKET_ARTIFACT_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_PACKET_ARTIFACT_FULL_BODY_VALUE_MUST_NOT_RETURN"

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_packet_artifact_metadata",
    "declared_packet_artifact_question",
    "selected_packet_boundary_basis",
    "selected_packet_boundary_terminal_summary_basis",
    "selected_command_success_basis",
    "selected_command_success_terminal_summary_basis",
    "selected_command_result_v2_basis",
    "selected_output_capture_v2_basis",
    "selected_command_output_report_artifact_basis",
    "selected_command_execution_basis",
    "selected_command_report_lineage_basis",
    "selected_predecessor_failure_basis",
    "selected_evidence_manifest_basis",
    "selected_artifact_containment_basis",
    "selected_portable_verification_basis",
    "packet_artifact_spec_only_posture",
    "one_local_packet_artifact_posture",
    "packet_boundary_basis_preserved_posture",
    "local_command_success_basis_preserved_posture",
    "copyable_packet_shape_declared_posture",
    "selected_packet_basis_declared_posture",
    "selected_basis_reference_shape_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_packet_authority_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "packet_not_emitted_posture",
    "packet_not_transferred_posture",
    "second_carrier_execution_not_authorized_posture",
    "second_carrier_receipt_not_created_posture",
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
    "packet_artifact_scope",
    "packet_artifact_checks",
    "packet_artifact_statement",
    "packet_artifact_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_packet_artifact_summary",
)

TRUE_RECORDED_FIELDS = (
    "packet_artifact_recorded",
    "one_local_packet_artifact_recorded",
    "packet_boundary_basis_preserved",
    "local_command_success_basis_preserved",
    "copyable_packet_shape_declared",
    "selected_packet_basis_declared",
    "selected_basis_reference_shape_preserved",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_packet_authority",
    "repo_local_availability_not_packet_authority",
    "raw_full_prior_artifact_body_not_returned",
    "packet_not_emitted",
    "packet_not_transferred",
    "second_carrier_execution_not_authorized",
    "second_carrier_receipt_not_created",
    "external_result_not_created",
    "cross_carrier_evidence_not_created",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "final_completion_not_created",
    "runtime_not_created",
    "follow_on_work_not_authorized",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

REPRESENTATIVE_BLOCK_CODES = (
    "PACKET_ARTIFACT_QUESTION_UNDECLARED",
    "PACKET_ARTIFACT_INTENT_UNSUPPORTED",
    "PACKET_BOUNDARY_BASIS_MISSING",
    "PACKET_BOUNDARY_NOT_RECORDED",
    "PACKET_BOUNDARY_FAILED_CHECKS_PRESENT",
    "PACKET_BOUNDARY_VERSION_NOT_0_1_0",
    "PACKET_BOUNDARY_DID_NOT_DECLARE_FUTURE_PACKET_STEP",
    "PACKET_BOUNDARY_ALREADY_CREATED_PACKET",
    "PACKET_BOUNDARY_ALREADY_EMITTED_PACKET",
    "PACKET_BOUNDARY_AUTHORIZED_TRANSFER",
    "PACKET_BOUNDARY_AUTHORIZED_SECOND_CARRIER_EXECUTION",
    "PACKET_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
    "PACKET_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_PACKET_AUTHORITY",
    "PACKET_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
    "COMMAND_SUCCESS_BASIS_MISSING",
    "COMMAND_SUCCESS_NOT_RECORDED",
    "COMMAND_SUCCESS_FAILED_CHECKS_PRESENT",
    "COMMAND_SUCCESS_TREATED_AS_PACKET_PERMISSION",
    "PACKET_ARTIFACT_TREATED_AS_PACKET_EMISSION",
    "PACKET_ARTIFACT_TREATED_AS_PACKET_TRANSFER",
    "PACKET_ARTIFACT_TREATED_AS_SOURCE",
    "PACKET_ARTIFACT_TREATED_AS_AUTHORITY",
    "PACKET_ARTIFACT_TREATED_AS_CURRENTNESS",
    "PACKET_ARTIFACT_TREATED_AS_FINAL_COMPLETION",
    "PACKET_ARTIFACT_TREATED_AS_RUNTIME",
    "PACKET_ARTIFACT_TREATED_AS_CROSS_CARRIER_PROOF",
    "PACKET_EMITTED",
    "PACKET_TRANSFERRED",
    "PACKET_COPIED_TO_ANOTHER_DEVICE",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SECOND_CARRIER_EXECUTION_CREATED",
    "SECOND_CARRIER_RECEIPT_CREATED",
    "EXTERNAL_RESULT_CREATED",
    "CROSS_CARRIER_EVIDENCE_CREATED",
    "MANIFEST_CREATED_WITHOUT_BOUNDED_ADMISSION",
    "CHECKSUM_CREATED_WITHOUT_BOUNDED_ADMISSION",
    "SIGNATURE_CREATED_WITHOUT_BOUNDED_ADMISSION",
    "REPRODUCIBLE_ENVIRONMENT_DECLARED_WITHOUT_BOUNDED_ADMISSION",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_PACKET_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_PACKET_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_PACKET_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_PACKET_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_PACKET_ARTIFACT_SCOPE",
)


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _false_non_claims() -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    non_claims.update({key: False for key in EXTRA_FALSE_NON_CLAIMS})
    return non_claims


def _request(**overrides: Any) -> dict[str, Any]:
    request = resolver.build_declared_portable_source_body_verification_packet_artifact_request(
        packet_artifact_request_id="packet_artifact_test_request_001"
    )
    request["packet_artifact_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = _false_non_claims()
    request["selected_packet_boundary_basis"].update(
        {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "one_future_packet_step_declared": True,
            "packet_created": False,
            "packet_emitted": False,
            "packet_boundary_authorized_transfer": False,
            "packet_boundary_authorized_second_carrier_execution": False,
            "cross_carrier_evidence_created": False,
            "hidden_repo_state_used_as_packet_authority": False,
            "raw_full_prior_artifact_body_returned": False,
        }
    )
    request["selected_packet_boundary_terminal_summary_basis"].update(
        {
            "terminal_summary_readability_basis_only": True,
            "packet_boundary_is_not_packet": True,
            "packet_boundary_is_not_packet_emission": True,
            "packet_boundary_is_not_source_authority_currentness": True,
        }
    )
    request["selected_command_success_basis"].update(
        {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "bounded_command_success_recorded": True,
            "command_success_treated_as_packet_permission": False,
            "command_success_treated_as_packet_emission": False,
            "source_not_created": True,
            "authority_not_created": True,
            "currentness_not_created": True,
            "final_completion_not_created": True,
            "runtime_not_created": True,
            "follow_on_work_not_authorized": True,
        }
    )
    request["selected_command_success_terminal_summary_basis"].update(
        {
            "terminal_summary_readability_basis_only": True,
            "local_command_success_not_packet_permission": True,
        }
    )
    request["selected_command_result_v2_basis"].update(
        {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED",
            "result_version": "0.2.0",
            "failed_check_count": 0,
        }
    )
    request["selected_output_capture_v2_basis"].update(
        {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED",
            "result_version": "0.2.0",
            "failed_check_count": 0,
        }
    )
    request["selected_command_output_report_artifact_basis"].update(
        {
            "outcome": (
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
            ),
            "failed_check_count": 0,
        }
    )
    request["selected_command_execution_basis"].update(
        {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED",
            "failed_check_count": 0,
            "execution_trace_audit_only": True,
            "execution_trace_audit_only_preserved": True,
        }
    )
    request["selected_command_report_lineage_basis"].update(
        {
            "lineage_only": True,
            "command_report_lineage_treated_as_current_report_artifact": False,
            "command_report_lineage_treated_as_source": False,
            "command_report_lineage_treated_as_authority": False,
            "command_report_lineage_treated_as_currentness": False,
        }
    )
    request["selected_predecessor_failure_basis"].update(
        {
            "predecessor_failures_visible": True,
            "predecessor_failures_repaired": False,
            "predecessor_failures_hidden": False,
            "predecessor_failures_claimed_passed": False,
        }
    )
    request["selected_evidence_manifest_basis"].update(evidence_manifest_basis_declared=True)
    request["selected_artifact_containment_basis"].update(
        artifact_containment_basis_declared=True,
        recursive_full_artifact_embedding_blocked=True,
    )
    request["selected_portable_verification_basis"].update(
        portable_verification_basis_declared=True,
        portable_verification_is_not_cross_carrier_proof=True,
    )
    for key, value in overrides.items():
        request[key] = value
    return request


def _resolve(request: Mapping[str, Any] | None = None) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_packet_artifact(
        declared_packet_artifact_request=request
    )


def _set_nested(mapping: dict[str, Any], section: str, key: str, value: Any) -> None:
    mapping[section][key] = value


def _delete(mapping: dict[str, Any], key: str) -> None:
    del mapping[key]


class PortableSourceBodyVerificationPacketArtifactTests(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block", {})
        if isinstance(block, Mapping):
            block_code = block.get("block_code")
            if block_code is not None:
                self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in result.get("packet_artifact_checks", []):
            self.assertIsInstance(check, Mapping)
            for code_key in ("block_code", "failure_code"):
                code = check.get(code_key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_no_overreach_created(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in (
            "packet_emitted",
            "packet_transferred",
            "packet_copied_to_another_device",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "second_carrier_execution_created",
            "second_carrier_receipt_created",
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
            "hidden_repo_state_used_as_packet_content",
            "hidden_repo_state_used_as_packet_authority",
            "repo_local_availability_treated_as_packet_authority",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(non_claims[key], False, key)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_packet_artifact",
            "resolve_portable_source_body_verification_packet_artifact_from_path",
            "write_portable_source_body_verification_packet_artifact_result",
            "build_portable_source_body_verification_packet_artifact_summary",
            "build_declared_portable_source_body_verification_packet_artifact_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_PACKET_ARTIFACT_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_artifact"
            )
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_packet_artifact_recorded_result(self) -> None:
        request = _request()
        result = _resolve(request)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(
            result["portable_source_body_verification_packet_artifact_metadata"][
                "failed_check_count"
            ],
            0,
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertIsNone(result["block"]["block_code"])
        self.assert_public_block_codes(result)

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        metadata = result["portable_source_body_verification_packet_artifact_metadata"]
        self.assertEqual(
            metadata["portable_source_body_verification_packet_artifact_result_version"],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(metadata["packet_artifact_request_id"], request["packet_artifact_request_id"])

        statement = result["packet_artifact_statement"]
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(statement[key], True, key)

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)
        for key in (
            "packet_emitted",
            "packet_transferred",
            "packet_copied_to_another_device",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "second_carrier_execution_created",
            "second_carrier_receipt_created",
            "external_result_created",
            "cross_carrier_evidence_created",
            "manifest_created_without_bounded_admission",
            "checksum_created_without_bounded_admission",
            "signature_created_without_bounded_admission",
            "reproducible_environment_declared_without_bounded_admission",
            "packet_artifact_treated_as_packet_emission",
            "packet_artifact_treated_as_packet_transfer",
            "packet_artifact_treated_as_source",
            "packet_artifact_treated_as_authority",
            "packet_artifact_treated_as_currentness",
            "packet_artifact_treated_as_final_completion",
            "packet_artifact_treated_as_runtime",
            "packet_artifact_treated_as_cross_carrier_proof",
            "artifact_existence_treated_as_packet_authority",
            "artifact_path_treated_as_currentness",
            "repo_local_availability_treated_as_packet_authority",
            "hidden_repo_state_used_as_packet_content",
            "hidden_repo_state_used_as_packet_authority",
        ):
            self.assertIs(non_claims[key], False, key)

        non_meaning = result["packet_artifact_non_meaning"]
        for key in (
            "packet_emitted",
            "packet_transferred",
            "packet_copied_to_another_device",
            "second_carrier_received_it",
            "second_carrier_executed_anything",
            "external_result_exists",
            "cross_carrier_evidence_exists",
            "source_exists",
            "authority_exists",
            "currentness_exists",
            "final_completion_exists",
            "runtime_exists",
            "follow_on_work_authorized",
            "artifact_existence_is_packet_authority",
            "artifact_path_is_currentness",
            "hidden_repo_state_is_packet_content_authority",
        ):
            self.assertIs(non_meaning[key], False, key)

    def test_summary_helper_preserves_packet_artifact_posture(self) -> None:
        request = _request()
        result = _resolve(request)
        summary = resolver.build_portable_source_body_verification_packet_artifact_summary(result)

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["request_id"], request["packet_artifact_request_id"])
        self.assertEqual(summary["question"], request["packet_artifact_question"])
        self.assertEqual(summary["intent"], request["packet_artifact_intent"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)

        for key in (
            "packet_artifact_recorded",
            "one_local_packet_artifact_recorded",
            "packet_boundary_basis_preserved",
            "local_command_success_basis_preserved",
            "copyable_packet_shape_declared",
            "selected_packet_basis_declared",
            "selected_basis_reference_shape_preserved",
            "hidden_repo_state_excluded",
            "hidden_repo_state_not_used_as_packet_authority",
            "repo_local_availability_not_packet_authority",
            "raw_full_prior_artifact_body_not_returned",
            "packet_not_emitted",
            "packet_not_transferred",
            "second_carrier_execution_not_authorized",
            "second_carrier_receipt_not_created",
            "external_result_not_created",
            "cross_carrier_evidence_not_created",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "final_completion_not_created",
            "runtime_not_created",
            "follow_on_work_not_authorized",
        ):
            self.assertIs(summary[key], True, key)

        self.assertEqual(
            summary["selected_packet_boundary_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED",
        )
        self.assertEqual(summary["selected_packet_boundary_version"], "0.1.0")
        self.assertEqual(summary["selected_packet_boundary_failed_check_count"], 0)
        self.assertIs(summary["no_packet_emission_transfer_receipt_cross_carrier_evidence"], True)
        self.assertIs(summary["no_source_authority_currentness_final_completion_runtime"], True)
        self.assertIs(summary["no_deployment_public_release_follow_on"], True)
        self.assertEqual(summary["key_non_claims"], result["non_claims"])

    def test_representative_blocking_behavior(self) -> None:
        def flip_non_claim(name: str) -> Callable[[dict[str, Any]], None]:
            return lambda request: request["declared_non_claims"].__setitem__(name, True)

        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", lambda r: r.__setitem__("packet_artifact_intent", resolver.INTENT_BLOCK)),
            ("unsupported intent", lambda r: r.__setitem__("packet_artifact_intent", "UNSUPPORTED")),
            ("unsupported scope", lambda r: r["packet_artifact_scope"].append("UNSUPPORTED_PACKET_ARTIFACT_SCOPE_VALUE")),
            ("missing packet boundary basis", lambda r: _delete(r, "selected_packet_boundary_basis")),
            ("missing packet boundary terminal summary", lambda r: _delete(r, "selected_packet_boundary_terminal_summary_basis")),
            ("packet boundary not recorded", lambda r: _set_nested(r, "selected_packet_boundary_basis", "outcome", "BAD")),
            ("packet boundary failed checks", lambda r: _set_nested(r, "selected_packet_boundary_basis", "failed_check_count", 1)),
            ("packet boundary bad version", lambda r: _set_nested(r, "selected_packet_boundary_basis", "result_version", "9.9.9")),
            ("packet boundary no future packet step", lambda r: _set_nested(r, "selected_packet_boundary_basis", "one_future_packet_step_declared", False)),
            ("packet boundary created packet", lambda r: _set_nested(r, "selected_packet_boundary_basis", "packet_created", True)),
            ("packet boundary emitted packet", lambda r: _set_nested(r, "selected_packet_boundary_basis", "packet_emitted", True)),
            ("packet boundary authorized transfer", lambda r: _set_nested(r, "selected_packet_boundary_basis", "packet_boundary_authorized_transfer", True)),
            ("packet boundary authorized second carrier", lambda r: _set_nested(r, "selected_packet_boundary_basis", "packet_boundary_authorized_second_carrier_execution", True)),
            ("packet boundary created cross-carrier evidence", lambda r: _set_nested(r, "selected_packet_boundary_basis", "cross_carrier_evidence_created", True)),
            ("packet boundary hidden repo state authority", lambda r: _set_nested(r, "selected_packet_boundary_basis", "hidden_repo_state_used_as_packet_authority", True)),
            ("packet boundary raw full body returned", lambda r: _set_nested(r, "selected_packet_boundary_basis", "raw_full_prior_artifact_body_returned", True)),
            ("missing command success", lambda r: _delete(r, "selected_command_success_basis")),
            ("command success not recorded", lambda r: _set_nested(r, "selected_command_success_basis", "outcome", "BAD")),
            ("command success failed checks", lambda r: _set_nested(r, "selected_command_success_basis", "failed_check_count", 1)),
            ("command success packet permission", lambda r: _set_nested(r, "selected_command_success_basis", "command_success_treated_as_packet_permission", True)),
            ("missing command result v2", lambda r: _delete(r, "selected_command_result_v2_basis")),
            ("missing output capture v2", lambda r: _delete(r, "selected_output_capture_v2_basis")),
            ("missing command output report artifact", lambda r: _delete(r, "selected_command_output_report_artifact_basis")),
            ("missing command execution", lambda r: _delete(r, "selected_command_execution_basis")),
            ("missing evidence manifest", lambda r: _delete(r, "selected_evidence_manifest_basis")),
            ("missing artifact containment", lambda r: _delete(r, "selected_artifact_containment_basis")),
            ("missing portable verification", lambda r: _delete(r, "selected_portable_verification_basis")),
            ("artifact treated as emission", flip_non_claim("packet_artifact_treated_as_packet_emission")),
            ("artifact treated as transfer", flip_non_claim("packet_artifact_treated_as_packet_transfer")),
            ("artifact treated as source", flip_non_claim("packet_artifact_treated_as_source")),
            ("artifact treated as authority", flip_non_claim("packet_artifact_treated_as_authority")),
            ("artifact treated as currentness", flip_non_claim("packet_artifact_treated_as_currentness")),
            ("artifact treated as final completion", flip_non_claim("packet_artifact_treated_as_final_completion")),
            ("artifact treated as runtime", flip_non_claim("packet_artifact_treated_as_runtime")),
            ("artifact treated as cross-carrier proof", flip_non_claim("packet_artifact_treated_as_cross_carrier_proof")),
            ("packet emitted", flip_non_claim("packet_emitted")),
            ("packet transferred", flip_non_claim("packet_transferred")),
            ("packet copied to another device", flip_non_claim("packet_copied_to_another_device")),
            ("source transfer occurred", flip_non_claim("source_transfer_occurred")),
            ("source receipt occurred", flip_non_claim("source_receipt_occurred")),
            ("reception authorization created", flip_non_claim("reception_authorization_created")),
            ("second carrier execution", flip_non_claim("second_carrier_execution_created")),
            ("second carrier receipt", flip_non_claim("second_carrier_receipt_created")),
            ("external result", flip_non_claim("external_result_created")),
            ("cross carrier evidence", flip_non_claim("cross_carrier_evidence_created")),
            ("manifest without bounded admission", flip_non_claim("manifest_created_without_bounded_admission")),
            ("checksum without bounded admission", flip_non_claim("checksum_created_without_bounded_admission")),
            ("signature without bounded admission", flip_non_claim("signature_created_without_bounded_admission")),
            ("reproducible env without bounded admission", flip_non_claim("reproducible_environment_declared_without_bounded_admission")),
            ("source created", flip_non_claim("source_created")),
            ("authority created", flip_non_claim("authority_created")),
            ("currentness created", flip_non_claim("currentness_created")),
            ("final completion claimed", flip_non_claim("final_completion_claimed")),
            ("runtime hosting created", flip_non_claim("runtime_hosting_created")),
            ("deployment created", flip_non_claim("deployment_created")),
            ("public release created", flip_non_claim("public_release_created")),
            ("operation permission created", flip_non_claim("operation_permission_created")),
            ("continuation authorized", flip_non_claim("continuation_authorized")),
            ("reusable permission created", flip_non_claim("reusable_permission_created")),
            ("follow on work authorized", flip_non_claim("follow_on_work_authorized")),
            ("artifact existence authority", flip_non_claim("artifact_existence_treated_as_packet_authority")),
            ("artifact path currentness", flip_non_claim("artifact_path_treated_as_currentness")),
            ("repo local availability authority", flip_non_claim("repo_local_availability_treated_as_packet_authority")),
            ("hidden repo state packet content", flip_non_claim("hidden_repo_state_used_as_packet_content")),
            ("hidden repo state packet authority", flip_non_claim("hidden_repo_state_used_as_packet_authority")),
            ("selected basis not reference shaped", lambda r: _set_nested(r, "selected_command_success_basis", "reference_shaped", False)),
            ("raw full prior body returned", lambda r: _set_nested(r, "selected_command_success_basis", "raw_full_prior_artifact_body_returned", True)),
            ("predecessor failure repaired", lambda r: _set_nested(r, "selected_predecessor_failure_basis", "predecessor_failures_repaired", True)),
            ("predecessor failure hidden", lambda r: _set_nested(r, "selected_predecessor_failure_basis", "predecessor_failures_hidden", True)),
            ("predecessor failure claimed passed", lambda r: _set_nested(r, "selected_predecessor_failure_basis", "predecessor_failures_claimed_passed", True)),
            ("lineage current report artifact", lambda r: _set_nested(r, "selected_command_report_lineage_basis", "command_report_lineage_treated_as_current_report_artifact", True)),
            ("lineage source", lambda r: _set_nested(r, "selected_command_report_lineage_basis", "command_report_lineage_treated_as_source", True)),
            ("lineage authority", lambda r: _set_nested(r, "selected_command_report_lineage_basis", "command_report_lineage_treated_as_authority", True)),
            ("lineage currentness", lambda r: _set_nested(r, "selected_command_report_lineage_basis", "command_report_lineage_treated_as_currentness", True)),
            ("consumed request reopened", flip_non_claim("consumed_request_reopened")),
            ("authorization token reused", flip_non_claim("authorization_token_reused")),
            ("full prior artifact body emitted", flip_non_claim("full_prior_artifact_body_emitted")),
            ("artifacts mutated", flip_non_claim("prior_artifacts_mutated")),
            ("required non-claim missing", lambda r: r["declared_non_claims"].pop("packet_emitted")),
        )

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

        for supplied in (None, ["not", "a", "mapping"]):
            with self.subTest(label=f"malformed request {type(supplied).__name__}"):
                result = resolver.resolve_portable_source_body_verification_packet_artifact(supplied)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assert_public_block_codes(result)
                self.assert_no_overreach_created(result)

    def test_path_and_write_behavior(self) -> None:
        request = _request()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_packet_artifact_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result["portable_source_body_verification_packet_artifact_metadata"]
            self.assertEqual(
                metadata["portable_source_body_verification_packet_artifact_result_version"],
                "0.1.0",
            )
            self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketArtifactError):
                resolver.resolve_portable_source_body_verification_packet_artifact_from_path(
                    malformed_path
                )

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketArtifactError):
                resolver.resolve_portable_source_body_verification_packet_artifact_from_path(array_path)

            missing_path = tmp_path / "missing.json"
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketArtifactError):
                resolver.resolve_portable_source_body_verification_packet_artifact_from_path(
                    missing_path
                )

            output_root = (
                tmp_path
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_artifact"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_portable_source_body_verification_packet_artifact_result(
                    result
                )
                second = resolver.write_portable_source_body_verification_packet_artifact_result(
                    result
                )

            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(first.parent, output_root)
            self.assertEqual(second.parent, output_root)
            self.assertTrue(first.name.endswith("__portable_source_body_verification_packet_artifact_result.json"))
            self.assertTrue(second.stem.endswith("_001"))
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            self.assertIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_artifact",
                str(first),
            )
            forbidden_roots = (
                "portable_source_body_verification_packet_boundary",
                "packet_emission",
                "manifest",
                "checksum",
                "signature",
                "cross_carrier",
                "runtime",
                "deployment",
                "public_release",
            )
            for forbidden in forbidden_roots:
                self.assertNotIn(forbidden, str(first.parent))

    def test_non_mutation(self) -> None:
        request = _request()
        original = copy.deepcopy(request)
        result = _resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, original)

    def test_raw_full_body_and_hidden_state_containment(self) -> None:
        request = _request()
        hostile_payload = {
            "raw_body": HOSTILE_RAW_VALUE,
            "raw_full_body": HOSTILE_RAW_VALUE,
            "full_body": HOSTILE_RAW_VALUE,
            "artifact_body": HOSTILE_RAW_VALUE,
            "raw_result_body": HOSTILE_RAW_VALUE,
            "raw_output_body": HOSTILE_RAW_VALUE,
            "packet_body": HOSTILE_RAW_VALUE,
            "source_body": HOSTILE_RAW_VALUE,
            "authority_body": HOSTILE_RAW_VALUE,
            "hidden_repo_state": HOSTILE_RAW_VALUE,
            "current_working_tree": HOSTILE_RAW_VALUE,
            "local_cache": HOSTILE_RAW_VALUE,
            "repo_local_only_dependency": HOSTILE_RAW_VALUE,
            "unlisted_file_dependency": HOSTILE_RAW_VALUE,
            "nested": {"list": [RAW_SENTINEL, HOSTILE_RAW_VALUE]},
        }
        for section in (
            "selected_packet_boundary_basis",
            "selected_command_success_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        ):
            request[section]["hostile_reference"] = copy.deepcopy(hostile_payload)

        original = copy.deepcopy(request)
        result = _resolve(request)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_public_block_codes(result)
        serialized = _json_text(result)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)
        self.assert_no_overreach_created(result)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_packet_content"], False)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_packet_authority"], False)
        self.assertIs(result["non_claims"]["repo_local_availability_treated_as_packet_authority"], False)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
