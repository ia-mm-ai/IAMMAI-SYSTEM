"""Resolve portable source-body verification second-carrier result boundary.

This module records one bounded second-carrier result-boundary posture only.
It is downstream of returned real second-carrier live capture intake. It does
not create second-carrier result, second-carrier success, external result,
cross-carrier evidence, source transfer, source receipt, reception
authorization, source, authority, currentness, final completion, runtime,
continuation, reusable permission, derivative reception, vessel relation,
another reception request, or follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class PortableSourceBodyVerificationSecondCarrierResultBoundaryError(Exception):
    """Raised for unreadable declared paths or impossible resolver shape."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_second_carrier_result_boundary"
)
RESULT_TYPE = "portable_source_body_verification_second_carrier_result_boundary_result"
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "second_carrier_result_boundary"
)

CORE_QUESTION = (
    "Can the preserved real returned second-carrier capture be bounded for one "
    "future second-carrier result step without creating result yet, creating "
    "second-carrier success, creating external result, creating cross-carrier "
    "evidence, creating source transfer, creating source receipt, creating "
    "reception authorization, creating source, authority, currentness, runtime, "
    "final completion, continuation, reusable permission, derivative reception, "
    "vessel relation, another reception request, or follow-on work?"
)

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BOUNDARY_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = (
    "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BOUNDARY"
)
SUPPORTED_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

EXPECTED_OUTPUT_CAPTURE_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED"
)

SUPPORTED_SCOPE_VALUES = {
    "SECOND_CARRIER_RESULT_BOUNDARY_ONLY",
    "ONE_FUTURE_SECOND_CARRIER_RESULT_STEP_ONLY",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_ARTIFACT_BASIS_PRESERVED",
    "ZERO_EXIT_CODE_NOT_SUCCESS",
    "OK_OUTPUT_NOT_VERIFICATION",
    "RETURNED_CAPTURE_NOT_CROSS_CARRIER_PROOF",
    "RESULT_NOT_CREATED",
    "SECOND_CARRIER_SUCCESS_NOT_CREATED",
    "EXTERNAL_RESULT_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "RESULT_NOT_SOURCE_TRANSFER",
    "RESULT_NOT_SOURCE_RECEIPT",
    "RESULT_NOT_RECEPTION_AUTHORIZATION",
    "RECEIVING_CARRIER_NOT_AUTHORITY",
    "NO_SOURCE_CREATED",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
    "NO_FINAL_COMPLETION",
    "NO_RUNTIME_CREATED",
    "NO_DEPLOYMENT_CREATED",
    "NO_PUBLIC_RELEASE_CREATED",
    "NO_OPERATION_PERMISSION_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "NO_REUSABLE_PERMISSION",
    "NO_DERIVATIVE_RECEPTION",
    "NO_VESSEL_RELATION",
    "NO_ANOTHER_RECEPTION_REQUEST",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
    "NO_RESULT_INFERENCE",
    "NO_SUCCESS_INFERENCE",
    "NO_EXTERNAL_RESULT_INFERENCE",
    "NO_CROSS_CARRIER_EVIDENCE_INFERENCE",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_FINAL_COMPLETION_INFERENCE",
    "NO_RUNTIME_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_RESULT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_RESULT_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "COMMAND_REPORT_LINEAGE_NOT_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_NOT_SOURCE",
    "COMMAND_REPORT_LINEAGE_NOT_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_NOT_CURRENTNESS",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
}

SELECTED_BASIS_KEYS = (
    "selected_returned_second_carrier_live_capture_intake_basis",
    "selected_actual_second_carrier_live_capture_packet_basis",
    "selected_actual_second_carrier_live_runbook_basis",
    "selected_returned_capture_material_basis",
    "selected_returned_zip_basis",
    "selected_returned_hash_basis",
    "selected_returned_extracted_files_basis",
    "selected_returned_combined_terminal_log_basis",
    "selected_returned_exit_code_basis",
    "selected_returned_command_text_basis",
    "selected_returned_timestamps_basis",
    "selected_second_carrier_output_capture_basis",
    "selected_second_carrier_output_capture_terminal_summary_basis",
    "selected_second_carrier_output_capture_boundary_basis",
    "selected_second_carrier_execution_output_basis",
    "selected_second_carrier_execution_basis",
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
)

POSTURE_KEYS = (
    "second_carrier_result_boundary_only_posture",
    "one_future_second_carrier_result_step_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "capture_artifact_basis_preserved_posture",
    "zero_exit_code_not_success_posture",
    "ok_output_not_verification_posture",
    "returned_capture_not_cross_carrier_proof_posture",
    "result_not_created_posture",
    "second_carrier_success_not_created_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "result_not_source_transfer_posture",
    "result_not_source_receipt_posture",
    "result_not_reception_authorization_posture",
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
    "repo_local_availability_not_result_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
)

FALSE_NON_CLAIM_KEYS = (
    "second_carrier_result_created",
    "second_carrier_success_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "returned_capture_treated_as_result",
    "returned_capture_treated_as_success",
    "returned_capture_treated_as_verification",
    "returned_capture_treated_as_cross_carrier_evidence",
    "returned_capture_treated_as_source",
    "returned_capture_treated_as_authority",
    "returned_capture_treated_as_currentness",
    "returned_capture_treated_as_runtime",
    "returned_capture_treated_as_final_completion",
    "zero_exit_code_treated_as_success",
    "ok_output_treated_as_verification",
    "ran_7_tests_treated_as_cross_carrier_proof",
    "second_carrier_result_boundary_treated_as_result",
    "second_carrier_result_boundary_treated_as_success",
    "second_carrier_result_boundary_treated_as_external_result",
    "second_carrier_result_boundary_treated_as_cross_carrier_evidence",
    "second_carrier_result_boundary_treated_as_source_transfer",
    "second_carrier_result_boundary_treated_as_source_receipt",
    "second_carrier_result_boundary_treated_as_reception_authorization",
    "second_carrier_result_boundary_treated_as_source",
    "second_carrier_result_boundary_treated_as_authority",
    "second_carrier_result_boundary_treated_as_currentness",
    "second_carrier_result_boundary_treated_as_final_completion",
    "second_carrier_result_boundary_treated_as_runtime",
    "second_carrier_result_boundary_treated_as_continuation",
    "second_carrier_result_boundary_treated_as_reusable_permission",
    "second_carrier_result_boundary_treated_as_follow_on_work",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_result_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_result_authority",
    "hidden_repo_state_used_as_result_content",
    "hidden_repo_state_used_as_result_authority",
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

TRUE_STATEMENT_KEYS = (
    "second_carrier_result_boundary_recorded",
    "one_future_second_carrier_result_step_declared",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "capture_artifact_basis_preserved",
    "zero_exit_code_not_success",
    "ok_output_not_verification",
    "returned_capture_not_cross_carrier_proof",
    "result_not_created",
    "second_carrier_success_not_created",
    "external_result_not_created",
    "cross_carrier_evidence_not_created",
    "result_not_source_transfer",
    "result_not_source_receipt",
    "result_not_reception_authorization",
    "receiving_carrier_not_authority",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "final_completion_not_created",
    "runtime_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_result_authority",
    "repo_local_availability_not_result_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

BLOCK_CODES = {
    "DECLARED_SECOND_CARRIER_RESULT_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_SECOND_CARRIER_RESULT_BOUNDARY_REQUEST_UNREADABLE",
    "SECOND_CARRIER_RESULT_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_RESULT_BOUNDARY_BLOCK_REQUESTED",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_RESULT",
    "RETURNED_CAPTURE_TREATED_AS_SUCCESS",
    "RETURNED_CAPTURE_TREATED_AS_VERIFICATION",
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
    "OK_OUTPUT_TREATED_AS_VERIFICATION",
    "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
    "RETURNED_CAPTURE_MATERIAL_MISSING",
    "RETURNED_ZIP_PATH_MISSING",
    "RETURNED_HASH_PATH_MISSING",
    "RETURNED_EXTRACTED_DIRECTORY_MISSING",
    "RETURNED_COMBINED_TERMINAL_LOG_MISSING",
    "RETURNED_EXIT_CODE_MISSING",
    "RETURNED_COMMAND_TEXT_MISSING",
    "RETURNED_TIMESTAMPS_MISSING",
    "RETURNED_CAPTURE_ALREADY_CREATED_RESULT",
    "RETURNED_CAPTURE_ALREADY_CREATED_SUCCESS",
    "RETURNED_CAPTURE_ALREADY_CREATED_EXTERNAL_RESULT",
    "RETURNED_CAPTURE_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
    "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_DID_NOT_RECORD_BOUNDED_CAPTURE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_SUCCESS",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_RESULT",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_SOURCE",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "ARTIFACT_EXISTENCE_TREATED_AS_RESULT_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RESULT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RESULT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RESULT_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_RESULT_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_RESULT_BOUNDARY_SCOPE",
}

SENSITIVE_BODY_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "prior_artifact_body",
    "raw_prior_artifact_body",
    "raw_full_prior_artifact_body",
    "raw_result_body",
    "raw_output_body",
    "result_body",
    "success_body",
    "external_result_body",
    "cross_carrier_evidence_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
}


def _utc_now() -> str:
    return (
        datetime.datetime.now(datetime.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def _is_present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (Mapping, Sequence)) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        return bool(value)
    return True


def _as_bool(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "yes", "1", "recorded", "preserved", "declared"}:
            return True
        if lowered in {"false", "no", "0", "missing", "blocked"}:
            return False
    return bool(value)


def _as_int(value: Any) -> int | None:
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return None
    return None


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            lowered = key_text.lower()
            if lowered in SENSITIVE_BODY_KEYS or lowered.endswith("_body"):
                sanitized[key_text] = "[bounded-result-boundary-redacted]"
            else:
                sanitized[key_text] = _sanitize(item)
        return sanitized
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str) and (
        "MUST_NOT_RETURN" in value
        or "RAW_FULL_PRIOR_ARTIFACT_BODY" in value
        or "HOSTILE_" in value
    ):
        return "[bounded-result-boundary-redacted]"
    return value


def _json_safe(value: Any) -> Any:
    return json.loads(json.dumps(_sanitize(value), sort_keys=True, default=str))


def _false_non_claims() -> dict[str, bool]:
    return {key: False for key in FALSE_NON_CLAIM_KEYS}


def _request_non_claims(request: Mapping[str, Any]) -> dict[str, bool]:
    non_claims = _false_non_claims()
    supplied = request.get("declared_non_claims")
    if isinstance(supplied, Mapping):
        for key in FALSE_NON_CLAIM_KEYS:
            if key in supplied:
                non_claims[key] = _as_bool(supplied[key])
    return non_claims


def _negative_flag(request: Mapping[str, Any], key: str) -> bool:
    non_claims = request.get("declared_non_claims")
    if isinstance(non_claims, Mapping) and key in non_claims:
        return _as_bool(non_claims.get(key))
    return _as_bool(request.get(key))


def _basis_supplied(request: Mapping[str, Any], key: str) -> bool:
    return _is_present(request.get(key))


def _basis_value(request: Mapping[str, Any], key: str, fallback_key: str | None = None) -> Any:
    if key in request:
        return request.get(key)
    if fallback_key and fallback_key in request:
        return request.get(fallback_key)
    return None


def _selected_basis(
    request: Mapping[str, Any],
    basis_key: str,
    extra: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    supplied = _basis_value(request, basis_key)
    section: dict[str, Any] = {
        "basis_key": basis_key,
        "basis_declared": _is_present(supplied),
        "basis": _sanitize(supplied),
        "basis_role": "reference-shaped second-carrier-result-boundary basis only",
        "does_not_create_result": True,
        "does_not_create_success": True,
        "does_not_create_external_result": True,
        "does_not_create_cross_carrier_evidence": True,
        "does_not_create_source_transfer": True,
        "does_not_create_source_receipt": True,
        "does_not_create_reception_authorization": True,
        "does_not_create_source_authority_currentness_runtime_or_final_completion": True,
        "does_not_authorize_follow_on_work": True,
    }
    if extra:
        section.update(_sanitize(dict(extra)))
    return section


def _posture(
    request: Mapping[str, Any],
    key: str,
    expected: str,
    default_declared: bool = False,
) -> dict[str, Any]:
    value = request.get(key)
    declared = _as_bool(value, default=default_declared)
    return {
        "posture_key": key,
        "declared": declared,
        "expected_posture": expected,
        "actual_posture": _sanitize(value),
        "posture_role": "second-carrier-result-boundary posture only",
    }


def _check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    code: str,
) -> dict[str, Any]:
    code_key = "block_code" if not passed else "failure_code"
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": _sanitize(actual_posture),
        code_key: None if passed else code,
    }


def _scope_values(request: Mapping[str, Any]) -> list[str]:
    supplied = request.get("second_carrier_result_boundary_scope")
    if supplied is None:
        return []
    if isinstance(supplied, str):
        return [supplied]
    if isinstance(supplied, Sequence) and not isinstance(
        supplied, (str, bytes, bytearray)
    ):
        return [str(item) for item in supplied]
    return [str(supplied)]


def _unsupported_scope_values(request: Mapping[str, Any]) -> list[str]:
    return [
        value
        for value in _scope_values(request)
        if value not in SUPPORTED_SCOPE_VALUES
    ]


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    question = request.get("second_carrier_result_boundary_question")
    intent = request.get("second_carrier_result_boundary_intent")
    unsupported_scope = _unsupported_scope_values(request)
    output_capture_failed_count = _as_int(
        request.get("selected_second_carrier_output_capture_failed_check_count")
    )

    def add(name: str, passed: bool, expected: str, actual: Any, code: str) -> None:
        checks.append(_check(name, passed, expected, actual, code))

    add(
        "second_carrier_result_boundary_question_declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "SECOND_CARRIER_RESULT_BOUNDARY_QUESTION_UNDECLARED",
    )
    add(
        "second_carrier_result_boundary_intent_supported",
        intent in SUPPORTED_INTENTS,
        "supported second-carrier-result-boundary intent",
        intent,
        "SECOND_CARRIER_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
    )
    add(
        "second_carrier_result_boundary_scope_supported",
        not unsupported_scope,
        "only supported second-carrier result boundary scope values",
        unsupported_scope,
        "UNSUPPORTED_SECOND_CARRIER_RESULT_BOUNDARY_SCOPE",
    )
    add(
        "returned_capture_intake_basis_declared",
        _basis_supplied(request, "selected_returned_second_carrier_live_capture_intake_basis")
        or _is_present(request.get("selected_returned_capture_intake_path")),
        "returned capture intake basis declared",
        request.get("selected_returned_second_carrier_live_capture_intake_basis"),
        "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    )
    add(
        "returned_capture_intake_preserved",
        _as_bool(request.get("selected_returned_capture_intake_preserved")),
        "returned capture intake preserved",
        request.get("selected_returned_capture_intake_preserved"),
        "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    )
    add(
        "returned_capture_intake_capture_only",
        _as_bool(request.get("selected_returned_capture_intake_capture_only")),
        "returned capture intake says capture-only",
        request.get("selected_returned_capture_intake_capture_only"),
        "RETURNED_CAPTURE_TREATED_AS_RESULT",
    )
    add(
        "returned_capture_records_macbook_pro_to_macbook_air",
        _as_bool(request.get("selected_returned_capture_from_macbook_pro_to_macbook_air")),
        "returned capture records MacBook Pro to MacBook Air return",
        request.get("selected_returned_capture_from_macbook_pro_to_macbook_air"),
        "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    )
    add(
        "returned_zip_path_present",
        _is_present(request.get("selected_returned_capture_zip_path"))
        or _basis_supplied(request, "selected_returned_zip_basis"),
        "returned zip path basis present",
        request.get("selected_returned_capture_zip_path"),
        "RETURNED_ZIP_PATH_MISSING",
    )
    add(
        "returned_hash_path_present",
        _is_present(request.get("selected_returned_capture_hash_path"))
        or _basis_supplied(request, "selected_returned_hash_basis"),
        "returned hash path basis present",
        request.get("selected_returned_capture_hash_path"),
        "RETURNED_HASH_PATH_MISSING",
    )
    add(
        "returned_extracted_directory_path_present",
        _is_present(request.get("selected_returned_capture_extracted_directory_path"))
        or _basis_supplied(request, "selected_returned_extracted_files_basis"),
        "returned extracted directory basis present",
        request.get("selected_returned_capture_extracted_directory_path"),
        "RETURNED_EXTRACTED_DIRECTORY_MISSING",
    )
    add(
        "returned_combined_terminal_log_path_present",
        _is_present(request.get("selected_returned_capture_combined_terminal_log_path"))
        or _basis_supplied(request, "selected_returned_combined_terminal_log_basis"),
        "returned combined terminal log basis present",
        request.get("selected_returned_capture_combined_terminal_log_path"),
        "RETURNED_COMBINED_TERMINAL_LOG_MISSING",
    )
    add(
        "returned_exit_code_present",
        request.get("selected_returned_capture_exit_code") is not None
        or _basis_supplied(request, "selected_returned_exit_code_basis"),
        "returned exit code basis present",
        request.get("selected_returned_capture_exit_code"),
        "RETURNED_EXIT_CODE_MISSING",
    )
    add(
        "returned_command_text_present",
        _is_present(request.get("selected_returned_capture_command_text"))
        or _basis_supplied(request, "selected_returned_command_text_basis"),
        "returned command text basis present",
        request.get("selected_returned_capture_command_text"),
        "RETURNED_COMMAND_TEXT_MISSING",
    )
    add(
        "returned_timestamps_present",
        _is_present(request.get("selected_returned_capture_started_at"))
        and _is_present(request.get("selected_returned_capture_completed_at")),
        "returned started and completed timestamps present",
        {
            "run_started_at": request.get("selected_returned_capture_started_at"),
            "run_completed_at": request.get("selected_returned_capture_completed_at"),
        },
        "RETURNED_TIMESTAMPS_MISSING",
    )
    add(
        "returned_command_captured",
        _is_present(request.get("selected_returned_capture_command_text")),
        "returned command captured",
        request.get("selected_returned_capture_command_text"),
        "RETURNED_COMMAND_TEXT_MISSING",
    )
    add(
        "returned_working_directory_captured",
        _is_present(request.get("selected_returned_capture_working_directory")),
        "returned working directory captured",
        request.get("selected_returned_capture_working_directory"),
        "RETURNED_CAPTURE_MATERIAL_MISSING",
    )
    add(
        "returned_exit_code_zero_preserved_as_capture_only",
        str(request.get("selected_returned_capture_exit_code")) == "0",
        "exit code 0 preserved as capture-only material",
        request.get("selected_returned_capture_exit_code"),
        "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
    )
    add(
        "returned_ran_7_tests_line_preserved_as_capture_only",
        "Ran 7 tests" in str(request.get("selected_returned_capture_ran_7_tests_line", "")),
        "Ran 7 tests line preserved as capture-only material",
        request.get("selected_returned_capture_ran_7_tests_line"),
        "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    )
    add(
        "returned_ok_line_preserved_as_capture_only",
        str(request.get("selected_returned_capture_ok_line", "")).strip() == "OK",
        "OK line preserved as capture-only material",
        request.get("selected_returned_capture_ok_line"),
        "OK_OUTPUT_TREATED_AS_VERIFICATION",
    )
    add(
        "raw_placeholder_carrier_fields_preserved",
        _is_present(request.get("selected_returned_capture_raw_placeholder_carrier_label"))
        and _is_present(request.get("selected_returned_capture_raw_placeholder_carrier_type")),
        "raw placeholder carrier fields preserved",
        {
            "carrier_label": request.get(
                "selected_returned_capture_raw_placeholder_carrier_label"
            ),
            "carrier_type": request.get(
                "selected_returned_capture_raw_placeholder_carrier_type"
            ),
        },
        "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
    )
    add(
        "placeholder_carrier_fields_unrepaired",
        _as_bool(request.get("selected_returned_capture_placeholder_fields_unrepaired")),
        "placeholder carrier fields are unrepaired raw-capture facts",
        request.get("selected_returned_capture_placeholder_fields_unrepaired"),
        "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
    )
    add(
        "zero_exit_code_not_success",
        _as_bool(request.get("selected_returned_capture_zero_exit_code_not_success"))
        and not _negative_flag(request, "zero_exit_code_treated_as_success"),
        "zero exit code is not success",
        {
            "not_success": request.get(
                "selected_returned_capture_zero_exit_code_not_success"
            ),
            "treated_as_success": _negative_flag(
                request, "zero_exit_code_treated_as_success"
            ),
        },
        "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
    )
    add(
        "ok_output_not_verification",
        _as_bool(request.get("selected_returned_capture_ok_not_verification"))
        and not _negative_flag(request, "ok_output_treated_as_verification"),
        "OK is not verification",
        {
            "ok_not_verification": request.get(
                "selected_returned_capture_ok_not_verification"
            ),
            "treated_as_verification": _negative_flag(
                request, "ok_output_treated_as_verification"
            ),
        },
        "OK_OUTPUT_TREATED_AS_VERIFICATION",
    )
    add(
        "returned_capture_not_cross_carrier_proof",
        _as_bool(request.get("selected_returned_capture_not_cross_carrier_proof"))
        and not _negative_flag(request, "returned_capture_treated_as_cross_carrier_evidence"),
        "returned capture is not cross-carrier proof",
        {
            "not_cross_carrier_proof": request.get(
                "selected_returned_capture_not_cross_carrier_proof"
            ),
            "treated_as_cross_carrier_evidence": _negative_flag(
                request, "returned_capture_treated_as_cross_carrier_evidence"
            ),
        },
        "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    )
    add(
        "actual_live_capture_packet_basis_declared",
        _basis_supplied(request, "selected_actual_second_carrier_live_capture_packet_basis"),
        "actual second-carrier live capture packet basis declared",
        request.get("selected_actual_second_carrier_live_capture_packet_basis"),
        "RETURNED_CAPTURE_MATERIAL_MISSING",
    )
    add(
        "actual_live_runbook_basis_declared",
        _basis_supplied(request, "selected_actual_second_carrier_live_runbook_basis"),
        "actual second-carrier live runbook basis declared",
        request.get("selected_actual_second_carrier_live_runbook_basis"),
        "RETURNED_CAPTURE_MATERIAL_MISSING",
    )
    add(
        "second_carrier_output_capture_basis_declared",
        _basis_supplied(request, "selected_second_carrier_output_capture_basis")
        or _is_present(request.get("selected_second_carrier_output_capture_result_path")),
        "second-carrier output capture basis declared",
        request.get("selected_second_carrier_output_capture_basis"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
    )
    add(
        "second_carrier_output_capture_recorded",
        request.get("selected_second_carrier_output_capture_result_outcome")
        == EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        request.get("selected_second_carrier_output_capture_result_outcome"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
    )
    add(
        "second_carrier_output_capture_failed_checks_zero",
        output_capture_failed_count == 0,
        "second-carrier output capture failed check count is zero",
        request.get("selected_second_carrier_output_capture_failed_check_count"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
    )
    add(
        "second_carrier_output_capture_recorded_bounded_capture",
        _as_bool(
            request.get("selected_second_carrier_output_capture_bounded_capture_recorded")
        ),
        "second-carrier output capture recorded bounded capture",
        request.get("selected_second_carrier_output_capture_bounded_capture_recorded"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_DID_NOT_RECORD_BOUNDED_CAPTURE",
    )
    add(
        "second_carrier_output_capture_not_result",
        not _as_bool(
            request.get("selected_second_carrier_output_capture_treated_capture_as_result")
        ),
        "second-carrier output capture did not treat capture as result",
        request.get("selected_second_carrier_output_capture_treated_capture_as_result"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_RESULT",
    )
    add(
        "second_carrier_output_capture_not_success",
        not _as_bool(
            request.get("selected_second_carrier_output_capture_treated_capture_as_success")
        ),
        "second-carrier output capture did not treat capture as success",
        request.get("selected_second_carrier_output_capture_treated_capture_as_success"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_SUCCESS",
    )
    add(
        "second_carrier_output_capture_not_external_result",
        not _as_bool(
            request.get(
                "selected_second_carrier_output_capture_treated_capture_as_external_result"
            )
        ),
        "second-carrier output capture did not treat capture as external result",
        request.get(
            "selected_second_carrier_output_capture_treated_capture_as_external_result"
        ),
        "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_EXTERNAL_RESULT",
    )
    add(
        "second_carrier_output_capture_not_cross_carrier_evidence",
        not _as_bool(
            request.get(
                "selected_second_carrier_output_capture_treated_capture_as_cross_carrier_evidence"
            )
        ),
        "second-carrier output capture did not treat capture as cross-carrier evidence",
        request.get(
            "selected_second_carrier_output_capture_treated_capture_as_cross_carrier_evidence"
        ),
        "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
    )

    grouped_basis = {
        "packet_transfer_basis_declared": (
            "selected_packet_transfer_basis",
            "packet transfer basis declared",
        ),
        "packet_emission_basis_declared": (
            "selected_packet_emission_basis",
            "packet emission basis declared",
        ),
        "command_success_basis_declared": (
            "selected_command_success_basis",
            "command success basis declared",
        ),
        "command_result_v2_basis_declared": (
            "selected_command_result_v2_basis",
            "command result v2 basis declared",
        ),
        "output_capture_v2_basis_declared": (
            "selected_output_capture_v2_basis",
            "output capture v2 basis declared",
        ),
        "command_output_report_artifact_basis_declared": (
            "selected_command_output_report_artifact_basis",
            "command output report artifact basis declared",
        ),
        "evidence_manifest_basis_declared": (
            "selected_evidence_manifest_basis",
            "evidence manifest basis declared",
        ),
        "artifact_containment_basis_declared": (
            "selected_artifact_containment_basis",
            "artifact containment basis declared",
        ),
        "portable_verification_basis_declared": (
            "selected_portable_verification_basis",
            "portable verification basis declared",
        ),
    }
    for check_name, (basis_key, expected) in grouped_basis.items():
        add(
            check_name,
            _basis_supplied(request, basis_key),
            expected,
            request.get(basis_key),
            "RETURNED_CAPTURE_MATERIAL_MISSING",
        )

    add(
        "predecessor_failure_visible_and_unrepaired",
        _basis_supplied(request, "selected_packet_emission_boundary_v1_predecessor_failure_basis")
        and _basis_supplied(request, "selected_predecessor_failure_basis")
        and not _negative_flag(request, "v1_repaired")
        and not _negative_flag(request, "v1_hidden")
        and not _negative_flag(request, "v1_claimed_passed"),
        "v1 predecessor failure visible, unrepaired, and not claimed passed",
        {
            "v1_basis": request.get(
                "selected_packet_emission_boundary_v1_predecessor_failure_basis"
            ),
            "predecessor_failure_basis": request.get("selected_predecessor_failure_basis"),
            "v1_repaired": _negative_flag(request, "v1_repaired"),
            "v1_hidden": _negative_flag(request, "v1_hidden"),
            "v1_claimed_passed": _negative_flag(request, "v1_claimed_passed"),
        },
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )

    posture_expectations = {
        "second_carrier_result_boundary_only_posture": (
            "second-carrier-result-boundary-only posture declared",
            "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_RESULT",
        ),
        "one_future_second_carrier_result_step_posture": (
            "one future second-carrier result step posture declared",
            "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
        ),
        "returned_second_carrier_capture_basis_preserved_posture": (
            "returned second-carrier capture basis preserved posture declared",
            "RETURNED_CAPTURE_MATERIAL_MISSING",
        ),
        "capture_intake_basis_preserved_posture": (
            "capture intake basis preserved posture declared",
            "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
        ),
        "second_carrier_output_capture_basis_preserved_posture": (
            "second-carrier output capture basis preserved posture declared",
            "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
        ),
        "capture_artifact_basis_preserved_posture": (
            "capture artifact basis preserved posture declared",
            "SECOND_CARRIER_OUTPUT_CAPTURE_DID_NOT_RECORD_BOUNDED_CAPTURE",
        ),
        "zero_exit_code_not_success_posture": (
            "zero-exit-code-not-success posture declared",
            "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
        ),
        "ok_output_not_verification_posture": (
            "OK-output-not-verification posture declared",
            "OK_OUTPUT_TREATED_AS_VERIFICATION",
        ),
        "returned_capture_not_cross_carrier_proof_posture": (
            "returned-capture-not-cross-carrier-proof posture declared",
            "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
        ),
        "result_not_created_posture": (
            "result-not-created posture declared",
            "SECOND_CARRIER_RESULT_CREATED",
        ),
        "second_carrier_success_not_created_posture": (
            "success-not-created posture declared",
            "SECOND_CARRIER_SUCCESS_CREATED",
        ),
        "external_result_not_created_posture": (
            "external-result-not-created posture declared",
            "EXTERNAL_RESULT_CREATED",
        ),
        "cross_carrier_evidence_not_created_posture": (
            "cross-carrier-evidence-not-created posture declared",
            "CROSS_CARRIER_EVIDENCE_CREATED",
        ),
        "result_not_source_transfer_posture": (
            "result-not-source-transfer posture declared",
            "SOURCE_TRANSFER_OCCURRED",
        ),
        "result_not_source_receipt_posture": (
            "result-not-source-receipt posture declared",
            "SOURCE_RECEIPT_OCCURRED",
        ),
        "result_not_reception_authorization_posture": (
            "result-not-reception-authorization posture declared",
            "RECEPTION_AUTHORIZATION_CREATED",
        ),
        "receiving_carrier_not_authority_posture": (
            "receiving-carrier-not-authority posture declared",
            "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
        ),
        "source_not_created_posture": (
            "source-not-created posture declared",
            "SOURCE_CREATED",
        ),
        "authority_not_created_posture": (
            "authority-not-created posture declared",
            "AUTHORITY_CREATED",
        ),
        "currentness_not_created_posture": (
            "currentness-not-created posture declared",
            "CURRENTNESS_CREATED",
        ),
        "final_completion_not_created_posture": (
            "final-completion-not-created posture declared",
            "FINAL_COMPLETION_CLAIMED",
        ),
        "runtime_not_created_posture": (
            "runtime-not-created posture declared",
            "RUNTIME_HOSTING_CREATED",
        ),
        "continuation_not_authorized_posture": (
            "continuation-not-authorized posture declared",
            "CONTINUATION_AUTHORIZED",
        ),
        "reusable_permission_not_created_posture": (
            "reusable-permission-not-created posture declared",
            "REUSABLE_PERMISSION_CREATED",
        ),
        "follow_on_work_not_authorized_posture": (
            "follow-on-work-not-authorized posture declared",
            "FOLLOW_ON_WORK_AUTHORIZED",
        ),
        "hidden_repo_state_excluded_posture": (
            "hidden repo state excluded posture declared",
            "HIDDEN_REPO_STATE_USED_AS_RESULT_AUTHORITY",
        ),
        "repo_local_availability_not_result_authority_posture": (
            "repo-local availability not result authority posture declared",
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_RESULT_AUTHORITY",
        ),
        "selected_basis_reference_shape_posture": (
            "selected basis reference-shaped posture declared",
            "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        ),
        "raw_full_prior_artifact_body_not_returned_posture": (
            "raw full prior artifact body not returned posture declared",
            "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        ),
    }
    for key, (expected, code) in posture_expectations.items():
        add(key, _as_bool(request.get(key)), expected, request.get(key), code)

    add(
        "hidden_repo_state_not_used_as_result_authority",
        not _negative_flag(request, "hidden_repo_state_used_as_result_authority"),
        "hidden repo state is not used as result authority",
        _negative_flag(request, "hidden_repo_state_used_as_result_authority"),
        "HIDDEN_REPO_STATE_USED_AS_RESULT_AUTHORITY",
    )
    add(
        "repo_local_availability_not_result_authority",
        not _negative_flag(request, "repo_local_availability_treated_as_result_authority"),
        "repo-local availability is not result authority",
        _negative_flag(request, "repo_local_availability_treated_as_result_authority"),
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_RESULT_AUTHORITY",
    )
    add(
        "selected_basis_reference_shaped",
        _as_bool(request.get("reference_shaped_input_posture"), default=True),
        "selected basis remains reference-shaped",
        request.get("reference_shaped_input_posture"),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    add(
        "raw_full_prior_artifact_body_not_returned",
        not _negative_flag(request, "raw_full_prior_artifact_body_returned"),
        "raw full prior artifact body not returned",
        _negative_flag(request, "raw_full_prior_artifact_body_returned"),
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    )
    add(
        "consumed_request_token_remains_closed",
        not _negative_flag(request, "consumed_request_reopened"),
        "consumed request token remains closed",
        _negative_flag(request, "consumed_request_reopened"),
        "CONSUMED_REQUEST_REOPENED",
    )
    add(
        "authorization_token_reuse_blocked",
        not _negative_flag(request, "authorization_token_reused"),
        "authorization token reuse remains blocked",
        _negative_flag(request, "authorization_token_reused"),
        "AUTHORIZATION_TOKEN_REUSED",
    )

    supplied_non_claims = request.get("declared_non_claims")
    non_claims = _request_non_claims(request)
    bad_non_claims = [
        key
        for key in FALSE_NON_CLAIM_KEYS
        if key not in non_claims or non_claims[key] is not False
    ]
    add(
        "required_non_claims_false",
        isinstance(supplied_non_claims, Mapping) and not bad_non_claims,
        "required non-claims are explicit and false",
        {"bad_non_claims": bad_non_claims},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    collapse_checks = {
        "returned_capture_not_treated_as_result": (
            "returned_capture_treated_as_result",
            "RETURNED_CAPTURE_TREATED_AS_RESULT",
        ),
        "returned_capture_not_treated_as_success": (
            "returned_capture_treated_as_success",
            "RETURNED_CAPTURE_TREATED_AS_SUCCESS",
        ),
        "returned_capture_not_treated_as_verification": (
            "returned_capture_treated_as_verification",
            "RETURNED_CAPTURE_TREATED_AS_VERIFICATION",
        ),
        "result_boundary_not_treated_as_result": (
            "second_carrier_result_boundary_treated_as_result",
            "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_RESULT",
        ),
        "result_boundary_not_treated_as_success": (
            "second_carrier_result_boundary_treated_as_success",
            "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_SUCCESS",
        ),
        "result_boundary_not_treated_as_external_result": (
            "second_carrier_result_boundary_treated_as_external_result",
            "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
        ),
        "result_boundary_not_treated_as_cross_carrier_evidence": (
            "second_carrier_result_boundary_treated_as_cross_carrier_evidence",
            "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
        ),
        "second_carrier_result_not_created": (
            "second_carrier_result_created",
            "SECOND_CARRIER_RESULT_CREATED",
        ),
        "second_carrier_success_not_created": (
            "second_carrier_success_created",
            "SECOND_CARRIER_SUCCESS_CREATED",
        ),
        "external_result_not_created": (
            "external_result_created",
            "EXTERNAL_RESULT_CREATED",
        ),
        "cross_carrier_evidence_not_created": (
            "cross_carrier_evidence_created",
            "CROSS_CARRIER_EVIDENCE_CREATED",
        ),
        "artifacts_not_mutated": ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
    }
    for name, (flag, code) in collapse_checks.items():
        add(
            name,
            not _negative_flag(request, flag),
            f"{flag} remains false",
            _negative_flag(request, flag),
            code,
        )

    return checks


def _failed_checks(checks: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [check for check in checks if not _as_bool(check.get("passed"))]


def _first_failure_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if not _as_bool(check.get("passed")):
            code = check.get("block_code") or check.get("failure_code")
            return str(code) if code else None
    return None


def _statement(recorded: bool) -> dict[str, bool]:
    statement = {key: True for key in TRUE_STATEMENT_KEYS}
    if not recorded:
        statement["second_carrier_result_boundary_recorded"] = False
        statement["one_future_second_carrier_result_step_declared"] = False
        statement["returned_second_carrier_capture_basis_preserved"] = False
        statement["capture_intake_basis_preserved"] = False
        statement["second_carrier_output_capture_basis_preserved"] = False
        statement["capture_artifact_basis_preserved"] = False
    return statement


def _non_meaning() -> dict[str, bool]:
    keys = (
        "second_carrier_result_exists",
        "second_carrier_success_exists",
        "external_result_exists",
        "cross_carrier_evidence_exists",
        "verification_has_occurred",
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
        "result_boundary_became_result",
        "result_boundary_became_success",
        "result_boundary_became_external_result",
        "result_boundary_became_cross_carrier_proof",
        "result_boundary_became_source_transfer_source_receipt_reception_authorization",
        "result_boundary_became_source_authority_currentness",
        "returned_capture_became_result",
        "zero_exit_code_became_success",
        "ok_became_verification",
        "ran_7_tests_became_cross_carrier_proof",
        "macbook_pro_became_authority",
        "macbook_air_became_source",
        "artifact_existence_became_result_authority",
        "artifact_path_became_currentness",
        "repo_local_availability_became_result_authority",
        "hidden_repo_state_became_result_authority",
        "v1_packet_emission_boundary_resolver_repaired_hidden_erased_or_claimed_passed",
    )
    return {key: False for key in keys}


def _additional_basis_required(
    request: Mapping[str, Any], outcome: str, failed: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    additional_context = _sanitize(request.get("additional_basis_context"))
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": required,
        "additional_basis_context": additional_context if required else None,
        "missing_or_unclear_basis": (
            [
                {
                    "check_name": check.get("check_name"),
                    "block_code": check.get("block_code") or check.get("failure_code"),
                    "actual_posture": check.get("actual_posture"),
                }
                for check in failed
            ]
            if required
            else []
        ),
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
    }


def _not_recorded_basis(
    request: Mapping[str, Any], outcome: str, failed: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    return {
        "not_recorded": not_recorded,
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis"))
        if not_recorded
        else None,
        "failed_review_reasons": (
            [
                {
                    "check_name": check.get("check_name"),
                    "failure_code": check.get("block_code") or check.get("failure_code"),
                }
                for check in failed
            ]
            if not_recorded
            else []
        ),
        "result_created": False,
        "success_created": False,
        "external_result_created": False,
        "cross_carrier_evidence_created": False,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_created": False,
        "runtime_created": False,
        "follow_on_work_authorized": False,
        "prior_artifacts_mutated": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "second-carrier result boundary test",
            "second-carrier result boundary live artifact",
            "second-carrier result boundary terminal summary, if needed",
            "second-carrier result spec/resolver/test/live artifact",
            "second-carrier success",
            "external result artifact",
            "cross-carrier evidence review",
            "line-level portable verification closure review",
            "source transfer",
            "source receipt",
            "reception authorization",
            "derivative reception",
            "vessel relation",
            "adoption",
            "authority creation",
            "currentness creation",
            "operation permission",
            "receiving-context governance",
            "final completion",
            "runtime hosting",
            "deployment",
            "public release",
            "continuation",
            "publication flow",
            "reusable permission",
            "successor reception request",
            "follow-on work",
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _block(code: str | None, reason: str | None = None) -> dict[str, Any] | None:
    if not code:
        return None
    return {
        "blocked": True,
        "block_code": code,
        "block_reason": reason or code,
    }


def _result_id(request: Mapping[str, Any]) -> str:
    request_id = request.get("second_carrier_result_boundary_request_id")
    if _is_present(request_id):
        return str(request_id)
    return "portable_source_body_verification_second_carrier_result_boundary_request"


def _selected_basis_sections(request: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    sections = {key: _selected_basis(request, key) for key in SELECTED_BASIS_KEYS}
    sections["selected_returned_second_carrier_live_capture_intake_basis"].update(
        {
            "selected_returned_capture_intake_path": _sanitize(
                request.get("selected_returned_capture_intake_path")
            ),
            "selected_returned_capture_intake_preserved": _as_bool(
                request.get("selected_returned_capture_intake_preserved")
            ),
            "selected_returned_capture_intake_capture_only": _as_bool(
                request.get("selected_returned_capture_intake_capture_only")
            ),
            "selected_returned_capture_from_macbook_pro_to_macbook_air": _as_bool(
                request.get("selected_returned_capture_from_macbook_pro_to_macbook_air")
            ),
        }
    )
    sections["selected_returned_capture_material_basis"].update(
        {
            "selected_returned_capture_stdout_path": _sanitize(
                request.get("selected_returned_capture_stdout_path")
            ),
            "selected_returned_capture_stderr_path": _sanitize(
                request.get("selected_returned_capture_stderr_path")
            ),
            "selected_returned_capture_working_directory": _sanitize(
                request.get("selected_returned_capture_working_directory")
            ),
            "selected_returned_capture_exit_code": _sanitize(
                request.get("selected_returned_capture_exit_code")
            ),
            "selected_returned_capture_ran_7_tests_line": _sanitize(
                request.get("selected_returned_capture_ran_7_tests_line")
            ),
            "selected_returned_capture_ok_line": _sanitize(
                request.get("selected_returned_capture_ok_line")
            ),
            "raw_placeholder_carrier_label": _sanitize(
                request.get("selected_returned_capture_raw_placeholder_carrier_label")
            ),
            "raw_placeholder_carrier_type": _sanitize(
                request.get("selected_returned_capture_raw_placeholder_carrier_type")
            ),
            "placeholder_fields_unrepaired": _as_bool(
                request.get("selected_returned_capture_placeholder_fields_unrepaired")
            ),
            "zero_exit_code_not_success": _as_bool(
                request.get("selected_returned_capture_zero_exit_code_not_success")
            ),
            "ok_not_verification": _as_bool(
                request.get("selected_returned_capture_ok_not_verification")
            ),
            "returned_capture_not_cross_carrier_proof": _as_bool(
                request.get("selected_returned_capture_not_cross_carrier_proof")
            ),
        }
    )
    sections["selected_returned_zip_basis"].update(
        {"selected_returned_capture_zip_path": _sanitize(request.get("selected_returned_capture_zip_path"))}
    )
    sections["selected_returned_hash_basis"].update(
        {"selected_returned_capture_hash_path": _sanitize(request.get("selected_returned_capture_hash_path"))}
    )
    sections["selected_returned_extracted_files_basis"].update(
        {
            "selected_returned_capture_extracted_directory_path": _sanitize(
                request.get("selected_returned_capture_extracted_directory_path")
            )
        }
    )
    sections["selected_returned_combined_terminal_log_basis"].update(
        {
            "selected_returned_capture_combined_terminal_log_path": _sanitize(
                request.get("selected_returned_capture_combined_terminal_log_path")
            )
        }
    )
    sections["selected_returned_exit_code_basis"].update(
        {"selected_returned_capture_exit_code": _sanitize(request.get("selected_returned_capture_exit_code"))}
    )
    sections["selected_returned_command_text_basis"].update(
        {"selected_returned_capture_command_text": _sanitize(request.get("selected_returned_capture_command_text"))}
    )
    sections["selected_returned_timestamps_basis"].update(
        {
            "selected_returned_capture_started_at": _sanitize(
                request.get("selected_returned_capture_started_at")
            ),
            "selected_returned_capture_completed_at": _sanitize(
                request.get("selected_returned_capture_completed_at")
            ),
        }
    )
    sections["selected_second_carrier_output_capture_basis"].update(
        {
            "selected_second_carrier_output_capture_result_path": _sanitize(
                request.get("selected_second_carrier_output_capture_result_path")
            ),
            "selected_second_carrier_output_capture_result_outcome": _sanitize(
                request.get("selected_second_carrier_output_capture_result_outcome")
            ),
            "selected_second_carrier_output_capture_failed_check_count": _sanitize(
                request.get("selected_second_carrier_output_capture_failed_check_count")
            ),
            "selected_second_carrier_output_capture_bounded_capture_recorded": _as_bool(
                request.get("selected_second_carrier_output_capture_bounded_capture_recorded")
            ),
            "capture_not_result": not _as_bool(
                request.get("selected_second_carrier_output_capture_treated_capture_as_result")
            ),
            "capture_not_success": not _as_bool(
                request.get("selected_second_carrier_output_capture_treated_capture_as_success")
            ),
            "capture_not_external_result": not _as_bool(
                request.get(
                    "selected_second_carrier_output_capture_treated_capture_as_external_result"
                )
            ),
            "capture_not_cross_carrier_evidence": not _as_bool(
                request.get(
                    "selected_second_carrier_output_capture_treated_capture_as_cross_carrier_evidence"
                )
            ),
        }
    )
    return sections


def _posture_sections(request: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    expected = {
        "second_carrier_result_boundary_only_posture": "boundary only; not result",
        "one_future_second_carrier_result_step_posture": "one future result step only",
        "returned_second_carrier_capture_basis_preserved_posture": "returned capture basis preserved",
        "capture_intake_basis_preserved_posture": "capture intake basis preserved",
        "second_carrier_output_capture_basis_preserved_posture": "output capture basis preserved",
        "capture_artifact_basis_preserved_posture": "capture artifact basis preserved",
        "zero_exit_code_not_success_posture": "zero exit code is not success",
        "ok_output_not_verification_posture": "OK output is not verification",
        "returned_capture_not_cross_carrier_proof_posture": "returned capture is not cross-carrier proof",
        "result_not_created_posture": "second-carrier result not created",
        "second_carrier_success_not_created_posture": "second-carrier success not created",
        "external_result_not_created_posture": "external result not created",
        "cross_carrier_evidence_not_created_posture": "cross-carrier evidence not created",
        "result_not_source_transfer_posture": "result boundary is not source transfer",
        "result_not_source_receipt_posture": "result boundary is not source receipt",
        "result_not_reception_authorization_posture": "result boundary is not reception authorization",
        "receiving_carrier_not_authority_posture": "receiving carrier is not authority",
        "source_not_created_posture": "source not created",
        "authority_not_created_posture": "authority not created",
        "currentness_not_created_posture": "currentness not created",
        "final_completion_not_created_posture": "final completion not created",
        "runtime_not_created_posture": "runtime not created",
        "continuation_not_authorized_posture": "continuation not authorized",
        "reusable_permission_not_created_posture": "reusable permission not created",
        "follow_on_work_not_authorized_posture": "follow-on work not authorized",
        "hidden_repo_state_excluded_posture": "hidden repo state excluded",
        "repo_local_availability_not_result_authority_posture": "repo-local availability is not result authority",
        "selected_basis_reference_shape_posture": "selected basis remains reference-shaped",
        "raw_full_prior_artifact_body_not_returned_posture": "raw full prior artifact body not returned",
    }
    return {key: _posture(request, key, expected[key]) for key in POSTURE_KEYS}


def _determine_outcome(
    request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]
) -> tuple[str, dict[str, Any] | None]:
    intent = request.get("second_carrier_result_boundary_intent")
    requested = request.get("requested_second_carrier_result_boundary_outcome")
    failed = _failed_checks(checks)

    if intent == INTENT_BLOCK:
        return OUTCOME_BLOCKED, _block(
            "SECOND_CARRIER_RESULT_BOUNDARY_BLOCK_REQUESTED",
            _sanitize(request.get("block_reason")) or "block requested",
        )
    if intent not in SUPPORTED_INTENTS:
        return OUTCOME_BLOCKED, _block(
            "SECOND_CARRIER_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
            "unsupported second-carrier result boundary intent",
        )
    if failed:
        code = _first_failure_code(checks) or "DECLARED_SECOND_CARRIER_RESULT_BOUNDARY_REQUEST_MALFORMED"
        return OUTCOME_BLOCKED, _block(code, "second-carrier result boundary check failed")
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or _is_present(
        request.get("additional_basis_context")
    ):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None
    if intent == INTENT_DO_NOT_RECORD or requested == OUTCOME_NOT_RECORDED:
        return OUTCOME_NOT_RECORDED, None
    return OUTCOME_RECORDED, None


def _malformed_request_result(reason: str, code: str) -> dict[str, Any]:
    request = {
        "second_carrier_result_boundary_request_id": "malformed_second_carrier_result_boundary_request",
        "second_carrier_result_boundary_question": None,
        "second_carrier_result_boundary_intent": None,
        "declared_non_claims": _false_non_claims(),
    }
    checks = [
        _check(
            "declared_second_carrier_result_boundary_request_malformed",
            False,
            "declared request must be a JSON object / mapping",
            reason,
            code,
        )
    ]
    return _assemble_result(
        request=request,
        checks=checks,
        outcome=OUTCOME_BLOCKED,
        block=_block(code, reason),
    )


def _assemble_result(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block: dict[str, Any] | None,
) -> dict[str, Any]:
    failed = _failed_checks(checks)
    recorded = outcome == OUTCOME_RECORDED
    basis_sections = _selected_basis_sections(request)
    posture_sections = _posture_sections(request)
    statement = _statement(recorded)
    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_result_boundary_metadata": {
            "portable_source_body_verification_second_carrier_result_boundary_result_id": _result_id(
                request
            ),
            "portable_source_body_verification_second_carrier_result_boundary_result_type": RESULT_TYPE,
            "portable_source_body_verification_second_carrier_result_boundary_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_second_carrier_result_boundary_question": {
            "question": _sanitize(request.get("second_carrier_result_boundary_question")),
            "expected_question": CORE_QUESTION,
            "intent": _sanitize(request.get("second_carrier_result_boundary_intent")),
            "request_id": _result_id(request),
        },
        **basis_sections,
        **posture_sections,
        "second_carrier_result_boundary_scope": {
            "scope_values": _sanitize(_scope_values(request)),
            "supported_scope_values": sorted(SUPPORTED_SCOPE_VALUES),
            "unsupported_scope_values": _sanitize(_unsupported_scope_values(request)),
            "unsupported_scope_values_must_not_be_silently_accepted": True,
        },
        "second_carrier_result_boundary_checks": list(checks),
        "second_carrier_result_boundary_statement": statement,
        "second_carrier_result_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": _additional_basis_required(request, outcome, failed),
        "not_recorded_basis": _not_recorded_basis(request, outcome, failed),
        "what_remains_open": _what_remains_open(),
        "non_claims": _request_non_claims(request),
        "outcome": outcome,
        "block": block,
    }
    result[
        "portable_source_body_verification_second_carrier_result_boundary_summary"
    ] = build_portable_source_body_verification_second_carrier_result_boundary_summary(
        result
    )
    return _json_safe(result)


def resolve_portable_source_body_verification_second_carrier_result_boundary(
    declared_second_carrier_result_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded second-carrier result-boundary request."""

    if declared_second_carrier_result_boundary_request is None:
        return _malformed_request_result(
            "declared second-carrier result boundary request is missing",
            "DECLARED_SECOND_CARRIER_RESULT_BOUNDARY_REQUEST_MALFORMED",
        )
    if not isinstance(declared_second_carrier_result_boundary_request, Mapping):
        return _malformed_request_result(
            "declared second-carrier result boundary request must be a mapping",
            "DECLARED_SECOND_CARRIER_RESULT_BOUNDARY_REQUEST_MALFORMED",
        )

    request = copy.deepcopy(dict(declared_second_carrier_result_boundary_request))
    request = _sanitize(request)
    checks = _build_checks(request)
    outcome, block = _determine_outcome(request, checks)
    return _assemble_result(request=request, checks=checks, outcome=outcome, block=block)


def resolve_portable_source_body_verification_second_carrier_result_boundary_from_path(
    declared_second_carrier_result_boundary_request_path: Path | str,
) -> dict:
    """Load a declared second-carrier result-boundary request from JSON."""

    path = Path(declared_second_carrier_result_boundary_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierResultBoundaryError(
            "DECLARED_SECOND_CARRIER_RESULT_BOUNDARY_REQUEST_UNREADABLE"
        ) from exc

    try:
        loaded = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierResultBoundaryError(
            "DECLARED_SECOND_CARRIER_RESULT_BOUNDARY_REQUEST_MALFORMED"
        ) from exc

    if not isinstance(loaded, Mapping):
        return _malformed_request_result(
            "declared request JSON must be an object",
            "DECLARED_SECOND_CARRIER_RESULT_BOUNDARY_REQUEST_MALFORMED",
        )
    return resolve_portable_source_body_verification_second_carrier_result_boundary(
        loaded
    )


def build_portable_source_body_verification_second_carrier_result_boundary_summary(
    result: Mapping[str, Any]
) -> dict:
    """Build a compact summary for a second-carrier result-boundary result."""

    metadata = result.get(
        "portable_source_body_verification_second_carrier_result_boundary_metadata",
        {},
    )
    question = result.get("declared_second_carrier_result_boundary_question", {})
    checks = result.get("second_carrier_result_boundary_checks", [])
    statement = result.get("second_carrier_result_boundary_statement", {})
    non_claims = result.get("non_claims", {})
    returned_basis = result.get("selected_returned_capture_material_basis", {})
    intake_basis = result.get(
        "selected_returned_second_carrier_live_capture_intake_basis", {}
    )
    zip_basis = result.get("selected_returned_zip_basis", {})
    hash_basis = result.get("selected_returned_hash_basis", {})
    extracted_basis = result.get("selected_returned_extracted_files_basis", {})
    output_capture_basis = result.get("selected_second_carrier_output_capture_basis", {})
    block = result.get("block") or {}

    passed_checks = sum(1 for check in checks if _as_bool(check.get("passed")))
    failed_checks = sum(1 for check in checks if not _as_bool(check.get("passed")))

    return _json_safe(
        {
            "outcome": result.get("outcome"),
            "block_code": block.get("block_code"),
            "block_reason": block.get("block_reason"),
            "request_id": metadata.get(
                "portable_source_body_verification_second_carrier_result_boundary_result_id"
            ),
            "question": question.get("question"),
            "intent": question.get("intent"),
            "passed_check_count": passed_checks,
            "failed_check_count": failed_checks,
            "second_carrier_result_boundary_recorded": statement.get(
                "second_carrier_result_boundary_recorded", False
            ),
            "one_future_second_carrier_result_step_declared": statement.get(
                "one_future_second_carrier_result_step_declared", False
            ),
            "returned_second_carrier_capture_basis_preserved": statement.get(
                "returned_second_carrier_capture_basis_preserved", False
            ),
            "capture_intake_basis_preserved": statement.get(
                "capture_intake_basis_preserved", False
            ),
            "second_carrier_output_capture_basis_preserved": statement.get(
                "second_carrier_output_capture_basis_preserved", False
            ),
            "capture_artifact_basis_preserved": statement.get(
                "capture_artifact_basis_preserved", False
            ),
            "zero_exit_code_not_success": statement.get(
                "zero_exit_code_not_success", False
            ),
            "ok_output_not_verification": statement.get(
                "ok_output_not_verification", False
            ),
            "returned_capture_not_cross_carrier_proof": statement.get(
                "returned_capture_not_cross_carrier_proof", False
            ),
            "result_not_created": statement.get("result_not_created", False),
            "second_carrier_success_not_created": statement.get(
                "second_carrier_success_not_created", False
            ),
            "external_result_not_created": statement.get(
                "external_result_not_created", False
            ),
            "cross_carrier_evidence_not_created": statement.get(
                "cross_carrier_evidence_not_created", False
            ),
            "result_not_source_transfer": statement.get(
                "result_not_source_transfer", False
            ),
            "result_not_source_receipt": statement.get(
                "result_not_source_receipt", False
            ),
            "result_not_reception_authorization": statement.get(
                "result_not_reception_authorization", False
            ),
            "receiving_carrier_not_authority": statement.get(
                "receiving_carrier_not_authority", False
            ),
            "source_not_created": statement.get("source_not_created", False),
            "authority_not_created": statement.get("authority_not_created", False),
            "currentness_not_created": statement.get("currentness_not_created", False),
            "final_completion_not_created": statement.get(
                "final_completion_not_created", False
            ),
            "runtime_not_created": statement.get("runtime_not_created", False),
            "follow_on_work_not_authorized": statement.get(
                "follow_on_work_not_authorized", False
            ),
            "hidden_repo_state_excluded": statement.get(
                "hidden_repo_state_excluded", False
            ),
            "hidden_repo_state_not_used_as_result_authority": statement.get(
                "hidden_repo_state_not_used_as_result_authority", False
            ),
            "repo_local_availability_not_result_authority": statement.get(
                "repo_local_availability_not_result_authority", False
            ),
            "selected_basis_reference_shape_preserved": statement.get(
                "selected_basis_reference_shape_preserved", False
            ),
            "raw_full_prior_artifact_body_not_returned": statement.get(
                "raw_full_prior_artifact_body_not_returned", False
            ),
            "selected_returned_capture_intake_path": intake_basis.get(
                "selected_returned_capture_intake_path"
            ),
            "selected_returned_capture_zip_path": zip_basis.get(
                "selected_returned_capture_zip_path"
            ),
            "selected_returned_capture_hash_path": hash_basis.get(
                "selected_returned_capture_hash_path"
            ),
            "selected_returned_capture_extracted_directory_path": extracted_basis.get(
                "selected_returned_capture_extracted_directory_path"
            ),
            "selected_returned_capture_exit_code": returned_basis.get(
                "selected_returned_capture_exit_code"
            ),
            "selected_returned_capture_ok_line": returned_basis.get(
                "selected_returned_capture_ok_line"
            ),
            "selected_second_carrier_output_capture_outcome": output_capture_basis.get(
                "selected_second_carrier_output_capture_result_outcome"
            ),
            "selected_second_carrier_output_capture_failed_check_count": output_capture_basis.get(
                "selected_second_carrier_output_capture_failed_check_count"
            ),
            "no_result_success_external_result_or_cross_carrier_evidence": (
                non_claims.get("second_carrier_result_created") is False
                and non_claims.get("second_carrier_success_created") is False
                and non_claims.get("external_result_created") is False
                and non_claims.get("cross_carrier_evidence_created") is False
            ),
            "no_source_authority_currentness_final_completion_or_runtime": (
                non_claims.get("source_created") is False
                and non_claims.get("authority_created") is False
                and non_claims.get("currentness_created") is False
                and non_claims.get("final_completion_claimed") is False
                and non_claims.get("runtime_hosting_created") is False
            ),
            "no_deployment_public_release_or_follow_on": (
                non_claims.get("deployment_created") is False
                and non_claims.get("public_release_created") is False
                and non_claims.get("follow_on_work_authorized") is False
            ),
            "key_non_claims": {
                "returned_capture_treated_as_result": non_claims.get(
                    "returned_capture_treated_as_result"
                ),
                "zero_exit_code_treated_as_success": non_claims.get(
                    "zero_exit_code_treated_as_success"
                ),
                "ok_output_treated_as_verification": non_claims.get(
                    "ok_output_treated_as_verification"
                ),
                "ran_7_tests_treated_as_cross_carrier_proof": non_claims.get(
                    "ran_7_tests_treated_as_cross_carrier_proof"
                ),
            },
            "v1_predecessor_failure_preserved": True,
            "v1_not_repaired": non_claims.get("v1_repaired") is False,
            "v1_not_hidden": non_claims.get("v1_hidden") is False,
            "v1_not_claimed_passed": non_claims.get("v1_claimed_passed") is False,
        }
    )


def _safe_filename_part(value: Any) -> str:
    text = str(value or "portable_source_body_verification_second_carrier_result_boundary_request")
    safe = []
    for char in text:
        if char.isalnum() or char in {"-", "_", "."}:
            safe.append(char)
        else:
            safe.append("_")
    return "".join(safe).strip("._") or "portable_source_body_verification_second_carrier_result_boundary_request"


def _available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    for index in range(1, 1000):
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
    raise PortableSourceBodyVerificationSecondCarrierResultBoundaryError(
        "unable to allocate non-overwriting second-carrier result-boundary output path"
    )


def write_portable_source_body_verification_second_carrier_result_boundary_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a bounded second-carrier result-boundary artifact without overwrite."""

    metadata = result.get(
        "portable_source_body_verification_second_carrier_result_boundary_metadata",
        {},
    )
    request_id = metadata.get(
        "portable_source_body_verification_second_carrier_result_boundary_result_id"
    )
    filename = (
        f"{_safe_filename_part(request_id)}__"
        "portable_source_body_verification_second_carrier_result_boundary_result.json"
    )
    destination = Path(output_path) if output_path is not None else OUTPUT_ROOT / filename
    if destination.exists():
        destination = _available_output_path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(_json_safe(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return destination


def build_declared_portable_source_body_verification_second_carrier_result_boundary_request(
    second_carrier_result_boundary_request_id: str = (
        "portable_source_body_verification_second_carrier_result_boundary_reference_review_001"
    ),
    **overrides: Any,
) -> dict:
    """Build a valid declared boundary request without inferring result or success."""

    returned_root = (
        "artifacts/actual_second_carrier_live_capture/"
        "portable_source_body_verification_actual_second_carrier_capture_001"
    )
    extracted_root = (
        f"{returned_root}/extracted/iammai_second_carrier_capture_001"
    )
    request: dict[str, Any] = {
        "second_carrier_result_boundary_request_id": second_carrier_result_boundary_request_id,
        "second_carrier_result_boundary_question": CORE_QUESTION,
        "second_carrier_result_boundary_intent": INTENT_RECORD,
        "selected_returned_second_carrier_live_capture_intake_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md",
            "basis_role": "returned real second-carrier live capture intake basis",
        },
        "selected_actual_second_carrier_live_capture_packet_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_ACTUAL_SECOND_CARRIER_LIVE_CAPTURE_PACKET_V0.md",
            "basis_role": "actual second-carrier live capture packet basis",
        },
        "selected_actual_second_carrier_live_runbook_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_ACTUAL_SECOND_CARRIER_LIVE_RUNBOOK_V0.md",
            "basis_role": "actual second-carrier live runbook basis",
        },
        "selected_returned_capture_material_basis": {
            "basis_role": "returned capture material basis only",
            "stdout_path": f"{extracted_root}/stdout.txt",
            "stderr_path": f"{extracted_root}/stderr.txt",
            "combined_terminal_log_path": f"{extracted_root}/combined_terminal_log.txt",
        },
        "selected_returned_zip_basis": {
            "path": f"{returned_root}/original_zip/iammai_second_carrier_capture_001.zip"
        },
        "selected_returned_hash_basis": {
            "path": f"{returned_root}/hashes/iammai_second_carrier_capture_001.sha256"
        },
        "selected_returned_extracted_files_basis": {"path": extracted_root},
        "selected_returned_combined_terminal_log_basis": {
            "path": f"{extracted_root}/combined_terminal_log.txt"
        },
        "selected_returned_exit_code_basis": {"exit_code": "0"},
        "selected_returned_command_text_basis": {
            "command_text": (
                "python3 -m unittest "
                "tests/test_resolve_portable_source_body_verification_"
                "second_carrier_output_capture.py"
            )
        },
        "selected_returned_timestamps_basis": {
            "run_started_at": "2026-05-09T11:34:26Z",
            "run_completed_at": "2026-05-09T11:34:27Z",
        },
        "selected_second_carrier_output_capture_basis": {
            "path": (
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
                "verification_second_carrier_output_capture/"
                "portable_source_body_verification_second_carrier_output_capture_"
                "reference_review_001__portable_source_body_verification_second_"
                "carrier_output_capture_result.json"
            ),
            "outcome": EXPECTED_OUTPUT_CAPTURE_OUTCOME,
            "failed_check_count": 0,
        },
        "selected_second_carrier_output_capture_terminal_summary_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_TERMINAL_SUMMARY_V0.md"
        },
        "selected_second_carrier_output_capture_boundary_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TERMINAL_SUMMARY_V0.md"
        },
        "selected_second_carrier_execution_output_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_TERMINAL_SUMMARY_V0.md"
        },
        "selected_second_carrier_execution_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_TERMINAL_SUMMARY_V0.md"
        },
        "selected_packet_transfer_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_TERMINAL_SUMMARY_V0.md"
        },
        "selected_packet_emission_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_TERMINAL_SUMMARY_V0.md"
        },
        "selected_packet_emission_boundary_v2_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_V2_TERMINAL_SUMMARY_V0.md"
        },
        "selected_packet_emission_boundary_v1_predecessor_failure_basis": {
            "path": "src/resolve_portable_source_body_verification_packet_emission_boundary.py",
            "preserved_failure_evidence": True,
        },
        "selected_packet_artifact_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_TERMINAL_SUMMARY_V0.md"
        },
        "selected_command_success_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_TERMINAL_SUMMARY_V0.md"
        },
        "selected_command_result_v2_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_V2_TERMINAL_SUMMARY_V0.md"
        },
        "selected_output_capture_v2_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_V2_TERMINAL_SUMMARY_V0.md"
        },
        "selected_command_output_report_artifact_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_TERMINAL_SUMMARY_V0.md"
        },
        "selected_command_execution_basis": {
            "path": "src/resolve_portable_source_body_verification_second_carrier_execution.py"
        },
        "selected_command_report_lineage_basis": {
            "basis_role": "command report lineage only; not current report artifact"
        },
        "selected_predecessor_failure_basis": {
            "path": "tests/test_resolve_portable_source_body_verification_packet_emission_boundary.py",
            "preserved_failure_evidence": True,
        },
        "selected_evidence_manifest_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_TERMINAL_SUMMARY_V0.md"
        },
        "selected_artifact_containment_basis": {
            "basis_role": "artifact containment basis only"
        },
        "selected_portable_verification_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
        },
        "selected_returned_capture_intake_path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md",
        "selected_returned_capture_intake_preserved": True,
        "selected_returned_capture_intake_capture_only": True,
        "selected_returned_capture_from_macbook_pro_to_macbook_air": True,
        "selected_returned_capture_zip_path": f"{returned_root}/original_zip/iammai_second_carrier_capture_001.zip",
        "selected_returned_capture_hash_path": f"{returned_root}/hashes/iammai_second_carrier_capture_001.sha256",
        "selected_returned_capture_extracted_directory_path": extracted_root,
        "selected_returned_capture_combined_terminal_log_path": f"{extracted_root}/combined_terminal_log.txt",
        "selected_returned_capture_stdout_path": f"{extracted_root}/stdout.txt",
        "selected_returned_capture_stderr_path": f"{extracted_root}/stderr.txt",
        "selected_returned_capture_command_text": (
            "python3 -m unittest "
            "tests/test_resolve_portable_source_body_verification_second_carrier_output_capture.py"
        ),
        "selected_returned_capture_working_directory": "/Users/markomarkota/Desktop/IAMMAI-SYSTEM",
        "selected_returned_capture_started_at": "2026-05-09T11:34:26Z",
        "selected_returned_capture_completed_at": "2026-05-09T11:34:27Z",
        "selected_returned_capture_exit_code": "0",
        "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
        "selected_returned_capture_ok_line": "OK",
        "selected_returned_capture_raw_placeholder_carrier_label": "SECOND_DEVICE_LABEL_TO_FILL",
        "selected_returned_capture_raw_placeholder_carrier_type": "Mac/Linux/etc_TO_FILL",
        "selected_returned_capture_placeholder_fields_unrepaired": True,
        "selected_returned_capture_zero_exit_code_not_success": True,
        "selected_returned_capture_ok_not_verification": True,
        "selected_returned_capture_not_cross_carrier_proof": True,
        "selected_second_carrier_output_capture_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_output_capture/"
            "portable_source_body_verification_second_carrier_output_capture_"
            "reference_review_001__portable_source_body_verification_second_"
            "carrier_output_capture_result.json"
        ),
        "selected_second_carrier_output_capture_result_outcome": EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        "selected_second_carrier_output_capture_failed_check_count": 0,
        "selected_second_carrier_output_capture_bounded_capture_recorded": True,
        "selected_second_carrier_output_capture_treated_capture_as_result": False,
        "selected_second_carrier_output_capture_treated_capture_as_success": False,
        "selected_second_carrier_output_capture_treated_capture_as_external_result": False,
        "selected_second_carrier_output_capture_treated_capture_as_cross_carrier_evidence": False,
        "reference_shaped_input_posture": True,
        "second_carrier_result_boundary_scope": sorted(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _false_non_claims(),
    }
    for key in POSTURE_KEYS:
        request[key] = True
    request.update(_sanitize(overrides))
    return _json_safe(request)

