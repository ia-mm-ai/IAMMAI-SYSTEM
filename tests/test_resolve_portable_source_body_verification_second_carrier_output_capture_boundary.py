"""Executable checks for second-carrier-output-capture-boundary posture only.

This suite is downstream of recorded second-carrier execution output. It
verifies that the resolver records one future second-carrier output capture
step boundary only: second-carrier output capture has not been created, capture
artifact has not been created, second-carrier result/success have not been
created, external result and cross-carrier evidence have not been created, and
source/authority/currentness/runtime/final-completion/follow-on remain
unauthorized. Receiving carrier is not authority, hidden repo state is
excluded, repo-local availability is not capture authority, selected basis
stays reference-shaped, the consumed request token remains closed, and
authorization token reuse remains blocked.
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

import resolve_portable_source_body_verification_second_carrier_output_capture_boundary as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINEL = "RAW_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = (
    "HOSTILE_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN"
)
REDACTION_STRINGS = {
    "[bounded-redacted-raw-or-hidden-state]",
    "[bounded-reference-redacted-raw-or-hidden-state]",
    "[bounded-reference-omitted-raw-or-hidden-state]",
}

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_output_capture_boundary_metadata",
    "declared_second_carrier_output_capture_boundary_question",
    "selected_second_carrier_execution_output_basis",
    "selected_second_carrier_execution_output_terminal_summary_basis",
    "selected_second_carrier_execution_output_boundary_basis",
    "selected_second_carrier_execution_basis",
    "selected_second_carrier_execution_boundary_basis",
    "selected_second_carrier_receipt_basis",
    "selected_packet_transfer_basis",
    "selected_packet_emission_basis",
    "selected_packet_emission_boundary_v2_basis",
    "selected_packet_emission_boundary_v1_predecessor_failure_basis",
    "selected_packet_artifact_basis",
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
    "second_carrier_output_capture_boundary_only_posture",
    "one_future_second_carrier_output_capture_step_posture",
    "second_carrier_execution_output_basis_preserved_posture",
    "output_artifact_basis_preserved_posture",
    "output_not_capture_posture",
    "capture_not_created_posture",
    "capture_artifact_not_created_posture",
    "second_carrier_result_not_created_posture",
    "second_carrier_success_not_created_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "capture_not_source_transfer_posture",
    "capture_not_source_receipt_posture",
    "capture_not_reception_authorization_posture",
    "receiving_carrier_not_authority_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "final_completion_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_capture_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "second_carrier_output_capture_boundary_scope",
    "second_carrier_output_capture_boundary_checks",
    "second_carrier_output_capture_boundary_statement",
    "second_carrier_output_capture_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_output_capture_boundary_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_OUTPUT_NOT_RECORDED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_EXECUTION_OUTPUT_DID_NOT_RECORD_BOUNDED_OUTPUT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_ALREADY_CREATED_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_ALREADY_CREATED_SECOND_CARRIER_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_CAPTURE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_SUCCESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_USED_HIDDEN_REPO_STATE_AS_CAPTURE_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_REPO_LOCAL_AVAILABILITY_AS_CAPTURE_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_OUTPUT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CAPTURE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CAPTURE_ARTIFACT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SOURCE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "SECOND_CARRIER_OUTPUT_CAPTURE_CREATED",
    "CAPTURE_ARTIFACT_CREATED",
    "SECOND_CARRIER_RESULT_CREATED",
    "SECOND_CARRIER_SUCCESS_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_CAPTURE_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_CAPTURE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_CAPTURE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_CAPTURE_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_CAPTURE_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE",
)

FALSE_NON_CLAIMS_TO_CHECK = (
    "second_carrier_output_capture_created",
    "capture_artifact_created",
    "second_carrier_result_created",
    "second_carrier_success_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_output_capture_boundary_treated_as_capture",
    "second_carrier_output_capture_boundary_treated_as_capture_artifact",
    "second_carrier_output_capture_boundary_treated_as_result",
    "second_carrier_output_capture_boundary_treated_as_success",
    "second_carrier_output_capture_boundary_treated_as_external_result",
    "second_carrier_output_capture_boundary_treated_as_cross_carrier_evidence",
    "second_carrier_output_capture_boundary_treated_as_source_transfer",
    "second_carrier_output_capture_boundary_treated_as_source_receipt",
    "second_carrier_output_capture_boundary_treated_as_reception_authorization",
    "second_carrier_output_capture_boundary_treated_as_source",
    "second_carrier_output_capture_boundary_treated_as_authority",
    "second_carrier_output_capture_boundary_treated_as_currentness",
    "second_carrier_output_capture_boundary_treated_as_final_completion",
    "second_carrier_output_capture_boundary_treated_as_runtime",
    "second_carrier_output_capture_boundary_treated_as_continuation",
    "second_carrier_output_capture_boundary_treated_as_reusable_permission",
    "second_carrier_output_capture_boundary_treated_as_follow_on_work",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_capture_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_capture_authority",
    "hidden_repo_state_used_as_capture_content",
    "hidden_repo_state_used_as_capture_authority",
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


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _request(**overrides: Any) -> dict[str, Any]:
    request = (
        resolver.build_declared_portable_source_body_verification_second_carrier_output_capture_boundary_request(
            second_carrier_output_capture_boundary_request_id=(
                "second_carrier_output_capture_boundary_test_request_001"
            )
        )
    )
    request["second_carrier_output_capture_boundary_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = _false_non_claims()

    request["selected_second_carrier_execution_output_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED",
        result_version="0.1.0",
        failed_check_count=0,
        bounded_second_carrier_execution_output_recorded=True,
        second_carrier_execution_output_recorded=True,
        output_artifact_recorded_or_bounded=True,
        output_recorded_bounded=True,
        output_not_capture=True,
        output_not_result=True,
        output_not_success=True,
        output_not_external_result=True,
        output_not_cross_carrier_evidence=True,
        second_carrier_output_capture_not_created=True,
        second_carrier_result_not_created=True,
        second_carrier_success_not_created=True,
        external_result_not_created=True,
        cross_carrier_evidence_not_created=True,
        receiving_carrier_not_authority=True,
        hidden_repo_state_excluded=True,
        hidden_repo_state_not_used_as_capture_authority=True,
        hidden_repo_state_not_used_as_output_authority=True,
        repo_local_availability_not_capture_authority=True,
        repo_local_availability_not_output_authority=True,
        selected_basis_reference_shape_preserved=True,
        raw_full_prior_artifact_body_not_returned=True,
    )
    request["selected_second_carrier_execution_output_terminal_summary_basis"].update(
        outcome=(
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_"
            "TERMINAL_SUMMARY_STANDING"
        ),
        terminal_summary_preserved=True,
    )
    request["selected_second_carrier_execution_output_boundary_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_RECORDED",
        result_version="0.1.0",
        failed_check_count=0,
    )
    request["selected_second_carrier_execution_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED",
        result_version="0.1.0",
        failed_check_count=0,
    )
    request["selected_second_carrier_execution_boundary_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED",
        result_version="0.1.0",
        failed_check_count=0,
    )
    request["selected_second_carrier_receipt_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_RECORDED",
        result_version="0.1.0",
        failed_check_count=0,
    )
    request["selected_packet_transfer_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_RECORDED",
        result_version="0.1.0",
        failed_check_count=0,
    )
    request["selected_packet_emission_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_RECORDED",
        result_version="0.1.0",
        failed_check_count=0,
    )
    request["selected_packet_emission_boundary_v2_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_RECORDED",
        result_version="0.2.0",
        failed_check_count=0,
    )
    request["selected_packet_emission_boundary_v1_predecessor_failure_basis"].update(
        v1_predecessor_failure_preserved=True,
        v1_repaired=False,
        v1_hidden=False,
        v1_claimed_passed=False,
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_V1_FAILED",
    )
    request["selected_packet_artifact_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED",
        result_version="0.1.0",
        failed_check_count=0,
    )
    request["selected_command_success_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED",
        result_version="0.1.0",
        failed_check_count=0,
    )
    request["selected_command_result_v2_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED",
        result_version="0.2.0",
        failed_check_count=0,
    )
    request["selected_output_capture_v2_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED",
        result_version="0.2.0",
        failed_check_count=0,
        original_carrier_output_capture_posture_only=True,
    )
    request["selected_command_output_report_artifact_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED",
        result_version="0.1.0",
        failed_check_count=0,
    )
    request["selected_command_execution_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED",
        original_carrier_execution_trace_audit_only=True,
    )
    request["selected_command_report_lineage_basis"].update(
        command_report_lineage_only=True,
        command_report_lineage_not_current_report_artifact=True,
        command_report_lineage_not_source=True,
        command_report_lineage_not_authority=True,
        command_report_lineage_not_currentness=True,
    )
    request["selected_predecessor_failure_basis"].update(
        predecessor_failures_visible=True,
        predecessor_failures_unrepaired=True,
    )
    request["selected_evidence_manifest_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_STANDING"
    )
    request["selected_artifact_containment_basis"].update(
        artifact_containment_basis_preserved=True
    )
    request["selected_portable_verification_basis"].update(
        portable_verification_boundary_basis_preserved=True
    )

    for key in POSTURE_KEYS:
        request[key] = {
            "posture_key": key,
            "posture_declared": True,
            "declared": True,
            "preserves_capture_boundary_membrane": True,
        }

    request.update(overrides)
    return request


def _resolve(request: Mapping[str, Any] | None) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_second_carrier_output_capture_boundary(
        declared_second_carrier_output_capture_boundary_request=request
    )


def _remove_execution_output_basis(request: dict[str, Any]) -> None:
    request["selected_second_carrier_execution_output_basis"] = {}
    for key in (
        "selected_second_carrier_execution_output_result_path",
        "selected_second_carrier_execution_output_result_id",
        "selected_second_carrier_execution_output_result_outcome",
        "selected_second_carrier_execution_output_result_version",
    ):
        request.pop(key, None)


def _block_cases() -> list[tuple[str, Callable[[dict[str, Any]], None]]]:
    cases: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
        (
            "explicit block intent",
            lambda request: request.__setitem__(
                "second_carrier_output_capture_boundary_intent", resolver.INTENT_BLOCK
            ),
        ),
        (
            "unsupported intent",
            lambda request: request.__setitem__(
                "second_carrier_output_capture_boundary_intent", "UNSUPPORTED_INTENT"
            ),
        ),
        (
            "unsupported scope",
            lambda request: request.__setitem__(
                "second_carrier_output_capture_boundary_scope", ["UNSUPPORTED_SCOPE"]
            ),
        ),
        ("missing second-carrier execution output basis", _remove_execution_output_basis),
        (
            "second-carrier execution output not recorded",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_result_outcome",
                "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_NOT_RECORDED",
            ),
        ),
        (
            "second-carrier execution output failed checks",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_failed_check_count", 1
            ),
        ),
        (
            "second-carrier execution output version not 0.1.0",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_result_version", "9.9.9"
            ),
        ),
        (
            "second-carrier execution output did not record bounded output",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_bounded_output_recorded",
                False,
            ),
        ),
        (
            "second-carrier execution output already created output capture",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_already_created_output_capture",
                True,
            ),
        ),
        (
            "second-carrier execution output already created second-carrier result",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_already_created_second_carrier_result",
                True,
            ),
        ),
        (
            "second-carrier execution output already created second-carrier success",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_already_created_second_carrier_success",
                True,
            ),
        ),
        (
            "second-carrier execution output created external result",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_created_external_result", True
            ),
        ),
        (
            "second-carrier execution output created cross-carrier evidence",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_created_cross_carrier_evidence",
                True,
            ),
        ),
        (
            "second-carrier execution output treated output as capture",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_treated_output_as_capture",
                True,
            ),
        ),
        (
            "second-carrier execution output treated output as result",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_treated_output_as_result", True
            ),
        ),
        (
            "second-carrier execution output treated output as success",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_treated_output_as_success",
                True,
            ),
        ),
        (
            "second-carrier execution output treated output as external result",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_treated_output_as_external_result",
                True,
            ),
        ),
        (
            "second-carrier execution output treated output as cross-carrier evidence",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_treated_output_as_cross_carrier_evidence",
                True,
            ),
        ),
        (
            "second-carrier execution output used hidden repo state as capture authority",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_used_hidden_repo_state_as_capture_authority",
                True,
            ),
        ),
        (
            "second-carrier execution output treated repo-local availability as capture authority",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_treated_repo_local_availability_as_capture_authority",
                True,
            ),
        ),
        (
            "second-carrier execution output treated receiving carrier as authority",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_treated_receiving_carrier_as_authority",
                True,
            ),
        ),
        (
            "second-carrier execution output returned raw full prior artifact body outside bounded output",
            lambda request: request.__setitem__(
                "selected_second_carrier_execution_output_raw_full_prior_artifact_body_returned_outside_bounded_output",
                True,
            ),
        ),
        (
            "selected basis not reference-shaped",
            lambda request: request.__setitem__("selected_basis_not_reference_shaped", True),
        ),
        (
            "command report lineage treated as current report artifact",
            lambda request: request.__setitem__(
                "command_report_lineage_treated_as_current_report_artifact", True
            ),
        ),
        (
            "command report lineage treated as source",
            lambda request: request.__setitem__("command_report_lineage_treated_as_source", True),
        ),
        (
            "command report lineage treated as authority",
            lambda request: request.__setitem__(
                "command_report_lineage_treated_as_authority", True
            ),
        ),
        (
            "command report lineage treated as currentness",
            lambda request: request.__setitem__(
                "command_report_lineage_treated_as_currentness", True
            ),
        ),
        (
            "full prior artifact body emitted outside bounded capture-boundary posture",
            lambda request: request.__setitem__(
                "full_prior_artifact_body_emitted_outside_bounded_capture_boundary",
                True,
            ),
        ),
        (
            "required non-claim missing",
            lambda request: request["declared_non_claims"].pop(
                "second_carrier_output_capture_created"
            ),
        ),
        (
            "required non-claim flipped",
            lambda request: request["declared_non_claims"].__setitem__(
                "second_carrier_output_capture_created", True
            ),
        ),
    ]
    cases.extend(
        (
            f"{key} basis missing",
            lambda request, basis_key=key: request.__setitem__(basis_key, {}),
        )
        for key in SELECTED_BASIS_KEYS
        if key != "selected_second_carrier_execution_output_basis"
    )
    cases.extend(
        (
            f"{key} posture missing",
            lambda request, posture_key=key: request.pop(posture_key, None),
        )
        for key in POSTURE_KEYS
    )
    cases.extend(
        (
            f"{key} true",
            lambda request, claim_key=key: request.__setitem__(claim_key, True),
        )
        for key in REQUIRED_FALSE_NON_CLAIMS
    )
    return cases


def _hostile_payload() -> dict[str, Any]:
    return {
        "raw_body": RAW_SENTINEL,
        "raw_full_body": HOSTILE_RAW_VALUE,
        "full_body": "full-body-value-MUST_NOT_RETURN",
        "artifact_body": "artifact-body-value-MUST_NOT_RETURN",
        "raw_result_body": "raw-result-body-MUST_NOT_RETURN",
        "raw_output_body": "raw-output-body-MUST_NOT_RETURN",
        "execution_body": "execution-body-MUST_NOT_RETURN",
        "execution_artifact_body": "execution-artifact-body-MUST_NOT_RETURN",
        "output_body": "output-body-MUST_NOT_RETURN",
        "output_artifact_body": "output-artifact-body-MUST_NOT_RETURN",
        "capture_body": "capture-body-MUST_NOT_RETURN",
        "capture_artifact_body": "capture-artifact-body-MUST_NOT_RETURN",
        "second_carrier_output_capture_body": "second-carrier-output-capture-body-MUST_NOT_RETURN",
        "second_carrier_result_body": "second-carrier-result-body-MUST_NOT_RETURN",
        "second_carrier_success_body": "second-carrier-success-body-MUST_NOT_RETURN",
        "external_result_body": "external-result-body-MUST_NOT_RETURN",
        "cross_carrier_evidence_body": "cross-carrier-evidence-body-MUST_NOT_RETURN",
        "packet_body": "packet-body-MUST_NOT_RETURN",
        "source_body": "source-body-MUST_NOT_RETURN",
        "authority_body": "authority-body-MUST_NOT_RETURN",
        "hidden_repo_state": "hidden-repo-state-MUST_NOT_RETURN",
        "current_working_tree": "current-working-tree-MUST_NOT_RETURN",
        "local_cache": "local-cache-MUST_NOT_RETURN",
        "repo_local_only_dependency": "repo-local-only-dependency-MUST_NOT_RETURN",
        "carrier_possession": "carrier-possession-MUST_NOT_RETURN",
        "copy_presence": "copy-presence-MUST_NOT_RETURN",
        "receiving_carrier": "receiving-carrier-MUST_NOT_RETURN",
        "receipt_artifact_presence": "receipt-artifact-presence-MUST_NOT_RETURN",
        "execution_artifact_presence": "execution-artifact-presence-MUST_NOT_RETURN",
        "output_artifact_presence": "output-artifact-presence-MUST_NOT_RETURN",
        "capture_artifact_presence": "capture-artifact-presence-MUST_NOT_RETURN",
        "capture_path_existence": "capture-path-existence-MUST_NOT_RETURN",
        "unlisted_file_dependency": "unlisted-file-dependency-MUST_NOT_RETURN",
        "nested": {
            "list": [
                RAW_SENTINEL,
                {"deeper": HOSTILE_RAW_VALUE},
            ],
        },
    }


class SecondCarrierOutputCaptureBoundaryResolverTests(unittest.TestCase):
    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping):
            block_code = block.get("block_code")
            if block_code:
                self.assertIn(block_code, resolver.BLOCK_CODES)
        checks = result.get("second_carrier_output_capture_boundary_checks", [])
        self.assertIsInstance(checks, list)
        for check in checks:
            self.assertIsInstance(check, Mapping)
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_booleans(self, result: Mapping[str, Any]) -> None:
        statement = result.get("second_carrier_output_capture_boundary_statement", {})
        self.assertIsInstance(statement, Mapping)
        for key in (
            TRUE_RECORDED_FIELDS
            + REQUIRED_FALSE_NON_CLAIMS
            + (
                "full_prior_artifact_body_emitted_outside_bounded_capture_boundary",
                "artifacts_mutated",
            )
        ):
            if key in statement:
                self.assertIs(type(statement[key]), bool, key)
                self.assertNotIn(statement[key], REDACTION_STRINGS, key)

        non_claims = result.get("non_claims", {})
        self.assertIsInstance(non_claims, Mapping)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(type(non_claims[key]), bool, key)
            self.assertNotIn(non_claims[key], REDACTION_STRINGS, key)

        summary = result.get(
            "portable_source_body_verification_second_carrier_output_capture_boundary_summary",
            {},
        )
        self.assertIsInstance(summary, Mapping)
        for key in TRUE_RECORDED_FIELDS + REQUIRED_FALSE_NON_CLAIMS:
            if key in summary:
                self.assertIs(type(summary[key]), bool, key)

    def assert_no_raw_or_hidden_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _json_text(result)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)
        self.assertNotIn("MUST_NOT_RETURN", serialized)
        self.assertNotIn("HOSTILE_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY", serialized)

    def assert_no_later_work_created(self, result: Mapping[str, Any]) -> None:
        statement = result.get("second_carrier_output_capture_boundary_statement", {})
        non_claims = result.get("non_claims", {})
        self.assertIsInstance(statement, Mapping)
        self.assertIsInstance(non_claims, Mapping)
        for key in FALSE_NON_CLAIMS_TO_CHECK:
            self.assertFalse(statement.get(key), key)
            self.assertFalse(non_claims.get(key), key)
        self.assertFalse(non_claims.get("consumed_request_reopened"))
        self.assertFalse(non_claims.get("authorization_token_reused"))
        self.assertFalse(non_claims.get("v1_repaired"))
        self.assertFalse(non_claims.get("v1_hidden"))
        self.assertFalse(non_claims.get("v1_claimed_passed"))

    def recorded_result(self) -> dict[str, Any]:
        result = _resolve(_request())
        self.assertEqual(result["outcome"], RECORDED)
        return result

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_output_capture_boundary",
            "resolve_portable_source_body_verification_second_carrier_output_capture_boundary_from_path",
            "write_portable_source_body_verification_second_carrier_output_capture_boundary_result",
            "build_portable_source_body_verification_second_carrier_output_capture_boundary_summary",
            "build_declared_portable_source_body_verification_second_carrier_output_capture_boundary_request",
        ):
            self.assertTrue(hasattr(resolver, name), name)
            self.assertTrue(callable(getattr(resolver, name)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_output_capture_boundary"
            )
        )
        self.assertEqual(set(SUPPORTED_SCOPE), set(resolver.SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE))
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_second_carrier_output_capture_boundary_recorded_result(self) -> None:
        request = _request()
        original = copy.deepcopy(request)

        result = _resolve(request)

        self.assertEqual(request, original)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertFalse(result["block"]["blocked"])
        self.assertIsNone(result["block"]["block_code"])

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)

        metadata = result[
            "portable_source_body_verification_second_carrier_output_capture_boundary_metadata"
        ]
        self.assertEqual(
            metadata[
                "portable_source_body_verification_second_carrier_output_capture_boundary_result_version"
            ],
            "0.1.0",
        )
        self.assertEqual(metadata["result_version"], "0.1.0")
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_second_carrier_output_capture_boundary",
        )
        self.assertEqual(
            metadata["second_carrier_output_capture_boundary_request_id"],
            request["second_carrier_output_capture_boundary_request_id"],
        )
        self.assertEqual(metadata["failed_check_count"], 0)
        self.assertGreater(metadata["passed_check_count"], 0)

        selected_output = result["selected_second_carrier_execution_output_basis"]
        self.assertEqual(
            selected_output["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED",
        )
        self.assertEqual(selected_output["result_version"], "0.1.0")
        self.assertEqual(selected_output["failed_check_count"], 0)
        self.assertTrue(selected_output["bounded_second_carrier_execution_output_recorded"])
        self.assertTrue(selected_output["output_not_capture"])
        self.assertTrue(selected_output["second_carrier_output_capture_not_created"])

        statement = result["second_carrier_output_capture_boundary_statement"]
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(statement[key], True, key)
        for key in FALSE_NON_CLAIMS_TO_CHECK:
            self.assertIs(statement[key], False, key)
            self.assertIs(result["non_claims"][key], False, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(result["non_claims"][key], False, key)

        non_meaning = result["second_carrier_output_capture_boundary_non_meaning"]
        for key in (
            "second_carrier_output_capture_exists",
            "capture_artifact_exists",
            "second_carrier_result_exists",
            "second_carrier_success_exists",
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
            "capture_boundary_became_capture",
            "capture_boundary_became_result",
            "capture_boundary_became_success",
            "output_became_capture",
            "output_artifact_became_capture",
            "receiving_carrier_became_authority",
            "transferred_packet_became_source_authority_or_currentness",
            "artifact_existence_became_capture_authority",
            "artifact_path_became_currentness",
            "repo_local_availability_became_capture_authority",
            "hidden_repo_state_became_capture_authority",
            "v1_packet_emission_boundary_resolver_repaired_hidden_erased_or_claimed_passed",
        ):
            self.assertIn(key, non_meaning)
            self.assertIs(non_meaning[key], False, key)

        self.assertEqual(
            result["additional_basis_required"]["requires_additional_basis"], False
        )
        self.assertEqual(result["not_recorded_basis"]["not_recorded"], False)
        self.assertTrue(result["what_remains_open"]["open_means_not_scheduled"])
        self.assertTrue(result["what_remains_open"]["open_means_not_authorized"])
        self.assertTrue(result["what_remains_open"]["open_means_not_executed"])

        self.assert_public_codes(result)
        self.assert_generated_booleans_are_booleans(result)
        self.assert_no_raw_or_hidden_sentinels(result)

    def test_summary_helper_preserves_capture_boundary_posture(self) -> None:
        result = self.recorded_result()
        summary = (
            resolver.build_portable_source_body_verification_second_carrier_output_capture_boundary_summary(
                result
            )
        )

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["request_id"],
            result[
                "portable_source_body_verification_second_carrier_output_capture_boundary_metadata"
            ]["second_carrier_output_capture_boundary_request_id"],
        )
        self.assertEqual(summary["question"], resolver.CORE_QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)

        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(summary[key], True, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(summary[key], False, key)
            self.assertIs(summary["key_non_claims"][key], False, key)

        self.assertEqual(
            summary["selected_second_carrier_execution_output_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED",
        )
        self.assertEqual(
            summary["selected_second_carrier_execution_output_result_version"], "0.1.0"
        )
        self.assertEqual(
            summary["selected_second_carrier_execution_output_failed_check_count"], 0
        )
        self.assertTrue(
            summary["no_capture_result_success_external_result_or_cross_carrier_evidence"]
        )
        self.assertTrue(summary["no_source_authority_currentness_final_completion_runtime"])
        self.assertTrue(summary["no_deployment_public_release_or_follow_on"])
        self.assertTrue(summary["v1_predecessor_failure_preserved"])
        self.assertTrue(summary["v1_not_repaired_hidden_or_claimed_passed"])

    def test_representative_blocking_behavior(self) -> None:
        missing_request = _resolve(None)
        self.assertEqual(missing_request["outcome"], BLOCKED)
        self.assert_public_codes(missing_request)
        self.assert_no_later_work_created(missing_request)

        non_mapping_request = (
            resolver.resolve_portable_source_body_verification_second_carrier_output_capture_boundary(
                declared_second_carrier_output_capture_boundary_request=["not", "a", "mapping"]  # type: ignore[arg-type]
            )
        )
        self.assertEqual(non_mapping_request["outcome"], BLOCKED)
        self.assert_public_codes(non_mapping_request)
        self.assert_no_later_work_created(non_mapping_request)

        for label, mutate in _block_cases():
            with self.subTest(label=label):
                request = _request()
                mutate(request)
                result = _resolve(request)

                self.assertEqual(result["outcome"], BLOCKED)
                self.assertTrue(result["block"]["blocked"])
                self.assertIsNotNone(result["block"]["block_code"])
                self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
                self.assert_public_codes(result)
                self.assert_no_later_work_created(result)
                self.assert_generated_booleans_are_booleans(result)

    def test_path_and_write_behavior(self) -> None:
        request = _request()

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(
                json.dumps(request, indent=2, sort_keys=True), encoding="utf-8"
            )

            result = (
                resolver.resolve_portable_source_body_verification_second_carrier_output_capture_boundary_from_path(
                    request_path
                )
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result[
                "portable_source_body_verification_second_carrier_output_capture_boundary_metadata"
            ]
            self.assertEqual(metadata["result_version"], "0.1.0")
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_second_carrier_output_capture_boundary",
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            try:
                malformed_result = (
                    resolver.resolve_portable_source_body_verification_second_carrier_output_capture_boundary_from_path(
                        malformed_path
                    )
                )
            except resolver.PortableSourceBodyVerificationSecondCarrierOutputCaptureBoundaryError:
                malformed_result = None
            if malformed_result is not None:
                self.assertEqual(malformed_result["outcome"], BLOCKED)
                self.assert_public_codes(malformed_result)

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_portable_source_body_verification_second_carrier_output_capture_boundary_from_path(
                    array_path
                )
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assert_public_codes(array_result)

            missing_path = tmp_path / "missing.json"
            try:
                missing_result = (
                    resolver.resolve_portable_source_body_verification_second_carrier_output_capture_boundary_from_path(
                        missing_path
                    )
                )
            except resolver.PortableSourceBodyVerificationSecondCarrierOutputCaptureBoundaryError:
                missing_result = None
            if missing_result is not None:
                self.assertEqual(missing_result["outcome"], BLOCKED)
                self.assert_public_codes(missing_result)

            redirected_root = (
                tmp_path
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_output_capture_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", redirected_root):
                first_path = (
                    resolver.write_portable_source_body_verification_second_carrier_output_capture_boundary_result(
                        result
                    )
                )
                second_path = (
                    resolver.write_portable_source_body_verification_second_carrier_output_capture_boundary_result(
                        result
                    )
                )

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(str(first_path).startswith(str(redirected_root)))
            self.assertTrue(str(second_path).startswith(str(redirected_root)))
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)

            first_path_text = str(first_path)
            self.assertIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_output_capture_boundary",
                first_path_text,
            )
            for forbidden_root in (
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_output_capture/",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_execution_output/",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result/",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success/",
                "external_result",
                "cross_carrier",
                "runtime",
                "deployment",
                "public_release",
            ):
                self.assertNotIn(forbidden_root, first_path_text)

    def test_resolver_does_not_mutate_request_or_selected_basis(self) -> None:
        request = _request()
        original = copy.deepcopy(request)
        selected_basis_original = {
            key: copy.deepcopy(request[key]) for key in SELECTED_BASIS_KEYS
        }
        posture_original = {key: copy.deepcopy(request[key]) for key in POSTURE_KEYS}
        scope_original = copy.deepcopy(request["second_carrier_output_capture_boundary_scope"])
        non_claims_original = copy.deepcopy(request["declared_non_claims"])

        result = _resolve(request)

        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, original)
        for key in SELECTED_BASIS_KEYS:
            self.assertEqual(request[key], selected_basis_original[key], key)
        for key in POSTURE_KEYS:
            self.assertEqual(request[key], posture_original[key], key)
        self.assertEqual(
            request["second_carrier_output_capture_boundary_scope"], scope_original
        )
        self.assertEqual(request["declared_non_claims"], non_claims_original)

    def test_raw_full_body_and_hidden_repo_state_containment(self) -> None:
        request = _request()
        injected_sections = (
            "selected_second_carrier_execution_output_basis",
            "selected_second_carrier_execution_output_boundary_basis",
            "selected_second_carrier_execution_basis",
            "selected_second_carrier_receipt_basis",
            "selected_packet_transfer_basis",
            "selected_packet_emission_basis",
            "selected_packet_emission_boundary_v2_basis",
            "selected_packet_artifact_basis",
            "selected_command_success_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        )
        for section in injected_sections:
            request[section].update(_hostile_payload())
        original = copy.deepcopy(request)

        result = _resolve(request)

        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_public_codes(result)
        self.assert_no_later_work_created(result)
        self.assert_generated_booleans_are_booleans(result)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
