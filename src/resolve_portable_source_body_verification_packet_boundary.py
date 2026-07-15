"""Bounded portable source-body verification packet boundary resolver.

This module records at most one packet-boundary posture downstream of the
clean local command-success basis. Packet boundary remains packet boundary
only. It is not a packet, packet emission, packet transfer, source transfer,
source receipt, second-carrier execution, second-carrier receipt, external
result, cross-carrier evidence, runtime, source, authority, currentness, final
completion, continuation, reusable permission, derivative reception, vessel
relation, another reception request, or follow-on work.

The resolver is self-contained, uses only the Python standard library, imports
no repo-local modules, runs no commands, mutates no upstream artifact, and never
returns a raw full prior artifact body.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationPacketBoundaryError(Exception):
    """Raised for explicit unreadable path or malformed JSON path inputs."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_packet_boundary"
RESULT_TYPE = "portable_source_body_verification_packet_boundary_result"
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_boundary"
)

CORE_QUESTION = (
    "Can the local command-success basis be bounded for one future portable "
    "verification packet step without creating packet emission, source transfer, "
    "source receipt, second-carrier execution, cross-carrier evidence, source, "
    "authority, currentness, final completion, runtime, continuation, reusable "
    "permission, derivative reception, vessel relation, another reception request, "
    "or follow-on work?"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

COMMAND_SUCCESS_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED"
COMMAND_SUCCESS_BOUNDARY_V3_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY_RECORDED"
)
COMMAND_RESULT_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED"
OUTPUT_CAPTURE_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED"
OUTPUT_REPORT_ARTIFACT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
)

SUPPORTED_PACKET_BOUNDARY_SCOPE = (
    "PACKET_BOUNDARY_ONLY",
    "ONE_FUTURE_PACKET_STEP_ONLY",
    "LOCAL_COMMAND_SUCCESS_BASIS_PRESERVED",
    "COMMAND_SUCCESS_NOT_PACKET_EMISSION",
    "COMMAND_SUCCESS_NOT_SOURCE",
    "COMMAND_SUCCESS_NOT_AUTHORITY",
    "COMMAND_SUCCESS_NOT_CURRENTNESS",
    "COMMAND_SUCCESS_NOT_FINAL_COMPLETION",
    "COMMAND_SUCCESS_NOT_CROSS_CARRIER_PROOF",
    "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_PRESERVED",
    "COMMAND_RESULT_V2_BASIS_PRESERVED",
    "OUTPUT_CAPTURE_V2_BASIS_PRESERVED",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_PRESERVED",
    "EXECUTION_TRACE_AUDIT_ONLY_PRESERVED",
    "PACKET_NOT_CREATED",
    "PACKET_NOT_EMITTED",
    "PACKET_TRANSFER_NOT_AUTHORIZED",
    "SOURCE_BODY_PACKET_NOT_CREATED",
    "MANIFEST_NOT_CREATED",
    "CHECKSUM_NOT_CREATED",
    "SIGNATURE_NOT_CREATED",
    "REPRODUCIBLE_ENVIRONMENT_NOT_DECLARED",
    "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED",
    "SECOND_CARRIER_RECEIPT_NOT_CREATED",
    "EXTERNAL_RESULT_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "PACKET_NOT_SOURCE",
    "PACKET_NOT_AUTHORITY",
    "PACKET_NOT_CURRENTNESS",
    "PACKET_NOT_FINAL_COMPLETION",
    "PACKET_NOT_RUNTIME",
    "PACKET_NOT_CONTINUATION",
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
    "NO_PACKET_EMISSION_INFERENCE",
    "NO_TRANSFER_INFERENCE",
    "NO_RECEIPT_INFERENCE",
    "NO_CROSS_CARRIER_EVIDENCE_INFERENCE",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_FINAL_COMPLETION_INFERENCE",
    "NO_RUNTIME_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_PACKET_AUTHORITY",
    "V1_COMMAND_SUCCESS_BOUNDARY_FAILURE_REMAINS_VISIBLE",
    "V2_COMMAND_SUCCESS_BOUNDARY_FAILURE_REMAINS_VISIBLE",
    "V1_COMMAND_RESULT_FAILURE_REMAINS_VISIBLE",
    "V1_OUTPUT_CAPTURE_FAILURE_REMAINS_VISIBLE",
    "COMMAND_REPORT_LINEAGE_NOT_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_NOT_COMMAND_RESULT_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_NOT_COMMAND_SUCCESS",
    "COMMAND_REPORT_LINEAGE_NOT_SOURCE",
    "COMMAND_REPORT_LINEAGE_NOT_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_NOT_CURRENTNESS",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
)

SELECTED_BASIS_KEYS = (
    "selected_command_success_basis",
    "selected_command_success_terminal_summary_basis",
    "selected_command_success_spec_basis",
    "selected_command_success_boundary_v3_basis",
    "selected_command_result_v2_basis",
    "selected_output_capture_v2_basis",
    "selected_command_output_report_artifact_basis",
    "selected_command_execution_basis",
    "selected_command_report_lineage_basis",
    "selected_predecessor_failure_basis",
)

POSTURE_KEYS = (
    "packet_boundary_only_posture",
    "one_future_packet_step_posture",
    "local_command_success_basis_preserved_posture",
    "command_success_not_packet_emission_posture",
    "packet_not_created_posture",
    "packet_not_emitted_posture",
    "packet_transfer_not_authorized_posture",
    "second_carrier_execution_not_authorized_posture",
    "second_carrier_receipt_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "final_completion_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "hidden_repo_state_not_used_as_packet_authority_posture",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "packet_created",
    "packet_emitted",
    "packet_transferred",
    "source_body_packet_created",
    "manifest_created",
    "checksum_created",
    "signature_created",
    "reproducible_environment_declared",
    "second_carrier_execution_created",
    "second_carrier_receipt_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "command_success_treated_as_packet_emission",
    "command_success_authorized_packet_creation",
    "command_success_authorized_packet_emission",
    "command_success_authorized_packet_transfer",
    "command_success_authorized_second_carrier_execution",
    "command_success_authorized_cross_carrier_evidence_review",
    "packet_treated_as_source",
    "packet_treated_as_authority",
    "packet_treated_as_currentness",
    "packet_treated_as_final_completion",
    "packet_treated_as_runtime",
    "packet_treated_as_cross_carrier_proof",
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
    "consumed_request_reopened",
    "authorization_token_reused",
    "hidden_repo_state_used_as_packet_authority",
    "artifact_existence_treated_as_packet_authority",
    "artifact_path_treated_as_currentness",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
)

EXTRA_FALSE_NON_CLAIMS = (
    "command_success_treated_as_source",
    "command_success_treated_as_authority",
    "command_success_treated_as_currentness",
    "command_success_treated_as_final_completion",
    "command_success_treated_as_cross_carrier_proof",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "full_prior_artifacts_embedded",
    "full_prior_artifact_body_emitted",
    "predecessor_failures_repaired",
    "predecessor_failures_hidden",
    "predecessor_failures_claimed_passed",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "packet_boundary_recorded",
    "one_future_packet_step_declared",
    "local_command_success_basis_preserved",
    "command_success_not_packet_emission",
    "packet_not_created",
    "packet_not_emitted",
    "packet_transfer_not_authorized",
    "second_carrier_execution_not_authorized",
    "second_carrier_receipt_not_created",
    "cross_carrier_evidence_not_created",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "final_completion_not_created",
    "runtime_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "hidden_repo_state_not_used_as_packet_authority",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

PUBLIC_BLOCK_CODES = frozenset(
    {
        "DECLARED_PACKET_BOUNDARY_REQUEST_MALFORMED",
        "DECLARED_PACKET_BOUNDARY_REQUEST_UNREADABLE",
        "PACKET_BOUNDARY_QUESTION_UNDECLARED",
        "PACKET_BOUNDARY_INTENT_UNSUPPORTED",
        "PACKET_BOUNDARY_EXPLICIT_BLOCK_INTENT",
        "COMMAND_SUCCESS_TERMINAL_SUMMARY_BASIS_MISSING",
        "COMMAND_SUCCESS_SPEC_BASIS_MISSING",
        "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_MISSING",
        "COMMAND_RESULT_V2_BASIS_MISSING",
        "OUTPUT_CAPTURE_V2_BASIS_MISSING",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING",
        "COMMAND_EXECUTION_BASIS_MISSING",
        "COMMAND_REPORT_LINEAGE_BASIS_MISSING",
        "PREDECESSOR_FAILURE_BASIS_MISSING",
        "COMMAND_SUCCESS_BASIS_MISSING",
        "COMMAND_SUCCESS_NOT_RECORDED",
        "COMMAND_SUCCESS_FAILED_CHECKS_PRESENT",
        "COMMAND_SUCCESS_VERSION_NOT_0_1_0",
        "COMMAND_SUCCESS_BOUNDED_SUCCESS_MISSING",
        "COMMAND_SUCCESS_TREATED_AS_PACKET_EMISSION",
        "COMMAND_SUCCESS_TREATED_AS_SOURCE",
        "COMMAND_SUCCESS_TREATED_AS_AUTHORITY",
        "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
        "COMMAND_SUCCESS_TREATED_AS_CROSS_CARRIER_PROOF",
        "COMMAND_SUCCESS_AUTHORIZED_PACKET_CREATION",
        "COMMAND_SUCCESS_AUTHORIZED_PACKET_EMISSION",
        "COMMAND_SUCCESS_AUTHORIZED_PACKET_TRANSFER",
        "COMMAND_SUCCESS_AUTHORIZED_SECOND_CARRIER_EXECUTION",
        "COMMAND_SUCCESS_AUTHORIZED_CROSS_CARRIER_EVIDENCE_REVIEW",
        "COMMAND_SUCCESS_BOUNDARY_V3_NOT_RECORDED",
        "COMMAND_RESULT_V2_NOT_RECORDED",
        "OUTPUT_CAPTURE_V2_NOT_RECORDED",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED",
        "EXECUTION_TRACE_NOT_AUDIT_ONLY",
        "COMMAND_REPORT_LINEAGE_NOT_LINEAGE_ONLY",
        "PREDECESSOR_FAILURE_EVIDENCE_NOT_VISIBLE",
        "PACKET_BOUNDARY_ONLY_POSTURE_MISSING",
        "ONE_FUTURE_PACKET_STEP_POSTURE_MISSING",
        "LOCAL_COMMAND_SUCCESS_BASIS_PRESERVED_POSTURE_MISSING",
        "COMMAND_SUCCESS_NOT_PACKET_EMISSION_POSTURE_MISSING",
        "PACKET_NOT_CREATED_POSTURE_MISSING",
        "PACKET_NOT_EMITTED_POSTURE_MISSING",
        "PACKET_TRANSFER_NOT_AUTHORIZED_POSTURE_MISSING",
        "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED_POSTURE_MISSING",
        "SECOND_CARRIER_RECEIPT_NOT_CREATED_POSTURE_MISSING",
        "CROSS_CARRIER_EVIDENCE_NOT_CREATED_POSTURE_MISSING",
        "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
        "SELECTED_BASIS_REFERENCE_SHAPE_POSTURE_MISSING",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED_POSTURE_MISSING",
        "HIDDEN_REPO_STATE_NOT_USED_AS_PACKET_AUTHORITY_POSTURE_MISSING",
        "PACKET_ALREADY_CREATED",
        "PACKET_ALREADY_EMITTED",
        "PACKET_ALREADY_TRANSFERRED",
        "SECOND_CARRIER_EXECUTION_ALREADY_CREATED",
        "SECOND_CARRIER_RECEIPT_ALREADY_CREATED",
        "EXTERNAL_RESULT_ALREADY_CREATED",
        "CROSS_CARRIER_EVIDENCE_ALREADY_CREATED",
        "SOURCE_BODY_PACKET_ALREADY_CREATED",
        "MANIFEST_ALREADY_CREATED",
        "CHECKSUM_ALREADY_CREATED",
        "SIGNATURE_ALREADY_CREATED",
        "REPRODUCIBLE_ENVIRONMENT_ALREADY_DECLARED",
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
        "PACKET_TREATED_AS_SOURCE",
        "PACKET_TREATED_AS_AUTHORITY",
        "PACKET_TREATED_AS_CURRENTNESS",
        "PACKET_TREATED_AS_FINAL_COMPLETION",
        "PACKET_TREATED_AS_RUNTIME",
        "PACKET_TREATED_AS_CROSS_CARRIER_PROOF",
        "ARTIFACT_EXISTENCE_TREATED_AS_PACKET_AUTHORITY",
        "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
        "HIDDEN_REPO_STATE_USED_AS_PACKET_AUTHORITY",
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_COMMAND_RESULT_AUTHORITY",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_COMMAND_SUCCESS",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
        "CONSUMED_REQUEST_REOPENED",
        "AUTHORIZATION_TOKEN_REUSED",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
        "SOURCE_TRANSFER_OCCURRED",
        "SOURCE_RECEIPT_OCCURRED",
        "RECEPTION_AUTHORIZATION_CREATED",
        "FULL_PRIOR_ARTIFACTS_EMBEDDED",
        "ARTIFACTS_MUTATED",
        "MUTATION_PERFORMED",
        "REPLAY_PERFORMED",
        "MERGE_PERFORMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "UNSUPPORTED_PACKET_BOUNDARY_SCOPE",
    }
)
BLOCK_CODES = PUBLIC_BLOCK_CODES

RAW_BODY_KEYS = frozenset(
    {
        "raw_body",
        "raw_full_body",
        "full_body",
        "artifact_body",
        "full_prior_artifact_body",
        "raw_prior_artifact_body",
        "raw_full_prior_artifact_body",
        "raw_command_success_body",
        "raw_command_success_boundary_body",
        "raw_packet_body",
        "raw_packet_artifact_body",
        "raw_packet_boundary_body",
        "raw_command_result_body",
        "raw_result_body",
        "raw_report_body",
        "raw_output_body",
        "stdout",
        "stderr",
        "process_output",
        "raw_process_output",
        "command_output_body",
        "report_body",
        "result_body",
        "success_body",
        "source_body",
        "source_body_packet",
        "authority_body",
        "currentness_claim",
        "final_completion_claim",
        "packet_artifact_body",
        "external_result_body",
        "cross_carrier_evidence_body",
    }
)
RAW_SENTINELS = (
    "RAW_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_SUCCESS_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_SUCCESS_BOUNDARY_BODY_MUST_NOT_RETURN",
    "MUST_NOT_RETURN",
)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _safe_text(value: Any) -> str:
    text = str(value)
    if any(sentinel in text for sentinel in RAW_SENTINELS):
        return "[omitted_raw_body_sentinel]"
    return text


def _raw_key(key: str) -> bool:
    lowered = key.lower()
    if lowered in RAW_BODY_KEYS:
        return True
    if lowered.endswith("_raw_body") or lowered.endswith("_full_body"):
        return True
    return lowered.endswith("_body") and not lowered.endswith(
        (
            "_not_invented",
            "_absent_or_bounded",
            "_basis",
            "_posture",
            "_preserved",
            "_returned",
            "_emitted",
            "_embedded",
            "_created",
        )
    )


def _json_safe(value: Any) -> Any:
    if isinstance(value, Mapping):
        cleaned: dict[str, Any] = {}
        for key, item in value.items():
            safe_key = _safe_text(key)
            cleaned[safe_key] = "[omitted_raw_body]" if _raw_key(safe_key) else _json_safe(item)
        return cleaned
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [_json_safe(item) for item in sorted(value, key=str)]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        return _safe_text(value)
    if isinstance(value, (int, float, bool)) or value is None:
        return value
    return _safe_text(value)


def _basis(request: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = request.get(key)
    return value if isinstance(value, Mapping) else {}


def _value(
    request: Mapping[str, Any],
    basis_key: str,
    names: Sequence[str],
    shortcuts: Sequence[str] = (),
    default: Any = None,
) -> Any:
    for shortcut in shortcuts:
        if shortcut in request:
            return request[shortcut]
    basis = _basis(request, basis_key)
    for name in names:
        if name in basis:
            return basis[name]
    for container_key in ("metadata", "summary", "command_success_statement"):
        container = basis.get(container_key)
        if isinstance(container, Mapping):
            for name in names:
                if name in container:
                    return container[name]
    return default


def _as_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return None
    return None


def _declared(value: Any) -> bool:
    if isinstance(value, Mapping):
        return (
            bool(value)
            and value.get("declared", True) is not False
            and value.get("basis_declared", True) is not False
        )
    return value is not None


def _basis_declared(request: Mapping[str, Any], key: str) -> bool:
    return _declared(request.get(key))


def _true(
    request: Mapping[str, Any],
    key: str,
    names: Sequence[str],
    shortcuts: Sequence[str] = (),
) -> bool:
    return _value(request, key, names, shortcuts) is True


def _false(
    request: Mapping[str, Any],
    key: str,
    names: Sequence[str],
    shortcuts: Sequence[str] = (),
    default: Any = False,
) -> bool:
    return _value(request, key, names, shortcuts, default) is False


def _check(name: str, passed: bool, expected: str, actual: Any, code: str) -> dict[str, Any]:
    return {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": expected,
        "actual_posture": _json_safe(actual),
        ("failure_code" if passed else "block_code"): None if passed else code,
    }


def _failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            return str(check.get("block_code") or check.get("failure_code"))
    return None


def _scope_values(request: Mapping[str, Any]) -> list[str]:
    value = request.get("packet_boundary_scope", [])
    if isinstance(value, str):
        return [value]
    if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)):
        return [str(item) for item in value]
    return []


def _non_claims_from_request(request: Mapping[str, Any]) -> Mapping[str, Any]:
    value = request.get("declared_non_claims")
    if isinstance(value, Mapping):
        return value
    value = request.get("non_claims")
    if isinstance(value, Mapping):
        return value
    return {}


def _safe_basis_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    raw = request.get(key)
    if isinstance(raw, Mapping):
        section = _json_safe(raw)
    elif raw is not None:
        section = {"basis_reference": _json_safe(raw)}
    else:
        section = {"declared": False}
    section.setdefault("basis_label", key)
    section.setdefault("declared", raw is not None)
    section.setdefault("basis_only", True)
    section.setdefault("reference_shaped", True)
    section.setdefault("selected_basis_reference_shape_preserved", True)
    section.setdefault("full_prior_artifact_body_embedded", False)
    section.setdefault("raw_full_prior_artifact_body_returned", False)
    section.setdefault("hidden_repo_state_used_as_packet_authority", False)
    return section


def _posture_section(request: Mapping[str, Any], key: str, recorded: bool) -> dict[str, Any]:
    raw = request.get(key)
    if isinstance(raw, Mapping):
        section = _json_safe(raw)
    elif raw is not None:
        section = {"declared": bool(raw), "posture_value": _json_safe(raw)}
    else:
        section = {"declared": False}
    section.setdefault("posture_label", key)
    section.setdefault("packet_boundary_posture_only", True)
    section.setdefault("recorded_outcome_only", recorded)
    section.setdefault("packet_created", False)
    section.setdefault("packet_emitted", False)
    section.setdefault("packet_transferred", False)
    section.setdefault("second_carrier_execution_created", False)
    section.setdefault("cross_carrier_evidence_created", False)
    section.setdefault("source_created", False)
    section.setdefault("authority_created", False)
    section.setdefault("currentness_created", False)
    section.setdefault("final_completion_claimed", False)
    section.setdefault("runtime_hosting_created", False)
    section.setdefault("follow_on_work_authorized", False)
    return section


def _non_claims_false(request: Mapping[str, Any]) -> bool:
    non_claims = _non_claims_from_request(request)
    return all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _all_selected_basis_reference_shaped(request: Mapping[str, Any]) -> bool:
    if request.get("reference_shaped_input_posture") is False:
        return False
    for key in SELECTED_BASIS_KEYS:
        if _value(
            request,
            key,
            ("reference_shaped", "selected_basis_reference_shape_preserved"),
            default=True,
        ) is False:
            return False
    return True


def _all_raw_full_prior_body_not_returned(request: Mapping[str, Any]) -> bool:
    for key in SELECTED_BASIS_KEYS:
        if _value(
            request,
            key,
            ("raw_full_prior_artifact_body_returned", "full_prior_artifact_body_emitted"),
            default=False,
        ) is True:
            return False
    return True


def _build_checks(request: Mapping[str, Any] | None) -> list[dict[str, Any]]:
    if not isinstance(request, Mapping):
        return [
            _check(
                "declared packet boundary request is mapping",
                False,
                "JSON object mapping",
                type(request).__name__,
                "DECLARED_PACKET_BOUNDARY_REQUEST_MALFORMED",
            )
        ]

    success = "selected_command_success_basis"
    terminal_summary = "selected_command_success_terminal_summary_basis"
    success_spec = "selected_command_success_spec_basis"
    success_boundary_v3 = "selected_command_success_boundary_v3_basis"
    result_v2 = "selected_command_result_v2_basis"
    capture_v2 = "selected_output_capture_v2_basis"
    report_artifact = "selected_command_output_report_artifact_basis"
    execution = "selected_command_execution_basis"
    lineage = "selected_command_report_lineage_basis"
    predecessor = "selected_predecessor_failure_basis"
    checks: list[dict[str, Any]] = []

    checks.append(
        _check(
            "packet boundary question declared",
            request.get("packet_boundary_question") == CORE_QUESTION,
            CORE_QUESTION,
            request.get("packet_boundary_question"),
            "PACKET_BOUNDARY_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "packet boundary intent supported",
            request.get("packet_boundary_intent") in SUPPORTED_INTENTS,
            str(SUPPORTED_INTENTS),
            request.get("packet_boundary_intent"),
            "PACKET_BOUNDARY_INTENT_UNSUPPORTED",
        )
    )
    if request.get("packet_boundary_intent") == INTENT_BLOCK:
        checks.append(
            _check(
                "packet boundary explicit block intent absent",
                False,
                "record or do-not-record intent",
                request.get("packet_boundary_intent"),
                "PACKET_BOUNDARY_EXPLICIT_BLOCK_INTENT",
            )
        )

    unsupported_scope = [
        value for value in _scope_values(request) if value not in SUPPORTED_PACKET_BOUNDARY_SCOPE
    ]
    checks.append(
        _check(
            "packet boundary scope supported",
            bool(_scope_values(request)) and not unsupported_scope,
            "supported packet boundary scope values only",
            {"values": _scope_values(request), "unsupported": unsupported_scope},
            "UNSUPPORTED_PACKET_BOUNDARY_SCOPE",
        )
    )

    declared_basis_codes = (
        (terminal_summary, "COMMAND_SUCCESS_TERMINAL_SUMMARY_BASIS_MISSING"),
        (success, "COMMAND_SUCCESS_BASIS_MISSING"),
        (success_spec, "COMMAND_SUCCESS_SPEC_BASIS_MISSING"),
        (success_boundary_v3, "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_MISSING"),
        (result_v2, "COMMAND_RESULT_V2_BASIS_MISSING"),
        (capture_v2, "OUTPUT_CAPTURE_V2_BASIS_MISSING"),
        (report_artifact, "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING"),
        (execution, "COMMAND_EXECUTION_BASIS_MISSING"),
        (lineage, "COMMAND_REPORT_LINEAGE_BASIS_MISSING"),
        (predecessor, "PREDECESSOR_FAILURE_BASIS_MISSING"),
    )
    for key, code in declared_basis_codes:
        checks.append(
            _check(
                f"{key} declared",
                _basis_declared(request, key),
                f"{key} declared as reference-shaped basis only",
                request.get(key),
                code,
            )
        )

    checks.extend(
        [
            _check(
                "command success outcome recorded",
                _value(
                    request,
                    success,
                    ("outcome", "result_outcome"),
                    ("selected_command_success_result_outcome",),
                )
                == COMMAND_SUCCESS_RECORDED,
                COMMAND_SUCCESS_RECORDED,
                _value(
                    request,
                    success,
                    ("outcome", "result_outcome"),
                    ("selected_command_success_result_outcome",),
                ),
                "COMMAND_SUCCESS_NOT_RECORDED",
            ),
            _check(
                "command success version 0.1.0",
                _value(
                    request,
                    success,
                    ("result_version", "version"),
                    ("selected_command_success_result_version",),
                )
                == "0.1.0",
                "0.1.0",
                _value(
                    request,
                    success,
                    ("result_version", "version"),
                    ("selected_command_success_result_version",),
                ),
                "COMMAND_SUCCESS_VERSION_NOT_0_1_0",
            ),
            _check(
                "command success failed check count zero",
                _as_int(
                    _value(
                        request,
                        success,
                        ("failed_check_count",),
                        ("selected_command_success_failed_check_count",),
                    )
                )
                == 0,
                "0",
                _value(
                    request,
                    success,
                    ("failed_check_count",),
                    ("selected_command_success_failed_check_count",),
                ),
                "COMMAND_SUCCESS_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "command success bounded success recorded",
                _true(
                    request,
                    success,
                    ("bounded_command_success_recorded", "command_success_recorded"),
                    ("selected_command_success_bounded_success_recorded",),
                ),
                "one bounded command success recorded",
                _value(
                    request,
                    success,
                    ("bounded_command_success_recorded", "command_success_recorded"),
                    ("selected_command_success_bounded_success_recorded",),
                ),
                "COMMAND_SUCCESS_BOUNDED_SUCCESS_MISSING",
            ),
            _check(
                "command success boundary v3 basis recorded",
                _value(request, success_boundary_v3, ("outcome", "result_outcome"))
                in (None, COMMAND_SUCCESS_BOUNDARY_V3_RECORDED)
                or _true(request, success, ("command_success_boundary_v3_basis_preserved",)),
                COMMAND_SUCCESS_BOUNDARY_V3_RECORDED,
                _value(request, success_boundary_v3, ("outcome", "result_outcome")),
                "COMMAND_SUCCESS_BOUNDARY_V3_NOT_RECORDED",
            ),
            _check(
                "command result v2 basis recorded",
                _value(request, result_v2, ("outcome", "result_outcome"))
                in (None, COMMAND_RESULT_V2_RECORDED)
                or _true(request, success, ("command_result_v2_basis_preserved",)),
                COMMAND_RESULT_V2_RECORDED,
                _value(request, result_v2, ("outcome", "result_outcome")),
                "COMMAND_RESULT_V2_NOT_RECORDED",
            ),
            _check(
                "output capture v2 basis recorded",
                _value(request, capture_v2, ("outcome", "result_outcome"))
                in (None, OUTPUT_CAPTURE_V2_RECORDED)
                or _true(request, success, ("output_capture_v2_basis_preserved",)),
                OUTPUT_CAPTURE_V2_RECORDED,
                _value(request, capture_v2, ("outcome", "result_outcome")),
                "OUTPUT_CAPTURE_V2_NOT_RECORDED",
            ),
            _check(
                "command output/report artifact basis recorded",
                _value(request, report_artifact, ("outcome", "result_outcome"))
                in (None, OUTPUT_REPORT_ARTIFACT_RECORDED)
                or _true(request, success, ("command_output_report_artifact_basis_preserved",)),
                OUTPUT_REPORT_ARTIFACT_RECORDED,
                _value(request, report_artifact, ("outcome", "result_outcome")),
                "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED",
            ),
            _check(
                "execution trace audit-only",
                _true(
                    request,
                    execution,
                    ("execution_trace_audit_only", "execution_trace_audit_only_preserved"),
                )
                or _true(request, success, ("execution_trace_audit_only_preserved",)),
                "execution trace audit-only",
                _value(
                    request,
                    execution,
                    ("execution_trace_audit_only", "execution_trace_audit_only_preserved"),
                ),
                "EXECUTION_TRACE_NOT_AUDIT_ONLY",
            ),
            _check(
                "command report lineage lineage-only",
                _value(request, lineage, ("lineage_only",), default=True) is True,
                "command report lineage remains lineage only",
                _value(request, lineage, ("lineage_only",), default=True),
                "COMMAND_REPORT_LINEAGE_NOT_LINEAGE_ONLY",
            ),
            _check(
                "predecessor failure evidence visible and unrepaired",
                _value(request, predecessor, ("predecessor_failures_visible",), default=True)
                is True
                and _value(request, predecessor, ("predecessor_failures_repaired",), default=False)
                is False
                and _value(request, predecessor, ("predecessor_failures_hidden",), default=False)
                is False
                and _value(
                    request,
                    predecessor,
                    ("predecessor_failures_claimed_passed",),
                    default=False,
                )
                is False,
                "predecessor failures visible and unrepaired",
                request.get(predecessor),
                "PREDECESSOR_FAILURE_EVIDENCE_NOT_VISIBLE",
            ),
        ]
    )

    for field, code in (
        ("command_success_treated_as_packet_emission", "COMMAND_SUCCESS_TREATED_AS_PACKET_EMISSION"),
        ("command_success_treated_as_source", "COMMAND_SUCCESS_TREATED_AS_SOURCE"),
        ("command_success_treated_as_authority", "COMMAND_SUCCESS_TREATED_AS_AUTHORITY"),
        ("command_success_treated_as_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
        ("command_success_treated_as_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
        ("command_success_treated_as_cross_carrier_proof", "COMMAND_SUCCESS_TREATED_AS_CROSS_CARRIER_PROOF"),
        ("command_success_authorized_packet_creation", "COMMAND_SUCCESS_AUTHORIZED_PACKET_CREATION"),
        ("command_success_authorized_packet_emission", "COMMAND_SUCCESS_AUTHORIZED_PACKET_EMISSION"),
        ("command_success_authorized_packet_transfer", "COMMAND_SUCCESS_AUTHORIZED_PACKET_TRANSFER"),
        ("command_success_authorized_second_carrier_execution", "COMMAND_SUCCESS_AUTHORIZED_SECOND_CARRIER_EXECUTION"),
        ("command_success_authorized_cross_carrier_evidence_review", "COMMAND_SUCCESS_AUTHORIZED_CROSS_CARRIER_EVIDENCE_REVIEW"),
    ):
        checks.append(
            _check(
                f"command success {field} false",
                _false(
                    request,
                    success,
                    (field,),
                    (f"selected_{field}",),
                ),
                f"{field} false",
                _value(request, success, (field,), (f"selected_{field}",), False),
                code,
            )
        )

    posture_codes = {
        "packet_boundary_only_posture": "PACKET_BOUNDARY_ONLY_POSTURE_MISSING",
        "one_future_packet_step_posture": "ONE_FUTURE_PACKET_STEP_POSTURE_MISSING",
        "local_command_success_basis_preserved_posture": "LOCAL_COMMAND_SUCCESS_BASIS_PRESERVED_POSTURE_MISSING",
        "command_success_not_packet_emission_posture": "COMMAND_SUCCESS_NOT_PACKET_EMISSION_POSTURE_MISSING",
        "packet_not_created_posture": "PACKET_NOT_CREATED_POSTURE_MISSING",
        "packet_not_emitted_posture": "PACKET_NOT_EMITTED_POSTURE_MISSING",
        "packet_transfer_not_authorized_posture": "PACKET_TRANSFER_NOT_AUTHORIZED_POSTURE_MISSING",
        "second_carrier_execution_not_authorized_posture": "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED_POSTURE_MISSING",
        "second_carrier_receipt_not_created_posture": "SECOND_CARRIER_RECEIPT_NOT_CREATED_POSTURE_MISSING",
        "cross_carrier_evidence_not_created_posture": "CROSS_CARRIER_EVIDENCE_NOT_CREATED_POSTURE_MISSING",
        "selected_basis_reference_shape_posture": "SELECTED_BASIS_REFERENCE_SHAPE_POSTURE_MISSING",
        "raw_full_prior_artifact_body_not_returned_posture": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED_POSTURE_MISSING",
        "hidden_repo_state_not_used_as_packet_authority_posture": "HIDDEN_REPO_STATE_NOT_USED_AS_PACKET_AUTHORITY_POSTURE_MISSING",
    }
    for key, code in posture_codes.items():
        checks.append(_check(f"{key} declared", _declared(request.get(key)), f"{key} declared", request.get(key), code))

    checks.append(
        _check(
            "no source authority currentness final completion runtime follow-on postures declared",
            all(
                _declared(request.get(key))
                for key in (
                    "source_not_created_posture",
                    "authority_not_created_posture",
                    "currentness_not_created_posture",
                    "final_completion_not_created_posture",
                    "runtime_not_created_posture",
                    "follow_on_work_not_authorized_posture",
                )
            ),
            "no source, authority, currentness, final completion, runtime, and follow-on postures declared",
            {
                key: request.get(key)
                for key in (
                    "source_not_created_posture",
                    "authority_not_created_posture",
                    "currentness_not_created_posture",
                    "final_completion_not_created_posture",
                    "runtime_not_created_posture",
                    "follow_on_work_not_authorized_posture",
                )
            },
            "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
        )
    )

    for field, code in (
        ("command_report_lineage_treated_as_current_report_artifact", "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT"),
        ("command_report_lineage_treated_as_command_result_authority", "COMMAND_REPORT_LINEAGE_TREATED_AS_COMMAND_RESULT_AUTHORITY"),
        ("command_report_lineage_treated_as_command_success", "COMMAND_REPORT_LINEAGE_TREATED_AS_COMMAND_SUCCESS"),
        ("command_report_lineage_treated_as_source", "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE"),
        ("command_report_lineage_treated_as_authority", "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY"),
        ("command_report_lineage_treated_as_currentness", "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS"),
    ):
        checks.append(
            _check(
                f"command report lineage {field} false",
                _false(request, lineage, (field,)),
                f"{field} false",
                _value(request, lineage, (field,), (), False),
                code,
            )
        )

    for posture_key, field, code in (
        ("packet_not_created_posture", "packet_created", "PACKET_ALREADY_CREATED"),
        ("packet_not_emitted_posture", "packet_emitted", "PACKET_ALREADY_EMITTED"),
        ("packet_transfer_not_authorized_posture", "packet_transferred", "PACKET_ALREADY_TRANSFERRED"),
        ("second_carrier_execution_not_authorized_posture", "second_carrier_execution_created", "SECOND_CARRIER_EXECUTION_ALREADY_CREATED"),
        ("second_carrier_receipt_not_created_posture", "second_carrier_receipt_created", "SECOND_CARRIER_RECEIPT_ALREADY_CREATED"),
        ("cross_carrier_evidence_not_created_posture", "cross_carrier_evidence_created", "CROSS_CARRIER_EVIDENCE_ALREADY_CREATED"),
        ("source_not_created_posture", "source_created", "SOURCE_CREATED"),
        ("authority_not_created_posture", "authority_created", "AUTHORITY_CREATED"),
        ("currentness_not_created_posture", "currentness_created", "CURRENTNESS_CREATED"),
        ("final_completion_not_created_posture", "final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
        ("runtime_not_created_posture", "runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
        ("continuation_not_authorized_posture", "continuation_authorized", "CONTINUATION_AUTHORIZED"),
        ("reusable_permission_not_created_posture", "reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
        ("follow_on_work_not_authorized_posture", "follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    ):
        checks.append(
            _check(
                f"{posture_key} keeps {field} false",
                _value(request, posture_key, (field,), default=False) is False,
                f"{field} false",
                _value(request, posture_key, (field,), default=False),
                code,
            )
        )

    checks.extend(
        [
            _check(
                "selected basis reference-shaped",
                _all_selected_basis_reference_shaped(request),
                "selected basis reference-shaped",
                {key: _value(request, key, ("reference_shaped", "selected_basis_reference_shape_preserved"), default=True) for key in SELECTED_BASIS_KEYS},
                "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
            ),
            _check(
                "raw full prior artifact body not returned",
                _all_raw_full_prior_body_not_returned(request),
                "raw full prior artifact body returned false",
                {key: _value(request, key, ("raw_full_prior_artifact_body_returned", "full_prior_artifact_body_emitted"), default=False) for key in SELECTED_BASIS_KEYS},
                "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
            ),
            _check(
                "hidden repo state not used as packet authority",
                _value(
                    request,
                    "hidden_repo_state_not_used_as_packet_authority_posture",
                    ("hidden_repo_state_used_as_packet_authority",),
                    ("hidden_repo_state_used_as_packet_authority",),
                    False,
                )
                is False,
                "hidden repo state used as packet authority false",
                _value(
                    request,
                    "hidden_repo_state_not_used_as_packet_authority_posture",
                    ("hidden_repo_state_used_as_packet_authority",),
                    ("hidden_repo_state_used_as_packet_authority",),
                    False,
                ),
                "HIDDEN_REPO_STATE_USED_AS_PACKET_AUTHORITY",
            ),
        ]
    )

    non_claims = _non_claims_from_request(request)
    checks.append(
        _check(
            "required non-claims remain false",
            _non_claims_false(request),
            "all required non-claims false",
            {key: non_claims.get(key) for key in REQUIRED_FALSE_NON_CLAIMS},
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )

    for field, code in (
        ("packet_created", "PACKET_ALREADY_CREATED"),
        ("packet_emitted", "PACKET_ALREADY_EMITTED"),
        ("packet_transferred", "PACKET_ALREADY_TRANSFERRED"),
        ("second_carrier_execution_created", "SECOND_CARRIER_EXECUTION_ALREADY_CREATED"),
        ("second_carrier_receipt_created", "SECOND_CARRIER_RECEIPT_ALREADY_CREATED"),
        ("external_result_created", "EXTERNAL_RESULT_ALREADY_CREATED"),
        ("cross_carrier_evidence_created", "CROSS_CARRIER_EVIDENCE_ALREADY_CREATED"),
        ("source_body_packet_created", "SOURCE_BODY_PACKET_ALREADY_CREATED"),
        ("manifest_created", "MANIFEST_ALREADY_CREATED"),
        ("checksum_created", "CHECKSUM_ALREADY_CREATED"),
        ("signature_created", "SIGNATURE_ALREADY_CREATED"),
        ("reproducible_environment_declared", "REPRODUCIBLE_ENVIRONMENT_ALREADY_DECLARED"),
        ("source_created", "SOURCE_CREATED"),
        ("authority_created", "AUTHORITY_CREATED"),
        ("currentness_created", "CURRENTNESS_CREATED"),
        ("final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
        ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
        ("deployment_created", "DEPLOYMENT_CREATED"),
        ("public_release_created", "PUBLIC_RELEASE_CREATED"),
        ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
        ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
        ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
        ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
        ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
        ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
        ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        ("packet_treated_as_source", "PACKET_TREATED_AS_SOURCE"),
        ("packet_treated_as_authority", "PACKET_TREATED_AS_AUTHORITY"),
        ("packet_treated_as_currentness", "PACKET_TREATED_AS_CURRENTNESS"),
        ("packet_treated_as_final_completion", "PACKET_TREATED_AS_FINAL_COMPLETION"),
        ("packet_treated_as_runtime", "PACKET_TREATED_AS_RUNTIME"),
        ("packet_treated_as_cross_carrier_proof", "PACKET_TREATED_AS_CROSS_CARRIER_PROOF"),
        ("artifact_existence_treated_as_packet_authority", "ARTIFACT_EXISTENCE_TREATED_AS_PACKET_AUTHORITY"),
        ("artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
        ("hidden_repo_state_used_as_packet_authority", "HIDDEN_REPO_STATE_USED_AS_PACKET_AUTHORITY"),
        ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
        ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
        ("raw_full_prior_artifact_body_returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
        ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
    ):
        checks.append(
            _check(
                f"non-claim {field} false",
                non_claims.get(field) is False,
                f"{field} false",
                non_claims.get(field),
                code,
            )
        )

    for field, code in (
        ("command_success_treated_as_source", "COMMAND_SUCCESS_TREATED_AS_SOURCE"),
        ("command_success_treated_as_authority", "COMMAND_SUCCESS_TREATED_AS_AUTHORITY"),
        ("command_success_treated_as_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
        ("command_success_treated_as_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
        ("command_success_treated_as_cross_carrier_proof", "COMMAND_SUCCESS_TREATED_AS_CROSS_CARRIER_PROOF"),
        ("source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
        ("source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
        ("reception_authorization_created", "RECEPTION_AUTHORIZATION_CREATED"),
        ("full_prior_artifacts_embedded", "FULL_PRIOR_ARTIFACTS_EMBEDDED"),
        ("full_prior_artifact_body_emitted", "FULL_PRIOR_ARTIFACT_BODY_EMITTED"),
        ("predecessor_failures_repaired", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("predecessor_failures_hidden", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("predecessor_failures_claimed_passed", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("mutation_performed", "MUTATION_PERFORMED"),
        ("replay_performed", "REPLAY_PERFORMED"),
        ("merge_performed", "MERGE_PERFORMED"),
    ):
        if field in non_claims:
            checks.append(
                _check(
                    f"non-claim {field} false",
                    non_claims.get(field) is False,
                    f"{field} false",
                    non_claims.get(field),
                    code,
                )
            )

    return checks


def _statement(recorded: bool) -> dict[str, Any]:
    statement = {key: recorded for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update({key: False for key in REQUIRED_FALSE_NON_CLAIMS})
    statement.update({key: False for key in EXTRA_FALSE_NON_CLAIMS})
    statement.update(
        {
            "local_command_success_remains_local_command_success_posture_only": True,
            "command_success_boundary_v3_remains_boundary_basis_only": True,
            "command_result_v2_remains_command_result_posture_only": True,
            "output_capture_v2_remains_output_capture_posture_only": True,
            "command_output_report_artifact_remains_artifact_posture_only": True,
            "execution_trace_remains_audit_only": True,
            "packet_boundary_is_not_packet": True,
            "packet_boundary_is_not_packet_emission": True,
            "packet_boundary_is_not_source_transfer": True,
            "packet_boundary_is_not_source_receipt": True,
            "packet_boundary_is_not_second_carrier_execution": True,
            "packet_boundary_is_not_cross_carrier_evidence": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
        }
    )
    return statement


def _non_meaning() -> dict[str, bool]:
    return {
        "packet_exists": False,
        "packet_was_emitted": False,
        "packet_was_copied_to_another_device": False,
        "packet_was_received_by_another_carrier": False,
        "another_device_executed_verification": False,
        "external_result_exists": False,
        "cross_carrier_evidence_exists": False,
        "source_body_packet_exists": False,
        "manifest_exists": False,
        "checksum_exists": False,
        "signature_exists": False,
        "reproducible_environment_declared": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "reception_authorization_exists": False,
        "source_exists": False,
        "authority_exists": False,
        "currentness_exists": False,
        "final_completion_exists": False,
        "runtime_exists": False,
        "deployment_exists": False,
        "public_release_exists": False,
        "continuation_authorized": False,
        "reusable_permission_exists": False,
        "follow_on_work_authorized": False,
        "command_success_became_packet_permission": False,
        "packet_boundary_became_packet_emission": False,
        "local_command_success_became_cross_carrier_proof": False,
        "artifact_path_became_packet_authority": False,
        "artifact_existence_became_source_standing": False,
        "local_repo_state_became_portable_packet_content": False,
        "hidden_repo_state_became_authority": False,
        "predecessor_failures_repaired_hidden_erased_or_claimed_passed": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "packet boundary test",
            "packet boundary live artifact",
            "packet artifact specification",
            "packet artifact resolver/test/live artifact",
            "packet emission",
            "manifest/checksum/signature implementation",
            "reproducible environment declaration",
            "second-device / second-carrier execution boundary",
            "second-device / second-carrier execution",
            "second-carrier output capture",
            "second-carrier result",
            "second-carrier success",
            "external result artifact",
            "cross-carrier evidence review",
            "line-level portable verification closure review",
            "source-body packet implementation",
            "source transfer",
            "source migration",
            "source receipt",
            "reception authorization",
            "derivative reception",
            "vessel relation",
            "adoption",
            "authority creation",
            "currentness creation",
            "operation permission",
            "receiving-context governance",
            "deployment readiness",
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


def _outcome(request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]) -> tuple[str, str | None]:
    code = _failed_code(checks)
    if code:
        return OUTCOME_BLOCKED, code
    if request.get("packet_boundary_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED, None
    if request.get("additional_basis_context") or request.get("requires_additional_basis"):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None
    return OUTCOME_RECORDED, None


def resolve_portable_source_body_verification_packet_boundary(
    declared_packet_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded packet boundary result without mutating inputs."""

    if isinstance(declared_packet_boundary_request, Mapping):
        request = copy.deepcopy(dict(declared_packet_boundary_request))
    else:
        request = {
            "packet_boundary_request_id": "malformed_packet_boundary_request",
            "packet_boundary_question": None,
            "packet_boundary_intent": None,
            "packet_boundary_scope": [],
            "declared_non_claims": {},
        }
    checks = _build_checks(request if isinstance(declared_packet_boundary_request, Mapping) else None)
    outcome, block_code = _outcome(request, checks)
    recorded = outcome == OUTCOME_RECORDED
    statement = _statement(recorded)
    metadata = {
        "portable_source_body_verification_packet_boundary_result_id": (
            f"{_safe_text(request.get('packet_boundary_request_id'))}"
            "__portable_source_body_verification_packet_boundary_result"
        ),
        "portable_source_body_verification_packet_boundary_result_type": RESULT_TYPE,
        "portable_source_body_verification_packet_boundary_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "packet_boundary_request_id": _safe_text(request.get("packet_boundary_request_id")),
        "passed_check_count": sum(1 for check in checks if check.get("passed")),
        "failed_check_count": sum(1 for check in checks if not check.get("passed")),
    }

    result: dict[str, Any] = {
        "portable_source_body_verification_packet_boundary_metadata": metadata,
        "declared_packet_boundary_question": {
            "packet_boundary_request_id": metadata["packet_boundary_request_id"],
            "question": _json_safe(request.get("packet_boundary_question")),
            "intent": _json_safe(request.get("packet_boundary_intent")),
            "core_question": CORE_QUESTION,
            "question_scope": "one future portable verification packet step boundary only",
        },
    }
    for key in SELECTED_BASIS_KEYS:
        result[key] = _safe_basis_section(request, key)
    for key in POSTURE_KEYS:
        result[key] = _posture_section(request, key, recorded)

    result.update(
        {
            "packet_boundary_scope": {
                "scope_values": _scope_values(request),
                "supported_scope_family": list(SUPPORTED_PACKET_BOUNDARY_SCOPE),
                "unsupported_scope_values": [
                    value for value in _scope_values(request) if value not in SUPPORTED_PACKET_BOUNDARY_SCOPE
                ],
            },
            "packet_boundary_checks": checks,
            "packet_boundary_statement": statement,
            "packet_boundary_non_meaning": _non_meaning(),
            "additional_basis_required": {
                "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                "missing_or_unclear_basis": _json_safe(request.get("additional_basis_context", [])) if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS else [],
                "basis_not_scheduled": True,
                "basis_not_authorized": True,
                "basis_not_executed": True,
                "packet_created": False,
                "packet_emitted": False,
                "source_created": False,
                "authority_created": False,
                "currentness_created": False,
                "final_completion_claimed": False,
                "cross_carrier_evidence_created": False,
                "follow_on_work_authorized": False,
            },
            "not_recorded_basis": {
                "not_recorded": outcome == OUTCOME_NOT_RECORDED,
                "not_recorded_reason": _json_safe(request.get("not_recorded_basis")) if outcome == OUTCOME_NOT_RECORDED else None,
                "prior_artifacts_mutated": False,
                "prior_artifacts_repaired": False,
                "next_work_authorized": False,
                "packet_created": False,
                "packet_emitted": False,
                "source_created": False,
                "authority_created": False,
                "currentness_created": False,
                "final_completion_claimed": False,
                "cross_carrier_evidence_created": False,
                "follow_on_work_authorized": False,
            },
            "what_remains_open": _what_remains_open(),
            "non_claims": {
                **{key: False for key in REQUIRED_FALSE_NON_CLAIMS},
                **{key: False for key in EXTRA_FALSE_NON_CLAIMS},
            },
            "outcome": outcome,
            "block": {
                "blocked": block_code is not None,
                "block_code": block_code,
                "block_reason": _json_safe(request.get("block_reason", block_code)),
            },
        }
    )
    result["portable_source_body_verification_packet_boundary_summary"] = (
        build_portable_source_body_verification_packet_boundary_summary(result)
    )
    return _json_safe(result)


def resolve_portable_source_body_verification_packet_boundary_from_path(
    declared_packet_boundary_request_path: Path | str,
) -> dict:
    """Resolve from an explicit JSON object request path."""

    path = Path(declared_packet_boundary_request_path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationPacketBoundaryError(
            f"Declared packet boundary request unreadable: {path}"
        ) from exc
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationPacketBoundaryError(
            f"Declared packet boundary request malformed JSON: {path}"
        ) from exc
    if not isinstance(parsed, Mapping):
        raise PortableSourceBodyVerificationPacketBoundaryError(
            "Declared packet boundary request path must contain a JSON object."
        )
    return resolve_portable_source_body_verification_packet_boundary(parsed)


def _section(result: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = result.get(key)
    return value if isinstance(value, Mapping) else {}


def build_portable_source_body_verification_packet_boundary_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build the public bounded summary surface."""

    metadata = _section(result, "portable_source_body_verification_packet_boundary_metadata")
    question = _section(result, "declared_packet_boundary_question")
    statement = _section(result, "packet_boundary_statement")
    non_claims = _section(result, "non_claims")
    block = _section(result, "block")
    checks = result.get("packet_boundary_checks", [])
    passed = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed"))
    failed = sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": metadata.get("packet_boundary_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "packet_boundary_recorded": statement.get("packet_boundary_recorded", False),
        "one_future_packet_step_declared": statement.get("one_future_packet_step_declared", False),
        "local_command_success_basis_preserved": statement.get("local_command_success_basis_preserved", False),
        "command_success_not_packet_emission": statement.get("command_success_not_packet_emission", False),
        "packet_not_created": statement.get("packet_not_created", False),
        "packet_not_emitted": statement.get("packet_not_emitted", False),
        "packet_transfer_not_authorized": statement.get("packet_transfer_not_authorized", False),
        "second_carrier_execution_not_authorized": statement.get("second_carrier_execution_not_authorized", False),
        "second_carrier_receipt_not_created": statement.get("second_carrier_receipt_not_created", False),
        "cross_carrier_evidence_not_created": statement.get("cross_carrier_evidence_not_created", False),
        "source_not_created": statement.get("source_not_created", False),
        "authority_not_created": statement.get("authority_not_created", False),
        "currentness_not_created": statement.get("currentness_not_created", False),
        "final_completion_not_created": statement.get("final_completion_not_created", False),
        "runtime_not_created": statement.get("runtime_not_created", False),
        "follow_on_work_not_authorized": statement.get("follow_on_work_not_authorized", False),
        "selected_basis_reference_shape_preserved": statement.get("selected_basis_reference_shape_preserved", False),
        "hidden_repo_state_not_used_as_packet_authority": statement.get("hidden_repo_state_not_used_as_packet_authority", False),
        "raw_full_prior_artifact_body_not_returned": statement.get("raw_full_prior_artifact_body_not_returned", False),
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked", False),
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed", False),
        "selected_command_success_outcome": _section(result, "selected_command_success_basis").get("outcome"),
        "selected_command_success_version": _section(result, "selected_command_success_basis").get("result_version"),
        "selected_command_success_failed_check_count": _section(result, "selected_command_success_basis").get("failed_check_count"),
        "no_packet_transfer_receipt_cross_carrier_evidence": non_claims.get("packet_created") is False
        and non_claims.get("packet_emitted") is False
        and non_claims.get("packet_transferred") is False
        and non_claims.get("second_carrier_receipt_created") is False
        and non_claims.get("cross_carrier_evidence_created") is False,
        "no_source_authority_currentness_final_completion_runtime": non_claims.get("source_created") is False
        and non_claims.get("authority_created") is False
        and non_claims.get("currentness_created") is False
        and non_claims.get("final_completion_claimed") is False
        and non_claims.get("runtime_hosting_created") is False,
        "no_deployment_public_release_follow_on": non_claims.get("deployment_created") is False
        and non_claims.get("public_release_created") is False
        and non_claims.get("follow_on_work_authorized") is False,
        "command_success_not_packet_permission": non_claims.get("command_success_treated_as_packet_emission") is False
        and non_claims.get("command_success_authorized_packet_creation") is False
        and non_claims.get("command_success_authorized_packet_emission") is False
        and non_claims.get("command_success_authorized_packet_transfer") is False,
        "hidden_repo_state_not_packet_authority": non_claims.get("hidden_repo_state_used_as_packet_authority") is False,
        "key_non_claims": _json_safe(non_claims),
    }


def _unique_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    counter = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{counter:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def write_portable_source_body_verification_packet_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a stable UTF-8 JSON result without overwriting prior artifacts."""

    metadata = _section(result, "portable_source_body_verification_packet_boundary_metadata")
    request_id = _safe_text(
        metadata.get(
            "packet_boundary_request_id",
            "portable_source_body_verification_packet_boundary_request",
        )
    )
    if output_path is None:
        output_path = OUTPUT_ROOT / f"{request_id}__portable_source_body_verification_packet_boundary_result.json"
    path = _unique_output_path(Path(output_path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_json_safe(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def _basis_stub(label: str, **overrides: Any) -> dict[str, Any]:
    basis = {
        "basis_label": label,
        "declared": True,
        "basis_only": True,
        "reference_shaped": True,
        "selected_basis_reference_shape_preserved": True,
        "full_prior_artifact_body_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
        "hidden_repo_state_used_as_packet_authority": False,
    }
    basis.update(overrides)
    return basis


def _posture_stub(label: str) -> dict[str, Any]:
    return {
        "posture_label": label,
        "declared": True,
        "packet_boundary_posture_only": True,
        "packet_created": False,
        "packet_emitted": False,
        "packet_transferred": False,
        "second_carrier_execution_created": False,
        "cross_carrier_evidence_created": False,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_claimed": False,
        "runtime_hosting_created": False,
        "follow_on_work_authorized": False,
    }


def build_declared_portable_source_body_verification_packet_boundary_request(
    packet_boundary_request_id: str = "portable_source_body_verification_packet_boundary_reference_review_001",
    packet_boundary_intent: str = INTENT_RECORD,
    selected_command_success_result_path: Path | str | None = None,
    selected_command_success_terminal_summary_path: Path | str | None = None,
) -> dict[str, Any]:
    """Build a reference-shaped declared request with required non-claims false."""

    request: dict[str, Any] = {
        "packet_boundary_request_id": packet_boundary_request_id,
        "packet_boundary_question": CORE_QUESTION,
        "packet_boundary_intent": packet_boundary_intent,
        "packet_boundary_scope": list(SUPPORTED_PACKET_BOUNDARY_SCOPE),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
    }
    request["selected_command_success_basis"] = _basis_stub(
        "selected_command_success_basis",
        path=_safe_text(selected_command_success_result_path) if selected_command_success_result_path else None,
        outcome=COMMAND_SUCCESS_RECORDED,
        result_version="0.1.0",
        failed_check_count=0,
        command_success_recorded=True,
        bounded_command_success_recorded=True,
        command_success_boundary_v3_basis_preserved=True,
        command_result_v2_basis_preserved=True,
        output_capture_v2_basis_preserved=True,
        command_output_report_artifact_basis_preserved=True,
        execution_trace_audit_only_preserved=True,
        command_success_treated_as_packet_emission=False,
        command_success_treated_as_source=False,
        command_success_treated_as_authority=False,
        command_success_treated_as_currentness=False,
        command_success_treated_as_final_completion=False,
        command_success_treated_as_cross_carrier_proof=False,
        command_success_authorized_packet_creation=False,
        command_success_authorized_packet_emission=False,
        command_success_authorized_packet_transfer=False,
        command_success_authorized_second_carrier_execution=False,
        command_success_authorized_cross_carrier_evidence_review=False,
        source_not_created=True,
        authority_not_created=True,
        currentness_not_created=True,
        final_completion_not_created=True,
        runtime_not_created=True,
        follow_on_work_not_authorized=True,
    )
    request["selected_command_success_terminal_summary_basis"] = _basis_stub(
        "selected_command_success_terminal_summary_basis",
        path=_safe_text(selected_command_success_terminal_summary_path) if selected_command_success_terminal_summary_path else "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_TERMINAL_SUMMARY_V0.md",
        terminal_summary_readability_basis_only=True,
        local_command_success_not_cross_carrier_proof=True,
    )
    request["selected_command_success_spec_basis"] = _basis_stub(
        "selected_command_success_spec_basis",
        path="spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_V0_MIN_SPEC.md",
    )
    request["selected_command_success_boundary_v3_basis"] = _basis_stub(
        "selected_command_success_boundary_v3_basis",
        outcome=COMMAND_SUCCESS_BOUNDARY_V3_RECORDED,
        result_version="0.3.0",
        failed_check_count=0,
        boundary_basis_only=True,
        command_success_boundary_v3_basis_preserved=True,
    )
    request["selected_command_result_v2_basis"] = _basis_stub(
        "selected_command_result_v2_basis",
        outcome=COMMAND_RESULT_V2_RECORDED,
        result_version="0.2.0",
        failed_check_count=0,
        command_result_v2_basis_preserved=True,
        command_result_v2_remains_command_result_posture_only=True,
    )
    request["selected_output_capture_v2_basis"] = _basis_stub(
        "selected_output_capture_v2_basis",
        outcome=OUTPUT_CAPTURE_V2_RECORDED,
        result_version="0.2.0",
        failed_check_count=0,
        output_capture_v2_basis_preserved=True,
        output_capture_v2_remains_output_capture_posture_only=True,
    )
    request["selected_command_output_report_artifact_basis"] = _basis_stub(
        "selected_command_output_report_artifact_basis",
        outcome=OUTPUT_REPORT_ARTIFACT_RECORDED,
        failed_check_count=0,
        command_output_report_artifact_basis_preserved=True,
        command_output_report_artifact_remains_artifact_posture_only=True,
    )
    request["selected_command_execution_basis"] = _basis_stub(
        "selected_command_execution_basis",
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED",
        failed_check_count=0,
        execution_trace_audit_only=True,
        execution_trace_audit_only_preserved=True,
    )
    request["selected_command_report_lineage_basis"] = _basis_stub(
        "selected_command_report_lineage_basis",
        lineage_only=True,
        command_report_lineage_treated_as_current_report_artifact=False,
        command_report_lineage_treated_as_command_result_authority=False,
        command_report_lineage_treated_as_command_success=False,
        command_report_lineage_treated_as_source=False,
        command_report_lineage_treated_as_authority=False,
        command_report_lineage_treated_as_currentness=False,
    )
    request["selected_predecessor_failure_basis"] = _basis_stub(
        "selected_predecessor_failure_basis",
        predecessor_failures_visible=True,
        predecessor_failures_repaired=False,
        predecessor_failures_hidden=False,
        predecessor_failures_claimed_passed=False,
        v1_command_success_boundary_failure_remains_visible=True,
        v2_command_success_boundary_failure_remains_visible=True,
        v1_command_result_failure_remains_visible=True,
        v1_output_capture_failure_remains_visible=True,
    )
    for key in POSTURE_KEYS:
        request[key] = _posture_stub(key)
    request["packet_not_created_posture"].update(packet_created=False)
    request["packet_not_emitted_posture"].update(packet_emitted=False)
    request["packet_transfer_not_authorized_posture"].update(packet_transferred=False)
    request["second_carrier_execution_not_authorized_posture"].update(
        second_carrier_execution_created=False
    )
    request["second_carrier_receipt_not_created_posture"].update(
        second_carrier_receipt_created=False
    )
    request["cross_carrier_evidence_not_created_posture"].update(
        cross_carrier_evidence_created=False
    )
    request["hidden_repo_state_not_used_as_packet_authority_posture"].update(
        hidden_repo_state_used_as_packet_authority=False
    )
    return request
